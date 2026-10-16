"""Tavily-compatible search service with two extra search_depth modes: better and harder.

POST /search takes Tavily's request body and auth (Authorization: Bearer <key>, or the legacy `api_key`
field) and returns Tavily's response format. GET /health reports readiness without revealing keys."""
import asyncio
import contextlib
import logging
import os

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from . import pipeline
from .auth import KeyRegistry, request_key
from .archive import Archive
from .cache import TavilyCache
from .config import Settings
from .upstream import Upstream

logging.basicConfig(level=os.environ.get("LOG_LEVEL", "INFO"), format="%(asctime)s %(levelname)s %(name)s %(message)s")
logging.getLogger("httpx").setLevel(logging.WARNING)  # per-request upstream lines; keys are never logged
UNAUTHORIZED = {"detail": {"error": "Unauthorized: missing or invalid API key."}}


def archive_path(settings):
    """None in the settings means the default, next to the cache directory; "" means no archive."""
    if settings.tavily_archive_db is None:
        return os.path.join(os.path.dirname(os.path.abspath(settings.tavily_cache_dir)), "archive.sqlite")
    return settings.tavily_archive_db or None


def create_app(settings=None, transport=None):
    settings = settings or Settings.from_env()
    cache = archive = None
    if settings.tavily_cache_dir and settings.tavily_cache_ttl_s > 0:
        db = archive_path(settings)
        archive = Archive(db) if db else None
        cache = TavilyCache(settings.tavily_cache_dir, settings.tavily_cache_ttl_s, archive=archive)
    upstream = Upstream(settings, transport, cache)
    ctx = pipeline.Context(settings, upstream, KeyRegistry(settings))

    @contextlib.asynccontextmanager
    async def lifespan(_app):
        if cache is not None:
            asyncio.get_running_loop().run_in_executor(None, cache.sweep)  # drop expired entries in the background
        yield
        await upstream.close()

    app = FastAPI(title="Tavily-compatible search with reranking", version="1.0.0", lifespan=lifespan)

    @app.get("/health")
    async def health():
        return {"status": "ok", "modes": list(pipeline.MODES),
                "configured": {"service_api_key": bool(settings.service_api_key),
                               "tavily_api_key": bool(settings.tavily_api_key),
                               "openai_api_key": bool(settings.openai_api_key)},
                "rerank_content_chars": settings.rerank_content_chars,
                "rerank_prefer_reference": settings.rerank_prefer_reference,
                "rerank_pin_wikipedia_top": settings.rerank_pin_wikipedia_top,
                "rephrase_n": settings.rephrase_n, "extra_take": settings.extra_take,
                "result_dates": settings.result_dates, "social_keep_top": settings.social_keep_top,
                "enrich_cache": settings.enrich_cache,
                "tavily_cache_ttl_s": settings.tavily_cache_ttl_s if cache is not None else 0,
                "tavily_archive": archive is not None,
                "exclude_domains": list(settings.exclude_domains)}

    @app.post("/search")
    async def search(request: Request):
        try:
            body = await request.json()
        except ValueError:
            return JSONResponse(status_code=400, content=pipeline.error("Invalid JSON body."))
        if not isinstance(body, dict):
            return JSONResponse(status_code=400, content=pipeline.error("The request body must be a JSON object."))
        key = request_key(request.headers, body)
        caller = ctx.keys.resolve(key) if key else None
        if caller is None:
            return JSONResponse(status_code=401, content=UNAUTHORIZED)
        if caller.kind == "operator" and not settings.tavily_api_key:
            return JSONResponse(status_code=500, content=pipeline.error("The service has no TAVILY_API_KEY configured."))
        depth = body.get("search_depth")
        mode = pipeline.ALIASES.get(depth, depth) if isinstance(depth, str) else depth
        if mode in pipeline.MODES:
            status, data, headers = await pipeline.run(mode, body, caller, ctx)
        else:
            status, data, headers = await pipeline.passthrough(body, caller, ctx)
        return JSONResponse(status_code=status, content=data, headers=headers)

    return app


app = create_app()
