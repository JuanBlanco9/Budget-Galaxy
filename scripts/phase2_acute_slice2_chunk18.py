# -*- coding: utf-8 -*-
# Phase 2 Acute slice 2 — chunk 18 (17 NHS Acute Trust orphan sub-lines)
# Hand-curated trust-specific PROGRAMME-archetype enrichment entries.
# Structural contract per docs/archetype_briefs.md.

NEW = {
    "General supplies & services — Stockport NHS Foundation Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "Stockport NHS Foundation Trust"}],
        "description": "Stockport NHS FT's £4.536M general supplies & services line covers non-clinical consumables, linen, catering provisions, hotel-services materials, office supplies and minor expensed equipment at Stepping Hill Hospital plus the trust's integrated Stockport borough community estate. The trust runs the only acute ED for the borough within the Greater Manchester ICS, with a sustained operational-deficit history that has shaped tight non-clinical procurement against Model Hospital benchmarks and GM ICS collaborative scaling.",
        "beneficiaries": "c. 4,500 WTE staff serving a c. 290,000 Stockport borough catchment; c. 110,000 ED attendances/yr at Stepping Hill ED — sole acute ED for the borough; c. 50,000 admissions/yr; integrated borough-wide community workforce (district nursing + therapies + community paediatric).",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 2 Inventories · Procurement Act 2023 · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "General supplies & services 2024-25", "value": "£4.536M"},
            {"label": "Trust scale", "value": "Single acute site (Stepping Hill, Stockport) + integrated Stockport borough community services; c. 4,500 WTE"},
            {"label": "ED throughput", "value": "c. 110,000 attendances/yr — sole acute ED for Stockport borough"},
            {"label": "Procurement route", "value": "NHS Supply Chain national framework + trust-direct contracts + Greater Manchester ICS collaborative procurement"},
            {"label": "Financial recovery context", "value": "Trust historically engaged with NHSE Recovery Support Programme; persistent deficit shapes tight non-clinical procurement discipline"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove cancellation-related re-stocking + agency-backfill consumables"},
            {"label": "April 2025 NIC + CPI uplift", "value": "Apr 2025 employer-NIC step-up on supply-chain pass-through + sustained non-clinical CPI"},
            {"label": "Funding trajectory", "value": "2021-22 c. £3.6M → 2023-24 £4.1M → 2024-25 £4.536M — CPI + activity recovery"},
            {"label": "Delivery body", "value": "Trust Procurement + NHS Supply Chain (DHSC ALB) + GM ICS procurement collaborative + GM mayoral health-devolution oversight"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Greater Manchester ICB"},
            {"label": "Evaluation evidence", "value": "Model Hospital non-clinical benchmarks; CQC RWJ inspection; Trust ARA disclosure; NHSE Recovery Support Programme reviews"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2011 separate acute + Stockport PCT community baselines · Successor: GM ICS collaborative procurement scaling under mayoral devolution"}
        ],
        "notes": "Stockport's baseline reflects integrated acute + community workforce consumption — Stepping Hill plus borough-wide district nursing, therapies and community-paediatric teams broaden non-clinical consumables footprint vs acute-only peers. Persistent operational deficit and historical engagement with NHSE's Recovery Support Programme have driven tight non-clinical procurement against Model Hospital benchmarks. Industrial action 2023-24 lifted cancellation-related re-stocking and agency-backfill use. April 2025 NIC step-up on contractor pass-through and CPI feed forward; Greater Manchester ICS collaborative procurement under mayoral health-devolution is the medium-term lever.",
        "sources": [
            {"publisher": "Stockport NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.stockport.nhs.uk/about-us/our-publications/"},
            {"publisher": "NHS Supply Chain", "title": "Annual Report 2023-24", "url": "https://www.supplychain.nhs.uk/about-us/our-publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Stockport NHS FT provider profile (RWJ)", "url": "https://www.cqc.org.uk/provider/RWJ"},
            {"publisher": "Greater Manchester Integrated Care Partnership", "title": "GM ICS collaborative procurement strategy", "url": "https://gmintegratedcare.org.uk/"}
        ],
        "related": ["Stockport NHS Foundation Trust", "Clinical Supplies & Drugs", "NHS Acute Trusts", "NHS Supply Chain", "General supplies & services — Liverpool University Hospitals NHS Foundation Trust", "Greater Manchester Integrated Care Board"]
    },
    # ENTRY_02
    "Transport (business + patient) — Norfolk and Norwich University Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "Norfolk and Norwich University Hospitals NHS Foundation Trust"}],
        "description": "NNUH's £4.498M transport line covers staff business mileage (AfC Section 17 + HMRC AMAP), pool fleet under IFRS 16, contracted Non-Emergency Patient Transport Services and inter-site transfers across the trust's main Norwich Research Park hospital site plus satellite outpatient/diagnostic centres serving rural Norfolk. As a major teaching trust on the Sep 2023 HSSIB RAAC list with sustained decant + temporary-build works, NNUH's transport baseline reflects acute regional centrality plus rural-county PTS demand.",
        "beneficiaries": "c. 9,000 WTE staff serving a c. 850,000 Norfolk + Waveney catchment plus tertiary specialty referrals across East Anglia; c. 150,000 ED attendances/yr at NNUH ED; c. 100,000 elective + day-case admissions/yr; major rural geography drives sustained PTS demand.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · IFRS 16 Leases (pool fleet) · NHS Act 2006 · NHSE Patient Transport Services Eligibility Framework 2022 · HMRC Approved Mileage Allowance Payments · NHS AfC Section 17 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£4.498M"},
            {"label": "Trust scale", "value": "Single acute teaching site (NNUH, Colney, Norwich Research Park) + satellite outpatient/diagnostic centres; c. 9,000 WTE"},
            {"label": "Rural catchment driver", "value": "Sparse Norfolk + Waveney rural geography drives sustained PTS demand at distance from acute hub"},
            {"label": "RAAC + decant context", "value": "NNUH on Sep 2023 HSSIB RAAC list (27 trusts); RAAC mitigation works drive ad-hoc inter-site / decant transfers"},
            {"label": "PTS provider mix", "value": "East of England Ambulance Service NHS Trust (EEAST) PTS + accredited NEPTS contractors via Norfolk & Waveney ICS framework"},
            {"label": "Staff mileage + IFRS 16 pool fleet", "value": "AfC Section 17 / HMRC AMAP 45p/25p; right-of-use depreciation + interest on leased pool vehicles post-2022-23 IFRS 16 transition"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove ad-hoc inter-site cover transfers + locum mileage claims"},
            {"label": "Funding trajectory", "value": "2021-22 c. £3.5M → 2023-24 £4.1M → 2024-25 £4.498M — fuel CPI + RAAC decant + activity recovery"},
            {"label": "Delivery body", "value": "Trust E&F + Travel team + EEAST PTS + accredited NEPTS contractors"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + Norfolk & Waveney ICB + NHSE PTS policy"},
            {"label": "Evaluation evidence", "value": "NHSE NEPTS Eligibility Framework 2022 review; HSSIB RAAC report Sep 2023; CQC RM1 inspection; Trust ARA disclosure"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-PFI (PFI built 2001) NNUH transport baseline · Successor: post-NHP rebuild + Norfolk & Waveney ICS shared-fleet pooling + EV transition"}
        ],
        "notes": "NNUH's transport baseline reflects three structural drivers: the trust's regional-teaching-centre role on the Norwich Research Park, the sparse Norfolk + Waveney rural geography sustaining PTS demand at distance from the acute hub, and the September 2023 HSSIB RAAC listing that drove sustained mitigation works and ad-hoc decant transfers. The 2001-built PFI estate frames the long-term hand-back planning horizon. Industrial action 2023-24 layered ad-hoc inter-site cover travel and locum mileage on pandemic-recovery activity. The IFRS 16 transition stepped pool fleet on-balance-sheet from 2022-23. April 2025 NIC step-up affects PTS-contractor pass-through; Norfolk & Waveney ICS shared-fleet pooling and EV transition are the medium-term levers.",
        "sources": [
            {"publisher": "Norfolk and Norwich University Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.nnuh.nhs.uk/publications/"},
            {"publisher": "NHS England", "title": "Non-Emergency Patient Transport Services Eligibility Framework 2022", "url": "https://www.england.nhs.uk/long-read/non-emergency-patient-transport-services-eligibility-framework/"},
            {"publisher": "Health Services Safety Investigations Body", "title": "Reinforced autoclaved aerated concrete (RAAC) in NHS hospitals", "url": "https://www.hssib.org.uk/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "NNUH provider profile (RM1)", "url": "https://www.cqc.org.uk/provider/RM1"}
        ],
        "related": ["Norfolk and Norwich University Hospitals NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Transport (business + patient) — Imperial College Healthcare NHS Trust", "New Hospital Programme", "East of England Ambulance Service NHS Trust"]
    },
    "Amortisation — East Lancashire Hospitals NHS Trust": {
        "aliases": [{"name": "Amortisation", "parent": "East Lancashire Hospitals NHS Trust"}],
        "description": "ELHT's £4.488M amortisation line covers the systematic write-down of capitalised intangible assets — software licences, the Cerner Millennium EPR (deployed via Lancashire & South Cumbria Cerner shared-tenancy), capitalised configuration costs, radiology PACS, internally-generated clinical applications and acquired digital systems — across the Royal Blackburn + Burnley General + Pendle Community + Clitheroe Community footprint. Frontline Digitisation funding has accelerated the intangible-asset baseline whose IAS 38 amortisation cycles over typical 5-10 year UELs.",
        "beneficiaries": "c. 8,500 WTE staff serving a c. 530,000 east Lancashire catchment (Blackburn with Darwen, Burnley, Pendle, Hyndburn, Ribble Valley, Rossendale); c. 200,000 ED attendances/yr (Royal Blackburn ED + Burnley urgent care); c. 95,000 admissions/yr; integrated community workforce.",
        "legal_basis": "IAS 38 Intangible Assets · IFRIC 22 SaaS configuration/customisation costs (March 2021 agenda decision) · DHSC Group Accounting Manual 2024-25 ch.5 · NHS Act 2006 · Health and Care Act 2022 · NHSE Frontline Digitisation programme guidance",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£4.488M"},
            {"label": "Trust scale", "value": "Two-acute-site (Royal Blackburn + Burnley General) + community footprint (Pendle + Clitheroe); c. 8,500 WTE"},
            {"label": "EPR context", "value": "Cerner Millennium EPR via Lancashire & South Cumbria shared-tenancy programme — capitalised intangible drives IAS 38 amortisation"},
            {"label": "Asset base composition", "value": "Cerner EPR licences + implementation costs + radiology PACS + clinical software + internally-generated apps; 5-10yr UEL per IAS 38 / DHSC GAM ch.5"},
            {"label": "IFRIC 22 effect", "value": "March 2021 SaaS configuration/customisation agenda decision reshaped capitalisation boundary; some costs reclassified opex"},
            {"label": "Frontline Digitisation context", "value": "NHSE Frontline Digitisation funds EPR rollouts to 'core' standard by 2026 — ELHT receiving FD investment via L&SC ICS"},
            {"label": "Funding trajectory", "value": "2021-22 c. £3.5M → 2023-24 £4.1M → 2024-25 £4.488M — sustained intangible additions through Frontline Digitisation cycle"},
            {"label": "Delivery body", "value": "Trust IT + Digital programme office + Cerner + Lancashire & South Cumbria ICS shared-EPR programme + DHSC Frontline Digitisation funding"},
            {"label": "Policy owner", "value": "DHSC + NHSE Frontline Digitisation + NHSE Provider Finance + Lancashire and South Cumbria ICB"},
            {"label": "Evaluation evidence", "value": "NHSE Frontline Digitisation programme evaluation; NAO Digital Transformation in the NHS (HC 8, 2020); CQC RXR inspection; Trust ARA disclosure"},
            {"label": "Predecessor / successor", "value": "Predecessor: legacy standalone clinical systems · Successor: convergent Cerner EPR + integrated PACS + AI-clinical-decision modules amortising 2024-2030+"}
        ],
        "notes": "ELHT's amortisation profile reflects sustained capitalisation of the Cerner Millennium EPR rollout via the Lancashire & South Cumbria shared-tenancy programme — providing a single regional EPR backbone across multiple acute trusts and accelerating convergence within the L&SC ICS. Implementation labour, software licences and configuration costs flow through IAS 38 over typical 5-10 year UELs, with the IFRIC 22 March 2021 agenda decision having reshaped the capitalisation boundary and pushed some configuration cost to opex. NHSE's 2026 'core' EPR target keeps the trajectory upward; Frontline Digitisation investment continues to lift the trust's intangible-asset baseline.",
        "sources": [
            {"publisher": "East Lancashire Hospitals NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.elht.nhs.uk/about-us/our-publications"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/connecting-health-and-care-providers/frontline-digitisation/"},
            {"publisher": "National Audit Office", "title": "Digital transformation in the NHS (HC 8, 2020)", "url": "https://www.nao.org.uk/reports/the-use-of-digital-technology-in-the-nhs/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 5)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "ELHT provider profile (RXR)", "url": "https://www.cqc.org.uk/provider/RXR"}
        ],
        "related": ["East Lancashire Hospitals NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Frontline Digitisation Programme", "Amortisation — University Hospitals of Leicester NHS Trust", "Lancashire and South Cumbria Integrated Care Board"]
    },
    "Business rates — Chelsea and Westminster Hospital NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "Chelsea and Westminster Hospital NHS Foundation Trust"}],
        "description": "Chelsea and Westminster's £4.485M business-rates line covers National Non-Domestic Rates on the trust's two-site footprint — Chelsea and Westminster Hospital (Fulham Road) and West Middlesex University Hospital (Isleworth) — plus satellite outpatient sites. Rateable values reflect the Valuation Office Agency's 2023 revaluation cycle, with central-London Chelsea contributing a high RV per square metre. The Non-Domestic Rating (Multipliers and Private Finance) Act 2024 introduces split multipliers from 2026-27, with implications for major NHS sites.",
        "beneficiaries": "c. 6,500 WTE staff serving a c. 1.5M north-west and west London catchment (Kensington & Chelsea, Hammersmith & Fulham, Hounslow, Richmond, Westminster); c. 270,000 ED attendances/yr (Chelsea + West Mid combined); c. 100,000 admissions/yr; large maternity service.",
        "legal_basis": "Local Government Finance Act 1988 (Sch 6 — non-domestic rating) · Non-Domestic Rating (Multipliers and Private Finance) Act 2024 · Non-Domestic Rating Act 2023 · Valuation Office Agency 2023 revaluation · DHSC Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£4.485M"},
            {"label": "Trust scale", "value": "Two-site acute (Chelsea + Westminster Fulham Road + West Middlesex Isleworth) post-2015 acquisition; c. 6,500 WTE"},
            {"label": "Estate covered", "value": "Chelsea + Westminster Hospital (Fulham Road, SW10) + West Middlesex University Hospital (Isleworth) + satellite outpatient sites"},
            {"label": "Multiplier 2024-25", "value": "Standard 54.6p / Small business 49.9p; new NDRA 2024 split multipliers from 2026-27"},
            {"label": "Revaluation cycle", "value": "VOA 2023 revaluation (effective Apr 2023, AVD 1 Apr 2021) + transitional relief regime"},
            {"label": "2015 West Middlesex acquisition + RV driver", "value": "Sept 2015 acquisition extended rate base into Hounslow; central-London Fulham Road location drives high RV per m²"},
            {"label": "Funding trajectory", "value": "Pre-2015 single-site baseline; post-2015 consolidated; sustained 2024-25 £4.485M reflecting 2023 revaluation"},
            {"label": "Billing authorities", "value": "Royal Borough of Kensington and Chelsea (Fulham Road site) + London Borough of Hounslow (West Mid)"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + VOA assessment + RBKC + Hounslow billing authorities + DLUHC oversight"},
            {"label": "Policy owner", "value": "HM Treasury + DLUHC (NDR policy) + DHSC + NHSE Provider Finance + North West London ICB"},
            {"label": "Evaluation evidence", "value": "VOA rating list disclosure; NAO NHS estate review; CQC RQM inspection; Trust ARA disclosure"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2015 separate Chelsea + Westminster + West Mid baselines · Successor: post-2026-27 NDRA split-multiplier regime"}
        ],
        "notes": "Chelsea and Westminster acquired West Middlesex University Hospital NHS Trust in September 2015, consolidating a two-site footprint that crosses central-London (RBKC) and outer-London (Hounslow) billing-authority boundaries. The Fulham Road site drives a high rateable-value contribution per square metre relative to the Isleworth West Middlesex site. The VOA's 2023 revaluation (AVD 1 April 2021) sets the rateable-value baseline for the current list cycle. The Non-Domestic Rating (Multipliers and Private Finance) Act 2024 introduces split multipliers from 2026-27 with implications for major NHS estate; transitional-relief flows continue to shape the trajectory.",
        "sources": [
            {"publisher": "Chelsea and Westminster Hospital NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.chelwest.nhs.uk/about-us/publications"},
            {"publisher": "Valuation Office Agency", "title": "2023 Rating list and revaluation", "url": "https://www.gov.uk/government/organisations/valuation-office-agency"},
            {"publisher": "Department for Levelling Up, Housing and Communities", "title": "Non-Domestic Rating Act 2023 and Multipliers and Private Finance Act 2024 — implementation guidance", "url": "https://www.gov.uk/government/collections/business-rates"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Chelsea and Westminster provider profile (RQM)", "url": "https://www.cqc.org.uk/provider/RQM"}
        ],
        "related": ["Chelsea and Westminster Hospital NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Business rates — University Hospitals Sussex NHS Foundation Trust", "Valuation Office Agency", "Non-Domestic Rating"]
    },
    "PFI / LIFT charges — Somerset NHS Foundation Trust": {
        "aliases": [{"name": "PFI / LIFT charges", "parent": "Somerset NHS Foundation Trust"}],
        "description": "Somerset NHS FT's £4.476M PFI / LIFT charge covers residual unitary-charge components and LIFT primary-care/community-clinic estate pass-through across Musgrove Park (Taunton) + Yeovil District + integrated Somerset community estate. The trust formed Apr 2020 by Taunton & Somerset + Somerset Partnership merger, then acquired Yeovil District in Apr 2023 — a multi-stage integration whose LIFT-line composition reflects mental-health + community-clinic + acute-satellite property concessions.",
        "beneficiaries": "c. 12,000 WTE staff serving a c. 580,000 Somerset catchment (Taunton, Yeovil, Bridgwater, Wellington, Chard); c. 150,000 ED attendances/yr (Musgrove Park + Yeovil District EDs combined); c. 70,000 admissions/yr; integrated mental-health + community workforce across Somerset.",
        "legal_basis": "IFRIC 12 Service Concession Arrangements · IFRS 16 Leases (post-2022 transition for service-concession components) · DHSC Group Accounting Manual 2024-25 ch.7 · Private Finance Initiative guidance (HM Treasury) · NHS LIFT framework (2001-) · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "PFI / LIFT charges 2024-25", "value": "£4.476M"},
            {"label": "Trust scale", "value": "Multi-modal trust: Musgrove Park (Taunton) + Yeovil District acute + Somerset mental health + community estate; c. 12,000 WTE"},
            {"label": "Merger lineage", "value": "Apr 2020 merger Taunton & Somerset NHS FT + Somerset Partnership NHS FT (MH + community); Apr 2023 acquisition Yeovil District NHS FT"},
            {"label": "LIFT-estate footprint", "value": "Somerset LIFT primary-care + community-clinic concessions inherited from Somerset Partnership; standard 25-30 year concessions"},
            {"label": "Yeovil PFI legacy", "value": "Yeovil District acquisition Apr 2023 brought legacy PFI / lease arrangements into trust scope"},
            {"label": "Indexation mechanism", "value": "RPI-linked annual uplift on indexed LIFT components per concession agreements"},
            {"label": "Unitary-charge composition", "value": "Senior debt service + lifecycle hard-FM + indexed soft-FM (cleaning, catering, portering) for relevant LIFT estate"},
            {"label": "Funding trajectory", "value": "Pre-2020 separate baselines; post-merger consolidated 2020-21; Yeovil acquisition Apr 2023 lift; 2024-25 £4.476M"},
            {"label": "Delivery body", "value": "LIFT SPVs (Somerset LIFT Co + sub-concessions) + Trust E&F + DHSC Hand-Back unit oversight"},
            {"label": "Policy owner", "value": "DHSC + HM Treasury PFI / LIFT guidance + NHSE Provider Finance + Somerset ICB + IPA PFI Hand-Back unit"},
            {"label": "Evaluation evidence", "value": "NAO PFI hand-back report 2020; NHSE LIFT oversight; Trust ARA disclosure; CQC RH5 inspection; merger benefits-realisation review"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2020 separate Taunton + Somerset Partnership + Yeovil PFI/LIFT baselines · Successor: 2030s LIFT hand-back + post-PFI direct-trust ownership"}
        ],
        "notes": "Somerset NHS FT is one of England's most integrated provider trusts following the April 2020 merger of Taunton & Somerset NHS FT with Somerset Partnership NHS FT (mental health + community) and the April 2023 acquisition of Yeovil District NHS FT — creating a multi-modal acute + mental-health + community footprint. The LIFT-line composition reflects this integration: Somerset Partnership brought LIFT primary-care and community-clinic concessions inherited under the 2001 LIFT framework, while Yeovil District added legacy PFI/lease arrangements into trust scope. RPI indexation continues to lift soft-FM components; IPA/HMT PFI Hand-Back unit engagement applies to residual concessions.",
        "sources": [
            {"publisher": "Somerset NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.somersetft.nhs.uk/about-us/publications/"},
            {"publisher": "National Audit Office", "title": "Managing PFI assets and services as contracts end (HC 632, 2020)", "url": "https://www.nao.org.uk/reports/managing-pfi-assets-and-services-as-contracts-end/"},
            {"publisher": "NHS England", "title": "LIFT framework and primary-care estate guidance", "url": "https://www.england.nhs.uk/estates/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 7)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Somerset NHS FT provider profile (RH5)", "url": "https://www.cqc.org.uk/provider/RH5"}
        ],
        "related": ["Somerset NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "PFI / LIFT charges — Sherwood Forest Hospitals NHS Foundation Trust", "PFI / LIFT charges — Worcestershire Acute Hospitals NHS Trust", "Infrastructure and Projects Authority"]
    },
    "General supplies & services — Salisbury NHS Foundation Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "Salisbury NHS Foundation Trust"}],
        "description": "Salisbury NHS FT's £4.441M general supplies & services line covers non-clinical consumables, linen, catering, hotel-services materials and minor expensed equipment at Salisbury District Hospital plus satellite outpatient sites. The trust hosts the Wessex Spinal Cord Injuries Centre, Wessex Genomics, Burns + Plastics + Cleft Lip & Palate, plus the Duke of Cornwall Spinal Treatment Centre — the regional tertiary-services concentration drives a non-clinical consumables baseline above peer single-site DGHs of similar bed count.",
        "beneficiaries": "c. 4,500 WTE staff serving a c. 270,000 south Wiltshire core catchment plus c. 3.5M tertiary catchment for Wessex spinal injuries, plastics, burns and genomics; c. 65,000 ED attendances/yr at Salisbury ED; c. 50,000 elective + day-case admissions/yr; nationally significant tertiary specialty footprint.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 2 Inventories · Procurement Act 2023 · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "General supplies & services 2024-25", "value": "£4.441M"},
            {"label": "Trust scale", "value": "Single acute site (Salisbury District Hospital, Odstock) + tertiary specialty footprint; c. 4,500 WTE"},
            {"label": "Tertiary specialties", "value": "Wessex Spinal Cord Injuries Centre + Burns + Plastics + Cleft Lip & Palate + Wessex Regional Genetics — drives specialised non-clinical consumables footprint"},
            {"label": "ED throughput", "value": "c. 65,000 attendances/yr — modest acute ED relative to tertiary specialty footprint"},
            {"label": "Procurement route", "value": "NHS Supply Chain national framework + trust-direct contracts + Bath, Swindon and Wiltshire ICS collaborative + tertiary-specialty specialist suppliers"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove cancellation-related re-stocking + agency-backfill consumable use"},
            {"label": "April 2025 NIC + CPI uplift", "value": "Apr 2025 employer-NIC step-up on supply-chain pass-through + sustained non-clinical CPI feed forward unit-cost pressure"},
            {"label": "Funding trajectory", "value": "2021-22 c. £3.5M → 2023-24 £4.0M → 2024-25 £4.441M — CPI + activity recovery + tertiary specialist consumables"},
            {"label": "Delivery body", "value": "Trust Procurement + NHS Supply Chain (DHSC ALB) + BSW ICS procurement collaborative + tertiary-specialty specialist suppliers"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Bath, Swindon and Wiltshire ICB + NHSE Specialised Commissioning"},
            {"label": "Evaluation evidence", "value": "Model Hospital benchmarks; NHSE Specialised Commissioning service spec for spinal injuries + plastics + burns; CQC RNZ inspection; Trust ARA disclosure"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-NHS Supply Chain framework (pre-2018) trust-direct procurement · Successor: BSW ICS collaborative + tertiary-specialist supplier consolidation"}
        ],
        "notes": "Salisbury NHS FT's general supplies & services baseline is structurally elevated by the trust's regional and national tertiary specialty concentration — Wessex Spinal Cord Injuries Centre, Burns + Plastics + Cleft Lip & Palate, plus Wessex Regional Genetics — which drives specialised non-clinical consumables (specialist-bed linen, surgical-prep materials, dressings, theatre-support items) above peer single-site DGHs of similar bed count. Industrial action 2023-24 layered cancellation-related re-stocking and agency-backfill on pandemic-recovery activity. The Procurement Act 2023 regime is reshaping framework call-off patterns. April 2025 NIC step-up on contractor pass-through and sustained CPI feed forward unit-cost pressure into 2025-26.",
        "sources": [
            {"publisher": "Salisbury NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.salisbury.nhs.uk/about-us/our-publications/"},
            {"publisher": "NHS Supply Chain", "title": "Annual Report 2023-24", "url": "https://www.supplychain.nhs.uk/about-us/our-publications/"},
            {"publisher": "NHS England", "title": "Specialised Commissioning service specifications (Spinal injuries + Plastics + Burns)", "url": "https://www.england.nhs.uk/commissioning/spec-services/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Salisbury NHS FT provider profile (RNZ)", "url": "https://www.cqc.org.uk/provider/RNZ"}
        ],
        "related": ["Salisbury NHS Foundation Trust", "Clinical Supplies & Drugs", "NHS Acute Trusts", "NHS Supply Chain", "General supplies & services — Liverpool University Hospitals NHS Foundation Trust", "NHS England"]
    },
    "Transport (business + patient) — Epsom and St Helier University Hospitals NHS Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "Epsom and St Helier University Hospitals NHS Trust"}],
        "description": "ESTH's £4.438M transport line covers business mileage (AfC Section 17 + HMRC AMAP), pool fleet under IFRS 16, contracted Non-Emergency Patient Transport Services and inter-site transfers across the trust's Epsom General + St Helier hospital footprint plus Sutton Health Campus and the planned Specialist Emergency Care Hospital (SECH) in Sutton. Inter-site clinical flows between two ageing single-DGH sites c. 12 miles apart sustain the transport baseline; the trust has chair-in-common arrangements with Kingston Hospital under SWL ICS planning.",
        "beneficiaries": "c. 5,500 WTE staff serving a c. 490,000 south-west London + east Surrey catchment (Sutton, Merton, Epsom & Ewell, Mole Valley, Wandsworth); c. 145,000 ED attendances/yr (St Helier + Epsom EDs combined); c. 65,000 admissions/yr; both sites RAAC-affected.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · IFRS 16 Leases (pool fleet) · NHS Act 2006 · Mental Health Act 1983 (s.135/136 conveyance) · NHSE Patient Transport Services Eligibility Framework 2022 · HMRC AMAP · NHS AfC Section 17",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£4.438M"},
            {"label": "Trust scale", "value": "Two-site DGH (St Helier + Epsom General) + Sutton Health Campus; c. 5,500 WTE"},
            {"label": "Inter-site corridor", "value": "St Helier (Sutton) to Epsom General c. 12 miles via A24 / A217 — sustains routine clinical + corporate inter-site travel"},
            {"label": "RAAC + NHP context", "value": "Both St Helier + Epsom on Sep 2023 HSSIB RAAC list; original NHP cohort with planned Specialist Emergency Care Hospital (SECH) in Sutton — Jan 2025 NHP Reset rephased delivery"},
            {"label": "Group-model context", "value": "Chair-in-common with Kingston Hospital NHS FT under SWL ICS group planning"},
            {"label": "PTS + mileage + IFRS 16", "value": "London Ambulance Service PTS + accredited NEPTS contractors via SWL ICS framework; AfC Section 17 / HMRC AMAP 45p/25p; IFRS 16 right-of-use pool fleet from 2022-23"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove ad-hoc inter-site cover transfers + locum mileage claims"},
            {"label": "Funding trajectory", "value": "2021-22 c. £3.5M → 2023-24 £4.0M → 2024-25 £4.438M — fuel CPI + RAAC mitigation churn + activity recovery"},
            {"label": "Delivery body", "value": "Trust E&F + Travel team + LAS PTS + accredited NEPTS contractors"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + South West London ICB + NHSE PTS policy"},
            {"label": "Evaluation evidence", "value": "NHSE NEPTS Eligibility Framework 2022 review; HSSIB RAAC report Sep 2023; NAO New Hospital Programme 2023; CQC RVR inspection"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-1999 separate Epsom + St Helier transport baselines · Successor: post-NHP SECH consolidated transport hub + SWL ICS shared-fleet pooling"}
        ],
        "notes": "ESTH operates two ageing single-DGH sites (St Helier and Epsom General) c. 12 miles apart, both on the September 2023 HSSIB RAAC list — inter-site clinical transfers and decant-related transport demand sit above peer single-site DGHs. The trust's place in the original NHP cohort, with the planned Specialist Emergency Care Hospital in Sutton intended to consolidate emergency, women's and children's services, was rephased at the January 2025 NHP Reset. The chair-in-common with Kingston Hospital NHS FT under SWL ICS group planning shapes shared-back-office transport strategy. April 2025 NIC step-up affects PTS-contractor pass-through.",
        "sources": [
            {"publisher": "Epsom and St Helier University Hospitals NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.epsom-sthelier.nhs.uk/annual-reports"},
            {"publisher": "NHS England", "title": "Non-Emergency Patient Transport Services Eligibility Framework 2022", "url": "https://www.england.nhs.uk/long-read/non-emergency-patient-transport-services-eligibility-framework/"},
            {"publisher": "Health Services Safety Investigations Body", "title": "Reinforced autoclaved aerated concrete (RAAC) in NHS hospitals", "url": "https://www.hssib.org.uk/"},
            {"publisher": "Department of Health and Social Care", "title": "New Hospital Programme — Plan for Implementation (Jan 2025 Reset)", "url": "https://www.gov.uk/government/publications/new-hospital-programme-plan-for-implementation"},
            {"publisher": "Care Quality Commission", "title": "ESTH provider profile (RVR)", "url": "https://www.cqc.org.uk/provider/RVR"}
        ],
        "related": ["Epsom and St Helier University Hospitals NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Transport (business + patient) — Imperial College Healthcare NHS Trust", "New Hospital Programme", "Kingston Hospital NHS Foundation Trust"]
    },
    "Lease expenditure — Countess of Chester Hospital NHS Foundation Trust": {
        "aliases": [{"name": "Lease expenditure", "parent": "Countess of Chester Hospital NHS Foundation Trust"}],
        "description": "Countess of Chester Hospital's £4.437M lease line covers IFRS 16 right-of-use depreciation and interest plus residual operating-lease P&L across leased clinic outposts, modular wards, decant accommodation, office space and equipment leases (imaging, dialysis, pool fleet) at the Countess of Chester acute site plus satellite community premises. The trust has been under sustained operational and reputational pressure following the Lucy Letby case — the Thirlwall Inquiry findings shape governance and capacity planning, with leased modular capacity supporting interim service provision.",
        "beneficiaries": "c. 4,500 WTE staff serving a c. 270,000 west Cheshire catchment (Chester, Ellesmere Port, Neston) plus a small share of Welsh cross-border activity; c. 90,000 ED attendances/yr at Countess of Chester ED; c. 45,000 admissions/yr; large maternity unit.",
        "legal_basis": "IFRS 16 Leases · DHSC Group Accounting Manual 2024-25 ch.7 · Landlord and Tenant Act 1954 · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "Lease expenditure 2024-25", "value": "£4.437M"},
            {"label": "Trust scale", "value": "Single acute site (Countess of Chester Hospital, Liverpool Road) + satellite community premises; c. 4,500 WTE"},
            {"label": "IFRS 16 transition (2022-23)", "value": "Operating leases brought on-balance-sheet 2022-23 — lifted lease-line presentation post-transition"},
            {"label": "Lease profile", "value": "Leased clinic outposts + modular wards + decant accommodation + leased office space + equipment leases (imaging modalities, dialysis, pool fleet)"},
            {"label": "Thirlwall Inquiry context", "value": "Trust under sustained governance scrutiny following Lucy Letby case; Thirlwall Inquiry hearings 2024-25 — leased modular capacity supports interim service provision"},
            {"label": "Industrial action 2023-24", "value": "Strike days drove modular ward + temporary capacity demand; lease-base churn"},
            {"label": "Cross-border catchment", "value": "Small share of Welsh cross-border activity drives some specialist equipment leasing"},
            {"label": "Funding trajectory", "value": "2021-22 c. £2.5M (pre-IFRS 16) → 2022-23 step-up post-IFRS 16 → 2024-25 £4.437M — transition + interim modular capacity"},
            {"label": "Delivery body", "value": "Trust E&F + Finance + Procurement + NHS Property Services + commercial landlords"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Cheshire and Merseyside ICB"},
            {"label": "Evaluation evidence", "value": "Thirlwall Inquiry findings; NHSE governance reviews; CQC RJR inspection; Trust ARA disclosure"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-IFRS 16 (2022) operating-lease P&L baseline · Successor: post-Thirlwall service redesign + Cheshire & Merseyside ICS estate consolidation"}
        ],
        "notes": "Countess of Chester Hospital NHS FT operates as a single-site DGH in west Cheshire, with the lease line shaped by IFRS 16 right-of-use depreciation on leased clinic outposts, modular wards, decant accommodation, office space and equipment leases. The trust has been under sustained operational and reputational pressure following the Lucy Letby case, with the Thirlwall Inquiry hearings through 2024-25 driving governance and capacity-planning reviews — leased modular capacity has supported interim service provision. The April 2022 IFRS 16 transition stepped operating leases on-balance-sheet, lifting the line's presentation. Industrial action 2023-24 drove modular ward and temporary capacity demand. Cheshire & Merseyside ICS estate consolidation is the medium-term lever.",
        "sources": [
            {"publisher": "Countess of Chester Hospital NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.coch.nhs.uk/our-publications/"},
            {"publisher": "Thirlwall Inquiry", "title": "Public Inquiry into events at the Countess of Chester Hospital", "url": "https://thirlwall.public-inquiry.uk/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 7)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Countess of Chester provider profile (RJR)", "url": "https://www.cqc.org.uk/provider/RJR"},
            {"publisher": "NHS Property Services", "title": "NHSPS leased estate framework", "url": "https://www.property.nhs.uk/about-us/"}
        ],
        "related": ["Countess of Chester Hospital NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Lease expenditure — University Hospitals of Leicester NHS Trust", "NHS Property Services", "Cheshire and Merseyside Integrated Care Board"]
    },
    "Amortisation — University Hospital Southampton NHS Foundation Trust": {
        "aliases": [{"name": "Amortisation", "parent": "University Hospital Southampton NHS Foundation Trust"}],
        "description": "UHS's £4.435M amortisation line covers IAS 38 write-down of capitalised intangibles — software licences, the trust's clinical-systems portfolio, capitalised configuration, radiology PACS, internally-generated apps and acquired digital systems — across the Southampton General + Princess Anne + Royal South Hants estate. UHS is a major teaching/tertiary trust hosting Wessex Cardiothoracic, Neurological, regional cancer + tertiary paediatric services, with Frontline Digitisation funding sustaining intangible additions.",
        "beneficiaries": "c. 12,500 WTE staff serving a c. 670,000 Southampton + south Hampshire core catchment plus c. 3.5M Wessex tertiary catchment for cardiothoracic, neurosciences, paediatric tertiary, complex cancer and trauma; c. 165,000 ED attendances/yr at Southampton General ED — Major Trauma Centre; c. 150,000 admissions/yr.",
        "legal_basis": "IAS 38 Intangible Assets · IFRIC 22 SaaS configuration/customisation costs (March 2021 agenda decision) · DHSC Group Accounting Manual 2024-25 ch.5 · NHS Act 2006 · Health and Care Act 2022 · NHSE Frontline Digitisation programme guidance",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£4.435M"},
            {"label": "Trust scale", "value": "Multi-site teaching/tertiary (Southampton General + Princess Anne + Royal South Hants); c. 12,500 WTE"},
            {"label": "Major Trauma Centre", "value": "Southampton General = Wessex MTC — drives high-spec clinical-systems intangible-asset baseline"},
            {"label": "Tertiary specialties", "value": "Wessex Cardiothoracic + Neurosciences + Paediatric tertiary + Complex Cancer — drives specialist clinical-software intangible-asset baseline"},
            {"label": "Asset base composition", "value": "Clinical-systems licences + capitalised configuration + radiology PACS + internally-generated clinical apps + research-software; 5-10yr UEL per IAS 38 / DHSC GAM ch.5"},
            {"label": "IFRIC 22 effect", "value": "March 2021 SaaS configuration/customisation agenda decision reshaped capitalisation boundary; some costs reclassified opex"},
            {"label": "Frontline Digitisation context", "value": "NHSE Frontline Digitisation funds EPR rollouts to 'core' standard by 2026 — UHS receiving FD investment via Hampshire & Isle of Wight ICS"},
            {"label": "Funding trajectory", "value": "2021-22 c. £3.5M → 2023-24 £4.0M → 2024-25 £4.435M — sustained intangible-asset additions through Frontline Digitisation cycle"},
            {"label": "Delivery body", "value": "Trust IT + Digital programme office + clinical-systems vendors + DHSC Frontline Digitisation funding + Hampshire & IoW ICS digital pillar"},
            {"label": "Policy owner", "value": "DHSC + NHSE Frontline Digitisation + NHSE Provider Finance + Hampshire and Isle of Wight ICB + NHSE Specialised Commissioning"},
            {"label": "Evaluation evidence", "value": "NHSE Frontline Digitisation programme evaluation; NAO Digital Transformation in the NHS (HC 8, 2020); CQC RHM inspection; Trust ARA disclosure"},
            {"label": "Predecessor / successor", "value": "Predecessor: legacy standalone clinical systems · Successor: convergent EPR + integrated PACS + AI-clinical-decision modules amortising 2024-2030+"}
        ],
        "notes": "UHS's amortisation reflects sustained capitalisation of clinical-systems software, PACS and Frontline Digitisation investment across a major teaching/tertiary trust hosting Wessex MTC plus regional cardiothoracic, neurosciences, paediatric tertiary and complex-cancer services. Implementation labour, software licences and configuration costs flow through IAS 38 over typical 5-10 year UELs, with the IFRIC 22 March 2021 agenda decision reshaping the capitalisation boundary and pushing some configuration cost to opex. NHSE's 2026 'core' EPR target keeps the trajectory upward; UHS receives FD funding via the Hampshire & Isle of Wight ICS digital pillar.",
        "sources": [
            {"publisher": "University Hospital Southampton NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.uhs.nhs.uk/about/our-publications/annual-report"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/connecting-health-and-care-providers/frontline-digitisation/"},
            {"publisher": "National Audit Office", "title": "Digital transformation in the NHS (HC 8, 2020)", "url": "https://www.nao.org.uk/reports/the-use-of-digital-technology-in-the-nhs/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 5)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "UHS provider profile (RHM)", "url": "https://www.cqc.org.uk/provider/RHM"}
        ],
        "related": ["University Hospital Southampton NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Frontline Digitisation Programme", "Amortisation — University Hospitals of Leicester NHS Trust", "Hampshire and Isle of Wight Integrated Care Board"]
    },
    "Amortisation — Wye Valley NHS Trust": {
        "aliases": [{"name": "Amortisation", "parent": "Wye Valley NHS Trust"}],
        "description": "Wye Valley's £4.382M amortisation line covers IAS 38 write-down of capitalised intangibles — software licences, EPR/clinical-systems configuration, radiology PACS, internally-generated apps and acquired digital systems — at Hereford County Hospital plus integrated Herefordshire community services. The trust completed acquisition by South Warwickshire NHS FT in April 2024 to form South Warwickshire University NHS FT — bringing intangible-asset accounting into a group-model boundary while 2024-25 amortisation continues to flow through the trust entity.",
        "beneficiaries": "c. 3,000 WTE staff serving a c. 190,000 Herefordshire catchment plus integrated community services across the county; c. 70,000 ED attendances/yr at Hereford County ED; c. 30,000 admissions/yr; integrated community workforce (district nursing, community paediatric, sexual-health, school-nursing).",
        "legal_basis": "IAS 38 Intangible Assets · IFRIC 22 SaaS configuration/customisation costs (March 2021 agenda decision) · DHSC Group Accounting Manual 2024-25 ch.5 · NHS Act 2006 · Health and Care Act 2022 · NHSE Frontline Digitisation programme guidance",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£4.382M"},
            {"label": "Trust scale", "value": "Single acute site (Hereford County Hospital) + integrated Herefordshire community services; c. 3,000 WTE"},
            {"label": "South Warwickshire merger", "value": "Apr 2024 acquisition completion → unified South Warwickshire University NHS FT; intangible-asset boundary entering group-model integration"},
            {"label": "Asset base composition", "value": "Clinical-systems licences + capitalised configuration + radiology PACS + internally-generated clinical apps; 5-10yr UEL per IAS 38 / DHSC GAM ch.5"},
            {"label": "IFRIC 22 effect", "value": "March 2021 SaaS configuration/customisation agenda decision reshaped capitalisation boundary; some costs reclassified opex"},
            {"label": "Frontline Digitisation context", "value": "NHSE Frontline Digitisation funds EPR rollouts to 'core' standard by 2026 — Wye Valley receiving FD investment within H&W ICS"},
            {"label": "Hereford PFI legacy", "value": "Hereford Hospital PFI 1998-signed, expiring c. 2032 — IT capitalisation interaction with PFI replacement-cycle assets"},
            {"label": "Funding trajectory", "value": "2021-22 c. £3.5M → 2023-24 £4.0M → 2024-25 £4.382M — sustained intangible additions through Frontline Digitisation cycle"},
            {"label": "Delivery body", "value": "Trust IT + Digital programme office + clinical-systems vendors + DHSC Frontline Digitisation funding + (post-merger) SWUFT Group digital functions"},
            {"label": "Policy owner", "value": "DHSC + NHSE Frontline Digitisation + NHSE Provider Finance + Herefordshire & Worcestershire ICB + Coventry & Warwickshire ICB (post-merger)"},
            {"label": "Evaluation evidence", "value": "NHSE Frontline Digitisation programme evaluation; NAO Digital Transformation in the NHS (HC 8, 2020); CQC RLQ inspection; SWUFT merger transaction business case"},
            {"label": "Predecessor / successor", "value": "Predecessor: legacy standalone clinical systems · Successor: post-merger SWUFT Group digital convergence + Frontline Digitisation EPR rollout amortising 2024-2030+"}
        ],
        "notes": "Wye Valley's amortisation reflects sustained capitalisation of clinical-systems software, PACS and Frontline Digitisation investment, with the April 2024 acquisition by South Warwickshire NHS FT (forming South Warwickshire University NHS FT) bringing the intangible-asset accounting boundary into group-model integration territory. Legacy 2024-25 amortisation continues to flow through the Wye Valley entity until full integration. The Hereford Hospital PFI (1998-signed, expiring c. 2032) interacts with IT capitalisation cycles via PFI replacement-cycle assets. NHSE's 2026 'core' EPR target keeps the trajectory upward. The IFRIC 22 March 2021 agenda decision reshaped the capitalisation boundary; group-model digital convergence under SWUFT shapes medium-term trajectory.",
        "sources": [
            {"publisher": "Wye Valley NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.wyevalley.nhs.uk/about-us/key-publications/annual-report.aspx"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/connecting-health-and-care-providers/frontline-digitisation/"},
            {"publisher": "National Audit Office", "title": "Digital transformation in the NHS (HC 8, 2020)", "url": "https://www.nao.org.uk/reports/the-use-of-digital-technology-in-the-nhs/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 5)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Wye Valley NHS Trust provider profile (RLQ)", "url": "https://www.cqc.org.uk/provider/RLQ"}
        ],
        "related": ["Wye Valley NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Frontline Digitisation Programme", "Amortisation — University Hospitals of Leicester NHS Trust", "South Warwickshire NHS Foundation Trust"]
    },
    "Establishment costs — University Hospitals Dorset NHS Foundation Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "University Hospitals Dorset NHS Foundation Trust"}],
        "description": "UHD's £4.366M establishment line covers postage, telephony, print, recruitment-advertising, training, conferences, subscriptions and legal & professional fees across the Royal Bournemouth + Poole + Christchurch hospital footprint. Formed October 2020 by merger of Royal Bournemouth & Christchurch Hospitals NHS FT with Poole Hospital NHS FT, UHD is in active service-reconfiguration ('Transforming Dorset' / NHP cohort) with planned consolidation of major emergency, planned and women's & children's services onto specialist sites — sustaining programme-management overhead.",
        "beneficiaries": "c. 9,000 WTE staff serving a c. 670,000 east Dorset + Hampshire-borders catchment (Bournemouth, Poole, Christchurch, Purbeck, East Dorset); c. 200,000 ED attendances/yr (Royal Bournemouth + Poole EDs combined); c. 100,000 admissions/yr; large maternity unit + tertiary cardiac.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25 · Public Contracts Regulations 2015 / Procurement Act 2023",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£4.366M"},
            {"label": "Trust scale", "value": "Three-site acute (Royal Bournemouth + Poole + Christchurch) post-Oct 2020 merger; c. 9,000 WTE"},
            {"label": "Composition", "value": "Postage + telephony + print + recruitment-advertising + training + conferences + subscriptions + legal & professional fees"},
            {"label": "Merger context", "value": "UHD formed Oct 2020 by merger of Royal Bournemouth & Christchurch Hospitals NHS FT + Poole Hospital NHS FT — sustained merger-integration professional fees"},
            {"label": "Transforming Dorset / NHP context + Reset", "value": "Active service-reconfiguration with emergency, planned and women's/children's consolidation; original NHP cohort; Jan 2025 NHP Reset rephased delivery — sustained reconfiguration consultancy + advertising fees"},
            {"label": "Industrial action 2023-24", "value": "44 days junior-doctor + 10 days consultant strikes drove agency-engagement + recruitment-advertising professional fees"},
            {"label": "April 2025 NIC + CPI", "value": "Apr 2025 NIC step-up raises forward professional-fee + recruitment-retainer cost; CPI on print/post/conference inputs"},
            {"label": "Funding trajectory", "value": "Post-Oct 2020 merger consolidated; 2023-24 c. £4.0M → 2024-25 £4.366M — sustained reconfiguration overhead + CPI"},
            {"label": "Delivery body", "value": "Trust Corporate Services + HR + Finance + IT + Communications + external counsel + reconfiguration-programme office"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Dorset ICB + New Hospital Programme + IPA"},
            {"label": "Evaluation evidence", "value": "NAO New Hospital Programme 2023; CQC RDZ inspection; merger benefits-realisation review; Trust ARA disclosure"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-Oct 2020 separate Royal Bournemouth & Christchurch + Poole baselines · Successor: post-NHP-Reset reconfigured corporate-services footprint"}
        ],
        "notes": "UHD was formed in October 2020 by merger of Royal Bournemouth & Christchurch Hospitals NHS FT with Poole Hospital NHS FT, and is in active service-reconfiguration under the 'Transforming Dorset' programme (within the original New Hospital Programme cohort) with planned consolidation of major emergency, planned and women's & children's services onto specialist sites. The January 2025 NHP Reset rephased delivery, sustaining programme-management consultancy, reconfiguration-related professional fees and recruitment-advertising spend on hard-to-fill roles. Industrial action 2023-24 lifted advertising and agency-engagement fees. April 2025 NIC step-up and CPI on print/post/conference inputs feed forward; Dorset ICB shared corporate-services pooling is the medium-term lever.",
        "sources": [
            {"publisher": "University Hospitals Dorset NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.uhd.nhs.uk/our-publications"},
            {"publisher": "National Audit Office", "title": "Progress with the New Hospital Programme (HC 1662, 2023)", "url": "https://www.nao.org.uk/reports/the-new-hospital-programme/"},
            {"publisher": "Department of Health and Social Care", "title": "New Hospital Programme — Plan for Implementation (Jan 2025 Reset)", "url": "https://www.gov.uk/government/publications/new-hospital-programme-plan-for-implementation"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "UHD provider profile (RDZ)", "url": "https://www.cqc.org.uk/provider/RDZ"}
        ],
        "related": ["University Hospitals Dorset NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Establishment costs — Wye Valley NHS Trust", "New Hospital Programme", "Dorset Integrated Care Board"]
    },
    "Business rates — University Hospitals Coventry And Warwickshire NHS Trust": {
        "aliases": [{"name": "Business rates", "parent": "University Hospitals Coventry And Warwickshire NHS Trust"}],
        "description": "UHCW's £4.331M business-rates line covers National Non-Domestic Rates on the trust's two-site footprint — University Hospital Coventry (Walsgrave) and the Hospital of St Cross (Rugby) — plus satellite outpatient facilities. Rateable values reflect the Valuation Office Agency's 2023 revaluation cycle, with the Coventry PFI build (signed 2002, opened 2006) contributing a substantial RV on the modern Walsgrave site. The Non-Domestic Rating (Multipliers and Private Finance) Act 2024 introduces split multipliers from 2026-27 with implications for major NHS sites.",
        "beneficiaries": "c. 11,000 WTE staff serving a c. 1.0M Coventry + Warwickshire core catchment plus regional tertiary referrals (renal, cardiac, neurosciences) across the West Midlands; c. 200,000 ED attendances/yr at UHCW ED; c. 130,000 admissions/yr; UHCW = West Midlands tertiary trauma centre (collaborates with QEHB MTC).",
        "legal_basis": "Local Government Finance Act 1988 (Sch 6 — non-domestic rating) · Non-Domestic Rating (Multipliers and Private Finance) Act 2024 · Non-Domestic Rating Act 2023 · Valuation Office Agency 2023 revaluation · DHSC Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£4.331M"},
            {"label": "Trust scale", "value": "Two-site acute (University Hospital Coventry, Walsgrave + Hospital of St Cross, Rugby); c. 11,000 WTE"},
            {"label": "Estate covered", "value": "University Hospital Coventry (Walsgrave, PFI-built 2006) + Hospital of St Cross (Rugby) + satellite outpatient facilities"},
            {"label": "Multiplier 2024-25", "value": "Standard 54.6p / Small business 49.9p; new NDRA 2024 split multipliers from 2026-27"},
            {"label": "Revaluation cycle", "value": "VOA 2023 revaluation (effective Apr 2023, AVD 1 Apr 2021) + transitional relief regime"},
            {"label": "Coventry PFI + tertiary specialty driver", "value": "University Hospital Coventry PFI signed 2002, opened 2006 — modern build with substantial RV baseline; regional renal + cardiac + neurosciences drive specialist-equipment plant adjustments"},
            {"label": "Funding trajectory", "value": "Post-2006 PFI opening baseline; sustained 2024-25 £4.331M reflecting 2023 revaluation"},
            {"label": "Billing authorities", "value": "Coventry City Council (Walsgrave site) + Rugby Borough Council (St Cross)"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + VOA assessment + Coventry CC + Rugby BC billing authorities + DLUHC oversight"},
            {"label": "Policy owner", "value": "HM Treasury + DLUHC (NDR policy) + DHSC + NHSE Provider Finance + Coventry & Warwickshire ICB"},
            {"label": "Evaluation evidence", "value": "VOA rating list disclosure; NAO PFI hand-back report 2020; CQC RKB inspection; Trust ARA disclosure"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2006 Walsgrave Hospital pre-PFI rate baseline · Successor: post-2026-27 NDRA split-multiplier regime + 2030s PFI hand-back"}
        ],
        "notes": "UHCW operates University Hospital Coventry (Walsgrave) under one of the UK's larger NHS PFI deals — signed 2002, opened 2006 — with the modern build contributing a substantial rateable-value baseline post-2006. The Hospital of St Cross in Rugby falls within Rugby Borough Council's billing area, separate from Coventry CC for Walsgrave. The Valuation Office Agency's 2023 revaluation (AVD 1 April 2021) sets the rateable-value baseline for the current list cycle, with NHS trusts subject to the standard non-domestic rating multiplier. The Non-Domestic Rating (Multipliers and Private Finance) Act 2024 introduces split multipliers from 2026-27 with implications for the Walsgrave PFI estate; PFI hand-back planning (2030s expiry window) is a parallel medium-term consideration.",
        "sources": [
            {"publisher": "University Hospitals Coventry and Warwickshire NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.uhcw.nhs.uk/about-us/our-publications"},
            {"publisher": "Valuation Office Agency", "title": "2023 Rating list and revaluation", "url": "https://www.gov.uk/government/organisations/valuation-office-agency"},
            {"publisher": "Department for Levelling Up, Housing and Communities", "title": "Non-Domestic Rating Act 2023 and Multipliers and Private Finance Act 2024 — implementation guidance", "url": "https://www.gov.uk/government/collections/business-rates"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "UHCW provider profile (RKB)", "url": "https://www.cqc.org.uk/provider/RKB"}
        ],
        "related": ["University Hospitals Coventry And Warwickshire NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Business rates — University Hospitals Sussex NHS Foundation Trust", "Valuation Office Agency", "Non-Domestic Rating"]
    },
    "General supplies & services — West Suffolk NHS Foundation Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "West Suffolk NHS Foundation Trust"}],
        "description": "West Suffolk NHS FT's £4.302M general supplies & services line covers non-clinical consumables, linen, catering, hotel-services materials and minor expensed equipment at the Bury St Edmunds DGH plus integrated community estate. The trust is on the September 2023 HSSIB RAAC list (27 trusts) where reinforced autoclaved aerated concrete planks have driven structural mitigation and ongoing decant works — adding decant-related re-stocking and modular-ward consumables on top of the baseline DGH demand profile.",
        "beneficiaries": "c. 4,500 WTE staff serving a c. 280,000 west Suffolk catchment (Bury St Edmunds, Newmarket, Haverhill, Sudbury); c. 75,000 ED attendances/yr at West Suffolk Hospital ED; c. 35,000 admissions/yr; large maternity unit + community footprint extending into rural west Suffolk.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 2 Inventories · Procurement Act 2023 · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "General supplies & services 2024-25", "value": "£4.302M"},
            {"label": "Trust scale", "value": "Single-site DGH (West Suffolk Hospital, Bury St Edmunds) + integrated community footprint; c. 4,500 WTE"},
            {"label": "RAAC + NHP context + mitigation effect", "value": "West Suffolk Hospital on Sep 2023 HSSIB RAAC list (27 trusts); original NHP cohort; Jan 2025 NHP Reset deferred new build; RAAC remediation + decant works drive incremental modular-ward consumables + re-stocking churn"},
            {"label": "ED throughput", "value": "c. 75,000 attendances/yr"},
            {"label": "Procurement route", "value": "NHS Supply Chain national framework + trust-direct contracts + Suffolk & North East Essex ICS collaborative"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove cancellation-related re-stocking + agency-backfill consumable use"},
            {"label": "April 2025 NIC + CPI uplift", "value": "Apr 2025 employer-NIC step-up on supply-chain pass-through + sustained non-clinical CPI"},
            {"label": "Funding trajectory", "value": "2021-22 c. £3.5M → 2023-24 £3.9M → 2024-25 £4.302M — RAAC decant + CPI + activity recovery"},
            {"label": "Delivery body", "value": "Trust Procurement + NHS Supply Chain (DHSC ALB) + SNEE ICS procurement collaborative"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Suffolk & North East Essex ICB + New Hospital Programme"},
            {"label": "Evaluation evidence", "value": "Model Hospital benchmarks; HSSIB RAAC report Sep 2023; CQC RGR inspection; Trust ARA disclosure"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-RAAC mitigation baseline · Successor: post-NHP-Reset rebuild + SNEE ICS collaborative procurement scaling"}
        ],
        "notes": "West Suffolk NHS FT's general supplies & services baseline reflects single-DGH demand layered on RAAC mitigation pressure — the Sep 2023 HSSIB listing (27-trust cohort) drove structural remediation and decant works that lift modular-ward consumables and re-stocking churn above pre-RAAC baseline. The original New Hospital Programme commitment to a replacement build was deferred under the January 2025 NHP Reset into the next financing window, sustaining the existing site as the operational baseline. Industrial action 2023-24 layered cancellation-related re-stocking and agency-backfill consumable use. April 2025 NIC step-up on contractor pass-through and sustained CPI feed forward unit-cost pressure into 2025-26.",
        "sources": [
            {"publisher": "West Suffolk NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.wsh.nhs.uk/About-us/Publications.aspx"},
            {"publisher": "Health Services Safety Investigations Body", "title": "Reinforced autoclaved aerated concrete (RAAC) in NHS hospitals", "url": "https://www.hssib.org.uk/"},
            {"publisher": "NHS Supply Chain", "title": "Annual Report 2023-24", "url": "https://www.supplychain.nhs.uk/about-us/our-publications/"},
            {"publisher": "Department of Health and Social Care", "title": "New Hospital Programme — Plan for Implementation (Jan 2025 Reset)", "url": "https://www.gov.uk/government/publications/new-hospital-programme-plan-for-implementation"},
            {"publisher": "Care Quality Commission", "title": "West Suffolk provider profile (RGR)", "url": "https://www.cqc.org.uk/provider/RGR"}
        ],
        "related": ["West Suffolk NHS Foundation Trust", "Clinical Supplies & Drugs", "NHS Acute Trusts", "NHS Supply Chain", "General supplies & services — Liverpool University Hospitals NHS Foundation Trust", "New Hospital Programme"]
    },
    "General supplies & services — Kettering General Hospital NHS Foundation Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "Kettering General Hospital NHS Foundation Trust"}],
        "description": "Kettering General Hospital NHS FT's £4.277M general supplies & services line covers non-clinical consumables, linen, catering, hotel-services materials and minor expensed equipment at Kettering General Hospital plus the trust's outpatient and community-clinic outposts across north Northamptonshire. The trust is part of the University Hospitals of Northamptonshire group with Northampton General (chair-in-common since 2021), and is in the original New Hospital Programme cohort with rebuild deferred at the January 2025 NHP Reset.",
        "beneficiaries": "c. 4,500 WTE staff serving a c. 360,000 north Northamptonshire catchment (Kettering, Corby, Wellingborough, Rushden); c. 90,000 ED attendances/yr; c. 50,000 admissions/yr; large maternity unit + Foundation Group functions shared with Northampton General.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 2 Inventories · Procurement Act 2023 · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "General supplies & services 2024-25", "value": "£4.277M"},
            {"label": "Trust scale", "value": "Single-site DGH (Kettering General Hospital) + outpatient and community-clinic outposts; c. 4,500 WTE"},
            {"label": "Group-model context", "value": "University Hospitals of Northamptonshire group with Northampton General — chair-in-common since 2021; shared corporate + procurement functions developing"},
            {"label": "ED throughput + procurement", "value": "c. 90,000 attendances/yr; NHS Supply Chain framework + trust-direct contracts + UHN Group joint procurement + Northants ICS collaborative"},
            {"label": "NHP context", "value": "Original NHP cohort; Jan 2025 NHP Reset deferred new build — existing site procurement baseline preserved"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove cancellation-related re-stocking + agency-backfill consumable use"},
            {"label": "April 2025 NIC + CPI uplift", "value": "Apr 2025 employer-NIC step-up on supply-chain pass-through + sustained non-clinical CPI"},
            {"label": "Funding trajectory", "value": "2021-22 c. £3.4M → 2023-24 £3.9M → 2024-25 £4.277M — CPI + activity recovery + UHN group-procurement cycle"},
            {"label": "Delivery body", "value": "Trust Procurement + NHS Supply Chain (DHSC ALB) + UHN Group joint procurement + Northants ICS procurement collaborative"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Northamptonshire ICB + New Hospital Programme"},
            {"label": "Evaluation evidence", "value": "Model Hospital benchmarks; CQC RNQ inspection; UHN group business case; Trust ARA disclosure"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2021 stand-alone Kettering procurement · Successor: UHN Group joint procurement + post-NHP-Reset rebuild procurement consolidation"}
        ],
        "notes": "Kettering General Hospital's general supplies & services baseline is shaped by its membership of the University Hospitals of Northamptonshire group with Northampton General — the chair-in-common arrangement since 2021 has driven shared corporate-functions consolidation, including joint procurement elements that affect non-clinical sourcing patterns. The trust's place in the original NHP cohort, with the January 2025 NHP Reset deferring rebuild, preserves the current site baseline. Industrial action 2023-24 layered cancellation-related re-stocking and agency-backfill use. April 2025 NIC step-up and sustained CPI feed forward; UHN Group joint procurement is the medium-term lever.",
        "sources": [
            {"publisher": "Kettering General Hospital NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.kgh.nhs.uk/our-publications"},
            {"publisher": "University Hospitals of Northamptonshire NHS Group", "title": "Group business case + chair-in-common arrangements", "url": "https://www.uhn.nhs.uk/"},
            {"publisher": "NHS Supply Chain", "title": "Annual Report 2023-24", "url": "https://www.supplychain.nhs.uk/about-us/our-publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Kettering General Hospital provider profile (RNQ)", "url": "https://www.cqc.org.uk/provider/RNQ"}
        ],
        "related": ["Kettering General Hospital NHS Foundation Trust", "Clinical Supplies & Drugs", "NHS Acute Trusts", "Northampton General Hospital NHS Trust", "NHS Supply Chain", "General supplies & services — Liverpool University Hospitals NHS Foundation Trust"]
    },
    "Amortisation — London North West University Healthcare NHS Trust": {
        "aliases": [{"name": "Amortisation", "parent": "London North West University Healthcare NHS Trust"}],
        "description": "LNWH's £4.246M amortisation line covers IAS 38 write-down of capitalised intangibles — software licences, EPR/clinical-systems configuration, radiology PACS, internally-generated apps and acquired digital systems — across the Northwick Park + Ealing Hospital + Central Middlesex + St Mark's footprint. Formed in 2014 (Northwick Park + Ealing merger), the trust is reshaped by NW London ICS configuration plus St Mark's national-bowel unit relocation — sustaining intangible-asset additions through Frontline Digitisation funding.",
        "beneficiaries": "c. 8,500 WTE staff serving a c. 850,000 north-west London catchment (Brent, Harrow, Ealing) plus St Mark's Hospital national bowel-disease tertiary referrals; c. 230,000 ED attendances/yr (Northwick Park + Ealing Hospital combined); c. 110,000 admissions/yr; high-deprivation Brent/Ealing catchment.",
        "legal_basis": "IAS 38 Intangible Assets · IFRIC 22 SaaS configuration/customisation costs (March 2021 agenda decision) · DHSC Group Accounting Manual 2024-25 ch.5 · NHS Act 2006 · Health and Care Act 2022 · NHSE Frontline Digitisation programme guidance",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£4.246M"},
            {"label": "Trust scale", "value": "Multi-site acute (Northwick Park + Ealing Hospital + Central Middlesex + St Mark's); c. 8,500 WTE"},
            {"label": "Tertiary specialty", "value": "St Mark's Hospital = national bowel-disease tertiary referral centre — drives specialist clinical-software intangible base"},
            {"label": "Asset base composition", "value": "Clinical-systems licences + capitalised configuration + radiology PACS + internally-generated clinical apps; 5-10yr UEL per IAS 38 / DHSC GAM ch.5"},
            {"label": "IFRIC 22 effect", "value": "March 2021 SaaS configuration/customisation agenda decision reshaped capitalisation boundary; some costs reclassified opex"},
            {"label": "Frontline Digitisation context", "value": "NHSE Frontline Digitisation funds EPR rollouts to 'core' standard by 2026 — LNWH receiving FD investment within NW London ICS"},
            {"label": "St Mark's relocation programme", "value": "St Mark's Hospital national bowel-disease unit planned relocation drives intangible-asset additions for service-transition systems"},
            {"label": "Funding trajectory", "value": "2021-22 c. £3.4M → 2023-24 £3.9M → 2024-25 £4.246M — sustained intangible additions through Frontline Digitisation cycle"},
            {"label": "Delivery body", "value": "Trust IT + Digital programme office + clinical-systems vendors + DHSC Frontline Digitisation funding + NW London ICS digital pillar"},
            {"label": "Policy owner", "value": "DHSC + NHSE Frontline Digitisation + NHSE Provider Finance + North West London ICB + NHSE Specialised Commissioning"},
            {"label": "Evaluation evidence", "value": "NHSE Frontline Digitisation programme evaluation; NAO Digital Transformation in the NHS (HC 8, 2020); CQC R1K inspection; Trust ARA disclosure"},
            {"label": "Predecessor / successor", "value": "Predecessor: legacy standalone clinical systems pre-2014 merger · Successor: convergent EPR + integrated PACS + St Mark's relocation digital build amortising 2024-2030+"}
        ],
        "notes": "LNWH's amortisation profile reflects sustained capitalisation of clinical-systems software, PACS and Frontline Digitisation investment across a multi-site acute trust formed in 2014 by the Northwick Park + Ealing merger. The St Mark's Hospital national bowel-disease tertiary referral function adds specialist clinical-software intangible to the asset base, with the planned St Mark's relocation programme driving intangible-asset additions for service-transition systems. Implementation labour, software licences and configuration costs flow through IAS 38 over typical 5-10 year UELs, with the IFRIC 22 March 2021 agenda decision having reshaped the capitalisation boundary. NHSE's 2026 'core' EPR target keeps the trajectory upward via NW London ICS digital pillar funding.",
        "sources": [
            {"publisher": "London North West University Healthcare NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.lnwh.nhs.uk/about/our-publications/"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/connecting-health-and-care-providers/frontline-digitisation/"},
            {"publisher": "National Audit Office", "title": "Digital transformation in the NHS (HC 8, 2020)", "url": "https://www.nao.org.uk/reports/the-use-of-digital-technology-in-the-nhs/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 5)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "LNWH provider profile (R1K)", "url": "https://www.cqc.org.uk/provider/R1K"}
        ],
        "related": ["London North West University Healthcare NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Frontline Digitisation Programme", "Amortisation — University Hospitals of Leicester NHS Trust", "North West London Integrated Care Board"]
    },
    "Transport (business + patient) — University Hospitals Sussex NHS Foundation Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "University Hospitals Sussex NHS Foundation Trust"}],
        "description": "UHSussex's £4.232M transport line covers staff business mileage (AfC Section 17 + HMRC AMAP), pool fleet under IFRS 16, contracted Non-Emergency Patient Transport Services and inter-site clinical transfers across the trust's seven-site Sussex footprint — Royal Sussex County Hospital (Brighton MTC), Princess Royal (Haywards Heath), Worthing, St Richard's (Chichester), Royal Alexandra Children's, Sussex Eye and Southlands. Inter-site flows between the four DGHs across Sussex sustain a transport baseline above peer single-DGH groups.",
        "beneficiaries": "c. 14,000 WTE staff serving a c. 1.8M Sussex catchment plus tertiary specialty referrals across the South East; c. 290,000 ED attendances/yr (RSCH + Princess Royal + Worthing + St Richard's combined); c. 180,000 admissions/yr; RSCH = Major Trauma Centre for Sussex.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · IFRS 16 Leases (pool fleet) · NHS Act 2006 · Mental Health Act 1983 (s.135/136 conveyance) · NHSE Patient Transport Services Eligibility Framework 2022 · HMRC AMAP · NHS AfC Section 17",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£4.232M"},
            {"label": "Trust scale", "value": "Seven-site Sussex group (RSCH Brighton + Princess Royal + Worthing + St Richard's + Royal Alex Children's + Sussex Eye + Southlands); c. 14,000 WTE"},
            {"label": "Major Trauma Centre", "value": "RSCH = Sussex MTC — drives inter-trust major-trauma transfer demand"},
            {"label": "Inter-site corridor", "value": "Brighton–Haywards Heath–Worthing–Chichester corridor c. 60 miles of A23 / A27 — sustains routine clinical + corporate inter-site travel"},
            {"label": "2021 merger context", "value": "UHSussex formed Apr 2021 by BSUH + WSHFT merger — consolidated four-DGH-plus footprint; transport baseline reflects post-merger integrated operations"},
            {"label": "PTS + mileage + IFRS 16", "value": "South Central + South East Coast Ambulance PTS + accredited NEPTS contractors via Sussex ICS framework; AfC Section 17 / HMRC AMAP 45p/25p; IFRS 16 right-of-use pool fleet from 2022-23"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove ad-hoc inter-site cover transfers + locum mileage claims"},
            {"label": "Funding trajectory", "value": "Pre-2021 separate BSUH + WSHFT baselines; post-merger consolidated; 2024-25 £4.232M — fuel CPI + activity recovery + 3Ts inter-site flows"},
            {"label": "Delivery body", "value": "Trust E&F + Travel team + SCAS + SECAmb PTS + accredited NEPTS contractors"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + Sussex ICB + NHSE PTS policy"},
            {"label": "Evaluation evidence", "value": "NHSE NEPTS Eligibility Framework 2022 review; CQC RYR inspection; Trust ARA disclosure; merger benefits-realisation review"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2021 separate BSUH + WSHFT transport baselines · Successor: Sussex ICS shared-fleet pooling + 3Ts phase 2 + EV transition"}
        ],
        "notes": "UHSussex was formed in April 2021 by the BSUH + WSHFT merger, creating a seven-site Sussex group whose transport baseline is the consolidated post-merger position rather than two separate lines. The Brighton–Haywards Heath–Worthing–Chichester corridor (c. 60 miles of A23 / A27) sustains routine clinical and corporate inter-site travel above peer single-DGH groups. The Brighton 3Ts phase 1 new-build (opened 2023) drives inter-site flow patterns as services consolidate at RSCH. Industrial action 2023-24 layered ad-hoc cover travel; the IFRS 16 transition stepped pool fleet on-balance-sheet from 2022-23. April 2025 NIC step-up affects PTS-contractor pass-through; Sussex ICS shared-fleet pooling and EV transition are the medium-term levers.",
        "sources": [
            {"publisher": "University Hospitals Sussex NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.uhsussex.nhs.uk/about/publications/annual-report-and-accounts/"},
            {"publisher": "NHS England", "title": "Non-Emergency Patient Transport Services Eligibility Framework 2022", "url": "https://www.england.nhs.uk/long-read/non-emergency-patient-transport-services-eligibility-framework/"},
            {"publisher": "South East Coast Ambulance Service NHS Foundation Trust", "title": "Annual Report 2023-24", "url": "https://www.secamb.nhs.uk/about-us/publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 7 — Leases)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "UHSussex provider profile (RYR)", "url": "https://www.cqc.org.uk/provider/RYR"}
        ],
        "related": ["University Hospitals Sussex NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Transport (business + patient) — Imperial College Healthcare NHS Trust", "Business rates — University Hospitals Sussex NHS Foundation Trust", "Sussex Integrated Care Board"]
    },
    "Business rates — Lewisham and Greenwich NHS Trust": {
        "aliases": [{"name": "Business rates", "parent": "Lewisham and Greenwich NHS Trust"}],
        "description": "Lewisham and Greenwich NHS Trust's £4.229M business-rates line covers National Non-Domestic Rates on the trust's two-site footprint — University Hospital Lewisham and Queen Elizabeth Hospital (Woolwich) — plus satellite outpatient facilities. Rateable values reflect the Valuation Office Agency's 2023 revaluation cycle, with the QEH Woolwich PFI build (signed 1998, opened 2001) contributing a substantial RV on the modern Greenwich site. The Non-Domestic Rating (Multipliers and Private Finance) Act 2024 introduces split multipliers from 2026-27.",
        "beneficiaries": "c. 6,500 WTE staff serving a c. 700,000 south-east London catchment (Lewisham, Greenwich, parts of Bexley); c. 220,000 ED attendances/yr (Lewisham + QEH Woolwich EDs combined); c. 100,000 admissions/yr; large maternity service across both sites.",
        "legal_basis": "Local Government Finance Act 1988 (Sch 6 — non-domestic rating) · Non-Domestic Rating (Multipliers and Private Finance) Act 2024 · Non-Domestic Rating Act 2023 · Valuation Office Agency 2023 revaluation · DHSC Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£4.229M"},
            {"label": "Trust scale", "value": "Two-site acute (University Hospital Lewisham + Queen Elizabeth Hospital Woolwich) post-2013 merger; c. 6,500 WTE"},
            {"label": "Estate covered", "value": "University Hospital Lewisham + Queen Elizabeth Hospital Woolwich (PFI-built 2001) + satellite outpatient facilities"},
            {"label": "Multiplier 2024-25", "value": "Standard 54.6p / Small business 49.9p; new NDRA 2024 split multipliers from 2026-27"},
            {"label": "Revaluation cycle", "value": "VOA 2023 revaluation (effective Apr 2023, AVD 1 Apr 2021) + transitional relief regime"},
            {"label": "QEH Woolwich PFI + 2013 merger context", "value": "QEH Woolwich PFI signed 1998, opened 2001 — modern build with substantial RV baseline; trust formed Oct 2013 by Lewisham Healthcare + QEH merger after South London Healthcare Trust dissolution; PFI hand-back ahead of c. 2031 expiry"},
            {"label": "Funding trajectory", "value": "Post-2013 merger consolidated; 2024-25 £4.229M reflecting 2023 revaluation"},
            {"label": "Billing authorities", "value": "London Borough of Lewisham (UHL site) + Royal Borough of Greenwich (QEH Woolwich)"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + VOA assessment + Lewisham + Greenwich billing authorities + DLUHC oversight"},
            {"label": "Policy owner", "value": "HM Treasury + DLUHC (NDR policy) + DHSC + NHSE Provider Finance + South East London ICB"},
            {"label": "Evaluation evidence", "value": "VOA rating list disclosure; NAO PFI hand-back report 2020; CQC RJ2 inspection; Trust ARA disclosure"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2013 separate Lewisham Healthcare + QEH Trust baselines · Successor: post-2026-27 NDRA split-multiplier regime + 2031 QEH PFI hand-back"}
        ],
        "notes": "Lewisham and Greenwich NHS Trust was formed in October 2013 by merger of Lewisham Healthcare NHS Trust with the Queen Elizabeth Hospital following the South London Healthcare NHS Trust dissolution under the Trust Special Administrator process — consolidating a two-site footprint that crosses Lewisham and Greenwich billing-authority boundaries. The QEH Woolwich PFI (signed 1998, opened 2001) contributes a substantial rateable-value baseline, with PFI hand-back planning ahead of c. 2031 expiry being a parallel medium-term consideration. The Valuation Office Agency's 2023 revaluation (AVD 1 April 2021) sets the current list-cycle baseline. The Non-Domestic Rating (Multipliers and Private Finance) Act 2024 introduces split multipliers from 2026-27 with implications for the QEH PFI estate.",
        "sources": [
            {"publisher": "Lewisham and Greenwich NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.lewishamandgreenwich.nhs.uk/our-publications"},
            {"publisher": "Valuation Office Agency", "title": "2023 Rating list and revaluation", "url": "https://www.gov.uk/government/organisations/valuation-office-agency"},
            {"publisher": "National Audit Office", "title": "Managing PFI assets and services as contracts end (HC 632, 2020)", "url": "https://www.nao.org.uk/reports/managing-pfi-assets-and-services-as-contracts-end/"},
            {"publisher": "Department for Levelling Up, Housing and Communities", "title": "Non-Domestic Rating Act 2023 and Multipliers and Private Finance Act 2024 — implementation guidance", "url": "https://www.gov.uk/government/collections/business-rates"},
            {"publisher": "Care Quality Commission", "title": "Lewisham and Greenwich provider profile (RJ2)", "url": "https://www.cqc.org.uk/provider/RJ2"}
        ],
        "related": ["Lewisham and Greenwich NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Business rates — University Hospitals Sussex NHS Foundation Trust", "Valuation Office Agency", "Non-Domestic Rating"]
    },
}
