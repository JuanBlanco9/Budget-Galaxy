# -*- coding: utf-8 -*-
# Phase 2 Acute slice 2 — chunk 25 (17 NHS Acute Trust orphan sub-lines)
# Hand-curated trust-specific PROGRAMME-archetype enrichment entries.
# Structural contract per docs/archetype_briefs.md.

NEW = {
    "Transport (business + patient) — Buckinghamshire Healthcare NHS Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "Buckinghamshire Healthcare NHS Trust"}],
        "description": "Buckinghamshire Healthcare's £2.79M transport line covers business mileage (AfC Section 17 + HMRC AMAP), pool-fleet IFRS 16 lease costs, NEPTS contract pass-through and patient travel reimbursements across the Stoke Mandeville Hospital + Wycombe Hospital + Amersham Hospital footprint. The trust hosts the National Spinal Injuries Centre at Stoke Mandeville, which generates substantial long-distance and specialist-vehicle PTS demand from across England. NEPTS is commissioned through the Buckinghamshire, Oxfordshire and Berkshire West ICS lead-commissioner.",
        "beneficiaries": "c. 6,500 WTE staff serving a c. 555,000 Buckinghamshire catchment plus national tertiary referrals; c. 130,000 ED attendances/yr at Stoke Mandeville + Wycombe MIU; c. 75,000 admissions/yr; National Spinal Injuries Centre tertiary catchment England-wide.",
        "legal_basis": "NHS Act 2006 — NHSE Patient Transport Services Eligibility Criteria 2021 — Agenda for Change Section 17 (business mileage) — HMRC AMAP rates — IFRS 16 Leases (pool fleet) — DHSC Group Accounting Manual 2024-25 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£2.79M"},
            {"label": "Trust scale", "value": "Stoke Mandeville Hospital + Wycombe Hospital + Amersham Hospital + community sites; c. 6,500 WTE"},
            {"label": "National Spinal Injuries Centre", "value": "NSIC at Stoke Mandeville — England's largest spinal injuries unit; drives long-distance specialist-vehicle PTS England-wide"},
            {"label": "NEPTS commissioning", "value": "Buckinghamshire, Oxfordshire and Berkshire West ICS lead-commissioner NEPTS contract; eligibility per NHSE 2021 criteria"},
            {"label": "Composition", "value": "Business mileage (AfC S17 + AMAP 45p/25p frozen since 2011) + pool-fleet IFRS 16 leases + NEPTS pass-through + patient travel reimbursements"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove cancellation rebooking + agency travel claims"},
            {"label": "April 2025 NIC + fuel CPI", "value": "Indirect via NEPTS contractor pass-through + diesel CPI feed forward unit-cost pressure"},
            {"label": "Funding trajectory", "value": "2021-22 c. £2.3M → 2023-24 c. £2.55M → 2024-25 £2.79M — fuel CPI + NEPTS contract uplift + tertiary spinal-injury volume recovery"},
            {"label": "Delivery body", "value": "Trust E&F + outsourced NEPTS provider (BOB ICS lead-commissioner) + pool-fleet leasing partner + Trust HR (mileage) + NSIC dedicated transport"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + NHSE Urgent and Emergency Care (NEPTS) + Buckinghamshire, Oxfordshire and Berkshire West ICB + DHSC"},
            {"label": "Evaluation evidence", "value": "NAO NEPTS 2019; CQC RXQ inspections; NHSE NEPTS Eligibility Review 2021; Trust ARA 2023-24; Spinal Injuries Association"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-ICS CCG-commissioned NEPTS contracts · Successor: BOB ICS-collaborative NEPTS retender + tertiary-network NSIC transfer protocol refresh"}
        ],
        "notes": "Buckinghamshire Healthcare's transport line is shaped by the National Spinal Injuries Centre at Stoke Mandeville — England's largest spinal injuries unit, generating long-distance specialist-vehicle PTS demand drawn from across England including paralympic-pathway and complex-disability transfers. The BOB ICS lead-commissioner NEPTS contract covers routine eligibility-tier journeys with NHSE 2021 criteria tightening the patient-paid threshold. Industrial action 2023-24 drove cancellation rebooking and agency travel claims; HMRC AMAP-rate freeze (45p/mile since 2011) sustains internal-rate dispute pressure. Diesel CPI and April 2025 employer NIC step-up (15%, £5k threshold) feed forward via NEPTS contractor pass-through.",
        "sources": [
            {"publisher": "Buckinghamshire Healthcare NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.buckshealthcare.nhs.uk/about-the-trust/board-papers-publications/"},
            {"publisher": "NHS England", "title": "Non-Emergency Patient Transport Services — National Framework + Eligibility Criteria 2021", "url": "https://www.england.nhs.uk/publication/non-emergency-patient-transport-services-nepts/"},
            {"publisher": "National Audit Office", "title": "NHS England's management of the primary care support services contract with Capita", "url": "https://www.nao.org.uk/reports/nhs-englands-management-of-the-primary-care-support-services-contract-with-capita/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Buckinghamshire Healthcare NHS Trust provider profile (RXQ)", "url": "https://www.cqc.org.uk/provider/RXQ"}
        ],
        "related": ["Buckinghamshire Healthcare NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Transport (business + patient) — University Hospital Southampton NHS Foundation Trust", "Transport (business + patient) — South Warwickshire NHS Foundation Trust", "NHS England"]
    },
    "Transport (business + patient) — South Warwickshire NHS Foundation Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "South Warwickshire NHS Foundation Trust"}],
        "description": "South Warwickshire's £2.783M transport line covers business mileage (AfC Section 17 + HMRC AMAP), pool-fleet IFRS 16 lease costs, NEPTS contract pass-through and patient travel reimbursements across the Warwick Hospital + Stratford Hospital + Leamington Spa Hospital + integrated community services footprint. The trust has an unusually integrated acute-plus-community model under the FT licence, generating heavy district-nurse and CCN business mileage in addition to NEPTS volume. NEPTS is commissioned through the Coventry and Warwickshire ICS lead-commissioner.",
        "beneficiaries": "c. 5,500 WTE staff serving a c. 280,000 South Warwickshire catchment plus integrated community population; c. 70,000 ED attendances/yr at Warwick Hospital ED; c. 50,000 admissions/yr; integrated acute + community services district-nurse + CCN footprint.",
        "legal_basis": "NHS Act 2006 — NHSE Patient Transport Services Eligibility Criteria 2021 — Agenda for Change Section 17 (business mileage) — HMRC AMAP rates — IFRS 16 Leases (pool fleet) — DHSC Group Accounting Manual 2024-25 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£2.783M"},
            {"label": "Trust scale", "value": "Warwick Hospital + Stratford Hospital + Leamington Spa Hospital + integrated community services; c. 5,500 WTE"},
            {"label": "Integrated acute + community", "value": "Combined acute-plus-community FT model — drives heavy district-nurse and CCN business mileage relative to peer DGHs"},
            {"label": "NEPTS commissioning", "value": "Coventry and Warwickshire ICS lead-commissioner NEPTS contract; eligibility per NHSE 2021 criteria"},
            {"label": "Composition", "value": "Business mileage (AfC S17 + AMAP 45p/25p frozen since 2011) + pool-fleet IFRS 16 leases + NEPTS pass-through + patient travel reimbursements"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove cancellation rebooking + agency travel claims"},
            {"label": "April 2025 NIC + fuel CPI", "value": "Indirect via NEPTS contractor pass-through + diesel CPI feed forward unit-cost pressure"},
            {"label": "Funding trajectory", "value": "2021-22 c. £2.3M → 2023-24 c. £2.55M → 2024-25 £2.783M — fuel CPI + NEPTS uplift + community-mileage growth"},
            {"label": "Delivery body", "value": "Trust E&F + outsourced NEPTS provider (Coventry + Warwickshire ICS lead-commissioner) + pool-fleet leasing partner + Trust HR (mileage)"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + NHSE Urgent and Emergency Care (NEPTS) + Coventry and Warwickshire ICB + DHSC"},
            {"label": "Evaluation evidence", "value": "NAO NEPTS 2019; CQC RJC inspections; NHSE NEPTS Eligibility Review 2021; Trust ARA 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-ICS CCG-commissioned NEPTS contracts · Successor: Coventry and Warwickshire ICS-collaborative NEPTS retender + community-mileage rationalisation"}
        ],
        "notes": "South Warwickshire's transport line is shaped by the unusually integrated acute-plus-community FT model — the trust runs district-nursing, community children's nursing, health visiting and end-of-life community services in addition to the Warwick Hospital DGH, generating heavy AfC Section 17 business mileage on top of routine NEPTS volume. Coventry and Warwickshire ICS lead-commissioner NEPTS contract covers routine eligibility-tier journeys with NHSE 2021 criteria tightening the patient-paid threshold. Industrial action 2023-24 drove cancellation rebooking and agency travel claims; HMRC AMAP-rate freeze (45p/mile since 2011) sustains internal-rate dispute pressure. Diesel CPI and April 2025 employer NIC step-up (15%, £5k threshold) feed forward via NEPTS contractor pass-through.",
        "sources": [
            {"publisher": "South Warwickshire NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.swft.nhs.uk/about-us/publications"},
            {"publisher": "NHS England", "title": "Non-Emergency Patient Transport Services — National Framework + Eligibility Criteria 2021", "url": "https://www.england.nhs.uk/publication/non-emergency-patient-transport-services-nepts/"},
            {"publisher": "National Audit Office", "title": "NHS England's management of the primary care support services contract with Capita", "url": "https://www.nao.org.uk/reports/nhs-englands-management-of-the-primary-care-support-services-contract-with-capita/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "South Warwickshire NHS FT provider profile (RJC)", "url": "https://www.cqc.org.uk/provider/RJC"}
        ],
        "related": ["South Warwickshire NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Transport (business + patient) — Buckinghamshire Healthcare NHS Trust", "Transport (business + patient) — The Hillingdon Hospitals NHS Foundation Trust", "NHS England"]
    },
    "Transport (business + patient) — The Hillingdon Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "The Hillingdon Hospitals NHS Foundation Trust"}],
        "description": "Hillingdon's £2.769M transport line covers business mileage (AfC Section 17 + HMRC AMAP), pool-fleet IFRS 16 lease costs, NEPTS contract pass-through and patient travel reimbursements across the Hillingdon Hospital + Mount Vernon Hospital footprint in north-west London. The trust serves the airport-borough of Hillingdon (including Heathrow worker population) and shares the Mount Vernon site with East and North Hertfordshire NHS Trust (cancer centre) — driving cross-trust patient transfer demand. NEPTS is commissioned through the North West London ICS lead-commissioner.",
        "beneficiaries": "c. 3,500 WTE staff serving a c. 310,000 Hillingdon catchment plus Heathrow-worker transient population; c. 110,000 ED attendances/yr at Hillingdon Hospital ED; c. 60,000 admissions/yr; Mount Vernon shared with East and North Herts NHS Trust (cancer centre).",
        "legal_basis": "NHS Act 2006 — NHSE Patient Transport Services Eligibility Criteria 2021 — Agenda for Change Section 17 (business mileage) — HMRC AMAP rates — IFRS 16 Leases (pool fleet) — DHSC Group Accounting Manual 2024-25 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£2.769M"},
            {"label": "Trust scale", "value": "Hillingdon Hospital + Mount Vernon Hospital (shared campus); c. 3,500 WTE"},
            {"label": "New Hospital Programme", "value": "Hillingdon Hospital is on the New Hospital Programme cohort (RAAC + structural concerns) — Reset Jan 2025 deferred construction timeline; demolition + decant journeys ahead"},
            {"label": "NEPTS commissioning", "value": "North West London ICS lead-commissioner NEPTS contract; eligibility per NHSE 2021 criteria"},
            {"label": "Mount Vernon shared site", "value": "Mount Vernon Hospital shared with East and North Herts NHS Trust (cancer centre) — cross-trust patient transfer flows"},
            {"label": "Composition", "value": "Business mileage (AfC S17 + AMAP 45p/25p frozen since 2011) + pool-fleet IFRS 16 leases + NEPTS pass-through + patient travel reimbursements"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove cancellation rebooking + agency travel claims"},
            {"label": "April 2025 NIC + fuel CPI", "value": "Indirect via NEPTS contractor pass-through + diesel CPI feed forward unit-cost pressure"},
            {"label": "Funding trajectory", "value": "2021-22 c. £2.3M → 2023-24 c. £2.5M → 2024-25 £2.769M — fuel CPI + NEPTS uplift + decant/transfer flows"},
            {"label": "Delivery body", "value": "Trust E&F + outsourced NEPTS provider (NW London ICS lead-commissioner) + pool-fleet leasing partner + Trust HR (mileage)"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + NHSE Urgent and Emergency Care (NEPTS) + North West London ICB + DHSC + NHP delivery"},
            {"label": "Evaluation evidence", "value": "NAO NEPTS 2019; CQC RAS inspections; NHSE NEPTS Eligibility Review 2021; Trust ARA 2023-24; NAO NHP 2025"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-ICS CCG-commissioned NEPTS contracts · Successor: NW London ICS-collaborative NEPTS retender + NHP rebuild decant transfers"}
        ],
        "notes": "Hillingdon's transport line carries both routine NEPTS pass-through and the early-phase decant flows associated with the New Hospital Programme rebuild — the trust is one of the original NHP-40 cohort with structural and RAAC concerns, deferred but not cancelled by the Jan 2025 NHP Reset. Mount Vernon shared-site flows with East and North Herts (cancer centre) generate cross-trust patient transfers. Heathrow Airport's transient worker and visitor population shapes ED demand and ad-hoc travel reimbursement claims. Industrial action 2023-24 drove cancellation rebooking and agency travel claims; HMRC AMAP-rate freeze (45p/mile since 2011) sustains internal-rate dispute pressure. Diesel CPI and April 2025 NIC step-up feed forward via NEPTS pass-through.",
        "sources": [
            {"publisher": "The Hillingdon Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.thh.nhs.uk/about-us/publications"},
            {"publisher": "NHS England", "title": "Non-Emergency Patient Transport Services — National Framework + Eligibility Criteria 2021", "url": "https://www.england.nhs.uk/publication/non-emergency-patient-transport-services-nepts/"},
            {"publisher": "Department of Health and Social Care", "title": "New Hospital Programme — Plan for Implementation (Jan 2025 Reset)", "url": "https://www.gov.uk/government/publications/new-hospital-programme-plan-for-implementation"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "The Hillingdon Hospitals NHS FT provider profile (RAS)", "url": "https://www.cqc.org.uk/provider/RAS"}
        ],
        "related": ["The Hillingdon Hospitals NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Transport (business + patient) — South Warwickshire NHS Foundation Trust", "Transport (business + patient) — Whittington Health NHS Trust", "New Hospital Programme"]
    },
    "Amortisation — University Hospitals of Derby and Burton NHS Foundation Trust": {
        "aliases": [{"name": "Amortisation", "parent": "University Hospitals of Derby and Burton NHS Foundation Trust"}],
        "description": "UHDB's £2.754M amortisation line is the systematic write-down of capitalised intangible assets — predominantly software licences, EPR-build internally generated intangibles and clinical-system development costs — across the Royal Derby Hospital + Queen's Hospital Burton + Florence Nightingale Community Hospital + Sir Robert Peel Community Hospital + Samuel Johnson Community Hospital footprint. UHDB merged July 2018 (Derby Teaching Hospitals + Burton Hospitals) and is on the Frontline Digitisation Cerner Oracle Health EPR programme, which drives material recent intangible additions and amortisation cycles.",
        "beneficiaries": "c. 13,500 WTE staff serving a c. 1.05M southern Derbyshire + east Staffordshire catchment; c. 250,000 ED attendances/yr (Royal Derby ED + Queen's Burton ED); c. 165,000 admissions/yr; five-site footprint post-2018 merger.",
        "legal_basis": "IAS 38 Intangible Assets — DHSC Group Accounting Manual 2024-25 chapter 5 — NHS Act 2006 — Health and Care Act 2022 — IFRS 16 (capitalised intangible interaction)",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£2.754M"},
            {"label": "Trust scale", "value": "Royal Derby Hospital + Queen's Hospital Burton + Florence Nightingale + Sir Robert Peel + Samuel Johnson Community Hospitals; c. 13,500 WTE"},
            {"label": "Merger origin", "value": "UHDB formed 1 July 2018 — Derby Teaching Hospitals + Burton Hospitals merger; combined intangible asset register from that date"},
            {"label": "Frontline Digitisation EPR", "value": "Cerner Oracle Health EPR rollout under Frontline Digitisation programme — capitalised intangible drives recent amortisation step-ups"},
            {"label": "Composition", "value": "Software licences (perpetual + capitalised SaaS) + internally generated EPR-build intangibles + clinical-system development costs — IAS 38 straight-line over useful life (typ. 3-10 years)"},
            {"label": "Trent and Derby ICS", "value": "Joined Up Care Derbyshire ICS — integrated digital roadmap shapes shared-system amortisation"},
            {"label": "April 2025 NIC step-up", "value": "Indirect via supplier-side cost pass-through on SaaS uplifts"},
            {"label": "Funding trajectory", "value": "2021-22 c. £2.3M → 2023-24 c. £2.55M → 2024-25 £2.754M — Frontline Digitisation EPR build amort + ongoing software refresh"},
            {"label": "Delivery body", "value": "Trust IT + Finance (intangible register) + Cerner Oracle Health (EPR vendor) + NHSE Frontline Digitisation team"},
            {"label": "Policy owner", "value": "NHSE Transformation Directorate (Frontline Digitisation) + DHSC + NHSE Provider Finance + Joined Up Care Derbyshire ICB"},
            {"label": "Evaluation evidence", "value": "NAO Digital Transformation in the NHS 2020; NAO Frontline Digitisation 2023; Trust ARA 2023-24; CQC RTG inspections"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-merger separate Derby + Burton intangible registers · Successor: continued EPR amort cycle to ≈ 2030 + future SaaS-shift cost-of-revenue treatment"}
        ],
        "notes": "UHDB's amortisation line is dominated by capitalised intangibles from the Cerner Oracle Health EPR programme rolled out under NHSE's Frontline Digitisation initiative — internally generated software-build costs plus perpetual licence acquisitions feed straight-line amortisation under IAS 38. The 2018 merger of Derby Teaching Hospitals and Burton Hospitals consolidated the intangible asset register and exposed legacy useful-life heterogeneity that has since been rationalised. The trust sits inside Joined Up Care Derbyshire ICS, where shared digital roadmap decisions shape cross-trust intangible amortisation. April 2025 NIC step-up feeds indirect cost pass-through on SaaS contract uplifts. Future shift toward subscription-model SaaS will progressively reclassify spend away from intangible amort toward operating expense.",
        "sources": [
            {"publisher": "University Hospitals of Derby and Burton NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.uhdb.nhs.uk/annual-reports-publications"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/frontline-digitisation/"},
            {"publisher": "National Audit Office", "title": "Frontline Digitisation in the NHS (HC 1727, 2023)", "url": "https://www.nao.org.uk/reports/digital-transformation-in-the-nhs/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "UHDB NHS FT provider profile (RTG)", "url": "https://www.cqc.org.uk/provider/RTG"}
        ],
        "related": ["University Hospitals of Derby and Burton NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Amortisation — Whittington Health NHS Trust", "Amortisation — Kettering General Hospital NHS Foundation Trust", "Frontline Digitisation"]
    },
    "PFI / LIFT charges — Cambridge University Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "PFI / LIFT charges", "parent": "Cambridge University Hospitals NHS Foundation Trust"}],
        "description": "Cambridge University Hospitals' £2.746M PFI/LIFT charges line is a small residual relative to the trust's overall scale — Addenbrooke's and the Rosie Hospital are largely on-balance-sheet public capital, so this entry captures specific PFI/LIFT-funded enabling-works, ancillary clinic premises and integrated primary-care LIFT space rather than a flagship hospital concession. Charges combine the IFRIC 12 service-concession service fee, lifecycle pass-through and IFRS 16 lease component (post-2022 GAM treatment).",
        "beneficiaries": "c. 12,000 WTE staff serving a c. 750,000 Cambridgeshire catchment plus East of England tertiary referrals; c. 145,000 ED attendances/yr at Addenbrooke's ED; c. 110,000 admissions/yr; major regional trauma centre, transplant centre, paediatric oncology and Cambridge Biomedical Campus.",
        "legal_basis": "IFRIC 12 Service Concession Arrangements — IFRS 16 Leases (post-Apr 2022 DHSC GAM treatment) — DHSC PFI guidance — NHS Act 2006 — Health and Care Act 2022 — DHSC Group Accounting Manual 2024-25",
        "key_stats": [
            {"label": "PFI / LIFT charges 2024-25", "value": "£2.746M"},
            {"label": "Trust scale", "value": "Addenbrooke's Hospital + Rosie Hospital (Cambridge Biomedical Campus); c. 12,000 WTE"},
            {"label": "Concession scope", "value": "Residual PFI/LIFT charges — ancillary enabling-works + integrated primary-care LIFT space (NOT Addenbrooke's main hospital, which is on-balance-sheet)"},
            {"label": "Major specialty mix", "value": "Major Trauma Centre + transplant centre + paediatric oncology + Royal Papworth co-location + Cambridge Biomedical Campus"},
            {"label": "IFRS 16 transition (Apr 2022)", "value": "DHSC GAM moved IFRIC 12 lease element onto IFRS 16 lessee accounting — re-baselined service charge presentation"},
            {"label": "Composition", "value": "IFRIC 12 service-concession service fee + lifecycle pass-through + indexation (typ. RPI/CPI cap) + IFRS 16 lease component"},
            {"label": "April 2025 NIC step-up", "value": "Indirect via PFI service-provider pass-through on hard + soft FM"},
            {"label": "Funding trajectory", "value": "2021-22 c. £2.5M → 2023-24 c. £2.65M → 2024-25 £2.746M — RPI indexation + lifecycle drawdown timing"},
            {"label": "Delivery body", "value": "Trust E&F + PFI/LIFT SPV + hard/soft FM service provider + NHSE Provider Finance"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC PFI Centre of Best Practice + HM Treasury PPP team + Cambridgeshire and Peterborough ICB"},
            {"label": "Evaluation evidence", "value": "NAO PFI and PF2 (HC 718, 2018); NAO Investigation into the management of PFI contracts; Trust ARA 2023-24; CQC RGT inspections"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-LIFT primary-care premises baseline · Successor: PFI expiry + handback decisions late 2020s/2030s · NHP Reset Jan 2025 deferral implications"}
        ],
        "notes": "Cambridge University Hospitals' PFI/LIFT line is unusual because the flagship Addenbrooke's complex remains largely on-balance-sheet public capital — the line therefore captures residual LIFT premises (integrated primary-care space) and PFI-funded enabling-works rather than a single dominant hospital concession. The IFRS 16 transition in April 2022 (DHSC GAM treatment) moved the lease element of IFRIC 12 contracts onto lessee accounting, re-baselining service-charge presentation. Cambridge Biomedical Campus expansion plans interact with NHP Reset Jan 2025 deferral pressures on related capital. April 2025 NIC step-up (15%, £5k threshold) feeds forward indirect via FM service-provider pass-through; RPI/CPI indexation caps drive forward charge.",
        "sources": [
            {"publisher": "Cambridge University Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.cuh.nhs.uk/about-us/publications/annual-report-and-accounts/"},
            {"publisher": "National Audit Office", "title": "PFI and PF2 (HC 718, 2018)", "url": "https://www.nao.org.uk/reports/pfi-and-pf2/"},
            {"publisher": "HM Treasury", "title": "Private Finance Initiative — public-private partnerships data", "url": "https://www.gov.uk/government/collections/public-private-partnerships"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Cambridge University Hospitals NHS FT provider profile (RGT)", "url": "https://www.cqc.org.uk/provider/RGT"}
        ],
        "related": ["Cambridge University Hospitals NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "PFI / LIFT charges — The Royal Wolverhampton NHS Trust", "PFI / LIFT charges — Sherwood Forest Hospitals NHS Foundation Trust", "Private Finance Initiative"]
    },
    "Transport (business + patient) — Whittington Health NHS Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "Whittington Health NHS Trust"}],
        "description": "Whittington Health's £2.734M transport line covers business mileage (AfC Section 17 + HMRC AMAP), pool-fleet IFRS 16 lease costs, NEPTS contract pass-through and patient travel reimbursements across the Whittington Hospital (Archway, North London) acute site plus an extensive integrated community-services footprint across Islington and Haringey. The integrated acute-plus-community model drives heavy district-nurse and CCN business mileage on top of routine NEPTS volume. NEPTS is commissioned through the North Central London ICS lead-commissioner.",
        "beneficiaries": "c. 4,500 WTE staff serving a c. 500,000 Islington + Haringey + parts of Camden/Barnet catchment; c. 100,000 ED attendances/yr at Whittington ED; c. 50,000 admissions/yr; integrated community services (district nursing + CCN + sexual health) across Islington and Haringey.",
        "legal_basis": "NHS Act 2006 — NHSE Patient Transport Services Eligibility Criteria 2021 — Agenda for Change Section 17 (business mileage) — HMRC AMAP rates — IFRS 16 Leases (pool fleet) — DHSC Group Accounting Manual 2024-25 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£2.734M"},
            {"label": "Trust scale", "value": "Whittington Hospital (Archway) + integrated community services across Islington + Haringey; c. 4,500 WTE"},
            {"label": "Integrated acute + community", "value": "Combined acute-plus-community model — drives heavy district-nurse + CCN + sexual-health-clinic business mileage relative to peer single-site DGHs"},
            {"label": "NEPTS commissioning", "value": "North Central London ICS lead-commissioner NEPTS contract; eligibility per NHSE 2021 criteria"},
            {"label": "Composition", "value": "Business mileage (AfC S17 + AMAP 45p/25p frozen since 2011) + pool-fleet IFRS 16 leases + NEPTS pass-through + patient travel reimbursements + ULEZ pool-fleet conversion costs"},
            {"label": "ULEZ exposure", "value": "Inner-London Whittington Hospital + community fleet — ULEZ + emerging zero-emission-zone exposure drives pool-fleet conversion + replacement"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove cancellation rebooking + agency travel claims"},
            {"label": "April 2025 NIC + fuel CPI", "value": "Indirect via NEPTS contractor pass-through + diesel CPI feed forward unit-cost pressure"},
            {"label": "Funding trajectory", "value": "2021-22 c. £2.3M → 2023-24 c. £2.5M → 2024-25 £2.734M — fuel CPI + NEPTS uplift + community-mileage growth + ULEZ-conversion lease churn"},
            {"label": "Delivery body", "value": "Trust E&F + outsourced NEPTS provider (NCL ICS lead-commissioner) + pool-fleet leasing partner + Trust HR (mileage)"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + NHSE Urgent and Emergency Care (NEPTS) + North Central London ICB + DHSC + GLA (ULEZ)"},
            {"label": "Evaluation evidence", "value": "NAO NEPTS 2019; CQC RKE inspections; NHSE NEPTS Eligibility Review 2021; Trust ARA 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-ICS CCG-commissioned NEPTS contracts · Successor: NCL ICS-collaborative NEPTS retender + zero-emission-zone full pool-fleet conversion"}
        ],
        "notes": "Whittington Health's transport line is shaped by the trust's integrated acute-plus-community model — district-nursing, CCN, sexual-health and community paediatric services across Islington and Haringey generate heavy AfC Section 17 business-mileage demand on top of routine NEPTS volume. London ULEZ exposure (and GLA emerging zero-emission-zone planning) drives accelerated pool-fleet replacement with associated IFRS 16 lease-churn cost. NCL ICS lead-commissioner NEPTS contract covers routine eligibility-tier journeys with NHSE 2021 criteria tightening the patient-paid threshold. Industrial action 2023-24 drove cancellation rebooking and agency travel claims; HMRC AMAP-rate freeze (45p/mile since 2011) sustains internal-rate dispute pressure. April 2025 NIC step-up feeds forward via NEPTS contractor pass-through.",
        "sources": [
            {"publisher": "Whittington Health NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.whittington.nhs.uk/default.asp?c=33483"},
            {"publisher": "NHS England", "title": "Non-Emergency Patient Transport Services — National Framework + Eligibility Criteria 2021", "url": "https://www.england.nhs.uk/publication/non-emergency-patient-transport-services-nepts/"},
            {"publisher": "Greater London Authority", "title": "Ultra Low Emission Zone — London", "url": "https://tfl.gov.uk/modes/driving/ultra-low-emission-zone"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Whittington Health NHS Trust provider profile (RKE)", "url": "https://www.cqc.org.uk/provider/RKE"}
        ],
        "related": ["Whittington Health NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Transport (business + patient) — The Hillingdon Hospitals NHS Foundation Trust", "Amortisation — Whittington Health NHS Trust", "NHS England"]
    },
    "General supplies & services — Dorset County Hospital NHS Foundation Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "Dorset County Hospital NHS Foundation Trust"}],
        "description": "Dorset County Hospital's £2.734M general supplies & services line covers non-clinical consumables, stationery, uniforms, catering provisions, housekeeping consumables and miscellaneous trust-wide supplies across the Dorchester DGH single-site footprint plus satellite outpatient and renal-dialysis sites across rural West Dorset. As a small DGH on the New Hospital Programme cohort with constrained estate and significant rural geography, the trust faces unit-cost pressure from low-volume ordering and long supply-chain logistics relative to peer urban DGHs.",
        "beneficiaries": "c. 2,500 WTE staff serving a c. 215,000 West Dorset catchment (Dorchester, Weymouth, Bridport, rural West Dorset); c. 60,000 ED attendances/yr at Dorset County ED; c. 30,000 admissions/yr; rural geography — long supply-chain logistics for satellite renal-dialysis + outpatient sites.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) — IAS 2 Inventories (interaction) — NHS Act 2006 — Health and Care Act 2022 — Public Contracts Regulations 2015 (procurement) — NHS Supply Chain framework",
        "key_stats": [
            {"label": "General supplies & services 2024-25", "value": "£2.734M"},
            {"label": "Trust scale", "value": "Dorset County Hospital (Dorchester) + satellite outpatient + renal-dialysis sites across West Dorset; c. 2,500 WTE"},
            {"label": "Composition", "value": "Non-clinical consumables + stationery + uniforms + catering provisions + housekeeping consumables + miscellaneous trust-wide supplies"},
            {"label": "Procurement route", "value": "NHS Supply Chain (Future Operating Model categories) for c. 60-70%; remainder direct + framework call-off"},
            {"label": "New Hospital Programme cohort", "value": "Dorset County Hospital is on the NHP cohort (RAAC + structural) — Reset Jan 2025 deferred construction timeline; supply-chain disruption ahead during decant"},
            {"label": "Rural geography premium", "value": "Low-volume ordering + long supply-chain logistics across West Dorset rural footprint drive unit-cost premium relative to peer urban DGHs"},
            {"label": "April 2025 NIC step-up", "value": "Indirect via supplier-side cost pass-through on consumable + catering category contracts"},
            {"label": "Funding trajectory", "value": "2021-22 c. £2.4M → 2023-24 c. £2.6M → 2024-25 £2.734M — CPI on consumables + NHS Supply Chain category-management uplifts"},
            {"label": "Delivery body", "value": "Trust Procurement + NHS Supply Chain (Future Operating Model) + DHSC Commercial + ICS-led collaborative procurement (Dorset ICS)"},
            {"label": "Policy owner", "value": "NHSE Commercial + DHSC + Dorset ICB + Cabinet Office Commercial Function + NHP delivery (rebuild)"},
            {"label": "Evaluation evidence", "value": "NAO Procurement in the NHS 2019; NAO Future Operating Model 2022; Trust ARA 2023-24; CQC RBD inspections"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-Future Operating Model fragmented procurement · Successor: NHS Supply Chain category-tower consolidation + NHP rebuild supply-chain reset"}
        ],
        "notes": "Dorset County Hospital's general supplies line carries a structural unit-cost premium driven by rural West Dorset geography — low-volume ordering and long supply-chain logistics across satellite renal-dialysis and outpatient sites generate higher per-item delivery and stocking cost relative to peer urban DGHs. The trust's New Hospital Programme position (Reset Jan 2025 deferral) places future supply-chain disruption around decant and rebuild on the medium-term horizon. NHS Supply Chain Future Operating Model category-tower consolidation continues to absorb fragmented purchasing into national framework call-off. April 2025 employer NIC step-up (15%, £5k threshold) feeds forward via supplier-side pass-through on consumable and catering category contracts.",
        "sources": [
            {"publisher": "Dorset County Hospital NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.dchft.nhs.uk/about-us/Pages/Annual-Reports-and-Accounts.aspx"},
            {"publisher": "NHS Supply Chain", "title": "Future Operating Model — category-tower structure", "url": "https://www.supplychain.nhs.uk/"},
            {"publisher": "National Audit Office", "title": "Procurement in the NHS (HC 1531, 2019)", "url": "https://www.nao.org.uk/reports/the-supply-of-everyday-healthcare-items-to-the-nhs/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Dorset County Hospital NHS FT provider profile (RBD)", "url": "https://www.cqc.org.uk/provider/RBD"}
        ],
        "related": ["Dorset County Hospital NHS Foundation Trust", "Clinical Supplies & Drugs", "NHS Acute Trusts", "General supplies & services — Isle of Wight NHS Trust", "Premises & Infrastructure — Dorset County Hospital NHS Foundation Trust", "NHS Supply Chain"]
    },
    "Termination & post-employment — Northern Care Alliance NHS Foundation Trust": {
        "aliases": [{"name": "Termination & post-employment", "parent": "Northern Care Alliance NHS Foundation Trust"}],
        "description": "Northern Care Alliance's £2.733M termination & post-employment line covers IAS 19 termination benefits (redundancies, MARS-style mutually agreed resignations and end-of-contract settlements) plus actuarial movement on post-employment defined-benefit obligations across the Salford Royal + Royal Oldham + Fairfield General + Rochdale Infirmary footprint. NCA is one of the largest acute groups in England, formed October 2021 from the merger of Salford Royal NHS FT and Pennine Acute Hospitals — ongoing post-merger workforce harmonisation and specialty consolidation feed redundancy provisions.",
        "beneficiaries": "c. 20,000 WTE staff serving a c. 1.0M Greater Manchester catchment (Salford, Oldham, Bury, Rochdale); c. 320,000 ED attendances/yr (Salford Royal + Royal Oldham + Fairfield + Rochdale combined); c. 220,000 admissions/yr; one of England's largest acute groups; major neurosciences + Major Trauma Centre at Salford Royal.",
        "legal_basis": "IAS 19 Employee Benefits — NHS Pension Scheme Regulations — Public Sector Exit Payments Regulations 2020 (and 2021 revocation; HMT cap reinstatement still under consultation) — DHSC Group Accounting Manual 2024-25 — NHS Act 2006",
        "key_stats": [
            {"label": "Termination & post-employment 2024-25", "value": "£2.733M"},
            {"label": "Trust scale", "value": "Salford Royal + Royal Oldham + Fairfield General + Rochdale Infirmary; c. 20,000 WTE — one of England's largest acute groups"},
            {"label": "Merger origin", "value": "NCA formed 1 Oct 2021 — Salford Royal NHS FT + Pennine Acute Hospitals NHS Trust merger; ongoing workforce harmonisation feeds redundancy provisions"},
            {"label": "Composition", "value": "IAS 19 termination benefits (redundancies + MARS-style + end-of-contract settlements) + actuarial movement on post-employment DB obligations"},
            {"label": "NHS Pension Scheme", "value": "Most NHS staff in NHS Pension Scheme — DB scheme accounted via funded employer contribution; small residual DB (legacy) at trust level"},
            {"label": "Post-merger consolidation", "value": "Specialty consolidation Salford Royal ↔ Pennine sites (e.g. neurosciences concentration) drives ongoing redundancy + redeployment"},
            {"label": "Public Sector Exit Payments", "value": "2020 £95k cap revoked Feb 2021; HMT consulted on revised cap; current £80k MARS scheme guidance applies"},
            {"label": "April 2025 NIC step-up", "value": "Direct hit on cost-of-employment + indirect on redundancy NIC component"},
            {"label": "Funding trajectory", "value": "2021-22 (post-merger) elevated → 2023-24 c. £2.5M → 2024-25 £2.733M — phase-out of merger redundancy peak; ongoing consolidation"},
            {"label": "Delivery body", "value": "Trust HR + NHSBSA Pensions + actuarial advisor (Government Actuary's Department for scheme actuarial) + NHS Resolution (employer liability)"},
            {"label": "Policy owner", "value": "DHSC + HM Treasury (exit payments cap policy) + NHSE Provider Finance + Greater Manchester ICB"},
            {"label": "Evaluation evidence", "value": "NAO NHS Workforce 2020; HMT Public Sector Exit Payments consultation; Trust ARA 2023-24; CQC RM3 inspections"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2021 separate Salford Royal + Pennine Acute baselines · Successor: continued specialty consolidation + Greater Manchester Provider Collaborative workforce strategy"}
        ],
        "notes": "Northern Care Alliance's termination line carries the residual post-merger workforce-harmonisation cost from the October 2021 unification of Salford Royal and Pennine Acute Hospitals — ongoing specialty consolidation across the four-site footprint (Salford concentrates neurosciences and Major Trauma; Oldham/Fairfield/Rochdale absorb DGH activity) drives redundancy and redeployment provisions. HMT's Public Sector Exit Payments £95k cap was revoked February 2021 and remains under consultation, with the £80k MARS scheme guidance currently applicable. April 2025 employer NIC step-up (15%, £5k threshold) hits cost-of-employment directly and indirectly through the redundancy NIC component. Greater Manchester Provider Collaborative shapes future workforce strategy beyond NCA's own ARA.",
        "sources": [
            {"publisher": "Northern Care Alliance NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://northerncarealliance.nhs.uk/about-us/our-publications"},
            {"publisher": "HM Treasury", "title": "Public sector exit payments — guidance", "url": "https://www.gov.uk/government/publications/public-sector-exit-payments-guidance-on-special-severance-payments"},
            {"publisher": "NHS Business Services Authority", "title": "NHS Pension Scheme — employer guide", "url": "https://www.nhsbsa.nhs.uk/employer-hub"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Northern Care Alliance NHS FT provider profile (RM3)", "url": "https://www.cqc.org.uk/provider/RM3"}
        ],
        "related": ["Northern Care Alliance NHS Foundation Trust", "Staff Costs", "NHS Acute Trusts", "Premises (other) — Northern Care Alliance NHS Foundation Trust", "NHS Pension Scheme", "Public Sector Exit Payments"]
    },
    "Business rates — Bedfordshire Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "Bedfordshire Hospitals NHS Foundation Trust"}],
        "description": "Bedfordshire Hospitals' £2.732M business-rates line covers non-domestic rates on the Bedford Hospital and Luton & Dunstable Hospital sites following the April 2020 merger of the two trusts. The Valuation Office Agency assesses rateable values (2023 list effective 1 April 2023) and Bedford Borough Council and Luton Borough Council bill respectively. NHS trusts pay the full multiplier with no charitable 80% relief, making the line sensitive to the 2023 revaluation, transitional uplifts and the Non-Domestic Rating (Multipliers and Private Finance) Act 2024.",
        "beneficiaries": "c. 7,500 WTE staff serving a c. 700,000 Bedfordshire and Luton catchment (Bedford, Luton, Dunstable, Mid Bedfordshire); c. 200,000 ED attendances/yr (Bedford ED + L&D ED — both very busy); c. 105,000 admissions/yr; integrated post-merger 2020 footprint.",
        "legal_basis": "Local Government Finance Act 1988 (Schedule 6) — Non-Domestic Rating (Multipliers and Private Finance) Act 2024 — Non-Domestic Rating Act 2023 — DHSC Group Accounting Manual 2024-25 — NHS Act 2006 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£2.732M"},
            {"label": "Trust scale", "value": "Bedford Hospital + Luton & Dunstable Hospital (post-Apr 2020 merger); c. 7,500 WTE"},
            {"label": "Billing authorities", "value": "Bedford Borough Council (Bedford Hospital) + Luton Borough Council (L&D Hospital)"},
            {"label": "2023 revaluation", "value": "VOA 2023 revaluation (effective 1 Apr 2023) re-set rateable values from 2017 list — transitional uplift on East of England hereditaments"},
            {"label": "Multiplier 2024-25", "value": "Standard non-domestic multiplier 54.6p (England, 2024-25); NHS pays full rate (no charitable relief); NDR 2024 Act splits multipliers"},
            {"label": "Merger origin", "value": "Bedford Hospital NHS Trust + L&D University Hospital NHS FT merged Apr 2020 — combined rates ledger from that date"},
            {"label": "L&D refurbishment / NHP", "value": "Luton & Dunstable on NHP cohort under previous schedule — Reset Jan 2025 deferred; affects future hereditament mix"},
            {"label": "Funding trajectory", "value": "2021-22 (post-merger) c. £2.4M → 2023-24 c. £2.6M → 2024-25 £2.732M — multiplier + transitional uplift"},
            {"label": "Delivery body", "value": "Trust E&F (rates appeals) + Valuation Office Agency + Bedford Borough Council + Luton Borough Council"},
            {"label": "Policy owner", "value": "MHCLG (NDR policy) + HM Treasury + DHSC + NHSE Provider Finance + Bedfordshire, Luton and Milton Keynes ICB"},
            {"label": "Evaluation evidence", "value": "VOA Rating List 2023; NAO Business Rates Reform; Trust ARA 2023-24; CQC RC9 inspections"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2020 separate Bedford + L&D rates ledgers · Successor: 2026 revaluation cycle + NDR 2024 Act multiplier-split implementation + NHP rebuild rateable-value reset"}
        ],
        "notes": "Bedfordshire Hospitals' rates line carries two distinct hereditaments under separate billing authorities (Bedford Borough Council for Bedford Hospital, Luton Borough Council for Luton & Dunstable) with combined ledger management since the April 2020 merger. The VOA 2023 revaluation lifted rateable values across the East of England estate with transitional relief tapering, while the Non-Domestic Rating (Multipliers and Private Finance) Act 2024 introduces a multiplier split that reshapes future bills for large hereditaments. Luton & Dunstable's New Hospital Programme position (Reset Jan 2025 deferral) shapes future hereditament mix as rebuild and demolition reshape the rateable footprint. NHS pays the full 54.6p standard multiplier with no charitable relief.",
        "sources": [
            {"publisher": "Bedfordshire Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.bedfordshirehospitals.nhs.uk/about-us/publications/"},
            {"publisher": "Valuation Office Agency", "title": "2023 Rating List", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "Ministry of Housing, Communities and Local Government", "title": "Non-Domestic Rating Act 2023 + Multipliers and Private Finance Act 2024", "url": "https://www.gov.uk/government/collections/business-rates"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Bedfordshire Hospitals NHS FT provider profile (RC9)", "url": "https://www.cqc.org.uk/provider/RC9"}
        ],
        "related": ["Bedfordshire Hospitals NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Business rates — Lancashire Teaching Hospitals NHS Foundation Trust", "Business rates — Royal Devon University Healthcare NHS Foundation Trust", "Valuation Office Agency"]
    },
    "Establishment costs — Mid Cheshire Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "Mid Cheshire Hospitals NHS Foundation Trust"}],
        "description": "Mid Cheshire's £2.73M establishment costs line covers postage, telecoms, courier, training and development, printing, recruitment advertising and broader trust-running corporate-services consumption across the Leighton Hospital (Crewe) main site + Victoria Infirmary Northwich + Elmhurst Intermediate Care Centre + community footprint. Leighton Hospital is on the New Hospital Programme cohort due to RAAC concrete-plank failure risk, and is one of the seven trusts NAO highlighted as priority for rebuild — driving distinctive establishment-cost pressures around decant communications, recruitment retention and project-management training.",
        "beneficiaries": "c. 5,000 WTE staff serving a c. 320,000 South Cheshire and Vale Royal catchment (Crewe, Nantwich, Northwich, Winsford); c. 95,000 ED attendances/yr at Leighton ED; c. 55,000 admissions/yr; Leighton Hospital is among the seven priority RAAC-affected trusts in the NHP rebuild cohort.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) — IAS 1 Presentation of Financial Statements — NHS Act 2006 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£2.73M"},
            {"label": "Trust scale", "value": "Leighton Hospital (Crewe) + Victoria Infirmary Northwich + Elmhurst Intermediate Care Centre; c. 5,000 WTE"},
            {"label": "RAAC + NHP priority", "value": "Leighton Hospital among seven RAAC-priority trusts on HSSIB Sep 2023 list — NHP cohort full rebuild target; Reset Jan 2025 confirmed Leighton in priority tranche"},
            {"label": "Composition", "value": "Postage + telecoms + courier + training and development + printing + recruitment advertising + corporate-services consumption"},
            {"label": "Frontline Digitisation EPR", "value": "Mid Cheshire on Frontline Digitisation programme — training and change-management feeds establishment line during EPR rollout"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove communications + cancellation rebooking + agency-recruitment advertising"},
            {"label": "April 2025 NIC step-up", "value": "Indirect via supplier-side cost pass-through on telecoms + courier + training contracts"},
            {"label": "Funding trajectory", "value": "2021-22 c. £2.3M → 2023-24 c. £2.55M → 2024-25 £2.73M — RAAC programme communications + EPR training + recruitment advertising"},
            {"label": "Delivery body", "value": "Trust Corporate Services + Trust IT (telecoms) + Trust HR (training + recruitment) + NHP delivery team"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + NHP delivery + Cheshire and Merseyside ICB + NHSE Transformation (Frontline Digitisation)"},
            {"label": "Evaluation evidence", "value": "HSSIB RAAC report Sep 2023; NAO NHP 2025; Trust ARA 2023-24; CQC RBT inspections"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-RAAC-emergence baseline · Successor: full rebuild Leighton Hospital under NHP + EPR steady-state amort"}
        ],
        "notes": "Mid Cheshire's establishment line is shaped by the Leighton Hospital RAAC crisis — the trust is on HSSIB's September 2023 priority list for concrete-plank failure risk and is one of the seven trusts NHP Reset (Jan 2025) confirmed in the priority rebuild tranche. Decant communications, recruitment retention advertising and project-management training feed distinctive establishment-cost pressure on top of routine corporate-services consumption. Frontline Digitisation EPR rollout adds training and change-management cost. Industrial action 2023-24 drove communications and agency-recruitment advertising. April 2025 NIC step-up (15%, £5k threshold) feeds forward via supplier-side pass-through on telecoms, courier and training contracts.",
        "sources": [
            {"publisher": "Mid Cheshire Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.mcht.nhs.uk/about-us/publications/annual-reports/"},
            {"publisher": "Health Services Safety Investigations Body", "title": "RAAC and the safety of NHS hospital buildings (2023)", "url": "https://www.hssib.org.uk/"},
            {"publisher": "Department of Health and Social Care", "title": "New Hospital Programme — Plan for Implementation (Jan 2025 Reset)", "url": "https://www.gov.uk/government/publications/new-hospital-programme-plan-for-implementation"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Mid Cheshire Hospitals NHS FT provider profile (RBT)", "url": "https://www.cqc.org.uk/provider/RBT"}
        ],
        "related": ["Mid Cheshire Hospitals NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "New Hospital Programme", "RAAC remediation", "Frontline Digitisation"]
    },
    "Business rates — Lancashire Teaching Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "Lancashire Teaching Hospitals NHS Foundation Trust"}],
        "description": "Lancashire Teaching Hospitals' £2.718M business-rates line covers non-domestic rates on the Royal Preston Hospital and Chorley & South Ribble Hospital sites plus ancillary education and outpatient premises across central Lancashire. The Valuation Office Agency assesses rateable values (2023 list effective 1 April 2023) and Preston City Council and Chorley Council bill respectively. The trust hosts the major Specialised Mobility and Rehabilitation Centre and Major Trauma Centre at Royal Preston, with substantial tertiary-specialty hereditament weight.",
        "beneficiaries": "c. 8,500 WTE staff serving a c. 380,000 central Lancashire catchment plus regional tertiary referrals from Lancashire and South Cumbria ICS (c. 1.7M tertiary catchment); c. 165,000 ED attendances/yr (Preston ED + Chorley UTC); c. 95,000 admissions/yr; Major Trauma Centre + Specialised Mobility Rehabilitation Centre at Royal Preston.",
        "legal_basis": "Local Government Finance Act 1988 (Schedule 6) — Non-Domestic Rating (Multipliers and Private Finance) Act 2024 — Non-Domestic Rating Act 2023 — DHSC Group Accounting Manual 2024-25 — NHS Act 2006 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£2.718M"},
            {"label": "Trust scale", "value": "Royal Preston Hospital + Chorley & South Ribble Hospital + ancillary education + outpatient premises; c. 8,500 WTE"},
            {"label": "Tertiary specialty", "value": "Major Trauma Centre + Specialised Mobility and Rehabilitation Centre + neurosciences — substantial tertiary hereditament weight at Royal Preston"},
            {"label": "Billing authorities", "value": "Preston City Council (Royal Preston) + Chorley Council (Chorley & South Ribble Hospital)"},
            {"label": "2023 revaluation", "value": "VOA 2023 revaluation (effective 1 Apr 2023) re-set rateable values from 2017 list — transitional uplift on North West hereditaments"},
            {"label": "Multiplier 2024-25", "value": "Standard non-domestic multiplier 54.6p (England, 2024-25); NHS pays full rate (no charitable relief); NDR 2024 Act splits multipliers"},
            {"label": "NHP Royal Preston", "value": "Royal Preston is on the NHP cohort — Reset Jan 2025 deferred construction; future hereditament reset on rebuild"},
            {"label": "Funding trajectory", "value": "2021-22 c. £2.5M → 2023-24 c. £2.6M → 2024-25 £2.718M — multiplier + transitional uplift + tertiary expansion"},
            {"label": "Delivery body", "value": "Trust E&F (rates appeals) + Valuation Office Agency + Preston City Council + Chorley Council"},
            {"label": "Policy owner", "value": "MHCLG (NDR policy) + HM Treasury + DHSC + NHSE Provider Finance + Lancashire and South Cumbria ICB"},
            {"label": "Evaluation evidence", "value": "VOA Rating List 2023; NAO Business Rates Reform; Trust ARA 2023-24; CQC RXN inspections"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2023-list baseline · Successor: 2026 revaluation cycle + NDR 2024 Act multiplier-split + NHP Royal Preston rebuild rateable-value reset"}
        ],
        "notes": "Lancashire Teaching Hospitals' rates line is weighted by the tertiary-specialty hereditament profile at Royal Preston — Major Trauma Centre, Specialised Mobility and Rehabilitation Centre and neurosciences carry higher per-square-metre rateable value than peer DGH hereditaments. The VOA 2023 revaluation lifted North West rateable values with transitional relief tapering, while the Non-Domestic Rating (Multipliers and Private Finance) Act 2024 introduces a multiplier-split that reshapes large-hereditament bills. Royal Preston's New Hospital Programme position (Reset Jan 2025 deferral) places future hereditament reset on the medium-term horizon as rebuild proposals advance. NHS pays the full 54.6p standard multiplier with no charitable relief.",
        "sources": [
            {"publisher": "Lancashire Teaching Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.lancsteachinghospitals.nhs.uk/annual-reports"},
            {"publisher": "Valuation Office Agency", "title": "2023 Rating List", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "Ministry of Housing, Communities and Local Government", "title": "Non-Domestic Rating Act 2023 + Multipliers and Private Finance Act 2024", "url": "https://www.gov.uk/government/collections/business-rates"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Lancashire Teaching Hospitals NHS FT provider profile (RXN)", "url": "https://www.cqc.org.uk/provider/RXN"}
        ],
        "related": ["Lancashire Teaching Hospitals NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Business rates — Bedfordshire Hospitals NHS Foundation Trust", "Business rates — Royal Devon University Healthcare NHS Foundation Trust", "Valuation Office Agency"]
    },
    "General supplies & services — Isle of Wight NHS Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "Isle of Wight NHS Trust"}],
        "description": "Isle of Wight NHS Trust's £2.713M general supplies & services line covers non-clinical consumables, stationery, uniforms, catering provisions and housekeeping supplies across the unique integrated acute + community + mental health + ambulance footprint at St Mary's Hospital (Newport) plus community sites across the island. As one of England's only fully integrated acute-community-mental-health-ambulance providers and serving an island geography, the trust faces structural unit-cost pressure from sea-freight logistics, low-volume ordering and constrained supplier-substitution options.",
        "beneficiaries": "c. 3,200 WTE staff serving a c. 140,000 island population (plus c. 2.5M summer visitor surge); c. 50,000 ED attendances/yr at St Mary's ED; c. 28,000 admissions/yr; unique integrated acute + community + mental health + ambulance footprint covering 380 km² island.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) — IAS 2 Inventories (interaction) — NHS Act 2006 — Health and Care Act 2022 — Public Contracts Regulations 2015 (procurement) — NHS Supply Chain framework",
        "key_stats": [
            {"label": "General supplies & services 2024-25", "value": "£2.713M"},
            {"label": "Trust scale", "value": "St Mary's Hospital (Newport) + community sites + ambulance + mental health across 380 km² Isle of Wight; c. 3,200 WTE"},
            {"label": "Integrated provider model", "value": "One of England's only fully integrated acute + community + mental health + ambulance providers — drives unique supply-chain category mix"},
            {"label": "Island geography premium", "value": "Sea-freight logistics (Wightlink + Red Funnel + ferry surcharges) + constrained supplier substitution drive structural unit-cost premium relative to mainland peers"},
            {"label": "Composition", "value": "Non-clinical consumables + stationery + uniforms + catering provisions + housekeeping supplies + courier surcharges"},
            {"label": "Procurement route", "value": "NHS Supply Chain (Future Operating Model) — but freight surcharges erode framework saving; ICS-led collaborative procurement (Hampshire and Isle of Wight ICS)"},
            {"label": "Mainland-trust partnership", "value": "Acute mainland-tertiary partnership with Portsmouth Hospitals University NHS Trust + UHS — drives cross-Solent supply transfers + courier costs"},
            {"label": "April 2025 NIC step-up", "value": "Indirect via supplier-side cost pass-through on consumable + catering category contracts + ferry-operator surcharges"},
            {"label": "Funding trajectory", "value": "2021-22 c. £2.4M → 2023-24 c. £2.55M → 2024-25 £2.713M — CPI on consumables + ferry-surcharge inflation + summer-visitor activity surge"},
            {"label": "Delivery body", "value": "Trust Procurement + NHS Supply Chain (Future Operating Model) + ICS-led collaborative procurement (HIOW ICS) + ferry-freight contractors"},
            {"label": "Policy owner", "value": "NHSE Commercial + DHSC + Hampshire and Isle of Wight ICB + Cabinet Office Commercial Function"},
            {"label": "Evaluation evidence", "value": "NAO Procurement in the NHS 2019; NAO Future Operating Model 2022; Trust ARA 2023-24; CQC R1F inspections"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-Future Operating Model fragmented procurement · Successor: HIOW ICS-collaborative integration + cross-Solent logistics rationalisation"}
        ],
        "notes": "Isle of Wight NHS Trust's general supplies line carries a unique structural premium driven by both island geography (sea-freight logistics with Wightlink and Red Funnel ferry surcharges; constrained supplier-substitution; long lead times) and the unusually broad integrated provider model spanning acute + community + mental health + ambulance — the only fully integrated mainland-equivalent FT in England. NHS Supply Chain Future Operating Model framework saving is partially eroded by freight surcharges. Cross-Solent partnership with Portsmouth Hospitals and UHS drives mainland-tertiary supply transfers. Summer visitor surge (c. 2.5M visitors/yr against 140k resident population) drives episodic demand spikes. April 2025 NIC step-up feeds forward via supplier-side and ferry-operator surcharge pass-through.",
        "sources": [
            {"publisher": "Isle of Wight NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.iow.nhs.uk/About-Us/publications/Annual-Reports/Annual-Report.htm"},
            {"publisher": "NHS Supply Chain", "title": "Future Operating Model — category-tower structure", "url": "https://www.supplychain.nhs.uk/"},
            {"publisher": "National Audit Office", "title": "Procurement in the NHS (HC 1531, 2019)", "url": "https://www.nao.org.uk/reports/the-supply-of-everyday-healthcare-items-to-the-nhs/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Isle of Wight NHS Trust provider profile (R1F)", "url": "https://www.cqc.org.uk/provider/R1F"}
        ],
        "related": ["Isle of Wight NHS Trust", "Clinical Supplies & Drugs", "NHS Acute Trusts", "General supplies & services — Dorset County Hospital NHS Foundation Trust", "Premises (other) — Isle of Wight NHS Trust", "NHS Supply Chain"]
    },
    "PFI / LIFT charges — The Royal Wolverhampton NHS Trust": {
        "aliases": [{"name": "PFI / LIFT charges", "parent": "The Royal Wolverhampton NHS Trust"}],
        "description": "RWT's £2.709M PFI/LIFT charges line covers ancillary PFI and integrated primary-care LIFT premises across the New Cross Hospital + Cannock Chase Hospital + West Park Hospital + extensive vertical-integration GP-practice estate footprint. New Cross main hospital is largely on-balance-sheet public capital, so this entry captures LIFT-funded primary-care premises (one of the NHS's largest vertical-integration GP-practice estates) and ancillary enabling-works. Charges combine the IFRIC 12 service-concession service fee, lifecycle pass-through and IFRS 16 lease component (post-2022 GAM treatment).",
        "beneficiaries": "c. 9,500 WTE staff serving a c. 470,000 Wolverhampton + Cannock Chase catchment plus integrated primary-care registered c. 65,000 patients (vertical-integration GP-practice model); c. 165,000 ED attendances/yr at New Cross ED; c. 95,000 admissions/yr.",
        "legal_basis": "IFRIC 12 Service Concession Arrangements — IFRS 16 Leases (post-Apr 2022 DHSC GAM treatment) — DHSC PFI guidance — DHSC LIFT guidance — NHS Act 2006 — Health and Care Act 2022 — DHSC Group Accounting Manual 2024-25",
        "key_stats": [
            {"label": "PFI / LIFT charges 2024-25", "value": "£2.709M"},
            {"label": "Trust scale", "value": "New Cross Hospital + Cannock Chase Hospital + West Park Hospital + extensive vertical-integration GP-practice estate; c. 9,500 WTE"},
            {"label": "Concession scope", "value": "Residual PFI/LIFT charges — vertical-integration GP-practice LIFT premises + ancillary enabling-works (NOT New Cross main hospital, which is on-balance-sheet)"},
            {"label": "Vertical integration", "value": "RWT operates one of NHS's largest vertical-integration GP-practice estates — drives LIFT-premises footprint distinctive among Acute trusts"},
            {"label": "IFRS 16 transition (Apr 2022)", "value": "DHSC GAM moved IFRIC 12 lease element onto IFRS 16 lessee accounting — re-baselined service charge presentation"},
            {"label": "Composition", "value": "IFRIC 12 service-concession service fee + lifecycle pass-through + indexation (typ. RPI/CPI cap) + IFRS 16 lease component"},
            {"label": "Cannock Chase acquisition", "value": "Cannock Chase Hospital acquired Nov 2014 from Mid Staffs dissolution — added Cannock-related concession/LIFT exposure"},
            {"label": "April 2025 NIC step-up", "value": "Indirect via PFI service-provider pass-through on hard + soft FM"},
            {"label": "Funding trajectory", "value": "2021-22 c. £2.4M → 2023-24 c. £2.6M → 2024-25 £2.709M — RPI indexation + lifecycle drawdown + LIFT estate growth"},
            {"label": "Delivery body", "value": "Trust E&F + LIFT SPV + hard/soft FM service provider + Community Health Partnerships (LIFT national)"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC PFI Centre of Best Practice + HM Treasury PPP team + Black Country ICB + Community Health Partnerships"},
            {"label": "Evaluation evidence", "value": "NAO PFI and PF2 (HC 718, 2018); NAO LIFT 2010; Trust ARA 2023-24; CQC RL4 inspections"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-LIFT primary-care premises baseline · Successor: LIFT contract expiry + handback decisions late 2020s/2030s"}
        ],
        "notes": "RWT's PFI/LIFT line is shaped by the trust's distinctive vertical-integration GP-practice model — RWT operates one of the NHS's largest vertical-integration GP estates, absorbing primary-care premises (often LIFT-funded) into its asset register and concession-charge footprint. New Cross Hospital remains largely on-balance-sheet public capital. The IFRS 16 transition in April 2022 (DHSC GAM treatment) moved the lease element of IFRIC 12 contracts onto lessee accounting, re-baselining service-charge presentation. Cannock Chase Hospital acquisition (Nov 2014 from Mid Staffs dissolution) added Cannock-related concession/LIFT exposure. April 2025 NIC step-up (15%, £5k threshold) feeds forward indirect via FM service-provider pass-through; RPI/CPI indexation caps drive forward charge.",
        "sources": [
            {"publisher": "The Royal Wolverhampton NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.royalwolverhampton.nhs.uk/about-us/our-publications/annual-reports/"},
            {"publisher": "Community Health Partnerships", "title": "LIFT national programme", "url": "https://communityhealthpartnerships.co.uk/"},
            {"publisher": "National Audit Office", "title": "PFI and PF2 (HC 718, 2018)", "url": "https://www.nao.org.uk/reports/pfi-and-pf2/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "The Royal Wolverhampton NHS Trust provider profile (RL4)", "url": "https://www.cqc.org.uk/provider/RL4"}
        ],
        "related": ["The Royal Wolverhampton NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "PFI / LIFT charges — Cambridge University Hospitals NHS Foundation Trust", "Business rates — The Royal Wolverhampton NHS Trust", "Private Finance Initiative"]
    },
    "Business rates — Royal Devon University Healthcare NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "Royal Devon University Healthcare NHS Foundation Trust"}],
        "description": "Royal Devon's £2.685M business-rates line covers non-domestic rates on the Royal Devon and Exeter (Wonford) main site + North Devon District Hospital (Barnstaple) following the April 2022 merger plus an unusually broad community premises footprint across Devon. Multiple billing authorities (Exeter City Council, North Devon Council, East Devon District Council, Mid Devon District Council and Torridge District Council) collect non-domestic rates on a hereditament base spanning two acute hospitals, community hospitals and primary-care premises.",
        "beneficiaries": "c. 14,000 WTE staff serving a c. 615,000 Devon catchment (Exeter, East Devon, North Devon, Mid Devon, Torridge) plus regional tertiary referrals; c. 165,000 ED attendances/yr (RDE Wonford ED + NDDH Barnstaple ED); c. 95,000 admissions/yr; integrated acute + community footprint post-merger 2022.",
        "legal_basis": "Local Government Finance Act 1988 (Schedule 6) — Non-Domestic Rating (Multipliers and Private Finance) Act 2024 — Non-Domestic Rating Act 2023 — DHSC Group Accounting Manual 2024-25 — NHS Act 2006 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£2.685M"},
            {"label": "Trust scale", "value": "Royal Devon and Exeter Hospital (Wonford) + North Devon District Hospital (Barnstaple) + community hospitals across Devon; c. 14,000 WTE"},
            {"label": "Merger origin", "value": "RD&E + Northern Devon Healthcare merged 1 Apr 2022 — combined rates ledger from that date; broad rural community-hospital hereditament base"},
            {"label": "Billing authorities", "value": "Exeter City Council + North Devon Council + East Devon District Council + Mid Devon District Council + Torridge District Council — five local billing authorities"},
            {"label": "2023 revaluation", "value": "VOA 2023 revaluation (effective 1 Apr 2023) re-set rateable values from 2017 list — transitional uplift on South West hereditaments"},
            {"label": "Multiplier 2024-25", "value": "Standard non-domestic multiplier 54.6p (England, 2024-25); NHS pays full rate (no charitable relief); NDR 2024 Act splits multipliers"},
            {"label": "NHP cohort", "value": "RD&E was on the NHP cohort under previous schedule — Reset Jan 2025 deferred construction; future hereditament reset on rebuild"},
            {"label": "Funding trajectory", "value": "2021-22 (pre-merger) baseline → 2023-24 c. £2.55M → 2024-25 £2.685M — multiplier + transitional uplift + post-merger consolidated ledger"},
            {"label": "Delivery body", "value": "Trust E&F (rates appeals) + Valuation Office Agency + five Devon billing authorities (Exeter City, North Devon, East Devon, Mid Devon, Torridge)"},
            {"label": "Policy owner", "value": "MHCLG (NDR policy) + HM Treasury + DHSC + NHSE Provider Finance + Devon ICB"},
            {"label": "Evaluation evidence", "value": "VOA Rating List 2023; NAO Business Rates Reform; Trust ARA 2023-24; CQC RH8 inspections"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2022 separate RD&E + Northern Devon rates ledgers · Successor: 2026 revaluation cycle + NDR 2024 Act multiplier-split + NHP rebuild rateable-value reset"}
        ],
        "notes": "Royal Devon's rates line carries an unusually broad rural community-hospital hereditament base since the April 2022 merger of Royal Devon and Exeter NHS FT with Northern Devon Healthcare NHS Trust — the trust now spans two acute hospitals (Wonford, Barnstaple) plus multiple community hospitals across Devon, billed by five local authorities (Exeter City, North Devon, East Devon, Mid Devon, Torridge). The VOA 2023 revaluation lifted South West rateable values with transitional relief tapering, and NDR 2024 Act multiplier-split reform reshapes future bills for large hereditaments. The Wonford site's New Hospital Programme position (Reset Jan 2025 deferral) places future hereditament reset on the medium-term horizon. NHS pays full 54.6p standard multiplier with no charitable relief.",
        "sources": [
            {"publisher": "Royal Devon University Healthcare NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.royaldevon.nhs.uk/about-us/publications/"},
            {"publisher": "Valuation Office Agency", "title": "2023 Rating List", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "Ministry of Housing, Communities and Local Government", "title": "Non-Domestic Rating Act 2023 + Multipliers and Private Finance Act 2024", "url": "https://www.gov.uk/government/collections/business-rates"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Royal Devon University Healthcare NHS FT provider profile (RH8)", "url": "https://www.cqc.org.uk/provider/RH8"}
        ],
        "related": ["Royal Devon University Healthcare NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Business rates — Lancashire Teaching Hospitals NHS Foundation Trust", "Business rates — Bedfordshire Hospitals NHS Foundation Trust", "Valuation Office Agency"]
    },
    "Amortisation — Whittington Health NHS Trust": {
        "aliases": [{"name": "Amortisation", "parent": "Whittington Health NHS Trust"}],
        "description": "Whittington Health's £2.671M amortisation line is the systematic write-down of capitalised intangible assets — predominantly software licences, EPR-build internally generated intangibles and clinical-system development costs — across the Whittington Hospital (Archway) acute site plus the integrated community-services footprint across Islington and Haringey. The trust is on the Frontline Digitisation EPR programme (with North Central London ICS shared roadmap), driving material recent intangible additions and amortisation cycles. The integrated acute-plus-community model also adds community-system intangibles atypical for peer single-site DGHs.",
        "beneficiaries": "c. 4,500 WTE staff serving a c. 500,000 Islington + Haringey + parts of Camden/Barnet catchment; c. 100,000 ED attendances/yr at Whittington ED; c. 50,000 admissions/yr; integrated community services (district nursing + CCN + sexual health) across Islington and Haringey.",
        "legal_basis": "IAS 38 Intangible Assets — DHSC Group Accounting Manual 2024-25 chapter 5 — NHS Act 2006 — Health and Care Act 2022 — IFRS 16 (capitalised intangible interaction)",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£2.671M"},
            {"label": "Trust scale", "value": "Whittington Hospital (Archway) + integrated community services across Islington + Haringey; c. 4,500 WTE"},
            {"label": "Frontline Digitisation EPR", "value": "Whittington on Frontline Digitisation programme — North Central London ICS shared digital roadmap drives capitalised intangible build + amort"},
            {"label": "Integrated acute + community", "value": "Combined acute-plus-community model adds community-system intangibles (district-nurse caseload, sexual-health, CCN systems) atypical for peer single-site DGHs"},
            {"label": "Composition", "value": "Software licences (perpetual + capitalised SaaS) + internally generated EPR-build intangibles + community-system intangibles + clinical-system development — IAS 38 straight-line over useful life (typ. 3-10 years)"},
            {"label": "NCL ICS digital roadmap", "value": "North Central London ICS shared digital strategy across UCLH + Whittington + RFL + N Mid + GOSH + Tavistock — collaborative intangible build interactions"},
            {"label": "April 2025 NIC step-up", "value": "Indirect via supplier-side cost pass-through on SaaS uplifts"},
            {"label": "Funding trajectory", "value": "2021-22 c. £2.2M → 2023-24 c. £2.5M → 2024-25 £2.671M — Frontline Digitisation EPR build amort + ongoing software refresh"},
            {"label": "Delivery body", "value": "Trust IT + Finance (intangible register) + EPR vendor + NHSE Frontline Digitisation team + NCL ICS digital lead"},
            {"label": "Policy owner", "value": "NHSE Transformation Directorate (Frontline Digitisation) + DHSC + NHSE Provider Finance + North Central London ICB"},
            {"label": "Evaluation evidence", "value": "NAO Digital Transformation in the NHS 2020; NAO Frontline Digitisation 2023; Trust ARA 2023-24; CQC RKE inspections"},
            {"label": "Predecessor / successor", "value": "Predecessor: legacy patient-administration intangibles · Successor: continued EPR amort cycle + NCL ICS shared-system rationalisation + future SaaS-shift cost-of-revenue treatment"}
        ],
        "notes": "Whittington Health's amortisation line reflects both the Frontline Digitisation EPR build and the unusually broad community-system intangibles tied to its integrated acute-plus-community model — district-nurse caseload, sexual-health and CCN system development costs feed amort under IAS 38 straight-line over typical 3-10 year useful lives. The North Central London ICS shared digital roadmap (covering UCLH, Whittington, Royal Free, North Middlesex, GOSH, Tavistock) drives collaborative intangible build interactions atypical for an isolated DGH. April 2025 NIC step-up feeds indirect cost pass-through on SaaS contract uplifts. Future shift toward subscription-model SaaS will progressively reclassify spend away from intangible amort toward operating expense.",
        "sources": [
            {"publisher": "Whittington Health NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.whittington.nhs.uk/default.asp?c=33483"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/frontline-digitisation/"},
            {"publisher": "National Audit Office", "title": "Frontline Digitisation in the NHS (HC 1727, 2023)", "url": "https://www.nao.org.uk/reports/digital-transformation-in-the-nhs/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Whittington Health NHS Trust provider profile (RKE)", "url": "https://www.cqc.org.uk/provider/RKE"}
        ],
        "related": ["Whittington Health NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Amortisation — University Hospitals of Derby and Burton NHS Foundation Trust", "Transport (business + patient) — Whittington Health NHS Trust", "Frontline Digitisation"]
    },
    "Amortisation — Kettering General Hospital NHS Foundation Trust": {
        "aliases": [{"name": "Amortisation", "parent": "Kettering General Hospital NHS Foundation Trust"}],
        "description": "Kettering General's £2.645M amortisation line is the systematic write-down of capitalised intangible assets — predominantly software licences, EPR-build internally generated intangibles and clinical-system development costs — across the Kettering General Hospital DGH single-site footprint. The trust is on the New Hospital Programme cohort (Reset Jan 2025 deferred) and operates as the Kettering and Northampton group with Northampton General Hospital under shared CEO and shared corporate-services arrangements. Frontline Digitisation EPR rollout drives recent intangible additions under IAS 38.",
        "beneficiaries": "c. 4,800 WTE staff serving a c. 365,000 north Northamptonshire catchment (Kettering, Corby, Wellingborough, East Northants); c. 105,000 ED attendances/yr at Kettering ED; c. 60,000 admissions/yr; group arrangement with Northampton General Hospital under shared CEO.",
        "legal_basis": "IAS 38 Intangible Assets — DHSC Group Accounting Manual 2024-25 chapter 5 — NHS Act 2006 — Health and Care Act 2022 — IFRS 16 (capitalised intangible interaction)",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£2.645M"},
            {"label": "Trust scale", "value": "Kettering General Hospital DGH single-site; c. 4,800 WTE"},
            {"label": "New Hospital Programme cohort", "value": "Kettering on the NHP cohort under previous schedule — Reset Jan 2025 deferred construction; affects intangible-asset depreciation horizon decisions"},
            {"label": "Group arrangement", "value": "University Hospitals of Northamptonshire group (Kettering + Northampton General) under shared CEO + shared corporate services since 2021 — drives shared-intangible cost-allocation"},
            {"label": "Frontline Digitisation EPR", "value": "Group Frontline Digitisation EPR rollout — capitalised intangible drives recent amortisation step-ups"},
            {"label": "Composition", "value": "Software licences (perpetual + capitalised SaaS) + internally generated EPR-build intangibles + clinical-system development costs — IAS 38 straight-line over useful life (typ. 3-10 years)"},
            {"label": "April 2025 NIC step-up", "value": "Indirect via supplier-side cost pass-through on SaaS uplifts"},
            {"label": "Funding trajectory", "value": "2021-22 c. £2.2M → 2023-24 c. £2.5M → 2024-25 £2.645M — Frontline Digitisation EPR build amort + group-wide system harmonisation"},
            {"label": "Delivery body", "value": "Group IT + Finance (intangible register) + EPR vendor + NHSE Frontline Digitisation team"},
            {"label": "Policy owner", "value": "NHSE Transformation Directorate (Frontline Digitisation) + DHSC + NHSE Provider Finance + Northamptonshire ICB"},
            {"label": "Evaluation evidence", "value": "NAO Digital Transformation in the NHS 2020; NAO Frontline Digitisation 2023; Trust ARA 2023-24; CQC RNQ inspections"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-group separate intangible registers · Successor: continued EPR amort cycle + group system convergence + NHP rebuild capitalised-intangibles"}
        ],
        "notes": "Kettering General's amortisation line reflects both the Frontline Digitisation EPR build (rolled out as part of the University Hospitals of Northamptonshire group programme since 2021) and the New Hospital Programme position — Reset Jan 2025 deferred Kettering's construction timeline, with implications for intangible-asset useful-life and impairment assumptions tied to scheduled estate renewal. Group corporate-services sharing with Northampton General drives cost-allocation considerations on shared intangibles. April 2025 NIC step-up (15%, £5k threshold) feeds indirect cost pass-through on SaaS contract uplifts. Future shift toward subscription-model SaaS will progressively reclassify spend away from intangible amort toward operating expense.",
        "sources": [
            {"publisher": "Kettering General Hospital NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.kgh.nhs.uk/about-us/our-publications/"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/frontline-digitisation/"},
            {"publisher": "National Audit Office", "title": "Frontline Digitisation in the NHS (HC 1727, 2023)", "url": "https://www.nao.org.uk/reports/digital-transformation-in-the-nhs/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Kettering General Hospital NHS FT provider profile (RNQ)", "url": "https://www.cqc.org.uk/provider/RNQ"}
        ],
        "related": ["Kettering General Hospital NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Amortisation — University Hospitals of Derby and Burton NHS Foundation Trust", "Amortisation — Bradford Teaching Hospitals NHS Foundation Trust", "Frontline Digitisation"]
    },
    "Amortisation — Bradford Teaching Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Amortisation", "parent": "Bradford Teaching Hospitals NHS Foundation Trust"}],
        "description": "Bradford Teaching Hospitals' £2.644M amortisation line is the systematic write-down of capitalised intangible assets — predominantly software licences, EPR-build internally generated intangibles, the long-running Bradford-developed clinical-system stack and Connected Yorkshire shared-system development costs — across the Bradford Royal Infirmary + St Luke's Hospital footprint. Bradford is a long-standing NHSE digital exemplar (Cerner Millennium since 2007 + extensive in-house clinical-system development) and Connected Yorkshire LHCRE participant, generating an unusually mature intangible asset register relative to peer DGHs.",
        "beneficiaries": "c. 6,500 WTE staff serving a c. 540,000 Bradford metropolitan catchment plus regional tertiary referrals; c. 145,000 ED attendances/yr at Bradford Royal Infirmary ED; c. 80,000 admissions/yr; major paediatric tertiary centre (Born in Bradford research cohort); historic NHSE digital exemplar.",
        "legal_basis": "IAS 38 Intangible Assets — DHSC Group Accounting Manual 2024-25 chapter 5 — NHS Act 2006 — Health and Care Act 2022 — IFRS 16 (capitalised intangible interaction)",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£2.644M"},
            {"label": "Trust scale", "value": "Bradford Royal Infirmary + St Luke's Hospital; c. 6,500 WTE"},
            {"label": "Digital exemplar history", "value": "Bradford has run Cerner Millennium since 2007 — long-standing NHSE digital exemplar; mature intangible asset register relative to peer DGHs"},
            {"label": "Connected Yorkshire LHCRE", "value": "Connected Yorkshire Local Health and Care Record Exemplar participant — drives shared-intangible build with peer Yorkshire trusts + ICS partners"},
            {"label": "Frontline Digitisation refresh", "value": "Cerner Oracle Health refresh under Frontline Digitisation — capitalised intangible drives ongoing amortisation step-ups"},
            {"label": "Composition", "value": "Software licences (perpetual + capitalised SaaS) + internally generated EPR + clinical-system development costs + Connected Yorkshire shared development — IAS 38 straight-line over useful life (typ. 3-10 years)"},
            {"label": "Born in Bradford research", "value": "Major birth cohort research base — drives research-intangible co-development with University of Bradford + NIHR"},
            {"label": "April 2025 NIC step-up", "value": "Indirect via supplier-side cost pass-through on SaaS uplifts"},
            {"label": "Funding trajectory", "value": "2021-22 c. £2.3M → 2023-24 c. £2.5M → 2024-25 £2.644M — Cerner refresh + Connected Yorkshire build + research-intangible additions"},
            {"label": "Delivery body", "value": "Trust IT + Finance (intangible register) + Cerner Oracle Health (EPR) + Connected Yorkshire LHCRE programme + NHSE Frontline Digitisation team"},
            {"label": "Policy owner", "value": "NHSE Transformation Directorate (Frontline Digitisation) + DHSC + NHSE Provider Finance + West Yorkshire ICB"},
            {"label": "Evaluation evidence", "value": "NAO Digital Transformation in the NHS 2020; NAO Frontline Digitisation 2023; Trust ARA 2023-24; CQC RAE inspections; Born in Bradford publications"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2007 Cerner go-live capitalised intangibles · Successor: continued Cerner Oracle Health refresh + Connected Yorkshire integration + future SaaS-shift cost-of-revenue treatment"}
        ],
        "notes": "Bradford Teaching Hospitals' amortisation line reflects an unusually mature intangible asset register — Bradford has run Cerner Millennium since 2007 as a long-standing NHSE digital exemplar, with substantial in-house clinical-system development capitalised over many years and ongoing refresh under Frontline Digitisation (Cerner Oracle Health) feeding new tranches into the IAS 38 straight-line cycle. Connected Yorkshire LHCRE participation drives shared-intangible build with peer Yorkshire trusts and ICS partners. Born in Bradford birth-cohort research collaboration with the University of Bradford and NIHR generates research-intangible additions. April 2025 NIC step-up feeds indirect cost pass-through on SaaS contract uplifts. Future SaaS-shift will progressively reclassify spend away from intangible amort toward operating expense.",
        "sources": [
            {"publisher": "Bradford Teaching Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.bradfordhospitals.nhs.uk/about-us/who-we-are/publications/annual-report-and-accounts/"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/frontline-digitisation/"},
            {"publisher": "National Audit Office", "title": "Frontline Digitisation in the NHS (HC 1727, 2023)", "url": "https://www.nao.org.uk/reports/digital-transformation-in-the-nhs/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Bradford Teaching Hospitals NHS FT provider profile (RAE)", "url": "https://www.cqc.org.uk/provider/RAE"}
        ],
        "related": ["Bradford Teaching Hospitals NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Amortisation — Kettering General Hospital NHS Foundation Trust", "Amortisation — University Hospitals of Derby and Burton NHS Foundation Trust", "Frontline Digitisation"]
    },
}
