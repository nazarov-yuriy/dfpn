"""Listwise reranking with the OpenAI Decisions API (ported from output/scripts/rerank_decisions.py).

One `choice` question whose choices are the documents, asked in the original and in the reversed order;
a document's score is its mean probability over the answered orders. Ties keep the original order. If no
order is answered (refusal or error), the original order is kept."""
import asyncio

from . import prompts


def _probs(resp):
    ans = ((resp or {}).get("answers") or [None])[0] or {}
    if ans.get("type") == "refusal":
        return None
    ps = {str(x.get("value")): x.get("probability") for x in ans.get("probabilities") or []}
    return ps if ps and all(isinstance(v, (int, float)) for v in ps.values()) else None


async def listwise(upstream, model, query, docs, version, today, content_chars=prompts.CONTENT_CHARS,
                   prefer_reference=False):
    """-> (order: list of indices into docs, scores: {index: score} or None, status)."""
    n = len(docs)
    if n <= 1:
        return list(range(n)), None, "ok"
    orders = [list(range(n)), list(range(n))[::-1]]
    resps = await asyncio.gather(*(upstream.openai("decisions", prompts.listwise_body(
        model, query, docs, o, version, today, content_chars, prefer_reference)) for o in orders))
    acc = {}
    answered = 0
    for o, resp in zip(orders, resps):
        ps = _probs(resp)
        if ps is None:
            continue
        answered += 1
        for p, k in enumerate(o):
            acc.setdefault(k, []).append(ps.get(f"doc{p + 1}", 0.0))
    if not answered:
        return list(range(n)), None, "failed"
    scores = {k: sum(v) / len(v) for k, v in acc.items()}
    return sorted(range(n), key=lambda k: (-scores[k], k)), scores, "ok" if answered == len(orders) else "partial"
