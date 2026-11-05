# Open source stack for search APIs

**Scope and status.** This is the coordinator's digest of five verified research notes in
`research_notes/Open source stack for search APIs/` (crawling and extraction; indexing and retrieval; ranking,
reranking and snippets; serving, infrastructure and the agent interface; evidence from job postings and
repositories). The session budget ran out before the full writer pass, so this document is shorter than the two
earlier reports and points into the notes for detail. Every figure below is in those notes with a source URL;
the skeptic pass over the notes' top claims returned 12 confirmed, 3 corrected on detail, 1 unverifiable
(the Brave and Tailcat acquisition wording), 0 refuted. Date: 2026-11-05. Labels: [vendor], [job posting],
[repo], [talk], [independent], [inferred].

**Bottom line.** Only four providers disclose anything checkable about their machinery: Exa (the most, across
four engineering posts), Perplexity (Vespa, then an in-house Rust/C++ "Search Core"; Triton and TensorRT-LLM
inference), Keenable (a Rust-first team and a token-classifier for snippets) and Brave (its Cliqz/Tailcat lineage).
Everyone else publishes bot names and SDKs only. What the disclosures and 300-odd job postings agree on is a
stack a practitioner can learn almost entirely from open source: Python plus Rust (C++ for inner loops), a
Lucene-style inverted index (tantivy, Vespa, PISA) fused with quantized ANN (FAISS, usearch, Lance), gradient-boosted
and cross-encoder rerankers, Spark or Ray pipelines over Parquet and Lance on object storage, Playwright for
rendering, trafilatura for extraction, vLLM or TEI for inference, Kubernetes and Terraform, and TypeScript for the
MCP surface. The two things open source does not give you are a fresh index above a few billion pages and
anti-bot rendering capacity at crawl scale; that is where the vendors' capital goes.

## The layered map

| Layer and component | What the providers disclose | Open-source equivalents | What to learn |
|---|---|---|---|
| Crawler | No vendor open-sources one. Bot identities: ExaSearchBot/1.0 and ExaUser signed per RFC 9421 [vendor, crawler.exa.ai, 2026-11-02]; Parallel ShapBot/0.1.0 (RFC 9421); PerplexityBot and Perplexity-User (the latter ignores robots.txt by design) [vendor]; KeenableBot and Keenable-User (RFC 9309, IP lists October 2026) [vendor]; CCBot/2.0. Exa's job ads ask for "a distributed crawler that can handle 100M+ pages per day" [job posting]; Keenable's ad specifies "a polite, scalable crawler dispatch queue with per-domain scheduling, robots.txt compliance" [job posting]; Linkup names StormCrawler [job posting] | Common Crawl's Apache Nutch fork (Apache-2.0; WARC and CDX writing in the fetcher, CLD2 language ID, Generator2 per-domain and per-host budgets); StormCrawler (Java, Apache-2.0); Marginalia's Java crawler (AGPL, about 5-day full crawls); Stract's Rust crawler (AGPL, archived 2026-04-02); Mwmbl (Python and Rust, volunteer crawl); crawler-commons, google/robotstxt, protego for robots parsing | The Nutch inject, generate, fetch, parse, update loop; per-domain politeness and URL frontiers; harmonic centrality for host selection (Common Crawl's choice over PageRank); two agents (index crawler versus user fetcher) with a max-age policy |
| Rendering and anti-bot | Exa asks for "TypeScript, Playwright, CDP" and "anti-bot measures"; Tavily patches and builds its own Chromium ("Blink, the V8 integration, the compositor", "TLS fingerprints (JA3/JA4)"); Firecrawl asks for "CDP, Playwright, Puppeteer", "fingerprinting", "proxies" [job postings] | Playwright and Puppeteer (Apache-2.0); Lightpanda (Zig, AGPL; vendor claims 16x less memory and 9x speed than Chrome, unverified); curl-impersonate for the lightweight path; Jina Reader's `auto` engine selection (Apache-2.0: Puppeteer plus curl-impersonate, PDF.js) | Chrome DevTools Protocol; when to render and when not to; TLS fingerprint hygiene |
| Parsing and extraction | Exa: custom HTML parser [vendor]; Keenable and Exa ship query-conditioned snippet models (next layer) | trafilatura (F 0.926 on the 2026-10-02 benchmark of 990 documents), jusText 0.862, readability-lxml 0.853, Resiliparse 0.811 at 0.3x the time [independent benchmark by trafilatura's author]; Crawl4AI (Apache-2.0, Playwright, BM25 content filter); Firecrawl core (AGPL, 198.7k stars) | Main-content extraction trade-offs (quality versus throughput); HTML to markdown for LLMs |
| Dedup, language, quality | Not disclosed by any vendor; Exa's "Index Intelligence" ad: "Something has to decide which pages are worth indexing, which links are worth following" [job posting] | datatrove (MinHash, fastText, Gopher and C4 filters, FineWeb-Edu classifier F1 0.82); DCLM's Resiliparse plus BFF plus fastText pipeline on Ray; CLD2 and fastText for language ID | Reproduce FineWeb on one Common Crawl snapshot |
| Storage and pipelines | Exa: corpus in Lance on S3 with a global manifest; `exa-d` turns a column graph into Ray Data jobs with embedding models resident in GPU memory [vendor, 2026-01-13]; Exa 2026 ads add Spark over Delta, Iceberg or Hudi at 100k documents a second [job posting]; Perplexity: Databricks, Snowflake, Kafka, Airflow [job postings]; Linkup: Spark, Delta Lake, NATS [job posting] | Lance and LanceDB (Rust, Apache-2.0), Parquet and Arrow, Ray Data, Apache Spark, cc-pyspark against `s3://commoncrawl`, Kafka or NATS | A lakehouse on object storage; batch GPU embedding; reading Spark query plans |
| Lexical index | Exa: a Rust BM25 index at 1.8 TB per 1B documents before a May 2025 encoding change (d-gaps and varints, TF bitmaps, zstd) cut it by more than half with WAND-style pruning [vendor, 2025-05-05]; Perplexity: Vespa, then "a purpose-built internal search system" (Belgrade "Search Core", Rust and C++) [Vespa case study, job postings]; Parallel: "its own large-scale full-text index" [job posting]; Brave: Cliqz 2019 design of query-n-gram "page models" in Keyvi, RocksDB and Cassandra, not a classic inverted index [blog, lineage unverified] | tantivy (Rust, MIT, 16k stars), Lucene and Elasticsearch or OpenSearch (ChatNoir: 124 nodes, 9.7 TB BM25 for 1.6B pages, 2018), Vespa (Java and C++, Apache-2.0), PISA (C++, compression research), Anserini and Pyserini (reproducible BM25 baselines), CIFF to move indexes between engines, Quickwit, Meilisearch | Segments, postings compression, BM25 and BM25F, WAND and MaxScore; sharding and Raft (Stract's openraft) |
| Dense retrieval | Exa: embeddings trained on link prediction, 4096-d Matryoshka vectors truncated to 256-d, 1-bit binary quantization, 100,000 IVF clusters, register-resident lookup tables, full-precision rerank, under 100 ms over billions of vectors [vendor, 2024-12-17]; Linkup: "HNSW and ANNs are second nature", "1B embeddings a day" [job posting]; Cliqz lineage: 200-d vectors in Granne | FAISS (MIT, 41k stars), usearch, hnswlib, DiskANN, ScaNN, Qdrant, Milvus, Vespa, pgvector; embedding models BGE-M3 (MIT), Qwen3-Embedding (Apache-2.0), E5, GTE, Nomic, Arctic-embed, ModernBERT-based; FlagEmbedding for training; SPLADE for learned sparse; ColBERT, PLAID and PyLate for late interaction | IVF plus product or binary quantization with filters; contrastive training in PyTorch (FSDP); MTEB evaluation |
| Fusion | Exa: dense and sparse fused by reciprocal rank fusion with k=60, then rerankers, about 250 ms per query [vendor, 2026-04-17]; Perplexity: "hybrid lexical and semantic retrieval" with sub-document spans [vendor, 2025-09-25] | RRF in Vespa, Elasticsearch and OpenSearch; a few lines in any language | Why RRF beats score mixing without calibration |
| Ranking and reranking | Exa: a query classifier and freshness model, then "relevance" and "authority" rerankers and an authority-weighted final ranking [vendor]; Perplexity: cross-encoders at document and sub-document level [vendor]; Parallel: "multi-stage ranking pipeline" [job posting]; Linkup: "auto-retrain ranking on agent clicks every 24 h" [job posting]; Keenable: nothing on ranking (the Yandex MatrixNet and CatBoost heritage is biography, not evidence); Jina: the only inspectable reranker (jina-reranker-v3, 0.6B, 64-document listwise, self-reported BEIR 61.94, CC-BY-NC) | LightGBM and XGBoost LambdaMART, CatBoost YetiRank (all Apache-2.0 or MIT, committed within the week); cross-encoders Qwen3-Reranker 0.6B, 4B and 8B (Apache-2.0; publisher MTEB-R 65.80, 69.76, 69.02 against bge-reranker-v2-m3 57.03), mxbai-rerank-v2 (BEIR 57.49, 0.89 s on an A100, vendor), bge-reranker-v2-m3 (14.3M downloads, 512-token limit), gte-reranker-modernbert; listwise LLM reranking with rank_llm, RankZephyr, RankGPT, FIRST; Stract is the one open engine shipping BM25F plus LambdaMART plus a cross-encoder in one codebase | Query-grouped features (BM25F per field, host and URL features, centrality, age, clicks or agent trajectories); yes/no-token scoring; distilling a listwise teacher into a small model |
| Link analysis and spam | Common Crawl ranks hosts by harmonic centrality (chosen for spam resistance); vendors disclose nothing | cc-webgraph and the WebGraph framework; TrustRank-style seed propagation; quality classifiers as features | PageRank versus harmonic centrality on the Common Crawl host graph |
| Query understanding | Exa: query classifier and freshness model [vendor]; Tavily's ads: "query understanding, query reformulation and expansion" [job posting]; the reader's own `detect-v1` and `rephrase-v3` prompts are working examples | SymSpell and symspellpy; small intent, language and time-sensitivity classifiers; LLM rewriting with explicit strategies | Spelling, intent and freshness detection before retrieval |
| Snippets and context shaping | Keenable Dynamic Snippets: a query-conditioned token classifier over overlapping chunks, thresholds max(0.6m, 0.5) and 0.75m, runs under 80 characters merged, trained on agent trajectories; responses 49% smaller, vendor BrowseComp 56.6% to 67.3% [vendor, 2026-10-15]; Exa Dynamic Highlights (95% fewer tokens claimed); Brave LLM Context smart chunks with a token budget, p90 under 500 ms claimed | LLMLingua-2 style token classifiers (MIT), Provence (non-commercial), ColBERT token scores, sentence-transformers passage ranking, Crawl4AI's BM25 content filter | A token classifier plus a global token allocator across results |
| Serving and inference | Exa: C++ hot path and Rust serving, 80 A100s plus 144 H200s (about $5M) [vendor]; Perplexity: Triton and TensorRT-LLM with proprietary CUDA runtimes on H100 pods in Kubernetes, 20+ models, about 435M queries a month, tensor parallelism across 4 to 8 GPUs [NVIDIA case study, 2024-12-05]; Perplexity ads: "Our stack is Rust, Python, CUDA, and CuTe DSL", a "Rust-native serving runtime" [job posting]; Keenable: Rust CLI, zero-latency classifier [vendor]; every sub-500 ms latency claim is vendor-measured | vLLM, SGLang, TensorRT-LLM, Triton Inference Server, text-embeddings-inference, ONNX Runtime; pplx-garden (Perplexity's Rust inference libraries, MIT) | Percentile discipline (p50 and p95 from a stated region, randomized queries against caches); cost per million queries |
| Agent interface | Hosted Streamable-HTTP MCP plus OAuth plus a keyless tier is universal except Brave (local only); Keenable alone prices x402 micropayments at $0.01 per call; SKILL.md files and CLIs from Keenable, Firecrawl, Brave, Parallel, Tavily | Official MCP SDKs (TypeScript, Python, C#, Go, Rust, Ruby), FastMCP; the 2025-06-18 MCP spec (servers as OAuth resource servers, RFC 8707, structured tool output); SearXNG, Perplexica, Morphic, Open WebUI, Khoj as open front-ends; self-hosted Firecrawl (Postgres, Redis, Playwright) for fetch | `search` plus `fetch` tools with age and freshness parameters; OAuth resource-server metadata |
| Evaluation | Perplexity search_evals, Keenable NEEDLE, Tavily evals, Exa benchmarks (all Python, MIT); Firecrawl hires for "when to trust an LLM judge" [job posting] | BEIR, MTEB, ir_measures, ranx, pytrec_eval, ir_datasets, Pyserini and PyTerrier baselines, BrowseComp-Plus with a pluggable retriever | nDCG, MRR and recall at k; auditing an LLM judge against human labels before trusting deltas |

## The stack to know, ordered by how often the vendors ask for it

Counted across nine live job boards fetched 2026-11-05 (Exa 63 postings, Perplexity 139, Parallel 33, Tavily 34,
Firecrawl 29, Linkup 14, Brave 10, Keenable 5) and about 85 public repositories. Brave, Kagi, Mojeek, You.com,
Jina, Octen and Ceramic are under-represented because their boards were unreachable or empty.

1. **Python plus one systems language, Rust first, C++ second.** Rust is named by Exa, Perplexity, Keenable
   ("a Rust-first engineering team"), Linkup, Tavily and Brave; C++ by Exa (vector-database hot path), Perplexity
   (CUDA kernels, Search Core), Tavily (Chromium, Blink, V8) and Brave; Go by five companies for services. Learn with
   tantivy, then Stract's crawler and indexer; port one PISA algorithm to Rust.
2. **Kubernetes and Terraform on AWS or GCP**, with stateful workloads (search shards, crawl fleets, queues). Named
   by Perplexity ("primarily on AWS"), Tavily, Firecrawl, Linkup, Parallel.
3. **Spark over a lakehouse (Parquet, Delta, Iceberg) on object storage, then Lance and Ray Data.** Named by Exa,
   Linkup, Perplexity, Tavily. Start with cc-pyspark over a Common Crawl snapshot.
4. **Crawler engineering**: StormCrawler or Nutch, robots.txt, per-domain queues, prioritization. Named by Exa,
   Keenable, Perplexity, Linkup, Firecrawl.
5. **Headless Chromium and anti-bot**: Playwright and CDP, TLS fingerprints, custom Chromium builds. Named by
   Tavily, Exa, Firecrawl, Jina.
6. **Inverted index and hybrid retrieval**, with Vespa as the one engine two vendors used (Linkup names it in its
   stack; Perplexity used it for the web index before moving in-house and still uses it elsewhere), Anserini and
   PISA for fundamentals, FAISS, usearch or Qdrant for ANN.
7. **Ranking cascades**: gradient-boosted learning to rank (LightGBM, CatBoost), cross-encoders, ColBERT; evaluation
   with nDCG and the vendors' open harnesses (NEEDLE, search_evals).
8. **Embedding-model training in PyTorch** (contrastive learning, FSDP; Exa asks for "a transformer from scratch",
   Perplexity for "contrastive learning, multilingual, and multimodal modeling"), then GPU inference (vLLM, Triton,
   TEI; read pplx-garden for the Rust and RDMA frontier).
9. **TypeScript** for MCP servers, SDKs and dashboards; every vendor's public repositories are MIT or Apache SDKs,
   MCP servers and evals, except Firecrawl's AGPL core, Jina Reader, Perplexity's Rust inference libraries and
   Brave's MPL browser.

Table stakes that no ad bothers to name: an observability stack, a CDN, a feature store. Kagi is the outlier
(Crystal and vanilla JavaScript, per an undated posting); Mojeek has no open roles.

## A minimum viable open-source search API, with the known cost figures

1. **Seed and bootstrap** from one Common Crawl snapshot (CC-MAIN-2026-43: 2.16B pages, 371 TiB uncompressed,
   41.4M hosts) or a focused own crawl; Stract and the Open Web Index both found a focused own crawl cheaper than
   indexing all of Common Crawl, and the Open Web Index pipeline does 30M pages a day with Spark on HPC.
2. **Crawl** with StormCrawler or the Nutch fork, render selectively with Playwright, extract with trafilatura (or
   Resiliparse where throughput matters), deduplicate and filter with datatrove, store WARC plus Parquet or Lance on
   object storage.
3. **Index** with tantivy or Vespa for BM25F and FAISS, usearch or Lance for binary-quantized IVF over BGE-M3 or
   Qwen3-Embedding vectors; fuse with RRF k=60. Sizing anchors: a 2018 tantivy experiment built a 13 TB BM25 index
   over 3.2B pages for under $50 of compute but about $400 a month of S3; ChatNoir needed 124 Elasticsearch nodes
   and 115.6 TB on disk for 1.6B pages at about 600 ms; Exa's Rust BM25 index ran 1.8 TB per 1B documents before
   compression; Marginalia serves about 300M documents from one server for about $200 a month.
4. **Rank** with LightGBM LambdaMART on BM25F, centrality (cc-webgraph), age and click or trajectory features, then
   Qwen3-Reranker-0.6B or 4B as the cross-encoder; select passages with an LLMLingua-2 style token classifier.
5. **Serve** a Rust or Go API with p50 and p95 targets stated per region, embeddings and rerankers on
   text-embeddings-inference, LLMs on vLLM; expose `search` and `fetch` over Streamable-HTTP MCP with OAuth and a
   keyless tier; wire it into Morphic or Perplexica for a front-end.

What this cannot reproduce [inferred from the notes]: a fresh index above about 10^9 pages with continuous recrawl
(open engines stop at 10^8 to 10^9), and anti-bot rendering capacity at crawl scale (Firecrawl's fire-engine is
closed; Tavily builds its own Chromium). Those two are where Exa's $5M GPU cluster, Perplexity's H100 pods and
every vendor's crawl fleet go.

## For this repository's reranking proxy

The proxy reranks 20 to 40 Tavily results listwise with a hosted LLM through two ordered passes. The open
replacements, in order of fit:

- **Qwen3-Reranker-0.6B or 4B** (Apache-2.0; publisher MTEB-R 65.80 and 69.76 against bge-reranker-v2-m3 at 57.03)
  as a pointwise cross-encoder over 4,000-character documents (32k context, yes/no-token scoring). No independent
  latency numbers exist; the swap must be measured on the repository's own Elo, SimpleQA and DeepSearchQA harness.
- **rank_llm with RankZephyr or FIRST** for a listwise open-weights replacement closest to the current design.
- **jina-reranker-v3** (0.6B, 64 documents per pass, self-reported BEIR 61.94) is the strongest inspectable listwise
  model but CC-BY-NC, so not for a paid service.
- **A snippet stage before reranking**: a Keenable-style token classifier (LLMLingua-2 recipe) would cut the 4,000
  characters the reranker reads per document, which the README identified as the main lever on SimpleQA.
- **Features the proxy already computes** (published dates, social-domain flags, rephrasing strategies) are exactly
  the inputs a small LambdaMART over Tavily results would use; the archive of cached responses is the training set.

## Gaps

- GitHub star, licence and activity verification was blocked (HTTP 403) for the serving and jobs researchers;
  figures marked [training knowledge] in the notes are unverified.
- The Brave and Tailcat acquisition wording ("Tailcat will become the foundation of Brave Search") could not be
  re-read; the Cliqz 2019 technical details are confirmed.
- No vendor discloses recrawl cadence quantitatively; all say "adaptive".
- Exa's "Query Engine" and "Index Intelligence" postings were only partly read (the Ashby feed was truncated).
- The intended full report pass was skipped for budget; the five notes (about 350 KB) carry the per-component
  evidence, URLs and the per-layer learning paths this digest condenses.
