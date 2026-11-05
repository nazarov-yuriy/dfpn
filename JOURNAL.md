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

## 2026-11-05 00:50 UTC. Wave 1, first thread back: Keenable

**Done**
- Committed `research_notes/Search API landscape and benchmarks/keenable.md` (267 lines, about 110 source links;
  every fact dated, vendor claims marked). The thread ran 58 tool calls in about 10 minutes and ran out of
  web-search budget before covering user opinions on Reddit, LinkedIn and X.
- Push to GitHub is refused with 403 (Claude has no access to the repository); commits stay local until access is
  reconnected. Retried after re-attaching the repository with push credentials: still refused.

**Found: Keenable**
- Company: founded 2025, out of stealth 2026-08-25 with a $26M seed led by Accel with Conviction Partners.
  Founders Andrey Styskin (CEO; ran Yandex Search, then web infrastructure at Amazon AGI) and Matthias Petri
  (Chief Scientist; ex-Amazon AGI, built Alexa's web-grounding service). About 15 engineers.
- Index: claims 100B+ documents, own crawler, index and ranking; first index stood up around February 2026.
  No architecture or ranking blog exists. The only disclosed ML component is "Dynamic Snippets" (2026-08-30),
  a token classifier that cut response bytes by about 49%. Freshness is exposed through `acquired_at`
  timestamps, four date filters and a point-in-time `query_time` ("Time Machine"). Recrawl policy unpublished.
  No mention of Common Crawl anywhere.
- Products: `/v1/search` (modes pro and realtime, site and date filters, 1 to 50 results, snippet length up to
  10,000 chars; no language, country or operators), `/v1/fetch` (markdown, live fetch, prompt-based extraction),
  hosted MCP (plain, OAuth and keyless public endpoints), Rust CLI via Homebrew, a `SKILL.md`, SDKs, and SELECT,
  an "SQL over the web" agent product.
- Pricing: 100K free requests per month per org; $4 per 1K pay-as-you-go; $1 per 1K on dedicated capacity at
  100+ requests per second (cloud or on-premises); keyless x402 USDC micropayments at $0.01 per call.
- Benchmarks: Vals Web Search Index (independent, 2026-10-21): Keenable Pro with GPT-5.6 Sol first at 49.08%
  against Exa with Claude Fable 5 at 48.45%, but at $8.84 per task against $3.48, and only Exa and native tools
  were compared. Artificial Analysis Search Index launch (2026-08-18): Keenable realtime 67, behind Parallel 75,
  Exa 74, Firecrawl 73, ahead of Brave 65, and fastest time per task (16.8 s). NEEDLE, Keenable's own open-source
  live benchmark (7 days to 2026-11-04, share of an oracle ceiling): Perplexity 74, Keenable 72, Exa 69,
  Parallel 68, Brave 59, Bing 48, Google via Serper 46, Tavily 43; latency p50 154 ms and p95 317 ms for Keenable
  against 1.4 s and 3.2 s for Exa. Vendor replication of the Artificial Analysis harness: BrowseComp 56.6% to
  67.3% after Dynamic Snippets. No SimpleQA number exists for Keenable.
- Why it is strong, in the vendor's words: an independent index ("federated engines can't improve beyond
  re-ranking"), per-task index structures that make queries cheap and fast, token-efficient snippets, learning
  from agent traffic, and latency. Third-party commentary is thin and neutral to skeptical ("legitimate but
  embryonic", "not yet independently benchmarked"). The Yandex MatrixNet/CatBoost link is heritage only; no
  source ties specific Yandex techniques to Keenable's ranker.
- The benchmark roundup page found during orientation (select.keenable.ai/r/ai-web-search-api-benchmarks) now
  returns 404; the Artificial Analysis Search Index page also returned 404 to the researcher.

**Spend**
- All transcripts: 90 model turns, 309k output, 1.69M cache-write, 7.79M cache-read tokens.
  Estimate $51 to $57 of $240 (21% to 24%). Eight threads still running.

**Next**
- Wave 2 should cover: NEEDLE's methodology and current leaderboard; the Vals Web Search Index; the current
  Artificial Analysis Search Index data (the page moved); Keenable crawl cadence and Common Crawl seeding;
  practitioner opinions on Keenable.
