# Brave Search API and Tavily as search backends: under the hood, pricing history, benchmarks, adoption

Research date: 2026-11-05. Labels used on every number: **[vendor]** = the company's own statement; **[independent]** = third-party benchmark/analyst; **[journalist]** = press; **[practitioner]** = developer forum/HN comment; **[competitor]** = a rival vendor's statement about the subject. Dates in parentheses are the publication/fetch date of the source.

---

## KQ1. Brave: what is under the hood (own crawler, Web Discovery Project, fallback to Bing/Google)?

### Takeaway
Brave Search has served 100% of web results from its own index since April 2023, when it removed the Bing API calls that had supplied ~7% of results; the index is built from Brave's own crawler plus opt-in browsing/click data from the Web Discovery Project (WDP), and the API page today states "no fallback to another search engine for any query." The only documented residual third-party use was images/video on the consumer engine in 2023; I found no 2026 statement on whether the API's Image/Video endpoints are own-index.

### Cited Findings
- [vendor, 2023-04-27, updated 2023-05-03] "We've removed all search API calls to Bing, which previously represented about 7% of query results." "Every Web search result seen in Brave Search is now served by our own index." At launch (June 2021) "about 13% of the queries required the help of third parties"; the independence score "rose from 87% to 93%" in under a year. Brave Search was "averaging about 22 million queries per day." — [Brave: search independence](https://brave.com/search-independence/)
- [vendor, 2023] WDP "allows Brave browser users to contribute anonymous browsing data" to improve the index; opt-in via the Brave browser. Image and video results were *not* served from Brave's own index "for now"; users could redirect those to Bing or Google. — [Brave: search independence](https://brave.com/search-independence/)
- [vendor, guide published 2023-09-22, updated 2025-10-16] "Brave Search is also built on more than just Web crawlers": WDP lets users "opt in and contribute anonymous data about searches and webpage visits"; the index is "powered by real queries and clicks in the Brave browser and Brave Search engine." Competitors are said to "rely on a combination of on-demand scraping, their own crawlers, and tools like the Bing API." — [Brave: what sets the API apart](https://brave.com/search/api/guides/what-sets-brave-search-api-apart/)
- [vendor, fetched 2026-11-05] API landing page: "Every result comes from Brave's own independent index"; FAQ: "no fallback to another search engine for any query"; data sources are Brave's own crawler plus WDP signals; the crawler code is described as open source; Brave calls itself "the only index built by signals from 130+ million real humans." — [Brave Search API](https://brave.com/search/api/)
- [vendor, 2026-02-12] Brave describes itself as "one of only three independent, global-scale search indexes in the western world." — [Brave blog: most powerful search API for AI](https://brave.com/blog/most-powerful-search-api-for-ai/)
- [journalist, 2023] Search Engine Journal covered the Bing cut-off as "Brave Search cuts ties with Bing, goes independent." — [SEJ](https://www.searchenginejournal.com/brave-search-cuts-ties-with-bing-goes-independent/485736/)

### Inferences
- The WDP click/visit signal is Brave's structural differentiator versus SERP-wrapper APIs: it gives Brave a behavioural ranking signal that scraping-based providers lack, which is why Brave frames index size as secondary (see KQ2).
- "No fallback for any query" (2026) is stronger than the 2023 statement, which exempted images/video on the consumer engine; the API now has Image and Video endpoints, but Brave did not say in any source I read whether those are own-index.

### Gaps
- No source states whether the Brave API's Image Search and Video Search endpoints are served from Brave's own index or a third party in 2026.
- The claim that the crawler code is open source appears on the API page, but I did not locate the repository URL.

---

## KQ2. Brave: index-size statements over time and the "vanity stat" framing

### Takeaway
Brave's own numbers moved from "over 30 billion pages" (API guide, Sept 2023; still on the page as of its Oct 2025 update, and in the Aug 2025 AI Grounding post) to "40 billion pages" (growth blog, 24 Feb 2026); by late 2026 the API landing page stopped giving a count, calling index size "a vanity stat" and claiming "99.9% of the web that matters." The 30B and 40B figures are both vendor claims with no independent measurement.

### Cited Findings
- [vendor, guide dated 2023-09-22, updated 2025-10-16] "Brave Search is powered by an independent index of over 30 billion pages" and "an index that grows by over one hundred million new and refreshed pages each day." — [Brave: what sets the API apart](https://brave.com/search/api/guides/what-sets-brave-search-api-apart/)
- [vendor, 2025-08-05] The AI Grounding post repeats "over 30 billion webpages" and says Brave Search handles "over 1.5 billion monthly queries." — [Brave blog: AI Grounding](https://brave.com/blog/ai-grounding/)
- [vendor, 2026-02-24] "40 billion pages"; "more than 100 million pages each day" added or refreshed; "one of just three Web search indexes at scale in the West." — [Brave blog: Search API growth](https://brave.com/blog/search-api-growth/)
- [vendor, fetched 2026-11-05] The API landing page gives no page count; it calls index size "a vanity stat" and claims "99.9% of the web that matters." — [Brave Search API](https://brave.com/search/api/)
- [independent analyst, undated] Sacra's Brave write-up cites roughly 40 billion pages (secondary restatement of Brave's figure). — [Sacra chat: Brave's independent index](https://sacra.com/chat/h/a1be974b-1269-41f7-bd55-54c9e7eabda1/)
- [vendor, 2026-02-12] The LLM Context launch post gives no count, only "billions of results from the Web." — [Brave blog](https://brave.com/blog/most-powerful-search-api-for-ai/)

### Inferences
- The primary source for "30B" is the Sept-2023 API guide (and the Aug-2025 AI Grounding post); the primary source for "40B" is the 24-Feb-2026 growth post. Anyone citing either number should date it.
- Dropping the count in favour of "vanity stat" is consistent with Brave repositioning against Perplexity's "hundreds of billions of webpages" claim (see KQ6) rather than competing on raw size.

### Gaps
- I did not find a standalone Brave blog post titled or themed "index size is a vanity stat"; the phrase appears on the API landing page. If such a post exists, it was not in the first page of the blog index or in search results.
- No independent measurement of Brave's index size exists in the sources found.

---

## KQ3. Brave: LLM Context endpoint (launched 2026-02-12) and Answers API

### Takeaway
LLM Context (`/res/v1/llm/context`) runs a normal Brave web search, extracts page content in real time, chunks and ranks it, and returns a token-budgeted (1k to ~33k tokens) context blob; Brave claims total latency "under 500ms at p90." Answers is a separate OpenAI-compatible, cited, grounded-answer product priced per search plus per token.

### Cited Findings
- [vendor, 2026-02-12; post updated 2026-06-25 and 2026-09-17] Mechanism: standard web search on Brave's index, then real-time extraction from each page (structured data, code, forum discussions, YouTube captions) split into "smart chunks," ranked and compiled; controls include Goggles, `maximum_number_of_tokens`, and location headers. "In practice we observe a total latency under 500ms at p90 for calls to LLM Context." No p50 given. The Sept 2026 update "revised the latency wording." Ask Brave uses open-weights Qwen3 on top of LLM Context; Ask Brave answers 22 million questions/day. — [Brave blog: most powerful search API for AI](https://brave.com/blog/most-powerful-search-api-for-ai/)
- [vendor, fetched 2026-11-05] Endpoint `/res/v1/llm/context`; token budget configurable "from 1k to ~33k tokens"; relevance threshold modes strict/balanced/lenient; each source carries URL and timestamp; results can be filtered to the last 24 hours; "under 500ms at P90"; token usage cut "by up to 4x." — [Brave Search API](https://brave.com/search/api/)
- [vendor, fetched 2026-11-05] Docs portal positions LLM Context as "Pre-extracted page content for your LLM — no scraping, token-budgeted," and lists Web, News, Image, Video, Place Search and Answers; the only number is "99.9% uptime." — [Brave API docs](https://api-dashboard.search.brave.com/app/documentation)
- [vendor, fetched 2026-11-05] Answers: summarized answers grounded on one or more searches with citations, streaming, OpenAI SDK compatibility; example model names "brave" and "brave-pro"; capacity 2 qps on the standard plan. — [Brave Search API](https://brave.com/search/api/)
- [competitor, 2026-07-27, modified 2026-10-29] Parallel notes Brave's Answers endpoint uses Chat Completions (Parallel's uses Responses) and that "Brave has no content extraction endpoint. If your agent needs full page text, that is a second vendor or your own fetcher." — [Parallel: Brave vs Parallel](https://parallel.ai/ai/articles/brave-search-api-vs-parallel)
- [vendor, 2025-08-05] Predecessor product "AI Grounding API" launched Aug 2025 at "$4 per thousand web searches, plus $5 per million tokens (input and output)"; single-search responses "finish streaming in under 4.5 seconds on average." — [Brave blog: AI Grounding](https://brave.com/blog/ai-grounding/)

### Inferences
- Answers appears to be the renamed/rebranded AI Grounding plan (identical $4/1k + $5/M-token pricing, same grounded-answer function). Not confirmed by an explicit Brave statement.
- The p90 claim is vendor-measured and was reworded in Sept 2026; treat "<500ms p90" as marketing until an independent latency test is cited.

### Gaps
- No independent p50/p90 latency measurement of LLM Context found. (Orcarouter's blog mentions an "independent benchmark published in August 2026" measuring nDCG@10 and latency across Brave, Tavily, etc., but I could not reach the primary source.)
- Brave's "up to 4x" token reduction has no published methodology.

---

## KQ4. Brave: pricing history, the early-2026 free-tier removal, terms changes, HN reaction

### Takeaway
Brave launched the API on 2023-05-30 with a free tier for "less than 2,000 queries per month" and a terms clause that (on the free plan) prohibited "using responses for AI inference"; on 2026-02-12 it collapsed plans into Search ($5 per 1,000 requests) and Answers ($4 per 1,000 + $5/M tokens), replaced the free plan with a $5 monthly credit (about 1,000 calls) that requires a credit card and attribution. HN reaction was thin and mostly practical (confusion over the AI-inference clause; later price comparisons against DeepSeek at $0.75/1k and Kagi at $12/1k).

### Cited Findings
- [vendor via HN, 2023-05-31] Show HN text: "Developers making less than 2,000 queries per month can use the API for free." — [HN 36140371](https://news.ycombinator.com/item?id=36140371); launch thread 95 points, 11 comments (2023-05-30) — [HN 36128702](https://news.ycombinator.com/item?id=36128702)
- [vendor, 2023-09-22 guide, updated 2025-10-16] Brave contrasted itself with rivals' "sudden price hikes" and noted "Exa offers plans as low as $2.5 CPM, but these plans come at the cost of slower speeds." — [Brave guide](https://brave.com/search/api/guides/what-sets-brave-search-api-apart/)
- [practitioner, 2026-01-30] Ask HN: while subscribing to the free tier the poster saw "By subscribing to this plan, you agree to abide by the Terms of Use. These Terms of Use prohibit using responses for AI inference," and asked whether OpenClaw agents violate it (4 points, 2 comments). Replies (2026-02-01, 2026-02-10): "Brave has an AI-specific API" / "Brave does have a plan for AI Inference ... https://api-dashboard.search.brave.com/app/plans?tab=ai." — [HN 46822822](https://news.ycombinator.com/item?id=46822822)
- [vendor, 2026-02-12] New pricing: Search $5 per 1,000 requests covering Web, LLM Context, Images, News, Videos; Answers $4 per 1k searches + $5 per million tokens; Spellcheck and Autocomplete $5 per 10k; "$5 of free credit renewed monthly" per plan ("$20 across all plans"), claimable only if you attribute the Brave Search API on your project's site. The post does not use the words "removing the free tier." — [Brave blog](https://brave.com/blog/most-powerful-search-api-for-ai/)
- [vendor, 2026-02-24] "$5 CPM" with a "$5 US monthly credit system (good for up to 1,000 calls per month)"; "up to 100 queries per second, depending on the plan." — [Brave blog: growth](https://brave.com/blog/search-api-growth/)
- [vendor, fetched 2026-11-05] Search: $5/1,000, 50 qps, "$5 in free credits each month"; Answers: $4/1,000 + $5/M tokens, 2 qps; Enterprise custom with Zero Data Retention. Header says "Up to $20 in free calls every month." "Prepaid credits, no subscription." A credit card is requested "To prevent abuse." — [Brave Search API](https://brave.com/search/api/)
- [competitor, 2026-07-27] "Brave restructured its plans in early 2026, retiring the old free tier that allowed a couple of thousand queries a month." Parallel also flags "Brave's storage rights clause" as something to raise during evaluation. — [Parallel](https://parallel.ai/ai/articles/brave-search-api-vs-parallel)
- [journalist, 2026-02] AlternativeTo headline: "Brave updates its Search API with a new LLM context endpoint for AI and new pricing" (article body behind a Cloudflare challenge; not read). — [AlternativeTo](https://alternativeto.net/news/2026/2/brave-updates-its-search-api-with-a-new-llm-context-endpoint-for-ai-and-new-pricing)
- [practitioner] HN item for the 2026-02-12 launch post got 5 points, 0 comments. — [HN 46992570](https://news.ycombinator.com/item?id=46992570)
- [practitioner, 2026-06-16] "Yesterday I wanted to get a brave search api key on the free tier and they require a credit card even for that." — [HN 48556902](https://news.ycombinator.com/item?id=48556902)
- [practitioner, 2026-07-17] "Unlike Kagi, Brave Search's API has a free tier (1000 searches per month)." — [HN 48942632](https://news.ycombinator.com/item?id=48942632)
- [practitioner, 2026-08-22] "to save on cost I will stick with the Brave Search API which gives you $5 free every month." — [HN 49404000](https://news.ycombinator.com/item?id=49404000)
- [practitioner, 2026-10-18] "It's 5 USD per 1000 requests, while DeepSeek's is 0.75 USD per 1000 requests." — [HN 50139295](https://news.ycombinator.com/item?id=50139295); "that's $5 with Brave Search API and $12 with Kagi API." — [HN 50138776](https://news.ycombinator.com/item?id=50138776)
- [practitioner, 2026-10-05] "they didn't include the Brave Search API, which is really great and imo a better experience than Exa." — [HN 49963644](https://news.ycombinator.com/item?id=49963644); another user switched from Brave to Keenable with "no noticable issues" (2026-10-06) — [HN 49974946](https://news.ycombinator.com/item?id=49974946)
- [vendor, fetched 2026-11-05] Brave's page notes Google's Custom Search JSON API shuts down January 1, 2027. — [Brave Search API](https://brave.com/search/api/)

### Inferences
- "Free-tier removal" is accurate in substance (the 2,000-query/month no-card free plan is gone) but Brave itself framed it as a $5 monthly credit; the credit requires a card and attribution, which is the practical change developers noticed.
- The pre-2026 AI-inference prohibition on the free plan explains why agent frameworks that shipped Brave as a default (OpenClaw) generated terms confusion in Jan 2026; the Feb 2026 unification into Search/Answers plans appears to have removed the plan-level distinction, though I did not read the new Terms text.
- HN reaction was muted: the launch post drew no comments; the free-tier change surfaced only indirectly in later threads.

### Gaps
- I could not read the current Brave API Terms of Use (the dashboard terms page is JS-rendered), so the exact post-Feb-2026 wording on AI inference and data storage is unverified.
- No HN thread specifically about the free-tier removal was found in Algolia searches; the reaction is reconstructed from scattered comments.

---

## KQ5. Brave: own benchmark posts, third-party benchmarks (Artificial Analysis, AIMultiple), and the Anthropic subprocessor listing

### Takeaway
Brave's own benchmarks are (a) SimpleQA for the AI Grounding API (Aug 2025: 4,332 questions, F1 92.1% single-search, 94.1% multi-search) and (b) a 1,500-query pairwise answer-quality test judged by Claude Opus 4.5/Sonnet 4.5 (Nov 2025; re-run June 2026 with Ask Brave first at Elo 1169). Independently, Artificial Analysis benchmarks two Brave configurations ("Brave web" and "Brave LLM context"); the LLM Context configuration scored 75 (tied with Parallel Advanced) in Sept 2026 snapshots. I found no Brave FreshQA post. Anthropic added Brave Search to its subprocessor list as of 2025-03-19.

### Cited Findings
**Brave's own SimpleQA (AI Grounding) benchmark**
- [vendor, 2025-08-05, updated 2025-09-01] Dataset: 4,332 SimpleQA questions; LLM judge (model not named); single-search F1 92.1% (up from 89.8% at release), Research single-search F1 92.3%, Research multi-search F1 94.1% (Acc 93.25%, Acc* 94.9%). Multi-search averaged 7 search queries and 210 unique pages per question, mean 74 seconds. Competitors as reported by Brave: Perplexity Sonar Pro F1 85.5%, Sonar 77.3%, Perplexity Deep Research 93.9%; Tavily + GPT-4.1 (multi-search) Acc* 93.3%; Exa Acc* 85.83%, Exa Research 91.6%, Exa Research Pro 94.9%. Harness notes: excluded huggingface.co/datasets URLs and pages containing "simpleqa"; of 292 answers the judge marked wrong, human review found 167 were judge errors; run-to-run variance up to 0.2% F1. — [Brave blog: AI Grounding](https://brave.com/blog/ai-grounding/)

**Brave's pairwise answer-quality ("multi-search") benchmark**
- [vendor, 2026-02-12, updated 2026-06-25] Nov 30, 2025 round: 1,500 queries sampled from real usage (withheld "for privacy reasons"); judges Claude Opus 4.5 and Sonnet 4.5 by majority vote; all pairwise comparisons, each pair in both orders to control position bias; competitor answers scraped via BrightData. 5-point Likert means: Grok 4.71, Ask Brave 4.66, Google AI Mode 4.39, ChatGPT 4.32, Perplexity 4.01. June 2026 round (Bradley-Terry/Elo): Ask Brave 1169, Grok 1157, Ask Brave v1 1098, Google AI Mode 1000, ChatGPT 880, Perplexity 695. — [Brave blog](https://brave.com/blog/most-powerful-search-api-for-ai/)
- [journalist, 2026-07-26] PPC Land: "Ask Brave posted 1169 Elo against Grok's 1157 in a test Brave ran and judged with Claude models. Calls cost $5 per 1,000. Who checks a vendor's own scorecard?" — [PPC Land](https://ppc.land/braves-5-search-api-wins-ai-answer-test-as-perplexity-finishes-last/)

**Third-party benchmarks**
- [independent, methodology page fetched 2026-11-05] Artificial Analysis Search Index = equal-weighted mean of DeepSearchQA, BrowseComp and AA-Omniscience. Its provider table lists two Brave rows: "Brave web" (Brave Web Search API, settings `q=agent query, result_filter=web`) and "Brave LLM context" (Brave LLM Context API, `q=agent query, api=llm_context`). Embedded leaderboard data includes ids `brave-gpt-5-6-luna-medium-search-api` and `tavily_basic-gpt-5-6-luna-medium-search-api` with `latestMeasuredAt` 2026-08-17. — [AA methodology](https://artificialanalysis.ai/methodology/search-api); live table: [AA leaderboard](https://artificialanalysis.ai/agents/search-api)
- [competitor citing independent, 2026-07-27, modified 2026-10-29] "Artificial Analysis's Search Index data dated September 22, 2026 shows Parallel Advanced and Brave LLM Context tied at 75, both behind Perplexity Search (medium) at 80 and Octen Search at 77. Parallel Advanced's search cost is $47.93 per 1,000 benchmark tasks; Brave LLM Context's is $61.96. Brave completes tasks faster, at 21.8 seconds versus 40.5." Also: "Evaluate Brave LLM Context when you need model grounding, rather than substituting its separate Web Search endpoint." — [Parallel](https://parallel.ai/ai/articles/brave-search-api-vs-parallel)
- [competitor citing independent, table "as of September 8" 2026] Octen's blog lists: Perplexity Search (high) 79; Octen 77; Perplexity (low) 77; Parallel (advanced) 75; "Brave Search (LLM context) — Index 75, 24.4s, about $0.130"; You.com 74; Exa (auto) 74. It also cites an unnamed "independent benchmark published in August 2026" with nDCG@10 placing Octen (0.495) "behind Parallel, Brave, Kagi, Perplexity, Context, Tavily and Exa." — [Orcarouter/Octen blog](https://www.orcarouter.ai/blog/octen-search-artificial-analysis-search-index)
- [vendor citing independent, fetched 2026-11-05] Brave's API page cites AIMultiple: agent quality score Brave 14.89, Firecrawl 14.58, Exa 14.39, Tavily 13.67; Brave 669 ms average latency, "Up to 20x faster." — [Brave Search API](https://brave.com/search/api/)

**Anthropic subprocessor listing**
- [independent blogger quoting Anthropic, 2025-03-21] Simon Willison quoted Anthropic's subprocessor list: "As of March 19, 2025 ... Subprocessors added: Brave Search," and found Claude's ten citations were "an exact match" for the same search on Brave. — [Simon Willison](https://simonwillison.net/2025/Mar/21/anthropic-use-brave/)
- [journalist, 2025-03-21] TechCrunch: "Anthropic appears to be using Brave to power web searches for its Claude chatbot." — [TechCrunch](https://techcrunch.com/2025/03/21/anthropic-appears-to-be-using-brave-to-power-web-searches-for-its-claude-chatbot/)
- [third-party tracker, unverified, dated 2026-06-10] A tracking site lists Brave Search as an Anthropic subprocessor for "Web search (all products)," US. — [stackposture](https://stackposture.pages.dev/vendors/anthropic/subprocessors/); authoritative page is [Anthropic Trust Center](https://trust.anthropic.com/subprocessors) (JS-rendered; could not extract text).
- [vendor, 2026-06-29] Brave blog: "Claude Cowork on Amazon Bedrock with Brave Search." — [Brave blog](https://brave.com/blog/claude-cowork-amazon-bedrock-brave-mcp/)

### Inferences
- The "65-to-75 endpoint switch": AA's methodology confirms both a "Brave web" and a "Brave LLM context" configuration are benchmarked, and Parallel's advice to evaluate LLM Context "rather than substituting its separate Web Search endpoint" is consistent with the LLM Context configuration scoring materially higher. However, no source I reached states a 65 score for the web endpoint; treat "65" as unverified.
- Brave's two headline benchmarks are both vendor-run with LLM judges; the SimpleQA one is the more reproducible (public dataset, documented filtering, judge-error audit), while the pairwise test uses a withheld query set.

### Gaps
- No Brave blog post reporting FreshQA results was found (WebSearch and blog index). Brave's "multi-search" results are the Research-mode SimpleQA rows and the pairwise answer test, not FreshQA.
- The 65 score for Brave's web endpoint on Artificial Analysis is unverified; the AA leaderboard is JS-rendered and the figure did not appear in the HTML I retrieved.
- I could not read the current Anthropic Trust Center subprocessor page directly.

---

## KQ6. Tavily: what is under the hood (own index vs SERP aggregation)?

### Takeaway
Primary-source evidence is split: Sacra states Tavily "does not maintain its own search index" and "fans out to multiple data sources and search engines in real time," while Tavily's own 2026 materials claim "billions of pages crawled and extracted," an "indexing" layer, "index coverage" improvements, and a `max_age_hours` parameter that trades cached/indexed results against live fetching. The most defensible reading is a hybrid: a cache/index of extracted content layered over upstream search fan-out, with live fetch on demand.

### Cited Findings
- [independent analyst, undated; latest cited item 2026-02-10] "does not maintain its own search index"; an asset-light aggregator that "fans out to multiple data sources and search engines in real time." — [Sacra: Tavily](https://sacra.com/c/tavily/)
- [vendor, fetched 2026-11-05] Homepage: "intelligent caching, and indexing keeps latency predictable as traffic grows"; "Billions of pages crawled and extracted without downtime"; "180 ms" is the "p50 on Tavily /search making us fastest on the market"; "300M+ monthly requests handled"; "3M+ developers"; "99.99% uptime"; requests pass through layers that "block PII leakage, prompt injection, and malicious sources." No literal phrase "agent-native index" appears on the homepage. — [Tavily](https://tavily.com)
- [vendor, 2026-08-11] Blog "Tavily Ranks #1 on SealQA and SimpleQA": "#1 in accuracy on SealQA-Hard, SealQA-0, and SimpleQA after rebuilding core parts of Search, including evidence ranking, contradiction handling, and index coverage." (Figures not extracted.) — [Tavily blog index](https://www.tavily.com/blog)
- [vendor, fetched 2026-11-05] Search endpoint docs: `max_age_hours` (range -1 to 720): "Lower values do not cost more credits, but fetching live adds latency"; under heavy load, non-paying requests setting `max_age_hours` "may be refused with `434 Flex tier capacity exceeded`." `include_raw_content: text` "may increase latency." Responses carry `response_time`. — [Tavily search API reference](https://docs.tavily.com/documentation/api-reference/endpoint/search)
- [vendor (Tavily's own eval repo), last updated 2026-04-02] Lists "Google (SERP via Serper)" as a separate provider category from Tavily, and labels Brave and Exa as distinct providers, i.e., Tavily does not describe itself as a SERP wrapper in its own benchmark. — [tavily-search-evals](https://github.com/tavily-ai/tavily-search-evals)
- [vendor (Perplexity), 2025-09-25] Perplexity's Search API launch post contrasts "Legacy search incumbents" that "maintain proprietary indices for their own exclusive use" with "Other providers [that] have tried their best to fill the gaps," and claims "an index covering hundreds of billions of webpages." The text I could read does **not** apply a "SERP-based" label to any named provider; the comparison figure (FIG. 03) is an image. — [Perplexity blog](https://www.perplexity.ai/hub/blog/introducing-the-perplexity-search-api)
- [practitioner, 2026-09-17] Scry's Show HN argues services like Tavily map agent context to a small subset of their index. — [HN 49748041](https://news.ycombinator.com/item?id=49748041); [practitioner, 2025-08-20] Channel3: when asked for products, Tavily "returned articles, not structured product data." — [HN 44962881](https://news.ycombinator.com/item?id=44962881)
- [vendor (Nebius), 2026-02-10] The acquisition release describes Tavily as "real-time web access" / "real-time search infrastructure" and says nothing about an index or crawler. — [Nebius newsroom](https://nebius.com/newsroom/nebius-announces-agreement-to-acquire-tavily-to-add-agentic-search-to-its-ai-cloud-platform)

### Inferences
- `max_age_hours` is the clearest technical tell: results default to a cached/indexed copy and can be forced live at a latency cost, which fits "cache + index of extracted pages over upstream retrieval" better than either "pure SERP wrapper" or "fully independent web index."
- The 180 ms p50 claim (vendor) is plausible only for cache hits; Brave's "669 ms average" for itself in the AIMultiple test is a different metric (end-to-end, third-party harness), so the two are not comparable.

### Gaps
- No Tavily engineering post or job posting naming its upstream search provider(s) or describing its crawler was found within budget.
- Perplexity's "SERP-based" label could not be confirmed in page text (it may live in the FIG. 03 image).
- Tavily's SealQA/SimpleQA figures (Aug 2026 post) were not extracted.

---

## KQ7. Tavily: search depths, credits, pricing and latency statements

### Takeaway
Tavily meters in credits: basic/fast/ultra-fast search = 1 credit, advanced = 2; Extract 1 credit per 5 URLs (2 for advanced); Research 4 to 250 credits. The free tier is 1,000 credits/month with no card; paid plans run from $30/4,000 credits ($7.50 per 1,000) to $500/100,000 ($5.00 per 1,000), with pay-as-you-go at $0.008/credit ($8 per 1,000). At parity (1 basic search = 1 credit) this makes Tavily's per-search cost equal to or above Brave's $5/1,000 except on the Growth plan.

### Cited Findings
- [vendor, fetched 2026-11-05] Credits: Search basic 1, advanced 2; Extract basic 1 per 5 successful URLs, advanced 2 per 5; Map 1 per 10 pages (2 with instructions); Crawl = map + extract; Research mini 4 to 110 credits, pro 15 to 250. Free: 1,000 credits/month, no credit card. Plans: Project 4,000 credits $30; Bootstrap 15,000 $100; Startup 38,000 $220; Growth 100,000 $500; Pay-as-you-go $0.008/credit; Enterprise custom. — [Tavily API credits](https://docs.tavily.com/documentation/api-credits)
- [vendor, fetched 2026-11-05] `search_depth` values: `advanced` ("Highest relevance with increased latency"; 2 credits), `basic` ("A balanced option for relevance and latency"; 1), `fast` ("Prioritizes lower latency while maintaining good relevance"; 1), `ultra-fast` ("Minimizes latency above all else"; 1; one NLP summary per URL). `max_results` default 10, max 20; `chunks_per_source` 1 to 3 (~500 chars basic/fast, ~800 advanced); topics `general`, `news`, `finance`; `include_domains` up to 300; `auto_parameters` may silently select `advanced` (2 credits). — [Tavily search API reference](https://docs.tavily.com/documentation/api-reference/endpoint/search)
- [vendor, fetched 2026-11-05] "180 ms" p50 on /search, "fastest on the market." — [Tavily](https://tavily.com)
- [independent analyst] Sacra lists the free tier as 100 credits/month, which conflicts with Tavily's docs (1,000). — [Sacra](https://sacra.com/c/tavily/)
- [practitioner, 2025-06-19] "Tavily - 15K searches a month for $100 a month" (matches today's Bootstrap plan, suggesting plan pricing has been stable since at least mid-2025). — [HN 44318748](https://news.ycombinator.com/item?id=44318748)
- [competitor, 2026-07-27] Parallel's own pricing for comparison: Basic ~1s and $5 per 1,000, Advanced ~3s and $5 per 1,000 (default); Extract $1 per 1,000 URLs. — [Parallel](https://parallel.ai/ai/articles/brave-search-api-vs-parallel)

### Inferences
- Tavily's free tier (1,000 credits, no card) is now more generous than Brave's ($5 credit = ~1,000 calls, card required), reversing the 2023 to 2025 situation when Brave offered 2,000 free queries.
- `advanced` is the depth Tavily used in its own SimpleQA/relevance benchmark (see KQ8), so the benchmarked configuration costs 2 credits ($10 to $16 per 1,000) rather than the headline 1-credit price.

### Gaps
- No pricing history (dates of plan changes) is published by Tavily; only the mid-2025 HN data point anchors stability.
- No independent latency measurement of the 180 ms p50 claim found.

---

## KQ8. Tavily: the evals repository (tavily-search-evals) methodology

### Takeaway
The repo at github.com/tavily-ai/tavily-evals returns 404; the live repo is tavily-ai/tavily-search-evals (17 stars, last updated 2026-04-02). It runs the full SimpleQA set, has gpt-4.1 extract an answer from retrieved documents, grades with the official SimpleQA classifier, and reports Tavily 93.3% vs Perplexity Search 85.92%, Serper 82.15%, Brave 76.05%, Exa 71.24%; a second "Document Relevance" benchmark uses QuotientAI on a Tavily-generated dynamic dataset (Tavily 83.02%, Brave 56.2%, Exa 51.33%). It is vendor-run with a vendor-chosen config.

### Cited Findings
- [vendor, repo last updated 2026-04-02] SimpleQA: "Runs the full SimpleQA dataset against each provider"; "Retrieved documents are reformatted for an LLM (we used `gpt-4.1`) to extract a predicted answer"; graded by "the official SimpleQA classifier." Document Relevance: "Uses QuotientAI to assess the relevance of retrieved documents," with a dynamic dataset from Tavily's open-source generator (`datasets/document_relevance_dynamic_test_set.json`). Providers: Tavily, Exa, Brave, Google (SERP via Serper), Perplexity Search, Perplexity, GPTR. — [tavily-search-evals README](https://github.com/tavily-ai/tavily-search-evals)
- [vendor] SimpleQA accuracy: Tavily 93.3%; Perplexity Search 85.92%; Google (SERP) via Serper 82.15%; Brave Search 76.05%; Exa Search 71.24%. Document Relevance: Tavily 83.02%; Perplexity Search 71.2%; Serper 58.11%; Brave 56.2%; Exa 51.33%. — [tavily-search-evals README](https://github.com/tavily-ai/tavily-search-evals)
- [vendor] Example config: Tavily `search_depth: "advanced"`, `include_raw_content: false`, `max_results: 10`; Perplexity Search `max_results: 10`, `max_tokens_per_page: 512`. Defaults: `--post_process_model gpt-4.1`, `--evaluator_model gpt-4.1`. MIT licence. — [tavily-search-evals README](https://github.com/tavily-ai/tavily-search-evals)
- [vendor (GitHub org listing), fetched 2026-11-05] "tavily-search-evals — A public repository for running search benchmarks across multiple search providers," 17 stars, Python, updated April 2, 2026. — [tavily-ai repositories](https://github.com/orgs/tavily-ai/repositories?q=eval)
- [vendor (Brave), 2025-08-05] For contrast, Brave's SimpleQA run reports Tavily + GPT-4.1 (multi-search) at Acc* 93.3% and Brave's own single-search F1 at 92.1%, i.e., the same Tavily number but a very different Brave number from Tavily's 76.05%. — [Brave blog: AI Grounding](https://brave.com/blog/ai-grounding/)

### Inferences
- The 93.3% Tavily figure recurs in both Tavily's repo and Brave's post, suggesting a common provenance (Tavily's published result). The gap between Brave's self-reported 92.1% and Tavily's 76.05% for Brave is almost certainly a harness difference: Tavily's repo appears to call Brave's web-search endpoint (snippets) while Brave's post uses its AI Grounding/LLM Context pipeline with full-page content. This is the clearest example in the study of endpoint choice dominating "provider" scores.
- No README date for the results table; the repo's example output folders are dated 2025-01-15, suggesting the numbers may predate Brave's LLM Context (Feb 2026) and Perplexity's Search API (Sept 2025) iterations.

### Gaps
- The README gives no date for the results, no run count, and no per-provider endpoint/parameter details beyond the config snippet (the full `configs/config.json` was not fetched).
- The Document Relevance dataset's topics and size were not read.

---

## KQ9. Tavily: the Nebius acquisition (date, price, terms)

### Takeaway
Nebius announced the agreement on 2026-02-10 with no disclosed price and closing expected "in the next few weeks"; Bloomberg (via Sacra) put the price at $275 million, and Sacra characterised it as "roughly a 98x revenue multiple" on 2025 revenue. Secondary outlets add unverified earn-out figures ($125M milestone; totals up to $337.5M to $400M). Tavily keeps its brand, and founder/CEO Rotem Weiss and the team join Nebius.

### Cited Findings
- [vendor (Nebius), 2026-02-10] "Transaction value was not disclosed." Closing "in the next few weeks, subject to customary closing conditions." Tavily stats cited: "over 3 million monthly SDK downloads," "developer community of more than 1 million users," customers including IBM (Fortune 500), Cohere and Groq. Tavily "will continue operating under its current brand." Quotes: Roman Chernin (Nebius CBO): "Tavily is solving a critical part of this stack with agentic search and has proven it with strong developer adoption." Rotem Weiss: "Tavily is on a mission to onboard the next billion AI agents to the web." — [Nebius newsroom](https://nebius.com/newsroom/nebius-announces-agreement-to-acquire-tavily-to-add-agentic-search-to-its-ai-cloud-platform)
- [independent analyst citing Bloomberg 2026-02-10] "$275 million"; "roughly a 98x revenue multiple" on 2025 revenue (implies ~$2.8M 2025 revenue; my arithmetic, not Sacra's statement). Prior funding $25M: $5M seed (July 2024), $20M Series A (August 2025) led by Insight Partners and Alpha Wave Global. Founded 2023; HQ New York; operations in US and Israel. — [Sacra: Tavily](https://sacra.com/c/tavily/)
- [journalist, 2026-02-10] SiliconANGLE: "AI infrastructure giant Nebius buys agentic search startup Tavily." — [SiliconANGLE](https://siliconangle.com/2026/02/10/ai-infrastructure-giant-nebius-buys-agentic-search-startup-tavily/)
- [journalist, 2026-02-11] The Star (Reuters-sourced): "Dutch AI cloud firm Nebius to acquire Israeli startup Tavily." — [The Star](https://www.thestar.com.my/news/world/2026/02/11/dutch-ai-cloud-firm-nebius-to-acquire-israeli-startup-tavily)
- [journalist, 2026-02] PYMNTS and iTiger report ~30 employees joining Nebius. — [PYMNTS](https://www.pymnts.com/?p=3470997)
- [secondary, unverified] Pulse.bot adds "$125 million payable if milestones are met"; Startupim lists $337.5M with reports ranging $275M to $400M. — [Pulse.bot](https://www.pulse.bot/ai/deals/nebius-group-acquires-ai-startup-tavily-for-275m-363d25bf-1c82-4f50-9bd5-4d3cf9c55c77/); [Startupim](https://startupim.com/company/tavily)
- [practitioner, 2026-02-15] HN story "Nebius to buy AI agent search company Tavily for 275M" (2 points, 1 comment). — [HN 47024216](https://news.ycombinator.com/item?id=47024216)
- [vendor, fetched 2026-11-05] Tavily's logo now reads "Tavily by Nebius"; press room lists "Tavily is Joining Nebius." — [Tavily](https://tavily.com)

### Inferences
- "Tavily by Nebius" branding on the live site implies the deal closed (consistent with the "next few weeks" guidance), but I found no closing announcement.
- The $275M headline is a Bloomberg report, not a disclosed term; earn-out figures are unconfirmed.

### Gaps
- No primary source for the closing date or final consideration; no Bloomberg article fetched directly.

---

## KQ10. Adoption: which agent frameworks ship Tavily or Brave as the default search tool?

### Takeaway
Evidence within budget is partial. Brave reports 1M+ sign-ups via OpenClaw and Hermes (vendor) and a Jan-2026 HN thread confirms OpenClaw prompts for a Brave key; Tavily reports 3M+ monthly SDK downloads and lists LangChain among customer logos (vendor). CrewAI's docs list Serper first, then Brave, Exa and Tavily, with no single default. LangChain/LangGraph and Claude Code docs pages were JS-rendered and could not be verified in this wave.

### Cited Findings
- [vendor, fetched 2026-11-05] "1 million+" OpenClaw and Hermes sign-ups; "more than 1 million OpenClaw users." — [Brave Search API](https://brave.com/search/api/); [vendor, 2026-04-01] "Brave Search API approaches 700,000 OpenClaw users." — [Brave blog](https://brave.com/blog/openclaw/)
- [practitioner, 2026-01-30] "I was setting up OpenClaw and it requested a Brave Search API key." — [HN 46822822](https://news.ycombinator.com/item?id=46822822)
- [vendor (Nebius), 2026-02-10] Tavily: "over 3 million monthly SDK downloads," "more than 1 million" developers. — [Nebius](https://nebius.com/newsroom/nebius-announces-agreement-to-acquire-tavily-to-add-agentic-search-to-its-ai-cloud-platform)
- [vendor, fetched 2026-11-05] Tavily customer logos include LangChain, MongoDB, JetBrains, Groq, AWS, IBM, Mastercard. — [Tavily](https://tavily.com)
- [vendor (CrewAI docs), fetched 2026-11-05] Search & Research tools listed: Serper Dev Tool ("Google search API integration"), Brave Search Tool ("Privacy-focused search with Brave's independent search index"), Exa, Linkup, Tavily Search / Extractor / Research tools, SerpApi, You.com; the code example imports `SerperDevTool` first. — [CrewAI tools overview](https://docs.crewai.com/en/tools/search-research/overview)
- [vendor (Anthropic docs), fetched 2026-11-05] The Claude web search tool documentation does not name the underlying search provider. — [Claude web search tool docs](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool); the provider is evidenced only by the subprocessor listing (KQ5).
- [vendor (LangChain), undated] LangChain maintains Brave Search integration pages. — [LangChain Brave provider](https://python.langchain.com/docs/integrations/providers/brave_search)
- [practitioner, 2026-02-26] A Show HN agent workspace "hits Brave/Serper/Tavily," illustrating the three as the usual interchangeable options. — [HN 47170946](https://news.ycombinator.com/item?id=47170946)

### Inferences
- Brave's adoption claims are concentrated in the open-source agent ecosystem (OpenClaw, Hermes, MCP servers), where a cheap flat $5/1k price and an official MCP server matter; Tavily's are concentrated in the Python agent-framework ecosystem (SDK downloads, LangChain relationship).
- Neither vendor is a universal default: CrewAI leads with Serper; OpenAI's Agents SDK ships a hosted WebSearchTool (not checked this wave).

### Gaps
- Could not verify from docs whether LangChain/LangGraph quickstarts still use `TavilySearch` as the canonical example tool, or what Claude Code's WebSearch uses (pages JS-rendered; budget exhausted). n8n, LlamaIndex and OpenAI Agents SDK examples were not checked.

---

## KQ11. Why each is a practical default (synthesis)

### Takeaway
Brave is the practical default when you want an independent index with no third-party fallback, flat predictable pricing ($5/1k across endpoints), enterprise compliance (SOC 2 Type II, ZDR), and an LLM-ready context endpoint; Tavily is the practical default when you want an agent-oriented toolchain (search, extract, crawl, map, research) in one SDK with a no-card free tier and depth/latency knobs, accepting that its retrieval layer sits on top of upstream sources and a cache.

### Cited Findings
- [vendor, 2026-02-24] Brave's own positioning: independence ("not affected by Big Tech lawsuits or attempted shutdowns"), "true Zero Data Retention" for enterprise, SOC 2 Type II, purpose-built LLM Context and news endpoints, "intuitively-structured JSON." — [Brave blog: growth](https://brave.com/blog/search-api-growth/)
- [vendor, 2025-10-29] SOC 2 Type II attestation for Brave Search API. — [Brave blog: SOC 2](https://brave.com/blog/soc2/); [vendor, 2025-07-16] listed in AWS Marketplace. — [Brave blog](https://brave.com/blog/search-api-aws-marketplace/)
- [vendor, fetched 2026-11-05] Tavily: SOC 2, ZDR, GDPR, ISO 27001; endpoints Search, Extract, Research, Crawl, Map. — [Tavily](https://tavily.com)
- [competitor, 2026-07-27] Brave "has no content extraction endpoint." — [Parallel](https://parallel.ai/ai/articles/brave-search-api-vs-parallel)
- [independent, Sept 2026 snapshots via secondary sources] Brave LLM Context scores 75 on the Artificial Analysis Search Index; Tavily (basic) is also benchmarked there (score not captured). — [AA methodology](https://artificialanalysis.ai/methodology/search-api)

### Inferences
- The two vendors' benchmark wars (Brave 92.1% vs Tavily's 76.05% for Brave on SimpleQA) show that a "default" choice is really an endpoint-and-harness choice; a buyer should benchmark Brave LLM Context (not Web Search snippets) against Tavily advanced (2 credits), at matched cost.
- Google's Custom Search JSON API shutdown on 2027-01-01 (per Brave's page) is likely to push more migrations toward both vendors in the coming year.

### Gaps
- No independent head-to-head of Brave LLM Context vs Tavily advanced at matched cost was found.

## Verification (wave 2, topic brave_tavily, 2026-11-05)

| claim | verdict | what the source says | URL |
|---|---|---|---|
| Brave removed all Bing API calls (~7% of results) in April 2023; API page says "no fallback to another search engine for any query" | CONFIRMED | Independence post (published Apr 27, 2023, updated May 3, 2023): "We've removed all search API calls to Bing," which "previously represented about 7% of query results." The "no fallback" sentence is not on this post; it is in the FAQ of the API page ("There is no fallback to another search engine for any query"; "Brave answers every query from its own index. No handoff."). Nuance: the independence post says optional Google Fallback mixing remains available to browser/search users (not the API). | https://brave.com/search-independence/ ; https://brave.com/search/api/ |
| LLM Context launched 2026-02-12, $5/1k requests, <500ms p90; Answers $4/1k searches + $5/M tokens; $5 monthly free credit requiring attribution | CONFIRMED | Published Feb 12, 2026 (later updated Jun 25 and Sep 17, 2026). "$5 per 1000 requests, with $5 free credit every month"; "total latency under 500ms at p90 for calls to LLM Context"; "Answers is priced at $4 per thousand Web searches plus $5 per million tokens (input and output)"; "Every plan gets $5 of free credit that renews every month" conditioned on attributing Brave Search API on the project's website/about pages. | https://brave.com/blog/most-powerful-search-api-for-ai/ |
| 2026-02-24 growth post: 40 billion pages, >100M pages refreshed per day | CONFIRMED | "Published Feb 24, 2026"; "independent search index of now 40 billion Web pages"; "we add or refresh more than 100 million pages each day". (The 2023 "over 30 billion" comparison was not re-checked here.) | https://brave.com/blog/search-api-growth/ |
| tavily-search-evals SimpleQA: Tavily 93.3%, Perplexity 85.92%, Serper 82.15%, Brave 76.05%, Exa 71.24%; gpt-4.1 extraction; official SimpleQA classifier | CONFIRMED | README table: Tavily 93.3%, Perplexity Search 85.92%, Google (SERP) via SERPER 82.15%, Brave Search 76.05%, Exa Search 71.24%. Extraction model gpt-4.1 (default --post_process_model); grading by "the official SimpleQA classifier" (evaluator gpt-4.1). Vendor-run eval. | https://github.com/tavily-ai/tavily-search-evals |
| Nebius announced Tavily acquisition 2026-02-10, value undisclosed, 3M+ monthly SDK downloads, 1M+ developers; Sacra citing Bloomberg: $275M | UNVERIFIABLE (Nebius part CONFIRMED) | Nebius release dated Feb 10, 2026: "The transaction value has not been disclosed"; "over 3 million monthly SDK downloads"; "developer community of more than one million users". Sacra page returned HTTP 503, so the $275M/Bloomberg attribution could not be re-read; HN item 47024216 ("Nebius to buy AI agent search company Tavily for 275M") corroborates a Bloomberg report dated 2026-02-10 in a comment link but is secondary. | https://nebius.com/newsroom/nebius-announces-agreement-to-acquire-tavily-to-add-agentic-search-to-its-ai-cloud-platform ; https://sacra.com/c/tavily/ (503) |
