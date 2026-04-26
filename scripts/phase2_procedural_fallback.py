"""Generate procedural fallback entries for NHS Acute + MH long-tail orphans.

Detects every shared-parent orphan still uncovered after waves 1-4, generates a
trust-specific minimal entry with:
- Composite key + scoped alias
- Trust name + sub-line + £ + parent line in description
- 6 minimal key_stats
- Sources: trust AR landing page + 1 sub-line-type authority
- _source: 'procedural-fallback' flag for frontend distinction
- Honest disclaimer: "approximation pending hand-curation"

The frontend can later render these differently (e.g. PROCEDURAL badge vs
ENRICHED) so users know when they're seeing auto-generated vs hand-curated.

Solves the visual regression where Cold Weather Payment / Community Care Grant /
Net Lending all rendered IDENTICAL parent COFOG content. Now each gets its own
trust-specific entry, even if minimal.
"""
import json
import re
import sys
import os
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

TARGET_CATEGORIES = {
    'NHS Acute Trusts': 'Acute',
    'NHS Mental Health Trusts': 'Mental Health',
    'NHS Specialist Trusts': 'Specialist',
    'NHS Community Trusts': 'Community',
    'NHS Ambulance Trusts': 'Ambulance',
}

def find_target_subtree(n, chain=[]):
    results = []
    name = n.get('name','')
    if name in TARGET_CATEGORIES:
        for t in (n.get('children') or []):
            tname = t.get('name','')
            if 'Trust' in tname or 'Health Board' in tname:
                results.append((t, chain + [name], TARGET_CATEGORIES[name]))
    for c in (n.get('children') or []):
        results.extend(find_target_subtree(c, chain + [name]))
    return results

trust_subtrees = find_target_subtree(tree)

orphans = []
def walk_node(n, trust_name, category, chain):
    name = n.get('name','')
    v = n.get('value') or 0
    if name and v > 1e5:
        composite_key = f"{name} — {trust_name}"
        if composite_key not in keys and (name, trust_name) not in aliases_scoped:
            # Orphan — needs entry (don't return; still recurse into children below)
            parent_line = chain[-1] if chain else ''
            orphans.append({
                'trust': trust_name,
                'category': category,
                'sub_line': name,
                'value': v,
                'parent_line': parent_line,
            })
    for c in (n.get('children') or []):
        walk_node(c, trust_name, category, chain + [name])

for trust_node, chain, category in trust_subtrees:
    tname = trust_node.get('name','')
    for child in (trust_node.get('children') or []):
        walk_node(child, tname, category, chain + [trust_node.get('name','')])

print(f'Total NHS orphans still uncovered: {len(orphans)}')
by_cat = Counter(o['category'] for o in orphans)
print(f'By category: {dict(by_cat)}')
total_gbp = sum(o['value'] for o in orphans)
print(f'Total £ absorbed: £{total_gbp/1e9:.2f}B')

# ---- Generate procedural entries ----
def trust_slug(t):
    """Convert trust name into a likely .nhs.uk subdomain root."""
    s = t.lower()
    s = re.sub(r'\s+(nhs|foundation|trust|partnership|healthcare|health|nhsft)(?:\s+|$)', ' ', s)
    s = re.sub(r"['’]", '', s)
    s = re.sub(r'[^a-z0-9 ]', '', s).strip()
    s = s.replace(' ', '')
    return s

# Map sub-line type -> central authority source
SUBLINE_AUTHORITY = {
    'Premises (other)': {'publisher': 'NHS England', 'title': 'NHS Estates Returns Information Collection (ERIC)', 'url': 'https://www.england.nhs.uk/statistics/statistical-work-areas/estates-returns-information-collection/'},
    'Establishment costs': {'publisher': 'NHS England', 'title': 'Provider Finance — Cost & Productivity', 'url': 'https://www.england.nhs.uk/financial-accounting-and-reporting/'},
    'Clinical supplies & services': {'publisher': 'NHS Supply Chain', 'title': 'Medical Category', 'url': 'https://www.supplychain.nhs.uk/categories/medical/'},
    'Drugs costs': {'publisher': 'NHS Business Services Authority', 'title': 'e-PACT2 Hospital Prescribing', 'url': 'https://www.nhsbsa.nhs.uk/pharmacies-gp-practices-and-appliance-contractors/dispensing-contractors-information/epact2'},
    'Transport (business + patient)': {'publisher': 'NHS England', 'title': 'NHS Patient Transport Services Eligibility Criteria', 'url': 'https://www.england.nhs.uk/non-emergency-patient-transport-services/'},
    'General supplies & services': {'publisher': 'NHS Supply Chain', 'title': 'Food, Facilities & Domestic (FFD) Category', 'url': 'https://www.supplychain.nhs.uk/categories/'},
    'Business rates': {'publisher': 'GOV.UK', 'title': 'Business rates revaluation (Valuation Office Agency)', 'url': 'https://www.gov.uk/government/organisations/valuation-office-agency'},
    'Amortisation': {'publisher': 'HM Treasury', 'title': 'Government Financial Reporting Manual (FReM)', 'url': 'https://www.gov.uk/government/collections/government-financial-reporting-manual-frem'},
    'Impairments net of reversals': {'publisher': 'HM Treasury', 'title': 'IAS 36 Impairment of Assets — DHSC GAM', 'url': 'https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025'},
    'Lease expenditure': {'publisher': 'HM Treasury', 'title': 'IFRS 16 Leases application guidance', 'url': 'https://www.gov.uk/government/publications/ifrs-16-leases-application-guidance'},
    'Social security & levy': {'publisher': 'HMRC', 'title': 'Employer National Insurance contributions 2024-25', 'url': 'https://www.gov.uk/national-insurance-rates-letters'},
    'PFI / LIFT charges': {'publisher': 'HM Treasury', 'title': 'PFI / PF2 — current projects database', 'url': 'https://www.gov.uk/government/publications/private-finance-initiative-and-private-finance-2-projects-2023-summary-data'},
    'Inventories written down': {'publisher': 'HM Treasury', 'title': 'NHS Group Accounting Manual 2024-25 — Inventories (IAS 2)', 'url': 'https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025'},
    'Termination & post-employment': {'publisher': 'HM Treasury', 'title': 'NHS Pension Scheme + Public Sector Exit Payments', 'url': 'https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025'},
    'Other & adjustments': {'publisher': 'HM Treasury', 'title': 'NHS Group Accounting Manual 2024-25', 'url': 'https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025'},
    'Other': {'publisher': 'HM Treasury', 'title': 'NHS Group Accounting Manual 2024-25', 'url': 'https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025'},
}

def make_entry(o):
    trust = o['trust']
    sub_line = o['sub_line']
    value_m = o['value'] / 1e6
    parent_line = o['parent_line']
    category = o['category']

    # Trust AR url — best-effort (some trusts don't have predictable subdomains; fall back to NHS England)
    slug = trust_slug(trust)
    trust_ar_url = f'https://www.{slug}.nhs.uk/about-us/publications/' if slug else 'https://www.england.nhs.uk/financial-accounting-and-reporting/'
    auth = SUBLINE_AUTHORITY.get(sub_line, SUBLINE_AUTHORITY['Other'])

    return {
        'aliases': [{'name': sub_line, 'parent': trust}],
        '_source': 'procedural-fallback',
        'description': (
            f'{sub_line} sub-line at {trust} — auto-generated procedural fallback for £{value_m:.2f}M long-tail orphan. '
            f'This entry is a minimal trust-scoped placeholder; full hand-curation with trust-specific drivers, peer benchmarks and CQC/recent-event context is pending. '
            f'Refer to the trust’s 2024-25 annual report for line-item detail.'
        ),
        'beneficiaries': f'Service users + staff at {trust} — NHS {category} Trust within the wider NHS Provider Sector.',
        'legal_basis': (
            'NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 '
            f'· sub-line specifics: see {auth["publisher"]} reference'
        ),
        'key_stats': [
            {'label': f'{sub_line} 2024-25', 'value': f'£{value_m:.2f}M'},
            {'label': 'Trust category', 'value': f'NHS {category} Trust'},
            {'label': 'Parent line', 'value': parent_line},
            {'label': 'Coverage status', 'value': 'Procedural fallback (not hand-curated)'},
            {'label': 'Hand-curation priority', 'value': 'low (long-tail by £)'},
            {'label': 'Source authority', 'value': auth['publisher']},
        ],
        'notes': (
            f'Procedural fallback for the long-tail orphan {sub_line} at {trust}. '
            f'The trust reports £{value_m:.2f}M for this sub-line in 2024-25 — modest enough that detailed hand-curation '
            f'has lower marginal information value than headline lines (Staff Costs, Drug Costs, Premises baseline). '
            f'For a tailored trust-specific narrative, request hand-curation in a future Phase 2 batch. '
            f'Until then this entry replaces the previous shared-parent fallback that rendered identical content across '
            f'every trust’s {sub_line} line.'
        ),
        'sources': [
            {'publisher': trust, 'title': '2024-25 Annual Report and Accounts (or most recent published)', 'url': trust_ar_url},
            auth,
        ],
        'related': [trust, parent_line],
    }

new_entries = {}
skipped_dups = 0
for o in orphans:
    composite = f"{o['sub_line']} — {o['trust']}"
    if composite in keys or composite in new_entries:
        skipped_dups += 1
        continue
    new_entries[composite] = make_entry(o)

print(f'\nGenerated procedural entries: {len(new_entries)}')
print(f'Skipped (already in enrichment): {skipped_dups}')

# Save as Python dict literal for the merge pipeline
out_path = 'scripts/phase2_procedural_nhs.py'
with open(out_path, 'w', encoding='utf-8') as f:
    f.write('# Auto-generated procedural fallback entries for NHS Acute + MH + Specialist + Community + Ambulance long-tail orphans\n')
    f.write('# Marked with _source: \'procedural-fallback\' to distinguish from hand-curated entries\n\n')
    f.write('NEW = ')
    json.dump(new_entries, f, ensure_ascii=False, indent=2)
    f.write('\n')

print(f'Wrote {out_path}')

# Apply via direct merge (skip duplicates)
added = 0
for k, e in new_entries.items():
    if k in ext['entries']: continue
    ext['entries'][k] = e
    added += 1

print(f'\nMerged: +{added} procedural entries')
print(f'Total enrichment: {len(ext["entries"]):,}')

with open('data/uk/node_enrichment_extended.json', 'w', encoding='utf-8') as f:
    json.dump(ext, f, ensure_ascii=False, indent=2)
print('Wrote node_enrichment_extended.json')
