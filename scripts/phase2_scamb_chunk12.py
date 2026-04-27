# -*- coding: utf-8 -*-
# Phase 2 SCamb — chunk 12 (17 NHS Specialist/Community/Ambulance Trust orphan sub-lines)
# Hand-curated trust-specific PROGRAMME-archetype enrichment entries.
# Structural contract per docs/archetype_briefs.md.

NEW = {
    "Transport (business + patient) — The Christie NHS Foundation Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "The Christie NHS Foundation Trust"}],
        "description": "The Christie's £1.20M transport line covers business mileage (AMAP) for clinical and support staff, leased pool-cars and inter-site transfers between the Withington main site and outreach hubs at Salford Royal, Oldham and Macclesfield, plus patient-transport reimbursements under NHSE PTS eligibility for cancer patients travelling for radiotherapy fractions, chemotherapy, proton-beam therapy and CAR-T. The line also captures specialist couriers shifting cytotoxic chemotherapy preparations, radioisotopes (short half-life PET tracers) and pathology samples between sites in Greater Manchester and across the supra-regional cancer catchment.",
        "beneficiaries": "Serves a c. 3.4M supra-regional cancer catchment across Greater Manchester, Cheshire, Lancashire and parts of the East Midlands; treats c. 60,000 patients/yr (c. 44,000 chemo episodes + c. 110,000 radiotherapy fractions); c. 3,500 WTE staff working across the Withington main hospital + outreach radiotherapy at Oldham, Salford, Macclesfield, plus the proton-beam therapy centre opened 2018.",
        "legal_basis": "NHS Act 2006 · NHSE Patient Transport Services Eligibility Criteria · Healthcare Travel Costs Scheme (HTCS) · Agenda for Change s.17 + HMRC Approved Mileage Allowance Payments · IFRS 16 Leases (pool fleet) · DHSC Group Accounting Manual 2024-25",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£1.20M"},
            {"label": "Specialty footprint", "value": "Tertiary cancer centre — Withington main site + radiotherapy outreach at Oldham, Salford Royal, Macclesfield"},
            {"label": "Supra-regional catchment", "value": "c. 3.4M GM + Cheshire + Lancashire + parts of East Midlands; one of two NHS proton-beam centres (UCLH the other)"},
            {"label": "Annual activity", "value": "c. 60,000 patients/yr; c. 44,000 chemo episodes; c. 110,000 radiotherapy fractions; c. 750 proton-beam patients/yr"},
            {"label": "Workforce", "value": "c. 3,500 WTE; c. 750 medical + nursing on-site mobile across outreach"},
            {"label": "PTS driver", "value": "Daily radiotherapy fractions (typically 15-30 visits/course) drive HTCS reimbursement volume; CAR-T transport across UK referral pathway"},
            {"label": "Specialist couriers", "value": "Cytotoxic chemo preparations + short half-life PET tracers (FDG, C-11) require dedicated radiotracer couriers ex-Manchester cyclotron"},
            {"label": "Funding trajectory", "value": "Modest but rising due to Christie at Macclesfield satellite (opened 2022) + IFRS 16 2022 lease re-recognition + AMAP mileage growth post-pandemic"},
            {"label": "Delivery body", "value": "Christie Estates & Facilities + leased-fleet supplier (NHS Fleet Solutions / commercial leasing) + specialist radiopharm couriers"},
            {"label": "Policy owner", "value": "NHSE Specialised Commissioning (cancer · proton-beam · CAR-T) + DHSC + Greater Manchester ICB"},
            {"label": "Evaluation evidence", "value": "Christie ARA; CQC inspection (RBV — Outstanding); Model Hospital cancer benchmarks; NHSE proton-beam annual report"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-IFRS-16 lease accounting · Successor: Christie at Macclesfield + Christie at Salford expansion + zero-emission pool fleet under NHSE Net Zero 2032"}
        ],
        "notes": "The Christie is one of Europe's largest single-site cancer centres and sits at the apex of NHS specialised cancer commissioning, including one of only two NHS proton-beam therapy centres (the other UCLH) and a major CAR-T cellular-therapy site. Its transport line is modest in absolute terms versus Acute trusts because patient flow concentrates at one main campus, but the rolling expansion of outreach radiotherapy (Oldham, Salford, Macclesfield from 2022) drives staff inter-site mileage and HTCS patient-reimbursement volume. Specialist radiopharm couriers (short half-life PET tracers, cytotoxic chemo) and IFRS 16 2022 lease re-recognition are the structural cost drivers. Net Zero 2032 fleet electrification is being phased into pool-car renewals.",
        "sources": [
            {"publisher": "The Christie NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.christie.nhs.uk/about-us/our-publications/annual-reports/"},
            {"publisher": "NHS England", "title": "Specialised commissioning — proton-beam therapy service specification", "url": "https://www.england.nhs.uk/commissioning/spec-services/"},
            {"publisher": "Care Quality Commission", "title": "The Christie NHS Foundation Trust provider profile (RBV)", "url": "https://www.cqc.org.uk/provider/RBV"},
            {"publisher": "NHS England", "title": "Healthcare Travel Costs Scheme (HTCS)", "url": "https://www.nhs.uk/nhs-services/help-with-health-costs/healthcare-travel-costs-scheme-htcs/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "NHS Net Zero — delivering a net zero NHS", "url": "https://www.england.nhs.uk/greenernhs/a-net-zero-nhs/"}
        ],
        "related": ["The Christie NHS Foundation Trust", "Premises & Infrastructure", "NHS Specialist Trusts", "Transport (business + patient) — The Royal Marsden NHS Foundation Trust", "Transport (business + patient) — Great Ormond Street Hospital for Children NHS Foundation Trust", "NHS England"]
    },
    "Business rates — Derbyshire Community Health Services NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "Derbyshire Community Health Services NHS Foundation Trust"}],
        "description": "DCHS's £1.11M non-domestic-rates (NDR) bill covers business rates payable on the trust's portfolio of community hospitals, health centres, urgent treatment centres and clinic estate scattered across Derby city and the wider Derbyshire footprint, including sites at Ripley, Ilkeston, Ashbourne, Buxton, Whitworth, Heanor and Bolsover. NDR is paid to the relevant billing authority (Derbyshire Dales DC, Amber Valley BC, Derby City, etc.) under the Local Government Finance Act 1988 small-multiplier and large-multiplier system, with revaluations from the Valuation Office Agency reflecting rateable values from the 2023 list.",
        "beneficiaries": "Serves a c. 1.05M Derbyshire population; operates from c. 30+ sites including community hospitals at Ilkeston, Ripley, Ashbourne, Bolsover, Heanor, Buxton and Whitworth, plus c. 100 clinic and base-station locations; c. 4,400 WTE staff including district nurses, AHPs, school nurses and health visitors covering urban Derby + rural Peak District.",
        "legal_basis": "Local Government Finance Act 1988 (Sch 6 — non-domestic rating) · Non-Domestic Rating Act 2023 · Non-Domestic Rating (Multipliers and Private Finance) Act 2024 · Valuation Office Agency 2023 rating list · DHSC Group Accounting Manual 2024-25",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£1.11M"},
            {"label": "Estate footprint", "value": "c. 30+ owned/leased sites incl. community hospitals at Ilkeston, Ripley, Ashbourne, Bolsover, Heanor, Buxton, Whitworth + c. 100 clinic/base locations"},
            {"label": "Population served", "value": "c. 1.05M Derbyshire residents (Derby City + Derbyshire County)"},
            {"label": "Workforce", "value": "c. 4,400 WTE — district nurses, school nurses, health visitors, AHPs, MSK community physio"},
            {"label": "Billing authorities", "value": "Multiple: Derby City Council, Amber Valley BC, Derbyshire Dales DC, Bolsover DC, Erewash BC, High Peak BC, NE Derbyshire DC, Chesterfield BC, South Derbyshire DC"},
            {"label": "VOA list cycle", "value": "2023 rating list (3-year cycle from 2026 revaluation under Non-Domestic Rating Act 2023)"},
            {"label": "NDR multiplier 2024-25", "value": "Standard 54.6p; small-business 49.9p; healthcare estate generally on standard multiplier (no NHS exemption)"},
            {"label": "Funding trajectory", "value": "Rising c. 3-5%/yr in line with multiplier uprating + VOA 2023 revaluation; supplements multiplier increase under Non-Domestic Rating (Multipliers and Private Finance) Act 2024"},
            {"label": "Delivery body", "value": "DCHS Estates & Facilities team + NHSPS for leased sites + relevant billing authorities + VOA"},
            {"label": "Policy owner", "value": "DLUHC (Department for Levelling Up, Housing and Communities — now MHCLG) + HM Treasury + DHSC + NHSE"},
            {"label": "Evaluation evidence", "value": "DCHS ARA (FY25); CQC provider profile (RY8); NHSE Estates Returns Information Collection (ERIC) annual return"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2011 PCT-era estate · Successor: 2026 VOA revaluation under 3-year cycle + ongoing estate consolidation under Three Shifts community-care policy"}
        ],
        "notes": "Community trusts pay full non-domestic rates on their estates with no NHS exemption — unlike charities, NHS bodies do not receive the 80% mandatory relief, so the line tracks closely with the size and rateable value of the owned/leased footprint. DCHS's c. £1.1M reflects the geographic spread across c. 30+ community hospital sites and a long tail of clinics serving the Peak District and rural Derbyshire. Drivers include the VOA 2023 rating list (which raised many community-hospital RVs), the annual multiplier uprating, and the new supplementary multiplier introduced by the Non-Domestic Rating (Multipliers and Private Finance) Act 2024. Three Shifts community-care policy may drive estate expansion in coming years.",
        "sources": [
            {"publisher": "Derbyshire Community Health Services NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.dchs.nhs.uk/about-us/corporate-information/our-publications/annual-reports"},
            {"publisher": "Valuation Office Agency", "title": "Find a business rates valuation (2023 rating list)", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "UK Government", "title": "Non-Domestic Rating Act 2023", "url": "https://www.legislation.gov.uk/ukpga/2023/53"},
            {"publisher": "Care Quality Commission", "title": "Derbyshire Community Health Services NHS Foundation Trust provider profile (RY8)", "url": "https://www.cqc.org.uk/provider/RY8"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Estates Returns Information Collection (ERIC) 2023-24", "url": "https://digital.nhs.uk/data-and-information/publications/statistical/estates-returns-information-collection"}
        ],
        "related": ["Derbyshire Community Health Services NHS Foundation Trust", "Premises & Infrastructure", "NHS Community Trusts", "Business rates — Hertfordshire Community NHS Trust", "Business rates — Sussex Community NHS Foundation Trust", "Valuation Office Agency"]
    },
    "Amortisation — Moorfields Eye Hospital NHS Foundation Trust": {
        "aliases": [{"name": "Amortisation", "parent": "Moorfields Eye Hospital NHS Foundation Trust"}],
        "description": "Moorfields' £1.08M amortisation charge represents the systematic write-down of intangible assets — predominantly software licences (electronic patient record, ophthalmic imaging analysis, OCT/fundus image management software, research-grade AI imaging algorithms developed with DeepMind/Google Health) and capitalised software development under IAS 38. Moorfields is England's leading specialist eye hospital and has invested heavily in digital ophthalmology, including teleophthalmology platforms supporting the c. 32-site outreach network across north-east London and the home counties.",
        "beneficiaries": "Serves a national + supra-regional ophthalmic catchment with c. 700,000 patient attendances/yr; operates from City Road main hospital + c. 32 satellite/outreach sites across north-east London, Essex, Hertfordshire, Bedfordshire and Surrey; c. 2,400 WTE incl. c. 380 medical staff and the UCL Institute of Ophthalmology research partnership.",
        "legal_basis": "IAS 38 Intangible Assets · DHSC Group Accounting Manual ch.5 · NHS Act 2006 · Health and Care Act 2022 · Frascati Manual research/development distinction",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£1.08M"},
            {"label": "Specialty footprint", "value": "England's largest specialist eye hospital — City Road main + c. 32 satellite/outreach sites across NE London + Essex + Herts + Beds + Surrey"},
            {"label": "Annual activity", "value": "c. 700,000 outpatient attendances/yr; c. 25,000 inpatient/day-case episodes; c. 850,000 OCT scans/yr"},
            {"label": "Workforce", "value": "c. 2,400 WTE incl. c. 380 medical staff; UCL Institute of Ophthalmology academic partnership at 11-43 Bath Street"},
            {"label": "Intangibles class", "value": "Predominantly software licences (EPR, OCT/fundus image management, teleophthalmology platforms) + capitalised software development under IAS 38"},
            {"label": "Digital innovation", "value": "Moorfields-DeepMind/Google Health AI partnership for retinal disease detection; teleophthalmology supports outreach network"},
            {"label": "Useful economic life", "value": "Software typically 3-7 years amortisation per DHSC GAM ch.5; clinical-system EPR straight-line over service life"},
            {"label": "Funding trajectory", "value": "Stable around £1M/yr; expected to rise as Oriel new hospital programme (planned new King's Cross/St Pancras campus) brings forward capitalised software"},
            {"label": "Delivery body", "value": "Moorfields Digital + Estates teams + EPR provider (e.g. OpenEyes electronic ophthalmic record — open-source) + UCL IoO research partnership"},
            {"label": "Policy owner", "value": "NHSE Specialised Commissioning (specialist ophthalmology) + DHSC + NEL ICB host commissioner"},
            {"label": "Evaluation evidence", "value": "Moorfields ARA; CQC inspection (RP6); NIHR Moorfields Biomedical Research Centre annual report; NHSE Specialised Commissioning service spec"},
            {"label": "Predecessor / successor", "value": "Predecessor: legacy paper records + IT systems · Successor: Oriel new-hospital programme (King's Cross / St Pancras integrated eye-care campus + UCL IoO research) — large new-build software capitalisation expected"}
        ],
        "notes": "Moorfields is internationally recognised as a centre for ophthalmic research and has been an early adopter of clinical AI (the Moorfields-DeepMind retinal-disease detection partnership produced a Nature Medicine paper in 2018), driving capitalised software development costs that flow through amortisation. The current line is dominated by EPR and ophthalmic image-management licences. The biggest forward-looking driver is Oriel — the planned integrated eye-care, research and education campus to be co-located with UCL IoO at the St Pancras Hospital site, which will bring substantial new software and intangible capitalisation. IAS 38 useful-economic-life judgements (typically 3-7 years for software) under DHSC GAM ch.5 govern the unwind.",
        "sources": [
            {"publisher": "Moorfields Eye Hospital NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.moorfields.nhs.uk/about-us/our-publications/annual-reports"},
            {"publisher": "Care Quality Commission", "title": "Moorfields Eye Hospital provider profile (RP6)", "url": "https://www.cqc.org.uk/provider/RP6"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 — chapter 5 Property Plant Equipment & Intangibles", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Moorfields Eye Hospital", "title": "Oriel — our new eye care, research and education centre", "url": "https://www.oriel-london.org.uk/"},
            {"publisher": "NIHR", "title": "Moorfields Biomedical Research Centre", "url": "https://www.moorfieldsbrc.nihr.ac.uk/"},
            {"publisher": "Nature Medicine", "title": "Clinically applicable deep learning for diagnosis of retinal disease (De Fauw et al., 2018)", "url": "https://www.nature.com/articles/s41591-018-0107-6"}
        ],
        "related": ["Moorfields Eye Hospital NHS Foundation Trust", "Premises & Infrastructure", "NHS Specialist Trusts", "Amortisation — The Royal Marsden NHS Foundation Trust", "Amortisation — Great Ormond Street Hospital for Children NHS Foundation Trust", "NHS England"]
    },
    "Establishment costs — Lincolnshire Community Health Services NHS Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "Lincolnshire Community Health Services NHS Trust"}],
        "description": "LCHS's £1.07M establishment costs line covers postage, telephony and mobile telecoms, stationery, printing, office supplies, courier services and small office consumables across the trust's c. 100+ community sites spread across Lincolnshire — one of England's most rural and geographically dispersed counties. The trust runs district nursing, urgent-treatment-centre out-of-hours, neighbourhood teams and community hospitals at sites including Skegness, Louth, Spalding, Gainsborough and Boston, with high mobile-telecoms costs reflecting district nurses' caseload management on the road.",
        "beneficiaries": "Serves a c. 770,000 Lincolnshire population (Lincoln City + East Lindsey + South Holland + Boston + South Kesteven + North Kesteven + West Lindsey); operates from c. 100+ community sites including UTCs at Skegness, Louth, Spalding, Gainsborough; c. 2,800 WTE incl. district nurses, school nurses, health visitors and community AHPs.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · NHS Act 2006 · Health and Care Act 2022 · Communications Act 2003 (telecoms regulation)",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£1.07M"},
            {"label": "Estate footprint", "value": "c. 100+ community sites across Lincolnshire — one of England's most rural counties; UTCs at Skegness, Louth, Spalding, Gainsborough"},
            {"label": "Population served", "value": "c. 770,000 Lincolnshire residents (excluding North & North East Lincs which are NHS Humber Health Partnership)"},
            {"label": "Workforce", "value": "c. 2,800 WTE — district nurses, school nurses, health visitors, AHPs, neighbourhood teams"},
            {"label": "Cost mix", "value": "Postage, mobile telephony (community-staff data SIMs), printing/stationery, courier services, office consumables — typical community-trust split"},
            {"label": "Mobile telecoms driver", "value": "District nursing + neighbourhood teams require mobile data SIMs for caseload management (e.g. SystmOne mobile, EMIS Mobile) — heavy MNO contract spend"},
            {"label": "Geographic driver", "value": "Rural Lincolnshire (East Lindsey, South Holland) drives postage + courier costs for pathology samples + meds delivery to remote sites"},
            {"label": "Funding trajectory", "value": "Flat to slightly declining as digital records reduce print volume; offset by mobile-telecoms growth and 2024-25 Royal Mail postage uprating"},
            {"label": "Delivery body", "value": "LCHS Corporate Services + Procurement + IT/Digital + NHS Supply Chain (some commodity routes) + commercial telecoms providers (BT/Vodafone)"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Lincolnshire ICB (host commissioner)"},
            {"label": "Evaluation evidence", "value": "LCHS ARA; CQC provider profile (RY5); Model Hospital corporate-services benchmark; NHSE Operational Plan returns"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2011 Lincolnshire PCT establishment costs · Successor: digital-first community-care model under Three Shifts policy + ULEZ-equivalent vehicle replacement (rural relevance limited)"}
        ],
        "notes": "Establishment costs in community trusts behave very differently from acute trusts — postage and stationery decline with EPR adoption while mobile telephony and data SIMs grow with caseload-management apps for district nurses (SystmOne mobile, EMIS Mobile, NerveCentre or equivalents). LCHS's c. £1M reflects a mid-scale community workforce serving one of England's most rural counties, where courier costs for pathology samples and prescription delivery to remote East Lindsey and South Holland sites push up the line. The Three Shifts policy (Darzi report Sep 2024) directs more out-of-hospital care, which will likely grow community-trust mobile-telecoms baselines further. April 2025 Royal Mail letter pricing uprating also feeds in.",
        "sources": [
            {"publisher": "Lincolnshire Community Health Services NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.lincolnshirecommunityhealthservices.nhs.uk/about-us/corporate-publications"},
            {"publisher": "Care Quality Commission", "title": "Lincolnshire Community Health Services provider profile (RY5)", "url": "https://www.cqc.org.uk/provider/RY5"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Department of Health and Social Care", "title": "Independent investigation of the NHS in England (Darzi report, Sep 2024)", "url": "https://www.gov.uk/government/publications/independent-investigation-of-the-nhs-in-england"},
            {"publisher": "NHS England", "title": "Operational planning guidance 2024-25", "url": "https://www.england.nhs.uk/operational-planning-and-contracting/"},
            {"publisher": "Lincolnshire ICB", "title": "Lincolnshire Integrated Care Board commissioning", "url": "https://lincolnshire.icb.nhs.uk/"}
        ],
        "related": ["Lincolnshire Community Health Services NHS Trust", "Premises & Infrastructure", "NHS Community Trusts", "Establishment costs — Norfolk Community Health and Care NHS Trust", "Establishment costs — Hertfordshire Community NHS Trust", "Lincolnshire ICB"]
    },
    "Transport (business + patient) — Liverpool Heart and Chest Hospital NHS Foundation Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "Liverpool Heart and Chest Hospital NHS Foundation Trust"}],
        "description": "LHCH's £1.05M transport line covers staff business mileage, leased pool-cars, courier services for pathology and donated organs (heart/lung transplant referrals), and HTCS patient-transport reimbursements for cardiothoracic surgical, transcatheter and respiratory patients travelling to the Broadgreen single-site campus from across the supra-regional Cheshire & Merseyside, North Wales and Isle of Man catchment. The trust is one of the largest single-specialty cardiothoracic centres in the UK and runs a tertiary heart-transplant service that drives organ-retrieval transport.",
        "beneficiaries": "Serves a c. 2.8M supra-regional cardiothoracic catchment across Cheshire, Merseyside, parts of Lancashire, North Wales and the Isle of Man; c. 110,000 outpatient attendances/yr; c. 4,500 cardiac surgical procedures/yr; c. 1,800 WTE incl. c. 230 medical staff at the single Broadgreen site.",
        "legal_basis": "NHS Act 2006 · NHSE Patient Transport Services Eligibility Criteria · Healthcare Travel Costs Scheme · Human Tissue Act 2004 (organ retrieval) · Agenda for Change s.17 + HMRC Approved Mileage Allowance Payments · IFRS 16 Leases · DHSC Group Accounting Manual 2024-25",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£1.05M"},
            {"label": "Specialty footprint", "value": "Single-site cardiothoracic specialist centre at Broadgreen (Liverpool); one of the largest cardiothoracic providers in the UK"},
            {"label": "Supra-regional catchment", "value": "c. 2.8M Cheshire + Merseyside + parts of Lancs + North Wales + Isle of Man"},
            {"label": "Annual activity", "value": "c. 110,000 OP attendances; c. 4,500 cardiac surgical procedures; c. 30 heart transplants/yr (UK heart-transplant centre)"},
            {"label": "Workforce", "value": "c. 1,800 WTE; c. 230 medical staff"},
            {"label": "Organ-retrieval driver", "value": "Heart-transplant team operates UK retrieval rota; specialist couriers + on-call retrieval-team transport drive episodic transport spend"},
            {"label": "PTS driver", "value": "HTCS reimbursement for North Wales + Isle of Man cardiothoracic patients; ferry transit (IoM) included"},
            {"label": "Funding trajectory", "value": "Modest growth; IFRS 16 2022 lease re-recognition + AMAP mileage growth + post-pandemic staff travel rebound"},
            {"label": "Delivery body", "value": "LHCH Estates & Facilities + leased-fleet supplier (NHS Fleet Solutions / commercial leasing) + NHS Blood & Transplant retrieval team co-ordination"},
            {"label": "Policy owner", "value": "NHSE Specialised Commissioning (cardiothoracic surgery + heart transplantation) + DHSC + Cheshire & Merseyside ICB"},
            {"label": "Evaluation evidence", "value": "LHCH ARA; CQC inspection (RBQ — Outstanding); NHS Blood & Transplant heart-transplant outcomes; SCTS UK cardiac-surgery audit"},
            {"label": "Predecessor / successor", "value": "Predecessor: legacy Cardiothoracic Centre Liverpool · Successor: planned LUHFT (Liverpool University Hospitals) cardiac-services collaboration + Net Zero 2032 fleet electrification"}
        ],
        "notes": "LHCH operates as a single-site supra-regional cardiothoracic specialist centre, one of the largest in the UK, and is one of seven NHS heart-transplant centres. Its transport line is small in absolute terms because nearly all activity concentrates at Broadgreen, but the heart/lung organ-retrieval programme and the Isle of Man + North Wales catchment drive episodic high-cost specialist couriers and ferry transit. IFRS 16 2022 lease re-recognition lifted the recognised charge for pool-car leasing. CQC has rated the trust 'Outstanding' for safety and effectiveness — a profile that supports the case for ongoing investment in transport for tertiary referrals. Net Zero 2032 fleet electrification is being phased into pool-car renewals.",
        "sources": [
            {"publisher": "Liverpool Heart and Chest Hospital NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.lhch.nhs.uk/about-us/our-publications/annual-reports/"},
            {"publisher": "Care Quality Commission", "title": "Liverpool Heart and Chest Hospital provider profile (RBQ)", "url": "https://www.cqc.org.uk/provider/RBQ"},
            {"publisher": "NHS Blood and Transplant", "title": "Annual report on heart and lung transplantation", "url": "https://www.odt.nhs.uk/statistics-and-reports/annual-activity-report/"},
            {"publisher": "NHS England", "title": "Specialised commissioning — adult cardiac surgery service specification", "url": "https://www.england.nhs.uk/commissioning/spec-services/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Society for Cardiothoracic Surgery", "title": "UK Cardiac Surgery National Audit", "url": "https://scts.org/professionals/audit-results/"}
        ],
        "related": ["Liverpool Heart and Chest Hospital NHS Foundation Trust", "Premises & Infrastructure", "NHS Specialist Trusts", "Transport (business + patient) — Royal Papworth Hospital NHS Foundation Trust", "Transport (business + patient) — The Christie NHS Foundation Trust", "NHS Blood and Transplant"]
    },
    "Business rates — Hertfordshire Community NHS Trust": {
        "aliases": [{"name": "Business rates", "parent": "Hertfordshire Community NHS Trust"}],
        "description": "HCT's £1.04M non-domestic-rates bill covers business rates payable on the trust's c. 50+ owned and leased community sites across Hertfordshire — including the Herts and Essex Hospital (Bishop's Stortford), Cheshunt Community Hospital, Danesbury (Welwyn), Holywell House, Potters Bar Community Hospital, Hemel Hempstead Hospital sites and a long tail of clinics and child-development centres. Bills are paid to the relevant Hertfordshire billing authorities (Watford BC, Three Rivers DC, St Albans City, Welwyn Hatfield, East Herts, Stevenage, Broxbourne, North Herts, Dacorum) under the LGFA 1988.",
        "beneficiaries": "Serves a c. 1.2M Hertfordshire population; operates from c. 50+ owned/leased sites including Herts & Essex Hospital, Cheshunt CH, Potters Bar CH, Danesbury, Holywell House plus c. 100 clinic and outreach base locations; c. 3,500 WTE incl. district nurses, school nurses, health visitors, AHPs and integrated child-health teams.",
        "legal_basis": "Local Government Finance Act 1988 (Sch 6 — non-domestic rating) · Non-Domestic Rating Act 2023 · Non-Domestic Rating (Multipliers and Private Finance) Act 2024 · Valuation Office Agency 2023 rating list · DHSC Group Accounting Manual 2024-25",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£1.04M"},
            {"label": "Estate footprint", "value": "c. 50+ owned/leased sites incl. Herts & Essex Hospital (Bishop's Stortford), Cheshunt CH, Potters Bar CH, Danesbury, Holywell House"},
            {"label": "Population served", "value": "c. 1.2M Hertfordshire residents"},
            {"label": "Workforce", "value": "c. 3,500 WTE — district nurses, school nurses, health visitors, AHPs, integrated child-health teams"},
            {"label": "Billing authorities", "value": "Multiple: Watford BC, Three Rivers DC, St Albans City, Welwyn Hatfield, East Herts, Stevenage, Broxbourne, North Herts, Dacorum"},
            {"label": "VOA list cycle", "value": "2023 rating list (3-year cycle from 2026 revaluation under Non-Domestic Rating Act 2023)"},
            {"label": "NDR multiplier 2024-25", "value": "Standard 54.6p; small-business 49.9p; healthcare estate generally on standard multiplier"},
            {"label": "Funding trajectory", "value": "Rising c. 3-5%/yr in line with multiplier uprating + VOA 2023 revaluation; supplements multiplier increase under Non-Domestic Rating (Multipliers and Private Finance) Act 2024"},
            {"label": "Delivery body", "value": "HCT Estates & Facilities team + NHSPS for leased sites + relevant billing authorities + VOA"},
            {"label": "Policy owner", "value": "MHCLG (formerly DLUHC) + HM Treasury + DHSC + NHSE"},
            {"label": "Evaluation evidence", "value": "HCT ARA; CQC provider profile (RY4); NHSE Estates Returns Information Collection (ERIC) annual return"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2011 Herts PCT estate · Successor: 2026 VOA revaluation + Three Shifts community-care estate expansion + ongoing site rationalisation"}
        ],
        "notes": "Hertfordshire Community Trust pays rates on c. 50+ sites across one of England's most affluent commuter counties, where Valuation Office rateable values are elevated relative to comparator rural community-trust footprints. Per the 2023 VOA rating list, the trust's NDR baseline rose materially with the revaluation, and is set to rise again in 2026 under the new 3-year cycle introduced by the Non-Domestic Rating Act 2023. The Non-Domestic Rating (Multipliers and Private Finance) Act 2024 introduces a supplementary multiplier on higher-RV properties from April 2026, which will further lift the line. NHS bodies receive no mandatory NDR relief — unlike registered charities — so the full liability flows through.",
        "sources": [
            {"publisher": "Hertfordshire Community NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.hct.nhs.uk/about-us/corporate-publications/"},
            {"publisher": "Valuation Office Agency", "title": "Find a business rates valuation (2023 rating list)", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "UK Government", "title": "Non-Domestic Rating (Multipliers and Private Finance) Act 2024", "url": "https://www.legislation.gov.uk/ukpga/2024/16"},
            {"publisher": "Care Quality Commission", "title": "Hertfordshire Community NHS Trust provider profile (RY4)", "url": "https://www.cqc.org.uk/provider/RY4"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Estates Returns Information Collection (ERIC) 2023-24", "url": "https://digital.nhs.uk/data-and-information/publications/statistical/estates-returns-information-collection"}
        ],
        "related": ["Hertfordshire Community NHS Trust", "Premises & Infrastructure", "NHS Community Trusts", "Business rates — Derbyshire Community Health Services NHS Foundation Trust", "Business rates — Sussex Community NHS Foundation Trust", "Valuation Office Agency"]
    },
    "Amortisation — Yorkshire Ambulance Service NHS Trust": {
        "aliases": [{"name": "Amortisation", "parent": "Yorkshire Ambulance Service NHS Trust"}],
        "description": "YAS's £1.02M amortisation charge represents the systematic write-down of intangible assets — predominantly Computer Aided Dispatch (CAD) systems, electronic Patient Care Record (ePCR) software, NHS 111 IUC clinical-triage software (YAS hosts the NHS 111 service for Yorkshire and the Humber), telephony platforms, fleet-management software and capitalised software development under IAS 38. The line tracks the unwind of major IT capital investment cycles for the c. 1,000-vehicle ambulance fleet and the integrated NHS 111 / 999 / IUC operating model.",
        "beneficiaries": "Serves a c. 5.5M population across Yorkshire and the Humber (West Yorks, South Yorks, North Yorks, East Riding, Hull, NE Lincs, North Lincs); responds to c. 1.0M 999 calls/yr + c. 1.6M NHS 111 calls/yr; c. 6,300 WTE staff including c. 3,500 frontline paramedics + EMTs operating c. 1,000 emergency vehicles from c. 60 ambulance stations.",
        "legal_basis": "IAS 38 Intangible Assets · DHSC Group Accounting Manual ch.5 · NHS Act 2006 · Health and Care Act 2022 · NHSE Integrated Urgent Care Service Specification",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£1.02M"},
            {"label": "Geographic footprint", "value": "c. 15,500 km² across Yorkshire and the Humber — large mixed urban + rural footprint (Pennines + N York Moors + East Riding)"},
            {"label": "999 + 111 call volume", "value": "c. 1.0M emergency calls/yr; c. 1.6M NHS 111 calls/yr (YAS hosts NHS 111 IUC for Yorkshire and Humber)"},
            {"label": "Population served", "value": "c. 5.5M residents (West Yorks + South Yorks + North Yorks + East Riding + Hull + NE Lincs + North Lincs)"},
            {"label": "Workforce", "value": "c. 6,300 WTE; c. 3,500 frontline paramedics + EMTs; c. 1,000 emergency vehicles; c. 60 ambulance stations"},
            {"label": "Intangibles class", "value": "Predominantly CAD (Computer Aided Dispatch), ePCR (electronic Patient Care Record), NHS 111 IUC clinical-triage software, telephony, fleet-management software"},
            {"label": "Useful economic life", "value": "Software typically 3-7 years amortisation per DHSC GAM ch.5; CAD/ePCR core systems straight-line over service life"},
            {"label": "Funding trajectory", "value": "Stable around £1M/yr; expected to rise as ARP3 (Ambulance Response Programme 3) software upgrades + EPR-style ePCR refresh + integrated 111/999 platform investment unwind"},
            {"label": "Delivery body", "value": "YAS Digital + Information Systems team + CAD vendor (e.g. CleriCAD, Cleric) + ePCR vendor (e.g. SIREN, Terrafix) + NHS 111 platform"},
            {"label": "Policy owner", "value": "NHSE Urgent & Emergency Care directorate (ARP + IUC) + DHSC + Humber & North Yorkshire ICB + West Yorkshire ICB + South Yorkshire ICB"},
            {"label": "Evaluation evidence", "value": "YAS ARA; CQC inspection (RX8); NHSE Ambulance Quality Indicators monthly; AACE benchmarking; ORH ambulance benchmarking"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2006 West/South/N Yorks ambulance services merger · Successor: ARP3 software refresh + NHS 111 IUC platform upgrade + zero-emission fleet under NHSE Net Zero 2032"}
        ],
        "notes": "YAS is one of two ambulance services that hosts the NHS 111 IUC clinical-triage service for its region (the other being SCAS in some areas), which means its intangibles base includes both 999 CAD/ePCR and 111 triage platform software, lifting the amortisation profile relative to ambulance services that do not host 111. IAS 38 useful-economic-life judgements (typically 3-7 years for software per DHSC GAM ch.5) govern the unwind. Forward-looking drivers include ARP3 (Ambulance Response Programme 3) software refresh, ePCR system replacement, and integrated 111/999/CAS platform investments. The c. £1M baseline is modest in cash terms but tracks closely with capital-investment cycles.",
        "sources": [
            {"publisher": "Yorkshire Ambulance Service NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.yas.nhs.uk/about-us/corporate-information/annual-reports/"},
            {"publisher": "NHS England", "title": "Ambulance Quality Indicators (monthly statistics)", "url": "https://www.england.nhs.uk/statistics/statistical-work-areas/ambulance-quality-indicators/"},
            {"publisher": "NHS England", "title": "Integrated Urgent Care Service Specification", "url": "https://www.england.nhs.uk/publication/integrated-urgent-care-service-specification/"},
            {"publisher": "Care Quality Commission", "title": "Yorkshire Ambulance Service provider profile (RX8)", "url": "https://www.cqc.org.uk/provider/RX8"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 — chapter 5 PPE & Intangibles", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Association of Ambulance Chief Executives", "title": "AACE Annual Report and ambulance benchmarking", "url": "https://aace.org.uk/"}
        ],
        "related": ["Yorkshire Ambulance Service NHS Trust", "Premises & Infrastructure", "NHS Ambulance Trusts", "Amortisation — London Ambulance Service NHS Trust", "Amortisation — East of England Ambulance Service NHS Trust", "NHS England"]
    },
    "General supplies & services — The Royal Orthopaedic Hospital NHS Foundation Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "The Royal Orthopaedic Hospital NHS Foundation Trust"}],
        "description": "ROH Birmingham's £1.02M general supplies & services line covers non-clinical consumables, hotel services, hard-FM consumables (cleaning chemicals, paper goods, laundry processing inputs), waste-management consumables and small office/clinical-area supplies that fall outside the dedicated drugs and clinical-supplies lines. ROH is England's largest specialist musculoskeletal trust at the Northfield site (south Birmingham), focused on elective orthopaedics, complex spinal surgery, bone-tumour oncology and paediatric orthopaedics — a single-specialty case-mix that drives a relatively contained general-supplies baseline.",
        "beneficiaries": "Serves a c. 5M+ supra-regional MSK catchment across the West Midlands and beyond for tertiary-level work (bone tumour, complex spine, revision arthroplasty); c. 145,000 outpatient attendances/yr; c. 14,000 day-case + inpatient procedures/yr (predominantly elective orthopaedics); c. 1,300 WTE at the single Northfield campus.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 2 Inventories (interaction) · NHS Act 2006 · Health and Care Act 2022 · Public Contracts Regulations 2015 / Procurement Act 2023",
        "key_stats": [
            {"label": "General supplies & services 2024-25", "value": "£1.02M"},
            {"label": "Specialty footprint", "value": "Single-site specialist MSK centre at Northfield (south Birmingham); England's largest specialist orthopaedic trust"},
            {"label": "Supra-regional catchment", "value": "c. 5M+ across West Midlands; tertiary national referrals for bone tumour and complex spine"},
            {"label": "Annual activity", "value": "c. 145,000 OP attendances; c. 14,000 day-case + inpatient procedures; one of England's highest-volume hip/knee arthroplasty providers"},
            {"label": "Workforce", "value": "c. 1,300 WTE at the Northfield campus"},
            {"label": "Cost mix", "value": "Hotel services consumables (linen, paper goods), cleaning chemicals, laundry-processing inputs, waste-stream consumables, small office/clinical-area supplies"},
            {"label": "Procurement route", "value": "NHS Supply Chain framework via Towers (Hotel Services / Catering / Patient Hygiene) + Procurement Act 2023 transition"},
            {"label": "Funding trajectory", "value": "Stable; modest growth tracking inflation and elective-recovery throughput"},
            {"label": "Delivery body", "value": "ROH Procurement + Estates & Facilities + NHS Supply Chain frameworks (multiple Towers) + soft-FM contractors"},
            {"label": "Policy owner", "value": "NHSE Specialised Commissioning (specialist MSK + bone-oncology) + DHSC + NHS Supply Chain + Birmingham & Solihull ICB host"},
            {"label": "Evaluation evidence", "value": "ROH ARA; CQC inspection (RRJ — Outstanding); Model Hospital MSK benchmarks; National Joint Registry (NJR) outcome data"},
            {"label": "Predecessor / successor", "value": "Predecessor: legacy ROH 1817 founding · Successor: planned MSK collaboration with UHB (University Hospitals Birmingham) + ongoing elective-recovery throughput growth"}
        ],
        "notes": "The Royal Orthopaedic Hospital is England's largest specialist orthopaedic trust and is consistently among the highest-volume hip/knee arthroplasty providers in England, with a strong elective-recovery focus that suits the post-pandemic high-volume low-complexity surgical hub model. Its general supplies & services line is contained at c. £1M because of single-site working and a narrow elective case-mix (no maternity, no ED, no general medicine). The line is dominated by hotel-services consumables and hard/soft FM inputs procured via NHS Supply Chain Towers. CQC has rated the trust 'Outstanding' for several recent inspection cycles. The MSK-collaboration policy direction with UHB may consolidate procurement routes in coming years.",
        "sources": [
            {"publisher": "The Royal Orthopaedic Hospital NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.roh.nhs.uk/about-us/publications-and-reports"},
            {"publisher": "Care Quality Commission", "title": "The Royal Orthopaedic Hospital provider profile (RRJ)", "url": "https://www.cqc.org.uk/provider/RRJ"},
            {"publisher": "NHS Supply Chain", "title": "Hotel services and Patient hygiene categories (Towers)", "url": "https://www.supplychain.nhs.uk/"},
            {"publisher": "National Joint Registry", "title": "NJR Annual Report (joint replacement outcomes)", "url": "https://www.njrcentre.org.uk/njr-annual-reports/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Specialised commissioning — specialist orthopaedics service spec", "url": "https://www.england.nhs.uk/commissioning/spec-services/"}
        ],
        "related": ["The Royal Orthopaedic Hospital NHS Foundation Trust", "Clinical Supplies & Drugs", "NHS Specialist Trusts", "General supplies & services — Royal National Orthopaedic Hospital NHS Trust", "General supplies & services — The Robert Jones and Agnes Hunt Orthopaedic Hospital NHS Foundation Trust", "NHS Supply Chain"]
    },
    "General supplies & services — Queen Victoria Hospital NHS Foundation Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "Queen Victoria Hospital NHS Foundation Trust"}],
        "description": "QVH East Grinstead's £1.01M general supplies & services line covers non-clinical consumables, hotel services, hard/soft FM consumables (cleaning chemicals, paper goods, laundry inputs), waste-management and small office supplies — outside dedicated drugs and clinical-supplies lines. QVH is England's leading specialist reconstructive plastic-surgery and burns centre, founded in WWII as part of Sir Archibald McIndoe's Guinea Pig Club work, and runs a tertiary supra-regional service for plastic surgery, oral & maxillofacial, head & neck cancer reconstruction, hand surgery, corneoplastics and prosthetics from its single Holtye Road site.",
        "beneficiaries": "Serves a c. 4.5M supra-regional plastics/reconstructive catchment across Sussex, Kent, Surrey and parts of South East London; c. 90,000 OP attendances/yr; c. 13,000 day-case + inpatient procedures/yr; c. 900 WTE at the single East Grinstead campus; tertiary national-referral burns centre.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 2 Inventories (interaction) · NHS Act 2006 · Health and Care Act 2022 · Public Contracts Regulations 2015 / Procurement Act 2023",
        "key_stats": [
            {"label": "General supplies & services 2024-25", "value": "£1.01M"},
            {"label": "Specialty footprint", "value": "Single-site specialist reconstructive + burns centre at Holtye Road, East Grinstead; founded WWII Sir Archibald McIndoe Guinea Pig Club"},
            {"label": "Supra-regional catchment", "value": "c. 4.5M Sussex + Kent + Surrey + parts of SE London + national tertiary burns referrals"},
            {"label": "Annual activity", "value": "c. 90,000 OP attendances; c. 13,000 day-case + inpatient procedures; tertiary plastics, OMFS, H&N cancer reconstruction, hand surgery, corneoplastics, prosthetics"},
            {"label": "Workforce", "value": "c. 900 WTE at the East Grinstead campus"},
            {"label": "Cost mix", "value": "Hotel services consumables (linen, paper goods), cleaning chemicals, laundry-processing inputs, waste-stream consumables, small office/clinical-area supplies"},
            {"label": "Procurement route", "value": "NHS Supply Chain framework via Towers (Hotel Services / Patient Hygiene) + Procurement Act 2023 transition"},
            {"label": "Funding trajectory", "value": "Stable; modest growth tracking inflation; elective-recovery and tertiary referrals supportive"},
            {"label": "Delivery body", "value": "QVH Procurement + Estates & Facilities + NHS Supply Chain frameworks + soft-FM contractors"},
            {"label": "Policy owner", "value": "NHSE Specialised Commissioning (specialist reconstructive surgery + burns) + DHSC + Sussex ICB host"},
            {"label": "Evaluation evidence", "value": "QVH ARA; CQC inspection (RPC — Outstanding); Model Hospital benchmarks; British Burn Association audit"},
            {"label": "Predecessor / successor", "value": "Predecessor: WWII Royal Air Force / civilian Plastic Surgery & Jaw Injury Centre (McIndoe) · Successor: continued partnership with Surrey & Sussex Healthcare for shared services + planned theatre expansion"}
        ],
        "notes": "QVH carries a unique heritage — the Guinea Pig Club of WWII airmen treated by Sir Archibald McIndoe — and remains one of the smallest specialist NHS foundation trusts by turnover (c. £75M). The general supplies & services line is contained at c. £1M because of single-site working and a narrow tertiary case-mix (no ED, no maternity, no general medicine). Hotel-services consumables and hard/soft FM inputs are procured via NHS Supply Chain Towers under the Procurement Act 2023 transition. CQC has rated the trust 'Outstanding'. The trust's small scale makes it vulnerable to absorption discussions periodically — though specialist-commissioning protections have preserved its independence to date.",
        "sources": [
            {"publisher": "Queen Victoria Hospital NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.qvh.nhs.uk/about-us/our-trust/annual-reports/"},
            {"publisher": "Care Quality Commission", "title": "Queen Victoria Hospital provider profile (RPC)", "url": "https://www.cqc.org.uk/provider/RPC"},
            {"publisher": "NHS Supply Chain", "title": "Hotel services and Patient hygiene categories (Towers)", "url": "https://www.supplychain.nhs.uk/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Specialised commissioning — burn care service specification", "url": "https://www.england.nhs.uk/commissioning/spec-services/"},
            {"publisher": "British Burn Association", "title": "BBA national burn-care audit and standards", "url": "https://www.britishburnassociation.org/"}
        ],
        "related": ["Queen Victoria Hospital NHS Foundation Trust", "Clinical Supplies & Drugs", "NHS Specialist Trusts", "General supplies & services — The Walton Centre NHS Foundation Trust", "General supplies & services — The Robert Jones and Agnes Hunt Orthopaedic Hospital NHS Foundation Trust", "NHS Supply Chain"]
    },
    "Drugs costs — Leeds Community Healthcare NHS Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "Leeds Community Healthcare NHS Trust"}],
        "description": "LCH's £0.99M drugs costs line covers community-administered medicines stock — predominantly vaccination programmes (school-age immunisations, flu, HPV, MMR catch-up), insulin/devices for community diabetes nursing, palliative end-of-life community medicines, anticipatory care kits for district nursing, and medicines used in the trust's intermediate-care and Neighbourhood Teams. Most prescription costs sit elsewhere (community-pharmacy primary-care budget) — this line covers stock dispensed and administered directly by trust clinicians.",
        "beneficiaries": "Serves the c. 825,000 Leeds population through district nursing, neighbourhood teams, school nursing, health visiting, intermediate care, end-of-life community care and the Leeds 0-19 Public Health Integrated Nursing Service; c. 3,200 WTE incl. district nurses, school nurses, health visitors, AHPs and clinical support workers across c. 70 community sites.",
        "legal_basis": "NHS Act 2006 (Drug Tariff) · Branded Medicines Pricing Scheme · Voluntary Scheme for Branded Medicines Pricing Access and Growth (VPAG) 2024 · Human Medicines Regulations 2012 · DHSC Group Accounting Manual 2024-25",
        "key_stats": [
            {"label": "Drugs costs 2024-25", "value": "£0.99M"},
            {"label": "Population served", "value": "c. 825,000 Leeds residents"},
            {"label": "Service footprint", "value": "District nursing, school nursing, health visiting, neighbourhood teams, intermediate care, end-of-life, 0-19 Public Health Integrated Nursing Service"},
            {"label": "Workforce", "value": "c. 3,200 WTE — district nurses, school nurses, health visitors, AHPs"},
            {"label": "Drugs mix", "value": "School-age immunisations (HPV, flu, MMR), community diabetes insulin/devices, anticipatory-care end-of-life kits, intermediate-care medicines"},
            {"label": "Vaccination volume", "value": "School-Age Immunisation Service delivers tens of thousands of HPV + flu + MMR doses annually across Leeds schools"},
            {"label": "Procurement route", "value": "NHS Supply Chain Pharmacy Tower + UKHSA-supplied centrally-procured vaccines (e.g. flu, HPV — flow varies)"},
            {"label": "Funding trajectory", "value": "Rising in line with vaccination-programme expansion (RSV adult programme 2024, MMR catch-up campaign), VPAG 2024 contributions and end-of-life community-care growth"},
            {"label": "Delivery body", "value": "LCH Pharmacy + Procurement + School-Age Immunisation team + community-nursing teams + NHS Supply Chain (Pharmacy Tower)"},
            {"label": "Policy owner", "value": "NHSE Vaccinations & Screening + DHSC + UKHSA (centrally procured vaccines) + West Yorkshire ICB (host commissioner)"},
            {"label": "Evaluation evidence", "value": "LCH ARA; CQC provider profile (RY2); UKHSA vaccination-coverage statistics (COVER); School-Age Immunisation national audits"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2011 Leeds PCT community-medicines budget · Successor: RSV adult vaccination programme (Sept 2024 rollout) + MMR catch-up campaign + Three Shifts community-care expansion"}
        ],
        "notes": "Community drug spend in trusts like LCH behaves very differently from acute drug spend — there is no chemotherapy, biologics or drug-tariff-listed exotic spend. The line is dominated by routine vaccination programmes (HPV, flu, MMR, school-age, with the new RSV adult programme launched September 2024 added to the mix), end-of-life anticipatory community medicines, community-diabetes insulin/devices and intermediate-care medicines. UKHSA centrally procures most vaccines and supplies them in kind, so the £0.99M line largely reflects locally-purchased adjuncts and community-administered medicines under the Drug Tariff. Three Shifts policy (Darzi report) directing more out-of-hospital care will continue to grow this baseline.",
        "sources": [
            {"publisher": "Leeds Community Healthcare NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.leedscommunityhealthcare.nhs.uk/about-us/our-publications/annual-reports/"},
            {"publisher": "UK Health Security Agency", "title": "Cover of Vaccination Evaluated Rapidly (COVER) statistics", "url": "https://www.gov.uk/government/collections/vaccine-uptake"},
            {"publisher": "Care Quality Commission", "title": "Leeds Community Healthcare provider profile (RY2)", "url": "https://www.cqc.org.uk/provider/RY2"},
            {"publisher": "Department of Health and Social Care", "title": "Voluntary Scheme for Branded Medicines Pricing Access and Growth (VPAG) 2024", "url": "https://www.gov.uk/government/publications/voluntary-scheme-for-branded-medicines-pricing-access-and-growth-vpag"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "RSV vaccination programme (Sept 2024)", "url": "https://www.england.nhs.uk/2024/06/nhs-prepares-to-roll-out-historic-vaccination-programme-against-deadly-virus/"}
        ],
        "related": ["Leeds Community Healthcare NHS Trust", "Clinical Supplies & Drugs", "NHS Community Trusts", "Drugs costs — Norfolk Community Health and Care NHS Trust", "Drugs costs — Hertfordshire Community NHS Trust", "UK Health Security Agency"]
    },
    "Drugs costs — West Midlands Ambulance Service University NHS Foundation Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "West Midlands Ambulance Service University NHS Foundation Trust"}],
        "description": "WMAS's £0.99M drugs costs line covers the medicines stock loaded onto front-line emergency vehicles (DCAs, RRVs, HART vehicles) and used by paramedics under PGDs and POMs Order exemptions — including analgesics (morphine, paracetamol, methoxyflurane Penthrox), tranexamic acid, antiemetics, salbutamol nebs, glucose 10% and adrenaline for anaphylaxis/cardiac arrest, atropine, naloxone for opioid OD, midazolam for status epilepticus, antibiotics for sepsis, and amiodarone for VF/VT. Stock turnover is heavy across c. 1,000 vehicles and Make Ready Centres in the West Midlands.",
        "beneficiaries": "Serves a c. 5.9M population across the West Midlands (Birmingham, Black Country, Coventry, Solihull, Staffordshire, Stoke, Warwickshire, Worcestershire, Herefordshire, Shropshire, Telford & Wrekin); responds to c. 1.2M 999 calls/yr; c. 7,000 WTE staff including c. 4,500 frontline paramedics + EMTs; c. 1,000 emergency vehicles operating from c. 95 ambulance stations + 15 Make Ready Centres.",
        "legal_basis": "Human Medicines Regulations 2012 (POMs Order — paramedic exemptions) · NHS Act 2006 (Drug Tariff) · Branded Medicines Pricing Scheme · VPAG 2024 · Misuse of Drugs Regs 2001 (CDs e.g. morphine) · DHSC Group Accounting Manual 2024-25",
        "key_stats": [
            {"label": "Drugs costs 2024-25", "value": "£0.99M"},
            {"label": "Geographic footprint", "value": "c. 13,000 km² across West Midlands — Birmingham + Black Country + Coventry + Solihull + Staffs + Stoke + Warks + Worcs + Herefs + Shrops + T&W"},
            {"label": "999 call volume", "value": "c. 1.2M emergency calls/yr"},
            {"label": "Population served", "value": "c. 5.9M residents (West Midlands)"},
            {"label": "Workforce", "value": "c. 7,000 WTE; c. 4,500 frontline paramedics + EMTs"},
            {"label": "Fleet drug-stock", "value": "c. 1,000 vehicles + 15 Make Ready Centres requiring rotating stock — strict CD storage + accountability per MDR 2001"},
            {"label": "Drug mix", "value": "Analgesics (morphine, paracetamol, Penthrox), TXA, antiemetics, salbutamol, adrenaline, atropine, naloxone, midazolam, sepsis antibiotics, amiodarone"},
            {"label": "Make Ready efficiency", "value": "WMAS pioneered Make Ready Centre model — centralised vehicle prep, drug-pack restocking, infection control"},
            {"label": "Funding trajectory", "value": "Rising with prescribing-scope expansion (paramedic independent prescribers from 2018), naloxone scope-up, drug-tariff inflation"},
            {"label": "Delivery body", "value": "WMAS Pharmacy + Make Ready Centre logistics + NHS Supply Chain Pharmacy Tower + commercial-pharmacy contractor"},
            {"label": "Policy owner", "value": "NHSE Urgent & Emergency Care + DHSC + MHRA (POMs Order paramedic exemptions) + JRCALC (Joint Royal Colleges Ambulance Liaison Committee — clinical guidelines)"},
            {"label": "Evaluation evidence", "value": "WMAS ARA; CQC provider profile (RYA — Outstanding); JRCALC clinical guideline updates; AACE benchmarking"},
            {"label": "Predecessor / successor", "value": "Predecessor: legacy 1974 NHS reorganisation regional ambulance services (Birmingham, Black Country, etc.) merged into WMAS · Successor: paramedic independent prescribing scope expansion + community-based ambulance care (CBAC) drug-pack diversification"}
        ],
        "notes": "WMAS pioneered the Make Ready Centre model — centralised vehicle preparation, drug-pack restocking and deep-cleaning hubs that have been adopted across English ambulance services — and is consistently rated CQC 'Outstanding'. Drug stock spend across c. 1,000 vehicles and 15 MRCs is dominated by JRCALC-guideline-driven items (analgesics, anaphylaxis, cardiac arrest, status epilepticus). Misuse of Drugs Regs 2001 governs CD (morphine) storage and accountability. Forward-looking drivers include paramedic independent-prescribing scope expansion (since 2018), naloxone scope-up (community drug overdose response), and JRCALC guideline-driven additions like Penthrox (methoxyflurane). Drug-tariff inflation and VPAG 2024 contributions add modest upward pressure.",
        "sources": [
            {"publisher": "West Midlands Ambulance Service University NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://wmas.nhs.uk/about-us/publications/annual-report-and-accounts/"},
            {"publisher": "Care Quality Commission", "title": "West Midlands Ambulance Service provider profile (RYA)", "url": "https://www.cqc.org.uk/provider/RYA"},
            {"publisher": "JRCALC", "title": "JRCALC Clinical Guidelines for paramedic practice", "url": "https://aace.org.uk/clinical/jrcalc/"},
            {"publisher": "MHRA / DHSC", "title": "Human Medicines Regulations 2012 — POMs Order exemptions", "url": "https://www.legislation.gov.uk/uksi/2012/1916/contents"},
            {"publisher": "NHS England", "title": "Ambulance Quality Indicators (monthly statistics)", "url": "https://www.england.nhs.uk/statistics/statistical-work-areas/ambulance-quality-indicators/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"}
        ],
        "related": ["West Midlands Ambulance Service University NHS Foundation Trust", "Clinical Supplies & Drugs", "NHS Ambulance Trusts", "Drugs costs — London Ambulance Service NHS Trust", "Drugs costs — South Western Ambulance Service NHS Foundation Trust", "JRCALC"]
    },
    "Amortisation — Liverpool Women's NHS Foundation Trust": {
        "aliases": [{"name": "Amortisation", "parent": "Liverpool Women's NHS Foundation Trust"}],
        "description": "Liverpool Women's £0.98M amortisation charge represents the systematic write-down of intangible assets — predominantly maternity electronic patient record software (e.g. BadgerNet/Cerner Maternity), neonatal IT, gynaecology and reproductive-medicine clinical systems, fertility-treatment software, IT licences and capitalised software development under IAS 38. The trust is the largest single-specialty women's hospital in Europe at the Crown Street site and one of three NHS specialist Women's hospital trusts (with Birmingham Women's & Children's and Tommy's research integration).",
        "beneficiaries": "Serves a c. 2.5M Cheshire & Merseyside maternity / gynae / neonatal catchment; c. 8,000 births/yr (one of England's largest single-site maternity units); c. 30,000 gynaecology OP attendances/yr; c. 1,000 IVF cycles/yr; one of England's busiest tertiary neonatal intensive-care units; c. 1,500 WTE at the Crown Street campus.",
        "legal_basis": "IAS 38 Intangible Assets · DHSC Group Accounting Manual ch.5 · NHS Act 2006 · Health and Care Act 2022 · Human Fertilisation and Embryology Act 1990/2008 (HFEA-licensed activity)",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£0.98M"},
            {"label": "Specialty footprint", "value": "Single-site specialist women's + neonatal hospital at Crown Street, Liverpool — largest single-specialty women's hospital in Europe"},
            {"label": "Annual activity", "value": "c. 8,000 births/yr; c. 30,000 gynaecology OP attendances; c. 1,000 IVF cycles; tertiary neonatal intensive-care"},
            {"label": "Catchment", "value": "c. 2,500,000 Cheshire & Merseyside + supra-regional fertility/neonatal referrals"},
            {"label": "Workforce", "value": "c. 1,500 WTE at Crown Street campus"},
            {"label": "Intangibles class", "value": "Maternity EPR (BadgerNet / Cerner Maternity), neonatal IT, gynaecology systems, fertility-treatment software, IT licences, capitalised software development"},
            {"label": "Useful economic life", "value": "Software typically 3-7 years amortisation per DHSC GAM ch.5; clinical-system EPR straight-line over service life"},
            {"label": "HFEA-regulated activity", "value": "Hewitt Fertility Centre is one of UK's largest IVF centres — HFEA-licensed, drives specialised-software capitalisation"},
            {"label": "Funding trajectory", "value": "Stable around £1M/yr; long-running Future Generations / new-hospital strategic case for Crown Street replacement may bring new software capitalisation"},
            {"label": "Delivery body", "value": "LWH Digital + Estates teams + EPR vendor (e.g. BadgerNet by Clevermed/Sword) + neonatal-IT vendor + Hewitt Centre fertility software"},
            {"label": "Policy owner", "value": "NHSE Specialised Commissioning (neonatal ICU + complex fertility) + DHSC + Cheshire & Merseyside ICB host"},
            {"label": "Evaluation evidence", "value": "LWH ARA; CQC inspection (REP); HFEA inspection of Hewitt Centre; MBRRACE-UK perinatal audit; NHS Resolution maternity-incentive scheme"},
            {"label": "Predecessor / successor", "value": "Predecessor: legacy paper records · Successor: long-running Future Generations strategic case for new women's hospital + integrated maternity-EPR refresh"}
        ],
        "notes": "Liverpool Women's runs one of Europe's largest single-site maternity services (c. 8,000 births/yr) and the Hewitt Fertility Centre — one of the UK's largest IVF clinics, HFEA-licensed and driving specialised fertility-treatment software capitalisation that flows through amortisation. Specialised maternity EPR software (e.g. BadgerNet) and neonatal IT also feature prominently. The long-running 'Future Generations' strategic case for replacement of the Crown Street site (raised periodically since c. 2014) has not yet been funded for new build; if approved, it would lift amortisation materially as new clinical systems are capitalised. IAS 38 useful-economic-life judgements (typically 3-7 years for software) under DHSC GAM ch.5 govern the unwind.",
        "sources": [
            {"publisher": "Liverpool Women's NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.liverpoolwomens.nhs.uk/about-us/publications/annual-report/"},
            {"publisher": "Care Quality Commission", "title": "Liverpool Women's provider profile (REP)", "url": "https://www.cqc.org.uk/provider/REP"},
            {"publisher": "Human Fertilisation and Embryology Authority", "title": "HFEA fertility-clinic inspections and licensing", "url": "https://www.hfea.gov.uk/"},
            {"publisher": "MBRRACE-UK", "title": "Mothers and Babies: Reducing Risk through Audits and Confidential Enquiries", "url": "https://www.npeu.ox.ac.uk/mbrrace-uk"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 — chapter 5 PPE & Intangibles", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS Resolution", "title": "Maternity Incentive Scheme", "url": "https://resolution.nhs.uk/services/claims-management/clinical-schemes/clinical-negligence-scheme-for-trusts/maternity-incentive-scheme/"}
        ],
        "related": ["Liverpool Women's NHS Foundation Trust", "Premises & Infrastructure", "NHS Specialist Trusts", "Amortisation — Moorfields Eye Hospital NHS Foundation Trust", "Amortisation — Sheffield Children's NHS Foundation Trust", "Human Fertilisation and Embryology Authority"]
    },
    "Establishment costs — Norfolk Community Health and Care NHS Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "Norfolk Community Health and Care NHS Trust"}],
        "description": "NCH&C's £0.98M establishment costs line covers postage, telephony and mobile telecoms, stationery, printing, courier services and small office consumables across the trust's c. 60+ community sites spread across one of England's most rural counties — Norfolk, including community hospitals at Norwich, North Walsham, Cromer, Swaffham, Beccles, Dereham and Benjamin Court (Cromer). Mobile telecoms are heavy because district nurses and neighbourhood teams operate caseload-management apps on mobile data SIMs across rural Norfolk.",
        "beneficiaries": "Serves a c. 925,000 Norfolk population (excl. Great Yarmouth/Waveney which is JPUH catchment); operates from c. 60+ community sites including community hospitals at North Walsham, Cromer, Swaffham, Beccles, Dereham + a long tail of clinics; c. 2,500 WTE incl. district nurses, school nurses, health visitors, AHPs and intermediate-care teams.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · NHS Act 2006 · Health and Care Act 2022 · Communications Act 2003 (telecoms regulation)",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£0.98M"},
            {"label": "Estate footprint", "value": "c. 60+ community sites across Norfolk incl. community hospitals at North Walsham, Cromer, Swaffham, Beccles, Dereham + clinic + base locations"},
            {"label": "Population served", "value": "c. 925,000 Norfolk residents (excl. Great Yarmouth/Waveney — JPUH catchment)"},
            {"label": "Workforce", "value": "c. 2,500 WTE — district nurses, school nurses, health visitors, AHPs, intermediate-care teams"},
            {"label": "Cost mix", "value": "Postage, mobile telephony (community-staff data SIMs), printing/stationery, courier services, office consumables — typical community-trust split"},
            {"label": "Mobile telecoms driver", "value": "District nursing + neighbourhood teams require mobile data SIMs for caseload management (e.g. SystmOne mobile, EMIS Mobile) — heavy MNO contract spend"},
            {"label": "Geographic driver", "value": "Rural Norfolk drives postage + courier costs for pathology samples + meds delivery to remote north Norfolk + Fens sites"},
            {"label": "Funding trajectory", "value": "Flat to slightly declining as digital records reduce print volume; offset by mobile-telecoms growth and Royal Mail postage uprating"},
            {"label": "Delivery body", "value": "NCH&C Corporate Services + Procurement + IT/Digital + NHS Supply Chain (some commodity routes) + commercial telecoms providers (BT/Vodafone)"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Norfolk & Waveney ICB (host commissioner)"},
            {"label": "Evaluation evidence", "value": "NCH&C ARA; CQC provider profile (RY3); Model Hospital corporate-services benchmark; NHSE Operational Plan returns"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2011 Norfolk PCT establishment costs · Successor: digital-first community-care model under Three Shifts policy + integrated working with Norfolk & Waveney ICB"}
        ],
        "notes": "NCH&C operates across one of England's most rural counties, where the spread of community hospitals (Cromer, Swaffham, Beccles, Dereham, North Walsham) and clinics drives postage and courier costs for pathology samples and prescription delivery. Mobile telephony is increasingly the largest establishment-cost component as district nurses and neighbourhood teams move to mobile caseload management on SystmOne mobile / EMIS Mobile. The c. £1M baseline is consistent with mid-scale community trusts; expect flat to slightly rising trajectory as digital records continue to displace paper but mobile-data SIM growth and 2024-25 Royal Mail letter-pricing uprating apply upward pressure. Three Shifts policy may grow this baseline.",
        "sources": [
            {"publisher": "Norfolk Community Health and Care NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.norfolkcommunityhealthandcare.nhs.uk/about-us/our-publications/annual-reports/"},
            {"publisher": "Care Quality Commission", "title": "Norfolk Community Health and Care provider profile (RY3)", "url": "https://www.cqc.org.uk/provider/RY3"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Department of Health and Social Care", "title": "Independent investigation of the NHS in England (Darzi report, Sep 2024)", "url": "https://www.gov.uk/government/publications/independent-investigation-of-the-nhs-in-england"},
            {"publisher": "Norfolk & Waveney ICB", "title": "Norfolk and Waveney Integrated Care Board", "url": "https://improvinglivesnw.org.uk/"},
            {"publisher": "NHS England", "title": "Operational planning guidance 2024-25", "url": "https://www.england.nhs.uk/operational-planning-and-contracting/"}
        ],
        "related": ["Norfolk Community Health and Care NHS Trust", "Premises & Infrastructure", "NHS Community Trusts", "Establishment costs — Lincolnshire Community Health Services NHS Trust", "Establishment costs — Hertfordshire Community NHS Trust", "Norfolk and Waveney ICB"]
    },
    "Transport (business + patient) — Central London Community Healthcare NHS Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "Central London Community Healthcare NHS Trust"}],
        "description": "CLCH's £0.98M transport line covers staff business mileage (AMAP) for district nurses, MSK community physios, school nursing teams and intermediate-care teams travelling between c. 100+ community sites across nine North Central + North West London + South West London boroughs (Barnet, Camden, Hammersmith & Fulham, Harrow, Hounslow, Kensington & Chelsea, Merton, Westminster, Wandsworth in scope), plus leased pool-cars, ULEZ-compliance vehicle costs, and very limited PTS/HTCS transport reimbursements. ULEZ expansion to outer London (Aug 2023) accelerated fleet renewal pressures.",
        "beneficiaries": "Serves a c. 2.5M-resident North Central + NW + SW London community-care footprint across c. 9 boroughs; c. 100+ sites including Edgware Community Hospital, Athlone House, Soho Square, Parsons Green Health Centre, Finchley Memorial; c. 3,500 WTE incl. district nurses, school nurses, health visitors, MSK community physios.",
        "legal_basis": "NHS Act 2006 · Agenda for Change s.17 + HMRC Approved Mileage Allowance Payments · IFRS 16 Leases · Greater London Low Emission Zone (Mayoral) Regulations · ULEZ Variation Order 2023 (Aug 2023 outer London expansion) · DHSC Group Accounting Manual 2024-25",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£0.98M"},
            {"label": "Service footprint", "value": "c. 100+ community sites across c. 9 London boroughs incl. Edgware CH, Athlone House, Soho Square, Parsons Green HC, Finchley Memorial"},
            {"label": "Population served", "value": "c. 2.5M residents across NC + NW + SW London + parts of outer Herts (in scope)"},
            {"label": "Workforce", "value": "c. 3,500 WTE — district nurses, school nurses, health visitors, MSK community physios"},
            {"label": "Cost mix", "value": "Predominantly AMAP staff mileage + leased pool-cars + ULEZ-compliance vehicle running costs; minimal PTS/HTCS"},
            {"label": "ULEZ driver", "value": "Aug 2023 ULEZ expansion to outer London accelerated fleet-replacement pressure; Euro-6 diesel + EV transition"},
            {"label": "Geographic driver", "value": "Dense urban footprint with congestion-charge zone — different cost mix vs rural community trusts"},
            {"label": "Funding trajectory", "value": "Modest growth; IFRS 16 2022 lease re-recognition + AMAP mileage rebound + ULEZ-compliance fleet renewal"},
            {"label": "Delivery body", "value": "CLCH Estates & Facilities + leased-fleet supplier (NHS Fleet Solutions / commercial leasing) + boroughs (parking permits / loading bays)"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + multiple London ICBs (NCL ICB · NWL ICB · SWL ICB)"},
            {"label": "Evaluation evidence", "value": "CLCH ARA; CQC provider profile (RYX — Outstanding); Model Hospital community-services benchmarks; NHSE Operational Plan returns"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2011 NCL/NWL/SWL PCT-era community services merger · Successor: ULEZ-driven EV fleet transition + Three Shifts community-care expansion + Net Zero 2032 fleet electrification"}
        ],
        "notes": "CLCH is one of London's largest community trusts and operates across an unusually wide footprint (c. 9 London boroughs spanning NCL, NWL and SWL ICBs), giving rise to a transport baseline that combines heavy AMAP staff mileage with London-specific cost drivers — most notably the August 2023 ULEZ expansion to outer London, which accelerated fleet-replacement pressure as older diesel pool-cars became non-compliant. CQC has rated the trust 'Outstanding'. IFRS 16 2022 lease re-recognition lifted the baseline. Forward-looking drivers include the Three Shifts community-care expansion (Darzi report direction) which grows district-nursing caseload, and Net Zero 2032 fleet electrification (well-aligned with London EV-charging infrastructure).",
        "sources": [
            {"publisher": "Central London Community Healthcare NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://clch.nhs.uk/about-us/corporate-publications"},
            {"publisher": "Care Quality Commission", "title": "Central London Community Healthcare provider profile (RYX)", "url": "https://www.cqc.org.uk/provider/RYX"},
            {"publisher": "Transport for London", "title": "Ultra Low Emission Zone (ULEZ) — outer London expansion (Aug 2023)", "url": "https://tfl.gov.uk/modes/driving/ultra-low-emission-zone"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "NHS Net Zero — delivering a net zero NHS", "url": "https://www.england.nhs.uk/greenernhs/a-net-zero-nhs/"},
            {"publisher": "Department of Health and Social Care", "title": "Independent investigation of the NHS in England (Darzi report)", "url": "https://www.gov.uk/government/publications/independent-investigation-of-the-nhs-in-england"}
        ],
        "related": ["Central London Community Healthcare NHS Trust", "Premises & Infrastructure", "NHS Community Trusts", "Transport (business + patient) — Sussex Community NHS Foundation Trust", "Transport (business + patient) — Kent Community Health NHS Foundation Trust", "Transport for London"]
    },
    "Business rates — East Midlands Ambulance Service NHS Trust": {
        "aliases": [{"name": "Business rates", "parent": "East Midlands Ambulance Service NHS Trust"}],
        "description": "EMAS's £0.98M non-domestic-rates bill covers business rates payable on the trust's c. 70+ ambulance stations, hub-and-spoke deployment points, Make Ready Centres and HQ at 1 Horizon Place, Mellors Way (Nottingham). The estate spans Derbyshire, Leicestershire, Lincolnshire, Northamptonshire, Nottinghamshire and Rutland, with bills paid to multiple billing authorities under the Local Government Finance Act 1988. Most ambulance stations are owned freehold (some PFI-LIFT), some leased from NHSPS — a smaller estate footprint than acute trusts but spread over a wide geographic area.",
        "beneficiaries": "Serves a c. 4.8M population across the East Midlands (Derbyshire, Leicestershire, Lincolnshire, Northamptonshire, Nottinghamshire, Rutland); responds to c. 800,000 999 calls/yr; c. 4,000 WTE staff; c. 70+ ambulance stations + Make Ready Centres + HQ; c. 750 emergency vehicles.",
        "legal_basis": "Local Government Finance Act 1988 (Sch 6 — non-domestic rating) · Non-Domestic Rating Act 2023 · Non-Domestic Rating (Multipliers and Private Finance) Act 2024 · Valuation Office Agency 2023 rating list · DHSC Group Accounting Manual 2024-25",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£0.98M"},
            {"label": "Estate footprint", "value": "c. 70+ ambulance stations + Make Ready Centres + HQ at 1 Horizon Place, Mellors Way (Nottingham); mix of owned freehold + NHSPS-leased + LIFT"},
            {"label": "Geographic footprint", "value": "c. 13,500 km² across East Midlands — Derbyshire + Leics + Lincs + Northants + Notts + Rutland"},
            {"label": "Population served", "value": "c. 4.8M East Midlands residents"},
            {"label": "Workforce", "value": "c. 4,000 WTE; c. 750 emergency vehicles"},
            {"label": "999 call volume", "value": "c. 800,000 emergency calls/yr"},
            {"label": "Billing authorities", "value": "Multiple county + district + city authorities across 6 ceremonial counties — fragmented bill administration"},
            {"label": "VOA list cycle", "value": "2023 rating list (3-year cycle from 2026 revaluation under Non-Domestic Rating Act 2023)"},
            {"label": "NDR multiplier 2024-25", "value": "Standard 54.6p; healthcare estate generally on standard multiplier (no NHS exemption)"},
            {"label": "Funding trajectory", "value": "Rising c. 3-5%/yr in line with multiplier uprating + VOA 2023 revaluation; supplements multiplier increase under Non-Domestic Rating (Multipliers and Private Finance) Act 2024"},
            {"label": "Delivery body", "value": "EMAS Estates team + NHSPS for leased sites + LIFT-Co for any LIFT sites + relevant billing authorities + VOA"},
            {"label": "Policy owner", "value": "MHCLG (formerly DLUHC) + HM Treasury + DHSC + NHSE"},
            {"label": "Evaluation evidence", "value": "EMAS ARA; CQC provider profile (RX9 — Requires Improvement at last full inspection); NHSE Estates Returns Information Collection (ERIC) annual return"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2006 Derbys + Leics + Lincs + Northants + Notts ambulance services merger · Successor: 2026 VOA revaluation + ongoing Make Ready Centre estate consolidation + ARP3 deployment-point review"}
        ],
        "notes": "Ambulance trusts pay full non-domestic rates on their station estate with no NHS exemption. EMAS's c. £1M reflects a moderate-sized but geographically fragmented station footprint covering six East Midlands ceremonial counties. The trust is mid-cycle through Make Ready Centre estate consolidation that may reduce the long tail of small stations over time and concentrate the rates burden on fewer larger sites. The 2023 VOA rating-list revaluation lifted the baseline; the 2026 revaluation under the new 3-year cycle (Non-Domestic Rating Act 2023) and the supplementary multiplier under the Non-Domestic Rating (Multipliers and Private Finance) Act 2024 will apply further upward pressure. CQC last rated EMAS 'Requires Improvement' (urgent and emergency care).",
        "sources": [
            {"publisher": "East Midlands Ambulance Service NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.emas.nhs.uk/about-us/corporate-publications/"},
            {"publisher": "Valuation Office Agency", "title": "Find a business rates valuation (2023 rating list)", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "Care Quality Commission", "title": "East Midlands Ambulance Service provider profile (RX9)", "url": "https://www.cqc.org.uk/provider/RX9"},
            {"publisher": "UK Government", "title": "Non-Domestic Rating Act 2023", "url": "https://www.legislation.gov.uk/ukpga/2023/53"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Estates Returns Information Collection (ERIC) 2023-24", "url": "https://digital.nhs.uk/data-and-information/publications/statistical/estates-returns-information-collection"}
        ],
        "related": ["East Midlands Ambulance Service NHS Trust", "Premises & Infrastructure", "NHS Ambulance Trusts", "Business rates — London Ambulance Service NHS Trust", "Business rates — South East Coast Ambulance Service NHS Foundation Trust", "Valuation Office Agency"]
    },
    "Business rates — Wirral Community Health and Care NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "Wirral Community Health and Care NHS Foundation Trust"}],
        "description": "Wirral CHCT's £0.98M non-domestic-rates bill covers business rates payable on the trust's owned and leased community estate across the Wirral peninsula plus services in Cheshire East and beyond — including St Catherine's Health Centre (Birkenhead), Victoria Central Health Centre (Wallasey), Eastham Clinic, Hoylake & Meols, Heswall and a long tail of clinics. Bills are paid to Wirral MBC and other relevant billing authorities under the Local Government Finance Act 1988. Unusually for community FTs, Wirral CHCT also operates 0-19 services in Cheshire East and out-of-hours services through Wirral Community Health and Care.",
        "beneficiaries": "Serves the c. 320,000 Wirral population (one of England's smaller community-trust catchments) plus 0-19 Children's Public Health services in Cheshire East (c. 380,000); operates from c. 25+ owned/leased sites including St Catherine's HC (Birkenhead), Victoria Central HC (Wallasey), Eastham Clinic; c. 1,300 WTE incl. district nurses, school nurses, health visitors and 0-19 teams.",
        "legal_basis": "Local Government Finance Act 1988 (Sch 6 — non-domestic rating) · Non-Domestic Rating Act 2023 · Non-Domestic Rating (Multipliers and Private Finance) Act 2024 · Valuation Office Agency 2023 rating list · DHSC Group Accounting Manual 2024-25",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£0.98M"},
            {"label": "Estate footprint", "value": "c. 25+ owned/leased sites incl. St Catherine's HC (Birkenhead), Victoria Central HC (Wallasey), Eastham Clinic, Hoylake & Meols, Heswall"},
            {"label": "Population served", "value": "c. 320,000 Wirral residents + c. 380,000 Cheshire East 0-19 service catchment"},
            {"label": "Workforce", "value": "c. 1,300 WTE — district nurses, school nurses, health visitors, 0-19 teams, AHPs"},
            {"label": "Billing authorities", "value": "Wirral MBC main + Cheshire East Council for Cheshire East 0-19 service estate"},
            {"label": "VOA list cycle", "value": "2023 rating list (3-year cycle from 2026 revaluation under Non-Domestic Rating Act 2023)"},
            {"label": "NDR multiplier 2024-25", "value": "Standard 54.6p; healthcare estate generally on standard multiplier (no NHS exemption)"},
            {"label": "Cross-border element", "value": "Cheshire East 0-19 services contract drives multi-LA estate footprint atypical for small community FT"},
            {"label": "Funding trajectory", "value": "Rising c. 3-5%/yr in line with multiplier uprating + VOA 2023 revaluation; supplements multiplier increase under Non-Domestic Rating (Multipliers and Private Finance) Act 2024"},
            {"label": "Delivery body", "value": "Wirral CHCT Estates team + NHSPS for some leased sites + Wirral MBC + Cheshire East Council billing authorities + VOA"},
            {"label": "Policy owner", "value": "MHCLG (formerly DLUHC) + HM Treasury + DHSC + NHSE + Cheshire & Merseyside ICB host"},
            {"label": "Evaluation evidence", "value": "Wirral CHCT ARA; CQC provider profile (RY7); NHSE Estates Returns Information Collection (ERIC) annual return"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2011 Wirral PCT + 2018 FT authorisation · Successor: 2026 VOA revaluation + ongoing community-services integration with the Cheshire & Merseyside provider collaborative"}
        ],
        "notes": "Wirral CHCT is one of England's smaller standalone community foundation trusts (turnover c. £85M) and operates an unusual cross-border footprint — community services for Wirral plus the Cheshire East 0-19 Children's Public Health contract — which expands the estate beyond the Wirral peninsula. NHS bodies receive no NDR mandatory relief (unlike charities), so the full liability flows. The 2023 VOA rating-list revaluation lifted the baseline, and the 2026 revaluation under the 3-year cycle plus the new supplementary multiplier under the Non-Domestic Rating (Multipliers and Private Finance) Act 2024 will apply further upward pressure. Three Shifts community-care policy direction may grow the estate further.",
        "sources": [
            {"publisher": "Wirral Community Health and Care NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.wchc.nhs.uk/about-us/corporate-publications/"},
            {"publisher": "Valuation Office Agency", "title": "Find a business rates valuation (2023 rating list)", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "Care Quality Commission", "title": "Wirral Community Health and Care provider profile (RY7)", "url": "https://www.cqc.org.uk/provider/RY7"},
            {"publisher": "UK Government", "title": "Non-Domestic Rating (Multipliers and Private Finance) Act 2024", "url": "https://www.legislation.gov.uk/ukpga/2024/16"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Estates Returns Information Collection (ERIC) 2023-24", "url": "https://digital.nhs.uk/data-and-information/publications/statistical/estates-returns-information-collection"}
        ],
        "related": ["Wirral Community Health and Care NHS Foundation Trust", "Premises & Infrastructure", "NHS Community Trusts", "Business rates — Derbyshire Community Health Services NHS Foundation Trust", "Business rates — Hertfordshire Community NHS Trust", "Valuation Office Agency"]
    },
    "Drugs costs — Norfolk Community Health and Care NHS Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "Norfolk Community Health and Care NHS Trust"}],
        "description": "NCH&C's £0.97M drugs costs line covers community-administered medicines stock — predominantly vaccination programmes (school-age immunisations including HPV, flu, MMR catch-up), end-of-life community palliative anticipatory-care kits for district nursing, intermediate-care medicines used in the trust's community hospitals at North Walsham/Cromer/Swaffham/Beccles/Dereham, community-IV antibiotic services, and community-diabetes insulin/devices. Most prescribing flows through community pharmacy primary-care budgets — this line covers stock dispensed and administered directly by trust clinicians.",
        "beneficiaries": "Serves the c. 925,000 Norfolk population through district nursing, school nursing, health visiting, intermediate care, community hospitals (North Walsham, Cromer, Swaffham, Beccles, Dereham), community-IV antibiotics and end-of-life community care; c. 2,500 WTE incl. district nurses, school nurses, health visitors and AHPs.",
        "legal_basis": "NHS Act 2006 (Drug Tariff) · Branded Medicines Pricing Scheme · Voluntary Scheme for Branded Medicines Pricing Access and Growth (VPAG) 2024 · Human Medicines Regulations 2012 · DHSC Group Accounting Manual 2024-25",
        "key_stats": [
            {"label": "Drugs costs 2024-25", "value": "£0.97M"},
            {"label": "Population served", "value": "c. 925,000 Norfolk residents (excl. Great Yarmouth/Waveney)"},
            {"label": "Service footprint", "value": "Community hospitals (5 sites), district nursing, school nursing, health visiting, intermediate care, end-of-life, community-IV antibiotics"},
            {"label": "Community hospital beds", "value": "c. 280 beds across North Walsham, Cromer, Swaffham, Beccles, Dereham — community-hospital prescribing flows through this line"},
            {"label": "Workforce", "value": "c. 2,500 WTE — district nurses, school nurses, health visitors, AHPs, community-hospital teams"},
            {"label": "Drugs mix", "value": "School-age immunisations (HPV, flu, MMR), community-hospital intermediate-care meds, anticipatory-care end-of-life kits, community-IV antibiotics, diabetes insulin/devices"},
            {"label": "Procurement route", "value": "NHS Supply Chain Pharmacy Tower + UKHSA-supplied centrally-procured vaccines (e.g. flu, HPV — flow varies)"},
            {"label": "Community-IV driver", "value": "OPAT (Outpatient Parenteral Antimicrobial Therapy) and community-IV antibiotic services drive antibiotic + giving-set stock"},
            {"label": "Funding trajectory", "value": "Rising in line with vaccination-programme expansion (RSV adult Sept 2024, MMR catch-up), VPAG 2024 contributions and end-of-life community-care growth"},
            {"label": "Delivery body", "value": "NCH&C Pharmacy + Procurement + School-Age Immunisation team + community-nursing teams + NHS Supply Chain (Pharmacy Tower)"},
            {"label": "Policy owner", "value": "NHSE Vaccinations & Screening + DHSC + UKHSA (centrally procured vaccines) + Norfolk & Waveney ICB (host commissioner)"},
            {"label": "Evaluation evidence", "value": "NCH&C ARA; CQC provider profile (RY3); UKHSA vaccination-coverage statistics (COVER); School-Age Immunisation national audits; OPAT national audit"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2011 Norfolk PCT community-medicines budget · Successor: RSV adult vaccination programme (Sept 2024 rollout) + community-virtual-ward expansion + Three Shifts community-care growth"}
        ],
        "notes": "Norfolk CH&C carries a slightly higher drug-stock baseline than peer community trusts of similar size because it operates five community hospitals (c. 280 inpatient beds in North Walsham, Cromer, Swaffham, Beccles and Dereham) that draw routine inpatient medicines through this line, alongside the community-IV antibiotic / OPAT service that drives antibiotic and giving-set stock turnover. UKHSA centrally procures most vaccines and supplies in kind, so the line largely reflects locally-purchased adjuncts plus inpatient and community-administered medicines under the Drug Tariff. The new RSV adult vaccination programme (September 2024 rollout), MMR catch-up campaign and Three Shifts community-virtual-ward expansion are forward-looking growth drivers. VPAG 2024 contributions and drug-tariff inflation add modest upward pressure.",
        "sources": [
            {"publisher": "Norfolk Community Health and Care NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.norfolkcommunityhealthandcare.nhs.uk/about-us/our-publications/annual-reports/"},
            {"publisher": "UK Health Security Agency", "title": "Cover of Vaccination Evaluated Rapidly (COVER) statistics", "url": "https://www.gov.uk/government/collections/vaccine-uptake"},
            {"publisher": "Care Quality Commission", "title": "Norfolk Community Health and Care provider profile (RY3)", "url": "https://www.cqc.org.uk/provider/RY3"},
            {"publisher": "Department of Health and Social Care", "title": "Voluntary Scheme for Branded Medicines Pricing Access and Growth (VPAG) 2024", "url": "https://www.gov.uk/government/publications/voluntary-scheme-for-branded-medicines-pricing-access-and-growth-vpag"},
            {"publisher": "NHS England", "title": "RSV vaccination programme (Sept 2024)", "url": "https://www.england.nhs.uk/2024/06/nhs-prepares-to-roll-out-historic-vaccination-programme-against-deadly-virus/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"}
        ],
        "related": ["Norfolk Community Health and Care NHS Trust", "Clinical Supplies & Drugs", "NHS Community Trusts", "Drugs costs — Leeds Community Healthcare NHS Trust", "Drugs costs — Hertfordshire Community NHS Trust", "UK Health Security Agency"]
    },
}
