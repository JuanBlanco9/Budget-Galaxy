"""Build D4_07 Premises (other) brief from tree.

Walks the budget tree to find every NHS trust with a 'Premises (other)' sub-line
at depth 5 (under Trust → Operating Costs → Premises (other) or similar).

Output:
  scripts/hand_curation_briefs/D4_07_premises.md
  scripts/hand_curation_briefs/D4_07_premises_{A,B,C,D}.json
"""
import json
import re
import sys
from pathlib import Path
from collections import Counter

sys.stdout.reconfigure(encoding='utf-8')

ext = json.load(open('data/uk/node_enrichment_extended.json', encoding='utf-8'))
tree = json.load(open('data/uk/uk_budget_tree_2024.json', encoding='utf-8'))

# Walk tree, find every node named exactly 'Premises (other)' (or similar variants)
PREMISES_NAMES = {'Premises (other)', 'Premises - other', 'Premises (Other)'}

rows = []
def walk(n, chain=[]):
    name = n.get('name', '')
    v = n.get('value') or 0
    if name in PREMISES_NAMES and len(chain) >= 2:
        # chain[-1] is parent line (e.g. 'Operating Costs' or 'Premises'), chain[-2] is the trust
        trust = chain[-2]
        if re.search(r'Trust|Health Board|Commissioning', trust, re.I):
            rows.append({'trust': trust, 'sub_line': name, 'value': v, 'parent_line': chain[-1]})
    for c in (n.get('children') or []):
        walk(c, chain + [name])
walk(tree)

print(f'Found {len(rows)} Premises (other) sub-lines under NHS trusts')

# Filter >= £100k + dedupe
rows = [r for r in rows if r['value'] >= 1e5]
seen = {}
for r in rows:
    k = (r['trust'], r['sub_line'])
    if k not in seen or r['value'] > seen[k]['value']:
        seen[k] = r
rows = sorted(seen.values(), key=lambda x: -x['value'])
print(f'After £100k filter + dedupe: {len(rows)} trusts')

# Skip trusts already covered (composite key already in enrichment)
existing = set(ext['entries'].keys())
def composite(r):
    return f"{r['sub_line']} \u2014 {r['trust']}"
new_rows = [r for r in rows if composite(r) not in existing]
print(f'Already in enrichment: {len(rows)-len(new_rows)}')
print(f'Remaining to curate: {len(new_rows)}')

def find_category(trust_name):
    cats = {'NHS Acute Trusts', 'NHS Specialist Trusts', 'NHS Community Trusts',
            'NHS Mental Health Trusts', 'NHS Ambulance Trusts'}
    def w(n, ch):
        if n.get('name') == trust_name:
            for anc in reversed(ch):
                if anc in cats:
                    return anc
            return ch[-1] if ch else '?'
        for c in (n.get('children') or []):
            r = w(c, ch + [n.get('name','')])
            if r: return r
        return None
    return w(tree, []) or '?'

selected = new_rows
cat_counts = Counter()
for r in selected:
    r['category'] = find_category(r['trust'])
    cat_counts[r['category']] += 1
print(f'Category spread: {dict(cat_counts)}')

brief_path = Path('scripts/hand_curation_briefs/D4_07_premises.md')
brief_path.write_text(f"""# Cluster D4_07 Premises (other) — NHS Trust depth-5 sub-lines

Scope: {len(selected)} NHS trust 'Premises (other)' sub-lines · total £{sum(r['value'] for r in selected)/1e9:.2f}B

## What 'Premises (other)' covers

Every NHS provider trust has a 'Premises' line in its accounts capturing estate
operating costs OUTSIDE the depreciation/amortisation lines. 'Premises (other)'
is the residual within Premises — building maintenance, hard FM contracts,
soft FM (cleaning, catering insourced), grounds maintenance, water + sewerage,
refuse, fire safety contracts, security, pest control, parking management,
sustainability/Net Zero retrofit operational costs.

## Key 2024-25 context anchors

- **NHS Net Zero (DHSC)** target for direct emissions 2040 has driven LED
  retrofit, heat-pump installations, BMS upgrades — visible in Premises (other)
  for trusts mid-program.
- **RAAC concrete crisis** (Reinforced Autoclaved Aerated Concrete): 27 trusts
  affected per HSSIB Sep 2023, with Premises (other) inflated by mitigation
  works (props, decant, monitoring).
- **NHP (New Hospital Programme) Reset** announced 20 Jan 2025 by Streeting:
  some trusts had budgeted for new builds, now decant/temporary works extending.
- **Industrial action 2023-24** had MINOR Premises (other) impact (security
  + extra catering for picket-line management).
- **PFI unitary charges are NOT in Premises (other)** — separate D4_11 line.
- **Business rates are NOT in Premises (other)** — separate D4_13 line.
- **Energy contracts (NHS Crown Commercial Service)** — most trusts on RM6011
  framework; price spikes 2022-23 partial pass-through to 2024-25 budgets.
- **Construction inflation 2024-25** ~5-7% on hard FM contracts.

## Specialty mix anchors by category

- **Acute Trusts** (~75% of clusters here): multi-site means heavier estate
  load — large hospitals + community sites + ambulances + warehouses.
- **Specialist** (cancer / cardiac / orthopaedic): single-site typically,
  but specialty equipment power demands inflate utilities.
- **Mental Health**: section 136 suites + PICU + ECT room conditions key;
  RAAC affected several MH estates (Edenfield, Tees Esk).
- **Community**: clinic estate + some inpatient (community hospitals).
- **Ambulance**: ambulance stations, HART bases, training centres,
  vehicle workshops + fuel costs.

## Schema per entry

```python
"Premises (other) \u2014 <trust>": {{
    "aliases": [{{"name": "Premises (other)", "parent": "<trust>"}}],
    "description": "2-3 sentences trust-specific (estate footprint, key sites, hard/soft FM contract holder, sustainability stage)",
    "beneficiaries": "Patients + staff at trust sites — be specific (5 hospitals · X ambulance stations · Y community clinics)",
    "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15 (Premises and Equipment)",
    "key_stats": [
        {{"label": "Premises (other) 2024-25", "value": "£<exact from brief>M"}},
        {{"label": "Share of trust total opex", "value": "c. X%"}},
        {{"label": "Estate scale", "value": "e.g. '5 hospital sites + 12 community sites · X m\u00b2 floorspace'"}},
        {{"label": "Hard FM contract", "value": "Holder + contract end date if known"}},
        {{"label": "Soft FM model", "value": "Insourced/outsourced + provider"}},
        {{"label": "RAAC status", "value": "if applicable"}},
        {{"label": "NHP scheme status", "value": "if applicable"}},
        {{"label": "Net Zero milestone", "value": "e.g. 'BMS upgrade 60% complete'"}},
        {{"label": "YoY change", "value": "c. +X% (driver)"}},
        {{"label": "Peer benchmark", "value": "vs trust-category median"}}
    ],  # 6-10 trust-specific
    "notes": "2-4 sentences trust-specific drivers (estate consolidation, RAAC mitigation, energy contract renewals, FM contract bidding cycles, decarbonisation grant funding)",
    "sources": [...],  # 2-3 with https:// URLs (trust AR, NHS ERIC, NHSE provider finance, CQC inspection)
    "related": ["<trust>", "<parent line>"]
}}
```

## Category spread of this brief

""", encoding='utf-8')
with brief_path.open('a', encoding='utf-8') as f:
    for cat, n in cat_counts.most_common():
        f.write(f'- **{cat}**: {n} trusts\n')
    f.write("""
## Hard rules
- Em-dash ` \u2014 ` (U+2014 with spaces) in composite keys
- Scoped alias parent = EXACT trust name (from brief JSON)
- Every source URL `https://`
- 6-10 key_stats per entry, trust-specific
- 2-4 sentence notes, trust-specific (NOT generic NHS-wide)

## Output

Each agent writes `scripts/D4_07_premises_<batch>.py` with `NEW = { ... }` direct dict literal. NO `__main__`, imports, or file mutation.

## Sub-lines in this cluster

""")
    for r in selected:
        f.write(f"""### Premises (other) \u2014 {r['trust']}
  sub-line type: Premises (other)
  parent trust: {r['trust']}
  trust category: {r['category']}
  parent line: {r['parent_line']}
  value: £{r['value']/1e6:.2f}M

""")
print(f'Wrote {brief_path}')

# Split into 4 batches
batches = [selected[i::4] for i in range(4)]
for i, b in enumerate(batches):
    p = Path(f'scripts/hand_curation_briefs/D4_07_premises_{chr(65+i)}.json')
    p.write_text(json.dumps(b, ensure_ascii=False, indent=2), encoding='utf-8')
    print(f'  split {chr(65+i)}: {len(b)} trusts')
