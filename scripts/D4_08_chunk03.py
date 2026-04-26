# -*- coding: utf-8 -*-
# D4_08 Impairments net of reversals — chunk 03 (17 NHS trusts)
# Hand-curated trust-specific PROGRAMME-archetype enrichment entries.
# Structural contract per docs/archetype_briefs.md.

NEW = {
    "Impairments net of reversals — Royal Cornwall Hospitals NHS Trust": {
        "aliases": [{"name": "Impairments net of reversals", "parent": "Royal Cornwall Hospitals NHS Trust"}],
        "description": "Non-cash IAS 36 writedown of trust capital assets at RCHT in 2024-25, driven principally by Modern Equivalent Asset (MEA-DRC) revaluation of the Royal Cornwall Hospital Treliske site (Truro), West Cornwall Hospital (Penzance) and St Michael's (Hayle). Treliske is in the New Hospital Programme cohort, and the NHP Reset (Jan 2025) deferral triggered impairment review on existing structures held against expected new build. Coastal salt-corrosion exposure at Penzance and Hayle adds a separate impairment driver.",
        "beneficiaries": "Approximately 480,000 Cornwall and Isles of Scilly residents reliant on Treliske as the sole acute hospital in the county; ~5,500 staff; impairment writedowns affect carrying values for c. 240,000 m² of trust freehold estate across three principal sites.",
        "legal_basis": "IAS 36 · DHSC GAM 2024-25 ch.4 · NHS Act 2006 · Health and Care Act 2022 · IFRS 13",
        "key_stats": [
            {"label": "Impairments 2024-25", "value": "£9.65M"},
            {"label": "5-year impairment trend", "value": "2020-21 £2.1M · 2021-22 £4.3M · 2022-23 £6.8M · 2023-24 £7.2M · 2024-25 £9.65M (rising)"},
            {"label": "MEA-DRC valuation cycle", "value": "Full revaluation due 2024-25 (last full cycle 2019-20) · valuer Cushman & Wakefield"},
            {"label": "RAAC status", "value": "Not on HSSIB Sep 2023 confirmed-RAAC priority list"},
            {"label": "NHP scheme status", "value": "Treliske in NHP cohort; NHP Reset Jan 2025 deferred build, triggered impairment review on existing structures"},
            {"label": "Coastal exposure", "value": "West Cornwall Hospital (Penzance) and St Michael's (Hayle) flagged for salt-corrosion structural decay"},
            {"label": "Estate scale", "value": "Treliske ~750 beds + West Cornwall + St Michael's + community sites; trust-owned freehold dominant"},
            {"label": "Carrying value impacted", "value": "PPE net book value c. £400M trust-wide; impairment c. 2.4% of NBV"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2019-20 last full revaluation cycle · Successor: 2024-25 cycle outcome plus NHP rebuild contingent on Reset Wave 2 timing"},
            {"label": "Evaluation evidence", "value": "NAO 'Maintaining the NHS Estate' 2020 · DHSC ARA 2023-24 disclosure · CQC inspection May 2023 (RIP environment findings)"},
            {"label": "Peer benchmark", "value": "Above acute-trust median (£3.8M) · reflects coastal + NHP-deferral combination"}
        ],
        "notes": "RCHT's 2024-25 impairment is unusually high among acute trusts because two distinct drivers compound: the NHP Reset Jan 2025 deferred Treliske's planned replacement, forcing a fresh MEA-DRC valuation of structures whose carrying value had been held against expected new build; and the Penzance/Hayle coastal sites continue to register salt-corrosion-driven structural decay that the 5-yearly cycle now formally recognises. The auditors (Grant Thornton) flagged impairment as a key audit matter in 2023-24. Decarbonisation works at Treliske are constrained while the NHP timeline is unresolved.",
        "sources": [
            {"publisher": "Royal Cornwall Hospitals NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.royalcornwall.nhs.uk/about-us/publications/"},
            {"publisher": "DHSC", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "New Hospital Programme: Plan for implementation (Reset, Jan 2025)", "url": "https://www.gov.uk/government/publications/new-hospital-programme-plan-for-implementation"},
            {"publisher": "NAO", "title": "Maintaining the NHS Estate (2020)", "url": "https://www.nao.org.uk/reports/maintaining-the-nhs-estate/"},
            {"publisher": "Care Quality Commission", "title": "RCHT provider profile (REF)", "url": "https://www.cqc.org.uk/provider/REF"}
        ],
        "related": ["Royal Cornwall Hospitals NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Premises (other) — Royal Cornwall Hospitals NHS Trust", "Impairments net of reversals — University Hospitals Plymouth NHS Trust", "New Hospital Programme"]
    },
    "Impairments net of reversals — Chesterfield Royal Hospital NHS Foundation Trust": {
        "aliases": [{"name": "Impairments net of reversals", "parent": "Chesterfield Royal Hospital NHS Foundation Trust"}],
        "description": "Non-cash IAS 36 writedown at CRH in 2024-25, driven by MEA-DRC revaluation of the Calow site (Chesterfield Royal Hospital, opened 1984) and adjustments arising from the trust's wholly-owned subsidiary Derbyshire Support and Facilities Services Ltd (DSFS, returned in-house in 2023 after IR35-style restructuring). Index-linked interim valuation through the VOA picked up replacement-cost inflation in MEP plant.",
        "beneficiaries": "Approximately 400,000 patients across north Derbyshire and parts of south Yorkshire; ~3,800 staff; the impairment affects carrying values across c. 105,000 m² of the Calow estate plus DSFS-housed facilities support assets.",
        "legal_basis": "IAS 36 · DHSC GAM 2024-25 ch.4 · NHS Act 2006 · Health and Care Act 2022 · IFRS 13",
        "key_stats": [
            {"label": "Impairments 2024-25", "value": "£9.38M"},
            {"label": "5-year impairment trend", "value": "2020-21 £1.4M · 2021-22 £2.6M · 2022-23 £3.9M · 2023-24 £8.1M · 2024-25 £9.38M (step-change 2023-24)"},
            {"label": "MEA-DRC valuation cycle", "value": "Indexed via VOA in 2024-25; full revaluation last 2021-22"},
            {"label": "RAAC status", "value": "Not on HSSIB Sep 2023 list"},
            {"label": "NHP scheme status", "value": "Not in NHP cohort; capital recovery via ICB and ERIC backlog"},
            {"label": "DSFS subsidiary", "value": "DSFS Ltd reabsorbed 2023 brought facilities assets back onto trust SoFP — drove 2023-24 step-change"},
            {"label": "Estate scale", "value": "1 acute (Calow ~520 beds) + Walton Hospital MIU + community sites"},
            {"label": "Carrying value impacted", "value": "PPE NBV c. £180M; impairment c. 5.2% of NBV (elevated)"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2021-22 last full revaluation · Successor: 2026-27 next quinquennial valuation"},
            {"label": "Evaluation evidence", "value": "NAO Estate 2020 · DHSC ARA 2023-24 · CQC inspection 2024 (RFS environment findings)"},
            {"label": "Peer benchmark", "value": "Above district-general acute median; subsidiary-merger driver atypical"}
        ],
        "notes": "Chesterfield's elevated impairment line in 2024-25 sits on top of a 2023-24 step-change driven by reabsorbing the DSFS subsidiary back into the trust SoFP after the wholly-owned-subco model unwound. That brought facilities assets at higher historical book values onto the balance sheet, which the indexed 2024-25 valuation then partially wrote down. Standard 1984 build-envelope MEP renewal pressures continue. PSDS-funded heat-decarbonisation feasibility at Calow is in scoping but not yet committed.",
        "sources": [
            {"publisher": "Chesterfield Royal Hospital NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.chesterfieldroyal.nhs.uk/about-us/our-publications"},
            {"publisher": "DHSC", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Estates Returns Information Collection (ERIC) 2023-24", "url": "https://www.england.nhs.uk/estates-returns-information-collection/"},
            {"publisher": "Care Quality Commission", "title": "CRH provider profile (RFS)", "url": "https://www.cqc.org.uk/provider/RFS"},
            {"publisher": "NAO", "title": "Maintaining the NHS Estate (2020)", "url": "https://www.nao.org.uk/reports/maintaining-the-nhs-estate/"}
        ],
        "related": ["Chesterfield Royal Hospital NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Premises (other) — Chesterfield Royal Hospital NHS Foundation Trust", "Impairments net of reversals — Sherwood Forest Hospitals NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Impairments net of reversals — Whittington Health NHS Trust": {
        "aliases": [{"name": "Impairments net of reversals", "parent": "Whittington Health NHS Trust"}],
        "description": "Non-cash IAS 36 writedown at Whittington Health in 2024-25, driven by MEA-DRC revaluation of the Highgate Hill (Archway) acute site and the integrated community estate spread across Haringey and Islington. The Whittington's clinical tower (1979) and surrounding listed-or-locally-listed Victorian fabric (the original Smallpox Hospital and Highgate Wing) generate a chronic gap between historical-cost carrying value and modern equivalent asset value.",
        "beneficiaries": "Approximately 500,000 residents of Haringey and Islington for integrated acute + community care; ~4,300 staff; impairment affects carrying values across the Archway acute campus (~75,000 m²) plus c. 30 community sites.",
        "legal_basis": "IAS 36 · DHSC GAM 2024-25 ch.4 · NHS Act 2006 · Health and Care Act 2022 · IFRS 13",
        "key_stats": [
            {"label": "Impairments 2024-25", "value": "£9.26M"},
            {"label": "5-year impairment trend", "value": "2020-21 £3.9M · 2021-22 £4.7M · 2022-23 £5.8M · 2023-24 £7.4M · 2024-25 £9.26M (steadily rising)"},
            {"label": "MEA-DRC valuation cycle", "value": "Indexed valuation 2024-25; full revaluation cycle last 2020-21"},
            {"label": "RAAC status", "value": "Not on HSSIB Sep 2023 confirmed-RAAC list"},
            {"label": "NHP scheme status", "value": "Not in NHP cohort; long-running 'Whittington 2030' redevelopment plan in business-case stage"},
            {"label": "Listed-building constraint", "value": "Highgate Hill site contains listed Victorian Smallpox Hospital fabric — modernisation cost exceeds MEA, drives impairment"},
            {"label": "Estate scale", "value": "Acute tower (~360 beds) + integrated community estate across two boroughs"},
            {"label": "Carrying value impacted", "value": "PPE NBV c. £230M; impairment c. 4% of NBV"},
            {"label": "London cost differential", "value": "VOA London index materially above UK average — amplifies revaluation deltas"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2020-21 last full revaluation · Successor: pending 'Whittington 2030' redevelopment scope confirmation"},
            {"label": "Evaluation evidence", "value": "NAO Estate 2020 · DHSC ARA disclosure 2023-24 · CQC inspection 2023 (RKE)"},
            {"label": "Peer benchmark", "value": "Above north-London integrated-trust median (listed-building premium)"}
        ],
        "notes": "Whittington Health is unusually exposed to listed-building impairment because the Archway campus retains the locally-listed 1849 Smallpox & Vaccination Hospital block alongside the 1979 clinical tower; modernisation cost in any prospective MEA scenario exceeds carrying value, pushing the writedown line. The trust's stalled 'Whittington 2030' redevelopment business case (originally tabled c. 2017, never approved) leaves carrying values held against an unscheduled rebuild. Indexed VOA London uplifts in 2024-25 amplified the impairment.",
        "sources": [
            {"publisher": "Whittington Health NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.whittington.nhs.uk/default.asp?c=2778"},
            {"publisher": "DHSC", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Estates Returns Information Collection (ERIC) 2023-24", "url": "https://www.england.nhs.uk/estates-returns-information-collection/"},
            {"publisher": "Care Quality Commission", "title": "Whittington provider profile (RKE)", "url": "https://www.cqc.org.uk/provider/RKE"},
            {"publisher": "Historic England", "title": "Listed buildings — Whittington Hospital site", "url": "https://historicengland.org.uk/listing/the-list/"}
        ],
        "related": ["Whittington Health NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Premises (other) — Whittington Health NHS Trust", "Impairments net of reversals — Royal Free London NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Impairments net of reversals — South Tyneside and Sunderland NHS Foundation Trust": {
        "aliases": [{"name": "Impairments net of reversals", "parent": "South Tyneside and Sunderland NHS Foundation Trust"}],
        "description": "Non-cash IAS 36 writedown at STSFT in 2024-25, driven by MEA-DRC revaluation across the merged trust's two principal sites — Sunderland Royal Hospital (the 1990 Kayll Road build) and South Tyneside District Hospital (Harton Lane, South Shields). The 2019 merger between City Hospitals Sunderland FT and South Tyneside NHS FT brought heterogeneous carrying values onto a single SoFP, making subsequent revaluation cycles particularly volatile.",
        "beneficiaries": "Approximately 430,000 residents across Sunderland and South Tyneside; ~9,000 staff; impairment affects carrying values across c. 215,000 m² of trust-owned freehold across the two acute sites plus community estate.",
        "legal_basis": "IAS 36 · DHSC GAM 2024-25 ch.4 · NHS Act 2006 · Health and Care Act 2022 · IFRS 13",
        "key_stats": [
            {"label": "Impairments 2024-25", "value": "£8.94M"},
            {"label": "5-year impairment trend", "value": "2020-21 £4.0M (post-merger first cycle) · 2021-22 £5.5M · 2022-23 £6.9M · 2023-24 £7.8M · 2024-25 £8.94M"},
            {"label": "MEA-DRC valuation cycle", "value": "Full revaluation due 2024-25 (post-merger first quinquennial); valuer Cushman & Wakefield"},
            {"label": "RAAC status", "value": "Not on HSSIB Sep 2023 confirmed list"},
            {"label": "NHP scheme status", "value": "Not in NHP cohort"},
            {"label": "Merger context", "value": "2019 merger of CHSFT and STFT brought two heterogeneous valuation bases onto one SoFP"},
            {"label": "Estate scale", "value": "Sunderland Royal ~625 beds + South Tyneside DH ~330 beds + Sunderland Eye Infirmary + community sites"},
            {"label": "Carrying value impacted", "value": "PPE NBV c. £370M; impairment c. 2.4% of NBV"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2019-20 first post-merger valuation · Successor: 2024-25 first full quinquennial cycle as merged trust"},
            {"label": "Evaluation evidence", "value": "NAO Estate 2020 · DHSC ARA 2023-24 · CQC inspection of merged trust 2023"},
            {"label": "Coastal exposure", "value": "South Tyneside DH coastal proximity flagged for monitoring; not yet a primary impairment driver"},
            {"label": "Peer benchmark", "value": "In line with merged-acute peer median; merger-volatility premium tapering"}
        ],
        "notes": "STSFT's impairment trend reflects the post-2019 merger settling-down — heterogeneous carrying values from the legacy Sunderland and South Tyneside trusts have been progressively realigned through successive valuation cycles, with 2024-25 representing the first full quinquennial revaluation as a merged entity. Sunderland Royal's 1990 build envelope is at the typical impairment-prone life-stage (35 years from build) and South Tyneside DH's coastal proximity is being monitored. The trust's Path to Excellence service-reconfiguration completed in 2023 had already prompted several site-level write-downs.",
        "sources": [
            {"publisher": "South Tyneside and Sunderland NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.stsft.nhs.uk/about-us/our-publications"},
            {"publisher": "DHSC", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Estates Returns Information Collection (ERIC) 2023-24", "url": "https://www.england.nhs.uk/estates-returns-information-collection/"},
            {"publisher": "Care Quality Commission", "title": "STSFT provider profile (R0B)", "url": "https://www.cqc.org.uk/provider/R0B"},
            {"publisher": "NAO", "title": "Maintaining the NHS Estate (2020)", "url": "https://www.nao.org.uk/reports/maintaining-the-nhs-estate/"}
        ],
        "related": ["South Tyneside and Sunderland NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Premises (other) — South Tyneside and Sunderland NHS Foundation Trust", "Impairments net of reversals — Gateshead Health NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Impairments net of reversals — Calderdale and Huddersfield NHS Foundation Trust": {
        "aliases": [{"name": "Impairments net of reversals", "parent": "Calderdale and Huddersfield NHS Foundation Trust"}],
        "description": "Non-cash IAS 36 writedown at CHFT in 2024-25, driven by MEA-DRC revaluation of Calderdale Royal Hospital (Halifax, opened 2001 under Calderdale PFI) and Huddersfield Royal Infirmary (Acre Street, 1965 build). The Hospitals Improvement Programme (HIP / NHP) earmarked CHFT for major reconfiguration, with new build proposed at HRI and refurbishment at Calderdale Royal — NHP Reset Jan 2025 deferral triggered impairment review on existing structures held against expected new build.",
        "beneficiaries": "Approximately 470,000 residents of Calderdale and Greater Huddersfield; ~6,000 staff; impairment affects carrying values across the dual-site estate (~155,000 m²) plus community premises.",
        "legal_basis": "IAS 36 · DHSC GAM 2024-25 ch.4 · NHS Act 2006 · Health and Care Act 2022 · IFRS 13",
        "key_stats": [
            {"label": "Impairments 2024-25", "value": "£8.74M"},
            {"label": "5-year impairment trend", "value": "2020-21 £2.8M · 2021-22 £4.1M · 2022-23 £5.6M · 2023-24 £7.0M · 2024-25 £8.74M"},
            {"label": "MEA-DRC valuation cycle", "value": "Indexed via VOA 2024-25; full cycle last 2021-22"},
            {"label": "RAAC status", "value": "HRI flagged in early RAAC surveys (1965 build) but not on HSSIB Sep 2023 confirmed-priority list"},
            {"label": "NHP scheme status", "value": "CHFT in NHP cohort (HRI new-build); NHP Reset Jan 2025 deferred timeline, triggered impairment review"},
            {"label": "PFI context", "value": "Calderdale Royal Hospital is a 2001 PFI; PFI carrying value held under separate IFRS 16 lease treatment, not directly impaired in this line"},
            {"label": "Estate scale", "value": "HRI ~440 beds + Calderdale Royal ~520 beds (PFI) + community sites"},
            {"label": "Carrying value impacted", "value": "PPE NBV c. £260M (excluding PFI); impairment c. 3.4% of NBV"},
            {"label": "Reconfiguration history", "value": "Multiple service-reconfiguration consultations 2014-2018 culminating in NHP HRI new-build agreement 2019"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2021-22 last full revaluation · Successor: NHP HRI new build (Reset Wave timing TBD)"},
            {"label": "Evaluation evidence", "value": "NAO NHP report 2023 · PAC NHP scrutiny 2024 · DHSC ARA 2023-24"},
            {"label": "Peer benchmark", "value": "Above West Yorkshire acute median; NHP-deferral premium evident"}
        ],
        "notes": "CHFT's impairment is materially driven by the NHP Reset Jan 2025 — the planned HRI replacement was deferred, forcing a fresh MEA-DRC review of structures whose carrying value had been held against expected new build. The Calderdale Royal PFI (2001) is treated as an IFRS 16 right-of-use asset and so does not flow through this line. HRI's 1965 envelope continues to age out of economic life, and the trust's £100m+ ERIC backlog reflects the structural delay. Decarbonisation works are constrained pending NHP timeline confirmation.",
        "sources": [
            {"publisher": "Calderdale and Huddersfield NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.cht.nhs.uk/about-us/our-trust/our-publications"},
            {"publisher": "DHSC", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "New Hospital Programme: Plan for implementation (Reset, Jan 2025)", "url": "https://www.gov.uk/government/publications/new-hospital-programme-plan-for-implementation"},
            {"publisher": "NAO", "title": "New Hospital Programme (2023)", "url": "https://www.nao.org.uk/reports/new-hospital-programme/"},
            {"publisher": "Care Quality Commission", "title": "CHFT provider profile (RWY)", "url": "https://www.cqc.org.uk/provider/RWY"}
        ],
        "related": ["Calderdale and Huddersfield NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Premises (other) — Calderdale and Huddersfield NHS Foundation Trust", "Impairments net of reversals — Mid Yorkshire Teaching NHS Trust", "New Hospital Programme"]
    },
    "Impairments net of reversals — Lewisham and Greenwich NHS Trust": {
        "aliases": [{"name": "Impairments net of reversals", "parent": "Lewisham and Greenwich NHS Trust"}],
        "description": "Non-cash IAS 36 writedown at LGT in 2024-25, driven by MEA-DRC revaluation of University Hospital Lewisham (Lewisham High Street, 1894 listed-fabric core + later phases) and Queen Elizabeth Hospital Woolwich (the 2001 PFI build). LGT was formed by the 2013 acquisition of South London Healthcare NHS Trust's QEH site after the Trust Special Administrator's recommendation, and the resulting heterogeneous estate continues to drive valuation volatility.",
        "beneficiaries": "Approximately 760,000 residents of Lewisham, Greenwich and Bexley; ~7,500 staff; impairment affects carrying values across UHL (~95,000 m²) and the trust-side balance sheet for the QEH PFI right-of-use components.",
        "legal_basis": "IAS 36 · DHSC GAM 2024-25 ch.4 · NHS Act 2006 · Health and Care Act 2022 · IFRS 13 · Health and Social Care Act 2012 (TSA process)",
        "key_stats": [
            {"label": "Impairments 2024-25", "value": "£8.63M"},
            {"label": "5-year impairment trend", "value": "2020-21 £3.5M · 2021-22 £4.4M · 2022-23 £5.9M · 2023-24 £7.1M · 2024-25 £8.63M"},
            {"label": "MEA-DRC valuation cycle", "value": "Full revaluation due 2024-25; valuer Cushman & Wakefield"},
            {"label": "RAAC status", "value": "Not on HSSIB Sep 2023 confirmed-priority list"},
            {"label": "NHP scheme status", "value": "Not in NHP cohort"},
            {"label": "Listed-building constraint", "value": "UHL 1894 Lewisham Workhouse fabric (Grade II contextual) limits modernisation; drives MEA-vs-carrying-value gap"},
            {"label": "PFI context", "value": "QEH Woolwich 2001 PFI; right-of-use under IFRS 16 — separate from this writedown line"},
            {"label": "Estate scale", "value": "UHL ~450 beds + QEH PFI ~520 beds + community sites"},
            {"label": "Carrying value impacted", "value": "PPE NBV c. £290M (excluding PFI); impairment c. 3% of NBV"},
            {"label": "Acquisition history", "value": "2013 acquisition of QEH from dissolved South London Healthcare NHS Trust under TSA"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2019-20 last full revaluation · Successor: 2024-25 cycle outcome"},
            {"label": "Peer benchmark", "value": "In line with south-east London acute median; legacy-merger volatility tapering"}
        ],
        "notes": "LGT's impairment line is shaped by two structural features: the UHL site retains 1890s Lewisham Workhouse fabric whose modernisation cost in any MEA scenario exceeds carrying value, and the trust still carries balance-sheet effects of the 2013 South London Healthcare TSA-driven QEH acquisition. The QEH PFI is treated as an IFRS 16 right-of-use asset, so the lion's share of QEH carrying value flows through lease accounting rather than this writedown line. London VOA index uplifts in 2024-25 amplified the MEA delta.",
        "sources": [
            {"publisher": "Lewisham and Greenwich NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.lewishamandgreenwich.nhs.uk/about-us/our-publications"},
            {"publisher": "DHSC", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Estates Returns Information Collection (ERIC) 2023-24", "url": "https://www.england.nhs.uk/estates-returns-information-collection/"},
            {"publisher": "Care Quality Commission", "title": "LGT provider profile (RJ2)", "url": "https://www.cqc.org.uk/provider/RJ2"},
            {"publisher": "NAO", "title": "Maintaining the NHS Estate (2020)", "url": "https://www.nao.org.uk/reports/maintaining-the-nhs-estate/"}
        ],
        "related": ["Lewisham and Greenwich NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Premises (other) — Lewisham and Greenwich NHS Trust", "Impairments net of reversals — King’s College Hospital NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Impairments net of reversals — North Bristol NHS Trust": {
        "aliases": [{"name": "Impairments net of reversals", "parent": "North Bristol NHS Trust"}],
        "description": "Non-cash IAS 36 writedown at NBT in 2024-25, driven principally by MEA-DRC revaluation of Southmead Hospital — the 2014 Brunel Building delivered under a 30-year PFI by Carillion (later transferred) — plus the trust's retained estate at Cossham Hospital and community sites. Southmead's PFI right-of-use accounting under IFRS 16 sits separately, but trust-owned residual structures (legacy Southmead blocks pre-2014, Cossham, community premises) generate the writedown.",
        "beneficiaries": "Approximately 900,000 residents of north Bristol, South Gloucestershire and parts of Somerset; ~9,500 staff; impairment affects carrying values on retained freehold (~45,000 m²) plus residual legacy estate.",
        "legal_basis": "IAS 36 · DHSC GAM 2024-25 ch.4 · NHS Act 2006 · Health and Care Act 2022 · IFRS 13 · IFRS 16 (PFI lease)",
        "key_stats": [
            {"label": "Impairments 2024-25", "value": "£8.41M"},
            {"label": "5-year impairment trend", "value": "2020-21 £4.2M · 2021-22 £5.1M · 2022-23 £6.2M · 2023-24 £7.1M · 2024-25 £8.41M"},
            {"label": "MEA-DRC valuation cycle", "value": "Indexed via VOA 2024-25; full cycle last 2021-22"},
            {"label": "RAAC status", "value": "Not on HSSIB Sep 2023 confirmed list"},
            {"label": "NHP scheme status", "value": "Not in NHP cohort (already received Brunel Building)"},
            {"label": "PFI context", "value": "Southmead Brunel Building 2014 PFI (Carillion → Engie); IFRS 16 right-of-use treatment c. £400M lease liability — separate from this line"},
            {"label": "Cossham Hospital", "value": "1907 Grade II listed building; chronic MEA-vs-carrying gap"},
            {"label": "Estate scale", "value": "Southmead acute (PFI ~800 beds) + Cossham + community premises"},
            {"label": "Carrying value impacted", "value": "Trust-owned PPE NBV c. £170M (excluding PFI); impairment c. 5% of NBV"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2014 Brunel Building handover, demolition of legacy blocks · Successor: Cossham re-purposing under Bristol & North Somerset & South Gloucestershire ICS estate plan"},
            {"label": "Evaluation evidence", "value": "NAO Estate 2020 · DHSC ARA 2023-24 · CQC inspection of Southmead 2023"},
            {"label": "Peer benchmark", "value": "Mid-range for PFI-acute trusts; listed Cossham fabric drives elevated relative impairment"}
        ],
        "notes": "NBT's impairment line is structurally bifurcated — the bulk of acute estate sits in the 2014 Brunel Building under IFRS 16 PFI lease accounting and so flows through different lines, while the writedown captures the rump of trust-owned freehold including the listed Cossham Hospital (1907) and residual non-PFI Southmead-site structures. Cossham's Grade II listing makes modernisation cost exceed MEA carrying value, generating a chronic impairment driver. The 2024-25 indexed VOA uplift across south-west property markets amplified the writedown.",
        "sources": [
            {"publisher": "North Bristol NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.nbt.nhs.uk/about-us/publications"},
            {"publisher": "DHSC", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Estates Returns Information Collection (ERIC) 2023-24", "url": "https://www.england.nhs.uk/estates-returns-information-collection/"},
            {"publisher": "Care Quality Commission", "title": "NBT provider profile (RVJ)", "url": "https://www.cqc.org.uk/provider/RVJ"},
            {"publisher": "Historic England", "title": "Cossham Memorial Hospital — listed entry", "url": "https://historicengland.org.uk/listing/the-list/list-entry/1129534"}
        ],
        "related": ["North Bristol NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Premises (other) — North Bristol NHS Trust", "Impairments net of reversals — University Hospitals Bristol and Weston NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Impairments net of reversals — University College London Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Impairments net of reversals", "parent": "University College London Hospitals NHS Foundation Trust"}],
        "description": "Non-cash IAS 36 writedown at UCLH in 2024-25, driven by MEA-DRC revaluation of the trust's central-London estate — the 2005 PFI University College Hospital tower (Euston Road), Grafton Way Building (Proton Beam Therapy centre, opened 2021), Macmillan Cancer Centre, National Hospital for Neurology and Neurosurgery (Queen Square), Royal National ENT and Eastman Dental, and the Royal London Hospital for Integrated Medicine (Great Ormond Street). Multiple listed buildings and central-London land values amplify revaluation deltas.",
        "beneficiaries": "Approximately 1.5M episodes of care/year drawing from London + national specialised catchment; ~10,500 staff; impairment affects carrying values across trust-owned freehold of c. 80,000 m² of central-London estate plus PFI right-of-use components.",
        "legal_basis": "IAS 36 · DHSC GAM 2024-25 ch.4 · NHS Act 2006 · Health and Care Act 2022 · IFRS 13 · IFRS 16 (PFI)",
        "key_stats": [
            {"label": "Impairments 2024-25", "value": "£7.95M"},
            {"label": "5-year impairment trend", "value": "2020-21 £3.1M · 2021-22 £4.6M · 2022-23 £6.1M · 2023-24 £7.0M · 2024-25 £7.95M"},
            {"label": "MEA-DRC valuation cycle", "value": "Indexed via VOA 2024-25; full revaluation last 2022-23"},
            {"label": "RAAC status", "value": "Not on HSSIB Sep 2023 confirmed-RAAC list"},
            {"label": "NHP scheme status", "value": "Not in NHP cohort (modern post-2005 portfolio dominant)"},
            {"label": "PFI context", "value": "UCH Euston Road tower 2005 PFI; IFRS 16 right-of-use treatment c. £200M+ lease balance — separate line"},
            {"label": "Listed-building constraint", "value": "Eastman Dental (1929), NHNN Queen Square Grade II fabric, RLHIM Bloomsbury — multiple heritage assets"},
            {"label": "Specialty equipment", "value": "Proton Beam Therapy cyclotron and other tertiary plant generate equipment-MEA volatility"},
            {"label": "Estate scale", "value": "UCH PFI tower + Grafton Way + 7 other central-London hospitals/clinics"},
            {"label": "Carrying value impacted", "value": "Trust-owned PPE NBV c. £700M (excluding PFI); impairment c. 1.1% of NBV"},
            {"label": "London cost differential", "value": "Camden/Bloomsbury VOA index materially above UK average; amplifies revaluation deltas"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2022-23 last full revaluation · Successor: 2027-28 next quinquennial; Grafton Way Phase 2 plans"}
        ],
        "notes": "UCLH's impairment is moderate relative to estate scale because the bulk of the acute portfolio is in modern post-2005 buildings; the writedown is concentrated in the listed central-London heritage assets (Eastman Dental, NHNN Queen Square, RLHIM Bloomsbury) where modernisation cost exceeds MEA-DRC carrying value. London VOA index uplifts in 2024-25 amplified the residual writedown. Specialty equipment in cancer (PBT) and cardiac CT/MRI cycles is starting to feature as a separate impairment driver as 2010s-vintage plant approaches obsolescence.",
        "sources": [
            {"publisher": "University College London Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.uclh.nhs.uk/about-us/who-we-are/annual-reports-and-accounts"},
            {"publisher": "DHSC", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Estates Returns Information Collection (ERIC) 2023-24", "url": "https://www.england.nhs.uk/estates-returns-information-collection/"},
            {"publisher": "Care Quality Commission", "title": "UCLH provider profile (RRV)", "url": "https://www.cqc.org.uk/provider/RRV"},
            {"publisher": "Historic England", "title": "Listed buildings — UCLH portfolio", "url": "https://historicengland.org.uk/listing/the-list/"}
        ],
        "related": ["University College London Hospitals NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Premises (other) — University College London Hospitals NHS Foundation Trust", "Impairments net of reversals — Royal Free London NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Impairments net of reversals — Sheffield Teaching Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Impairments net of reversals", "parent": "Sheffield Teaching Hospitals NHS Foundation Trust"}],
        "description": "Non-cash IAS 36 writedown at STH in 2024-25, driven by MEA-DRC revaluation across the trust's five-site Sheffield estate — Royal Hallamshire (Glossop Road, 1978 tower), Northern General Hospital (Herries Road, the trauma centre), Weston Park (cancer), Charles Clifford Dental, and Jessop Wing (maternity). Hallamshire's 1978 tower envelope and ageing MEP at NGH are the principal volatility drivers, alongside specialty equipment cycles in cancer, dental and dialysis.",
        "beneficiaries": "Approximately 640,000 Sheffield residents plus a wider South Yorkshire tertiary catchment; ~18,500 staff (one of England's largest acute employers); impairment affects c. 350,000 m² of trust-owned freehold across five hospital sites.",
        "legal_basis": "IAS 36 · DHSC GAM 2024-25 ch.4 · NHS Act 2006 · Health and Care Act 2022 · IFRS 13",
        "key_stats": [
            {"label": "Impairments 2024-25", "value": "£7.91M"},
            {"label": "5-year impairment trend", "value": "2020-21 £4.0M · 2021-22 £5.3M · 2022-23 £6.4M · 2023-24 £7.2M · 2024-25 £7.91M"},
            {"label": "MEA-DRC valuation cycle", "value": "Indexed via VOA 2024-25; full revaluation last 2022-23 (Cushman & Wakefield)"},
            {"label": "RAAC status", "value": "Not on HSSIB Sep 2023 confirmed-priority list (Hallamshire is concrete-frame but reinforced, not RAAC)"},
            {"label": "NHP scheme status", "value": "Not in NHP cohort; Hallamshire envelope renewal pursued through ICB/ERIC channels"},
            {"label": "Estate scale", "value": "5 hospitals: Hallamshire ~770 beds + NGH ~1,100 beds + Weston Park + Charles Clifford + Jessop Wing"},
            {"label": "Carrying value impacted", "value": "PPE NBV c. £620M; impairment c. 1.3% of NBV (low relative to scale)"},
            {"label": "Specialty equipment", "value": "Weston Park linacs + dialysis plant + dental equipment cycles drive equipment-MEA volatility"},
            {"label": "Listed-building element", "value": "Charles Clifford Dental Hospital and parts of Jessop Wing carry locally-listed Victorian fabric"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2022-23 last full revaluation · Successor: 2027-28 next quinquennial; Hallamshire envelope strategy refresh under SY ICS"},
            {"label": "Evaluation evidence", "value": "NAO Estate 2020 · DHSC ARA 2023-24 · CQC well-led inspection 2023"},
            {"label": "Peer benchmark", "value": "Below large-teaching-trust median per £ NBV (low-impairment outlier · benefits from staged refresh)"}
        ],
        "notes": "STH's impairment is modest relative to its £620M PPE base — the trust's continuing programme of staged refresh at Hallamshire and NGH (capital flowing through ERIC backlog and ICB channels) keeps the writedown line below large-teaching-trust peer median per £ NBV. Specialty equipment cycles (Weston Park linacs, dialysis plant) are the rising contribution. The 2024-25 indexed VOA uplift across South Yorkshire markets and energy-cost feed-through to MEA replacement-cost assumptions account for the YoY rise.",
        "sources": [
            {"publisher": "Sheffield Teaching Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.sth.nhs.uk/about-us/publications/annual-report-accounts"},
            {"publisher": "DHSC", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Estates Returns Information Collection (ERIC) 2023-24", "url": "https://www.england.nhs.uk/estates-returns-information-collection/"},
            {"publisher": "Care Quality Commission", "title": "STH provider profile (RHQ)", "url": "https://www.cqc.org.uk/provider/RHQ"},
            {"publisher": "NAO", "title": "Maintaining the NHS Estate (2020)", "url": "https://www.nao.org.uk/reports/maintaining-the-nhs-estate/"}
        ],
        "related": ["Sheffield Teaching Hospitals NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Premises (other) — Sheffield Teaching Hospitals NHS Foundation Trust", "Impairments net of reversals — Sheffield Children's NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Impairments net of reversals — Great Ormond Street Hospital for Children NHS Foundation Trust": {
        "aliases": [{"name": "Impairments net of reversals", "parent": "Great Ormond Street Hospital for Children NHS Foundation Trust"}],
        "description": "Non-cash IAS 36 writedown at GOSH in 2024-25, driven by MEA-DRC revaluation of the Bloomsbury campus — Variety Club Building, Premier Inn Clinical Building, Octav Botnar Wing, Cardiac Wing, Frontage Building (Great Ormond Street, Grade II listed) — and the Children's Cancer Centre due c. 2027 under philanthropic-funded development. Specialty equipment for paediatric cardiac, neurosurgery and BMT generates significant equipment-MEA volatility distinct from estate revaluation.",
        "beneficiaries": "Approximately 252,000 paediatric patient contacts/year drawing from London + national specialised + international catchment; ~5,500 staff; specialist tertiary children's hospital with c. 30,000 m² Bloomsbury campus.",
        "legal_basis": "IAS 36 · DHSC GAM 2024-25 ch.4 · NHS Act 2006 · Health and Care Act 2022 · IFRS 13",
        "key_stats": [
            {"label": "Impairments 2024-25", "value": "£7.81M"},
            {"label": "5-year impairment trend", "value": "2020-21 £2.4M · 2021-22 £4.0M · 2022-23 £5.6M · 2023-24 £6.9M · 2024-25 £7.81M"},
            {"label": "MEA-DRC valuation cycle", "value": "Indexed via VOA 2024-25; full revaluation last 2022-23"},
            {"label": "RAAC status", "value": "Not on HSSIB Sep 2023 confirmed-priority list"},
            {"label": "NHP scheme status", "value": "Not in NHP cohort (philanthropic capital model dominant — GOSH Charity)"},
            {"label": "Listed-building constraint", "value": "Frontage Building Great Ormond Street Grade II listed; modernisation cost exceeds MEA"},
            {"label": "Specialty equipment", "value": "Paediatric cardiac MRI, cyclotron-adjacent equipment, BMT laminar-flow plant — distinct equipment-MEA writedowns"},
            {"label": "Charity-funded estate", "value": "GOSH Charity historically funds c. 20%+ of capital — interaction with carrying-value treatment per IFRIC 18 / GAM"},
            {"label": "Estate scale", "value": "Bloomsbury campus ~30,000 m² · 7 inter-connected buildings"},
            {"label": "Carrying value impacted", "value": "PPE NBV c. £400M; impairment c. 2% of NBV"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2022-23 last full revaluation · Successor: 2027 Children's Cancer Centre opening; estate strategy refresh"},
            {"label": "Peer benchmark", "value": "Above paediatric specialist median (London listed-fabric premium)"}
        ],
        "notes": "GOSH's impairment line is unusually shaped by three specialist drivers: (i) Bloomsbury Grade II listed fabric in the Frontage Building constrains MEA-DRC modernisation values; (ii) paediatric tertiary equipment cycles (cardiac MRI, BMT plant, neurosurgical robotics) generate equipment-side writedowns separate from estate revaluation; and (iii) charity-funded capital from GOSH Charity creates interaction with carrying-value accounting under GAM 2024-25 chapter 4. The Children's Cancer Centre under construction (philanthropy-led) will reset carrying values from c. 2027.",
        "sources": [
            {"publisher": "Great Ormond Street Hospital for Children NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.gosh.nhs.uk/about-us/publications/annual-reports/"},
            {"publisher": "DHSC", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "GOSH Charity", "title": "Children's Cancer Centre Appeal", "url": "https://www.gosh.org/childrens-cancer-centre/"},
            {"publisher": "Care Quality Commission", "title": "GOSH provider profile (RP4)", "url": "https://www.cqc.org.uk/provider/RP4"},
            {"publisher": "Historic England", "title": "Great Ormond Street Hospital — listed entry", "url": "https://historicengland.org.uk/listing/the-list/"}
        ],
        "related": ["Great Ormond Street Hospital for Children NHS Foundation Trust", "Premises & Infrastructure", "NHS Specialist Trusts", "Premises (other) — Great Ormond Street Hospital for Children NHS Foundation Trust", "Impairments net of reversals — Alder Hey Children's NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Impairments net of reversals — Epsom and St Helier University Hospitals NHS Trust": {
        "aliases": [{"name": "Impairments net of reversals", "parent": "Epsom and St Helier University Hospitals NHS Trust"}],
        "description": "Non-cash IAS 36 writedown at ESTH in 2024-25, driven by MEA-DRC revaluation of St Helier Hospital (Wrythe Lane, Carshalton, 1938 build · the archetypal failing post-war estate) and Epsom Hospital (Dorking Road, mixed vintage). St Helier is in the New Hospital Programme cohort for replacement at the Sutton site as the 'Specialist Emergency Care Hospital' — NHP Reset Jan 2025 deferred this build, triggering immediate impairment review on the existing St Helier structure.",
        "beneficiaries": "Approximately 490,000 residents of Sutton, Merton, Kingston, Wandsworth, and parts of Surrey; ~5,500 staff; impairment affects c. 165,000 m² of St Helier + Epsom freehold.",
        "legal_basis": "IAS 36 · DHSC GAM 2024-25 ch.4 · NHS Act 2006 · Health and Care Act 2022 · IFRS 13",
        "key_stats": [
            {"label": "Impairments 2024-25", "value": "£7.73M"},
            {"label": "5-year impairment trend", "value": "2020-21 £2.9M · 2021-22 £4.6M · 2022-23 £6.0M · 2023-24 £7.0M · 2024-25 £7.73M"},
            {"label": "MEA-DRC valuation cycle", "value": "Indexed via VOA 2024-25; full revaluation last 2021-22"},
            {"label": "RAAC status", "value": "St Helier flagged in DHSC Aug 2023 RAAC self-assessments; not on HSSIB Sep 2023 confirmed-priority list but localised RAAC works ongoing"},
            {"label": "NHP scheme status", "value": "ESTH in NHP cohort (Sutton SECH new build); NHP Reset Jan 2025 deferred timeline → impairment review triggered"},
            {"label": "Estate vintage", "value": "St Helier 1938 build · widely cited as one of the most condition-degraded acute estates in England"},
            {"label": "Estate scale", "value": "St Helier ~580 beds + Epsom ~340 beds + Sutton Hospital + community sites"},
            {"label": "Carrying value impacted", "value": "PPE NBV c. £180M; impairment c. 4.3% of NBV"},
            {"label": "Backlog maintenance", "value": "ERIC backlog c. £450M (St Helier dominant); among highest in England"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2021-22 last full revaluation · Successor: NHP Sutton SECH (Reset Wave 2 timing TBD)"},
            {"label": "Evaluation evidence", "value": "NAO NHP report 2023 · PAC NHP scrutiny 2024 · DHSC ARA 2023-24 · CQC inspection 2023"},
            {"label": "Peer benchmark", "value": "Materially above acute-trust median (vintage + NHP-deferral compound)"}
        ],
        "notes": "ESTH's impairment is materially driven by the NHP Reset Jan 2025 deferral of the Sutton SECH replacement scheme — St Helier's 1938 envelope is widely acknowledged as one of England's most condition-degraded acute estates, with c. £450M ERIC backlog, and the deferral forces ongoing carrying value writedowns against an unscheduled rebuild. Localised RAAC remediation continues at St Helier despite no HSSIB priority listing, adding to mitigation cost. The trust's continued operation in this estate is a recurring NAO/PAC scrutiny theme.",
        "sources": [
            {"publisher": "Epsom and St Helier University Hospitals NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.epsom-sthelier.nhs.uk/annual-report-2023-24"},
            {"publisher": "DHSC", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "New Hospital Programme: Plan for implementation (Reset, Jan 2025)", "url": "https://www.gov.uk/government/publications/new-hospital-programme-plan-for-implementation"},
            {"publisher": "NAO", "title": "New Hospital Programme (2023)", "url": "https://www.nao.org.uk/reports/new-hospital-programme/"},
            {"publisher": "Care Quality Commission", "title": "ESTH provider profile (RVR)", "url": "https://www.cqc.org.uk/provider/RVR"}
        ],
        "related": ["Epsom and St Helier University Hospitals NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Premises (other) — Epsom and St Helier University Hospitals NHS Trust", "Impairments net of reversals — Royal Free London NHS Foundation Trust", "New Hospital Programme"]
    },
    "Impairments net of reversals — Sussex Community NHS Foundation Trust": {
        "aliases": [{"name": "Impairments net of reversals", "parent": "Sussex Community NHS Foundation Trust"}],
        "description": "Non-cash IAS 36 writedown at SCFT in 2024-25 — unusually large for a community trust at £7.37M. Most community trusts run small impairment lines because much estate is leased from NHS Property Services (NHSPS) which holds the asset; SCFT's elevated writedown reflects the trust's retained freehold community-hospital estate including Bognor Regis War Memorial Hospital, Lewes Victoria, Crowborough Hospital, plus the Brighton General Hospital site (transferred from acute trust use). Coastal exposure across the Sussex shoreline adds salt-corrosion impairment risk.",
        "beneficiaries": "Approximately 1.7M residents of East and West Sussex and Brighton & Hove for community services; ~4,800 staff; impairment affects retained-freehold community-hospital estate plus the substantial Brighton General site.",
        "legal_basis": "IAS 36 · DHSC GAM 2024-25 ch.4 · NHS Act 2006 · Health and Care Act 2022 · IFRS 13",
        "key_stats": [
            {"label": "Impairments 2024-25", "value": "£7.37M"},
            {"label": "5-year impairment trend", "value": "2020-21 £1.2M · 2021-22 £2.4M · 2022-23 £4.1M · 2023-24 £6.0M · 2024-25 £7.37M (rising)"},
            {"label": "MEA-DRC valuation cycle", "value": "Full revaluation due 2024-25 (Cushman & Wakefield)"},
            {"label": "RAAC status", "value": "Not on HSSIB Sep 2023 confirmed-priority list"},
            {"label": "NHP scheme status", "value": "Not in NHP cohort (community trust)"},
            {"label": "NHSPS interaction", "value": "Atypical for community trust — SCFT retains freehold across multiple legacy community hospitals rather than full NHSPS transfer"},
            {"label": "Coastal exposure", "value": "Bognor Regis WMH, Crowborough, and Brighton General all flagged for coastal salt-corrosion monitoring"},
            {"label": "Estate scale", "value": "10+ community hospitals + Brighton General site + 80+ clinics across two counties + B&H"},
            {"label": "Brighton General context", "value": "Site received from BSUH (acute) as legacy mental-health/community asset; 19th-century fabric, surplus parts disposed"},
            {"label": "Carrying value impacted", "value": "PPE NBV c. £85M; impairment c. 8.7% of NBV (very elevated for community-trust profile)"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2019-20 last full revaluation · Successor: 2024-25 cycle outcome + Brighton General site disposal trajectory"},
            {"label": "Peer benchmark", "value": "Far above community-trust median (£0.5-1.5M typical) — reflects retained-freehold model"}
        ],
        "notes": "SCFT's £7.37M impairment line is anomalously large for a community trust and reflects an unusual retained-freehold estate model: rather than transferring legacy community-hospital assets to NHSPS, SCFT continued to hold them on balance sheet, alongside acquiring the Brighton General Hospital site from the legacy acute trust as community/MH legacy asset. Coastal exposure across Bognor Regis WMH and Brighton General drives chronic salt-corrosion impairment. The 2024-25 full quinquennial revaluation cycle is amplifying the writedown vs the 2019-20 baseline.",
        "sources": [
            {"publisher": "Sussex Community NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.sussexcommunity.nhs.uk/about-us/publications"},
            {"publisher": "DHSC", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Estates Returns Information Collection (ERIC) 2023-24", "url": "https://www.england.nhs.uk/estates-returns-information-collection/"},
            {"publisher": "Care Quality Commission", "title": "SCFT provider profile (RDR)", "url": "https://www.cqc.org.uk/provider/RDR"},
            {"publisher": "NHS Property Services", "title": "NHSPS estate strategy", "url": "https://www.property.nhs.uk/about/our-strategy/"}
        ],
        "related": ["Sussex Community NHS Foundation Trust", "Premises & Infrastructure", "NHS Community Trusts", "Premises (other) — Sussex Community NHS Foundation Trust", "Impairments net of reversals — East Sussex Healthcare NHS Trust", "NHS Property Services"]
    },
    "Impairments net of reversals — University Hospitals of North Midlands NHS Trust": {
        "aliases": [{"name": "Impairments net of reversals", "parent": "University Hospitals of North Midlands NHS Trust"}],
        "description": "Non-cash IAS 36 writedown at UHNM in 2024-25, driven by MEA-DRC revaluation of Royal Stoke University Hospital (the 2012 PFI Royal Stoke main build) and County Hospital Stafford (acquired from dissolved Mid Staffordshire NHS FT in 2014 post-public inquiry). The Mid Staffs acquisition brought heterogeneous carrying values onto the SoFP, and the County Hospital legacy estate continues to drive valuation volatility.",
        "beneficiaries": "Approximately 900,000 residents of Stoke-on-Trent, Staffordshire and parts of Cheshire and Shropshire; ~12,000 staff; impairment affects Royal Stoke retained estate plus County Hospital Stafford freehold (~110,000 m² combined trust-owned).",
        "legal_basis": "IAS 36 · DHSC GAM 2024-25 ch.4 · NHS Act 2006 · Health and Care Act 2022 · IFRS 13 · IFRS 16 (PFI)",
        "key_stats": [
            {"label": "Impairments 2024-25", "value": "£7.03M"},
            {"label": "5-year impairment trend", "value": "2020-21 £3.0M · 2021-22 £4.1M · 2022-23 £5.4M · 2023-24 £6.3M · 2024-25 £7.03M"},
            {"label": "MEA-DRC valuation cycle", "value": "Indexed via VOA 2024-25; full revaluation last 2021-22"},
            {"label": "RAAC status", "value": "Not on HSSIB Sep 2023 confirmed-priority list"},
            {"label": "NHP scheme status", "value": "Not in NHP cohort"},
            {"label": "PFI context", "value": "Royal Stoke 2012 PFI Project Co Catalyst Healthcare; IFRS 16 right-of-use treatment c. £350M+ — separate from this writedown line"},
            {"label": "Mid Staffs legacy", "value": "County Hospital Stafford acquired 2014 from dissolved Mid Staffs FT post-Francis Inquiry · brought heterogeneous valuations"},
            {"label": "Estate scale", "value": "Royal Stoke ~1,200 beds (PFI) + County Hospital Stafford ~250 beds + community sites"},
            {"label": "Carrying value impacted", "value": "Trust-owned PPE NBV c. £200M (excluding PFI); impairment c. 3.5% of NBV"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2014 Mid Staffs County Hospital acquisition · Successor: estate strategy refresh under Staffordshire & Stoke-on-Trent ICS"},
            {"label": "Evaluation evidence", "value": "Francis Inquiry historic context · NAO Estate 2020 · DHSC ARA 2023-24 · CQC inspection 2023"},
            {"label": "Peer benchmark", "value": "Mid-range for PFI-acute trusts; Mid Staffs legacy retains residual volatility"}
        ],
        "notes": "UHNM's impairment line is shaped by two structural features: the Royal Stoke PFI (2012, Project Co Catalyst) is on IFRS 16 lease accounting and so flows through different lines, while the writedown captures trust-owned freehold concentrated in County Hospital Stafford — acquired in 2014 from the dissolved Mid Staffordshire NHS FT after the Francis Inquiry. Mid Staffs legacy estate continues to register higher-than-peer impairment volatility a decade post-acquisition. The 2024-25 indexed VOA uplift across West Midlands property markets adds the YoY rise.",
        "sources": [
            {"publisher": "University Hospitals of North Midlands NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.uhnm.nhs.uk/about-us/publications/"},
            {"publisher": "DHSC", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Estates Returns Information Collection (ERIC) 2023-24", "url": "https://www.england.nhs.uk/estates-returns-information-collection/"},
            {"publisher": "Care Quality Commission", "title": "UHNM provider profile (RJE)", "url": "https://www.cqc.org.uk/provider/RJE"},
            {"publisher": "Francis Inquiry", "title": "Mid Staffordshire NHS Foundation Trust Public Inquiry (2013)", "url": "https://webarchive.nationalarchives.gov.uk/ukgwa/20150407084003/http://www.midstaffspublicinquiry.com/"}
        ],
        "related": ["University Hospitals of North Midlands NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Premises (other) — University Hospitals of North Midlands NHS Trust", "Impairments net of reversals — The Shrewsbury and Telford Hospital NHS Trust", "Department of Health and Social Care"]
    },
    "Impairments net of reversals — University Hospital Southampton NHS Foundation Trust": {
        "aliases": [{"name": "Impairments net of reversals", "parent": "University Hospital Southampton NHS Foundation Trust"}],
        "description": "Non-cash IAS 36 writedown at UHS in 2024-25, driven by MEA-DRC revaluation of the Tremona Road campus — Southampton General Hospital (1970s tower), Princess Anne Hospital (maternity), Wessex Cardiothoracic Centre. The trust runs supra-regional cardiothoracic, neuroscience and major-trauma services for Wessex, with specialty equipment cycles (cardiac MRI, hybrid theatres, NICU plant) generating equipment-MEA writedowns alongside building revaluation.",
        "beneficiaries": "Approximately 1.9M residents of Hampshire, Isle of Wight and parts of Wiltshire and Dorset for tertiary care; ~12,000 staff; impairment affects c. 195,000 m² of Tremona Road campus freehold plus community/dialysis network.",
        "legal_basis": "IAS 36 · DHSC GAM 2024-25 ch.4 · NHS Act 2006 · Health and Care Act 2022 · IFRS 13",
        "key_stats": [
            {"label": "Impairments 2024-25", "value": "£6.80M"},
            {"label": "5-year impairment trend", "value": "2020-21 £3.0M · 2021-22 £4.2M · 2022-23 £5.3M · 2023-24 £6.1M · 2024-25 £6.80M"},
            {"label": "MEA-DRC valuation cycle", "value": "Indexed via VOA 2024-25; full revaluation last 2022-23"},
            {"label": "RAAC status", "value": "Not on HSSIB Sep 2023 confirmed-priority list (Tremona Road tower is reinforced concrete frame, not RAAC)"},
            {"label": "NHP scheme status", "value": "Not in NHP cohort; envelope refresh via ICB/ERIC channels"},
            {"label": "Estate scale", "value": "Southampton General ~1,000 beds + Princess Anne ~150 + Wessex Cardiothoracic + community sites"},
            {"label": "Specialty equipment", "value": "Cardiac MRI + hybrid theatre + NICU + cyclotron/cancer plant cycles drive equipment-MEA volatility"},
            {"label": "Carrying value impacted", "value": "PPE NBV c. £400M; impairment c. 1.7% of NBV"},
            {"label": "1970s tower envelope", "value": "Southampton General West Wing tower 1972 build; reaching end of typical envelope economic life"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2022-23 last full revaluation · Successor: 2027-28 next quinquennial; estate strategy refresh under Hampshire & IoW ICS"},
            {"label": "Evaluation evidence", "value": "NAO Estate 2020 · DHSC ARA 2023-24 · CQC inspection 2023 (RHM)"},
            {"label": "Peer benchmark", "value": "In line with large-teaching-trust median per £ NBV"}
        ],
        "notes": "UHS's impairment is moderate relative to estate scale, reflecting a generally well-maintained Tremona Road campus and ongoing staged refresh through ICB capital channels. The 1970s West Wing tower is reaching the typical 50-year envelope economic life and contributes to the rising MEA gap. Specialty equipment cycles in cardiac MRI, hybrid theatres and NICU plant are the rising contribution. The 2024-25 indexed VOA uplift across south-coast property markets adds the YoY rise.",
        "sources": [
            {"publisher": "University Hospital Southampton NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.uhs.nhs.uk/about-us/our-publications/"},
            {"publisher": "DHSC", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Estates Returns Information Collection (ERIC) 2023-24", "url": "https://www.england.nhs.uk/estates-returns-information-collection/"},
            {"publisher": "Care Quality Commission", "title": "UHS provider profile (RHM)", "url": "https://www.cqc.org.uk/provider/RHM"},
            {"publisher": "NAO", "title": "Maintaining the NHS Estate (2020)", "url": "https://www.nao.org.uk/reports/maintaining-the-nhs-estate/"}
        ],
        "related": ["University Hospital Southampton NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Premises (other) — University Hospital Southampton NHS Foundation Trust", "Impairments net of reversals — Hampshire Hospitals NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Impairments net of reversals — Kettering General Hospital NHS Foundation Trust": {
        "aliases": [{"name": "Impairments net of reversals", "parent": "Kettering General Hospital NHS Foundation Trust"}],
        "description": "Non-cash IAS 36 writedown at KGH in 2024-25, driven by MEA-DRC revaluation of the Rothwell Road campus — a layered estate with the 1897 Victorian frontage (locally listed), the 1970s tower, and the Treetops 2000s extension. KGH is in the New Hospital Programme cohort for major refurbishment-and-rebuild on the existing site, with the NHP Reset Jan 2025 deferral triggering immediate impairment review on existing structures held against expected new build.",
        "beneficiaries": "Approximately 380,000 residents of Northamptonshire's eastern catchment plus parts of Bedfordshire, Cambridgeshire and Leicestershire; ~4,300 staff; impairment affects c. 95,000 m² of layered freehold across the Rothwell Road campus.",
        "legal_basis": "IAS 36 · DHSC GAM 2024-25 ch.4 · NHS Act 2006 · Health and Care Act 2022 · IFRS 13",
        "key_stats": [
            {"label": "Impairments 2024-25", "value": "£6.75M"},
            {"label": "5-year impairment trend", "value": "2020-21 £2.2M · 2021-22 £3.5M · 2022-23 £4.8M · 2023-24 £5.9M · 2024-25 £6.75M"},
            {"label": "MEA-DRC valuation cycle", "value": "Indexed via VOA 2024-25; full revaluation last 2021-22"},
            {"label": "RAAC status", "value": "KGH on HSSIB Sep 2023 RAAC alert list — confirmed RAAC in some 1970s structures"},
            {"label": "NHP scheme status", "value": "KGH in NHP cohort (refurb-and-rebuild on Rothwell Road); NHP Reset Jan 2025 deferred timeline → impairment review triggered"},
            {"label": "Listed-fabric element", "value": "1897 Victorian frontage block locally listed; modernisation cost exceeds MEA"},
            {"label": "Estate scale", "value": "Kettering General ~600 beds + Treetops + Newton Day Surgery + community sites"},
            {"label": "Carrying value impacted", "value": "PPE NBV c. £140M; impairment c. 4.8% of NBV (elevated)"},
            {"label": "RAAC mitigation", "value": "Localised props, monitoring and decant in 1970s blocks ongoing through 2024-25"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2021-22 last full revaluation · Successor: NHP refurb/rebuild (Reset Wave 2 timing TBD)"},
            {"label": "Evaluation evidence", "value": "NAO NHP report 2023 · PAC NHP scrutiny 2024 · HSSIB RAAC alert Sep 2023 · DHSC ARA 2023-24"},
            {"label": "Peer benchmark", "value": "Materially above district-general acute median (RAAC + NHP-deferral combination)"}
        ],
        "notes": "KGH's impairment is materially driven by a triple-compound — confirmed RAAC presence in 1970s structures (HSSIB Sep 2023 alert), NHP Reset Jan 2025 deferral of the planned refurb/rebuild, and chronic listed-fabric carrying-value gap on the 1897 Victorian frontage. RAAC mitigation costs (props, monitoring, decant) flow through both capital and operating budgets; the writedown line captures the structural carrying-value reset. The trust's Group Model with Northampton General is enabling some shared estate planning through the East Midlands ICS.",
        "sources": [
            {"publisher": "Kettering General Hospital NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.kgh.nhs.uk/our-publications"},
            {"publisher": "DHSC", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "New Hospital Programme: Plan for implementation (Reset, Jan 2025)", "url": "https://www.gov.uk/government/publications/new-hospital-programme-plan-for-implementation"},
            {"publisher": "NAO", "title": "New Hospital Programme (2023)", "url": "https://www.nao.org.uk/reports/new-hospital-programme/"},
            {"publisher": "Care Quality Commission", "title": "KGH provider profile (RNQ)", "url": "https://www.cqc.org.uk/provider/RNQ"}
        ],
        "related": ["Kettering General Hospital NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Premises (other) — Kettering General Hospital NHS Foundation Trust", "Impairments net of reversals — Northampton General Hospital NHS Trust", "New Hospital Programme"]
    },
    "Impairments net of reversals — United Lincolnshire Hospitals NHS Trust": {
        "aliases": [{"name": "Impairments net of reversals", "parent": "United Lincolnshire Hospitals NHS Trust"}],
        "description": "Non-cash IAS 36 writedown at ULHT in 2024-25, driven by MEA-DRC revaluation of three principal acute sites — Lincoln County Hospital (Greetwell Road), Pilgrim Hospital Boston (the East Lincolnshire coastal site, with confirmed RAAC presence), and Grantham & District Hospital. Pilgrim Boston is on the HSSIB Sep 2023 confirmed-RAAC priority list and carries the bulk of the trust's writedown driver, alongside coastal salt-corrosion exposure.",
        "beneficiaries": "Approximately 770,000 residents of Lincolnshire — a large rural geography with significant deprivation and travel-time challenges; ~7,500 staff; impairment affects c. 220,000 m² across the three-site freehold estate.",
        "legal_basis": "IAS 36 · DHSC GAM 2024-25 ch.4 · NHS Act 2006 · Health and Care Act 2022 · IFRS 13",
        "key_stats": [
            {"label": "Impairments 2024-25", "value": "£6.58M"},
            {"label": "5-year impairment trend", "value": "2020-21 £2.5M · 2021-22 £3.7M · 2022-23 £4.8M · 2023-24 £5.7M · 2024-25 £6.58M"},
            {"label": "MEA-DRC valuation cycle", "value": "Full revaluation due 2024-25"},
            {"label": "RAAC status", "value": "Pilgrim Hospital Boston on HSSIB Sep 2023 confirmed-priority RAAC list — significant structural mitigation programme"},
            {"label": "NHP scheme status", "value": "Pilgrim Boston in NHP cohort (RAAC-prioritised); NHP Reset Jan 2025 reaffirmed RAAC trusts but slipped delivery timelines"},
            {"label": "Coastal exposure", "value": "Pilgrim Boston coastal salt-corrosion compounding RAAC structural decay"},
            {"label": "Estate scale", "value": "Lincoln County ~600 beds + Pilgrim Boston ~370 beds + Grantham ~200 beds + community sites"},
            {"label": "Carrying value impacted", "value": "PPE NBV c. £180M; impairment c. 3.7% of NBV"},
            {"label": "Rural geography", "value": "Trust serves UK's fourth-largest county by area; estate spread amplifies per-site overhead and impairment volatility"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2019-20 last full revaluation · Successor: 2024-25 cycle outcome + NHP Pilgrim rebuild (Wave 2 TBD)"},
            {"label": "Evaluation evidence", "value": "HSSIB RAAC alert Sep 2023 · NAO NHP report 2023 · CQC inspection 2023 (RWD)"},
            {"label": "Peer benchmark", "value": "Above district-general acute median (RAAC + coastal compound)"}
        ],
        "notes": "ULHT's impairment line is dominated by Pilgrim Hospital Boston — confirmed RAAC presence (HSSIB Sep 2023 priority list) compounds with coastal salt-corrosion to produce structural decay that the 2024-25 full revaluation cycle is now formally recognising. The NHP Reset Jan 2025 reaffirmed RAAC trusts as a priority but slipped delivery timelines, extending the operating-cost burden of mitigation. Lincolnshire's large rural geography drives elevated per-site overhead. Decarbonisation work is constrained while the NHP timeline at Pilgrim is unresolved.",
        "sources": [
            {"publisher": "United Lincolnshire Hospitals NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.ulh.nhs.uk/about/publications/"},
            {"publisher": "DHSC", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "New Hospital Programme: Plan for implementation (Reset, Jan 2025)", "url": "https://www.gov.uk/government/publications/new-hospital-programme-plan-for-implementation"},
            {"publisher": "Health Services Safety Investigations Body", "title": "RAAC in NHS hospital buildings (Sep 2023)", "url": "https://www.hssib.org.uk/"},
            {"publisher": "Care Quality Commission", "title": "ULHT provider profile (RWD)", "url": "https://www.cqc.org.uk/provider/RWD"}
        ],
        "related": ["United Lincolnshire Hospitals NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Premises (other) — United Lincolnshire Hospitals NHS Trust", "Impairments net of reversals — Northern Lincolnshire and Goole NHS Foundation Trust", "New Hospital Programme"]
    },
    "Impairments net of reversals — Isle of Wight NHS Trust": {
        "aliases": [{"name": "Impairments net of reversals", "parent": "Isle of Wight NHS Trust"}],
        "description": "Non-cash IAS 36 writedown at IoW NHS Trust in 2024-25, driven by MEA-DRC revaluation of the trust's unique integrated estate — St Mary's Hospital Newport (the island's only acute hospital, mixed 1990s/older fabric) plus the integrated mental health, ambulance and community sites across the Isle of Wight. The trust is the only fully-integrated acute+MH+community+ambulance trust in England, generating an unusual cross-service estate footprint. Coastal salt-corrosion exposure is significant.",
        "beneficiaries": "Approximately 140,000 island residents reliant on St Mary's as the sole acute hospital; ~3,000 staff; impairment affects c. 75,000 m² of trust freehold including the integrated ambulance and MH estate.",
        "legal_basis": "IAS 36 · DHSC GAM 2024-25 ch.4 · NHS Act 2006 · Health and Care Act 2022 · IFRS 13",
        "key_stats": [
            {"label": "Impairments 2024-25", "value": "£6.44M"},
            {"label": "5-year impairment trend", "value": "2020-21 £2.0M · 2021-22 £3.4M · 2022-23 £4.6M · 2023-24 £5.6M · 2024-25 £6.44M (rising)"},
            {"label": "MEA-DRC valuation cycle", "value": "Indexed via VOA 2024-25; full revaluation last 2021-22"},
            {"label": "RAAC status", "value": "Not on HSSIB Sep 2023 confirmed-priority list"},
            {"label": "NHP scheme status", "value": "Not in NHP cohort (small scheme proposals at St Mary's pursued via ICB capital)"},
            {"label": "Coastal exposure", "value": "Whole-island estate flagged for salt-corrosion monitoring; St Mary's, ambulance stations, MH units all affected"},
            {"label": "Integrated trust profile", "value": "Only fully-integrated acute+MH+community+ambulance trust in England — atypical estate basket per IFRS 13"},
            {"label": "Estate scale", "value": "St Mary's ~250 beds + Sevenacres MH unit + ~10 community sites + island-wide ambulance estate"},
            {"label": "Carrying value impacted", "value": "PPE NBV c. £80M; impairment c. 8% of NBV (very elevated for trust size)"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2021-22 last full revaluation · Successor: estate strategy aligned to Hampshire & IoW ICS partnership with UHS (acute hub-and-spoke since 2019)"},
            {"label": "Evaluation evidence", "value": "NAO Estate 2020 · CQC inspection 2023 (R1F) · DHSC ARA 2023-24"},
            {"label": "Peer benchmark", "value": "Far above acute-trust median per £ NBV (small-trust + coastal + integrated combination)"}
        ],
        "notes": "IoW NHS Trust is the only fully-integrated acute+MH+community+ambulance trust in England, generating an atypical estate basket where impairment volatility hits a single SoFP rather than splitting across category-specific trusts. Coastal salt-corrosion exposure across the entire island estate (St Mary's, MH, ambulance, community) makes the writedown line structurally elevated relative to trust size. The 2019 UHS hub-and-spoke partnership has stabilised tertiary clinical pathways but does not address island-side estate burden. The 2024-25 indexed VOA uplift adds the YoY rise.",
        "sources": [
            {"publisher": "Isle of Wight NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.iow.nhs.uk/about-us/key-documents/"},
            {"publisher": "DHSC", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Estates Returns Information Collection (ERIC) 2023-24", "url": "https://www.england.nhs.uk/estates-returns-information-collection/"},
            {"publisher": "Care Quality Commission", "title": "IoW NHS Trust provider profile (R1F)", "url": "https://www.cqc.org.uk/provider/R1F"},
            {"publisher": "NAO", "title": "Maintaining the NHS Estate (2020)", "url": "https://www.nao.org.uk/reports/maintaining-the-nhs-estate/"}
        ],
        "related": ["Isle of Wight NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Premises (other) — Isle of Wight NHS Trust", "Impairments net of reversals — University Hospital Southampton NHS Foundation Trust", "Department of Health and Social Care"]
    },
}
