"""API-key handling.

  - the service key (SERVICE_API_KEY): every upstream call uses the operator's keys;
  - any other key: bring your own key. It is forwarded to Tavily as the client's Tavily key; reranking
    and enrichment run on the operator's OpenAI key once Tavily has accepted the key.

To keep unknown keys from spending the operator's OpenAI budget, a BYOK key that Tavily has not accepted
recently is validated by the first Tavily call before any OpenAI call is made; keys Tavily rejected are
refused for a short while without calling Tavily. Keys are kept only as SHA-256 hashes."""
import hashlib
import hmac
import time
from dataclasses import dataclass


@dataclass(frozen=True)
class Caller:
    kind: str          # "operator" or "byok"
    tavily_key: str
    trusted: bool      # True when the key is known to be accepted by Tavily


def request_key(headers, body):
    """Bearer token (Tavily's scheme), or the legacy `api_key` body field."""
    auth = headers.get("authorization") or ""
    if auth[:7].lower() == "bearer " and auth[7:].strip():
        return auth[7:].strip()
    k = body.get("api_key") if isinstance(body, dict) else None
    return k.strip() if isinstance(k, str) and k.strip() else None


class KeyRegistry:
    def __init__(self, settings, clock=time.monotonic):
        self.s = settings
        self.clock = clock
        self.valid, self.invalid = {}, {}

    @staticmethod
    def _h(key):
        return hashlib.sha256(key.encode()).hexdigest()

    def is_service_key(self, key):
        return bool(self.s.service_api_key) and hmac.compare_digest(key.encode(), self.s.service_api_key.encode())

    def resolve(self, key):
        """-> Caller, or None when the key was rejected by Tavily recently."""
        if self.is_service_key(key):
            return Caller("operator", self.s.tavily_api_key or "", True)
        h, now = self._h(key), self.clock()
        if self.invalid.get(h, 0) > now:
            return None
        return Caller("byok", key, self.valid.get(h, 0) > now)

    def mark(self, caller, accepted):
        if caller.kind != "byok":
            return
        h = self._h(caller.tavily_key)
        if accepted:
            self.valid[h] = self.clock() + self.s.key_cache_ttl_s
            self.invalid.pop(h, None)
        else:
            self.invalid[h] = self.clock() + self.s.invalid_key_ttl_s
            self.valid.pop(h, None)
        if len(self.valid) + len(self.invalid) > 100_000:  # bound memory
            now = self.clock()
            self.valid = {k: t for k, t in self.valid.items() if t > now}
            self.invalid = {k: t for k, t in self.invalid.items() if t > now}
