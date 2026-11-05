# Search APIs for AI agents: market positioning, business strategy, UVPs and practitioner sentiment (as of 2026-11-05)

Scope note: findings are dated inline. Labels used throughout: **[VENDOR]** = company's own statement; **[PRESS]** = journalist/analyst reporting; **[PRACTITIONER]** = developer opinion (HN/Reddit/blogs); **[AGGREGATOR]** = secondary funding-database or news-aggregator summary that I could not confirm against a primary source. Web-search budget for this session ran out before I could pull Reddit r/LocalLLaMA / r/ClaudeAI / r/cursor / r/mcp threads directly or verify a few items; those are listed under Gaps.

---

## Key Question 1: Funding and traction (rounds, valuations, investors, query volumes, customers, ARR)

### Takeaway
Between Sept 2025 and Oct 2026 the category went from "seed-stage API startups" to three multi-billion-dollar valuations (Exa $2.2B, Parallel $2B, You.com $1.5B), one $275M exit (Tavily to Nebius), one strategic absorption (Jina into Elastic), and a wave of new well-funded entrants with their own indexes (Keenable $26M, Octen $10M, Linkup $10M). Exa is the only provider to publicly claim a revenue figure ($100M annualized, Oct 2026); everyone else discloses developer counts or request volumes instead.

### Cited Findings

**Exa (formerly Metaphor; YC S21)**
- Series A $17M led by Lightspeed with Nvidia and Y Combinator, July 16, 2024 **[PRESS]** — [TechCrunch](https://techcrunch.com/2024/07/16/exa-raises-17m-lightspeed-nvidia-ycombinator-google-ai-models)
- Series B $85M at a $700M valuation, led by Benchmark with Lightspeed, YC and Nvidia's NVentures, announced Sept 3, 2025; company described as a "35 person startup" in the HN submission **[PRESS]** — [Built In](https://builtin.com/articles/exa-raises-85m-series-b-20250908); [HN item 45118788](https://news.ycombinator.com/item?id=45118788)
- Series C $250M at a $2.2B valuation led by a16z, with Benchmark, Lightspeed and YC participating, May 20, 2026; Exa stated "5000+ companies and 400,000+ developers" at that time **[VENDOR]** — [Exa blog, Series C](https://exa.ai/blog/announcing-series-c); Latham & Watkins advised **[PRESS]** — [Latham](https://www.lw.com/en/news/2026/05/latham-advises-exa-in-series-c)
- "Exa just passed $100M in annualized revenue." "We've grown almost exactly 10x per year for 3 years." "200k+ teams." "2 billion requests a month." (Will Bryk, Oct 13, 2026) **[VENDOR]** — [Exa blog, $100M run rate](https://exa.ai/blog/100m-run-rate)
- Sacra's independent estimate: ~$1.9M annualized at end-2024, ~$10M in Sept 2025, $14M at end-2025, ~$100M in Sept 2026; customers named: Cursor, Cognition, HubSpot, OpenRouter, Monday.com **[PRESS/analyst]** — [Sacra Exa research](https://sacra.com/research/exa); earlier Sacra note "Exa at $10M growing 11x YoY" — [Sacra](https://sacra.com/research/exa-at-10m-growing-11x-yoy)
- Homepage (fetched Nov 5, 2026) claims "900,000+ developers" and "Up to 25T tokens passed to models each week" — note this is more than double the 400,000 developers claimed in May 2026 **[VENDOR]** — [exa.ai](https://exa.ai)
- Infrastructure claims in Series C post: "crawlers that track over 500 billion URLs", "sub-200ms latency", goal of "hundreds of thousands of searches per second" **[VENDOR]** — [Exa Series C](https://exa.ai/blog/announcing-series-c)
- a16z (Nov 2025) states Exa runs "144 H200 GPUs" **[PRESS/VC]** — [a16z Search Wars Episode 2](https://a16z.com/search-wars-episode-2/); Bryk on Latent Space (Jan 10, 2025): "we just purchased a $5 million H 200 cluster" **[VENDOR]** — [Latent Space](https://www.latent.space/p/exa)
- Strategic distribution: "Grounding with Exa" on Google's Gemini Enterprise Agent Platform (Private Preview, April 2026) and Exa Agent in the Gemini Enterprise Agent Marketplace **[VENDOR]** — [Exa blog, Google Cloud](https://exa.ai/blog/exa-google-cloud); "Exa is now powering search in Firefox" (Aug 17, 2026) **[VENDOR]** — [Exa blog index](https://exa.ai/blog)

**Tavily (Israel; began as open-source GPT Researcher, 2023)**
- Seed ~$5M (July 2024, per Sacra); Series A $20M led by Insight Partners and Alpha Wave Global, Aug 6, 2025, total $25M; customers cited: Groq, Cohere, MongoDB, Writer; "over a million monthly downloads" **[PRESS]** — [TechCrunch](https://techcrunch.com/2025/08/06/tavily-raises-25m-to-connect-ai-agents-to-the-web); [SiliconANGLE](https://siliconangle.com/2025/08/06/tavily-raises-25m-expand-real-time-web-access-infrastructure-ai-agents/); [Tavily blog](https://blog.tavily.com/big-news-from-tavily-announcing-25m-series-a-to-power-the-internet-of-agents)
- Acquired by Nebius Group: agreement announced Feb 10, 2026; Nebius did not disclose price; "more than 3 million monthly SDK downloads", "developer community of more than one million users", customers IBM, Cohere, Groq; ~30 employees join Nebius; brand retained; Rotem Weiss: "Tavily is on a mission to onboard the next billion AI agents to the web." **[VENDOR]** — [Nebius newsroom](https://nebius.com/newsroom/nebius-announces-agreement-to-acquire-tavily-to-add-agentic-search-to-its-ai-cloud-platform); Nebius 6-K **[PRIMARY]** — [SEC](https://www.sec.gov/Archives/edgar/data/1513845/000110465926012492/tm265786d1_ex99-1.htm)
- Price reported as $275M (Bloomberg, Feb 10, 2026, via Sacra); Sacra describes this as "roughly a 98x revenue multiple", implying ~$2.8M revenue (my arithmetic, not Sacra's statement) **[PRESS]** — [Sacra Tavily](https://sacra.com/research/tavily); [SiliconANGLE](https://siliconangle.com/2026/02/10/ai-infrastructure-giant-nebius-buys-agentic-search-startup-tavily/); [Calcalist](https://www.calcalistech.com/ctechnews/article/r168bhodbe)
- Homepage (Nov 2026): "Trusted by 3M+ developers", "300M+" monthly requests, "99.99% uptime", "180 ms" p50 latency on /search; logos include Writer, MongoDB, JetBrains, Groq, LangChain, AWS, Mastercard, IBM, BMO **[VENDOR]** — [tavily.com](https://www.tavily.com)

**Parallel Web Systems (Parag Agrawal, Palo Alto)**
- Earlier $30M round in Jan 2024 (per Economic Times, cited by one outlet) **[AGGREGATOR]** — [Technology Magazine](https://technologymagazine.com/news/inside-ex-twitter-ceos-us-100m-funding-for-ai-startup)
- Series A $100M at ~$740M valuation co-led by Kleiner Perkins and Index Ventures with Khosla, announced on stage at Cerebral Valley AI Summit, Nov 12, 2025; Agrawal told Reuters funds would be used in part for "deals with online content owners" **[PRESS]** — [Newcomer](https://www.newcomer.co/p/exclusive-parag-agrawals-parallel); [SiliconANGLE](https://siliconangle.com/?p=720910); [Business Today](https://www.businesstoday.in/technology/news/story/parag-agrawals-parallel-raises-100-million-from-kleiner-perkins-and-index-ventures-heres-why-its-significant-502250-2025-11-14)
- Series B $100M at $2B valuation led by Sequoia, April 29, 2026, "five months after its last big raise" (per WSJ via TechCrunch); one report claims "over 100,000 developers" and Notion and major banks as clients **[PRESS]** — [TechCrunch](https://techcrunch.com/2026/04/29/parallel-web-systems-hits-2b-valuation-five-months-after-its-last-big-raise/); [SiliconANGLE](https://siliconangle.com/?p=743333); [Pulse2](https://pulse2.com/parallel-web-systems-100-million-series-b-at-2-billion-valuation-raised-to-scale-ai-agent-web-infrastructure/amp/)
- Homepage logos (Nov 2026): Granola, Lovable, Harvey, Notion, Pfizer, LangChain, Modal, Replit, Profound, Rogo; distribution via Google Cloud, OpenRouter, Vercel, Snowflake **[VENDOR]** — [parallel.ai](https://parallel.ai)
- Google lists "Parallel web search" as a grounding source option alongside Google Search in Vertex/Gemini grounding docs (per search summary of Google's grounding overview; I could not fetch the page directly) **[PRESS/unverified]** — see Gaps.

**Keenable (US/Europe)**
- $26M seed led by Accel (partner Zhenya Loginov), with Conviction Partners and angels; exited stealth Aug 25, 2026; founders Andrey Styskin ("previously led Russian search giant Yandex's search, AI and cloud division") and Matthias Petri (German AI scientist; "seven years at Amazon as a scientist working on web grounding for Alexa/AGI" per his HN post); index "more than 100 billion documents"; API "in production at several AI labs and inference providers, used for both training and runtime" but customers unnamed; partnered with voice-AI company Gradium; 15 engineers, plans to double headcount by year-end **[PRESS]** — [TechCrunch](https://techcrunch.com/2026/08/25/accel-backed-keenable-is-indexing-the-web-for-ai-agents/); [SiliconANGLE](https://siliconangle.com/2026/08/25/agentic-web-search-infrastructure-startup-keenable-raises-26m/); [Keenable blog](https://keenable.ai/blog/keenable-raised-26m-to-beat-google-in-the-agentic-search-market); [Show HN](https://news.ycombinator.com/item?id=49435555)
- Styskin on index cost: "Don't ask — it is painfully expensive"; ambition: "the next Google for AI agents" **[VENDOR via PRESS]** — [TechCrunch](https://techcrunch.com/2026/08/25/accel-backed-keenable-is-indexing-the-web-for-ai-agents/)

**Linkup (France)**
- €3M seed reported Nov 28, 2024 **[PRESS]** — [TechCrunch via BestofAI mirror](https://bestofai.com/article/linkup-connects-llms-with-premium-content-sources-legally-techcrunch)
- $10M seed led by Gradient, reported Feb 2026 (aggregators; primary press-release page returned 503 when fetched) **[AGGREGATOR]** — [Parsers.vc](https://parsers.vc/news/260210-linkup-secures-10m-seed-for-ai-s-real-time/); [Mammoth Times/Accesswire](https://business.mammothtimes.com/mammothtimes/article/accwirecq-2026-2-3-linkup-raises-10m-seed-round-led-by-gradient-to-build-web-search-for-ai)
- Homepage logos (Nov 2026): EY, Die Bundesregierung, McKinsey & Company, Databricks, KPMG, Legora; "Trusted by Fortune 500s, frontier AI labs, and government agencies" **[VENDOR]** — [linkup.so](https://www.linkup.so)
- Selected by Cloudflare as one of three launch providers for its Web Search API (Oct 2, 2026) **[VENDOR/Cloudflare]** — [Cloudflare changelog](https://developers.cloudflare.com/changelog/post/2026-10-02-introducing-web-search-api/)

**Valyu (London)**
- Only aggregator data found: ~$500K pre-seed, last round March 2024, investor listed as a16z crypto **[AGGREGATOR]** — [VCBacked](https://www.vcbacked.co/company/valyu); [Caplight](https://www.caplight.com/company/valyu). Customers named on company page: UK Nuclear Decommissioning Authority (horizon scanning), o11 (financial AI agents) **[VENDOR]** — [valyu.ai/company](https://www.valyu.ai/company). a16z's Nov 2025 essay names Valyu as a provider that "crawls periodically with RL-guided re-crawling" **[PRESS/VC]** — [a16z](https://a16z.com/search-wars-episode-2/)

**Firecrawl (YC; "Sideguide Technologies")**
- Series A $14.5M led by Nexus Venture Partners with YC and Tobias Lütke, Aug 19, 2025; total $16.2M **[PRESS/VENDOR]** — [Firecrawl press release PDF](https://www.firecrawl.dev/press/firecrawl-series-a-press-release.pdf); [SiliconANGLE](https://siliconangle.com/?p=707860)
- Series B $75M led by Smash Capital with Altos, Nexus, YC, Freestyle, Offline Ventures, Sept 22, 2026; "Over 1.5 million users build with Firecrawl now"; launched "Alexandria" ("knowledge library for superintelligence") with Research, Developer and Government indexes and payments to contributors **[VENDOR]** — [Firecrawl blog](https://www.firecrawl.dev/blog/introducing-alexandria-series-b)
- A Form D filed Sept 14, 2026 shows $82.1M in preferred stock sold to seven investors — ~$7.1M more than the announced $75M; discrepancy unexplained **[PRESS]** — [RuntimeWire](https://runtimewire.com/article/scoop-firecrawl-raises-82m-after-its-14-5m-series-a-warm-up)
- Self-reported elsewhere: "1.25 million developers, 150,000 companies, 5 billion requests served" **[VENDOR via PRESS]** — [RuntimeWire](https://runtimewire.com/article/scoop-firecrawl-raises-82m-after-its-14-5m-series-a-warm-up)

**Jina AI (Berlin)**
- Acquired by Elastic; deal completed Oct 9, 2025; Han Xiao became VP of AI at Elastic; models to continue on Hugging Face and via Elastic Inference Service **[PRIMARY]** — [Elastic IR](https://ir.elastic.co/News--Events/news/news-details/2025/Elastic-Completes-Acquisition-of-Jina-AI-a-Leader-in-Frontier-Models-for-Multimodal-and-Multilingual-Search/default.aspx); [Business Wire](https://www.businesswire.com/news/home/20251009619654/en). Jina's site footer now reads "Elastic © 2026" **[VENDOR]** — [jina.ai](https://jina.ai)

**You.com**
- Series C $100M at $1.5B led by Cox Enterprises with Georgian, Salesforce Ventures, Norwest (Sept 2025; page metadata Jan 9, 2026); "over 1 billion queries per month" via API; API customers DuckDuckGo, Windsurf, Harvey; "100,000+ agents built on you.com in the last 12 months"; describes a "transition to becoming an AI infrastructure company" **[VENDOR]** — [You.com Series C](https://you.com/articles/series-c); SiliconANGLE reported $150M, conflicting with the $100M figure **[PRESS]** — [SiliconANGLE](https://siliconangle.com/?p=709848)
- Acquired Graft (team and technology), Oct 2025 **[AGGREGATOR]** — [Simplify](https://simplify.jobs/c/YOU-Dot-Com)
- Named as an early "Pay Per Use" partner by Cloudflare (July 2026) **[PRESS]** — [TNW](https://thenextweb.com/news/cloudflare-block-ai-crawlers-pay-publishers)

**Perplexity (Search API as a business line)**
- Search API launched Sept 25, 2025; index "hundreds of billions of webpages"; "Each second, our systems process tens of thousands of index update requests" **[VENDOR]** — [Perplexity blog](https://www.perplexity.ai/hub/blog/introducing-the-perplexity-search-api)
- Pricing: $5.00 per 1,000 requests; Fast Search $1.00 per 1,000; "no additional token-based charges" **[VENDOR]** — [Perplexity pricing docs](https://docs.perplexity.ai/getting-started/pricing)
- No query-volume, customer-count or revenue disclosure for the API line found. See Gaps.

**Brave Search API**
- Company-wide: passed $100M annualized revenue in Q1 2025 (secondhand summary of The Information) **[PRESS/secondhand]** — [Sacra](https://sacra.com/c/brave/)
- "Brave Search handles over 2 billion monthly queries across the API and end-user search"; "nearly 700,000 OpenClaw users have now signed up to use the Brave Search API" (Apr 1, 2026) **[VENDOR]** — [Brave blog](https://brave.com/blog/openclaw/)
- Index "30 billion pages, with more than 100 million updates daily"; "Over 200,000 developers signed up after the OpenClaw release"; API "already powers the vast majority of the world's largest AI LLM companies" (Brave claims, reported June 8, 2026) **[VENDOR via PRESS]** — [Implicator.ai](https://www.implicator.ai/brave-drops-free-search-api-tier-puts-all-developers-on-metered-billing/)
- API landing page: "150 billion" total queries answered; "hundreds of millions of queries daily"; logos AWS, Cohere, Mistral AI, Snowflake, You.com, Firecrawl, Kagi, Shopify, Together.ai **[VENDOR]** — [brave.com/search/api](https://brave.com/search/api/)
- Anthropic lists Brave Search as a subprocessor (as of March 19, 2025) and Claude's web_search tool schema was titled "BraveSearchParams" **[PRACTITIONER/PRIMARY]** — [Simon Willison](https://simonwillison.net/2025/Mar/21/anthropic-used-brave/); [TechCrunch](https://techcrunch.com/2025/03/21/anthropic-appears-to-be-using-brave-to-power-web-searches-for-its-claude-chatbot/)
- No API-specific revenue breakdown found. See Gaps.

**Kagi**
- 75,938 members, 10,192 families, 396 teams, 1,086,600 queries in past day (stats page, Nov 5, 2026) **[VENDOR]** — [kagi.com/stats](https://kagi.com/stats)
- Search API: "$12 /1k requests" **[VENDOR]** — [Kagi API pricing](https://kagi.com/api/pricing); Enrichment API uses "Kagi's own Teclis (web) and TinyGem (news) indexes" **[VENDOR]** — [Kagi API overview](https://help.kagi.com/kagi/api/overview.html)

**Mojeek (UK)**
- Own crawler (MojeekBot), "global index of billions of fresh webpages", "Zero Sub-Processors", infrastructure in Europe; pricing £2/1K (Startup), £3/1K (Business), Enterprise custom with Zero Data Retention **[VENDOR]** — [Mojeek Web Search API](https://www.mojeek.com/services/search/web-search-api/)

**Other entrants surfaced**
- Octen (Singapore/SF): $10M seed led by Square Peg, Apr 22, 2026; "62 milliseconds" median on SealQA Hard; invite-only beta **[PRESS]** — [SiliconANGLE](https://siliconangle.com/?p=741155)
- DeepSeek: Search and Fetch APIs at "$0.75 per 1,000 successful requests", "powered by DeepSeek's in-house search engine" (live by Oct 18, 2026) **[VENDOR]** — [DeepSeek docs](https://api-docs.deepseek.com/guides/search/)
- Cloudflare Web Search API (beta, Oct 2, 2026): resells Ceramic.ai, Exa and Linkup "at each provider's list API price, with no additional markup" **[VENDOR]** — [Cloudflare changelog](https://developers.cloudflare.com/changelog/post/2026-10-02-introducing-web-search-api/)

### Inferences
- Valuations have decoupled from disclosed revenue: Exa's $2.2B (May 2026) was ~150x Sacra's end-2025 ARR estimate; Tavily sold at ~98x revenue (Sacra). The market is pricing "search layer for agents" as infrastructure, not as a SaaS multiple.
- Developer counts are the preferred vanity metric (Exa 900k+, Tavily 3M+, Firecrawl 1.5M, Brave 700k OpenClaw users), while only Exa (revenue) and You.com/Exa/Tavily/Brave (request volumes) disclose usage. Request-volume claims (Exa 2B/mo; You.com 1B+/mo; Tavily 300M+/mo; Brave 2B/mo incl. consumer) are not independently audited.
- Strategic buyers so far are infrastructure/cloud players (Nebius, Elastic) rather than the frontier labs — consistent with search being treated as a stack component bundled with inference.

### Gaps
- No disclosed revenue, query volume or customer count for Perplexity's Search API line, Brave's API line specifically, Linkup, Valyu, Keenable, Mojeek or Kagi's API.
- Valyu funding status after March 2024 is unknown; no 2025–2026 round found.
- Linkup's $10M Gradient seed: primary press release unreachable (HTTP 503); amount/lead from aggregators only.
- Parallel's total raised (~$230M) is a derived figure from aggregators; the $30M Jan 2024 round is from a single secondhand citation.

---

## Key Question 2: Stated unique value propositions (verbatim, with URLs)

### Takeaway
Nearly every vendor now uses the same three words—"for AI agents"—so differentiation in copy has shifted to (a) claiming an own index (Exa, Brave, Keenable, Parallel, Perplexity, Mojeek), (b) claiming benchmark leadership (Exa, Parallel, Linkup, Keenable, Tavily), or (c) claiming a data moat beyond the open web (Valyu, Linkup, Firecrawl's Alexandria). Only Brave and Linkup still lead with privacy/compliance; only Kagi and Mojeek lead with anti-ad/independence ethics.

### Cited Findings

- **Exa** — Title: "Exa — The world's data for AI agents." Tagline: "Search the largest index of public web and private information." "Web-scale index: comprehensive coverage over all search verticals." "Exa 3.0 leads on BrowseComp, DSQA, and WideSearch, the standard benchmarks for search agents." "Zero data retention — your queries and results are never stored or trained on." (Nov 2026) **[VENDOR]** — [exa.ai](https://exa.ai). Earlier framing: "We're neural all the way we're building an end to end neural search engine"; "The link prediction objective can be seen as like a neural PageRank"; "we are a search infrastructure company" (Bryk, Jan 2025) **[VENDOR]** — [Latent Space](https://www.latent.space/p/exa). Series C: aim to build "perfect search over all the world's information" (May 2026) — [Exa blog](https://exa.ai/blog/announcing-series-c)
- **Tavily** — "Connect your AI agents to the web." "One secure API for real-time web access." "The web access layer for AI agents." "Built by researchers. Trusted by 3M+ developers." Endpoints: Search ("Fast and relevant web results"), Extract ("Clean and structured content for LLMs"), Research, Crawl, Map. "Requests pass through security, privacy, and content validation layers that block PII leakage, prompt injection, and malicious sources." (Nov 2026) **[VENDOR]** — [tavily.com](https://www.tavily.com). Note: the phrases "search engine for AI agents" and "optimized for LLMs" no longer appear on the homepage. Blog (Apr 27, 2026): "Tavily is built as the production web access layer for agents that need fresh, grounded retrieval" — [Tavily blog](https://tavily.com/blog/exa-vs-parallel-benchmarking-retrieval-apis-for-ai-agents-in-2026)
- **Parallel** — "Where agents find answers." "Web infrastructure for AI to search, extract, monitor, and reason over the world's information." "Parallel builds web search and research APIs purpose-built for AI agents and agentic workflows." Index "built from the ground up for AIs", "billions of pages, and millions are added or updated daily", described as "proprietary" and "web-scale". "Web search starts as low as $1 per 1,000 requests." Customer quote (Gumloop CEO): "the highest accuracy API on the market." (Nov 2026) **[VENDOR]** — [parallel.ai](https://parallel.ai). The literal phrase "web research infrastructure" does not appear on the homepage.
- **Keenable** — "Keenable.ai — Independent Web Search API for AI." "Keenable is independent web search infrastructure for AI"; "our own crawler, index and ranking"; "100B+ documents"; "<250ms p95 (US East)"; "from $1 / 1K requests @ 100 RPS+"; "Keenable ranks #1 on the Vals Web Search Index." (Nov 2026) **[VENDOR]** — [keenable.ai](https://keenable.ai). Show HN (Aug 25, 2026): "We built https://keenable.ai, a different web search API for AI agents." "Keenable searches our own 100B+ page index." "we are competitive in quality to exa (the market leader) but much cheaper and lower latency." **[VENDOR]** — [HN 49435555](https://news.ycombinator.com/item?id=49435555). Note: the homepage does not mention Yandex; the ex-Yandex framing comes from TechCrunch and the founders' HN post.
- **Linkup** — "Web Search API for AI." "Industry-leading accuracy, in your stack via one API call or deployed inside your own cloud." "Get sourced, cited answers with full-text snippets from across the web." Links to "Verified SimpleQA" methodology. (Nov 2026) **[VENDOR]** — [linkup.so](https://www.linkup.so). The homepage no longer mentions "premium licensed content" or publisher partners; that positioning is from TechCrunch's Nov 2024 coverage ("signs content licensing deals with publishers" and "integrates with their CMS to fetch content without scraping", paying partners "based on how often Linkup clients access their content") **[PRESS]** — [TechCrunch via BestofAI](https://bestofai.com/article/linkup-connects-llms-with-premium-content-sources-legally-techcrunch)
- **Valyu** — "Search and Deep Research for AI knowledge work." "One API to search specialist, proprietary and web sources, run multi-step research with cited, structured outputs — across Finance and Science & R&D." "LLMs are guessing more than reasoning. That's a context problem." (Nov 2026) **[VENDOR]** — [valyu.ai](https://www.valyu.ai); [valyu.ai/company](https://www.valyu.ai/company)
- **Firecrawl** — "Firecrawl is the open-source web data API for AI agents and LLM applications." "Firecrawl is how AI agents get context from the web." "LLM-optimized Markdown output by default." Alexandria: "knowledge library for superintelligence." (Nov 2026) **[VENDOR]** — [firecrawl.dev](https://www.firecrawl.dev); [Alexandria post](https://www.firecrawl.dev/blog/introducing-alexandria-series-b)
- **Jina AI** — "Your Search Foundation, Supercharged." Reader: "Convert any URL to Markdown for better grounding LLMs." Search: "Use s.jina.ai to search the web and get SERP." Embeddings: "Multimodal multilingual embeddings." Reranker: "Reranker for maximizing search relevance." (Nov 2026) **[VENDOR]** — [jina.ai](https://jina.ai)
- **Brave** — "Quality in. Quality out." "The best answers require the best data." "Every result comes from Brave's own independent index, crawled and ranked by Brave." "Brave is the only fully-fledged search index available through an open API." "Index size is a vanity stat." "99.9% of the web that matters." "Architectural ZDR: Built in, not a contract bolt-on. Your queries never leave Brave." "Search results are for people. Brave's LLM Context endpoint is for machines." (Nov 2026) **[VENDOR]** — [brave.com/search/api](https://brave.com/search/api/). Blog: "the go-to Web search for the agentic future" (Apr 2026) — [Brave blog](https://brave.com/blog/openclaw/)
- **Perplexity** — "Access real-time web search results with Perplexity's Search API." "Search returns ranked results with page text in snippet, and no generated answer." **[VENDOR]** — [Perplexity docs](https://docs.perplexity.ai/docs/search/quickstart). Launch post: index "hundreds of billions of webpages"; "Each second, our systems process tens of thousands of index update requests"; API "sits at the Pareto frontier of relevance and speed"; "Perplexity leads the competition across output quality and latency" (Sept 25, 2025) **[VENDOR]** — [Perplexity blog](https://www.perplexity.ai/hub/blog/introducing-the-perplexity-search-api). The word "hybrid" does not appear in the launch post.
- **Kagi** — "The Search API gives programmable access to Kagi's premium search results." **[VENDOR]** — [Kagi help](https://help.kagi.com/kagi/api/search.html); "$12 /1k requests" — [Kagi API pricing](https://kagi.com/api/pricing)
- **You.com** — "Build with search and inference APIs for AI." "One Platform for Search and Inference." "Access web search, web fetch, and deep research tools using our product MCP server." (Nov 2026) **[VENDOR]** — [you.com/docs/welcome](https://you.com/docs/welcome). The word "customizable" does not appear on the docs landing page.
- **Mojeek** — "Connect AI agents to the real-time web." "Independent Index." "Unique European data sovereignty." "Zero Sub-Processors." **[VENDOR]** — [Mojeek](https://www.mojeek.com/services/search/web-search-api/)
- **Cloudflare (new intermediary)** — Web Search API lets agents "ground their responses in live information" with a choice of Ceramic.ai, Exa or Linkup, billed "with no additional markup" (Oct 2, 2026) **[VENDOR]** — [Cloudflare](https://developers.cloudflare.com/changelog/post/2026-10-02-introducing-web-search-api/)

**Published list prices (per 1,000 requests unless noted; fetched Nov 2026)**
- Exa: lite/instant $4; auto/fast $7; deep $12; deep-reasoning $15; answer $5; contents $1/1k pages; $10/month free credit — [Exa pricing](https://exa.ai/pricing)
- Tavily: $0.008/credit (= $8/1k credits); 1,000 free credits/month; basic search 1 credit, advanced 2 (per Sacra) — [Tavily pricing](https://www.tavily.com/pricing); [Sacra](https://sacra.com/research/tavily)
- Parallel: "as low as $1 per 1,000"; $5 recurring monthly free allowance — [parallel.ai](https://parallel.ai)
- Keenable: $4 (Agent Builder tier); $1 at 100+ RPS (Frontier tier) — [keenable.ai](https://keenable.ai)
- Linkup: $5 standard search ($6 with sourcedAnswer); $50 deep search; fetch $1–$11; $20 free credit for professional emails — [Linkup pricing](https://docs.linkup.so/pages/documentation/platform/pricing.md)
- Brave: $5 search; $4 answers + $5/M tokens; free tier removed Feb 2026, replaced by $5 monthly credit requiring attribution and a credit card — [Brave API](https://brave.com/search/api/); [Implicator](https://www.implicator.ai/brave-drops-free-search-api-tier-puts-all-developers-on-metered-billing/)
- Perplexity: $5 standard; $1 Fast Search — [Perplexity pricing](https://docs.perplexity.ai/getting-started/pricing)
- Kagi: $12 — [Kagi](https://kagi.com/api/pricing)
- Mojeek: £2–£3 — [Mojeek](https://www.mojeek.com/services/search/web-search-api/)
- DeepSeek: $0.75 (successful requests only) — [DeepSeek](https://api-docs.deepseek.com/guides/search/)
- Google Custom Search JSON API (legacy): $5; closed to new customers; ends Jan 1, 2027 — [Google](https://developers.google.com/custom-search/v1/overview)
- Firecrawl: credit plans from $19/mo (5,000 credits) to $749/mo (1M credits) — [firecrawl.dev](https://www.firecrawl.dev)

### Inferences
- $5/1K has become the anchor price (Brave, Perplexity, Linkup, legacy Google, Exa's answer endpoint); an HN commenter called it "market rate for a product like this" ([HN 46736917](https://news.ycombinator.com/item?id=46736917)). The sub-$1 tier (Parallel Fast $1, Keenable $1 at volume, Perplexity Fast $1, DeepSeek $0.75, Ceramic $0.25) emerged only in 2026.
- Tavily's copy deliberately avoids claiming an index ("web access layer") — consistent with Sacra's characterization of it as an aggregator; Parallel and Keenable both explicitly say "own index", which reads as a direct response to that distinction.
- Linkup appears to have de-emphasized the "licensed premium content" story in favor of "accuracy + deploy in your own cloud" (enterprise/EU compliance), suggesting the licensing moat was hard to sell to developers.

### Gaps
- Could not retrieve Linkup's current SimpleQA score or the list of licensed publisher partners (homepage gives no numbers or names).
- Could not confirm a "hybrid index" claim for Perplexity from its own materials.
- You.com's full API marketing page (logos, "customizable" positioning) did not render; only the docs landing page was captured.

---

## Key Question 3: Practitioner sentiment (HN, Reddit, developer blogs)

### Takeaway
Developers broadly accept that Exa is the quality reference point ("the market leader" even in competitors' words) but complain loudly about price, opaque billing and ZDR terms; they treat Brave as the cheap/pragmatic default with its own index but resent the free-tier removal and ToS confusion; they are skeptical of every vendor-run benchmark; and the Oct 2026 DeepSeek ($0.75) and Cloudflare launches triggered an explicit "race to the bottom" debate. Reddit coverage in this research is thin (one r/AI_Agents thread) because the search budget ran out.

### Cited Findings

**Exa — Launch HN (May 6, 2025; 412 points, 133 comments)**
- Pitch: "For every search, we perform dozens of embedding searches over Exa's vector database of the web"; pricing reply: "We charge $5 per 1000 requests with our search and answer endpoints" (Liam Hinzman); Bryk: Websets is "a very expensive product to run" **[VENDOR]**
- Praise: xp84 — "an amazing tool for people trying to find 'the best X for me'". Complaints: AznHisoka — "it's been 15 minutes and it barely verified the first row"; mdaniel — "turns out, AI does not solve all problems" (~30/70 accuracy on a GitHub query); esafak — "I would not want to pay $49/month"; jackienotchan and xena raised robots.txt compliance. A question about index size vs Google went unanswered **[PRACTITIONER]** — [HN 43906841](https://news.ycombinator.com/item?id=43906841)
- Later HN submission (1 point, Jan 11, 2026): "Exa.ai is indexing personal site data ignoring robots.txt" linking a tweet by rbbydotdev; no discussion **[PRACTITIONER, single unverified report]** — [HN 46574182](https://news.ycombinator.com/item?id=46574182)
- Reddit r/AI_Agents (post ~Dec 2025; snapshot May 29, 2026): "Exa Web Search pricings are killing our margins, what am I doing wrong?" — agency CTO spending ~$1,200/week across 22 clients. u/mattate: alternatives like Brave and spider.dev are "only about 30% cheaper", cut own costs ~95% via engineering; Exa cofounder (u/yibaiveintiocho): "Cofounder of Exa here! Would love to get you a discount, or brainstorm how to save some costs."; Parallel's official account pitched in the thread **[PRACTITIONER]** — [Reddit snapshot](https://reddit.sentinel-team.org/posts/1tn44cu/snapshots/2026-05-29T19%3A16%3A10.134322Z)
- Cloudflare thread (Oct 2026): 0fflineuser — "I am pretty sure exa specifically say it trains on your data in it's privacy policy"; lukewarm707 — "exa has zdr, but they charge for the 'feature' of not storing your data"; Exa's alexey-salmin (self-identified Head of Index) — "We certainly do have our own index and it's one of the biggest among the independent players" and "Thanks for raising this! We're looking into this discrepancy (I work at Exa)" re the ZDR claim; timpera on Brave — "really great and imo a better experience than Exa" **[PRACTITIONER]** — [HN 49963171](https://news.ycombinator.com/item?id=49963171)
- Parallel thread: nextworddev raised cancellation difficulty "citing Exa" **[PRACTITIONER]** — [HN 45837425](https://news.ycombinator.com/item?id=45837425)

**Parallel — HN "The Parallel Search API" (Nov 6, 2025; 123 points, 52 comments)**
- Praise: amnigos impressed by "the quality and latency of Parallel search APIs"; kanodiaayush found pricing "compelling". Complaints: davidsainez — "try a query -> balance is insufficient … patterns like this leave me with a really bad impression"; aabhay — "If it is indeed 5s per request that seems like a deal breaker"; nahnahno — "The fact that GPT-4.1 was the judge does not convince of the validity of the bench"; dragonwriter on ToS content clause — "It may merely be poorly written, but I wouldn't rely on that"; BinaryIgor doubted LLM search differs from human search. Parag Agrawal replied that Parallel spends more compute per search so agents make fewer searches, and that building an index is "not insurmountable" **[PRACTITIONER / VENDOR]** — [HN 45837425](https://news.ycombinator.com/item?id=45837425)

**Keenable — Show HN (Aug 25, 2026; 12 points) and Needle benchmark thread (Aug 27, 2026; 33 points)**
- ic1018: "But still don't understand the differentiation with Perplexity."; styskin (user): "How is it different from Exa or Parallel?" Founder matt4711: "some players in the market, such as Parallel and Brave, may be using the same underlying search index." phoenix120: "Exa charges 7$ per 1000 queries, and charges additionally for each result that is out of top-10." **[PRACTITIONER / VENDOR]** — [HN 49435555](https://news.ycombinator.com/item?id=49435555)
- Needle thread: mpalmer — "The blog post appears to get confused and devotes its entire second half to pitching Keenable itself."; daft_pink — "so is this an independent search engine benchmark or a blog post from a search engine provider"; hexer303 — "It seems that the agentic search benchmarks have fallen victim to reward hacking, just like the coding benchmarks." **[PRACTITIONER]** — [HN 49466250](https://news.ycombinator.com/item?id=49466250)
- Quality reports (Oct 2026): shingoshoji — "I've been using keenable a lot and I've had no noticable issues with it" (migrated from Brave); scosman — "It's okay but not great … Generally the same pattern: it's not usable" (Grokipedia outranking Wikipedia; definitive link at position 5/6) **[PRACTITIONER]** — [HN 49963171](https://news.ycombinator.com/item?id=49963171)

**Brave**
- "Ask HN: Brave Search API forbids use with AI agents" (Jan 30, 2026) quoting Brave's terms: "These Terms of Use prohibit using responses for AI inference."; commenters pointed to a separate AI-inference plan **[PRACTITIONER]** — [HN 46822822](https://news.ycombinator.com/item?id=46822822)
- Free-tier removal (Feb 2026): implicator.ai documents support-forum threads closing without Brave replies, a card being required for the "free" credit despite earlier FAQ saying it "will not be charged", and a 35-comment GitHub issue on the official MCP servers repo about ToS compliance **[PRESS]** — [Implicator](https://www.implicator.ai/brave-drops-free-search-api-tier-puts-all-developers-on-metered-billing/); dizhn: "they require a credit card even for that"; execution: "I also confirm the $5 you get is only promotional credit" (Kagi) vs Brave's "$5 free every month" **[PRACTITIONER]** — [HN 48556902](https://news.ycombinator.com/item?id=48556902); [HN 49404000](https://news.ycombinator.com/item?id=49404000)
- pclark: "Brave is the only one I've found that'll let you store their results" (storage/resyndication rights) **[PRACTITIONER]** — [HN 49963171](https://news.ycombinator.com/item?id=49963171)
- artooro on SearXNG: "It works well if you connect it the Brave Search API, but using it a scraper is fairly unreliable." **[PRACTITIONER]** — [HN 48780356](https://news.ycombinator.com/item?id=48780356)

**DeepSeek $0.75 launch — HN (Oct 18, 2026; 607 points, 282 comments)**
- Price comparisons: frenchtoast8 — "Kagi charges $12 per 1000 searches"; hobofan — "$1 for LinkUp fetch, $5 for LinkUp search."; wmchen — "Ceramic.ai is $0.25/1000 searches."; ece — "$4 with Exa, $1.50 with SERP API" (disputed by porker: "the cheapest is over $9 per 1000 searches"); thombles — "that's $5 with Brave Search API and $12 with Kagi API"; risphere — Brave "is expensive" at $5 vs $0.75.
- Quality: breadislove — "ceramic is very very bad, the worst search provider of all."; Havoc ranked LLM-judged preference "Exa and tavily #1, brave #2, searx last".
- Data/China: apwheele — "the fact DeepSeek API is not zero data retention I cannot get over."; jstrasner — "the search call becomes a new data path to China even if the model runs in the EU."
- Race to the bottom: londons_explore — "I suspect we might see the price of search API's going negative in the future."; mjmvisser — "These services only exist because Google refuses to provide a paid search API."; Havoc — "Think the era of respecting stuff like robots.txt is over." **[PRACTITIONER]** — [HN 50138531](https://news.ycombinator.com/item?id=50138531); [HN 50138776](https://news.ycombinator.com/item?id=50138776); [HN 50139295](https://news.ycombinator.com/item?id=50139295)

**Cloudflare Web Search API — HN (Oct 5, 2026)**
- simonw on whether results can be stored/resyndicated: "Am I alone in caring about this?"; binarymax: "Why not use those providers directly? Does Cloudflare need to be in the middle of everything?"; qingcharles on Google/Bing APIs: "Basically, yes. Everyone is just scraping them with residential proxies."; EcommerceFlow: provider pricing "is 3x-8x higher than something like Luna 5.6 w/ Web Search"; sejje on Serper: "is $1 per 1,000 … it seemed good"; jeromechoo: "Codex uses SerpAPI" (unverified); hartator: SerpApi "has also now its own index" (unverified); luplex happy with Linkup as EU provider with "GDPR-compliance and zero data retention"; jerrygoyal recommends Jina Search as cheaper; timpera: Perplexity's absence "is to be expected … knowing how much these two companies despise each other" **[PRACTITIONER]** — [HN 49963171](https://news.ycombinator.com/item?id=49963171)

**Perplexity Search API**
- Five separate HN submissions of the launch post (Sept 25–28, 2025) collected 0 comments each (max 16 points) **[PRACTITIONER]** — [HN Algolia](https://hn.algolia.com/api/v1/search?query=%22perplexity%20search%20api%22&hitsPerPage=30); n1xis10t: "I don't think perplexity's search api even let's you paginate" — [HN 45932127](https://news.ycombinator.com/item?id=45932127)

**Independent/third-party comparison blogs (mostly 2026)**
- AIMultiple (Dec 2025, as summarized by a comparison blog): Brave 14.89, Exa 14.39, Tavily 13.67, with top four (Brave, Firecrawl, Exa, Parallel) "statistically indistinguishable" **[PRACTITIONER/analyst, secondhand]** — [rhumb.dev](https://rhumb.dev/blog/exa-vs-tavily-vs-serper-vs-brave-search)
- "Tavily vs Exa vs Brave: The Page Text Costs More Than the Search" — argues content-fetch costs dominate agent search bills **[PRACTITIONER]** — [beri.net](https://www.beri.net/article/tavily-vs-exa-vs-brave-vs-perplexity-search-api-agent-cost-2026)
- Keenable-generated comparison (Sept 1, 2026): "Parallel leads measured agent-search quality; Exa is the closest general-purpose alternative" **[VENDOR-generated]** — [select.keenable.ai](https://select.keenable.ai/r/ai-agent-search-engines-compared/tOGxcKyQnRF-4P_6uts9gw)
- Routing/meta-layer tools appearing on HN: Telem ("Route agent web search across providers and inspect the traces", Aug 2026), Sifthound ("self-hosted, Tavily-compatible search API", Sept 2026), Scry ("programmable internet search w/ congestion pricing", 61 points, Sept 2026) **[PRACTITIONER]** — [HN Algolia](https://hn.algolia.com/api/v1/search?query=tavily&tags=story&hitsPerPage=30)

### Inferences
- The recurring practitioner complaints are commercial, not technical: billing surprises (Exa per-result add-ons, Brave card requirement, Parallel "balance insufficient"), data-retention terms (Exa ZDR as paid feature; DeepSeek no ZDR), and storage/resyndication rights (only Brave permits storing results). Quality complaints cluster on the cheapest tier (Ceramic) and newest index (Keenable).
- The HN audience increasingly treats Google-grounding or model-native search (Gemini free tier, "Luna 5.6 w/ Web Search") as the price benchmark, which pressures standalone APIs.

### Gaps
- No direct r/LocalLLaMA, r/ClaudeAI, r/cursor or r/mcp threads were retrieved (search budget exhausted). Only one Reddit thread (r/AI_Agents) is cited.
- No named X/Twitter posts by well-known AI engineers were captured beyond the rbbydotdev robots.txt tweet (not fetchable).
- No reliability/outage incident reports (status pages, postmortems) were found for any provider.

---

## Key Question 4: Industry analysis (search API wars, Bing/Google exits, licensed content, labs building search, economics, consolidation)

### Takeaway
Two incumbent exits (Bing API, Aug 11, 2025; Google Custom Search JSON API, closed to new customers with a Jan 1, 2027 end date) created the demand vacuum; a16z framed the result as a multi-winner "Search Wars: Episode 2" (Nov 2025) in which APIs "compete primarily on speed, pricing, and ease of integration." Content economics are being re-plumbed by Cloudflare (default-block July 2025 → Pay Per Use Sept 2026), and consolidation has begun from the infrastructure side (Nebius–Tavily, Elastic–Jina, Cloudflare as reseller, Google grounding partnerships with Parallel and Exa).

### Cited Findings

**Incumbent exits**
- Microsoft announced on May 12, 2025 that Bing Search and Bing Custom Search APIs would retire Aug 11, 2025 ("decommissioned completely"), pointing developers to "Grounding with Bing Search" inside Azure AI Agents; DuckDuckGo and other long-term partners kept access **[PRIMARY/PRESS]** — [Microsoft Lifecycle](https://learn.microsoft.com/en-us/lifecycle/announcements/bing-search-api-retirement); [The Register](https://www.theregister.com/2025/05/15/bing_search_apis_retired/); PPC Land: the Azure alternative "costs 40-483% more" — [PPC Land](https://ppc.land/microsoft-ends-bing-search-apis-on-august-11-alternative-costs-40-483-more/)
- Google: "The Custom Search JSON API is closed to new customers." "Existing Custom Search JSON API customers have until January 1, 2027 to transition to an alternative solution." Suggested alternatives: Vertex AI Search (up to 50 domains) or "contact Google about its full web search solution" **[PRIMARY]** — [Google docs](https://developers.google.com/custom-search/v1/overview); announcement post dated Jan 20, 2026 **[PRIMARY, body not retrieved]** — [Google blog](https://programmablesearchengine.googleblog.com/2026/01/updates-to-our-web-search-products.html)
- Google's grounding stance: a Parallel article (Sept 2026) says "for a team building an agent today, there's no signup button" for Google web search; a Parallel article dated Oct 2026 claims Google published a "Web Search Service API" with REST/gRPC JSON results — I could not verify this against Google documentation **[VENDOR-authored, unverified]** — [Parallel](https://parallel.ai/articles/why-ai-agents-cant-just-use-google-search); [Parallel](https://parallel.ai/articles/web-grounding-gemini-enterprise-agent-platform)
- Google does route third-party search into Gemini: "Grounding with Exa" in Private Preview on Gemini Enterprise Agent Platform (April 2026) **[VENDOR]** — [Exa blog](https://exa.ai/blog/exa-google-cloud); Accel's Loginov (Aug 2026) on why Keenable: "Google and Microsoft are shutting down their existing search APIs to avoid cannibalizing their own products" **[PRESS]** — [TechCrunch](https://techcrunch.com/2026/08/25/accel-backed-keenable-is-indexing-the-web-for-ai-agents/)

**VC/analyst framing**
- a16z "Search Wars: Episode 2" (Nov 13, 2025; Cui, Li, Wang, Zhang): "Search can (and should) be built from the ground up to be AI-native"; "the majority of organizations are expecting to rely on third-party search providers"; API providers "compete primarily on speed, pricing, and ease of integration"; "Our emerging view is that deep research will become the dominant and most monetizable form of agentic search"; re-indexing the web at Google quality is "a non-trivial feat" needing "petabytes of data"; based on 30+ search-API customer interviews; names Exa (144 H200s), Parallel (millions of pages/day), Tavily and Valyu (RL-guided re-crawl), Seda **[PRESS/VC]** — [a16z](https://a16z.com/search-wars-episode-2/)
- Bright Data (vendor): search APIs hit latency targets "through caching and pre-indexing" which "creates freshness gaps" **[VENDOR-authored]** — [Bright Data](https://brightdata.com/blog/ai/search-apis-vs-knowledge-supply-chains)
- Vespa blog: Perplexity and Parallel are "leveraging Vespa" **[VENDOR-authored]** — [Vespa via PlushCap](https://www.plushcap.com/content/vespa/blog/vespa-the-search-api-reset-incumbents-retreat-innovators-step-up)
- System1 analysis (summary only; page returned 403): "AI agents using a single search index see about half of what multiple search APIs collectively surface" **[PRESS, unverified]** — [Longbridge](https://longbridge.com/news/293623051)

**Labs building vs buying**
- Anthropic: Brave Search listed as subprocessor "As of March 19, 2025"; Claude's tool schema titled "BraveSearchParams" **[PRACTITIONER/PRIMARY]** — [Simon Willison](https://simonwillison.net/2025/Mar/21/anthropic-used-brave/)
- OpenAI: Sacra reports OpenAI "developing its own search index and web crawler" (OAI-SearchBot) **[PRESS/analyst, thin]** — [Sacra chat](https://sacra.com/chat/h/81567c5f-0c70-4d25-8b85-a3de9c81a3b1/); HN practitioner claim "Codex uses SerpAPI" (jeromechoo) is unverified — [HN 49963171](https://news.ycombinator.com/item?id=49963171)
- DeepSeek shipped its own "in-house search engine" API at $0.75/1K (Oct 2026) **[VENDOR]** — [DeepSeek docs](https://api-docs.deepseek.com/guides/search/)
- Perplexity opened its index as an API (Sept 2025) and, per Sacra, "competes with its own customers through its consumer interface" **[PRESS]** — [Sacra Tavily](https://sacra.com/research/tavily)

**Licensed content and publisher economics**
- Perplexity Comet Plus (Aug 26, 2025): $5/month subscription; "Publishers will receive 80% of all revenue"; initial $42.5M pool; launch partners Condé Nast, The Washington Post, Le Monde; older ad-share program partners Time, Der Spiegel, Texas Tribune, Gannett, Lee Enterprises **[PRESS]** — [Axios](https://www.axios.com/2025/08/26/perplexity-comet-plus-subscription); [Press Gazette](https://pressgazette.co.uk/news/perplexity-launches-ai-subscription-revenue-share-scheme-for-publishers/); Digiday: publishers say Perplexity "has been unresponsive" and "It remains unclear how much revenue is actually getting paid out" **[PRESS]** — [Digiday](https://digiday.com/media/media-briefing-here-are-the-hurdles-to-perplexitys-pitch-as-the-publisher-friendly-llm)
- ProRata: Fortune "signed up with Prorata's planned revenue sharing" (mentioned only as an alternative scheme) **[PRESS]** — [Digiday](https://digiday.com/media/how-perplexity-new-revenue-model-works-according-to-its-head-of-publisher-partnerships/)
- Linkup's 2024 model: CMS-integrated licensing paying publishers per access **[PRESS]** — [TechCrunch via BestofAI](https://bestofai.com/article/linkup-connects-llms-with-premium-content-sources-legally-techcrunch)
- Parallel: Series A funds earmarked partly for "deals with online content owners" (Reuters via Business Today, Nov 2025) **[PRESS]** — [Business Today](https://www.businesstoday.in/technology/news/story/parag-agrawals-parallel-raises-100-million-from-kleiner-perkins-and-index-ventures-heres-why-its-significant-502250-2025-11-14)
- Firecrawl Alexandria "pays contributors when agents use their knowledge" (Sept 2026) **[VENDOR]** — [Firecrawl](https://www.firecrawl.dev/blog/introducing-alexandria-series-b)
- Cloudflare "Content Independence Day" (July 1, 2025): default to "block AI crawlers unless they pay creators for their content"; cites that getting traffic is "750 times more difficult" from OpenAI and "30,000 times more difficult" from Anthropic than from old Google; Prince: "Traffic was always a poor proxy for value." **[PRIMARY]** — [Cloudflare blog](https://blog.cloudflare.com/content-independence-day-no-ai-crawl-without-compensation/)
- Cloudflare July 2026 update: from Sept 15, 2026 new sites, new sites of existing customers and free-plan users default to allow search indexing but block AI training, AI agents and "mixed-use" crawlers on ad-supported pages; "Pay Per Crawl" replaced by "Pay Per Use" paying publishers when content "shapes an AI answer"; early partners Ceramic.ai and You.com; Prince: Cloudflare "must go further and act faster so that a sustainable ecosystem can emerge." **[PRESS]** — [TNW](https://thenextweb.com/news/cloudflare-block-ai-crawlers-pay-publishers)

**Consolidation and partnerships (2025–2026)**
- Elastic completes acquisition of Jina AI (Oct 9, 2025) — [Elastic IR](https://ir.elastic.co/News--Events/news/news-details/2025/Elastic-Completes-Acquisition-of-Jina-AI-a-Leader-in-Frontier-Models-for-Multimodal-and-Multilingual-Search/default.aspx)
- You.com acquires Graft (Oct 2025) — [Simplify](https://simplify.jobs/c/YOU-Dot-Com)
- Nebius agrees to acquire Tavily (Feb 10, 2026; ~$275M per Bloomberg) — [Nebius](https://nebius.com/newsroom/nebius-announces-agreement-to-acquire-tavily-to-add-agentic-search-to-its-ai-cloud-platform); [Sacra](https://sacra.com/research/tavily)
- Exa × Google Cloud grounding + marketplace (Apr 2026) — [Exa](https://exa.ai/blog/exa-google-cloud); Exa powering Firefox search (Aug 2026) — [Exa blog](https://exa.ai/blog)
- Cloudflare Web Search API reselling Ceramic.ai, Exa, Linkup (Oct 2, 2026) — [Cloudflare](https://developers.cloudflare.com/changelog/post/2026-10-02-introducing-web-search-api/)
- Brave listed on AWS Marketplace (July 2025) and SOC 2 Type II (Oct 2025) — [HN 44586242](https://news.ycombinator.com/item?id=44586242); [HN 45744078](https://news.ycombinator.com/item?id=45744078)

**Economics**
- Exa's exa-d post ("How to store the web in S3", Jan 13–14, 2026, 46 HN points) describes a Lance/S3 columnar framework for web-scale crawl data to cut recomputation and storage cost **[VENDOR]** — [Exa exa-d](https://exa.ai/blog/exa-d); [HN 46611063](https://news.ycombinator.com/item?id=46611063)
- Independent napkin math on Exa's infrastructure cost (Nov 26, 2025) **[PRACTITIONER]** — [kshivendu.dev](https://www.kshivendu.dev/blog/exa-napkin-math)
- Vals (Oct 2, 2026): some Keenable runs cost ~$190 (finance) and ~$281 (legal) per task; GPT-5.6 Sol + Exa averaged $18.97/task because some tasks triggered hundreds of search calls; "Model tokens made up about 95% of Keenable's $8.84 average cost" **[analyst]** — [AlphaSignal](https://alphasignal.ai/news/keenable-beats-every-search-tool-on-vals-finance-and-legal-ai-index)
- Parallel's own cost-per-1,000-questions figures show order-of-magnitude spreads: BrowseComp "frontier" tier Exa Auto 971 CPM vs Parallel Advanced 399 vs Perplexity 275 (Sept 9, 2026) **[VENDOR]** — [Parallel benchmarks](https://parallel.ai/benchmarks)

### Inferences
- The two big exits plus Cloudflare's default-block are mutually reinforcing: incumbents won't sell raw SERPs, publishers won't let crawlers in for free, so the economic niche is a licensed/compensated independent index — which is exactly what the 2026 funding went to (Keenable, Parallel, Exa, Linkup).
- Per-task LLM token spend dwarfs per-query search spend in agentic workloads (Vals: ~95% tokens). This favors providers whose results reduce the number of search calls (Exa's "7.6 queries per task" claim; Parallel's "more compute per search so agents make fewer searches") over providers competing on headline $/1K.
- Cloudflare's dual role (gatekeeper of crawl access and reseller of search) makes it the most consequential non-vendor actor; its choice of Exa/Linkup/Ceramic and exclusion of Perplexity and Brave is already shaping default stacks.

### Gaps
- Could not retrieve the body of Google's Jan 20, 2026 blog post or verify any "Web Search Service API".
- No primary Cloudflare blog text for the July 2026 Pay Per Use announcement (only TNW's report).
- No disclosed economics of any publisher-licensing deal (Linkup, Parallel, Perplexity payouts).
- Status of Google v. SerpApi after the Feb 20, 2026 motion to dismiss is unknown (search budget exhausted).

---

## Key Question 5: Where differentiation really is (own index vs SERP wrap vs hybrid vs post-processing) and what evidence shows

### Takeaway
On quality benchmarks the own-index providers (Perplexity, Exa, Parallel) and the aggregator (Tavily) are within a few points of each other and leaderboards flip month to month (Perplexity #1 on Artificial Analysis in Sept 2026; Exa 3.0 #1 in Oct 2026; Exa #1 on Vals in July 2026; Keenable #1 on Vals in Oct 2026 by 0.63 points). The layer that measurably moves outcomes is (a) having search at all (Vals: 2.9–7.4% → 30–50%) and (b) excerpt/extraction quality that lowers queries per task; the index layer drives cost, latency, storage rights and legal exposure more than it drives accuracy.

### Cited Findings

**Who owns an index (self-declared) vs who wraps**
- Own index: Exa ("one of the biggest among the independent players" — Head of Index, Oct 2026) — [HN 49963171](https://news.ycombinator.com/item?id=49963171); Brave ("own independent index, crawled and ranked by Brave") — [Brave](https://brave.com/search/api/); Keenable ("our own crawler, index and ranking") — [Keenable](https://keenable.ai); Parallel ("proprietary", "web-scale") — [Parallel](https://parallel.ai); Perplexity ("hundreds of billions of webpages") — [Perplexity](https://www.perplexity.ai/hub/blog/introducing-the-perplexity-search-api); Mojeek (MojeekBot) — [Mojeek](https://www.mojeek.com/services/search/web-search-api/); Kagi partially (Teclis/TinyGem) — [Kagi](https://help.kagi.com/kagi/api/overview.html); DeepSeek ("in-house search engine") — [DeepSeek](https://api-docs.deepseek.com/guides/search/)
- Aggregator: Sacra describes Tavily as "an asset-light aggregator that does not maintain its own search index" pulling "from multiple data sources and search engines in real time" **[PRESS]** — [Sacra Tavily](https://sacra.com/research/tavily); a16z says Tavily and Valyu crawl "periodically" with RL re-crawl decisions **[PRESS/VC]** — [a16z](https://a16z.com/search-wars-episode-2/)
- Contested: Keenable founder alleges "some players in the market, such as Parallel and Brave, may be using the same underlying search index" **[VENDOR allegation]** — [HN 49435555](https://news.ycombinator.com/item?id=49435555); HN user hartator claims SerpApi "has also now its own index" **[PRACTITIONER, unverified]** — [HN 49963171](https://news.ycombinator.com/item?id=49963171)
- SERP wrap: Google is suing SerpApi over scraping (see KQ6); HN practitioner view: "Everyone is just scraping them with residential proxies." (qingcharles) — [HN 49963171](https://news.ycombinator.com/item?id=49963171); Kagi and You.com resell Brave results among other sources (Brave lists both as customers) — [Brave](https://brave.com/search/api/)
- Post-processing specialists: Jina (Reader/Reranker/Embeddings) — [jina.ai](https://jina.ai); Firecrawl (scrape/crawl to Markdown; Alexandria indexes) — [firecrawl.dev](https://www.firecrawl.dev)

**Benchmark evidence (all vendor- or third-party-run; dates matter)**
- Artificial Analysis Search Index (Sept 2026 data, per Parallel's write-up): Perplexity Search (medium) 80 (top), Octen 77, Parallel Advanced 75, Brave LLM-context 75; "25 search API products across 12 providers on a fixed GPT-5.6 Luna agent harness" **[VENDOR-reported third-party data]** — [Parallel](https://parallel.ai/articles/best-ai-search-for-agents.md)
- Artificial Analysis Search Index (Oct 19, 2026, per Exa): Exa Search auto 80.3, lite 79.2; search queries per task: Exa auto 7.60, You.com 9.51, Parallel 9.59, DeepSeek 11.3, Perplexity 11.4, Brave 12.4, Firecrawl 15.4; "DeepSeek Search needs about 1.5x more queries than Exa, which offsets its lower price" **[VENDOR-reported third-party data]** — [Exa blog](https://exa.ai/blog/artificial-analysis-exa-3-best-search-api)
- Vals Web Search Index (Oct 2, 2026): fixed model/harness, swap search tool; private Finance Agent v2 + Legal Research sets; no-search baseline 2.9% (legal) and 7.4% (finance) vs 30–50% with search; conclusion "search is the driver of good performance on our index, not memorization or test-set leakage" **[third-party]** — [Vals](https://www.vals.ai/blogs/web-search-index). Leaderboard: Keenable Pro + GPT-5.6 Sol 49.08%, Exa + Claude Fable 5 48.45%, Claude native search 46.94%, Exa + GPT-5.6 Sol 45.2%, OpenAI native 43.6%; "The reported scores alone do not establish whether that difference is statistically significant"; "cannot separate retrieval quality from search volume" (Oct 21, 2026) **[analyst]** — [AlphaSignal](https://alphasignal.ai/news/keenable-beats-every-search-tool-on-vals-finance-and-legal-ai-index); July 16, 2026 snapshot had Exa first at 48.45% — [BenchLM](https://benchlm.ai/benchmarks/valsWebSearchIndex)
- Parallel-run (Sept 9, 2026; 50–100 question samples; LLM judge): SimpleQA Verified frontier tier — Parallel Advanced 97, Perplexity 95, Tavily 92, Exa Auto 91; BrowseComp frontier — Parallel Advanced 74, Perplexity 74, Exa 70, Tavily 66 (CPM 399 / 275 / 971 / 935); WideSearch — Exa 55.9, Tavily 55.9, Parallel 57.6, Perplexity 53.5; page notes "Perplexity is search-only. Parallel, Exa, and Tavily also use an extract tool." **[VENDOR]** — [Parallel benchmarks](https://parallel.ai/benchmarks)
- Exa-run (last updated Oct 19, 2026): "Exa leads every one of these six comparisons while returning faster in both brackets" (FRAMES/SealQA Lite vs Parallel basic, Auto vs Advanced); latency Exa Lite ~450ms vs Parallel basic 906ms; entity search Exa people R@1 72% vs Parallel 20.8%; Exa Agent High BrowseComp 74% at $0.50 vs Parallel Ultra 8x 58% at $2.40 **[VENDOR]** — [Exa vs Parallel](https://exa.ai/versus/parallel). Exa homepage separately claims BrowseComp Exa 91.8, Perplexity 91.5, Brave 83.5, Parallel 72.7 — [exa.ai](https://exa.ai)
- Perplexity-run search_evals (2026): BrowseComp Perplexity 0.805, OpenAI 0.720, Parallel 0.56, Anthropic 0.598, Exa 0.38; DSQA Perplexity 0.871, Anthropic 0.815, Parallel 0.81, Exa 0.53 **[VENDOR]** — [GitHub perplexityai/search_evals](https://github.com/perplexityai/search_evals)
- Tavily-republished Parallel numbers (Apr 27, 2026): Exa vs Parallel Advanced tied on FRAMES 87/87, SealQA 41/41; Parallel ahead on BrowseComp 51 vs 40 **[VENDOR]** — [Tavily blog](https://tavily.com/blog/exa-vs-parallel-benchmarking-retrieval-apis-for-ai-agents-in-2026)
- Keenable Needle (Aug 2026): live, fresh-query benchmark scored against "the reranked aggregate of the other engines" — HN criticized it as self-promotional **[VENDOR + PRACTITIONER]** — [HN 49466250](https://news.ycombinator.com/item?id=49466250)
- Exa ATLAS benchmark (Oct 8, 2026) and blog "Does the AI world really need another search benchmark?" (Oct 8, 2026) **[VENDOR]** — [Exa blog](https://exa.ai/blog)
- Firecrawl: agent using /search 94.7% SimpleQA; Alexandria agents "21% higher on answer quality than those using built-in web tools, across 845 tasks" **[VENDOR]** — [firecrawl.dev](https://www.firecrawl.dev); [Alexandria](https://www.firecrawl.dev/blog/introducing-alexandria-series-b)

**Where adoption comes from (as distinct from benchmark wins)**
- Distribution/default status: Brave via OpenClaw (~700k users) and Anthropic; Exa via Cursor, Cognition, Firefox, Google Gemini grounding, OpenRouter resale ("$4 per 1000 results" per stefs); Tavily via LangChain/GPT Researcher open-source lineage and 3M+ SDK downloads; Parallel via Google Cloud grounding and OpenRouter/Vercel — [Brave](https://brave.com/blog/openclaw/); [Exa](https://exa.ai/blog/exa-google-cloud); [Nebius](https://nebius.com/newsroom/nebius-announces-agreement-to-acquire-tavily-to-add-agentic-search-to-its-ai-cloud-platform); [parallel.ai](https://parallel.ai); [HN 49963171](https://news.ycombinator.com/item?id=49963171)
- Agrawal's stated design choice: spend more compute per search so "agents make fewer searches" (Nov 2025) **[VENDOR]** — [HN 45837425](https://news.ycombinator.com/item?id=45837425); Exa's "Dynamic Highlights" (Aug 2026) and "text extraction models that cut LLM token counts by over 20x" **[VENDOR]** — [Exa blog](https://exa.ai/blog); [Exa Series C](https://exa.ai/blog/announcing-series-c)

### Inferences
- Every vendor's own benchmark puts itself first, and the two most-cited third-party indexes (Artificial Analysis, Vals) show top-tier gaps of ~1–5 points that flip within weeks — so "benchmark leadership" is not a durable differentiator and should be read as marketing.
- The evidence that does separate providers is operational: latency tiers (Keenable <250ms p95, Tavily 180ms p50, Exa Lite ~450ms, Parallel standard ~1–3s per Exa's measurements), queries-per-task efficiency, storage rights (Brave only), ZDR terms, EU residency (Linkup, Mojeek), and price floors enabled by owning an index (Parallel/Keenable $1; DeepSeek $0.75).
- Owning an index is a necessary condition for low floor prices and for legal insulation from Google's anti-scraping campaign, but not a sufficient condition for quality — Tavily (aggregator) matches own-index providers on SimpleQA in Parallel's own tables, and the cheapest own-index entrants (Ceramic, early Keenable) drew the sharpest quality complaints.
- Post-processing (extraction, highlights, reranking) is where the measurable efficiency gains are showing up (Exa's queries-per-task lead; Alexandria's claimed +21%), consistent with Vals' finding that token spend dominates cost.

### Gaps
- No Artificial Analysis primary page could be fetched (404); all AA figures are vendor-relayed.
- No independent latency benchmark across all providers was retrieved (Openbenchmarks figures cited only via Parallel).
- No evidence found on whether Tavily's post-acquisition stack has changed to include an owned index.

---

## Key Question 6: Risks and critiques (dependence on Google/Bing, SERP-scraping legality, crawler blocking, Cloudflare, licensing costs)

### Takeaway
The legal and access environment hardened sharply in 2025–2026: Google sued SerpApi under the DMCA (Dec 19, 2025) and Reddit sued SerpApi and others (Oct 2025); Cloudflare de-listed Perplexity as a verified bot for stealth crawling (Aug 2025), moved to default-block AI agents and "mixed-use" crawlers on ad-supported pages (effective Sept 15, 2026), and became a reseller choosing which search providers to carry. Independent-index vendors are exposed to crawl-blocking and index cost ("painfully expensive"); wrappers are exposed to litigation and upstream shutdowns; everyone is exposed to price compression from DeepSeek, Ceramic and model-native search.

### Cited Findings

**SERP-scraping legal exposure**
- Google v. SerpApi filed Dec 19, 2025 in federal court: DMCA anti-circumvention plus ToS breach; alleges "hundreds of millions of fake search queries" and proxy use; SerpApi moved to dismiss Feb 20, 2026 arguing "no one owns the internet"; Reddit sued SerpApi and other scrapers in Oct 2025 and backed Google's suit **[PRESS]** — [IPWatchdog](https://ipwatchdog.com/2025/12/26/google-sues-serpapi-parasitic-scraping-circumvention-protection-measures/); [Search Engine Land](https://searchengineland.com/google-sues-serpapi-466541); [PPC Land](https://ppc.land/google-sues-serpapi-over-search-scraping-in-copyright-lawsuit/); [Proxyway](https://proxyway.com/news/google-sues-serpapi)
- Practitioner framing: "These services only exist because Google refuses to provide a paid search API." (mjmvisser) — [HN 50138531](https://news.ycombinator.com/item?id=50138531)

**Upstream dependence**
- Bing API retirement (Aug 11, 2025) and Google Custom Search closure (ends Jan 1, 2027) remove the two historical wholesale sources — [Microsoft](https://learn.microsoft.com/en-us/lifecycle/announcements/bing-search-api-retirement); [Google](https://developers.google.com/custom-search/v1/overview)
- Kagi and You.com appear on Brave's customer-logo wall, i.e., some "independent" consumer brands depend on Brave's index — [Brave](https://brave.com/search/api/)
- Perplexity "competes with its own customers through its consumer interface" (Sacra) — [Sacra](https://sacra.com/research/tavily)

**Crawler blocking and publisher pushback**
- Cloudflare (Aug 4, 2025): Perplexity's declared crawler ~20–25M daily requests plus an undeclared crawler ~3–6M daily requests across "tens of thousands of domains", rotating user agents/ASNs, impersonating Chrome on macOS, ignoring robots.txt; Cloudflare de-listed Perplexity as a verified bot and added managed-rule signatures; ChatGPT-User stopped when disallowed in the same test **[PRIMARY]** — [Cloudflare blog](https://blog.cloudflare.com/perplexity-is-using-stealth-undeclared-crawlers-to-evade-website-no-crawl-directives/); Perplexity called the claims "a misunderstanding – or a PR stunt" and argued robots.txt applies to training, not user-triggered fetches **[PRESS]** — [Slashdot](https://tech.slashdot.org/story/25/08/05/2153232/perplexity-says-cloudflares-accusations-of-stealth-ai-scraping-are-based-on-embarrassing-errors); [Search Engine Land](https://searchengineland.com/cloudflare-vs-perplexity-ai-crawling-460016)
- Cloudflare default-block for new customers and Pay Per Crawl beta (July 1, 2025) — [Cloudflare](https://blog.cloudflare.com/content-independence-day-no-ai-crawl-without-compensation/); [MIT Technology Review](https://www.technologyreview.com/2025/07/01/1119498/cloudflare-will-now-by-default-block-ai-bots-from-crawling-its-clients-websites/)
- Cloudflare Sept 15, 2026 defaults: block AI training, AI agents and "mixed-use" crawlers on ad-supported pages for new sites and free plans; Pay Per Use (Ceramic.ai, You.com partners); "automated bots now drive more than half of all web traffic"; Google's crawler gets "roughly twice the data access of rival AI firms" **[PRESS]** — [TNW](https://thenextweb.com/news/cloudflare-block-ai-crawlers-pay-publishers)
- Exa: single HN report of "indexing personal site data ignoring robots.txt" (Jan 2026, 1 point) and robots.txt questions at launch (May 2025) **[PRACTITIONER, unverified]** — [HN 46574182](https://news.ycombinator.com/item?id=46574182); [HN 43906841](https://news.ycombinator.com/item?id=43906841)
- Mojeek positions MojeekBot as an "Established" crawler that "respects the Robots Exclusion Protocol" **[VENDOR]** — [Mojeek](https://www.mojeek.com/services/search/web-search-api/)
- Cloudflare's crawl-vs-referral statistics ("750 times" OpenAI; "30,000 times" Anthropic) frame the publisher grievance — [Cloudflare](https://blog.cloudflare.com/content-independence-day-no-ai-crawl-without-compensation/)

**Terms, data retention and rights**
- Brave ToS confusion ("prohibit using responses for AI inference" on the standard plan; separate AI plan) — [HN 46822822](https://news.ycombinator.com/item?id=46822822); Brave credit now requires attribution and a card — [Implicator](https://www.implicator.ai/brave-drops-free-search-api-tier-puts-all-developers-on-metered-billing/)
- Storage/resyndication: Ceramic terms restrict storing output beyond real-time display; "Brave is the only one I've found that'll let you store their results" (pclark); Cloudflare's ZDR claim for Exa disputed by Exa staff as a documentation error — [HN 49963171](https://news.ycombinator.com/item?id=49963171)
- Exa lists Zero Data Retention as an Enterprise feature — [Exa pricing](https://exa.ai/pricing); DeepSeek lacks ZDR per practitioners — [HN 50138531](https://news.ycombinator.com/item?id=50138531)
- Mojeek: API agreement "does not license the third-party content on the linked pages" — [Mojeek](https://www.mojeek.com/services/search/web-search-api/)
- Parallel ToS content clause criticized as possibly barring lawful uses (dragonwriter) — [HN 45837425](https://news.ycombinator.com/item?id=45837425)

**Cost of independence**
- Styskin: "the cost of serving and scanning the whole internet is enormous because of the volume"; on index cost "Don't ask — it is painfully expensive" — [TechCrunch](https://techcrunch.com/2026/08/25/accel-backed-keenable-is-indexing-the-web-for-ai-agents/); a16z: Exa runs 144 H200s and re-indexing is "a non-trivial feat" — [a16z](https://a16z.com/search-wars-episode-2/); Brave's counter-position: "Index size is a vanity stat." — [Brave](https://brave.com/search/api/)

**Price compression**
- DeepSeek $0.75 (Oct 2026), Ceramic.ai $0.25 via Cloudflare (Oct 2026), Perplexity Fast $1 (Sept 2026), Parallel Fast $1, Keenable $1 at volume vs the $5 anchor — [DeepSeek](https://api-docs.deepseek.com/guides/search/); [HN 49963171](https://news.ycombinator.com/item?id=49963171); [Perplexity](https://docs.perplexity.ai/getting-started/pricing); [parallel.ai](https://parallel.ai); [keenable.ai](https://keenable.ai)
- Practitioners expect negative prices ("providers paying for placement") — [HN 50138531](https://news.ycombinator.com/item?id=50138531)

### Inferences
- Perplexity's open API is the most legally and reputationally exposed own-index offering (de-listed by Cloudflare; excluded from Cloudflare's reseller lineup; BBC legal letter and paywall-bypass history), which may explain why it leads some quality benchmarks yet drew near-zero HN engagement at launch.
- Cloudflare's Sept 2026 "agent" blocking category creates a new risk for live-fetch/extraction products (Tavily Extract, Firecrawl, Jina Reader, Exa Contents, Linkup Fetch) distinct from index crawlers; none of the vendors' current marketing addresses it.
- SERP wrappers (Serper, SerpApi, Bright Data) remain the cheapest path to Google-quality results but now carry direct litigation risk; expect enterprise buyers to prefer vendors who can assert an owned or licensed index.

### Gaps
- Status of Google v. SerpApi after Feb 2026 and of Reddit's suits is unknown.
- No publisher-side data on how many sites block specific AI-search crawlers (e.g., Exa's, Keenable's, Parallel's user agents); crawler UA names for Exa/Keenable/Parallel not verified.
- No reports found on outages or SLA breaches for any provider.
- Cloudflare's own text for the July 2026 Pay Per Use change was not retrieved; scope details (which plans/customers) conflict across secondary sources.
