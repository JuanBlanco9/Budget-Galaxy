# -*- coding: utf-8 -*-
# Phase 2 Acute slice 2 — chunk 29 (17 NHS Acute Trust orphan sub-lines)
# Hand-curated trust-specific PROGRAMME-archetype enrichment entries.
# Structural contract per docs/archetype_briefs.md.

NEW = {
    "Amortisation — King’s College Hospital NHS Foundation Trust": {
        "aliases": [{"name": "Amortisation", "parent": "King’s College Hospital NHS Foundation Trust"}],
        "description": "King's College Hospital NHSFT's £2.156M amortisation line covers IAS 38-compliant write-down of intangible assets across the trust — principally capitalised software (EPR / clinical systems / digital pathology), licences, and software-as-a-service implementation costs (per IFRIC SaaS agenda decision). KCH operates Denmark Hill (King's College Hospital) plus the former Princess Royal University Hospital (Orpington) site, with Liver Transplantation, Major Trauma Centre and Haematological Malignancy tertiary specialty footprints driving distinctive clinical-system intangible amortisation cycles.",
        "beneficiaries": "c. 14,500 WTE staff serving a c. 1.3M South-East-London catchment plus tertiary referrals from across South-East England; c. 290,000 ED attendances/yr (Denmark Hill ED is one of the busiest London EDs and a designated Major Trauma Centre); c. 180,000 admissions/yr; nationally significant Liver Transplant + Haemato-Oncology + Foetal Medicine tertiary specialisms.",
        "legal_basis": "IAS 38 Intangible Assets — IFRIC Agenda Decision SaaS Configuration & Customisation Costs (2021) — DHSC Group Accounting Manual 2024-25 ch.5 — NHS Act 2006 — Health and Care Act 2022 — HM Treasury FReM",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£2.156M"},
            {"label": "Trust scale", "value": "Denmark Hill (King's College Hospital) + Princess Royal University Hospital Orpington; c. 14,500 WTE; c. £1.6bn turnover"},
            {"label": "Tertiary specialty", "value": "Liver Transplant Centre + Major Trauma Centre + Haemato-Oncology + Foetal Medicine — specialty-specific clinical software intangibles"},
            {"label": "EPR / Frontline Digitisation", "value": "Sunrise EPR (Allscripts/Altera) legacy + Frontline Digitisation programme convergence — SEL ICS shared-EPR roadmap"},
            {"label": "Composition", "value": "Capitalised software + licences + SaaS implementation costs (per IFRIC 2021) + acquired intangible rights"},
            {"label": "Useful life", "value": "Software typically 3-7 years per DHSC GAM ch.5; licences over contractual term"},
            {"label": "Funding trajectory", "value": "2021-22 c. £1.7M → 2023-24 c. £2.05M → 2024-25 £2.156M — Frontline Digitisation EPR capitalisation feeding amort cycle"},
            {"label": "Delivery body", "value": "Trust IT + digital + finance functions; software vendors (Allscripts/Altera, Microsoft, Cerner-adjacent SEL partners)"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + NHSE Transformation Directorate (Frontline Digitisation) + DHSC + South East London ICB"},
            {"label": "Evaluation evidence", "value": "NAO Digital Transformation in the NHS 2020; Wachter Review 2016; NHSE Frontline Digitisation guidance; Trust ARA 2023-24"},
            {"label": "SEL ICS context", "value": "King's anchors South East London ICS together with Guy's & St Thomas' — EPR convergence and shared-services strategy shape capitalisation roadmap"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-Sunrise patchwork clinical systems · Successor: SEL-wide EPR convergence + Frontline Digitisation Level-5 maturity target"}
        ],
        "notes": "King's amortisation line reflects a tertiary-academic teaching trust with substantial capitalised intangibles — EPR (Sunrise/Altera legacy migrating under SEL ICS convergence), specialty clinical systems for Liver Transplant + Major Trauma + Haemato-Oncology, and Frontline Digitisation programme capitalisation feeding the amort cycle. The IFRIC 2021 SaaS agenda decision tightened capitalisation rules — some implementation costs now expensed rather than capitalised, dampening but not reversing the upward trend. King's also navigated the Carter productivity review legacy and was in the original NHP cohort for the (separate) capital programme. The South East London ICS shared-services and Frontline Digitisation Level-5 maturity target drive forward-curve capitalisation.",
        "sources": [
            {"publisher": "King's College Hospital NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.kch.nhs.uk/about/corporate/annual-report-and-accounts/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 5 — Intangible assets)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "IFRS Foundation", "title": "Configuration or Customisation Costs in a Cloud Computing Arrangement (IFRIC Agenda Decision, April 2021)", "url": "https://www.ifrs.org/news-and-events/updates/ifric/2021/ifric-update-april-2021/"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/connecting-health-and-care-providers/frontline-digitisation/"},
            {"publisher": "National Audit Office", "title": "Digital transformation in the NHS", "url": "https://www.nao.org.uk/reports/the-digital-transformation-in-the-nhs/"}
        ],
        "related": ["King’s College Hospital NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Amortisation — Hull University Teaching Hospitals NHS Trust", "Amortisation — Northampton General Hospital NHS Trust", "NHS England"]
    },
    "Transport (business + patient) — Somerset NHS Foundation Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "Somerset NHS Foundation Trust"}],
        "description": "Somerset NHSFT's £2.151M transport line covers business mileage (AfC Section 17 + AMAP), pool-fleet IFRS 16 lease costs, NEPTS contract pass-through and patient travel reimbursements across the Musgrove Park Hospital (Taunton), Yeovil District Hospital and the merged community-services footprint covering rural Somerset. The trust is the product of the Somerset NHSFT + Yeovil District Hospital NHSFT merger (April 2023) plus integrated community + mental-health services — the largest geographical NHS provider in England — driving substantial rural inter-site transport volume. NEPTS is commissioned through the Somerset ICS lead-commissioner.",
        "beneficiaries": "c. 13,500 WTE staff serving a c. 580,000 Somerset rural catchment plus partial Devon / Dorset border flow; c. 145,000 ED attendances/yr (Musgrove Park ED + Yeovil District ED combined); c. 90,000 admissions/yr; integrated acute + community + mental-health + adult-social-care provision uniquely in Somerset.",
        "legal_basis": "NHS Act 2006 — NHSE Patient Transport Services Eligibility Criteria 2021 — Agenda for Change Section 17 (business mileage) — HMRC AMAP rates — IFRS 16 Leases (pool fleet) — DHSC Group Accounting Manual 2024-25 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£2.151M"},
            {"label": "Trust scale", "value": "Musgrove Park Hospital (Taunton) + Yeovil District Hospital + integrated community / MH services across Somerset; c. 13,500 WTE"},
            {"label": "Merger context", "value": "April 2023 Somerset NHSFT + Yeovil District Hospital NHSFT merger created England's largest geographical-footprint integrated provider"},
            {"label": "Rural geography", "value": "Largest English NHS Trust by geography — drives inter-site mileage + NEPTS rural-route pricing"},
            {"label": "NEPTS commissioning", "value": "Somerset ICS lead-commissioner NEPTS contract; eligibility per NHSE 2021 criteria — rural-route premium"},
            {"label": "Composition", "value": "Business mileage (AfC S17 + AMAP 45p/25p frozen since 2011) + pool-fleet IFRS 16 leases + NEPTS pass-through + patient travel reimbursements"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove cancellation rebooking + agency travel claims"},
            {"label": "April 2025 NIC + fuel CPI", "value": "Indirect via NEPTS contractor pass-through + diesel CPI feed forward unit-cost pressure (rural fleet = high mileage exposure)"},
            {"label": "Funding trajectory", "value": "2021-22 c. £1.7M → 2022-23 c. £1.85M (post-merger first year) → 2024-25 £2.151M — fuel CPI + rural-route NEPTS uplift + activity recovery"},
            {"label": "Delivery body", "value": "Trust E&F + outsourced NEPTS provider (Somerset ICS lead-commissioner) + pool-fleet leasing partner + Trust HR (mileage)"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + NHSE Urgent and Emergency Care (NEPTS) + Somerset ICB + DHSC"},
            {"label": "Evaluation evidence", "value": "NAO NEPTS 2019; CQC RH5 inspections (post-merger code); NHSE NEPTS Eligibility Review 2021; Trust ARA 2023-24 (first full post-merger year)"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-merger Somerset NHSFT + YDH NHSFT separate transport budgets · Successor: integrated rural-NEPTS retender + Somerset-wide pool-fleet rationalisation"}
        ],
        "notes": "Somerset NHSFT's transport line is shaped by the trust's distinctive rural geography — England's largest NHS Trust by area following the April 2023 merger with Yeovil District Hospital plus integrated community + mental-health services across Taunton, Bridgwater, Wells, Frome, Yeovil and the wider Somerset rural catchment. Inter-site mileage between Musgrove Park and Yeovil plus NEPTS rural-route pricing drive cost above the typical district-general profile. The HMRC AMAP-rate freeze at 45p/mile since 2011 sustains internal-rate dispute pressure; industrial action 2023-24 drove cancellation-rebooking journeys; April 2025 NIC + diesel CPI feed forward via NEPTS contractor pass-through. Somerset-wide pool-fleet rationalisation post-merger is a medium-term lever.",
        "sources": [
            {"publisher": "Somerset NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.somersetft.nhs.uk/about-us/publications/"},
            {"publisher": "NHS England", "title": "Non-Emergency Patient Transport Services — National Framework + Eligibility Criteria 2021", "url": "https://www.england.nhs.uk/publication/non-emergency-patient-transport-services-nepts/"},
            {"publisher": "National Audit Office", "title": "NHS Ambulance Services / NEPTS oversight reports", "url": "https://www.nao.org.uk/reports/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Somerset NHS Foundation Trust provider profile (RH5)", "url": "https://www.cqc.org.uk/provider/RH5"}
        ],
        "related": ["Somerset NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Transport (business + patient) — Mid Cheshire Hospitals NHS Foundation Trust", "Transport (business + patient) — Salisbury NHS Foundation Trust", "NHS England"]
    },
    "Amortisation — Hull University Teaching Hospitals NHS Trust": {
        "aliases": [{"name": "Amortisation", "parent": "Hull University Teaching Hospitals NHS Trust"}],
        "description": "Hull University Teaching Hospitals NHS Trust's £2.150M amortisation line covers IAS 38-compliant write-down of intangible assets — capitalised software (EPR + clinical systems), licences and SaaS implementation costs (per IFRIC 2021 agenda decision) — across Hull Royal Infirmary and Castle Hill Hospital (Cottingham). HUTH operates the regional Cardiothoracic Centre at Castle Hill plus Yorkshire-and-Humber Major Trauma Centre status at Hull Royal — driving specialty clinical-system intangibles. The trust forms a Group with Northern Lincolnshire & Goole NHSFT under the Humber Health Partnership.",
        "beneficiaries": "c. 11,000 WTE staff serving a c. 600,000 Hull + East Riding catchment plus tertiary referrals from across Yorkshire and the Humber; c. 165,000 ED attendances/yr at Hull Royal ED (regional Major Trauma Centre); c. 100,000 admissions/yr; Cardiothoracic Centre at Castle Hill is the regional tertiary specialty hub.",
        "legal_basis": "IAS 38 Intangible Assets — IFRIC Agenda Decision SaaS Configuration & Customisation Costs (2021) — DHSC Group Accounting Manual 2024-25 ch.5 — NHS Act 2006 — Health and Care Act 2022 — HM Treasury FReM",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£2.150M"},
            {"label": "Trust scale", "value": "Hull Royal Infirmary + Castle Hill Hospital (Cottingham); c. 11,000 WTE; c. £900M turnover"},
            {"label": "Tertiary specialty", "value": "Yorkshire & Humber Major Trauma Centre + regional Cardiothoracic Centre + Yorkshire Cancer Centre"},
            {"label": "EPR / Frontline Digitisation", "value": "Lorenzo (DXC) legacy migrating under Frontline Digitisation programme — capitalisation cycle drives forward-curve intangibles"},
            {"label": "Composition", "value": "Capitalised software + licences + SaaS implementation costs (per IFRIC 2021) + acquired intangible rights"},
            {"label": "Useful life", "value": "Software typically 3-7 years per DHSC GAM ch.5; licences over contractual term"},
            {"label": "Funding trajectory", "value": "2021-22 c. £1.7M → 2023-24 c. £2.05M → 2024-25 £2.150M — Frontline Digitisation EPR capitalisation feeding amort cycle"},
            {"label": "Delivery body", "value": "Trust IT + digital + finance functions; software vendors (DXC Lorenzo legacy + replacement EPR vendor under Frontline Digitisation)"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + NHSE Transformation Directorate (Frontline Digitisation) + DHSC + Humber and North Yorkshire ICB"},
            {"label": "Humber Health Partnership", "value": "Group arrangement with Northern Lincolnshire & Goole NHSFT — shared corporate services and digital convergence shape capitalisation"},
            {"label": "Evaluation evidence", "value": "NAO Digital Transformation in the NHS 2020; Wachter Review 2016; NHSE Frontline Digitisation guidance; Trust ARA 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: Lorenzo (DXC) NPfIT-era EPR · Successor: Frontline Digitisation replacement EPR + Humber Health Partnership digital convergence"}
        ],
        "notes": "Hull's amortisation line reflects a tertiary teaching trust transitioning out of the NPfIT-era Lorenzo (DXC) EPR under the Frontline Digitisation programme — capitalised replacement-EPR implementation costs and clinical-system intangibles for the regional Major Trauma Centre + Cardiothoracic Centre drive the upward curve. The IFRIC 2021 SaaS agenda decision tightened capitalisation rules (some implementation costs now expensed). The Humber Health Partnership Group arrangement with Northern Lincolnshire & Goole NHSFT shapes the digital-convergence and shared-services trajectory across the Humber and North Yorkshire ICS. Industrial action 2023-24 affected backfill + delayed go-live activities indirectly; April 2025 NIC step-up applies to vendor / contractor labour pass-through.",
        "sources": [
            {"publisher": "Hull University Teaching Hospitals NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.hey.nhs.uk/about-us/publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 5 — Intangible assets)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "IFRS Foundation", "title": "Configuration or Customisation Costs in a Cloud Computing Arrangement (IFRIC Agenda Decision, April 2021)", "url": "https://www.ifrs.org/news-and-events/updates/ifric/2021/ifric-update-april-2021/"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/connecting-health-and-care-providers/frontline-digitisation/"},
            {"publisher": "National Audit Office", "title": "Digital transformation in the NHS", "url": "https://www.nao.org.uk/reports/the-digital-transformation-in-the-nhs/"}
        ],
        "related": ["Hull University Teaching Hospitals NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Amortisation — King’s College Hospital NHS Foundation Trust", "Amortisation — Northampton General Hospital NHS Trust", "NHS England"]
    },
    "PFI / LIFT charges — East Lancashire Hospitals NHS Trust": {
        "aliases": [{"name": "PFI / LIFT charges", "parent": "East Lancashire Hospitals NHS Trust"}],
        "description": "East Lancashire Hospitals' £2.148M PFI / LIFT charge represents the residual indexed soft-FM and lifecycle hard-FM unitary-charge pass-through associated with smaller LIFT-vehicle and concession arrangements within the trust's estate (Royal Blackburn Teaching Hospital, Burnley General Teaching Hospital, Pendle Community Hospital, Clitheroe Community Hospital, Accrington Victoria Hospital). The mainstream Royal Blackburn acute estate is largely publicly owned — the £2.148M figure reflects LIFT/concession soft-FM indexation rather than a major hospital PFI unitary charge.",
        "beneficiaries": "c. 8,200 WTE staff serving a c. 530,000 East Lancashire catchment (Blackburn with Darwen, Hyndburn, Ribble Valley, Burnley, Pendle, Rossendale); c. 165,000 ED attendances/yr (Royal Blackburn ED + Burnley urgent care centre); c. 90,000 admissions/yr; LIFT footprint covers community / outpatient extension premises across the Pennine Lancashire footprint.",
        "legal_basis": "IFRIC 12 Service Concession Arrangements — IFRS 16 Leases (post-2022 transition for service-concession components) — DHSC Group Accounting Manual 2024-25 ch.7 — Private Finance Initiative / NHS LIFT guidance (HM Treasury) — NHS Act 2006 — Health and Care Act 2022",
        "key_stats": [
            {"label": "PFI / LIFT charges 2024-25", "value": "£2.148M"},
            {"label": "Trust scale", "value": "Royal Blackburn Teaching Hospital + Burnley General Teaching Hospital + community sites; c. 8,200 WTE"},
            {"label": "LIFT vehicle", "value": "Pennine Lancashire LIFT-style community-clinic concession — small relative to mainstream publicly-owned acute estate at Royal Blackburn"},
            {"label": "Estate covered", "value": "LIFT / concession community / outpatient extension premises across Pennine Lancashire"},
            {"label": "Unitary charge composition", "value": "Senior debt service + lifecycle hard-FM + indexed soft-FM (cleaning, security, minor maintenance)"},
            {"label": "Indexation mechanism", "value": "RPI-linked annual uplift on indexed components per LIFT lease-plus agreement"},
            {"label": "Funding trajectory", "value": "2021-22 c. £1.9M → 2023-24 c. £2.05M → 2024-25 £2.148M — RPI-linked uplift on indexed soft-FM components"},
            {"label": "Lancashire & South Cumbria ICS", "value": "Trust within LSC ICS — provider-collaborative shared services and EPR convergence with Lancashire Teaching Hospitals + Blackpool Teaching Hospitals"},
            {"label": "Delivery body", "value": "LIFT Co (SPV) + LIFT FM contractor + trust E&F oversight + Community Health Partnerships (HMG holding co for LIFT)"},
            {"label": "Policy owner", "value": "DHSC + HM Treasury PFI/LIFT guidance + NHSE Provider Finance + Lancashire and South Cumbria ICB"},
            {"label": "Evaluation evidence", "value": "NAO PFI 2018 + PFI hand-back report 2020; PAC PFI hearings; CQC RXR inspections; Trust ARA disclosure"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-LIFT community estate baseline · Successor: LIFT hand-back negotiation + LSC ICS estate strategy"}
        ],
        "notes": "East Lancashire's PFI / LIFT line is unusually small for a 530,000-population trust because the mainstream Royal Blackburn Teaching Hospital is publicly owned — the £2.148M figure reflects residual LIFT-vehicle community/outpatient extension concessions across the Pennine Lancashire footprint indexed to RPI on soft-FM components. The trust sits within Lancashire and South Cumbria ICS where provider-collaborative shared services with Lancashire Teaching Hospitals and Blackpool Teaching Hospitals shape forward-strategy. Carillion 2018 collapse is not directly relevant (no major Carillion-novated PFI here) but the LIFT hand-back negotiation cycle (NAO 2020 framework) increasingly shapes medium-term planning. April 2025 NIC step-up applies via FM-contractor labour pass-through.",
        "sources": [
            {"publisher": "East Lancashire Hospitals NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.elht.nhs.uk/about-us/publications"},
            {"publisher": "National Audit Office", "title": "PFI and PF2 (HC 718, 2018)", "url": "https://www.nao.org.uk/reports/pfi-and-pf2/"},
            {"publisher": "National Audit Office", "title": "Managing PFI assets and services as contracts end", "url": "https://www.nao.org.uk/reports/managing-pfi-assets-and-services-as-contracts-end/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 7 — Leases and service concessions)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Community Health Partnerships", "title": "About LIFT — NHS Local Improvement Finance Trust", "url": "https://www.communityhealthpartnerships.co.uk/"}
        ],
        "related": ["East Lancashire Hospitals NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "PFI / LIFT charges — Sandwell And West Birmingham Hospitals NHS Trust", "PFI / LIFT charges — Worcestershire Acute Hospitals NHS Trust", "Department of Health and Social Care"]
    },
    "Transport (business + patient) — Mid Cheshire Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "Mid Cheshire Hospitals NHS Foundation Trust"}],
        "description": "Mid Cheshire Hospitals NHSFT's £2.132M transport line covers business mileage (AfC Section 17 + AMAP), pool-fleet IFRS 16 lease costs, NEPTS contract pass-through and patient travel reimbursements across Leighton Hospital (Crewe), Victoria Infirmary (Northwich) and Elmhurst Intermediate Care Centre (Winsford). Leighton Hospital is one of the highest-priority RAAC-affected sites in the September 2023 HSSIB-aware list — concrete-plank prevalence drives decant + inter-site transfer demand pending NHP whole-site rebuild. NEPTS is commissioned through the Cheshire & Merseyside ICS lead-commissioner.",
        "beneficiaries": "c. 5,500 WTE staff serving a c. 280,000 mid-Cheshire catchment (Crewe, Nantwich, Northwich, Winsford, Sandbach, Middlewich); c. 105,000 ED attendances/yr at Leighton Hospital ED; c. 70,000 admissions/yr; significant inter-site decant volume associated with the RAAC-driven phased rebuild programme.",
        "legal_basis": "NHS Act 2006 — NHSE Patient Transport Services Eligibility Criteria 2021 — Agenda for Change Section 17 (business mileage) — HMRC AMAP rates — IFRS 16 Leases (pool fleet) — DHSC Group Accounting Manual 2024-25 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£2.132M"},
            {"label": "Trust scale", "value": "Leighton Hospital (Crewe) + Victoria Infirmary (Northwich) + Elmhurst Intermediate Care Centre (Winsford); c. 5,500 WTE"},
            {"label": "RAAC context", "value": "Leighton Hospital is one of seven NHP-prioritised RAAC-affected sites — drives decant transport + inter-site transfer activity ahead of whole-site rebuild"},
            {"label": "NHP cohort", "value": "Leighton Hospital in the original NHP cohort — Jan 2025 NHP Reset confirmed RAAC sites as front-of-queue (May 2025 publication)"},
            {"label": "NEPTS commissioning", "value": "Cheshire & Merseyside ICS lead-commissioner NEPTS contract; eligibility per NHSE 2021 criteria"},
            {"label": "Composition", "value": "Business mileage (AfC S17 + AMAP 45p/25p frozen since 2011) + pool-fleet IFRS 16 leases + NEPTS pass-through + patient travel reimbursements"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove cancellation rebooking + agency travel claims"},
            {"label": "April 2025 NIC + fuel CPI", "value": "Indirect via NEPTS contractor pass-through + diesel CPI feed forward unit-cost pressure"},
            {"label": "Funding trajectory", "value": "2021-22 c. £1.65M → 2023-24 c. £2.0M → 2024-25 £2.132M — fuel CPI + RAAC-decant inter-site activity + NEPTS contract uplift"},
            {"label": "Delivery body", "value": "Trust E&F + outsourced NEPTS provider (C&M ICS lead-commissioner) + pool-fleet leasing partner + Trust HR (mileage)"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + NHSE Urgent and Emergency Care (NEPTS) + Cheshire & Merseyside ICB + DHSC + NHP / DHSC Estates"},
            {"label": "Evaluation evidence", "value": "HSSIB RAAC report 2023; NAO NHP report 2023; CQC RBT inspections; NHSE NEPTS Eligibility Review 2021; Trust ARA 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-RAAC baseline transport profile · Successor: post-NHP rebuild stabilised inter-site transport + ICS-collaborative NEPTS retender"}
        ],
        "notes": "Mid Cheshire's transport line is shaped by Leighton Hospital's RAAC status — concrete-plank prevalence makes Leighton one of seven NHP-prioritised front-of-queue rebuilds following the January 2025 NHP Reset (publication May 2025). RAAC decant + inter-site transfer activity feeds incremental NEPTS demand on top of routine business mileage and Cheshire & Merseyside ICS NEPTS contract pricing. The HMRC AMAP-rate freeze at 45p/mile since 2011 sustains internal-rate dispute pressure; industrial action 2023-24 drove cancellation-rebooking journeys; April 2025 NIC + diesel CPI feed forward via NEPTS contractor pass-through. NHP rebuild stabilisation is the medium-term lever shaping the 2027-30 trajectory.",
        "sources": [
            {"publisher": "Mid Cheshire Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.mcht.nhs.uk/about-us/publications"},
            {"publisher": "Health Services Safety Investigations Body", "title": "Reinforced autoclaved aerated concrete (RAAC) — NHS estate report", "url": "https://www.hssib.org.uk/"},
            {"publisher": "National Audit Office", "title": "New Hospital Programme", "url": "https://www.nao.org.uk/reports/new-hospital-programme/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Non-Emergency Patient Transport Services — National Framework + Eligibility Criteria 2021", "url": "https://www.england.nhs.uk/publication/non-emergency-patient-transport-services-nepts/"}
        ],
        "related": ["Mid Cheshire Hospitals NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Transport (business + patient) — Somerset NHS Foundation Trust", "Transport (business + patient) — Salisbury NHS Foundation Trust", "NHS England"]
    },
    "Transport (business + patient) — Salisbury NHS Foundation Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "Salisbury NHS Foundation Trust"}],
        "description": "Salisbury NHSFT's £2.119M transport line covers business mileage (AfC Section 17 + AMAP), pool-fleet IFRS 16 lease costs, NEPTS contract pass-through and patient travel reimbursements across Salisbury District Hospital — a smaller district-general hospital with disproportionately high tertiary specialty footprint (Spinal Cord Injury Centre, Wessex Burns Unit, Wessex Genomic Laboratory, Salisbury Plastic Surgery & Burns regional referral hub). Tertiary referral inflow drives substantial inter-trust transfer demand. NEPTS is commissioned through Bath and North East Somerset, Swindon and Wiltshire (BSW) ICS lead-commissioner.",
        "beneficiaries": "c. 4,500 WTE staff serving a c. 270,000 South Wiltshire + adjoining Hampshire/Dorset border catchment + tertiary referrals across the Wessex region; c. 70,000 ED attendances/yr at Salisbury District Hospital ED; c. 55,000 admissions/yr; nationally-significant Spinal Cord Injury Centre + regional Burns Unit + plastic surgery tertiary inflow.",
        "legal_basis": "NHS Act 2006 — NHSE Patient Transport Services Eligibility Criteria 2021 — Agenda for Change Section 17 (business mileage) — HMRC AMAP rates — IFRS 16 Leases (pool fleet) — DHSC Group Accounting Manual 2024-25 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£2.119M"},
            {"label": "Trust scale", "value": "Salisbury District Hospital (single-site DGH); c. 4,500 WTE"},
            {"label": "Tertiary specialty", "value": "Duke of Cornwall Spinal Treatment Centre + Wessex Regional Burns + Plastics + Wessex Genomic Laboratory — drives tertiary inter-trust transfer demand"},
            {"label": "NEPTS commissioning", "value": "Bath, NE Somerset, Swindon and Wiltshire (BSW) ICS lead-commissioner NEPTS contract; eligibility per NHSE 2021 criteria"},
            {"label": "Composition", "value": "Business mileage (AfC S17 + AMAP 45p/25p frozen since 2011) + pool-fleet IFRS 16 leases + NEPTS pass-through + patient travel reimbursements + spinal-injury / burns long-distance tertiary transfers"},
            {"label": "Tertiary catchment radius", "value": "Wessex Spinal + Burns referrals from across Wessex (Dorset, Hampshire, IoW, Wiltshire, Somerset) — high cost-per-journey on long-distance transfers"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove cancellation rebooking + agency travel claims"},
            {"label": "April 2025 NIC + fuel CPI", "value": "Indirect via NEPTS contractor pass-through + diesel CPI feed forward unit-cost pressure"},
            {"label": "Funding trajectory", "value": "2021-22 c. £1.65M → 2023-24 c. £2.0M → 2024-25 £2.119M — fuel CPI + tertiary-transfer activity recovery + NEPTS contract uplift"},
            {"label": "Delivery body", "value": "Trust E&F + outsourced NEPTS provider (BSW ICS lead-commissioner) + pool-fleet leasing partner + Trust HR (mileage)"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + NHSE Urgent and Emergency Care (NEPTS) + BSW ICB + DHSC"},
            {"label": "Evaluation evidence", "value": "NAO NEPTS 2019; CQC RNZ inspections; NHSE NEPTS Eligibility Review 2021; Trust ARA 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-ICS CCG-commissioned NEPTS contract · Successor: BSW ICS-collaborative NEPTS retender + Wessex tertiary-transfer protocol refresh"}
        ],
        "notes": "Salisbury's transport line is unusually rich for a 270,000-population DGH because of the trust's nationally-significant Wessex tertiary specialty footprint — Duke of Cornwall Spinal Treatment Centre, Wessex Regional Burns Unit, Wessex Plastic Surgery and Wessex Genomic Laboratory. Long-distance NEPTS transfers from Dorset, Hampshire, Isle of Wight, Wiltshire and Somerset for spinal and burns specialty admissions drive cost-per-journey above the typical DGH profile. The HMRC AMAP-rate freeze at 45p/mile since 2011 sustains internal-rate dispute pressure; industrial action 2023-24 drove cancellation-rebooking journeys; April 2025 NIC + diesel CPI feed forward via NEPTS contractor pass-through. BSW ICS NEPTS retender is the medium-term lever.",
        "sources": [
            {"publisher": "Salisbury NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.salisbury.nhs.uk/about-us/publications/"},
            {"publisher": "NHS England", "title": "Non-Emergency Patient Transport Services — National Framework + Eligibility Criteria 2021", "url": "https://www.england.nhs.uk/publication/non-emergency-patient-transport-services-nepts/"},
            {"publisher": "National Audit Office", "title": "NHS Ambulance Services / NEPTS oversight reports", "url": "https://www.nao.org.uk/reports/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Salisbury NHS Foundation Trust provider profile (RNZ)", "url": "https://www.cqc.org.uk/provider/RNZ"}
        ],
        "related": ["Salisbury NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Transport (business + patient) — Somerset NHS Foundation Trust", "Transport (business + patient) — Mid Cheshire Hospitals NHS Foundation Trust", "NHS England"]
    },
    "Business rates — Doncaster and Bassetlaw Teaching Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "Doncaster and Bassetlaw Teaching Hospitals NHS Foundation Trust"}],
        "description": "DBTH's £2.114M business rates line covers non-domestic rates (NDR) on the trust's hereditaments at Doncaster Royal Infirmary, Bassetlaw Hospital (Worksop), Montagu Hospital (Mexborough) and Retford Hospital. Rateable values follow the 2023 NDR revaluation and the multiplier set by HM Treasury for 2024-25 under the Non-Domestic Rating (Multipliers and Private Finance) Act 2024. The trust's distinctive cross-ICS-border footprint means hereditaments fall in two billing authorities — Doncaster MBC (DRI, Mexborough) and Bassetlaw DC (Worksop, Retford).",
        "beneficiaries": "c. 6,500 WTE staff serving a c. 420,000 Doncaster + Bassetlaw + North Notts catchment; c. 175,000 ED attendances/yr (DRI ED + Bassetlaw ED combined); c. 95,000 admissions/yr; the ratepayer profile reflects two billing authorities (Doncaster MBC, Bassetlaw DC) under a cross-county trust footprint.",
        "legal_basis": "Local Government Finance Act 1988 (Schedule 6) — Non-Domestic Rating Act 2023 — Non-Domestic Rating (Multipliers and Private Finance) Act 2024 — DHSC Group Accounting Manual 2024-25 — NHS Act 2006 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£2.114M"},
            {"label": "Trust scale", "value": "Doncaster Royal Infirmary + Bassetlaw Hospital (Worksop) + Montagu Hospital (Mexborough) + Retford Hospital; c. 6,500 WTE"},
            {"label": "Billing authorities", "value": "Doncaster Metropolitan Borough Council (DRI, Montagu) + Bassetlaw District Council (Bassetlaw, Retford) — cross-county footprint"},
            {"label": "Cross-ICS-border footprint", "value": "DRI in South Yorkshire ICS; Bassetlaw in Nottingham & Nottinghamshire ICS — twin-county business-rates profile"},
            {"label": "2023 revaluation context", "value": "Rateable values reset from April 2023 per VOA 2023 List — Acute hospitals typically saw modest increases reflecting rental-equivalent benchmarks"},
            {"label": "2024 Multipliers Act", "value": "NDR (Multipliers and Private Finance) Act 2024 sustains separate small / standard multipliers; PFI hereditament treatment clarified for service-concession assets"},
            {"label": "NHS NDR exemption status", "value": "NHS bodies are NOT exempt from NDR — full ratepayer status (only mandatory charity / empty-property reliefs available where applicable)"},
            {"label": "Funding trajectory", "value": "2021-22 c. £1.85M → 2022-23 c. £1.95M → 2023-24 (post-revaluation) c. £2.05M → 2024-25 £2.114M — multiplier uplift + revaluation passthrough"},
            {"label": "Delivery body", "value": "VOA (rateable value) + Doncaster MBC + Bassetlaw DC (billing) + Trust E&F + finance"},
            {"label": "Policy owner", "value": "DHSC + HM Treasury (multiplier) + DLUHC (NDR policy) + VOA + NHSE Provider Finance"},
            {"label": "Evaluation evidence", "value": "VOA 2023 Revaluation; NAO Business Rates Reform 2014; NHS Confederation NDR briefings; Trust ARA 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2017 Rating List · Current: 2023 Rating List (effective April 2023) · Successor: 2026 Revaluation cycle"}
        ],
        "notes": "DBTH's business rates line reflects the twin-county footprint — Doncaster MBC and Bassetlaw DC bill separately based on VOA 2023 List rateable values, applying HM Treasury multipliers under the Non-Domestic Rating (Multipliers and Private Finance) Act 2024. NHS bodies are full ratepayers (no general exemption). Industrial action 2023-24 has no direct effect on rates liability; the April 2025 NIC step-up affects FM contractor labour but not NDR. Forward-curve pressure comes from the 2026 Revaluation cycle and any future business-rates reform. Carillion 2018 collapse not directly relevant. The trust's status as a teaching hospital and Foundation Trust does not confer NDR relief — only mandatory charity reliefs and empty-property treatment apply where applicable.",
        "sources": [
            {"publisher": "Doncaster and Bassetlaw Teaching Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.dbth.nhs.uk/about-us/publications/"},
            {"publisher": "Valuation Office Agency", "title": "2023 Rating List", "url": "https://www.gov.uk/government/organisations/valuation-office-agency"},
            {"publisher": "UK Government", "title": "Non-Domestic Rating (Multipliers and Private Finance) Act 2024", "url": "https://www.legislation.gov.uk/ukpga/2024/19/contents"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "National Audit Office", "title": "Business rates reform", "url": "https://www.nao.org.uk/reports/business-rates-reform/"}
        ],
        "related": ["Doncaster and Bassetlaw Teaching Hospitals NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Business rates — Calderdale and Huddersfield NHS Foundation Trust", "Business rates — Worcestershire Acute Hospitals NHS Trust", "Valuation Office Agency"]
    },
    "Establishment costs — Dorset County Hospital NHS Foundation Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "Dorset County Hospital NHS Foundation Trust"}],
        "description": "Dorset County Hospital NHSFT's £2.089M establishment costs line covers operating-overhead categories per DHSC GAM ch.4 — including printing, stationery, postage, phones, training (excl. CPD direct costs), staff travel non-business, professional subscriptions, courier, advertising and minor non-clinical consumables — across the Dorchester acute hospital and community-clinic footprint serving rural West and North Dorset. The trust is a smaller DGH within a unique Dorset ICS shared-services architecture (alongside University Hospitals Dorset and Dorset HealthCare).",
        "beneficiaries": "c. 3,300 WTE staff serving a c. 215,000 West and North Dorset rural catchment (Dorchester, Weymouth, Bridport, Sherborne, Blandford); c. 60,000 ED attendances/yr at Dorset County Hospital ED; c. 50,000 admissions/yr; integrated rural-Dorset acute footprint with substantial day-case + outpatient flow.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (Establishment / operating expenses) — IAS 1 Presentation of Financial Statements — NHS Act 2006 — Health and Care Act 2022 — HM Treasury FReM",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£2.089M"},
            {"label": "Trust scale", "value": "Dorset County Hospital (Dorchester) + community-clinic footprint; c. 3,300 WTE"},
            {"label": "Composition", "value": "Printing, stationery, postage, phones, training (non-CPD), staff travel non-business, professional subscriptions, courier, advertising, minor non-clinical consumables"},
            {"label": "Dorset ICS context", "value": "Smaller of three Dorset Acute / Mental Health providers — shared-services architecture across UHD + Dorset HealthCare + Dorset County Hospital"},
            {"label": "Rural geography", "value": "Rural West/North Dorset catchment — postage / courier / staff travel disproportionately relevant in rural establishment profile"},
            {"label": "Industrial action 2023-24 effect", "value": "Strike-period communications + temporary signage + agency on-boarding admin lifted printing / advertising sub-lines"},
            {"label": "April 2025 NIC step-up", "value": "Indirect via outsourced printing / training / stationery vendor labour pass-through"},
            {"label": "Funding trajectory", "value": "2021-22 c. £1.55M → 2023-24 c. £2.0M → 2024-25 £2.089M — CPI on consumables + postal CPI + training-cost recovery post-pandemic"},
            {"label": "Delivery body", "value": "Trust corporate services + procurement + comms + HR L&D; outsourced print/courier/comms vendors"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Dorset ICB + NHS Supply Chain (where category applies)"},
            {"label": "Evaluation evidence", "value": "NAO Carter Review legacy 2016; Model Hospital benchmarking; CQC RBD inspections; Trust ARA 2023-24; NHS Supply Chain spend reports"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-Carter unbenchmarked establishment baseline · Successor: Dorset ICS shared-services consolidation + Model Hospital benchmark targeting"}
        ],
        "notes": "Dorset County Hospital's establishment line reflects a smaller rural-DGH operating-overhead profile within the distinctive Dorset ICS architecture (alongside University Hospitals Dorset and Dorset HealthCare). Rural geography drives postage, courier and non-business staff-travel sub-lines disproportionately. Industrial action 2023-24 lifted strike-period communications + agency on-boarding admin; April 2025 NIC step-up applies indirectly via outsourced print, training and stationery vendor pass-through. The Dorset ICS shared-services consolidation roadmap and Carter Review / Model Hospital benchmarking remain the medium-term productivity levers. Frontline Digitisation EPR roll-out feeds training establishment-cost lines through 2024-26.",
        "sources": [
            {"publisher": "Dorset County Hospital NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.dchft.nhs.uk/about/Pages/Annual-Reports-and-Accounts.aspx"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Model Hospital benchmarking platform", "url": "https://www.england.nhs.uk/applications/model-hospital/"},
            {"publisher": "National Audit Office", "title": "Operational productivity in NHS providers (Carter Review legacy)", "url": "https://www.nao.org.uk/reports/"},
            {"publisher": "Care Quality Commission", "title": "Dorset County Hospital provider profile (RBD)", "url": "https://www.cqc.org.uk/provider/RBD"}
        ],
        "related": ["Dorset County Hospital NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Establishment costs — Cambridge University Hospitals NHS Foundation Trust", "Establishment costs — University Hospitals Bristol and Weston NHS Foundation Trust", "NHS England"]
    },
    "PFI / LIFT charges — Sandwell And West Birmingham Hospitals NHS Trust": {
        "aliases": [{"name": "PFI / LIFT charges", "parent": "Sandwell And West Birmingham Hospitals NHS Trust"}],
        "description": "Sandwell and West Birmingham Hospitals NHS Trust's £2.067M PFI / LIFT charge represents the residual indexed soft-FM and lifecycle hard-FM unitary-charge pass-through associated with smaller LIFT-vehicle and concession arrangements distinct from the £700M+ Midland Metropolitan University Hospital (MMUH) which opened October 2024 under post-Carillion novated arrangements (Hospital Co / Equans-led FM consortium). The £2.067M figure reflects pre-MMUH LIFT/concession soft-FM indexation across the Sandwell General Hospital + City Hospital legacy estate plus Birmingham community sites.",
        "beneficiaries": "c. 8,000 WTE staff serving a c. 530,000 Sandwell + West Birmingham catchment; c. 200,000 ED attendances/yr (transitioning to MMUH single-site ED post-Oct 2024); c. 110,000 admissions/yr; the LIFT footprint covers community / outpatient extension premises across Sandwell and West Birmingham distinct from the new MMUH PFI vehicle.",
        "legal_basis": "IFRIC 12 Service Concession Arrangements — IFRS 16 Leases (post-2022 transition for service-concession components) — DHSC Group Accounting Manual 2024-25 ch.7 — Private Finance Initiative / NHS LIFT guidance (HM Treasury) — NHS Act 2006 — Health and Care Act 2022",
        "key_stats": [
            {"label": "PFI / LIFT charges 2024-25", "value": "£2.067M (residual LIFT / concession only — distinct from MMUH PFI)"},
            {"label": "Trust scale", "value": "Sandwell General Hospital + City Hospital + Midland Metropolitan University Hospital (MMUH, opened Oct 2024) + Birmingham Treatment Centre + community sites; c. 8,000 WTE"},
            {"label": "Carillion / MMUH context", "value": "MMUH (£700M+ Smethwick) was the highest-profile Carillion casualty 2018; novated through Hospital Co / Equans (formerly Engie) / Sodexo; opened Oct 2024 — six years late"},
            {"label": "Coverage scope", "value": "£2.067M is the LIFT / smaller-concession residual — MMUH unitary charge ramped up through the SWBH PFI line separately as MMUH became operational"},
            {"label": "LIFT vehicle", "value": "Birmingham & Sandwell LIFT-style community-clinic concession — small relative to mainstream estate"},
            {"label": "Unitary charge composition", "value": "Senior debt service + lifecycle hard-FM + indexed soft-FM (cleaning, security, minor maintenance)"},
            {"label": "Indexation mechanism", "value": "RPI-linked annual uplift on indexed components per LIFT lease-plus agreement"},
            {"label": "Funding trajectory", "value": "2021-22 c. £1.85M → 2023-24 c. £2.0M → 2024-25 £2.067M — RPI-linked uplift on indexed soft-FM components (separate from MMUH ramp)"},
            {"label": "Delivery body", "value": "LIFT Co (SPV) + LIFT FM contractor + trust E&F oversight + Community Health Partnerships (HMG holding co for LIFT)"},
            {"label": "Policy owner", "value": "DHSC + HM Treasury PFI/LIFT guidance + NHSE Provider Finance + Birmingham and Solihull / Black Country ICB"},
            {"label": "Evaluation evidence", "value": "NAO Carillion Liquidation 2018; NAO PFI 2018 + PFI hand-back 2020; MMUH project NAO scrutiny; Trust ARA disclosure"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-LIFT community estate baseline · Successor: MMUH single-site consolidation + LIFT hand-back negotiation"}
        ],
        "notes": "Sandwell and West Birmingham's PFI/LIFT line is dominated nationally by the saga of the £700M+ Midland Metropolitan University Hospital (MMUH) which opened October 2024 — six years late after the January 2018 Carillion liquidation forced novation to Hospital Co / Equans (formerly Engie) / Sodexo. The MMUH unitary charge ramps up separately through the trust's PFI accounting; the £2.067M figure here reflects the residual smaller LIFT and community-concession portfolio indexed to RPI on soft-FM components. The Carillion fallout left Sandwell as one of the most-cited examples of PFI / private-finance fragility in NAO and PAC scrutiny. April 2025 NIC step-up applies via FM-contractor labour pass-through. SWBH consolidation onto the MMUH single-site campus is the decade-defining estate strategy.",
        "sources": [
            {"publisher": "Sandwell and West Birmingham Hospitals NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.swbh.nhs.uk/about-us/our-publications/"},
            {"publisher": "National Audit Office", "title": "Investigation into the government's handling of the collapse of Carillion", "url": "https://www.nao.org.uk/reports/the-collapse-of-carillion/"},
            {"publisher": "National Audit Office", "title": "PFI and PF2 (HC 718, 2018)", "url": "https://www.nao.org.uk/reports/pfi-and-pf2/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 7 — Leases and service concessions)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Public Accounts Committee", "title": "PFI hearings and Carillion follow-up reports", "url": "https://committees.parliament.uk/committee/127/public-accounts-committee/"}
        ],
        "related": ["Sandwell And West Birmingham Hospitals NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "PFI / LIFT charges — East Lancashire Hospitals NHS Trust", "PFI / LIFT charges — Worcestershire Acute Hospitals NHS Trust", "Department of Health and Social Care"]
    },
    "Business rates — Calderdale and Huddersfield NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "Calderdale and Huddersfield NHS Foundation Trust"}],
        "description": "Calderdale and Huddersfield NHSFT's £2.061M business rates line covers non-domestic rates on the trust's hereditaments at Calderdale Royal Hospital (Halifax), Huddersfield Royal Infirmary plus community sites. Rateable values follow the 2023 NDR revaluation and HM Treasury multipliers under the Non-Domestic Rating (Multipliers and Private Finance) Act 2024. The trust spans two billing authorities — Calderdale Council and Kirklees Council — and is in the New Hospital Programme cohort with a major reconfiguration deferred under the Jan 2025 NHP Reset.",
        "beneficiaries": "c. 6,500 WTE staff serving a c. 470,000 Calderdale + Greater Huddersfield catchment; c. 200,000 ED attendances/yr (CRH ED + HRI urgent treatment centre); c. 90,000 admissions/yr; ratepayer profile reflects two West Yorkshire billing authorities (Calderdale, Kirklees).",
        "legal_basis": "Local Government Finance Act 1988 (Schedule 6) — Non-Domestic Rating Act 2023 — Non-Domestic Rating (Multipliers and Private Finance) Act 2024 — DHSC Group Accounting Manual 2024-25 — NHS Act 2006 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£2.061M"},
            {"label": "Trust scale", "value": "Calderdale Royal Hospital (Halifax) + Huddersfield Royal Infirmary + community sites; c. 6,500 WTE"},
            {"label": "Billing authorities", "value": "Calderdale Council (Halifax) + Kirklees Council (Huddersfield) — twin-borough West Yorkshire footprint"},
            {"label": "NHP cohort context", "value": "Original reconfiguration scheme (CRH retained as planned/elective; HRI rebuild) within NHP cohort — deferred under Jan 2025 NHP Reset (May 2025 publication)"},
            {"label": "PFI overlay", "value": "Calderdale Royal Hospital is itself PFI-owned — hereditament treatment for service-concession assets clarified under NDR Multipliers Act 2024"},
            {"label": "2023 revaluation context", "value": "Rateable values reset from April 2023 per VOA 2023 List"},
            {"label": "NHS NDR exemption status", "value": "NHS bodies are NOT exempt from NDR — full ratepayer status"},
            {"label": "Funding trajectory", "value": "2021-22 c. £1.8M → 2022-23 c. £1.9M → 2023-24 c. £2.0M → 2024-25 £2.061M — multiplier uplift + revaluation passthrough"},
            {"label": "Delivery body", "value": "VOA (rateable value) + Calderdale Council + Kirklees Council (billing) + Trust E&F + finance"},
            {"label": "Policy owner", "value": "DHSC + HM Treasury (multiplier) + DLUHC (NDR policy) + VOA + NHSE Provider Finance + West Yorkshire ICB"},
            {"label": "Evaluation evidence", "value": "VOA 2023 Revaluation; NAO Business Rates Reform 2014; NAO NHP report 2023; NHS Confederation NDR briefings; Trust ARA 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2017 Rating List · Current: 2023 Rating List · Successor: 2026 Revaluation cycle + post-NHP-Reset reconfiguration impact"}
        ],
        "notes": "Calderdale and Huddersfield's business rates line reflects a twin-borough West Yorkshire footprint with hereditaments billed separately by Calderdale Council and Kirklees Council using VOA 2023 List rateable values. The trust's reconfiguration scheme (originally splitting unscheduled care to Halifax / planned to Huddersfield and rebuilding HRI) sits in the NHP cohort that was deferred under the January 2025 NHP Reset (publication May 2025) — meaning the 2024-25 rates baseline persists into the medium term. Calderdale Royal Hospital is itself PFI-owned (the £2.061M is rates on hereditaments distinct from the unitary charge) — service-concession hereditament treatment was clarified under the NDR (Multipliers and Private Finance) Act 2024. NHS bodies are full ratepayers with no general exemption.",
        "sources": [
            {"publisher": "Calderdale and Huddersfield NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.cht.nhs.uk/about-us/publications/"},
            {"publisher": "Valuation Office Agency", "title": "2023 Rating List", "url": "https://www.gov.uk/government/organisations/valuation-office-agency"},
            {"publisher": "UK Government", "title": "Non-Domestic Rating (Multipliers and Private Finance) Act 2024", "url": "https://www.legislation.gov.uk/ukpga/2024/19/contents"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "National Audit Office", "title": "New Hospital Programme", "url": "https://www.nao.org.uk/reports/new-hospital-programme/"}
        ],
        "related": ["Calderdale and Huddersfield NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Business rates — Doncaster and Bassetlaw Teaching Hospitals NHS Foundation Trust", "Business rates — Worcestershire Acute Hospitals NHS Trust", "Valuation Office Agency"]
    },
    "Amortisation — Northampton General Hospital NHS Trust": {
        "aliases": [{"name": "Amortisation", "parent": "Northampton General Hospital NHS Trust"}],
        "description": "Northampton General Hospital NHS Trust's £2.035M amortisation line covers IAS 38-compliant write-down of intangible assets — capitalised software (EPR + clinical systems), licences and SaaS implementation costs (per IFRIC 2021 agenda decision) — at the single Northampton General Hospital site. NGH operates in a Group arrangement with Kettering General Hospital NHSFT (University Hospitals of Northamptonshire Group), with shared digital strategy driving converging EPR capitalisation across both trusts. Frontline Digitisation programme funding feeds the upward amort cycle.",
        "beneficiaries": "c. 5,500 WTE staff serving a c. 380,000 Northampton + South Northants catchment; c. 105,000 ED attendances/yr at Northampton General ED; c. 70,000 admissions/yr; the trust hosts regional cancer + maternity tertiary specialty footprint as part of the University Hospitals of Northamptonshire Group with KGH.",
        "legal_basis": "IAS 38 Intangible Assets — IFRIC Agenda Decision SaaS Configuration & Customisation Costs (2021) — DHSC Group Accounting Manual 2024-25 ch.5 — NHS Act 2006 — Health and Care Act 2022 — HM Treasury FReM",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£2.035M"},
            {"label": "Trust scale", "value": "Northampton General Hospital (single-site DGH); c. 5,500 WTE"},
            {"label": "University Hospitals of Northamptonshire Group", "value": "Group arrangement with Kettering General Hospital NHSFT — shared digital + corporate services drive EPR convergence"},
            {"label": "EPR / Frontline Digitisation", "value": "Group-wide EPR strategy under Frontline Digitisation programme — capitalisation cycle drives forward-curve intangibles"},
            {"label": "Composition", "value": "Capitalised software + licences + SaaS implementation costs (per IFRIC 2021) + acquired intangible rights"},
            {"label": "Useful life", "value": "Software typically 3-7 years per DHSC GAM ch.5; licences over contractual term"},
            {"label": "Funding trajectory", "value": "2021-22 c. £1.6M → 2023-24 c. £1.95M → 2024-25 £2.035M — Frontline Digitisation EPR capitalisation feeding amort cycle"},
            {"label": "Delivery body", "value": "Trust IT + digital + finance functions + Group-wide UHN digital function; software vendors"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + NHSE Transformation Directorate (Frontline Digitisation) + DHSC + Northamptonshire ICB"},
            {"label": "Evaluation evidence", "value": "NAO Digital Transformation in the NHS 2020; Wachter Review 2016; NHSE Frontline Digitisation guidance; Trust ARA 2023-24"},
            {"label": "IFRIC 2021 SaaS impact", "value": "Some EPR cloud-implementation costs now expensed rather than capitalised — dampens but does not reverse upward trend"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-Group separate NGH/KGH digital systems · Successor: UHN Group-wide EPR convergence + Frontline Digitisation Level-5 maturity target"}
        ],
        "notes": "Northampton General's amortisation line reflects a smaller single-site DGH operating in the University Hospitals of Northamptonshire Group with Kettering General — Group-wide EPR strategy and shared digital corporate services drive converging capitalised-software portfolios across both trusts. The Frontline Digitisation programme funds Level-5 maturity capitalisation cycles; the IFRIC 2021 SaaS agenda decision tightened capitalisation rules (some implementation costs expensed rather than capitalised). Industrial action 2023-24 affected backfill costs indirectly; April 2025 NIC step-up applies to vendor / contractor labour pass-through. The UHN Group is one of the more advanced England Acute trust-pair group models — its digital convergence is a useful comparator for the Hampshire Hospitals + Royal Surrey, Northern Care Alliance and similar groups.",
        "sources": [
            {"publisher": "Northampton General Hospital NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.northamptongeneral.nhs.uk/About/Annual-Reports.aspx"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 5 — Intangible assets)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "IFRS Foundation", "title": "Configuration or Customisation Costs in a Cloud Computing Arrangement (IFRIC Agenda Decision, April 2021)", "url": "https://www.ifrs.org/news-and-events/updates/ifric/2021/ifric-update-april-2021/"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/connecting-health-and-care-providers/frontline-digitisation/"},
            {"publisher": "National Audit Office", "title": "Digital transformation in the NHS", "url": "https://www.nao.org.uk/reports/the-digital-transformation-in-the-nhs/"}
        ],
        "related": ["Northampton General Hospital NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Amortisation — King’s College Hospital NHS Foundation Trust", "Amortisation — Hull University Teaching Hospitals NHS Trust", "NHS England"]
    },
    "Business rates — Worcestershire Acute Hospitals NHS Trust": {
        "aliases": [{"name": "Business rates", "parent": "Worcestershire Acute Hospitals NHS Trust"}],
        "description": "Worcestershire Acute Hospitals NHS Trust's £2.031M business rates line covers non-domestic rates on the trust's hereditaments at Worcestershire Royal Hospital (Worcester), Alexandra Hospital (Redditch) and Kidderminster Hospital plus community sites. Rateable values follow the 2023 NDR revaluation and HM Treasury multipliers under the Non-Domestic Rating (Multipliers and Private Finance) Act 2024. Hereditaments span three district billing authorities (Worcester City, Redditch BC, Wyre Forest DC). Worcestershire Royal is itself a PFI hospital with separate hereditament treatment for service-concession assets.",
        "beneficiaries": "c. 6,000 WTE staff serving a c. 600,000 Worcestershire catchment (Worcester, Redditch, Bromsgrove, Wyre Forest, Malvern, Wychavon); c. 165,000 ED attendances/yr (Worcestershire Royal ED + Alexandra ED); c. 85,000 admissions/yr; ratepayer profile reflects three district billing authorities under a county-wide trust footprint.",
        "legal_basis": "Local Government Finance Act 1988 (Schedule 6) — Non-Domestic Rating Act 2023 — Non-Domestic Rating (Multipliers and Private Finance) Act 2024 — DHSC Group Accounting Manual 2024-25 — NHS Act 2006 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£2.031M"},
            {"label": "Trust scale", "value": "Worcestershire Royal Hospital (Worcester) + Alexandra Hospital (Redditch) + Kidderminster Hospital + community sites; c. 6,000 WTE"},
            {"label": "Billing authorities", "value": "Worcester City Council + Redditch Borough Council + Wyre Forest District Council — three-district county footprint"},
            {"label": "PFI overlay", "value": "Worcestershire Royal Hospital is PFI-built (Catalyst Healthcare Worcester) — hereditament treatment for service-concession assets clarified under NDR Multipliers Act 2024"},
            {"label": "2023 revaluation context", "value": "Rateable values reset from April 2023 per VOA 2023 List"},
            {"label": "NHS NDR exemption status", "value": "NHS bodies are NOT exempt from NDR — full ratepayer status"},
            {"label": "Long-running reconfiguration context", "value": "Worcestershire Acute services reconfiguration (Three Counties / Future of Acute Hospital Services in Worcestershire) shapes hereditament profile through to NHP horizon"},
            {"label": "Funding trajectory", "value": "2021-22 c. £1.8M → 2022-23 c. £1.9M → 2023-24 c. £1.95M → 2024-25 £2.031M — multiplier uplift + revaluation passthrough"},
            {"label": "Delivery body", "value": "VOA (rateable value) + Worcester City + Redditch BC + Wyre Forest DC (billing) + Trust E&F + finance"},
            {"label": "Policy owner", "value": "DHSC + HM Treasury (multiplier) + DLUHC (NDR policy) + VOA + NHSE Provider Finance + Herefordshire & Worcestershire ICB"},
            {"label": "Evaluation evidence", "value": "VOA 2023 Revaluation; NAO Business Rates Reform 2014; CQC RWP inspections; NHS Confederation NDR briefings; Trust ARA 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2017 Rating List · Current: 2023 Rating List · Successor: 2026 Revaluation cycle + post-reconfiguration estate consolidation"}
        ],
        "notes": "Worcestershire Acute Hospitals' business rates line reflects a county-wide footprint with three district billing authorities (Worcester City, Redditch BC, Wyre Forest DC) using VOA 2023 List rateable values. Worcestershire Royal Hospital is itself PFI-built (Catalyst Healthcare Worcester contract) — hereditament treatment for service-concession assets was clarified under the NDR (Multipliers and Private Finance) Act 2024. The long-running Future of Acute Hospital Services in Worcestershire reconfiguration shapes the medium-term estate profile. NHS bodies are full ratepayers with no general exemption. April 2025 NIC step-up does not affect NDR liability directly but does affect FM contractor labour. 2026 Revaluation cycle is the next inflection point.",
        "sources": [
            {"publisher": "Worcestershire Acute Hospitals NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.worcsacute.nhs.uk/about-us/our-publications"},
            {"publisher": "Valuation Office Agency", "title": "2023 Rating List", "url": "https://www.gov.uk/government/organisations/valuation-office-agency"},
            {"publisher": "UK Government", "title": "Non-Domestic Rating (Multipliers and Private Finance) Act 2024", "url": "https://www.legislation.gov.uk/ukpga/2024/19/contents"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Worcestershire Acute Hospitals provider profile (RWP)", "url": "https://www.cqc.org.uk/provider/RWP"}
        ],
        "related": ["Worcestershire Acute Hospitals NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Business rates — Doncaster and Bassetlaw Teaching Hospitals NHS Foundation Trust", "Business rates — Calderdale and Huddersfield NHS Foundation Trust", "Valuation Office Agency"]
    },
    "Amortisation — Chesterfield Royal Hospital NHS Foundation Trust": {
        "aliases": [{"name": "Amortisation", "parent": "Chesterfield Royal Hospital NHS Foundation Trust"}],
        "description": "Chesterfield Royal Hospital NHSFT's £2.027M amortisation line covers IAS 38-compliant write-down of intangible assets — capitalised software (EPR + clinical systems), licences and SaaS implementation costs (per IFRIC 2021 agenda decision) — at the single Chesterfield Royal Hospital site (Calow). The trust runs Royal Primary Care subsidiary (GP federation) and Derbyshire Support and Facilities Services (DSFS) wholly-owned subsidiary providing FM services across Derbyshire NHS — distinctive group-structure shaping intangible-asset capitalisation choices.",
        "beneficiaries": "c. 4,000 WTE staff serving a c. 400,000 North Derbyshire + High Peak catchment (Chesterfield, Bolsover, NE Derbyshire, Dales); c. 100,000 ED attendances/yr at Chesterfield Royal Hospital ED; c. 65,000 admissions/yr; trust also runs DSFS subsidiary providing FM services to multiple Derbyshire NHS bodies + Royal Primary Care GP federation.",
        "legal_basis": "IAS 38 Intangible Assets — IFRIC Agenda Decision SaaS Configuration & Customisation Costs (2021) — DHSC GAM 2024-25 ch.5 — NHS Act 2006 — Health and Care Act 2022 — HM Treasury FReM",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£2.027M"},
            {"label": "Trust scale", "value": "Chesterfield Royal Hospital (Calow); c. 4,000 WTE; plus DSFS + Royal Primary Care subsidiary structure"},
            {"label": "Subsidiary structure", "value": "Derbyshire Support and Facilities Services (DSFS) wholly-owned subsidiary + Royal Primary Care GP federation — group-level capitalisation choices"},
            {"label": "EPR / Frontline Digitisation", "value": "Frontline Digitisation programme funding feeds upward amort cycle; Joined Up Care Derbyshire (JUCD) ICS digital convergence shapes EPR strategy"},
            {"label": "Composition", "value": "Capitalised software + licences + SaaS implementation costs (per IFRIC 2021) + acquired intangible rights"},
            {"label": "Useful life", "value": "Software typically 3-7 years per DHSC GAM ch.5; licences over contractual term"},
            {"label": "Funding trajectory", "value": "2021-22 c. £1.5M → 2023-24 c. £1.9M → 2024-25 £2.027M — Frontline Digitisation EPR capitalisation feeding amort cycle"},
            {"label": "Delivery body", "value": "Trust IT + digital + finance functions + DSFS subsidiary; software vendors"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + NHSE Transformation Directorate (Frontline Digitisation) + DHSC + Derbyshire ICB (JUCD)"},
            {"label": "Evaluation evidence", "value": "NAO Digital Transformation in the NHS 2020; Wachter Review 2016; NHSE Frontline Digitisation guidance; Trust ARA 2023-24"},
            {"label": "JUCD ICS digital convergence", "value": "Joined Up Care Derbyshire ICS shared-EPR strategy with University Hospitals of Derby & Burton — shapes capitalisation roadmap"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-Frontline Digitisation patchwork systems · Successor: JUCD ICS shared-EPR + Frontline Digitisation Level-5 maturity target"}
        ],
        "notes": "Chesterfield Royal's amortisation line reflects a smaller single-site DGH with a distinctive subsidiary structure — Derbyshire Support and Facilities Services (DSFS) is the trust-owned FM company providing services to multiple Derbyshire NHS bodies, and Royal Primary Care is a GP federation subsidiary. Frontline Digitisation programme funding feeds the upward amort cycle, and the Joined Up Care Derbyshire ICS shared-EPR strategy with University Hospitals of Derby and Burton shapes the medium-term capitalisation roadmap. The IFRIC 2021 SaaS agenda decision tightened cloud-implementation capitalisation rules. April 2025 NIC step-up applies to vendor / contractor labour pass-through. Industrial action 2023-24 affected backfill costs indirectly.",
        "sources": [
            {"publisher": "Chesterfield Royal Hospital NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.chesterfieldroyal.nhs.uk/about-us/publications"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 5 — Intangible assets)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "IFRS Foundation", "title": "Configuration or Customisation Costs in a Cloud Computing Arrangement (IFRIC Agenda Decision, April 2021)", "url": "https://www.ifrs.org/news-and-events/updates/ifric/2021/ifric-update-april-2021/"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/connecting-health-and-care-providers/frontline-digitisation/"},
            {"publisher": "National Audit Office", "title": "Digital transformation in the NHS", "url": "https://www.nao.org.uk/reports/the-digital-transformation-in-the-nhs/"}
        ],
        "related": ["Chesterfield Royal Hospital NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Amortisation — Hull University Teaching Hospitals NHS Trust", "Amortisation — Wirral University Teaching Hospital NHS Foundation Trust", "NHS England"]
    },
    "Amortisation — Wirral University Teaching Hospital NHS Foundation Trust": {
        "aliases": [{"name": "Amortisation", "parent": "Wirral University Teaching Hospital NHS Foundation Trust"}],
        "description": "Wirral University Teaching Hospital NHSFT's £2.025M amortisation line covers IAS 38-compliant write-down of intangible assets — capitalised software (EPR + clinical systems), licences and SaaS implementation costs (per IFRIC 2021 agenda decision) — across Arrowe Park Hospital (Upton) and Clatterbridge Hospital (Bebington) sites on the Wirral. The trust sits within Cheshire & Merseyside ICS provider-collaborative arrangements; its EPR strategy (Cerner Millennium legacy) is increasingly converged with C&M-wide Frontline Digitisation roadmap.",
        "beneficiaries": "c. 6,800 WTE staff serving a c. 320,000 Wirral peninsula catchment plus partial flows from West Cheshire and North Wales; c. 145,000 ED attendances/yr at Arrowe Park ED; c. 75,000 admissions/yr; the trust hosts the Wirral Women & Children's Hospital and shares the Clatterbridge campus with the separate Clatterbridge Cancer Centre NHSFT (specialty oncology partner).",
        "legal_basis": "IAS 38 Intangible Assets — IFRIC Agenda Decision SaaS Configuration & Customisation Costs (2021) — DHSC GAM 2024-25 ch.5 — NHS Act 2006 — Health and Care Act 2022 — HM Treasury FReM",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£2.025M"},
            {"label": "Trust scale", "value": "Arrowe Park Hospital (Upton) + Clatterbridge Hospital (Bebington); c. 6,800 WTE"},
            {"label": "EPR legacy", "value": "Cerner Millennium legacy EPR — Frontline Digitisation programme funds maturation + roadmap convergence with Liverpool / C&M wider"},
            {"label": "C&M ICS context", "value": "Cheshire & Merseyside ICS provider-collaborative shared-services with Liverpool University Hospitals + St Helens & Knowsley + Warrington & Halton"},
            {"label": "Composition", "value": "Capitalised software + licences + SaaS implementation costs (per IFRIC 2021) + acquired intangible rights"},
            {"label": "Useful life", "value": "Software typically 3-7 years per DHSC GAM ch.5; licences over contractual term"},
            {"label": "Funding trajectory", "value": "2021-22 c. £1.6M → 2023-24 c. £1.9M → 2024-25 £2.025M — Frontline Digitisation EPR capitalisation feeding amort cycle"},
            {"label": "Delivery body", "value": "Trust IT + digital + finance functions; software vendors (Cerner / Oracle Health post-acquisition)"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + NHSE Transformation Directorate (Frontline Digitisation) + DHSC + Cheshire & Merseyside ICB"},
            {"label": "Evaluation evidence", "value": "NAO Digital Transformation in the NHS 2020; Wachter Review 2016; NHSE Frontline Digitisation guidance; Trust ARA 2023-24"},
            {"label": "Clatterbridge campus context", "value": "Clatterbridge campus shared with Clatterbridge Cancer Centre NHSFT (separate trust) — adds digital interface complexity to capitalisation"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-Frontline Digitisation Cerner Millennium baseline · Successor: Oracle Health convergence + C&M ICS shared-EPR + Level-5 maturity target"}
        ],
        "notes": "Wirral's amortisation line reflects a typical mid-sized Acute trust transitioning Cerner Millennium EPR (now Oracle Health post-acquisition) under the Frontline Digitisation programme — capitalised replacement and maturation costs feed the upward curve. The Cheshire & Merseyside ICS provider-collaborative shared-services strategy with Liverpool University Hospitals + St Helens & Knowsley + Warrington & Halton shapes the medium-term roadmap. The Clatterbridge campus is shared with the separate Clatterbridge Cancer Centre NHSFT (specialty oncology trust) — the inter-trust digital interface adds capitalisation complexity. IFRIC 2021 SaaS agenda decision dampens but does not reverse the capitalisation upward trend. April 2025 NIC step-up applies via vendor/contractor labour pass-through.",
        "sources": [
            {"publisher": "Wirral University Teaching Hospital NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.wuth.nhs.uk/about-us/publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 5 — Intangible assets)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "IFRS Foundation", "title": "Configuration or Customisation Costs in a Cloud Computing Arrangement (IFRIC Agenda Decision, April 2021)", "url": "https://www.ifrs.org/news-and-events/updates/ifric/2021/ifric-update-april-2021/"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/connecting-health-and-care-providers/frontline-digitisation/"},
            {"publisher": "National Audit Office", "title": "Digital transformation in the NHS", "url": "https://www.nao.org.uk/reports/the-digital-transformation-in-the-nhs/"}
        ],
        "related": ["Wirral University Teaching Hospital NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Amortisation — Chesterfield Royal Hospital NHS Foundation Trust", "Amortisation — Hull University Teaching Hospitals NHS Trust", "NHS England"]
    },
    "General supplies & services — The Dudley Group NHS Foundation Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "The Dudley Group NHS Foundation Trust"}],
        "description": "The Dudley Group NHSFT's £2.018M general supplies and services line covers operational consumables outside specific clinical / drugs / surgical categories — non-clinical consumables, hotel-services consumables (cleaning, linen, food-service), uniform / PPE non-clinical, ward consumables and minor non-pay supply categories — across Russells Hall Hospital (Dudley), Corbett Hospital (Stourbridge) and Dudley Guest Hospital sites. Procurement runs through NHS Supply Chain national framework with trust-direct top-up sourcing. Black Country ICS provider-collaborative shapes shared-procurement strategy.",
        "beneficiaries": "c. 4,500 WTE staff serving a c. 320,000 Dudley + Stourbridge + Halesowen catchment; c. 130,000 ED attendances/yr at Russells Hall ED; c. 75,000 admissions/yr; trust within Black Country ICS alongside Sandwell & West Birmingham, Royal Wolverhampton, Walsall.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) — IAS 2 Inventories — NHS Act 2006 — Health and Care Act 2022 — HM Treasury FReM",
        "key_stats": [
            {"label": "General supplies & services 2024-25", "value": "£2.018M"},
            {"label": "Trust scale", "value": "Russells Hall Hospital (Dudley) + Corbett Hospital (Stourbridge) + Guest Hospital + community sites; c. 4,500 WTE"},
            {"label": "Composition", "value": "Non-clinical consumables + hotel-services consumables + uniforms / non-clinical PPE + ward consumables + minor non-pay supply categories"},
            {"label": "Procurement channel", "value": "NHS Supply Chain national framework + trust-direct top-up; NHSE Procurement Target Operating Model alignment"},
            {"label": "Black Country ICS context", "value": "Provider-collaborative shared-procurement with Sandwell & West Birmingham, Royal Wolverhampton, Walsall — converging supply contracts shape unit-cost trajectory"},
            {"label": "Russells Hall PFI overlay", "value": "Russells Hall is PFI-built (Summit Healthcare) — soft-FM hotel-services overlap with separate PFI unitary charge but consumables sourced via Trust"},
            {"label": "Industrial action 2023-24 effect", "value": "Strike-period catering / linen / consumables demand fluctuation feeds line variability"},
            {"label": "April 2025 NIC + supplier passthrough", "value": "Supply Chain framework prices reflect supplier NIC pass-through from April 2025; cumulative CPI on consumables sustains upward pressure"},
            {"label": "Funding trajectory", "value": "2021-22 c. £1.6M → 2023-24 c. £1.95M → 2024-25 £2.018M — CPI on consumables + activity recovery + Frontline Digitisation transition"},
            {"label": "Delivery body", "value": "Trust procurement + ward / clinical-unit ordering; NHS Supply Chain (national framework) + direct suppliers"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + NHS Supply Chain + DHSC + Black Country ICB"},
            {"label": "Evaluation evidence", "value": "NAO NHS Supply Chain 2019 + 2024; Carter Review legacy 2016; CQC RNA inspections; NHSE Procurement TOM; Trust ARA 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-Carter unbenchmarked supply baseline · Successor: Black Country ICS shared-procurement consolidation + NHSE Procurement Target Operating Model maturity"}
        ],
        "notes": "The Dudley Group's general supplies and services line reflects a typical mid-sized Acute trust supply profile — non-clinical consumables, hotel-services consumables and ward-level supplies sourced via NHS Supply Chain national framework with trust-direct top-up. The Black Country ICS provider-collaborative shared-procurement strategy with Sandwell & West Birmingham, Royal Wolverhampton and Walsall is converging contract terms across the four ICS Acute providers. Russells Hall Hospital is PFI-built (Summit Healthcare contract) — soft-FM hotel services run through the PFI unitary charge separately, but consumables remain trust-sourced. CPI on consumables, April 2025 NIC supplier pass-through, and Black Country ICS procurement consolidation drive the medium-term trajectory. Carter Review / Model Hospital benchmarking remains the productivity lever.",
        "sources": [
            {"publisher": "The Dudley Group NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://dgft.nhs.uk/about-us/publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS Supply Chain", "title": "About NHS Supply Chain — Operating Model", "url": "https://www.supplychain.nhs.uk/"},
            {"publisher": "National Audit Office", "title": "NHS Supply Chain", "url": "https://www.nao.org.uk/reports/nhs-supply-chain-and-efficiency-in-the-health-service/"},
            {"publisher": "Care Quality Commission", "title": "The Dudley Group provider profile (RNA)", "url": "https://www.cqc.org.uk/provider/RNA"}
        ],
        "related": ["The Dudley Group NHS Foundation Trust", "Clinical Supplies & Drugs", "NHS Acute Trusts", "NHS Supply Chain", "General supplies & services — Liverpool University Hospitals NHS Foundation Trust", "General supplies & services — North Middlesex University Hospital NHS Trust"]
    },
    "Business rates — South Warwickshire NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "South Warwickshire NHS Foundation Trust"}],
        "description": "South Warwickshire NHSFT's £2.011M business rates line covers non-domestic rates on the trust's hereditaments at Warwick Hospital, Stratford-upon-Avon Hospital, Ellen Badger Hospital (Shipston) plus community sites across South Warwickshire. The trust is unusual in providing integrated acute + community + mental-health services within a single Foundation Trust footprint. Rateable values follow the 2023 NDR revaluation under the Non-Domestic Rating (Multipliers and Private Finance) Act 2024. Hereditaments span multiple billing authorities (Warwick DC + Stratford-on-Avon DC).",
        "beneficiaries": "c. 5,000 WTE staff serving a c. 290,000 South Warwickshire catchment (Warwick, Leamington Spa, Stratford, Shipston, Kenilworth, Henley-in-Arden); c. 75,000 ED attendances/yr at Warwick Hospital ED; c. 55,000 admissions/yr; integrated acute + community + MH model uniquely within South Warwickshire footprint.",
        "legal_basis": "Local Government Finance Act 1988 (Schedule 6) — Non-Domestic Rating Act 2023 — Non-Domestic Rating (Multipliers and Private Finance) Act 2024 — DHSC Group Accounting Manual 2024-25 — NHS Act 2006 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£2.011M"},
            {"label": "Trust scale", "value": "Warwick Hospital + Stratford-upon-Avon Hospital + Ellen Badger Hospital (Shipston) + community sites; c. 5,000 WTE"},
            {"label": "Billing authorities", "value": "Warwick District Council + Stratford-on-Avon District Council — twin-district South Warwickshire footprint"},
            {"label": "Integrated provider model", "value": "Acute + community + mental-health services within single Foundation Trust — distinctive model in England"},
            {"label": "2023 revaluation context", "value": "Rateable values reset from April 2023 per VOA 2023 List"},
            {"label": "NHS NDR exemption status", "value": "NHS bodies are NOT exempt from NDR — full ratepayer status"},
            {"label": "Community estate footprint", "value": "Community-clinic hereditaments disproportionately relevant for an integrated provider — multi-site community footprint adds rateable-value complexity"},
            {"label": "Coventry & Warwickshire ICS context", "value": "C&W ICS alongside University Hospitals Coventry & Warwickshire and George Eliot Hospital — ICS-wide estate strategy convergence"},
            {"label": "Funding trajectory", "value": "2021-22 c. £1.8M → 2022-23 c. £1.85M → 2023-24 c. £1.95M → 2024-25 £2.011M — multiplier uplift + revaluation passthrough"},
            {"label": "Delivery body", "value": "VOA (rateable value) + Warwick DC + Stratford-on-Avon DC (billing) + Trust E&F + finance"},
            {"label": "Policy owner", "value": "DHSC + HM Treasury (multiplier) + DLUHC (NDR policy) + VOA + NHSE Provider Finance + Coventry and Warwickshire ICB"},
            {"label": "Evaluation evidence", "value": "VOA 2023 Revaluation; NAO Business Rates Reform 2014; CQC RJC inspections; NHS Confederation NDR briefings; Trust ARA 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2017 Rating List · Current: 2023 Rating List · Successor: 2026 Revaluation cycle"}
        ],
        "notes": "South Warwickshire NHSFT's business rates line reflects a distinctive integrated acute + community + mental-health provider model with multi-site community-clinic hereditaments adding complexity to the rateable-value profile. Two district billing authorities (Warwick DC, Stratford-on-Avon DC) bill against VOA 2023 List values under HM Treasury multipliers per the Non-Domestic Rating (Multipliers and Private Finance) Act 2024. NHS bodies are full ratepayers with no general exemption. The Coventry and Warwickshire ICS estate-strategy convergence with UHCW and George Eliot is the medium-term shaper. April 2025 NIC step-up does not affect NDR liability directly but does affect FM contractor labour. 2026 Revaluation cycle is the next inflection point.",
        "sources": [
            {"publisher": "South Warwickshire NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.swft.nhs.uk/about-us/publications"},
            {"publisher": "Valuation Office Agency", "title": "2023 Rating List", "url": "https://www.gov.uk/government/organisations/valuation-office-agency"},
            {"publisher": "UK Government", "title": "Non-Domestic Rating (Multipliers and Private Finance) Act 2024", "url": "https://www.legislation.gov.uk/ukpga/2024/19/contents"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "South Warwickshire provider profile (RJC)", "url": "https://www.cqc.org.uk/provider/RJC"}
        ],
        "related": ["South Warwickshire NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Business rates — Doncaster and Bassetlaw Teaching Hospitals NHS Foundation Trust", "Business rates — Worcestershire Acute Hospitals NHS Trust", "Valuation Office Agency"]
    },
    "Transport (business + patient) — South Tyneside and Sunderland NHS Foundation Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "South Tyneside and Sunderland NHS Foundation Trust"}],
        "description": "South Tyneside and Sunderland NHSFT's £2.005M transport line covers business mileage (AfC Section 17 + AMAP), pool-fleet IFRS 16 lease costs, NEPTS contract pass-through and patient travel reimbursements across Sunderland Royal Hospital, South Tyneside District Hospital (South Shields) and Sunderland Eye Infirmary plus community sites. The trust formed in April 2019 from City Hospitals Sunderland + South Tyneside NHSFT merger — twin-site post-merger inter-hospital transfer flow drives substantial transport demand. NEPTS commissioned through North East and North Cumbria ICS lead-commissioner.",
        "beneficiaries": "c. 9,000 WTE staff serving a c. 430,000 Sunderland + South Tyneside catchment; c. 175,000 ED attendances/yr (Sunderland Royal ED + South Tyneside ED combined); c. 100,000 admissions/yr; trust hosts the Sunderland Eye Infirmary regional ophthalmology specialty hub.",
        "legal_basis": "NHS Act 2006 — NHSE Patient Transport Services Eligibility Criteria 2021 — Agenda for Change Section 17 (business mileage) — HMRC AMAP rates — IFRS 16 Leases (pool fleet) — DHSC Group Accounting Manual 2024-25 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£2.005M"},
            {"label": "Trust scale", "value": "Sunderland Royal Hospital + South Tyneside District Hospital (South Shields) + Sunderland Eye Infirmary + community sites; c. 9,000 WTE"},
            {"label": "Merger context", "value": "April 2019 City Hospitals Sunderland + South Tyneside NHSFT merger created twin-site Tyne-Wear Acute trust"},
            {"label": "Tertiary specialty", "value": "Sunderland Eye Infirmary regional ophthalmology hub — drives intermittent specialty-transfer demand"},
            {"label": "NEPTS commissioning", "value": "North East and North Cumbria ICS lead-commissioner NEPTS contract; eligibility per NHSE 2021 criteria"},
            {"label": "Composition", "value": "Business mileage (AfC S17 + AMAP 45p/25p frozen since 2011) + pool-fleet IFRS 16 leases + NEPTS pass-through + patient travel reimbursements"},
            {"label": "Inter-site transfers", "value": "Sunderland Royal <> South Tyneside cross-borough patient flows post-merger drive distinctive twin-site transport profile"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove cancellation rebooking + agency travel claims"},
            {"label": "April 2025 NIC + fuel CPI", "value": "Indirect via NEPTS contractor pass-through + diesel CPI feed forward unit-cost pressure"},
            {"label": "Funding trajectory", "value": "2021-22 c. £1.65M → 2023-24 c. £1.9M → 2024-25 £2.005M — fuel CPI + NEPTS contract uplift + activity recovery"},
            {"label": "Delivery body", "value": "Trust E&F + outsourced NEPTS provider (NENC ICS lead-commissioner) + pool-fleet leasing partner + Trust HR (mileage)"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + NHSE Urgent and Emergency Care (NEPTS) + North East and North Cumbria ICB + DHSC"},
            {"label": "Evaluation evidence", "value": "NAO NEPTS 2019; CQC R0B inspections; NHSE NEPTS Eligibility Review 2021; Trust ARA 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-merger separate City Hospitals Sunderland + South Tyneside transport budgets · Successor: NENC ICS-collaborative NEPTS retender + post-merger pool-fleet rationalisation"}
        ],
        "notes": "South Tyneside and Sunderland's transport line is shaped by the twin-site post-merger geography — Sunderland Royal Hospital and South Tyneside District Hospital straddle the Tyne-Wear borough boundary with substantial inter-site patient flows since the April 2019 merger of City Hospitals Sunderland and South Tyneside NHSFT. The Sunderland Eye Infirmary regional ophthalmology hub adds intermittent specialty-transfer demand. NEPTS is commissioned through the North East and North Cumbria ICS lead-commissioner under NHSE 2021 eligibility criteria. The HMRC AMAP-rate freeze at 45p/mile since 2011 sustains internal-rate dispute pressure; industrial action 2023-24 drove cancellation-rebooking; April 2025 NIC + diesel CPI feed forward via NEPTS contractor pass-through. Post-merger pool-fleet rationalisation is the medium-term lever.",
        "sources": [
            {"publisher": "South Tyneside and Sunderland NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.stsft.nhs.uk/about-us/publications"},
            {"publisher": "NHS England", "title": "Non-Emergency Patient Transport Services — National Framework + Eligibility Criteria 2021", "url": "https://www.england.nhs.uk/publication/non-emergency-patient-transport-services-nepts/"},
            {"publisher": "National Audit Office", "title": "NHS Ambulance Services / NEPTS oversight reports", "url": "https://www.nao.org.uk/reports/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "South Tyneside and Sunderland provider profile (R0B)", "url": "https://www.cqc.org.uk/provider/R0B"}
        ],
        "related": ["South Tyneside and Sunderland NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Transport (business + patient) — Somerset NHS Foundation Trust", "Transport (business + patient) — Mid Cheshire Hospitals NHS Foundation Trust", "Transport (business + patient) — Salisbury NHS Foundation Trust"]
    },
}
