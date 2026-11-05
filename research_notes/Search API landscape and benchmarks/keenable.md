# Keenable (keenable.ai) — web search and page-fetch API for AI agents

Research cut-off: 2026-11-05. All claims dated; "vendor claim" = stated by Keenable or its investors and not independently verified. Note: Keenable's blog pages carry an HTML metadata date of "Nov 3, 2026" on every post regardless of byline date (likely a site-wide republish); byline dates are used below.

Method note: ~45 tool calls (web search + fetch). The shared web-search budget ran out before I could check Reddit, LinkedIn, X threads directly (x.com returned HTTP 402), the Medium "AI Search API Wars" piece (HTTP 403), or Dealroom. Gaps are listed per section.

---

## 1. Company: founding, founders, funding, HQ, headcount

### Takeaway
Keenable.ai Inc. is a 2025-founded, ~15-person search-infrastructure startup that came out of stealth on 2026-08-25 with a $26M seed led by Accel (Zhenya Loginov) with Conviction Partners and angels. Co-founders are Andrey Styskin (ex-Yandex search chief, ex-Amazon AGI director) and Matthias Petri (ex-Amazon AGI principal applied scientist who built Alexa's web-grounding service). HQ is reported as San Francisco by one secondary source; TechCrunch says only "US and Europe".

### Cited Findings
- Launch/funding: Keenable exited stealth 2026-08-25 with a $26M seed round led by Accel (partner Zhenya Loginov), with Conviction Partners and "some business angels". Author Anna Heim. — [TechCrunch, 2026-08-25](https://techcrunch.com/2026/08/25/accel-backed-keenable-is-indexing-the-web-for-ai-agents/)
- Angels came from Amazon, ClickHouse, Databricks, Google, Snowflake and SpaceXAI (per Accel). — [Accel portfolio post by Zhenya Loginov, 2026-08-25](https://www.accel.com/news/our-seed-investment-in-keenable-search-infrastructure-for-better-ai-agents); corroborated by [Pulse2, 2026-08-25](https://pulse2.com/keenable-raises-26-million-seed-as-100-billion-document-search-index-targets-ai-knowledge-access/)
- Legal entity named as "Keenable.ai Inc."; SiliconANGLE says unnamed Google and Amazon executives were angels. Author Mike Wheatley. — [SiliconANGLE, 2026-08-25](https://siliconangle.com/2026/08/25/agentic-web-search-infrastructure-startup-keenable-raises-26m/)
- Headquarters: San Francisco; founded 2025; hiring engineers "across the Bay Area and Europe". (Secondary source, repeating press release.) — [Pulse2, 2026-08-25](https://pulse2.com/keenable-raises-26-million-seed-as-100-billion-document-search-index-targets-ai-knowledge-access/)
- TechCrunch gives no HQ; says team is "spread across the U.S. and Europe"; 15 engineering staff; plans to double headcount by year-end 2026 to build a go-to-market motion. — [TechCrunch, 2026-08-25](https://techcrunch.com/2026/08/25/accel-backed-keenable-is-indexing-the-web-for-ai-agents/)
- SiliconANGLE: 15 employees, plans to double headcount. — [SiliconANGLE, 2026-08-25](https://siliconangle.com/2026/08/25/agentic-web-search-infrastructure-startup-keenable-raises-26m/)
- Andrey Styskin, Co-founder & CEO. Per TechCrunch he "previously led the search, AI, and cloud division" at Yandex and spent ~20 years building search at Yandex and Amazon; at Amazon he worked with Petri on web search infrastructure for AI applications such as Alexa. — [TechCrunch, 2026-08-25](https://techcrunch.com/2026/08/25/accel-backed-keenable-is-indexing-the-web-for-ai-agents/)
- Accel's version: Styskin spent "over 15 years at Yandex", rising from engineer to CEO of Search, leading an organization of "7,000+ employees", and at Yandex "built a 200-billion-document web index"; later a director at Amazon AGI. — [Accel, 2026-08-25](https://www.accel.com/news/our-seed-investment-in-keenable-search-infrastructure-for-better-ai-agents)
- Keenable's own site describes Styskin as ex-"CEO of Search and Ads at Yandex" and "Director of Web Infra at Amazon AGI" (search-result summary of keenable.ai). — [keenable.ai](https://keenable.ai/)
- Aggregator org-chart profile (low quality, unverified): Yandex Feb 2007–Apr 2022, titles including Head of Web Ranking Team, VP of Search, CEO of the Search, Assistant, Ads and Cloud Business Group; Amazon Director of Web Information Services and Structured Knowledge from Feb 2023. — [theorg.com](https://theorg.com/org/amazon/org-chart/andrey-styskin)
- Search Engine Journal identified Styskin as Head of Yandex Search at the time of the Aug 2017 "Korolyov" neural-ranking update. — [SEJ](https://www.searchenginejournal.com/yandex-artificial-intelligence-machine-learning-algorithms/332945/)
- Matthias Petri, Co-founder & Chief Scientist; "Previously Principal Applied Scientist at Amazon AGI, where he built the web grounding service behind Alexa." — [keenable.ai homepage](https://keenable.ai/); TechCrunch calls him a "German AI scientist" — [TechCrunch](https://techcrunch.com/2026/08/25/accel-backed-keenable-is-indexing-the-web-for-ai-agents/)
- Petri (HN handle matt4711) said he "spent seven years at Amazon on web grounding for Alexa/AGI" and that "co-founder Andrey previously led search at Yandex." — [Show HN thread, ~late Aug 2026](https://news.ycombinator.com/item?id=49435555)
- Third named staffer: Ilya Gusev co-authors the NEEDLE, SELECT and Dynamic Snippets posts. — [keenable.ai/blog](https://keenable.ai/blog)
- Customers: API "in production at several AI labs and inference providers", used in both training and runtime; partnership with voice-AI company Gradium. No customer names. — [TechCrunch](https://techcrunch.com/2026/08/25/accel-backed-keenable-is-indexing-the-web-for-ai-agents/); Accel: "commercial contracts with multiple AI labs" — [Accel](https://www.accel.com/news/our-seed-investment-in-keenable-search-infrastructure-for-better-ai-agents)
- Self-reported traction (vendor claim, X post seen only via search snippet): "last month traffic grew 8x, and we enabled 1M search requests a day from Hermes agents." — [Styskin on X](https://x.com/styskin/status/2092265673041084505)
- Third-party X commentary (search snippet only): "Andrey Styskin ran search at Yandex, then worked on web infrastructure at Amazon AGI. Keenable is his third search build. They spent under a year…" — [Alex Prompter on X](https://x.com/alex_prompter/status/2092299531752767663)
- InfoQ/36Kr profile (2026-09-07): ~15 engineers; Styskin "nearly 20 years at Yandex, leading its search, AI, and cloud businesses". — [36Kr/InfoQ](https://eu.36kr.com/en/p/3972565139845640)
- Stated ambition: "the next Google for AI agents." — [TechCrunch](https://techcrunch.com/2026/08/25/accel-backed-keenable-is-indexing-the-web-for-ai-agents/)

### Inferences
- Founding year 2025 (Pulse2) is consistent with Styskin leaving Amazon after Feb 2023 and with the NEEDLE post's statement that the first index was stood up ~Feb 2026 (see §2).
- The Yandex "200-billion-document index" figure is Accel's description of Styskin's past work, not Keenable's index; Keenable's 100B+ claim is half that scale.

### Gaps
- Exact founding month and HQ: only Pulse2 (press-release repeat) says San Francisco/2025; TechCrunch does not confirm. Dealroom not reached (budget).
- Full investor list beyond Accel/Conviction; valuation not disclosed anywhere found.
- One aggregator reportedly cited a "10 billion documents" figure conflicting with 100B (seen only in a search summary; I could not identify or fetch the aggregator). Treat 100B+ as the company's consistent figure.
- A claim that "Web Search API and Web Query Language are free through September [2026]" appeared only in a search summary of aggregator coverage; not confirmed on any fetched page.

---

## 2. Index: size, crawler, ranking, freshness, architecture, latency engineering

### Takeaway
Keenable asserts an independent stack — own crawler, own index of "100B+ documents (by its own count)", own ranking — with sub-250 ms p95 latency from US East. It has published no technical architecture or ranking post; the only disclosed ML component is the "Dynamic Snippets" token classifier. Freshness is exposed through `acquired_at` timestamps and point-in-time queries rather than any published recrawl policy. The first index was stood up roughly Feb 2026.

### Cited Findings
- Index size: "100B+ documents"; latency "<250ms p95 (US East)" (vendor claim, homepage). — [keenable.ai](https://keenable.ai/)
- TechCrunch repeats "more than 100 billion documents" and says the approach "narrows the search space quickly based on each query, using index structures fine-tuned for specific tasks"; Styskin: "the cost of serving and scanning the whole internet is enormous because of the volume" and, on index cost, "Don't ask — it is painfully expensive." Crawling/ranking methods "not described in detail." — [TechCrunch, 2026-08-25](https://techcrunch.com/2026/08/25/accel-backed-keenable-is-indexing-the-web-for-ai-agents/)
- ZeroClick partnership post (2026-10-27, Lindsey Pozzuto) relays Keenable's claim of "its own crawler", "its own index of more than 100 billion documents" ("by its own count"), its own ranking, and that the index "gets better the more agents use it". — [ZeroClick blog](https://zeroclick.ai/blog/keenable-independent-web-search-any-ai-agent-can-buy)
- InfoQ/36Kr: Keenable "rebuilds crawling, indexing, retrieval, and ranking from the ground up, rather than adding an LLM layer on top of Google or Bing APIs." — [36Kr/InfoQ, 2026-09-07](https://eu.36kr.com/en/p/3972565139845640)
- Timeline: NEEDLE post (2026-08-27) says "the first index was set up about six months before the post, with news coverage, query syntax, and snippets added in later months." — [NEEDLE blog post](https://keenable.ai/blog/needle-the-benchmark-your-search-engine-can-t-memorize)
- Architecture framing (vendor): built as a "learning machine", quality gains "coming from the architecture rather than manual engineering"; owned index "allows latency optimization"; engines that federate other indexes "can't meaningfully improve" beyond re-ranking and snippets. — [NEEDLE blog post](https://keenable.ai/blog/needle-the-benchmark-your-search-engine-can-t-memorize)
- Flywheel thesis: Styskin — "This actually creates a new flywheel that is different from what Google learned from human behavior" (grounding AI responses in source documents). — [TechCrunch](https://techcrunch.com/2026/08/25/accel-backed-keenable-is-indexing-the-web-for-ai-agents/)
- Measured latency (Keenable's own live benchmark, 7-day window ending 2026-11-04 23:52 UTC, sequential calls): Keenable p50 154 ms / p95 317 ms / 0.0% errors; Brave 558/807 ms; Exa 1.4 s/3.2 s; Google via Serper 1.5/3.0 s; Tavily 1.6/3.2 s; Parallel 2.4/3.9 s; Bing via SearchApi 2.1/7.5 s. — [NEEDLE live leaderboard](https://keenableai.github.io/needle/)
- Realtime mode: "p95 latency of 200 ms"; Dynamic Snippets "add no latency" (vendor). — [Dynamic Snippets post, 2026-10-15](https://keenable.ai/blog/keenable-snippets-full-page-cost-reduction)
- Artificial Analysis launch snapshot (independent): Keenable realtime had the lowest time per task of all search providers, 16.8 s vs Parallel basic 22.2 s, Exa auto 27.8 s, Brave 28.9 s. — [AlphaSignal summary of AA, 2026-08-18](https://alphasignal.ai/news/artificial-analysis-ranks-11-search-apis-by-how-well-ai-agents-answer)
- Freshness mechanics: results carry `published_at` and `acquired_at` (indexing time); filters `acquired_after/before`, `published_after/before`; `query_time` returns the index "as it stood at this time; pages acquired later are excluded". — [Search API reference](https://docs.keenable.ai/api-reference/search.md)
- Keenable-generated "cards" (e.g., prices, exchange rates, company facts) are blended into results unless `disable_cards=true`. — [Search API reference](https://docs.keenable.ai/api-reference/search.md)
- Fetch serves an "indexed copy" by default; `live=true` fetches from source and is required for unindexed URLs (implies the index stores page content, not just URLs). — [Fetch API reference](https://docs.keenable.ai/api-reference/fetch.md); SKUs `fetch` (indexed copy) vs `fetch.live` — [Pricing](https://keenable.ai/pricing)
- Only disclosed ML component: Dynamic Snippets — documents split into overlapping chunks; a token classifier reads query+chunk and assigns each token a usefulness probability; trained "on real search needs and agent trajectories"; thresholds relative to document max score m: lower = max(0.6·m, 0.5), peak = 0.75·m; runs <80 chars apart merged; fallback of 200 chars around top token (~4% of docs). Model not named. — [Dynamic Snippets post, 2026-10-15](https://keenable.ai/blog/keenable-snippets-full-page-cost-reduction)
- Styskin's framing of agent vs human search: agent loop is "task, search, fetch, read, refine, verify, act, often dozens of times per task"; agent search judged on "recall, freshness, latency, QPS, machine readability, token efficiency, provenance, and total task cost". — [36Kr/InfoQ, 2026-09-07](https://eu.36kr.com/en/p/3972565139845640)
- landing.keenable.ai/blog 301-redirects to keenable.ai/blog; the blog (8 posts, Jul 26–Oct 20, 2026) contains no architecture, crawling or ranking post. — [keenable.ai/blog](https://keenable.ai/blog)

### Inferences
- "Index structures fine-tuned for specific tasks" plus separate `pro`/`realtime` modes and NEEDLE's five task slices suggest multiple specialised indexes/tiers rather than one monolithic posting list — but this is inference from vendor phrasing; no architecture document exists.
- The 100B+ figure cannot be independently verified; NEEDLE's "AgenticRare" slice (Keenable 49% of oracle ceiling) indicates meaningful long-tail gaps remain.

### Gaps
- No published recrawl cadence, crawl rate, or freshness SLA. NEEDLE's hourly News slice (Keenable 62% vs Exa 65%) is the only indirect freshness signal.
- No technical description of ranking (learning-to-rank, neural rankers, link graph, spam filtering). Nothing links Keenable's ranking to Yandex's MatrixNet/CatBoost beyond founder heritage (see §7).
- Crawler user-agent: a search snippet named "KeenableBot" as "Keenable's crawler for public pages", but I could not fetch a primary robots/crawler page confirming it.
- No latency-engineering post exists despite the "sub-250 ms" headline.

---

## 3. Products and access surfaces

### Takeaway
Keenable sells one metered Search API (modes `pro`/`realtime`) and one Fetch API, exposed via REST, a hosted MCP server, a Rust CLI (Homebrew), a SKILL.md, SDKs (Python/TS/Go, LlamaIndex, Haystack, Pipecat) and inference-platform embedding (Baseten). SELECT (formerly "Web Query Language"/WebQL) is a SQL-over-the-web agent that emits cited tables; select.keenable.ai is its host and `/r/` hosts shareable reports. "Time Machine" is point-in-time search (early access). Keyless and x402 crypto-paid access exist; on-prem is enterprise-only.

### Cited Findings
- Homepage lists three products: Search API (MCP at https://api.keenable.ai/mcp; "search tool has 9 params, fetch_page_content has 4"), SELECT ("Queries web pages as a table, with a source for each row"), Time Machine ("Early access by request only"); "Cloud & On-premises" under the Frontier tier; "In production at several AI labs and inference providers". — [keenable.ai](https://keenable.ai/)
- REST endpoints: `POST /v1/search` (keyless `/v1/search/public`, pay-per-request `/v1/x402/search`); `GET /v1/fetch` (`/v1/fetch/public`, `/v1/x402/fetch`). Auth `X-API-Key: keen_<key>` or `Authorization: Bearer`. Keyless calls require `X-Keenable-Title` header (else `400 Missing app identifier`). — [API reference overview](https://docs.keenable.ai/api-reference.md)
- MCP server: `https://api.keenable.ai/mcp` (API key), `/mcp-oauth` (Claude remote connector via OAuth), `/mcp-public` (keyless). Tools: `search_web_pages` (10 parameters per docs: query, site, acquired_after/before, published_after/before, query_time, snippet_max_length, max_results, disable_cards) and `fetch_page_content` (url, max_chars, live, prompt). Local stdio bridge `npx -y @keenable/mcp-server` for Claude Desktop. Config snippets for Claude Code, Codex (`web_search = "disabled"`), Cursor. — [MCP docs](https://docs.keenable.ai/mcp-server.md)
- CLI: single Rust binary; `brew install keenableai/tap/keenable-cli`; shell/PowerShell installers; `cargo install --git https://github.com/keenableai/keenable-cli`; YAML output by default; `keenable login` (device-code), `keenable search`, `keenable fetch`, `keenable configure-mcp --all` (Claude Code, Cursor, Windsurf, Codex, OpenCode). — [SKILL.md at app.keenable.ai](https://app.keenable.ai/SKILL.md); [Quickstart](https://docs.keenable.ai)
- SKILL.md: keenable.ai/SKILL.md 308-redirects to app.keenable.ai/SKILL.md; the file is a CLI-centric agent skill (install, auth, search flags, fetch, MCP setup); notes docs are available as markdown by appending `.md` to any docs URL and an index at docs.keenable.ai/llms.txt. — [SKILL.md](https://app.keenable.ai/SKILL.md)
- SELECT: "agentic search tool with SQL-like syntax that treats a topical slice of the live web as a dataframe", returning "typed, cited rows"; semantic operators (filter, map, join, top-k) traced to Stanford's LOTUS; "materializes only what the agent's query actually needs"; evaluated on WideSearch and WANDR, "performs similarly to Perplexity's Search as Code" (vendor); authors found 12 contaminated WideSearch samples; report gallery at keenableai.github.io/select-showcase. Authors Gusev, Petri, Styskin, 2026-09-03. — [SELECT the tail FROM the web](https://keenable.ai/blog/select-the-tail-from-the-web)
- select.keenable.ai 302-redirects to app.keenable.ai/select/start, which describes SELECT as "an agent that queries the open web in SQL"; each report gets a shareable `/r/` link; available as a Claude connector, via MCP at `https://select.keenable.ai/mcp`, in Codex/Cursor/Claude Code; "free through October" [2026]; sample reports include "A Living History of Search Engines (1982–2026)" and "Popular Open-Source AI Agents & Agentic Frameworks". — [SELECT start page](https://app.keenable.ai/select/start)
- Pre-launch name: TechCrunch/Accel/Pulse2 call it "Web Query Language" ("lets agents pull from thousands of live sources at once"; to launch "within the coming week" of 2026-08-25). — [Accel](https://www.accel.com/news/our-seed-investment-in-keenable-search-infrastructure-for-better-ai-agents); [Pulse2](https://pulse2.com/keenable-raises-26-million-seed-as-100-billion-document-search-index-targets-ai-knowledge-access/)
- Time Machine: SiliconANGLE — "supports point-in-time queries, so models can search the web as it existed at a given moment." — [SiliconANGLE](https://siliconangle.com/2026/08/25/agentic-web-search-infrastructure-startup-keenable-raises-26m/); implemented via `query_time` parameter — [Search API reference](https://docs.keenable.ai/api-reference/search.md); SourceForge listing (low quality) calls it "point-in-time search across historical versions of pages". — [SourceForge](https://sourceforge.net/software/product/Keenable/)
- SDKs/integrations: `keenable-sdk` (Python, TypeScript, Go; MIT), `keenable-mcp`, `keenable-cli`, `needle`, `keenable-grok-plugin`, `keenable-antigravity` (Gemini CLI). GitHub org shows 211 public repos, most of them forks; `needle` has 40 stars (2026-11-05). — [github.com/keenableai](https://github.com/keenableai)
- LlamaIndex: `llama-index-tools-keenable` v0.1.0 released 2026-06-19 (pre-public-launch), v0.1.3 on 2026-08-15; `KeenableToolSpec` exposes `search` (filters site, date ranges, mode) and `fetch`; keyless by default, `KEENABLE_API_KEY` optional; MIT; deps llama-index-core >=0.13,<0.15. — [PyPI JSON](https://pypi.org/pypi/llama-index-tools-keenable/json)
- Haystack: `pip install keenable-haystack`; `KeenableWebSearch` (api_key, top_k, mode pro/realtime, site) and `KeenableFetcher`; "An API key is required for mode='realtime'". — [Haystack integration page](https://haystack.deepset.ai/integrations/keenable)
- Pipecat integration exists. — [Pipecat docs](https://docs.pipecat.ai/api-reference/server/services/knowledge-retrieval/keenable)
- Baseten: Keenable Search available through Baseten Hosted Tools, "our first inference-platform partner"; model can search/fetch inside the same inference request. Author Styskin, 2026-09-16. — [Baseten partnership post](https://keenable.ai/blog/keenable-partners-with-baseten)
- Other integrations: Lightpanda browser (2026-08-28), cognee agent memory (2026-09-22), Gradium voice (2026-07-26). — [keenable.ai/blog](https://keenable.ai/blog)
- Agent storefront: zeroclick.keenable.ai publishes prices and payment setup; agents can buy "autonomously or with human approval". — [keenable.ai](https://keenable.ai/); [Dynamic Snippets post](https://keenable.ai/blog/keenable-snippets-full-page-cost-reduction)
- On-prem: offered only on the dedicated-capacity "AI labs and inference platforms" plan, "in your cloud or your own perimeter"; pay-as-you-go is cloud-only. — [Pricing](https://keenable.ai/pricing)
- Trust/status pages: status.keenable.ai, trust.keenable.ai. — [keenable.ai](https://keenable.ai/)

### Inferences
- The LlamaIndex package's June 2026 release shows the API was quietly live ~2 months before the August public launch.
- "Fetcher API" as a product name does not appear on Keenable's site; the fetch capability is the `/v1/fetch` endpoint and `fetch_page_content` tool.

### Gaps
- The benchmark roundup at select.keenable.ai/r/ai-web-search-api-benchmarks returned HTTP 404 on 2026-11-05; its content could not be reviewed.
- Homepage says 9 search params; MCP docs list 10 (likely `disable_cards` added). Minor inconsistency.
- No Vercel AI SDK or LangChain first-party integration found (only forks of their docs in the GitHub org).

---

## 4. Pricing and rate limits

### Takeaway
Pricing is simple and low relative to peers: 100K free requests/month per org, $4 per 1,000 pay-as-you-go, $1 per 1,000 at 100+ RPS dedicated capacity (cloud or on-prem), and $0.01 per call via x402 USDC with no sign-up. One request = one search (1–50 results) or one fetch; MCP is not billed separately.

### Cited Findings
- Free: 100K requests/month per organization, no card; resets monthly on org creation day. Pay-as-you-go: $4/1K after free allowance, cloud only. Dedicated capacity: $1/1K at 100+ RPS, cloud or on-prem. Keyless x402: $0.01 per search or fetch in USDC on Base. — [Pricing](https://keenable.ai/pricing)
- Four SKUs each 1 credit per call: `search.realtime`, `search.pro`, `fetch` (indexed copy), `fetch.live`. A search is one request whether it returns 1 or 50 results (default 10, `max_results` 1–50). MCP uses same credits/price. — [Pricing](https://keenable.ai/pricing)
- Rate limits: with API key 10 RPS per org, no hourly cap; keyless 1,000 req/hour and 10 RPS per IP per endpoint on a shared pool; x402 50 RPS per wallet; higher limits via sales. Custom price between $4 and $1 for volumes below 100 RPS. — [Pricing](https://keenable.ai/pricing); [Rate limits in API reference](https://docs.keenable.ai/api-reference.md)
- Exhaustion returns HTTP 402 until credits bought or allowance resets; auto top-up defaults: trigger below $5, charge $20, $1,000 monthly cap; purchased credits never expire; free requests consumed first. — [Pricing](https://keenable.ai/pricing)
- Homepage headline: "from $1 / 1K requests @ 100 RPS+"; "Agent Builder Tier" $4/1K; "Frontier Tier" $1/1K; "Get Free 100K requests". — [keenable.ai](https://keenable.ai/)
- ZeroClick storefront: $0.004 per search or fetch (same as $4/1K); failed requests free; prepaid credits from $0.50 (=125 requests); 50 RPS, no hourly cap; payment via x402, MPP or card. — [ZeroClick blog, 2026-10-27](https://zeroclick.ai/blog/keenable-independent-web-search-any-ai-agent-can-buy)
- Competitor prices as compiled by Keenable's NEEDLE page (prices collected 2026-08-21, lowest public tier per 1K queries): Google/Serper $0.30; Keenable $1.00 (dedicated); Bing/SearchApi $1.00; Brave $5; Tavily $5; Parallel $5; Exa $7. — [NEEDLE leaderboard](https://keenableai.github.io/needle/)
- HN commenter phoenix120: Keenable ~$4/1K with up to 50 results at same price; Exa ~$7/1K plus charges beyond top 10; Parallel ~$5/1K. — [Show HN](https://news.ycombinator.com/item?id=49435555)
- SiliconANGLE: "$1 per 1,000 API requests, aimed at 'frontier-scale' users." — [SiliconANGLE](https://siliconangle.com/2026/08/25/agentic-web-search-infrastructure-startup-keenable-raises-26m/)
- SELECT: "free through October" (as of fetch 2026-11-05; no SELECT pricing published). — [SELECT start page](https://app.keenable.ai/select/start)
- No SLA, uptime or latency commitments on the pricing page; "index and ranking are the same across tiers". — [Pricing](https://keenable.ai/pricing)

### Inferences
- The $1/1K dedicated rate used in NEEDLE's cost comparison requires ≥100 RPS sustained; the comparable self-serve rate is $4/1K, which is still below Brave/Tavily/Parallel/Exa list prices but above Serper/SearchApi SERP-scraper bulk tiers.

### Gaps
- Dedicated-capacity minimum commitment, contract length, and on-prem licensing terms not published.
- Whether `fetch.live` or `pro` will be priced differently later is not stated ("currently one credit per call").

---

## 5. API features: filters, fields, operators, output

### Takeaway
The search API is deliberately minimal: a query, two modes, one `site` filter, four date filters (publish/acquire), point-in-time `query_time`, result count 1–50, snippet length 180–10,000 chars, and a card toggle. Responses are title/url/snippet/published_at/acquired_at only — no relevance score, no full text, no language/country filters, and no documented boolean operators. Fetch returns markdown with optional LLM extraction via `prompt`.

### Cited Findings
- Search request params: `query` (required); `mode` default `pro` ("deeper retrieval") or `realtime` ("fastest"); `site`; `published_after/before`; `acquired_after/before`; `query_time` (index as it stood at that time; re-bases relative deltas); `snippet_max_length` 180–10000; `max_results` 1–50 default 10; `disable_cards` (pro/realtime only). Date formats: `YYYY-MM-DD` (whole UTC day), ISO 8601 timestamp, or relative delta with units `min, h, d, mo, y`. — [Search API reference](https://docs.keenable.ai/api-reference/search.md)
- Not documented: `language`, `country`, query operators (beyond `site`/dates), full-content inclusion in search, relevance `score`. — [Search API reference](https://docs.keenable.ai/api-reference/search.md)
- Search response: `query`, `mode`, `results[]` with `title`, `url`, `description` (deprecated, always empty), `snippet`, `published_at` (ISO 8601 UTC), `acquired_at` (ISO 8601 UTC). — [Search API reference](https://docs.keenable.ai/api-reference/search.md)
- CLI mirrors these: `--site`, `--published-after/before`, `--acquired-after/before`, `--query-time`; relative values like `12h`, `7d`, `3mo`, `1y`. — [SKILL.md](https://app.keenable.ai/SKILL.md)
- Fetch request: `url` (required); `max_chars` default 50,000; `live` (default false; required for unindexed URLs); `prompt` ≤2,000 chars ("An LLM reads the page and `content` contains only the output for this instruction"). Response: `url`, `title`, `description` (deprecated), `author`, `content` (markdown), `published_at` (Unix seconds). — [Fetch API reference](https://docs.keenable.ai/api-reference/fetch.md)
- Dynamic Snippets (query-dependent passage selection) are on by default in realtime mode; no explicit toggle documented; snippet length varies with how many passages score near the top (example: 346 tokens narrow question, 913 broad). — [Dynamic Snippets post](https://keenable.ai/blog/keenable-snippets-full-page-cost-reduction)
- Rate-limit headers `X-RateLimit-Limit/Remaining/Reset`; `429` with `Retry-After`. — [API reference overview](https://docs.keenable.ai/api-reference.md)
- NEEDLE post says "query syntax" was added to the index in the months after launch, but no operator syntax is documented in the API reference. — [NEEDLE post](https://keenable.ai/blog/needle-the-benchmark-your-search-engine-can-t-memorize)

### Inferences
- The absence of language/country/safe-search filters and of a score field positions the API as agent-only infrastructure (agents iterate; they do not need localisation knobs), consistent with the "AI agent-only" framing in press.

### Gaps
- Structured-output options for search (e.g., JSON schema) beyond SELECT: none documented.
- Whether `pro` mode uses a different index tier, a re-ranker, or more candidates is not explained.

---

## 6. Benchmarks: Keenable's own numbers and third-party evaluations

### Takeaway
Three sets of numbers exist. (a) Independent, Vals AI Web Search Index (2026-10-21): Keenable Pro + GPT-5.6 Sol ranks #1 of 9 configurations at 49.08%, ahead of Exa configurations, but at higher cost per task than most and only tested against Exa and native search. (b) Independent, Artificial Analysis Search Index launch (2026-08-18): Keenable realtime scored 67 — mid-pack behind Parallel 75 / Exa 74 / Firecrawl 73, ahead of Brave 65 — but was the fastest per task. (c) Vendor-run NEEDLE live benchmark (window to 2026-11-04): Keenable 72% of oracle ceiling, second to Perplexity 74%, ahead of Exa 69 / Parallel 68 / Brave 59 / Bing 48 / Google-Serper 46 / Tavily 43, with by far the lowest latency. No SimpleQA number was found anywhere.

### Cited Findings — Vals AI (independent)
- Vals Web Search Index (updated 2026-10-21): holds model and harness fixed, varies only the search tool; 450 FAB v2 finance questions + 208 expert legal-research tasks; domain tools (SEC EDGAR, CourtListener) removed. Leaderboard: 1. GPT-5.6 Sol + Keenable 49.08% ($8.84/task, 6m35s); 2. Claude Fable 5 + Exa 48.45% ($3.48, 5m52s); 3. Claude Fable 5 + Native 46.94%; 4. GPT-5.6 Sol + Exa 45.24% ($18.97, 8m51s); 5. GPT-5.6 Sol + Native 43.58% ($0.95); 6. Gemini 3.5 Flash + Exa 41.36%; 7. Grok 4.5 + Exa 38.75%; 8. Gemini 3.5 Flash + Native 37.04%; 9. Grok 4.5 + Native 35.54%. Keenable "was run only with GPT-5.6 Sol"; median cost $3.22/task, tail ~$190 (finance) and ~$281 (legal). Vals "open to evaluating other search API providers". — [Vals Web Search Index](https://www.vals.ai/benchmarks/web_search)
- Keenable's write-up (byline 2026-10-20, eval run 2026-10-19): Keenable Pro with GPT-5.6 Sol 49.08% overall; finance 53.9% vs Exa 52.0%; legal 44.2% vs Exa 38.5%; +5.50 pts vs native search, +3.84 vs Exa (same model); cost/task $8.84 vs $18.97 for Exa (-53%); duration 6m35s vs 8m51s (-26%). — [Keenable ranks #1 on the Vals Web Search Index](https://keenable.ai/blog/keenable-vals-web-search-index)

### Cited Findings — Artificial Analysis (independent)
- Methodology: provider-swap; candidate and grader model GPT-5.6 Luna (medium reasoning); tools `web_search` (provider native response, up to 10 results) and `web_fetch` (15 s timeout); 25-turn budget; Stirrup agent loop; three benchmarks equally weighted — DeepSearchQA (900 tasks, F1), BrowseComp 200-sample subset (accuracy), AA-Omniscience (600 private samples, accuracy); contamination filtering. Keenable listed twice: "Keenable pro" (`mode=pro`) and "Keenable realtime" (`mode=realtime`). SimpleQA is not part of it. — [AA Search API methodology](https://artificialanalysis.ai/methodology/search-api)
- Launch (2026-08-18) scores: Parallel advanced 75 ($83.51/1k tasks, 37.5 s/task); Exa auto 74 ($127.15, 27.8 s); Firecrawl 73 ($75.42, 56.9 s); Parallel basic 73 ($114.83, 22.2 s); Keenable realtime 67 ($90.54, 16.8 s); Brave 65 ($146.13, 28.9 s); model-only baseline 33. Keenable pro not listed in that snapshot. — [AlphaSignal, 2026-08-18](https://alphasignal.ai/news/artificial-analysis-ranks-11-search-apis-by-how-well-ai-agents-answer); AA announcement listing initial providers Parallel, Exa, Firecrawl, You.com, Tavily, Keenable, Brave — [Artificial Analysis on X](https://x.com/ArtificialAnlys/status/2089755262915936661); The Decoder confirms 75/74/73 and range 65–75 — [The Decoder, 2026-08-18](https://the-decoder.com/new-benchmark-ranks-search-apis-for-ai-agents-on-quality-cost-and-speed/)
- Later AA snapshots (search-summary only, Sept 2026): Perplexity 80, Octen 77, Parallel 75, Brave 75, You.com 74, Exa 74, Firecrawl 73; no updated Keenable figure located. — [Parallel vs Exa compare page, vendor](https://parallel.ai/compare/exa-vs-parallel); [keirolabs roundup](https://keirolabs.cloud/blog/web-search-apis-for-agents-2026)
- HN commenter phoenix120 cited "the Artificial Analysis search API ranking" as evidence Keenable is "roughly equal or sometimes better quality" at lower price/latency. — [Show HN](https://news.ycombinator.com/item?id=49435555)

### Cited Findings — Keenable's own replication of the AA setup (vendor)
- Dynamic Snippets post: BrowseComp accuracy 56.6% → 67.3% after Dynamic Snippets while search-result tokens per question fell 1.16M → 466k; claims "fewer tokens per question than Exa and Parallel on all three benchmarks" and "highest accuracy on BrowseComp and AA-Omniscience"; setup = AA Search API harness, Stirrup, GPT-5.6 Luna, 25 turns, two tools. Authors caution "benchmark results do not always carry over to real questions." Production: mean response size 135 KiB → 69 KiB (-49%) after 2026-08-30 rollout; 28–60% fewer search-result tokens across three public benchmarks. — [Dynamic Snippets post, 2026-10-15](https://keenable.ai/blog/keenable-snippets-full-page-cost-reduction)

### Cited Findings — NEEDLE (vendor-run, open source)
- NEEDLE = News, Everyday, Expert, Deep-tail, Legal Evaluation; live, continuously re-run (News hourly, others daily); built to avoid overfitting/leakage of static sets like BrowseComp; queries partly from real agent search logs; slices: News (RSS + Google Trends), Finance (Wikidata/GLEIF/SEC XBRL answers), Scholar (degraded titles, tip-of-tongue; inspired by Exa's publication evals), AgenticRare (rare-word queries from DeepResearchGym, LRAT, OpenResearcher logs), Legal (court opinions, CFR sections). Providers: Google via Serper, Bing via SearchAPI, Brave, Tavily, Parallel, Exa, Keenable (+ Perplexity on live page). Authors Gusev, Petri, Styskin, 2026-08-27. Repo github.com/keenableai/needle; raw runs on Hugging Face keenable-ai/needle-results. — [NEEDLE post](https://keenable.ai/blog/needle-the-benchmark-your-search-engine-can-t-memorize)
- Live leaderboard, 7-day means to 2026-11-04 23:52 UTC, "share of _ultimate_" (oracle pooling all engines): Perplexity 74; Keenable 72 (CI 70.0–73.1); Exa 69 (66.8–70.1); Parallel 68; Brave 59; Bing/SearchApi 48; Google/Serper 46; Tavily 43. Per slice (Keenable / Exa / Parallel): Scholar 77/58/64; News 62/65/57; Finance 88/92/92; AgenticRare 49/46/41; Legal 83/82/84. Raw: Keenable Scholar recall@10 0.712 (Exa 0.540), News nDCG@5 0.617 (Exa 0.648), Finance answer-recall@5 0.875 (Exa 0.910), AgenticRare nDCG@5 0.494 (Exa 0.460), Legal recall@5 0.805 (Exa 0.799). — [NEEDLE live leaderboard](https://keenableai.github.io/needle/)
- NEEDLE judge: `openai/gpt-6-luna` via OpenRouter, high reasoning, temp 0, pointwise, blind to engine; snippets capped 2,000 chars; pages not fetched or re-ranked; sequential calls; "The authors have not yet run a systematic human-agreement audit of the judge." — [NEEDLE live leaderboard](https://keenableai.github.io/needle/)
- NEEDLE "suspicious sharing" test: engines returning the same judged-irrelevant URL or ≥3 identical URLs may share an upstream index. Petri on HN "suggested Parallel and Brave may use the same underlying index." — [NEEDLE leaderboard](https://keenableai.github.io/needle/); [Show HN](https://news.ycombinator.com/item?id=49435555)
- Homepage benchmark framing is "Overall quality 7-day mean share of ultimate" vs "Cost, $ per 1K queries Lowest public price" — i.e., NEEDLE data. — [keenable.ai](https://keenable.ai/)

### Inferences
- Across the two independent evals, Keenable's standing depends heavily on mode and date: realtime scored mid-pack on AA in Aug 2026 (before Dynamic Snippets shipped 2026-08-30), while pro topped Vals in Oct 2026. The vendor's own AA-harness replication claims a large BrowseComp jump after Dynamic Snippets, which would be consistent with an improved current AA position, but no post-August independent AA score for Keenable was found.
- The Vals #1 is narrow: one model, only Exa and native as comparators, and a 0.63-point lead over Exa+Claude Fable 5 at ~2.5x the cost per task. Cost comparisons are confounded by model choice.
- On Keenable's own NEEDLE, Perplexity leads; Keenable's clearest edges are Scholar (+19 vs Exa) and latency (~9x faster p50 than Exa); it trails Exa/Parallel on Finance and Exa on News.

### Gaps
- No SimpleQA (or SimpleQA Verified) score for Keenable found in any source.
- select.keenable.ai/r/ai-web-search-api-benchmarks returned 404; its roundup could not be reviewed.
- Current AA leaderboard page (artificialanalysis.ai/search-api) returned 404; Keenable pro's AA score and any post-Aug update are unknown.
- Parallel's "Best Web Search API 2026" report does not include Keenable (per search summary). — [Parallel report](https://parallel.ai/articles/best-web-search-api-for-ai-applications)
- No Keenable results from You.com's open eval framework found.

---

## 7. Why Keenable performs strongly — vendor explanation, heritage, third-party views, criticism

### Takeaway
Keenable's own explanation is structural: an owned, independent index ("federated engines can't improve beyond re-ranking"), index structures tuned per task that make searches cheap and fast, query-dependent Dynamic Snippets that halve tokens and raise agent accuracy, point-in-time/acquire-date metadata, and a "learning machine" that improves from agent traffic. Investors emphasise the founders' Yandex (200B-doc index, 7,000-person org) and Amazon Alexa web-grounding pedigree. Independent commentary is thin and mostly neutral-to-skeptical ("legitimate but embryonic"; thesis "not yet independently benchmarked"); the HN launch drew 12 points and 5 comments.

### Cited Findings — what Keenable says
- Independent index is "the main factor"; engines that federate other indexes "can't meaningfully improve" beyond re-ranking/snippets; some engines "appear to share upstream indexes"; Keenable is a "learning machine" whose gains come "from the architecture rather than manual engineering"; owned index enables latency optimisation. — [NEEDLE post, 2026-08-27](https://keenable.ai/blog/needle-the-benchmark-your-search-engine-can-t-memorize)
- Cost/latency via query-specific narrowing: "index structures fine-tuned for specific tasks"; Styskin on generic enterprise search at web scale: prohibitively expensive. — [TechCrunch](https://techcrunch.com/2026/08/25/accel-backed-keenable-is-indexing-the-web-for-ai-agents/); Pulse2: "an order of magnitude more cost-efficient than traditional search." — [Pulse2](https://pulse2.com/keenable-raises-26-million-seed-as-100-billion-document-search-index-targets-ai-knowledge-access/)
- Agent flywheel: grounding "creates a new flywheel that is different from what Google learned from human behavior"; Google "beatable" for agentic queries due to innovator's dilemma. — [TechCrunch](https://techcrunch.com/2026/08/25/accel-backed-keenable-is-indexing-the-web-for-ai-agents/)
- Token efficiency as a quality lever: Dynamic Snippets cut tokens ~50% and raised BrowseComp 56.6% → 67.3% in their AA-harness replication. — [Dynamic Snippets post](https://keenable.ai/blog/keenable-snippets-full-page-cost-reduction)
- Petri on HN: "competitive on quality with Exa, the market leader, but cheaper and faster"; lower cost lets models "call search more often". — [Show HN](https://news.ycombinator.com/item?id=49435555)
- Market framing: Google and Microsoft "are retiring their existing search APIs" and favouring bundled deals, creating room for independents. — [TechCrunch](https://techcrunch.com/2026/08/25/accel-backed-keenable-is-indexing-the-web-for-ai-agents/); RuntimeWire: independent index can compete "on speed, price, and neutrality". — [RuntimeWire](https://runtimewire.com/article/andrey-styskin-keenable-26m-seed-ai-agent-search)
- Styskin X launch post (snippet): "an AI-native index of the best human knowledge we have, starting with the open web. AI seems to know just about everything until you ask it about something you know deeply. The answer isn't wrong, but it's just very average." — [Styskin on X, 2026-08-25](https://x.com/styskin/status/2092265673041084505)
- "The bottleneck is not only intelligence, it is also access" (Keenable team on SELECT). — [ZeroClick blog](https://zeroclick.ai/blog/keenable-independent-web-search-any-ai-agent-can-buy)

### Cited Findings — Yandex/Amazon heritage
- Accel: Styskin built "a 200-billion-document web index" at Yandex and led a 7,000+ org as CEO of Search. — [Accel](https://www.accel.com/news/our-seed-investment-in-keenable-search-infrastructure-for-better-ai-agents)
- Petri built "the web grounding service behind Alexa" at Amazon AGI. — [keenable.ai](https://keenable.ai/)
- Yandex ML-ranking lineage (context, not Keenable-specific): MatrixNet developed 2009, credited to Andrey Gulin; CatBoost open-sourced July 2017 as "the successor of the MatrixNet algorithm… widely used within the company for ranking tasks"; Styskin was Head of Yandex Search at the Aug 2017 Korolyov neural update. No source documents Styskin personally leading MatrixNet/CatBoost. — [Wikipedia CatBoost](https://en.wikipedia.org/wiki/CatBoost); [Yandex CatBoost page](https://tech.yandex.com/CatBoost/); [SEJ](https://www.searchenginejournal.com/yandex-artificial-intelligence-machine-learning-algorithms/332945/)
- Accel's investment thesis: "search engines built for humans fall short"; "A new search infrastructure built from the ground up for AI agent needs must emerge." — [Accel](https://www.accel.com/news/our-seed-investment-in-keenable-search-infrastructure-for-better-ai-agents)

### Cited Findings — third-party views and criticism
- Show HN (~late Aug 2026): 12 points, 5 comments. ic1018 could not tell how Keenable differs from Perplexity from the quality-vs-cost chart; madmecodes asked about behaviour under rapid repeated calls — no reply shown. No Yandex/privacy concerns raised. — [Show HN](https://news.ycombinator.com/item?id=49435555)
- Medium opinion piece (fetch blocked, 403; search summary): calls Keenable "a legitimate but embryonic entrant"; argues SimpleQA is "near-saturated and contamination-prone". — [AI Search API Wars, Medium](https://chierhu.medium.com/ai-search-api-wars-who-will-own-the-web-for-ai-agents-bf90b0663d6f)
- One outlet calls the narrowing-the-search-space thesis "not yet independently benchmarked proof" (search summary). — [OpenTools](https://opentools.ai/news/keenable-search-index-ai-agents)
- InfoQ/36Kr: Exa is the "most direct competitor" (Exa ~100B docs, ~1.4T URLs tracked, $250M Series C at $2.2B, $7/1K); "the two products aren't directly comparable on price" given Keenable's narrower lab/inference-platform positioning. — [36Kr/InfoQ, 2026-09-07](https://eu.36kr.com/en/p/3972565139845640)
- SiliconANGLE relays Keenable's claim that its results "already outperform" Tavily, Exa and Perplexity on "relevant, clean, agent-ready information" (vendor claim). — [SiliconANGLE](https://siliconangle.com/2026/08/25/agentic-web-search-infrastructure-startup-keenable-raises-26m/)
- Vals caveats: Keenable tested with one model only; cost/task $8.84 vs $3.48 for Exa+Claude Fable 5; cost tail to ~$281. — [Vals](https://www.vals.ai/benchmarks/web_search)
- NEEDLE caveats (self-declared): no human-agreement audit of LLM judge; Keenable designs the slices; Perplexity still leads overall. — [NEEDLE leaderboard](https://keenableai.github.io/needle/)
- Keenable listed in third-party directories (low quality): The Rundown, nexusai-tech, SourceForge, awesome-agent-native-services issue #281 (notes OpenAPI spec and MCP endpoint). — [The Rundown](https://www.therundown.ai/tools/keenable); [GitHub issue #281](https://github.com/haoruilee/awesome-agent-native-services/issues/281)

### Inferences
- The strongest evidence-backed differentiators are (1) latency (independently the fastest per task on AA at launch; ~150 ms p50 in NEEDLE) and (2) price per request; quality leadership is supported by Vals (narrowly) and by Keenable's own NEEDLE/AA replications but not by the one independent AA snapshot available (Aug 2026, pre-Dynamic-Snippets).
- The founders' heritage plausibly explains the ability to stand up a 100B-scale crawl/index in ~6 months with ~15 engineers, but no source connects specific Yandex techniques (MatrixNet/CatBoost-style GBDT ranking, Korolyov-style neural matching) to Keenable's ranker.

### Gaps
- No critical user reviews found on Reddit, LinkedIn or X (budget exhausted before Reddit search; X fetches blocked).
- No independent audit of the 100B+ claim or of crawl politeness/robots compliance.
- No Styskin podcast or conference talk located; the TechCrunch and InfoQ interviews are the only long-form founder statements.

---

## 8. Comparison to Common Crawl

### Takeaway
No source — vendor or third-party — mentions Common Crawl in connection with Keenable. Keenable states it runs its own crawler and index; its product exposes per-page acquisition timestamps and hourly-refreshed news, which is a fundamentally different freshness model from Common Crawl's monthly-ish batch snapshots. Whether Keenable seeded from Common Crawl is unknown.

### Cited Findings
- Keenable claims "its own crawler", "its own index of more than 100 billion documents", "its own ranking". — [ZeroClick blog relaying Keenable, 2026-10-27](https://zeroclick.ai/blog/keenable-independent-web-search-any-ai-agent-can-buy)
- Keenable's first index was set up ~Feb 2026, with news coverage added in later months. — [NEEDLE post](https://keenable.ai/blog/needle-the-benchmark-your-search-engine-can-t-memorize)
- Keenable exposes `acquired_at` per result and `acquired_after/before`/`query_time` filters. — [Search API reference](https://docs.keenable.ai/api-reference/search.md)
- Common Crawl publishes a new crawl roughly every 1–2 months and typically misses sites under ~30 days old (SEO-vendor source, low quality). — [CrawlGraph](https://crawlgraph.com/blog/common-crawl-release-schedule); Common Crawl's URL Index is a columnar Parquet index over WARC files. — [Common Crawl URL Index](https://commoncrawl.org/url-index)
- For scale context, Brave's independent index is described as "more than 30 billion pages". — [TNW](https://thenextweb.com/news/nyt-newspapers-sue-brave-ai-scraping)

### Inferences
- If the 100B+ count is accurate, Keenable's index would be larger than any single Common Crawl snapshot (historically ~2–3B pages per monthly crawl) and comparable to Exa's self-reported ~100B; the claim is unverified.

### Gaps
- Whether Keenable seeded URL discovery or content from Common Crawl, Yandex-era assets, or a from-scratch crawl is undisclosed.
- No crawl-rate, politeness, robots.txt policy, or recrawl-frequency documentation found; no primary page for "KeenableBot".
