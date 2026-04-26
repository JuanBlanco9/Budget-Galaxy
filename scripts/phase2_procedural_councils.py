"""Generate procedural fallback entries for UK Local Government long-tail orphans.

Same pattern as phase2_procedural_fallback.py (NHS) but applied to council categories:
- Shire Districts (~948 orphans · £3.5B)
- Unitary Authorities (~652 · £30B)
- Metropolitan Districts (~369 · £24B)
- London Boroughs (~322 · £20B)
- Shire Counties (~216 · £31B)
- Other Authorities (PCCs/FRAs/Combined Authorities · ~237)

Maps each council sub-line type to its sector authority (MHCLG, DfE for school
services, DfT for highways, DLUHC for housing, etc.) and generates trust-scoped
procedural entries with disclaimer.
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

# Council categories (taxonomy from MHCLG RO5)
TARGET_CATEGORIES = {
    'Shire Districts': 'Shire District',
    'Unitary Authorities': 'Unitary Authority',
    'Metropolitan Districts': 'Metropolitan District',
    'London Boroughs': 'London Borough',
    'Shire Counties': 'Shire County',
    'Other Authorities': 'Other Authority',  # PCCs, FRAs, Combined Authorities
}

def find_target_subtree(n, chain=[]):
    results = []
    name = n.get('name','')
    if name in TARGET_CATEGORIES:
        # Children of a TARGET_CATEGORY node ARE authorities — no filter needed
        for t in (n.get('children') or []):
            tname = t.get('name','')
            if tname:  # just skip blank
                results.append((t, chain + [name], TARGET_CATEGORIES[name]))
    for c in (n.get('children') or []):
        results.extend(find_target_subtree(c, chain + [name]))
    return results

trust_subtrees = find_target_subtree(tree)
print(f'Target authorities found: {len(trust_subtrees)}')
sample_names = [t[0].get('name','')[:60] for t in trust_subtrees[:8]]
print(f'Sample: {sample_names}')

orphans = []
def walk_node(n, auth_name, category, chain):
    name = n.get('name','')
    v = n.get('value') or 0
    if name and v > 1e5:  # >= £100k
        composite_key = f"{name} — {auth_name}"
        if composite_key not in keys and (name, auth_name) not in aliases_scoped:
            parent_line = chain[-1] if chain else ''
            orphans.append({
                'authority': auth_name,
                'category': category,
                'sub_line': name,
                'value': v,
                'parent_line': parent_line,
            })
    for c in (n.get('children') or []):
        walk_node(c, auth_name, category, chain + [name])

for trust_node, chain, category in trust_subtrees:
    aname = trust_node.get('name','')
    for child in (trust_node.get('children') or []):
        walk_node(child, aname, category, chain + [trust_node.get('name','')])

print(f'\nTotal council orphans: {len(orphans)}')
by_cat = Counter(o['category'] for o in orphans)
for cat, n in by_cat.most_common():
    cat_total = sum(o['value'] for o in orphans if o['category']==cat) / 1e9
    print(f'  {cat}: {n} orphans · £{cat_total:.2f}B')
print(f'Total £ absorbed: £{sum(o["value"] for o in orphans)/1e9:.2f}B')

# Sub-line type → authority mapping for councils
SUBLINE_AUTHORITY_LG = {
    'Education': {'publisher': 'DfE', 'title': 'Education and children\'s services statistics', 'url': 'https://explore-education-statistics.service.gov.uk/'},
    'Schools': {'publisher': 'DfE', 'title': 'School funding statistics', 'url': 'https://www.gov.uk/government/collections/statistics-school-funding'},
    'Adult Social Care': {'publisher': 'NHS Digital', 'title': 'Adult Social Care Activity & Finance Report', 'url': 'https://digital.nhs.uk/data-and-information/publications/statistical/adult-social-care-activity-and-finance-report'},
    "Children's Social Care": {'publisher': 'DfE', 'title': "Children's social care statistics", 'url': 'https://www.gov.uk/government/collections/statistics-children-in-need'},
    'Children Looked After': {'publisher': 'DfE', 'title': 'Children Looked After in England', 'url': 'https://explore-education-statistics.service.gov.uk/find-statistics/children-looked-after-in-england-including-adoptions'},
    'Public Health': {'publisher': 'OHID', 'title': 'Public Health Outcomes Framework', 'url': 'https://www.gov.uk/government/collections/public-health-outcomes-framework'},
    'Highways and Transport Services': {'publisher': 'DfT', 'title': 'Local authority road maintenance statistics', 'url': 'https://www.gov.uk/government/collections/road-network-and-traffic'},
    'Highways and Transport': {'publisher': 'DfT', 'title': 'Local authority road maintenance statistics', 'url': 'https://www.gov.uk/government/collections/road-network-and-traffic'},
    'Roads': {'publisher': 'DfT', 'title': 'Local authority road maintenance statistics', 'url': 'https://www.gov.uk/government/collections/road-network-and-traffic'},
    'Housing': {'publisher': 'MHCLG', 'title': 'Local authority housing statistics', 'url': 'https://www.gov.uk/government/collections/local-authority-housing-data'},
    'Housing (GFRA only)': {'publisher': 'MHCLG', 'title': 'Local authority housing statistics', 'url': 'https://www.gov.uk/government/collections/local-authority-housing-data'},
    'Housing Services': {'publisher': 'MHCLG', 'title': 'Local authority housing statistics', 'url': 'https://www.gov.uk/government/collections/local-authority-housing-data'},
    'Cultural and Related Services': {'publisher': 'DCMS', 'title': 'Cultural sector statistics', 'url': 'https://www.gov.uk/government/collections/dcms-statistics'},
    'Cultural & Related Services': {'publisher': 'DCMS', 'title': 'Cultural sector statistics', 'url': 'https://www.gov.uk/government/collections/dcms-statistics'},
    'Environmental and Regulatory Services': {'publisher': 'DEFRA', 'title': 'Local authority environmental data', 'url': 'https://www.gov.uk/government/collections/local-authority-collected-waste-management-statistics'},
    'Environmental & Regulatory Services': {'publisher': 'DEFRA', 'title': 'Local authority environmental data', 'url': 'https://www.gov.uk/government/collections/local-authority-collected-waste-management-statistics'},
    'Planning and Development Services': {'publisher': 'MHCLG', 'title': 'Planning applications statistics', 'url': 'https://www.gov.uk/government/collections/planning-applications-statistics'},
    'Police Services': {'publisher': 'Home Office', 'title': 'Police funding settlement', 'url': 'https://www.gov.uk/government/publications/police-grant-report-england-and-wales'},
    'Fire & Rescue Services': {'publisher': 'Home Office', 'title': 'Fire and rescue authority spending', 'url': 'https://www.gov.uk/government/collections/fire-statistics'},
    'Central Services': {'publisher': 'MHCLG', 'title': 'Local authority revenue expenditure', 'url': 'https://www.gov.uk/government/collections/local-authority-revenue-expenditure-and-financing'},
    'Other Services': {'publisher': 'MHCLG', 'title': 'Local authority revenue expenditure', 'url': 'https://www.gov.uk/government/collections/local-authority-revenue-expenditure-and-financing'},
    'Capital Financing': {'publisher': 'MHCLG', 'title': 'Local authority capital expenditure & receipts', 'url': 'https://www.gov.uk/government/collections/local-authority-capital-expenditure-receipts-and-financing'},
}

DEFAULT_AUTH = {'publisher': 'MHCLG', 'title': 'Local authority revenue expenditure & financing', 'url': 'https://www.gov.uk/government/collections/local-authority-revenue-expenditure-and-financing'}

def auth_slug(name):
    """Best-effort slug for council website."""
    s = name.lower()
    s = re.sub(r"\s+(council|borough|metropolitan|authority|of)(?:\s+|$)", ' ', s)
    s = re.sub(r"['’]", '', s)
    s = re.sub(r'[^a-z0-9 ]', '', s).strip()
    s = s.replace(' ', '')
    return s

def make_entry(o):
    auth = o['authority']
    sub_line = o['sub_line']
    value_m = o['value'] / 1e6
    parent_line = o['parent_line']
    category = o['category']

    slug = auth_slug(auth)
    auth_url = f'https://www.{slug}.gov.uk/' if slug else 'https://www.gov.uk/find-local-council'
    src_auth = SUBLINE_AUTHORITY_LG.get(sub_line, DEFAULT_AUTH)

    return {
        'aliases': [{'name': sub_line, 'parent': auth}],
        '_source': 'procedural-fallback',
        'description': (
            f'{sub_line} sub-line at {auth} — auto-generated procedural fallback for £{value_m:.2f}M long-tail orphan. '
            f'This entry is a minimal authority-scoped placeholder; full hand-curation with council-specific drivers, '
            f'political control context, S114 risk and recent service-pressure events is pending. '
            f'Refer to the authority\'s 2024-25 Statement of Accounts for line-item detail.'
        ),
        'beneficiaries': f'Residents + service users of {auth} ({category}).',
        'legal_basis': (
            'Local Government Act 1972 · Local Government Finance Act 1988 · Local Government Act 2000 · '
            f'Local Authorities (Capital Finance and Accounting) Regulations 2003 · sub-line specifics: see {src_auth["publisher"]} reference'
        ),
        'key_stats': [
            {'label': f'{sub_line} 2024-25', 'value': f'£{value_m:.2f}M'},
            {'label': 'Authority category', 'value': category},
            {'label': 'Parent line', 'value': parent_line},
            {'label': 'Coverage status', 'value': 'Procedural fallback (not hand-curated)'},
            {'label': 'Hand-curation priority', 'value': 'low (long-tail by £)'},
            {'label': 'Source authority', 'value': src_auth['publisher']},
        ],
        'notes': (
            f'Procedural fallback for the long-tail orphan {sub_line} at {auth}. '
            f'The authority reports £{value_m:.2f}M for this sub-line in 2024-25 — modest enough that detailed '
            f'hand-curation has lower marginal information value than headline lines (Adult Social Care, Children\'s Social Care, '
            f'Education, Highways). For a tailored authority-specific narrative (political control, S114 risk, recent '
            f'service-pressure events), request hand-curation in a future Phase 2 batch. Until then this entry replaces '
            f'the previous shared-parent fallback that rendered identical content across every authority\'s {sub_line} line.'
        ),
        'sources': [
            {'publisher': auth, 'title': '2024-25 Statement of Accounts (or most recent)', 'url': auth_url},
            src_auth,
        ],
        'related': [auth, parent_line],
    }

new_entries = {}
for o in orphans:
    composite = f"{o['sub_line']} — {o['authority']}"
    if composite in keys or composite in new_entries: continue
    new_entries[composite] = make_entry(o)

print(f'\nGenerated procedural entries: {len(new_entries)}')

with open('scripts/phase2_procedural_councils.py.new', 'w', encoding='utf-8') as f:
    f.write('# Auto-generated procedural fallback entries for UK council long-tail orphans\n')
    f.write('# Marked with _source: \'procedural-fallback\' to distinguish from hand-curated entries\n\n')
    f.write('NEW = ')
    json.dump(new_entries, f, ensure_ascii=False, indent=2)
    f.write('\n')
print('Wrote scripts/phase2_procedural_councils.py.new (output dict)')

# Apply via direct merge
added = 0
for k, e in new_entries.items():
    if k in ext['entries']: continue
    ext['entries'][k] = e
    added += 1

print(f'\nMerged: +{added} council procedural entries')
print(f'Total enrichment: {len(ext["entries"]):,}')

with open('data/uk/node_enrichment_extended.json', 'w', encoding='utf-8') as f:
    json.dump(ext, f, ensure_ascii=False, indent=2)
print('Wrote node_enrichment_extended.json')
