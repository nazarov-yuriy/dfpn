"""Async clients for the upstream APIs: Tavily search and the OpenAI Decisions and Responses APIs.

Keys travel only in request headers and are never logged."""
import asyncio
import copy
import logging

import httpx

from .cache import ENRICHMENT_ACCOUNT, TavilyCache

log = logging.getLogger("search_service.upstream")
RETRY_STATUSES = {408, 409, 425, 429, 500, 502, 503, 504}


class Upstream:
    def __init__(self, settings, transport=None, cache=None):
        self.s = settings
        self.cache = cache
        self._inflight = {}  # request key -> future of an upstream call in progress (single-flight)
        self.http = httpx.AsyncClient(
            timeout=settings.upstream_timeout_s, transport=transport,
            limits=httpx.Limits(max_connections=200, max_keepalive_connections=50))

    async def close(self):
        await self.http.aclose()

    async def _post(self, url, headers, body, tries=3):
        """-> (status, parsed JSON body). Network errors give status 0."""
        for attempt in range(tries):
            try:
                r = await self.http.post(url, headers=headers, json=body)
            except httpx.HTTPError as e:
                if attempt < tries - 1:
                    await asyncio.sleep(0.5 * 2 ** attempt)
                    continue
                return 0, {"detail": {"error": f"upstream unreachable: {type(e).__name__}"}}
            if r.status_code in RETRY_STATUSES and attempt < tries - 1:
                ra = r.headers.get("retry-after")
                await asyncio.sleep(min(float(ra), 5.0) if ra and ra.replace(".", "", 1).isdigit() else 0.5 * 2 ** attempt)
                continue
            try:
                data = r.json()
            except ValueError:
                data = {"detail": {"error": r.text[:500]}}
            return r.status_code, data
        return 0, {"detail": {"error": "upstream unavailable"}}

    async def _single_flight(self, k, fetch):
        """Identical calls in flight at the same time share one upstream call (a shared future in this
        process). A call that reused another's result reports cache_hit=True."""
        pending = self._inflight.get(k)
        if pending is not None:
            st, data, _ = await asyncio.shield(pending)
            return st, copy.deepcopy(data), True
        fut = asyncio.get_running_loop().create_future()
        self._inflight[k] = fut
        try:
            res = await fetch()
            fut.set_result(res)
            return res
        except BaseException as e:
            fut.set_exception(e)
            fut.exception()  # mark retrieved: waiters re-raise it, no "never retrieved" warning
            raise
        finally:
            self._inflight.pop(k, None)

    async def _cached(self, k, account, body, call, usable):
        """call() -> (status, data); stored when usable(status, data). Worker processes coordinate through
        the cache's file lock, so one of them makes the call and the others read its result."""
        if self.cache is None:
            st, data = await call()
            return st, data, False
        hit = await asyncio.to_thread(self.cache.get, account, body)
        if hit is not None:
            return 200, hit, True
        async with self.cache.lock(k, timeout_s=self.s.upstream_timeout_s + 5):
            hit = await asyncio.to_thread(self.cache.get, account, body)  # another worker may have just fetched it
            if hit is not None:
                return 200, hit, True
            st, data = await call()
            if usable(st, data):
                await asyncio.to_thread(self.cache.put, account, body, data)
            return st, data, False

    async def tavily_search(self, body, key):
        """-> (status, data, cache_hit). Successful responses are cached per (Tavily key, body); identical
        requests in flight share one call. A request served from the cache or another's call consumed no
        credits (cache_hit=True)."""
        k = TavilyCache.key(key, body)
        url, headers = f"{self.s.tavily_base_url}/search", {"Authorization": f"Bearer {key}"}
        return await self._single_flight(k, lambda: self._cached(
            k, key, body, lambda: self._post(url, headers, body), lambda st, _d: st == 200))

    async def openai_enrich(self, path, body, usable):
        """Detection and rephrasing calls depend only on the query and the date, so they are cached and
        shared like Tavily searches when ENRICH_CACHE is on. -> response JSON, or None on failure."""
        if not self.s.openai_api_key:
            return None
        if self.cache is None or not self.s.enrich_cache:
            data = await self.openai(path, body)
            return data if data is not None and usable(data) else None
        account, cbody = ENRICHMENT_ACCOUNT, {"path": path, "body": body}
        k = TavilyCache.key(account, cbody)
        url, headers = f"{self.s.openai_base_url}/{path}", {"Authorization": f"Bearer {self.s.openai_api_key}"}
        st, data, _ = await self._single_flight(k, lambda: self._cached(
            k, account, cbody, lambda: self._post(url, headers, body), lambda st, d: st == 200 and usable(d)))
        if st != 200 or not usable(data):
            log.warning("openai %s failed: status %s", path, st)
            return None
        return data

    async def openai(self, path, body):
        """-> response JSON, or None on any failure (callers degrade gracefully)."""
        if not self.s.openai_api_key:
            return None
        st, data = await self._post(f"{self.s.openai_base_url}/{path}",
                                    {"Authorization": f"Bearer {self.s.openai_api_key}"}, body)
        if st != 200:
            log.warning("openai %s failed: status %s", path, st)
            return None
        return data
