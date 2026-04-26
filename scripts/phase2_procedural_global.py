"""Generate procedural fallback for ALL global tree orphans.

After hand-curated batches + NHS procedural fallback, ~1,001 orphans remain
across the whole tree (>£500k, depth>=2, no composite key + no scoped alias).

Most are:
- COFOG codes appearing under multiple depts (e.g. "1.1 Executive and legislative
  organs" appears 26 times across central depts)
- Category-level NHS/council aggregates not yet hand-curated
- Specific high-£ programme orphans

Generates one procedural entry per (sub-line, parent) pair. Marked
_source: 'procedural-fallback-global' for distinction from NHS-specific
fallback.
"""
import json
import re
import sys
from collections import defaultdict, Counter

sys.stdout.reconfigure(encoding='utf-8')
sys.setrecursionlimit(50000)

with open('data/uk/node_enrichment_extended.json', encoding='utf-8') as f:
    ext = json.load(f)
with open('data/uk/uk_budget_tree_2024.json', encoding='utf-8') as f:
    tree = json.load(f)
keys = set(ext['entries'].keys())

aliases_scoped = defaultdict(set)
for k, e in ext['entries'].items():
    for a in (e.get('aliases') or []):
        if isinstance(a, dict) and a.get('name') and a.get('parent'):
            aliases_scoped[(a['name'], a['parent'])].add(k)

orphans = []
def walk(n, chain=[]):
    name = n.get('name','')
    v = n.get('value') or 0
    if name and v > 5e5 and len(chain) >= 2:
        composite = f"{name} — {chain[-1]}"
        if composite not in keys:
            covered = False
            for anc in reversed(chain):
                if (name, anc) in aliases_scoped:
                    covered = True; break
            if not covered:
                orphans.append({
                    'name': name,
                    'parent': chain[-1] if chain else '',
                    'grandparent': chain[-2] if len(chain) >= 2 else '',
                    'value': v,
                    'depth': len(chain),
                })
    for c in (n.get('children') or []):
        walk(c, chain + [name])
walk(tree)

print(f'Orphans found: {len(orphans)}')

# Classify by type
COFOG_PREFIX = re.compile(r'^\d+\.\d+|^\d+\.\w$')
def classify(o):
    name = o['name']
    if COFOG_PREFIX.match(name):
        return 'cofog'
    if 'NHS' in name or 'Trust' in name or 'Hospital' in name:
        return 'nhs-aggregate'
    if any(w in o['parent'] for w in ['NHS Acute', 'NHS Mental', 'NHS Specialist', 'NHS Community', 'NHS Ambulance']):
        return 'nhs-trust-subline'
    return 'general'

by_type = Counter(classify(o) for o in orphans)
print(f'Classification: {dict(by_type)}')

# Generic source map
GENERAL_SOURCE = {'publisher': 'HM Treasury', 'title': 'Public Expenditure Statistical Analyses 2024', 'url': 'https://www.gov.uk/government/collections/public-expenditure-statistical-analyses-pesa'}
COFOG_SOURCE = {'publisher': 'ONS', 'title': 'Classification of the Functions of Government (COFOG)', 'url': 'https://www.ons.gov.uk/economy/governmentpublicsectorandtaxes/publicsectorfinance/methodologies/classificationofthefunctionsofgovernmentcofog'}
NHS_SOURCE = {'publisher': 'NHS England', 'title': 'Provider Finance — Trust Accounts Consolidation', 'url': 'https://www.england.nhs.uk/financial-accounting-and-reporting/'}

def make_entry(o):
    name = o['name']
    parent = o['parent']
    value_b = o['value'] / 1e9
    depth = o['depth']
    cat = classify(o)

    if cat == 'cofog':
        src = COFOG_SOURCE
        cofog_code = re.match(r'^(\d+\.\w+)', name).group(1) if re.match(r'^(\d+\.\w+)', name) else ''
        domain = name[len(cofog_code):].lstrip(' ').lstrip(':').strip()
        desc = (
            f'COFOG {cofog_code} ({domain}) at {parent} — auto-generated procedural fallback for £{value_b:.2f}B '
            f'category aggregate. The COFOG code groups all spending of this functional type under {parent}; '
            f'individual programmes are typically hand-curated separately. Coverage status: procedural placeholder, '
            f'full functional analysis pending.'
        )
        beneficiaries = f'Recipients of {parent} spending classified under COFOG {cofog_code}.'
        legal_basis = (
            f'UN Classification of the Functions of Government (CoFoG 1999, ESA 2010 alignment) · '
            f'HM Treasury Public Expenditure Statistical Analyses (PESA) framework · '
            f'OSCAR II reporting standards'
        )
    elif cat in ('nhs-aggregate', 'nhs-trust-subline'):
        src = NHS_SOURCE
        desc = (
            f'{name} at {parent} — auto-generated procedural fallback for £{value_b:.2f}B aggregate. '
            f'This category-level entry covers all spending of this type within {parent}. Individual provider '
            f'sub-lines are typically hand-curated; this placeholder gives the aggregate context until a full '
            f'category narrative is added.'
        )
        beneficiaries = f'Patients + staff served by {parent} provider organisations.'
        legal_basis = 'NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHSE Provider Finance reporting'
    else:
        src = GENERAL_SOURCE
        desc = (
            f'{name} at {parent} — auto-generated procedural fallback for £{value_b:.2f}B. '
            f'This entry is a minimal placeholder for a long-tail category orphan; full hand-curation '
            f'with policy context, statutory basis and recent events is pending.'
        )
        beneficiaries = f'Recipients of {name} spending under {parent}.'
        legal_basis = (
            'UK Public Finance and Accountability framework · departmental statutes · '
            'HM Treasury Consolidated Budgeting Guidance'
        )

    return {
        'aliases': [{'name': name, 'parent': parent}],
        '_source': 'procedural-fallback',
        'description': desc,
        'beneficiaries': beneficiaries,
        'legal_basis': legal_basis,
        'key_stats': [
            {'label': f'{name} 2024-25 (under {parent[:40]})', 'value': f'£{value_b:.2f}B'},
            {'label': 'Classification', 'value': cat.replace('-', ' ').title()},
            {'label': 'Tree depth', 'value': str(depth)},
            {'label': 'Parent line', 'value': parent},
            {'label': 'Coverage status', 'value': 'Procedural fallback (not hand-curated)'},
            {'label': 'Source authority', 'value': src['publisher']},
        ],
        'notes': (
            f'Procedural fallback for {name} as a sub-aggregate of {parent} (£{value_b:.2f}B, 2024-25). '
            f'Replaces previous shared-parent rendering. Hand-curation candidate when £>£10B or political salience '
            f'increases (e.g. major Spending Review category, public-interest investigation).'
        ),
        'sources': [
            src,
            GENERAL_SOURCE if src is not GENERAL_SOURCE else COFOG_SOURCE,
        ],
        'related': [parent, o.get('grandparent', '')] if o.get('grandparent') else [parent],
    }

new_entries = {}
for o in orphans:
    composite = f"{o['name']} — {o['parent']}"
    if composite in keys or composite in new_entries: continue
    new_entries[composite] = make_entry(o)

print(f'\nGenerated procedural entries: {len(new_entries)}')

added = 0
for k, e in new_entries.items():
    if k in ext['entries']: continue
    ext['entries'][k] = e
    added += 1

print(f'Merged: +{added}')
print(f'Total enrichment: {len(ext["entries"]):,}')

with open('data/uk/node_enrichment_extended.json', 'w', encoding='utf-8') as f:
    json.dump(ext, f, ensure_ascii=False, indent=2)
print('Wrote node_enrichment_extended.json')

# Save script for git
with open('scripts/phase2_procedural_global_output.py', 'w', encoding='utf-8') as f:
    f.write('# Auto-generated procedural fallback for global tree orphans (COFOG codes + NHS/council aggregates)\n')
    f.write('# Marked with _source: \'procedural-fallback\'\n\n')
    f.write('NEW = ')
    json.dump(new_entries, f, ensure_ascii=False, indent=2)
    f.write('\n')
print('Wrote scripts/phase2_procedural_global_output.py')
