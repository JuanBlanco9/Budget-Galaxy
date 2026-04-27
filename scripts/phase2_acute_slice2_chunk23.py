# -*- coding: utf-8 -*-
# Phase 2 Acute slice 2 — chunk 23 (17 NHS Acute Trust orphan sub-lines)
# Hand-curated trust-specific PROGRAMME-archetype enrichment entries.
# Structural contract per docs/archetype_briefs.md.

NEW = {
    "Establishment costs — Torbay and South Devon NHS Foundation Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "Torbay and South Devon NHS Foundation Trust"}],
        "description": "Torbay and South Devon's £3.155M establishment costs line covers postage, telephony, mobile-data, printing, stationery, recruitment advertising, subscriptions and minor sundries across the Torbay Hospital acute site plus the wide community-clinic, community-nursing and adult-social-care footprint embedded in England's most-developed Integrated Care Trust model. The integrated acute + community + adult-social-care budget broadens the back-office overhead base above pure-acute peers, with industrial-action 2023-24 recruitment campaigns and EPR optimisation feeding 2024-25 spend.",
        "beneficiaries": "c. 6,500 WTE staff serving a c. 375,000 Torbay + South Devon catchment (Torquay, Paignton, Brixham, Newton Abbot, Totnes); c. 90,000 ED attendances/yr at Torbay Hospital ED; c. 50,000 admissions/yr; integrated community-nursing + adult-social-care teams across rural South Devon driving a broader corporate-services baseline.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) — IAS 1 Presentation of Financial Statements — NHS Act 2006 — Health and Care Act 2022 — Care Act 2014 (integrated adult-social-care delegation) — NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£3.155M"},
            {"label": "Trust scale", "value": "Torbay Hospital + integrated community-nursing + adult-social-care teams; c. 6,500 WTE"},
            {"label": "Integrated Care Trust model", "value": "Acute + community + adult social-care under single budget — broadens corporate-services + recruitment base above pure-acute peers"},
            {"label": "Composition", "value": "Postage, telephony/mobile, printing, stationery, recruitment advertising, subscriptions, hospitality, minor sundries"},
            {"label": "EPR / Frontline Digitisation", "value": "EPR optimisation track drives change-mgmt + training-materials + comms baseline"},
            {"label": "Industrial action 2023-24", "value": "Junior-doctor 44 days + consultant 10 days strikes drove recruitment-advertising spike + comms costs"},
            {"label": "April 2025 CPI uplift", "value": "Royal Mail + telecoms + advertising CPI feed forward unit-cost pressure"},
            {"label": "Funding trajectory", "value": "2021-22 c. £2.5M → 2023-24 c. £2.9M → 2024-25 £3.155M — sustained CPI + activity uplift"},
            {"label": "Delivery body", "value": "Trust Corporate Services + Procurement + IT + Crown Commercial Service framework (telecoms/postage)"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Devon ICB"},
            {"label": "Evaluation evidence", "value": "Model Hospital corporate-services benchmark; CQC RA9 inspections; NAO Health and Social Care integration 2023; Trust ARA 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2015 stand-alone Torbay Hospital + Devon PCT community baselines · Successor: continued ICT-model embedding under Devon ICS + digital-comms shift"}
        ],
        "notes": "Torbay and South Devon's establishment-costs line sits inside England's earliest-formed Integrated Care Trust — acute, community and adult social-care delivery under a single statutory umbrella broadens the corporate-services and recruitment-advertising base materially above peer acute trusts, with rural South Devon community-team workforce feeding subscription and travel-related back-office spend. Industrial action 2023-24 lifted recruitment-advertising spend through agency and substantive recruitment campaigns. EPR optimisation under NHSE's Frontline Digitisation track sustains digital-training and comms baseline. Royal Mail postage uplifts and telecoms CPI feed forward unit-cost pressure into 2025-26; Devon ICB allocation governs the medium-term frame.",
        "sources": [
            {"publisher": "Torbay and South Devon NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.torbayandsouthdevon.nhs.uk/about-us/our-publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "National Audit Office", "title": "Progress in implementing the integration of health and social care", "url": "https://www.nao.org.uk/reports/progress-in-implementing-integrated-care/"},
            {"publisher": "Care Quality Commission", "title": "Torbay and South Devon provider profile (RA9)", "url": "https://www.cqc.org.uk/provider/RA9"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/connecting-health-and-care/frontline-digitisation/"}
        ],
        "related": ["Torbay and South Devon NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Transport (business + patient) — Torbay and South Devon NHS Foundation Trust", "Establishment costs — Royal Berkshire NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Business rates — South Tees Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "South Tees Hospitals NHS Foundation Trust"}],
        "description": "South Tees Hospitals' £3.115M business-rates line covers non-domestic rates on the James Cook University Hospital Middlesbrough main site (a tertiary regional centre with major-trauma, cardiothoracic and neurosciences specialism) plus the Friarage Hospital Northallerton and outlying community sites. Hereditaments are assessed by the Valuation Office Agency on the 2023 Rating List with billing handled by Middlesbrough Council and North Yorkshire Council. NHS trusts pay the full multiplier with no charitable 80% relief, making rates a meaningful operating-cost item.",
        "beneficiaries": "c. 9,000 WTE staff serving a c. 1.5M Tees Valley + North Yorkshire catchment as regional tertiary centre; c. 130,000 ED attendances/yr (James Cook + Friarage EDs combined); c. 80,000 admissions/yr; James Cook is the regional Major Trauma Centre + cardiothoracic + neurosciences tertiary hub for the Tees Valley.",
        "legal_basis": "Local Government Finance Act 1988 (Schedule 6) — Non-Domestic Rating (Multipliers and Private Finance) Act 2024 — Non-Domestic Rating Act 2023 — DHSC Group Accounting Manual 2024-25 — NHS Act 2006 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£3.115M"},
            {"label": "Trust scale", "value": "James Cook University Hospital (Middlesbrough) c. 1,000 beds + Friarage Hospital (Northallerton) + community sites; c. 9,000 WTE"},
            {"label": "Major Trauma Centre", "value": "James Cook = North-East regional MTC + cardiothoracic + neurosciences tertiary — large rateable footprint"},
            {"label": "Billing authorities", "value": "Middlesbrough Council (James Cook) + North Yorkshire Council (Friarage, post-Apr 2023 LGR)"},
            {"label": "2023 revaluation", "value": "VOA 2023 revaluation (effective 1 Apr 2023) re-set rateable values from 2017 list — large transitional effects on tertiary hereditaments"},
            {"label": "Multiplier 2024-25", "value": "Standard non-domestic multiplier 54.6p (England, 2024-25); NHS pays full rate (no charitable relief)"},
            {"label": "NDR 2024 Act context", "value": "Non-Domestic Rating (Multipliers and Private Finance) Act 2024 — multiplier-split + anti-avoidance reform; tertiary specialty buildings exposed to higher-multiplier classification"},
            {"label": "Funding trajectory", "value": "2021-22 c. £2.7M → 2023-24 (post-revaluation) c. £2.95M → 2024-25 £3.115M — multiplier + transitional uplift"},
            {"label": "Delivery body", "value": "Trust E&F (rates appeals) + Valuation Office Agency + Middlesbrough Council + North Yorkshire Council"},
            {"label": "Policy owner", "value": "MHCLG (NDR policy) + HM Treasury + DHSC + NHSE Provider Finance + North East and North Cumbria ICB"},
            {"label": "Evaluation evidence", "value": "VOA Rating List 2023; NAO Business Rates Reform; Trust ARA 2023-24; CQC RTR inspections"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2017 rating list baseline · Successor: 2026 revaluation cycle + NDR 2024 Act multiplier-split implementation"}
        ],
        "notes": "South Tees' rates line is dominated by the James Cook University Hospital Middlesbrough hereditament — the regional Major Trauma Centre with cardiothoracic and neurosciences tertiary specialism on a c. 1,000-bed footprint — sitting alongside the Friarage Hospital Northallerton (where A&E was downgraded to UTC in 2019, reshaping the retained estate). The VOA 2023 revaluation lifted rateable values across the NHS estate with transitional relief tapering. NHS trusts cannot claim charitable 80% relief, so the full 54.6p standard multiplier applies. The Non-Domestic Rating (Multipliers and Private Finance) Act 2024 introduces multiplier splitting exposing tertiary hereditaments to higher-multiplier classification in future bills.",
        "sources": [
            {"publisher": "South Tees Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.southtees.nhs.uk/about/publications/"},
            {"publisher": "Valuation Office Agency", "title": "2023 Rating List", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "Ministry of Housing, Communities and Local Government", "title": "Non-Domestic Rating Act 2023 + Multipliers and Private Finance Act 2024", "url": "https://www.gov.uk/government/collections/business-rates"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "South Tees Hospitals provider profile (RTR)", "url": "https://www.cqc.org.uk/provider/RTR"}
        ],
        "related": ["South Tees Hospitals NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Business rates — Portsmouth Hospitals University NHS Trust", "Business rates — University Hospitals Bristol and Weston NHS Foundation Trust", "Valuation Office Agency"]
    },
    "Amortisation — The Shrewsbury and Telford Hospital NHS Trust": {
        "aliases": [{"name": "Amortisation", "parent": "The Shrewsbury and Telford Hospital NHS Trust"}],
        "description": "SaTH's £3.115M amortisation line covers the systematic write-down of intangible assets — capitalised software, EPR licences, internally-developed clinical applications and licensed IP — under IAS 38 across the Royal Shrewsbury Hospital and Princess Royal Hospital Telford two-site footprint. SaTH is a New Hospital Programme cohort trust with the Future Fit / Hospitals Transformation Programme (Shrewsbury emergency-care + Telford planned-care reconfiguration) reshaping the medium-term capitalisation profile, and the trust runs an EPR rollout under NHSE's Frontline Digitisation programme.",
        "beneficiaries": "c. 6,500 WTE staff serving a c. 500,000 Shropshire, Telford and Wrekin and Mid Wales catchment; c. 130,000 ED attendances/yr (Royal Shrewsbury + Princess Royal EDs); c. 70,000 admissions/yr; both main sites benefit from amortising digital infrastructure and EPR investment.",
        "legal_basis": "IAS 38 Intangible Assets — DHSC Group Accounting Manual 2024-25 (chapter 5 — Intangibles) — IFRIC SaaS configuration agenda decisions — NHS Act 2006 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£3.115M"},
            {"label": "Trust scale", "value": "Royal Shrewsbury Hospital + Princess Royal Hospital (Telford); c. 6,500 WTE"},
            {"label": "Composition", "value": "Capitalised software + EPR licences + internally-developed clinical applications + licensed IP"},
            {"label": "EPR / Frontline Digitisation", "value": "SaTH Frontline Digitisation track — capitalised EPR build amortising over assessed UEL (5-10 years)"},
            {"label": "NHP / HTP context", "value": "Hospitals Transformation Programme reconfiguration (Shrewsbury emergency-care + Telford planned-care) within the NHP cohort — Jan 2025 NHP Reset deferred construction; intangibles capitalisation continues on operational systems"},
            {"label": "Useful economic life", "value": "Software 3-5 years; EPR / clinical-system 5-10 years per DHSC GAM ch.5 + IAS 38 review"},
            {"label": "IFRIC SaaS agenda decision", "value": "2021 IFRIC agenda decision on SaaS configuration costs — restricts capitalisation; some EPR programme spend now opex"},
            {"label": "Funding trajectory", "value": "2021-22 c. £2.4M → 2023-24 c. £2.85M → 2024-25 £3.115M — Frontline Digitisation amortisation cycle ramp + Ockenden-driven maternity-system capitalisation"},
            {"label": "Delivery body", "value": "Trust IT + Finance (capitalisation) + EPR vendor + NHSE Frontline Digitisation programme"},
            {"label": "Policy owner", "value": "DHSC + NHSE Transformation Directorate + NHSE Provider Finance + Shropshire, Telford and Wrekin ICB"},
            {"label": "Evaluation evidence", "value": "NAO Digital transformation in NHS 2020; Final Ockenden Review 2022; DHSC GAM ch.5; Trust ARA 2023-24; CQC RXW inspections"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-Frontline Digitisation legacy clinical-system amortisation tail · Successor: full EPR-go-live amortisation peak + post-HTP reconfiguration capitalisation reset"}
        ],
        "notes": "SaTH's amortisation line tracks intangible-asset stock through a difficult institutional period — the Final Ockenden Review (March 2022) on maternity failures drove regulatory action and substantial governance + clinical-information-system investment, with maternity-system upgrades feeding capitalised intangibles. Frontline Digitisation EPR build amortises over a 5-10 year assessed useful-economic-life per DHSC GAM ch.5 and IAS 38. The 2021 IFRIC SaaS agenda decision restricts SaaS configuration capitalisation, pushing some build spend into opex. The Hospitals Transformation Programme reconfiguration within the NHP cohort was deferred under January 2025 NHP Reset; intangibles capitalisation continues on operational system rollouts independently of the deferred capital build.",
        "sources": [
            {"publisher": "The Shrewsbury and Telford Hospital NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.sath.nhs.uk/about-us/key-publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 5 — Intangibles)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Donna Ockenden Review Team", "title": "Final Ockenden Report — review of maternity services at SaTH (Mar 2022)", "url": "https://www.gov.uk/government/publications/final-report-of-the-ockenden-review"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/connecting-health-and-care/frontline-digitisation/"},
            {"publisher": "Care Quality Commission", "title": "SaTH provider profile (RXW)", "url": "https://www.cqc.org.uk/provider/RXW"}
        ],
        "related": ["The Shrewsbury and Telford Hospital NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Amortisation — Portsmouth Hospitals University NHS Trust", "Amortisation — University Hospitals Bristol and Weston NHS Foundation Trust", "NHS England"]
    },
    "Business rates — University Hospital Southampton NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "University Hospital Southampton NHS Foundation Trust"}],
        "description": "UHS's £3.112M business-rates line covers non-domestic rates on the Southampton General Hospital main site (a tertiary regional centre with cardiothoracic, neurosciences, paediatrics and major-trauma specialism), the Princess Anne Hospital (maternity + neonatal) and the Royal South Hants Hospital outpatient site. Hereditaments are assessed by the Valuation Office Agency on the 2023 Rating List with billing handled by Southampton City Council. NHS trusts pay the full multiplier with no charitable 80% relief, making rates a meaningful operating-cost item across this large tertiary footprint.",
        "beneficiaries": "c. 12,000 WTE staff serving a c. 1.9M Wessex tertiary catchment as regional centre; c. 130,000 ED attendances/yr at Southampton General ED; c. 110,000 admissions/yr; Southampton General hosts the regional Major Trauma Centre, cardiothoracic + neurosciences + paediatric tertiary specialism; Princess Anne is the regional maternity/neonatal hub.",
        "legal_basis": "Local Government Finance Act 1988 (Schedule 6) — Non-Domestic Rating (Multipliers and Private Finance) Act 2024 — Non-Domestic Rating Act 2023 — DHSC Group Accounting Manual 2024-25 — NHS Act 2006 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£3.112M"},
            {"label": "Trust scale", "value": "Southampton General Hospital c. 1,000 beds + Princess Anne (maternity/neonatal) + Royal South Hants outpatient; c. 12,000 WTE"},
            {"label": "Major Trauma Centre", "value": "Southampton General = Wessex regional MTC + cardiothoracic + neurosciences + paediatric tertiary — large rateable footprint"},
            {"label": "Billing authority", "value": "Southampton City Council (NDR collection); Valuation Office Agency rateable-value assessment"},
            {"label": "2023 revaluation", "value": "VOA 2023 revaluation (effective 1 Apr 2023) re-set rateable values from 2017 list — large transitional effects on tertiary hereditaments"},
            {"label": "Multiplier 2024-25", "value": "Standard non-domestic multiplier 54.6p (England, 2024-25); NHS pays full rate (no charitable relief)"},
            {"label": "NDR 2024 Act context", "value": "Non-Domestic Rating (Multipliers and Private Finance) Act 2024 — multiplier-split + anti-avoidance reform; tertiary specialty buildings exposed to higher-multiplier classification"},
            {"label": "Funding trajectory", "value": "2021-22 c. £2.7M → 2023-24 (post-revaluation) c. £2.95M → 2024-25 £3.112M — multiplier + transitional uplift"},
            {"label": "Delivery body", "value": "Trust E&F (rates appeals) + Valuation Office Agency + Southampton City Council"},
            {"label": "Policy owner", "value": "MHCLG (NDR policy) + HM Treasury + DHSC + NHSE Provider Finance + Hampshire and Isle of Wight ICB"},
            {"label": "Evaluation evidence", "value": "VOA Rating List 2023; NAO Business Rates Reform; Trust ARA 2023-24; CQC RHM inspections"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2017 rating list baseline · Successor: 2026 revaluation cycle + NDR 2024 Act multiplier-split implementation"}
        ],
        "notes": "UHS's rates line is dominated by the Southampton General Hospital hereditament — a c. 1,000-bed Wessex tertiary regional centre with the Major Trauma Centre, cardiothoracic, neurosciences and paediatric services on a single site — supplemented by the Princess Anne maternity/neonatal site and Royal South Hants outpatient hereditament. The VOA 2023 revaluation lifted rateable values across the NHS estate with transitional relief tapering. NHS trusts cannot claim charitable 80% relief, so the full 54.6p standard multiplier applies. The Non-Domestic Rating (Multipliers and Private Finance) Act 2024 introduces multiplier splitting that exposes the larger tertiary hereditaments to higher-multiplier classification in future bills.",
        "sources": [
            {"publisher": "University Hospital Southampton NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.uhs.nhs.uk/about-us/our-publications/annual-report"},
            {"publisher": "Valuation Office Agency", "title": "2023 Rating List", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "Ministry of Housing, Communities and Local Government", "title": "Non-Domestic Rating Act 2023 + Multipliers and Private Finance Act 2024", "url": "https://www.gov.uk/government/collections/business-rates"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "UHS provider profile (RHM)", "url": "https://www.cqc.org.uk/provider/RHM"}
        ],
        "related": ["University Hospital Southampton NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Business rates — Portsmouth Hospitals University NHS Trust", "Business rates — South Tees Hospitals NHS Foundation Trust", "Valuation Office Agency"]
    },
    "Transport (business + patient) — Lancashire Teaching Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "Lancashire Teaching Hospitals NHS Foundation Trust"}],
        "description": "Lancashire Teaching Hospitals' £3.111M transport line covers business mileage (AfC Section 17 + AMAP), pool-fleet IFRS 16 lease costs, NEPTS contract pass-through and patient travel reimbursements across the Royal Preston Hospital and Chorley & South Ribble Hospital two-site footprint. Royal Preston is the regional Major Trauma Centre and tertiary neurosciences/cancer centre for Lancashire and South Cumbria, generating substantial inter-site and inter-trust patient-transport demand. NEPTS is commissioned through the LSC ICS lead-commissioner arrangement.",
        "beneficiaries": "c. 8,500 WTE staff serving a c. 390,000 Central Lancashire catchment plus c. 1.6M tertiary referrals across Lancashire and South Cumbria; c. 165,000 ED attendances/yr (Royal Preston + Chorley EDs); c. 90,000 admissions/yr; Royal Preston is the regional MTC and tertiary neurosciences/specialist-cancer centre.",
        "legal_basis": "NHS Act 2006 — NHSE Patient Transport Services Eligibility Criteria — Agenda for Change Section 17 (business mileage) — HMRC AMAP rates — IFRS 16 Leases (pool fleet) — DHSC Group Accounting Manual 2024-25 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£3.111M"},
            {"label": "Trust scale", "value": "Royal Preston Hospital + Chorley and South Ribble Hospital two-site; c. 8,500 WTE"},
            {"label": "Major Trauma Centre + tertiary", "value": "Royal Preston = Lancashire and South Cumbria regional MTC + tertiary neurosciences + specialist-cancer (Rosemere) — drives high inter-site + inter-trust transfer demand"},
            {"label": "Composition", "value": "Business mileage (AfC S17 + AMAP 45p/25p) + pool-fleet IFRS 16 leases + NEPTS contract pass-through + patient travel reimbursements"},
            {"label": "NEPTS commissioning", "value": "Lancashire and South Cumbria ICS lead-commissioner NEPTS contract; outsourced operator delivery; eligibility per NHSE 2021 criteria; Chorley A&E intermittent closures since 2016 drive inter-site emergency-transfer demand"},
            {"label": "AMAP rate context", "value": "HMRC AMAP rate frozen at 45p/mile (first 10k miles) since 2011 — real-terms erosion lifts NHS-internal mileage rate disputes"},
            {"label": "Industrial action 2023-24 effect", "value": "Junior-doctor 44 days + consultant 10 days strikes drove agency travel-claim spikes + cancellation rebooking transport"},
            {"label": "Funding trajectory", "value": "2021-22 c. £2.5M → 2023-24 c. £2.85M → 2024-25 £3.111M — fuel CPI + activity recovery"},
            {"label": "Delivery body", "value": "Trust E&F + Travel team + outsourced NEPTS provider (LSC ICS lead-commissioner) + pool-fleet leasing partner + Trust HR (mileage)"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + NHSE Urgent and Emergency Care (NEPTS) + Lancashire and South Cumbria ICB + DHSC"},
            {"label": "Evaluation evidence", "value": "NAO NEPTS context 2019; CQC RXN inspections; NHSE NEPTS Eligibility Review 2021; Trust ARA 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-ICS CCG-commissioned NEPTS contracts · Successor: ICS-collaborative NEPTS retender + group-model planning under LSC integration discussions"}
        ],
        "notes": "Lancashire Teaching Hospitals' transport baseline reflects Royal Preston's role as the Lancashire and South Cumbria regional Major Trauma Centre, tertiary neurosciences and Rosemere specialist-cancer centre — these tertiary services drive significant inter-trust patient-transport demand from across the LSC ICS footprint. Chorley A&E's intermittent closures and downgrades since 2016 have generated substantial planned and unplanned inter-site patient-transfer flows to Preston, which sustain the line above peer two-site DGH baselines. Industrial action 2023-24 lifted agency travel-claim and rebooking spend; HMRC AMAP-rate freeze (45p/mile since 2011) sustains internal-rate dispute pressure. LSC ICS commissions NEPTS centrally, with eligibility tightened under NHSE's 2021 criteria refresh.",
        "sources": [
            {"publisher": "Lancashire Teaching Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.lancsteachinghospitals.nhs.uk/annual-reports"},
            {"publisher": "NHS England", "title": "Non-Emergency Patient Transport Services — National Framework + Eligibility Criteria 2021", "url": "https://www.england.nhs.uk/publication/non-emergency-patient-transport-services-nepts/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Lancashire Teaching Hospitals provider profile (RXN)", "url": "https://www.cqc.org.uk/provider/RXN"},
            {"publisher": "HM Revenue and Customs", "title": "AMAP rates and thresholds", "url": "https://www.gov.uk/expenses-and-benefits-business-travel-mileage/rules-for-tax"}
        ],
        "related": ["Lancashire Teaching Hospitals NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Transport (business + patient) — Royal Berkshire NHS Foundation Trust", "Transport (business + patient) — Torbay and South Devon NHS Foundation Trust", "NHS England"]
    },
    "Amortisation — University Hospitals Sussex NHS Foundation Trust": {
        "aliases": [{"name": "Amortisation", "parent": "University Hospitals Sussex NHS Foundation Trust"}],
        "description": "UHSussex's £3.108M amortisation line covers systematic write-down of intangible assets — capitalised software, EPR licences, internally-developed clinical applications and licensed IP — under IAS 38 across the seven-site Brighton + Worthing + St Richard's Chichester + Princess Royal Haywards Heath + Southlands footprint following the April 2021 merger of Brighton and Sussex UH with Western Sussex Hospitals. The trust runs an Oracle-Cerner EPR convergence under Frontline Digitisation, with merger-driven system convergence pulling capitalised build through.",
        "beneficiaries": "c. 13,000 WTE staff serving a c. 1.8M Sussex catchment as regional centre; c. 250,000 ED attendances/yr (Royal Sussex County + Worthing + St Richard's EDs); c. 130,000 admissions/yr; Royal Sussex County is the regional Major Trauma Centre + tertiary cardiac/neurosciences hub — all sites benefit from amortising digital infrastructure.",
        "legal_basis": "IAS 38 Intangible Assets — DHSC Group Accounting Manual 2024-25 (chapter 5 — Intangibles) — IFRIC SaaS configuration agenda decisions — NHS Act 2006 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£3.108M"},
            {"label": "Trust scale", "value": "Seven-site (Royal Sussex County + Princess Royal Haywards Heath + Worthing + St Richard's Chichester + Southlands + community) post-2021 merger; c. 13,000 WTE"},
            {"label": "Composition", "value": "Capitalised software + EPR licences + internally-developed clinical applications + licensed IP"},
            {"label": "Merger context", "value": "Apr 2021 merger of Brighton and Sussex UH + Western Sussex — post-merger system convergence drives integration-related capitalised build"},
            {"label": "EPR / Frontline Digitisation", "value": "Oracle-Cerner EPR convergence under NHSE Frontline Digitisation — capitalised build amortising over assessed UEL (5-10 years); Royal Sussex County 3Ts redevelopment generates clinical-system fit-out intangibles alongside tangibles"},
            {"label": "Useful economic life", "value": "Software 3-5 years; EPR / clinical-system 5-10 years per DHSC GAM ch.5 + IAS 38 review"},
            {"label": "IFRIC SaaS agenda decision", "value": "2021 IFRIC agenda decision on SaaS configuration costs — restricts capitalisation; some EPR programme spend now opex"},
            {"label": "Funding trajectory", "value": "2021-22 (post-merger) c. £2.4M → 2023-24 c. £2.85M → 2024-25 £3.108M — Frontline Digitisation amortisation cycle ramp"},
            {"label": "Delivery body", "value": "Trust IT + Finance (capitalisation) + EPR vendor (Oracle Health/Cerner) + NHSE Frontline Digitisation programme"},
            {"label": "Policy owner", "value": "DHSC + NHSE Transformation Directorate + NHSE Provider Finance + Sussex ICB"},
            {"label": "Evaluation evidence", "value": "NAO Digital transformation in NHS 2020; DHSC GAM ch.5; Trust ARA 2023-24; CQC inspections (RYR)"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-merger separate BSUH + WSH intangible stocks · Successor: post-merger system-convergence amortisation peak + post-IFRIC SaaS reclassification"}
        ],
        "notes": "UHSussex's amortisation line carries the post-April-2021 merger system-convergence trajectory — Brighton and Sussex UH integrated with Western Sussex Hospitals creating a seven-site Sussex regional trust, with Oracle-Cerner EPR convergence under Frontline Digitisation pulling capitalised build through the line. The Royal Sussex County 3Ts redevelopment generates clinical-system fit-out intangibles alongside tangible-asset depreciation in a separate line. The 2021 IFRIC SaaS agenda decision restricts capitalisation of SaaS configuration costs, pushing some build spend into opex. UEL assessment per DHSC GAM ch.5 and IAS 38 governs the 5-10 year clinical-system cycle.",
        "sources": [
            {"publisher": "University Hospitals Sussex NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.uhsussex.nhs.uk/about-us/our-publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 5 — Intangibles)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/connecting-health-and-care/frontline-digitisation/"},
            {"publisher": "National Audit Office", "title": "Digital transformation in the NHS (HC 317, 2020)", "url": "https://www.nao.org.uk/reports/the-use-of-digital-technology-in-the-nhs/"},
            {"publisher": "Care Quality Commission", "title": "UHSussex provider profile (RYR)", "url": "https://www.cqc.org.uk/provider/RYR"}
        ],
        "related": ["University Hospitals Sussex NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Amortisation — Portsmouth Hospitals University NHS Trust", "Amortisation — University Hospitals Bristol and Weston NHS Foundation Trust", "NHS England"]
    },
    "General supplies & services — Wye Valley NHS Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "Wye Valley NHS Trust"}],
        "description": "Wye Valley's £3.103M general supplies & services line covers non-clinical consumables, linen, catering, hotel-services materials, office supplies and minor expensed equipment across the Hereford County Hospital DGH and integrated Herefordshire community-services footprint. The trust runs an integrated acute + community model under Herefordshire and Worcestershire ICS, with Hereford County Hospital PFI (op. 2002, novated to Engie/Equans post-Carillion 2018) shaping soft-FM consumables boundaries. Rural geography sustains community-consumable demand above peer DGH baselines.",
        "beneficiaries": "c. 3,500 WTE staff serving a c. 200,000 Herefordshire catchment plus rural Welsh borders patients; c. 65,000 ED attendances/yr at Hereford County Hospital ED; c. 35,000 admissions/yr; integrated Herefordshire community-services workforce broadens consumable footprint across rural settings.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) — IAS 2 Inventories — Procurement Act 2023 — NHS Act 2006 — Health and Care Act 2022 — NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "General supplies & services 2024-25", "value": "£3.103M"},
            {"label": "Trust scale", "value": "Hereford County Hospital DGH + integrated Herefordshire community services; c. 3,500 WTE"},
            {"label": "PFI estate context", "value": "Hereford County Hospital PFI (operational 2002, c. 2032 expiry) — Carillion 2018 collapse drove FM novation to Engie/Equans; consumable-ownership boundary shapes line scope"},
            {"label": "Composition + integration", "value": "Linen, catering, hotel-services materials, office + IT consumables, minor expensed equipment; integrated acute + community model broadens consumable base across rural community settings"},
            {"label": "Procurement route", "value": "NHS Supply Chain national framework + trust-direct contracts + Herefordshire and Worcestershire ICS collaborative"},
            {"label": "Industrial action 2023-24 effect", "value": "Junior-doctor 44 days + consultant strikes drove cancellation rebooking + agency-backfill consumable churn"},
            {"label": "April 2025 NIC + CPI uplift", "value": "Indirect via supplier pass-through; non-clinical CPI + supplier NIC step-up feed forward unit-cost pressure"},
            {"label": "Funding trajectory", "value": "2021-22 c. £2.5M → 2023-24 c. £2.85M → 2024-25 £3.103M — sustained CPI + activity uplift"},
            {"label": "Delivery body", "value": "Trust Procurement + NHS Supply Chain (DHSC ALB) + Herefordshire & Worcestershire ICS procurement collaborative + Engie/Equans PFI soft-FM (boundary)"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Herefordshire and Worcestershire ICB"},
            {"label": "Evaluation evidence", "value": "Model Hospital benchmarks; NAO PFI hand-back report 2020; NHS Supply Chain ARA; Trust ARA 2023-24; CQC RLQ inspections"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2018 Carillion-era FM baseline · Successor: ICS-collaborative procurement scaling + 2032 PFI hand-back consumable-boundary reset"}
        ],
        "notes": "Wye Valley's general supplies & services baseline is shaped by the Hereford County Hospital PFI (operational 2002, expiry c. 2032) where Carillion's January 2018 collapse drove FM novation to Engie/Equans, with the soft-FM consumable-ownership boundary affecting which materials flow through this line versus the unitary charge. The integrated acute + community model under Herefordshire and Worcestershire ICS broadens the consumable base across rural community settings. NHS Supply Chain remains dominant; ICS procurement collaborative scaling is the medium-term lever. Industrial action 2023-24 drove cancellation rebooking and agency-backfill churn; PFI hand-back planning ahead of 2032 expiry will reset the consumable-boundary structure.",
        "sources": [
            {"publisher": "Wye Valley NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.wyevalley.nhs.uk/about-us/our-publications.aspx"},
            {"publisher": "NHS Supply Chain", "title": "Annual Report 2023-24", "url": "https://www.supplychain.nhs.uk/about-us/our-publications/"},
            {"publisher": "National Audit Office", "title": "Managing PFI assets and services as contracts end (HC 632, 2020)", "url": "https://www.nao.org.uk/reports/managing-pfi-assets-and-services-as-contracts-end/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Wye Valley NHS Trust provider profile (RLQ)", "url": "https://www.cqc.org.uk/provider/RLQ"}
        ],
        "related": ["Wye Valley NHS Trust", "Clinical Supplies & Drugs", "NHS Acute Trusts", "General supplies & services — Sherwood Forest Hospitals NHS Foundation Trust", "NHS Supply Chain", "Department of Health and Social Care"]
    },
    "Establishment costs — Dartford and Gravesham NHS Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "Dartford and Gravesham NHS Trust"}],
        "description": "Dartford and Gravesham's £3.101M establishment costs line covers postage, telephony, mobile-data, printing, stationery, recruitment advertising, subscriptions and minor sundries across the Darent Valley Hospital DGH (PFI-built, operational 2000) plus the Erith and Gravesham community-clinic outreach footprint. The Darent Valley PFI was one of the NHS's earliest (signed 1997, operational 2000) and runs to 2028, putting the trust in active hand-back planning. Industrial-action 2023-24 recruitment campaigns and EPR rollout change-management feed 2024-25 spend.",
        "beneficiaries": "c. 3,500 WTE staff serving a c. 500,000 north-Kent + south-east London catchment (Dartford, Gravesend, Bexley); c. 130,000 ED attendances/yr at Darent Valley ED; c. 60,000 admissions/yr; single main DGH (Darent Valley) plus Erith and Gravesham community outpatient sites.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) — IAS 1 Presentation of Financial Statements — NHS Act 2006 — Health and Care Act 2022 — NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£3.101M"},
            {"label": "Trust scale", "value": "Darent Valley Hospital (Dartford, PFI-built operational 2000) + Erith + Gravesham community sites; c. 3,500 WTE"},
            {"label": "PFI hand-back window", "value": "Darent Valley PFI signed 1997, operational 2000, expiry c. 2028 — first-wave PFI in active hand-back planning window"},
            {"label": "Composition", "value": "Postage, telephony/mobile, printing, stationery, recruitment advertising, subscriptions, hospitality, minor sundries"},
            {"label": "EPR / Frontline Digitisation", "value": "Frontline Digitisation track drives change-mgmt + training-materials baseline"},
            {"label": "Industrial action 2023-24", "value": "Junior-doctor 44 days + consultant 10 days strikes drove recruitment-advertising spike + comms costs"},
            {"label": "April 2025 CPI uplift", "value": "Royal Mail + telecoms + advertising CPI feed forward unit-cost pressure"},
            {"label": "Funding trajectory", "value": "2021-22 c. £2.4M → 2023-24 c. £2.85M → 2024-25 £3.101M — sustained CPI + hand-back planning costs"},
            {"label": "Delivery body", "value": "Trust Corporate Services + Procurement + IT + Crown Commercial Service framework (telecoms/postage)"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + IPA PFI Hand-Back unit + Kent and Medway ICB"},
            {"label": "Evaluation evidence", "value": "Model Hospital corporate-services benchmark; NAO PFI hand-back 2020; CQC RN7 inspections; Trust ARA 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-PFI fragmented North Kent acute baselines · Successor: post-2028 PFI hand-back operating-model + post-EPR digital-comms shift"}
        ],
        "notes": "Dartford and Gravesham's establishment-costs line carries the embedded back-office overhead of one of the NHS's first-wave PFI hospitals — Darent Valley (1997-signed, 2000-operational, 2028-expiry) — putting the trust in active hand-back planning under IPA/HMT engagement. The hand-back transition is generating planning-related advisory and recruitment costs that feed corporate-services lines ahead of the 2028 contract end. Industrial action 2023-24 drove recruitment-advertising spend through agency and substantive recruitment campaigns. Frontline Digitisation EPR rollout sustains digital-training and comms baseline. Royal Mail postage uplifts and telecoms CPI feed forward unit-cost pressure into 2025-26; Kent and Medway ICB allocation governs medium-term frame.",
        "sources": [
            {"publisher": "Dartford and Gravesham NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.dvh.nhs.uk/about-us/publications/"},
            {"publisher": "National Audit Office", "title": "Managing PFI assets and services as contracts end (HC 632, 2020)", "url": "https://www.nao.org.uk/reports/managing-pfi-assets-and-services-as-contracts-end/"},
            {"publisher": "Infrastructure and Projects Authority", "title": "PFI Hand-Back Resource Centre", "url": "https://www.gov.uk/government/collections/pfi-and-pf2"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Dartford and Gravesham provider profile (RN7)", "url": "https://www.cqc.org.uk/provider/RN7"}
        ],
        "related": ["Dartford and Gravesham NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Establishment costs — Sherwood Forest Hospitals NHS Foundation Trust", "Establishment costs — Royal Berkshire NHS Foundation Trust", "Infrastructure and Projects Authority"]
    },
    "Transport (business + patient) — Mid and South Essex NHS Foundation Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "Mid and South Essex NHS Foundation Trust"}],
        "description": "MSE's £3.099M transport line covers business mileage (AfC Section 17 + AMAP), pool-fleet IFRS 16 lease costs, NEPTS contract pass-through and patient travel reimbursements across the trust's three-site footprint (Basildon, Broomfield Chelmsford, Southend) following the April 2020 merger of Basildon and Thurrock UH + Mid Essex + Southend UH. Inter-site transfers between Essex Cardiothoracic Centre at Basildon, the Burns Service at Broomfield and the Southend cancer centre generate substantial PTS demand. NEPTS sits with the MSE ICS lead-commissioner arrangement.",
        "beneficiaries": "c. 14,000 WTE staff serving a c. 1.2M Mid and South Essex catchment plus tertiary cardiothoracic + burns referrals; c. 320,000 ED attendances/yr (Basildon + Broomfield + Southend EDs combined); c. 130,000 admissions/yr; tertiary Essex Cardiothoracic Centre + St Andrew's Burns Service drive inter-site demand.",
        "legal_basis": "NHS Act 2006 — NHSE Patient Transport Services Eligibility Criteria — Agenda for Change Section 17 (business mileage) — HMRC AMAP rates — IFRS 16 Leases (pool fleet) — DHSC Group Accounting Manual 2024-25 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£3.099M"},
            {"label": "Trust scale", "value": "Three-site (Basildon + Broomfield Chelmsford + Southend) post-2020 merger; c. 14,000 WTE"},
            {"label": "Tertiary specialty centres", "value": "Essex Cardiothoracic Centre (Basildon) + St Andrew's Centre for Plastic Surgery and Burns (Broomfield) — drive inter-site clinical-transfer demand"},
            {"label": "Composition", "value": "Business mileage (AfC S17 + AMAP 45p/25p) + pool-fleet IFRS 16 leases + NEPTS contract pass-through + patient travel reimbursements"},
            {"label": "NEPTS commissioning", "value": "Mid and South Essex ICS lead-commissioner NEPTS contract — outsourced operator (recently re-tendered); eligibility per NHSE 2021 criteria"},
            {"label": "AMAP rate context", "value": "HMRC AMAP rate frozen at 45p/mile (first 10k miles) since 2011 — real-terms erosion lifts NHS-internal mileage rate disputes"},
            {"label": "Industrial action 2023-24 effect", "value": "Junior-doctor 44 days + consultant 10 days strikes drove agency travel-claim spikes + cancellation rebooking transport"},
            {"label": "Funding trajectory", "value": "2021-22 (post-merger) c. £2.4M → 2023-24 c. £2.85M → 2024-25 £3.099M — fuel CPI + activity recovery"},
            {"label": "Delivery body", "value": "Trust E&F + Travel team + outsourced NEPTS provider (MSE ICS lead-commissioner) + pool-fleet leasing partner + Trust HR (mileage)"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + NHSE Urgent and Emergency Care (NEPTS) + Mid and South Essex ICB + DHSC"},
            {"label": "Evaluation evidence", "value": "NAO NEPTS context 2019; CQC RDD inspections; NHSE NEPTS Eligibility Review 2021; Trust ARA 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2020 separate Basildon + Mid Essex + Southend transport baselines · Successor: ICS-collaborative NEPTS retender + post-merger inter-site flow optimisation"}
        ],
        "notes": "Mid and South Essex's transport line carries the consequence of the April 2020 three-trust merger — Basildon and Thurrock UH, Mid Essex and Southend UH formed a c. 14,000-WTE single trust, with the Essex Cardiothoracic Centre at Basildon and the St Andrew's Burns Service at Broomfield generating substantial inter-site clinical-transfer demand for both elective and emergency PTS. NEPTS is commissioned through the Mid and South Essex ICS lead-commissioner arrangement with outsourced operator delivery, re-tendered under the 2021 NHSE eligibility framework. Industrial action 2023-24 lifted agency travel-claim and rebooking spend; HMRC AMAP-rate freeze (45p/mile since 2011) sustains internal-rate dispute pressure.",
        "sources": [
            {"publisher": "Mid and South Essex NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.mse.nhs.uk/our-publications"},
            {"publisher": "NHS England", "title": "Non-Emergency Patient Transport Services — National Framework + Eligibility Criteria 2021", "url": "https://www.england.nhs.uk/publication/non-emergency-patient-transport-services-nepts/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Mid and South Essex provider profile (RDD)", "url": "https://www.cqc.org.uk/provider/RDD"},
            {"publisher": "HM Revenue and Customs", "title": "AMAP rates and thresholds", "url": "https://www.gov.uk/expenses-and-benefits-business-travel-mileage/rules-for-tax"}
        ],
        "related": ["Mid and South Essex NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Transport (business + patient) — Lancashire Teaching Hospitals NHS Foundation Trust", "Transport (business + patient) — Royal Berkshire NHS Foundation Trust", "NHS England"]
    },
    "Transport (business + patient) — Blackpool Teaching Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "Blackpool Teaching Hospitals NHS Foundation Trust"}],
        "description": "Blackpool Teaching's £3.077M transport line covers business mileage (AfC Section 17 + AMAP), pool-fleet IFRS 16 leases, NEPTS contract pass-through and patient travel reimbursements across the Victoria Hospital Blackpool acute site, Clifton Hospital and the integrated Fylde + Wyre community-services footprint. The trust hosts the Lancashire Cardiac Centre tertiary specialty (catheter labs, cardiothoracic surgery), generating regional inter-trust patient-transfer demand from across Lancashire and South Cumbria. NEPTS sits with the LSC ICS lead-commissioner.",
        "beneficiaries": "c. 7,000 WTE staff serving a c. 330,000 Fylde Coast catchment plus c. 1.6M tertiary cardiac referrals across Lancashire and South Cumbria; c. 110,000 ED attendances/yr at Victoria Hospital Blackpool ED; c. 60,000 admissions/yr; tertiary Lancashire Cardiac Centre + integrated Fylde + Wyre community services.",
        "legal_basis": "NHS Act 2006 — NHSE Patient Transport Services Eligibility Criteria — Agenda for Change Section 17 (business mileage) — HMRC AMAP rates — IFRS 16 Leases (pool fleet) — DHSC Group Accounting Manual 2024-25 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£3.077M"},
            {"label": "Trust scale", "value": "Victoria Hospital Blackpool + Clifton Hospital + integrated Fylde and Wyre community services; c. 7,000 WTE"},
            {"label": "Tertiary specialty centre", "value": "Lancashire Cardiac Centre — regional cardiothoracic + interventional-cardiology hub generating inter-trust patient-transfer demand"},
            {"label": "Composition", "value": "Business mileage (AfC S17 + AMAP 45p/25p) + pool-fleet IFRS 16 leases + NEPTS contract pass-through + patient travel reimbursements"},
            {"label": "NEPTS commissioning + community", "value": "LSC ICS lead-commissioner NEPTS contract; outsourced operator delivery; eligibility per NHSE 2021 criteria; integrated Fylde + Wyre community services broaden business-mileage base across rural visits"},
            {"label": "AMAP rate context", "value": "HMRC AMAP rate frozen at 45p/mile (first 10k miles) since 2011 — real-terms erosion sustains internal-rate dispute pressure"},
            {"label": "Industrial action 2023-24 effect", "value": "Junior-doctor 44 days + consultant 10 days strikes drove agency travel-claim spikes + cancellation rebooking transport"},
            {"label": "Funding trajectory", "value": "2021-22 c. £2.5M → 2023-24 c. £2.85M → 2024-25 £3.077M — fuel CPI + activity recovery"},
            {"label": "Delivery body", "value": "Trust E&F + Travel team + outsourced NEPTS provider (LSC ICS lead-commissioner) + pool-fleet leasing partner + Trust HR (mileage)"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + NHSE Urgent and Emergency Care (NEPTS) + Lancashire and South Cumbria ICB + DHSC"},
            {"label": "Evaluation evidence", "value": "NAO NEPTS context 2019; CQC RXL inspections; NHSE NEPTS Eligibility Review 2021; Trust ARA 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-ICS CCG-commissioned NEPTS contracts · Successor: LSC ICS-collaborative NEPTS retender + group-model planning"}
        ],
        "notes": "Blackpool Teaching's transport baseline reflects two distinctive drivers — the Lancashire Cardiac Centre tertiary specialism generating regional inter-trust patient-transport flows from across Lancashire and South Cumbria, and the integrated Fylde + Wyre community services that broaden the business-mileage base above peer DGH baselines. LSC ICS commissions NEPTS centrally, with eligibility tightened under NHSE's 2021 criteria refresh and outsourced operator delivery. Industrial action 2023-24 lifted agency travel-claim and rebooking spend; HMRC AMAP-rate freeze (45p/mile since 2011) sustains internal-rate dispute pressure. Fylde Coast deprivation profile and seasonal-population variation feed unique transport demands not seen in peer trusts.",
        "sources": [
            {"publisher": "Blackpool Teaching Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.bfwh.nhs.uk/about-us/key-publications/annual-report/"},
            {"publisher": "NHS England", "title": "Non-Emergency Patient Transport Services — National Framework + Eligibility Criteria 2021", "url": "https://www.england.nhs.uk/publication/non-emergency-patient-transport-services-nepts/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Blackpool Teaching Hospitals provider profile (RXL)", "url": "https://www.cqc.org.uk/provider/RXL"},
            {"publisher": "HM Revenue and Customs", "title": "AMAP rates and thresholds", "url": "https://www.gov.uk/expenses-and-benefits-business-travel-mileage/rules-for-tax"}
        ],
        "related": ["Blackpool Teaching Hospitals NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Transport (business + patient) — Lancashire Teaching Hospitals NHS Foundation Trust", "Transport (business + patient) — Mid and South Essex NHS Foundation Trust", "NHS England"]
    },
    "Establishment costs — Harrogate and District NHS Foundation Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "Harrogate and District NHS Foundation Trust"}],
        "description": "Harrogate and District's £3.039M establishment costs line covers postage, telephony, mobile-data, printing, stationery, recruitment advertising, subscriptions and minor sundries across the Harrogate District Hospital DGH and integrated North Yorkshire community-services footprint. The trust runs an integrated acute + community model under Humber and North Yorkshire ICS, broadening the corporate-services base above pure-acute peers. Industrial-action 2023-24 recruitment campaigns and regional EPR convergence feed 2024-25 spend.",
        "beneficiaries": "c. 4,500 WTE staff serving a c. 600,000 catchment (Harrogate, Knaresborough, Ripon and surrounding rural North Yorkshire); c. 70,000 ED attendances/yr at Harrogate District Hospital ED; c. 35,000 admissions/yr; integrated North Yorkshire community-services workforce broadens corporate-services baseline.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) — IAS 1 Presentation of Financial Statements — NHS Act 2006 — Health and Care Act 2022 — NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£3.039M"},
            {"label": "Trust scale", "value": "Harrogate District Hospital + integrated North Yorkshire community services; c. 4,500 WTE"},
            {"label": "Integrated acute + community", "value": "Trust runs North Yorkshire community services alongside acute — broadens recruitment + corporate-services base across rural community settings"},
            {"label": "Composition", "value": "Postage, telephony/mobile, printing, stationery, recruitment advertising, subscriptions, hospitality, minor sundries"},
            {"label": "EPR / Frontline Digitisation", "value": "Yorkshire and Humber regional EPR convergence under Frontline Digitisation drives change-mgmt + training-materials baseline"},
            {"label": "Industrial action 2023-24", "value": "Junior-doctor 44 days + consultant 10 days strikes drove recruitment-advertising spike + comms costs"},
            {"label": "April 2025 CPI uplift", "value": "Royal Mail + telecoms + advertising CPI feed forward unit-cost pressure"},
            {"label": "Funding trajectory", "value": "2021-22 c. £2.4M → 2023-24 c. £2.8M → 2024-25 £3.039M — sustained CPI + activity uplift"},
            {"label": "Delivery body", "value": "Trust Corporate Services + Procurement + IT + Crown Commercial Service framework (telecoms/postage)"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Humber and North Yorkshire ICB"},
            {"label": "Evaluation evidence", "value": "Model Hospital corporate-services benchmark; CQC RCD inspections; NHSE Yorkshire and Humber ICS group-model planning; Trust ARA 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2014 stand-alone acute + PCT community baselines · Successor: continued integrated-care embedding under Humber and North Yorkshire ICS + digital-comms shift"}
        ],
        "notes": "Harrogate and District's establishment-costs line carries the embedded back-office overhead of an integrated acute + community model under Humber and North Yorkshire ICS — the trust runs North Yorkshire community services alongside the Harrogate District Hospital DGH, broadening the recruitment-advertising and corporate-services base above pure-acute peers. Industrial action 2023-24 lifted recruitment-advertising spend through agency and substantive recruitment campaigns. Yorkshire and Humber regional EPR convergence sustains digital-training and comms baseline. Royal Mail postage uplifts and telecoms CPI feed forward unit-cost pressure into 2025-26.",
        "sources": [
            {"publisher": "Harrogate and District NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.hdft.nhs.uk/about-us/key-publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/connecting-health-and-care/frontline-digitisation/"},
            {"publisher": "Care Quality Commission", "title": "Harrogate and District provider profile (RCD)", "url": "https://www.cqc.org.uk/provider/RCD"},
            {"publisher": "National Audit Office", "title": "Progress in implementing the integration of health and social care", "url": "https://www.nao.org.uk/reports/progress-in-implementing-integrated-care/"}
        ],
        "related": ["Harrogate and District NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Establishment costs — Sherwood Forest Hospitals NHS Foundation Trust", "Establishment costs — Torbay and South Devon NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Transport (business + patient) — University Hospitals of Derby and Burton NHS Foundation Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "University Hospitals of Derby and Burton NHS Foundation Trust"}],
        "description": "UHDB's £3.034M transport line covers business mileage (AfC Section 17 + AMAP), pool-fleet IFRS 16 lease costs, NEPTS contract pass-through and patient travel reimbursements across the Royal Derby Hospital + Queen's Hospital Burton + Florence Nightingale + community-hospital five-site footprint following the July 2018 merger. Inter-site clinical transfers between Royal Derby (Major Trauma Unit + tertiary specialty hub) and Queen's Hospital Burton (DGH) generate substantial PTS demand, with NEPTS commissioned through Joined Up Care Derbyshire ICS lead-commissioner arrangement.",
        "beneficiaries": "c. 13,000 WTE staff serving a c. 600,000 Derbyshire and Staffordshire catchment plus tertiary specialty referrals; c. 230,000 ED attendances/yr (Royal Derby + Queen's Burton EDs combined); c. 130,000 admissions/yr; Royal Derby is regional Major Trauma Unit + cardiology + cancer-services tertiary hub.",
        "legal_basis": "NHS Act 2006 — NHSE Patient Transport Services Eligibility Criteria — Agenda for Change Section 17 (business mileage) — HMRC AMAP rates — IFRS 16 Leases (pool fleet) — DHSC Group Accounting Manual 2024-25 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£3.034M"},
            {"label": "Trust scale", "value": "Five-site (Royal Derby + Queen's Hospital Burton + Florence Nightingale + Sir Robert Peel + Samuel Johnson Lichfield) post-2018 merger; c. 13,000 WTE"},
            {"label": "Tertiary specialty hub", "value": "Royal Derby Major Trauma Unit + cardiology + cancer services — drives inter-site clinical-transfer demand from Burton DGH side"},
            {"label": "Composition", "value": "Business mileage (AfC S17 + AMAP 45p/25p) + pool-fleet IFRS 16 leases + NEPTS contract pass-through + patient travel reimbursements"},
            {"label": "NEPTS + community hospitals", "value": "Joined Up Care Derbyshire ICS + Staffordshire and Stoke-on-Trent ICS NEPTS arrangement; outsourced operator delivery; eligibility per NHSE 2021 criteria; Sir Robert Peel + Samuel Johnson Lichfield community hospitals broaden inter-site transfer base"},
            {"label": "AMAP rate context", "value": "HMRC AMAP rate frozen at 45p/mile (first 10k miles) since 2011 — real-terms erosion sustains internal-rate dispute pressure"},
            {"label": "Industrial action 2023-24 effect", "value": "Junior-doctor 44 days + consultant strikes drove agency travel-claim spikes + cancellation rebooking transport"},
            {"label": "Funding trajectory", "value": "2021-22 (post-merger) c. £2.5M → 2023-24 c. £2.85M → 2024-25 £3.034M — fuel CPI + activity recovery"},
            {"label": "Delivery body", "value": "Trust E&F + Travel team + outsourced NEPTS provider (Derbyshire + Staffordshire ICS arrangement) + pool-fleet leasing partner + Trust HR (mileage)"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + NHSE Urgent and Emergency Care (NEPTS) + Joined Up Care Derbyshire ICB + Staffordshire and Stoke-on-Trent ICB + DHSC"},
            {"label": "Evaluation evidence", "value": "NAO NEPTS context 2019; CQC RTG inspections; NHSE NEPTS Eligibility Review 2021; Trust ARA 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2018 separate Derby Hospitals + Burton Hospitals transport baselines · Successor: continued post-merger flow optimisation + cross-ICS NEPTS retender"}
        ],
        "notes": "UHDB's transport line carries the consequence of the July 2018 merger of Derby Hospitals NHS FT and Burton Hospitals NHS FT — Royal Derby's Major Trauma Unit and tertiary specialty services generate substantial inter-site patient-transport flows from the Burton DGH side, with the Sir Robert Peel and Samuel Johnson Lichfield community hospitals broadening the inter-site and community-team mileage base. NEPTS sits across two ICS commissioning arrangements (Joined Up Care Derbyshire and Staffordshire and Stoke-on-Trent) given the trust's cross-boundary footprint, with eligibility tightened under NHSE's 2021 criteria refresh. Industrial action 2023-24 lifted agency travel-claim and rebooking spend; HMRC AMAP-rate freeze (45p/mile since 2011) sustains internal-rate dispute pressure.",
        "sources": [
            {"publisher": "University Hospitals of Derby and Burton NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.uhdb.nhs.uk/annual-reports"},
            {"publisher": "NHS England", "title": "Non-Emergency Patient Transport Services — National Framework + Eligibility Criteria 2021", "url": "https://www.england.nhs.uk/publication/non-emergency-patient-transport-services-nepts/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "UHDB provider profile (RTG)", "url": "https://www.cqc.org.uk/provider/RTG"},
            {"publisher": "HM Revenue and Customs", "title": "AMAP rates and thresholds", "url": "https://www.gov.uk/expenses-and-benefits-business-travel-mileage/rules-for-tax"}
        ],
        "related": ["University Hospitals of Derby and Burton NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Transport (business + patient) — Mid and South Essex NHS Foundation Trust", "Transport (business + patient) — Lancashire Teaching Hospitals NHS Foundation Trust", "NHS England"]
    },
    "Establishment costs — The Dudley Group NHS Foundation Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "The Dudley Group NHS Foundation Trust"}],
        "description": "The Dudley Group's £3.018M establishment costs line covers postage, telephony, mobile-data, printing, stationery, recruitment advertising, subscriptions and minor sundries across the Russells Hall Hospital DGH (PFI-built, operational 2005) plus the Corbett Outpatient Centre and Guest Outpatient Centre community sites serving the Black Country. The Russells Hall PFI runs to 2041 and the trust operates within the Black Country ICS group context. Industrial-action 2023-24 recruitment campaigns and EPR rollout change-management feed 2024-25 spend.",
        "beneficiaries": "c. 4,500 WTE staff serving a c. 450,000 Dudley borough catchment plus surrounding Black Country flows; c. 110,000 ED attendances/yr at Russells Hall Hospital ED; c. 60,000 admissions/yr; main DGH (Russells Hall) plus Corbett + Guest community outpatient centres.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) — IAS 1 Presentation of Financial Statements — NHS Act 2006 — Health and Care Act 2022 — NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£3.018M"},
            {"label": "Trust scale", "value": "Russells Hall Hospital (PFI-built operational 2005) + Corbett Outpatient + Guest Outpatient; c. 4,500 WTE"},
            {"label": "PFI estate context", "value": "Russells Hall PFI signed 2003, operational 2005, expiry c. 2041 — high unitary-charge environment shapes back-office overhead allocation"},
            {"label": "Composition", "value": "Postage, telephony/mobile, printing, stationery, recruitment advertising, subscriptions, hospitality, minor sundries"},
            {"label": "EPR + Black Country ICS", "value": "Frontline Digitisation track drives change-mgmt + training-materials baseline; Black Country ICS group context (Sandwell + West Birmingham + Walsall + Wolverhampton trusts) shapes shared-services planning"},
            {"label": "Industrial action 2023-24", "value": "Junior-doctor 44 days + consultant 10 days strikes drove recruitment-advertising spike + comms costs"},
            {"label": "April 2025 CPI uplift", "value": "Royal Mail + telecoms + advertising CPI feed forward unit-cost pressure"},
            {"label": "Funding trajectory", "value": "2021-22 c. £2.4M → 2023-24 c. £2.8M → 2024-25 £3.018M — sustained CPI + activity uplift"},
            {"label": "Delivery body", "value": "Trust Corporate Services + Procurement + IT + Crown Commercial Service framework (telecoms/postage)"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Black Country ICB"},
            {"label": "Evaluation evidence", "value": "Model Hospital corporate-services benchmark; CQC RNA inspections; NAO PFI legacy reports; Trust ARA 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-PFI Russells Hall + Wordsley Hospital baseline · Successor: post-EPR digital-comms shift + 2041 PFI hand-back overhead reset"}
        ],
        "notes": "The Dudley Group's establishment-costs line carries the embedded back-office overhead of a single-DGH trust in the Black Country ICS — Russells Hall Hospital PFI (signed 2003, operational 2005, 2041 expiry) shapes the high-unitary-charge environment that pushes the trust to keep non-clinical overheads tight under recurrent affordability scrutiny. Industrial action 2023-24 lifted recruitment-advertising spend through agency and substantive recruitment campaigns. Frontline Digitisation EPR rollout sustains digital-training and comms baseline. Royal Mail postage uplifts and telecoms CPI feed forward unit-cost pressure into 2025-26. Black Country ICS shared-services planning across Sandwell + West Birmingham, Walsall and Wolverhampton is the medium-term lever for back-office consolidation.",
        "sources": [
            {"publisher": "The Dudley Group NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.dgft.nhs.uk/about-us/our-publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "National Audit Office", "title": "PFI and PF2 (HC 718, 2018)", "url": "https://www.nao.org.uk/reports/pfi-and-pf2/"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/connecting-health-and-care/frontline-digitisation/"},
            {"publisher": "Care Quality Commission", "title": "The Dudley Group provider profile (RNA)", "url": "https://www.cqc.org.uk/provider/RNA"}
        ],
        "related": ["The Dudley Group NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Establishment costs — Sherwood Forest Hospitals NHS Foundation Trust", "Establishment costs — Royal Berkshire NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Business rates — South Tyneside and Sunderland NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "South Tyneside and Sunderland NHS Foundation Trust"}],
        "description": "STSFT's £3.003M business-rates line covers non-domestic rates on the Sunderland Royal Hospital, the Sunderland Eye Infirmary precinct and South Tyneside District Hospital following the 2019 merger that brought South Tyneside into the Sunderland-led group. Hereditaments are assessed by the Valuation Office Agency on the 2023 Rating List with billing by Sunderland City Council and South Tyneside Council. NHS trusts pay the full multiplier with no charitable 80% relief, making rates a meaningful operating-cost item.",
        "beneficiaries": "c. 8,500 WTE staff serving a c. 600,000 Sunderland + South Tyneside catchment; c. 200,000 ED attendances/yr (Sunderland Royal + South Tyneside DH EDs combined); c. 100,000 admissions/yr; Sunderland Royal hosts regional stroke + emergency medicine + maternity; South Tyneside DH carries elective work + outpatients post-2019 reconfiguration.",
        "legal_basis": "Local Government Finance Act 1988 (Schedule 6) — Non-Domestic Rating (Multipliers and Private Finance) Act 2024 — Non-Domestic Rating Act 2023 — DHSC Group Accounting Manual 2024-25 — NHS Act 2006 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£3.003M"},
            {"label": "Trust scale", "value": "Sunderland Royal Hospital (c. 670 beds) + South Tyneside District Hospital + Sunderland Eye Infirmary; c. 8,500 WTE"},
            {"label": "Merger context", "value": "Apr 2019 merger of City Hospitals Sunderland NHS FT + South Tyneside NHS FT — single rating profile post-merger"},
            {"label": "Path to Excellence + billing", "value": "Post-2019 service reconfiguration concentrating emergency-medicine + maternity at Sunderland Royal; elective + outpatients at South Tyneside DH; billed by Sunderland City Council + South Tyneside Council"},
            {"label": "2023 revaluation", "value": "VOA 2023 revaluation (effective 1 Apr 2023) re-set rateable values from 2017 list — large transitional effects on multi-site hospitals"},
            {"label": "Multiplier 2024-25", "value": "Standard non-domestic multiplier 54.6p (England, 2024-25); NHS pays full rate (no charitable relief)"},
            {"label": "NDR 2024 Act context", "value": "Non-Domestic Rating (Multipliers and Private Finance) Act 2024 — multiplier-split + anti-avoidance reform"},
            {"label": "Funding trajectory", "value": "2021-22 (post-merger) c. £2.6M → 2023-24 (post-revaluation) c. £2.85M → 2024-25 £3.003M — multiplier + transitional uplift"},
            {"label": "Delivery body", "value": "Trust E&F (rates appeals) + Valuation Office Agency + Sunderland City Council + South Tyneside Council"},
            {"label": "Policy owner", "value": "MHCLG (NDR policy) + HM Treasury + DHSC + NHSE Provider Finance + North East and North Cumbria ICB"},
            {"label": "Evaluation evidence", "value": "VOA Rating List 2023; NAO Business Rates Reform; Trust ARA 2023-24; CQC R0B inspections"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2019 separate City Hospitals Sunderland + South Tyneside NHS FT rate baselines · Successor: 2026 revaluation cycle + NDR 2024 Act multiplier-split implementation"}
        ],
        "notes": "South Tyneside and Sunderland's rates line carries the consequence of the April 2019 merger and the subsequent Path to Excellence service reconfiguration — emergency medicine, maternity and stroke services concentrated at Sunderland Royal while South Tyneside District Hospital retained elective, outpatients and minor injuries — reshaping the rateable footprint across two billing authorities. The VOA 2023 revaluation lifted rateable values across the NHS estate with transitional relief tapering. NHS trusts cannot claim charitable 80% relief, so the full 54.6p standard multiplier applies. The Non-Domestic Rating (Multipliers and Private Finance) Act 2024 introduces multiplier splitting that affects future bills; appeals are managed via the Trust E&F team.",
        "sources": [
            {"publisher": "South Tyneside and Sunderland NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.stsft.nhs.uk/about-us/our-publications/annual-reports"},
            {"publisher": "Valuation Office Agency", "title": "2023 Rating List", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "Ministry of Housing, Communities and Local Government", "title": "Non-Domestic Rating Act 2023 + Multipliers and Private Finance Act 2024", "url": "https://www.gov.uk/government/collections/business-rates"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "STSFT provider profile (R0B)", "url": "https://www.cqc.org.uk/provider/R0B"}
        ],
        "related": ["South Tyneside and Sunderland NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Business rates — South Tees Hospitals NHS Foundation Trust", "Business rates — Portsmouth Hospitals University NHS Trust", "Valuation Office Agency"]
    },
    "Amortisation — The Princess Alexandra Hospital NHS Trust": {
        "aliases": [{"name": "Amortisation", "parent": "The Princess Alexandra Hospital NHS Trust"}],
        "description": "PAHT's £3.001M amortisation line covers the systematic write-down of intangible assets — capitalised software, EPR licences, internally-developed clinical applications and licensed IP — under IAS 38 across the Princess Alexandra Hospital Harlow main site plus St Margaret's Hospital Epping and Herts and Essex Hospital Bishop's Stortford community sites. PAHT is a New Hospital Programme cohort trust whose Harlow new-build was deferred under the January 2025 NHP Reset, with EPR rollout under NHSE's Frontline Digitisation programme driving capitalised intangible build through the line.",
        "beneficiaries": "c. 4,000 WTE staff serving a c. 350,000 West Essex + East Hertfordshire catchment (Harlow, Epping Forest, Uttlesford, East Herts); c. 100,000 ED attendances/yr at Princess Alexandra Hospital ED; c. 50,000 admissions/yr; main Harlow site plus St Margaret's Epping and Herts + Essex Bishop's Stortford community-clinic sites benefit from amortising digital infrastructure.",
        "legal_basis": "IAS 38 Intangible Assets — DHSC Group Accounting Manual 2024-25 (chapter 5 — Intangibles) — IFRIC SaaS configuration agenda decisions — NHS Act 2006 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£3.001M"},
            {"label": "Trust scale", "value": "Princess Alexandra Hospital (Harlow) + St Margaret's Hospital (Epping) + Herts and Essex Hospital (Bishop's Stortford); c. 4,000 WTE"},
            {"label": "Composition", "value": "Capitalised software + EPR licences + internally-developed clinical applications + licensed IP"},
            {"label": "EPR / Frontline Digitisation", "value": "PAHT Frontline Digitisation track — EPR (Alex Plus) capitalised build amortising over assessed UEL (5-10 years)"},
            {"label": "NHP cohort + Reset + estate", "value": "Harlow new-build originally in NHP 40-hospital programme (1960s estate replacement); Jan 2025 NHP Reset deferred construction; ageing-estate structural concerns feed capitalisation/impairment boundary debates"},
            {"label": "Useful economic life", "value": "Software 3-5 years; EPR / clinical-system 5-10 years per DHSC GAM ch.5 + IAS 38 review"},
            {"label": "IFRIC SaaS agenda decision", "value": "2021 IFRIC agenda decision on SaaS configuration costs — restricts capitalisation; some EPR programme spend now opex"},
            {"label": "Funding trajectory", "value": "2021-22 c. £2.4M → 2023-24 c. £2.8M → 2024-25 £3.001M — Frontline Digitisation amortisation cycle ramp"},
            {"label": "Delivery body", "value": "Trust IT + Finance (capitalisation) + EPR vendor + NHSE Frontline Digitisation programme"},
            {"label": "Policy owner", "value": "DHSC + NHSE Transformation Directorate + NHSE Provider Finance + Hertfordshire and West Essex ICB"},
            {"label": "Evaluation evidence", "value": "NAO Digital transformation in NHS 2020; DHSC GAM ch.5; NHP / IPA Major Projects Report; Trust ARA 2023-24; CQC RQW inspections"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-Frontline Digitisation legacy clinical-system amortisation tail · Successor: post-NHP-Reset deferred-rebuild + EPR-go-live amortisation peak"}
        ],
        "notes": "PAHT's amortisation line tracks intangible-asset stock during a difficult estate transition — Princess Alexandra Hospital Harlow's ageing 1960s estate carries flagged structural concerns that feed capitalisation/impairment boundary debates, while the long-promised Harlow new-build deferred under January 2025 NHP Reset preserves the existing site for the medium term. The Alex Plus EPR rollout under NHSE's Frontline Digitisation programme is the dominant capitalised-build driver, with assessed useful-economic-life of 5-10 years per DHSC GAM ch.5 and IAS 38. The 2021 IFRIC SaaS agenda decision restricts capitalisation of SaaS configuration costs, pushing some build spend into opex. Tangible-asset depreciation across the PAH estate sits in a separate line.",
        "sources": [
            {"publisher": "The Princess Alexandra Hospital NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.pah.nhs.uk/our-publications"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 5 — Intangibles)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/connecting-health-and-care/frontline-digitisation/"},
            {"publisher": "Department of Health and Social Care", "title": "New Hospital Programme — January 2025 Reset", "url": "https://www.gov.uk/government/publications/new-hospital-programme-plan-for-implementation"},
            {"publisher": "Care Quality Commission", "title": "PAHT provider profile (RQW)", "url": "https://www.cqc.org.uk/provider/RQW"}
        ],
        "related": ["The Princess Alexandra Hospital NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Amortisation — The Shrewsbury and Telford Hospital NHS Trust", "Amortisation — University Hospitals Sussex NHS Foundation Trust", "NHS England"]
    },
    "Transport (business + patient) — The Royal Wolverhampton NHS Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "The Royal Wolverhampton NHS Trust"}],
        "description": "Royal Wolverhampton's £2.991M transport line covers business mileage (AfC Section 17 + AMAP), pool-fleet IFRS 16 lease costs, NEPTS contract pass-through and patient travel reimbursements across the New Cross Hospital main acute site, the Cannock Chase Hospital DGH (acquired 2014) and the integrated Wolverhampton primary-care + community services. The trust's broad integrated acute + community + primary-care footprint under the Black Country ICS broadens the business-mileage base above peer DGH baselines, with NEPTS commissioned through the Black Country ICS lead-commissioner arrangement.",
        "beneficiaries": "c. 9,500 WTE staff serving a c. 470,000 Wolverhampton + Cannock catchment plus integrated primary-care registered list; c. 130,000 ED attendances/yr at New Cross Hospital ED; c. 80,000 admissions/yr; main New Cross site + Cannock Chase Hospital + integrated Vertical Integration primary-care GP practices.",
        "legal_basis": "NHS Act 2006 — NHSE Patient Transport Services Eligibility Criteria — Agenda for Change Section 17 (business mileage) — HMRC AMAP rates — IFRS 16 Leases (pool fleet) — DHSC Group Accounting Manual 2024-25 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£2.991M"},
            {"label": "Trust scale", "value": "New Cross Hospital + Cannock Chase Hospital + integrated Wolverhampton primary-care + community; c. 9,500 WTE"},
            {"label": "Vertical Integration + Cannock", "value": "RWT runs a portfolio of GP practices under Vertical Integration (Wolverhampton primary-care holding) and acquired Cannock Chase Hospital 2014 (former Mid Staffs site) — broadens business-mileage + inter-site transfer base across Wolverhampton + South Staffordshire"},
            {"label": "Composition", "value": "Business mileage (AfC S17 + AMAP 45p/25p) + pool-fleet IFRS 16 leases + NEPTS contract pass-through + patient travel reimbursements"},
            {"label": "NEPTS commissioning", "value": "Black Country ICS lead-commissioner NEPTS contract; outsourced operator delivery; eligibility per NHSE 2021 criteria"},
            {"label": "AMAP rate context", "value": "HMRC AMAP rate frozen at 45p/mile (first 10k miles) since 2011 — real-terms erosion sustains internal-rate dispute pressure"},
            {"label": "Industrial action 2023-24 effect", "value": "Junior-doctor 44 days + consultant 10 days strikes drove agency travel-claim spikes + cancellation rebooking transport"},
            {"label": "Funding trajectory", "value": "2021-22 c. £2.4M → 2023-24 c. £2.75M → 2024-25 £2.991M — fuel CPI + activity recovery"},
            {"label": "Delivery body", "value": "Trust E&F + Travel team + outsourced NEPTS provider (Black Country ICS lead-commissioner) + pool-fleet leasing partner + Trust HR (mileage)"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + NHSE Urgent and Emergency Care (NEPTS) + Black Country ICB + DHSC"},
            {"label": "Evaluation evidence", "value": "NAO NEPTS context 2019; CQC RL4 inspections; NHSE NEPTS Eligibility Review 2021; Vertical Integration evaluation studies; Trust ARA 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2014 separate Royal Wolverhampton + Mid Staffs Cannock baselines · Successor: continued Vertical Integration scaling + Black Country ICS-collaborative NEPTS retender"}
        ],
        "notes": "Royal Wolverhampton's transport baseline reflects an unusually broad integrated acute + community + primary-care footprint — the trust runs a portfolio of GP practices under its Vertical Integration model alongside the New Cross Hospital acute site and the Cannock Chase Hospital DGH (acquired 2014 from Mid Staffordshire NHS FT), broadening business-mileage and community-team transport demand above peer DGH baselines. NEPTS is commissioned through the Black Country ICS lead-commissioner arrangement, with eligibility tightened under NHSE's 2021 criteria refresh and outsourced operator delivery. Industrial action 2023-24 lifted agency travel-claim and rebooking spend; HMRC AMAP-rate freeze (45p/mile since 2011) sustains internal-rate dispute pressure.",
        "sources": [
            {"publisher": "The Royal Wolverhampton NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.royalwolverhampton.nhs.uk/about-us/our-publications/"},
            {"publisher": "NHS England", "title": "Non-Emergency Patient Transport Services — National Framework + Eligibility Criteria 2021", "url": "https://www.england.nhs.uk/publication/non-emergency-patient-transport-services-nepts/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "The Royal Wolverhampton NHS Trust provider profile (RL4)", "url": "https://www.cqc.org.uk/provider/RL4"},
            {"publisher": "Nuffield Trust", "title": "Vertical integration in the NHS — evidence and lessons", "url": "https://www.nuffieldtrust.org.uk/research/vertical-integration"}
        ],
        "related": ["The Royal Wolverhampton NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Transport (business + patient) — University Hospitals of Derby and Burton NHS Foundation Trust", "Transport (business + patient) — Blackpool Teaching Hospitals NHS Foundation Trust", "NHS England"]
    },
    "Business rates — University Hospitals Dorset NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "University Hospitals Dorset NHS Foundation Trust"}],
        "description": "UHD's £2.991M business-rates line covers non-domestic rates on the Royal Bournemouth Hospital, Poole Hospital and Christchurch Hospital sites following the October 2020 merger of Royal Bournemouth and Christchurch Hospitals NHS FT with Poole Hospital NHS FT. Hereditaments are assessed by the Valuation Office Agency on the 2023 Rating List and billed by BCP Council (Bournemouth, Christchurch and Poole unitary authority post-2019 LGR). NHS trusts pay the full multiplier with no charitable 80% relief, making rates a meaningful operating-cost item across the multi-site Dorset coastal footprint.",
        "beneficiaries": "c. 9,000 WTE staff serving a c. 800,000 Dorset coastal catchment (BCP + East Dorset); c. 180,000 ED attendances/yr (Royal Bournemouth + Poole EDs); c. 110,000 admissions/yr; multi-site (Royal Bournemouth + Poole + Christchurch) post-merger reconfigured under Bournemouth + Poole Reconfiguration programme.",
        "legal_basis": "Local Government Finance Act 1988 (Schedule 6) — Non-Domestic Rating (Multipliers and Private Finance) Act 2024 — Non-Domestic Rating Act 2023 — DHSC Group Accounting Manual 2024-25 — NHS Act 2006 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£2.991M"},
            {"label": "Trust scale", "value": "Royal Bournemouth Hospital + Poole Hospital + Christchurch Hospital (community); c. 9,000 WTE"},
            {"label": "Merger + BEACH", "value": "Oct 2020 merger of Royal Bournemouth and Christchurch Hospitals NHS FT + Poole Hospital NHS FT; in-flight BEACH reconfiguration (emergency-care + critical-care concentrating at Royal Bournemouth) reshapes rateable footprint as new builds come online"},
            {"label": "Billing authority", "value": "BCP Council (Bournemouth, Christchurch and Poole unitary, established Apr 2019 LGR)"},
            {"label": "2023 revaluation", "value": "VOA 2023 revaluation (effective 1 Apr 2023) re-set rateable values from 2017 list — large transitional effects on multi-site hospitals"},
            {"label": "Multiplier 2024-25", "value": "Standard non-domestic multiplier 54.6p (England, 2024-25); NHS pays full rate (no charitable relief)"},
            {"label": "NDR 2024 Act context", "value": "Non-Domestic Rating (Multipliers and Private Finance) Act 2024 — multiplier-split + anti-avoidance reform"},
            {"label": "Funding trajectory", "value": "2021-22 (post-merger) c. £2.6M → 2023-24 (post-revaluation) c. £2.85M → 2024-25 £2.991M — multiplier + transitional uplift; future BEACH-build effect"},
            {"label": "Delivery body", "value": "Trust E&F (rates appeals) + Valuation Office Agency + BCP Council"},
            {"label": "Policy owner", "value": "MHCLG (NDR policy) + HM Treasury + DHSC + NHSE Provider Finance + Dorset ICB"},
            {"label": "Evaluation evidence", "value": "VOA Rating List 2023; NAO Business Rates Reform; Trust ARA 2023-24; CQC inspections (RDZ)"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2020 separate Royal Bournemouth + Poole Hospital rate baselines · Successor: post-BEACH reconfiguration rate-list re-baselining + 2026 revaluation cycle"}
        ],
        "notes": "UHD's rates line carries the consequence of the October 2020 merger and the in-flight BEACH (Bournemouth Emergency and Critical Healthcare) reconfiguration — concentrating emergency-care and critical-care at Royal Bournemouth while Poole takes the major planned-care role — which is reshaping the rateable footprint as new build comes online and existing space is repurposed. The VOA 2023 revaluation lifted rateable values across the NHS estate with transitional relief tapering. NHS trusts cannot claim charitable 80% relief, so the full 54.6p standard multiplier applies. The Non-Domestic Rating (Multipliers and Private Finance) Act 2024 introduces multiplier splitting that affects future bills; appeals are managed via the Trust E&F team across the BCP Council billing authority.",
        "sources": [
            {"publisher": "University Hospitals Dorset NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.uhd.nhs.uk/about-us/our-publications/"},
            {"publisher": "Valuation Office Agency", "title": "2023 Rating List", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "Ministry of Housing, Communities and Local Government", "title": "Non-Domestic Rating Act 2023 + Multipliers and Private Finance Act 2024", "url": "https://www.gov.uk/government/collections/business-rates"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "UHD provider profile (RDZ)", "url": "https://www.cqc.org.uk/provider/RDZ"}
        ],
        "related": ["University Hospitals Dorset NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Business rates — University Hospital Southampton NHS Foundation Trust", "Business rates — South Tyneside and Sunderland NHS Foundation Trust", "Valuation Office Agency"]
    },
}
