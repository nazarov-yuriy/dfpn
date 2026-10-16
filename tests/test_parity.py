"""The service's prompts must match the evaluated benchmark pipelines (skipped outside the repo)."""
import os
import sys

import pytest

from app import enrich, prompts

SCRIPTS = os.path.join(os.path.dirname(__file__), "..", "..", "output", "scripts")
pytestmark = pytest.mark.skipif(not os.path.isdir(SCRIPTS), reason="benchmark scripts not available")
sys.path.insert(0, SCRIPTS)


def test_listwise_prompts_match_rerank_decisions():
    import rerank_decisions as rd
    docs = [{"url": "https://a.com/x", "title": "A", "content": "alpha " * 200, "published_date": "Mon, 05 Oct 2026"},
            {"url": "https://b.com/y", "title": "B", "content": "beta"}]
    as_script = [{"url": d["url"], "title": d["title"], "snippet": d["content"], "page_age": d.get("published_date")}
                 for d in docs]
    for v in ("rerank-v1", "rerank-v2"):
        ours = prompts.listwise_body("m", "q", docs, [0, 1], v, rd.SEARCH_DATE)
        theirs = rd.bodies("m", "q", as_script, "listwise", 600, v)[0][1]
        assert ours == theirs, v


def test_detection_and_site_rewrite_match_multi_retrieve():
    import multi_retrieve as mr
    assert prompts.detect_body("m", "q", mr.SEARCH_DATE) == mr.detect_body("m", "q")
    assert prompts.LANGUAGES == mr.LANGUAGES and prompts.RECENCY == mr.RECENCY
    for q in ("site:openai.com/blog 2025 OpenAI model release", '"repo:a/b" "x"', "no operator"):
        assert enrich.site_rewrite(q) == mr.site_rewrite(q)
    det = {"p_fresh": 0.9, "recency": "week", "language": "russian"}
    theirs = mr.tavily_bodies("x site:a.com", det, 0.5)
    ours = enrich.variant_overrides("x site:a.com", det)
    assert {k: {kk: vv for kk, vv in b.items() if kk in ("query", "include_domains", "topic", "time_range", "language",
                                                          "country")} for k, b in theirs.items() if k != "main"} == \
        {k: ({"query": "x site:a.com", **v} if k != "site" else v) for k, v in ours.items()}


def test_rephrase_prompt_matches_rephrase_retrieve():
    import rephrase_retrieve as rr
    body = prompts.rephrase_body("m", "low", "q", rr.SEARCH_DATE)
    assert body == rr.rephrase_body("m", "low", "q")
