# -*- coding: utf-8 -*-
# Phase 2 Acute slice 2 — chunk 15 (17 NHS Acute Trust orphan sub-lines)
# Hand-curated trust-specific PROGRAMME-archetype enrichment entries.
# Structural contract per docs/archetype_briefs.md.

NEW = {
    "Establishment costs — Salisbury NHS Foundation Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "Salisbury NHS Foundation Trust"}],
        "description": "Salisbury NHS FT's £5.48M establishment costs line covers postage, telephony, printing, advertising, hospitality, training, courses, professional fees and other operating-cost categories at the Salisbury District Hospital site plus the Spinal Treatment Centre (one of England's eight spinal cord injury centres) and the Wessex regional Genetics, Burns, Cleft Lip and Plastic Surgery services. The trust's Frontline Digitisation EPR transition and BSW ICS shared-service consolidation drive change-management and professional-fees baseline.",
        "beneficiaries": "c. 4,000 WTE staff serving a c. 270,000 south Wiltshire and Hampshire local catchment plus extended Wessex tertiary catchment of c. 3M for spinal, plastic, burns, cleft and genetics specialties; c. 65,000 ED attendances/yr at Salisbury District Hospital; c. 50,000 admissions/yr (incl. national Spinal Treatment Centre referrals).",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · NHS Act 2006 · Health and Care Act 2022 · Procurement Act 2023 · NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£5.48M"},
            {"label": "Trust scale", "value": "Single acute site (Salisbury District Hospital, Odstock) + Wessex regional specialty services; c. 4,000 WTE"},
            {"label": "Specialty footprint", "value": "Duke of Cornwall Spinal Treatment Centre (1 of 8 NHS spinal cord injury centres) + Wessex regional Genetics, Burns, Cleft Lip & Plastic Surgery"},
            {"label": "ED throughput", "value": "c. 65,000 attendances/yr"},
            {"label": "Frontline Digitisation EPR", "value": "Nervecentre / Mizaic clinical-systems adoption — drives professional fees + training + change-management establishment cost"},
            {"label": "Composition", "value": "Postage + telephony + printing + advertising + hospitality + training + courses + professional fees + minor non-clinical operating items"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove additional comms + training + locum-onboarding establishment cost"},
            {"label": "April 2025 NIC + CPI uplift", "value": "Apr 2025 employer-NIC step-up flows through professional-services suppliers + non-pay CPI on print, postage, telephony"},
            {"label": "BSW ICS context", "value": "Bath, Swindon and Wiltshire ICS shared-corporate-functions exploration with GWH + RUH Bath shapes medium-term professional-fees consolidation"},
            {"label": "Funding trajectory", "value": "2021-22 c. £4.6M → 2023-24 £5.1M → 2024-25 £5.48M — sustained CPI + EPR-related professional fees"},
            {"label": "Delivery body", "value": "Trust Finance + Procurement + IT + HR/OD; external advisors + EPR vendor (Nervecentre / Mizaic)"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Bath, Swindon and Wiltshire ICB + NHSE Frontline Digitisation programme"},
            {"label": "Evaluation evidence", "value": "Model Hospital benchmarks; CQC inspection RNZ; NHSE Frontline Digitisation programme returns; Trust ARA"}
        ],
        "notes": "Salisbury's establishment-cost baseline reflects its dual role as a local DGH for south Wiltshire/Hampshire and host of national/regional Wessex specialty services — the Duke of Cornwall Spinal Treatment Centre (one of eight NHS spinal cord injury centres) plus regional Genetics, Burns, Cleft Lip and Plastic Surgery — sustaining professional fees, advertising and training above peer single-site DGHs. The Frontline Digitisation EPR programme (Nervecentre / Mizaic) drives change-management training and professional-fees demand. Industrial action 2023-24 added comms and locum-onboarding cost. Bath, Swindon and Wiltshire ICS shared-corporate-functions exploration with GWH and RUH Bath is the medium-term consolidation lever; April 2025 NIC step-up and CPI feed forward unit-cost pressure.",
        "sources": [
            {"publisher": "Salisbury NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.salisbury.nhs.uk/about-us/publications/annual-reports/"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/connecting-health-and-care-providers/frontline-digitisation/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Salisbury NHS FT provider profile (RNZ)", "url": "https://www.cqc.org.uk/provider/RNZ"},
            {"publisher": "NHS England", "title": "Spinal Cord Injury Service Specification (specialised commissioning)", "url": "https://www.england.nhs.uk/commissioning/spec-services/npc-crg/group-d/d14/"}
        ],
        "related": ["Salisbury NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Frontline Digitisation programme", "Establishment costs — Great Western Hospitals NHS Foundation Trust", "Establishment costs — Royal United Hospitals Bath NHS Foundation Trust"]
    },
    "Transport (business + patient) — East Kent Hospitals University NHS Foundation Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "East Kent Hospitals University NHS Foundation Trust"}],
        "description": "EKHUFT's £5.45M transport line covers staff business mileage, inter-site clinical transfers and Non-Emergency Patient Transport Services across the trust's three-site footprint — William Harvey (Ashford), Queen Elizabeth The Queen Mother (Margate) and Kent and Canterbury (Canterbury) — a geographically dispersed configuration sustaining substantial inter-site transfer demand for stroke, cardiology and complex-care pathways. SECAmb is primary 999 carrier; G4S/ERS-type accredited NEPTS contractors deliver routine PTS under Kent & Medway ICS commissioning.",
        "beneficiaries": "c. 8,000 WTE staff serving a c. 760,000 East Kent catchment (Ashford, Canterbury, Dover, Folkestone, Thanet); c. 220,000 ED attendances/yr across William Harvey + QEQM EDs; c. 110,000 admissions/yr; substantial inter-site transfer activity given dispersed three-site geography.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · IFRS 16 Leases (pool fleet) · NHS Act 2006 · NHSE Patient Transport Services Eligibility Framework 2022 · HMRC AMAP · NHS AfC Section 17",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£5.45M"},
            {"label": "Trust scale", "value": "Three-site acute (William Harvey Ashford + QEQM Margate + Kent & Canterbury); c. 8,000 WTE"},
            {"label": "Inter-site geography", "value": "c. 35-40 miles between William Harvey and QEQM via A28/A299 — drives substantial inter-site clinical transfer baseline"},
            {"label": "Stroke + cardiac transfer", "value": "Hyperacute stroke + PCI cardiology centralisation across sites generates time-critical inter-hospital transfers"},
            {"label": "ED throughput", "value": "c. 220,000 attendances/yr (William Harvey + QEQM combined)"},
            {"label": "PTS provider mix", "value": "South East Coast Ambulance Service NHS FT (SECAmb) for 999 + accredited NEPTS contractors (G4S / ERS-type) for routine PTS under Kent & Medway ICS"},
            {"label": "Maternity safety context", "value": "Kirkup Reading the Signals Oct 2022 review drove ongoing service-pattern review affecting cross-site obstetric flows"},
            {"label": "Staff + pool fleet", "value": "AfC Section 17 / HMRC AMAP 45p first 10,000 miles + 25p thereafter; IFRS 16 right-of-use on leased pool vehicles"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove ad-hoc inter-site transfer + locum mileage"},
            {"label": "Funding trajectory", "value": "2021-22 c. £4.4M → 2023-24 £5.1M → 2024-25 £5.45M — fuel CPI + sustained inter-site activity"},
            {"label": "Delivery body", "value": "Trust E&F + Travel team + SECAmb + accredited NEPTS contractor pool + Kent & Medway ICS commissioning"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + NHSE NEPTS framework + Kent & Medway ICB"},
            {"label": "Evaluation evidence", "value": "NHSE NEPTS Eligibility Framework 2022; Kirkup Reading the Signals Oct 2022; CQC inspection RVV; Trust ARA"}
        ],
        "notes": "EKHUFT's transport baseline is structurally elevated by its three-site dispersed geography — c. 35-40 miles between William Harvey and QEQM — and centralisation of hyperacute stroke and PCI cardiology pathways, generating sustained inter-hospital transfer demand. The Kirkup 'Reading the Signals' review (October 2022) into maternity and neonatal services drove ongoing service-pattern review with implications for obstetric flows. Industrial action 2023-24 added ad-hoc transfer demand and locum mileage. April 2025 NIC step-up affects PTS-contractor pass-through; fuel CPI remains dominant. Kent & Medway ICS shared-fleet pooling and EV transition are medium-term levers.",
        "sources": [
            {"publisher": "East Kent Hospitals University NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.ekhuft.nhs.uk/about-us/publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Reading the Signals — Kirkup review of maternity and neonatal services in East Kent", "url": "https://www.gov.uk/government/publications/maternity-and-neonatal-services-in-east-kent-reading-the-signals"},
            {"publisher": "NHS England", "title": "Non-Emergency Patient Transport Services Eligibility Framework 2022", "url": "https://www.england.nhs.uk/long-read/non-emergency-patient-transport-services-eligibility-framework/"},
            {"publisher": "South East Coast Ambulance Service NHS Foundation Trust", "title": "Annual Report 2023-24", "url": "https://www.secamb.nhs.uk/about-us/our-publications/"},
            {"publisher": "Care Quality Commission", "title": "EKHUFT provider profile (RVV)", "url": "https://www.cqc.org.uk/provider/RVV"}
        ],
        "related": ["East Kent Hospitals University NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "South East Coast Ambulance Service NHS Foundation Trust", "Transport (business + patient) — Imperial College Healthcare NHS Trust", "Establishment costs — East Kent Hospitals University NHS Foundation Trust"]
    },
    "Transport (business + patient) — North Cumbria Integrated Care NHS Foundation Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "North Cumbria Integrated Care NHS Foundation Trust"}],
        "description": "NCIC's £5.42M transport line covers staff business mileage, inter-site clinical transfers and Non-Emergency Patient Transport Services across an exceptionally rural geography spanning the Cumberland and Westmorland & Furness council areas — Cumberland Infirmary (Carlisle) and West Cumberland Hospital (Whitehaven) plus integrated community-team mileage across c. 7,000 km² of largely rural and Lake District terrain. NWAS is primary 999 carrier; the trust runs c. 60 miles of inter-site clinical transfer corridor (A595/A66) for stroke, cardiac and complex maternity flows.",
        "beneficiaries": "c. 6,500 WTE staff serving a c. 320,000 north Cumbria catchment (Carlisle, Allerdale, Copeland — including Sellafield-area Whitehaven population); c. 110,000 ED attendances/yr across Cumberland Infirmary + West Cumberland EDs; c. 50,000 admissions/yr; integrated community caseload across deeply rural geography sustains district-nursing mileage.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · IFRS 16 Leases (pool fleet) · NHS Act 2006 · NHSE Patient Transport Services Eligibility Framework 2022 · HMRC AMAP · NHS AfC Section 17 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£5.42M"},
            {"label": "Trust scale", "value": "Two acute sites (Cumberland Infirmary Carlisle + West Cumberland Hospital Whitehaven) + integrated north Cumbria community services; c. 6,500 WTE"},
            {"label": "Inter-site geography", "value": "c. 60 miles between Cumberland Infirmary (Carlisle) and West Cumberland Hospital (Whitehaven) via A595/A66 — among the longest acute inter-site corridors in England"},
            {"label": "Rural footprint", "value": "Catchment c. 7,000 km² incl. western Lake District + Solway Plain — drives community-team mileage above peer trusts"},
            {"label": "PTS provider mix", "value": "North West Ambulance Service NHS Trust (NWAS) for 999 + accredited NEPTS contractors under NENC ICS commissioning"},
            {"label": "Stroke + complex transfer", "value": "Centralised hyperacute stroke + complex maternity flows generate time-critical Whitehaven → Carlisle transfers"},
            {"label": "Staff + pool fleet", "value": "AfC Section 17 / HMRC AMAP 45p first 10,000 miles + 25p thereafter; IFRS 16 right-of-use on leased pool vehicles"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove ad-hoc inter-site transfer + locum mileage on long-distance corridor"},
            {"label": "NHP cohort context", "value": "West Cumberland new-build retained in NHP cohort post Jan 2025 Reset; rebuild planning will reshape inter-site demand long-term"},
            {"label": "Funding trajectory", "value": "2021-22 c. £4.5M → 2023-24 £5.1M → 2024-25 £5.42M — sustained fuel CPI + rural mileage activity"},
            {"label": "Delivery body", "value": "Trust E&F + Travel team + NWAS + accredited NEPTS contractors + NENC ICS commissioning"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + NHSE NEPTS framework + North East and North Cumbria ICB"},
            {"label": "Evaluation evidence", "value": "NHSE NEPTS Eligibility Framework 2022; CQC inspection RNN; Trust ARA disclosure; NHP business case"}
        ],
        "notes": "NCIC was formed in October 2019 by merging North Cumbria University Hospitals NHS Trust with the community services arm of Cumbria Partnership NHS FT, creating an integrated acute + community trust spanning one of England's most rural geographies. Transport spend is structurally elevated by the c. 60-mile Carlisle–Whitehaven inter-site corridor (one of the longest in English acute provision) and community-team mileage across c. 7,000 km² of Lake District and Solway terrain. West Cumberland Hospital remains in the NHP cohort post the January 2025 Reset, with rebuild planning reshaping long-term inter-site demand. Industrial action 2023-24 added ad-hoc transfer and locum mileage. Fuel CPI and April 2025 NIC pass-through are dominant near-term drivers.",
        "sources": [
            {"publisher": "North Cumbria Integrated Care NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.ncic.nhs.uk/about-us/publications"},
            {"publisher": "NHS England", "title": "New Hospital Programme — January 2025 Reset", "url": "https://www.gov.uk/government/publications/new-hospital-programme-update"},
            {"publisher": "NHS England", "title": "Non-Emergency Patient Transport Services Eligibility Framework 2022", "url": "https://www.england.nhs.uk/long-read/non-emergency-patient-transport-services-eligibility-framework/"},
            {"publisher": "North West Ambulance Service NHS Trust", "title": "Annual Report 2023-24", "url": "https://www.nwas.nhs.uk/about-us/our-publications/"},
            {"publisher": "Care Quality Commission", "title": "NCIC provider profile (RNN)", "url": "https://www.cqc.org.uk/provider/RNN"}
        ],
        "related": ["North Cumbria Integrated Care NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "New Hospital Programme", "Transport (business + patient) — East Kent Hospitals University NHS Foundation Trust", "PFI / LIFT charges — North Cumbria Integrated Care NHS Foundation Trust"]
    },
    "Business rates — County Durham and Darlington NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "County Durham and Darlington NHS Foundation Trust"}],
        "description": "CDDFT's £5.40M business rates line covers NDR on the trust's multi-site estate — University Hospital of North Durham, Darlington Memorial, Bishop Auckland, Shotley Bridge, Chester-le-Street and the Richardson and Weardale community sites. Rates are billed by Durham County Council and Darlington Borough Council against VOA 2023 List rateable values multiplied by the 54.6p standard multiplier, with no NHS charitable relief following the Court of Appeal's 2019 Derby Teaching Hospitals NHS FT v Derby City Council ruling.",
        "beneficiaries": "c. 7,500 WTE staff serving a c. 600,000 County Durham + Darlington catchment; c. 200,000 ED attendances/yr (UHND + Darlington Memorial EDs); c. 95,000 admissions/yr; multi-site community-hospital footprint sustains broad rates-list exposure.",
        "legal_basis": "Local Government Finance Act 1988 (Schedule 6 — non-domestic rating) · Non-Domestic Rating (Multipliers and Private Finance) Act 2024 · Local Government Finance Act 1992 · DHSC Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£5.40M"},
            {"label": "Trust scale", "value": "Multi-site acute + community: UHND Durham + Darlington Memorial + Bishop Auckland + Shotley Bridge + Chester-le-Street + Richardson + Weardale; c. 7,500 WTE"},
            {"label": "Billing authorities", "value": "Durham County Council (Durham + Bishop Auckland + community sites) + Darlington Borough Council (Darlington Memorial)"},
            {"label": "VOA 2023 List", "value": "Revaluation effective 1 Apr 2023 reset rateable values; transitional relief tapering"},
            {"label": "NDR multiplier 2024-25", "value": "54.6p (standard) / 49.9p (small) — applied to RV"},
            {"label": "Exemption position", "value": "Post-2020 Derby Teaching Hospitals v Derby CC Court of Appeal ruling — NHS FTs not entitled to charitable rates relief; trust pays full NDR"},
            {"label": "Empty / partial occupation", "value": "Rates impact at decommissioned wards / vacated community-hospital wings (Shotley Bridge legacy)"},
            {"label": "Bishop Auckland reconfiguration", "value": "Phased reconfiguration of acute services since 2018 reshaped rates exposure on retained estate"},
            {"label": "Funding trajectory", "value": "2021-22 c. £4.7M → 2023-24 £5.1M → 2024-25 £5.40M — VOA 2023 List uplift + multiplier indexation"},
            {"label": "Delivery body", "value": "Trust E&F + Finance + Durham CC + Darlington BC billing teams + Valuation Office Agency assessments"},
            {"label": "Policy owner", "value": "MHCLG (NDR policy) + HM Treasury + DHSC + VOA + NHSE Provider Finance + NENC ICB"},
            {"label": "Evaluation evidence", "value": "NAO NHS estate report; HFMA NDR briefings; Trust ARA disclosure; CQC inspection RXP"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2002 separate Durham + Darlington trust rates exposures · Successor: VOA 2026 List anticipated revaluation cycle + ongoing community-estate rationalisation"}
        ],
        "notes": "CDDFT's business-rates baseline reflects a broad multi-site acute + community footprint — two acute DGHs (UHND, Darlington Memorial), the partly reconfigured Bishop Auckland site, and a network of community hospitals (Shotley Bridge, Chester-le-Street, Richardson, Weardale) each carrying separate rateable assessments. The Court of Appeal's 2019 Derby ruling confirmed NHS trusts pay full NDR with no charitable-rates relief. VOA 2023 Rating List revaluation reset rateable values from April 2023 with transitional tapering, and the 54.6p multiplier applies in 2024-25. Bishop Auckland reconfiguration since 2018 has reshaped the retained-estate rates exposure.",
        "sources": [
            {"publisher": "County Durham and Darlington NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.cddft.nhs.uk/about-us/our-publications/"},
            {"publisher": "Valuation Office Agency", "title": "2023 Rating List", "url": "https://www.gov.uk/government/collections/rating-2023-revaluation"},
            {"publisher": "Ministry of Housing, Communities and Local Government", "title": "Business rates: 2024-25 multipliers", "url": "https://www.gov.uk/introduction-to-business-rates"},
            {"publisher": "England and Wales Court of Appeal", "title": "Derby Teaching Hospitals NHS Foundation Trust v Derby City Council [2019] EWCA Civ 1320 (charitable rates relief)", "url": "https://www.bailii.org/ew/cases/EWCA/Civ/2019/1320.html"},
            {"publisher": "Care Quality Commission", "title": "CDDFT provider profile (RXP)", "url": "https://www.cqc.org.uk/provider/RXP"}
        ],
        "related": ["County Durham and Darlington NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Business rates — Liverpool University Hospitals NHS Foundation Trust", "Valuation Office Agency", "PFI / LIFT charges — County Durham and Darlington NHS Foundation Trust"]
    },
    "Business rates — North West Anglia NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "North West Anglia NHS Foundation Trust"}],
        "description": "NWAFT's £5.40M business rates line covers NDR on the trust's three-site acute estate — Peterborough City Hospital (PFI-built, opened 2010), Hinchingbrooke and Stamford and Rutland Hospital — billed by Peterborough City Council, Huntingdonshire District Council and South Kesteven District Council against VOA 2023 List rateable values. The Peterborough PFI's SPV structure shapes ratepayer attribution; Hinchingbrooke's RAAC remediation affects rateable-value reviews on partially restricted clinical areas.",
        "beneficiaries": "c. 6,500 WTE staff serving a c. 800,000 north-west Cambridgeshire + south Lincolnshire + Rutland catchment; c. 200,000 ED attendances/yr (Peterborough + Hinchingbrooke EDs); c. 95,000 admissions/yr; three-site footprint sustains broad rateable-value exposure.",
        "legal_basis": "Local Government Finance Act 1988 (Schedule 6 — non-domestic rating) · Non-Domestic Rating (Multipliers and Private Finance) Act 2024 · Local Government Finance Act 1992 · DHSC Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£5.40M"},
            {"label": "Trust scale", "value": "Three-site acute (Peterborough City PFI + Hinchingbrooke + Stamford and Rutland); c. 6,500 WTE"},
            {"label": "Billing authorities", "value": "Peterborough CC (Peterborough City Hospital) + Huntingdonshire DC (Hinchingbrooke) + South Kesteven DC (Stamford & Rutland)"},
            {"label": "VOA 2023 List", "value": "Revaluation effective 1 Apr 2023 reset rateable values; transitional relief tapering"},
            {"label": "NDR multiplier 2024-25", "value": "54.6p (standard) / 49.9p (small)"},
            {"label": "Peterborough PFI context", "value": "Peterborough City Hospital PFI signed 2007, operational 2010 — c. £39M/yr unitary charge — IFRIC 12 service-concession; rates ratepayer is the trust"},
            {"label": "Hinchingbrooke RAAC context", "value": "Site listed in HSSIB Sep 2023 RAAC cohort; remediation programme affects rateable-value position on partially restricted areas"},
            {"label": "Exemption position", "value": "Post-2020 Derby Teaching Hospitals v Derby CC ruling — NHS trusts pay full NDR (no charitable relief)"},
            {"label": "Funding trajectory", "value": "2021-22 c. £4.6M → 2023-24 £5.1M → 2024-25 £5.40M — VOA 2023 List uplift + multiplier indexation"},
            {"label": "Delivery body", "value": "Trust E&F + Finance + Peterborough CC + Huntingdonshire DC + South Kesteven DC billing teams + VOA"},
            {"label": "Policy owner", "value": "MHCLG (NDR policy) + HM Treasury + DHSC + VOA + NHSE Provider Finance + Cambridgeshire & Peterborough ICB"},
            {"label": "Evaluation evidence", "value": "NAO NHS estate report; HSSIB RAAC list 2023; CQC inspection RGN; Trust ARA disclosure"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2017 separate Peterborough & Stamford Hospitals NHS FT + Hinchingbrooke Health Care NHS Trust rates exposures · Successor: VOA 2026 List + post-RAAC rebuild rateable-value reset"}
        ],
        "notes": "NWAFT was formed in April 2017 via merger of Peterborough & Stamford Hospitals NHS FT with Hinchingbrooke Health Care NHS Trust, consolidating three-site rates exposure under one entity. The Peterborough City Hospital PFI (signed 2007, operational 2010) is one of the larger acute PFIs in the eastern region with a c. £39M/yr unitary charge under IFRIC 12 service-concession recognition, with the trust as ratepayer of record. Hinchingbrooke sits in the HSSIB September 2023 RAAC cohort and is committed to NHP rebuild — RAAC remediation and rebuild planning shape future rateable-value reviews. The Court of Appeal's 2019 Derby ruling confirmed NHS trusts pay full NDR. VOA 2023 List revaluation and the 54.6p multiplier drove 2023-24 onward uplift.",
        "sources": [
            {"publisher": "North West Anglia NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.nwangliaft.nhs.uk/about-us/publications/"},
            {"publisher": "Valuation Office Agency", "title": "2023 Rating List", "url": "https://www.gov.uk/government/collections/rating-2023-revaluation"},
            {"publisher": "Health Services Safety Investigations Body", "title": "RAAC in NHS estate (Sep 2023 list)", "url": "https://www.gov.uk/government/news/extra-funding-to-eradicate-raac-from-the-nhs"},
            {"publisher": "England and Wales Court of Appeal", "title": "Derby Teaching Hospitals NHS Foundation Trust v Derby City Council [2019] EWCA Civ 1320", "url": "https://www.bailii.org/ew/cases/EWCA/Civ/2019/1320.html"},
            {"publisher": "Care Quality Commission", "title": "NWAFT provider profile (RGN)", "url": "https://www.cqc.org.uk/provider/RGN"}
        ],
        "related": ["North West Anglia NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Business rates — County Durham and Darlington NHS Foundation Trust", "New Hospital Programme", "Valuation Office Agency"]
    },
    "General supplies & services — The Rotherham NHS Foundation Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "The Rotherham NHS Foundation Trust"}],
        "description": "The Rotherham NHS FT's £5.38M general supplies & services line covers non-clinical consumables, linen, catering provisions, hotel-services materials, office supplies, IT consumables and minor expensed equipment at the single-site Rotherham Hospital plus integrated community sites across the Rotherham borough. The trust is in active group-model arrangements with Doncaster and Bassetlaw Teaching Hospitals NHS FT and Sheffield Teaching Hospitals NHS FT under South Yorkshire ICS provider collaboratives, shaping medium-term procurement consolidation alongside dominant NHS Supply Chain delivery.",
        "beneficiaries": "c. 4,500 WTE staff serving a c. 265,000 Rotherham borough catchment; c. 130,000 ED attendances/yr at Rotherham Hospital ED; c. 50,000 admissions/yr; integrated borough community caseload (district nursing + therapies + community-paediatric).",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 2 Inventories · Procurement Act 2023 · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "General supplies & services 2024-25", "value": "£5.38M"},
            {"label": "Trust scale", "value": "Single acute site (Rotherham Hospital, Moorgate Road) + integrated Rotherham borough community services; c. 4,500 WTE"},
            {"label": "ED throughput", "value": "c. 130,000 attendances/yr"},
            {"label": "Catchment deprivation", "value": "Rotherham borough — high IMD deprivation pockets; sustains acute + community-team consumable demand"},
            {"label": "Procurement route", "value": "NHS Supply Chain national framework + South Yorkshire ICS collaborative (with DBTH + STH) + trust-direct contracts"},
            {"label": "Group-model context", "value": "South Yorkshire ICS provider collaborative with Doncaster & Bassetlaw + Sheffield Teaching Hospitals shapes medium-term back-office + procurement consolidation"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove cancellation-related re-stocking churn + agency backfill"},
            {"label": "Composition", "value": "Linen + catering + hotel services + office supplies + IT consumables + minor expensed equipment below capitalisation threshold"},
            {"label": "April 2025 NIC + CPI uplift", "value": "Apr 2025 employer-NIC step-up + non-clinical CPI feed forward unit-cost pressure"},
            {"label": "Funding trajectory", "value": "2021-22 c. £4.6M → 2023-24 £5.1M → 2024-25 £5.38M — sustained CPI + activity uplift"},
            {"label": "Delivery body", "value": "Trust Procurement + Supply Chain team + NHS Supply Chain (DHSC ALB) + South Yorkshire ICS procurement collaborative"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + South Yorkshire ICB"},
            {"label": "Evaluation evidence", "value": "Model Hospital benchmarks; CQC inspection RFR; NHS Supply Chain ARA; Trust ARA disclosure"}
        ],
        "notes": "The Rotherham NHS FT's general supplies & services baseline reflects a single-site acute integrated with Rotherham borough community services since the 2011 transfer of Rotherham PCT community arms — broadening non-clinical consumable demand beyond acute-only peers. South Yorkshire ICS provider-collaborative arrangements with Doncaster & Bassetlaw Teaching Hospitals and Sheffield Teaching Hospitals are the medium-term procurement consolidation lever, with NHS Supply Chain remaining dominant delivery channel. Industrial action 2023-24 drove agency-backfill consumable churn through cancellation re-stocking. April 2025 NIC step-up flows through supplier pass-through, and sustained CPI on non-clinical inputs (linen, catering, hotel services, IT consumables) feeds forward unit-cost pressure.",
        "sources": [
            {"publisher": "The Rotherham NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.therotherhamft.nhs.uk/About_Us/Our-publications/"},
            {"publisher": "NHS Supply Chain", "title": "Annual Report 2023-24", "url": "https://www.supplychain.nhs.uk/about-us/our-publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "The Rotherham NHS FT provider profile (RFR)", "url": "https://www.cqc.org.uk/provider/RFR"},
            {"publisher": "South Yorkshire ICB", "title": "Provider collaborative arrangements", "url": "https://syics.co.uk/"}
        ],
        "related": ["The Rotherham NHS Foundation Trust", "Clinical Supplies & Drugs", "NHS Acute Trusts", "NHS Supply Chain", "General supplies & services — Barnsley Hospital NHS Foundation Trust", "Sheffield Teaching Hospitals NHS Foundation Trust"]
    },
    "Establishment costs — Surrey And Sussex Healthcare NHS Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "Surrey And Sussex Healthcare NHS Trust"}],
        "description": "SASH's £5.37M establishment costs line covers postage, telephony, printing, advertising, hospitality, training, courses, professional fees and other operating-cost items at East Surrey Hospital (Redhill) plus the Caterham Dene, Crawley and Horsham community facilities. The trust is CQC Outstanding-rated, with the Frontline Digitisation EPR programme (Cerner Millennium since 2019) and Surrey Heartlands ICS shared-corporate-functions consolidation driving change-management and professional-fees baseline.",
        "beneficiaries": "c. 4,500 WTE staff serving a c. 535,000 east Surrey + west Sussex catchment (Reigate, Redhill, Horley, Crawley, Horsham, East Grinstead); c. 145,000 ED attendances/yr at East Surrey Hospital ED; c. 60,000 admissions/yr; c. 4,500 deliveries/yr.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · NHS Act 2006 · Health and Care Act 2022 · Procurement Act 2023 · NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£5.37M"},
            {"label": "Trust scale", "value": "Single acute site (East Surrey Hospital, Redhill) + Caterham Dene + Crawley + Horsham community sites; c. 4,500 WTE"},
            {"label": "CQC rating", "value": "Outstanding (last full inspection RTP) — drives sustained training + professional-fees investment to maintain rating"},
            {"label": "Frontline Digitisation EPR", "value": "Cerner Millennium EPR adopted from 2019; ongoing optimisation + module rollout drives change-management + training establishment cost"},
            {"label": "Composition", "value": "Postage + telephony + printing + advertising + hospitality + training + courses + professional fees + minor non-clinical operating items"},
            {"label": "ED throughput", "value": "c. 145,000 attendances/yr — sustained pressure on training + change-management spend"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove additional comms + training + locum-onboarding establishment cost"},
            {"label": "April 2025 NIC + CPI uplift", "value": "Apr 2025 employer-NIC step-up flows through professional-services suppliers + non-pay CPI on print, postage, telephony"},
            {"label": "Surrey Heartlands ICS", "value": "ICS shared-corporate-functions exploration with Royal Surrey + ASPH shapes medium-term professional-fees consolidation"},
            {"label": "Funding trajectory", "value": "2021-22 c. £4.5M → 2023-24 £5.0M → 2024-25 £5.37M"},
            {"label": "Delivery body", "value": "Trust Finance + Procurement + IT + HR/OD; external advisors + Cerner / Oracle Health (EPR) + training providers"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Surrey Heartlands ICB + NHSE Frontline Digitisation programme"},
            {"label": "Evaluation evidence", "value": "Model Hospital benchmarks; CQC inspection RTP (Outstanding); NHSE Frontline Digitisation programme returns; Trust ARA"}
        ],
        "notes": "SASH is one of the small group of CQC Outstanding-rated acute providers in England, sustaining investment in training, change management and professional fees that feeds the establishment-cost line. The Cerner Millennium EPR (adopted from 2019, with ongoing module optimisation under NHSE Frontline Digitisation) is a continuing driver of training and consultancy cost. Industrial action 2023-24 added comms, training and locum-onboarding cost. The Surrey Heartlands ICS shared-corporate-functions agenda — exploration of consolidation with Royal Surrey and Ashford & St Peter's — is the medium-term lever; April 2025 NIC step-up and non-pay CPI feed forward unit-cost pressure.",
        "sources": [
            {"publisher": "Surrey and Sussex Healthcare NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.surreyandsussex.nhs.uk/about-us/about-the-trust/our-publications/"},
            {"publisher": "Care Quality Commission", "title": "SASH provider profile (RTP) — Outstanding rated", "url": "https://www.cqc.org.uk/provider/RTP"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/connecting-health-and-care-providers/frontline-digitisation/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Surrey Heartlands ICB", "title": "Provider collaborative arrangements", "url": "https://www.surreyheartlands.org/"}
        ],
        "related": ["Surrey And Sussex Healthcare NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Frontline Digitisation programme", "Establishment costs — Ashford and St Peter's Hospitals NHS Foundation Trust", "Establishment costs — Salisbury NHS Foundation Trust"]
    },
    "PFI / LIFT charges — Kingston Hospital NHS Foundation Trust": {
        "aliases": [{"name": "PFI / LIFT charges", "parent": "Kingston Hospital NHS Foundation Trust"}],
        "description": "Kingston Hospital's £5.31M PFI/LIFT charge covers residual service-concession arrangements on partial-site PFI structures (notably the maternity wing redevelopment and ancillary LIFT-style community-clinic arrangements) at the Galsworthy Road Kingston site. The trust is not subject to a single full-hospital PFI deal — distinguishing it from peers like Sherwood Forest or Worcestershire Acute — but carries discrete service-concession components arising from estate refurbishments and community-clinic LIFT vehicles under the South West London ICS footprint, accounted under IFRIC 12 / IFRS 16.",
        "beneficiaries": "c. 4,000 WTE staff serving a c. 350,000 Kingston, Richmond and Wandsworth catchment; c. 110,000 ED attendances/yr at Kingston ED; c. 45,000 admissions/yr; c. 5,500 deliveries/yr (large maternity service — partly delivered through the historic PFI-financed maternity wing).",
        "legal_basis": "IFRIC 12 Service Concession Arrangements · IFRS 16 Leases (post-2022 transition for service-concession components) · DHSC Group Accounting Manual 2024-25 ch.7 · Private Finance Initiative guidance (HM Treasury) · LIFT framework guidance · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "PFI / LIFT charges 2024-25", "value": "£5.31M"},
            {"label": "PFI footprint", "value": "Discrete service-concession components on partial-site PFI structures (maternity wing redevelopment) + LIFT-style community-clinic arrangements — not a single full-hospital PFI"},
            {"label": "Trust scale", "value": "Single-site DGH (Kingston Hospital, Galsworthy Road); c. 4,000 WTE; CQC Outstanding-rated"},
            {"label": "Maternity scale", "value": "c. 5,500 deliveries/yr — among the largest in south-west London"},
            {"label": "Unitary charge composition", "value": "Debt service + lifecycle hard-FM + indexed soft-FM components on concession-financed estate elements"},
            {"label": "Indexation mechanism", "value": "RPI-linked uplift on indexed soft-FM components per concession agreements"},
            {"label": "IFRS 16 transition", "value": "2022 IFRS 16 transition reshaped right-of-use vs operating-expense split for service-concession components"},
            {"label": "LIFT context", "value": "LIFTCo SPVs delivered NHS LIFT-framework community clinics 2004-2010s; charges flow through in trust accounts"},
            {"label": "Group-model context", "value": "Group arrangements with Hounslow & Richmond Community Healthcare; chair-in-common with Epsom & St Helier under SWL ICS shapes medium-term FM consolidation"},
            {"label": "Funding trajectory", "value": "2021-22 c. £4.7M → 2023-24 £5.1M → 2024-25 £5.31M — RPI indexation on indexed components"},
            {"label": "Delivery body", "value": "PFI/LIFT SPVs + hard/soft FM contractors + trust E&F oversight"},
            {"label": "Policy owner", "value": "DHSC + HM Treasury PFI guidance + IPA PFI Hand-Back Resource Centre + NHSE Provider Finance + South West London ICB"},
            {"label": "Evaluation evidence", "value": "NAO PFI hand-back review 2020; CQC inspection RAX (Outstanding); IPA PFI Hand-Back guidance; Trust ARA"}
        ],
        "notes": "Kingston Hospital's PFI/LIFT charge sits at the smaller end of the NHS PFI distribution — the trust does not host a single full-hospital PFI deal (unlike Sherwood Forest, Worcestershire Acute or Dartford & Gravesham) but carries discrete service-concession arrangements on partial-site PFI structures plus residual NHS LIFT-framework community-clinic arrangements. The IFRS 16 2022 transition reshaped the right-of-use vs operating-expense split without altering the underlying obligations. The Galsworthy Road site's CQC Outstanding rating and large maternity service (c. 5,500 deliveries/yr — among SWL's largest) shape the operational context. SWL ICS group-model planning with Epsom & St Helier is the medium-term FM-consolidation lever.",
        "sources": [
            {"publisher": "Kingston Hospital NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.kingstonhospital.nhs.uk/about-us/publications/annual-report-and-accounts/"},
            {"publisher": "National Audit Office", "title": "Managing PFI assets and services as contracts end (HC 632, 2020)", "url": "https://www.nao.org.uk/reports/managing-pfi-assets-and-services-as-contracts-end/"},
            {"publisher": "Infrastructure and Projects Authority", "title": "PFI Hand-Back Resource Centre", "url": "https://www.gov.uk/government/collections/pfi-and-pf2"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 7 — Leases and service concessions)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Kingston Hospital provider profile (RAX) — Outstanding rated", "url": "https://www.cqc.org.uk/provider/RAX"}
        ],
        "related": ["Kingston Hospital NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "PFI / LIFT charges — Sherwood Forest Hospitals NHS Foundation Trust", "Social security & levy — Kingston Hospital NHS Foundation Trust", "Infrastructure and Projects Authority"]
    },
    "General supplies & services — Wrightington, Wigan and Leigh NHS Foundation Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "Wrightington, Wigan and Leigh NHS Foundation Trust"}],
        "description": "WWL's £5.30M general supplies & services line covers non-clinical consumables, linen, catering, hotel-services materials, office supplies, IT consumables and minor expensed equipment across the trust's three-site footprint — Royal Albert Edward Infirmary (Wigan), Wrightington Hospital (orthopaedic specialty centre near Standish) and Leigh Infirmary. Wrightington's national reputation for elective orthopaedic surgery (a centre of excellence with international hip-replacement heritage) elevates specialty consumable demand alongside general DGH-level baseline at Wigan and Leigh.",
        "beneficiaries": "c. 5,000 WTE staff serving a c. 320,000 Wigan borough catchment plus tertiary orthopaedic referrals nationally; c. 130,000 ED attendances/yr at Royal Albert Edward Infirmary ED; c. 60,000 admissions/yr (incl. high-volume elective orthopaedic at Wrightington); broad community-team service.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 2 Inventories · Procurement Act 2023 · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "General supplies & services 2024-25", "value": "£5.30M"},
            {"label": "Trust scale", "value": "Three-site (Royal Albert Edward Infirmary Wigan + Wrightington Hospital + Leigh Infirmary); c. 5,000 WTE"},
            {"label": "Specialty footprint", "value": "Wrightington = national centre of orthopaedic excellence (Sir John Charnley hip-replacement heritage; tertiary referrals)"},
            {"label": "ED throughput", "value": "c. 130,000 attendances/yr at Royal Albert Edward Infirmary"},
            {"label": "Procurement route", "value": "NHS Supply Chain national framework + Greater Manchester ICS collaborative + trust-direct contracts (incl. orthopaedic implant frameworks)"},
            {"label": "GM ICS context", "value": "Greater Manchester ICS provider-collaborative procurement consolidation alongside MFT, NCA, Stockport, Bolton, Salford, Tameside"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove cancellation-related re-stocking churn + agency backfill"},
            {"label": "Composition", "value": "Linen + catering + hotel services + office supplies + IT consumables + minor expensed equipment below capitalisation threshold"},
            {"label": "April 2025 NIC + CPI uplift", "value": "Apr 2025 employer-NIC step-up + non-clinical CPI feed forward unit-cost pressure"},
            {"label": "Funding trajectory", "value": "2021-22 c. £4.5M → 2023-24 £5.0M → 2024-25 £5.30M — sustained CPI + activity uplift + elective recovery"},
            {"label": "Delivery body", "value": "Trust Procurement + Supply Chain team + NHS Supply Chain (DHSC ALB) + GM ICS procurement collaborative"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Greater Manchester ICB"},
            {"label": "Evaluation evidence", "value": "Model Hospital benchmarks; CQC inspection RRF; NHS Supply Chain ARA; Trust ARA disclosure"}
        ],
        "notes": "WWL's general supplies & services baseline reflects a three-site footprint anchored by Wrightington Hospital — internationally known as Sir John Charnley's pioneering hip-replacement centre and a continuing national centre of orthopaedic excellence — alongside the Royal Albert Edward Infirmary in Wigan and Leigh Infirmary. Elective-orthopaedic specialty mix elevates consumable demand on Wrightington's high-volume planned-care lists. Greater Manchester ICS provider-collaborative procurement consolidation with MFT, Northern Care Alliance, Stockport, Bolton, Salford and Tameside is the medium-term lever; NHS Supply Chain remains dominant delivery channel. Industrial action 2023-24 drove agency-backfill consumable churn. April 2025 NIC step-up and CPI feed forward unit-cost pressure.",
        "sources": [
            {"publisher": "Wrightington, Wigan and Leigh NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.wwl.nhs.uk/annual-report"},
            {"publisher": "NHS Supply Chain", "title": "Annual Report 2023-24", "url": "https://www.supplychain.nhs.uk/about-us/our-publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "WWL provider profile (RRF)", "url": "https://www.cqc.org.uk/provider/RRF"},
            {"publisher": "Greater Manchester ICB", "title": "GM provider collaborative arrangements", "url": "https://gmintegratedcare.org.uk/"}
        ],
        "related": ["Wrightington, Wigan and Leigh NHS Foundation Trust", "Clinical Supplies & Drugs", "NHS Acute Trusts", "NHS Supply Chain", "General supplies & services — The Rotherham NHS Foundation Trust", "Manchester University NHS Foundation Trust"]
    },
    "Business rates — Somerset NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "Somerset NHS Foundation Trust"}],
        "description": "Somerset NHS FT's £5.26M business rates line covers NDR on the trust's integrated acute + community + mental health estate — Musgrove Park Hospital (Taunton), Yeovil District Hospital (post-2023 merger), the Bridgwater + Burnham + Frome + Wellington + West Mendip community hospitals and a network of mental-health units. Rates are billed by Somerset Council (unitary since April 2023) against VOA 2023 List rateable values. The trust is one of England's earliest fully integrated acute + community + mental health providers post the 2023 Yeovil merger.",
        "beneficiaries": "c. 12,000 WTE staff serving a c. 570,000 Somerset population; c. 175,000 ED attendances/yr (Musgrove Park + Yeovil EDs); c. 95,000 admissions/yr; broad community-hospital + mental-health-unit footprint sustains exceptionally broad rateable-value exposure.",
        "legal_basis": "Local Government Finance Act 1988 (Schedule 6 — non-domestic rating) · Non-Domestic Rating (Multipliers and Private Finance) Act 2024 · Local Government Finance Act 1992 · DHSC Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£5.26M"},
            {"label": "Trust scale", "value": "Two acute (Musgrove Park Taunton + Yeovil District post-2023 merger) + community hospitals (Bridgwater + Burnham + Frome + Wellington + West Mendip + Williton + Minehead + Chard + Crewkerne + South Petherton) + mental-health units; c. 12,000 WTE"},
            {"label": "Yeovil merger", "value": "Apr 2023 acquisition of Yeovil District Hospital NHS FT to form unified Somerset NHS FT — substantially expanded rates exposure"},
            {"label": "Billing authority", "value": "Somerset Council (unitary since Apr 2023, replacing 4 former districts: Mendip + Sedgemoor + Somerset West & Taunton + South Somerset)"},
            {"label": "VOA 2023 List", "value": "Revaluation effective 1 Apr 2023 reset rateable values; transitional relief tapering"},
            {"label": "NDR multiplier 2024-25", "value": "54.6p (standard) / 49.9p (small)"},
            {"label": "Exemption position", "value": "Post-2020 Derby Teaching Hospitals v Derby CC ruling — NHS trusts pay full NDR (no charitable relief)"},
            {"label": "Integrated estate scope", "value": "One of England's earliest fully integrated acute + community + mental health providers — broadens rates exposure beyond acute-only peers"},
            {"label": "Funding trajectory", "value": "2021-22 c. £3.5M (pre-Yeovil) → 2023-24 £5.0M (post-merger first full year) → 2024-25 £5.26M — Yeovil merger + VOA 2023 List uplift"},
            {"label": "Delivery body", "value": "Trust E&F + Finance + Somerset Council billing team + Valuation Office Agency assessments"},
            {"label": "Policy owner", "value": "MHCLG (NDR policy) + HM Treasury + DHSC + VOA + NHSE Provider Finance + Somerset ICB"},
            {"label": "Evaluation evidence", "value": "NAO NHS estate report; HFMA NDR briefings; Trust ARA disclosure; CQC inspection RH5; Yeovil merger transaction business case"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-Apr 2023 separate Somerset NHS FT + Yeovil District Hospital NHS FT rates exposures · Successor: VOA 2026 List + ongoing community-estate rationalisation"}
        ],
        "notes": "Somerset NHS FT was formed in April 2020 from the merger of Somerset Partnership NHS FT (mental health + community) with Taunton & Somerset NHS FT (Musgrove Park acute), and was substantially expanded in April 2023 with the acquisition of Yeovil District Hospital NHS FT — making it one of England's earliest and most fully integrated acute + community + mental health providers. The 2023 transaction roughly doubled the rates exposure baseline. Somerset Council became a single unitary authority in April 2023, simplifying billing-authority interaction. The Court of Appeal's 2019 Derby ruling confirmed NHS trusts pay full NDR. VOA 2023 List revaluation and the 54.6p multiplier drove 2023-24 onward uplift.",
        "sources": [
            {"publisher": "Somerset NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.somersetft.nhs.uk/about-us/publications/"},
            {"publisher": "Valuation Office Agency", "title": "2023 Rating List", "url": "https://www.gov.uk/government/collections/rating-2023-revaluation"},
            {"publisher": "Somerset Council", "title": "Business rates (post-2023 unitary)", "url": "https://www.somerset.gov.uk/business-and-licensing/business-rates/"},
            {"publisher": "England and Wales Court of Appeal", "title": "Derby Teaching Hospitals NHS Foundation Trust v Derby City Council [2019] EWCA Civ 1320", "url": "https://www.bailii.org/ew/cases/EWCA/Civ/2019/1320.html"},
            {"publisher": "Care Quality Commission", "title": "Somerset NHS FT provider profile (RH5)", "url": "https://www.cqc.org.uk/provider/RH5"}
        ],
        "related": ["Somerset NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Business rates — County Durham and Darlington NHS Foundation Trust", "Valuation Office Agency", "Amortisation — Somerset NHS Foundation Trust"]
    },
    "Establishment costs — East Kent Hospitals University NHS Foundation Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "East Kent Hospitals University NHS Foundation Trust"}],
        "description": "EKHUFT's £5.24M establishment costs line covers postage, telephony, printing, advertising, hospitality, training, courses, professional fees and other operating-cost items across the trust's three-site footprint — William Harvey (Ashford), QEQM (Margate) and Kent and Canterbury (Canterbury). The trust carries elevated professional-fees and training spend through ongoing maternity-improvement programmes following the Kirkup 'Reading the Signals' review (October 2022) and the Frontline Digitisation EPR programme alongside Kent & Medway ICS shared-corporate-functions consolidation.",
        "beneficiaries": "c. 8,000 WTE staff serving a c. 760,000 East Kent catchment (Ashford, Canterbury, Dover, Folkestone, Thanet); c. 220,000 ED attendances/yr across William Harvey + QEQM EDs; c. 110,000 admissions/yr; substantial cross-site training + professional-fees demand given dispersed three-site geography and ongoing maternity-improvement programme.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · NHS Act 2006 · Health and Care Act 2022 · Procurement Act 2023 · NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£5.24M"},
            {"label": "Trust scale", "value": "Three-site acute (William Harvey Ashford + QEQM Margate + Kent & Canterbury); c. 8,000 WTE"},
            {"label": "Kirkup maternity improvement", "value": "Reading the Signals Oct 2022 Kirkup review drove sustained training + improvement-programme professional-fees spend; ongoing maternity safety transformation"},
            {"label": "Frontline Digitisation EPR", "value": "EPR adoption + optimisation drives change-management + training establishment cost"},
            {"label": "Composition", "value": "Postage + telephony + printing + advertising + hospitality + training + courses + professional fees + minor non-clinical operating items"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove additional comms + training + locum-onboarding establishment cost"},
            {"label": "Three-site geography effect", "value": "Cross-site training delivery + dispersed comms add to baseline above peer single-site DGHs"},
            {"label": "April 2025 NIC + CPI uplift", "value": "Apr 2025 employer-NIC step-up flows through professional-services suppliers + non-pay CPI on print, postage, telephony"},
            {"label": "Kent & Medway ICS context", "value": "Shared-corporate-functions exploration with MTW + Dartford & Gravesham + Medway shapes medium-term professional-fees consolidation"},
            {"label": "Funding trajectory", "value": "2021-22 c. £4.4M → 2023-24 £4.9M → 2024-25 £5.24M — Kirkup-driven training spend + sustained CPI"},
            {"label": "Delivery body", "value": "Trust Finance + Procurement + IT + HR/OD + Maternity Improvement programme; external advisors + EPR vendor + training providers"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Kent & Medway ICB + NHSE Frontline Digitisation + NHSE Maternity Transformation"},
            {"label": "Evaluation evidence", "value": "Kirkup Reading the Signals Oct 2022; CQC inspection RVV; NHSE Maternity Improvement programme returns; Trust ARA"}
        ],
        "notes": "EKHUFT's establishment-cost baseline is elevated by three-site dispersed geography and the ongoing maternity-improvement programme triggered by Bill Kirkup's 'Reading the Signals' review (October 2022) into maternity and neonatal services failings — sustained spend on professional fees, external improvement consultancy, training and communications continues feeding through. The Frontline Digitisation EPR programme adds change-management and training cost. Industrial action 2023-24 added comms, training and locum-onboarding establishment cost. Kent & Medway ICS shared-corporate-functions agenda — with MTW, Dartford & Gravesham and Medway — is the medium-term consolidation lever; April 2025 NIC step-up and non-pay CPI feed forward unit-cost pressure.",
        "sources": [
            {"publisher": "East Kent Hospitals University NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.ekhuft.nhs.uk/about-us/publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Reading the Signals — Kirkup review of maternity and neonatal services in East Kent", "url": "https://www.gov.uk/government/publications/maternity-and-neonatal-services-in-east-kent-reading-the-signals"},
            {"publisher": "NHS England", "title": "Maternity Transformation Programme", "url": "https://www.england.nhs.uk/mat-transformation/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "EKHUFT provider profile (RVV)", "url": "https://www.cqc.org.uk/provider/RVV"}
        ],
        "related": ["East Kent Hospitals University NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Frontline Digitisation programme", "Transport (business + patient) — East Kent Hospitals University NHS Foundation Trust", "General supplies & services — East Kent Hospitals University NHS Foundation Trust"]
    },
    "Business rates — London North West University Healthcare NHS Trust": {
        "aliases": [{"name": "Business rates", "parent": "London North West University Healthcare NHS Trust"}],
        "description": "LNWH's £5.22M business rates line covers non-domestic rates on the trust's three-site acute estate — Northwick Park Hospital (Harrow), Central Middlesex Hospital (Park Royal, Brent) and Ealing Hospital — plus the St Mark's national bowel-disease hospital (relocating to Northwick Park) and a community-clinic footprint across north-west London. Rates are billed by Harrow, Brent and Ealing London Borough Councils against VOA 2023 List rateable values, with central-London and high-density inner suburb rateable values driving exposure.",
        "beneficiaries": "c. 8,500 WTE staff serving a c. 850,000 north-west London catchment (Brent, Harrow, Ealing); c. 250,000 ED attendances/yr (Northwick Park + Ealing EDs — Northwick Park among London's busiest); c. 110,000 admissions/yr; St Mark's national bowel-disease referrals.",
        "legal_basis": "Local Government Finance Act 1988 (Schedule 6 — non-domestic rating) · Non-Domestic Rating (Multipliers and Private Finance) Act 2024 · Local Government Finance Act 1992 · DHSC Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£5.22M"},
            {"label": "Trust scale", "value": "Three-site acute (Northwick Park + Central Middlesex + Ealing) + St Mark's Hospital (national bowel disease) + community clinics; c. 8,500 WTE"},
            {"label": "Billing authorities", "value": "London Borough of Harrow (Northwick Park + St Mark's) + London Borough of Brent (Central Middlesex) + London Borough of Ealing (Ealing Hospital)"},
            {"label": "VOA 2023 List", "value": "Revaluation effective 1 Apr 2023 reset rateable values; transitional relief tapering"},
            {"label": "NDR multiplier 2024-25", "value": "54.6p (standard) / 49.9p (small)"},
            {"label": "London RV uplift", "value": "London RVs in VOA 2023 List rose materially — drives line above peer non-London multi-site trusts"},
            {"label": "St Mark's relocation", "value": "St Mark's Hospital national bowel disease centre relocation to Northwick Park progressing — reshapes future rateable assessment"},
            {"label": "ED throughput", "value": "Northwick Park among London's busiest EDs (c. 200,000+ attendances/yr); Ealing c. 50,000"},
            {"label": "Exemption position", "value": "Post-2020 Derby Teaching Hospitals v Derby CC ruling — NHS trusts pay full NDR (no charitable relief)"},
            {"label": "Funding trajectory", "value": "2021-22 c. £4.5M → 2023-24 £5.0M → 2024-25 £5.22M — VOA 2023 List uplift + multiplier indexation + London RV pressure"},
            {"label": "Delivery body", "value": "Trust E&F + Finance + LB Harrow + LB Brent + LB Ealing billing teams + Valuation Office Agency"},
            {"label": "Policy owner", "value": "MHCLG (NDR policy) + HM Treasury + DHSC + VOA + NHSE Provider Finance + NWL ICB"},
            {"label": "Evaluation evidence", "value": "NAO NHS estate report; CQC inspection R1K; HFMA NDR briefings; Trust ARA"}
        ],
        "notes": "LNWH was formed in October 2014 by merging North West London Hospitals NHS Trust (Northwick Park + Central Middlesex + St Mark's) with Ealing Hospital NHS Trust, consolidating three-borough rates exposure under one entity. London rateable values in the VOA 2023 List rose materially relative to non-London peers, driving the line above peer multi-site DGH groups. The St Mark's Hospital relocation — moving the national bowel-disease centre to Northwick Park — will reshape future rateable assessments. The Court of Appeal's 2019 Derby ruling confirmed NHS trusts pay full NDR. The 54.6p multiplier applies in 2024-25; NWL ICS estate rationalisation is the medium-term lever.",
        "sources": [
            {"publisher": "London North West University Healthcare NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.lnwh.nhs.uk/about-us/publications-and-reports/"},
            {"publisher": "Valuation Office Agency", "title": "2023 Rating List", "url": "https://www.gov.uk/government/collections/rating-2023-revaluation"},
            {"publisher": "Ministry of Housing, Communities and Local Government", "title": "Business rates: 2024-25 multipliers", "url": "https://www.gov.uk/introduction-to-business-rates"},
            {"publisher": "England and Wales Court of Appeal", "title": "Derby Teaching Hospitals NHS Foundation Trust v Derby City Council [2019] EWCA Civ 1320", "url": "https://www.bailii.org/ew/cases/EWCA/Civ/2019/1320.html"},
            {"publisher": "Care Quality Commission", "title": "LNWH provider profile (R1K)", "url": "https://www.cqc.org.uk/provider/R1K"}
        ],
        "related": ["London North West University Healthcare NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Business rates — Somerset NHS Foundation Trust", "Establishment costs — London North West University Healthcare NHS Trust", "Valuation Office Agency"]
    },
    "Transport (business + patient) — Frimley Health NHS Foundation Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "Frimley Health NHS Foundation Trust"}],
        "description": "Frimley Health's £5.22M transport line covers staff business mileage, inter-site clinical transfers and Non-Emergency Patient Transport Services across the trust's two-site acute footprint — Frimley Park Hospital (Camberley) and Wexham Park Hospital (Slough) — plus the Heatherwood Hospital elective centre (Ascot, opened 2022). SCAS is primary 999 carrier; the c. 20-mile Frimley Park – Wexham Park corridor sustains cross-site clinical-transfer demand. Frimley Park's RAAC-driven full rebuild commitment shapes medium-term inter-site activity.",
        "beneficiaries": "c. 9,500 WTE staff serving a c. 900,000 catchment across north-east Hampshire, west Surrey and east Berkshire; c. 230,000 ED attendances/yr (Frimley Park + Wexham Park EDs); c. 110,000 admissions/yr; new Heatherwood elective centre (opened Mar 2022) drives planned-care inter-site flow.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · IFRS 16 Leases (pool fleet) · NHS Act 2006 · NHSE Patient Transport Services Eligibility Framework 2022 · HMRC AMAP · NHS AfC Section 17 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£5.22M"},
            {"label": "Trust scale", "value": "Two acute (Frimley Park Camberley + Wexham Park Slough) + Heatherwood elective centre (Ascot, opened Mar 2022); c. 9,500 WTE"},
            {"label": "Inter-site geography", "value": "c. 20 miles between Frimley Park and Wexham Park via M3/M25/M4 — drives cross-site clinical transfer baseline"},
            {"label": "Frimley Park RAAC + NHP", "value": "Frimley Park retained in NHP cohort post Jan 2025 Reset; full RAAC-driven rebuild commitment — drives long-term inter-site activity reshaping"},
            {"label": "Heatherwood elective", "value": "New Heatherwood Hospital opened Mar 2022 (c. £100M elective surgical hub) — drives planned-care inter-site patient flows"},
            {"label": "PTS provider mix + ICS footprint", "value": "SCAS for 999 + accredited NEPTS contractors; trust crosses Frimley ICS, BOB ICS and HIOW ICS — multi-ICS commissioning complexity"},
            {"label": "ED throughput", "value": "c. 230,000 attendances/yr (Frimley Park + Wexham Park combined)"},
            {"label": "Staff + pool fleet", "value": "AfC Section 17 / HMRC AMAP 45p first 10,000 miles + 25p thereafter; IFRS 16 right-of-use on leased pool vehicles"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove ad-hoc inter-site transfer + locum mileage"},
            {"label": "Funding trajectory", "value": "2021-22 c. £4.3M → 2023-24 £4.9M → 2024-25 £5.22M — fuel CPI + Heatherwood elective opening"},
            {"label": "Delivery body", "value": "Trust E&F + Travel team + SCAS + accredited NEPTS contractor pool"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + NHSE NEPTS framework + Frimley ICB + (cross-ICS) BOB ICB + HIOW ICB"},
            {"label": "Evaluation evidence", "value": "NHSE NEPTS Eligibility Framework 2022; CQC inspection RDU; NHP business case; Trust ARA"}
        ],
        "notes": "Frimley Health's transport baseline is shaped by its two-site acute footprint plus the Heatherwood elective centre opened March 2022, with sustained cross-site transfer demand on the c. 20-mile Frimley Park–Wexham Park corridor and planned-care flows to Heatherwood. Frimley Park is one of the highest-priority sites in the New Hospital Programme post the January 2025 Reset — RAAC presence at the existing site has driven full-rebuild commitment, with rebuild planning reshaping long-term inter-site demand. The trust crosses three ICS footprints (Frimley, BOB, HIOW), adding NEPTS commissioning complexity. Industrial action 2023-24 added ad-hoc transfer and locum mileage. Fuel CPI and April 2025 NIC pass-through to PTS contractors are dominant near-term drivers.",
        "sources": [
            {"publisher": "Frimley Health NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.fhft.nhs.uk/about-us/our-publications/"},
            {"publisher": "NHS England", "title": "New Hospital Programme — January 2025 Reset", "url": "https://www.gov.uk/government/publications/new-hospital-programme-update"},
            {"publisher": "NHS England", "title": "Non-Emergency Patient Transport Services Eligibility Framework 2022", "url": "https://www.england.nhs.uk/long-read/non-emergency-patient-transport-services-eligibility-framework/"},
            {"publisher": "South Central Ambulance Service NHS Foundation Trust", "title": "Annual Report 2023-24", "url": "https://www.scas.nhs.uk/about-us/our-publications/"},
            {"publisher": "Care Quality Commission", "title": "Frimley Health provider profile (RDU)", "url": "https://www.cqc.org.uk/provider/RDU"}
        ],
        "related": ["Frimley Health NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "New Hospital Programme", "Transport (business + patient) — North Cumbria Integrated Care NHS Foundation Trust", "Establishment costs — Frimley Health NHS Foundation Trust"]
    },
    "General supplies & services — Barnsley Hospital NHS Foundation Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "Barnsley Hospital NHS Foundation Trust"}],
        "description": "Barnsley Hospital NHS FT's £5.21M general supplies & services line covers non-clinical consumables, linen, catering provisions, hotel-services materials, office supplies, IT consumables and minor expensed equipment at the single-site Barnsley District General Hospital. The trust operates within the South Yorkshire ICS provider collaborative alongside Sheffield Teaching Hospitals, Doncaster & Bassetlaw and Rotherham, with a chair-in-common arrangement with Sheffield Teaching Hospitals NHS FT (since 2022) shaping medium-term back-office and procurement consolidation.",
        "beneficiaries": "c. 3,500 WTE staff serving a c. 245,000 Barnsley borough catchment; c. 90,000 ED attendances/yr at Barnsley Hospital ED; c. 35,000 admissions/yr; community-clinic activity through the Barnsley Hospital Outpatient + Diagnostics network.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 2 Inventories · Procurement Act 2023 · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "General supplies & services 2024-25", "value": "£5.21M"},
            {"label": "Trust scale", "value": "Single acute site (Barnsley District General Hospital, Gawber Road); c. 3,500 WTE"},
            {"label": "ED throughput", "value": "c. 90,000 attendances/yr"},
            {"label": "Catchment deprivation", "value": "Barnsley borough — high IMD deprivation; sustains acute consumable demand on emergency-care pathway"},
            {"label": "Procurement route", "value": "NHS Supply Chain national framework + South Yorkshire ICS collaborative + trust-direct contracts"},
            {"label": "Group-model context", "value": "Chair-in-common with Sheffield Teaching Hospitals NHS FT since 2022; shared corporate functions developing under South Yorkshire ICS"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove cancellation-related re-stocking churn + agency backfill"},
            {"label": "Composition", "value": "Linen + catering + hotel services + office supplies + IT consumables + minor expensed equipment below capitalisation threshold"},
            {"label": "April 2025 NIC + CPI uplift", "value": "Apr 2025 employer-NIC step-up + non-clinical CPI feed forward unit-cost pressure"},
            {"label": "Funding trajectory", "value": "2021-22 c. £4.4M → 2023-24 £4.9M → 2024-25 £5.21M — sustained CPI + activity uplift"},
            {"label": "Delivery body", "value": "Trust Procurement + Supply Chain team + NHS Supply Chain (DHSC ALB) + (developing) Sheffield Teaching Hospitals shared functions + South Yorkshire ICS procurement collaborative"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + South Yorkshire ICB"},
            {"label": "Evaluation evidence", "value": "Model Hospital benchmarks; CQC inspection RFF; NHS Supply Chain ARA; Trust ARA disclosure; chair-in-common transaction"}
        ],
        "notes": "Barnsley Hospital NHS FT is a single-site DGH in the heart of the Barnsley borough, with a long-running deprivation profile sustaining acute and emergency-care consumable demand. The chair-in-common arrangement with Sheffield Teaching Hospitals NHS FT (in place since 2022) is reshaping back-office function ownership and procurement consolidation under South Yorkshire ICS, alongside parallel collaborative arrangements with Doncaster & Bassetlaw and The Rotherham NHS FT. NHS Supply Chain remains the dominant delivery channel. Industrial action 2023-24 drove agency-backfill consumable churn through cancellation re-stocking. April 2025 NIC step-up and sustained CPI on non-clinical inputs (linen, catering, hotel services, IT consumables) feed forward unit-cost pressure.",
        "sources": [
            {"publisher": "Barnsley Hospital NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.barnsleyhospital.nhs.uk/about-us/our-publications/"},
            {"publisher": "NHS Supply Chain", "title": "Annual Report 2023-24", "url": "https://www.supplychain.nhs.uk/about-us/our-publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Barnsley Hospital provider profile (RFF)", "url": "https://www.cqc.org.uk/provider/RFF"},
            {"publisher": "South Yorkshire ICB", "title": "Provider collaborative arrangements", "url": "https://syics.co.uk/"}
        ],
        "related": ["Barnsley Hospital NHS Foundation Trust", "Clinical Supplies & Drugs", "NHS Acute Trusts", "NHS Supply Chain", "General supplies & services — The Rotherham NHS Foundation Trust", "Sheffield Teaching Hospitals NHS Foundation Trust"]
    },
    "Establishment costs — Walsall Healthcare NHS Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "Walsall Healthcare NHS Trust"}],
        "description": "Walsall Healthcare NHS Trust's £5.20M establishment costs line covers postage, telephony, printing, advertising, hospitality, training, courses, professional fees and other operating-cost categories at the single-site Walsall Manor Hospital plus the integrated Walsall borough community service estate. The trust is in active group-model integration with Royal Wolverhampton NHS Trust under the Black Country Provider Collaborative (chair-in-common since 2020), with shared corporate functions and back-office consolidation reshaping the establishment-cost reporting boundary.",
        "beneficiaries": "c. 4,500 WTE staff serving a c. 285,000 Walsall borough catchment; c. 110,000 ED attendances/yr at Walsall Manor ED; c. 50,000 admissions/yr; integrated borough-wide community services (district nursing + therapies + community-paediatric + sexual-health).",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · NHS Act 2006 · Health and Care Act 2022 · Procurement Act 2023 · NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£5.20M"},
            {"label": "Trust scale", "value": "Single acute site (Walsall Manor Hospital, Moat Road) + integrated Walsall borough community services; c. 4,500 WTE"},
            {"label": "Group-model context", "value": "Royal Wolverhampton + Walsall Healthcare chair-in-common since 2020 → Black Country Provider Collaborative; shared corporate functions developing"},
            {"label": "Frontline Digitisation EPR", "value": "EPR adoption + optimisation drives change-management + training establishment cost; aligned with RWT under group-model"},
            {"label": "Composition", "value": "Postage + telephony + printing + advertising + hospitality + training + courses + professional fees + minor non-clinical operating items"},
            {"label": "Catchment deprivation", "value": "Walsall borough — high IMD deprivation; sustains training + community-comms spend"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove additional comms + training + locum-onboarding establishment cost"},
            {"label": "April 2025 NIC + CPI uplift", "value": "Apr 2025 employer-NIC step-up flows through professional-services suppliers + non-pay CPI on print, postage, telephony"},
            {"label": "Black Country ICS", "value": "Provider Collaborative shared-corporate-functions agenda with Royal Wolverhampton, Sandwell & West Birmingham, Dudley shapes medium-term professional-fees consolidation"},
            {"label": "Funding trajectory", "value": "2021-22 c. £4.3M → 2023-24 £4.8M → 2024-25 £5.20M — sustained CPI + EPR-related professional fees + group-model transition cost"},
            {"label": "Delivery body", "value": "Trust Finance + Procurement + IT + HR/OD + (developing) Black Country Provider Collaborative shared functions; external advisors + EPR vendor + training providers"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Black Country ICB + NHSE Frontline Digitisation programme"},
            {"label": "Evaluation evidence", "value": "Model Hospital benchmarks; CQC inspection RBK; Black Country group-model business case; NHSE Frontline Digitisation; Trust ARA"}
        ],
        "notes": "Walsall Healthcare's establishment-cost baseline reflects an integrated acute + community trust at the heart of the developing group-model relationship with Royal Wolverhampton NHS Trust under the Black Country Provider Collaborative — chair-in-common since 2020 has shaped shared back-office and corporate-functions consolidation, with transition cost feeding through professional fees. Frontline Digitisation EPR optimisation drives change-management and training. Industrial action 2023-24 added comms and locum-onboarding cost. April 2025 NIC step-up flows through suppliers; non-pay CPI feeds forward. Black Country ICS provider-collaborative consolidation will progressively reshape the corporate-cost boundary.",
        "sources": [
            {"publisher": "Walsall Healthcare NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.walsallhealthcare.nhs.uk/about-us/publications/"},
            {"publisher": "Black Country ICB", "title": "Black Country Provider Collaborative + group-model arrangements", "url": "https://blackcountry.icb.nhs.uk/"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/connecting-health-and-care-providers/frontline-digitisation/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Walsall Healthcare provider profile (RBK)", "url": "https://www.cqc.org.uk/provider/RBK"}
        ],
        "related": ["Walsall Healthcare NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "The Royal Wolverhampton NHS Trust", "Social security & levy — Walsall Healthcare NHS Trust", "Frontline Digitisation programme"]
    },
    "Amortisation — Cambridge University Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Amortisation", "parent": "Cambridge University Hospitals NHS Foundation Trust"}],
        "description": "CUHFT's £5.19M amortisation line covers systematic write-down of recognised intangible assets at the trust — predominantly capitalised software and licences related to the Epic EPR (deployed Oct 2014, the first NHS Epic implementation) plus the Cambridge Biomedical Research Centre research-software estate, supplementary clinical-system modules, and intangible-asset components arising from major capital programmes. Amortisation is driven by the Epic asset's useful-economic-life recycling and IFRS 16 / IAS 38 treatment under DHSC GAM ch.5.",
        "beneficiaries": "c. 13,000 WTE staff serving a c. 1.0M Cambridgeshire local catchment plus extended East of England and national tertiary referrals (c. 5M+) for transplant, neurosurgery, paediatrics and rare disease; c. 130,000 ED attendances/yr at Addenbrooke's ED; c. 230,000 admissions/yr (incl. nationally-commissioned highly specialised activity).",
        "legal_basis": "IAS 38 Intangible Assets · DHSC Group Accounting Manual 2024-25 ch.5 · IFRS 16 Leases · NHS Act 2006 · Health and Care Act 2022 · National Health Service Foundation Trust Annual Reports and Accounts Manual",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£5.19M"},
            {"label": "Trust scale", "value": "Single major site (Addenbrooke's + Rosie Hospital, Cambridge Biomedical Campus); c. 13,000 WTE"},
            {"label": "Specialty footprint", "value": "Major Trauma Centre + national specialist transplant + neurosurgery + paediatric + rare-disease centre + Cambridge BRC anchor"},
            {"label": "Epic EPR", "value": "Cambridge first NHS Epic implementation (go-live Oct 2014, eHospital programme); capitalised intangible asset baseline drove sustained amortisation cycle"},
            {"label": "Frontline Digitisation EPR cycle", "value": "Epic optimisation + module rollouts feed continued capitalisation + amortisation cycle"},
            {"label": "Useful economic life", "value": "Software / licences typically 5-10 years per IAS 38 + DHSC GAM ch.5 application"},
            {"label": "Cambridge Biomedical Research Centre", "value": "NIHR BRC anchor + research-software intangibles add to amortisation base"},
            {"label": "Composition", "value": "Capitalised software + licences + acquired intangibles; clinical-system module amortisation; research-software amortisation"},
            {"label": "Cambridge Children's Hospital", "value": "New dedicated children's hospital programme on Cambridge Biomedical Campus — capital build under NHP cohort post Reset; future intangible additions on commissioning"},
            {"label": "Funding trajectory", "value": "Stabilised post-2014 Epic baseline; £5.19M reflects mature amortisation cycle on existing intangibles plus marginal new additions"},
            {"label": "Delivery body", "value": "Trust Finance + IT + Capital Programme team + Epic Systems Corporation (EPR vendor) + research-software vendors"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + NHSE Frontline Digitisation + Cambridge & Peterborough ICB + NIHR"},
            {"label": "Evaluation evidence", "value": "NAO eHospital reporting; NHSE Frontline Digitisation returns; Trust ARA; CQC inspection RGT (Outstanding)"}
        ],
        "notes": "CUHFT was the first NHS organisation to deploy Epic Systems Corporation's electronic patient record, going live in October 2014 under the eHospital programme — establishing a substantial capitalised intangible-asset baseline that has driven sustained amortisation cycles since. The trust is a flagship academic and research provider with the Cambridge Biomedical Research Centre (NIHR-funded) and major nationally-commissioned tertiary referral activity in transplant, neurosurgery and rare disease. The new Cambridge Children's Hospital on the Cambridge Biomedical Campus, in the NHP cohort post the January 2025 Reset, will drive further intangible additions on commissioning. Amortisation is calculated under IAS 38 per DHSC GAM ch.5; Epic module rollouts continue to feed the cycle.",
        "sources": [
            {"publisher": "Cambridge University Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.cuh.nhs.uk/about-us/our-publications/annual-reports/"},
            {"publisher": "National Audit Office", "title": "Digital transformation in the NHS (incl. Cambridge eHospital)", "url": "https://www.nao.org.uk/reports/the-use-of-digital-technology-in-the-nhs/"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/connecting-health-and-care-providers/frontline-digitisation/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 5 — Intangible Assets)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Cambridge University Hospitals provider profile (RGT) — Outstanding rated", "url": "https://www.cqc.org.uk/provider/RGT"}
        ],
        "related": ["Cambridge University Hospitals NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Frontline Digitisation programme", "Amortisation — Mid and South Essex NHS Foundation Trust", "Establishment costs — Cambridge University Hospitals NHS Foundation Trust"]
    },
    "General supplies & services — Northampton General Hospital NHS Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "Northampton General Hospital NHS Trust"}],
        "description": "Northampton General's £5.14M general supplies & services line covers non-clinical consumables, linen, catering provisions, hotel-services materials, office supplies, IT consumables and minor expensed equipment at the single-site Northampton General Hospital site (Cliftonville). The trust is in active group-model arrangements with Kettering General Hospital NHS FT under the University Hospitals of Northamptonshire Group (chair-in-common since 2021, joint-CEO arrangement) — shaping medium-term procurement consolidation across the Northamptonshire ICS acute footprint.",
        "beneficiaries": "c. 5,000 WTE staff serving a c. 380,000 south Northamptonshire catchment (Northampton, Daventry, South Northants); c. 130,000 ED attendances/yr at Northampton General ED; c. 65,000 admissions/yr; c. 5,000 deliveries/yr maternity service.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 2 Inventories · Procurement Act 2023 · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "General supplies & services 2024-25", "value": "£5.14M"},
            {"label": "Trust scale", "value": "Single acute site (Northampton General Hospital, Cliftonville); c. 5,000 WTE"},
            {"label": "ED throughput", "value": "c. 130,000 attendances/yr"},
            {"label": "Maternity scale", "value": "c. 5,000 deliveries/yr"},
            {"label": "Procurement route", "value": "NHS Supply Chain national framework + UHN Group joint-procurement (with Kettering General) + trust-direct contracts"},
            {"label": "UHN Group context", "value": "University Hospitals of Northamptonshire Group: chair-in-common since 2021 + joint-CEO with Kettering General Hospital NHS FT — single-county Northamptonshire ICS dominated by UHN Group"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove cancellation-related re-stocking churn + agency backfill"},
            {"label": "Composition", "value": "Linen + catering + hotel services + office supplies + IT consumables + minor expensed equipment below capitalisation threshold"},
            {"label": "April 2025 NIC + CPI uplift", "value": "Apr 2025 employer-NIC step-up + non-clinical CPI feed forward unit-cost pressure"},
            {"label": "Funding trajectory", "value": "2021-22 c. £4.4M → 2023-24 £4.8M → 2024-25 £5.14M — sustained CPI + activity uplift + UHN joint-procurement scaling"},
            {"label": "Delivery body", "value": "Trust Procurement + Supply Chain team + NHS Supply Chain (DHSC ALB) + UHN Group joint-procurement + Northamptonshire ICS collaborative"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Northamptonshire ICB"},
            {"label": "Evaluation evidence", "value": "Model Hospital benchmarks; CQC inspection RNS; NHS Supply Chain ARA; Trust ARA disclosure; UHN Group business case"}
        ],
        "notes": "Northampton General Hospital NHS Trust is one half of the University Hospitals of Northamptonshire Group — the developing group-model partnership with Kettering General Hospital NHS FT (chair-in-common since 2021, joint-CEO) covers the entirety of Northamptonshire ICS acute provision and is reshaping back-office and procurement functions. NHS Supply Chain remains the dominant delivery channel; UHN Group joint-procurement scaling is the medium-term consolidation lever. Industrial action 2023-24 drove agency-backfill consumable churn through cancellation re-stocking and elective recovery. April 2025 NIC step-up flows through supplier pass-through, and sustained CPI on non-clinical inputs (linen, catering, hotel services, IT consumables) feeds forward unit-cost pressure.",
        "sources": [
            {"publisher": "Northampton General Hospital NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.northamptongeneral.nhs.uk/About/Publications/AnnualReportandAccounts.aspx"},
            {"publisher": "NHS Supply Chain", "title": "Annual Report 2023-24", "url": "https://www.supplychain.nhs.uk/about-us/our-publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Northampton General Hospital provider profile (RNS)", "url": "https://www.cqc.org.uk/provider/RNS"},
            {"publisher": "University Hospitals of Northamptonshire Group", "title": "UHN Group corporate overview", "url": "https://www.northamptongeneral.nhs.uk/About/UniversityHospitalsofNorthamptonshire/"}
        ],
        "related": ["Northampton General Hospital NHS Trust", "Clinical Supplies & Drugs", "NHS Acute Trusts", "NHS Supply Chain", "Kettering General Hospital NHS Foundation Trust", "General supplies & services — Barnsley Hospital NHS Foundation Trust"]
    },
}
