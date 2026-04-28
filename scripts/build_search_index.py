#!/usr/bin/env python3
"""Build /data/search_index.json — lightweight global search for the frontend.

Powers the Cmd+K / header search bar. Optimized for size (~150-300 KB) so
it loads instantly on every page.

Includes:
  - Top L1 + L2 programme nodes from the budget tree (~500)
  - All 400 hand-curated suppliers
  - Top 2,000 v2 suppliers by FY 2024 spend
  - Top 500 buyers by FY 2024 spend
  - All 39 insights

Each entry: { name, kind, target } where target is a deep-link path.

Schema:
  {
    "version": 1,
    "generated_at": "...",
    "items": [
      {"n":"DEPARTMENT FOR WORK AND PENSIONS","k":"prog","t":"explore:0"},
      {"n":"Atos Healthcare","k":"sup-curated","t":"sup:01432832"},
      {"n":"Cambridgeshire County Council","k":"buyer","t":"buyer:cambridgeshire-county-council__cb31bw"},
      {"n":"PIP claimant numbers","k":"insight","t":"insight:welfare/pip_caseload"},
      ...
    ]
  }
"""
import json
import sys
import datetime as dt
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
sys.setrecursionlimit(50000)

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "data/search_index.json"

items = []

# 1. Programme nodes — top L1 + selective L2
tree = json.loads((ROOT / "data/uk/uk_budget_tree_2024.json").read_text(encoding="utf-8"))
for i, c1 in enumerate(tree.get("children") or []):
    if not c1.get("name"):
        continue
    items.append({"n": c1["name"], "k": "prog", "t": f"explore:{i}", "v": c1.get("value", 0)})
    # L2 children (only those with > £100M for relevance)
    for j, c2 in enumerate(c1.get("children") or []):
        if (c2.get("value") or 0) > 1e8 and c2.get("name"):
            items.append({"n": c2["name"], "k": "prog", "t": f"explore:{i},{j}", "v": c2.get("value", 0)})

# 2. Curated suppliers (all 400)
cur = json.loads((ROOT / "data/suppliers/_index.json").read_text(encoding="utf-8"))
for s in cur:
    if not s.get("display_name"):
        continue
    items.append({
        "n": s["display_name"],
        "k": "sup-curated",
        "t": f"sup:{s.get('company_number','')}",
        "v": s.get("total_gbp_2024", 0),
    })

# 3. V2 suppliers top 2,000 by £
v2 = json.loads((ROOT / "data/suppliers_v2/_index.json").read_text(encoding="utf-8"))
v2_arr = [(ch, e) for ch, e in v2.items() if e.get("display_name")]
v2_arr.sort(key=lambda x: -(x[1].get("total_gbp_2024") or 0))
seen_curated_ch = {s.get("company_number") for s in cur}
n_v2_added = 0
for ch, e in v2_arr:
    if ch in seen_curated_ch:
        continue  # avoid dup with curated
    if n_v2_added >= 2000:
        break
    items.append({
        "n": e["display_name"],
        "k": "sup-v2",
        "t": f"sup:{ch}",
        "v": e.get("total_gbp_2024", 0),
    })
    n_v2_added += 1

# 4. Buyers top 500 by £
buyers = json.loads((ROOT / "data/map/buyers.json").read_text(encoding="utf-8"))
b_arr = [(bid, b) for bid, b in buyers.items() if b.get("name")]
b_arr.sort(key=lambda x: -(x[1].get("total_gbp_2024") or 0))
for bid, b in b_arr[:500]:
    items.append({
        "n": b["name"],
        "k": "buyer",
        "t": f"buyer:{bid}",
        "v": b.get("total_gbp_2024", 0),
    })

# 5. Insights
try:
    ins_idx = json.loads((ROOT / "data/insights/_index.json").read_text(encoding="utf-8"))
    for cat_key, cat in (ins_idx.get("categories") or {}).items():
        for it in (cat.get("items") or []):
            items.append({
                "n": it.get("title", "?"),
                "k": "insight",
                "t": f"insight:{cat_key}/{it.get('id','')}",
                "v": 0,
            })
except FileNotFoundError:
    pass

# Dedup by (name, kind) — keep largest £
seen = {}
for it in items:
    key = (it["n"].lower(), it["k"])
    if key not in seen or it["v"] > seen[key]["v"]:
        seen[key] = it
items = list(seen.values())

# Sort by £ desc within each kind, then write
items.sort(key=lambda x: (x["k"], -x.get("v", 0)))

out = {
    "version": 1,
    "generated_at": dt.datetime.now(dt.timezone.utc).isoformat(),
    "n_items": len(items),
    "items": items,
}
OUT.write_text(json.dumps(out, ensure_ascii=False), encoding="utf-8")
size_kb = OUT.stat().st_size / 1024
print(f"Wrote {OUT}  ·  {len(items):,} items  ·  {size_kb:.1f} KB")

# Breakdown
from collections import Counter
ck = Counter(it["k"] for it in items)
for k, n in sorted(ck.items()):
    print(f"  {k:15s} {n:>6,}")
