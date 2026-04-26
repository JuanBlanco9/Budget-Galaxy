# -*- coding: utf-8 -*-
# Phase 2 MH slice 2 — chunk 02 (17 NHS Mental Health Trust orphan sub-lines)
# Hand-curated trust-specific PROGRAMME-archetype enrichment entries.
# Structural contract per docs/archetype_briefs.md.

NEW = {
    "Establishment costs — South London and Maudsley NHS Foundation Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "South London and Maudsley NHS Foundation Trust"}],
        "description": "SLaM is the largest specialist mental health and addictions provider in the UK and one of the four King's Health Partners AHSC trusts; its £2.81M 2024-25 establishment line covers premises running costs (telecoms, postage, water, refuse, food provisions) at Maudsley Hospital Denmark Hill, Bethlem Royal Park, Lambeth Hospital and the Lewisham/Croydon community estate. Volume is driven by 24/7 secure forensic and CAMHS Tier-4 wards plus National & Specialist services.",
        "beneficiaries": "Around 35,000-40,000 service users in 4 SE London boroughs (Lambeth, Southwark, Lewisham, Croydon) plus national specialist referrals; c. 5,500 staff across c. 230 sites; inpatient bed base c. 700 (acute, forensic, CAMHS, eating disorders) requires 24/7 catering, laundry and consumables.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 ch.5 (operating costs disclosure) · NHS Act 2006 · Health and Care Act 2022 · Mental Health Act 1983 (s.140 facilities duty) · IAS/IFRS",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£2.81M (largest MH-trust establishment line in slice 2)"},
            {"label": "5-year trend", "value": "2020-21 c. £2.0M → 2021-22 c. £2.1M → 2022-23 c. £2.4M → 2023-24 c. £2.6M → 2024-25 £2.81M (CPI + Bethlem catering insourcing)"},
            {"label": "Inpatient bed base driving food/laundry/consumables", "value": "c. 700 beds across Maudsley + Bethlem Royal + Lambeth + Lewisham"},
            {"label": "Site footprint", "value": "Maudsley Hospital (Denmark Hill, Camberwell), Bethlem Royal Hospital (Park), Lambeth Hospital, Ladywell Unit Lewisham, Croydon community estate"},
            {"label": "Specialist services driver", "value": "National & Specialist services (eating disorders, OCD, neuropsychiatry, mother-and-baby unit) with referrals from across England"},
            {"label": "Delivery body", "value": "SLaM Estates and Facilities directorate (in-house FM model, soft FM partly insourced 2022)"},
            {"label": "Policy owner", "value": "DHSC + NHSE Mental Health · South East London ICB commissioner"},
            {"label": "Funding trajectory", "value": "Above-CPI growth driven by food inflation, energy on top, and Bethlem on-site catering insourcing 2022-24"},
            {"label": "Evaluation evidence", "value": "CQC 'Good' overall 2024; NHSE benchmarking shows establishment cost per bed in upper quartile reflecting forensic + 24/7 specialist mix"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2022 ISS soft-FM contract (terminated, partial insourcing) · Successor: Douglas Bennett House replacement at Maudsley (Denmark Hill redevelopment)"}
        ],
        "notes": "SLaM's £2.81M establishment line is structurally larger than peer London MH trusts because the Bethlem Royal Park alone is a 270-acre site with full hospitality logistics for forensic and eating-disorder inpatients, and the National & Specialist services concentrate complex 24/7 admissions at Denmark Hill. The 2022 partial insourcing of soft FM (catering, portering) following the ISS contract review brought provisions and consumables onto the trust's establishment line rather than a contracted-out facilities line, contributing to the upward trajectory. Food inflation 2022-24 added a further structural step. The Denmark Hill redevelopment (Douglas Bennett House replacement) will reshape the line over the 2026-2030 cycle.",
        "sources": [
            {"publisher": "South London and Maudsley NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.slam.nhs.uk/about-us/publications/"},
            {"publisher": "NHS England", "title": "Mental health provider finance benchmarking 2024-25", "url": "https://www.england.nhs.uk/financial-accounts/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "South London and Maudsley NHS FT provider profile (RV5)", "url": "https://www.cqc.org.uk/provider/RV5"},
            {"publisher": "King's Health Partners", "title": "Academic Health Sciences Centre partner profile", "url": "https://www.kingshealthpartners.org/"}
        ],
        "related": ["South London and Maudsley NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Department of Health and Social Care", "Business rates — South London and Maudsley NHS Foundation Trust", "Establishment costs — Berkshire Healthcare NHS Foundation Trust"]
    },
    "General supplies & services — Sheffield Health and Social Care NHS Foundation Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "Sheffield Health and Social Care NHS Foundation Trust"}],
        "description": "SHSC is the integrated mental health, learning disability and substance-misuse provider for Sheffield, with adult acute wards at the Longley Centre (Northern General), older-adult inpatients at Grenoside Grange, plus city-wide CMHTs. The £2.77M 2024-25 general supplies & services line covers ward consumables (linen, gloves, dressings, food), small equipment under the capitalisation threshold, household items and non-prescription stock across c. 200 beds and c. 100 community sites. Driven by Talking Therapies and post-Lampard ligature-anchor replacement.",
        "beneficiaries": "Around 30,000 active service users across Sheffield (c. 580,000 population catchment); ~2,800 staff; inpatient base c. 200 beds at Longley Centre, Grenoside Grange and Forest Close; c. 100 community sites consuming PPE, dressings, household and non-clinical supplies.",
        "legal_basis": "IAS 2 Inventories · DHSC Group Accounting Manual 2024-25 ch.5 (consumables disclosure) · NHS Act 2006 · Health and Care Act 2022 · Mental Health Units (Use of Force) Act 2018",
        "key_stats": [
            {"label": "General supplies & services 2024-25", "value": "£2.77M"},
            {"label": "5-year trend", "value": "2020-21 c. £1.9M (PPE-elevated COVID base) → 2021-22 c. £2.0M → 2022-23 c. £2.3M → 2023-24 c. £2.5M → 2024-25 £2.77M"},
            {"label": "Inpatient bed base driving consumables", "value": "c. 200 beds at Longley Centre + Grenoside Grange + Forest Close"},
            {"label": "Site footprint", "value": "Longley Centre (Northern General), Grenoside Grange, Forest Close, Fulwood House, Michael Carlisle Centre, c. 100 community sites"},
            {"label": "Service-mix driver", "value": "Adult acute, older-adult inpatient, LD, drug-and-alcohol services + IAPT/Talking Therapies city-wide"},
            {"label": "Delivery body", "value": "SHSC procurement + NHS Supply Chain (CCS framework) for non-pharmaceutical consumables"},
            {"label": "Policy owner", "value": "DHSC + NHSE Mental Health · South Yorkshire ICB commissioner"},
            {"label": "Funding trajectory", "value": "CPI + ligature-anchor and anti-ligature furniture upgrade volume post-Lampard Inquiry recommendations"},
            {"label": "Evaluation evidence", "value": "CQC 'Requires Improvement' 2023 (subsequently improving); Lampard Inquiry findings flagging consumable-grade equipment standards"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2020-21 PPE-elevated COVID base · Successor: anti-ligature replacement programme tail through 2026-27"}
        ],
        "notes": "SHSC's £2.77M is shaped by the post-pandemic normalisation of PPE consumption combined with a sustained increase in ward safety equipment after the Lampard Inquiry into deaths in Essex MH inpatient services raised national focus on ligature-anchor replacement, anti-ligature furniture and observation consumables across all MH inpatient providers. Talking Therapies city-wide expansion adds non-clinical office consumables. SHSC's CQC trajectory from 'Requires Improvement' to 'Good' (sub-services) drove additional consumable spend on environment standards. South Yorkshire ICB capital is the route for larger-ticket anti-ligature works that fall above the supplies threshold.",
        "sources": [
            {"publisher": "Sheffield Health and Social Care NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.shsc.nhs.uk/about-us/who-we-are/publications"},
            {"publisher": "NHS England", "title": "Mental health provider finance benchmarking 2024-25", "url": "https://www.england.nhs.uk/financial-accounts/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Sheffield Health and Social Care NHS FT provider profile (TAH)", "url": "https://www.cqc.org.uk/provider/TAH"},
            {"publisher": "Lampard Inquiry", "title": "Essex Mental Health Independent Inquiry — interim findings", "url": "https://lampardinquiry.org.uk/"}
        ],
        "related": ["Sheffield Health and Social Care NHS Foundation Trust", "Clinical Supplies & Drugs", "NHS Mental Health Trusts", "Department of Health and Social Care", "Business rates — Sheffield Health and Social Care NHS Foundation Trust", "General supplies & services — Leeds and York Partnership NHS Foundation Trust"]
    },
    "Transport (business + patient) — Derbyshire Healthcare NHS Foundation Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "Derbyshire Healthcare NHS Foundation Trust"}],
        "description": "Derbyshire Healthcare provides MH, LD and substance-misuse services across the large Derbyshire ICS footprint, with adult acute inpatients at the Radbourne Unit (Royal Derby Hospital), Hartington Unit (Chesterfield Royal) and Kingsway Hospital Derby. The £2.76M 2024-25 transport line covers s.136 conveyance, secure-unit transfers, lease-car cost for community clinicians, and patient mileage in the Peak District catchment. Rural geography is the structural driver.",
        "beneficiaries": "Around 50,000 service users across Derbyshire (c. 1.05M population, including the largely rural High Peak, Derbyshire Dales and Bolsover districts); ~2,700 staff; community teams travel from Derby and Chesterfield bases to deliver care across c. 2,600 km² of mostly rural geography.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 ch.7 (transport disclosure) · NHS Act 2006 · Health and Care Act 2022 · Mental Health Act 1983 (s.136 conveyance) · IFRS 16 Leases (lease cars) · HMRC Approved Mileage Allowance Payments",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£2.76M"},
            {"label": "5-year trend", "value": "2020-21 c. £1.9M (COVID-suppressed travel) → 2021-22 c. £2.1M → 2022-23 c. £2.4M → 2023-24 c. £2.6M → 2024-25 £2.76M"},
            {"label": "Catchment geography", "value": "c. 2,600 km² covering Derby city + High Peak + Derbyshire Dales + Bolsover + Amber Valley + Erewash"},
            {"label": "Inpatient sites driving secure-transfer cost", "value": "Radbourne Unit (Royal Derby Hospital site), Hartington Unit (Chesterfield Royal site), Kingsway Hospital site"},
            {"label": "Lease-car fleet driver", "value": "c. 1,400 community-team clinicians use lease cars or own cars under HMRC AMAP rates"},
            {"label": "s.136 conveyance interaction", "value": "Joint pathway with EMAS and Derbyshire Constabulary; trust funds non-emergency MH transfers"},
            {"label": "Delivery body", "value": "Trust transport team + framework providers (NSL, ERS Medical) for patient-conveyance"},
            {"label": "Policy owner", "value": "DHSC + NHSE Mental Health · Joined Up Care Derbyshire ICB commissioner"},
            {"label": "Funding trajectory", "value": "CPI + fuel-price spike 2022-23 + AMAP-rate review pressure (HMRC rate held since 2011 at 45p/25p)"},
            {"label": "Evaluation evidence", "value": "CQC 'Good' 2024; HMICFRS s.136 review 2023 noted Derbyshire pathway pressures"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2017 commissioner contract for non-emergency patient transport · Successor: ICS-wide non-emergency transport recommissioning 2025-26"}
        ],
        "notes": "Derbyshire's £2.76M transport line is structurally elevated by the rural geography — High Peak, Derbyshire Dales and parts of Bolsover are among the most rural CCG-equivalent areas in England, and community mental health teams (CMHTs, IAPT, perinatal, older-adult) travel substantial distances to deliver home visits. The 2022-23 fuel-price spike compounded a longer-running pressure: HMRC's Approved Mileage Allowance Payment rate has held at 45p/25p since 2011 despite real-terms erosion, but trusts pay the gap when travel is essential. s.136 conveyance pressure peaked in 2023-24 as Derbyshire Constabulary's withdrawal from non-criminal mental-health response (Right Care, Right Person) pushed more transfers onto trust-funded providers.",
        "sources": [
            {"publisher": "Derbyshire Healthcare NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.derbyshirehealthcareft.nhs.uk/about-us/our-publications"},
            {"publisher": "NHS England", "title": "Mental health provider finance benchmarking 2024-25", "url": "https://www.england.nhs.uk/financial-accounts/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Derbyshire Healthcare NHS FT provider profile (RXM)", "url": "https://www.cqc.org.uk/provider/RXM"},
            {"publisher": "HMICFRS", "title": "Right Care, Right Person — police mental-health response review", "url": "https://hmicfrs.justiceinspectorates.gov.uk/"}
        ],
        "related": ["Derbyshire Healthcare NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Department of Health and Social Care", "Business rates — Derbyshire Healthcare NHS Foundation Trust", "Transport (business + patient) — Norfolk and Suffolk NHS Foundation Trust"]
    },
    "Establishment costs — Dorset Healthcare University NHS Foundation Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "Dorset Healthcare University NHS Foundation Trust"}],
        "description": "Dorset Healthcare is a combined community + mental health trust covering the Dorset and Bournemouth-Christchurch-Poole footprint, with adult mental health inpatient wards at St Ann's Hospital Poole and Forston Clinic Dorchester, older-adult inpatients at Alderney Hospital, plus community mental health teams across rural West Dorset and Purbeck. The £2.75M 2024-25 establishment line covers premises-related running costs (telecoms, postage, food provisions, water, refuse) across c. 100 sites, with elevated cost from the integrated community-and-MH model serving Dorset's older population.",
        "beneficiaries": "Around 230,000 patients seen yearly across mental health and community services for c. 800,000 Dorset residents; ~5,500 staff; c. 100 sites including community hospitals (Bridport, Sherborne, Wimborne) plus MH inpatient units (St Ann's, Forston Clinic, Alderney).",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 ch.5 (operating costs disclosure) · NHS Act 2006 · Health and Care Act 2022 · Mental Health Act 1983 · IAS/IFRS",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£2.75M"},
            {"label": "5-year trend", "value": "2020-21 c. £1.9M → 2021-22 c. £2.1M → 2022-23 c. £2.3M → 2023-24 c. £2.6M → 2024-25 £2.75M"},
            {"label": "Site footprint", "value": "c. 100 sites — 9 community hospitals + 3 MH inpatient units + community-team bases across rural Dorset"},
            {"label": "Inpatient bed base", "value": "MH inpatient c. 130 beds at St Ann's, Forston Clinic, Alderney + c. 380 community-hospital beds"},
            {"label": "Older-population driver", "value": "Dorset has one of the oldest demographic profiles in England — older-adult MH and community provision drives food, laundry, environmental costs"},
            {"label": "Delivery body", "value": "Dorset Healthcare Estates and Facilities + soft-FM contracts (catering and cleaning across community hospitals)"},
            {"label": "Policy owner", "value": "DHSC + NHSE Mental Health · NHS Dorset ICB commissioner"},
            {"label": "Funding trajectory", "value": "CPI-plus growth driven by food inflation and demographic-led older-adult inpatient occupancy"},
            {"label": "Evaluation evidence", "value": "CQC 'Good' overall 2024; NHSE benchmarking shows establishment cost per site below combined-trust average"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2011 merger of Dorset Community Health Services with Dorset Mental Health · Successor: NHS Dorset 'Healthy Places, Healthy Lives' estate strategy"}
        ],
        "notes": "Dorset Healthcare's £2.75M establishment line reflects the breadth of the integrated community + mental health model — the trust runs nine community hospitals (Bridport, Sherborne, Wimborne, Westminster Memorial, Yeatman, Portland, Swanage, Wareham, Blandford) alongside MH inpatient units, so establishment costs are spread across many small sites rather than concentrated at one main hospital. The Dorset population skews older than the England average, sustaining inpatient occupancy and catering volume on community-hospital wards. The NHS Dorset 'Healthy Places, Healthy Lives' strategy contemplates community-hospital reconfiguration which would reshape this line over the 2026-2030 cycle.",
        "sources": [
            {"publisher": "Dorset Healthcare University NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.dorsethealthcare.nhs.uk/about-us/publications"},
            {"publisher": "NHS England", "title": "Mental health provider finance benchmarking 2024-25", "url": "https://www.england.nhs.uk/financial-accounts/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Dorset Healthcare University NHS FT provider profile (RDY)", "url": "https://www.cqc.org.uk/provider/RDY"},
            {"publisher": "NHS Dorset ICB", "title": "Healthy Places, Healthy Lives strategy", "url": "https://www.nhsdorset.nhs.uk/"}
        ],
        "related": ["Dorset Healthcare University NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Department of Health and Social Care", "Business rates — Dorset Healthcare University NHS Foundation Trust", "Establishment costs — Berkshire Healthcare NHS Foundation Trust"]
    },
    "Transport (business + patient) — Surrey and Borders Partnership NHS Foundation Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "Surrey and Borders Partnership NHS Foundation Trust"}],
        "description": "Surrey and Borders Partnership delivers MH and learning-disability services across Surrey and parts of north-east Hampshire, with adult acute inpatients at the Abraham Cowley Unit (St Peter's Chertsey), Farnham Road Hospital Guildford, plus LD and forensic services. The £2.74M 2024-25 transport line covers s.136 conveyance, secure-unit transfers, lease-car cost for community clinicians, and Halliwick Centre intensive-support inter-site transfers. Surrey's commuter geography and high lease-car uptake structurally drive the line.",
        "beneficiaries": "Around 35,000 service users across Surrey (c. 1.2M population) plus north-east Hampshire and parts of west Sussex; ~3,000 staff; community teams travel from Chertsey, Guildford, Redhill and Leatherhead bases across c. 1,663 km² of mostly suburban geography.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 ch.7 (transport disclosure) · NHS Act 2006 · Health and Care Act 2022 · Mental Health Act 1983 (s.136 conveyance) · IFRS 16 Leases (lease cars) · HMRC AMAP",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£2.74M"},
            {"label": "5-year trend", "value": "2020-21 c. £2.0M → 2021-22 c. £2.2M → 2022-23 c. £2.4M → 2023-24 c. £2.6M → 2024-25 £2.74M"},
            {"label": "Catchment geography", "value": "Surrey c. 1,663 km² + north-east Hampshire + parts of west Sussex"},
            {"label": "Inpatient sites driving secure-transfer cost", "value": "Abraham Cowley Unit (St Peter's Chertsey), Farnham Road Hospital Guildford, Halliwick Centre"},
            {"label": "Lease-car fleet driver", "value": "High suburban lease-car uptake by community staff; trust salary-sacrifice fleet > peer average"},
            {"label": "s.136 conveyance interaction", "value": "Joint pathway with SECAmb and Surrey Police (Right Care, Right Person rolled out 2023)"},
            {"label": "Delivery body", "value": "Trust transport team + framework providers (NSL) for non-emergency patient-conveyance"},
            {"label": "Policy owner", "value": "DHSC + NHSE Mental Health · NHS Surrey Heartlands ICB + NHS Frimley ICB commissioners"},
            {"label": "Funding trajectory", "value": "CPI + 2022-23 fuel-price spike + Surrey Police RCRP 2023 transferring conveyance cost"},
            {"label": "Evaluation evidence", "value": "CQC 'Good' 2023; HMICFRS RCRP review 2023; trust scrutiny of Halliwick model post-2024 NHSE review"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2017 NHS Surrey commissioner contract for non-emergency transport · Successor: ICS-wide non-emergency MH transport recommissioning 2025-26"}
        ],
        "notes": "Surrey and Borders' £2.74M transport line is shaped by two structural drivers: a high-uptake salary-sacrifice lease-car scheme reflecting the trust's professional workforce and Surrey commuter context (lease-car fleet runs above peer-trust average); and the 2023 rollout of Right Care, Right Person across Surrey Police, which moved non-criminal MH conveyance from police vehicles onto trust-funded transport providers (NSL framework). The Halliwick Centre intensive-support service for learning-disability patients requires inter-site clinical transfers that add to the patient-transport component. AMAP-rate erosion since 2011 is the chronic background pressure shared with all rural-suburban trusts.",
        "sources": [
            {"publisher": "Surrey and Borders Partnership NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.sabp.nhs.uk/about-us/publications"},
            {"publisher": "NHS England", "title": "Mental health provider finance benchmarking 2024-25", "url": "https://www.england.nhs.uk/financial-accounts/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Surrey and Borders Partnership NHS FT provider profile (RXX)", "url": "https://www.cqc.org.uk/provider/RXX"},
            {"publisher": "HMICFRS", "title": "Right Care, Right Person — police mental-health response review", "url": "https://hmicfrs.justiceinspectorates.gov.uk/"}
        ],
        "related": ["Surrey and Borders Partnership NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Department of Health and Social Care", "Business rates — Surrey and Borders Partnership NHS Foundation Trust", "Establishment costs — Surrey and Borders Partnership NHS Foundation Trust"]
    },
    "General supplies & services — Leeds and York Partnership NHS Foundation Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "Leeds and York Partnership NHS Foundation Trust"}],
        "description": "LYPFT delivers MH and learning-disability services across Leeds and the York footprint and runs national specialist services for inpatient eating disorders, gender, deafness and personality disorder. The £2.73M 2024-25 general supplies & services line covers ward consumables, dressings, household items, food provisions and small clinical equipment under the capitalisation threshold across the Becklin Centre, Mount Hospital, Newsam Centre and Yorkshire Centre for Eating Disorders. National specialist case-mix drives consumable intensity above peer trusts.",
        "beneficiaries": "Around 28,000 service users across Leeds (c. 820,000 population) plus national specialist inpatient referrals (eating disorders, gender, deafness, PD); ~3,300 staff; inpatient base c. 250 beds across Becklin, Newsam, Mount, and the Yorkshire Centre at St James's University Hospital site.",
        "legal_basis": "IAS 2 Inventories · DHSC Group Accounting Manual 2024-25 ch.5 · NHS Act 2006 · Health and Care Act 2022 · Mental Health Units (Use of Force) Act 2018",
        "key_stats": [
            {"label": "General supplies & services 2024-25", "value": "£2.73M"},
            {"label": "5-year trend", "value": "2020-21 c. £2.0M (PPE base) → 2021-22 c. £2.0M → 2022-23 c. £2.3M → 2023-24 c. £2.5M → 2024-25 £2.73M"},
            {"label": "Inpatient bed base driving consumables", "value": "c. 250 beds across Becklin, Mount, Newsam, Yorkshire Centre + 4 PICUs"},
            {"label": "Site footprint", "value": "Becklin Centre (St James's), Mount Hospital (Burley), Newsam Centre (Seacroft), Yorkshire Centre for Eating Disorders, Asket Croft, Bootham Park (York legacy)"},
            {"label": "National specialist case-mix driver", "value": "Adult and adolescent inpatient eating disorders + Gender Identity Service + national deafness service drive enteral feed, NG tubes, specialist consumable spend"},
            {"label": "Delivery body", "value": "LYPFT procurement + NHS Supply Chain (CCS framework) for non-pharmaceutical consumables"},
            {"label": "Policy owner", "value": "DHSC + NHSE Mental Health · West Yorkshire ICB commissioner + NHSE specialised commissioning"},
            {"label": "Funding trajectory", "value": "Above-CPI growth driven by ED case-mix, anti-ligature replacement, food inflation"},
            {"label": "Evaluation evidence", "value": "CQC 'Good' 2024; NHSE benchmarking shows above-peer consumable intensity reflecting national specialist mix"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2012 Leeds Mental Health Teaching Trust + York legacy estate (Bootham Park closed 2015) · Successor: anti-ligature replacement programme tail through 2026-27"}
        ],
        "notes": "LYPFT's £2.73M is structurally above peer general MH trusts because the case-mix carries multiple national specialist services with high consumable intensity. The Yorkshire Centre for Eating Disorders runs adult and adolescent inpatient programmes requiring enteral nutrition (NG feeds), refeeding-syndrome consumables, and specialist monitoring; the National Deaf CAMHS service has interpreting and accessibility consumables; the Gender Identity Service consumes specialist clinical and assessment equipment. Anti-ligature replacement post-Lampard adds furniture-grade cost. The 2015 Bootham Park Hospital York closure narrowed the legacy footprint; the modern estate is the structural cost base.",
        "sources": [
            {"publisher": "Leeds and York Partnership NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.leedsandyorkpft.nhs.uk/about-us/publications/"},
            {"publisher": "NHS England", "title": "Mental health provider finance benchmarking 2024-25", "url": "https://www.england.nhs.uk/financial-accounts/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Leeds and York Partnership NHS FT provider profile (RGD)", "url": "https://www.cqc.org.uk/provider/RGD"},
            {"publisher": "Lampard Inquiry", "title": "Essex Mental Health Independent Inquiry — interim findings", "url": "https://lampardinquiry.org.uk/"}
        ],
        "related": ["Leeds and York Partnership NHS Foundation Trust", "Clinical Supplies & Drugs", "NHS Mental Health Trusts", "Department of Health and Social Care", "Establishment costs — Leeds and York Partnership NHS Foundation Trust", "General supplies & services — Sheffield Health and Social Care NHS Foundation Trust"]
    },
    "Establishment costs — Essex Partnership University NHS Foundation Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "Essex Partnership University NHS Foundation Trust"}],
        "description": "EPUT was created in 2017 from the merger of South Essex Partnership and North Essex Partnership and is the central trust under live scrutiny by the statutory Lampard Inquiry into deaths in Essex MH inpatient services 2000-2023. The £2.70M 2024-25 establishment line covers premises-related running costs (telecoms, postage, food, water, refuse) across acute MH wards at the Linden Centre Chelmsford, Basildon Mental Health Unit, Rochford Hospital, plus community-MH bases. Lampard-driven environmental upgrade programme is the structural cost driver beyond CPI.",
        "beneficiaries": "Around 70,000 service users across Essex (c. 1.85M population including Southend, Basildon, Chelmsford, Colchester, Tendring); ~5,800 staff; inpatient base c. 600 beds across Linden Centre, Basildon MHU, Rochford, Lakes/Peter Bruff, plus community sites.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 ch.5 · NHS Act 2006 · Health and Care Act 2022 · Mental Health Act 1983 · Inquiries Act 2005 (Lampard Inquiry context)",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£2.70M"},
            {"label": "5-year trend", "value": "2020-21 c. £1.9M → 2021-22 c. £2.1M → 2022-23 c. £2.4M → 2023-24 c. £2.6M → 2024-25 £2.70M"},
            {"label": "Inpatient bed base driving food/laundry/consumables", "value": "c. 600 beds — one of the larger MH inpatient footprints in England"},
            {"label": "Site footprint", "value": "Linden Centre Chelmsford, Basildon MHU, Rochford, The Lakes/Peter Bruff Colchester + community-team bases"},
            {"label": "Lampard Inquiry context", "value": "Trust at centre of statutory inquiry into deaths in Essex MH inpatient services 2000-2023; environmental and observation standards under scrutiny"},
            {"label": "Delivery body", "value": "EPUT Estates and Facilities + soft-FM contracts"},
            {"label": "Policy owner", "value": "DHSC + NHSE Mental Health · NHS Mid and South Essex ICB + NHS Suffolk and North East Essex ICB commissioners"},
            {"label": "Funding trajectory", "value": "CPI + Lampard-driven environmental remediation including anti-ligature furniture renewal and ward-fabric replacement"},
            {"label": "Evaluation evidence", "value": "CQC enforcement actions on inpatient services 2020-23; Lampard Inquiry interim findings 2024"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2017 merger of South + North Essex Partnership Trusts · Successor: post-Lampard inpatient environment programme + new MH inpatient builds in NHP successor capital"}
        ],
        "notes": "EPUT's £2.70M establishment line carries an unusually heavy post-merger transition tail combined with the cost of the Lampard-driven environmental remediation programme. The statutory Lampard Inquiry into deaths in Essex MH inpatient services 2000-2023 (chaired by Baroness Lampard, opened evidence 2024) has driven the trust to invest in anti-ligature furniture renewal, observation enhancement and ward-fabric replacement — much of which falls into establishment / supplies rather than capital because of unit cost. CQC enforcement actions on inpatient services through 2020-23 reinforced the same pressure. ICB capital is the route for larger ticket items but the establishment line carries the granular consumable-grade portion of the remediation.",
        "sources": [
            {"publisher": "Essex Partnership University NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://eput.nhs.uk/about-us/publications/"},
            {"publisher": "Lampard Inquiry", "title": "Essex Mental Health Independent Inquiry", "url": "https://lampardinquiry.org.uk/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "EPUT provider profile (RWN)", "url": "https://www.cqc.org.uk/provider/RWN"},
            {"publisher": "NHS England", "title": "Mental health provider finance benchmarking 2024-25", "url": "https://www.england.nhs.uk/financial-accounts/"}
        ],
        "related": ["Essex Partnership University NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Department of Health and Social Care", "Business rates — Essex Partnership University NHS Foundation Trust", "Lease expenditure — Essex Partnership University NHS Foundation Trust"]
    },
    "Lease expenditure — Oxford Health NHS Foundation Trust": {
        "aliases": [{"name": "Lease expenditure", "parent": "Oxford Health NHS Foundation Trust"}],
        "description": "Oxford Health is a combined community + mental health trust with services across Oxfordshire, Buckinghamshire, Bath and North East Somerset, Swindon and Wiltshire. The £2.70M 2024-25 lease expenditure line is the IFRS 16 right-of-use asset opex post-2022 transition: it captures payments to NHS Property Services for community-clinic estate (Health Centres in Oxford city and Bicester, Banbury, Witney) plus third-party landlord leases for CMHT bases. NHSPS service-charge dispute — common across MH trusts — is the structural cost driver.",
        "beneficiaries": "Around 200,000 patient contacts annually across Oxfordshire (c. 730,000), Buckinghamshire and BSW; ~7,000 staff; community-clinic estate of c. 130 sites including the Warneford Hospital MH inpatient site, Whiteleaf Centre Aylesbury, Marlborough House CAMHS, plus NHSPS-leased Oxford city Health Centres.",
        "legal_basis": "IFRS 16 Leases · DHSC Group Accounting Manual 2024-25 ch.7 · NHS Act 2006 · Health and Care Act 2022 · Landlord and Tenant Act 1954",
        "key_stats": [
            {"label": "Lease expenditure 2024-25", "value": "£2.70M (IFRS 16 right-of-use opex)"},
            {"label": "5-year trend", "value": "2020-21 c. £0.7M (pre-IFRS 16) → 2021-22 c. £0.8M → 2022-23 c. £2.4M (IFRS 16 transition jump) → 2023-24 c. £2.6M → 2024-25 £2.70M"},
            {"label": "IFRS 16 transition driver", "value": "April 2022 implementation under DHSC GAM brought NHSPS clinic-estate occupancy onto balance sheet as right-of-use assets, with depreciation + interest replacing rental opex"},
            {"label": "NHSPS lease portfolio", "value": "Multiple Oxford community Health Centres + town-centre clinics held under NHSPS occupancy charge — disputed nationally on service-charge scope"},
            {"label": "Third-party leased estate", "value": "Selected CMHT bases held under high-street and business-park commercial leases"},
            {"label": "Specialist site driver", "value": "Warneford Hospital — historic Oxford MH site with mixed-tenure estate; redevelopment programme under exploration"},
            {"label": "Delivery body", "value": "Oxford Health Estates + NHSPS landlord + commercial agents"},
            {"label": "Policy owner", "value": "DHSC + NHSE Estates · NHS Buckinghamshire, Oxfordshire and Berkshire West ICB + NHS BSW ICB commissioners"},
            {"label": "Funding trajectory", "value": "CPI-linked; structural step-up complete; future driven by NHSPS dispute resolution + Warneford redevelopment"},
            {"label": "Evaluation evidence", "value": "CQC 'Good' overall 2024; NAO IFRS 16 implementation report 2023; ongoing NHSPS / NHS provider service-charge dispute"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2022 IAS 17 operating-lease expense · Successor: Warneford Hospital redevelopment + NHSPS service-charge negotiation outcome"}
        ],
        "notes": "Oxford Health's £2.70M IFRS 16 lease line shows the classic 2022 transition jump (sub-£1M pre-2022 → £2.4M+ post-transition) as community-clinic occupancy moved from rental opex into the right-of-use asset amortisation + interest model under DHSC GAM ch.7. The largest landlord is NHSPS, which delivers Oxford city and town-centre Health Centres and is in long-running national dispute with NHS providers over service-charge scope (cleaning, security, life-cycle maintenance recharges); MH trusts are particularly exposed because their community footprint is heavily NHSPS-leased. The Warneford Hospital redevelopment exploration with Oxford University would reshape the line in the medium term.",
        "sources": [
            {"publisher": "Oxford Health NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.oxfordhealth.nhs.uk/about-us/publications/"},
            {"publisher": "NHS Property Services", "title": "Service charge dispute and tenant communications", "url": "https://www.property.nhs.uk/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Oxford Health NHS FT provider profile (RNU)", "url": "https://www.cqc.org.uk/provider/RNU"},
            {"publisher": "National Audit Office", "title": "IFRS 16 implementation across the public sector", "url": "https://www.nao.org.uk/"}
        ],
        "related": ["Oxford Health NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "NHS Property Services Ltd", "Amortisation — Oxford Health NHS Foundation Trust", "Lease expenditure — Mersey Care NHS Foundation Trust"]
    },
    "Transport (business + patient) — Rotherham Doncaster and South Humber NHS Foundation Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "Rotherham Doncaster and South Humber NHS Foundation Trust"}],
        "description": "RDaSH delivers MH, community physical health and learning-disability services across Rotherham, Doncaster and parts of North Lincolnshire. The £2.68M 2024-25 transport line covers patient-conveyance for s.136 detentions, secure transfers, lease-car cost for community-team clinicians driving between Rotherham, Doncaster and rural North Lincolnshire bases, plus business mileage for community physical-health home visits. The combined MH + community footprint and rural North Lincolnshire catchment are the structural cost drivers.",
        "beneficiaries": "Around 90,000 patient contacts annually across Rotherham (c. 270,000), Doncaster (c. 320,000) and North Lincolnshire (c. 170,000); ~3,500 staff; community teams operate from c. 80 sites including Tickhill Road Hospital Doncaster (main MH inpatient), Swallownest Court Rotherham, Great Oaks Scunthorpe.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 ch.7 · NHS Act 2006 · Health and Care Act 2022 · Mental Health Act 1983 (s.136) · IFRS 16 Leases · HMRC AMAP",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£2.68M"},
            {"label": "5-year trend", "value": "2020-21 c. £1.9M (COVID-suppressed) → 2021-22 c. £2.1M → 2022-23 c. £2.4M → 2023-24 c. £2.5M → 2024-25 £2.68M"},
            {"label": "Catchment geography", "value": "Rotherham + Doncaster + North Lincolnshire — c. 1,700 km² with rural North Lincs adding to mileage profile"},
            {"label": "Inpatient sites driving secure-transfer cost", "value": "Tickhill Road Hospital Doncaster, Swallownest Court Rotherham, Great Oaks Scunthorpe"},
            {"label": "Service-mix driver", "value": "Combined MH + community-physical-health model means home-visit mileage on top of MH conveyance"},
            {"label": "Lease-car fleet", "value": "Salary-sacrifice fleet for community-team clinicians"},
            {"label": "s.136 conveyance interaction", "value": "Joint pathway with YAS, EMAS and Humberside / South Yorkshire Police; RCRP rolled out across both forces 2023-24"},
            {"label": "Delivery body", "value": "Trust transport team + framework providers (NSL) for non-emergency"},
            {"label": "Policy owner", "value": "DHSC + NHSE Mental Health · South Yorkshire ICB + Humber and North Yorkshire ICB commissioners"},
            {"label": "Funding trajectory", "value": "CPI + 2022-23 fuel-price spike + RCRP volume transfer 2023-24"},
            {"label": "Evaluation evidence", "value": "CQC 'Good' 2024; HMICFRS RCRP review; trust ARA disclosure on RCRP cost shift"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2017 separate Rotherham + Doncaster + South Humber legacy contracts · Successor: ICS-wide non-emergency MH transport recommissioning 2025-26"}
        ],
        "notes": "RDaSH's £2.68M transport line is shaped by the combined MH + community-physical-health model — community nurses and therapists drive between patients' homes across rural North Lincolnshire alongside MH-team mileage. The Right Care, Right Person rollout across both Humberside Police and South Yorkshire Police in 2023-24 transferred conveyance volume from police vehicles onto trust-funded providers, contributing to the upward step-change. AMAP-rate erosion since 2011 (45p/25p unchanged) compounds the structural pressure. The trust's footprint spans two ICBs (South Yorkshire and Humber and North Yorkshire), adding contracting complexity.",
        "sources": [
            {"publisher": "Rotherham Doncaster and South Humber NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.rdash.nhs.uk/about-us/our-publications/"},
            {"publisher": "NHS England", "title": "Mental health provider finance benchmarking 2024-25", "url": "https://www.england.nhs.uk/financial-accounts/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "RDaSH provider profile (RXE)", "url": "https://www.cqc.org.uk/provider/RXE"},
            {"publisher": "HMICFRS", "title": "Right Care, Right Person — police mental-health response review", "url": "https://hmicfrs.justiceinspectorates.gov.uk/"}
        ],
        "related": ["Rotherham Doncaster and South Humber NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Department of Health and Social Care", "Establishment costs — Rotherham Doncaster and South Humber NHS Foundation Trust", "Transport (business + patient) — Pennine Care NHS Foundation Trust"]
    },
    "Transport (business + patient) — Pennine Care NHS Foundation Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "Pennine Care NHS Foundation Trust"}],
        "description": "Pennine Care delivers MH and learning-disability services across the five north-east Greater Manchester boroughs (Bury, Oldham, Rochdale, Stockport, Tameside) plus a slice of Glossop. The £2.66M 2024-25 transport line covers patient-conveyance for s.136 detentions, secure transfers, lease-car cost for community CMHT clinicians and the post-Edenfield Centre out-of-area placement transfer cost — a structural driver that emerged after BBC Panorama exposure of the Edenfield Centre forensic ward (Greater Manchester Mental Health) in 2022 forced wider GM patient flow reconfiguration.",
        "beneficiaries": "Around 60,000 service users across the five north-east GM boroughs (Bury, Oldham, Rochdale, Stockport, Tameside, total population c. 1.2M); ~3,500 staff; community teams operate from c. 100 sites including the Meadowbrook Unit Salford, Tameside General MH Unit, Stockport's Rivington Unit, Birch Hill Hospital Rochdale.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 ch.7 · NHS Act 2006 · Health and Care Act 2022 · Mental Health Act 1983 (s.136) · IFRS 16 Leases · HMRC AMAP",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£2.66M"},
            {"label": "5-year trend", "value": "2020-21 c. £1.9M → 2021-22 c. £2.0M → 2022-23 c. £2.4M (post-Edenfield reconfig start) → 2023-24 c. £2.5M → 2024-25 £2.66M"},
            {"label": "Catchment geography", "value": "Bury + Oldham + Rochdale + Stockport + Tameside + Glossop — five GM boroughs"},
            {"label": "Inpatient sites driving secure-transfer cost", "value": "Meadowbrook Salford (jointly with GMMH), Tameside MH Unit, Rivington Unit Stockport, Birch Hill Hospital Rochdale"},
            {"label": "Edenfield post-Panorama context", "value": "GMMH's Edenfield Centre forensic ward exposed by BBC Panorama Sep 2022; GM-wide patient-flow reconfiguration 2022-24 added inter-trust transfer mileage to Pennine Care"},
            {"label": "Lease-car fleet", "value": "Salary-sacrifice fleet for community-team clinicians"},
            {"label": "s.136 conveyance interaction", "value": "Joint pathway with NWAS and Greater Manchester Police; RCRP rolled out 2023-24"},
            {"label": "Delivery body", "value": "Trust transport team + NSL framework for non-emergency"},
            {"label": "Policy owner", "value": "DHSC + NHSE Mental Health · NHS Greater Manchester ICB"},
            {"label": "Funding trajectory", "value": "CPI + 2022-23 fuel-price spike + Edenfield reconfig + RCRP transfer"},
            {"label": "Evaluation evidence", "value": "CQC 'Requires Improvement' overall 2023; NHSE GM patient-flow review post-Edenfield; HMICFRS RCRP review"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2017 split before community-services reorganisation · Successor: GM-wide MH inpatient recommissioning + GM ICS unified non-emergency transport"}
        ],
        "notes": "Pennine Care's £2.66M transport line carries a clear structural step-change in 2022-23 driven by the BBC Panorama exposure of the Edenfield Centre forensic ward at Greater Manchester Mental Health (Sep 2022), which forced ward closures and GM-wide patient flow reconfiguration. Pennine Care absorbed inter-trust transfer mileage as patients were redistributed across the GM ICS footprint. The 2023-24 RCRP rollout across Greater Manchester Police compounded the pressure, and the AMAP-rate freeze since 2011 keeps a structural cost gap. CQC's 'Requires Improvement' rating in 2023 sharpened scrutiny of inter-site safety on transfers.",
        "sources": [
            {"publisher": "Pennine Care NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.penninecare.nhs.uk/about-us/publications"},
            {"publisher": "BBC Panorama", "title": "Investigation of Edenfield Centre forensic ward (Sep 2022)", "url": "https://www.bbc.co.uk/news/uk-england-manchester-63064377"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Pennine Care NHS FT provider profile (RT2)", "url": "https://www.cqc.org.uk/provider/RT2"},
            {"publisher": "HMICFRS", "title": "Right Care, Right Person — police mental-health response review", "url": "https://hmicfrs.justiceinspectorates.gov.uk/"}
        ],
        "related": ["Pennine Care NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Department of Health and Social Care", "Greater Manchester Mental Health NHS Foundation Trust", "Establishment costs — Pennine Care NHS Foundation Trust"]
    },
    "PFI / LIFT charges — Cambridgeshire and Peterborough NHS Foundation Trust": {
        "aliases": [{"name": "PFI / LIFT charges", "parent": "Cambridgeshire and Peterborough NHS Foundation Trust"}],
        "description": "CPFT delivers MH and community services across Cambridgeshire and Peterborough, with adult acute MH inpatients at the Cavell Centre Peterborough (a flagship 2012 PFI-built facility, Project Co Peterborough City Hospital and Cavell consortium aligned with the wider Peterborough hospital scheme), plus older-adult and CAMHS inpatients elsewhere. The £2.64M 2024-25 PFI / LIFT line is the unitary charge service component for the Cavell Centre — covering hard-FM, life-cycle, soft-FM and finance recovery components under the project agreement.",
        "beneficiaries": "Around 50,000 service users across Cambridgeshire (c. 680,000) and Peterborough (c. 220,000); ~4,000 staff; the Cavell Centre houses adult acute MH inpatients (c. 90 beds), PICU, dementia inpatient and S136 suite serving the Peterborough/Fenland catchment.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 ch.7 (PFI accounting) · NHS Act 2006 · Health and Care Act 2022 · IFRIC 12 Service Concession Arrangements · Project agreement (Peterborough City Hospital / Cavell PFI 2012)",
        "key_stats": [
            {"label": "PFI / LIFT charges 2024-25", "value": "£2.64M unitary charge service component"},
            {"label": "5-year trend", "value": "2020-21 c. £2.4M → 2021-22 c. £2.5M → 2022-23 c. £2.6M (RPI uplift) → 2023-24 c. £2.6M → 2024-25 £2.64M (RPI-linked)"},
            {"label": "Cavell Centre PFI build", "value": "Opened 2012 as part of the Peterborough City Hospital PFI scheme (Progress Health, Brookfield consortium)"},
            {"label": "Concession term", "value": "Unitary charge runs to c. 2042 (30-year concession from 2012 service commencement)"},
            {"label": "Inpatient bed base under PFI", "value": "c. 90 adult acute MH beds + PICU + dementia + S136 suite"},
            {"label": "Service component vs interest/depreciation", "value": "£2.64M is service-cost element; finance interest and right-of-use depreciation booked elsewhere under IFRIC 12"},
            {"label": "Delivery body", "value": "Project Co Progress Health + CPFT Estates monitoring"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + NHS Cambridgeshire & Peterborough ICB"},
            {"label": "Funding trajectory", "value": "RPI-indexed annual uplift; structural step-change at concession end c. 2042"},
            {"label": "Evaluation evidence", "value": "CQC 'Good' 2024; NAO PFI hand-back report 2023; trust ARA disclosure on Cavell Centre operational performance"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2012 Edith Cavell Hospital legacy MH wards · Successor: Cavell Centre asset hand-back planning c. 2042"}
        ],
        "notes": "CPFT's £2.64M PFI / LIFT line is the unitary-charge service component of the Cavell Centre Peterborough — a 2012 PFI build delivered under Progress Health (Brookfield consortium) as the MH-services element of the wider Peterborough City Hospital scheme. The concession runs to approximately 2042, with RPI-indexed annual uplifts driving the modest CPI-plus growth in this line. Asset hand-back planning is now starting c. 17 years out, given NAO's national 2023 PFI hand-back report flagging condition-survey, life-cycle dispute and operational performance risks across the NHS PFI estate. CPFT's separation of service-cost component from finance interest follows IFRIC 12 disclosure under DHSC GAM.",
        "sources": [
            {"publisher": "Cambridgeshire and Peterborough NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.cpft.nhs.uk/about-us/publications"},
            {"publisher": "National Audit Office", "title": "Managing PFI assets and contracts as they expire (HC 2023)", "url": "https://www.nao.org.uk/reports/managing-pfi-assets/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "CPFT provider profile (RT1)", "url": "https://www.cqc.org.uk/provider/RT1"},
            {"publisher": "HM Treasury", "title": "PFI signed projects database", "url": "https://www.gov.uk/government/publications/private-finance-initiative-and-private-finance-2-projects-2018-summary-data"}
        ],
        "related": ["Cambridgeshire and Peterborough NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Department of Health and Social Care", "Transport (business + patient) — Cambridgeshire and Peterborough NHS Foundation Trust", "PFI / LIFT charges — Cornwall Partnership NHS Foundation Trust"]
    },
    "Amortisation — Oxford Health NHS Foundation Trust": {
        "aliases": [{"name": "Amortisation", "parent": "Oxford Health NHS Foundation Trust"}],
        "description": "Oxford Health's £2.63M 2024-25 amortisation line is dominated by the Frontline Digitisation EPR rollout — the trust's deployment of an integrated MH/community electronic patient record (Cerner Millennium / RioMed lineage with bespoke MH workflow modules) plus capitalised software and digitised research-platform investment leveraging the Oxford BRC partnership with Oxford University. Amortisation under IAS 38 spreads software, configuration and capitalised implementation cost over 5-7 year useful economic life, replacing one-off cash outlays with smoothed P&L charge.",
        "beneficiaries": "Around 7,000 staff using the EPR estate across Oxfordshire, Buckinghamshire, BSW; c. 200,000 patient contacts annually flow through the digitised record; researchers in the Oxford Health Biomedical Research Centre access pseudonymised data via capitalised research platforms.",
        "legal_basis": "IAS 38 Intangible Assets · DHSC Group Accounting Manual 2024-25 ch.5 · NHS Act 2006 · Health and Care Act 2022 · Frontline Digitisation programme contractual framework",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£2.63M"},
            {"label": "5-year trend", "value": "2020-21 c. £1.4M → 2021-22 c. £1.7M → 2022-23 c. £2.0M (FD ramp) → 2023-24 c. £2.4M → 2024-25 £2.63M (sustained upward as more capitalised software comes online)"},
            {"label": "Frontline Digitisation context", "value": "NHSE programme target: every NHS trust on EPR or in deployment by Mar 2026; MH trusts in scope from 2022 wave"},
            {"label": "EPR vendor / lineage", "value": "Oxford Health uses Cerner Millennium-based stack for community + MH workflow + bespoke MH modules"},
            {"label": "Useful economic life", "value": "5-7 years for capitalised software + configuration; longer for licence-perpetual elements"},
            {"label": "Oxford BRC research-platform driver", "value": "Capitalised digital research platforms via Oxford Health BRC partnership with Oxford University add to intangible asset base"},
            {"label": "Delivery body", "value": "Trust Digital + supplier (Cerner / Oracle Health) under NHSE FD framework"},
            {"label": "Policy owner", "value": "DHSC + NHSE Transformation Directorate · NHS BOB ICB + NHS BSW ICB commissioner sign-off"},
            {"label": "Funding trajectory", "value": "Continued upward as capital investment in EPR + digital research yields amortisation tail through late 2020s"},
            {"label": "Evaluation evidence", "value": "NHSE FD programme assurance reports; NAO digital transformation reviews; CQC 'Good' 2024 with positive digital-maturity reference"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2018 paper / RiO-only legacy · Successor: ongoing FD top-ups + AI / ambient-scribe pilots through late 2020s"}
        ],
        "notes": "Oxford Health's amortisation trajectory tracks the national Frontline Digitisation rollout which targets full EPR coverage of NHS trusts by March 2026 — capitalised software, configuration and implementation costs amortise over 5-7 years, generating a sustained upward charge through the late 2020s. Oxford Health's research density (Oxford Health Biomedical Research Centre with Oxford University) adds capitalised digital research platforms beyond the core EPR. The shift from one-off cash outlays into smoothed P&L charge is the structural reason this line has moved from c. £1.4M to £2.63M over five years even though headline FD spend has plateaued.",
        "sources": [
            {"publisher": "Oxford Health NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.oxfordhealth.nhs.uk/about-us/publications/"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://transform.england.nhs.uk/digitise-connect-transform/frontline-digitisation/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Oxford Health Biomedical Research Centre", "title": "BRC research infrastructure and digital platforms", "url": "https://oxfordhealthbrc.nihr.ac.uk/"},
            {"publisher": "National Audit Office", "title": "Digital transformation in the NHS (HC 2024)", "url": "https://www.nao.org.uk/reports/digital-transformation-in-the-nhs/"}
        ],
        "related": ["Oxford Health NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Department of Health and Social Care", "Lease expenditure — Oxford Health NHS Foundation Trust", "Amortisation — Mersey Care NHS Foundation Trust"]
    },
    "Establishment costs — Avon and Wiltshire Mental Health Partnership NHS Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "Avon and Wiltshire Mental Health Partnership NHS Trust"}],
        "description": "AWP delivers MH services across Bristol, North Somerset, South Gloucestershire, Bath and North East Somerset, Swindon and Wiltshire — a five-LA, multi-ICB footprint. The £2.62M 2024-25 establishment line covers premises-related running costs (telecoms, postage, food provisions, water, refuse) across acute MH inpatient sites at Callington Road Bristol, Southmead Hospital MH Unit, Fountain Way Salisbury, Hillview Lodge Bath plus c. 80 community-team bases. Geographically dispersed footprint and the AWP MH redevelopment programme drive structural cost.",
        "beneficiaries": "Around 60,000 service users across Bristol/North Somerset/South Glos (c. 1.0M), B&NES (c. 195,000), Swindon (c. 220,000), Wiltshire (c. 510,000); ~3,800 staff; inpatient base c. 250 beds across Callington Road, Southmead MH Unit, Fountain Way, Hillview Lodge, plus PICU and forensic.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 ch.5 · NHS Act 2006 · Health and Care Act 2022 · Mental Health Act 1983 · IAS/IFRS",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£2.62M"},
            {"label": "5-year trend", "value": "2020-21 c. £1.8M → 2021-22 c. £2.0M → 2022-23 c. £2.3M → 2023-24 c. £2.5M → 2024-25 £2.62M"},
            {"label": "Inpatient bed base", "value": "c. 250 beds — Callington Road Bristol, Southmead MH Unit, Fountain Way Salisbury, Hillview Lodge Bath, Forensic Fromeside"},
            {"label": "Site footprint", "value": "c. 80 community + inpatient sites across 5 LAs spanning 3 ICBs (BNSSG, BSW)"},
            {"label": "Service-mix driver", "value": "Adult acute, older-adult, forensic (Fromeside medium secure), CAMHS Tier-4 plus city + rural community footprint"},
            {"label": "Delivery body", "value": "AWP Estates and Facilities + soft-FM contracts for catering / cleaning"},
            {"label": "Policy owner", "value": "DHSC + NHSE Mental Health · NHS BNSSG ICB + NHS BSW ICB commissioners"},
            {"label": "Funding trajectory", "value": "CPI + AWP MH redevelopment context (Callington Road remediation post-CQC enforcement)"},
            {"label": "Evaluation evidence", "value": "CQC enforcement actions on inpatient services 2022-23; CQC 'Requires Improvement' 2023; NHSE quality oversight under recovery support"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2002 merger of Avon, Wiltshire and Swindon MH services · Successor: AWP MH redevelopment programme — Callington Road / Southmead replacement under BNSSG ICS capital case"}
        ],
        "notes": "AWP's £2.62M establishment line is shaped by an unusually dispersed footprint — five local-authority areas spanning three ICBs (BNSSG, BSW) — and by the operational pressure following CQC enforcement actions on inpatient services through 2022-23 which drove environmental remediation including ward fabric replacement, anti-ligature furniture, observation infrastructure that lands partly in establishment / supplies. The AWP MH redevelopment programme (Callington Road and Southmead unit replacement) is being progressed via BNSSG ICS capital case rather than NHP. Food inflation 2022-24 across c. 250 inpatient beds adds CPI-plus pressure.",
        "sources": [
            {"publisher": "Avon and Wiltshire Mental Health Partnership NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.awp.nhs.uk/about-us/publications-policies"},
            {"publisher": "NHS England", "title": "Mental health provider finance benchmarking 2024-25", "url": "https://www.england.nhs.uk/financial-accounts/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "AWP provider profile (RVN)", "url": "https://www.cqc.org.uk/provider/RVN"},
            {"publisher": "NHS BNSSG ICB", "title": "Mental health redevelopment estate strategy", "url": "https://bnssg.icb.nhs.uk/"}
        ],
        "related": ["Avon and Wiltshire Mental Health Partnership NHS Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Department of Health and Social Care", "PFI / LIFT charges — Avon and Wiltshire Mental Health Partnership NHS Trust", "Business rates — Avon and Wiltshire Mental Health Partnership NHS Trust"]
    },
    "Impairments net of reversals — Leeds and York Partnership NHS Foundation Trust": {
        "aliases": [{"name": "Impairments net of reversals", "parent": "Leeds and York Partnership NHS Foundation Trust"}],
        "description": "LYPFT's £2.54M 2024-25 impairment line reflects MEA-DRC revaluation across the Becklin Centre (St James's University Hospital site Leeds), Mount Hospital, Newsam Centre Seacroft and the Yorkshire Centre for Eating Disorders, applied under the 5-yearly cycle. The trust's national-specialist mix (eating disorders, gender, deafness, PD) means valuation must reflect specialist-fit-out depreciation alongside generic MH ward standards. Estates & Facilities is delivery body; external valuer panel applied the cycle reset.",
        "beneficiaries": "Inpatient base c. 250 beds + national specialist commissioning catchment; gross MH-estate floor area c. 35,000 m² across Becklin, Mount, Newsam and Yorkshire Centre; ~3,300 staff working on the revalued estate.",
        "legal_basis": "IAS 36 Impairment of Assets · DHSC Group Accounting Manual 2024-25 ch.4 · NHS Act 2006 · Health and Care Act 2022 · IFRS 13 Fair Value Measurement",
        "key_stats": [
            {"label": "Impairments net of reversals 2024-25", "value": "£2.54M"},
            {"label": "5-year trend", "value": "2020-21 c. £0.7M → 2021-22 c. £1.0M → 2022-23 c. £1.6M → 2023-24 c. £2.1M → 2024-25 £2.54M"},
            {"label": "Estate gross floor area revalued", "value": "c. 35,000 m² across Becklin + Mount + Newsam + Yorkshire Centre"},
            {"label": "MEA-DRC vs market value driver", "value": "Specialist-fit-out depreciation on ED-feeding rooms, deaf-CAMHS accessibility, gender clinic; standard MH ward modernisation cost-to-replicate driver elsewhere"},
            {"label": "RAAC scope", "value": "Not on HSSIB confirmed-RAAC list"},
            {"label": "NHP cohort + Reset Jan 2025 status", "value": "Not in NHP cohort; capital pursued through West Yorkshire ICS bids and NHSE specialised commissioning"},
            {"label": "Bootham Park York legacy", "value": "Bootham Park Hospital York closed Sep 2015 after CQC enforcement; legacy estate impairments tail closed pre-2020"},
            {"label": "Valuation cycle phase", "value": "5-yearly full revaluation 2024-25"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + external valuer DHSC central panel"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + West Yorkshire ICB + NHSE Specialised Commissioning"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2015 Bootham Park York legacy estate · Successor: Becklin / Newsam refurb cycle through West Yorkshire ICS capital"}
        ],
        "notes": "LYPFT's £2.54M is structurally driven by specialist-fit-out depreciation: the Yorkshire Centre for Eating Disorders requires bespoke refeeding rooms, dining infrastructure, observation cubicles; the National Deaf CAMHS service requires accessibility features; the Gender Identity Service requires specialist clinical-fit-out — all of which depreciate against modernisation cost-to-replicate. The Bootham Park York legacy (closed Sep 2015 after CQC enforcement) is fully run off so does not feature in current impairments. Without an NHP slot, capital renewal must come through West Yorkshire ICS and NHSE specialised commissioning bids, which keeps impairments sustained as economic life is extended on existing fabric.",
        "sources": [
            {"publisher": "Leeds and York Partnership NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.leedsandyorkpft.nhs.uk/about-us/publications/"},
            {"publisher": "NHS England", "title": "Mental health provider finance benchmarking 2024-25", "url": "https://www.england.nhs.uk/financial-accounts/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Leeds and York Partnership NHS FT provider profile (RGD)", "url": "https://www.cqc.org.uk/provider/RGD"},
            {"publisher": "National Audit Office", "title": "NHS Estate condition report 2024", "url": "https://www.nao.org.uk/reports/nhs-estate/"}
        ],
        "related": ["Leeds and York Partnership NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Department of Health and Social Care", "Establishment costs — Leeds and York Partnership NHS Foundation Trust", "General supplies & services — Leeds and York Partnership NHS Foundation Trust"]
    },
    "Amortisation — Mersey Care NHS Foundation Trust": {
        "aliases": [{"name": "Amortisation", "parent": "Mersey Care NHS Foundation Trust"}],
        "description": "Mersey Care is the largest provider of MH and addictions services on Merseyside and runs the high-secure Ashworth Hospital (one of three high-secure MH units in England alongside Broadmoor and Rampton). The £2.49M 2024-25 amortisation line reflects Frontline Digitisation EPR rollout (RiO platform with bespoke MH workflows) plus capitalised software for high-secure-specific systems (offender risk management, restricted-mail digitisation) and the 2018 transfer of Calderstones LD services. Amortisation under IAS 38 spreads software cost over 5-7 year UEL.",
        "beneficiaries": "Around 100,000 patient contacts annually across Liverpool (c. 500,000), Sefton (c. 280,000), South Sefton, Knowsley, St Helens; ~12,000 staff use the EPR; Ashworth Hospital high-secure inpatients (c. 200 beds) require additional restricted-environment digital systems.",
        "legal_basis": "IAS 38 Intangible Assets · DHSC Group Accounting Manual 2024-25 ch.5 · NHS Act 2006 · Health and Care Act 2022 · Frontline Digitisation programme contractual framework",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£2.49M"},
            {"label": "5-year trend", "value": "2020-21 c. £1.2M → 2021-22 c. £1.5M → 2022-23 c. £1.8M (FD ramp + Calderstones tail) → 2023-24 c. £2.2M → 2024-25 £2.49M"},
            {"label": "Frontline Digitisation context", "value": "NHSE programme target full EPR coverage by Mar 2026; Mersey Care in MH wave from 2022"},
            {"label": "EPR vendor / lineage", "value": "Mersey Care uses RiO MH-specific EPR with bespoke workflow modules"},
            {"label": "High-secure-specific systems", "value": "Capitalised offender risk-management, restricted-mail digitisation, intelligence-management software for Ashworth Hospital"},
            {"label": "Calderstones transfer 2016", "value": "Trust absorbed Calderstones Partnership LD services in Nov 2016; capitalised system migration tail amortising through late 2020s"},
            {"label": "Useful economic life", "value": "5-7 years for capitalised software + configuration"},
            {"label": "Delivery body", "value": "Mersey Care Digital + supplier (Civica RiO) under NHSE FD framework"},
            {"label": "Policy owner", "value": "DHSC + NHSE Transformation Directorate + NHSE Specialised Commissioning (high-secure) · NHS Cheshire and Merseyside ICB"},
            {"label": "Funding trajectory", "value": "Sustained upward as capital investment in EPR + high-secure platforms yields amortisation tail through late 2020s"},
            {"label": "Evaluation evidence", "value": "NHSE FD programme assurance; CQC 'Good' overall 2024; NAO digital transformation reviews"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2016 Calderstones legacy systems · Successor: ongoing FD top-ups + AI / ambient-scribe pilots through late 2020s"}
        ],
        "notes": "Mersey Care's amortisation profile combines the standard Frontline Digitisation upward trajectory with two trust-specific capitalised software pools: high-secure-environment systems for Ashworth Hospital (offender risk management, restricted-mail digitisation, intelligence management) which are not part of the generic MH EPR scope and require bespoke development; and the Calderstones Partnership LD-services migration tail from the November 2016 absorption, which continues to amortise capitalised system migration costs. The combined effect explains why the line has moved from c. £1.2M to £2.49M over five years.",
        "sources": [
            {"publisher": "Mersey Care NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.merseycare.nhs.uk/about-us/our-publications"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://transform.england.nhs.uk/digitise-connect-transform/frontline-digitisation/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Mersey Care NHS FT provider profile (RW4)", "url": "https://www.cqc.org.uk/provider/RW4"},
            {"publisher": "National Audit Office", "title": "Digital transformation in the NHS (HC 2024)", "url": "https://www.nao.org.uk/reports/digital-transformation-in-the-nhs/"}
        ],
        "related": ["Mersey Care NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Department of Health and Social Care", "Lease expenditure — Mersey Care NHS Foundation Trust", "Amortisation — Oxford Health NHS Foundation Trust"]
    },
    "PFI / LIFT charges — Avon and Wiltshire Mental Health Partnership NHS Trust": {
        "aliases": [{"name": "PFI / LIFT charges", "parent": "Avon and Wiltshire Mental Health Partnership NHS Trust"}],
        "description": "AWP's £2.48M 2024-25 PFI / LIFT charges line is dominated by LIFT (Local Improvement Finance Trust) buildings — the New-Labour-era community-based primary-care + community-MH facility model — across Bristol, B&NES and Wiltshire. LIFT facilities deliver community-MH bases with shared occupancy alongside GP and primary-care services, with AWP paying a service-component unitary charge under the NHS LIFT national framework. The 2018-2025 LIFT contract review cycle and RPI uplifts are the structural cost driver.",
        "beneficiaries": "Around 60,000 service users access community-MH services delivered partly through LIFT facilities across Bristol, B&NES and Wiltshire; community CMHTs and IAPT teams co-locate in LIFT buildings with primary care; ~3,800 staff trust-wide.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 ch.7 · NHS Act 2006 · Health and Care Act 2022 · IFRIC 12 Service Concession Arrangements · NHS LIFT framework agreement (2001 onwards) · Community Health Partnerships master agreements",
        "key_stats": [
            {"label": "PFI / LIFT charges 2024-25", "value": "£2.48M (predominantly LIFT facility service-component)"},
            {"label": "5-year trend", "value": "2020-21 c. £2.2M → 2021-22 c. £2.3M → 2022-23 c. £2.4M (RPI uplift) → 2023-24 c. £2.4M → 2024-25 £2.48M"},
            {"label": "LIFT framework context", "value": "NHS LIFT launched 2001 — Community Health Partnerships acts as PSP partner; 49 LIFTCo SPVs nationally; AWP occupies LIFT space across BNSSG, BSW LIFTs"},
            {"label": "Concession term", "value": "LIFT facilities operate on 25-30 year concessions; mid-cycle for most AWP-occupied sites c. 2030-2035 expiries"},
            {"label": "LIFTCo counterparties", "value": "BNSSG LIFTCo + Wiltshire LIFTCo (Community Health Partnerships partner) plus Aspire / 3ED operating SPVs"},
            {"label": "Service component vs interest/depreciation", "value": "£2.48M is service-cost element of unitary charge; right-of-use and finance-interest elements booked separately under IFRIC 12"},
            {"label": "Delivery body", "value": "LIFTCo SPVs + Community Health Partnerships + AWP Estates monitoring"},
            {"label": "Policy owner", "value": "DHSC + Community Health Partnerships + NHS BNSSG ICB + NHS BSW ICB"},
            {"label": "Funding trajectory", "value": "RPI-indexed annual uplift; concession-end planning starts 2027-28 for earliest LIFT expiries"},
            {"label": "Evaluation evidence", "value": "NAO PFI hand-back report 2023 (LIFT included); IfG 2024 analysis of community-estate concession model"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2001 NHS-owned community clinic estate · Successor: LIFT concession-end re-letting / hand-back from late 2020s"}
        ],
        "notes": "AWP's PFI / LIFT line is unusual among MH trusts in being dominated by LIFT (community-estate) rather than acute PFI — most MH trusts are LIFT-light because their main inpatient sites pre-date 2001 LIFT or were funded conventionally. AWP's dispersed five-LA footprint means a higher proportion of community-MH bases sit in LIFT facilities co-located with primary care. The earliest LIFTs are now approaching 25-30 year mid-life points; NAO's 2023 PFI hand-back report and IfG's 2024 analysis flag concession-end risks (condition surveys, life-cycle disputes, re-letting friction). RPI uplifts are the visible annual driver but concession-end is the medium-term strategic question.",
        "sources": [
            {"publisher": "Avon and Wiltshire Mental Health Partnership NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.awp.nhs.uk/about-us/publications-policies"},
            {"publisher": "Community Health Partnerships", "title": "NHS LIFT framework and LIFTCo portfolio", "url": "https://communityhealthpartnerships.co.uk/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "National Audit Office", "title": "Managing PFI assets and contracts as they expire (HC 2023)", "url": "https://www.nao.org.uk/reports/managing-pfi-assets/"},
            {"publisher": "Institute for Government", "title": "PFI and LIFT contract expiry — preparing for hand-back", "url": "https://www.instituteforgovernment.org.uk/"}
        ],
        "related": ["Avon and Wiltshire Mental Health Partnership NHS Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Community Health Partnerships Ltd", "Establishment costs — Avon and Wiltshire Mental Health Partnership NHS Trust", "PFI / LIFT charges — Cornwall Partnership NHS Foundation Trust"]
    },
    "Business rates — Surrey and Borders Partnership NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "Surrey and Borders Partnership NHS Foundation Trust"}],
        "description": "SaBP's £2.38M 2024-25 business rates line is the non-domestic rate liability on c. 90 occupied hereditaments across Surrey, north-east Hampshire and parts of west Sussex — calculated on VOA rateable values multiplied by the 2024-25 standard multiplier of 54.6p (small business 49.9p). Rates are levied on the trust under Local Government Finance Act 1988 because NHS Foundation Trusts are 'Other' rated occupiers (not Crown bodies, not charities). Surrey's high-value commercial-property zone underpins above-average rateable values per square metre.",
        "beneficiaries": "Around 35,000 service users across c. 90 occupied sites — Abraham Cowley Unit Chertsey (St Peter's site), Farnham Road Hospital Guildford, Halliwick Centre, plus c. 80 community-team and admin bases in Surrey's high-rateable-value commercial zones.",
        "legal_basis": "Local Government Finance Act 1988 (Schedule 6 valuation) · Non-Domestic Rating (Multipliers and Private Finance) Act 2024 · NHS Act 2006 · Health and Care Act 2022 · DHSC Group Accounting Manual 2024-25",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£2.38M"},
            {"label": "5-year trend", "value": "2020-21 c. £1.9M → 2021-22 c. £2.0M → 2022-23 c. £2.1M (multiplier freeze, partial reval relief) → 2023-24 c. £2.2M → 2024-25 £2.38M (post-2023 reval list + 2024-25 multiplier uplift)"},
            {"label": "Hereditament count", "value": "c. 90 separately rated NHS-occupied properties across Surrey + NE Hampshire"},
            {"label": "VOA rateable value drivers", "value": "Surrey commercial-property zone among highest rateable-value rates per m² outside London — pushes per-site cost above peer trusts"},
            {"label": "Multiplier 2024-25", "value": "Standard 54.6p / Small 49.9p (frozen 2023-24, partly uplifted 2024-25 under Non-Domestic Rating Act 2024)"},
            {"label": "NHSPS interaction", "value": "Multiple Surrey community sites occupied via NHSPS lease — NHSPS holds rates liability on common parts but trust pays direct rates on own-occupied space"},
            {"label": "Charitable exemption", "value": "Not applied — SaBP not a registered charity (NHS FT status only); 80% mandatory relief unavailable"},
            {"label": "Delivery body", "value": "Trust Estates + VOA + Surrey-area billing authorities (11 districts)"},
            {"label": "Policy owner", "value": "MHCLG (rates policy) + DHSC (NHS impact) · NHS Surrey Heartlands ICB"},
            {"label": "Funding trajectory", "value": "Annual multiplier uplift + 2026 next reval list (VOA antecedent valuation date 1 Apr 2024)"},
            {"label": "Evaluation evidence", "value": "VOA 2023 reval list outcomes; NAO 2024 review of business rates; trust ARA disclosure on rates exposure"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2017 reval list (AVD 1 Apr 2015) · Successor: 2026 reval list (AVD 1 Apr 2024) under Non-Domestic Rating Act 2024 reform"}
        ],
        "notes": "SaBP's £2.38M business rates line sits above peer MH trusts of similar bed base because Surrey's commercial-property values are among the highest outside London, feeding directly into VOA rateable values per square metre. The 2023 reval list (AVD 1 Apr 2021) reset rateable values upward for Surrey commercial zones. NHS Foundation Trusts cannot claim 80% mandatory charitable relief — only registered charities qualify — so the full liability falls on the trust. The next reval list takes effect April 2026 (AVD 1 Apr 2024) under the Non-Domestic Rating (Multipliers and Private Finance) Act 2024 framework, with Surrey property values expected to remain elevated. NHSPS-held common-part rates create a recurring negotiation pressure on the lease line.",
        "sources": [
            {"publisher": "Surrey and Borders Partnership NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.sabp.nhs.uk/about-us/publications"},
            {"publisher": "Valuation Office Agency", "title": "Find a business rates valuation (search by NHS site)", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Ministry of Housing, Communities and Local Government", "title": "Non-Domestic Rating Act 2024 — multiplier reform", "url": "https://www.gov.uk/government/collections/business-rates"},
            {"publisher": "National Audit Office", "title": "Business rates — administration and reform (HC 2024)", "url": "https://www.nao.org.uk/"}
        ],
        "related": ["Surrey and Borders Partnership NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Valuation Office Agency", "Establishment costs — Surrey and Borders Partnership NHS Foundation Trust", "Transport (business + patient) — Surrey and Borders Partnership NHS Foundation Trust"]
    },
}
