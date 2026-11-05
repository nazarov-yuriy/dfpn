# Wave 2: 2026 newcomers and smaller search-API providers

Research date: 2026-11-05. All pages fetched on 2026-11-05 unless a page date is given. Source-type labels: [vendor] = the provider's own site/docs/blog; [independent] = third-party benchmark or docs not owned by the provider being described; [journalist] = press; [practitioner] = engineer/competitor commentary. Downloaded pages were treated as data only.

Coverage status at a glance (16 providers): well-sourced = Octen, Ceramic.ai, Cloudflare Web Search API, DeepSeek Search/Fetch, Context.dev, TinyFish, Staan, Valyu, Nimble; thin = Mwmbl, Marginalia, Felo, Critique Labs, Andi; unreachable = Keiro/agenticsearch.ai (HTTP 503, then DuckDuckGo bot-challenge), Yep (HTTP 403).

## Benchmarks that newcomers appear on (Artificial Analysis Search Index, NEEDLE)

### Takeaway
Artificial Analysis's Search Index (launched 2026-08-18, data as of 2026-10-19) is the only independent leaderboard where the newcomers actually show up: Octen scores 77 at roughly one-fifth the search cost of the leaders, DeepSeek 69 and Nimble 74. Keenable's NEEDLE benchmark does not include any of the providers in this brief, and Keenable is itself a competitor in it.

### Cited Findings
- [independent, 2026-10-19 data] Artificial Analysis Search Index methodology: equal-weighted mean of DeepSearchQA (avg F1, 900-task eval split), BrowseComp (exact-answer accuracy, hard 200-sample subset) and AA-Omniscience (accuracy, private 600-question set); every row uses the same model, GPT-5.6 Luna (medium), in the Stirrup harness with web_search and web_fetch tools, only the search provider varies; page says it benchmarks 26 products across 14 providers — [Artificial Analysis Search Index](https://artificialanalysis.ai/agents/search-api); methodology page [Artificial Analysis methodology](https://artificialanalysis.ai/methodology/search-api)
- [independent, 2026-08-18] Index launched 2026-08-18 with 11 provider results across 7 providers; a 2026-08-31 snapshot listed 19 products from 9 providers with Perplexity Search (medium) on top at 80 — [Artificial Analysis articles](https://artificialanalysis.ai/articles/search-api); [AA Japanese leaderboard](https://artificialanalysis.ai/ja/agents/search-api)
- [independent, 2026-10-19 data] Leaderboard rows (Index / DeepSearchQA F1 / BrowseComp / AA-Omniscience / search $ per 1k tasks / model $ per 1k tasks / time per task): Exa Search (auto, dynamic highlights) 80/86/83/73/$53.17/$10.60/36.9s; Perplexity Search (medium) 80/81/87/72/$62.30/$8.04/31.4s; Exa Search (lite) 79/85/81/72/$31.20/$10.95/19.6s; Perplexity Search (high) 79/81/86/71/$56.93/$9.37/29.5s; **Octen Search (highlights) 77/80/86/66/$9.07/$14.50/15.8s**; Parallel Search (advanced) 75/81/77/67/$47.93/$10.67/40.0s; Brave Search (LLM context) 75/78/77/69/$61.96/$16.95/22.9s; You.com Search (highlights) 74/77/77/69/$47.54/$19.41/21.5s; **Nimble Search (standard) 74/76/75/71/$46.14/$16.64/24.6s**; OpenAI Web Search (medium) 74/78/74/72/$40.19/$9.40/33.3s; Firecrawl Search 73/74/74/73/$30.48/$11.58/61.9s; **DeepSeek Search (summary) 69/75/63/70/$8.47/$20.19/22.7s**; model-only baseline 33/45/17/38/—/$2.92/26.9s — [Artificial Analysis Search Index](https://artificialanalysis.ai/agents/search-api)
- [independent, 2026-10-19 data] Note on columns: the "$ per 1k tasks" column is cost per 1,000 benchmark tasks (each task issues many queries), not per 1,000 queries; "time per task" combines model and search time, so it is not per-query latency — [Artificial Analysis Search Index](https://artificialanalysis.ai/agents/search-api)
- [independent, 2026-10-19 data] Ceramic.ai, Keenable, Keiro, Valyu, Linkup, Tavily, Serper, SerpApi and Cloudflare did not appear in the leaderboard rows extracted from the page text; the page states 26 products / 14 providers but the extracted table shows 12 providers, so some rows (possibly TinyFish, Tavily, Linkup) may be rendered client-side — [Artificial Analysis Search Index](https://artificialanalysis.ai/agents/search-api)
- [vendor citing independent, 2026-10-19 data] TinyFish says its TinySearch averaged $0.0093 per task in the Artificial Analysis Search Index with search fees listed as $0 — [TinyFish homepage](https://tinyfish.ai/)
- [vendor, 2026-08-27 byline; page metadata 2026-11-03] NEEDLE (News, Everyday, Expert, Deep-tail, Legal Evaluation) by Keenable: a live benchmark whose news queries regenerate hourly and other verticals daily; the Keenable post names seven engines tested — Keenable, Google (via Serper), Bing (via SearchAPI), Brave, Tavily, Parallel, Exa — and gives Keenable p50 latency of 200 ms; GitHub https://github.com/keenableai/needle — [Keenable NEEDLE post](https://keenable.ai/blog/needle-the-benchmark-your-search-engine-can-t-memorize)
- [journalist, 2026-08-31] MarkTechPost's coverage says NEEDLE spans 15 search APIs with a 2,000-character evidence cap and reports Deep-tail scores Exa 0.557, Keenable 0.470, Bing 0.199 "of ultimate", with p50 latency Keenable-realtime 193 ms, Exa 1,876 ms, Bing 2,767 ms — [MarkTechPost](https://www.marktechpost.com/2026/08/31/keenable-ai-open-sources-needle-a-live-search-benchmark-that-rebuilds-its-query-set-every-hour/) (numbers came via search-result summary; the Keenable post itself puts them only in charts)
- [practitioner] NEEDLE's ceiling is a synthetic "oracle" pooled from the tested engines, so it cannot see pages none of the engines found; Keenable competes in its own benchmark and no independent replication was found — [MarkTechPost](https://www.marktechpost.com/2026/08/31/keenable-ai-open-sources-needle-a-live-search-benchmark-that-rebuilds-its-query-set-every-hour/)

### Inferences
- Octen's 77 Index at $9.07 per 1k tasks versus Exa auto's 80 at $53.17 implies roughly 6x lower search spend for a 3-point Index deficit; its BrowseComp 86 ties the leaders while AA-Omniscience 66 is the lowest of the top tier, consistent with a fast-but-shallower index.
- DeepSeek Search (summary) is the cheapest search row ($8.47/1k tasks) but has the worst BrowseComp (63) among commercial rows and the highest model cost ($20.19), suggesting its summaries make the model work harder.
- None of Octen, Ceramic, Keiro, Valyu, Staan, Context.dev or Cloudflare has a NEEDLE row; NEEDLE should not be cited for these providers.

### Gaps
- Artificial Analysis's "Search API Cost per 1k Queries" chart values were not in page text; per-query prices on the leaderboard could not be extracted.
- The full NEEDLE per-vertical table (15 engines) was not obtainable from text; only the three Deep-tail scores and three latencies surfaced via a secondary summary.
- No Artificial Analysis row for Ceramic, Linkup, Valyu, Staan, Keiro or Context.dev was found.

## Octen (Singapore / San Francisco)

### Takeaway
Octen (legal entity APITECH AI Pte Ltd., founded by ex-Alibaba Cloud/Baidu search lead Kuan Zou) raised a $10M seed led by Square Peg with Argor, claims P50 latency of 62 ms and >1M QPS per account on a proprietary distributed engine, and by November 2026 has moved from invite-only beta to self-serve pricing of $1 per 1K calls (shown as 80% off a $5 list) with MCP, Skill and CLI access; it scores 77 on Artificial Analysis's Search Index.

### Cited Findings
- [journalist, 2026-04-22] Octen, officially APITECH AI Pte Ltd., a three-month-old startup with offices in Singapore and San Francisco, raised a $10M seed led by Square Peg joined by Singapore-based Argor and a group of AI researchers; founder and CEO Kuan Zou; product in invite-only beta being tested by multiple AI software providers; funds for engineering, developer relations and globally distributed backend infrastructure — [SiliconANGLE](https://siliconangle.com/2026/04/22/octen-raises-10m-seed-funding-speed-ai-agent-search-queries/)
- [journalist, 2026-04-22] Median response time of 62 ms on the SealQA Hard benchmark (200+ multistep questions requiring web retrieval and reasoning), described as more than four times faster than the fastest (unnamed) rival; infrastructure processes more than one million queries per second per customer account; Octen-Embedding-8B reportedly set a record on RTEB — [SiliconANGLE](https://siliconangle.com/2026/04/22/octen-raises-10m-seed-funding-speed-ai-agent-search-queries/)
- [journalist, 2026-04-22] Kuan Zou quote: "An agent can process thousands of data points simultaneously"; stated aim is to let agents reason over the live web at a speed comparable to memory — [SiliconANGLE](https://siliconangle.com/2026/04/22/octen-raises-10m-seed-funding-speed-ai-agent-search-queries/)
- [investor, 2026-03-25] Square Peg investment note: Kuan Zou has nearly a decade in search/AI infrastructure, led AI search at Alibaba Cloud for over five years and earlier built Baidu's enterprise search platform; team from Meta, Google, TikTok, Alibaba, Baidu, DeepSeek and Xiaohongshu; US$10M seed led by Square Peg with Argor and a group of AI scientists; P50 latency 62 ms; >1M QPS on a single account; real-time indexing keeps data fresh within 5-minute intervals; "proprietary distributed search engine built for AI workloads"; embedding model "swept the RTEB leaderboard" and is open-sourced on HuggingFace; UVP: "the real-time, LLM-native search layer AI agents actually need" — [Square Peg](https://squarepeg.vc/blog/investment-notes-octen-us-10m-seed)
- [vendor, accessed 2026-11-05] Homepage UVP: "LLM-native web search, delivering industry-leading real-time intelligence with the lowest latency and enterprise-grade reliability"; "Real-time indexing"; demo widget shows Web Search 79 ms and Extract 164 ms; access "One API key, three ways in — as a Skill, over MCP, or from the CLI" (GitHub Octen-Team/octen-skills); SOC 2 Type 2 badge; Video Search and Multimodal Chat are "Early Access", Web Search has open "Get Started" — [Octen homepage](https://octen.ai); docs https://docs.octen.ai/capabilities/web-search
- [vendor, accessed 2026-11-05] Vendor accuracy table (SimpleQA / FreshQA Strict): Octen 95.2% / 55.8%; Exa instant 89.2% / 52.8%; Parallel turbo 88.6% / 52.8%; Tavily ultra-fast 69.9% / 43.2% — [Octen homepage](https://octen.ai)
- [vendor, accessed 2026-11-05] Embedding leaderboards: Octen-Embedding-8B #1 on RTEB (mean 0.7953, January 2026); octen-vl-embedding-large #1 on MMEB-V2 (80.09, May 2026) — [Octen homepage](https://octen.ai)
- [vendor, accessed 2026-11-05] Pricing: Web Search (FAST) pay-as-you-go $1 per 1K calls, displayed next to $5 per 1K with an "80% Off" label; $0.5 per 1K results for full content, 10 full-content results free per call; Extract $1 per 1K URLs standard / $2.5 advanced, failed URLs free; Answer billed as search fees plus model rates; new accounts get $5 free balance; QPS tiers Free 10-20, Builder 50, Pro 200, Max 500, Enterprise 1M+; enterprise adds Zero Data Retention, volume discounts, dedicated Slack; no invite-only or waitlist language on the pricing page — [Octen pricing](https://octen.ai/pricing)
- [independent, 2026-10-19 data] Artificial Analysis: Octen Search (highlights) Index 77 (DeepSearchQA 80, BrowseComp 86, AA-Omniscience 66), search cost $9.07 per 1k tasks, 15.8 s per task (fastest per-task time in the top tier) — [Artificial Analysis Search Index](https://artificialanalysis.ai/agents/search-api)

### Inferences
- The invite-only status reported 2026-04-22 appears to have ended: the pricing page now offers self-serve sign-up with a $5 credit. Treat "invite-only" as historical (April 2026).
- The task's stated "$1.10 vs $5" conflict attributed to Nimble may partly stem from Octen's page, which shows a $5 list price struck to $1; Nimble's own page shows $1.1 (see Nimble section).
- The 62 ms figure is a vendor-measured P50 on SealQA Hard, repeated by Square Peg and SiliconANGLE; no independent per-query latency measurement for Octen was found. Artificial Analysis's 15.8 s/task is end-to-end agent time, not search latency.
- Octen's index is described only as a "proprietary distributed search engine" with "real-time indexing"; no page states whether it crawls independently or relies on Google/Bing/Common Crawl. Index size is unpublished.

### Gaps
- Index size, crawler name and crawl source not disclosed anywhere fetched.
- SealQA Hard latency comparison does not name the rival; no independent replication found.
- Square Peg's note is dated 2026-03-25 while the press announcement is 2026-04-22; the discrepancy (pre-publication vs embargo) is unexplained.

## DeepSeek Search / Fetch API

### Takeaway
DeepSeek's standalone Search and Fetch APIs cost $0.75 per 1,000 successful requests each, run on an "in-house search engine", and score 69 on the Artificial Analysis Search Index at the lowest search spend on the board ($8.47 per 1k tasks).

### Cited Findings
- [vendor, accessed 2026-11-05] "$0.75 per 1,000 successful requests" for both Search and Fetch; per request, not per token or result; failed requests, empty results and timeouts are not billed; `count` (1-50, default 10) does not change the price — [DeepSeek Search guide](https://api-docs.deepseek.com/guides/search)
- [vendor, accessed 2026-11-05] Search is "powered by DeepSeek's in-house search engine"; endpoints `POST https://api.deepseek.com/v1/tools/search` and `POST https://api.deepseek.com/v1/tools/fetch`, bearer auth, standalone raw JSON; rate limits 100 QPS for Search and 25 QPS for Fetch at the account level plus a per-domain QPS limit on Fetch, HTTP 429 over limit; calls triggered by server-side tools in DeepSeek Harness, Claude Code or Codex are billed the same way; UVP: "The Search API and the Fetch API give agents and RAG applications access to live web content" — [DeepSeek Search guide](https://api-docs.deepseek.com/guides/search)
- [vendor, accessed 2026-11-05] Docs homepage banner: "Search / Fetch API is now available, powered by our in-house search engine and supporting web search and fetch"; news item slug `/news/news261017` — [DeepSeek API docs](https://api-docs.deepseek.com)
- [independent, 2026-10-19 data] Artificial Analysis: DeepSeek Search (summary) Index 69 (DeepSearchQA 75, BrowseComp 63, AA-Omniscience 70), search $8.47 per 1k tasks, model $20.19, 22.7 s/task — [Artificial Analysis Search Index](https://artificialanalysis.ai/agents/search-api)

### Inferences
- The news slug `news261017` suggests an announcement dated 2026-10-17, consistent with the task brief's "October 2026"; the launch date is otherwise not stated in the guide.
- No MCP server is mentioned in the guide; access is via raw HTTP or through DeepSeek Harness/Claude Code/Codex server-side tools.

### Gaps
- Launch date not explicitly stated; latency not published; index size and crawler not disclosed; no vendor benchmark claims found.

## Cloudflare Web Search API and Ceramic.ai

### Takeaway
Cloudflare's Web Search API (docs last updated 2026-10-02) is a single AI Gateway endpoint that routes to Ceramic.ai (default, $0.25/1K, ZDR), Exa ($7.00/1K, no ZDR) or Linkup ($5.00/1K, ZDR) "at the provider's list API price, with no additional markup"; Ceramic.ai, founded by ex-Google VP Anna Patterson and Cuil founder Tom Costello, claims a 40B+ page independent index, 50 ms latency and "20x cheaper, 10x faster".

### Cited Findings
- [independent (Cloudflare on third parties), last updated 2026-10-02] Providers page: Ceramic.ai $0.25 per 1,000 requests, Zero Data Retention yes, "more than 40 billion pages" in its own independent index, returns long page descriptions up to 8,000 characters, default when no provider is set; Exa $7.00 per 1,000, ZDR no, returns query-relevant highlights, `auto` mode only; Linkup $5.00 per 1,000, ZDR yes, `fast` depth, raw sourced snippets with no generated answer; "each search is billed at the provider's list API price, with no additional markup" when paid with AI Gateway credits; BYOK billed by the provider — [Cloudflare Web Search providers](https://developers.cloudflare.com/web-search/providers/index.md)
- [practitioner/competitor, 2026-10-11] Parallel.ai's analysis: each call returns at most 10 results; search only (no fetch/extract); Exa's search mode cannot be changed; BYOK supported for all three; Cloudflare's changelog says all three providers support ZDR while the Providers page lists Exa as "No" — advises treating Exa as non-ZDR until reconciled — [Parallel.ai article](https://parallel.ai/articles/cloudflare-web-search-api)
- [journalist (Spanish), 2026-10] Coverage of the launch naming Exa, Ceramic and Linkup as the three providers — [Ecosistema Startup](https://ecosistemastartup.com/cloudflare-lanza-web-search-api-con-exa-ceramic-y-linkup/)
- [vendor, accessed 2026-11-05] Ceramic.ai founders: Dr. Anna Patterson, former Google VP of Engineering and Product and "inventor of TeraGoogle"; Dr. Tom Costello, Stanford AI PhD and founder of Cuil; backed by NEA, Earthshot Ventures, IBM, Samsung Next and Mento VC (no amounts) — [Ceramic.ai](https://ceramic.ai); team page https://ceramic.ai/team
- [vendor, accessed 2026-11-05] "40B+ pages indexed", launched Q2 2026; $0.25 per 1K queries with 1,000 free queries; "As fast as 50ms"; UVP: "Web-scale search that's 20× cheaper, 10× faster, accurate & fully independent"; tagline "Search More. Pay Less. Built for AI Agents."; cost example: competitor $14.00 per 1K vs Ceramic $0.25 (with Grok 4.6 model cost $2.00 per 1K assumed), totals $16.00 vs $2.25; demo "4x more searches" and "14x cheaper"; enterprise: private data indexing, SOC 2 Type II, zero data retention; site owners told to "add Allow: TerraCotta to your robots.txt" — [Ceramic.ai](https://ceramic.ai); docs https://docs.ceramic.ai/; SDK https://github.com/CeramicTeam/ceramic-python

### Inferences
- The robots.txt instruction ("Allow: TerraCotta") strongly implies Ceramic runs its own crawler named TerraCotta, consistent with Cloudflare's "own independent index" description; neither page states this explicitly.
- Ceramic's "20x cheaper" is arithmetic against an unnamed $5/1K competitor; its own cost example uses $14/1K, i.e. 56x. The vendor comparison baseline is inconsistent.
- Cloudflare's no-markup resale makes Ceramic's $0.25 the cheapest listed price among all providers in this brief except TinySearch ($0).

### Gaps
- Ceramic funding amount, latency measurements beyond "as fast as 50ms", any accuracy benchmark, and MCP availability were not found.
- Cloudflare's own 2026-10-02 blog post was not fetched directly (discovery search surfaced docs and third-party coverage instead).

## Context.dev

### Takeaway
Context.dev is a YC-backed "unified web context API for software and AI agents" sold on monthly credit plans (roughly $0.38-$2.00 per 1K credits by my arithmetic) with an MCP server; it discloses a 99.96% scrape success rate but no index source, latency or search benchmark.

### Cited Findings
- [vendor, accessed 2026-11-05] UVP: "The unified web context API for software and AI agents"; scope covers search (`POST /v1/web/search`), scraping, crawling, structured extraction, brand data, people enrichment, news and monitors; "backed by Y Combinator"; plans: Developer $20/mo for 10,000 credits, Pro $90/mo for 100,000, Growth $300/mo for 500,000, Scale $500/mo for 1,000,000, Scale 2.5M $950/mo for 2,500,000; credit costs: scrape 1 credit (2 with browser actions), Answers 10 fast / 100 Ultra, People Search 10 per page, Company Search 2 fast / 10 ultra; 99.96% scrape success rate; 99.9% uptime SLA on Enterprise; Company Search ultra "can take up to 20 seconds"; MCP server offered (install docs https://docs.context.dev/install-mcp); SDKs Apache-2.0 at https://github.com/context-dot-dev — [Context.dev](https://context.dev); pricing https://www.context.dev/pricing

### Inferences
- Effective rates of about $2.00, $0.90, $0.60, $0.50 and $0.38 per 1K credits are my division of plan price by included credits, not vendor figures; a plain search call's credit cost was not stated, so per-1K-query pricing cannot be derived.

### Gaps
- Founders, funding amount, index source, search latency, benchmark rows: none found.

## TinyFish

### Takeaway
TinyFish positions itself as "The web stack for AI agents" with a free TinySearch that, per its own FAQ, queries Google's live index through a real browser, plus paid TinyAgent ($0.016/step) and TinyBrowser ($0.002/min); it cites named enterprise customers and an 89.9% Online-Mind2Web score.

### Cited Findings
- [vendor, accessed 2026-11-05] Products: TinySearch, TinyFetch, TinyBrowser, TinyAgent, Mako ("web-native model for live workflows"); "All products share one API key"; UVP: "The web stack for AI agents" / "Search, extract, browse, and act on the web with one platform"; TinySearch: "Fresh results from the live web. Never cached", FAQ says it queries Google's live index, "not a secondary index or cached results"; pricing: TinySearch free, TinyFetch free, TinyAgent $0.016 per step, TinyBrowser $0.002 per minute, TinyMonitor $0.005 per check, "$8 free"; benchmarks: TinyAgent 89.9% on Online-Mind2Web, hard tasks 81.9% vs Operator 43.2% and Claude 32.4%, 300 runs open-sourced; $0.0093 per task average on Artificial Analysis Search Index (2026-10-19) with $0 search fees; customers DoorDash ("1M+ quarterly web workflows"), ClassPass ("98.6% less manual work"), Amazon, The Zebra, Grubhub ("353 net-new restaurants found in Boston"), GetGo, TestSprite; search mockup shows 556 ms; MCP not listed as a feature, only a G2 reviewer says "The MCP connection was easy to set up" — [TinyFish](https://tinyfish.ai/); docs https://docs.tinyfish.ai/; benchmarks https://tinyfish.ai/benchmarks

### Inferences
- TinySearch is a Google-SERP-backed live search, not an independent index; it competes on price ($0) rather than on index ownership.
- tinyfish.io 301-redirects to tinyfish.ai.

### Gaps
- Founders, funding, explicit latency claim, and an official MCP server page were not found on the homepage.

## Keiro (agenticsearch.ai)

### Takeaway
Nothing could be verified: agenticsearch.ai returned HTTP 503 and the DuckDuckGo fallback returned a bot-verification challenge instead of results.

### Cited Findings
- None.

### Inferences
- None.

### Gaps
- Founders, funding, index source, pricing, latency, benchmarks, MCP and UVP for Keiro are all unverified; the provider does not appear in the Artificial Analysis rows extracted or in the Keenable NEEDLE engine list.

## Staan (European Search Perspective; Qwant/Ecosia)

### Takeaway
Staan markets itself as "the first European Search API", priced at EUR 2 per 1K (Web Search) and EUR 4 per 1K (Web Search for AI) with 1,000 free requests per month, p95 under 800 ms, EU-only hosting, and runs "on the same search stack as Qwant Search", "Powered by European Search Perspective"; the Qwant/Ecosia ownership is not stated on the site.

### Cited Findings
- [vendor, accessed 2026-11-05] UVP: "Fuel your AI with the first European Search API"; FAQ: "an independent European web search index for developers and modern AI applications"; "our own European web search API and index"; "on the same search stack as Qwant Search"; "Powered by European Search Perspective"; pricing: Web Search EUR 2 per 1,000 requests, Web Search for AI EUR 4 per 1,000 (adds extra snippets, reranking, full document fetch in HTML or Markdown), both up to 20 QPS, first 1,000 requests per month free, Custom plan; latency under 800 ms p95 for search, Web Search for AI end-to-end minimum 1 s; "4× cheaper than alternatives"; markets fr-fr, en-us, de-de, en-uk; languages French, English, German; EU data centres, EU-only routing available — [Staan](https://staan.ai); FAQ https://staan.ai/faq; docs https://docs.staan.ai
- [vendor (Mwmbl), accessed 2026-11-05] Mwmbl's Seed Search builds its index "with high quality results from EUSP and ranking from Typesafe AI", confirming EUSP operates as a results supplier to third parties — [Mwmbl](https://mwmbl.org)

### Inferences
- The Qwant/Ecosia joint ownership of European Search Perspective (EUSP) is in the task brief but was not confirmed by any page fetched here; treat it as unverified in this wave.

### Gaps
- Index size, pages crawled, launch date, MCP availability, benchmark rows, and the Qwant/Ecosia ownership statement were not found on staan.ai.

## Valyu

### Takeaway
Valyu sells "One API to search specialist, proprietary and web sources" priced per 1,000 results returned rather than per query: web about $0.63 CPM, arXiv/PubMed about $0.31, up to $30 CPM for licensed journals; founders, funding, index source and benchmarks were not found on the vendor pages.

### Cited Findings
- [vendor, accessed 2026-11-05] UVP: "One API to search specialist, proprietary and web sources, and run multi-step research with cited, structured outputs"; verticals Finance and Science & R&D; "o11" named as a customer using Valyu as a data layer for financial research agents — [Valyu](https://valyu.ai)
- [vendor, accessed 2026-11-05] Search API priced per 1,000 results (CPM) by source: arXiv/PubMed/bioRxiv/medRxiv about $0.31; Web about $0.63; clinical trials $5; stock prices $6; patents $8; SEC filings $12; licensed journals $30; "for the results you get back, not a flat rate per query"; DeepResearch API credits per task: Instant 8, Fast 25, Standard 100, Heavy 500, Max 2,500, add-ons (screenshots 8, code execution 16, browser use 48, deliverables 16 each after first); failed tasks not charged; auto top-up "from $10"; 402 `insufficient_credits` when exhausted, no overage — [Valyu pricing](https://www.valyu.ai/pricing)

### Inferences
- At the default 10 results per query, web search costs about $0.0063 per query, i.e. roughly $6.30 per 1K queries — my arithmetic, not a vendor figure; per-result pricing makes direct comparison with per-query vendors sensitive to result count.

### Gaps
- Founders, funding, crawler/index source (own vs licensed), latency, benchmark rows, MCP server: not on the two pages fetched.

## Nimble (nimbleway.com) and the $1.10 vs $5 question

### Takeaway
Nimble's own pricing page lists the Search API at "$1.1 /1k requests" with 5,000 free requests per month; no $5 per 1K figure appears anywhere on it, so $1.10 is the current list price and the $5 figure is unconfirmed (possibly historical, or a mix-up with Octen's $5 struck-through list price or Linkup's $5 via Cloudflare). Nimble announced a $47M Series B, offers an MCP server, and scores 74 on Artificial Analysis.

### Cited Findings
- [vendor, accessed 2026-11-05] Pricing: Free $0 with "5,000 free requests per month"; Search API $1.1 per 1K requests (labels "Lite" and "Standard" with no separate prices); Extract, Crawl, Map API $1 per 1K; Extract Template API $3 per 1K; Media API $2 per GB; Agent API priced per request (amount not rendered); Startup $2,500/mo (350K monthly web page credits, 5 concurrent agents), Scale $7,000/mo (1.2M credits, 10 agents), Professional $15,000/mo (3M credits, 20 agents), Enterprise custom, all billed annually; "$5 per 1K" does not appear — [Nimble pricing](https://www.nimbleway.com/pricing)
- [vendor, accessed 2026-11-05] Homepage: blog post "Announcing Our $47M Series B and the Nimble Web Search Agent Platform"; products Agent API, Search API, Extract API; endpoints /search, /agent, /dataset, /monitor (beta), /extract, /crawl; "Proprietary Index and Memory"; UVP "Get Expert-Level Web Search for Your AI Agents" and "delivers higher accuracy at a fraction of the token cost"; MCP Server documented at https://docs.nimbleway.com/integrations/mcp-server/mcp-server; listed as an official plugin for ChatGPT and Codex; case study (Alta) "3-4× deeper context" and ">99% reliability"; blog "How Nimble Benchmarks Web Search" — [Nimble](https://nimbleway.com)
- [independent, 2026-10-19 data] Artificial Analysis: Nimble Search (standard) Index 74 (DeepSearchQA 76, BrowseComp 75, AA-Omniscience 71), search $46.14 per 1k tasks, 24.6 s/task — [Artificial Analysis Search Index](https://artificialanalysis.ai/agents/search-api)

### Inferences
- Resolution of the price conflict: the vendor's live page supports $1.10 per 1K for Search API (2026-11-05). The $5 figure may be an older Nimble price or a conflation with Octen ($5 list, "80% off" to $1) or Linkup ($5 via Cloudflare); it should not be cited as Nimble's current price.
- Nimble's $46.14 per 1k tasks on Artificial Analysis versus $1.1 per 1K requests implies roughly 40 search requests per benchmark task, or that the benchmark used a dearer tier; the two numbers are not directly comparable.

### Gaps
- Whether Nimble's Search API queries Google/Bing live or its own index is not stated ("Proprietary Index and Memory" is marketing language); founders and Series B investors/date were not on the fetched pages; Agent API price did not render; the $47M Series B post was not fetched.

## Andi, Felo, Critique Labs

### Takeaway
All three are consumer-facing AI search products with little public API detail: Andi's homepage rendered only its title, Felo exposes an API portal (openapi.felo.ai) with no public pricing found, and Critique Labs (Starman LLC) describes an "Agentic Search Engine" and API-builder platform without pricing or index details.

### Cited Findings
- [vendor, accessed 2026-11-05] Andi: only text retrieved is the title "Andi - AI Search for the Next Generation" — [Andi](https://andisearch.com)
- [vendor, accessed 2026-11-05] Felo: operated by "Felo Inc." (copyright 2026, https://official.felo.ai/); UVP "Search, understand, and create with AI"; API portal https://openapi.felo.ai/; products LiveDoc, Agents, Slides, LLM Playground, Enterprise — [Felo](https://felo.ai)
- [vendor, accessed 2026-11-05] Critique Labs: company Starman LLC, Mountain View, CA (copyright 2026); "Agentic Search Engine" described as "The foundation of our ecosystem - an intelligent engine that powers all Critique AI products through agentic search capabilities"; Critique API Platform "An agentic API builder that takes you from prompt to production-ready deployed endpoint just by prompting"; Critique Browser extension with "autonomous fact-checks, in-line cited facts"; headline UVP "Powering a new generation of intelligent applications with agentic search" — [Critique Labs](https://critique-labs.ai); docs docs.critique-labs.ai

### Inferences
- None of the three published a per-1K price, latency figure, benchmark row or MCP server on the pages fetched; they are better classed as consumer answer engines than as search-API vendors as of this wave.

### Gaps
- Founders, funding, index source (own vs Bing/Google), API pricing, latency, benchmarks, MCP: all unfound for Andi, Felo and Critique Labs.

## Mwmbl, Marginalia, Yep (independent/open indexes)

### Takeaway
Mwmbl is "The truly open source search engine" (AGPL-3.0, non-profit, donation-funded) now seeding its index with EUSP results and Typesafe AI ranking; Marginalia runs "Custom index and crawler software" prioritising non-commercial content with "no AI"; Yep (Ahrefs) was unreachable (HTTP 403). No 2026 index-size figure was obtainable for Marginalia or Mwmbl from the pages fetched.

### Cited Findings
- [vendor, accessed 2026-11-05] Mwmbl: "The truly open source search engine"; "Mwmbl (pronounced 'mumble') is a search engine that's completely independent, open source, and non-profit"; AGPL-3.0, copyright 2024-2026; donations via https://opencollective.com/mwmbl; Seed Search helps "build our index with high quality results from EUSP and ranking from Typesafe AI"; stats at /stats, index dumps at /dumps; GitHub https://github.com/mwmbl; blog https://blog.mwmbl.org/ — [Mwmbl](https://mwmbl.org)
- [vendor, accessed 2026-11-05] Marginalia: "Custom index and crawler software"; UVP sections "Prioritizes non-commercial content", "Simple technology, no AI", "Filter out tracking"; AGPL; source at https://git.marginalia.nu/; about page https://about.marginalia-search.com/; old version remains at https://old-search.marginalia.nu/; www.marginalia-search.com 301-redirects to http://marginalia-search.com/ — [Marginalia](http://marginalia-search.com/)
- [vendor, accessed 2026-11-05] Yep: https://yep.com returned HTTP 403 Forbidden to the fetcher — no content obtained.

### Inferences
- Mwmbl's use of EUSP results implies it is no longer purely volunteer-crawled for seeding; this is a notable 2026 shift for a project branded as fully independent, but the page does not quantify it.

### Gaps
- Marginalia's 2026 index size (documents/pages), founder name, NLnet funding, and API terms were not on the homepage; the about page was not fetched within budget.
- Mwmbl founder name, index size (stats page not fetched), and API availability not confirmed.
- Yep: ownership by Ahrefs, index size, crawler name, 90/10 revenue share, and API availability could not be verified (403).

## Cross-provider summary table (as fetched 2026-11-05)

| Provider | Founders / funding | Index source | List price | Latency claim | Independent benchmark | MCP | UVP (vendor words) |
|---|---|---|---|---|---|---|---|
| Octen | Kuan Zou; $10M seed, Square Peg + Argor (2026-04-22) | Proprietary distributed engine, "real-time indexing", size undisclosed | $1/1K (was $5), $0.5/1K full-content results | P50 62 ms (SealQA Hard, vendor) | AA Index 77, $9.07/1k tasks | Yes (+Skill, CLI) | "LLM-native web search... lowest latency and enterprise-grade reliability" |
| DeepSeek Search | DeepSeek | "In-house search engine" | $0.75/1K successful requests | none | AA Index 69, $8.47/1k tasks | not stated | "give agents and RAG applications access to live web content" |
| Cloudflare Web Search | Cloudflare | Resells Ceramic/Exa/Linkup | $0.25 / $7.00 / $5.00 per 1K, no markup | none | none | not stated | single AI Gateway endpoint |
| Ceramic.ai | Anna Patterson, Tom Costello; NEA, Earthshot, IBM, Samsung Next, Mento | Own 40B+ page index (crawler likely "TerraCotta") | $0.25/1K, 1,000 free | "as fast as 50ms" | none found | not stated | "20× cheaper, 10× faster, accurate & fully independent" |
| Context.dev | YC-backed | undisclosed | $20-$950/mo credit plans | none | none | Yes | "The unified web context API for software and AI agents" |
| TinyFish | undisclosed | Google live index via real browser | TinySearch free | none (556 ms mockup) | AA $0.0093/task (vendor citing) | implied only | "The web stack for AI agents" |
| Keiro | unreachable | — | — | — | — | — | — |
| Staan | EUSP ("same stack as Qwant") | Own European index | EUR 2 / EUR 4 per 1K | <800 ms p95 | none | not stated | "the first European Search API" |
| Valyu | undisclosed | specialist + web, source undisclosed | ~$0.63 CPM web, $0.31-$30 CPM others | none | none | not stated | "One API to search specialist, proprietary and web sources" |
| Nimble | $47M Series B | "Proprietary Index and Memory" | $1.1/1K Search API | "blazing-fast" | AA Index 74, $46.14/1k tasks | Yes | "Expert-Level Web Search for Your AI Agents" |
| Andi / Felo / Critique | undisclosed | undisclosed | none public | none | none | not stated | "AI Search for the Next Generation" / "Search, understand, and create with AI" / "agentic search" |
| Mwmbl | non-profit, donations | own + EUSP seed results | none | none | none | no | "The truly open source search engine" |
| Marginalia | undisclosed here | own crawler | none | none | none | no | "Prioritizes non-commercial content", "no AI" |
| Yep | unreachable (403) | — | — | — | — | — | — |

## Verification (wave 2, topic newcomers, 2026-11-05)

| claim | verdict | what the source says | URL |
|---|---|---|---|
| AA Search Index (data 2026-10-19): Octen (highlights) 77 (DSQA 80, BrowseComp 86, Omniscience 66), $9.07/1k, 15.8 s/task; Nimble (standard) 74 @ $46.14; DeepSeek (summary) 69 @ $8.47; Exa auto 80 @ $53.17 | CORRECTED | "Latest data: Oct 19, 2026". Octen 77 / 80 / 86 / 66, $9.07/1k tasks, but time per task is **15.5s** (not 15.8s). Nimble 74 @ $46.14 (24.2s); DeepSeek 69 @ $8.47 (22.2s); Exa Search (auto, dynamic highlights) 80 @ $53.17 (36.5s). All other figures confirmed. | https://artificialanalysis.ai/agents/search-api |
| Cloudflare Web Search providers (updated 2026-10-02): Ceramic.ai $0.25 (default, ZDR yes, 40B+ pages), Exa $7.00 (ZDR no), Linkup $5.00 (ZDR yes); billed at list price, no markup | CONFIRMED | "Last updated Oct 2, 2026"; Ceramic.ai default, $0.25/1k, ZDR Yes, "more than 40 billion pages"; Exa $7.00, ZDR No; Linkup $5.00, ZDR Yes; "each search is billed at the provider's list API price, with no additional markup" (AI Gateway credits). | https://developers.cloudflare.com/web-search/providers/index.md |
| DeepSeek Search/Fetch $0.75 per 1k successful requests each, "powered by DeepSeek's in-house search engine", 100 QPS search / 25 QPS fetch account-level, count 1-50 | CONFIRMED | $0.75 "Per 1,000 successful requests" for both; "It is powered by DeepSeek's in-house search engine"; Search 100 QPS, Fetch 25 QPS at account level (fetch also per-domain limit); count "between 1 and 50", default 10. | https://api-docs.deepseek.com/guides/search |
| Octen pricing: Web Search (FAST) $1/1K beside $5/1K with "80% Off", $0.5/1K full-content, $5 free balance, QPS tiers to 1M+, enterprise ZDR, no invite-only language | CONFIRMED | "$1$5/ 1k calls" with "80% Off" label; "$0.5/ 1k results(full content)" (10 free per call); "$5 in free balance" on signup; tiers 20/50/200/500 QPS and Enterprise "1M+ QPS"; ZDR listed under Enterprise; no invite-only/waitlist wording (only "Early Access" on Video Search / Multimodal Chat). | https://octen.ai/pricing |
| Nimble pricing: Search API $1.1/1K, 5,000 free requests/month, Extract/Crawl/Map $1/1K, plans $2,500-$15,000/month; no $5/1K figure | CONFIRMED | Search API "$1.1 /1k requests"; "5,000 free requests per month"; Extract/Crawl/Map "$1 /1k requests"; Startup $2,500, Scale $7,000, Professional $15,000 /month (billed annually), Enterprise custom; no "$5 per 1K" figure present. | https://www.nimbleway.com/pricing |
