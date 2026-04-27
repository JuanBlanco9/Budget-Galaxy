# -*- coding: utf-8 -*-
# Phase 2 Acute slice 2 — chunk 24 (17 NHS Acute Trust orphan sub-lines)
# Hand-curated trust-specific PROGRAMME-archetype enrichment entries.
# Structural contract per docs/archetype_briefs.md.

NEW = {
    "Business rates — The Royal Wolverhampton NHS Trust": {
        "aliases": [{"name": "Business rates", "parent": "The Royal Wolverhampton NHS Trust"}],
        "description": "RWT's £2.99M business-rates line covers non-domestic rates on the New Cross Hospital main site (Wolverhampton), Cannock Chase Hospital (post-2018 acquisition from Mid Staffs dissolution), West Park Hospital and a substantial integrated primary-care + community footprint across the Black Country and Staffordshire. The Valuation Office Agency assesses rateable values (2023 list effective Apr 2023) and Wolverhampton City Council and Cannock Chase District Council bill respectively. NHS trusts pay the full multiplier with no charitable 80% relief.",
        "beneficiaries": "c. 9,500 WTE staff serving a c. 470,000 Wolverhampton + Cannock Chase catchment plus integrated primary-care registered c. 65,000 patients (Vertical Integration GP-practice model); c. 165,000 ED attendances/yr at New Cross ED; c. 95,000 admissions/yr; multi-site Black Country footprint plus Cannock Chase DGH.",
        "legal_basis": "Local Government Finance Act 1988 (Schedule 6) — Non-Domestic Rating (Multipliers and Private Finance) Act 2024 — Non-Domestic Rating Act 2023 — DHSC Group Accounting Manual 2024-25 — NHS Act 2006 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£2.99M"},
            {"label": "Trust scale", "value": "New Cross Hospital (c. 700 beds) + Cannock Chase Hospital + West Park Hospital + integrated GP-practice estate; c. 9,500 WTE"},
            {"label": "Cannock Chase acquisition", "value": "Cannock Chase Hospital acquired Nov 2014 from Mid Staffs NHS Foundation Trust dissolution — added Cannock hereditament to RWT rating profile"},
            {"label": "Vertical integration", "value": "RWT operates GP-practice estate under vertical-integration model (one of NHS's largest) — adds primary-care premises to rating footprint"},
            {"label": "Billing authorities", "value": "Wolverhampton City Council (New Cross + West Park) + Cannock Chase District Council (Cannock Chase Hospital)"},
            {"label": "2023 revaluation", "value": "VOA 2023 revaluation (effective 1 Apr 2023) re-set rateable values from 2017 list — transitional uplift on West Midlands hereditaments"},
            {"label": "Multiplier 2024-25", "value": "Standard non-domestic multiplier 54.6p (England, 2024-25); NHS pays full rate (no charitable relief); NDR 2024 Act splits multipliers"},
            {"label": "Funding trajectory", "value": "2021-22 c. £2.6M → 2023-24 c. £2.85M → 2024-25 £2.99M — multiplier + transitional uplift"},
            {"label": "Delivery body", "value": "Trust E&F (rates appeals) + Valuation Office Agency + Wolverhampton City Council + Cannock Chase District Council"},
            {"label": "Policy owner", "value": "MHCLG (NDR policy) + HM Treasury + DHSC + NHSE Provider Finance + Black Country ICB"},
            {"label": "Evaluation evidence", "value": "VOA Rating List 2023; NAO Business Rates Reform; Trust ARA 2023-24; CQC RL4 inspections"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2014 pre-Cannock-acquisition baseline · Successor: 2026 revaluation cycle + NDR 2024 Act multiplier-split implementation"}
        ],
        "notes": "RWT's rates line carries an unusually broad hereditament base relative to its bed count — the trust runs one of the NHS's largest vertical-integration GP-practice models, absorbing primary-care premises into the rating footprint, plus the Cannock Chase Hospital site acquired in November 2014 from the dissolved Mid Staffordshire NHS Foundation Trust. The VOA 2023 revaluation lifted rateable values across the West Midlands estate with transitional relief tapering, while the Non-Domestic Rating (Multipliers and Private Finance) Act 2024's multiplier-split reform reshapes future bills for large hereditaments. Two billing authorities (Wolverhampton City Council and Cannock Chase District Council) collect; NHS pays full 54.6p standard multiplier with no charitable relief.",
        "sources": [
            {"publisher": "The Royal Wolverhampton NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.royalwolverhampton.nhs.uk/about-us/our-publications/annual-reports/"},
            {"publisher": "Valuation Office Agency", "title": "2023 Rating List", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "Ministry of Housing, Communities and Local Government", "title": "Non-Domestic Rating Act 2023 + Multipliers and Private Finance Act 2024", "url": "https://www.gov.uk/government/collections/business-rates"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "The Royal Wolverhampton NHS Trust provider profile (RL4)", "url": "https://www.cqc.org.uk/provider/RL4"}
        ],
        "related": ["The Royal Wolverhampton NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Business rates — St George's University Hospitals NHS Foundation Trust", "Business rates — Hull University Teaching Hospitals NHS Trust", "Valuation Office Agency"]
    },
    "Transport (business + patient) — University Hospital Southampton NHS Foundation Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "University Hospital Southampton NHS Foundation Trust"}],
        "description": "UHS's £2.984M transport line covers business mileage (AfC Section 17 + AMAP), pool-fleet IFRS 16 lease costs, NEPTS contract pass-through and patient travel reimbursements across the Southampton General Hospital + Princess Anne Hospital + Royal South Hants footprint. The trust is a major regional tertiary centre — paediatric cardiac surgery, neurosciences, transplantation and Wessex Cancer Centre — driving substantial inter-hospital and inter-trust patient transfer demand. NEPTS is commissioned through the Hampshire and Isle of Wight ICS lead-commissioner arrangement.",
        "beneficiaries": "c. 12,500 WTE staff serving a c. 1.9M Wessex tertiary catchment (Southampton, South Hampshire, plus regional referrals from Dorset, Wiltshire, IoW, Channel Islands); c. 150,000 ED attendances/yr at Southampton General ED; c. 145,000 admissions/yr; major regional trauma centre, paediatric cardiac surgery centre and Wessex Cancer Centre.",
        "legal_basis": "NHS Act 2006 — NHSE Patient Transport Services Eligibility Criteria 2021 — Agenda for Change Section 17 (business mileage) — HMRC AMAP rates — IFRS 16 Leases (pool fleet) — DHSC Group Accounting Manual 2024-25 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£2.984M"},
            {"label": "Trust scale", "value": "Southampton General Hospital (c. 1,200 beds) + Princess Anne Hospital + Royal South Hants Hospital; c. 12,500 WTE"},
            {"label": "Tertiary specialty", "value": "Major Trauma Centre + paediatric cardiac surgery + neurosciences + transplantation + Wessex Cancer Centre — high inter-hospital transfer demand"},
            {"label": "NEPTS commissioning", "value": "Hampshire and Isle of Wight ICS lead-commissioner NEPTS contract; eligibility per NHSE 2021 criteria"},
            {"label": "Composition", "value": "Business mileage (AfC S17 + AMAP 45p/25p frozen since 2011) + pool-fleet IFRS 16 leases + NEPTS pass-through + patient travel reimbursements"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove cancellation rebooking + agency travel claims"},
            {"label": "April 2025 NIC + fuel CPI", "value": "Indirect via NEPTS contractor pass-through + diesel CPI feed forward unit-cost pressure"},
            {"label": "Funding trajectory", "value": "2021-22 c. £2.4M → 2023-24 c. £2.7M → 2024-25 £2.984M — fuel CPI + NEPTS contract uplift + activity recovery"},
            {"label": "Delivery body", "value": "Trust E&F + outsourced NEPTS provider (HIOW ICS lead-commissioner) + pool-fleet leasing partner + Trust HR (mileage)"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + NHSE Urgent and Emergency Care (NEPTS) + Hampshire and Isle of Wight ICB + DHSC"},
            {"label": "Evaluation evidence", "value": "NAO NEPTS 2019; CQC RHM inspections; NHSE NEPTS Eligibility Review 2021; Trust ARA 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-ICS CCG-commissioned NEPTS contracts · Successor: ICS-collaborative NEPTS retender + tertiary-network transfer protocol refresh"}
        ],
        "notes": "UHS's transport line is shaped by the trust's tertiary regional role across Wessex — paediatric cardiac surgery patients transferred from Bristol/Oxford networks, Wessex Cancer Centre repeat-attender oncology travel, and Major Trauma Centre inter-hospital transfers all generate substantial NEPTS volume on top of routine business mileage. Hampshire and Isle of Wight ICS lead-commissioner NEPTS contract retender is a medium-term lever, with NHSE 2021 eligibility criteria tightening the patient-paid threshold. Industrial action 2023-24 drove cancellation-rebooking journeys and agency travel claims; HMRC AMAP-rate freeze at 45p/mile since 2011 sustains internal-rate dispute pressure. Diesel CPI and April 2025 NIC step-up feed forward via NEPTS contractor pass-through.",
        "sources": [
            {"publisher": "University Hospital Southampton NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.uhs.nhs.uk/about-us/our-publications/"},
            {"publisher": "NHS England", "title": "Non-Emergency Patient Transport Services — National Framework + Eligibility Criteria 2021", "url": "https://www.england.nhs.uk/publication/non-emergency-patient-transport-services-nepts/"},
            {"publisher": "National Audit Office", "title": "NHS England's management of the primary care support services contract with Capita", "url": "https://www.nao.org.uk/reports/nhs-englands-management-of-the-primary-care-support-services-contract-with-capita/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "University Hospital Southampton NHS FT provider profile (RHM)", "url": "https://www.cqc.org.uk/provider/RHM"}
        ],
        "related": ["University Hospital Southampton NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Transport (business + patient) — Gloucestershire Hospitals NHS Foundation Trust", "Transport (business + patient) — Bedfordshire Hospitals NHS Foundation Trust", "NHS England"]
    },
    "Transport (business + patient) — Bedfordshire Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "Bedfordshire Hospitals NHS Foundation Trust"}],
        "description": "Bedfordshire Hospitals' £2.963M transport line covers business mileage, pool-fleet IFRS 16 lease costs, NEPTS contract pass-through and patient travel reimbursements across the Bedford Hospital + Luton & Dunstable Hospital footprint following the April 2020 merger of the two trusts. Inter-site transfers between Bedford and L&D — notably for maternity, paediatric and emergency care — generate distinctive volume. NEPTS is commissioned through the Bedfordshire, Luton and Milton Keynes ICS lead-commissioner.",
        "beneficiaries": "c. 7,500 WTE staff serving a c. 700,000 Bedfordshire and Luton catchment (Bedford, Luton, Dunstable, Mid Bedfordshire); c. 200,000 ED attendances/yr (Bedford ED + L&D ED combined — both very busy); c. 105,000 admissions/yr; integrated post-merger 2020 footprint.",
        "legal_basis": "NHS Act 2006 — NHSE Patient Transport Services Eligibility Criteria 2021 — Agenda for Change Section 17 (business mileage) — HMRC AMAP rates — IFRS 16 Leases (pool fleet) — DHSC Group Accounting Manual 2024-25 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£2.963M"},
            {"label": "Trust scale", "value": "Bedford Hospital + Luton & Dunstable Hospital (post-Apr 2020 merger); c. 7,500 WTE"},
            {"label": "Merger + reconfiguration", "value": "Bedford Hospital NHS Trust + L&D University Hospital NHS FT merged Apr 2020 — drives Bedford ↔ Luton paediatric + maternity + complex emergency transfers"},
            {"label": "NEPTS commissioning", "value": "Bedfordshire, Luton and Milton Keynes ICS lead-commissioner NEPTS contract; eligibility per NHSE 2021 criteria"},
            {"label": "Composition", "value": "Business mileage (AfC S17 + AMAP 45p/25p) + pool-fleet IFRS 16 leases + NEPTS pass-through + patient travel reimbursements"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove cancellation rebooking + agency travel claims"},
            {"label": "April 2025 NIC + fuel CPI", "value": "Indirect via NEPTS contractor pass-through + diesel CPI feed forward unit-cost pressure"},
            {"label": "Funding trajectory", "value": "2021-22 (post-merger) c. £2.4M → 2023-24 c. £2.7M → 2024-25 £2.963M — fuel CPI + NEPTS contract uplift + cross-site transfer growth"},
            {"label": "Delivery body", "value": "Trust E&F + outsourced NEPTS provider (BLMK ICS lead-commissioner) + pool-fleet leasing partner + Trust HR (mileage)"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + NHSE Urgent and Emergency Care (NEPTS) + Bedfordshire, Luton and Milton Keynes ICB + DHSC"},
            {"label": "Evaluation evidence", "value": "NAO NEPTS 2019; CQC RC9 inspections; NHSE NEPTS Eligibility Review 2021; Trust ARA 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2020 separate Bedford + L&D transport baselines · Successor: BLMK ICS-collaborative NEPTS retender + post-merger network rationalisation"}
        ],
        "notes": "Bedfordshire Hospitals' transport line carries the post-merger inter-site transfer demand created by the April 2020 unification of Bedford Hospital and Luton & Dunstable — clinical-network reconfiguration concentrates paediatric, maternity and complex emergency volumes between the two sites, generating distinctive cross-site PTS journeys absent from peer single-site DGHs. NEPTS is commissioned by the BLMK ICS lead-commissioner with eligibility tightened under NHSE's 2021 criteria refresh. Industrial action 2023-24 drove cancellation rebooking and agency travel claims; HMRC AMAP-rate freeze at 45p/mile since 2011 sustains internal-rate dispute pressure. Diesel CPI and April 2025 NIC step-up feed forward via NEPTS contractor pass-through.",
        "sources": [
            {"publisher": "Bedfordshire Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.bedfordshirehospitals.nhs.uk/about-us/publications/"},
            {"publisher": "NHS England", "title": "Non-Emergency Patient Transport Services — National Framework + Eligibility Criteria 2021", "url": "https://www.england.nhs.uk/publication/non-emergency-patient-transport-services-nepts/"},
            {"publisher": "National Audit Office", "title": "NHS England's management of the primary care support services contract with Capita", "url": "https://www.nao.org.uk/reports/nhs-englands-management-of-the-primary-care-support-services-contract-with-capita/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Bedfordshire Hospitals NHS FT provider profile (RC9)", "url": "https://www.cqc.org.uk/provider/RC9"}
        ],
        "related": ["Bedfordshire Hospitals NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Transport (business + patient) — University Hospital Southampton NHS Foundation Trust", "Transport (business + patient) — County Durham and Darlington NHS Foundation Trust", "NHS England"]
    },
    "Transport (business + patient) — The Mid Yorkshire Hospitals NHS Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "The Mid Yorkshire Hospitals NHS Trust"}],
        "description": "Mid Yorkshire's £2.956M transport line covers business mileage, pool-fleet IFRS 16 lease costs, NEPTS contract pass-through and patient travel reimbursements across the Pinderfields Hospital (Wakefield) PFI flagship + Pontefract Hospital + Dewsbury & District Hospital footprint. Inter-site clinical-network reconfiguration between Pinderfields (planned-care concentration), Dewsbury (community/elective) and Pontefract drives substantial cross-site PTS demand. NEPTS is commissioned through the West Yorkshire ICS lead-commissioner.",
        "beneficiaries": "c. 9,000 WTE staff serving a c. 530,000 Wakefield, Kirklees and North Kirklees catchment; c. 200,000 ED attendances/yr (Pinderfields ED + Dewsbury ED + Pontefract Walk-in); c. 95,000 admissions/yr; three-site footprint with PFI flagship at Pinderfields.",
        "legal_basis": "NHS Act 2006 — NHSE Patient Transport Services Eligibility Criteria 2021 — Agenda for Change Section 17 (business mileage) — HMRC AMAP rates — IFRS 16 Leases (pool fleet) — DHSC Group Accounting Manual 2024-25 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£2.956M"},
            {"label": "Trust scale", "value": "Pinderfields Hospital (Wakefield, PFI 2010) + Pontefract Hospital + Dewsbury & District Hospital; c. 9,000 WTE"},
            {"label": "PFI + reconfiguration", "value": "Pinderfields + Pontefract under c. £311M PFI signed 2007 (operational 2010-11); Pinderfields concentrates planned-care + emergency; Dewsbury community/elective; Pontefract elective + walk-in — drives cross-site PTS"},
            {"label": "NEPTS commissioning", "value": "West Yorkshire ICS lead-commissioner NEPTS contract; eligibility per NHSE 2021 criteria"},
            {"label": "Composition", "value": "Business mileage (AfC S17 + AMAP 45p/25p) + pool-fleet IFRS 16 leases + NEPTS pass-through + patient travel reimbursements"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove cancellation rebooking + agency travel claims"},
            {"label": "April 2025 NIC + fuel CPI", "value": "Indirect via NEPTS contractor pass-through + diesel CPI feed forward unit-cost pressure"},
            {"label": "Funding trajectory", "value": "2021-22 c. £2.4M → 2023-24 c. £2.7M → 2024-25 £2.956M — fuel CPI + NEPTS contract uplift + cross-site flows"},
            {"label": "Delivery body", "value": "Trust E&F + outsourced NEPTS provider (West Yorkshire ICS lead-commissioner) + pool-fleet leasing partner + Trust HR (mileage)"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + NHSE Urgent and Emergency Care (NEPTS) + West Yorkshire ICB + DHSC"},
            {"label": "Evaluation evidence", "value": "NAO NEPTS 2019; CQC RXF inspections; NHSE NEPTS Eligibility Review 2021; Trust ARA 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-PFI separate site transport baselines · Successor: West Yorkshire ICS-collaborative NEPTS retender + further reconfiguration"}
        ],
        "notes": "Mid Yorkshire's transport line carries the cross-site PTS volume created by the post-PFI 2010-11 service reconfiguration — Pinderfields (Wakefield PFI flagship) concentrates planned-care and emergency, Dewsbury holds community/elective, and Pontefract sits as elective + walk-in — generating distinctive inter-site patient flows on top of routine business mileage. The c. £311M Pinderfields/Pontefract PFI shapes the trust's site-utilisation strategy and West Yorkshire ICS NEPTS contract structure. Industrial action 2023-24 drove cancellation-rebooking and agency travel claims; HMRC AMAP-rate freeze (45p/mile since 2011) sustains internal-rate dispute pressure. Diesel CPI and April 2025 NIC step-up feed forward via NEPTS pass-through.",
        "sources": [
            {"publisher": "The Mid Yorkshire Hospitals NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.midyorks.nhs.uk/annual-reports"},
            {"publisher": "NHS England", "title": "Non-Emergency Patient Transport Services — National Framework + Eligibility Criteria 2021", "url": "https://www.england.nhs.uk/publication/non-emergency-patient-transport-services-nepts/"},
            {"publisher": "National Audit Office", "title": "PFI and PF2 (HC 718, 2018)", "url": "https://www.nao.org.uk/reports/pfi-and-pf2/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Mid Yorkshire Hospitals NHS Trust provider profile (RXF)", "url": "https://www.cqc.org.uk/provider/RXF"}
        ],
        "related": ["The Mid Yorkshire Hospitals NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Transport (business + patient) — Bedfordshire Hospitals NHS Foundation Trust", "Transport (business + patient) — Gloucestershire Hospitals NHS Foundation Trust", "NHS England"]
    },
    "Transport (business + patient) — Gloucestershire Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "Gloucestershire Hospitals NHS Foundation Trust"}],
        "description": "Gloucestershire Hospitals' £2.947M transport line covers business mileage, pool-fleet IFRS 16 lease costs, NEPTS contract pass-through and patient travel reimbursements across the Gloucestershire Royal Hospital (Gloucester) + Cheltenham General Hospital twin-site footprint plus community sites. Inter-site clinical-network reconfiguration concentrates emergency at Gloucester and elective + tertiary at Cheltenham, creating distinctive cross-site PTS demand. NEPTS is commissioned through the One Gloucestershire ICS lead-commissioner.",
        "beneficiaries": "c. 8,500 WTE staff serving a c. 670,000 Gloucestershire catchment (Gloucester, Cheltenham, Stroud, Cotswolds, Forest of Dean); c. 145,000 ED attendances/yr at Gloucester ED (sole 24/7 ED post 2024 Cheltenham reconfiguration); c. 80,000 admissions/yr; major acute and tertiary cancer services.",
        "legal_basis": "NHS Act 2006 — NHSE Patient Transport Services Eligibility Criteria 2021 — Agenda for Change Section 17 (business mileage) — HMRC AMAP rates — IFRS 16 Leases (pool fleet) — DHSC Group Accounting Manual 2024-25 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£2.947M"},
            {"label": "Trust scale", "value": "Gloucestershire Royal Hospital (Gloucester) + Cheltenham General Hospital + community sites; c. 8,500 WTE"},
            {"label": "Twin-site reconfiguration + cancer", "value": "2024 Cheltenham A&E permanently downgraded to MIIU overnight (Gloucester sole 24/7 ED); Cheltenham hosts regional cancer centre with chemo + radiotherapy PTS volume"},
            {"label": "NEPTS commissioning", "value": "One Gloucestershire ICS lead-commissioner NEPTS contract; eligibility per NHSE 2021 criteria"},
            {"label": "Composition", "value": "Business mileage (AfC S17 + AMAP 45p/25p) + pool-fleet IFRS 16 leases + NEPTS pass-through + patient travel reimbursements"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove cancellation rebooking + agency travel claims"},
            {"label": "April 2025 NIC + fuel CPI", "value": "Indirect via NEPTS contractor pass-through + diesel CPI feed forward unit-cost pressure"},
            {"label": "Funding trajectory", "value": "2021-22 c. £2.4M → 2023-24 c. £2.7M → 2024-25 £2.947M — fuel CPI + NEPTS contract uplift + reconfiguration flows"},
            {"label": "Delivery body", "value": "Trust E&F + outsourced NEPTS provider (One Gloucestershire ICS lead-commissioner) + pool-fleet leasing partner + Trust HR (mileage)"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + NHSE Urgent and Emergency Care (NEPTS) + One Gloucestershire ICB + DHSC"},
            {"label": "Evaluation evidence", "value": "NAO NEPTS 2019; CQC RTE inspections; Cheltenham A&E reconfiguration consultation 2023-24; Trust ARA 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2024 dual-site A&E baseline · Successor: post-Cheltenham downgrade reconfiguration steady-state + ICS NEPTS retender"}
        ],
        "notes": "Gloucestershire's transport line is shaped by the 2024 permanent reconfiguration of Cheltenham General's A&E to a Minor Injury and Illness Unit overnight (Gloucester becoming the sole 24/7 ED for the county) — concentrating emergency PTS at Gloucester and reshaping inter-site flows. Cheltenham retains regional cancer-centre status, sustaining repeat-attender chemo and radiotherapy NEPTS volume across a rural Cotswolds and Forest of Dean catchment. Industrial action 2023-24 drove cancellation rebooking and agency travel claims; HMRC AMAP-rate freeze at 45p/mile since 2011 sustains internal-rate dispute pressure. Diesel CPI and April 2025 NIC step-up feed forward via NEPTS contractor pass-through.",
        "sources": [
            {"publisher": "Gloucestershire Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.gloshospitals.nhs.uk/about-us/annual-reports/"},
            {"publisher": "NHS England", "title": "Non-Emergency Patient Transport Services — National Framework + Eligibility Criteria 2021", "url": "https://www.england.nhs.uk/publication/non-emergency-patient-transport-services-nepts/"},
            {"publisher": "One Gloucestershire ICB", "title": "Cheltenham A&E reconfiguration decision 2024", "url": "https://www.onegloucestershire.net/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Gloucestershire Hospitals NHS FT provider profile (RTE)", "url": "https://www.cqc.org.uk/provider/RTE"}
        ],
        "related": ["Gloucestershire Hospitals NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Transport (business + patient) — The Mid Yorkshire Hospitals NHS Trust", "Transport (business + patient) — Isle of Wight NHS Trust", "NHS England"]
    },
    "Business rates — St George's University Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "St George's University Hospitals NHS Foundation Trust"}],
        "description": "St George's £2.942M business-rates line covers non-domestic rates on the St George's Hospital Tooting main site plus Queen Mary's Hospital (Roehampton) under the GESH (Group Hospitals) arrangement with Epsom and St Helier. The Tooting hereditament — a c. 1,000-bed inner-London tertiary teaching hospital with a Major Trauma Centre — sits on the VOA 2023 list with a high inner-London rateable value, billed by Wandsworth Council. NHS trusts pay the full multiplier (no charitable 80% relief).",
        "beneficiaries": "c. 9,500 WTE staff serving a c. 1.3M South West London catchment plus tertiary referrals from South East England; c. 170,000 ED attendances/yr at St George's ED; c. 100,000 admissions/yr; St George's is one of London's four Major Trauma Centres and a leading academic medical centre with St George's, University of London.",
        "legal_basis": "Local Government Finance Act 1988 (Schedule 6) — Non-Domestic Rating (Multipliers and Private Finance) Act 2024 — Non-Domestic Rating Act 2023 — DHSC Group Accounting Manual 2024-25 — NHS Act 2006 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£2.942M"},
            {"label": "Trust scale", "value": "St George's Hospital Tooting (c. 1,000 beds) + Queen Mary's Hospital Roehampton; c. 9,500 WTE"},
            {"label": "Major Trauma Centre", "value": "St George's = one of London's four MTCs — high acuity tertiary hereditament"},
            {"label": "Group Hospitals (GESH)", "value": "Group arrangement with Epsom and St Helier University Hospitals NHS Trust + St George's, University of London — shared rating profile elements"},
            {"label": "Billing authority", "value": "Wandsworth Council (St George's Tooting + Queen Mary's Roehampton)"},
            {"label": "2023 revaluation", "value": "VOA 2023 revaluation (effective 1 Apr 2023) re-set rateable values from 2017 list — material inner-London uplift on tertiary teaching hospital"},
            {"label": "Multiplier 2024-25 + NDR 2024 Act", "value": "Standard 54.6p (England, 2024-25); NHS pays full rate (no charitable relief); NDR 2024 Act splits multipliers — large hereditaments exposed"},
            {"label": "Funding trajectory", "value": "2021-22 c. £2.6M → 2023-24 c. £2.85M → 2024-25 £2.942M — multiplier + transitional uplift on inner-London hereditament"},
            {"label": "Delivery body", "value": "Trust E&F (rates appeals) + Valuation Office Agency + Wandsworth Council"},
            {"label": "Policy owner", "value": "MHCLG (NDR policy) + HM Treasury + DHSC + NHSE Provider Finance + South West London ICB"},
            {"label": "Evaluation evidence", "value": "VOA Rating List 2023; NAO Business Rates Reform; Trust ARA 2023-24; CQC RJ7 inspections"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2017 rating list baseline · Successor: 2026 revaluation cycle + NDR 2024 Act multiplier-split implementation"}
        ],
        "notes": "St George's rates line carries the high rateable value of an inner-London tertiary teaching hospital and Major Trauma Centre — Wandsworth's VOA 2023 list lifted London hospital hereditaments materially with transitional relief tapering. Queen Mary's Hospital Roehampton adds a smaller hereditament under the same authority. NHS trusts cannot claim charitable 80% relief, so the full 54.6p standard multiplier applies. The NDR 2024 Act's multiplier-split reform exposes large hereditaments to higher-multiplier classification in future bills. The Group Hospitals (GESH) arrangement with Epsom and St Helier reshapes shared corporate-services rating allocation; appeals are managed via the Trust E&F team.",
        "sources": [
            {"publisher": "St George's University Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.stgeorges.nhs.uk/about/publications-and-policies/annual-reports/"},
            {"publisher": "Valuation Office Agency", "title": "2023 Rating List", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "Ministry of Housing, Communities and Local Government", "title": "Non-Domestic Rating Act 2023 + Multipliers and Private Finance Act 2024", "url": "https://www.gov.uk/government/collections/business-rates"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "St George's University Hospitals NHS FT provider profile (RJ7)", "url": "https://www.cqc.org.uk/provider/RJ7"}
        ],
        "related": ["St George's University Hospitals NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Business rates — The Royal Wolverhampton NHS Trust", "Business rates — York and Scarborough Teaching Hospitals NHS Foundation Trust", "Valuation Office Agency"]
    },
    "General supplies & services — The Hillingdon Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "The Hillingdon Hospitals NHS Foundation Trust"}],
        "description": "Hillingdon's £2.904M general supplies & services line covers non-clinical consumables, linen, catering, hotel-services materials, office supplies, IT consumables and minor expensed equipment across the Hillingdon Hospital + Mount Vernon Hospital footprint serving north-west outer London. The trust is delivering a major estate replacement under the New Hospital Programme (Hillingdon redevelopment) — original hospital structurally constrained — with line dynamics shaped by the redevelopment cohort transition and NHP Reset 2025 deferral landscape.",
        "beneficiaries": "c. 3,800 WTE staff serving a c. 305,000 Hillingdon catchment (Uxbridge, Hayes, Ruislip, Northwood plus Heathrow workforce-related demand); c. 110,000 ED attendances/yr at Hillingdon ED; c. 55,000 admissions/yr; covers Hillingdon Hospital + Mount Vernon non-cancer outpatient services.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) — IAS 2 Inventories — Procurement Act 2023 — NHS Act 2006 — Health and Care Act 2022 — NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "General supplies & services 2024-25", "value": "£2.904M"},
            {"label": "Trust scale", "value": "Hillingdon Hospital (Uxbridge) + Mount Vernon Hospital (non-cancer outpatient); c. 3,800 WTE"},
            {"label": "NHP redevelopment + Heathrow", "value": "Hillingdon redevelopment in original NHP cohort (structurally constrained, on Reset 2025 trajectory); Heathrow Airport adjacent — transient + worker population lifts ED demand and consumable use"},
            {"label": "Procurement route", "value": "NHS Supply Chain national framework + trust-direct contracts + North West London ICS procurement collaborative"},
            {"label": "Composition", "value": "Linen, catering provisions, hotel-services materials, office supplies, IT consumables, minor expensed equipment"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove cancellation rebooking + agency-backfill consumable churn"},
            {"label": "April 2025 NIC + CPI uplift", "value": "Indirect via supplier pass-through; non-clinical CPI feed forward unit-cost pressure"},
            {"label": "Funding trajectory", "value": "2021-22 c. £2.4M → 2023-24 c. £2.7M → 2024-25 £2.904M — sustained CPI + activity uplift"},
            {"label": "Delivery body", "value": "Trust Procurement + NHS Supply Chain (DHSC ALB) + NW London ICS procurement collaborative"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + North West London ICB + NHP programme team"},
            {"label": "Evaluation evidence", "value": "Model Hospital benchmarks; NAO New Hospital Programme; NHS Supply Chain ARA; CQC RAS inspections; Trust ARA 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: legacy Hillingdon Hospital ageing-estate baseline · Successor: post-redevelopment new-build consumable-baseline reset (NHP Reset 2025 trajectory)"}
        ],
        "notes": "Hillingdon's general supplies & services baseline reflects an ageing primary estate — Hillingdon Hospital is in the original NHP cohort with replacement scheme deferred under the January 2025 NHP Reset, sustaining the constrained-fabric operating context that affects hotel-services consumable workflow. The trust serves a Heathrow-adjacent catchment whose transient and airport-worker demand lifts ED throughput and consumable use above standard outer-London DGH baselines. NHS Supply Chain remains dominant; NW London ICS procurement collaborative scales medium-term. Industrial action 2023-24 drove cancellation-rebooking and agency-backfill churn; April 2025 NIC step-up + CPI feed forward via supplier pass-through.",
        "sources": [
            {"publisher": "The Hillingdon Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.thh.nhs.uk/about-us/our-publications/"},
            {"publisher": "NHS Supply Chain", "title": "Annual Report 2023-24", "url": "https://www.supplychain.nhs.uk/about-us/our-publications/"},
            {"publisher": "National Audit Office", "title": "Progress with the New Hospital Programme (HC 1062, 2023)", "url": "https://www.nao.org.uk/reports/progress-with-the-new-hospital-programme/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "The Hillingdon Hospitals NHS FT provider profile (RAS)", "url": "https://www.cqc.org.uk/provider/RAS"}
        ],
        "related": ["The Hillingdon Hospitals NHS Foundation Trust", "Clinical Supplies & Drugs", "NHS Acute Trusts", "General supplies & services — Gateshead Health NHS Foundation Trust", "General supplies & services — Great Western Hospitals NHS Foundation Trust", "NHS Supply Chain"]
    },
    "Establishment costs — Countess of Chester Hospital NHS Foundation Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "Countess of Chester Hospital NHS Foundation Trust"}],
        "description": "Countess of Chester's £2.891M establishment costs line covers postage, telephony, mobile-data, printing, stationery, recruitment advertising, subscriptions and minor sundries across the Countess of Chester Hospital (Chester) main site and Ellesmere Port Hospital community footprint. The trust has been operating under intense scrutiny following the Lucy Letby case, the Thirlwall Inquiry (ongoing) and consequent governance, recruitment and communications spend that elevates the establishment-cost base above pre-2018 baseline.",
        "beneficiaries": "c. 3,800 WTE staff serving a c. 445,000 west Cheshire and Deeside catchment (Chester, Ellesmere Port, Neston, plus cross-border Welsh patients); c. 90,000 ED attendances/yr at Countess of Chester ED; c. 55,000 admissions/yr; main Countess of Chester Hospital + Ellesmere Port Hospital community.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) — IAS 1 Presentation of Financial Statements — NHS Act 2006 — Health and Care Act 2022 — NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£2.891M"},
            {"label": "Trust scale", "value": "Countess of Chester Hospital + Ellesmere Port Hospital; c. 3,800 WTE"},
            {"label": "Composition", "value": "Postage, telephony/mobile, printing, stationery, recruitment advertising, subscriptions, hospitality, minor sundries"},
            {"label": "Letby / Thirlwall context", "value": "Lucy Letby convictions 2023; Thirlwall Inquiry (statutory, ongoing, due 2025-26 reporting) — drives governance review costs, legal counsel support, comms spend, recruitment advertising"},
            {"label": "Industrial action 2023-24", "value": "44 days junior-doctor + 10 days consultant strikes drove recruitment-advertising spike + comms costs"},
            {"label": "EPR / Frontline Digitisation", "value": "Cerner Millennium EPR + Frontline Digitisation track drives change-mgmt comms, training-materials printing"},
            {"label": "April 2025 NIC + CPI uplift", "value": "Royal Mail + telecoms CPI feed forward unit-cost pressure"},
            {"label": "Funding trajectory", "value": "2021-22 c. £2.3M → 2023-24 c. £2.7M → 2024-25 £2.891M — Letby-related comms/governance + sustained CPI uplift"},
            {"label": "Delivery body", "value": "Trust Corporate Services + Communications + Procurement + IT + Crown Commercial Service framework (telecoms/postage)"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Cheshire and Merseyside ICB"},
            {"label": "Evaluation evidence", "value": "Thirlwall Inquiry submissions; CQC RJR inspections; Model Hospital benchmark; Trust ARA 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2018 pre-Letby-investigation baseline · Successor: post-Thirlwall recommendations implementation + governance overhead refresh"}
        ],
        "notes": "Countess of Chester's establishment-costs baseline reflects a single major DGH operating under intense governance scrutiny — Lucy Letby's 2023 convictions and the ongoing statutory Thirlwall Inquiry have driven sustained governance-review, legal-counsel-support, communications and recruitment-advertising spend that elevate the line above peer DGH baselines. EPR rollout (Cerner Millennium) under the Frontline Digitisation track adds change-management printing and digital-training materials. Industrial action 2023-24 lifted recruitment-advertising spend through agency-recruitment campaigns. Royal Mail and telecoms CPI feed forward unit-cost pressure into 2025-26 ahead of Thirlwall reporting.",
        "sources": [
            {"publisher": "Countess of Chester Hospital NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.coch.nhs.uk/about-the-trust/annual-reports-and-accounts/"},
            {"publisher": "Thirlwall Inquiry", "title": "Statutory inquiry into the events at the Countess of Chester Hospital", "url": "https://thirlwall.public-inquiry.uk/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Countess of Chester Hospital NHS FT provider profile (RJR)", "url": "https://www.cqc.org.uk/provider/RJR"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme (EPR rollout)", "url": "https://www.england.nhs.uk/digitaltechnology/connecting-health-and-care/frontline-digitisation/"}
        ],
        "related": ["Countess of Chester Hospital NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Establishment costs — Maidstone And Tunbridge Wells NHS Trust", "Thirlwall Inquiry", "Department of Health and Social Care"]
    },
    "Business rates — York and Scarborough Teaching Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "York and Scarborough Teaching Hospitals NHS Foundation Trust"}],
        "description": "York and Scarborough Teaching Hospitals' £2.879M business-rates line covers non-domestic rates on York Hospital, Scarborough Hospital, Bridlington Hospital, Selby Community Hospital, Malton Community Hospital and Whitby Community Hospital — a geographically spread multi-site footprint covering York, North Yorkshire and the East Coast. Multiple billing authorities (City of York Council, North Yorkshire Council, East Riding of Yorkshire Council) collect with VOA assessing rateable values on the 2023 list. NHS pays full multiplier (no charitable relief).",
        "beneficiaries": "c. 9,000 WTE staff serving a c. 800,000 York, North Yorkshire and East Coast catchment; c. 175,000 ED attendances/yr (York ED + Scarborough ED + Bridlington MIU); c. 90,000 admissions/yr; six-site geographically dispersed footprint covering one of England's largest acute-trust catchment areas by area.",
        "legal_basis": "Local Government Finance Act 1988 (Schedule 6) — Non-Domestic Rating (Multipliers and Private Finance) Act 2024 — Non-Domestic Rating Act 2023 — DHSC Group Accounting Manual 2024-25 — NHS Act 2006 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£2.879M"},
            {"label": "Trust scale", "value": "York Hospital + Scarborough Hospital + Bridlington Hospital + Selby + Malton + Whitby community hospitals; c. 9,000 WTE"},
            {"label": "Geographic spread", "value": "Largest English acute-trust catchment by area — six-site footprint across c. 3,400 sq km"},
            {"label": "Billing authorities + North Yorkshire LGR", "value": "City of York Council + North Yorkshire Council (formed Apr 2023 from county/district structure) + East Riding of Yorkshire Council (Bridlington)"},
            {"label": "2023 revaluation", "value": "VOA 2023 revaluation (effective 1 Apr 2023) re-set rateable values from 2017 list — modest North Yorkshire rural-site uplift, moderate York city-centre uplift"},
            {"label": "Multiplier 2024-25", "value": "Standard non-domestic multiplier 54.6p (England, 2024-25); NHS pays full rate (no charitable relief)"},
            {"label": "NDR 2024 Act context", "value": "Non-Domestic Rating (Multipliers and Private Finance) Act 2024 splits multipliers + reforms anti-avoidance"},
            {"label": "Funding trajectory", "value": "2021-22 c. £2.5M → 2023-24 c. £2.75M → 2024-25 £2.879M — multiplier + transitional uplift"},
            {"label": "Delivery body", "value": "Trust E&F (rates appeals) + Valuation Office Agency + City of York Council + North Yorkshire Council + East Riding of Yorkshire Council"},
            {"label": "Policy owner", "value": "MHCLG (NDR policy) + HM Treasury + DHSC + NHSE Provider Finance + Humber and North Yorkshire ICB"},
            {"label": "Evaluation evidence", "value": "VOA Rating List 2023; NAO Business Rates Reform; Trust ARA 2023-24; CQC RCB inspections"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-LGR district-billing structure for non-York sites · Successor: 2026 revaluation cycle + NDR 2024 Act multiplier-split implementation"}
        ],
        "notes": "York and Scarborough Teaching Hospitals' rates line is unusually fragmented — covering one of England's largest acute-trust catchments by area with six sites across three billing authorities (City of York Council, the new North Yorkshire Council formed in April 2023 from the pre-LGR district structure, and East Riding of Yorkshire Council). The April 2023 North Yorkshire LGR simplified billing for non-York sites into a single unitary, reducing administrative overhead. The VOA 2023 revaluation lifted city-centre York values moderately and rural sites modestly. NHS pays full 54.6p multiplier with no charitable relief; the NDR 2024 Act's multiplier-split reform reshapes future bills.",
        "sources": [
            {"publisher": "York and Scarborough Teaching Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.yorkhospitals.nhs.uk/about-us/our-publications/"},
            {"publisher": "Valuation Office Agency", "title": "2023 Rating List", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "Ministry of Housing, Communities and Local Government", "title": "Non-Domestic Rating Act 2023 + Multipliers and Private Finance Act 2024", "url": "https://www.gov.uk/government/collections/business-rates"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "York and Scarborough Teaching Hospitals NHS FT provider profile (RCB)", "url": "https://www.cqc.org.uk/provider/RCB"}
        ],
        "related": ["York and Scarborough Teaching Hospitals NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Business rates — Hull University Teaching Hospitals NHS Trust", "Business rates — St George's University Hospitals NHS Foundation Trust", "Valuation Office Agency"]
    },
    "Amortisation — Salisbury NHS Foundation Trust": {
        "aliases": [{"name": "Amortisation", "parent": "Salisbury NHS Foundation Trust"}],
        "description": "Salisbury's £2.878M amortisation line covers systematic write-down of intangible assets — capitalised software, EPR licences, internally-developed clinical applications and licensed-IP — under IAS 38 across the Salisbury District Hospital footprint. The trust runs a Cerner-based EPR (one of the earlier NHS Cerner adopters from the National Programme for IT era) plus capitalised tertiary-specialty digital systems for the Spinal Treatment Centre, Plastic Surgery and Burns Service and Wessex Genomics — all driving distinct intangible-asset amortisation profiles.",
        "beneficiaries": "c. 4,500 WTE staff serving a c. 270,000 South Wiltshire local catchment plus tertiary referrals to Spinal (regional spinal injuries), Burns and Plastics (South Coast network) and Wessex Genomics (regional); c. 75,000 ED attendances/yr at Salisbury District Hospital ED; c. 50,000 admissions/yr.",
        "legal_basis": "IAS 38 Intangible Assets — DHSC Group Accounting Manual 2024-25 (chapter 5 — Intangibles) — IFRS 15 / IAS 38 SaaS configuration agenda decisions — NHS Act 2006 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£2.878M"},
            {"label": "Trust scale", "value": "Salisbury District Hospital (c. 470 beds); c. 4,500 WTE"},
            {"label": "Tertiary specialty", "value": "Duke of Cornwall Spinal Treatment Centre + Wessex Regional Burns + Plastic Surgery + Wessex Genomics — distinct intangible-asset capitalisation profiles"},
            {"label": "Composition", "value": "Capitalised software + Cerner EPR licences + internally-developed clinical applications + licensed IP"},
            {"label": "EPR / Frontline Digitisation", "value": "Cerner adoption from NPfIT-era — long-running amortisation tail; Frontline Digitisation track adds capitalised optimisation build"},
            {"label": "Useful economic life", "value": "Software 3-5 years; EPR / clinical-system 5-10 years per DHSC GAM ch.5 + IAS 38 review"},
            {"label": "IFRIC SaaS agenda decision", "value": "2021 IFRIC agenda decision on SaaS configuration costs — restricts capitalisation; some Frontline Digitisation programme spend now opex"},
            {"label": "Funding trajectory", "value": "2021-22 c. £2.4M → 2023-24 c. £2.75M → 2024-25 £2.878M — Frontline Digitisation amortisation cycle + tertiary digital build"},
            {"label": "Delivery body", "value": "Trust IT + Finance (capitalisation) + EPR vendor (Oracle Health / Cerner) + NHSE Frontline Digitisation programme + Genomics England (Wessex node)"},
            {"label": "Policy owner", "value": "DHSC + NHSE Transformation Directorate + NHSE Provider Finance + Bath, Swindon and Wiltshire ICB"},
            {"label": "Evaluation evidence", "value": "NAO Digital transformation in NHS 2020; DHSC GAM ch.5; Trust ARA 2023-24; CQC RNZ inspections"},
            {"label": "Predecessor / successor", "value": "Predecessor: NPfIT-era Cerner amortisation tail · Successor: full Frontline Digitisation amortisation peak + post-IFRIC SaaS reclassification"}
        ],
        "notes": "Salisbury's amortisation line tracks a long-running Cerner-EPR amortisation tail (Salisbury was an earlier-cohort NPfIT-era Cerner adopter) layered on Frontline Digitisation capitalised optimisation build under IAS 38 and DHSC GAM ch.5 (5-10 year UEL). The tertiary specialty footprint — Duke of Cornwall Spinal Treatment Centre, Wessex Regional Burns and Plastics, and Wessex Genomics — drives distinct intangible-asset capitalisation profiles for specialty-specific clinical systems. The 2021 IFRIC SaaS agenda decision restricted SaaS configuration capitalisation, pushing some programme spend into opex. Industrial action 2023-24 had no direct amortisation effect; ongoing EPR optimisation continues to feed capitalisable intangibles.",
        "sources": [
            {"publisher": "Salisbury NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.salisbury.nhs.uk/about-us/publications/annual-reports/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 5 — Intangibles)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/connecting-health-and-care/frontline-digitisation/"},
            {"publisher": "National Audit Office", "title": "Digital transformation in the NHS (HC 317, 2020)", "url": "https://www.nao.org.uk/reports/the-use-of-digital-technology-in-the-nhs/"},
            {"publisher": "Care Quality Commission", "title": "Salisbury NHS Foundation Trust provider profile (RNZ)", "url": "https://www.cqc.org.uk/provider/RNZ"}
        ],
        "related": ["Salisbury NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Frontline Digitisation", "Business rates — York and Scarborough Teaching Hospitals NHS Foundation Trust", "NHS England"]
    },
    "General supplies & services — Gateshead Health NHS Foundation Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "Gateshead Health NHS Foundation Trust"}],
        "description": "Gateshead Health's £2.875M general supplies & services line covers non-clinical consumables, linen, catering, hotel-services materials, office supplies, IT consumables and minor expensed equipment across the Queen Elizabeth Hospital Gateshead main acute site, Bensham Hospital and Blaydon Primary Care Centre. The trust runs the QE Hospital private finance initiative-built (1999) flagship and operates QE Facilities Ltd as a wholly-owned subsidiary delivering FM and procurement scaling — affecting the consumable-ownership boundary in the accounts.",
        "beneficiaries": "c. 4,500 WTE staff serving a c. 200,000 Gateshead local catchment plus regional women's-services and laboratory referrals across North East ICS; c. 90,000 ED attendances/yr at QE Gateshead ED; c. 55,000 admissions/yr; QE Hospital + Bensham Hospital + Blaydon community footprint.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) — IAS 2 Inventories — Procurement Act 2023 — NHS Act 2006 — Health and Care Act 2022 — NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "General supplies & services 2024-25", "value": "£2.875M"},
            {"label": "Trust scale", "value": "Queen Elizabeth Hospital Gateshead + Bensham Hospital + Blaydon Primary Care Centre; c. 4,500 WTE"},
            {"label": "QE Facilities Ltd + PFI", "value": "Wholly-owned trust subsidiary delivering FM, hotel services, procurement scaling (pioneer NHS subsidiary model); QE Hospital partial PFI (1999) — affects consumable-ownership boundaries"},
            {"label": "Procurement route", "value": "NHS Supply Chain national framework + QE Facilities Ltd subsidiary procurement + North East and North Cumbria ICS collaborative"},
            {"label": "Composition", "value": "Linen, catering provisions, hotel-services materials, office supplies, IT consumables, minor expensed equipment"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove cancellation rebooking + agency-backfill consumable churn"},
            {"label": "April 2025 NIC + CPI uplift", "value": "Indirect via supplier pass-through; non-clinical CPI feed forward unit-cost pressure"},
            {"label": "Funding trajectory", "value": "2021-22 c. £2.3M → 2023-24 c. £2.7M → 2024-25 £2.875M — sustained CPI + activity uplift"},
            {"label": "Delivery body", "value": "Trust Procurement + QE Facilities Ltd subsidiary + NHS Supply Chain (DHSC ALB) + North East and North Cumbria ICS procurement collaborative"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + North East and North Cumbria ICB"},
            {"label": "Evaluation evidence", "value": "Model Hospital benchmarks; NHS Supply Chain ARA; HMRC subsidiary VAT scheme reviews; CQC RR7 inspections; Trust ARA 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-QE Facilities subsidiary direct-procurement baseline · Successor: ICS-collaborative procurement scaling + post-VAT-scheme HMRC review settlement"}
        ],
        "notes": "Gateshead Health is a pioneer of the NHS wholly-owned-subsidiary model — QE Facilities Ltd delivers FM, hotel services and procurement scaling, affecting which consumable inputs flow through the trust accounts versus the subsidiary's. The arrangement also became one of the early test cases for NHS subsidiary VAT structures and HMRC scrutiny. NHS Supply Chain remains dominant for non-clinical consumables, with North East and North Cumbria ICS procurement collaborative scaling as a medium-term lever. The QE Hospital partial PFI (1999) shapes additional consumable-ownership boundaries with the FM contractor cohort. Industrial action 2023-24 drove cancellation-rebooking and agency-backfill consumable churn; April 2025 NIC step-up and CPI feed forward via supplier pass-through.",
        "sources": [
            {"publisher": "Gateshead Health NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.gatesheadhealth.nhs.uk/about-us/publications/"},
            {"publisher": "NHS Supply Chain", "title": "Annual Report 2023-24", "url": "https://www.supplychain.nhs.uk/about-us/our-publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Gateshead Health NHS FT provider profile (RR7)", "url": "https://www.cqc.org.uk/provider/RR7"},
            {"publisher": "HM Revenue and Customs", "title": "VAT and the NHS — wholly-owned subsidiaries guidance", "url": "https://www.gov.uk/guidance/vat-government-and-public-bodies-notice-70150"}
        ],
        "related": ["Gateshead Health NHS Foundation Trust", "Clinical Supplies & Drugs", "NHS Acute Trusts", "General supplies & services — The Hillingdon Hospitals NHS Foundation Trust", "General supplies & services — Airedale NHS Foundation Trust", "NHS Supply Chain"]
    },
    "Transport (business + patient) — County Durham and Darlington NHS Foundation Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "County Durham and Darlington NHS Foundation Trust"}],
        "description": "CDDFT's £2.853M transport line covers business mileage, pool-fleet IFRS 16 lease costs, NEPTS contract pass-through and patient travel reimbursements across an unusually broad multi-site footprint — University Hospital of North Durham, Darlington Memorial Hospital, Bishop Auckland Hospital, Shotley Bridge Hospital plus integrated community services across County Durham and Darlington. Cross-site clinical-network flows and rural NEPTS demand drive a significant patient-transport share. NEPTS is commissioned through the North East ICS lead-commissioner.",
        "beneficiaries": "c. 7,000 WTE staff serving a c. 600,000 County Durham and Darlington catchment; c. 145,000 ED attendances/yr (Durham + Darlington EDs + Bishop Auckland UCC); c. 75,000 admissions/yr; multi-site geographically dispersed footprint with significant rural/semi-rural element.",
        "legal_basis": "NHS Act 2006 — NHSE Patient Transport Services Eligibility Criteria 2021 — Agenda for Change Section 17 (business mileage) — HMRC AMAP rates — IFRS 16 Leases (pool fleet) — DHSC Group Accounting Manual 2024-25 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£2.853M"},
            {"label": "Trust scale", "value": "University Hospital of North Durham + Darlington Memorial Hospital + Bishop Auckland Hospital + Shotley Bridge Hospital + community sites; c. 7,000 WTE"},
            {"label": "Reconfiguration + rural NEPTS", "value": "Bishop Auckland reconfigured to elective + UCC; Durham + Darlington concentrate emergency; Weardale, Teesdale, rural Durham villages drive long-distance NEPTS above urban-DGH baselines"},
            {"label": "NEPTS commissioning", "value": "North East and North Cumbria ICS lead-commissioner NEPTS contract; eligibility per NHSE 2021 criteria"},
            {"label": "Composition", "value": "Business mileage (AfC S17 + AMAP 45p/25p) + pool-fleet IFRS 16 leases + NEPTS pass-through + patient travel reimbursements"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove cancellation rebooking + agency travel claims"},
            {"label": "April 2025 NIC + fuel CPI", "value": "Indirect via NEPTS contractor pass-through + diesel CPI feed forward unit-cost pressure"},
            {"label": "Funding trajectory", "value": "2021-22 c. £2.3M → 2023-24 c. £2.6M → 2024-25 £2.853M — fuel CPI + NEPTS contract uplift + cross-site reconfig flows"},
            {"label": "Delivery body", "value": "Trust E&F + outsourced NEPTS provider (NENC ICS lead-commissioner) + pool-fleet leasing partner + Trust HR (mileage)"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + NHSE Urgent and Emergency Care (NEPTS) + North East and North Cumbria ICB + DHSC"},
            {"label": "Evaluation evidence", "value": "NAO NEPTS 2019; CQC RXP inspections; NHSE NEPTS Eligibility Review 2021; Trust ARA 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-ICS CCG-commissioned NEPTS contracts · Successor: NENC ICS-collaborative NEPTS retender + further site reconfiguration"}
        ],
        "notes": "CDDFT's transport line carries a distinctive rural-NEPTS share — Weardale, Teesdale and rural County Durham villages drive long-distance patient journeys above urban-DGH peer baselines, with the trust's Bishop Auckland reconfiguration to elective + UCC concentrating emergency volumes at Durham and Darlington. The North East and North Cumbria ICS lead-commissioner NEPTS contract structure shapes contract economics, with NHSE 2021 eligibility criteria tightening the patient-paid threshold. Industrial action 2023-24 drove cancellation-rebooking and agency travel claims; HMRC AMAP-rate freeze at 45p/mile since 2011 sustains internal-rate dispute pressure. Diesel CPI and April 2025 NIC step-up feed forward via NEPTS contractor pass-through.",
        "sources": [
            {"publisher": "County Durham and Darlington NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.cddft.nhs.uk/about-us/our-publications.aspx"},
            {"publisher": "NHS England", "title": "Non-Emergency Patient Transport Services — National Framework + Eligibility Criteria 2021", "url": "https://www.england.nhs.uk/publication/non-emergency-patient-transport-services-nepts/"},
            {"publisher": "National Audit Office", "title": "NHS England's management of the primary care support services contract with Capita", "url": "https://www.nao.org.uk/reports/nhs-englands-management-of-the-primary-care-support-services-contract-with-capita/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "County Durham and Darlington NHS FT provider profile (RXP)", "url": "https://www.cqc.org.uk/provider/RXP"}
        ],
        "related": ["County Durham and Darlington NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Transport (business + patient) — Isle of Wight NHS Trust", "Transport (business + patient) — Gloucestershire Hospitals NHS Foundation Trust", "NHS England"]
    },
    "Transport (business + patient) — Isle of Wight NHS Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "Isle of Wight NHS Trust"}],
        "description": "Isle of Wight NHS Trust's £2.848M transport line is structurally distinctive in the NHS — the trust delivers acute, ambulance, mental-health and community services across the Isle of Wight from St Mary's Hospital (Newport, IoW), with cross-Solent ferry-based patient transfers to mainland tertiary centres (UHS Southampton, Portsmouth, Southampton General) a structural daily feature. The line covers business mileage, ambulance operations (the trust runs the IoW ambulance service in-house), pool-fleet IFRS 16 lease costs, NEPTS contract pass-through and ferry-related patient travel.",
        "beneficiaries": "c. 3,000 WTE staff serving the c. 140,000 Isle of Wight catchment plus tourist-season uplift; c. 60,000 ED attendances/yr at St Mary's ED (the only ED on the Isle of Wight); c. 30,000 admissions/yr; integrated acute + ambulance + community + mental health services — the only fully-integrated all-services trust in England.",
        "legal_basis": "NHS Act 2006 — NHSE Patient Transport Services Eligibility Criteria 2021 — Agenda for Change Section 17 (business mileage) — HMRC AMAP rates — IFRS 16 Leases (pool fleet) — DHSC Group Accounting Manual 2024-25 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£2.848M"},
            {"label": "Trust scale", "value": "St Mary's Hospital (Newport, IoW) + community + ambulance + mental health; c. 3,000 WTE"},
            {"label": "Integrated all-services + ambulance", "value": "Only fully-integrated acute + ambulance + community + mental health trust in England; in-house IoW Ambulance (CAT-1 + CAT-2 999) embedded in transport line"},
            {"label": "Cross-Solent transfers", "value": "Patient transfers to UHS Southampton + Portsmouth tertiary services via Wightlink + Red Funnel ferries — structural daily feature"},
            {"label": "Tourist-season uplift", "value": "Summer tourist population materially lifts ED + ambulance demand May-Sep — drives seasonal transport workload"},
            {"label": "Composition", "value": "Business mileage (AfC S17 + AMAP) + ambulance ops + pool-fleet IFRS 16 + cross-Solent ferry travel + NEPTS pass-through"},
            {"label": "Industrial action + fuel CPI", "value": "44 days junior-doctor + 10 days consultant strikes drove cancellation rebooking; ferry-tariff + diesel CPI + Apr 2025 NIC feed forward"},
            {"label": "Funding trajectory", "value": "2021-22 c. £2.3M → 2023-24 c. £2.6M → 2024-25 £2.848M — fuel CPI + ferry-tariff CPI + activity"},
            {"label": "Delivery body", "value": "Trust E&F + IoW Ambulance Service + Wightlink/Red Funnel ferry contracts + Hampshire and Isle of Wight ICS"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + NHSE UEC + Hampshire and Isle of Wight ICB + DHSC"},
            {"label": "Evaluation evidence", "value": "NAO NEPTS 2019; CQC R1F inspections; NHSE Special Measures interventions (historical); Trust ARA 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2017 NHSE Special-Measures intervention baseline · Successor: HIOW ICS partnership with UHS Southampton + structural transformation programme"}
        ],
        "notes": "Isle of Wight NHS Trust is structurally unique in the English NHS — the only fully-integrated trust delivering acute, ambulance, community and mental-health services from a single statutory body — with cross-Solent ferry-based patient transfers to UHS Southampton and Portsmouth a structural daily feature. The in-house ambulance service embeds CAT-1 and CAT-2 999 response within the transport-line cost structure, distinguishing the trust from peer Acute trusts whose ambulance is contracted-in. Tourist-season demand uplift (May-Sep) drives material seasonal variation. Ferry-tariff CPI and diesel CPI feed forward ahead of HIOW ICS partnership transformation with UHS.",
        "sources": [
            {"publisher": "Isle of Wight NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.iow.nhs.uk/about-us/our-publications/annual-reports-and-accounts.htm"},
            {"publisher": "NHS England", "title": "Non-Emergency Patient Transport Services — National Framework + Eligibility Criteria 2021", "url": "https://www.england.nhs.uk/publication/non-emergency-patient-transport-services-nepts/"},
            {"publisher": "National Audit Office", "title": "NHS Ambulance Services (HC 972, 2017)", "url": "https://www.nao.org.uk/reports/nhs-ambulance-services/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Isle of Wight NHS Trust provider profile (R1F)", "url": "https://www.cqc.org.uk/provider/R1F"}
        ],
        "related": ["Isle of Wight NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Transport (business + patient) — University Hospital Southampton NHS Foundation Trust", "Transport (business + patient) — County Durham and Darlington NHS Foundation Trust", "NHS England"]
    },
    "Establishment costs — Maidstone And Tunbridge Wells NHS Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "Maidstone And Tunbridge Wells NHS Trust"}],
        "description": "MTW's £2.832M establishment costs line covers postage, telephony, mobile-data, printing, stationery, recruitment advertising, subscriptions and minor sundries across the Maidstone Hospital and Tunbridge Wells Hospital (Pembury, PFI 2011) twin-site footprint. Tunbridge Wells is one of the larger second-wave PFI flagships — a £225M build operational from 2011 — shaping the back-office overhead allocation and FM-contractor consumable boundary. EPR rollout under Frontline Digitisation and industrial-action recruitment campaigns shape 2024-25 spend.",
        "beneficiaries": "c. 7,000 WTE staff serving a c. 590,000 west Kent catchment (Maidstone, Tunbridge Wells, Tonbridge, Sevenoaks); c. 145,000 ED attendances/yr (Maidstone ED + Tunbridge Wells ED Pembury); c. 75,000 admissions/yr; covers Maidstone Hospital + Tunbridge Wells Hospital Pembury PFI flagship.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) — IAS 1 Presentation of Financial Statements — NHS Act 2006 — Health and Care Act 2022 — NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£2.832M"},
            {"label": "Trust scale", "value": "Maidstone Hospital + Tunbridge Wells Hospital (Pembury, PFI 2011); c. 7,000 WTE"},
            {"label": "Composition", "value": "Postage, telephony/mobile, printing, stationery, recruitment advertising, subscriptions, hospitality, minor sundries"},
            {"label": "Tunbridge Wells PFI + EPR", "value": "Pembury PFI £225M operational 2011 (second-wave flagship; FM cohort affects back-office allocation); Frontline Digitisation track drives change-mgmt comms + training-materials"},
            {"label": "Industrial action 2023-24", "value": "44 days junior-doctor + 10 days consultant strikes drove recruitment-advertising spike + comms costs"},
            {"label": "April 2025 NIC + CPI uplift", "value": "Royal Mail + telecoms CPI feed forward unit-cost pressure"},
            {"label": "Cancer specialty", "value": "Kent Oncology Centre (Maidstone) regional cancer service — drives specialty patient-comms postage volume"},
            {"label": "Funding trajectory", "value": "2021-22 c. £2.3M → 2023-24 c. £2.6M → 2024-25 £2.832M — sustained CPI + activity uplift"},
            {"label": "Delivery body", "value": "Trust Corporate Services + Procurement + IT + Crown Commercial Service framework (telecoms/postage)"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Kent and Medway ICB"},
            {"label": "Evaluation evidence", "value": "Model Hospital corporate-services benchmark; CQC RWF inspections; NAO PFI legacy reports; Trust ARA 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-Pembury-PFI baseline · Successor: post-EPR digital-comms shift + Kent and Medway ICS-collaborative back-office scaling"}
        ],
        "notes": "MTW's establishment-costs baseline reflects a twin-site west Kent footprint with the Tunbridge Wells Pembury PFI (£225M, operational 2011) shaping back-office overhead allocation — the second-wave PFI flagship's FM contractor cohort affects which non-clinical overheads flow through the trust accounts versus the SPV. The Kent Oncology Centre at Maidstone adds regional cancer-service patient-comms postage volume above peer DGH baselines. EPR rollout under the Frontline Digitisation track drives change-management printing and digital-training materials. Industrial action 2023-24 lifted recruitment-advertising spend through agency-recruitment campaigns. April 2025 employer-NIC step-up sits outside this line but Royal Mail and telecoms CPI feed forward unit-cost pressure into 2025-26.",
        "sources": [
            {"publisher": "Maidstone And Tunbridge Wells NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.mtw.nhs.uk/about-us/publications/"},
            {"publisher": "National Audit Office", "title": "PFI and PF2 (HC 718, 2018)", "url": "https://www.nao.org.uk/reports/pfi-and-pf2/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Maidstone And Tunbridge Wells NHS Trust provider profile (RWF)", "url": "https://www.cqc.org.uk/provider/RWF"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme (EPR rollout)", "url": "https://www.england.nhs.uk/digitaltechnology/connecting-health-and-care/frontline-digitisation/"}
        ],
        "related": ["Maidstone And Tunbridge Wells NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Establishment costs — Countess of Chester Hospital NHS Foundation Trust", "Frontline Digitisation", "Department of Health and Social Care"]
    },
    "Business rates — Hull University Teaching Hospitals NHS Trust": {
        "aliases": [{"name": "Business rates", "parent": "Hull University Teaching Hospitals NHS Trust"}],
        "description": "HUTH's £2.822M business-rates line covers non-domestic rates on Hull Royal Infirmary and Castle Hill Hospital (Cottingham) — the trust's two main acute sites — plus Princess Royal Hospital and outpatient outposts. Hull Royal Infirmary is in the New Hospital Programme cohort with rebuild deferred under the January 2025 NHP Reset, sustaining the existing high-rateable-value tower hereditament. Hull City Council and East Riding of Yorkshire Council collect, with VOA assessing rateable values on the 2023 list. NHS pays full multiplier (no charitable relief).",
        "beneficiaries": "c. 9,500 WTE staff serving a c. 600,000 Hull and East Riding catchment plus tertiary referrals from North Lincolnshire and parts of North Yorkshire; c. 165,000 ED attendances/yr at Hull Royal Infirmary ED; c. 95,000 admissions/yr; covers Hull Royal Infirmary + Castle Hill Hospital (Cottingham) + Princess Royal Hospital.",
        "legal_basis": "Local Government Finance Act 1988 (Schedule 6) — Non-Domestic Rating (Multipliers and Private Finance) Act 2024 — Non-Domestic Rating Act 2023 — DHSC Group Accounting Manual 2024-25 — NHS Act 2006 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£2.822M"},
            {"label": "Trust scale", "value": "Hull Royal Infirmary + Castle Hill Hospital (Cottingham) + Princess Royal Hospital; c. 9,500 WTE"},
            {"label": "NHP cohort + Castle Hill specialty", "value": "Hull Royal Infirmary in original NHP cohort, rebuild deferred under Jan 2025 NHP Reset; Castle Hill (Cottingham) hosts Queen's Centre for Oncology + Cardiology — tertiary hereditaments"},
            {"label": "Billing authorities", "value": "Hull City Council (Hull Royal Infirmary) + East Riding of Yorkshire Council (Castle Hill Cottingham)"},
            {"label": "2023 revaluation", "value": "VOA 2023 revaluation (effective 1 Apr 2023) re-set rateable values from 2017 list — modest Yorkshire urban uplift"},
            {"label": "Multiplier 2024-25", "value": "Standard non-domestic multiplier 54.6p (England, 2024-25); NHS pays full rate (no charitable relief)"},
            {"label": "NDR 2024 Act context", "value": "Non-Domestic Rating (Multipliers and Private Finance) Act 2024 splits multipliers + reforms anti-avoidance"},
            {"label": "Funding trajectory", "value": "2021-22 c. £2.5M → 2023-24 c. £2.7M → 2024-25 £2.822M — multiplier + transitional uplift"},
            {"label": "Delivery body", "value": "Trust E&F (rates appeals) + Valuation Office Agency + Hull City Council + East Riding of Yorkshire Council"},
            {"label": "Policy owner", "value": "MHCLG (NDR policy) + HM Treasury + DHSC + NHSE Provider Finance + Humber and North Yorkshire ICB + NHP programme team"},
            {"label": "Evaluation evidence", "value": "VOA Rating List 2023; NAO Business Rates Reform; NAO New Hospital Programme; Trust ARA 2023-24; CQC RWA inspections"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2017 rating list baseline · Successor: 2026 revaluation cycle + post-NHP Reset rebuild trajectory + multiplier-split implementation"}
        ],
        "notes": "HUTH's rates line is dominated by the Hull Royal Infirmary tower hereditament — one of the more dated NHS tower-block estates whose rebuild was scheduled under the original New Hospital Programme cohort but has been deferred under the January 2025 NHP Reset, sustaining the existing rateable-value baseline for the medium term. Castle Hill Hospital (Cottingham) under East Riding of Yorkshire Council adds Queen's Centre for Oncology and Cardiology hereditaments. The VOA 2023 revaluation lifted Yorkshire urban hospital values modestly with transitional relief tapering. NHS pays full 54.6p standard multiplier with no charitable relief; the Non-Domestic Rating (Multipliers and Private Finance) Act 2024's multiplier-split reform reshapes future bills for large hereditaments.",
        "sources": [
            {"publisher": "Hull University Teaching Hospitals NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.hey.nhs.uk/about-us/our-publications/"},
            {"publisher": "Valuation Office Agency", "title": "2023 Rating List", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "National Audit Office", "title": "Progress with the New Hospital Programme (HC 1062, 2023)", "url": "https://www.nao.org.uk/reports/progress-with-the-new-hospital-programme/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Hull University Teaching Hospitals NHS Trust provider profile (RWA)", "url": "https://www.cqc.org.uk/provider/RWA"}
        ],
        "related": ["Hull University Teaching Hospitals NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Business rates — York and Scarborough Teaching Hospitals NHS Foundation Trust", "Business rates — The Royal Wolverhampton NHS Trust", "Valuation Office Agency"]
    },
    "General supplies & services — Great Western Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "Great Western Hospitals NHS Foundation Trust"}],
        "description": "GWH's £2.8035M general supplies & services line covers non-clinical consumables, linen, catering, hotel-services materials, office supplies, IT consumables and minor expensed equipment across the Great Western Hospital Swindon (PFI 2002) main site plus integrated community services across Wiltshire and Bath & North East Somerset (BSW ICS). The acute + community integrated workforce broadens the consumable base above acute-only peer trusts of similar bed count, with PFI hotel-services subcontractor cohort affecting consumable-ownership boundaries.",
        "beneficiaries": "c. 5,500 WTE staff serving a c. 350,000 Swindon catchment plus c. 1.0M for community services across Wiltshire and BaNES; c. 110,000 ED attendances/yr at Great Western ED; c. 60,000 admissions/yr; integrated community workforce (district nursing + community-paediatric + sexual-health + school-nursing).",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) — IAS 2 Inventories — Procurement Act 2023 — NHS Act 2006 — Health and Care Act 2022 — NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "General supplies & services 2024-25", "value": "£2.8035M"},
            {"label": "Trust scale", "value": "Great Western Hospital Swindon (PFI operational 2002) + integrated Wiltshire + BaNES community services; c. 5,500 WTE"},
            {"label": "PFI + integrated community", "value": "GWH PFI signed 2000, operational 2002; Carillion Jan 2018 collapse → FM novations affect consumable-ownership boundary; Wiltshire + BaNES community integration broadens non-clinical consumable base"},
            {"label": "Procurement route", "value": "NHS Supply Chain national framework + trust-direct contracts + BSW ICS procurement collaborative"},
            {"label": "Composition", "value": "Linen, catering provisions, hotel-services materials, office supplies, IT consumables, minor expensed equipment + community-team consumables"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove cancellation rebooking + agency-backfill consumable churn"},
            {"label": "April 2025 NIC + CPI uplift", "value": "Indirect via supplier pass-through; non-clinical CPI feed forward unit-cost pressure"},
            {"label": "Funding trajectory", "value": "2021-22 c. £2.3M → 2023-24 c. £2.6M → 2024-25 £2.8035M — sustained CPI + activity uplift"},
            {"label": "Delivery body", "value": "Trust Procurement + NHS Supply Chain (DHSC ALB) + BSW ICS procurement collaborative + PFI soft-FM subcontractors (boundary)"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Bath, Swindon and Wiltshire ICB"},
            {"label": "Evaluation evidence", "value": "Model Hospital benchmarks; NHS Supply Chain ARA; NAO PFI legacy reports; CQC RN3 inspections; Trust ARA 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-Carillion-collapse FM-contractor baseline · Successor: post-2032 PFI hand-back consumable-boundary reset + ICS-collaborative procurement scaling"}
        ],
        "notes": "GWH's general supplies & services baseline reflects the acute + Wiltshire + BaNES community-services integrated model — consumables flow through district-nursing, community-paediatric, sexual-health and school-nursing teams alongside the Swindon acute site, broadening the non-clinical consumable base above acute-only peers. The Swindon PFI (operational 2002, 30-year concession to 2032) shapes hotel-services consumable-ownership boundaries, with Carillion's January 2018 collapse and subsequent novations adding contract-management complexity. NHS Supply Chain remains dominant; BSW ICS procurement collaborative scales medium-term. Industrial action 2023-24 drove cancellation-rebooking churn; Apr 2025 NIC + CPI feed forward via supplier pass-through.",
        "sources": [
            {"publisher": "Great Western Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.gwh.nhs.uk/about-us/key-publications/"},
            {"publisher": "NHS Supply Chain", "title": "Annual Report 2023-24", "url": "https://www.supplychain.nhs.uk/about-us/our-publications/"},
            {"publisher": "National Audit Office", "title": "Investigation into the rescue of Carillion's PFI hospital contracts", "url": "https://www.nao.org.uk/reports/investigation-into-the-rescue-of-carillions-pfi-hospital-contracts/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Great Western Hospitals NHS FT provider profile (RN3)", "url": "https://www.cqc.org.uk/provider/RN3"}
        ],
        "related": ["Great Western Hospitals NHS Foundation Trust", "Clinical Supplies & Drugs", "NHS Acute Trusts", "General supplies & services — Gateshead Health NHS Foundation Trust", "General supplies & services — Airedale NHS Foundation Trust", "NHS Supply Chain"]
    },
    "General supplies & services — Airedale NHS Foundation Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "Airedale NHS Foundation Trust"}],
        "description": "Airedale's £2.792M general supplies & services line covers non-clinical consumables, linen, catering, hotel-services materials, office supplies, IT consumables and minor expensed equipment at Airedale General Hospital (Steeton, Keighley) plus community sites. Airedale General Hospital is the most prominent RAAC-affected acute trust in England — placed in the original New Hospital Programme cohort with confirmed 2030 rebuild commitment under the January 2025 NHP Reset (one of the few protected schemes) — driving distinctive consumable-flow disruption from RAAC mitigation works.",
        "beneficiaries": "c. 3,200 WTE staff serving a c. 200,000 Craven, Wharfedale, Aire Valley and South Pennines catchment (Keighley, Skipton, Bingley, Ilkley, plus parts of Bradford and East Lancashire); c. 75,000 ED attendances/yr at Airedale ED; c. 45,000 admissions/yr; covers Airedale General Hospital + community sites.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) — IAS 2 Inventories — Procurement Act 2023 — NHS Act 2006 — Health and Care Act 2022 — NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "General supplies & services 2024-25", "value": "£2.792M"},
            {"label": "Trust scale", "value": "Airedale General Hospital (Steeton, Keighley) + community sites; c. 3,200 WTE"},
            {"label": "RAAC + NHP protected scheme", "value": "Most prominent RAAC-affected NHS hospital — c. 80%+ RAAC-built (HSSIB 2023); rebuild confirmed under Jan 2025 NHP Reset as protected scheme, target 2030; mitigation works ongoing 2024-25"},
            {"label": "Decant + mitigation", "value": "Failsafe propping + clinical-area decant drive temporary modular consumables, additional cleaning materials, increased PPE"},
            {"label": "Procurement route", "value": "NHS Supply Chain national framework + trust-direct + West Yorkshire ICS procurement collaborative + decant-specific contracts"},
            {"label": "Composition", "value": "Linen, catering provisions, hotel-services materials, office supplies, IT consumables, minor expensed equipment + RAAC-mitigation consumables"},
            {"label": "Industrial action + Apr 2025 NIC", "value": "44 days junior-doctor + 10 days consultant strikes drove cancellation rebooking layered on RAAC disruption; Apr 2025 NIC + CPI feed forward via supplier pass-through"},
            {"label": "Funding trajectory", "value": "2021-22 c. £2.2M → 2023-24 c. £2.6M (RAAC mitigation begins) → 2024-25 £2.792M — RAAC mitigation + sustained CPI"},
            {"label": "Delivery body", "value": "Trust Procurement + NHS Supply Chain (DHSC ALB) + West Yorkshire ICS procurement collaborative + NHP Programme team"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + West Yorkshire ICB + NHP RAAC programme team"},
            {"label": "Evaluation evidence", "value": "HSSIB RAAC report 2023; NAO New Hospital Programme; NHSE RAAC eradication programme; CQC RCF inspections; Trust ARA 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-RAAC-disclosure standard-DGH baseline · Successor: 2030 NHP rebuild new-build consumable-baseline reset on protected scheme"}
        ],
        "notes": "Airedale General Hospital is the most prominent RAAC-affected acute trust in England — Reinforced Autoclaved Aerated Concrete plank construction across c. 80%+ of the building, identified on the HSSIB September 2023 list. Failsafe propping, monitoring and clinical-area decant work disrupt consumable workflow with temporary modular consumables, additional cleaning materials and increased PPE feeding the line above peer DGH baselines. Airedale's rebuild is confirmed under the January 2025 NHP Reset as a protected RAAC-cohort scheme (target 2030). NHS Supply Chain remains dominant; West Yorkshire ICS procurement collaborative scales medium-term. Industrial action 2023-24 layered consumable churn on RAAC disruption.",
        "sources": [
            {"publisher": "Airedale NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.airedale-trust.nhs.uk/about-us/our-publications/"},
            {"publisher": "Health Services Safety Investigations Body", "title": "Reinforced Autoclaved Aerated Concrete in NHS estate (RAAC)", "url": "https://www.hssib.org.uk/"},
            {"publisher": "National Audit Office", "title": "Progress with the New Hospital Programme (HC 1062, 2023)", "url": "https://www.nao.org.uk/reports/progress-with-the-new-hospital-programme/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Airedale NHS FT provider profile (RCF)", "url": "https://www.cqc.org.uk/provider/RCF"}
        ],
        "related": ["Airedale NHS Foundation Trust", "Clinical Supplies & Drugs", "NHS Acute Trusts", "General supplies & services — Great Western Hospitals NHS Foundation Trust", "General supplies & services — Gateshead Health NHS Foundation Trust", "New Hospital Programme"]
    },
}
