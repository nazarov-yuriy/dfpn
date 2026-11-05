# Head-to-head results: web-search APIs for AI agents (2025 – 5 Nov 2026)

Scope: every published numeric comparison of search-API providers against each other that I could locate, with harness, model, date, author (vendor vs. independent) and reproducibility noted per result. Numbers from different runs are kept in separate tables; where I pull several runs into one table for a single provider, each row names its run. "Vendor" = authored by a company that sells one of the compared products. All dates are publication/run dates as stated by the source. Research cut-off: 2026-11-05. The web-search budget for this session was exhausted during the last fetch wave, so a few vendor blogs (Jina, Nimble, Bright Data, Brave blog archive) were not fully checked; see Gaps.

---

## Key Question 1 — Parallel.ai's comparison series: July 2026 run, September 2026 run, "five-engine" report, finance runs; what changed between runs

### Takeaway
Parallel has published at least four distinct vendor-run head-to-head series (July 10–12 2026 "Turbo launch" run on GPT-5.4; Aug 26 2026 Task-API run; Sept 9 2026 Search-API run on GPT-5.6 Sol/Luna; Oct 22–28 2026 finance runs on GPT-6 Sol) plus ~30 SEO-style articles that recycle those numbers alongside Artificial Analysis and Openbenchmarks figures. The July and September BrowseComp numbers differ mainly because the agent model (GPT-5.4 → GPT-5.6), reasoning tier, sample size (1,266 → 50), scoring rule (best-of-sessions → unstated) and competitor product tiers (Instant/Ultra-Fast/SerpApi → Auto/default/Perplexity) all changed; Parallel never published judge prompts, sampled IDs or run variance, so none of its runs is independently reproducible.

### Cited Findings

**1A. July 2026 run ("Turbo launch run", run July 10–12 2026) — vendor (Parallel)**

Harness as stated: GPT-5.4 agent, up to 20 search+fetch tool calls per question, GPT-5.4 judge, "best observed per provider across sessions"; BrowseComp on all 1,266 questions; SerpApi ran search-only (no fetch tool); search latency = client-side p50 from us-central. Question counts for non-BrowseComp suites not stated. — [Parallel vs SerpApi compare page](https://parallel.ai/compare/serpapi-vs-parallel); [Parallel vs Exa compare page](https://parallel.ai/compare/exa-vs-parallel); [Parallel vs Tavily compare page](https://parallel.ai/compare/tavily-vs-parallel) (all "last updated Oct 16 2026").

| Product (fastest tiers) | BrowseComp | SimpleQA | HLE | WebWalker | Coding | p50 search latency | Measured cost / 1k BrowseComp Qs (tokens + tools) | Source |
|---|---|---|---|---|---|---|---|---|
| Parallel Turbo | 51% | 91% | 52.7% | 75.7% | 79.7% | 216 ms (BrowseComp run), 240 ms (SimpleQA run); 216–240 ms across five suites | $350 | [serpapi-vs-parallel](https://parallel.ai/compare/serpapi-vs-parallel), [exa-vs-parallel](https://parallel.ai/compare/exa-vs-parallel) |
| Exa Instant | 33.7% | 89.3% | — | — | — | 335–361 ms p50 across the same five suites (361 ms on BrowseComp) | not stated | [exa-vs-parallel](https://parallel.ai/compare/exa-vs-parallel) |
| Tavily Ultra Fast | 19.3% | — | — | — | — | 150–357 ms p50 (faster than Turbo on 2 of 5 suites; less accurate on all 5) | not stated | [tavily-vs-parallel](https://parallel.ai/compare/tavily-vs-parallel) |
| SerpApi (search-only) | 23.3% | 76.7% ("equal content budget") | 40% | 50.7% | 54% | 999 ms (BrowseComp run), 652 ms (SimpleQA run) | $296 | [serpapi-vs-parallel](https://parallel.ai/compare/serpapi-vs-parallel) |
| OpenAI Web Search | 57.7% | — | — | — | — | — | — | cited "in the same run" against Parallel Task Ultra8x at 58% — [exa-vs-parallel](https://parallel.ai/compare/exa-vs-parallel) |
| Brave | **38.3% — not confirmed.** This figure appeared only in a search-engine snippet attributed to a Parallel article ("the best result of any tool here outside Parallel and OpenAI"); none of the Parallel pages I fetched on 2026-11-05 (compare/brave-vs-parallel, articles/brave-search-api-vs-parallel, parallel-vs-serpapi-vs-brave-vs-bing, best-ai-search-for-agents, best-web-search-api) contains it. The only Brave "38" on current Parallel pages is Openbenchmarks' 38.0% coding-agent task completion. | | | | | | | [compare/brave-vs-parallel](https://parallel.ai/compare/brave-vs-parallel) |

Other July-run cost rows (per 1k questions, Parallel Turbo vs SerpApi): HLE $298 vs $250; WebWalker $82 vs $124; SimpleQA $8 vs $6; Coding $131 vs $131 — [serpapi-vs-parallel](https://parallel.ai/compare/serpapi-vs-parallel).

- Parallel's Exa page states: "Exa publishes its own runs with different configurations and results." — [exa-vs-parallel](https://parallel.ai/compare/exa-vs-parallel)
- Exa's own version of the same era (June 2026) puts Exa Agent High at 74% on BrowseComp (1,266 Qs) at $0.50/task vs Parallel Task Ultra 8x 58% at $2.40 — a comparison of Exa's agent product with Parallel's Task API, not the search APIs — [Exa vs Parallel](https://exa.ai/versus/parallel) (vendor: Exa).

**1B. August 26 2026 Task-API (deep-research) run — vendor (Parallel)**

Fixed 100-question subsets; cost = end-to-end spend ÷ questions; agent/harness for Parallel tiers not tied to a named model; competitor arms are complete research agents. — [parallel.ai/benchmarks](https://parallel.ai/benchmarks)

| System | BrowseComp (n=100) | $/1k | DeepSearchQA (n=100, accuracy) | $/1k |
|---|---|---|---|---|
| Parallel Ultra4x | 94% | $1,200 | 86% | $1,200 |
| Parallel Ultra2x | 93% | $600 | 85% | $600 |
| Parallel Ultra | 92% | $300 | — | — |
| Parallel Pro | — | — | 83% | $100 |
| Parallel Core2x | — | — | 81% | $50 |
| Parallel Core | 91% | $25 | — | — |
| Parallel Base | — | — | 77% | $10 |
| Parallel Lite | 88% | $5 | 76% | $5 |
| Perplexity (high) | 86% | $441.5 | 68% | $371.9 |
| GPT-5.6 Sol PTC (max) | 85% | $791.1 | 85% | $1,047.8 |
| Exa Agent Max | 78% | $1,043.5 | 65% | $1,506.5 |
| Gemini 3.1 Pro (high) | 72% | $194.4 | 77% | $123.9 |

Source: [parallel.ai/benchmarks](https://parallel.ai/benchmarks); DeepSearchQA rows also in [Parallel DeepSearchQA article](https://parallel.ai/articles/deepsearchqa-benchmark). Perplexity's own harness reports BrowseComp 78.0 (high) / 85.33 (xhigh) and DeepSearchQA F1 89.6 / 93.0 for the same product — "different method, not comparable" — [Parallel vs Perplexity compare](https://parallel.ai/compare/perplexity-vs-parallel).

**1C. September 9 2026 Search-API run — vendor (Parallel)**

Harness as stated: frontier tier = GPT-5.6 Sol agent (reasoning high) with Parallel Basic/Advanced; low-cost tier = GPT-5.6 Luna agent (reasoning low) with Parallel Fast/Turbo; every competitor run at both tiers with the same agent; Parallel, Exa, Tavily get search + extract tools, Perplexity search-only; LLM judge (model not named); cost = LLM tokens + tool calls, USD per 1k questions ("CPM"); SimpleQA Verified n=100 (of 1,000), BrowseComp n=50 (of 1,266), WideSearch n=100 tasks (of 200, partial credit). No latency reported. GPT-6 models (released Sept 22 2026) not tested. — [parallel.ai/benchmarks](https://parallel.ai/benchmarks); [How we evaluate web search APIs](https://parallel.ai/articles/how-we-evaluate-web-search-apis)

| Configuration | Tier | SimpleQA Verified (acc / CPM) | BrowseComp (acc / CPM) | WideSearch (score / CPM) |
|---|---|---|---|---|
| Parallel Advanced | Frontier | 97% / $28.3 | 74% / $399 | 57.6 / $692 |
| Parallel Basic | Frontier | 97% / $45 | 72% / $612 | 55.3 / $965 |
| Perplexity | Frontier | 95% / $20.2 | 74% / $275 | 53.5 / $547 |
| Exa Auto | Frontier | 91% / $35.7 | 70% / $971 | 55.9 / $1,061 |
| Tavily | Frontier | 92% / $61.3 | 66% / $935 | 55.9 / $1,072 |
| Parallel Fast | Low-cost | 94% / $2.0 | 44% / $11.8 | 45.5 / $10.5 |
| Parallel Turbo | Low-cost | 91% / $2.0 | 32% / $13.2 | 44.0 / $10.1 |
| Perplexity | Low-cost | 94% / $5.5 | 46% / $37.1 | 47.0 / $24.8 |
| Exa Auto | Low-cost | 91% / $7.9 | 36% / $53.4 | 53.0 / $41.2 |
| Tavily | Low-cost | 94% / $17.4 | 32% / $176 | 47.9 / $107 |

Source: [parallel.ai/benchmarks](https://parallel.ai/benchmarks) (run date Sept 9 2026); identical numbers repeated in [BrowseComp article](https://parallel.ai/articles/browsecomp-benchmark), [SimpleQA article](https://parallel.ai/articles/simpleqa-benchmark), [Best web search API for AI applications](https://parallel.ai/articles/best-web-search-api-for-ai-applications), [Most powerful search API](https://parallel.ai/articles/most-powerful-search-api-for-ai), [Best web search API: 5 tools](https://parallel.ai/articles/best-web-search-api), [Best AI search for agents: 6 APIs](https://parallel.ai/articles/best-ai-search-for-agents).
- Not included in the Sept runs: Brave Search, SerpAPI, OpenAI Web Search, Firecrawl — [Most powerful search API](https://parallel.ai/articles/most-powerful-search-api-for-ai); [Parallel vs Firecrawl compare](https://parallel.ai/compare/firecrawl-vs-parallel).
- Parallel's own caveat: at ~70% accuracy, standard error ≈ 6.5 points at n=50, 4.6 at n=100, 3.2 at n=200; the 2-point low-cost gap is "within sampling noise" — [BrowseComp article](https://parallel.ai/articles/browsecomp-benchmark).
- Not published for these runs: judge model and prompt, tool-call/turn budget, sampled question IDs, agent system prompt, runs per configuration, run-to-run variance, contamination filtering, WideSearch matching rules; whether harness code is open-source is not stated — [How we evaluate](https://parallel.ai/articles/how-we-evaluate-web-search-apis).

**1D. "Best web search API for AI applications: a 2026 benchmark report on 5 engines" — vendor (Parallel)**
- The five engines are Parallel, Perplexity, Exa, Tavily, Brave. Accuracy/cost numbers are the Sept 9 2026 table above (Brave: "Not in runs"); latency is imported from Openbenchmarks (mean, Sept 15 2026 board): Parallel Turbo 348 ms, Exa Instant 398 ms, Brave 601–630 ms (523 ms on hard-retrieval search-only board), Parallel Fast 942 ms ("documented at ~700 ms"), Perplexity (low) 1.38 s, Tavily Basic 1.88 s; AA Search Index (Sept 2026, GPT-5.6 Luna harness): Perplexity medium 80, Octen 77, Parallel advanced 75, Brave LLM context 75, You.com highlights 74, Exa auto 74; Parallel Fast search cost $8.41 per 1k AA tasks (Sept 8 data). No p50/p95 anywhere in the article. — [Best web search API for AI applications](https://parallel.ai/articles/best-web-search-api-for-ai-applications)
- "No engine led on every benchmark at every price tier" is Parallel's own summary of that report — [search-result summary of the same article](https://parallel.ai/articles/best-web-search-api-for-ai-applications).

**1E. October 2026 finance runs — vendor (Parallel)**

Harness: GPT-6 Sol (reasoning high) answer model for Parallel Advanced, Exa Auto, OpenAI native search, Perplexity, Tavily; Parallel Fast on GPT-6 Luna (high) — so the "only variable is the search layer" claim does not hold for the Fast arm; 20 tool-call budget; FinSearchComp T3/T2 scores = mean of 3 runs (Tavily single run); published FinSearchComp answer copies were removed for non-Parallel arms (OpenAI native scored 64.0 T3 / 82.8 T2 before adjustment). Run dates Oct 22 2026 (Tavily Oct 28), FrontierFinance/PWS-Finance Oct 27 2026. — [parallel.ai/benchmarks](https://parallel.ai/benchmarks)

| Arm | FinSearchComp T3 (n=172) acc / CPM | FinSearchComp T2 (n=219) acc / CPM | FrontierFinance (n=220, rubric, 3-judge) / CPM | PWS-Finance (n=174, private, 3-run mean) / CPM |
|---|---|---|---|---|
| Parallel Fast (GPT-6 Luna) | 53.7% / $15.2 | 77.5% / $3.3 | 46.0 / $201.5 | 83.0% / $110.3 |
| Parallel Advanced | 57.4% / $161.1 | 79.9% / $35.1 | 46.8 / $234.2 | 84.3% / $125.5 |
| Exa Auto | 51.4% / $226.2 | 77.9% / $69.9 | 47.2 / $376.3 | 75.9% / $197.6 |
| OpenAI native search | 48.3% / $204.3 | 77.9% / $70.2 | 45.0 / $298.7 | 83.7% / $180.7 |
| Perplexity (Finance + Web; Search API only for FF/PWS) | 50.0% / $347 | 79.7% / $104.6 | 44.3 / $254.3 | 74.3% / $121.9 |
| Tavily | 43.0% / $481.8 | 77.2% / $169 | 42.1 / $470.3 | excluded from plot: 36.4% / $432.1 (date filters on; hit call cap on 77% of Qs) |

Source: [parallel.ai/benchmarks](https://parallel.ai/benchmarks); summarised in [OpenAI web search vs Parallel vs Exa vs Tavily](https://parallel.ai/articles/openai-web-search-vs-parallel-vs-exa-vs-tavily-how-to-choose).

**1F. Earlier Parallel launch benchmark (Nov 2025) — vendor; page now 404**
- HN discussion of "The Parallel Search API" (~12 months before Nov 2026): commenters note the judge was GPT-4.1 and question validity; Parallel staff said the latest Search API benchmarks "were run against GPT-5"; the launch blog URL (parallel.ai/blog/introducing-parallel-search) returned 404 on 2026-11-05 — [HN thread](https://news.ycombinator.com/item?id=45837425).

**1G. Vendor latency/pricing claims by Parallel (not benchmark results)**
- Turbo ~200 ms p50, Fast <1 s (~700 ms in docs), Basic ~1 s, Advanced ~3 s; $1/1k Turbo/Fast, $5/1k Basic/Advanced (+$1 per 1k per extra 10 results); Responses API $10/$50/$250 per 1k (low/medium/high); 600 RPM; $5/month free credits — [Brave vs Parallel article](https://parallel.ai/articles/brave-search-api-vs-parallel); [Recall & accuracy article](https://parallel.ai/articles/which-ai-search-api-has-the-best-recall-and-accuracy).
- Parallel also cites a NewsCatcher benchmark (Parallel Base generator F1 0.406 in Lite tier, won 12 of 32 queries) without further detail — [Recall & accuracy article](https://parallel.ai/articles/which-ai-search-api-has-the-best-recall-and-accuracy).
- Parallel cites OpenRouter runs (Aug–Sept 2026, 25-turn budget): Claude Opus 5 BrowseComp 86.3% (Parallel) vs 89.0% (Perplexity); HLE 68.6% vs 77.4%; GPT-5.6 Sol WideSearch 80.6% vs 84.0%; DeepSearchQA 77.0% vs 76.5% — [Parallel vs Perplexity compare](https://parallel.ai/compare/perplexity-vs-parallel). (I could not locate OpenRouter's primary page; treat as second-hand.)

### Inferences
- What changed July → September: (a) agent model GPT-5.4 → GPT-5.6 Sol (high) / Luna (low); (b) BrowseComp sample 1,266 → 50; (c) judge GPT-5.4 → unnamed LLM; (d) selection rule "best observed across sessions" → unstated; (e) competitor tiers switched from fastest modes (Exa Instant, Tavily Ultra Fast, SerpApi search-only) to default/auto modes plus Perplexity; (f) Parallel's own hero product moved from Turbo to Advanced. These explain why Parallel Turbo is 51% in July but 32% in September (Luna-low agent, n=50), and why Exa goes from 33.7% (Instant) to 70%/36% (Auto, frontier/low-cost).
- Parallel's Sept low-cost tier (GPT-5.6 Luna, low reasoning) yields BrowseComp scores (32–46%) far below Artificial Analysis's GPT-5.6 Luna (medium) Stirrup harness on a *harder* 200-question subset (63–87), indicating Parallel's low-cost harness is substantially weaker than AA's and that Parallel's absolute numbers should not be compared across sources.
- Parallel's SEO articles (~30) do not add new runs; they re-mix the Sept 9 run with Openbenchmarks and AA numbers. The "6 APIs benchmarked" and "5 tools compared" titles overstate what was run (Brave/SerpAPI/OpenAI are described, not run).

### Gaps
- Brave 38.3%, and whether Brave/Tavily Ultra Fast were run on all 1,266 BrowseComp questions in July, could not be confirmed from any live Parallel page; the search snippet could be from a since-edited page.
- No Parallel page states the SimpleQA question count, HLE/WebWalker/Coding suite sizes, or the number of sessions behind "best observed" in the July run.
- Parallel's Nov 2025 launch benchmark page (GPT-5 agent, GPT-4.1 judge) is no longer online; its numbers are unrecoverable here.
- Parallel publishes no p95 latency anywhere; its only percentile is p50 for Turbo/Exa Instant/Tavily Ultra Fast/SerpApi (July run).

---

## Key Question 2 — Artificial Analysis Search Index: products, scores, accuracy, latency, cost, task set, weighting, update cadence

### Takeaway
The AA Search Index (launched Aug 18 2026) runs the same GPT-5.6 Luna (medium) agent in AA's open-source Stirrup harness and swaps only the search API; the score is the equal-weighted mean of DeepSearchQA F1 (900 tasks), BrowseComp accuracy (200-hard subset) and AA-Omniscience accuracy (600 private Qs). Coverage grew from 11 configurations/7 providers (launch) to 26 products/14 providers (Oct 19 2026 page) and 27 products (DeepSeek debut); the top moved from Parallel advanced (75) at launch to Exa auto/Perplexity medium (80) by Oct 19 2026. AA does not state an update frequency; observed data drops were Aug 18/19, Sept 8, Sept 22, Sept 28, Oct 6, Oct 19 2026.

### Cited Findings

**Methodology (independent — Artificial Analysis)**
- Candidate model GPT-5.6 Luna (medium) for every provider; harness = Stirrup (AA's open-source agent harness); tools `web_search` (sends query to provider, returns native payload, `max_results=10`, filters known contamination sources), `web_fetch` (15-second page extraction timeout), `finish`; 25-turn limit (all 25 turns without `finish` = 0) — [AA launch article](https://artificialanalysis.ai/articles/search-api); [AlphaSignal on OpenAI debut](https://alphasignal.ai/news/openai-web-search-scores-74-but-loses-on-cost-to-cheaper-rivals).
- Index = equal-weighted mean of DeepSearchQA (900-task full eval split, LLM-graded F1 over answer items), BrowseComp (hard 200-sample subset of 1,266, exact-answer check), AA-Omniscience (600 private questions, 6 domains) — [AA launch article](https://artificialanalysis.ai/articles/search-api); [AA leaderboard](https://artificialanalysis.ai/agents/search-api).
- Cost per task = provider list price × searches run + candidate model token cost; time per task = measured search time + model time (answer+reasoning tokens ÷ model's canonical output speed) — [AA launch article](https://artificialanalysis.ai/articles/search-api).
- Model-only baseline (no search): index 33 (DSQA 45, BrowseComp 17, Omniscience 38), $2.92/1k tasks — [AA leaderboard](https://artificialanalysis.ai/agents/search-api).
- OpenAI Web Search is the first integrated first-party tool on the board; it bypassed Stirrup and ran as a single Responses API request with `search_context_size=medium`; AA estimated search time from streamed events (upper bound) — [AlphaSignal](https://alphasignal.ai/news/openai-web-search-scores-74-but-loses-on-cost-to-cheaper-rivals); [AA leaderboard footnote](https://artificialanalysis.ai/agents/search-api).
- Update frequency: not stated anywhere on the page; page says "Latest data: Oct 19, 2026" — [AA leaderboard](https://artificialanalysis.ai/agents/search-api).

**Launch table, Aug 18 2026 (11 configurations, 7 providers)** — [AA launch article](https://artificialanalysis.ai/articles/search-api)

| Rank | Product | Index | Lift vs model-only | DSQA F1 | BrowseComp | AA-Omniscience | Search $/1k tasks | Model $/1k tasks | Time/task |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Parallel Search (advanced) | 75 | +42 | 81 | 77 | 67 | $47.93 | $35.58 | 35.9 s |
| 2 | Exa Search (auto) | 74 | +41 | 78 | 74 | 70 | $65.57 | $61.58 | 26.2 s |
| 3 | Firecrawl Search | 73 | +40 | 74 | 74 | 73 | $30.48 | $44.94 | 55.0 s |
| 4 | Parallel Search (basic) | 73 | +40 | 79 | 73 | 68 | $45.14 | $69.69 | 20.4 s |
| 5 | Exa Search (fast) | 68 | +35 | 76 | 61 | 69 | $78.11 | $80.53 | 20.7 s |
| 6 | You.com Search | 68 | +35 | 63 | 74 | 66 | $68.93 | $58.28 | 33.7 s |
| 7 | Parallel Search (turbo) | 67 | +34 | 70 | 75 | 56 | $13.64 | $46.57 | 18.8 s |
| 8 | Keenable Search (pro) | 67 | +34 | 70 | 66 | 65 | $23.69 | $73.20 | 23.2 s |
| 9 | Keenable Search (realtime) | 67 | +34 | 70 | 64 | 66 | $26.87 | $63.67 | 15.1 s |
| 10 | Tavily Search (basic) | 66 | +33 | 74 | 59 | 64 | $126 | $66.58 | 36.3 s |
| 11 | Brave Search | 65 | +32 | 62 | 67 | 65 | $71.61 | $74.52 | 26.6 s |
| — | Model only | 33 | — | 45 | 17 | 38 | — | $2.92 | 13.8 s |

- Per-query search latency at launch: Keenable realtime 0.34 s (fastest), Parallel turbo 0.51 s, Exa fast 0.91 s, Exa auto 2.10 s; Firecrawl slowest total time (55.0 s) — [AA launch article](https://artificialanalysis.ai/articles/search-api).
- Parallel's launch announcement claims "#1 on every dimension" and "43% lower cost per task than the next closest provider" (no competitor named, no scores given) — [Parallel blog](https://parallel.ai/blog/artificial-analysis-best-search-api) (vendor).

**Interim snapshots (as reported second-hand by Parallel pages; vendor-relayed)**
- Sept 8 2026 data: Parallel Search (fast) 73, search cost $8.41/1k tasks, ~15.7–16 s/task; Octen Search 0.21 s per query, "only Search API in top 3 for quality, speed and search cost", search fees ≈1/7 of Exa auto's — [Best fast search APIs](https://parallel.ai/articles/best-fast-search-apis); [X post by @kimmonismus](https://x.com/kimmonismus/status/2103322857082408967).
- Sept 22/28 2026 data (25 products, 12 providers): Perplexity Search (medium) 80, (high) 79, Octen 77, Parallel advanced 75 (DSQA 81, BC 77, Omni 67; $47.93 search; 40.5–40.7 s), Brave LLM Context 75 (DSQA 78, BC 77, Omni 69; $61.96; 21.8–22.0 s), You.com highlights 74, Exa auto 74, Parallel basic 73 (25.6 s), Firecrawl 73 (60.7 s; $42.57 total) — [Brave vs Parallel compare](https://parallel.ai/compare/brave-vs-parallel); [Firecrawl vs Parallel compare](https://parallel.ai/compare/firecrawl-vs-parallel); [Perplexity vs Parallel compare](https://parallel.ai/compare/perplexity-vs-parallel).
- Oct 6 2026 (OpenAI Web Search debut; 26 configurations): OpenAI Web Search (medium) 74 = 5th-best provider / 7th of 26 configs; BrowseComp 74% (13th of 26; Perplexity and Octen 85–87%); Omniscience 72% (Firecrawl leads at 73%); DSQA 78 F1; total $49.59/1k tasks ($40.19 search + $9.40 model; ~4 search calls/task at $10/1k calls); ~40k input tokens/task vs ~125k for leanest external API; time 30.4 s; Perplexity medium total $70.34, Octen $23.99, Parallel advanced $59.22, Brave $79.42; Octen 15.9 s, Brave 22.7 s, Perplexity 27.5 s, Parallel 41.4 s — [AlphaSignal](https://alphasignal.ai/news/openai-web-search-scores-74-but-loses-on-cost-to-cheaper-rivals); [AA X post](https://x.com/ArtificialAnlys/status/2107347774262112765) (seen as a search snippet only).
- DeepSeek Search debut (DeepSeek launched its Search API Oct 17 2026): index 69, "17th of 27 search products, at the lowest price of any paid Search API on the board" — [AA X post](https://x.com/ArtificialAnlys/status/2113124084410425362) (seen as a search snippet only).

**Leaderboard as of Oct 19 2026 (page says 26 products / 14 providers; 12 rows extracted)** — [AA leaderboard](https://artificialanalysis.ai/agents/search-api)

| # | Product | Index | Lift | DSQA F1 | BrowseComp | AA-Omni | Search $/1k tasks | Model $/1k tasks | Time/task |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Exa Search (auto, dynamic highlights) | 80 | +47 | 86 | 83 | 73 | $53.17 | $10.60 | 36.9 s |
| 2 | Perplexity Search (medium) | 80 | +47 | 81 | 87 | 72 | $62.30 | $8.04 | 31.4 s |
| 3 | Exa Search (lite, dynamic highlights) | 79 | +46 | 85 | 81 | 72 | $31.20 | $10.95 | 19.6 s |
| 4 | Perplexity Search (high) | 79 | +46 | 81 | 86 | 71 | $56.93 | $9.37 | 29.4 s |
| 5 | Octen Search (highlights) | 77 | +44 | 80 | 86 | 66 | $9.07 | $14.50 | 15.8 s |
| 6 | Parallel Search (advanced) | 75 | +42 | 81 | 77 | 67 | $47.93 | $10.67 | 40.0 s |
| 7 | Brave Search (LLM context) | 75 | +42 | 78 | 77 | 69 | $61.96 | $16.95 | 22.8 s |
| 8 | OpenAI Web Search (medium) | 74 | +41 | 78 | 74 | 72 | $40.19 | $9.40 | 33.3 s (upper bound) |
| 9 | You.com Search (highlights) | 74 | +41 | 77 | 77 | 69 | $47.54 | $19.41 | 21.5 s |
| 10 | Nimble Search (standard) | 74 | +41 | 76 | 75 | 71 | $46.14 | $16.64 | 24.6 s |
| 11 | Firecrawl Search | 73 | +40 | 74 | 74 | 73 | $30.48 | $11.58 | 61.9 s |
| 12 | DeepSeek Search (summary) | 69 | +36 | 75 | 63 | 70 | $8.47 | $20.19 | 22.6 s |
| — | Model only (GPT-5.6 Luna, medium) | 33 | — | 45 | 17 | 38 | — | $2.92 | 26.8 s |

- Exa's own write-up gives the unrounded values Exa auto 80.3 and Exa lite 79.2, and AA's "search queries per task": Exa auto 7.60, Exa lite 7.80, You.com 9.51, Parallel 9.59, DeepSeek 11.3, Perplexity 11.4, Brave 12.4, Firecrawl 15.4 — [Exa AA blog](https://exa.ai/blog/artificial-analysis-exa-3-best-search-api) (vendor: Exa, Oct 19 2026).
- TinyFish Search (web) is listed in AA's FAQ with $0 measured search cost but is absent from the extracted table; Octen has the fastest per-query time at 0.21 s — [AA leaderboard](https://artificialanalysis.ai/agents/search-api).
- Note the model-cost column collapsed between launch and Oct 19 (e.g., Parallel advanced $35.58 → $10.67/1k tasks; Exa auto $61.58 → $10.60); AA does not explain this on the page (possibly a GPT-5.6 Luna price change or token accounting change) — compare [launch article](https://artificialanalysis.ai/articles/search-api) and [leaderboard](https://artificialanalysis.ai/agents/search-api).

### Inferences
- AA is the only cross-vendor source with a fixed, documented, open-source harness, a stated turn budget, and both quality and all-in cost; but one of its three components (AA-Omniscience) is private, and BrowseComp is a 200-question "hard" subset, so exact replication is impossible for outsiders.
- Rankings shift with product-version updates: Brave rose 65 → 75 when AA switched from "Brave Search" to the "LLM context" endpoint; Exa rose 74 → 80 with Exa 3.0's "dynamic highlights" (Oct 19 2026); Perplexity entered at 80 in September. Vendors announce "#1" at whichever snapshot favours them (Parallel Aug 18; Perplexity Sept; Exa Oct 19).
- The prompt's "15 products, 7 providers" does not match any snapshot I found (11/7 at launch; 25/12 Sept; 26/14 and 27 products in Oct). It may describe an early-September intermediate state that no page I fetched preserves.

### Gaps
- The full 26/27-row table (incl. Keenable pro/realtime, Exa fast, Parallel basic/turbo/fast, Tavily, You.com snippets, TinyFish, Linkup if present) was not visible in the Oct 19 fetch; only 12 rows were extractable. Per-query latency/cost charts are image-only.
- AA's update cadence and whether products are re-run when vendors ship changes is not documented.
- The AA X posts (OpenAI debut, DeepSeek debut) could not be fetched directly; their numbers are taken from search snippets and AlphaSignal.

---

## Key Question 3 — Keenable: select.keenable.ai roundup and Keenable-published numbers (NEEDLE)

### Takeaway
select.keenable.ai redirects to a Keenable SELECT product page ("ask the web for a table") with no benchmark content, and the sentence "No single search API wins every AI benchmark" was not found on any Keenable page or elsewhere. Keenable's real published numbers are its open-source NEEDLE live benchmark (vendor-run; Keenable 2nd–3rd overall at 71–72% of "ultimate", first on latency and AgenticRare) plus its AA scores (67 pro, 67 realtime, fastest per-query time at launch).

### Cited Findings
- select.keenable.ai → 302 → app.keenable.ai/select/start: a Keenable SELECT product page (reports with rows/columns/sources; "Free Through October"; Claude connector, MCP connector); no benchmark names, providers, scores, latency, cost or the quoted sentence — [Keenable SELECT](https://app.keenable.ai/select/start).
- NEEDLE ("News, Everyday, Expert, Deep-tail, Legal Evaluation") is a live, open-source benchmark run in GitHub Actions by Keenable (authors Andrey Styskin, Matthias Petri, Ilya Gusev); verticals Scholar, News (hourly refresh), Finance, AgenticRare, Legal (daily refresh); scores ranking/titles/snippets only (no page fetch, no rerank); same query text to every engine; sequential requests; snippets capped at 2,000 chars; engine-caused failures score zero; judge for News/AgenticRare = `openai/gpt-6-luna` via OpenRouter, temp 0, blind to engine; Scholar/Legal deterministic ID match; Finance answer match with LLM fallback; metrics nDCG@5 (News, AgenticRare, duplicate-URL penalty), recall@5/MRR@5 (Finance), recall@10/recall@5 + MRR (Scholar/Legal); "ultimate" = synthetic engine pooling all results per query; index-independence overlap test; no systematic human-agreement audit of the judge — [NEEDLE standings](https://keenableai.github.io/needle/); [Keenable NEEDLE blog, Aug 27 2026](https://keenable.ai/blog/needle-the-benchmark-your-search-engine-can-t-memorize); [MarkTechPost, Aug 31 2026](https://www.marktechpost.com/2026/08/31/keenable-ai-open-sources-needle-a-live-search-benchmark-that-rebuilds-its-query-set-every-hour/).

**NEEDLE overall standings (7-day mean share of "ultimate"; runs early Nov 2026; prices = lowest self-serve $/1k collected 2026-08-21; latency p50/p95 over successful calls) — vendor (Keenable)** — [NEEDLE standings](https://keenableai.github.io/needle/)

| Engine | Overall | $/1k | p50 | p95 | Error rate |
|---|---|---|---|---|---|
| perplexity | 74% | $5.00 | 1.2 s | 1.6 s | 1.7% |
| perplexity-fast | 72% | $1.00 | 176 ms | 260 ms | 1.7% |
| Keenable | 72% | $1.00 | 154 ms | 317 ms | 0.0% |
| exa | 69% | $7.00 | 1.4 s | 3.2 s | 0.2% |
| parallel | 68% | $5.00 | 2.4 s | 3.9 s | 0.0% |
| exa-lite | 68% | $4.00 | 464 ms | 689 ms | 0.2% |
| brave-llmcontext | 66% | $5.00 | 1.2 s | 2.4 s | 0.0% |
| context.dev | 60% | $0.50 | 1.7 s | 4.0 s | 0.0% |
| brave | 59% | $5.00 | 558 ms | 807 ms | 0.0% |
| linkup | 59% | $5.00 | 1.3 s | 1.9 s | 0.0% |
| you | 58% | $5.00 | 544 ms | 736 ms | 0.0% |
| parallel-turbo | 58% | $1.00 | 344 ms | 550 ms | 0.0% |
| deepseek | 57% | $0.75 | 587 ms | 733 ms | 0.0% |
| chatgpt-search | 53% | $10.00 | 43 s | 53 s | 1.0% |
| claude-search | 53% | $10.00 | 36 s | 51 s | 57.8% |
| firecrawl | 50% | $1.20 | 843 ms | 3.5 s | 4.7% |
| octen | 49% | $1.00 | 200 ms | 381 ms | 0.0% |
| bing/searchapi | 48% | $1.00 | 2.1 s | 7.5 s | 0.3% |
| kagi | 47% | $12.00 | 1.2 s | 2.1 s | 87.9% |
| google/serper | 46% | $0.30 | 1.5 s | 3.0 s | 0.0% |
| tinyfish | 44% | $0.00 | 1.9 s | 4.3 s | 9.8% |
| tavily | 43% | $5.00 | 1.6 s | 3.2 s | 0.0% |
| jina | 40% | $3.40 | 17 s | 25 s | 3.5% |

- Per-vertical leaders (7-day means): Scholar recall@10 — perplexity 0.737, Keenable 0.712, context.dev 0.702 (ultimate 0.925); News nDCG@5 — exa-lite 0.650, exa 0.648, perplexity 0.640, Keenable 0.617; Finance recall@5 — perplexity 0.921, exa-lite and parallel 0.917 (ultimate 0.992); AgenticRare nDCG@5 — Keenable 0.494, perplexity 0.469; Legal recall@5 — perplexity-fast 0.859 (ultimate 0.974) — [NEEDLE standings](https://keenableai.github.io/needle/).
- Earlier NEEDLE snapshot (around Aug 31 2026, via MarkTechPost/secondary): Keenable and Perplexity tied at ~71% overall (95% CI [70%, 73%] for Keenable), Exa 68%; Exa led deep-tail (0.557 of ultimate) vs Keenable 0.470 and Bing 0.199; Keenable-realtime 193 ms p50 / 284 ms p95 vs Exa 1,876 / 2,955 ms — [MarkTechPost](https://www.marktechpost.com/2026/08/31/keenable-ai-open-sources-needle-a-live-search-benchmark-that-rebuilds-its-query-set-every-hour/); [The Agentic Digest Q&A](https://www.theagenticdigest.com/q-and-a/how-does-keenable-needle-benchmark-web-search-apis-for-agent-like-queries) (secondary).
- Keenable blog (Aug 27 2026): engines compared = Google (via Serper), Bing (via SearchAPI), Brave, Tavily, Parallel, Exa, Keenable; Keenable p50 "200 ms today", p95 target 200 ms; overlap analysis to detect shared upstream indexes; no standings table in text — [Keenable blog](https://keenable.ai/blog/needle-the-benchmark-your-search-engine-can-t-memorize).
- Keenable on AA (independent): pro 67 (DSQA 70, BC 66, Omni 65, $23.69, 23.2 s), realtime 67 (DSQA 70, BC 64, Omni 66, $26.87, 15.1 s; 0.34 s/query, fastest) at launch Aug 18 2026 — [AA launch article](https://artificialanalysis.ai/articles/search-api).
- Show HN (≈Aug 2026): Keenable $4/1k with up to 50 results, Parallel $5/1k, Exa $7/1k (+ per extra result beyond top 10); Keenable p50 "<200 ms"; founder claims quality "competitive to exa … but much cheaper and lower latency" and suggests Parallel and Brave may share an index per the NEEDLE overlap card — [HN Show HN: Keenable](https://news.ycombinator.com/item?id=49435555).
- HN DeepSeek thread (≈Oct 2026): Keenable staff ran DeepSeek Search on NEEDLE: "better than Jina, Firecrawl and Tavily but worser than Parallel and Exa in terms of quality" (no numbers) — [HN DeepSeek search thread](https://news.ycombinator.com/item?id=50138531).

### Inferences
- NEEDLE's price column (Keenable $1/1k) conflicts with Keenable's own HN pricing ($4/1k); NEEDLE's prices were frozen on 2026-08-21 while the standings are live, so the cost column is stale by ~2.5 months.
- NEEDLE is the only public source with p50/p95 for >20 engines under one client, but it measures snippet/ranking quality rather than end-task accuracy, which is why Tavily (43%) and Firecrawl (50%) rank far lower here than on AA/Openbenchmarks (where their extract/fetch payloads help agents).
- The "no single API wins" framing in the task description is best supported by (a) Openbenchmarks' three task-specific winners (Exa fast, Exa deep/Perplexity, Parallel basic/Exa deep) and (b) Parallel's own statement that "no engine led on every benchmark at every price tier"; I could not attribute it to Keenable.

### Gaps
- No Keenable-authored multi-benchmark roundup exists at select.keenable.ai; if the client saw one, it was likely a SELECT-generated report not publicly indexed.
- NEEDLE's historic snapshots (daily) are on Hugging Face but I did not extract a dated time series; the Aug-31 vs Nov standings above are the only two points.

---

## Key Question 4 — Exa: published numbers and third-party numbers for Exa

### Takeaway
Exa publishes the largest volume of vendor benchmarks (entity/people/company retrieval, publications, WebCode, ATLAS, Exa 3.0's eight-benchmark sweep, matched-latency FRAMES/SealQA vs Parallel) with open query sets and grading code (github.com/exa-labs/benchmarks) but mostly no competitor numbers in text and no raw outputs for the 3.0 sweep. Third parties place Exa anywhere from 71% (Tavily's GPT-4.1 SimpleQA harness, 2025) to 95.4–95.5% (You.com's 2026 harness) on SimpleQA, and from 33.7% (Parallel July, Instant) to 83 (AA) on BrowseComp — ranges driven entirely by tier, agent model and harness.

### Cited Findings

**Exa-authored (vendor)**
- Jan 24 2025 "State of the art web search API": Exa "tops the charts" on SimpleQA (Exa setup: gemini-1.5-flash writes query, GPT-4o-mini answers; Bing: GPT-4o-mini; Perplexity: Sonar-Pro) and MSMARCO (1,000-query sample graded 1–5 by GPT-4o); numbers are image-only — [Exa api-evals](https://exa.ai/blog/api-evals). Linkup's post cites Exa's SimpleQA at 90.04% — [Linkup SimpleQA post](https://www.linkup.so/blog/linkup-establishes-sota-performance-on-simpleqa).
- Feb 12 2026 Exa Instant: "sub-200 ms", "up to 15x faster" than compared providers (Tavily Ultra Fast, Brave, Parallel one-shot), Google-SERP wrappers "over 700 ms P50"; measured from us-west-1 on SealQA queries with random GPT-5 words appended to defeat caching; P50/P90 chart image-only; Oct 2026 update recommends Lite instead — [Exa Instant](https://exa.ai/blog/exa-instant).
- May 13 2026 RL post: Exa 4B+RL scored SimpleQA 0.767, FRAMES 0.566, BrowseComp 0.043 vs a SERP backend 0.692 / 0.521 / 0.039 — [Exa RL post](https://exa.ai/blog/rl-search-outcomes).
- Exa vs Parallel page (tests July 8–24 2026; eight providers tested: Exa, Parallel, Brave, Tavily, Perplexity, Linkup, Firecrawl, You.com; Perplexity errored on 115 of 200 SimpleQA queries, You.com on 95, Firecrawl on 10): — [Exa vs Parallel](https://exa.ai/versus/parallel)

| Matched-latency budget | Dataset | Exa | Parallel |
|---|---|---|---|
| Lite (Exa Lite ~450 ms vs Parallel basic ~0.9–1.1 s) | FRAMES | 0.375 | 0.261 |
| | SealQA | 0.225 | 0.090 |
| | SealQA-Hard | 0.335 | 0.180 |
| Research (Exa Auto ~1.5 s vs Parallel advanced ~2.2 s) | FRAMES | 0.46 | 0.295 |
| | SealQA | 0.270 | 0.135 |
| | SealQA-Hard | 0.355 | 0.185 |

  p50 latency: Exa Lite ~450 ms, Parallel basic 906 ms, Exa Auto 1,502 ms, Parallel advanced 2,246 ms (no p95); People R@1 Exa 72% / Parallel 20.8% / Brave 44.4%; Company R@1 61.8% / 36.6% / 35.9%; Company RAG accuracy 79% / 66% / 65% (1,400 people + 605 company queries); WebCode (Mar 2026, ~840 queries): signal 94.5 / 77.6 / Claude 55.1, code recall 96.7 / 94.1 / 82.4; academic search (1,472 queries): recall Exa 86.4% (MRR 0.726, 0.578 s), Perplexity 66.8% (0.568, 1.277 s), Parallel advanced 50.0% (0.312, 3.118 s), Parallel turbo 39.2% (0.278, 0.403 s), Google Scholar 28.0%; Exa Agent High vs Parallel Task (June 2026): BrowseComp 74% @ $0.50 vs 58% Ultra 8x @ $2.40; DeepSearchQA 0.77 vs 0.762 (Ultra 2x, $0.60); FinanceAgent-V2 64.2% vs 63%; WideSearch 52% vs 51.3% — [Exa vs Parallel](https://exa.ai/versus/parallel). Model/harness for most results not named.
- Exa vs Tavily (evaluated Aug 4 2026; Exa `lite` vs Tavily `advanced`; GPT-5.4 scoring with repo rubrics; 200 people, 200 company, 597 LitSearch queries): People R@1 75.5% vs 40.5%; Company R@1 81.5% vs 61.3%; Company R@3 88.3% vs 73.0%; Publication R@1 63.3% vs 31.8%; Perplexity People R@1 53.5%, Company R@1 69.3%, R@3 83.3%; "Fortune 100 evaluation" p95: Exa 1.4–1.7 s vs Tavily 3.8–4.5 s; Tavily ultra-fast claimed 90 ms, measured 210 ms typical / 420 ms long inputs — [Exa vs Tavily](https://exa.ai/versus/tavily).
- Exa vs Brave (run July 29–Aug 2 2026; 1,400 people, 605 company, 307 WebCode RAG queries): People R@1 72.0% vs 44.4%; Company R@1 61.8% vs 35.9%; Company RAG 79% vs 65%; WebCode RAG groundedness 79.4 vs 76.3; citation precision 0.259 vs 0.328 ("Brave leads on citation precision") — [Exa vs Brave](https://exa.ai/versus/brave).
- exa-labs/benchmarks repo (undated; "historical measurements with earlier adapters"): Scout harness swaps search APIs with fixed model/prompts/budgets; default judge and Scout model `openai/gpt-6-luna`; RAG answer model `openai/gpt-5.6-luna`; 95% bootstrap CIs (10k resamples); People R@1 Exa 89.5% / Brave 44.4% / Parallel 20.8%; Company retrieval R@1 61.8% / 35.9% / 36.6%; WebCode Highlights groundedness Exa 94.8 / Parallel 85.6 / Claude 81.5; WebCode RAG groundedness Exa 79.4 / Brave 76.3 / Parallel 75.3 / Perplexity 64.6; Publication tip-of-tongue recall Exa 86.4% / Perplexity 66.8% / Parallel adv 50.0%; Tavily listed as provider but no results — [exa-labs/benchmarks](https://github.com/exa-labs/benchmarks).
- ATLAS (Oct 8 2026): 547 tasks, 23 categories, entity-discovery + 2–10 multi-hop attributes; 12 systems (Exa Agent ×4 efforts; Claude Opus 5.5 and GPT-6 Astra ×2 with native search; GPT-5.6/GPT-6 Luna with Exa, Perplexity, Brave, Parallel via "Scout"); Row F1 headline metric, deterministic cells + GPT-6 Luna judge for 4.5%; best system 0.66 row F1 at $8.92 and 18 min/task; no system under $1/task above 0.5; "scores vary by up to 16% across search backends"; per-provider table promised later — [Exa ATLAS](https://exa.ai/blog/atlas-benchmark).
- Exa 3.0 (Oct 19 2026): eight-benchmark sweep, "first on every benchmark we tested", vs Perplexity, Brave, Parallel; Exa 3.0 Auto: BrowseComp 91.8%, DSQA 88.2%, WideSearch 56.1%, ATLAS 42.0%, WebCode 75.5%, FinSearchComp 68.0%, Company FindAll 15.4, People FindAll 7.6; competitor scores not in text; Lite $4/1k, Auto $7/1k; "Dynamic Highlights use 95% fewer tokens" — [Exa 3.0](https://exa.ai/blog/exa-3); [explainx claimed-vs-verified](https://explainx.ai/blog/exa-3-0-search-api-lite-auto-pricing-benchmarks-claimed-vs-verified-2026); [AlphaSignal](https://alphasignal.ai/news/exa-3-0-beats-perplexity-on-8-benchmarks-and-slashes-search-costs). Competitor numbers reported second-hand (MarkTechPost, Oct 20 2026; page 403'd for me, values from search snippet): BrowseComp Exa 3.0 Auto 91.8 / Perplexity Search API 91.5 / Brave LLM Context 83.5 / Parallel Advanced 63.1; ATLAS 42.0 / 37.2 / 28.2 / 24.8; Exa used "each provider's highest-scoring single-step endpoint"; no raw outputs published — [MarkTechPost](https://www.marktechpost.com/2026/10/20/exa-3-0-search-api-lite/).

**Third-party numbers for Exa (independent unless marked)**
| Source (date, author) | Exa product | Metric | Value | Harness | Reproducible? |
|---|---|---|---|---|---|
| AA launch (Aug 18 2026) | Exa auto / fast | Index | 74 / 68 (BC 74 / 61; DSQA 78 / 76; Omni 70 / 69; search $65.57 / $78.11 per 1k tasks; 26.2 / 20.7 s) | GPT-5.6 Luna, Stirrup | Harness open; Omni private — [AA](https://artificialanalysis.ai/articles/search-api) |
| AA (Oct 19 2026) | Exa auto / lite (dynamic highlights) | Index | 80 / 79 (BC 83 / 81; DSQA 86 / 85; Omni 73 / 72; $53.17 / $31.20; 36.9 / 19.6 s) | same | — [AA](https://artificialanalysis.ai/agents/search-api) |
| Parallel (July 2026, vendor) | Exa Instant | BrowseComp / SimpleQA | 33.7% / 89.3%; p50 335–361 ms | GPT-5.4 agent+judge, 20 calls | No — [Parallel](https://parallel.ai/compare/exa-vs-parallel) |
| Parallel (Sept 9 2026, vendor) | Exa Auto | BC / SQA-V / WideSearch | 70% / 91% / 55.9 (frontier); 36% / 91% / 53.0 (low-cost) | GPT-5.6 Sol high / Luna low | No — [Parallel](https://parallel.ai/benchmarks) |
| Parallel finance (Oct 22–27 2026, vendor) | Exa Auto | FinSearchComp T3 / T2 / FrontierFinance / PWS | 51.4% / 77.9% / 47.2 / 75.9% | GPT-6 Sol high, 20 calls | No — [Parallel](https://parallel.ai/benchmarks) |
| Openbenchmarks (Oct 21 2026) | Exa fast / instant | Factual-lookup acc; mean latency; $/1k | 99.3% / 652 ms / $7; 97.7% / 398 ms / $7 | gpt-5.6-terra extractor, claude-opus-5 judge, 300 Qs | Code+partial data open — [Openbenchmarks](https://openbenchmarks.com/web-search) |
| Openbenchmarks | Exa deep / auto | Coding-agent task completion (search+fetch) | 83.0±1.0% (37 s) / 81.7±1.1% (23 s) | gpt-5.6-sol, 5 searches, 32 turns, 100 tickets ×3 | — [Openbenchmarks](https://openbenchmarks.com/web-search) |
| Openbenchmarks | Exa deep / instant | Multi-hop company F1 (search+fetch) | 48.2% / 44.9%; search-only 45.4% / 43.3% | gpt-5.6-sol medium, 8 turns, 14 searches, 45 Qs ×3 | — |
| Perplexity search_evals blog (Sept 25 2025, vendor: Perplexity) | Exa | SimpleQA / FRAMES / BrowseComp / HLE | .781 / .399 / .265 / .242; latency p50 1,375 ms, p75 1,499, p90 1,798, p95 2,188 (from AWS us-east-1) | model unnamed | Framework open — [Perplexity](https://www.perplexity.ai/hub/blog/architecting-and-evaluating-an-ai-first-search-api) |
| Perplexity search_evals repo (commit #6, 2026) | Exa | SimpleQA / FRAMES / BrowseComp / HLE / DSQA / SEAL-0 / SEAL-hard | gpt-5-medium: 0.874 (3781/4326) / 0.881 / 0.336 / 0.314; claude-opus-4-5-thinking: 0.867 (3750/4326) / 0.871 (718/824) / 0.127 (161/1265) / 0.245 / 0.347 / 0.171 / 0.343 | agentic harness | Open — [search_evals commit](https://github.com/perplexityai/search_evals/commit/39d576b) |
| Tavily evals repo (vendor: Tavily) | Exa Search | SimpleQA (full) / Document relevance | 71.24% / 51.33% | gpt-4.1 extractor, official classifier, max_results 10 | Open — [tavily-search-evals](https://github.com/tavily-ai/tavily-search-evals) |
| Valyu (Oct 3 2025, vendor: Valyu) | Exa | SimpleQA (4,326) / FreshQA (600) / Finance (120) / Economics (100) / MedAgent (562) | 91% / 24% / 63% / 45% / 44% | AI-SDK harness; graders Gemini 2.5 Pro, Claude Sonnet 4, GPT-4.1 | Code open — [Valyu](https://www.valyu.ai/blogs/benchmarking-search-apis-for-ai-agents) |
| You.com (Sept 21 2026, vendor: You.com) | Exa (full page) | SimpleQA / p50 | 95.47% / 1,337 ms | GPT-5.4-nano synth, GPT-5.4-mini grader | Harness open — [You.com Highlights](https://you.com/resources/highlights-parameter-web-search-api) |
| You.com harness run (Oct 7 2026, vendor) | exa_search_with_text | SimpleQA / FRAMES / p50 | 95.40% (2,502 ms) / 73.79% (2,694 ms) | synthesis model stated inconsistently (GPT-5.6 Luna vs GPT-5.4 nano) | Open — [web-search-api-evals](https://github.com/youdotcom-oss/web-search-api-evals) |
| Linkup (Feb/Mar 2025, vendor: Linkup) | Exa | SimpleQA | 90.04% (Exa's own published figure) | — | — [Linkup](https://www.linkup.so/blog/linkup-establishes-sota-performance-on-simpleqa) |
| Keirolabs (Oct 19 2026, vendor: Keiro) | Exa | SimpleQA | 91.9% ("GPT-5.4 agent, official grader, independent test"); elsewhere 95.47% | — | No — [Keiro](https://keirolabs.cloud/blog/most-accurate-web-search-api); [Keiro](https://keirolabs.cloud/best-web-search-api) |
| AIMultiple (Dec 2025 snapshot, pub. Jan 2026, upd. May 2026) | Exa | Agent Score (max 25) | 14.39 (CI 13.25–15.50); relevance 4.32/5; quality 3.33/5; ~1.2 s | GPT-5.2 judge, 100 queries, ~4,000 results | Methodology only — [AIMultiple](https://aimultiple.com/agentic-search) |
| arlenkumar.com (June 14 2026, independent) | Exa | hit@1 / hit@5 | 62.2% / 80.9% (CI 76.1–85.0), 299 queries ×3 | deterministic golden URLs, no LLM | Code+data open — [arlenkumar](https://arlenkumar.com/bench/leaderboards/web-search) |
| cloro.dev (run July 8 2026; vendor: cloro, Google-SERP API) | Exa | URL overlap@10 with Google / domain Jaccard / rank ρ | 32% / 0.30 / 0.27 | 500 queries | — [cloro](https://cloro.dev/blog/best-search-api/) |
| NEEDLE (Nov 2026, vendor: Keenable) | exa / exa-lite | Overall; p50/p95 | 69% (1.4 s / 3.2 s); 68% (464 / 689 ms) | snippet-level, GPT-6 Luna judge | Open — [NEEDLE](https://keenableai.github.io/needle/) |
| Brave API page (undated, vendor: Brave) | Exa | FreshQA acc / all-in $ per 1k Qs | 78.0% / $84 | Brave's own runs | No — [Brave API](https://brave.com/search/api/) |
| agenticsearch.cloud (Aug 16 2026; Keiro-affiliated) | Exa | FinanceBench / SimpleQA / blended | 71% / 76% / 73 ("blended from public evals, vendor claims and spot tests, ±3") | 350 Qs; no model named | Partial — [Agentic Search](https://www.agenticsearch.cloud/posts/i-benchmarked-15-ai-search-apis/) |
| BrowseComp-Plus — | — | no Exa entry found | — | — | — [BrowseComp-Plus](https://texttron.github.io/BrowseComp-Plus/) |

### Inferences
- Exa's own cross-vendor claims cluster around retrieval-centric tasks (entity, publications, code, matched-latency SealQA/FRAMES) where embedding search has structural advantages; agentic end-task benchmarks run by others (Parallel Sept, Openbenchmarks search-only) show smaller or reversed gaps.
- Exa 3.0's "91.8% BrowseComp" is on a different scale from every other BrowseComp number here (it exceeds even Parallel's Task Ultra4x at 94% only slightly while using a single-step search endpoint); without the harness/model/budget published it cannot be reconciled with AA's 83 or Parallel's 70%.
- The Exa SimpleQA spread (71% → 95.5%) tracks harness generation: GPT-4.1 one-shot extraction (2025) vs GPT-5.4-class agent with fetch (2026).

### Gaps
- Exa's eight-benchmark competitor table (per-benchmark Perplexity/Brave/Parallel scores) is only partially recoverable (BrowseComp and ATLAS rows via MarkTechPost snippet); the Exa 3.0 post text itself lists only Exa's scores.
- ATLAS per-provider results had not been released as of the fetch.
- Exa publishes no p95 for its own API outside the "Fortune 100" anecdote.

---

## Key Question 5 — Other vendors' published numbers (Tavily, Linkup, Firecrawl, Valyu, Brave, Perplexity, Jina, You.com, Nimble, Bright Data) with harness details

### Takeaway
Every vendor that publishes a cross-provider table ranks itself first (Tavily 93.3%→97.6% SimpleQA; Linkup 90.1%→94% Verified; Firecrawl 94.7%; Valyu 94%; You.com 95.17–96.11%; Perplexity .930; Brave 85.3% FreshQA; Keirolabs 95.3%), typically on its own harness and often reporting competitor results only in images or not at all. Jina, Nimble and Bright Data publish no answer-accuracy head-to-heads at all; their numbers come only from third parties (NEEDLE, Openbenchmarks, AA, AIMultiple).

### Cited Findings

**Tavily (vendor)**
- tavily-search-evals repo (undated; example folders dated 2025-01-15): full SimpleQA; gpt-4.1 extracts answer from retrieved docs; official SimpleQA classifier; example config Tavily `search_depth=advanced`, `max_results=10`, Perplexity `max_results=10`, `max_tokens_per_page=512`. SimpleQA: Tavily 93.3%, Perplexity Search 85.92%, Google (Serper) 82.15%, Brave 76.05%, Exa 71.24%. Document relevance (QuotientAI grader, dynamic set): Tavily 83.02%, Perplexity 71.2%, Serper 58.11%, Brave 56.2%, Exa 51.33% — [tavily-search-evals](https://github.com/tavily-ai/tavily-search-evals).
- Aug 11 2026 "Tavily ranks #1 on SealQA and SimpleQA": reader gpt-5.4 Mini (medium), grader gpt-4.1-mini with official SealQA prompt, max_results=10 for all; Tavily SealQA-0 49.5%, SealQA-Hard 55.7%, SimpleQA 97.6%; also "topped SimpleQA Verified" (no figure); competitors Exa Auto, Parallel Advanced, Perplexity Search, Brave, You.com said to be outperformed but no scores, no question count, no latency, no cost, no code link — [Tavily blog](https://www.tavily.com/blog/tavily-ranks-1-on-sealqa-and-simpleqa).
- Sept 14 2026 six-way comparison post: repeats "#1 on SealQA-0, SealQA-Hard, SimpleQA Verified"; no numbers — [Tavily blog](https://www.tavily.com/blog/tavily-vs-exa-vs-parallel-vs-firecrawl-vs-perplexity-vs-brave-choosing-the-right-web-search-api).
- Third-party Tavily numbers: AA basic 66 (DSQA 74, BC 59, Omni 64; $126 search/1k tasks — highest on board; 36.3 s) at launch — [AA](https://artificialanalysis.ai/articles/search-api); Parallel Sept 9: 66%/32% BC, 92%/94% SQA-V, 55.9/47.9 WideSearch, $935/$176 per 1k BC — [Parallel](https://parallel.ai/benchmarks); Parallel July: Ultra Fast 19.3% BC, p50 150–357 ms — [Parallel](https://parallel.ai/compare/tavily-vs-parallel); Openbenchmarks: advanced 93.0% / 4.29 s / $16, basic 87.7% / 1.88 s / $8; coding advanced 60.0±2.0% / basic 59.0±1.7% (search+fetch), basic 51.0±5.3% search-only; multi-hop advanced 41.1 (search-only) / 41.0 (fetch), basic 36.5 / 38.1 — [Openbenchmarks](https://openbenchmarks.com/web-search); Perplexity blog (Sept 2025) "SERP-based (represented by Tavily)" .890 / .437 / .348 / .248, p50 1,342 ms, p95 1,790 — [Perplexity](https://www.perplexity.ai/hub/blog/architecting-and-evaluating-an-ai-first-search-api); search_evals: tavily gpt-5-medium 0.798 / 0.854 / 0.332, claude-opus-4-5-thinking 0.737 / 0.836 / 0.116, claude-sonnet-4-5-thinking 0.713 / 0.796 / 0.085 — [search_evals commit](https://github.com/perplexityai/search_evals/commit/39d576b); You.com harness: 88.53% SQA (1,930 ms p50), 66.14% FRAMES — [web-search-api-evals](https://github.com/youdotcom-oss/web-search-api-evals); Linkup-run 73% (2025) — [Linkup](https://www.linkup.so/blog/linkup-establishes-sota-performance-on-simpleqa); AIMultiple 13.67, 998 ms — [AIMultiple](https://aimultiple.com/agentic-search); arlenkumar hit@5 49.4% — [arlenkumar](https://arlenkumar.com/bench/leaderboards/web-search); NEEDLE 43% — [NEEDLE](https://keenableai.github.io/needle/); cloro ~60% Google overlap (highest), rank ρ 0.03 — [cloro](https://cloro.dev/blog/best-search-api/); Brave FreshQA 78.0% @ $89 — [Brave](https://brave.com/search/api/); Keiro harness 78/77/68 (SimpleQA/FreshQA/HotpotQA, Gemma 3 12B judge) — [Keiro](https://keirolabs.cloud/blog/web-search-apis-for-agents-2026); Parallel finance T3 43.0%, T2 77.2%, FF 42.1, PWS 36.4% — [Parallel](https://parallel.ai/benchmarks).

**Linkup (vendor)**
- SimpleQA post (header Dec 3 2025; body "first published 02/21/2025, updated 03/12/2025"): Linkup Deep 90.10%, Exa 90.04%, Perplexity Sonar Pro 86%, Linkup Standard 85%, Sonar 77%, Tavily 73% (Linkup ran Tavily itself), Grok 3 45%; "Linkup proprietary model" 91.0% F-score (Mar 12 2025 update); model/grader not named; most competitor scores are their own published figures; code github.com/LinkupPlatform/eval-simpleQA — [Linkup](https://www.linkup.so/blog/linkup-establishes-sota-performance-on-simpleqa).
- June 15 2026 buyer's guide: /search 94% F-score on SimpleQA Verified ("top among sub-second APIs"); /research 61% SealQA-0; claims Tavily, Exa, Brave, SerpApi "no published SimpleQA F-score" (contradicted by the Tavily repo and Exa's 2025 post) — [Linkup](https://www.linkup.so/blog/best-web-search-api-in-2026-top-providers-compared).
- Third-party: Openbenchmarks fast 96.7% / 1.57 s / $5, standard 92.0% / 2.55 s; coding standard 48.3±4.9% (fetch), fast 43.3±1.1% (search-only); multi-hop fast 41.1 / standard 40.6 (search-only), standard 42.0 / fast 39.9 (fetch) — [Openbenchmarks](https://openbenchmarks.com/web-search); NEEDLE 59%, 1.3 s / 1.9 s, $5 — [NEEDLE](https://keenableai.github.io/needle/); agenticsearch blended 60 — [Agentic Search](https://www.agenticsearch.cloud/posts/i-benchmarked-15-ai-search-apis/); Exa tested Linkup in July 2026 but published no Linkup score — [Exa vs Parallel](https://exa.ai/versus/parallel).

**Firecrawl (vendor)**
- July 22 2026: /search 94.7% on full SimpleQA (4,326 Qs); GPT-5.4 agent (high reasoning), up to 20 tool calls, `search_web` + `web_fetch` via each provider's extract API (Firecrawl Scrape / Parallel Extract / Exa Contents); Claude native = Claude Sonnet 4.6 server-side search; judge GPT-5.4 with official grader prompt; two sessions per provider, best score reported; GPT-5.4 no-search baseline 43.8; competitor scores only in an image; no code or logs — [Firecrawl](https://www.firecrawl.dev/blog/introducing-our-most-accurate-search-yet); [Nicolas Camara on X](https://x.com/nickscamara_/status/2089785680654455165).
- Firecrawl's "best web search APIs" post cites Openbenchmarks Oct 2026: 678 result tokens/query, 510 ms mean; AIMultiple 2nd overall (relevance 4.30/5) — [Firecrawl](https://www.firecrawl.dev/blog/best-web-search-apis).
- Third-party: AA 73 (DSQA 74, BC 74, Omni 73 — highest Omniscience; $30.48 search; 55.0 s → 61.9 s/task, slowest) — [AA](https://artificialanalysis.ai/agents/search-api); Openbenchmarks 95.3% / 510 ms / $5; coding 76.0±1.0% (fetch) / 70.3±1.5% (search-only, 2nd); multi-hop 30.4 / 33.2 — [Openbenchmarks](https://openbenchmarks.com/web-search); AIMultiple 14.58 (2nd), 1,335 ms — [AIMultiple](https://aimultiple.com/agentic-search); NEEDLE 50%, 843 ms / 3.5 s, 4.7% errors — [NEEDLE](https://keenableai.github.io/needle/); agenticsearch 53 — [Agentic Search](https://www.agenticsearch.cloud/posts/i-benchmarked-15-ai-search-apis/).

**Valyu (vendor)**
- Runs Oct 3 2025; AI-SDK harness, one-shot + multi-turn; graders Gemini 2.5 Pro, Claude Sonnet 4, GPT-4.1 (correct/partial/incorrect); tool definitions from each provider's AI-SDK docs; code github.com/valyu-network/valyu-benchmarks — [Valyu](https://www.valyu.ai/blogs/benchmarking-search-apis-for-ai-agents)

| Benchmark (n) | Valyu | Parallel | Exa | Google |
|---|---|---|---|---|
| FreshQA (600, Aug 27 set) | 79% | 52% | 24% | 39% |
| SimpleQA (4,326) | 94% | 93% | 91% | 38% |
| Finance (120) | 73% | 67% | 63% | 55% |
| Economics (100) | 73% | 52% | 45% | 43% |
| MedAgent (562) | 48% | 42% | 44% | 45% |

- valyu.ai/benchmarks returned 404 on 2026-11-05. Keiro cites a FinanceBench table with Valyu 73%, Keirolabs 78%, Parallel 67%, Exa 63%, Google 55% (Keiro's own run) — [Keiro](https://keirolabs.cloud/blog/most-accurate-web-search-api).

**Brave (vendor)**
- No Brave blog post with a cross-vendor benchmark was found (2026 blog index lists API growth/Place Search/OpenClaw posts only) — [Brave blog](https://brave.com/blog/).
- brave.com/search/api page (undated): AIMultiple agent quality Brave 14.89 (1st), Firecrawl 14.58, Exa 14.39, Tavily 13.67; AIMultiple latency Brave 669 ms, Tavily 998, Exa 1,200, Firecrawl 1,335, SerpApi 2,400, Perplexity 11,000, Parallel Pro 13,600 ("up to 20x faster"); Brave's own FreshQA runs (all-in cost per 1k Qs): Brave 85.3% @ $18, Parallel Advanced 79.0% @ $49, Exa 78.0% @ $84, Tavily 78.0% @ $89; LLM Context "under 500 ms at P90"; blind Bradley-Terry Elo: Ask Brave (Nemotron 3 Ultra) 1,278, Ask Brave v2 (Qwen3) 1,121, Grok 1,115, Google AI Mode 941, ChatGPT 840, Perplexity 652 (evaluator unnamed); pricing Search $5/1k (50 QPS), Answers $4/1k + $5/M tokens — [Brave Search API](https://brave.com/search/api/).
- Third-party: AA "Brave Search" 65 (Aug 18) → "Brave Search (LLM context)" 75 (Sept–Oct; DSQA 78, BC 77, Omni 69; $61.96; 22.8 s) — [AA](https://artificialanalysis.ai/agents/search-api); Openbenchmarks LLM Context 94.0% / 601 ms / $5, Web 93.3% / 630 ms; coding search-only 38.0±2.6% (lowest); multi-hop 28.0 / 29.4 (fastest median 43.5 s) — [Openbenchmarks](https://openbenchmarks.com/web-search); Perplexity (Sept 2025) .822 / .320 / .221 / .191, p50 513 ms, p75 637, p90 728, p95 808 — [Perplexity](https://www.perplexity.ai/hub/blog/architecting-and-evaluating-an-ai-first-search-api); Tavily repo 76.05% / 56.2% — [tavily-search-evals](https://github.com/tavily-ai/tavily-search-evals); arlenkumar hit@5 58.9% — [arlenkumar](https://arlenkumar.com/bench/leaderboards/web-search); NEEDLE brave-llmcontext 66% (1.2 s / 2.4 s), brave 59% (558 / 807 ms) — [NEEDLE](https://keenableai.github.io/needle/); cloro 47% overlap, 89% "#1 is Google-ranked", ρ 0.55 — [cloro](https://cloro.dev/blog/best-search-api/); Exa vs Brave (above); agenticsearch 64 — [Agentic Search](https://www.agenticsearch.cloud/posts/i-benchmarked-15-ai-search-apis/).

**Perplexity (vendor)**
- Sept 25 2025 Search API launch eval (open-source `search_evals`; two harnesses: single-shot and deep-research; prompted classifier graders; agent model, judge, question counts not stated): — [Perplexity](https://www.perplexity.ai/hub/blog/architecting-and-evaluating-an-ai-first-search-api)

| Provider | SimpleQA | FRAMES | BrowseComp | HLE | p50 | p75 | p90 | p95 (ms, AWS us-east-1) |
|---|---|---|---|---|---|---|---|---|
| Perplexity | .930 | .453 | .371 | .288 | 358 | 443 | 604 | 763 |
| Exa | .781 | .399 | .265 | .242 | 1,375 | 1,499 | 1,798 | 2,188 |
| Brave | .822 | .320 | .221 | .191 | 513 | 637 | 728 | 808 |
| SERP-based (Tavily) | .890 | .437 | .348 | .248 | 1,342 | 1,586 | 1,743 | 1,790 |

- search_evals README (2026; Agent-API tier): Perplexity Agent API DSQA 0.871, BrowseComp 0.805, HLE 0.612, WideSearch 0.651; OpenAI Responses 0.733 / 0.720 / 0.614 / 0.522; Anthropic Managed Agents 0.815 / 0.598 / 0.566 / 0.590; Exa Agent 0.53 / 0.38 / 0.387 / 0.471; Parallel Task 0.81 / 0.56 / 0.515 / 0.584; suites BrowseComp 1,266, DSQA 900, HLE text-only 2,158, WideSearch 200; grader unnamed — [search_evals](https://github.com/perplexityai/search_evals).
- Mar 11 2026 "Search API: better extraction, dynamic benchmarks": SEAL/SEAL-Hard added to search_evals; model Claude Sonnet 4.5; "Perplexity's scores rose while other providers' declined" — numbers image-only — [Perplexity](https://www.perplexity.ai/hub/blog/search-api-better-extraction-dynamic-benchmarks).
- Search Arena (Apr 2025): Sonar-Reasoning-Pro-High 1136 (+21/−19) tied with Gemini-2.5-Pro-Grounding 1142 (+14/−17); beat Gemini 53% head-to-head; Sonar cites 2–3x more sources — [Perplexity Search Arena post](https://www.perplexity.ai/hub/blog/perplexity-sonar-dominates-new-search-arena-evolution) (seen via search snippet; the api-platform copy no longer carries the numbers — [api-platform page](https://www.perplexity.ai/api-platform/resources/perplexity-sonar-dominates-new-search-arena-evaluation)).
- Third-party Perplexity: AA medium 80 / high 79 (BC 87 / 86 — highest BC on board) — [AA](https://artificialanalysis.ai/agents/search-api); Parallel Sept 74% / 46% BC ($275 / $37.1), 95% / 94% SQA-V, 53.5 / 47.0 WS — [Parallel](https://parallel.ai/benchmarks); Openbenchmarks (low) 97.3% / 1.38 s / $5; coding search-only 77.3±2.1% (1st, 18 s), fetch 77.7±1.5%; multi-hop fetch 46.6 (2nd), search-only 37.8; median search-only company task cost $0.334 vs Parallel $1.12 — [Openbenchmarks](https://openbenchmarks.com/web-search); Tavily repo 85.92% — [tavily-search-evals](https://github.com/tavily-ai/tavily-search-evals); NEEDLE perplexity 74% (1st), perplexity-fast 72% (176 / 260 ms, $1) — [NEEDLE](https://keenableai.github.io/needle/); AIMultiple 12.96 (7th of 8), 11+ s — [AIMultiple](https://aimultiple.com/agentic-search); cloro 33% overlap, median result age ~277 days — [cloro](https://cloro.dev/blog/best-search-api/); Exa 3.0 run BC 91.5 / ATLAS 37.2 — [MarkTechPost](https://www.marktechpost.com/2026/10/20/exa-3-0-search-api-lite/); Keiro harness 86/83/74 — [Keiro](https://keirolabs.cloud/blog/web-search-apis-for-agents-2026); Perplexity Fast Search 160 ms median / 230 ms p95 (vendor claim relayed) — [Parallel](https://parallel.ai/compare/perplexity-vs-parallel); You.com FinSearchComp T2: perplexity_finance_historical_lookup 72.27%, sonar_deep_research_high 53.78% — [web-search-api-evals](https://github.com/youdotcom-oss/web-search-api-evals).

**You.com (vendor)**
- Sept 21 2026 Highlights launch: SimpleQA by mode — Snippets 81.68%, Highlights 95.17%, Full page 88.98%; FRAMES 80.58 / 82.04 / 82.77; RetrievalQA 63.91 / 66.93 / 63.77; cross-provider SimpleQA (best config each): You.com+Highlights 95.17% @ 695 ms p50, Exa (full page) 95.47% @ 1,337 ms, Parallel (advanced) 95.33% @ 2,098 ms; Braintrust independent eval (1,329 Qs) cost per query: Claude Sonnet 5 $0.0747 (You.com) vs $0.1148 (built-in search, −35%); GPT-5.6 Terra $0.0417 vs $0.0467 (−11%); Highlights same $5 CPM — [You.com](https://you.com/resources/highlights-parameter-web-search-api); [Unite.ai coverage](https://www.unite.ai/you-com-web-search-highlights-reaches-95-17-on-simpleqa/).
- Open harness run Oct 7 2026 (grader GPT-5.4 mini; synthesis stated as both GPT-5.6 Luna and GPT-5.4 nano): SimpleQA you_search 96.11% (598 ms), exa_search_with_text 95.40% (2,502 ms), you_search_with_livecrawl 95.23% (4,000 ms), parallel_search_basic 94.87% (1,660 ms), tavily_search 88.53% (1,930 ms), google_search 50.08% (1,430 ms); FRAMES you 74.03%, parallel 73.79%, exa 73.79%, you livecrawl 72.12%, tavily 66.14%, google 60.00%; FinSearchComp T2 you_finance_research_deep 87.29%, parallel_ultra 73.11%, perplexity_finance_historical_lookup 72.27%, perplexity_sonar_deep_research_high 53.78%, exa_research_pro 42.02%, tavily_research_pro 40.34%, parallel_pro 34.45% — [web-search-api-evals](https://github.com/youdotcom-oss/web-search-api-evals).
- Third-party: AA 68 (launch) → 74 highlights (DSQA 77, BC 77, Omni 69; $47.54; 21.5 s) — [AA](https://artificialanalysis.ai/agents/search-api); Openbenchmarks highlights 90.7% / 628 ms, knowledge=core 92.0% / 889 ms; coding 55.0 / 54.0 (fetch), 41.3 / 38.3 (search-only); multi-hop 38.6 / 38.5 — [Openbenchmarks](https://openbenchmarks.com/web-search); NEEDLE 58% (544 / 736 ms) — [NEEDLE](https://keenableai.github.io/needle/); Keiro cites 92.1% (GPT-5.4 nano / GPT-5.4 mini) — [Keiro](https://keirolabs.cloud/blog/most-accurate-web-search-api); agenticsearch 68 — [Agentic Search](https://www.agenticsearch.cloud/posts/i-benchmarked-15-ai-search-apis/).

**Jina (no vendor head-to-head found)**
- NEEDLE: jina 40% (last), p50 17 s / p95 25 s, $3.40/1k, 3.5% errors; Jina's default mode fetches each result page so its "snippet" is page content clipped to budget — [NEEDLE](https://keenableai.github.io/needle/).
- agenticsearch blended 58 at $0.02/1k (estimate) — [Agentic Search](https://www.agenticsearch.cloud/posts/i-benchmarked-15-ai-search-apis/).
- ZenRows (competitor) scraping-success test: Jina Reader 99.33% success, ~1.26 s — not an accuracy benchmark — [ZenRows](https://www.zenrows.com/blog/best-web-scraping-api-for-ai-agents).

**Nimble (no vendor head-to-head found)**
- AA standard 74 (DSQA 76, BC 75, Omni 71; $46.14; 24.6 s) — [AA](https://artificialanalysis.ai/agents/search-api); Openbenchmarks lite 94.3% / 2.46 s / $1.1 (lowest paid cost per correct answer, $1.17/1k), standard 93.0% / 861 ms / $5; coding lite 60.3±2.5%, standard 45.0±1.0%; multi-hop standard 30.7 / 31.3, lite 25.3 / 27.1 — [Openbenchmarks](https://openbenchmarks.com/web-search); AIMultiple agentic-web (scraping, not answer accuracy): Nimble CLI slowest at 830 s — [AIMultiple](https://aimultiple.com/agentic-web).

**Bright Data (no answer-accuracy head-to-head found)**
- Bright Data blog relays AIMultiple 2026 agentic benchmark: 100% search success / 90% automation vs Nimble 93% / N/A; 76.8% success at 250 concurrent agents vs Nimble 51.2%; AIMultiple web-data index Bright Data 91.7 (1st) vs Nimble 82.8 (4th) — scraping success, not QA accuracy — [Bright Data](https://brightdata.com/blog/ai/data-for-ai-benchmarks); [AIMultiple web-data](https://aimultiple.com/web-data-scraping); HackerNoon SERP reliability 99.99% success for Bright Data SERP API (no competitors) — [HackerNoon](https://hackernoon.com/serp-benchmarks-success-rates-and-latency-at-scale).

**Others appearing in head-to-heads**
- SerpApi/Serper/Google: Parallel July SerpApi 23.3% BC etc. (above); Openbenchmarks "SERP" 96.0% / 751 ms / $3 factual, 0.4% / 0.0% multi-hop F1; AIMultiple SerpAPI 12.28 (last), 2.4 s; arlenkumar SerpAPI hit@5 69.2% (p≈0.001 vs Exa); NEEDLE google/serper 46% ($0.30), bing/searchapi 48%; Tavily repo Serper 82.15%; You.com google_search 50.08%; Valyu Google 38% SimpleQA; Keiro Google-via-Serper 82.2%; BrowseComp-Plus GPT-5 + Google Search API 59.9% — sources as cited above and [BrowseComp-Plus](https://texttron.github.io/BrowseComp-Plus/).
- OpenAI Web Search: AA 74 (Oct 6 2026); Parallel July 57.7% BC; Parallel finance T3 48.3% (64.0 unadjusted), T2 77.9% (82.8), FF 45.0, PWS 83.7%; NEEDLE chatgpt-search 53% (43 s / 53 s, $10); Search Arena api-gpt-4o-search below Gemini/Sonar (Apr 2025) — [AlphaSignal](https://alphasignal.ai/news/openai-web-search-scores-74-but-loses-on-cost-to-cheaper-rivals); [Parallel](https://parallel.ai/benchmarks); [NEEDLE](https://keenableai.github.io/needle/); [Arena blog](https://arena.ai/blog/search-arena/).
- Anthropic/Claude web search: Keiro cites 90.5% SimpleQA (GPT-5.4 agent, native tool); NEEDLE claude-search 53% (36 s / 51 s, 57.8% errors); Exa WebCode Claude signal 55.1; cloro says Claude search uses the Brave index — [Keiro](https://keirolabs.cloud/blog/most-accurate-web-search-api); [NEEDLE](https://keenableai.github.io/needle/); [Exa vs Parallel](https://exa.ai/versus/parallel); [cloro](https://cloro.dev/blog/best-search-api/).
- Octen: AA 77 (DSQA 80, BC 86, Omni 66; $9.07 search; 15.8 s; 0.21 s/query); NEEDLE 49% (200 / 381 ms, $1) — [AA](https://artificialanalysis.ai/agents/search-api); [NEEDLE](https://keenableai.github.io/needle/).
- DeepSeek Search (launched Oct 17 2026): AA 69 (DSQA 75, BC 63, Omni 70; $8.47; 22.6 s; 17th of 27); NEEDLE 57% (587 / 733 ms, $0.75) — [AA](https://artificialanalysis.ai/agents/search-api); [NEEDLE](https://keenableai.github.io/needle/).
- Context.dev: Openbenchmarks 98.0% / 15.93 s / $4.4; NEEDLE 60% ($0.50; 1.7 / 4.0 s) — price discrepancy between the two boards — [Openbenchmarks](https://openbenchmarks.com/web-search); [NEEDLE](https://keenableai.github.io/needle/).
- TinyFish: Openbenchmarks 92.0% / 2.62 s / free (30 req/min); coding 79.0±2.0% (fetch, 3rd) / 59.3±1.5%; multi-hop 26.6 / 30.2; cheapest per task ($0.035–0.050 coding; $0.212–0.219 multi-hop); NEEDLE 44% (9.8% errors) — [Openbenchmarks](https://openbenchmarks.com/web-search); [NEEDLE](https://keenableai.github.io/needle/).
- Kagi: NEEDLE 47% ($12; 87.9% errors); agenticsearch 65 — [NEEDLE](https://keenableai.github.io/needle/); [Agentic Search](https://www.agenticsearch.cloud/posts/i-benchmarked-15-ai-search-apis/). Seltz: Openbenchmarks multi-hop 14.5 / 16.3 — [Openbenchmarks](https://openbenchmarks.com/web-search).
- Keirolabs (vendor): deep search 95.3% SimpleQA (retrieval-only judged check, n=1,000), standard 84%; FinanceBench 78%; own 100-query harness (Gemma 3 12B judge; only Keiro/Perplexity/Tavily scored) Keiro 94/91/82, Perplexity 86/83/74, Tavily 78/77/68 — [Keiro Oct 19 2026](https://keirolabs.cloud/blog/most-accurate-web-search-api); [Keiro Sept 18 2026](https://keirolabs.cloud/blog/web-search-apis-for-agents-2026).

### Inferences
- The only vendor harnesses that are open-source and have been used by third parties are Perplexity's `search_evals`, Tavily's `tavily-search-evals`, You.com's `web-search-api-evals`, Linkup's `eval-simpleQA`, Valyu's `valyu-benchmarks`, Keenable's `needle` and Exa's `exa-labs/benchmarks`; Firecrawl's 94.7%, Tavily's 97.6%, Linkup's 94% Verified and Brave's FreshQA table have no published code or raw outputs.
- Vendors systematically pick the competitor tier that loses (Exa `lite` vs Tavily `advanced`; Parallel Turbo vs Exa Instant; Firecrawl "best of two sessions"), and several report "best observed" rather than mean scores.

### Gaps
- Jina, Nimble and Bright Data: no vendor-authored answer-accuracy comparison located (search budget exhausted before jina.ai/news and nimbleway.com could be checked directly).
- Brave's FreshQA source post (with model/harness) was not found; only the API landing page figures exist.
- Tavily's Aug 2026 competitor scores, Firecrawl's competitor scores, Linkup's 94% harness details (model, grader, n) are not in text anywhere I could access.
- Valyu's updated /benchmarks page is 404.

---

## Key Question 6 — Independent and academic comparisons (BrowseComp-Plus, Openbenchmarks, AIMultiple, arlenkumar, cloro, Search Arena, HN/Reddit)

### Takeaway
Truly independent cross-vendor numbers come from five sources: Artificial Analysis (Q2), Openbenchmarks (13 vendors, 3 tasks, open code, Oct 21 2026), AIMultiple (8 APIs, 100 queries, Dec 2025), arlenkumar.com (4 vendors, 299 golden queries, June 2026) and LMArena/Arena Search Arena (search-augmented models, not APIs, Apr 2025). BrowseComp-Plus (academic) deliberately replaces commercial APIs with a fixed corpus and offers only one commercial data point (GPT-5 + Google Search API 59.9%). HN threads contain prices and anecdotes but no reproducible mini-benchmarks; no Reddit mini-benchmark was found.

### Cited Findings

**Openbenchmarks (independent; "no vendor pays"; code `openbenchmarks-labs/*` on GitHub, datasets on Hugging Face; last measured Oct 21 2026)** — [Openbenchmarks](https://openbenchmarks.com/web-search); [summary page](https://openbenchmarks.com/web-search/best-web-search-api-for-ai)
- Tasks: Factual lookup (300 company-news Qs, max 10 results, extractor `gpt-5.6-terra` medium, judge `claude-opus-5` via Bedrock; model-only baseline 10.9%); Hard retrieval / coding agents (100 held-out tickets ×3 runs, agent `gpt-5.6-sol`, 5 searches, 32 turns; baseline 0); Multi-hop company discovery (45 Qs ×3 runs, 5,400 agent runs, `gpt-5.6-sol` medium, 8 turns, 14 searches; baseline F1 20.1%). Known issue: "Vendors benchmarked later tend to score higher, for reasons unrelated to quality"; re-run in progress; advises against using factual-lookup rankings to compare vendors. Datasets: 100/300 news Qs public; 30 coding tickets public (board uses private set); 10/45 company Qs public. Changelog: 2026-09-09 TinyFish re-eval; 09-11 Tavily updated; 09-15 Nimble and You added.

Factual lookup (accuracy; mean latency; list $/1k):

| API | Acc | Mean latency | $/1k |
|---|---|---|---|
| Exa fast | 99.3% | 652 ms | $7 |
| Context | 98.0% | 15.93 s | $4.4 |
| Exa instant | 97.7% | 398 ms | $7 |
| Perplexity (low) | 97.3% | 1.38 s | $5 |
| Linkup fast | 96.7% | 1.57 s | $5 |
| SERP | 96.0% | 751 ms | $3 |
| Firecrawl | 95.3% | 510 ms | $5 |
| Nimble lite | 94.3% | 2.46 s | $1.1 |
| Brave LLM Context | 94.0% | 601 ms | $5 |
| Brave Web | 93.3% | 630 ms | $5 |
| Parallel Basic* | 93.3% | 1.68 s | $5 |
| Nimble standard | 93.0% | 861 ms | $5 |
| Tavily advanced | 93.0% | 4.29 s | $16 |
| TinyFish | 92.0% | 2.62 s | free (30 rpm) |
| Linkup standard | 92.0% | 2.55 s | $5 |
| You (highlights, knowledge=core) | 92.0% | 889 ms | $5 |
| You (highlights) | 90.7% | 628 ms | $5 |
| Tavily basic | 87.7% | 1.88 s | $8 |
| Parallel Fast* | 86.0% | 942 ms | $1 |
| Parallel Turbo* | 71.3% | 348 ms | $1 |

*Parallel rows were absent from the Oct 21 main-board fetch but appear on Openbenchmarks data relayed by Parallel's compare pages (Sept 12 2026 "fastest" board) — [Parallel vs Firecrawl](https://parallel.ai/compare/firecrawl-vs-parallel); [Parallel vs Brave](https://parallel.ai/compare/brave-vs-parallel).

Coding agents, search+fetch (task completion ± SD; median time): Exa deep 83.0±1.0% (37 s); Exa auto 81.7±1.1% (23 s); TinyFish 79.0±2.0% (24 s); Perplexity 77.7±1.5% (22 s); Parallel advanced 77.0±1.0% (33 s); Parallel basic 76.0±0.0% (30 s); Firecrawl 76.0±1.0% (34 s); Nimble lite 60.3±2.5%; Tavily advanced 60.0±2.0%; Tavily basic 59.0±1.7%; You highlights 55.0±1.7%; You core 54.0±2.0%; Linkup standard 48.3±4.9%; Nimble standard 45.0±1.0%.
Coding agents, search-only: Perplexity 77.3±2.1% (18 s); Firecrawl 70.3±1.5%; Parallel fast 66.7±1.5%; Exa fast 66.3±1.5%; Parallel turbo 64.7±2.1%; Exa instant 61.3±2.9%; TinyFish 59.3±1.5%; Tavily basic 51.0±5.3%; Nimble lite 46.7±3.8%; Linkup fast 43.3±1.1%; Nimble standard 42.3±2.5%; You highlights 41.3±3.1%; You core 38.3±3.2%; Brave 38.0±2.6%.
Multi-hop company search, search-only (F1; median time): Parallel basic 46.5% (67.6 s); Exa deep 45.4% (89.5 s); Parallel advanced 44.2%; Exa instant 43.3%; Linkup fast 41.1%; Tavily advanced 41.1%; Linkup standard 40.6%; You highlights 38.6%; You core 38.1%; Parallel fast 38.0%; Perplexity 37.8%; Tavily basic 36.5%; Parallel turbo 34.7%; Nimble standard 30.7%; Firecrawl 30.4%; Brave 28.0% (43.5 s, fastest); TinyFish 26.6%; Nimble lite 25.3%; Seltz 14.5%; SERP 0.4%.
Multi-hop, search+fetch: Exa deep 48.2%; Perplexity 46.6%; Exa instant 44.9%; Parallel basic 42.3%; Parallel advanced 42.2%; Linkup standard 42.0%; Tavily advanced 41.0%; Linkup fast 39.9%; Parallel fast 39.3%; You highlights/core 38.5%; Tavily basic 38.1%; Parallel turbo 36.0%; Firecrawl 33.2%; Nimble standard 31.3%; TinyFish 30.2%; Brave 29.4%; Nimble lite 27.1%; Seltz 16.3%; SERP 0.0%.
Latency reporting: mean search latency (factual), median end-to-end task time (coding, multi-hop); no p50/p95. Cost: list $/1k and $ per 1k correct answers (factual); median LLM+API cost per run (others).

**AIMultiple (independent; Dec 2025 snapshot; published Jan 8–9 2026; updated May 13–14 2026)** — [AIMultiple](https://aimultiple.com/agentic-search)
- 100 real AI/LLM queries from AIMultiple's top-500 organic queries; 5 results per query per API (~4,000 results); judge GPT-5.2 via OpenRouter temp 0 (relevance bool, quality 1–5, noise, source type); ~10% human-verified; Agent Score = mean relevant × quality (max 25); 10k bootstrap CIs; Contabo VPS France; 30 s timeout. Limitations: AI/LLM-domain only, single time point.

| Rank | API | Mean relevant /5 | Quality /5 | Agent Score (95% CI) | Latency |
|---|---|---|---|---|---|
| 1 | Brave Search | 4.28 | 3.48 | 14.89 (13.80–15.93) | 669 ms |
| 2 | Firecrawl | 4.30 | 3.39 | 14.58 (13.12–15.98) | 1,335 ms |
| 3 | Exa | 4.32 | 3.33 | 14.39 (13.25–15.50) | ~1.2 s |
| 4 | Parallel Search (Pro) | 4.32 | 3.29 | 14.21 (13.07–15.47) | 13.6 s |
| 5 | Tavily | 4.18 | 3.27 | 13.67 (12.62–14.76) | 998 ms |
| 6 | Parallel Search (Base) | 4.18 | 3.23 | 13.50 (12.38–14.66) | ~2.9 s |
| 7 | Perplexity | 4.00 | 3.24 | 12.96 (11.77–14.22) | 11+ s |
| 8 | SerpAPI | 3.58 | 3.43 | 12.28 (11.19–13.41) | 2.4 s |

- Top four statistically indistinguishable; only Brave > Tavily (~1 point) is significant; latency varies ~20x — [AIMultiple](https://aimultiple.com/agentic-search).

**arlenkumar.com GoldenEvalWebSearch (independent; updated June 14 2026; snapshot `web_search-2026-q3`)** — [arlenkumar](https://arlenkumar.com/bench/leaderboards/web-search)
- 299 public descriptive queries ×3 reps (30% private holdout excluded); deterministic set-membership vs golden URLs; 95% Wilson CIs; McNemar Exa vs SerpAPI p≈0.001; latency/cost/freshness not measured this snapshot; raw JSON and code (github.com/arlenk2021/GoldenEvalsWebSearch) published.

| Vendor | hit@1 | hit@5 (95% CI) |
|---|---|---|
| Exa | 62.2% | 80.9% (76.1–85.0) |
| SerpAPI | 56.9% | 69.2% (63.8–74.2) |
| Brave | 48.8% | 58.9% (53.2–64.3) |
| Tavily | 31.4% | 49.4% (43.8–55.0) |

**cloro.dev Google-overlap study (vendor-adjacent: cloro sells a Google SERP API; run July 8 2026; pub. June 20 2026, upd. Nov 4 2026)** — [cloro](https://cloro.dev/blog/best-search-api/)
- 500 queries, 5 intents, 12 verticals; vs live Google top-10. URL overlap@10 / domain Jaccard / Google-domain recall / "#1 is Google-ranked" / Spearman ρ / results dated / returns answer / $ per 1k: Tavily ~60% / 0.66 / 80% / 78% / 0.03 / 0% / 99.6% / ~$8; Brave 47% / 0.45 / 65% / 89% / 0.55 / 63% / 0% / $5; Perplexity Search API 33% / 0.33 / 49% / 72% / 0.43 / 100% / 0% / $5 (median result age ~277 days); Exa 32% / 0.30 / 44% / 48% / 0.27 / 0% / 0% / $7 ($4 lite); no latency.

**agenticsearch.cloud (Keiro-affiliated; Aug 16 2026)** — [Agentic Search](https://www.agenticsearch.cloud/posts/i-benchmarked-15-ai-search-apis/)
- 350 Qs (200 FinanceBench subset, 150 SimpleQA subset); gold-answer matcher + 10% human re-score; no model named; only Keirolabs fully run — other scores "blended from public evals, vendor claims, and spot tests, ±3". Blended: Keirolabs 81 ($0.25/1k), Perplexity Sonar 77 (~$2), Exa 73 ($7+$1), Tavily 70 ($8), You.com 68 ($3.50), Kagi 65 ($4), Brave 64 ($5), Bing 62 ($3), Linkup 60 ($5.50), Google CSE 59 ($5), Jina 58 ($0.02), Firecrawl 53 ($3.20), ScrapingBee 51 ($1), Serper 46 ($1), SerpAPI 43 ($15). Author: "looks like an ad". No p50/p95.

**BrowseComp-Plus (academic; arXiv 2508.06600, Aug 8 2025; ACL 2026 long paper)** — [arXiv](https://arxiv.org/abs/2508.06600); [leaderboard page](https://texttron.github.io/BrowseComp-Plus/)
- 830 queries over a fixed corpus of 100,195 documents, built to replace black-box commercial search APIs; GPT-5 + Google Search API 59.9% (only commercial-API entry); GPT-5 + Qwen3-Embedding-8B 70.1%; GPT-5 + BM25 55.9%; Search-R1 + BM25 3.86%; Qwen3-Embed-8B beats BM25 for every model (gpt-4.1 14.58→35.42; o3 49.28→63.49; Sonnet 4 14.34→36.75) and cuts search calls by ~1–3; Qwen3-Embedding-8B retriever-only 20.3 nDCG@10; GPT-5/o3 average >20 search calls/query; leaderboard table "will be posted soon" on the HF space. Mixedbread (vendor) claims 90.48% (get-document scaffold) / 80% standard vs 71.69% Qwen3-Embed — [Mixedbread](https://www.mixedbread.com/evals/browsecomp-plus).
- No paper comparing several commercial search APIs as agent tools on BrowseComp-Plus was found.

**LMArena / Arena Search Arena (independent crowd preference; models, not APIs)** — [Arena blog, Apr 15 2025 (upd. Aug 2 2025)](https://arena.ai/blog/search-arena/)
- ~7,000 votes (Mar 18–Apr 13 2025; 11k collected before filtering); 11 models from Perplexity, Gemini, OpenAI; Bradley-Terry → Elo; ordering: gemini-2.5-pro-grounding and ppl-sonar-reasoning-pro-high lead; then rest of Sonar family (ppl-sonar-reasoning ahead); gemini-2.0-flash-grounding; then api-gpt-4o-search > api-gpt-4o-mini-search; scores: Gemini-2.5-Pro-Grounding 1142 (+14/−17), Sonar-Reasoning-Pro-High 1136 (+21/−19), Sonar beat Gemini 53% head-to-head (Perplexity's framing) — [Perplexity Threads post](https://www.threads.com/@perplexity/post/DIcPnZfxm_l); [TestingCatalog](https://www.testingcatalog.com/perplexity-sonar-model-ties-with-google-gemini-in-top-ai-search-ranking/). Drivers: response length (coef 0.255, p<0.05), citation count (0.234, p<0.05); Sonar cites 2–3x more sources; OpenAI ~2–2.5 citations/response. Live leaderboard (arena.ai/leaderboard/search) returned 403 on 2026-11-05; no 2026 standings obtained.

**Hacker News (anecdotal; no reproducible mini-benchmark found)**
- "The Parallel Search API" (≈Nov 2025): judge GPT-4.1 criticised; Parallel says latest runs "against GPT-5"; a chart point at 47% noted; "5 s" basic-tier latency questioned — [HN](https://news.ycombinator.com/item?id=45837425).
- "Show HN: Keenable" (≈Aug 2026): prices Keenable $4/1k (50 results), Parallel $5, Exa $7 (+ per extra result); Keenable p50 <200 ms — [HN](https://news.ycombinator.com/item?id=49435555).
- "DeepSeek search and fetch" (≈Oct 2026): Keenable ran NEEDLE on DeepSeek (qualitative only); prices Ceramic $0.25/1k, Serper $1, Mojeek £2, Exa $4, Brave $5, LinkUp $5 search + $1 fetch, Kagi $12; SerpAPI $1.50 claim disputed (">$9/1k cheapest tier"); break-even vs a €5/mo plan: Tavily Basic 1,704 searches/mo, Exa Fast/Auto 2,233, Exa Instant 3,907, DeepSeek 7,503, Ceramic 22,507; one user's LLM-preference test ranked Exa and Tavily first, Brave second, SearXNG last (no numbers) — [HN](https://news.ycombinator.com/item?id=50138531).
- Reddit: no thread with a reproducible benchmark surfaced in any search.

### Inferences
- Across independent boards, Exa leads retrieval-heavy single-query tasks (Openbenchmarks factual 99.3%, arlenkumar hit@5 80.9%) and Exa deep leads fetch-enabled agent tasks; Perplexity leads search-only agent tasks; Parallel basic leads search-only multi-hop; Brave leads AIMultiple's relevance-quality rubric. This is the empirical basis for "no single winner".
- Openbenchmarks' own warning about order-of-benchmarking effects, plus AIMultiple's overlapping CIs, means most 1–3 point gaps on these boards are not significant.

### Gaps
- No academic paper benchmarking several commercial search APIs as agent tools (beyond BrowseComp-Plus's single Google data point) was found.
- Search Arena's current (2026) leaderboard is inaccessible; whether Sonar/Gemini/OpenAI positions changed is unknown.
- Openbenchmarks' per-vendor run dates and its Parallel rows were not fully visible in the main-board fetch.

---

## Key Question 7 — Where results conflict and why (harness / product-version differences)

### Takeaway
The same product's "BrowseComp" score spans 32%–91.8% and "SimpleQA" 71%–97.6% across sources; each gap maps to an identifiable change in agent model, reasoning effort, sample, tool budget, judge, tier/endpoint, or scoring rule (best-of vs mean), not to a change in the underlying index.

### Cited Findings
- Parallel Turbo BrowseComp: 51% (July 2026; GPT-5.4 agent+judge; n=1,266; 20 tool calls; best observed across sessions) vs 32% (Sept 9 2026; GPT-5.6 Luna low; n=50; unnamed judge) vs 75 BrowseComp component (AA Aug 18 2026; GPT-5.6 Luna medium; 200 hard Qs; 25 turns) — [Parallel compare](https://parallel.ai/compare/serpapi-vs-parallel); [Parallel benchmarks](https://parallel.ai/benchmarks); [AA](https://artificialanalysis.ai/articles/search-api).
- Exa BrowseComp: 33.7% (Instant; Parallel July) / 70% & 36% (Auto; Parallel Sept frontier/low-cost) / 74 → 83 (AA auto, Aug → Oct, after Exa 3.0 dynamic highlights) / 0.336 (gpt-5-medium, Perplexity search_evals) / 0.127 (claude-opus-4-5-thinking, same repo) / 74% (Exa Agent High, Exa June 2026) / 91.8% (Exa 3.0 Auto, Exa's Scout harness, Oct 19 2026) — sources as above.
- Perplexity BrowseComp: 46% / 74% (Parallel Sept low/frontier) / 86% (Perplexity "high", Parallel Task-API run Aug 26) / 78.0 high & 85.33 xhigh (Perplexity's own harness, via Parallel) / 87 (AA medium) / 91.5 (Exa 3.0 run) / 0.805 (Agent API, search_evals) / .371 (Sept 2025 Search API launch eval) — [Parallel benchmarks](https://parallel.ai/benchmarks); [Parallel vs Perplexity](https://parallel.ai/compare/perplexity-vs-parallel); [AA](https://artificialanalysis.ai/agents/search-api); [MarkTechPost](https://www.marktechpost.com/2026/10/20/exa-3-0-search-api-lite/); [search_evals](https://github.com/perplexityai/search_evals); [Perplexity 2025](https://www.perplexity.ai/hub/blog/architecting-and-evaluating-an-ai-first-search-api).
- Brave on AA: 65 ("Brave Search", Aug 18) → 75 ("Brave Search (LLM context)", Sept 22 onward) — endpoint change, not re-scoring — [AA launch](https://artificialanalysis.ai/articles/search-api); [AA leaderboard](https://artificialanalysis.ai/agents/search-api).
- Exa SimpleQA: 71.24% (Tavily harness, gpt-4.1 one-shot extraction) / 90.04% (Exa 2025, gemini-1.5-flash + GPT-4o-mini) / 91% (Valyu Oct 2025) / 0.874 (gpt-5-medium agent, search_evals) / 91.9% (Keiro-cited GPT-5.4 agent) / 91% SQA-Verified (Parallel Sept) / 95.40–95.47% (You.com GPT-5.4-nano/mini harness, full page) — sources above.
- Tavily SimpleQA: 73% (Linkup-run 2025) / 93.3% (own repo, gpt-4.1) / 97.6% (own, gpt-5.4 mini reader, Aug 2026) / 0.798 (gpt-5-medium, search_evals) / 88.53% (You.com harness) / 92%–94% SQA-Verified (Parallel Sept) — sources above.
- Latency for the same product differs by measurer: Parallel Turbo ~200 ms p50 (vendor) vs 216–240 ms p50 (Parallel July, us-central) vs 348 ms mean (Openbenchmarks) vs 344/550 ms p50/p95 (NEEDLE) vs 0.51 s/query (AA); Exa Instant "sub-200 ms" (Exa) vs 335–361 ms p50 (Parallel) vs 398 ms mean (Openbenchmarks); Tavily Ultra Fast 90 ms (Tavily claim) vs 150–357 ms p50 (Parallel) vs 210–420 ms (Exa) — [Parallel](https://parallel.ai/compare/exa-vs-parallel); [Openbenchmarks](https://openbenchmarks.com/web-search); [NEEDLE](https://keenableai.github.io/needle/); [AA](https://artificialanalysis.ai/articles/search-api); [Exa Instant](https://exa.ai/blog/exa-instant); [Exa vs Tavily](https://exa.ai/versus/tavily).
- Parallel itself says its three BrowseComp tables (Search API, Task API, AA) "measure different things and should not be compared directly" — [Parallel BrowseComp article](https://parallel.ai/articles/browsecomp-benchmark).
- You.com's harness README states two different synthesis models for the same results; Exa's ATLAS post states GPT-5.6 Luna in one place and GPT-6 Luna in another; Parallel's benchmarks page uses GPT-5.6 for search runs and GPT-6 for finance runs (and GPT-6 Luna for its own Fast arm only) — [web-search-api-evals](https://github.com/youdotcom-oss/web-search-api-evals); [Exa ATLAS](https://exa.ai/blog/atlas-benchmark); [Parallel benchmarks](https://parallel.ai/benchmarks).

### Inferences
- Reasoning effort of the agent is the single biggest lever: Parallel's Luna-low tier scores ~30 points below its Sol-high tier on identical search APIs; AA's Luna-medium agent sits between. Any BrowseComp comparison across sources without matching the agent is meaningless.
- "Best observed across sessions" (Parallel July; Firecrawl) inflates scores relative to mean-of-3-run reporting (Openbenchmarks, Parallel finance).
- Product-version drift (Exa 2.x → 3.0; Brave Search → LLM Context; Tavily basic → advanced/ultra-fast; Perplexity Search vs Fast Search) means dated snapshots are required; AA and Openbenchmarks date their boards, most vendor pages do not.

### Gaps
- No source re-ran the July 2026 Parallel configuration in September (or vice versa), so the model-vs-sample contribution to the 51% → 32% change cannot be separated.

---

## Key Question 8 — Latency (who publishes p50/p95) and cost per 1k queries by product tier

### Takeaway
Only four sources publish true percentiles across vendors: Keenable's NEEDLE (p50/p95, 23 engines, vendor-run), Perplexity's 2025 launch eval (p50/p75/p90/p95, 4 providers), Parallel's July-2026 compare pages (p50 only, 4 products) and You.com's harness (p50, 6 samplers); Exa publishes p50 for Exa/Parallel tiers and a p95 anecdote; Brave states "under 500 ms at P90". Independent boards (AA, Openbenchmarks, AIMultiple) report means/medians per query or per task, not percentiles. List prices cluster at $1/1k (Parallel Turbo/Fast, Perplexity Fast, Keenable, Octen), $4–5/1k (Exa Lite, Brave, Perplexity, You.com, Linkup, Parallel Basic/Advanced), $7–16/1k (Exa Auto/Deep, Tavily basic/advanced) and $10+/1k for first-party model search tools (OpenAI, Anthropic).

### Cited Findings

**Percentile latency tables (all values as published)**
| Source (date; author) | Product | p50 | p75 | p90 | p95 | Client location / notes |
|---|---|---|---|---|---|---|
| Perplexity (Sept 25 2025; vendor) | Perplexity Search | 358 ms | 443 | 604 | 763 | AWS us-east-1 — [Perplexity](https://www.perplexity.ai/hub/blog/architecting-and-evaluating-an-ai-first-search-api) |
| | Brave | 513 | 637 | 728 | 808 | |
| | Tavily (SERP-based) | 1,342 | 1,586 | 1,743 | 1,790 | |
| | Exa | 1,375 | 1,499 | 1,798 | 2,188 | |
| Parallel (July 10–12 2026; vendor) | Parallel Turbo | 216–240 ms | — | — | — | us-central; BrowseComp/SimpleQA runs — [Parallel](https://parallel.ai/compare/serpapi-vs-parallel) |
| | Exa Instant | 335–361 ms | — | — | — | |
| | Tavily Ultra Fast | 150–357 ms | — | — | — | [Parallel](https://parallel.ai/compare/tavily-vs-parallel) |
| | SerpApi | 652–999 ms | — | — | — | |
| Exa (July 2026; vendor) | Exa Lite / Exa Auto | ~450 / 1,502 ms | — | — | — | [Exa vs Parallel](https://exa.ai/versus/parallel) |
| | Parallel basic / advanced | 906 / 2,246 ms | — | — | — | |
| Exa (undated "Fortune 100" eval; vendor) | Exa / Tavily | — | — | — | 1.4–1.7 s / 3.8–4.5 s | [Exa vs Tavily](https://exa.ai/versus/tavily) |
| You.com (Sept 21 2026; vendor) | You.com Highlights / Exa full page / Parallel advanced | 695 / 1,337 / 2,098 ms | — | — | — | [You.com](https://you.com/resources/highlights-parameter-web-search-api) |
| You.com harness (Oct 7 2026; vendor) | you_search / parallel_basic / tavily / google / exa_with_text / you_livecrawl | 598 / 1,660 / 1,930 / 1,430 / 2,502 / 4,000 ms | — | — | — | provider-internal latency where available — [GitHub](https://github.com/youdotcom-oss/web-search-api-evals) |
| NEEDLE (Nov 2026; vendor Keenable) | Keenable / perplexity-fast / octen / parallel-turbo / exa-lite / you / brave / deepseek / firecrawl / perplexity / brave-llmcontext / kagi / linkup / exa / google-serper / tavily / context.dev / tinyfish / bing-searchapi / parallel / jina / claude-search / chatgpt-search | 154 / 176 / 200 / 344 / 464 / 544 / 558 / 587 / 843 ms / 1.2 / 1.2 / 1.2 / 1.3 / 1.4 / 1.5 / 1.6 / 1.7 / 1.9 / 2.1 / 2.4 / 17 / 36 / 43 s | — | — | 317 / 260 / 381 / 550 / 689 / 736 / 807 / 733 ms / 3.5 / 1.6 / 2.4 / 2.1 / 1.9 / 3.2 / 3.0 / 3.2 / 4.0 / 4.3 / 7.5 / 3.9 / 25 / 51 / 53 s | GitHub Actions runners; sequential calls — [NEEDLE](https://keenableai.github.io/needle/) |
| Brave API page (undated; vendor) | LLM Context | — | — | <500 ms | — | [Brave](https://brave.com/search/api/) |
| Vendor claims relayed by Parallel (Oct 2026) | Perplexity Fast Search | 160 ms median | — | — | 230 ms | [Parallel](https://parallel.ai/compare/perplexity-vs-parallel) |
| Keenable blog (Aug 27 2026; vendor) | Keenable | 200 ms | — | — | target 200 ms | [Keenable](https://keenable.ai/blog/needle-the-benchmark-your-search-engine-can-t-memorize) |

**Mean/median latency sources (no percentiles)**: Openbenchmarks mean search latency (table in Q6) and median task times — [Openbenchmarks](https://openbenchmarks.com/web-search); AA per-task time and per-query averages (Octen 0.21 s, Keenable realtime 0.34 s, Parallel turbo 0.51 s, Exa fast 0.91 s, Exa auto 2.10 s) — [AA](https://artificialanalysis.ai/articles/search-api); AIMultiple mean latency (Q6) — [AIMultiple](https://aimultiple.com/agentic-search); Exa academic-track mean latency (Exa 0.578 s, Perplexity 1.277 s, Parallel adv 3.118 s, turbo 0.403 s) — [exa-labs/benchmarks](https://github.com/exa-labs/benchmarks).

**List price per 1k queries by tier (date of price check in parentheses)**
| Provider / tier | $/1k | Notes & source |
|---|---|---|
| Parallel Turbo, Fast | $1 | +$1/1k per extra 10 results; 600 RPM; $5/mo free (Oct 14 2026) — [Parallel](https://parallel.ai/compare/serpapi-vs-parallel) |
| Parallel Basic, Advanced | $5 | 10 results with extraction — [Parallel](https://parallel.ai/articles/the-honest-2026-comparison-web-search-apis-for-ai-agents) |
| Parallel Task Lite / Base / Core / Core2x / Pro / Ultra / Ultra2x / Ultra4x | $5 / $10 / $25 / $50 / $100 / $300 / $600 / $1,200 | per 1k runs — [Parallel benchmarks](https://parallel.ai/benchmarks); Ultra 8x $2.40/task — [Exa](https://exa.ai/versus/parallel) |
| Parallel Responses low / medium / high | $10 / $50 / $250 | 5–10 s / 15–20 s / 30–60 s — [Parallel](https://parallel.ai/articles/brave-search-api-vs-parallel) |
| Exa Lite | $4 | from Oct 19 2026 — [Exa 3.0](https://exa.ai/blog/exa-3) |
| Exa Auto / Fast / Instant | $7 | raised from $5 in March 2026; +$1 per extra result beyond 10 (Parallel's reading) or $1/1k contents — [Parallel](https://parallel.ai/compare/exa-vs-parallel); [Openbenchmarks](https://openbenchmarks.com/web-search) |
| Exa Deep / Deep-Reasoning | $12 / $15 | — [Parallel](https://parallel.ai/compare/exa-vs-parallel) |
| Exa Agent High | $0.50/task | — [Exa](https://exa.ai/versus/parallel) |
| Tavily basic / advanced | $8 / $16 PAYG ($0.008/credit; 1 vs 2 credits); monthly plans $0.005–0.0075/credit; Parallel lists basic/fast/ultra-fast $5–8, advanced $10–16; 1,000 RPM | — [Exa vs Tavily](https://exa.ai/versus/tavily); [Parallel](https://parallel.ai/compare/tavily-vs-parallel) |
| Brave Search / Answers | $5 / $4 + $5 per M tokens | 50 QPS / 2 QPS; $5/mo free — [Brave](https://brave.com/search/api/) |
| Perplexity Search / Fast Search | $5 / $1 | Sonar models retired Sept 27 2026 — [Parallel](https://parallel.ai/articles/which-ai-search-api-has-the-best-recall-and-accuracy) |
| You.com (incl. Highlights) | $5 | — [You.com](https://you.com/resources/highlights-parameter-web-search-api) |
| Linkup search / fetch | $5 / $1 | 4,000 free queries — [Linkup](https://www.linkup.so/blog/best-web-search-api-in-2026-top-providers-compared); [HN](https://news.ycombinator.com/item?id=50138531) |
| Firecrawl | 2 credits/search; $1.50–7.60/1k by plan (Standard $99/mo ≈ $1.98/1k); Openbenchmarks lists $5; NEEDLE $1.20 | — [Parallel](https://parallel.ai/compare/firecrawl-vs-parallel); [Openbenchmarks](https://openbenchmarks.com/web-search); [NEEDLE](https://keenableai.github.io/needle/) |
| Nimble lite / standard | $1.1 / $5 | — [Openbenchmarks](https://openbenchmarks.com/web-search) |
| Keenable | $1 (NEEDLE, Aug 21 2026) vs $4 with 50 results (HN) | — [NEEDLE](https://keenableai.github.io/needle/); [HN](https://news.ycombinator.com/item?id=49435555) |
| Octen | $1 | — [NEEDLE](https://keenableai.github.io/needle/) |
| DeepSeek Search | $0.75 | "lowest paid on AA board" — [NEEDLE](https://keenableai.github.io/needle/); [AA X](https://x.com/ArtificialAnlys/status/2113124084410425362) |
| Context.dev | $0.50 (NEEDLE) vs $4.4 (Openbenchmarks) | conflicting — sources as named |
| TinyFish | $0 (30 req/min cap) | — [Openbenchmarks](https://openbenchmarks.com/web-search) |
| Kagi | $12 | — [NEEDLE](https://keenableai.github.io/needle/) |
| Jina | $3.40 (NEEDLE) / $0.02 (agenticsearch estimate) | — [NEEDLE](https://keenableai.github.io/needle/) |
| Serper | $0.30–1.00 | — [NEEDLE](https://keenableai.github.io/needle/); [Firecrawl](https://www.firecrawl.dev/blog/best-web-search-apis) |
| SerpApi | $25 (1k/mo) → $10 (15k) → $7.25 (100k) → $5.50 (500k) → $3.75 (Cloud 1M); Parallel also cites $1.96 floor | — [Parallel](https://parallel.ai/articles/parallel-vs-serpapi-vs-brave-vs-bing); [Parallel](https://parallel.ai/compare/serpapi-vs-parallel) |
| Bing (Grounding with Bing) / SearchAPI Bing | $14 / $1 | — [Parallel](https://parallel.ai/articles/parallel-vs-serpapi-vs-brave-vs-bing); [NEEDLE](https://keenableai.github.io/needle/) |
| OpenAI web search | $10/1k calls + tokens (legacy `web_search_preview` $25); ~4 calls/task on AA | — [Parallel](https://parallel.ai/articles/the-honest-2026-comparison-web-search-apis-for-ai-agents); [AlphaSignal](https://alphasignal.ai/news/openai-web-search-scores-74-but-loses-on-cost-to-cheaper-rivals) |
| Anthropic web search | $10/1k + tokens | — [cloro](https://cloro.dev/blog/best-search-api/) |
| Keirolabs lite / deep | $0.25 / $1.78 | — [Keiro](https://keirolabs.cloud/blog/most-accurate-web-search-api) |
| Mojeek / Ceramic | £2 / $0.25 | HN comments — [HN](https://news.ycombinator.com/item?id=50138531) |

**All-in measured cost per 1k tasks (search + model)**: AA Oct 19 2026 table (Q2) and AlphaSignal totals (Perplexity medium $70.34, Octen $23.99, Parallel advanced $59.22, Brave $79.42, OpenAI $49.59, Firecrawl $42.57, Parallel basic $66.79) — [AA](https://artificialanalysis.ai/agents/search-api); [AlphaSignal](https://alphasignal.ai/news/openai-web-search-scores-74-but-loses-on-cost-to-cheaper-rivals); [Parallel vs Firecrawl](https://parallel.ai/compare/firecrawl-vs-parallel). Parallel's per-1k-question CPMs (Q1). Openbenchmarks $ per 1k correct answers: Parallel Fast $1.16, Nimble lite $1.17, Brave LLM Context $5.32, Parallel Basic $5.36, Firecrawl $5.24, Perplexity $5.14, Tavily basic $9.13, Tavily advanced $17.20 — [Openbenchmarks](https://openbenchmarks.com/web-search); [Parallel vs Tavily](https://parallel.ai/compare/tavily-vs-parallel).

### Inferences
- p95 is almost never published by vendors for competitors; the only cross-vendor p95 sets are NEEDLE (Keenable) and Perplexity's 2025 post, both vendor-run. Buyers wanting p95 must run their own harness (Openbenchmarks, Perplexity search_evals and You.com's harness are open and could be extended).
- Cost rankings invert between list price and all-in cost: Octen ($1 list, $9.07 search per 1k AA tasks) and Exa lite ($4 list, $31.20) look cheap, while Tavily basic ($8 list) was the most expensive on AA at launch ($126) because agents issue more searches with it.

### Gaps
- No source publishes p50/p95 for Parallel Basic/Advanced, Firecrawl, Nimble, You.com or Linkup from an independent client; NEEDLE is the only percentile source for these and is vendor-run.
- Price checks are dated inconsistently (NEEDLE Aug 21 2026; Parallel Oct 14 2026; AIMultiple May 2026); Exa's March 2026 price rise and Oct 2026 Lite tier mean pre-Oct cost comparisons involving Exa are stale.
