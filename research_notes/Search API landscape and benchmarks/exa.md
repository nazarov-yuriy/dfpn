# Exa (exa.ai, formerly Metaphor): index, retrieval, products, pricing, benchmarks — as of 2026-11-05

Scope note: all claims are dated. "VENDOR" = Exa's own claim; "COMPETITOR" = a rival vendor's published number (Parallel, Tavily, Perplexity); "INDEPENDENT" = a third party with no product in the category (Artificial Analysis, press). Web-search budget was exhausted near the end of this research run, so a few items (Hacker News threads, Common Crawl relationship, arXiv usage) could not be fully chased and are recorded as gaps.

## 1. Company: founding, founders, funding, headcount, customers

### Takeaway
Exa was founded in 2021 as Metaphor Systems by Harvard friends Will Bryk (CEO) and Jeff Wang, went through YC S21, launched a consumer neural search engine in Nov 2022, rebranded to Exa in Jan 2024, and has since raised a $17M Series A (Jul 2024, Lightspeed), an $85M Series B at $700M (Sep 2025, Benchmark) and a $250M Series C at $2.2B (May 2026, a16z). It reported crossing $100M annualized revenue in Oct 2026 (VENDOR) with ~2B requests/month; headcount is not disclosed anywhere I found.

### Cited Findings
- Founding/timeline: "Founded 2021. First search engine launched November 2022," two weeks before ChatGPT; API requests followed — [Exa Series B post, 2025-09-03](https://exa.ai/blog/announcing-series-b) (VENDOR)
- Exa was in the summer-2021 YC cohort; founders Will Bryk (CEO, 27 in 2024) and Jeff Wang (26) "met as freshmen at Harvard" — [TechCrunch, 2024-07-16](https://techcrunch.com/2024/07/16/exa-raises-17m-lightspeed-nvidia-ycombinator-google-ai-models/) (INDEPENDENT press)
- Metaphor pitched itself in YC as "Google 2.0" after GPT-3 showed LLMs could understand intent; Bryk and Jeff built an earlier crowdsourced-link search engine as Harvard roommates — [Latent Space podcast, 2025-01-10](https://www.latent.space/p/exa); [Latent Space wiki](https://latent.space/wiki/exa-f75ed103/)
- Rebrand: "Announcing Exa" (renaming Metaphor to Exa), 2024-01-25; name explained as Exa = 10^18 vs Google = 10^100; mission "organize the world's knowledge" — [exa.ai/blog/announcing-exa](https://exa.ai/blog/announcing-exa) (VENDOR)
- In Feb 2024 Exa was "a seven-person startup" with "over 4,000 developers signed up for the API in recent months" — [Cerebral Valley deep dive, 2024-02-01](https://cerebralvalley.beehiiv.com/p/exa-prev-metaphor-aims-reshape-web-search)
- Metaphor's Nov 2022 public launch was described as a search engine that "predicts a likely link based on a text input," queries ideally ending mid-sentence or with a colon — [The Decoder, 2022](https://the-decoder.com/?p=1831)
- Series A: $17M led by Lightspeed (Guru Chahal), with NVentures and Y Combinator; total raised $22M including a prior $5M seed; valuation not disclosed; Databricks named as marquee customer (training-set curation) — [TechCrunch, 2024-07-16](https://techcrunch.com/2024/07/16/exa-raises-17m-lightspeed-nvidia-ycombinator-google-ai-models/); [Exa Series A post, 2024-07-16](https://exa.ai/blog/series-a)
- Series B: $85M led by Benchmark at $700M valuation, with Lightspeed, YC, NVentures; Peter Fenton (Benchmark) joined the board; named customers Cursor and Notion AI; "thousands of companies"; plan to build "5x bigger GPU cluster" — [Exa Series B post, 2025-09-03](https://exa.ai/blog/announcing-series-b) (VENDOR); corroborated by [SiliconANGLE, 2025-09-03](https://siliconangle.com/?p=709880) and [Latham & Watkins deal note](https://www.lw.com/en/news/2025/09/latham-watkins-advises-exa-in-us85-million-series-b-financing-with-benchmark-and-lightspeed)
- Revenue estimate at Series B: Sacra estimated ~$10M annualized revenue in Sep 2025 (up ~11x YoY from ~$880K; ~$1.86M at end-2024), implying ~70x multiple; $111M total raised; customers named Cursor, Vercel v0, Lovable — [Sacra, 2026-01-09](https://sacra.com/research/exa-at-10m-growing-11x-yoy) (INDEPENDENT estimate, not company disclosure)
- Series C: $250M led by a16z at $2.2B valuation (2026-05-20); ">5,000 companies" and ">400,000 developers"; named customers Cursor, Cognition, HubSpot, OpenRouter, Monday.com; crawlers "track over 500 billion URLs"; Marcus Holm (ex-President, LaunchDarkly) joined as CRO; hires included Meta's head of retrieval infrastructure, Yandex's head of search backend, and a research team from Google — [Exa Series C post, 2026-05-20](https://exa.ai/blog/announcing-series-c) (VENDOR); echoed by [AlphaSignal](https://alphasignal.ai/news/exa-raises-250m-as-ai-agents-threaten-to-replace-human-web-search)
- Revenue milestone: "Annualized revenue passed $100M"; "roughly 10x per year for three years"; "about 2 billion requests per month"; ">200,000 teams" — [Exa blog, 2026-10-13](https://exa.ai/blog/100m-run-rate) (VENDOR)
- Headcount: not stated in Series B, Series C, or $100M posts; the $100M post refers only to a "small but legendary team" — [Exa blog, 2026-10-13](https://exa.ai/blog/100m-run-rate)
- A conflicting valuation ($550M for Series B) appears on one aggregator page and is an outlier vs all primary sources — [salestools.io](https://salestools.io/en/report/exa-85m-series-b-september-2025)

### Inferences
- The Series B ($700M, Sep 2025) to Series C ($2.2B, May 2026) step-up in eight months, plus the Oct 2026 $100M ARR claim, is consistent with Exa's stated ~10x/yr growth; Sacra's $10M ARR (Sep 2025) → $100M (Oct 2026) is roughly 10x in 13 months.

### Gaps
- Headcount: no primary or reliable secondary figure found beyond "seven people" in Feb 2024.
- No independently audited revenue figure; the $100M ARR number is company-reported.

## 2. Architecture: embeddings over its own crawl, index size, vector DB, GPU cluster, keyword+neural, Exa 2.0/3.0 modes, freshness, contents, Websets, research API

### Takeaway
Exa runs its own crawler (ExaSearchBot), parses pages into S3 (Lance format via its "exa-d" framework), embeds every document with in-house transformer models originally trained on a link-prediction ("neural PageRank") objective, serves them from a custom C++/Rust vector database (Matryoshka 256-d + binary quantization + 100k clusters), fuses dense retrieval with a sparse BM25 inverted index via reciprocal rank fusion, and applies relevance and authority rerankers. Index claims have grown from "billions of documents" (Mar 2025) to "2 trillion URLs tracked / 100 billion pages served" (Oct 2026). Search types evolved from neural/keyword/auto (2024) → Fast/Auto/Deep (Exa 2.0, Oct 2025) → Instant, deep-lite, deep, deep-reasoning (early 2026) → Lite/Auto/Deep plus the Agent API (Exa 3.0, Oct 2026).

### Cited Findings

**Training objective and models**
- "We train our search engine to predict the next link"; founders bought ~$1M of GPUs; the model is trained to understand links, not words, using links people share on the web as training data; predicts the most probable next link (or 10) analogous to next-word prediction — [TechCrunch, 2024-07-16](https://techcrunch.com/2024/07/16/exa-raises-17m-lightspeed-nvidia-ycombinator-google-ai-models/)
- Core model trained on link prediction: text surrounding a link is shown with the link hidden and the model predicts which document it points to; Bryk calls it "document prediction" / "neural PageRank" because it learns which pages people link to; later supplemented with synthetic data and SFT; Exa uses LLMs as relevance labelers because human labelers "tended to match keywords rather than meaning"; Exa is "neural all the way" and never relied on keyword retrieval; rerankers run on 10–1,000 candidates depending on cost/quality — [Latent Space, 2025-01-10](https://www.latent.space/p/exa) (VENDOR interview)
- Jan 2024: "algorithm uses transformers end-to-end," filters "by meaning, not by keyword"; Highlights chunk and embed full pages with a "paragraph prediction model" — [Announcing Exa, 2024-01-25](https://exa.ai/blog/announcing-exa)
- Exa 2.0: a new embedding model "pretrained and fine-tuned" for semantic search, trained "over a month on a 144x H200 cluster"; vector DB updated with new clustering algorithms, lexical compression, and assembly optimizations in Rust; Exa "crawls and parses tens of billions of webpages and refreshes them every minute" — [Exa 2.0, 2025-10-10](https://exa.ai/blog/exa-api-2-0) (VENDOR)
- Exa 2.1: "scaled our pre-training and test-time compute by an order of magnitude"; built its own semantic and lexical databases and crawling infrastructure — [Exa 2.1, 2025-11-24](https://exa.ai/blog/exa-api-2-1) (VENDOR)
- Exa 3.0: "a larger embedding model, trained with more compute and data than any previous Exa model"; Dynamic Highlights GA ("95% fewer tokens than full page text" while improving answer quality; a model selects tokens across all results); "billions of documents added" (1.27B e-commerce listings, 211M+ local businesses, real-time news/sports/weather/markets, flights, events, transit, podcasts) — [Exa 3.0, 2026-10-19](https://exa.ai/blog/exa-3) (VENDOR)

**Crawl and index pipeline**
- Pipeline: URL discovery + distributed crawl, custom HTML parser, storage in S3; "many petabytes" of documents; "billions of documents"; most crawled documents are low quality so selecting good URLs is central; challenges: "crawlers get blocked," "query variety is nearly infinite," custom DBs are tricky, metadata updates need substantial compute at scale — [How we're building the next generation of search, 2025-03-11](https://exa.ai/blog/how-to-build-nextgen-search) (VENDOR)
- exa-d data framework: "hundreds of billions of pages, petabytes of raw content"; data stored in Lance format on S3 with a global manifest; jobs run on Ray Data with embedding models kept resident in GPU memory; crawlers detect changes and regenerate embeddings before a query arrives; update frequency varies (news hourly, some papers never) — [exa-d, 2026-01-13](https://exa.ai/blog/exa-d) (VENDOR)
- Crawler is `ExaSearchBot`; respects robots.txt, rate-limits per site, doesn't bypass logins/paywalls/CAPTCHAs; removal via `noindex`; index "tracks over 2 trillion URLs and serves 100 billion pages" as of Oct 2026; pages "discovered and refreshed continuously," no fixed recrawl schedule — [Exa docs FAQ](https://exa.ai/docs/admin/faqs.md) (VENDOR)
- Index coverage categories: news (incl. podcast/video transcripts), code & docs (GitHub, package registries), companies & people, financial markets (SEC filings, earnings calls), research publications (papers, patents, grants, clinical trials), legal/public records, sports/weather/places, cybersecurity (CVE/GHSA) — [Exa docs: The Exa Index](https://docs.exa.ai/reference/the-exa-index)

**Index size claims over time (all VENDOR)**
- Feb 2024: goal of crawling "100 billion websites"; no index size stated — [Cerebral Valley, 2024-02-01](https://cerebralvalley.beehiiv.com/p/exa-prev-metaphor-aims-reshape-web-search)
- Mar 2025: "billions of documents," "many petabytes" — [Exa blog, 2025-03-11](https://exa.ai/blog/how-to-build-nextgen-search)
- Oct 2025: "tens of billions of webpages" — [Exa 2.0](https://exa.ai/blog/exa-api-2-0)
- Jan 2026: "hundreds of billions of pages" (stored, pre-processing) — [exa-d](https://exa.ai/blog/exa-d)
- Feb 2026: searches "tens of billions of pages" in under 200ms — [Exa Instant, 2026-02-12](https://exa.ai/blog/exa-instant)
- May 2026: crawlers "track over 500 billion URLs" — [Series C post](https://exa.ai/blog/announcing-series-c)
- Jul 2026: publication index of 350M publications — [Exa changelog, 2026-07-23](https://docs.exa.ai/changelog)
- Aug 3, 2026: Bryk (X post) says Exa "serves 80 billion pages and tracks 1.4 trillion URLs," targets "Google-scale" in early 2027, acknowledging index sizes are hard to compare — [Runtimewire, 2026-08-03](https://runtimewire.com/article/exa-search-index-80-billion-pages-google-scale-2027)
- Sep 2026: Exa Snapshot draws on "over 400 billion webpage snapshots" spanning ~20 years (`snapshotAsOf` parameter) — [Exa Snapshot, 2026-09-17](https://exa.ai/blog/exa-snapshot)
- Oct 2026: "tracking over 2 trillion URLs and serving 100 billion pages"; "100s of billions of web documents" — [Exa 3.0](https://exa.ai/blog/exa-3); [$100M post](https://exa.ai/blog/100m-run-rate)
- Oct 2026: 211M places, 3.2M podcast episodes with transcripts — [Places, 2026-10-05](https://exa.ai/blog/places-search); [Podcasts, 2026-10-29](https://exa.ai/blog/podcast-search)

**Custom vector database (VENDOR engineering post)**
- Requirements: billions of 4096-float vectors, metadata filters (dates, domains), <100ms, >500 QPS; techniques: Matryoshka embeddings truncated to 256 dims (20x memory cut), binary quantization to 1 bit/dim (16x more), asymmetric dot-product with 4-dim subvector lookup tables kept in CPU registers (hot path in C++ rather than Rust), 100,000 clusters searched by nearest cluster (~1000x throughput gain), rerank of extra candidates with uncompressed vectors; inverted indexes for filterable fields (category, date, domain, keyword) so search runs only over the filtered set; clustering preferred to HNSW because it handles filters and sharding better; ~10x cheaper than cloud vector-DB quotes; memory footprint "less than a gaming PC" — [How we built a web-scale vector database, 2024-12-17](https://exa.ai/blog/building-web-scale-vector-db)
- Exa also serves BM25 and published a 50%-memory-reduction encoding scheme for it — [Serving BM25 with 50% memory reduction, 2025-05-05](https://exa.ai/blog/bm25-optimization)
- Highlights server scaling post (embedding full pages at query time) — [Scaling our highlights server, 2024-02-21](https://exa.ai/blog/scaling-our-highlights-server)

**How keyword and neural retrieval are combined (VENDOR)**
- Query pipeline as a typed DAG: query enrichment (filters; a query classifier and freshness model are mentioned), query embedding → token-level ANN worker group (replicated encoders/scorers), a sparse retrieval node on an inverted index fused with dense results via reciprocal rank fusion (k=60), domain-diversity step, safe-search filter, two rerankers (relevance and authority) with authority-weighted final ranking, then highlights/summary; serving ~250ms; limitation: DAG can't express cycles/feedback loops — [Composing a Search Engine, 2026-04-17](https://exa.ai/blog/composing-a-search-engine)
- exa-code (Sep 2025) runs "hybrid search over more than 1 billion webpages," extracts code examples from top results and reranks them, returning a few hundred tokens — [exa-code, 2025-09-25](https://exa.ai/blog/exa-code)
- a16z interview summary: Exa "handles both semantic and keyword queries, with filters and toggles" — [Summify summary of a16z Deep Dive, 2026-06](https://summify.io/discover/how-exa-is-building-the-perfect-search-engine-deep-dives-wit-k6OkMk) (secondary)

**GPU cluster (VENDOR)**
- Cluster 1 (2021, bought with half the seed money): 80x A100-80GB across 10 nodes. "Exacluster" (late 2024/2025): 144x H200 (141GB) in 18 Lenovo SR680a V3 nodes, 20TB HBM3, 36TB DDR5, 270TB NVMe, ConnectX-7/BlueField-3, 100kW, ~$5M; combined 224 GPUs, ~168 FP16 PFLOPs; used to embed billions of pages, train a reranker, pre-train (e.g., 7B param runs on 16 nodes); "a run that used to take a week ... can now finish in ~1 day"; inference needs grew 100x by late 2024; stack: Pulumi, Ansible/Kubespray, NVIDIA operators, Alluxio cache over S3, Flyte — [Meet the Exacluster, 2025-05-15](https://exa.ai/blog/meet-the-exacluster); hardware also covered by [Tom's Hardware, 2025-01-11](https://www.tomshardware.com/tech-industry/artificial-intelligence/nvidia-hopper-based-100kw-cluster-deploys-with-144-h200-gpus-exacluster-features-192-96-core-cpus-36tb-ddr5-ram-and-270tb-of-nvme-storage)
- Inference runs on a mix of own cluster and AWS — [Latent Space, 2025-01-10](https://www.latent.space/p/exa)
- Series B plan: "5x bigger GPU cluster" — [Series B post, 2025-09-03](https://exa.ai/blog/announcing-series-b)

**Search types / modes timeline (VENDOR docs and changelog)**
- 2024-12-11: Auto became default search type — [Exa changelog](https://docs.exa.ai/changelog)
- 2025-07-29: `type="fast"` launched, p50 < 425ms — [changelog](https://docs.exa.ai/changelog); [Fastest search API post, 2025-07-29](https://exa.ai/blog/fastest-search-api)
- 2025-10-10 Exa 2.0: Exa Fast "under 350ms end-to-end P50" (~30% faster than next-fastest, measured from us-west-2 with benchmark code on GitHub); Exa Auto default, higher quality; Exa Deep agentic endpoint at 3.5s P50 (searches, processes, searches again) — [Exa 2.0](https://exa.ai/blog/exa-api-2-0)
- 2025-10-28: major SDK release; contents returned by default; `use_autoprompt` deprecated; 2025-11-20: `type="deep"` with query expansion and summaries; 2025-11-05: automatic language filtering — [changelog](https://docs.exa.ai/changelog)
- 2025-11-24 Exa 2.1: Fast "most accurate search API that's sub 500ms"; MCP server got a deep search tool; APIs that wrap Google have a ~1000ms floor — [Exa 2.1](https://exa.ai/blog/exa-api-2-1)
- 2026-02-05/12: Exa Instant, "sub-200ms," "up to 15x faster than providers tested" (Tavily Ultra Fast, Brave, Parallel one-shot; SealQA queries with random words to defeat caching; tested from us-west-1 with ~50ms network latency); Google-wrapping APIs have >700ms P50 — [Exa Instant, 2026-02-12](https://exa.ai/blog/exa-instant); [changelog](https://docs.exa.ai/changelog)
- 2026-03-04 Exa Deep revamp: runs on Exa Instant + LLM reasoning; "optimized query expansion and LLM reasoning"; multiple search agents in parallel; `outputSchema` with `grounding` (URL, title, confidence per field; ≤10 properties, 2 nesting levels); `deep` 4–12s at $12/1k (20% cheaper than before), `deep-reasoning` 12–50s at $15/1k; ~20% of Deep queries are scientific literature — [Exa Deep, 2026-03-04](https://exa.ai/blog/exa-deep)
- 2026-04-01: `/research` endpoint deprecated and replaced by `/search` with `deep-reasoning`; `resolvedSearchType` and `highlightScores` removed May 1; `startCrawlDate`/`endCrawlDate` ignored — [changelog](https://docs.exa.ai/changelog)
- 2026-04-20 Deep Max announced ("releasing soon," contact sales): frontier LLMs + dozens of parallel Exa Search calls — [Deep Max](https://exa.ai/blog/deep-max)
- 2026-06-16 Exa Agent API (effort modes, `outputSchema`, dataset input); 2026-06-24 Exa Connect (partner data sources: Fiber.ai, Similarweb, Baselayer, Polymarket, Macrobond, etc.); 2026-07-01 `agent_run` in MCP; 2026-09-24 Agent Ultra — [changelog](https://docs.exa.ai/changelog); [Agent Ultra, 2026-09-25](https://exa.ai/blog/exa-agent-ultra)
- 2026-03-30 Monitors (scheduled searches → webhook); 2026-10-29 Monitors v2 — [changelog](https://docs.exa.ai/changelog); [Monitors v2](https://exa.ai/blog/monitors-v2)
- 2026-10-19 Exa 3.0: `lite` added; recommended types now `lite`, `auto`, `deep`; `fast`, `instant`, `deep-reasoning` are legacy; responses gained `warnings`/`notices` — [changelog](https://docs.exa.ai/changelog)
- Current mode descriptions: `auto` ~1s default; `lite` ~450ms, cache-only content (results without a cached copy are dropped if text/highlights requested; rejects `outputSchema`, `summary`, `maxAgeHours`, `additionalQueries`); `deep-lite` ~4s; `deep` 4–15s; `numResults` default 10, max 100, no pagination — [Exa docs: How Exa search works](https://docs.exa.ai/reference/how-exa-search-works); [Evaluating Exa search](https://docs.exa.ai/reference/evaluating-exa-search)

**Content extraction**
- Options: `text` (clean body, cap with `maxCharacters`), `highlights` (query-relevant excerpts; bare `highlights: true` recommended), `summary` (runs an LM per page, extra cost); `contents.maxAgeHours` controls cache age (omitted = cache if available; N = cache if newer than N hours; 0 = always fetch; -1 = cache only); `snapshotAsOf` for historical versions — [Exa docs](https://docs.exa.ai/reference/how-exa-search-works)
- Freshness-control history: `livecrawl: "preferred"` added 2025-06-07 (now deprecated); `maxAgeHours` replaced `livecrawl` 2026-02-02; markdown default 2025-06-23; per-URL `statuses` 2025-05-22 — [changelog](https://docs.exa.ai/changelog)
- Highlights for agents (2026-04-22) and Dynamic Highlights research preview (2026-08-28; allocates excerpts across the full result set; beta header) — [Exa Highlights](https://exa.ai/blog/highlights-for-agents); [Dynamic Highlights](https://exa.ai/blog/dynamic-highlights)
- Series C claim: text-extraction models "reduce LLM token counts by over 20x" — [Series C post](https://exa.ai/blog/announcing-series-c)

**Websets (bulk entity search)**
- Websets deploys "an army of agents" using Exa's embedding search to build "nearly comprehensive" entity lists (people, companies, articles); positioned as the test-time-compute product vs Exa Search as the "base model" — [Websets vs Google, 2025-02-19](https://exa.ai/blog/websets-evals); [Next-gen search post, 2025-03-11](https://exa.ai/blog/how-to-build-nextgen-search)
- Websets billed in separate credits: free tier 1,000 credits (up to 25 results); Core/Starter $49/month for 8,000 credits; Pro $449/month for 100,000 credits; 5 credits per email/phone, 2 per other enrichment row — [Exa Websets FAQ](https://exa.ai/docs/websets/faq.md); [websets.exa.ai/billing](https://websets.exa.ai/billing)
- A competitor review says Exa's docs now steer new list-building to Exa Agent rather than Websets — [Crustdata review, 2026](https://crustdata.com/reviews/exa) (COMPETITOR, unverified)

**Research API → Agent**
- The standalone `/research` endpoint was deprecated 2026-04-01 in favor of `deep-reasoning`, then Exa Agent (2026-06-16) with `minimal`…`xhigh` fixed-effort tiers and metered `auto`/`ultra` modes — [changelog](https://docs.exa.ai/changelog); [pricing](https://exa.ai/pricing)
- Exa built a research multi-agent system with LangGraph/LangSmith (LangChain case study) — [LangChain blog, 2025-06-30](https://blog.langchain.com/exa/)

### Inferences
- Exa's architecture has drifted from "neural all the way" (Bryk, Jan 2025) to an explicitly hybrid design: the Apr 2026 "Composing a Search Engine" post shows a BM25 inverted-index node fused with dense ANN via RRF, plus a freshness model and authority reranker. This is a meaningful change from the 2022–2024 pure-embedding story and likely explains improved performance on exact-match/factoid tasks.
- Index-size numbers are inconsistent in units (pages stored vs pages served vs URLs tracked) and jumped 500B → 1.4T → 2T "URLs tracked" within five months of 2026; treat them as marketing-grade.

### Gaps
- No published p95 latency figures from Exa; only p50/approximate numbers.
- Exa does not publish a recrawl cadence or freshness SLA; "refreshes every minute" (Exa 2.0) is unquantified.
- No detail on the current embedding model size, dimensionality, or training-data mix beyond "larger"/"more compute."

## 3. Why Exa performs strongly on agent-search benchmarks (and known weaknesses)

### Takeaway
Exa's own explanation: long natural-language queries are embedded directly ("search for meaning"), the index stores full parsed page text plus embeddings so results carry usable content (highlights) rather than SERP snippets, rerankers trade compute for quality, and retrieval quality means agents need fewer search calls. Independent and competitor evidence partially supports this (AA's Oct 2026 index put Exa auto first and showed Exa needing ~7.6 queries/task vs 9.5–15.4 for others), but competitor harnesses repeatedly show Exa behind Parallel/Perplexity on BrowseComp and as the highest-cost provider per task, and its measured latency exceeds advertised figures.

### Cited Findings

**Exa's stated reasons (VENDOR)**
- Built "from the ground up for LLMs to use"; plugging Exa retrieval into an LLM gives strong factuality "with minimal prompting effort" — [Exa api-evals, 2025-01-24](https://exa.ai/blog/api-evals)
- Handles long queries including full paragraphs; filters out "noisy SEO results"; highlights users saw "significant increases in conversion compared with Bing" — [Announcing Exa, 2024-01-25](https://exa.ai/blog/announcing-exa)
- Keyword retrieval "cannot benefit from more compute and is essentially static," whereas neural models improve with more data and GPUs — [Next-gen search, 2025-03-11](https://exa.ai/blog/how-to-build-nextgen-search)
- "The right interface to search is actually an LLM," because LLMs generate the long queries Exa is built to handle; variable query-time compute and rerankers on 10–1,000 candidates — [Latent Space, 2025-01-10](https://www.latent.space/p/exa)
- Exa returns full page content while many competitors return snippets; Exa says its lead persisted even when all engines were given Exa's content — [How we do evals at Exa, 2025-05-30](https://exa.ai/blog/evals-at-exa)
- Exa 3.0 attribution: bigger embedding model, Dynamic Highlights (95% fewer tokens), bigger index, and agents using "20% to 50% fewer search queries per task than other providers" (7.60 queries/task for Exa auto vs You.com 9.51, Parallel 9.59, DeepSeek 11.3, Perplexity 11.4, Brave 12.4, Firecrawl 15.4, citing AA data) — [Exa on AA ranking, 2026-10-19](https://exa.ai/blog/artificial-analysis-exa-3-best-search-api)
- Deep Max attribution: parallel tool calls fanning out across angles, token-efficient contents, and sub-second in-house search that "compounds across dozens of calls" — [Deep Max, 2026-04-20](https://exa.ai/blog/deep-max)
- Exa's benchmark critique: with the harness fixed, ATLAS scores vary 16% across search backends and Exa "defines the cost-performance Pareto frontier"; hiding the top 7 of 10 results halves the ATLAS score but leaves 81–89% of score on BrowseComp/WideSearch/DSQA, which Exa argues means those benchmarks barely measure search quality; closed-book memorization 48–61% for BrowseComp/WideSearch/DSQA vs 9% for ATLAS — [ATLAS, 2026-10-08](https://exa.ai/blog/atlas-benchmark); [Another search benchmark?, 2026-10-08](https://exa.ai/blog/another-search-benchmark)
- "How Search Quality Shapes RL Outcomes" (2026-05-13) argues better retrieval improves RL training of agents — [Exa blog](https://exa.ai/blog/rl-search-outcomes) (title only; not fetched)

**What independent/competitor evaluators credit**
- INDEPENDENT: Artificial Analysis Search Index (data as of 2026-10-19) ranks Exa Search (auto, dynamic highlights) first at 80 (BrowseComp 83, DSQA F1 86, AA-Omniscience 73), tied on the rounded index with Perplexity Search (medium) 80 (BrowseComp 87, DSQA 81, Omniscience 72); Exa lite 79 at $31.20 search cost per 1k tasks — [AA Search API leaderboard](https://artificialanalysis.ai/agents/search-api)
- COMPETITOR (Parallel) credits Exa with: "semantic discovery where vector ranking is the priority"; leading Parallel Fast on WideSearch (53.0 vs 45.5, low-cost tier); Exa fast scoring 99.3% on single-fact company news (vs Parallel Basic 93.3%); Exa deep leading multi-turn company search with page fetching (49.2 vs 43.8 F1); Exa Instant second-lowest factual-lookup latency (398ms vs Parallel Turbo 348ms) — [Parallel BrowseComp report, Sep 2026](https://parallel.ai/articles/most-powerful-search-api-for-ai); [Parallel vs Exa comparison, updated 2026-10-16](https://parallel.ai/compare/exa-vs-parallel)
- COMPETITOR (Tavily) frames Exa as "search-centered, with semantic discovery and similar-page search," strong for fast results and contents, with SOC 2 Type II and ZDR — [Tavily blog, 2026-04-27](https://tavily.com/blog/exa-vs-parallel-benchmarking-retrieval-apis-for-ai-agents-in-2026)
- Secondary: a16z interview summary says Cognition's Devin "makes fewer mistakes when powered by Exa" and retrieval can let smaller models perform like larger ones — [Summify summary](https://summify.io/discover/how-exa-is-building-the-perfect-search-engine-deep-dives-wit-k6OkMk) (unverified)
- Personal benchmark (MARB, multi-step coding/infra tasks) scored Exa 87.5 vs Parallel and Tavily 75.0; method not explained — [Agent Native newsletter](https://buttondown.com/agentnative/archive/we-scored-5-search-apis-for-ai-agents-2-were) (low-confidence)

**Known weaknesses**
- COMPETITOR (Parallel, Sep 2026 run, 50 BrowseComp questions): Exa Auto 70% at $971/1k questions vs Parallel Advanced 74% at $399 and Perplexity 74% at $275; Exa had the highest frontier-tier cost in the table — [Parallel report](https://parallel.ai/articles/most-powerful-search-api-for-ai)
- COMPETITOR (Parallel, Jul 2026): Exa Instant 33.7% BrowseComp vs Parallel Turbo 51%; SimpleQA Exa 89.3% vs Parallel Turbo 91%; Exa Instant measured 335–361ms p50 (client-side, us-central) vs advertised sub-200ms; AA fast-mode time per task Exa 22.6s vs Parallel 15.7s; AA cost per 1k tasks Exa auto $65.57 / Exa fast $78.11 vs Parallel fast $8.41; no documented EU data residency; list price raised $5 → $7 per 1k in March 2026 — [Parallel vs Exa](https://parallel.ai/compare/exa-vs-parallel)
- COMPETITOR (Perplexity's search_evals repo, 2026, agent-API comparison): Exa Agent API scored DSQA 0.53, BrowseComp 0.38, HLE 0.387, WideSearch 0.471 vs Perplexity Agent API 0.871/0.805/0.612/0.651 and Parallel Task API 0.81/0.56/0.515/0.584 — [perplexityai/search_evals](https://github.com/perplexityai/search_evals)
- VENDOR-admitted: "the scraper is not yet perfect," ranking is subjective, comprehensiveness is costly for broad queries — [Latent Space, 2025-01-10](https://www.latent.space/p/exa); crawlers get blocked, "the open web is becoming more closed" — [Next-gen search, 2025-03-11](https://exa.ai/blog/how-to-build-nextgen-search); [a16z summary](https://summify.io/discover/how-exa-is-building-the-perfect-search-engine-deep-dives-wit-k6OkMk)
- VENDOR docs on query style: "vague one-word queries like 'news' don't give enough intent"; put URL paths in `includeDomains` "rather than using `site:` in the query"; `lite` serves only cached content and drops results without a cached copy — [Evaluating Exa search](https://docs.exa.ai/reference/evaluating-exa-search)
- Exa's own eval post concedes LLM-judge evals are expensive, variable, prompt-dependent, and that manual review found problems the evals missed — [Evals at Exa, 2025-05-30](https://exa.ai/blog/evals-at-exa)
- Sacra characterizes Exa's index as "a curated subset of the web" — [Sacra, 2026-01-09](https://sacra.com/research/exa-at-10m-growing-11x-yoy)

### Inferences
- The two consistent independent/competitor findings are (a) Exa's per-call quality lets agents finish with fewer calls, and (b) Exa is expensive per call ($7/1k auto) and per task, so its cost-adjusted ranking depends heavily on whether the harness counts call volume. Parallel's harness (50 questions, cost-weighted) and Perplexity's repo (agent-vs-agent) show Exa trailing; AA's larger, model-fixed harness after Exa 3.0 shows it leading.
- Exa's shift to hybrid retrieval (BM25 + RRF, Apr 2026) plus Dynamic Highlights (Aug–Oct 2026) coincides with its AA index rising from 74 (Aug 2026, auto) to 80 (Oct 2026, auto + dynamic highlights), suggesting content packaging mattered as much as retrieval.

### Gaps
- No explicit source (vendor or independent) quantifying Exa's weakness on exact-match/keyword or operator-style queries; only indirect docs guidance.
- No independent measurement of index freshness.
- Hacker News discussion threads on Exa launches could not be retrieved (search budget exhausted).

## 4. Benchmarks: Exa-published numbers, Parallel's and Artificial Analysis' numbers, academic use

### Takeaway
Exa's own blog posts mostly show benchmark results as chart images with numbers absent from the text, except Exa 3.0 (BrowseComp 91.8%, DSQA 88.2%, WideSearch 56.1%, ATLAS 42.0%, WebCode 75.5%, FinSearchComp 68.0%) and Deep Max (DSQA 90%, FRAMES 94%, HLE-Search 80%). Independent Artificial Analysis data: Exa auto 74 / fast 68 at index launch (Aug 18, 2026); Exa auto (dynamic highlights) 80 (80.3 per Exa) and lite 79 as of Oct 19, 2026. Parallel's Sep 9, 2026 BrowseComp run (50 questions) put Exa Auto at 70% vs Parallel Advanced 74%. No peer-reviewed academic paper using Exa as a retriever was found.

### Cited Findings

**Exa-published (VENDOR), with harness details where available**
- 2025-01-24: SimpleQA and MSMARCO vs Bing, Perplexity (Sonar-Pro), GPT-4o no-web baseline; SimpleQA harness: gemini-1.5-flash generates the query, 4o-mini writes the answer; MSMARCO: 1,000 random queries graded by GPT-4o 1–5; Exa "tops the charts" but numbers only in images; Exa reported the higher of its own and the provider's public score — [api-evals](https://exa.ai/blog/api-evals)
- 2025-02-19 Websets vs Google: 200 o1-generated complex queries; Google ≈16 correct results/query (capped at 100); Websets low compute (100 requested) ≈66 (~4x); high compute (1,000 requested) ≈320 (~20x); OpenAI Deep Research higher precision but stopped after "a couple dozen"; author calls numbers "rough estimates" — [websets-evals](https://exa.ai/blog/websets-evals)
- 2025-05-30 Evals methodology: pointwise LLM grading (GPT-4.1) of top-5 results on ~5,000 real user queries, 10,000 MS MARCO queries, ~500 "Exa Olympiad" queries; SimpleQA via agent loop with OpenAI's grader prompt; grader agreed with humans 97% (easy) / 83% (hard) — [evals-at-exa](https://exa.ai/blog/evals-at-exa)
- 2025-10-10 Exa 2.0: SimpleQA and FRAMES named; harness GPT-4.1 as RAG model, GPT-4o-mini grader, matching Perplexity's public search_evals harness; "Exa Deep tops nearly every benchmark"; numbers only in charts — [Exa 2.0](https://exa.ai/blog/exa-api-2-0)
- 2025-11-24 Exa 2.1: "SingleStep" harness (query → top-10 results → GPT-5 mini answer → gpt-4o-mini grade, run 2025-11-23) and MCP agentic harness (GPT-5 with up to 10 MCP calls, run 2025-11-20); datasets and numbers not in text — [Exa 2.1](https://exa.ai/blog/exa-api-2-1)
- 2025-12-17 People Search benchmark; 2026-01-22 Company Search benchmarks; 2026-03-23 WebCode (coding-agent search evals) — [people-search-benchmark](https://exa.ai/blog/people-search-benchmark); [company-search-benchmarks](https://exa.ai/blog/company-search-benchmarks); [webcode](https://exa.ai/blog/webcode)
- 2026-03-04 Exa Deep: HLE-Search, DSQA, FRAMES vs Perplexity Sonar Reasoning Pro and Parallel Task (Core, Base); "up and to the left" claim; numbers only in charts — [exa-deep](https://exa.ai/blog/exa-deep)
- 2026-04-20 Deep Max: DSQA 90% in 64s (You Frontier 84% / 5908s; Parallel Ultra 8x 82% / 1703s); FRAMES 94% / 11s (Parallel Ultra 88% / 1457s); HLE-Search 80% / 25s ("GPT 5.4 matches on quality at about twice the latency"); harness not stated — [deep-max](https://exa.ai/blog/deep-max)
- 2026-07-23 Publications search: Exa retrieved the correct paper for 82.8% of queries — [publications-search](https://exa.ai/blog/publications-search)
- 2026-10-08 ATLAS: 547 tasks, 23 categories, generated by frontier agents (Codex/GPT-6 Astra, Claude Code/Opus 5.5), audited <1% gold error; headline metric row F1; best system 0.66 row F1 at $8.92 and 18 min/task; no run under $1/task exceeded 0.5; 12 systems incl. Exa Agent (4 effort levels), Opus 5.5 and GPT-6 Astra with native search, and GPT-5.6 Luna with Exa/Perplexity/Brave/Parallel in the "Scout" harness; per-provider numbers only in charts — [atlas-benchmark](https://exa.ai/blog/atlas-benchmark)
- 2026-10-19 Exa 3.0 scores: BrowseComp 91.8%, DSQA 88.2%, WideSearch 56.1%, ATLAS 42.0%, WebCode 75.5%, FinSearchComp 68.0%, Company FindAll 15.4, People FindAll 7.6; "leads Perplexity, Brave, and Parallel on all eight"; competitor numbers and harness not in text — [Exa 3.0](https://exa.ai/blog/exa-3)
- exa-labs/benchmarks repo (12 suites; Scout harness default model `openai/gpt-6-luna` for agent and judge; `gpt-5.6-luna` for RAG; 95% bootstrap CIs): WebCode Highlights groundedness Exa 94.8 vs Parallel 85.6 vs Claude 81.5; WebCode RAG groundedness Exa 79.4, Brave 76.3, Parallel 75.3, Perplexity 64.6; People Search R@1 Exa 89.5% vs Brave 44.4% vs Parallel 20.8%; Company retrieval R@1 Exa 61.8% vs Brave 35.9% vs Parallel 36.6%; Company RAG accuracy Exa 79% / Parallel 66% / Brave 65%; Publication tip-of-tongue recall Exa 86.4% (0.578s) vs Perplexity 66.8% (1.277s) vs Parallel Advanced 50.0% (3.118s); README labels these "historical measurements" without dates — [github.com/exa-labs/benchmarks](https://github.com/exa-labs/benchmarks)

**Artificial Analysis (INDEPENDENT)**
- Methodology: Search Index = equal-weighted mean of DeepSearchQA (900 tasks, LLM-graded F1), AA-Omniscience (600 private samples, accuracy), BrowseComp (200-sample subset of 1,266, exact-answer accuracy); Stirrup harness with `web_search` + `web_fetch`; candidate model GPT-5.6 Luna (medium), same model grades; 25-turn budget; 10 results per search; Exa configured as `type=lite` and `type=auto`, both with dynamic highlights; fatal errors retried; contamination filtering — [AA methodology](https://artificialanalysis.ai/methodology/search-api)
- Launch (2026-08-18): Parallel Search (advanced) 75; Exa Search (auto) 74; Firecrawl 73; Parallel basic 73; Exa Search (fast) 68; You.com 68; Parallel turbo 67; Keenable pro/realtime 67; Tavily basic 66; Brave 65; model-only baseline 33; Perplexity absent at launch — [AA launch article, 2026-08-18](https://artificialanalysis.ai/articles/search-api). (Column alignment in the extracted launch table was ambiguous; Parallel's page gives the component breakdown as DSQA Parallel 81 vs Exa 78, BrowseComp Parallel 77 vs Exa 74, Omniscience Exa 70 vs Parallel 67 — [Parallel vs Exa](https://parallel.ai/compare/exa-vs-parallel).)
- Sep/Oct 2026 (pre-Exa 3.0): Perplexity Search (medium) led at 80; Octen 77; Parallel advanced 75; Brave LLM context 75; Exa auto 74 — [Parallel, 2026-10-11](https://parallel.ai/articles/exa-alternatives) (COMPETITOR citing AA); [Crypto Briefing](https://cryptobriefing.com/perplexity-tops-artificial-analysis-search-index/)
- Latest leaderboard (data 2026-10-19): Exa auto (dynamic highlights) 80 — DSQA 86, BrowseComp 83, Omniscience 73, search cost $53.17/1k tasks, model cost $10.60, 36.9s/task; Perplexity medium 80 (81/87/72, $62.30, 31.4s); Exa lite (dynamic highlights) 79 (85/81/72, $31.20, 19.6s); Perplexity high 79; Octen 77 ($9.07); Parallel advanced 75 ($47.93, 40.0s); Brave LLM context 75 ($61.96); OpenAI Web Search medium 74 ($40.19); You.com 74; Nimble 74; Firecrawl 73 ($30.48, 61.9s); DeepSeek 69 ($8.47); model-only 33 — [AA Search API leaderboard](https://artificialanalysis.ai/agents/search-api)
- Exa reports the unrounded figures as 80.3 (auto) and 79.2 (lite) and claims "#1" — [Exa, 2026-10-19](https://exa.ai/blog/artificial-analysis-exa-3-best-search-api) (VENDOR interpretation of INDEPENDENT data; the rounded leaderboard shows a tie with Perplexity medium at 80)

**Parallel (COMPETITOR)**
- Sep 9, 2026 BrowseComp run, 50-question sample, LLM judge; frontier tier (GPT-5.6 Sol, reasoning high): Parallel Advanced 74% ($399/1k questions), Perplexity 74% ($275), Parallel Basic 72% ($612), Exa Auto 70% ($971), Tavily 66% ($935); low-cost tier (GPT-5.6 Luna, low): Perplexity 46% ($37.1), Parallel Fast 44% ($11.8), Exa Auto 36% ($53.4), Parallel Turbo 32% ($13.2), Tavily 32% ($176); Perplexity had search only, others search + extract — [Parallel report](https://parallel.ai/articles/most-powerful-search-api-for-ai)
- Jul 2026 run: BrowseComp Parallel Turbo 51% vs Exa Instant 33.7%; SimpleQA Parallel Turbo 91% vs Exa 89.3% — [Parallel vs Exa](https://parallel.ai/compare/exa-vs-parallel)
- Parallel's benchmark page as relayed by Tavily (Apr 2026; Exa mode unspecified; "CPM" = cost per 1k requests incl. LLM tokens): FRAMES Exa 87% (CPM 169) vs Parallel Advanced 87% (93); WebWalker 74% vs 73%; BrowseComp 40% (1,160) vs 51% (379); HLE 57% vs 56%; FreshQA 78% vs 79%; SealQA 41% vs 41% — [Tavily blog, 2026-04-27](https://tavily.com/blog/exa-vs-parallel-benchmarking-retrieval-apis-for-ai-agents-in-2026)
- Openbenchmarks (Sep 2026, cited by Parallel): factual-lookup mean latency Parallel Turbo 348ms, Exa Instant 398ms, Brave 601–630ms, Tavily basic 1.88s — [Parallel report](https://parallel.ai/articles/most-powerful-search-api-for-ai)

**Perplexity (COMPETITOR)**
- search_evals repo compares agent APIs (Perplexity Agent API, OpenAI Responses, Anthropic Managed Agents, Exa Agent API, Parallel Task API): Exa 0.53 DSQA / 0.38 BrowseComp / 0.387 HLE / 0.471 WideSearch; no run dates — [perplexityai/search_evals](https://github.com/perplexityai/search_evals)

**Academic use**
- Search for arXiv papers using Exa as a retriever returned none; results were vendor blogs, GitHub repos, and a personal benchmark — [search result summary]; ATLAS dataset is gated on Hugging Face via [exa-labs/benchmarks](https://github.com/exa-labs/benchmarks)

### Inferences
- Exa's published numbers are strongest where Exa also wrote the benchmark (People/Company Search, WebCode, ATLAS, publications), while on third-party-designed BrowseComp Exa's standing varies from 70% (Parallel's 50-question Sol harness) to 83 (AA 200-question Luna harness) to 91.8% (Exa's own Exa 3.0 post, harness unstated). The spread is mostly harness/model differences, not retrieval alone.
- The task brief's reference figures check out: "BrowseComp 70% in Parallel's September 2026 run" (Exa Auto, frontier tier) and "Exa 74 on the Artificial Analysis Search Index" (Exa auto, Aug–early Oct 2026, before Exa 3.0 raised it to 80).

### Gaps
- Exa's own SimpleQA/FRAMES percentages for Exa 2.0/2.1 are only in chart images and could not be read; Exa 3.0's post omits SimpleQA and FRAMES.
- No per-provider numbers from Exa's ATLAS post (charts only).
- No peer-reviewed paper found that uses Exa as a retriever (search budget exhausted before deeper arXiv checks).

## 5. Pricing, free credits, rate limits, latency

### Takeaway
As of Nov 2026 Exa is pay-as-you-go: Lite $4/1k, Auto $7/1k (raised from $5 in Mar 2026), deep-lite/deep $12/1k, deep-reasoning (legacy) $15/1k, contents $1/1k pages per content type (first 10 results' contents free since Mar 2026), Answer $5/1k, Monitors $2/1k, Agent $0.012–$1.00 per fixed-effort run; $10 free credits at signup resetting monthly; default 10 QPS on search (5 QPS on deep, 100 QPS contents), rising to 25 QPS after $1,000 of credits in 30 days.

### Cited Findings
- Pricing page (Nov 2026): Search from $4/1k; Deep Search $12–15/1k; Contents $1/1k pages; Answer $5/1k; Monitors $2/1k; Agent $0.012–$1.00 per fixed-effort run or usage-based; `/search` lite $4/1k (≤10 results), instant (legacy) $4/1k, auto and fast (legacy) $7/1k; each result above 10 $1/1k results; AI page summaries $1/1k pages; `/contents` $1/1k pages per content type (text, highlights, summary billed separately); deep-lite $12/1k (~4s), deep $12/1k (4–15s), deep-reasoning (legacy) $15/1k (12–40s); Agent effort minimal $0.012, low $0.025, medium $0.10, high $0.50, xhigh $1.00; metered `auto` ($5 cap/run) and `ultra` ($20 cap): ACU $0.10, search tool call $0.005, email enrichment $0.02, phone $0.07; Connect providers extra (Fiber.ai $0.02/credit, Baselayer $0.10–$4.00/order); free tier $10 credits at signup (≈2,500 Lite searches), resetting to $10 monthly, no card required, one-time $10 team onboarding bonus; Enterprise: up to 1,000 results/search, custom QPS, custom indexes, SLAs, ZDR, volume discounts, invoicing — [exa.ai/pricing](https://exa.ai/pricing)
- Pricing history: Mar 3, 2026 update made contents free for the first 10 results and lowered Deep pricing — [changelog](https://docs.exa.ai/changelog); Sacra (Jan 2026) quoted $5/1k searches, $15/1k deep research, $5/1k answers — [Sacra](https://sacra.com/research/exa-at-10m-growing-11x-yoy); Parallel says search list price rose from $5 to $7 per 1k in March 2026 and quotes Exa's free tier as "$20 at signup, plus $10/month" (conflicts with the $10 on Exa's current page) and Monitors at $15/1k (conflicts with $2/1k on Exa's current page; Monitors v2 shipped 2026-10-29) — [Parallel vs Exa, updated 2026-10-16](https://parallel.ai/compare/exa-vs-parallel); [Tavily, 2026-04-27](https://tavily.com/blog/exa-vs-parallel-benchmarking-retrieval-apis-for-ai-agents-in-2026)
- Websets plans: free 1,000 credits; $49/month 8,000 credits; $449/month 100,000 credits — [Websets FAQ](https://exa.ai/docs/websets/faq.md)
- Rate limits (per team, shared across keys): `/search`, `/answer`, `/chat/completions` 10 QPS; deep types 5 QPS; `/contents` 100 QPS; `/agent/runs` 5 QPS and 50 active runs; `/websets/*` 20 QPS; PAYG rises to 25 QPS for 90 days after adding $1,000 credits within 30 days; >25 QPS via sales — [Exa rate limits](https://docs.exa.ai/reference/rate-limits)
- Latency (VENDOR): Fast p50 < 425ms (Jul 2025) → < 350ms P50 from us-west-2 (Oct 2025) → "sub 500ms" (Nov 2025); Deep 3.5s P50 (Oct 2025); Instant "sub-200ms" (Feb 2026); Series B "sub 450ms", Series C "sub-200ms"; current docs: lite ~450ms, auto ~1s, deep-lite ~4s, deep 4–15s, deep-reasoning 12–40s, "approximate and assume cached content" — [changelog](https://docs.exa.ai/changelog); [Exa 2.0](https://exa.ai/blog/exa-api-2-0); [Exa 2.1](https://exa.ai/blog/exa-api-2-1); [Exa Instant](https://exa.ai/blog/exa-instant); [Series C](https://exa.ai/blog/announcing-series-c); [Evaluating Exa search](https://docs.exa.ai/reference/evaluating-exa-search); [pricing](https://exa.ai/pricing)
- Latency (COMPETITOR measurement): Exa Instant 335–361ms p50 client-side from us-central vs advertised sub-200ms — [Parallel vs Exa](https://parallel.ai/compare/exa-vs-parallel); Exa Instant 398ms mean on factual lookup (Openbenchmarks) — [Parallel report](https://parallel.ai/articles/most-powerful-search-api-for-ai)
- Latency (INDEPENDENT, whole-task): AA time per task Exa auto 36.9s, Exa lite 19.6s vs Perplexity medium 31.4s, Parallel advanced 40.0s — [AA leaderboard](https://artificialanalysis.ai/agents/search-api)
- Zero Data Retention across search products (2025-08-18); HIPAA compliance mode on lite; SOC 2 Type II (per Tavily) — [ZDR post](https://exa.ai/blog/zdr-search-engine); [Exa docs](https://docs.exa.ai/reference/how-exa-search-works); [Tavily](https://tavily.com/blog/exa-vs-parallel-benchmarking-retrieval-apis-for-ai-agents-in-2026)

### Inferences
- Exa's $7/1k Auto is 7x Parallel's $1/1k Turbo list price; Exa's counterargument (fewer queries per task) narrows but does not close the gap in AA's cost-per-task data ($53.17 vs Parallel advanced $47.93, though Parallel advanced is a $5/1k tier).

### Gaps
- Exa publishes no p95/p99 latency and no uptime SLA figures publicly (SLAs are enterprise-only).
- Livecrawl pricing is not itemized; `maxAgeHours: 0` fetches are described as adding latency but not as a separate charge.

## 6. Integrations: MCP, SDKs, Claude/Cursor/Windsurf, OpenAI-compatible endpoints, frameworks

### Takeaway
Exa ships a hosted MCP server (https://mcp.exa.ai/mcp, free anonymous tier, OAuth) and an MIT-licensed open-source server (exa-labs/exa-mcp-server, ~5.2k stars) with install paths for Claude (official plugin and connector), Cursor, VS Code, Windsurf, Codex/ChatGPT; official Python (exa-py) and JavaScript (exa-js) SDKs; OpenAI SDK compatibility (chat completions and responses); and documented tools for LangChain, LlamaIndex, CrewAI, AG2, Pydantic AI, Vercel AI SDK, OpenRouter, Fireworks, Baseten; plus Google's "Grounding with Exa" (Apr 2026) and Firefox search (Aug 2026).

### Cited Findings
- exa-mcp-server: default tools `web_search_exa`, `web_fetch_exa`; optional `agent_run` and `web_search_advanced_exa` (filters, dates, highlights, summaries, subpage crawling); hosted endpoint `https://mcp.exa.ai/mcp` works anonymously with rate limits, OAuth or API key for higher limits; Claude install `claude plugin install exa@claude-plugins-official`; one-click Cursor and VS Code badges; Windsurf via `~/.codeium/windsurf/mcp_config.json`; Codex `codex mcp add exa --url https://mcp.exa.ai/mcp`; npm `exa-mcp-server`; MIT; 5.2k stars, 409 forks, 448 commits — [github.com/exa-labs/exa-mcp-server](https://github.com/exa-labs/exa-mcp-server)
- Free unauthenticated MCP tier added 2026-02-02; `agent_run` added to MCP 2026-07-01 — [changelog](https://docs.exa.ai/changelog)
- Claude: plugin "Exa" in `claude-plugins-official`; connector "Exa" in Claude web/desktop/Cowork connector directory; manual `claude mcp add --transport http exa https://mcp.exa.ai/mcp`; capabilities Search, Read, Research; Enterprise Managed Auth for Claude documented — [Exa docs: Claude](https://exa.ai/docs/integrations/claude-web-desktop.md); [docs index](https://docs.exa.ai/llms.txt)
- SDKs: Python `exa-py`, JavaScript `exa-js`; JS SDK v2.0.11 restored highlights (2025-11-26) — [docs index](https://docs.exa.ai/llms.txt); [changelog](https://docs.exa.ai/changelog)
- OpenAI SDK compatibility (chat completions and responses), OpenAI and Anthropic tool-calling guides, Fireworks, OpenRouter, Baseten; frameworks LangChain, LlamaIndex, CrewAI, AG2, Pydantic AI; Vercel AI SDK / AI Gateway; n8n, Gumloop, Google Sheets, Snowflake, Browserbase, ElevenLabs; payments via Stripe Projects, x402, Tempo MPP, Nevermined; integrations for Codex/ChatGPT, Grok Build, Slack, Hermes Agent, OpenClaw — [docs.exa.ai/llms.txt](https://docs.exa.ai/llms.txt)
- Parallel credits Exa with "LangChain, LlamaIndex, CrewAI, Vercel AI SDK, and 25+ others" — [Parallel vs Exa](https://parallel.ai/compare/exa-vs-parallel)
- Google: "Grounding with Exa" in Private Preview on the Gemini Enterprise Agent Platform (Exa pulls fresh results at request time; Highlights model trims pages before Gemini); Exa Agent launch partner on Gemini Enterprise Agent Marketplace — [Exa and Google, 2026-04-28](https://exa.ai/blog/exa-google-cloud)
- Firefox: "Exa is now powering search in Firefox" (2026-08-17) — [exa.ai/blog/exa-firefox](https://exa.ai/blog/exa-firefox) (title only; not fetched)
- exa-code MCP tool for coding agents, free, triggered by "use exa-code" — [exa-code, 2025-09-25](https://exa.ai/blog/exa-code)
- Cursor as customer: named in Series B and Series C posts; Sacra names Cursor, Vercel v0, Lovable for code/docs retrieval — [Series B](https://exa.ai/blog/announcing-series-b); [Series C](https://exa.ai/blog/announcing-series-c); [Sacra](https://sacra.com/research/exa-at-10m-growing-11x-yoy)
- Parallel's MCP comparison (Aug 28, 2026) exists — [parallel.ai](https://parallel.ai/articles/parallel-search-mcp-vs-exa-mcp) (not fetched)

### Inferences
- Cursor's `@web` has been reported by third parties as Exa-powered, but I only have Exa naming Cursor as a customer; the exact Cursor feature is not confirmed by a primary source.

### Gaps
- No Windsurf-specific docs page from Exa (only the README's manual config).
- Did not verify the Firefox integration details.

## 7. Relationship to Common Crawl

### Takeaway
No source found — vendor, press, or third-party — states that Exa seeded or trains on Common Crawl; every primary description says Exa runs its own URL discovery, crawler (ExaSearchBot), parser, and storage. The indexes differ fundamentally in representation: Exa stores parsed text plus learned embeddings (and ~400B historical page snapshots) served through a vector/BM25 hybrid, whereas Common Crawl publishes raw WARC archives (specifics on Common Crawl's cadence and size are left as a gap because no Common Crawl source was fetched in this run).

### Cited Findings
- Exa describes its own crawl end to end: "continuously finds new URLs and crawls them across a distributed network of machines and IPs," custom HTML parser, S3 storage — [Next-gen search, 2025-03-11](https://exa.ai/blog/how-to-build-nextgen-search)
- Crawler identity `ExaSearchBot` with robots.txt controls at crawler.exa.ai; FAQ does not mention Common Crawl or third-party data — [Exa FAQ](https://exa.ai/docs/admin/faqs.md)
- "Exa operates its own web crawling infrastructure separate from any third-party search index" — [MorphLLM profile](https://www.morphllm.com/exa-search-api) (secondary)
- The Latent Space interview and wiki, Exa's vector-DB, exa-d, and Exacluster posts, TechCrunch, and the Cerebral Valley profile do not mention Common Crawl — [Latent Space](https://www.latent.space/p/exa); [Latent Space wiki](https://latent.space/wiki/exa-f75ed103/); [exa-d](https://exa.ai/blog/exa-d); [TechCrunch](https://techcrunch.com/2024/07/16/exa-raises-17m-lightspeed-nvidia-ycombinator-google-ai-models/); [Cerebral Valley](https://cerebralvalley.beehiiv.com/p/exa-prev-metaphor-aims-reshape-web-search)
- Scale/representation on Exa's side: 2T URLs tracked, 100B pages served (Oct 2026); 400B snapshots over ~20 years; Lance-format columnar storage with embeddings; continuous refresh — [FAQ](https://exa.ai/docs/admin/faqs.md); [Snapshot](https://exa.ai/blog/exa-snapshot); [exa-d](https://exa.ai/blog/exa-d)
- Training data for the link-prediction model is "links people share on the web" — [TechCrunch](https://techcrunch.com/2024/07/16/exa-raises-17m-lightspeed-nvidia-ycombinator-google-ai-models/); whether the 2021–2022 corpus came from Common Crawl is not stated anywhere I found.

### Inferences
- Given Exa bought an 80-A100 cluster with half its 2021 seed and launched a web-scale engine by Nov 2022 with ~7 people, it is plausible (but unsourced) that early Metaphor used a public corpus such as Common Crawl for bootstrapping. Treat as speculation.
- Representation difference (from Exa's own descriptions): Exa's unit of storage is a parsed, embedded document with metadata and multiple time-versions, queryable semantically in <1s; Common Crawl's unit is a raw archived HTTP response. Exa's "400B snapshots over 20 years" claim suggests it ingests historical web archives of some kind, but the source is unnamed.

### Gaps
- No statement from Exa or Bryk about Common Crawl (positive or negative). Web search budget ran out before targeted queries ("Exa" + "Common Crawl") could be run; the one attempt returned no match.
- No Common Crawl figures were fetched in this run, so the scale/freshness comparison cannot be quantified here with citations.
