# SERP wrappers, meta-search layers and LLM-platform search tools (as of 2026-11-05)

Scope note: this file covers providers that WRAP or RESELL existing engines (Google/Bing/Yandex/Baidu SERP scraping APIs), official engine APIs, meta-search layers used by agents, and the search tools built into LLM platforms. Own-index providers (Exa, Brave, Parallel, Perplexity's index) appear only where they are needed for benchmark comparison or the "who sits on top of whom" diagram. Every price below was read from the cited page on 2026-11-05 unless a different date is stated. "Disclosed" means the vendor states it; "inferred" means I am reasoning from indirect evidence and say so.

Research-method note: the shared WebSearch budget for this session ran out near the end of the research, so a handful of secondary items (Hacker News threads, Jina token-pack prices, Mistral's official connector price, Cohere's current web-search status beyond its connector deprecation) could not be searched further. They are listed under Gaps.

## Key question 1: SERP-scraping / reselling APIs (Serper, SerpApi, SearchApi, Bright Data, Oxylabs, DataForSEO, ZenRows, ScrapingBee, Scrapfly, Apify, Nimble, Scale SERP / Value SERP, Serply, Zyte)

### Takeaway
Google-SERP scraping is now a commodity priced between roughly $0.30/1k (Serper Ultimate), $0.50–$0.60/1k (Oxylabs non-JS at 5M+, DataForSEO standard queue) and $1–$5/1k at entry tiers, with a long tail of general-purpose scraping APIs (ZenRows, ScrapingBee, Scrapfly, Zyte) where a Google query costs 10–25 "credits" and lands at $1–$10/1k depending on plan. Vendors differentiate on legal indemnity (SerpApi and SearchApi both advertise a $2M "Legal Shield"), speed tiers, engine breadth (SearchApi ~80 engines; Bright Data 7 engines; DataForSEO 7 engines), and how they absorbed Google's January-2025 JavaScript requirement and the September-2025 removal of `num=100` (vendors paginate internally; top-100 now costs ~10 requests where depth is billed per 10 results).

### Cited Findings

**Serper.dev**
- Positioning: "The World's Fastest & Cheapest Google Search API"; "lightning-fast Google search results in 1-2 seconds"; 2,500 free queries, no credit card; endpoints: Search, Images, News, Maps, Places, Videos, Shopping, Scholar, Patents, Autocomplete (Google only); ~10 organic results per query in samples (accessed 2026-11-05) — [Serper](https://serper.dev/)
- Pricing (credits valid 6 months, no monthly subscription): Starter $50 / 50k credits ($1.00/1k), Standard $375 / 500k ($0.75/1k), Scale $1,250 / 2.5M ($0.50/1k), Ultimate $3,750 / 12.5M ($0.30/1k); rate limits 50 / 100 / 200 / 300 queries per second by plan; "Queries typically return in 1 to 2 seconds, sometimes 2 to 4 seconds when a retry to Google is needed" (accessed 2026-11-05) — [Serper pricing section](https://serper.dev/)
- No legal/ToS statement found on the page; MCP availability not stated (see Gaps).

**SerpApi**
- Pricing (monthly, accessed 2026-11-05): Free 250 searches/mo (50/hr); Starter $25 / 1,000 ($25.00/1k); Developer $75 / 5,000 ($15.00/1k); Production $150 / 15,000 ($10.00/1k); Big Data $275 / 30,000 ($9.17/1k); Searcher $725 / 100k ($7.25/1k); Volume $1,475 / 250k ($5.90/1k); Infrastructure $2,750 / 500k ($5.50/1k); Cloud 1M $3,750 ($3.75/1k); Cloud 5M $11,475 ($2.30/1k); Cloud 10M $21,125 ($2.11/1k); Cloud 54M $106,050 ($1.96/1k). "Throughput" is a guaranteed successful-searches-per-hour figure per plan (e.g., 3,000/hr at Production, 110,000/hr at Cloud 1M). Only successful searches are billed; cached/errored searches are not — [SerpApi pricing](https://serpapi.com/pricing)
- Speed tiers: "Ludicrous Speed" at 2x plan price claims 2.2x faster average and 4.2x faster p99 than Best Effort; "Ludicrous Speed Max" at 4x claims a further 9.6% average / 35.4% p99 improvement over Ludicrous Speed. No formal SLA stated — [SerpApi pricing](https://serpapi.com/pricing)
- Legal posture: "U.S. Legal Shield" up to $2M coverage for scraping/parsing claims, on Production and above (not Free/Starter/Developer); covers only claims under U.S. state/federal law in a U.S. court; conditional on the customer's own use being lawful; "SerpApi assumes liability for the lawful collection of public search data"; search data retained 31 days unless ZeroTrace Mode (Cloud 1M+) which stores nothing; proxy providers are listed as subprocessors — [SerpApi legal](https://serpapi.com/legal); [SerpApi pricing](https://serpapi.com/pricing)
- Google JS requirement: SerpApi blog dated January 17, 2025 says that as of January 15, 2025 Google requires JavaScript to view results; "SEO tools and other SERP data providers were hit hard ... significant lags and outages"; SerpApi says it was "minimally impacted" because Ludicrous Speed tiers already solved the JS challenge; standard searches briefly saw slightly higher latency — [SerpApi blog](https://serpapi.com/blog/google-now-requires-javascript/)
- Benchmarks: Parallel's pages (vendor-run, Parallel is a competitor) report SerpAPI at 23.3% BrowseComp accuracy with 999 ms p50 search latency in runs dated July 10–12, 2026, versus Parallel 51% with the same GPT-5.4 agent; the same page notes "Neither Artificial Analysis nor Openbenchmarks tests SerpApi" (from search-result snippets of these pages, not a full fetch) — [Parallel vs SerpApi](https://parallel.ai/compare/serpapi-vs-parallel); [Parallel best web search API](https://parallel.ai/articles/best-web-search-api)
- The pricing page does not list supported engines (SerpApi's broad engine list is widely known but was not verified on the fetched page — see Gaps).

**SearchApi.io**
- Pricing (accessed 2026-11-05): Developer $40 / 10,000 ($4.00/1k); Production $100 / 35,000 ($3.00/1k; adds Legal Protection Guarantee); BigData $250 / 100k ($2.50/1k); Scale $500 / 250k ($2.00/1k); Octo 500K $900 ($1.80/1k); Octo 1M $1,500 ($1.50/1k); Octo 2M $2,800 ($1.40/1k); Octo 5M $5,000 ($1.00/1k); 100 free requests at signup; only HTTP-200 searches billed; usage capped at 20% of plan credits per hour; 99.9% uptime SLA on all plans — [SearchApi pricing](https://www.searchapi.io/pricing)
- Engines (~80 APIs): Google (SERP, Maps, Shopping, Images, News, Scholar, Flights, Hotels, Trends, Lens, Finance, Patents, Jobs, Events...), Bing (Search, Images, Videos, Shopping, Maps, Copilot), Yandex, Baidu, DuckDuckGo, Yahoo, Naver, Perplexity, ChatGPT, plus Amazon/eBay/Walmart/LinkedIn/Reddit/TikTok/YouTube etc. — [SearchApi pricing](https://www.searchapi.io/pricing)
- Legal: "Legal Protection Guarantee" (Production+) — accepts legal responsibility for collecting/parsing public search results, up to $2M coverage, worldwide customers, under U.S. law; excludes customer's use of data — [SearchApi pricing](https://www.searchapi.io/pricing)
- UVP: pay-per-success, built-in geo-targeting, "premium proxies only" from a 20M+ network, AWS infrastructure — [SearchApi pricing](https://www.searchapi.io/pricing)

**Bright Data SERP API**
- Pricing (accessed 2026-11-05): Free 5K requests/month; Pay-as-you-go $1.50/1k requests; Scale $499/mo incl. 380K requests then $1.30/1k; Enterprise custom with Premium SLA/SSO; first-deposit match up to $500; AWS Marketplace; "Response time under 5 sec"; unlimited concurrency; 195 countries, city-level targeting; JSON or HTML output — [Bright Data SERP pricing](https://brightdata.com/pricing/serp)
- Engines (docs): Google, Bing, DuckDuckGo, Yandex, Baidu, Yahoo, Naver; output raw HTML, parsed JSON (`brd_json=1`), markdown, or `parsed_light` ("top 10 organic results without ads or knowledge panels") — [Bright Data SERP docs](https://docs.brightdata.com/scraping-automation/serp-api/introduction)
- Billing: per 1,000 successful requests; failed requests not charged by default (but all requests billed if custom headers/cookies enabled); async "collect" call free — [Bright Data billing](https://docs.brightdata.com/scraping-automation/serp-api/pricing-and-billing.md)
- Legal/compliance: pricing page contains no acceptable-use or legal-posture statements — [Bright Data SERP pricing](https://brightdata.com/pricing/serp)

**Oxylabs Web Scraper API (SERP)**
- Pricing (accessed 2026-11-05): Google JS from $1.35/1k (up to 3.7K results) down to $0.90/1k (2.78M+); Google non-JS from $1.00/1k (up to 5K) down to $0.50/1k (5M+); generic /Scrape from $0.50/1k down to $0.25/1k (10M+); plans Starter $30/mo, Basic $100/mo, Flexible $500/mo, Enterprise from $2,500/mo; $5 welcome credit; also sells "LLM scrapers" for ChatGPT, Perplexity, Gemini and Google AI Mode — [Oxylabs SERP pricing](https://oxylabs.io/products/scraper-api/serp/pricing); [Oxylabs SERP](https://oxylabs.io/products/scraper-api/serp)
- Engines: Google, Baidu, Bing, Yandex (no DuckDuckGo); claims "100% Google success rate" and "6.04 seconds avg. response time" citing Proxyway; FAQ says "less than 10 seconds" average; parsed JSON with 269 data points for Google Web; results with 2xx or 4xx count as billable successes — [Oxylabs SERP](https://oxylabs.io/products/scraper-api/serp)
- Oxylabs blog dates Google's JS requirement announcement to January 17, 2025 and describes it as targeting "bots, scrapers, and SEO tools that rely on non-JavaScript-based methods" (from search snippet) — [Oxylabs blog](https://oxylabs.io/blog/google-search-javascript)

**DataForSEO**
- Google Organic SERP pricing (accessed 2026-11-05): Standard queue $0.0006/SERP ($0.60/1k), avg ~5 min latency (45-min target); Priority queue $0.0012 ($1.20/1k), up to 1 min; Live mode $0.002 ($2.00/1k), up to 6 s average; "+1 base price per each additional 10 results" (so a 100-result pull = 10 base prices = $6/$12/$20 per 1k — my arithmetic); refunds the difference if Google returns fewer results — [DataForSEO Google Organic](https://dataforseo.com/pricing/google-serp-pricing/google-organic-serp-api)
- Other engines all "from $0.0006": YouTube (per 20 results), Bing (per SERP, 10 results), Yahoo (6 results), Baidu (10), Naver (20), Seznam (10); Yandex not listed — [DataForSEO SERP pricing](https://dataforseo.com/pricing/serp)

**ZenRows**
- Credit plans (accessed 2026-11-05): Free 5,000 credits; Build $19 / 45k ($0.42 per 1k credits) to $39 / 120k; Launch $69–$129 (250k–700k); Growth $199–$399 (1.2M–3M); Scale $549–$2,999 (5M–45M, down to ~$0.07 per 1k credits); concurrency 5 → 200–400; multipliers: standard page 1 credit, JS rendering 5x, premium proxy 10x, JS + premium proxy 25x; failed requests free — [ZenRows pricing](https://www.zenrows.com/pricing)
- The dedicated SERP API page returned HTTP 404 on 2026-11-05, so a Google-specific price could not be confirmed — [ZenRows SERP API (404)](https://www.zenrows.com/serp-api)

**ScrapingBee**
- Plans (accessed 2026-11-05): Hobby $19 / 75k credits (25 concurrent); Freelance $49 / 250k; Startup $99 / 1M (100 concurrent); Business $249 / 3M; Business+ $599 / 8M; Enterprise $999 / 14M up to $5,799 / 120M — [ScrapingBee pricing](https://www.scrapingbee.com/pricing/)
- Google Search API: "Each search costs 10 credits with Light Request enabled, or 15 otherwise"; `search_type` web, news, maps, images; `extra_params` passes Google's `gl`, `hl`, `num`, `start`; structured JSON output with organic_results, knowledge_graph, top_ads etc. — [ScrapingBee Google docs](https://www.scrapingbee.com/documentation/google/)

**Scrapfly**
- Plans (accessed 2026-11-05): Free 1,000 credits (5 concurrent); Discovery $30 / 200k; Pro $100 / 1M (20 concurrent); Startup $250 / 2.5M; Enterprise $500 / 5.5M (100 concurrent); custom $1,200–$30,000+. Google SERP credit cost not published on the page; it points to a cost-estimation endpoint (`?cost=true`) — [Scrapfly pricing](https://scrapfly.io/pricing)

**Apify — Google Search Results Scraper**
- Pay-per-event, "from $1.80 / 1,000 scraped search result pages" (`search-page-scraped` event); each page ≈ 10 results; `maxPagesPerQuery` 10 ≈ 100 results; add-on events for AI Mode/AI Overviews/ChatGPT/Gemini/Perplexity/Copilot; Free plan $5 credit "covers over 1,000 Google Search results"; usable via hosted MCP server at `https://mcp.apify.com` (OAuth or bearer token); readme advises factoring in "Google's Terms of Use" and consulting lawyers (accessed 2026-11-05) — [Apify Google Search Scraper](https://apify.com/apify/google-search-scraper)

**Nimble**
- Official docs (accessed 2026-11-05): Search API Lite $1.10 per 1K inputs, Standard $5.00 per 1K inputs, `full_content: true` add-on $1.00 per 1K URLs; Extract API $1.00/1K URLs ($2.50 with `max` driver); Agent API $0.025–$2.00 per task by effort; plans Startup $2,500/mo (350K pages), Scale $7,000/mo, Professional $15,000/mo; 5,000 free pages — [Nimble pricing docs](https://docs.nimbleway.com/nimble-sdk/admin/pricing.md)
- Conflicting third-party data: a pricing-change tracker reports a July 2026 change raising Nimble Search from $1.50 to $5 per 1K; another snapshot cited $1.00/1k with up to 100 results per request (from search snippets) — [PricingSaaS Nimble 2026W29](https://pricingsaas.com/companies/nimbleway/diffs/2026W29); [Nimble SERP docs](https://docs.nimbleway.com:8443/data-platform/serp-api)
- Benchmark: Artificial Analysis (Oct 19, 2026) lists Nimble Search (standard) at Search Index 74, BrowseComp 75, search cost $46.14 per 1k tasks — [Artificial Analysis Search API](https://artificialanalysis.ai/agents/search-api)

**Scale SERP and Value SERP (Traject Data)**
- Scale SERP (annual-billed monthly prices, accessed 2026-11-05): 1,000 searches $23 ($23.00/1k); 10,000 $66 ($6.60/1k); 50,000 $199 ($3.98/1k); 250,000 $599 ($2.40/1k); 1M $1,699 ($1.70/1k); 5M $4,999 ($1.00/1k); overage from $0.038 down to $0.002 per search; 125 free searches/month; Google only; "not affiliated with Google"; Traject Data also owns Value SERP and SerpWow — [Traject Data Scale SERP](https://trajectdata.com/pricing/scaleserp-api)
- Value SERP (accessed 2026-11-05): 25,000 credits $50/mo (page states $1.60/1k; arithmetic gives $2.00/1k), 200,000 $240 ($1.20/1k), 1M $1,000 ($1.00/1k); pay-as-you-go "from just $2.50/1k"; real-time limits 250 / 1,000 / 1,500 per minute; Google only — [Traject Data Value SERP](https://trajectdata.com/pricing/value-serp-api)

**Serply**
- Prepaid, non-expiring credits (accessed 2026-11-05): Micro 2,500 / $5 ($2.00/1k); Starter 10,000 / $15 ($1.50/1k); Growth 50,000 / $49 ($0.98/1k); Pro 500,000 / $375 ($0.75/1k); Scale 2.5M / $1,875; Max 10M / $7,500 ($0.75/1k); 2,500 free credits for 30 days; engines Google (Search, News, Video, Images, Jobs, Scholar, Product, Maps) and Bing, plus Reddit/eBay; "One credit buys one request on any endpoint, including MCP tool calls" — has an MCP server — [Serply pricing](https://serply.io/pricing)

**Zyte API**
- "From $0.06 per 1,000 successful responses"; $5 free credit; website tiers HTTP $0.13–$1.27/1k PAYG, browser-rendered $1.01–$16.08/1k PAYG, with discounts at $100/$200/$500 commitments; no Google-SERP-specific price and no legal/compliance statement on the pricing page (accessed 2026-11-05) — [Zyte pricing](https://www.zyte.com/pricing/)

**Google's 2025 changes affecting all of the above**
- JavaScript requirement: effective ~January 15, 2025 (SerpApi) / announced January 17, 2025 (Oxylabs); Google spokesperson: protects "our services and users from bots and evolving forms of abuse and spam"; outages at some rank trackers (e.g., SERPrecon) and a shift toward headless browsers — [SerpApi blog](https://serpapi.com/blog/google-now-requires-javascript/); [TechRadar](https://www.techradar.com/pro/surviving-googles-javascript-rendering-shift-one-month-later); [Practical Ecommerce](https://www.practicalecommerce.com/googles-javascript-serps-impact-trackers-ai)
- `num=100` removal: rolled out gradually in September 2025, non-functional worldwide by late September; Google made no official statement and called the parameter "not an officially supported feature"; top-100 now requires ~10 paginated requests ("What once required 1,000 queries may now need 10,000"); Search Engine Land figure of 77% of sites reporting reduced keyword visibility; 87.7% of sites saw impression drops in one analysis; "professional providers adjusted their backend logic so users could keep retrieving 100 results" by paginating internally (Decodo article dated Oct 23, 2025) — [Decodo](https://decodo.com/blog/google-removes-num-100-parameter); [Idea Digital](https://ideadigital.agency/en/blog/google-removed-num100-parameter/); [Arc Intermedia](https://www.arcintermedia.com/shoptalk/google-disables-num100-parameter-what-it-means-for-seo-tracking/)

### Inferences
- Underlying engine: all of these are disclosed Google (and, for several, Bing/Yandex/Baidu/DDG) SERP scrapers; none claims an index of its own. Oxylabs' separate "Google JS" vs "Google non-JS" SKUs, and SerpApi's explanation that its premium tiers "solved Google's JavaScript challenge", are the clearest evidence that post-January-2025 Google scraping requires JS-capable rendering and that vendors pass that cost through (JS Google costs 35–80% more at Oxylabs).
- Effective cost of a 100-result Google pull after September 2025 is ~10x a 10-result pull wherever vendors bill per page/depth (DataForSEO, Apify, SerpApi throughput, ScrapingBee via `start`), so "price per 1k queries" comparisons must fix the depth at 10 results.
- Legal posture clusters: (a) indemnity-style "legal shield" marketing (SerpApi, SearchApi — both capped at $2M, U.S.-court-only for SerpApi); (b) silence plus "consult your lawyer" (Apify); (c) no statement at all (Bright Data, Oxylabs, Zyte pricing pages). None cites a specific court ruling on the pages fetched.
- MCP: confirmed first-party MCP for Apify (mcp.apify.com) and Serply; not confirmed for Serper, SerpApi, SearchApi, Bright Data, Oxylabs, DataForSEO, ZenRows, ScrapingBee, Scrapfly, Nimble, Traject Data, Zyte on the pages fetched.
- ZenRows implied Google price (inference, not a published SKU): Google requires JS + premium proxy = 25 credits, so ~$10.50/1k searches on Build $19 and ~$1.75/1k at Scale top tier.
- ScrapingBee implied Google price: 10–15 credits/search → ~$2.53–$3.80/1k on Hobby, ~$0.99–$1.49/1k on Startup, ~$0.75–$1.12/1k on Business+.

### Gaps
- SerpApi, Serper and SearchApi latency figures beyond vendor claims (no independent p50/p95 except Parallel's 999 ms p50 for SerpAPI, which is a competitor's measurement).
- Serper terms-of-service/legal posture text, MCP availability, and supported non-Google engines (none on the fetched page).
- SerpApi's supported-engine list and any statement on how it handled `num=100` removal.
- Zyte and Scrapfly Google-SERP-specific prices (require estimator/cost endpoint).
- Nimble: the conflict between $1.10/$5.00 (official docs) and the tracker's $1.50 → $5 change could not be resolved by date.
- Bright Data's own statement on JS/`num=100` handling; DataForSEO's minimum deposit and rate limits; Yandex support at DataForSEO.

## Key question 2: Official engine APIs (Google Programmable Search / Custom Search JSON API, Vertex AI Search and Gemini grounding, Bing Web Search retirement and Grounding with Bing, Yandex Search API, DuckDuckGo, SearXNG)

### Takeaway
The two historic "official" web-search APIs are gone or going: Microsoft retired all Bing Search APIs on August 11, 2025 (replacement: LLM-only "Grounding with Bing Search", now $14/1k transactions, no raw results), and Google's Custom Search JSON API is closed to new customers and will be discontinued January 1, 2027 (existing users: 100 free/day, $5/1k, 10k/day cap). What remains official is grounding-as-a-feature (Gemini: $35/1k grounded prompts on 2.5 models, $14/1k search queries on Gemini 3+; Vertex: $35 standard, $45 Enterprise Web Grounding), Yandex's paid XML/JSON API (~$4/1k sync), and nothing from DuckDuckGo beyond the Instant Answer API; SearXNG fills the gap as self-hosted meta-search but lives on engines' tolerance (Google reCAPTCHA suspends the engine for 7 days by default).

### Cited Findings

**Google Custom Search JSON API / Programmable Search Engine**
- "100 search queries per day for free"; beyond that $5 per 1,000 queries; up to 10,000 queries per day; the API "is closed to new customers"; existing customers can use it until January 1, 2027, when it is discontinued; Vertex AI Search recommended for up to 50 domains, "contact Google" for full web (accessed 2026-11-05) — [Google Custom Search overview](https://developers.google.com/custom-search/v1/overview)
- Secondary sources agree on the January 1, 2027 shutdown; one says closure to new customers began January 20, 2026, another that it closed in 2025 with the discontinuation announced January 2026; new projects reportedly get `403 PERMISSION_DENIED` (vendor blogs — Apify, Firecrawl, Brave, Searlo — all sell alternatives) — [Apify blog](https://blog.apify.com/google-custom-search-api-alternative/); [Brave](https://brave.com/learn/google-api-shutdown/); [Searlo](https://searlo.tech/google-custom-search-json-api-closed-to-new-customers); [Firecrawl](https://www.firecrawl.dev/blog/google-search-json-api-alternative)

**Gemini API — Grounding with Google Search (AI Studio pricing, accessed 2026-11-05)**
- Gemini 2.5 Pro / Flash / Flash-Lite: 1,500 RPD free (Flash and Flash-Lite share; 500 RPD on Standard/Priority), then $35 per 1,000 grounded prompts; "Gemini 2.5 models are billed per grounded prompt"; the tools table also says Google Search is "Not available for Pro", which conflicts with the 2.5 Pro section — [AI Studio pricing](https://aistudio.google.com/docs/pricing)
- Gemini 3 and newer (3.1 Pro Preview, 3.1 Flash-Lite, 3 Flash Preview, 3.5 Flash-Lite, 3.6 Flash, 3.8 Flash, Live models): 5,000 free requests per month shared across Gemini 3+ models, then $14 per 1,000 requests, billed per search query — "You will be charged for each individual search query performed"; default cap 1,500 requests/day/project; grounded context is not charged as input tokens — [AI Studio pricing](https://aistudio.google.com/docs/pricing)
- Google Maps grounding: $25/1k grounded prompts (2.5), $14/1k search queries (3+); URL context tool free, retrieved content billed as input tokens; 2.5 Pro/Flash requests route to Gemini 3.8 Flash / 3.5 Flash-Lite from December 1, 2026 — [AI Studio pricing](https://aistudio.google.com/docs/pricing)

**Vertex AI (Google Cloud)**
- Vertex pricing page: "even if multiple search queries are sent to Google Search, there is only one charge for a grounded prompt"; $35 per 1,000 grounded prompts; Web Grounding for Enterprise $45 per 1,000 grounded prompts; billed only when a prompt returns web results; a newer locale version adds 5,000 free search queries/month across Gemini 3 models then $14 per 1,000 search queries (from search snippets of Google's pages; the English page returned truncated content on 2026-11-05) — [Vertex AI pricing](https://cloud.google.com/vertex-ai/generative-ai/pricing); [Vertex AI pricing (ar)](https://cloud.google.com/vertex-ai/generative-ai/pricing?hl=ar)
- Vertex AI Search (standalone): 10,000 free queries/account/month; Search Standard $1.50/1k (Italian locale) or $2.00/1k (zh-tw locale) — inconsistent; Search Enterprise $4.00/1k (from search snippets) — [AI Applications pricing](https://cloud.google.com/generative-ai-app-builder/pricing); [AI Applications pricing (it)](https://cloud.google.com/generative-ai-app-builder/pricing?hl=it)

**Bing Web Search API retirement and Grounding with Bing Search**
- Microsoft Lifecycle notice (ms.date 2025-05-15): "Bing Search APIs will be retired on August 11, 2025. Any existing instances of Bing Search APIs will be decommissioned completely, and the product will no longer be available to be used or new customer signup. Customers are encouraged to migrate to Grounding with Bing Search as part of Azure AI Agents" — [Microsoft Lifecycle](https://learn.microsoft.com/en-us/lifecycle/announcements/bing-search-api-retirement)
- ppc.land (2025): announcement May 12, 2025; old Bing Search API tiers S1 $25, S2 $15, S3 $6 per 1,000 transactions (after a May 2023 increase); Grounding with Bing then priced at $35/1k transactions → increases of 40% (vs S1), 133% (vs S2), 483% (vs S3) — [ppc.land](https://ppc.land/microsoft-ends-bing-search-apis-on-august-11-alternative-costs-40-483-more/)
- Current Microsoft pricing (accessed 2026-11-05): Grounding with Bing Search $14 per 1,000 transactions, 150 transactions/second, 1 million transactions/day; Grounding with Bing Custom Search same; charges apply "for transactions that return summarized Bing results" — [Microsoft Bing grounding pricing](https://www.microsoft.com/en-us/bing/apis/grounding-pricing)
- Constraints (Foundry classic doc, ms.date 2026-03-06): "Developers and end users don't have access to raw content returned from Grounding with Bing Search"; must display website URLs and Bing search query URLs per Use and Display Requirements; `count` default 5, max 50; `freshness`, `market`, `set_lang`; only paid/PAYG Azure subscriptions eligible; customer data "is transferred outside of the Azure compliance boundary"; does not work with VPN/private endpoints; transactions counted per tool call per run; classic agents deprecated, retiring March 31, 2027 — [Bing grounding (classic)](https://learn.microsoft.com/en-us/azure/ai-foundry/agents/how-to/tools/bing-grounding)
- New Foundry Agent Service (ms.date 2026-04-08, updated 2026-09-17): recommends the new "Web Search" tool (GA; Microsoft-managed Bing resource; params `user_location`, `search_context_size` low/medium/high) over "Grounding with Bing Search" (GA; customer-managed resource; `count/freshness/market/set_lang`; supports non-OpenAI Azure models); both "submit queries to Bing" and both flow "outside Azure compliance boundary"; Microsoft Data Protection Addendum does not apply; Grounding with Bing Custom Search is Preview — [Foundry web grounding overview](https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/tools/web-overview)
- Commentary: Neowin argued Grounding with Bing "is not a real alternative" because raw content is inaccessible and pointed to Brave Search API; cloro.dev notes pre-retirement v7 calls now return HTTP 410 Gone — [Neowin](https://www.neowin.net/news/microsoft-pulls-plug-on-bing-search-apis/); [cloro.dev](https://cloro.dev/blog/bing-search-api-key/)

**Yandex Search API (Yandex Cloud / AI Studio, accessed 2026-11-05)**
- Billed per request (5xx/auth errors not billed); USD prices (net of VAT) via Iron Hive doo Beograd (Serbia) or Direct Cursus Technology L.L.C. (Dubai); RUB via Yandex.Cloud LLC: daytime synchronous ~$4.00/1k (₽488/1k); daytime deferred ~$0.25/1k (₽30.5/1k); night sync ~$3.00/1k, night deferred ~$0.21/1k (00:00–07:59 UTC+3); image search ~$7.50/1k; synchronous with generative response ~$41.64/1k (₽5,080/1k); no free tier stated; quotas via support — [Yandex Search API pricing](https://aistudio.yandex.ru/docs/en/search-api/pricing)

**DuckDuckGo**
- No official full-results API: the Instant Answer API (api.duckduckgo.com) returns instant answers, not full SERPs, and needs no key; vendors scrape "DuckDuckGo HTML" (html.duckduckgo.com) and warn it breaks on frontend changes; multiple Apify actors and RapidAPI listings sell hosted DDG scraping (vendor sources) — [DEV Community](https://dev.to/donnyautomation/how-to-search-the-web-without-googles-api-rate-limits-using-duckduckgo-search-api-58ab); [Apify DDG scraper](https://apify.com/jaybird/duckduckgo-scraper); [Apify DDG scraper (automation-lab)](https://apify.com/automation-lab/duckduckgo-scraper)

**SearXNG**
- "SearXNG is a free internet metasearch engine which aggregates results from up to 261 search services"; no tracking; public instances or self-host — [SearXNG docs](https://docs.searxng.org/)
- Search API: GET/POST on `/search` with `q`, `categories`, `language`, `pageno`, `time_range` (day/month/year), `format` (json/csv/rss), `safesearch`; "Requesting an unset format will return a 403 Forbidden error"; many public instances disable non-HTML formats — [SearXNG search API](https://docs.searxng.org/dev/search_api.html)
- `search.formats` default is `html` only (csv/json/rss must be enabled); engine suspension defaults: access denied (HTTP 402/403) 86,400 s (1 day); CAPTCHA 86,400 s; too many requests (HTTP 429) 3,600 s; Cloudflare CAPTCHA 1,296,000 s (15 days); Cloudflare access denied 86,400 s; Google reCAPTCHA (`recaptcha_SearxEngineCaptcha`) 604,800 s (7 days) — [SearXNG settings_search](https://docs.searxng.org/admin/settings/settings_search.html)
- User reports: Google engine on a public instance returning "Suspended: access denied"; a Lemmy thread reports developers saying there is no simple fix because Google actively hunts and blocks this traffic; public instances get rate-limited by big engines and self-hosting is the reliable workaround (community sources) — [SearXNG issue #2498](https://github.com/searxng/searxng/issues/2498); [Lemmy thread](https://lemmy.uninsane.org/post/757276)

### Inferences
- Bing grounding pricing moved from $35/1k (as reported at retirement in 2025) to $14/1k (Microsoft page, Nov 2026) — a price cut of 60% that coincides with Google pricing Gemini 3+ grounding at exactly $14/1k search queries; I infer competitive matching but have no statement from either company.
- Google's two grounding billing bases differ materially: per *grounded prompt* (2.5 models; multiple queries = one charge) vs per *search query* (3+ models; agentic multi-query prompts can cost several units). For the same prompt, $14/1k queries may be cheaper or costlier than $35/1k prompts depending on queries per prompt (break-even 2.5 queries/prompt).
- "Grounding" products (Bing, Gemini, Vertex Enterprise Web Grounding) are not SERP APIs: they return model-synthesized answers plus citations and (for Bing) forbid raw access; builders who need ranked raw results must use third-party wrappers or own-index APIs.
- SearXNG is viable for agents only when self-hosted with JSON enabled and Google de-prioritized or proxied; the 7-day reCAPTCHA suspension default means a single Google challenge removes Google from the mix for a week unless the admin intervenes.
- DuckDuckGo's web results have been Bing-syndicated historically; with Bing's API retired, DDG remains reachable only via HTML scraping, which several SERP vendors (SearchApi, Bright Data) sell.

### Gaps
- Official Google announcement text for the Custom Search JSON API closure (only the overview page's current wording and vendor blogs were found).
- English Vertex AI pricing page could not be read (truncated); the $35/$45/$14 figures rest on locale-variant pages via search snippets.
- Microsoft's dated announcement of the $35 → $14 Grounding with Bing price change.
- Yandex API rate limits (RPS) and any free quota.
- Any official DuckDuckGo statement on API policy (only vendor and community sources found).
- SearXNG official MCP integration (none in docs fetched); the limiter/bot-detection pages were not fetched.
- Hacker News discussion threads for the Bing retirement and Google SERP changes (search budget exhausted).

## Key question 3: LLM-platform built-in search tools (OpenAI, Anthropic, Google Gemini grounding, xAI Grok, Perplexity Sonar/Search API, Mistral, Cohere) — pricing and who supplies the index

### Takeaway
Platform search tools cluster at $5–$14 per 1k calls plus tokens: xAI web_search $5/1k, Perplexity Search API $5/1k (fast $1/1k) and Agent API web_search $2.50/1k, OpenAI $10/1k (+ content tokens; $25/1k preview on non-reasoning models), Anthropic $10/1k, Google Gemini 3+ $14/1k queries (2.5: $35/1k prompts), Microsoft Bing grounding $14/1k; Mistral is reported at $30/1k by third parties; Cohere deprecated its web-search connector on September 15, 2025. None of OpenAI, Anthropic, xAI or Mistral discloses its index on its pricing/tool docs; the best evidence is Bing + OAI-SearchBot for OpenAI (2024) and Brave Search for Anthropic (March 2025), while Google and Microsoft are explicitly first-party and Perplexity runs its own stack.

### Cited Findings

**OpenAI (Responses API web search), accessed 2026-11-05**
- "Web search (all models): $10.00 / 1k calls + Search content tokens billed at model rates"; Image Web search same; "Web search preview (reasoning models, including gpt-5, o-series): $10.00 / 1k calls + Search content tokens billed at model rates"; "Web search preview (non-reasoning models): $25.00 / 1k calls + Search content tokens are free"; for gpt-4o-mini / gpt-4.1-mini with the non-preview tool, search content is billed as "a fixed block of 8,000 input tokens per call"; file search $2.50/1k calls — [OpenAI pricing](https://developers.openai.com/api/docs/pricing)
- Tool docs: `web_search` recommended, `web_search_preview` legacy; `search_context_size` low/medium (default)/high with no fixed token count; `filters` up to 100 allowed or 100 blocked domains; `user_location`; actions `search`, `open_page`, `find_in_page`; `sources` include real-time feeds labeled `oai-sports`, `oai-weather`, `oai-finance`; web search context window capped at 128k tokens; `gpt-5-search-api` is the Chat Completions search model; `gpt-4o-search-preview` / `gpt-4o-mini-search-preview` shut down 2026-07-23; the page "doesn't name the search index or provider" — [OpenAI web search guide](https://developers.openai.com/api/docs/guides/tools-web-search)
- Index evidence (2024 reporting): OpenAI's VP of Engineering said in a Reddit AMA that Bing is "an important part of the stack"; OAI-SearchBot is OpenAI's own crawler for ChatGPT search; one analysis says OpenAI stopped naming Bing publicly but still treats it as the likely main source; one outlet claimed OpenAI uses Google results behind the scenes (single report, uncorroborated) — [Search Engine Roundtable](https://www.seroundtable.com/bing-powers-chatgpt-search-38345.html); [BotMonster](https://botmonster.com/ai/ai-web-search-backends-who-owns-who-rents/); [InfoQ](https://www.infoq.com/news/2024/11/chatgpt-search-release); [inkl](https://www.inkl.com/news/chatgpt-is-using-google-search-to-answer-your-questions-here-s-what-we-know)
- Benchmark: Artificial Analysis (Oct 19, 2026): OpenAI Web Search (medium) Search Index 74, DeepSearchQA 78, BrowseComp 74, AA-Omniscience 72, search cost $40.19/1k tasks, model $9.40/1k, 33.3 s/task — [Artificial Analysis](https://artificialanalysis.ai/agents/search-api); Parallel (Oct 2026) cites OpenAI web search at 48.3% on FinSearchComp T3 at $204.30/1k — [Parallel best AI search for agents](https://parallel.ai/articles/best-ai-search-for-agents.md)

**Anthropic (Claude web_search server tool), accessed 2026-11-05**
- "Web search is available on the Claude API for $10 USD per 1,000 searches, plus standard token costs for search-generated content"; "Each web search counts as one use, regardless of the number of results returned"; errored searches not billed; `usage.server_tool_use.web_search_requests` counts them; Batches API same price — [Claude web search tool](https://platform.claude.com/docs/en/docs/agents-and-tools/tool-use/web-search-tool)
- Tool versions `web_search_20250305` (basic), `web_search_20260209` (dynamic filtering: Claude writes code that filters results before they hit context), `web_search_20260318` (`response_inclusion`); `max_uses`; `allowed_domains` or `blocked_domains` (not both); `user_location`; results carry `encrypted_content` that must be passed back; citations always on, `cited_text` ≤150 chars; "When displaying API outputs directly to end users, citations must be included to the original source"; available on Claude API, AWS, Google Cloud (Anthropic-managed), Microsoft Foundry; ZDR-eligible except dynamic filtering; the doc does not name the search backend — [Claude web search tool](https://platform.claude.com/docs/en/docs/agents-and-tools/tool-use/web-search-tool)
- Index evidence (March 21, 2025): Anthropic added "Brave Search" to its subprocessor list; Simon Willison found a `BraveSearchParams` parameter in Claude's web search; identical citations observed between Claude and Brave; TechCrunch headline "Anthropic appears to be using Brave to power web searches" — [Simon Willison](https://simonwillison.net/2025/Mar/21/anthropic-use-brave/); [TechCrunch](https://techcrunch.com/2025/03/21/anthropic-appears-to-be-using-brave-to-power-web-searches-for-its-claude-chatbot/)

**Google Gemini grounding** — see Key question 2 ($35/1k grounded prompts on 2.5; $14/1k search queries on 3+; 5,000 free/month) — [AI Studio pricing](https://aistudio.google.com/docs/pricing). Index: first-party Google Search (disclosed by product name).

**xAI Grok, accessed 2026-11-05**
- Tool invocation pricing: Web Search `web_search` $5 per 1k calls; X Search `x_search` $5 per 1k posts and $10 per 1k profiles (billed per item returned); Code Execution $5/1k; Collections Search $2.50/1k; Image Search billed at Web Search rate; Remote MCP tools token-only — [xAI pricing](https://docs.x.ai/developers/pricing)
- Web Search tool: `allowed_domains` / `excluded_domains` up to 5 each (mutually exclusive); `enable_image_understanding`, `enable_image_search`; examples use `grok-4.7`; available through xAI SDK, OpenAI Responses API compatibility, Vercel AI SDK — [xAI web search](https://docs.x.ai/docs/guides/live-search)
- Legacy "Live Search" (`search_parameters`) pricing of $25 per 1,000 sources ($0.025/source, counted via `response.usage.num_sources_used`, sources web/X/news/RSS) appears only in third-party sources; current xAI docs do not mention Live Search — [theneuralbase](https://theneuralbase.com/xai-grok/learn/advanced/live-search-advantage/); [feedbagel](https://feedbagel.com/post/xai-grok-model-pricing-and-tool-costs-documentation)

**Perplexity, accessed 2026-11-05**
- Search API: $5.00 per 1k successful `POST /search` requests (standard); Fast Search (`search_type: "fast"`) $1.00 per 1k; "charges for each successful POST /search request, not for each query in the request" (up to five queries per request = one billing unit); invalid/rate-limited/upstream-failed requests not billed — [Perplexity pricing](https://docs.perplexity.ai/docs/getting-started/pricing.md)
- Agent API tools: `web_search` $0.0025/call ($2.50/1k), fast $0.001 ($1/1k); `image_search` $0.0025; `fetch_url` $0.0005; `people_search` / `finance_search` $0.005; sandbox $0.03/session + $0.0025 per SDK search; Decisions API web_grounding $0.001 per search and per fetch — [Perplexity pricing](https://docs.perplexity.ai/docs/getting-started/pricing.md)
- Sonar family: not on the current official pricing page. Third-party summaries: Sonar $1/M tokens + per-1k-request fee $5 (low) / $8 (medium) / $12 (high); Sonar Pro $3 in / $15 out per M + $6 / $10 / $14 per 1k requests; Sonar Reasoning Pro same request fees; one third-party source says Sonar is supported until 27 September 2026 and points new builds to the Agent API (unverified against Perplexity's changelog) — [Puter](https://developer.puter.com/tutorials/perplexity-api-pricing/); [Amnic](https://amnic.com/blogs/perplexity-api-pricing); [costbench](https://costbench.com/software/ai-search-apis/perplexity-sonar-api/)
- Index: Parallel describes Perplexity as running its "own search stack" — [Parallel](https://parallel.ai/articles/most-powerful-search-api-for-ai.md)
- Benchmarks: AA (Oct 19, 2026) Perplexity Search (medium) Search Index 80 (top, tied with Exa auto), BrowseComp 87, DeepSearchQA 81, Omniscience 72, search cost $62.30/1k tasks, 31.4 s; (high) 79, $56.93/1k — [Artificial Analysis](https://artificialanalysis.ai/agents/search-api); Parallel (Sept 9, 2026, 50 Qs): Perplexity 74% / $275 per 1k (frontier GPT-5.6 Sol), 46% / $37.1 (low-cost GPT-5.6 Luna) — [Parallel](https://parallel.ai/articles/browsecomp-benchmark.md)

**Mistral**
- Connectors `web_search` ("A simple web search tool that enables access to a search engine") and `web_search_premium` (adds news articles "with integrated news provider verification"); Conversations/Agents API only, not Chat Completions; org-level domain allow/block lists; blocked `open_url` returns 451; no provider named and no price on the docs page (accessed 2026-11-05) — [Mistral websearch connector](https://docs.mistral.ai/agents/connectors/websearch)
- Official pricing page: "tool APIs are priced per call" without rates; Le Chat plans show web search "Up to 5x free" for paid tiers — [Mistral pricing](https://mistral.ai/pricing)
- Third-party: web search $30 per 1,000 calls (and code execution $30/1k, image generation $100/1k images) — [Puter Mistral pricing](https://developer.puter.com/tutorials/mistral-api-pricing/); [CurlScape](https://curlscape.com/blog/mistral-api-pricing-2026)

**Cohere**
- Managed `web-search` connector existed in the Chat API; "Cohere's connector parameter was deprecated on September 15, 2025"; Cohere recommends multi-step tool use instead; no provider or price stated (accessed 2026-11-05) — [Cohere connectors overview](https://docs.cohere.com/docs/overview-rag-connectors)

### Inferences
- Who supplies the index (disclosed vs inferred): Google Gemini/Vertex = Google (disclosed); Microsoft Foundry Web Search / Bing grounding = Bing (disclosed); Perplexity = own stack (vendor and competitor statements); OpenAI = Bing index + own OAI-SearchBot crawl (inferred from 2024 statements; not in current docs); Anthropic = Brave Search (inferred from March 2025 subprocessor list and `BraveSearchParams`; not confirmed current); xAI = undisclosed (X data is first-party; web index unknown); Mistral = undisclosed; Cohere = no built-in web search since Sept 2025 (inferred from connector deprecation).
- "Per call" is not comparable across platforms: Anthropic and xAI bill per search invocation; OpenAI bills per call plus content tokens (or fixed 8k-token blocks on mini models); Gemini 3+ bills per query inside a prompt; Gemini 2.5 and Vertex bill per prompt. For an agent issuing 3 queries per turn, Gemini 3+ ($42) ≈ OpenAI ($30 + tokens) ≈ Anthropic ($30) > Gemini 2.5 ($35 flat) > xAI/Perplexity ($15 / $7.50).
- xAI appears to have replaced source-count billing ($25/1k sources) with per-call billing ($5/1k calls); the absence of Live Search from current docs implies deprecation, but no dated notice was found.
- Perplexity appears to be steering API customers from Sonar (bundled model + search, per-request fee by context size) to the Search API / Agent API (unbundled), given Sonar's absence from the official pricing page; the "supported until 27 Sept 2026" claim is third-party only.

### Gaps
- Official OpenAI/Anthropic/xAI/Mistral statements about their current search index provider (none in docs fetched; OpenAI and Anthropic evidence is from 2024–2025 reporting).
- Mistral's official per-call connector price and whether `web_search_premium` uses a named news partner.
- xAI official deprecation notice for Live Search and the date of the pricing change.
- Perplexity's official Sonar pricing and sunset notice (search budget exhausted before the Sonar page could be located).
- Cohere's current recommended web-search path (which third-party tool, if any).

## Key question 4: Meta-search / aggregation layers used by agents (Jina s.jina.ai, Firecrawl /search, Tavily, mcp-omnisearch, Linkup, You.com)

### Takeaway
These layers sit between agents and engines, charge $1.50–$8 per 1k searches, and mostly do not disclose what they query: Jina returns the top-5 results for a fixed ≥10,000-token charge; Firecrawl bills 2 credits per 10 results (≈$1.50–$10/1k by plan) and exposes Google-syntax `tbs=qdr:` time filters and an "upstream search provider" — strong but circumstantial evidence it fronts a Google-derived SERP; Tavily (1,000 free credits/month, $8/1k credits PAYG) describes itself as aggregating up to 20 sites per call and is described by analysts as having no index of its own; Linkup ($5–6/1k) and You.com ($5/1k, up to 100 results, "licensed data providers") are partially partner-based; mcp-omnisearch is an MIT MCP server that fans out to Tavily, Brave, Kagi, Exa, Linkup, Firecrawl and GitHub.

### Cited Findings

**Jina AI (s.jina.ai), accessed 2026-11-05**
- Search API: "Every request costs a fixed number of tokens, starting from 10,000 tokens"; returns "the top five results with their URLs and contents"; rate limits: no key = blocked, free key 100 RPM, paid key 100 RPM, premium key 1,000 RPM; average latency 2.5 s; Reader (r.jina.ai): 20 RPM without key, 500 RPM with key, 5,000 RPM premium, 7.9 s average latency; "Every new API key comes with 10M free tokens"; no backing engine disclosed — [Jina rate limits](https://jina.ai/api-dashboard/rate-limit); [Jina Reader](https://jina.ai/reader/)

**Firecrawl /search, accessed 2026-11-05**
- Credits: "Search costs 2 credits per 10 results, rounded up"; scrape add-on 1 credit/page (PDF 1 credit/page, JSON mode +4); ZDR enterprise 10 credits per 10 results; sources `web`, `news`, `images`, `alexandria`; categories `research` (moving to a PubMed/arXiv "Research Index" on 2026-11-16), `pdf`, `developer`, `gov`; time filters `tbs` = `qdr:h/d/w/m/y`, `sbd:1`, `cdr:1,cd_min,cd_max` (web only); `location`; the docs refer only to an "upstream search provider" and do not name the engine — [Firecrawl search docs](https://docs.firecrawl.dev/features/search)
- Plans: Free 1,000 credits; Hobby $19 / 5,000; Standard $99 / 100,000; Growth $399 / 500,000; Scale $749 / 1,000,000; PAYG $5 per 1,000 / 2,000 / 2,500 / 5,000 credits by plan → implied per 1k 10-result searches: Hobby ~$7.60 (PAYG $10), Standard ~$1.98 ($5), Growth ~$1.60 ($4), Scale ~$1.50 ($2) — [Firecrawl pricing](https://www.firecrawl.dev/pricing)
- Benchmarks: AA (Oct 19, 2026): Firecrawl Search Index 73, BrowseComp 74, Omniscience 73, search cost $30.48/1k tasks, 61.9 s/task (slowest in table) — [Artificial Analysis](https://artificialanalysis.ai/agents/search-api); AA launch (Aug 18, 2026) scored Firecrawl 73 — [The Decoder](https://the-decoder.com/new-benchmark-ranks-search-apis-for-ai-agents-on-quality-cost-and-speed/)

**Tavily, accessed 2026-11-05**
- Pricing: Researcher (free) 1,000 credits/month, reset on the 1st; Pay As You Go $0.008 per credit (= $8 per 1k credits, my arithmetic); Project $30/mo for 4,000 credits with "Higher rate limits"; Enterprise custom; 100k free credits via startup program; credit cost per request type is "in the documentation" (not on the page) — [Tavily pricing](https://www.tavily.com/pricing)
- Index: Tavily docs describe "aggregating up to 20 sites per a single API call" then ranking; Tavily FAQ contrasts itself with "Bing, Google, or SerpAPI"; Sacra: Tavily "does not maintain its own search index, instead it fans out to multiple data sources and search engines in real time"; cloro.dev: Tavily "isn't scraping Google's results page and it isn't reselling a single third-party index" but results overlap heavily with Google's top domains; APIScout contradicts itself (says own index, table says "Aggregated") — [Tavily docs](https://docs.tavily.com/documentation/about); [Tavily FAQ](https://docs.tavily.com/faq/faq.md); [Sacra](https://sacra.com/chat/h/ea40129a-9577-4876-a178-a119243006be/); [cloro.dev](https://cloro.dev/blog/tavily-vs-google-search/); [APIScout](https://apiscout.dev/guides/tavily-vs-serpapi-vs-brave-search-api-2026)
- Benchmarks (Parallel, Sept 9, 2026, 50 Qs): Tavily 66% BrowseComp at $935/1k (frontier), 32% at $176/1k (low-cost); Basic mode 1.88 s mean latency on factual lookups (Openbenchmarks); Parallel's July 10–12, 2026 run listed Tavily at 19.3% and 357 ms (from search snippet) — [Parallel](https://parallel.ai/articles/most-powerful-search-api-for-ai.md); [Parallel best web search API](https://parallel.ai/articles/best-web-search-api)

**Linkup, accessed 2026-11-05**
- Pricing: "Run 4,000 queries for free"; Search $0.005–$0.006 per request (Fast/Standard/Deep) ≈ $5–$6/1k; Fetch $0.001–$0.006; Research $0.25–$2.50 (async, 1–10 min); SOC 2 Type II all plans; ZDR on Enterprise; Enterprise offers "personalized indexes" and "dedicated refresh rate of the index"; $5,000 startup credits — [Linkup pricing](https://www.linkup.so/pricing)
- Claims: "#1 among sub-second web search APIs on Verified SimpleQA, with a 94% F-score"; "#1 ... on SealQA-0, with 61% accuracy"; Flash search <200 ms; other modes 1–30 s; "Define which sources to trust, which domains to prefer, which proprietary data to blend in"; no engine or partner named — [Linkup docs](https://docs.linkup.so/pages/documentation/get-started/introduction)

**You.com, accessed 2026-11-05**
- Web Search $5.00 per 1,000 calls, web + news in one request, up to 100 results per call; full-page extraction add-on $1.00 per 1,000 live-crawled pages (cached free under `blend`); Contents $1.00/1k pages; Answer $5.00/1k calls; Research lite $12 / standard $50 / deep $100 / exhaustive $450 / frontier $1,200 per 1k; Finance Research $110–$500; "Web Search includes Knowledge results from licensed data providers at no extra cost"; Finance uses "a purpose-built financial index"; enterprise "Custom QPS Limits" — [You.com billing](https://you.com/docs/administration/billing)
- Price cut announced March 11, 2026 to "$5 per 1,000 calls" flat regardless of result count (previously tiered, e.g., $8/1k for 51–100 results); new accounts get $100 free credits (from search snippets) — [You.com announcement](https://about.you.com/resources/lower-search-api-cost); [UsagePricing](https://usagepricing.com/blueprint/activity/you-com-2026-04-price-change)
- Benchmark: AA (Oct 19, 2026) You.com Search (highlights) Search Index 74, BrowseComp 77, search cost $47.54/1k tasks, model cost $19.41/1k, 21.5 s — [Artificial Analysis](https://artificialanalysis.ai/agents/search-api)

**mcp-omnisearch (spences10)**
- MIT-licensed MCP server, 358 stars, 479 commits; four tools `web_search`, `ai_search`, `github_search`, `web_extract`; providers: Tavily, Brave, Kagi, Exa (search); Kagi FastGPT, Exa Answer, Linkup, Tavily Research (AI answers); Firecrawl, Tavily, Exa (extraction); GitHub; providers without keys are skipped (accessed 2026-11-05) — [mcp-omnisearch](https://github.com/spences10/mcp-omnisearch)

### Inferences
- Firecrawl's `tbs=qdr:h|d|w|m|y` and `cdr:1,cd_min,cd_max` syntax is Google's own URL parameter grammar; combined with the "upstream search provider" wording in the ZDR section, I infer Firecrawl's web source is a Google-derived SERP obtained via a SERP provider or its own scraping. Firecrawl does not say this.
- ScrapingBee passing `gl/hl/num/start` and Firecrawl passing `tbs` both show how Google's parameter vocabulary leaks through wrapper layers; Jina gives no such tell.
- Tavily, Linkup and You.com are "hybrid" layers: real-time fan-out/rerank plus some licensed or proprietary data; none of them publishes a provider list, so the "who sits on top of whom" picture for them is partially inferred.
- mcp-omnisearch is itself a meta-layer over meta-layers (Tavily → engines; Linkup → partners), so an agent using it can be three hops from the underlying index.

### Gaps
- Jina token-pack prices (dollars per billion tokens), so the dollar cost of a 10,000-token search could not be computed.
- Tavily's per-request credit costs (basic vs advanced) and RPM limits (not on the pricing page).
- Any disclosure by Firecrawl, Jina, Tavily, Linkup or You.com of the engine(s) they query; You.com's "licensed data providers" are unnamed.
- Independent latency measurements for Jina, Linkup and You.com beyond vendor claims.

## Key question 5: Published benchmark results (BrowseComp, Artificial Analysis Search Index, vendor comparisons)

### Takeaway
Two public references exist as of November 2026: Artificial Analysis's Search Index (launched Aug 18, 2026; Oct 19, 2026 snapshot: Perplexity Search medium and Exa auto tied at 80, OpenAI Web Search 74, You.com 74, Nimble 74, Firecrawl 73, with a 33-point model-only baseline) and Parallel's own BrowseComp runs (vendor-run; Sept 9, 2026: Parallel Advanced 74%, Perplexity 74%, Exa 70%, Tavily 66% with GPT-5.6 Sol; July 2026: SerpAPI 23.3% at 999 ms p50 vs Parallel 51% with GPT-5.4). No SERP wrapper (SerpApi, Serper, Bright Data, etc.) appears on the Artificial Analysis board; the only SERP-wrapper BrowseComp figure found is Parallel's 23.3% for SerpAPI.

### Cited Findings
- Artificial Analysis Search Index (Oct 19, 2026; candidate model GPT-5.6 Luna medium; index = equal-weighted mean of DeepSearchQA, BrowseComp, AA-Omniscience; 200 BrowseComp questions): Exa Search (auto, dynamic highlights) 80 / BrowseComp 83 / $53.17 search + $10.60 model per 1k tasks / 36.9 s; Perplexity Search (medium) 80 / 87 / $62.30 + $8.04 / 31.4 s; Exa (lite) 79 / 81 / $31.20; Perplexity (high) 79 / 86 / $56.93; Octen Search (highlights) 77 / 86 / $9.07 + $14.50 / 15.8 s; Parallel Search (advanced) 75 / 77 / $47.93 / 40.0 s; Brave Search (LLM context) 75 / 77 / $61.96 + $16.95 / 22.8 s; OpenAI Web Search (medium) 74 / 74 / $40.19 + $9.40 / 33.3 s; You.com Search (highlights) 74 / 77 / $47.54 + $19.41 / 21.5 s; Nimble Search (standard) 74 / 75 / $46.14 + $16.64 / 24.6 s; Firecrawl Search 73 / 74 / $30.48 + $11.58 / 61.9 s; DeepSeek Search (summary) 69 / 63 / $8.47 + $20.19; Model only (no search) 33 / 17 / $2.92; page claims 26 products across 14 providers but shows 13 rows; FAQ cites TinyFish Search as cheapest at $0/1k tasks (not in table); Tavily, Serper, SerpApi, Linkup, Jina and Google are absent — [Artificial Analysis Search API](https://artificialanalysis.ai/agents/search-api)
- AA launch (Aug 18, 2026): Parallel advanced 75, Exa auto 74, Firecrawl 73, Parallel basic 73; methodology: same fixed candidate model so only the search provider varies — [The Decoder](https://the-decoder.com/new-benchmark-ranks-search-apis-for-ai-agents-on-quality-cost-and-speed/); [AA methodology](https://artificialanalysis.ai/methodology/search-api)
- Parallel agent-loop BrowseComp (Sept 9, 2026; 50-question sample of 1,266; LLM judge; cost includes tokens + tool calls): frontier (GPT-5.6 Sol high): Parallel Advanced 74% / $399 per 1k, Perplexity 74% / $275, Parallel Basic 72% / $612, Exa Auto 70% / $971, Tavily 66% / $935; low-cost (GPT-5.6 Luna low): Perplexity 46% / $37.1, Parallel Fast 44% / $11.8, Exa Auto 36% / $53.4, Parallel Turbo 32% / $13.2, Tavily 32% / $176; author states bias toward Parallel — [Parallel BrowseComp explained](https://parallel.ai/articles/browsecomp-benchmark.md); [Parallel most powerful search API](https://parallel.ai/articles/most-powerful-search-api-for-ai.md)
- Parallel deep-research/Task API runs (Aug 26, 2026; 100 Qs): Parallel Ultra4x 94% / $1,200 per 1k; Ultra 92% / $300; Core 91% / $25; Lite 88% / $5; Perplexity (high) 86% / $441.5; GPT-5.6 Sol PTC (max) 85% / $791.1; Exa Agent Max 78% / $1,043.5; Gemini 3.1 Pro (high) 72% / $194.4 — [Parallel BrowseComp explained](https://parallel.ai/articles/browsecomp-benchmark.md)
- Parallel July 10–12, 2026 run (from search snippets of Parallel pages): SerpAPI 23.3% accuracy, 999 ms p50 search latency; Tavily 19.3%, 357 ms; Parallel 51% vs SerpApi 23.3% (+27.7 points) with the same GPT-5.4 agent; "Neither Artificial Analysis nor Openbenchmarks tests SerpApi" — [Parallel vs SerpApi](https://parallel.ai/compare/serpapi-vs-parallel); [Parallel best web search API](https://parallel.ai/articles/best-web-search-api)
- Latency (Openbenchmarks via Parallel, Sept 2026, factual lookups, mean): Parallel Turbo 348 ms; Exa Instant 398 ms; Brave 601–630 ms; Tavily Basic 1.88 s — [Parallel most powerful search API](https://parallel.ai/articles/most-powerful-search-api-for-ai.md)
- Other vendor claims: Linkup 94% F-score on Verified SimpleQA — [Linkup docs](https://docs.linkup.so/pages/documentation/get-started/introduction); OpenAI web search 48.3% on FinSearchComp T3 at $204.30/1k (Parallel, Oct 2026) — [Parallel best AI search for agents](https://parallel.ai/articles/best-ai-search-for-agents.md)
- BrowseComp itself: OpenAI benchmark of 1,266 hard fact-seeking questions released April 10, 2025 — [Parallel BrowseComp explained](https://parallel.ai/articles/browsecomp-benchmark.md)

### Inferences
- The SERP-wrapper tier (raw Google SERP, 10 blue links, no content extraction) scores far below agent-oriented APIs on BrowseComp in the only available head-to-head (23.3% vs 44–74%), mainly because wrappers return snippets rather than page content; this is a format effect as much as an index-quality effect.
- Benchmark results depend heavily on the agent model and harness: the same provider (Perplexity) ranges from 46% (Luna, low) to 74% (Sol, high) to 86–87 (AA, 200 Qs); cross-table comparisons are only approximate.
- The "OpenAI web search 57.7% BrowseComp" figure named in the assignment did not appear in any page fetched; the closest OpenAI figures found are AA's 74 (BrowseComp component, Oct 2026) and 48.3% on FinSearchComp T3.

### Gaps
- Source for "OpenAI web search 57.7% BrowseComp" (not found in Parallel's or AA's pages fetched; may be an older Parallel run).
- Independent (non-vendor) BrowseComp numbers for any SERP wrapper other than SerpAPI (Serper, Bright Data, Oxylabs, DataForSEO are untested publicly).
- AA's full 26-product configuration list (Tavily basic was reported as configured but is absent from the Oct 19 table fetched).
- Openbenchmarks' own pages were not fetched; latency figures are as relayed by Parallel.

## Key question 6: Cost comparison (normalized price per 1k queries at smallest paid tier and at scale), comparison table, and "who sits on top of whom"

### Takeaway
At the smallest paid tier, raw Google SERP access costs $1–$5/1k from scraping specialists (Serper $1.00, Oxylabs $1.00–$1.35, Bright Data $1.50, DataForSEO $0.60–$2.00, SearchApi $4.00) but $15–$25/1k from SerpApi's small plans and $7.60–$10/1k from Firecrawl's Hobby tier; at scale the floor is $0.25–$0.60/1k (Oxylabs, Serper, DataForSEO). LLM-platform search tools are 5–30x costlier per call ($5–$14/1k, Mistral reportedly $30/1k) but bundle synthesis/citations; official grounding products ($14–$45/1k) sit at the top. Structurally, the market is three layers deep: Google/Bing/Yandex/Baidu/Brave/own indexes at the bottom; scrapers and licensed resellers in the middle; agent-facing meta-layers (Tavily, Firecrawl, Jina, Linkup, You.com, mcp-omnisearch) and LLM-platform tools on top.

### Cited Findings

Comparison table (per 1k queries at 10 results unless noted; "entry" = smallest paid tier; "scale" = largest published tier; all accessed 2026-11-05 unless dated; each row's source is in the relevant section above):

| Provider / tool | Underneath (D = disclosed, I = inferred) | Result format | Entry $/1k | Scale $/1k | Latency claim | Rate limit | Legal posture | MCP | Benchmark |
|---|---|---|---|---|---|---|---|---|---|
| Serper.dev | Google (D) | JSON SERP | $1.00 (Starter $50) | $0.30 (Ultimate) | 1–2 s (2–4 s w/ retry) | 50–300 QPS | none stated | not stated | none |
| SerpApi | Google + others (D; list not on page) | JSON SERP | $25.00 (Starter) / $10.00 (Production) | $1.96 (Cloud 54M) | speed tiers 2x/4x price | per-hour throughput | $2M US Legal Shield (Production+) | not stated | 23.3% BrowseComp, 999 ms p50 (Parallel, Jul 2026) |
| SearchApi.io | Google, Bing, Yandex, Baidu, DDG, Yahoo, Naver + ~80 (D) | JSON SERP | $4.00 (Developer) | $1.00 (Octo 5M) | "seconds"; 99.9% SLA | 20% of credits/hr | $2M Legal Protection (Production+) | not stated | none |
| Bright Data SERP | Google, Bing, DDG, Yandex, Baidu, Yahoo, Naver (D) | HTML/JSON/MD | $1.50 (PAYG) | $1.30 (Scale) | <5 s | unlimited concurrency | none stated | not stated | none |
| Oxylabs | Google, Baidu, Bing, Yandex (D) | HTML/JSON | $1.00 non-JS / $1.35 JS | $0.50 non-JS / $0.90 JS | 6.04 s avg (Proxyway) | not stated | none stated | not stated | none |
| DataForSEO | Google, Bing, Yahoo, Baidu, Naver, Seznam, YouTube (D) | JSON | $0.60 std / $1.20 priority / $2.00 live | same (depth +1 base per 10) | 5 min / 1 min / 6 s | not stated | none stated | not stated | none |
| ZenRows | Google via generic scraper (I: 25 credits) | HTML/JSON | ~$10.50 (I) | ~$1.75 (I) | n/a | 5–400 concurrent | none stated | not stated | none |
| ScrapingBee | Google (D; 10–15 credits) | JSON | ~$2.53–$3.80 | ~$0.75–$1.12 | n/a | 25–900 concurrent | none stated | not stated | none |
| Scrapfly | Google via generic scraper (D; cost via estimator) | HTML/JSON | not published | not published | n/a | 5–100 concurrent | none stated | not stated | none |
| Apify Google Search Scraper | Google (D) | JSON per page | $1.80 per 1k pages | lower on higher plans | n/a | plan-based | "consider Google ToU" | yes (mcp.apify.com) | none |
| Nimble Search | own "Search API" (D product; engine not stated) | JSON (+full content) | $1.10 Lite / $5.00 Standard | plans from $2,500/mo | n/a | n/a | none stated | not stated | AA 74; BrowseComp 75; $46.14/1k tasks (Oct 2026) |
| Scale SERP (Traject) | Google (D) | JSON | $23.00 (1k plan) / $6.60 (10k) | $1.00 (5M) | n/a | batches | "not affiliated with Google" | not stated | none |
| Value SERP (Traject) | Google (D) | JSON | $2.00 (25k plan) / $2.50 PAYG | $1.00 (1M) | n/a | 250–1,500/min | none stated | not stated | none |
| Serply | Google, Bing (D) | JSON | $2.00 (Micro) | $0.75 (Pro+) | n/a | not stated | none stated | yes | none |
| Zyte API | generic (Google price not shown) | HTML/extract | $0.13–$1.27 HTTP | $0.06 floor | n/a | n/a | none stated | not stated | none |
| Google Custom Search JSON API | Google (D) | JSON, 10/req | $5.00 after 100 free/day | $5.00 (10k/day cap) | n/a | 10k/day | closed to new; ends 2027-01-01 | no | none |
| Gemini Grounding (2.5) | Google (D) | synthesized + citations | $35/1k grounded prompts (1,500 RPD free) | same | n/a | 1,500 RPD | first-party ToS | n/a | n/a |
| Gemini Grounding (3+) | Google (D) | synthesized + citations | $14/1k search queries (5,000/mo free) | same | n/a | 1,500 RPD default | first-party ToS | n/a | n/a |
| Vertex Enterprise Web Grounding | Google (D) | synthesized | $45/1k grounded prompts | same | n/a | n/a | first-party | n/a | n/a |
| Grounding with Bing Search (Foundry) | Bing (D) | synthesized only; no raw | $14/1k transactions | same | n/a | 150 TPS; 1M/day | outside Azure compliance boundary; display rules | n/a | n/a |
| Yandex Search API | Yandex (D) | XML/JSON | ~$4.00 sync / ~$0.25 deferred | same | n/a | quotas | Serbian/Dubai/RU entities | no | n/a |
| SearXNG (self-host) | up to 261 engines incl. Google (D) | JSON if enabled | $0 (infra only) | $0 | engine-dependent | engine suspension (Google reCAPTCHA 7 d) | relies on engine tolerance | not in docs | n/a |
| OpenAI web_search | Bing + OAI-SearchBot (I, 2024) | synthesized + url_citation + sources | $10/1k calls + content tokens ($25 preview non-reasoning) | same | n/a | model tier | citations must be prominent links | n/a | AA 74; BrowseComp 74; $40.19/1k tasks |
| Anthropic web_search | Brave Search (I, Mar 2025) | encrypted results + citations | $10/1k searches + tokens | same | n/a | org limit | citations required for end users | n/a | not on AA board |
| xAI web_search | undisclosed (+ X first-party) | synthesized + citations | $5/1k calls | same | n/a | n/a | n/a | n/a | none |
| Perplexity Search API | own stack (D via competitor) | ranked results | $5/1k requests ($1 fast) | same | n/a | tiers | n/a | n/a | AA 80; BrowseComp 87; $62.30/1k tasks |
| Perplexity Agent web_search | own stack | tool results | $2.50/1k calls ($1 fast) | same | n/a | tiers | n/a | n/a | — |
| Mistral web_search connector | undisclosed | citations | $30/1k (third-party) | same | n/a | n/a | n/a | n/a | none |
| Cohere | connector deprecated 2025-09-15 | — | — | — | — | — | — | — | — |
| Jina s.jina.ai | undisclosed | top-5 URLs + content | ≥10,000 tokens/req (pack price unknown) | same | 2.5 s avg | 100–1,000 RPM | n/a | n/a | none |
| Firecrawl /search | "upstream search provider" (Google-syntax tbs → I: Google-derived) | results + optional scrape | ~$7.60 (Hobby) / $10 PAYG | ~$1.50 (Scale) / $2 PAYG | 61.9 s/task (AA) | plan-based | ZDR enterprise | yes (Firecrawl MCP widely used; not verified here) | AA 73; BrowseComp 74; $30.48/1k tasks |
| Tavily | fan-out to "up to 20 sites"; no own index (I via Sacra) | ranked snippets + content | $8/1k credits PAYG; $7.50 (Project) | custom | 1.88 s mean (Openbenchmarks) | "higher" on paid | n/a | via mcp-omnisearch; own MCP not verified | 66% / $935 and 32% / $176 BrowseComp (Parallel, Sept 2026) |
| Linkup | undisclosed + "personalized indexes" | sourced answers/results | $5–$6/1k | enterprise | <200 ms Flash | n/a | SOC2; ZDR ent. | via mcp-omnisearch | 94% F Verified SimpleQA (self-reported) |
| You.com | undisclosed + "licensed data providers" | up to 100 results | $5.00/1k | same | 21.5 s/task (AA) | custom QPS | n/a | n/a | AA 74; BrowseComp 77; $47.54/1k tasks |
| mcp-omnisearch | Tavily, Brave, Kagi, Exa, Linkup, Firecrawl, GitHub (D) | unified MCP tools | pass-through | pass-through | n/a | n/a | MIT | is an MCP server | n/a |

Sources for table rows: see the Cited Findings in Key questions 1–5; additionally [Artificial Analysis](https://artificialanalysis.ai/agents/search-api), [Parallel](https://parallel.ai/articles/browsecomp-benchmark.md), [Google Custom Search](https://developers.google.com/custom-search/v1/overview), [AI Studio pricing](https://aistudio.google.com/docs/pricing), [Microsoft grounding pricing](https://www.microsoft.com/en-us/bing/apis/grounding-pricing), [OpenAI pricing](https://developers.openai.com/api/docs/pricing), [Claude web search](https://platform.claude.com/docs/en/docs/agents-and-tools/tool-use/web-search-tool), [xAI pricing](https://docs.x.ai/developers/pricing), [Perplexity pricing](https://docs.perplexity.ai/docs/getting-started/pricing.md), [Yandex pricing](https://aistudio.yandex.ru/docs/en/search-api/pricing), [SearXNG settings](https://docs.searxng.org/admin/settings/settings_search.html).

### Inferences

Who sits on top of whom (D = disclosed by the party, I = inferred; arrows point from the layer that calls to the layer it depends on):

```
LAYER 0 — crawlers / indexes
  Google Search ─────┐   Bing ──────────┐   Yandex   Baidu   Naver/Yahoo/Seznam   Brave (own crawl, D)   Perplexity (own stack, D-ish)   Exa (own neural index)   Parallel (own index, D)
                     │                  │
LAYER 1 — official access
  Google Custom Search JSON API (D, closing 2027-01-01)      Bing Web Search API (RETIRED 2025-08-11)
  Gemini / Vertex Grounding (D, synthesized only)            Grounding with Bing Search + Foundry Web Search (D, synthesized only)
  Yandex Search API (D)                                      DuckDuckGo: Instant Answer API only (no full API)
                     │                  │
LAYER 1b — unofficial access (scraping, residential proxies, JS rendering since Jan 2025)
  Serper ─► Google (D)                     DataForSEO ─► Google/Bing/Yahoo/Baidu/Naver/Seznam (D)
  SerpApi ─► Google + many (D)             Oxylabs ─► Google/Bing/Yandex/Baidu (D)
  SearchApi ─► ~80 engines (D)             Bright Data ─► Google/Bing/DDG/Yandex/Baidu/Yahoo/Naver (D)
  Scale SERP / Value SERP ─► Google (D)    Apify actors ─► Google, DDG (D)
  Serply ─► Google/Bing (D)                ZenRows / ScrapingBee / Scrapfly / Zyte ─► Google via generic scraping (D/I)
  SearXNG (self-hosted) ─► up to 261 engines, Google tolerated until reCAPTCHA (D)
                     │
LAYER 2 — agent-facing meta / aggregation layers
  Firecrawl /search ─► "upstream search provider" (D) — Google-derived SERP (I, from tbs=qdr: syntax)
  Tavily ─► fan-out to multiple engines/sites + rerank (D "up to 20 sites"; no own index per Sacra, I)
  Jina s.jina.ai ─► undisclosed engine; top-5 + Reader content (D format, I engine)
  Linkup ─► undisclosed engines + licensed/"personalized" indexes (D partial)
  You.com ─► undisclosed web index + "licensed data providers" (D partial)
  Nimble Search ─► own Search API; engine not stated
  mcp-omnisearch ─► Tavily, Brave, Kagi, Exa, Linkup, Firecrawl, GitHub (D)  [a layer over Layer 2 and Layer 0]
                     │
LAYER 3 — LLM-platform built-in search tools
  OpenAI web_search ─► Bing index + OAI-SearchBot own crawl (I, 2024 statements)
  Anthropic web_search ─► Brave Search (I, Mar 2025 subprocessor list / BraveSearchParams)
  Google Gemini grounding ─► Google (D)              Microsoft Foundry Web Search ─► Bing (D)
  xAI web_search / x_search ─► undisclosed web + X first-party (D for X)
  Perplexity Sonar / Agent API ─► Perplexity own stack (D)
  Mistral web_search(_premium) ─► undisclosed engine + news providers (D that providers exist; names not given)
  Cohere ─► none since connector deprecation 2025-09-15 (D)
```

- Normalized entry-tier ranking for a plain 10-result Google query (cheapest first, Nov 2026): DataForSEO standard $0.60 (5-min latency) < Serper $1.00 ≈ Oxylabs non-JS $1.00 < Oxylabs JS $1.35 < Bright Data $1.50 < DataForSEO live $2.00 ≈ Value SERP $2.00–$2.50 ≈ Serply $2.00 < ScrapingBee ~$2.53 < SearchApi $4.00 < Google CSE $5.00 < Firecrawl Hobby ~$7.60 < SerpApi Production $10.00 (Starter $25.00) < Scale SERP 1k plan $23.00.
- Normalized at-scale floor: Oxylabs non-JS $0.50 (5M+) ≈ Serper $0.30 (12.5M) ≈ DataForSEO $0.60 ≈ Serply $0.75 ≈ SearchApi/Scale SERP/Value SERP $1.00 ≈ Bright Data $1.30 ≈ Firecrawl ~$1.50 ≈ SerpApi $1.96.
- LLM-platform tools cost 5–30x a raw SERP call per invocation ($5 xAI/Perplexity; $10 OpenAI/Anthropic; $14 Gemini 3+/Bing; $30 Mistral reported) but return synthesized, cited answers and absorb the content-fetching step; the fair comparison is against SERP + fetch + model tokens, where AA's "search cost per 1k tasks" ($30–$62 for most agent-grade APIs) is the closest like-for-like figure.
- Concentration risk: with Bing's API retired and Google's CSE closing, every non-Google/Microsoft layer in the diagram ultimately depends on either scraping Google (legally contested, technically adversarial since Jan 2025) or on a small set of independent indexes (Brave, Perplexity, Exa, Parallel, You.com/Linkup partners). Anthropic's and OpenAI's inferred dependencies (Brave, Bing) illustrate that even frontier labs rent rather than own web indexes.

### Gaps
- Latency: almost no independent p50/p95 data for SERP wrappers; vendor claims only (Serper 1–2 s, Bright Data <5 s, Oxylabs 6.04 s, DataForSEO ≤6 s live, SerpApi relative speed-ups).
- MCP availability for most SERP wrappers (only Apify and Serply confirmed on pages fetched; Firecrawl/Tavily MCP servers exist in the ecosystem but were not verified in this pass).
- Dollar price of a Jina search (token pack price missing) and a Scrapfly/Zyte Google query (estimator-only).
- Official statements (as opposed to 2024–2025 reporting) on which index OpenAI and Anthropic use today.
- A dated Microsoft notice for the $35 → $14 Bing grounding price change, and English-language confirmation of the Vertex $35/$45/$14 grounding figures.
