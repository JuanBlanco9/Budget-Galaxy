"""Build D4_08 Impairments net of reversals brief from tree."""
import json
import re
import sys
from pathlib import Path
from collections import Counter

sys.stdout.reconfigure(encoding='utf-8')

ext = json.load(open('data/uk/node_enrichment_extended.json', encoding='utf-8'))
tree = json.load(open('data/uk/uk_budget_tree_2024.json', encoding='utf-8'))

NAMES = {'Impairments net of reversals'}
rows = []
def walk(n, chain=[]):
    name = n.get('name', '')
    v = n.get('value') or 0
    if name in NAMES and len(chain) >= 2:
        trust = chain[-2]
        if re.search(r'Trust|Health Board|Commissioning', trust, re.I):
            rows.append({'trust': trust, 'sub_line': name, 'value': v, 'parent_line': chain[-1]})
    for c in (n.get('children') or []):
        walk(c, chain + [name])
walk(tree)
print(f'Found: {len(rows)}')

rows = [r for r in rows if r['value'] >= 1e5]
seen = {}
for r in rows:
    k = (r['trust'], r['sub_line'])
    if k not in seen or r['value'] > seen[k]['value']:
        seen[k] = r
rows = sorted(seen.values(), key=lambda x: -x['value'])

existing = set(ext['entries'].keys())
new = [r for r in rows if f"{r['sub_line']} — {r['trust']}" not in existing]
print(f'Already covered: {len(rows)-len(new)}, new to curate: {len(new)}')

def find_category(trust_name):
    cats = {'NHS Acute Trusts', 'NHS Specialist Trusts', 'NHS Community Trusts',
            'NHS Mental Health Trusts', 'NHS Ambulance Trusts'}
    def w(n, ch):
        if n.get('name') == trust_name:
            for anc in reversed(ch):
                if anc in cats: return anc
            return ch[-1] if ch else '?'
        for c in (n.get('children') or []):
            r = w(c, ch + [n.get('name','')])
            if r: return r
        return None
    return w(tree, []) or '?'

cat_counts = Counter()
for r in new:
    r['category'] = find_category(r['trust'])
    cat_counts[r['category']] += 1
print(f'Category spread: {dict(cat_counts)}')

# Brief
brief_path = Path('scripts/hand_curation_briefs/D4_08_impairments.md')
brief_path.write_text(f"""# Cluster D4_08 Impairments net of reversals — NHS Trust depth-4

Scope: {len(new)} NHS trust 'Impairments net of reversals' sub-lines · total £{sum(r['value'] for r in new)/1e9:.2f}B

## Archetype: PROGRAMME (per docs/archetype_briefs.md)

Required dimensions per entry: Delivery body · Policy owner · Beneficiary count · Funding trajectory · Evaluation evidence · Predecessor/successor

## What 'Impairments net of reversals' covers

Non-cash accounting writedowns of trust capital assets, primarily driven by:
- **Modern Equivalent Asset (MEA) revaluation** — annual DHSC valuation reassessment of NHS estate (5-year cycle for buildings, indexed via VOA in interim years). Negative deltas hit this line.
- **Net realisable value impairment** — when a building's market value drops below carrying value (e.g. listed-buildings becoming non-functional, RAAC-affected sites awaiting decant)
- **Reversals** — write-up if value recovers (rare for NHS estate)

Treatment per IAS 36 (Impairment of Assets) + DHSC Group Accounting Manual 2024-25 Chapter 4.

## Key 2024-25 context anchors

- **RAAC crisis impairments** — trusts with concrete-plank failures (HSSIB list Sep 2023) booked impairment when remedial cost > MEA-DRC value. Examples: Frimley Park, Whipps Cross, Hinchingbrooke, Royal Devon NDDH, Mid Cheshire, Princess Alexandra.
- **NHP Reset Jan 2025** — trusts in original NHP cohort had carrying values held against expected new build; Reset deferral triggered impairment review on existing structures (Imperial St Mary's, Leeds, Hull, Bedfordshire).
- **MEA-DRC revaluation cycle** — 5-yearly full revaluation due 2024-25 for many trusts (last full 2019-20). Indexation in interim years uses VOA. Results vary by region (London inflation higher than rural).
- **Listed-building constraints** — heritage estate (RUH Bath WHS, QVH McIndoe, Tavistock) often impaired when modernisation cost exceeds MEA.
- **Coastal salt-corrosion** — impairment risk at coastal trusts (Blackpool, Pilgrim Boston, Conquest, Eastbourne, Margate ESHT).

## Schema per entry (PROGRAMME contract floors)

```python
"Impairments net of reversals — <trust>": {{
    "aliases": [{{"name": "Impairments net of reversals", "parent": "<trust>"}}],
    "description": "3-5 sentences, 250-600 chars · trust-specific impairment driver (RAAC / NHP / heritage / coastal / merger transition / specialty equipment)",
    "beneficiaries": "1-2 sentences · concrete N (sites with assets impaired, m² affected, replacement-vs-impair decision)",
    "legal_basis": "IAS 36 Impairment of Assets · DHSC Group Accounting Manual 2024-25 ch.4 · NHS Act 2006 · Health and Care Act 2022 · IFRS 13 Fair Value Measurement",
    "key_stats": [...],  # 8-12 trust-specific (£ this year, 5-year trend, MEA-DRC vs market, RAAC scope, NHP status, valuation cycle phase, peer comparison)
    "notes": "3-5 sentences, 300-800 chars · trust-specific drivers + recent context (RAAC mitigation, NHP Reset deferral cost, valuation cycle, listed-building constraints)",
    "sources": [...],  # 4-6 dicts {{publisher, title, url}} https://
    "related": [...]   # 3-6 cross-links: trust + Premises (other) cross-ref + RAAC affected peers + NHP cohort + parent line
}}
```

## PROGRAMME dimensions (must hit each entry)
1. **Delivery body**: trust Estates & Facilities · external valuer (often Cushman & Wakefield, JLL, GVA for NHS)
2. **Policy owner**: DHSC + NHSE Provider Finance · IAS 36 / DHSC GAM oversight
3. **Beneficiary count**: concrete N (assets impaired, m², replacement timeline)
4. **Funding trajectory**: 3-5 year impairment trend (volatile · spike years vs base years)
5. **Evaluation evidence**: NAO Estate report · HSSIB RAAC alert · CQC infrastructure findings · DHSC ARA disclosure
6. **Predecessor/successor**: prior valuation cycle outcome · current write-down · planned NHP rebuild or retain-and-refurbish

## Specialty mix per category
- **Acute** (~118 trusts in scope): biggest impairments by £ · multi-site MEA volatility · RAAC + NHP exposure
- **Specialist**: lower volume, but big impairments when single-site equipment becomes obsolete (PBT cyclotron, MRI replacement cycles)
- **Mental Health**: heritage + listed building impairments · forensic-secure perimeter constraints
- **Community**: smaller values · NHSPS-leased estate so impairments lower (NHSPS holds the asset)
- **Ambulance**: vehicle fleet impairments · station refresh cycle

## Category spread of this brief

""", encoding='utf-8')
with brief_path.open('a', encoding='utf-8') as f:
    for cat, n in cat_counts.most_common():
        f.write(f'- **{cat}**: {n} trusts\n')
    f.write('\n## Hard rules\n- Em-dash ` — ` (U+2014)\n- Scoped alias parent = EXACT trust name\n- Sources = list of dicts with `https://` URLs\n- 8-12 stats · 4-6 sources · 3-6 related · 3-5 sentence notes/desc\n- All 6 PROGRAMME dimensions present\n- Watchdog-safe incremental Edit (skeleton + per-entry inserts)\n\n## Sub-lines in this cluster\n\n')
    for r in new:
        f.write(f"### Impairments net of reversals — {r['trust']}\n  parent trust: {r['trust']}\n  trust category: {r['category']}\n  parent line: {r['parent_line']}\n  value: £{r['value']/1e6:.2f}M\n\n")

print(f'Wrote {brief_path}')

# Split into chunks of 17
CHUNK = 17
for i in range(0, len(new), CHUNK):
    chunk = new[i:i+CHUNK]
    label = f'D4_08_chunk{(i//CHUNK)+1:02d}'
    p = Path(f'scripts/hand_curation_briefs/{label}.json')
    p.write_text(json.dumps(chunk, ensure_ascii=False, indent=2), encoding='utf-8')
    print(f'  {label}: {len(chunk)} trusts')
