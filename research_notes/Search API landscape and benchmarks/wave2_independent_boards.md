# Wave 2: Independent cross-vendor search-API leaderboards (complete data, with dates)

Research date: 2026-11-05. Tool budget 35 calls; 33 used. Every number below is labelled **[vendor]**, **[independent]**, **[journalist]** or **[practitioner]**, and **[secondary]** when I could only reach it through a search-engine summary or a mirror rather than the primary page. All currency is USD unless marked.

Access notes that shaped coverage (so the report writer knows what is a real gap vs. a fetch failure):
- `https://artificialanalysis.ai/search` and `/evaluations/search-index` both 404; the live board is at `https://artificialanalysis.ai/agents/search-api` (found via WebSearch).
- `https://www.vals.ai/benchmarks/web-search` 404; the live board is `https://www.vals.ai/benchmarks/web_search` (underscore).
- `https://openbenchmarks.ai` returned 503 and two WebSearch queries for "OpenBenchmarks" surfaced no such project.
- `https://lmarena.ai/leaderboard/search` 301-redirects to `https://arena.ai/leaderboard/search`, which returned 403 on both the English and Italian locale paths.
- `https://needle.keenable.ai` does not resolve from this session (host outside the allowed network domains); needle.keenable.ai has to be allowed in the session's network settings before it can be fetched.
- `https://research.aimultiple.com/web-search-api/` redirects to `https://aimultiple.com/web-search-api`, which 404s; the actual benchmark is at `https://aimultiple.com/agentic-search`.
- DuckDuckGo HTML endpoint served a bot-check; Bing returned unrelated results. WebSearch worked for discovery.

---

## KQ1. Artificial Analysis Search Index: full current table, per-benchmark scores, cost and time

### Takeaway
As of the board's "Latest data" stamp of **Oct 19, 2026**, the AA Search Index covers **26 search-API products across 14 providers**, all run with GPT-5.6 Luna (medium) in AA's Stirrup harness; **Exa Search (auto, dynamic highlights) and Perplexity Search (medium) tie at 80**, with Octen Search (highlights) at 77 the cheapest high scorer ($23.57 total per 1K tasks). The default page view exposes only 13 rows (12 providers + model-only baseline); the remaining 13 configurations (incl. Tavily, Linkup, Keenable, TinyFish and several Parallel/Perplexity/Exa/Brave/Nimble/You.com variants) are hidden behind a client-side filter I could not expand within budget.

### Cited Findings

**Live leaderboard (fetched 2026-11-05; page stamp "Latest data: Oct 19, 2026") [independent — Artificial Analysis]** — [AA Search Index leaderboard](https://artificialanalysis.ai/agents/search-api)
- Intro text: 26 Search API products across 14 providers; leaderboard view labelled "12 of 26 providers", 13 rows including the model-only baseline; FAQ also cites 14 providers. Candidate answer model for every result: GPT-5.6 Luna (medium). No "total cost" column on the page; the Total column below is search + model cost, computed by me. — [Source](https://artificialanalysis.ai/agents/search-api)

| # | Provider / configuration | Search Index | DeepSearchQA F1 | BrowseComp acc. | AA-Omniscience acc. | Search $/1K tasks | Model $/1K tasks | Total $/1K (calc.) | Time per task | Baseline lift |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Exa Search (auto, dynamic highlights) | 80 | 86 | 83 | 73 | $53.17 | $10.60 | $63.77 | 36.9 s | +47 |
| 2 | Perplexity Search (medium) | 80 | 81 | 87 | 72 | $62.30 | $8.04 | $70.34 | 31.4 s | +47 |
| 3 | Exa Search (lite, dynamic highlights) | 79 | 85 | 81 | 72 | $31.20 | $10.95 | $42.15 | 19.6 s | |
| 4 | Perplexity Search (high) | 79 | 81 | 86 | 71 | $56.93 | $9.37 | $66.30 | 29.5 s | |
| 5 | Octen Search (highlights) | 77 | 80 | 86 | 66 | $9.07 | $14.50 | $23.57 | 15.8 s | |
| 6 | Parallel Search (advanced) | 75 | 81 | 77 | 67 | $47.93 | $10.67 | $58.60 | 40.0 s | |
| 7 | Brave Search (LLM context) | 75 | 78 | 77 | 69 | $61.96 | $16.95 | $78.91 | 22.9 s | |
| 8 | OpenAI Web Search (medium) | 74 | 78 | 74 | 72 | $40.19 | $9.40 | $49.59 | 33.3 s | |
| 9 | You.com Search (highlights) | 74 | 77 | 77 | 69 | $47.54 | $19.41 | $66.95 | 21.5 s | |
| 10 | Nimble Search (standard) | 74 | 76 | 75 | 71 | $46.14 | $16.64 | $62.78 | 24.6 s | |
| 11 | Firecrawl Search | 73 | 74 | 74 | 73 | $30.48 | $11.58 | $42.06 | 61.9 s | |
| 12 | DeepSeek Search (summary) | 69 | 75 | 63 | 70 | $8.47 | $20.19 | $28.66 | 22.7 s | +36 |
| — | Model only (no search) | 33 | 45 | 17 | 38 | — | $2.92 | $2.92 | 26.9 s | baseline |

— [Source](https://artificialanalysis.ai/agents/search-api) (table as rendered 2026-11-05; "Latest data: Oct 19, 2026")

- Page methodology notes: Index = equal-weighted mean of DeepSearchQA F1, BrowseComp accuracy and AA-Omniscience accuracy (0-100). DeepSearchQA = full eval split of 900 tasks, LLM-graded F1 over answer items; BrowseComp = hard 200-sample subset, exact-answer grading; AA-Omniscience = private set of 600 factual questions across 6 domains. Time per task = model time (output tokens / output speed) + measured search time; for OpenAI Web Search the search time is an upper bound. — [Source](https://artificialanalysis.ai/agents/search-api)
- The leaderboard page references no API/JSON endpoint (no `api.artificialanalysis.ai` string) and no GitHub repository; it links only to `/methodology/search-api`. — [Source](https://artificialanalysis.ai/agents/search-api)

**Methodology page (fetched 2026-11-05) [independent — Artificial Analysis]** — [AA Search API methodology](https://artificialanalysis.ai/methodology/search-api)
- Harness: **Stirrup**, AA's search-agent harness; the page links only to the docs site `stirrup.artificialanalysis.ai`, not a GitHub repo. — [Source](https://artificialanalysis.ai/methodology/search-api)
- Candidate model: GPT-5.6 Luna (medium), reasoning effort medium, max output 127,999 tokens; the only answer model. **Grader: also GPT-5.6 Luna (medium)** for all three benchmarks (same model as candidate — stated as a caveat). — [Source](https://artificialanalysis.ai/methodology/search-api)
- Task counts: DeepSearchQA 900 (full public eval split); AA-Omniscience 600 private (100 per domain x 6); BrowseComp 200 (subset of the 1,266-sample pool). Total 1,700 tasks per provider result. — [Source](https://artificialanalysis.ai/methodology/search-api)
- Agent setup: tools `web_search` (routed to provider under test) and `web_fetch` (text-only, 15 s timeout per page); 25-turn budget, unlimited tool calls within it; up to 10 results per search; no `finish` call by turn 25 scores zero. Other modes: `model_only` baseline; OpenAI Web Search = one Responses API call with `search_context_size=medium`, no turn budget. — [Source](https://artificialanalysis.ai/methodology/search-api)
- Cost: reported as total experiment cost split into candidate-model cost (input, cached, reasoning, output tokens; earlier-turn input priced at cache-hit rates) and Search API provider cost. OpenAI Web Search priced at $10 per 1,000 `web_search` calls with search content billed as input tokens. No explicit "per 1K tasks" formula on the page. — [Source](https://artificialanalysis.ai/methodology/search-api)
- Latency: model time per task = output tokens / end-to-end output speed; search time per task = average measured time in `web_search`; time per task = sum; time per search query also tracked. — [Source](https://artificialanalysis.ai/methodology/search-api)
- Error handling: recoverable errors (page timeouts, HTTP errors, fetching a non-returned URL) are returned to the model and kept; fatal provider errors (429, 5xx, timeouts) are retried until success so no published result contains one. — [Source](https://artificialanalysis.ai/methodology/search-api)
- Contamination: known benchmark URLs/datasets and canary strings are filtered from search results and fetched text; for OpenAI Web Search the domain filter is used. — [Source](https://artificialanalysis.ai/methodology/search-api)
- **Provider configurations listed (this is the 26-configuration / 14-provider roster):** Brave web (`result_filter=web`), Brave LLM context (`api=llm_context`); DeepSeek summary (`need_content=false`); Exa lite, Exa auto (`type=lite`/`auto`, dynamic highlights); Firecrawl (`scrape_format=none`); Keenable pro, Keenable realtime (`mode=`); Linkup flash (alpha), fast, standard (`depth=`); Nimble lite, standard (`search_depth=`, `full_content=false`); Octen highlights (highlights enabled, English); OpenAI Web Search medium; Parallel turbo, fast, basic, advanced (`mode=`); Perplexity low, medium, high (`search_context_size=`); Tavily basic (`search_depth=basic`); TinyFish web (`domain_type=web`); You.com snippets, You.com highlights (`safesearch=moderate`). All other settings at provider defaults. — [Source](https://artificialanalysis.ai/methodology/search-api)
- Run dates and update cadence: not stated on the methodology page. — [Source](https://artificialanalysis.ai/methodology/search-api)
- Stated caveats: grader = candidate model; a provider can be fast per call yet add total time if the model searches more; index reflects search uplift only because everything else is fixed; top score may not be best once cost/latency are considered; results are for one candidate model. — [Source](https://artificialanalysis.ai/methodology/search-api)

**Launch article, Aug 18, 2026: "Announcing the Artificial Analysis Search Index: Same Agent, Different Search" [independent — Artificial Analysis]** — [AA articles](https://artificialanalysis.ai/articles/search-api)
- Scope at launch: 11 provider results across 7 search providers plus model-only baseline (33; ~13.8 s/task; $2.92 per 1K tasks model cost). — [Source](https://artificialanalysis.ai/articles/search-api)

| Provider (Aug 18, 2026) | Index | Lift | DeepSearchQA F1 | BrowseComp | Omniscience | Search $/1K | Model $/1K | Time/task |
|---|---|---|---|---|---|---|---|---|
| Parallel Search (advanced) | 75 | 42 | 81 | 77 | 67 | $47.93 | $35.58 | 35.9 s |
| Exa Search (auto) | 74 | 41 | 78 | 74 | 70 | $65.57 | $61.58 | 26.2 s |
| Firecrawl Search | 73 | 40 | 74 | 74 | 73 | $30.48 | $44.94 | 55.0 s |
| Parallel Search (basic) | 73 | 40 | 79 | 73 | 68 | $45.14 | $69.69 | 20.4 s |
| Exa Search (fast) | 68 | 35 | 76 | 61 | 69 | $78.11 | $80.53 | 20.7 s |
| You.com Search | 68 | 35 | 63 | 74 | 66 | $68.93 | $58.28 | 33.7 s |
| Parallel Search (turbo) | 67 | 34 | 70 | 75 | 56 | $13.64 | $46.57 | 18.8 s |
| Keenable Search (pro) | 67 | 34 | 70 | 66 | 65 | $23.69 | $73.20 | 23.2 s |
| Keenable Search (realtime) | 67 | 34 | 70 | 64 | 66 | $26.87 | $63.67 | 15.1 s |
| Tavily Search (basic) | 66 | 33 | 74 | 59 | 64 | $126 | $66.58 | 36.3 s |
| Brave Search | 65 | 32 | 62 | 67 | 65 | $71.61 | $74.52 | 26.6 s |
| Model only | 33 | baseline | 45 | 17 | 38 | — | $2.92 | 13.8 s |

— [Source](https://artificialanalysis.ai/articles/search-api) (Aug 18, 2026)
- Article text: Parallel advanced total $0.084/task vs $0.11 for Parallel basic; Firecrawl $0.075/task; Exa fast $0.16 vs Exa auto $0.13; baseline $0.0029. Keenable realtime fastest search call at 0.34 s/query and lowest total time 15.1 s; Parallel turbo 0.51 s/query vs basic 1.03 s. — [Source](https://artificialanalysis.ai/articles/search-api)

**Journalist coverage, Aug 18, 2026 [journalist — The Decoder, Matthias Bastian]** — [The Decoder](https://the-decoder.com/new-benchmark-ranks-search-apis-for-ai-agents-on-quality-cost-and-speed/)
- Reports the same launch numbers (baseline 33; providers 65-75; Parallel 75, Exa 74, Firecrawl 73, Parallel basic 73, Parallel turbo 67); says Stirrup is described as open-source; notes "25 runs per task" (this appears to be the 25-turn budget misreported as runs); says methodology is public and other providers "can apply to join"; AA named Parallel, Firecrawl and Parallel turbo as best cost/performance mix. No criticisms raised. — [Source](https://the-decoder.com/new-benchmark-ranks-search-apis-for-ai-agents-on-quality-cost-and-speed/)

**Intermediate (September 2026) snapshot [practitioner, secondary — WebSearch summary of orcarouter.ai blog, not fetched]**
- Third-party blog posts dated Sept 2026 reported Perplexity Search (low) 77, Parallel Search (advanced) 75, Octen Search 77 with the fastest per-query latency. Treat as unverified. — [Source](https://www.orcarouter.ai/blog/octen-search-artificial-analysis-search-index)

**Cross-snapshot discrepancies inside AA (Aug 18 vs Oct 19, 2026)**
- Parallel advanced has identical sub-scores (81/77/67) and identical search cost ($47.93) in both snapshots, but model cost fell from $35.58 to $10.67 per 1K and time rose 35.9 s to 40.0 s; Firecrawl likewise 74/74/73 and $30.48 both times but model cost $44.94 -> $11.58 and time 55.0 s -> 61.9 s. The model-cost column is ~3-4x lower across the board in October (baseline unchanged at $2.92). Neither page explains this; plausible causes are a repricing of GPT-5.6 Luna or a change to cache-hit accounting (the methodology says earlier-turn input is priced at cache-hit rates). — [Aug table](https://artificialanalysis.ai/articles/search-api); [Oct table](https://artificialanalysis.ai/agents/search-api)
- Exa auto rose from 74 (78/74/70) in Aug to 80 (86/83/73) in Oct, but the Oct configuration is labelled "auto, dynamic highlights" — i.e., a configuration change, not a like-for-like re-run. — [Aug](https://artificialanalysis.ai/articles/search-api); [Oct](https://artificialanalysis.ai/agents/search-api)

### Inferences
- The 26 configurations in the methodology settings table enumerate exactly 14 providers: Brave, DeepSeek, Exa, Firecrawl, Keenable, Linkup, Nimble, Octen, OpenAI, Parallel, Perplexity, Tavily, TinyFish, You.com. **Valyu, Kagi and Mojeek are not on the AA board** as of the fetched methodology page.
- The hidden 13 rows in the default view are, by elimination: Brave web, Exa (one more variant if the two Exa rows shown exhaust lite/auto — otherwise none), Keenable pro, Keenable realtime, Linkup flash/fast/standard, Nimble lite, Parallel turbo/fast/basic, Perplexity low, Tavily basic, TinyFish web, You.com snippets. Their Oct 19 scores are unknown; the Aug 18 article gives last-known scores for Keenable (67/67), Tavily basic (66), Parallel turbo/basic (67/73) and Brave (65).
- The page shows no sign of a public JSON API for the Search Index; AA's model-level API (api.artificialanalysis.ai) was not referenced on either page.

### Gaps
- Full 26-row Oct 19 table (Tavily, Linkup, Keenable, TinyFish, Parallel turbo/fast/basic, Perplexity low, Brave web, Nimble lite, You.com snippets rows): hidden by a client-side "12 of 26 providers" filter; not retrievable in the two fetches available. Needs a browser session or the Stirrup results export.
- Whether AA exposes the Search Index via api.artificialanalysis.ai: no reference on the leaderboard or methodology page; not tested.
- Stirrup GitHub repository: only `stirrup.artificialanalysis.ai` docs link found; repo URL not confirmed.
- Exact run dates for each provider result and the update cadence: not stated.

---

## KQ2. Vals AI Web Search Index: methodology, runs, full tables, pairings, confidence statements

### Takeaway
Vals' Web Search Index (board dated **Oct 21, 2026**) pairs four frontier models with their native search and with Exa (and GPT-5.6 Sol additionally with Keenable) on 208 legal and 450 finance expert tasks; **GPT-5.6 Sol + Keenable leads at 49.08% ($8.84/task) with Claude Fable 5 + Exa at 48.45% ($3.48/task)**. Only the Oct 21 board exists on the page — I found no July 2026 run. Uncertainty is given as ± standard errors per category and mixed-effects p-values, not CIs on the headline scores.

### Cited Findings

**Launch blog, Oct 2, 2026, by Nikil Ravi [independent — Vals AI]** — [Vals blog](https://www.vals.ai/blogs/web-search-index)
- Private test set; evaluations under Zero Data Retention policies; search tool swapped while model and harness fixed; final answer of the whole agent session is scored, not per-query result lists. Domains: finance via FAB v2 (questions written by IB / private-equity analysts) and legal via the Legal Research Benchmark (written and graded by 15 licensed attorneys, avg ~15 years' experience); more domains planned. — [Source](https://www.vals.ai/blogs/web-search-index)
- A no-search run scored 2.9% (legal) and 7.4% (finance); agents with search reach 30-50% on both splits. — [Source](https://www.vals.ai/blogs/web-search-index)
- Names four partners: **Exa, Keenable, Parallel, Tavily** — but shows no scores for them (and the Oct 21 board contains only Exa and Keenable as external tools). — [Source](https://www.vals.ai/blogs/web-search-index)

**Live leaderboard "As of October 21, 2026" (fetched 2026-11-05) [independent — Vals AI]** — [Vals Web Search Index](https://www.vals.ai/benchmarks/web_search)
- Setup: compares native provider search with independent tools (Exa, Keenable); agent uses the tool as its only window onto the web; domain tools (SEC EDGAR, CourtListener) removed. Orchestrated through Vals' Valkyrie harness with model calls via model-library. Dataset: 208 legal tasks, 450 finance questions. Cost per task = model inference + search fee. — [Source](https://www.vals.ai/benchmarks/web_search)
- Grading: legal — expert rubric per task (1-22 items, mean 9.47), primary metric All-pass, single LLM judge GPT-5.4; finance — FAB v2 dealbreaker-gated Partial Credit, category-balanced across nine categories (any failed dealbreaker = 0% for that question), All-pass secondary, three-judge jury (GPT-5.4, Gemini-3.1-Pro, Claude Sonnet 4.6). — [Source](https://www.vals.ai/benchmarks/web_search)

| Rank | Model | Search tool | Score | Cost / task | Duration / test |
|---|---|---|---|---|---|
| 1 | GPT-5.6 Sol | Keenable | 49.08% | $8.84 | 6m35s |
| 2 | Claude Fable 5 | Exa | 48.45% | $3.48 | 5m52s |
| 3 | Claude Fable 5 | Native | 46.94% | $4.37 | 12m22s |
| 4 | GPT-5.6 Sol | Exa | 45.24% | $18.97 | 8m51s |
| 5 | GPT-5.6 Sol | Native | 43.58% | $0.95 | 5m29s |
| 6 | Gemini 3.5 Flash | Exa | 41.36% | $1.18 | 3m17s |
| 7 | Grok 4.5 | Exa | 38.75% | $0.58 | 100.93 s |
| 8 | Gemini 3.5 Flash | Native | 37.04% | $0.50 | 4m10s |
| 9 | Grok 4.5 | Native | 35.54% | $0.99 | 2m17s |

— [Source](https://www.vals.ai/benchmarks/web_search) (as of Oct 21, 2026)
- Text findings: GPT-5.6 Sol + Keenable most accurate (49.1%); Claude Fable 5 + Exa close behind (48.5%) at less than half the cost. In finance, external tools hold most of the Pareto frontier; in legal, native search holds all of it, led by Claude Fable 5 (49.0% legal). GPT-5.6 Sol + Exa is the cost outlier (~$18.97 overall, up to $28.28 on legal) and never on the frontier. Model cost dominates: for GPT-5.6 Sol + Keenable the search fee is $0.41 of the $8.84 mean; median cost $3.22 with tails ~$190 (finance) and ~$281 (legal). — [Source](https://www.vals.ai/benchmarks/web_search)
- Search calls per task (median): finance — Native 18, Exa 14, Exa (GPT-5.6 Sol) 49, Keenable (GPT-5.6 Sol) 58; legal — Native 16, Exa 12, Exa (GPT-5.6 Sol) 84, Keenable (GPT-5.6 Sol) 99.5; a few GPT-5.6 Sol runs exceed 1,000 Exa searches. — [Source](https://www.vals.ai/benchmarks/web_search)
- Finance accuracy by category (± SE), Native / Exa / Keenable: General Qualitative 57.7±3.1 / 59.5±3.0 / 65.8±6.1; General Quantitative 67.5±2.9 / 68.9±2.9 / 73.5±5.6; Market Analysis 36.0±3.4 / 54.1±3.5 / 58.2±7.0; Comparables 41.8±3.2 / 43.1±3.2 / 48.9±6.4; Precedents 23.2±3.0 / 29.0±3.2 / 27.5±6.4; Adjustments 36.0±3.4 / 44.0±3.5 / 54.4±6.9; Earnings Analysis 59.4±3.5 / 73.3±3.1 / 75.5±6.1; Disclosure Analysis 53.6±3.4 / 59.6±3.3 / 62.1±6.7; Financial Modeling 17.8±2.6 / 17.4±2.5 / 19.5±5.3. — [Source](https://www.vals.ai/benchmarks/web_search)
- Legal accuracy by question type (± SE), Native / Exa / Keenable: Statutory Interpretation 35.7±2.0 / 37.0±2.0 / 43.3±4.1; Application of Precedent 34.6±2.1 / 31.6±2.1 / 39.5±4.4; Doctrinal Test Identification 38.3±3.2 / 36.6±3.2 / 42.1±6.6; Regulatory Framework 48.5±3.9 / 54.1±4.0 / 58.5±7.8; Interaction of Multiple Regimes 32.4±3.9 / 31.7±3.9 / 35.1±8.0; Cross-Jurisdiction 32.5±5.2 / 31.6±5.3 / 42.9±11.1; Timeline/Doctrinal Evolution 36.9±5.3 / 34.5±5.2 / 38.1±10.9; Validity of Precedent 37.5±5.4 / 36.3±5.4 / 40.0±11.2; Resolving Conflicting Precedent 26.7±5.8 / 28.3±5.9 / 46.7±13.3; Consensus vs Disagreement 25.0±6.1 / 26.0±6.3 / 38.5±14.0. — [Source](https://www.vals.ai/benchmarks/web_search)
- **Confidence statements:** mixed-effects models with search tool as fixed effect (native = reference) and random intercept per task. Exa vs native: finance weighted score +6.51 points (SE 0.98, t = 6.62, p < 0.001); legal All-pass −0.02 log-odds (SE 0.13, z = −0.17, p = 0.86), i.e., no significant legal effect. No CIs on the headline leaderboard scores; the ±SE values per category are the only uncertainty shown. — [Source](https://www.vals.ai/benchmarks/web_search)
- Answer length / sources: legal 1,590 words (Exa) vs 1,380 (native); finance 790 vs 735; Exa cites 15-18% more distinct sources than native. Top-cited domain: sec.gov is 53.7% (native) / 57.6% (Exa) / 77.4% (Keenable+GPT-5.6 Sol) of finance citations; justia.com 25.9% / 19.2% / 28.7% of legal citations. — [Source](https://www.vals.ai/benchmarks/web_search)

### Inferences
- Vals and AA measure different things: AA fixes one model (GPT-5.6 Luna) and varies the search API; Vals varies both the model and the tool and includes the models' native search, so Vals' ranking is a model+tool ranking. Comparing Vals' Keenable #1 against AA's Keenable 67 (Aug) is not like-for-like.
- Keenable appears in only one Vals pairing (GPT-5.6 Sol) with wider SEs (±5-14 vs ±2-4 for Exa/native), implying a smaller Keenable sample; the Keenable lead is therefore less certain than the rank suggests.
- The four named "partners" (Exa, Keenable, Parallel, Tavily) suggests vendor participation in the index; whether partners pay is not stated.

### Gaps
- July 2026 run: not present on either Vals page; the blog is dated Oct 2, 2026 and the board Oct 21, 2026. I could not confirm a July run existed.
- Parallel and Tavily results: named as partners but absent from the Oct 21 board.
- Per-row finance vs legal split scores for the nine leaderboard rows: not tabulated (only the Claude Fable 5 legal 49.0% figure is given in text).
- No-search baseline on the board page: not reported (only the blog's 2.9% / 7.4% figures).
- Confidence intervals on headline scores: not provided.

---

## KQ3. OpenBenchmarks: operator, three boards, methodology, dates, ordering-bias caveat

### Takeaway
I could not locate any project called "OpenBenchmarks" that publishes search-API boards: `openbenchmarks.ai` returned HTTP 503 and two WebSearch queries surfaced no such site. The closest match is an "Agentic Search Index v0.1" (Firecrawl 82.9, Serper 80.9, with CIs, cost and p50/p95 latency) cited by a Keenable-generated report via `x402oracle.com/llms.txt`, operator unknown.

### Cited Findings
- `https://openbenchmarks.ai` returned HTTP 503 Service Unavailable on 2026-11-05 (fetch result; no content). — no source page retrievable.
- WebSearch for "OpenBenchmarks search API leaderboard ... ordering bias" and for "\"OpenBenchmarks\" web search API agents benchmark leaderboard 2026" returned no project of that name; results were Exa's own `exa-labs/benchmarks` repo, Perplexity's `search_evals`, `youdotcom-oss/web-search-agent-evals`, `openfunnel/gtm-bench` and IBM's Open Agent Leaderboard. — [exa-labs/benchmarks mirror](https://github.gg22.workers.dev/exa-labs/benchmarks); [perplexityai/search_evals mirror](https://gh.r-mj.com/perplexityai/search_evals); [youdotcom-oss/web-search-agent-evals](https://awesome.ecosyste.ms/projects/github.com%2Fyoudotcom-oss%2Fweb-search-agent-evals)
- A Keenable SELECT auto-generated report (searches run 21 Aug 2026) **[vendor-tool, secondary]** lists an "Agentic Search Index v0.1" (operator not stated, "appears third-party") with Firecrawl 82.9 top and Serper 80.9 runner-up, reporting confidence intervals, cost and p50/p95 latency; source given as `x402oracle.com/llms.txt`. — [Keenable SELECT report](https://select.keenable.ai/r/ai-web-search-api-benchmarks/OaFKKMHeqBfx3jQKy9nI-w)
- Same report's eight-suite roundup (wins = first place per suite): Firecrawl 2, Tavily 2, Parallel 1, Brave 1, Keiro 1, cloro 1; it labels vendor-authored results and says they should not outweigh independent controlled tests. — [Source](https://select.keenable.ai/r/ai-web-search-api-benchmarks/OaFKKMHeqBfx3jQKy9nI-w)

### Inferences
- Either "OpenBenchmarks" is a very new or renamed site (503 suggests the host exists but is down), or the brief's name is inexact and refers to the "Agentic Search Index v0.1" or another community board. The ordering-bias caveat the brief mentions could not be verified anywhere.

### Gaps
- Operator identity, the three boards' tables, methodology, dates and the ordering-bias caveat: all unverified — site unreachable and undiscoverable via search in this session. Recommend retrying `openbenchmarks.ai` later and fetching `x402oracle.com/llms.txt` directly.

---

## KQ4. LMArena / Arena.ai Search Arena 2026 leaderboard

### Takeaway
The Search Arena leaderboard now lives at `arena.ai/leaderboard/search` (lmarena.ai 301-redirects there) but returned HTTP 403 to this session on both locale paths; the only figures I could obtain are secondary: a Jan 29, 2026 snapshot (183,043 votes, 19 models, Google top at 1224) and a Sept 2026 third-party tracker putting Claude Opus 4.6 first at 1253 and GPT-5.5 at 1240.

### Cited Findings
- `https://lmarena.ai/leaderboard/search` -> 301 -> `https://arena.ai/leaderboard/search`; both `arena.ai/leaderboard/search` and `arena.ai/it/leaderboard/search` returned HTTP 403 on 2026-11-05. — [arena.ai](https://arena.ai/leaderboard/search)
- **[independent, secondary — WebSearch summary of the arena.ai page]** Official snapshot dated Jan 29, 2026: 183,043 votes, 19 models, Google holding the top rank at 1224. — [arena.ai (Italian locale)](https://arena.ai/it/leaderboard/search)
- **[practitioner, secondary]** Third-party tracker (Sept 2026): Claude Opus 4.6 (Anthropic) #1 on Arena Search Elo at 1253, GPT-5.5 at 1240. — [anotherwrapper.com](https://anotherwrapper.com/tools/llm-pricing/evals/arena-search-elo)
- **[practitioner, secondary]** benchmarklist.com reports a leading Search Arena score of 1252.82 across 50 ranked models, undated. — [benchmarklist](https://benchmarklist.com/arenas/lmarena_search_arena/)
- Arena release notes list claude-opus-4-7 added to the Search leaderboard (date not captured). — [releasebot](https://releasebot.io/updates/arena-ai); Arena blog "March 2026: Arena Updates across Product, Leaderboard Rankings & Research". — [arena.ai blog](https://arena.ai/blog/march-2026-arena-updates/)
- Search Arena GitHub repo exists at `lmarena/search-arena` (mirror seen in search). — [mirror](https://gh.r-mj.com/lmarena/search-arena)

### Inferences
- Search Arena ranks LLM+search *products/models* (Gemini, GPT, Claude, Perplexity Sonar etc.) by human preference votes, not raw search APIs; it is not directly comparable to AA/Vals/AIMultiple API boards. Perplexity did not appear in the secondary summaries I retrieved.

### Gaps
- Full 2026 table (rank, score, CI, votes, org, licence) and last-updated date: blocked by HTTP 403. Needs a browser session or the `lmarena/search-arena` repo's data export.

---

## KQ5. AIMultiple search-API benchmark (December 2025 snapshot, 8 APIs, confidence intervals)

### Takeaway
AIMultiple's "Agentic Search: Benchmark of 8 Search APIs for Agents" (data December 2025; page updated May 13/14, 2026) ranks **Brave 14.89 > Firecrawl 14.58 > Exa 14.39 > Parallel Pro 14.21 > Tavily 13.67 > Parallel Base 13.50 > Perplexity 12.96 > SerpAPI 12.28** on an LLM-judged Agent Score over 100 queries, with overlapping 95% bootstrap CIs making the top four statistically indistinguishable; Brave is also fastest (669 ms) and Parallel Pro slowest (13.6 s).

### Cited Findings [independent analyst — AIMultiple; authors Ekrem Sarı with Hazal Şimşek] — [AIMultiple](https://aimultiple.com/agentic-search)
- Dates: results are a single snapshot from December 2025; page "last updated May 13, 2026" (footer May 14, 2026); the May 13 update replaced Brave's pricing tiers. — [Source](https://aimultiple.com/agentic-search)
- APIs (8): Brave Search, Tavily, Exa, Firecrawl, SerpAPI, Perplexity, Parallel Search (Base), Parallel Search (Pro). — [Source](https://aimultiple.com/agentic-search)
- Method: 100 AI/LLM queries drawn from AIMultiple's top organic queries (Dec 2024-Jan 2025) in six categories (Research 24, Factual Verification 20, Technical Documentation 20, Real-time Events 10, Comparative 16, Tool Discovery 10); top 5 results per query per API (~4,000 results); default settings except result count; judge GPT-5.2 via OpenRouter at temperature 0 rating relevance (boolean), quality (1-5), noise (boolean), source type; ~10% (~400) manually checked. Agent Score = Mean Relevant x Quality. 95% bootstrap CIs from 10,000 resamples plus paired bootstrap difference tests. Run on a Contabo VPS (France), Ubuntu 24.04.3, Python 3.11+/asyncio/httpx, 3 retries with exponential backoff, 30 s timeout; Brave free tier limited to 1 req/s; run took ~3.5 h. — [Source](https://aimultiple.com/agentic-search)

| Rank | API | Mean Relevant /5 (95% CI) | Quality /5 (95% CI) | Agent Score (95% CI) | Latency (reported) |
|---|---|---|---|---|---|
| 1 | Brave Search | 4.28 (4.09-4.47) | 3.48 (3.37-3.60) | 14.89 (13.80-15.93) | 669 ms |
| 2 | Firecrawl | 4.30 (4.08-4.53) | 3.39 (3.23-3.56) | 14.58 (13.12-15.98) | 1,335 ms |
| 3 | Exa | 4.32 (4.13-4.51) | 3.33 (3.21-3.46) | 14.39 (13.25-15.50) | ~1.2 s |
| 4 | Parallel Search (Pro) | 4.32 (4.13-4.52) | 3.29 (3.17-3.41) | 14.21 (13.07-15.47) | 13.6 s |
| 5 | Tavily | 4.18 (3.99-4.37) | 3.27 (3.14-3.40) | 13.67 (12.62-14.76) | 998 ms |
| 6 | Parallel Search (Base) | 4.18 (3.96-4.41) | 3.23 (3.11-3.35) | 13.50 (12.38-14.66) | ~2.9 s |
| 7 | Perplexity | 4.00 (3.76-4.24) | 3.24 (3.10-3.39) | 12.96 (11.77-14.22) | 11+ s |
| 8 | SerpAPI | 3.58 (3.36-3.81) | 3.43 (3.29-3.57) | 12.28 (11.19-13.41) | 2.4 s |

— [Source](https://aimultiple.com/agentic-search) (Dec 2025 data)
- Latency spread ~20x; a five-call agent workflow waits ~3 s (Brave) to ~68 s (Parallel Pro). — [Source](https://aimultiple.com/agentic-search)
- Pricing as listed (vendor list prices quoted by AIMultiple): Brave $5/1K requests (Search plan, $5 free monthly credit; Answers $4/1K + $5/M tokens); Exa $5-$15 per 1K requests/pages PAYG, Websets from $49/mo; Tavily $0.008/credit PAYG, free 1,000 credits/mo, Project $30/mo for 4,000 credits; SerpAPI Developer $75/5,000, Production $150/15,000, Big Data $275/30,000 (≈ $15 / $10 / $9.17 per 1K — my arithmetic); Perplexity Search API $5/1K requests, no token cost; Firecrawl page-based plans in EUR (free 500 pages; Hobby €14/mo 3,000; Standard €74/mo 100,000; Growth €298/mo 500,000); Parallel: no pricing given. — [Source](https://aimultiple.com/agentic-search)
- Conclusions: top four statistically indistinguishable; Brave the only clear winner over Tavily (~1 point; p-values not shown and CIs overlap); recommends Brave for production agents, Tavily or Brave for prototyping; Perplexity's latency unsuited to interactive agents. Limitations: AI/LLM-topic queries only; single Dec 2025 snapshot; LLM-judge bias in the ~90% not manually verified. — [Source](https://aimultiple.com/agentic-search)

### Inferences
- AIMultiple measures SERP-level relevance of the top-5 results (no agent loop), which explains why Brave tops it while sitting last of 11 on AA's Aug 2026 agentic index: AA scores end-task success after multi-turn search+fetch.
- The AIMultiple score and CI widths (~±1 point on a ~14 scale) mean only the Brave-vs-SerpAPI and Brave-vs-Perplexity gaps are clearly outside overlap.

### Gaps
- Paired-test p-values behind the "Brave beats Tavily" claim: not published.
- Parallel pricing in the benchmark: not given.

---

## KQ6. Keenable NEEDLE live board: standings with p50, p95 and cost

### Takeaway
NEEDLE (Keenable, blog Aug 27, 2026, authors Ilya Gusev, Matthias Petri, Andrey Styskin) is a vendor-run, continuously refreshed benchmark across five verticals; the live board at needle.keenable.ai could not be reached from this session (host not in the allowed network list), so the only standings I have are secondary latency figures — **Keenable-realtime 193 ms p50 / 284 ms p95, Exa 1,876 / 2,955 ms, Bing 2,767 / 9,381 ms** — from an undated window, with the obvious conflict of interest that Keenable competes in its own benchmark.

### Cited Findings
- **[vendor — Keenable; via Plushcap mirror/summary]** Blog "NEEDLE: The benchmark your search engine can't memorize", published Aug 27, 2026, authors Ilya Gusev, Matthias Petri, Andrey Styskin; ~2,005 words; 33 Hacker News points; source URL `keenable.ai/blog/needle-the-benchmark-your-search-engine-can-t-memorize`. Positioned as a "continuously refreshed, open-source benchmark" for web search engines used by AI agents, designed to avoid leakage, memorization and overfitting. Verticals: breaking news, finance, scholarly research, rare long-tail entities, legal materials. Data from live public sources and agent search logs; daily or hourly updates; code, tasks and metrics stated to be public. Engines named in the summary: Keenable, Google, Bing, Brave, Tavily, Parallel, Exa, plus an "upper bound" of the best results collectively returned by all engines. — [Plushcap mirror](https://www.plushcap.com/content/keenable/blog/keenable-needle-the-benchmark-your-search-engine-cant-memorize)
- **[vendor, secondary — WebSearch summaries of MarkTechPost/aiunderstanding and zeli.app coverage]** NEEDLE covers five verticals, 15 search APIs and one protocol; queries regenerate hourly for news and daily for the other four verticals; calls are sequential (no concurrent load on any engine); judging uses only the engine's own ranking, titles and snippets — pages are never fetched and results never re-ranked. — [aiunderstanding.org](https://aiunderstanding.org/news/marktechpost-reports-keenable-ai-open-sources-needle-a-live-benchmark-for-search-a); [zeli.app (German)](https://zeli.app/de/story/49466250)
- **[vendor, secondary]** Latency from one measurement window (dates not given): Keenable-realtime 193 ms p50 / 284 ms p95; Exa 1,876 / 2,955 ms; Bing 2,767 / 9,381 ms. — [aiunderstanding.org](https://aiunderstanding.org/news/marktechpost-reports-keenable-ai-open-sources-needle-a-live-benchmark-for-search-a)
- **[vendor]** Keenable marketing separately claims sub-250 ms p95 latency in US East (different setup from the NEEDLE window). — [plushcap Keenable summaries](https://www.plushcap.com/companies/keenable/blog/summaries/2026/08)
- Conflict of interest: a reader comment on the German summary raises the concern that Keenable sits at the top of its own benchmark; the Plushcap summary itself states no caveat. — [zeli.app](https://zeli.app/de/story/49466250)
- `https://needle.keenable.ai` failed DNS resolution from this session (host outside allowed network domains) on 2026-11-05.

### Inferences
- NEEDLE's "snippet-only, never fetch" judging means it measures SERP quality (like AIMultiple), not agentic end-task success (like AA/Vals), so Keenable's NEEDLE lead and AA's mid-table 67 (Aug) for Keenable are not contradictory.
- Independent corroboration of NEEDLE standings is absent: all numbers trace back to Keenable.

### Gaps
- Current standings for all 15 engines with accuracy, p50, p95 and cost: live board unreachable (network allowlist); GitHub repo URL not confirmed. The session needs `needle.keenable.ai` (and probably `keenable.ai`, `github.com/keenable`) allowed.
- Dates of the latency window quoted above: not given in the secondary coverage.

---

## KQ7. 2026 academic papers comparing commercial search APIs as agent tools

### Takeaway
No 2026 arXiv paper was found that benchmarks Exa, Tavily, Brave, Perplexity and Serper head-to-head as agent tools; the closest are **LiveNewsBench (arXiv:2602.13543, Feb 14, 2026)**, which evaluates "LLM-based web search APIs" on freshly generated news questions with a public leaderboard at livenewsbench.com, and SGR-Bench (arXiv:2605.22219, May 2026), which includes three commercial search-agent products.

### Cited Findings
- **[academic/independent]** LiveNewsBench: Evaluating LLM Web Search Capabilities with Freshly Curated News — Yunfan Zhang, Kathleen McKeown, Smaranda Muresan; arXiv:2602.13543 v1 submitted Feb 14, 2026 (earlier version on OpenReview as an ICLR 2026 submission, Sept 2025). Auto-generates QA pairs from recent news requiring multi-hop search, page visits and reasoning; human-verified test subset; evaluates "commercial and open-weight LLMs as well as LLM-based web search APIs"; leaderboard at livenewsbench.com. The abstract page names no products or scores. — [arXiv 2602.13543](https://arxiv.org/abs/2602.13543)
- **[secondary — WebSearch summary]** Best-performing system on LiveNewsBench reached only 19.30% exact match. — [fugumt mirror](https://fugumt.com/fugumt/paper_check/2602.13543v1_enmode)
- **[academic, secondary — WebSearch summary]** SGR-Bench (arXiv:2605.22219, May 2026) evaluates eight CLI-based agentic LLM systems and three commercial search-agent products; strongest reaches 66.18% item-level F1 on a specialised retrieval task; commercial APIs not named in the summary. — [arXiv 2605.22219](https://arxiv.org/html/2605.22219)
- **[vendor]** Parallel.ai published multiple 2026 BrowseComp-based comparisons (six-API run July 10-12, 2026; accuracies ~19%-58%; Parallel Turbo 51%, Brave 38.3%, Exa Instant 33.7%, Tavily 19.3% in one report) — vendor-run, listed here only because the search surfaced them as the most-cited "comparison" content. — [parallel.ai](https://parallel.ai/articles/most-powerful-search-api-for-ai)

### Inferences
- Academic work in 2026 benchmarks search *agents/products*, not raw search APIs under a fixed agent; AA's Stirrup design (same agent, swap API) remains the only independent, controlled API-level comparison found, with Vals a close second.

### Gaps
- Full LiveNewsBench leaderboard (which search APIs, scores): not fetched (arXiv abstract only; livenewsbench.com not fetched).
- SGR-Bench details: not fetched.
- A peer-reviewed Exa/Tavily/Brave/Perplexity/Serper comparison: none found.

---

## Cross-board disagreements (explicit)

- **Who is #1:** AA Oct 19, 2026 — Exa auto (dynamic highlights) and Perplexity medium tie at 80 [independent]; AA Aug 18, 2026 — Parallel advanced 75 [independent]; Vals Oct 21, 2026 — GPT-5.6 Sol + Keenable 49.08% [independent]; AIMultiple Dec 2025 — Brave 14.89 [independent analyst], top four indistinguishable; "Agentic Search Index v0.1" — Firecrawl 82.9 [operator unknown, secondary]; NEEDLE — Keenable fastest/top [vendor, secondary]. Sources: [AA board](https://artificialanalysis.ai/agents/search-api), [AA Aug article](https://artificialanalysis.ai/articles/search-api), [Vals](https://www.vals.ai/benchmarks/web_search), [AIMultiple](https://aimultiple.com/agentic-search), [Keenable SELECT](https://select.keenable.ai/r/ai-web-search-api-benchmarks/OaFKKMHeqBfx3jQKy9nI-w).
- **Brave:** last of 11 (65) on AA Aug 2026 agentic index vs first of 8 on AIMultiple's SERP-relevance test; by Oct 2026 AA's Brave "LLM context" endpoint scores 75. — [AA Aug](https://artificialanalysis.ai/articles/search-api); [AIMultiple](https://aimultiple.com/agentic-search); [AA Oct](https://artificialanalysis.ai/agents/search-api)
- **Perplexity:** 7th of 8 on AIMultiple with 11+ s latency vs tied #1 (80) on AA Oct 2026 at 31.4 s per full task. — [AIMultiple](https://aimultiple.com/agentic-search); [AA Oct](https://artificialanalysis.ai/agents/search-api)
- **Tavily:** 10th of 11 (66) on AA Aug 2026 with the highest search cost ($126/1K tasks); 5th of 8 on AIMultiple; a named Vals partner but absent from the Vals board. — [AA Aug](https://artificialanalysis.ai/articles/search-api); [AIMultiple](https://aimultiple.com/agentic-search); [Vals blog](https://www.vals.ai/blogs/web-search-index)
- **Keenable:** mid-table 67 on AA Aug 2026 (fastest search call, 0.34 s) vs #1 on Vals Oct 2026 (paired with GPT-5.6 Sol, 58-99.5 median searches per task) vs top of its own NEEDLE board. — [AA Aug](https://artificialanalysis.ai/articles/search-api); [Vals](https://www.vals.ai/benchmarks/web_search); [NEEDLE coverage](https://aiunderstanding.org/news/marktechpost-reports-keenable-ai-open-sources-needle-a-live-benchmark-for-search-a)
- **Exa:** 74 -> 80 within AA between Aug and Oct 2026 reflects a configuration change (dynamic highlights), not necessarily a like-for-like improvement. — [AA Aug](https://artificialanalysis.ai/articles/search-api); [AA Oct](https://artificialanalysis.ai/agents/search-api)
- **Within AA:** model-cost column is ~3-4x lower in the Oct 19 snapshot than in the Aug 18 article for identical sub-scores (e.g., Parallel advanced $35.58 -> $10.67 per 1K); unexplained on either page. — [AA Aug](https://artificialanalysis.ai/articles/search-api); [AA Oct](https://artificialanalysis.ai/agents/search-api)

## Verification (wave 2, topic independent_boards, 2026-11-05)

| claim | verdict | what the source says | URL |
|---|---|---|---|
| 1. AA Search Index (Oct 19, 2026): Exa auto & Perplexity medium tie at 80; Exa auto $53.17 search + $10.60 model per 1K tasks at 36.9 s/task; Octen highlights 77 at $9.07 + $14.50; baseline 33; 26 products / 14 providers | CORRECTED | Page stamp "Latest data: Oct 19, 2026"; "26 Search API products across 14 providers"; Exa auto (dynamic highlights) 80, $53.17 search, $10.60 model, **36.5 s/task** (not 36.9); Perplexity medium 80 ($62.30 + $8.04, 30.9 s); Octen highlights 77, $9.07 + $14.50, 15.5 s; model only 33 ($2.92, 26.2 s). Only the Exa time differs. | https://artificialanalysis.ai/agents/search-api |
| 2. AA methodology: Stirrup; candidate & grader GPT-5.6 Luna (medium); 900 DeepSearchQA + 600 Omniscience + 200 BrowseComp; 25 turns; 10 results/search; 15 s web_fetch timeout; 26 configs over 14 providers, no Valyu/Kagi/Mojeek | CONFIRMED | Stirrup harness; both candidate and grader GPT-5.6 Luna (medium); 900 / 600 / 200 tasks; 25-turn budget; up to 10 results per search; 15-second per-page timeout for the text-extraction (fetch) layer; 26 configurations across Brave, DeepSeek, Exa, Firecrawl, Keenable, Linkup, Nimble, Octen, OpenAI, Parallel, Perplexity, Tavily, TinyFish, You.com (14); Valyu, Kagi, Mojeek absent. | https://artificialanalysis.ai/methodology/search-api |
| 3. AA launch table Aug 18, 2026: Parallel advanced 75, Exa auto 74, Firecrawl 73, Parallel basic 73, Exa fast 68, You.com 68, Parallel turbo 67, Keenable pro 67, Keenable realtime 67 (0.34 s/query, 15.1 s/task), Tavily basic 66 ($126/1K search), Brave 65 | CONFIRMED | Article "Announcing the Artificial Analysis Search Index: Same Agent, Different Search", Aug 18, 2026; all listed scores match; Keenable realtime 0.34 s/query and 15.1 s/task; Tavily basic $126 search per 1K tasks; Brave 65; baseline 33. | https://artificialanalysis.ai/articles/search-api |
| 4. Vals Web Search Index (Oct 21, 2026): GPT-5.6 Sol+Keenable 49.08% $8.84; Claude Fable 5+Exa 48.45% $3.48; Fable 5 native 46.94%; GPT-5.6 Sol+Exa 45.24% $18.97; 208 legal / 450 finance; Exa vs native +6.51 finance (t=6.62, p<0.001), -0.02 log-odds legal (p=0.86) | CONFIRMED | "Updated 10/21/2026"; rows and costs match exactly (native Fable 5 at $4.37); 208 legal tasks, 450 finance questions; finance +6.51 (SE 0.98, t=6.62, p<0.001); legal -0.02 log-odds (SE 0.13, z=-0.17, p=0.86). | https://www.vals.ai/benchmarks/web_search |
| 5. AIMultiple Agentic Search (Dec 2025 data, 100 queries, GPT-5.2 judge, 10,000-resample bootstrap CIs): Brave 14.89 (13.80-15.93), Firecrawl 14.58, Exa 14.39, Parallel Pro 14.21, Tavily 13.67, Parallel Base 13.50, Perplexity 12.96, SerpAPI 12.28; Brave 669 ms, Parallel Pro 13.6 s | CONFIRMED | Page (updated May 13, 2026) calls data a "December 2025 snapshot"; 100 queries; GPT-5.2 judge via OpenRouter, temp 0; 10,000 bootstrap resamples, 95% CI; all eight scores and the Brave CI match; Brave 669 ms, Parallel Pro 13.6 s. | https://aimultiple.com/agentic-search |
