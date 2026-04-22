# Cluster Phase2_MH_slice1 — NHS Mental Health Trust orphan sub-lines

Scope: 200 orphan depth-5 sub-lines under NHS Mental Health Trusts (top-£ slice of 485 total orphans · £2.83B absorbed).

## Context — the shared-parent gap

Per Budget Galaxy mandate: **every entity-level node at every depth must have its own tailor-made entry**. Today, these 200 sub-lines resolve to a generic parent (Staff Costs / Premises / COFOG 7.A Medical services) because they don't have trust-scoped aliases. Example visible regression:

- `Premises (other)` under Tavistock & Portman, Camden+Islington-pre-merger, and Oxleas all render IDENTICAL content (inherited from the generic "Premises (other)" parent or the MH Trust category page).

Each of these 200 needs a TRUST-SPECIFIC entry — per-site, per-drug formulary, per-PFI contract, per-estate footprint.

## Sub-line types in this slice (ranked by £)

- **Premises (other)** — 45 trusts · £0.67B · includes leases, business rates on MH estates, facilities contracts, void-space decommissioning
- **Establishment costs** — 45 trusts · £0.22B · office costs, training, legal, printing
- **Clinical supplies & services** — 45 trusts · £0.27B · restraint equipment, ward diagnostics, PPE
- **Transport (business + patient)** — 45 trusts · £0.14B · patient transfer, section 136 transport, community team travel
- **General supplies & services** — 44 trusts · £0.27B · hotel services, catering (insourced), PPE
- **Business rates** — 45 trusts · £0.06B · uniform business rates on clinical estate
- **Amortisation** — 44 trusts · £0.04B · intangible asset depreciation (software, capitalised training)
- **Impairments net of reversals** — 37 trusts · £0.41B · asset revaluation losses (notable on RAAC-affected estates)
- **Social security & levy** — 33 trusts · £0.62B · employer NI contributions at 13.8% + apprenticeship levy 0.5%
- **Lease expenditure** — 35 trusts · £0.04B · operating leases post-IFRS 16
- **PFI / LIFT charges** — 26 trusts · £0.08B · unitary charges on PFI schemes (varied by trust)

## Task — per entry

Every orphan gets a TAILOR-MADE entry that reflects:

1. **The specific MH trust's geography + estate footprint** (which buildings, when acquired, PFI or not)
2. **The sub-line's MH-specific driver** (e.g. Premises: section 136 suites + PICU + ECT rooms + specialty forensic units)
3. **Industrial action 2023-24 impact** on this specific sub-line (for MH: less oncology/less acute, more ADP backfill + 1:1 observation agency)
4. **Peer benchmark vs MH-trust median**, NOT acute-trust benchmark — MH estate footprint per bed is different
5. **Recent-year context** (RAAC survey outcomes 2024, BCUHB Report Apr 2025, Edenfield Centre BBC Panorama 2022-24 aftermath, NMIP reforms, 2023 Mental Health Bill stalled)

## Schema

```python
"<sub-line> — <MH trust>": {
    "aliases": [{"name": "<sub-line>", "parent": "<MH trust>"}],
    "description": "2-3 sentences: what this sub-line represents for THIS trust (estate type, PFI status, specialty mix)",
    "beneficiaries": "Service users receiving mental health care at trust sites (inpatient/community/CAMHS/forensic — be specific)",
    "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Mental Health Act 1983 (s.140/s.136) · Health and Care Act 2022 · specific statutes (e.g. Section 136 for PICU, Section 117 for aftercare)",
    "key_stats": [
        {"label": "<sub-line> 2024-25", "value": "£<exact from slice JSON>M"},
        {"label": "Share of trust total opex", "value": "c. X%"},
        {"label": "Beds/sites anchor", "value": "e.g. 'c. 350 beds across 4 sites'"},
        {"label": "Specific driver", "value": "e.g. 'PFI unitary charge at Highgate Centre ~£4M/yr + backfill'"},
        {"label": "YoY change", "value": "c. +X% (driver)"},
        {"label": "Peer benchmark (MH trust)", "value": "e.g. 'above/below MH-trust median £/bed-day'"},
        {"label": "Workforce interaction", "value": "e.g. '1:1 observation agency £Ym'"},
        {"label": "Recent context", "value": "e.g. 'RAAC survey 2024: N sites affected'"}
    ],  # 6-10 trust-specific
    "notes": "2-4 sentences: MH-trust-specific drivers. Reference specific events: BCUHB Apr 2025 spec-measures, Edenfield BBC Panorama, Mental Health Bill 2023 implications, trust forensic/learning-disability specialty if relevant",
    "sources": [
        {"publisher": "<trust>", "title": "Annual Report 2024-25 or 2023-24", "url": "https://<trust-domain>/..."},
        {"publisher": "CQC", "title": "Inspection report <trust>", "url": "https://www.cqc.org.uk/..."}
    ],  # 2-3 with https:// URLs
    "related": ["<trust>", "<sub-line parent>"]  # e.g. "Premises — <trust>"
}
```

## MH-trust specific anchors (weave into narratives as relevant)

- **Forensic specialty trusts** (Broadmoor-housing West London, Rampton-housing Notts, Ashworth-housing Mersey Care): higher secure unit costs, lifetime sentences, restraint equipment
- **Learning disability specialists** (Tees Esk & Wear, parts of Sussex Partnership): bespoke ward design, specialist staff ratios
- **CAMHS heavy** (South London & Maudsley, North West Boroughs): MH Crisis Teams, 4-week waiting target pressure
- **PFI-heavy**: Oxleas (Oxleas House PFI), Tees Esk & Wear (Roseberry Park PFI), East London FT (Forest + Tower Hamlets PFI)
- **RAAC estate risks 2024-25** affecting wards at certain trusts — flag where known
- **Pre-merger vs post-merger**: Camden & Islington + BEH → NLMHP (1 Oct 2024); Birmingham & Solihull + Forward Thinking; Lincolnshire Partnership integration
- **Industrial action drag**: medical staff action had LESS direct impact on MH than on acutes, but agency nurse / HCA backfill costs were higher

## Rules (same as D4_05 / D4_06)
- Em-dash ` — ` (U+2014 with spaces)
- Scoped alias parent = EXACT trust name from slice JSON
- Every source URL `https://`
- 6-10 key_stats per entry, trust-specific
- 2-4 sentence notes, trust-specific (NO generic NHS-wide boilerplate)

## Output

Three batches A/B/C:
- `scripts/hand_curation_briefs/phase2_mh_slice1_A.json` (67 entries)
- `scripts/hand_curation_briefs/phase2_mh_slice1_B.json` (67 entries)
- `scripts/hand_curation_briefs/phase2_mh_slice1_C.json` (66 entries)

Each agent writes `scripts/phase2_mh_slice1_<A|B|C>.py` with `NEW = {...}` direct dict literal. No `__main__`, imports, or file mutation.
