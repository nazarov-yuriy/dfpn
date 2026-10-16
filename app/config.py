"""Service settings, read from the environment."""
import os
from dataclasses import dataclass


def _float(name, default):
    v = os.environ.get(name)
    return float(v) if v not in (None, "") else default


def _bool(v, default):
    return default if v in (None, "") else v.strip().lower() in ("1", "true", "yes", "on")


@dataclass(frozen=True)
class Settings:
    # Clients presenting this key get every upstream call on the operator's keys. Any other key is treated
    # as the client's own Tavily key (bring your own key): Tavily calls use it, reranking and enrichment
    # still run on the operator's OpenAI key.
    service_api_key: str | None = None
    tavily_api_key: str | None = None      # the operator's Tavily key (used with service_api_key)
    openai_api_key: str | None = None      # the operator's OpenAI key (reranking, detection, rephrasing)
    openai_model: str = "gpt-6-luna"
    rephrase_effort: str = "low"
    tavily_base_url: str = "https://api.tavily.com"
    openai_base_url: str = "https://api.openai.com/v1"
    upstream_timeout_s: float = 60.0
    key_cache_ttl_s: float = 600.0         # how long a BYOK key Tavily accepted is trusted
    invalid_key_ttl_s: float = 60.0        # how long a BYOK key Tavily rejected is refused without a call
    rerank_content_chars: int = 4000       # characters of each document's content the reranker sees
    rerank_prefer_reference: bool = False  # ask the reranker to prefer Wikipedia / authoritative reference sources
    rerank_pin_wikipedia_top: int = 0      # Wikipedia results within the pool's first N positions keep their position
    # harder's tuning knobs (the evaluated configuration is the default)
    rephrase_n: int = 2                    # rephrased queries per request
    extra_take: int = 5                    # results kept from each targeted or rephrased call
    result_dates: bool = False             # return published_date when known even if the client did not ask
    social_keep_top: int = 0               # >0: a page on EXCLUDE_DOMAINS stays in the list only in the reranker's top N
    enrich_cache: bool = True              # cache detection and rephrasing calls with the Tavily cache's TTL
    tavily_cache_dir: str | None = "cache"  # persistent Tavily response cache (None or ttl 0: disabled)
    tavily_cache_ttl_s: float = 604800.0   # 7 days
    # harder: the domains its second set of Tavily calls excludes (Tavily's exclude_domains) and whose pages the
    # reranker is told to demote. Social-media and forum pages make an agent's result lists noisier without
    # adding answers; see the DeepSearchQA analysis. Empty: each call is issued once and nothing is marked.
    exclude_domains: tuple = ("facebook.com", "instagram.com", "youtube.com", "reddit.com", "tiktok.com", "x.com",
                              "twitter.com", "linkedin.com", "pinterest.com", "quora.com", "threads.net")
    # durable archive of every cached response (SQLite). None: next to the cache directory (archive.sqlite,
    # /data/archive.sqlite in the image); "": off. Entries stay in the archive after the cache's TTL removes them.
    tavily_archive_db: str | None = None

    @classmethod
    def from_env(cls):
        e = os.environ.get
        return cls(
            service_api_key=e("SERVICE_API_KEY") or None,
            tavily_api_key=e("TAVILY_API_KEY") or None,
            openai_api_key=e("OPENAI_API_KEY") or None,
            openai_model=e("OPENAI_MODEL") or cls.openai_model,
            rephrase_effort=e("REPHRASE_EFFORT") or cls.rephrase_effort,
            tavily_base_url=(e("TAVILY_BASE_URL") or cls.tavily_base_url).rstrip("/"),
            openai_base_url=(e("OPENAI_BASE_URL") or cls.openai_base_url).rstrip("/"),
            upstream_timeout_s=_float("UPSTREAM_TIMEOUT_S", cls.upstream_timeout_s),
            key_cache_ttl_s=_float("KEY_CACHE_TTL_S", cls.key_cache_ttl_s),
            invalid_key_ttl_s=_float("INVALID_KEY_TTL_S", cls.invalid_key_ttl_s),
            rerank_content_chars=int(_float("RERANK_CONTENT_CHARS", cls.rerank_content_chars)),
            rerank_prefer_reference=_bool(e("RERANK_PREFER_REFERENCE"), cls.rerank_prefer_reference),
            enrich_cache=_bool(e("ENRICH_CACHE"), cls.enrich_cache),
            rerank_pin_wikipedia_top=int(_float("RERANK_PIN_WIKIPEDIA_TOP", cls.rerank_pin_wikipedia_top)),
            rephrase_n=int(_float("REPHRASE_N", cls.rephrase_n)),
            extra_take=int(_float("EXTRA_TAKE", cls.extra_take)),
            result_dates=_bool(e("RESULT_DATES"), cls.result_dates),
            social_keep_top=int(_float("SOCIAL_KEEP_TOP", cls.social_keep_top)),
            tavily_cache_dir=e("TAVILY_CACHE_DIR") or cls.tavily_cache_dir,
            tavily_cache_ttl_s=_float("TAVILY_CACHE_TTL_S", cls.tavily_cache_ttl_s),
            tavily_archive_db=e("TAVILY_ARCHIVE_DB"),
            exclude_domains=cls.exclude_domains if e("EXCLUDE_DOMAINS") is None
            else tuple(d.strip() for d in e("EXCLUDE_DOMAINS").split(",") if d.strip()),
        )
