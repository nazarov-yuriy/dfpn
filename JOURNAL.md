# Research Journal: search API providers, benchmarks and UVP

Session goal (2026-11-05): an in-depth report on the benchmarks used to evaluate web-search APIs, the search
engines available as API or MCP server, why Keenable and Exa score so well, how these providers differ from a
Common Crawl index, and what each one's unique value proposition is. Budget: about $240 of cloud quota for
the whole session.

Layout:
- `JOURNAL.md`: this chronological log (newest entry last). Each entry records what was done, what was found
  and the spend estimate at that point.
- `research_notes/Search API landscape and benchmarks/`: raw research notes, one file per subtopic, with sources.
- `reports/`: the synthesized report.

Spend tracking: token counts are summed from the session transcript (`~/.claude/projects/.../*.jsonl`).
Dollar figures are estimates; the list price of the serving model is noted where it was found.

---

## 2026-11-05 00:25 UTC. Setup and orientation

**Done**
- Read the repository: a Tavily-compatible `/search` proxy that widens the candidate pool and reranks it
  with an LLM. Its README cites benchmarks kept outside this repo (`../benchmark/`, `../report/`): a 200-request
  Elo leaderboard, SimpleQA top-3 on 1,200 questions, DeepSearchQA with a 5-step agent. The `harder` mode is
  described as "level with Keenable" on that leaderboard.
- Two orienting web searches to brief the researchers.

**Found so far**
- Keenable: web search and page-fetch API for agents, own crawler, index and ranking, claims 100B+ documents and
  sub-250 ms p95 latency; $26M seed; founders Andrey Styskin (ex-head of search/AI/cloud at Yandex) and
  Matthias Petri. Ships a CLI, REST API, MCP server and a `SKILL.md`; LlamaIndex tool spec works keyless.
- Published head-to-head results are mostly vendor-authored (Parallel wrote most of the BrowseComp comparisons:
  July 2026 run Parallel 51%, Brave 38.3%, Exa Instant 33.7%, Tavily Ultra Fast 19.3%; September run Parallel
  Advanced 74%, Exa 70%, Tavily 66%). The Artificial Analysis Search Index (15 products, 7 providers, fixed agent
  harness) is the most neutral source found so far: Parallel Search advanced 75, Brave LLM-context 75, Exa 74.
- No independent SimpleQA head-to-head surfaced yet; Tavily's and Firecrawl's (94.7%) numbers are self-reported.

**Spend**
- Transcript so far: 20 model turns, 47k output tokens, 320k cache-write tokens, 1.54M cache-read tokens.
  Dollar estimate pending the model's list price.

**Next**
- Launch nine parallel research threads: benchmark catalogue; published head-to-head results; Keenable; Exa;
  own-index providers; SERP wrappers and platform search tools; Common Crawl versus commercial indexes; the MCP
  ecosystem; market positioning and UVP. Commit their notes here when they return.
