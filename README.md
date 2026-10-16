# Tavily-compatible search with reranking

A drop-in Tavily `/search` endpoint with two extra `search_depth` modes. They retrieve more candidates from Tavily and rerank them with the OpenAI Decisions API. Every other `search_depth` (`basic`, `advanced`, `fast`, `ultra-fast`, or none) is passed through to Tavily unchanged.

| `search_depth` | What it does | Upstream calls per request | Cost per request¹ | Latency² | Benchmarks³ |
|---|---|---|---|---|---|
| **`better`** | Tavily advanced with 20 results; listwise rerank (`rerank-v1`); returns the top `max_results` | 1 Tavily advanced, 2 Decisions | $0.0167 | 4.6–5.1 s | 995 / 1024 Elo; 96.3% on SimpleQA, F1 59.6% on DeepSearchQA |
| **`harder`** | `better`'s main call (the same request, shared through the cache) plus up to three targeted Tavily basic calls with published dates and two LLM-rephrased queries, the first 5 results of each added to the pool. Every one of these calls is issued twice, with and without `EXCLUDE_DOMAINS` (social-media sites by default), and both result sets are merged, about 40 documents; the reranker (`rerank-v3`, date-aware) sees which pages are on those domains and ranks them below other relevant documents unless they are the best evidence | 2 advanced + about 6 basic; 3 Decisions + 1 Responses | about $0.09 | 7–11 s uncached | **1083 / 1109** Elo; 96.5% on SimpleQA, F1 66.8% on DeepSearchQA, level with Keenable |
| *Tavily advanced (reference)* | | 1 advanced | $0.016 | 3–5 s | 954 / 944 Elo; 96.3%, F1 60.4% |

**Notes on the table**
1. **Cost:** Tavily pay-as-you-go ($0.008 per credit) plus gpt-6-luna ($0.10 per 1M input, $0.50 per 1M output tokens), averaged over the 200 benchmark queries. With your own Tavily key (BYOK), the operator pays only the model part: about $0.0007 per `better` request and $0.0015 per `harder` request.
2. **Latency:** a live smoke test, 3 queries per mode.
3. **Benchmarks:** the final report's five-system comparison (`../report/DETAILS.md`): Elo on 200 agent and chat search requests under Claude Haiku 5.5 / gpt-6-luna as judges, SimpleQA top 3 on 1,200 questions, and DeepSearchQA with a 5-step agent on 500 tasks.

**Naming.** `harder` is the configuration the benchmark directories and the report's result files call `harder-hybrid` (entries `dfpn_harder-hybrid_10`, runs `s500_service_harder-hybrid` and `results_r12_1200_hybrid`); the service accepts `harder-hybrid` as an alias, so those reproduction commands keep their names. The `harder`, `stronger` and `harder-clean` of the benchmark reports are the earlier configurations, which `harder` replaced on 2026-10-15 (see "History" below); they are no longer served.

### The targeted calls

| Call | Fires when | Request |
|---|---|---|
| site | the query has `site:` or `repo:` | the operator is removed from the query and its host goes into `include_domains` (`repo:` → github.com) |
| fresh | a Decisions question detects a need for recent information and a recency window | `time_range` = that window; `topic: news` for day / week |
| locale | the query language is detected | `language`, plus `country` for non-English queries |

### The rephrasings

gpt-6-luna, reasoning effort low, writes two alternative queries. The strategies:
- split multi-part queries;
- turn questions into keywords;
- search bare package or model names;
- add "pdf" or "report" when a document is wanted;
- always include an English translation of a non-English query.

### The two sets of calls

Every Tavily call of `harder` (the main call, the targeted calls and the rephrased queries) is issued plain and with `EXCLUDE_DOMAINS` added to the request's `exclude_domains` (merged after the client's own list). Tavily's `exclude_domains` changes what is retrieved, not only what is filtered: with the exclusion the advanced call keeps only 43% of the plain call's non-social pages, so neither variant alone is best. Both result sets go into the pool (the plain copy of a page first), and the reranker is told which pages are on the excluded domains. A call restricted to `include_domains` (the site call, or any call when the client set `include_domains`) is issued once, since an exclusion could contradict it. With `EXCLUDE_DOMAINS` empty, each call is issued once and nothing is marked.

## API

The request and response are Tavily's.

```sh
curl -s localhost:8000/search -H "Authorization: Bearer $KEY" -H "Content-Type: application/json" \
  -d '{"query": "MiniMax-M3 release date license", "search_depth": "harder", "max_results": 5}'
```

- **`max_results`:** 0–20, default 10. It cuts the reranked pool, so `better` always reranks the full 20 results.
- **`score`:** in the new modes, the reranker's score, the mean listwise probability over the two orders.
- **`published_date`:** returned only when the client asks for `include_published_date`, as with Tavily. `harder` always requests dates on its extra calls, for the date-aware reranker. The main call asks for them only when the client does, because the flag changes what Tavily retrieves (see "History").
- **Client parameters** (`topic`, `time_range`, `include_domains`, `country`, `include_raw_content`, …):
  - They are forwarded to every upstream call.
  - `include_answer` and `include_images` go to the main call only.
  - A targeted call is skipped when the client already set its dimension. A client `include_domains` skips the site call; `topic` (other than general), `time_range`, `start_date` or `end_date` skip the fresh call; `country` or `language` skip the locale call.
  - A client `exclude_domains` is forwarded to every call and merged with `EXCLUDE_DOMAINS` in the second set of calls.
- **`include_usage: true`** returns the summed Tavily credits of all upstream calls.
- **Auth:** `Authorization: Bearer <key>`, or the legacy `api_key` body field, which is never forwarded.
- **`GET /health`:** readiness, the modes, the active settings and which keys are configured, never their values.

## Keys: operator-paid and BYOK

| The client sends | Tavily calls use | OpenAI calls use |
|---|---|---|
| `SERVICE_API_KEY` | the operator's `TAVILY_API_KEY` | the operator's `OPENAI_API_KEY` |
| any other key | **that key** (bring your own Tavily key) | the operator's `OPENAI_API_KEY` |

- **Unknown BYOK keys** are validated before any other spend: the plain main Tavily call runs alone before the second main call, detection, rephrasing or reranking. A rejected key returns 401 and is then refused for `INVALID_KEY_TTL_S` (60 s) without calling Tavily.
- **Accepted keys** are trusted for `KEY_CACHE_TTL_S` (600 s), so their requests run fully in parallel.
- **Storage and forwarding:** keys are kept only as SHA-256 hashes. The service key is never forwarded upstream.
- **Operator key rejected:** if Tavily rejects the operator's key, the client gets 502, not 401.

**Limitation:** in BYOK mode anyone with a valid Tavily key can spend the operator's OpenAI budget, about $0.001 per request. Put the service behind a rate limiter, or restrict BYOK, if it is exposed publicly.

## Run

```sh
cp .env.example .env    # set SERVICE_API_KEY, TAVILY_API_KEY, OPENAI_API_KEY
docker build -t tavily-rerank .
docker run --rm -p 8000:8000 --env-file .env -v tavily-cache:/data tavily-rerank
```

| Variable | Default | |
|---|---|---|
| `SERVICE_API_KEY` | — | the key for operator-paid requests; without it, only BYOK works |
| `TAVILY_API_KEY` | — | the operator's Tavily key |
| `OPENAI_API_KEY` | — | the operator's OpenAI key; without it the new modes fall back to Tavily's order |
| `RERANK_CONTENT_CHARS` | `4000` | characters of each document the reranker sees; the early benchmark entries used 600, which hid the answer on SimpleQA (see "History") |
| `RERANK_PREFER_REFERENCE` | `false` | add "prefer Wikipedia and other authoritative reference sources" to the rerank instruction; it did not help on SimpleQA |
| `RERANK_PIN_WIKIPEDIA_TOP` | `0` | keep a Wikipedia result found in the first N pool positions at its position, and rerank the rest around it; `3` helps SimpleQA, but not agent requests |
| `REPHRASE_N` | `2` | `harder`: rephrased queries per request (the prompt asks for exactly that many) |
| `EXTRA_TAKE` | `5` | `harder`: results kept from each targeted or rephrased call (each call requests 20) |
| `RESULT_DATES` | `false` | return `published_date` whenever the pool knows it (from the extra calls), even when the client did not send `include_published_date`; the main call is unchanged |
| `SOCIAL_KEEP_TOP` | `0` | `harder`: when > 0, a page on `EXCLUDE_DOMAINS` is returned only if the reranker put it in the first N positions; the rest are dropped from the list |
| `ENRICH_CACHE` | `true` | also cache the detection and rephrasing LLM calls (same TTL as the Tavily cache), so repeated queries reuse them |
| `TAVILY_CACHE_DIR` | `cache` (`/data/cache` in the image) | persistent Tavily response cache |
| `TAVILY_CACHE_TTL_S` | `604800` (7 days) | cache time-to-live in seconds; `0` disables the cache |
| `EXCLUDE_DOMAINS` | facebook.com, instagram.com, youtube.com, reddit.com, tiktok.com, x.com, twitter.com, linkedin.com, pinterest.com, quora.com, threads.net | the domains `harder` issues its second set of calls without and marks for the reranker (comma-separated; empty makes it issue each call once and mark nothing) |
| `TAVILY_ARCHIVE_DB` | `archive.sqlite` next to the cache directory (`/data/archive.sqlite` in the image) | durable SQLite archive of every cached response, kept after the TTL removes it from the cache; empty disables it |
| `OPENAI_MODEL` | `gpt-6-luna` | Decisions and Responses model |
| `REPHRASE_EFFORT` | `low` | reasoning effort for `harder`'s rephrasing |
| `UPSTREAM_TIMEOUT_S` | `60` | per upstream request |
| `KEY_CACHE_TTL_S` / `INVALID_KEY_TTL_S` | `600` / `60` | BYOK key caching |
| `LOG_LEVEL` | `INFO` | one line per request: mode, caller kind, upstream calls, pool size, rerank status, credits, time; never keys or queries |

The image runs 2 uvicorn workers; each keeps its own BYOK key cache.

The last four settings are `harder`'s tuning knobs, added after the Perplexity comparison (`../benchmark/analysis/perplexity/REPORT.md`): more rephrasings and a larger take widen the pool where `harder` loses on coverage (BrowseComp); dates in the response and the social-media cut address the list-quality reasons the judges gave for Perplexity's wins. The defaults are the evaluated configuration.

**Local development**

```sh
uv venv --python 3.12 .venv && uv pip install --python .venv/bin/python -r requirements-dev.txt
.venv/bin/python -m pytest -q                      # 43 tests: mocked upstreams, plus prompt parity with the benchmark scripts
SERVICE_API_KEY=... TAVILY_API_KEY=... OPENAI_API_KEY=... .venv/bin/uvicorn app.main:app --port 8000
.venv/bin/python scripts/smoke_test.py --base-url http://localhost:8000 --key-file <file with SERVICE_API_KEY>
```

## Tavily response cache and parallel requests

- **What is cached:** every successful Tavily response, on disk, for `TAVILY_CACHE_TTL_S` (7 days by default).
- **Cache key:** the exact upstream request body plus a hash of the Tavily key that paid for it.
  - A BYOK client is served only responses fetched with its own key, and the operator's requests share one cache.
  - A key Tavily never accepted can't be served from the cache, so the BYOK validation still holds.
- **Cached calls cost no credits.** `usage.credits` counts only live calls.
- **The `x-cache` header:** `HIT` / `MISS` for passthrough requests, and `<hits>/<calls>` for the new modes. `harder`'s plain main call is `better`'s call, so a `harder` request after a `better` one for the same query pays only for its other calls.
- **Identical requests in flight share one upstream call.**
  - Within a worker, the others wait for the first call and get a copy (counted as hits).
  - Across workers, a per-request file lock in the cache directory makes the second worker wait and then read the cached response.
  - With the cache disabled, only the within-worker sharing applies.
- **Housekeeping:** expired entries are removed on startup and every 1,000 writes.
- **Archive:** nothing fetched is lost when the TTL cleans the cache. Every entry is also written to a SQLite database (`TAVILY_ARCHIVE_DB`, by default `archive.sqlite` next to the cache directory, `/data/archive.sqlite` in the image), and an entry that was never archived (written by an older version) is archived when it expires, before it is deleted. The archive keeps the request body, the account hash and the response, with timestamps; a response fetched again after expiry is kept as a second version. The service never reads it; `python -m scripts.cache_archive` imports an existing cache directory into it, prints statistics, and exports entries as JSON lines.

## History

The service was built up in steps, each evaluated on the benchmarks under `../benchmark/`, and the reports there use the names of that time:

- **`better`** (unchanged): reranking only.
- **`stronger`**: `better`'s call plus the targeted calls (site, fresh, locale), with the date-aware `rerank-v2`.
- **`harder`** (the earlier one): `stronger` plus the two rephrased queries. On the 9-entry leaderboard it reached 1134 Elo against 947 for Tavily advanced, and 97.1% on SimpleQA top 3 (800 questions), but as an agent's search tool it stayed at Tavily's level on DeepSearchQA (`../benchmark/deepsearchqa/REPORT.md`).
- **`harder-clean`**: `harder` with `EXCLUDE_DOMAINS` on every call. It gained 4.8 points of fully correct DeepSearchQA tasks but lost about 35 Elo on the leaderboard and 2.3 points on SimpleQA, because the exclusion changes what Tavily retrieves (`../benchmark/leaderboard_hc/REPORT.md`).
- **`harder-hybrid`**, now **`harder`**: every call issued both ways and the reranker told about the social-media pages (`rerank-v3`). It keeps the agent gain without the cost: level with `harder` on the leaderboard, 96.5% on SimpleQA, F1 66.8% on DeepSearchQA (`../benchmark/analysis/hybrid_pilot/REPORT.md`). On 2026-10-15 it replaced `harder`, and `stronger` and `harder-clean` were removed.

Three findings along the way shaped the settings:

- **Rerank content length is 4,000 characters by default** (it was 600). On SimpleQA top 3, the 600-character reranker dropped the answer-bearing page in 5 of 20 failures studied, because the answer usually starts later in the page (`../benchmark/analysis/simpleqa_top3_diagnosis/REPORT.md`); `better` went from 93.5% to 96.1% on 800 questions, level with Tavily advanced. Agent requests prefer the 600-character versions slightly, partly because the judge itself sees only 600 characters per result. Set `RERANK_CONTENT_CHARS=600` to reproduce the early benchmark entries.
- **The main call does not send `include_published_date`** unless the client does; the extra calls still do. Requesting dates changes what Tavily retrieves (fewer Wikipedia pages, only 6.2–6.5 of 10 top URLs shared with the plain call): on SimpleQA top 3 the change took the multi-call modes from about 94% to about 97%, and it lets `better` and `harder` share one cached main call (`../benchmark/pm_check/REPORT.md`).
- **The Wikipedia hint (`RERANK_PREFER_REFERENCE`), a 6,000-character window and a rerank prompt without the date preference did not help**, and the **Wikipedia pin** (`RERANK_PIN_WIKIPEDIA_TOP`) helps SimpleQA by about a point but not agent requests; all are off by default.

## Failure behaviour

- **The main Tavily call fails:** the client gets Tavily's status and body. Tavily's 400 / 401 / 429 / 432 pass through unchanged.
- **A variant, rephrased or second-set call fails:** it is dropped.
- **An OpenAI call fails** (error, timeout or refusal): detection and rephrasing are skipped, and the rerank keeps Tavily's order. The request still succeeds.
- **Retries:** upstream 429 / 5xx and network errors are retried twice, honouring `Retry-After` up to 5 s.

## Layout

- `app/main.py`: FastAPI app, auth and routing.
- `app/pipeline.py`: the two modes.
- `app/enrich.py`: `site:` rewrite, detection and rephrasing.
- `app/rerank.py`: listwise reranking.
- `app/prompts.py`: the evaluated prompts.
- `app/auth.py`: key handling.
- `app/upstream.py`: async Tavily and OpenAI clients.
- `app/archive.py`: the durable archive of cached responses.
- `app/config.py`: settings.
