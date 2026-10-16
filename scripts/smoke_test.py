"""Smoke-test a running service: each mode on a few queries, plus auth checks. Never prints keys.

usage: python scripts/smoke_test.py --base-url http://localhost:8000 --key-file path/to/service_key
           [--byok-key-file path/to/tavily_key] [--modes basic,better,harder]
"""
import argparse
import json
import time
import urllib.error
import urllib.request

QUERIES = ["Who runs Puffin Croft?",
           "MiniMax-M3 release date license open source multimodal reasoning",
           "Какие последние сделки были на российском рынке нефти и газа?"]


def search(base, key, body):
    req = urllib.request.Request(f"{base}/search", data=json.dumps(body).encode(), method="POST",
                                 headers={"Content-Type": "application/json", "Authorization": f"Bearer {key}"})
    t0 = time.time()
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            return r.status, json.loads(r.read()), time.time() - t0
    except urllib.error.HTTPError as e:
        return e.code, json.loads(e.read() or b"{}"), time.time() - t0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--base-url", default="http://localhost:8000"), ap.add_argument("--key-file", required=True)
    ap.add_argument("--byok-key-file"), ap.add_argument("--modes", default="basic,better,harder")
    a = ap.parse_args()
    key = open(a.key_file).read().strip()
    print("health:", urllib.request.urlopen(f"{a.base_url}/health", timeout=10).read().decode())
    for mode in a.modes.split(","):
        for q in QUERIES:
            st, data, dt = search(a.base_url, key, {"query": q, "search_depth": mode, "max_results": 5,
                                                    "include_usage": True})
            res = data.get("results") or []
            print(f"[{mode:8s}] {st} {dt:5.1f}s credits={(data.get('usage') or {}).get('credits')} "
                  f"n={len(res)} | {q[:45]}")
            for r in res[:3]:
                print(f"      {r.get('score', 0):.3f} {r.get('url', '')[:95]}")
    st, data, _ = search(a.base_url, "tvly-definitely-not-a-key", {"query": "smoke test query", "search_depth": "harder"})
    print("invalid key:", st, data)
    if a.byok_key_file:
        st, data, dt = search(a.base_url, open(a.byok_key_file).read().strip(),
                              {"query": QUERIES[0], "search_depth": "better", "max_results": 3})
        print(f"byok key (better): {st} {dt:.1f}s n={len(data.get('results') or [])}")


if __name__ == "__main__":
    main()
