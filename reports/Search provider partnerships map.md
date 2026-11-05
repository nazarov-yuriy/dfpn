# Search providers carve up the agent stack

Only one frontier lab has visibly outsourced its default web search: Anthropic, whose subprocessor list added **Brave Search on 2025-03-19** and whose leaked tool schema was titled `BraveSearchParams` ([Willison](https://simonwillison.net/2025/Mar/21/anthropic-used-brave/)). OpenAI, Google, Microsoft, xAI, DeepSeek and Perplexity run their own indexes, and Mistral, Groq, Ollama and Zed ship built-in search without naming a backend. Below the labs the market has split into tiers. **Tavily owns the "documentation default" tier**: it is the only internet-search tool wired into Cohere's docs and cookbooks, the only vendor with a dedicated NVIDIA NeMo Agent Toolkit package, the search in AWS, Azure and IBM first-party samples, the hard-coded default in LangChain's open_deep_research and GPT Researcher, and the default engine of OpenHands Cloud — and Nebius bought it on 2026-02-10 ([Nebius](https://nebius.com/newsroom/nebius-announces-agreement-to-acquire-tavily-to-add-agentic-search-to-its-ai-cloud-platform)). **Exa owns the "platform default" tier**: the fallback engine for every non-native model on OpenRouter, the sole backend of Letta's `web_search`, the search layer behind Firefox's Smart Window, a Google Cloud grounding option, a Vercel AI Gateway tool and a Cloudflare resale option, with Cursor, Notion AI, Cognition and HubSpot as press-named customers ([Exa Series C](https://exa.ai/blog/announcing-series-c)). **Parallel is the second name wherever a hyperscaler lists two** (Google Cloud, Vercel, OpenRouter, Cerebras, AWS Marketplace). Brave sells its index quietly (Anthropic, OpenClaw's default key prompt, a logo wall of Cohere, Mistral, Together and Snowflake), while Keenable (Baseten, Pipecat), Linkup (Cloudflare, EU enterprise logos), You.com (DuckDuckGo, Windsurf, Harvey) and Ceramic (Cloudflare's default) hold single niches. Truly exclusive relationships are rare — two acquisitions (Nebius–Tavily, Elastic–Jina), Firefox–Exa, Letta–Exa, OpenHands–Tavily and Anthropic–Brave — and every cloud, gateway, orchestration framework, open chat UI and plugin marketplace observed is multi-homed with three to thirty providers. The answer to "Cohere recommends Tavily" is yes in substance (Tavily is the sole search tool in Cohere's docs and Cohere is a named Tavily customer) but no literal "we recommend" sentence exists; Cohere's docs say "swap in any other LangChain tool you like" ([Cohere docs source](https://raw.githubusercontent.com/cohere-ai/cohere-developer-experience/main/fern/pages/integrations/cohere-and-langchain/tools-on-langchain.mdx)).

**How to read the tables.** All pages were fetched 2026-11-05 ("obs.") unless a publication date is given; verification re-fetched ten load-bearing claims the same day. Relationship types: **Default** (shipped or documented as the default or sole backend), **Built-in option** (consumer-side code or docs expose it as one of several), **Docs sample** (first-party tutorial, template or cookbook names the vendor), **Marketplace** (plugin, connector or catalog listing), **Reseller** (consumer bills for the vendor's API), **Customer** (named in press), **Logo** (vendor logo wall), **Vendor-side** (only the search vendor documents the integration), **Owner/Investor**, **Inferred**. Evidence labels: *docs* (consumer's own documentation), *vendor docs* (search vendor's documentation), *code* (source files, manifests, PyPI), *press* (company release or blog), *case study*, *subprocessor* (subprocessor list), *directory* (marketplace listing or logo wall), *journalist*, *inferred*.

## Frontier labs build their own search; Anthropic alone buys an index

Every lab with its own index exposes a first-party tool and prices it per thousand calls: OpenAI **$10/1k** ([OpenAI pricing](https://developers.openai.com/api/docs/pricing)), Google **$14/1k after 5,000 free per month** on Gemini 3+ ([Gemini pricing](https://aistudio.google.com/docs/pricing)), xAI **$5/1k** ([xAI pricing](https://docs.x.ai/developers/pricing)), DeepSeek **$0.75/1k** on an "in-house search engine" ([DeepSeek](https://api-docs.deepseek.com/guides/search)). Microsoft retired the Bing Search APIs on 2025-08-11 and funnels developers to "Grounding with Bing Search" inside Azure AI Agents ([Microsoft](https://learn.microsoft.com/en-us/lifecycle/announcements/bing-search-api-retirement)); Google closed the Custom Search JSON API to new customers with existing access ending 2027-01-01 ([Google](https://developers.google.com/custom-search/v1/overview)). Anthropic's docs never name a provider ([Claude docs](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool)); the Brave relationship rests on a March 2025 subprocessor disclosure quoted by a journalist and has not been re-verified against the live Trust Center, which is client-rendered. Cohere and NVIDIA, the two labs without an index, are the only labs whose first-party material names a third party, and both name Tavily. The third-party vendors' presence at the labs is otherwise confined to plugin marketplaces: Anthropic's official manifest carries `exa`, `tavily`, `firecrawl`, `brightdata-plugin`, `nimble`, `youdotcom-agent-skills` and `context7` among 315 plugins ([marketplace.json](https://raw.githubusercontent.com/anthropics/claude-plugins-official/main/.claude-plugin/marketplace.json)).

### Matrix A — labs and model providers

| Organization | Own / first-party | Brave | Tavily | Exa | Parallel | Perplexity | Linkup | Keenable | You.com | Firecrawl | SERP wrappers | Open / other |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Anthropic** (Claude API, Claude Code, claude.ai) | Default: `web_search` tool, docs provider-silent — docs[^3]; Claude Code `WebSearch` "runs a query against Anthropic's web search backend", unavailable on Bedrock — docs[^4] | **Default backend**: "Subprocessors added: Brave Search" (2025-03-19), schema `BraveSearchParams` — subprocessor via journalist[^1][^2]; Claude Cowork on Bedrock via Brave MCP — press (2026-06-29)[^6] | Marketplace: official plugin + connector — directory[^5], vendor docs[^132] | Marketplace: plugin + connector — directory[^5], vendor docs[^158] | Marketplace: Claude Code plugin — vendor docs[^133] | Marketplace: Claude Code / Desktop MCP — vendor docs[^89] | — | Marketplace: Claude connector — vendor docs[^159] | Marketplace: `youdotcom-agent-skills` — directory[^5] | Marketplace: `firecrawl` plugin — directory[^5] | — | Marketplace: Bright Data, Nimble, Context7 — directory[^5] |
| **OpenAI** (API, Agents SDK, Codex, ChatGPT) | Default: Codex `web_search = "cached"` uses "an OpenAI-maintained index" — docs[^7]; Agents SDK hosted `WebSearchTool` only — docs[^8]; $10/1k — docs[^9] | — | Marketplace: Agent Builder MCP — vendor docs[^11] | Marketplace: Codex/ChatGPT plugin — vendor docs[^10] | Marketplace: MCP in ChatGPT/Codex — vendor docs[^160] | Marketplace: Codex MCP client — vendor docs[^89] | — | Marketplace: OpenAI Plugins Directory — vendor docs[^12] | — | — | — | — |
| **Google** (Gemini API, ADK, Gemini CLI, Antigravity) | Default: Google Search grounding — docs[^13]; ADK `GoogleSearchTool` — code[^14]; Gemini CLI `google_web_search` — docs[^15]; Custom Search API closed, ends 2027-01-01 — docs[^20] | — | — | — | — | Marketplace: Antigravity MCP — vendor docs[^134] | — | Marketplace: Antigravity / Grok plugins — code[^161] | — | — | — | — |
| **Microsoft** (Azure AI Foundry Agents, M365 Copilot) | Default: "Grounding with Bing Search" sole public-web tool — docs[^21]; Bing APIs retired 2025-08-11 — docs[^22] | — | Docs sample: "Azure AI Agent with Tavily MCP Tool Example" — code[^23]; Marketplace: Foundry Tools Catalog, Azure MCP Center — vendor docs[^25]; M365 Copilot declarative agent / Cowork plugin — vendor docs[^24] | — | — | — | — | — | — | — | — | Partner tools are licensed data (Tripadvisor, Morningstar), not web search — docs[^21] |
| **Meta** (Llama Stack) | — | Unverified (registry not fetchable) | Unverified | — | — | — | — | — | — | — | — | Gap |
| **Cohere** | None: generic tool-use docs use a mock tool — docs[^34] | Logo — directory[^39]; Toolkit `Brave_Web_Search` — code[^36] | **Docs default**: sole internet-search tool in "Tools on LangChain" and agentic-RAG cookbook — docs[^34][^35]; Customer — journalist (2025-08-06)[^37], press (2026-02-10)[^38]; Toolkit `Tavily_Web_Search` — code[^36] | — | — | — | — | — | — | — | — | Toolkit `Google_Web_Search`, `Hybrid_Web_Search` — code[^36] |
| **Mistral** | Default: `web_search` / `web_search_premium`, engine undisclosed — docs[^40] | Logo — directory[^39] | — | — | — | — | Vendor-side tutorial — vendor docs[^41] | — | — | — | — | — |
| **xAI** (Grok API, Grok Build) | Default: Web Search $5/1k, X Search — docs[^42] | — | Marketplace: Grok Build — vendor docs[^44] | Marketplace: Grok Build plugin — vendor docs[^43] | — | — | — | Marketplace: `keenable-grok-plugin` — code[^161] | — | — | — | — |
| **DeepSeek** | Default: "in-house search engine", $0.75/1k — docs[^45] | — | — | — | — | — | — | — | — | — | — | — |
| **NVIDIA** (NeMo Agent Toolkit; NVentures) | — | — | **Default package**: `nemo-agent-toolkit-tavily` function group; LangChain `tavily_internet_search` removed in 1.8 — code[^46] | Investor: Series A (2024-07-16), Series B (2025-09-03) — journalist[^47], press[^48] | — | — | — | — | — | — | — | — |
| **IBM** (watsonx, BeeAI) | — | — | Docs sample: watsonx.ai LangGraph-Tavily template — code[^50]; Marketplace: watsonx Orchestrate (Research Agent, Search API) — vendor docs[^51]; Customer — press[^38] | — | — | — | — | — | — | — | — | BeeAI bundles DuckDuckGo tool — code[^52]; Investor in Ceramic.ai — vendor page[^53] |
| **Perplexity** (as lab) | Default: own index; Search API resold by others (see Matrix B) | — | — | — | — | own | — | — | — | — | — | — |

## Clouds and gateways sell menus, not defaults

No hyperscaler names a single third-party default. Google Cloud's Gemini Enterprise Agent Platform documents "Grounding with Parallel web search" and "Grounding with Exa web search" beside Google Search, Maps and Elasticsearch, but both are explicitly **"Separate Offering[s] (as defined in your Google Cloud Agreement)"**: Parallel is bought on Google Cloud Marketplace or with a Parallel key, Exa requires a key "from Exa's web site" and quota goes to support@exa.ai ([Parallel page](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/grounding/grounding-with-parallel); [Exa page](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/grounding/grounding-with-exa)). Gemini Enterprise separately carries a native Tavily connector in Public Preview, evidenced so far only through Tavily's docs citing Google's ([Tavily](https://docs.tavily.com/documentation/integrations/google-gemini-enterprise.md)). Cloudflare's Web Search API (beta, 2026-10-02) resells **Ceramic.ai ($0.25/1k, default), Exa ($7/1k) and Linkup ($5/1k)** "at the provider's list API price, with no additional markup" ([Cloudflare](https://developers.cloudflare.com/changelog/post/2026-10-02-introducing-web-search-api/)). OpenRouter passes native search through for OpenAI, Anthropic, Google, Perplexity and xAI models and defaults everything else to Exa, with Firecrawl, Parallel and Perplexity selectable ([OpenRouter](https://openrouter.ai/docs/guides/features/plugins/web-search)). Vercel's AI Gateway hard-codes `exaSearch`, `parallelSearch` and `perplexitySearch` ([vercel/ai](https://raw.githubusercontent.com/vercel/ai/main/packages/gateway/src/gateway-tools.ts)). AWS is the exception in tone: its first-party Bedrock samples use a Tavily Lambda and AgentCore blueprints call `tavily_search.py`, and AWS Activate discounts Tavily 30%, yet AWS Marketplace also lists Parallel. Nebius is the only cloud that resolved the question by acquisition.

### Matrix B — clouds and inference platforms

| Organization | Own / first-party | Brave | Tavily | Exa | Parallel | Perplexity | Linkup | Keenable | You.com | Firecrawl | SERP wrappers | Open / other |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Google Cloud** (Gemini Enterprise Agent Platform, Gemini Enterprise) | Default: Grounding with Google Search — docs[^16] | — | Built-in option: native connector, Public Preview — vendor docs citing Google[^19][^162] | Built-in option: "Grounding with Exa", Separate Offering, Exa API key — docs[^17]; Private Preview 2026-04-28, Agent Marketplace launch partner — press[^18] | Built-in option: "Grounding with Parallel", Separate Offering, Google Cloud Marketplace — docs[^16], vendor docs[^157] | — | — | — | — | — | — | Elasticsearch grounding — docs[^16] |
| **AWS** (Bedrock, AgentCore, Marketplace, Activate, Kiro) | None; Claude Code `WebSearch` unavailable on Bedrock — docs[^4] | Claude Cowork on Bedrock via Brave MCP — press[^6]; Logo — directory[^39] | **Docs sample**: shared `web_search` Lambda "using the Tavily API" — code[^28]; AgentCore blueprint `tavily_search.py` — code[^29]; Activate "30% off any plan" — code[^30]; Marketplace + AgentCore managed MCP — vendor docs[^31]; Kiro guide — vendor docs[^33]; Logo — directory[^98] | — | Marketplace: AWS Marketplace — vendor docs[^32] | — | — | — | — | — | — | — |
| **Nebius** (Token Factory) | — | — | **Owner** (agreement 2026-02-10) — press[^38]; Token Factory integration — docs[^82] | — | — | — | — | — | — | — | — | — |
| **Cloudflare** (Web Search API, Pay Per Use) | — | — | — | Reseller: $7/1k — docs (2026-10-02)[^75][^76] | — | Excluded from lineup — inferred[^75] | Reseller: $5/1k — docs[^75][^76] | — | Pay Per Use early partner — journalist (2026-07)[^77] | — | — | **Default**: Ceramic.ai $0.25/1k "default when no provider is set" — docs[^76]; Pay Per Use partner — journalist[^77] |
| **Vercel** (AI Gateway, AI SDK, Connect) | — | — | Vendor-side: Vercel Connect — vendor docs[^79] | Built-in option: `exaSearch` gateway tool — code[^78] | Built-in option: `parallelSearch` — code[^78] | Built-in option: `perplexitySearch` — code[^78] | Vendor-side: AI SDK — vendor docs[^80] | — | — | — | — | — |
| **OpenRouter** (web plugin) | Native pass-through for OpenAI, Anthropic, Google, Perplexity, xAI models — docs[^70] | — | — | **Default** "for all other models" — docs[^70], vendor docs[^71]; Customer — press[^49] | Built-in option: engine `parallel` — docs[^70], vendor docs[^163] | Built-in option: engine `perplexity` — docs[^70] | — | — | — | Reseller: OpenRouter-managed key, $0.005/search + $0.0125/result — docs[^70] | — | — |
| **Baseten** (Hosted Tools) | — | — | — | Built-in option — vendor docs[^85] | — | — | Built-in option — vendor docs[^86] | **Built-in option, "first inference-platform partner"** — press (2026-09-16)[^84] | — | — | — | — |
| **Groq** | Default: Compound built-in search, engine undisclosed, decommissioned 2026-09-21 — docs[^61][^62] | — | Customer — journalist[^37], press[^38]; Docs sample "Tavily + Groq" — docs[^64]; MCP launch partner — code[^63] | Docs sample — docs[^64]; MCP launch partner — code[^63] | Docs sample "Parallel + Groq" — docs[^64] | — | — | — | Docs sample — docs[^64] | Docs sample — docs[^64] | — | Browserbase page — docs[^64] |
| **Together AI** | — | Logo — directory[^39] | — | **Docs sample**: TurboSeek "pulls multiple sources from the web using Exa's API" — docs[^65] | — | — | — | — | — | — | — | — |
| **Fireworks** | — | — | — | Vendor-side — vendor docs[^66] | Vendor-side — vendor docs[^67] | — | — | — | — | — | — | — |
| **Cerebras** | — | — | — | Docs sample: integration page + cookbooks — docs[^68] | Docs sample: integration page — docs[^68] | — | Vendor-side — vendor docs[^69] | — | — | — | — | — |
| **SambaNova, FriendliAI, Hugging Face Inference** | — | — | — | — | — | — | Vendor-side — vendor docs[^69] | — | — | — | — | — |
| **Snowflake** (Cortex) | — | Logo — directory[^39] | Marketplace: Snowflake Native App — vendor docs[^55] | Vendor-side: Cortex Agents — vendor docs[^54] | Vendor-side: data integration — vendor docs[^56]; distribution claim — vendor page[^57] | — | — | — | — | — | — | — |
| **Databricks** | — | — | Marketplace: MCP Server on Databricks Marketplace — vendor docs[^59] | Customer (training-set curation, 2024-07-16) — journalist[^47] | — | — | Logo — directory[^58] | — | — | — | — | — |
| **Ollama** | Default: hosted web search API, provider undisclosed — docs[^73] | — | — | — | Vendor-side — vendor docs[^74] | — | — | — | — | — | — | — |
| **Elastic** | — | — | — | — | — | — | — | — | — | — | — | **Owner** of Jina AI (completed 2025-10-09) — press[^83] |

## Frameworks: Tavily is the default wherever a default exists

Across orchestration frameworks the pattern is a menu with a Tavily bias. Where a framework hard-codes one provider, it is Tavily (open_deep_research `default=SearchAPI.TAVILY` with only OpenAI native, Anthropic native or none as alternatives ([configuration.py](https://raw.githubusercontent.com/langchain-ai/open_deep_research/main/src/open_deep_research/configuration.py)); GPT Researcher `"RETRIEVER": "tavily"`; Pydantic AI's two common tools are DuckDuckGo and Tavily; Mastra ships only `@mastra/tavily` and a Perplexity package) or Exa (Letta's `web_search` is "powered by Exa's AI-powered search engine" ([Letta](https://docs.letta.com/guides/agents/web-search)); Onyx lists Exa first). Hugging Face's smolagents is the outlier: its `WebSearchTool` defaults to DuckDuckGo, its `GoogleSearchTool` to SerpApi, and its `ApiWebSearchTool` to Brave ([default_tools.py](https://raw.githubusercontent.com/huggingface/smolagents/main/src/smolagents/default_tools.py)). LangChain is Tavily's anchor relationship — Tavily calls itself "LangChain's recommended search tool", holds four separate tool pages and a partner package, and the LangChain logo sits on tavily.com — yet LangChain also publishes partner packages for Exa, Perplexity, Linkup, Parallel, Jina and Firecrawl and a case study on Exa, while `langchain-brave-search` does not exist on PyPI ([LangChain tools](https://docs.langchain.com/oss/python/integrations/tools)). Serper and SerpApi remain the default "Google results" path in CrewAI, smolagents, n8n and Khoj. AG2 is the one framework whose search docs skip Tavily and DuckDuckGo entirely in favour of Exa, Keenable, Firecrawl and newcomers TinyFish, Glasser and Xquik.

### Matrix C — agent frameworks, orchestration and voice platforms

| Organization | Own / first-party | Brave | Tavily | Exa | Parallel | Perplexity | Linkup | Keenable | You.com | Firecrawl | SERP wrappers | Open / other |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **LangChain / LangGraph** | — | Docs page only; no partner pkg (PyPI 404) — docs[^93], code[^96] | **Default** in open_deep_research — code[^94]; "LangChain's recommended search tool", 4 tool pages, `langchain-tavily` — vendor docs[^92], docs[^95], code[^96]; Logo — directory[^98] | Partner pkg — docs[^95]; case study (2025-06-30) — case study[^97] | Partner pkg — docs[^95]; Logo — directory[^57] | Partner pkg — docs[^95] | Partner pkg — docs[^95] | — | No pkg (PyPI 404) — code[^96] | Partner pkg — docs[^95] | SearchApi, SerpApi listed — docs[^95] | Jina pkg; Octen, Nimble, Search1API, Diffbot, Webz listed — docs[^95] |
| **LlamaIndex** | — | Built-in option: tool-spec pkg — code[^99] | Built-in option — code[^99] | Built-in option — code[^99] | — | — | No pkg (404) — code[^99] | Built-in option — code[^99] | No pkg (404) — code[^99] | — | SearchApi pkg — code[^99] | DuckDuckGo, Bing, Google, Jina, Valyu pkgs — code[^99] |
| **CrewAI** | — | Built-in option — docs[^100] | Built-in option — docs[^100] | Built-in option — docs[^100] | — | — | Built-in option — docs[^100] | — | Built-in option — docs[^100] | — | **Serper listed first, in code example**; SerpApi — docs[^100] | — |
| **AG2** (AutoGen fork) | — | — | — | Built-in option: `ExaToolkit` — docs[^101] | — | Vendor-side — vendor docs[^102] | — | Built-in option: `KeenableSearchToolkit` — docs[^101] | — | Built-in option — docs[^101] | Serply toolkit — docs[^101] | TinyFish, Glasser, Xquik — docs[^101] |
| **Pydantic AI** | — | — | **Built-in common tool** — docs[^103] | — | — | — | — | — | — | — | — | **DuckDuckGo common tool, listed first (keyless)** — docs[^103] |
| **Mastra** | — | — | **Built-in pkg** `@mastra/tavily` (search, extract, crawl, map) — docs[^104] | — | — | Built-in pkg — docs[^104] | — | — | — | — | — | — |
| **Haystack** (deepset) | — | Built-in option — directory[^105] | Built-in option — directory[^105] | Built-in option — directory[^105] | — | Built-in option — directory[^105] | Built-in option — directory[^105] | Built-in option — directory[^105] | — | — | SerperDev, SearchApi, Serpex — directory[^105] | DuckDuckGo, Jina — directory[^105] |
| **smolagents** (Hugging Face) | — | **Default of `ApiWebSearchTool`** — code[^72] | — | `WebSearchTool` engine option — code[^72] | — | — | — | — | — | — | **`GoogleSearchTool` default `serpapi`**, else Serper — code[^72] | **`WebSearchTool` default `duckduckgo`**; Bing option — code[^72] |
| **Agno** | — | Built-in module — code[^106] | Built-in module — code[^106] | Built-in module — code[^106] | Built-in module — code[^106] | Built-in module — code[^106] | Built-in module — code[^106] | — | No module (404) — code[^106] | Built-in module — code[^106] | serpapi, serper — code[^106] | duckduckgo, searxng, baidu, jina, valyu — code[^106] |
| **Letta** | — | — | — | **Default (sole backend)** of `web_search` — docs[^107] | — | — | — | — | — | — | — | — |
| **Semantic Kernel** (Microsoft) | — | Built-in connector `BraveTextSearch` — code[^27] | Built-in connector `TavilyTextSearch` — code[^27] | — | — | — | — | — | — | — | — | Bing, Google documented as out-of-the-box — docs[^26] |
| **Dify** (official plugins) | — | Built-in plugin — code[^108] | Built-in plugin — code[^108] | No plugin (404) — code[^108] | — | Built-in plugin — code[^108] | No plugin; vendor-side guide — code[^108], vendor docs[^164] | — | No plugin (404) — code[^108] | Built-in plugin — code[^108] | Serper, SearchApi — code[^108] | SearXNG, Jina, Google, Bing, DuckDuckGo — code[^108] |
| **n8n** | — | — | Vendor-side guide — vendor docs[^165] | Vendor-side guide — vendor docs[^166] | Vendor-side guide — vendor docs | Built-in node — code[^109] | Vendor-side guide — vendor docs | — | — | — | **Built-in `ToolSerpApi` node** — code[^109] | Built-in `ToolSearXng` node — code[^109] |
| **Flowise** | — | Built-in node — code[^110] | Built-in node — code[^110] | Built-in node — code[^110] | — | — | — | — | — | — | Serper node — code[^110] | — |
| **Langflow** | — | — | Vendor-side (bundle slug 404) — vendor docs[^167] | Built-in bundle — docs[^111] | — | Built-in bundle — docs[^111] | — | — | — | Built-in bundle — docs[^111] | SearchApi bundle — docs[^111] | DuckDuckGo, Bing, Google bundles — docs[^111] |
| **Composio** | — | Toolkit — directory[^112] | Toolkit — directory[^112] | Toolkit — directory[^112] | — | Toolkit — directory[^112] | Toolkit — directory[^112] | — | — | Toolkit — directory[^112] | SerpApi toolkit — directory[^112] | — |
| **IBM BeeAI** | — | — | — | — | — | — | — | — | — | — | — | **Default**: bundled DuckDuckGo tool — code[^52] |
| **NVIDIA NeMo Agent Toolkit** | — | — | **Default package** (see Matrix A) — code[^46] | — | — | — | — | — | — | — | — | — |
| **ElevenLabs Agents** | — | — | Built-in option — docs[^146] | Built-in option — docs[^146], vendor docs[^168] | Built-in option — docs[^146] | Built-in option — docs[^146] | — | — | — | — | — | — |
| **Pipecat** (Daily) | — | — | — | — | — | Built-in LLM service with web search — docs[^147] | — | **Sole "Knowledge Retrieval" service** `KeenableWebSearch` — docs[^147] | — | — | — | — |
| **LiveKit Agents** | — | — | — | — | — | Vendor-side — vendor docs[^148] | — | — | — | — | — | — |
| **Vapi** | — | — | — | — | — | Model provider only (Sonar), no search tool — docs[^149] | — | — | — | — | — | — |
| **Browser Use** | — | — | — | — | Reverse direction: Parallel tasks call Browser Use MCP — vendor docs[^113] | — | — | — | — | — | — | — |

## Coding agents route through their maker's index; independents pick Tavily or Exa

The three first-party coding agents inherit their lab's search and bolt on marketplaces: Claude Code's `WebSearch` hits "Anthropic's web search backend" with a 200-call session cap and no Bedrock availability ([Claude Code](https://code.claude.com/docs/en/tools)); Codex defaults to a cached OpenAI index and only goes `live` under `--yolo` ([Codex config](https://learn.chatgpt.com/docs/config-file/config-reference)); Gemini CLI ships `google_web_search` ([Gemini CLI](https://raw.githubusercontent.com/google-gemini/gemini-cli/main/docs/tools/web-search.md)). Codex's cached default and Zed's Pro-only gate are precisely where Keenable, Parallel and Exa publish client-specific setup. Among independents, **OpenHands documents Tavily as its only engine and says it "is configured as a search engine by default in OpenHands Cloud"** ([OpenHands](https://docs.all-hands.dev/usage/search-engine-setup)); goose's official docs tutorial adds Tavily as an extension ([goose](https://raw.githubusercontent.com/block/goose/main/documentation/docs/mcp/tavily-mcp.md)); OpenClaw prompts users for a Brave key, which Brave converted into "nearly 700,000 OpenClaw users" by April 2026 ([Brave](https://brave.com/blog/openclaw/)). Cursor is the most consequential unknown: Exa names Cursor as a customer in two funding posts, third parties call Exa Cursor's @Web backend, but Cursor's docs name nobody and its subprocessor list sits behind an unreadable trust portal ([Cursor security](https://cursor.com/security)). Windsurf was a You.com API customer before Cognition absorbed it; Devin's enterprise web-search toggle names no provider.

### Matrix D — coding agents, IDEs and harnesses

| Organization | Own / first-party | Brave | Tavily | Exa | Parallel | Perplexity | Linkup | Keenable | You.com | Firecrawl | SERP wrappers | Open / other |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Claude Code** (Anthropic) | Default: `WebSearch` → Anthropic backend; 200 calls/session; not on Bedrock — docs[^4] | Backend per subprocessor list — subprocessor via journalist[^1] | Marketplace: official plugin — vendor docs[^132] | Marketplace — directory[^5] | Marketplace — vendor docs[^133] | Marketplace — vendor docs[^89] | — | Marketplace — vendor docs[^159] | Marketplace — directory[^5] | Marketplace — directory[^5] | — | Bright Data, Nimble — directory[^5] |
| **Codex** (OpenAI) | Default: `cached` OpenAI index; `live` under `--yolo` — docs[^7] | — | — | Marketplace: "Exa in Codex and ChatGPT" — vendor docs[^10] | Marketplace: MCP — vendor docs[^160] | Marketplace: MCP client — vendor docs[^89] | — | Marketplace: setup requires `web_search = "disabled"` — vendor docs[^159] | — | — | — | — |
| **Gemini CLI / Antigravity** (Google) | Default: `google_web_search` — docs[^15] | — | — | — | — | Marketplace: Antigravity MCP — vendor docs[^134] | — | Marketplace: Antigravity plugin — code[^161] | — | — | — | — |
| **Cursor** | @Web backend undisclosed — docs[^123]; subprocessors unreadable — docs[^124] | — | Marketplace: "Add to Cursor" — vendor docs[^125] | **Customer** (Series B 2025-09-03, Series C 2026-05-20) — press[^48][^49]; @Web backend = Exa — **inferred**[^144] | Marketplace: Cursor plugin — vendor docs[^126] | Marketplace: MCP — vendor docs[^169] | — | — | — | — | — | — |
| **Windsurf** (Codeium → Cognition) | Cascade now "legacy" — docs[^127] | — | — | — | — | MCP client — vendor docs[^89] | — | — | **Customer** — press (vendor, 2025-09)[^60] | — | — | — |
| **Cognition / Devin** | Enterprise "Enable Web Search" names no provider — docs[^129] | — | Vendor-side guide — vendor docs[^128] | **Customer** — press (2026-05-20)[^49] | — | — | — | — | — | — | — | — |
| **Zed** | Default: `zed.dev` provider, backend undisclosed, Zed Pro only; MCP otherwise — code[^130], docs[^131] | — | — | — | — | — | — | — | — | — | — | — |
| **OpenHands** (All Hands) | — | — | **Default**: sole documented engine; default in OpenHands Cloud — docs[^136] | — | — | — | — | — | — | — | — | — |
| **goose** (Block) | — | — | **Docs sample**: official MCP tutorial — docs[^135] | — | — | — | — | — | — | — | — | — |
| **OpenClaw** | — | **Default key prompt** — practitioner (2026-01-30)[^141]; ~700k users — press (2026-04-01)[^140] | Vendor-side — vendor docs[^81] | Vendor-side — vendor docs[^170] | Vendor-side: ClawHub — vendor docs[^138] | Vendor-side — vendor docs[^89] | — | — | — | — | — | — |
| **Hermes Agent** | — | Sign-ups counted with OpenClaw — directory[^39] | **Built-in keyless default** — vendor docs[^90] | Vendor-side — vendor docs[^139] | — | Vendor-side — vendor docs[^89] | — | — | — | — | — | — |
| **OpenCode** | — | — | Vendor-side — vendor docs[^137] | — | Vendor-side plugin — vendor docs[^172] | Vendor-side — vendor docs[^89] | — | — | — | — | — | — |
| **Kiro** (AWS) | Docs silent — docs[^173] | — | Vendor-side — vendor docs[^33] | — | — | — | — | — | — | — | — | — |
| **Cline** | No built-in provider; MCP — docs[^174] | — | — | — | — | — | — | — | — | — | — | — |
| **Kilo, Factory AI, Replit** | — | — | Vendor-side — vendor docs[^81] | — | Replit logo — directory[^57] | — | — | — | — | — | — | — |
| **Continue, Roo Code, Aider** | — | — | — | — | — | — | — | — | — | — | — | Nothing found |

## Agent products surface mostly as customers in vendor press

Enterprise and consumer products rarely document their search supplier; the evidence is vendor press and logo walls, which rank below first-party docs. The one product with a vendor-published exclusive is **Firefox: "Exa powers Smart Window on Firefox desktop as well as Quick Answers on Firefox for iOS… Firefox picked Exa after a thorough evaluation"** (2026-08-17, [Exa](https://exa.ai/blog/exa-firefox)). Exa's funding posts name Cursor, Notion AI, Cognition, HubSpot, OpenRouter and Monday.com ([Series C](https://exa.ai/blog/announcing-series-c)); You.com names DuckDuckGo, Windsurf and Harvey as API customers behind "over 1 billion queries monthly" ([You.com](https://you.com/articles/series-c)); TechCrunch names Groq, Cohere, MongoDB and Writer as Tavily customers ([TechCrunch](https://techcrunch.com/2025/08/06/tavily-raises-25m-to-connect-ai-agents-to-the-web/)). Parallel's logo wall (Granola, Lovable, Harvey, Notion, Pfizer, LangChain, Modal, Replit, Profound, Rogo) and Linkup's (EY, Die Bundesregierung, McKinsey, Databricks, KPMG, Legora) overlap with competitors' customer lists — Notion and Harvey appear on two vendors' pages each — which is itself evidence that products multi-source.

### Matrix E — agent products and enterprises

| Organization | Own / first-party | Brave | Tavily | Exa | Parallel | Perplexity | Linkup | Keenable | You.com | Firecrawl | SERP wrappers | Open / other |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Mozilla Firefox** | — | — | — | **Default (sole)**: Smart Window, Quick Answers; `/search` endpoint, no query retention — press (2026-08-17)[^87] | — | — | — | — | — | — | — | — |
| **Notion AI** | — | — | — | Customer — press (2025-09-03)[^48] | Logo — directory[^57] | — | — | — | — | — | — | — |
| **HubSpot, Monday.com** | — | — | — | Customer — press (2026-05-20)[^49] | — | — | — | — | — | — | — | — |
| **Harvey** | — | — | — | — | Logo — directory[^57] | — | — | — | Customer — press[^60] | — | — | — |
| **Writer, MongoDB** | — | — | Customer — journalist (2025-08-06)[^37]; Writer logo — directory[^98] | — | — | — | — | — | — | — | — | — |
| **Lovable** | — | — | — | Customer — analyst[^144] | Logo — directory[^57] | — | Vendor-side page — vendor docs[^143] | — | — | — | — | — |
| **Granola, Superhuman, Modal, Profound, Rogo, Pfizer** | — | — | — | — | Logo — directory[^57]; Superhuman integration — vendor docs[^142] | — | — | — | — | — | — | — |
| **EY, McKinsey, KPMG, Legora, Die Bundesregierung** | — | — | — | — | — | — | Logo — directory[^58] | — | — | — | — | — |
| **DuckDuckGo** | Own front end | — | — | — | — | — | — | — | Customer — press[^60] | — | — | Bing access retained after API retirement — journalist (2025-05-15)[^88] |
| **Kagi, Shopify, Firecrawl, You.com** (as Brave customers) | — | Logo (index resale) — directory[^39] | — | — | — | — | — | — | — | — | — | — |
| **Vellum, Merge Gateway** | — | — | Built-in provider — vendor docs[^91] | — | — | — | — | — | — | — | — | — |
| **Zapier, Make, Workato, Tines, StackAI, Arcade.dev, Scalekit, TrueFoundry** | — | — | Vendor-side — vendor docs[^81] | TrueFoundry — vendor docs[^81] | Zapier — vendor docs[^145] | — | Zapier — vendor docs | — | — | — | — | — |
| **Browserbase** | — | — | — | Vendor-side — vendor docs[^150] | — | — | — | — | — | — | — | Groq doc page — docs[^64] |

### Matrix F — open deep-research projects and chat UIs

| Project | Own / first-party | Brave | Tavily | Exa | Parallel | Perplexity | Linkup | Keenable | You.com | Firecrawl | SERP wrappers | Open / other |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **open_deep_research** (LangChain) | — | — | **Default** `SearchAPI.TAVILY`; alternatives only OpenAI native, Anthropic native, None — code[^94] | — | — | — | — | — | — | — | — | — |
| **GPT Researcher** (Tavily's origin project) | — | — | **Default** `"RETRIEVER": "tavily"` — code[^114] | — | — | — | — | — | — | — | — | — |
| **Khoj** | — | — | — | Second priority (`EXA_API_KEY`) — code[^115] | — | — | — | — | — | Third priority — code[^115] | **Serper first** — code[^115] | Google PSE, SearXNG — code[^115] |
| **Perplexica / Vane** | — | — | "coming soon" — code[^116] | "coming soon" — code[^116] | — | — | — | — | — | — | — | **Default (sole)**: SearXNG — code[^116] |
| **Morphic** | — | Built-in option — code[^117] | Built-in option; **required for Vercel deploy** — code[^117] | Built-in option — code[^117] | — | — | — | — | — | — | — | SearXNG bundled in Docker — code[^117] |
| **Open WebUI** | — | Built-in (incl. LLM Context) — code[^118] | Built-in — code[^118] | Built-in — code[^118] | — | Built-in — code[^118] | Built-in — code[^118] | — | Built-in (`ydc`) — code[^118] | Built-in — code[^118] | serpapi, serper, searchapi, serply, serphouse, serpstack — code[^118] | SearXNG, Google PSE, Bing, Azure, Kagi, Mojeek, Bocha, Jina, DuckDuckGo, Yandex, YaCy, Sougou, Ollama, Microsoft Web IQ, Staan, OpenSERP — code[^118] |
| **AnythingLLM** | — | Built-in — code[^119] | Built-in — code[^119] | Built-in — code[^119] | — | Built-in — code[^119] | — | — | — | — | serpapi, searchapi, serper — code[^119] | Google PSE, Bing, DuckDuckGo, SearXNG — code[^119] |
| **LibreChat** | — | — | Built-in; example `searchProvider: tavily` — code[^120] | — | — | — | — | Built-in; example `searchProvider: keenable` — code[^120] | — | Built-in scraper — code[^120] | Serper — code[^120] | SearXNG; Jina and Cohere rerankers — code[^120] |
| **Onyx** | Own crawler option — docs[^121] | Built-in — docs[^121] | Built-in (search + crawl) — docs[^121] | **Built-in, listed first** (search + crawl) — docs[^121] | — | — | — | — | — | Built-in (search + crawl) — docs[^121] | Serper — docs[^121] | Google PSE, SearXNG — docs[^121] |
| **SurfSense** | README names no search API — code[^122] | — | — | — | — | — | Vendor-side page — vendor docs[^122] | — | — | — | — | — |

## Per-provider ledger: who each vendor has taken

The ledger below collapses the matrices by provider. "Taken" means a default, sole backend, acquirer or reseller slot; named customers and logos are listed separately because they do not imply exclusivity. Tavily has the most defaults and the only acquirer; Exa has the most platform-grade placements and the most press-named customers; Parallel has no default anywhere but the broadest "second option" footprint among hyperscalers; Brave's footprint is the least visible in documentation and the largest by implied query volume (Anthropic plus OpenClaw).

| Provider | Defaults / sole backends (date) | Resellers, marketplaces, grounding options | Acquirer / investors | Named customers (press or journalist) | Logo-only or vendor-asserted |
|---|---|---|---|---|---|
| **Tavily** | Cohere docs sole search tool (obs.)[^34]; NVIDIA NeMo dedicated package (1.8, obs.)[^46]; AWS Bedrock shared sample + AgentCore blueprint (obs.)[^28][^29]; Azure-Samples MCP (obs.)[^23]; IBM watsonx template (obs.)[^50]; open_deep_research default (obs.)[^94]; GPT Researcher default (obs.)[^114]; OpenHands Cloud default (obs.)[^136]; Pydantic AI common tool (obs.)[^103]; Mastra package (obs.)[^104]; Morphic Vercel deploy (obs.)[^117]; goose tutorial (obs.)[^135] | Google Gemini Enterprise native connector, Public Preview[^19]; Azure AI Foundry Tools Catalog, Azure MCP Center[^25]; M365 Copilot[^24]; AWS Marketplace + AgentCore managed MCP[^31]; AWS Activate 30% off[^30]; Databricks Marketplace[^59]; Snowflake Native App[^55]; IBM watsonx Orchestrate[^51]; Claude plugin marketplace[^5]; OpenAI Agent Builder[^11]; Grok Build[^44]; Nebius Token Factory[^82] | **Nebius acquired** (agreement 2026-02-10; price undisclosed by Nebius, ~$275M per Bloomberg via Sacra)[^38][^151] | Groq, Cohere, MongoDB, Writer (TechCrunch 2025-08-06)[^37]; IBM, Cohere, Groq (Nebius 2026-02-10)[^38] | LangChain "recommended search tool"[^92]; Hermes Agent keyless default[^90]; Vellum, Merge Gateway built-in[^91]; logos AWS, IBM, Groq, Writer, LangChain[^98] |
| **Exa** | OpenRouter default for non-native models (obs.)[^70]; Letta sole backend (obs.)[^107]; Firefox Smart Window / Quick Answers (2026-08-17)[^87]; Together AI TurboSeek tutorial (obs.)[^65]; Onyx listed first (obs.)[^121] | Google Cloud "Grounding with Exa", Separate Offering (Private Preview 2026-04-28)[^17][^18]; Gemini Enterprise Agent Marketplace launch partner[^18]; Cloudflare resale $7/1k (2026-10-02)[^75]; Vercel AI Gateway `exaSearch`[^78]; Baseten Hosted Tools[^85]; Cerebras integration + cookbooks[^68]; Claude plugin marketplace[^5]; Codex/ChatGPT plugin[^10]; Grok Build[^43]; Groq MCP launch partner[^63] | NVIDIA NVentures (Series A 2024-07-16; Series B 2025-09-03)[^47][^48] | Databricks (2024-07-16)[^47]; Cursor, Notion AI (2025-09-03)[^48]; Cursor, Cognition, HubSpot, OpenRouter, Monday.com (2026-05-20)[^49]; LangChain case study (2025-06-30)[^97] | Cursor @Web backend (inferred)[^144]; Lovable, Vercel v0 (analyst)[^144]; Fireworks, Snowflake, Browserbase, ElevenLabs integration pages[^66][^54][^150][^168] |
| **Parallel** | None found | Google Cloud "Grounding with Parallel", Separate Offering, Google Cloud Marketplace (obs.)[^16][^157]; AWS Marketplace[^32]; OpenRouter engine[^70]; Vercel AI Gateway `parallelSearch`[^78]; Cerebras integration[^68]; ElevenLabs[^146]; Claude Code, Cursor, OpenCode plugins[^133][^126][^172] | Kleiner Perkins, Index (Series A $100M, 2025-11-12)[^155]; Sequoia (Series B $100M at $2B, 2026-04-29)[^154] | Notion and "major banks" (journalist, 2026-04-29)[^154] | Logos Granola, Lovable, Harvey, Notion, Pfizer, LangChain, Modal, Replit, Profound, Rogo[^57]; distribution "Google Cloud, OpenRouter, Vercel, Snowflake"[^57]; Superhuman page[^142] |
| **Brave** | Anthropic web search backend (subprocessor added 2025-03-19)[^1][^2]; OpenClaw default key prompt (2026-01-30)[^141]; smolagents `ApiWebSearchTool` default (obs.)[^72] | Claude Cowork on Bedrock via Brave MCP (2026-06-29)[^6]; Semantic Kernel, Cohere Toolkit, Flowise, LlamaIndex, Haystack, CrewAI, Dify, Agno, Composio, Open WebUI, AnythingLLM, Onyx, Morphic connectors[^27][^36][^110][^99][^105][^100][^108][^106][^112][^118][^119][^121][^117] | — | — | Logos AWS, Cohere, Mistral AI, Snowflake, You.com, Firecrawl, Kagi, Shopify, Together.ai[^39]; "nearly 700,000 OpenClaw users" (2026-04-01)[^140]; "1 million+" OpenClaw and Hermes sign-ups[^39] |
| **Perplexity (Search API)** | Own products only | OpenRouter engine[^70]; Vercel AI Gateway `perplexitySearch`[^78]; Mastra package[^104]; ElevenLabs[^146]; Pipecat LLM service[^147]; n8n node[^109]; Dify plugin[^108]; MCP clients Claude Code, Cursor, VS Code, Antigravity, Claude Desktop, Windsurf, Codex[^89] | — | — | Excluded from Cloudflare's reseller lineup (inferred)[^75]; LiveKit, AG2 vendor-side[^148][^102] |
| **Linkup** | None found | Cloudflare resale $5/1k (2026-10-02)[^75]; Baseten Hosted Tools[^86]; CrewAI, Haystack, Agno, Composio, Open WebUI, LangChain pkg[^100][^105][^106][^112][^118][^95] | Gradient ($10M seed, Feb 2026; aggregator-sourced)[^175] | — | Logos EY, Die Bundesregierung, McKinsey, Databricks, KPMG, Legora[^58]; Mistral, Cerebras, SambaNova, FriendliAI, Hugging Face, Lovable, SurfSense, Dify, n8n, Vercel pages[^41][^69][^143][^122][^164][^80] |
| **Keenable** | Pipecat sole "Knowledge Retrieval" service (obs.)[^147] | Baseten Hosted Tools, "first inference-platform partner" (2026-09-16)[^84]; LlamaIndex pkg[^99]; AG2 toolkit[^101]; Haystack[^105]; LibreChat example[^120]; Claude connector, OpenAI Plugins Directory, Codex, Antigravity, Grok Build[^159][^12][^161] | Accel ($26M seed, 2026-08-25), Conviction[^153] | "in production at several AI labs and inference providers" — unnamed (journalist)[^153] | — |
| **You.com** | None found | Cloudflare Pay Per Use early partner (2026-07)[^77]; Claude plugin `youdotcom-agent-skills`[^5]; Groq doc page[^64]; CrewAI[^100]; Open WebUI `ydc`[^118] | Cox Enterprises, Georgian, Salesforce Ventures, Norwest (Series C, 2025-09)[^60]; acquired Graft (Oct 2025, aggregator)[^156] | DuckDuckGo, Windsurf, Harvey (vendor press)[^60] | Also a Brave API customer (logo)[^39] |
| **Firecrawl** | None (scraper role) | OpenRouter engine on OpenRouter-managed key, $0.005/search + $0.0125/result[^70]; Claude plugin marketplace[^5]; LangChain, Agno, Dify, Langflow, Composio, Onyx, Khoj, LibreChat scraper[^95][^106][^108][^111][^112][^121][^115][^120] | Smash Capital (Series B $75M, 2026-09-22)[^176] | — | Brave API customer (logo)[^39] |
| **Ceramic.ai** | Cloudflare Web Search API default, $0.25/1k (2026-10-02)[^76] | Cloudflare Pay Per Use early partner (2026-07)[^77] | NEA, Earthshot, IBM, Samsung Next, Mento (vendor page)[^53] | — | — |
| **Jina AI** | — | LangChain, LlamaIndex, Agno, Dify, Haystack, Open WebUI; LibreChat reranker[^95][^99][^106][^108][^105][^118][^120] | **Elastic acquired** (completed 2025-10-09)[^83] | — | — |
| **Serper / SerpApi / SearchApi** | CrewAI first-listed with code example (obs.)[^100]; smolagents `GoogleSearchTool` default serpapi (obs.)[^72]; Khoj first priority (obs.)[^115]; n8n `ToolSerpApi` node (obs.)[^109] | LibreChat, Open WebUI, AnythingLLM, Onyx, Flowise, Dify, Haystack, Composio, LlamaIndex, LangChain[^120][^118][^119][^121][^110][^108][^105][^112][^99][^95] | — | — | — |
| **DuckDuckGo / SearXNG** | smolagents `WebSearchTool` default (obs.)[^72]; Pydantic AI first common tool (obs.)[^103]; IBM BeeAI bundled tool (obs.)[^52]; Perplexica/Vane sole (obs.)[^116]; Morphic Docker bundle (obs.)[^117] | Open WebUI, AnythingLLM, LibreChat, Onyx, Dify, Agno, Haystack, LlamaIndex, n8n[^118][^119][^120][^121][^108][^106][^105][^99][^109] | — | — | — |
| **Bing / Google Search (first-party)** | Azure AI Foundry sole grounding[^21]; Gemini API, ADK, Gemini CLI[^13][^14][^15]; DuckDuckGo retained Bing access[^88] | Semantic Kernel, Cohere Toolkit, smolagents, Dify, Langflow, Open WebUI PSE, AnythingLLM, Onyx[^26][^36][^72][^108][^111][^118][^119][^121] | — | — | — |

## Exclusivity: a handful of locked doors and dozens of open ones

Genuine single-provider relationships cluster in three places: ownership, consumer-facing products that need one answer, and small agent projects that ship a default. Every distribution platform hedges. Google's choice to list Parallel and Exa side by side, Vercel's three gateway tools, Cloudflare's three resold providers, OpenRouter's five engines, Baseten's three hosted tools and Anthropic's seven marketplace vendors all point the same way: platforms treat search as a commodity slot and let the buyer choose. The labs' own-index strategy has a cost that is now visible in the ecosystem — Codex's cached default and Zed's Pro-only gate are exactly where Keenable, Parallel and Exa publish client-specific setup, and Claude Code's `WebSearch` being unavailable on Bedrock is why Brave markets a Cowork-on-Bedrock MCP. Where the labs do name a third party in first-party material, it is always a sample or template rather than a shipped default, with two exceptions: Cohere, whose docs and cookbooks wire only Tavily and whose Toolkit source nonetheless carries Tavily, Google and Brave; and NVIDIA, whose NeMo Agent Toolkit removed the generic LangChain search tool and replaced it with a Tavily-specific package.

| Organization | Status | Provider(s) | Basis |
|---|---|---|---|
| Anthropic (Claude, Claude Code) | **Single default (backend)**; multi-homed at plugin layer | Brave underneath; 7 marketplace vendors on top | subprocessor via journalist (2025-03-19), directory (obs.)[^1][^5] |
| OpenAI (Codex, Agents SDK, ChatGPT) | **Own build**; multi-homed at plugin layer | Own index; Exa, Tavily, Parallel, Keenable, Perplexity plugins | docs, vendor docs[^7][^8] |
| Google (Gemini API, ADK, CLI) | **Own build** | Google Search | docs, code[^13][^14] |
| Google Cloud (Gemini Enterprise Agent Platform) | **Multi-homed** | Google Search + Parallel + Exa (Separate Offerings) + Tavily connector + Elasticsearch | docs[^16][^17][^19] |
| Microsoft (Azure AI Foundry) | **Own build** (Bing); Tavily only in samples and catalog | Bing | docs[^21][^23] |
| xAI, DeepSeek, Perplexity | **Own build** | Own indexes | docs[^42][^45] |
| Mistral, Groq, Ollama, Zed | **Own tool, undisclosed backend** | Unnamed | docs[^40][^61][^73][^131] |
| Cohere | **Single docs default**; Toolkit multi-homed | Tavily (docs); Tavily/Google/Brave (Toolkit) | docs, code[^34][^36] |
| NVIDIA NeMo Agent Toolkit | **Single default package** | Tavily | code[^46] |
| AWS | **Single sample default**, multi-homed marketplace | Tavily (samples, Activate); Parallel (Marketplace); Brave (Cowork MCP) | code, vendor docs, press[^28][^32][^6] |
| Nebius | **Owner** | Tavily | press[^38] |
| Elastic | **Owner** | Jina AI | press[^83] |
| Cloudflare | **Multi-homed with default** | Ceramic (default), Exa, Linkup | docs[^76] |
| OpenRouter | **Multi-homed with default** | Exa (default), Firecrawl, Parallel, Perplexity, native | docs[^70] |
| Vercel AI Gateway | **Multi-homed** | Exa, Parallel, Perplexity | code[^78] |
| Baseten Hosted Tools | **Multi-homed** | Keenable (first), Exa, Linkup | press, vendor docs[^84][^85][^86] |
| Cerebras, Fireworks, Together, Snowflake, Databricks, IBM | **Multi-homed** (two to four vendor pages each) | Exa/Parallel/Linkup; Tavily/Exa/Parallel; Tavily/Exa/Linkup; Tavily/DuckDuckGo/Ceramic | docs, vendor docs[^68][^65][^55][^59][^50] |
| LangChain | **Single default in open_deep_research**; integrations multi-homed | Tavily default; 7 partner packages | code, docs[^94][^95] |
| GPT Researcher, OpenHands, Hermes Agent, Vellum, Merge Gateway | **Single default** | Tavily | code, docs, vendor docs[^114][^136][^90][^91] |
| Letta, Firefox | **Single default (sole backend)** | Exa | docs, press[^107][^87] |
| Pipecat | **Single listed knowledge-retrieval service** | Keenable | docs[^147] |
| Pydantic AI, Mastra | **Two shipped** | DuckDuckGo + Tavily; Tavily + Perplexity | docs[^103][^104] |
| smolagents | **Three defaults by tool class** | DuckDuckGo, SerpApi, Brave | code[^72] |
| Perplexica/Vane, IBM BeeAI | **Single default (open engine)** | SearXNG; DuckDuckGo | code[^116][^52] |
| LlamaIndex, CrewAI, AG2, Haystack, Agno, Dify, n8n, Flowise, Langflow, Composio, Semantic Kernel | **Multi-homed menus** (4–14 providers) | Tavily, Exa, Brave, Serper/SerpApi most frequent | code, docs, directory[^99][^100][^101][^105][^106][^108][^109][^110][^111][^112][^27] |
| Open WebUI, AnythingLLM, LibreChat, Onyx, Morphic, Khoj | **Multi-homed menus** (4–30 engines) | No provider default; Open WebUI 30+ | code, docs[^118][^119][^120][^121][^117][^115] |
| Cursor | **Inferred single backend**; multi-homed plugins | Exa (inferred); Tavily, Parallel, Perplexity plugins | press, inferred, vendor docs[^49][^144][^125] |
| Windsurf (legacy), Devin | **Single customer relationship, backend unknown** | You.com (Windsurf); Exa customer (Cognition) | press[^60][^49] |
| OpenClaw | **Single default key prompt**; vendor pages for five others | Brave | practitioner, press[^141][^140] |
| ElevenLabs Agents | **Multi-homed** | Exa, Parallel, Perplexity, Tavily | docs[^146] |

## Acquisitions, investments and resale channels

Strategic money has come from infrastructure and cloud players rather than the labs: Nebius bought Tavily, Elastic bought Jina, NVIDIA invested in Exa, IBM in Ceramic, Salesforce Ventures in You.com. Resale is where the real routing decisions are made — Cloudflare passing through list prices for three providers, OpenRouter holding a managed Firecrawl key with its own per-result pricing, Google Cloud selling Parallel through its Marketplace while Exa stays bring-your-own-key, and Baseten, Vercel and the three enterprise data clouds hosting two or three vendors each.

| Date | Party | Counterparty | Type | Terms / scope | Evidence |
|---|---|---|---|---|---|
| 2024-07-16 | NVIDIA (NVentures), Lightspeed, Y Combinator | Exa | Investment | $17M Series A; Databricks named as customer | journalist[^47] |
| 2025-03-19 | Anthropic | Brave Search | Subprocessor | "Subprocessors added: Brave Search"; schema `BraveSearchParams` | subprocessor via journalist (2025-03-21)[^1][^2] |
| 2025-08-06 | Tavily investors | Tavily | Investment | $25M; customers Groq, Cohere, MongoDB, Writer | journalist[^37] |
| 2025-09 | Cox Enterprises, Georgian, Salesforce Ventures, Norwest | You.com | Investment | $100M Series C at $1.5B; API customers DuckDuckGo, Windsurf, Harvey | press (vendor)[^60] |
| 2025-09-03 | Benchmark, NVentures | Exa | Investment | $85M Series B at $700M; customers Cursor, Notion AI | press (vendor)[^48] |
| 2025-10-09 | Elastic | Jina AI | **Acquisition (completed)** | Jina's models continue on Hugging Face and Elastic Inference Service | press[^83] |
| Oct 2025 | You.com | Graft | Acquisition (team and technology) | — | aggregator[^156] |
| 2025-11-12 | Kleiner Perkins, Index Ventures, Khosla | Parallel | Investment | $100M Series A at ~$740M | journalist[^155] |
| 2026-02-10 | Nebius | Tavily | **Acquisition (agreement)** | Price undisclosed by Nebius; ~$275M per Bloomberg via Sacra; ~30 staff; brand retained; Token Factory integration | press[^38]; journalist[^151][^152] |
| Feb 2026 | Gradient | Linkup | Investment | $10M seed (aggregator-sourced; primary release unreachable) | aggregator[^175] |
| 2026-04-28 | Google Cloud | Exa | Grounding option (Separate Offering) + Agent Marketplace launch partner | "Grounding with Exa" Private Preview; Exa API key required; quota via Exa support | docs[^17]; press (vendor)[^18] |
| obs. 2026-11-05 | Google Cloud | Parallel | Grounding option (Separate Offering) + Marketplace | "Subscribe directly to Grounding with Parallel Web Search on Google Cloud Marketplace" or existing Parallel key | docs[^16]; vendor docs[^157] |
| obs. 2026-11-05 | Google (Gemini Enterprise) | Tavily | Native connector | Public Preview; web search, extract, crawl, research | vendor docs citing Google[^19][^162] |
| 2026-04-29 | Sequoia | Parallel | Investment | $100M Series B at $2B | journalist[^154] |
| 2026-05-20 | a16z and others | Exa | Investment | $250M Series C at $2.2B; customers Cursor, Cognition, HubSpot, OpenRouter, Monday.com | press (vendor)[^49] |
| 2026-06-29 | Brave | Anthropic / AWS | Integration | Claude Cowork on Amazon Bedrock with Brave Search MCP | press (vendor)[^6] |
| 2026-07 | Cloudflare | Ceramic.ai, You.com | Pay Per Use early partners | Publisher-compensation program | journalist[^77] |
| 2026-08-17 | Mozilla Firefox | Exa | Supply deal | Smart Window (desktop), Quick Answers (iOS); `/search` endpoint; Exa retains no query data | press (vendor)[^87] |
| 2026-08-25 | Accel, Conviction | Keenable | Investment | $26M seed; "in production at several AI labs" (unnamed) | journalist[^153] |
| 2026-09-16 | Baseten | Keenable | Hosted Tools partner | "Baseten is our first inference-platform partner" | press (vendor)[^84] |
| obs. 2026-11-05 | Baseten | Exa, Linkup | Hosted Tools providers | Web search providers in Baseten Hosted Tools | vendor docs[^85][^86] |
| 2026-09-22 | Smash Capital, Altos, Nexus, YC | Firecrawl | Investment | $75M Series B; Alexandria indexes | press (vendor)[^176] |
| 2026-10-02 | Cloudflare | Ceramic.ai, Exa, Linkup | **Reseller (Web Search API beta)** | List price, no markup: Ceramic $0.25/1k (default, ZDR), Exa $7/1k, Linkup $5/1k | docs[^75][^76] |
| obs. 2026-11-05 | OpenRouter | Exa, Firecrawl, Parallel, Perplexity | Reseller / engine menu | Exa default for non-native models; Firecrawl on OpenRouter-managed key at $0.005/search + $0.0125/result | docs[^70] |
| obs. 2026-11-05 | Vercel | Exa, Parallel, Perplexity | Gateway tools | `exaSearch`, `parallelSearch`, `perplexitySearch` in `@ai-sdk/gateway` | code[^78] |
| obs. 2026-11-05 | AWS | Tavily; Parallel | Marketplace + managed MCP; Marketplace; Activate | Tavily MCP on AWS Marketplace and AgentCore; Parallel on AWS Marketplace; Tavily "30% off any plan - for 6 months" | vendor docs[^31][^32]; code[^30] |
| obs. 2026-11-05 | Microsoft | Tavily | Catalog listings | Azure AI Foundry Tools Catalog; Azure MCP Center; M365 Copilot declarative agent and Cowork plugin | vendor docs[^25][^24] |
| obs. 2026-11-05 | Databricks, Snowflake, IBM | Tavily (all three); Exa, Parallel (Snowflake) | Marketplace / native app | Databricks Marketplace MCP; Snowflake Native App; watsonx Orchestrate | vendor docs[^59][^55][^51][^54][^56] |
| obs. 2026-11-05 | Anthropic | Exa, Tavily, Firecrawl, Bright Data, Nimble, You.com, Context7 | Official plugin marketplace | 7 web-data vendors among 315 plugins | code (manifest)[^5] |
| obs. 2026-11-05 | xAI | Exa, Tavily, Keenable | Grok Build marketplace | Plugins | vendor docs, code[^43][^44][^161] |
| obs. 2026-11-05 | IBM | Ceramic.ai | Investment | Amount undisclosed | vendor page[^53] |

## Open gaps

The map's weakest joints are the places where a compliance document, not a docs page, would settle the question. Anthropic's live Trust Center is client-rendered and could not be read, so whether Brave still powers Claude in November 2026 rests on March 2025 reporting. Cursor's subprocessor list sits behind an unreadable trust portal, leaving the single most-cited "Exa powers X" claim as an inference. Groq, Mistral, Ollama and Zed sell built-in search without naming a backend, and Groq's simultaneous status as a Tavily customer and Exa/Tavily MCP launch partner ties neither to its decommissioned Compound search.

| Gap | Why it matters | What would close it |
|---|---|---|
| Anthropic's current subprocessor list (trust.anthropic.com unreadable) | Only lab-to-vendor backend relationship; status is 2025-03 | A readable Trust Center export or a 2026 subprocessor notice[^1] |
| Cursor @Web backend | Largest coding-agent query stream outside the labs; Exa link is inferred | Cursor trust-portal subprocessor list[^124] |
| Groq Compound, Mistral `web_search`, Ollama web search, Zed `zed.dev` backends | Four built-in tools with undisclosed suppliers | Subprocessor lists or engineering posts[^61][^40][^73][^130] |
| Meta Llama Stack tool-runtime providers (historically brave-search, tavily-search, bing-search) | Only major lab framework not mapped | Registry fetch (docs 404, GitHub API blocked this session) |
| Google's own Tavily connector page and the GA/Preview stage of Exa and Parallel grounding | Google Cloud is the one hyperscaler listing three third parties | Fetch of docs.cloud.google.com connector page and release notes[^162] |
| Cohere "recommendation" wording | User's framing; evidence is sole-tool placement, not a recommendation sentence | None expected; current docs say "swap in any other LangChain tool"[^34] |
| Keenable's "several AI labs and inference providers" | Unnamed customers behind the only new own-index entrant with lab claims | Customer disclosure[^153] |
| Windsurf/Devin current provider | You.com relationship predates Cognition; Devin names no provider | Cognition docs or subprocessor list[^129] |
| Salesforce Agentforce, Databricks Agent Bricks, Snowflake Cortex (Snowflake-side), Hugging Face Inference, Perplexity enterprise partners | No first-party page naming a web-search provider found | Vendor-side docs exist for Snowflake and Databricks only[^54][^59] |
| Spring AI, Lobe Chat, AutoGen (Microsoft), Continue, Roo Code, Aider, Kiro (first-party), Hebbia, Glean, Manus, Genspark, Lightpanda, Retell | No search-provider relationship found within budget | Targeted docs or source fetches |
| Linkup's $10M seed and Nebius–Tavily price | Both rest on aggregators or a single journalist citation | Primary press release; Nebius filing[^175][^151] |

## Conclusion

The partnership map says that web search for agents is being sold the way CDNs and payment rails were: the biggest buyers build or bundle their own, the platforms in the middle refuse to pick a winner, and the vendors compete for whichever default slots are still open. Those slots are now mostly in documentation — Cohere's cookbooks, NVIDIA's package, AWS's Lambda sample, LangChain's research template — and Tavily has filled nearly all of them, which explains why an aggregator with no index of its own commanded an acquisition from a GPU cloud. Exa took the other route and won the places where a platform must ship exactly one engine without asking (OpenRouter's fallback, Letta, Firefox), which is a stronger position per slot but a shorter list. Parallel's strategy of being the second name on every hyperscaler menu buys distribution without a single exclusive, and Brave's position — invisible in docs, present in Anthropic's compliance paperwork and OpenClaw's setup prompt — shows that index supply and tool branding have decoupled.

For anyone deciding whether a given organization is "taken," the useful test is whether the relationship appears in the consumer's own code, docs or subprocessor list rather than the vendor's. By that test only Anthropic–Brave, Nebius–Tavily, Elastic–Jina, Firefox–Exa, Letta–Exa, OpenHands–Tavily, NeMo–Tavily, Cohere–Tavily (docs only) and Cloudflare–Ceramic (default only) qualify; every other pairing in this report, including every cloud marketplace and every plugin directory, is one vendor among several and can be displaced by a config change.

## Sources

[^1]: journalist quoting Anthropic subprocessor list and tool schema, 2025-03-21 — https://simonwillison.net/2025/Mar/21/anthropic-used-brave/
[^2]: journalist, 2025-03-21 — https://techcrunch.com/2025/03/21/anthropic-appears-to-be-using-brave-to-power-web-searches-for-its-claude-chatbot/
[^3]: docs (provider-silent), obs. 2026-11-05 — https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool
[^4]: docs, obs. 2026-11-05 — https://code.claude.com/docs/en/tools
[^5]: code (plugin manifest, 315 plugins), obs. 2026-11-05 — https://raw.githubusercontent.com/anthropics/claude-plugins-official/main/.claude-plugin/marketplace.json
[^6]: press (Brave blog), 2026-06-29 — https://brave.com/blog/claude-cowork-amazon-bedrock-brave-mcp/
[^7]: docs, obs. 2026-11-05 — https://learn.chatgpt.com/docs/config-file/config-reference
[^8]: docs, obs. 2026-11-05 — https://openai.github.io/openai-agents-python/tools/
[^9]: docs, obs. 2026-11-05 — https://developers.openai.com/api/docs/pricing
[^10]: vendor docs (Exa), obs. 2026-11-05 — https://exa.ai/docs/integrations/chatgpt-codex.md
[^11]: vendor docs (Tavily), obs. 2026-11-05 — https://docs.tavily.com/documentation/integrations/agent-builder.md
[^12]: vendor docs (Keenable), obs. 2026-11-05 — https://docs.keenable.ai/integrations.md
[^13]: docs, obs. 2026-11-05 — https://aistudio.google.com/docs/pricing
[^14]: code, obs. 2026-11-05 — https://raw.githubusercontent.com/google/adk-python/main/src/google/adk/tools/google_search_tool.py
[^15]: docs, obs. 2026-11-05 — https://raw.githubusercontent.com/google-gemini/gemini-cli/main/docs/tools/web-search.md
[^16]: docs, obs. 2026-11-05 — https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/grounding/grounding-with-parallel
[^17]: docs, obs. 2026-11-05 — https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/grounding/grounding-with-exa
[^18]: press (Exa blog), 2026-04-28 — https://exa.ai/blog/exa-google-cloud
[^19]: vendor docs (Tavily, citing Google docs), obs. 2026-11-05 — https://docs.tavily.com/documentation/integrations/google-gemini-enterprise.md
[^20]: docs, obs. 2026-11-05 — https://developers.google.com/custom-search/v1/overview
[^21]: docs, obs. 2026-11-05 — https://learn.microsoft.com/en-us/azure/foundry-classic/agents/how-to/tools-classic/overview
[^22]: docs (lifecycle announcement), 2025-05-12 — https://learn.microsoft.com/en-us/lifecycle/announcements/bing-search-api-retirement
[^23]: code (Azure-Samples README), obs. 2026-11-05 — https://raw.githubusercontent.com/Azure-Samples/ai-foundry-agents-samples/main/examples/mcp/tavily/README.md
[^24]: vendor docs (Tavily), obs. 2026-11-05 — https://docs.tavily.com/documentation/integrations/microsoft.md
[^25]: vendor docs (Tavily), obs. 2026-11-05 — https://docs.tavily.com/documentation/partnerships/azure.md
[^26]: docs, obs. 2026-11-05 — https://learn.microsoft.com/en-us/semantic-kernel/concepts/text-search/out-of-the-box-textsearch
[^27]: code, obs. 2026-11-05 — https://github.com/microsoft/semantic-kernel/tree/main/dotnet/src/Plugins/Plugins.Web
[^28]: code (awslabs README), obs. 2026-11-05 — https://raw.githubusercontent.com/awslabs/amazon-bedrock-agent-samples/main/src/shared/web_search/README.md
[^29]: code (awslabs repo, `tavily_search.py`), obs. 2026-11-05 — https://github.com/awslabs/agentcore-samples
[^30]: code (awslabs startups offers), obs. 2026-11-05 — https://raw.githubusercontent.com/awslabs/startups/main/advisor/plugins/aws-startup-advisor/skills/knowledge-base-for-startups/references/offers/tavily.md
[^31]: vendor docs (Tavily), obs. 2026-11-05 — https://docs.tavily.com/documentation/partnerships/amazon.md
[^32]: vendor docs (Parallel), obs. 2026-11-05 — https://docs.parallel.ai/integrations/aws-marketplace.md
[^33]: vendor docs (Tavily), obs. 2026-11-05 — https://docs.tavily.com/documentation/integrations/kiro.md
[^34]: docs (Cohere source; published at https://docs.cohere.com/docs/tools-on-langchain), obs. 2026-11-05 — https://raw.githubusercontent.com/cohere-ai/cohere-developer-experience/main/fern/pages/integrations/cohere-and-langchain/tools-on-langchain.mdx
[^35]: code (Cohere agentic-RAG cookbook), obs. 2026-11-05 — https://raw.githubusercontent.com/cohere-ai/cohere-developer-experience/main/notebooks/guides/agentic-rag/tool_def.py
[^36]: code (Cohere Toolkit), obs. 2026-11-05 — https://github.com/cohere-ai/cohere-toolkit/blob/main/src/backend/config/tools.py
[^37]: journalist, 2025-08-06 — https://techcrunch.com/2025/08/06/tavily-raises-25m-to-connect-ai-agents-to-the-web/
[^38]: press (Nebius), 2026-02-10 — https://nebius.com/newsroom/nebius-announces-agreement-to-acquire-tavily-to-add-agentic-search-to-its-ai-cloud-platform
[^39]: directory (Brave logo wall and sign-up claims), obs. 2026-11-05 — https://brave.com/search/api/
[^40]: docs, obs. 2026-11-05 — https://docs.mistral.ai/studio/agents/agent-tools/websearch
[^41]: vendor docs (Linkup), obs. 2026-11-05 — https://docs.linkup.so/pages/integrations/linkup-mistral.md
[^42]: docs, obs. 2026-11-05 — https://docs.x.ai/developers/pricing
[^43]: vendor docs (Exa), obs. 2026-11-05 — https://exa.ai/docs/integrations/grok-build.md
[^44]: vendor docs (Tavily), obs. 2026-11-05 — https://docs.tavily.com/documentation/integrations/grok-build.md
[^45]: docs, obs. 2026-11-05 — https://api-docs.deepseek.com/guides/search
[^46]: code (NVIDIA migration stub), obs. 2026-11-05 — https://raw.githubusercontent.com/NVIDIA/NeMo-Agent-Toolkit/main/packages/nvidia_nat_langchain/src/nat/plugins/langchain/tools/tavily_internet_search.py
[^47]: journalist, 2024-07-16 — https://techcrunch.com/2024/07/16/exa-raises-17m-lightspeed-nvidia-ycombinator-google-ai-models
[^48]: press (Exa blog), 2025-09-03 — https://exa.ai/blog/announcing-series-b
[^49]: press (Exa blog), 2026-05-20 — https://exa.ai/blog/announcing-series-c
[^50]: code (IBM watsonx-developer-hub README), obs. 2026-11-05 — https://raw.githubusercontent.com/IBM/watsonx-developer-hub/main/agents/community/langgraph-tavily-tool/README.md
[^51]: vendor docs (Tavily), obs. 2026-11-05 — https://docs.tavily.com/documentation/partnerships/ibm.md
[^52]: code (BeeAI framework), obs. 2026-11-05 — https://github.com/i-am-bee/beeai-framework
[^53]: vendor page (Ceramic.ai investors), obs. 2026-11-05 — https://ceramic.ai
[^54]: vendor docs (Exa), obs. 2026-11-05 — https://exa.ai/docs/integrations/snowflake.md
[^55]: vendor docs (Tavily), obs. 2026-11-05 — https://docs.tavily.com/documentation/partnerships/snowflake.md
[^56]: vendor docs (Parallel), obs. 2026-11-05 — https://docs.parallel.ai/data-integrations/snowflake.md
[^57]: directory (Parallel logo wall and distribution claims), obs. 2026-11-05 — https://parallel.ai
[^58]: directory (Linkup logo wall), obs. 2026-11-05 — https://www.linkup.so
[^59]: vendor docs (Tavily), obs. 2026-11-05 — https://docs.tavily.com/documentation/partnerships/databricks.md
[^60]: press (You.com Series C), 2025-09 — https://you.com/articles/series-c
[^61]: docs, obs. 2026-11-05 — https://console.groq.com/docs/compound/systems/compound.md
[^62]: docs, obs. 2026-11-05 — https://console.groq.com/docs/deprecations
[^63]: code (Groq changelog), obs. 2026-11-05 — https://raw.githubusercontent.com/groq/groq-changelog/main/CHANGELOG.md
[^64]: docs (Groq integration pages: /tavily, /parallel, /exa, /you, /browserbase), obs. 2026-11-05 — https://console.groq.com/docs/tavily
[^65]: docs (Together AI tutorial), obs. 2026-11-05 — https://docs.together.ai/docs/ai-search-engine.md
[^66]: vendor docs (Exa), obs. 2026-11-05 — https://exa.ai/docs/integrations/fireworks.md
[^67]: vendor docs (Parallel), obs. 2026-11-05 — https://docs.parallel.ai/integrations/fireworks.md
[^68]: docs (Cerebras docs index; pages /integrations/exa.md, /integrations/parallel.md), obs. 2026-11-05 — https://inference-docs.cerebras.ai/llms.txt
[^69]: vendor docs (Linkup; also /sambanova/sambanova.md, /huggingface.md), obs. 2026-11-05 — https://docs.linkup.so/pages/integrations/cerebras.md
[^70]: docs, obs. 2026-11-05 — https://openrouter.ai/docs/guides/features/plugins/web-search
[^71]: vendor docs (Exa), obs. 2026-11-05 — https://exa.ai/docs/integrations/openrouter.md
[^72]: code (smolagents), obs. 2026-11-05 — https://raw.githubusercontent.com/huggingface/smolagents/main/src/smolagents/default_tools.py
[^73]: docs, obs. 2026-11-05 — https://docs.ollama.com/capabilities/web-search
[^74]: vendor docs (Parallel), obs. 2026-11-05 — https://docs.parallel.ai/integrations/ollama-tool-calling.md
[^75]: docs (Cloudflare changelog), 2026-10-02 — https://developers.cloudflare.com/changelog/post/2026-10-02-introducing-web-search-api/
[^76]: docs (Cloudflare providers page), updated 2026-10-02 — https://developers.cloudflare.com/web-search/providers/
[^77]: journalist (TNW), 2026-07 — https://thenextweb.com/news/cloudflare-block-ai-crawlers-pay-publishers
[^78]: code (vercel/ai gateway tools), obs. 2026-11-05 — https://raw.githubusercontent.com/vercel/ai/main/packages/gateway/src/gateway-tools.ts
[^79]: vendor docs (Tavily), obs. 2026-11-05 — https://docs.tavily.com/documentation/integrations/vercel-connect.md
[^80]: vendor docs (Linkup), obs. 2026-11-05 — https://docs.linkup.so/pages/integrations/vercel-ai-sdk.md
[^81]: vendor docs (Tavily integrations index), obs. 2026-11-05 — https://docs.tavily.com/llms.txt
[^82]: docs (Nebius Token Factory), obs. 2026-11-05 — https://docs.tokenfactory.nebius.com/integrations/overview.md
[^83]: press (Elastic investor relations), 2025-10-09 — https://ir.elastic.co/News--Events/news/news-details/2025/Elastic-Completes-Acquisition-of-Jina-AI-a-Leader-in-Frontier-Models-for-Multimodal-and-Multilingual-Search/default.aspx
[^84]: press (Keenable blog), 2026-09-16 — https://keenable.ai/blog/keenable-partners-with-baseten
[^85]: vendor docs (Exa), obs. 2026-11-05 — https://exa.ai/docs/integrations/baseten.md
[^86]: vendor docs (Linkup), obs. 2026-11-05 — https://docs.linkup.so/pages/integrations/baseten/baseten.md
[^87]: press (Exa blog), 2026-08-17 — https://exa.ai/blog/exa-firefox
[^88]: journalist (The Register), 2025-05-15 — https://www.theregister.com/2025/05/15/bing_search_apis_retired/
[^89]: vendor docs (Perplexity MCP client list and integration pages), obs. 2026-11-05 — https://docs.perplexity.ai
[^90]: vendor docs (Tavily), obs. 2026-11-05 — https://docs.tavily.com/documentation/integrations/hermes-agent.md
[^91]: vendor docs (Tavily; also /integrations/merge-gateway.md), obs. 2026-11-05 — https://docs.tavily.com/documentation/integrations/vellum.md
[^92]: vendor docs (Tavily), obs. 2026-11-05 — https://docs.tavily.com/documentation/integrations/langchain.md
[^93]: docs (LangChain Brave provider page), obs. 2026-11-05 — https://python.langchain.com/docs/integrations/providers/brave_search
[^94]: code (open_deep_research), obs. 2026-11-05 — https://raw.githubusercontent.com/langchain-ai/open_deep_research/main/src/open_deep_research/configuration.py
[^95]: docs (LangChain tools integrations), obs. 2026-11-05 — https://docs.langchain.com/oss/python/integrations/tools
[^96]: code (PyPI; langchain-tavily 200, langchain-brave-search and langchain-you 404), obs. 2026-11-05 — https://pypi.org/project/langchain-tavily/
[^97]: case study (LangChain blog), 2025-06-30 — https://blog.langchain.com/exa/
[^98]: directory (Tavily logo wall), obs. 2026-11-05 — https://www.tavily.com
[^99]: code (PyPI llama-index-tools-*; exa, keenable shown), obs. 2026-11-05 — https://pypi.org/project/llama-index-tools-exa/ ; https://pypi.org/pypi/llama-index-tools-keenable/json
[^100]: docs, obs. 2026-11-05 — https://docs.crewai.com/en/tools/search-research/overview
[^101]: docs (AG2 search toolkits), obs. 2026-11-05 — https://docs.ag2.ai/docs/user-guide/extensions/tools/search/exa/ ; https://docs.ag2.ai/docs/user-guide/extensions/tools/search/keenable/
[^102]: vendor docs (Perplexity), obs. 2026-11-05 — https://docs.perplexity.ai/docs/getting-started/integrations/ag2.md
[^103]: docs (Pydantic AI), obs. 2026-11-05 — https://raw.githubusercontent.com/pydantic/pydantic-ai/main/docs/common-tools.md
[^104]: docs (Mastra), obs. 2026-11-05 — https://mastra.ai/integrations/tools/tavily.md ; https://mastra.ai/integrations/tools/perplexity.md
[^105]: directory (Haystack integrations), obs. 2026-11-05 — https://haystack.deepset.ai/integrations
[^106]: code (Agno tools directory), obs. 2026-11-05 — https://github.com/agno-agi/agno/tree/main/libs/agno/agno/tools
[^107]: docs (Letta), obs. 2026-11-05 — https://docs.letta.com/guides/agents/web-search
[^108]: code (Dify official plugins), obs. 2026-11-05 — https://github.com/langgenius/dify-official-plugins/tree/main/tools
[^109]: code (n8n LangChain tool nodes), obs. 2026-11-05 — https://github.com/n8n-io/n8n/tree/master/packages/%40n8n/nodes-langchain/nodes/tools
[^110]: code (Flowise tool nodes), obs. 2026-11-05 — https://github.com/FlowiseAI/Flowise/tree/main/packages/components/nodes/tools
[^111]: docs (Langflow bundles), obs. 2026-11-05 — https://docs.langflow.org/bundles-exa
[^112]: directory (Composio toolkits), obs. 2026-11-05 — https://composio.dev/toolkits/tavily
[^113]: vendor docs (Parallel), obs. 2026-11-05 — https://docs.parallel.ai/integrations/browseruse.md
[^114]: code (GPT Researcher default config), obs. 2026-11-05 — https://raw.githubusercontent.com/assafelovic/gpt-researcher/master/gpt_researcher/config/variables/default.py
[^115]: code (Khoj), obs. 2026-11-05 — https://raw.githubusercontent.com/khoj-ai/khoj/master/src/khoj/processor/tools/online_search.py
[^116]: code (Perplexica README), obs. 2026-11-05 — https://raw.githubusercontent.com/ItzCrazyKns/Perplexica/master/README.md
[^117]: code (Morphic README), obs. 2026-11-05 — https://raw.githubusercontent.com/miurla/morphic/main/README.md
[^118]: code (Open WebUI retrieval router), obs. 2026-11-05 — https://github.com/open-webui/open-webui/blob/main/backend/open_webui/routers/retrieval.py
[^119]: code (AnythingLLM web-browsing plugin), obs. 2026-11-05 — https://github.com/Mintplex-Labs/anything-llm/blob/master/server/utils/agents/aibitat/plugins/web-browsing.js
[^120]: code (LibreChat example config), obs. 2026-11-05 — https://raw.githubusercontent.com/danny-avila/LibreChat/main/librechat.example.yaml
[^121]: docs (Onyx web search), obs. 2026-11-05 — https://docs.onyx.app/overview/core_features/web_search.md
[^122]: vendor docs (Linkup) and code (SurfSense README), obs. 2026-11-05 — https://docs.linkup.so/pages/integrations/surfsense/surfsense.md ; https://raw.githubusercontent.com/MODSetter/SurfSense/main/README.md
[^123]: docs (Cursor @Web, provider-silent), obs. 2026-11-05 — https://docs.cursor.com/context/%40-symbols/%40-web
[^124]: docs (Cursor security; subprocessors on trust portal), obs. 2026-11-05 — https://cursor.com/security
[^125]: vendor docs (Tavily), obs. 2026-11-05 — https://docs.tavily.com/documentation/integrations/cursor.md
[^126]: vendor docs (Parallel), obs. 2026-11-05 — https://docs.parallel.ai/integrations/cursor-marketplace.md
[^127]: docs (Devin; Cascade legacy), obs. 2026-11-05 — https://docs.devin.ai/desktop/cascade
[^128]: vendor docs (Tavily), obs. 2026-11-05 — https://docs.tavily.com/documentation/integrations/devin.md
[^129]: docs (Devin CLI enterprise settings), obs. 2026-11-05 — https://docs.devin.ai/cli/enterprise/team-settings.md
[^130]: code (Zed web_search_providers), obs. 2026-11-05 — https://raw.githubusercontent.com/zed-industries/zed/main/crates/web_search_providers/src/cloud.rs
[^131]: docs (Zed AI tools), obs. 2026-11-05 — https://zed.dev/docs/ai/tools.md
[^132]: vendor docs (Tavily), obs. 2026-11-05 — https://docs.tavily.com/documentation/integrations/claude.md
[^133]: vendor docs (Parallel), obs. 2026-11-05 — https://docs.parallel.ai/integrations/claude-code-marketplace.md
[^134]: vendor docs (Perplexity), obs. 2026-11-05 — https://docs.perplexity.ai/docs/getting-started/integrations/antigravity.md
[^135]: docs (goose official tutorial), obs. 2026-11-05 — https://raw.githubusercontent.com/block/goose/main/documentation/docs/mcp/tavily-mcp.md
[^136]: docs (OpenHands; page moved to /openhands/usage/advanced/search-engine-setup), obs. 2026-11-05 — https://docs.all-hands.dev/usage/search-engine-setup
[^137]: vendor docs (Tavily), obs. 2026-11-05 — https://docs.tavily.com/documentation/integrations/opencode.md
[^138]: vendor docs (Parallel), obs. 2026-11-05 — https://docs.parallel.ai/integrations/clawhub.md
[^139]: vendor docs (Exa), obs. 2026-11-05 — https://exa.ai/docs/integrations/hermes-agent.md
[^140]: press (Brave blog), 2026-04-01 — https://brave.com/blog/openclaw/
[^141]: practitioner (Hacker News), 2026-01-30 — https://news.ycombinator.com/item?id=46822822
[^142]: vendor docs (Parallel), obs. 2026-11-05 — https://docs.parallel.ai/integrations/superhuman.md
[^143]: vendor docs (Linkup), obs. 2026-11-05 — https://docs.linkup.so/pages/integrations/lovable/lovable.md
[^144]: analyst (Sacra; independent estimate), 2026-01-09 — https://sacra.com/research/exa-at-10m-growing-11x-yoy
[^145]: vendor docs (Parallel), obs. 2026-11-05 — https://docs.parallel.ai/integrations/zapier.md
[^146]: docs (ElevenLabs; also /integrations/tavily.md, /parallel.md, /perplexity.md), obs. 2026-11-05 — https://elevenlabs.io/docs/eleven-agents/customization/integrations/exa.md
[^147]: docs (Pipecat; also /services/llm/perplexity.md), obs. 2026-11-05 — https://docs.pipecat.ai/api-reference/server/services/knowledge-retrieval/keenable.md
[^148]: vendor docs (Perplexity), obs. 2026-11-05 — https://docs.perplexity.ai/docs/getting-started/integrations/livekit.md
[^149]: docs (Vapi), obs. 2026-11-05 — https://docs.vapi.ai/providers/model/perplexity.md
[^150]: vendor docs (Exa), obs. 2026-11-05 — https://exa.ai/docs/integrations/browserbase.md
[^151]: journalist (Sacra citing Bloomberg), 2026-02 — https://sacra.com/research/tavily
[^152]: journalist (SiliconANGLE), 2026-02-10 — https://siliconangle.com/2026/02/10/ai-infrastructure-giant-nebius-buys-agentic-search-startup-tavily/
[^153]: journalist (TechCrunch), 2026-08-25 — https://techcrunch.com/2026/08/25/accel-backed-keenable-is-indexing-the-web-for-ai-agents/
[^154]: journalist (TechCrunch), 2026-04-29 — https://techcrunch.com/2026/04/29/parallel-web-systems-hits-2b-valuation-five-months-after-its-last-big-raise/
[^155]: journalist (Newcomer), 2025-11-12 — https://www.newcomer.co/p/exclusive-parag-agrawals-parallel
[^156]: aggregator (Simplify), Oct 2025 — https://simplify.jobs/c/YOU-Dot-Com
[^157]: vendor docs (Parallel), obs. 2026-11-05 — https://docs.parallel.ai/integrations/google-cloud-marketplace.md
[^158]: vendor docs (Exa), obs. 2026-11-05 — https://exa.ai/docs/integrations/claude-web-desktop.md
[^159]: vendor docs (Keenable MCP server; Claude connector, Codex setup), obs. 2026-11-05 — https://docs.keenable.ai/mcp-server.md
[^160]: vendor docs (Parallel MCP installation), obs. 2026-11-05 — https://docs.parallel.ai/integrations/mcp/installation.md
[^161]: code (Keenable GitHub org: keenable-grok-plugin, keenable-antigravity), obs. 2026-11-05 — https://github.com/keenableai
[^162]: docs (Google Tavily connector page; cited by Tavily, not fetched this session) — https://docs.cloud.google.com/gemini/enterprise/docs/connectors/tavily
[^163]: vendor docs (Parallel), obs. 2026-11-05 — https://docs.parallel.ai/integrations/openrouter.md
[^164]: vendor docs (Linkup Dify guide), obs. 2026-11-05 — https://docs.linkup.so/pages/integrations/dify/dify.md
[^165]: vendor docs (Tavily n8n guide), obs. 2026-11-05 — https://docs.tavily.com/documentation/integrations/n8n.md
[^166]: vendor docs (Exa n8n guide), obs. 2026-11-05 — https://exa.ai/docs/integrations/n8n.md
[^167]: vendor docs (Tavily Langflow guide), obs. 2026-11-05 — https://docs.tavily.com/documentation/integrations/langflow.md
[^168]: vendor docs (Exa ElevenLabs guide), obs. 2026-11-05 — https://exa.ai/docs/integrations/elevenlabs.md
[^169]: vendor docs (Perplexity Cursor guide), obs. 2026-11-05 — https://docs.perplexity.ai/docs/getting-started/integrations/cursor.md
[^170]: vendor docs (Exa OpenClaw guide, listed in Exa docs index), obs. 2026-11-05 — https://docs.exa.ai/llms.txt
[^172]: vendor docs (Parallel OpenCode plugin), obs. 2026-11-05 — https://docs.parallel.ai/integrations/opencode-plugin.md
[^173]: docs (Kiro docs index, no search-provider mention), obs. 2026-11-05 — https://kiro.dev/docs/llms.txt
[^174]: docs (Cline docs index, no built-in provider), obs. 2026-11-05 — https://docs.cline.bot/llms.txt
[^175]: aggregator (Parsers.vc; primary release returned 503), 2026-02 — https://parsers.vc/news/260210-linkup-secures-10m-seed-for-ai-s-real-time/
[^176]: press (Firecrawl blog), 2026-09-22 — https://www.firecrawl.dev/blog/introducing-alexandria-series-b
