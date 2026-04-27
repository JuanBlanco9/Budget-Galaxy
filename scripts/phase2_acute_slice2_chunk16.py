# -*- coding: utf-8 -*-
# Phase 2 Acute slice 2 — chunk 16 (17 NHS Acute Trust orphan sub-lines)
# Hand-curated trust-specific PROGRAMME-archetype enrichment entries.
# Structural contract per docs/archetype_briefs.md.

NEW = {
    "Amortisation — University Hospitals of Leicester NHS Trust": {
        "aliases": [{"name": "Amortisation", "parent": "University Hospitals of Leicester NHS Trust"}],
        "description": "UHL's £5.113M amortisation line covers the systematic write-down of capitalised intangible assets — software licences, the Nervecentre EPR, capitalised configuration costs, radiology PACS, internally-generated clinical applications and acquired digital systems — across the three-site Leicester Royal Infirmary + Glenfield Hospital + Leicester General estate. UHL is among England's largest acute trusts and a NHP cohort site (Leicester reconfiguration), whose intangible-asset baseline flows through IAS 38 over typical 5-10 year UELs.",
        "beneficiaries": "c. 17,000 WTE staff serving a c. 1.1M Leicester, Leicestershire and Rutland catchment plus East Midlands tertiary referrals (cardiac, renal, vascular, neonatal); c. 220,000 ED attendances/yr at Leicester Royal Infirmary ED — among the busiest single-site EDs in England; c. 170,000 elective + day-case admissions/yr; Glenfield = East Midlands Congenital Heart Centre.",
        "legal_basis": "IAS 38 Intangible Assets · IFRIC 22 SaaS configuration/customisation costs (March 2021 agenda decision) · DHSC Group Accounting Manual 2024-25 ch.5 · NHS Act 2006 · Health and Care Act 2022 · NHSE Frontline Digitisation programme guidance",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£5.113M"},
            {"label": "Trust scale", "value": "Three-site acute (Leicester Royal Infirmary + Glenfield + Leicester General); c. 17,000 WTE"},
            {"label": "Asset base composition", "value": "Nervecentre EPR + radiology PACS + capitalised software + internally-generated clinical apps; 5-10yr UEL per IAS 38 / DHSC GAM ch.5"},
            {"label": "IFRIC 22 effect", "value": "March 2021 SaaS configuration/customisation agenda decision reshaped capitalisation boundary; some costs reclassified opex"},
            {"label": "Frontline Digitisation context", "value": "NHSE Frontline Digitisation funds EPR rollouts to 'core' standard by 2026 — UHL receiving FD investment"},
            {"label": "NHP Leicester reconfiguration", "value": "Leicester three-site reconfiguration is a NHP cohort scheme (rephased at Jan 2025 Reset) — pre-construction intangibles flow through amortisation"},
            {"label": "Funding trajectory", "value": "2021-22 c. £4M → 2023-24 £4.7M → 2024-25 £5.113M — sustained intangible-asset additions through Frontline Digitisation"},
            {"label": "Delivery body", "value": "Trust IT + Digital programme office + Nervecentre + DHSC Frontline Digitisation funding + LLR ICB digital pillar"},
            {"label": "Policy owner", "value": "DHSC + NHSE Frontline Digitisation + NHSE Provider Finance + Leicester, Leicestershire and Rutland ICB"},
            {"label": "Evaluation evidence", "value": "NHSE Frontline Digitisation programme evaluation; NAO Digital Transformation in the NHS (HC 8, 2020); Trust ARA disclosure"},
            {"label": "Predecessor / successor", "value": "Predecessor: legacy ICE / standalone clinical systems · Successor: convergent Nervecentre + integrated PACS + AI-clinical-decision modules amortising 2024-2030+"}
        ],
        "notes": "UHL's amortisation reflects sustained capitalisation of the Nervecentre EPR rollout and the wider Frontline Digitisation programme investment — software licences, implementation labour and configuration costs flow through IAS 38 over typical 5-10 year UELs, with the IFRIC 22 March 2021 agenda decision having reshaped the capitalisation boundary and pushed some configuration cost to opex. The Leicester three-site reconfiguration sits in the New Hospital Programme cohort and was rephased at the January 2025 NHP Reset, with downstream implications for any pre-construction intangibles already capitalised. NHSE's 2026 'core' EPR target keeps the sector trajectory upward; UHL's first full year of post-rollout amortisation sets the new baseline above the 2021-22 level.",
        "sources": [
            {"publisher": "University Hospitals of Leicester NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.leicestershospitals.nhs.uk/aboutus/our-publications/"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/connecting-health-and-care-providers/frontline-digitisation/"},
            {"publisher": "National Audit Office", "title": "Digital transformation in the NHS (HC 8, 2020)", "url": "https://www.nao.org.uk/reports/the-use-of-digital-technology-in-the-nhs/"},
            {"publisher": "IFRS Foundation / IFRIC", "title": "Configuration or customisation costs in a cloud computing arrangement (IFRIC March 2021 agenda decision)", "url": "https://www.ifrs.org/news-and-events/news/2021/04/ifric-update-march-2021/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 5)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "UHL provider profile (RWE)", "url": "https://www.cqc.org.uk/provider/RWE"}
        ],
        "related": ["University Hospitals of Leicester NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Frontline Digitisation Programme", "Amortisation — Guy's & St Thomas' NHS Foundation Trust", "New Hospital Programme"]
    },
    "Establishment costs — Wye Valley NHS Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "Wye Valley NHS Trust"}],
        "description": "Wye Valley's £5.07M establishment costs line covers postage, telephony, printing, recruitment-advertising, training, conferences, subscriptions and legal & professional fees across the Hereford County Hospital + integrated Herefordshire community-services footprint. The integrated acute + community model in the H&W ICS, the rural geography sustaining hard-to-fill consultant recruitment, and the original Hereford Hospital PFI (signed 1998) drive an establishment baseline above peer single-site DGHs.",
        "beneficiaries": "c. 3,000 WTE staff serving a c. 190,000 Herefordshire catchment plus integrated community services across the county; c. 70,000 ED attendances/yr at Hereford County ED; c. 30,000 admissions/yr; integrated community workforce (district nursing, community paediatric, sexual-health, school-nursing).",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25 · Public Contracts Regulations 2015 / Procurement Act 2023",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£5.07M"},
            {"label": "Trust scale", "value": "Single acute site (Hereford County Hospital) + integrated Herefordshire community services; c. 3,000 WTE"},
            {"label": "Composition", "value": "Postage + telephony + print + recruitment-advertising + training + conferences + subscriptions + legal & professional fees"},
            {"label": "Hereford PFI context", "value": "Hereford Hospital PFI signed 1998 (first-wave NHS PFI); operational 2002 — sustained PFI contract-management professional fees"},
            {"label": "Rural recruitment driver", "value": "Hard-to-fill consultant + middle-grade recruitment across rural Herefordshire — agency-recruitment + advertising fees above urban peers"},
            {"label": "Industrial action 2023-24", "value": "44 days junior-doctor + 10 days consultant strikes drove agency-engagement + recruitment-advertising professional fees"},
            {"label": "April 2025 NIC + CPI", "value": "Apr 2025 NIC step-up raises forward professional-fee + recruitment-retainer cost; CPI on print/post/conference inputs"},
            {"label": "Funding trajectory", "value": "2021-22 c. £3.8M → 2023-24 £4.6M → 2024-25 £5.07M — sustained recruitment churn + PFI legacy"},
            {"label": "Delivery body", "value": "Trust Corporate Services + HR + Finance + IT + Communications + external counsel + PFI contract-management team"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Herefordshire & Worcestershire ICB + IPA PFI Hand-Back unit"},
            {"label": "Evaluation evidence", "value": "Model Hospital corporate-services benchmarks; NAO PFI hand-back report 2020; Trust ARA disclosure; CQC inspection (RLQ)"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2011 separate Hereford Hospitals + Herefordshire PCT baselines · Successor: H&W ICB shared corporate-services + Hereford PFI hand-back towards 2032"}
        ],
        "notes": "Wye Valley's establishment baseline is shaped by three drivers: the integrated acute + community model (district nursing, community-paediatric, sexual-health, school-nursing) broadens the corporate-services overhead vs acute-only peers; the rural-Herefordshire recruitment problem sustains agency-recruitment and advertising professional fees on hard-to-fill consultant and middle-grade posts; and the legacy 1998-signed Hereford Hospital PFI (first-wave, expiring c. 2032) continues to absorb contract-management professional fees layered on Carillion-collapse-era FM novation churn. Industrial action 2023-24 lifted advertising and agency-engagement; April 2025 NIC step-up and CPI feed forward; H&W ICB shared-services pooling is the medium-term lever.",
        "sources": [
            {"publisher": "Wye Valley NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.wyevalley.nhs.uk/about-us/key-publications/annual-report.aspx"},
            {"publisher": "National Audit Office", "title": "Managing PFI assets and services as contracts end (HC 632, 2020)", "url": "https://www.nao.org.uk/reports/managing-pfi-assets-and-services-as-contracts-end/"},
            {"publisher": "Infrastructure and Projects Authority", "title": "PFI Hand-Back Resource Centre", "url": "https://www.gov.uk/government/collections/pfi-and-pf2"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Wye Valley NHS Trust provider profile (RLQ)", "url": "https://www.cqc.org.uk/provider/RLQ"}
        ],
        "related": ["Wye Valley NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Establishment costs — Bedfordshire Hospitals NHS Foundation Trust", "PFI / LIFT charges — Worcestershire Acute Hospitals NHS Trust", "Department of Health and Social Care"]
    },
    "Transport (business + patient) — East Suffolk and North Essex NHS Foundation Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "East Suffolk and North Essex NHS Foundation Trust"}],
        "description": "ESNEFT's £5.055M transport line covers staff business mileage under AfC Section 17 + HMRC AMAP, pool fleet (lease + fuel) under IFRS 16, contracted patient transport services under NHSE PTS Eligibility, and inter-site transfers between Ipswich Hospital and Colchester Hospital — separated by c. 30 miles of A12 / A14 corridor. The trust formed July 2018 via Ipswich + Colchester merger, and the dual-hub geography combined with rural Suffolk + north Essex catchment drives a sustained transport baseline above peer single-site DGHs.",
        "beneficiaries": "c. 11,000 WTE staff serving a c. 1.0M east Suffolk + north Essex catchment (Ipswich, Colchester, Felixstowe, Tendring); c. 200,000 ED attendances/yr (Ipswich + Colchester EDs combined); c. 100,000 elective + day-case admissions/yr; PTS volume substantial across rural geography.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 + IFRS 16 Leases (pool fleet) · NHS Act 2006 · NHSE Patient Transport Services Eligibility Criteria · AfC Section 17 + HMRC Approved Mileage Allowance Payments · Health and Care Act 2022",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£5.055M"},
            {"label": "Trust scale", "value": "Two-hub acute (Ipswich + Colchester); c. 11,000 WTE; c. 1.0M catchment"},
            {"label": "Inter-site corridor", "value": "Ipswich to Colchester c. 30 miles via A12 / A14 — sustains routine clinical + corporate inter-site travel"},
            {"label": "2018 merger context", "value": "Trust formed July 2018 via Ipswich + Colchester merger — dual-hub model drives transport baseline above single-site DGH peers"},
            {"label": "Rural catchment driver", "value": "Rural east Suffolk + north Essex (Tendring, mid-Suffolk) drives PTS demand at distance from acute hubs"},
            {"label": "PTS provider", "value": "PTS contracted via NHSE Suffolk & North East Essex ICS framework + commercial cohort"},
            {"label": "IFRS 16 effect", "value": "Pool fleet + lease vehicles brought on-balance-sheet from 2022-23 transition — inflates line vs pre-IFRS 16 baseline"},
            {"label": "Industrial action 2023-24 effect", "value": "Strike-related inter-site cover travel + locum mileage claims layered on pandemic-recovery activity"},
            {"label": "Funding trajectory", "value": "Pre-IFRS 16 c. £3.5M → IFRS 16 transition 2022-23 step-up → 2024-25 £5.055M — fuel CPI + activity recovery"},
            {"label": "Delivery body", "value": "Trust Estates + Travel team + contracted PTS + East of England Ambulance Service for emergency transfers"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Suffolk and North East Essex ICB + NHSE PTS policy"},
            {"label": "Predecessor / successor", "value": "Predecessor: separate Ipswich + Colchester transport baselines pre-July 2018 · Successor: SNEE ICS pooled-fleet + EV transition"}
        ],
        "notes": "ESNEFT's transport line reflects the operational legacy of the July 2018 Ipswich + Colchester merger — running a dual-hub acute model across c. 30 miles of A12 / A14 corridor sustains routine clinical and corporate inter-site travel above what single-site peer DGHs require. The rural east Suffolk and north Essex catchment (Tendring, mid-Suffolk) drives sustained PTS demand at distance from the two acute hubs. The April 2022 IFRS 16 transition stepped pool fleet and lease vehicles onto the balance sheet, lifting the transport line's headline figure. Industrial action 2023-24 layered inter-site cover travel and locum mileage on pandemic-recovery activity; SNEE ICS pooled-fleet and EV transition are the medium-term levers.",
        "sources": [
            {"publisher": "East Suffolk and North Essex NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.esneft.nhs.uk/about-us/publications/annual-report-and-accounts/"},
            {"publisher": "NHS England", "title": "Non-Emergency Patient Transport Services Review", "url": "https://www.england.nhs.uk/publication/non-emergency-patient-transport-services-review/"},
            {"publisher": "NHS Employers", "title": "Agenda for Change Section 17 — Mileage allowances", "url": "https://www.nhsemployers.org/publications/tchandbook"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 7 — Leases)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "ESNEFT provider profile (RDE)", "url": "https://www.cqc.org.uk/provider/RDE"}
        ],
        "related": ["East Suffolk and North Essex NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Transport (business + patient) — Imperial College Healthcare NHS Trust", "Transport (business + patient) — Barts Health NHS Trust", "General supplies & services — East Suffolk and North Essex NHS Foundation Trust"]
    },
    "Establishment costs — Lancashire Teaching Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "Lancashire Teaching Hospitals NHS Foundation Trust"}],
        "description": "LTHTR's £5.03M establishment costs line covers postage, telephony, printing, stationery, recruitment-advertising, training, conferences, subscriptions and legal & professional fees across the Royal Preston + Chorley & South Ribble two-site footprint. The trust hosts the Lancashire & South Cumbria Major Trauma Centre at Royal Preston plus tertiary specialist neurosciences, plastics + burns, renal and cancer services for the wider region — the specialist-recruitment overhead and ongoing Chorley A&E redesign / NHP cohort engagement layer professional-fee spend above peer DGHs.",
        "beneficiaries": "c. 8,500 WTE staff serving a c. 390,000 Preston + South Ribble + Chorley core catchment plus c. 1.5M Lancashire & South Cumbria tertiary catchment; c. 170,000 ED attendances/yr (Royal Preston + Chorley); c. 90,000 elective + day-case admissions/yr; Royal Preston = Lancs & South Cumbria MTC.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25 · Public Contracts Regulations 2015 / Procurement Act 2023",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£5.03M"},
            {"label": "Trust scale", "value": "Two-site (Royal Preston + Chorley & South Ribble); c. 8,500 WTE"},
            {"label": "Composition", "value": "Postage + telephony + print + recruitment-advertising + training + conferences + subscriptions + legal & professional fees"},
            {"label": "MTC + tertiary recruitment driver", "value": "Royal Preston = Lancs & South Cumbria MTC + tertiary neurosciences, plastics + burns, renal — drives specialist-recruitment spend"},
            {"label": "Chorley A&E history", "value": "Chorley A&E reconfiguration 2016 (downgrade) + recurrent reopening debate — drives community-engagement comms + professional fees"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove rota-restructuring + agency-recruitment spend"},
            {"label": "April 2025 NIC + CPI uplift", "value": "Apr 2025 employer-NIC step-up raises forward professional-fee + recruitment-retainer cost; CPI on print/post inputs"},
            {"label": "Funding trajectory", "value": "2021-22 c. £3.8M → 2023-24 £4.6M → 2024-25 £5.03M — sustained CPI + EPR + tertiary recruitment churn"},
            {"label": "Delivery body", "value": "Trust Corporate Services + HR + Finance + IT + Communications + EPR programme office + external counsel"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Lancashire and South Cumbria ICB + NHSE Major Trauma policy"},
            {"label": "Evaluation evidence", "value": "Model Hospital corporate-services benchmarks; NHSE Major Trauma annual review; Trust ARA disclosure; CQC inspection (RXN)"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2002 separate Royal Preston + Chorley baselines · Successor: L&SC ICB shared services + Frontline Digitisation convergence"}
        ],
        "notes": "LTHTR's establishment line is shaped by the trust's role as the Lancashire & South Cumbria Major Trauma Centre at Royal Preston plus its tertiary specialist mix (neurosciences, plastics + burns, renal, cancer), which sustains specialist-recruitment and advertising spend above peer DGHs. The Chorley A&E reconfiguration history — 2016 downgrade plus recurrent reopening debate — drives sustained community-engagement comms spend. Frontline Digitisation EPR work and 2023-24 industrial action layered training, change-management and rota-restructuring professional-fee uplift through the year. April 2025 NIC step-up and CPI feed forward unit-cost pressure; L&SC ICB shared-corporate-services pooling is the medium-term lever.",
        "sources": [
            {"publisher": "Lancashire Teaching Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.lancsteachinghospitals.nhs.uk/about-us/our-publications"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/connecting-health-and-care-providers/frontline-digitisation/"},
            {"publisher": "NHS England", "title": "Major Trauma Centres + 2024-25 Operational Planning Guidance", "url": "https://www.england.nhs.uk/publication/2024-25-priorities-and-operational-planning-guidance/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "LTHTR provider profile (RXN)", "url": "https://www.cqc.org.uk/provider/RXN"}
        ],
        "related": ["Lancashire Teaching Hospitals NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Establishment costs — Bedfordshire Hospitals NHS Foundation Trust", "Establishment costs — North Bristol NHS Trust", "Frontline Digitisation Programme"]
    },
    "Transport (business + patient) — The Newcastle Upon Tyne Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "The Newcastle Upon Tyne Hospitals NHS Foundation Trust"}],
        "description": "NUTH's £5.024M transport line covers staff business mileage (AfC Section 17 + HMRC AMAP), pool fleet under IFRS 16, contracted patient transport services and inter-site transfers between the Royal Victoria Infirmary, Freeman Hospital, Centre for Life and Newcastle Dental Hospital. NUTH is one of England's leading academic acute trusts and the regional tertiary centre for the North East and North Cumbria — Freeman's national cardiothoracic transplant + cancer centre and the RVI's Major Trauma Centre status drive substantial inter-site clinical, specimen and clinician transfer activity.",
        "beneficiaries": "c. 16,000 WTE staff serving a c. 800,000 Newcastle, North Tyneside core catchment plus c. 3.0M North East and North Cumbria tertiary catchment plus national Freeman transplant referrals; c. 230,000 ED attendances/yr at RVI ED (Major Trauma Centre); c. 200,000 elective + day-case admissions/yr.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 + IFRS 16 Leases (pool fleet) · NHS Act 2006 · NHSE Patient Transport Services Eligibility Criteria · AfC Section 17 + HMRC Approved Mileage Allowance Payments · Health and Care Act 2022",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£5.024M"},
            {"label": "Trust scale", "value": "Multi-site academic acute (RVI + Freeman + Centre for Life + Dental Hospital); c. 16,000 WTE"},
            {"label": "Major Trauma Centre", "value": "RVI = North East + North Cumbria MTC — drives inter-site major-trauma transfer demand + helicopter handover"},
            {"label": "Freeman national specialist", "value": "Freeman cardiothoracic transplant (heart + lung) + cancer + paediatric — national/international tertiary referrals; inter-site patient + organ-retrieval transport"},
            {"label": "PTS provider", "value": "PTS contracted via NEAS / North East Ambulance Service + commercial cohort under NHSE eligibility"},
            {"label": "IFRS 16 effect", "value": "Pool fleet + lease vehicles brought on-balance-sheet from 2022-23 transition — inflates line vs pre-IFRS 16 baseline"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove inter-site cover travel + locum mileage claims"},
            {"label": "Funding trajectory", "value": "Pre-IFRS 16 c. £3.5M → IFRS 16 transition 2022-23 step-up → 2024-25 £5.024M — fuel CPI + activity recovery"},
            {"label": "Delivery body", "value": "Trust Estates + Travel + NEAS PTS + commercial NEPTS + organ retrieval logistics for Freeman transplant"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + North East and North Cumbria ICB + NHSE PTS policy + NHSBT for organ retrieval"},
            {"label": "Evaluation evidence", "value": "NHSE PTS Review 2021-22; CQC inspection (RTD); NHSE Major Trauma annual review; Trust ARA 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2006 separate Newcastle General + RVI baselines · Successor: NENC ICS pooled-fleet + EV transition"}
        ],
        "notes": "NUTH's transport line is shaped by its position as the leading academic acute trust for the North East and North Cumbria — the RVI's Major Trauma Centre status combined with Freeman's national cardiothoracic transplant, cancer and paediatric centre roles drive substantial inter-site patient, specimen, organ-retrieval and clinician transfer above peers. The April 2022 IFRS 16 transition stepped pool fleet onto balance sheet, lifting the headline figure. Industrial action 2023-24 layered inter-site cover travel and locum mileage on post-pandemic recovery and fuel CPI. NEAS-contracted PTS plus commercial NEPTS under NHSE eligibility serve rural North Cumbria; NENC ICS pooled-fleet + EV transition are the medium-term levers.",
        "sources": [
            {"publisher": "The Newcastle Upon Tyne Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.newcastle-hospitals.nhs.uk/about-us/our-publications/"},
            {"publisher": "NHS England", "title": "Non-Emergency Patient Transport Services Review", "url": "https://www.england.nhs.uk/publication/non-emergency-patient-transport-services-review/"},
            {"publisher": "NHS Employers", "title": "Agenda for Change Section 17 — Mileage allowances", "url": "https://www.nhsemployers.org/publications/tchandbook"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 7 — Leases)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "NUTH provider profile (RTD)", "url": "https://www.cqc.org.uk/provider/RTD"}
        ],
        "related": ["The Newcastle Upon Tyne Hospitals NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Transport (business + patient) — Imperial College Healthcare NHS Trust", "Transport (business + patient) — Barts Health NHS Trust", "NHS Blood and Transplant"]
    },
    "Transport (business + patient) — South Tees Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "South Tees Hospitals NHS Foundation Trust"}],
        "description": "South Tees' £5.015M transport line covers staff business mileage (AfC Section 17 + HMRC AMAP), pool fleet under IFRS 16, contracted patient transport services and inter-site transfers between James Cook University Hospital (Middlesbrough) and the Friarage Hospital (Northallerton). James Cook hosts the North East Major Trauma Centre plus tertiary cardiothoracic, neurosciences and spinal-injuries services; the Friarage 2019 A&E + obstetric anaesthesia downgrade reshaped Northallerton-to-Middlesbrough patient transfer activity across the c. 30-mile A19 / A684 corridor.",
        "beneficiaries": "c. 9,500 WTE staff serving a c. 1.5M North Yorkshire + Tees Valley tertiary catchment; c. 145,000 ED attendances/yr (James Cook ED + Friarage Urgent Treatment); c. 100,000 elective + day-case admissions/yr; James Cook = NE MTC + tertiary cardiothoracic + neuro + spinal-injuries.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 + IFRS 16 Leases (pool fleet) · NHS Act 2006 · NHSE Patient Transport Services Eligibility Criteria · AfC Section 17 + HMRC Approved Mileage Allowance Payments · Health and Care Act 2022",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£5.015M"},
            {"label": "Trust scale", "value": "Two-hub acute (James Cook + Friarage); c. 9,500 WTE; c. 1.5M tertiary catchment"},
            {"label": "Major Trauma Centre", "value": "James Cook = North East MTC — drives inter-site major-trauma transfer demand"},
            {"label": "Tertiary specialty driver", "value": "James Cook tertiary cardiothoracic + neurosciences + spinal injuries — substantial inter-trust patient + clinician transfer"},
            {"label": "Friarage reconfiguration", "value": "Friarage A&E + obstetric anaesthesia downgrade 2019 — sustained Northallerton-to-Middlesbrough patient transfer activity"},
            {"label": "PTS provider", "value": "PTS contracted via regional cohort under NHSE eligibility framework"},
            {"label": "IFRS 16 effect", "value": "Pool fleet + lease vehicles brought on-balance-sheet from 2022-23 transition — inflates line vs pre-IFRS 16 baseline"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove inter-site cover travel + locum mileage claims"},
            {"label": "Funding trajectory", "value": "Pre-IFRS 16 c. £3.5M → IFRS 16 transition 2022-23 step-up → 2024-25 £5.015M — fuel CPI + activity recovery"},
            {"label": "Delivery body", "value": "Trust Estates + Travel + NEAS PTS + commercial NEPTS contractors"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + NENC ICB + HNY ICB (Hambleton/Richmondshire) + NHSE PTS policy"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2002 South Tees Acute + Friarage separate baselines · Successor: NENC + HNY ICS pooled-fleet + EV transition"}
        ],
        "notes": "South Tees' transport baseline is shaped by the dual-hub geography between James Cook in Middlesbrough and the Friarage in Northallerton, separated by c. 30 miles of A19 / A684 corridor — sustained by James Cook's North East MTC role plus tertiary cardiothoracic, neurosciences and spinal-injuries services. The Friarage's 2019 A&E and obstetric anaesthesia downgrade increased Northallerton-to-Middlesbrough patient transfers as services were reorganised. The April 2022 IFRS 16 transition stepped pool fleet onto balance sheet; industrial action 2023-24 layered cover travel and locum mileage. The trust spans two ICS footprints (NENC + HNY), adding commissioning complexity; pooled-fleet and EV transition are the medium-term levers.",
        "sources": [
            {"publisher": "South Tees Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.southtees.nhs.uk/about/publications-policies/"},
            {"publisher": "NHS England", "title": "Non-Emergency Patient Transport Services Review", "url": "https://www.england.nhs.uk/publication/non-emergency-patient-transport-services-review/"},
            {"publisher": "NHS Employers", "title": "Agenda for Change Section 17 — Mileage allowances", "url": "https://www.nhsemployers.org/publications/tchandbook"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 7 — Leases)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "South Tees Hospitals NHS FT provider profile (RTR)", "url": "https://www.cqc.org.uk/provider/RTR"}
        ],
        "related": ["South Tees Hospitals NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Transport (business + patient) — The Newcastle Upon Tyne Hospitals NHS Foundation Trust", "Transport (business + patient) — Imperial College Healthcare NHS Trust", "New Hospital Programme"]
    },
    "Business rates — Mersey and West Lancashire Teaching Hospitals NHS Trust": {
        "aliases": [{"name": "Business rates", "parent": "Mersey and West Lancashire Teaching Hospitals NHS Trust"}],
        "description": "MWL's £4.996M business-rates line covers non-domestic rates on the trust's multi-site footprint following the July 2023 merger of St Helens & Knowsley Teaching Hospitals with Southport & Ormskirk — uniting Whiston Hospital (Prescot, BREEAM-Excellent PFI 2010), St Helens Hospital, Southport & Formby District General, Ormskirk District General + community sites across Cheshire & Merseyside ICS. The 2023 Valuation Office Agency revaluation and the Non-Domestic Rating (Multipliers and Private Finance) Act 2024 reshape the trajectory across the merged hereditament base.",
        "beneficiaries": "c. 9,500 WTE staff serving a c. 600,000 St Helens, Knowsley, Sefton and West Lancashire catchment; c. 200,000 ED attendances/yr (Whiston ED + Southport ED combined); c. 90,000 elective + day-case admissions/yr; recurrent CQC 'Outstanding' for legacy St Helens & Knowsley.",
        "legal_basis": "Local Government Finance Act 1988 Schedule 6 (non-domestic rating valuation) · Non-Domestic Rating (Multipliers and Private Finance) Act 2024 · Local Government Finance Act 1992 · DHSC Group Accounting Manual 2024-25 · NHS Act 2006",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£4.996M"},
            {"label": "Trust scale", "value": "Multi-site post-merger acute (Whiston + St Helens + Southport + Ormskirk + community); c. 9,500 WTE"},
            {"label": "July 2023 merger context", "value": "St Helens & Knowsley Teaching Hospitals + Southport & Ormskirk merged 1 July 2023 to form MWL — combined hereditament base"},
            {"label": "Estate covered", "value": "Whiston (PFI 2010 BREEAM-Excellent) + St Helens + Southport & Formby DGH + Ormskirk DGH + community"},
            {"label": "VOA 2023 revaluation", "value": "April 2023 list took effect — hereditaments revalued, transitional relief tapered through 2024-25"},
            {"label": "Multiplier reform 2024", "value": "NDR (Multipliers and Private Finance) Act 2024 introduces higher multiplier band from 2026-27 for properties > £500k rateable value"},
            {"label": "Whiston PFI hereditament", "value": "Whiston is a 2010-opened PFI build; rateable value reflects modern bed capacity + BREEAM Excellent rating"},
            {"label": "Funding trajectory", "value": "Pre-merger combined c. £4.2M → 2023-24 first-year merger c. £4.7M → 2024-25 £4.996M"},
            {"label": "Delivery body", "value": "Trust E&F + St Helens / Knowsley / Sefton / West Lancashire billing authorities + Valuation Office Agency"},
            {"label": "Policy owner", "value": "MHCLG (multiplier policy) + HM Treasury + DHSC + NHSE Provider Finance + Cheshire and Merseyside ICB"},
            {"label": "Evaluation evidence", "value": "VOA 2023 list publication + revaluation impact assessment; NAO/IFS NDR commentary; Trust ARA 2023-24 (first post-merger)"},
            {"label": "Predecessor / successor", "value": "Predecessor: separate StHK + S&O rates baselines pre-July 2023 · Successor: 2026-27 multiplier-reform band split + 2028 revaluation cycle"}
        ],
        "notes": "MWL's business-rates baseline reflects the operational consolidation of the July 2023 merger that united St Helens & Knowsley Teaching Hospitals with Southport & Ormskirk to form the new Cheshire & Merseyside provider. The combined hereditament base spans Whiston's modern 2010 PFI BREEAM-Excellent build plus the older Southport and Ormskirk DGH stock — a heterogeneous rateable-value mix sensitive to the April 2023 VOA revaluation. The NDR (Multipliers and Private Finance) Act 2024 introduces a higher multiplier band from 2026-27 for properties above £500,000 rateable value. NHS bodies remain liable for full business rates without charitable mandatory relief, exposing the trust fully to the multiplier and revaluation cycle through 2028.",
        "sources": [
            {"publisher": "Mersey and West Lancashire Teaching Hospitals NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.merseywestlancs.nhs.uk/about-us/publications/"},
            {"publisher": "Valuation Office Agency", "title": "Business rates revaluation 2023", "url": "https://www.gov.uk/government/collections/non-domestic-rating-2023-revaluation"},
            {"publisher": "UK Parliament", "title": "Non-Domestic Rating (Multipliers and Private Finance) Act 2024", "url": "https://www.legislation.gov.uk/ukpga/2024/39"},
            {"publisher": "Ministry of Housing, Communities and Local Government", "title": "Business rates: NDR multipliers 2024-25", "url": "https://www.gov.uk/government/publications/business-rates-revaluation-2023-information"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"}
        ],
        "related": ["Mersey and West Lancashire Teaching Hospitals NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Business rates — Guy's & St Thomas' NHS Foundation Trust", "Valuation Office Agency", "Department of Health and Social Care"]
    },
    "Business rates — The Newcastle Upon Tyne Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "The Newcastle Upon Tyne Hospitals NHS Foundation Trust"}],
        "description": "NUTH's £4.979M business-rates line covers non-domestic rates payable on the Royal Victoria Infirmary (Newcastle city centre, MTC), Freeman Hospital (Heaton, North East tertiary cardiothoracic + cancer + transplant centre), Centre for Life, Newcastle Dental Hospital and the trust's community + research estate. The 2023 VOA revaluation reset rateable values and the NDR (Multipliers and Private Finance) Act 2024 introduces a higher multiplier band from 2026-27 — Freeman and the RVI fall in the new higher band.",
        "beneficiaries": "c. 16,000 WTE staff serving a c. 800,000 Newcastle, North Tyneside core catchment plus c. 3.0M North East and North Cumbria tertiary catchment plus national Freeman transplant referrals; c. 230,000 ED attendances/yr at RVI ED (Major Trauma Centre); c. 200,000 elective + day-case admissions/yr.",
        "legal_basis": "Local Government Finance Act 1988 Schedule 6 (non-domestic rating valuation) · Non-Domestic Rating (Multipliers and Private Finance) Act 2024 · Local Government Finance Act 1992 · DHSC Group Accounting Manual 2024-25 · NHS Act 2006",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£4.979M"},
            {"label": "Trust scale", "value": "Multi-site academic acute (RVI + Freeman + Centre for Life + Dental); c. 16,000 WTE"},
            {"label": "Estate covered", "value": "RVI (Newcastle city centre, MTC) + Freeman (Heaton, tertiary cardiothoracic + cancer) + Centre for Life + Dental + community + research"},
            {"label": "VOA 2023 revaluation", "value": "April 2023 list took effect — hereditaments revalued, transitional relief tapered through 2024-25"},
            {"label": "Multiplier reform 2024", "value": "NDR (Multipliers and Private Finance) Act 2024 introduces higher multiplier band from 2026-27 for properties > £500k rateable value"},
            {"label": "Freeman + RVI value driver", "value": "Freeman national cardiothoracic transplant + cancer + RVI MTC ED + helipad + critical care drive high rateable values"},
            {"label": "NHS Charitable status", "value": "NHS bodies pay full business rates — no charitable mandatory relief unlike charity-sector peers"},
            {"label": "Funding trajectory", "value": "2021-22 c. £4.3M → 2023-24 £4.7M → 2024-25 £4.979M (VOA 2023 effects + multiplier indexation)"},
            {"label": "Delivery body", "value": "Trust E&F + Newcastle City + North Tyneside billing authorities + Valuation Office Agency"},
            {"label": "Policy owner", "value": "MHCLG (multiplier policy) + HM Treasury + DHSC + NHSE Provider Finance + North East and North Cumbria ICB"},
            {"label": "Evaluation evidence", "value": "VOA 2023 list publication + revaluation impact assessment; NAO/IFS NDR commentary; Trust ARA 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2006 separate Newcastle General + RVI baselines · Successor: 2026-27 multiplier-reform band split + 2028 revaluation cycle"}
        ],
        "notes": "NUTH's business-rates line is shaped by the high rateable values of the Royal Victoria Infirmary city-centre Major Trauma Centre site and the Freeman Hospital national cardiothoracic transplant + cancer centre — both fall well above the £500,000 rateable-value threshold that defines the new higher-multiplier band introduced from 2026-27 by the Non-Domestic Rating (Multipliers and Private Finance) Act 2024. The April 2023 VOA revaluation reset central rateable values and the transitional-relief taper through 2024-25 lifted the year-on-year line. NHS bodies pay full non-domestic rates without charitable mandatory relief, leaving NUTH fully exposed to the multiplier and revaluation cycle through the 2028 next list. NENC ICB has no levers on the multiplier itself.",
        "sources": [
            {"publisher": "The Newcastle Upon Tyne Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.newcastle-hospitals.nhs.uk/about-us/our-publications/"},
            {"publisher": "Valuation Office Agency", "title": "Business rates revaluation 2023", "url": "https://www.gov.uk/government/collections/non-domestic-rating-2023-revaluation"},
            {"publisher": "UK Parliament", "title": "Non-Domestic Rating (Multipliers and Private Finance) Act 2024", "url": "https://www.legislation.gov.uk/ukpga/2024/39"},
            {"publisher": "Ministry of Housing, Communities and Local Government", "title": "Business rates: NDR multipliers 2024-25", "url": "https://www.gov.uk/government/publications/business-rates-revaluation-2023-information"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"}
        ],
        "related": ["The Newcastle Upon Tyne Hospitals NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Business rates — Guy's & St Thomas' NHS Foundation Trust", "Transport (business + patient) — The Newcastle Upon Tyne Hospitals NHS Foundation Trust", "Valuation Office Agency"]
    },
    "Business rates — Maidstone And Tunbridge Wells NHS Trust": {
        "aliases": [{"name": "Business rates", "parent": "Maidstone And Tunbridge Wells NHS Trust"}],
        "description": "MTW's £4.977M business-rates line covers non-domestic rates payable on the two-site footprint of Maidstone Hospital and Tunbridge Wells Hospital at Pembury — the latter a fully-private-room PFI build (signed 2007, opened 2011, SPV Hospital Company (Pembury) Ltd, John Laing concession). The Pembury PFI rateable value reflects modern bed capacity. The April 2023 VOA revaluation reset rateable values and the NDR (Multipliers and Private Finance) Act 2024 introduces a higher multiplier band from 2026-27 — large hereditaments fall in the new band.",
        "beneficiaries": "c. 5,500 WTE staff serving a c. 530,000 west Kent + East Sussex border catchment (Maidstone, Tonbridge, Tunbridge Wells, Sevenoaks); c. 130,000 ED attendances/yr (Maidstone + Tunbridge Wells EDs); c. 65,000 admissions/yr; tertiary cancer centre at Maidstone for Kent.",
        "legal_basis": "Local Government Finance Act 1988 Schedule 6 (non-domestic rating valuation) · Non-Domestic Rating (Multipliers and Private Finance) Act 2024 · Local Government Finance Act 1992 · DHSC Group Accounting Manual 2024-25 · NHS Act 2006",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£4.977M"},
            {"label": "Trust scale", "value": "Two-site (Maidstone + Tunbridge Wells at Pembury); c. 5,500 WTE"},
            {"label": "Estate covered", "value": "Maidstone Hospital + Tunbridge Wells Hospital at Pembury (2011 PFI build, fully single-room) + community-clinic estate"},
            {"label": "Pembury PFI hereditament", "value": "Pembury PFI signed 2007, opened Sep 2011 (SPV Hospital Company (Pembury) Ltd; John Laing) — modern bed capacity drives rateable value"},
            {"label": "Maidstone Cancer Centre", "value": "Kent Oncology Centre at Maidstone — high rateable value reflects oncology + radiotherapy + capital equipment"},
            {"label": "VOA 2023 revaluation", "value": "April 2023 list took effect — hereditaments revalued, transitional relief tapered through 2024-25"},
            {"label": "Multiplier reform 2024", "value": "NDR (Multipliers and Private Finance) Act 2024 introduces higher multiplier band from 2026-27 for properties > £500k rateable value"},
            {"label": "Funding trajectory", "value": "2021-22 c. £4.2M → 2023-24 £4.7M → 2024-25 £4.977M (VOA 2023 effects + multiplier indexation)"},
            {"label": "Delivery body", "value": "Trust E&F + Maidstone Borough + Tunbridge Wells Borough billing authorities + Valuation Office Agency"},
            {"label": "Policy owner", "value": "MHCLG (multiplier policy) + HM Treasury + DHSC + NHSE Provider Finance + Kent and Medway ICB"},
            {"label": "Evaluation evidence", "value": "VOA 2023 list publication + revaluation impact assessment; NAO/IFS NDR commentary; Trust ARA 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2011 Kent & Sussex Hospital (Tunbridge Wells) hereditament · Successor: 2026-27 multiplier-reform band split + 2028 revaluation cycle"}
        ],
        "notes": "MTW's business-rates line is driven by the modern Pembury PFI hereditament (2011 fully-single-room build) at Tunbridge Wells alongside Maidstone Hospital's Kent Oncology Centre — both with rateable values well above the £500,000 threshold that defines the new higher-multiplier band introduced from 2026-27. The April 2023 VOA revaluation reset central rateable values and the transitional-relief taper through 2024-25 lifted the year-on-year line. The Pembury PFI itself runs to c. 2041 with John Laing as the concession holder; the rates line is independent of unitary-charge accounting but sits on the same modern hereditament. NHS bodies pay full non-domestic rates without charitable mandatory relief; Kent and Medway ICB has no levers on the multiplier itself.",
        "sources": [
            {"publisher": "Maidstone and Tunbridge Wells NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.mtw.nhs.uk/about-us/publications/annual-reports/"},
            {"publisher": "Valuation Office Agency", "title": "Business rates revaluation 2023", "url": "https://www.gov.uk/government/collections/non-domestic-rating-2023-revaluation"},
            {"publisher": "UK Parliament", "title": "Non-Domestic Rating (Multipliers and Private Finance) Act 2024", "url": "https://www.legislation.gov.uk/ukpga/2024/39"},
            {"publisher": "Ministry of Housing, Communities and Local Government", "title": "Business rates: NDR multipliers 2024-25", "url": "https://www.gov.uk/government/publications/business-rates-revaluation-2023-information"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"}
        ],
        "related": ["Maidstone And Tunbridge Wells NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Business rates — Guy's & St Thomas' NHS Foundation Trust", "Business rates — The Newcastle Upon Tyne Hospitals NHS Foundation Trust", "Valuation Office Agency"]
    },
    "Business rates — Nottingham University Hospitals NHS Trust": {
        "aliases": [{"name": "Business rates", "parent": "Nottingham University Hospitals NHS Trust"}],
        "description": "NUH's £4.967M business-rates line covers non-domestic rates payable on the Queen's Medical Centre (QMC, Nottingham West — East Midlands MTC + paediatric centre, one of the largest hospitals in Europe by floor area), Nottingham City Hospital (cardiology + oncology + respiratory tertiary), Ropewalk House and the trust's research + community estate. The April 2023 VOA revaluation reset rateable values and the NDR (Multipliers and Private Finance) Act 2024 introduces a higher multiplier band from 2026-27 — QMC and City fall in the new band.",
        "beneficiaries": "c. 17,000 WTE staff serving a c. 2.5M East Midlands tertiary catchment; c. 220,000 ED attendances/yr (QMC ED — Major Trauma Centre); c. 130,000 elective + day-case admissions/yr; QMC = East Midlands MTC + national paediatric centre.",
        "legal_basis": "Local Government Finance Act 1988 Schedule 6 (non-domestic rating valuation) · Non-Domestic Rating (Multipliers and Private Finance) Act 2024 · Local Government Finance Act 1992 · DHSC Group Accounting Manual 2024-25 · NHS Act 2006",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£4.967M"},
            {"label": "Trust scale", "value": "Multi-site academic acute (QMC + City Hospital + Ropewalk House); c. 17,000 WTE"},
            {"label": "Estate covered", "value": "QMC (Nottingham West, East Midlands MTC, c. 100,000 m² — one of Europe's largest hospitals) + City Hospital + Ropewalk House + research + community"},
            {"label": "City tertiary specialty", "value": "Tertiary cardiology, oncology, respiratory and stem-cell transplant — drives equipment + capacity hereditament value"},
            {"label": "VOA 2023 revaluation", "value": "April 2023 list took effect — hereditaments revalued, transitional relief tapered through 2024-25"},
            {"label": "Multiplier reform 2024", "value": "NDR (Multipliers and Private Finance) Act 2024 introduces higher multiplier band from 2026-27 for properties > £500k rateable value"},
            {"label": "NHP cohort context", "value": "NUH Tomorrow scheme (NHP cohort) — QMC + City reconfiguration rephased at Jan 2025 NHP Reset; long-term rates tied to estate plan"},
            {"label": "Funding trajectory", "value": "2021-22 c. £4.3M → 2023-24 £4.7M → 2024-25 £4.967M (VOA 2023 effects + multiplier indexation)"},
            {"label": "Delivery body", "value": "Trust E&F + Nottingham City Council billing authority + Valuation Office Agency"},
            {"label": "Policy owner", "value": "MHCLG (multiplier policy) + HM Treasury + DHSC + NHSE Provider Finance + Nottingham and Nottinghamshire ICB"},
            {"label": "Evaluation evidence", "value": "VOA 2023 list publication + revaluation impact assessment; NAO/IFS NDR commentary; Trust ARA 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2006 separate QMC + City + Hucknall hereditaments · Successor: 2026-27 multiplier-reform band split + NHP-Reset estate transformation"}
        ],
        "notes": "NUH's business-rates line reflects the scale of QMC (one of the largest hospitals in Europe by floor area) plus Nottingham City Hospital's tertiary cardiology, oncology, respiratory and stem-cell transplant facilities — both well above the £500,000 rateable-value threshold that defines the new higher-multiplier band introduced from 2026-27. The April 2023 VOA revaluation reset central rateable values and the transitional-relief taper through 2024-25 lifted the year-on-year line. The 'NUH Tomorrow' New Hospital Programme cohort scheme (rephased at the January 2025 NHP Reset) ties the long-run rates trajectory to the QMC + City estate transformation plan; meanwhile NHS bodies remain liable for full non-domestic rates without charitable mandatory relief.",
        "sources": [
            {"publisher": "Nottingham University Hospitals NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.nuh.nhs.uk/annual-reports"},
            {"publisher": "Valuation Office Agency", "title": "Business rates revaluation 2023", "url": "https://www.gov.uk/government/collections/non-domestic-rating-2023-revaluation"},
            {"publisher": "UK Parliament", "title": "Non-Domestic Rating (Multipliers and Private Finance) Act 2024", "url": "https://www.legislation.gov.uk/ukpga/2024/39"},
            {"publisher": "Ministry of Housing, Communities and Local Government", "title": "Business rates: NDR multipliers 2024-25", "url": "https://www.gov.uk/government/publications/business-rates-revaluation-2023-information"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"}
        ],
        "related": ["Nottingham University Hospitals NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Business rates — Guy's & St Thomas' NHS Foundation Trust", "Transport (business + patient) — Nottingham University Hospitals NHS Trust", "New Hospital Programme"]
    },
    "Termination & post-employment — King’s College Hospital NHS Foundation Trust": {
        "aliases": [{"name": "Termination & post-employment", "parent": "King’s College Hospital NHS Foundation Trust"}],
        "description": "KCH's £4.964M termination & post-employment line covers redundancy, ex-gratia exit, contractual termination, payments in lieu of notice and post-employment benefits under IAS 19 — including the unfunded NHS Compensation for Premature Retirement scheme and other defined-benefit post-employment elements outside NHSPS. The line scales with restructuring activity, particularly the Apollo Epic EPR cross-trust go-live (Oct 2023, joint with GSTT) and recovery from the trust's earlier financial-deficit Recovery Support Programme exit.",
        "beneficiaries": "c. 14,000 WTE staff serving a c. 1.0M south London (Lambeth, Southwark, Lewisham, Bromley) catchment plus tertiary referrals nationally (liver transplant, neuroscience, haemato-oncology, foetal medicine); c. 250,000 ED attendances/yr (Denmark Hill ED — Major Trauma Centre); c. 200,000 admissions/yr.",
        "legal_basis": "IAS 19 Employee Benefits · NHS Pension Scheme Regulations 2015 (and 1995/2008 sections) · Public Sector Exit Payments Regulations 2020 (revoked Feb 2021 — guidance reinstated) · Social Security Contributions and Benefits Act 1992 · DHSC Group Accounting Manual 2024-25 · NHS Act 2006 · Employment Rights Act 1996",
        "key_stats": [
            {"label": "Termination & post-employment 2024-25", "value": "£4.964M"},
            {"label": "Trust scale", "value": "Multi-site academic acute (Denmark Hill + Princess Royal University Hospital + Orpington); c. 14,000 WTE"},
            {"label": "Composition", "value": "Redundancy + PILON + ex-gratia exit + IAS 19 post-employment (CPR + injury benefit + unfunded elements)"},
            {"label": "Apollo EPR go-live", "value": "Joint Apollo Epic with GSTT; KCH Oct 2023 go-live drove operating-model change + supportive exit packages on legacy roles"},
            {"label": "Recovery Support Programme history", "value": "KCH in NHSE Recovery Support Programme (formerly NOF4) — Tier 1 financial-deficit oversight 2017-2022; restructuring + senior turnover legacy"},
            {"label": "MTC + tertiary specialty", "value": "Denmark Hill = south London MTC + national liver transplant + neuroscience + haemato-oncology — drives senior medical churn"},
            {"label": "Exit payment cap context", "value": "Public Sector Exit Payments Regs 2020 (£95k cap) revoked Feb 2021; senior-manager exits subject to MAPLE / NHSE approval"},
            {"label": "NHSPS membership", "value": "Substantively all staff in NHSPS 1995/2008/2015 sections; CPR scheme sits outside main pension scheme as unfunded employer obligation"},
            {"label": "Funding trajectory", "value": "2021-22 c. £3M → 2023-24 £4.5M (Apollo go-live) → 2024-25 £4.964M — Apollo + RSP recovery + general churn"},
            {"label": "Delivery body", "value": "Trust HR + NHSBSA Pensions + Government Actuary's Department (CPR actuarial valuation) + DHSC"},
            {"label": "Policy owner", "value": "DHSC + HM Treasury + Cabinet Office (exit-pay policy) + NHSE Workforce + South East London ICB"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2014 stand-alone King's pre-PRUH integration + pre-RSP baseline · Successor: post-Apollo + post-RSP operating-model + SEL ICS workforce planning"}
        ],
        "notes": "KCH's termination & post-employment line reflects two structural drivers — the Apollo Epic EPR cross-trust go-live in October 2023 (joint with GSTT) reshaped operating models and triggered supportive exit packages on legacy roles, and the legacy of the NHSE Recovery Support Programme (formerly NOF4) under which the trust sat 2017-2022 with Tier 1 financial-deficit oversight and senior turnover. The IAS 19 post-employment element captures the unfunded NHS Compensation for Premature Retirement actuarial cost plus injury-benefit and similar unfunded employer obligations. The Public Sector Exit Payments Regs 2020 (£95k cap) were revoked Feb 2021; senior exits route via MAPLE / NHSE approval. Denmark Hill's MTC + national liver transplant role drives ongoing senior-medical churn.",
        "sources": [
            {"publisher": "King's College Hospital NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.kch.nhs.uk/about/our-publications/"},
            {"publisher": "NHS Business Services Authority", "title": "NHS Pensions Annual Report and Accounts 2023-24", "url": "https://www.nhsbsa.nhs.uk/employers/nhs-pensions-employers"},
            {"publisher": "HM Treasury / Cabinet Office", "title": "Public Sector Exit Payments — guidance and senior approval thresholds", "url": "https://www.gov.uk/government/publications/restriction-of-public-sector-exit-payments-directions-2022"},
            {"publisher": "NHS England", "title": "Recovery Support Programme — provider list and oversight framework", "url": "https://www.england.nhs.uk/system-and-organisational-oversight/recovery-support-programme/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "KCH provider profile (RJZ)", "url": "https://www.cqc.org.uk/provider/RJZ"}
        ],
        "related": ["King’s College Hospital NHS Foundation Trust", "Staff Costs", "NHS Acute Trusts", "Termination & post-employment — Guy's & St Thomas' NHS Foundation Trust", "NHS Pension Scheme", "NHS Business Services Authority"]
    },
    "Establishment costs — North Tees and Hartlepool NHS Foundation Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "North Tees and Hartlepool NHS Foundation Trust"}],
        "description": "NTH's £4.937M establishment line covers postage, telephony, print, recruitment-advertising, training, conferences, subscriptions and legal & professional fees across the University Hospital of North Tees (Stockton) + University Hospital of Hartlepool + integrated community-services footprint. The trust is a long-standing NHP cohort site (Wave 1), with Jan 2025 NHP Reset rephasing affecting pre-construction advisor fees, while the dual-hub geography sustains corporate-overhead spend above single-site DGHs.",
        "beneficiaries": "c. 5,500 WTE staff serving a c. 400,000 Stockton-on-Tees, Hartlepool, East Cleveland catchment; c. 110,000 ED attendances/yr (North Tees ED + Hartlepool Urgent Care); c. 50,000 admissions/yr; integrated community workforce across Stockton + Hartlepool + East Cleveland.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25 · Public Contracts Regulations 2015 / Procurement Act 2023",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£4.937M"},
            {"label": "Trust scale", "value": "Two-hub (University Hospital of North Tees + Hartlepool) + integrated community; c. 5,500 WTE"},
            {"label": "Composition", "value": "Postage + telephony + print + recruitment-advertising + training + conferences + subscriptions + legal & professional fees"},
            {"label": "NHP cohort context", "value": "NHP Wave 1 cohort — original 'North Tees + Hartlepool' new-build; Jan 2025 NHP Reset rephased completion; ongoing advisor fees flow through establishment"},
            {"label": "Integrated acute + community", "value": "Wider corporate-services overhead than acute-only peers due to integrated community-services scope"},
            {"label": "Industrial action 2023-24", "value": "44 days junior-doctor + 10 days consultant strikes drove rota-restructuring + agency-recruitment professional fees"},
            {"label": "April 2025 NIC + CPI", "value": "Apr 2025 NIC step-up raises forward professional-fee + recruitment-retainer cost; CPI on print/post inputs"},
            {"label": "Funding trajectory", "value": "2021-22 c. £3.8M → 2023-24 £4.5M → 2024-25 £4.937M — sustained CPI + NHP advisor costs + recruitment churn"},
            {"label": "Delivery body", "value": "Trust Corporate Services + HR + Finance + IT + Communications + NHP advisors + EPR programme office"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + North East and North Cumbria ICB + DHSC New Hospital Programme team"},
            {"label": "Evaluation evidence", "value": "Model Hospital benchmarks; NAO New Hospital Programme review 2023; Trust ARA disclosure; CQC inspection (RVW)"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2011 separate North Tees + Hartlepool baselines · Successor: NHP Reset rephased new-build + post-build single-hub baseline"}
        ],
        "notes": "NTH's establishment baseline is shaped by three drivers — the dual-hub operating model running both University Hospital of North Tees (Stockton) and University Hospital of Hartlepool sustains corporate-services overhead above single-site DGHs; the integrated acute + community model broadens the corporate footprint vs acute-only peers; and the long-running New Hospital Programme cohort engagement (Wave 1 'North Tees + Hartlepool' new-build, rephased at the January 2025 NHP Reset) drives ongoing scheme-development professional fees and advisor costs. Industrial action 2023-24 and Frontline Digitisation EPR work layered training, change-management and agency-recruitment professional fees. April 2025 NIC step-up and CPI feed forward.",
        "sources": [
            {"publisher": "North Tees and Hartlepool NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.nth.nhs.uk/about-us/our-publications/"},
            {"publisher": "National Audit Office", "title": "New Hospital Programme (HC 1662, 2023)", "url": "https://www.nao.org.uk/reports/the-new-hospital-programme/"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/connecting-health-and-care-providers/frontline-digitisation/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "NTH provider profile (RVW)", "url": "https://www.cqc.org.uk/provider/RVW"}
        ],
        "related": ["North Tees and Hartlepool NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Establishment costs — Bedfordshire Hospitals NHS Foundation Trust", "Establishment costs — North Bristol NHS Trust", "New Hospital Programme"]
    },
    "Amortisation — University Hospitals of North Midlands NHS Trust": {
        "aliases": [{"name": "Amortisation", "parent": "University Hospitals of North Midlands NHS Trust"}],
        "description": "UHNM's £4.876M amortisation line covers the systematic write-down of capitalised intangible assets — software licences, EPR (Cerner Millennium / Oracle Health), capitalised configuration costs, radiology PACS and internally-generated clinical applications — across the Royal Stoke + County Hospital (Stafford) two-site footprint. UHNM is the regional tertiary centre for Staffordshire, Shropshire, Cheshire and North Wales; the digital-convergence path drives an intangible-asset baseline flowing through IAS 38 over typical 5-10 year UELs.",
        "beneficiaries": "c. 11,000 WTE staff serving a c. 950,000 Staffordshire + Stoke catchment plus c. 3.0M tertiary catchment for major trauma, neuroscience, cardiothoracic; c. 220,000 ED attendances/yr (Royal Stoke ED — Major Trauma Centre); c. 130,000 elective + day-case admissions/yr.",
        "legal_basis": "IAS 38 Intangible Assets · IFRIC 22 SaaS configuration/customisation costs (March 2021 agenda decision) · DHSC Group Accounting Manual 2024-25 ch.5 · NHS Act 2006 · Health and Care Act 2022 · NHSE Frontline Digitisation programme guidance",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£4.876M"},
            {"label": "Trust scale", "value": "Two-site academic acute (Royal Stoke + County Hospital, Stafford); c. 11,000 WTE; Royal Stoke = West Midlands North MTC"},
            {"label": "Asset base composition", "value": "Cerner / Oracle Health EPR + radiology PACS + capitalised software + internally-generated clinical apps; 5-10yr UEL per IAS 38 / DHSC GAM ch.5"},
            {"label": "EPR programme context", "value": "UHNM Cerner Millennium / Oracle Health adoption — capitalised licence + configuration costs feed IAS 38 cycle"},
            {"label": "IFRIC 22 effect", "value": "March 2021 SaaS configuration/customisation agenda decision reshaped capitalisation boundary; some costs reclassified opex"},
            {"label": "Frontline Digitisation context", "value": "NHSE Frontline Digitisation funds EPR rollouts to 'core' standard by 2026 — UHNM receiving FD investment"},
            {"label": "Royal Stoke PFI context", "value": "Royal Stoke build (opened 2012) under PFI — capitalised intangibles separate from PFI fixed-asset accounting"},
            {"label": "Funding trajectory", "value": "2021-22 c. £3.8M → 2023-24 £4.5M → 2024-25 £4.876M — sustained intangible-asset additions through Frontline Digitisation"},
            {"label": "Delivery body", "value": "Trust IT + Digital programme office + Cerner / Oracle Health + DHSC Frontline Digitisation + Staffordshire & Stoke-on-Trent ICB digital pillar"},
            {"label": "Policy owner", "value": "DHSC + NHSE Frontline Digitisation + NHSE Provider Finance + Staffordshire and Stoke-on-Trent ICB"},
            {"label": "Evaluation evidence", "value": "NHSE Frontline Digitisation programme evaluation; NAO Digital Transformation in the NHS (HC 8, 2020); Trust ARA disclosure; CQC inspection (RJE)"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2014 University Hospital of North Staffordshire + Mid Staffs separate baselines · Successor: convergent Cerner / Oracle Health + AI-decision modules amortising 2024-2030+"}
        ],
        "notes": "UHNM's amortisation reflects the cumulative capitalisation of the trust's Cerner Millennium / Oracle Health EPR platform plus the wider Frontline Digitisation investment programme — software licences, implementation labour and configuration costs flow through IAS 38 over typical 5-10 year UELs. The IFRIC 22 March 2021 agenda decision reshaped the capitalisation boundary, with some configuration cost reclassified to opex. The 2014 absorption of Mid Staffordshire NHS Foundation Trust services into UHNM (post-Francis Inquiry) consolidated the County Hospital intangible baseline. NHSE's 2026 'core' EPR target keeps the sector trajectory upward; Staffordshire & Stoke-on-Trent ICB digital pillar shapes the medium-term path.",
        "sources": [
            {"publisher": "University Hospitals of North Midlands NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.uhnm.nhs.uk/about-us/who-we-are/publications/"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/connecting-health-and-care-providers/frontline-digitisation/"},
            {"publisher": "National Audit Office", "title": "Digital transformation in the NHS (HC 8, 2020)", "url": "https://www.nao.org.uk/reports/the-use-of-digital-technology-in-the-nhs/"},
            {"publisher": "IFRS Foundation / IFRIC", "title": "Configuration or customisation costs in a cloud computing arrangement (IFRIC March 2021 agenda decision)", "url": "https://www.ifrs.org/news-and-events/news/2021/04/ifric-update-march-2021/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 5)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "UHNM provider profile (RJE)", "url": "https://www.cqc.org.uk/provider/RJE"}
        ],
        "related": ["University Hospitals of North Midlands NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Frontline Digitisation Programme", "Amortisation — Guy's & St Thomas' NHS Foundation Trust", "Amortisation — University Hospitals of Leicester NHS Trust"]
    },
    "General supplies & services — Mid Cheshire Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "Mid Cheshire Hospitals NHS Foundation Trust"}],
        "description": "Mid Cheshire's £4.869M general supplies & services line covers non-clinical consumables, linen, catering provisions, hotel-services materials, office supplies, IT consumables and minor expensed equipment across the Leighton Hospital (Crewe) + Victoria Infirmary (Northwich) + Elmhurst Intermediate Care + community-clinic footprint serving mid-Cheshire. The Sep 2023 RAAC HSSIB list included Leighton Hospital — driving additional decant, prop-and-shore-area consumables and operational consequence costs that lift the line above peer DGHs of similar bed count.",
        "beneficiaries": "c. 5,500 WTE staff serving a c. 450,000 mid-Cheshire catchment (Crewe, Nantwich, Northwich, Winsford, Sandbach); c. 110,000 ED attendances/yr at Leighton ED; c. 50,000 admissions/yr; large maternity unit at Leighton.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 2 Inventories · Procurement Act 2023 · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "General supplies & services 2024-25", "value": "£4.869M"},
            {"label": "Trust scale", "value": "Leighton (Crewe) + Victoria Infirmary (Northwich) + Elmhurst Intermediate Care + community; c. 5,500 WTE"},
            {"label": "RAAC Sep 2023 HSSIB context", "value": "Leighton on the 27-trust RAAC HSSIB list — Sep 2023; drives prop-and-shore + decant + temporary-area consumables"},
            {"label": "NHP cohort uplift Aug 2023", "value": "RAAC trusts elevated into accelerated NHP cohort Aug 2023; rephased at Jan 2025 NHP Reset; pre-construction consumables continue"},
            {"label": "Procurement route", "value": "NHS Supply Chain national framework + Cheshire & Merseyside ICS collaborative + trust-direct contracts"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove cancellation re-stocking + agency backfill churn"},
            {"label": "April 2025 NIC + CPI uplift", "value": "Apr 2025 employer-NIC step-up + sustained non-clinical CPI feed forward unit-cost pressure"},
            {"label": "Funding trajectory", "value": "2021-22 c. £3.6M → 2023-24 £4.4M → RAAC + activity uplift → 2024-25 £4.869M"},
            {"label": "Delivery body", "value": "Trust Procurement + NHS Supply Chain (DHSC ALB) + C&M ICS collaborative + RAAC-decant temporary-area facilities"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Cheshire and Merseyside ICB + DHSC NHP team (RAAC cohort)"},
            {"label": "Evaluation evidence", "value": "Model Hospital benchmarks; HSSIB RAAC report 2023; NAO NHP review 2023; Trust ARA disclosure"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-RAAC-cohort non-clinical baseline · Successor: post-NHP-Reset Leighton rebuild + integrated C&M procurement scaling"}
        ],
        "notes": "Mid Cheshire's general supplies & services baseline is materially shaped by the September 2023 RAAC HSSIB inclusion of Leighton Hospital — a 27-trust national list driving decant operations, prop-and-shore working areas, temporary-clinic consumables and other operational-consequence costs that lift the line above peer DGHs of similar bed count. Leighton was elevated into the accelerated NHP cohort in August 2023 and rephased at the January 2025 NHP Reset, with pre-construction consumables continuing. NHS Supply Chain remains dominant; C&M ICS collaborative scaling alongside LUHFT and Countess of Chester is the medium-term lever. Industrial action 2023-24 layered cancellation re-stocking; April 2025 NIC step-up and non-clinical CPI feed forward.",
        "sources": [
            {"publisher": "Mid Cheshire Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.mcht.nhs.uk/about-us/our-publications-and-data/annual-reports/"},
            {"publisher": "Health Services Safety Investigations Body", "title": "RAAC in NHS hospital buildings — investigation report", "url": "https://www.hssib.org.uk/"},
            {"publisher": "National Audit Office", "title": "New Hospital Programme (HC 1662, 2023)", "url": "https://www.nao.org.uk/reports/the-new-hospital-programme/"},
            {"publisher": "NHS Supply Chain", "title": "Annual Report 2023-24", "url": "https://www.supplychain.nhs.uk/about-us/our-publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Mid Cheshire Hospitals provider profile (RBT)", "url": "https://www.cqc.org.uk/provider/RBT"}
        ],
        "related": ["Mid Cheshire Hospitals NHS Foundation Trust", "Clinical Supplies & Drugs", "NHS Acute Trusts", "NHS Supply Chain", "General supplies & services — Liverpool University Hospitals NHS Foundation Trust", "New Hospital Programme"]
    },
    "General supplies & services — Kingston Hospital NHS Foundation Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "Kingston Hospital NHS Foundation Trust"}],
        "description": "Kingston Hospital's £4.847M general supplies & services line covers non-clinical consumables, linen, catering, hotel-services materials, office supplies, IT consumables and minor expensed equipment at the single-site Galsworthy Road DGH serving south-west London. The trust merged 1 Apr 2024 with Hounslow & Richmond Community Healthcare to form Kingston & Richmond NHS FT, reshaping the medium-term procurement vehicle. Kingston serves a very high maternity volume (c. 6,500 deliveries/yr — among London's busiest).",
        "beneficiaries": "c. 4,000 WTE staff serving a c. 350,000 Kingston, Richmond, parts of Merton and Surbiton catchment; c. 110,000 ED attendances/yr at Kingston ED; c. 60,000 admissions/yr; large maternity unit c. 6,500 deliveries/yr — among London's busiest single-site maternity services.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 2 Inventories · Procurement Act 2023 · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "General supplies & services 2024-25", "value": "£4.847M"},
            {"label": "Trust scale", "value": "Single-site DGH (Galsworthy Road, Kingston upon Thames); c. 4,000 WTE"},
            {"label": "Apr 2024 group-model context", "value": "Kingston Hospital + HRCH merged 1 Apr 2024 to form Kingston & Richmond NHS FT — combined acute + community procurement footprint"},
            {"label": "Maternity volume driver", "value": "c. 6,500 deliveries/yr — among London's busiest single-site maternity services; drives non-clinical consumables baseline"},
            {"label": "ED throughput", "value": "c. 110,000 attendances/yr"},
            {"label": "Procurement route", "value": "NHS Supply Chain national framework + South West London ICS collaborative + trust-direct contracts"},
            {"label": "Industrial action 2023-24", "value": "44 days junior-doctor + 10 days consultant strikes drove cancellation re-stocking + agency backfill churn"},
            {"label": "April 2025 NIC + CPI uplift", "value": "Apr 2025 employer-NIC step-up + sustained non-clinical CPI feed forward unit-cost pressure"},
            {"label": "Funding trajectory", "value": "2021-22 c. £3.6M → 2023-24 £4.3M → 2024-25 £4.847M (post-merger first year + CPI)"},
            {"label": "Delivery body", "value": "Trust Procurement + NHS Supply Chain (DHSC ALB) + SWL ICS procurement collaborative + (post-merger) integrated procurement"},
            {"label": "Evaluation evidence", "value": "Model Hospital benchmarks; CQC (RAX) — recurrent Outstanding; NHSE SWL ICS group-model business case; Trust ARA"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-Apr 2024 stand-alone Kingston + HRCH community baseline · Successor: integrated Kingston & Richmond NHS FT consolidated procurement"}
        ],
        "notes": "Kingston Hospital's general supplies & services baseline is shaped by two drivers — the very high maternity volume (c. 6,500 deliveries/yr ranks among London's busiest single-site maternity services), which drives non-clinical consumables above peer DGHs; and the April 2024 merger with Hounslow & Richmond Community Healthcare to form Kingston & Richmond NHS FT, adding the integrated community-services consumables footprint to the consolidated procurement baseline. NHS Supply Chain remains dominant; SWL ICS collaborative scaling is the medium-term lever. Industrial action 2023-24 drove cancellation re-stocking and agency-backfill consumables; April 2025 NIC step-up and non-clinical CPI feed forward.",
        "sources": [
            {"publisher": "Kingston and Richmond NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24 (Kingston Hospital NHS FT)", "url": "https://www.kingstonhospital.nhs.uk/about-us/our-publications/annual-report"},
            {"publisher": "NHS England", "title": "South West London ICS group-model transaction (Kingston + HRCH)", "url": "https://www.england.nhs.uk/london/our-work/south-west-london/"},
            {"publisher": "NHS Supply Chain", "title": "Annual Report 2023-24", "url": "https://www.supplychain.nhs.uk/about-us/our-publications/"},
            {"publisher": "Care Quality Commission", "title": "Kingston Hospital provider profile (RAX)", "url": "https://www.cqc.org.uk/provider/RAX"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"}
        ],
        "related": ["Kingston Hospital NHS Foundation Trust", "Clinical Supplies & Drugs", "NHS Acute Trusts", "NHS Supply Chain", "General supplies & services — Liverpool University Hospitals NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Amortisation — University Hospitals Dorset NHS Foundation Trust": {
        "aliases": [{"name": "Amortisation", "parent": "University Hospitals Dorset NHS Foundation Trust"}],
        "description": "UHD's £4.833M amortisation line covers the systematic write-down of capitalised intangible assets — software licences, EPR, capitalised configuration costs, radiology PACS and internally-generated clinical applications — across the post-Oct 2020 merger combine of Royal Bournemouth + Christchurch + Poole Hospital. The trust is mid-way through the Dorset Hospital Reconfiguration (Royal Bournemouth as 'major emergency hospital', Poole as 'major planned hospital'), driving substantial digital-convergence work whose IAS 38 amortisation flows over typical 5-10 year UELs.",
        "beneficiaries": "c. 9,000 WTE staff serving a c. 700,000 Bournemouth, Christchurch, Poole and East Dorset catchment plus tertiary referrals; c. 200,000 ED attendances/yr (Royal Bournemouth + Poole EDs combined); c. 100,000 elective + day-case admissions/yr.",
        "legal_basis": "IAS 38 Intangible Assets · IFRIC 22 SaaS configuration/customisation costs (March 2021 agenda decision) · DHSC Group Accounting Manual 2024-25 ch.5 · NHS Act 2006 · Health and Care Act 2022 · NHSE Frontline Digitisation programme guidance",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£4.833M"},
            {"label": "Trust scale", "value": "Three-site acute (Royal Bournemouth + Christchurch + Poole); c. 9,000 WTE"},
            {"label": "Oct 2020 merger context", "value": "Royal Bournemouth & Christchurch + Poole Hospital merged 1 Oct 2020 to form UHD — single-instance EPR convergence drives intangible additions"},
            {"label": "Asset base composition", "value": "EPR + radiology PACS + capitalised software + internally-generated clinical apps; 5-10yr UEL per IAS 38 / DHSC GAM ch.5"},
            {"label": "Dorset Reconfiguration context", "value": "Royal Bournemouth = major emergency hospital + Poole = major planned hospital — service-line transition drives capitalised configuration"},
            {"label": "IFRIC 22 effect", "value": "March 2021 SaaS configuration/customisation agenda decision reshaped capitalisation boundary; some costs reclassified opex"},
            {"label": "Frontline Digitisation context", "value": "NHSE Frontline Digitisation funds EPR rollouts to 'core' by 2026 — UHD receiving FD investment for single-instance convergence"},
            {"label": "Funding trajectory", "value": "Pre-merger c. £3M → 2021-22 first-year c. £4M → 2023-24 £4.5M → 2024-25 £4.833M — sustained additions through convergence + FD"},
            {"label": "Delivery body", "value": "Trust IT + Digital programme office + EPR vendor + DHSC Frontline Digitisation + NHS Dorset ICB digital pillar"},
            {"label": "Policy owner", "value": "DHSC + NHSE Frontline Digitisation + NHSE Provider Finance + NHS Dorset ICB"},
            {"label": "Evaluation evidence", "value": "NHSE Frontline Digitisation programme evaluation; NAO Digital Transformation in the NHS (HC 8, 2020); Trust ARA disclosure; CQC (R0D)"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-Oct 2020 separate Bournemouth + Poole baselines · Successor: convergent single-instance EPR + AI-decision modules amortising 2024-2030+"}
        ],
        "notes": "UHD's amortisation reflects the cumulative capitalisation work driven by two parallel transformations — the October 2020 merger of Royal Bournemouth & Christchurch with Poole Hospital that required single-instance EPR convergence and shared intangible-asset rationalisation, and the ongoing Dorset Hospital Reconfiguration that designates Royal Bournemouth as the major emergency hospital and Poole as the major planned hospital, generating capitalised configuration on service-line transitions. The IFRIC 22 March 2021 agenda decision reshaped the capitalisation boundary, with some configuration cost reclassified to opex. NHSE's 2026 'core' EPR target keeps the sector trajectory upward; NHS Dorset ICB digital pillar shapes the medium-term path alongside the wider estate-reconfiguration plan.",
        "sources": [
            {"publisher": "University Hospitals Dorset NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.uhd.nhs.uk/about-us/publications/"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/connecting-health-and-care-providers/frontline-digitisation/"},
            {"publisher": "National Audit Office", "title": "Digital transformation in the NHS (HC 8, 2020)", "url": "https://www.nao.org.uk/reports/the-use-of-digital-technology-in-the-nhs/"},
            {"publisher": "IFRS Foundation / IFRIC", "title": "Configuration or customisation costs in a cloud computing arrangement (IFRIC March 2021 agenda decision)", "url": "https://www.ifrs.org/news-and-events/news/2021/04/ifric-update-march-2021/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 5)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "UHD provider profile (R0D)", "url": "https://www.cqc.org.uk/provider/R0D"}
        ],
        "related": ["University Hospitals Dorset NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Frontline Digitisation Programme", "Amortisation — Guy's & St Thomas' NHS Foundation Trust", "Amortisation — University Hospitals of North Midlands NHS Trust"]
    },
    "Establishment costs — Royal Cornwall Hospitals NHS Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "Royal Cornwall Hospitals NHS Trust"}],
        "description": "RCHT's £4.819M establishment line covers postage, telephony, print, recruitment-advertising, training, conferences, subscriptions and legal & professional fees across the Royal Cornwall Hospital (Treliske, Truro) + West Cornwall Hospital (Penzance) + St Michael's Hospital (Hayle) footprint serving Cornwall and the Isles of Scilly. The peripheral geography sustains hard-to-fill consultant + middle-grade recruitment churn, and the trust's NHSE Recovery Support Programme engagement plus EPR work drive corporate-services overhead above peer DGHs.",
        "beneficiaries": "c. 6,000 WTE staff serving a c. 570,000 Cornwall + Isles of Scilly catchment (Truro, Penzance, Hayle, Camborne, Falmouth, Bodmin, Newquay, St Austell); c. 90,000 ED attendances/yr at Royal Cornwall ED; c. 50,000 admissions/yr; only major acute provider in Cornwall.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25 · Public Contracts Regulations 2015 / Procurement Act 2023",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£4.819M"},
            {"label": "Trust scale", "value": "Three-site acute (Royal Cornwall + West Cornwall + St Michael's) + community; c. 6,000 WTE; sole major acute provider in Cornwall"},
            {"label": "Composition", "value": "Postage + telephony + print + recruitment-advertising + training + conferences + subscriptions + legal & professional fees"},
            {"label": "Peripheral geography driver", "value": "Cornwall isolation + Isles of Scilly air-transfer logistics — hard-to-fill recruitment sustains agency-recruitment + advertising fees above urban peers"},
            {"label": "RSP / NOF history", "value": "RCHT in NHSE Recovery Support Programme (formerly NOF4) — sustained restructuring + senior-turnover + advisor-fee spend"},
            {"label": "Industrial action 2023-24", "value": "44 days junior-doctor + 10 days consultant strikes drove rota-restructuring + agency-recruitment professional fees"},
            {"label": "April 2025 NIC + CPI", "value": "Apr 2025 NIC step-up raises forward professional-fee + recruitment-retainer cost; CPI on print/post inputs"},
            {"label": "Funding trajectory", "value": "2021-22 c. £3.6M → 2023-24 £4.4M → 2024-25 £4.819M — sustained CPI + RSP advisor costs + recruitment churn"},
            {"label": "Delivery body", "value": "Trust Corporate Services + HR + Finance + IT + Communications + RSP improvement-director + EPR programme office"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + NHS Cornwall and the Isles of Scilly ICB + NHSE Recovery Support Programme"},
            {"label": "Evaluation evidence", "value": "Model Hospital benchmarks; NHSE Recovery Support Programme reviews for RCHT; Trust ARA disclosure; CQC (REF)"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-RSP corporate baseline · Successor: post-RSP-exit + ICS-shared-services + Frontline Digitisation convergence"}
        ],
        "notes": "RCHT's establishment baseline is shaped by three drivers — Cornwall's peripheral geography (plus Isles of Scilly air-transfer logistics) sustains hard-to-fill consultant and middle-grade recruitment churn and the agency-recruitment + advertising professional fees that flow with it; the trust's NHSE Recovery Support Programme engagement (formerly NOF4) has driven sustained restructuring, senior-turnover and improvement-director advisor-fee spend; and the trust's status as Cornwall's sole major acute provider means corporate-services obligations cannot be shared across providers within the county. Frontline Digitisation EPR work and 2023-24 industrial action layered training, change-management and rota-restructuring fees. April 2025 NIC step-up and CPI feed forward.",
        "sources": [
            {"publisher": "Royal Cornwall Hospitals NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.royalcornwall.nhs.uk/about-us/publications/annual-report-and-accounts/"},
            {"publisher": "NHS England", "title": "Recovery Support Programme — provider list and oversight framework", "url": "https://www.england.nhs.uk/system-and-organisational-oversight/recovery-support-programme/"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/connecting-health-and-care-providers/frontline-digitisation/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "RCHT provider profile (REF)", "url": "https://www.cqc.org.uk/provider/REF"}
        ],
        "related": ["Royal Cornwall Hospitals NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Establishment costs — Bedfordshire Hospitals NHS Foundation Trust", "Establishment costs — Wye Valley NHS Trust", "Frontline Digitisation Programme"]
    },
}
