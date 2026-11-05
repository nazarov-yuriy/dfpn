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
Dollar figures use the official list prices of the serving model (see the 00:46 entry). Entry times are the
commit times in UTC; the session started at 00:13 UTC.

---

## 2026-11-05 00:26 UTC. Setup and orientation

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

## 2026-11-05 00:40 UTC. Wave 1, first thread back: Keenable

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

## 2026-11-05 00:41 UTC. Wave 1, thread 2 back: Exa

**Done**
- Committed the final `exa.md` (seven sections; vendor, competitor and independent sources labelled). This thread
  also exhausted its web-search budget before reaching HN threads and arXiv usage, so wave 2 will use narrower
  briefs and direct page fetches.

**Found: Exa**
- Company: Metaphor Systems (2021, YC S21, Will Bryk and Jeff Wang), rebranded Exa 2024-01-25. Funding: $5M seed,
  $17M Series A (July 2024, Lightspeed), $85M Series B at $700M (2025-09-03, Benchmark), $250M Series C at $2.2B
  (2026-05-20, a16z). Vendor-reported: over $100M annualized revenue (2026-10-13), about 2B requests per month,
  over 200k teams; Sacra estimated about $10M ARR in September 2025. Customers include Databricks, Cursor,
  Notion AI, Cognition, HubSpot, OpenRouter.
- Architecture (from Exa's engineering posts): own crawler (ExaSearchBot), custom parser, S3 and Lance storage,
  an embedding model first trained on link prediction ("neural PageRank"), later fine-tuned on synthetic data; a
  custom C++/Rust vector database (4096-d Matryoshka embeddings cut to 256-d, binary quantization, 100k clusters,
  under 100 ms over billions of vectors, December 2024); BM25 served alongside; the April 2026 "Composing a Search
  Engine" post shows dense ANN and a sparse inverted index fused with reciprocal rank fusion (k=60), then
  relevance and authority rerankers, about 250 ms serving. GPUs: 80 A100s (2021) plus a 144-H200 cluster (2025).
- Index claims over time: "billions" (March 2025), "tens of billions" (October 2025), 500B URLs tracked (May
  2026), 80B pages and 1.4T URLs (August 2026), 100B pages served and 2T URLs tracked (October 2026), plus 400B
  historical snapshots (Exa Snapshot, September 2026).
- Modes: Auto (December 2024), Fast (July 2025), Exa 2.0 Fast/Auto/Deep (2025-10-10), Instant sub-200 ms
  (February 2026), deep and deep-reasoning with output schemas (March 2026), Deep Max (April 2026), Exa Agent
  (June 2026), Exa 3.0 (2026-10-19: Lite/Auto/Deep, larger embedding model, Dynamic Highlights GA claiming 95%
  fewer tokens).
- Pricing (November 2026): lite $4, auto $7 (raised from $5 in March 2026), deep $12, deep-reasoning $15 per 1K
  searches; contents $1 per 1K pages per type; $10 free credits monthly; 10 QPS search.
- Benchmarks. Independent, Artificial Analysis Search Index (equal mean of DeepSearchQA, BrowseComp-200 and
  AA-Omniscience; GPT-5.6 Luna agent): at launch (2026-08-18) Exa auto 74, fast 68, Parallel advanced 75; as of
  2026-10-19 Exa auto with dynamic highlights 80 (tied with Perplexity medium), Exa lite 79, Parallel advanced 75,
  Brave 75, OpenAI 74, Firecrawl 73; Exa auto cost $53 per 1K tasks at 36.9 s per task. Competitor-run (Parallel,
  2026-09-09, 50 BrowseComp questions): Parallel Advanced 74% ($399 per 1K), Perplexity 74%, Exa Auto 70% ($971,
  highest cost), Tavily 66%; July 2026: Exa Instant 33.7% BrowseComp against Parallel Turbo 51%, SimpleQA 89.3%
  against 91%; measured Exa Instant p50 335 to 361 ms against the advertised sub-200 ms. Perplexity's
  search_evals shows Exa's Agent API far behind on BrowseComp (0.38 against 0.805). Vendor: Exa 3.0 BrowseComp
  91.8%, DeepSearchQA 88.2%, WideSearch 56.1%, ATLAS 42.0% (harness unstated).
- Exa's ATLAS post argues BrowseComp, WideSearch and DeepSearchQA barely measure search quality: 48% to 61% of
  questions are answerable closed-book, and hiding 7 of 10 results retains 81% to 89% of the score, while the
  search backend moves ATLAS scores by 16%.
- Why strong: embeddings of long natural-language queries, full parsed page content and highlights instead of
  snippets, compute-scalable rerankers, and fewer queries per task (7.6 against 9.5 to 15.4 for others in the
  Artificial Analysis data). Weaknesses: the highest per-task cost in competitor runs, an advertised-versus-measured
  latency gap, lite mode is cache-only, no EU data residency, and crawler blocking acknowledged by the CEO.
- Common Crawl: no vendor or third-party source links Exa to Common Crawl; every primary description says own
  crawl, parse and embed pipeline.

**Spend**
- See the tracker line below this entry's commit. Seven threads still running.

**Next**
- Wave 2 additions: Perplexity's search_evals repository (an open harness with cross-vendor numbers), Exa's ATLAS
  benchmark, and the per-task cost data in the Artificial Analysis index.
- Tracker: TOTAL         99    352923    1861342     9152277    2694    64.05    57.19 budget $240: 27% used (high estimate), 24% (low estimate) 

## 2026-11-05 00:43 UTC. Wave 1, thread 3 back: benchmark catalogue

**Done**
- Committed `benchmarks_catalogue.md`: about 30 benchmarks and three cross-vendor leaderboards, every number tagged
  vendor, independent or academic.

**Found: benchmarks**
- SimpleQA is a Wikipedia test. OpenAI's own paper cites Wikipedia for about 3.5k of 4.3k questions (about 81%),
  then fandom (410), ac.uk (154) and imdb (121). Google's SimpleQA Verified paper says tool-enabled runs are
  "near perfect" and the set reflects "substantial human rater biases". In Parallel's September 2026 run all ten
  provider configurations score 91% to 97%. Brave found its LLM judge wrong on 167 of 292 "incorrect" verdicts;
  Brave and SerpApi both hand-filtered pages that leak the benchmark (SerpApi dropped 40 of 1,000 Verified
  questions). Search Arena finds real users disfavour Wikipedia citations. This matches the repository's own
  finding that pinning Wikipedia helps SimpleQA but not agent requests.
- Agent-in-the-loop versus retrieval-only harnesses flip the winners. Agent loops: Artificial Analysis, Parallel,
  OpenBenchmarks hard-retrieval and multi-hop, Firecrawl, SerpApi, Brave multi-search. Retrieval-only: the
  Tavily repo, Perplexity single-step, You.com 2025, Exa pointwise, AIMultiple, BEIR/MTEB. BrowseComp-Plus
  isolates the retriever: GPT-5 goes from 55.9% with BM25 to 70.1% with Qwen3-Embedding-8B over a fixed corpus.
  LiveBrowseComp shows agents use retrieved evidence less than a third of the time, and closed-book pass@4
  reaches 44.5% on BrowseComp.
- Saturation: SimpleQA and SimpleQA Verified are saturated for any tool-enabled system. BrowseComp is near the
  ceiling for deep-research products (88% to 94% on 100-question subsets) but still spreads search APIs 63 to 87
  on Artificial Analysis' hard-200 subset and 32% to 74% in Parallel's harness. DeepSearchQA (74 to 86),
  OpenBenchmarks hard retrieval (38 to 83) and multi-hop (0 to 48 F1), SealQA (o3 at 17%) and WideSearch (about
  0% to 5%) still discriminate.
- Artificial Analysis Search Index methodology: Stirrup harness, GPT-5.6 Luna as candidate and grader, 25 turns,
  at most 10 results per search, text-only web_fetch with a 15 s timeout, a contamination filter; the score is
  the equal-weighted mean of DeepSearchQA F1, BrowseComp (n=200) and AA-Omniscience (600). Cost is model tokens
  plus list-price search per 1K tasks; model time is derived from tokens and search time is measured. No p50/p95
  and no confidence intervals. Leaderboards of 2026-08-18 and 2026-10-19 are recorded in full in the notes.
- Other cross-vendor boards: OpenBenchmarks (three boards, fixed reader, judge and agent, three runs, October
  2026) and AIMultiple (100 queries, GPT-5.2 judge, bootstrap confidence intervals, December 2025).
- Latency and cost reporting is inconsistent: only Perplexity (p50 to p95 from us-east-1) and You.com (p50)
  publish percentiles; Parallel reports dollars per 1K questions and no latency; OpenBenchmarks mixes mean call
  latency, median task time and cost per 1K correct answers.
- Methodology critiques on record: Google grading itself on DeepSearchQA; Parallel disclosing unpublished judge,
  tool budget and sample IDs with about 14-point noise at n=50; Linkup, SerpApi and Brave tables mixing
  competitors' self-published numbers from different harnesses; Firecrawl reporting best of two; OpenBenchmarks
  admitting later-benchmarked vendors score higher for non-quality reasons; TREC RAG 2025 automated relevance
  judgments agreeing with humans at only 0.30 to 0.34; Search Arena rewarding length and citation count.

**Gaps for wave 2**
- Keenable NEEDLE full scores (one source returned 403), Valyu's harness (page 404), WideSearch affiliation, any
  independent measurement of the Wikipedia top-k inflation effect, and sensitivity of the Artificial Analysis
  ranking to web_fetch and candidate model.

**Spend**
- Tracker: TOTAL        115    479252    2263554    11803794    3120    81.07    72.22 budget $240: 34% used (high estimate), 30% (low estimate)  Six threads still running.

## 2026-11-05 00:44 UTC. Wave 1, thread 4 back: SERP wrappers, official engine APIs, platform tools

**Done**
- Committed `providers_serp_wrappers_and_platforms.md` (375 lines, about 96 citations), with a normalized price
  table and a text diagram of who sits on top of whom.

**Found**
- Google SERP scraping is a commodity. Entry-tier price per 1K ten-result Google queries: DataForSEO standard
  queue $0.60 (5-minute latency), Serper $1.00, Oxylabs $1.00 to $1.35, Bright Data $1.50, Serply and Value SERP
  about $2.00, ScrapingBee about $2.53, SearchApi $4.00, Firecrawl Hobby about $7.60, SerpApi $10 (Starter $25).
  At scale the floor is Serper $0.30 and Oxylabs $0.50. SearchApi covers about 80 engines, Bright Data 7,
  Oxylabs 4; Serper is Google-only. SerpApi and SearchApi sell a $2M "legal shield" on production plans.
- Google's changes hit the wrappers: JavaScript required for results since about 2025-01-15 (Oxylabs now sells a
  separate Google-JS SKU at 35% to 80% more), and `num=100` removed in September 2025, so a top-100 page costs
  about 10 requests.
- Official engine APIs are closing or getting expensive. Google Custom Search JSON API is closed to new customers
  and discontinued 2027-01-01 ($5 per 1K for existing users). Gemini grounding costs $14 per 1K search queries on
  Gemini 3+ and $35 per 1K grounded prompts on 2.5 models; Vertex Enterprise Web Grounding $45 per 1K. Bing Search
  APIs retired 2025-08-11; Grounding with Bing Search now $14 per 1K transactions, no raw results. Yandex Search
  API about $4 per 1K synchronous. DuckDuckGo has only the Instant Answer API. SearXNG public instances are
  routinely blocked by Google (reCAPTCHA suspends the engine for 7 days by default).
- LLM-platform search tools, price per 1K calls plus tokens: xAI web_search $5; Perplexity Search API $5 ($1
  fast); OpenAI $10 (backend undisclosed; 2024 evidence points to Bing plus OAI-SearchBot); Anthropic $10 per
  search (backend undisclosed; March 2025 evidence points to Brave Search as subprocessor); Gemini $14; Bing
  grounding $14; Mistral about $30 (third-party figure).
- Meta-layers over other engines: Jina s.jina.ai (engine undisclosed, 2.5 s average), Firecrawl /search (uses
  Google-syntax `tbs=qdr:` filters and an "upstream search provider", so inferred Google-derived), Tavily ($8 per
  1K credits pay-as-you-go, describes "aggregating up to 20 sites per call"; analysts say it has no index of its
  own), Linkup ($5 to $6 per 1K, "personalized indexes", self-reported 94% on SimpleQA Verified), You.com ($5 per
  1K, "licensed data providers"), mcp-omnisearch fanning out to seven backends.
- Artificial Analysis Search Index, 2026-10-19: Exa auto 80 and Perplexity medium 80, Octen 77, Parallel
  advanced 75, Brave 75, OpenAI Web Search 74 ($40 per 1K tasks), You.com 74, Nimble 74, Firecrawl 73; a
  model-only baseline scores 33. No SERP wrapper is on the board.
- Correction to the orientation entry: the "OpenAI web search 57.7% on BrowseComp" figure that the first web
  search summarized was not found on any Parallel page fetched; treat it as unverified.

**Gaps for wave 2**
- Who is Octen (new on the Artificial Analysis board)? Independent latency data for SERP wrappers; current
  disclosure of OpenAI's and Anthropic's index providers; Nimble's price conflict; HN threads on the Bing
  retirement.

**Spend**
- Tracker: TOTAL        120    547816    2645463    12422520    3250    92.76    83.44 budget $240: 39% used (high estimate), 35% (low estimate)  Five threads still running.

## 2026-11-05 00:44 UTC. Wave 1, thread 5 back: market positioning and UVP

**Done**
- Committed `uvp_and_market.md` (verbatim homepage positioning for 13+ vendors, funding, practitioner sentiment
  from HN threads fetched directly, market analysis).

**Found**
- Funding and traction: Exa $250M Series C at $2.2B (a16z, 2026-05-20), claims $100M annualized revenue and 2B
  requests a month (Sacra: about $14M ARR end-2025, about $100M September 2026). Parallel $100M Series A at $740M
  (November 2025), $100M Series B at $2B (Sequoia, 2026-04-29). Tavily $20M Series A (Insight, August 2025), then
  acquired by Nebius for about $275M (Bloomberg, announced 2026-02-10), claims 3M+ developers and 300M+ monthly
  requests. Keenable $26M seed (2026-08-25). You.com $100M Series C at $1.5B (September 2025), 1B+ API queries a
  month, customers DuckDuckGo, Windsurf, Harvey. Firecrawl $75M Series B (2026-09-22). Jina acquired by Elastic
  (2025-10-09). Linkup $10M seed (February 2026). New entrants: Octen ($10M, April 2026), DeepSeek search API at
  $0.75 per 1K (October 2026), Cloudflare Web Search API reselling Exa, Linkup and Ceramic at no markup
  (2026-10-02). Brave removed its free tier in February 2026 and is a confirmed Anthropic subprocessor. Kagi API
  $12 per 1K; Mojeek £2 to £3 per 1K.
- Positioning shifts: Tavily no longer calls itself "the search engine for agents" but a "web access layer";
  Linkup dropped "licensed premium content" from its homepage for "industry-leading accuracy, deploy in your own
  cloud"; Brave says "index size is a vanity stat"; Keenable, Parallel and Exa all explicitly claim their own
  index. $5 per 1K is the anchor price, with $1 and sub-$1 tiers appearing in 2026.
- Practitioner sentiment (HN): Exa is the quality reference (competitors call it "the market leader") but
  criticized for price, per-result add-ons and zero-data-retention as a paid feature; Brave is the pragmatic
  default but resented for the free-tier removal; vendor benchmarks are widely distrusted ("reward hacking"); an
  explicit race-to-the-bottom debate followed DeepSeek's launch.
- Market structure: Bing API retired 2025-08-11 and Google's Custom Search JSON API closes 2027-01-01, while
  Google routes third-party grounding to Exa (private preview, April 2026) and Parallel. Cloudflare moved from
  default-blocking AI crawlers (2025-07-01) to accusing Perplexity of stealth crawling (2025-08-04) to default
  blocking of AI agents and mixed-use crawlers on ad-supported pages with "Pay Per Use" (2026-09-15). Google sued
  SerpApi under the DMCA on 2025-12-19 (motion to dismiss 2026-02-20). a16z's "Search Wars" (November 2025):
  a multi-winner market competing on speed, pricing and ease of integration, with deep research the most
  monetizable layer.
- Where differentiation really is: leaderboards flip monthly (Artificial Analysis: Perplexity top in September
  2026, Exa 3.0 top in October 2026; Vals: Exa first in July 2026, Keenable first in October 2026 by 0.63 points,
  "not established as statistically significant"). Vals shows search itself moves accuracy from 3% to 7% to 30% to
  50%, and about 95% of per-task cost is model tokens, so queries per task (Exa 7.6, Brave 12.4, Firecrawl 15.4)
  and extraction quality matter more than the headline price per 1K. An own index drives price floors, storage
  rights and legal insulation rather than accuracy: aggregator Tavily matches own-index vendors on SimpleQA in
  Parallel's own tables.

**Gaps for wave 2**
- Reddit threads (budget exhausted), named engineers' posts, Linkup's current SimpleQA score and publisher list,
  Google's 2026-01-20 announcement body, SerpApi case status after February 2026, the Artificial Analysis primary
  page (404 for this thread; figures were vendor-relayed).

**Spend**
- Tracker: TOTAL        123    554434    2818642    12871170    3316    97.00    87.35 budget $240: 40% used (high estimate), 36% (low estimate)  Four threads still running.

## 2026-11-05 00:45 UTC. Wave 1, threads 6 and 7 back: Common Crawl versus commercial; own-index providers

**Done**
- Committed `common_crawl_vs_commercial.md` and `providers_own_index.md` (412 lines, 19 sections, a 27-row
  comparison table).

**Found: Common Crawl versus a commercial index**
- Scale in 2026: the October crawl (CC-MAIN-2026-43) holds 2.16B pages, 371 TiB uncompressed, 41.4M hosts, with
  about 38% never-before-seen URLs; the per-crawl size fell about 29% from 3.03B pages in early 2025 to about
  2.15B in 2026 (cause unidentified). Cumulative archive over 300B pages; English is 42.6% of pages.
- Selection mechanics (Mozilla's 2024 interviews with Common Crawl staff): a CrawlDB of about 25B URLs, domains
  ranked by harmonic centrality (chosen over PageRank for spam resistance), a per-domain budget scaled by
  centrality, a fixed per-crawl cap ("if we 10x that, quality would drop"), about half of each crawl revisits,
  "samples of samples, never whole sites", politeness that leaves highly ranked domains under-represented, no
  JavaScript, no cookies, no paywalls.
- What it lacks: only URL-lookup indexes (the rate-limited CDXJ server and a Parquet URL index), no inverted index,
  no embeddings, no ranking signals beyond host-level centrality, no snippets, no rendering, no sub-second
  serving. Measured provider latencies (Perplexity, September 2025): Perplexity p50 358 ms, Brave 513, Tavily
  1,342, Exa 1,375.
- Building search on it: Elastic ChatNoir (2018) indexed 1.6B pages on 124 Elasticsearch data nodes, 9.7 TB index
  plus 28.8 TB document store, 115.6 TB on disk at 3x replication, about 600 ms warm queries; a 2018 tantivy
  experiment built a 13 TB BM25 index over 3.2B pages for under $50 of compute but about $400 a month of S3. Stract
  used Common Crawl only to bootstrap, then its own crawler (repository archived 2026-04-02). Marginalia runs its
  own crawl on one server at about $200 a month. The EU's Open Web Index project (€8.5M, ended 2026-02-28) argues a
  focused own crawl is cheaper than indexing a Common Crawl-sized collection and crawls over 30M pages a day.
  Common Crawl's real downstream success is LLM corpora (FineWeb 15T tokens, RefinedWeb, DCLM).
- Commercial sizes: Google "hundreds of billions" of pages; Brave 30B+ pages with 100M+ updates a day (vendor);
  Mojeek 9B+; Exa 80B to 100B documents and 1.4T URLs tracked (vendor; the CEO concedes figures are not
  comparable); Keenable 100B+; Perplexity over 200B URLs tracked. No official Bing or Yandex totals.
- CCBot blocking: 26% of the top 1,000 sites have CCBot robots rules (2026-11-04); 37.4% of 107 prominent
  publishers block it (June 2026), including NYT, BBC, Guardian, Amazon, LinkedIn; CCBot is second only to
  Bytespider on block-to-allow ratio in Cloudflare Radar (September 2026). No evidence that Exa, Keenable,
  Brave, Mojeek or Perplexity use Common Crawl; all say they run their own crawlers.

**Found: own-index providers**
- Confirmed own crawler and index (crawler named): Brave (30B+ pages; $5 per 1K; LLM Context endpoint launched
  2026-02-12 with p90 under 500 ms; official MCP), Mojeek (9B pages; £2 to £3 per 1K; EU-only infrastructure),
  Perplexity (PerplexityBot; over 200B URLs; Search API launched 2025-09-25 at $5 per 1K, $1 fast; vendor p50
  358 ms, p95 763 ms; vendor SimpleQA 0.930; official MCP), Yep by Ahrefs (100B pages, 8B crawled a day; $4 per
  1K with 20 results), Valyu (HenkBot; about $0.63 per 1K results), Yandex, Marginalia (about 300M documents),
  Stract, Mwmbl ($5 per 1K, under 200 ms), Kagi (Teclis and TinyGem indexes at $2 per 1K; the full Search API
  at $12 per 1K blends all major providers plus Marginalia).
- Own index claimed, crawler and size undisclosed: Parallel ("billions of pages, millions updated daily"; turbo
  and fast $1 per 1K at about 200 and 700 ms, basic and advanced $5 per 1K at about 1 and 3 s), Linkup ("our
  index" plus premium data partners; $5 standard, $50 deep per 1K), EUSP Staan (Qwant and Ecosia joint venture;
  €2 per 1K; p95 under 800 ms), Octen (launched 2026-04-22, $10M seed; "indexed within 5 minutes", 62 ms p50,
  $1 per 1K; Artificial Analysis 77 at the lowest cost and time; invite-only).
- Evidence points to third-party aggregation: Tavily (Sacra: "does not maintain its own search index";
  Perplexity labelled it SERP-based; Tavily says "agent-native index" plus caching), Jina s.jina.ai, Nimble
  (scrapes "major search engines" with a proprietary cache), You.com (bills only live crawls; no size or
  crawler), Firecrawl /search (web engine unnamed; own vertical indexes of 113M+ sources).

**Gaps for wave 2**
- Artificial Analysis scores for Tavily, Linkup, Valyu, Kagi, Mojeek; Brave's circulating 40B figure has no
  primary source; official MCP status for Linkup, Valyu, Firecrawl; Octen's background; Yandex and Bing sizes.

**Spend**
- Tracker: TOTAL        124    557093    2827173    13070108    3318    97.50    87.70 budget $240: 41% used (high estimate), 37% (low estimate)  Two threads still running (head-to-head results, MCP ecosystem).

## 2026-11-05 00:46 UTC. Pricing confirmed

- Anthropic's official pricing page lists Claude Fable 5.1 at $10 per million input tokens, $12.50 for 5-minute
  and $20 for 1-hour cache writes, $0.25 for cache reads, and $50 per million output tokens. The tracker's
  "official" column is therefore the right estimate; the earlier high column ($1 cache reads) is kept only as a
  conservative upper bound. Every previous entry's lower figure is the one to read.

## 2026-11-05 00:49 UTC. Wave 1, thread 8 back: published head-to-head results

**Done**
- Committed `head_to_head_results.md` (about 98 KB, 89 unique sources; every number dated and labelled vendor or
  independent, with harness and reproducibility notes).

**Found**
- Parallel's series is four distinct runs, not one. (a) July 10 to 12, 2026: GPT-5.4 agent and judge, 20 tool
  calls, all 1,266 BrowseComp questions, "best observed across sessions": Parallel Turbo 51% BrowseComp, 91%
  SimpleQA; Exa Instant 33.7% and 89.3%; Tavily Ultra Fast 19.3%; SerpApi 23.3% and 76.7%; OpenAI web search
  57.7% BrowseComp (so the figure flagged earlier does exist on a live page). The Brave 38.3% figure appears only
  in a search snippet, not on any live Parallel page. (b) 2026-08-26 Task API run (n=100): Parallel Ultra4x 94%,
  Perplexity high 86%, Exa Agent Max 78%. (c) 2026-09-09 Search API run: GPT-5.6 Sol high and Luna low, n=50
  BrowseComp, n=100 SimpleQA Verified, n=100 WideSearch, unnamed judge: Parallel Advanced 74% at $399 per 1K,
  Perplexity 74% at $275, Exa Auto 70% at $971, Tavily 66% at $935; SimpleQA Verified 91% to 97% for every
  product. (d) October 2026 finance runs on GPT-6 Sol. Between July and September Parallel changed the agent,
  the sample (1,266 to 50), the judge, best-of reporting and the competitor tiers (fastest modes to default),
  and publishes no judge prompt, sample IDs, variance or code.
- Artificial Analysis Search Index, complete tables. Launch 2026-08-18 (11 configurations, 7 providers): Parallel
  advanced 75, Exa auto 74, Firecrawl 73, Parallel basic 73, Exa fast 68, You.com 68, Parallel turbo 67, Keenable
  pro 67, Keenable realtime 67, Tavily basic 66, Brave 65. As of 2026-10-19: Exa auto 80, Perplexity medium 80,
  Exa lite 79, Perplexity high 79, Octen 77, Parallel advanced 75, Brave LLM context 75, OpenAI 74, You.com 74,
  Nimble 74, Firecrawl 73, DeepSeek 69. Brave's 65 to 75 was an endpoint switch; Exa's 74 to 80 was Exa 3.0's
  dynamic highlights. Updates observed on Aug 18, Sep 8, 22, 28, Oct 6 and 19; cadence undocumented.
- Keenable's NEEDLE: full standings for 23 engines (7-day mean share of an oracle ceiling, p50 and p95, dollars
  per 1K, error rates; vendor-run with a GPT-6 Luna judge), with methodology and per-vertical leaders.
- Vendor self-reports collected with harnesses: Tavily repo 93.3% SimpleQA against Perplexity 85.9, Serper 82.2,
  Brave 76.1, Exa 71.2 (retrieval-only); Tavily August 2026 97.6% SimpleQA, 49.5 SealQA; Linkup 94% SimpleQA
  Verified; Firecrawl 94.7% (best of two sessions, no competitors); Brave FreshQA 85.3% at $18 per 1K against
  Parallel 79.0% at $49, Exa 78.0% at $84, Tavily 78.0% at $89; Perplexity's September 2025 latency table; You.com
  95.17% SimpleQA with highlights.
- Independent: OpenBenchmarks three-task tables for 13 vendors with an ordering-bias caveat; AIMultiple's 8-API
  table with confidence intervals; BrowseComp-Plus has a single commercial data point (GPT-5 with the Google
  Search API, 59.9%); Search Arena April 2025 had Gemini 2.5 Pro grounding at 1142 against Perplexity's
  Sonar Reasoning Pro at 1136 (the 2026 board was inaccessible). No reproducible community mini-benchmark found.
- Why the same product spans 32% to 91.8% on BrowseComp and 71% to 97.6% on SimpleQA: agent model, reasoning
  tier, sample size, tool budget, judge, product tier and best-of reporting, all mapped in the notes.

**Gaps for wave 2**
- Brave 38.3% unconfirmed; the full 26-row Artificial Analysis table (only 12 rows extractable); Jina, Nimble and
  Bright Data head-to-heads; Search Arena 2026 standings; ATLAS per-provider results.

**Spend**
- budget $240: $97.56 = 41% used at official prices ($108.86 = 45% with cache reads at $1/M). One thread still running (MCP ecosystem).

## 2026-11-05 00:52 UTC. Wave 1 complete, thread 9 back: MCP ecosystem

**Done**
- Committed `mcp_ecosystem.md`. All nine wave-1 note files are now in the repository (about 630 KB of sourced notes).
- Checked that web search still works from the coordinating session; the researchers' "shared budget exhausted"
  reports describe a per-agent cap (the notes record a 200-call session cap for Claude Code's WebSearch tool).

**Found: MCP ecosystem (counters observed 2026-11-05)**
- GitHub stars: Apify 14,791, Firecrawl 7,764, Exa 5,212, Bright Data 2,710, Perplexity 2,608, Tavily 2,478,
  Brave 1,561, DuckDuckGo community server 1,567, SearXNG 1,345, Jina 902, Kagi 558, mcp-omnisearch 358, SerpApi
  183, Keenable 6. Context7 (docs search) 64,201.
- npm weekly downloads: context7 741k, firecrawl-mcp 147k, exa-mcp-server 76k, Brave 59k, Perplexity 42k, Apify
  31k, tavily-mcp 24k, Bright Data 18k, mcp-searxng 15k, Keenable 128. PyPI monthly: the reference fetch server
  506k, duckduckgo-mcp-server 72k. No registry publishes install or call counts; Smithery shut its proxy on
  2026-10-31.
- Hosting: nearly every vendor runs a hosted Streamable-HTTP endpoint (Exa, Tavily, Perplexity, Firecrawl, Jina,
  Kagi, Linkup, Parallel, Bright Data, Apify, Oxylabs, SerpApi, ZenRows, You.com, Keenable, Nimble); Brave is the
  holdout (local only). Keyless tiers: Keenable (1,000 requests per hour per IP), Parallel, Exa (IPv4 only),
  Firecrawl, Tavily, You.com. OAuth: Perplexity, Tavily, Exa, Firecrawl, Parallel, Keenable, Apify, ZenRows.
- Tool surfaces converge on search, fetch or extract, map or crawl, and an async research or agent tool; vendors
  are pruning tools (Jina removed eight, Exa dropped company and people tools, Kagi removed FastGPT).
- First-party search pricing: Anthropic $10 per 1K searches (web fetch free; Claude Code's WebSearch uses it with
  a 200-call session cap); OpenAI $10 per 1K on reasoning models, $25 per 1K preview on 4o-class; Google $14 per
  1K after 5,000 free a month on Gemini 3 ($35 on 2.5); xAI $5 per 1K. Codex's web_search defaults to a "cached"
  OpenAI index. Cursor's @Web is reported (third party only) to run on Exa.
- Skills and CLIs as the alternative to MCP: the Agent Skills open standard (2025-12-18), Keenable's SKILL.md and
  Homebrew CLI, Firecrawl's CLI and skills, Brave's bx CLI, Nimble's 13 skills, Parallel's CLI, Tavily's CLI; Exa,
  Tavily and Keenable all shipped Antigravity and Gemini CLI plugins in October and November 2026.

**Wave 1 summary**
- Nine threads, about 900 tool calls, roughly 1.9M subagent tokens of transcript, 10 to 21 minutes each; the
  whole wave ran from 00:28 to 00:52 UTC. Cost of
  the whole session so far is in the tracker line below.
- The picture that emerges: (1) the independent boards (Artificial Analysis, Vals, OpenBenchmarks) rank Exa,
  Perplexity, Parallel, Keenable and Brave at the top, but the leaders swap monthly and the gaps are within noise;
  (2) an own index is a cost, freshness, storage-rights and legal-insulation story more than an accuracy story,
  since aggregators (Tavily, Linkup) match own-index vendors on SimpleQA; (3) what moves agent accuracy is
  queries per task, result-text quality (full content, highlights, dynamic snippets) and latency, because about
  95% of per-task cost is model tokens; (4) Common Crawl is a sampled, politeness-limited monthly archive with
  no inverted index, no ranking and no serving layer, and none of the commercial providers admits to using it.

**Next: wave 2**
- Six gap-filling threads (Keenable depth, Perplexity and Parallel, Brave and Tavily under the hood, 2026
  newcomers, the independent boards in full, practitioner sentiment), each followed by a skeptic that re-fetches
  its top claims, plus three verifiers over about 33 load-bearing wave-1 numbers. Then the report.

**Spend**
- budget $240: $103.04 = 43% used at official prices ($114.71 = 48% with cache reads at $1/M)

## 2026-11-05 00:56 UTC. Wave 2 launched as a workflow

- Script saved as `research_notes/wave2_workflow.js`. Six researchers (Keenable depth; Perplexity and Parallel;
  Brave and Tavily under the hood; 2026 newcomers; the independent boards in full; practitioner sentiment) each
  write a `wave2_*.md` note and return their five most load-bearing claims; a skeptic then re-fetches those
  claims and appends a verification table to the same file. In parallel, three verifiers re-check 34 wave-1
  numbers from primary sources and write `verification_wave1_{A,B,C}.md`. Verdicts are CONFIRMED, CORRECTED,
  UNVERIFIABLE or REFUTED, with UNVERIFIABLE as the default under uncertainty.
- Tool budgets are capped (35 calls per researcher, 15 per skeptic, 35 per verifier) to keep wave 2 near $60.
- The spend tracker now also sums the workflow agents' transcripts.
- Correction (00:58 UTC): the entry times above were first written as estimates and have been replaced with the
  commit times. The workflow runs at most two agents at a time on this 4-CPU container (the Agent tool had no such
  cap in wave 1), so wave 2 will take about 45 minutes of wall-clock time at the same cost.

## 2026-11-05 01:35 UTC. Wave 2 complete: six gap-filling notes, nine verification tables

**Done**
- The workflow ran 15 agents (370 tool calls, about 1.4M subagent transcript tokens) in 36 minutes. Committed
  `wave2_keenable_depth.md`, `wave2_perplexity_parallel.md`, `wave2_brave_tavily.md`, `wave2_newcomers.md`,
  `wave2_independent_boards.md`, `wave2_practitioner_sentiment.md` (each ending in a skeptic's verification
  table) and `verification_wave1_{A,B,C}.md`.

**Verification tally: 68 claims re-checked against primary sources**
- 56 CONFIRMED, 7 CORRECTED, 5 UNVERIFIABLE, 0 REFUTED. The corrections:
  - Tavily's sale to Nebius: Nebius says "the transaction value has not been disclosed"; the $275M figure is
    Bloomberg's reporting, not an announced price.
  - Exa 3.0 (2026-10-19) introduced only the Lite search type; Auto dates from December 2024 and Deep from
    November 2025.
  - Keenable's crawler page lists two user agents, KeenableBot and Keenable-User (RFC 9309 compliance stated),
    not three.
  - Artificial Analysis time per task: Exa auto 36.5 s, Perplexity medium 30.9 s, Octen 15.5 s (the notes had
    36.9, 31.4 and 15.8).
  - Search Arena, April 2025: the arXiv paper's table gives Gemini 2.5 Pro grounding 1150.6 and Sonar Reasoning
    Pro High 1150.1, not 1142 and 1136.
  - Keenable's founders: TechCrunch describes Styskin as ex-head of Yandex search, AI and cloud with 20 years at
    Yandex and Amazon, and Petri as a German AI scientist; the "100B+ documents" and "15 engineers" figures are
    the company's, not quotes.
- Unverifiable: the 37.4% publisher CCBot-blocking figure (vendor blog not fetched), GitHub star counts (API
  blocked for the verifier), the exact default of Claude Code's per-session web-search cap (the binary has the
  setting `CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION`), and the April 2025 Search Arena numbers.

**Found: wave 2**
- Keenable, why strong. The founders have disclosed almost nothing mechanistic. Styskin to TechCrunch: scanning
  the whole web is "painfully expensive", so Keenable "narrow[s] the search space based on your query very fast"
  with index structures tuned per task. The NEEDLE post calls Keenable "a learning machine" and gives the
  timeline: first index February 2026, news April, query syntax May, snippets June. Vendor latency p50 200 ms;
  Artificial Analysis independently measures 0.34 s per call, the fastest on its board, while scoring Keenable
  realtime 67 against Exa auto 74 at launch. Dynamic Snippets (2026-10-15) is the one fully documented component:
  a query-conditioned token classifier that cut responses from 135 to 69 KiB and, in vendor runs, BrowseComp
  tokens from 1.16M to 466k with accuracy 56.6% to 67.3%. The Vals board ran Keenable with a single model;
  77% of its finance citations were SEC filings. Practitioner signal is HN-only: positive on speed and price,
  skeptical of the vendor-run NEEDLE. First-stage retrieval (lexical, dense or hybrid) is undisclosed.
- Perplexity and Parallel. On the 2026-10-19 Artificial Analysis board Perplexity medium ties Exa auto at 80;
  its lead over Parallel (75) is BrowseComp (87 against 77) while both score 81 on DeepSearchQA; search cost
  $62.30 against $47.93 per 1K tasks. Perplexity's index (vendor, 2025-09-25): PerplexityBot, over 200B URLs,
  exabyte scale, hybrid lexical and semantic retrieval, sub-document spans, cross-encoder rerankers, 50 QPS flat.
  Its search_evals repository now benchmarks the Agent API (BrowseComp 0.805 against Parallel's Task API 0.56).
  Cloudflare alleged a stealth Chrome-UA crawler at 3M to 6M requests a day; Perplexity attributed it to
  BrowserBase and says Perplexity-User ignores robots.txt by design.
- Brave and Tavily. Brave has been 100% own-index since April 2023 (the removed Bing calls supplied about 7% of
  results) and now states "no fallback to another search engine for any query". Index-size claims went from "over
  30 billion" (2023, repeated 2025) to "40 billion" (2026-02-24) to no number ("a vanity stat"). LLM Context
  (2026-02-12) does search plus extraction plus chunk ranking under a 1k to 33k token budget, under 500 ms p90
  claimed. The free plan became a $5 monthly credit requiring a card and attribution; the old free terms
  prohibited AI inference. Brave's own SimpleQA F1: 92.1% single search, 94.1% multi-search. Anthropic added
  Brave as a subprocessor on 2025-03-19. For Tavily, Sacra's "does not maintain its own search index" stands
  against Tavily's claim of billions of pages crawled plus caching; the "SERP-based" accusation remains unproven.
- Newcomers. Octen (APITECH AI Pte Ltd, Singapore; founder Kuan Zou, ex-Alibaba Cloud and Baidu search) is now
  self-serve at $1 per 1K with MCP, skill and CLI; Artificial Analysis: Octen 77 at $9.07 per 1K tasks against Exa
  auto 80 at $53.17, Nimble 74 at $46.14, DeepSeek 69 at $8.47. DeepSeek's search is $0.75 per 1K on an "in-house
  search engine". Cloudflare's Web Search API resells Ceramic.ai at $0.25 per 1K (default, zero data retention,
  40B+ pages claimed; founders ex-Google VP Anna Patterson and Cuil founder Tom Costello), Exa at $7 and Linkup at
  $5, at list price. Nimble's price is $1.10 per 1K. Staan (Qwant and Ecosia) €2 to €4 per 1K under 800 ms p95.
- Independent boards. Artificial Analysis covers 26 configurations from 14 providers (Valyu, Kagi and Mojeek
  absent); at launch Tavily basic scored 66 at the highest search cost ($126 per 1K tasks); the model-cost column
  is 3 to 4 times lower in October for identical sub-scores, unexplained. Vals: 208 legal and 450 finance tasks,
  no July run found. AIMultiple (100 queries): Brave 14.89, Firecrawl 14.58, Exa 14.39, Parallel Pro 14.21, Tavily
  13.67, Perplexity 12.96, SerpApi 12.28, with the top four inside overlapping confidence intervals.
- Practitioners. Reddit, X and the Brave status page were unreachable from this session (a hard gap). Exa's
  keyword weakness is attested by three independent write-ups (one mini-benchmark: Exa fastest at 137 ms but 3.2
  of 10 on keyword relevance); Exa's status page shows six incidents from September to November 2026 (longest
  4 h 56 min), Tavily, Perplexity and Parallel none. Keenable has no practitioner reports beyond HN.

**Next**
- Report writer, then an independent review of the report against the notes, then the final Journal entry.

**Spend**
- budget $240: $138.48 = 58% used at official prices ($156.66 = 65% with cache reads at $1/M)

## 2026-11-05 01:50 UTC. Report drafted

- `reports/Search API landscape and benchmarks.md`: about 14,300 words, 98 inline citations, eleven sections plus
  a bottom-line-up-front and a conclusion; a 24-row benchmark table and a 27-row provider table; dedicated
  sections on Keenable, Exa, Common Crawl versus commercial indexes, UVP per provider, methodology caveats, open
  gaps, and a section relating the findings to this repository's own benchmarks. The writer applied the
  verification verdicts (corrected values used, unverifiable figures marked) and notes that the README's
  `../benchmark/` directories are not in this checkout.
- Next: an independent adversarial review of the report against the notes (claim audit, verification
  compliance, completeness, consistency), then fixes, then the final entry.
- budget $240: $163.42 = 68% used at official prices ($183.98 = 77% with cache reads at $1/M)
