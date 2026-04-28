#!/usr/bin/env python3
"""Build /frontend/sitemap.xml — main static URLs + top programmes + top suppliers + insights.

Strategy: don't list 19k suppliers (too noisy for crawlers), only the
~500 most-visited URLs (top by £ for suppliers, all hand-curated programme
top-levels, all 39 insights, the major tabs).

Run: PYTHONIOENCODING=utf-8 python scripts/build_sitemap.py
"""
import json
import sys
import datetime as dt
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
sys.setrecursionlimit(50000)

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "frontend/sitemap.xml"
BASE = "https://budgetgalaxy.com"
TODAY = dt.date.today().isoformat()

urls = []

def add(loc, lastmod=TODAY, changefreq="weekly", priority="0.5"):
    urls.append({"loc": loc, "lastmod": lastmod, "changefreq": changefreq, "priority": priority})

# 1. Main tabs (high priority)
add(BASE + "/",                         priority="1.0", changefreq="daily")
add(BASE + "/#galaxy",                  priority="0.9", changefreq="weekly")
add(BASE + "/#explore",                 priority="0.9", changefreq="weekly")
add(BASE + "/#suppliers",               priority="0.9", changefreq="weekly")
add(BASE + "/#taxpayer",                priority="0.9", changefreq="weekly")
add(BASE + "/#insights",                priority="0.8", changefreq="weekly")
add(BASE + "/#about",                   priority="0.6", changefreq="monthly")

# 2. All hand-curated programme L1 nodes (60 deps)
try:
    tree = json.loads((ROOT / "data/uk/uk_budget_tree_2024.json").read_text(encoding="utf-8"))
    for i, c in enumerate(tree.get("children") or []):
        if (c.get("value") or 0) < 1e8:
            continue
        add(f"{BASE}/#explore/{i}", priority="0.7", changefreq="monthly")
except FileNotFoundError:
    pass

# 3. Top 100 curated suppliers (by £)
try:
    cur = json.loads((ROOT / "data/suppliers/_index.json").read_text(encoding="utf-8"))
    cur.sort(key=lambda s: -(s.get("total_gbp_2024") or 0))
    for s in cur[:100]:
        ch = s.get("company_number")
        if ch:
            add(f"{BASE}/#suppliers/{ch}", priority="0.7", changefreq="monthly")
except FileNotFoundError:
    pass

# 4. Top 200 v2 enriched suppliers (by £)
try:
    v2 = json.loads((ROOT / "data/suppliers_v2/_index.json").read_text(encoding="utf-8"))
    v2_arr = sorted(v2.items(), key=lambda kv: -(kv[1].get("total_gbp_2024") or 0))
    for ch, e in v2_arr[:200]:
        add(f"{BASE}/#suppliers/{ch}", priority="0.6", changefreq="monthly")
except FileNotFoundError:
    pass

# 5. All insights
try:
    ins_idx = json.loads((ROOT / "data/insights/_index.json").read_text(encoding="utf-8"))
    for cat_key, cat in (ins_idx.get("categories") or {}).items():
        for it in (cat.get("items") or []):
            iid = it.get("id")
            if iid:
                add(f"{BASE}/#insights/{cat_key}/{iid}", priority="0.6", changefreq="monthly")
except FileNotFoundError:
    pass

# Build XML
parts = ['<?xml version="1.0" encoding="UTF-8"?>']
parts.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')
for u in urls:
    parts.append('  <url>')
    parts.append(f'    <loc>{u["loc"]}</loc>')
    parts.append(f'    <lastmod>{u["lastmod"]}</lastmod>')
    parts.append(f'    <changefreq>{u["changefreq"]}</changefreq>')
    parts.append(f'    <priority>{u["priority"]}</priority>')
    parts.append('  </url>')
parts.append('</urlset>')

OUT.write_text("\n".join(parts) + "\n", encoding="utf-8")
print(f"Wrote {OUT}  ·  {len(urls)} URLs  ·  {OUT.stat().st_size/1024:.1f} KB")
