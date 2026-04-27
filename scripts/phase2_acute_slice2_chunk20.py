# -*- coding: utf-8 -*-
# Phase 2 Acute slice 2 — chunk 20 (17 NHS Acute Trust orphan sub-lines)
# Hand-curated trust-specific PROGRAMME-archetype enrichment entries.
# Structural contract per docs/archetype_briefs.md.

NEW = {
    "Establishment costs — Sherwood Forest Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "Sherwood Forest Hospitals NHS Foundation Trust"}],
        "description": "Sherwood Forest's £3.94M establishment costs line covers postage, telephony, printing, stationery, recruitment advertising, subscriptions, hospitality and minor sundries across the King's Mill DGH, Newark Hospital and Mansfield Community Hospital sites — the day-to-day non-pay operating overhead outside clinical supplies. The line carries the embedded cost of running back-office functions for a c. 5,000-WTE workforce serving Mid Nottinghamshire, with industrial-action 2023-24 recruitment campaigns and EPR rollout change-comms feeding 2024-25 spend above pre-pandemic baseline.",
        "beneficiaries": "c. 5,000 WTE staff serving a c. 420,000 Mid Nottinghamshire catchment (Mansfield, Newark, Sherwood); c. 130,000 ED attendances/yr at King's Mill ED; c. 60,000 admissions/yr; three-site footprint (King's Mill DGH c. 460 beds + Newark Hospital + Mansfield Community Hospital).",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) — IAS 1 Presentation of Financial Statements — NHS Act 2006 — Health and Care Act 2022 — NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£3.94M"},
            {"label": "Trust scale", "value": "Three-site (King's Mill DGH + Newark Hospital + Mansfield Community Hospital); c. 5,000 WTE"},
            {"label": "Composition", "value": "Postage, telephony/mobile, printing, stationery, recruitment advertising, subscriptions, hospitality, minor sundries"},
            {"label": "PFI estate context", "value": "King's Mill PFI 2005-2043 — high unitary-charge environment shapes back-office overhead allocation"},
            {"label": "Industrial action 2023-24", "value": "Junior-doctor 44 days + consultant 10 days strikes drove recruitment-advertising spike + comms costs"},
            {"label": "EPR / Frontline Digitisation", "value": "Nervecentre + EPR rollout drives change-mgmt comms, training-materials printing"},
            {"label": "April 2025 NIC + CPI uplift", "value": "Royal Mail + telecoms CPI feed forward unit-cost pressure"},
            {"label": "Funding trajectory", "value": "2021-22 c. £3.0M → 2023-24 c. £3.6M → 2024-25 £3.94M — sustained CPI + activity uplift"},
            {"label": "Delivery body", "value": "Trust Corporate Services + Procurement + IT + (Crown Commercial Service framework for telecoms/postage)"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Nottingham & Nottinghamshire ICB"},
            {"label": "Evaluation evidence", "value": "Model Hospital corporate-services benchmark; CQC RK5 inspections; NAO PFI legacy reports; Trust ARA 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2014 contract-reset baseline · Successor: post-EPR digital-comms shift + 2043 PFI hand-back overhead reset"}
        ],
        "notes": "Sherwood Forest's establishment-costs baseline reflects a three-site Mid Nottinghamshire footprint with the King's Mill PFI (2005-2043) shaping back-office overhead allocation — NAO/PAC-flagged unitary-charge pressure has long pushed the trust to keep non-clinical overheads tight under recurrent affordability scrutiny. Industrial action 2023-24 lifted recruitment-advertising spend through agency-recruitment campaigns and rota-rebuild comms, while EPR rollout (Nervecentre + Frontline Digitisation track) drove change-management printing and digital-training materials. April 2025 employer-NIC step-up sits outside this line but Royal Mail and telecoms CPI feed forward unit-cost pressure into 2025-26.",
        "sources": [
            {"publisher": "Sherwood Forest Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.sfh-tr.nhs.uk/about-us/our-publications/"},
            {"publisher": "National Audit Office", "title": "PFI and PF2 (HC 718, 2018)", "url": "https://www.nao.org.uk/reports/pfi-and-pf2/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Sherwood Forest Hospitals provider profile (RK5)", "url": "https://www.cqc.org.uk/provider/RK5"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme (EPR rollout)", "url": "https://www.england.nhs.uk/digitaltechnology/connecting-health-and-care/frontline-digitisation/"}
        ],
        "related": ["Sherwood Forest Hospitals NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "PFI / LIFT charges — Sherwood Forest Hospitals NHS Foundation Trust", "Establishment costs — Northampton General Hospital NHS Trust", "Department of Health and Social Care"]
    },
    "Transport (business + patient) — Royal Berkshire NHS Foundation Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "Royal Berkshire NHS Foundation Trust"}],
        "description": "Royal Berkshire's £3.94M transport line covers business mileage (AfC Section 17 + AMAP), pool-fleet IFRS 16 lease costs, non-emergency patient transport service (NEPTS) contracts and patient travel reimbursements across the Reading-based DGH and outreach community-clinic footprint serving West Berkshire. NEPTS is commissioned through the Buckinghamshire, Oxfordshire and Berkshire West (BOB) ICS lead-commissioner arrangement, with outsourced provider contracts (historically South Central Ambulance Service NHS FT or contracted private operator) carrying a substantial share of the line.",
        "beneficiaries": "c. 6,500 WTE staff serving a c. 600,000 West Berkshire catchment (Reading, Wokingham, West Berkshire); c. 130,000 ED attendances/yr at Royal Berkshire Hospital ED (London Road site); c. 80,000 admissions/yr; large maternity unit and regional cancer-centre + renal-dialysis NEPTS dependency.",
        "legal_basis": "NHS Act 2006 — NHSE Patient Transport Services Eligibility Criteria — Agenda for Change Section 17 (business mileage) — HMRC AMAP rates — IFRS 16 Leases (pool fleet) — DHSC Group Accounting Manual 2024-25 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£3.94M"},
            {"label": "Trust scale", "value": "Single main acute (Royal Berkshire Hospital, London Road, Reading) + community outreach; c. 6,500 WTE"},
            {"label": "NEPTS commissioning", "value": "BOB ICS lead-commissioner NEPTS contract — outsourced operator delivery; eligibility per NHSE 2021 criteria"},
            {"label": "Composition", "value": "Business mileage (AfC S17 + AMAP 45p/25p) + pool-fleet IFRS 16 leases + NEPTS contract pass-through + patient travel reimbursements"},
            {"label": "AMAP rate context", "value": "HMRC AMAP rate frozen at 45p/mile (first 10k miles) since 2011 — real-terms erosion lifts NHS-internal mileage rate disputes"},
            {"label": "Industrial action 2023-24 effect", "value": "Junior-doctor 44 days + consultant strikes drove agency travel-claim spikes + cancellation rebooking transport"},
            {"label": "April 2025 NIC + fuel CPI", "value": "Indirect via NEPTS contractor pass-through + diesel CPI feed forward unit-cost pressure"},
            {"label": "Funding trajectory", "value": "2021-22 c. £3.2M → 2023-24 c. £3.6M → 2024-25 £3.94M — fuel CPI + NEPTS contract uplift"},
            {"label": "Delivery body", "value": "Trust E&F + outsourced NEPTS provider (BOB ICS lead-commissioner) + pool-fleet leasing partner + Trust HR (mileage)"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + NHSE Urgent and Emergency Care (NEPTS) + BOB ICB + DHSC"},
            {"label": "Evaluation evidence", "value": "NAO NEPTS 2019; CQC RHW inspections; NHSE NEPTS Eligibility Review 2021; Trust ARA 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-ICS CCG-commissioned NEPTS contracts · Successor: post-NHP rebuild new-site transport-flow re-baselining + ICS-collaborative NEPTS retender"}
        ],
        "notes": "Royal Berkshire's transport line carries a high NEPTS-contract share given the regional cancer-centre and renal-dialysis dependency — patients travelling repeated journeys for chemo or dialysis dominate non-emergency volume — with eligibility tightened under NHSE's 2021 criteria refresh. The trust sits in the New Hospital Programme cohort but the January 2025 NHP Reset deferred the planned Reading new-build, sustaining the Royal Berkshire Hospital London Road site and its established community-clinic transport flows. Industrial action 2023-24 drove cancellation-rebooking and agency-travel claims; HMRC AMAP-rate freeze (45p/mile since 2011) sustains internal-rate dispute pressure.",
        "sources": [
            {"publisher": "Royal Berkshire NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.royalberkshire.nhs.uk/about-us/publications/annual-reports/"},
            {"publisher": "NHS England", "title": "Non-Emergency Patient Transport Services — National Framework + Eligibility Criteria 2021", "url": "https://www.england.nhs.uk/publication/non-emergency-patient-transport-services-nepts/"},
            {"publisher": "National Audit Office", "title": "NHS England's management of the primary care support services contract with Capita", "url": "https://www.nao.org.uk/reports/nhs-englands-management-of-the-primary-care-support-services-contract-with-capita/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Royal Berkshire NHS FT provider profile (RHW)", "url": "https://www.cqc.org.uk/provider/RHW"}
        ],
        "related": ["Royal Berkshire NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Transport (business + patient) — Torbay and South Devon NHS Foundation Trust", "Transport (business + patient) — Chelsea and Westminster Hospital NHS Foundation Trust", "NHS England"]
    },
    "Establishment costs — Royal Berkshire NHS Foundation Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "Royal Berkshire NHS Foundation Trust"}],
        "description": "Royal Berkshire's £3.91M establishment costs line covers postage, telephony, mobile-data, printing, stationery, recruitment advertising, subscriptions and minor sundries across the Reading-based DGH and West Berkshire community-clinic outreach footprint. The trust sits in the New Hospital Programme cohort with its Reading new-build deferred under the January 2025 NHP Reset, preserving the existing London Road site and its embedded back-office overhead for the medium term. EPR rollout change-management and industrial-action recruitment campaigns shape 2024-25 spend.",
        "beneficiaries": "c. 6,500 WTE staff serving a c. 600,000 West Berkshire catchment (Reading, Wokingham, West Berkshire); c. 130,000 ED attendances/yr at Royal Berkshire Hospital ED; c. 80,000 admissions/yr; integrated community-clinic outreach across BOB ICS.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) — IAS 1 Presentation of Financial Statements — NHS Act 2006 — Health and Care Act 2022 — NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£3.91M"},
            {"label": "Trust scale", "value": "Single main acute (Royal Berkshire Hospital, Reading) + outreach community clinics; c. 6,500 WTE"},
            {"label": "Composition", "value": "Postage, telephony/mobile, printing, stationery, recruitment advertising, subscriptions, hospitality, minor sundries"},
            {"label": "NHP cohort + Reset", "value": "Reading new-build originally in NHP 40-hospital programme; Jan 2025 NHP Reset deferred to 2030s — sustains existing-site overhead"},
            {"label": "EPR / Frontline Digitisation", "value": "Cerner Millennium EPR (live since 2012) — ongoing optimisation drives change-comms + training-materials baseline"},
            {"label": "Industrial action 2023-24", "value": "Junior-doctor 44 days + consultant strikes drove recruitment-advertising spike + comms costs"},
            {"label": "April 2025 CPI uplift", "value": "Royal Mail + telecoms + advertising CPI feed forward unit-cost pressure"},
            {"label": "Funding trajectory", "value": "2021-22 c. £3.0M → 2023-24 c. £3.6M → 2024-25 £3.91M — sustained CPI + activity uplift"},
            {"label": "Delivery body", "value": "Trust Corporate Services + Procurement + IT + (Crown Commercial Service framework for telecoms/postage)"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Buckinghamshire, Oxfordshire and Berkshire West (BOB) ICB"},
            {"label": "Evaluation evidence", "value": "Model Hospital corporate-services benchmark; CQC RHW inspections; NHP / IPA Major Projects Report; Trust ARA 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2012 paper-based recruitment + comms baseline · Successor: post-NHP-Reset deferred-rebuild planning + digital-comms shift"}
        ],
        "notes": "Royal Berkshire's establishment-costs line carries the embedded cost of running back-office functions for a c. 6,500-WTE workforce on a constrained inner-Reading site whose long-promised replacement was deferred under the January 2025 NHP Reset. Cerner Millennium EPR (live since 2012) sustains a high digital-comms and training-materials baseline as functionality continues to be optimised. Industrial action 2023-24 lifted recruitment-advertising spend through agency and substantive recruitment campaigns. Royal Mail postage uplifts (2024-25 stamp price increases) and telecoms CPI feed forward unit-cost pressure into 2025-26, while NHP-Reset deferral preserves the existing-site overhead profile rather than triggering a transition baseline.",
        "sources": [
            {"publisher": "Royal Berkshire NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.royalberkshire.nhs.uk/about-us/publications/annual-reports/"},
            {"publisher": "Department of Health and Social Care", "title": "New Hospital Programme — January 2025 Reset", "url": "https://www.gov.uk/government/publications/new-hospital-programme-plan-for-implementation"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Royal Berkshire NHS FT provider profile (RHW)", "url": "https://www.cqc.org.uk/provider/RHW"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/connecting-health-and-care/frontline-digitisation/"}
        ],
        "related": ["Royal Berkshire NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Transport (business + patient) — Royal Berkshire NHS Foundation Trust", "Establishment costs — Northampton General Hospital NHS Trust", "Department of Health and Social Care"]
    },
    "Establishment costs — Northampton General Hospital NHS Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "Northampton General Hospital NHS Trust"}],
        "description": "Northampton General's £3.89M establishment costs line covers postage, telephony, mobile-data, printing, stationery, advertising/recruitment, subscriptions and minor sundries across the Cliftonville DGH site serving Northamptonshire. The trust operates a group-model arrangement with Kettering General Hospital under the University Hospitals of Northamptonshire (UHN) group (chair-in-common since 2021, shared executive team), shaping consolidating back-office overhead allocation. Industrial-action 2023-24 recruitment campaigns and EPR rollout change-management feed 2024-25 spend.",
        "beneficiaries": "c. 5,000 WTE staff serving a c. 380,000 South Northamptonshire catchment (Northampton, Daventry, South Northants, Wellingborough peripherals); c. 110,000 ED attendances/yr at Northampton General ED; c. 55,000 admissions/yr; single-site DGH (Cliftonville) with regional cancer-centre + maternity hub.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) — IAS 1 Presentation of Financial Statements — NHS Act 2006 — Health and Care Act 2022 — NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£3.89M"},
            {"label": "Trust scale", "value": "Single-site DGH (Cliftonville, Northampton); c. 5,000 WTE"},
            {"label": "UHN group context", "value": "University Hospitals of Northamptonshire group with Kettering General — chair-in-common since 2021; shared executive team + consolidating back-office"},
            {"label": "Composition", "value": "Postage, telephony/mobile, printing, stationery, recruitment advertising, subscriptions, hospitality, minor sundries"},
            {"label": "EPR / Frontline Digitisation", "value": "Nervecentre + EPR convergence with Kettering under UHN group drives change-mgmt + training comms baseline"},
            {"label": "Industrial action 2023-24", "value": "Junior-doctor 44 days + consultant strikes drove recruitment-advertising spike + comms costs"},
            {"label": "April 2025 CPI uplift", "value": "Royal Mail + telecoms + advertising CPI feed forward unit-cost pressure"},
            {"label": "Funding trajectory", "value": "2021-22 c. £3.0M → 2023-24 c. £3.5M → 2024-25 £3.89M — sustained CPI + group-model integration costs"},
            {"label": "Delivery body", "value": "UHN group corporate services + Trust Procurement + IT + (Crown Commercial Service framework for telecoms/postage)"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Northamptonshire ICB"},
            {"label": "Evaluation evidence", "value": "Model Hospital corporate-services benchmark; CQC RNS inspections; UHN group-model business case; Trust ARA 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2021 stand-alone NGH baseline · Successor: full UHN group consolidation + post-EPR digital-comms shift"}
        ],
        "notes": "Northampton General's establishment-costs line reflects the active University Hospitals of Northamptonshire group-model integration with Kettering General Hospital — chair-in-common since 2021, shared executive team and progressive back-office consolidation are reshaping the overhead boundary, with shared-services efficiencies offset short-term by integration project costs. Industrial action 2023-24 drove recruitment-advertising spend through agency and substantive campaigns. Nervecentre and EPR convergence under the UHN group feeds change-management and training-materials spend. Royal Mail postage uplifts and telecoms CPI feed forward unit-cost pressure into 2025-26. Northamptonshire ICB allocation remains the governing finance frame.",
        "sources": [
            {"publisher": "Northampton General Hospital NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.northamptongeneral.nhs.uk/AboutUs/Publications/AnnualReports/"},
            {"publisher": "University Hospitals of Northamptonshire NHS Group", "title": "Group strategy and arrangements", "url": "https://www.ngh-kgh.nhs.uk/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Northampton General provider profile (RNS)", "url": "https://www.cqc.org.uk/provider/RNS"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/connecting-health-and-care/frontline-digitisation/"}
        ],
        "related": ["Northampton General Hospital NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Establishment costs — Sherwood Forest Hospitals NHS Foundation Trust", "Establishment costs — Royal Berkshire NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Transport (business + patient) — Torbay and South Devon NHS Foundation Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "Torbay and South Devon NHS Foundation Trust"}],
        "description": "Torbay and South Devon's £3.88M transport line carries an unusually broad profile reflecting the trust's status as one of England's most-integrated acute + community Care Trust models — covering business mileage (AfC S17 + AMAP), pool-fleet IFRS 16 leases, NEPTS contracts and a substantial community-team mileage baseline across the South Devon rural footprint. The trust integrates Torbay Hospital acute care with a wide community-clinic, community-nursing and adult-social-care footprint under a single budget, lifting the transport-line per-£ baseline above pure-acute peers.",
        "beneficiaries": "c. 6,500 WTE staff serving a c. 375,000 Torbay + South Devon catchment (Torquay, Paignton, Brixham, Newton Abbot, Totnes); c. 90,000 ED attendances/yr at Torbay Hospital ED; c. 50,000 admissions/yr; integrated community-nursing + adult-social-care teams across rural South Devon driving substantial business-mileage baseline.",
        "legal_basis": "NHS Act 2006 — NHSE Patient Transport Services Eligibility Criteria — Agenda for Change Section 17 (business mileage) — HMRC AMAP rates — IFRS 16 Leases (pool fleet) — Care Act 2014 (integrated adult social-care delegation) — DHSC Group Accounting Manual 2024-25",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£3.88M"},
            {"label": "Trust scale", "value": "Torbay Hospital + integrated community-nursing + adult-social-care teams; c. 6,500 WTE"},
            {"label": "Integrated Care Trust model", "value": "Acute + community + adult social-care under single budget — lifts community-team mileage baseline materially above pure-acute peers"},
            {"label": "Composition", "value": "Business mileage (AfC S17 + AMAP 45p/25p) + pool-fleet IFRS 16 leases + NEPTS contract pass-through + patient travel reimbursements"},
            {"label": "Rural geography", "value": "South Devon dispersed rural footprint — high mileage per community visit + long NEPTS journeys to regional centres (Exeter, Plymouth)"},
            {"label": "NEPTS commissioning", "value": "Devon ICS lead-commissioner NEPTS contract — eligibility per NHSE 2021 criteria; outsourced operator delivery"},
            {"label": "Industrial action 2023-24 effect", "value": "Junior-doctor 44 days + consultant strikes drove agency travel-claim + cancellation rebooking transport"},
            {"label": "Funding trajectory", "value": "2021-22 c. £3.2M → 2023-24 c. £3.6M → 2024-25 £3.88M — fuel CPI + community-team activity uplift"},
            {"label": "Delivery body", "value": "Trust E&F + outsourced NEPTS provider (Devon ICS lead-commissioner) + pool-fleet leasing partner + Trust HR (mileage)"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + NHSE Urgent and Emergency Care (NEPTS) + Devon ICB + DHSC"},
            {"label": "Evaluation evidence", "value": "NAO Health and Social Care integration 2023; CQC RA9 inspections; NHSE NEPTS Eligibility Review 2021; Torbay ICT model evaluations"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2015 stand-alone Torbay Hospital + Devon PCT community baselines · Successor: continued ICT-model embedding under Devon ICS + ICS-collaborative NEPTS retender"}
        ],
        "notes": "Torbay and South Devon's transport baseline reflects England's earliest and most-developed integrated Care Trust model — acute, community and adult-social-care delivery under a single statutory umbrella drives a substantially broader business-mileage profile than peer acute trusts, with rural South Devon community-team visits dominating the line. Devon ICS commissions NEPTS centrally, with eligibility tightened under NHSE's 2021 criteria refresh and rural long-distance journeys to Exeter and Plymouth carrying weight in unit cost. Industrial action 2023-24 lifted agency travel-claim and rebooking spend; HMRC AMAP-rate freeze (45p since 2011) sustains internal-rate dispute pressure.",
        "sources": [
            {"publisher": "Torbay and South Devon NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.torbayandsouthdevon.nhs.uk/about-us/our-publications/"},
            {"publisher": "NHS England", "title": "Non-Emergency Patient Transport Services — National Framework + Eligibility Criteria 2021", "url": "https://www.england.nhs.uk/publication/non-emergency-patient-transport-services-nepts/"},
            {"publisher": "National Audit Office", "title": "Progress in implementing the integration of health and social care", "url": "https://www.nao.org.uk/reports/progress-in-implementing-integrated-care/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Torbay and South Devon provider profile (RA9)", "url": "https://www.cqc.org.uk/provider/RA9"}
        ],
        "related": ["Torbay and South Devon NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Transport (business + patient) — Royal Berkshire NHS Foundation Trust", "Transport (business + patient) — Chelsea and Westminster Hospital NHS Foundation Trust", "NHS England"]
    },
    "Business rates — Portsmouth Hospitals University NHS Trust": {
        "aliases": [{"name": "Business rates", "parent": "Portsmouth Hospitals University NHS Trust"}],
        "description": "Portsmouth Hospitals University's £3.82M business-rates line covers non-domestic rates (NDR) on the Queen Alexandra Hospital Cosham main site plus satellite outpatient facilities — assessed by the Valuation Office Agency on rateable values (2023 revaluation effective Apr 2023) and billed by Portsmouth City Council. The hereditament reflects the c. 1,200-bed PFI-built hospital plus parking and ancillary buildings. NHS trusts pay the full multiplier (no charitable 80% relief applicable to NHS), making rates a meaningful operating-cost item.",
        "beneficiaries": "c. 8,000 WTE staff serving a c. 675,000 South East Hampshire and South-West Sussex catchment (Portsmouth, Havant, Fareham, Gosport, Petersfield); c. 160,000 ED attendances/yr at Queen Alexandra ED (one of South Coast's busiest); c. 90,000 admissions/yr; main-site Queen Alexandra Hospital plus St Mary's outpatient site.",
        "legal_basis": "Local Government Finance Act 1988 (Schedule 6) — Non-Domestic Rating (Multipliers and Private Finance) Act 2024 — Non-Domestic Rating Act 2023 — DHSC Group Accounting Manual 2024-25 — NHS Act 2006 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£3.82M"},
            {"label": "Trust scale", "value": "Queen Alexandra Hospital (Cosham) c. 1,200 beds + St Mary's outpatient site; c. 8,000 WTE"},
            {"label": "PFI estate", "value": "Queen Alexandra rebuilt under 2005 PFI (operational 2009) — large rateable hereditament"},
            {"label": "Billing authority", "value": "Portsmouth City Council (NDR collection); Valuation Office Agency rateable-value assessment"},
            {"label": "2023 revaluation", "value": "VOA 2023 revaluation (effective 1 Apr 2023) re-set rateable values from 2017 list — large transitional effects on big hospital hereditaments"},
            {"label": "Multiplier 2024-25", "value": "Standard non-domestic multiplier 54.6p (England, 2024-25); NHS pays full rate (no charitable relief)"},
            {"label": "NDR 2024 Act context", "value": "Non-Domestic Rating (Multipliers and Private Finance) Act 2024 — splits multipliers + reforms anti-avoidance; NHS PFI rateability remains contested in some sector cases"},
            {"label": "Funding trajectory", "value": "2021-22 c. £3.4M → 2023-24 (post-revaluation) c. £3.7M → 2024-25 £3.82M — multiplier + transitional uplift"},
            {"label": "Delivery body", "value": "Trust E&F (rates appeals) + Valuation Office Agency + Portsmouth City Council"},
            {"label": "Policy owner", "value": "MHCLG (NDR policy) + HM Treasury + DHSC + NHSE Provider Finance + Hampshire and Isle of Wight ICB"},
            {"label": "Evaluation evidence", "value": "VOA Rating List 2023; NAO Business Rates Reform; Trust ARA 2023-24; CQC RHU inspections"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2017 rating list baseline · Successor: 2026 revaluation cycle + NDR 2024 Act multiplier-split implementation"}
        ],
        "notes": "Portsmouth Hospitals University's rates line is dominated by the Queen Alexandra Hospital Cosham hereditament — rebuilt under the 2005 PFI deal (operational 2009) — whose c. 1,200-bed footprint and modern PFI build standards drive a large rateable value on the VOA 2023 list. NHS trusts cannot claim charitable 80% relief, so the full standard multiplier (54.6p in 2024-25) applies. The 2023 revaluation lifted rateable values across the NHS estate with transitional relief tapering, while the Non-Domestic Rating (Multipliers and Private Finance) Act 2024 introduces multiplier splitting and anti-avoidance reform that will reshape future bills. Portsmouth City Council collects, with VOA assessing — appeals are managed via the Trust E&F team.",
        "sources": [
            {"publisher": "Portsmouth Hospitals University NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.porthosp.nhs.uk/about-us/our-publications.htm"},
            {"publisher": "Valuation Office Agency", "title": "2023 Rating List", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "Ministry of Housing, Communities and Local Government", "title": "Non-Domestic Rating Act 2023 + Multipliers and Private Finance Act 2024", "url": "https://www.gov.uk/government/collections/business-rates"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Portsmouth Hospitals University provider profile (RHU)", "url": "https://www.cqc.org.uk/provider/RHU"}
        ],
        "related": ["Portsmouth Hospitals University NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Business rates — University Hospitals Bristol and Weston NHS Foundation Trust", "Business rates — Sherwood Forest Hospitals NHS Foundation Trust", "Valuation Office Agency"]
    },
    "Business rates — University Hospitals Bristol and Weston NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "University Hospitals Bristol and Weston NHS Foundation Trust"}],
        "description": "UHBW's £3.79M business-rates line covers non-domestic rates on the Bristol Royal Infirmary (BRI) precinct — including BRI, Bristol Heart Institute, Bristol Royal Hospital for Children, Bristol Eye Hospital, St Michael's maternity and the South Bristol Community Hospital — plus Weston General Hospital following the 2020 merger. The hereditaments span a high-value Bristol city-centre footprint and a Weston-super-Mare DGH, assessed by the Valuation Office Agency and billed by Bristol City Council and North Somerset Council respectively.",
        "beneficiaries": "c. 13,000 WTE staff serving a c. 800,000 South West catchment; c. 200,000 ED attendances/yr (BRI + Bristol Children's + Weston EDs combined); c. 130,000 admissions/yr; multi-site city-centre Bristol footprint plus Weston General DGH; tertiary cardiac, paediatric and ophthalmology specialty.",
        "legal_basis": "Local Government Finance Act 1988 (Schedule 6) — Non-Domestic Rating (Multipliers and Private Finance) Act 2024 — Non-Domestic Rating Act 2023 — DHSC Group Accounting Manual 2024-25 — NHS Act 2006 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£3.79M"},
            {"label": "Trust scale", "value": "BRI precinct (c. 1,200 beds across BRI + Children's + Heart + Eye + St Michael's) + Weston General Hospital + South Bristol Community Hospital; c. 13,000 WTE"},
            {"label": "Merger context", "value": "Merger of UH Bristol with Weston Area Health Trust completed Apr 2020 — single rating profile post-merger"},
            {"label": "Billing authorities", "value": "Bristol City Council (BRI precinct + South Bristol Community) + North Somerset Council (Weston General)"},
            {"label": "2023 revaluation", "value": "VOA 2023 revaluation (effective 1 Apr 2023) re-set rateable values from 2017 list — high city-centre Bristol values"},
            {"label": "Multiplier 2024-25", "value": "Standard non-domestic multiplier 54.6p (England, 2024-25); NHS pays full rate (no charitable relief)"},
            {"label": "Tertiary specialty hereditaments", "value": "Heart Institute + Children's + Eye + St Michael's tertiary buildings carry distinct rateable values driving line above peer multi-site DGH baselines"},
            {"label": "Funding trajectory", "value": "2021-22 (post-merger) c. £3.4M → 2023-24 c. £3.65M → 2024-25 £3.79M — multiplier + transitional uplift"},
            {"label": "Delivery body", "value": "Trust E&F (rates appeals) + Valuation Office Agency + Bristol City Council + North Somerset Council"},
            {"label": "Policy owner", "value": "MHCLG (NDR policy) + HM Treasury + DHSC + NHSE Provider Finance + Bristol, North Somerset and South Gloucestershire ICB"},
            {"label": "Evaluation evidence", "value": "VOA Rating List 2023; NAO Business Rates Reform; Trust ARA 2023-24; CQC RA7 inspections"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2020 separate UH Bristol + Weston rate baselines · Successor: 2026 revaluation cycle + NDR 2024 Act multiplier-split implementation"}
        ],
        "notes": "UHBW's rates line carries the full breadth of the Bristol city-centre tertiary precinct — the Heart Institute, Children's, Eye and St Michael's all sit on distinct hereditaments with high city-centre rateable values — plus the Weston General DGH (post-2020 merger) under North Somerset Council. The VOA 2023 revaluation lifted city-centre Bristol values materially, with transitional relief tapering. NHS trusts cannot claim charitable 80% relief, so the full 54.6p standard multiplier applies. The Non-Domestic Rating (Multipliers and Private Finance) Act 2024 introduces multiplier splitting that will affect large hereditaments — UHBW's tertiary buildings are exposed to higher-multiplier classification in future bills. Appeals are managed via the Trust E&F team across two billing authorities.",
        "sources": [
            {"publisher": "University Hospitals Bristol and Weston NHS FT", "title": "Annual Report and Accounts 2023-24", "url": "https://www.uhbw.nhs.uk/about-us/publications"},
            {"publisher": "Valuation Office Agency", "title": "2023 Rating List", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "Ministry of Housing, Communities and Local Government", "title": "Non-Domestic Rating Act 2023 + Multipliers and Private Finance Act 2024", "url": "https://www.gov.uk/government/collections/business-rates"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "UHBW provider profile (RA7)", "url": "https://www.cqc.org.uk/provider/RA7"}
        ],
        "related": ["University Hospitals Bristol and Weston NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Business rates — Portsmouth Hospitals University NHS Trust", "Amortisation — University Hospitals Bristol and Weston NHS Foundation Trust", "Valuation Office Agency"]
    },
    "General supplies & services — Sherwood Forest Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "Sherwood Forest Hospitals NHS Foundation Trust"}],
        "description": "Sherwood Forest's £3.79M general supplies & services line covers non-clinical consumables, linen, catering provisions, hotel-services materials, office supplies, IT consumables and minor expensed equipment across King's Mill DGH, Newark Hospital and Mansfield Community Hospital. The line sits within Clinical Supplies & Drugs in the trust accounts but covers non-clinical-consumable inputs to clinical environments. King's Mill PFI (2005-2043) shapes hotel-services contract structure with subcontracted soft-FM cohort affecting consumables ownership boundaries.",
        "beneficiaries": "c. 5,000 WTE staff serving a c. 420,000 Mid Nottinghamshire catchment (Mansfield, Newark, Sherwood); c. 130,000 ED attendances/yr at King's Mill ED; c. 60,000 admissions/yr; three-site footprint (King's Mill DGH c. 460 beds + Newark Hospital + Mansfield Community Hospital).",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) — IAS 2 Inventories — Procurement Act 2023 — NHS Act 2006 — Health and Care Act 2022 — NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "General supplies & services 2024-25", "value": "£3.79M"},
            {"label": "Trust scale", "value": "Three-site (King's Mill DGH + Newark Hospital + Mansfield Community Hospital); c. 5,000 WTE"},
            {"label": "PFI estate context", "value": "King's Mill PFI 2005-2043 — soft-FM subcontracted cohort affects consumable-ownership boundary; non-PFI scope drives this line"},
            {"label": "Procurement route", "value": "NHS Supply Chain national framework + trust-direct contracts + East Midlands ICS/ICB collaborative"},
            {"label": "Composition", "value": "Linen, catering provisions, hotel-services materials, office supplies, IT consumables, minor expensed equipment"},
            {"label": "Industrial action 2023-24 effect", "value": "Junior-doctor 44 days + consultant strikes drove cancellation rebooking + agency-backfill consumable churn"},
            {"label": "April 2025 NIC + CPI uplift", "value": "Indirect via supplier pass-through; non-clinical CPI feed forward unit-cost pressure"},
            {"label": "Funding trajectory", "value": "2021-22 c. £2.9M → 2023-24 c. £3.5M → 2024-25 £3.79M — sustained CPI + activity uplift"},
            {"label": "Delivery body", "value": "Trust Procurement + NHS Supply Chain (DHSC ALB) + Nottingham & Nottinghamshire ICS procurement collaborative + PFI soft-FM subcontractors (boundary)"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Nottingham & Nottinghamshire ICB"},
            {"label": "Evaluation evidence", "value": "Model Hospital benchmarks; NAO PFI legacy reports; NHS Supply Chain ARA; Trust ARA 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2014 contract-reset baseline · Successor: ICS-collaborative procurement scaling + 2043 PFI hand-back consumable-boundary reset"}
        ],
        "notes": "Sherwood Forest's general supplies & services baseline is shaped by the King's Mill PFI (2005-2043) and the soft-FM subcontracted cohort that delivers cleaning, catering and portering — the consumable-ownership boundary between the SPV and the trust affects which materials flow through this line versus the unitary charge. NHS Supply Chain remains dominant for non-clinical consumables, with Nottingham & Nottinghamshire ICS procurement collaborative scaling as a medium-term lever. Industrial action 2023-24 drove cancellation-rebooking and agency-backfill consumable churn. Non-clinical CPI feed forward unit-cost pressure into 2025-26, while 2043 PFI hand-back planning will reset the consumable-boundary structure.",
        "sources": [
            {"publisher": "Sherwood Forest Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.sfh-tr.nhs.uk/about-us/our-publications/"},
            {"publisher": "NHS Supply Chain", "title": "Annual Report 2023-24", "url": "https://www.supplychain.nhs.uk/about-us/our-publications/"},
            {"publisher": "National Audit Office", "title": "PFI and PF2 (HC 718, 2018)", "url": "https://www.nao.org.uk/reports/pfi-and-pf2/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Sherwood Forest Hospitals provider profile (RK5)", "url": "https://www.cqc.org.uk/provider/RK5"}
        ],
        "related": ["Sherwood Forest Hospitals NHS Foundation Trust", "Clinical Supplies & Drugs", "NHS Acute Trusts", "PFI / LIFT charges — Sherwood Forest Hospitals NHS Foundation Trust", "General supplies & services — Portsmouth Hospitals University NHS Trust", "NHS Supply Chain"]
    },
    "Amortisation — Portsmouth Hospitals University NHS Trust": {
        "aliases": [{"name": "Amortisation", "parent": "Portsmouth Hospitals University NHS Trust"}],
        "description": "Portsmouth Hospitals University's £3.78M amortisation line covers the systematic write-down of intangible assets — capitalised software, EPR licences, internally-developed clinical applications and licensed-intellectual-property — under IAS 38 across the c. 1,200-bed Queen Alexandra Hospital + St Mary's outpatient site footprint. The trust runs an Oracle-Cerner-based EPR convergence trajectory under NHSE's Frontline Digitisation programme, with capitalised intangible build now amortising over assessed useful-economic-life (typically 5-10 years).",
        "beneficiaries": "c. 8,000 WTE staff serving a c. 675,000 South East Hampshire and South-West Sussex catchment; c. 160,000 ED attendances/yr at Queen Alexandra ED; c. 90,000 admissions/yr; main-site Queen Alexandra Hospital plus St Mary's outpatient site benefit from amortising digital infrastructure.",
        "legal_basis": "IAS 38 Intangible Assets — DHSC Group Accounting Manual 2024-25 (chapter 5 — Intangibles) — IFRS 15 / IAS 38 SaaS configuration agenda decisions — NHS Act 2006 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£3.78M"},
            {"label": "Trust scale", "value": "Queen Alexandra Hospital (Cosham) c. 1,200 beds + St Mary's outpatient site; c. 8,000 WTE"},
            {"label": "Composition", "value": "Capitalised software + EPR licences + internally-developed clinical applications + licensed IP"},
            {"label": "EPR / Frontline Digitisation", "value": "PHU is on Frontline Digitisation track — capitalised EPR build amortises over assessed UEL (typically 5-10 years)"},
            {"label": "Useful economic life", "value": "Software 3-5 years; EPR / clinical-system 5-10 years per DHSC GAM ch.5 + IAS 38 review"},
            {"label": "IFRIC SaaS agenda decision", "value": "2021 IFRIC agenda decision on SaaS configuration costs — restricts capitalisation; some EPR programme spend now opex"},
            {"label": "PFI build context", "value": "Queen Alexandra Hospital PFI build (2009 operational) — tangible-asset depreciation sits separately; this line is intangibles only"},
            {"label": "Funding trajectory", "value": "2021-22 c. £3.0M → 2023-24 c. £3.5M → 2024-25 £3.78M — Frontline Digitisation amortisation cycle ramp"},
            {"label": "Delivery body", "value": "Trust IT + Finance (capitalisation) + EPR vendor (Oracle Health / Cerner) + NHSE Frontline Digitisation programme"},
            {"label": "Policy owner", "value": "DHSC + NHSE Transformation Directorate + NHSE Provider Finance + Hampshire and Isle of Wight ICB"},
            {"label": "Evaluation evidence", "value": "NAO Digital transformation in NHS 2020; DHSC GAM ch.5; Trust ARA 2023-24; CQC RHU inspections"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-Frontline Digitisation legacy clinical-system amortisation tail · Successor: full EPR-go-live amortisation peak + post-IFRIC SaaS reclassification"}
        ],
        "notes": "Portsmouth Hospitals University's amortisation line tracks the trust's intangible-asset stock — capitalised EPR build under NHSE's Frontline Digitisation programme is the dominant driver, with Oracle-Cerner stack capitalised costs amortising over a 5-10 year assessed useful-economic-life per DHSC GAM ch.5 and IAS 38. The 2021 IFRIC SaaS agenda decision restricted capitalisation of SaaS configuration costs, pushing some Frontline Digitisation programme spend into opex and reshaping the medium-term amortisation profile. The Queen Alexandra PFI tangible-asset depreciation sits in a separate line. Industrial action 2023-24 had no direct effect on amortisation but EPR optimisation costs continue to feed both opex and capitalisable elements.",
        "sources": [
            {"publisher": "Portsmouth Hospitals University NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.porthosp.nhs.uk/about-us/our-publications.htm"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 5 — Intangibles)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/connecting-health-and-care/frontline-digitisation/"},
            {"publisher": "National Audit Office", "title": "Digital transformation in the NHS (HC 317, 2020)", "url": "https://www.nao.org.uk/reports/the-use-of-digital-technology-in-the-nhs/"},
            {"publisher": "Care Quality Commission", "title": "Portsmouth Hospitals University provider profile (RHU)", "url": "https://www.cqc.org.uk/provider/RHU"}
        ],
        "related": ["Portsmouth Hospitals University NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Amortisation — University Hospitals Bristol and Weston NHS Foundation Trust", "Business rates — Portsmouth Hospitals University NHS Trust", "NHS England"]
    },
    "Amortisation — University Hospitals Bristol and Weston NHS Foundation Trust": {
        "aliases": [{"name": "Amortisation", "parent": "University Hospitals Bristol and Weston NHS Foundation Trust"}],
        "description": "UHBW's £3.70M amortisation line covers systematic write-down of intangible assets — capitalised software, EPR licences, internally-developed clinical applications, tertiary-specialty clinical-information-system licences and licensed IP — under IAS 38 across the Bristol city-centre tertiary precinct (BRI + Children's + Heart + Eye + St Michael's) plus Weston General. The trust's tertiary cardiac, paediatric and ophthalmology specialism drives capitalised specialty-system stock above peer DGH baselines, with Frontline Digitisation programme pulling ongoing capitalised build through.",
        "beneficiaries": "c. 13,000 WTE staff serving a c. 800,000 South West catchment; c. 200,000 ED attendances/yr (BRI + Children's + Weston EDs combined); c. 130,000 admissions/yr; multi-site city-centre Bristol footprint plus Weston General DGH; tertiary cardiac, paediatric and ophthalmology specialty all benefit from amortising digital infrastructure.",
        "legal_basis": "IAS 38 Intangible Assets — DHSC Group Accounting Manual 2024-25 (chapter 5 — Intangibles) — IFRIC SaaS configuration agenda decisions — NHS Act 2006 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£3.70M"},
            {"label": "Trust scale", "value": "BRI precinct (c. 1,200 beds across BRI + Children's + Heart + Eye + St Michael's) + Weston General + South Bristol Community Hospital; c. 13,000 WTE"},
            {"label": "Composition", "value": "Capitalised software + EPR + tertiary specialty clinical-information systems + licensed IP + internally-developed apps"},
            {"label": "EPR / Frontline Digitisation", "value": "UHBW EPR convergence on Epic via merger-integration — capitalised build amortises over assessed UEL"},
            {"label": "Tertiary specialty systems", "value": "Cardiac CIS + paediatric specialty systems + ophthalmology imaging — high-value intangible stock above peer DGH"},
            {"label": "Useful economic life", "value": "Software 3-5 years; EPR / clinical-system 5-10 years per DHSC GAM ch.5 + IAS 38 review"},
            {"label": "Merger context", "value": "Apr 2020 UH Bristol + Weston merger — post-merger system convergence drives integration-related capitalisation; 2021 IFRIC SaaS agenda decision restricts SaaS configuration capitalisation"},
            {"label": "Funding trajectory", "value": "2021-22 (post-merger) c. £2.9M → 2023-24 c. £3.4M → 2024-25 £3.70M — Frontline Digitisation amortisation cycle ramp"},
            {"label": "Delivery body", "value": "Trust IT + Finance (capitalisation) + EPR vendor (Epic/Oracle Health/Cerner) + NHSE Frontline Digitisation programme"},
            {"label": "Policy owner", "value": "DHSC + NHSE Transformation Directorate + NHSE Provider Finance + Bristol, North Somerset and South Gloucestershire ICB"},
            {"label": "Evaluation evidence", "value": "NAO Digital transformation in NHS 2020; DHSC GAM ch.5; Trust ARA 2023-24; CQC RA7 inspections"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-merger separate UH Bristol + Weston intangible stocks · Successor: post-merger system-convergence amortisation peak + post-IFRIC SaaS reclassification"}
        ],
        "notes": "UHBW's amortisation line carries the cumulative effect of Bristol's tertiary-specialty clinical-information-system stack (cardiac CIS, paediatric specialty systems, ophthalmology imaging) plus the EPR convergence trajectory following the April 2020 Weston merger. NHSE's Frontline Digitisation programme is pulling capitalised EPR build through the line at a ramping pace, with assessed useful-economic-life of 5-10 years for clinical systems per DHSC GAM ch.5 and IAS 38. The 2021 IFRIC SaaS agenda decision restricted capitalisation of SaaS configuration costs, reshaping the medium-term amortisation profile by pushing some build spend into opex. Tangible-asset depreciation across the Bristol precinct sits in a separate line; this is intangibles only.",
        "sources": [
            {"publisher": "University Hospitals Bristol and Weston NHS FT", "title": "Annual Report and Accounts 2023-24", "url": "https://www.uhbw.nhs.uk/about-us/publications"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 5 — Intangibles)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/connecting-health-and-care/frontline-digitisation/"},
            {"publisher": "National Audit Office", "title": "Digital transformation in the NHS (HC 317, 2020)", "url": "https://www.nao.org.uk/reports/the-use-of-digital-technology-in-the-nhs/"},
            {"publisher": "Care Quality Commission", "title": "UHBW provider profile (RA7)", "url": "https://www.cqc.org.uk/provider/RA7"}
        ],
        "related": ["University Hospitals Bristol and Weston NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Business rates — University Hospitals Bristol and Weston NHS Foundation Trust", "Amortisation — Portsmouth Hospitals University NHS Trust", "NHS England"]
    },
    "Lease expenditure — London North West University Healthcare NHS Trust": {
        "aliases": [{"name": "Lease expenditure", "parent": "London North West University Healthcare NHS Trust"}],
        "description": "LNWH's £3.70M lease expenditure line covers IFRS 16 right-of-use lease costs across the trust's complex North-West London estate — Northwick Park Hospital, Central Middlesex, Ealing Hospital and a wide community-clinic + outpatient footprint serving Brent, Harrow and Ealing. The line includes NHSPS occupier-cost-rentals on community sites, third-party leased space and pool-fleet/equipment leases — IFRS 16 (effective 1 Apr 2022 in DHSC GAM) lifted balance-sheet capitalisation but residual short-term and low-value leases continue to flow through this opex line.",
        "beneficiaries": "c. 9,500 WTE staff serving a c. 950,000 Brent, Harrow and Ealing catchment; c. 200,000 ED attendances/yr (Northwick Park + Ealing EDs combined); c. 90,000 admissions/yr; multi-site footprint (Northwick Park acute hub + Central Middlesex elective + Ealing DGH + community clinics).",
        "legal_basis": "IFRS 16 Leases — DHSC Group Accounting Manual 2024-25 (chapter 7 — Leases and service concessions) — Landlord and Tenant Act 1954 — NHS Act 2006 — Health and Care Act 2022 — NHS Property Services occupier-cost-rental framework",
        "key_stats": [
            {"label": "Lease expenditure 2024-25", "value": "£3.70M"},
            {"label": "Trust scale", "value": "Northwick Park Hospital + Central Middlesex Hospital + Ealing Hospital + community clinics; c. 9,500 WTE"},
            {"label": "Estate complexity", "value": "Multi-site North-West London footprint with substantial NHSPS-leased community-clinic + outpatient space"},
            {"label": "IFRS 16 transition", "value": "DHSC GAM IFRS 16 effective 1 Apr 2022 — most material leases now capitalised; residual short-term + low-value continue through opex"},
            {"label": "NHSPS occupier-cost-rentals", "value": "Community-clinic NHSPS rentals on full market-rent transition trajectory — historic dispute resolution shapes baseline"},
            {"label": "Composition", "value": "Short-term leases <12mo + low-value leases <£5k + variable lease components + service-charge elements not in IFRS 16 scope"},
            {"label": "Pool-fleet + equipment", "value": "Operational leases on pool fleet + medical equipment off-balance-sheet residuals"},
            {"label": "Funding trajectory", "value": "2021-22 (pre-IFRS 16) c. £8M opex → 2022-23 (post-IFRS 16) c. £3.5M residual → 2024-25 £3.70M"},
            {"label": "Delivery body", "value": "Trust E&F + NHS Property Services (NHSPS) + leasing partners + NHS Shared Business Services (estates payments)"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + NHS Property Services + North West London ICB"},
            {"label": "Evaluation evidence", "value": "NAO Estate management 2020; PAC NHSPS hearings; DHSC GAM ch.7; Trust ARA 2023-24; CQC R1K inspections"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-IFRS 16 full-opex lease baseline · Successor: ongoing NHSPS rental-trajectory + lease re-negotiation under estate-rationalisation"}
        ],
        "notes": "LNWH's lease expenditure line reflects the residual short-term and low-value leases flowing through opex after the 1 April 2022 IFRS 16 transition under DHSC GAM ch.7 — material property leases are now capitalised on balance sheet, leaving this line covering scope-exempt elements plus service-charge components, variable lease elements and pool-fleet/equipment operational leases. The trust's wide North-West London community-clinic footprint carries substantial NHSPS-leased space, with historic occupier-cost-rental disputes (sector-wide 2018-2024) progressively resolving towards full market-rent recovery. Estate-rationalisation under the merged trust (post-2014 NWLH + Ealing) continues to reshape the residual lease base, with CPI and April 2025 NIC pass-through feeding landlord costs.",
        "sources": [
            {"publisher": "London North West University Healthcare NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.lnwh.nhs.uk/about-us/who-we-are/publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 7 — Leases and service concessions)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS Property Services", "title": "Annual Report 2023-24", "url": "https://www.property.nhs.uk/about/our-publications/"},
            {"publisher": "National Audit Office", "title": "Managing the NHS estate (HC 1135, 2020)", "url": "https://www.nao.org.uk/reports/managing-the-nhs-estate/"},
            {"publisher": "Care Quality Commission", "title": "London North West University Healthcare provider profile (R1K)", "url": "https://www.cqc.org.uk/provider/R1K"}
        ],
        "related": ["London North West University Healthcare NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "NHS Property Services", "Lease expenditure — Northern Care Alliance NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Transport (business + patient) — Chelsea and Westminster Hospital NHS Foundation Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "Chelsea and Westminster Hospital NHS Foundation Trust"}],
        "description": "Chelsea and Westminster's £3.69M transport line covers business mileage (AfC S17 + AMAP), pool-fleet IFRS 16 leases, NEPTS contracts and patient travel reimbursements across the two-site Chelsea + West Middlesex DGH footprint plus an extensive sexual-health/HIV community service network (10HS, 56 Dean Street). NEPTS commissioning sits with North West London ICS lead-commissioner, with an outsourced provider model serving the dialysis, oncology and wider OP-attendance flow into the central-London and Isleworth sites.",
        "beneficiaries": "c. 7,500 WTE staff serving a c. 800,000 inner London catchment (Westminster, Kensington & Chelsea, Hammersmith & Fulham, Hounslow); c. 200,000 ED attendances/yr (Chelsea + West Middlesex EDs combined); c. 90,000 admissions/yr; large neonatal + maternity service + nationally-recognised sexual-health network adding patient-flow complexity.",
        "legal_basis": "NHS Act 2006 — NHSE Patient Transport Services Eligibility Criteria — Agenda for Change Section 17 (business mileage) — HMRC AMAP rates — IFRS 16 Leases (pool fleet) — DHSC Group Accounting Manual 2024-25 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£3.69M"},
            {"label": "Trust scale", "value": "Chelsea and Westminster Hospital + West Middlesex University Hospital (Isleworth) + sexual-health network (10HS, 56 Dean Street); c. 7,500 WTE"},
            {"label": "NEPTS commissioning", "value": "North West London ICS lead-commissioner NEPTS contract — outsourced operator delivery; eligibility per NHSE 2021 criteria"},
            {"label": "Composition", "value": "Business mileage (AfC S17 + AMAP 45p/25p) + pool-fleet IFRS 16 leases + NEPTS contract pass-through + patient travel reimbursements"},
            {"label": "Specialty patient-flow", "value": "Dialysis + oncology + neonatal transfers across Chelsea + West Mid + tertiary referrals drive substantial NEPTS demand"},
            {"label": "Sexual-health community network", "value": "56 Dean Street + 10HS sexual-health hubs add community-team mileage baseline above peer two-site DGHs"},
            {"label": "Industrial action 2023-24 effect", "value": "Junior-doctor 44 days + consultant strikes drove agency travel-claim + cancellation rebooking transport"},
            {"label": "Funding trajectory", "value": "2021-22 c. £3.0M → 2023-24 c. £3.4M → 2024-25 £3.69M — fuel CPI + NEPTS contract uplift"},
            {"label": "Delivery body", "value": "Trust E&F + outsourced NEPTS provider (NWL ICS lead-commissioner) + pool-fleet leasing partner + Trust HR (mileage)"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + NHSE Urgent and Emergency Care (NEPTS) + North West London ICB + DHSC"},
            {"label": "Evaluation evidence", "value": "NAO NEPTS 2019; CQC RQM inspections; NHSE NEPTS Eligibility Review 2021; Trust ARA 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2015 stand-alone Chelsea + Westminster transport (pre-West Mid acquisition Sep 2014) · Successor: ICS-collaborative NEPTS retender + ULEZ + congestion-charge-zone fleet electrification"}
        ],
        "notes": "Chelsea and Westminster's transport line carries the cross-site flow between the central-London Chelsea site and West Middlesex Hospital in Isleworth (acquired September 2014), plus a wider sexual-health community-team network (56 Dean Street, 10HS). NEPTS volume is shaped by tertiary dialysis, oncology and neonatal transfers, with North West London ICS lead-commissioner running the outsourced contract under NHSE's 2021 eligibility criteria. The London ULEZ extension (Aug 2023 outer London) and central-London congestion-charge environment increasingly shape pool-fleet electrification trajectory. Industrial action 2023-24 lifted agency travel-claim and rebooking spend; HMRC AMAP-rate freeze (45p since 2011) sustains internal-rate dispute pressure.",
        "sources": [
            {"publisher": "Chelsea and Westminster Hospital NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.chelwest.nhs.uk/about-us/key-information/annual-reports"},
            {"publisher": "NHS England", "title": "Non-Emergency Patient Transport Services — National Framework + Eligibility Criteria 2021", "url": "https://www.england.nhs.uk/publication/non-emergency-patient-transport-services-nepts/"},
            {"publisher": "National Audit Office", "title": "NHS England's management of NEPTS / NHS travel costs", "url": "https://www.nao.org.uk/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Chelsea and Westminster Hospital provider profile (RQM)", "url": "https://www.cqc.org.uk/provider/RQM"}
        ],
        "related": ["Chelsea and Westminster Hospital NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Transport (business + patient) — Royal Berkshire NHS Foundation Trust", "Transport (business + patient) — Torbay and South Devon NHS Foundation Trust", "NHS England"]
    },
    "Transport (business + patient) — North Middlesex University Hospital NHS Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "North Middlesex University Hospital NHS Trust"}],
        "description": "North Middlesex's £3.68M transport line covers business mileage (AfC S17 + AMAP), pool-fleet IFRS 16 leases, NEPTS contracts and patient travel reimbursements at the single-site Edmonton DGH serving north-east London's high-deprivation Enfield + Haringey catchment. The trust is in active merger transaction with Royal Free London NHS FT under the North Central London ICS group model, reshaping the medium-term NEPTS commissioning vehicle. Inner-London ULEZ environment plus dialysis + maternity transfer flow drive line composition.",
        "beneficiaries": "c. 3,500 WTE staff serving a c. 350,000 Enfield and Haringey catchment with very high IMD deprivation; c. 200,000 ED attendances/yr (one of London's busiest single-site EDs); c. 65,000 admissions/yr; large maternity unit (c. 4,500 deliveries/yr) drives transfer-in / transfer-out NEPTS demand.",
        "legal_basis": "NHS Act 2006 — NHSE Patient Transport Services Eligibility Criteria — Agenda for Change Section 17 (business mileage) — HMRC AMAP rates — IFRS 16 Leases (pool fleet) — DHSC Group Accounting Manual 2024-25 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£3.68M"},
            {"label": "Trust scale", "value": "Single-site DGH (Sterling Way, Edmonton); c. 3,500 WTE"},
            {"label": "NEPTS commissioning", "value": "North Central London ICS lead-commissioner NEPTS contract — outsourced operator delivery; eligibility per NHSE 2021 criteria"},
            {"label": "Royal Free merger context", "value": "Transaction with Royal Free London NHS FT progressing 2023-25 → group-model integration under NCL ICS reshapes medium-term transport vehicle"},
            {"label": "Composition", "value": "Business mileage (AfC S17 + AMAP 45p/25p) + pool-fleet IFRS 16 leases + NEPTS contract pass-through + patient travel reimbursements"},
            {"label": "Catchment + maternity + ULEZ", "value": "Enfield + Haringey high IMD drives high reimbursement-claim volume; c. 4,500 deliveries/yr drives in-utero/neonatal NEPTS to UCLH + Royal Free; Aug 2023 ULEZ extension covers Edmonton shaping pool-fleet electrification"},
            {"label": "Industrial action 2023-24 effect", "value": "Junior-doctor 44 days + consultant strikes drove agency travel-claim + cancellation rebooking transport"},
            {"label": "Funding trajectory", "value": "2021-22 c. £3.0M → 2023-24 c. £3.4M → 2024-25 £3.68M — fuel CPI + NEPTS contract uplift"},
            {"label": "Delivery body", "value": "Trust E&F + outsourced NEPTS provider (NCL ICS lead-commissioner) + pool-fleet leasing partner + Trust HR (mileage)"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + NHSE Urgent and Emergency Care (NEPTS) + North Central London ICB + DHSC"},
            {"label": "Evaluation evidence", "value": "NAO NEPTS 2019; CQC RAP inspections; NHSE NEPTS Eligibility Review 2021; NCL ICS group-model business case"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-merger stand-alone trust transport baseline · Successor: Royal Free Group consolidated transport post-transaction + ICS-collaborative NEPTS retender"}
        ],
        "notes": "North Middlesex's transport line reflects one of London's most deprived catchments — Enfield + Haringey — with very high patient-travel reimbursement claim volumes and a c. 4,500-delivery maternity unit driving substantial in-utero and neonatal transfer NEPTS demand to NCL tertiary partners (UCLH, Royal Free). The active merger transaction with Royal Free London NHS FT under the North Central London ICS group model will progressively reshape the transport-commissioning vehicle as Royal Free Group functions absorb the contract base. The August 2023 ULEZ extension covers Edmonton, shaping pool-fleet electrification trajectory. Industrial action 2023-24 lifted agency travel-claim and rebooking spend; HMRC AMAP-rate freeze (45p since 2011) sustains internal-rate dispute pressure.",
        "sources": [
            {"publisher": "North Middlesex University Hospital NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.northmid.nhs.uk/annual-reports"},
            {"publisher": "NHS England", "title": "Non-Emergency Patient Transport Services — National Framework + Eligibility Criteria 2021", "url": "https://www.england.nhs.uk/publication/non-emergency-patient-transport-services-nepts/"},
            {"publisher": "NHS England (London)", "title": "North Central London ICS group-model transaction (Royal Free + North Mid)", "url": "https://www.england.nhs.uk/london/our-work/north-central-london/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "North Middlesex provider profile (RAP)", "url": "https://www.cqc.org.uk/provider/RAP"}
        ],
        "related": ["North Middlesex University Hospital NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Royal Free London NHS Foundation Trust", "Transport (business + patient) — Chelsea and Westminster Hospital NHS Foundation Trust", "NHS England"]
    },
    "Business rates — Sherwood Forest Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "Sherwood Forest Hospitals NHS Foundation Trust"}],
        "description": "Sherwood Forest's £3.67M business-rates line covers non-domestic rates on King's Mill Hospital, Newark Hospital and Mansfield Community Hospital — assessed by the Valuation Office Agency on rateable values (2023 revaluation effective Apr 2023) and billed by Ashfield District Council, Newark and Sherwood District Council and Mansfield District Council. King's Mill Hospital was rebuilt under the 2005 PFI deal (operational 2011), giving it a substantial modern-build rateable hereditament that dominates the line.",
        "beneficiaries": "c. 5,000 WTE staff serving a c. 420,000 Mid Nottinghamshire catchment (Mansfield, Newark, Sherwood); c. 130,000 ED attendances/yr at King's Mill ED; c. 60,000 admissions/yr; three-site footprint (King's Mill DGH c. 460 beds + Newark Hospital + Mansfield Community Hospital).",
        "legal_basis": "Local Government Finance Act 1988 (Schedule 6) — Non-Domestic Rating (Multipliers and Private Finance) Act 2024 — Non-Domestic Rating Act 2023 — DHSC Group Accounting Manual 2024-25 — NHS Act 2006 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£3.67M"},
            {"label": "Trust scale", "value": "Three-site (King's Mill DGH c. 460 beds + Newark Hospital + Mansfield Community Hospital); c. 5,000 WTE"},
            {"label": "PFI build context", "value": "King's Mill rebuilt under 2005 PFI (operational 2011) — modern-build rateable hereditament dominates line"},
            {"label": "Billing authorities", "value": "Ashfield District Council (King's Mill) + Newark and Sherwood District Council (Newark Hospital) + Mansfield District Council (Mansfield Community)"},
            {"label": "2023 revaluation", "value": "VOA 2023 revaluation (effective 1 Apr 2023) re-set rateable values from 2017 list"},
            {"label": "Multiplier 2024-25", "value": "Standard non-domestic multiplier 54.6p (England, 2024-25); NHS pays full rate (no charitable relief)"},
            {"label": "NDR 2024 Act + PFI rateability", "value": "NDR (Multipliers and Private Finance) Act 2024 splits multipliers; PFI hospital rateability + multiple-occupier disputes have been a recurring sector-wide issue — King's Mill engagement with VOA via Trust E&F"},
            {"label": "Funding trajectory", "value": "2021-22 c. £3.3M → 2023-24 (post-revaluation) c. £3.55M → 2024-25 £3.67M — multiplier + transitional uplift"},
            {"label": "Delivery body", "value": "Trust E&F (rates appeals) + Valuation Office Agency + Ashfield/Newark+Sherwood/Mansfield District Councils"},
            {"label": "Policy owner", "value": "MHCLG (NDR policy) + HM Treasury + DHSC + NHSE Provider Finance + Nottingham & Nottinghamshire ICB"},
            {"label": "Evaluation evidence", "value": "VOA Rating List 2023; NAO Business Rates Reform; Trust ARA 2023-24; CQC RK5 inspections"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2017 rating list baseline · Successor: 2026 revaluation cycle + NDR 2024 Act multiplier-split implementation + 2043 PFI hand-back rates re-assessment"}
        ],
        "notes": "Sherwood Forest's rates line is dominated by the King's Mill Hospital hereditament — rebuilt under the 2005 PFI deal (operational 2011) — whose c. 460-bed modern-build footprint sits on a substantial rateable value on the VOA 2023 list. NHS trusts cannot claim charitable 80% relief, so the full 54.6p standard multiplier applies. Three District Councils — Ashfield, Newark and Sherwood, and Mansfield — bill the trust across the three sites. PFI hospital rateability has been a recurring sector-wide issue (multiple-occupier disputes), and the Non-Domestic Rating (Multipliers and Private Finance) Act 2024 introduces multiplier splitting affecting future bills; 2043 PFI hand-back will trigger a hereditament re-assessment.",
        "sources": [
            {"publisher": "Sherwood Forest Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.sfh-tr.nhs.uk/about-us/our-publications/"},
            {"publisher": "Valuation Office Agency", "title": "2023 Rating List", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "Ministry of Housing, Communities and Local Government", "title": "Non-Domestic Rating Act 2023 + Multipliers and Private Finance Act 2024", "url": "https://www.gov.uk/government/collections/business-rates"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Sherwood Forest Hospitals provider profile (RK5)", "url": "https://www.cqc.org.uk/provider/RK5"}
        ],
        "related": ["Sherwood Forest Hospitals NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Business rates — Portsmouth Hospitals University NHS Trust", "Business rates — University Hospitals Bristol and Weston NHS Foundation Trust", "Valuation Office Agency"]
    },
    "General supplies & services — Portsmouth Hospitals University NHS Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "Portsmouth Hospitals University NHS Trust"}],
        "description": "Portsmouth Hospitals University's £3.64M general supplies & services line covers non-clinical consumables, linen, catering provisions, hotel-services materials, office supplies, IT consumables and minor expensed equipment across the c. 1,200-bed Queen Alexandra Hospital plus St Mary's outpatient site. The line sits in Clinical Supplies & Drugs in trust accounts but covers non-clinical consumable inputs to clinical environments. Procurement is via NHS Supply Chain national framework plus Hampshire and Isle of Wight ICS collaborative scaling.",
        "beneficiaries": "c. 8,000 WTE staff serving a c. 675,000 South East Hampshire and South-West Sussex catchment; c. 160,000 ED attendances/yr at Queen Alexandra ED; c. 90,000 admissions/yr; main-site Queen Alexandra Hospital (c. 1,200 beds, PFI 2009 build) plus St Mary's outpatient site.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) — IAS 2 Inventories — Procurement Act 2023 — NHS Act 2006 — Health and Care Act 2022 — NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "General supplies & services 2024-25", "value": "£3.64M"},
            {"label": "Trust scale", "value": "Queen Alexandra Hospital (Cosham) c. 1,200 beds + St Mary's outpatient site; c. 8,000 WTE"},
            {"label": "PFI estate context", "value": "Queen Alexandra rebuilt under 2005 PFI (operational 2009) — soft-FM contract structure shapes consumable-ownership boundary"},
            {"label": "Procurement route", "value": "NHS Supply Chain national framework + Hampshire and Isle of Wight ICS collaborative + trust-direct contracts"},
            {"label": "Composition", "value": "Linen, catering provisions, hotel-services materials, office supplies, IT consumables, minor expensed equipment"},
            {"label": "ED throughput + activity churn", "value": "c. 160,000 ED attendances/yr (among South Coast's busiest) drives high-volume consumable baseline; industrial action 2023-24 (junior-doctor 44 days + consultant strikes) drove cancellation rebooking + agency-backfill consumable churn"},
            {"label": "April 2025 NIC + CPI uplift", "value": "Indirect via supplier pass-through; non-clinical CPI feed forward unit-cost pressure"},
            {"label": "Funding trajectory", "value": "2021-22 c. £2.8M → 2023-24 c. £3.4M → 2024-25 £3.64M — sustained CPI + activity uplift"},
            {"label": "Delivery body", "value": "Trust Procurement + NHS Supply Chain (DHSC ALB) + Hampshire and Isle of Wight ICS procurement collaborative + PFI soft-FM (boundary)"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Hampshire and Isle of Wight ICB"},
            {"label": "Evaluation evidence", "value": "Model Hospital benchmarks; NHS Supply Chain ARA; Trust ARA 2023-24; CQC RHU inspections"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2009 PFI-build baseline · Successor: ICS-collaborative procurement scaling + Procurement Act 2023 implementation"}
        ],
        "notes": "Portsmouth Hospitals University's general supplies & services baseline reflects high ED attendance (c. 160,000/yr — among South Coast's busiest) at the modern Queen Alexandra Hospital, with the 2009 PFI build's soft-FM contract structure shaping the consumable-ownership boundary between SPV-delivered hotel services and trust-purchased materials. NHS Supply Chain remains dominant for non-clinical consumables, with Hampshire and Isle of Wight ICS procurement collaborative scaling as a medium-term lever. Industrial action 2023-24 drove cancellation-rebooking and agency-backfill consumable churn. Procurement Act 2023 implementation (2024-25 onwards) reshapes contracting framework. Non-clinical CPI feed forward unit-cost pressure into 2025-26.",
        "sources": [
            {"publisher": "Portsmouth Hospitals University NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.porthosp.nhs.uk/about-us/our-publications.htm"},
            {"publisher": "NHS Supply Chain", "title": "Annual Report 2023-24", "url": "https://www.supplychain.nhs.uk/about-us/our-publications/"},
            {"publisher": "Cabinet Office", "title": "Procurement Act 2023 — Implementation guidance", "url": "https://www.gov.uk/government/collections/procurement-act-2023-guidance-documents"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Portsmouth Hospitals University provider profile (RHU)", "url": "https://www.cqc.org.uk/provider/RHU"}
        ],
        "related": ["Portsmouth Hospitals University NHS Trust", "Clinical Supplies & Drugs", "NHS Acute Trusts", "General supplies & services — Sherwood Forest Hospitals NHS Foundation Trust", "Business rates — Portsmouth Hospitals University NHS Trust", "NHS Supply Chain"]
    },
    "Business rates — Norfolk and Norwich University Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "Norfolk and Norwich University Hospitals NHS Foundation Trust"}],
        "description": "Norfolk and Norwich's £3.62M business-rates line covers non-domestic rates on the Norfolk and Norwich University Hospital (Colney) PFI-built main site plus the Cromer Hospital satellite — assessed by the Valuation Office Agency on rateable values (2023 revaluation effective Apr 2023) and billed by South Norfolk District Council and North Norfolk District Council. NNUH was one of the first-wave PFI hospitals (signed 1998, operational 2001), giving it a substantial PFI-built rateable hereditament that dominates the line.",
        "beneficiaries": "c. 10,000 WTE staff serving a c. 1.0M Norfolk + North Suffolk catchment; c. 175,000 ED attendances/yr at NNUH ED; c. 100,000 admissions/yr; main-site NNUH (c. 1,200 beds, PFI 2001 build) + Cromer Hospital satellite + Jenny Lind Children's outpatient.",
        "legal_basis": "Local Government Finance Act 1988 (Schedule 6) — Non-Domestic Rating (Multipliers and Private Finance) Act 2024 — Non-Domestic Rating Act 2023 — DHSC Group Accounting Manual 2024-25 — NHS Act 2006 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£3.62M"},
            {"label": "Trust scale", "value": "NNUH Colney site (c. 1,200 beds) + Cromer Hospital + Jenny Lind Children's outpatient; c. 10,000 WTE"},
            {"label": "PFI build context", "value": "NNUH first-wave PFI (signed 1998, operational 2001) — concession runs to c. 2037; large modern-build rateable hereditament"},
            {"label": "Billing authorities", "value": "South Norfolk District Council (NNUH Colney) + North Norfolk District Council (Cromer Hospital)"},
            {"label": "2023 revaluation", "value": "VOA 2023 revaluation (effective 1 Apr 2023) re-set rateable values from 2017 list"},
            {"label": "Multiplier 2024-25", "value": "Standard non-domestic multiplier 54.6p (England, 2024-25); NHS pays full rate (no charitable relief)"},
            {"label": "RAAC + PFI hand-back planning", "value": "NNUH on Sep 2023 HSSIB RAAC list — remediation underway; c. 12-13 years to PFI expiry, IPA/HMT Hand-Back unit engagement triggers future hereditament re-assessment"},
            {"label": "Funding trajectory", "value": "2021-22 c. £3.2M → 2023-24 (post-revaluation) c. £3.5M → 2024-25 £3.62M — multiplier + transitional uplift"},
            {"label": "Delivery body", "value": "Trust E&F (rates appeals) + Valuation Office Agency + South Norfolk + North Norfolk District Councils"},
            {"label": "Policy owner", "value": "MHCLG (NDR policy) + HM Treasury + DHSC + NHSE Provider Finance + Norfolk and Waveney ICB"},
            {"label": "Evaluation evidence", "value": "VOA Rating List 2023; HSSIB RAAC list 2023; NAO PFI hand-back review 2020; Trust ARA 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2017 rating list baseline · Successor: 2026 revaluation cycle + NDR 2024 Act multiplier-split + 2037 PFI hand-back hereditament re-assessment"}
        ],
        "notes": "Norfolk and Norwich's rates line is dominated by the NNUH Colney hereditament — built under the 1998-signed first-wave PFI deal (operational 2001) — whose c. 1,200-bed footprint sits on a substantial rateable value on the VOA 2023 list. NHS trusts cannot claim charitable 80% relief, so the full 54.6p standard multiplier applies. The trust appears on the September 2023 HSSIB RAAC list, with concrete-plank remediation under way at NNUH. PFI hand-back planning ahead of c. 2037 expiry is the medium-term reset trigger, and the Non-Domestic Rating (Multipliers and Private Finance) Act 2024 introduces multiplier splitting affecting future bills, with Trust E&F managing appeals across two District Councils.",
        "sources": [
            {"publisher": "Norfolk and Norwich University Hospitals NHS FT", "title": "Annual Report and Accounts 2023-24", "url": "https://www.nnuh.nhs.uk/publications/"},
            {"publisher": "Valuation Office Agency", "title": "2023 Rating List", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "Health Services Safety Investigations Body", "title": "RAAC in NHS estate — September 2023 list", "url": "https://www.hssib.org.uk/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Norfolk and Norwich University Hospitals provider profile (RM1)", "url": "https://www.cqc.org.uk/provider/RM1"}
        ],
        "related": ["Norfolk and Norwich University Hospitals NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Business rates — Sherwood Forest Hospitals NHS Foundation Trust", "Business rates — Portsmouth Hospitals University NHS Trust", "Valuation Office Agency"]
    },
    "Establishment costs — Wrightington, Wigan and Leigh NHS Foundation Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "Wrightington, Wigan and Leigh NHS Foundation Trust"}],
        "description": "WWL's £3.62M establishment costs line covers postage, telephony, printing, stationery, recruitment advertising, subscriptions and minor sundries across the trust's three-site Greater Manchester footprint — Wigan Royal Albert Edward Infirmary (RAEI), Leigh Infirmary and Wrightington Hospital (orthopaedic specialist centre). The Wrightington orthopaedic specialty (national centre for joint-replacement) and group-model relationships across Greater Manchester ICS shape a non-clinical-overhead profile balancing DGH overhead with tertiary-orthopaedic comms needs.",
        "beneficiaries": "c. 5,000 WTE staff serving a c. 320,000 Wigan borough catchment plus national-tertiary orthopaedic referrals; c. 110,000 ED attendances/yr at RAEI ED; c. 55,000 admissions/yr; three-site footprint (RAEI Wigan + Leigh Infirmary + Wrightington orthopaedic specialist centre).",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) — IAS 1 Presentation of Financial Statements — NHS Act 2006 — Health and Care Act 2022 — NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£3.62M"},
            {"label": "Trust scale", "value": "Three-site (Wigan RAEI + Leigh Infirmary + Wrightington orthopaedic specialist); c. 5,000 WTE"},
            {"label": "Wrightington tertiary orthopaedic", "value": "Internationally-recognised joint-replacement centre (Charnley legacy) — drives national tertiary referrals + comms baseline"},
            {"label": "Composition", "value": "Postage, telephony/mobile, printing, stationery, recruitment advertising, subscriptions, hospitality, minor sundries"},
            {"label": "EPR / Frontline Digitisation", "value": "Allscripts EPR + Nervecentre rollout — drives change-mgmt comms + training-materials baseline"},
            {"label": "Industrial action 2023-24 + GM ICS group", "value": "Junior-doctor 44 days + consultant strikes drove recruitment-advertising spike + comms costs; WWL participates in GM ICS provider-collaborative arrangements with developing shared-back-office trajectory"},
            {"label": "April 2025 CPI uplift", "value": "Royal Mail + telecoms + advertising CPI feed forward unit-cost pressure"},
            {"label": "Funding trajectory", "value": "2021-22 c. £2.8M → 2023-24 c. £3.3M → 2024-25 £3.62M — sustained CPI + activity uplift"},
            {"label": "Delivery body", "value": "Trust Corporate Services + Procurement + IT + (Crown Commercial Service framework for telecoms/postage)"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Greater Manchester ICB"},
            {"label": "Evaluation evidence", "value": "Model Hospital corporate-services benchmark; CQC RRF inspections; GM ICS provider-collaborative reports; Trust ARA 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-FT (2008) corporate-services baseline · Successor: GM ICS provider-collaborative shared-back-office + post-EPR digital-comms shift"}
        ],
        "notes": "WWL's establishment-costs baseline reflects a three-site Greater Manchester footprint where the Wrightington Hospital orthopaedic specialist centre — internationally recognised since the Charnley low-friction-arthroplasty legacy of the 1960s — drives a national-tertiary-referral comms profile alongside the Wigan and Leigh DGH overhead. Allscripts EPR and Nervecentre rollout under NHSE's Frontline Digitisation programme feeds change-management and training-materials baseline. Industrial action 2023-24 lifted recruitment-advertising spend through agency and substantive campaigns. Greater Manchester ICS provider-collaborative arrangements are shaping a medium-term shared-back-office trajectory. Royal Mail postage uplifts and telecoms CPI feed forward unit-cost pressure into 2025-26.",
        "sources": [
            {"publisher": "Wrightington, Wigan and Leigh NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.wwl.nhs.uk/annual-report"},
            {"publisher": "NHS Greater Manchester ICB", "title": "Provider collaborative arrangements", "url": "https://gmintegratedcare.org.uk/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Wrightington, Wigan and Leigh provider profile (RRF)", "url": "https://www.cqc.org.uk/provider/RRF"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/connecting-health-and-care/frontline-digitisation/"}
        ],
        "related": ["Wrightington, Wigan and Leigh NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Establishment costs — Sherwood Forest Hospitals NHS Foundation Trust", "Establishment costs — Northampton General Hospital NHS Trust", "Department of Health and Social Care"]
    },
}
