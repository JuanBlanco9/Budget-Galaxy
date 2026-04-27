# -*- coding: utf-8 -*-
# Phase 2 SCamb — chunk 15 (17 NHS Specialist/Community/Ambulance Trust orphan sub-lines)
# Hand-curated trust-specific PROGRAMME-archetype enrichment entries.
# Structural contract per docs/archetype_briefs.md.

NEW = {
    "Drugs costs — East Midlands Ambulance Service NHS Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "East Midlands Ambulance Service NHS Trust"}],
        "description": "EMAS's £0.57M drugs-costs line covers pre-hospital pharmaceuticals carried on the trust's c. 600+ frontline ambulance, RRV and CFR fleet across the five East Midlands counties (Derbyshire, Leicestershire, Lincolnshire, Northamptonshire, Nottinghamshire). The line includes paramedic-administered analgesics (paracetamol, morphine sulfate, ibuprofen), cardiac drugs (adrenaline, amiodarone, GTN), Entonox cylinders (50/50 N2O/O2), naloxone for opioid overdose reversal, salbutamol/ipratropium nebs, glucagon and antiemetics, sourced via NHS Supply Chain pharmacy framework and stocked at Make Ready Centres at Beechdale (Nottingham), Hucknall, Long Eaton, Lincoln, Leicester and Northampton.",
        "beneficiaries": "Serves a c. 4.9M East Midlands population across 6,400 sq miles; responds to c. 920,000 incidents/yr (c. 760,000 see-and-treat or convey + c. 160,000 hear-and-treat) with c. 3,800 WTE staff including c. 2,400 paramedics + ECAs + technicians + EOC call-handlers operating from c. 70 ambulance stations and 7 hub/Make Ready Centres.",
        "legal_basis": "NHS Act 2006 · Health and Care Act 2022 · Human Medicines Regulations 2012 (paramedic exemptions Sch 17 + Sch 19 PGD provisions) · Misuse of Drugs Regs 2001 (Sch 2-5 controlled drugs incl. morphine) · NHS Supply Chain pharmacy framework · DHSC Group Accounting Manual 2024-25",
        "key_stats": [
            {"label": "Drugs costs 2024-25", "value": "£0.57M"},
            {"label": "Specialty footprint", "value": "Regional 999 ambulance service — Derbyshire, Leicestershire, Lincolnshire, Northamptonshire, Nottinghamshire (5 counties · 6,400 sq miles)"},
            {"label": "Population served", "value": "c. 4.9M East Midlands residents"},
            {"label": "Annual activity", "value": "c. 920,000 incidents; c. 760,000 face-to-face responses + c. 160,000 hear-and-treat; c. 540,000 conveyances to ED"},
            {"label": "Workforce", "value": "c. 3,800 WTE; c. 2,400 paramedics + ECAs + technicians; EOC at Nottingham (Beechdale) + Lincoln backup"},
            {"label": "Estate", "value": "c. 70 ambulance stations + 7 Make Ready Centres at Beechdale, Hucknall, Long Eaton, Lincoln, Leicester, Northampton, Derby"},
            {"label": "Drug stock profile", "value": "Paramedic POM exemptions (adrenaline, GTN, naloxone, salbutamol, paracetamol, morphine sulfate via PGD) + Entonox cylinders + IV fluids; CD register controls under Misuse of Drugs Regs"},
            {"label": "Procurement route", "value": "NHS Supply Chain pharmacy framework + direct manufacturer contracts for Entonox (BOC) + CD wholesalers"},
            {"label": "Funding trajectory", "value": "Rising 4-7%/yr post-pandemic on Cat-2 demand growth + naloxone scale-up under DHSC drug-deaths plan + VAT and global API price pressure"},
            {"label": "Delivery body", "value": "EMAS Pharmacy lead + Make Ready Centre stock teams + NHS Supply Chain + paramedic dispensary at station level"},
            {"label": "Policy owner", "value": "NHSE Urgent and Emergency Care + MHRA (medicines regulation) + DHSC + Home Office (CDs) + East Midlands ICBs (commissioning)"},
            {"label": "Evaluation evidence", "value": "EMAS ARA; CQC inspection (RX9 — currently rated Requires Improvement at last inspection); ORH ambulance benchmarks; AACE national activity reports"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2006 county-level ambulance services merged into EMAS · Successor: NHSE 10-year drugs-deaths naloxone scale-up + ARP (Ambulance Response Programme) Cat-1/2 demand growth"}
        ],
        "notes": "Drugs costs are a small but operationally critical line for ambulance trusts — the c. £0.57M reflects EMAS's status as the smallest of the 10 English regional ambulance services by income, plus a relatively young paramedic specialist-practitioner workforce dispensing under PGD vs full prescribing. Cost drivers include the c. 920,000 annual incidents (paramedic-administered analgesia and cardiac drugs are the bulk volume), the rural-Lincolnshire long-tail-of-stations stock, and naloxone scale-up under the DHSC drug-deaths plan from 2022. Recent context includes the 2023-24 industrial action (paramedic strikes by GMB and Unison) which did not materially affect drug consumption, and rising NHS Supply Chain framework prices on Entonox, morphine and saline.",
        "sources": [
            {"publisher": "East Midlands Ambulance Service NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.emas.nhs.uk/about-us/our-publications/annual-reports/"},
            {"publisher": "Care Quality Commission", "title": "East Midlands Ambulance Service NHS Trust provider profile (RX9)", "url": "https://www.cqc.org.uk/provider/RX9"},
            {"publisher": "NHS England", "title": "Ambulance Response Programme (ARP) — Cat-1/Cat-2 standards", "url": "https://www.england.nhs.uk/urgent-emergency-care/improving-ambulance-services/arp/"},
            {"publisher": "MHRA / UK Government", "title": "Human Medicines Regulations 2012 (paramedic exemptions Schs 17/19)", "url": "https://www.legislation.gov.uk/uksi/2012/1916/contents"},
            {"publisher": "Department of Health and Social Care", "title": "From harm to hope — 10-year drugs strategy and naloxone provision", "url": "https://www.gov.uk/government/publications/from-harm-to-hope-a-10-year-drugs-plan-to-cut-crime-and-save-lives"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"}
        ],
        "related": ["East Midlands Ambulance Service NHS Trust", "Clinical Supplies & Drugs", "NHS Ambulance Trusts", "Drugs costs — North East Ambulance Service NHS Foundation Trust", "Drugs costs — West Midlands Ambulance Service University NHS Foundation Trust", "NHS Supply Chain"]
    },
    "Transport (business + patient) — The Walton Centre NHS Foundation Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "The Walton Centre NHS Foundation Trust"}],
        "description": "The Walton Centre's £0.57M transport line covers business mileage (AMAP) for clinical and outreach staff travelling between the Fazakerley campus and outreach neurology / neuro-rehab clinics across Cheshire, Merseyside, Lancashire, Cumbria, Isle of Man and North Wales, plus pool-car leases and patient-transport reimbursements under NHSE PTS eligibility for neurology, neurosurgery, complex spinal and pain-management patients travelling for surgery, follow-up clinics or rehab. Specialist couriers transport pathology samples, neuropath specimens and CSF between the centre and partner labs across the supra-regional catchment.",
        "beneficiaries": "Serves a c. 3.5M supra-regional neuro catchment across Cheshire, Merseyside, Lancashire, Cumbria, the Isle of Man and North Wales as the only standalone specialist neurosciences trust in the UK; treats c. 60,000 outpatient attendances + c. 5,000 neurosurgical procedures + c. 13,000 spell admissions/yr; c. 1,600 WTE staff at the Fazakerley main site + Sid Watkins building outreach.",
        "legal_basis": "NHS Act 2006 · NHSE Patient Transport Services Eligibility Criteria · Healthcare Travel Costs Scheme (HTCS) · Agenda for Change s.17 + HMRC Approved Mileage Allowance Payments · IFRS 16 Leases (pool fleet) · DHSC Group Accounting Manual 2024-25",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£0.57M"},
            {"label": "Specialty footprint", "value": "UK's only standalone specialist neurosciences NHS trust — neurology, neurosurgery, complex spinal, neuro-rehab, pain"},
            {"label": "Supra-regional catchment", "value": "c. 3.5M across Cheshire, Merseyside, Lancashire, Cumbria, Isle of Man, North Wales"},
            {"label": "Annual activity", "value": "c. 60,000 outpatient attendances; c. 5,000 neurosurgery cases; c. 13,000 spell admissions; c. 200 deep-brain stimulation procedures/yr"},
            {"label": "Workforce", "value": "c. 1,600 WTE; c. 100 consultants in neurology/neurosurgery/anaesthetics/rehab"},
            {"label": "PTS driver", "value": "Long-distance follow-up neurology and post-op spinal/neurosurgery clinics; Cumbria + IoM patient transfers"},
            {"label": "Specialist couriers", "value": "Pathology + neuropath + CSF samples between Fazakerley and partner labs (Liverpool Clinical Labs, RLBUH)"},
            {"label": "Funding trajectory", "value": "Modest growth driven by IFRS 16 lease re-recognition (2022) + AMAP mileage rate freeze gap + outreach clinic expansion"},
            {"label": "Delivery body", "value": "Walton Centre Estates & Facilities + leased-pool-car supplier + Mersey + N Wales pathology courier services"},
            {"label": "Policy owner", "value": "NHSE Specialised Commissioning (neurosciences) + DHSC + Cheshire & Merseyside ICB"},
            {"label": "Evaluation evidence", "value": "Walton Centre ARA; CQC inspection (RET — Outstanding 2019); Model Hospital neurosciences benchmarks; Getting It Right First Time (GIRFT) neurosurgery"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-IFRS-16 lease accounting · Successor: continued outreach expansion + zero-emission pool fleet under NHSE Net Zero 2032"}
        ],
        "notes": "The Walton Centre is the UK's only standalone specialist neurosciences NHS trust, with a supra-regional catchment of c. 3.5M across the North West, Cumbria, Isle of Man and North Wales — meaning patient transport reimbursement under HTCS is structurally elevated for long-distance follow-up neurology and post-op spinal patients. The transport line is small in absolute terms because activity concentrates at the single Fazakerley campus, but specialist neuropath / CSF couriers and pool-car leases for outreach clinics dominate the cost mix. Drivers include IFRS 16 lease re-recognition from 2022, AMAP rate freeze (45p/25p unchanged since 2011) widening real-terms cost gap, and gradual EV pool-car transition under NHS Net Zero 2032.",
        "sources": [
            {"publisher": "The Walton Centre NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.thewaltoncentre.nhs.uk/about-us/our-publications/annual-reports/"},
            {"publisher": "Care Quality Commission", "title": "The Walton Centre NHS Foundation Trust provider profile (RET)", "url": "https://www.cqc.org.uk/provider/RET"},
            {"publisher": "NHS England", "title": "Healthcare Travel Costs Scheme (HTCS)", "url": "https://www.nhs.uk/nhs-services/help-with-health-costs/healthcare-travel-costs-scheme-htcs/"},
            {"publisher": "NHS England", "title": "Specialised commissioning — neurosciences service specifications", "url": "https://www.england.nhs.uk/commissioning/spec-services/npc-crg/group-d/d04/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "NHS Net Zero — delivering a net zero NHS", "url": "https://www.england.nhs.uk/greenernhs/a-net-zero-nhs/"}
        ],
        "related": ["The Walton Centre NHS Foundation Trust", "Premises & Infrastructure", "NHS Specialist Trusts", "Transport (business + patient) — The Christie NHS Foundation Trust", "Transport (business + patient) — Royal National Orthopaedic Hospital NHS Trust", "NHS England"]
    },
    "Drugs costs — North East Ambulance Service NHS Foundation Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "North East Ambulance Service NHS Foundation Trust"}],
        "description": "NEAS's £0.57M drugs-costs line covers pre-hospital pharmaceuticals carried on the trust's frontline ambulance, RRV and PTS fleet across the North East England footprint (Northumberland, Tyne & Wear, County Durham, Tees Valley, Hartlepool, Darlington). The line includes paramedic-administered analgesics (paracetamol, morphine sulfate via PGD, ibuprofen), cardiac drugs (adrenaline, amiodarone, GTN), Entonox cylinders, naloxone, salbutamol/ipratropium nebs and antiemetics, sourced via NHS Supply Chain pharmacy framework. The trust operates Make Ready Centres at Newburn (Newcastle), Russell House (Hebburn), Coulby Newham (Middlesbrough) and Pity Me (Durham).",
        "beneficiaries": "Serves a c. 2.7M North East population across c. 3,230 sq miles; responds to c. 600,000 incidents/yr (c. 480,000 face-to-face responses + c. 120,000 hear-and-treat) with c. 2,800 WTE staff including c. 1,800 paramedics + ECAs + technicians + EOC at Bernicia House (Newburn) and operates from c. 60 ambulance stations + 4 hub/Make Ready Centres.",
        "legal_basis": "NHS Act 2006 · Health and Care Act 2022 · Human Medicines Regulations 2012 (paramedic exemptions Sch 17 + Sch 19 PGD) · Misuse of Drugs Regs 2001 (CDs incl. morphine) · NHS Supply Chain pharmacy framework · DHSC Group Accounting Manual 2024-25",
        "key_stats": [
            {"label": "Drugs costs 2024-25", "value": "£0.57M"},
            {"label": "Specialty footprint", "value": "Regional 999 + 111 ambulance service — Northumberland, Tyne & Wear, Durham, Tees Valley (4 ICB sub-areas)"},
            {"label": "Population served", "value": "c. 2.7M North East residents"},
            {"label": "Annual activity", "value": "c. 600,000 incidents; c. 480,000 face-to-face responses; c. 350,000 conveyances; 111-IUC contract in-house"},
            {"label": "Workforce", "value": "c. 2,800 WTE; c. 1,800 paramedics + ECAs + technicians; EOC at Bernicia House (Newburn)"},
            {"label": "Estate", "value": "c. 60 ambulance stations + 4 Make Ready Centres at Newburn, Russell House (Hebburn), Coulby Newham, Pity Me (Durham)"},
            {"label": "Drug stock profile", "value": "Paramedic POM exemptions (adrenaline, GTN, naloxone, salbutamol, paracetamol, morphine sulfate via PGD) + Entonox + IV fluids + antiemetics; CD register controls"},
            {"label": "Procurement route", "value": "NHS Supply Chain pharmacy framework + BOC for Entonox + CD wholesalers"},
            {"label": "Funding trajectory", "value": "Rising on Cat-2 demand + naloxone scale-up under DHSC drug-deaths plan + winter pressures backfill drugs spend"},
            {"label": "Delivery body", "value": "NEAS Pharmacy + Make Ready stock teams + NHS Supply Chain"},
            {"label": "Policy owner", "value": "NHSE Urgent and Emergency Care + MHRA + DHSC + Home Office (CDs) + 4 North East ICBs (Newcastle/Gateshead, North Cumbria & North East, Tees Valley, County Durham)"},
            {"label": "Evaluation evidence", "value": "NEAS ARA; CQC inspection (RX6 — Requires Improvement following 111-IUC governance findings); ORH benchmarks; AACE national activity"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2006 county-level NE ambulance services merged · Successor: post-Marsh Review governance reforms + naloxone scale-up + ARP demand growth"}
        ],
        "notes": "NEAS has had a turbulent recent history with the 2022-23 Marsh Review into governance and 111-IUC concerns, leading to leadership changes and new oversight under NHSE / North East ICBs. Drugs costs are a small but operationally critical line — the c. £0.57M reflects c. 600,000 annual incidents and a paramedic-led PGD model. Drivers include naloxone scale-up under the DHSC From Harm to Hope 10-year drugs strategy (active distribution to bystanders), rising Entonox costs under BOC contract uplifts, and global API pressure on saline / paracetamol. The 2023-24 GMB+Unison paramedic strikes did not materially affect drug consumption.",
        "sources": [
            {"publisher": "North East Ambulance Service NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.neas.nhs.uk/about-us/our-publications/annual-reports.aspx"},
            {"publisher": "Care Quality Commission", "title": "North East Ambulance Service NHS Foundation Trust provider profile (RX6)", "url": "https://www.cqc.org.uk/provider/RX6"},
            {"publisher": "NHS England", "title": "Ambulance Response Programme — Cat-1/Cat-2 standards", "url": "https://www.england.nhs.uk/urgent-emergency-care/improving-ambulance-services/arp/"},
            {"publisher": "Dame Marianne Griffiths / NHSE", "title": "NEAS Marsh Review and follow-up actions", "url": "https://www.neas.nhs.uk/about-us/marsh-review.aspx"},
            {"publisher": "Department of Health and Social Care", "title": "From harm to hope — 10-year drugs strategy and naloxone provision", "url": "https://www.gov.uk/government/publications/from-harm-to-hope-a-10-year-drugs-plan-to-cut-crime-and-save-lives"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"}
        ],
        "related": ["North East Ambulance Service NHS Foundation Trust", "Clinical Supplies & Drugs", "NHS Ambulance Trusts", "Drugs costs — East Midlands Ambulance Service NHS Trust", "Drugs costs — West Midlands Ambulance Service University NHS Foundation Trust", "NHS England"]
    },
    "Amortisation — Birmingham Community Healthcare NHS Foundation Trust": {
        "aliases": [{"name": "Amortisation", "parent": "Birmingham Community Healthcare NHS Foundation Trust"}],
        "description": "BCHC's £0.56M amortisation charge represents the systematic write-down of intangible assets — chiefly software licences, EPR/clinical system development costs, and other capitalised intangibles — across the trust's c. 70+ community health sites including community hospitals at Moseley Hall, West Heath and Ann Marie Howes plus dental and learning-disability inpatient units in Birmingham. The line reflects amortisation of capitalised SystmOne / Rio configurations, Microsoft enterprise licensing, ERP platforms and any internally generated software meeting IAS 38 capitalisation criteria. The charge runs over typical 3-5 year useful lives for software per DHSC GAM ch.5 guidance.",
        "beneficiaries": "Serves a c. 1.15M Birmingham population through community nursing, district nursing, school nursing, health visiting, dental services, community paediatrics and learning-disability inpatient services; operates from Moseley Hall Hospital, West Heath Hospital, Ann Marie Howes (LD inpatient), Bromford and Loxton Court community units + c. 60+ clinic and base locations; c. 5,500 WTE staff.",
        "legal_basis": "IAS 38 Intangible Assets · DHSC Group Accounting Manual 2024-25 ch.5 · NHS Act 2006 · Health and Care Act 2022 · IFRS 16 (where intangibles relate to leased software)",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£0.56M"},
            {"label": "Specialty footprint", "value": "Birmingham community health — community nursing, district nursing, dental, LD inpatient, community paediatrics"},
            {"label": "Population served", "value": "c. 1.15M Birmingham residents"},
            {"label": "Estate", "value": "Moseley Hall, West Heath, Ann Marie Howes (LD inpatient), Bromford + c. 60+ clinics across Birmingham city + LDA/dental services"},
            {"label": "Workforce", "value": "c. 5,500 WTE — district nurses, health visitors, school nurses, AHPs, community paediatricians, dental, LD nurses"},
            {"label": "Intangible asset profile", "value": "EPR / SystmOne configuration costs · Microsoft enterprise licensing · ERP capitalised dev · clinical-pathway software"},
            {"label": "Useful life", "value": "Typically 3-5 years for software per DHSC GAM ch.5"},
            {"label": "Funding trajectory", "value": "Rising as capitalised digital investment under Frontline Digitisation programme rolls into amortisation profile"},
            {"label": "Delivery body", "value": "BCHC Finance + IT/Digital + capitalisation board · external software vendors (TPP SystmOne, Microsoft, ERP supplier)"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + NHSE Digital (Frontline Digitisation) + DHSC + Birmingham & Solihull ICB"},
            {"label": "Evaluation evidence", "value": "BCHC ARA (FY25); CQC inspection (RYW — Good); Frontline Digitisation tracker; NHSE Capital Guidance"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2010 PCT-era intangibles transferred at TCS · Successor: ongoing Frontline Digitisation capitalisation roll-in + IFRS 16-aligned cloud SaaS treatment"}
        ],
        "notes": "Amortisation is a small but rising line for community trusts as Frontline Digitisation funding from NHSE flows into capitalised software which then unwinds into the amortisation charge over 3-5 year useful lives. BCHC's c. £0.56M reflects its relatively modest digital-asset base — community trusts run a thinner clinical-system footprint than acute trusts, primarily SystmOne for community nursing rather than full hospital EPRs. Drivers include capitalised SystmOne configuration, Microsoft enterprise licensing renewal, and any internally generated clinical-pathway software meeting IAS 38 capitalisation. The Three Shifts policy direction (out-of-hospital, prevention, digital) is likely to lift this line via further digital-asset capitalisation in coming years.",
        "sources": [
            {"publisher": "Birmingham Community Healthcare NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.bhamcommunity.nhs.uk/about-us/corporate-information/annual-report/"},
            {"publisher": "Care Quality Commission", "title": "Birmingham Community Healthcare NHS Foundation Trust provider profile (RYW)", "url": "https://www.cqc.org.uk/provider/RYW"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (ch.5 on amortisation)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "IFRS Foundation", "title": "IAS 38 Intangible Assets", "url": "https://www.ifrs.org/issued-standards/list-of-standards/ias-38-intangible-assets/"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/connecting-health-and-care-providers/frontline-digitisation/"},
            {"publisher": "Lord Darzi / DHSC", "title": "Independent investigation of the NHS in England (Sep 2024) — Three Shifts", "url": "https://www.gov.uk/government/publications/independent-investigation-of-the-nhs-in-england"}
        ],
        "related": ["Birmingham Community Healthcare NHS Foundation Trust", "Premises & Infrastructure", "NHS Community Trusts", "Amortisation — Northamptonshire Healthcare NHS Foundation Trust", "Amortisation — Bridgewater Community Healthcare NHS Foundation Trust", "Frontline Digitisation"]
    },
    "Lease expenditure — Norfolk Community Health and Care NHS Trust": {
        "aliases": [{"name": "Lease expenditure", "parent": "Norfolk Community Health and Care NHS Trust"}],
        "description": "NCHC's £0.56M lease-expenditure line covers operating-lease and IFRS 16 right-of-use rentals across the trust's c. 50+ community sites in Norfolk including community hospitals at Benjamin Court (Cromer), Kelling Hospital (Holt), North Walsham, and Norwich Community Hospital, plus clinic and base estate scattered across the c. 2,000 sq miles of Norfolk. Most clinic premises are leased from NHS Property Services (NHSPS) under group leases, with some commercial leases for office and storage units. Vehicle-fleet leases for district-nursing pool cars are also captured here under IFRS 16.",
        "beneficiaries": "Serves a c. 920,000 Norfolk population (Greater Norwich + Norfolk coast + Breckland + N Norfolk + W Norfolk + S Norfolk); operates from c. 50+ sites including 4 community hospitals (Benjamin Court, Kelling, North Walsham, Norwich Community Hospital) + c. 45 clinics, base stations and admin units; c. 2,400 WTE staff including district nurses, AHPs, school nurses and health visitors.",
        "legal_basis": "IFRS 16 Leases · DHSC Group Accounting Manual 2024-25 ch.7 · Landlord and Tenant Act 1954 · NHS Act 2006 · Health and Care Act 2022 · NHSPS group-lease framework",
        "key_stats": [
            {"label": "Lease expenditure 2024-25", "value": "£0.56M"},
            {"label": "Specialty footprint", "value": "Norfolk community health — community hospitals, district nursing, AHPs, school nursing, health visiting"},
            {"label": "Population served", "value": "c. 920,000 Norfolk residents (large rural footprint c. 2,000 sq miles)"},
            {"label": "Estate", "value": "4 community hospitals (Benjamin Court Cromer, Kelling Holt, North Walsham, Norwich Community Hospital) + c. 45 clinics/bases"},
            {"label": "Workforce", "value": "c. 2,400 WTE — district nurses, AHPs, school nurses, health visitors, MSK community physio"},
            {"label": "Lease portfolio", "value": "Mostly NHSPS group leases on community-clinic estate + some commercial office leases + IFRS 16 right-of-use vehicle leases for district-nursing pool fleet"},
            {"label": "Lease type", "value": "Mostly short-term tenancies-at-will or 5-7yr Landlord & Tenant Act 1954 protected leases on NHSPS estate"},
            {"label": "IFRS 16 effect", "value": "From 2022-23 brought leases on-BS as right-of-use assets + lease liabilities; charge split between depreciation + interest unwind"},
            {"label": "Funding trajectory", "value": "Rising on IFRS 16 reclassification + NHSPS rent uplifts + growing district-nursing pool-fleet"},
            {"label": "Delivery body", "value": "NCHC Estates & Facilities + NHS Property Services + NHSE leasing framework"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + NHS Property Services + Norfolk & Waveney ICB"},
            {"label": "Evaluation evidence", "value": "NCHC ARA (FY25); CQC inspection (RY3 — Good); ERIC estates returns; NHSE community trust premises review"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2013 PCT/Community Health Partnerships estate transferred to NHSPS · Successor: continued estate rationalisation under Three Shifts + NHSPS lease modernisation programme"}
        ],
        "notes": "Community trusts have a distinctive lease-heavy estate footprint — NCHC operates from c. 50+ sites scattered across rural Norfolk, mostly leased from NHS Property Services on group-lease arrangements. The c. £0.56M reflects a mid-size community-trust lease bill, lifted by IFRS 16 application from 2022-23 which brought operating leases on-BS as right-of-use assets and split the charge between depreciation and interest unwind. Drivers include NHSPS rent uplifts (multi-year rent reviews), growing district-nursing pool-fleet under Three Shifts community-care direction, and ongoing rationalisation of legacy clinic sites. The trust's rural Norfolk footprint means relatively many small bases vs urban community trusts.",
        "sources": [
            {"publisher": "Norfolk Community Health and Care NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.norfolkcommunityhealthandcare.nhs.uk/about-us/corporate-information/annual-reports/"},
            {"publisher": "Care Quality Commission", "title": "Norfolk Community Health and Care NHS Trust provider profile (RY3)", "url": "https://www.cqc.org.uk/provider/RY3"},
            {"publisher": "IFRS Foundation", "title": "IFRS 16 Leases", "url": "https://www.ifrs.org/issued-standards/list-of-standards/ifrs-16-leases/"},
            {"publisher": "NHS Property Services", "title": "NHSPS — community estate group leases", "url": "https://www.property.nhs.uk/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 ch.7", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Lord Darzi / DHSC", "title": "Independent investigation of the NHS in England (Sep 2024)", "url": "https://www.gov.uk/government/publications/independent-investigation-of-the-nhs-in-england"}
        ],
        "related": ["Norfolk Community Health and Care NHS Trust", "Premises & Infrastructure", "NHS Community Trusts", "Lease expenditure — Lincolnshire Community Health Services NHS Trust", "Lease expenditure — Wirral Community Health and Care NHS Foundation Trust", "NHS Property Services"]
    },
    "Lease expenditure — Moorfields Eye Hospital NHS Foundation Trust": {
        "aliases": [{"name": "Lease expenditure", "parent": "Moorfields Eye Hospital NHS Foundation Trust"}],
        "description": "Moorfields' £0.55M lease-expenditure line covers operating-lease and IFRS 16 right-of-use rentals on the trust's network of c. 30+ outreach satellite eye-clinic sites across London and the South East — beyond the City Road main hospital — plus equipment leases for diagnostic imaging (OCT, fundus cameras, ultrasound A/B-scan) and pool-car fleet. Outreach sites include Moorfields at St George's, Bedford, Northwick Park, Croydon, Ealing, Mile End, Potters Bar, Stratford and (under the Oriel programme) the planned move from City Road to St Pancras with UCL Institute of Ophthalmology by c. 2027.",
        "beneficiaries": "Serves a c. 9M Greater London + South East referral catchment as the world's oldest specialist eye hospital; delivers c. 700,000 patient attendances/yr and c. 50,000 surgical procedures from c. 30+ sites (City Road HQ + outreach hubs across London, Bedfordshire, Hertfordshire, Surrey); c. 2,500 WTE staff including c. 350 ophthalmologists.",
        "legal_basis": "IFRS 16 Leases · DHSC Group Accounting Manual 2024-25 ch.7 · Landlord and Tenant Act 1954 · NHS Act 2006 · Health and Care Act 2022 · NHSPS / commercial-host lease frameworks",
        "key_stats": [
            {"label": "Lease expenditure 2024-25", "value": "£0.55M"},
            {"label": "Specialty footprint", "value": "World's oldest specialist eye hospital — ophthalmology, vitreoretinal, glaucoma, cornea, paediatrics, oculoplastics, neuro-ophth"},
            {"label": "Catchment", "value": "c. 9M Greater London + Home Counties referral catchment + national/international quaternary referrals"},
            {"label": "Annual activity", "value": "c. 700,000 attendances; c. 50,000 procedures; c. 12,000 cataract ops; major AMD anti-VEGF injection volume"},
            {"label": "Workforce", "value": "c. 2,500 WTE; c. 350 ophthalmologists; c. 100 optometrists"},
            {"label": "Estate", "value": "City Road HQ + c. 30+ outreach sites incl. St George's, Bedford, Northwick Park, Croydon, Ealing, Mile End, Potters Bar, Stratford"},
            {"label": "Lease portfolio", "value": "Outreach satellite clinics hosted at acute-trust sites + commercial premises + equipment leases (OCT, fundus, A/B-scan)"},
            {"label": "IFRS 16 effect", "value": "From 2022-23 brought operating leases on-BS as right-of-use assets; depreciation + interest unwind split"},
            {"label": "Funding trajectory", "value": "Rising on continued outreach hub-and-spoke expansion + Oriel campus relocation programme + IFRS 16 lease re-recognition"},
            {"label": "Delivery body", "value": "Moorfields Estates & Facilities + host acute-trust E&F (St George's, Croydon, etc.) + commercial landlords + NHSPS"},
            {"label": "Policy owner", "value": "NHSE Specialised Commissioning (ophth quaternary) + DHSC + NCL ICB + Oriel partnership (Moorfields + UCL + Moorfields Eye Charity)"},
            {"label": "Evaluation evidence", "value": "Moorfields ARA; CQC inspection (RP6 — Good/Outstanding domains); NHSE Specialised Commissioning ophth dashboard; Oriel project gateway reviews"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-IFRS-16 lease accounting + 1899 City Road site · Successor: Oriel St Pancras integrated eye-care + research campus c. 2027 (Moorfields + UCL IoO)"}
        ],
        "notes": "Moorfields runs a distinctive hub-and-spoke model with c. 30+ outreach sites across London and the South East as the world's oldest specialist eye hospital, meaning lease expenditure is structurally elevated relative to single-site specialist trusts. The c. £0.55M reflects a mix of outreach satellite-clinic rents (often hosted within acute-trust sites under sub-leases), commercial premises, and equipment leases for OCT and fundus-imaging diagnostic kit. IFRS 16 from 2022-23 lifted the BS treatment. The Oriel programme (planned c. 2027 move from City Road to St Pancras as an integrated eye-care + research campus with UCL Institute of Ophthalmology, funded jointly with Moorfields Eye Charity) will reshape the lease profile in coming years.",
        "sources": [
            {"publisher": "Moorfields Eye Hospital NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.moorfields.nhs.uk/content/annual-reports"},
            {"publisher": "Care Quality Commission", "title": "Moorfields Eye Hospital NHS Foundation Trust provider profile (RP6)", "url": "https://www.cqc.org.uk/provider/RP6"},
            {"publisher": "Oriel partnership", "title": "Oriel — Moorfields + UCL + Moorfields Eye Charity new eye-care and research campus", "url": "https://oriel-london.org.uk/"},
            {"publisher": "IFRS Foundation", "title": "IFRS 16 Leases", "url": "https://www.ifrs.org/issued-standards/list-of-standards/ifrs-16-leases/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 ch.7", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Specialised commissioning — ophthalmology service specifications", "url": "https://www.england.nhs.uk/commissioning/spec-services/"}
        ],
        "related": ["Moorfields Eye Hospital NHS Foundation Trust", "Premises & Infrastructure", "NHS Specialist Trusts", "Lease expenditure — Norfolk Community Health and Care NHS Trust", "Lease expenditure — Lincolnshire Community Health Services NHS Trust", "NHS Property Services"]
    },
    "Amortisation — Northamptonshire Healthcare NHS Foundation Trust": {
        "aliases": [{"name": "Amortisation", "parent": "Northamptonshire Healthcare NHS Foundation Trust"}],
        "description": "NHFT's £0.55M amortisation charge represents the systematic write-down of intangible assets — chiefly software licences, EPR/clinical-system development costs, and other capitalised intangibles — across the trust's combined community + mental-health footprint serving Northamptonshire. The trust is an integrated provider running community physical-health services + adult and child mental health + LD services from sites including Berrywood Hospital (Northampton, mental health), St Mary's Hospital (Kettering), Isebrook (Wellingborough), Rushden Hospital and c. 50+ community clinics. Amortisation runs over typical 3-5 year useful lives for software per DHSC GAM ch.5.",
        "beneficiaries": "Serves a c. 770,000 Northamptonshire population through integrated community + mental-health + LD services; operates from c. 50+ sites including Berrywood Hospital (mental health, Northampton), St Mary's (Kettering), Isebrook (Wellingborough), Rushden Hospital + c. 45 community clinics; c. 4,300 WTE staff including community + mental-health nurses, AHPs, psychiatrists.",
        "legal_basis": "IAS 38 Intangible Assets · DHSC Group Accounting Manual 2024-25 ch.5 · NHS Act 2006 · Health and Care Act 2022 · IFRS 16 (where intangibles relate to leased software)",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£0.55M"},
            {"label": "Specialty footprint", "value": "Integrated community + mental health + LD provider for Northamptonshire"},
            {"label": "Population served", "value": "c. 770,000 Northamptonshire residents (North Northants + West Northants)"},
            {"label": "Estate", "value": "Berrywood Hospital (Northampton MH), St Mary's (Kettering), Isebrook (Wellingborough), Rushden Hospital + c. 45 community clinics"},
            {"label": "Workforce", "value": "c. 4,300 WTE — community nurses, mental-health nurses, AHPs, psychiatrists, LD nurses"},
            {"label": "Intangible asset profile", "value": "EPR (RiO mental-health) + SystmOne community + Microsoft licensing + capitalised digital projects under Frontline Digitisation"},
            {"label": "Useful life", "value": "Typically 3-5 years for software; longer for some bespoke clinical systems"},
            {"label": "Funding trajectory", "value": "Rising as Frontline Digitisation capitalised assets unwind into amortisation profile + EPR upgrades capitalised"},
            {"label": "Delivery body", "value": "NHFT Finance + Digital/IT + capitalisation board · external vendors (Servelec/CSA RiO MH, TPP SystmOne, Microsoft)"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + NHSE Digital (Frontline Digitisation) + DHSC + Northamptonshire ICB"},
            {"label": "Evaluation evidence", "value": "NHFT ARA (FY25); CQC inspection (RP1 — Good); Frontline Digitisation tracker"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2017 merger of Northamptonshire community + mental-health into integrated provider · Successor: ongoing Frontline Digitisation capitalisation roll-in + EPR convergence"}
        ],
        "notes": "Amortisation is a small but rising line for combined community + mental-health trusts as Frontline Digitisation funding flows into capitalised software. NHFT runs both RiO (mental health EPR) and SystmOne (community) which means a more complex digital-asset base than pure community trusts, lifting the amortisation profile. Drivers include capitalised EPR configurations, Microsoft enterprise renewal, and bespoke clinical-pathway software meeting IAS 38 capitalisation. The 2017 merger of Northamptonshire community and mental-health services into a single integrated provider created the current footprint, and the Three Shifts policy direction (community + prevention + digital) is likely to keep this line on a rising trajectory.",
        "sources": [
            {"publisher": "Northamptonshire Healthcare NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.nhft.nhs.uk/about-us/key-documents/annual-report-and-accounts"},
            {"publisher": "Care Quality Commission", "title": "Northamptonshire Healthcare NHS Foundation Trust provider profile (RP1)", "url": "https://www.cqc.org.uk/provider/RP1"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (ch.5 amortisation)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "IFRS Foundation", "title": "IAS 38 Intangible Assets", "url": "https://www.ifrs.org/issued-standards/list-of-standards/ias-38-intangible-assets/"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/connecting-health-and-care-providers/frontline-digitisation/"},
            {"publisher": "Lord Darzi / DHSC", "title": "Independent investigation of the NHS in England (Sep 2024)", "url": "https://www.gov.uk/government/publications/independent-investigation-of-the-nhs-in-england"}
        ],
        "related": ["Northamptonshire Healthcare NHS Foundation Trust", "Premises & Infrastructure", "NHS Community Trusts", "Amortisation — Birmingham Community Healthcare NHS Foundation Trust", "Amortisation — Bridgewater Community Healthcare NHS Foundation Trust", "Frontline Digitisation"]
    },
    "Amortisation — South Central Ambulance Service NHS Foundation Trust": {
        "aliases": [{"name": "Amortisation", "parent": "South Central Ambulance Service NHS Foundation Trust"}],
        "description": "SCAS's £0.53M amortisation charge represents the systematic write-down of intangible assets — primarily Computer-Aided Despatch (CAD) software (Cleric / IBIS), capitalised 999/111 telephony platforms, EPR/Patient Clinical Records system development, capitalised software for Make Ready Centre logistics, and Microsoft enterprise licensing — across the trust's footprint covering Berkshire, Buckinghamshire, Hampshire and Oxfordshire. The charge runs over typical 3-5 year useful lives for software per DHSC GAM ch.5; longer asset lives apply to bespoke clinical-systems integration work.",
        "beneficiaries": "Serves a c. 4M South Central population across c. 3,554 sq miles (Berkshire, Buckinghamshire, Hampshire, Oxfordshire); responds to c. 740,000 999 incidents + delivers c. 4M+ NHS 111 contacts/yr (largest 111-IUC contract holder among ambulance trusts); c. 4,200 WTE staff including paramedics, ECAs, technicians, NHS 111 health advisors and clinical advisors.",
        "legal_basis": "IAS 38 Intangible Assets · DHSC Group Accounting Manual 2024-25 ch.5 · NHS Act 2006 · Health and Care Act 2022 · IFRS 16 (where intangibles relate to leased software)",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£0.53M"},
            {"label": "Specialty footprint", "value": "Regional 999 + 111 ambulance + non-emergency PTS — Berkshire, Bucks, Hampshire, Oxfordshire (4 counties · 3,554 sq miles)"},
            {"label": "Population served", "value": "c. 4M South Central residents"},
            {"label": "Annual activity", "value": "c. 740,000 999 incidents; c. 4M+ NHS 111 contacts (multi-region 111 contract)"},
            {"label": "Workforce", "value": "c. 4,200 WTE; paramedics + ECAs + technicians + 111 health/clinical advisors"},
            {"label": "Intangible asset profile", "value": "CAD software (Cleric/IBIS dispatch) + 111 telephony + EPR/PCR · capitalised Microsoft licensing · MRC logistics software"},
            {"label": "111 contract scale", "value": "Holds NHS 111-IUC contracts across multiple regions including SE — drives larger telephony + clinical-decision-support intangible base than peer ambulance trusts"},
            {"label": "Useful life", "value": "Typically 3-5 years for software; some bespoke CAD integration capitalised over longer life"},
            {"label": "Funding trajectory", "value": "Rising on NHSE 111-IUC retender capitalisation + Frontline Digitisation + capitalised CAD upgrades"},
            {"label": "Delivery body", "value": "SCAS Finance + Digital/IT + CAD vendor (Cleric/IBIS) · Microsoft + 111 telephony partner"},
            {"label": "Policy owner", "value": "NHSE Urgent and Emergency Care + NHSE Digital + DHSC + 4 South Central ICBs"},
            {"label": "Evaluation evidence", "value": "SCAS ARA; CQC inspection (RYE); ORH benchmarks; AACE national activity; NHSE 111-IUC dashboards"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2006 county-level ambulance services + 111-IUC contract roll-up · Successor: ongoing CAD upgrade + 111 retender + ARP demand growth + Net Zero fleet electrification"}
        ],
        "notes": "Among the 10 English regional ambulance services SCAS has the most digitally complex intangible footprint because it runs a very large NHS 111-IUC operation (largest 111 contract holder among ambulance trusts), which drives capitalised telephony platforms and clinical-decision-support software in addition to the standard CAD dispatch software all trusts run. The c. £0.53M reflects amortisation of these capitalised assets over 3-5 year useful lives. Recent context includes the 2023-24 industrial action (paramedic strikes), ongoing 111-IUC contract retender pressures, and capitalised Frontline Digitisation investment. Tunnel-vision risk is the SE 111 contract loss in 2022-23 to IC24 which reshaped the asset base.",
        "sources": [
            {"publisher": "South Central Ambulance Service NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.scas.nhs.uk/about-us/our-publications/annual-reports/"},
            {"publisher": "Care Quality Commission", "title": "South Central Ambulance Service NHS Foundation Trust provider profile (RYE)", "url": "https://www.cqc.org.uk/provider/RYE"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (ch.5 amortisation)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "IFRS Foundation", "title": "IAS 38 Intangible Assets", "url": "https://www.ifrs.org/issued-standards/list-of-standards/ias-38-intangible-assets/"},
            {"publisher": "NHS England", "title": "Integrated Urgent Care (NHS 111) service specification", "url": "https://www.england.nhs.uk/urgent-emergency-care/"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/connecting-health-and-care-providers/frontline-digitisation/"}
        ],
        "related": ["South Central Ambulance Service NHS Foundation Trust", "Premises & Infrastructure", "NHS Ambulance Trusts", "Amortisation — West Midlands Ambulance Service University NHS Foundation Trust", "Amortisation — London Ambulance Service NHS Trust", "NHS England"]
    },
    "Amortisation — Derbyshire Community Health Services NHS Foundation Trust": {
        "aliases": [{"name": "Amortisation", "parent": "Derbyshire Community Health Services NHS Foundation Trust"}],
        "description": "DCHS's £0.52M amortisation charge represents the systematic write-down of capitalised intangible assets — primarily SystmOne community-EPR configuration costs, capitalised digital projects under NHSE Frontline Digitisation, Microsoft enterprise licensing and ERP / payroll software — across the trust's c. 30+ community-hospital and clinic estate spread between Derby city and the wider Derbyshire footprint, including community hospitals at Ilkeston, Ripley, Ashbourne, Bolsover, Heanor, Buxton and Whitworth. The charge runs over 3-5 year useful lives per DHSC GAM ch.5 guidance.",
        "beneficiaries": "Serves a c. 1.05M Derbyshire population (Derby City + Derbyshire County); operates from c. 30+ sites including community hospitals at Ilkeston, Ripley, Ashbourne, Bolsover, Heanor, Buxton and Whitworth, plus c. 100 clinic and base-station locations; c. 4,400 WTE staff including district nurses, AHPs, school nurses and health visitors covering urban Derby + rural Peak District.",
        "legal_basis": "IAS 38 Intangible Assets · DHSC Group Accounting Manual 2024-25 ch.5 · NHS Act 2006 · Health and Care Act 2022 · IFRS 16 (where intangibles relate to leased software)",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£0.52M"},
            {"label": "Specialty footprint", "value": "Derbyshire community health — community hospitals + district nursing + school nursing + AHPs + MSK community physio"},
            {"label": "Population served", "value": "c. 1.05M Derbyshire residents"},
            {"label": "Estate", "value": "c. 30+ sites incl. community hospitals at Ilkeston, Ripley, Ashbourne, Bolsover, Heanor, Buxton, Whitworth + c. 100 clinic/base locations"},
            {"label": "Workforce", "value": "c. 4,400 WTE — district nurses, AHPs, school nurses, health visitors, MSK community physio"},
            {"label": "Intangible asset profile", "value": "SystmOne community-EPR config · Frontline Digitisation capitalised projects · Microsoft enterprise licensing · ERP / payroll software"},
            {"label": "Useful life", "value": "Typically 3-5 years for software per DHSC GAM ch.5"},
            {"label": "Funding trajectory", "value": "Rising as Frontline Digitisation capitalised investment unwinds into amortisation profile + EPR upgrades"},
            {"label": "Delivery body", "value": "DCHS Finance + Digital/IT + capitalisation board · TPP SystmOne + Microsoft + ERP supplier"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + NHSE Digital (Frontline Digitisation) + DHSC + Derby & Derbyshire ICB"},
            {"label": "Evaluation evidence", "value": "DCHS ARA (FY25); CQC inspection (RY8 — Outstanding); Frontline Digitisation tracker"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2011 PCT-era intangibles transferred at TCS · Successor: ongoing Frontline Digitisation roll-in + Three Shifts community-care digital expansion"}
        ],
        "notes": "Amortisation is a small but rising line for community trusts as Frontline Digitisation funding from NHSE flows into capitalised software which then unwinds over 3-5 year useful lives. DCHS is one of only two community trusts rated CQC Outstanding (alongside Bridgewater historically), and its digital posture is correspondingly mature, lifting the intangible-asset base above the community-trust median. Drivers include capitalised SystmOne configuration, Microsoft enterprise renewal, and bespoke clinical-pathway software meeting IAS 38 capitalisation. The Three Shifts policy direction (out-of-hospital, digital, prevention) is likely to further lift this line via additional digital capitalisation in coming years.",
        "sources": [
            {"publisher": "Derbyshire Community Health Services NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.dchs.nhs.uk/about-us/corporate-information/our-publications/annual-reports"},
            {"publisher": "Care Quality Commission", "title": "Derbyshire Community Health Services NHS Foundation Trust provider profile (RY8 — Outstanding)", "url": "https://www.cqc.org.uk/provider/RY8"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (ch.5 amortisation)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "IFRS Foundation", "title": "IAS 38 Intangible Assets", "url": "https://www.ifrs.org/issued-standards/list-of-standards/ias-38-intangible-assets/"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/connecting-health-and-care-providers/frontline-digitisation/"},
            {"publisher": "Lord Darzi / DHSC", "title": "Independent investigation of the NHS in England (Sep 2024)", "url": "https://www.gov.uk/government/publications/independent-investigation-of-the-nhs-in-england"}
        ],
        "related": ["Derbyshire Community Health Services NHS Foundation Trust", "Premises & Infrastructure", "NHS Community Trusts", "Amortisation — Birmingham Community Healthcare NHS Foundation Trust", "Amortisation — Northamptonshire Healthcare NHS Foundation Trust", "Frontline Digitisation"]
    },
    "Business rates — Hounslow and Richmond Community Healthcare NHS Trust": {
        "aliases": [{"name": "Business rates", "parent": "Hounslow and Richmond Community Healthcare NHS Trust"}],
        "description": "HRCH's £0.52M non-domestic-rates bill covers business rates payable on the trust's portfolio of community sites in West London — including the Heart of Hounslow Centre for Health, Teddington Memorial Hospital, Whitton Corner, Heart of Hounslow on Bath Road, Twickenham Health Centre and a long tail of clinic, school-nursing base and district-nursing hub locations across the London Boroughs of Hounslow and Richmond upon Thames. NDR is paid to LB Hounslow and LB Richmond billing authorities under the Local Government Finance Act 1988, with rateable values from the VOA 2023 rating list driving the multiplier-based liability.",
        "beneficiaries": "Serves a c. 480,000 combined population across LB Hounslow (c. 290k) + LB Richmond upon Thames (c. 195k); operates from c. 25+ sites including Heart of Hounslow Centre for Health, Teddington Memorial Hospital, Whitton Corner + Twickenham Health Centre + community clinics; c. 1,500 WTE staff including district nurses, school nurses, health visitors, AHPs and MSK community physio.",
        "legal_basis": "Local Government Finance Act 1988 (Sch 6 — non-domestic rating) · Non-Domestic Rating Act 2023 · Non-Domestic Rating (Multipliers and Private Finance) Act 2024 · Valuation Office Agency 2023 rating list · DHSC Group Accounting Manual 2024-25",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£0.52M"},
            {"label": "Specialty footprint", "value": "West London community health — community nursing, district nursing, school nursing, health visiting, MSK, dental, end-of-life community"},
            {"label": "Population served", "value": "c. 480,000 (LB Hounslow c. 290k + LB Richmond c. 195k)"},
            {"label": "Estate", "value": "Heart of Hounslow Centre for Health, Teddington Memorial Hospital, Whitton Corner, Twickenham Health Centre + c. 20+ clinic/base locations"},
            {"label": "Workforce", "value": "c. 1,500 WTE — district nurses, school nurses, health visitors, AHPs, MSK"},
            {"label": "Billing authorities", "value": "LB Hounslow + LB Richmond upon Thames (West London — both Conservative-led councils as of 2024 elections)"},
            {"label": "VOA list cycle", "value": "2023 rating list (3-year cycle from 2026 revaluation under Non-Domestic Rating Act 2023)"},
            {"label": "NDR multiplier 2024-25", "value": "Standard 54.6p; small-business 49.9p; healthcare estate generally on standard multiplier (no NHS exemption)"},
            {"label": "Funding trajectory", "value": "Rising c. 3-5%/yr in line with multiplier uprating + 2023 VOA revaluation effects on West London RVs"},
            {"label": "Delivery body", "value": "HRCH Estates & Facilities + NHSPS for leased sites + LB Hounslow + LB Richmond billing authorities + VOA"},
            {"label": "Policy owner", "value": "MHCLG (was DLUHC) + HM Treasury + DHSC + NHSE + NW London ICB / SW London ICB"},
            {"label": "Evaluation evidence", "value": "HRCH ARA (FY25); CQC inspection (RY9 — Good); ERIC estates returns"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2011 PCT-era estate · Successor: 2026 VOA revaluation under 3-year cycle + NW/SW London ICB community estate review"}
        ],
        "notes": "Community trusts pay full non-domestic rates on their estates with no NHS exemption — unlike charities, NHS bodies do not receive the 80% mandatory relief, so the line tracks closely with the size and rateable value of the owned/leased footprint. HRCH's c. £0.52M reflects a mid-size West London community-trust estate exposed to Greater London RV inflation under the VOA 2023 rating list. Drivers include the 2023 revaluation lifting RVs on health-centre estate, annual multiplier uprating, and the new supplementary multiplier introduced by the Non-Domestic Rating (Multipliers and Private Finance) Act 2024. The 2026 revaluation cycle (next under the new 3-yearly system) is the next reset point.",
        "sources": [
            {"publisher": "Hounslow and Richmond Community Healthcare NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.hrch.nhs.uk/about-us/corporate-information/annual-report/"},
            {"publisher": "Care Quality Commission", "title": "Hounslow and Richmond Community Healthcare NHS Trust provider profile (RY9)", "url": "https://www.cqc.org.uk/provider/RY9"},
            {"publisher": "Valuation Office Agency", "title": "Find a business rates valuation (2023 rating list)", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "UK Government", "title": "Non-Domestic Rating Act 2023", "url": "https://www.legislation.gov.uk/ukpga/2023/53"},
            {"publisher": "UK Government", "title": "Non-Domestic Rating (Multipliers and Private Finance) Act 2024", "url": "https://www.legislation.gov.uk/ukpga/2024/26"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"}
        ],
        "related": ["Hounslow and Richmond Community Healthcare NHS Trust", "Premises & Infrastructure", "NHS Community Trusts", "Business rates — Liverpool Women's NHS Foundation Trust", "Business rates — Liverpool Heart and Chest Hospital NHS Foundation Trust", "Valuation Office Agency"]
    },
    "Amortisation — Bridgewater Community Healthcare NHS Foundation Trust": {
        "aliases": [{"name": "Amortisation", "parent": "Bridgewater Community Healthcare NHS Foundation Trust"}],
        "description": "Bridgewater's £0.50M amortisation charge represents the systematic write-down of intangible assets — chiefly SystmOne community-EPR configuration costs, capitalised digital projects under NHSE Frontline Digitisation, Microsoft enterprise licensing and ERP/payroll software — across the trust's footprint covering Halton, Warrington, St Helens and Wigan. Bridgewater is one of England's largest community-only providers and runs a complex multi-borough digital estate with capitalised software unwinding over typical 3-5 year useful lives per DHSC GAM ch.5.",
        "beneficiaries": "Serves a c. 1.05M population across the four NW boroughs of Halton, Warrington, St Helens and Wigan; operates from c. 90+ community sites including Halton Hospital community wing, Newton Community Hospital, Padgate House (Warrington), Leigh Health Centre + c. 80 clinics; c. 3,200 WTE staff including district nurses, AHPs, school nurses, health visitors and dental services.",
        "legal_basis": "IAS 38 Intangible Assets · DHSC Group Accounting Manual 2024-25 ch.5 · NHS Act 2006 · Health and Care Act 2022 · IFRS 16 (where intangibles relate to leased software)",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£0.50M"},
            {"label": "Specialty footprint", "value": "NW community health across Halton, Warrington, St Helens, Wigan — district nursing, AHPs, school nursing, dental, MSK"},
            {"label": "Population served", "value": "c. 1.05M across 4 NW boroughs"},
            {"label": "Estate", "value": "c. 90+ sites incl. Halton community wing, Newton CH, Padgate House (Warrington), Leigh Health Centre + c. 80 clinics/bases"},
            {"label": "Workforce", "value": "c. 3,200 WTE — district nurses, AHPs, school nurses, health visitors, dental, MSK"},
            {"label": "Intangible asset profile", "value": "SystmOne community-EPR config · Frontline Digitisation capitalised projects · Microsoft licensing · ERP/payroll software"},
            {"label": "Useful life", "value": "Typically 3-5 years for software per DHSC GAM ch.5"},
            {"label": "Funding trajectory", "value": "Rising as Frontline Digitisation capitalised investment unwinds + EPR upgrades capitalised"},
            {"label": "Delivery body", "value": "Bridgewater Finance + Digital/IT + capitalisation board · TPP SystmOne + Microsoft + ERP supplier"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + NHSE Digital (Frontline Digitisation) + DHSC + Cheshire & Merseyside ICB + GM ICB"},
            {"label": "Evaluation evidence", "value": "Bridgewater ARA (FY25); CQC inspection (RY2 — Good); Frontline Digitisation tracker"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2011 PCT-era intangibles transferred at TCS · Successor: ongoing Frontline Digitisation capitalisation roll-in + Three Shifts community-care digital expansion"}
        ],
        "notes": "Bridgewater operates across a four-borough NW England footprint that straddles two ICBs (Cheshire & Merseyside for Halton/Warrington/St Helens; Greater Manchester for Wigan) creating a relatively complex digital and intangible-asset profile. The c. £0.50M amortisation reflects capitalised SystmOne configuration, Microsoft enterprise renewal, and Frontline Digitisation projects unwinding over 3-5 year lives. The trust has had recent commissioning churn — service-line transfers (e.g. Trafford services moving in 2018, dental service contract changes) reshape the intangible-asset base. The Three Shifts policy direction (community + prevention + digital) is likely to keep this line on a rising trajectory.",
        "sources": [
            {"publisher": "Bridgewater Community Healthcare NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.bridgewater.nhs.uk/about-us/corporate-information/annual-report/"},
            {"publisher": "Care Quality Commission", "title": "Bridgewater Community Healthcare NHS Foundation Trust provider profile (RY2)", "url": "https://www.cqc.org.uk/provider/RY2"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (ch.5 amortisation)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "IFRS Foundation", "title": "IAS 38 Intangible Assets", "url": "https://www.ifrs.org/issued-standards/list-of-standards/ias-38-intangible-assets/"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/connecting-health-and-care-providers/frontline-digitisation/"},
            {"publisher": "Lord Darzi / DHSC", "title": "Independent investigation of the NHS in England (Sep 2024)", "url": "https://www.gov.uk/government/publications/independent-investigation-of-the-nhs-in-england"}
        ],
        "related": ["Bridgewater Community Healthcare NHS Foundation Trust", "Premises & Infrastructure", "NHS Community Trusts", "Amortisation — Birmingham Community Healthcare NHS Foundation Trust", "Amortisation — Derbyshire Community Health Services NHS Foundation Trust", "Frontline Digitisation"]
    },
    "Lease expenditure — Lincolnshire Community Health Services NHS Trust": {
        "aliases": [{"name": "Lease expenditure", "parent": "Lincolnshire Community Health Services NHS Trust"}],
        "description": "LCHS's £0.47M lease-expenditure line covers operating-lease and IFRS 16 right-of-use rentals across the trust's c. 50+ community sites in Lincolnshire — one of the largest, most rural counties in England — including community hospitals at Skegness, Gainsborough, Louth and Spalding (John Coupland Hospital), plus health centres in Boston, Sleaford, Stamford, Grantham community estate and a long tail of clinics and base stations across c. 2,300 sq miles. Most clinic premises are leased from NHS Property Services (NHSPS) under group leases. Vehicle-fleet leases for district-nursing pool cars are also captured here under IFRS 16.",
        "beneficiaries": "Serves a c. 770,000 Lincolnshire population across c. 2,300 sq miles (England's 2nd-largest county by area); operates from c. 50+ sites including community hospitals at Skegness, Gainsborough, Louth, John Coupland (Gainsborough), County Hospital Louth + clinics in Boston, Sleaford, Stamford and rural Lincolnshire; c. 2,400 WTE staff including district nurses, AHPs, school nurses and health visitors.",
        "legal_basis": "IFRS 16 Leases · DHSC Group Accounting Manual 2024-25 ch.7 · Landlord and Tenant Act 1954 · NHS Act 2006 · Health and Care Act 2022 · NHSPS group-lease framework",
        "key_stats": [
            {"label": "Lease expenditure 2024-25", "value": "£466,608"},
            {"label": "Specialty footprint", "value": "Lincolnshire community health — community hospitals, district nursing, AHPs, school nursing, health visiting"},
            {"label": "Population served", "value": "c. 770,000 Lincolnshire residents (England's 2nd-largest county by area c. 2,300 sq miles)"},
            {"label": "Estate", "value": "Community hospitals at Skegness, Gainsborough, Louth, John Coupland + clinics in Boston, Sleaford, Stamford + base stations"},
            {"label": "Workforce", "value": "c. 2,400 WTE — district nurses, AHPs, school nurses, health visitors, MSK community physio"},
            {"label": "Lease portfolio", "value": "Mostly NHSPS group leases on community-clinic estate + some commercial office leases + IFRS 16 right-of-use vehicle leases for district-nursing pool fleet"},
            {"label": "Lease type", "value": "Mostly short-term tenancies-at-will or 5-7yr Landlord & Tenant Act 1954 protected leases on NHSPS estate"},
            {"label": "IFRS 16 effect", "value": "From 2022-23 brought leases on-BS as right-of-use assets + lease liabilities; charge split between depreciation + interest unwind"},
            {"label": "Funding trajectory", "value": "Rising on IFRS 16 reclassification + NHSPS rent uplifts + growing district-nursing pool-fleet under rural-Lincolnshire workforce model"},
            {"label": "Delivery body", "value": "LCHS Estates & Facilities + NHS Property Services + NHSE leasing framework"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + NHS Property Services + Lincolnshire ICB"},
            {"label": "Evaluation evidence", "value": "LCHS ARA (FY25); CQC inspection (RY5 — Good); ERIC estates returns; NHSE community trust premises review"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2013 PCT/CHP estate transferred to NHSPS · Successor: continued estate rationalisation under Three Shifts + NHSPS lease modernisation programme"}
        ],
        "notes": "LCHS runs one of the most geographically dispersed community estates in England — Lincolnshire is the country's second-largest county by area at c. 2,300 sq miles, with community hospitals dotted across the coast (Skegness, Louth), the fens (Boston, Spalding), the Wolds and the Trent valley (Gainsborough). The c. £0.47M lease bill reflects this rural-spread footprint, with most premises leased from NHSPS under group-lease arrangements and lifted by IFRS 16 application from 2022-23. Drivers include NHSPS rent uplifts (multi-year reviews), growing district-nursing pool-fleet to cover the rural footprint, and ongoing rationalisation of legacy clinic sites. The Three Shifts community-care policy direction is likely to drive estate expansion in coming years.",
        "sources": [
            {"publisher": "Lincolnshire Community Health Services NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.lincolnshirecommunityhealthservices.nhs.uk/about-us/corporate-information/annual-reports/"},
            {"publisher": "Care Quality Commission", "title": "Lincolnshire Community Health Services NHS Trust provider profile (RY5)", "url": "https://www.cqc.org.uk/provider/RY5"},
            {"publisher": "IFRS Foundation", "title": "IFRS 16 Leases", "url": "https://www.ifrs.org/issued-standards/list-of-standards/ifrs-16-leases/"},
            {"publisher": "NHS Property Services", "title": "NHSPS — community estate group leases", "url": "https://www.property.nhs.uk/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 ch.7", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Lord Darzi / DHSC", "title": "Independent investigation of the NHS in England (Sep 2024)", "url": "https://www.gov.uk/government/publications/independent-investigation-of-the-nhs-in-england"}
        ],
        "related": ["Lincolnshire Community Health Services NHS Trust", "Premises & Infrastructure", "NHS Community Trusts", "Lease expenditure — Norfolk Community Health and Care NHS Trust", "Lease expenditure — Wirral Community Health and Care NHS Foundation Trust", "NHS Property Services"]
    },
    "Business rates — Liverpool Women's NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "Liverpool Women's NHS Foundation Trust"}],
        "description": "Liverpool Women's £0.47M non-domestic-rates bill covers business rates payable on the trust's estate centred on the Crown Street main hospital site in Toxteth, Liverpool — one of only two NHS specialist women's hospitals in the UK (alongside Birmingham Women's & Children's) — plus outreach community midwifery and gynaecology clinic sites. NDR is paid to Liverpool City Council under the Local Government Finance Act 1988, with rateable values from the Valuation Office Agency 2023 rating list driving the multiplier-based liability. The trust has been the subject of long-running estate-strategy debate over the future location of women's services in Liverpool.",
        "beneficiaries": "Serves a c. 2.4M Cheshire & Merseyside catchment plus regional fetal medicine and reproductive medicine referrals across the North West and beyond; delivers c. 8,000 births/yr (one of the busiest single-site UK maternity units), c. 50,000 outpatient attendances + neonatal-IC tertiary care; c. 1,500 WTE staff at the Crown Street main site.",
        "legal_basis": "Local Government Finance Act 1988 (Sch 6 — non-domestic rating) · Non-Domestic Rating Act 2023 · Non-Domestic Rating (Multipliers and Private Finance) Act 2024 · Valuation Office Agency 2023 rating list · DHSC Group Accounting Manual 2024-25",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£0.47M"},
            {"label": "Specialty footprint", "value": "One of two NHS specialist women's hospitals in the UK — maternity, gynaecology, fetal medicine, reproductive medicine, neonatal-IC tertiary"},
            {"label": "Catchment", "value": "c. 2.4M Cheshire & Merseyside + regional NW fetal medicine/reproductive medicine quaternary referrals"},
            {"label": "Annual activity", "value": "c. 8,000 births/yr; c. 50,000 outpatient attendances; tertiary neonatal-IC; major IVF/reproductive medicine programme (Hewitt Centre)"},
            {"label": "Workforce", "value": "c. 1,500 WTE at Crown Street main site"},
            {"label": "Estate", "value": "Crown Street main hospital (Toxteth, Liverpool, c. 1995) + community midwifery clinics + Hewitt Fertility Centre"},
            {"label": "Billing authority", "value": "Liverpool City Council"},
            {"label": "VOA list cycle", "value": "2023 rating list (3-year cycle from 2026 revaluation under Non-Domestic Rating Act 2023)"},
            {"label": "NDR multiplier 2024-25", "value": "Standard 54.6p; small-business 49.9p; healthcare estate generally on standard multiplier (no NHS exemption)"},
            {"label": "Funding trajectory", "value": "Rising c. 3-5%/yr in line with multiplier uprating + 2023 VOA revaluation effects"},
            {"label": "Delivery body", "value": "LWH Estates & Facilities + Liverpool City Council billing authority + VOA"},
            {"label": "Policy owner", "value": "MHCLG + HM Treasury + DHSC + NHSE Specialised Commissioning (fetal medicine + reproductive medicine) + Cheshire & Merseyside ICB"},
            {"label": "Evaluation evidence", "value": "LWH ARA; CQC inspection (REP — Requires Improvement following 2018 maternity findings, then Good); Ockenden / national maternity reviews"},
            {"label": "Predecessor / successor", "value": "Predecessor: 1995 Crown Street site opened consolidating Mill Road / Oxford St maternity hospitals · Successor: long-running estate strategy debate over future co-location with new Royal Liverpool / Aintree (no decision agreed as of 2024)"}
        ],
        "notes": "Liverpool Women's pays full non-domestic rates on its Crown Street single-site estate with no NHS exemption — unlike charities, NHS bodies do not receive the 80% mandatory relief. The trust has been at the centre of a long-running and politically charged estate-strategy debate over whether women's services in Liverpool should remain on the Crown Street site (which lacks adult HDU/ICU on-site, requiring blue-light transfers) or be co-located with a major Liverpool acute trust. As of 2024 no agreed solution. Drivers for the c. £0.47M NDR include the 2023 revaluation effects, annual multiplier uprating and the new supplementary multiplier under the Non-Domestic Rating (Multipliers and Private Finance) Act 2024.",
        "sources": [
            {"publisher": "Liverpool Women's NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.liverpoolwomens.nhs.uk/about-us/corporate-information/annual-report-and-accounts/"},
            {"publisher": "Care Quality Commission", "title": "Liverpool Women's NHS Foundation Trust provider profile (REP)", "url": "https://www.cqc.org.uk/provider/REP"},
            {"publisher": "Valuation Office Agency", "title": "Find a business rates valuation (2023 rating list)", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "UK Government", "title": "Non-Domestic Rating Act 2023", "url": "https://www.legislation.gov.uk/ukpga/2023/53"},
            {"publisher": "UK Government", "title": "Non-Domestic Rating (Multipliers and Private Finance) Act 2024", "url": "https://www.legislation.gov.uk/ukpga/2024/26"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"}
        ],
        "related": ["Liverpool Women's NHS Foundation Trust", "Premises & Infrastructure", "NHS Specialist Trusts", "Business rates — Liverpool Heart and Chest Hospital NHS Foundation Trust", "Business rates — Hounslow and Richmond Community Healthcare NHS Trust", "Valuation Office Agency"]
    },
    "Lease expenditure — Wirral Community Health and Care NHS Foundation Trust": {
        "aliases": [{"name": "Lease expenditure", "parent": "Wirral Community Health and Care NHS Foundation Trust"}],
        "description": "WCHC's £0.46M lease-expenditure line covers operating-lease and IFRS 16 right-of-use rentals across the trust's c. 30+ community sites in Wirral and (since 2020) Cheshire East, including St Catherine's Health Centre (Birkenhead), Victoria Central Health Centre (Wallasey), Eastham Clinic, Heswall Clinic and a long tail of community-nursing base stations. Most clinic premises are leased from NHS Property Services (NHSPS) under group leases. Vehicle-fleet leases for district-nursing pool cars are also captured here under IFRS 16. WCHC took on Cheshire East 0-19 services in 2020 expanding the lease footprint.",
        "beneficiaries": "Serves a c. 320,000 Wirral population + c. 380,000 Cheshire East 0-19 population (since 2020) — combined c. 700,000; operates from c. 30+ sites including St Catherine's Health Centre (Birkenhead), Victoria Central (Wallasey), Eastham Clinic + community-nursing bases; c. 1,300 WTE staff including district nurses, school nurses, health visitors, AHPs and MSK community physio.",
        "legal_basis": "IFRS 16 Leases · DHSC Group Accounting Manual 2024-25 ch.7 · Landlord and Tenant Act 1954 · NHS Act 2006 · Health and Care Act 2022 · NHSPS group-lease framework",
        "key_stats": [
            {"label": "Lease expenditure 2024-25", "value": "£463,536"},
            {"label": "Specialty footprint", "value": "Wirral + Cheshire East community health — district nursing, school nursing, health visiting, MSK, dental"},
            {"label": "Population served", "value": "c. 320k Wirral + c. 380k Cheshire East 0-19 (combined c. 700k)"},
            {"label": "Estate", "value": "St Catherine's Health Centre (Birkenhead), Victoria Central (Wallasey), Eastham Clinic, Heswall Clinic + base stations"},
            {"label": "Workforce", "value": "c. 1,300 WTE — district nurses, school nurses, health visitors, AHPs, MSK"},
            {"label": "Lease portfolio", "value": "Mostly NHSPS group leases on community-clinic estate + some commercial office leases + IFRS 16 right-of-use vehicle leases for district-nursing pool fleet"},
            {"label": "Lease type", "value": "Mostly short-term tenancies-at-will or 5-7yr Landlord & Tenant Act 1954 protected leases on NHSPS estate"},
            {"label": "IFRS 16 effect", "value": "From 2022-23 brought leases on-BS as right-of-use assets + lease liabilities; charge split between depreciation + interest unwind"},
            {"label": "Funding trajectory", "value": "Rising on IFRS 16 + NHSPS rent uplifts + Cheshire East 0-19 contract take-on (2020) expanding base-station footprint"},
            {"label": "Delivery body", "value": "WCHC Estates & Facilities + NHS Property Services + NHSE leasing framework"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + NHS Property Services + Cheshire & Merseyside ICB"},
            {"label": "Evaluation evidence", "value": "WCHC ARA (FY25); CQC inspection (RY7 — Good); ERIC estates returns"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2011 PCT-era estate transferred to NHSPS · Successor: continued estate consolidation under Three Shifts + NHSPS lease modernisation"}
        ],
        "notes": "WCHC has expanded geographically since 2020 by taking on Cheshire East 0-19 services (school nursing, health visiting), which lifted the base-station footprint and lease bill from a relatively small Wirral-only profile. The c. £0.46M lease line reflects this dual-area coverage with most premises leased from NHSPS under group-lease arrangements, lifted by IFRS 16 application from 2022-23. Drivers include NHSPS rent uplifts (multi-year rent reviews), growing district-nursing pool-fleet, and the Cheshire East contract footprint. The Three Shifts policy direction (community + prevention + digital) is likely to keep this line on a rising trajectory.",
        "sources": [
            {"publisher": "Wirral Community Health and Care NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.wchc.nhs.uk/about-us/corporate-information/annual-reports/"},
            {"publisher": "Care Quality Commission", "title": "Wirral Community Health and Care NHS Foundation Trust provider profile (RY7)", "url": "https://www.cqc.org.uk/provider/RY7"},
            {"publisher": "IFRS Foundation", "title": "IFRS 16 Leases", "url": "https://www.ifrs.org/issued-standards/list-of-standards/ifrs-16-leases/"},
            {"publisher": "NHS Property Services", "title": "NHSPS — community estate group leases", "url": "https://www.property.nhs.uk/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 ch.7", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Lord Darzi / DHSC", "title": "Independent investigation of the NHS in England (Sep 2024)", "url": "https://www.gov.uk/government/publications/independent-investigation-of-the-nhs-in-england"}
        ],
        "related": ["Wirral Community Health and Care NHS Foundation Trust", "Premises & Infrastructure", "NHS Community Trusts", "Lease expenditure — Lincolnshire Community Health Services NHS Trust", "Lease expenditure — Norfolk Community Health and Care NHS Trust", "NHS Property Services"]
    },
    "Amortisation — West Midlands Ambulance Service University NHS Foundation Trust": {
        "aliases": [{"name": "Amortisation", "parent": "West Midlands Ambulance Service University NHS Foundation Trust"}],
        "description": "WMAS's £0.46M amortisation charge represents the systematic write-down of intangible assets — primarily Computer-Aided Despatch (CAD) software, capitalised 999 telephony platforms, EPR/Patient Clinical Records system development, capitalised software for Make Ready Centre logistics, and Microsoft enterprise licensing — across the trust's footprint covering the entire West Midlands region (Birmingham, Black Country, Coventry & Warwickshire, Herefordshire, Worcestershire, Shropshire, Staffordshire). The charge runs over typical 3-5 year useful lives for software per DHSC GAM ch.5; longer asset lives for bespoke clinical-systems integration.",
        "beneficiaries": "Serves a c. 5.9M West Midlands population across c. 5,000 sq miles (Birmingham, Black Country, Coventry & Warks, Herefordshire, Worcs, Shropshire, Staffs); responds to c. 1.1M 999 incidents/yr — making WMAS the highest-performing English ambulance trust on Cat-1 and Cat-2 standards; c. 5,500 WTE staff; operates from c. 15 hub-and-spoke Make Ready Centres including the model HQ MRC at Brierley Hill.",
        "legal_basis": "IAS 38 Intangible Assets · DHSC Group Accounting Manual 2024-25 ch.5 · NHS Act 2006 · Health and Care Act 2022 · IFRS 16 (where intangibles relate to leased software)",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£459,875"},
            {"label": "Specialty footprint", "value": "Regional 999 ambulance — entire West Midlands region (7 county/met areas · c. 5,000 sq miles)"},
            {"label": "Population served", "value": "c. 5.9M West Midlands residents"},
            {"label": "Annual activity", "value": "c. 1.1M 999 incidents (highest-performing English ambulance trust on Cat-1/Cat-2 ARP standards)"},
            {"label": "Workforce", "value": "c. 5,500 WTE; paramedics + ECAs + technicians + EOC at Brierley Hill"},
            {"label": "Estate", "value": "Pioneered hub-and-spoke MRC model — c. 15 Make Ready Centres + small estate footprint vs other trusts"},
            {"label": "Intangible asset profile", "value": "CAD software dispatch + 999 telephony + EPR/PCR · capitalised Microsoft licensing · MRC logistics + CFR fleet software"},
            {"label": "Useful life", "value": "Typically 3-5 years for software per DHSC GAM ch.5"},
            {"label": "Funding trajectory", "value": "Rising on Frontline Digitisation capitalisation + capitalised CAD upgrades + EPR/PCR software unwind"},
            {"label": "Delivery body", "value": "WMAS Finance + Digital/IT + capitalisation board · CAD vendor · Microsoft enterprise"},
            {"label": "Policy owner", "value": "NHSE Urgent and Emergency Care + NHSE Digital + DHSC + 5 West Midlands ICBs"},
            {"label": "Evaluation evidence", "value": "WMAS ARA; CQC inspection (RYA — Outstanding only ambulance trust at Outstanding); ORH benchmarks; AACE national activity"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2006 county-level WM ambulance services merged · Successor: ongoing CAD upgrade + ARP demand growth + Net Zero fleet electrification"}
        ],
        "notes": "WMAS is the only ambulance trust in England rated CQC Outstanding and is the highest-performing on Cat-1 and Cat-2 ARP response-time standards, partly due to its pioneering hub-and-spoke Make Ready Centre model which it rolled out in the late 2000s. The c. £0.46M amortisation reflects capitalised CAD dispatch software, 999 telephony, EPR/PCR and Microsoft enterprise licensing unwinding over 3-5 year useful lives. Recent context includes the 2023-24 industrial action (paramedic strikes by GMB and Unison — though WMAS was less affected than peer trusts), Frontline Digitisation capitalised investment, and ongoing CAD platform upgrades. The University title reflects the trust's strong paramedic-education and research role.",
        "sources": [
            {"publisher": "West Midlands Ambulance Service University NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://wmas.nhs.uk/about-us/corporate-publications/annual-reports/"},
            {"publisher": "Care Quality Commission", "title": "West Midlands Ambulance Service University NHS Foundation Trust provider profile (RYA — Outstanding)", "url": "https://www.cqc.org.uk/provider/RYA"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (ch.5 amortisation)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "IFRS Foundation", "title": "IAS 38 Intangible Assets", "url": "https://www.ifrs.org/issued-standards/list-of-standards/ias-38-intangible-assets/"},
            {"publisher": "NHS England", "title": "Ambulance Response Programme — Cat-1/Cat-2 standards", "url": "https://www.england.nhs.uk/urgent-emergency-care/improving-ambulance-services/arp/"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/connecting-health-and-care-providers/frontline-digitisation/"}
        ],
        "related": ["West Midlands Ambulance Service University NHS Foundation Trust", "Premises & Infrastructure", "NHS Ambulance Trusts", "Amortisation — South Central Ambulance Service NHS Foundation Trust", "Amortisation — London Ambulance Service NHS Trust", "NHS England"]
    },
    "Inventories written down — Great Ormond Street Hospital for Children NHS Foundation Trust": {
        "aliases": [{"name": "Inventories written down", "parent": "Great Ormond Street Hospital for Children NHS Foundation Trust"}],
        "description": "GOSH's £0.46M inventories-written-down line captures the IAS 2 charge for stock written off below cost — chiefly time-expired pharmaceuticals (high-cost paediatric oncology drugs, ATMP/CAR-T components, factor concentrates and ophthalmic/neuro intra-vitreal injections), expired consumables (paediatric-sized cardiothoracic surgical kit, paediatric anaesthetic circuits, ECMO components), and obsolete bespoke implant stock. Paediatric specialist trusts hold lower-volume/higher-unit-cost inventory profiles than general acute trusts, raising the absolute write-down value per turnover.",
        "beneficiaries": "Serves the UK and international quaternary paediatric referral base from the Bloomsbury main site (London) — c. 280,000 outpatient attendances + c. 100,000 inpatient + day-case admissions/yr; c. 5,000 WTE staff including c. 800 doctors and c. 1,500 nurses across c. 50+ paediatric subspecialties from rare-disease metabolic medicine to paediatric cardiac surgery, BMT, gene therapy and ATMP CAR-T.",
        "legal_basis": "IAS 2 Inventories · DHSC Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · Drug Tariff (NHS Act 2006 Sch 1) · MHRA medicines regulation",
        "key_stats": [
            {"label": "Inventories written down 2024-25", "value": "£0.46M"},
            {"label": "Specialty footprint", "value": "UK's largest paediatric quaternary referral centre — paediatric cardiac, BMT, gene therapy, ATMP CAR-T, rare-disease metabolic, paediatric oncology"},
            {"label": "Catchment", "value": "UK + international paediatric quaternary referrals; c. 280,000 outpatient attendances + c. 100,000 inpatient/day-case admissions/yr"},
            {"label": "Workforce", "value": "c. 5,000 WTE; c. 800 doctors; c. 1,500 nurses; c. 50+ paediatric subspecialty divisions"},
            {"label": "Stock profile", "value": "Paediatric oncology drugs (high unit cost) + ATMP CAR-T components + factor concentrates + bespoke paediatric implants + paediatric anaesthetic kit + ECMO consumables"},
            {"label": "Write-down driver", "value": "Time-expiry of high-cost low-volume paediatric drugs + bespoke implant obsolescence + ATMP cell-therapy QC failures"},
            {"label": "Procurement route", "value": "NHS Supply Chain + direct manufacturer agreements (paediatric oncology, factor concentrates, ATMP) + bespoke implant suppliers"},
            {"label": "Funding trajectory", "value": "Rising on growing ATMP / gene-therapy / CAR-T programme + paediatric cardiac surgery volume growth + global API price pressure"},
            {"label": "Delivery body", "value": "GOSH Pharmacy + Procurement + Theatres stock control + NHS Supply Chain + ATMP cell-therapy facility"},
            {"label": "Policy owner", "value": "NHSE Specialised Commissioning (paediatric quaternary, ATMP, gene therapy) + NICE (HST appraisals) + DHSC + MHRA"},
            {"label": "Evaluation evidence", "value": "GOSH ARA; CQC inspection (RP4 — Good); NHSE Specialised Commissioning paediatric dashboards; Model Hospital paediatric benchmarks"},
            {"label": "Predecessor / successor", "value": "Predecessor: standard expired-stock write-off practice · Successor: tighter ATMP cell-therapy QC controls + Frontline Digitisation stock-management software + global ATMP supply chain maturation"}
        ],
        "notes": "GOSH operates one of the most specialised inventory profiles in the NHS — paediatric oncology drugs, ATMP CAR-T cell-therapy components, factor concentrates for paediatric haematology, and bespoke paediatric implants are all high-unit-cost low-volume items where write-downs from time-expiry or QC failure can be material relative to total inventory turnover. The c. £0.46M reflects normal IAS 2 NRV adjustments. Drivers include the rapidly growing ATMP / gene-therapy / CAR-T programme (GOSH is one of the world-leading paediatric ATMP centres), bespoke paediatric implant obsolescence (small-patient implants have shorter useful lives), and global API price pressure on paediatric oncology compounds. Recent context includes the post-COVID elective recovery driving bespoke stock turnover and ongoing Specialised Commissioning growth.",
        "sources": [
            {"publisher": "Great Ormond Street Hospital for Children NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.gosh.nhs.uk/about-us/our-publications/annual-report-and-accounts/"},
            {"publisher": "Care Quality Commission", "title": "Great Ormond Street Hospital for Children NHS Foundation Trust provider profile (RP4)", "url": "https://www.cqc.org.uk/provider/RP4"},
            {"publisher": "IFRS Foundation", "title": "IAS 2 Inventories", "url": "https://www.ifrs.org/issued-standards/list-of-standards/ias-2-inventories/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Specialised commissioning — paediatric quaternary services + ATMP commissioning", "url": "https://www.england.nhs.uk/commissioning/spec-services/"},
            {"publisher": "NICE", "title": "Highly Specialised Technologies (HST) appraisal programme", "url": "https://www.nice.org.uk/about/what-we-do/our-programmes/nice-guidance/nice-highly-specialised-technologies-guidance"}
        ],
        "related": ["Great Ormond Street Hospital for Children NHS Foundation Trust", "Clinical Supplies & Drugs", "NHS Specialist Trusts", "Drugs costs — North East Ambulance Service NHS Foundation Trust", "Drugs costs — East Midlands Ambulance Service NHS Trust", "NHS England"]
    },
    "Business rates — Liverpool Heart and Chest Hospital NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "Liverpool Heart and Chest Hospital NHS Foundation Trust"}],
        "description": "LHCH's £0.44M non-domestic-rates bill covers business rates payable on the trust's specialist cardiothoracic estate centred on the Thomas Drive site in Broadgreen, Liverpool — one of the largest single-site cardiothoracic specialist centres in the UK delivering tertiary cardiac surgery, cardiology, thoracic surgery, respiratory medicine and aortic-vascular services. NDR is paid to Liverpool City Council under the Local Government Finance Act 1988, with rateable values from the Valuation Office Agency 2023 rating list driving the multiplier-based liability. The trust has been rated CQC Outstanding consistently and is one of the highest-volume cardiothoracic centres in Europe.",
        "beneficiaries": "Serves a c. 2.8M Cheshire & Merseyside + Isle of Man + North Wales supra-regional cardiothoracic catchment; delivers c. 2,500 cardiac surgeries + c. 5,000 cardiac caths + c. 1,500 thoracic surgeries + c. 25,000 echo studies + c. 70,000 outpatient attendances/yr; c. 1,800 WTE staff at the Thomas Drive main site (Broadgreen, Liverpool).",
        "legal_basis": "Local Government Finance Act 1988 (Sch 6 — non-domestic rating) · Non-Domestic Rating Act 2023 · Non-Domestic Rating (Multipliers and Private Finance) Act 2024 · Valuation Office Agency 2023 rating list · DHSC Group Accounting Manual 2024-25",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£441,933"},
            {"label": "Specialty footprint", "value": "Specialist cardiothoracic — cardiac surgery, interventional cardiology, electrophysiology, thoracic surgery, respiratory, aortic-vascular"},
            {"label": "Catchment", "value": "c. 2.8M Cheshire & Merseyside + Isle of Man + North Wales supra-regional cardiothoracic referrals"},
            {"label": "Annual activity", "value": "c. 2,500 cardiac surgeries; c. 5,000 cardiac caths; c. 1,500 thoracic; c. 25,000 echos; c. 70,000 OP attendances"},
            {"label": "Workforce", "value": "c. 1,800 WTE at Thomas Drive (Broadgreen) main site"},
            {"label": "Estate", "value": "Thomas Drive site (Broadgreen, Liverpool) — modern PFI-built tower (2014) + legacy buildings"},
            {"label": "Billing authority", "value": "Liverpool City Council"},
            {"label": "VOA list cycle", "value": "2023 rating list (3-year cycle from 2026 revaluation under Non-Domestic Rating Act 2023)"},
            {"label": "NDR multiplier 2024-25", "value": "Standard 54.6p; small-business 49.9p; healthcare estate generally on standard multiplier (no NHS exemption)"},
            {"label": "Funding trajectory", "value": "Rising c. 3-5%/yr in line with multiplier uprating + 2023 VOA revaluation effects on Liverpool RVs"},
            {"label": "Delivery body", "value": "LHCH Estates & Facilities + Liverpool City Council billing authority + VOA"},
            {"label": "Policy owner", "value": "MHCLG + HM Treasury + DHSC + NHSE Specialised Commissioning (cardiothoracic) + Cheshire & Merseyside ICB"},
            {"label": "Evaluation evidence", "value": "LHCH ARA; CQC inspection (RBQ — Outstanding repeatedly); GIRFT cardiothoracic; NHSE Specialised Commissioning dashboards"},
            {"label": "Predecessor / successor", "value": "Predecessor: c. 1991 Cardiothoracic Centre at Broadgreen + 2014 PFI-built new tower · Successor: 2026 VOA revaluation under 3-year cycle"}
        ],
        "notes": "LHCH pays full non-domestic rates on its Broadgreen single-site estate with no NHS exemption — unlike charities, NHS bodies do not receive the 80% mandatory relief. The c. £0.44M reflects a modern specialist-cardiothoracic estate including the 2014 PFI-built tower. As one of Europe's highest-volume cardiothoracic centres and a CQC-Outstanding trust, LHCH's NDR is on a standard rising trajectory. Drivers include the 2023 VOA revaluation effects on Liverpool RVs, annual multiplier uprating, and the new supplementary multiplier introduced by the Non-Domestic Rating (Multipliers and Private Finance) Act 2024. The 2026 revaluation cycle is the next reset point.",
        "sources": [
            {"publisher": "Liverpool Heart and Chest Hospital NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.lhch.nhs.uk/about-us/corporate-information/annual-reports/"},
            {"publisher": "Care Quality Commission", "title": "Liverpool Heart and Chest Hospital NHS Foundation Trust provider profile (RBQ — Outstanding)", "url": "https://www.cqc.org.uk/provider/RBQ"},
            {"publisher": "Valuation Office Agency", "title": "Find a business rates valuation (2023 rating list)", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "UK Government", "title": "Non-Domestic Rating Act 2023", "url": "https://www.legislation.gov.uk/ukpga/2023/53"},
            {"publisher": "UK Government", "title": "Non-Domestic Rating (Multipliers and Private Finance) Act 2024", "url": "https://www.legislation.gov.uk/ukpga/2024/26"},
            {"publisher": "NHS England", "title": "Specialised commissioning — cardiothoracic service specifications", "url": "https://www.england.nhs.uk/commissioning/spec-services/"}
        ],
        "related": ["Liverpool Heart and Chest Hospital NHS Foundation Trust", "Premises & Infrastructure", "NHS Specialist Trusts", "Business rates — Liverpool Women's NHS Foundation Trust", "Business rates — Hounslow and Richmond Community Healthcare NHS Trust", "Valuation Office Agency"]
    }
}
