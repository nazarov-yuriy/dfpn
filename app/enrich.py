"""Query enrichment: site:/repo: rewriting, freshness/recency/language detection and query rephrasing.
Ported from output/scripts/multi_retrieve.py and rephrase_retrieve.py."""
import json
import re

from . import prompts

SITE_RE = re.compile(r'"?\b(site|repo):(\S+?)"?(?=\s|$)')


def site_rewrite(query):
    """-> (query without operators, [hosts]) or None when the query has no site:/repo: operator.
    A path after the host (site:openai.com/blog) stays in the query as words."""
    hosts, extra = [], []
    for kind, arg in SITE_RE.findall(query):
        arg = arg.strip('"')
        if kind == "repo":
            hosts.append("github.com")
            extra.append(arg)
        else:
            host, _, path = arg.partition("/")
            hosts.append(host.lower().removeprefix("www."))
            extra += [w for w in path.split("/") if w]
    if not hosts:
        return None
    rest = re.sub(r"\s+", " ", SITE_RE.sub(" ", query)).strip()
    return " ".join([rest] + extra).strip(), sorted(set(hosts))


def parse_detection(resp):
    ans = {a.get("name"): a for a in (resp or {}).get("answers") or []}
    try:
        fresh = float(ans["needs_fresh"]["probability"])
        rec = {p["value"]: p["probability"] for p in ans["recency"]["probabilities"]}
        lang = {p["value"]: p["probability"] for p in ans["language"]["probabilities"]}
    except (KeyError, TypeError, ValueError):
        return None
    return {"p_fresh": fresh, "recency": max(rec, key=rec.get), "language": max(lang, key=lang.get)}


def variant_overrides(query, det, fresh_threshold=0.5):
    """The targeted basic calls of the `harder` pipeline -> {name: overrides of the request body}."""
    out = {}
    sr = site_rewrite(query)
    if sr:
        out["site"] = {"query": sr[0], "include_domains": sr[1]}
    if det and det["p_fresh"] >= fresh_threshold and det["recency"] != "any":
        # day / week: news search; month / year: general search filtered by date
        out["fresh"] = {"topic": "news" if det["recency"] in ("day", "week") else "general",
                        "time_range": det["recency"]}
    if det:
        code, country = prompts.LANGUAGES.get(det["language"], (None, None))
        if code:
            out["locale"] = {"language": code, **({"country": country} if country else {})}
    return out


def parse_rephrasings(resp, query, n=2):
    """-> up to n rephrased queries (strings), different from the query and from each other. A non-English
    query always includes its English translation."""
    text = "".join(c.get("text") or "" for it in (resp or {}).get("output") or [] if it.get("type") == "message"
                   for c in it.get("content") or [] if c.get("type") == "output_text")
    try:
        d = json.loads(text)
        qs = [q for q in d["queries"] if isinstance(q, dict) and (q.get("query") or "").strip()]
    except Exception:
        return []
    if d.get("is_english") is False and (d.get("english_translation") or "").strip() \
            and not any(q.get("strategy") == "translation" for q in qs[:2]):
        qs = qs[:1] + [{"query": d["english_translation"].strip(), "strategy": "translation"}]
    norm = lambda s: re.sub(r"\s+", " ", s).strip().casefold()  # noqa: E731
    seen, out = {norm(query)}, []
    for q in qs:
        if norm(q["query"]) not in seen and len(out) < n:
            seen.add(norm(q["query"]))
            out.append(q["query"].strip())
    return out
