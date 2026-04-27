# -*- coding: utf-8 -*-
"""Phase 2 SCamb chunk 09 — 17 NHS Specialist/Community/Ambulance Trust orphan sub-lines."""

NEW = {
    "Transport (business + patient) — Norfolk Community Health and Care NHS Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "Norfolk Community Health and Care NHS Trust"}],
        "description": "Business and patient transport at Norfolk Community Health and Care NHS Trust (NCH&C) — primarily AMAP mileage reimbursement for the trust's district nursing, community matron, MSK physio and end-of-life teams driving across one of England's largest and most rural ICS footprints. The £2.37M also includes pool-fleet leases (IFRS 16 right-of-use assets), patient ambulance journeys for community-hospital transfers, and Eastern AHSN courier links between Dereham, North Walsham and Norwich community hubs. Norfolk's geography (low population density, dispersed market towns) makes per-contact travel intrinsically high.",
        "beneficiaries": "~2,800 WTE serving the ~900,000 residents of Norfolk via ~1.4M annual community contacts across 4 community hospitals and 60+ clinics.",
        "legal_basis": "NHS Act 2006 · NHSE Patient Transport Services eligibility criteria · Agenda for Change s.17 mileage rates plus HMRC AMAP · IFRS 16 Leases (pool fleet) · Health and Care Act 2022",
        "key_stats": [
            {"label": "Transport (business + patient) 2023-24", "value": "£2.37M"},
            {"label": "Parent line", "value": "Premises & Infrastructure"},
            {"label": "Trust category", "value": "NHS Community"},
            {"label": "Catchment population", "value": "~900,000 (Norfolk)"},
            {"label": "WTE staff", "value": "~2,800"},
            {"label": "Annual contacts", "value": "~1.4M"},
            {"label": "Community hospitals", "value": "4 (Dereham, North Walsham, Swaffham, Benjamin Court)"},
            {"label": "ICS", "value": "Norfolk and Waveney ICB"},
            {"label": "Geography", "value": "Largely rural; one of England's largest county footprints"},
            {"label": "AMAP rate", "value": "45p/mile first 10k (HMRC)"},
            {"label": "CQC most recent rating", "value": "Good"},
            {"label": "Trust authorised", "value": "2011"}
        ],
        "notes": "Delivery body: NCH&C Fleet and Estates teams plus Workforce (mileage payroll); pool-vehicle leases through NHS Fleet Solutions and NHS Shared Business Services frameworks; patient transfers brokered with East of England Ambulance Service for non-emergency journeys. Policy owner: NHSE Provider Finance for envelope; Norfolk and Waveney ICB as commissioner; DHSC GAM 2024-25 for accounting; NHSE Patient Transport Services policy guides eligibility. Funding trajectory: rising — fuel inflation, IFRS 16 right-of-use recognition (2022 step-up), and Three Shifts (Darzi Sep 2024) expansion of virtual wards and home-based care all push miles travelled. Evaluation: CQC Good; NHSE Operational Plan returns; Model Hospital community benchmarks. Predecessor: NCH&C carved out of Norfolk PCT in 2011; successor: ongoing fleet electrification and NHS Net Zero by 2040 target driving EV pilot in district-nursing pool.",
        "sources": [
            {"publisher": "Norfolk Community Health and Care NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.norfolkcommunityhealthandcare.nhs.uk/about-us/annual-report-and-accounts/"},
            {"publisher": "NHS England", "title": "Non-Emergency Patient Transport Services eligibility criteria (2022)", "url": "https://www.england.nhs.uk/publication/non-emergency-patient-transport-services-eligibility-criteria/"},
            {"publisher": "HMRC", "title": "Approved Mileage Allowance Payments (AMAP) rates", "url": "https://www.gov.uk/government/publications/rates-and-allowances-travel-mileage-and-fuel-allowances"},
            {"publisher": "Care Quality Commission", "title": "Norfolk Community Health and Care NHS Trust inspection reports", "url": "https://www.cqc.org.uk/provider/RY3"},
            {"publisher": "Lord Darzi", "title": "Independent Investigation of the NHS in England (Sep 2024)", "url": "https://www.gov.uk/government/publications/independent-investigation-of-the-nhs-in-england"},
            {"publisher": "NHS England", "title": "Delivering a net zero NHS", "url": "https://www.england.nhs.uk/greenernhs/a-net-zero-nhs/"}
        ],
        "related": ["Premises & Infrastructure — Norfolk Community Health and Care NHS Trust", "Norfolk Community Health and Care NHS Trust", "Norfolk and Waveney ICB", "Lord Darzi Independent Investigation 2024", "NHS Net Zero by 2040"]
    },
    "Business rates — South East Coast Ambulance Service NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "South East Coast Ambulance Service NHS Foundation Trust"}],
        "description": "Non-domestic rates levied on the SECAmb estate — make-ready centres at Banstead and Crawley, regional fleet workshops, ~70 ambulance stations and standby points across Kent, Surrey, Sussex and North East Hampshire, the EOC at Coxheath (999 dispatch), and the Resilience HQ at Nutfield. The £2.36M reflects 2023 list valuations applied at the small business multiplier, with limited charitable mandatory relief because most sites are NHS-owned operational hereditaments. The 2023 revaluation pushed rateable values up across the South East where land values are highest.",
        "beneficiaries": "~4,200 WTE responding to ~1.0M 999 calls and ~700,000 incidents annually for ~5.0M residents of Kent, Surrey, Sussex and NE Hampshire.",
        "legal_basis": "Local Government Finance Act 1988 (Schedule 6) · Non-Domestic Rating Act 2023 · Non-Domestic Rating (Multipliers and Private Finance) Act 2024 · NHS Act 2006 · 2023 Rating List (VOA)",
        "key_stats": [
            {"label": "Business rates 2023-24", "value": "£2.36M"},
            {"label": "Parent line", "value": "Premises & Infrastructure"},
            {"label": "Trust category", "value": "NHS Ambulance"},
            {"label": "Catchment population", "value": "~5.0M (Kent, Surrey, Sussex, NE Hants)"},
            {"label": "Ambulance stations + standby", "value": "~70"},
            {"label": "Make ready centres", "value": "2 (Banstead, Crawley)"},
            {"label": "EOC", "value": "Coxheath, Maidstone"},
            {"label": "WTE staff", "value": "~4,200"},
            {"label": "999 calls / year", "value": "~1.0M"},
            {"label": "Incidents / year", "value": "~700,000"},
            {"label": "FT authorised", "value": "2011"},
            {"label": "Most recent CQC rating", "value": "Requires Improvement (2023)"}
        ],
        "notes": "Delivery body: SECAmb Estates and Facilities, with rating advisory typically procured via NHS Shared Business Services framework; billing authorities are the 30+ districts and unitaries across the patch. Policy owner: DLUHC for the rating system and multiplier; VOA for valuations; Treasury for the 2024 multiplier reform; NHSE Provider Finance for the funding envelope. Funding trajectory: stepped up at the 2023 revaluation; the 2024 Act introduced lower multipliers for retail, hospitality and leisure but NHS hereditaments remain on the standard multiplier (51.2p in 2024-25), so SECAmb sees only multiplier inflation. Evaluation: CQC Requires Improvement (2023, Cat-2 response and culture concerns); NHSE Operational Plan returns; Lord Carter ambulance review benchmarks; ORH demand-and-capacity reviews. Predecessor: SECAmb formed 2006 from merger of Kent, Surrey, Sussex services; successor: estate consolidation programme including new Make Ready Centres replacing legacy stations.",
        "sources": [
            {"publisher": "South East Coast Ambulance Service NHS FT", "title": "Annual Report and Accounts 2023-24", "url": "https://www.secamb.nhs.uk/about-us/annual-reports/"},
            {"publisher": "Valuation Office Agency", "title": "2023 Rating List", "url": "https://www.gov.uk/government/collections/business-rates-2023-revaluation"},
            {"publisher": "Care Quality Commission", "title": "South East Coast Ambulance Service NHSFT inspection reports", "url": "https://www.cqc.org.uk/provider/RYD"},
            {"publisher": "UK Government", "title": "Non-Domestic Rating (Multipliers and Private Finance) Act 2024", "url": "https://www.legislation.gov.uk/ukpga/2024/15/contents"},
            {"publisher": "NHS England", "title": "Ambulance services — Operational Plan returns", "url": "https://www.england.nhs.uk/statistics/statistical-work-areas/ambulance-quality-indicators/"}
        ],
        "related": ["Premises & Infrastructure — South East Coast Ambulance Service NHS Foundation Trust", "South East Coast Ambulance Service NHS Foundation Trust", "Valuation Office Agency", "Non-Domestic Rating Act 2023", "Lord Carter NHS Ambulance Review"]
    },
    "General supplies & services — Alder Hey Children's NHS Foundation Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "Alder Hey Children's NHS Foundation Trust"}],
        "description": "Non-pharmaceutical clinical consumables at Alder Hey — paediatric-specific dressings, IV sets sized for neonates and small children, single-use surgical instruments for children's theatre, neonatal and PICU consumables, and play-therapy and family-room consumables. Alder Hey is one of Europe's largest children's hospitals (and a designated tertiary specialised commissioner), so the £2.28M is small in trust terms but the per-unit cost mix is heavily weighted toward small-volume paediatric SKUs that NHS Supply Chain frameworks underprice; many items are ordered direct.",
        "beneficiaries": "~4,200 WTE serving ~330,000 patient contacts/year, with ~270,000 ED attendances and ~16,000 surgical procedures for children across Cheshire & Merseyside and as a tertiary specialised centre.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 2 Inventories (consumption interaction) · NHS Act 2006 · NHSE Specialised Services contracts · NHS Supply Chain framework",
        "key_stats": [
            {"label": "General supplies & services 2023-24", "value": "£2.28M"},
            {"label": "Parent line", "value": "Clinical Supplies & Drugs"},
            {"label": "Trust category", "value": "NHS Specialist (paediatric)"},
            {"label": "Specialty", "value": "Tertiary children's hospital"},
            {"label": "ED attendances / year", "value": "~270,000"},
            {"label": "Surgical procedures / year", "value": "~16,000"},
            {"label": "WTE staff", "value": "~4,200"},
            {"label": "ICS", "value": "Cheshire and Merseyside ICB"},
            {"label": "Specialised commissioning", "value": "NHSE direct (paediatric tertiary)"},
            {"label": "Main site", "value": "Alder Hey in the Park, Liverpool (opened 2015)"},
            {"label": "Foundation Trust authorised", "value": "2008"},
            {"label": "Children's hospital ranking", "value": "One of Europe's largest"}
        ],
        "notes": "Delivery body: Alder Hey Procurement and theatres / PICU / neonatal supply teams, with NHS Supply Chain delivering routine items via Towers and a long tail of direct-from-manufacturer paediatric-sized items not in the standard catalogue. Policy owner: NHSE Specialised Commissioning sets contract envelope for tertiary paediatric services; DHSC for GAM treatment; NHS Supply Chain (NHSBSA-sponsored) for category management. Funding trajectory: rising — paediatric subspecialty growth (cardiac, neuro, oncology), inflation passthrough on single-use SKUs, and post-COVID infection-prevention pricing all push the line. Evaluation: CQC Good (2023); NHSE Specialised Services contract performance; Model Hospital paediatric benchmarks. Predecessor: Alder Hey moved to its £237M new-build 'in the Park' in 2015 (PFI-funded); successor: ongoing campus completion (Catkin and Sunflower mental health and community children's facilities) and tighter integration with Liverpool University Hospitals on transition pathways.",
        "sources": [
            {"publisher": "Alder Hey Children's NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://alderhey.nhs.uk/about/annual-report"},
            {"publisher": "NHS England", "title": "Specialised commissioning — paediatric services", "url": "https://www.england.nhs.uk/commissioning/spec-services/"},
            {"publisher": "NHS Supply Chain", "title": "About the NHS Supply Chain operating model", "url": "https://www.supplychain.nhs.uk/about-us/"},
            {"publisher": "Care Quality Commission", "title": "Alder Hey Children's NHSFT inspection reports", "url": "https://www.cqc.org.uk/provider/RBS"},
            {"publisher": "DHSC", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"}
        ],
        "related": ["Clinical Supplies & Drugs — Alder Hey Children's NHS Foundation Trust", "Alder Hey Children's NHS Foundation Trust", "NHS Supply Chain", "NHSE Specialised Commissioning", "Cheshire and Merseyside ICB"]
    },
    "General supplies & services — Royal Papworth Hospital NHS Foundation Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "Royal Papworth Hospital NHS Foundation Trust"}],
        "description": "Non-pharmaceutical clinical consumables at Royal Papworth — the UK's largest specialist heart and lung hospital, sited on the Cambridge Biomedical Campus since 2019 and the country's main centre for heart and lung transplantation, ECMO, complex cardiac surgery and respiratory medicine. The £2.26M covers cardiothoracic theatre consumables, perfusion circuits, ECMO tubing not on a Service Line code, ICU airway and ventilation consumables, and respiratory diagnostics consumables. Specialised commissioning via NHSE direct, not the local ICB.",
        "beneficiaries": "~2,300 WTE supporting ~26,000 inpatient/day-case admissions, ~110,000 outpatient attendances, and the UK's largest heart-and-lung transplant programme (~140 transplants/year combined).",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 2 Inventories · NHS Act 2006 · NHSE Specialised Services contracts (cardiothoracic, transplant, ECMO) · NHS Supply Chain framework",
        "key_stats": [
            {"label": "General supplies & services 2023-24", "value": "£2.26M"},
            {"label": "Parent line", "value": "Clinical Supplies & Drugs"},
            {"label": "Trust category", "value": "NHS Specialist (cardiothoracic)"},
            {"label": "Specialty", "value": "Heart and lung — largest UK centre"},
            {"label": "Site", "value": "Cambridge Biomedical Campus (since 2019)"},
            {"label": "Inpatient + day-case admissions", "value": "~26,000"},
            {"label": "Outpatient attendances", "value": "~110,000"},
            {"label": "Heart + lung transplants / year", "value": "~140 (combined)"},
            {"label": "ICU / ECMO bed base", "value": "~46 critical care beds"},
            {"label": "WTE staff", "value": "~2,300"},
            {"label": "Foundation Trust authorised", "value": "2004"},
            {"label": "CQC most recent rating", "value": "Outstanding"}
        ],
        "notes": "Delivery body: Royal Papworth Procurement and theatre / perfusion / ECMO supply leads, with NHS Supply Chain Towers covering routine surgical consumables and direct contracts for low-volume high-spec cardiothoracic items (LVAD/ECMO accessories, transplant-specific kits). Policy owner: NHSE Specialised Commissioning sets envelope for cardiothoracic, transplant and ECMO contracts; DHSC for GAM treatment; NHS Supply Chain for category management. Funding trajectory: rising — transplant volumes recovered post-pandemic, ECMO demand increased after COVID-19, and inflation passthrough on consumables persists. Evaluation: CQC Outstanding (2019, retained); NHSE specialised services contract performance; UK Transplant Registry (NHS Blood and Transplant) outcome metrics. Predecessor: Royal Papworth moved from rural Papworth Everard to its new £165M building on the Cambridge Biomedical Campus in May 2019; successor: deepening clinical integration with Cambridge University Hospitals (Addenbrooke's) and the AstraZeneca / MRC Cambridge cluster.",
        "sources": [
            {"publisher": "Royal Papworth Hospital NHS FT", "title": "Annual Report and Accounts 2023-24", "url": "https://royalpapworth.nhs.uk/about-us/our-publications/annual-report-and-accounts"},
            {"publisher": "NHS England", "title": "Specialised services — cardiothoracic transplantation", "url": "https://www.england.nhs.uk/commissioning/spec-services/npc-crg/group-a/a06/"},
            {"publisher": "NHS Blood and Transplant", "title": "Annual report on cardiothoracic transplantation", "url": "https://www.odt.nhs.uk/statistics-and-reports/annual-activity-report/"},
            {"publisher": "Care Quality Commission", "title": "Royal Papworth Hospital NHSFT inspection reports", "url": "https://www.cqc.org.uk/provider/RGM"},
            {"publisher": "NHS Supply Chain", "title": "About the NHS Supply Chain operating model", "url": "https://www.supplychain.nhs.uk/about-us/"}
        ],
        "related": ["Clinical Supplies & Drugs — Royal Papworth Hospital NHS Foundation Trust", "Royal Papworth Hospital NHS Foundation Trust", "NHSE Specialised Commissioning", "Cambridge Biomedical Campus", "NHS Blood and Transplant"]
    },
    "General supplies & services — The Robert Jones and Agnes Hunt Orthopaedic Hospital NHS Foundation Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "The Robert Jones and Agnes Hunt Orthopaedic Hospital NHS Foundation Trust"}],
        "description": "Non-pharmaceutical clinical consumables at RJAH — the elective orthopaedic specialist trust at Gobowen, Oswestry, providing hip and knee replacement, spinal surgery, MSK, paediatric orthopaedic and sarcoma services to a supra-regional catchment across Shropshire, mid-Wales, Cheshire, Staffordshire and Powys. The £2.26M covers theatre consumables (drapes, sutures, single-use instruments) outside the Service Line implants envelope, plus rehab and limb-fitting consumables for the trust's MSK and prosthetics service. Implants themselves sit in a separate line.",
        "beneficiaries": "~1,400 WTE serving a supra-regional catchment of ~1.5M, with ~7,000 inpatient/day-case episodes and ~70,000 outpatient attendances per year; runs the Midlands Centre for Spinal Injuries.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 2 Inventories · NHS Act 2006 · NHSE Specialised Services contracts (spinal injuries, sarcoma) · NHS Supply Chain framework · Health and Care Act 2022",
        "key_stats": [
            {"label": "General supplies & services 2023-24", "value": "£2.26M"},
            {"label": "Parent line", "value": "Clinical Supplies & Drugs"},
            {"label": "Trust category", "value": "NHS Specialist (orthopaedic)"},
            {"label": "Specialty", "value": "Elective orthopaedic + spinal injuries"},
            {"label": "Site", "value": "Gobowen, Oswestry (1900 sanatorium origin)"},
            {"label": "Inpatient / day-case episodes", "value": "~7,000"},
            {"label": "Outpatient attendances", "value": "~70,000"},
            {"label": "Catchment population", "value": "~1.5M (supra-regional)"},
            {"label": "WTE staff", "value": "~1,400"},
            {"label": "ICS", "value": "Shropshire, Telford and Wrekin ICB (host)"},
            {"label": "Foundation Trust authorised", "value": "2011"},
            {"label": "CQC most recent rating", "value": "Good"}
        ],
        "notes": "Delivery body: RJAH Procurement and theatre supply teams, with NHS Supply Chain Towers 4 and 7 (orthopaedic and theatre consumables) plus direct contracts for spinal-injury rehab consumables. Policy owner: NHSE Specialised Commissioning sets envelope for spinal injuries and bone tumour services; DHSC for GAM; Shropshire, Telford and Wrekin ICB hosts trust. Funding trajectory: rising — elective recovery push (2024 Elective Reform Plan) increases through-put, RJAH is one of the listed Surgical Hubs with growth funding; inflation passthrough on theatre consumables persists. Evaluation: CQC Good; NHSE elective recovery dashboard; National Joint Registry; NHSE Specialised Services contract performance. Predecessor: trust origins as 1900 open-air sanatorium founded by Agnes Hunt; FT authorised 2011; successor: Surgical Hub designation under 2024 Elective Reform Plan and ongoing campus modernisation (Headley Court Veterans' Orthopaedic facility opened 2018).",
        "sources": [
            {"publisher": "RJAH Orthopaedic NHS FT", "title": "Annual Report and Accounts 2023-24", "url": "https://www.rjah.nhs.uk/About-Us/Annual-Reports.aspx"},
            {"publisher": "NHS England", "title": "Elective Reform Plan (2025) and Surgical Hubs", "url": "https://www.england.nhs.uk/long-read/reforming-elective-care-for-patients/"},
            {"publisher": "Care Quality Commission", "title": "RJAH Orthopaedic NHSFT inspection reports", "url": "https://www.cqc.org.uk/provider/RL1"},
            {"publisher": "NHS Supply Chain", "title": "About the NHS Supply Chain operating model", "url": "https://www.supplychain.nhs.uk/about-us/"},
            {"publisher": "National Joint Registry", "title": "21st Annual Report 2024", "url": "https://www.njrcentre.org.uk/njr-annual-reports/"}
        ],
        "related": ["Clinical Supplies & Drugs — The Robert Jones and Agnes Hunt Orthopaedic Hospital NHS Foundation Trust", "The Robert Jones and Agnes Hunt Orthopaedic Hospital NHS Foundation Trust", "NHSE Specialised Commissioning", "NHS Elective Reform Plan 2025", "NHS Supply Chain"]
    },
    "General supplies & services — Wirral Community Health and Care NHS Foundation Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "Wirral Community Health and Care NHS Foundation Trust"}],
        "description": "Non-pharmaceutical clinical consumables at Wirral Community Health and Care NHS Foundation Trust (WCHC) — district nursing dressings, leg-ulcer compression kits, infection-prevention items, MSK-physio consumables, school nursing equipment, and end-of-life community pack contents. WCHC also runs the All Age Disability service for Wirral and the 0-19 universal-services contract. The £2.20M sits within a workforce-heavy community trust where consumables flow primarily to nursing teams in patients' homes, schools and community clinics across the Wirral peninsula.",
        "beneficiaries": "~1,400 WTE serving the ~325,000 residents of Wirral via ~900,000 community contacts including district nursing, health visiting, school nursing, MSK and 0-19 services.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 2 Inventories · NHS Act 2006 · Health and Care Act 2022 · NHS Supply Chain framework",
        "key_stats": [
            {"label": "General supplies & services 2023-24", "value": "£2.20M"},
            {"label": "Parent line", "value": "Clinical Supplies & Drugs"},
            {"label": "Trust category", "value": "NHS Community"},
            {"label": "Catchment population", "value": "~325,000 (Wirral)"},
            {"label": "WTE staff", "value": "~1,400"},
            {"label": "Annual contacts", "value": "~900,000"},
            {"label": "ICS", "value": "Cheshire and Merseyside ICB"},
            {"label": "0-19 universal services", "value": "Lead provider on Wirral"},
            {"label": "Foundation Trust authorised", "value": "2017 (FT) from 2011 trust"},
            {"label": "Estate landlord", "value": "Mostly NHS Property Services"},
            {"label": "Most recent CQC rating", "value": "Good"},
            {"label": "Lead procurement framework", "value": "NHS Supply Chain"}
        ],
        "notes": "Delivery body: WCHC Procurement and District Nursing leadership; NHS Supply Chain delivers routine wound-care, dressings and IPC items via Towers, with direct contracts for the 0-19 service consumables. Policy owner: NHSE Provider Finance for envelope; Cheshire and Merseyside ICB as block-contract lead; DHSC for GAM. Funding trajectory: rising — out-of-hospital direction of travel (Darzi Sep 2024 Three Shifts), virtual-ward and hospital-at-home expansion drive consumable volumes; inflation passthrough on dressings persists. Evaluation: CQC Good (2022); NHSE Operational Plan returns; Cheshire and Merseyside ICB community dashboards. Predecessor: WCHC formed 2011 from Wirral PCT, awarded FT status 2017; successor: Wirral Place-based Partnership integration with Wirral University Teaching Hospital, Wirral Community Diagnostic Centre development, and ongoing place-based pooled budget arrangements.",
        "sources": [
            {"publisher": "Wirral Community Health and Care NHS FT", "title": "Annual Report and Accounts 2023-24", "url": "https://www.wchc.nhs.uk/about-us/publications/annual-reports/"},
            {"publisher": "NHS Supply Chain", "title": "About the NHS Supply Chain operating model", "url": "https://www.supplychain.nhs.uk/about-us/"},
            {"publisher": "Care Quality Commission", "title": "Wirral Community Health and Care NHSFT inspection reports", "url": "https://www.cqc.org.uk/provider/RY7"},
            {"publisher": "Lord Darzi", "title": "Independent Investigation of the NHS in England (Sep 2024)", "url": "https://www.gov.uk/government/publications/independent-investigation-of-the-nhs-in-england"},
            {"publisher": "Cheshire and Merseyside ICB", "title": "Joint Forward Plan 2023-28", "url": "https://www.cheshireandmerseyside.nhs.uk/"}
        ],
        "related": ["Clinical Supplies & Drugs — Wirral Community Health and Care NHS Foundation Trust", "Wirral Community Health and Care NHS Foundation Trust", "NHS Supply Chain", "Cheshire and Merseyside ICB", "Lord Darzi Independent Investigation 2024"]
    },
    "Establishment costs — Hounslow and Richmond Community Healthcare NHS Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "Hounslow and Richmond Community Healthcare NHS Trust"}],
        "description": "Establishment costs at Hounslow and Richmond Community Healthcare NHS Trust (HRCH) — telephony, postage, office supplies, advertising, training, audit and bank charges, courier and indirect non-payroll non-clinical overhead. HRCH is a small community-only trust covering the West London boroughs of Hounslow and Richmond upon Thames; it provides district nursing, health visiting, school nursing, MSK, podiatry, sexual health, end-of-life and 0-19 services across a dispersed multi-site footprint. The £2.17M overhead reflects high London property and back-office prices on a relatively small revenue base.",
        "beneficiaries": "~1,500 WTE serving ~480,000 residents of Hounslow and Richmond upon Thames via ~600,000 community contacts.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Establishment costs 2023-24", "value": "£2.17M"},
            {"label": "Parent line", "value": "Premises & Infrastructure"},
            {"label": "Trust category", "value": "NHS Community"},
            {"label": "Catchment", "value": "Hounslow + Richmond upon Thames boroughs"},
            {"label": "Catchment population", "value": "~480,000"},
            {"label": "WTE staff", "value": "~1,500"},
            {"label": "Annual contacts", "value": "~600,000"},
            {"label": "ICS", "value": "North West London ICB + South West London ICB (cross-ICS)"},
            {"label": "Trust authorised", "value": "2011"},
            {"label": "Most recent CQC rating", "value": "Good"},
            {"label": "Estate landlord", "value": "Mostly NHS Property Services"},
            {"label": "Sexual health", "value": "Lead provider for Hounslow + Richmond contracts"}
        ],
        "notes": "Delivery body: HRCH Estates and Facilities + Procurement; corporate services partly delivered through shared arrangements with Hounslow and Richmond ICB partners and NHS SBS for finance and payroll. Policy owner: NHSE Provider Finance for envelope; North West London ICB and South West London ICB as commissioners; DHSC for GAM. Funding trajectory: small absolute line, broadly flat in real terms; London supplier inflation, telephony refresh and IT costs push modest growth. Evaluation: CQC Good (most recent comprehensive inspection); NHSE Operational Plan returns; ICB community dashboards. Predecessor: HRCH formed 2011 from Hounslow + Richmond PCTs; successor: continued exploration of merger / closer working with neighbouring community providers and Place-based partnerships in both boroughs.",
        "sources": [
            {"publisher": "Hounslow and Richmond Community Healthcare NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.hrch.nhs.uk/about-us/publications-and-reports/"},
            {"publisher": "Care Quality Commission", "title": "Hounslow and Richmond Community Healthcare NHS Trust inspection reports", "url": "https://www.cqc.org.uk/provider/RY9"},
            {"publisher": "DHSC", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Lord Darzi", "title": "Independent Investigation of the NHS in England (Sep 2024)", "url": "https://www.gov.uk/government/publications/independent-investigation-of-the-nhs-in-england"},
            {"publisher": "NHS England", "title": "Three Shifts and out-of-hospital care", "url": "https://www.england.nhs.uk/long-read/community-services-investment-plan/"}
        ],
        "related": ["Premises & Infrastructure — Hounslow and Richmond Community Healthcare NHS Trust", "Hounslow and Richmond Community Healthcare NHS Trust", "North West London ICB", "South West London ICB", "Lord Darzi Independent Investigation 2024"]
    },
    "Lease expenditure — Yorkshire Ambulance Service NHS Trust": {
        "aliases": [{"name": "Lease expenditure", "parent": "Yorkshire Ambulance Service NHS Trust"}],
        "description": "Lease costs at Yorkshire Ambulance Service NHS Trust (YAS) — IFRS 16 right-of-use accounting on ambulance stations, standby points, fleet workshops and the EOC at Wakefield, plus modest non-property leases. YAS covers the four Yorkshire ICSs (West, South, Humber & North Yorkshire and Coast & Vale) and runs the regional 999 service plus NHS 111 for Yorkshire. The £2.14M is the residual of property and equipment leases not otherwise on hire-purchase or capitalised vehicles after the IFRS 16 step-up was absorbed.",
        "beneficiaries": "~6,000 WTE serving ~5.4M residents of Yorkshire and the Humber via ~1.05M emergency 999 incidents and ~3.7M NHS 111 calls per year.",
        "legal_basis": "IFRS 16 Leases · DHSC Group Accounting Manual 2024-25 ch.7 · Landlord and Tenant Act 1954 · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Lease expenditure 2023-24", "value": "£2.14M"},
            {"label": "Parent line", "value": "Premises & Infrastructure"},
            {"label": "Trust category", "value": "NHS Ambulance"},
            {"label": "Catchment population", "value": "~5.4M (Yorkshire + Humber)"},
            {"label": "Ambulance stations + standby", "value": "~75"},
            {"label": "EOC", "value": "Wakefield + Springhill, York"},
            {"label": "WTE staff", "value": "~6,000"},
            {"label": "999 incidents / year", "value": "~1.05M"},
            {"label": "NHS 111 calls / year", "value": "~3.7M (Yorkshire host)"},
            {"label": "Trust formed", "value": "2006 (from West, South, North Yorks + Tees)"},
            {"label": "Most recent CQC rating", "value": "Requires Improvement"},
            {"label": "IFRS 16 transition", "value": "April 2022 (NHS adoption)"}
        ],
        "notes": "Delivery body: YAS Estates and Facilities; lease counterparties include NHS Property Services, Community Health Partnerships, local authority landlords and a small private-landlord tail. Policy owner: NHSE Provider Finance for envelope; DHSC GAM ch.7 sets IFRS 16 treatment; Treasury / FReM controls cross-public-sector accounting harmonisation. Funding trajectory: stepped up at IFRS 16 transition (April 2022) when operating leases were brought on balance sheet as right-of-use assets and lease liabilities; subsequent flat-to-rising as renewals price in inflation and YAS consolidates older stations into newer hub-and-spoke Make Ready Centres. Evaluation: CQC Requires Improvement (most recent inspection raised Cat-2 response and culture concerns); NHSE Ambulance Quality Indicators; ORH benchmark; trust ARA. Predecessor: YAS formed 2006 from merger of West, South and North Yorkshire + Tees ambulance services; successor: ongoing estate consolidation programme and electrification pilots.",
        "sources": [
            {"publisher": "Yorkshire Ambulance Service NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.yas.nhs.uk/about-us/our-publications/annual-report-and-accounts/"},
            {"publisher": "DHSC", "title": "Group Accounting Manual 2024-25 (ch.7 Leases)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Ambulance Quality Indicators", "url": "https://www.england.nhs.uk/statistics/statistical-work-areas/ambulance-quality-indicators/"},
            {"publisher": "Care Quality Commission", "title": "Yorkshire Ambulance Service NHS Trust inspection reports", "url": "https://www.cqc.org.uk/provider/RX8"},
            {"publisher": "HM Treasury", "title": "FReM 2024-25 (IFRS 16 application)", "url": "https://www.gov.uk/government/collections/government-financial-reporting-manual-frem"}
        ],
        "related": ["Premises & Infrastructure — Yorkshire Ambulance Service NHS Trust", "Yorkshire Ambulance Service NHS Trust", "NHS Property Services", "IFRS 16 Leases (NHS adoption April 2022)", "Lord Carter NHS Ambulance Review"]
    },
    "Lease expenditure — London Ambulance Service NHS Trust": {
        "aliases": [{"name": "Lease expenditure", "parent": "London Ambulance Service NHS Trust"}],
        "description": "Lease expenditure at London Ambulance Service NHS Trust (LAS) — IFRS 16 right-of-use charges on ambulance stations, standby points, fleet workshops and the two EOCs (Waterloo and Bow), plus a tail of equipment and short-life vehicle leases. LAS is the largest single ambulance trust in the UK by population served, covering the 33 London boroughs. The £2.12M reflects the residual P&L lease charge after IFRS 16 transition; many former operating leases moved onto balance sheet as right-of-use assets/liabilities, and the trust runs a hub-and-spoke estate model with much premises sat in NHS Property Services.",
        "beneficiaries": "~6,000 WTE serving ~9.0M Greater London residents via ~1.4M emergency incidents and ~2.4M 999 calls per year, with two EOCs (Waterloo, Bow).",
        "legal_basis": "IFRS 16 Leases · DHSC Group Accounting Manual 2024-25 ch.7 · Landlord and Tenant Act 1954 · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Lease expenditure 2023-24", "value": "£2.12M"},
            {"label": "Parent line", "value": "Premises & Infrastructure"},
            {"label": "Trust category", "value": "NHS Ambulance"},
            {"label": "Catchment population", "value": "~9.0M (Greater London)"},
            {"label": "Ambulance stations", "value": "~70"},
            {"label": "EOCs", "value": "2 (Waterloo, Bow)"},
            {"label": "WTE staff", "value": "~6,000"},
            {"label": "999 calls / year", "value": "~2.4M"},
            {"label": "Incidents / year", "value": "~1.4M"},
            {"label": "Trust formed", "value": "1965 as London Ambulance Service"},
            {"label": "Most recent CQC rating", "value": "Good (2023)"},
            {"label": "IFRS 16 transition", "value": "April 2022 (NHS adoption)"}
        ],
        "notes": "Delivery body: LAS Estates and Facilities (one of the largest NHS ambulance estate teams); lease counterparties include NHS Property Services, Community Health Partnerships, the GLA, TfL (for some standby-point space) and a long tail of London local authorities and private landlords. Policy owner: NHSE Provider Finance for envelope; DHSC GAM ch.7 for IFRS 16; Treasury FReM. Funding trajectory: stepped up at the April 2022 IFRS 16 NHS adoption (operating leases on balance sheet); rising thereafter as London commercial rents inflate at renewal and as the trust converts a few legacy leases into longer modernised commitments. Evaluation: CQC Good (2023, return from Requires Improvement); NHSE Ambulance Quality Indicators; Mayor of London health committee scrutiny; ORH demand-and-capacity benchmarks. Predecessor: LAS pre-dated NHS reorganisation and entered the trust era in 1996; successor: ongoing estate strategy involving fewer larger Make Ready Centres + dispersed standby points, plus EV fleet pilot.",
        "sources": [
            {"publisher": "London Ambulance Service NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.londonambulance.nhs.uk/about-us/our-publications/annual-reports/"},
            {"publisher": "DHSC", "title": "Group Accounting Manual 2024-25 (ch.7 Leases)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Ambulance Quality Indicators", "url": "https://www.england.nhs.uk/statistics/statistical-work-areas/ambulance-quality-indicators/"},
            {"publisher": "Care Quality Commission", "title": "London Ambulance Service NHS Trust inspection reports", "url": "https://www.cqc.org.uk/provider/RRU"},
            {"publisher": "HM Treasury", "title": "FReM 2024-25 (IFRS 16 application)", "url": "https://www.gov.uk/government/collections/government-financial-reporting-manual-frem"}
        ],
        "related": ["Premises & Infrastructure — London Ambulance Service NHS Trust", "London Ambulance Service NHS Trust", "NHS Property Services", "IFRS 16 Leases (NHS adoption April 2022)", "Mayor of London health committee"]
    },
    "Business rates — Royal Papworth Hospital NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "Royal Papworth Hospital NHS Foundation Trust"}],
        "description": "Non-domestic rates levied on Royal Papworth's main hospital hereditament on the Cambridge Biomedical Campus, plus residual rates on legacy assets and ancillary office space. The £2.16M reflects the 2023 list rateable value applied at the standard multiplier (51.2p in 2024-25). Royal Papworth's 2019 new build at Cambridge — a £165M PFI-style facility next to Addenbrooke's — has a substantially higher rateable value than the rural Papworth Everard predecessor site and the 2023 revaluation entrenched the higher RV.",
        "beneficiaries": "~2,300 WTE supporting ~26,000 inpatient/day-case admissions, ~110,000 outpatient attendances and the UK's largest combined heart-and-lung transplant programme.",
        "legal_basis": "Local Government Finance Act 1988 (Schedule 6) · Non-Domestic Rating Act 2023 · Non-Domestic Rating (Multipliers and Private Finance) Act 2024 · NHS Act 2006 · 2023 Rating List (VOA)",
        "key_stats": [
            {"label": "Business rates 2023-24", "value": "£2.12M"},
            {"label": "Parent line", "value": "Premises & Infrastructure"},
            {"label": "Trust category", "value": "NHS Specialist (cardiothoracic)"},
            {"label": "Specialty", "value": "Heart and lung — largest UK centre"},
            {"label": "Site", "value": "Cambridge Biomedical Campus (since 2019)"},
            {"label": "Building cost (new build)", "value": "~£165M"},
            {"label": "Inpatient + day-case admissions", "value": "~26,000"},
            {"label": "Outpatient attendances", "value": "~110,000"},
            {"label": "Heart + lung transplants / year", "value": "~140 (combined)"},
            {"label": "WTE staff", "value": "~2,300"},
            {"label": "Billing authority", "value": "South Cambridgeshire District Council"},
            {"label": "Foundation Trust authorised", "value": "2004"}
        ],
        "notes": "Delivery body: Royal Papworth Estates and Finance handle rating with NHS-framework rating advisers; billing authority is South Cambridgeshire District Council. Policy owner: DLUHC (now MHCLG) for the rating system; VOA for valuations; Treasury for the 2024 multipliers reform; NHSE Provider Finance for the funding envelope; DHSC for GAM. Funding trajectory: stepped up at the 2019 site move and again at the 2023 revaluation; the 2024 Act introduced lower multipliers for retail-hospitality-leisure but NHS hereditaments remain on the standard multiplier so Papworth sees only multiplier inflation. Evaluation: CQC Outstanding (2019, retained); NHSE Specialised Services contract performance; UK Transplant Registry outcome metrics. Predecessor: Royal Papworth at Papworth Everard (Cambridgeshire) had much lower rateable value; successor: ongoing scientific integration with the Cambridge campus and the AstraZeneca Discovery Centre.",
        "sources": [
            {"publisher": "Royal Papworth Hospital NHS FT", "title": "Annual Report and Accounts 2023-24", "url": "https://royalpapworth.nhs.uk/about-us/our-publications/annual-report-and-accounts"},
            {"publisher": "Valuation Office Agency", "title": "2023 Rating List", "url": "https://www.gov.uk/government/collections/business-rates-2023-revaluation"},
            {"publisher": "UK Government", "title": "Non-Domestic Rating (Multipliers and Private Finance) Act 2024", "url": "https://www.legislation.gov.uk/ukpga/2024/15/contents"},
            {"publisher": "South Cambridgeshire District Council", "title": "Business rates and the 2023 list", "url": "https://www.scambs.gov.uk/business-rates/"},
            {"publisher": "Care Quality Commission", "title": "Royal Papworth Hospital NHSFT inspection reports", "url": "https://www.cqc.org.uk/provider/RGM"}
        ],
        "related": ["Premises & Infrastructure — Royal Papworth Hospital NHS Foundation Trust", "Royal Papworth Hospital NHS Foundation Trust", "Valuation Office Agency", "Non-Domestic Rating Act 2023", "Cambridge Biomedical Campus"]
    },
    "General supplies & services — South Central Ambulance Service NHS Foundation Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "South Central Ambulance Service NHS Foundation Trust"}],
        "description": "Non-pharmaceutical clinical consumables at South Central Ambulance Service NHS Foundation Trust (SCAS) — paramedic single-use kit (cannulas, dressings, airway adjuncts, defib pads), Make Ready cleaning consumables, IPC items, and ambulance station consumables. SCAS covers Berkshire, Buckinghamshire, Hampshire and Oxfordshire and also delivers NHS 111 across the patch. The £2.11M is dominated by per-incident clinical consumables for paramedics on Cat-1 and Cat-2 jobs, plus station supplies; vehicle consumables sit in the Transport line.",
        "beneficiaries": "~4,200 WTE serving ~4.6M residents of Berks, Bucks, Hants and Oxon via ~720,000 emergency incidents and ~3.0M NHS 111 calls per year.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 2 Inventories · NHS Act 2006 · Health and Care Act 2022 · NHS Supply Chain framework",
        "key_stats": [
            {"label": "General supplies & services 2023-24", "value": "£2.11M"},
            {"label": "Parent line", "value": "Clinical Supplies & Drugs"},
            {"label": "Trust category", "value": "NHS Ambulance"},
            {"label": "Catchment population", "value": "~4.6M (Berks, Bucks, Hants, Oxon)"},
            {"label": "WTE staff", "value": "~4,200"},
            {"label": "Emergency incidents / year", "value": "~720,000"},
            {"label": "NHS 111 calls / year", "value": "~3.0M"},
            {"label": "Make Ready Centres", "value": "~5 (Bicester, Otterbourne, Reading area)"},
            {"label": "EOCs", "value": "2 (Otterbourne, Bicester)"},
            {"label": "FT authorised", "value": "2012"},
            {"label": "Most recent CQC rating", "value": "Requires Improvement"},
            {"label": "Lead procurement framework", "value": "NHS Supply Chain"}
        ],
        "notes": "Delivery body: SCAS Procurement and Make Ready Centre teams; routine paramedic consumables flow via NHS Supply Chain Tower 5 (orthopaedic / consumables) and infection-prevention items via Tower 7; some specialist airway and IO devices direct from manufacturer. Policy owner: NHSE Provider Finance for envelope; DHSC for GAM; ICBs across the four counties as commissioners (Frimley, Buckinghamshire-Oxfordshire-Berkshire West, Hampshire and Isle of Wight). Funding trajectory: rising — Cat-1/Cat-2 demand has risen sharply post-pandemic, single-use IPC consumables remain elevated relative to pre-2020, and inflation passthrough on medical consumables persists. Evaluation: CQC Requires Improvement (2024 inspection raised culture and patient safety concerns); NHSE Ambulance Quality Indicators; ORH demand-and-capacity benchmarks. Predecessor: SCAS formed 2006 from Hampshire, Oxfordshire, Berkshire and Buckinghamshire ambulance services; successor: ongoing improvement plan and Make Ready estate consolidation.",
        "sources": [
            {"publisher": "South Central Ambulance Service NHS FT", "title": "Annual Report and Accounts 2023-24", "url": "https://www.scas.nhs.uk/about/our-publications/"},
            {"publisher": "NHS Supply Chain", "title": "About the NHS Supply Chain operating model", "url": "https://www.supplychain.nhs.uk/about-us/"},
            {"publisher": "NHS England", "title": "Ambulance Quality Indicators", "url": "https://www.england.nhs.uk/statistics/statistical-work-areas/ambulance-quality-indicators/"},
            {"publisher": "Care Quality Commission", "title": "South Central Ambulance Service NHSFT inspection reports", "url": "https://www.cqc.org.uk/provider/RYE"},
            {"publisher": "DHSC", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"}
        ],
        "related": ["Clinical Supplies & Drugs — South Central Ambulance Service NHS Foundation Trust", "South Central Ambulance Service NHS Foundation Trust", "NHS Supply Chain", "NHSE Ambulance Quality Indicators", "Lord Carter NHS Ambulance Review"]
    },
    "Business rates — North West Ambulance Service NHS Trust": {
        "aliases": [{"name": "Business rates", "parent": "North West Ambulance Service NHS Trust"}],
        "description": "Non-domestic rates levied on the NWAS estate — ~110 ambulance stations and standby points across Cumbria, Lancashire, Greater Manchester, Cheshire and Merseyside, four EOCs (Liverpool, Manchester, Preston, Carlisle), and regional fleet workshops and Make Ready Centres. The £2.11M reflects the 2023 list rateable values applied at the standard multiplier; NWAS covers one of the geographically largest ambulance footprints with mixed urban (Liverpool, Manchester) and very rural (Cumbria, Pennines) hereditaments.",
        "beneficiaries": "~7,000 WTE serving ~7.4M residents of the North West of England via ~1.3M emergency incidents and ~2.0M NHS 111 calls per year.",
        "legal_basis": "Local Government Finance Act 1988 (Schedule 6) · Non-Domestic Rating Act 2023 · Non-Domestic Rating (Multipliers and Private Finance) Act 2024 · NHS Act 2006 · 2023 Rating List (VOA)",
        "key_stats": [
            {"label": "Business rates 2023-24", "value": "£2.11M"},
            {"label": "Parent line", "value": "Premises & Infrastructure"},
            {"label": "Trust category", "value": "NHS Ambulance"},
            {"label": "Catchment population", "value": "~7.4M (North West England)"},
            {"label": "Ambulance stations + standby", "value": "~110"},
            {"label": "EOCs", "value": "4 (Liverpool, Manchester, Preston, Carlisle)"},
            {"label": "WTE staff", "value": "~7,000"},
            {"label": "999 incidents / year", "value": "~1.3M"},
            {"label": "NHS 111 calls / year", "value": "~2.0M"},
            {"label": "Trust formed", "value": "2006 (from Cumbria, Lancs, GM, Mersey ambulance services)"},
            {"label": "Most recent CQC rating", "value": "Good (2023)"},
            {"label": "Geography", "value": "Mixed urban + extensive rural (Cumbria, Pennines)"}
        ],
        "notes": "Delivery body: NWAS Estates and Facilities; rating advice typically procured via NHS framework; billing authorities are the 30+ districts and unitaries across the patch from Carlisle to Crewe. Policy owner: DLUHC/MHCLG for the rating system and multiplier; VOA for valuations; Treasury for the 2024 multipliers reform; NHSE Provider Finance for the funding envelope. Funding trajectory: stepped up at the 2023 revaluation; the 2024 Act introduced lower multipliers for retail-hospitality-leisure but NHS hereditaments remain on the standard multiplier (51.2p in 2024-25), so NWAS sees only multiplier inflation. Evaluation: CQC Good (2023, return from Requires Improvement); NHSE Ambulance Quality Indicators; ORH demand-and-capacity benchmarks. Predecessor: NWAS formed 2006 from merger of Cumbria, Lancashire, Greater Manchester and Mersey ambulance services; successor: estate consolidation including new Make Ready Centres and Cumbria EOC integration.",
        "sources": [
            {"publisher": "North West Ambulance Service NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.nwas.nhs.uk/about-us/annual-report-and-accounts/"},
            {"publisher": "Valuation Office Agency", "title": "2023 Rating List", "url": "https://www.gov.uk/government/collections/business-rates-2023-revaluation"},
            {"publisher": "UK Government", "title": "Non-Domestic Rating (Multipliers and Private Finance) Act 2024", "url": "https://www.legislation.gov.uk/ukpga/2024/15/contents"},
            {"publisher": "Care Quality Commission", "title": "North West Ambulance Service NHS Trust inspection reports", "url": "https://www.cqc.org.uk/provider/RX7"},
            {"publisher": "NHS England", "title": "Ambulance Quality Indicators", "url": "https://www.england.nhs.uk/statistics/statistical-work-areas/ambulance-quality-indicators/"}
        ],
        "related": ["Premises & Infrastructure — North West Ambulance Service NHS Trust", "North West Ambulance Service NHS Trust", "Valuation Office Agency", "Non-Domestic Rating Act 2023", "NHSE Ambulance Quality Indicators"]
    },
    "Establishment costs — The Robert Jones and Agnes Hunt Orthopaedic Hospital NHS Foundation Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "The Robert Jones and Agnes Hunt Orthopaedic Hospital NHS Foundation Trust"}],
        "description": "Establishment costs at RJAH — telephony, postage, office supplies, advertising, training, audit and bank charges, courier and indirect non-payroll non-clinical overhead at the elective orthopaedic specialist trust at Gobowen, Oswestry. The £2.09M overhead is small relative to large DGH peers but high per-bed because the trust is a single supra-regional site running specialist services to a 1.5M catchment across Shropshire, mid-Wales, Cheshire and Powys. Listed-building constraints on parts of the historic 1900-origin estate and rural-mileage telephony/postage costs add to the structural overhead.",
        "beneficiaries": "~1,400 WTE serving a supra-regional catchment of ~1.5M with ~7,000 inpatient/day-case episodes and ~70,000 outpatient attendances per year; runs the Midlands Centre for Spinal Injuries.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Establishment costs 2023-24", "value": "£2.09M"},
            {"label": "Parent line", "value": "Premises & Infrastructure"},
            {"label": "Trust category", "value": "NHS Specialist (orthopaedic)"},
            {"label": "Site", "value": "Gobowen, Oswestry (1900 sanatorium origin)"},
            {"label": "Listed buildings", "value": "Several Grade II elements on heritage campus"},
            {"label": "Inpatient / day-case episodes", "value": "~7,000"},
            {"label": "Outpatient attendances", "value": "~70,000"},
            {"label": "Catchment population", "value": "~1.5M (supra-regional)"},
            {"label": "WTE staff", "value": "~1,400"},
            {"label": "ICS", "value": "Shropshire, Telford and Wrekin ICB (host)"},
            {"label": "Foundation Trust authorised", "value": "2011"},
            {"label": "Surgical Hub designation", "value": "Yes (NHSE Elective Reform Plan 2025)"}
        ],
        "notes": "Delivery body: RJAH Estates and Facilities, Procurement and IT; corporate services partly delivered via NHS SBS frameworks. Policy owner: NHSE Provider Finance for envelope; NHSE Specialised Commissioning sets contract for spinal injuries; DHSC for GAM; Shropshire, Telford and Wrekin ICB hosts. Funding trajectory: small absolute line, broadly flat in real terms; rural overhead (mileage, postage) and IT modernisation push modest growth; CHKS/elective recovery activity growth nudges throughput-linked overhead. Evaluation: CQC Good; NHSE elective recovery dashboard; National Joint Registry; ORH benchmarks. Predecessor: trust origins as 1900 open-air sanatorium under Agnes Hunt; FT authorised 2011; successor: Surgical Hub designation under 2024-25 Elective Reform Plan and Headley Court Veterans' Orthopaedic centre (opened 2018).",
        "sources": [
            {"publisher": "RJAH Orthopaedic NHS FT", "title": "Annual Report and Accounts 2023-24", "url": "https://www.rjah.nhs.uk/About-Us/Annual-Reports.aspx"},
            {"publisher": "NHS England", "title": "Elective Reform Plan (2025) and Surgical Hubs", "url": "https://www.england.nhs.uk/long-read/reforming-elective-care-for-patients/"},
            {"publisher": "Care Quality Commission", "title": "RJAH Orthopaedic NHSFT inspection reports", "url": "https://www.cqc.org.uk/provider/RL1"},
            {"publisher": "DHSC", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "National Joint Registry", "title": "21st Annual Report 2024", "url": "https://www.njrcentre.org.uk/njr-annual-reports/"}
        ],
        "related": ["Premises & Infrastructure — The Robert Jones and Agnes Hunt Orthopaedic Hospital NHS Foundation Trust", "The Robert Jones and Agnes Hunt Orthopaedic Hospital NHS Foundation Trust", "NHSE Specialised Commissioning", "NHS Elective Reform Plan 2025", "Shropshire, Telford and Wrekin ICB"]
    },
    "Establishment costs — Wirral Community Health and Care NHS Foundation Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "Wirral Community Health and Care NHS Foundation Trust"}],
        "description": "Establishment costs at Wirral Community Health and Care NHS Foundation Trust (WCHC) — telephony, postage, office supplies, advertising, training, audit and bank charges, and indirect non-payroll non-clinical overhead at this community-only FT covering the Wirral peninsula. The £2.04M reflects the cost of running a multi-site community trust spanning ~325,000 residents across Birkenhead, Wallasey, Bebington and rural Wirral, with district nursing, health visiting, school nursing, MSK and 0-19 services delivered out of clinics and patients' homes.",
        "beneficiaries": "~1,400 WTE serving the ~325,000 residents of Wirral via ~900,000 community contacts including district nursing, health visiting, school nursing, MSK and 0-19 services.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Establishment costs 2023-24", "value": "£2.04M"},
            {"label": "Parent line", "value": "Premises & Infrastructure"},
            {"label": "Trust category", "value": "NHS Community"},
            {"label": "Catchment population", "value": "~325,000 (Wirral)"},
            {"label": "WTE staff", "value": "~1,400"},
            {"label": "Annual contacts", "value": "~900,000"},
            {"label": "Community sites", "value": "~30 clinics + base stations"},
            {"label": "ICS", "value": "Cheshire and Merseyside ICB"},
            {"label": "Estate landlord", "value": "Mostly NHS Property Services"},
            {"label": "FT authorised", "value": "2017 (FT) from 2011 trust"},
            {"label": "Most recent CQC rating", "value": "Good"},
            {"label": "0-19 universal services", "value": "Lead provider on Wirral"}
        ],
        "notes": "Delivery body: WCHC Estates and Facilities, IT and Corporate Services; some corporate services delivered via NHS SBS for finance / payroll and through Cheshire and Merseyside shared corporate arrangements. Policy owner: NHSE Provider Finance for envelope; Cheshire and Merseyside ICB as block-contract lead; DHSC for GAM. Funding trajectory: small absolute line, broadly flat-to-modestly-rising; telephony refresh and IT investment in EPR and mobile-working solutions for district-nursing teams nudge growth; Three Shifts (Darzi Sep 2024) virtual-ward expansion adds modest overhead. Evaluation: CQC Good (2022 most recent comprehensive); NHSE Operational Plan returns; ICB community dashboards. Predecessor: WCHC formed 2011 from Wirral PCT, awarded FT status 2017; successor: Wirral Place-based Partnership integration with Wirral University Teaching Hospital, Wirral CDC development.",
        "sources": [
            {"publisher": "Wirral Community Health and Care NHS FT", "title": "Annual Report and Accounts 2023-24", "url": "https://www.wchc.nhs.uk/about-us/publications/annual-reports/"},
            {"publisher": "Care Quality Commission", "title": "Wirral Community Health and Care NHSFT inspection reports", "url": "https://www.cqc.org.uk/provider/RY7"},
            {"publisher": "DHSC", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Lord Darzi", "title": "Independent Investigation of the NHS in England (Sep 2024)", "url": "https://www.gov.uk/government/publications/independent-investigation-of-the-nhs-in-england"},
            {"publisher": "Cheshire and Merseyside ICB", "title": "Joint Forward Plan 2023-28", "url": "https://www.cheshireandmerseyside.nhs.uk/"}
        ],
        "related": ["Premises & Infrastructure — Wirral Community Health and Care NHS Foundation Trust", "Wirral Community Health and Care NHS Foundation Trust", "Cheshire and Merseyside ICB", "NHS Property Services", "Lord Darzi Independent Investigation 2024"]
    },
    "Transport (business + patient) — Leeds Community Healthcare NHS Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "Leeds Community Healthcare NHS Trust"}],
        "description": "Business and patient transport at Leeds Community Healthcare NHS Trust (LCH) — primarily AMAP mileage reimbursement for the trust's district nursing, neighbourhood-team, MSK community-physio, dental, podiatry and 0-19 staff driving across the City of Leeds, plus pool-fleet leases (IFRS 16 right-of-use assets) and small patient-transport budgets. The £2.04M reflects miles driven across one of England's largest single-city footprints (552 km²), where rural-fringe outer Leeds (Otley, Wetherby, Garforth) sits alongside dense inner-city neighbourhoods.",
        "beneficiaries": "~3,000 WTE serving the ~825,000 residents of the City of Leeds via ~1.7M community contacts across district nursing, neighbourhood teams, MSK, dental, 0-19 and end-of-life services.",
        "legal_basis": "NHS Act 2006 · NHSE Patient Transport Services eligibility criteria · Agenda for Change s.17 mileage rates plus HMRC AMAP · IFRS 16 Leases (pool fleet) · Health and Care Act 2022",
        "key_stats": [
            {"label": "Transport (business + patient) 2023-24", "value": "£2.04M"},
            {"label": "Parent line", "value": "Premises & Infrastructure"},
            {"label": "Trust category", "value": "NHS Community"},
            {"label": "Catchment population", "value": "~825,000 (City of Leeds)"},
            {"label": "WTE staff", "value": "~3,000"},
            {"label": "Annual contacts", "value": "~1.7M"},
            {"label": "Geography", "value": "552 km² — largest English city footprint"},
            {"label": "ICS", "value": "West Yorkshire ICB (Leeds Place)"},
            {"label": "Estate landlord", "value": "Mostly NHS Property Services"},
            {"label": "AMAP rate", "value": "45p/mile first 10k (HMRC)"},
            {"label": "Trust authorised", "value": "2011"},
            {"label": "Most recent CQC rating", "value": "Outstanding"}
        ],
        "notes": "Delivery body: LCH Fleet, Estates and Workforce teams; pool-vehicle leases through NHS Fleet Solutions and SBS frameworks; patient transfers brokered with Yorkshire Ambulance Service for non-emergency journeys. Policy owner: NHSE Provider Finance for envelope; West Yorkshire ICB and Leeds Place-based Partnership as commissioners; DHSC GAM 2024-25 for accounting; HMRC AMAP rate for mileage reimbursement. Funding trajectory: rising — fuel inflation, IFRS 16 right-of-use recognition (2022 step-up), and Three Shifts (Darzi Sep 2024) virtual-ward and home-based care expansion drive miles travelled. Evaluation: CQC Outstanding (2018, retained); NHSE Operational Plan returns; Leeds Health and Care Partnership performance reports. Predecessor: LCH established 2011 from Leeds PCT community services; successor: NHS Net Zero by 2040 driving EV pilot; deepening Place-based integration with Leeds Teaching Hospitals NHS Trust and Leeds and York Partnership FT.",
        "sources": [
            {"publisher": "Leeds Community Healthcare NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.leedscommunityhealthcare.nhs.uk/about-us/publications/annual-report-and-accounts/"},
            {"publisher": "NHS England", "title": "Non-Emergency Patient Transport Services eligibility criteria (2022)", "url": "https://www.england.nhs.uk/publication/non-emergency-patient-transport-services-eligibility-criteria/"},
            {"publisher": "HMRC", "title": "Approved Mileage Allowance Payments (AMAP) rates", "url": "https://www.gov.uk/government/publications/rates-and-allowances-travel-mileage-and-fuel-allowances"},
            {"publisher": "Care Quality Commission", "title": "Leeds Community Healthcare NHS Trust inspection reports", "url": "https://www.cqc.org.uk/provider/RY2"},
            {"publisher": "Lord Darzi", "title": "Independent Investigation of the NHS in England (Sep 2024)", "url": "https://www.gov.uk/government/publications/independent-investigation-of-the-nhs-in-england"},
            {"publisher": "NHS England", "title": "Delivering a net zero NHS", "url": "https://www.england.nhs.uk/greenernhs/a-net-zero-nhs/"}
        ],
        "related": ["Premises & Infrastructure — Leeds Community Healthcare NHS Trust", "Leeds Community Healthcare NHS Trust", "West Yorkshire ICB", "NHS Net Zero by 2040", "Lord Darzi Independent Investigation 2024"]
    },
    "Amortisation — Herefordshire and Worcestershire Health and Care NHS Trust": {
        "aliases": [{"name": "Amortisation", "parent": "Herefordshire and Worcestershire Health and Care NHS Trust"}],
        "description": "Amortisation of intangible assets at Herefordshire and Worcestershire Health and Care NHS Trust (HWHCT) — chiefly the EPR / patient record system (SystmOne / TPP), software licences, and capitalised intangible development costs across the trust's mental health, learning disability and community services. The £1.98M is recognised straight-line under IAS 38 over assessed useful economic lives and reflects ongoing digital investment as the trust modernises under the NHSE Frontline Digitisation programme.",
        "beneficiaries": "~3,500 WTE serving ~780,000 residents of Herefordshire and Worcestershire via combined community + mental health pathways with ~1.4M annual contacts.",
        "legal_basis": "IAS 38 Intangible Assets · DHSC Group Accounting Manual 2024-25 ch.5 · NHS Act 2006 · NHSE Frontline Digitisation programme · NHSE What Good Looks Like",
        "key_stats": [
            {"label": "Amortisation 2023-24", "value": "£1.98M"},
            {"label": "Parent line", "value": "Premises & Infrastructure"},
            {"label": "Trust category", "value": "NHS Community + Mental Health"},
            {"label": "Catchment population", "value": "~780,000 (Herefordshire + Worcestershire)"},
            {"label": "WTE staff", "value": "~3,500"},
            {"label": "Annual contacts", "value": "~1.4M"},
            {"label": "ICS", "value": "Herefordshire and Worcestershire ICB"},
            {"label": "Trust formed", "value": "2020 (merger of 2gether and Worcs Health and Care)"},
            {"label": "EPR vendor", "value": "SystmOne (TPP)"},
            {"label": "Digital programme", "value": "NHSE Frontline Digitisation"},
            {"label": "Most recent CQC rating", "value": "Good"},
            {"label": "Useful economic life (software)", "value": "Typically 3-5 years"}
        ],
        "notes": "Delivery body: HWHCT Digital and Finance teams capitalise software development and licences in line with IAS 38 and the DHSC GAM ch.5; vendor relationships include TPP (SystmOne) for EPR and a tail of mental-health-specific software (RIO competitors, prescribing systems). Policy owner: NHSE Frontline Digitisation programme sets capital direction and the What Good Looks Like framework; DHSC for GAM treatment; ICB for digital strategy alignment. Funding trajectory: rising — Frontline Digitisation funding from 2021-22 onwards put new EPR / EPMA assets on the balance sheet, lifting subsequent amortisation; April 2025 NHSE digital strategy refresh continues this. Evaluation: CQC Good (2022 most recent comprehensive); NHSE Frontline Digitisation maturity assessments; What Good Looks Like score. Predecessor: HWHCT formed 2020 from merger of 2gether NHS Foundation Trust (Glos+Hereford) and Worcestershire Health and Care NHS Trust; successor: ongoing EPR convergence and integration with primary care.",
        "sources": [
            {"publisher": "Herefordshire and Worcestershire Health and Care NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.hacw.nhs.uk/about-us/publications/annual-reports/"},
            {"publisher": "DHSC", "title": "Group Accounting Manual 2024-25 (ch.5 Intangibles)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/frontline-digitisation/"},
            {"publisher": "Care Quality Commission", "title": "Herefordshire and Worcestershire Health and Care NHS Trust inspection reports", "url": "https://www.cqc.org.uk/provider/RWP"},
            {"publisher": "NHS England", "title": "What Good Looks Like framework", "url": "https://transform.england.nhs.uk/digitise-connect-transform/what-good-looks-like/"}
        ],
        "related": ["Premises & Infrastructure — Herefordshire and Worcestershire Health and Care NHS Trust", "Herefordshire and Worcestershire Health and Care NHS Trust", "Herefordshire and Worcestershire ICB", "NHSE Frontline Digitisation", "IAS 38 Intangible Assets"]
    },
    "Amortisation — East of England Ambulance Service NHS Trust": {
        "aliases": [{"name": "Amortisation", "parent": "East of England Ambulance Service NHS Trust"}],
        "description": "Amortisation of intangible assets at East of England Ambulance Service NHS Trust (EEAST) — chiefly Computer Aided Dispatch (CAD) software, Electronic Patient Care Records (ePCR), telephony platforms (NHS 111 and 999 systems), software licences and capitalised in-house development. The £1.98M is recognised straight-line under IAS 38 over assessed useful economic lives. EEAST covers the six East of England counties — Cambridgeshire, Norfolk, Suffolk, Essex, Bedfordshire and Hertfordshire — and has invested heavily in dispatch and clinical-decision-support software since the 2018-22 improvement programme.",
        "beneficiaries": "~5,500 WTE serving ~6.3M residents of the East of England via ~1.05M emergency incidents per year and three EOCs (Bedford, Norwich, Chelmsford).",
        "legal_basis": "IAS 38 Intangible Assets · DHSC Group Accounting Manual 2024-25 ch.5 · NHS Act 2006 · NHSE Frontline Digitisation programme · NHSE What Good Looks Like",
        "key_stats": [
            {"label": "Amortisation 2023-24", "value": "£1.98M"},
            {"label": "Parent line", "value": "Premises & Infrastructure"},
            {"label": "Trust category", "value": "NHS Ambulance"},
            {"label": "Catchment population", "value": "~6.3M (East of England)"},
            {"label": "Counties", "value": "Cambs, Norfolk, Suffolk, Essex, Beds, Herts"},
            {"label": "WTE staff", "value": "~5,500"},
            {"label": "Emergency incidents / year", "value": "~1.05M"},
            {"label": "EOCs", "value": "3 (Bedford, Norwich, Chelmsford)"},
            {"label": "CAD platform", "value": "MIS Cleric / Frequentis (sector standard)"},
            {"label": "Trust formed", "value": "2006 (merger of Beds-Herts, Essex, East Anglian ambulance)"},
            {"label": "Most recent CQC rating", "value": "Requires Improvement"},
            {"label": "Useful economic life (software)", "value": "Typically 3-5 years"}
        ],
        "notes": "Delivery body: EEAST Digital and Finance teams capitalise software and in-house development under IAS 38 and DHSC GAM ch.5; vendor relationships include CAD/EOC platform suppliers, Frequentis-style telephony, and ePCR vendors. Policy owner: NHSE Frontline Digitisation programme; DHSC for GAM treatment; NHSE Provider Finance for capital envelope; the six East of England ICBs as commissioners. Funding trajectory: rising — post-2018 turnaround investment in CAD modernisation, NHS 111 platform integration, and ePCR refresh placed new intangibles on the balance sheet that now amortise; the IFRS 16-style capital ratchet plus inflation-linked software refresh continue to push amortisation. Evaluation: CQC Requires Improvement (most recent inspection); NHSE Ambulance Quality Indicators; ORH demand-and-capacity benchmarks; trust ARA. Predecessor: EEAST formed 2006 from merger of Bedfordshire-Hertfordshire, Essex and East Anglian ambulance services; successor: ongoing improvement plan and digital convergence with NHS 111 and clinical-decision-support tools.",
        "sources": [
            {"publisher": "East of England Ambulance Service NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.eastamb.nhs.uk/about-us/our-publications/annual-report-and-accounts.htm"},
            {"publisher": "DHSC", "title": "Group Accounting Manual 2024-25 (ch.5 Intangibles)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/frontline-digitisation/"},
            {"publisher": "NHS England", "title": "Ambulance Quality Indicators", "url": "https://www.england.nhs.uk/statistics/statistical-work-areas/ambulance-quality-indicators/"},
            {"publisher": "Care Quality Commission", "title": "East of England Ambulance Service NHS Trust inspection reports", "url": "https://www.cqc.org.uk/provider/RYC"}
        ],
        "related": ["Premises & Infrastructure — East of England Ambulance Service NHS Trust", "East of England Ambulance Service NHS Trust", "NHSE Frontline Digitisation", "IAS 38 Intangible Assets", "NHSE Ambulance Quality Indicators"]
    },
}
