# -*- coding: utf-8 -*-
# Phase 2 Acute slice 2 — chunk 10 (17 NHS Acute Trust orphan sub-lines)
# Hand-curated trust-specific PROGRAMME-archetype enrichment entries.
# Structural contract per docs/archetype_briefs.md.

NEW = {
    "General supplies & services — Whittington Health NHS Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "Whittington Health NHS Trust"}],
        "description": "Whittington Health's £8.15M general supplies & services line covers non-clinical consumables, linen, catering provisions, hotel-services materials, office supplies and minor expensed equipment across the Whittington Hospital acute site (Highgate Hill, Archway) plus an integrated community-services footprint across Islington and Haringey boroughs. The trust is one of the few full-integrated acute + community providers in London, broadening the consumables baseline beyond the acute DGH benchmark for North Central London ICS.",
        "beneficiaries": "c. 4,500 WTE staff serving a c. 500,000 Islington + Haringey catchment with high deprivation; c. 95,000 ED attendances/yr at the single Whittington ED; c. 35,000 admissions/yr; c. 4,000 deliveries/yr at the maternity unit; community footprint covers district nursing + health-visiting + school-nursing + community-paediatric services.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 2 Inventories · Procurement Act 2023 · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "General supplies & services 2024-25", "value": "£8.15M"},
            {"label": "Trust scale", "value": "Single acute site (Whittington Hospital, Archway) + integrated Islington + Haringey community services; c. 4,500 WTE"},
            {"label": "Integrated acute + community", "value": "Acute + community-services integration broadens non-clinical-consumables base via district nursing, health-visiting, school-nursing kits + community-clinic hotel services"},
            {"label": "ED throughput", "value": "c. 95,000 ED attendances/yr at single Whittington ED"},
            {"label": "Catchment deprivation", "value": "Islington + Haringey — high IMD deprivation; drives emergency-care + maternity volume on consumables baseline"},
            {"label": "Procurement route", "value": "NHS Supply Chain national framework + North Central London ICS collaborative + trust-direct spot-buy for community sites"},
            {"label": "Industrial action 2023-24", "value": "44 days junior-doctor + 10 days consultant strike days drove cancellation re-stocking churn + agency-backfill consumable use"},
            {"label": "April 2025 NIC + CPI", "value": "Apr 2025 employer-NIC step-up + sustained non-clinical CPI feed forward unit-cost via supplier pass-through"},
            {"label": "Funding trajectory", "value": "2021-22 c. £6.5M → 2023-24 £7.6M → 2024-25 £8.15M — sustained CPI + community activity + acute backlog recovery"},
            {"label": "Delivery body", "value": "Trust Procurement + Supply Chain + Hotel Services teams + NHS Supply Chain (DHSC ALB) + NCL ICS procurement collaborative"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + North Central London ICB"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2011 separate Whittington acute + Islington/Haringey PCT-provider community baselines · Successor: NCL ICS group-procurement scaling"}
        ],
        "notes": "Whittington Health is one of London's fully-integrated acute + community provider trusts, formed via the 2011 transfer of community services from Islington and Haringey PCTs into the existing acute trust — broadening the non-clinical-consumables baseline through district nursing kit, health-visiting bags, school-nursing supplies and community-clinic hotel services. The high-deprivation Islington and Haringey catchment sustains ED and maternity volumes that drive consumables churn at the single acute site. Industrial action 2023-24 added cancellation re-stocking and agency-backfill use. NHS Supply Chain remains dominant; NCL ICS collaborative procurement scaling and Apr 2025 NIC step-up shape the unit-cost path.",
        "sources": [
            {"publisher": "Whittington Health NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.whittington.nhs.uk/default.asp?c=10665"},
            {"publisher": "NHS Supply Chain", "title": "Annual Report 2023-24", "url": "https://www.supplychain.nhs.uk/about-us/our-publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Whittington Health provider profile (RKE)", "url": "https://www.cqc.org.uk/provider/RKE"},
            {"publisher": "NHS England", "title": "North Central London ICS — provider collaborative", "url": "https://www.england.nhs.uk/london/our-work/north-central-london/"}
        ],
        "related": ["Whittington Health NHS Trust", "Clinical Supplies & Drugs", "NHS Acute Trusts", "NHS Supply Chain", "General supplies & services — North West Anglia NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Establishment costs — University Hospital Southampton NHS Foundation Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "University Hospital Southampton NHS Foundation Trust"}],
        "description": "UHS's £8.07M establishment line covers office supplies, postage, telecoms, printing, training, courses, recruitment-advertising, professional fees and minor IT/software subscriptions across the Southampton General + Princess Anne + Royal South Hants + New Forest Birth Centre + community-clinic footprint. UHS is the major tertiary teaching trust for Hampshire & IoW ICS — running the Wessex region's specialist cardiothoracic, neuroscience, paediatrics, transplant and major-trauma services — driving sustained corporate-services overhead vs DGH peers.",
        "beneficiaries": "c. 13,000 WTE staff serving c. 1.9M Wessex residents through tertiary referrals plus a c. 650,000 local Southampton catchment; c. 175,000 ED attendances/yr (Southampton General ED); c. 175,000 admissions/yr; specialist-services hub for cardiac, neurosciences, paediatric oncology, transplant, major trauma.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25 · Procurement Act 2023",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£8.07M"},
            {"label": "Trust scale", "value": "c. 13,000 WTE; major teaching/tertiary trust for Wessex"},
            {"label": "Site mix", "value": "Southampton General Hospital + Princess Anne (maternity/women's) + Royal South Hants + New Forest Birth Centre + community clinics"},
            {"label": "Tertiary specialty hub", "value": "Cardiothoracic + neurosciences + paediatric oncology (one of the principal-treatment-centre nodes) + transplant + Major Trauma Centre — multiplies professional-fee + training + recruitment overhead"},
            {"label": "University of Southampton link", "value": "Joint academic enterprise with University of Southampton + Wessex BRC (NIHR) — research-admin + clinical-academic recruitment overhead"},
            {"label": "Composition", "value": "Telecoms + postage + printing + courses + training + recruitment-advertising + minor IT/software subs + professional fees + research-admin"},
            {"label": "Industrial action 2023-24", "value": "44 days junior-doctor + 10 days consultant strike action drove rota-restructuring + agency-recruitment + temporary-staffing-platform spend"},
            {"label": "Frontline Digitisation EPR", "value": "Trust EPR programme (CHARTS / Cerner Millennium) drives sustained training, change-mgmt + interoperability spend on establishment"},
            {"label": "April 2025 NIC step-up", "value": "Apr 2025 employer-NIC threshold drop to £5,000 + rate to 15% raises forward establishment cost on professional fees + recruitment retainers"},
            {"label": "Funding trajectory", "value": "2021-22 c. £6.5M → 2023-24 £7.5M → 2024-25 £8.07M — sustained tertiary-specialty + research-admin overhead + recruitment churn"},
            {"label": "Delivery body", "value": "Trust Finance + HR + IT + Communications corporate functions + R&D office + EPR programme office"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Hampshire and Isle of Wight ICB + NIHR (BRC funding)"}
        ],
        "notes": "UHS sustains a tertiary-specialty + teaching establishment overhead well above DGH peers — the Wessex cardiothoracic, neurosciences, transplant, paediatric-oncology and Major Trauma Centre roles multiply professional fees, recruitment retainers and clinical-academic admin layered on top of the DGH corporate-services baseline. The joint academic enterprise with the University of Southampton and the NIHR Wessex Biomedical Research Centre drives further research-admin overhead on training, courses and professional fees. Industrial action 2023-24 layered rota-restructuring and agency-recruitment costs. The Cerner Millennium / CHARTS EPR baseline drives change-mgmt and interoperability spend; Apr 2025 NIC step-up raises forward professional-fee cost.",
        "sources": [
            {"publisher": "University Hospital Southampton NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.uhs.nhs.uk/about-us/who-we-are/annual-reports/"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme + EPR rollout tracker", "url": "https://www.england.nhs.uk/digitaltechnology/connecteddigitalsystems/frontline-digitisation/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "UHS provider profile (RHM)", "url": "https://www.cqc.org.uk/provider/RHM"},
            {"publisher": "National Institute for Health and Care Research", "title": "NIHR Southampton Biomedical Research Centre", "url": "https://www.nihr.ac.uk/explore-nihr/infrastructure/biomedical-research-centres.htm"}
        ],
        "related": ["University Hospital Southampton NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Establishment costs — Royal Free London NHS Foundation Trust", "Frontline Digitisation programme", "Department of Health and Social Care"]
    },
    "Transport (business + patient) — Oxford University Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "Oxford University Hospitals NHS Foundation Trust"}],
        "description": "OUH's £8.04M transport line covers business mileage, inter-site clinical transfers and Non-Emergency Patient Transport Services across the four-site footprint (John Radcliffe + Churchill + Nuffield Orthopaedic Centre + Horton General). Tertiary-referral inter-site flows — major-trauma to John Radcliffe MTC, oncology to Churchill, orthopaedics to NOC, plus the Horton (Banbury) DGH spoke — drive substantial PTS demand, with South Central Ambulance Service and accredited NEPTS contractors as primary carriers across the BOB ICS catchment.",
        "beneficiaries": "c. 13,500 WTE staff serving c. 1.6M BOB-ICS residents plus tertiary referrals across the wider Thames Valley; c. 175,000 ED attendances/yr (John Radcliffe + Horton EDs combined); c. 130,000 admissions/yr; John Radcliffe is the Thames Valley Major Trauma Centre and a regional cardiac, neurosciences and transplant hub.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · IFRS 16 Leases (pool fleet) · NHS Act 2006 · Mental Health Act 1983 (s.135/136 conveyance) · NHSE Patient Transport Services Eligibility Framework 2022 · HMRC AMAP · NHS AfC Section 17",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£8.04M"},
            {"label": "Trust scale", "value": "Four-site academic acute (John Radcliffe + Churchill + Nuffield Orthopaedic Centre + Horton General); c. 13,500 WTE"},
            {"label": "Major Trauma Centre", "value": "John Radcliffe = Thames Valley MTC — drives inter-site major-trauma transfer demand"},
            {"label": "Tertiary specialty mix", "value": "Churchill oncology + NOC orthopaedics + JR neurosciences/cardiac/transplant — sustained inter-hospital + inter-trust PTS"},
            {"label": "Horton spoke", "value": "Horton General Hospital (Banbury) — DGH spoke c. 23 miles north; daily inter-site clinical transfers + staff mileage"},
            {"label": "PTS provider mix", "value": "South Central Ambulance Service NHS FT (SCAS) + accredited NEPTS contractors — re-tendered via BOB ICS"},
            {"label": "Staff mileage rate", "value": "NHS Agenda for Change Section 17 / HMRC AMAP 45p first 10,000 miles + 25p thereafter"},
            {"label": "Pool fleet (IFRS 16)", "value": "Right-of-use depreciation + interest on leased pool vehicles for AHPs + community teams"},
            {"label": "Funding trajectory", "value": "2021-22 c. £6M → 2023-24 £7.5M → 2024-25 £8.04M — fuel CPI + activity recovery + tertiary-flow growth"},
            {"label": "Delivery body", "value": "Trust E&F + Travel team + SCAS NEPTS + accredited NEPTS contractors"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Buckinghamshire, Oxfordshire and Berkshire West ICB"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2007 pre-merger separate ORH + Nuffield Orthopaedic transport baselines · Successor: BOB ICS shared-transport collaborative + IFRS 16 lifecycle"}
        ],
        "notes": "OUH's transport line carries the cost of running tertiary-specialty inter-site transfer flows across the four-site Oxford academic complex plus the c. 23-mile Horton spoke at Banbury — the John Radcliffe MTC role drives major-trauma transfer demand from across the Thames Valley while Churchill oncology and NOC orthopaedic specialty flows multiply NEPTS demand on patients moving between sites for treatment phases. South Central Ambulance Service holds the dominant NEPTS contract via BOB ICS commissioning, with accredited contractors filling capacity. Industrial action 2023-24 added ad-hoc inter-site transfers and locum mileage; fuel CPI through 2022-24 fed unit-cost. The IFRS 16 right-of-use treatment of the pool fleet (AHP + community-team vehicles) sits within the line.",
        "sources": [
            {"publisher": "Oxford University Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.ouh.nhs.uk/about/publications/"},
            {"publisher": "South Central Ambulance Service NHS Foundation Trust", "title": "NEPTS service provision", "url": "https://www.scas.nhs.uk/our-services/non-emergency-patient-transport/"},
            {"publisher": "NHS England", "title": "Non-Emergency Patient Transport Services Eligibility Framework 2022", "url": "https://www.england.nhs.uk/publication/non-emergency-patient-transport-services-nepts/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Oxford University Hospitals provider profile (RTH)", "url": "https://www.cqc.org.uk/provider/RTH"}
        ],
        "related": ["Oxford University Hospitals NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "South Central Ambulance Service NHS Foundation Trust", "Transport (business + patient) — Imperial College Healthcare NHS Trust", "Department of Health and Social Care"]
    },
    "PFI / LIFT charges — North Bristol NHS Trust": {
        "aliases": [{"name": "PFI / LIFT charges", "parent": "North Bristol NHS Trust"}],
        "description": "NBT's £7.88M PFI charge reflects the residual unitary-charge pass-through component on the Brunel building PFI at Southmead Hospital (operational May 2014, signed 2010 with Hospital Company (Southmead) Ltd / Carillion-Equion consortium). The Brunel building is one of the largest PFI hospital schemes in England — c. 800 beds — with Carillion's Jan 2018 collapse triggering FM novation to Sodexo on hard-FM and continuing soft-FM transitions. The line covers debt service, lifecycle and indexed FM components after the IFRS 16 GAM ch.7 split.",
        "beneficiaries": "c. 8,500 WTE staff serving a c. 900,000 South Gloucestershire + north Bristol catchment plus tertiary referrals across the South West; c. 110,000 ED attendances/yr at Southmead ED; c. 70,000 admissions/yr; Southmead is the South West Major Trauma Centre and a regional neurosciences/renal/plastics hub.",
        "legal_basis": "IFRIC 12 Service Concession Arrangements · IFRS 16 Leases (post-2022 transition for service-concession components) · DHSC Group Accounting Manual 2024-25 ch.7 · Private Finance Initiative guidance (HM Treasury) · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "PFI / LIFT charges 2024-25 (residual line)", "value": "£7.88M"},
            {"label": "PFI vehicle", "value": "Brunel building Southmead PFI signed 2010, operational May 2014; SPV Hospital Company (Southmead) Ltd — Carillion-Equion / Innisfree consortium"},
            {"label": "Contract end date", "value": "c. 2044 (30-year operational concession)"},
            {"label": "Carillion 2018 effect", "value": "Carillion (hard-FM contractor) Jan 2018 collapse → Sodexo novation; ongoing soft-FM contract churn at Southmead"},
            {"label": "Estate covered", "value": "Brunel building, Southmead Hospital — c. 800 beds, single concentrated build replacing legacy Frenchay + Southmead estate"},
            {"label": "Unitary charge composition", "value": "Senior + subordinated debt service + lifecycle hard-FM + indexed soft-FM (cleaning, catering, portering, helpdesk)"},
            {"label": "Indexation mechanism", "value": "RPI-linked annual uplift on indexed soft-FM components per concession agreement"},
            {"label": "Headline PFI obligation", "value": "Whole-PFI annual unitary charge c. £55-65M (cited in Trust ARA + NAO PFI hand-back review); £7.88M residual line is post-IFRS 16 GAM ch.7 split component"},
            {"label": "Major Trauma Centre", "value": "Southmead = South West MTC — concentrated single-site rebuild rationale"},
            {"label": "Delivery body", "value": "Hospital Company (Southmead) SPV + Sodexo (post-Carillion FM) + trust E&F oversight"},
            {"label": "Policy owner", "value": "DHSC + HM Treasury PFI guidance + NHSE Provider Finance + Bristol, North Somerset and South Gloucestershire ICB"},
            {"label": "Predecessor / successor", "value": "Predecessor: legacy Frenchay + Southmead pre-2014 estate · Successor: 2044 hand-back + post-PFI estate ownership"}
        ],
        "notes": "NBT's PFI obligation centres on the Brunel building at Southmead — one of the largest single-site PFI hospital builds in England, opened May 2014 to consolidate the legacy Frenchay and Southmead estates onto a c. 800-bed footprint. Carillion's January 2018 collapse triggered hard-FM novation to Sodexo (NAO documented 2020), with continuing soft-FM contract management adjustments. The South West Major Trauma Centre role anchors the operational case. RPI indexation continues to lift soft-FM components; the 2044 hand-back window remains c. 20 years out. The £7.88M figure is the residual PFI/LIFT-line component after the IFRS 16 + GAM ch.7 split allocates parts of the obligation to other lines.",
        "sources": [
            {"publisher": "North Bristol NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.nbt.nhs.uk/about-us/publications-policies/annual-reports-publications"},
            {"publisher": "National Audit Office", "title": "Investigation into the rescue of Carillion's PFI hospital contracts (HC 23, 2020)", "url": "https://www.nao.org.uk/reports/investigation-into-the-rescue-of-carillions-pfi-hospital-contracts/"},
            {"publisher": "National Audit Office", "title": "Managing PFI assets and services as contracts end (HC 632, 2020)", "url": "https://www.nao.org.uk/reports/managing-pfi-assets-and-services-as-contracts-end/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 7)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "North Bristol NHS Trust provider profile (RVJ)", "url": "https://www.cqc.org.uk/provider/RVJ"}
        ],
        "related": ["North Bristol NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "PFI / LIFT charges — Sherwood Forest Hospitals NHS Foundation Trust", "PFI / LIFT charges — Worcestershire Acute Hospitals NHS Trust", "Department of Health and Social Care"]
    },
    "Establishment costs — Royal Free London NHS Foundation Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "Royal Free London NHS Foundation Trust"}],
        "description": "Royal Free London's £7.84M establishment line covers office supplies, postage, telecoms, printing, training, courses, recruitment-advertising, professional fees and minor IT/software subscriptions across the Royal Free Hospital + Barnet Hospital + Chase Farm Hospital footprint plus the trust-led group-model corporate functions. Royal Free is one of the NHS's flagship group-model trusts, with active acquisition transaction underway with North Middlesex University Hospital NHS Trust to extend the group across North Central London ICS.",
        "beneficiaries": "c. 12,000 WTE staff serving a c. 1.6M North Central London catchment plus tertiary referrals (renal transplant, HIV, hepatology, infectious diseases); c. 280,000 ED attendances/yr (Royal Free + Barnet EDs + Chase Farm UTC); c. 165,000 admissions/yr; specialist hub for renal/transplant, hepatology, HIV, high-consequence infectious diseases.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25 · Procurement Act 2023",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£7.84M"},
            {"label": "Trust scale", "value": "c. 12,000 WTE across Royal Free + Barnet + Chase Farm; c. 1.6M NCL catchment + tertiary referrals"},
            {"label": "Group model", "value": "Royal Free London Group — flagship NHS group-model trust; active acquisition transaction with North Middlesex 2023-25 under NCL ICS"},
            {"label": "Tertiary specialty mix", "value": "Royal Free Hampstead = renal/transplant + hepatology + HIV/HCID hub; Barnet + Chase Farm DGH-acute services; Chase Farm purpose-built elective hub"},
            {"label": "HCID centre", "value": "Royal Free runs one of England's two High-Consequence Infectious Diseases (HCID) centres — sustained training + biosafety overhead on establishment"},
            {"label": "Composition", "value": "Telecoms + postage + printing + courses + training + recruitment-advertising + minor IT/software subs + professional fees + transaction-advisory fees"},
            {"label": "Industrial action 2023-24", "value": "44 days junior-doctor + 10 days consultant strike action drove rota-restructuring + agency-recruitment + temporary-staffing-platform spend"},
            {"label": "Frontline Digitisation EPR + transaction advisory", "value": "Cerner Millennium baseline + group-model EPR convergence training/change-mgmt; active North Middlesex acquisition drives elevated 2023-25 due-diligence overhead"},
            {"label": "April 2025 NIC step-up", "value": "Apr 2025 employer-NIC threshold drop + rate to 15% raises forward establishment cost on professional fees + recruitment retainers"},
            {"label": "Funding trajectory", "value": "2021-22 c. £6M → 2023-24 £7.2M → 2024-25 £7.84M — sustained group + transaction overhead"},
            {"label": "Delivery body", "value": "Trust Finance + HR + IT + Communications + Group Functions + Transaction Office + EPR programme office"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2014 Royal Free standalone + pre-2014 Barnet & Chase Farm separate baselines · Successor: post-North Middlesex acquisition consolidated NCL group functions"}
        ],
        "notes": "Royal Free London is one of the NHS's flagship group-model trusts, with the Hampstead site running tertiary renal/transplant, hepatology, HIV and one of the two HCID centres in England layered on top of the Barnet and Chase Farm DGH-acute services. The active acquisition transaction with North Middlesex University Hospital NHS Trust, progressing through 2023-25, drives elevated professional-fee, due-diligence and transaction-advisory overhead through the establishment line — visible in the 2024-25 step-up. The HCID role sustains training and biosafety overhead distinct from peer DGH trusts. Industrial action 2023-24 added rota-restructuring and recruitment costs; Apr 2025 NIC step-up raises forward professional-fee cost on the consolidated group-functions baseline.",
        "sources": [
            {"publisher": "Royal Free London NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.royalfree.nhs.uk/about-us/corporate-information/annual-reports-and-financial-information/"},
            {"publisher": "NHS England", "title": "North Central London ICS — group-model transaction (Royal Free + North Mid)", "url": "https://www.england.nhs.uk/london/our-work/north-central-london/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Royal Free London provider profile (RAL)", "url": "https://www.cqc.org.uk/provider/RAL"},
            {"publisher": "UK Health Security Agency", "title": "High Consequence Infectious Diseases (HCID) network", "url": "https://www.gov.uk/guidance/high-consequence-infectious-diseases-hcid"}
        ],
        "related": ["Royal Free London NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Establishment costs — University Hospital Southampton NHS Foundation Trust", "General supplies & services — North Middlesex University Hospital NHS Trust", "Department of Health and Social Care"]
    },
    "Establishment costs — East Lancashire Hospitals NHS Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "East Lancashire Hospitals NHS Trust"}],
        "description": "ELHT's £7.83M establishment line covers office supplies, postage, telecoms, printing, training, courses, recruitment-advertising, professional fees and minor IT/software subscriptions across the Royal Blackburn Teaching Hospital + Burnley General Teaching Hospital + Pendle Community Hospital + Clitheroe Community Hospital + Accrington Victoria Community Hospital footprint. ELHT is the principal acute provider for Pennine Lancashire, serving a high-deprivation east-Lancashire catchment within the Lancashire & South Cumbria ICS.",
        "beneficiaries": "c. 8,500 WTE staff serving a c. 540,000 Pennine Lancashire catchment (Blackburn with Darwen, Hyndburn, Burnley, Pendle, Rossendale, Ribble Valley); c. 175,000 ED attendances/yr (Royal Blackburn ED + Burnley urgent-care); c. 90,000 admissions/yr; large maternity service across Burnley + Royal Blackburn.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25 · Procurement Act 2023",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£7.83M"},
            {"label": "Trust scale", "value": "c. 8,500 WTE across Royal Blackburn + Burnley + Pendle + Clitheroe + Accrington Victoria"},
            {"label": "Catchment deprivation", "value": "Pennine Lancashire — high IMD deprivation across Blackburn with Darwen + Hyndburn + Burnley; sustains acute activity + recruitment-retention overhead"},
            {"label": "Site rationalisation", "value": "Post-2007 acute reconfiguration concentrated emergency + acute-medicine at Royal Blackburn; Burnley = elective + women & children's"},
            {"label": "Composition", "value": "Telecoms + postage + printing + courses + training + recruitment-advertising + minor IT/software subs + professional fees"},
            {"label": "Industrial action 2023-24", "value": "44 days junior-doctor + 10 days consultant strike action drove rota-restructuring + agency-recruitment + temporary-staffing-platform spend"},
            {"label": "Frontline Digitisation EPR", "value": "Cerner Millennium EPR (live since 2010s) + Frontline Digitisation optimisation drives ongoing training + change-mgmt; Pennine Lancashire recruitment-retention pressure sustains advertising + agency-retainer cost"},
            {"label": "April 2025 NIC step-up", "value": "Apr 2025 employer-NIC threshold drop + rate to 15% raises forward establishment cost on professional fees + recruitment retainers"},
            {"label": "Funding trajectory", "value": "2021-22 c. £6.5M → 2023-24 £7.3M → 2024-25 £7.83M — sustained recruitment churn + EPR optimisation"},
            {"label": "Delivery body", "value": "Trust Finance + HR + IT + Communications corporate functions + EPR programme office"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Lancashire and South Cumbria ICB"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2003 Blackburn, Hyndburn & Ribble Valley + Burnley & Pendle separate trusts · Successor: ICS-shared corporate-services pooling"}
        ],
        "notes": "ELHT runs the Pennine Lancashire acute footprint anchored on Royal Blackburn (post-2007 reconfiguration concentrated emergency + acute medicine here) with Burnley General as the elective + women & children's site, plus community hospitals at Pendle, Clitheroe and Accrington. The high-deprivation east-Lancashire catchment sustains recruitment-retention pressure — visible in advertising, agency-retainer and recruitment-platform spend — relative to neighbouring Manchester and Preston systems. Industrial action 2023-24 added rota-restructuring and recruitment costs; the Cerner Millennium EPR baseline drives ongoing training and change-mgmt under Frontline Digitisation optimisation. Apr 2025 NIC step-up raises forward professional-fee cost.",
        "sources": [
            {"publisher": "East Lancashire Hospitals NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.elht.nhs.uk/about-us/corporate-information/annual-reports-and-accounts"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme + EPR rollout tracker", "url": "https://www.england.nhs.uk/digitaltechnology/connecteddigitalsystems/frontline-digitisation/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "East Lancashire Hospitals provider profile (RXR)", "url": "https://www.cqc.org.uk/provider/RXR"},
            {"publisher": "NHS England", "title": "Lancashire and South Cumbria ICS", "url": "https://www.england.nhs.uk/north-west/lancashire-south-cumbria-integrated-care-system/"}
        ],
        "related": ["East Lancashire Hospitals NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Establishment costs — University Hospitals of Morecambe Bay NHS Foundation Trust", "Frontline Digitisation programme", "Department of Health and Social Care"]
    },
    "General supplies & services — The Mid Yorkshire Hospitals NHS Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "The Mid Yorkshire Hospitals NHS Trust"}],
        "description": "Mid Yorkshire's £7.83M general supplies & services line covers non-clinical consumables, linen, catering provisions, hotel-services materials, office supplies and minor expensed equipment across the three-site footprint of Pinderfields Hospital (Wakefield), Dewsbury and District Hospital and Pontefract Hospital. The trust (rebranded The Mid Yorkshire Teaching NHS Trust from late 2023) serves a c. 525,000 catchment across Wakefield, Dewsbury and Pontefract within the West Yorkshire ICS, with consumables baseline reflecting the consolidated post-2011 PFI new-build at Pinderfields and Pontefract.",
        "beneficiaries": "c. 8,500 WTE staff serving a c. 525,000 catchment across Wakefield, Dewsbury and Pontefract; c. 175,000 ED attendances/yr (Pinderfields A&E + Dewsbury urgent treatment + Pontefract minor injuries); c. 90,000 admissions/yr; major-trauma unit + regional spinal-injuries unit at Pinderfields.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 2 Inventories · Procurement Act 2023 · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "General supplies & services 2024-25", "value": "£7.83M"},
            {"label": "Trust scale", "value": "Three-site acute (Pinderfields + Dewsbury + Pontefract); c. 8,500 WTE; c. 525,000 catchment"},
            {"label": "Pinderfields PFI new build", "value": "Pinderfields + Pontefract PFI new builds operational 2010-11 — modern footprint sustains consumables baseline above pre-build legacy"},
            {"label": "Trust rename", "value": "Rebranded 'The Mid Yorkshire Teaching NHS Trust' from late 2023 — strategic teaching designation; no merger"},
            {"label": "Specialty mix", "value": "Pinderfields = main acute + regional spinal injuries unit + Yorkshire Centre for Burns and Plastic Surgery; Dewsbury = local DGH; Pontefract = local A&E + elective"},
            {"label": "Procurement route", "value": "NHS Supply Chain national framework + West Yorkshire ICS regional collaboration + spot-buy for community + smaller sites"},
            {"label": "Industrial action 2023-24", "value": "44 days junior-doctor + 10 days consultant strike days drove cancellation re-stocking churn + agency-backfill consumable use"},
            {"label": "Procurement Act 2023 + Apr 2025 NIC", "value": "New procurement regime live Oct 2024; Apr 2025 employer-NIC step-up feeds forward unit-cost via supplier pass-through"},
            {"label": "Funding trajectory", "value": "2021-22 c. £6.5M → 2023-24 £7.4M → 2024-25 £7.83M — CPI + activity recovery + spinal-burns demand"},
            {"label": "Delivery body", "value": "Trust Procurement + Supply Chain + Hotel Services + NHS Supply Chain + West Yorkshire ICS procurement collaborative"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + West Yorkshire ICB"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2002 separate Pinderfields, Dewsbury, Pontefract trust baselines · Successor: WY ICS group-procurement scaling + teaching designation"}
        ],
        "notes": "Mid Yorkshire's consumables baseline reflects the consolidated post-2010-11 PFI new-build footprint at Pinderfields and Pontefract — modern build standards (single-room ratios, clinical layout, hotel-services scope) sustain non-clinical consumables above pre-build legacy. The Pinderfields specialist services — regional spinal-injuries unit and Yorkshire Centre for Burns and Plastic Surgery — drive consumables demand layered on the DGH baseline. Industrial action 2023-24 added cancellation re-stocking and agency-backfill use. NHS Supply Chain remains dominant; WY ICS scaling and Apr 2025 NIC step-up shape unit-cost. The late-2023 rebrand was a strategic-designation change, not a merger.",
        "sources": [
            {"publisher": "The Mid Yorkshire Hospitals NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.midyorks.nhs.uk/Annual-Reports"},
            {"publisher": "NHS Supply Chain", "title": "Annual Report 2023-24", "url": "https://www.supplychain.nhs.uk/about-us/our-publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Mid Yorkshire Hospitals provider profile (RXF)", "url": "https://www.cqc.org.uk/provider/RXF"},
            {"publisher": "NHS England", "title": "West Yorkshire ICS — provider collaborative", "url": "https://www.england.nhs.uk/north-east-yorkshire/our-work/west-yorkshire-integrated-care-system/"}
        ],
        "related": ["The Mid Yorkshire Hospitals NHS Trust", "Clinical Supplies & Drugs", "NHS Acute Trusts", "NHS Supply Chain", "General supplies & services — Whittington Health NHS Trust", "Department of Health and Social Care"]
    },
    "Lease expenditure — University Hospitals of Leicester NHS Trust": {
        "aliases": [{"name": "Lease expenditure", "parent": "University Hospitals of Leicester NHS Trust"}],
        "description": "UHL's £7.76M lease line covers IFRS 16 right-of-use depreciation and interest plus residual operating-lease P&L across leased clinic outposts, satellite community sites, modular wards, office accommodation and equipment leases (imaging, dialysis, pool fleet) across the Leicester Royal Infirmary + Leicester General + Glenfield Hospital tri-site complex. UHL is in the original 40-hospital New Hospital Programme cohort with reconfiguration planned onto two acute sites — lease profile in flux pending NHP Reset trajectory.",
        "beneficiaries": "c. 17,000 WTE staff serving a c. 1.1M Leicester, Leicestershire and Rutland catchment plus tertiary referrals (East Midlands Congenital Heart Centre at Glenfield, regional neurosciences/renal/transplant); c. 240,000 ED attendances/yr at Leicester Royal Infirmary ED; c. 200,000 admissions/yr.",
        "legal_basis": "IFRS 16 Leases · DHSC Group Accounting Manual 2024-25 ch.7 · Landlord and Tenant Act 1954 · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "Lease expenditure 2024-25", "value": "£7.76M"},
            {"label": "Trust scale", "value": "Tri-site academic acute (Leicester Royal Infirmary + Leicester General + Glenfield); c. 17,000 WTE — one of England's largest acute trusts"},
            {"label": "IFRS 16 transition (2022-23)", "value": "Operating leases brought on-balance-sheet 2022-23 — lifted lease-line presentation post-transition"},
            {"label": "NHP cohort", "value": "Original 40-hospital New Hospital Programme cohort: reconfiguration onto LRI + Glenfield acute sites + Leicester General redevelopment"},
            {"label": "NHP Reset (Jan 2025)", "value": "Jan 2025 NHP Reset rephased delivery — UHL likely deferred from first wave; lease decisions on modular interim accommodation deferred"},
            {"label": "Lease profile", "value": "Leased clinic outposts + satellite community sites + modular wards + decant accommodation + leased office space + equipment leases (imaging modalities, dialysis modules, pool fleet)"},
            {"label": "East Midlands Congenital Heart Centre", "value": "Glenfield houses the East Midlands Congenital Heart Centre (DOH-saved 2014) — drives specialist equipment leasing"},
            {"label": "Industrial action 2023-24", "value": "Strike days drove modular ward + temporary capacity demand; lease-base churn"},
            {"label": "Funding trajectory", "value": "2021-22 c. £4M (pre-IFRS 16) → 2022-23 step-up post-IFRS 16 → 2024-25 £7.76M — transition + NHP-cohort interim leasing"},
            {"label": "Delivery body", "value": "Trust E&F + Finance + Procurement + NHS Property Services + commercial landlords"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Leicester, Leicestershire and Rutland ICB + New Hospital Programme"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-IFRS 16 (2022) operating-lease P&L baseline · Successor: NHP-cohort post-rebuild owned-estate consolidation"}
        ],
        "notes": "UHL is one of England's largest acute trusts and sits in the original 40-hospital New Hospital Programme cohort, with reconfiguration onto two acute sites (Leicester Royal Infirmary + Glenfield) including Leicester General redevelopment — the January 2025 NHP Reset rephased delivery, deferring UHL from the first wave and extending the interim-accommodation lease horizon. The IFRS 16 transition brought operating leases on-balance-sheet from 2022-23, lifting the line's presentation. The leased estate spans clinic outposts, modular wards, decant accommodation, office space and equipment leases — including specialist imaging, dialysis modules and the East Midlands Congenital Heart Centre at Glenfield. NHP Reset trajectory is the dominant medium-term driver.",
        "sources": [
            {"publisher": "University Hospitals of Leicester NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.leicestershospitals.nhs.uk/aboutus/who-we-are/publications/"},
            {"publisher": "National Audit Office", "title": "Progress with the New Hospital Programme (HC 1662, 2023)", "url": "https://www.nao.org.uk/reports/the-new-hospital-programme/"},
            {"publisher": "Department of Health and Social Care", "title": "New Hospital Programme — Plan for Implementation (Jan 2025 Reset)", "url": "https://www.gov.uk/government/publications/new-hospital-programme-plan-for-implementation"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 7)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "University Hospitals of Leicester provider profile (RWE)", "url": "https://www.cqc.org.uk/provider/RWE"}
        ],
        "related": ["University Hospitals of Leicester NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "New Hospital Programme", "Lease expenditure — Hull University Teaching Hospitals NHS Trust", "Department of Health and Social Care"]
    },
    "Establishment costs — University Hospitals of Morecambe Bay NHS Foundation Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "University Hospitals of Morecambe Bay NHS Foundation Trust"}],
        "description": "UHMBT's £7.75M establishment line covers office supplies, postage, telecoms, printing, training, courses, recruitment-advertising, professional fees and minor IT/software subscriptions across the Royal Lancaster Infirmary + Furness General Hospital (Barrow) + Westmorland General Hospital (Kendal) tri-site footprint plus a community-clinic cohort spanning Cumbria + north Lancashire. The geographically dispersed catchment across the Lancashire & South Cumbria ICS sustains a multi-site corporate-services overhead.",
        "beneficiaries": "c. 6,500 WTE staff serving a c. 365,000 catchment across south Cumbria + north Lancashire (Lancaster, Morecambe, Barrow-in-Furness, Kendal) over c. 1,000 km² of geographically dispersed terrain; c. 100,000 ED attendances/yr (RLI + Furness General EDs); c. 60,000 admissions/yr.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25 · Procurement Act 2023",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£7.75M"},
            {"label": "Trust scale", "value": "c. 6,500 WTE across RLI + Furness General + Westmorland General + community sites"},
            {"label": "Geographic dispersal", "value": "Lancaster + Barrow + Kendal — c. 60-mile spread across south Cumbria + north Lancashire; multi-site corporate overhead"},
            {"label": "Morecambe Bay Investigation legacy", "value": "Kirkup 'Morecambe Bay Investigation' (2015) maternity failings — sustained governance + training + safety-culture overhead on establishment"},
            {"label": "Composition", "value": "Telecoms + postage + printing + courses + training + recruitment-advertising + minor IT/software subs + professional fees + governance-investment"},
            {"label": "Industrial action 2023-24", "value": "44 days junior-doctor + 10 days consultant strike action drove rota-restructuring + agency-recruitment + temporary-staffing-platform spend"},
            {"label": "Frontline Digitisation EPR", "value": "Trust EPR programme (Lorenzo legacy + transition path) drives sustained training + change-mgmt"},
            {"label": "Recruitment + retention", "value": "Rural Cumbria recruitment-retention pressure (especially senior medical) sustains advertising + agency-retainer cost"},
            {"label": "April 2025 NIC step-up", "value": "Apr 2025 employer-NIC threshold drop + rate to 15% raises forward establishment cost on professional fees + recruitment retainers"},
            {"label": "Funding trajectory", "value": "2021-22 c. £6M → 2023-24 £7.2M → 2024-25 £7.75M — sustained recruitment churn + governance + EPR overhead"},
            {"label": "Delivery body", "value": "Trust Finance + HR + IT + Communications + EPR programme office + maternity-governance team"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-1998 separate Lancaster Acute + Westmorland + Furness baselines · Successor: L&SC ICS corporate-services pooling"}
        ],
        "notes": "UHMBT runs an unusually geographically dispersed three-acute-site footprint across c. 60 miles of south Cumbria and north Lancashire — Lancaster, Barrow and Kendal — sustaining a multi-site corporate-services overhead disproportionate to its bed count. The Kirkup 'Morecambe Bay Investigation' (2015) maternity failings legacy continues to drive sustained governance, training and safety-culture overhead distinct from peer DGH trusts. Rural Cumbria recruitment-retention pressure (especially for senior medical posts at Furness General in Barrow) sustains advertising, agency-retainer and recruitment-platform spend. Industrial action 2023-24 layered rota-restructuring and recruitment costs; the EPR transition path drives change-mgmt; Apr 2025 NIC step-up raises forward professional-fee cost.",
        "sources": [
            {"publisher": "University Hospitals of Morecambe Bay NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.uhmb.nhs.uk/about-us/publications-and-policies/annual-report-and-accounts"},
            {"publisher": "Department of Health and Social Care", "title": "Morecambe Bay Investigation report (Kirkup, 2015)", "url": "https://www.gov.uk/government/publications/morecambe-bay-investigation-report"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "UHMBT provider profile (RTX)", "url": "https://www.cqc.org.uk/provider/RTX"},
            {"publisher": "NHS England", "title": "Lancashire and South Cumbria ICS", "url": "https://www.england.nhs.uk/north-west/lancashire-south-cumbria-integrated-care-system/"}
        ],
        "related": ["University Hospitals of Morecambe Bay NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Establishment costs — East Lancashire Hospitals NHS Trust", "Frontline Digitisation programme", "Department of Health and Social Care"]
    },
    "Establishment costs — East Suffolk and North Essex NHS Foundation Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "East Suffolk and North Essex NHS Foundation Trust"}],
        "description": "ESNEFT's £7.65M establishment line covers office supplies, postage, telecoms, printing, training, courses, recruitment-advertising, professional fees and minor IT/software subscriptions across the Ipswich Hospital + Colchester Hospital twin-site combine plus a community-clinic footprint. The trust formed via the July 2018 merger of Ipswich Hospital NHS Trust and Colchester Hospital University NHS FT — bridging the Suffolk and North East Essex ICS — and sustains a multi-site corporate-services overhead with cross-county-boundary commissioner interfaces.",
        "beneficiaries": "c. 11,000 WTE staff serving a c. 1.0M Suffolk and North East Essex catchment (Ipswich, Colchester, Felixstowe, Tendring, Babergh); c. 200,000 ED attendances/yr (Ipswich + Colchester EDs combined); c. 130,000 admissions/yr; large maternity service across both sites; community-services footprint covers east Suffolk + north-east Essex.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25 · Procurement Act 2023",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£7.65M"},
            {"label": "Trust scale", "value": "c. 11,000 WTE across Ipswich + Colchester acute sites + community footprint; c. 1.0M catchment"},
            {"label": "2018 merger", "value": "Formed July 2018 via merger of Ipswich Hospital NHS Trust + Colchester Hospital University NHS FT — multi-site harmonisation overhead persists"},
            {"label": "Cross-boundary commissioning", "value": "Catchment spans Suffolk + North East Essex ICS — multi-commissioner contract interfaces multiply professional fees vs single-ICS peer trusts"},
            {"label": "Composition", "value": "Telecoms + postage + printing + courses + training + recruitment-advertising + minor IT/software subs + professional fees + merger-harmonisation residual"},
            {"label": "Industrial action 2023-24", "value": "44 days junior-doctor + 10 days consultant strike action drove rota-restructuring + agency-recruitment + temporary-staffing-platform spend"},
            {"label": "Frontline Digitisation EPR", "value": "Epic EPR live (deployed 2018-19 at Cambridge UH; ESNEFT EPR programme on Cerner / Epic-vintage assessment) drives sustained training + interoperability spend"},
            {"label": "Integrated community services", "value": "East Suffolk + Tendring community services integrated into trust scope — broadens corporate-services + recruitment overhead"},
            {"label": "April 2025 NIC step-up", "value": "Apr 2025 employer-NIC threshold drop + rate to 15% raises forward establishment cost on professional fees + recruitment retainers"},
            {"label": "Funding trajectory", "value": "2021-22 c. £6M → 2023-24 £7.1M → 2024-25 £7.65M — sustained merger-harmonisation + recruitment overhead"},
            {"label": "Delivery body", "value": "Trust Finance + HR + IT + Communications corporate functions + EPR programme office"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2018 separate Ipswich + Colchester trust baselines · Successor: ICS-pooled corporate + EPR convergence"}
        ],
        "notes": "ESNEFT formed in July 2018 via the merger of Ipswich Hospital NHS Trust and Colchester Hospital University NHS FT, creating a cross-county-boundary trust whose catchment spans the Suffolk and North East Essex ICS — multi-commissioner contract interfaces multiply professional-fee and contracting overhead vs single-ICS peer trusts. Residual merger-harmonisation overhead persists in the establishment line through 2024-25 across IT, telecoms, training and recruitment platforms. The integrated community-services scope (east Suffolk + Tendring) broadens the corporate-services and recruitment overhead. Industrial action 2023-24 layered rota-restructuring and recruitment costs; the EPR programme drives change-mgmt; Apr 2025 NIC step-up raises forward professional-fee cost.",
        "sources": [
            {"publisher": "East Suffolk and North Essex NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.esneft.nhs.uk/about-us/our-publications/"},
            {"publisher": "NHS England", "title": "Suffolk and North East Essex ICS", "url": "https://www.england.nhs.uk/east-of-england/our-work/suffolk-and-north-east-essex-ics/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "ESNEFT provider profile (RDE)", "url": "https://www.cqc.org.uk/provider/RDE"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme + EPR rollout tracker", "url": "https://www.england.nhs.uk/digitaltechnology/connecteddigitalsystems/frontline-digitisation/"}
        ],
        "related": ["East Suffolk and North Essex NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Establishment costs — Lewisham and Greenwich NHS Trust", "Frontline Digitisation programme", "Department of Health and Social Care"]
    },
    "Establishment costs — Lewisham and Greenwich NHS Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "Lewisham and Greenwich NHS Trust"}],
        "description": "LGT's £7.64M establishment line covers office supplies, postage, telecoms, printing, training, courses, recruitment-advertising, professional fees and minor IT/software subscriptions across the University Hospital Lewisham + Queen Elizabeth Hospital Woolwich (Greenwich) twin-site combine. The trust formed via the Oct 2013 merger of Lewisham Healthcare NHS Trust with the dissolved South London Healthcare NHS Trust's Queen Elizabeth Hospital — a forced reorganisation following the unsustainability regime — and the QEH PFI legacy continues to shape corporate overhead.",
        "beneficiaries": "c. 6,000 WTE staff serving a c. 700,000 south-east London catchment (Lewisham + Greenwich + Bexley overlap); c. 220,000 ED attendances/yr (Lewisham + QEH EDs combined — both very high-volume south-London EDs); c. 95,000 admissions/yr; large maternity service.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25 · Procurement Act 2023",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£7.64M"},
            {"label": "Trust scale", "value": "c. 6,000 WTE across Lewisham + QEH Woolwich; c. 700,000 catchment in SE London"},
            {"label": "2013 forced merger", "value": "Formed Oct 2013 via merger of Lewisham Healthcare with QEH (transferred from dissolved South London Healthcare NHS Trust under unsustainability regime, NHS Act 2006 s.65L)"},
            {"label": "QEH PFI legacy", "value": "Queen Elizabeth Hospital PFI (Greenwich, signed late 1990s) inherited at merger — sustains contract-management overhead distinct from typical DGH"},
            {"label": "Catchment deprivation", "value": "Lewisham + Greenwich — high IMD deprivation; sustains recruitment + retention pressure"},
            {"label": "Composition", "value": "Telecoms + postage + printing + courses + training + recruitment-advertising + minor IT/software subs + professional fees + PFI contract-management"},
            {"label": "Industrial action + EPR", "value": "44 days junior-doctor + 10 days consultant strike days drove rota-restructuring + agency-recruitment; trust EPR (Cerner / SEL ICS convergence) drives training + change-mgmt"},
            {"label": "April 2025 NIC step-up", "value": "Apr 2025 employer-NIC threshold drop + rate to 15% raises forward establishment cost on professional fees + recruitment retainers"},
            {"label": "Funding trajectory", "value": "2021-22 c. £6M → 2023-24 £7.1M → 2024-25 £7.64M — sustained recruitment + PFI overhead"},
            {"label": "Delivery body", "value": "Trust Finance + HR + IT + Communications + EPR programme office + PFI contract-management team"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + South East London ICB"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2013 Lewisham Healthcare standalone + South London Healthcare QEH baseline · Successor: SEL ICS group-functions pooling"}
        ],
        "notes": "LGT formed via the October 2013 merger of Lewisham Healthcare NHS Trust with the Queen Elizabeth Hospital Woolwich, transferred from the dissolved South London Healthcare NHS Trust under the NHS Act 2006 unsustainability regime — a forced reorganisation that drew the 'Save Lewisham Hospital' campaign and a 2013 Court of Appeal judgment shaping the final trust footprint. The QEH PFI legacy inherited at merger sustains contract-management overhead distinct from DGH peers. The high-deprivation Lewisham + Greenwich catchment sustains recruitment pressure. Industrial action 2023-24 layered rota-restructuring costs; EPR programme drives change-mgmt; Apr 2025 NIC step-up raises forward professional-fee cost.",
        "sources": [
            {"publisher": "Lewisham and Greenwich NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.lewishamandgreenwich.nhs.uk/about-us/publications/"},
            {"publisher": "Department of Health", "title": "South London Healthcare NHS Trust dissolution + Trust Special Administrator final report (2013)", "url": "https://www.gov.uk/government/publications/south-london-healthcare-nhs-trust-and-the-nhs-in-south-east-london"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Lewisham and Greenwich provider profile (RJ2)", "url": "https://www.cqc.org.uk/provider/RJ2"},
            {"publisher": "NHS England", "title": "South East London ICS — provider collaborative", "url": "https://www.england.nhs.uk/london/our-work/south-east-london/"}
        ],
        "related": ["Lewisham and Greenwich NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Establishment costs — East Suffolk and North Essex NHS Foundation Trust", "Frontline Digitisation programme", "Department of Health and Social Care"]
    },
    "General supplies & services — North West Anglia NHS Foundation Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "North West Anglia NHS Foundation Trust"}],
        "description": "NWAFT's £7.61M general supplies & services line covers non-clinical consumables, linen, catering, hotel-services materials, office supplies and minor expensed equipment across the Peterborough City Hospital + Hinchingbrooke Hospital + Stamford and Rutland Hospital tri-site footprint. The trust formed via the April 2017 merger of Peterborough & Stamford Hospitals NHS FT and Hinchingbrooke Health Care NHS Trust — bringing the 2007-signed Peterborough City PFI into a wider trust and broadening the consumables baseline across Cambridgeshire & Peterborough ICS.",
        "beneficiaries": "c. 6,500 WTE staff serving a c. 800,000 catchment across Peterborough, Huntingdonshire and South Lincolnshire (Stamford, Rutland); c. 175,000 ED attendances/yr (Peterborough + Hinchingbrooke EDs combined); c. 90,000 admissions/yr; large maternity service at Peterborough.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 2 Inventories · Procurement Act 2023 · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "General supplies & services 2024-25", "value": "£7.61M"},
            {"label": "Trust scale", "value": "Three-site acute (Peterborough City + Hinchingbrooke + Stamford); c. 6,500 WTE; c. 800,000 catchment"},
            {"label": "2017 merger", "value": "Formed Apr 2017 via merger of Peterborough & Stamford Hospitals NHS FT + Hinchingbrooke Health Care NHS Trust — broadened consumables baseline"},
            {"label": "Peterborough PFI", "value": "Peterborough City Hospital PFI signed 2007, operational 2010 — modern build sustains hotel-services consumables baseline"},
            {"label": "Hinchingbrooke history", "value": "Hinchingbrooke = first NHS hospital franchised to private operator (Circle Health Mar 2012-Mar 2015 contract); returned to NHS pre-merger"},
            {"label": "Procurement route", "value": "NHS Supply Chain national framework + Cambridgeshire & Peterborough ICS regional collaboration + spot-buy"},
            {"label": "Industrial action 2023-24", "value": "44 days junior-doctor + 10 days consultant strike days drove cancellation re-stocking churn + agency-backfill consumable use"},
            {"label": "Procurement Act 2023 + Apr 2025 NIC", "value": "New procurement regime live Oct 2024; Apr 2025 employer-NIC step-up feeds forward unit-cost via supplier pass-through"},
            {"label": "Funding trajectory", "value": "2021-22 c. £6M → 2023-24 £7.2M → 2024-25 £7.61M — sustained CPI + activity recovery across tri-site"},
            {"label": "Delivery body", "value": "Trust Procurement + Supply Chain + Hotel Services + NHS Supply Chain + C&P ICS procurement collaborative"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Cambridgeshire and Peterborough ICB"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2017 separate Peterborough & Stamford + Hinchingbrooke baselines · Successor: C&P ICS group-procurement scaling"}
        ],
        "notes": "NWAFT formed in April 2017 via the merger of Peterborough & Stamford Hospitals NHS FT and Hinchingbrooke Health Care NHS Trust, creating a tri-site acute trust spanning Cambridgeshire and South Lincolnshire. The Peterborough City Hospital PFI (signed 2007, operational 2010) sustains a modern hotel-services consumables baseline across the main acute site. Hinchingbrooke carries the legacy of the 2012-2015 Circle Health franchise — the first NHS hospital franchised to a private operator — returned to NHS direct operation prior to the 2017 merger. Industrial action 2023-24 added cancellation re-stocking and agency-backfill use. NHS Supply Chain remains dominant; C&P ICS scaling and Apr 2025 NIC step-up shape unit-cost.",
        "sources": [
            {"publisher": "North West Anglia NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.nwangliaft.nhs.uk/about-us/publications/"},
            {"publisher": "National Audit Office", "title": "Hinchingbrooke Health Care NHS Trust franchise (HC 1011, 2012; HC 408, 2015)", "url": "https://www.nao.org.uk/reports/the-franchising-of-hinchingbrooke-health-care-nhs-trust/"},
            {"publisher": "NHS Supply Chain", "title": "Annual Report 2023-24", "url": "https://www.supplychain.nhs.uk/about-us/our-publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "NWAFT provider profile (RGN)", "url": "https://www.cqc.org.uk/provider/RGN"}
        ],
        "related": ["North West Anglia NHS Foundation Trust", "Clinical Supplies & Drugs", "NHS Acute Trusts", "NHS Supply Chain", "General supplies & services — Whittington Health NHS Trust", "Department of Health and Social Care"]
    },
    "Establishment costs — The Royal Wolverhampton NHS Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "The Royal Wolverhampton NHS Trust"}],
        "description": "RWT's £7.58M establishment line covers office supplies, postage, telecoms, printing, training, courses, recruitment-advertising, professional fees and minor IT/software subscriptions across the New Cross Hospital + West Park Hospital + Cannock Chase Hospital footprint plus a substantial primary-care plus community-services scope. RWT is one of England's most vertically-integrated trusts — operating GP practices via Vertical Integration of Primary Care plus community services across Wolverhampton — broadening corporate-services overhead vs typical acute peers in the Black Country ICS.",
        "beneficiaries": "c. 9,500 WTE staff serving a c. 470,000 Wolverhampton + Cannock catchment plus a primary-care list of c. 80,000 patients across vertically-integrated GP practices; c. 175,000 ED attendances/yr at New Cross ED; c. 95,000 admissions/yr; specialist heart-and-lung centre at New Cross.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25 · Procurement Act 2023 · NHS (General Medical Services Contracts) Regulations 2015",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£7.58M"},
            {"label": "Trust scale", "value": "c. 9,500 WTE across New Cross + West Park + Cannock Chase + community + vertically-integrated GP practices"},
            {"label": "Vertical integration of primary care", "value": "RWT operates a sizeable cohort of Wolverhampton GP practices under vertical-integration model — broadens corporate-services + recruitment + training overhead well beyond typical acute peer"},
            {"label": "Site model", "value": "New Cross Hospital (main acute + heart-lung centre) + West Park (rehab) + Cannock Chase Hospital (DGH spoke) + c. 5+ vertically-integrated GP practices"},
            {"label": "Specialty mix", "value": "Heart and Lung Centre at New Cross — regional cardiothoracic + thoracic surgery + interventional cardiology"},
            {"label": "Composition", "value": "Telecoms + postage + printing + courses + training + recruitment-advertising + minor IT/software subs + professional fees + GMS contract administration"},
            {"label": "Industrial action 2023-24", "value": "44 days junior-doctor + 10 days consultant strike action drove rota-restructuring + agency-recruitment + temporary-staffing-platform spend"},
            {"label": "Frontline Digitisation EPR", "value": "Trust EPR (Cerner / system-c blend) drives sustained training + change-mgmt; primary-care system integration extra layer"},
            {"label": "April 2025 NIC step-up", "value": "Apr 2025 employer-NIC threshold drop + rate to 15% raises forward establishment cost on professional fees + recruitment retainers + GP-practice payroll"},
            {"label": "Funding trajectory", "value": "2021-22 c. £6M → 2023-24 £7.1M → 2024-25 £7.58M — sustained vertically-integrated overhead + recruitment churn"},
            {"label": "Delivery body", "value": "Trust Finance + HR + IT + Communications + Primary Care directorate + EPR programme office"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2014 acute-only RWT baseline · Successor: post-vertical-integration consolidated acute + primary-care functions"}
        ],
        "notes": "RWT runs one of England's most extensive vertical-integration-of-primary-care models — the trust directly operates a sizeable cohort of Wolverhampton GP practices alongside the New Cross + West Park + Cannock Chase acute and rehabilitation footprint, broadening corporate-services overhead across HR, IT, finance and recruitment well beyond the typical acute-peer baseline. The Heart and Lung Centre at New Cross adds tertiary-cardiothoracic specialty overhead. Industrial action 2023-24 layered rota-restructuring and recruitment costs on the acute rotas; the EPR programme drives change-mgmt with extra integration-layer complexity for primary-care system interoperability. Apr 2025 employer-NIC step-up raises forward establishment cost both on trust-employed staff and on the GMS-payroll layer.",
        "sources": [
            {"publisher": "The Royal Wolverhampton NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.royalwolverhampton.nhs.uk/about-us/key-publications/annual-reports/"},
            {"publisher": "NHS England", "title": "Vertical integration of primary care — guidance + case studies", "url": "https://www.england.nhs.uk/gp/the-best-of-care-near-where-you-live/integrated-models-of-care/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "RWT provider profile (RL4)", "url": "https://www.cqc.org.uk/provider/RL4"},
            {"publisher": "NHS England", "title": "Black Country ICS", "url": "https://www.england.nhs.uk/midlands/our-work/black-country-integrated-care-system/"}
        ],
        "related": ["The Royal Wolverhampton NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Establishment costs — Hull University Teaching Hospitals NHS Trust", "Frontline Digitisation programme", "Department of Health and Social Care"]
    },
    "Amortisation — Somerset NHS Foundation Trust": {
        "aliases": [{"name": "Amortisation", "parent": "Somerset NHS Foundation Trust"}],
        "description": "Somerset NHS FT's £7.58M amortisation line covers the periodic write-off of capitalised intangible assets — principally Electronic Patient Record (EPR) software (TPP SystmOne — Somerset is a TPP heartland system), other major clinical-system licences, capitalised software development, and software-as-a-service rights-of-use intangibles per IAS 38. The trust formed via the April 2020 merger of Somerset Partnership NHS FT (community + mental health) with Taunton & Somerset NHS FT (acute) — creating an integrated acute + community + mental-health trust whose breadth multiplies intangibles base.",
        "beneficiaries": "c. 13,000 WTE staff serving a c. 580,000 Somerset catchment across Musgrove Park (Taunton), Yeovil District Hospital (post-Apr 2023 acquisition), community hospitals, mental-health inpatient sites and a county-wide community footprint; c. 175,000 ED attendances/yr (Musgrove + Yeovil EDs combined); integrated community + MH workforce broadens EPR-licence base.",
        "legal_basis": "IAS 38 Intangible Assets · DHSC Group Accounting Manual 2024-25 ch.5 · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£7.58M"},
            {"label": "Trust scale", "value": "Integrated acute + community + mental-health + Yeovil acute; c. 13,000 WTE"},
            {"label": "2020 merger", "value": "Formed Apr 2020 via merger of Somerset Partnership (community + MH) with Taunton & Somerset (acute) — first integrated A+C+MH trust merger in England"},
            {"label": "Yeovil acquisition (Apr 2023)", "value": "Yeovil District Hospital NHS FT acquired Apr 2023 — second-site acute footprint added; intangibles base extended"},
            {"label": "EPR baseline", "value": "TPP SystmOne deeply embedded across community + MH + primary-care interfaces; significant capitalised software intangible amortising"},
            {"label": "Frontline Digitisation EPR", "value": "Acute-side EPR programme (post-merger convergence) drives intangible additions feeding amortisation cohort"},
            {"label": "Composition", "value": "Capitalised software (EPR + departmental clinical systems) + software development + SaaS rights-of-use intangibles + licensed clinical-imaging software"},
            {"label": "Useful-economic-life", "value": "Per DHSC GAM ch.5: software typically 5-10 years; clinical-system EPR 10-15 years; SaaS intangibles per contract term"},
            {"label": "Funding trajectory", "value": "2020-21 c. £4M → 2022-23 (pre-Yeovil) £6M → 2023-24 (post-acquisition) £7.2M → 2024-25 £7.58M"},
            {"label": "Delivery body", "value": "Trust Finance + Capital Accounting + IT directorate + EPR programme office + TPP / Cerner suppliers"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + NHSE Frontline Digitisation team + Somerset ICB"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2020 separate acute + MH/community amort baselines · Successor: integrated trust amort cycle through 2030s on Yeovil + EPR assets"}
        ],
        "notes": "Somerset NHS FT is England's first fully-integrated acute + community + mental-health trust merger (April 2020 merger of Somerset Partnership and Taunton & Somerset), with the April 2023 acquisition of Yeovil District Hospital NHS FT extending the footprint to two acute sites alongside extensive community and MH estate. The amortisation profile reflects TPP SystmOne software deeply embedded across community, mental-health and primary-care interfaces, plus acute-side EPR programme convergence post-merger and post-Yeovil feeding intangibles into the cohort under IAS 38 + GAM ch.5. Useful-economic-lives of 5-10 years for departmental software and 10-15 years for major EPR shape the profile through the 2030s.",
        "sources": [
            {"publisher": "Somerset NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.somersetft.nhs.uk/about-us/our-publications/"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme + EPR rollout tracker", "url": "https://www.england.nhs.uk/digitaltechnology/connecteddigitalsystems/frontline-digitisation/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 5 — Property, plant and equipment + intangibles)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Somerset NHS FT provider profile (RH5)", "url": "https://www.cqc.org.uk/provider/RH5"},
            {"publisher": "NHS England", "title": "Somerset ICS — provider collaborative", "url": "https://www.england.nhs.uk/south-west/somerset-integrated-care-system/"}
        ],
        "related": ["Somerset NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Amortisation — South Tees Hospitals NHS Foundation Trust", "Frontline Digitisation programme", "Department of Health and Social Care"]
    },
    "Amortisation — South Tees Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Amortisation", "parent": "South Tees Hospitals NHS Foundation Trust"}],
        "description": "South Tees' £7.48M amortisation line covers the periodic write-off of capitalised intangible assets — principally Electronic Patient Record (EPR) software, capitalised major-clinical-system development, software-as-a-service rights-of-use intangibles and licensed clinical-imaging software per IAS 38 — across the James Cook University Hospital (Middlesbrough) + Friarage Hospital (Northallerton) twin-site footprint. South Tees runs the Tees Valley's tertiary-specialty hub (regional cardiothoracic, neurosciences, major trauma) alongside the rural Friarage DGH spoke.",
        "beneficiaries": "c. 9,000 WTE staff serving a c. 750,000 Tees Valley + North Yorkshire catchment plus tertiary referrals across the North East; c. 175,000 ED attendances/yr (James Cook ED + Friarage urgent treatment); c. 130,000 admissions/yr; James Cook is the North East's secondary-MTC and a regional neurosciences/cardiothoracic hub.",
        "legal_basis": "IAS 38 Intangible Assets · DHSC Group Accounting Manual 2024-25 ch.5 · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£7.48M"},
            {"label": "Trust scale", "value": "Twin-site academic acute (James Cook + Friarage); c. 9,000 WTE; tertiary-specialty hub for Tees Valley + North Yorkshire"},
            {"label": "Tertiary specialty mix", "value": "James Cook = regional cardiothoracic + neurosciences + Major Trauma + spinal-injuries — multiplies intangible-software base for specialist clinical systems"},
            {"label": "EPR baseline", "value": "Trust EPR programme (Cerner Millennium / convergence path) drives intangible additions feeding amortisation cohort"},
            {"label": "Composition", "value": "Capitalised software (EPR + departmental clinical systems) + software development + SaaS rights-of-use + licensed cardiac/neuro imaging software"},
            {"label": "Useful-economic-life", "value": "Per DHSC GAM ch.5: software typically 5-10 years; clinical-system EPR 10-15 years; SaaS intangibles per contract term"},
            {"label": "Frontline Digitisation EPR", "value": "Trust on Frontline Digitisation EPR rollout pathway — capitalised additions through 2024-26 will feed forward amortisation"},
            {"label": "RAAC remediation", "value": "James Cook + Friarage estate condition reviews ongoing; capitalised software-asset additions independent of RAAC remediation but trust capital programme broad"},
            {"label": "Funding trajectory", "value": "2021-22 c. £6M → 2023-24 £7.0M → 2024-25 £7.48M — sustained EPR + clinical-system amort cycle"},
            {"label": "Delivery body", "value": "Trust Finance + Capital Accounting + IT directorate + EPR programme office + Cerner / Oracle Health"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + NHSE Frontline Digitisation team + North East and North Cumbria ICB"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2002 South Tees Acute Hospitals NHS Trust amort baseline · Successor: post-EPR-convergence intangibles cohort"}
        ],
        "notes": "South Tees runs James Cook University Hospital as the Tees Valley's tertiary-specialty hub — regional cardiothoracic, neurosciences, North East secondary-Major Trauma Centre and spinal-injuries — alongside the rural Friarage DGH spoke at Northallerton, multiplying the specialist clinical-software intangible base. The Cerner Millennium EPR baseline plus departmental imaging and cardiac-cath-lab software dominate the amortisation cohort, with Frontline Digitisation rollout driving capitalised additions through 2024-26 feeding forward amortisation under IAS 38 + GAM ch.5. Useful-economic-lives of 5-10 years for departmental software and 10-15 years for major EPR shape the profile through the 2030s.",
        "sources": [
            {"publisher": "South Tees Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.southtees.nhs.uk/about/publications-policies/"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme + EPR rollout tracker", "url": "https://www.england.nhs.uk/digitaltechnology/connecteddigitalsystems/frontline-digitisation/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 5)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "South Tees provider profile (RTR)", "url": "https://www.cqc.org.uk/provider/RTR"},
            {"publisher": "NHS England", "title": "North East and North Cumbria ICS", "url": "https://www.england.nhs.uk/north-east-yorkshire/our-work/north-east-north-cumbria-integrated-care-system/"}
        ],
        "related": ["South Tees Hospitals NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Amortisation — Somerset NHS Foundation Trust", "Frontline Digitisation programme", "Department of Health and Social Care"]
    },
    "Establishment costs — London North West University Healthcare NHS Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "London North West University Healthcare NHS Trust"}],
        "description": "LNWUH's £7.38M establishment line covers office supplies, postage, telecoms, printing, training, courses, recruitment-advertising, professional fees and minor IT/software subscriptions across the Northwick Park Hospital + Central Middlesex Hospital + Ealing Hospital tri-site footprint plus a substantial integrated community-services scope across Brent, Harrow and Ealing. The trust formed via the Oct 2014 merger of North West London Hospitals NHS Trust with Ealing Hospital NHS Trust and integrated community services — bridging the North West London ICS.",
        "beneficiaries": "c. 9,000 WTE staff serving a c. 1.0M North West London catchment (Brent, Harrow, Ealing) with high deprivation + diversity; c. 240,000 ED attendances/yr (Northwick Park ED — one of London's busiest, plus Ealing UTC); c. 110,000 admissions/yr; integrated community-services workforce.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25 · Procurement Act 2023",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£7.38M"},
            {"label": "Trust scale", "value": "c. 9,000 WTE across Northwick Park + Central Middlesex + Ealing acute + integrated community; c. 1.0M catchment"},
            {"label": "2014 merger", "value": "Formed Oct 2014 via merger of North West London Hospitals + Ealing Hospital + integrated community services — multi-site harmonisation overhead persists"},
            {"label": "Ealing maternity + paediatric closure", "value": "Ealing maternity closed 2015; Ealing paediatric inpatients closed 2016 — pre-merger reconfiguration shaped current footprint"},
            {"label": "Catchment deprivation + diversity", "value": "Brent + Harrow + Ealing — high IMD deprivation + ethnic diversity; sustains recruitment churn + interpreter + cultural-competence training overhead"},
            {"label": "Composition", "value": "Telecoms + postage + printing + courses + training + recruitment-advertising + minor IT/software subs + professional fees + interpreter services"},
            {"label": "Industrial action + EPR", "value": "44 days junior-doctor + 10 days consultant strike days drove rota-restructuring + agency-recruitment; trust EPR (Cerner Millennium / NWL ICS convergence) drives training + change-mgmt"},
            {"label": "April 2025 NIC step-up", "value": "Apr 2025 employer-NIC threshold drop + rate to 15% raises forward establishment cost on professional fees + recruitment retainers"},
            {"label": "Funding trajectory", "value": "2021-22 c. £6M → 2023-24 £6.9M → 2024-25 £7.38M — sustained recruitment + acute/community harmonisation"},
            {"label": "Delivery body", "value": "Trust Finance + HR + IT + Communications + EPR programme office + community-services directorate"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + North West London ICB"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2014 North West London Hospitals + Ealing + PCT-provider community baselines · Successor: NWL ICS group-functions pooling"}
        ],
        "notes": "LNWUH formed in October 2014 via the merger of North West London Hospitals NHS Trust and Ealing Hospital NHS Trust together with integrated community services across Brent, Harrow and Ealing — creating a tri-site acute + integrated community trust within the North West London ICS. Pre-merger Ealing reconfiguration (maternity closed 2015; paediatric inpatients 2016) shaped the current footprint. The high-deprivation, ethnically-diverse catchment sustains recruitment, interpreter-services and cultural-competence training overhead distinct from peer London DGHs. Industrial action 2023-24 layered rota-restructuring costs; the EPR programme drives change-mgmt; Apr 2025 NIC step-up raises forward professional-fee cost.",
        "sources": [
            {"publisher": "London North West University Healthcare NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.lnwh.nhs.uk/about-us/publications/"},
            {"publisher": "NHS England", "title": "North West London ICS — provider collaborative", "url": "https://www.england.nhs.uk/london/our-work/north-west-london/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "LNWUH provider profile (R1K)", "url": "https://www.cqc.org.uk/provider/R1K"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme + EPR rollout tracker", "url": "https://www.england.nhs.uk/digitaltechnology/connecteddigitalsystems/frontline-digitisation/"}
        ],
        "related": ["London North West University Healthcare NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Establishment costs — Lewisham and Greenwich NHS Trust", "Frontline Digitisation programme", "Department of Health and Social Care"]
    },
    "Establishment costs — Hull University Teaching Hospitals NHS Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "Hull University Teaching Hospitals NHS Trust"}],
        "description": "HUTH's £7.31M establishment line covers office supplies, postage, telecoms, printing, training, courses, recruitment-advertising, professional fees and minor IT/software subscriptions across the Hull Royal Infirmary + Castle Hill Hospital twin-site footprint (operating in group-model partnership with NLAG as the Humber Health Partnership from 2024). HUTH is the major teaching/tertiary trust for the Humber sub-region — running regional cancer, cardiothoracic, neurosciences and major-trauma services — with the group model reshaping corporate-services trajectory.",
        "beneficiaries": "c. 11,000 WTE staff serving a c. 600,000 Hull and East Riding catchment plus tertiary referrals across the Humber; c. 175,000 ED attendances/yr at Hull Royal Infirmary ED; c. 130,000 admissions/yr; Castle Hill houses the regional cancer centre, cardiothoracic surgery + Castle Hill specialist cardio-renal hub.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25 · Procurement Act 2023",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£7.31M"},
            {"label": "Trust scale", "value": "c. 11,000 WTE across Hull Royal Infirmary + Castle Hill Hospital; c. 600,000 catchment + tertiary referrals"},
            {"label": "Humber Health Partnership group model", "value": "Joint group-model partnership with Northern Lincolnshire and Goole NHS FT (NLAG) operational from 2024 under shared CEO + group functions — reshapes corporate-services overhead trajectory"},
            {"label": "Tertiary specialty mix", "value": "Castle Hill = regional cancer centre + cardiothoracic + cardio-renal specialist hub; HRI = major trauma + acute medicine + neurosciences"},
            {"label": "University of Hull link", "value": "Hull York Medical School + University of Hull joint academic enterprise — research-admin + clinical-academic recruitment overhead"},
            {"label": "Composition", "value": "Telecoms + postage + printing + courses + training + recruitment-advertising + minor IT/software subs + professional fees + group-transaction advisory"},
            {"label": "Industrial action 2023-24", "value": "44 days junior-doctor + 10 days consultant strike action drove rota-restructuring + agency-recruitment + temporary-staffing-platform spend"},
            {"label": "Frontline Digitisation EPR", "value": "Trust EPR programme (System-C / convergence with NLAG under group model) drives sustained training + change-mgmt"},
            {"label": "April 2025 NIC step-up", "value": "Apr 2025 employer-NIC threshold drop + rate to 15% raises forward establishment cost on professional fees + recruitment retainers"},
            {"label": "Funding trajectory", "value": "2021-22 c. £5.5M → 2023-24 £6.8M → 2024-25 £7.31M — sustained tertiary + group-transaction overhead"},
            {"label": "Delivery body", "value": "Trust Finance + HR + IT + Communications + EPR programme office + Humber Health Partnership group functions"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-1999 separate Hull Royal + Castle Hill baselines · Successor: Humber Health Partnership group consolidation with NLAG"}
        ],
        "notes": "HUTH is the major teaching/tertiary trust for the Humber sub-region — running the regional cancer centre, cardiothoracic surgery and cardio-renal specialist hub at Castle Hill alongside major-trauma and acute-medicine services at Hull Royal Infirmary — multiplying professional-fee, recruitment-retainer and clinical-academic admin overhead vs DGH peers. The Humber Health Partnership group-model arrangement with NLAG operational from 2024 under shared CEO and group functions is reshaping the corporate-services overhead trajectory, with transaction-advisory and harmonisation costs visible through 2024-25. Industrial action 2023-24 layered rota-restructuring costs; EPR convergence drives change-mgmt; Apr 2025 NIC step-up raises forward professional-fee cost.",
        "sources": [
            {"publisher": "Hull University Teaching Hospitals NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.hey.nhs.uk/about-us/key-publications/"},
            {"publisher": "Humber Health Partnership", "title": "HUTH + NLAG group-model partnership", "url": "https://www.humberhealthpartnership.nhs.uk/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "HUTH provider profile (RWA)", "url": "https://www.cqc.org.uk/provider/RWA"},
            {"publisher": "NHS England", "title": "Humber and North Yorkshire ICS", "url": "https://www.england.nhs.uk/north-east-yorkshire/our-work/humber-and-north-yorkshire-integrated-care-system/"}
        ],
        "related": ["Hull University Teaching Hospitals NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Establishment costs — The Royal Wolverhampton NHS Trust", "Frontline Digitisation programme", "Department of Health and Social Care"]
    },
}
