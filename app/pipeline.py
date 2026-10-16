"""Search modes on top of Tavily.

  better    Tavily advanced, 20 results -> listwise rerank (rerank-v1) -> top max_results
  harder    the same main call + targeted Tavily basic calls (20 results each, first 5 kept), all with
            published dates:
              site     the query has site:/repo:        -> operator removed, host in include_domains
              fresh    freshness need + recency window   -> time_range (topic news for day/week)
              locale   query language detected           -> language (+ country for non-English)
            + two LLM-rephrased queries (Tavily basic, first 5 of each). Every one of these calls is issued
            twice, with and without the configured exclude_domains (social-media sites by default; a client's
            own exclude_domains are merged in; a site-restricted call is issued once), and both result sets
            go into the pool, the plain copy of a page first -> deduplicated pool -> listwise rerank
            (rerank-v3: date-aware, and told which pages are on the excluded domains and to rank them below
            other relevant documents unless they are the best evidence) -> top max_results

harder-hybrid, the development name of harder in the benchmark files, is accepted as an alias. Any other
search_depth is passed through to Tavily unchanged. Client parameters are forwarded; a variant call is
skipped when the client already constrained its dimension (for example a client include_domains skips the
site call). If an OpenAI call fails, the pipeline degrades (no variant, Tavily's order) instead of failing
the request."""
import asyncio
import datetime
import logging
import time
import urllib.parse
import uuid

from . import enrich, prompts, rerank

log = logging.getLogger("search_service.pipeline")

MODES = ("better", "harder")
ALIASES = {"harder-hybrid": "harder"}  # harder's development name, kept for the benchmark configs and files
POOL_SIZE = 20       # results requested from every Tavily call (the results kept from an extra call: settings.extra_take)
DEFAULT_MAX_RESULTS = 10
CREDITS = {"advanced": 2, "basic": 1, "fast": 1, "ultra-fast": 1}
STRIPPED = {"api_key", "search_depth", "max_results", "include_published_date"}
MAIN_ONLY = {"include_answer", "include_images", "include_image_descriptions", "auto_parameters"}
DIMENSIONS = {"site": ("include_domains",), "fresh": ("topic", "time_range", "start_date", "end_date", "days"),
              "locale": ("country", "language")}


def error(msg):
    return {"detail": {"error": msg}}


def norm_url(u):
    """Host without www + path, lowercased and percent-decoded (so /Boyac%C3%A1 and /Boyacá are one page)."""
    p = urllib.parse.urlsplit(u or "")
    return (p.netloc.lower().removeprefix("www.") + urllib.parse.unquote(p.path).rstrip("/")).lower()


def is_wikipedia(url):
    host = (urllib.parse.urlsplit(url or "").hostname or "").lower()
    return host == "wikipedia.org" or host.endswith(".wikipedia.org")


def pin_wikipedia(order, pool, top):
    """Wikipedia results within the pool's first `top` positions keep exactly that position; the reranked
    order fills the other positions. [site1, site2, wiki1, site3] -> [site3, site1, wiki1, site2]."""
    pinned = {pos: pos for pos in range(min(top, len(pool))) if is_wikipedia(pool[pos].get("url"))}
    if not pinned:
        return order
    rest = iter(k for k in order if k not in pinned)
    return [pinned[pos] if pos in pinned else next(rest) for pos in range(len(order))]


def excluding(body, domains):
    """body with the mode's exclude_domains added (merged with the client's), unless the call is restricted to
    include_domains, where an exclusion could contradict it."""
    if not domains or body.get("include_domains"):
        return body
    own = [d for d in (body.get("exclude_domains") or []) if isinstance(d, str)]
    return {**body, "exclude_domains": own + [d for d in domains if d not in own]}


def is_social(url, domains):
    """Whether the page is on one of the configured (social-media) domains or their subdomains."""
    host = (urllib.parse.urlsplit(url or "").hostname or "").lower()
    return any(host == d or host.endswith("." + d) for d in domains)


def client_constrains(body, variant):
    for k in DIMENSIONS[variant]:
        v = body.get(k)
        if k == "topic" and v in (None, "general"):
            continue
        if v not in (None, "", [], {}):
            return True
    return False


def upstream_error(st, data, caller):
    """A failed main Tavily call -> the response for the client."""
    if st in (401, 403) and caller.kind == "operator":
        return 502, error("Upstream Tavily rejected the service's API key.")
    if st == 0:
        return 502, data
    return st, data


def merge(calls):
    """calls: [(name, results)] with the main call first -> pool of result dicts, deduplicated by URL. The first
    copy of a page is kept; a published date missing there is filled from a later copy."""
    seen, pool = {}, []
    for name, results, take in calls:
        for r in (results or [])[:take]:
            nu = norm_url(r.get("url"))
            if not nu:
                continue
            if nu in seen:
                kept = pool[seen[nu]]
                if not kept.get("published_date") and r.get("published_date"):
                    kept["published_date"] = r["published_date"]
                continue
            seen[nu] = len(pool)
            pool.append(dict(r, _source=name))
    return pool


class Context:
    def __init__(self, settings, upstream, keys):
        self.s, self.up, self.keys = settings, upstream, keys


async def passthrough(body, caller, ctx):
    """-> (status, data, headers)."""
    t0 = time.monotonic()
    fwd = {k: v for k, v in body.items() if k != "api_key"}
    st, data, hit = await ctx.up.tavily_search(fwd, caller.tavily_key)
    if st in (200, 401, 403):
        ctx.keys.mark(caller, st == 200)
    if st != 200:
        return (*upstream_error(st, data, caller), {})
    if hit:  # a cached response gets this request's id and time, and cost no credits
        data = dict(data, request_id=str(uuid.uuid4()), response_time=round(time.monotonic() - t0, 2))
        if "usage" in data:
            data["usage"] = {"credits": 0}
    return st, data, {"x-cache": "HIT" if hit else "MISS"}


async def run(mode, body, caller, ctx):
    """-> (status, data, headers)."""
    t0 = time.monotonic()
    query = body.get("query")
    if not isinstance(query, str) or not query.strip():
        return 400, error("Query is missing."), {}
    max_results = body.get("max_results", DEFAULT_MAX_RESULTS)
    if isinstance(max_results, bool) or not isinstance(max_results, int) or not 0 <= max_results <= POOL_SIZE:
        return 400, error(f"max_results must be an integer between 0 and {POOL_SIZE}."), {}
    today = datetime.datetime.now(datetime.timezone.utc).date().isoformat()
    model = ctx.s.openai_model
    exclude = tuple(ctx.s.exclude_domains) if mode == "harder" else ()
    excludes = [(), exclude]  # harder issues each logical Tavily call without and with the exclusions
    want_dates = bool(body.get("include_published_date"))
    base = {k: v for k, v in body.items() if k not in STRIPPED}
    # The main call is the same in every mode, so the modes share one cached call. It asks for dates only when
    # the client does: include_published_date changes what Tavily retrieves (fewer Wikipedia pages), so the
    # date-aware reranker gets its dates from the extra calls, which always request them.
    main_body = {**base, "search_depth": "advanced", "max_results": POOL_SIZE}
    if want_dates:
        main_body["include_published_date"] = True
    extra_base = {k: v for k, v in base.items() if k not in MAIN_ONLY}
    tav = lambda b: ctx.up.tavily_search(b, caller.tavily_key)  # noqa: E731
    extra_body = lambda over: {**extra_base, "search_depth": "basic", "max_results": POOL_SIZE,  # noqa: E731
                               "include_published_date": True, **over}

    def variants(b):
        """The bodies one logical call is issued with (deduplicated: a site-restricted call has no exclusion)."""
        out = []
        for ex in excludes:
            vb = excluding(b, ex)
            if vb not in out:
                out.append(vb)
        return out

    main_bodies = variants(main_body)
    main_task = asyncio.create_task(tav(main_bodies[0]))
    if not caller.trusted:  # validate a new BYOK key with this one call before spending anything else
        st, main, main_hit = await main_task
        if st in (200, 401, 403):
            ctx.keys.mark(caller, st == 200)
        if st != 200:
            return (*upstream_error(st, main, caller), {})

    clean_tasks = [asyncio.create_task(tav(b)) for b in main_bodies[1:]]  # harder's main call with the exclusions
    tasks = []  # each resolves to [(name, status, data, cache_hit)]

    async def one(name, b):
        """One logical call, issued once per exclusion variant; the second variant is named <name>-clean."""
        res = await asyncio.gather(*(tav(vb) for vb in variants(b)))
        return [(name if i == 0 else f"{name}-clean", *r) for i, r in enumerate(res)]

    if mode == "harder":
        sr = enrich.site_rewrite(query)
        if sr and not client_constrains(body, "site"):
            tasks.append(asyncio.create_task(one("site", extra_body({"query": sr[0], "include_domains": sr[1]}))))

        async def detected():
            det = enrich.parse_detection(await ctx.up.openai_enrich(
                "decisions", prompts.detect_body(model, query, today), lambda d: enrich.parse_detection(d) is not None))
            ov = enrich.variant_overrides(query, det)
            names = [n for n in ("fresh", "locale") if n in ov and not client_constrains(body, n)]
            groups = await asyncio.gather(*(one(n, extra_body(ov[n])) for n in names))
            return [x for g in groups for x in g]
        tasks.append(asyncio.create_task(detected()))

        async def rephrased():
            resp = await ctx.up.openai_enrich("responses", prompts.rephrase_body(model, ctx.s.rephrase_effort, query, today, ctx.s.rephrase_n),
                                              lambda d: bool(enrich.parse_rephrasings(d, query, ctx.s.rephrase_n)))
            qs = enrich.parse_rephrasings(resp, query, ctx.s.rephrase_n)
            groups = await asyncio.gather(*(one(f"rephrase{i + 1}", extra_body({"query": q})) for i, q in enumerate(qs)))
            return [x for g in groups for x in g]
        tasks.append(asyncio.create_task(rephrased()))

    if caller.trusted:
        st, main, main_hit = await main_task
        if caller.kind == "byok" and st in (200, 401, 403):
            ctx.keys.mark(caller, st == 200)
        if st != 200:
            for t in tasks + clean_tasks:
                t.cancel()
            return (*upstream_error(st, main, caller), {})

    # the second main call (with the exclusions) joins the extras, with a full-size take
    extras = [("main-clean", *r) for r in await asyncio.gather(*clean_tasks, return_exceptions=True)
              if not isinstance(r, BaseException)]
    extras += [x for group in await asyncio.gather(*tasks, return_exceptions=True)
               if not isinstance(group, BaseException) for x in group]
    calls = [("main", main.get("results"), POOL_SIZE)] + [
        (name, d.get("results"), POOL_SIZE if name == "main-clean" else ctx.s.extra_take) for name, st, d, _ in extras if st == 200]
    pool = merge(calls)
    for r in pool:
        if exclude and is_social(r.get("url"), exclude):
            r["_social"] = True
    version = "rerank-v3" if mode == "harder" else "rerank-v1"
    order, scores, rstatus = await rerank.listwise(ctx.up, model, query, pool, version, today,
                                                   ctx.s.rerank_content_chars, ctx.s.rerank_prefer_reference)
    if ctx.s.rerank_pin_wikipedia_top > 0:
        order = pin_wikipedia(order, pool, ctx.s.rerank_pin_wikipedia_top)
    if ctx.s.social_keep_top > 0:  # a social-media page stays only when the reranker put it in the first N
        order = [k for pos, k in enumerate(order) if pos < ctx.s.social_keep_top or not pool[k].get("_social")]

    results = []
    for k in order[:max_results]:
        r = {kk: vv for kk, vv in pool[k].items() if kk not in ("_source", "_social")}
        if scores is not None:
            r["score"] = round(scores[k], 6)
        if not want_dates and not ctx.s.result_dates:
            r.pop("published_date", None)
        results.append(r)

    live = [(main, "advanced")] if not main_hit else []  # cached calls cost no credits
    live += [(d, "advanced" if name == "main-clean" else "basic") for name, st, d, hit in extras if st == 200 and not hit]
    credits = sum(((d.get("usage") or {}).get("credits") or CREDITS[b]) for d, b in live)
    n_calls = 1 + sum(1 for _, st, _, _ in extras if st == 200)
    n_hits = int(main_hit) + sum(1 for _, st, _, hit in extras if st == 200 and hit)
    out = {k: v for k, v in main.items() if k not in ("results", "usage", "response_time", "request_id")}
    out.update(query=query, results=results, response_time=round(time.monotonic() - t0, 2),
               request_id=str(uuid.uuid4()))
    if body.get("include_usage"):
        out["usage"] = {"credits": credits}
    log.info("mode=%s caller=%s calls=%s pool=%d rerank=%s credits=%d cache=%d/%d time=%.2fs", mode, caller.kind,
             ",".join(["main"] + [f"{n}:{st}" for n, st, _, _ in extras]), len(pool), rstatus, credits,
             n_hits, n_calls, out["response_time"])
    return 200, out, {"x-cache": f"{n_hits}/{n_calls}"}
