# -*- coding: utf-8 -*-
# Phase 2 SCamb — chunk 16 (17 NHS Specialist/Community/Ambulance Trust orphan sub-lines)
# Hand-curated trust-specific PROGRAMME-archetype enrichment entries.
# Structural contract per docs/archetype_briefs.md.

NEW = {
    "General supplies & services — Bridgewater Community Healthcare NHS Foundation Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "Bridgewater Community Healthcare NHS Foundation Trust"}],
        "description": "Bridgewater's £0.44M general supplies & services orphan covers non-clinical consumables and small-ticket community-care equipment used by district nursing, health visiting, school nursing, MSK community physiotherapy and end-of-life teams across Halton, St Helens and Warrington — items such as continence products bought outside the FP10 stoma/continence pathway, dressings and minor medical sundries, point-of-care testing strips, single-use diagnostic kit, infection-prevention PPE, and stationery/printing for community caseload paperwork. The line sits below the formal NHS Supply Chain catalogue spend and reflects the long tail of low-value consumables district nurses carry into patients' homes.",
        "beneficiaries": "Serves c. 360,000 residents of Halton, St Helens and Warrington (and pockets of Wigan and Bolton via specialist services); delivers c. 850,000 community contacts/yr through a c. 1,800 WTE workforce of district nurses, health visitors, school nurses, AHPs and MSK community physios operating from c. 60 health centres, clinics and Sure Start sites.",
        "legal_basis": "NHS Act 2006 · Health and Care Act 2022 · DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 2 Inventories (interaction with consumables held) · NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "General supplies & services 2024-25", "value": "£0.44M"},
            {"label": "Footprint", "value": "Halton, St Helens, Warrington (+ specialist services into Wigan/Bolton)"},
            {"label": "Population served", "value": "c. 360,000 residents across the core boroughs"},
            {"label": "Annual activity", "value": "c. 850,000 community contacts/yr (district nursing + HVs + school nursing + MSK)"},
            {"label": "Workforce", "value": "c. 1,800 WTE — district nurses, health visitors, school nurses, AHPs, MSK community physios"},
            {"label": "Estate", "value": "c. 60 community health centres, clinics, Sure Start hubs (mostly NHSPS-leased)"},
            {"label": "Spend mix", "value": "Continence products, dressings/sundries, POCT strips, diagnostic single-use kit, IPC PPE, printing — long tail below NHS Supply Chain catalogue spend"},
            {"label": "Delivery body", "value": "Bridgewater Procurement + NHS Supply Chain Hub (NWC) + local catalogue suppliers"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Cheshire & Merseyside ICB (lead commissioner) + NHS Supply Chain"},
            {"label": "Funding trajectory", "value": "Broadly flat in cash terms; April 2025 employer-NIC step-up indirect (via supplier overhead recovery); Three Shifts (Darzi Sep 2024) may grow community caseload + consumables footprint"},
            {"label": "Evaluation evidence", "value": "Bridgewater ARA; CQC provider profile (RY2 — rated Good); NHSE ERIC 2023-24; Model Hospital procurement benchmarks"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2011 PCT / NHS Trust legacy contracts · Successor: NHS Supply Chain Future Operating Model + Three Shifts community uplift"}
        ],
        "notes": "Community trusts run a fundamentally different consumables mix from acute hospitals: nurses carry stock into patients' homes rather than draw from ward Pyxis cabinets, so the long-tail of low-value supplies (continence pads, dressings, POCT strips, PPE, printing for paper caseload notes) sits in 'general supplies' rather than the formal Supply Chain clinical line. Bridgewater's £0.44M is small but persistent and tracks workforce headcount and visit volume more than estate. Drivers include the post-pandemic IPC PPE baseline reset, FP10-stoma vs trust-supply boundary disputes, and the Darzi Three Shifts (Sep 2024) push to move more activity into community settings, which over time grows visit volume and consumables draw. April 2025 employer-NIC step-up flows through indirectly via supplier overhead.",
        "sources": [
            {"publisher": "Bridgewater Community Healthcare NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.bridgewater.nhs.uk/about-us/publications/annual-reports/"},
            {"publisher": "Care Quality Commission", "title": "Bridgewater Community Healthcare NHS Foundation Trust provider profile (RY2)", "url": "https://www.cqc.org.uk/provider/RY2"},
            {"publisher": "NHS Supply Chain", "title": "Future Operating Model and category towers", "url": "https://www.supplychain.nhs.uk/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Lord Darzi / DHSC", "title": "Independent investigation of the NHS in England (Darzi Report, Sep 2024)", "url": "https://www.gov.uk/government/publications/independent-investigation-of-the-nhs-in-england"},
            {"publisher": "NHS England", "title": "Estates Returns Information Collection (ERIC) 2023-24", "url": "https://digital.nhs.uk/data-and-information/publications/statistical/estates-returns-information-collection"}
        ],
        "related": ["Bridgewater Community Healthcare NHS Foundation Trust", "Clinical Supplies & Drugs", "NHS Community Trusts", "General supplies & services — Hertfordshire Community NHS Trust", "General supplies & services — Solent NHS Trust", "NHS Supply Chain"]
    },
    "Lease expenditure — Liverpool Women's NHS Foundation Trust": {
        "aliases": [{"name": "Lease expenditure", "parent": "Liverpool Women's NHS Foundation Trust"}],
        "description": "Liverpool Women's £0.43M lease line covers IFRS 16 right-of-use leases for non-headquarters premises — primarily small satellite consulting and outpatient clinic space in community settings, gynaecology outreach clinics, neonatal transport vehicle leases under the Cheshire & Merseyside neonatal transport network, and pool fleet for staff travel between the Crown Street main hospital and Aintree-area outreach. From the 2022-23 IFRS 16 transition, leases longer than 12 months and above the de-minimis threshold sit on balance sheet as right-of-use assets with a lease-liability and an associated finance/interest split.",
        "beneficiaries": "England's only standalone women's hospital alongside Birmingham Women's; serves a c. 1.5M Cheshire & Merseyside catchment for tertiary-level obstetrics and gynaecology with c. 8,200 deliveries/yr, the Hewitt Fertility Centre and a Level-3 NICU; c. 1,500 WTE on Crown Street main site + outreach.",
        "legal_basis": "IFRS 16 Leases · DHSC Group Accounting Manual 2024-25 ch.7 · Landlord and Tenant Act 1954 · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Lease expenditure 2024-25", "value": "£0.43M"},
            {"label": "Specialty footprint", "value": "Standalone tertiary women's & neonatal hospital (Crown Street, Liverpool L8) — only one of two in England (Birmingham Women's the other)"},
            {"label": "Catchment", "value": "c. 1.5M Cheshire & Merseyside; tertiary obstetric + Level-3 NICU + gynae-oncology + fertility (Hewitt Fertility Centre)"},
            {"label": "Annual activity", "value": "c. 8,200 deliveries/yr; c. 1,000 NICU admissions/yr; c. 50,000 outpatient attendances; Hewitt Fertility c. 4,000 cycles/yr"},
            {"label": "Workforce", "value": "c. 1,500 WTE; c. 230 medical + c. 700 nursing/midwifery"},
            {"label": "Lease composition", "value": "Outreach gynae clinic space + neonatal transport vehicle leases (CMNTS) + pool-fleet vehicles + small office space"},
            {"label": "IFRS 16 driver", "value": "April 2022 transition recognised right-of-use assets and lease liabilities on balance sheet; pre-2022 these were operating-lease P&L charges"},
            {"label": "Future capital", "value": "New Liverpool Women's hospital business case (relocation/co-location with Royal Liverpool) repeatedly deferred — current Crown Street estate retained"},
            {"label": "Delivery body", "value": "LWH Estates & Facilities + NHS Property Services for community clinic space + commercial fleet leasing"},
            {"label": "Policy owner", "value": "NHSE Specialised Commissioning (Level-3 NICU + gynae-oncology) + Cheshire & Merseyside ICB + DHSC"},
            {"label": "Funding trajectory", "value": "Stable around £0.4-0.5M; IFRS 16 2022 step-up; future relocation business case could materially restructure the line"},
            {"label": "Evaluation evidence", "value": "LWH ARA; CQC provider profile (REP); NHSE perinatal mortality reviews; HFEA Hewitt Fertility benchmarks"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-IFRS-16 operating-lease P&L treatment · Successor: long-term Liverpool Women's relocation/co-location strategic outline case"}
        ],
        "notes": "Liverpool Women's is one of only two standalone women's hospitals in England (Birmingham Women's the other) and a tertiary referral centre for Cheshire & Merseyside. Its lease line is small in absolute terms because the trust is single-site and owns the Crown Street estate, so leases are concentrated in outreach clinics, neonatal-transport vehicles for the Cheshire & Merseyside Neonatal Transport Service and pool-car fleet. Drivers include the IFRS 16 April 2022 balance-sheet jump, the Landlord and Tenant Act 1954 renewal cycle on satellite clinic space, and continued political uncertainty around the long-rumoured relocation/co-location with Royal Liverpool — repeatedly deferred but still in NHSE's strategic capital pipeline.",
        "sources": [
            {"publisher": "Liverpool Women's NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.liverpoolwomens.nhs.uk/about-us/publications/"},
            {"publisher": "Care Quality Commission", "title": "Liverpool Women's NHS Foundation Trust provider profile (REP)", "url": "https://www.cqc.org.uk/provider/REP"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (ch.7 leases)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "IFRS Foundation", "title": "IFRS 16 Leases", "url": "https://www.ifrs.org/issued-standards/list-of-standards/ifrs-16-leases/"},
            {"publisher": "NHS England", "title": "Specialised commissioning — neonatal critical care service specification", "url": "https://www.england.nhs.uk/commissioning/spec-services/"},
            {"publisher": "Human Fertilisation and Embryology Authority", "title": "Hewitt Fertility Centre clinic profile", "url": "https://www.hfea.gov.uk/choose-a-clinic/"}
        ],
        "related": ["Liverpool Women's NHS Foundation Trust", "Premises & Infrastructure", "NHS Specialist Trusts", "Lease expenditure — Central London Community Healthcare NHS Trust", "Lease expenditure — The Royal Orthopaedic Hospital NHS Foundation Trust", "NHS Property Services"]
    },
    "Amortisation — Gloucestershire Health and Care NHS Foundation Trust": {
        "aliases": [{"name": "Amortisation", "parent": "Gloucestershire Health and Care NHS Foundation Trust"}],
        "description": "GHC's £0.40M amortisation charge represents the systematic write-down of intangible assets — predominantly software licences and capitalised software development under IAS 38, including the Trust's electronic patient record (Rio / SystmOne community), mental health service software, the digital community-caseload platform, and capitalised development on the Gloucestershire ICS shared-care record. GHC is a combined community and mental health trust (formed 2019 by merging 2gether NHS Foundation Trust with Gloucestershire Care Services), so intangibles span both physical-health community digital tools and mental-health-specific systems.",
        "beneficiaries": "Serves a c. 670,000 Gloucestershire population delivering c. 1.6M community + mental health contacts/yr; operates from c. 70 sites including community hospitals at Cirencester, Stroud, Tewkesbury, Dilke (Forest of Dean), Lydney, North Cotswolds, Vale (Dursley), plus mental health inpatient units; c. 5,500 WTE.",
        "legal_basis": "IAS 38 Intangible Assets · DHSC Group Accounting Manual 2024-25 ch.5 · NHS Act 2006 · Health and Care Act 2022 · Mental Health Act 1983 (operational interaction)",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£0.40M"},
            {"label": "Trust profile", "value": "Combined community + mental health FT formed 2019 by merger of 2gether NHSFT + Gloucestershire Care Services"},
            {"label": "Footprint", "value": "Whole of Gloucestershire; c. 70 sites incl. community hospitals at Cirencester, Stroud, Tewkesbury, Dilke, Lydney, North Cotswolds, Vale + mental health inpatient units"},
            {"label": "Population served", "value": "c. 670,000 Gloucestershire residents"},
            {"label": "Annual activity", "value": "c. 1.6M community + mental health contacts/yr; community hospital inpatient bed-days; CAMHS, IAPT/Talking Therapies, learning disabilities, eating disorders"},
            {"label": "Workforce", "value": "c. 5,500 WTE — district nurses, AHPs, community physios, mental health nurses, psychiatrists, psychologists"},
            {"label": "Intangibles class", "value": "Software licences (Rio/SystmOne community, mental health EPR), capitalised software development for ICS shared-care record + digital caseload"},
            {"label": "Useful economic life", "value": "Software typically 3-7 years amortisation per DHSC GAM ch.5; clinical-system EPR straight-line over service life"},
            {"label": "Delivery body", "value": "GHC IT/Digital + Gloucestershire ICS digital programme + EPR vendor (TPP SystmOne / Servelec Rio)"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + One Gloucestershire ICB + NHSE Frontline Digitisation programme"},
            {"label": "Funding trajectory", "value": "Stable around £0.3-0.5M; modest growth as Frontline Digitisation capital flows through to capitalised software + ICS shared-care record"},
            {"label": "Evaluation evidence", "value": "GHC ARA; CQC provider profile (RTQ); NHSE digital maturity assessment; Mental Health Act monitoring"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2019 separate 2gether + GCS systems · Successor: One Gloucestershire shared-care record + Frontline Digitisation 2025-30 capital programme"}
        ],
        "notes": "GHC is one of England's combined community-and-mental-health trusts, formed by the 2019 merger of 2gether NHS Foundation Trust (mental health) with Gloucestershire Care Services (community), giving it an unusually broad intangibles footprint spanning two clinical-system stacks. Amortisation is small but steady at c. £0.4M and is dominated by software licences and capitalised development costs amortised on 3-7-year straight-line bases per DHSC GAM ch.5. Drivers include the NHSE Frontline Digitisation capital programme, the One Gloucestershire ICS shared-care-record build-out, and ongoing system rationalisation post-merger. The line will likely rise modestly as Frontline Digitisation capital matures into in-service intangibles.",
        "sources": [
            {"publisher": "Gloucestershire Health and Care NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.ghc.nhs.uk/about-us/publications/annual-reports/"},
            {"publisher": "Care Quality Commission", "title": "Gloucestershire Health and Care NHS Foundation Trust provider profile (RTQ)", "url": "https://www.cqc.org.uk/provider/RTQ"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (ch.5 intangibles)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "IFRS Foundation", "title": "IAS 38 Intangible Assets", "url": "https://www.ifrs.org/issued-standards/list-of-standards/ias-38-intangible-assets/"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://transform.england.nhs.uk/digitise-connect-transform/frontline-digitisation/"},
            {"publisher": "One Gloucestershire ICB", "title": "Integrated Care System publications", "url": "https://www.onegloucestershire.net/"}
        ],
        "related": ["Gloucestershire Health and Care NHS Foundation Trust", "Premises & Infrastructure", "NHS Community Trusts", "Amortisation — Central London Community Healthcare NHS Trust", "Amortisation — Sussex Community NHS Foundation Trust", "NHS England"]
    },
    "Drugs costs — Hounslow and Richmond Community Healthcare NHS Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "Hounslow and Richmond Community Healthcare NHS Trust"}],
        "description": "HRCH's £0.39M drugs costs orphan covers medicines used in community settings — vaccines for school-age immunisation programmes (HPV, MenACWY, Td/IPV) delivered by school-nursing teams, child-flu nasal spray, BCG for at-risk neonates, oral antibiotics and dressings/topicals dispensed by district nursing teams, end-of-life anticipatory medicines (just-in-case boxes), and small-volume PGD-supplied drugs in walk-in centres. Most prescribing is via FP10 in the community pharmacy network rather than trust drug spend, so the line is small relative to acute trusts.",
        "beneficiaries": "Serves c. 480,000 residents of the London boroughs of Hounslow and Richmond upon Thames; delivers c. 1.0M community contacts/yr including c. 80,000 child immunisations across the school-nursing programme; c. 1,000 WTE workforce including district nurses, health visitors, school nurses, and walk-in-centre clinicians at Teddington Memorial Hospital and the West Middlesex satellite.",
        "legal_basis": "NHS Act 2006 (Drug Tariff Part VIIIA) · Branded Medicines (Voluntary Scheme for Branded Medicines Pricing, Access and Growth — VPAG) · Human Medicines Regulations 2012 · Patient Group Directions (NICE MPG2) · DHSC GAM 2024-25 · UKHSA Green Book immunisation schedule",
        "key_stats": [
            {"label": "Drugs costs 2024-25", "value": "£0.39M"},
            {"label": "Footprint", "value": "London boroughs of Hounslow + Richmond upon Thames; main hub Teddington Memorial Hospital + West Middlesex satellite"},
            {"label": "Population served", "value": "c. 480,000 (Hounslow c. 290k + Richmond c. 200k)"},
            {"label": "Annual activity", "value": "c. 1.0M community contacts/yr; c. 80,000 school-age immunisations/yr; c. 50,000 health-visiting contacts; c. 200,000 district-nursing visits"},
            {"label": "Workforce", "value": "c. 1,000 WTE incl. district nurses, HVs, school nurses, walk-in-centre clinicians"},
            {"label": "Drug mix", "value": "School-age vaccines (HPV, MenACWY, Td/IPV, child-flu nasal spray, BCG), end-of-life JIC anticipatories, dressings/topicals, PGD walk-in stock"},
            {"label": "Procurement", "value": "Vaccines via UKHSA central immunisation supply (ImmForm); other drugs via NHS Supply Chain pharmacy + local LPP framework"},
            {"label": "Delivery body", "value": "HRCH Pharmacy + school-nursing teams + district-nursing teams + UKHSA central vaccine supply (ImmForm)"},
            {"label": "Policy owner", "value": "NHSE Public Health Commissioning (s.7A — childhood immunisations) + UKHSA + NW London ICB + DHSC"},
            {"label": "Funding trajectory", "value": "Modest rise post-pandemic catch-up of HPV/MenACWY in 12-13yo cohort; April 2025 employer-NIC step-up indirect via wholesaler overhead"},
            {"label": "Evaluation evidence", "value": "HRCH ARA; CQC provider profile (RY9 — Good); UKHSA cover survey for childhood immunisations; NHSE s.7A return"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2011 PCT immunisation contracts · Successor: NHSE 2025-26 s.7A immunisation refresh + HPV one-dose schedule (Sep 2023)"}
        ],
        "notes": "Community-trust drug spend is structurally small because most prescribing in the community is dispensed via FP10 in the high-street pharmacy network and reimbursed through the Drug Tariff Part VIII rather than the trust's own ledger. What does sit on HRCH's books is the trust-supplied stock for school-age immunisation programmes (mostly cost-neutral via UKHSA central supply through ImmForm), end-of-life 'just-in-case' anticipatory medicines for community palliative care, and PGD walk-in-centre stock at Teddington Memorial. Drivers include the HPV one-dose move (Sep 2023), pandemic-era cohort catch-up, and the standing NHSE s.7A childhood-immunisation contract.",
        "sources": [
            {"publisher": "Hounslow and Richmond Community Healthcare NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.hrch.nhs.uk/about-us/our-publications/"},
            {"publisher": "Care Quality Commission", "title": "Hounslow and Richmond Community Healthcare NHS Trust provider profile (RY9)", "url": "https://www.cqc.org.uk/provider/RY9"},
            {"publisher": "UK Health Security Agency", "title": "Immunisation against infectious disease (Green Book)", "url": "https://www.gov.uk/government/collections/immunisation-against-infectious-disease-the-green-book"},
            {"publisher": "NHS England", "title": "Section 7A public health functions agreement 2024-25", "url": "https://www.england.nhs.uk/commissioning/pub-hlth-res/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS Business Services Authority", "title": "Drug Tariff", "url": "https://www.nhsbsa.nhs.uk/pharmacies-gp-practices-and-appliance-contractors/drug-tariff"}
        ],
        "related": ["Hounslow and Richmond Community Healthcare NHS Trust", "Clinical Supplies & Drugs", "NHS Community Trusts", "Drugs costs — Norfolk Community Health and Care NHS Trust", "Drugs costs — Hertfordshire Community NHS Trust", "UK Health Security Agency"]
    },
    "Amortisation — The Royal Orthopaedic Hospital NHS Foundation Trust": {
        "aliases": [{"name": "Amortisation", "parent": "The Royal Orthopaedic Hospital NHS Foundation Trust"}],
        "description": "ROH Birmingham's £0.38M amortisation charge represents the systematic write-down of intangible assets — predominantly software licences and capitalised software development under IAS 38, including the orthopaedic-specialist EPR, theatre-scheduling and PACS imaging systems, joint-registry data feeds (NJR + bespoke trust register), and capitalised development for the high-throughput elective hub workflows. ROH is one of the largest single-site orthopaedic centres in Europe, focused on hip and knee arthroplasty, spinal surgery, oncology, paediatric and limb-reconstruction work.",
        "beneficiaries": "Tertiary supra-regional orthopaedic catchment across the West Midlands and beyond (c. 6M reference population) with c. 65,000 outpatient attendances/yr and c. 7,500 elective inpatient/day-case episodes including c. 2,500 hip/knee arthroplasties and c. 500 spinal cases/yr; c. 1,300 WTE on the Northfield (Bristol Road South, B31) main site.",
        "legal_basis": "IAS 38 Intangible Assets · DHSC Group Accounting Manual 2024-25 ch.5 · NHS Act 2006 · Health and Care Act 2022 · Frascati Manual research/development distinction",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£0.38M"},
            {"label": "Specialty footprint", "value": "Single-site tertiary orthopaedic FT — Bristol Road South, Northfield, Birmingham B31; one of largest standalone orthopaedic centres in Europe"},
            {"label": "Catchment", "value": "Supra-regional West Midlands + national referrals; c. 6M reference population for tertiary work"},
            {"label": "Annual activity", "value": "c. 65,000 outpatient attendances; c. 7,500 elective inpatient/day-case; c. 2,500 hip/knee arthroplasties; c. 500 spinal cases; oncology + paediatric"},
            {"label": "Workforce", "value": "c. 1,300 WTE; c. 110 medical + c. 400 nursing"},
            {"label": "Intangibles class", "value": "Software licences (orthopaedic EPR, theatre scheduling, PACS), joint-registry data feeds (NJR), capitalised software dev for elective hub"},
            {"label": "Useful economic life", "value": "Software typically 3-7 years amortisation per DHSC GAM ch.5"},
            {"label": "Elective hub status", "value": "Designated high-volume low-complexity (HVLC) elective hub under NHSE elective recovery — drives capitalised software for theatre scheduling + flow"},
            {"label": "Delivery body", "value": "ROH IT/Digital + EPR vendor + NJR data services + theatre-scheduling vendor"},
            {"label": "Policy owner", "value": "NHSE Specialised Commissioning (orthopaedic oncology + complex spinal) + DHSC + Birmingham & Solihull ICB + NHSE Elective Recovery"},
            {"label": "Funding trajectory", "value": "Stable around £0.4M; modest growth as Frontline Digitisation + elective hub IT capital flows through to in-service intangibles"},
            {"label": "Evaluation evidence", "value": "ROH ARA; CQC provider profile (RRJ); NJR annual report; GIRFT orthopaedic benchmarks; NHSE elective recovery returns"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-IFRS-16 era operating-lease software · Successor: NHSE Frontline Digitisation 2025-30 + elective hub expansion"}
        ],
        "notes": "ROH is one of England's standalone orthopaedic specialist trusts (alongside RNOH Stanmore and RJAH Oswestry) and a designated NHSE elective hub for hip/knee arthroplasty, where post-pandemic recovery has driven a step-up in theatre throughput. Amortisation is small in cash terms but reflects software-heavy intangibles tied to the EPR, theatre-scheduling and PACS estate, plus capitalised development for the elective-hub workflows. The line will rise modestly as Frontline Digitisation capital matures and the elective-hub investment programme is depreciated. The trust feeds the National Joint Registry (NJR) and uses GIRFT benchmarks heavily for outcome reporting.",
        "sources": [
            {"publisher": "The Royal Orthopaedic Hospital NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.roh.nhs.uk/about-us/publications"},
            {"publisher": "Care Quality Commission", "title": "The Royal Orthopaedic Hospital NHS Foundation Trust provider profile (RRJ)", "url": "https://www.cqc.org.uk/provider/RRJ"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (ch.5 intangibles)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "National Joint Registry", "title": "NJR Annual Report 2024", "url": "https://www.njrcentre.org.uk/njr-annual-report/"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://transform.england.nhs.uk/digitise-connect-transform/frontline-digitisation/"},
            {"publisher": "Getting It Right First Time (GIRFT)", "title": "Orthopaedic GIRFT national specialty report", "url": "https://www.gettingitrightfirsttime.co.uk/surgical-specialty/orthopaedic-surgery/"}
        ],
        "related": ["The Royal Orthopaedic Hospital NHS Foundation Trust", "Premises & Infrastructure", "NHS Specialist Trusts", "Amortisation — Sheffield Children's NHS Foundation Trust", "Amortisation — Alder Hey Children's NHS Foundation Trust", "NHS England"]
    },
    "Business rates — The Royal Orthopaedic Hospital NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "The Royal Orthopaedic Hospital NHS Foundation Trust"}],
        "description": "ROH Birmingham's £0.37M non-domestic-rates (NDR) bill is the business-rates payable to Birmingham City Council under the Local Government Finance Act 1988 on the Bristol Road South single-site campus at Northfield (B31), based on the Valuation Office Agency 2023 rating list and the standard multiplier. NHS bodies do not enjoy the 80% mandatory charity relief, so the line tracks rateable value × multiplier directly and is a non-discretionary annual cost pegged to the size of the elective-orthopaedic estate (including the on-site research/teaching wing and outpatient clinic block).",
        "beneficiaries": "Single-site tertiary orthopaedic FT serving a c. 6M West Midlands + national catchment for hip/knee arthroplasty, spinal, paediatric and oncology orthopaedics; c. 7,500 elective episodes and c. 65,000 outpatient attendances/yr; c. 1,300 WTE on the Northfield campus; one of England's three standalone orthopaedic specialist trusts.",
        "legal_basis": "Local Government Finance Act 1988 (Sch 6) · Non-Domestic Rating Act 2023 · Non-Domestic Rating (Multipliers and Private Finance) Act 2024 · Valuation Office Agency 2023 rating list · DHSC GAM 2024-25",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£0.37M"},
            {"label": "Estate", "value": "Single-site Bristol Road South, Northfield, Birmingham B31; main hospital + outpatient block + research/teaching wing"},
            {"label": "Billing authority", "value": "Birmingham City Council"},
            {"label": "VOA list", "value": "2023 rating list — RV based on receipts-and-expenditure / contractor's basis for hospital hereditaments"},
            {"label": "NDR multiplier 2024-25", "value": "Standard 54.6p; small-business 49.9p; healthcare estate generally on standard multiplier (no NHS charity relief)"},
            {"label": "Catchment", "value": "Supra-regional West Midlands + national referrals; c. 6M reference population"},
            {"label": "Workforce", "value": "c. 1,300 WTE on Northfield campus"},
            {"label": "Elective hub status", "value": "Designated NHSE high-volume low-complexity (HVLC) elective hub for arthroplasty"},
            {"label": "Delivery body", "value": "ROH Estates & Facilities + Birmingham City Council billing + Valuation Office Agency"},
            {"label": "Policy owner", "value": "MHCLG (formerly DLUHC) + HM Treasury + DHSC + NHSE"},
            {"label": "Funding trajectory", "value": "Rising c. 3-5%/yr in line with multiplier uprating + 2023 revaluation; supplementary multiplier under Non-Domestic Rating (Multipliers and Private Finance) Act 2024 from 2026-27"},
            {"label": "Evaluation evidence", "value": "ROH ARA; CQC provider profile (RRJ); NHSE ERIC 2023-24 estates return; VOA 2023 list entry"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2017 VOA rating list · Successor: 2026 VOA revaluation under 3-year cycle (NDR Act 2023) + supplementary multiplier 2026-27"}
        ],
        "notes": "NHS hospital trusts are full ratepayers under the Local Government Finance Act 1988 with no NHS-specific exemption, so business rates are a direct function of rateable value × multiplier. ROH's c. £0.37M reflects its single-site Northfield estate of c. 28,000sqm and the standard multiplier on a sizeable 'large' hereditament. Drivers include the VOA 2023 rating list (raising RVs on most hospital hereditaments), annual multiplier uprating, and the new supplementary multiplier on >£500k RVs introduced by the Non-Domestic Rating (Multipliers and Private Finance) Act 2024 (effective 2026-27). Future estate growth tied to NHSE elective-hub expansion would feed through into a higher RV at the next revaluation.",
        "sources": [
            {"publisher": "The Royal Orthopaedic Hospital NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.roh.nhs.uk/about-us/publications"},
            {"publisher": "Valuation Office Agency", "title": "Find a business rates valuation (2023 rating list)", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "UK Government", "title": "Non-Domestic Rating Act 2023", "url": "https://www.legislation.gov.uk/ukpga/2023/53"},
            {"publisher": "UK Government", "title": "Non-Domestic Rating (Multipliers and Private Finance) Act 2024", "url": "https://www.legislation.gov.uk/ukpga/2024/16"},
            {"publisher": "Care Quality Commission", "title": "The Royal Orthopaedic Hospital NHS Foundation Trust provider profile (RRJ)", "url": "https://www.cqc.org.uk/provider/RRJ"},
            {"publisher": "NHS England", "title": "Estates Returns Information Collection (ERIC) 2023-24", "url": "https://digital.nhs.uk/data-and-information/publications/statistical/estates-returns-information-collection"}
        ],
        "related": ["The Royal Orthopaedic Hospital NHS Foundation Trust", "Premises & Infrastructure", "NHS Specialist Trusts", "Business rates — Queen Victoria Hospital NHS Foundation Trust", "Business rates — Sheffield Children's NHS Foundation Trust", "Valuation Office Agency"]
    },
    "Amortisation — North East Ambulance Service NHS Foundation Trust": {
        "aliases": [{"name": "Amortisation", "parent": "North East Ambulance Service NHS Foundation Trust"}],
        "description": "NEAS's £0.37M amortisation charge represents the systematic write-down of intangible assets — predominantly software licences and capitalised software development under IAS 38, including the Computer-Aided Dispatch (CAD) system, the Electronic Patient Care Record (ePCR) used by paramedics on tablets in the back of ambulances, the NHS 111 Pathways platform (NEAS is the integrated 999/111 provider for the North East), and capitalised development on Make Ready Centre vehicle-prep IT and fleet-telematics integration with ORCDS dispatch.",
        "beneficiaries": "Sole 999 emergency-ambulance + 111 integrated provider for the North East of England — c. 2.7M population across Northumberland, Tyne & Wear, County Durham + Darlington, Tees Valley; c. 460,000 999 incidents/yr + c. 1.0M 111 calls/yr; c. 2,800 WTE; ambulance hub at Russell House, Newburn Riverside HQ + c. 60 stations.",
        "legal_basis": "IAS 38 Intangible Assets · DHSC Group Accounting Manual 2024-25 ch.5 · NHS Act 2006 · Health and Care Act 2022 · Civil Contingencies Act 2004 (Cat-1 responder)",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£0.37M"},
            {"label": "Service profile", "value": "999 emergency ambulance + integrated NHS 111 provider for the North East of England"},
            {"label": "Catchment", "value": "c. 2.7M population — Northumberland, Tyne & Wear, County Durham + Darlington, Tees Valley"},
            {"label": "Annual demand", "value": "c. 460,000 999 incidents/yr; c. 1.0M 111 calls/yr (one of few trusts integrating both)"},
            {"label": "Workforce", "value": "c. 2,800 WTE incl. paramedics, ECAs, 111 health advisors, clinicians, dispatchers"},
            {"label": "Estate", "value": "Russell House Newburn Riverside HQ + Hebburn EOC + c. 60 ambulance stations + Make Ready Centres at Newburn, Hebburn, Pallion + standby points"},
            {"label": "Intangibles class", "value": "CAD system, ePCR (paramedic tablet record), NHS 111 Pathways, fleet telematics, capitalised software dev"},
            {"label": "Useful economic life", "value": "Software typically 3-7 years amortisation per DHSC GAM ch.5"},
            {"label": "Delivery body", "value": "NEAS IT/Digital + CAD vendor + Adastra/Pathways for 111 + ePCR vendor"},
            {"label": "Policy owner", "value": "NHSE Urgent and Emergency Care + DHSC + North East and North Cumbria ICB + AACE (Association of Ambulance Chief Executives)"},
            {"label": "Funding trajectory", "value": "Stable around £0.3-0.4M; modest growth as NHSE single-CAD + Frontline Digitisation capital flows through to in-service intangibles"},
            {"label": "Evaluation evidence", "value": "NEAS ARA; CQC provider profile (RX6) — historic improvement journey post-2022 cultural review (Marsh review); ORH benchmarks; AACE returns"},
            {"label": "Predecessor / successor", "value": "Predecessor: legacy CAD + paper PCR · Successor: NHSE single-CAD national programme + ePCR refresh + Cat-2 mean target reform"}
        ],
        "notes": "Ambulance trust intangibles are dominated by mission-critical real-time software stacks: the Computer-Aided Dispatch (CAD) system that runs the 999/111 control rooms, the ePCR clinical record on paramedic tablets, and the NHS Pathways triage platform. NEAS has been on a transformation journey since the 2022 Marsh independent review of its culture and clinical-incident reporting, and is currently embedding the NHSE single-CAD national programme. Drivers include Frontline Digitisation capital, post-Marsh governance investment, and the Cat-2 mean response-time policy reset (Jul 2023, target 30 min) that reshaped operational software KPIs. Amortisation is small in absolute terms but rising slowly as new digital assets enter service.",
        "sources": [
            {"publisher": "North East Ambulance Service NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.neas.nhs.uk/about-us/publications/annual-reports-and-accounts/"},
            {"publisher": "Care Quality Commission", "title": "North East Ambulance Service NHS Foundation Trust provider profile (RX6)", "url": "https://www.cqc.org.uk/provider/RX6"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (ch.5 intangibles)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Ambulance services performance — operational reporting", "url": "https://www.england.nhs.uk/statistics/statistical-work-areas/ambulance-quality-indicators/"},
            {"publisher": "Association of Ambulance Chief Executives (AACE)", "title": "AACE national statistics + benchmarking", "url": "https://aace.org.uk/"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://transform.england.nhs.uk/digitise-connect-transform/frontline-digitisation/"}
        ],
        "related": ["North East Ambulance Service NHS Foundation Trust", "Premises & Infrastructure", "NHS Ambulance Trusts", "Amortisation — London Ambulance Service NHS Trust", "Amortisation — Yorkshire Ambulance Service NHS Trust", "NHS England"]
    },
    "Business rates — Leeds Community Healthcare NHS Trust": {
        "aliases": [{"name": "Business rates", "parent": "Leeds Community Healthcare NHS Trust"}],
        "description": "LCH's £0.37M non-domestic-rates (NDR) bill is the business rates payable to Leeds City Council under the Local Government Finance Act 1988 on the trust's portfolio of community-care premises across Leeds — community health centres, neighbourhood teams' bases, the WY-FI integrated health and wellbeing hubs, school-nursing bases, and dental-services clinics. NHS bodies do not enjoy charity relief, so the line tracks rateable value × multiplier directly across c. 60+ hereditaments scattered across the LS postcode area, with the Valuation Office Agency 2023 rating list driving 2024-25 RVs.",
        "beneficiaries": "Sole NHS provider of community physical and child health services to the c. 820,000 population of the city of Leeds; delivers c. 1.6M community contacts/yr through c. 3,300 WTE workforce (district nurses, HVs, school nurses, AHPs, MSK community physio, sexual health, community dental); operates from c. 60+ neighbourhood team bases, health centres and clinics.",
        "legal_basis": "Local Government Finance Act 1988 (Sch 6) · Non-Domestic Rating Act 2023 · Non-Domestic Rating (Multipliers and Private Finance) Act 2024 · Valuation Office Agency 2023 rating list · DHSC GAM 2024-25",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£0.37M"},
            {"label": "Estate footprint", "value": "c. 60+ neighbourhood-team bases, community health centres, dental clinics across the LS postcode area"},
            {"label": "Population served", "value": "c. 820,000 Leeds residents (sole NHS community provider)"},
            {"label": "Workforce", "value": "c. 3,300 WTE — district nurses, HVs, school nurses, AHPs, MSK physio, sexual health, community dental"},
            {"label": "Activity", "value": "c. 1.6M community contacts/yr; child health 0-19 service for c. 165,000 children"},
            {"label": "Billing authority", "value": "Leeds City Council"},
            {"label": "VOA list cycle", "value": "2023 rating list (3-year cycle from 2026 revaluation under Non-Domestic Rating Act 2023)"},
            {"label": "NDR multiplier 2024-25", "value": "Standard 54.6p; small-business 49.9p; healthcare estate generally on standard multiplier (no NHS exemption)"},
            {"label": "Delivery body", "value": "LCH Estates & Facilities + NHS Property Services (significant share of LCH estate is NHSPS-leased) + Leeds City Council billing"},
            {"label": "Policy owner", "value": "MHCLG (formerly DLUHC) + HM Treasury + DHSC + West Yorkshire ICB"},
            {"label": "Funding trajectory", "value": "Rising c. 3-5%/yr in line with multiplier uprating + 2023 revaluation; supplementary multiplier under Non-Domestic Rating (Multipliers and Private Finance) Act 2024 from 2026-27"},
            {"label": "Evaluation evidence", "value": "LCH ARA; CQC provider profile (RY6); NHSE ERIC 2023-24; VOA 2023 list entries"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2017 VOA rating list · Successor: 2026 VOA revaluation + Three Shifts (Darzi Sep 2024) community estate growth"}
        ],
        "notes": "Community-trust business-rates lines track directly with the breadth of estate rather than headcount: LCH's c. £0.37M reflects the long tail of c. 60+ small-to-medium hereditaments scattered across Leeds rather than a single large hospital. NHS bodies do not enjoy the 80% charity relief, so the bill is a non-discretionary annual cost. Drivers include the VOA 2023 rating list (which raised RVs on community-clinic hereditaments), annual multiplier uprating, and the new supplementary multiplier under the NDR (Multipliers and Private Finance) Act 2024 (effective 2026-27). The Three Shifts community-care policy may grow estate over time, feeding into future revaluations.",
        "sources": [
            {"publisher": "Leeds Community Healthcare NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.leedscommunityhealthcare.nhs.uk/about-us/publications/annual-reports/"},
            {"publisher": "Valuation Office Agency", "title": "Find a business rates valuation (2023 rating list)", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "UK Government", "title": "Non-Domestic Rating Act 2023", "url": "https://www.legislation.gov.uk/ukpga/2023/53"},
            {"publisher": "Care Quality Commission", "title": "Leeds Community Healthcare NHS Trust provider profile (RY6)", "url": "https://www.cqc.org.uk/provider/RY6"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Estates Returns Information Collection (ERIC) 2023-24", "url": "https://digital.nhs.uk/data-and-information/publications/statistical/estates-returns-information-collection"}
        ],
        "related": ["Leeds Community Healthcare NHS Trust", "Premises & Infrastructure", "NHS Community Trusts", "Business rates — Hertfordshire Community NHS Trust", "Business rates — Sussex Community NHS Foundation Trust", "Valuation Office Agency"]
    },
    "Termination & post-employment — Kent Community Health NHS Foundation Trust": {
        "aliases": [{"name": "Termination & post-employment", "parent": "Kent Community Health NHS Foundation Trust"}],
        "description": "KCHFT's £0.36M termination & post-employment line covers contractual exit costs and post-employment benefit charges recognised under IAS 19 — comprising voluntary-redundancy lump sums (subject to the Public Sector Exit Payments Regulations 2020 thresholds and waivers), early-retirement enhancements where actuarial uplift accrues to the trust, NHS Pension Scheme strain payments triggered by early-release decisions, and any contractual notice/PILON payments to leavers. The line moves with restructuring activity rather than baseline headcount, and is sensitive to ICS-led service-redesign rounds and the rolling out-of-hospital direction of travel.",
        "beneficiaries": "Sole NHS provider of community physical health and a wide tranche of community services across the c. 1.5M Kent + Medway population; c. 5,000 WTE workforce of district nurses, HVs, school nurses, MSK community physio, sexual health, dental, end-of-life and 0-19 child health teams operating from c. 100+ community sites; among the largest community FTs in England by headcount.",
        "legal_basis": "IAS 19 Employee Benefits · NHS Pension Scheme Regulations · NHS Terms and Conditions of Service Handbook (Agenda for Change s.16) · Public Sector Exit Payments Regulations 2020 · Pensions (Special Severance Payments) under HMT/DHSC guidance · DHSC GAM 2024-25",
        "key_stats": [
            {"label": "Termination & post-employment 2024-25", "value": "£0.36M"},
            {"label": "Trust profile", "value": "Among largest community FTs in England by headcount; covers Kent + Medway community services"},
            {"label": "Population served", "value": "c. 1.5M Kent + Medway residents"},
            {"label": "Workforce", "value": "c. 5,000 WTE — district nurses, HVs, school nurses, AHPs, MSK community physio, dental, sexual health, 0-19, end-of-life"},
            {"label": "Estate", "value": "c. 100+ community health centres, clinics, minor injuries units, GP-led centres + walk-in across Kent"},
            {"label": "Driver", "value": "Voluntary redundancy lump sums + IAS 19 actuarial uplift on early retirement + NHS pension scheme strain payments + PILONs"},
            {"label": "AfC reference", "value": "Section 16 NHS T&Cs Handbook redundancy formula (1 month's pay × reckonable years, capped 24 months)"},
            {"label": "Exit Payments cap", "value": "Public Sector Exit Payments Regulations 2020 (£95k cap revoked 2021 but ministerial waiver/approval framework retained)"},
            {"label": "Delivery body", "value": "KCHFT HR + NHS Pensions Agency + NHSBSA + actuarial advisor"},
            {"label": "Policy owner", "value": "DHSC + HMT + NHSE + Kent & Medway ICB"},
            {"label": "Funding trajectory", "value": "Cyclical — rises with restructuring rounds (e.g. ICS-led pathway redesign); generally low in steady state"},
            {"label": "Evaluation evidence", "value": "KCHFT ARA (remuneration + exit-payment disclosures); CQC provider profile (RYY); NAO public-sector exit-payments reports"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2020 £95k cap regs (revoked 2021) · Successor: ongoing HMT exit-payment guidance + Three Shifts community uplift potentially deferring redundancy rounds"}
        ],
        "notes": "Termination & post-employment lines are inherently lumpy and reflect organisational restructuring activity rather than baseline workforce. KCHFT is one of England's largest community FTs by headcount (c. 5,000 WTE), so even modest reorganisation rounds generate visible exit costs. Drivers include the AfC s.16 redundancy formula (1 month per year, capped at 24 months), IAS 19 actuarial uplift for early-retirement strain payments, and the post-2020 exit-payments framework (the £95k cap was revoked in 2021 but HMT/DHSC retain a ministerial-approval regime for exits >£100k). The line is sensitive to ICS-led pathway redesign and the post-Darzi Three Shifts policy direction.",
        "sources": [
            {"publisher": "Kent Community Health NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.kentcht.nhs.uk/about-us/publications/annual-report/"},
            {"publisher": "NHS Employers", "title": "NHS Terms and Conditions of Service Handbook (s.16 redundancy)", "url": "https://www.nhsemployers.org/publications/tchandbook"},
            {"publisher": "IFRS Foundation", "title": "IAS 19 Employee Benefits", "url": "https://www.ifrs.org/issued-standards/list-of-standards/ias-19-employee-benefits/"},
            {"publisher": "HM Treasury", "title": "Guidance on public sector exit payments", "url": "https://www.gov.uk/government/publications/guidance-on-public-sector-exit-payments"},
            {"publisher": "Care Quality Commission", "title": "Kent Community Health NHS Foundation Trust provider profile (RYY)", "url": "https://www.cqc.org.uk/provider/RYY"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"}
        ],
        "related": ["Kent Community Health NHS Foundation Trust", "Staff Costs", "NHS Community Trusts", "Termination & post-employment — Derbyshire Community Health Services NHS Foundation Trust", "Termination & post-employment — Norfolk Community Health and Care NHS Trust", "NHS Pension Scheme"]
    },
    "Lease expenditure — Birmingham Community Healthcare NHS Foundation Trust": {
        "aliases": [{"name": "Lease expenditure", "parent": "Birmingham Community Healthcare NHS Foundation Trust"}],
        "description": "BCHC's £0.36M lease expenditure orphan covers IFRS 16 right-of-use leases for non-headquarters premises and operational kit — community-clinic space leased from NHS Property Services and third-party landlords across Birmingham city, the West Midlands Rehabilitation Centre satellite estate, dental-services chairs and clinic suites, the trust's pool fleet of district-nursing and MSK community-physio cars, and small-ticket medical-equipment finance leases. Since the April 2022 IFRS 16 transition, leases above 12 months and the de-minimis threshold sit on balance sheet as right-of-use assets with associated lease-liability and finance-charge splits.",
        "beneficiaries": "Sole NHS community provider for Birmingham (c. 1.15M residents) including dental services across Birmingham + Solihull; specialist services include the West Midlands Rehabilitation Centre, learning disability inpatient + community, prison healthcare, and a children's community service; c. 5,200 WTE operating from c. 130 sites across the city.",
        "legal_basis": "IFRS 16 Leases · DHSC Group Accounting Manual 2024-25 ch.7 · Landlord and Tenant Act 1954 · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Lease expenditure 2024-25", "value": "£0.36M"},
            {"label": "Trust profile", "value": "Sole NHS community provider for Birmingham; runs WM Rehab Centre, Bham + Solihull dental, LD inpatient + community, prison healthcare"},
            {"label": "Population served", "value": "c. 1.15M Birmingham residents (+ regional draw on WM Rehab Centre)"},
            {"label": "Workforce", "value": "c. 5,200 WTE — district nurses, HVs, school nurses, AHPs, MSK community physio, dental, LD, prison healthcare"},
            {"label": "Estate", "value": "c. 130 sites across Birmingham — community health centres, dental clinics, WM Rehab Centre, LD inpatient units"},
            {"label": "Lease composition", "value": "NHSPS-leased clinic space + third-party clinic space + dental-services chairs + pool-fleet vehicles + medical-equipment finance leases"},
            {"label": "IFRS 16 driver", "value": "April 2022 transition recognised right-of-use assets and lease liabilities on balance sheet"},
            {"label": "Delivery body", "value": "BCHC Estates & Facilities + NHS Property Services + commercial fleet leasing + medical-equipment finance"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Birmingham & Solihull ICB + NHS Property Services"},
            {"label": "Funding trajectory", "value": "Stable around £0.3-0.4M; April 2022 IFRS 16 step-up; modest growth as Three Shifts community policy may grow community estate"},
            {"label": "Evaluation evidence", "value": "BCHC ARA; CQC provider profile (RYW); NHSE ERIC 2023-24 estates return; NHSPS lease portfolio reporting"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-IFRS-16 operating-lease P&L treatment · Successor: NHSPS estate rationalisation + Three Shifts community lift"}
        ],
        "notes": "BCHC operates one of the largest urban community estates in England — c. 130 sites across Birmingham — and a meaningful share is leased from NHS Property Services rather than owned, so the lease line picks up that NHSPS rental flow plus pool-fleet and dental-chair finance leases. The April 2022 IFRS 16 transition stepped this onto balance sheet, and ongoing drivers include NHSPS estate rationalisation, Landlord and Tenant Act 1954 renewal cycles on third-party clinic space, and the Three Shifts (Darzi Sep 2024) push to expand community capacity. Pool-fleet electrification under NHSE Net Zero 2032 will also change the lease mix over coming years.",
        "sources": [
            {"publisher": "Birmingham Community Healthcare NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.bhamcommunity.nhs.uk/about-us/our-publications/annual-reports/"},
            {"publisher": "NHS Property Services", "title": "About NHSPS", "url": "https://www.property.nhs.uk/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (ch.7 leases)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "IFRS Foundation", "title": "IFRS 16 Leases", "url": "https://www.ifrs.org/issued-standards/list-of-standards/ifrs-16-leases/"},
            {"publisher": "Care Quality Commission", "title": "Birmingham Community Healthcare NHS Foundation Trust provider profile (RYW)", "url": "https://www.cqc.org.uk/provider/RYW"},
            {"publisher": "NHS England", "title": "Estates Returns Information Collection (ERIC) 2023-24", "url": "https://digital.nhs.uk/data-and-information/publications/statistical/estates-returns-information-collection"}
        ],
        "related": ["Birmingham Community Healthcare NHS Foundation Trust", "Premises & Infrastructure", "NHS Community Trusts", "Lease expenditure — Central London Community Healthcare NHS Trust", "Lease expenditure — Kent Community Health NHS Foundation Trust", "NHS Property Services"]
    },
    "Drugs costs — Yorkshire Ambulance Service NHS Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "Yorkshire Ambulance Service NHS Trust"}],
        "description": "YAS's £0.35M drugs costs covers the medicines carried in the back of every front-line ambulance and Rapid Response Vehicle in Yorkshire — paramedic-administered emergency drugs under PGDs and the Human Medicines Regulations 2012 Sch 17 paramedic exemption: morphine, midazolam, adrenaline, naloxone, salbutamol/ipratropium nebs, paracetamol, tranexamic acid, glucagon, glucose gel, oxygen and TXA for trauma. Stock is replenished through the Make Ready Centre model that turns vehicles around between shifts. Volume is high but unit cost is mostly low (oxygen, generics) so the line is small relative to acute hospital pharmacy spend.",
        "beneficiaries": "Sole 999 emergency-ambulance + 111 integrated provider for the c. 5.5M population of Yorkshire and the Humber (West, North, South + East Yorkshire + the Humber); c. 1.0M 999 incidents/yr + c. 1.4M 111 calls/yr; c. 6,500 WTE operating from c. 60 ambulance stations + Make Ready Centres at Springhill (Wakefield), Doncaster, York and Hull.",
        "legal_basis": "NHS Act 2006 (Drug Tariff) · Human Medicines Regulations 2012 (Sch 17 paramedic exemption + PGDs) · Misuse of Drugs Regulations 2001 (CD storage / records) · Health and Care Act 2022 · DHSC GAM 2024-25",
        "key_stats": [
            {"label": "Drugs costs 2024-25", "value": "£0.35M"},
            {"label": "Service profile", "value": "999 emergency ambulance + integrated NHS 111 provider for Yorkshire and the Humber"},
            {"label": "Catchment", "value": "c. 5.5M residents — West, North, South, East Yorkshire + the Humber"},
            {"label": "Annual demand", "value": "c. 1.0M 999 incidents/yr; c. 1.4M 111 calls/yr; ~5th-largest ambulance trust by activity"},
            {"label": "Workforce", "value": "c. 6,500 WTE incl. paramedics, ECAs, technicians, 111 health advisors, dispatchers"},
            {"label": "Drug formulary", "value": "Paramedic emergency formulary — morphine, midazolam, adrenaline, naloxone, salbutamol/ipratropium, paracetamol, TXA, glucagon, oxygen"},
            {"label": "Make Ready Centres", "value": "Vehicle prep + stock replenishment hubs at Springhill (Wakefield), Doncaster, York, Hull — drives stock-management efficiency"},
            {"label": "CD storage", "value": "Schedule-2 CD registers (morphine, midazolam) under Misuse of Drugs Regulations 2001 with HQ + station-level safes"},
            {"label": "Delivery body", "value": "YAS Pharmacy Lead + station-level Medicines Management + NHS Supply Chain pharmacy + LPP / North of England framework"},
            {"label": "Policy owner", "value": "NHSE Urgent and Emergency Care + DHSC + AACE + JRCALC (paramedic clinical practice guidelines)"},
            {"label": "Funding trajectory", "value": "Stable — slight rise from naloxone expansion (community drug-poisoning response) + Cat-1/Cat-2 demand growth"},
            {"label": "Evaluation evidence", "value": "YAS ARA; CQC provider profile (RX8); JRCALC formulary updates; AACE benchmarking; NHSE Cat-1/Cat-2 returns"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2018 paramedic prescribing era · Successor: paramedic independent prescribing (HCPC reg 2018) + naloxone expansion + JRCALC formulary refresh"}
        ],
        "notes": "Ambulance trusts run a structurally small but highly regulated drugs spend: the paramedic emergency formulary is narrow (c. 30 drugs) but every front-line vehicle must be stocked and CDs (morphine/midazolam) need register-based audit trails under the Misuse of Drugs Regulations 2001. The Make Ready Centre model concentrates stock replenishment at four hubs, which keeps unit cost down. Drivers include the JRCALC paramedic clinical-guideline updates, paramedic independent prescribing (HCPC registered 2018, expanded scope), and naloxone expansion as part of national drug-poisoning response (lifesaving overdose-reversal, c. £30/dose). YAS also went through the 2023-24 paramedic industrial action which had operational but limited drug-spend implications.",
        "sources": [
            {"publisher": "Yorkshire Ambulance Service NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.yas.nhs.uk/about-us/our-publications/annual-reports-and-accounts/"},
            {"publisher": "Care Quality Commission", "title": "Yorkshire Ambulance Service NHS Trust provider profile (RX8)", "url": "https://www.cqc.org.uk/provider/RX8"},
            {"publisher": "JRCALC / Association of Ambulance Chief Executives", "title": "JRCALC Clinical Guidelines (paramedic formulary)", "url": "https://aace.org.uk/clinical-practice-guidelines/"},
            {"publisher": "UK Government", "title": "Human Medicines Regulations 2012 (Sch 17 paramedic exemption)", "url": "https://www.legislation.gov.uk/uksi/2012/1916/contents"},
            {"publisher": "UK Government", "title": "Misuse of Drugs Regulations 2001", "url": "https://www.legislation.gov.uk/uksi/2001/3998/contents"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"}
        ],
        "related": ["Yorkshire Ambulance Service NHS Trust", "Clinical Supplies & Drugs", "NHS Ambulance Trusts", "Drugs costs — South Central Ambulance Service NHS Foundation Trust", "Drugs costs — London Ambulance Service NHS Trust", "JRCALC"]
    },
    "Transport (business + patient) — The Robert Jones and Agnes Hunt Orthopaedic Hospital NHS Foundation Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "The Robert Jones and Agnes Hunt Orthopaedic Hospital NHS Foundation Trust"}],
        "description": "RJAH Oswestry's £0.35M transport line covers business mileage (AMAP) for clinical and corporate staff travelling between the rural Oswestry main site and outreach orthopaedic clinics across Shropshire, Mid Wales and Cheshire, leased pool-cars and inter-site transfers, plus patient-transport reimbursements under NHSE PTS eligibility for arthroplasty, paediatric orthopaedic, spinal and limb-reconstruction patients travelling for tertiary care. The very rural catchment and supra-regional referral footprint mean PTS volumes per case are unusually high, with patients regularly travelling 60+ miles from Mid Wales and Powys.",
        "beneficiaries": "Tertiary supra-regional orthopaedic specialist FT serving a c. 3M reference population from Shropshire + Cheshire + Staffordshire + Mid Wales + Powys + parts of West Midlands; c. 50,000 outpatient attendances + c. 4,500 inpatient/day-case episodes/yr including paediatric, spinal, oncology and limb-reconstruction; c. 1,400 WTE on the rural Gobowen, Oswestry main site.",
        "legal_basis": "NHS Act 2006 · NHSE Patient Transport Services Eligibility Criteria · Healthcare Travel Costs Scheme (HTCS) · Agenda for Change s.17 + HMRC Approved Mileage Allowance Payments · IFRS 16 Leases (pool fleet) · DHSC Group Accounting Manual 2024-25",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£0.35M"},
            {"label": "Specialty footprint", "value": "Tertiary specialist orthopaedic FT — single rural site at Gobowen, Oswestry, Shropshire SY10; one of three standalone orthopaedic trusts in England"},
            {"label": "Catchment", "value": "c. 3M Shropshire + Cheshire + Staffordshire + Mid Wales + Powys; cross-border NHS Wales referrals are a key driver"},
            {"label": "Annual activity", "value": "c. 50,000 outpatients; c. 4,500 elective inpatient/day-case; paediatric, spinal, oncology, limb-reconstruction subspecialties"},
            {"label": "Workforce", "value": "c. 1,400 WTE; c. 90 medical + c. 400 nursing"},
            {"label": "Rurality driver", "value": "Long PTS journey distances — Mid Wales and Powys patients regularly travel 60+ miles each way to Oswestry"},
            {"label": "Cross-border flow", "value": "Powys Teaching Health Board commissions large arthroplasty + spinal volume from RJAH (c. 25-30% of activity is Welsh patients)"},
            {"label": "Delivery body", "value": "RJAH Estates & Facilities + leased-fleet supplier + commissioned PTS operator + AMAP staff mileage"},
            {"label": "Policy owner", "value": "NHSE Specialised Commissioning (orthopaedic oncology + complex spinal) + Welsh Government / Powys THB (cross-border) + Shropshire, Telford and Wrekin ICB"},
            {"label": "Funding trajectory", "value": "Modest growth post-pandemic + IFRS 16 2022 lease re-recognition + AMAP rate review pressure"},
            {"label": "Evaluation evidence", "value": "RJAH ARA; CQC provider profile (RL1); NJR annual report; GIRFT orthopaedic benchmarks; cross-border patient flow returns to Welsh Government"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-IFRS-16 era operating-lease pool fleet · Successor: zero-emission pool fleet under NHSE Net Zero 2032 + cross-border review of Welsh patient flows"}
        ],
        "notes": "RJAH is one of England's three standalone tertiary orthopaedic specialist FTs (alongside RNOH Stanmore and ROH Birmingham), with a unique rural single-site footprint at Gobowen near the Welsh border. That geography drives an unusually high PTS reimbursement per case as patients travel from Mid Wales and Powys (where Powys Teaching Health Board commissions a quarter to a third of RJAH's activity). Drivers include the rural catchment, HTCS eligibility for low-income elective patients, IFRS 16 2022 lease step-up, AMAP rate uplift pressure, and NHSE Net Zero 2032 fleet electrification. Welsh-Government NHS-Wales cross-border commissioning reviews are an ongoing structural risk.",
        "sources": [
            {"publisher": "The Robert Jones and Agnes Hunt Orthopaedic Hospital NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.rjah.nhs.uk/about-us/publications/annual-reports/"},
            {"publisher": "Care Quality Commission", "title": "The Robert Jones and Agnes Hunt Orthopaedic Hospital NHS Foundation Trust provider profile (RL1)", "url": "https://www.cqc.org.uk/provider/RL1"},
            {"publisher": "NHS England", "title": "Healthcare Travel Costs Scheme (HTCS)", "url": "https://www.nhs.uk/nhs-services/help-with-health-costs/healthcare-travel-costs-scheme-htcs/"},
            {"publisher": "Welsh Government", "title": "Cross-border healthcare arrangements England-Wales", "url": "https://www.gov.wales/cross-border-arrangements-nhs"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "NHS Net Zero — delivering a net zero NHS", "url": "https://www.england.nhs.uk/greenernhs/a-net-zero-nhs/"}
        ],
        "related": ["The Robert Jones and Agnes Hunt Orthopaedic Hospital NHS Foundation Trust", "Premises & Infrastructure", "NHS Specialist Trusts", "Transport (business + patient) — The Royal Marsden NHS Foundation Trust", "Transport (business + patient) — The Christie NHS Foundation Trust", "NHS England"]
    },
    "Amortisation — Sheffield Children's NHS Foundation Trust": {
        "aliases": [{"name": "Amortisation", "parent": "Sheffield Children's NHS Foundation Trust"}],
        "description": "Sheffield Children's £0.35M amortisation charge represents the systematic write-down of intangible assets — predominantly software licences and capitalised software development under IAS 38, including the paediatric EPR (Sheffield uses Lorenzo / EPIC migration in progress), PACS and paediatric-imaging analysis, the children's hospital research-systems estate (Sheffield is a major paediatric NIHR research centre), and capitalised development on the Becton off-site outpatient hub and CAMHS digital platform. Sheffield is one of England's four standalone children's specialist FTs.",
        "beneficiaries": "Tertiary children's specialist FT serving a c. 3.5M reference population across South Yorkshire, North Derbyshire, North Notts and parts of the East Midlands; c. 280,000 outpatient attendances + c. 60,000 ED attendances + c. 15,000 inpatient/day-case episodes/yr; c. 3,500 WTE on Western Bank main site (S10) + Becton ambulatory care hub + Ryegate.",
        "legal_basis": "IAS 38 Intangible Assets · DHSC Group Accounting Manual 2024-25 ch.5 · NHS Act 2006 · Health and Care Act 2022 · Frascati Manual research/development distinction",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£0.35M"},
            {"label": "Specialty footprint", "value": "Tertiary children's hospital — Western Bank main site + Becton ambulatory hub + Ryegate; one of four standalone children's FTs in England (with GOSH, Alder Hey, Birmingham Children's)"},
            {"label": "Catchment", "value": "c. 3.5M reference population — South Yorkshire, North Derbyshire, North Notts, parts of East Midlands"},
            {"label": "Annual activity", "value": "c. 280,000 outpatients; c. 60,000 ED; c. 15,000 inpatient/day-case; CAMHS Tier 4; major paediatric trauma; metabolic + cancer subspecialties"},
            {"label": "Workforce", "value": "c. 3,500 WTE; c. 360 medical + c. 1,200 nursing"},
            {"label": "Intangibles class", "value": "Paediatric EPR (Lorenzo, EPIC migration), PACS, research systems (NIHR-supported), CAMHS digital platform, capitalised software dev"},
            {"label": "Useful economic life", "value": "Software typically 3-7 years amortisation per DHSC GAM ch.5"},
            {"label": "Research footprint", "value": "NIHR Sheffield Children's Clinical Research Facility; major paediatric clinical-trial portfolio"},
            {"label": "Delivery body", "value": "SCH IT/Digital + EPR vendor (Lorenzo/EPIC) + research-grant-funded systems + South Yorkshire ICS digital programme"},
            {"label": "Policy owner", "value": "NHSE Specialised Commissioning (paediatric tertiary services) + DHSC + South Yorkshire ICB + NHSE Frontline Digitisation"},
            {"label": "Funding trajectory", "value": "Stable around £0.3-0.4M; modest growth as Frontline Digitisation + EPIC migration capital flows through to in-service intangibles"},
            {"label": "Evaluation evidence", "value": "SCH ARA; CQC provider profile (RCU); NHSE Specialised Commissioning paediatric returns; NIHR research metrics"},
            {"label": "Predecessor / successor", "value": "Predecessor: legacy paediatric systems · Successor: EPIC migration + Frontline Digitisation 2025-30 + Becton hub digital build-out"}
        ],
        "notes": "Sheffield Children's is one of England's four standalone children's specialist FTs and a major NIHR paediatric research centre, so its intangibles base mixes operational EPR/PACS software with research-grant-funded clinical-research IT. Amortisation is small in cash terms (c. £0.35M) but is rising as the trust progresses through Frontline Digitisation capital and a planned EPIC EPR migration that will replace the legacy Lorenzo footprint. The Becton ambulatory hub also drives capitalised software for paediatric outpatient flow. Drivers include NHSE Frontline Digitisation, EPIC migration, and ongoing research-systems investment.",
        "sources": [
            {"publisher": "Sheffield Children's NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.sheffieldchildrens.nhs.uk/about-us/our-publications/"},
            {"publisher": "Care Quality Commission", "title": "Sheffield Children's NHS Foundation Trust provider profile (RCU)", "url": "https://www.cqc.org.uk/provider/RCU"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (ch.5 intangibles)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://transform.england.nhs.uk/digitise-connect-transform/frontline-digitisation/"},
            {"publisher": "National Institute for Health and Care Research", "title": "NIHR Sheffield Children's Clinical Research Facility", "url": "https://www.nihr.ac.uk/explore-nihr/support/clinical-research-facilities.htm"},
            {"publisher": "IFRS Foundation", "title": "IAS 38 Intangible Assets", "url": "https://www.ifrs.org/issued-standards/list-of-standards/ias-38-intangible-assets/"}
        ],
        "related": ["Sheffield Children's NHS Foundation Trust", "Premises & Infrastructure", "NHS Specialist Trusts", "Amortisation — Alder Hey Children's NHS Foundation Trust", "Amortisation — Great Ormond Street Hospital for Children NHS Foundation Trust", "NHS England"]
    },
    "Business rates — Queen Victoria Hospital NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "Queen Victoria Hospital NHS Foundation Trust"}],
        "description": "QVH East Grinstead's £0.34M non-domestic-rates (NDR) bill is the business rates payable to Mid Sussex District Council under the Local Government Finance Act 1988 on the historic East Grinstead campus, including the Sir Archibald McIndoe wartime burns-and-plastics legacy buildings. As a small specialist FT focused on reconstructive surgery, burns, head & neck and complex trauma reconstruction (the original 'Guinea Pig Club' wartime hospital), QVH's site is geographically compact but the rateable value is significant given the listed-building status and the on-site research/teaching wing.",
        "beneficiaries": "Tertiary specialist FT for reconstructive surgery, burns, head & neck cancer, complex trauma reconstruction and corneoplastic ophthalmology — serving a c. 4M reference population across Sussex, Surrey, Kent and the wider South East; c. 70,000 outpatients + c. 15,000 inpatient/day-case episodes/yr; c. 1,150 WTE on a single East Grinstead RH19 site.",
        "legal_basis": "Local Government Finance Act 1988 (Sch 6) · Non-Domestic Rating Act 2023 · Non-Domestic Rating (Multipliers and Private Finance) Act 2024 · Valuation Office Agency 2023 rating list · DHSC GAM 2024-25",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£0.34M"},
            {"label": "Estate", "value": "Single-site East Grinstead RH19; historic wartime burns + plastics campus (Sir Archibald McIndoe legacy buildings)"},
            {"label": "Specialty footprint", "value": "Tertiary reconstructive surgery, burns, head & neck cancer, complex trauma reconstruction, corneoplastic ophthalmology"},
            {"label": "Catchment", "value": "c. 4M reference population across Sussex, Surrey, Kent + wider South East referrals"},
            {"label": "Annual activity", "value": "c. 70,000 outpatient attendances; c. 15,000 inpatient/day-case episodes; specialised commissioning for burns + reconstruction"},
            {"label": "Workforce", "value": "c. 1,150 WTE on the East Grinstead campus"},
            {"label": "Billing authority", "value": "Mid Sussex District Council"},
            {"label": "VOA list", "value": "2023 rating list — RV based on contractor's basis for hospital hereditament with listed-building considerations"},
            {"label": "NDR multiplier 2024-25", "value": "Standard 54.6p; healthcare estate generally on standard multiplier (no NHS exemption)"},
            {"label": "Delivery body", "value": "QVH Estates & Facilities + Mid Sussex District Council billing + Valuation Office Agency"},
            {"label": "Policy owner", "value": "MHCLG (formerly DLUHC) + HM Treasury + DHSC + NHSE Specialised Commissioning + Sussex ICB"},
            {"label": "Funding trajectory", "value": "Rising c. 3-5%/yr in line with multiplier uprating + 2023 revaluation; supplementary multiplier under Non-Domestic Rating (Multipliers and Private Finance) Act 2024 from 2026-27"},
            {"label": "Evaluation evidence", "value": "QVH ARA; CQC provider profile (RPC); NHSE Specialised Commissioning burns + reconstruction returns; NHSE ERIC 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2017 VOA list · Successor: 2026 VOA revaluation under 3-year cycle + supplementary multiplier 2026-27 + ongoing east-wing redevelopment business case"}
        ],
        "notes": "QVH is a small specialist FT with one of the most distinctive histories in the NHS — the East Grinstead campus housed the wartime Guinea Pig Club under Sir Archibald McIndoe — and continues as the South East's tertiary reconstructive-surgery centre. Its £0.34M rates bill reflects the standard multiplier applied to a sizeable RV on a historic single-site campus (with listed-building elements complicating contractor's-basis valuation). NHS bodies do not enjoy charity relief, so the bill is a non-discretionary annual cost. Drivers include the VOA 2023 rating list, annual multiplier uprating, the new supplementary multiplier under the NDR (Multipliers and Private Finance) Act 2024, and any future rebuild affecting RV at next revaluation.",
        "sources": [
            {"publisher": "Queen Victoria Hospital NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.qvh.nhs.uk/about-us/our-publications/"},
            {"publisher": "Valuation Office Agency", "title": "Find a business rates valuation (2023 rating list)", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "UK Government", "title": "Non-Domestic Rating Act 2023", "url": "https://www.legislation.gov.uk/ukpga/2023/53"},
            {"publisher": "UK Government", "title": "Non-Domestic Rating (Multipliers and Private Finance) Act 2024", "url": "https://www.legislation.gov.uk/ukpga/2024/16"},
            {"publisher": "Care Quality Commission", "title": "Queen Victoria Hospital NHS Foundation Trust provider profile (RPC)", "url": "https://www.cqc.org.uk/provider/RPC"},
            {"publisher": "NHS England", "title": "Specialised commissioning — burns service specification", "url": "https://www.england.nhs.uk/commissioning/spec-services/"}
        ],
        "related": ["Queen Victoria Hospital NHS Foundation Trust", "Premises & Infrastructure", "NHS Specialist Trusts", "Business rates — The Royal Marsden NHS Foundation Trust", "Business rates — The Christie NHS Foundation Trust", "Valuation Office Agency"]
    },
    "Transport (business + patient) — The Clatterbridge Cancer Centre NHS Foundation Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "The Clatterbridge Cancer Centre NHS Foundation Trust"}],
        "description": "Clatterbridge's £0.34M transport line covers business mileage (AMAP) for clinical and corporate staff travelling between the Clatterbridge Liverpool main hub (opened 2020 in the Liverpool Knowledge Quarter), the historic Wirral campus, and outreach radiotherapy + chemo at Aintree, Halton and Wirral, plus patient-transport reimbursements under NHSE PTS for chemotherapy, radiotherapy fractions and proton-beam-therapy referrals. Specialist couriers move cytotoxic chemotherapy preparations, short-half-life PET tracers and radioisotopes between sites within the c. 2.4M Cheshire & Merseyside cancer catchment.",
        "beneficiaries": "Tertiary cancer specialist FT serving a c. 2.4M Cheshire & Merseyside + Isle of Man + parts of Lancashire population; c. 33,000 patients/yr including c. 11,000 chemo episodes + c. 90,000 radiotherapy fractions + c. 15,000 systemic anti-cancer therapy episodes; c. 2,000 WTE across Clatterbridge Liverpool (CCC-L), Wirral (Bebington), Aintree and Halton outreach.",
        "legal_basis": "NHS Act 2006 · NHSE Patient Transport Services Eligibility Criteria · Healthcare Travel Costs Scheme (HTCS) · Agenda for Change s.17 + HMRC Approved Mileage Allowance Payments · IFRS 16 Leases (pool fleet) · DHSC Group Accounting Manual 2024-25",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£0.34M"},
            {"label": "Specialty footprint", "value": "Tertiary cancer centre — Clatterbridge Liverpool (Knowledge Quarter, opened 2020) + historic Wirral campus + Aintree + Halton outreach"},
            {"label": "Catchment", "value": "c. 2.4M Cheshire & Merseyside + Isle of Man + parts of Lancashire"},
            {"label": "Annual activity", "value": "c. 33,000 patients/yr; c. 11,000 chemo episodes; c. 90,000 radiotherapy fractions; c. 15,000 SACT episodes"},
            {"label": "Workforce", "value": "c. 2,000 WTE across CCC-L + Wirral + outreach"},
            {"label": "PTS driver", "value": "Daily radiotherapy fractions (15-30 visits/course) drive HTCS reimbursement volume; proton-beam therapy referrals to The Christie or UCLH"},
            {"label": "Specialist couriers", "value": "Cytotoxic chemo preparations + short-half-life PET tracers + radioisotopes between Wirral pharmacy aseptic unit + CCC-L + outreach"},
            {"label": "Inter-site transfers", "value": "Mersey + Wirral logistics — significant inter-site flow since CCC-L opened 2020 (no longer Wirral-only)"},
            {"label": "Delivery body", "value": "Clatterbridge Estates & Facilities + leased-fleet supplier + commissioned PTS operator (NWAS PTS contract) + specialist radiopharm couriers"},
            {"label": "Policy owner", "value": "NHSE Specialised Commissioning (cancer) + DHSC + Cheshire & Merseyside ICB"},
            {"label": "Funding trajectory", "value": "Modest growth post-CCC-L opening (2020) + IFRS 16 2022 lease re-recognition + AMAP rate review pressure + Net Zero 2032 fleet electrification"},
            {"label": "Evaluation evidence", "value": "Clatterbridge ARA; CQC provider profile (REN); Model Hospital cancer benchmarks; NHSE radiotherapy + SACT activity returns"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2020 Wirral-only campus · Successor: zero-emission pool fleet under NHSE Net Zero 2032 + further outreach radiotherapy expansion"}
        ],
        "notes": "Clatterbridge underwent a transformational change in 2020 when the new Clatterbridge Liverpool main hub opened in the Knowledge Quarter, sitting alongside the Royal Liverpool University Hospital and creating significant inter-site flow with the historic Wirral campus and outreach at Aintree and Halton. That has driven up business mileage and pool-fleet utilisation. Drivers include the post-2020 inter-site logistics, daily radiotherapy fractionation driving HTCS reimbursement, specialist radiopharm courier costs (cytotoxic chemo, PET tracers), IFRS 16 2022 lease re-recognition, AMAP rate-uplift pressure, and NHSE Net Zero 2032 fleet electrification.",
        "sources": [
            {"publisher": "The Clatterbridge Cancer Centre NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.clatterbridgecc.nhs.uk/about-us/our-publications/annual-reports/"},
            {"publisher": "Care Quality Commission", "title": "The Clatterbridge Cancer Centre NHS Foundation Trust provider profile (REN)", "url": "https://www.cqc.org.uk/provider/REN"},
            {"publisher": "NHS England", "title": "Specialised commissioning — cancer service specification", "url": "https://www.england.nhs.uk/commissioning/spec-services/"},
            {"publisher": "NHS England", "title": "Healthcare Travel Costs Scheme (HTCS)", "url": "https://www.nhs.uk/nhs-services/help-with-health-costs/healthcare-travel-costs-scheme-htcs/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "NHS Net Zero — delivering a net zero NHS", "url": "https://www.england.nhs.uk/greenernhs/a-net-zero-nhs/"}
        ],
        "related": ["The Clatterbridge Cancer Centre NHS Foundation Trust", "Premises & Infrastructure", "NHS Specialist Trusts", "Transport (business + patient) — The Christie NHS Foundation Trust", "Transport (business + patient) — The Royal Marsden NHS Foundation Trust", "NHS England"]
    },
    "Drugs costs — South Central Ambulance Service NHS Foundation Trust": {
        "aliases": [{"name": "Drugs costs", "parent": "South Central Ambulance Service NHS Foundation Trust"}],
        "description": "SCAS's £0.33M drugs costs covers the medicines carried in the back of every front-line ambulance and Rapid Response Vehicle across the South Central region — paramedic-administered emergency drugs under PGDs and the Human Medicines Regulations 2012 Sch 17 paramedic exemption: morphine, midazolam, adrenaline, naloxone, salbutamol/ipratropium, paracetamol, tranexamic acid, glucagon, glucose gel, oxygen and TXA for trauma. Stock is replenished through the Make Ready model. SCAS also runs the integrated NHS 111 service for Hampshire, IoW, Berkshire, Buckinghamshire and Oxfordshire, but 111 is largely a triage/dispatch service with limited drug stock implications.",
        "beneficiaries": "999 emergency-ambulance + integrated NHS 111 provider for the South Central region — c. 4.6M population across Hampshire, Isle of Wight, Berkshire, Buckinghamshire + Oxfordshire; c. 600,000 999 incidents/yr + c. 1.4M 111 calls/yr; c. 4,200 WTE; HQ Bicester (Oxon) + Northern Resource Centre (Otterbourne, Hants) + c. 50 ambulance stations.",
        "legal_basis": "NHS Act 2006 (Drug Tariff) · Human Medicines Regulations 2012 (Sch 17 paramedic exemption + PGDs) · Misuse of Drugs Regulations 2001 (CD storage / records) · Health and Care Act 2022 · DHSC GAM 2024-25",
        "key_stats": [
            {"label": "Drugs costs 2024-25", "value": "£0.33M"},
            {"label": "Service profile", "value": "999 emergency ambulance + integrated NHS 111 provider for the South Central region"},
            {"label": "Catchment", "value": "c. 4.6M residents — Hampshire, Isle of Wight, Berkshire, Buckinghamshire + Oxfordshire"},
            {"label": "Annual demand", "value": "c. 600,000 999 incidents/yr; c. 1.4M 111 calls/yr"},
            {"label": "Workforce", "value": "c. 4,200 WTE incl. paramedics, ECAs, technicians, 111 health advisors, dispatchers"},
            {"label": "Estate", "value": "HQ Bicester (Oxon) + Northern Resource Centre Otterbourne (Hants) + c. 50 ambulance stations + Make Ready locations"},
            {"label": "Drug formulary", "value": "Paramedic emergency formulary — morphine, midazolam, adrenaline, naloxone, salbutamol/ipratropium, paracetamol, TXA, glucagon, oxygen"},
            {"label": "CD storage", "value": "Schedule-2 CD registers (morphine, midazolam) under Misuse of Drugs Regulations 2001 with HQ + station-level safes"},
            {"label": "Delivery body", "value": "SCAS Pharmacy Lead + station-level Medicines Management + NHS Supply Chain pharmacy + LPP framework"},
            {"label": "Policy owner", "value": "NHSE Urgent and Emergency Care + DHSC + AACE + JRCALC (paramedic clinical practice guidelines)"},
            {"label": "Funding trajectory", "value": "Stable — slight rise from naloxone expansion + Cat-1/Cat-2 demand growth + JRCALC formulary updates"},
            {"label": "Evaluation evidence", "value": "SCAS ARA; CQC provider profile (RYE) — historic 2022-23 inspection findings around culture/governance with Requires Improvement; JRCALC formulary updates; AACE benchmarking"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2018 paramedic prescribing era · Successor: paramedic independent prescribing (HCPC reg 2018) + naloxone expansion + JRCALC formulary refresh"}
        ],
        "notes": "SCAS covers a large but relatively low-density catchment with mixed urban (Reading, Oxford, Southampton, Portsmouth) and deep-rural (New Forest, IoW, Chilterns) demand patterns. Drugs spend is structurally small because the paramedic emergency formulary is narrow (c. 30 drugs) and Make Ready replenishment keeps unit cost down. The trust has been on an improvement journey post the 2022-23 CQC findings around culture/governance and the 2023 dispute over historic non-conveyance/handover practices. Drivers include JRCALC paramedic formulary updates, paramedic independent prescribing, naloxone expansion (c. £30/dose, lifesaving overdose-reversal), and Cat-1/Cat-2 demand growth.",
        "sources": [
            {"publisher": "South Central Ambulance Service NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.scas.nhs.uk/about/about-us/publications/"},
            {"publisher": "Care Quality Commission", "title": "South Central Ambulance Service NHS Foundation Trust provider profile (RYE)", "url": "https://www.cqc.org.uk/provider/RYE"},
            {"publisher": "JRCALC / Association of Ambulance Chief Executives", "title": "JRCALC Clinical Guidelines (paramedic formulary)", "url": "https://aace.org.uk/clinical-practice-guidelines/"},
            {"publisher": "UK Government", "title": "Human Medicines Regulations 2012 (Sch 17 paramedic exemption)", "url": "https://www.legislation.gov.uk/uksi/2012/1916/contents"},
            {"publisher": "UK Government", "title": "Misuse of Drugs Regulations 2001", "url": "https://www.legislation.gov.uk/uksi/2001/3998/contents"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"}
        ],
        "related": ["South Central Ambulance Service NHS Foundation Trust", "Clinical Supplies & Drugs", "NHS Ambulance Trusts", "Drugs costs — Yorkshire Ambulance Service NHS Trust", "Drugs costs — London Ambulance Service NHS Trust", "JRCALC"]
    },
    "Termination & post-employment — Yorkshire Ambulance Service NHS Trust": {
        "aliases": [{"name": "Termination & post-employment", "parent": "Yorkshire Ambulance Service NHS Trust"}],
        "description": "YAS's £0.33M termination & post-employment line covers contractual exit costs and post-employment benefit charges recognised under IAS 19 — comprising voluntary-redundancy lump sums (subject to the Public Sector Exit Payments Regulations 2020 thresholds and waivers), early-retirement enhancements where actuarial uplift accrues to the trust, NHS Pension Scheme strain payments triggered by early-release decisions, and contractual notice/PILON payments to leavers. Ambulance trust workforces have a higher early-retirement profile because paramedics qualify for special-class status / mental-health-officer-equivalent enhancements depending on date of joining.",
        "beneficiaries": "Sole 999 emergency-ambulance + 111 integrated provider for the c. 5.5M population of Yorkshire and the Humber; c. 6,500 WTE workforce of paramedics, ECAs, technicians, 111 health advisors, dispatchers and corporate staff operating from c. 60 ambulance stations + Make Ready Centres at Springhill, Doncaster, York and Hull; one of the larger ambulance trusts by headcount and activity.",
        "legal_basis": "IAS 19 Employee Benefits · NHS Pension Scheme Regulations · NHS Terms and Conditions of Service Handbook (Agenda for Change s.16) · Public Sector Exit Payments Regulations 2020 · Pensions (Special Severance Payments) under HMT/DHSC guidance · DHSC GAM 2024-25",
        "key_stats": [
            {"label": "Termination & post-employment 2024-25", "value": "£0.33M"},
            {"label": "Trust profile", "value": "999 emergency ambulance + integrated NHS 111 provider for Yorkshire and the Humber; ~5th-largest ambulance trust by activity"},
            {"label": "Population served", "value": "c. 5.5M residents — West, North, South, East Yorkshire + the Humber"},
            {"label": "Workforce", "value": "c. 6,500 WTE — paramedics, ECAs, technicians, 111 health advisors, dispatchers, corporate"},
            {"label": "Annual demand", "value": "c. 1.0M 999 incidents/yr; c. 1.4M 111 calls/yr"},
            {"label": "Driver", "value": "Voluntary redundancy lump sums + IAS 19 actuarial uplift on early retirement + NHS pension scheme strain payments + PILONs"},
            {"label": "Paramedic pension status", "value": "Pre-2008 entrants accrued under MHO-equivalent special-class status (early retirement at 55); post-2008 reformed scheme; affects strain-payment exposure"},
            {"label": "Industrial action context", "value": "2023-24 paramedic strikes (GMB + Unison) drove churn; some retirement decisions accelerated by the dispute"},
            {"label": "AfC reference", "value": "Section 16 NHS T&Cs Handbook redundancy formula (1 month per year, capped 24 months)"},
            {"label": "Delivery body", "value": "YAS HR + NHS Pensions Agency + NHSBSA + actuarial advisor"},
            {"label": "Policy owner", "value": "DHSC + HMT + NHSE + West Yorkshire / South Yorkshire / Humber and North Yorkshire ICBs"},
            {"label": "Funding trajectory", "value": "Cyclical — rises with restructuring rounds + post-strike workforce churn; generally low in steady state"},
            {"label": "Evaluation evidence", "value": "YAS ARA (remuneration + exit-payment disclosures); CQC provider profile (RX8); NAO public-sector exit-payments reports"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2020 £95k cap regs (revoked 2021) · Successor: ongoing HMT exit-payment guidance + post-strike workforce stabilisation"}
        ],
        "notes": "Ambulance trust termination spend has a distinctive workforce profile: pre-2008 paramedic entrants accrued NHS Pension Scheme benefits under mental-health-officer-equivalent special-class status (allowing retirement from 55), so early-retirement strain payments under IAS 19 disproportionately affect ambulance trusts compared to acute or community providers. The 2023-24 paramedic industrial action (GMB + Unison disputes over pay and conditions) drove additional workforce churn and accelerated some retirement decisions. Drivers include the AfC s.16 redundancy formula, the post-2020 exit-payments framework (the £95k cap was revoked in 2021 but HMT/DHSC retain ministerial-approval for >£100k exits), and ongoing post-strike workforce stabilisation.",
        "sources": [
            {"publisher": "Yorkshire Ambulance Service NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.yas.nhs.uk/about-us/our-publications/annual-reports-and-accounts/"},
            {"publisher": "NHS Employers", "title": "NHS Terms and Conditions of Service Handbook (s.16 redundancy)", "url": "https://www.nhsemployers.org/publications/tchandbook"},
            {"publisher": "NHS Business Services Authority", "title": "NHS Pension Scheme — special class status (paramedics)", "url": "https://www.nhsbsa.nhs.uk/member-hub/your-membership/special-class-status"},
            {"publisher": "IFRS Foundation", "title": "IAS 19 Employee Benefits", "url": "https://www.ifrs.org/issued-standards/list-of-standards/ias-19-employee-benefits/"},
            {"publisher": "HM Treasury", "title": "Guidance on public sector exit payments", "url": "https://www.gov.uk/government/publications/guidance-on-public-sector-exit-payments"},
            {"publisher": "Care Quality Commission", "title": "Yorkshire Ambulance Service NHS Trust provider profile (RX8)", "url": "https://www.cqc.org.uk/provider/RX8"}
        ],
        "related": ["Yorkshire Ambulance Service NHS Trust", "Staff Costs", "NHS Ambulance Trusts", "Termination & post-employment — Kent Community Health NHS Foundation Trust", "Termination & post-employment — London Ambulance Service NHS Trust", "NHS Pension Scheme"]
    },
}
