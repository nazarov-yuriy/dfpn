"""Durable archive of cache entries: a SQLite database that keeps every Tavily (and enrichment) response the
cache ever stored, so nothing is lost when the cache's time-to-live cleans it up.

Entries are added when the cache writes them, and again (idempotently) when the sweep or a read finds them
expired, so an entry written by an older version of the service that never archived on write is still saved
before deletion. The archive is never read by the service; it exists for replay and audit
(`scripts/cache_archive.py` imports, exports and summarizes it). API keys are never stored: the account is a
hash of the Tavily key, as in the cache key.

Standard-library sqlite3; WAL mode and a busy timeout let several worker processes write to one file."""
import contextlib
import json
import logging
import os
import sqlite3
import time

log = logging.getLogger("search_service.archive")

SCHEMA = """
CREATE TABLE IF NOT EXISTS entries (
    key         TEXT NOT NULL,   -- the cache key (SHA-256 of account + request body)
    created_at  REAL NOT NULL,   -- when the response was fetched (the cache entry's timestamp)
    archived_at REAL NOT NULL,
    reason      TEXT NOT NULL,   -- put | expired | import
    account     TEXT,            -- hash of the Tavily key, or "openai-enrichment"
    request     TEXT,            -- the request body as JSON (NULL for entries written before it was stored)
    response    TEXT NOT NULL,   -- the response as JSON
    PRIMARY KEY (key, created_at)
);
CREATE INDEX IF NOT EXISTS entries_created_at ON entries (created_at);
"""


class Archive:
    def __init__(self, path, clock=time.time):
        self.path = path
        self.clock = clock
        os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
        with self._connect() as con:
            con.executescript(SCHEMA)

    def _connect(self):
        con = sqlite3.connect(self.path, timeout=10)
        con.execute("PRAGMA journal_mode=WAL")
        return contextlib.closing(con)

    def add(self, key, created_at, response, account=None, request=None, reason="put"):
        """Store one entry; -> True if it was new. A failure is logged and never raised: the service must not
        break because the archive is unavailable."""
        try:
            with self._connect() as con, con:
                cur = con.execute(
                    "INSERT OR IGNORE INTO entries (key, created_at, archived_at, reason, account, request, response) "
                    "VALUES (?, ?, ?, ?, ?, ?, ?)",
                    (key, float(created_at), self.clock(), reason, account,
                     None if request is None else json.dumps(request, ensure_ascii=False, sort_keys=True),
                     json.dumps(response, ensure_ascii=False)))
                return cur.rowcount == 1
        except (sqlite3.Error, OSError, TypeError, ValueError) as e:
            log.warning("archive write failed (%s): %s", type(e).__name__, e)
            return False

    def add_entry(self, key, entry, reason):
        """Archive a cache file's content ({"created_at", "response", optionally "account", "body"})."""
        if not isinstance(entry, dict) or "response" not in entry:
            return False
        return self.add(key, entry.get("created_at", 0), entry["response"], entry.get("account"), entry.get("body"), reason)

    def stats(self):
        with self._connect() as con:
            n, oldest, newest = con.execute("SELECT COUNT(*), MIN(created_at), MAX(created_at) FROM entries").fetchone()
            by_reason = dict(con.execute("SELECT reason, COUNT(*) FROM entries GROUP BY reason").fetchall())
            with_request = con.execute("SELECT COUNT(*) FROM entries WHERE request IS NOT NULL").fetchone()[0]
        return {"path": self.path, "entries": n, "with_request": with_request, "by_reason": by_reason,
                "oldest_created_at": oldest, "newest_created_at": newest,
                "size_bytes": sum(os.path.getsize(p) for p in (self.path, self.path + "-wal") if os.path.exists(p))}

    def rows(self, key=None):
        """Yield entries as dicts (request and response parsed), newest first; optionally one key only."""
        q = "SELECT key, created_at, archived_at, reason, account, request, response FROM entries"
        args = ()
        if key:
            q += " WHERE key = ?"
            args = (key,)
        with self._connect() as con:
            for k, c, a, r, acc, req, resp in con.execute(q + " ORDER BY created_at DESC", args):
                yield {"key": k, "created_at": c, "archived_at": a, "reason": r, "account": acc,
                       "request": None if req is None else json.loads(req), "response": json.loads(resp)}
