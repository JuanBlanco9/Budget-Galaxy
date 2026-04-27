# -*- coding: utf-8 -*-
# Phase 2 SCamb (Specialist + Community + Ambulance) — chunk 05 (17 NHS Trust orphan sub-lines)
# Hand-curated trust-specific PROGRAMME-archetype enrichment entries.
# Structural contract per docs/archetype_briefs.md and scripts/hand_curation_briefs/phase2_scamb.md.

NEW = {
    "Social security & levy — Wirral Community Health and Care NHS Foundation Trust": {
        "aliases": [{"name": "Social security & levy", "parent": "Wirral Community Health and Care NHS Foundation Trust"}],
        "description": "Wirral Community Health and Care's £6.18M social-security & levy line is the employer National Insurance Contribution (Class 1 secondary) on the trust's c. 1,500-WTE community-services workforce — district nurses, health visitors, school nurses, community matrons, MSK physios and community-paediatrics teams delivering care across the Wirral peninsula and West Cheshire. The line tracks Agenda for Change pay-bands (mostly Bands 5-6 nursing and AHP), with the April 2025 employer-NIC step-up to 15% above £5k threshold imposing a step-change uplift partially backfilled by Treasury under Autumn Budget 2024 mitigation.",
        "beneficiaries": "c. 1,500 WTE community staff serving a c. 320,000 Wirral + West Cheshire population; community caseload includes c. 120,000 district-nursing contacts/yr, c. 30,000 health-visiting + 0-19 contacts/yr, MSK community physio across c. 20 sites.",
        "legal_basis": "Social Security Contributions and Benefits Act 1992 — National Insurance Contributions Act 2024 (April 2025 employer rate to 15% / threshold £5,000) — NHS Pension Scheme Regulations 2015 (employer contribution) — Agenda for Change pay framework — DHSC Group Accounting Manual 2024-25 — IAS 19 Employee Benefits — NHS Act 2006",
        "key_stats": [
            {"label": "Social security & levy 2024-25", "value": "£6.18M"},
            {"label": "Trust scale", "value": "c. 1,500 WTE community-services workforce; c. 20 community sites across Wirral peninsula"},
            {"label": "Workforce mix", "value": "District nurses, health visitors, school nurses, community matrons, MSK physios, community paediatrics, end-of-life community nursing"},
            {"label": "AfC band concentration", "value": "Predominantly Bands 5-6 (registered nurses + AHPs) with Band 7 specialist roles + Band 4 nursing associates"},
            {"label": "Apr 2025 employer NIC step-up", "value": "Rate 13.8% to 15.0%; threshold £9,100 to £5,000 — c. 1.4 ppt uplift on c. £37M paybill"},
            {"label": "Treasury backfill (HCL repeal context)", "value": "Health and Social Care Levy repealed Nov 2022; Autumn Budget 2024 NHS NIC mitigation — net residual via ICS allocation"},
            {"label": "Funding trajectory", "value": "2021-22 c. £4.7M → 2022-23 c. £5.0M (HCL spike) → 2023-24 c. £5.7M → 2024-25 £6.18M; 2025-26 step uplift +c. £0.5M from NIC reset"},
            {"label": "Delivery body", "value": "Trust HR/Payroll + NHS Business Services Authority (NHSBSA pension admin) + HMRC (RTI PAYE/NIC submission)"},
            {"label": "Policy owner", "value": "HM Treasury (NIC rates) + DHSC (paybill envelope) + NHSE Provider Finance + Cheshire and Merseyside ICB"},
            {"label": "Evaluation evidence", "value": "OBR EFO Mar 2025 (NIC receipts); HMRC RTI submissions; Trust ARA 2023-24; NHSE Operational Plan paybill returns; CQC RY7 inspections"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2022 HCL 1.25 ppt levy (April 2022 - Nov 2022) · Successor: April 2025 NIC step-up + Three Shifts community-lift workforce growth driving long-run baseline"},
            {"label": "Three Shifts community lift", "value": "Darzi Sep 2024 + 10 Year Plan direction-of-travel toward out-of-hospital — paybill expected to grow above CPI"}
        ],
        "notes": "Wirral Community's social-security & levy line is dominated by employer NIC on a workforce-heavy community-services paybill — the trust's cost mix is c. 70% staff costs against the all-NHS provider benchmark of c. 65%, reflecting the labour-intensive district-nursing and health-visiting model. The April 2025 employer-NIC step-up (13.8% to 15.0%, threshold drop £9,100 to £5,000) imposes a structural baseline reset partially backfilled by the Treasury via Autumn Budget 2024 NHS mitigation but with residual ICS-level allocation impact. The Darzi report (Sep 2024) and forthcoming 10 Year Plan Three Shifts policy lifting out-of-hospital care imply paybill growth above CPI, sustaining workforce expansion over the medium term across district nursing and 0-19 services. Cheshire and Merseyside ICB allocations and NHSBSA pension admin frame the operational delivery.",
        "sources": [
            {"publisher": "Wirral Community Health and Care NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.wchc.nhs.uk/about-us/publications/annual-reports/"},
            {"publisher": "HM Revenue & Customs", "title": "National Insurance Contributions rates and thresholds 2025-26", "url": "https://www.gov.uk/government/publications/rates-and-allowances-national-insurance-contributions"},
            {"publisher": "HM Treasury", "title": "Autumn Budget 2024 — Employer NIC and public sector mitigation", "url": "https://www.gov.uk/government/publications/autumn-budget-2024"},
            {"publisher": "Department of Health and Social Care", "title": "The Lord Darzi independent investigation of the NHS in England (Sep 2024)", "url": "https://www.gov.uk/government/publications/independent-investigation-of-the-nhs-in-england"},
            {"publisher": "Care Quality Commission", "title": "Wirral Community Health and Care provider profile (RY7)", "url": "https://www.cqc.org.uk/provider/RY7"}
        ],
        "related": ["Wirral Community Health and Care NHS Foundation Trust", "Staff Costs", "NHS Community Trusts", "Social security & levy — Bridgewater Community Healthcare NHS Foundation Trust", "Social security & levy — Sussex Community NHS Foundation Trust", "HM Revenue & Customs"]
    },
    "Establishment costs — South East Coast Ambulance Service NHS Foundation Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "South East Coast Ambulance Service NHS Foundation Trust"}],
        "description": "South East Coast Ambulance (SECAmb) £6.04M establishment costs covers postage, telephony, mobile-data (CAD-linked vehicle terminals), printing, stationery, recruitment advertising, subscriptions and minor sundries across the trust's c. 110-station hub-and-spoke network spanning Kent, Surrey, Sussex and North-East Hampshire. Heavy mobile-data and CAD/MDT communications spend distinguishes ambulance overhead from acute-trust profiles, with industrial-action 2023-24 paramedic recruitment campaigns and CARE2 cultural-recovery comms feeding 2024-25 spend above pre-pandemic baseline.",
        "beneficiaries": "c. 4,500 WTE staff (paramedics, EMTs, ECAs, call handlers) serving a c. 4.9M population across Kent, Surrey, Sussex and NE Hampshire; c. 985,000 Cat-1/2/3/4 incidents/yr; c. 110 ambulance stations + 3 emergency operations centres (Coxheath, Crawley, Banstead).",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) — IAS 1 Presentation of Financial Statements — NHS Act 2006 — Health and Care Act 2022 — NHS Standard Contract 2024-25 — Civil Contingencies Act 2004 (Cat-1 responder)",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£6.04M"},
            {"label": "Trust scale", "value": "c. 4,500 WTE; c. 110 ambulance stations + 3 EOCs (Coxheath, Crawley, Banstead); c. 4.9M population"},
            {"label": "Annual incidents", "value": "c. 985,000 999 calls / dispatches across Cat-1 (8-min) to Cat-4"},
            {"label": "Composition", "value": "Mobile-data + CAD/MDT comms, postage, telephony, printing, stationery, recruitment advertising, subscriptions, hospitality"},
            {"label": "CAD / MDT spend", "value": "Cleric CAD + mobile-data terminals on c. 600+ vehicles drives recurrent telecoms-establishment cost"},
            {"label": "Industrial action 2023-24", "value": "GMB + Unison paramedic strikes (Dec 2022 - Mar 2023) drove substantive + agency recruitment-advertising spike"},
            {"label": "CQC s.29A warning notice (2022) + recovery", "value": "Post-2022 CQC inspection driving CARE2 cultural-recovery programme — comms + training-materials spend"},
            {"label": "Apr 2025 CPI uplift", "value": "Royal Mail + telecoms + advertising CPI feed forward unit-cost pressure; mobile-data tariff renewals 2024-25"},
            {"label": "Funding trajectory", "value": "2021-22 c. £4.5M → 2023-24 c. £5.6M → 2024-25 £6.04M — sustained recruitment + comms uplift"},
            {"label": "Delivery body", "value": "Trust Corporate Services + Fleet IT + Procurement + (Crown Commercial Service framework for telecoms / EE Blue Light tariff)"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + NHSE Urgent and Emergency Care + DHSC + Kent and Medway / Surrey Heartlands / Sussex / Frimley ICBs (commissioning)"},
            {"label": "Evaluation evidence", "value": "CQC RYD inspections (incl. s.29A 2022 warning notice + 2024 follow-up); ORH ambulance benchmarks; NHSE Ambulance Quality Indicators monthly; Trust ARA 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2017 HSIB Bristol failures + cultural decline · Successor: post-CARE2 cultural-recovery + EE Blue Light Network mobile-data refresh"}
        ],
        "notes": "SECAmb's establishment costs are shaped by the dual demand of a 110-station hub-and-spoke network and the CAD/MDT mobile-data backbone connecting EOCs at Coxheath, Crawley and Banstead — telecoms/data spend is structurally higher than a typical community-trust profile of comparable WTE. Industrial action 2023-24 (paramedic strikes Dec 2022 - Mar 2023) drove agency and substantive recruitment-advertising; the trust remains under post-2022 CQC s.29A warning-notice recovery (CARE2 cultural-recovery programme) which sustains training-materials and internal-comms baseline above peer-trust norms. EE Blue Light Network mobile-data tariff renewals and Royal Mail postage CPI feed forward unit-cost pressure into 2025-26. ICB commissioning is fragmented across Kent and Medway, Surrey Heartlands, Sussex and Frimley with NHSE UEC the primary policy owner.",
        "sources": [
            {"publisher": "South East Coast Ambulance Service NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.secamb.nhs.uk/about-us/publications/annual-reports/"},
            {"publisher": "Care Quality Commission", "title": "South East Coast Ambulance Service provider profile (RYD) — inspection reports", "url": "https://www.cqc.org.uk/provider/RYD"},
            {"publisher": "NHS England", "title": "Ambulance Quality Indicators (AQI) — monthly statistics", "url": "https://www.england.nhs.uk/statistics/statistical-work-areas/ambulance-quality-indicators/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "National Audit Office", "title": "NHS ambulance services (HC 972, 2017 — baseline) and follow-up", "url": "https://www.nao.org.uk/reports/nhs-ambulance-services/"}
        ],
        "related": ["South East Coast Ambulance Service NHS Foundation Trust", "Premises & Infrastructure", "NHS Ambulance Trusts", "Establishment costs — South Central Ambulance Service NHS Foundation Trust", "Establishment costs — Yorkshire Ambulance Service NHS Trust", "NHS England"]
    },
    "Social security & levy — The Royal Orthopaedic Hospital NHS Foundation Trust": {
        "aliases": [{"name": "Social security & levy", "parent": "The Royal Orthopaedic Hospital NHS Foundation Trust"}],
        "description": "The Royal Orthopaedic Hospital (ROH) £5.99M social-security & levy line is the employer National Insurance Contribution (Class 1 secondary) on the trust's c. 1,200-WTE specialist orthopaedic workforce — consultant orthopaedic surgeons, anaesthetists, theatre nurses, MSK physios and radiology staff at the Northfield Birmingham single-site campus. As a single-specialty NHSE specialised-commissioned tertiary centre, the trust carries a high consultant-grade (Bands 8a-9 and AfC equivalent + medical) concentration that lifts average employer NIC per WTE above all-NHS norms.",
        "beneficiaries": "c. 1,200 WTE staff at the single Northfield Birmingham campus; c. 6,000 elective inpatient + day-case orthopaedic procedures/yr (hip, knee, spine, sarcoma, paediatric ortho); supra-regional referral catchment serving West Midlands and beyond.",
        "legal_basis": "Social Security Contributions and Benefits Act 1992 — National Insurance Contributions Act 2024 (April 2025 employer rate to 15% / threshold £5,000) — NHS Pension Scheme Regulations 2015 — Agenda for Change pay framework + medical/dental T&Cs — DHSC Group Accounting Manual 2024-25 — IAS 19 Employee Benefits — NHS Act 2006 (specialised commissioning)",
        "key_stats": [
            {"label": "Social security & levy 2024-25", "value": "£5.99M"},
            {"label": "Trust scale", "value": "Single-site specialist (Bristol Road South, Northfield, Birmingham); c. 1,200 WTE"},
            {"label": "Specialty mix", "value": "Hip / knee / spine / sarcoma / paediatric orthopaedics; supra-regional sarcoma centre"},
            {"label": "Workforce concentration", "value": "High medical + senior AHP ratio (consultant ortho surgeons, theatre nurses, MSK physios, radiographers)"},
            {"label": "Specialised commissioning", "value": "NHSE Specialised Commissioning funded for sarcoma + complex spine; ICB-commissioned for general elective ortho"},
            {"label": "Apr 2025 employer NIC step-up", "value": "Rate 13.8% to 15.0%; threshold £9,100 to £5,000 — c. 1.4 ppt uplift on c. £36M paybill"},
            {"label": "Treasury backfill (HCL repeal context)", "value": "HCL repealed Nov 2022; Autumn Budget 2024 NHS NIC mitigation — net residual via NHSE specialised + ICB allocation"},
            {"label": "Funding trajectory", "value": "2021-22 c. £4.5M → 2022-23 c. £4.9M (HCL spike) → 2023-24 c. £5.6M → 2024-25 £5.99M; 2025-26 step uplift from NIC reset"},
            {"label": "Delivery body", "value": "Trust HR/Payroll + NHS Business Services Authority (NHSBSA pension admin) + HMRC (RTI PAYE/NIC submission)"},
            {"label": "Policy owner", "value": "HM Treasury (NIC rates) + NHSE Specialised Commissioning + DHSC + Birmingham and Solihull ICB"},
            {"label": "Evaluation evidence", "value": "GIRFT orthopaedic deep-dive 2015 + refresh; CQC RRJ inspections; NHSE Specialised Commissioning service specs; Trust ARA 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2022 HCL 1.25 ppt levy · Successor: April 2025 NIC step-up + GIRFT high-volume low-complexity (HVLC) hub model expansion"}
        ],
        "notes": "ROH's social-security & levy is shaped by a high-consultant-density single-specialty workforce — orthopaedic surgeons, anaesthetists and theatre-nursing concentrations push the average employer NIC per WTE above all-NHS provider norms. The April 2025 employer-NIC step-up (13.8% to 15.0%, threshold £9,100 to £5,000) imposes a structural baseline reset partially backfilled by Autumn Budget 2024 NHS mitigation but carried partly via NHSE Specialised Commissioning and Birmingham and Solihull ICB allocations. The GIRFT high-volume low-complexity (HVLC) elective-hub model — for which ROH is a flagship surgical hub — is driving sustained workforce expansion to clear the elective backlog, lifting paybill above CPI through the medium term. Sarcoma and complex spine workload sits under NHSE specialised-commissioning service specifications.",
        "sources": [
            {"publisher": "The Royal Orthopaedic Hospital NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.roh.nhs.uk/about-us/publications"},
            {"publisher": "HM Revenue & Customs", "title": "National Insurance Contributions rates and thresholds 2025-26", "url": "https://www.gov.uk/government/publications/rates-and-allowances-national-insurance-contributions"},
            {"publisher": "HM Treasury", "title": "Autumn Budget 2024 — Employer NIC and public sector mitigation", "url": "https://www.gov.uk/government/publications/autumn-budget-2024"},
            {"publisher": "Getting It Right First Time (GIRFT)", "title": "Orthopaedics — High Volume Low Complexity programme", "url": "https://gettingitrightfirsttime.co.uk/surgical_specialties/orthopaedic-surgery/"},
            {"publisher": "Care Quality Commission", "title": "The Royal Orthopaedic Hospital provider profile (RRJ)", "url": "https://www.cqc.org.uk/provider/RRJ"}
        ],
        "related": ["The Royal Orthopaedic Hospital NHS Foundation Trust", "Staff Costs", "NHS Specialist Trusts", "Social security & levy — Royal National Orthopaedic Hospital NHS Trust", "Social security & levy — The Robert Jones and Agnes Hunt Orthopaedic Hospital NHS Foundation Trust", "NHS England"]
    },
    "Social security & levy — Queen Victoria Hospital NHS Foundation Trust": {
        "aliases": [{"name": "Social security & levy", "parent": "Queen Victoria Hospital NHS Foundation Trust"}],
        "description": "Queen Victoria Hospital (QVH East Grinstead) £5.97M social-security & levy line is the employer National Insurance Contribution (Class 1 secondary) on the trust's c. 950-WTE specialist reconstructive-surgery workforce — plastic, hand, oral & maxillofacial, head & neck, ophthalmic and corneo-plastic surgeons together with specialist theatre, burns and ITU nursing. As the historic 'McIndoe' burns and reconstructive centre, the trust runs a high consultant-density single-specialty paybill served via NHSE specialised commissioning for burns and complex reconstruction.",
        "beneficiaries": "c. 950 WTE staff at the single East Grinstead site; supra-regional reconstructive-surgery referral catchment across Sussex, Kent, Surrey and SE London; c. 18,000 elective + day-case operations/yr; specialist NHSE-commissioned burns + corneo-plastic centre.",
        "legal_basis": "Social Security Contributions and Benefits Act 1992 — National Insurance Contributions Act 2024 (April 2025 employer rate to 15% / threshold £5,000) — NHS Pension Scheme Regulations 2015 — Agenda for Change + medical/dental T&Cs — DHSC Group Accounting Manual 2024-25 — IAS 19 Employee Benefits — NHS Act 2006 (specialised commissioning)",
        "key_stats": [
            {"label": "Social security & levy 2024-25", "value": "£5.97M"},
            {"label": "Trust scale", "value": "Single-site specialist (Holtye Road, East Grinstead); c. 950 WTE"},
            {"label": "Specialty mix", "value": "Plastic / hand / OMF / head & neck / ophthalmic / corneo-plastic / burns / sleep / ITU"},
            {"label": "Heritage", "value": "Sir Archibald McIndoe WWII 'Guinea Pig Club' burns + reconstructive heritage; listed-site constraints"},
            {"label": "Specialised commissioning", "value": "NHSE Specialised Commissioning for burns + complex reconstruction; ICB-commissioned for elective plastics + ophthalmic"},
            {"label": "Apr 2025 employer NIC step-up", "value": "Rate 13.8% to 15.0%; threshold £9,100 to £5,000 — c. 1.4 ppt uplift on c. £36M paybill"},
            {"label": "Treasury backfill (HCL repeal context)", "value": "HCL repealed Nov 2022; Autumn Budget 2024 NHS NIC mitigation — residual via NHSE specialised + Sussex ICB allocation"},
            {"label": "Funding trajectory", "value": "2021-22 c. £4.5M → 2022-23 c. £4.9M (HCL spike) → 2023-24 c. £5.6M → 2024-25 £5.97M; 2025-26 step uplift from NIC reset"},
            {"label": "Delivery body", "value": "Trust HR/Payroll + NHS Business Services Authority (NHSBSA pension admin) + HMRC (RTI PAYE/NIC submission)"},
            {"label": "Policy owner", "value": "HM Treasury (NIC rates) + NHSE Specialised Commissioning + DHSC + Sussex ICB"},
            {"label": "Evaluation evidence", "value": "CQC RPC inspections; NHSE Specialised Burns Service specifications; GIRFT plastics deep-dive; Trust ARA 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2022 HCL 1.25 ppt levy · Successor: April 2025 NIC step-up + ongoing NHSE Burns Service Review remodel"}
        ],
        "notes": "QVH's social-security & levy is concentrated on a small but consultant-dense single-specialty paybill — plastic, hand, OMF, ophthalmic and corneo-plastic surgeons together with specialist theatre and burns nursing push the average employer NIC per WTE above all-NHS norms despite the trust's modest absolute size. The April 2025 employer-NIC step-up (13.8% to 15.0%, threshold £9,100 to £5,000) imposes a baseline reset partially backfilled via Autumn Budget 2024 NHS mitigation, with residual carried via NHSE Specialised Commissioning (burns) and Sussex ICB allocations. The historic Sir Archibald McIndoe burns heritage shapes the listed-site campus while the NHSE National Burns Service review trajectory and elective-recovery hub status (GIRFT plastics) drive sustained workforce expansion. Recruitment of corneo-plastic and OMF consultants is a long-running national-shortage challenge.",
        "sources": [
            {"publisher": "Queen Victoria Hospital NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.qvh.nhs.uk/about-us/publications/"},
            {"publisher": "HM Revenue & Customs", "title": "National Insurance Contributions rates and thresholds 2025-26", "url": "https://www.gov.uk/government/publications/rates-and-allowances-national-insurance-contributions"},
            {"publisher": "HM Treasury", "title": "Autumn Budget 2024 — Employer NIC and public sector mitigation", "url": "https://www.gov.uk/government/publications/autumn-budget-2024"},
            {"publisher": "NHS England", "title": "Specialised Burns Service — service specification", "url": "https://www.england.nhs.uk/commissioning/spec-services/npc-crg/group-d/d06/"},
            {"publisher": "Care Quality Commission", "title": "Queen Victoria Hospital provider profile (RPC)", "url": "https://www.cqc.org.uk/provider/RPC"}
        ],
        "related": ["Queen Victoria Hospital NHS Foundation Trust", "Staff Costs", "NHS Specialist Trusts", "Social security & levy — The Royal Orthopaedic Hospital NHS Foundation Trust", "Social security & levy — Liverpool Heart and Chest Hospital NHS Foundation Trust", "NHS England"]
    },
    "Transport (business + patient) — Great Ormond Street Hospital for Children NHS Foundation Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "Great Ormond Street Hospital for Children NHS Foundation Trust"}],
        "description": "Great Ormond Street Hospital (GOSH) £5.85M transport line covers business mileage (AfC Section 17 + AMAP), pool-fleet IFRS 16 leases, paediatric inter-hospital retrieval transport (CATS — Children's Acute Transport Service), non-emergency patient transport for clinic attendance, accommodation/travel reimbursement for families of long-stay patients and outreach-team mileage. As a national/international tertiary paediatric specialist with a supra-regional referral catchment, transport spend is structurally elevated by long-distance patient and family travel and the CATS retrieval service.",
        "beneficiaries": "c. 5,500 WTE staff at the Bloomsbury and Frontage Road campuses; c. 280,000 patient visits/yr; supra-regional + international paediatric tertiary referral catchment; CATS service runs c. 3,000 paediatric retrievals/yr across North Thames region.",
        "legal_basis": "NHS Act 2006 — NHSE Patient Transport Services Eligibility Criteria — Agenda for Change Section 17 (business mileage) — HMRC AMAP rates — IFRS 16 Leases (pool fleet) — DHSC Group Accounting Manual 2024-25 — Health and Care Act 2022 — NHSE Specialised Commissioning service specs (paediatric retrieval / CATS)",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£5.85M"},
            {"label": "Trust scale", "value": "Two-site Bloomsbury London; c. 5,500 WTE; c. 280,000 patient visits/yr"},
            {"label": "Supra-regional reach", "value": "National/international paediatric tertiary; long-distance referral travel for families"},
            {"label": "CATS — Children's Acute Transport Service", "value": "c. 3,000 paediatric ICU retrievals/yr across North Thames; lease-based ambulance + helicopter dependency"},
            {"label": "Composition", "value": "Business mileage (AfC S17 + AMAP 45p/25p) + IFRS 16 pool-fleet leases + CATS retrieval ops + family travel reimbursement + outreach"},
            {"label": "AMAP rate context", "value": "HMRC AMAP rate frozen at 45p/mile (first 10k miles) since 2011 — real-terms erosion"},
            {"label": "Industrial action 2023-24 effect", "value": "Junior-doctor + consultant strikes drove cancellation rebooking patient travel + agency travel claims"},
            {"label": "April 2025 NIC + fuel CPI", "value": "Diesel CPI feed forward unit-cost pressure; NEPTS contractor pass-through"},
            {"label": "Funding trajectory", "value": "2021-22 c. £4.6M → 2023-24 c. £5.4M → 2024-25 £5.85M — fuel CPI + CATS expansion + family-travel growth"},
            {"label": "Delivery body", "value": "Trust E&F + CATS retrieval team + outsourced NEPTS provider (London region) + pool-fleet leasing partner + Trust HR (mileage)"},
            {"label": "Policy owner", "value": "NHSE Specialised Commissioning (paediatric retrieval) + NHSE UEC (NEPTS) + DHSC + North Central London ICB"},
            {"label": "Evaluation evidence", "value": "NAO NEPTS 2019; CQC RP4 inspections; NHSE Paediatric Critical Care Service spec; CATS Annual Report; Trust ARA 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2021 NEPTS eligibility regime · Successor: post-NHP-era new-build paediatric estate at GOSH (Sight & Sound Centre baseline) + electrified pool-fleet refresh"}
        ],
        "notes": "GOSH's transport line is structurally elevated by its national/international paediatric-tertiary referral profile — long-distance patient and family travel, accommodation reimbursement for long-stay paediatric admissions and the CATS retrieval service together push the line well above an acute trust of comparable WTE. CATS (Children's Acute Transport Service) runs c. 3,000 paediatric ICU retrievals/yr across the North Thames region under NHSE Specialised Commissioning, with lease-based ambulance fleet and helicopter dependency. The HMRC AMAP-rate freeze (45p/mile since 2011) sustains internal-mileage rate-dispute pressure. Industrial action 2023-24 drove cancellation-rebooking patient-travel volume and agency travel claims. NHSE NEPTS Eligibility Criteria 2021 govern the patient-funded transport portion.",
        "sources": [
            {"publisher": "Great Ormond Street Hospital for Children NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.gosh.nhs.uk/about-us/our-corporate-information/annual-reports-and-accounts/"},
            {"publisher": "Children's Acute Transport Service (CATS)", "title": "Annual Report — paediatric ICU retrieval activity", "url": "https://www.cats.nhs.uk/"},
            {"publisher": "NHS England", "title": "Non-Emergency Patient Transport Services — National Framework + Eligibility Criteria 2021", "url": "https://www.england.nhs.uk/publication/non-emergency-patient-transport-services-nepts/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Great Ormond Street Hospital provider profile (RP4)", "url": "https://www.cqc.org.uk/provider/RP4"}
        ],
        "related": ["Great Ormond Street Hospital for Children NHS Foundation Trust", "Premises & Infrastructure", "NHS Specialist Trusts", "Business rates — Great Ormond Street Hospital for Children NHS Foundation Trust", "Transport (business + patient) — The Royal Marsden NHS Foundation Trust", "NHS England"]
    },
    "Establishment costs — South Central Ambulance Service NHS Foundation Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "South Central Ambulance Service NHS Foundation Trust"}],
        "description": "South Central Ambulance Service (SCAS) £5.70M establishment costs covers postage, telephony, mobile-data (CAD/MDT vehicle terminals), printing, stationery, recruitment advertising, subscriptions and minor sundries across the trust's c. 70-station hub-and-spoke network spanning Berkshire, Buckinghamshire, Hampshire and Oxfordshire and the integrated NHS 111 service. Heavy 111-clinical-assessment-service (CAS) telecoms spend distinguishes SCAS overhead from peer ambulance trusts that do not host 111.",
        "beneficiaries": "c. 4,200 WTE staff (paramedics, EMTs, ECAs, 999 call handlers, 111 health advisers + clinicians) serving a c. 4M population across Thames Valley + Hampshire; c. 800,000 999 incidents/yr + c. 2.4M 111 calls/yr; c. 70 ambulance stations + 2 EOCs (Bicester, Otterbourne).",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) — IAS 1 Presentation of Financial Statements — NHS Act 2006 — Health and Care Act 2022 — NHS Standard Contract 2024-25 — Civil Contingencies Act 2004 (Cat-1 responder)",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£5.70M"},
            {"label": "Trust scale", "value": "c. 4,200 WTE; c. 70 ambulance stations + 2 EOCs (Bicester, Otterbourne); integrated 111 service"},
            {"label": "Annual demand", "value": "c. 800,000 999 incidents + c. 2.4M 111 calls/yr"},
            {"label": "Composition", "value": "Mobile-data + CAD/MDT + 111 telephony, postage, printing, stationery, recruitment advertising, subscriptions"},
            {"label": "111 integrated service", "value": "SCAS hosts 111 + Clinical Assessment Service for Thames Valley + Hampshire — telephony spend higher than peer ambulance trust"},
            {"label": "Industrial action 2023-24", "value": "GMB + Unison paramedic strikes drove substantive + agency recruitment-advertising spike"},
            {"label": "CAD / MDT spend", "value": "Cleric CAD + mobile-data terminals on c. 450+ vehicles; EE Blue Light tariff renewals"},
            {"label": "Apr 2025 CPI uplift", "value": "Royal Mail + telecoms + advertising CPI feed forward unit-cost pressure"},
            {"label": "Funding trajectory", "value": "2021-22 c. £4.3M → 2023-24 c. £5.3M → 2024-25 £5.70M — sustained recruitment + 111 expansion"},
            {"label": "Delivery body", "value": "Trust Corporate Services + Fleet IT + 111/CAS Operations + Procurement + (Crown Commercial Service framework for telecoms / EE Blue Light)"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + NHSE Urgent and Emergency Care + DHSC + Buckinghamshire, Oxfordshire and Berkshire West (BOB) / Hampshire and IoW / Frimley ICBs"},
            {"label": "Evaluation evidence", "value": "CQC RYE inspections; NHSE Ambulance Quality Indicators monthly; NHSE Integrated Urgent Care reports; ORH ambulance benchmarks; Trust ARA 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2019 separate 111 / 999 contract baseline · Successor: NHSE Integrated Urgent Care + Cat-2 segmentation reform 2024-25"}
        ],
        "notes": "SCAS's establishment-costs profile carries a distinct telephony+telecoms loading because the trust hosts the integrated 111 / Clinical Assessment Service for Thames Valley + Hampshire alongside its 999 ambulance operation — twin call-centre demand pushes telecoms spend above peer ambulance-only trusts. Industrial action 2023-24 (paramedic strikes) drove substantive and agency recruitment-advertising spend; the trust ran high-profile NHS-staff retention campaigns through 2024. EE Blue Light Network mobile-data tariff renewals and Royal Mail postage CPI feed forward unit-cost pressure into 2025-26. ICB commissioning is fragmented across BOB, Hampshire and IoW, and Frimley with NHSE UEC the primary policy owner; the Cat-2 segmentation reform 2024-25 is reshaping operational comms and training-materials baseline.",
        "sources": [
            {"publisher": "South Central Ambulance Service NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.scas.nhs.uk/about-scas/publications/"},
            {"publisher": "Care Quality Commission", "title": "South Central Ambulance Service provider profile (RYE)", "url": "https://www.cqc.org.uk/provider/RYE"},
            {"publisher": "NHS England", "title": "Ambulance Quality Indicators (AQI) — monthly statistics", "url": "https://www.england.nhs.uk/statistics/statistical-work-areas/ambulance-quality-indicators/"},
            {"publisher": "NHS England", "title": "Integrated Urgent Care service specification (111/CAS)", "url": "https://www.england.nhs.uk/publication/integrated-urgent-care-service-specification/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"}
        ],
        "related": ["South Central Ambulance Service NHS Foundation Trust", "Premises & Infrastructure", "NHS Ambulance Trusts", "Establishment costs — South East Coast Ambulance Service NHS Foundation Trust", "Establishment costs — Yorkshire Ambulance Service NHS Trust", "NHS England"]
    },
    "General supplies & services — Birmingham Community Healthcare NHS Foundation Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "Birmingham Community Healthcare NHS Foundation Trust"}],
        "description": "Birmingham Community Healthcare (BCHC) £5.65M general supplies & services line covers non-pay clinical and operational consumables for the trust's community-services portfolio across Birmingham — wound-care dressings, continence pads, sterile-services, MSK exercise consumables, dental clinic instruments, school-nursing public-health supplies and laundry/linen — plus learning-disability inpatient unit and specialist community-paediatric clinic stock. The portfolio runs through NHS Supply Chain Health, Care and Community Services tower with elements of trust-direct procurement.",
        "beneficiaries": "c. 5,000 WTE staff serving a c. 1.2M Birmingham + Solihull population through community sites; community-dental, MSK, district-nursing, health-visiting, school-nursing, community-paediatric and learning-disability inpatient services; c. 100+ community sites including Moseley Hall Hospital, West Heath Hospital and West Midlands Rehab Centre.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) — IAS 2 Inventories (interaction) — NHS Act 2006 — Health and Care Act 2022 — NHS Standard Contract 2024-25 — Public Contracts Regulations 2015 / Procurement Act 2023",
        "key_stats": [
            {"label": "General supplies & services 2024-25", "value": "£5.65M"},
            {"label": "Trust scale", "value": "c. 5,000 WTE; c. 100+ community sites; Birmingham + Solihull catchment c. 1.2M"},
            {"label": "Service mix", "value": "District nursing, health visiting, school nursing, community dental, MSK, community paeds, LD inpatient, prison healthcare"},
            {"label": "Composition", "value": "Wound-care dressings, continence pads, sterile-services, dental instruments, MSK consumables, laundry/linen, school-nursing public-health stock"},
            {"label": "Procurement vehicle", "value": "NHS Supply Chain Health, Care and Community Services tower + trust-direct procurement under Procurement Act 2023"},
            {"label": "Three Shifts community lift", "value": "Darzi Sep 2024 + 10 Year Plan direction toward out-of-hospital — consumables baseline expected to grow above CPI"},
            {"label": "Apr 2025 employer NIC step-up", "value": "Indirect via supplier pass-through cost; inflation pressure on consumables tendered 2024-25"},
            {"label": "Continence + wound-care drivers", "value": "Frailty + ageing population drive sustained growth in community continence + wound-care dressing volumes"},
            {"label": "Funding trajectory", "value": "2021-22 c. £4.5M → 2023-24 c. £5.3M → 2024-25 £5.65M — sustained CPI + caseload growth"},
            {"label": "Delivery body", "value": "Trust Procurement + NHS Supply Chain (Health, Care and Community tower) + Trust Pharmacy/Stores + community-services management"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + NHSE Community Services Improvement + DHSC + Birmingham and Solihull ICB"},
            {"label": "Evaluation evidence", "value": "CQC RYW inspections; NHSE Community Services Statistics; Model Hospital community benchmark; Trust ARA 2023-24; NAO Adult community health services 2020"},
            {"label": "Predecessor / successor", "value": "Predecessor: Heart of England + South Central CIC pre-2011 split · Successor: Three Shifts community lift + LMNS/community-paeds reconfiguration"}
        ],
        "notes": "BCHC's general supplies & services is a workforce-multiplied consumables line — district nurses, health visitors, MSK physios and community-dental teams across c. 100+ sites generate a high-throughput, low-unit-cost stock profile dominated by wound-care dressings, continence pads and sterile dental instruments. NHS Supply Chain's Health, Care and Community Services tower is the primary procurement vehicle, with trust-direct procurement under the Procurement Act 2023 (in force 24 Feb 2025) for non-tower categories. The Darzi report (Sep 2024) and 10 Year Plan Three Shifts policy lifting out-of-hospital care imply consumables baseline growth above CPI, sustained by population frailty + continence + wound-care demand. Birmingham and Solihull ICB allocations frame the operational envelope.",
        "sources": [
            {"publisher": "Birmingham Community Healthcare NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.bhamcommunity.nhs.uk/about-us/publications/"},
            {"publisher": "NHS Supply Chain", "title": "Health, Care and Community Services category tower", "url": "https://www.supplychain.nhs.uk/categories/health-care-and-community-services/"},
            {"publisher": "Department of Health and Social Care", "title": "The Lord Darzi independent investigation of the NHS in England (Sep 2024)", "url": "https://www.gov.uk/government/publications/independent-investigation-of-the-nhs-in-england"},
            {"publisher": "Cabinet Office", "title": "Procurement Act 2023 — guidance and commencement (24 Feb 2025)", "url": "https://www.gov.uk/government/collections/procurement-act-2023-guidance-documents"},
            {"publisher": "Care Quality Commission", "title": "Birmingham Community Healthcare provider profile (RYW)", "url": "https://www.cqc.org.uk/provider/RYW"}
        ],
        "related": ["Birmingham Community Healthcare NHS Foundation Trust", "Clinical Supplies & Drugs", "NHS Community Trusts", "Social security & levy — Birmingham Community Healthcare NHS Foundation Trust", "General supplies & services — Central London Community Healthcare NHS Trust", "NHS Supply Chain"]
    },
    "Lease expenditure — West Midlands Ambulance Service University NHS Foundation Trust": {
        "aliases": [{"name": "Lease expenditure", "parent": "West Midlands Ambulance Service University NHS Foundation Trust"}],
        "description": "West Midlands Ambulance Service (WMAS) £5.61M lease expenditure line is the IFRS 16 right-of-use lease cost on the trust's c. 90+ ambulance station and Make Ready Centre estate (largely leased from NHS Property Services or local authority landlords) plus pool-fleet vehicles and CAD/IT hardware leases. Following IFRS 16 adoption from 2022-23 (HM Treasury FReM application), operating-lease commitments transitioned to balance-sheet right-of-use assets with corresponding interest + depreciation lease expense.",
        "beneficiaries": "c. 7,000 WTE staff (paramedics, EMTs, ECAs, call handlers) serving a c. 5.9M population across the West Midlands; c. 1.2M 999 incidents/yr; c. 90+ stations / hubs / Make Ready Centres; 3 EOCs (Stafford, Brierley Hill, Tollgate Coventry).",
        "legal_basis": "IFRS 16 Leases (HM Treasury FReM application 2022-23) — DHSC Group Accounting Manual 2024-25 ch.7 — Landlord and Tenant Act 1954 (landlord/tenant) — NHS Act 2006 — Health and Care Act 2022 — NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "Lease expenditure 2024-25", "value": "£5.61M"},
            {"label": "Trust scale", "value": "c. 7,000 WTE; c. 90+ stations / hubs / Make Ready Centres; 3 EOCs (Stafford, Brierley Hill, Tollgate Coventry)"},
            {"label": "Annual demand", "value": "c. 1.2M 999 incidents across c. 5.9M population (Birmingham, Black Country, Coventry, Warwickshire, Staffordshire, Hereford & Worcester, Shropshire)"},
            {"label": "Composition", "value": "IFRS 16 right-of-use leases — ambulance stations + MRCs (NHSPS / LA landlords) + pool-fleet vehicles + CAD/IT hardware"},
            {"label": "Make Ready Centre model", "value": "WMAS pioneered MRC hub-and-spoke model — fewer larger centres + more remote response posts; underpins lease-portfolio shape"},
            {"label": "IFRS 16 adoption", "value": "From 2022-23 (HM Treasury FReM) — operating leases moved on-balance-sheet as RoU assets + lease liabilities"},
            {"label": "NHSPS landlord exposure", "value": "Significant proportion of station portfolio leased from NHS Property Services with subjected market-rent reviews"},
            {"label": "Industrial action 2023-24 effect", "value": "Strikes drove minor pool-fleet wear lift; lease portfolio largely unaffected directly"},
            {"label": "Funding trajectory", "value": "2021-22 c. £1.5M (pre-IFRS 16) → 2022-23 c. £5.0M (IFRS 16 step-up) → 2023-24 c. £5.4M → 2024-25 £5.61M"},
            {"label": "Delivery body", "value": "Trust Estates + Fleet + (NHS Property Services landlord) + Local Authorities (landlord) + leasing partner"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + HM Treasury (FReM/IFRS 16) + Black Country / Birmingham and Solihull / Coventry and Warwickshire / Staffordshire and Stoke / Herefordshire and Worcestershire / Shropshire ICBs"},
            {"label": "Evaluation evidence", "value": "CQC RYA inspections (rated Outstanding 2017-2022); ORH ambulance benchmarks; NHSE AQI monthly; Trust ARA 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-IFRS 16 operating-lease off-balance-sheet treatment · Successor: ambulance fleet electrification + MRC consolidation + NHSPS market-rent revaluations"}
        ],
        "notes": "WMAS pioneered the Make Ready Centre (MRC) hub-and-spoke model — a smaller number of larger centralised vehicle-prep + decontamination + crewing hubs combined with remote response posts — which shapes the trust's lease portfolio toward fewer, larger NHSPS-leased buildings plus a wide network of micro-stations. IFRS 16 adoption from 2022-23 (HM Treasury FReM) recognised c. 90+ station leases as right-of-use assets with corresponding lease expense, driving the step-up from c. £1.5M pre-IFRS 16 to the current c. £5.6M baseline. Pool-fleet IFRS 16 leases account for a smaller share. Ambulance fleet electrification (NHS Net Zero Plan 2040 trajectory) and NHSPS market-rent revaluations are the key forward drivers.",
        "sources": [
            {"publisher": "West Midlands Ambulance Service University NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://wmas.nhs.uk/about-us/publications/"},
            {"publisher": "HM Treasury", "title": "Financial Reporting Manual (FReM) 2022-23 — IFRS 16 application", "url": "https://www.gov.uk/government/collections/government-financial-reporting-manual-frem"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (ch.7 Leases)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS Property Services", "title": "Tenant strategy and market-rent policy", "url": "https://www.property.nhs.uk/"},
            {"publisher": "Care Quality Commission", "title": "West Midlands Ambulance Service provider profile (RYA)", "url": "https://www.cqc.org.uk/provider/RYA"}
        ],
        "related": ["West Midlands Ambulance Service University NHS Foundation Trust", "Premises & Infrastructure", "NHS Ambulance Trusts", "Lease expenditure — South Central Ambulance Service NHS Foundation Trust", "Lease expenditure — Yorkshire Ambulance Service NHS Trust", "NHS Property Services"]
    },
    "Social security & levy — Shropshire Community Health NHS Trust": {
        "aliases": [{"name": "Social security & levy", "parent": "Shropshire Community Health NHS Trust"}],
        "description": "Shropshire Community Health (SCHT) £5.60M social-security & levy line is the employer National Insurance Contribution (Class 1 secondary) on the trust's c. 1,400-WTE rural-community workforce — district nurses, health visitors, school nurses, MSK community physios, community-paediatric teams and the Bridgnorth and Whitchurch community-hospital nursing staff. The line tracks Agenda for Change pay-bands (predominantly Bands 5-6) across a sparsely populated rural Shropshire and Telford catchment, with the April 2025 employer-NIC step-up driving a structural baseline reset.",
        "beneficiaries": "c. 1,400 WTE community staff serving a c. 500,000 Shropshire + Telford and Wrekin population; c. 90,000 district-nursing contacts/yr; community-hospital inpatient beds at Bridgnorth, Whitchurch, Ludlow; rural-coverage MSK + community-paediatric services across c. 30+ sites.",
        "legal_basis": "Social Security Contributions and Benefits Act 1992 — National Insurance Contributions Act 2024 (April 2025 employer rate to 15% / threshold £5,000) — NHS Pension Scheme Regulations 2015 — Agenda for Change pay framework — DHSC Group Accounting Manual 2024-25 — IAS 19 Employee Benefits — NHS Act 2006",
        "key_stats": [
            {"label": "Social security & levy 2024-25", "value": "£5.60M"},
            {"label": "Trust scale", "value": "c. 1,400 WTE rural-community workforce; c. 30+ community sites; community hospitals at Bridgnorth, Whitchurch, Ludlow"},
            {"label": "Catchment", "value": "c. 500,000 Shropshire + Telford and Wrekin (highly rural, low population density)"},
            {"label": "Workforce mix", "value": "District nurses, health visitors, school nurses, community-hospital ward nursing, MSK physios, community paeds, end-of-life community"},
            {"label": "AfC band concentration", "value": "Predominantly Bands 5-6 with Band 4 nursing associates + Band 7 specialist roles; rural-mileage AfC s.17 supplements"},
            {"label": "Apr 2025 employer NIC step-up", "value": "Rate 13.8% to 15.0%; threshold £9,100 to £5,000 — c. 1.4 ppt uplift on c. £35M paybill"},
            {"label": "Rural-recruitment premium", "value": "Significant rural recruitment-and-retention premium drives paybill uplift versus urban peers; reliance on bank + agency"},
            {"label": "Treasury backfill (HCL repeal context)", "value": "HCL repealed Nov 2022; Autumn Budget 2024 NHS NIC mitigation — net residual via Shropshire, Telford and Wrekin ICB allocation"},
            {"label": "Funding trajectory", "value": "2021-22 c. £4.3M → 2022-23 c. £4.6M (HCL spike) → 2023-24 c. £5.2M → 2024-25 £5.60M; 2025-26 step uplift from NIC reset"},
            {"label": "Delivery body", "value": "Trust HR/Payroll + NHS Business Services Authority (NHSBSA pension admin) + HMRC (RTI PAYE/NIC submission)"},
            {"label": "Policy owner", "value": "HM Treasury (NIC rates) + DHSC (paybill envelope) + NHSE Provider Finance + Shropshire, Telford and Wrekin ICB"},
            {"label": "Evaluation evidence", "value": "CQC RXW inspections; NHSE Community Services Statistics; OBR EFO Mar 2025 (NIC receipts); Trust ARA 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2022 HCL 1.25 ppt levy · Successor: April 2025 NIC step-up + Three Shifts community-lift workforce growth + potential STW NHS reconfiguration"}
        ],
        "notes": "SCHT's social-security & levy is dominated by employer NIC on a workforce-heavy rural-community paybill — district nurses, health visitors and community-hospital nursing teams across a sparsely populated Shropshire and Telford and Wrekin catchment. Rural recruitment-and-retention premium (geographical isolation, travel distances, limited workforce supply locally) sustains a paybill structurally elevated above urban community-trust peers, with bank and agency reliance further lifting employer-NIC liability. The April 2025 employer-NIC step-up (13.8% to 15.0%, threshold £9,100 to £5,000) imposes a baseline reset partially backfilled by Autumn Budget 2024 mitigation. The Darzi Three Shifts policy lifting out-of-hospital care and the long-running Shropshire, Telford and Wrekin (STW) acute-services reconfiguration are forward drivers of community-paybill expansion.",
        "sources": [
            {"publisher": "Shropshire Community Health NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.shropscommunityhealth.nhs.uk/our-publications"},
            {"publisher": "HM Revenue & Customs", "title": "National Insurance Contributions rates and thresholds 2025-26", "url": "https://www.gov.uk/government/publications/rates-and-allowances-national-insurance-contributions"},
            {"publisher": "HM Treasury", "title": "Autumn Budget 2024 — Employer NIC and public sector mitigation", "url": "https://www.gov.uk/government/publications/autumn-budget-2024"},
            {"publisher": "Department of Health and Social Care", "title": "The Lord Darzi independent investigation of the NHS in England (Sep 2024)", "url": "https://www.gov.uk/government/publications/independent-investigation-of-the-nhs-in-england"},
            {"publisher": "Care Quality Commission", "title": "Shropshire Community Health provider profile (RXW)", "url": "https://www.cqc.org.uk/provider/RXW"}
        ],
        "related": ["Shropshire Community Health NHS Trust", "Staff Costs", "NHS Community Trusts", "Social security & levy — Wirral Community Health and Care NHS Foundation Trust", "Social security & levy — Hertfordshire Community NHS Trust", "HM Revenue & Customs"]
    },
    "General supplies & services — Lincolnshire Community Health Services NHS Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "Lincolnshire Community Health Services NHS Trust"}],
        "description": "Lincolnshire Community Health Services (LCHS) £5.53M general supplies & services line covers non-pay clinical and operational consumables for the trust's rural community-services portfolio across Lincolnshire — wound-care dressings, continence pads, sterile-services for community-clinic minor procedures, MSK exercise consumables, school-nursing public-health supplies, podiatry consumables and laundry/linen — plus community-hospital inpatient unit stock at Skegness, Louth, Boston and Stamford. Procurement runs through NHS Supply Chain Health, Care and Community Services tower with trust-direct contracts for rural-specific categories.",
        "beneficiaries": "c. 2,500 WTE staff serving a c. 770,000 Lincolnshire population across one of England's most rural counties; community caseload includes wound-care, district nursing, health visiting, school nursing, MSK, podiatry, community paediatrics; community-hospital inpatient beds at Skegness, Louth, Boston, Stamford and rural sites.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) — IAS 2 Inventories (interaction) — NHS Act 2006 — Health and Care Act 2022 — NHS Standard Contract 2024-25 — Public Contracts Regulations 2015 / Procurement Act 2023",
        "key_stats": [
            {"label": "General supplies & services 2024-25", "value": "£5.53M"},
            {"label": "Trust scale", "value": "c. 2,500 WTE; rural community-services across c. 60+ sites in Lincolnshire"},
            {"label": "Catchment", "value": "c. 770,000 Lincolnshire population — one of England's most rural counties; long travel distances"},
            {"label": "Service mix", "value": "Wound-care, district nursing, HV, school nursing, MSK, podiatry, comm paeds + community-hospital inpatient (Skegness, Louth, Boston, Stamford)"},
            {"label": "Composition", "value": "Wound-care dressings, continence pads, sterile-services, MSK + podiatry consumables, community-hospital ward stock, laundry/linen, public-health stock"},
            {"label": "Procurement vehicle", "value": "NHS Supply Chain Health, Care and Community Services tower + trust-direct procurement under Procurement Act 2023"},
            {"label": "Three Shifts community lift", "value": "Darzi Sep 2024 + 10 Year Plan direction toward out-of-hospital — consumables baseline expected to grow above CPI"},
            {"label": "Apr 2025 CPI uplift", "value": "Royal Mail + supplier pass-through inflation; consumables tendered 2024-25"},
            {"label": "Funding trajectory", "value": "2021-22 c. £4.4M → 2023-24 c. £5.2M → 2024-25 £5.53M — sustained CPI + caseload growth"},
            {"label": "Delivery body", "value": "Trust Procurement + NHS Supply Chain (Health, Care and Community tower) + Trust Pharmacy/Stores + community-services management"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + NHSE Community Services Improvement + DHSC + Lincolnshire ICB"},
            {"label": "Evaluation evidence", "value": "CQC RY5 inspections; NHSE Community Services Statistics; Model Hospital community benchmark; NAO Adult community health services 2020; Trust ARA 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: ULHT-led pre-2011 community services · Successor: Three Shifts community lift + potential Lincs system-wide community/acute reconfiguration"}
        ],
        "notes": "LCHS's general supplies & services baseline reflects a rural-community model dominated by district-nursing wound-care and continence consumables across one of England's most sparsely populated counties — long travel distances drive higher per-contact stock-handling overhead than urban community trusts. Community-hospital inpatient units at Skegness, Louth, Boston and Stamford add ward-stock demand that sits outside acute-trust supply chains. NHS Supply Chain's Health, Care and Community Services tower is the primary procurement vehicle, with trust-direct Procurement Act 2023 contracts for rural-specific categories. The Darzi report (Sep 2024) and 10 Year Plan Three Shifts policy lifting out-of-hospital care imply consumables baseline growth above CPI, sustained by population frailty and rural-coverage demands. Lincolnshire ICB allocation frames the operational envelope.",
        "sources": [
            {"publisher": "Lincolnshire Community Health Services NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.lincolnshirecommunityhealthservices.nhs.uk/about-us/our-publications"},
            {"publisher": "NHS Supply Chain", "title": "Health, Care and Community Services category tower", "url": "https://www.supplychain.nhs.uk/categories/health-care-and-community-services/"},
            {"publisher": "Department of Health and Social Care", "title": "The Lord Darzi independent investigation of the NHS in England (Sep 2024)", "url": "https://www.gov.uk/government/publications/independent-investigation-of-the-nhs-in-england"},
            {"publisher": "Cabinet Office", "title": "Procurement Act 2023 — guidance and commencement (24 Feb 2025)", "url": "https://www.gov.uk/government/collections/procurement-act-2023-guidance-documents"},
            {"publisher": "Care Quality Commission", "title": "Lincolnshire Community Health Services provider profile (RY5)", "url": "https://www.cqc.org.uk/provider/RY5"}
        ],
        "related": ["Lincolnshire Community Health Services NHS Trust", "Clinical Supplies & Drugs", "NHS Community Trusts", "Social security & levy — Lincolnshire Community Health Services NHS Trust", "General supplies & services — Birmingham Community Healthcare NHS Foundation Trust", "NHS Supply Chain"]
    },
    "Social security & levy — Bridgewater Community Healthcare NHS Foundation Trust": {
        "aliases": [{"name": "Social security & levy", "parent": "Bridgewater Community Healthcare NHS Foundation Trust"}],
        "description": "Bridgewater Community Healthcare £5.45M social-security & levy line is the employer National Insurance Contribution (Class 1 secondary) on the trust's c. 1,300-WTE community-services workforce — district nurses, health visitors, school nurses, MSK community physios, community-paediatric teams and community-dental staff serving Halton, Warrington, St Helens and parts of Bolton, Wigan and Cheshire. The line tracks Agenda for Change pay-bands (predominantly Bands 5-6) with the April 2025 employer-NIC step-up driving a structural baseline reset.",
        "beneficiaries": "c. 1,300 WTE community staff serving a c. 800,000 Halton + Warrington + St Helens + Greater Manchester / Cheshire fringe population; community caseload includes c. 100,000 district-nursing contacts/yr, health visiting + 0-19 services, MSK and community-dental clinic activity.",
        "legal_basis": "Social Security Contributions and Benefits Act 1992 — National Insurance Contributions Act 2024 (April 2025 employer rate to 15% / threshold £5,000) — NHS Pension Scheme Regulations 2015 — Agenda for Change pay framework — DHSC Group Accounting Manual 2024-25 — IAS 19 Employee Benefits — NHS Act 2006",
        "key_stats": [
            {"label": "Social security & levy 2024-25", "value": "£5.45M"},
            {"label": "Trust scale", "value": "c. 1,300 WTE community-services workforce; c. 50+ community sites across Halton, Warrington, St Helens + cross-boundary footprint"},
            {"label": "Catchment", "value": "c. 800,000 Halton + Warrington + St Helens + parts of Bolton/Wigan/Cheshire"},
            {"label": "Workforce mix", "value": "District nurses, health visitors, school nurses, MSK physios, community paeds, community dental, end-of-life nursing"},
            {"label": "AfC band concentration", "value": "Predominantly Bands 5-6 with Band 4 nursing associates + Band 7 specialist roles"},
            {"label": "Apr 2025 employer NIC step-up", "value": "Rate 13.8% to 15.0%; threshold £9,100 to £5,000 — c. 1.4 ppt uplift on c. £33M paybill"},
            {"label": "Treasury backfill (HCL repeal context)", "value": "HCL repealed Nov 2022; Autumn Budget 2024 NHS NIC mitigation — net residual via Cheshire and Merseyside ICB allocation"},
            {"label": "Funding trajectory", "value": "2021-22 c. £4.1M → 2022-23 c. £4.4M (HCL spike) → 2023-24 c. £5.0M → 2024-25 £5.45M; 2025-26 step uplift from NIC reset"},
            {"label": "Delivery body", "value": "Trust HR/Payroll + NHS Business Services Authority (NHSBSA pension admin) + HMRC (RTI PAYE/NIC submission)"},
            {"label": "Policy owner", "value": "HM Treasury (NIC rates) + DHSC (paybill envelope) + NHSE Provider Finance + Cheshire and Merseyside ICB"},
            {"label": "Evaluation evidence", "value": "CQC RY2 inspections; OBR EFO Mar 2025 (NIC receipts); NHSE Community Services Statistics; Trust ARA 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2022 HCL 1.25 ppt levy · Successor: April 2025 NIC step-up + Three Shifts community-lift workforce growth"}
        ],
        "notes": "Bridgewater Community Healthcare's social-security & levy is dominated by employer NIC on a workforce-heavy community-services paybill — the trust is c. 70% staff costs reflecting the labour-intensive district-nursing and health-visiting model. The April 2025 employer-NIC step-up (13.8% to 15.0%, threshold £9,100 to £5,000) imposes a structural baseline reset partially backfilled by Autumn Budget 2024 NHS mitigation but with residual ICS-level allocation impact. Cross-boundary service delivery into Bolton, Wigan and Cheshire (alongside core Halton, Warrington and St Helens) adds operational complexity to paybill allocation. The Darzi report (Sep 2024) and 10 Year Plan Three Shifts policy lifting out-of-hospital care imply paybill growth above CPI through medium-term workforce expansion.",
        "sources": [
            {"publisher": "Bridgewater Community Healthcare NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.bridgewater.nhs.uk/about-us/publications/"},
            {"publisher": "HM Revenue & Customs", "title": "National Insurance Contributions rates and thresholds 2025-26", "url": "https://www.gov.uk/government/publications/rates-and-allowances-national-insurance-contributions"},
            {"publisher": "HM Treasury", "title": "Autumn Budget 2024 — Employer NIC and public sector mitigation", "url": "https://www.gov.uk/government/publications/autumn-budget-2024"},
            {"publisher": "Department of Health and Social Care", "title": "The Lord Darzi independent investigation of the NHS in England (Sep 2024)", "url": "https://www.gov.uk/government/publications/independent-investigation-of-the-nhs-in-england"},
            {"publisher": "Care Quality Commission", "title": "Bridgewater Community Healthcare provider profile (RY2)", "url": "https://www.cqc.org.uk/provider/RY2"}
        ],
        "related": ["Bridgewater Community Healthcare NHS Foundation Trust", "Staff Costs", "NHS Community Trusts", "Social security & levy — Wirral Community Health and Care NHS Foundation Trust", "Social security & levy — Shropshire Community Health NHS Trust", "HM Revenue & Customs"]
    },
    "Establishment costs — Hertfordshire Community NHS Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "Hertfordshire Community NHS Trust"}],
        "description": "Hertfordshire Community NHS Trust (HCT) £5.38M establishment costs covers postage, telephony, mobile-data (community-staff smartphone/tablet fleet), printing, stationery, recruitment advertising, subscriptions and minor sundries across the trust's c. 50+ community-clinic and community-hospital footprint serving Hertfordshire. The line carries the embedded back-office overhead for a c. 2,500-WTE community workforce delivering district nursing, school nursing, MSK and community-paediatric services across an urban-rural mix in Watford, Stevenage, St Albans and the rural west.",
        "beneficiaries": "c. 2,500 WTE staff serving a c. 1.2M Hertfordshire population; community-hospital inpatient beds at Cheshunt, Potters Bar, Hemel Hempstead and others; district nursing, health visiting, school nursing, MSK and community-paediatric services across c. 50+ sites.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) — IAS 1 Presentation of Financial Statements — NHS Act 2006 — Health and Care Act 2022 — NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£5.38M"},
            {"label": "Trust scale", "value": "c. 2,500 WTE community workforce; c. 50+ sites across Hertfordshire including community hospitals at Cheshunt, Potters Bar, Hemel Hempstead"},
            {"label": "Catchment", "value": "c. 1.2M Hertfordshire population (urban-rural mix — Watford, Stevenage, St Albans, rural west)"},
            {"label": "Composition", "value": "Postage, telephony/mobile, community-staff smartphone/tablet fleet, printing, stationery, recruitment advertising, subscriptions, hospitality, minor sundries"},
            {"label": "Mobile workforce telephony", "value": "Community staff smartphone/tablet fleet for clinical record-keeping in patients' homes drives mobile-data baseline"},
            {"label": "Industrial action 2023-24", "value": "Junior-doctor + consultant strikes drove minor recruitment-advertising spike (limited direct exposure as community trust)"},
            {"label": "EPR / Frontline Digitisation", "value": "SystmOne community EPR baseline; ongoing optimisation drives change-comms + training-materials baseline"},
            {"label": "Apr 2025 CPI uplift", "value": "Royal Mail + telecoms + advertising CPI feed forward unit-cost pressure"},
            {"label": "Funding trajectory", "value": "2021-22 c. £4.1M → 2023-24 c. £5.0M → 2024-25 £5.38M — sustained CPI + mobile-workforce digital uplift"},
            {"label": "Delivery body", "value": "Trust Corporate Services + Procurement + IT + (Crown Commercial Service framework for telecoms/postage)"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Hertfordshire and West Essex ICB"},
            {"label": "Evaluation evidence", "value": "CQC RY4 inspections; Model Hospital community-services benchmark; NHSE Community Services Statistics; Trust ARA 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2010 PCT-provider arm baseline · Successor: Three Shifts community lift + further mobile-digital workforce expansion"}
        ],
        "notes": "Hertfordshire Community's establishment-costs profile carries a distinctive mobile-workforce telephony loading — community staff using smartphone/tablet fleet for clinical record-keeping in patients' homes drives a mobile-data baseline higher than equivalent acute-trust profiles. SystmOne community EPR baseline and ongoing optimisation feed change-management and training-materials spend. Industrial action exposure is limited (community trust) but recruitment-advertising for community nursing and health-visiting hard-to-fill posts remains a sustained driver. Royal Mail postage uplifts and telecoms CPI feed forward unit-cost pressure into 2025-26. The Darzi Three Shifts policy lifting out-of-hospital care implies further mobile-digital workforce expansion. Hertfordshire and West Essex ICB allocation frames the operational envelope.",
        "sources": [
            {"publisher": "Hertfordshire Community NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.hct.nhs.uk/about-us/publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme (community EPR)", "url": "https://www.england.nhs.uk/digitaltechnology/connecting-health-and-care/frontline-digitisation/"},
            {"publisher": "Department of Health and Social Care", "title": "The Lord Darzi independent investigation of the NHS in England (Sep 2024)", "url": "https://www.gov.uk/government/publications/independent-investigation-of-the-nhs-in-england"},
            {"publisher": "Care Quality Commission", "title": "Hertfordshire Community NHS Trust provider profile (RY4)", "url": "https://www.cqc.org.uk/provider/RY4"}
        ],
        "related": ["Hertfordshire Community NHS Trust", "Premises & Infrastructure", "NHS Community Trusts", "Social security & levy — Hertfordshire Community NHS Trust", "Establishment costs — Kent Community Health NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "PFI / LIFT charges — Alder Hey Children's NHS Foundation Trust": {
        "aliases": [{"name": "PFI / LIFT charges", "parent": "Alder Hey Children's NHS Foundation Trust"}],
        "description": "Alder Hey Children's £5.10M PFI / LIFT charges line is the unitary charge service-element on the 'Alder Hey in the Park' PFI scheme, which delivered the new c. £237M Alder Hey Children's Hospital opened October 2015 — the Liverpool flagship paediatric tertiary hospital and the first major children's hospital in a park setting. The unitary charge covers facilities-management services (cleaning, catering, portering, estates maintenance) plus the financing element across a 30-year concession running to c. 2045 (Project Co: Catalyst Lea Healthcare Ltd / Laing O'Rourke / InfraRed Capital Partners).",
        "beneficiaries": "c. 4,200 WTE staff at the Alder Hey in the Park flagship + Liverpool community sites; c. 330,000 patient visits/yr; supra-regional paediatric tertiary catchment serving North West England, parts of Wales and Isle of Man; c. 270 inpatient beds.",
        "legal_basis": "IFRIC 12 Service Concession Arrangements — IFRS 16 Leases (post-2022 application) — DHSC PFI guidance — DHSC Group Accounting Manual 2024-25 — NHS Act 2006 — Health and Care Act 2022 — Public-Private Partnerships (PPP) framework",
        "key_stats": [
            {"label": "PFI / LIFT charges 2024-25", "value": "£5.10M"},
            {"label": "Trust scale", "value": "c. 4,200 WTE; c. 270 inpatient beds; c. 330,000 patient visits/yr; supra-regional paediatric tertiary"},
            {"label": "PFI scheme", "value": "Alder Hey in the Park — c. £237M new-build opened Oct 2015; 30-year concession to c. 2045"},
            {"label": "Project Co", "value": "Catalyst Lea Healthcare Ltd; sponsors Laing O'Rourke + InfraRed Capital Partners; FM provided by Equans (formerly Engie)"},
            {"label": "Composition", "value": "FM service element (cleaning, catering, portering, lifecycle, estates) + financing element of unitary charge"},
            {"label": "Park-setting flagship", "value": "First major children's hospital in a park setting; 60% of site is public parkland"},
            {"label": "Specialised commissioning", "value": "NHSE Specialised Commissioning for paediatric tertiary services drives capacity demand"},
            {"label": "Apr 2025 RPI / CPI uplift", "value": "Annual unitary-charge indexation (typically 50/50 RPI fix-element + CPI services)"},
            {"label": "Funding trajectory", "value": "FY1 (2015-16) c. £4.6M → 2023-24 c. £4.9M → 2024-25 £5.10M — RPI/CPI indexation sustains uplift"},
            {"label": "Delivery body", "value": "Trust Estates + Equans (FM provider) + Catalyst Lea Healthcare Ltd (Project Co) + (HM Treasury IPA monitoring)"},
            {"label": "Policy owner", "value": "DHSC PFI/PPP team + HM Treasury Infrastructure and Projects Authority + NHSE Provider Finance + Cheshire and Merseyside ICB"},
            {"label": "Evaluation evidence", "value": "NAO PFI and PF2 (HC 718, 2018); HMT IPA Annual Reports; CQC RBS inspections; PAC PFI hand-back inquiries; Trust ARA 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: Alder Hey Eaton Road Victorian estate (closed 2015) · Successor: 2045 PFI hand-back to Trust ownership; HMT 'Managing PFI assets and contracts hand-back' guidance applies"}
        ],
        "notes": "Alder Hey's PFI / LIFT charges line covers only the operating-expense FM service element of the 'Alder Hey in the Park' unitary charge — the financing/interest element flows through Finance costs and capital depreciation through other premises lines, so this £5.10M understates total scheme cost. The c. £237M new-build opened October 2015 was the first major UK children's hospital in a park setting (60% of site is public parkland) and replaced the Victorian Eaton Road estate. The 30-year concession runs to c. 2045 with annual RPI/CPI indexation sustaining unitary-charge uplift. NAO and PAC have repeatedly flagged PFI affordability and hand-back risk; HM Treasury's PFI hand-back guidance frames Trust transition planning. Equans (formerly Engie) provides the bundled FM services.",
        "sources": [
            {"publisher": "Alder Hey Children's NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://alderhey.nhs.uk/about-us/our-publications/"},
            {"publisher": "National Audit Office", "title": "PFI and PF2 (HC 718, 2018)", "url": "https://www.nao.org.uk/reports/pfi-and-pf2/"},
            {"publisher": "HM Treasury / Infrastructure and Projects Authority", "title": "Managing PFI assets and contracts: hand-back guidance", "url": "https://www.gov.uk/government/publications/managing-pfi-assets-and-contracts"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Alder Hey Children's NHS FT provider profile (RBS)", "url": "https://www.cqc.org.uk/provider/RBS"}
        ],
        "related": ["Alder Hey Children's NHS Foundation Trust", "Premises & Infrastructure", "NHS Specialist Trusts", "Social security & levy — Alder Hey Children's NHS Foundation Trust", "PFI / LIFT charges — Northamptonshire Healthcare NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Establishment costs — Yorkshire Ambulance Service NHS Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "Yorkshire Ambulance Service NHS Trust"}],
        "description": "Yorkshire Ambulance Service (YAS) £4.90M establishment costs covers postage, telephony, mobile-data (CAD/MDT terminals), printing, stationery, recruitment advertising, subscriptions and minor sundries across the trust's c. 60+ ambulance station and Make Ready Hub network spanning North, South, West and East Yorkshire and Humber, plus the integrated NHS 111 service. Heavy 111-clinical-assessment-service telecoms spend distinguishes YAS overhead from peer ambulance trusts that do not host 111.",
        "beneficiaries": "c. 6,800 WTE staff (paramedics, EMTs, ECAs, 999 call handlers, 111 health advisers + clinicians) serving a c. 5.5M Yorkshire and Humber population; c. 1.05M 999 incidents/yr + c. 2.2M 111 calls/yr; c. 60+ stations + 2 EOCs (Wakefield, York).",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) — IAS 1 Presentation of Financial Statements — NHS Act 2006 — Health and Care Act 2022 — NHS Standard Contract 2024-25 — Civil Contingencies Act 2004 (Cat-1 responder)",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£4.90M"},
            {"label": "Trust scale", "value": "c. 6,800 WTE; c. 60+ ambulance stations + 2 EOCs (Wakefield, York); integrated 111 service"},
            {"label": "Annual demand", "value": "c. 1.05M 999 incidents + c. 2.2M 111 calls/yr; c. 5.5M Yorkshire and Humber population"},
            {"label": "Composition", "value": "Mobile-data + CAD/MDT + 111 telephony, postage, printing, stationery, recruitment advertising, subscriptions"},
            {"label": "111 integrated service", "value": "YAS hosts 111 + Clinical Assessment Service for Yorkshire and Humber — telephony spend higher than 999-only peers"},
            {"label": "Industrial action 2023-24", "value": "GMB + Unison paramedic strikes drove substantive + agency recruitment-advertising spike"},
            {"label": "CAD / MDT spend", "value": "Cleric CAD + mobile-data terminals on c. 600+ vehicles; EE Blue Light tariff"},
            {"label": "CQC s.29A warning notice (2023) recovery", "value": "2023 inspection drove governance/comms remediation — training-materials + internal-comms baseline"},
            {"label": "Funding trajectory", "value": "2021-22 c. £3.7M → 2023-24 c. £4.5M → 2024-25 £4.90M — sustained recruitment + 111 expansion"},
            {"label": "Delivery body", "value": "Trust Corporate Services + Fleet IT + 111/CAS Operations + Procurement + (Crown Commercial Service framework for telecoms / EE Blue Light)"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + NHSE Urgent and Emergency Care + DHSC + Humber and North Yorkshire / West Yorkshire / South Yorkshire ICBs"},
            {"label": "Evaluation evidence", "value": "CQC RX8 inspections (incl. 2023 s.29A); NHSE Ambulance Quality Indicators monthly; ORH ambulance benchmarks; Trust ARA 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2019 separate 111 / 999 baseline · Successor: NHSE Integrated Urgent Care + Cat-2 segmentation reform 2024-25 + post-CQC governance recovery"}
        ],
        "notes": "YAS's establishment-costs profile mirrors SCAS in carrying twin 999 + 111/Clinical Assessment Service telephony loadings — Yorkshire and Humber 111 hosting drives telecoms baseline above 999-only peer trusts. Industrial action 2023-24 (paramedic strikes Dec 2022 - Mar 2023) drove substantive and agency recruitment-advertising spending. The 2023 CQC s.29A warning notice on governance and patient safety has driven sustained training-materials and internal-comms spend through 2024-25 as the trust completes its remediation programme. EE Blue Light Network mobile-data tariff renewals and Royal Mail postage CPI feed forward unit-cost pressure into 2025-26. ICB commissioning is fragmented across Humber and North Yorkshire, West Yorkshire and South Yorkshire with NHSE UEC the primary policy owner; Cat-2 segmentation reform 2024-25 is reshaping operational comms baseline.",
        "sources": [
            {"publisher": "Yorkshire Ambulance Service NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.yas.nhs.uk/about-us/our-publications/annual-reports/"},
            {"publisher": "Care Quality Commission", "title": "Yorkshire Ambulance Service provider profile (RX8) — incl. 2023 s.29A inspection", "url": "https://www.cqc.org.uk/provider/RX8"},
            {"publisher": "NHS England", "title": "Ambulance Quality Indicators (AQI) — monthly statistics", "url": "https://www.england.nhs.uk/statistics/statistical-work-areas/ambulance-quality-indicators/"},
            {"publisher": "NHS England", "title": "Integrated Urgent Care service specification (111/CAS)", "url": "https://www.england.nhs.uk/publication/integrated-urgent-care-service-specification/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"}
        ],
        "related": ["Yorkshire Ambulance Service NHS Trust", "Premises & Infrastructure", "NHS Ambulance Trusts", "Social security & levy — Yorkshire Ambulance Service NHS Trust", "Establishment costs — South Central Ambulance Service NHS Foundation Trust", "NHS England"]
    },
    "Business rates — Great Ormond Street Hospital for Children NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "Great Ormond Street Hospital for Children NHS Foundation Trust"}],
        "description": "Great Ormond Street Hospital (GOSH) £4.69M business rates line is non-domestic rates payable to the London Borough of Camden under the Local Government Finance Act 1988 on the trust's c. 320,000 sq ft Bloomsbury campus comprising the Variety Club Building, the Octav Botnar Wing, the Premier Inn Clinical Building (Sight & Sound Centre, opened 2022), the Frontage Building and the Mittal Children's Medical Centre. GOSH's Zone-A central-London valuation drives a substantial rateable-value liability — among the highest per-sq-ft NHS trust ratings.",
        "beneficiaries": "c. 5,500 WTE staff at the central-London Bloomsbury campus; c. 280,000 patient visits/yr; supra-regional + international paediatric tertiary referral catchment; c. 320,000 sq ft estate footprint adjacent to Russell Square.",
        "legal_basis": "Local Government Finance Act 1988 (Schedule 6) — Non-Domestic Rating Act 2023 — Non-Domestic Rating (Multipliers and Private Finance) Act 2024 — Valuation Office Agency 2023 Revaluation List — DHSC Group Accounting Manual 2024-25 — IAS 1 — NHS Act 2006",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£4.69M"},
            {"label": "Trust scale", "value": "c. 5,500 WTE; c. 320,000 sq ft Bloomsbury campus; central-London Zone-A valuation"},
            {"label": "Site composition", "value": "Variety Club Building, Octav Botnar Wing, Premier Inn Clinical / Sight & Sound (2022), Frontage Building, Mittal Children's Medical Centre"},
            {"label": "Billing authority", "value": "London Borough of Camden — multiplier set centrally; 2023 List rateable values"},
            {"label": "VOA 2023 Revaluation", "value": "Effective 1 April 2023; central London medical buildings carry significant uplift versus 2017 list"},
            {"label": "Multipliers Act 2024", "value": "Non-Domestic Rating (Multipliers and Private Finance) Act 2024 reshapes 2025-26 multiplier structure (introduces lower/standard split)"},
            {"label": "Apr 2025 multiplier uplift", "value": "Standard multiplier subject to CPI cap; charity / public sector reliefs do not generally apply to NHS trusts"},
            {"label": "Funding trajectory", "value": "2021-22 c. £3.8M → 2022-23 c. £4.0M → 2023-24 c. £4.5M (post-Revaluation) → 2024-25 £4.69M"},
            {"label": "Delivery body", "value": "Trust Estates + Valuation Office Agency (rateable-value setting) + London Borough of Camden (billing)"},
            {"label": "Policy owner", "value": "Ministry of Housing, Communities and Local Government (MHCLG) + HM Treasury (multipliers) + NHSE Provider Finance + DHSC"},
            {"label": "Evaluation evidence", "value": "VOA Annual Report; NAO Business rates retention; Model Hospital premises benchmark; Trust ARA 2023-24; CQC RP4 inspections"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2017 VOA Revaluation list · Successor: 2026 VOA Revaluation list + Multipliers Act 2024 split-multiplier 2025-26"}
        ],
        "notes": "GOSH's business-rates liability is structurally elevated by central-London Zone-A valuation across its c. 320,000 sq ft Bloomsbury estate — the trust pays among the highest per-sq-ft business-rates of any NHS provider, with Russell Square location commanding rateable values well above provincial children's hospitals. The 1 April 2023 VOA Revaluation lifted the rateable-value baseline materially given central-London commercial-medical valuation uplift. The Non-Domestic Rating (Multipliers and Private Finance) Act 2024 introduces a split-multiplier structure (lower multiplier for high street + standard multiplier for higher-value premises) from 2025-26, which is unlikely to ease NHS trust large-property liabilities. Camden is the billing authority. Rates are not eligible for charity relief as NHS trusts do not qualify; mandatory reliefs are not in scope.",
        "sources": [
            {"publisher": "Great Ormond Street Hospital for Children NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.gosh.nhs.uk/about-us/our-corporate-information/annual-reports-and-accounts/"},
            {"publisher": "Valuation Office Agency", "title": "Business Rates 2023 Revaluation — Rating List", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "Ministry of Housing, Communities and Local Government", "title": "Non-Domestic Rating (Multipliers and Private Finance) Act 2024", "url": "https://www.legislation.gov.uk/ukpga/2024/30"},
            {"publisher": "London Borough of Camden", "title": "Business rates — non-domestic rates", "url": "https://www.camden.gov.uk/business-rates"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"}
        ],
        "related": ["Great Ormond Street Hospital for Children NHS Foundation Trust", "Premises & Infrastructure", "NHS Specialist Trusts", "Transport (business + patient) — Great Ormond Street Hospital for Children NHS Foundation Trust", "Business rates — The Royal Marsden NHS Foundation Trust", "Valuation Office Agency"]
    },
    "Transport (business + patient) — Kent Community Health NHS Foundation Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "Kent Community Health NHS Foundation Trust"}],
        "description": "Kent Community Health (KCHFT) £4.50M transport line covers business mileage (AfC Section 17 + AMAP) for c. 5,000 community-based clinical staff, pool-fleet IFRS 16 leases for district-nursing and MSK-physio mobile units, and patient-travel reimbursements across one of England's largest geographical community-trust footprints serving Kent and Medway. Mileage spend is structurally elevated by the rural and coastal-spread Kent geography — district nurses and health visitors travel substantial daily mileage between dispersed patient homes.",
        "beneficiaries": "c. 5,000 WTE community staff serving a c. 1.8M Kent and Medway population; c. 200+ community sites including community hospitals at Hawkhurst, Faversham, Sevenoaks, Tonbridge, Whitstable; district nursing, health visiting, school nursing, MSK community physio, intermediate-care.",
        "legal_basis": "NHS Act 2006 — NHSE Patient Transport Services Eligibility Criteria 2021 — Agenda for Change Section 17 (business mileage) — HMRC AMAP rates — IFRS 16 Leases (pool fleet) — DHSC Group Accounting Manual 2024-25 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£4.50M"},
            {"label": "Trust scale", "value": "c. 5,000 WTE community workforce; c. 200+ sites across Kent and Medway"},
            {"label": "Catchment", "value": "c. 1.8M Kent and Medway population; large rural + coastal footprint (one of England's biggest community-trust geographies)"},
            {"label": "Composition", "value": "Business mileage (AfC S17 + AMAP 45p/25p) + IFRS 16 pool-fleet leases (district-nursing + MSK mobile units) + patient travel reimbursement"},
            {"label": "AMAP rate context", "value": "HMRC AMAP rate frozen at 45p/mile (first 10k miles) since 2011 — real-terms erosion is contentious nationally"},
            {"label": "Rural-coverage driver", "value": "Kent + Medway dispersed-population geography drives daily community-staff mileage well above urban community trusts"},
            {"label": "Industrial action 2023-24 effect", "value": "Limited direct exposure (community trust) — minor cancellation rebooking + recruitment-travel impact"},
            {"label": "Apr 2025 fuel CPI / NIC", "value": "Diesel CPI feed forward unit-cost pressure; NEPTS contractor pass-through"},
            {"label": "Funding trajectory", "value": "2021-22 c. £3.6M → 2023-24 c. £4.2M → 2024-25 £4.50M — fuel CPI + caseload growth"},
            {"label": "Delivery body", "value": "Trust Fleet + HR (mileage) + pool-fleet leasing partner + community-services management"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + NHSE Urgent and Emergency Care (NEPTS) + DHSC + Kent and Medway ICB"},
            {"label": "Evaluation evidence", "value": "NAO NEPTS 2019; CQC RYY inspections; NHSE Community Services Statistics; Trust ARA 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-IFRS 16 operating-lease pool-fleet · Successor: pool-fleet electrification + Three Shifts community lift increasing mileage volume"}
        ],
        "notes": "KCHFT's transport line is the highest of any NHS community trust in this cluster precisely because Kent and Medway represents one of England's largest community-services geographies — district nurses, health visitors, MSK physios and intermediate-care teams travel substantial daily mileage between dispersed coastal and rural patient homes. The HMRC AMAP-rate freeze (45p/mile since 2011, c. 35% real-terms erosion versus CPI) sustains internal-mileage rate-dispute pressure. Pool-fleet IFRS 16 leases (district-nursing cars and MSK mobile units) are the structural backbone, with diesel CPI and the planned electrification trajectory under NHS Net Zero Plan 2040 the key forward drivers. Industrial action exposure is limited (community trust). The Darzi Three Shifts policy lifting out-of-hospital care implies sustained mileage-volume growth as community caseload expands.",
        "sources": [
            {"publisher": "Kent Community Health NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.kentcht.nhs.uk/about-us/publications/annual-report/"},
            {"publisher": "NHS England", "title": "Non-Emergency Patient Transport Services — National Framework + Eligibility Criteria 2021", "url": "https://www.england.nhs.uk/publication/non-emergency-patient-transport-services-nepts/"},
            {"publisher": "HM Revenue & Customs", "title": "Approved Mileage Allowance Payments (AMAP) rates", "url": "https://www.gov.uk/government/publications/rates-and-allowances-travel-mileage-and-fuel-allowances"},
            {"publisher": "NHS England", "title": "Delivering a Net Zero National Health Service (Greener NHS)", "url": "https://www.england.nhs.uk/greenernhs/a-net-zero-nhs/"},
            {"publisher": "Care Quality Commission", "title": "Kent Community Health NHS FT provider profile (RYY)", "url": "https://www.cqc.org.uk/provider/RYY"}
        ],
        "related": ["Kent Community Health NHS Foundation Trust", "Premises & Infrastructure", "NHS Community Trusts", "Social security & levy — Kent Community Health NHS Foundation Trust", "Establishment costs — Kent Community Health NHS Foundation Trust", "NHS England"]
    },
    "General supplies & services — The Clatterbridge Cancer Centre NHS Foundation Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "The Clatterbridge Cancer Centre NHS Foundation Trust"}],
        "description": "Clatterbridge Cancer Centre (CCC) £4.49M general supplies & services line covers non-pay clinical and operational consumables for the trust's specialist cancer-services portfolio across the Liverpool flagship (CCC-Liverpool, opened 2020), the Wirral original Clatterbridge campus and outreach satellite radiotherapy units at Aintree and Halton — radiotherapy beam-shaping consumables, brachytherapy applicators, immobilisation devices, IV chemotherapy ancillaries, sterile-services and standard medical/surgical consumables. As a single-specialty NHSE specialised-commissioned tertiary cancer centre, the consumables profile differs materially from acute-trust benchmarks.",
        "beneficiaries": "c. 1,800 WTE staff at the Liverpool flagship + Wirral + Aintree + Halton sites; c. 33,000 patients/yr; supra-regional cancer referral catchment serving Cheshire and Merseyside, parts of N Wales and Isle of Man; one of UK's largest non-surgical oncology providers.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) — IAS 2 Inventories (interaction) — NHS Act 2006 — Health and Care Act 2022 — NHS Standard Contract 2024-25 — Public Contracts Regulations 2015 / Procurement Act 2023 — IRMER 2017 (radiotherapy)",
        "key_stats": [
            {"label": "General supplies & services 2024-25", "value": "£4.49M"},
            {"label": "Trust scale", "value": "c. 1,800 WTE; CCC-Liverpool flagship (opened 2020) + Wirral original + Aintree + Halton outreach sites"},
            {"label": "Annual activity", "value": "c. 33,000 patients/yr; one of UK's largest non-surgical oncology providers"},
            {"label": "Service mix", "value": "External-beam radiotherapy, brachytherapy, systemic anti-cancer therapy (chemo/immuno), proton-beam therapy (UK national service partnership)"},
            {"label": "Composition", "value": "Radiotherapy beam-shaping consumables, brachytherapy applicators, immobilisation devices, IV chemo ancillaries, sterile-services, standard medical/surgical"},
            {"label": "Specialised commissioning", "value": "NHSE Specialised Commissioning funded across all cancer pathways"},
            {"label": "Procurement vehicle", "value": "NHS Supply Chain category towers + trust-direct procurement under Procurement Act 2023 for niche oncology categories"},
            {"label": "Drugs separated", "value": "SACT (chemo/immuno drugs) flow through Drugs costs line — this G&S line is consumables only"},
            {"label": "Funding trajectory", "value": "2021-22 c. £3.5M → 2023-24 c. £4.2M → 2024-25 £4.49M — sustained CPI + activity uplift"},
            {"label": "Delivery body", "value": "Trust Procurement + NHS Supply Chain + Trust Pharmacy/Stores + Radiotherapy Physics team + (linac vendor consumables: Elekta / Varian)"},
            {"label": "Policy owner", "value": "NHSE Specialised Commissioning + NHSE Provider Finance + DHSC + Cheshire and Merseyside ICB"},
            {"label": "Evaluation evidence", "value": "CQC REN inspections; NHSE Specialised Cancer Service specs; NCRAS cancer registration; Model Hospital cancer benchmark; Trust ARA 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2020 single-Wirral site model · Successor: continued radiotherapy fractionation reform (hypofractionation) + CAR-T / advanced therapies expansion"}
        ],
        "notes": "Clatterbridge's general supplies & services profile is shaped by its single-specialty non-surgical-oncology mission — radiotherapy consumables (beam-shaping multi-leaf collimator parts, immobilisation devices, brachytherapy applicators) and IV chemo/immunotherapy ancillaries dominate the line. The 2020 opening of the CCC-Liverpool flagship next to the Royal Liverpool added a major urban hub to the original Wirral campus, with outreach satellite radiotherapy at Aintree and Halton extending reach. SACT drugs flow through a separate Drugs costs line. NHSE Specialised Commissioning funds all cancer pathways, with linac-vendor (Elekta / Varian) consumables a structural recurring spend. Hypofractionation (fewer higher-dose fractions) under royal-college guidance is a forward driver lifting consumables-per-fraction while reducing total fractions; CAR-T and advanced therapies introduce new niche consumables.",
        "sources": [
            {"publisher": "The Clatterbridge Cancer Centre NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.clatterbridgecc.nhs.uk/about-us/publications"},
            {"publisher": "NHS England", "title": "Specialised Cancer Services — service specifications", "url": "https://www.england.nhs.uk/commissioning/spec-services/npc-crg/group-b/"},
            {"publisher": "NHS Supply Chain", "title": "Specialised cancer consumables category", "url": "https://www.supplychain.nhs.uk/"},
            {"publisher": "Cabinet Office", "title": "Procurement Act 2023 — guidance and commencement (24 Feb 2025)", "url": "https://www.gov.uk/government/collections/procurement-act-2023-guidance-documents"},
            {"publisher": "Care Quality Commission", "title": "The Clatterbridge Cancer Centre provider profile (REN)", "url": "https://www.cqc.org.uk/provider/REN"}
        ],
        "related": ["The Clatterbridge Cancer Centre NHS Foundation Trust", "Clinical Supplies & Drugs", "NHS Specialist Trusts", "Social security & levy — The Clatterbridge Cancer Centre NHS Foundation Trust", "General supplies & services — The Christie NHS Foundation Trust", "NHS England"]
    },
}
