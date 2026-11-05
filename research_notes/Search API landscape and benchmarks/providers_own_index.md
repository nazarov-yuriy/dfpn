# Web-search API providers that operate their OWN crawler and index (catalogue as of 2026-11-05)

Scope: providers whose search API is (or claims to be) served from an index they crawl and build themselves, rather than wrapping Google/Bing SERPs. Exa and Keenable are covered by other researchers and appear only as one-line rows. Every price and claim below carries the date of the page or article it came from; pages marked "fetched 2026-11-05" were read live on that date. Where a provider does not disclose its index source, that is stated explicitly together with the evidence.

Method note: WebSearch and WebFetch of primary docs/pricing pages, engineering blogs, funding press, Wikipedia, GitHub and the Artificial Analysis Search API leaderboard. The shared WebSearch budget was exhausted near the end of the run, so a handful of final checks (You.com index-size statements, Andi primary source, Linkup/Valyu official MCP pages, Alexandria.org liveness) could not be completed and are listed as gaps.

## Classification context and the independent benchmark baseline (Artificial Analysis Search Index)

### Takeaway
There is now one controlled, third-party benchmark that spans most providers (Artificial Analysis Search Index, data dated Oct 19, 2026). Among own-index providers it ranks Perplexity (80), Octen (77), Parallel (75), Brave LLM-context (75), You.com (74), Nimble (74) and Firecrawl (73); Exa (80) tops the table. Microsoft's retirement of the Bing Search API in August 2025 is the market event that pushed developers toward these independent indexes.

### Cited Findings
- The Artificial Analysis Search Index is "the equal-weighted mean of DeepSearchQA F1, BrowseComp accuracy, and AA-Omniscience accuracy, on a 0-100 scale"; every run uses the same candidate model (GPT-5.6 Luna, medium) and harness, only the search provider changes; the page covers 26 Search API products from 14 providers, latest data Oct 19, 2026 — [Artificial Analysis Search API leaderboard](https://artificialanalysis.ai/agents/search-api); methodology at [AA methodology](https://artificialanalysis.ai/methodology/search-api)
- Leaderboard rows (Search Index / DeepSearchQA / BrowseComp / AA-Omniscience / cost per task / time per task), Oct 19, 2026: Exa (auto, dynamic highlights) 80/86/83/73/$0.0638/36.9s; Perplexity Search (medium) 80/81/87/72/$0.0703/31.4s; Exa (lite) 79; Perplexity (high) 79/81/86/71/$0.0663/29.4s; Octen Search (highlights) 77/80/86/66/$0.0236/15.8s; Parallel Search (advanced) 75/81/77/67/$0.0586/40.0s; Brave Search (LLM context) 75/78/77/69/$0.0789/22.8s; OpenAI Web Search (medium) 74; You.com Search (highlights) 74/77/77/69/$0.0670/21.5s; Nimble Search (standard) 74/76/75/71/$0.0628/24.6s; Firecrawl Search 73/74/74/73/$0.0421/61.9s; DeepSeek Search (summary) 69; model-only baseline 33 — [Artificial Analysis Search API leaderboard](https://artificialanalysis.ai/agents/search-api)
- An earlier AA snapshot (launch article dated Aug 18, 2026) had Perplexity Search (medium) alone at the top at 80 "across 9 Search API providers", with Brave LLM context at 75 and You.com and Exa at 74; AA notes Brave was run without the web_fetch tool that other engines received — [AA Search Index launch article](https://artificialanalysis.ai/es/articles/search-api); Parallel's vendor write-up of the same snapshot — [Parallel: Brave vs Parallel](https://parallel.ai/articles/brave-search-api-vs-parallel.md)
- "Microsoft announced in May 2025 the retirement of its [Bing Search] API, taking place in August 2025" — [Brave API guide, updated Oct 16, 2025](https://brave.com/search/api/guides/what-sets-brave-search-api-apart/); Sacra also dates the Bing public API deprecation to August 2025 — [Sacra: Tavily](https://sacra.com/research/tavily)
- searchenginemap.com classifies engines as yellow (independent crawler-based index, where a crawler "could be uniquely identified by a webmaster"), orange (index without a provable independent crawler) and green (metasearch), and excludes Google Custom Search engines — [searchenginemap.com](https://www.searchenginemap.com/) (the interactive map's engine labels were not readable in the fetched text)

### Inferences
- The "crawler identifiable by a webmaster" test used by searchenginemap.com is a practical criterion for this catalogue: Brave, Mojeek (MojeekBot), Perplexity (PerplexityBot), Valyu (HenkBot), Yep (AhrefsBot), Marginalia, Stract, Mwmbl and Kagi (Teclis) pass it; Tavily, Jina, Nimble, Firecrawl's general web search, Felo and Critique Labs publish no crawler identity, which is the main evidence that their index source is undisclosed or third-party.
- AA cost-per-task differences are dominated by the LLM tokens the returned content consumes, not list price, which is why Octen ($0.0236/task) and Firecrawl ($0.0421) look cheap despite similar or higher per-query prices than Perplexity fast.

### Gaps
- The AA leaderboard page lists 26 products, but only 13 rows were extractable; Tavily's, Linkup's, Valyu's, Kagi's and Mojeek's AA scores (if tested) were not captured.
- searchenginemap.com's actual engine-by-engine classification could not be read from the fetched page text.

## Brave Search API

### Takeaway
Brave is the largest Western independent index available through an open API: Brave's own guide says "over 30 billion pages" growing by 100M+ pages/day (Oct 2025), while its 2026 pages stop quoting a size ("index size is a vanity stat"). Pricing was consolidated on Feb 12, 2026 to $5/1k for Search (including the new LLM Context endpoint) and $4/1k plus $5/M tokens for Answers, with $5 free credit/month; Brave LLM Context scores 75 on the Artificial Analysis Search Index.

### Cited Findings
- Who: Brave Search was built after Brave acquired Tailcat (from Cliqz, a Hubert Burda Media subsidiary); beta June 2021, full release June 2022; ended reliance on Bing for web search in April 2023 and launched its own image/video index in August 2023; 1.6 billion monthly searches in September 2025; API announced May/June 2023 — [Wikipedia: Brave Search](https://en.wikipedia.org/wiki/Brave_Search)
- Index size/freshness: "over 30 billion pages", "grows by over one hundred million new and refreshed pages each day"; "95% of requests return in under one second"; "more than 50 million searches per day"; free tier of 2,000 queries/month and paid plans "begin at $3 CPM" (page published Sept 22, 2023, last updated Oct 16, 2025 — the pricing is now superseded) — [Brave: What sets Brave Search API apart](https://brave.com/search/api/guides/what-sets-brave-search-api-apart/)
- Third-party claim of "over 40 billion pages as of February 2026" (not found on any Brave page) — [Firecrawl blog](https://www.firecrawl.dev/blog/brave-search-api-alternatives)
- Independence: "Zero dependencies on Google or Bing"; "Every result comes from Brave's own independent index" with no fallback; data from Brave's own crawler plus opt-in signals from the Web Discovery Project; "signals from 130+ million real humans"; "Index size is a vanity stat"; coverage "99.9% of the web that matters"; Brave calls itself "the only fully-fledged search index available through an open API" (fetched 2026-11-05) — [Brave Search API homepage](https://brave.com/search/api/)
- Web Discovery Project: Brave browser users can opt in to "contribute anonymous data about searches and webpage visits" — [Brave API guide](https://brave.com/search/api/guides/what-sets-brave-search-api-apart/)
- Pricing (fetched 2026-11-05): Search $5 per 1,000 requests (covers Web, LLM Context, Images, News, Videos), 50 QPS, Goggles, extra alternate snippets, schema-enriched results; Answers $4 per 1,000 requests plus $5 per million input and output tokens, 2 QPS, citations, streaming, OpenAI-SDK compatible; Spellcheck and Autocomplete $5 per 10,000; every plan includes $5 free credit per month (homepage hero also says "Up to $20 in free calls every month" — internal inconsistency); Enterprise custom; storage/training rights depend on plan — [Brave Search API homepage](https://brave.com/search/api/); [Brave blog, Feb 12, 2026](https://brave.com/blog/most-powerful-search-api-for-ai/)
- LLM Context API (launched Feb 12, 2026; blog updated June 25 and Sept 17, 2026): returns "smart chunks" with "data-first ranking" (structured data, code, forum posts, YouTube captions), `maximum_number_of_tokens` budget, Goggles re-ranking, local/POI results, "a total latency under 500ms at p90", and "powering over 22 million answers per day in Brave Search"; Brave describes itself as "one of only three independent, global-scale search indexes in the western world" and "the only one outside of Big Tech" — [Brave blog](https://brave.com/blog/most-powerful-search-api-for-ai/)
- LLM Context token budget 1k to ~33k tokens; `context_threshold_mode` strict/balanced/lenient; 24-hour freshness filter; every source carries URL, timestamp and last-fetch time — [Brave Search API homepage](https://brave.com/search/api/)
- Filters (from Brave's MCP tool list): web, local, image, video, news search, summarizer, LLM context and place search tools — [brave/brave-search-mcp-server](https://github.com/brave/brave-search-mcp-server)
- Benchmarks (vendor): Answers plan "state-of-the-art 94.1% F1-score on SimpleQA"; Nov 2025 Ask Brave eval (1,500 queries, Claude Opus 4.5/Sonnet 4.5 judges): Grok 4.71 rating, Ask Brave 4.66, Google AI Mode 4.39, ChatGPT 4.32, Perplexity 4.01; June 2026 Elo: Ask Brave 1169, Grok 1157, Google AI Mode 1000, ChatGPT 880, Perplexity 695 — [Brave blog](https://brave.com/blog/most-powerful-search-api-for-ai/); secondary coverage — [ppc.land](https://ppc.land/braves-5-search-api-wins-ai-answer-test-as-perplexity-finishes-last/)
- Benchmarks (third-party): AA Search Index 75 (DeepSearchQA 78, BrowseComp 77, AA-Omniscience 69), $0.0789/task, 22.8 s/task, Oct 19, 2026 — [Artificial Analysis](https://artificialanalysis.ai/agents/search-api); Perplexity's Sept 2025 eval measured Brave p50 513 ms / p95 808 ms and SimpleQA .822, FRAMES .320, BrowseComp .221, HLE .191 — [Perplexity research post](https://www.perplexity.ai/hub/blog/architecting-and-evaluating-an-ai-first-search-api); Parallel's July 2026 test: Brave 38.3% BrowseComp at 430 ms — [Parallel benchmark report](https://parallel.ai/articles/best-web-search-api-for-ai-applications.md)
- MCP: `brave/brave-search-mcp-server` in Brave's GitHub org exposes `brave_web_search`, `brave_local_search`, `brave_image_search`, `brave_video_search`, `brave_news_search`, `brave_summarizer`, `brave_llm_context`, `brave_place_search`; STDIO default, HTTP optional; 1.6k stars — [GitHub](https://github.com/brave/brave-search-mcp-server)

### Inferences
- The 2023-2025 guide (30B pages, $3 CPM, 2,000 free queries) and the Feb 2026 pages ($5/1k flat, $5 credits, no index-size figure) describe two different pricing eras; anyone quoting "$3 CPM" or "2,000 free queries" is using the pre-Feb-2026 structure.
- Brave's "one of only three independent global-scale indexes in the western world" implies Google, Bing and Brave; it implicitly excludes Mojeek, Yep and Perplexity from "global-scale", which is a vendor framing, not an independent finding.

### Gaps
- No Brave primary source for the "40 billion pages" figure circulating in 2026; Brave's own pages have stopped stating a page count.
- Brave's API Terms about storing results were only seen via third-party summaries, not the terms page itself.

## Mojeek

### Takeaway
Mojeek (Brighton, UK; crawler MojeekBot) is the oldest independent Western index after Google/Bing, reporting 9 billion pages in 2025 (up from 8B in 2024), and sells a straightforward pay-as-you-go Web Search API at £2/1k (Startup, 10 results) and £3/1k (Business, 40 results), with EU-only infrastructure as its main differentiator; it publishes no benchmarks or latency figures and has no known MCP server.

### Cited Findings
- Index milestones (Mojeek about page, fetched 2026-11-05): 3B pages (2020), 6B (2022), 7B (2023), 8B (2024), "passing 9 billion pages in 2025"; crawler MojeekBot; office at Sussex Innovation Centre, Brighton; hosted at the Custodian data centre — [Mojeek: About](https://www.mojeek.com/about/)
- Wikipedia corroborates earlier points: "over 2.3 billion pages" (May 2019), 6 billion (Oct 2022); started 2004 as Marc Smith's personal project, incorporated 2009; uses its own crawler-based index rather than Google/Bing results; no tracking or personalization — [Wikipedia: Mojeek](https://en.wikipedia.org/wiki/Mojeek)
- Web Search API pricing (fetched 2026-11-05): Startup £2 per 1,000 requests, 5 QPS, 100,000 queries/day, up to 10 results/request, results cacheable 1 hour; Business £3 per 1,000, 10 QPS, 400,000/day, up to 40 results, indefinite storage allowed; Enterprise custom, up to 100 results; pay-as-you-go, no minimum, free credit on Startup (amount unstated), card required — [Mojeek Web Search API](https://www.mojeek.com/services/search/web-search-api/)
- Older API page lists a "Personal" tier at "£1* CPM" and says to enquire for full pricing — [Mojeek API services](https://www.mojeek.com/services/api.html)
- Features: "Global index with billions of fresh webpages"; country and language boosting; ranking and site clustering; configurable title/description lengths; optional SafeSearch; keyword and semantic scores on custom plans; 90-day retention standard, Zero Data Retention on request; "Unique European data sovereignty", "Zero Sub-Processors", infrastructure "owned and operated in Europe"; MojeekBot respects robots.txt — [Mojeek Web Search API](https://www.mojeek.com/services/search/web-search-api/)
- Site Search API tiers (1,000/5,000/10,000/unlimited pages) are "POA" — [Mojeek Site Search API](https://www.mojeek.com/services/search/site-search-api/)
- Kagi lists Mojeek-class engines only generically ("all major search result providers worldwide"), so Mojeek's role as a Kagi source is not confirmed by Kagi's page — [Kagi search sources](https://help.kagi.com/kagi/search-details/search-sources.html)

### Inferences
- At ~9B pages Mojeek is roughly 1/3 of Brave's last stated size and ~1/20 of Perplexity's 200B-URL claim, but it is the only one of the three that publishes a year-by-year page count.
- The £ pricing and EU-sovereignty framing position Mojeek for GDPR-sensitive buyers rather than for the agentic-search benchmark race.

### Gaps
- No published benchmark scores, no latency claims, no documented LLM-context or content-extraction mode, and no MCP server were found.
- Request-parameter documentation (filters by date/language) was linked but not readable from the fetched page.

## Kagi (Teclis, TinyGem, Search API, Enrichment API, FastGPT)

### Takeaway
Kagi is a hybrid: its own Teclis (web) and TinyGem (news) indexes are small-web/non-commercial complements, blended with "anonymized API calls to all major search result providers" plus Marginalia and vertical APIs. The Enrichment API exposes just the own indexes at $2/1k; the full Search API is $12/1k; FastGPT is $15/1k; Kagi publishes an official MCP server.

### Cited Findings
- Sources: own web index Teclis, own news index TinyGem, "anonymized API calls to all major search result providers worldwide", Marginalia, Wolfram Alpha, Apple, Wikipedia, Open Meteo, Yelp, TripAdvisor and others; a query typically calls "a dozen or so different sources simultaneously"; no proportion stated — [Kagi: Search sources](https://help.kagi.com/kagi/search-details/search-sources.html)
- Enrichment API: "$2/1000 searches ($0.002 USD per search)", billed only when non-zero results return; `GET /enrich/web` (Teclis, "non-commercial websites and 'small web' discussions", Kagi's "secret sauce") and `GET /enrich/news` (TinyGem); "best used in combination with a general results index"; response fields `rank`, `url`, `title`, `snippet`, `published` — [Kagi Enrichment API](https://help.kagi.com/kagi/api/enrich.html)
- Search API pricing (fetched 2026-11-05): "$12 /1k requests"; Extract API "$4 /1k pages" — [kagi.com/api/pricing](https://kagi.com/api/pricing)
- Search API v1: `POST https://kagi.com/api/v1/search` with Bearer key; inherits account personalization (site blocking/promotion, snippet length); legacy v0 documented separately — [Kagi Search API](https://help.kagi.com/kagi/api/search.html)
- FastGPT: "1.5¢ per query ($15 USD per 1000 queries)" with web search enabled; prepaid credits — [Kagi FastGPT](https://help.kagi.com/kagi/api/fastgpt.html)
- Billing: pay-per-use prepaid credit, invoiced at $100 or monthly; Universal Summarizer not yet in v1 — [Kagi API overview](https://help.kagi.com/kagi/api/overview.html)
- Third-party price claims conflict ($2.50/1k; "$15-$25 per 1k") and should be disregarded in favour of kagi.com/api/pricing — [CostBench](https://costbench.com/software/ai-search-apis/kagi-search-api/)
- MCP: Kagi publishes `kagimcp` (web, news, video, podcast, image search plus page extraction), hosted at mcp.kagi.com or run locally via uvx — [mcp.so: kagimcp](https://mcp.so/zh/servers/kagimcp)

### Inferences
- Because the full Search API blends third-party providers, only the Enrichment API qualifies as a pure "own index" product; at $2/1k it is the cheapest way to query a proprietary small-web index.
- The $12/1k Search API price is above Brave ($5), Perplexity ($5/$1) and Parallel ($1-5), consistent with Kagi paying upstream provider fees.

### Gaps
- Teclis/TinyGem index sizes are not disclosed anywhere found.
- The Search API's beta/invite status (claimed by some third-party pages) is not stated on Kagi's current pages; the pricing page simply lists it.

## Perplexity Search API

### Takeaway
Launched Sept 25, 2025, Perplexity's Search API is served from its own PerplexityBot-built index that it says "tracks over 200 billion unique URLs" with "tens of thousands of indexing operations per second". It costs $5/1k (default) or $1/1k (`search_type: "fast"`), claims p50 358 ms / p95 763 ms, and leads or co-leads the Artificial Analysis Search Index at 80 (medium).

### Cited Findings
- Launch Sept 25, 2025; index covers "hundreds of billions of webpages"; "Each second, our systems process tens of thousands of index update requests"; documents split into sub-document units "individually surfaced and scored"; open-source `search_evals` framework — [Perplexity: Introducing the Search API](https://www.perplexity.ai/hub/blog/introducing-the-perplexity-search-api)
- Research post (Sept 25, 2025): "Our search index tracks over 200 billion unique URLs, with capacity to track many hundreds of billions more"; exabyte-scale, tens of thousands of CPUs, hundreds of TB of RAM; an ML model decides which URLs to index and when; PerplexityBot follows robots.txt; hybrid lexical + semantic retrieval, multi-stage ranking with cross-encoder rerankers, document- and span-level scoring — [Perplexity research post](https://www.perplexity.ai/hub/blog/architecting-and-evaluating-an-ai-first-search-api)
- Latency (ms, from AWS us-east-1; vendor-run): Perplexity p50 358 / p75 443 / p90 604 / p95 763; Brave 513/637/728/808; "SERP-based (Tavily)" 1342/1586/1743/1790; Exa 1375/1499/1798/2188 — [Perplexity research post](https://www.perplexity.ai/hub/blog/architecting-and-evaluating-an-ai-first-search-api)
- Quality (vendor-run, scores): Perplexity SimpleQA .930, FRAMES .453, BrowseComp .371, HLE .288; Tavily .890/.437/.348/.248; Brave .822/.320/.221/.191; Exa .781/.399/.265/.242 — [Perplexity research post](https://www.perplexity.ai/hub/blog/architecting-and-evaluating-an-ai-first-search-api)
- Pricing (fetched 2026-11-05): Search API $5.00 per 1k successful requests (default), $1.00 per 1k with `search_type: "fast"` ("lower-latency results in the same response format"); one request may carry up to five queries as one billing unit; Agent API `web_search` tool $2.50/1k standard, $1.00/1k fast — [Perplexity pricing docs](https://docs.perplexity.ai/getting-started/pricing)
- Crawlers: PerplexityBot "surfaces and links websites in Perplexity search results" and "is not used to crawl content for AI foundation models"; Perplexity-User fetches pages on user request and generally ignores robots.txt — [Perplexity bots guide](https://docs.perplexity.ai/guides/bots)
- Third-party benchmark: AA Search Index 80 (medium: DeepSearchQA 81, BrowseComp 87, AA-Omniscience 72; $0.0703/task; 31.4 s) and 79 (high), Oct 19, 2026 — [Artificial Analysis](https://artificialanalysis.ai/agents/search-api); Parallel's Sept 2026 report says Perplexity "led the low-cost tier at 46%" BrowseComp — [Parallel report](https://parallel.ai/articles/most-powerful-search-api-for-ai.md)
- Outlier third-party index claims ("~300B pages"; "~5 billion URLs") contradict Perplexity's 200B-URL statement and are unreliable — [search summary citing ai2.work and others](https://ai2.work/blog/ai-tech-perplexity-search-api-2025)
- MCP: official `perplexityai/modelcontextprotocol` server exposing Sonar search/research tools and the Search API — [LobeHub listing](https://lobehub.com/en/mcp/perplexityai-modelcontextprotocol)

### Inferences
- "200 billion unique URLs tracked" is a URL-graph figure, not necessarily full-text indexed pages; it is not directly comparable to Brave's "30B pages" or Mojeek's "9B pages".
- Perplexity labelling Tavily "SERP-based" in a published benchmark is independent-of-Tavily evidence that Tavily was, at least in Sept 2025, serving results via third-party SERPs.

### Gaps
- The rate-limits page (free tier / usage tiers) returned 404; free-credit terms could not be confirmed from a primary source.
- No independently measured latency for the Search API in 2026 was found (AA reports time-per-task, not raw search latency).

## You.com Search API

### Takeaway
You.com sells a Web Search API at $5/1k (flat for 1-100 results since Mar 12, 2026; previously $6.25-$8/1k), a Contents API at $1/1k pages (cut from $10), Research tiers from $12 to $1,200/1k and a Finance Research API on a "purpose-built financial index"; it scores 74 on the AA Search Index. Whether its general web results come entirely from its own crawl is undisclosed: You.com describes "improved crawling, extraction, and serving" and bills only live crawls, but publishes no index size or crawler name.

### Cited Findings
- Pricing (fetched 2026-11-05): Web Search API $5.00 per 1,000 calls, up to 100 results/call; full-page extraction add-on $1.00 per 1,000 pages billed only for pages crawled live (source modes `blend` default, `cache`, `fetch`); Contents API $1.00/1k pages; Research API per 1k: lite $12, standard $50, deep $100, exhaustive $450, frontier $1,200 (background only); Finance Research API deep $110, exhaustive $500; "Knowledge results from licensed data providers at no extra cost"; Finance "searches a purpose-built financial index" — [You.com billing docs](https://you.com/docs/administration/billing)
- Price cut effective Mar 12, 2026: Web Search from $6.25/1k (1-50 results) and $8.00/1k (50-100) to $5.00 flat; Contents from $10.00 to $1.00/1k; attributed to "infrastructure optimizations, including improved crawling, extraction, and serving of page content"; "Nothing was removed or downgraded" — [You.com: Lower Search API cost](https://about.you.com/resources/lower-search-api-cost)
- A 100-calls/day free tier was added to the Web Search API on July 29, 2026, with $5.00/1k thereafter (third-party tracker; You.com docs had not yet reflected it) — [UsagePricing change log](https://www.usagepricing.com/blueprint/activity/you-com-2026-07-29-web-search-free-tier)
- MCP: live Web Search is free through You.com's MCP server by appending `?profile=free` to the server path; agents can call the API "with no account and no key" — [You.com billing docs](https://you.com/docs/administration/billing)
- Response fields `title`, `description`, `url`, `site_name`, `age`; `count` parameter; a separate Contents API returns full text; article dated 2026-10-01 — [You.com: AI search API explainer](https://you.com/resources/ai-search-api)
- Third-party benchmark: AA Search Index 74 (DeepSearchQA 77, BrowseComp 77, AA-Omniscience 69; $0.0670/task; 21.5 s), Oct 19, 2026 — [Artificial Analysis](https://artificialanalysis.ai/agents/search-api); a You.com teaser cites "95.17% on SimpleQA" for an endpoint/mode combination (not detailed) — [You.com pricing post](https://about.you.com/resources/lower-search-api-cost)
- Contents example endpoints use the `ydc-index.io` domain (per third-party pricing page), suggesting You.com-branded index infrastructure — [CostBench You.com](https://costbench.com/software/ai-search-apis/you-com-api/)

### Inferences
- "Only pages crawled live are billed" plus "cache coverage varies by how recently pages were crawled" indicates You.com maintains its own page cache/crawl, but nothing published rules out blending third-party web indexes; treat You.com's general web index as partially disclosed.
- The Finance Research API is the only You.com product explicitly described as running on a You.com-built index.

### Gaps
- No index size, freshness or crawler user-agent published; the planned search for "You.com own index" statements could not run (search budget exhausted).
- ARI (You.com's research agent) was not researched beyond the Research API price tiers above.

## Parallel.ai (Parallel Web Systems)

### Takeaway
Parallel says it runs a "proprietary web-scale index" covering "billions of public web pages" with "millions added or updated daily", and returns token-dense "excerpts" rather than snippets. Search is $1/1k (turbo/fast) or $5/1k (basic/advanced) for 10 results, Extract $1/1k URLs, Task API $5-$2,400/1k runs; it raised a $100M Series B at $2B (Sequoia, Apr 2026) and scores 75 (advanced) on the AA Search Index.

### Cited Findings
- Index: "Parallel's index covers billions of public web pages and adds or updates millions daily"; recrawls pages for freshness; crawler respects robots.txt — [Parallel Search product page](https://parallel.ai/ai/products/search); index covers web pages from "more than 30 countries" and many languages (Korean, Chinese, Japanese, Spanish, Hindi, German, Arabic, Portuguese, Russian); Advanced mode reranks and compresses "across general and specialized indexes" — [Parallel Search API blog](https://parallel.ai/blog/parallel-search-api)
- Excerpts: "query-relevant passages compressed to be token-efficient"; dense snippets or full page content as Markdown; `max_chars_per_result` (example 10,000) — [Parallel Search product page](https://parallel.ai/ai/products/search)
- Modes/latency/price: Turbo ~200 ms, $1/1k; Fast ~700 ms, $1/1k; Basic ~1 s, $5/1k; Advanced ~3 s, $5/1k; Basic P50 under 1 s and P90 under 2 s, Advanced P50 ~3 s — [Parallel Search product page](https://parallel.ai/ai/products/search); [Parallel blog](https://parallel.ai/blog/parallel-search-api)
- Pricing (fetched 2026-11-05): Search $1 per 1k (turbo/fast) or $5 per 1k (basic/advanced), 10 results per request, additional results/excerpts $1 per 1k; Extract $1 per 1,000 URLs; Task API per 1k successful runs: lite $5, base $10, core $25, core2x $50, pro $100, ultra $300, ultra2x $600, ultra4x $1,200, ultra8x $2,400 — [Parallel pricing docs](https://docs.parallel.ai/getting-started/pricing); "Up to 80,000 free search requests to start"; rate limit 600 requests/minute — [Parallel Search product page](https://parallel.ai/ai/products/search)
- Filters: include/exclude domains; `max_age` (hours, default 24) triggers live crawl; `fetch_timeout` (default 90 s); live fetch on/off; premium extraction for PDFs, JS-heavy and CAPTCHA-protected sites; no date filter mentioned — [Parallel Search product page](https://parallel.ai/ai/products/search)
- Vendor benchmarks (Sept 9, 2026; 100/50/100 samples): SimpleQA Verified Advanced 97% at 28.3 CPM, Basic 97% at 45 CPM, Fast 94% at 2 CPM, Turbo 91% at 2 CPM (competitors 91-94% at 7.9-61.3 CPM); BrowseComp Advanced 74% at 399 CPM, Basic 72% at 612 CPM, Fast 44%, Turbo 32% (competitors 32-70% at 53.4-971 CPM); WideSearch Advanced 57.6, Basic 55.3 (competitors 47.9-55.9) — [Parallel Search product page](https://parallel.ai/ai/products/search)
- Vendor benchmark reports: July 10-12, 2026: Parallel Turbo 216 ms p50 and 51% BrowseComp vs Exa Instant 33.7% at 361 ms, Tavily Ultra Fast 19.3% at 357 ms, Brave 38.3% at 430 ms — [Parallel: best web search API report](https://parallel.ai/articles/best-web-search-api-for-ai-applications.md); Sept 2026: Parallel Basic 72% at $612/1k questions, Exa Auto 70% at $971, Tavily 66% at $935; Parallel admits it is "biased toward our own product" — [Parallel: BrowseComp report](https://parallel.ai/articles/most-powerful-search-api-for-ai.md)
- Third-party benchmark: AA Search Index 75 (advanced: DeepSearchQA 81, BrowseComp 77, AA-Omniscience 67; $0.0586/task; 40.0 s), Oct 19, 2026 — [Artificial Analysis](https://artificialanalysis.ai/agents/search-api)
- Funding: $100M Series B at $2B valuation led by Sequoia (TechCrunch, Apr 29, 2026), five months after a $100M Series A at ~$740M; Kleiner Perkins, Index Ventures, Khosla participated; total ~ $230M; founder Parag Agrawal (ex-Twitter CEO) — [TechCrunch](https://techcrunch.com/2026/04/29/parallel-web-systems-hits-2b-valuation-five-months-after-its-last-big-raise/); [Seedtable](https://seedtable.com/companies/parallel-web-systems/funding-rounds/series-b-2026-04)
- MCP: hosted search MCP server at `search-mcp.parallel.ai/mcp` — [mcp.so listing](https://mcp.so/servers/search-mcp-parallel-web)

### Inferences
- Parallel does operate its own crawl (robots.txt-respecting crawler, recrawl schedule, live-fetch via `max_age`), but the "general and specialized indexes" phrasing in its blog leaves open whether some candidates come from licensed/third-party indexes; no crawler user-agent string was found, which is unusual for a provider claiming a proprietary web-scale crawl.
- "Billions of pages" is one to two orders of magnitude below Brave (30B+) and Perplexity (200B URLs); Parallel's pitch rests on excerpt compression and objective-driven ranking rather than raw index breadth.

### Gaps
- No crawler user-agent, exact page count or freshness SLA published.
- Free-credit terms differ between the product page (80,000 free requests) and the pricing docs (not stated); not reconciled.

## Tavily

### Takeaway
Tavily (founded 2023, acquired by Nebius for a reported $275M in Feb 2026) does not disclose its index source; Sacra states flatly that it "does not maintain its own search index" and fans out to multiple engines in real time, Perplexity classed it as "SERP-based", while Tavily's own blog speaks of an "agent-native index" plus dynamic caching. Pricing is credit-based ($0.008/credit PAYG; 1,000 free credits/month; basic/fast/ultra-fast 1 credit, advanced 2 credits).

### Cited Findings
- Pricing (fetched 2026-11-05): Researcher (free) 1,000 credits/month, no card; Pay As You Go $0.008 per credit; Project $30/month for 4,000 credits (slider text garbled); Enterprise custom; 100k free credits for startups; free for students; credits reset monthly — [Tavily pricing](https://www.tavily.com/pricing); Brave's guide describes Tavily's PAYG as "starting at $8 CPM" — [Brave API guide](https://brave.com/search/api/guides/what-sets-brave-search-api-apart/)
- Search parameters (fetched 2026-11-05): `search_depth` = `basic` (default), `advanced` (2 credits, multiple snippets/URL), `fast`, `ultra-fast` (one NLP summary/URL); `max_results` 0-20 (default 10); `include_domains` up to 300 with `restrict`/`prefer` modes; `exclude_domains` up to 150; `country` boost; `language` boost or strict `filter_by_language`; `time_range` day/week/month/year; `start_date`/`end_date`; `max_age_hours` (-1 to 720) controls cached-copy age vs live fetch; `include_raw_content` (markdown/text); `include_answer` basic/advanced; `auto_parameters`; `exact_match`; `topic` general/news/finance; `chunks_per_source` 1-3 — [Tavily search endpoint reference](https://docs.tavily.com/documentation/api-reference/endpoint/search)
- Index source: Tavily's About page describes Search, Extract, Crawl, Map and Research endpoints but says nothing about an index, crawler or aggregation — [Tavily docs: About](https://docs.tavily.com/documentation/about); Sacra: Tavily "does not maintain its own search index" and "fans out to multiple data sources and search engines in real time" — [Sacra: Tavily](https://sacra.com/research/tavily); Tavily blog claims low latency "powered by dynamic caching and an agent-native index" — [Tavily 101](https://tavily.com/blog/tavily-101-ai-powered-search-for-developers); Perplexity labelled Tavily "SERP-based" in its Sept 2025 benchmark — [Perplexity research post](https://www.perplexity.ai/hub/blog/architecting-and-evaluating-an-ai-first-search-api)
- Ownership/funding: founded 2023; $5M seed July 2024; $20M Series A Aug 2025 led by Insight Partners and Alpha Wave Global; Nebius agreed to acquire Tavily for $275M (Feb 10, 2026), ~98x 2025 revenue per Sacra; Tavily keeps its brand and CEO Rotem Weiss joins Nebius — [Sacra](https://sacra.com/research/tavily); [Nebius newsroom](https://nebius.com/newsroom/nebius-announces-agreement-to-acquire-tavily-to-add-agentic-search-to-its-ai-cloud-platform); [SiliconANGLE, Feb 10, 2026](https://siliconangle.com/2026/02/10/ai-infrastructure-giant-nebius-buys-agentic-search-startup-tavily/)
- Benchmarks (all third-party or competitor-run): Perplexity Sept 2025: Tavily SimpleQA .890, FRAMES .437, BrowseComp .348, HLE .248; p50 1,342 ms, p95 1,790 ms — [Perplexity research post](https://www.perplexity.ai/hub/blog/architecting-and-evaluating-an-ai-first-search-api); Parallel July 2026: Tavily Ultra Fast 19.3% BrowseComp at 357 ms; Sept 2026: 66% at frontier tier ($935/1k Q), 32% low-cost tier ($176) — [Parallel report](https://parallel.ai/articles/most-powerful-search-api-for-ai.md)
- MCP: `tavily-ai/tavily-mcp` covering search, extract, map and crawl — [search summary via mcp.so](https://mcp.so/servers/search-mcp-parallel-web)

### Inferences
- The weight of external evidence (Sacra, Perplexity's "SERP-based" label, absence of any crawler user-agent or robots.txt page) indicates Tavily is a real-time aggregator with a cache layer rather than an independent crawl; `max_age_hours` describes cache freshness, not crawl freshness.
- Nebius ownership gives Tavily the capital to build an index, but nothing published since Feb 2026 says it has.

### Gaps
- No Tavily primary statement on index source, crawler, or index size; Tavily's AA Search Index score was not captured.

## Linkup

### Takeaway
Paris-based Linkup (US$10M seed led by Gradient, Feb 2026) says results come from "our index" built with a proprietary retrieval model and augmented by paid partnerships with "premium data providers"; it prices standard calls at $0.005 ($0.006 with sourced answer/structured output) and deep at $0.05/$0.055, gives $20 free credit monthly, and self-reports a 94% F-score on Verified SimpleQA, "first among sub-second web search APIs".

### Cited Findings
- Pricing (fetched 2026-11-05): standard depths (`flash`, `fast`, `standard`) $0.005 per call for `searchResults`, $0.006 for `sourcedAnswer`/`structured`; `deep` $0.05 / $0.055; $20 free credit for professional-email accounts, topped up to $20 monthly for eligible accounts — [Linkup pricing](https://docs.linkup.so/pages/documentation/platform/pricing)
- Index: results come from "the index"/"our index"; "proprietary retrieval model" plus "selected third-party LLMs" for standard/deep; Linkup "partners with premium data providers" for snippet quality and freshness (providers unnamed) — [Linkup FAQ](https://docs.linkup.so/pages/faq/faq.md); third-party reviews describe revenue-sharing deals with premium publishers — [search summary via aitoolsatlas](https://aitoolsatlas.ai/tools/linkup-ai/review)
- Benchmarks (self-reported): Verified SimpleQA 94% F-score, first among sub-second web search APIs ahead of Perplexity Sonar Pro, Exa and Tavily; Research endpoint first on SealQA-0 at 61%; evaluation harness open source — [Linkup FAQ](https://docs.linkup.so/pages/faq/faq.md); older third-party copies cite 92% or 91% F-score — [search summary via doolpa/aitoolsatlas](https://doolpa.com/article/linkup-search-api)
- Latency: `flash` "under 200 ms", `fast` about one second — [Linkup FAQ](https://docs.linkup.so/pages/faq/faq.md)
- Cost benchmark (May 12, 2026, 200 enterprise queries, cost only): Linkup $5.90/1k standard, $59/1k deep; Exa ~$15 (search+contents), ~$25 (/answer), ~$400 (/research); Linkup ~64% cheaper than Tavily; Perplexity token-based and estimated — [Linkup blog](https://linkup.so/blog/cheapest-ai-search-api-benchmark)
- Funding: $10M seed led by Gradient announced Feb 3, 2026; prior €3M (Nov 2024); offices Paris, New York, San Francisco; launched `/fast` sub-second tier — [AccessNewswire release](https://www.accessnewswire.com/newsroom/en/business-and-professional-services/linkup-raises-10m-seed-round-led-by-gradient-to-build-web-search-1132439); [Elaia portfolio](https://www.elaia.com/portfolio/linkup/)

### Inferences
- Linkup's "own index" is asserted but unquantified and no crawler is named; the premium-publisher partnerships suggest a curated/licensed corpus layered on a web index of unknown provenance, so treat "own index" as partially disclosed.
- The SimpleQA figure has climbed from 91% to 94% across Linkup's own materials in 2025-2026, so cite the version and date.

### Gaps
- No index size, crawler name or freshness claim; no official MCP server found in directory searches (not confirmed either way); AA Search Index score not captured.

## Valyu

### Takeaway
Valyu runs its own crawler (HenkBot) and sells a credit-priced DeepSearch API spanning web/news, academic, patents, SEC filings, clinical trials, market data and licensed publishers; current docs price web/news at 100 credits per 1,000 results (about $0.63/1k at pay-as-you-go), with $10-$20 free credit. Index size and benchmarks are not published.

### Cited Findings
- Crawler: "HenkBot" (UA `Mozilla/5.0 (compatible; HenkBot/1.0; +https://valyu.ai/crawler)`) "discovers and indexes web content for search through our APIs"; honors robots.txt, crawl-delay, nofollow/noindex; adaptive rate limiting; content partnerships for access/attribution/commercial terms — [Valyu crawler docs](https://docs.valyu.ai/crawler); Valyu says it is "building the biggest index for AI while making sure content owners get paid" — [search summary via docs.valyu.ai/crawler.md](https://docs.valyu.ai/crawler.md)
- Pricing (fetched 2026-11-05): credits per 1,000 results: web and news 100; arXiv/PubMed/bioRxiv/medRxiv 50; clinical trials 800; stock prices 960; patents 1,280; SEC filings 1,920; Wiley 4,800; Contents API 0.2 credit per extracted URL (+0.2 for summary/structured); DeepResearch instant 8, fast 25, standard 100, heavy 500, max 2,500 credits; pay-as-you-go 1,600 credits per $10 (12-month expiry); plans $29/mo (5,000 credits), $99/mo (18,000), $499/mo (100,000), Enterprise custom; free $10 on signup or $20 with company email, no card — [Valyu pricing docs](https://docs.valyu.ai/pricing)
- An earlier pricing scheme quoted in search summaries listed dollar CPMs (academic $0.50, web $1.50, financial $8.00, proprietary $30-50 per 1k retrievals) and a `max_price` cap; this conflicts with the credit model now on the docs page — [Valyu pricing (older rendering)](https://www.valyu.ai/pricing.md)
- Company page gives mission only ("Search and Deep Research for AI knowledge work"); no funding or team data — [Valyu company](https://valyu.ai/company); Caplight lists total funding of $500,000 (accelerator round Mar 2024) which is likely stale — [Caplight](https://www.caplight.com/company/valyu)

### Inferences
- At PAYG rates, 100 credits ≈ $0.625, making Valyu's web search one of the cheapest own-crawler offerings per 1,000 results, but the unit is "results" not "requests", so a 10-result query costs ~$0.006 (comparable to Brave/Perplexity per query).
- Valyu's differentiation is source breadth (academic, financial, patents, licensed publishers), not web-index scale.

### Gaps
- No index size, freshness or latency claims; no benchmark results; no funding announcement after 2024 found; official MCP server not confirmed.

## Firecrawl /search (and "Alexandria")

### Takeaway
Firecrawl's `/search` (2 credits per 10 results, free 1,000 credits/month) does not disclose what web index it queries; its own-index effort is "Alexandria" (Sept 22, 2026, with a $75M Series B), which is a set of vertical indexes (Research, Developer, Government/Legal; 113M+ sources) plus the live web rather than a general web crawl. Firecrawl Search scores 73 on the AA Search Index.

### Cited Findings
- Billing (fetched 2026-11-05): Search 2 credits per 10 results, rounded up (11 results = 4 credits); scraping returned pages adds per-page scrape cost (1 credit/page, + modifiers); enterprise Zero-Data-Retention search 10 credits/10 results; free plan 1,000 credits/month, 10 rpm on /search; plans Hobby 5,000, Standard 100,000, Growth 500,000, Scale 1,000,000 credits; underlying search engine not named — [Firecrawl billing docs](https://docs.firecrawl.dev/billing); plan prices $19/$99/$399/$749 per month — [Firecrawl pricing](https://www.firecrawl.dev/pricing)
- Alexandria: announced Sept 22, 2026 with $75M Series B led by Smash Capital (Altos, Nexus, Y Combinator, Freestyle, Offline participating); "the knowledge library for superintelligence"; combines live web, official data providers, site connectors and Firecrawl's own Research, Developer and Government indexes; agents using Alexandria scored 21% higher on answer quality across 845 tasks (blind AI judging) — [Firecrawl changelog](https://www.firecrawl.dev/changelog/introducing-alexandria-series-b); 113M+ indexed sources, 457 providers; `/search` accepts `sources: ["web", "alexandria"]` — [Firecrawl Alexandria](https://firecrawl.dev/alexandria)
- Series A $14.5M (Aug 19, 2025) — [TechCrunch](https://techcrunch.com/2025/08/19/ai-crawler-firecrawl-raises-14-5m-is-still-looking-to-hire-agents-as-employees)
- Third-party benchmark: AA Search Index 73 (DeepSearchQA 74, BrowseComp 74, AA-Omniscience 73; $0.0421/task; 61.9 s, the slowest in the table), Oct 19, 2026 — [Artificial Analysis](https://artificialanalysis.ai/agents/search-api)

### Inferences
- Firecrawl is a scraper/crawler company, so it clearly operates crawling infrastructure, but nothing published says its general `web` search source is a Firecrawl-built index; the 61.9 s AA time-per-task is consistent with live fetching of results rather than serving from a pre-built index.

### Gaps
- Underlying engine for `/search` `web` source remains undisclosed in docs; official MCP server not verified in this run.

## Jina (s.jina.ai)

### Takeaway
Jina's `s.jina.ai` returns the top five results with full-page markdown, billed as a fixed token count "starting from 10,000 tokens" per request, with 100 RPM on free/paid keys and ~2.5 s average latency; Jina has never disclosed the search engine or index behind it, and no Jina crawler is documented.

### Cited Findings
- Reader page (fetched 2026-11-05): `s.jina.ai` "search the web and return the top five results with their URLs and contents"; "Every request costs a fixed number of tokens, starting from 10,000 tokens"; rate limits: no key blocked, free key 100 RPM, paid 100 RPM, premium 1,000 RPM; average latency 2.5 s; engine/index not named; Elastic has sold "Jina On-Prem" licences as its own SKU since Aug 10, 2026 — [Jina Reader](https://jina.ai/reader/)
- Launch post (May 14, 2024): prepend `https://s.jina.ai/`; top 5 results, "full content! not abstract"; builds on `r.jina.ai` infrastructure; token count based on output tokens of all 5 results; 5 RPM without key / 40 RPM with key at launch; average latency then 30 s; no SERP provider disclosed — [Jina news](https://jina.ai/news/jina-reader-for-search-grounding-to-improve-factuality-of-llms)
- SearXNG's engine docs say "By default, Jina's own index is used" (this is SearXNG's description, not Jina's) — [SearXNG docs](https://docs.searxng.org/dev/engines/online/jina.html)
- Jina AI was acquired by Elastic in October 2025 (third-party profile) — [Neuronfeed](https://neuronfeed.com/startups/jina-ai)

### Inferences
- A fixed five-result output, token-based billing and absence of any crawler identity are the pattern of a SERP wrapper with on-the-fly page fetching; the SearXNG remark is the only claim of an "own index" and is unsupported by Jina.

### Gaps
- Jina has not disclosed its SERP/index source; no index size, filters or benchmark data exist.

## Marginalia Search

### Takeaway
Marginalia is a one-developer, open-source (AGPL) engine with its own crawler, ~300M documents (2024, "outdated" FAQ), focused on the non-commercial "small web"; its API (api2.marginalia-search.com) offers a public key, free non-commercial keys under CC-BY-NC-SA 4.0 and metered commercial keys with no published price.

### Cited Findings
- Index: passed 100,000,000 documents (106,857,244) in October 2022 — [Marginalia log](https://www.marginalia.nu/log/64-hundred-million/); FAQ (marked outdated) records about 300 million documents in 2024 and ~1 TB footprint; "an index with a million documents that are all of high quality is better than an index with a billion documents where only a fraction of them are interesting" — [Marginalia FAQ](https://marginalia.nu/marginalia-search/faq)
- API (fetched 2026-11-05): `GET https://api2.marginalia-search.com/search?query=...` with `count` (1-100), `timeout` (50-250 ms), `dc` (results per domain), `page`, `nsfw`, `filter`; custom filters via `/filter/NAME`; `API-Key` header; `public` key for experimentation (rate-limited, cannot create filters); free non-commercial keys by email (CC-BY-NC-SA 4.0); optional one-time paid non-commercial key; commercial keys metered via polar.sh with "no commercial usage restriction or attribution requirement", price unlisted; JSON response with `url`, `title`, `description`; legacy `api.marginalia.nu/{key}/search/{query}` deprecated — [Marginalia API article](https://about.marginalia-search.com/article/api/)
- Source code: GitHub MarginaliaSearch/MarginaliaSearch — [GitHub](https://github.com/MarginaliaSearch/MarginaliaSearch); Kagi lists Marginalia as a search source — [Kagi search sources](https://help.kagi.com/kagi/search-details/search-sources.html)

### Inferences
- Marginalia is the clearest example of a quality-over-scale independent index; its commercial API exists but is bespoke, so it is a complement (as Kagi uses it) rather than a general-purpose grounding source.

### Gaps
- No 2025-2026 document count published; commercial per-query price not published.

## Stract, Mwmbl, Alexandria.org, Wiby, Andi, Gigablast (indie and defunct engines)

### Takeaway
These are small independent indexes: Stract (own crawler, AGPL, hosted at stract.com, but its GitHub repo was archived Apr 2, 2026), Mwmbl (non-profit, volunteer-distributed crawling, API at $5/1k after 2,000 free/month), Alexandria.org (Common-Crawl-based, site unreachable from this session), Wiby (GPLv2, curated personal-site index, JSON endpoint), Andi (claims a 15B-page index and early-access API, weakly sourced) and Gigablast (12B pages in 2015; offline since April 2023).

### Cited Findings
- Stract: "open source web search engine hosted at stract.com targeted towards tinkerers and developers"; "Fully independent search index" with own crawler, Common Crawl used in early development; AGPL-3.0; 2.4k stars; repository archived and read-only as of Apr 2, 2026; no index size or API documented — [GitHub StractOrg/stract](https://github.com/StractOrg/stract); stract.com still serves a live site with "© 2026 Stract" footer and no shutdown notice (fetched 2026-11-05) — [stract.com](https://stract.com/); an archive listing says the exact index size is not publicly disclosed — [echo.archivarix](https://echo.archivarix.net/pt/archive/stract)
- Mwmbl: "a non-profit, open source search engine where the community determines the rankings"; AGPL-3.0; centralized index, crawling "distributed across servers run by volunteers"; index "much smaller than those of commercial search engines"; Firefox extension retrieves commercial results to evaluate Mwmbl's ranking — [GitHub mwmbl/mwmbl](https://github.com/mwmbl/mwmbl); API `https://api.mwmbl.org/api/v2/search/?q=`; anonymous 1,000 requests/month at 1 rps; free key 2,000/month at 5 rps; pay-as-you-go $5 per 1,000 requests; enterprise custom; "custom built search index" with latency under 200 ms (fetched 2026-11-05) — [developer.mwmbl.org](https://developer.mwmbl.org/)
- Alexandria.org: GitHub repo "Full text search engine powering Alexandria.org - the open search engine", 198 stars, 796 commits, not archived — [GitHub alexandria-org/alexandria](https://github.com/alexandria-org/alexandria); a third-party write-up describes it as non-profit, ad-free, with an index built from Common Crawl — [seirdy.one mirror](https://git.broken-by-design.fr/fmaury/seirdy.one/commit/935b55f10f9024ee660d5b0f6c9f7e546db159d8); www.alexandria.org did not resolve from this session (DNS/network restriction) on 2026-11-05
- Wiby: builds "a web of pages as it was in the earlier days of the internet"; JSON output at `wiby.me/json`; "now free software under GPLv2"; no terms, limits or index size stated — [Wiby about](https://wiby.me/about/)
- Andi: a LinkedIn company post describes 150,000+ monthly active users, a recently launched API with early access for a small number of developers, and a "15-billion-page index" (weak, unverified source; andisearch.com homepage returned only a title) — [LinkedIn: Andi](https://linkedin.com/company/andisearch)
- Gigablast: founded by Matt Wells; claimed over 12 billion pages indexed in 2015; open-sourced under Apache 2 in July 2013; went offline in early April 2023 without statement — [Wikipedia: Gigablast](https://en.wikipedia.org/wiki/Gigablast)

### Inferences
- Mwmbl is the only engine in this group with published, self-serve commercial pricing; Stract's archived repo plus live site suggests the hosted service continues without active development.
- Alexandria.org's reliance on Common Crawl means it does not meet the "own crawler" test even though the index is self-built.

### Gaps
- No index sizes for Stract, Mwmbl, Wiby or Alexandria; Andi's 15B-page claim lacks a primary source; Alexandria.org liveness unverified.

## Yep (Ahrefs)

### Takeaway
Ahrefs' Yep pivoted in 2025 to a Search API served from Ahrefs' own AhrefsBot crawl, claiming "100B pages in the index" and "8B pages crawled daily"; the Balanced plan is $4/1k requests including 20 results (+$1/1k per extra result) with 1,000 free requests.

### Cited Findings
- Platform page (fetched 2026-11-05): "100B pages in the index"; "8B pages crawled daily by AhrefsBot"; Balanced plan $4 per 1,000 requests including first 20 results, each additional result $1 per 1,000 requests, only returned results charged; "Start with 1,000 free API requests—no credit card required"; Highlights = "Query-relevant excerpts from each page"; Enterprise up to 1,000 results per search and custom QPS; timeline: Yep announced 2019, pivot to Search API in 2025; no latency claims — [platform.yep.com](https://platform.yep.com/)
- YepBot page: AhrefsBot "remains the primary source of data for both Yep and Ahrefs" — [yep.com/yepbot](https://yep.com/yepbot/)
- Ahrefs invested $60 million in Yep; AhrefsBot "visits more than 8 billion pages every 24 hours" (TechCrunch, June 2022, via Slashdot) — [Slashdot](https://tech.slashdot.org/story/22/06/11/0120258/seo-tool-ahrefs-built-a-60m-creator-friendly-search-engine-named-yep)
- Ahrefs' separate SEO API advertises "493.9B pages in index" (backlink/SEO index, not the Yep search index) — [Ahrefs SEO API](https://ahrefs.com/seo-api)

### Inferences
- Yep is the only provider besides Brave/Perplexity/Mojeek that names its crawler and gives a daily crawl volume; its 100B-page claim would make it the second-largest disclosed index after Perplexity's 200B URLs, but it is unverified marketing.

### Gaps
- No filters, latency, freshness interval (a third-party "15-30 minute update" claim was not confirmed) or benchmark results published; no MCP server found.

## European Search Perspective (EUSP) "Staan" and OpenWebSearch.eu Open Web Index

### Takeaway
Staan, the Qwant/Ecosia joint-venture index, went live for French users on Aug 7, 2025 and opened self-service API keys in June 2026 at €2/1k (Web Search) and €4/1k (Web Search for AI) with 1,000 free requests/month and a p95 < 800 ms claim; it discloses no crawler or page count. The EU-funded OpenWebSearch.eu project ended Feb 28, 2026 with an Open Web Index prototype downloadable under a research licence but no search API yet.

### Cited Findings
- Staan (fetched 2026-11-05): "Our own European web search API and index", "an independent European web search index"; languages FR/EN/DE, markets fr-fr, en-us, de-de, en-uk; 10 ranked results per call (documents, news, structured data); filter by domain, market, language; include/exclude up to 10 domains; Web Search for AI adds extra snippets, snippet scoring/re-ranking, full document fetch as HTML/Markdown; Web Search €2 per 1,000 requests at up to 20 QPS; Web Search for AI €4 per 1,000; first 1,000 requests/month free; "< 800 ms" p95 search latency, "End-to-end latency down to 1s min" for AI mode; "up to 4× cheaper"; "Powered by European Search Perspective", "runs on the same stack as Qwant Search" — [staan.ai](https://staan.ai/)
- Ecosia blog (Aug 7, 2025): Staan = "Search Trusted API Access Network"; EUSP is a joint venture of Ecosia and Qwant; French users receive "a portion" of results from the index; target 30% of French queries by year-end; index "also available to other tech companies" — [Ecosia blog](https://blog.ecosia.org/launching-our-european-search-index/)
- Self-service launch reported June 16, 2026 ("any developer can now get an API key") — [onlinemarketing.de](https://onlinemarketing.de/seo/europaeische-search-api-staan-jetzt-als-self-service); joint-venture formation Nov 2024 and launch coverage — [Search Engine Journal](https://www.searchenginejournal.com/ecosia-qwant-launch-european-search-infrastructure/553182/); Ecosia CEO claimed "a tenth of the cost of Google and Bing" (company claim) — [tech.eu](https://tech.eu/2025/08/06/ecosia-rolls-out-independent-search-results-in-europe-taking-another-giant-step-away-from-big-tech/)
- OpenWebSearch.eu: project "officially ended on 28 February 2026"; Open Web Index prototype launched May 2025; team "still working to launch the first search API and operational search frontend"; index shards downloadable under a research licence via the OWI dashboard (openwebindex.eu); commercial licensing unresolved; follow-on "European Open Web Search initiative" (Open Search Foundation, University of Passau); Horizon Europe grant 101070014 — [OpenWebSearch.eu, April 2026](https://openwebsearch.eu/2026/04/); [project end post](https://openwebsearch.eu/title-42-months-in-the-making-openwebsearch-eu-project-end-results-look-promising/)

### Inferences
- Staan is the only new European commercial index with public self-serve pricing; its "same stack as Qwant Search" statement implies Qwant's 2023 re-engineered crawler/index, but EUSP has not published a crawler identity or size.
- The Open Web Index is an index-as-data offering (download shards), not an API, so it is not yet a search API provider.

### Gaps
- Staan page count, crawler name, freshness, benchmarks and MCP availability unpublished; no verification that EUSP met its 30%/50% French-query targets (a Feb 2026 review reportedly found no confirming data).

## Yandex Search API (and Baidu / Naver / Seznam, brief)

### Takeaway
Yandex sells its own-index Search API through Yandex Cloud/AI Studio at roughly $4.00/1k for daytime synchronous requests, $0.25/1k deferred, $3.00/1k at night, and ~$41.64/1k for generative answers (USD, ex-VAT). No official developer web-search APIs with public pricing were found for Baidu, Naver or Seznam; third parties (DataForSEO) resell scraped SERPs for all three.

### Cited Findings
- Yandex pricing (fetched 2026-11-05; USD per 1,000 requests ex-VAT, billed per request): daytime synchronous $3.99999936 (~$0.004/request); daytime deferred $0.24999996; night-time synchronous $2.99999952; night-time deferred $0.2082786552; synchronous with generative response $41.6393376; image search $7.4999988; smart snippets for RU search $12.29508; night rates 00:00-07:59 UTC+3; RUB example ₽488/1k synchronous, ₽5,080/1k generative; prices in USD apply to contracts with Iron Hive doo Beograd (Serbia) or Direct Cursus Technology L.L.C. (Dubai); no free tier described — [Yandex Search API pricing](https://aistudio.yandex.ru/docs/en/search-api/pricing)
- API v2 natively integrated in Yandex Cloud; v1 is Yandex-XML-compatible; cost tied to requests per calendar month — [Yandex Search API docs](https://yandex.cloud/en/docs/search-api); terms of use — [Yandex legal](https://yandex.com/legal/cloud_terms_search_api/en/)
- Baidu/Naver/Seznam: DataForSEO changed its Organic SERP API pricing for Baidu, Seznam and Naver on Sept 19, 2025; Naver returns one SERP of up to 15 results via a queue (no Live mode) — [DataForSEO update](https://dataforseo.com/update/organic-serp-api-pricing-changes-now-in-effect); [DataForSEO Naver](https://dataforseo.com/pricing/serp/naver-organic-serp-api); a Keenable comparison says Chinese web-search APIs start at ¥12 per 1,000 calls but that official pricing or access "could not be verified" — [Keenable select](https://select.keenable.ai/r/web-search-apis-china-market-comparison/3G5FI8ZzfPffaploN_Zmqw)

### Inferences
- Yandex is the cheapest large own-index API by far on deferred requests (~$0.25/1k) but the contracting-entity (Serbia/Dubai) and sanctions context limit its usability for many Western buyers.

### Gaps
- Yandex index size and freshness are not stated on the pricing/docs pages read; no official Baidu, Naver or Seznam developer-API pricing was found.

## Nimble, Octen, Critique Labs, Felo, Omnisearch and other 2026 newcomers

### Takeaway
Octen (launched Apr 22, 2026, $10M seed led by Square Peg) is the notable newcomer: 77 on the AA Search Index at the lowest cost ($0.0236/task) and fastest time, with vendor claims of 62 ms p50, content "indexed within 5 minutes" and $1/1k, but no disclosed crawler. Nimble ($1.1/1k, AA 74) markets a "Proprietary Index" but its product copy describes scraping live search engines. Critique Labs and Felo publish neither pricing nor index disclosures; "Omnisearch" is not a search-API product.

### Cited Findings
- Octen: launched Apr 22, 2026 with $10M seed led by Square Peg (Argor participating); company APITECH AI Pte Ltd, Singapore and San Francisco, founder/CEO Kuan Zou; median 62 ms on SealQA Hard ("more than four times faster than the fastest rival"); >1 million QPS per account; invite-only beta — [SiliconANGLE, Apr 22, 2026](https://siliconangle.com/2026/04/22/octen-raises-10m-seed-funding-speed-ai-agent-search-queries/); Product Hunt listing (launched there July 22, 2026): "new content indexed within 5 minutes", 62 ms P50, $1 per 1,000 calls vs "typical competitor rates of $4 to $9", embedding models #1 on RTEB/MMEB-v2; Octen Extract launched Sept 2, 2026 — [Product Hunt](https://www.producthunt.com/products/octen-search-infrastructure-for-ai); founder previously led AI search at Alibaba Cloud — [Pulse2](https://pulse2.com/octen-10-million-seed-and-new-api-launch-aim-to-redefine-search-infrastructure-for-ai-agents/); AA Search Index 77 (DeepSearchQA 80, BrowseComp 86, AA-Omniscience 66; $0.0236/task; 15.8 s), Oct 19, 2026 — [Artificial Analysis](https://artificialanalysis.ai/agents/search-api)
- Nimble: Search API "Starting at $1.1/1k search requests" (lite tier, short snippets); "Search and retrieve context-rich excerpts in <500ms"; "Proprietary Index and Memory that gets smarter with every query" — [Nimble Search API](https://www.nimbleway.com/product/search-api); pricing page: $1.1 per 1,000 requests, free tier 5,000 requests/month, platform plans $2,500/$7,000/$15,000 per month billed annually — [Nimble pricing](https://www.nimbleway.com/pricing); its tools include "deep web search for scraping real-time content from major search engines" and it is a native LiteLLM search provider — [search summary via nimbleway/litellm docs](https://docs.litellm.ai/docs/search/nimble.md); AA Search Index 74 (standard) — [Artificial Analysis](https://artificialanalysis.ai/agents/search-api)
- Critique Labs: operated by Starman LLC (Mountain View, CA); products Agentic Search Engine, Critique API Platform ("agentic API builder"), Critique Browser, Critique DB; no pricing, index or benchmark claims on site — [critique-labs.ai](https://critique-labs.ai/); an n8n community node references `api.critique-labs.ai/v1/search` and `/v1/contents` (unverified docs) — [n8n node page](https://frontend-f26.pages.dev/package/n8n-nodes-critique-api/critiqueapi)
- Felo: July 16, 2026 post lists `POST /v2/chat` (AI search), `/v2/web/extract`, X/tweet search, YouTube subtitles, LiveDocs; cost rated "Low" without figures; no index/crawler disclosure or latency figures — [Felo blog](https://felo.ai/blog/best-web-search-api-ai-agents-2026/)
- Omnisearch: the name refers to an enterprise site-search SaaS (from $49/month), an Obsidian plugin, and open-source `mcp-omnisearch` servers that wrap Tavily, Brave, Kagi, Exa and Perplexity — not an independent web-search API — [Glama: mcp-omnisearch](https://glama.ai/mcp/servers/@spences10/mcp-omnisearch/tree); [Capterra](https://www.capterra.com/p/247857/Omnisearch/)
- Liner: advertises $1 per 1,000 web search requests (index source not researched) — [Liner blog](https://build.liner.com/blog/liner-api-pricing)
- One-line rows for providers covered elsewhere: Keenable — own crawler/index/ranking, "more than 100 billion documents", $26M seed led by Accel (Sept 2026), $1/1k at frontier volume — [StorageNewsletter](https://www.storagenewsletter.com/2026/09/07/keenable-raised-26-million-seed-round/); [ai2.work](https://ai2.work/blog/keenable-raises-26m-to-build-a-web-search-index-for-ai-agents); Exa — own crawlers, index claims range from "500+ billion URLs" to "1.4T URLs tracked / 80B pages served", $250M Series C at $2.2B (a16z, May 2026), AA Search Index 80 (auto) — [AI Tools Atlas](https://aitoolsatlas.ai/tools/exa); [Keenable select](https://select.keenable.ai/r/keenable-ai-vs-exa-ai-which-is-better/6OadhpXDQ9OFrHyUEDVNKw); [Artificial Analysis](https://artificialanalysis.ai/agents/search-api)

### Inferences
- Octen's "indexed within 5 minutes" and 1M QPS claims only make sense with a self-operated index, but with no crawler identity or page count it must be classed as "own index claimed, undisclosed".
- Nimble's heritage as a proxy/scraping vendor and its "scraping real-time content from major search engines" copy indicate a SERP-derived pipeline with a cache ("Proprietary Index") on top; it is not an independent crawl.

### Gaps
- Octen crawler, index size and independent latency verification; Critique Labs pricing/docs; Felo pricing and sourcing; Liner sourcing.

## Comparison table (all providers, as of 2026-11-05)

### Takeaway
Only Brave, Mojeek, Perplexity, Yep, Yandex, Marginalia, Stract, Mwmbl and Kagi's Enrichment (Teclis/TinyGem) publish a named crawler and an own-index statement; Parallel, Linkup, Valyu, Staan and Octen claim own indexes without a page count or crawler identity (Valyu does name HenkBot); You.com, Firecrawl, Nimble, Jina, Tavily, Felo and Critique Labs leave the index source undisclosed, with external evidence pointing to third-party SERPs for Tavily, Jina and Nimble.

### Cited Findings
| Provider | Own crawler/index? (evidence) | Index size / freshness claim (date) | Price per 1k queries (date) | Free tier | Latency claim | AA Search Index (Oct 19, 2026) | MCP server | Stated UVP / notable benchmark |
|---|---|---|---|---|---|---|---|---|
| Brave Search API | Yes; own crawler + Web Discovery Project; "zero dependencies on Google or Bing" ([Brave](https://brave.com/search/api/)) | "over 30B pages", +100M/day (guide upd. Oct 2025); no size on 2026 pages ([guide](https://brave.com/search/api/guides/what-sets-brave-search-api-apart/)) | Search $5; Answers $4 + $5/M tokens (Feb 12, 2026) ([Brave](https://brave.com/search/api/)) | $5 credit/month | LLM Context p90 <500 ms; 95% <1 s ([blog](https://brave.com/blog/most-powerful-search-api-for-ai/)) | 75 (LLM context) | Official (brave/brave-search-mcp-server) | Only non-Big-Tech global index via open API; SimpleQA 94.1% F1 (Answers) |
| Mojeek | Yes; MojeekBot; "Independent Index" ([Mojeek](https://www.mojeek.com/services/search/web-search-api/)) | 9B pages (2025) ([about](https://www.mojeek.com/about/)) | £2 (Startup, 10 results) / £3 (Business, 40 results) (fetched 2026-11-05) | Unspecified free credit | None | Not captured | None found | EU data sovereignty, zero sub-processors, no tracking |
| Kagi (Enrichment: Teclis/TinyGem) | Yes for Enrichment; full Search API blends "all major providers" + Marginalia ([Kagi](https://help.kagi.com/kagi/search-details/search-sources.html)) | Undisclosed | Enrich $2; Search API $12; FastGPT $15 (fetched 2026-11-05) | Prepaid credits only | None | Not captured | Official (kagimcp) | Small-web/non-commercial index as complement |
| Perplexity Search API | Yes; PerplexityBot ([bots](https://docs.perplexity.ai/guides/bots)) | >200B unique URLs; tens of thousands of index ops/s (Sept 25, 2025) ([research](https://www.perplexity.ai/hub/blog/architecting-and-evaluating-an-ai-first-search-api)) | $5 default; $1 fast (fetched 2026-11-05) | Not confirmed (rate-limits page 404) | p50 358 ms, p95 763 ms (vendor, Sept 2025) | 80 (medium), 79 (high) | Official | Sub-document ranking; SimpleQA .930 (vendor) |
| You.com | Undisclosed; bills only live crawls, cites "improved crawling" ([billing](https://you.com/docs/administration/billing)) | Undisclosed; Finance index purpose-built | $5 web (1-100 results); Contents $1; Research $12-$1,200 (Mar 12, 2026) | 100 calls/day (Jul 29, 2026, third-party); free MCP profile | None | 74 (highlights) | Yes (free `?profile=free`) | Full page content in every result; Finance Research |
| Parallel.ai | Claimed proprietary index, robots.txt-respecting crawler; no UA named ([product](https://parallel.ai/ai/products/search)) | "billions of pages", millions added/updated daily (fetched 2026-11-05) | $1 turbo/fast; $5 basic/advanced; +$1 per extra results; Extract $1 (fetched 2026-11-05) | Up to 80,000 requests | Turbo ~200 ms, Fast ~700 ms, Basic ~1 s, Advanced ~3 s | 75 (advanced) | Hosted (search-mcp.parallel.ai) | Token-dense excerpts; BrowseComp 74% advanced (vendor); $2B valuation |
| Tavily (Nebius) | No per Sacra ("does not maintain its own search index"); Perplexity: "SERP-based"; Tavily: "agent-native index" + caching ([Sacra](https://sacra.com/research/tavily)) | Undisclosed | $8 PAYG per 1k credits (basic 1 credit, advanced 2) (fetched 2026-11-05) | 1,000 credits/month | None official | Not captured | Official (tavily-mcp) | Search+Extract+Crawl+Map; acquired for ~$275M (Feb 2026) |
| Linkup | Claimed "our index" + premium data partners; no crawler named ([FAQ](https://docs.linkup.so/pages/faq/faq.md)) | Undisclosed | $5 standard ($6 with answer); $50 deep (fetched 2026-11-05) | $20/month credit | flash <200 ms; fast ~1 s | Not captured | Not confirmed | Verified SimpleQA 94% F-score (vendor); publisher partnerships |
| Valyu | Yes; HenkBot ([crawler](https://docs.valyu.ai/crawler)) | Undisclosed | Web 100 credits/1k results ≈ $0.63 PAYG; academic 50; SEC 1,920 (fetched 2026-11-05) | $10-$20 credit | None | Not captured | Not confirmed | Web + academic + financial + licensed sources in one API |
| Firecrawl /search | Undisclosed for web; own vertical indexes (Alexandria, 113M+ sources) ([Alexandria](https://firecrawl.dev/alexandria)) | Undisclosed | 2 credits/10 results (~$0.0038-$0.019 per 10 results by plan) (fetched 2026-11-05) | 1,000 credits/month | None | 73 | Not verified | Search + scrape in one; $75M Series B Sept 2026 |
| Jina s.jina.ai | Undisclosed; no crawler ([Reader](https://jina.ai/reader/)) | Undisclosed | Token-based, ≥10,000 tokens/request (fetched 2026-11-05) | Free key 100 RPM | avg 2.5 s | Not listed | Community | Top-5 results with full markdown |
| Marginalia | Yes; own crawler, AGPL ([API](https://about.marginalia-search.com/article/api/)) | ~300M docs (2024) | Commercial metered, price unlisted; non-commercial free | Public key | None | Not listed | None | Small-web, non-commercial focus |
| Stract | Yes; own crawler (repo archived Apr 2, 2026) ([GitHub](https://github.com/StractOrg/stract)) | Undisclosed | None published | n/a | None | Not listed | None | Open-source, hackable |
| Mwmbl | Yes; volunteer-distributed crawl ([GitHub](https://github.com/mwmbl/mwmbl)) | "much smaller than commercial" | $5 after 2,000 free/month (fetched 2026-11-05) | 1,000 anon / 2,000 keyed per month | <200 ms | Not listed | None | Non-profit, community-ranked |
| Alexandria.org | Self-built index from Common Crawl (no own crawler) ([GitHub](https://github.com/alexandria-org/alexandria)) | Undisclosed | None found | n/a | None | Not listed | None | Non-profit open engine (site unreachable 2026-11-05) |
| Wiby | Curated own index, GPLv2 ([about](https://wiby.me/about/)) | Undisclosed | Free JSON endpoint | Yes | None | Not listed | None | Early-web personal sites |
| Yep (Ahrefs) | Yes; AhrefsBot ([platform](https://platform.yep.com/)) | 100B pages; 8B crawled/day (fetched 2026-11-05) | $4 incl. 20 results; +$1 per extra result | 1,000 requests | None | Not listed | None found | Backed by Ahrefs' $60M crawl investment |
| Andi | Claimed 15B-page index (LinkedIn, weak) ([LinkedIn](https://linkedin.com/company/andisearch)) | 15B pages (undated) | Early access only | n/a | None | Not listed | None | Consumer AI search |
| Gigablast | Was own index (Apache 2 OSS) ([Wikipedia](https://en.wikipedia.org/wiki/Gigablast)) | 12B pages (2015) | Defunct (offline Apr 2023) | n/a | n/a | n/a | n/a | Historical |
| EUSP Staan (Qwant/Ecosia) | Claimed own European index on Qwant stack; no crawler named ([staan.ai](https://staan.ai/)) | Undisclosed; FR/EN/DE | €2 Web Search; €4 Web Search for AI (fetched 2026-11-05) | 1,000 requests/month | p95 <800 ms | Not listed | None found | European sovereignty; "up to 4× cheaper" |
| OpenWebSearch.eu OWI | Yes (EU-funded crawl); no API yet ([Apr 2026](https://openwebsearch.eu/2026/04/)) | Undisclosed | Shards free under research licence | n/a | n/a | n/a | n/a | Open index-as-data |
| Yandex Search API | Yes (Yandex index) ([pricing](https://aistudio.yandex.ru/docs/en/search-api/pricing)) | Undisclosed on docs | ~$4.00 sync day; ~$0.25 deferred; ~$41.64 generative (fetched 2026-11-05) | None stated | None | Not listed | None found | Cheapest deferred tier; RU/CIS coverage |
| Nimble | Undisclosed; copy says scraping "major search engines" + "Proprietary Index" cache ([product](https://www.nimbleway.com/product/search-api)) | Undisclosed | $1.1 (lite) (fetched 2026-11-05) | 5,000 requests/month | <500 ms | 74 (standard) | LiteLLM native | Low cost per query |
| Octen | Claimed (content "indexed within 5 minutes"); no crawler named ([Product Hunt](https://www.producthunt.com/products/octen-search-infrastructure-for-ai)) | Undisclosed; 5-minute freshness | $1 (vendor) | Invite-only beta | 62 ms p50 (vendor) | 77 (highlights), cheapest/fastest in table | Not found | Speed; $10M seed Apr 2026 |
| Critique Labs | Undisclosed ([site](https://critique-labs.ai/)) | Undisclosed | Not published | n/a | None | Not listed | None found | Agentic search/API builder |
| Felo | Undisclosed ([blog](https://felo.ai/blog/best-web-search-api-ai-agents-2026/)) | Undisclosed | "Low", not published | Free key | None | Not listed | None found | Conversational answers + X/YouTube search |
| Exa (one line) | Yes, own crawlers | 500B+ URLs or 1.4T URLs/80B pages (conflicting) | See other researcher | — | — | 80 (auto) | Official | $250M Series C at $2.2B (May 2026) |
| Keenable (one line) | Yes, own crawler/index | >100B documents (Sept 2026) | $1 at frontier volume | — | — | Not captured | MCP interface | $26M seed led by Accel (Sept 2026) |

### Inferences
- Disclosed index sizes span three orders of magnitude (Marginalia 0.3B; Mojeek 9B; Brave 30B+; Yep 100B; Perplexity 200B URLs), and the providers that publish sizes are not the ones leading the AA benchmark; quality on agentic benchmarks tracks ranking/excerpt design more than page count.
- List prices have converged on $1/1k for "fast" tiers (Perplexity fast, Parallel turbo/fast, Octen, Nimble, Keenable) and $4-5/1k for full-quality tiers (Brave, Perplexity, Parallel, You.com, Yep, Yandex sync), with Kagi ($12) and Tavily (~$8-16 effective) as the expensive outliers.

### Gaps
- AA scores for Tavily, Linkup, Valyu, Kagi, Mojeek, Staan and Yep were not captured or not tested; official MCP status for Linkup, Valyu, Firecrawl and Mojeek was not verified; You.com, Parallel, Linkup, Staan and Octen never publish page counts or crawler user-agents.
