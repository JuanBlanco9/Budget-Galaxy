"""Build (1) tier-2 entries [£5B-£30B] for fact-check, and (2) D4_05 Drugs costs brief."""
import json
import sys
import re
from pathlib import Path
from collections import defaultdict

sys.stdout.reconfigure(encoding='utf-8')

ext = json.load(open('data/uk/node_enrichment_extended.json', encoding='utf-8'))
tree = json.load(open('data/uk/uk_budget_tree_2024.json', encoding='utf-8'))

# Build {name -> max value} from tree walk
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

# ---------- (1) TIER 2 [£5B, £30B) ----------
TIER2_LO = 5e9
TIER2_HI = 30e9
ranked = [
    (k, entry_value(k, e), e)
    for k, e in ext['entries'].items()
]
tier2 = [(k, v, e) for k, v, e in ranked if TIER2_LO <= v < TIER2_HI]
tier2.sort(key=lambda x: -x[1])

# De-duplicate suspicious default-value entries (we saw a £28.25B cluster earlier where
# unmatched entries fell back to a spurious shared value). Drop entries tied on the exact
# same value with count > 3 (heuristic — signals fallback not real £).
from collections import Counter
val_counts = Counter(round(v/1e6) for k,v,e in tier2)
suspicious_vals = {v for v,n in val_counts.items() if n > 3}
clean_tier2 = [(k,v,e) for k,v,e in tier2 if round(v/1e6) not in suspicious_vals]
dropped = len(tier2) - len(clean_tier2)
print(f'Tier 2 [£5B, £30B): {len(tier2)} raw · {dropped} dropped as fallback-value cluster · {len(clean_tier2)} kept')

out_tier2 = []
for k, v, e in clean_tier2[:60]:  # cap at 60 for batch budget
    urls = [s.get('url') for s in (e.get('sources') or []) if isinstance(s, dict) and s.get('url')]
    out_tier2.append({
        'key': k,
        'value_gbp': v,
        'urls': urls,
        'n_stats': len(e.get('key_stats') or []),
        'description': e.get('description'),
        'notes': e.get('notes'),
        'key_stats': e.get('key_stats'),
        'sources': e.get('sources'),
    })

Path('data/uk/factcheck').mkdir(parents=True, exist_ok=True)
json.dump(out_tier2, open('data/uk/factcheck/tier2_entries.json','w', encoding='utf-8'), indent=2, ensure_ascii=False)
print(f'Wrote data/uk/factcheck/tier2_entries.json · {len(out_tier2)} entries')
print('\nFirst 30 tier-2 entries:')
for i, (k, v, _) in enumerate(clean_tier2[:30], 1):
    print(f'  {i:2d}. £{v/1e9:>6.2f}B  {k[:70]}')

# ---------- (2) D4_05 DRUGS BRIEF ----------
# Walk tree, find every node whose name contains drug-like keyword at depth matching
# 'Drug Costs' or 'Drugs' as a sub-line of 'Clinical Supplies & Drugs' or similar.
# The depth-4 tree structure per trust is:
#   NHS Provider Sector → <category> → <trust> → Clinical Supplies & Drugs → Drug Costs (depth-5 from root)
# We want the {trust → drug sub-line value} mapping.

drug_names = {'Drugs costs', 'Drug Costs', 'Drugs'}

drug_rows = []  # list of (trust, sub-line name, value, parent chain)
def walk_drugs(n, chain=[]):
    name = n.get('name','')
    v = n.get('value') or 0
    if name in drug_names and len(chain) >= 2:
        # parent chain typically: [root, ..., trust_category, trust_name, 'Clinical Supplies & Drugs']
        # The trust is chain[-2] (since chain[-1] is 'Clinical Supplies & Drugs')
        parent_line = chain[-1] if chain else ''
        trust = chain[-2] if len(chain) >= 2 else ''
        # Filter to trusts (heuristic: name contains 'Trust' or 'Foundation Trust' or 'Health Board')
        if re.search(r'Trust|Health Board|Commissioning', trust, re.I):
            drug_rows.append({'trust': trust, 'sub_line': name, 'value': v, 'parent_line': parent_line})
    for c in (n.get('children') or []):
        walk_drugs(c, chain + [name])
walk_drugs(tree)

print(f'\nFound {len(drug_rows)} drug sub-line nodes under NHS trusts')

# Filter out tiny lines (< £1M — noise)
drug_rows = [r for r in drug_rows if r['value'] >= 1e6]
# Dedupe by (trust, sub_line) keep max value
seen = {}
for r in drug_rows:
    k = (r['trust'], r['sub_line'])
    if k not in seen or r['value'] > seen[k]['value']:
        seen[k] = r
drug_rows = sorted(seen.values(), key=lambda x: -x['value'])
print(f'After £1M+ filter + dedupe: {len(drug_rows)} trusts')

# Check which are already in enrichment
existing = set(ext['entries'].keys())
def composite(r):
    return f"{r['sub_line']} \u2014 {r['trust']}"
new_rows = [r for r in drug_rows if composite(r) not in existing]
print(f'Already in enrichment: {len(drug_rows)-len(new_rows)}')
print(f'Remaining to curate: {len(new_rows)}')

# Determine category for each trust from its tree ancestry
def find_category(trust_name):
    """Walk tree to find the immediate parent of trust_name (should be a category)."""
    def walk(n, chain):
        if n.get('name') == trust_name:
            # return nearest category ancestor
            for anc in reversed(chain):
                if anc in {'NHS Acute Trusts', 'NHS Specialist Trusts', 'NHS Community Trusts',
                          'NHS Mental Health Trusts', 'NHS Ambulance Trusts', 'NHS Provider Sector'}:
                    return anc
            return chain[-1] if chain else '?'
        for c in (n.get('children') or []):
            r = walk(c, chain + [n.get('name','')])
            if r: return r
        return None
    return walk(tree, []) or '?'

# Build brief file content
LIM = 206  # target 206 trusts per handoff
selected = new_rows[:LIM] if len(new_rows) > LIM else new_rows
print(f'Selected top-{len(selected)} by £ for the brief')

from collections import Counter
cat_counts = Counter()
for r in selected:
    r['category'] = find_category(r['trust'])
    cat_counts[r['category']] += 1
print(f'Category spread: {dict(cat_counts)}')

brief_path = Path('scripts/hand_curation_briefs/D4_05_drugs.md')
with brief_path.open('w', encoding='utf-8') as f:
    f.write(f"""# Cluster D4_05 Drugs costs (NHS Trusts)

Scope: {len(selected)} trust drug-cost sub-lines · total £{sum(r['value'] for r in selected)/1e9:.2f}B

## Task

Each depth-4 "Drug Costs" sub-line under a specific NHS Trust needs a hand-curated Tier A entry that is TAILOR-MADE per-entity. NO generic template fallback. NO shared content.

```python
NEW = {{
    "Drug Costs \u2014 Royal Cornwall Hospitals NHS Trust": {{
        "aliases": [{{"name": "Drug Costs", "parent": "Royal Cornwall Hospitals NHS Trust"}}],
        "description": "2-3 sentences: trust-specific drug-spend context (formulary posture · high-cost drugs share · biosimilar uptake · specialty mix)",
        "beneficiaries": "Patients served by the trust's pharmacy-dispensed and ward-administered drugs",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · Health and Care Act 2022 (drug commissioning) · NICE TAs (funding mandate) · specific commissioning context",
        "key_stats": [...],  # 6-10 trust-specific stats
        "notes": "2-4 sentences: trust-specific drug-spend drivers (cancer drugs growth · high-cost devices · homecare insourcing · PbR reimbursement mix)",
        "sources": [...],  # 2-3 URLs
        "related": ["<trust name>", "Clinical Supplies & Drugs \u2014 <trust>"]
    }}
}}
```

## Rules
- Em-dash separator ` \u2014 ` (U+2014 with spaces) in composite keys
- Scoped alias parent = TRUST NAME exactly
- Every source with working URL (trust annual report · NHS Digital · NHS England · manufacturer-specific refs if relevant)
- 6-10 key_stats per entry, trust-specific
- Drug-spend narrative should reflect:
  * Oncology share (MHRA-licensed new tumour agents growing ~8-12%/yr)
  * High-cost drugs list (HCDs commissioned directly by ICB/specialised commissioning, not in trust tariff)
  * Biosimilar penetration (adalimumab · rituximab · trastuzumab switches)
  * Cancer Drugs Fund (£340M 2024-25 national · not in trust Drug Costs)
  * Homecare medicines (direct-to-patient, impacting trust bill)
- Each entry's `notes` must include specific operational context (which specialties drive spend · any recent shortage · procurement consortium)

## Output
Write your file as `scripts/D4_05_drugs_<batch>.py` where <batch> is A / B / C / D (depending which brief slice the agent handled) — with a single `NEW = {{ ... }}` direct dict literal. No `if __name__ == '__main__'` block.

## Trust-specific anchors (reference these in narratives)

Category spread of this brief:
""")
    for cat, n in cat_counts.most_common():
        f.write(f'- **{cat}**: {n} trusts\n')
    f.write('\n## Sub-lines in this cluster\n\n')
    for r in selected:
        f.write(f"""### Drug Costs \u2014 {r['trust']}
  sub-line type: Drug Costs
  parent trust: {r['trust']}
  trust category: {r['category']}
  parent line: {r['parent_line']}
  value: £{r['value']/1e6:.2f}M

""")

print(f'\nWrote {brief_path}')

# Also emit a batch split into 4 parts for parallel agents
batches = [selected[i::4] for i in range(4)]
for i, batch in enumerate(batches):
    split_path = Path(f'scripts/hand_curation_briefs/D4_05_drugs_{chr(65+i)}.json')
    split_path.write_text(json.dumps(batch, ensure_ascii=False, indent=2), encoding='utf-8')
    print(f'  split {chr(65+i)}: {len(batch)} trusts → {split_path}')
