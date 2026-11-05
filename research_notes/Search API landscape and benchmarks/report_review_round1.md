# Adversarial review of the report draft (round 1, 2026-11-05)

Reviewer: an independent subagent that read the full report, the README and the verification files, and
grep-checked about 150 numeric or factual claims against the 15 notes (26 tool calls).

Counts: SUPPORTED about 140; MERGED or MISMATCH 1 headline figure plus 2 live-page drift values; MISLABELLED 2
(one table column header, one sentence); UNSUPPORTED 0. Verification compliance: all 8 CORRECTED verdicts applied,
all 7 UNVERIFIABLE figures marked or unused.

## High
- H1. The BLUF, a heading and a first sentence say "the same product's BrowseComp score spans 32% to 91.8%". The
  32% is Parallel Turbo or Tavily in Parallel's September 2026 low-cost tier; 91.8% is Exa 3.0's own post. No
  single product spans both. Exa's documented span is 33.7% to 91.8%; Parallel Turbo's is 32% to 75%.
- H2. The provider table's "Independent scores" column holds vendor-run (NEEDLE is Keenable-run) and
  competitor-run numbers (Parallel's July 2026 figures for SerpApi and OpenAI; Tavily's repo figure for Serper;
  Valyu's own FreshQA run). Rename to "Third-party and competitor scores (source named)" and tag each cell.
- H3. The dfpn section calls NEEDLE an independent board in one sentence.

## Medium
- M1. "Only two independent boards" (BLUF and heading) against "Three independent sources" (body);
  OpenBenchmarks is self-described independent with undisclosed operators; Vals varies the model, so only
  Artificial Analysis holds everything but the provider fixed.
- M2. The full 21-row NEEDLE standings (p50, p95, error, cost) and the 31 August snapshot (Keenable and
  Perplexity tied at about 71%, Exa 68%; Exa led the deep-tail slice 0.557 against Keenable 0.470; Keenable
  realtime 193/284 ms against Exa 1,876/2,955 ms) are in the notes but not in the report.
- M3. Keenable's "clearest edge" is framed against Exa only; on the same 7-day means Perplexity leads Scholar
  (0.737) and Finance (0.921), exa-lite leads News (0.650); Keenable leads only AgenticRare (0.494).
- M4. Two citations point at URLs that do not support the claim (a NEEDLE GitHub page cited for price clustering;
  searchenginemap.com cited for crawler disclosure); one link text leaks internal file naming.
- M5. The Artificial Analysis October table caption claims all times per task were verified; only four rows were
  re-read; Perplexity high is 29.4 or 29.5 s depending on the fetch.
- M6. Providers in the notes but missing from the table: Context.dev, Keiro, Yandex Search API, the SERP-scraper
  price ladder beyond Serper and SerpApi, Mistral and Cohere built-in tools, Felo, Critique Labs, Andi.
- M7. Practitioner evidence unused: Brave free-tier removal reaction (GitHub issue closed NOT_PLANNED), framework
  maintainers' default-tool statements, Keenable staff's HN comment on DeepSeek, a pricing-surprises list.
- M8. The dfpn section restates the README to its author for about a third of its length.

## Low
- L1. Parallel's n=50 implies about ±13 points at 95%, not ±14. L2. 0.2 points on 1,200 is two or three
  questions, not three. L3. Known Agents measures sites with robots.txt rules for CCBot, not sites blocking it.
  L4. Brave's 94.1% is Research-mode multi-search F1 on 4,332 questions. L5. "Perplexity 97.3%" on OpenBenchmarks
  is the low tier. L6. Vals labels the tool "Keenable" without a tier. L7. Dynamic Snippets rolled out 2026-08-30
  and was described in a post dated 2026-10-15. L8. Artificial Analysis added a second Brave configuration rather
  than switching. L9. Five price cells lack URLs. L10. The October crawl ran 14 days, about 150M fetches a day
  while crawling. L11. Keenable's NEEDLE 72% is tied second with perplexity-fast. L12. LiveNewsBench figure is
  via a mirror. L13. The conclusion repeats the BLUF. L14. Minor benchmark and MCP omissions.

## Verdict
The numeric core is sound. After H1 to H3 and M1 to M5 the report is fit to deliver; M6 to M8 raise it from
accurate to complete. All fixes were applied by the report writer in round 2 (see the Journal).
