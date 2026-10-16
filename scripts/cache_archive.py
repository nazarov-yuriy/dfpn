"""Manage the cache archive (app/archive.py): import a cache directory into it, show statistics, export entries.

  import   archive every entry of a cache directory now, expired or not (for example before deploying a
           version that archives on its own, or before a cache directory is removed)
  stats    entry counts and size
  export   write entries as JSON lines (one per cached response), optionally one key only

usage: python -m scripts.cache_archive import <cache_dir> [--db PATH]
       python -m scripts.cache_archive stats [--db PATH]
       python -m scripts.cache_archive export --out entries.jsonl [--key K] [--db PATH]
  --db defaults to <cache_dir>/../archive.sqlite for import, and to ./archive.sqlite otherwise
       (the service's own default is the same: next to its cache directory, /data/archive.sqlite in the image)."""
import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app.archive import Archive  # noqa: E402


def import_dir(archive, cache_dir):
    added = seen = bad = 0
    for root, _dirs, files in os.walk(cache_dir):
        if os.path.basename(root) == "locks":
            continue
        for name in files:
            if not name.endswith(".json"):
                continue
            seen += 1
            try:
                with open(os.path.join(root, name), encoding="utf-8") as f:
                    entry = json.load(f)
            except (OSError, ValueError):
                bad += 1
                continue
            added += archive.add_entry(name[:-5], entry, "import")
    return {"files": seen, "added": added, "already_archived": seen - added - bad, "unreadable": bad}


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("import"), sub.add_parser("stats"), sub.add_parser("export")
    p[0].add_argument("cache_dir")
    p[2].add_argument("--out", required=True), p[2].add_argument("--key")
    for x in p:
        x.add_argument("--db")
    a = ap.parse_args()
    db = a.db or (os.path.join(os.path.dirname(os.path.abspath(a.cache_dir)), "archive.sqlite") if a.cmd == "import"
                  else "archive.sqlite")
    archive = Archive(db)
    if a.cmd == "import":
        print(json.dumps({"db": db, **import_dir(archive, a.cache_dir)}))
    elif a.cmd == "stats":
        print(json.dumps(archive.stats(), indent=1))
    else:
        n = 0
        with open(a.out, "w", encoding="utf-8") as fo:
            for row in archive.rows(a.key):
                fo.write(json.dumps(row, ensure_ascii=False) + "\n")
                n += 1
        print(f"{n} entries written to {a.out}")


if __name__ == "__main__":
    main()
