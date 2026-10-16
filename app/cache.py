"""Persistent cache for Tavily responses: one JSON file per request, with a time-to-live.

The key is the SHA-256 of the request body plus a hash of the Tavily key that made the request, so a
client's own key (BYOK) only ever sees responses fetched with that same key, and a key Tavily never
accepted can never be served from the cache. Only successful (HTTP 200) responses are stored. Files are
written atomically (temp file + rename), so several worker processes can share one directory. API keys
are never stored.

With an Archive (app/archive.py), every entry is also written to a durable SQLite database when it is
stored, and an entry that was never archived (written by an older version) is archived when it expires,
before it is deleted: the time-to-live cleans the cache, not the record of what was fetched."""
import asyncio
import contextlib
import fcntl
import hashlib
import json
import os
import tempfile
import time


ENRICHMENT_ACCOUNT = "openai-enrichment"  # the pseudo-account of cached detection / rephrasing calls


class TavilyCache:
    def __init__(self, directory, ttl_s, clock=time.time, archive=None):
        self.dir = directory
        self.ttl = ttl_s
        self.clock = clock
        self.archive = archive
        self.enabled = bool(directory) and ttl_s > 0
        self._writes = 0
        if self.enabled:
            os.makedirs(directory, exist_ok=True)

    @staticmethod
    def account_of(tavily_key):
        """The account an entry belongs to: a hash of the Tavily key, or the enrichment pseudo-account."""
        return tavily_key if tavily_key == ENRICHMENT_ACCOUNT else hashlib.sha256(tavily_key.encode()).hexdigest()[:16]

    @staticmethod
    def key(tavily_key, body):
        account = hashlib.sha256(tavily_key.encode()).hexdigest()[:16]
        canon = json.dumps({"account": account, "body": body}, sort_keys=True, ensure_ascii=False, separators=(",", ":"))
        return hashlib.sha256(canon.encode()).hexdigest()

    def _path(self, k):
        return os.path.join(self.dir, k[:2], k + ".json")

    @contextlib.asynccontextmanager
    async def lock(self, k, timeout_s):
        """Cross-process lock for one request key (an flock on a lock file), so worker processes that get
        the same request at the same time make one upstream call: the others wait, then read the cache.
        Waits at most timeout_s, then proceeds unlocked. Lock files are left in place (removing them while
        another process waits would break the lock) and swept when old."""
        path = os.path.join(self.dir, "locks", k[:2], k + ".lock")
        os.makedirs(os.path.dirname(path), exist_ok=True)
        fd = os.open(path, os.O_CREAT | os.O_RDWR, 0o600)
        locked = False
        try:
            deadline = time.monotonic() + timeout_s
            while True:
                try:
                    fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
                    locked = True
                    break
                except BlockingIOError:
                    if time.monotonic() > deadline:
                        break
                    await asyncio.sleep(0.05)
            os.utime(path)
            yield locked
        finally:
            if locked:
                fcntl.flock(fd, fcntl.LOCK_UN)
            os.close(fd)

    def get(self, tavily_key, body):
        """-> the cached response, or None (missing, expired or unreadable)."""
        if not self.enabled:
            return None
        p = self._path(self.key(tavily_key, body))
        try:
            with open(p, encoding="utf-8") as f:
                entry = json.load(f)
        except (OSError, ValueError):
            return None
        if self.clock() - entry.get("created_at", 0) > self.ttl:
            self._expire(p, entry)
            return None
        return entry.get("response")

    def put(self, tavily_key, body, response):
        if not self.enabled:
            return
        k = self.key(tavily_key, body)
        p = self._path(k)
        entry = {"created_at": self.clock(), "account": self.account_of(tavily_key), "body": body, "response": response}
        os.makedirs(os.path.dirname(p), exist_ok=True)
        fd, tmp = tempfile.mkstemp(dir=os.path.dirname(p), suffix=".tmp")
        try:
            with os.fdopen(fd, "w", encoding="utf-8") as f:
                json.dump(entry, f, ensure_ascii=False)
            os.replace(tmp, p)
        except OSError:
            try:
                os.remove(tmp)
            except OSError:
                pass
            return
        if self.archive is not None:
            self.archive.add_entry(k, entry, "put")
        self._writes += 1
        if self._writes % 1000 == 0:
            self.sweep()

    def _expire(self, p, entry):
        """Archive an expired entry if it is not archived yet, then delete its file."""
        if self.archive is not None:
            self.archive.add_entry(os.path.basename(p)[:-5], entry, "expired")
        try:
            os.remove(p)
        except OSError:
            pass

    def sweep(self):
        """Delete expired entries (and stale temp files); -> number removed."""
        if not self.enabled:
            return 0
        removed, now = 0, self.clock()
        for root, _dirs, files in os.walk(self.dir):
            for name in files:
                p = os.path.join(root, name)
                try:
                    if name.endswith((".tmp", ".lock")):
                        if now - os.path.getmtime(p) > 3600:
                            os.remove(p)
                            removed += 1
                        continue
                    with open(p, encoding="utf-8") as f:
                        entry = json.load(f)
                    if now - entry.get("created_at", 0) > self.ttl:
                        self._expire(p, entry)
                        removed += 1
                except (OSError, ValueError):
                    continue
        return removed
