"""Wave 1 setup: (1) tier-3 entries £1B-£5B, (2) D4_06 Clinical supplies brief,
(3) tier-2 URLs extracted for URL-repair agent."""
import json
import sys
import re
from pathlib import Path
from collections import defaultdict, Counter

sys.stdout.reconfigure(encoding='utf-8')

ext = json.load(open('data/uk/node_enrichment_extended.json', encoding='utf-8'))
tree = json.load(open('data/uk/uk_budget_tree_2024.json', encoding='utf-8'))

name_values = {}
def walk_vals(n):
    name = n.get('name')
    v = n.get('value') or 0
    if name and v > name_values.get(name, 0):
        name_values[name] = v
    for c in (n.get('children') or []):
        walk_vals(c)
walk_vals(tree)

def entry_value(k, e):
    cands = [k]
    for a in (e.get('aliases') or []):
        if isinstance(a, dict) and a.get('name'):
            cands.append(a['name'])
        elif isinstance(a, str):
            cands.append(a)
    return max((name_values.get(c, 0) for c in cands), default=0)

# ===== (1) TIER 3 [£1B, £5B) =====
TIER3_LO = 1e9
TIER3_HI = 5e9
ranked = [(k, entry_value(k, e), e) for k, e in ext['entries'].items()]
tier3 = [(k, v, e) for k, v, e in ranked if TIER3_LO <= v < TIER3_HI]
tier3.sort(key=lambda x: -x[1])

# Drop fallback-value clusters
val_counts = Counter(round(v/1e6) for k,v,e in tier3)
suspicious = {v for v,n in val_counts.items() if n > 3}
clean = [(k,v,e) for k,v,e in tier3 if round(v/1e6) not in suspicious]
print(f'Tier 3 [£1B,£5B): {len(tier3)} raw · {len(tier3)-len(clean)} dropped · {len(clean)} kept')

# Skip if already in tier-2 list
tier2_keys = set(x['key'] for x in json.load(open('data/uk/factcheck/tier2_entries.json', encoding='utf-8')))
clean = [(k,v,e) for k,v,e in clean if k not in tier2_keys]

# Cap at 100 for budget
TIER3_CAP = 100
out_tier3 = []
for k, v, e in clean[:TIER3_CAP]:
    out_tier3.append({
        'key': k, 'value_gbp': v,
        'urls': [s.get('url') for s in (e.get('sources') or []) if isinstance(s, dict) and s.get('url')],
        'n_stats': len(e.get('key_stats') or []),
        'description': e.get('description'),
        'notes': e.get('notes'),
        'key_stats': e.get('key_stats'),
        'sources': e.get('sources'),
    })
json.dump(out_tier3, open('data/uk/factcheck/tier3_entries.json','w', encoding='utf-8'), indent=2, ensure_ascii=False)
print(f'Wrote data/uk/factcheck/tier3_entries.json · {len(out_tier3)} entries')

# ===== (2) D4_06 CLINICAL SUPPLIES BRIEF =====
# Tree node names: 'Clinical supplies & services' (206 trusts per earlier grep)
cs_names = {'Clinical supplies & services', 'Clinical Supplies & Services'}
cs_rows = []
def walk_cs(n, chain=[]):
    name = n.get('name','')
    v = n.get('value') or 0
    if name in cs_names and len(chain) >= 2:
        trust = chain[-2]
        if re.search(r'Trust|Health Board|Commissioning', trust, re.I):
            cs_rows.append({'trust': trust, 'sub_line': name, 'value': v})
    for c in (n.get('children') or []):
        walk_cs(c, chain + [name])
walk_cs(tree)

# Dedupe + filter >= £1M + not already in enrichment
cs_rows = [r for r in cs_rows if r['value'] >= 1e6]
seen = {}
for r in cs_rows:
    k = (r['trust'], r['sub_line'])
    if k not in seen or r['value'] > seen[k]['value']:
        seen[k] = r
cs_rows = sorted(seen.values(), key=lambda x: -x['value'])

existing = set(ext['entries'].keys())
def composite(r):
    return f"{r['sub_line']} \u2014 {r['trust']}"
new_rows = [r for r in cs_rows if composite(r) not in existing]
print(f'\nD4_06 Clinical supplies & services: {len(cs_rows)} trusts · {len(new_rows)} new')

def find_category(trust_name):
    cats = {'NHS Acute Trusts', 'NHS Specialist Trusts', 'NHS Community Trusts',
            'NHS Mental Health Trusts', 'NHS Ambulance Trusts'}
    def walk(n, chain):
        if n.get('name') == trust_name:
            for anc in reversed(chain):
                if anc in cats:
                    return anc
            return chain[-1] if chain else '?'
        for c in (n.get('children') or []):
            r = walk(c, chain + [n.get('name','')])
            if r: return r
        return None
    return walk(tree, []) or '?'

selected = new_rows
cat_counts = Counter()
for r in selected:
    r['category'] = find_category(r['trust'])
    cat_counts[r['category']] += 1

brief_path = Path('scripts/hand_curation_briefs/D4_06_clinical_supplies.md')
with brief_path.open('w', encoding='utf-8') as f:
    f.write(f"""# Cluster D4_06 Clinical supplies & services (NHS Trusts)

Scope: {len(selected)} trust clinical-supplies sub-lines · total £{sum(r['value'] for r in selected)/1e9:.2f}B

## Task

Each depth-4 "Clinical supplies & services" sub-line under a specific NHS Trust needs a hand-curated Tier A entry that is TAILOR-MADE per-entity. NO generic template. NO shared content.

## Scope (what clinical supplies & services covers)
- Surgical supplies (sutures · meshes · prostheses · single-use instruments)
- Diagnostic reagents (pathology · histopathology · POC tests)
- Blood products (NHSBT invoiced per bag)
- Oxygen and medical gases (BOC contract)
- Dressings / wound-care (procured via NHS Supply Chain Medical category)
- Theatre packs / custom procedure packs
- Radiology contrast media
- Consumables for devices (pacemaker leads · hip stems · knee trays · CGM sensors)
- NOT drugs (those are D4_05, separate line)
- NOT premises / IT (separate lines)

## Key context 2024-25
- **NHS Supply Chain** delivers 80%+ via category management (Medical, FFD - Food/Facilities, ORCA)
- **High-cost devices** (HCDs) commissioning split — some devices pass through trust ClinSupp, others ICB-commissioned
- **VAT** on clinical supplies: UK VAT refund for NHS (since 1984) — zero-rate via RCS reclaim — usually NOT visible in trust Drug/ClinSupp gross
- **Industrial action 2023-24**: elective cancellations reduced theatre-consumable spend (partial rebound 2024-25)
- **CNST** (Clinical Negligence Scheme for Trusts) is NOT Clinical supplies — that's NHS Resolution premium, separate
- **Sustainability (DHSC Net Zero)**: pressure to switch from single-use to reusable instruments impacting post-2024 procurement strategy

## Schema per entry
```python
"Clinical supplies & services \u2014 <trust>": {{
    "aliases": [{{"name": "Clinical supplies & services", "parent": "<trust>"}}],
    "description": "2-3 sentences trust-specific clinical supplies (surgical volume · specialty mix · consumable-heavy specialties)",
    "beneficiaries": "Patients undergoing procedures / diagnostics / treatment at trust sites",
    "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Terms and Conditions for the Supply of Goods and Services",
    "key_stats": [
        {{"label": "Clinical supplies & services 2024-25", "value": "£<exact from brief>M"}},
        {{"label": "Share of trust total opex", "value": "c. X%"}},
        {{"label": "Activity anchor", "value": "e.g. 'c.140k elective admissions/yr'"}},
        {{"label": "Biggest sub-category", "value": "e.g. 'Orthopaedic implants ~20% (hip/knee/trauma)'"}},
        {{"label": "Supply-chain channel", "value": "NHS Supply Chain Medical ~80% · direct ~20%"}},
        {{"label": "YoY change", "value": "c. +X% nominal"}},
        {{"label": "Peer benchmark", "value": "£/elective or per bed-day vs peer"}},
        {{"label": "Theatre activity", "value": "N theatres · M sessions/yr"}}
    ],  # 6-10 trust-specific stats
    "notes": "2-4 sentences trust-specific drivers (high-volume specialties like orthopaedics · cardiology · vascular · radiotherapy devices · infection-control pressures · CCRW robotic surgery scaling · contract renegotiation dates · supply-chain incidents 2024-25)",
    "sources": [...],  # 2-3 with https:// URLs
    "related": ["<trust>", "Drugs costs \u2014 <trust>"]
}}
```

## Specialty-mix anchors by category
- **Acute Trusts**: ~12-18% of trust opex · driven by surgery volume · orthopaedic implants · cardiology stents · vascular grafts
- **Specialist Trusts** (cancer / cardiac / orthopaedic): higher share 20-25% · prostheses · specialty devices · robot consumables
- **Mental Health Trusts**: LOW (1-3%) · mostly restraint devices · ward diagnostics · PPE
- **Community Trusts**: LOW-MEDIUM (3-6%) · wound-care · continence · catheters · home respiratory
- **Ambulance Trusts**: MEDIUM · defibrillator consumables · trauma packs · O2 cylinders · stretchers

## Category spread of this brief
""")
    for cat, n in cat_counts.most_common():
        f.write(f'- **{cat}**: {n} trusts\n')
    f.write(f"""
## Rules
- Em-dash ` \u2014 ` (U+2014 with spaces) in composite keys
- Scoped alias parent = EXACT trust name (from brief JSON)
- Every source with https:// URL
- Use £ value from the brief JSON as anchor
- 6-10 key_stats per entry
- Trust-specific notes, NOT generic NHS-wide

## Output
Write `scripts/D4_06_clinical_<batch>.py` with `NEW = {{ ... }}` direct dict literal.

## Sub-lines in this cluster

""")
    for r in selected:
        f.write(f"""### Clinical supplies & services \u2014 {r['trust']}
  sub-line type: Clinical supplies & services
  parent trust: {r['trust']}
  trust category: {r['category']}
  value: £{r['value']/1e6:.2f}M

""")

print(f'Wrote {brief_path}')

# Split into 4 batches
batches = [selected[i::4] for i in range(4)]
for i, batch in enumerate(batches):
    split_path = Path(f'scripts/hand_curation_briefs/D4_06_clinical_{chr(65+i)}.json')
    split_path.write_text(json.dumps(batch, ensure_ascii=False, indent=2), encoding='utf-8')
    print(f'  split {chr(65+i)}: {len(batch)} trusts')

# ===== (3) TIER-2 URLs list (for tier-2 URL-repair agent) =====
# Use existing tier2_entries.json URLs
t2 = json.load(open('data/uk/factcheck/tier2_entries.json', encoding='utf-8'))
t2_urls = []
for e in t2:
    for u in e.get('urls', []):
        t2_urls.append((e['key'], u))
print(f'\nTier-2 URLs to check: {len(t2_urls)}')
