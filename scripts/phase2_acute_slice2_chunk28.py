# -*- coding: utf-8 -*-
# Phase 2 Acute slice 2 — chunk 28 (17 NHS Acute Trust orphan sub-lines)
# Hand-curated trust-specific PROGRAMME-archetype enrichment entries.
# Structural contract per docs/archetype_briefs.md.

NEW = {
    "Transport (business + patient) — University Hospitals Coventry And Warwickshire NHS Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "University Hospitals Coventry And Warwickshire NHS Trust"}],
        "description": "UHCW's £2.305M transport line covers business mileage (AfC Section 17 + AMAP), pool-fleet IFRS 16 lease costs, NEPTS contract pass-through and patient travel reimbursements across the University Hospital Coventry main site and the Hospital of St Cross Rugby. UHCW is a major regional tertiary centre — kidney transplant, neurosciences, vascular and Major Trauma Centre status — driving substantial inter-hospital and inter-trust patient transfer demand. NEPTS is commissioned through the Coventry & Warwickshire ICS lead-commissioner.",
        "beneficiaries": "c. 11,000 WTE staff serving a c. 1.0M Coventry + Warwickshire catchment plus tertiary referrals from across the West Midlands; c. 165,000 ED attendances/yr at UHC ED (one of the busiest in the West Midlands); c. 105,000 admissions/yr; UHC hosts the regional Major Trauma Centre, kidney transplant centre and neurosciences tertiary specialism.",
        "legal_basis": "NHS Act 2006 — NHSE Patient Transport Services Eligibility Criteria 2021 — Agenda for Change Section 17 (business mileage) — HMRC AMAP rates — IFRS 16 Leases (pool fleet) — DHSC Group Accounting Manual 2024-25 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£2.305M"},
            {"label": "Trust scale", "value": "University Hospital Coventry (c. 1,250 beds) + Hospital of St Cross Rugby; c. 11,000 WTE"},
            {"label": "Tertiary specialty", "value": "Major Trauma Centre + kidney transplant + neurosciences + vascular tertiary — high inter-hospital transfer demand"},
            {"label": "NEPTS commissioning", "value": "Coventry and Warwickshire ICS lead-commissioner NEPTS contract; eligibility per NHSE 2021 criteria"},
            {"label": "Composition", "value": "Business mileage (AfC S17 + AMAP 45p/25p frozen since 2011) + pool-fleet IFRS 16 leases + NEPTS pass-through + patient travel reimbursements"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove cancellation rebooking + agency travel claims"},
            {"label": "April 2025 NIC + fuel CPI", "value": "Indirect via NEPTS contractor pass-through + diesel CPI feed forward unit-cost pressure"},
            {"label": "Funding trajectory", "value": "2021-22 c. £1.85M → 2023-24 c. £2.1M → 2024-25 £2.305M — fuel CPI + NEPTS contract uplift + activity recovery"},
            {"label": "Delivery body", "value": "Trust E&F + outsourced NEPTS provider (Coventry & Warwickshire ICS lead-commissioner) + pool-fleet leasing partner + Trust HR (mileage)"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + NHSE Urgent and Emergency Care (NEPTS) + Coventry and Warwickshire ICB + DHSC"},
            {"label": "Evaluation evidence", "value": "NAO NEPTS 2019; CQC RKB inspections; NHSE NEPTS Eligibility Review 2021; Trust ARA 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-ICS CCG-commissioned NEPTS contracts · Successor: ICS-collaborative NEPTS retender + tertiary-network transfer protocol refresh"}
        ],
        "notes": "UHCW's transport line is shaped by the trust's tertiary regional role across Coventry and Warwickshire — kidney transplant transfers from across the West Midlands, neurosciences referrals and Major Trauma Centre inter-hospital transfers all generate substantial NEPTS volume on top of routine business mileage between UHC and St Cross Rugby. The Coventry and Warwickshire ICS lead-commissioner NEPTS contract retender is the medium-term lever, with NHSE 2021 eligibility criteria tightening the patient-paid threshold. Industrial action 2023-24 drove cancellation-rebooking journeys and agency travel claims; HMRC AMAP-rate freeze at 45p/mile since 2011 sustains internal-rate dispute pressure. Diesel CPI and April 2025 NIC step-up feed forward via NEPTS contractor pass-through.",
        "sources": [
            {"publisher": "University Hospitals Coventry and Warwickshire NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.uhcw.nhs.uk/about-us/publications/"},
            {"publisher": "NHS England", "title": "Non-Emergency Patient Transport Services — National Framework + Eligibility Criteria 2021", "url": "https://www.england.nhs.uk/publication/non-emergency-patient-transport-services-nepts/"},
            {"publisher": "National Audit Office", "title": "NHS England's management of the primary care support services contract with Capita", "url": "https://www.nao.org.uk/reports/nhs-englands-management-of-the-primary-care-support-services-contract-with-capita/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "University Hospitals Coventry and Warwickshire provider profile (RKB)", "url": "https://www.cqc.org.uk/provider/RKB"}
        ],
        "related": ["University Hospitals Coventry And Warwickshire NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Transport (business + patient) — University Hospital Southampton NHS Foundation Trust", "Transport (business + patient) — Gloucestershire Hospitals NHS Foundation Trust", "NHS England"]
    },
    "PFI / LIFT charges — Nottingham University Hospitals NHS Trust": {
        "aliases": [{"name": "PFI / LIFT charges", "parent": "Nottingham University Hospitals NHS Trust"}],
        "description": "NUH's £2.287M PFI / LIFT line covers the unitary-charge pass-through on a smaller LIFT (Local Improvement Finance Trust) facility within the NUH portfolio — the bulk of NUH's estate (Queen's Medical Centre, City Hospital, Nottingham Children's Hospital) is publicly owned and the £2.287M figure reflects the residual LIFT-vehicle community-clinic / outpatient-extension element rather than a major hospital PFI. NUH is also a New Hospital Programme cohort trust under the NHP Reset January 2025 with the Tomorrow's NUH whole-site reconfiguration deferred.",
        "beneficiaries": "c. 16,000 WTE staff serving a c. 2.5M Nottinghamshire + East Midlands tertiary catchment; c. 250,000 ED attendances/yr (QMC ED is the regional Major Trauma Centre + Nottingham Children's ED); c. 175,000 admissions/yr; LIFT estate covers community/outpatient extension premises across the Nottingham conurbation supporting the wider Tertiary footprint.",
        "legal_basis": "IFRIC 12 Service Concession Arrangements — IFRS 16 Leases (post-2022 transition for service-concession components) — DHSC Group Accounting Manual 2024-25 ch.7 — Private Finance Initiative / NHS LIFT guidance (HM Treasury) — NHS Act 2006 — Health and Care Act 2022",
        "key_stats": [
            {"label": "PFI / LIFT charges 2024-25", "value": "£2.287M"},
            {"label": "Trust scale", "value": "Queen's Medical Centre + Nottingham City Hospital + Nottingham Children's Hospital + community LIFT footprint; c. 16,000 WTE"},
            {"label": "LIFT vehicle", "value": "Express LIFT / Nottingham LIFT-style community-clinic concession — far smaller than NUH's mainstream publicly-owned acute estate"},
            {"label": "Tomorrow's NUH / NHP context", "value": "NUH is a New Hospital Programme cohort trust — Tomorrow's NUH whole-site reconfiguration (QMC + City Hospital) deferred under Jan 2025 NHP Reset; LIFT line continues independently of capital-build deferral"},
            {"label": "Estate covered", "value": "LIFT-vehicle community / outpatient extension premises (modest hereditament base relative to NUH-wide opex)"},
            {"label": "Unitary charge composition", "value": "Senior debt service + lifecycle hard-FM + indexed soft-FM (cleaning, security, minor maintenance)"},
            {"label": "Indexation mechanism", "value": "RPI-linked annual uplift on indexed components per LIFT lease-plus agreement"},
            {"label": "Funding trajectory", "value": "2021-22 c. £2.0M → 2023-24 c. £2.18M → 2024-25 £2.287M — RPI-linked uplift on indexed soft-FM components"},
            {"label": "Delivery body", "value": "LIFT Co (SPV) + LIFT FM contractor + trust E&F oversight + Community Health Partnerships (HMG holding co for LIFT)"},
            {"label": "Policy owner", "value": "DHSC + HM Treasury PFI/LIFT guidance + NHSE Provider Finance + Nottingham & Nottinghamshire ICB"},
            {"label": "Evaluation evidence", "value": "NAO PFI 2018 + PFI hand-back report 2020; PAC PFI hearings; NAO New Hospital Programme 2023; Trust ARA disclosure"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-LIFT community estate baseline · Successor: LIFT hand-back + Tomorrow's NUH (post-NHP Reset) reconfiguration"}
        ],
        "notes": "NUH's PFI / LIFT line is unusually small for a large tertiary trust because the mainstream acute estate (QMC, City Hospital, Nottingham Children's Hospital) is publicly owned rather than PFI — the £2.287M figure reflects a residual LIFT (Local Improvement Finance Trust) community-clinic/outpatient-extension concession indexed to RPI on soft-FM components. NUH sits in the New Hospital Programme cohort with the Tomorrow's NUH whole-site reconfiguration deferred under the January 2025 NHP Reset (publication May 2025), but the LIFT obligation runs independently of the deferred capital build. NUH was also subject to the Donna Ockenden review of maternity services with an Independent Senior Midwifery Advisor remit ongoing — separate from the PFI/LIFT line but shaping the broader institutional context.",
        "sources": [
            {"publisher": "Nottingham University Hospitals NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.nuh.nhs.uk/annual-report"},
            {"publisher": "National Audit Office", "title": "PFI and PF2 (HC 718, 2018)", "url": "https://www.nao.org.uk/reports/pfi-and-pf2/"},
            {"publisher": "National Audit Office", "title": "New Hospital Programme", "url": "https://www.nao.org.uk/reports/new-hospital-programme/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 7 — Leases and service concessions)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Community Health Partnerships", "title": "About LIFT — NHS Local Improvement Finance Trust", "url": "https://www.communityhealthpartnerships.co.uk/"}
        ],
        "related": ["Nottingham University Hospitals NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "PFI / LIFT charges — Sherwood Forest Hospitals NHS Foundation Trust", "PFI / LIFT charges — Worcestershire Acute Hospitals NHS Trust", "Department of Health and Social Care"]
    },
    "Transport (business + patient) — Doncaster and Bassetlaw Teaching Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "Doncaster and Bassetlaw Teaching Hospitals NHS Foundation Trust"}],
        "description": "DBTH's £2.280M transport line covers business mileage (AfC Section 17 + AMAP), pool-fleet IFRS 16 lease costs, NEPTS contract pass-through and patient travel reimbursements across the Doncaster Royal Infirmary, Bassetlaw Hospital (Worksop), Montagu Hospital (Mexborough) and Retford Hospital community footprint. Inter-site transfers between the Doncaster and Bassetlaw EDs — straddling the South Yorkshire / Nottinghamshire ICS border — generate distinctive volume. NEPTS is commissioned through the South Yorkshire ICS lead-commissioner.",
        "beneficiaries": "c. 6,500 WTE staff serving a c. 420,000 Doncaster + Bassetlaw + North Notts catchment; c. 175,000 ED attendances/yr (DRI ED + Bassetlaw ED combined); c. 95,000 admissions/yr; cross-ICS-border footprint (South Yorkshire and Nottinghamshire ICBs) drives the inter-site patient-flow profile.",
        "legal_basis": "NHS Act 2006 — NHSE Patient Transport Services Eligibility Criteria 2021 — Agenda for Change Section 17 (business mileage) — HMRC AMAP rates — IFRS 16 Leases (pool fleet) — DHSC Group Accounting Manual 2024-25 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£2.280M"},
            {"label": "Trust scale", "value": "Doncaster Royal Infirmary + Bassetlaw Hospital (Worksop) + Montagu Hospital (Mexborough) + Retford Hospital; c. 6,500 WTE"},
            {"label": "Cross-ICS-border footprint", "value": "DRI in South Yorkshire ICS; Bassetlaw in Nottingham & Nottinghamshire ICS — twin-ED inter-site transfers cross ICB boundary"},
            {"label": "NEPTS commissioning", "value": "South Yorkshire ICS lead-commissioner NEPTS contract (DRI); Bassetlaw NEPTS via Notts ICS arrangements; eligibility per NHSE 2021 criteria"},
            {"label": "Composition", "value": "Business mileage (AfC S17 + AMAP 45p/25p frozen since 2011) + pool-fleet IFRS 16 leases + NEPTS pass-through + patient travel reimbursements"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove cancellation rebooking + agency travel claims"},
            {"label": "April 2025 NIC + fuel CPI", "value": "Indirect via NEPTS contractor pass-through + diesel CPI feed forward unit-cost pressure"},
            {"label": "Funding trajectory", "value": "2021-22 c. £1.85M → 2023-24 c. £2.1M → 2024-25 £2.280M — fuel CPI + NEPTS contract uplift + activity recovery"},
            {"label": "Delivery body", "value": "Trust E&F + outsourced NEPTS providers (SY ICS + Notts ICS) + pool-fleet leasing partner + Trust HR (mileage)"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + NHSE Urgent and Emergency Care (NEPTS) + South Yorkshire ICB + Nottingham & Nottinghamshire ICB + DHSC"},
            {"label": "Evaluation evidence", "value": "NAO NEPTS 2019; CQC RP5 inspections; NHSE NEPTS Eligibility Review 2021; Trust ARA 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-ICS CCG-commissioned NEPTS contracts · Successor: ICS-collaborative NEPTS retender + cross-ICB protocol harmonisation"}
        ],
        "notes": "DBTH's transport line is shaped by the trust's distinctive cross-ICS-border footprint — DRI in South Yorkshire and Bassetlaw Hospital in Nottinghamshire mean inter-site patient transfers cross both an ICB boundary and a county boundary, with NEPTS commissioning split between two ICS lead-commissioners (South Yorkshire and Nottingham & Nottinghamshire). The HMRC AMAP-rate freeze at 45p/mile since 2011 sustains internal-rate dispute pressure and industrial action 2023-24 drove cancellation-rebooking journeys and agency travel claims. Diesel CPI and the April 2025 NIC step-up feed forward via NEPTS contractor pass-through. Cross-ICB protocol harmonisation is the medium-term lever shaping NEPTS retender pricing.",
        "sources": [
            {"publisher": "Doncaster and Bassetlaw Teaching Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.dbth.nhs.uk/about-us/publications/"},
            {"publisher": "NHS England", "title": "Non-Emergency Patient Transport Services — National Framework + Eligibility Criteria 2021", "url": "https://www.england.nhs.uk/publication/non-emergency-patient-transport-services-nepts/"},
            {"publisher": "National Audit Office", "title": "NHS England's management of the primary care support services contract with Capita", "url": "https://www.nao.org.uk/reports/nhs-englands-management-of-the-primary-care-support-services-contract-with-capita/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Doncaster and Bassetlaw Teaching Hospitals provider profile (RP5)", "url": "https://www.cqc.org.uk/provider/RP5"}
        ],
        "related": ["Doncaster and Bassetlaw Teaching Hospitals NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Transport (business + patient) — University Hospitals Coventry And Warwickshire NHS Trust", "Transport (business + patient) — Bedfordshire Hospitals NHS Foundation Trust", "NHS England"]
    },
    "PFI / LIFT charges — Gloucestershire Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "PFI / LIFT charges", "parent": "Gloucestershire Hospitals NHS Foundation Trust"}],
        "description": "Gloucestershire Hospitals' £2.259M PFI / LIFT charge covers the unitary-charge pass-through on a smaller LIFT-vehicle community / outpatient extension concession within the Gloucestershire estate (Gloucestershire Royal Hospital, Cheltenham General Hospital). The bulk of the trust's main acute estate is publicly owned — the £2.259M figure reflects the residual LIFT element rather than a major hospital PFI. Indexed soft-FM components and lifecycle hard-FM cycles drive year-on-year movement.",
        "beneficiaries": "c. 8,000 WTE staff serving a c. 670,000 Gloucestershire catchment (Gloucester, Cheltenham, Stroud, Forest of Dean, Cotswolds); c. 145,000 ED attendances/yr (Gloucestershire Royal ED + Cheltenham General Type-3 minor-injuries unit); c. 90,000 admissions/yr; LIFT estate covers community/outpatient extension premises supporting the wider acute footprint.",
        "legal_basis": "IFRIC 12 Service Concession Arrangements — IFRS 16 Leases (post-2022 transition for service-concession components) — DHSC Group Accounting Manual 2024-25 ch.7 — Private Finance Initiative / NHS LIFT guidance (HM Treasury) — NHS Act 2006 — Health and Care Act 2022",
        "key_stats": [
            {"label": "PFI / LIFT charges 2024-25", "value": "£2.259M"},
            {"label": "Trust scale", "value": "Gloucestershire Royal Hospital + Cheltenham General Hospital + community LIFT footprint; c. 8,000 WTE"},
            {"label": "LIFT vehicle", "value": "Gloucestershire LIFT-style community-clinic concession — far smaller than the trust's mainstream publicly-owned acute estate"},
            {"label": "Cheltenham General reconfiguration", "value": "Centre for Excellence model post-pandemic; A&E to UTC overnight downgrade 2020+ shaped retained estate footprint"},
            {"label": "Estate covered", "value": "LIFT-vehicle community / outpatient extension premises (modest hereditament base)"},
            {"label": "Unitary charge composition", "value": "Senior debt service + lifecycle hard-FM + indexed soft-FM (cleaning, security, minor maintenance)"},
            {"label": "Indexation mechanism", "value": "RPI-linked annual uplift on indexed components per LIFT lease-plus agreement"},
            {"label": "Funding trajectory", "value": "2021-22 c. £2.0M → 2023-24 c. £2.15M → 2024-25 £2.259M — RPI-linked uplift on indexed soft-FM components"},
            {"label": "Delivery body", "value": "LIFT Co (SPV) + LIFT FM contractor + trust E&F oversight + Community Health Partnerships (HMG holding co for LIFT)"},
            {"label": "Policy owner", "value": "DHSC + HM Treasury PFI/LIFT guidance + NHSE Provider Finance + Gloucestershire ICB"},
            {"label": "Evaluation evidence", "value": "NAO PFI 2018 + PFI hand-back report 2020; PAC PFI hearings; Trust ARA disclosure; CQC RTE inspections"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-LIFT community estate baseline · Successor: LIFT hand-back + ICS estate-rationalisation"}
        ],
        "notes": "Gloucestershire Hospitals' PFI / LIFT line reflects a residual community-LIFT concession indexed to RPI on soft-FM components rather than a major hospital PFI — the trust's mainstream acute estate (Gloucestershire Royal, Cheltenham General) is publicly owned. The Cheltenham General A&E-to-UTC overnight downgrade introduced from 2020 (Centre for Excellence reconfiguration) reshaped the operational footprint of the public estate but does not directly affect the LIFT line. RPI-linked uplifts on indexed soft-FM components drive cost growth and lifecycle hard-FM cycles produce year-on-year volatility. Community Health Partnerships (HMG holding co) governs LIFT-Co stewardship; ICS estate-rationalisation is the medium-term lever.",
        "sources": [
            {"publisher": "Gloucestershire Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.gloshospitals.nhs.uk/about-us/publications/"},
            {"publisher": "National Audit Office", "title": "PFI and PF2 (HC 718, 2018)", "url": "https://www.nao.org.uk/reports/pfi-and-pf2/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 7 — Leases and service concessions)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Community Health Partnerships", "title": "About LIFT — NHS Local Improvement Finance Trust", "url": "https://www.communityhealthpartnerships.co.uk/"},
            {"publisher": "Care Quality Commission", "title": "Gloucestershire Hospitals provider profile (RTE)", "url": "https://www.cqc.org.uk/provider/RTE"}
        ],
        "related": ["Gloucestershire Hospitals NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "PFI / LIFT charges — Nottingham University Hospitals NHS Trust", "PFI / LIFT charges — Sherwood Forest Hospitals NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Lease expenditure — Lancashire Teaching Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Lease expenditure", "parent": "Lancashire Teaching Hospitals NHS Foundation Trust"}],
        "description": "LTHTR's £2.258M lease expenditure line covers IFRS 16 right-of-use depreciation and interest charges on property, equipment and pool-fleet leases across the Royal Preston Hospital and Chorley & South Ribble Hospital footprint. The trust hosts the Lancashire and South Cumbria Major Trauma Centre, Lancashire and South Cumbria Specialised Services for neurosciences and a regional vascular service at Royal Preston, with Chorley A&E having seen recurring opening-hour reductions since 2016 — driving an evolving estate-lease profile.",
        "beneficiaries": "c. 8,000 WTE staff serving a c. 1.5M Lancashire and South Cumbria tertiary catchment (Preston, Chorley, South Ribble) plus regional referrals; c. 175,000 ED attendances/yr (Royal Preston ED + Chorley UTC/A&E); c. 95,000 admissions/yr; Royal Preston is the Lancashire and South Cumbria Major Trauma Centre and regional neurosciences hub.",
        "legal_basis": "IFRS 16 Leases — DHSC Group Accounting Manual 2024-25 ch.7 — Landlord and Tenant Act 1954 (security of tenure) — NHS Act 2006 — Health and Care Act 2022 — NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "Lease expenditure 2024-25", "value": "£2.258M"},
            {"label": "Trust scale", "value": "Royal Preston Hospital + Chorley and South Ribble Hospital; c. 8,000 WTE"},
            {"label": "Tertiary specialty", "value": "Lancashire and South Cumbria Major Trauma Centre + neurosciences + regional vascular at Royal Preston — specialist-equipment leases layered into the line"},
            {"label": "Chorley A&E downgrade history", "value": "Chorley A&E temporarily downgraded to UTC 2016 (medical staffing); part-time A&E reopening cycles since — shapes Chorley site lease utilisation"},
            {"label": "IFRS 16 transition", "value": "DHSC GAM 2022 IFRS 16 transition brought operating-lease commitments on-balance-sheet → right-of-use asset depreciation + interest charge structure"},
            {"label": "Composition", "value": "Right-of-use depreciation (operating-lease classification under IAS 17 → IFRS 16) + lease-liability interest + low-value + short-term lease expense"},
            {"label": "NHSPS / commercial landlord exposure", "value": "Mix of NHS Property Services tenancies (community clinics) and commercial landlords; pool-fleet leases for community + estates teams"},
            {"label": "Pool-fleet IFRS 16", "value": "Right-of-use depreciation on leased pool-vehicle fleet for AHPs + community + facilities teams"},
            {"label": "Funding trajectory", "value": "2021-22 first-full IFRS 16 year c. £1.85M → 2023-24 c. £2.1M → 2024-25 £2.258M"},
            {"label": "Delivery body", "value": "Trust E&F + Finance + NHSPS landlord + commercial landlords + LSC ICB Procurement vehicle-lease frameworks"},
            {"label": "Policy owner", "value": "DHSC (GAM ch.7) + NHSE Provider Finance + Lancashire and South Cumbria ICB"},
            {"label": "Evaluation evidence", "value": "Trust ARA disclosure of right-of-use assets + lease liabilities; CQC RXN inspections; NAO IFRS 16 transition review"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-IFRS 16 operating-lease commitments off-balance-sheet · Successor: LSC ICS estate-rationalisation + community-clinic lease consolidation"}
        ],
        "notes": "LTHTR's lease line is shaped by the trust's tertiary regional role across Lancashire and South Cumbria — Major Trauma Centre and neurosciences specialist-equipment leases at Royal Preston layer onto routine property and pool-fleet IFRS 16 right-of-use assets. The Chorley A&E temporary downgrade in 2016 (medical staffing crisis) and successive part-time A&E reopening cycles since have shaped the operational utilisation profile of the Chorley site lease estate. The DHSC GAM 2022 IFRS 16 transition consolidated previously off-balance-sheet operating-lease commitments into the right-of-use asset and interest-cost structure. Lancashire and South Cumbria ICS estate-rationalisation is the medium-term lever shaping community-clinic lease consolidation.",
        "sources": [
            {"publisher": "Lancashire Teaching Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.lancsteachinghospitals.nhs.uk/our-publications"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 7 — Leases and service concessions)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS Property Services", "title": "Annual Report 2023-24", "url": "https://www.property.nhs.uk/about/annual-reports/"},
            {"publisher": "Care Quality Commission", "title": "Lancashire Teaching Hospitals provider profile (RXN)", "url": "https://www.cqc.org.uk/provider/RXN"},
            {"publisher": "National Audit Office", "title": "Implementing IFRS 16 across government", "url": "https://www.nao.org.uk/insights/implementing-ifrs-16-leases-across-government/"}
        ],
        "related": ["Lancashire Teaching Hospitals NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Lease expenditure — Northern Care Alliance NHS Foundation Trust", "NHS Property Services", "Department of Health and Social Care"]
    },
    "Business rates — Hampshire Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "Hampshire Hospitals NHS Foundation Trust"}],
        "description": "HHFT's £2.255M business-rates line covers non-domestic rates on the Royal Hampshire County Hospital Winchester, Basingstoke and North Hampshire Hospital and Andover War Memorial Hospital sites. Hereditaments are assessed by the Valuation Office Agency on the 2023 Rating List with billing handled by Winchester City Council, Basingstoke and Deane Borough Council and Test Valley Borough Council respectively. NHS trusts pay the full multiplier with no charitable 80% relief — a tri-site footprint with three billing authorities makes for a particularly fragmented rates ledger.",
        "beneficiaries": "c. 5,500 WTE staff serving a c. 600,000 north and mid Hampshire catchment (Winchester, Basingstoke, Andover, Alton, Whitchurch); c. 130,000 ED attendances/yr (RHCH ED + Basingstoke ED + Andover MIU); c. 75,000 admissions/yr; tri-site DGH model with cross-site speciality networks.",
        "legal_basis": "Local Government Finance Act 1988 (Schedule 6) — Non-Domestic Rating (Multipliers and Private Finance) Act 2024 — Non-Domestic Rating Act 2023 — DHSC Group Accounting Manual 2024-25 — NHS Act 2006 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£2.255M"},
            {"label": "Trust scale", "value": "Royal Hampshire County Hospital (Winchester) + Basingstoke and North Hampshire Hospital + Andover War Memorial Hospital; c. 5,500 WTE"},
            {"label": "Billing authorities", "value": "Winchester City Council (RHCH) + Basingstoke and Deane Borough Council (Basingstoke) + Test Valley Borough Council (Andover)"},
            {"label": "Tri-site footprint", "value": "Three separate hereditaments across three billing authorities — fragmented rates ledger and three sets of rateable-value appeal cycles"},
            {"label": "NHP / hospital reconfiguration context", "value": "HHFT successfully pitched into NHP Wave 2 considerations for new hospital build replacing Basingstoke; deferred under Jan 2025 NHP Reset — rates ledger continues unchanged in interim"},
            {"label": "2023 revaluation", "value": "VOA 2023 revaluation (effective 1 Apr 2023) re-set rateable values from 2017 list — transitional uplift on Hampshire DGH hereditaments"},
            {"label": "Multiplier 2024-25", "value": "Standard non-domestic multiplier 54.6p (England, 2024-25); NHS pays full rate (no charitable relief); NDR 2024 Act splits multipliers"},
            {"label": "NDR 2024 Act context", "value": "Non-Domestic Rating (Multipliers and Private Finance) Act 2024 — multiplier-split + anti-avoidance reform"},
            {"label": "Funding trajectory", "value": "2021-22 c. £1.95M → 2023-24 (post-revaluation) c. £2.15M → 2024-25 £2.255M — multiplier + transitional uplift"},
            {"label": "Delivery body", "value": "Trust E&F (rates appeals) + Valuation Office Agency + Winchester CC + Basingstoke and Deane BC + Test Valley BC"},
            {"label": "Policy owner", "value": "MHCLG (NDR policy) + HM Treasury + DHSC + NHSE Provider Finance + Hampshire and Isle of Wight ICB"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2017 rating list baseline · Successor: 2026 revaluation cycle + post-NHP Reset Basingstoke replacement scheme review"}
        ],
        "notes": "HHFT's business-rates line is shaped by the trust's tri-site DGH model with three separate hereditaments across three billing authorities (Winchester CC, Basingstoke and Deane BC, Test Valley BC) — a more fragmented rates ledger than peer single-site trusts. The 2023 VOA revaluation lifted rateable values across Hampshire DGH estate with transitional uplift cycles still propagating. NHS trusts cannot claim charitable 80% relief, so the full 54.6p standard multiplier applies. HHFT pitched into the New Hospital Programme for a Basingstoke replacement scheme; the project was deferred under the January 2025 NHP Reset (publication May 2025), meaning the rates ledger continues unchanged on the existing 1970s-era Basingstoke building hereditament for the medium term.",
        "sources": [
            {"publisher": "Hampshire Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.hampshirehospitals.nhs.uk/about-us/our-publications/"},
            {"publisher": "Valuation Office Agency", "title": "2023 Rating List", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "Ministry of Housing, Communities and Local Government", "title": "Non-Domestic Rating Act 2023 + Multipliers and Private Finance Act 2024", "url": "https://www.gov.uk/government/collections/business-rates"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Hampshire Hospitals provider profile (RN5)", "url": "https://www.cqc.org.uk/provider/RN5"}
        ],
        "related": ["Hampshire Hospitals NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Business rates — The Royal Wolverhampton NHS Trust", "Business rates — Whittington Health NHS Trust", "Valuation Office Agency"]
    },
    "Transport (business + patient) — Northern Care Alliance NHS Foundation Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "Northern Care Alliance NHS Foundation Trust"}],
        "description": "NCA's £2.235M transport line covers business mileage (AfC Section 17 + AMAP), pool-fleet IFRS 16 lease costs, NEPTS contract pass-through and patient travel reimbursements across Salford Royal, Royal Oldham, Fairfield General Bury and Rochdale Infirmary plus the integrated community estate. The Manchester Centre for Clinical Neurosciences at Salford Royal generates substantial inter-hospital tertiary transfer demand. NEPTS is commissioned through the NHS Greater Manchester ICS lead-commissioner.",
        "beneficiaries": "c. 20,000 WTE staff serving a c. 1.0M northern Greater Manchester catchment (Salford, Bury, Oldham, Rochdale) plus tertiary referrals; c. 380,000 ED attendances/yr (Salford Royal + Royal Oldham + Fairfield combined); c. 165,000 admissions/yr; Salford Royal hosts the Manchester Centre for Clinical Neurosciences.",
        "legal_basis": "NHS Act 2006 — NHSE Patient Transport Services Eligibility Criteria 2021 — Agenda for Change Section 17 (business mileage) — HMRC AMAP rates — IFRS 16 Leases (pool fleet) — DHSC Group Accounting Manual 2024-25 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£2.235M"},
            {"label": "Trust scale", "value": "Salford Royal + Royal Oldham + Fairfield General Bury + Rochdale Infirmary + community estate; c. 20,000 WTE"},
            {"label": "Tertiary specialty", "value": "Manchester Centre for Clinical Neurosciences at Salford Royal — high inter-hospital tertiary transfer demand"},
            {"label": "Post-PAHT-merger context", "value": "Oct 2021 NCA-as-FT formation absorbed dissolved Pennine Acute Hospitals Trust — driving cross-site mileage reorganisation through 2022-24"},
            {"label": "NEPTS commissioning", "value": "NHS Greater Manchester ICS lead-commissioner NEPTS contract; eligibility per NHSE 2021 criteria"},
            {"label": "Composition", "value": "Business mileage (AfC S17 + AMAP 45p/25p frozen since 2011) + pool-fleet IFRS 16 leases + NEPTS pass-through + patient travel reimbursements"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove cancellation rebooking + agency travel claims"},
            {"label": "April 2025 NIC + fuel CPI", "value": "Indirect via NEPTS contractor pass-through + diesel CPI feed forward unit-cost pressure"},
            {"label": "Funding trajectory", "value": "2021-22 (post-merger) c. £1.85M → 2023-24 c. £2.05M → 2024-25 £2.235M — fuel CPI + NEPTS contract uplift + activity recovery"},
            {"label": "Delivery body", "value": "Trust E&F + outsourced NEPTS provider (NHS GM ICS lead-commissioner) + pool-fleet leasing partner + Trust HR (mileage)"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + NHSE Urgent and Emergency Care (NEPTS) + NHS Greater Manchester ICB + DHSC"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-Oct 2021 separate Salford Royal FT + PAHT mileage ledgers · Successor: post-merger NCA consolidated ledger + GM ICS NEPTS retender"}
        ],
        "notes": "NCA's transport line is shaped by the Oct 2021 formation of Northern Care Alliance as an NHS FT — bringing the dissolved Pennine Acute Hospitals Trust's four-site footprint (Salford Royal + Royal Oldham + Fairfield Bury + Rochdale) under a single trust ledger drove cross-site mileage reorganisation through 2022-24. Manchester Centre for Clinical Neurosciences tertiary referrals at Salford Royal generate inter-hospital transfer volume layered onto routine four-site business mileage. NHS Greater Manchester ICS lead-commissioner NEPTS contract retender is the medium-term lever. Industrial action 2023-24 drove cancellation-rebooking journeys; HMRC AMAP-rate freeze at 45p/mile since 2011 sustains internal-rate dispute pressure; diesel CPI feeds forward via NEPTS pass-through.",
        "sources": [
            {"publisher": "Northern Care Alliance NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.northerncarealliance.nhs.uk/about-us/publications"},
            {"publisher": "NHS England", "title": "Non-Emergency Patient Transport Services — National Framework + Eligibility Criteria 2021", "url": "https://www.england.nhs.uk/publication/non-emergency-patient-transport-services-nepts/"},
            {"publisher": "National Audit Office", "title": "NHS England's management of the primary care support services contract with Capita", "url": "https://www.nao.org.uk/reports/nhs-englands-management-of-the-primary-care-support-services-contract-with-capita/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Northern Care Alliance provider profile (RM3)", "url": "https://www.cqc.org.uk/provider/RM3"}
        ],
        "related": ["Northern Care Alliance NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Lease expenditure — Northern Care Alliance NHS Foundation Trust", "Transport (business + patient) — Doncaster and Bassetlaw Teaching Hospitals NHS Foundation Trust", "NHS England"]
    },
    "Amortisation — East Suffolk and North Essex NHS Foundation Trust": {
        "aliases": [{"name": "Amortisation", "parent": "East Suffolk and North Essex NHS Foundation Trust"}],
        "description": "ESNEFT's £2.232M amortisation line covers the systematic write-down of intangible assets — capitalised software, EPR licences, internally-developed clinical applications and licensed IP — under IAS 38 across the Ipswich Hospital, Colchester Hospital, Aldeburgh, Felixstowe, Bluebird Lodge and Clacton community footprint. The trust formed July 2018 from the merger of Ipswich Hospital NHS Trust + Colchester Hospital University NHS FT, integrating two heterogeneous clinical-system estates and prompting sustained EPR/digital investment under NHSE's Frontline Digitisation programme.",
        "beneficiaries": "c. 11,000 WTE staff serving a c. 1.0M East Suffolk and North Essex catchment (Ipswich, Colchester, Felixstowe, Clacton); c. 240,000 ED attendances/yr (Ipswich ED + Colchester ED combined); c. 130,000 admissions/yr; integrated post-merger 2018 footprint with substantial community-services arm benefits from amortising digital infrastructure.",
        "legal_basis": "IAS 38 Intangible Assets — DHSC Group Accounting Manual 2024-25 (chapter 5 — Intangibles) — IFRIC SaaS configuration agenda decisions — NHS Act 2006 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£2.232M"},
            {"label": "Trust scale", "value": "Ipswich Hospital + Colchester Hospital + Aldeburgh + Felixstowe + Clacton + Bluebird Lodge community footprint; c. 11,000 WTE"},
            {"label": "Composition", "value": "Capitalised software + EPR licences + internally-developed clinical applications + licensed IP"},
            {"label": "Post-merger 2018 context", "value": "ESNEFT formed Jul 2018 from Ipswich Hospital NHS Trust + Colchester Hospital University NHS FT merger — integrated heterogeneous EPR/PAS estate driving amortising digital investment"},
            {"label": "EPR / Frontline Digitisation", "value": "ESNEFT Frontline Digitisation track — capitalised EPR build amortising over assessed UEL (5-10 years)"},
            {"label": "Useful economic life", "value": "Software 3-5 years; EPR / clinical-system 5-10 years per DHSC GAM ch.5 + IAS 38 review"},
            {"label": "IFRIC SaaS agenda decision", "value": "2021 IFRIC agenda decision on SaaS configuration costs — restricts capitalisation; some EPR programme spend now opex"},
            {"label": "Funding trajectory", "value": "2021-22 c. £1.85M → 2023-24 c. £2.1M → 2024-25 £2.232M — Frontline Digitisation amortisation cycle ramp + post-merger integration capitalisation"},
            {"label": "Delivery body", "value": "Trust IT + Finance (capitalisation) + EPR vendor + NHSE Frontline Digitisation programme"},
            {"label": "Policy owner", "value": "DHSC + NHSE Transformation Directorate + NHSE Provider Finance + Suffolk and North East Essex ICB"},
            {"label": "Evaluation evidence", "value": "NAO Digital transformation in NHS 2020; DHSC GAM ch.5; Trust ARA 2023-24; CQC RDE inspections"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2018 separate Ipswich + Colchester intangibles ledgers · Successor: full EPR-go-live amortisation peak under SNEE ICS"}
        ],
        "notes": "ESNEFT's amortisation line tracks intangible-asset stock through the post-merger integration period — the July 2018 formation of the trust from Ipswich Hospital NHS Trust + Colchester Hospital University NHS FT brought together two heterogeneous clinical-system estates, and the consequent EPR/PAS harmonisation programme has been a sustained driver of capitalised intangibles amortising under IAS 38. Frontline Digitisation EPR build amortises over a 5-10 year assessed useful-economic-life per DHSC GAM ch.5. The 2021 IFRIC SaaS agenda decision restricts SaaS configuration capitalisation, pushing some build spend into opex. Suffolk and North East Essex ICB allocation governs the medium-term frame for further digital capitalisation cycles.",
        "sources": [
            {"publisher": "East Suffolk and North Essex NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.esneft.nhs.uk/about-us/publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 5 — Intangibles)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/connecting-health-and-care/frontline-digitisation/"},
            {"publisher": "National Audit Office", "title": "Digital transformation in the NHS", "url": "https://www.nao.org.uk/reports/the-digital-transformation-in-the-nhs/"},
            {"publisher": "Care Quality Commission", "title": "East Suffolk and North Essex NHS FT provider profile (RDE)", "url": "https://www.cqc.org.uk/provider/RDE"}
        ],
        "related": ["East Suffolk and North Essex NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Amortisation — The Shrewsbury and Telford Hospital NHS Trust", "Amortisation — Royal Surrey NHS Foundation Trust", "NHS England"]
    },
    "Amortisation — Royal Surrey NHS Foundation Trust": {
        "aliases": [{"name": "Amortisation", "parent": "Royal Surrey NHS Foundation Trust"}],
        "description": "Royal Surrey's £2.227M amortisation line covers the systematic write-down of intangible assets — capitalised software, EPR licences, internally-developed clinical applications and licensed IP — under IAS 38 across the Royal Surrey County Hospital Guildford footprint. The trust hosts the South West Sector Cancer Centre serving Surrey, Sussex and Hampshire, with substantial radiotherapy and PET-CT investment driving capitalised intangibles. Royal Surrey runs a joint integrated-care arrangement with CSH Surrey for community services in Guildford and Waverley.",
        "beneficiaries": "c. 4,500 WTE staff serving a c. 320,000 Guildford and Waverley catchment plus regional cancer-centre referrals from across South West London + Surrey + parts of Sussex and Hampshire; c. 90,000 ED attendances/yr at RSCH ED; c. 55,000 admissions/yr; cancer-centre tertiary specialism drives intangibles capitalisation profile.",
        "legal_basis": "IAS 38 Intangible Assets — DHSC Group Accounting Manual 2024-25 (chapter 5 — Intangibles) — IFRIC SaaS configuration agenda decisions — NHS Act 2006 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£2.227M"},
            {"label": "Trust scale", "value": "Royal Surrey County Hospital (Guildford); c. 4,500 WTE"},
            {"label": "Tertiary specialty", "value": "South West Sector Cancer Centre — Surrey + parts of Sussex + Hampshire catchment; PET-CT + radiotherapy capitalisation profile"},
            {"label": "Composition", "value": "Capitalised software + EPR licences + internally-developed clinical applications + licensed IP"},
            {"label": "EPR / Frontline Digitisation", "value": "Royal Surrey Frontline Digitisation track — capitalised EPR build amortising over assessed UEL (5-10 years)"},
            {"label": "Useful economic life", "value": "Software 3-5 years; EPR / clinical-system 5-10 years per DHSC GAM ch.5 + IAS 38 review"},
            {"label": "IFRIC SaaS agenda decision", "value": "2021 IFRIC agenda decision on SaaS configuration costs — restricts capitalisation; some EPR programme spend now opex"},
            {"label": "Cancer-centre digital investment", "value": "Radiotherapy planning systems + PET-CT image-management + oncology EPR modules drive intangibles capitalisation"},
            {"label": "Funding trajectory", "value": "2021-22 c. £1.85M → 2023-24 c. £2.1M → 2024-25 £2.227M — Frontline Digitisation amortisation cycle ramp + cancer-system capitalisation"},
            {"label": "Delivery body", "value": "Trust IT + Finance (capitalisation) + EPR vendor + NHSE Frontline Digitisation programme + radiotherapy planning-system vendor"},
            {"label": "Policy owner", "value": "DHSC + NHSE Transformation Directorate + NHSE Provider Finance + Surrey Heartlands ICB"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-Frontline Digitisation legacy clinical-system amortisation tail · Successor: full EPR-go-live amortisation peak + cancer-centre capital programme"}
        ],
        "notes": "Royal Surrey's amortisation line is shaped by its tertiary cancer-centre specialism — the South West Sector Cancer Centre serves Surrey, Sussex and parts of Hampshire and drives a distinctive intangibles capitalisation profile through radiotherapy planning systems, PET-CT image-management software and oncology-specific EPR modules. Frontline Digitisation EPR build amortises over a 5-10 year assessed useful-economic-life per DHSC GAM ch.5 and IAS 38. The 2021 IFRIC SaaS agenda decision restricts SaaS configuration capitalisation, pushing some build spend into opex. Surrey Heartlands ICB allocation governs the medium-term frame; the joint integrated-care arrangement with CSH Surrey (community services) shapes the back-office digital footprint.",
        "sources": [
            {"publisher": "Royal Surrey NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.royalsurrey.nhs.uk/about/our-publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 5 — Intangibles)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/connecting-health-and-care/frontline-digitisation/"},
            {"publisher": "National Audit Office", "title": "Digital transformation in the NHS", "url": "https://www.nao.org.uk/reports/the-digital-transformation-in-the-nhs/"},
            {"publisher": "Care Quality Commission", "title": "Royal Surrey NHS FT provider profile (RA2)", "url": "https://www.cqc.org.uk/provider/RA2"}
        ],
        "related": ["Royal Surrey NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Amortisation — East Suffolk and North Essex NHS Foundation Trust", "Amortisation — The Shrewsbury and Telford Hospital NHS Trust", "NHS England"]
    },
    "Business rates — Whittington Health NHS Trust": {
        "aliases": [{"name": "Business rates", "parent": "Whittington Health NHS Trust"}],
        "description": "Whittington Health's £2.227M business-rates line covers non-domestic rates on the Whittington Hospital Archway main site (a London integrated-care trust providing both acute and community services across Islington and Haringey) plus a large community-clinic and health-centre estate across the two boroughs. Hereditaments are assessed by the Valuation Office Agency on the 2023 Rating List with billing handled by the London Borough of Islington and the London Borough of Haringey. NHS trusts pay the full multiplier with no charitable 80% relief.",
        "beneficiaries": "c. 4,500 WTE staff serving a c. 500,000 Islington + Haringey integrated-care catchment; c. 75,000 ED attendances/yr at Whittington ED; c. 35,000 admissions/yr; integrated acute + community model with substantial community-clinic estate (c. 30 sites across Islington + Haringey) feeding the rates ledger.",
        "legal_basis": "Local Government Finance Act 1988 (Schedule 6) — Non-Domestic Rating (Multipliers and Private Finance) Act 2024 — Non-Domestic Rating Act 2023 — DHSC Group Accounting Manual 2024-25 — NHS Act 2006 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£2.227M"},
            {"label": "Trust scale", "value": "Whittington Hospital (Archway, c. 280 beds) + community-clinic estate across Islington + Haringey; c. 4,500 WTE"},
            {"label": "Integrated-care model", "value": "Acute + community trust — c. 30 community-clinic / health-centre hereditaments across Islington + Haringey broaden rates footprint above pure-acute peers"},
            {"label": "Billing authorities", "value": "London Borough of Islington (Whittington Hospital + Islington community sites) + London Borough of Haringey (Haringey community sites)"},
            {"label": "London VOA premium", "value": "Inner London rateable values significantly above national NHS average — material driver of per-bed rates burden"},
            {"label": "2023 revaluation", "value": "VOA 2023 revaluation (effective 1 Apr 2023) re-set rateable values from 2017 list — large transitional uplift on London hereditaments"},
            {"label": "Multiplier 2024-25", "value": "Standard non-domestic multiplier 54.6p (England, 2024-25); NHS pays full rate (no charitable relief); NDR 2024 Act splits multipliers"},
            {"label": "NDR 2024 Act context", "value": "Non-Domestic Rating (Multipliers and Private Finance) Act 2024 — multiplier-split + anti-avoidance reform"},
            {"label": "Funding trajectory", "value": "2021-22 c. £1.95M → 2023-24 (post-revaluation) c. £2.12M → 2024-25 £2.227M — multiplier + transitional uplift"},
            {"label": "Delivery body", "value": "Trust E&F (rates appeals) + Valuation Office Agency + LB Islington + LB Haringey"},
            {"label": "Policy owner", "value": "MHCLG (NDR policy) + HM Treasury + DHSC + NHSE Provider Finance + North Central London ICB"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2017 rating list baseline · Successor: 2026 revaluation cycle + NDR 2024 Act multiplier-split implementation"}
        ],
        "notes": "Whittington Health's business-rates line is shaped by the trust's distinctive integrated-care model — a single statutory trust delivering both acute and community services across Islington and Haringey, with c. 30 community-clinic hereditaments adding to the main Whittington Hospital Archway site to broaden the rates footprint above pure-acute peers. Inner London VOA rateable values run materially above the NHS national average, so the post-2023-revaluation transitional uplift hits Whittington harder than peer DGH trusts. Two billing authorities (LB Islington and LB Haringey) collect; NHS pays full 54.6p standard multiplier with no charitable 80% relief. The NDR 2024 Act multiplier split exposes the main hospital hereditament to higher-multiplier classification in future bills.",
        "sources": [
            {"publisher": "Whittington Health NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.whittington.nhs.uk/default.asp?c=33396"},
            {"publisher": "Valuation Office Agency", "title": "2023 Rating List", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "Ministry of Housing, Communities and Local Government", "title": "Non-Domestic Rating Act 2023 + Multipliers and Private Finance Act 2024", "url": "https://www.gov.uk/government/collections/business-rates"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Whittington Health provider profile (RKE)", "url": "https://www.cqc.org.uk/provider/RKE"}
        ],
        "related": ["Whittington Health NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Business rates — Hampshire Hospitals NHS Foundation Trust", "Business rates — The Leeds Teaching Hospitals NHS Trust", "Valuation Office Agency"]
    },
    "Transport (business + patient) — Wrightington, Wigan and Leigh NHS Foundation Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "Wrightington, Wigan and Leigh NHS Foundation Trust"}],
        "description": "WWL's £2.224M transport line covers business mileage (AfC Section 17 + AMAP), pool-fleet IFRS 16 lease costs, NEPTS contract pass-through and patient travel reimbursements across the Royal Albert Edward Infirmary Wigan, Leigh Infirmary and Wrightington Hospital footprint. Wrightington is internationally renowned as the John Charnley birthplace of modern hip-replacement surgery and the trust's regional orthopaedic centre — driving substantial elective referral travel. NEPTS is commissioned through the NHS Greater Manchester ICS lead-commissioner.",
        "beneficiaries": "c. 5,000 WTE staff serving a c. 320,000 Wigan + Leigh + West Lancashire catchment plus regional orthopaedic referrals to Wrightington; c. 110,000 ED attendances/yr at RAEI ED; c. 60,000 admissions/yr; Wrightington is a regional + national elective orthopaedic referral centre.",
        "legal_basis": "NHS Act 2006 — NHSE Patient Transport Services Eligibility Criteria 2021 — Agenda for Change Section 17 (business mileage) — HMRC AMAP rates — IFRS 16 Leases (pool fleet) — DHSC Group Accounting Manual 2024-25 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£2.224M"},
            {"label": "Trust scale", "value": "Royal Albert Edward Infirmary (Wigan) + Leigh Infirmary + Wrightington Hospital; c. 5,000 WTE"},
            {"label": "Wrightington orthopaedic specialism", "value": "John Charnley birthplace of modern hip-replacement surgery — regional + national elective orthopaedic referral centre, drives elective inbound patient travel"},
            {"label": "NEPTS commissioning", "value": "NHS Greater Manchester ICS lead-commissioner NEPTS contract; eligibility per NHSE 2021 criteria"},
            {"label": "Composition", "value": "Business mileage (AfC S17 + AMAP 45p/25p frozen since 2011) + pool-fleet IFRS 16 leases + NEPTS pass-through + patient travel reimbursements"},
            {"label": "Three-site mileage profile", "value": "Cross-site clinical staffing across RAEI + Leigh + Wrightington drives routine business-mileage volume above single-site DGH peers"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove cancellation rebooking + agency travel claims"},
            {"label": "April 2025 NIC + fuel CPI", "value": "Indirect via NEPTS contractor pass-through + diesel CPI feed forward unit-cost pressure"},
            {"label": "Funding trajectory", "value": "2021-22 c. £1.85M → 2023-24 c. £2.05M → 2024-25 £2.224M — fuel CPI + NEPTS contract uplift + activity recovery"},
            {"label": "Delivery body", "value": "Trust E&F + outsourced NEPTS provider (NHS GM ICS lead-commissioner) + pool-fleet leasing partner + Trust HR (mileage)"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + NHSE Urgent and Emergency Care (NEPTS) + NHS Greater Manchester ICB + DHSC"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-ICS CCG-commissioned NEPTS contract · Successor: ICS-collaborative NEPTS retender + GM elective recovery network volume"}
        ],
        "notes": "WWL's transport line is shaped by Wrightington Hospital's national orthopaedic-centre role — the John Charnley birthplace of modern hip-replacement surgery draws elective patients from across the North West and beyond, generating distinctive inbound patient travel demand alongside routine three-site cross-staffing business mileage between Wigan, Leigh and Wrightington. NHS Greater Manchester ICS lead-commissioner NEPTS contract retender is the medium-term lever, with NHSE 2021 eligibility criteria tightening the patient-paid threshold. Industrial action 2023-24 drove cancellation-rebooking journeys and agency travel claims; HMRC AMAP-rate freeze at 45p/mile since 2011 sustains internal-rate dispute pressure. Diesel CPI and April 2025 NIC step-up feed forward via NEPTS contractor pass-through.",
        "sources": [
            {"publisher": "Wrightington, Wigan and Leigh NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.wwl.nhs.uk/wwl-annual-report"},
            {"publisher": "NHS England", "title": "Non-Emergency Patient Transport Services — National Framework + Eligibility Criteria 2021", "url": "https://www.england.nhs.uk/publication/non-emergency-patient-transport-services-nepts/"},
            {"publisher": "National Audit Office", "title": "NHS England's management of the primary care support services contract with Capita", "url": "https://www.nao.org.uk/reports/nhs-englands-management-of-the-primary-care-support-services-contract-with-capita/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Wrightington, Wigan and Leigh NHS FT provider profile (RRF)", "url": "https://www.cqc.org.uk/provider/RRF"}
        ],
        "related": ["Wrightington, Wigan and Leigh NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Transport (business + patient) — Northern Care Alliance NHS Foundation Trust", "Transport (business + patient) — University Hospitals Coventry And Warwickshire NHS Trust", "NHS England"]
    },
    "Establishment costs — James Paget University Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "James Paget University Hospitals NHS Foundation Trust"}],
        "description": "JPUH's £2.207M establishment costs line covers postage, telephony, mobile-data, printing, stationery, recruitment advertising, subscriptions and minor sundries across the James Paget Hospital Gorleston-on-Sea (Great Yarmouth) main site and outreach community footprint covering Lowestoft, Great Yarmouth and rural North-East Suffolk. JPUH is one of seven RAAC-affected hospitals in the New Hospital Programme cohort with a confirmed full replacement scheme — driving sustained recruitment-advertising and project-comms baseline pressure as the new-build planning runs.",
        "beneficiaries": "c. 4,000 WTE staff serving a c. 230,000 Great Yarmouth + Waveney + East Norfolk catchment; c. 75,000 ED attendances/yr at JPH ED; c. 45,000 admissions/yr; coastal demographic with high rurality + age structure shapes back-office workload and recruitment-advertising spend.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) — IAS 1 Presentation of Financial Statements — NHS Act 2006 — Health and Care Act 2022 — NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£2.207M"},
            {"label": "Trust scale", "value": "James Paget Hospital (Gorleston-on-Sea); c. 4,000 WTE"},
            {"label": "RAAC + NHP context", "value": "JPUH is one of seven hospitals built primarily with RAAC concrete planks — confirmed in NHP for full replacement; new-build planning + comms drive establishment-line pressure"},
            {"label": "NHP Reset Jan 2025", "value": "Wave 1 RAAC-cohort (incl. JPUH) prioritised in Jan 2025 NHP Reset; comms + recruitment-advertising baseline elevated through Reset publication May 2025"},
            {"label": "Composition", "value": "Postage, telephony/mobile, printing, stationery, recruitment advertising, subscriptions, hospitality, minor sundries"},
            {"label": "Industrial action 2023-24", "value": "Junior-doctor 44 days + consultant 10 days strikes drove recruitment-advertising spike + comms costs"},
            {"label": "Coastal recruitment premium", "value": "Coastal market recruitment-advertising spend elevated above national average — drives establishment baseline above peer DGH"},
            {"label": "April 2025 CPI uplift", "value": "Royal Mail + telecoms + advertising CPI feed forward unit-cost pressure"},
            {"label": "Funding trajectory", "value": "2021-22 c. £1.8M → 2023-24 c. £2.05M → 2024-25 £2.207M — sustained CPI + NHP-comms + recruitment uplift"},
            {"label": "Delivery body", "value": "Trust Corporate Services + Procurement + IT + Crown Commercial Service framework (telecoms/postage)"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Norfolk and Waveney ICB + NHP / NHS New Hospital Programme team"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-NHP-confirmation 2019 baseline · Successor: full new-hospital-build scheme + post-build digital-comms shift"}
        ],
        "notes": "JPUH's establishment-costs line reflects a RAAC-hospital trust running in the active New Hospital Programme cohort — the trust is one of seven NHS hospitals built primarily with reinforced autoclaved aerated concrete planks and is confirmed for full replacement under NHP, with the Wave 1 RAAC-cohort prioritised under the January 2025 NHP Reset (publication May 2025). New-build planning, public consultation, recruitment-advertising and project-comms drive sustained establishment-line pressure above peer DGH baseline. Coastal recruitment-market premium (Great Yarmouth / Lowestoft) lifts recruitment-advertising spend further. Industrial action 2023-24 lifted recruitment costs. Royal Mail postage and telecoms CPI feed forward; Norfolk and Waveney ICB allocation governs the medium-term frame.",
        "sources": [
            {"publisher": "James Paget University Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.jpaget.nhs.uk/about-us/our-publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "National Audit Office", "title": "Investigation into RAAC in education and other public sector buildings", "url": "https://www.nao.org.uk/reports/investigation-into-the-effects-of-raac-in-schools/"},
            {"publisher": "DHSC / NHS England", "title": "New Hospital Programme — January 2025 Reset", "url": "https://www.gov.uk/government/news/new-hospital-programme-update"},
            {"publisher": "Care Quality Commission", "title": "James Paget University Hospitals provider profile (RGP)", "url": "https://www.cqc.org.uk/provider/RGP"}
        ],
        "related": ["James Paget University Hospitals NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Establishment costs — Torbay and South Devon NHS Foundation Trust", "Establishment costs — George Eliot Hospital NHS Trust", "DHSC New Hospital Programme"]
    },
    "Establishment costs — George Eliot Hospital NHS Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "George Eliot Hospital NHS Trust"}],
        "description": "George Eliot Hospital's £2.195M establishment costs line covers postage, telephony, mobile-data, printing, stationery, recruitment advertising, subscriptions and minor sundries across the George Eliot Hospital Nuneaton main site and outreach community footprint covering North Warwickshire and the wider Coventry+Warwickshire+Hinckley border. GEH is a small DGH that has explored multiple acquisition / partnership configurations (UHCW, UHB) over the past decade — sustaining a back-office overhead profile shaped by repeated organisational-form reviews and NHSE turnaround intervention.",
        "beneficiaries": "c. 2,500 WTE staff serving a c. 300,000 North Warwickshire + Hinckley + Bosworth catchment; c. 80,000 ED attendances/yr at GEH ED; c. 35,000 admissions/yr; small-DGH cost base with elevated back-office overhead per WTE relative to larger peers.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) — IAS 1 Presentation of Financial Statements — NHS Act 2006 — Health and Care Act 2022 — NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£2.195M"},
            {"label": "Trust scale", "value": "George Eliot Hospital (Nuneaton); c. 2,500 WTE"},
            {"label": "Small-DGH profile", "value": "Smallest acute trust in the West Midlands by income — fixed back-office overhead spread over smaller WTE base lifts establishment ratio per WTE"},
            {"label": "Acquisition / partnership history", "value": "GEH has explored multiple acquisition / partnership routes (UHCW, UHB) over past decade — sustained M&A advisory + comms baseline"},
            {"label": "Composition", "value": "Postage, telephony/mobile, printing, stationery, recruitment advertising, subscriptions, hospitality, minor sundries"},
            {"label": "EPR / Frontline Digitisation", "value": "GEH Frontline Digitisation track drives change-mgmt + training-materials + comms baseline"},
            {"label": "Industrial action 2023-24", "value": "Junior-doctor 44 days + consultant 10 days strikes drove recruitment-advertising spike + comms costs"},
            {"label": "April 2025 CPI uplift", "value": "Royal Mail + telecoms + advertising CPI feed forward unit-cost pressure"},
            {"label": "Funding trajectory", "value": "2021-22 c. £1.8M → 2023-24 c. £2.05M → 2024-25 £2.195M — sustained CPI + NHSE-turnaround comms + recruitment uplift"},
            {"label": "Delivery body", "value": "Trust Corporate Services + Procurement + IT + Crown Commercial Service framework (telecoms/postage)"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Coventry and Warwickshire ICB"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-NHSE-turnaround 2019 baseline · Successor: continued ICS-collaborative back-office consolidation under Coventry & Warwickshire ICB"}
        ],
        "notes": "George Eliot Hospital's establishment-costs line is shaped by the trust's small-DGH structural position — the smallest acute trust in the West Midlands by income, with fixed back-office overhead spread over a smaller WTE base lifts the establishment-cost ratio per WTE relative to larger peers. The trust has explored multiple acquisition / partnership routes over the past decade (with UHCW and UHB at different points) and has had recurring NHSE turnaround / oversight engagement, sustaining an M&A advisory + project-comms baseline above peer DGH. EPR / Frontline Digitisation rollout drives change-management and training-materials spend; industrial action 2023-24 lifted recruitment costs. Royal Mail postage and telecoms CPI feed forward; Coventry and Warwickshire ICB allocation governs the medium-term frame.",
        "sources": [
            {"publisher": "George Eliot Hospital NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.geh.nhs.uk/about-us/our-publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/connecting-health-and-care/frontline-digitisation/"},
            {"publisher": "Care Quality Commission", "title": "George Eliot Hospital provider profile (RLT)", "url": "https://www.cqc.org.uk/provider/RLT"},
            {"publisher": "National Audit Office", "title": "NHS financial sustainability", "url": "https://www.nao.org.uk/reports/nhs-financial-sustainability-2024/"}
        ],
        "related": ["George Eliot Hospital NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Establishment costs — James Paget University Hospitals NHS Foundation Trust", "Establishment costs — Medway NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Business rates — The Leeds Teaching Hospitals NHS Trust": {
        "aliases": [{"name": "Business rates", "parent": "The Leeds Teaching Hospitals NHS Trust"}],
        "description": "LTHT's £2.194M business-rates line covers non-domestic rates on Leeds General Infirmary, St James's University Hospital (Jimmy's), Seacroft Hospital, Wharfedale Hospital and the Chapel Allerton Hospital outpatient site. Hereditaments are assessed by the Valuation Office Agency on the 2023 Rating List with billing handled by Leeds City Council. LTHT is one of England's largest tertiary teaching trusts — host to the Leeds Cancer Centre, Yorkshire Heart Centre, neurosciences and a major academic-medical-centre footprint. NHS trusts pay the full multiplier with no charitable 80% relief.",
        "beneficiaries": "c. 22,000 WTE staff serving a c. 800,000 Leeds catchment plus tertiary referrals from c. 5.5M people across Yorkshire and Humber; c. 250,000 ED attendances/yr (LGI ED + Jimmy's ED combined); c. 240,000 admissions/yr; LTHT is one of England's largest teaching trusts with major-trauma, cancer, cardiac, neurosciences and transplant tertiary specialism.",
        "legal_basis": "Local Government Finance Act 1988 (Schedule 6) — Non-Domestic Rating (Multipliers and Private Finance) Act 2024 — Non-Domestic Rating Act 2023 — DHSC Group Accounting Manual 2024-25 — NHS Act 2006 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£2.194M"},
            {"label": "Trust scale", "value": "Leeds General Infirmary + St James's University Hospital + Seacroft Hospital + Wharfedale Hospital + Chapel Allerton; c. 22,000 WTE"},
            {"label": "Tertiary specialty profile", "value": "Leeds Cancer Centre + Yorkshire Heart Centre + neurosciences + transplantation + Major Trauma Centre — extensive specialty footprint"},
            {"label": "Billing authority", "value": "Leeds City Council (NDR collection); Valuation Office Agency rateable-value assessment"},
            {"label": "Hospitals of the Future / NHP context", "value": "LGI Hospitals of the Future scheme (LGI replacement + Children's Hospital build) is a New Hospital Programme cohort scheme — deferred under Jan 2025 NHP Reset; rates ledger continues unchanged"},
            {"label": "2023 revaluation", "value": "VOA 2023 revaluation (effective 1 Apr 2023) re-set rateable values from 2017 list — large transitional effects on tertiary hereditaments"},
            {"label": "Multiplier 2024-25", "value": "Standard non-domestic multiplier 54.6p (England, 2024-25); NHS pays full rate (no charitable relief); NDR 2024 Act splits multipliers"},
            {"label": "NDR 2024 Act context", "value": "Non-Domestic Rating (Multipliers and Private Finance) Act 2024 — multiplier-split + anti-avoidance reform; tertiary specialty buildings exposed to higher-multiplier classification"},
            {"label": "Funding trajectory", "value": "2021-22 c. £1.9M → 2023-24 (post-revaluation) c. £2.08M → 2024-25 £2.194M — multiplier + transitional uplift; figure modest relative to trust income because Leeds rateable-value market sits below London peers"},
            {"label": "Delivery body", "value": "Trust E&F (rates appeals) + Valuation Office Agency + Leeds City Council"},
            {"label": "Policy owner", "value": "MHCLG (NDR policy) + HM Treasury + DHSC + NHSE Provider Finance + West Yorkshire ICB"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2017 rating list baseline · Successor: 2026 revaluation cycle + post-NHP Reset Hospitals of the Future scheme"}
        ],
        "notes": "LTHT's business-rates line is dominated by the Leeds General Infirmary and St James's University Hospital tertiary footprints — major-trauma, cancer, cardiac, neurosciences and transplant specialism on hereditaments across Leeds — with Leeds City Council as sole billing authority. The figure is modest relative to trust income because Leeds rateable-value market sits below inner-London peers despite the trust being one of England's largest. The Hospitals of the Future scheme (LGI replacement + new Leeds Children's Hospital build) is a New Hospital Programme cohort scheme deferred under the January 2025 NHP Reset (publication May 2025) — meaning the rates ledger continues unchanged on the existing LGI hereditament for the medium term. The NDR 2024 Act multiplier split exposes large tertiary hereditaments to higher-multiplier classification in future bills.",
        "sources": [
            {"publisher": "The Leeds Teaching Hospitals NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.leedsth.nhs.uk/about-us/publications/annual-report/"},
            {"publisher": "Valuation Office Agency", "title": "2023 Rating List", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "Ministry of Housing, Communities and Local Government", "title": "Non-Domestic Rating Act 2023 + Multipliers and Private Finance Act 2024", "url": "https://www.gov.uk/government/collections/business-rates"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "The Leeds Teaching Hospitals provider profile (RR8)", "url": "https://www.cqc.org.uk/provider/RR8"}
        ],
        "related": ["The Leeds Teaching Hospitals NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Business rates — Whittington Health NHS Trust", "Business rates — Hampshire Hospitals NHS Foundation Trust", "Valuation Office Agency"]
    },
    "Establishment costs — Medway NHS Foundation Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "Medway NHS Foundation Trust"}],
        "description": "Medway's £2.175M establishment costs line covers postage, telephony, mobile-data, printing, stationery, recruitment advertising, subscriptions and minor sundries across the Medway Maritime Hospital Gillingham main site. Medway emerged from special-measures + buddied-trust arrangements in the mid-2010s following CQC inadequate ratings — sustaining a back-office overhead profile shaped by improvement-programme comms and recruitment-advertising spend in a Kent labour market with material competition from neighbouring trusts and the M2/M20 commute-pull to London.",
        "beneficiaries": "c. 5,500 WTE staff serving a c. 425,000 Medway Towns + Swale catchment (Gillingham, Chatham, Rochester, Strood, Sittingbourne, Sheerness); c. 145,000 ED attendances/yr at Medway Maritime ED; c. 70,000 admissions/yr; coastal+commuter demographic with Kent labour-market competition shapes back-office workload.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) — IAS 1 Presentation of Financial Statements — NHS Act 2006 — Health and Care Act 2022 — NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£2.175M"},
            {"label": "Trust scale", "value": "Medway Maritime Hospital (Gillingham); c. 5,500 WTE"},
            {"label": "Special-measures + improvement history", "value": "Medway placed in special measures 2013-17 following CQC inadequate ratings; buddying with Guy's and St Thomas' (then GSTT) — sustained improvement-programme comms baseline post-exit"},
            {"label": "Kent labour-market premium", "value": "Kent NHS labour market faces M2/M20 commuter-pull to London hospitals — drives recruitment-advertising spend above national-average baseline"},
            {"label": "Composition", "value": "Postage, telephony/mobile, printing, stationery, recruitment advertising, subscriptions, hospitality, minor sundries"},
            {"label": "EPR / Frontline Digitisation", "value": "Medway Frontline Digitisation track drives change-mgmt + training-materials + comms baseline"},
            {"label": "Industrial action 2023-24", "value": "Junior-doctor 44 days + consultant 10 days strikes drove recruitment-advertising spike + comms costs"},
            {"label": "April 2025 CPI uplift", "value": "Royal Mail + telecoms + advertising CPI feed forward unit-cost pressure"},
            {"label": "Funding trajectory", "value": "2021-22 c. £1.8M → 2023-24 c. £2.0M → 2024-25 £2.175M — sustained CPI + recruitment-advertising uplift"},
            {"label": "Delivery body", "value": "Trust Corporate Services + Procurement + IT + Crown Commercial Service framework (telecoms/postage)"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Kent and Medway ICB"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2013 special-measures baseline · Successor: continued ICS-collaborative back-office consolidation under Kent and Medway ICB"}
        ],
        "notes": "Medway's establishment-costs line carries the legacy of the trust's 2013-17 special-measures period — the trust was placed in special measures following CQC inadequate ratings and was buddied with Guy's and St Thomas' (GSTT), with substantial improvement-programme comms, recruitment-advertising and project-management infrastructure that has continued to shape the post-exit baseline. The Kent labour market faces material M2/M20 commuter-pull to London hospitals offering inner-London weighting, sustaining recruitment-advertising spend above national-average peer DGH. EPR / Frontline Digitisation rollout drives change-management and training-materials spend; industrial action 2023-24 lifted recruitment costs. Royal Mail and telecoms CPI feed forward; Kent and Medway ICB allocation governs the medium-term frame.",
        "sources": [
            {"publisher": "Medway NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.medway.nhs.uk/about-us/our-publications.htm"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Medway NHS Foundation Trust provider profile (RPA)", "url": "https://www.cqc.org.uk/provider/RPA"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/connecting-health-and-care/frontline-digitisation/"},
            {"publisher": "National Audit Office", "title": "NHS financial sustainability", "url": "https://www.nao.org.uk/reports/nhs-financial-sustainability-2024/"}
        ],
        "related": ["Medway NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Establishment costs — George Eliot Hospital NHS Trust", "Establishment costs — James Paget University Hospitals NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Transport (business + patient) — Harrogate and District NHS Foundation Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "Harrogate and District NHS Foundation Trust"}],
        "description": "HDFT's £2.168M transport line covers business mileage (AfC Section 17 + AMAP), pool-fleet IFRS 16 lease costs, NEPTS contract pass-through and patient travel reimbursements across the Harrogate District Hospital acute site plus a wide community / 0-19 children's-services footprint that extends across multiple local authorities (North Yorkshire, Leeds, Bradford, County Durham, Sunderland, Gateshead, Stockton, Middlesbrough, Hartlepool, Darlington and Northumberland). The geographically dispersed children's-services arm is a distinctive driver of business-mileage volume.",
        "beneficiaries": "c. 4,500 WTE staff serving a c. 160,000 Harrogate + Knaresborough + Wetherby + Ripon acute catchment plus a far wider c. 1.0M+ children-and-young-people 0-19 services population across multiple LAs in the North-East and West Yorkshire; c. 65,000 ED attendances/yr at Harrogate ED; c. 35,000 admissions/yr.",
        "legal_basis": "NHS Act 2006 — NHSE Patient Transport Services Eligibility Criteria 2021 — Agenda for Change Section 17 (business mileage) — HMRC AMAP rates — IFRS 16 Leases (pool fleet) — DHSC Group Accounting Manual 2024-25 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£2.168M"},
            {"label": "Trust scale", "value": "Harrogate District Hospital + multi-LA children-and-young-people 0-19 services footprint; c. 4,500 WTE"},
            {"label": "Multi-LA 0-19 services", "value": "Children-and-young-people 0-19 services delivered across North Yorkshire, Leeds, Bradford, County Durham, Sunderland, Gateshead, Stockton, Middlesbrough, Hartlepool, Darlington, Northumberland — drives geographically dispersed business mileage volume"},
            {"label": "NEPTS commissioning", "value": "West Yorkshire ICS lead-commissioner NEPTS contract (Harrogate acute); 0-19 services travel via LA contracts; eligibility per NHSE 2021 criteria"},
            {"label": "Composition", "value": "Business mileage (AfC S17 + AMAP 45p/25p frozen since 2011) + pool-fleet IFRS 16 leases + NEPTS pass-through + patient travel reimbursements"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove cancellation rebooking + agency travel claims"},
            {"label": "April 2025 NIC + fuel CPI", "value": "Indirect via NEPTS contractor pass-through + diesel CPI feed forward unit-cost pressure"},
            {"label": "Funding trajectory", "value": "2021-22 c. £1.8M → 2023-24 c. £2.0M → 2024-25 £2.168M — fuel CPI + NEPTS contract uplift + 0-19 services-mileage growth"},
            {"label": "Delivery body", "value": "Trust E&F + outsourced NEPTS provider (West Yorkshire ICS lead-commissioner) + 0-19 services LA contracts + pool-fleet leasing partner + Trust HR (mileage)"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + NHSE Urgent and Emergency Care (NEPTS) + West Yorkshire ICB + relevant 0-19 commissioning LAs + DHSC"},
            {"label": "Evaluation evidence", "value": "NAO NEPTS 2019; CQC RCD inspections; NHSE NEPTS Eligibility Review 2021; Trust ARA 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-LA-contract 0-19 acquisition + pre-ICS CCG-NEPTS · Successor: ICS-collaborative NEPTS retender + LA 0-19 contract retender cycles"}
        ],
        "notes": "HDFT's transport line is shaped by a structurally distinctive footprint — a small Harrogate acute base supports a far-flung multi-local-authority children-and-young-people 0-19 services arm that delivers across North Yorkshire, Leeds, Bradford and a swathe of North-East LAs (Co Durham, Sunderland, Gateshead, Stockton, Middlesbrough, Hartlepool, Darlington, Northumberland), generating geographically dispersed business-mileage volume that dwarfs what a Harrogate-acute-only DGH would generate. NEPTS sits with West Yorkshire ICS lead-commissioner for the acute site; 0-19 LA-contract travel is funded through LA agreements. Industrial action 2023-24 drove cancellation-rebooking journeys; HMRC AMAP-rate freeze at 45p/mile since 2011 sustains internal-rate dispute pressure; diesel CPI and April 2025 NIC step-up feed forward via NEPTS pass-through.",
        "sources": [
            {"publisher": "Harrogate and District NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.hdft.nhs.uk/about/our-publications/"},
            {"publisher": "NHS England", "title": "Non-Emergency Patient Transport Services — National Framework + Eligibility Criteria 2021", "url": "https://www.england.nhs.uk/publication/non-emergency-patient-transport-services-nepts/"},
            {"publisher": "National Audit Office", "title": "NHS England's management of the primary care support services contract with Capita", "url": "https://www.nao.org.uk/reports/nhs-englands-management-of-the-primary-care-support-services-contract-with-capita/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Harrogate and District NHS FT provider profile (RCD)", "url": "https://www.cqc.org.uk/provider/RCD"}
        ],
        "related": ["Harrogate and District NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Transport (business + patient) — Wrightington, Wigan and Leigh NHS Foundation Trust", "Transport (business + patient) — Doncaster and Bassetlaw Teaching Hospitals NHS Foundation Trust", "NHS England"]
    },
    "Transport (business + patient) — Homerton Healthcare NHS Foundation Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "Homerton Healthcare NHS Foundation Trust"}],
        "description": "Homerton's £2.157M transport line covers business mileage (AfC Section 17 + AMAP), pool-fleet IFRS 16 lease costs, NEPTS contract pass-through and patient travel reimbursements across the Homerton Hospital Hackney main site plus a substantial integrated community-services footprint covering Hackney, City of London and the cross-border 0-19 / sexual-health / community arm reaching into Tower Hamlets and Newham. The integrated acute + community model broadens the business-mileage base above pure-acute peer trusts, and inner-London cross-trust transfers feed NEPTS volume.",
        "beneficiaries": "c. 4,500 WTE staff serving a c. 280,000 Hackney + City of London integrated-care catchment plus wider East London community / sexual-health reach to c. 1.0M people; c. 110,000 ED attendances/yr at Homerton ED; c. 35,000 admissions/yr; integrated acute + community model with substantial cross-borough children's, sexual-health and community-nursing arm.",
        "legal_basis": "NHS Act 2006 — NHSE Patient Transport Services Eligibility Criteria 2021 — Agenda for Change Section 17 (business mileage) — HMRC AMAP rates — IFRS 16 Leases (pool fleet) — DHSC Group Accounting Manual 2024-25 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£2.157M"},
            {"label": "Trust scale", "value": "Homerton Hospital (Hackney) + integrated community + sexual-health + 0-19 services across Hackney, City of London, Tower Hamlets, Newham; c. 4,500 WTE"},
            {"label": "Integrated-care model", "value": "Acute + community + sexual-health + 0-19 services arm broadens business-mileage base above pure-acute peers — community-team travel feeds the line"},
            {"label": "NEPTS commissioning", "value": "North East London ICS lead-commissioner NEPTS contract; eligibility per NHSE 2021 criteria"},
            {"label": "Composition", "value": "Business mileage (AfC S17 + AMAP 45p/25p frozen since 2011) + pool-fleet IFRS 16 leases + NEPTS pass-through + patient travel reimbursements"},
            {"label": "Inner-London cross-trust transfers", "value": "Cross-trust transfers within NEL ICS (to Royal London tertiary, Bart's, UCLH) generate NEPTS pass-through volume"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove cancellation rebooking + agency travel claims"},
            {"label": "April 2025 NIC + fuel CPI", "value": "Indirect via NEPTS contractor pass-through + diesel CPI feed forward unit-cost pressure"},
            {"label": "Funding trajectory", "value": "2021-22 c. £1.8M → 2023-24 c. £2.0M → 2024-25 £2.157M — fuel CPI + NEPTS contract uplift + community-team mileage growth"},
            {"label": "Delivery body", "value": "Trust E&F + outsourced NEPTS provider (NEL ICS lead-commissioner) + pool-fleet leasing partner + Trust HR (mileage)"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + NHSE Urgent and Emergency Care (NEPTS) + North East London ICB + DHSC"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2014 separate Homerton acute + community-services baselines · Successor: NEL ICS-collaborative NEPTS retender + cross-trust transfer protocol refresh"}
        ],
        "notes": "Homerton's transport line is shaped by the trust's integrated acute + community + sexual-health + 0-19 services model — community-team and sexual-health-team business mileage across Hackney, City of London, Tower Hamlets and Newham broadens the mileage base materially above pure-acute peer trusts in inner London. North East London ICS lead-commissioner NEPTS contract retender is the medium-term lever, with cross-trust transfers within NEL (to Royal London, Bart's, UCLH) generating NEPTS pass-through volume. Industrial action 2023-24 drove cancellation-rebooking journeys and agency travel claims; HMRC AMAP-rate freeze at 45p/mile since 2011 sustains internal-rate dispute pressure. Diesel CPI and April 2025 NIC step-up feed forward via NEPTS contractor pass-through.",
        "sources": [
            {"publisher": "Homerton Healthcare NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.homerton.nhs.uk/our-publications"},
            {"publisher": "NHS England", "title": "Non-Emergency Patient Transport Services — National Framework + Eligibility Criteria 2021", "url": "https://www.england.nhs.uk/publication/non-emergency-patient-transport-services-nepts/"},
            {"publisher": "National Audit Office", "title": "NHS England's management of the primary care support services contract with Capita", "url": "https://www.nao.org.uk/reports/nhs-englands-management-of-the-primary-care-support-services-contract-with-capita/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Homerton Healthcare NHS FT provider profile (RQX)", "url": "https://www.cqc.org.uk/provider/RQX"}
        ],
        "related": ["Homerton Healthcare NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Business rates — Whittington Health NHS Trust", "Transport (business + patient) — Harrogate and District NHS Foundation Trust", "NHS England"]
    },
}
