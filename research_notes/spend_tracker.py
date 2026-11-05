#!/usr/bin/env python3
"""Sum token usage of this Claude Code session (main transcript + subagent transcripts) and estimate cost.

The transcripts are JSON lines; only `message.usage` fields are read, never the content. Prices are the
list prices found for the serving model (third-party aggregators, 2026-11-05; unverified):
  input $10/M, output $50/M, 1-hour cache write $20/M, cache read $1/M (one source says $0.25/M).
Usage: python3 -I spend_tracker.py [--budget 240]
"""
import glob, json, os, sys, collections

SESSION = os.environ.get("CLAUDE_CODE_SESSION_ID", "7b686cf8-f2a0-5249-ac1c-6e0b138a6ac4")
MAIN = f"/root/.claude/projects/-home-user-dfpn/{SESSION}.jsonl"
TASKS = f"/tmp/claude-0/-home-user-dfpn/{SESSION}/tasks/*.output"
PRICE = {"input_tokens": 10, "output_tokens": 50, "cache_creation_input_tokens": 20, "cache_read_input_tokens": 1}
PRICE_LOW = dict(PRICE, cache_read_input_tokens=0.25)


def usage_of(path):
    tot, per = collections.Counter(), {}
    try:
        with open(path, encoding="utf-8", errors="replace") as f:
            for line in f:
                try:
                    d = json.loads(line)
                except ValueError:
                    continue
                m = d.get("message") if isinstance(d, dict) and isinstance(d.get("message"), dict) else None
                if not m or not isinstance(m.get("usage"), dict):
                    continue
                # one API response can be split over several lines (text + tool_use blocks), each repeating the
                # usage as known at that point; keep the largest value seen per response and count it once
                mid = m.get("id") or d.get("uuid")
                cur = per.setdefault(mid, collections.Counter())
                for k in PRICE:
                    cur[k] = max(cur[k], int(m["usage"].get(k) or 0))
    except OSError:
        pass
    for cur in per.values():
        tot.update(cur)
    return len(per), tot


def cost(tot, price):
    return sum(tot[k] * price[k] / 1e6 for k in price)


def main():
    budget = float(sys.argv[sys.argv.index("--budget") + 1]) if "--budget" in sys.argv else 240.0
    rows = [("main", *usage_of(MAIN))]
    for p in sorted(glob.glob(TASKS)):
        rows.append((os.path.basename(p)[:8], *usage_of(p)))
    grand = collections.Counter()
    print(f"{'transcript':10s} {'turns':>5s} {'output':>9s} {'cache_w':>10s} {'cache_r':>11s} {'input':>7s} {'$ (hi)':>8s} {'$ (lo)':>8s}")
    for name, n, t in rows:
        grand.update(t)
        print(f"{name:10s} {n:5d} {t['output_tokens']:9d} {t['cache_creation_input_tokens']:10d} "
              f"{t['cache_read_input_tokens']:11d} {t['input_tokens']:7d} {cost(t, PRICE):8.2f} {cost(t, PRICE_LOW):8.2f}")
    hi, lo = cost(grand, PRICE), cost(grand, PRICE_LOW)
    print(f"{'TOTAL':10s} {sum(r[1] for r in rows):5d} {grand['output_tokens']:9d} {grand['cache_creation_input_tokens']:10d} "
          f"{grand['cache_read_input_tokens']:11d} {grand['input_tokens']:7d} {hi:8.2f} {lo:8.2f}")
    print(f"budget ${budget:.0f}: {hi / budget * 100:.0f}% used (high estimate), {lo / budget * 100:.0f}% (low estimate)")


if __name__ == "__main__":
    main()
