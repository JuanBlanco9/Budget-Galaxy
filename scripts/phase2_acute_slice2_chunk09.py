# -*- coding: utf-8 -*-
# Phase 2 Acute slice 2 — chunk 09 (17 NHS Acute Trust orphan sub-lines)
# Hand-curated trust-specific PROGRAMME-archetype enrichment entries.
# Structural contract per docs/archetype_briefs.md.

NEW = {
    "PFI / LIFT charges — The Leeds Teaching Hospitals NHS Trust": {
        "aliases": [{"name": "PFI / LIFT charges", "parent": "The Leeds Teaching Hospitals NHS Trust"}],
        "description": "Leeds Teaching Hospitals' £9.13M PFI/LIFT line covers the residual unitary-charge pass-through on Leeds-area LIFT (Local Improvement Finance Trust) and PFI components embedded in the trust's seven-site footprint — primarily Wellcome Wing / Oncology PFI elements at St James's plus LIFT-built community accommodation. The headline represents the IFRIC 12 / IFRS 16 split for the smaller PFI/LIFT footprint after the larger acute estate is held on owned-asset balance sheet.",
        "beneficiaries": "c. 21,000 WTE staff serving a c. 800,000 Leeds catchment plus tertiary cancer, neuroscience, paediatric and renal referrals across Yorkshire and the Humber (c. 5.4M tertiary catchment); c. 280,000 ED attendances/yr (LGI + St James's combined); c. 220,000 admissions/yr; Leeds Children's Hospital is the regional tertiary paediatric centre.",
        "legal_basis": "IFRIC 12 Service Concession Arrangements · IFRS 16 Leases (post-2022 transition) · DHSC Group Accounting Manual 2024-25 ch.7 · HM Treasury PFI guidance · NHS LIFT programme guidance · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "PFI / LIFT charges 2024-25", "value": "£9.13M"},
            {"label": "Trust scale", "value": "Seven-site teaching trust (LGI + St James's + Leeds Children's + Chapel Allerton + Wharfedale + Seacroft + Leeds Cancer Centre); c. 21,000 WTE — among the largest trusts in England"},
            {"label": "PFI / LIFT vehicles", "value": "St James's Wellcome Wing / Oncology PFI elements + Leeds-area LIFT-built community-clinic accommodation"},
            {"label": "Estate context", "value": "Most acute estate owned on balance sheet; PFI/LIFT line is residual relative to peer-trust scale (e.g. Sherwood Forest, UHB)"},
            {"label": "Building the Leeds Way", "value": "Hospitals of the Future programme (Adult & Children's) — NHP Cohort 4; new-build replacements affect long-term lifecycle profile"},
            {"label": "Unitary charge composition", "value": "Senior + subordinated debt service + lifecycle hard-FM + indexed soft-FM components"},
            {"label": "Indexation mechanism", "value": "RPI/CPI-linked annual uplift on indexed FM components per concession agreements"},
            {"label": "Funding trajectory", "value": "Stable c. £8-10M/yr range; IFRS 16 2022 transition split reshaped headline; NHP rebuild long-term replaces some PFI estate"},
            {"label": "Delivery body", "value": "LIFT Co + PFI SPVs + FM contractors (Engie/Equans-era novations) + Trust Estates & Facilities"},
            {"label": "Policy owner", "value": "DHSC + HM Treasury PFI guidance + IPA PFI Hand-Back unit + NHSE Provider Finance + West Yorkshire ICB"},
            {"label": "Evaluation evidence", "value": "NAO PFI 2018 + PFI hand-back 2020 reports; PAC PFI hearings; NHP Cohort 4 business case; Trust ARA disclosure"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-PFI/LIFT site infrastructure · Successor: NHP 'Hospitals of the Future' adult + children's new builds (post-2030 Reset deferral) replace some PFI estate"}
        ],
        "notes": "Leeds Teaching Hospitals' PFI/LIFT line is small relative to peer mega-trusts because most acute estate is owned on balance sheet — £9.13M represents residual PFI elements (St James's Wellcome/Oncology, LIFT community accommodation) rather than a whole-hospital PFI like King's Mill or Worcestershire Royal. The 'Building the Leeds Way' / Hospitals of the Future programme (adult + children's rebuilds in NHP Cohort 4) sets a long-term replacement path, but the January 2025 NHP Reset deferred completion into the 2030s, leaving lifecycle hard-FM cycles driving year-on-year volatility. RPI/CPI indexation continues to lift soft-FM; IPA PFI Hand-Back unit guidance shapes residual-concession governance.",
        "sources": [
            {"publisher": "The Leeds Teaching Hospitals NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.leedsth.nhs.uk/about-us/our-publications/annual-report/"},
            {"publisher": "National Audit Office", "title": "PFI and PF2 (HC 718, 2018)", "url": "https://www.nao.org.uk/reports/pfi-and-pf2/"},
            {"publisher": "National Audit Office", "title": "Managing PFI assets and services as contracts end (HC 632, 2020)", "url": "https://www.nao.org.uk/reports/managing-pfi-assets-and-services-as-contracts-end/"},
            {"publisher": "NHS England", "title": "New Hospital Programme — Cohort allocations and Reset (Jan 2025)", "url": "https://www.england.nhs.uk/new-hospital-programme/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 7)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Leeds Teaching Hospitals provider profile (RR8)", "url": "https://www.cqc.org.uk/provider/RR8"}
        ],
        "related": ["The Leeds Teaching Hospitals NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "PFI / LIFT charges — Sherwood Forest Hospitals NHS Foundation Trust", "PFI / LIFT charges — Worcestershire Acute Hospitals NHS Trust", "New Hospital Programme"]
    },
    "Business rates — University Hospitals Sussex NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "University Hospitals Sussex NHS Foundation Trust"}],
        "description": "UHSussex's £9.08M business-rates line covers National Non-Domestic Rates on the trust's seven-site footprint across Sussex — Royal Sussex County Hospital (Brighton), Princess Royal (Haywards Heath), Worthing, St Richard's (Chichester), Royal Alexandra Children's, Sussex Eye and Southlands. Rateable values reflect the 2023 Valuation Office revaluation, with NHS trusts subject to the standard multiplier (51.2p in 2024-25 under the NDRA 2024 split-multiplier regime). The line scales with the new Brighton 3Ts (Teaching, Trauma, Tertiary) build that opened phase 1 in 2023.",
        "beneficiaries": "c. 14,000 WTE staff serving a c. 1.8M Sussex catchment plus tertiary specialty referrals across the South East; c. 290,000 ED attendances/yr (RSCH + Princess Royal + Worthing + St Richard's); c. 180,000 admissions/yr; RSCH = Major Trauma Centre for Sussex.",
        "legal_basis": "Local Government Finance Act 1988 (Sch 6) · Non-Domestic Rating (Multipliers and Private Finance) Act 2024 · Non-Domestic Rating Act 2023 · Valuation Office Agency 2023 revaluation · DHSC Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£9.08M"},
            {"label": "Trust scale", "value": "Seven-site Sussex group (formed Apr 2021 from BSUH + WSHFT merger); c. 14,000 WTE"},
            {"label": "Estate covered", "value": "RSCH Brighton + Princess Royal Haywards Heath + Worthing + St Richard's Chichester + Royal Alex Children's + Sussex Eye + Southlands"},
            {"label": "3Ts new build", "value": "Brighton 3Ts (Teaching, Trauma, Tertiary) phase 1 opened 2023 — increased rateable value baseline"},
            {"label": "Multiplier 2024-25", "value": "Standard 54.6p / Small business 49.9p; new NDRA 2024 split multipliers from 2026-27"},
            {"label": "Revaluation cycle", "value": "VOA 2023 revaluation (effective Apr 2023, AVD 1 Apr 2021) + transitional relief regime"},
            {"label": "Major Trauma Centre", "value": "RSCH = Sussex MTC — high-spec rateable value contribution"},
            {"label": "Funding trajectory", "value": "Pre-merger BSUH + WSHFT separate baselines; post-2021 merger consolidated; 3Ts phase 1 (2023) lift; mature path 2024-25"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + VOA assessment + billing local authorities (Brighton & Hove + West Sussex CC + districts) + DLUHC oversight"},
            {"label": "Policy owner", "value": "HM Treasury + DLUHC (NDR policy) + DHSC + NHSE Provider Finance + Sussex ICB"},
            {"label": "Evaluation evidence", "value": "VOA rating list disclosure; NAO NHS estate review; Trust ARA disclosure; CQC inspection (RYR)"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2021 BSUH + WSHFT separate rate baselines · Successor: post-2026-27 NDRA split-multiplier regime + 3Ts phase 2 completion"}
        ],
        "notes": "UHSussex was formed in April 2021 by the BSUH + WSHFT merger, creating a seven-site Sussex group whose business-rates baseline is the consolidated post-merger position rather than two separate lines. The Brighton 3Ts phase 1 new-build opened in 2023, lifting rateable value at RSCH — the regional Major Trauma Centre. The Non-Domestic Rating (Multipliers and Private Finance) Act 2024 introduces split multipliers from 2026-27 (lower for retail/hospitality, higher for the largest properties), with implications for major NHS sites; the VOA's 2023 revaluation sets the rateable-value baseline for the current list cycle. Billing flows through Brighton & Hove and West Sussex districts.",
        "sources": [
            {"publisher": "University Hospitals Sussex NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.uhsussex.nhs.uk/about/publications/annual-report-and-accounts/"},
            {"publisher": "Valuation Office Agency", "title": "2023 Rating list and revaluation", "url": "https://www.gov.uk/government/organisations/valuation-office-agency"},
            {"publisher": "Department for Levelling Up, Housing and Communities", "title": "Non-Domestic Rating Act 2023 and Multipliers and Private Finance Act 2024 — implementation guidance", "url": "https://www.gov.uk/government/collections/business-rates"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "UHSussex provider profile (RYR)", "url": "https://www.cqc.org.uk/provider/RYR"}
        ],
        "related": ["University Hospitals Sussex NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Establishment costs — University Hospitals Sussex NHS Foundation Trust", "Valuation Office Agency", "Non-Domestic Rating"]
    },
    "Transport (business + patient) — University Hospitals of Leicester NHS Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "University Hospitals of Leicester NHS Trust"}],
        "description": "UHL's £9.04M transport line covers business mileage, inter-site clinical transfers and Non-Emergency Patient Transport Services across the trust's three-site footprint (Leicester Royal Infirmary, Leicester General, Glenfield Hospital). Inter-site flows are particularly heavy because Glenfield concentrates cardiac/respiratory specialities (incl. ECMO) while LRI hosts the MTC and Children's Hospital, generating frequent clinical transfers. The 'Reconfiguring our hospitals' programme (NHP Cohort 2 — service consolidation onto two sites) reshapes the medium-term flow.",
        "beneficiaries": "c. 17,000 WTE staff serving a c. 1.1M Leicester, Leicestershire and Rutland catchment plus tertiary cardiac, respiratory, paediatric and HPB referrals across the East Midlands (c. 5M tertiary catchment); c. 290,000 ED attendances/yr (LRI adult + paediatric ED); c. 200,000 admissions/yr; LRI = East Midlands Major Trauma Centre.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · IFRS 16 Leases (pool fleet) · NHS Act 2006 · Mental Health Act 1983 (s.135/136 conveyance) · NHSE Patient Transport Services Eligibility Framework 2022 · HMRC AMAP · NHS AfC Section 17",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£9.04M"},
            {"label": "Trust scale", "value": "Three-site teaching trust (LRI + Leicester General + Glenfield); c. 17,000 WTE"},
            {"label": "Major Trauma Centre", "value": "LRI = East Midlands MTC — drives inter-trust major-trauma transfer demand"},
            {"label": "Tertiary specialties", "value": "Glenfield: cardiac surgery + ECMO + respiratory; LRI: paediatric tertiary + HPB; inter-site flows substantial"},
            {"label": "PTS provider mix", "value": "EMAS (East Midlands Ambulance Service) PTS + accredited NEPTS contractors (re-tendered via Leicester, Leicestershire and Rutland ICS)"},
            {"label": "Reconfiguration context", "value": "NHP Cohort 2 'Reconfiguring our hospitals' — consolidation onto LRI + Glenfield; Jan 2025 NHP Reset deferred timeline to 2030s"},
            {"label": "Staff mileage + pool fleet (IFRS 16)", "value": "NHS AfC Section 17 / HMRC AMAP 45p first 10,000 miles + 25p thereafter; right-of-use depreciation + interest on leased pool vehicles for AHPs + community teams"},
            {"label": "Funding trajectory", "value": "2021-22 c. £7M → 2023-24 £8M → 2024-25 £9.04M — fuel CPI + activity recovery + ECMO inter-trust referrals + 2023-24 IA churn"},
            {"label": "Delivery body", "value": "Trust E&F + Travel team + EMAS PTS + accredited NEPTS contractors"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + LLR ICB (PTS commissioning) + HMRC (AMAP)"},
            {"label": "Evaluation evidence", "value": "NHSE PTS Eligibility Framework review; NAO ambulance services 2017; Trust ARA disclosure; CQC inspection (RWE)"},
            {"label": "Predecessor / successor", "value": "Predecessor: three-site stand-alone PTS arrangements · Successor: post-reconfiguration two-site model + NHP rebuild reduces some inter-site flow"}
        ],
        "notes": "UHL's transport baseline is driven by the three-site clinical model: Glenfield concentrates cardiac surgery, ECMO and tertiary respiratory while LRI hosts the East Midlands MTC and tertiary paediatric, and Leicester General runs diabetes, renal and elderly-care — generating frequent inter-site clinical transfers handled by EMAS PTS and accredited contractors. The 'Reconfiguring our hospitals' programme (NHP Cohort 2) was designed to consolidate onto LRI + Glenfield, but the January 2025 NHP Reset deferred completion into the 2030s, sustaining the three-site transport baseline. Industrial action 2023-24 drove ad-hoc cover transfers; fuel CPI and activity recovery (incl. ECMO inter-trust referrals) lift the line into 2024-25.",
        "sources": [
            {"publisher": "University Hospitals of Leicester NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.leicestershospitals.nhs.uk/aboutus/our-publications/annual-reports/"},
            {"publisher": "NHS England", "title": "Patient Transport Services Eligibility Framework 2022", "url": "https://www.england.nhs.uk/publication/non-emergency-patient-transport-services-nepts/"},
            {"publisher": "NHS England", "title": "New Hospital Programme — Cohort 2 (Leicester) and Reset (Jan 2025)", "url": "https://www.england.nhs.uk/new-hospital-programme/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "UHL provider profile (RWE)", "url": "https://www.cqc.org.uk/provider/RWE"}
        ],
        "related": ["University Hospitals of Leicester NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Establishment costs — University Hospitals of Leicester NHS Trust", "New Hospital Programme", "Transport (business + patient) — Imperial College Healthcare NHS Trust"]
    },
    "Amortisation — Guy's & St Thomas' NHS Foundation Trust": {
        "aliases": [{"name": "Amortisation", "parent": "Guy's & St Thomas' NHS Foundation Trust"}],
        "description": "GSTT's £8.94M amortisation line covers the systematic write-down of capitalised intangible assets — primarily software licences, the Epic EPR (Electronic Patient Record) implementation, software-as-a-service implementation costs, internally-generated clinical software and acquired digital systems. GSTT was an early Epic adopter (go-live 2023 on the £400M+ Apollo programme spanning GSTT + KCH), driving a substantial intangible-asset baseline whose IAS 38 amortisation flows through this line over the asset's useful economic life (typically 5-10 years for EPR/software).",
        "beneficiaries": "c. 23,000 WTE staff serving a c. 2.6M south London catchment plus tertiary cardiothoracic, transplant, foetal medicine and renal referrals nationally; c. 240,000 ED attendances/yr (St Thomas' adult ED + Evelina paediatric ED); c. 220,000 admissions/yr; Evelina London Children's Hospital is a national tertiary paediatric centre.",
        "legal_basis": "IAS 38 Intangible Assets · IFRIC 22 SaaS configuration/customisation costs guidance (IFRIC March 2021 agenda decision) · DHSC Group Accounting Manual 2024-25 ch.5 · NHS Act 2006 · Health and Care Act 2022 · NHSE Frontline Digitisation programme guidance",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£8.94M"},
            {"label": "Trust scale", "value": "Multi-site academic acute (St Thomas' + Guy's + Evelina London + Royal Brompton + Harefield post-2021 group); c. 23,000 WTE"},
            {"label": "Apollo EPR programme", "value": "Epic EPR cross-trust (GSTT + KCH) — go-live 2023; £400M+ programme cost; capitalised intangible drives IAS 38 amortisation cycle"},
            {"label": "Asset base composition", "value": "Epic EPR licences + implementation costs + clinical software + radiology PACS + internally-generated clinical apps + research software; 5-10yr UEL per IAS 38 / DHSC GAM ch.5"},
            {"label": "IFRIC 22 effect", "value": "March 2021 SaaS configuration/customisation agenda decision reshaped capitalisation boundary; some costs reclassified opex"},
            {"label": "Frontline Digitisation context", "value": "NHSE Frontline Digitisation programme funds EPR rollouts to 'core' standard by 2026; GSTT well ahead with Epic"},
            {"label": "Royal Brompton & Harefield acquisition", "value": "Feb 2021 group integration — added cardiothoracic specialty intangibles to consolidated balance sheet"},
            {"label": "Funding trajectory", "value": "Pre-Apollo £4-5M → 2023-24 post-Epic go-live £8M → 2024-25 £8.94M — first full year of Epic intangible amortisation; cycle continues 5-10yr"},
            {"label": "Delivery body", "value": "Trust IT + Apollo programme + Epic Systems Corp + DHSC Frontline Digitisation funding"},
            {"label": "Policy owner", "value": "DHSC + NHSE Frontline Digitisation + NHSE Provider Finance + South East London ICB"},
            {"label": "Evaluation evidence", "value": "NHSE Frontline Digitisation programme evaluation; NAO Digital Transformation in the NHS (HC 8, 2020); Trust ARA disclosure"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2023 Allscripts / iSOFT legacy systems · Successor: Apollo Epic + integrated radiology/PACS + AI-clinical-decision modules amortising over 2024-2030+"}
        ],
        "notes": "GSTT's £8.94M amortisation reflects the trust being one of the most digitally advanced in the NHS — the Apollo programme go-live in 2023 deployed Epic EPR across GSTT and King's College Hospital under a shared £400M+ implementation, capitalising software licences, implementation labour and configuration costs that flow through IAS 38 amortisation over typical 5-10 year UELs. The IFRIC 22 SaaS agenda decision (March 2021) reshaped the capitalisation boundary, with some elements reclassified to opex. The February 2021 Royal Brompton & Harefield group integration added cardiothoracic specialty intangibles. NHSE Frontline Digitisation's 2026 'core' EPR target keeps the sector trajectory; GSTT's first full year of Epic amortisation in 2024-25 sets the new baseline.",
        "sources": [
            {"publisher": "Guy's & St Thomas' NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.guysandstthomas.nhs.uk/about-us/corporate-information/annual-reports"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/connecting-health-and-care-providers/frontline-digitisation/"},
            {"publisher": "National Audit Office", "title": "Digital transformation in the NHS (HC 8, 2020)", "url": "https://www.nao.org.uk/reports/the-use-of-digital-technology-in-the-nhs/"},
            {"publisher": "IFRS Foundation / IFRIC", "title": "Configuration or customisation costs in a cloud computing arrangement (IFRIC March 2021 agenda decision)", "url": "https://www.ifrs.org/news-and-events/news/2021/04/ifric-update-march-2021/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 5)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "GSTT provider profile (RJ1)", "url": "https://www.cqc.org.uk/provider/RJ1"}
        ],
        "related": ["Guy's & St Thomas' NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Frontline Digitisation Programme", "Termination & post-employment — Guy's & St Thomas' NHS Foundation Trust", "Amortisation — Royal Devon University Healthcare NHS Foundation Trust"]
    },
    "General supplies & services — East Lancashire Hospitals NHS Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "East Lancashire Hospitals NHS Trust"}],
        "description": "ELHT's £8.91M general supplies & services line covers non-clinical consumables, linen, catering provisions, hotel-services materials, office supplies, IT consumables and minor expensed equipment across the trust's five-site footprint — Royal Blackburn Teaching Hospital, Burnley General Teaching Hospital, Pendle Community, Clitheroe Community and Accrington Victoria. The trust serves a mixed urban/rural Lancashire & East Lancs catchment with high deprivation in Blackburn-with-Darwen and Burnley, driving above-peer ED throughput and consequent non-clinical consumables baseline.",
        "beneficiaries": "c. 8,500 WTE staff serving a c. 530,000 East Lancashire catchment (Blackburn-with-Darwen, Burnley, Pendle, Hyndburn, Ribble Valley, Rossendale); c. 175,000 ED attendances/yr (Royal Blackburn ED + urgent care centres); c. 90,000 admissions/yr; large maternity and women's-health service.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 2 Inventories · Procurement Act 2023 · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "General supplies & services 2024-25", "value": "£8.91M"},
            {"label": "Trust scale", "value": "Five-site (Royal Blackburn + Burnley General + Pendle Community + Clitheroe Community + Accrington Victoria); c. 8,500 WTE"},
            {"label": "Catchment deprivation", "value": "Blackburn-with-Darwen + Burnley + Pendle — high IMD; drives ED (c. 175k attendances/yr) + maternity volume"},
            {"label": "Procurement route", "value": "NHS Supply Chain national framework + Lancashire & South Cumbria ICS collaborative + trust-direct contracts"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove cancellation re-stocking + agency backfill churn"},
            {"label": "April 2025 NIC + CPI uplift", "value": "Non-clinical CPI feeds forward unit-cost pressure"},
            {"label": "L&SC ICS context", "value": "Lancashire & South Cumbria ICS-wide procurement collaboration with LTHTR + Blackpool Teaching + UHMBT"},
            {"label": "Funding trajectory", "value": "2021-22 c. £7M → 2023-24 £8M → 2024-25 £8.91M — sustained CPI + activity uplift"},
            {"label": "Delivery body", "value": "Trust Procurement + NHS Supply Chain (DHSC ALB) + L&SC ICS procurement collaborative"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Lancashire & South Cumbria ICB"},
            {"label": "Evaluation evidence", "value": "Model Hospital benchmarks; NHSE NCDR procurement data; Trust ARA disclosure; CQC inspection (RXR)"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-NHS Supply Chain reform (2018) decentralised procurement · Successor: ICS-wide collaborative procurement scaling"}
        ],
        "notes": "ELHT's general supplies & services baseline reflects a five-site footprint serving one of the most deprived catchments in North West England — Blackburn-with-Darwen and Burnley both rank highly on IMD, driving sustained ED throughput at Royal Blackburn and a large maternity/women's health service that lifts non-clinical consumables above peer DGHs of similar bed count. NHS Supply Chain (DHSC ALB) remains the dominant procurement vehicle, with L&SC ICS collaborative scaling alongside Lancashire Teaching, Blackpool Teaching and UHMBT as the medium-term unit-cost lever. Industrial action 2023-24 drove re-stocking churn plus agency-backfill consumables; non-clinical CPI feeds forward unit-cost pressure into 2025-26.",
        "sources": [
            {"publisher": "East Lancashire Hospitals NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.elht.nhs.uk/about/our-publications"},
            {"publisher": "NHS Supply Chain", "title": "Annual Report 2023-24", "url": "https://www.supplychain.nhs.uk/about-us/our-publications/"},
            {"publisher": "NHS England", "title": "Lancashire & South Cumbria ICS", "url": "https://www.healthierlsc.co.uk/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "ELHT provider profile (RXR)", "url": "https://www.cqc.org.uk/provider/RXR"}
        ],
        "related": ["East Lancashire Hospitals NHS Trust", "Clinical Supplies & Drugs", "NHS Acute Trusts", "NHS Supply Chain", "General supplies & services — East Sussex Healthcare NHS Trust", "Department of Health and Social Care"]
    },
    "Amortisation — Royal Devon University Healthcare NHS Foundation Trust": {
        "aliases": [{"name": "Amortisation", "parent": "Royal Devon University Healthcare NHS Foundation Trust"}],
        "description": "Royal Devon's £8.71M amortisation line covers the systematic write-down of capitalised intangible assets — software licences, the Epic EPR programme, internally-generated clinical software and acquired digital systems. The trust was formed April 2022 by merger of RD&E NHS FT with Northern Devon Healthcare, consolidating two intangible-asset registers, and went live with Epic EPR in October 2020 — among the earliest English Epic adopters, driving sustained IAS 38 amortisation across a 5-10 year UEL.",
        "beneficiaries": "c. 14,000 WTE staff serving a c. 615,000 Devon catchment (Eastern Devon + Northern Devon) plus tertiary referrals; c. 200,000 ED attendances/yr (Wonford Royal Devon ED + North Devon District Hospital ED); c. 130,000 admissions/yr; integrated acute + community + mental health post-merger model.",
        "legal_basis": "IAS 38 Intangible Assets · IFRIC 22 SaaS configuration/customisation costs guidance · DHSC Group Accounting Manual 2024-25 ch.5 · NHS Act 2006 · Health and Care Act 2022 · NHSE Frontline Digitisation programme guidance",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£8.71M"},
            {"label": "Trust scale", "value": "Two-site major + community footprint (Wonford Royal Devon Exeter + North Devon District Hospital Barnstaple) + community estate; c. 14,000 WTE — formed Apr 2022 merger"},
            {"label": "Epic EPR go-live", "value": "Oct 2020 (RD&E original) — among first English Epic deployments; post-2022 merger extension to ND footprint"},
            {"label": "Asset base composition", "value": "Epic EPR licences + implementation costs + clinical software + radiology PACS + research + integrated community-system intangibles; 5-10yr UEL per IAS 38 / DHSC GAM ch.5"},
            {"label": "Merger integration", "value": "Apr 2022 RD&E + Northern Devon merger — consolidated two intangible registers; some impairment + revaluation through merger accounting"},
            {"label": "Frontline Digitisation context", "value": "NHSE Frontline Digitisation programme funds EPR rollouts to 'core' standard by 2026; Royal Devon ahead of cohort"},
            {"label": "IFRIC 22 effect", "value": "March 2021 SaaS agenda decision reshaped capitalisation boundary"},
            {"label": "Funding trajectory", "value": "Pre-Epic c. £4M → post-2020 go-live £6-7M → 2024-25 £8.71M — Epic amortisation cycle through 2024-2030"},
            {"label": "Delivery body", "value": "Trust IT + Epic Systems Corp + DHSC Frontline Digitisation funding"},
            {"label": "Policy owner", "value": "DHSC + NHSE Frontline Digitisation + NHSE Provider Finance + Devon ICB"},
            {"label": "Evaluation evidence", "value": "NHSE Frontline Digitisation programme evaluation; NAO Digital Transformation in the NHS (HC 8, 2020); Trust ARA disclosure"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2020 Lorenzo / iSOFT legacy systems · Successor: extended Epic + integrated community modules + AI clinical-decision tools amortising 2025-2030+"}
        ],
        "notes": "Royal Devon University Healthcare was formed in April 2022 by the merger of RD&E with Northern Devon Healthcare, creating an integrated acute, community and mental-health provider for Devon. RD&E went live with Epic EPR in October 2020 — among the earliest English deployments — and post-merger the system has been extended into the Northern Devon footprint, capitalising further licence and implementation cost. The IAS 38 amortisation cycle runs over 5-10 year UELs, with the IFRIC 22 SaaS agenda decision (March 2021) reshaping the capitalisation boundary. NHSE Frontline Digitisation funding underpins continued investment as the sector targets 'core' EPR by 2026; Royal Devon's combined intangible base sustains an above-DGH-peer amortisation baseline.",
        "sources": [
            {"publisher": "Royal Devon University Healthcare NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.royaldevon.nhs.uk/about-us/publications/"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/connecting-health-and-care-providers/frontline-digitisation/"},
            {"publisher": "National Audit Office", "title": "Digital transformation in the NHS (HC 8, 2020)", "url": "https://www.nao.org.uk/reports/the-use-of-digital-technology-in-the-nhs/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 5)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Royal Devon University Healthcare provider profile (RH8)", "url": "https://www.cqc.org.uk/provider/RH8"}
        ],
        "related": ["Royal Devon University Healthcare NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Frontline Digitisation Programme", "Amortisation — Guy's & St Thomas' NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Establishment costs — University Hospitals Sussex NHS Foundation Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "University Hospitals Sussex NHS Foundation Trust"}],
        "description": "UHSussex's £8.65M establishment costs line covers postage, telephony, printing, stationery, advertising/recruitment, training, conferences, subscriptions, legal & professional fees and other corporate-overhead support across the seven-site Sussex group. Recruitment-advertising spend has been elevated since the Apr 2021 BSUH+WSHFT merger and the 3Ts new build (phase 1 opened 2023), and ongoing CQC engagement following the post-merger maternity and surgical-services scrutiny has driven legal & professional fees. Industrial action 2023-24 also lifted change-management and communication spend.",
        "beneficiaries": "c. 14,000 WTE staff serving a c. 1.8M Sussex catchment; c. 290,000 ED attendances/yr (RSCH + Princess Royal + Worthing + St Richard's); c. 180,000 admissions/yr; RSCH = Major Trauma Centre.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25 · Public Contracts Regulations 2015 / Procurement Act 2023",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£8.65M"},
            {"label": "Trust scale", "value": "Seven-site Sussex group (formed Apr 2021 BSUH+WSHFT merger); c. 14,000 WTE"},
            {"label": "Composition", "value": "Postage + telephony + print/stationery + advertising/recruitment + training + conferences + subscriptions + legal & professional fees"},
            {"label": "Merger + 3Ts context", "value": "Apr 2021 BSUH + WSHFT merger drove sustained legal/professional + change-mgmt fee uplift; 3Ts Brighton phase 1 opened 2023 + Sussex EPR training spend"},
            {"label": "CQC scrutiny", "value": "Post-merger CQC inspection cycle (RSCH maternity + surgical services) drove legal/regulatory + professional fees"},
            {"label": "Industrial action 2023-24 effect", "value": "Strike-related comms + recruitment advertising + agency-engagement professional fees uplift"},
            {"label": "April 2025 NIC + CPI uplift", "value": "Pay-on-pay-bill items uplifted by NIC step-up; CPI on print/post/conference fees"},
            {"label": "Funding trajectory", "value": "2021-22 post-merger c. £6M → 2023-24 £8M → 2024-25 £8.65M — sustained CPI + 3Ts opening + EPR change cost"},
            {"label": "Delivery body", "value": "Trust Corporate Services + Communications + HR + Legal + external counsel"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Sussex ICB + CQC (regulatory engagement)"},
            {"label": "Evaluation evidence", "value": "Model Hospital corporate-services benchmarks; Trust ARA disclosure; CQC inspection (RYR); NHSE Carter review legacy"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2021 BSUH + WSHFT separate establishment lines · Successor: post-merger consolidated corporate functions + 3Ts phase 2 completion"}
        ],
        "notes": "UHSussex's establishment line reflects the integration overhead of one of the largest recent NHS provider mergers — the April 2021 BSUH + WSHFT consolidation produced a seven-site group with sustained legal & professional, change-management and recruitment-advertising spend through 2023-25 as the new operating model embeds. The 3Ts phase 1 opening in 2023 added training, conference and recruitment activity around the new tertiary specialties; ongoing CQC engagement on RSCH maternity and surgical services keeps legal/regulatory fees elevated. Industrial action 2023-24 drove additional comms and agency-engagement fee spend; April 2025 NIC step-up and CPI on print/post feed forward unit-cost pressure.",
        "sources": [
            {"publisher": "University Hospitals Sussex NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.uhsussex.nhs.uk/about/publications/annual-report-and-accounts/"},
            {"publisher": "Care Quality Commission", "title": "UHSussex inspection reports (RYR)", "url": "https://www.cqc.org.uk/provider/RYR"},
            {"publisher": "NHS England", "title": "3Ts Brighton — capital programme oversight", "url": "https://www.england.nhs.uk/south-east/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Model Hospital corporate-services benchmarks", "url": "https://www.england.nhs.uk/applications/model-hospital/"}
        ],
        "related": ["University Hospitals Sussex NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Business rates — University Hospitals Sussex NHS Foundation Trust", "Establishment costs — University Hospitals of Leicester NHS Trust", "Care Quality Commission"]
    },
    "General supplies & services — University Hospitals of North Midlands NHS Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "University Hospitals of North Midlands NHS Trust"}],
        "description": "UHNM's £8.59M general supplies & services line covers non-clinical consumables, linen, catering, hotel-services materials, office and IT consumables, and minor expensed equipment across the trust's two-site footprint — Royal Stoke University Hospital and County Hospital (Stafford). The trust serves North Staffordshire and Shropshire/mid-Wales tertiary referrals, with Royal Stoke hosting the West Midlands North Major Trauma Centre and a tertiary cardiothoracic centre — driving an above-DGH-peer non-clinical consumables baseline shaped by the two-site model.",
        "beneficiaries": "c. 11,000 WTE staff serving a c. 900,000 North Staffordshire and South Cheshire catchment plus tertiary referrals from Shropshire and mid-Wales; c. 200,000 ED attendances/yr (Royal Stoke ED + County Hospital Stafford urgent care); c. 130,000 admissions/yr; Royal Stoke = MTC.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 2 Inventories · Procurement Act 2023 · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "General supplies & services 2024-25", "value": "£8.59M"},
            {"label": "Trust scale", "value": "Two-site (Royal Stoke + County Stafford); c. 11,000 WTE; Royal Stoke = West Midlands North MTC"},
            {"label": "Tertiary specialty mix", "value": "Cardiothoracic + neurosciences + tertiary paediatric + spinal injuries — wider tertiary catchment lifts non-clinical baseline"},
            {"label": "Procurement route", "value": "NHS Supply Chain national framework + Staffordshire & Stoke-on-Trent ICS collaborative + trust-direct contracts"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove cancellation re-stocking + agency backfill churn"},
            {"label": "April 2025 NIC + CPI uplift", "value": "Non-clinical CPI feeds forward unit-cost pressure"},
            {"label": "Funding trajectory", "value": "2021-22 c. £7M → 2023-24 £8M → 2024-25 £8.59M — sustained CPI + activity uplift + tertiary referral recovery"},
            {"label": "Delivery body", "value": "Trust Procurement + NHS Supply Chain (DHSC ALB) + Staffordshire & Stoke-on-Trent ICS procurement collaborative"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Staffordshire & Stoke-on-Trent ICB"},
            {"label": "Evaluation evidence", "value": "Model Hospital benchmarks; NHSE NCDR procurement data; Trust ARA disclosure; CQC inspection (RJE)"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2014 University Hospital of North Staffordshire + Mid Staffs separate baselines; Mid Staffs dissolution 2014 brought Stafford into UHNM · Successor: ICS-wide procurement collaborative scaling"}
        ],
        "notes": "UHNM was created from the 2014 dissolution of Mid Staffordshire NHS FT (following the Francis Inquiry) which brought Stafford Hospital into a combined trust with University Hospital of North Staffordshire — Royal Stoke and County operate the integrated tertiary + DGH model. Royal Stoke's role as the West Midlands North MTC, tertiary cardiothoracic and tertiary paediatric centre lifts the non-clinical consumables baseline above peer DGHs. NHS Supply Chain (DHSC ALB) remains dominant, with Staffordshire & Stoke-on-Trent ICS collaborative as the medium-term unit-cost lever. Industrial action 2023-24 drove re-stocking churn; April 2025 NIC step-up + non-clinical CPI feed forward unit-cost pressure.",
        "sources": [
            {"publisher": "University Hospitals of North Midlands NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.uhnm.nhs.uk/about-us/publications/"},
            {"publisher": "NHS Supply Chain", "title": "Annual Report 2023-24", "url": "https://www.supplychain.nhs.uk/about-us/our-publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "UHNM provider profile (RJE)", "url": "https://www.cqc.org.uk/provider/RJE"},
            {"publisher": "Mid Staffordshire NHS Foundation Trust Public Inquiry", "title": "Francis Inquiry final report (HC 947, 2013)", "url": "https://webarchive.nationalarchives.gov.uk/ukgwa/20150407084003/http://www.midstaffspublicinquiry.com/report"}
        ],
        "related": ["University Hospitals of North Midlands NHS Trust", "Clinical Supplies & Drugs", "NHS Acute Trusts", "NHS Supply Chain", "General supplies & services — East Lancashire Hospitals NHS Trust", "Department of Health and Social Care"]
    },
    "General supplies & services — East Sussex Healthcare NHS Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "East Sussex Healthcare NHS Trust"}],
        "description": "ESHT's £8.49M general supplies & services line covers non-clinical consumables, linen, catering, hotel-services materials, office and IT consumables, and minor expensed equipment across the trust's two-site acute footprint — Conquest Hospital (Hastings) and Eastbourne District General Hospital — plus community-clinic estate across East Sussex. The trust serves a coastal, ageing catchment with high frailty demand, and operates an integrated acute + community model that broadens the non-clinical consumables base relative to acute-only peers.",
        "beneficiaries": "c. 7,500 WTE staff serving a c. 530,000 East Sussex catchment (Hastings, Rother, Eastbourne, Lewes, Wealden); c. 145,000 ED attendances/yr (Conquest + Eastbourne EDs); c. 75,000 admissions/yr; integrated community services (district nursing, community paediatric, sexual health).",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 2 Inventories · Procurement Act 2023 · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "General supplies & services 2024-25", "value": "£8.49M"},
            {"label": "Trust scale", "value": "Two-site acute + community (Conquest Hastings + Eastbourne DGH); c. 7,500 WTE"},
            {"label": "Catchment ageing profile", "value": "High proportion 65+/85+ across coastal East Sussex — drives elderly-care + frailty consumables baseline"},
            {"label": "Integrated community workforce", "value": "Acute trust integrated with East Sussex community services (district nursing, community paediatric, sexual health) — broadens consumables base"},
            {"label": "Procurement route", "value": "NHS Supply Chain national framework + Sussex ICS collaborative (alongside UHSussex) + trust-direct contracts"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove cancellation re-stocking + agency backfill churn"},
            {"label": "April 2025 NIC + CPI uplift", "value": "Non-clinical CPI feeds forward unit-cost pressure"},
            {"label": "Funding trajectory", "value": "2021-22 c. £6.5M → 2023-24 £7.5M → 2024-25 £8.49M — sustained CPI + activity uplift + frailty demand"},
            {"label": "Delivery body", "value": "Trust Procurement + NHS Supply Chain (DHSC ALB) + Sussex ICS procurement collaborative"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Sussex ICB"},
            {"label": "Evaluation evidence", "value": "Model Hospital benchmarks; NHSE NCDR procurement data; Trust ARA disclosure; CQC inspection (RXC)"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2011 East Sussex Hospitals + East Sussex Downs & Weald + Hastings & Rother PCT separate baselines · Successor: Sussex ICS-wide procurement collaborative scaling"}
        ],
        "notes": "ESHT serves an East Sussex coastal catchment with one of England's older age profiles, sustaining elevated frailty and elderly-care consumable demand at both Conquest (Hastings) and Eastbourne DGH sites. The trust's integrated acute + community model — covering district nursing, community paediatric, sexual health and community-clinic services across East Sussex — broadens the non-clinical consumables base compared to acute-only peers. NHS Supply Chain (DHSC ALB) remains the dominant procurement vehicle, with Sussex ICS collaborative scaling alongside UHSussex as the medium-term unit-cost containment lever. Industrial action 2023-24 drove cancellation re-stocking churn; April 2025 NIC step-up and non-clinical CPI on linen, catering and hotel services feed forward unit-cost pressure.",
        "sources": [
            {"publisher": "East Sussex Healthcare NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.esht.nhs.uk/about-the-trust/key-publications/"},
            {"publisher": "NHS Supply Chain", "title": "Annual Report 2023-24", "url": "https://www.supplychain.nhs.uk/about-us/our-publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Sussex ICS", "url": "https://www.sussex.ics.nhs.uk/"},
            {"publisher": "Care Quality Commission", "title": "ESHT provider profile (RXC)", "url": "https://www.cqc.org.uk/provider/RXC"}
        ],
        "related": ["East Sussex Healthcare NHS Trust", "Clinical Supplies & Drugs", "NHS Acute Trusts", "NHS Supply Chain", "General supplies & services — East Lancashire Hospitals NHS Trust", "University Hospitals Sussex NHS Foundation Trust"]
    },
    "General supplies & services — University Hospitals Plymouth NHS Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "University Hospitals Plymouth NHS Trust"}],
        "description": "UHP's £8.45M general supplies & services line covers non-clinical consumables, linen, catering, hotel-services materials, office and IT consumables, and minor expensed equipment at the single-site Derriford Hospital — the South West Peninsula's tertiary acute centre. Derriford hosts the South West Peninsula Major Trauma Centre and tertiary cardiac, neurosciences, hepatobiliary, renal and oncology services, drawing referrals across Devon, Cornwall and the Isles of Scilly — driving an above-DGH-peer non-clinical consumables baseline shaped by tertiary specialty mix.",
        "beneficiaries": "c. 9,500 WTE staff serving a c. 450,000 Plymouth and South West Devon catchment plus tertiary specialty referrals across Devon, Cornwall and the Isles of Scilly (c. 2.0M tertiary catchment); c. 130,000 ED attendances/yr at Derriford; c. 100,000 admissions/yr; Derriford = South West Peninsula MTC.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 2 Inventories · Procurement Act 2023 · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "General supplies & services 2024-25", "value": "£8.45M"},
            {"label": "Trust scale", "value": "Single-site teaching trust (Derriford Hospital, Plymouth); c. 9,500 WTE; Derriford = South West Peninsula MTC"},
            {"label": "Tertiary specialty mix", "value": "Cardiac surgery + neurosciences + HPB + renal + oncology + plastic surgery — wide tertiary catchment lifts non-clinical baseline"},
            {"label": "Procurement route", "value": "NHS Supply Chain national framework + Devon ICS collaborative (alongside Royal Devon + Torbay & South Devon) + South West Procurement Partnership"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove cancellation re-stocking + agency backfill churn"},
            {"label": "April 2025 NIC + CPI uplift", "value": "Non-clinical CPI feeds forward unit-cost pressure"},
            {"label": "Funding trajectory", "value": "2021-22 c. £6.5M → 2023-24 £7.5M → 2024-25 £8.45M — sustained CPI + activity uplift + tertiary referral recovery"},
            {"label": "Delivery body", "value": "Trust Procurement + NHS Supply Chain (DHSC ALB) + Devon ICS procurement collaborative + South West Procurement Partnership"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Devon ICB"},
            {"label": "Evaluation evidence", "value": "Model Hospital benchmarks; NHSE NCDR procurement data; Trust ARA disclosure; CQC inspection (RK9)"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-NHS Supply Chain reform (2018) decentralised procurement · Successor: Devon ICS-wide procurement collaborative scaling"}
        ],
        "notes": "UHP's general supplies & services baseline reflects Derriford's role as the South West Peninsula's tertiary acute centre — MTC, tertiary cardiothoracic, neurosciences, HPB and renal services drive a wide tertiary catchment that lifts non-clinical consumables above DGH peers. The geographically isolated Plymouth catchment also sustains a higher minimum stocking baseline relative to densely populated regions where pooled stock can be drawn at short notice. NHS Supply Chain (DHSC ALB) is dominant, with Devon ICS collaborative and the South West Procurement Partnership scaling unit-cost levers alongside Royal Devon and Torbay. Industrial action 2023-24 drove re-stocking churn; April 2025 NIC + CPI feed forward pressure.",
        "sources": [
            {"publisher": "University Hospitals Plymouth NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.plymouthhospitals.nhs.uk/aboutus/publications/annualreports/"},
            {"publisher": "NHS Supply Chain", "title": "Annual Report 2023-24", "url": "https://www.supplychain.nhs.uk/about-us/our-publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Devon ICS", "url": "https://onedevon.org.uk/"},
            {"publisher": "Care Quality Commission", "title": "UHP provider profile (RK9)", "url": "https://www.cqc.org.uk/provider/RK9"}
        ],
        "related": ["University Hospitals Plymouth NHS Trust", "Clinical Supplies & Drugs", "NHS Acute Trusts", "NHS Supply Chain", "General supplies & services — University Hospitals of North Midlands NHS Trust", "Royal Devon University Healthcare NHS Foundation Trust"]
    },
    "Establishment costs — University Hospitals of Leicester NHS Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "University Hospitals of Leicester NHS Trust"}],
        "description": "UHL's £8.44M establishment costs line covers postage, telephony, printing, stationery, advertising/recruitment, training, conferences, subscriptions, legal & professional fees and other corporate-overhead support across the three-site Leicester teaching trust. The 'Reconfiguring our hospitals' programme (NHP Cohort 2) plus EPR rollout and ongoing CQC engagement on maternity and emergency-care services have driven elevated legal/professional and change-management spend, layered on substantive recruitment-advertising activity for one of the largest acute trusts in England.",
        "beneficiaries": "c. 17,000 WTE staff serving a c. 1.1M Leicester, Leicestershire and Rutland catchment plus tertiary referrals across the East Midlands; c. 290,000 ED attendances/yr; c. 200,000 admissions/yr; LRI = East Midlands MTC + tertiary paediatric centre.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25 · Public Contracts Regulations 2015 / Procurement Act 2023",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£8.44M"},
            {"label": "Trust scale", "value": "Three-site teaching trust (LRI + Leicester General + Glenfield); c. 17,000 WTE — among the largest in England"},
            {"label": "Composition", "value": "Postage + telephony + print/stationery + advertising/recruitment + training + conferences + subscriptions + legal & professional fees"},
            {"label": "Reconfiguration + EPR context", "value": "NHP Cohort 2 'Reconfiguring our hospitals' drives sustained legal/professional + business-case spend; major EPR rollout adds training + change-mgmt + comms"},
            {"label": "CQC scrutiny", "value": "Maternity + emergency-care CQC engagement drove legal/regulatory + professional fees"},
            {"label": "Industrial action 2023-24 effect", "value": "Strike-related comms + recruitment-advertising + agency-engagement professional fees uplift"},
            {"label": "April 2025 NIC + CPI uplift", "value": "Pay-on-pay-bill items uplifted by NIC step-up; CPI on print/post/conference fees"},
            {"label": "Funding trajectory", "value": "2021-22 c. £6.5M → 2023-24 £8M → 2024-25 £8.44M — sustained CPI + reconfiguration + EPR + IA churn"},
            {"label": "Delivery body", "value": "Trust Corporate Services + Communications + HR + Legal + external counsel"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + LLR ICB + CQC + NHP delivery board"},
            {"label": "Evaluation evidence", "value": "Model Hospital corporate-services benchmarks; NHP business case; Trust ARA disclosure; CQC inspection (RWE)"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2000 separate Leicester trusts · Successor: post-reconfiguration two-site model corporate-services consolidation"}
        ],
        "notes": "UHL's establishment line reflects the corporate overhead of one of England's largest acute trusts operating across three sites with substantial tertiary specialty footprint and an active NHP Cohort 2 'Reconfiguring our hospitals' programme — sustained legal/professional, business-case and change-management spend through 2023-25 as service consolidation onto LRI + Glenfield embeds. The January 2025 NHP Reset deferred completion into the 2030s, sustaining the three-site corporate baseline. Major EPR rollout adds training and comms spend; CQC engagement on maternity + ED keeps legal/regulatory fees elevated. Industrial action 2023-24 drove comms + agency-engagement spend; April 2025 NIC step-up + CPI feed forward pressure.",
        "sources": [
            {"publisher": "University Hospitals of Leicester NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.leicestershospitals.nhs.uk/aboutus/our-publications/annual-reports/"},
            {"publisher": "NHS England", "title": "New Hospital Programme — Cohort 2 (Leicester) and Reset (Jan 2025)", "url": "https://www.england.nhs.uk/new-hospital-programme/"},
            {"publisher": "Care Quality Commission", "title": "UHL inspection reports (RWE)", "url": "https://www.cqc.org.uk/provider/RWE"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Model Hospital corporate-services benchmarks", "url": "https://www.england.nhs.uk/applications/model-hospital/"}
        ],
        "related": ["University Hospitals of Leicester NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Transport (business + patient) — University Hospitals of Leicester NHS Trust", "Establishment costs — University Hospitals Sussex NHS Foundation Trust", "New Hospital Programme"]
    },
    "Establishment costs — North Bristol NHS Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "North Bristol NHS Trust"}],
        "description": "NBT's £8.41M establishment costs line covers postage, telephony, printing, stationery, advertising/recruitment, training, conferences, subscriptions, legal & professional fees and other corporate-overhead support across the Southmead Hospital + Cossham + community-clinic footprint. The trust's major Southmead PFI (Brunel building, signed 2009 with Carillion as construction-and-FM contractor; opened 2014) drives sustained PFI-contract management professional fees, particularly through the Carillion 2018 collapse and Engie/Equans novation cycle that continues to shape FM oversight effort.",
        "beneficiaries": "c. 9,000 WTE staff serving a c. 900,000 North Bristol, South Gloucestershire and northern Somerset catchment plus tertiary referrals (neurosciences, plastic + burns, renal, major trauma); c. 130,000 ED attendances/yr at Southmead ED; c. 100,000 admissions/yr; Southmead = Severn MTC.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25 · Public Contracts Regulations 2015 / Procurement Act 2023",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£8.41M"},
            {"label": "Trust scale", "value": "Single major site (Southmead — Brunel PFI building) + Cossham + community estate; c. 9,000 WTE; Southmead = Severn MTC"},
            {"label": "Composition", "value": "Postage + telephony + print/stationery + advertising/recruitment + training + conferences + subscriptions + legal & professional fees"},
            {"label": "Brunel PFI context", "value": "Southmead Brunel PFI signed 2009 with Carillion; opened May 2014; SPV Hospital Company (Southmead) Ltd"},
            {"label": "Carillion 2018 effect", "value": "Carillion Jan 2018 collapse → Engie / Equans / Sodexo FM novations; sustained legal/professional fee uplift on contract management"},
            {"label": "Industrial action 2023-24 effect", "value": "Strike-related comms + recruitment-advertising + agency-engagement professional fees uplift"},
            {"label": "April 2025 NIC + CPI uplift", "value": "Pay-on-pay-bill items uplifted by NIC step-up; CPI on print/post/conference fees"},
            {"label": "Funding trajectory", "value": "2021-22 c. £6.5M → 2023-24 £8M → 2024-25 £8.41M — sustained CPI + Carillion legacy + tertiary recruitment"},
            {"label": "Delivery body", "value": "Trust Corporate Services + Communications + HR + Legal + external counsel + PFI contract-management team"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Bristol, North Somerset and South Gloucestershire ICB + IPA PFI Hand-Back unit"},
            {"label": "Evaluation evidence", "value": "Model Hospital corporate-services benchmarks; NAO Carillion 2018 and PFI hand-back 2020 reports; Trust ARA disclosure; CQC inspection (RVJ)"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2014 Frenchay + Southmead separate sites · Successor: continued Brunel PFI operation through concession to c. 2044 + post-PFI hand-back planning"}
        ],
        "notes": "NBT's establishment baseline is shaped by the operational complexity of the Southmead Brunel PFI — signed 2009 with Carillion as construction-and-FM contractor, opened May 2014 — and the Carillion 2018 collapse aftermath which forced FM novations to Engie, Equans and Sodexo across hard- and soft-FM components, sustaining a contract-management professional-fee baseline that runs above acute peers without major PFI footprints. Southmead's role as the Severn Major Trauma Centre and tertiary neurosciences, plastics + burns and renal centre also drives a wide recruitment-advertising base. Industrial action 2023-24 lifted comms and agency-engagement professional fees; April 2025 employer-NIC step-up and CPI on print/post/conference inputs feed forward unit-cost pressure into 2025-26.",
        "sources": [
            {"publisher": "North Bristol NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.nbt.nhs.uk/about-us/our-publications/annual-report-accounts"},
            {"publisher": "National Audit Office", "title": "Investigation into the rescue of Carillion's PFI hospital contracts", "url": "https://www.nao.org.uk/reports/investigation-into-the-rescue-of-carillions-pfi-hospital-contracts/"},
            {"publisher": "National Audit Office", "title": "Managing PFI assets and services as contracts end (HC 632, 2020)", "url": "https://www.nao.org.uk/reports/managing-pfi-assets-and-services-as-contracts-end/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "NBT provider profile (RVJ)", "url": "https://www.cqc.org.uk/provider/RVJ"}
        ],
        "related": ["North Bristol NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Establishment costs — University Hospitals of Leicester NHS Trust", "Infrastructure and Projects Authority", "PFI / LIFT charges — Worcestershire Acute Hospitals NHS Trust"]
    },
    "Termination & post-employment — Guy's & St Thomas' NHS Foundation Trust": {
        "aliases": [{"name": "Termination & post-employment", "parent": "Guy's & St Thomas' NHS Foundation Trust"}],
        "description": "GSTT's £8.37M termination & post-employment line covers redundancy payments, ex-gratia exit payments, contractual termination costs, payments in lieu of notice and post-employment benefits accounted under IAS 19 — including the actuarial cost of the unfunded NHS Compensation for Premature Retirement scheme and other defined-benefit post-employment elements outside the main NHS Pension Scheme. The line scales with restructuring activity, particularly post-2021 Royal Brompton & Harefield group integration plus Apollo EPR-related operating-model change.",
        "beneficiaries": "c. 23,000 WTE staff serving a c. 2.6M south London catchment plus tertiary cardiothoracic, transplant, foetal medicine and renal referrals nationally; c. 240,000 ED attendances/yr; c. 220,000 admissions/yr; Evelina London = national tertiary paediatric centre.",
        "legal_basis": "IAS 19 Employee Benefits · NHS Pension Scheme Regulations 2015 (and 1995/2008 sections) · Public Sector Exit Payments Regulations 2020 (revoked Feb 2021 — guidance reinstated) · Social Security Contributions and Benefits Act 1992 · DHSC Group Accounting Manual 2024-25 · NHS Act 2006 · Employment Rights Act 1996",
        "key_stats": [
            {"label": "Termination & post-employment 2024-25", "value": "£8.37M"},
            {"label": "Trust scale", "value": "Multi-site academic acute (St Thomas' + Guy's + Evelina + Royal Brompton + Harefield); c. 23,000 WTE"},
            {"label": "Composition", "value": "Redundancy + PILON + ex-gratia exit + IAS 19 post-employment (CPR scheme + injury benefit + other unfunded elements)"},
            {"label": "Group integration + Apollo", "value": "Feb 2021 Royal Brompton & Harefield group integration drove restructuring exit costs 2022-25; 2023 Apollo Epic go-live drove operating-model change + supportive exit packages"},
            {"label": "Exit payment cap context", "value": "Public Sector Exit Payments Regs 2020 (£95k cap) revoked Feb 2021; HMT/Cabinet Office guidance reinstated; senior-manager exits subject to MAPLE / NHSE approval"},
            {"label": "NHS Pension Scheme membership", "value": "Substantively all staff in NHSPS 1995/2008/2015 sections; CPR scheme sits outside main pension scheme as unfunded employer obligation"},
            {"label": "Industrial action 2023-24 effect", "value": "Indirect — sustained workforce churn + early retirement decisions"},
            {"label": "Funding trajectory", "value": "2021-22 c. £5M → 2023-24 £7M → 2024-25 £8.37M — Brompton group integration + Apollo change + general churn"},
            {"label": "Delivery body", "value": "Trust HR + NHSBSA Pensions + Government Actuary's Department (CPR actuarial valuation) + DHSC"},
            {"label": "Policy owner", "value": "DHSC + HM Treasury + Cabinet Office (exit-pay policy) + NHSE Workforce + South East London ICB"},
            {"label": "Evaluation evidence", "value": "NAO Investigation into the management of NHS finances 2024; NHSBSA Pensions Annual Report; Trust ARA remuneration & exit-package disclosure"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2021 separate GSTT + RB&H baselines · Successor: integrated group restructuring + Apollo-driven role changes through 2024-26"}
        ],
        "notes": "GSTT's termination & post-employment line reflects the trust's scale (c. 23,000 WTE) plus two major change drivers — the February 2021 Royal Brompton & Harefield group integration driving restructuring exit costs through 2022-25, and the 2023 Apollo Epic go-live reshaping operating models with supportive exit packages on legacy roles. The IAS 19 post-employment element captures the unfunded NHS Compensation for Premature Retirement scheme actuarial cost (outside the main NHS Pension Scheme) plus injury-benefit and similar unfunded employer obligations. The Public Sector Exit Payments Regs 2020 (£95k cap) were revoked Feb 2021, with HMT/Cabinet Office guidance reinstating senior-manager exit-payment approval via MAPLE / NHSE.",
        "sources": [
            {"publisher": "Guy's & St Thomas' NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.guysandstthomas.nhs.uk/about-us/corporate-information/annual-reports"},
            {"publisher": "NHS Business Services Authority", "title": "NHS Pensions Annual Report and Accounts 2023-24", "url": "https://www.nhsbsa.nhs.uk/employers/nhs-pensions-employers"},
            {"publisher": "HM Treasury / Cabinet Office", "title": "Public Sector Exit Payments — guidance and senior approval thresholds", "url": "https://www.gov.uk/government/publications/restriction-of-public-sector-exit-payments-directions-2022"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "GSTT provider profile (RJ1)", "url": "https://www.cqc.org.uk/provider/RJ1"}
        ],
        "related": ["Guy's & St Thomas' NHS Foundation Trust", "Staff Costs", "NHS Acute Trusts", "Amortisation — Guy's & St Thomas' NHS Foundation Trust", "NHS Pension Scheme", "NHS Business Services Authority"]
    },
    "PFI / LIFT charges — Northern Care Alliance NHS Foundation Trust": {
        "aliases": [{"name": "PFI / LIFT charges", "parent": "Northern Care Alliance NHS Foundation Trust"}],
        "description": "NCA's £8.37M PFI/LIFT line covers unitary-charge pass-through on PFI elements at the trust's footprint — primarily the Salford Royal extension and Pennine-area LIFT-built community-clinic accommodation across Bury, Oldham and Rochdale. NCA was formed October 2021 by formal merger of Salford Royal NHS FT with Pennine Acute Hospitals NHS Trust, consolidating multiple legacy PFI/LIFT contracts. The line covers IFRIC 12 / IFRS 16 split-recognised debt service, lifecycle and indexed FM components.",
        "beneficiaries": "c. 20,000 WTE staff serving a c. 1.0M Greater Manchester north-east catchment (Salford, Bury, Oldham, Rochdale) plus tertiary neurosciences referrals across the North West; c. 350,000 ED attendances/yr (Salford Royal + Royal Oldham + Fairfield + Rochdale Infirmary EDs); c. 220,000 admissions/yr; Salford Royal = NW Major Trauma Centre (neurosciences specialist).",
        "legal_basis": "IFRIC 12 Service Concession Arrangements · IFRS 16 Leases (post-2022 transition) · DHSC Group Accounting Manual 2024-25 ch.7 · HM Treasury PFI guidance · NHS LIFT programme guidance · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "PFI / LIFT charges 2024-25", "value": "£8.37M"},
            {"label": "Trust scale", "value": "Four-site acute group (Salford Royal + Royal Oldham + Fairfield General Bury + Rochdale Infirmary); c. 20,000 WTE — formed Oct 2021 merger; Salford Royal = NW MTC (neurosciences-led)"},
            {"label": "Merger context", "value": "Oct 2021 formal merger Salford Royal + Pennine Acute → Northern Care Alliance NHS FT; consolidated multiple PFI/LIFT obligations"},
            {"label": "PFI / LIFT vehicles", "value": "Salford Royal extension PFI elements + Pennine-area LIFT-built community-clinic accommodation (Bury, Oldham, Rochdale)"},
            {"label": "Estate covered", "value": "Salford Royal hub + selected Pennine community LIFT clinics; main acute estate held on owned-asset balance sheet"},
            {"label": "Unitary charge composition", "value": "Senior + subordinated debt service + lifecycle hard-FM + indexed soft-FM components"},
            {"label": "Indexation mechanism", "value": "RPI/CPI-linked annual uplift on indexed FM components"},
            {"label": "Funding trajectory", "value": "Pre-merger separate Salford Royal + Pennine baselines; post-2021 consolidated; £8-9M/yr range as RPI uplift continues"},
            {"label": "Delivery body", "value": "PFI SPVs + LIFT Co + FM contractors (post-Carillion Engie/Equans/Sodexo cohort) + Trust E&F"},
            {"label": "Policy owner", "value": "DHSC + HM Treasury PFI guidance + IPA PFI Hand-Back unit + NHSE Provider Finance + Greater Manchester ICB"},
            {"label": "Evaluation evidence", "value": "NAO PFI 2018 + PFI hand-back 2020 reports; PAC PFI hearings; Trust ARA disclosure; CQC inspection (R0A)"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2021 Salford Royal + Pennine Acute separate PFI/LIFT lines · Successor: post-merger consolidated PFI portfolio + IPA hand-back planning"}
        ],
        "notes": "Northern Care Alliance NHS FT was formed in October 2021 by the formal merger of Salford Royal NHS FT with Pennine Acute Hospitals, consolidating multiple PFI/LIFT obligations into a single £8.37M line. The estate spans the Salford Royal hub (NW MTC, tertiary neurosciences) plus the Pennine-area Royal Oldham, Fairfield General (Bury) and Rochdale Infirmary sites, with Pennine LIFT-built community clinics in Bury, Oldham and Rochdale. The line covers IFRIC 12 / IFRS 16 split-recognised debt service, lifecycle hard-FM and indexed soft-FM. Carillion's January 2018 collapse and subsequent FM novations to Engie / Equans / Sodexo shape the FM contract-management baseline; IPA PFI Hand-Back unit guidance shapes residual-concession governance.",
        "sources": [
            {"publisher": "Northern Care Alliance NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.northerncarealliance.nhs.uk/about-us/our-publications"},
            {"publisher": "National Audit Office", "title": "Managing PFI assets and services as contracts end (HC 632, 2020)", "url": "https://www.nao.org.uk/reports/managing-pfi-assets-and-services-as-contracts-end/"},
            {"publisher": "Infrastructure and Projects Authority", "title": "PFI Hand-Back Resource Centre", "url": "https://www.gov.uk/government/collections/pfi-and-pf2"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 7)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "NCA provider profile (R0A)", "url": "https://www.cqc.org.uk/provider/R0A"}
        ],
        "related": ["Northern Care Alliance NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "PFI / LIFT charges — The Leeds Teaching Hospitals NHS Trust", "PFI / LIFT charges — Sherwood Forest Hospitals NHS Foundation Trust", "Infrastructure and Projects Authority"]
    },
    "Establishment costs — Sheffield Teaching Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "Sheffield Teaching Hospitals NHS Foundation Trust"}],
        "description": "STHFT's £8.36M establishment costs line covers postage, telephony, printing, stationery, advertising/recruitment, training, conferences, subscriptions, legal & professional fees and other corporate-overhead support across the trust's five-site footprint — Royal Hallamshire, Northern General, Weston Park (cancer), Charles Clifford Dental and Jessop Wing (women's). The trust's tertiary specialty footprint (cardiothoracic, neurosciences, transplant, spinal injuries, oncology) drives a wide recruitment-advertising and professional-subscription baseline.",
        "beneficiaries": "c. 19,000 WTE staff serving a c. 600,000 Sheffield catchment plus tertiary referrals across South Yorkshire, North Derbyshire and beyond (c. 2.0M tertiary catchment); c. 220,000 ED attendances/yr (Northern General A&E); c. 175,000 admissions/yr; Northern General = South Yorkshire MTC.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25 · Public Contracts Regulations 2015 / Procurement Act 2023",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£8.36M"},
            {"label": "Trust scale", "value": "Five-site teaching trust (Royal Hallamshire + Northern General + Weston Park + Charles Clifford Dental + Jessop Wing); c. 19,000 WTE; Northern General = South Yorkshire MTC"},
            {"label": "Composition", "value": "Postage + telephony + print/stationery + advertising/recruitment + training + conferences + subscriptions + legal & professional fees"},
            {"label": "Tertiary specialty mix", "value": "Cardiothoracic + neurosciences + transplant + spinal injuries + oncology (Weston Park) — wide professional-subscription + conference base"},
            {"label": "Industrial action 2023-24 effect", "value": "Strike-related comms + recruitment-advertising + agency-engagement professional fees uplift"},
            {"label": "EPR programme", "value": "EPR rollout (Lorenzo legacy + planned next-gen) drives training + change-mgmt spend"},
            {"label": "April 2025 NIC + CPI uplift", "value": "Pay-on-pay-bill items uplifted by NIC step-up; CPI on print/post/conference fees"},
            {"label": "Funding trajectory", "value": "2021-22 c. £6.5M → 2023-24 £7.8M → 2024-25 £8.36M — sustained CPI + tertiary recruitment + IA churn"},
            {"label": "Delivery body", "value": "Trust Corporate Services + Communications + HR + Legal + external counsel + IT/EPR programme"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + South Yorkshire ICB + CQC"},
            {"label": "Evaluation evidence", "value": "Model Hospital corporate-services benchmarks; Trust ARA disclosure; CQC inspection (RHQ)"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2001 separate Royal Hallamshire + Northern General trusts · Successor: continued five-site model + EPR-driven corporate-services modernisation"}
        ],
        "notes": "STHFT's establishment baseline reflects the corporate overhead of one of England's largest teaching trusts — five sites with tertiary cardiothoracic, neurosciences, transplant, spinal injuries and oncology services drawing referrals across South Yorkshire, North Derbyshire and beyond, sustaining a wide professional-subscription, conference and recruitment-advertising base. Industrial action 2023-24 drove additional comms, recruitment-advertising and agency-engagement fees; EPR programme effort (Lorenzo legacy + planned next-gen) adds training and change-management spend. April 2025 NIC step-up on pay-on-pay-bill items and CPI on print/post/conference inputs feed forward unit-cost pressure into 2025-26.",
        "sources": [
            {"publisher": "Sheffield Teaching Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.sth.nhs.uk/about-us/key-publications"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/connecting-health-and-care-providers/frontline-digitisation/"},
            {"publisher": "Care Quality Commission", "title": "STHFT inspection reports (RHQ)", "url": "https://www.cqc.org.uk/provider/RHQ"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Model Hospital corporate-services benchmarks", "url": "https://www.england.nhs.uk/applications/model-hospital/"}
        ],
        "related": ["Sheffield Teaching Hospitals NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Establishment costs — North Bristol NHS Trust", "Establishment costs — University Hospitals of Leicester NHS Trust", "Frontline Digitisation Programme"]
    },
    "Establishment costs — United Lincolnshire Hospitals NHS Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "United Lincolnshire Hospitals NHS Trust"}],
        "description": "ULHT's £8.31M establishment costs line covers postage, telephony, printing, stationery, advertising/recruitment, training, conferences, subscriptions, legal & professional fees and other corporate-overhead support across four rural sites — Lincoln County, Pilgrim (Boston), Grantham & District and County Hospital (Louth). Long-running CQC engagement (Requires Improvement) drives sustained legal/regulatory + professional-fee spend, and the Lincoln Acute Reconfiguration / NHP review shapes ongoing business-case and change-management activity.",
        "beneficiaries": "c. 8,500 WTE staff serving a c. 750,000 Lincolnshire catchment (Lincoln, Boston, Grantham, Louth, Skegness); c. 195,000 ED attendances/yr (Lincoln County + Pilgrim + Grantham EDs combined); c. 100,000 admissions/yr; rural-dispersed catchment with significant ambulance-delivered demand.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25 · Public Contracts Regulations 2015 / Procurement Act 2023",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£8.31M"},
            {"label": "Trust scale", "value": "Four-site rural acute (Lincoln County + Pilgrim Boston + Grantham & District + Louth County); c. 8,500 WTE"},
            {"label": "Composition", "value": "Postage + telephony + print/stationery + advertising/recruitment + training + conferences + subscriptions + legal & professional fees"},
            {"label": "CQC + reconfiguration", "value": "Long-running CQC scrutiny (Requires Improvement) on maternity + emergency-care + Lincoln Acute Services Review + NHP-Cohort engagement drive sustained legal/regulatory + business-case + consultation fees"},
            {"label": "Recruitment context", "value": "Persistent rural recruitment challenge → above-peer recruitment-advertising + locum-engagement professional fees"},
            {"label": "Industrial action 2023-24 effect", "value": "Strike-related comms + recruitment-advertising + agency-engagement professional fees uplift"},
            {"label": "April 2025 NIC + CPI uplift", "value": "Pay-on-pay-bill items uplifted by NIC step-up; CPI on print/post/conference fees"},
            {"label": "Funding trajectory", "value": "2021-22 c. £6M → 2023-24 £7.5M → 2024-25 £8.31M — sustained CQC engagement + reconfiguration + IA churn + recruitment effort"},
            {"label": "Delivery body", "value": "Trust Corporate Services + Communications + HR + Legal + external counsel + reconfiguration programme team"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Lincolnshire ICB + CQC + NHSE/I improvement directorate"},
            {"label": "Evaluation evidence", "value": "Model Hospital corporate-services benchmarks; CQC inspection reports; NHSE/I improvement reviews; Trust ARA disclosure"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2000 separate Lincolnshire trusts · Successor: post-reconfiguration acute model + Lincolnshire ICB system-wide modernisation"}
        ],
        "notes": "ULHT's establishment baseline is shaped by sustained CQC engagement — the trust has been Requires Improvement with maternity and emergency-care issues drawing regulatory attention through 2022-25, driving above-peer legal/regulatory + professional-fee spend. The Lincoln Acute Services Review and NHP-cohort engagement layer continued business-case, consultation and reconfiguration legal fees on top of routine corporate-services spend. The geographically dispersed rural Lincolnshire catchment also sustains persistent recruitment challenges that drive higher recruitment-advertising and locum-engagement fees. Industrial action 2023-24 added comms + agency spend; April 2025 NIC step-up + CPI feed forward pressure.",
        "sources": [
            {"publisher": "United Lincolnshire Hospitals NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.ulh.nhs.uk/about/publications/annual-reports/"},
            {"publisher": "Care Quality Commission", "title": "ULHT inspection reports (RWD)", "url": "https://www.cqc.org.uk/provider/RWD"},
            {"publisher": "NHS England", "title": "Lincolnshire ICS — acute services reconfiguration", "url": "https://lincolnshire.icb.nhs.uk/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Model Hospital corporate-services benchmarks", "url": "https://www.england.nhs.uk/applications/model-hospital/"}
        ],
        "related": ["United Lincolnshire Hospitals NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Establishment costs — Sheffield Teaching Hospitals NHS Foundation Trust", "Establishment costs — Worcestershire Acute Hospitals NHS Trust", "Care Quality Commission"]
    },
    "Establishment costs — Worcestershire Acute Hospitals NHS Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "Worcestershire Acute Hospitals NHS Trust"}],
        "description": "WAHT's £8.31M establishment costs line covers postage, telephony, print, stationery, advertising/recruitment, training, conferences, subscriptions, legal & professional fees and other corporate-overhead support across three sites — Worcestershire Royal (Worcester), Alexandra (Redditch) and Kidderminster. The Worcestershire Royal PFI (1999/2002), ongoing CQC engagement, the long-running FAHSW reconfiguration debate and Carillion 2018 collapse FM novations sustain elevated legal/professional fee spend.",
        "beneficiaries": "c. 6,500 WTE staff serving a c. 600,000 Worcestershire catchment (Worcester, Redditch, Bromsgrove, Kidderminster); c. 180,000 ED attendances/yr (Worcester + Redditch Alexandra EDs combined); c. 80,000 admissions/yr; large maternity service.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25 · Public Contracts Regulations 2015 / Procurement Act 2023",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£8.31M"},
            {"label": "Trust scale", "value": "Three-site (Worcestershire Royal + Alexandra Redditch + Kidderminster); c. 6,500 WTE"},
            {"label": "Composition", "value": "Postage + telephony + print/stationery + advertising/recruitment + training + conferences + subscriptions + legal & professional fees"},
            {"label": "PFI + hand-back", "value": "Worcestershire Royal PFI (1999/2002, expires 2032) + Catalyst Healthcare SPV oversight + post-Carillion Engie/Equans FM novation + IPA/HMT PFI Hand-Back unit engagement drive sustained legal/professional fee baseline"},
            {"label": "CQC engagement", "value": "Long-running CQC scrutiny on emergency-care + maternity drove sustained legal/regulatory + professional-fee uplift"},
            {"label": "FAHSW reconfiguration", "value": "Future of Acute Hospital Services in Worcestershire long-running reconfiguration debate — sustained business-case + consultation + legal fees"},
            {"label": "IA 2023-24 + April 2025 NIC + CPI", "value": "Strike-related comms + recruitment-advertising + agency-engagement fee uplift; pay-on-pay-bill items uplifted by NIC step-up; CPI on print/post/conference"},
            {"label": "Funding trajectory", "value": "2021-22 c. £6M → 2023-24 £7.5M → 2024-25 £8.31M — sustained PFI mgmt + reconfiguration + CQC engagement + IA churn"},
            {"label": "Delivery body", "value": "Trust Corporate Services + Communications + HR + Legal + external counsel + PFI contract-management team"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Herefordshire & Worcestershire ICB + CQC + IPA PFI Hand-Back unit"},
            {"label": "Evaluation evidence", "value": "Model Hospital corporate-services benchmarks; NAO PFI hand-back 2020 report; CQC inspection (RWP); Trust ARA disclosure"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2000 separate Worcester + Redditch + Kidderminster trusts · Successor: post-2032 PFI hand-back + post-reconfiguration acute model"}
        ],
        "notes": "WAHT's establishment baseline is shaped by three concurrent pressures: the Worcestershire Royal PFI (signed 1999, operational 2002) requiring sustained Catalyst Healthcare SPV contract management plus post-Carillion Engie/Equans FM novation oversight; the long-running FAHSW reconfiguration debate that has driven sustained business-case, consultation and legal fees over a decade; and ongoing CQC engagement on emergency-care and maternity that keeps legal/regulatory professional fees elevated. Approaching the 2032 PFI expiry, IPA/HMT PFI Hand-Back engagement adds further professional-fee effort. Industrial action 2023-24 lifted comms; April 2025 NIC step-up + CPI feed forward pressure.",
        "sources": [
            {"publisher": "Worcestershire Acute Hospitals NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.worcsacute.nhs.uk/about-us/key-publications/annual-reports"},
            {"publisher": "National Audit Office", "title": "Managing PFI assets and services as contracts end (HC 632, 2020)", "url": "https://www.nao.org.uk/reports/managing-pfi-assets-and-services-as-contracts-end/"},
            {"publisher": "Care Quality Commission", "title": "WAHT inspection reports (RWP)", "url": "https://www.cqc.org.uk/provider/RWP"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Herefordshire & Worcestershire ICS", "url": "https://herefordshireandworcestershireics.nhs.uk/"}
        ],
        "related": ["Worcestershire Acute Hospitals NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "PFI / LIFT charges — Worcestershire Acute Hospitals NHS Trust", "Establishment costs — United Lincolnshire Hospitals NHS Trust", "Infrastructure and Projects Authority"]
    },
}
