# -*- coding: utf-8 -*-
# Phase 2 MH slice 2 — chunk 11 (17 NHS Mental Health Trust orphan sub-lines)
# Hand-curated trust-specific PROGRAMME-archetype enrichment entries.
# Structural contract per docs/archetype_briefs.md.

NEW = {
    "Lease expenditure — Birmingham and Solihull Mental Health NHS Foundation Trust": {
        "aliases": [{"name": "Lease expenditure", "parent": "Birmingham and Solihull Mental Health NHS Foundation Trust"}],
        "description": "BSMHFT's £0.61M lease expenditure reflects IFRS 16 right-of-use depreciation + interest charges on the trust's leased estate following the 2022 on-balance-sheet transition. The portfolio is dominated by NHS Property Services-leased community-MH and CAMHS premises across Birmingham (Reaside, Aston, Yardley, Erdington) and Solihull, plus Community Health Partnerships LIFT vehicles for primary-care-co-located bases — the Oleaster, Ardenleigh and Reaside hubs anchor the inpatient estate while c. 30+ leased community sites sustain the line.",
        "beneficiaries": "c. 4,000 staff serving a registered catchment of c. 1.4M across Birmingham and Solihull; leased-estate component covers c. 30+ community-MH, CAMHS, perinatal-MH, EIP and recovery-college bases plus secure-MH ancillary support space.",
        "legal_basis": "IFRS 16 Leases · DHSC Group Accounting Manual 2024-25 ch.7 · Landlord and Tenant Act 1954 · NHS Act 2006 · Health and Care Act 2022 · IFRIC 12 Service Concession Arrangements (where applicable to LIFT lease-components)",
        "key_stats": [
            {"label": "Lease expenditure 2024-25", "value": "£0.61M"},
            {"label": "IFRS 16 transition jump", "value": "2022 on-balance-sheet adoption — operating leases reclassified to ROU asset + lease liability with depreciation + interest split"},
            {"label": "Leased site count", "value": "c. 30+ NHSPS + CHP-LIFT community-MH, CAMHS, perinatal-MH and EIP bases"},
            {"label": "Major lessor", "value": "NHS Property Services Ltd (majority) + Community Health Partnerships (LIFT) + private landlords + University of Birmingham (Oleaster co-location)"},
            {"label": "NHSPS rates dispute", "value": "Sustained NHSPS / MH-trust dispute on community-clinic market-rent uplift + service-charge methodology — feeds annual lease-cost volatility"},
            {"label": "Discount rate applied", "value": "HM Treasury PES discount rate per DHSC GAM 2024-25 ch.7 — recalibrated annually"},
            {"label": "Lease term profile", "value": "Mix of 5-year + 10-year community clinic leases; longer-term LIFT contracts to 25+ years"},
            {"label": "Funding trajectory", "value": "2021-22 (pre-IFRS16) c. £0.3M operating lease → 2022-23 c. £0.5M ROU first year → 2024-25 £0.61M (sustained NHSPS uplift)"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + NHSPS + CHP for LIFT vehicles"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + Birmingham and Solihull ICB · IFRS 16 / DHSC GAM ch.7 oversight"},
            {"label": "Evaluation evidence", "value": "Trust ARA 2023-24 disclosure; CQC inspection reports (RXT); BSOL ICS estate strategy"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2022 IAS 17 operating-lease expense · Successor: NHSPS market-rent reform + BSOL ICS estate consolidation"}
        ],
        "notes": "BSMHFT's lease line jumped at the IFRS 16 2022 transition as previously off-balance-sheet operating leases moved on-balance-sheet, and has continued to grow as NHS Property Services pursued market-rent uplifts on community clinics. The trust's split between centralised inpatient hubs (Oleaster on the Queen Elizabeth Hospital site, Ardenleigh medium-secure, Reaside Clinic) and a dispersed community-MH footprint across Birmingham and Solihull means the leased component sits on the smaller community/CAMHS/perinatal end of the estate. The University of Birmingham co-location at the Oleaster contributes a non-NHSPS lease element. BSOL ICS estate consolidation under the long-term plan is the medium-term lever to flatten cost growth.",
        "sources": [
            {"publisher": "Birmingham and Solihull Mental Health NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.bsmhft.nhs.uk/about-us/publications/annual-reports/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 7 — Leases)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS Property Services", "title": "Annual Report 2023-24 + market-rent methodology", "url": "https://www.property.nhs.uk/about/our-publications/"},
            {"publisher": "Community Health Partnerships", "title": "LIFT estate annual review", "url": "https://www.communityhealthpartnerships.co.uk/"},
            {"publisher": "Care Quality Commission", "title": "BSMHFT provider profile (RXT)", "url": "https://www.cqc.org.uk/provider/RXT"}
        ],
        "related": ["Birmingham and Solihull Mental Health NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "NHS Property Services Ltd", "Lease expenditure — Mersey Care NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Lease expenditure — West London NHS Trust": {
        "aliases": [{"name": "Lease expenditure", "parent": "West London NHS Trust"}],
        "description": "West London NHS Trust's £0.59M lease expenditure reflects IFRS 16 right-of-use depreciation + interest charges on the trust's leased estate following the 2022 on-balance-sheet transition. The portfolio is dominated by NHS Property Services-leased community-MH and CAMHS premises across Hammersmith & Fulham, Ealing and Hounslow, plus specialist co-location and ancillary leases supporting the Broadmoor Hospital high-secure men's service at Crowthorne and the St Bernard's / West London Forensic Service campus at Southall.",
        "beneficiaries": "c. 4,500 staff serving a registered catchment of c. 800,000 across Hammersmith & Fulham, Ealing and Hounslow, plus the national Broadmoor high-secure men's catchment; leased component covers c. 25+ community-MH, CAMHS, addictions and forensic-step-down bases.",
        "legal_basis": "IFRS 16 Leases · DHSC Group Accounting Manual 2024-25 ch.7 · Landlord and Tenant Act 1954 · NHS Act 2006 · Health and Care Act 2022 · Mental Health Act 1983 (high-secure estate provisions)",
        "key_stats": [
            {"label": "Lease expenditure 2024-25", "value": "£0.59M"},
            {"label": "IFRS 16 transition jump", "value": "2022 on-balance-sheet adoption — operating leases reclassified to ROU asset + lease liability with depreciation + interest split"},
            {"label": "Leased site count", "value": "c. 25+ NHSPS + private-landlord community-MH, CAMHS, addictions and forensic-step-down bases"},
            {"label": "Major lessor", "value": "NHS Property Services Ltd (majority) + Community Health Partnerships + private landlords"},
            {"label": "Inpatient anchor sites (owned/PFI)", "value": "Broadmoor Hospital (Crowthorne, high-secure) + St Bernard's (Southall) + Lakeside MH unit (West Mid Hospital) — owned/PFI, not in lease line"},
            {"label": "NHSPS rates dispute", "value": "Sustained NHSPS / MH-trust dispute on community-clinic market-rent uplift + service-charge methodology — feeds annual lease-cost volatility"},
            {"label": "Discount rate applied", "value": "HM Treasury PES discount rate per DHSC GAM 2024-25 ch.7 — recalibrated annually"},
            {"label": "Lease term profile", "value": "Mix of 5-year + 10-year community clinic leases plus shorter satellite/forensic-step-down house leases"},
            {"label": "Funding trajectory", "value": "2021-22 (pre-IFRS16) c. £0.3M operating lease → 2022-23 c. £0.5M ROU first year → 2024-25 £0.59M"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + NHSPS + CHP for LIFT vehicles"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + NW London ICB · IFRS 16 / DHSC GAM ch.7 oversight"},
            {"label": "Evaluation evidence", "value": "Trust ARA 2023-24 disclosure; CQC inspection reports (RKL); NW London ICS estate strategy; Broadmoor redevelopment context"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2022 IAS 17 operating-lease expense · Successor: NHSPS market-rent reform + NW London ICS estate consolidation"}
        ],
        "notes": "West London NHS Trust's lease line is driven by the community-MH and forensic-step-down dispersed footprint, while the headline inpatient anchors (Broadmoor high-secure men's service, St Bernard's forensic campus, Lakeside MH unit) sit outside the lease line as owned or PFI-financed estate. The 2019 Broadmoor new-build replaced the Victorian asylum and reshaped the high-secure capital base; subsequent forensic-step-down community accommodation has expanded the leased footprint. NHS Property Services market-rent uplift on community clinics across NW London continues to drive year-on-year volatility. NW London ICS estate consolidation is the medium-term lever for the community-MH lease portfolio.",
        "sources": [
            {"publisher": "West London NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.westlondon.nhs.uk/about-our-services/corporate-information/our-publications"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 7 — Leases)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS Property Services", "title": "Annual Report 2023-24 + market-rent methodology", "url": "https://www.property.nhs.uk/about/our-publications/"},
            {"publisher": "Care Quality Commission", "title": "West London NHS Trust provider profile (RKL)", "url": "https://www.cqc.org.uk/provider/RKL"},
            {"publisher": "NHS England", "title": "High Secure Mental Health Services + Broadmoor redevelopment", "url": "https://www.england.nhs.uk/commissioning/spec-services/npc-crg/group-c/c02/"}
        ],
        "related": ["West London NHS Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "NHS Property Services Ltd", "Lease expenditure — Birmingham and Solihull Mental Health NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Impairments net of reversals — Devon Partnership NHS Trust": {
        "aliases": [{"name": "Impairments net of reversals", "parent": "Devon Partnership NHS Trust"}],
        "description": "DPT's £0.57M net impairments charge captures non-cash writedowns (and reversals) on property, plant and equipment under IAS 36 / DHSC GAM, triggered by the annual District Valuer revaluation cycle and event-based impairment reviews on inpatient wards and community premises across Devon. Drivers include the long-running estate-rationalisation programme — Langdon Hospital (Dawlish) secure-services consolidation, Wonford House (Exeter) acute-MH redevelopment plans and dispersed community-MH base reviews — combined with cost-vs-value reassessments on EBITDA-additive sites.",
        "beneficiaries": "c. 3,300 staff and a registered catchment of c. 850,000 across Devon (excluding Plymouth and Torbay); estate footprint covers Wonford House, Langdon Hospital secure-services campus, Cygnet ward portfolio, dispersed CAMHS, EIP and recovery-college bases.",
        "legal_basis": "IAS 36 Impairment of Assets · IAS 16 Property, Plant and Equipment · DHSC Group Accounting Manual 2024-25 ch.4 · NHS Act 2006 · Health and Care Act 2022 · IFRS 13 Fair Value Measurement",
        "key_stats": [
            {"label": "Impairments net of reversals 2024-25", "value": "£0.57M"},
            {"label": "Trigger mechanism", "value": "Annual District Valuer revaluation + event-based reviews under DHSC GAM 2024-25 ch.4"},
            {"label": "Major estate components", "value": "Wonford House (Exeter, acute-MH) + Langdon Hospital (Dawlish, secure-services) + dispersed community-MH bases"},
            {"label": "Composition", "value": "Downward revaluation of land + buildings + plant + equipment, net of reversals where market evidence supports recovery"},
            {"label": "Modern Equivalent Asset basis", "value": "DHSC GAM uses MEA / depreciated replacement cost for specialised NHS estate — sensitive to construction-cost CPI"},
            {"label": "Estate strategy context", "value": "Long-running rationalisation; Wonford House redevelopment plan in scoping; community-base portfolio reviewed against ICS estate strategy"},
            {"label": "BCIS construction CPI", "value": "RICS BCIS general building cost index movements drive valuation outcomes year-to-year"},
            {"label": "Funding trajectory", "value": "Volatile by nature — non-cash; 2020-21 to 2024-25 oscillates between low single-digit £M charges and credits"},
            {"label": "Delivery body", "value": "Trust Estates + Finance + District Valuer (VOA) for revaluation"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + Devon ICB; HM Treasury FReM / DHSC GAM oversight"},
            {"label": "Evaluation evidence", "value": "Trust ARA 2023-24 fixed-asset note + impairment disclosure; District Valuer reports; CQC RWV provider profile"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2010 historical-cost basis · Successor: ongoing 5-yearly DV revaluation under DHSC GAM ch.4"}
        ],
        "notes": "DPT's impairments line is structurally non-cash and driven by the annual District Valuer revaluation under the Modern Equivalent Asset / depreciated replacement cost basis prescribed by DHSC GAM ch.4 — sensitive to RICS BCIS construction-cost CPI movements rather than service activity. The trust's estate is dominated by Wonford House (Exeter acute-MH) and Langdon Hospital secure-services campus at Dawlish, where event-based reviews on planned redevelopment can crystallise impairments. The Devon ICS estate strategy and Wonford House redevelopment scoping shape forward-year impairment risk. Volatility is normal — the line can swing materially year-to-year as DV outputs land, and reversals are recognised where market evidence supports recovery.",
        "sources": [
            {"publisher": "Devon Partnership NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.dpt.nhs.uk/about-us/publications/annual-reports"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 4 — Property, plant and equipment)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Valuation Office Agency", "title": "District Valuer Services — NHS revaluation", "url": "https://www.gov.uk/government/organisations/valuation-office-agency"},
            {"publisher": "RICS", "title": "BCIS Building Cost Information Service", "url": "https://bcis.co.uk/"},
            {"publisher": "Care Quality Commission", "title": "Devon Partnership NHS Trust provider profile (RWV)", "url": "https://www.cqc.org.uk/provider/RWV"}
        ],
        "related": ["Devon Partnership NHS Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Valuation Office Agency", "Impairments net of reversals — Leeds and York Partnership NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Establishment costs — North Staffordshire Combined Healthcare NHS Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "North Staffordshire Combined Healthcare NHS Trust"}],
        "description": "Combined Healthcare's £0.56M establishment-costs line covers postage, telephony, stationery, IT consumables, advertising + recruitment, training overheads and other office-operating costs across the trust's Stoke-on-Trent + North Staffordshire footprint — the Harplands Hospital (Stoke) anchor inpatient site and c. 25+ community-MH, CAMHS, addictions and LD bases serving the city of Stoke-on-Trent and the rural Staffordshire Moorlands and Newcastle-under-Lyme districts.",
        "beneficiaries": "c. 1,800 staff and a registered catchment of c. 470,000 across Stoke-on-Trent, Newcastle-under-Lyme and the Staffordshire Moorlands; supports community-MH, CAMHS, addictions, EIP and LD pathways alongside Harplands inpatient services.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · NHS Act 2006 · Health and Care Act 2022 · Public Contracts Regulations 2015 / Procurement Act 2023 (telephony + IT framework procurement)",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£0.56M"},
            {"label": "Composition", "value": "Postage + telephony + stationery + IT consumables + advertising + recruitment + training overheads + minor office-operating costs"},
            {"label": "Site footprint generating consumption", "value": "Harplands Hospital (Stoke, c. 121 beds) + c. 25+ community-MH, CAMHS, addictions and LD bases"},
            {"label": "Recruitment driver", "value": "MH workforce shortage — sustained advertising spend on consultant psychiatrist + community-MH-nursing recruitment"},
            {"label": "Telephony / IT frameworks", "value": "NHS Shared Business Services + Crown Commercial Service category contracts + Frontline Digitisation EPR roll-in"},
            {"label": "Training overheads", "value": "MHA s.5(2) statutory training + restraint reduction (Restraint Reduction Network) + HEE / NHSE workforce development"},
            {"label": "April 2025 NIC step-up", "value": "Employer NIC threshold drop + rate rise (Apr 2025) raises forward employer-cost on training + recruitment-onboarding"},
            {"label": "Funding trajectory", "value": "2020-21 c. £0.4M → 2024-25 £0.56M — uplift driven by post-pandemic recruitment + telephony / IT CPI"},
            {"label": "Delivery body", "value": "Trust Procurement + HR + IT teams"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + Staffordshire and Stoke-on-Trent ICB"},
            {"label": "Evaluation evidence", "value": "Trust ARA 2023-24 disclosure; CQC inspection reports (RLY); SST ICS workforce strategy"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2018 fragmented spot-buy regime · Successor: NHS Shared Business Services category consolidation + Procurement Act 2023"}
        ],
        "notes": "Combined Healthcare's establishment-costs line is sized to a small-trust footprint (c. 1,800 staff, c. 470,000 catchment) anchored by Harplands Hospital in Stoke and a dispersed community estate across the Staffordshire Moorlands. Recruitment advertising is a structural driver — the trust competes with larger Midlands MH peers for consultant psychiatrist and community-MH-nursing capacity, particularly post-pandemic. Frontline Digitisation EPR rollout is shifting some IT consumables spend into capital + amortisation, partially offsetting establishment-line growth. NHS Shared Business Services category consolidation and the Procurement Act 2023 transition (in force October 2024) reshape the framework architecture but the near-term cost driver remains telephony + recruitment CPI.",
        "sources": [
            {"publisher": "North Staffordshire Combined Healthcare NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.combined.nhs.uk/about-us/publications/annual-reports/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS Shared Business Services", "title": "Procurement frameworks + category contracts", "url": "https://www.sbs.nhs.uk/"},
            {"publisher": "Cabinet Office", "title": "Procurement Act 2023 + transition guidance", "url": "https://www.gov.uk/government/collections/procurement-act-2023-guidance-documents"},
            {"publisher": "Care Quality Commission", "title": "Combined Healthcare provider profile (RLY)", "url": "https://www.cqc.org.uk/provider/RLY"}
        ],
        "related": ["North Staffordshire Combined Healthcare NHS Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Department of Health and Social Care", "Establishment costs — Bradford District Care NHS Foundation Trust", "Staffordshire and Stoke-on-Trent ICB"]
    },
    "PFI / LIFT charges — Leicestershire Partnership NHS Trust": {
        "aliases": [{"name": "PFI / LIFT charges", "parent": "Leicestershire Partnership NHS Trust"}],
        "description": "LPT's £0.55M PFI / LIFT charge reflects the trust's occupation of LIFT-procured community-MH and integrated-care bases across Leicester, Leicestershire and Rutland under the Leicester Health Investments LIFT vehicle (Community Health Partnerships shareholding + private partners + LA co-investment). The line covers the unitary-charge pass-through — debt service, FM lifecycle and soft-FM components — for those LIFT premises hosting MH community teams, CAMHS hubs and integrated primary-care-co-located bases.",
        "beneficiaries": "c. 5,500 staff and a registered catchment of c. 1.1M across Leicester city, Leicestershire county and Rutland; LIFT-procured estate hosts community-MH team bases, CAMHS hubs, addictions services and integrated primary-care-co-located bases.",
        "legal_basis": "IFRS 16 Leases (post-2022 transition for finance-lease + service-concession arrangements) · IFRIC 12 Service Concession Arrangements · DHSC Group Accounting Manual 2024-25 ch.7 · NHS (Local Improvement Finance Trust) regulations · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "PFI / LIFT charges 2024-25", "value": "£0.55M"},
            {"label": "Procurement vehicle", "value": "Leicester Health Investments LIFT — CHP shareholding + private investor + LA partnership"},
            {"label": "Estate covered", "value": "Community-MH team bases + CAMHS hubs + addictions services + primary-care-co-located integrated bases"},
            {"label": "Unitary charge composition", "value": "Debt-service component + lifecycle (hard-FM building maintenance) + soft-FM (cleaning, security, catering where contracted)"},
            {"label": "Contract duration profile", "value": "LIFT contracts typically 25-year initial with extension option; Leicester LIFT signed mid-2000s — c. 8-12 years remaining"},
            {"label": "IFRS 16 / IFRIC 12 treatment", "value": "Service-concession assets recognised on-balance-sheet under IFRIC 12; lease-component re-evaluated under IFRS 16 ch.7 GAM"},
            {"label": "Lifecycle indexation", "value": "Annual RPI / CPI indexation per LIFT contract terms — material driver of year-on-year line movement"},
            {"label": "Funding trajectory", "value": "2020-21 c. £0.4M → 2024-25 £0.55M — sustained CPI-linked uplift"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + Community Health Partnerships + private LIFT investor consortium"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + Leicester, Leicestershire and Rutland ICB; LIFT policy oversight at DHSC"},
            {"label": "Evaluation evidence", "value": "NAO LIFT review 2017-18; trust ARA disclosure 2023-24; LLR ICS estate strategy; CQC RT5 provider profile"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-LIFT mid-2000s NHS-Estates community-clinic model · Successor: end-of-LIFT-contract review + ICS estate consolidation early 2030s"}
        ],
        "notes": "LPT's PFI / LIFT line is dominated by the Leicester Health Investments LIFT vehicle, which procured community-health bases in the mid-2000s under the Local Improvement Finance Trust model — service-concession structures where Community Health Partnerships (DHSC majority shareholder) co-invests with private partners and local-authority partners, and the trust occupies as tenant under unitary-charge contracts. CPI / RPI indexation is the main driver of cost growth, layered on fixed debt-service and lifecycle components. The trust's broader estate also includes the Bradgate Mental Health Unit (Glenfield Hospital site, owned/PFI-mixed), which sits in adjacent finance-lease and PFI service-charge lines. As LIFT contracts approach their 25-year endpoint in the early 2030s, LLR ICS faces strategic hand-back / extension / consolidation decisions.",
        "sources": [
            {"publisher": "Leicestershire Partnership NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.leicspart.nhs.uk/about/publications/annual-reports/"},
            {"publisher": "Community Health Partnerships", "title": "LIFT estate annual review", "url": "https://www.communityhealthpartnerships.co.uk/"},
            {"publisher": "National Audit Office", "title": "PFI and PF2 / LIFT review", "url": "https://www.nao.org.uk/reports/pfi-and-pf2/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 7 — Leases and service concessions)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "LPT provider profile (RT5)", "url": "https://www.cqc.org.uk/provider/RT5"}
        ],
        "related": ["Leicestershire Partnership NHS Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Community Health Partnerships", "PFI / LIFT charges — Cornwall Partnership NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Lease expenditure — Cambridgeshire and Peterborough NHS Foundation Trust": {
        "aliases": [{"name": "Lease expenditure", "parent": "Cambridgeshire and Peterborough NHS Foundation Trust"}],
        "description": "CPFT's £0.55M lease expenditure reflects IFRS 16 right-of-use depreciation + interest charges on the trust's leased estate following the 2022 on-balance-sheet transition. The portfolio is dominated by NHS Property Services-leased community-MH and CAMHS premises across the city of Cambridge, Peterborough, Huntingdonshire, Fenland, East Cambridgeshire and South Cambridgeshire, plus Community Health Partnerships LIFT vehicles for primary-care-co-located bases — the trust's combined MH + community + LD remit drives a wider site count than pure-MH peers.",
        "beneficiaries": "c. 4,500 staff and a registered catchment of c. 1.0M across Cambridgeshire and Peterborough; leased component covers c. 35+ community-MH, CAMHS, LD, older-people's MH and addictions bases plus integrated-care-system co-located sites.",
        "legal_basis": "IFRS 16 Leases · DHSC Group Accounting Manual 2024-25 ch.7 · Landlord and Tenant Act 1954 · NHS Act 2006 · Health and Care Act 2022 · IFRIC 12 Service Concession Arrangements (LIFT lease-components)",
        "key_stats": [
            {"label": "Lease expenditure 2024-25", "value": "£0.55M"},
            {"label": "IFRS 16 transition jump", "value": "2022 on-balance-sheet adoption — operating leases reclassified to ROU asset + lease liability with depreciation + interest split"},
            {"label": "Leased site count", "value": "c. 35+ NHSPS + CHP-LIFT community-MH, CAMHS, LD, older-people's MH and addictions bases"},
            {"label": "Major lessor", "value": "NHS Property Services Ltd (majority) + Community Health Partnerships (LIFT) + private landlords + University of Cambridge / Cambridge Biomedical Campus co-locations"},
            {"label": "NHSPS rates dispute", "value": "Sustained NHSPS / MH-trust dispute on community-clinic market-rent uplift + service-charge methodology — feeds annual lease-cost volatility"},
            {"label": "Discount rate applied", "value": "HM Treasury PES discount rate per DHSC GAM 2024-25 ch.7 — recalibrated annually"},
            {"label": "Lease term profile", "value": "Mix of 5-year + 10-year community clinic leases; longer-term LIFT contracts to 25+ years; CBC research-co-location bespoke terms"},
            {"label": "Combined MH + community footprint", "value": "Trust delivers MH + community physical-health + LD — wider site portfolio than pure-MH peers"},
            {"label": "Funding trajectory", "value": "2021-22 (pre-IFRS16) c. £0.3M operating lease → 2022-23 c. £0.45M ROU first year → 2024-25 £0.55M"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + NHSPS + CHP for LIFT vehicles"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + Cambridgeshire and Peterborough ICB · IFRS 16 / DHSC GAM ch.7 oversight"},
            {"label": "Evaluation evidence", "value": "Trust ARA 2023-24 disclosure; CQC inspection reports (RT1); CPICS estate strategy"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2022 IAS 17 operating-lease expense · Successor: NHSPS market-rent reform + CPICS estate consolidation"}
        ],
        "notes": "CPFT's lease line jumped at the IFRS 16 2022 transition as previously off-balance-sheet operating leases moved on-balance-sheet, and has continued to grow as NHS Property Services pursued market-rent uplifts on community clinics. The trust's combined MH + community physical-health + LD remit means the leased footprint is wider than pure-MH peers — c. 35+ community bases serving the dispersed Cambridgeshire and Peterborough geography plus Cambridge Biomedical Campus research co-locations. The Fulbourn Hospital inpatient anchor sits outside the lease line as owned/freehold estate. CPICS estate consolidation under the long-term plan is the medium-term lever to flatten cost growth.",
        "sources": [
            {"publisher": "Cambridgeshire and Peterborough NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.cpft.nhs.uk/about-us/our-publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 7 — Leases)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS Property Services", "title": "Annual Report 2023-24 + market-rent methodology", "url": "https://www.property.nhs.uk/about/our-publications/"},
            {"publisher": "Community Health Partnerships", "title": "LIFT estate annual review", "url": "https://www.communityhealthpartnerships.co.uk/"},
            {"publisher": "Care Quality Commission", "title": "CPFT provider profile (RT1)", "url": "https://www.cqc.org.uk/provider/RT1"}
        ],
        "related": ["Cambridgeshire and Peterborough NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "NHS Property Services Ltd", "Lease expenditure — Birmingham and Solihull Mental Health NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Impairments net of reversals — Birmingham and Solihull Mental Health NHS Foundation Trust": {
        "aliases": [{"name": "Impairments net of reversals", "parent": "Birmingham and Solihull Mental Health NHS Foundation Trust"}],
        "description": "BSMHFT's £0.54M net impairments charge captures non-cash writedowns (and reversals) on property, plant and equipment under IAS 36 / DHSC GAM, triggered by the annual District Valuer revaluation cycle and event-based impairment reviews on inpatient wards and community premises across Birmingham and Solihull. Drivers include estate-strategy reviews on the Reaside Clinic, Ardenleigh medium-secure unit, the Oleaster acute-MH hub at the QE Hospital site and dispersed community-MH bases, combined with cost-vs-value reassessments on capital-additive sites.",
        "beneficiaries": "c. 4,000 staff and a registered catchment of c. 1.4M across Birmingham and Solihull; estate footprint covers Reaside Clinic, Ardenleigh medium-secure unit, the Oleaster, Tamarind Centre, Zinnia Centre and dispersed community-MH, perinatal-MH and CAMHS bases.",
        "legal_basis": "IAS 36 Impairment of Assets · IAS 16 Property, Plant and Equipment · DHSC Group Accounting Manual 2024-25 ch.4 · NHS Act 2006 · Health and Care Act 2022 · IFRS 13 Fair Value Measurement",
        "key_stats": [
            {"label": "Impairments net of reversals 2024-25", "value": "£0.54M"},
            {"label": "Trigger mechanism", "value": "Annual District Valuer revaluation + event-based reviews under DHSC GAM 2024-25 ch.4"},
            {"label": "Major estate components", "value": "Reaside Clinic + Ardenleigh + Oleaster + Tamarind + Zinnia + dispersed community-MH bases"},
            {"label": "Composition", "value": "Downward revaluation of land + buildings + plant + equipment, net of reversals where market evidence supports recovery"},
            {"label": "Modern Equivalent Asset basis", "value": "DHSC GAM uses MEA / depreciated replacement cost for specialised NHS estate — sensitive to construction-cost CPI"},
            {"label": "Estate strategy context", "value": "Reaside Clinic redevelopment scoping; Ardenleigh secure-LD redesign; community-base portfolio reviewed against ICS estate strategy"},
            {"label": "BCIS construction CPI", "value": "RICS BCIS general building cost index movements drive valuation outcomes year-to-year"},
            {"label": "Funding trajectory", "value": "Volatile by nature — non-cash; 2020-21 to 2024-25 oscillates between low single-digit £M charges and credits"},
            {"label": "Delivery body", "value": "Trust Estates + Finance + District Valuer (VOA) for revaluation"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + BSOL ICB; HM Treasury FReM / DHSC GAM oversight"},
            {"label": "Evaluation evidence", "value": "Trust ARA 2023-24 fixed-asset note + impairment disclosure; District Valuer reports; CQC RXT provider profile"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2010 historical-cost basis · Successor: ongoing 5-yearly DV revaluation under DHSC GAM ch.4"}
        ],
        "notes": "BSMHFT's impairments line is structurally non-cash and driven by the annual District Valuer revaluation under the Modern Equivalent Asset / depreciated replacement cost basis prescribed by DHSC GAM ch.4 — sensitive to RICS BCIS construction-cost CPI movements rather than service activity. The Reaside Clinic medium-secure facility and Ardenleigh secure-LD unit are the two largest specialised-estate components where event-based reviews on planned redevelopment or service-model redesign can crystallise impairments. The Oleaster sits on the QE Hospital site as a relatively modern build with University of Birmingham co-location. Volatility is normal — the line can swing materially year-to-year as DV outputs land, and reversals are recognised where market evidence supports recovery.",
        "sources": [
            {"publisher": "Birmingham and Solihull Mental Health NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.bsmhft.nhs.uk/about-us/publications/annual-reports/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 4 — Property, plant and equipment)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Valuation Office Agency", "title": "District Valuer Services — NHS revaluation", "url": "https://www.gov.uk/government/organisations/valuation-office-agency"},
            {"publisher": "RICS", "title": "BCIS Building Cost Information Service", "url": "https://bcis.co.uk/"},
            {"publisher": "Care Quality Commission", "title": "BSMHFT provider profile (RXT)", "url": "https://www.cqc.org.uk/provider/RXT"}
        ],
        "related": ["Birmingham and Solihull Mental Health NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Valuation Office Agency", "Impairments net of reversals — Devon Partnership NHS Trust", "Department of Health and Social Care"]
    },
    "Lease expenditure — Cheshire and Wirral Partnership NHS Foundation Trust": {
        "aliases": [{"name": "Lease expenditure", "parent": "Cheshire and Wirral Partnership NHS Foundation Trust"}],
        "description": "CWP's £0.54M lease expenditure reflects IFRS 16 right-of-use depreciation + interest charges on the trust's leased estate following the 2022 on-balance-sheet transition. The portfolio is dominated by NHS Property Services-leased community-MH and CAMHS premises across Cheshire West, Cheshire East, the Wirral peninsula and parts of West Cheshire, plus Community Health Partnerships LIFT vehicles for primary-care-co-located bases. The trust's combined MH + LD + community remit drives a wider site count than pure-MH peers.",
        "beneficiaries": "c. 4,000 staff and a registered catchment of c. 1.0M across Cheshire West and Chester, Cheshire East, the Wirral and West Cheshire; leased component covers c. 30+ community-MH, CAMHS, LD, addictions and EIP bases plus all-age neurodevelopmental pathway sites.",
        "legal_basis": "IFRS 16 Leases · DHSC Group Accounting Manual 2024-25 ch.7 · Landlord and Tenant Act 1954 · NHS Act 2006 · Health and Care Act 2022 · IFRIC 12 Service Concession Arrangements (LIFT lease-components)",
        "key_stats": [
            {"label": "Lease expenditure 2024-25", "value": "£0.54M"},
            {"label": "IFRS 16 transition jump", "value": "2022 on-balance-sheet adoption — operating leases reclassified to ROU asset + lease liability with depreciation + interest split"},
            {"label": "Leased site count", "value": "c. 30+ NHSPS + CHP-LIFT community-MH, CAMHS, LD, addictions and EIP bases"},
            {"label": "Major lessor", "value": "NHS Property Services Ltd (majority) + Community Health Partnerships (LIFT) + private landlords"},
            {"label": "NHSPS rates dispute", "value": "Sustained NHSPS / MH-trust dispute on community-clinic market-rent uplift + service-charge methodology — feeds annual lease-cost volatility"},
            {"label": "Discount rate applied", "value": "HM Treasury PES discount rate per DHSC GAM 2024-25 ch.7 — recalibrated annually"},
            {"label": "Lease term profile", "value": "Mix of 5-year + 10-year community clinic leases; longer-term LIFT contracts to 25+ years"},
            {"label": "Combined MH + LD + community footprint", "value": "Trust delivers MH + LD + community physical-health (Wirral) — wider site portfolio than pure-MH peers"},
            {"label": "Funding trajectory", "value": "2021-22 (pre-IFRS16) c. £0.3M operating lease → 2022-23 c. £0.45M ROU first year → 2024-25 £0.54M"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + NHSPS + CHP for LIFT vehicles"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + Cheshire and Merseyside ICB · IFRS 16 / DHSC GAM ch.7 oversight"},
            {"label": "Evaluation evidence", "value": "Trust ARA 2023-24 disclosure; CQC inspection reports (RXA); C&M ICS estate strategy"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2022 IAS 17 operating-lease expense · Successor: NHSPS market-rent reform + C&M ICS estate consolidation"}
        ],
        "notes": "CWP's lease line jumped at the IFRS 16 2022 transition as previously off-balance-sheet operating leases moved on-balance-sheet, and has continued to grow as NHS Property Services pursued market-rent uplifts on community clinics. The trust's combined MH + LD + community physical-health (Wirral) remit means the leased footprint is wider than pure-MH peers — c. 30+ community bases serving the Cheshire and Wirral geography. The Countess of Chester, Bowmere Hospital and Springview (Wirral) inpatient anchors sit outside the lease line as owned/freehold estate. C&M ICS estate consolidation under the long-term plan is the medium-term lever; CWP shares the LIFT exposure profile with Mersey Care across the same regional vehicle architecture.",
        "sources": [
            {"publisher": "Cheshire and Wirral Partnership NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.cwp.nhs.uk/about-us/publications-and-policies/annual-reports/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 7 — Leases)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS Property Services", "title": "Annual Report 2023-24 + market-rent methodology", "url": "https://www.property.nhs.uk/about/our-publications/"},
            {"publisher": "Community Health Partnerships", "title": "LIFT estate annual review", "url": "https://www.communityhealthpartnerships.co.uk/"},
            {"publisher": "Care Quality Commission", "title": "CWP provider profile (RXA)", "url": "https://www.cqc.org.uk/provider/RXA"}
        ],
        "related": ["Cheshire and Wirral Partnership NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "NHS Property Services Ltd", "Lease expenditure — Mersey Care NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Amortisation — Rotherham Doncaster and South Humber NHS Foundation Trust": {
        "aliases": [{"name": "Amortisation", "parent": "Rotherham Doncaster and South Humber NHS Foundation Trust"}],
        "description": "RDaSH's £0.53M amortisation charge represents the IAS 38-prescribed straight-line write-down of capitalised intangible assets — predominantly EPR / clinical software, capitalised internally-developed digital systems, training-cost capitalisation under the Frontline Digitisation programme and licence agreements. The line covers software and intangibles deployed across the trust's MH, LD and community-physical-health footprint serving Rotherham, Doncaster, North Lincolnshire and parts of Bassetlaw.",
        "beneficiaries": "c. 3,800 staff and a registered catchment of c. 750,000 across Rotherham, Doncaster and North Lincolnshire (plus Bassetlaw community); EPR + clinical-system rollouts deliver to c. 4,000 clinical end-users across MH, LD and community pathways.",
        "legal_basis": "IAS 38 Intangible Assets · DHSC Group Accounting Manual 2024-25 ch.5 · NHS Act 2006 · Health and Care Act 2022 · NHSE Frontline Digitisation programme · IAS 36 Impairment of Assets",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£0.53M"},
            {"label": "Composition", "value": "EPR / clinical software amortisation + capitalised internally-developed systems + training-cost capitalisation under FD + licence agreements"},
            {"label": "Useful-life convention", "value": "Software typically 3-5 years SL; bespoke clinical-system development up to 7-10 years where supportable per DHSC GAM ch.5"},
            {"label": "Frontline Digitisation context", "value": "NHSE FD programme funds EPR rollouts to MH-trust sector — capital-then-amortisation profile post-go-live"},
            {"label": "Major intangibles", "value": "EPR system + e-prescribing + clinical-portal + ESR HR/payroll module + radiology-PACS / imaging links + cyber-security tooling"},
            {"label": "Capitalisation threshold", "value": "DHSC GAM 2024-25 capitalisation threshold £5,000 per item; bespoke software capitalised where IAS 38 development-phase criteria met"},
            {"label": "Funding trajectory", "value": "2020-21 c. £0.3M → 2022-23 c. £0.4M → 2024-25 £0.53M — sustained uplift driven by FD-funded EPR amortisation onset"},
            {"label": "Delivery body", "value": "Trust Digital + Finance teams + EPR vendor + NHSE Frontline Digitisation programme office"},
            {"label": "Policy owner", "value": "DHSC + NHSE Transformation Directorate (FD) + South Yorkshire ICB / Humber and North Yorkshire ICB"},
            {"label": "Evaluation evidence", "value": "Trust ARA 2023-24 intangibles note; NHSE FD programme reports; CQC RXE provider profile; SY ICS digital strategy"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-FD legacy patient-administration systems (RiO / IAPTus / locally-built) · Successor: post-rollout steady-state amortisation + cyber-security capitalisation pipeline"}
        ],
        "notes": "RDaSH's amortisation line has grown materially since 2022-23 as Frontline Digitisation EPR rollout costs began amortising post-go-live. The trust's combined MH + LD + community physical-health remit means the EPR rollout footprint extends beyond pure-MH systems to community-nursing, podiatry and integrated-care workflows, raising the capitalisation base above pure-MH peers of comparable headcount. NHSE Transformation Directorate's Frontline Digitisation programme is the dominant policy and funding lever, providing capital grants that subsequently feed the trust's amortisation line over the 3-7 year useful-life period. South Yorkshire ICS digital strategy and the Humber and North Yorkshire ICS digital strategy frame the medium-term roadmap.",
        "sources": [
            {"publisher": "Rotherham Doncaster and South Humber NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.rdash.nhs.uk/about-us/publications/annual-report/"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/connecteddigitalsystems/digitisation/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 5 — Intangible Assets)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "RDaSH provider profile (RXE)", "url": "https://www.cqc.org.uk/provider/RXE"},
            {"publisher": "South Yorkshire Integrated Care Board", "title": "South Yorkshire digital strategy", "url": "https://syics.co.uk/"}
        ],
        "related": ["Rotherham Doncaster and South Humber NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "NHS England", "Amortisation — Oxford Health NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Business rates — Bradford District Care NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "Bradford District Care NHS Foundation Trust"}],
        "description": "BDCFT's £0.52M business-rates charge reflects VOA-set rateable values × 49.9p UBR (small) / 54.6p (standard) on the trust's occupied estate — the Lynfield Mount Hospital (Bradford), Airedale Centre for Mental Health, c. 25+ community-MH, CAMHS, LD and community-physical-health bases across Bradford, Airedale, Wharfedale and Craven, plus the trust's children's-community-services footprint. NHS FTs do not get charitable exemption; the line is rebased at each VOA revaluation cycle.",
        "beneficiaries": "Approximately 25+ occupied hereditaments (acute MH wards, community clinics, CAMHS sites, LD bases, children's community-services bases) across Bradford, Airedale, Wharfedale and Craven; serves a registered catchment c. 600,000.",
        "legal_basis": "Local Government Finance Act 1988 (Schedule 6 valuation) · Non-Domestic Rating (Multipliers and Private Finance) Act 2024 · Non-Domestic Rating Act 2023 · NHS Act 2006 · Health and Care Act 2022 · DHSC GAM 2024-25",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£0.52M"},
            {"label": "Hereditament count", "value": "c. 25+ occupied sites across Bradford, Airedale, Wharfedale + Craven"},
            {"label": "Major rated sites", "value": "Lynfield Mount Hospital (Bradford) + Airedale Centre for Mental Health + community + children's-services bases"},
            {"label": "UBR 2024-25", "value": "49.9p small-multiplier / 54.6p standard-multiplier — frozen at 2023-24 levels under Autumn Statement 2023"},
            {"label": "Charitable exemption", "value": "Not applicable — NHS FTs are not registered charities under Charities Act 2011"},
            {"label": "Billing authorities", "value": "City of Bradford MDC + Craven DC (now part of North Yorkshire Council from Apr 2023) + parts of Leeds CC where overlapping community services"},
            {"label": "VOA 2023 revaluation impact", "value": "Mixed urban Bradford + rural Craven / Wharfedale community clinics; net broadly neutral post-pandemic; Lynfield Mount carries higher £/m² RV as specialised inpatient facility"},
            {"label": "NHSPS interaction", "value": "Some community clinic estate held via NHSPS lease; rates passed through to BDCFT as occupier"},
            {"label": "Combined MH + community footprint driver", "value": "BDCFT delivers MH + community-physical-health + children's-community — wider hereditament list than pure-MH peers"},
            {"label": "Funding trajectory", "value": "2020-21 c. £0.4M → 2024-25 £0.52M — tracks frozen UBR + new-site additions + community-services hereditament base"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + VOA + 2-3 billing authorities"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2017 antecedent valuation date list · Successor: 2026 next revaluation (3-year cycle under NDRA 2023)"}
        ],
        "notes": "BDCFT's business-rates line is structurally inflated by the trust's combined MH + community-physical-health + children's-community remit — Lynfield Mount Hospital (Bradford) and the Airedale Centre for Mental Health are the two largest specialist hereditaments, but the c. 20+ community-services bases (including children's community sites and community-nursing offices) push the total above pure-MH peers of comparable headcount. The Autumn Statement 2023 UBR freeze gave a one-year reprieve, but the 2026 revaluation under NDRA 2023's 3-year cycle is expected to rebase upward. North Yorkshire Council unitary reorganisation (April 2023) absorbed Craven DC, simplifying the billing-authority picture in the rural northern footprint. NHSPS-leased community clinics pass rates through to BDCFT under occupier-rule.",
        "sources": [
            {"publisher": "Bradford District Care NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.bdct.nhs.uk/about-us/publications/"},
            {"publisher": "Valuation Office Agency", "title": "Find a business rates valuation (NHS hereditaments)", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "Department for Levelling Up, Housing and Communities", "title": "Business rates — multipliers and reliefs 2024-25", "url": "https://www.gov.uk/introduction-to-business-rates"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "BDCFT provider profile (RT5 — note Bradford differs)", "url": "https://www.cqc.org.uk/provider/RT5BD"}
        ],
        "related": ["Bradford District Care NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Valuation Office Agency", "Business rates — Coventry and Warwickshire Partnership NHS Trust", "Department of Health and Social Care"]
    },
    "PFI / LIFT charges — Bradford District Care NHS Foundation Trust": {
        "aliases": [{"name": "PFI / LIFT charges", "parent": "Bradford District Care NHS Foundation Trust"}],
        "description": "BDCFT's £0.52M PFI / LIFT charge reflects the trust's occupation of LIFT-procured community-MH and integrated-care bases across Bradford under the Bradford LIFT vehicle (Community Health Partnerships shareholding + private partners + LA co-investment). The line covers the unitary-charge pass-through — debt service, FM lifecycle and soft-FM components — for those LIFT premises hosting MH community teams, CAMHS and children's-community-services bases.",
        "beneficiaries": "c. 3,000 staff and a registered catchment of c. 600,000 across Bradford, Airedale, Wharfedale and Craven; LIFT-procured estate hosts community-MH team bases, CAMHS, children's-community and integrated primary-care-co-located bases.",
        "legal_basis": "IFRS 16 Leases (post-2022 transition for finance-lease + service-concession arrangements) · IFRIC 12 Service Concession Arrangements · DHSC Group Accounting Manual 2024-25 ch.7 · NHS (Local Improvement Finance Trust) regulations · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "PFI / LIFT charges 2024-25", "value": "£0.52M"},
            {"label": "Procurement vehicle", "value": "Bradford LIFT — CHP shareholding + private investor + LA partnership"},
            {"label": "Estate covered", "value": "Community-MH team bases + CAMHS + children's-community + integrated primary-care-co-located bases"},
            {"label": "Unitary charge composition", "value": "Debt-service component + lifecycle (hard-FM building maintenance) + soft-FM (cleaning, security, catering where contracted)"},
            {"label": "Contract duration profile", "value": "LIFT contracts typically 25-year initial with extension option; Bradford LIFT signed mid-2000s — c. 8-12 years remaining"},
            {"label": "IFRS 16 / IFRIC 12 treatment", "value": "Service-concession assets recognised on-balance-sheet under IFRIC 12; lease-component re-evaluated under IFRS 16 ch.7 GAM"},
            {"label": "Lifecycle indexation", "value": "Annual RPI / CPI indexation per LIFT contract terms — material driver of year-on-year line movement"},
            {"label": "Combined MH + community + children's footprint", "value": "Trust delivers MH + community-physical-health + children's-community — wider LIFT-base utilisation than pure-MH peers"},
            {"label": "Funding trajectory", "value": "2020-21 c. £0.4M → 2024-25 £0.52M — sustained CPI-linked uplift"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + Community Health Partnerships + private LIFT investor consortium"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + West Yorkshire ICB; LIFT policy oversight at DHSC"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-LIFT mid-2000s NHS-Estates community-clinic model · Successor: end-of-LIFT-contract review + ICS estate consolidation early 2030s"}
        ],
        "notes": "BDCFT's PFI / LIFT line is dominated by the Bradford LIFT vehicle, which procured community-health bases in the mid-2000s under the Local Improvement Finance Trust model — service-concession structures where Community Health Partnerships (DHSC majority shareholder) co-invests with private partners and local-authority partners, and the trust occupies as tenant under unitary-charge contracts. The trust's combined MH + community-physical-health + children's-community remit means LIFT-base utilisation extends across more service lines than pure-MH peers. CPI / RPI indexation is the main driver of cost growth, layered on fixed debt-service and lifecycle components. As LIFT contracts approach their 25-year endpoint in the early 2030s, West Yorkshire ICS faces strategic hand-back / extension / consolidation decisions.",
        "sources": [
            {"publisher": "Bradford District Care NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.bdct.nhs.uk/about-us/publications/"},
            {"publisher": "Community Health Partnerships", "title": "LIFT estate annual review", "url": "https://www.communityhealthpartnerships.co.uk/"},
            {"publisher": "National Audit Office", "title": "PFI and PF2 / LIFT review", "url": "https://www.nao.org.uk/reports/pfi-and-pf2/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 7 — Leases and service concessions)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "West Yorkshire Integrated Care Board", "title": "West Yorkshire ICS estate strategy", "url": "https://www.wypartnership.co.uk/"}
        ],
        "related": ["Bradford District Care NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Community Health Partnerships", "PFI / LIFT charges — Leicestershire Partnership NHS Trust", "Department of Health and Social Care"]
    },
    "Lease expenditure — Coventry and Warwickshire Partnership NHS Trust": {
        "aliases": [{"name": "Lease expenditure", "parent": "Coventry and Warwickshire Partnership NHS Trust"}],
        "description": "CWPT's £0.46M lease expenditure reflects IFRS 16 right-of-use depreciation + interest charges on the trust's leased estate following the 2022 on-balance-sheet transition. The portfolio is dominated by NHS Property Services-leased community-MH and CAMHS premises across Coventry, Warwickshire and Solihull, plus Community Health Partnerships LIFT vehicles for primary-care-co-located bases — c. 30+ leased community sites support the trust's MH + LD + community-children's footprint alongside the Caludon Centre and Brooklands inpatient anchors (which sit outside the lease line as owned/freehold).",
        "beneficiaries": "c. 4,500 staff and a registered catchment of c. 1.05M across Coventry, Warwickshire and Solihull (plus regional secure-LD catchment); leased component covers c. 30+ community-MH, CAMHS, LD, children's and addictions bases.",
        "legal_basis": "IFRS 16 Leases · DHSC Group Accounting Manual 2024-25 ch.7 · Landlord and Tenant Act 1954 · NHS Act 2006 · Health and Care Act 2022 · IFRIC 12 Service Concession Arrangements (LIFT lease-components)",
        "key_stats": [
            {"label": "Lease expenditure 2024-25", "value": "£0.46M"},
            {"label": "IFRS 16 transition jump", "value": "2022 on-balance-sheet adoption — operating leases reclassified to ROU asset + lease liability with depreciation + interest split"},
            {"label": "Leased site count", "value": "c. 30+ NHSPS + CHP-LIFT community-MH, CAMHS, LD, children's and addictions bases"},
            {"label": "Major lessor", "value": "NHS Property Services Ltd (majority) + Community Health Partnerships (LIFT) + private landlords"},
            {"label": "Inpatient anchor sites (owned/freehold)", "value": "Caludon Centre (Coventry, c. 130 acute MH beds) + Brooklands (Marston Green, secure-LD) — owned/freehold, not in lease line"},
            {"label": "NHSPS rates dispute", "value": "Sustained NHSPS / MH-trust dispute on community-clinic market-rent uplift + service-charge methodology — feeds annual lease-cost volatility"},
            {"label": "Discount rate applied", "value": "HM Treasury PES discount rate per DHSC GAM 2024-25 ch.7 — recalibrated annually"},
            {"label": "Lease term profile", "value": "Mix of 5-year + 10-year community clinic leases; longer-term LIFT contracts to 25+ years"},
            {"label": "Funding trajectory", "value": "2021-22 (pre-IFRS16) c. £0.25M operating lease → 2022-23 c. £0.4M ROU first year → 2024-25 £0.46M"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + NHSPS + CHP for LIFT vehicles"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + Coventry and Warwickshire ICB · IFRS 16 / DHSC GAM ch.7 oversight"},
            {"label": "Evaluation evidence", "value": "Trust ARA 2023-24 disclosure; CQC inspection reports (RYG); CW ICS estate strategy"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2022 IAS 17 operating-lease expense · Successor: NHSPS market-rent reform + CW ICS estate consolidation"}
        ],
        "notes": "CWPT's lease line jumped at the IFRS 16 2022 transition as previously off-balance-sheet operating leases moved on-balance-sheet, and has continued to grow as NHS Property Services pursued market-rent uplifts on community clinics. The trust's combined MH + LD + community-children's remit drives a wider community-base footprint than pure-MH peers. Brooklands Hospital regional secure-LD inpatient resource at Marston Green and the Caludon Centre acute-MH unit sit outside the lease line as owned/freehold estate. NHSPS-leased community clinics across Coventry, Warwickshire and Solihull pass service-charge friction through to the trust as tenant. CW ICS estate consolidation under the long-term plan is the medium-term lever to flatten cost growth.",
        "sources": [
            {"publisher": "Coventry and Warwickshire Partnership NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.covwarkpt.nhs.uk/publications"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 7 — Leases)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS Property Services", "title": "Annual Report 2023-24 + market-rent methodology", "url": "https://www.property.nhs.uk/about/our-publications/"},
            {"publisher": "Community Health Partnerships", "title": "LIFT estate annual review", "url": "https://www.communityhealthpartnerships.co.uk/"},
            {"publisher": "Care Quality Commission", "title": "CWPT provider profile (RYG)", "url": "https://www.cqc.org.uk/provider/RYG"}
        ],
        "related": ["Coventry and Warwickshire Partnership NHS Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "NHS Property Services Ltd", "Lease expenditure — Birmingham and Solihull Mental Health NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Lease expenditure — Devon Partnership NHS Trust": {
        "aliases": [{"name": "Lease expenditure", "parent": "Devon Partnership NHS Trust"}],
        "description": "DPT's £0.43M lease expenditure reflects IFRS 16 right-of-use depreciation + interest charges on the trust's leased estate following the 2022 on-balance-sheet transition. The portfolio is dominated by NHS Property Services-leased community-MH and CAMHS premises across the city of Exeter, Plymouth (community-MH catchment), Torbay-adjacent areas and rural Devon (East Devon, Mid Devon, North Devon, Teignbridge, West Devon, South Hams). The dispersed-rural geography drives a higher site count for a relatively modest turnover.",
        "beneficiaries": "c. 3,300 staff and a registered catchment of c. 850,000 across Devon (excluding Plymouth and Torbay acute MH); leased component covers c. 25+ community-MH, CAMHS, EIP, recovery-college and crisis-team bases dispersed across Devon.",
        "legal_basis": "IFRS 16 Leases · DHSC Group Accounting Manual 2024-25 ch.7 · Landlord and Tenant Act 1954 · NHS Act 2006 · Health and Care Act 2022 · IFRIC 12 Service Concession Arrangements (LIFT lease-components where applicable)",
        "key_stats": [
            {"label": "Lease expenditure 2024-25", "value": "£0.43M"},
            {"label": "IFRS 16 transition jump", "value": "2022 on-balance-sheet adoption — operating leases reclassified to ROU asset + lease liability with depreciation + interest split"},
            {"label": "Leased site count", "value": "c. 25+ NHSPS + private-landlord community-MH, CAMHS, EIP and crisis-team bases dispersed across Devon"},
            {"label": "Major lessor", "value": "NHS Property Services Ltd (majority) + Community Health Partnerships + private landlords"},
            {"label": "Inpatient anchor sites (owned/freehold)", "value": "Wonford House (Exeter, acute-MH) + Langdon Hospital (Dawlish, secure-services) — owned/freehold, not in lease line"},
            {"label": "Rural geography premium", "value": "Dispersed Devon footprint (East/Mid/North/West Devon + South Hams) drives higher per-WTE site count than urban-trust peers"},
            {"label": "NHSPS rates dispute", "value": "Sustained NHSPS / MH-trust dispute on community-clinic market-rent uplift + service-charge methodology"},
            {"label": "Discount rate applied", "value": "HM Treasury PES discount rate per DHSC GAM 2024-25 ch.7 — recalibrated annually"},
            {"label": "Funding trajectory", "value": "2021-22 (pre-IFRS16) c. £0.2M operating lease → 2022-23 c. £0.35M ROU first year → 2024-25 £0.43M"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + NHSPS"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + Devon ICB · IFRS 16 / DHSC GAM ch.7 oversight"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2022 IAS 17 operating-lease expense · Successor: NHSPS market-rent reform + Devon ICS estate consolidation"}
        ],
        "notes": "DPT's lease line jumped at the IFRS 16 2022 transition as previously off-balance-sheet operating leases moved on-balance-sheet. The trust's dispersed-rural Devon geography means it sustains a relatively wide community-base footprint (c. 25+ leased sites) for a modest turnover, exposing it to NHSPS service-charge volatility on each clinic. Wonford House (Exeter) and Langdon Hospital (Dawlish) inpatient anchors sit outside the lease line as owned/freehold estate — the lease line is wholly community + administrative. Devon ICS estate consolidation and the ongoing Wonford House redevelopment scoping are the medium-term levers; the rural geography limits the consolidation upside compared with urban-trust peers.",
        "sources": [
            {"publisher": "Devon Partnership NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.dpt.nhs.uk/about-us/publications/annual-reports"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 7 — Leases)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS Property Services", "title": "Annual Report 2023-24 + market-rent methodology", "url": "https://www.property.nhs.uk/about/our-publications/"},
            {"publisher": "Care Quality Commission", "title": "Devon Partnership NHS Trust provider profile (RWV)", "url": "https://www.cqc.org.uk/provider/RWV"},
            {"publisher": "Devon Integrated Care Board", "title": "Devon ICS estate strategy", "url": "https://onedevon.org.uk/"}
        ],
        "related": ["Devon Partnership NHS Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "NHS Property Services Ltd", "Lease expenditure — Cornwall Partnership NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Termination & post-employment — Southern Health NHS Foundation Trust": {
        "aliases": [{"name": "Termination & post-employment", "parent": "Southern Health NHS Foundation Trust"}],
        "description": "Southern Health's £0.43M termination + post-employment line covers one-off severance, contractual notice pay-in-lieu, redundancy and the NHS Pension Scheme employer-element on early-retirement and exit packages across the trust's c. 6,500-staff base. The trust's high-profile governance history — the 2015 Mazars review of unexpected deaths (including Connor Sparrowhawk) and the long-running Hampshire community-MH service redesigns — has driven elevated senior-leadership turnover and remediation-related exits across the past decade.",
        "beneficiaries": "c. 6,500 staff covering MH, LD and community-physical-health services across Hampshire (excluding Portsmouth) and parts of Wiltshire; redundancy + exit-package pool of c. 20-50 individuals per year on average, scaled to remediation cycles and senior-leadership turnover.",
        "legal_basis": "IAS 19 Employee Benefits · NHS Pension Scheme regulations · Public Sector Exit Payments Regulations 2020 (uncapped post-2021 quash) · Employment Rights Act 1996 (s.139 redundancy + s.86 statutory notice) · DHSC Group Accounting Manual 2024-25 · NHS Act 2006",
        "key_stats": [
            {"label": "Termination & post-employment 2024-25", "value": "£0.43M"},
            {"label": "Headcount + exit-pool context", "value": "c. 6,500 substantive WTE; estimated 20-50 exit packages annually"},
            {"label": "Composition", "value": "Statutory + contractual redundancy + pay-in-lieu of notice + NHS Pension Scheme employer-element on early retirement + senior-staff exit packages"},
            {"label": "Mazars review legacy", "value": "Dec 2015 Mazars review of unexpected deaths in MH/LD services — Connor Sparrowhawk case driver — triggered sustained governance + leadership-turnover cycles"},
            {"label": "Service redesign context", "value": "Hampshire community-MH redesign + LD-service reconfiguration drove repeated senior-team restructures"},
            {"label": "April 2025 NIC step-up", "value": "Employer NIC threshold drop + rate rise (Apr 2025) raises NHS Pension Scheme employer-cost on exit packages forward"},
            {"label": "PSE Payments Regs 2020", "value": "Capped exit-payment regs revoked 2021; trust currently operates under HM Treasury non-statutory guidance + NHS England consent rules"},
            {"label": "Funding trajectory", "value": "Variable year-on-year; 2020-21 elevated through MH-community redesign; 2024-25 £0.43M"},
            {"label": "Delivery body", "value": "Trust HR + Finance teams + NHS Business Services Authority (Pensions) + NHSE consent for senior packages"},
            {"label": "Policy owner", "value": "DHSC + NHSE Workforce + HM Treasury (exit-pay guidance) + Hampshire and Isle of Wight ICB"},
            {"label": "Evaluation evidence", "value": "Mazars 2015 review; NHSE Special Measures designation + exit; CQC inspection reports (RW1); Trust ARA workforce remuneration report"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2021 capped PSE payments regime · Successor: HMT non-statutory exit-pay guidance + NIC step-up Apr 2025"}
        ],
        "notes": "Southern Health's termination line carries the long shadow of the Mazars review, which in December 2015 examined unexpected deaths in MH/LD services and was prompted in part by the death of Connor Sparrowhawk in 2013 — a case that became a national reference point for LD-service safety. The cumulative governance fallout drove repeated senior-leadership exits, NHSE Special Measures designation, and a decade-long remediation programme that periodically inflates this line. Hampshire community-MH redesign and the ongoing LD-service reconfiguration generate routine restructuring-related exits. The April 2025 employer-NIC step-up will raise forward NHS Pension Scheme employer-cost on subsequent exit packages.",
        "sources": [
            {"publisher": "Southern Health NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.southernhealth.nhs.uk/about/publications/"},
            {"publisher": "Mazars LLP / NHS England", "title": "Independent review of deaths of people with a learning disability or mental health problem in contact with Southern Health (2015)", "url": "https://www.england.nhs.uk/south/wp-content/uploads/sites/6/2015/12/mazars-rep.pdf"},
            {"publisher": "NHS Business Services Authority", "title": "NHS Pension Scheme employer guidance", "url": "https://www.nhsbsa.nhs.uk/employer-hub"},
            {"publisher": "HM Treasury", "title": "Guidance on public sector exit payments", "url": "https://www.gov.uk/government/publications/public-sector-exit-payments-guidance"},
            {"publisher": "Care Quality Commission", "title": "Southern Health provider profile (RW1)", "url": "https://www.cqc.org.uk/provider/RW1"}
        ],
        "related": ["Southern Health NHS Foundation Trust", "Staff Costs", "NHS Mental Health Trusts", "NHS Pension Scheme", "Termination & post-employment — Nottinghamshire Healthcare NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Amortisation — Barnet, Enfield And Haringey Mental Health NHS Trust": {
        "aliases": [{"name": "Amortisation", "parent": "Barnet, Enfield And Haringey Mental Health NHS Trust"}],
        "description": "BEH-MHT's £0.41M amortisation charge represents the IAS 38-prescribed straight-line write-down of capitalised intangible assets — predominantly EPR / clinical software, capitalised internally-developed digital systems, training-cost capitalisation under the Frontline Digitisation programme and licence agreements. The line covers software and intangibles deployed across the trust's MH footprint serving Barnet, Enfield and Haringey, plus the North London Forensic Service hosted at Chase Farm Hospital.",
        "beneficiaries": "c. 2,800 staff and a registered catchment of c. 1.0M across the three north London boroughs of Barnet, Enfield and Haringey, plus regional forensic catchment via the North London Forensic Service; EPR + clinical-system rollouts deliver to c. 3,000 clinical end-users.",
        "legal_basis": "IAS 38 Intangible Assets · DHSC Group Accounting Manual 2024-25 ch.5 · NHS Act 2006 · Health and Care Act 2022 · NHSE Frontline Digitisation programme · IAS 36 Impairment of Assets",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£0.41M"},
            {"label": "Composition", "value": "EPR / clinical software amortisation + capitalised internally-developed systems + training-cost capitalisation under FD + licence agreements"},
            {"label": "Useful-life convention", "value": "Software typically 3-5 years SL; bespoke clinical-system development up to 7-10 years where supportable per DHSC GAM ch.5"},
            {"label": "Frontline Digitisation context", "value": "NHSE FD programme funds EPR rollouts to MH-trust sector — capital-then-amortisation profile post-go-live"},
            {"label": "Major intangibles", "value": "EPR system + e-prescribing + clinical-portal + ESR HR/payroll module + cyber-security tooling"},
            {"label": "Capitalisation threshold", "value": "DHSC GAM 2024-25 capitalisation threshold £5,000 per item; bespoke software capitalised where IAS 38 development-phase criteria met"},
            {"label": "North London merger context", "value": "Apr 2024 merger with Camden and Islington NHS FT to form North London NHS Foundation Trust — successor entity inherits intangibles + amortisation tail"},
            {"label": "Funding trajectory", "value": "2020-21 c. £0.2M → 2022-23 c. £0.3M → 2024-25 £0.41M — sustained uplift driven by FD-funded EPR amortisation onset"},
            {"label": "Delivery body", "value": "Trust Digital + Finance teams + EPR vendor + NHSE Frontline Digitisation programme office"},
            {"label": "Policy owner", "value": "DHSC + NHSE Transformation Directorate (FD) + North Central London ICB"},
            {"label": "Evaluation evidence", "value": "Trust ARA 2023-24 intangibles note; NHSE FD programme reports; CQC RRP provider profile; NCL ICS digital strategy"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-FD legacy patient-administration systems · Successor: North London NHS FT (post-merger Apr 2024) inherits intangibles + amortisation tail"}
        ],
        "notes": "BEH-MHT's amortisation line has grown materially since 2022-23 as Frontline Digitisation EPR rollout costs began amortising post-go-live. The trust is a transitional entity — in April 2024 it merged with Camden and Islington NHS Foundation Trust to form the North London NHS Foundation Trust under the NCL ICS strategy; the 2024-25 charge is therefore the final standalone amortisation line, with the successor entity inheriting the intangibles register and amortisation tail. NHSE Transformation Directorate's Frontline Digitisation programme is the dominant policy and funding lever, providing capital grants that subsequently feed amortisation over the 3-7 year useful-life period. North London Forensic Service intangibles add a specialist software layer.",
        "sources": [
            {"publisher": "Barnet, Enfield and Haringey Mental Health NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.beh-mht.nhs.uk/about-us/our-publications/"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/connecteddigitalsystems/digitisation/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 5 — Intangible Assets)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "North Central London Integrated Care Board", "title": "NCL ICS digital strategy + BEH/C&I merger framework", "url": "https://nclhealthandcare.org.uk/"},
            {"publisher": "Care Quality Commission", "title": "BEH-MHT provider profile (RRP)", "url": "https://www.cqc.org.uk/provider/RRP"}
        ],
        "related": ["Barnet, Enfield And Haringey Mental Health NHS Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "NHS England", "Amortisation — Rotherham Doncaster and South Humber NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "PFI / LIFT charges — Black Country Healthcare NHS Foundation Trust": {
        "aliases": [{"name": "PFI / LIFT charges", "parent": "Black Country Healthcare NHS Foundation Trust"}],
        "description": "BCHFT's £0.41M PFI / LIFT charge reflects the trust's occupation of LIFT-procured community-MH and integrated-care bases across Dudley, Sandwell, Walsall and Wolverhampton under the Black Country LIFT vehicles (Community Health Partnerships shareholding + private partners + LA co-investment). The line covers the unitary-charge pass-through — debt service, FM lifecycle and soft-FM components — for those LIFT premises hosting MH community teams, CAMHS, addictions and primary-care-co-located bases.",
        "beneficiaries": "c. 4,000 staff and a registered catchment of c. 1.2M across Dudley, Sandwell, Walsall and Wolverhampton (the four Black Country boroughs); LIFT-procured estate hosts community-MH team bases, CAMHS, addictions and integrated primary-care-co-located bases.",
        "legal_basis": "IFRS 16 Leases (post-2022 transition for finance-lease + service-concession arrangements) · IFRIC 12 Service Concession Arrangements · DHSC Group Accounting Manual 2024-25 ch.7 · NHS (Local Improvement Finance Trust) regulations · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "PFI / LIFT charges 2024-25", "value": "£0.41M"},
            {"label": "Procurement vehicle", "value": "Black Country LIFT vehicles — CHP shareholding + private investor + LA partnership across Dudley + Sandwell + Walsall + Wolverhampton"},
            {"label": "Estate covered", "value": "Community-MH team bases + CAMHS + addictions + integrated primary-care-co-located bases"},
            {"label": "Unitary charge composition", "value": "Debt-service component + lifecycle (hard-FM building maintenance) + soft-FM (cleaning, security, catering where contracted)"},
            {"label": "Contract duration profile", "value": "LIFT contracts typically 25-year initial with extension option; Black Country LIFTs signed mid-2000s — c. 8-12 years remaining"},
            {"label": "IFRS 16 / IFRIC 12 treatment", "value": "Service-concession assets recognised on-balance-sheet under IFRIC 12; lease-component re-evaluated under IFRS 16 ch.7 GAM"},
            {"label": "Lifecycle indexation", "value": "Annual RPI / CPI indexation per LIFT contract terms — material driver of year-on-year line movement"},
            {"label": "Trust-merger context", "value": "BCHFT formed Apr 2020 from merger of Black Country Partnership NHS FT + Dudley & Walsall MH Partnership NHS Trust — consolidated multiple LIFT exposures"},
            {"label": "Funding trajectory", "value": "2020-21 c. £0.3M (post-merger baseline) → 2024-25 £0.41M — sustained CPI-linked uplift"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + Community Health Partnerships + private LIFT investor consortium"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + Black Country ICB; LIFT policy oversight at DHSC"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-merger Black Country Partnership + Dudley & Walsall MH Partnership LIFT exposures · Successor: end-of-LIFT-contract review + Black Country ICS estate consolidation early 2030s"}
        ],
        "notes": "BCHFT's PFI / LIFT line consolidates the LIFT exposures inherited from the April 2020 merger of Black Country Partnership NHS FT and Dudley & Walsall Mental Health Partnership NHS Trust, which between them occupied LIFT-procured community-health bases across all four Black Country boroughs. CPI / RPI indexation is the main driver of year-on-year cost growth, layered on fixed debt-service and lifecycle components. As LIFT contracts approach their 25-year endpoint in the early 2030s, Black Country ICS faces strategic hand-back / extension / consolidation decisions across the inherited portfolio. The Penn Hospital (Wolverhampton), Hallam Street Hospital (West Bromwich) and Edward Street Hospital inpatient anchors sit outside the LIFT line as owned/freehold estate.",
        "sources": [
            {"publisher": "Black Country Healthcare NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.blackcountryhealthcare.nhs.uk/about-us/publications/"},
            {"publisher": "Community Health Partnerships", "title": "LIFT estate annual review", "url": "https://www.communityhealthpartnerships.co.uk/"},
            {"publisher": "National Audit Office", "title": "PFI and PF2 / LIFT review", "url": "https://www.nao.org.uk/reports/pfi-and-pf2/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 7 — Leases and service concessions)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "BCHFT provider profile (RYK)", "url": "https://www.cqc.org.uk/provider/RYK"}
        ],
        "related": ["Black Country Healthcare NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Community Health Partnerships", "PFI / LIFT charges — Bradford District Care NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Business rates — North Staffordshire Combined Healthcare NHS Trust": {
        "aliases": [{"name": "Business rates", "parent": "North Staffordshire Combined Healthcare NHS Trust"}],
        "description": "Combined Healthcare's £0.41M business-rates charge reflects VOA-set rateable values × 49.9p UBR (small) / 54.6p (standard) on the trust's occupied estate — the Harplands Hospital (Stoke, c. 121 acute MH beds) anchor site plus c. 25+ community-MH, CAMHS, addictions and LD bases serving the city of Stoke-on-Trent and the Staffordshire Moorlands and Newcastle-under-Lyme districts. NHS Trusts do not get charitable exemption; the line is rebased at each VOA revaluation cycle.",
        "beneficiaries": "Approximately 25+ occupied hereditaments (Harplands Hospital + community clinics + CAMHS sites + addictions bases + LD bases) across Stoke-on-Trent, Newcastle-under-Lyme and the Staffordshire Moorlands; serves a registered catchment of c. 470,000.",
        "legal_basis": "Local Government Finance Act 1988 (Schedule 6 valuation) · Non-Domestic Rating (Multipliers and Private Finance) Act 2024 · Non-Domestic Rating Act 2023 · NHS Act 2006 · Health and Care Act 2022 · DHSC GAM 2024-25",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£0.41M"},
            {"label": "Hereditament count", "value": "c. 25+ occupied sites across Stoke-on-Trent + Newcastle-under-Lyme + Staffordshire Moorlands"},
            {"label": "Major rated sites", "value": "Harplands Hospital (Stoke, c. 121 beds) + Lawton House (CAMHS) + community bases"},
            {"label": "UBR 2024-25", "value": "49.9p small-multiplier / 54.6p standard-multiplier — frozen at 2023-24 levels under Autumn Statement 2023"},
            {"label": "Charitable exemption", "value": "Not applicable — NHS Trusts are not registered charities under Charities Act 2011"},
            {"label": "Billing authorities", "value": "Stoke-on-Trent City Council + Newcastle-under-Lyme BC + Staffordshire Moorlands DC"},
            {"label": "VOA 2023 revaluation impact", "value": "Mixed urban Stoke + rural Moorlands community clinics; net broadly neutral; Harplands carries higher £/m² RV as specialised inpatient facility"},
            {"label": "NHSPS interaction", "value": "Some community clinic estate held via NHSPS lease; rates passed through to trust as occupier"},
            {"label": "Funding trajectory", "value": "2020-21 c. £0.3M → 2024-25 £0.41M — tracks frozen UBR + new-site additions"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + VOA + 3 billing authorities"},
            {"label": "Policy owner", "value": "DHSC + MHCLG (business rates policy) + NHSE Provider Finance + Staffordshire and Stoke-on-Trent ICB"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2017 antecedent valuation date list · Successor: 2026 next revaluation (3-year cycle under NDRA 2023)"}
        ],
        "notes": "Combined Healthcare's business-rates line reflects a small-trust footprint where Harplands Hospital (Stoke) is the dominant hereditament and a dispersed community estate of c. 20+ smaller sites generates the residual liability. The Autumn Statement 2023 UBR freeze gave a one-year reprieve, but the 2026 revaluation under NDRA 2023's 3-year cycle is expected to rebase upward. The Staffordshire Moorlands rural component carries lower per-m² RV than Stoke city sites, partially offsetting the cost. NHSPS-leased community clinics pass rates through to the trust under occupier-rule, consistent with the sector-wide service-charge friction. Combined Healthcare's small-trust scale limits negotiating leverage with NHSPS compared with merged peer-trust complexes.",
        "sources": [
            {"publisher": "North Staffordshire Combined Healthcare NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.combined.nhs.uk/about-us/publications/annual-reports/"},
            {"publisher": "Valuation Office Agency", "title": "Find a business rates valuation (NHS hereditaments)", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "Department for Levelling Up, Housing and Communities", "title": "Business rates — multipliers and reliefs 2024-25", "url": "https://www.gov.uk/introduction-to-business-rates"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Combined Healthcare provider profile (RLY)", "url": "https://www.cqc.org.uk/provider/RLY"}
        ],
        "related": ["North Staffordshire Combined Healthcare NHS Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Valuation Office Agency", "Business rates — Coventry and Warwickshire Partnership NHS Trust", "Department of Health and Social Care"]
    },
}
