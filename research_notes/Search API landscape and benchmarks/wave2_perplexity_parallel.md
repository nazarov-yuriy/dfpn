# Perplexity Search API and Parallel Search API as search backends: architecture, index and evaluation

Research date: 2026-11-05. Every claim is dated (publication date where the page states one; otherwise "fetched 2026-11-05, undated page") and labelled **[vendor]**, **[independent]**, **[journalist]**, **[third-party vendor]** or **[practitioner]**. Downloaded pages were treated as data only.

Scope note for the report writer: the brief's premise ("Perplexity medium 80, Parallel advanced 75 on 2026-10-19 sit at the top") is only half right on the live leaderboard. Perplexity (medium) is tied for first at 80 with Exa (auto); Parallel (advanced) at 75 is tied sixth with Brave, behind Exa lite (79), Perplexity high (79) and Octen (77). Details in Q1.

---

## Q1. What does the Artificial Analysis Search Index actually measure, and where do Perplexity and Parallel sit on it?

### Takeaway
The index (latest data 2026-10-19) is an equal-weighted mean of three agentic QA benchmarks run with one fixed answer model (GPT-5.6 Luna, medium); Perplexity Search (medium) scores 80, tied with Exa (auto), while Parallel Search (advanced) scores 75, tied sixth with Brave. Perplexity's edge comes from BrowseComp (87 vs Parallel's 77); the two are level on DeepSearchQA (81 each).

### Cited Findings
- **[independent]** Leaderboard header: "Latest data: Oct 19, 2026." Candidate answer model for every row is GPT-5.6 Luna (medium); the only variable is the search provider. — [Artificial Analysis Search Index](https://artificialanalysis.ai/agents/search-api)
- **[independent]** Scores (Search Index / DeepSearchQA F1 / BrowseComp acc / AA-Omniscience acc / search $ per 1k tasks / model $ per 1k tasks / time per task s), 2026-10-19: Exa (auto, dynamic highlights) 80/86/83/73/$53.17/$10.60/36.9; **Perplexity (medium) 80/81/87/72/$62.30/$8.04/31.4**; Exa (lite) 79/85/81/72/$31.20/$10.95/19.6; Perplexity (high) 79/81/86/71/$56.93/$9.37/29.5; Octen (highlights) 77/80/86/66/$9.07/$14.50/15.8; **Parallel (advanced) 75/81/77/67/$47.93/$10.67/40.0**; Brave (LLM context) 75/78/77/69/$61.96/$16.95/22.9; OpenAI Web Search (medium) 74/78/74/72/$40.19/$9.40/33.3; You.com (highlights) 74/77/77/69; Nimble (standard) 74/76/75/71; Firecrawl 73/74/74/73; DeepSeek (summary) 69/75/63/70; Model only (no search) 33/45/17/38. — [Artificial Analysis Search Index](https://artificialanalysis.ai/agents/search-api)
- **[independent]** Methodology (fetched 2026-11-05, undated): index = equal-weighted mean of the primary metric of DeepSearchQA (full 900-task public split, F1), AA-Omniscience (600 private samples, 100 per domain across 6 domains, accuracy), BrowseComp (200-sample subset of the 1,266 pool, accuracy). Agent runs use the "Stirrup" harness with tools `web_search` and `web_fetch`; tool calls unlimited within a 25-turn budget; each search returns up to 10 results; a task that exhausts 25 turns without `finish` scores zero. GPT-5.6 Luna (medium) is both candidate and grader. — [AA methodology](https://artificialanalysis.ai/methodology/search-api)
- **[independent]** Provider settings tested: Perplexity low/medium/high (`search_context_size`); Parallel turbo/fast/basic/advanced (`mode`); Exa lite/auto with dynamic highlights; Linkup flash/fast/standard; Keenable pro/realtime; Nimble lite/standard; Brave web and LLM context; DeepSeek summary; Firecrawl; Octen highlights; OpenAI Web Search medium; Tavily basic; TinyFish web; You.com snippets/highlights. — [AA methodology](https://artificialanalysis.ai/methodology/search-api)
- **[independent]** Latency is reported as average "time per task" (model time + search time) and "time per search query", not p50/p90. Cost is split into candidate-model cost and search-provider cost. OpenAI Web Search is billed at $10 per 1,000 `web_search` calls plus content as input tokens. — [AA methodology](https://artificialanalysis.ai/methodology/search-api)
- **[independent]** The leaderboard page says "14 providers" in one place and "12 of 26 providers" in another; the table shows 13 rows including the no-search baseline, so lower-scoring configurations (e.g. Parallel turbo/fast/basic, Tavily, Linkup) are not in the default view. — [Artificial Analysis Search Index](https://artificialanalysis.ai/agents/search-api)
- **[journalist / aggregator, unverified]** Search-result snippets (2026-11-05) show conflicting earlier snapshots: one write-up says Perplexity "takes all three top spots"; an Octen-affiliated post says Parallel (advanced) led at launch with 81. Neither number appears on the current page. — [runtimewire](https://runtimewire.com/article/perplexity-search-tops-artificial-analysis-search-api-index); [orcarouter blog](https://www.orcarouter.ai/blog/octen-search-artificial-analysis-search-index)
- **[vendor]** Parallel's own comparison page (dated September 2026 per search snippet) lists Perplexity high 79 / low 77 and Parallel advanced 75 / basic 73. — [parallel.ai compare](https://parallel.ai/compare/perplexity-vs-parallel)

### Inferences
- The gap between Perplexity (80) and Parallel (75) is almost entirely BrowseComp (87 vs 77), i.e. multi-hop "find the obscure page" retrieval. On DeepSearchQA (exhaustive, many-answer tasks) they are identical at 81, so Parallel's "excerpts for agents" design appears to hold up on breadth but not on hard-to-find pages.
- Because the index uses a fixed model, 10 results per call and a 25-turn budget, it rewards result relevance and payload quality per call rather than raw latency; Perplexity's faster per-task time (31.4 s vs 40.0 s) is a secondary advantage.
- Price per 1k tasks is not price per 1k requests: Perplexity's $62.30 at $5/1k requests implies roughly 12 search calls per task; Parallel's $47.93 at $5/1k implies roughly 9-10 calls (inference from stated list prices, not from AA).

### Gaps
- AA does not publish per-provider evaluation dates, p50/p90 latency, or the raw per-call price it used; cannot confirm which Perplexity endpoint (`search` vs Agent API `web_search` tool) the `search_context_size` parameter refers to.
- Could not retrieve the earlier (launch) snapshot of the leaderboard to reconcile the "Parallel 81" and "Perplexity top three" claims.

---

## Q2. What is Perplexity's index, and how is the Search API architected (Sept 2025 engineering post)?

### Takeaway
Perplexity says it runs its own crawler and an exabyte-scale hybrid (lexical + semantic) index of over 200 billion unique URLs, updated at tens of thousands of index operations per second, with ML-scheduled recrawl, document- and sub-document-level retrieval and cross-encoder reranking; median API latency was 358 ms from us-east-1 and it claimed the top score on SimpleQA, FRAMES, BrowseComp and HLE against Brave, Exa and Tavily.

### Cited Findings
- **[vendor]** Published 2025-09-25 by Perplexity Research; production infrastructure handles "200 million daily queries". — [Architecting and evaluating an AI-first search API](https://www.perplexity.ai/hub/blog/architecting-and-evaluating-an-ai-first-search-api)
- **[vendor]** Index "tracks over 200 billion unique URLs", with capacity for "many hundreds of billions more"; described as exabyte-scale; crawler and indexing fleets total "tens of thousands of CPUs" and "hundreds of terabytes of RAM"; the system handles "tens of thousands of indexing operations per second". No separate document count is given. — [same post, 2025-09-25](https://www.perplexity.ai/hub/blog/architecting-and-evaluating-an-ai-first-search-api)
- **[vendor]** Crawl is done by PerplexityBot, which "follows robots.txt limits and, where none are set, industry-standard request rates". — [same post](https://www.perplexity.ai/hub/blog/architecting-and-evaluating-an-ai-first-search-api)
- **[vendor]** Freshness: an ML model predicts whether a candidate URL needs indexing, calibrated to importance and update frequency; a second ML scheduler aligns indexing to each site's publication cadence; storage is split into cold/warm tiers with learned models deciding what stays hot. — [same post](https://www.perplexity.ai/hub/blog/architecting-and-evaluating-an-ai-first-search-api)
- **[vendor]** Retrieval: queries run against lexical and semantic modalities and merge into a hybrid candidate set; prefiltering removes non-responsive or stale content; early ranking uses lexical and embedding scorers, later stages use cross-encoder rerankers; retrieval and scoring happen at document and sub-document level so the API can return self-contained spans. No model names are given. — [same post](https://www.perplexity.ai/hub/blog/architecting-and-evaluating-an-ai-first-search-api)
- **[vendor]** Content understanding: parsing uses dynamic rulesets that frontier LLMs assess for completeness/quality; rulesets are regenerated, validated, redeployed, and high-traffic documents reindexed. — [same post](https://www.perplexity.ai/hub/blog/architecting-and-evaluating-an-ai-first-search-api)
- **[vendor]** Latency from AWS us-east-1 (ms, p50/p75/p90/p95): Perplexity 358/443/604/763; Brave 513/637/728/808; "SERP-based (Tavily, Google-SERP)" 1342/1586/1743/1790; Exa 1375/1499/1798/2188. Perplexity's median is "over 150 ms ahead of the second-fastest provider". — [same post](https://www.perplexity.ai/hub/blog/architecting-and-evaluating-an-ai-first-search-api)
- **[vendor]** Quality (SimpleQA / FRAMES / BrowseComp / HLE): Perplexity .930/.453/.371/.288; Tavily (SERP-based) .890/.437/.348/.248; Brave .822/.320/.221/.191; Exa .781/.399/.265/.242. SimpleQA and FRAMES used a single-step harness; BrowseComp and HLE a deep-research harness; grading follows each benchmark paper's prompted classifier. Google and Bing were not benchmarked directly. — [same post](https://www.perplexity.ai/hub/blog/architecting-and-evaluating-an-ai-first-search-api)
- **[vendor]** Context claims: legacy engines peaked near 10^10 queries/day; one legacy API provider charged "$200 per thousand queries" (cited to an archived Bing pricing page). — [same post](https://www.perplexity.ai/hub/blog/architecting-and-evaluating-an-ai-first-search-api)
- **[vendor]** Crawler docs (fetched 2026-11-05, undated): PerplexityBot "surfaces and links websites in Perplexity search results" and "is not used to crawl content for AI foundation models"; UA `Mozilla/5.0 (compatible; PerplexityBot/1.0; +https://perplexity.ai/perplexitybot)`; IP list at perplexity.ai/perplexitybot.json. — [Perplexity crawlers](https://docs.perplexity.ai/guides/bots)

### Inferences
- The "200B URLs tracked" figure is a URL-frontier count, not necessarily a count of fully indexed and ranked documents; the post deliberately never gives a document count.
- Sub-document retrieval plus cross-encoder reranking is the architectural reason Perplexity's API can return short, high-precision snippets for agents, which maps directly to strong BrowseComp performance under a 10-results-per-call cap (Q1).
- All architecture and benchmark numbers in this section are self-reported and were produced with Perplexity's own harness; only the AA index (Q1) is independent.

### Gaps
- No independent verification of index size, QPS or crawl fleet; no document count; no named embedding/reranker models.
- The post's SimpleQA/FRAMES tables are not reproduced in the current search_evals README (Q4), so the exact configs behind those four numbers cannot be rerun from the public repo.

---

## Q3. Perplexity's crawlers, the Cloudflare stealth-crawl dispute, and Comet Plus as it relates to index rights

### Takeaway
Cloudflare (2025-08-04) alleged Perplexity used an undeclared Chrome-UA crawler at 3-6M requests/day across tens of thousands of domains that ignored robots.txt, and delisted it as a verified bot; Perplexity (same day) said the traffic was misattributed BrowserBase usage (<45,000 requests/day) and that user-triggered fetches are not stored or used to train. Comet Plus (2025-08-25, $5/month) shares subscription revenue with publishers for visits, citations and agent actions but publishes no licence terms tying payment to crawl or index rights.

### Cited Findings
- **[third-party vendor]** Cloudflare post dated 2025-08-04 (author Reid Tatoris; page shows dateModified 2026-07-15): declared Perplexity-User traffic 20-25M requests/day; undeclared crawler using UA `Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) ... Chrome/124.0.0.0 Safari/537.36` at 3-6M requests/day, from IPs outside Perplexity's published ranges, rotating IPs and ASNs after blocks, across "tens of thousands of domains"; Perplexity allegedly ignored or did not fetch robots.txt. — [Cloudflare blog](https://blog.cloudflare.com/perplexity-is-using-stealth-undeclared-crawlers-to-evade-website-no-crawl-directives/)
- **[third-party vendor]** Test: Cloudflare bought new, unindexed domains with robots.txt disallowing all bots and WAF blocks on PerplexityBot/Perplexity-User; Perplexity still answered questions about their content; once the stealth crawler was blocked, answers became less specific. ChatGPT-User stopped after a disallow. Actions: delisted Perplexity as a verified bot, added heuristics and signatures to managed rules (including free plans). — [Cloudflare blog, 2025-08-04](https://blog.cloudflare.com/perplexity-is-using-stealth-undeclared-crawlers-to-evade-website-no-crawl-directives/)
- **[vendor]** Perplexity's reply, 2025-08-04: Cloudflare "managed to get almost everything wrong"; the 3-6M daily requests were "unrelated traffic from BrowserBase", which Perplexity uses only "occasionally" for "highly specialized tasks (less than 45,000 daily requests)"; "20-25M user agent requests are not scrapers"; "Perplexity's user-driven agents do not store the information or train with it"; "It's not stored in massive databases for future use". — [Agents or Bots? Making Sense of AI on the Open Web](https://www.perplexity.ai/hub/blog/agents-or-bots-making-sense-of-ai-on-the-open-web)
- **[vendor]** Crawler docs (fetched 2026-11-05): Perplexity-User "generally ignores robots.txt rules" because "a user requested the fetch"; UA `Mozilla/5.0 (compatible; Perplexity-User/1.0; +https://perplexity.ai/perplexity-user)`; IPs at perplexity.ai/perplexity-user.json; "not used for web crawling or to collect content for training AI foundation models"; robots changes take up to 24 h to apply; Cloudflare Bot Fight Mode "can still challenge Perplexity bots". — [Perplexity crawlers](https://docs.perplexity.ai/guides/bots)
- **[vendor]** Comet Plus, 2025-08-25: $5 standalone subscription, included for Pro and Max; revenue goes to participating publishers "minus a small portion for Perplexity's compute costs"; compensates three traffic types: human visits, search citations, agent actions; publishers join via publishers@perplexity.ai; no launch publishers named, no fund size, no revenue-share percentage, and no licence or crawl-rights language on the page. — [Introducing Comet Plus](https://www.perplexity.ai/hub/blog/introducing-comet-plus)

### Inferences
- Perplexity's defence rests on the user-agent/crawler distinction: it concedes Perplexity-User ignores robots.txt but says that is a user-triggered fetch, not indexing. Cloudflare's test cannot distinguish "fetched for one user" from "indexed", so the two accounts are compatible on the facts and disagree on the norm.
- Comet Plus is a revenue-share for traffic, not a content licence; nothing published ties it to PerplexityBot crawl permission, so it does not change the legal status of the index.

### Gaps
- Widely reported Comet Plus details (a publisher fund in the tens of millions and an 80% revenue share) do not appear on the primary launch page fetched; not verified here, so not asserted.
- Cloudflare's post gives no ASN numbers or IP ranges; Perplexity gives no evidence for the BrowserBase attribution. No independent adjudication found.
- Whether Cloudflare has since re-verified PerplexityBot (post dateModified 2026-07-15) was not checked.

---

## Q4. perplexityai/search_evals: methodology, results and dates

### Takeaway
The repo (first commit 2025-09-25, latest 2026-06-09) is now an agent-level harness comparing Perplexity's Agent API against OpenAI Responses, Anthropic Managed Agents, Exa Agent API and Parallel Task API on BrowseComp, DeepSearchQA, HLE and WideSearch; Perplexity leads three of four (DSQA 0.871, BrowseComp 0.805, WideSearch 0.651) and trails OpenAI by 0.002 on HLE. The original Sept 2025 search-API tables (SimpleQA/FRAMES vs Brave/Exa/Tavily) are no longer in the README.

### Cited Findings
- **[vendor]** Commit history: "Initial commit" 2025-09-25 (jma127); "Add additional details about benchmark configuration to README" 2025-09-26; "Add Exa evaluation results (#6)" 2026-01-28; "Update SEAL datasets / scores (#8)" 2026-02-24; "Upgrade search evals to 0.2.0: code refactor" 2026-06-02; "Add Exa and Parallel harnesses (#16)" 2026-06-09 (most recent). 14 commits total. — [search_evals commits](https://github.com/perplexityai/search_evals/commits/main)
- **[vendor]** README (fetched 2026-11-05): "a batteries-included runner for evaluating deep-research systems"; provider harnesses, graders, cost accounting, resumable runs, per-task traces; run dirs `runs/{system}-{suite}[-{suffix}]-{config-hash}/`; `summary.json` reports failed-as-zero and failed-excluded metrics plus agent and grader cost. — [search_evals README](https://github.com/perplexityai/search_evals)
- **[vendor]** Suites: browsecomp 1,266 tasks; dsqa (DeepSearchQA) 900; hle 2,158 (text-only IR subset); widesearch 200. Datasets are not redistributed (pinned Hugging Face downloads; HLE gated at cais/hle). `OPENAI_API_KEY` required for grading. — [search_evals README](https://github.com/perplexityai/search_evals)
- **[vendor]** Results table (perplexity / openai / anthropic / exa / parallel): dsqa 0.871/0.733/0.815/0.53/0.81; browsecomp 0.805/0.720/0.598/0.38/0.56; hle 0.612/0.614/0.566/0.387/0.515; widesearch (avg f1_by_row) 0.651/0.522/0.590/0.471/0.584. Systems: Perplexity Agent API, OpenAI Responses API, Anthropic Managed Agents, Exa Agent API, Parallel Task API. — [search_evals README](https://github.com/perplexityai/search_evals)
- **[vendor]** The README shows no evaluation dates, no agent model per provider, no latency, and no SimpleQA/FRAMES/Brave/Tavily results. — [search_evals README](https://github.com/perplexityai/search_evals)

### Inferences
- The README's BrowseComp 0.805 for Perplexity is not comparable to the 0.371 in the 2025-09-25 blog: the former is the full Agent API (its own model plus tools), the latter a fixed external model calling the raw Search API. The 2026-06-09 "Add Exa and Parallel harnesses" commit dates the current table to roughly June 2026.
- Parallel Task API's 0.81 on DSQA vs Perplexity's 0.871, and 0.56 vs 0.805 on BrowseComp, repeats the Q1 pattern: closest on exhaustive search, furthest on hard single-page retrieval, in a harness Perplexity controls.

### Gaps
- No run dates, model versions or sample sizes for the published table; no way to tell whether rows are full suites or subsets without cloning and inspecting `runs/`.

---

## Q5. Perplexity Search API: pricing, rate limits, latency and the Agent API

### Takeaway
Search API is $5 per 1,000 requests (standard) or $1 (fast), billed per request not per query (up to 5 queries per request), with a flat 50 query-units-per-second limit independent of spend tier; the Agent API (`POST /v1/agent`, OpenAI-Responses-compatible alias) is a multi-provider endpoint with built-in `web_search` ($2.50 per 1k, $1 fast), `fetch_url`, `finance_search`, `people_search` and sandbox tools.

### Cited Findings
- **[vendor]** Pricing (fetched 2026-11-05, undated): Search API standard $5.00 per 1,000 requests; `search_type: "fast"` $1.00 per 1,000; "charges for each successful POST /search request, not for each query in the request"; up to five queries per request count as one unit; `max_tokens` / `max_tokens_per_page` do not change price. — [Perplexity pricing](https://docs.perplexity.ai/getting-started/pricing)
- **[vendor]** Agent API tool pricing: `web_search` $0.0025 per invocation (fast $0.001); `image_search` $0.0025; `fetch_url` $0.0005; `people_search` $0.005; `finance_search` $0.005; `sandbox` $0.03 per 20-minute session plus $0.0025 per in-sandbox search; `flex` tier bills tokens at 0.5x, `priority` at 2x where offered. — [Perplexity pricing](https://docs.perplexity.ai/getting-started/pricing)
- **[vendor]** Rate limits (fetched 2026-11-05): Search API 50 query units/second, burst 50, "independent of your usage tier". Agent API by cumulative spend: Tier 0 ($0) 1 QPS / 5M TPM / 300M TPH; Tier 1 ($50+) 3 QPS / 6M / 360M; Tier 2 ($250+) 8 / 8M / 480M; Tier 3 ($500+) 17 / 10M / 600M; Tier 4 ($1,000+) 33 / 13M / 780M; Tier 5 ($5,000+) 33 / 16M / 960M. Polling counts against QPS. — [Rate limits and usage tiers](https://docs.perplexity.ai/docs/admin/rate-limits-usage-tiers.md)
- **[vendor]** Agent API (fetched 2026-11-05): `POST https://api.perplexity.ai/v1/agent`, alias `/v1/responses`; "a multi-provider, interoperable API specification" with models from OpenAI, Anthropic, Google, xAI and others (example `openai/gpt-5.6-sol`); built-in tools `web_search` (opt-in), `fetch_url`, `finance_search`; effort presets `low`/`medium`; Sonar referred to only as the legacy Chat Completions format. SDKs `perplexityai` (Python), `@perplexity-ai/perplexity_ai` (TS). — [Agent API quickstart](https://docs.perplexity.ai/docs/agent-api/quickstart.md)
- **[vendor]** Latency percentiles for the Search API are only those self-reported in the 2025-09-25 post (p50 358 ms, p95 763 ms from us-east-1); see Q2. — [engineering post](https://www.perplexity.ai/hub/blog/architecting-and-evaluating-an-ai-first-search-api)

### Inferences
- Pricing per request with up to 5 queries bundled makes Perplexity's effective per-query cost as low as $1 per 1k (standard) when agents batch, which is not reflected in AA's per-task cost column.
- The Agent API repositions Perplexity from "search backend" to "orchestration layer over third-party models", with its own index exposed as a tool; this is the product the search_evals README now benchmarks.

### Gaps
- No current (2026) latency percentiles for standard vs fast search; the fast-search docs page was not fetched within budget.
- Agent API model token prices live on a separate models page not fetched.

---

## Q6. What is Parallel's index, crawler and "excerpts" approach?

### Takeaway
Parallel describes a "proprietary index of the global internet" of "billions of pages" with "millions of pages added daily", crawled by its own bot ShapBot (which signs requests with Web Bot Auth, RFC 9421) and served as "dense excerpts" compressed for token efficiency against a natural-language `objective`; the docs concede the index "may lack a page or contain an older copy" unless a fetch policy forces a live fetch.

### Cited Findings
- **[vendor]** Product page (fetched 2026-11-05): "Billions of pages covering the full depth and breadth of the public web"; "Millions of pages added daily"; FAQ: crawling and ranking systems "add and update millions of pages daily"; "Intelligently recrawled to keep data fresh"; freshness policies can set page-age triggers for live crawls; Parallel runs its own crawler which "respects robots.txt and related crawling directives". — [parallel.ai/products/search](https://parallel.ai/products/search)
- **[vendor]** Excerpts: "the most query relevant content from a webpage, compressed to be extremely token efficient". — [parallel.ai/products/search](https://parallel.ai/products/search)
- **[vendor]** GA launch post (undated page, sitemap lastmod 2026-11-02): "proprietary index of the global internet", "built from the ground up for AI consumption", "now spans web pages from 30+ countries"; Advanced mode involves "querying, reranking, and compressing results"; Basic P50 under 1 s, P90 under 2 s; Advanced P50 3 s. No Google/Bing mention. — [Parallel Search API post](https://parallel.ai/blog/parallel-search-api)
- **[vendor]** Crawler docs (fetched 2026-11-05): bot is ShapBot, UA `Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko); compatible; ShapBot/0.1.0`; "finds and catalogs sites for Parallel's web APIs"; IP list in shapbot.json; requests signed with Web Bot Auth (HTTP Message Signatures, RFC 9421), key directory at shapbot.parallel.ai/.well-known/http-message-signatures-directory; the docs page itself does not state robots.txt behaviour, crawl rate, training use or an opt-out. — [Parallel crawler docs](https://docs.parallel.ai/resources/crawler.md)
- **[vendor]** Indexed-content doc (fetched 2026-11-05): Search returns titles, URLs and excerpts from "indexed web content"; the index "may lack a page or contain an older copy"; by default Search does not fetch missing/stale pages; `advanced_settings.fetch_policy` can force live fetch; `source_policy.include_domains` restricts domains. No size, update frequency, or ranking description. — [Indexed content for agents](https://docs.parallel.ai/search/indexed-content-for-agents.md)
- **[vendor]** Search quickstart (fetched 2026-11-05): request takes `objective` plus optional `search_queries`; each result has `url`, `title`, `publish_date`, `excerpts[]`; `/v1/search` is the current endpoint, `/v1beta/search` legacy. — [Search quickstart](https://docs.parallel.ai/search/search-quickstart)
- **[vendor]** Series A post: search products depend on "innovations across crawling, indexing, retrieval and ranking", each built with AI as the primary user. — [Series A post](https://parallel.ai/blog/series-a)
- **[vendor]** Benchmark post: Parallel search "accepts broader declarative objectives rather than only keyword queries" and returns "the most relevant dense excerpts in an LLM-friendly format" instead of snippets or full pages. — [Search API benchmark post](https://parallel.ai/blog/search-api-benchmark)

### Inferences
- "Billions of pages" vs Perplexity's "200B URLs tracked" are not the same unit, but even generously Parallel's stated index is one to two orders of magnitude smaller than Perplexity's claimed URL frontier; the docs' admission that pages may be missing or stale, plus an opt-in live fetch, is consistent with a smaller, more selectively crawled index.
- ShapBot's RFC 9421 signatures and the "respects robots.txt" statement position Parallel as the compliant counter-image to the Perplexity/Cloudflare dispute (Q3); the name ShapBot also foreshadows the Shapley-value compensation model (Q9).

### Gaps
- No page count, URL count, crawl QPS, or hardware figures anywhere in Parallel's published material; no independent measurement of index size or freshness.
- Robots.txt compliance is asserted on the marketing page but not on the crawler docs page; no opt-out procedure documented.

---

## Q7. Parallel Search API tiers, Task API and Deep Research: latency, price, limits

### Takeaway
Four search modes: turbo (~200 ms, $1 per 1k), fast (~700 ms, $1), basic (~1 s, $5), advanced (~3 s, $5, default), with 10 results included and extra results/excerpts at $1 per 1k; the Task API ladders from lite ($5 per 1k runs) to ultra8x ($2,400 per 1k), and the product page advertises a 600 requests/min limit and up to 80,000 free search requests.

### Cited Findings
- **[vendor]** Modes (fetched 2026-11-05): turbo "~200ms", "$1 per 1,000 requests", "built to ground every call", English and Japanese only; fast "~700ms", $1 per 1k, "Recommended default for most agents"; basic "~1s", $5 per 1k, "extended snippets per result", best with 2-3 queries; advanced (default) "~3s", $5 per 1k, "a more advanced retrieval and compression pipeline" for multi-hop background agents. EU endpoint supports basic only. — [Search modes](https://docs.parallel.ai/search/modes.md)
- **[vendor]** Pricing (fetched 2026-11-05, USD): Search turbo/fast $1 per 1k requests, basic/advanced $5, 10 results included, additional results and excerpts $1 per 1k; Image Search fast $1 / advanced $5; Extract $1 per 1k URLs; Decisions $1 per 1k fast requests (up to 100 questions each); Task API per 1k successful runs lite $5, base $10, core $25, core2x $50, pro $100, ultra $300, ultra2x $600, ultra4x $1,200, ultra8x $2,400 (failed runs not billed); Responses API low $10 / medium $50 / high $250 per 1k; Monitor lite $3 / base $10 per 1k executions; FindAll preview $0.10 fixed, base $0.25 + $0.03 per match, core $2.00 + $0.15, pro $10.00 + $1.00; Entity Search $5 per 1k (100 results) + $0.05 per 1k extra. — [Parallel pricing](https://docs.parallel.ai/getting-started/pricing.md)
- **[vendor]** Product page: "$0.001 per request with 10 results + $0.001 per page extracted"; latency range 200 ms-3 s; "600 requests/min rate limit"; "up to 80,000 free search requests"; "Zero data retention", "SOC 2 Type 2", "No training with ZDR". — [parallel.ai/products/search](https://parallel.ai/products/search)
- **[vendor]** Deep Research is documented as a Task API example (task-deep-research) rather than a separate API; Task API processor guide covers lite/base/core/pro/ultra. — [Parallel docs index](https://docs.parallel.ai/llms.txt)
- **[vendor]** GA post latency: Basic P50 <1 s, P90 <2 s; Advanced P50 3 s. — [Parallel Search API post](https://parallel.ai/blog/parallel-search-api)

### Inferences
- Parallel's $1 tiers undercut Perplexity's $5 standard by 5x and match Perplexity fast; at the $5 tier the two are list-price identical, so AA's cost difference (Q1) comes from call counts, not list price.
- The "excerpts" billing line ($1 per 1k extra results/excerpts) means the headline price assumes the default payload; heavy agents paying for more excerpts narrow the gap further.

### Gaps
- Rate-limits docs page not fetched; the "600 requests/min" figure comes from the marketing page only and may differ by tier/mode.
- No p90/p95 figures for turbo, fast or advanced, and none measured independently.

---

## Q8. Parallel's published benchmarks (vendor) versus independent results

### Takeaway
Parallel's benchmark post uses its own WISER-Search set (196 questions, tested 2025-07-28/29) to show Parallel MCP beating native search and Exa MCP by 1.5-10 points across four models; its product page (tests 2026-09-09) reports Advanced at 97% SimpleQA Verified (n=100), 74% BrowseComp (n=50) and 57.6% WideSearch (n=100). No Parallel page fetched cites the Artificial Analysis score, and the "November 2025 launch benchmark post" named in the brief could not be identified.

### Cited Findings
- **[vendor]** Search API benchmark post (publication date not stated; data generated 2025-07-28, testing 2025-07-28/29): WISER-Search = WISER-Fresh (76 same-day-event questions generated by o3 pro) + WISER-Atomic (120 questions from customer use cases); agents GPT-4.1, o4-mini, o3, Claude Sonnet 4; configs Parallel Search MCP, Exa Search MCP, native web search; LLM-graded. Scores (Parallel MCP / native / Exa MCP): GPT-4.1 74.90/68.88/58.67; o4-mini 82.14/77.55/61.73; o3 80.61/79.08/56.12; Claude Sonnet 4 78.57/68.83/67.13. Claims "up to 50% cheaper" than LLM-native search; no latency numbers. — [Search API benchmark](https://parallel.ai/blog/search-api-benchmark)
- **[vendor]** Product page, tests dated 2026-09-09: SimpleQA Verified (n=100) Advanced 97%, Basic 97%, Fast 94%, Turbo 91% vs Exa/Tavily 91-94%; BrowseComp (n=50) Advanced 74%, Basic 72%, Fast 44%, Turbo 32% vs Exa/Tavily 32-70%; WideSearch (n=100, partial credit) Advanced 57.6%, Basic 55.3%, Fast 45.5%, Turbo 44%. Self-described as "the highest accuracy web search API"; no AA ranking cited. — [parallel.ai/products/search](https://parallel.ai/products/search)
- **[vendor]** GA post embeds charts for BrowseComp, HLE, SealQA, WebWalker, FreshQA, FRAMES, Coding and FinanceBench without axis labels; raw BrowseComp series values are Parallel Basic 600, Parallel Advanced 379, Tavily 973, Exa 1160 (unit unlabelled; likely cost or tokens, not accuracy). — [Parallel Search API post](https://parallel.ai/blog/parallel-search-api)
- **[vendor]** Parallel maintains a blog post titled "artificial-analysis-best-search-api" (sitemap lastmod 2026-09-18) and a "search-leaderboard" post (2026-09-18); neither was fetched within budget. — [parallel.ai sitemap](https://parallel.ai/sitemap.xml)
- **[independent]** AA (2026-10-19) places Parallel advanced at 75 with BrowseComp 77 and DSQA 81 (see Q1). — [Artificial Analysis Search Index](https://artificialanalysis.ai/agents/search-api)

### Inferences
- Parallel's self-reported BrowseComp 74% (n=50, 2026-09-09) is close to AA's independent 77 (n=200), suggesting its vendor numbers are not inflated; the gap to Perplexity is real rather than a harness artefact.
- Small vendor sample sizes (50-100) carry roughly +/-7-10 point confidence intervals, so the Advanced-vs-Basic differences on the product page are within noise.

### Gaps
- Could not identify a Parallel benchmark post dated November 2025; the sitemap shows only lastmod dates (2026) and the fetched posts omit publication dates.
- Parallel's own AA write-up and "search-leaderboard" post not fetched; whether Parallel ever held the top AA spot (the "81" claim) is unverified.

---

## Q9. Parallel's funding, Agrawal's rationale, and Index by Parallel (publisher compensation)

### Takeaway
Parallel raised a $100M Series A at $740M (co-led by Kleiner Perkins and Index Ventures, reported 2025-11-13) and a $100M Series B at $2B led by Sequoia about five months later (total raised $230M, 100,000+ developers); Agrawal frames the index as infrastructure for agents that cannot do their jobs without web access, and Index by Parallel (2026-05) pays content owners by Shapley-value contribution rather than by crawl licence.

### Cited Findings
- **[journalist]** Reuters (Krystal Hu), published 2025-11-13: $100M Series A at $740M valuation, co-led by Kleiner Perkins and Index Ventures, Khosla Ventures among existing backers. Agrawal: "How many jobs are there where we could turn off web access and ask you to do the same job fully?" and "You can't deprive an M&A lawyer from not being able to use the web, so why would you deprive their agents?"; the system returns optimized content ("tokens") for a model's context window rather than ranked links; funds to "go all in" on product and customers. No named customers, revenue or headcount. — [Reuters via The Star](https://www.thestar.com.my/tech/tech-news/2025/11/13/ex-twitter-ceo-agrawal039s-ai-search-startup-parallel-raises-100-million-)
- **[vendor]** Series A post (undated page): $100M at $740M; Kleiner Perkins and Index Ventures lead, Spark Capital participating; Khosla, First Round, Terrain existing; customers Clay, Sourcegraph, Owner, Starbridge, Actively, Genpact and an unnamed Fortune 100 insurer; "innovations across crawling, indexing, retrieval and ranking". — [Series A post](https://parallel.ai/blog/series-a)
- **[vendor]** Series B post (undated page; sitemap lastmod 2026-08-11): $100M Series B at $2B, led by Sequoia (Andrew Reed joins board); Kleiner Perkins, Index, Khosla, First Round, Spark, Terrain increased; total raised $230M; valuation "more than doubles" from the Series A "five months earlier"; "more than 100,000 developers"; customers Harvey (60+ jurisdictions), Notion, Profound, Opendoor, Actively, two large US P&C insurers, unnamed banks and hedge funds; funds to "grow its index", scale enterprise infrastructure and build "the layer connecting open-web content and data owners to AI systems". — [Series B post](https://parallel.ai/blog/series-b)
- **[journalist, snippet only]** Search results date the Series B/$2B round to late April 2026 (SiliconANGLE item dated 2026-04-28) and Index by Parallel to 2026-05-19 (Fortune; CNBC video), with a Stratechery interview on 2026-05-21; the texts were not fetched. — [SiliconANGLE](https://siliconangle.com/?p=743333); [Fortune](https://fortune.com/2026/05/19/parag-agrawal-parallel-startup-pay-publishers-when-ai-agents-use-their-work/)
- **[vendor]** Index by Parallel (undated page; sitemap lastmod 2026-08-11): shows content owners which queries their content answers and how unique its contribution is; compensation based on each source's Shapley value, "marginal contribution to the work an agent performs at the moment of inference"; launch partners The Atlantic, Fortune, Enigma, Fiscal AI, PR Newswire, RocketReach, Tracxn, ZoomInfo, and creators Alex Heath, Azeem Azhar, Mario Gabriele, Packy McCormick; "79% of major news sites block at least one AI crawler"; no revenue-share percentages or dollar amounts. — [Introducing Index by Parallel](https://parallel.ai/blog/introducing-index-by-parallel)
- **[journalist, earlier]** Search snippets: Parallel emerged from stealth in 2025-08 with about $30M raised (Business Today, 2025-08-18). Not fetched. — [Business Today](https://www.businesstoday.in/amp/technology/news/story/ex-twitter-chief-parag-agrawal-returns-to-silicon-valley-with-a-30-million-ai-company-489880-2025-08-18)

### Inferences
- Agrawal's stated rationale is demand-side ("agents need the web like workers do") rather than a technical critique of Google/Bing; the published justification for owning the index is that crawling, indexing, retrieval and ranking must be redesigned "with AI as the primary user" (vendor), plus the business goal of a compensation layer, which requires knowing exactly which indexed page contributed to which answer.
- Index by Parallel is the opposite design to Comet Plus: payment keyed to per-inference contribution of indexed content rather than to consumer-subscription traffic, and it only applies to agents using Parallel's own tools.

### Gaps
- No primary quote from Agrawal explaining why Parallel built its own crawler/index instead of licensing Bing or Google; the Stratechery and CNBC interviews were not accessible within budget.
- Series B publication date and Index launch date confirmed only via search-result snippets, not fetched articles.

---

## Q10. Is there evidence either provider uses Google, Bing or Common Crawl underneath?

### Takeaway
Both vendors assert first-party indexes built by their own crawlers (PerplexityBot; ShapBot), and no fetched source shows either reselling Google, Bing or Common Crawl; but there is also no independent audit, and the evidence is entirely self-description plus the existence of published crawler UAs and IP lists.

### Cited Findings
- **[vendor]** Perplexity, 2025-09-25: index built by its own crawler PerplexityBot; the post contrasts its architecture with "SERP-based" APIs and classes Tavily as "Google-SERP" based; Bing is mentioned only for historical pricing. — [engineering post](https://www.perplexity.ai/hub/blog/architecting-and-evaluating-an-ai-first-search-api)
- **[vendor]** Perplexity publishes PerplexityBot and Perplexity-User UAs and IP lists (perplexitybot.json, perplexity-user.json). — [Perplexity crawlers](https://docs.perplexity.ai/guides/bots)
- **[third-party vendor]** Cloudflare observed first-party crawl traffic at 20-25M declared plus an alleged 3-6M undeclared requests per day, which is direct (if contested) evidence that Perplexity fetches the web itself rather than relying solely on a third-party index. — [Cloudflare blog, 2025-08-04](https://blog.cloudflare.com/perplexity-is-using-stealth-undeclared-crawlers-to-evade-website-no-crawl-directives/)
- **[vendor]** Parallel: "proprietary index of the global internet", own crawler ShapBot with IP list and RFC 9421 signatures; no mention of Google, Bing or Common Crawl on any fetched page. — [Parallel Search API post](https://parallel.ai/blog/parallel-search-api); [Parallel crawler docs](https://docs.parallel.ai/resources/crawler.md)
- **[vendor]** Parallel's docs allow an explicit live fetch of a page absent from its index (`fetch_policy`), implying no fallback to a third-party web index. — [Indexed content for agents](https://docs.parallel.ai/search/indexed-content-for-agents.md)

### Inferences
- Published crawler identities, IP ranges and (for Perplexity) a public dispute over crawl volume are consistent with genuinely first-party indexes; a pure Bing/Google reseller would have no reason to operate crawlers at this scale.
- Absence of any Common Crawl mention does not rule out its use for seeding URL frontiers; neither vendor addresses the question.

### Gaps
- No independent audit or practitioner reverse-engineering (e.g. result-overlap studies against Google/Bing) was found within budget; Perplexity's pre-2025 reliance on third-party search APIs was not researched here.

## Verification (wave 2, topic perplexity_parallel, 2026-11-05)

| claim | verdict | what the source says | URL |
|---|---|---|---|
| 1. AA Search Index (data 2026-10-19): Perplexity (medium) 80 (DSQA 81, BrowseComp 87, Omniscience 72, $62.30, 31.4 s) tied 1st with Exa (auto) 80; Parallel (advanced) 75 (DSQA 81, BrowseComp 77, Omniscience 67, $47.93, 40.0 s) tied 6th with Brave; answer model GPT-5.6 Luna (medium) | CORRECTED | Page shows "Latest data: Oct 19, 2026", answer model GPT-5.6 Luna (medium); Perplexity 80 / 81 / 87 / 72 / $62.30 but 30.9 s/task (not 31.4); Exa (auto) 80; Parallel (advanced) 75 / 81 / 77 / 67 / $47.93 but 39.6 s/task (not 40.0); Brave 75. Ranks are derived from sort order, not stated. Live page, latency figures may drift. | https://artificialanalysis.ai/agents/search-api |
| 2. Perplexity (2025-09-25): >200B unique URLs, exabyte-scale, tens of thousands of indexing ops/s, hybrid lexical+semantic, sub-document spans, cross-encoder reranking, p50 358 ms / p95 763 ms from AWS us-east-1 vs Brave p50 513 ms, Exa p50 1375 ms | CONFIRMED | Dated Sep 25, 2025; "over 200 billion unique URLs"; "exabyte-scale index"; "tens of thousands of indexing operations per second"; hybrid lexical/semantic, self-contained spans, cross-encoder rerankers; table from AWS us-east-1: Perplexity 358/763 ms, Brave 513/808 ms, Exa 1375/2188 ms | https://www.perplexity.ai/hub/blog/architecting-and-evaluating-an-ai-first-search-api |
| 3. Parallel modes: turbo ~200 ms, fast ~700 ms at $1/1k; basic ~1 s, advanced ~3 s at $5/1k; 10 results included, extra results/excerpts $1/1k; EU endpoint basic only | CONFIRMED | modes.md: turbo ~200ms $1, fast ~700ms $1, basic ~1s $5, advanced (default) ~3s $5; "The EU endpoint at https://eu.parallel.ai supports only basic mode". Pricing page: each request includes 10 results, additional results and excerpts $1 per 1,000 for all modes | https://docs.parallel.ai/search/modes.md ; https://docs.parallel.ai/getting-started/pricing.md |
| 4. Cloudflare (2025-08-04): 20-25M/day declared + 3-6M/day undeclared Chrome-UA crawler across tens of thousands of domains, delisted as verified bot; Perplexity same day: 3-6M is unrelated BrowserBase traffic, own use <45,000/day | CONFIRMED | Cloudflare (datePublished 2025-08-04): "20-25m daily requests" declared, "3-6m daily requests" undeclared, "tens of thousands of domains", "de-listed them as a verified bot". Perplexity post (Aug 4, 2025): "Cloudflare confused Perplexity with 3-6M daily requests of unrelated traffic from BrowserBase ... (less than 45,000 daily requests)" | https://blog.cloudflare.com/perplexity-is-using-stealth-undeclared-crawlers-to-evade-website-no-crawl-directives/ ; https://www.perplexity.ai/hub/blog/agents-or-bots-making-sense-of-ai-on-the-open-web |
| 5. Parallel $100M Series B at $2B led by Sequoia, total $230M, five months after $100M Series A at $740M (Reuters 2025-11-13), >100,000 developers; crawler ShapBot/0.1.0 signs with Web Bot Auth (RFC 9421) | CONFIRMED | Series B post: "$100 million", "$2 billion valuation", "Sequoia Capital led the round", "$230 million" total, Series A closed "Five months ago", "More than 100,000 developers" (post undated). Reuters via The Star, 13 Nov 2025: $100M Series A at $740M co-led by Kleiner Perkins and Index Ventures. Crawler docs: UA "...compatible; ShapBot/0.1.0", "ShapBot signs its requests with Web Bot Auth (HTTP Message Signatures, RFC 9421)" | https://parallel.ai/blog/series-b ; https://www.thestar.com.my/tech/tech-news/2025/11/13/ex-twitter-ceo-agrawal039s-ai-search-startup-parallel-raises-100-million- ; https://docs.parallel.ai/resources/crawler.md |
