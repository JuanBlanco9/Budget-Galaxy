# -*- coding: utf-8 -*-
# Phase 2 SCamb — chunk 01 (17 NHS Specialist/Community/Ambulance Trust orphan sub-lines)
# Hand-curated trust-specific PROGRAMME-archetype enrichment entries.
# Structural contract per docs/archetype_briefs.md.

NEW = {
    "Transport (business + patient) — North West Ambulance Service NHS Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "North West Ambulance Service NHS Trust"}],
        "description": "NWAS's £59.19M transport line is the largest operational input cost of any English ambulance service — covering fleet fuel (DERV + AdBlue), vehicle leasing, AMAP staff mileage, vehicle maintenance, tyres, breakdown recovery and Patient Transport Service (PTS) fleet running across Cumbria, Lancashire, Greater Manchester, Merseyside and Cheshire. The trust runs c. 1,100 emergency vehicles plus a separate PTS fleet across one of England's largest geographic ambulance footprints, including remote Cumbrian fells where rural response distances drive heavy mileage.",
        "beneficiaries": "Serves a c. 7.3M resident population across the North West (Cumbria, Lancashire, Greater Manchester, Merseyside, Cheshire); responds to c. 1.4M 999 calls/yr and c. 1.3M PTS journeys/yr; c. 7,000 WTE staff including c. 4,500 frontline paramedics + EMTs operating from c. 110 ambulance stations and Make Ready Centres.",
        "legal_basis": "NHS Act 2006 · NHSE Patient Transport Services Eligibility Criteria · Agenda for Change s.17 + HMRC Approved Mileage Allowance Payments · IFRS 16 Leases (pool fleet) · DHSC Group Accounting Manual 2024-25 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£59.19M"},
            {"label": "Geographic footprint", "value": "c. 14,200 km² across Cumbria, Lancashire, Greater Manchester, Merseyside, Cheshire — largest English ambulance footprint by area"},
            {"label": "Fleet scale", "value": "c. 1,100 emergency vehicles (DCAs, RRVs, motorbikes) plus separate PTS fleet"},
            {"label": "999 call volume", "value": "c. 1.4M emergency calls/yr; c. 1.3M PTS patient journeys/yr"},
            {"label": "Population served", "value": "c. 7.3M residents (Cumbria + Lancashire + GM + Merseyside + Cheshire)"},
            {"label": "Workforce", "value": "c. 7,000 WTE; c. 4,500 frontline paramedics + EMTs"},
            {"label": "Cost driver — rural Cumbria", "value": "Cumbrian fells and Lake District drive long Cat-1 / Cat-2 response distances; air-ambulance partner reliance with NWAA charity"},
            {"label": "Cat-1 8-min standard", "value": "NHSE Ambulance Response Programme Cat-1 mean 7-min target — drives RRV deployment + fleet diversification"},
            {"label": "Funding trajectory", "value": "Sustained DERV cost growth 2022-23 + 2023-24 industrial action backfill mileage + IFRS 16 lease re-recognition 2022 lifted line vs c. £45M pre-2021"},
            {"label": "Delivery body", "value": "NWAS Fleet & Logistics directorate + leased-fleet partners (e.g. NHS Fleet Solutions / commercial leasing) + AA / RAC breakdown cover"},
            {"label": "Policy owner", "value": "NHSE Urgent & Emergency Care directorate (Ambulance Response Programme) + DHSC + NW ICBs"},
            {"label": "Evaluation evidence", "value": "ORH ambulance benchmarking; AACE annual reports; NAO Ambulance Services NHS report; NHSE Ambulance Quality Indicators monthly"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2006 Cumbria + Cheshire/Mersey + GM + Lancs ambulance services merged into NWAS · Successor: zero-emission fleet transition (NHSE Net Zero 2032 ambulance road-fleet target)"}
        ],
        "notes": "NWAS runs the largest English ambulance footprint by geographic area, with rural Cumbria and the Lake District driving disproportionate transport cost per call versus urban-dense services like LAS. Sustained DERV (diesel) price growth across 2022-24, the 2022 IFRS 16 transition that brought leased pool-fleet onto the balance sheet at higher recognised charge, and the 2023-24 GMB+Unison industrial action that drove backfill mileage, combine to push the line to c. £59M. The Net Zero 2032 ambulance road-fleet target is reshaping fleet-replacement procurement towards EV DCAs (diesel-cycle ambulances are operationally challenging given EV range constraints), with phased pilots underway. Cat-1 mean 7-minute standard performance drives RRV (Rapid Response Vehicle) deployment alongside DCAs.",
        "sources": [
            {"publisher": "North West Ambulance Service NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.nwas.nhs.uk/about-us/corporate-information/annual-report/"},
            {"publisher": "NHS England", "title": "Ambulance Quality Indicators (monthly statistics)", "url": "https://www.england.nhs.uk/statistics/statistical-work-areas/ambulance-quality-indicators/"},
            {"publisher": "Association of Ambulance Chief Executives", "title": "AACE Annual Report and ambulance benchmarking", "url": "https://aace.org.uk/"},
            {"publisher": "National Audit Office", "title": "NHS ambulance services (HC 972, 2017)", "url": "https://www.nao.org.uk/reports/nhs-ambulance-services/"},
            {"publisher": "Care Quality Commission", "title": "NWAS provider profile (RX7)", "url": "https://www.cqc.org.uk/provider/RX7"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"}
        ],
        "related": ["North West Ambulance Service NHS Trust", "Premises & Infrastructure", "NHS Ambulance Trusts", "Transport (business + patient) — South Western Ambulance Service NHS Foundation Trust", "Transport (business + patient) — London Ambulance Service NHS Trust", "NHS England"]
    },
    "Transport (business + patient) — South Western Ambulance Service NHS Foundation Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "South Western Ambulance Service NHS Foundation Trust"}],
        "description": "SWASFT's £53.66M transport line covers the running cost of England's geographically-largest ambulance fleet, serving Cornwall, Devon, Dorset, Somerset, Wiltshire, Bristol, Gloucestershire and the Isles of Scilly. The line covers DERV fuel, vehicle leasing, AMAP staff mileage, vehicle maintenance, tyres, breakdown recovery, ferry transit (Isles of Scilly + Torpoint Ferry) and Patient Transport Service running costs. Long rural distances and seasonal tourist-population spikes (Cornwall + Devon + Dorset coastal) drive disproportionate fleet running cost per call.",
        "beneficiaries": "Serves a c. 5.5M resident population across the South West plus a peak summer tourist surge that adds an estimated c. 23M annual visitor-days; responds to c. 1.0M 999 calls/yr; c. 5,000 WTE staff including c. 3,500 frontline paramedics + EMTs operating c. 950 emergency vehicles from c. 90 ambulance stations and Make Ready Centres.",
        "legal_basis": "NHS Act 2006 · NHSE Patient Transport Services Eligibility Criteria · Agenda for Change s.17 + HMRC Approved Mileage Allowance Payments · IFRS 16 Leases (pool fleet) · DHSC Group Accounting Manual 2024-25 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£53.66M"},
            {"label": "Geographic footprint", "value": "c. 25,000 km² — largest English ambulance footprint by area (covers c. 20% of England's land area)"},
            {"label": "Fleet scale", "value": "c. 950 emergency vehicles (DCAs, RRVs, BASICS, critical-care cars)"},
            {"label": "999 call volume", "value": "c. 1.0M emergency calls/yr"},
            {"label": "Population + tourist spike", "value": "c. 5.5M residents + c. 23M visitor-days/yr summer surge in Cornwall/Devon/Dorset"},
            {"label": "Workforce", "value": "c. 5,000 WTE; c. 3,500 frontline clinicians"},
            {"label": "Rural-cost driver", "value": "Long rural Cornwall + Devon + Exmoor + Dartmoor distances; Isles of Scilly + Torpoint Ferry transit; high AMAP mileage exposure"},
            {"label": "Cat-1 8-min standard", "value": "Cat-1 mean target performance pressured by rural geography; CFR (Community First Responder) volunteer scheme heavy reliance"},
            {"label": "Funding trajectory", "value": "DERV cost growth 2022-23 + 2023-24 industrial action backfill mileage + IFRS 16 2022 lease re-recognition lifted line vs c. £42M pre-2021"},
            {"label": "Delivery body", "value": "SWASFT Fleet & Logistics directorate + leased-fleet partners + Devon & Cornwall Police shared-radio (Airwave / ESN)"},
            {"label": "Policy owner", "value": "NHSE Urgent & Emergency Care directorate + DHSC + South West ICBs (Cornwall + IoS · Devon · Dorset · Somerset · BNSSG · BSW · Glos)"},
            {"label": "Evaluation evidence", "value": "ORH ambulance benchmarking; AACE annual reports; CQC inspections; NHSE AQI monthly returns"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2006 Westcountry + Avon + Gloucestershire + Wiltshire ambulance services + 2013 GWAS merger absorbed Great Western · Successor: zero-emission fleet pilot under NHSE Net Zero 2032 plan"}
        ],
        "notes": "SWASFT's transport baseline is structurally elevated by the largest English ambulance geographic footprint and the seasonal Cornwall/Devon/Dorset tourist surge that adds tens of millions of visitor-days each summer. The 2013 merger with Great Western Ambulance Service (covering Avon, Gloucestershire, Wiltshire) consolidated procurement scale but did not reduce per-call rural mileage. Sustained DERV price growth across 2022-24, IFRS 16 2022 lease-recognition transition, and 2023-24 GMB+Unison industrial action backfill all feed into the £53.66M line. Net Zero 2032 ambulance road-fleet transition is operationally constrained by long rural EV-range demands; phased pilots run alongside Critical-Care Car and BASICS-doctor fleet diversification.",
        "sources": [
            {"publisher": "South Western Ambulance Service NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.swast.nhs.uk/about-us/freedom-of-information/publications/annual-reports"},
            {"publisher": "NHS England", "title": "Ambulance Quality Indicators (monthly statistics)", "url": "https://www.england.nhs.uk/statistics/statistical-work-areas/ambulance-quality-indicators/"},
            {"publisher": "Association of Ambulance Chief Executives", "title": "AACE Annual Report and ambulance benchmarking", "url": "https://aace.org.uk/"},
            {"publisher": "Care Quality Commission", "title": "SWASFT provider profile (RYF)", "url": "https://www.cqc.org.uk/provider/RYF"},
            {"publisher": "National Audit Office", "title": "NHS ambulance services (HC 972, 2017)", "url": "https://www.nao.org.uk/reports/nhs-ambulance-services/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"}
        ],
        "related": ["South Western Ambulance Service NHS Foundation Trust", "Premises & Infrastructure", "NHS Ambulance Trusts", "Transport (business + patient) — North West Ambulance Service NHS Trust", "Transport (business + patient) — South East Coast Ambulance Service NHS Foundation Trust", "NHS England"]
    },
    "Social security & levy — London Ambulance Service NHS Trust": {
        "aliases": [{"name": "Social security & levy", "parent": "London Ambulance Service NHS Trust"}],
        "description": "LAS's £46.84M social security & levy line is the employer National Insurance contribution and Apprenticeship Levy (0.5% of pay above £3M threshold) on the largest urban ambulance workforce in England. The line scales with paramedic/EMT pay-bill — driven by London weighting (HCA + Inner-London zone), Agenda for Change pay awards (5%+ in 2023-24), Cat-1 8-minute response rota intensity and 2023-24 industrial-action backfill. The April 2025 employer-NIC step-up (15% rate, lower £5k threshold) materially lifts the line forward.",
        "beneficiaries": "Funds employer-side NIC on c. 8,500 WTE LAS staff including c. 5,500 frontline paramedics + EMTs + EOC clinicians serving 9 million Greater London residents; LAS handles c. 2.0M emergency 999 calls/yr and dispatches from c. 70 ambulance stations + 5 hub Make Ready Centres (Deptford, Friern Barnet, Brent etc.).",
        "legal_basis": "Social Security Contributions and Benefits Act 1992 · Apprenticeship Levy (Finance Act 2016) · Health and Social Care Levy Act 2021 (repealed Nov 2022) · Autumn Budget 2024 employer-NIC reform (15% / £5k threshold from 6 April 2025) · NHS Pension Scheme Regulations · DHSC GAM 2024-25 · NHS Act 2006",
        "key_stats": [
            {"label": "Social security & levy 2024-25", "value": "£46.84M"},
            {"label": "Workforce", "value": "c. 8,500 WTE; c. 5,500 frontline paramedics + EMTs + EOC clinicians"},
            {"label": "Population served", "value": "c. 9.0M Greater London residents (32 boroughs + City of London)"},
            {"label": "999 call volume", "value": "c. 2.0M emergency calls/yr — highest English ambulance volume"},
            {"label": "London weighting", "value": "HCA Inner London zone + Outer London zone Agenda for Change supplements lift base pay-bill vs other ambulance trusts"},
            {"label": "AfC pay award 2023-24", "value": "5% consolidated + £1,250 non-consolidated lump sum lifted base pay; flow-through to NIC"},
            {"label": "Industrial action 2022-24", "value": "GMB + Unison paramedic strikes Dec 2022 - Feb 2024 drove agency backfill + payroll volatility"},
            {"label": "April 2025 NIC step-up", "value": "15% employer rate + £5k threshold from 6 Apr 2025; estimated £6-8M annualised step-up across LAS pay-bill"},
            {"label": "Funding trajectory", "value": "2021-22 c. £35M → 2022-23 £38M → 2023-24 £43M → 2024-25 £46.84M; April 2025 NIC reform feeds forward"},
            {"label": "Delivery body", "value": "LAS HR + Payroll (NHS SBS payroll service) + HMRC employer NIC remittance + NHS Pensions"},
            {"label": "Policy owner", "value": "HM Treasury (NIC + Apprenticeship Levy) + HMRC + DHSC + NHSE Workforce directorate"},
            {"label": "Evaluation evidence", "value": "Trust ARA staff costs note; Model Hospital workforce benchmarks; NHSE Operational Plan returns; AACE workforce returns"},
            {"label": "Predecessor / successor", "value": "Predecessor: Health and Social Care Levy 1.25% (Apr 2022 - Nov 2022, repealed) · Successor: 6 April 2025 employer-NIC step-up to 15% / £5k threshold"}
        ],
        "notes": "LAS carries the largest single ambulance pay-bill in England, reflecting London weighting, the highest emergency-call volume of any English ambulance service (c. 2M/yr) and a frontline workforce that grew through the 2020-2024 expansion to meet Cat-2 mean response targets. The 2023-24 GMB+Unison paramedic industrial action drove substantial agency backfill volatility through this line. Looking forward, the April 2025 employer-NIC step-up to 15% with the £5k threshold is the single biggest single-year cost shock — DHSC has indicated partial public-sector compensation but LAS faces an estimated £6-8M annualised gross uplift before any compensating grant. Apprenticeship Levy applies at 0.5% above £3M.",
        "sources": [
            {"publisher": "London Ambulance Service NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.londonambulance.nhs.uk/about-us/our-publications/annual-reports/"},
            {"publisher": "HM Treasury", "title": "Autumn Budget 2024 — employer National Insurance contributions changes", "url": "https://www.gov.uk/government/publications/autumn-budget-2024"},
            {"publisher": "HMRC", "title": "Employer National Insurance contributions guidance", "url": "https://www.gov.uk/national-insurance-rates-letters"},
            {"publisher": "NHS Employers", "title": "Agenda for Change pay scales 2024-25", "url": "https://www.nhsemployers.org/articles/pay-scales-202425"},
            {"publisher": "Care Quality Commission", "title": "London Ambulance Service provider profile (RRU)", "url": "https://www.cqc.org.uk/provider/RRU"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"}
        ],
        "related": ["London Ambulance Service NHS Trust", "Staff Costs", "NHS Ambulance Trusts", "Social security & levy — Yorkshire Ambulance Service NHS Trust", "Social security & levy — South Western Ambulance Service NHS Foundation Trust", "HM Treasury"]
    },
    "Transport (business + patient) — East of England Ambulance Service NHS Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "East of England Ambulance Service NHS Trust"}],
        "description": "EEAST's £45.29M transport line covers fuel (DERV), vehicle leasing, AMAP staff mileage, vehicle maintenance and Patient Transport Service running cost across Bedfordshire, Cambridgeshire, Essex, Hertfordshire, Norfolk and Suffolk. The trust runs c. 1,000 emergency vehicles across a region that combines London commuter belt (Hertfordshire, Essex) with deeply rural Norfolk Fens, Broads and Suffolk coastal areas — driving significant rural-mileage exposure alongside high A14 / M11 / M25 motorway-incident workload.",
        "beneficiaries": "Serves a c. 6.2M resident population across the East of England (Beds, Cambs, Essex, Herts, Norfolk, Suffolk); responds to c. 1.2M 999 calls/yr; c. 5,500 WTE staff including c. 4,000 frontline paramedics + EMTs operating from c. 130 ambulance stations and Make Ready Centres including hub sites at Norwich, Chelmsford, Stevenage.",
        "legal_basis": "NHS Act 2006 · NHSE Patient Transport Services Eligibility Criteria · Agenda for Change s.17 + HMRC Approved Mileage Allowance Payments · IFRS 16 Leases (pool fleet) · DHSC Group Accounting Manual 2024-25 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£45.29M"},
            {"label": "Geographic footprint", "value": "c. 19,000 km² across 6 counties (Beds, Cambs, Essex, Herts, Norfolk, Suffolk)"},
            {"label": "Fleet scale", "value": "c. 1,000 emergency vehicles (DCAs, RRVs, critical-care cars)"},
            {"label": "999 call volume", "value": "c. 1.2M emergency calls/yr"},
            {"label": "Population served", "value": "c. 6.2M residents — high rural Norfolk Fens + Broads + Suffolk coastal exposure"},
            {"label": "Workforce", "value": "c. 5,500 WTE; c. 4,000 frontline paramedics + EMTs"},
            {"label": "CQC special-measures history", "value": "EEAST entered NHSE recovery support 2022 after CQC ratings — operational + cultural improvement plan reshaped fleet utilisation; line stabilised through 2023-24"},
            {"label": "Cat-1 8-min standard", "value": "Cat-1 mean target challenged by rural Norfolk + Suffolk geography; CFR scheme dependency in coastal areas"},
            {"label": "Funding trajectory", "value": "DERV cost growth 2022-23 + 2023-24 industrial action backfill mileage + IFRS 16 lease re-recognition 2022 lifted line vs c. £35M pre-2021"},
            {"label": "Delivery body", "value": "EEAST Fleet & Logistics directorate + leased-fleet partners + Magpas Air Ambulance + EAAA partner charity HEMS"},
            {"label": "Policy owner", "value": "NHSE Urgent & Emergency Care directorate (ARP) + DHSC + 6 East of England ICBs"},
            {"label": "Evaluation evidence", "value": "ORH ambulance benchmarking; AACE annual reports; CQC inspections; NHSE AQI monthly returns; NHSE recovery support oversight returns"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2006 East Anglian + Essex + Beds & Herts ambulance services merged into EEAST · Successor: zero-emission fleet pilot under NHSE Net Zero 2032 plan"}
        ],
        "notes": "EEAST's transport line reflects a region of extreme geographic heterogeneity — dense Hertfordshire/Essex commuter towns alongside rural Norfolk Fens, Suffolk coast and Cambridgeshire farmland. The trust entered NHSE recovery support in 2022 after CQC concerns, with fleet utilisation and operational productivity central to the recovery plan. Sustained DERV price growth across 2022-24, the 2022 IFRS 16 transition that brought leased pool fleet onto the recognised charge, and the 2023-24 GMB+Unison paramedic industrial action backfill mileage all feed into the current £45.29M figure. Air-ambulance HEMS partnerships with Magpas (Cambs) and East Anglian Air Ambulance reduce some long-distance ground-mileage exposure but are charity-funded.",
        "sources": [
            {"publisher": "East of England Ambulance Service NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.eastamb.nhs.uk/about-us/publications.htm"},
            {"publisher": "NHS England", "title": "Ambulance Quality Indicators (monthly statistics)", "url": "https://www.england.nhs.uk/statistics/statistical-work-areas/ambulance-quality-indicators/"},
            {"publisher": "Care Quality Commission", "title": "EEAST provider profile (RYC)", "url": "https://www.cqc.org.uk/provider/RYC"},
            {"publisher": "Association of Ambulance Chief Executives", "title": "AACE Annual Report and ambulance benchmarking", "url": "https://aace.org.uk/"},
            {"publisher": "National Audit Office", "title": "NHS ambulance services (HC 972, 2017)", "url": "https://www.nao.org.uk/reports/nhs-ambulance-services/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"}
        ],
        "related": ["East of England Ambulance Service NHS Trust", "Premises & Infrastructure", "NHS Ambulance Trusts", "Transport (business + patient) — North West Ambulance Service NHS Trust", "Transport (business + patient) — East Midlands Ambulance Service NHS Trust", "NHS England"]
    },
    "General supplies & services — London Ambulance Service NHS Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "London Ambulance Service NHS Trust"}],
        "description": "LAS's £42.19M general supplies & services line covers non-clinical consumables, uniforms (paramedic + EMT high-vis + body armour), stationery, IT consumables, hotel-services materials at the c. 70 ambulance stations and Make Ready Centres, vehicle deep-clean supplies, infection-control consumables (PPE retained from COVID-era sourcing), and the running supplies for the 999 + 111 Emergency Operations Centres (Waterloo + Newham). Make Ready Centre vehicle preparation drives a high-volume cleaning + minor-equipment baseline distinct from acute trusts.",
        "beneficiaries": "Supports c. 8,500 WTE staff across c. 70 ambulance stations + 5 Make Ready Centres + 2 EOCs serving 9 million Greater London residents and an additional c. 21M annual visitor-day tourist load; LAS handles c. 2.0M emergency 999 calls/yr — highest volume of any English ambulance trust.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 2 Inventories · Procurement Act 2023 · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "General supplies & services 2024-25", "value": "£42.19M"},
            {"label": "Workforce", "value": "c. 8,500 WTE; c. 5,500 frontline clinicians + c. 1,200 EOC staff"},
            {"label": "Estate", "value": "c. 70 ambulance stations + 5 hub Make Ready Centres (Deptford, Friern Barnet, Brent, Bow, Croydon area)"},
            {"label": "Call volume", "value": "c. 2.0M 999 emergency calls/yr — highest English ambulance volume"},
            {"label": "Make Ready Centre model", "value": "Vehicle preparation hubs deep-clean + restock + bedding turnaround drive cleaning chemical + linen + minor-equipment consumable volume"},
            {"label": "PPE / infection control", "value": "Post-COVID elevated baseline — paramedic respirator stock + body armour + glove + apron volumes; some Pandemic Preparedness retained-stock components"},
            {"label": "Procurement route", "value": "NHS Supply Chain national framework + LAS-direct contracts + Crown Commercial Service framework"},
            {"label": "Industrial action 2023-24", "value": "Paramedic strikes drove cancellation re-stocking + agency-backfill consumable churn"},
            {"label": "April 2025 NIC + CPI uplift", "value": "Apr 2025 employer NIC step-up flow-through to outsourced cleaning + sustained CPI on non-clinical inputs feeds forward"},
            {"label": "Funding trajectory", "value": "2021-22 c. £30M (PPE-elevated) → 2022-23 £35M → 2023-24 £40M → 2024-25 £42.19M"},
            {"label": "Delivery body", "value": "LAS Procurement + Supply Chain team + NHS Supply Chain (DHSC ALB) + Crown Commercial Service frameworks"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + London ICBs"},
            {"label": "Evaluation evidence", "value": "Trust ARA disclosure; Model Hospital benchmarks (limited ambulance comparators); AACE non-clinical procurement returns"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2020 baseline before COVID PPE step-up · Successor: ongoing Net Zero procurement specification + zero-emission MRC re-fit specifications"}
        ],
        "notes": "LAS's general supplies & services baseline is structurally elevated by the Make Ready Centre operating model — vehicles are deep-cleaned, restocked and turned around at hub sites between shifts, driving high cleaning chemical, linen, minor-equipment and PPE consumable volumes that are a smaller line in pre-MRC ambulance estates. Post-COVID retained stock baselines on respirators and infection-control PPE remain elevated versus 2019. NHS Supply Chain provides the dominant procurement vehicle, with LAS-direct contracts for Met-Police-style body armour and London-specific kit. Industrial action 2023-24 drove cancellation-related churn; April 2025 NIC step-up flows through to outsourced cleaning contracts.",
        "sources": [
            {"publisher": "London Ambulance Service NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.londonambulance.nhs.uk/about-us/our-publications/annual-reports/"},
            {"publisher": "NHS Supply Chain", "title": "Annual Report 2023-24", "url": "https://www.supplychain.nhs.uk/about-us/our-publications/"},
            {"publisher": "Care Quality Commission", "title": "London Ambulance Service provider profile (RRU)", "url": "https://www.cqc.org.uk/provider/RRU"},
            {"publisher": "NHS England", "title": "Ambulance Quality Indicators (monthly statistics)", "url": "https://www.england.nhs.uk/statistics/statistical-work-areas/ambulance-quality-indicators/"},
            {"publisher": "Association of Ambulance Chief Executives", "title": "AACE Annual Report", "url": "https://aace.org.uk/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"}
        ],
        "related": ["London Ambulance Service NHS Trust", "Clinical Supplies & Drugs", "NHS Ambulance Trusts", "NHS Supply Chain", "Transport (business + patient) — London Ambulance Service NHS Trust", "Social security & levy — London Ambulance Service NHS Trust"]
    },
    "General supplies & services — Central London Community Healthcare NHS Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "Central London Community Healthcare NHS Trust"}],
        "description": "CLCH's £36.92M general supplies & services line covers non-clinical consumables, district-nursing kit bags, school-nursing pack supplies, end-of-life care community-stock provisioning, MSK community physio resistance bands and equipment, IT consumables and stationery across the trust's footprint covering Barnet, Hammersmith & Fulham, Kensington & Chelsea, Westminster, Hertfordshire (Watford, Three Rivers, Hertsmere) and Merton. Out-of-hospital community delivery into c. 2,700 patients' homes per day drives a high mobile-supplies baseline distinct from acute trust hospital-stock-room patterns.",
        "beneficiaries": "c. 4,200 WTE staff (the largest English community trust by workforce) serving a c. 2.0M registered population across 11 London boroughs + Hertfordshire districts + Merton; c. 2.7M community contacts/yr through district nursing, health visiting, school nursing, community paediatrics, end-of-life, MSK and walk-in centres; c. 250 service points across the catchment.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 2 Inventories · Procurement Act 2023 · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25 · Care Act 2014 (s.6 cooperation)",
        "key_stats": [
            {"label": "General supplies & services 2024-25", "value": "£36.92M"},
            {"label": "Workforce", "value": "c. 4,200 WTE — largest English community trust by staff"},
            {"label": "Footprint", "value": "11 London boroughs + Hertfordshire (Watford, Three Rivers, Hertsmere) + Merton; c. 250 service points"},
            {"label": "Population served", "value": "c. 2.0M registered residents"},
            {"label": "Activity", "value": "c. 2.7M community contacts/yr; district nursing + health visiting + school nursing + end-of-life + MSK community physio + walk-in centres"},
            {"label": "Community-care driver", "value": "Mobile workforce delivering into homes drives high van-stock + kit-bag consumable volume; school-nursing pack supplies + immunisation cold-chain consumables"},
            {"label": "Procurement route", "value": "NHS Supply Chain national framework + London ICS-collaborative procurement + trust-direct contracts"},
            {"label": "Three Shifts (Darzi) policy lift", "value": "Sep 2024 Darzi report + Three Shifts hospital-to-community policy direction lifts community-trust activity expectations 2025+"},
            {"label": "Funding trajectory", "value": "2021-22 c. £28M → 2022-23 £30M → 2023-24 £33M → 2024-25 £36.92M; sustained CPI + activity expansion"},
            {"label": "Delivery body", "value": "CLCH Procurement + NHS Supply Chain + London ICS collaborative procurement + NHS Property Services (premises/clinic supplies linked)"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + 4 London ICBs (NCL · NWL · SWL inc Merton · plus Herts & West Essex ICB)"},
            {"label": "Evaluation evidence", "value": "Trust ARA disclosure; CQC Outstanding rating maintained 2019 + 2022; Model Hospital community benchmarks; NHSE Community Services Data Set"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2010 PCT-provider arms across the central London boroughs · Successor: Three Shifts community lift + Neighbourhood Health Service planning under NHS 10-Year Plan"}
        ],
        "notes": "CLCH is the largest English community trust by workforce, providing community nursing, health visiting, school nursing, end-of-life and MSK community physio across 11 London boroughs plus Hertfordshire districts and Merton — a footprint that reflects 2010-era PCT-provider mergers consolidating central London community services. Its mobile-workforce model, with district nurses delivering into c. 2,700 homes daily, drives a higher van-stock + kit-bag consumable baseline than acute trusts. The September 2024 Darzi report and the government's Three Shifts policy direction (hospital-to-community) is set to lift community-trust activity from 2025 onwards, with consequent supplies expansion. The trust is a CQC Outstanding-rated provider since 2019.",
        "sources": [
            {"publisher": "Central London Community Healthcare NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://clch.nhs.uk/about-us/publications-and-reports"},
            {"publisher": "Department of Health and Social Care", "title": "Independent investigation of the NHS in England (Darzi report, Sep 2024)", "url": "https://www.gov.uk/government/publications/independent-investigation-of-the-nhs-in-england"},
            {"publisher": "Care Quality Commission", "title": "CLCH provider profile (RYX)", "url": "https://www.cqc.org.uk/provider/RYX"},
            {"publisher": "NHS Supply Chain", "title": "Annual Report 2023-24", "url": "https://www.supplychain.nhs.uk/about-us/our-publications/"},
            {"publisher": "NHS England", "title": "Community Services Data Set", "url": "https://digital.nhs.uk/data-and-information/data-collections-and-data-sets/data-sets/community-services-data-set"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"}
        ],
        "related": ["Central London Community Healthcare NHS Trust", "Clinical Supplies & Drugs", "NHS Community Trusts", "Social security & levy — Central London Community Healthcare NHS Trust", "Lease expenditure — Central London Community Healthcare NHS Trust", "NHS Supply Chain"]
    },
    "Transport (business + patient) — East Midlands Ambulance Service NHS Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "East Midlands Ambulance Service NHS Trust"}],
        "description": "EMAS's £34.79M transport line covers fuel, vehicle leasing, AMAP staff mileage, vehicle maintenance and PTS running cost across Derbyshire, Leicestershire & Rutland, Lincolnshire, Northamptonshire and Nottinghamshire. The trust runs c. 700 emergency vehicles across a region combining the Peak District National Park, rural Lincolnshire Wolds and Fens, and motorway-incident workload along the M1 / A1 / A14. Lincolnshire's geographic dispersion drives heavy AMAP rural-mileage exposure and Cat-1 8-min response challenge.",
        "beneficiaries": "Serves a c. 4.8M resident population across 5 East Midlands counties; responds to c. 950,000 emergency 999 calls/yr; c. 4,200 WTE staff including c. 3,000 frontline paramedics + EMTs operating from c. 70 ambulance stations and Make Ready hubs at Beechdale (Nottingham), Hinckley, Lincoln, Northampton.",
        "legal_basis": "NHS Act 2006 · NHSE Patient Transport Services Eligibility Criteria · Agenda for Change s.17 + HMRC Approved Mileage Allowance Payments · IFRS 16 Leases (pool fleet) · DHSC Group Accounting Manual 2024-25 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£34.79M"},
            {"label": "Geographic footprint", "value": "c. 16,000 km² across Derbys, Leics & Rutland, Lincs, Northants, Notts"},
            {"label": "Fleet scale", "value": "c. 700 emergency vehicles"},
            {"label": "999 call volume", "value": "c. 950,000 emergency calls/yr"},
            {"label": "Population served", "value": "c. 4.8M residents — Peak District + rural Lincolnshire Wolds + Fens drivers"},
            {"label": "Workforce", "value": "c. 4,200 WTE; c. 3,000 frontline clinicians"},
            {"label": "Make Ready hubs", "value": "Beechdale (Nottingham), Hinckley, Lincoln, Northampton — vehicle prep + restock model"},
            {"label": "Cat-1 8-min standard", "value": "Cat-1 mean target challenged by Lincolnshire dispersion + Peak District; LIVES (Lincolnshire CFR + BASICS) volunteer-doctor scheme support"},
            {"label": "Industrial action 2023-24", "value": "GMB + Unison strikes drove backfill mileage + agency-fleet-utilisation churn"},
            {"label": "Funding trajectory", "value": "DERV cost growth 2022-23 + IFRS 16 lease re-recognition 2022 + industrial action backfill mileage lifted line vs c. £25M pre-2021"},
            {"label": "Delivery body", "value": "EMAS Fleet & Logistics directorate + leased-fleet partners + LIVES + Lincs/Notts Air Ambulance partner charities"},
            {"label": "Policy owner", "value": "NHSE Urgent & Emergency Care directorate (ARP) + DHSC + 5 East Midlands ICBs"},
            {"label": "Evaluation evidence", "value": "ORH ambulance benchmarking; AACE annual reports; CQC inspections; NHSE AQI monthly returns"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2006 Derbys + Leics + Lincs + Northants + Notts ambulance services merged into EMAS · Successor: zero-emission fleet pilot under NHSE Net Zero 2032 plan"}
        ],
        "notes": "EMAS's transport baseline reflects the geographic challenge of Lincolnshire — one of England's most rural counties — combined with the Peak District National Park (Derbyshire), generating high AMAP rural-mileage exposure and challenging Cat-1 8-minute response performance. Volunteer schemes (LIVES — Lincolnshire BASICS doctors + Community First Responders) and Lincs & Notts Air Ambulance charity partnerships extend reach but are external to the cost base. Sustained DERV price growth across 2022-24, IFRS 16 lease re-recognition transition (2022), and industrial action backfill mileage in 2023-24 push the line to c. £35M. Net Zero 2032 fleet transition is operationally constrained by long Lincolnshire EV-range demands.",
        "sources": [
            {"publisher": "East Midlands Ambulance Service NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.emas.nhs.uk/about-us/our-publications/"},
            {"publisher": "NHS England", "title": "Ambulance Quality Indicators (monthly statistics)", "url": "https://www.england.nhs.uk/statistics/statistical-work-areas/ambulance-quality-indicators/"},
            {"publisher": "Care Quality Commission", "title": "EMAS provider profile (RX9)", "url": "https://www.cqc.org.uk/provider/RX9"},
            {"publisher": "Association of Ambulance Chief Executives", "title": "AACE Annual Report and ambulance benchmarking", "url": "https://aace.org.uk/"},
            {"publisher": "National Audit Office", "title": "NHS ambulance services (HC 972, 2017)", "url": "https://www.nao.org.uk/reports/nhs-ambulance-services/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"}
        ],
        "related": ["East Midlands Ambulance Service NHS Trust", "Premises & Infrastructure", "NHS Ambulance Trusts", "Transport (business + patient) — East of England Ambulance Service NHS Trust", "Transport (business + patient) — West Midlands Ambulance Service University NHS Foundation Trust", "NHS England"]
    },
    "Transport (business + patient) — Yorkshire Ambulance Service NHS Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "Yorkshire Ambulance Service NHS Trust"}],
        "description": "YAS's £28.11M transport line covers fuel, vehicle leasing, AMAP staff mileage, vehicle maintenance and PTS running cost across West, North, South and East Yorkshire (incl. Hull) and the Humber, plus the trust's NHS 111 service for the Yorkshire region. The fleet runs through the Yorkshire Dales, North York Moors and rural East Riding alongside the dense urban West Yorkshire conurbation (Leeds, Bradford, Wakefield, Sheffield). Trans-Pennine motorway-incident workload (M1, M62) and rural Dales response distances drive the line.",
        "beneficiaries": "Serves a c. 5.5M resident population across Yorkshire and the Humber; responds to c. 1.0M emergency 999 calls/yr; runs the regional NHS 111 service handling c. 2.5M calls/yr; c. 6,000 WTE staff including c. 3,800 frontline paramedics + EMTs operating from c. 60 ambulance stations and Make Ready Centres at Wakefield, Springhead Park (Hull), Sheffield, York.",
        "legal_basis": "NHS Act 2006 · NHSE Patient Transport Services Eligibility Criteria · Agenda for Change s.17 + HMRC Approved Mileage Allowance Payments · IFRS 16 Leases (pool fleet) · DHSC Group Accounting Manual 2024-25 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£28.11M"},
            {"label": "Geographic footprint", "value": "c. 15,400 km² across West, North, South and East Yorkshire + Humber"},
            {"label": "Fleet scale", "value": "c. 850 emergency vehicles + PTS fleet"},
            {"label": "999 call volume", "value": "c. 1.0M emergency calls/yr; YAS also runs Yorkshire NHS 111 (c. 2.5M calls/yr)"},
            {"label": "Population served", "value": "c. 5.5M residents — Dales + Moors + East Riding rural exposure alongside West Yorkshire urban density"},
            {"label": "Workforce", "value": "c. 6,000 WTE; c. 3,800 frontline clinicians"},
            {"label": "Make Ready Centres", "value": "Wakefield, Springhead Park (Hull), Sheffield, York hub model"},
            {"label": "Cat-1 8-min standard", "value": "Performance pressured by Dales + Moors rural geography; YAA + Air Ambulance partner charity HEMS support"},
            {"label": "Industrial action 2023-24", "value": "GMB + Unison strikes drove backfill mileage + agency-fleet-utilisation churn"},
            {"label": "Funding trajectory", "value": "DERV cost growth 2022-23 + IFRS 16 lease re-recognition 2022 + industrial action mileage backfill lifted line vs c. £20M pre-2021"},
            {"label": "Delivery body", "value": "YAS Fleet & Logistics directorate + leased-fleet partners + Yorkshire Air Ambulance charity HEMS"},
            {"label": "Policy owner", "value": "NHSE Urgent & Emergency Care directorate (ARP) + DHSC + 4 Yorkshire ICBs (West Yorkshire · South Yorkshire · Humber & North Yorkshire · plus North East ICB overlap)"},
            {"label": "Evaluation evidence", "value": "ORH ambulance benchmarking; AACE annual reports; CQC inspections; NHSE AQI monthly returns"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2006 West/North/South/East Yorkshire ambulance services merged into YAS · Successor: zero-emission fleet pilot under NHSE Net Zero 2032 plan"}
        ],
        "notes": "YAS's transport line reflects a region that combines dense West Yorkshire urban (Leeds, Bradford, Wakefield, Sheffield) with deeply rural Yorkshire Dales, North York Moors and East Riding, generating mixed Cat-1 response demand and significant rural AMAP mileage. The trust also runs Yorkshire NHS 111, a separate cost driver with c. 2.5M annual calls. Sustained DERV price growth across 2022-24, IFRS 16 lease re-recognition (2022), and 2023-24 industrial action backfill mileage all feed into the £28.11M line. Yorkshire Air Ambulance charity HEMS extends rural reach but is externally funded. Net Zero 2032 fleet transition is in pilot.",
        "sources": [
            {"publisher": "Yorkshire Ambulance Service NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.yas.nhs.uk/about-us/publications/annual-report-and-accounts/"},
            {"publisher": "NHS England", "title": "Ambulance Quality Indicators (monthly statistics)", "url": "https://www.england.nhs.uk/statistics/statistical-work-areas/ambulance-quality-indicators/"},
            {"publisher": "Care Quality Commission", "title": "YAS provider profile (RX8)", "url": "https://www.cqc.org.uk/provider/RX8"},
            {"publisher": "Association of Ambulance Chief Executives", "title": "AACE Annual Report", "url": "https://aace.org.uk/"},
            {"publisher": "National Audit Office", "title": "NHS ambulance services (HC 972, 2017)", "url": "https://www.nao.org.uk/reports/nhs-ambulance-services/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"}
        ],
        "related": ["Yorkshire Ambulance Service NHS Trust", "Premises & Infrastructure", "NHS Ambulance Trusts", "Transport (business + patient) — East Midlands Ambulance Service NHS Trust", "Transport (business + patient) — North West Ambulance Service NHS Trust", "Social security & levy — Yorkshire Ambulance Service NHS Trust"]
    },
    "Transport (business + patient) — West Midlands Ambulance Service University NHS Foundation Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "West Midlands Ambulance Service University NHS Foundation Trust"}],
        "description": "WMAS's £27.51M transport line covers fuel, vehicle leasing, AMAP staff mileage, vehicle maintenance and PTS running cost across Birmingham, Black Country, Coventry & Warwickshire, Herefordshire & Worcestershire, Shropshire & Telford, and Staffordshire & Stoke. WMAS has the highest Cat-1 8-minute response performance among English ambulance trusts and pioneered the hub-and-spoke Make Ready Centre model which concentrates fleet preparation at large central sites and reduces total estate cost.",
        "beneficiaries": "Serves a c. 5.9M resident population across the West Midlands; responds to c. 1.2M emergency 999 calls/yr; c. 6,500 WTE staff including c. 4,500 frontline paramedics + EMTs operating c. 900 emergency vehicles from c. 15 hub Make Ready Centres + c. 80 community ambulance stations across the region.",
        "legal_basis": "NHS Act 2006 · NHSE Patient Transport Services Eligibility Criteria · Agenda for Change s.17 + HMRC Approved Mileage Allowance Payments · IFRS 16 Leases (pool fleet) · DHSC Group Accounting Manual 2024-25 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£27.51M"},
            {"label": "Geographic footprint", "value": "c. 13,000 km² across 6 sub-regions"},
            {"label": "Fleet scale", "value": "c. 900 emergency vehicles concentrated at hub MRCs"},
            {"label": "999 call volume", "value": "c. 1.2M emergency calls/yr"},
            {"label": "Population served", "value": "c. 5.9M residents — Birmingham + Black Country urban dense alongside rural Shropshire + Herefordshire"},
            {"label": "Workforce", "value": "c. 6,500 WTE; c. 4,500 frontline clinicians"},
            {"label": "Cat-1 performance lead", "value": "Consistently best-performing English ambulance trust on Cat-1 8-min standard — hub-and-spoke MRC model + Make Ready model pioneer"},
            {"label": "University trust status", "value": "WMAS Foundation Trust holds 'University' designation reflecting paramedic education partnerships"},
            {"label": "Industrial action 2023-24", "value": "GMB + Unison strikes drove backfill mileage; WMAS comparatively less impacted"},
            {"label": "Funding trajectory", "value": "DERV cost growth 2022-23 + IFRS 16 lease re-recognition 2022 + sustained activity growth lifted line vs c. £20M pre-2021"},
            {"label": "Delivery body", "value": "WMAS Fleet & Logistics directorate + leased-fleet partners + Midlands Air Ambulance charity HEMS partner"},
            {"label": "Policy owner", "value": "NHSE Urgent & Emergency Care directorate (ARP) + DHSC + 6 West Midlands ICBs"},
            {"label": "Evaluation evidence", "value": "ORH ambulance benchmarking (WMAS frequently top-quartile); AACE annual reports; CQC ratings; NHSE AQI monthly returns"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2006 West Midlands + Coventry/Warks + Hereford/Worcs + Shropshire + Staffs ambulance services merged into WMAS · Successor: zero-emission fleet pilot under NHSE Net Zero 2032 plan; ongoing MRC capacity expansion"}
        ],
        "notes": "WMAS is the consistent top-performer among English ambulance trusts on Cat-1 8-minute mean response and pioneered the hub-and-spoke Make Ready Centre model — concentrating vehicle preparation at large central sites with deep-clean and restock teams while paramedics rotate through community ambulance stations. The model lifts fleet utilisation and historically produced lower per-call transport unit cost. Sustained DERV price growth across 2022-24, IFRS 16 lease re-recognition (2022), and incremental fleet expansion to meet activity growth lifted the line to £27.51M. Midlands Air Ambulance charity HEMS partnership provides supplementary reach for rural Shropshire/Herefordshire incidents.",
        "sources": [
            {"publisher": "West Midlands Ambulance Service University NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://wmas.nhs.uk/about-us/our-publications/"},
            {"publisher": "NHS England", "title": "Ambulance Quality Indicators (monthly statistics)", "url": "https://www.england.nhs.uk/statistics/statistical-work-areas/ambulance-quality-indicators/"},
            {"publisher": "Care Quality Commission", "title": "WMAS provider profile (RYA)", "url": "https://www.cqc.org.uk/provider/RYA"},
            {"publisher": "Association of Ambulance Chief Executives", "title": "AACE Annual Report", "url": "https://aace.org.uk/"},
            {"publisher": "National Audit Office", "title": "NHS ambulance services (HC 972, 2017)", "url": "https://www.nao.org.uk/reports/nhs-ambulance-services/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"}
        ],
        "related": ["West Midlands Ambulance Service University NHS Foundation Trust", "Premises & Infrastructure", "NHS Ambulance Trusts", "Transport (business + patient) — East Midlands Ambulance Service NHS Trust", "Social security & levy — West Midlands Ambulance Service University NHS Foundation Trust", "NHS England"]
    },
    "Social security & levy — Yorkshire Ambulance Service NHS Trust": {
        "aliases": [{"name": "Social security & levy", "parent": "Yorkshire Ambulance Service NHS Trust"}],
        "description": "YAS's £25.91M social security & levy line is the employer National Insurance contribution + Apprenticeship Levy on its c. 6,000 WTE workforce, covering frontline paramedics, EMTs, EOC clinicians and the Yorkshire NHS 111 service staff. The line scales with Agenda for Change pay-bill — driven by 2023-24 AfC pay awards (5%+ consolidated), Cat-1 response rota intensity, NHS 111 staffing scale, and 2023-24 industrial-action backfill agency cost. The April 2025 employer-NIC step-up materially lifts the line forward.",
        "beneficiaries": "Funds employer-side NIC on c. 6,000 WTE YAS staff including c. 3,800 frontline paramedics + EMTs, EOC clinicians, and Yorkshire NHS 111 service workforce serving 5.5 million Yorkshire and Humber residents; YAS handles c. 1.0M emergency 999 calls + c. 2.5M NHS 111 calls/yr.",
        "legal_basis": "Social Security Contributions and Benefits Act 1992 · Apprenticeship Levy (Finance Act 2016) · Health and Social Care Levy Act 2021 (repealed Nov 2022) · Autumn Budget 2024 employer-NIC reform (15% / £5k threshold from 6 April 2025) · NHS Pension Scheme Regulations · DHSC GAM 2024-25 · NHS Act 2006",
        "key_stats": [
            {"label": "Social security & levy 2024-25", "value": "£25.91M"},
            {"label": "Workforce", "value": "c. 6,000 WTE; c. 3,800 frontline clinicians + Yorkshire NHS 111 staff"},
            {"label": "Population served", "value": "c. 5.5M Yorkshire + Humber residents"},
            {"label": "Activity", "value": "c. 1.0M 999 emergency calls + c. 2.5M NHS 111 calls/yr"},
            {"label": "AfC pay award 2023-24", "value": "5% consolidated + £1,250 non-consolidated lump sum lifted base pay; flow-through to NIC"},
            {"label": "Industrial action 2022-24", "value": "GMB + Unison paramedic strikes Dec 2022 - Feb 2024 drove agency backfill + payroll volatility"},
            {"label": "April 2025 NIC step-up", "value": "15% employer rate + £5k threshold from 6 Apr 2025; estimated £3-4M annualised step-up"},
            {"label": "Apprenticeship Levy", "value": "0.5% of pay-bill above £3M threshold — paramedic apprenticeship pathway active"},
            {"label": "Funding trajectory", "value": "2021-22 c. £18M → 2022-23 £21M → 2023-24 £24M → 2024-25 £25.91M; April 2025 NIC reform feeds forward"},
            {"label": "Delivery body", "value": "YAS HR + Payroll (NHS SBS payroll service) + HMRC employer NIC remittance + NHS Pensions"},
            {"label": "Policy owner", "value": "HM Treasury (NIC + Apprenticeship Levy) + HMRC + DHSC + NHSE Workforce directorate"},
            {"label": "Evaluation evidence", "value": "Trust ARA staff costs note; Model Hospital workforce benchmarks; NHSE Operational Plan returns; AACE workforce returns"},
            {"label": "Predecessor / successor", "value": "Predecessor: Health and Social Care Levy 1.25% (Apr-Nov 2022, repealed) · Successor: 6 April 2025 employer-NIC step-up to 15% / £5k threshold"}
        ],
        "notes": "YAS's social security & levy line scales with the c. 6,000 WTE workforce that supports both regional ambulance operations and the Yorkshire NHS 111 service — an unusual dual-service structure that lifts pay-bill versus pure ambulance peers of comparable population. The 2023-24 GMB+Unison paramedic industrial action drove substantial agency backfill volatility through this line during the dispute period. Looking forward, the April 2025 employer-NIC step-up to 15% with the £5k threshold is the single biggest single-year cost shock — DHSC has indicated partial public-sector compensation but YAS faces an estimated £3-4M annualised gross uplift before any compensating grant. Apprenticeship Levy applies at 0.5% above the £3M threshold; paramedic-apprenticeship pathways draw down levy spend.",
        "sources": [
            {"publisher": "Yorkshire Ambulance Service NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.yas.nhs.uk/about-us/publications/annual-report-and-accounts/"},
            {"publisher": "HM Treasury", "title": "Autumn Budget 2024 — employer National Insurance contributions changes", "url": "https://www.gov.uk/government/publications/autumn-budget-2024"},
            {"publisher": "HMRC", "title": "Employer National Insurance contributions guidance", "url": "https://www.gov.uk/national-insurance-rates-letters"},
            {"publisher": "NHS Employers", "title": "Agenda for Change pay scales 2024-25", "url": "https://www.nhsemployers.org/articles/pay-scales-202425"},
            {"publisher": "Care Quality Commission", "title": "YAS provider profile (RX8)", "url": "https://www.cqc.org.uk/provider/RX8"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"}
        ],
        "related": ["Yorkshire Ambulance Service NHS Trust", "Staff Costs", "NHS Ambulance Trusts", "Social security & levy — London Ambulance Service NHS Trust", "Social security & levy — West Midlands Ambulance Service University NHS Foundation Trust", "HM Treasury"]
    },
    "Social security & levy — West Midlands Ambulance Service University NHS Foundation Trust": {
        "aliases": [{"name": "Social security & levy", "parent": "West Midlands Ambulance Service University NHS Foundation Trust"}],
        "description": "WMAS's £25.80M social security & levy line is the employer National Insurance contribution + Apprenticeship Levy on its c. 6,500 WTE workforce — the largest English ambulance Foundation Trust workforce after LAS. The line scales with Agenda for Change pay-bill — driven by 2023-24 AfC pay awards (5%+), the trust's workforce expansion to support sustained Cat-1 8-min response leadership, paramedic-apprenticeship pathway draws on Levy, and 2023-24 industrial-action backfill. The April 2025 employer-NIC step-up materially lifts the line forward.",
        "beneficiaries": "Funds employer-side NIC on c. 6,500 WTE WMAS staff including c. 4,500 frontline paramedics + EMTs + EOC clinicians serving 5.9 million West Midlands residents; WMAS handles c. 1.2M emergency 999 calls/yr and operates the hub-and-spoke MRC model across c. 15 hub MRCs + c. 80 community ambulance stations.",
        "legal_basis": "Social Security Contributions and Benefits Act 1992 · Apprenticeship Levy (Finance Act 2016) · Health and Social Care Levy Act 2021 (repealed Nov 2022) · Autumn Budget 2024 employer-NIC reform (15% / £5k threshold from 6 April 2025) · NHS Pension Scheme Regulations · DHSC GAM 2024-25 · NHS Act 2006",
        "key_stats": [
            {"label": "Social security & levy 2024-25", "value": "£25.80M"},
            {"label": "Workforce", "value": "c. 6,500 WTE; c. 4,500 frontline clinicians"},
            {"label": "Population served", "value": "c. 5.9M West Midlands residents"},
            {"label": "Activity", "value": "c. 1.2M 999 emergency calls/yr"},
            {"label": "AfC pay award 2023-24", "value": "5% consolidated + £1,250 non-consolidated lump sum lifted base pay; flow-through to NIC"},
            {"label": "University trust status", "value": "WMAS holds 'University' designation reflecting paramedic education partnerships — drives Apprenticeship Levy use for paramedic apprenticeships"},
            {"label": "Industrial action 2022-24", "value": "WMAS comparatively less impacted than peer ambulance trusts but some agency backfill"},
            {"label": "April 2025 NIC step-up", "value": "15% employer rate + £5k threshold from 6 Apr 2025; estimated £3-4M annualised step-up"},
            {"label": "Apprenticeship Levy", "value": "0.5% pay-bill above £3M; paramedic apprenticeship pathway active drawing down Levy spend"},
            {"label": "Funding trajectory", "value": "2021-22 c. £18M → 2022-23 £21M → 2023-24 £24M → 2024-25 £25.80M; April 2025 NIC reform feeds forward"},
            {"label": "Delivery body", "value": "WMAS HR + Payroll (NHS SBS payroll) + HMRC NIC remittance + NHS Pensions"},
            {"label": "Policy owner", "value": "HM Treasury (NIC + Apprenticeship Levy) + HMRC + DHSC + NHSE Workforce directorate"},
            {"label": "Evaluation evidence", "value": "Trust ARA staff costs note; Model Hospital workforce benchmarks; NHSE Operational Plan returns; AACE workforce returns"},
            {"label": "Predecessor / successor", "value": "Predecessor: Health and Social Care Levy 1.25% (Apr-Nov 2022, repealed) · Successor: 6 April 2025 employer-NIC step-up to 15% / £5k threshold"}
        ],
        "notes": "WMAS carries one of the largest English ambulance pay-bills, reflecting workforce expansion that has supported the trust's consistent top-quartile Cat-1 8-min response performance. The University-trust designation drives Apprenticeship Levy uptake on paramedic-apprenticeship pathways, partially offsetting the gross levy charge. WMAS was comparatively less impacted by 2022-24 GMB+Unison industrial action than peer ambulance trusts. Looking forward, the April 2025 employer-NIC step-up to 15% with the £5k threshold is the biggest single-year cost shock — WMAS faces an estimated £3-4M annualised gross uplift before any DHSC compensating grant.",
        "sources": [
            {"publisher": "West Midlands Ambulance Service University NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://wmas.nhs.uk/about-us/our-publications/"},
            {"publisher": "HM Treasury", "title": "Autumn Budget 2024 — employer National Insurance contributions changes", "url": "https://www.gov.uk/government/publications/autumn-budget-2024"},
            {"publisher": "HMRC", "title": "Employer National Insurance contributions guidance", "url": "https://www.gov.uk/national-insurance-rates-letters"},
            {"publisher": "NHS Employers", "title": "Agenda for Change pay scales 2024-25", "url": "https://www.nhsemployers.org/articles/pay-scales-202425"},
            {"publisher": "Care Quality Commission", "title": "WMAS provider profile (RYA)", "url": "https://www.cqc.org.uk/provider/RYA"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"}
        ],
        "related": ["West Midlands Ambulance Service University NHS Foundation Trust", "Staff Costs", "NHS Ambulance Trusts", "Social security & levy — London Ambulance Service NHS Trust", "Social security & levy — Yorkshire Ambulance Service NHS Trust", "HM Treasury"]
    },
    "Social security & levy — Central London Community Healthcare NHS Trust": {
        "aliases": [{"name": "Social security & levy", "parent": "Central London Community Healthcare NHS Trust"}],
        "description": "CLCH's £25.70M social security & levy line is the employer National Insurance contribution + Apprenticeship Levy on the largest English community-trust workforce. The line scales with Agenda for Change pay-bill — driven by London weighting (Inner + Outer zone HCA supplements), 2023-24 AfC pay awards (5%+), district-nurse + health-visitor + school-nurse + MSK-physio workforce expansion, and Three Shifts hospital-to-community policy direction lifting community capacity. The April 2025 employer-NIC step-up materially lifts the line forward.",
        "beneficiaries": "Funds employer-side NIC on c. 4,200 WTE CLCH staff — the largest English community trust by workforce — including district nurses, health visitors, school nurses, MSK community physios, end-of-life clinicians and walk-in centre staff serving c. 2.0M residents across 11 London boroughs + Hertfordshire districts + Merton; c. 2.7M community contacts/yr.",
        "legal_basis": "Social Security Contributions and Benefits Act 1992 · Apprenticeship Levy (Finance Act 2016) · Health and Social Care Levy Act 2021 (repealed Nov 2022) · Autumn Budget 2024 employer-NIC reform (15% / £5k threshold from 6 April 2025) · NHS Pension Scheme Regulations · DHSC GAM 2024-25 · NHS Act 2006",
        "key_stats": [
            {"label": "Social security & levy 2024-25", "value": "£25.70M"},
            {"label": "Workforce", "value": "c. 4,200 WTE — largest English community trust by staff"},
            {"label": "London weighting", "value": "HCA Inner London + Outer London supplements lift base pay-bill vs non-London community trust peers"},
            {"label": "Population served", "value": "c. 2.0M residents across 11 London boroughs + Herts + Merton"},
            {"label": "Activity", "value": "c. 2.7M community contacts/yr"},
            {"label": "AfC pay award 2023-24", "value": "5% consolidated + £1,250 non-consolidated lump sum; flow-through to NIC"},
            {"label": "Three Shifts (Darzi) policy lift", "value": "Sep 2024 Darzi report + community-shift direction lifts trust workforce expectations 2025+"},
            {"label": "April 2025 NIC step-up", "value": "15% employer rate + £5k threshold from 6 Apr 2025; estimated £3-4M annualised step-up"},
            {"label": "Apprenticeship Levy", "value": "0.5% pay-bill above £3M; nursing-apprenticeship + AHP-apprenticeship pathways draw down Levy"},
            {"label": "Funding trajectory", "value": "2021-22 c. £19M → 2022-23 £22M → 2023-24 £24M → 2024-25 £25.70M; April 2025 NIC reform feeds forward"},
            {"label": "Delivery body", "value": "CLCH HR + Payroll (NHS SBS payroll) + HMRC NIC remittance + NHS Pensions"},
            {"label": "Policy owner", "value": "HM Treasury (NIC + Apprenticeship Levy) + HMRC + DHSC + NHSE Workforce directorate"},
            {"label": "Evaluation evidence", "value": "Trust ARA staff costs note; CQC Outstanding rating maintained 2019/2022; Model Hospital community workforce benchmarks"},
            {"label": "Predecessor / successor", "value": "Predecessor: Health and Social Care Levy 1.25% (Apr-Nov 2022, repealed) · Successor: 6 Apr 2025 NIC step-up + Three Shifts community-workforce expansion"}
        ],
        "notes": "CLCH carries the largest English community-trust pay-bill, reflecting London weighting, the integration of c. 4,200 WTE district nurses, health visitors, school nurses, community paediatrics, end-of-life clinicians and MSK community physios across 11 London boroughs plus Hertfordshire districts and Merton. The September 2024 Darzi report and the government's Three Shifts (hospital-to-community) policy direction are set to lift community-trust workforce 2025+, with consequent pay-bill expansion. April 2025 employer-NIC step-up to 15% with £5k threshold is the biggest single-year cost shock — estimated £3-4M annualised gross uplift. Apprenticeship Levy partially offset by trainee-nurse + AHP apprenticeship pathways.",
        "sources": [
            {"publisher": "Central London Community Healthcare NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://clch.nhs.uk/about-us/publications-and-reports"},
            {"publisher": "HM Treasury", "title": "Autumn Budget 2024 — employer NIC changes", "url": "https://www.gov.uk/government/publications/autumn-budget-2024"},
            {"publisher": "Department of Health and Social Care", "title": "Independent investigation of the NHS in England (Darzi report, Sep 2024)", "url": "https://www.gov.uk/government/publications/independent-investigation-of-the-nhs-in-england"},
            {"publisher": "NHS Employers", "title": "Agenda for Change pay scales 2024-25", "url": "https://www.nhsemployers.org/articles/pay-scales-202425"},
            {"publisher": "Care Quality Commission", "title": "CLCH provider profile (RYX)", "url": "https://www.cqc.org.uk/provider/RYX"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"}
        ],
        "related": ["Central London Community Healthcare NHS Trust", "Staff Costs", "NHS Community Trusts", "General supplies & services — Central London Community Healthcare NHS Trust", "Social security & levy — Birmingham Community Healthcare NHS Foundation Trust", "HM Treasury"]
    },
    "Social security & levy — South Western Ambulance Service NHS Foundation Trust": {
        "aliases": [{"name": "Social security & levy", "parent": "South Western Ambulance Service NHS Foundation Trust"}],
        "description": "SWASFT's £24.02M social security & levy line is the employer National Insurance contribution + Apprenticeship Levy on its c. 5,000 WTE workforce, covering frontline paramedics, EMTs and EOC clinicians serving England's largest geographic ambulance footprint. The line scales with Agenda for Change pay-bill — driven by 2023-24 AfC pay awards (5%+), workforce expansion to maintain Cat-1 8-min response across rural Cornwall/Devon/Dorset distances, and 2023-24 industrial-action backfill agency cost. The April 2025 employer-NIC step-up materially lifts the line forward.",
        "beneficiaries": "Funds employer-side NIC on c. 5,000 WTE SWASFT staff including c. 3,500 frontline paramedics + EMTs + EOC clinicians serving 5.5 million South West residents plus tourist-population summer surge; SWASFT handles c. 1.0M emergency 999 calls/yr.",
        "legal_basis": "Social Security Contributions and Benefits Act 1992 · Apprenticeship Levy (Finance Act 2016) · Health and Social Care Levy Act 2021 (repealed Nov 2022) · Autumn Budget 2024 employer-NIC reform (15% / £5k threshold from 6 April 2025) · NHS Pension Scheme Regulations · DHSC GAM 2024-25 · NHS Act 2006",
        "key_stats": [
            {"label": "Social security & levy 2024-25", "value": "£24.02M"},
            {"label": "Workforce", "value": "c. 5,000 WTE; c. 3,500 frontline clinicians"},
            {"label": "Population served", "value": "c. 5.5M residents + c. 23M visitor-days/yr summer surge"},
            {"label": "Activity", "value": "c. 1.0M 999 emergency calls/yr"},
            {"label": "AfC pay award 2023-24", "value": "5% consolidated + £1,250 non-consolidated lump sum; flow-through to NIC"},
            {"label": "Industrial action 2022-24", "value": "GMB + Unison paramedic strikes drove agency backfill + payroll volatility"},
            {"label": "April 2025 NIC step-up", "value": "15% employer rate + £5k threshold from 6 Apr 2025; estimated £3M annualised step-up"},
            {"label": "Apprenticeship Levy", "value": "0.5% pay-bill above £3M — paramedic apprenticeship pathways draw down Levy"},
            {"label": "Rural-recruitment context", "value": "Cornwall + Devon retention challenges drive higher agency reliance + payroll volatility vs urban peers"},
            {"label": "Funding trajectory", "value": "2021-22 c. £17M → 2022-23 £20M → 2023-24 £22M → 2024-25 £24.02M; April 2025 NIC reform feeds forward"},
            {"label": "Delivery body", "value": "SWASFT HR + Payroll (NHS SBS payroll) + HMRC NIC remittance + NHS Pensions"},
            {"label": "Policy owner", "value": "HM Treasury (NIC + Apprenticeship Levy) + HMRC + DHSC + NHSE Workforce directorate"},
            {"label": "Evaluation evidence", "value": "Trust ARA staff costs note; Model Hospital workforce benchmarks; NHSE Operational Plan returns; AACE workforce returns"},
            {"label": "Predecessor / successor", "value": "Predecessor: Health and Social Care Levy 1.25% (Apr-Nov 2022, repealed) · Successor: 6 Apr 2025 NIC step-up to 15% / £5k threshold"}
        ],
        "notes": "SWASFT's pay-bill carries elevated cost relative to peer ambulance trusts because of Cornwall/Devon recruitment-retention challenges that drive agency backfill, especially during summer tourist surge when activity peaks against domestic-staff annual leave. The 2013 merger with Great Western Ambulance Service consolidated procurement and HR scale but did not solve the rural-recruitment dynamic. The 2023-24 GMB+Unison paramedic industrial action drove substantial agency volatility through this line. Looking forward, the April 2025 employer-NIC step-up to 15% with the £5k threshold is the biggest single-year cost shock — estimated £3M annualised gross uplift before any DHSC compensating grant.",
        "sources": [
            {"publisher": "South Western Ambulance Service NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.swast.nhs.uk/about-us/freedom-of-information/publications/annual-reports"},
            {"publisher": "HM Treasury", "title": "Autumn Budget 2024 — employer NIC changes", "url": "https://www.gov.uk/government/publications/autumn-budget-2024"},
            {"publisher": "HMRC", "title": "Employer National Insurance contributions guidance", "url": "https://www.gov.uk/national-insurance-rates-letters"},
            {"publisher": "NHS Employers", "title": "Agenda for Change pay scales 2024-25", "url": "https://www.nhsemployers.org/articles/pay-scales-202425"},
            {"publisher": "Care Quality Commission", "title": "SWASFT provider profile (RYF)", "url": "https://www.cqc.org.uk/provider/RYF"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"}
        ],
        "related": ["South Western Ambulance Service NHS Foundation Trust", "Staff Costs", "NHS Ambulance Trusts", "Transport (business + patient) — South Western Ambulance Service NHS Foundation Trust", "Social security & levy — South East Coast Ambulance Service NHS Foundation Trust", "HM Treasury"]
    },
    "Transport (business + patient) — London Ambulance Service NHS Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "London Ambulance Service NHS Trust"}],
        "description": "LAS's £22.60M transport line covers fuel (DERV), vehicle leasing, AMAP staff mileage, vehicle maintenance, motorbike + bicycle response unit running cost and Patient Transport Service across Greater London. The fleet runs c. 900 emergency vehicles (DCAs, RRVs, Cycle Response Units in central London, motorbikes) supporting Cat-1 8-min response in central-London traffic — a fundamentally different operating context from rural ambulance services where mileage rather than congestion is the cost driver.",
        "beneficiaries": "Serves a c. 9.0M Greater London resident population plus c. 21M annual visitor-days; c. 8,500 WTE staff including c. 5,500 frontline clinicians operating c. 900 emergency vehicles + Cycle Response Units across c. 70 ambulance stations and 5 hub Make Ready Centres; LAS handles c. 2.0M emergency 999 calls/yr.",
        "legal_basis": "NHS Act 2006 · NHSE Patient Transport Services Eligibility Criteria · Agenda for Change s.17 + HMRC Approved Mileage Allowance Payments · IFRS 16 Leases (pool fleet) · DHSC Group Accounting Manual 2024-25 · Health and Care Act 2022 · Greater London Low Emission Zone + ULEZ regulations",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£22.60M"},
            {"label": "Geographic footprint", "value": "c. 1,572 km² Greater London — densest English ambulance footprint by population/area"},
            {"label": "Fleet scale", "value": "c. 900 emergency vehicles + Cycle Response Units (CRU) + motorbikes for central London"},
            {"label": "999 call volume", "value": "c. 2.0M emergency calls/yr — highest English ambulance volume"},
            {"label": "Population + tourist surge", "value": "c. 9.0M residents + c. 21M visitor-days/yr"},
            {"label": "Workforce", "value": "c. 8,500 WTE; c. 5,500 frontline clinicians"},
            {"label": "ULEZ compliance", "value": "All LAS emergency vehicles required to meet ULEZ standards or hold emergency-services exemption; fleet renewal towards EV pilots"},
            {"label": "CRU + motorbikes", "value": "Central London Cycle Response Unit + motorbike RRVs reduce Cat-1 response time in congested West End; small fleet diversification"},
            {"label": "Cat-1 8-min standard", "value": "Cat-1 mean response in central-London traffic is congestion-driven not distance-driven; CRU + motorbike support"},
            {"label": "Funding trajectory", "value": "DERV cost growth 2022-23 + IFRS 16 lease re-recognition 2022 + 2023-24 industrial action backfill mileage lifted line vs c. £15M pre-2021"},
            {"label": "Delivery body", "value": "LAS Fleet & Logistics directorate + leased-fleet partners + London's Air Ambulance charity HEMS partner"},
            {"label": "Policy owner", "value": "NHSE Urgent & Emergency Care directorate (ARP) + DHSC + 5 London ICBs + GLA (ULEZ)"},
            {"label": "Evaluation evidence", "value": "ORH ambulance benchmarking; AACE annual reports; CQC inspections; NHSE AQI monthly returns; ULEZ-compliance returns to TfL"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-1996 LAS pre-acute-care reform · Successor: zero-emission fleet pilot under NHSE Net Zero 2032 plan + GLA Net Zero pressure"}
        ],
        "notes": "LAS's transport line is comparatively lower than other large-population ambulance trusts (NWAS at £59M, EEAST at £45M, SWASFT at £54M) because central-London geography means lower per-call mileage despite handling the highest call volume in England (c. 2M/yr) — congestion and dispatch density drive Cat-1 response, not distance. Cycle Response Units, motorbikes and Rapid Response Cars supplement DCAs in the West End. ULEZ + GLA Net Zero pressure accelerates fleet transition to EV pilots ahead of NHSE Net Zero 2032 ambulance road-fleet target. London's Air Ambulance charity HEMS provides supplementary trauma response.",
        "sources": [
            {"publisher": "London Ambulance Service NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.londonambulance.nhs.uk/about-us/our-publications/annual-reports/"},
            {"publisher": "NHS England", "title": "Ambulance Quality Indicators (monthly statistics)", "url": "https://www.england.nhs.uk/statistics/statistical-work-areas/ambulance-quality-indicators/"},
            {"publisher": "Care Quality Commission", "title": "London Ambulance Service provider profile (RRU)", "url": "https://www.cqc.org.uk/provider/RRU"},
            {"publisher": "Greater London Authority / Transport for London", "title": "Ultra Low Emission Zone (ULEZ) emergency-services guidance", "url": "https://tfl.gov.uk/modes/driving/ultra-low-emission-zone"},
            {"publisher": "Association of Ambulance Chief Executives", "title": "AACE Annual Report", "url": "https://aace.org.uk/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"}
        ],
        "related": ["London Ambulance Service NHS Trust", "Premises & Infrastructure", "NHS Ambulance Trusts", "Transport (business + patient) — North West Ambulance Service NHS Trust", "Social security & levy — London Ambulance Service NHS Trust", "General supplies & services — London Ambulance Service NHS Trust"]
    },
    "Social security & levy — Birmingham Community Healthcare NHS Foundation Trust": {
        "aliases": [{"name": "Social security & levy", "parent": "Birmingham Community Healthcare NHS Foundation Trust"}],
        "description": "BCHC's £21.15M social security & levy line is the employer National Insurance contribution + Apprenticeship Levy on its c. 4,500 WTE workforce providing community nursing, dental, learning-disability and children's community services across Birmingham. The line scales with Agenda for Change pay-bill — driven by 2023-24 AfC pay awards (5%+), workforce expansion under Three Shifts community direction, and dental + learning-disability service-line scale. The April 2025 employer-NIC step-up materially lifts the line forward.",
        "beneficiaries": "Funds employer-side NIC on c. 4,500 WTE BCHC staff including district nurses, community dental clinicians, learning-disability nurses + AHPs, children's community nurses, school nurses, health visitors and intermediate-care staff serving c. 1.2M Birmingham residents; c. 1.0M+ community contacts/yr.",
        "legal_basis": "Social Security Contributions and Benefits Act 1992 · Apprenticeship Levy (Finance Act 2016) · Health and Social Care Levy Act 2021 (repealed Nov 2022) · Autumn Budget 2024 employer-NIC reform (15% / £5k threshold from 6 April 2025) · NHS Pension Scheme Regulations · DHSC GAM 2024-25 · NHS Act 2006",
        "key_stats": [
            {"label": "Social security & levy 2024-25", "value": "£21.15M"},
            {"label": "Workforce", "value": "c. 4,500 WTE community + dental + LD + children's community staff"},
            {"label": "Population served", "value": "c. 1.2M Birmingham residents"},
            {"label": "Activity", "value": "c. 1.0M+ community contacts/yr; community dental + LD + children's services"},
            {"label": "Service-line breadth", "value": "Includes Community Dental Service (citywide), Learning Disability Service, Children's Community Nursing — broader than typical adult-community trusts"},
            {"label": "AfC pay award 2023-24", "value": "5% consolidated + £1,250 non-consolidated lump sum; flow-through to NIC"},
            {"label": "Three Shifts (Darzi) policy lift", "value": "Sep 2024 Darzi report + community-shift direction lifts trust workforce expectations 2025+"},
            {"label": "April 2025 NIC step-up", "value": "15% employer rate + £5k threshold from 6 Apr 2025; estimated £2-3M annualised step-up"},
            {"label": "Apprenticeship Levy", "value": "0.5% pay-bill above £3M; nursing + AHP apprenticeship pathways draw down Levy"},
            {"label": "Funding trajectory", "value": "2021-22 c. £15M → 2022-23 £18M → 2023-24 £20M → 2024-25 £21.15M; April 2025 NIC reform feeds forward"},
            {"label": "Delivery body", "value": "BCHC HR + Payroll (NHS SBS payroll) + HMRC NIC remittance + NHS Pensions"},
            {"label": "Policy owner", "value": "HM Treasury (NIC + Apprenticeship Levy) + HMRC + DHSC + NHSE Workforce + Birmingham & Solihull ICB"},
            {"label": "Evaluation evidence", "value": "Trust ARA staff costs note; CQC inspections; Model Hospital community workforce benchmarks"},
            {"label": "Predecessor / successor", "value": "Predecessor: Health and Social Care Levy 1.25% (Apr-Nov 2022, repealed) · Successor: 6 Apr 2025 NIC step-up + Three Shifts community-workforce expansion"}
        ],
        "notes": "BCHC carries a community-trust pay-bill that is unusually broad in service-line scope — combining standard adult community nursing with citywide community dental services, learning-disability community provision and children's community nursing. The c. 4,500 WTE workforce serves Birmingham, England's second-largest city, under Birmingham & Solihull ICB. 2023-24 AfC pay award flows through to NIC; the September 2024 Darzi report and Three Shifts community-direction lift workforce expectations 2025+. April 2025 employer-NIC step-up to 15% with £5k threshold is the biggest single-year cost shock — estimated £2-3M annualised gross uplift. Apprenticeship Levy partially offset by trainee-nurse + AHP pathways.",
        "sources": [
            {"publisher": "Birmingham Community Healthcare NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.bhamcommunity.nhs.uk/about-us/publications/"},
            {"publisher": "HM Treasury", "title": "Autumn Budget 2024 — employer NIC changes", "url": "https://www.gov.uk/government/publications/autumn-budget-2024"},
            {"publisher": "Department of Health and Social Care", "title": "Independent investigation of the NHS in England (Darzi report, Sep 2024)", "url": "https://www.gov.uk/government/publications/independent-investigation-of-the-nhs-in-england"},
            {"publisher": "NHS Employers", "title": "Agenda for Change pay scales 2024-25", "url": "https://www.nhsemployers.org/articles/pay-scales-202425"},
            {"publisher": "Care Quality Commission", "title": "BCHC provider profile (RYW)", "url": "https://www.cqc.org.uk/provider/RYW"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"}
        ],
        "related": ["Birmingham Community Healthcare NHS Foundation Trust", "Staff Costs", "NHS Community Trusts", "Social security & levy — Central London Community Healthcare NHS Trust", "Social security & levy — Northamptonshire Healthcare NHS Foundation Trust", "HM Treasury"]
    },
    "Social security & levy — Northamptonshire Healthcare NHS Foundation Trust": {
        "aliases": [{"name": "Social security & levy", "parent": "Northamptonshire Healthcare NHS Foundation Trust"}],
        "description": "NHFT's £20.59M social security & levy line is the employer National Insurance contribution + Apprenticeship Levy on the integrated community + mental-health + learning-disability workforce serving Northamptonshire. NHFT is one of England's combined community-and-mental-health trusts (rather than pure community), which lifts pay-bill scale relative to single-service-line community peers. The line scales with Agenda for Change pay-bill — driven by 2023-24 AfC awards (5%+) and 2025 employer-NIC reform.",
        "beneficiaries": "Funds employer-side NIC on c. 4,400 WTE NHFT staff providing community nursing, mental-health inpatient + community, learning-disability services, CAMHS, children's community + IAPT (NHS Talking Therapies) for c. 750,000 Northamptonshire residents (North Northants + West Northants); c. 1.2M+ community + mental-health contacts/yr.",
        "legal_basis": "Social Security Contributions and Benefits Act 1992 · Apprenticeship Levy (Finance Act 2016) · Health and Social Care Levy Act 2021 (repealed Nov 2022) · Autumn Budget 2024 employer-NIC reform (15% / £5k threshold from 6 April 2025) · NHS Pension Scheme Regulations · Mental Health Act 1983 (as amended) · DHSC GAM 2024-25 · NHS Act 2006",
        "key_stats": [
            {"label": "Social security & levy 2024-25", "value": "£20.59M"},
            {"label": "Workforce", "value": "c. 4,400 WTE; integrated community + mental-health + LD"},
            {"label": "Population served", "value": "c. 750,000 Northamptonshire residents (North Northants + West Northants unitaries)"},
            {"label": "Trust type", "value": "Combined Community + Mental-Health Trust — broader scope than pure community"},
            {"label": "Activity", "value": "c. 1.2M+ community + mental-health contacts/yr; CAMHS + IAPT + LD services"},
            {"label": "AfC pay award 2023-24", "value": "5% consolidated + £1,250 non-consolidated lump sum; flow-through to NIC"},
            {"label": "April 2025 NIC step-up", "value": "15% employer rate + £5k threshold from 6 Apr 2025; estimated £2-3M annualised step-up"},
            {"label": "Apprenticeship Levy", "value": "0.5% pay-bill above £3M; nursing + AHP + mental-health-nurse apprenticeship pathways draw down Levy"},
            {"label": "MH Act + LD context", "value": "Inpatient mental-health + LD wards drive 24/7 rota staffing — higher unsocial-hours premia + bank/agency vs pure community"},
            {"label": "Three Shifts (Darzi) policy lift", "value": "Sep 2024 Darzi report + community + mental-health shift direction lifts workforce expectations 2025+"},
            {"label": "Funding trajectory", "value": "2021-22 c. £15M → 2022-23 £17M → 2023-24 £19M → 2024-25 £20.59M; April 2025 NIC reform feeds forward"},
            {"label": "Delivery body", "value": "NHFT HR + Payroll (NHS SBS payroll) + HMRC NIC remittance + NHS Pensions"},
            {"label": "Policy owner", "value": "HM Treasury (NIC + Apprenticeship Levy) + HMRC + DHSC + NHSE Workforce + Northamptonshire ICB"},
            {"label": "Evaluation evidence", "value": "Trust ARA staff costs note; CQC inspections; Model Hospital community + MH workforce benchmarks"},
            {"label": "Predecessor / successor", "value": "Predecessor: Health and Social Care Levy 1.25% (Apr-Nov 2022, repealed) · Successor: 6 Apr 2025 NIC step-up + integrated provider model evolution"}
        ],
        "notes": "NHFT is one of the combined community + mental-health + LD trusts in England, with pay-bill scale lifted by 24/7 inpatient mental-health and learning-disability ward staffing alongside community nursing — a structural difference from pure community trusts. The c. 4,400 WTE workforce serves Northamptonshire (North + West unitaries since 2021 LGR) under Northamptonshire ICB. 2023-24 AfC pay award flows through to NIC; the September 2024 Darzi report and government Three Shifts direction lift community + mental-health workforce expectations 2025+. April 2025 employer-NIC step-up to 15% with £5k threshold is the biggest single-year cost shock — estimated £2-3M annualised gross uplift before any DHSC compensating grant.",
        "sources": [
            {"publisher": "Northamptonshire Healthcare NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.nhft.nhs.uk/about-us/our-publications/"},
            {"publisher": "HM Treasury", "title": "Autumn Budget 2024 — employer NIC changes", "url": "https://www.gov.uk/government/publications/autumn-budget-2024"},
            {"publisher": "Department of Health and Social Care", "title": "Independent investigation of the NHS in England (Darzi report, Sep 2024)", "url": "https://www.gov.uk/government/publications/independent-investigation-of-the-nhs-in-england"},
            {"publisher": "NHS Employers", "title": "Agenda for Change pay scales 2024-25", "url": "https://www.nhsemployers.org/articles/pay-scales-202425"},
            {"publisher": "Care Quality Commission", "title": "NHFT provider profile (RP1)", "url": "https://www.cqc.org.uk/provider/RP1"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"}
        ],
        "related": ["Northamptonshire Healthcare NHS Foundation Trust", "Staff Costs", "NHS Community Trusts", "Social security & levy — Central London Community Healthcare NHS Trust", "Social security & levy — Birmingham Community Healthcare NHS Foundation Trust", "HM Treasury"]
    },
    "Social security & levy — South East Coast Ambulance Service NHS Foundation Trust": {
        "aliases": [{"name": "Social security & levy", "parent": "South East Coast Ambulance Service NHS Foundation Trust"}],
        "description": "SECAmb's £20.48M social security & levy line is the employer National Insurance contribution + Apprenticeship Levy on its c. 4,500 WTE workforce, covering frontline paramedics, EMTs and EOC clinicians serving Kent, Surrey, Sussex and parts of north-east Hampshire. The line scales with Agenda for Change pay-bill — driven by 2023-24 AfC pay awards (5%+), London-fringe HCA supplements for Surrey + west Kent, sustained workforce expansion, and 2023-24 industrial-action backfill. The April 2025 employer-NIC step-up materially lifts the line forward.",
        "beneficiaries": "Funds employer-side NIC on c. 4,500 WTE SECAmb staff including c. 3,200 frontline paramedics + EMTs + EOC clinicians serving 4.7 million Kent + Surrey + Sussex + NE Hampshire residents; SECAmb handles c. 950,000 emergency 999 calls/yr.",
        "legal_basis": "Social Security Contributions and Benefits Act 1992 · Apprenticeship Levy (Finance Act 2016) · Health and Social Care Levy Act 2021 (repealed Nov 2022) · Autumn Budget 2024 employer-NIC reform (15% / £5k threshold from 6 April 2025) · NHS Pension Scheme Regulations · DHSC GAM 2024-25 · NHS Act 2006",
        "key_stats": [
            {"label": "Social security & levy 2024-25", "value": "£20.48M"},
            {"label": "Workforce", "value": "c. 4,500 WTE; c. 3,200 frontline clinicians"},
            {"label": "Population served", "value": "c. 4.7M Kent + Surrey + Sussex + NE Hants residents"},
            {"label": "Activity", "value": "c. 950,000 emergency 999 calls/yr"},
            {"label": "London-fringe HCA", "value": "Surrey + west Kent qualify for Outer London / Fringe HCA supplements lifting base pay vs pure provincial peers"},
            {"label": "AfC pay award 2023-24", "value": "5% consolidated + £1,250 non-consolidated lump sum; flow-through to NIC"},
            {"label": "Industrial action 2022-24", "value": "GMB + Unison paramedic strikes drove agency backfill + payroll volatility"},
            {"label": "April 2025 NIC step-up", "value": "15% employer rate + £5k threshold from 6 Apr 2025; estimated £2-3M annualised step-up"},
            {"label": "Apprenticeship Levy", "value": "0.5% pay-bill above £3M; paramedic apprenticeship pathways draw down Levy"},
            {"label": "Recent governance", "value": "SECAmb came out of NHSE recovery support 2022-23 after sustained operational improvement; payroll discipline part of recovery"},
            {"label": "Funding trajectory", "value": "2021-22 c. £15M → 2022-23 £17M → 2023-24 £19M → 2024-25 £20.48M; April 2025 NIC reform feeds forward"},
            {"label": "Delivery body", "value": "SECAmb HR + Payroll (NHS SBS payroll) + HMRC NIC remittance + NHS Pensions"},
            {"label": "Policy owner", "value": "HM Treasury (NIC + Apprenticeship Levy) + HMRC + DHSC + NHSE Workforce + Kent & Medway / Surrey Heartlands / Sussex / Hampshire & IoW ICBs"},
            {"label": "Evaluation evidence", "value": "Trust ARA staff costs note; Model Hospital workforce benchmarks; CQC inspections; AACE workforce returns"},
            {"label": "Predecessor / successor", "value": "Predecessor: Health and Social Care Levy 1.25% (Apr-Nov 2022, repealed) · Successor: 6 Apr 2025 NIC step-up to 15% / £5k threshold"}
        ],
        "notes": "SECAmb's pay-bill scales with the c. 4,500 WTE workforce serving Kent, Surrey, Sussex and parts of north-east Hampshire — a region that combines London-fringe (Surrey + west Kent qualifying for HCA Outer/Fringe supplements) with rural Sussex coast and Romney Marsh. The trust came out of NHSE recovery support 2022-23 after sustained operational improvement, with workforce + payroll discipline central to the recovery plan. 2023-24 GMB+Unison paramedic industrial action drove substantial agency volatility through this line. The April 2025 employer-NIC step-up to 15% with £5k threshold is the biggest single-year cost shock — estimated £2-3M annualised gross uplift before any DHSC compensating grant.",
        "sources": [
            {"publisher": "South East Coast Ambulance Service NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.secamb.nhs.uk/about_us/our_publications/annual_reports.aspx"},
            {"publisher": "HM Treasury", "title": "Autumn Budget 2024 — employer NIC changes", "url": "https://www.gov.uk/government/publications/autumn-budget-2024"},
            {"publisher": "HMRC", "title": "Employer National Insurance contributions guidance", "url": "https://www.gov.uk/national-insurance-rates-letters"},
            {"publisher": "NHS Employers", "title": "Agenda for Change pay scales 2024-25", "url": "https://www.nhsemployers.org/articles/pay-scales-202425"},
            {"publisher": "Care Quality Commission", "title": "SECAmb provider profile (RYD)", "url": "https://www.cqc.org.uk/provider/RYD"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"}
        ],
        "related": ["South East Coast Ambulance Service NHS Foundation Trust", "Staff Costs", "NHS Ambulance Trusts", "Social security & levy — South Western Ambulance Service NHS Foundation Trust", "Social security & levy — London Ambulance Service NHS Trust", "HM Treasury"]
    },
}
