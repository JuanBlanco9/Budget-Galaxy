# -*- coding: utf-8 -*-
"""Phase 2 SCamb chunk 10 — 17 NHS Specialist/Community/Ambulance Trust orphan sub-lines."""

NEW = {
    "Establishment costs — Royal Papworth Hospital NHS Foundation Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "Royal Papworth Hospital NHS Foundation Trust"}],
        "description": "Establishment costs at Royal Papworth Hospital NHS Foundation Trust — telephony, postage, audit, training, advertising and indirect non-payroll non-clinical overhead. Royal Papworth is the UK's leading heart and lung tertiary centre, relocated to a new build on the Cambridge Biomedical Campus in 2019 and adjacent to Addenbrooke's. It performs the highest UK volume of heart and lung transplants and runs the national PVD service. The £1.96M overhead reflects a single-site specialist footprint with high research-active correspondence and recruitment volumes.",
        "beneficiaries": "~2,200 WTE serving a supra-regional/national catchment with ~120,000 outpatient attendances and ~22,000 inpatient/daycase episodes per year, including the UK's largest transplant programme.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Establishment costs 2023-24", "value": "£1.96M"},
            {"label": "Parent line", "value": "Premises & Infrastructure"},
            {"label": "Trust category", "value": "NHS Specialist (heart + lung)"},
            {"label": "Site", "value": "Cambridge Biomedical Campus (opened 2019)"},
            {"label": "WTE staff", "value": "~2,200"},
            {"label": "Annual outpatients", "value": "~120,000"},
            {"label": "Heart + lung transplants/year", "value": "~150 (largest UK volume)"},
            {"label": "ICS", "value": "Cambridgeshire and Peterborough ICB (host)"},
            {"label": "Commissioning route", "value": "NHSE Specialised Commissioning"},
            {"label": "Foundation Trust authorised", "value": "2004"},
            {"label": "CQC most recent rating", "value": "Outstanding (2019)"},
            {"label": "PFI status", "value": "New hospital under PFI (Equitix consortium)"}
        ],
        "notes": "Delivery body: Papworth Corporate Services + Procurement, with SBS for finance back-office and CUH-shared service partnerships on the campus. Policy owner: NHSE Specialised Commissioning sets the service envelope (cardiac surgery, transplantation, PVD); DHSC for GAM treatment. Funding trajectory: rising — post-pandemic transplant activity recovery, restart of complex cardiac surgery and the inflationary uplift on telephony and recruitment advertising drove growth, partly offset by efficiency on a younger digital estate. April 2025 employer NIC step-up (15% / £5k threshold) raises the embedded social-security overhead in establishment-adjacent recharges. Evaluation: CQC Outstanding (2019), Model Hospital benchmarks vs RBHT and Liverpool Heart and Chest, and NHSE Operational Plan returns. Predecessor: Papworth Everard rural site (1918-2019); successor: deeper integration with Cambridge University Hospitals on the Biomedical Campus and joint research with University of Cambridge / AstraZeneca.",
        "sources": [
            {"publisher": "Royal Papworth Hospital NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://royalpapworth.nhs.uk/about-us/our-publications"},
            {"publisher": "Care Quality Commission", "title": "Royal Papworth Hospital inspection reports", "url": "https://www.cqc.org.uk/provider/RGM"},
            {"publisher": "NHS England", "title": "Specialised commissioning — cardiothoracic services", "url": "https://www.england.nhs.uk/commissioning/spec-services/"},
            {"publisher": "DHSC", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS Blood and Transplant", "title": "Annual report on heart and lung transplantation", "url": "https://www.odt.nhs.uk/statistics-and-reports/annual-activity-report/"}
        ],
        "related": ["Premises & Infrastructure — Royal Papworth Hospital NHS Foundation Trust", "Royal Papworth Hospital NHS Foundation Trust", "NHS England Specialised Commissioning", "Cambridge University Hospitals NHS Foundation Trust", "PFI / LIFT charges — Royal Papworth Hospital NHS Foundation Trust"]
    },
    "Transport (business + patient) — Cambridgeshire Community Services NHS Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "Cambridgeshire Community Services NHS Trust"}],
        "description": "Business and patient transport at Cambridgeshire Community Services NHS Trust (CCS) — staff mileage (AMAP), pool fleet, IFRS 16 right-of-use vehicles, taxi and patient travel costs. CCS is a stand-alone community provider serving Cambridgeshire, Peterborough, Luton, Bedfordshire, Norfolk and Suffolk via children's services, MSK, dental, sexual health, immunisations and 0-19. Its £1.95M transport line reflects a heavy district-nursing and health-visiting fleet operating across a large rural geography stretching from the Fens to Bedfordshire.",
        "beneficiaries": "~3,200 WTE serving ~3.0M residents across Cambs/Peterborough/Beds/Luton/Norfolk/Suffolk via ~1.7M annual community contacts, with hundreds of community nurses driving daily.",
        "legal_basis": "NHS Act 2006 · NHSE Patient Transport Services Eligibility · AfC s.17 Mileage + HMRC AMAP rates · IFRS 16 Leases (pool fleet) · Health and Care Act 2022",
        "key_stats": [
            {"label": "Transport (business + patient) 2023-24", "value": "£1.95M"},
            {"label": "Parent line", "value": "Premises & Infrastructure"},
            {"label": "Trust category", "value": "NHS Community"},
            {"label": "Catchment population", "value": "~3.0M (multi-county)"},
            {"label": "WTE staff", "value": "~3,200"},
            {"label": "Annual contacts", "value": "~1.7M"},
            {"label": "Geographic spread", "value": "Cambs/Peterborough/Luton/Beds/Norfolk/Suffolk"},
            {"label": "AMAP rate", "value": "45p/mile to 10,000mi · 25p thereafter"},
            {"label": "Lead ICS", "value": "Cambridgeshire and Peterborough ICB"},
            {"label": "0-19 contracts", "value": "Cambs, Peterborough, Suffolk, Norfolk, Luton"},
            {"label": "CQC most recent rating", "value": "Good"},
            {"label": "Trust authorised", "value": "2010"}
        ],
        "notes": "Delivery body: CCS Fleet/Estates and HR (mileage claims via ESR), with leased pool vehicles via NHS Fleet Solutions / Tusker / Lex Autolease frameworks. Policy owner: NHSE Provider Finance for envelope; Cambs and Peterborough ICB as host commissioner; HMRC sets AMAP rates (frozen at 45p/25p since 2011 — a real-terms cut). Funding trajectory: rising — district-nurse caseload growth, virtual-ward visits and Three Shifts (Darzi Sep 2024) push fleet utilisation up, while fuel and IFRS 16 (2022-23 transition) lifted the line. April 2025 employer NIC step-up affects mileage gross-ups. Evaluation: CQC Good, NHSE Operational Plan returns, internal Model Hospital fleet benchmarks. Predecessor: spun out from NHS Cambridgeshire PCT 2010; successor: closer integration with Cambridgeshire and Peterborough NHS FT and Norfolk Community on cross-county MSK and 0-19 lots.",
        "sources": [
            {"publisher": "Cambridgeshire Community Services NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.cambscommunityservices.nhs.uk/about-us/publications/annual-reports"},
            {"publisher": "HMRC", "title": "Approved Mileage Allowance Payments (AMAP)", "url": "https://www.gov.uk/government/publications/rates-and-allowances-travel-mileage-and-fuel-allowances"},
            {"publisher": "NHS Employers", "title": "Agenda for Change Section 17 — mileage", "url": "https://www.nhsemployers.org/publications/tchandbook"},
            {"publisher": "Care Quality Commission", "title": "Cambridgeshire Community Services NHS Trust", "url": "https://www.cqc.org.uk/provider/RYV"},
            {"publisher": "Lord Darzi", "title": "Independent Investigation of the NHS in England (Sep 2024)", "url": "https://www.gov.uk/government/publications/independent-investigation-of-the-nhs-in-england"}
        ],
        "related": ["Premises & Infrastructure — Cambridgeshire Community Services NHS Trust", "Cambridgeshire Community Services NHS Trust", "Cambridgeshire and Peterborough ICB", "Lord Darzi Independent Investigation 2024", "Social security & levy — Cambridgeshire Community Services NHS Trust"]
    },
    "PFI / LIFT charges — Northamptonshire Healthcare NHS Foundation Trust": {
        "aliases": [{"name": "PFI / LIFT charges", "parent": "Northamptonshire Healthcare NHS Foundation Trust"}],
        "description": "PFI / LIFT charges at Northamptonshire Healthcare NHS Foundation Trust (NHFT) — unitary payments and on-balance-sheet IFRS 16 reclassified service charges on legacy NHS LIFT (Local Improvement Finance Trust) primary-care and community estate built across Northamptonshire from the early 2000s. NHFT is a combined community + mental health provider operating from a network of LIFT-built health centres and CCG-era hubs; the £1.90M reflects ongoing service-element charges to the SPV concessionaires under 25-year DBFO contracts.",
        "beneficiaries": "~4,800 WTE delivering services from a network of LIFT-built community and mental-health hubs serving ~770,000 Northamptonshire residents.",
        "legal_basis": "IFRIC 12 Service Concession Arrangements · IFRS 16 Leases (post-2022 reclassification) · DHSC PFI/LIFT guidance · DHSC Group Accounting Manual 2024-25 · NHS LIFT framework agreements (DH 2001)",
        "key_stats": [
            {"label": "PFI / LIFT charges 2023-24", "value": "£1.90M"},
            {"label": "Parent line", "value": "Premises & Infrastructure"},
            {"label": "Trust category", "value": "NHS Community + Mental Health"},
            {"label": "Catchment population", "value": "~770,000 (Northamptonshire)"},
            {"label": "ICS", "value": "Northamptonshire ICB"},
            {"label": "WTE staff", "value": "~4,800"},
            {"label": "Scheme type", "value": "NHS LIFT (DH 2001 programme)"},
            {"label": "Concession length", "value": "25 years typical"},
            {"label": "Reporting standard", "value": "IFRIC 12 + IFRS 16 (2022 transition)"},
            {"label": "Counterparty", "value": "LIFT Co. SPV (Community Health Partnerships shareholder)"},
            {"label": "Foundation Trust authorised", "value": "2009"},
            {"label": "Successor vehicle", "value": "NHS-owned blocks via CHP / NHSPS"}
        ],
        "notes": "Delivery body: NHFT Estates and Facilities, with charges paid to the Northamptonshire LIFT Company (SPV) and Community Health Partnerships (CHP) as DH-owned shareholder. Policy owner: DHSC PFI/LIFT policy team; NHSE Provider Finance for envelope; HM Treasury PUK / IPA for guidance on PFI exits. Funding trajectory: broadly flat in cash, with the IFRS 16 reclassification in 2022-23 lifting the on-balance-sheet element; concessions roll off through the late 2020s and early 2030s, after which the buildings revert to the Trust / CHP. April 2025 employer NIC step-up indirectly affects facilities sub-contractor pricing within unitary payments. Evaluation: NAO PFI report (HC 718, 2018) on PFI value-for-money; NHSE PFI/LIFT register; CQC Good. Predecessor: legacy primary-care premises pre-LIFT (2001-onwards builds replaced fragmented PCT estate); successor: NHS-owned and NHSPS-leased model post-concession-end, with Three Shifts (Darzi Sep 2024) emphasising community estate utilisation.",
        "sources": [
            {"publisher": "Northamptonshire Healthcare NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.nhft.nhs.uk/about-us/publications-and-reports/"},
            {"publisher": "Community Health Partnerships", "title": "About LIFT and the LIFT estate", "url": "https://www.communityhealthpartnerships.co.uk/our-properties/"},
            {"publisher": "DHSC", "title": "Group Accounting Manual 2024-25 (PFI/IFRS 16)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "National Audit Office", "title": "PFI and PF2 (HC 718, 2018)", "url": "https://www.nao.org.uk/reports/pfi-and-pf2/"},
            {"publisher": "HM Treasury", "title": "Private Finance Initiative and PF2 guidance", "url": "https://www.gov.uk/government/collections/public-private-partnerships"}
        ],
        "related": ["Premises & Infrastructure — Northamptonshire Healthcare NHS Foundation Trust", "Northamptonshire Healthcare NHS Foundation Trust", "Community Health Partnerships", "Northamptonshire ICB", "NAO PFI report 2018"]
    },
    "Establishment costs — Sheffield Children's NHS Foundation Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "Sheffield Children's NHS Foundation Trust"}],
        "description": "Establishment costs at Sheffield Children's NHS Foundation Trust — telephony, postage, audit, training, advertising and indirect non-payroll non-clinical overhead. SCFT is one of only four stand-alone children's hospitals in the UK, providing tertiary paediatric services from Western Bank to a supra-regional catchment across South Yorkshire, North Derbyshire, North Nottinghamshire and Lincolnshire. The £1.85M overhead reflects research-active, training-intensive operations (including the Becton site for community CAMHS and child & adolescent mental health) plus the new Acorn Surgical Centre.",
        "beneficiaries": "~3,800 WTE serving a supra-regional paediatric catchment of ~3.5M children with ~270,000 outpatient attendances and ~30,000 inpatient/daycase episodes a year.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Establishment costs 2023-24", "value": "£1.85M"},
            {"label": "Parent line", "value": "Premises & Infrastructure"},
            {"label": "Trust category", "value": "NHS Specialist (paediatric)"},
            {"label": "Sites", "value": "Western Bank · Becton · Ryegate · Centenary Wing · Acorn Surgical Centre (2024)"},
            {"label": "WTE staff", "value": "~3,800"},
            {"label": "Annual outpatients", "value": "~270,000"},
            {"label": "Catchment", "value": "South Yorks/N Derbyshire/N Notts/Lincs ~3.5M children"},
            {"label": "Lead ICS", "value": "South Yorkshire ICB"},
            {"label": "Commissioning route", "value": "NHSE Specialised Commissioning (tertiary paeds)"},
            {"label": "Foundation Trust authorised", "value": "2006"},
            {"label": "CQC most recent rating", "value": "Good"},
            {"label": "Charity partner", "value": "The Children's Hospital Charity (helipad funded 2017)"}
        ],
        "notes": "Delivery body: SCFT Corporate Services + Procurement, with NHS Supply Chain frameworks for routine items and shared back-office with Sheffield Teaching Hospitals on selected functions. Policy owner: NHSE Specialised Commissioning sets the tertiary paediatric envelope; DHSC for GAM treatment; Yorkshire and Humber Children's CDC programme for diagnostic capacity. Funding trajectory: rising — opening of the Acorn Surgical Centre in 2024 (paediatric day-case capacity) lifted training, signage and recruitment establishment lines, and inflation passthrough on telephony and audit fees continued. April 2025 employer NIC step-up (15% / £5k threshold) raises social-security gross-ups in establishment-adjacent recharges. Evaluation: CQC Good, NHSE Operational Plan returns, Model Hospital benchmarks vs GOSH, Alder Hey and Birmingham Children's. Predecessor: founded 1876 on Western Bank; successor: continuing capital programme post-Acorn and deeper ICS integration on community paediatrics with Sheffield Teaching Hospitals.",
        "sources": [
            {"publisher": "Sheffield Children's NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.sheffieldchildrens.nhs.uk/about-us/publications/"},
            {"publisher": "Care Quality Commission", "title": "Sheffield Children's NHSFT inspection reports", "url": "https://www.cqc.org.uk/provider/RCU"},
            {"publisher": "NHS England", "title": "Specialised commissioning — paediatric services", "url": "https://www.england.nhs.uk/commissioning/spec-services/"},
            {"publisher": "DHSC", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "South Yorkshire ICB", "title": "South Yorkshire ICS plans", "url": "https://syics.co.uk/"}
        ],
        "related": ["Premises & Infrastructure — Sheffield Children's NHS Foundation Trust", "Sheffield Children's NHS Foundation Trust", "NHS England Specialised Commissioning", "South Yorkshire ICB", "Social security & levy — Sheffield Children's NHS Foundation Trust"]
    },
    "Establishment costs — Derbyshire Community Health Services NHS Foundation Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "Derbyshire Community Health Services NHS Foundation Trust"}],
        "description": "Establishment costs at Derbyshire Community Health Services NHS Foundation Trust (DCHS) — telephony, postage, audit, training, advertising, courier and indirect non-payroll non-clinical overhead. DCHS is a stand-alone community provider serving the city of Derby and the largely rural county of Derbyshire (incl. the Peak District) from a network of 11 community hospitals plus health centres. The £1.85M reflects a dispersed rural footprint with high postage and travel-letter print volumes and recruitment-advertising spend across a tight midlands labour market.",
        "beneficiaries": "~4,500 WTE serving the ~1.06M residents of Derby and Derbyshire from 11 community hospitals and 30+ health centres, with ~3M annual community contacts.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Establishment costs 2023-24", "value": "£1.85M"},
            {"label": "Parent line", "value": "Premises & Infrastructure"},
            {"label": "Trust category", "value": "NHS Community"},
            {"label": "Catchment population", "value": "~1.06M (Derby + Derbyshire)"},
            {"label": "WTE staff", "value": "~4,500"},
            {"label": "Annual contacts", "value": "~3.0M"},
            {"label": "Community hospitals", "value": "11 (incl. Walton, Ilkeston, Ashbourne, Buxton)"},
            {"label": "Geography", "value": "City + Peak District + commuter belt"},
            {"label": "ICS", "value": "Joined Up Care Derbyshire ICB"},
            {"label": "Foundation Trust authorised", "value": "2014"},
            {"label": "CQC most recent rating", "value": "Outstanding (2018, sustained 2022)"},
            {"label": "Estate landlord (much of)", "value": "NHS Property Services"}
        ],
        "notes": "Delivery body: DCHS Estates and Facilities + Procurement, with NHS Supply Chain category management and corporate-services partnerships across the Joined Up Care Derbyshire ICS. Policy owner: NHSE Provider Finance for envelope; Joined Up Care Derbyshire ICB as commissioner; DHSC for GAM treatment. Funding trajectory: broadly flat in real terms, with rural overhead (postage, mileage to remote Peak District patches) structurally elevated and the Three Shifts policy (Darzi Sep 2024) plus virtual-ward expansion pushing modest growth. April 2025 employer NIC step-up affects sub-contractor pricing within establishment recharges. Evaluation: CQC Outstanding (2018, sustained on 2022 review); NHSE Operational Plan returns; Model Hospital benchmarks vs Lincolnshire Community and Sussex Community. Predecessor: spun out from Derbyshire County PCT in 2011, FT 2014; successor: tighter ICS-level integration with University Hospitals of Derby and Burton (UHDB) and Chesterfield Royal on community pathways.",
        "sources": [
            {"publisher": "Derbyshire Community Health Services NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.dchs.nhs.uk/about-us/publications-and-policies/annual-reports-and-accounts"},
            {"publisher": "Care Quality Commission", "title": "DCHS NHSFT inspection reports", "url": "https://www.cqc.org.uk/provider/RY8"},
            {"publisher": "DHSC", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Joined Up Care Derbyshire ICB", "title": "ICS plans and priorities", "url": "https://joinedupcarederbyshire.co.uk/"},
            {"publisher": "Lord Darzi", "title": "Independent Investigation of the NHS in England (Sep 2024)", "url": "https://www.gov.uk/government/publications/independent-investigation-of-the-nhs-in-england"}
        ],
        "related": ["Premises & Infrastructure — Derbyshire Community Health Services NHS Foundation Trust", "Derbyshire Community Health Services NHS Foundation Trust", "Joined Up Care Derbyshire ICB", "NHS Property Services", "Social security & levy — Derbyshire Community Health Services NHS Foundation Trust"]
    },
    "Establishment costs — Liverpool Heart and Chest Hospital NHS Foundation Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "Liverpool Heart and Chest Hospital NHS Foundation Trust"}],
        "description": "Establishment costs at Liverpool Heart and Chest Hospital NHS Foundation Trust (LHCH) — telephony, postage, audit, training, advertising and indirect non-payroll non-clinical overhead. LHCH is a single-site cardiothoracic specialist trust at Broadgreen, Liverpool, performing the second-largest UK volume of cardiac surgery and a major thoracic and respiratory programme. The £1.83M reflects a research-active footprint with significant patient-correspondence volumes from a Cheshire/Mersey supra-regional catchment and shared corporate services with the Liverpool University Hospitals system.",
        "beneficiaries": "~1,800 WTE serving a supra-regional catchment of ~2.8M across Cheshire and Merseyside via ~85,000 outpatient attendances and ~14,000 inpatient/daycase episodes a year.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Establishment costs 2023-24", "value": "£1.83M"},
            {"label": "Parent line", "value": "Premises & Infrastructure"},
            {"label": "Trust category", "value": "NHS Specialist (heart + lung)"},
            {"label": "Site", "value": "Broadgreen, Liverpool (single site)"},
            {"label": "WTE staff", "value": "~1,800"},
            {"label": "Annual outpatients", "value": "~85,000"},
            {"label": "Cardiac surgery volume", "value": "2nd largest in UK"},
            {"label": "Catchment", "value": "Cheshire + Merseyside ~2.8M"},
            {"label": "ICS", "value": "Cheshire and Merseyside ICB"},
            {"label": "Commissioning route", "value": "NHSE Specialised Commissioning"},
            {"label": "Foundation Trust authorised", "value": "2009"},
            {"label": "CQC most recent rating", "value": "Outstanding (2019)"}
        ],
        "notes": "Delivery body: LHCH Corporate Services + Procurement, with shared back-office across the Cheshire and Merseyside cardiac and thoracic networks and NHS Supply Chain frameworks. Policy owner: NHSE Specialised Commissioning sets the cardiothoracic envelope; DHSC for GAM treatment; Cheshire and Merseyside ICB hosts the system board. Funding trajectory: rising — post-pandemic activity recovery, restart of complex cardiac surgery and inflation passthrough on telephony, audit and training drove growth, partly offset by efficiencies on a digitised estate. April 2025 employer NIC step-up (15% / £5k threshold) affects the social-security gross-ups in establishment-adjacent recharges. Evaluation: CQC Outstanding (2019), Model Hospital benchmarks vs Royal Papworth and Royal Brompton & Harefield, NHSE Operational Plan returns. Predecessor: long-standing single-site cardiothoracic centre on Thomas Drive (Broadgreen); successor: ongoing CathLab modernisation and cardiac network leadership across Cheshire/Merseyside.",
        "sources": [
            {"publisher": "Liverpool Heart and Chest Hospital NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.lhch.nhs.uk/about-us/publications/"},
            {"publisher": "Care Quality Commission", "title": "LHCH inspection reports", "url": "https://www.cqc.org.uk/provider/RBQ"},
            {"publisher": "NHS England", "title": "Specialised commissioning — cardiothoracic services", "url": "https://www.england.nhs.uk/commissioning/spec-services/"},
            {"publisher": "DHSC", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Cheshire and Merseyside ICB", "title": "ICS plans", "url": "https://www.cheshireandmerseyside.nhs.uk/"}
        ],
        "related": ["Premises & Infrastructure — Liverpool Heart and Chest Hospital NHS Foundation Trust", "Liverpool Heart and Chest Hospital NHS Foundation Trust", "NHS England Specialised Commissioning", "Cheshire and Merseyside ICB", "Social security & levy — Liverpool Heart and Chest Hospital NHS Foundation Trust"]
    },
    "Business rates — Gloucestershire Health and Care NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "Gloucestershire Health and Care NHS Foundation Trust"}],
        "description": "Business rates (non-domestic rates) at Gloucestershire Health and Care NHS Foundation Trust (GHC) — annual liability under the Local Government Finance Act 1988 on community hospitals, mental-health units and outpatient sites across Gloucestershire. GHC is a combined community + mental health provider serving the county from a network of seven community hospitals plus inpatient mental-health and learning-disability units. The £1.80M rates bill reflects rateable values across a dispersed estate with no NHS-specific exemption.",
        "beneficiaries": "~5,000 WTE delivering services from 7 community hospitals and 50+ sites to ~640,000 Gloucestershire residents.",
        "legal_basis": "Local Government Finance Act 1988 (Schedule 6) · Non-Domestic Rating (Multipliers and Private Finance) Act 2024 · DHSC Group Accounting Manual 2024-25 · Charities Act mandatory relief (n/a — NHS not a charity)",
        "key_stats": [
            {"label": "Business rates 2023-24", "value": "£1.80M"},
            {"label": "Parent line", "value": "Premises & Infrastructure"},
            {"label": "Trust category", "value": "NHS Community + Mental Health"},
            {"label": "Catchment population", "value": "~640,000 (Gloucestershire)"},
            {"label": "WTE staff", "value": "~5,000"},
            {"label": "Community hospitals", "value": "7 (incl. Stroud, Cirencester, Tewkesbury, Dilke, Lydney, Vale, North Cotswolds)"},
            {"label": "ICS", "value": "One Gloucestershire ICB"},
            {"label": "Multiplier 2024-25", "value": "54.6p (standard) / 49.9p (small)"},
            {"label": "Billing authority", "value": "Multiple Gloucestershire district councils"},
            {"label": "VOA list", "value": "2023 rating list (in force from April 2023)"},
            {"label": "Foundation Trust authorised", "value": "2019 (community + MH merger)"},
            {"label": "CQC most recent rating", "value": "Good"}
        ],
        "notes": "Delivery body: GHC Estates and Facilities, with rates bills issued by Stroud DC, Tewkesbury BC, Cotswold DC, Forest of Dean DC, Cheltenham BC, Gloucester City and Stroud DC and assessed by the Valuation Office Agency (VOA) on the 2023 rating list. Policy owner: HMT and DLUHC set multipliers and reliefs (Non-Domestic Rating Act 2024 introduced lower multipliers for some retail/hospitality and a new high-multiplier for £500k+ properties); DHSC for GAM treatment. Funding trajectory: rising — annual multiplier uplift (CPI-linked) and the 2023 list revaluation lifted bills; transitional relief tapers. April 2025 employer NIC step-up adds indirect cost pressure across the estate but is separate. Evaluation: CQC Good; NHSE Operational Plan returns; Model Hospital estate benchmarks. Predecessor: GHC formed 2019 from merger of 2gether (MH) and Glos Care Services (community); successor: continued ICS-level integration with Gloucestershire Hospitals NHS FT on community pathways.",
        "sources": [
            {"publisher": "Gloucestershire Health and Care NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.ghc.nhs.uk/about-us/our-publications/"},
            {"publisher": "Valuation Office Agency", "title": "Find a business rates valuation (2023 list)", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "DLUHC", "title": "Business rates: explanatory notes 2024-25", "url": "https://www.gov.uk/introduction-to-business-rates"},
            {"publisher": "UK Parliament", "title": "Non-Domestic Rating (Multipliers and Private Finance) Act 2024", "url": "https://www.legislation.gov.uk/ukpga/2024/19/contents"},
            {"publisher": "One Gloucestershire ICB", "title": "ICS plans", "url": "https://www.onegloucestershire.net/"}
        ],
        "related": ["Premises & Infrastructure — Gloucestershire Health and Care NHS Foundation Trust", "Gloucestershire Health and Care NHS Foundation Trust", "Valuation Office Agency", "One Gloucestershire ICB", "Social security & levy — Gloucestershire Health and Care NHS Foundation Trust"]
    },
    "Lease expenditure — South East Coast Ambulance Service NHS Foundation Trust": {
        "aliases": [{"name": "Lease expenditure", "parent": "South East Coast Ambulance Service NHS Foundation Trust"}],
        "description": "Lease expenditure at South East Coast Ambulance Service NHS Foundation Trust (SECAmb) — IFRS 16 right-of-use property and short-life vehicle leases on ambulance stations, make-ready centres and pool fleet across Kent, Surrey and Sussex. SECAmb is one of ten regional 999 ambulance services, dispatching from a hub-and-spoke estate of make-ready centres and ambulance stations and operating ~700 emergency vehicles. The £1.76M reflects predominantly NHSPS-leased estate plus IFRS 16 reclassified vehicle leases.",
        "beneficiaries": "~4,000 WTE responding to ~1.0M calls a year across Kent, Surrey and Sussex (population ~4.8M) from a hub-and-spoke network of make-ready centres and ambulance stations.",
        "legal_basis": "IFRS 16 Leases · DHSC Group Accounting Manual 2024-25 (chapter 7 leases) · Landlord and Tenant Act 1954 · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Lease expenditure 2023-24", "value": "£1.76M"},
            {"label": "Parent line", "value": "Premises & Infrastructure"},
            {"label": "Trust category", "value": "NHS Ambulance"},
            {"label": "Catchment population", "value": "~4.8M (Kent + Surrey + Sussex)"},
            {"label": "WTE staff", "value": "~4,000"},
            {"label": "Calls per year", "value": "~1.0M"},
            {"label": "Estate model", "value": "Hub-and-spoke; many sites NHSPS-leased"},
            {"label": "Reporting standard", "value": "IFRS 16 (transition 2022-23)"},
            {"label": "Cat-1 standard", "value": "8-min mean (national target)"},
            {"label": "Foundation Trust authorised", "value": "2011"},
            {"label": "Industrial action 2023-24", "value": "Paramedic strikes (GMB + Unison)"},
            {"label": "CQC most recent rating", "value": "Requires improvement (improving trajectory 2023)"}
        ],
        "notes": "Delivery body: SECAmb Estates and Fleet, with NHS Property Services as landlord on most ambulance stations and lease vehicles from NHS Fleet Solutions / Lex Autolease frameworks. Policy owner: NHSE Ambulance Improvement Programme; NHSE Provider Finance for envelope; HMT for IFRS 16 transition guidance via DHSC GAM. Funding trajectory: rising — IFRS 16 reclassification 2022-23 lifted on-balance-sheet lease expense; Make Ready Centre rollout consolidates stations and modestly compresses property rents while expanding RoU on equipment; April 2025 NIC step-up affects landlord-passthrough costs. Evaluation: CQC currently RI but improving; NAO Ambulance Services report (HC 1112, 2017); ORH benchmarks vs SCAS, NEAS and EEAST; AACE national reports. Predecessor: SECAmb formed 2006 from Kent, Surrey, Sussex services; successor: continued station consolidation, electric/ULEZ-compliant fleet and ambulance estate strategy aligned to NHSPS national model.",
        "sources": [
            {"publisher": "South East Coast Ambulance Service NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.secamb.nhs.uk/about-us/publications/"},
            {"publisher": "Care Quality Commission", "title": "SECAmb inspection reports", "url": "https://www.cqc.org.uk/provider/RYD"},
            {"publisher": "NHS England", "title": "Ambulance services: response time data and the Ambulance Improvement Programme", "url": "https://www.england.nhs.uk/statistics/statistical-work-areas/ambulance-quality-indicators/"},
            {"publisher": "DHSC", "title": "Group Accounting Manual 2024-25 (IFRS 16)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Association of Ambulance Chief Executives", "title": "AACE national ambulance reports", "url": "https://aace.org.uk/"}
        ],
        "related": ["Premises & Infrastructure — South East Coast Ambulance Service NHS Foundation Trust", "South East Coast Ambulance Service NHS Foundation Trust", "NHS Property Services", "NHS England Ambulance Improvement Programme", "Amortisation — South East Coast Ambulance Service NHS Foundation Trust"]
    },
    "General supplies & services — Yorkshire Ambulance Service NHS Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "Yorkshire Ambulance Service NHS Trust"}],
        "description": "General supplies & services at Yorkshire Ambulance Service NHS Trust (YAS) — non-pharmaceutical clinical and non-clinical consumables: PPE, dressings, oxygen masks, defibrillator pads, IPC supplies, vehicle cleaning materials and Make Ready Centre stock. YAS is one of ten regional 999 services, covering all of Yorkshire and the Humber from a hub-and-spoke estate plus the Yorkshire Integrated Urgent Care (NHS 111) service. The £1.75M reflects high-volume single-use consumables across emergency, urgent care and PTS pathways.",
        "beneficiaries": "~7,000 WTE responding to ~1.0M emergency calls and handling ~3.5M NHS 111 contacts a year for the ~5.5M residents of Yorkshire and the Humber.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 2 Inventories (consumption interaction) · NHS Act 2006 · Health and Care Act 2022 · NHS Supply Chain framework",
        "key_stats": [
            {"label": "General supplies & services 2023-24", "value": "£1.75M"},
            {"label": "Parent line", "value": "Clinical Supplies & Drugs"},
            {"label": "Trust category", "value": "NHS Ambulance + IUC (111)"},
            {"label": "Catchment population", "value": "~5.5M (Yorkshire + Humber)"},
            {"label": "WTE staff", "value": "~7,000"},
            {"label": "Emergency calls/year", "value": "~1.0M"},
            {"label": "NHS 111 contacts/year", "value": "~3.5M"},
            {"label": "Lead procurement framework", "value": "NHS Supply Chain Tower 2 (Sterile Intervention)"},
            {"label": "Make Ready Centres", "value": "Multiple (Wakefield, Sheffield, Hull, Leeds region)"},
            {"label": "Trust authorised", "value": "2006"},
            {"label": "CQC most recent rating", "value": "Good"},
            {"label": "Industrial action 2023-24", "value": "Paramedic strikes (GMB + Unison)"}
        ],
        "notes": "Delivery body: YAS Procurement and Make Ready operations, with NHS Supply Chain providing the bulk of routine PPE, dressings and IPC items, plus direct contracts for ambulance-specific items (e.g., defib pads, oxygen). Policy owner: NHS Supply Chain (NHSBSA-sponsored) for category management; NHSE Provider Finance for envelope; AACE for clinical-supplies standards. Funding trajectory: rising — post-pandemic IPC inventory normalised but still elevated, Make Ready Centre standardisation and inflation passthrough on consumables drive growth, partly offset by NHS Supply Chain price aggregation. April 2025 employer NIC step-up indirectly raises supplier costs. Evaluation: CQC Good; NHSE Ambulance Quality Indicators; ORH benchmarks vs NWAS and NEAS; NAO Ambulance Services report (HC 1112, 2017). Predecessor: YAS formed 2006 from West, South and (former Tees) East Yorkshire services; successor: continued NHS 111 integration with IUC and Yorkshire & Humber Care Record links.",
        "sources": [
            {"publisher": "Yorkshire Ambulance Service NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.yas.nhs.uk/about-us/publications/"},
            {"publisher": "NHS Supply Chain", "title": "About the NHS Supply Chain operating model", "url": "https://www.supplychain.nhs.uk/about-us/"},
            {"publisher": "Care Quality Commission", "title": "Yorkshire Ambulance Service inspection reports", "url": "https://www.cqc.org.uk/provider/RX8"},
            {"publisher": "NHS England", "title": "Ambulance Quality Indicators", "url": "https://www.england.nhs.uk/statistics/statistical-work-areas/ambulance-quality-indicators/"},
            {"publisher": "Association of Ambulance Chief Executives", "title": "AACE national reports", "url": "https://aace.org.uk/"}
        ],
        "related": ["Clinical Supplies & Drugs — Yorkshire Ambulance Service NHS Trust", "Yorkshire Ambulance Service NHS Trust", "NHS Supply Chain", "NHS England Ambulance Improvement Programme", "Social security & levy — Yorkshire Ambulance Service NHS Trust"]
    },
    "Business rates — East of England Ambulance Service NHS Trust": {
        "aliases": [{"name": "Business rates", "parent": "East of England Ambulance Service NHS Trust"}],
        "description": "Business rates (non-domestic rates) at East of England Ambulance Service NHS Trust (EEAST) — annual liability under the Local Government Finance Act 1988 on ambulance stations, make-ready centres and Hazardous Area Response Team (HART) bases across Bedfordshire, Cambridgeshire, Essex, Hertfordshire, Norfolk and Suffolk. EEAST operates from ~150 sites including stations and HQ at Melbourn. The £1.73M rates bill reflects an extensive station network across six counties with no NHS-specific exemption.",
        "beneficiaries": "~5,500 WTE responding to ~1.1M emergency calls a year across the six East of England counties (population ~6.3M).",
        "legal_basis": "Local Government Finance Act 1988 (Schedule 6) · Non-Domestic Rating (Multipliers and Private Finance) Act 2024 · DHSC Group Accounting Manual 2024-25 · NHS Act 2006",
        "key_stats": [
            {"label": "Business rates 2023-24", "value": "£1.73M"},
            {"label": "Parent line", "value": "Premises & Infrastructure"},
            {"label": "Trust category", "value": "NHS Ambulance"},
            {"label": "Catchment population", "value": "~6.3M (6 counties)"},
            {"label": "WTE staff", "value": "~5,500"},
            {"label": "Emergency calls/year", "value": "~1.1M"},
            {"label": "Stations + sites", "value": "~150 (incl. HQ Melbourn)"},
            {"label": "Multiplier 2024-25", "value": "54.6p (standard) / 49.9p (small)"},
            {"label": "Billing authorities", "value": "~30 district councils across 6 counties"},
            {"label": "VOA list", "value": "2023 rating list"},
            {"label": "Cat-1 standard", "value": "8-min mean (national)"},
            {"label": "CQC most recent rating", "value": "Requires improvement (improving 2023-24)"}
        ],
        "notes": "Delivery body: EEAST Estates Department, with rates bills issued by the ~30 district billing authorities across the six counties and assessed by the VOA on the 2023 rating list. Policy owner: HMT and DLUHC set multipliers and reliefs (Non-Domestic Rating Act 2024 introduces lower retail/hospitality multipliers and a new high-multiplier for £500k+ properties); DHSC for GAM treatment. Funding trajectory: rising — annual multiplier uplift, 2023 list revaluation lifted bills, and any station consolidation only marginally offsets. April 2025 employer NIC step-up adds separate cost pressure. Evaluation: CQC RI but improving; NAO Ambulance Services report (HC 1112, 2017); NHSE Ambulance Quality Indicators; ORH benchmarks vs SECAmb and SCAS. Predecessor: EEAST formed 2006 from Beds, Cambs, Essex, Herts, Norfolk and Suffolk services; successor: continued estate rationalisation under the Make Ready Centre programme and joint working with the East of England HEMS / EAAA charity helicopter.",
        "sources": [
            {"publisher": "East of England Ambulance Service NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.eastamb.nhs.uk/about-us/publications.htm"},
            {"publisher": "Valuation Office Agency", "title": "Find a business rates valuation (2023 list)", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "DLUHC", "title": "Business rates: explanatory notes 2024-25", "url": "https://www.gov.uk/introduction-to-business-rates"},
            {"publisher": "Care Quality Commission", "title": "EEAST inspection reports", "url": "https://www.cqc.org.uk/provider/RYC"},
            {"publisher": "UK Parliament", "title": "Non-Domestic Rating (Multipliers and Private Finance) Act 2024", "url": "https://www.legislation.gov.uk/ukpga/2024/19/contents"}
        ],
        "related": ["Premises & Infrastructure — East of England Ambulance Service NHS Trust", "East of England Ambulance Service NHS Trust", "Valuation Office Agency", "NHS England Ambulance Improvement Programme", "Establishment costs — East of England Ambulance Service NHS Trust"]
    },
    "Establishment costs — Royal National Orthopaedic Hospital NHS Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "Royal National Orthopaedic Hospital NHS Trust"}],
        "description": "Establishment costs at Royal National Orthopaedic Hospital NHS Trust (RNOH) — telephony, postage, audit, training, advertising and indirect non-payroll non-clinical overhead. RNOH at Stanmore is the UK's largest orthopaedic specialist centre, operating across the Stanmore campus and the Bolsover Street outpatient site in central London. The £1.72M reflects a national/supra-regional referral profile, listed-building constraints on the 1922 Stanmore campus, and high research-active correspondence linked to UCL Institute of Orthopaedics.",
        "beneficiaries": "~1,400 WTE serving a national/supra-regional orthopaedic catchment with ~95,000 outpatient attendances and ~7,500 inpatient/daycase episodes a year (incl. complex spinal, sarcoma, paediatric ortho).",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Establishment costs 2023-24", "value": "£1.72M"},
            {"label": "Parent line", "value": "Premises & Infrastructure"},
            {"label": "Trust category", "value": "NHS Specialist (orthopaedic)"},
            {"label": "Sites", "value": "Stanmore (HQ, listed buildings 1922) + Bolsover Street, W1"},
            {"label": "WTE staff", "value": "~1,400"},
            {"label": "Annual outpatients", "value": "~95,000"},
            {"label": "Catchment", "value": "National (sarcoma, spinal cord injuries)"},
            {"label": "Lead ICS", "value": "North West London ICB"},
            {"label": "Commissioning route", "value": "NHSE Specialised Commissioning"},
            {"label": "Trust authorised", "value": "1991 (FT application paused)"},
            {"label": "CQC most recent rating", "value": "Good"},
            {"label": "Academic partner", "value": "UCL Institute of Orthopaedics"}
        ],
        "notes": "Delivery body: RNOH Corporate Services + Procurement, with NHS Supply Chain frameworks and shared back-office partnerships across the North West London Acute Provider Collaborative. Policy owner: NHSE Specialised Commissioning sets the orthopaedic envelope (sarcoma, spinal injury, complex revision); DHSC for GAM treatment. Funding trajectory: rising — phased redevelopment of the Stanmore campus (Stanmore Building completed 2019) lifted training and signage establishment lines; inflation passthrough on telephony and recruitment-advertising in a London labour market continues. April 2025 employer NIC step-up (15% / £5k threshold) raises social-security recharges. Evaluation: CQC Good; Model Hospital benchmarks vs Royal Orthopaedic Birmingham and Robert Jones & Agnes Hunt; NHSE Operational Plan returns. Predecessor: founded 1909 (originally three London ortho hospitals), Stanmore site opened 1922; successor: continued capital programme on the Stanmore master plan and deeper integration with London ICBs on elective recovery.",
        "sources": [
            {"publisher": "Royal National Orthopaedic Hospital NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.rnoh.nhs.uk/about/annual-reports"},
            {"publisher": "Care Quality Commission", "title": "RNOH inspection reports", "url": "https://www.cqc.org.uk/provider/RAN"},
            {"publisher": "NHS England", "title": "Specialised commissioning — orthopaedic services", "url": "https://www.england.nhs.uk/commissioning/spec-services/"},
            {"publisher": "DHSC", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "UCL Institute of Orthopaedics and Musculoskeletal Science", "title": "Stanmore campus partnership", "url": "https://www.ucl.ac.uk/orthopaedics/"}
        ],
        "related": ["Premises & Infrastructure — Royal National Orthopaedic Hospital NHS Trust", "Royal National Orthopaedic Hospital NHS Trust", "NHS England Specialised Commissioning", "North West London ICB", "Social security & levy — Royal National Orthopaedic Hospital NHS Trust"]
    },
    "Business rates — South Western Ambulance Service NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "South Western Ambulance Service NHS Foundation Trust"}],
        "description": "Business rates (non-domestic rates) at South Western Ambulance Service NHS Foundation Trust (SWAST) — annual liability under the Local Government Finance Act 1988 on ambulance stations, make-ready centres, the Bristol HQ Abbey Court and HART base across the South West. SWAST covers the largest geographic ambulance area in England — Cornwall, Devon, Somerset, Dorset, Wiltshire, Gloucestershire and the former Avon — over ~10,000 sq miles. The £1.72M reflects a station-heavy estate with no NHS-specific exemption.",
        "beneficiaries": "~5,000 WTE responding to ~1.0M emergency calls a year across ~10,000 sq miles serving ~5.7M residents from a network of stations and make-ready centres.",
        "legal_basis": "Local Government Finance Act 1988 (Schedule 6) · Non-Domestic Rating (Multipliers and Private Finance) Act 2024 · DHSC Group Accounting Manual 2024-25 · NHS Act 2006",
        "key_stats": [
            {"label": "Business rates 2023-24", "value": "£1.72M"},
            {"label": "Parent line", "value": "Premises & Infrastructure"},
            {"label": "Trust category", "value": "NHS Ambulance"},
            {"label": "Catchment population", "value": "~5.7M (South West)"},
            {"label": "Geographic area", "value": "~10,000 sq miles (largest in England)"},
            {"label": "WTE staff", "value": "~5,000"},
            {"label": "Emergency calls/year", "value": "~1.0M"},
            {"label": "Multiplier 2024-25", "value": "54.6p / 49.9p"},
            {"label": "Billing authorities", "value": "Multiple unitary + district councils"},
            {"label": "VOA list", "value": "2023 rating list"},
            {"label": "Foundation Trust authorised", "value": "2011"},
            {"label": "CQC most recent rating", "value": "Good (improving)"}
        ],
        "notes": "Delivery body: SWAST Estates Department, with rates bills issued by ~25 unitary and district councils across the seven historic counties and the VOA assessing on the 2023 rating list. Policy owner: HMT and DLUHC set multipliers and reliefs (Non-Domestic Rating Act 2024); DHSC for GAM treatment; NHSE Provider Finance for envelope. Funding trajectory: rising — annual multiplier uplift, 2023 list revaluation lifted bills, sparse rural coverage prevents station closures, and April 2025 NIC step-up adds separate cost pressure. Evaluation: CQC Good; NHSE Ambulance Quality Indicators; ORH benchmarks vs SECAmb and SCAS; NAO Ambulance Services report (HC 1112, 2017). Predecessor: SWAST formed 2006 from Westcountry, Dorset, Wiltshire and Avon services; absorbed Great Western Ambulance Service 2013; successor: continued estate rationalisation under Make Ready Centre programme and joint working with Devon Air Ambulance / Cornwall Air Ambulance charities.",
        "sources": [
            {"publisher": "South Western Ambulance Service NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.swast.nhs.uk/about-us/publications-and-reports"},
            {"publisher": "Valuation Office Agency", "title": "Find a business rates valuation (2023 list)", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "DLUHC", "title": "Business rates: explanatory notes 2024-25", "url": "https://www.gov.uk/introduction-to-business-rates"},
            {"publisher": "Care Quality Commission", "title": "SWAST inspection reports", "url": "https://www.cqc.org.uk/provider/RYF"},
            {"publisher": "UK Parliament", "title": "Non-Domestic Rating (Multipliers and Private Finance) Act 2024", "url": "https://www.legislation.gov.uk/ukpga/2024/19/contents"}
        ],
        "related": ["Premises & Infrastructure — South Western Ambulance Service NHS Foundation Trust", "South Western Ambulance Service NHS Foundation Trust", "Valuation Office Agency", "NHS England Ambulance Improvement Programme", "Social security & levy — South Western Ambulance Service NHS Foundation Trust"]
    },
    "Amortisation — Kent Community Health NHS Foundation Trust": {
        "aliases": [{"name": "Amortisation", "parent": "Kent Community Health NHS Foundation Trust"}],
        "description": "Amortisation of intangible assets at Kent Community Health NHS Foundation Trust (KCHFT) — annual systematic write-down of capitalised software licences (EMIS, SystmOne, e-rostering, finance ERP), bespoke development and right-of-use software under IAS 38. KCHFT is a stand-alone community provider serving Kent and parts of London via a network of community hospitals, minor injury units, dental services and 0-19 contracts. The £1.69M reflects a digital-led operating model with substantial EPR and clinical-system capitalised cost.",
        "beneficiaries": "~5,500 WTE serving ~1.6M residents of Kent and Medway plus parts of London with ~3.0M annual community contacts.",
        "legal_basis": "IAS 38 Intangible Assets · DHSC Group Accounting Manual 2024-25 (chapter 5) · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Amortisation 2023-24", "value": "£1.69M"},
            {"label": "Parent line", "value": "Premises & Infrastructure"},
            {"label": "Trust category", "value": "NHS Community"},
            {"label": "Catchment population", "value": "~1.6M (Kent + Medway + parts of London)"},
            {"label": "WTE staff", "value": "~5,500"},
            {"label": "Annual contacts", "value": "~3.0M"},
            {"label": "Community hospitals", "value": "Multiple (incl. Tonbridge, Sevenoaks, Sittingbourne)"},
            {"label": "ICS", "value": "Kent and Medway ICB"},
            {"label": "Main clinical system", "value": "Rio / SystmOne / EMIS"},
            {"label": "Foundation Trust authorised", "value": "2011"},
            {"label": "CQC most recent rating", "value": "Outstanding (2018, sustained 2022)"},
            {"label": "Estate landlord (much of)", "value": "NHS Property Services"}
        ],
        "notes": "Delivery body: KCHFT Digital and Finance teams, with EPR and clinical-system suppliers (TPP SystmOne, EMIS, Servelec/Rio) and shared digital partnerships across the Kent and Medway ICS. Policy owner: NHSE Frontline Digitisation programme; DHSC for GAM treatment; HMT for IFRS treatment. Funding trajectory: rising — Frontline Digitisation funding accelerated EPR and clinical-system capitalisation through 2022-25, lifting amortisation as assets enter the depreciation phase; cyber and Cloud-migration capex adds further. April 2025 NIC step-up is unrelated. Evaluation: CQC Outstanding (2018, sustained 2022); NHSE Operational Plan returns; Model Hospital benchmarks; ICS digital maturity assessments. Predecessor: KCHFT spun out from Eastern and Coastal Kent PCT 2011; successor: continued Kent and Medway ICS digital integration with KMPT, Medway NHS FT and East Kent Hospitals.",
        "sources": [
            {"publisher": "Kent Community Health NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.kentcht.nhs.uk/about-us/publications/"},
            {"publisher": "DHSC", "title": "Group Accounting Manual 2024-25 (chapter 5 intangibles)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/frontline-digitisation/"},
            {"publisher": "Care Quality Commission", "title": "KCHFT inspection reports", "url": "https://www.cqc.org.uk/provider/RYY"},
            {"publisher": "Kent and Medway ICB", "title": "ICS plans", "url": "https://www.kentandmedway.icb.nhs.uk/"}
        ],
        "related": ["Premises & Infrastructure — Kent Community Health NHS Foundation Trust", "Kent Community Health NHS Foundation Trust", "NHS England Frontline Digitisation", "Kent and Medway ICB", "Social security & levy — Kent Community Health NHS Foundation Trust"]
    },
    "General supplies & services — East Midlands Ambulance Service NHS Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "East Midlands Ambulance Service NHS Trust"}],
        "description": "General supplies & services at East Midlands Ambulance Service NHS Trust (EMAS) — non-pharmaceutical clinical and non-clinical consumables: PPE, dressings, oxygen masks, defibrillator pads, IPC supplies, vehicle cleaning materials and Make Ready Centre stock. EMAS is one of ten regional 999 services covering Derbyshire, Nottinghamshire, Lincolnshire, Leicestershire, Rutland and Northamptonshire from a hub-and-spoke estate. The £1.68M reflects high-volume single-use consumables across emergency and PTS pathways for ~4.8M residents.",
        "beneficiaries": "~4,000 WTE responding to ~900,000 emergency calls a year for the ~4.8M residents of the East Midlands region.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 2 Inventories (consumption interaction) · NHS Act 2006 · Health and Care Act 2022 · NHS Supply Chain framework",
        "key_stats": [
            {"label": "General supplies & services 2023-24", "value": "£1.68M"},
            {"label": "Parent line", "value": "Clinical Supplies & Drugs"},
            {"label": "Trust category", "value": "NHS Ambulance"},
            {"label": "Catchment population", "value": "~4.8M (East Midlands)"},
            {"label": "WTE staff", "value": "~4,000"},
            {"label": "Emergency calls/year", "value": "~900,000"},
            {"label": "Counties covered", "value": "Derbys/Notts/Lincs/Leics/Rutland/Northants"},
            {"label": "Lead procurement framework", "value": "NHS Supply Chain Tower 2"},
            {"label": "Make Ready Centres", "value": "Multiple (Beechdale, Lincoln region, Hilltop)"},
            {"label": "HQ", "value": "Beechdale, Nottingham"},
            {"label": "Trust authorised", "value": "2006"},
            {"label": "Industrial action 2023-24", "value": "Paramedic strikes (GMB + Unison)"}
        ],
        "notes": "Delivery body: EMAS Procurement and Make Ready operations, with NHS Supply Chain providing the bulk of routine PPE, dressings and IPC items, plus direct contracts for ambulance-specific items. Policy owner: NHS Supply Chain (NHSBSA-sponsored) for category management; NHSE Provider Finance for envelope; AACE for clinical-supplies standards; NHSE Ambulance Improvement Programme for performance frame. Funding trajectory: rising — post-pandemic IPC inventory normalised but elevated, Make Ready Centre standardisation lifts consumable throughput, and inflation passthrough on dressings continues, partly offset by NHS Supply Chain price aggregation. April 2025 NIC step-up indirectly raises supplier costs. Evaluation: CQC; NHSE Ambulance Quality Indicators; ORH benchmarks vs YAS and WMAS; NAO Ambulance Services report (HC 1112, 2017). Predecessor: EMAS formed 2006 from Derbyshire, Nottinghamshire, Leicestershire and Lincolnshire services; successor: continued station consolidation under Make Ready Centre programme.",
        "sources": [
            {"publisher": "East Midlands Ambulance Service NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.emas.nhs.uk/about-us/publications/"},
            {"publisher": "NHS Supply Chain", "title": "About the NHS Supply Chain operating model", "url": "https://www.supplychain.nhs.uk/about-us/"},
            {"publisher": "Care Quality Commission", "title": "EMAS inspection reports", "url": "https://www.cqc.org.uk/provider/RX9"},
            {"publisher": "NHS England", "title": "Ambulance Quality Indicators", "url": "https://www.england.nhs.uk/statistics/statistical-work-areas/ambulance-quality-indicators/"},
            {"publisher": "Association of Ambulance Chief Executives", "title": "AACE national reports", "url": "https://aace.org.uk/"}
        ],
        "related": ["Clinical Supplies & Drugs — East Midlands Ambulance Service NHS Trust", "East Midlands Ambulance Service NHS Trust", "NHS Supply Chain", "NHS England Ambulance Improvement Programme", "Social security & levy — East Midlands Ambulance Service NHS Trust"]
    },
    "Amortisation — The Clatterbridge Cancer Centre NHS Foundation Trust": {
        "aliases": [{"name": "Amortisation", "parent": "The Clatterbridge Cancer Centre NHS Foundation Trust"}],
        "description": "Amortisation of intangible assets at The Clatterbridge Cancer Centre NHS Foundation Trust — annual systematic write-down of capitalised software (Epic-aligned EPR / Oracle / Mosaiq oncology system), bespoke radiotherapy planning systems and right-of-use software under IAS 38. Clatterbridge is one of the UK's largest specialist cancer centres, operating from a flagship Liverpool site (opened 2020) plus Wirral and aintree satellites and a proton-beam linkage with The Christie. The £1.68M reflects digital-led oncology operations.",
        "beneficiaries": "~2,200 WTE serving ~2.4M residents of Cheshire and Merseyside with ~150,000 outpatient attendances and ~30,000 chemotherapy / radiotherapy episodes a year.",
        "legal_basis": "IAS 38 Intangible Assets · DHSC Group Accounting Manual 2024-25 (chapter 5) · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Amortisation 2023-24", "value": "£1.68M"},
            {"label": "Parent line", "value": "Premises & Infrastructure"},
            {"label": "Trust category", "value": "NHS Specialist (cancer)"},
            {"label": "Sites", "value": "Liverpool (2020) + Wirral + Aintree satellite"},
            {"label": "WTE staff", "value": "~2,200"},
            {"label": "Annual outpatients", "value": "~150,000"},
            {"label": "Catchment", "value": "~2.4M Cheshire and Merseyside"},
            {"label": "Lead ICS", "value": "Cheshire and Merseyside ICB"},
            {"label": "Commissioning route", "value": "NHSE Specialised Commissioning"},
            {"label": "Foundation Trust authorised", "value": "2006"},
            {"label": "CQC most recent rating", "value": "Outstanding"},
            {"label": "Main oncology system", "value": "Mosaiq + Epic-aligned EPR"}
        ],
        "notes": "Delivery body: Clatterbridge Digital and Finance teams, with Mosaiq (Elekta) and Epic-aligned EPR suppliers, and digital partnerships across the Cheshire and Merseyside Cancer Alliance. Policy owner: NHSE Frontline Digitisation programme; NHSE Specialised Commissioning for oncology envelope; DHSC for GAM treatment. Funding trajectory: rising — Frontline Digitisation funding accelerated EPR and oncology-system capitalisation through 2022-25, lifting amortisation as assets enter the depreciation phase; new linac and brachytherapy planning software adds further. April 2025 NIC step-up unrelated. Evaluation: CQC Outstanding; NHSE Operational Plan returns; Model Hospital benchmarks vs The Christie and Royal Marsden; ICS digital maturity assessments. Predecessor: founded 1932 as Liverpool Radium Institute; the new Liverpool city-centre flagship opened 2020 alongside RLBUH; successor: deeper integration with Liverpool University Hospitals on the Knowledge Quarter and proton-beam pathway with The Christie.",
        "sources": [
            {"publisher": "The Clatterbridge Cancer Centre NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.clatterbridgecc.nhs.uk/about-us/publications"},
            {"publisher": "DHSC", "title": "Group Accounting Manual 2024-25 (chapter 5 intangibles)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/frontline-digitisation/"},
            {"publisher": "Care Quality Commission", "title": "Clatterbridge inspection reports", "url": "https://www.cqc.org.uk/provider/REN"},
            {"publisher": "NHS England", "title": "Specialised commissioning — cancer services", "url": "https://www.england.nhs.uk/commissioning/spec-services/"}
        ],
        "related": ["Premises & Infrastructure — The Clatterbridge Cancer Centre NHS Foundation Trust", "The Clatterbridge Cancer Centre NHS Foundation Trust", "NHS England Specialised Commissioning", "Cheshire and Merseyside ICB", "Social security & levy — The Clatterbridge Cancer Centre NHS Foundation Trust"]
    },
    "Amortisation — South East Coast Ambulance Service NHS Foundation Trust": {
        "aliases": [{"name": "Amortisation", "parent": "South East Coast Ambulance Service NHS Foundation Trust"}],
        "description": "Amortisation of intangible assets at South East Coast Ambulance Service NHS Foundation Trust (SECAmb) — annual systematic write-down of capitalised software for the Computer Aided Dispatch (CAD) system, electronic patient care record (ePCR), e-rostering, finance ERP and bespoke development, plus right-of-use software under IAS 38. SECAmb covers Kent, Surrey and Sussex from a hub-and-spoke estate with a national 999 call-handling system. The £1.67M reflects digital-led emergency operations.",
        "beneficiaries": "~4,000 WTE responding to ~1.0M emergency calls a year across Kent, Surrey and Sussex (~4.8M residents) — supported by CAD, ePCR and Cleric / Cleric-equivalent dispatch systems.",
        "legal_basis": "IAS 38 Intangible Assets · DHSC Group Accounting Manual 2024-25 (chapter 5) · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Amortisation 2023-24", "value": "£1.67M"},
            {"label": "Parent line", "value": "Premises & Infrastructure"},
            {"label": "Trust category", "value": "NHS Ambulance"},
            {"label": "Catchment population", "value": "~4.8M (Kent + Surrey + Sussex)"},
            {"label": "WTE staff", "value": "~4,000"},
            {"label": "Emergency calls/year", "value": "~1.0M"},
            {"label": "Main systems", "value": "CAD + ePCR + finance ERP"},
            {"label": "Cat-1 standard", "value": "8-min mean (national)"},
            {"label": "Foundation Trust authorised", "value": "2011"},
            {"label": "Industrial action 2023-24", "value": "Paramedic strikes (GMB + Unison)"},
            {"label": "CQC most recent rating", "value": "Requires improvement (improving 2023)"},
            {"label": "Estate model", "value": "Hub-and-spoke; many sites NHSPS-leased"}
        ],
        "notes": "Delivery body: SECAmb Digital and Finance teams, with CAD/ePCR suppliers and shared digital partnerships across the South East Ambulance Programme and London/SE Cancer Alliance digital links. Policy owner: NHSE Frontline Digitisation; NHSE Ambulance Improvement Programme for performance; DHSC for GAM treatment. Funding trajectory: rising — Frontline Digitisation funding and ambulance digital programmes (CAD modernisation, ePCR rollout, integration with NHS 111 and ICS clinical systems) accelerated capitalisation through 2022-25, lifting amortisation as assets enter the depreciation phase. April 2025 NIC step-up unrelated. Evaluation: CQC RI but improving; NAO Ambulance Services report (HC 1112, 2017); NHSE Ambulance Quality Indicators; ORH benchmarks vs SCAS, EEAST. Predecessor: SECAmb formed 2006 from KSS services; FT 2011; successor: continued CAD modernisation, ePCR national rollout and AI-enabled triage.",
        "sources": [
            {"publisher": "South East Coast Ambulance Service NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.secamb.nhs.uk/about-us/publications/"},
            {"publisher": "DHSC", "title": "Group Accounting Manual 2024-25 (chapter 5 intangibles)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/frontline-digitisation/"},
            {"publisher": "Care Quality Commission", "title": "SECAmb inspection reports", "url": "https://www.cqc.org.uk/provider/RYD"},
            {"publisher": "Association of Ambulance Chief Executives", "title": "AACE national reports", "url": "https://aace.org.uk/"}
        ],
        "related": ["Premises & Infrastructure — South East Coast Ambulance Service NHS Foundation Trust", "South East Coast Ambulance Service NHS Foundation Trust", "NHS England Frontline Digitisation", "NHS England Ambulance Improvement Programme", "Lease expenditure — South East Coast Ambulance Service NHS Foundation Trust"]
    },
    "Business rates — South Central Ambulance Service NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "South Central Ambulance Service NHS Foundation Trust"}],
        "description": "Business rates (non-domestic rates) at South Central Ambulance Service NHS Foundation Trust (SCAS) — annual liability under the Local Government Finance Act 1988 on ambulance stations, make-ready centres, the HQ at Bicester and HART base across Berkshire, Buckinghamshire, Hampshire and Oxfordshire. SCAS also operates 999 call handling for SCAS counties and NHS 111 for the Thames Valley, Hampshire and IOW. The £1.65M reflects a station-heavy estate plus call centres with no NHS-specific exemption.",
        "beneficiaries": "~4,000 WTE responding to ~700,000 emergency calls a year and handling NHS 111 contacts for the ~4.5M residents of Berks, Bucks, Hants and Oxon.",
        "legal_basis": "Local Government Finance Act 1988 (Schedule 6) · Non-Domestic Rating (Multipliers and Private Finance) Act 2024 · DHSC Group Accounting Manual 2024-25 · NHS Act 2006",
        "key_stats": [
            {"label": "Business rates 2023-24", "value": "£1.65M"},
            {"label": "Parent line", "value": "Premises & Infrastructure"},
            {"label": "Trust category", "value": "NHS Ambulance + IUC (111)"},
            {"label": "Catchment population", "value": "~4.5M (Berks/Bucks/Hants/Oxon)"},
            {"label": "WTE staff", "value": "~4,000"},
            {"label": "Emergency calls/year", "value": "~700,000"},
            {"label": "HQ", "value": "Bicester, Oxfordshire"},
            {"label": "Multiplier 2024-25", "value": "54.6p / 49.9p"},
            {"label": "Billing authorities", "value": "Multiple unitary + district councils across 4 counties"},
            {"label": "VOA list", "value": "2023 rating list"},
            {"label": "Foundation Trust authorised", "value": "2012"},
            {"label": "CQC most recent rating", "value": "Requires improvement (2023; improving)"}
        ],
        "notes": "Delivery body: SCAS Estates Department, with rates bills issued by the unitary and district councils across Berkshire, Buckinghamshire, Hampshire and Oxfordshire and the VOA assessing on the 2023 rating list. Policy owner: HMT and DLUHC set multipliers and reliefs (Non-Domestic Rating Act 2024 introduces lower retail/hospitality multipliers and a new high-multiplier for £500k+ properties); DHSC for GAM treatment; NHSE Provider Finance for envelope. Funding trajectory: rising — annual multiplier uplift, 2023 list revaluation lifted bills; April 2025 NIC step-up adds separate cost pressure. Evaluation: CQC RI but improving (post-2022 leadership renewal); NAO Ambulance Services report (HC 1112, 2017); NHSE Ambulance Quality Indicators; ORH benchmarks vs SECAmb and EEAST. Predecessor: SCAS formed 2006 from Berkshire, Hampshire, Oxfordshire and Buckinghamshire services; FT 2012; successor: continued estate rationalisation under Make Ready Centre programme and IUC integration with Thames Valley NHS 111.",
        "sources": [
            {"publisher": "South Central Ambulance Service NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.scas.nhs.uk/about-us/publications/"},
            {"publisher": "Valuation Office Agency", "title": "Find a business rates valuation (2023 list)", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "DLUHC", "title": "Business rates: explanatory notes 2024-25", "url": "https://www.gov.uk/introduction-to-business-rates"},
            {"publisher": "Care Quality Commission", "title": "SCAS inspection reports", "url": "https://www.cqc.org.uk/provider/RYE"},
            {"publisher": "UK Parliament", "title": "Non-Domestic Rating (Multipliers and Private Finance) Act 2024", "url": "https://www.legislation.gov.uk/ukpga/2024/19/contents"}
        ],
        "related": ["Premises & Infrastructure — South Central Ambulance Service NHS Foundation Trust", "South Central Ambulance Service NHS Foundation Trust", "Valuation Office Agency", "NHS England Ambulance Improvement Programme", "Lease expenditure — South Central Ambulance Service NHS Foundation Trust"]
    },
}
