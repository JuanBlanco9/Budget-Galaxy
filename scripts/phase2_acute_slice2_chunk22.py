# -*- coding: utf-8 -*-
# Phase 2 Acute slice 2 — chunk 22 (17 NHS Acute Trust orphan sub-lines)
# Hand-curated trust-specific PROGRAMME-archetype enrichment entries.
# Structural contract per docs/archetype_briefs.md.

NEW = {
    "Business rates — East Kent Hospitals University NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "East Kent Hospitals University NHS Foundation Trust"}],
        "description": "EKHUFT's £3.36M business-rates line covers non-domestic rating liability across the trust's multi-site Kent acute footprint — William Harvey (Ashford), Queen Elizabeth The Queen Mother (QEQM, Margate), Kent and Canterbury, plus Buckland and Royal Victoria community sites. Rates apply on hereditament rateable values set by the Valuation Office Agency, with the 2023 revaluation list driving the 2024-25 baseline. The trust is a Kent and Medway ICS member with cross-site activity transfer that touches multiple billing authorities (Ashford BC, Thanet DC, Canterbury CC).",
        "beneficiaries": "c. 8,000 WTE staff serving a c. 760,000 east Kent catchment (Ashford, Canterbury, Dover, Folkestone, Thanet); c. 200,000 ED attendances/yr across William Harvey + QEQM EDs; c. 95,000 admissions/yr; large rural + coastal-deprivation footprint.",
        "legal_basis": "Local Government Finance Act 1988 (Schedule 6) · Non-Domestic Rating Act 2023 · Non-Domestic Rating (Multipliers and Private Finance) Act 2024 · Rating (Empty Properties) Act 2007 · DHSC Group Accounting Manual 2024-25 · NHS Act 2006",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£3.36M"},
            {"label": "Trust scale", "value": "Three-site acute (William Harvey + QEQM + Kent and Canterbury) + community sites; c. 8,000 WTE"},
            {"label": "Billing authorities", "value": "Ashford BC + Thanet DC + Canterbury CC + Dover DC — multiple bills under multi-site footprint"},
            {"label": "Revaluation", "value": "2023 revaluation list (effective 1 Apr 2023) feeds 2024-25 transitional position; 2026 next revaluation"},
            {"label": "Multiplier 2024-25", "value": "Standard non-domestic rating multiplier 54.6p (England); Sch 6 RV-based liability"},
            {"label": "Mandatory + discretionary relief", "value": "NHS bodies do not qualify for mandatory charity relief; some hereditaments may receive discretionary relief from billing authority"},
            {"label": "RAAC context", "value": "QEQM Margate confirmed RAAC presence (2023 HSSIB list cohort); RAAC mitigation works affect rateable footprint"},
            {"label": "Funding trajectory", "value": "2021-22 c. £3.0M → 2023-24 £3.2M → 2024-25 £3.36M (revaluation + multiplier creep)"},
            {"label": "Delivery body", "value": "Trust E&F + Finance + VOA-set RV + multiple Kent billing authorities"},
            {"label": "Policy owner", "value": "MHCLG (rating policy) + HM Treasury + DHSC + Kent and Medway ICB"},
            {"label": "Evaluation evidence", "value": "VOA 2023 revaluation list; CQC inspection RVV (improvement-rated); NAO RAAC progress reports; Trust ARA"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2023 revaluation list baseline · Successor: 2026 revaluation + post-NDR 2024 Act split-multiplier reform"}
        ],
        "notes": "EKHUFT's rates baseline is set by the Valuation Office Agency 2023 revaluation list across a multi-site footprint that touches several Kent billing authorities — William Harvey (Ashford BC), QEQM (Thanet DC), Kent and Canterbury (Canterbury CC) and community-clinic sites. NHS bodies do not qualify for the mandatory 80% charity relief, so the full standard multiplier (54.6p in 2024-25 England) applies on the VOA-set rateable value. QEQM Margate's confirmed RAAC presence (2023 HSSIB cohort) drives mitigation works that interact with rateable footprint. The Non-Domestic Rating (Multipliers and Private Finance) Act 2024 introduces split-multiplier reforms feeding forward; the 2026 revaluation cycle will reset baseline.",
        "sources": [
            {"publisher": "East Kent Hospitals University NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.ekhuft.nhs.uk/patients-and-visitors/about-us/key-publications/annual-report-and-accounts/"},
            {"publisher": "Valuation Office Agency", "title": "Non-domestic rating: revaluation 2023", "url": "https://www.gov.uk/guidance/non-domestic-rates-revaluation-2023"},
            {"publisher": "Department for Levelling Up, Housing and Communities", "title": "Business rates: how your rateable value is calculated", "url": "https://www.gov.uk/introduction-to-business-rates"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "East Kent Hospitals provider profile (RVV)", "url": "https://www.cqc.org.uk/provider/RVV"}
        ],
        "related": ["East Kent Hospitals University NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Business rates — Barts Health NHS Trust", "Valuation Office Agency", "General supplies & services — East Kent Hospitals University NHS Foundation Trust"]
    },
    "Business rates — Frimley Health NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "Frimley Health NHS Foundation Trust"}],
        "description": "Frimley Health's £3.35M business-rates line covers non-domestic rating liability across a three-site acute footprint — Frimley Park Hospital (Surrey/Hampshire border), Wexham Park (Slough) and Heatherwood (Ascot), the latter rebuilt 2022 as a planned-care surgical centre. The trust spans the Frimley ICS catchment and is in NHP cohort 2 — Frimley Park rebuild was approved in the original 2020 New Hospital Programme but caught by the January 2025 Reset deferral, with Frimley pushed into the post-2030 wave. The 2023 VOA revaluation reflects the new Heatherwood footprint.",
        "beneficiaries": "c. 9,500 WTE staff serving a c. 900,000 catchment across Surrey, Hampshire, Berkshire, Buckinghamshire and south Bucks; c. 220,000 ED attendances/yr (Frimley Park + Wexham Park EDs); c. 100,000 admissions/yr; Frimley Park supports military Defence Medical Services (Camberley garrison).",
        "legal_basis": "Local Government Finance Act 1988 (Schedule 6) · Non-Domestic Rating Act 2023 · Non-Domestic Rating (Multipliers and Private Finance) Act 2024 · DHSC Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£3.35M"},
            {"label": "Trust scale", "value": "Three-site acute (Frimley Park + Wexham Park + Heatherwood); c. 9,500 WTE"},
            {"label": "Billing authorities", "value": "Surrey Heath BC (Frimley Park) + Slough BC (Wexham Park) + RBWM (Heatherwood, Ascot)"},
            {"label": "Heatherwood rebuild 2022", "value": "New Heatherwood Hospital opened Mar 2022 — rebuilt as planned-care surgical hub; new RV reflected in 2023 VOA list"},
            {"label": "NHP Reset Jan 2025", "value": "Frimley Park (RAAC + ageing fabric) pushed from 2030 cohort to post-2030 wave under DHSC NHP Reset"},
            {"label": "RAAC context", "value": "Frimley Park confirmed RAAC presence (2023 HSSIB list cohort); mitigation works affect rateable footprint + decant transport"},
            {"label": "Multiplier 2024-25", "value": "Standard non-domestic rating multiplier 54.6p (England)"},
            {"label": "Funding trajectory", "value": "2021-22 c. £2.9M → 2022-23 step-up post-Heatherwood opening → 2024-25 £3.35M"},
            {"label": "Delivery body", "value": "Trust E&F + Finance + VOA-set RV + Surrey Heath BC + Slough BC + RBWM"},
            {"label": "Policy owner", "value": "MHCLG (rating policy) + HM Treasury + DHSC + Frimley ICB + Buckinghamshire, Oxfordshire and Berkshire West ICB"},
            {"label": "Evaluation evidence", "value": "VOA 2023 list; NHP Reset announcement Jan 2025; CQC inspection RDU; Trust ARA"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2022 legacy Heatherwood + pre-2014 Heatherwood and Wexham Park Hospitals NHS FT (acquired by Frimley) · Successor: 2026 revaluation + post-NHP Reset rebuild"}
        ],
        "notes": "Frimley Health's rates baseline reflects the 2022 opening of the new Heatherwood Hospital — a planned-care surgical hub rebuilt to specification — alongside the larger Frimley Park (RAAC-affected) and Wexham Park sites. The 2014 acquisition of Heatherwood and Wexham Park NHS FT consolidated the current three-site footprint. The January 2025 NHP Reset announcement pushed Frimley Park's full rebuild from the original 2030 cohort into the post-2030 wave despite confirmed RAAC presence, leaving the trust managing mitigation works and decant on the existing rateable footprint. The 2024 NDR multiplier reform and 2026 revaluation will reshape the forward trajectory.",
        "sources": [
            {"publisher": "Frimley Health NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.fhft.nhs.uk/about-us/corporate-information/annual-report-and-accounts/"},
            {"publisher": "Department of Health and Social Care", "title": "New Hospital Programme: plan for implementation (Jan 2025 Reset)", "url": "https://www.gov.uk/government/publications/new-hospital-programme-plan-for-implementation"},
            {"publisher": "Valuation Office Agency", "title": "Non-domestic rating: revaluation 2023", "url": "https://www.gov.uk/guidance/non-domestic-rates-revaluation-2023"},
            {"publisher": "National Audit Office", "title": "Progress with the New Hospital Programme (HC 1662, 2023)", "url": "https://www.nao.org.uk/reports/progress-with-the-new-hospital-programme/"},
            {"publisher": "Care Quality Commission", "title": "Frimley Health provider profile (RDU)", "url": "https://www.cqc.org.uk/provider/RDU"}
        ],
        "related": ["Frimley Health NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "New Hospital Programme", "Business rates — East Kent Hospitals University NHS Foundation Trust", "Valuation Office Agency"]
    },
    "Business rates — East Suffolk and North Essex NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "East Suffolk and North Essex NHS Foundation Trust"}],
        "description": "ESNEFT's £3.35M business-rates line covers non-domestic rating liability across the trust's two main acute sites — Ipswich Hospital (Suffolk) and Colchester Hospital (Essex) — plus Clacton, Harwich and a community-clinic footprint. ESNEFT was formed in July 2018 by merger of Ipswich Hospital NHS Trust with Colchester Hospital University NHS FT, creating one of the largest NHS organisations in the East of England. Rates are billed by Ipswich BC, Colchester CC and Tendring DC against VOA 2023-list rateable values.",
        "beneficiaries": "c. 10,000 WTE staff serving a c. 1.0M east Suffolk and north Essex catchment; c. 200,000 ED attendances/yr (Ipswich + Colchester EDs); c. 110,000 admissions/yr; mixed urban + rural + coastal footprint with high elderly demographic.",
        "legal_basis": "Local Government Finance Act 1988 (Schedule 6) · Non-Domestic Rating Act 2023 · Non-Domestic Rating (Multipliers and Private Finance) Act 2024 · DHSC Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£3.35M"},
            {"label": "Trust scale", "value": "Two main acute sites (Ipswich + Colchester) + Clacton + Harwich + community; c. 10,000 WTE"},
            {"label": "Billing authorities", "value": "Ipswich BC + Colchester CC + Tendring DC (Clacton, Harwich) — multi-billing-authority footprint"},
            {"label": "Merger 2018", "value": "Formed Jul 2018 by merger of Ipswich Hospital NHS Trust + Colchester Hospital University NHS FT"},
            {"label": "Multiplier 2024-25", "value": "Standard non-domestic rating multiplier 54.6p (England)"},
            {"label": "Revaluation cycle", "value": "2023 VOA list effective Apr 2023; 2026 revaluation cycle next reset"},
            {"label": "ICS context", "value": "Suffolk and North East Essex ICB — one of NHSE's stronger integrated-care performers (CQC + NHSE assurance)"},
            {"label": "Funding trajectory", "value": "2021-22 c. £3.0M → 2024-25 £3.35M (revaluation + multiplier creep)"},
            {"label": "Delivery body", "value": "Trust E&F + Finance + VOA-set RV + Ipswich BC + Colchester CC + Tendring DC"},
            {"label": "Policy owner", "value": "MHCLG (rating policy) + HM Treasury + DHSC + Suffolk and North East Essex ICB"},
            {"label": "Evaluation evidence", "value": "CQC inspection RDE (Good-rated); VOA 2023 list; HSSIB / SNEE ICB assurance reports; Trust ARA"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2018 separate Ipswich + Colchester rating baselines · Successor: 2026 revaluation + post-NDR 2024 Act"}
        ],
        "notes": "ESNEFT's rates baseline reflects the multi-site footprint inherited from the July 2018 merger of Ipswich Hospital NHS Trust with Colchester Hospital University NHS FT — the trust now spans Ipswich BC, Colchester CC and Tendring DC billing authorities. The 2023 VOA revaluation reset baseline rateable values; the 2026 revaluation cycle is the next reset. Suffolk and North East Essex ICB has been one of NHSE's stronger integrated-care performers, and ESNEFT's CQC Good rating reflects the merger's operational consolidation. The Non-Domestic Rating (Multipliers and Private Finance) Act 2024 introduces split-multiplier reforms for higher-RV hereditaments feeding forward.",
        "sources": [
            {"publisher": "East Suffolk and North Essex NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.esneft.nhs.uk/about-us/our-publications/"},
            {"publisher": "Valuation Office Agency", "title": "Non-domestic rating: revaluation 2023", "url": "https://www.gov.uk/guidance/non-domestic-rates-revaluation-2023"},
            {"publisher": "Department for Levelling Up, Housing and Communities", "title": "Business rates: introduction", "url": "https://www.gov.uk/introduction-to-business-rates"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "ESNEFT provider profile (RDE)", "url": "https://www.cqc.org.uk/provider/RDE"}
        ],
        "related": ["East Suffolk and North Essex NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Business rates — Frimley Health NHS Foundation Trust", "General supplies & services — East Suffolk and North Essex NHS Foundation Trust", "Valuation Office Agency"]
    },
    "Establishment costs — Bradford Teaching Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "Bradford Teaching Hospitals NHS Foundation Trust"}],
        "description": "Bradford Teaching Hospitals' £3.30M establishment costs line covers stationery, office supplies, postage, telephony, printing and minor admin sundries below the trust's capitalisation threshold across the Bradford Royal Infirmary and St Luke's Hospital footprint. The trust is in the NHP cohort 1 with Airedale and Leeds Teaching among the original 40-hospitals programme — Airedale's RAAC + ageing fabric is the regional driver, with West Yorkshire ICS group-model planning shaping shared back-office consolidation that touches establishment-cost baselines.",
        "beneficiaries": "c. 6,000 WTE staff serving a c. 540,000 Bradford district catchment with very high IMD deprivation and a young, ethnically diverse population; c. 145,000 ED attendances/yr at BRI ED; c. 70,000 admissions/yr; large maternity service (c. 5,500 deliveries/yr) and Bradford Institute for Health Research home of Born in Bradford cohort.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25 · Procurement Act 2023",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£3.30M"},
            {"label": "Trust scale", "value": "Two-site acute (Bradford Royal Infirmary + St Luke's); c. 6,000 WTE"},
            {"label": "Composition", "value": "Stationery + postage + telephony + print + minor office sundries below capitalisation threshold"},
            {"label": "Born in Bradford context", "value": "Bradford Institute for Health Research hosts Born in Bradford cohort study (c. 13,500 children) — research admin baseline contributes"},
            {"label": "Frontline Digitisation EPR", "value": "Cerner Millennium adopted; FD programme reduces stationery + print spend over time as EPR matures"},
            {"label": "Industrial action 2023-24 effect", "value": "Strike days drove communications + admin churn"},
            {"label": "ICS context", "value": "West Yorkshire ICS — six trusts across the patch; shared back-office and procurement collaborative shape medium-term establishment baseline"},
            {"label": "Funding trajectory", "value": "2021-22 c. £2.8M → 2023-24 £3.1M → 2024-25 £3.30M — sustained CPI + activity uplift"},
            {"label": "Delivery body", "value": "Trust Procurement + Comms + IT + Estates + WY ICS shared services"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + West Yorkshire ICB"},
            {"label": "Evaluation evidence", "value": "CQC inspection RAE; Model Hospital establishment-cost benchmarks; FD digitisation programme returns; Trust ARA"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-FD paper-heavy admin baseline · Successor: post-FD digital-first admin + WY ICS shared back-office"}
        ],
        "notes": "Bradford Teaching Hospitals' establishment baseline reflects a two-site acute footprint serving one of England's most deprived metropolitan populations, with a high-volume maternity service (c. 5,500 deliveries/yr) and the Bradford Institute for Health Research hosting the Born in Bradford cohort study. Cerner Millennium EPR adoption under Frontline Digitisation reduces print and stationery over time, but the transition pathway sustains a hybrid baseline. West Yorkshire ICS group-model shared back-office and procurement collaborative — six trusts across the patch — is the medium-term lever. April 2025 NIC step-up affects external admin contractors via pass-through. Industrial action 2023-24 added comms + admin churn.",
        "sources": [
            {"publisher": "Bradford Teaching Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.bradfordhospitals.nhs.uk/about-us/key-publications/annual-reports/"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/connecting-health-and-care/frontline-digitisation/"},
            {"publisher": "Bradford Institute for Health Research", "title": "Born in Bradford cohort", "url": "https://borninbradford.nhs.uk/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Bradford Teaching Hospitals provider profile (RAE)", "url": "https://www.cqc.org.uk/provider/RAE"}
        ],
        "related": ["Bradford Teaching Hospitals NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Establishment costs — Kettering General Hospital NHS Foundation Trust", "General supplies & services — Bradford Teaching Hospitals NHS Foundation Trust", "NHS England"]
    },
    "Amortisation — East And North Hertfordshire NHS Trust": {
        "aliases": [{"name": "Amortisation", "parent": "East And North Hertfordshire NHS Trust"}],
        "description": "East And North Herts' £3.28M amortisation line reflects systematic write-down of capitalised intangible assets — predominantly EPR / clinical software, licences, software development costs and intangibles arising from Frontline Digitisation — across the Lister Hospital (Stevenage) main acute site, Hertford County Hospital, New QEII and Mount Vernon Cancer Centre. The trust runs Mount Vernon Cancer Centre on behalf of multiple ICBs, embedding cancer-IT systems with their own capitalised software stack feeding the amortisation baseline.",
        "beneficiaries": "c. 5,500 WTE staff serving a c. 600,000 east and north Hertfordshire catchment plus extended Mount Vernon cancer-network referrals across Beds, Bucks, Herts, NW London; c. 130,000 ED attendances/yr at Lister ED; c. 60,000 admissions/yr; Mount Vernon serves c. 8,000 new cancer patients/yr.",
        "legal_basis": "IAS 38 Intangible Assets · DHSC Group Accounting Manual 2024-25 ch.5 · IFRS 16 (interaction on cloud-SaaS arrangements) · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£3.28M"},
            {"label": "Trust scale", "value": "Lister + Hertford County + New QEII + Mount Vernon Cancer Centre; c. 5,500 WTE"},
            {"label": "Composition", "value": "Capitalised EPR + clinical software + cancer-IT + licences + software development — IAS 38 systematic amortisation"},
            {"label": "EPR context", "value": "Cerner Millennium implementation under Frontline Digitisation; capitalised cost amortised over c. 5-10yr useful life"},
            {"label": "Mount Vernon Cancer Centre", "value": "Hosted by E&NH on behalf of multi-ICB cancer network (c. 2.0M catchment); cancer-specific IT capitalised software stack contributes"},
            {"label": "Useful economic life", "value": "Software/licences typically 3-7yr; bespoke EPR clinical config typically 7-10yr per DHSC GAM ch.5"},
            {"label": "Frontline Digitisation funding", "value": "FD national programme central capital + trust-funded; capitalised costs feed 5-10yr amortisation cycle"},
            {"label": "Funding trajectory", "value": "Rising amortisation as FD-era EPR + cancer-IT capitalisation matures; c. £2.8M 2021-22 → £3.28M 2024-25"},
            {"label": "Delivery body", "value": "Trust IT + Finance + EPR programme team + Cerner / Oracle Health partnership"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC GAM + NHSE Frontline Digitisation programme + Hertfordshire and West Essex ICB"},
            {"label": "Evaluation evidence", "value": "NHSE FD programme returns; CQC inspection RWH; NAO Digital transformation reports; Trust ARA intangible-assets note"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-FD legacy clinical-systems amortisation · Successor: full-mature FD EPR cycle + cloud-SaaS IFRS 16 interaction"}
        ],
        "notes": "East And North Herts' amortisation profile reflects the layered intangibles base from Frontline Digitisation EPR rollout (Cerner Millennium) plus Mount Vernon Cancer Centre's capitalised cancer-IT stack — Mount Vernon serves a multi-ICB cancer network (c. 2.0M catchment) and embeds cancer-specific systems alongside the trust's main EPR. IAS 38 systematic amortisation runs over 3-7yr for software/licences and 7-10yr for bespoke EPR clinical configuration per DHSC GAM ch.5. The cloud-SaaS shift (IFRS 16 interaction) reshapes mix between intangibles amortisation and right-of-use depreciation as new contracts arrive. NHP Reset January 2025 affects medium-term capitalisation cycle for new clinical builds.",
        "sources": [
            {"publisher": "East And North Hertfordshire NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.enherts-tr.nhs.uk/about-us/key-documents/"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/connecting-health-and-care/frontline-digitisation/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 5 — Intangible assets)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "National Audit Office", "title": "Digital transformation in the NHS (HC 1591, 2020)", "url": "https://www.nao.org.uk/reports/the-use-of-digital-technology-in-the-nhs/"},
            {"publisher": "Care Quality Commission", "title": "East And North Herts provider profile (RWH)", "url": "https://www.cqc.org.uk/provider/RWH"}
        ],
        "related": ["East And North Hertfordshire NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Mount Vernon Cancer Centre", "Amortisation — University College London Hospitals NHS Foundation Trust", "NHS England"]
    },
    "Transport (business + patient) — Northern Lincolnshire and Goole NHS Foundation Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "Northern Lincolnshire and Goole NHS Foundation Trust"}],
        "description": "NLAG's £3.27M transport line covers business mileage, inter-site patient transfers and NEPTS across the three-site Humber footprint — Diana Princess of Wales (Grimsby), Scunthorpe General and Goole. The dispersed rural + coastal footprint and Humber estuary split drive inter-hospital PTS demand, with EMAS PTS contractors and trust pool fleet covering AHP and community-team mileage. The trust is in active group-arrangement discussions with Hull University Teaching Hospitals via the Humber Acute Services Programme.",
        "beneficiaries": "c. 6,500 WTE staff serving a c. 410,000 north + north-east Lincolnshire + East Riding (Goole) catchment; c. 130,000 ED attendances/yr (Grimsby + Scunthorpe EDs); c. 60,000 admissions/yr; Goole functions as planned-care site with significant inter-site transfer demand to Grimsby/Scunthorpe.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · IFRS 16 Leases (pool fleet) · NHS Act 2006 · NHSE Patient Transport Services Eligibility Framework 2022 · HMRC AMAP · NHS AfC Section 17 · Mental Health Act 1983 (s.135/136 conveyance)",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£3.27M"},
            {"label": "Trust scale", "value": "Three-site acute (Grimsby + Scunthorpe + Goole) across Humber + East Riding; c. 6,500 WTE"},
            {"label": "Geography", "value": "Dispersed rural + coastal footprint; Humber estuary split between sites — drives high inter-site PTS demand"},
            {"label": "Group-arrangement context", "value": "Active discussions with Hull University Teaching Hospitals via Humber Acute Services Programme — shapes medium-term transport pooling"},
            {"label": "PTS provider mix", "value": "EMAS PTS + accredited NEPTS contractors + trust pool fleet (AHP + community-team mileage)"},
            {"label": "Pool fleet (IFRS 16)", "value": "Right-of-use depreciation + interest on leased pool vehicles"},
            {"label": "Staff mileage rate", "value": "AfC Section 17 / HMRC AMAP 45p first 10,000 miles + 25p thereafter"},
            {"label": "Funding trajectory", "value": "2021-22 c. £2.7M → 2023-24 £3.1M → 2024-25 £3.27M — fuel CPI + activity recovery"},
            {"label": "Delivery body", "value": "Trust E&F + Travel team + EMAS PTS + accredited NEPTS contractors"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + NHSE NEPTS framework + Humber and North Yorkshire ICB"},
            {"label": "Evaluation evidence", "value": "NHSE NEPTS Eligibility Framework 2022 review; CQC inspection RJL; HASR review reports; Trust ARA"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2001 separate Grimsby + Scunthorpe baselines · Successor: post-HASR Hull/NLAG group arrangements"}
        ],
        "notes": "NLAG's transport baseline is structurally elevated by the three-site Humber footprint — Diana Princess of Wales (Grimsby), Scunthorpe General and Goole + District — with the Humber estuary geography forcing inter-site PTS demand for clinical pathways requiring transfer between Grimsby/Scunthorpe and tertiary services across the Humber to Hull. Goole's planned-care function adds further inter-site flow. The Humber Acute Services Review programme and active group-arrangement discussions with Hull University Teaching Hospitals shape the medium-term transport vehicle. April 2025 NIC step-up affects PTS-contractor pass-through; CPI fuel pressure remains the dominant driver. EV transition and ICS shared-fleet pooling are medium-term levers.",
        "sources": [
            {"publisher": "Northern Lincolnshire and Goole NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.nlg.nhs.uk/about-us/key-documents/"},
            {"publisher": "NHS England", "title": "Non-Emergency Patient Transport Services Eligibility Framework 2022", "url": "https://www.england.nhs.uk/long-read/non-emergency-patient-transport-services-eligibility-framework/"},
            {"publisher": "Humber and North Yorkshire ICB", "title": "Humber Acute Services Programme", "url": "https://humberandnorthyorkshire.icb.nhs.uk/our-work/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "NLAG provider profile (RJL)", "url": "https://www.cqc.org.uk/provider/RJL"}
        ],
        "related": ["Northern Lincolnshire and Goole NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Hull University Teaching Hospitals NHS Trust", "Transport (business + patient) — Imperial College Healthcare NHS Trust", "Department of Health and Social Care"]
    },
    "Establishment costs — Kettering General Hospital NHS Foundation Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "Kettering General Hospital NHS Foundation Trust"}],
        "description": "Kettering General Hospital's £3.25M establishment costs line covers stationery, postage, telephony, print and minor admin sundries below the trust's capitalisation threshold at the single-site DGH serving north Northamptonshire. KGH is in NHP cohort 1 (original 40-hospitals programme) — the trust holds Strategic Outline Case approval for full rebuild but caught by the January 2025 Reset deferral, with construction now post-2030. The trust shares group-model arrangements with Northampton General Hospital under the University Hospitals of Northamptonshire group form.",
        "beneficiaries": "c. 4,500 WTE staff serving a c. 320,000 north Northamptonshire catchment (Kettering, Corby, Wellingborough, Rushden); c. 100,000 ED attendances/yr at KGH ED; c. 50,000 admissions/yr; large maternity service.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25 · Procurement Act 2023",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£3.25M"},
            {"label": "Trust scale", "value": "Single-site DGH (Kettering); c. 4,500 WTE"},
            {"label": "Composition", "value": "Stationery + postage + telephony + print + minor office sundries below capitalisation threshold"},
            {"label": "NHP cohort 1", "value": "Original 40-hospitals programme — Strategic Outline Case approved; caught by Jan 2025 NHP Reset deferral; construction post-2030"},
            {"label": "Group-model UH Northamptonshire", "value": "Group form with Northampton General Hospital — shared back-office + chair-in-common; reshapes establishment baseline trajectory"},
            {"label": "Frontline Digitisation EPR", "value": "Nervecentre + capitalised digital programme reduces print/stationery over time"},
            {"label": "Industrial action 2023-24 effect", "value": "Strike days drove additional comms + admin churn"},
            {"label": "Funding trajectory", "value": "2021-22 c. £2.8M → 2023-24 £3.1M → 2024-25 £3.25M — sustained CPI + admin uplift"},
            {"label": "Delivery body", "value": "Trust Procurement + Comms + IT + Estates + UH Northamptonshire shared services"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + NHP delivery body + Northamptonshire ICB"},
            {"label": "Evaluation evidence", "value": "CQC inspection RNQ (improvement-rated); NAO NHP progress reports; Trust ARA disclosure"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2018 stand-alone trust establishment baseline · Successor: post-NHP rebuild + UH Northamptonshire group consolidation"}
        ],
        "notes": "Kettering General Hospital's establishment baseline reflects a single-site DGH operating from 1897-era Victorian fabric augmented with later builds — the trust holds approved Strategic Outline Case for full rebuild under New Hospital Programme cohort 1, but the January 2025 NHP Reset announcement deferred construction beyond 2030 leaving KGH continuing operation from ageing fabric with sustained admin and comms baseline. Group-model arrangements with Northampton General Hospital under the University Hospitals of Northamptonshire group form share back-office functions and chair-in-common, reshaping medium-term establishment trajectory. Nervecentre EPR adoption and Frontline Digitisation reduce print/stationery over time; April 2025 NIC step-up affects external admin contractor pass-through.",
        "sources": [
            {"publisher": "Kettering General Hospital NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.kgh.nhs.uk/annualreports"},
            {"publisher": "Department of Health and Social Care", "title": "New Hospital Programme: plan for implementation (Jan 2025 Reset)", "url": "https://www.gov.uk/government/publications/new-hospital-programme-plan-for-implementation"},
            {"publisher": "National Audit Office", "title": "Progress with the New Hospital Programme (HC 1662, 2023)", "url": "https://www.nao.org.uk/reports/progress-with-the-new-hospital-programme/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Kettering General Hospital provider profile (RNQ)", "url": "https://www.cqc.org.uk/provider/RNQ"}
        ],
        "related": ["Kettering General Hospital NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "New Hospital Programme", "Northampton General Hospital NHS Trust", "Establishment costs — Bradford Teaching Hospitals NHS Foundation Trust"]
    },
    "Business rates — North Middlesex University Hospital NHS Trust": {
        "aliases": [{"name": "Business rates", "parent": "North Middlesex University Hospital NHS Trust"}],
        "description": "North Middlesex's £3.24M business-rates line covers non-domestic rating liability on the single-site Sterling Way, Edmonton hereditament — billed by Enfield Council against the Valuation Office Agency 2023-list rateable value. The trust is in active merger transaction with Royal Free London NHS FT under the North Central London ICS group model; merger completion will consolidate billing within Royal Free Group's portfolio though the rateable hereditament remains site-specific.",
        "beneficiaries": "c. 3,500 WTE staff serving a c. 350,000 Enfield and Haringey catchment with very high IMD deprivation; c. 200,000 ED attendances/yr (one of London's busiest single-site EDs); c. 65,000 admissions/yr; large maternity unit (c. 4,500 deliveries/yr).",
        "legal_basis": "Local Government Finance Act 1988 (Schedule 6) · Non-Domestic Rating Act 2023 · Non-Domestic Rating (Multipliers and Private Finance) Act 2024 · DHSC Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£3.24M"},
            {"label": "Trust scale", "value": "Single-site DGH (Sterling Way, Edmonton); c. 3,500 WTE"},
            {"label": "Billing authority", "value": "Enfield Council — single hereditament rates bill"},
            {"label": "Royal Free merger context", "value": "Transaction with Royal Free London NHS FT progressing 2023-25; targets group-model integration under NCL ICS"},
            {"label": "Multiplier 2024-25", "value": "Standard non-domestic rating multiplier 54.6p (England)"},
            {"label": "Revaluation cycle", "value": "2023 VOA list (effective Apr 2023); 2026 next revaluation"},
            {"label": "Catchment deprivation", "value": "Enfield + Haringey — high IMD deprivation drives elevated ED + maternity volume"},
            {"label": "Funding trajectory", "value": "2021-22 c. £2.9M → 2023-24 £3.1M → 2024-25 £3.24M (revaluation + multiplier creep)"},
            {"label": "Delivery body", "value": "Trust E&F + Finance + VOA-set RV + Enfield Council billing"},
            {"label": "Policy owner", "value": "MHCLG (rating policy) + HM Treasury + DHSC + North Central London ICB"},
            {"label": "Evaluation evidence", "value": "VOA 2023 list; CQC inspection RAP; NCL ICS group-model business case; Trust ARA"},
            {"label": "Predecessor / successor", "value": "Predecessor: stand-alone trust pre-merger rates baseline · Successor: post-merger Royal Free Group consolidated billing"}
        ],
        "notes": "North Middlesex's rates baseline reflects the single Sterling Way, Edmonton hereditament billed by Enfield Council against the VOA 2023-list rateable value. NHS bodies do not qualify for mandatory charity relief, so the full standard 54.6p multiplier applies. The active merger transaction with Royal Free London NHS FT — one of NHSE's flagship North Central London ICS group-model transactions — will consolidate billing within Royal Free Group's portfolio though the hereditament remains site-specific. The 2026 revaluation cycle and the Non-Domestic Rating (Multipliers and Private Finance) Act 2024 split-multiplier reforms feed forward. North Mid's site sits in one of London's most deprived catchments, sustaining among the busiest single-site ED volumes in the capital.",
        "sources": [
            {"publisher": "North Middlesex University Hospital NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.northmid.nhs.uk/annual-reports"},
            {"publisher": "Valuation Office Agency", "title": "Non-domestic rating: revaluation 2023", "url": "https://www.gov.uk/guidance/non-domestic-rates-revaluation-2023"},
            {"publisher": "NHS England", "title": "North Central London ICS group-model transaction (Royal Free + North Mid)", "url": "https://www.england.nhs.uk/london/our-work/north-central-london/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "North Middlesex provider profile (RAP)", "url": "https://www.cqc.org.uk/provider/RAP"}
        ],
        "related": ["North Middlesex University Hospital NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Royal Free London NHS Foundation Trust", "Business rates — East Suffolk and North Essex NHS Foundation Trust", "Valuation Office Agency"]
    },
    "Amortisation — University College London Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Amortisation", "parent": "University College London Hospitals NHS Foundation Trust"}],
        "description": "UCLH's £3.23M amortisation line reflects systematic IAS 38 write-down of capitalised intangibles — Epic EPR (one of the NHS's flagship Epic implementations, go-live 2019), specialist clinical software, capitalised software development and licences. UCLH operates as one of London's largest specialist acute providers across the Tottenham Court Road campus (UCH, NHNN Queen Square, RLHIM, Eastman Dental, UCH Macmillan) plus Westmoreland Street, with research-active intangibles from joint-UCL programmes.",
        "beneficiaries": "c. 12,000 WTE staff serving a c. 1.0M central + north London catchment plus extensive tertiary specialty referrals national/international (neurosciences via NHNN, cancer via UCH, women's via EGA UCH); c. 200,000 ED attendances/yr at UCH ED; c. 130,000 admissions/yr; UCH BRC is one of the largest NIHR Biomedical Research Centres.",
        "legal_basis": "IAS 38 Intangible Assets · DHSC Group Accounting Manual 2024-25 ch.5 · IFRS 16 (cloud-SaaS interaction) · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£3.23M"},
            {"label": "Trust scale", "value": "Multi-site academic acute (UCH + NHNN Queen Square + RNTNEH + RLHIM + Eastman Dental + UCH Macmillan + Westmoreland Street); c. 12,000 WTE"},
            {"label": "Composition", "value": "Capitalised Epic EPR + specialist clinical software + research IT + licences + capitalised software development"},
            {"label": "Epic EPR context", "value": "Epic go-live Apr 2019 — one of the NHS's flagship Epic deployments under Frontline Digitisation; capitalised cost amortised c. 7-10yr useful life"},
            {"label": "Specialty IT stack", "value": "NHNN neurosciences + UCH Macmillan cancer + EGA women's + Eastman Dental — specialist capitalised systems contribute"},
            {"label": "BRC research IT", "value": "NIHR UCLH BRC research-IT capitalised costs feed amortisation as projects close to capital"},
            {"label": "Useful economic life", "value": "Software/licences typically 3-7yr; bespoke EPR clinical config 7-10yr per DHSC GAM ch.5"},
            {"label": "Funding trajectory", "value": "Mature post-Epic-go-live amortisation cycle; c. £3.0M 2021-22 → £3.23M 2024-25"},
            {"label": "Delivery body", "value": "Trust IT + Finance + Epic programme team + UCLH BRC technology core"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC GAM + NHSE Frontline Digitisation programme + North Central London ICB"},
            {"label": "Evaluation evidence", "value": "NHSE FD programme returns; CQC inspection RRV (Outstanding-rated); NAO Digital transformation reports; Trust ARA intangibles note"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2019 multi-system clinical-IT amortisation · Successor: full-mature Epic cycle + cloud-SaaS IFRS 16 interaction + post-NHP capital"}
        ],
        "notes": "UCLH's amortisation profile is shaped by the April 2019 Epic EPR go-live — one of the NHS's flagship Epic deployments under Frontline Digitisation — alongside specialist capitalised IT for neurosciences (NHNN Queen Square), cancer (UCH Macmillan), women's (EGA UCH) and dental (Eastman). NIHR UCLH BRC research-IT capitalised costs feed amortisation as research projects close to capital. IAS 38 systematic amortisation runs over 7-10yr for bespoke Epic clinical configuration per DHSC GAM ch.5; software/licences shorter at 3-7yr. The cloud-SaaS shift (IFRS 16 interaction) reshapes mix between intangibles amortisation and right-of-use depreciation. CQC Outstanding rating reflects UCLH's clinical and digital maturity.",
        "sources": [
            {"publisher": "University College London Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.uclh.nhs.uk/about-us/our-publications/annual-reports-and-accounts"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/connecting-health-and-care/frontline-digitisation/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 5 — Intangible assets)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "National Audit Office", "title": "Digital transformation in the NHS (HC 1591, 2020)", "url": "https://www.nao.org.uk/reports/the-use-of-digital-technology-in-the-nhs/"},
            {"publisher": "Care Quality Commission", "title": "UCLH provider profile (RRV) — Outstanding rated", "url": "https://www.cqc.org.uk/provider/RRV"}
        ],
        "related": ["University College London Hospitals NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Amortisation — East And North Hertfordshire NHS Trust", "NHS England", "National Institute for Health and Care Research"]
    },
    "Transport (business + patient) — North Bristol NHS Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "North Bristol NHS Trust"}],
        "description": "NBT's £3.23M transport line covers business mileage, inter-site patient transfers and Non-Emergency Patient Transport across the Southmead Hospital (PFI-built, opened 2014, the Brunel building) main site and Cossham community hospital. Major Trauma Centre status at Southmead and the trust's tertiary specialties — neurosciences (one of UK's largest), plastics and renal — drive substantial inter-trust transfer demand from across South West England. The line interacts with PFI-novated FM contracts following Carillion's 2018 collapse (Engie/Equans novation) and SWASFT PTS contractor framework.",
        "beneficiaries": "c. 8,500 WTE staff serving a c. 900,000 north Bristol + South Glos catchment plus extended tertiary referrals across South West England; c. 130,000 ED attendances/yr at Southmead ED; c. 75,000 admissions/yr; Southmead is one of the UK's four Major Trauma Centres serving the South West.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · IFRS 16 Leases (pool fleet) · NHS Act 2006 · NHSE Patient Transport Services Eligibility Framework 2022 · HMRC AMAP · NHS AfC Section 17 · Mental Health Act 1983 (s.135/136 conveyance)",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£3.23M"},
            {"label": "Trust scale", "value": "Southmead Hospital (Brunel PFI building) + Cossham; c. 8,500 WTE"},
            {"label": "Major Trauma Centre", "value": "Southmead = one of the UK's four MTCs serving South West England — drives inter-hospital trauma transfer"},
            {"label": "Tertiary specialties", "value": "Neurosciences (one of UK's largest) + Plastics + Renal — substantial inter-trust PTS from across South West"},
            {"label": "PFI context", "value": "Brunel building PFI signed 2010, operational 2014; SPV Hospital Co (Southmead) Ltd; Carillion Jan 2018 collapse → Engie/Equans hard-FM novation"},
            {"label": "PTS provider mix", "value": "South Western Ambulance Service NHS FT (SWASFT) PTS + accredited NEPTS contractors + trust pool fleet"},
            {"label": "Staff mileage rate", "value": "AfC Section 17 / HMRC AMAP 45p first 10,000 miles + 25p thereafter; pool fleet right-of-use under IFRS 16"},
            {"label": "Funding trajectory", "value": "2021-22 c. £2.7M → 2023-24 £3.0M → 2024-25 £3.23M — fuel CPI + activity recovery"},
            {"label": "Delivery body", "value": "Trust E&F + Travel team + SWASFT PTS + NEPTS contractors"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + NHSE NEPTS framework + Bristol, North Somerset and South Gloucestershire ICB"},
            {"label": "Evaluation evidence", "value": "NHSE NEPTS Eligibility Framework 2022 review; CQC inspection RVJ; NAO Carillion + PFI hand-back reports; Trust ARA"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2014 pre-Brunel-building dispersed-site baseline · Successor: BNSSG ICS shared-fleet pooling + EV transition"}
        ],
        "notes": "NBT's transport baseline is structurally elevated by Major Trauma Centre status at Southmead — one of the UK's four MTCs serving South West England — which drives inter-hospital trauma transfers from across the region, alongside substantial tertiary referral flows for neurosciences (one of the UK's largest neurosciences services), plastics and renal. The 2014 opening of the Brunel building consolidated the trust's footprint via a major PFI, with the Carillion Jan 2018 collapse triggering Engie/Equans novation of hard-FM that adds contract-management complexity to PTS coordination. SWASFT PTS dominates non-emergency patient transport, with EV transition and BNSSG ICS shared-fleet pooling as medium-term levers.",
        "sources": [
            {"publisher": "North Bristol NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.nbt.nhs.uk/about-us/publications-policies/annual-reports-accounts"},
            {"publisher": "NHS England", "title": "Non-Emergency Patient Transport Services Eligibility Framework 2022", "url": "https://www.england.nhs.uk/long-read/non-emergency-patient-transport-services-eligibility-framework/"},
            {"publisher": "South Western Ambulance Service NHS FT", "title": "Annual Report 2023-24", "url": "https://www.swast.nhs.uk/about-us/our-publications"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "North Bristol NHS Trust provider profile (RVJ)", "url": "https://www.cqc.org.uk/provider/RVJ"}
        ],
        "related": ["North Bristol NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Transport (business + patient) — Northern Lincolnshire and Goole NHS Foundation Trust", "South Western Ambulance Service NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Amortisation — Royal Cornwall Hospitals NHS Trust": {
        "aliases": [{"name": "Amortisation", "parent": "Royal Cornwall Hospitals NHS Trust"}],
        "description": "Royal Cornwall's £3.20M amortisation line reflects systematic IAS 38 write-down of capitalised intangibles — predominantly EPR clinical software (Cerner Millennium under Frontline Digitisation), specialist software, licences and capitalised software development — across the Royal Cornwall Hospital (Truro), West Cornwall Hospital (Penzance) and St Michael's Hospital (Hayle) footprint. The peripheral Cornish geography forces high investment in telehealth and digital-clinical systems that capitalise into intangibles, augmented by Cornwall and Isles of Scilly ICB's digital programme.",
        "beneficiaries": "c. 5,500 WTE staff serving a c. 532,000 Cornwall and Isles of Scilly catchment; c. 75,000 ED attendances/yr at Royal Cornwall ED; c. 40,000 admissions/yr; peripheral geography with c. 4-hour drive to nearest tertiary centre (Plymouth/Bristol) — drives in-trust specialty + digital-clinical investment.",
        "legal_basis": "IAS 38 Intangible Assets · DHSC Group Accounting Manual 2024-25 ch.5 · IFRS 16 (cloud-SaaS interaction) · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£3.20M"},
            {"label": "Trust scale", "value": "Royal Cornwall (Truro) + West Cornwall (Penzance) + St Michael's (Hayle); c. 5,500 WTE"},
            {"label": "Composition", "value": "Capitalised Cerner EPR + telehealth platforms + specialist clinical software + licences + capitalised software development"},
            {"label": "EPR context", "value": "Cerner Millennium adopted under Frontline Digitisation; capitalised cost amortised c. 7-10yr useful life per IAS 38 / DHSC GAM"},
            {"label": "Geography premium", "value": "Peripheral Cornish footprint c. 4-hour drive to tertiary Plymouth/Bristol — drives in-trust specialty + telehealth capitalisation"},
            {"label": "Useful economic life", "value": "Software/licences typically 3-7yr; bespoke EPR clinical config 7-10yr per DHSC GAM ch.5; FD national programme funding feeds 5-10yr cycle"},
            {"label": "ICS context", "value": "Cornwall and Isles of Scilly ICB — small population (c. 580k) but very dispersed; digital programme coordinates EPR + telehealth capital"},
            {"label": "Funding trajectory", "value": "Rising amortisation as FD-era EPR + telehealth capitalisation matures; c. £2.8M 2021-22 → £3.20M 2024-25"},
            {"label": "Delivery body", "value": "Trust IT + Finance + EPR programme team + Cerner partnership + Cornwall ICB digital"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC GAM + NHSE Frontline Digitisation programme + Cornwall and Isles of Scilly ICB"},
            {"label": "Evaluation evidence", "value": "NHSE FD programme returns; CQC inspection REF; NAO Digital transformation reports; Trust ARA intangibles note"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-FD legacy clinical-systems amortisation · Successor: full-mature FD EPR cycle + cloud-SaaS IFRS 16 interaction"}
        ],
        "notes": "Royal Cornwall's amortisation profile reflects layered intangibles from Frontline Digitisation EPR rollout (Cerner Millennium) plus capitalised telehealth and digital-clinical platforms — the trust's peripheral Cornish geography with c. 4-hour drive to nearest tertiary centre (Plymouth/Bristol) forces in-trust specialty maintenance and remote-monitoring investment that capitalise into intangibles. IAS 38 systematic amortisation runs over 3-7yr for software/licences and 7-10yr for bespoke EPR clinical configuration per DHSC GAM ch.5. Cornwall and Isles of Scilly ICB's digital programme — coordinating across this dispersed, low-density catchment — is a structural driver of capitalisation cycle. The cloud-SaaS shift (IFRS 16 interaction) reshapes mix as new contracts arrive.",
        "sources": [
            {"publisher": "Royal Cornwall Hospitals NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.royalcornwall.nhs.uk/about-us/key-publications/annual-reports/"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/connecting-health-and-care/frontline-digitisation/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 5 — Intangible assets)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "National Audit Office", "title": "Digital transformation in the NHS (HC 1591, 2020)", "url": "https://www.nao.org.uk/reports/the-use-of-digital-technology-in-the-nhs/"},
            {"publisher": "Care Quality Commission", "title": "Royal Cornwall Hospitals provider profile (REF)", "url": "https://www.cqc.org.uk/provider/REF"}
        ],
        "related": ["Royal Cornwall Hospitals NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Amortisation — University College London Hospitals NHS Foundation Trust", "Amortisation — East And North Hertfordshire NHS Trust", "NHS England"]
    },
    "General supplies & services — George Eliot Hospital NHS Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "George Eliot Hospital NHS Trust"}],
        "description": "George Eliot Hospital's £3.20M general supplies & services line covers non-clinical consumables, linen, catering, hotel-services materials and minor expensed equipment at the single-site Nuneaton DGH serving north Warwickshire. The trust is a small DGH with structural sub-scale challenges that NHSE has long flagged — multiple options-appraisal exercises have considered partnership/merger paths, with active group-arrangement discussions under Coventry & Warwickshire ICS planning.",
        "beneficiaries": "c. 2,800 WTE staff serving a c. 300,000 north Warwickshire catchment (Nuneaton, Bedworth, Atherstone, Hinckley); c. 80,000 ED attendances/yr at GEH ED; c. 30,000 admissions/yr; small-DGH scale challenges drive sustained NHSE strategic-options engagement.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 2 Inventories · Procurement Act 2023 · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "General supplies & services 2024-25", "value": "£3.20M"},
            {"label": "Trust scale", "value": "Single-site DGH (College Street, Nuneaton); c. 2,800 WTE — smallest acute trust scale band"},
            {"label": "Sub-scale challenge", "value": "Small DGH at c. 30,000 admissions/yr — sustained NHSE options-appraisal engagement on strategic future"},
            {"label": "Group-arrangement context", "value": "Active partnership discussions with UHB + UHCW under Coventry & Warwickshire ICS; chair-in-common consideration"},
            {"label": "Procurement route", "value": "NHS Supply Chain national framework + ICS collaborative + trust-direct contracts"},
            {"label": "Industrial action 2023-24 effect", "value": "Strike days hit small-DGH harder per WTE; cancellation re-stocking + agency-backfill churn"},
            {"label": "April 2025 NIC + CPI uplift", "value": "Apr 2025 NIC step-up affects external supplier pass-through; sustained CPI on non-clinical inputs"},
            {"label": "Funding trajectory", "value": "2021-22 c. £2.6M → 2023-24 £3.0M → 2024-25 £3.20M"},
            {"label": "Delivery body", "value": "Trust Procurement + Supply Chain team + NHS Supply Chain + C&W ICS procurement collaborative"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Coventry & Warwickshire ICB"},
            {"label": "Evaluation evidence", "value": "Model Hospital benchmarks; CQC inspection RLT (improvement-rated); NHSE strategic-options reviews; Trust ARA"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-options-review stand-alone trust baseline · Successor: post-partnership/merger consolidated baseline + ICS collaborative scaling"}
        ],
        "notes": "George Eliot Hospital is among the smallest acute trusts in England by admissions/WTE, sustaining structural sub-scale procurement challenges that NHSE's Coventry & Warwickshire ICS planning has long flagged through options-appraisal exercises considering partnership and merger paths with University Hospitals Birmingham and University Hospitals Coventry & Warwickshire. Industrial action 2023-24 hit small-DGH supplies churn harder per WTE through cancellation re-stocking and agency backfill. NHS Supply Chain remains the dominant procurement vehicle, with C&W ICS collaborative scaling as the immediate efficiency lever pending strategic-future resolution. April 2025 NIC step-up and sustained CPI on non-clinical inputs feed forward unit-cost pressure.",
        "sources": [
            {"publisher": "George Eliot Hospital NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.geh.nhs.uk/about-us/publications-and-policies/"},
            {"publisher": "NHS Supply Chain", "title": "Annual Report 2023-24", "url": "https://www.supplychain.nhs.uk/about-us/our-publications/"},
            {"publisher": "Coventry and Warwickshire ICB", "title": "ICB strategic plans", "url": "https://www.happyhealthylives.uk/about-us/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "George Eliot Hospital provider profile (RLT)", "url": "https://www.cqc.org.uk/provider/RLT"}
        ],
        "related": ["George Eliot Hospital NHS Trust", "Clinical Supplies & Drugs", "NHS Acute Trusts", "University Hospitals Coventry and Warwickshire NHS Trust", "University Hospitals Birmingham NHS Foundation Trust", "NHS Supply Chain"]
    },
    "PFI / LIFT charges — London North West University Healthcare NHS Trust": {
        "aliases": [{"name": "PFI / LIFT charges", "parent": "London North West University Healthcare NHS Trust"}],
        "description": "LNWUHT's £3.19M PFI/LIFT charge reflects unitary-charge pass-through on Central Middlesex Hospital and Northwick Park ACAD-related PFI/LIFT components — plus residual concession arrangements across the trust's footprint (Northwick Park, Central Middlesex, Ealing). The trust was formed in October 2014 by merger of North West London Hospitals NHS Trust with Ealing Hospital NHS Trust. The PFI/LIFT line is a residual element relative to the trust's larger non-PFI estate, with FM novations following Carillion 2018 collapse adding contract-management complexity on subcontracted soft-FM.",
        "beneficiaries": "c. 9,000 WTE staff serving a c. 850,000 north-west London catchment (Brent, Harrow, Ealing); c. 220,000 ED attendances/yr (Northwick Park + Ealing + Central Middlesex urgent-care); c. 100,000 admissions/yr; large maternity service.",
        "legal_basis": "IFRIC 12 Service Concession Arrangements · IFRS 16 Leases (post-2022 transition) · DHSC Group Accounting Manual 2024-25 ch.7 · LIFT (Local Improvement Finance Trust) framework · Private Finance Initiative guidance (HM Treasury) · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "PFI / LIFT charges 2024-25", "value": "£3.19M"},
            {"label": "Trust scale", "value": "Three-site acute (Northwick Park + Central Middlesex + Ealing); c. 9,000 WTE"},
            {"label": "Merger context", "value": "Formed Oct 2014 by merger of North West London Hospitals NHS Trust + Ealing Hospital NHS Trust"},
            {"label": "PFI/LIFT components", "value": "Central Middlesex ACAD-related PFI/LIFT components + residual concession arrangements"},
            {"label": "Carillion 2018 effect", "value": "Soft-FM subcontract novations to Engie/Equans/Sodexo on Carillion-affected subcontracts"},
            {"label": "IFRS 16 transition", "value": "2022 transition reshaped split between PFI/LIFT line + lease line per DHSC GAM ch.7"},
            {"label": "Indexation mechanism", "value": "RPI / CPI-linked annual uplift on indexed FM components per concession"},
            {"label": "Funding trajectory", "value": "Mature concession; £3M-range residual line"},
            {"label": "Delivery body", "value": "LIFT Co + SPV vehicles + post-Carillion FM contractors + trust E&F oversight"},
            {"label": "Policy owner", "value": "DHSC + HM Treasury PFI/LIFT guidance + NHSE Provider Finance + North West London ICB"},
            {"label": "Evaluation evidence", "value": "NAO PFI hand-back review 2020; CQC inspection R1K; Trust ARA disclosure; NWL ICS estate review"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2014 separate North West London Hospitals + Ealing Hospital baselines · Successor: post-PFI/LIFT hand-back + NWL ICS estate consolidation"}
        ],
        "notes": "LNWUHT's PFI/LIFT line is a residual element relative to the trust's larger non-PFI estate — covering Central Middlesex ACAD-related PFI/LIFT components and other residual concession arrangements inherited via the 2014 merger of North West London Hospitals NHS Trust with Ealing Hospital NHS Trust. The Carillion January 2018 collapse triggered soft-FM novations to Engie, Equans and Sodexo on subcontracted FM elements, layering contract-management complexity on the existing LIFT/SPV structure. The IFRS 16 2022 transition reshaped the split between the PFI/LIFT line and lease lines per DHSC GAM ch.7. RPI/CPI indexation continues to lift soft-FM components. NWL ICS estate consolidation is the medium-term lever as the wider strategic estate review progresses.",
        "sources": [
            {"publisher": "London North West University Healthcare NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.lnwh.nhs.uk/about-us/our-publications/"},
            {"publisher": "National Audit Office", "title": "Managing PFI assets and services as contracts end (HC 632, 2020)", "url": "https://www.nao.org.uk/reports/managing-pfi-assets-and-services-as-contracts-end/"},
            {"publisher": "Infrastructure and Projects Authority", "title": "PFI Hand-Back Resource Centre", "url": "https://www.gov.uk/government/collections/pfi-and-pf2"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 7)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "LNWUHT provider profile (R1K)", "url": "https://www.cqc.org.uk/provider/R1K"}
        ],
        "related": ["London North West University Healthcare NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "PFI / LIFT charges — Sherwood Forest Hospitals NHS Foundation Trust", "PFI / LIFT charges — Worcestershire Acute Hospitals NHS Trust", "Infrastructure and Projects Authority"]
    },
    "Amortisation — Ashford and St Peter's Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Amortisation", "parent": "Ashford and St Peter's Hospitals NHS Foundation Trust"}],
        "description": "ASPH's £3.19M amortisation line reflects systematic IAS 38 write-down of capitalised intangibles — predominantly EPR clinical software, specialist clinical systems, licences and capitalised software development across the two-site St Peter's Hospital (Chertsey) + Ashford Hospital footprint. The trust has progressed Frontline Digitisation EPR adoption with capitalised costs feeding 5-10yr amortisation cycle, augmented by Surrey Heartlands ICS digital programme coordination.",
        "beneficiaries": "c. 4,500 WTE staff serving a c. 410,000 north-west Surrey catchment (Runnymede, Spelthorne, Surrey Heath, Woking); c. 130,000 ED attendances/yr (St Peter's main ED + Ashford Walk-in); c. 65,000 admissions/yr; large maternity unit at St Peter's.",
        "legal_basis": "IAS 38 Intangible Assets · DHSC Group Accounting Manual 2024-25 ch.5 · IFRS 16 (cloud-SaaS interaction) · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£3.19M"},
            {"label": "Trust scale", "value": "Two-site DGH (St Peter's, Chertsey + Ashford); c. 4,500 WTE"},
            {"label": "Composition", "value": "Capitalised EPR + clinical software + licences + capitalised software development — IAS 38 systematic amortisation"},
            {"label": "EPR context", "value": "Frontline Digitisation EPR programme; capitalised cost amortised c. 5-10yr useful life; FD national programme + trust-funded"},
            {"label": "Useful economic life", "value": "Software/licences typically 3-7yr; bespoke EPR clinical config 7-10yr per DHSC GAM ch.5"},
            {"label": "ICS context", "value": "Surrey Heartlands ICB digital programme — coordinates EPR + clinical-systems capitalisation across patch"},
            {"label": "Industrial action 2023-24 effect", "value": "Strike days drove systems-config capitalisation cycle (clinical-pathway redesign IT)"},
            {"label": "Funding trajectory", "value": "Rising amortisation as FD-era EPR capitalisation matures; c. £2.8M 2021-22 → £3.19M 2024-25"},
            {"label": "Delivery body", "value": "Trust IT + Finance + EPR programme team + Surrey Heartlands ICS digital"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC GAM + NHSE Frontline Digitisation programme + Surrey Heartlands ICB"},
            {"label": "Evaluation evidence", "value": "NHSE FD programme returns; CQC inspection RTK; NAO Digital transformation reports; Trust ARA intangibles note"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-FD legacy clinical-systems amortisation · Successor: full-mature FD EPR cycle + cloud-SaaS IFRS 16 interaction"}
        ],
        "notes": "ASPH's amortisation profile reflects layered intangibles from Frontline Digitisation EPR rollout plus capitalised specialist clinical systems across the two-site St Peter's + Ashford footprint. IAS 38 systematic amortisation runs over 3-7yr for software/licences and 7-10yr for bespoke EPR clinical configuration per DHSC GAM ch.5. Surrey Heartlands ICS digital programme coordination shapes capitalisation cycle across the patch. The cloud-SaaS shift (IFRS 16 interaction) reshapes mix between intangibles amortisation and right-of-use depreciation as new SaaS contracts arrive. Industrial action 2023-24 drove additional clinical-pathway redesign IT that capitalises into the amortisation cycle as the FD programme matures.",
        "sources": [
            {"publisher": "Ashford and St Peter's Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.ashfordstpeters.nhs.uk/annual-reports"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/connecting-health-and-care/frontline-digitisation/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 5 — Intangible assets)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "National Audit Office", "title": "Digital transformation in the NHS (HC 1591, 2020)", "url": "https://www.nao.org.uk/reports/the-use-of-digital-technology-in-the-nhs/"},
            {"publisher": "Care Quality Commission", "title": "ASPH provider profile (RTK)", "url": "https://www.cqc.org.uk/provider/RTK"}
        ],
        "related": ["Ashford and St Peter's Hospitals NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Amortisation — Royal Cornwall Hospitals NHS Trust", "Amortisation — University College London Hospitals NHS Foundation Trust", "Social security & levy — Ashford and St Peter's Hospitals NHS Foundation Trust"]
    },
    "Transport (business + patient) — Sheffield Teaching Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "Sheffield Teaching Hospitals NHS Foundation Trust"}],
        "description": "STH's £3.17M transport line covers business mileage, inter-site patient transfers and Non-Emergency Patient Transport across the trust's five-site footprint — Royal Hallamshire, Northern General (with the Major Trauma Centre and emergency-medicine focus), Weston Park (cancer), Jessop Wing (women's) and Charles Clifford Dental. Inter-campus transfers between the Hallamshire and Northern General sites in Sheffield, plus tertiary specialty patient flows for cancer (Weston Park), neurosciences and renal, drive substantial PTS demand. Yorkshire Ambulance Service provides PTS framework.",
        "beneficiaries": "c. 19,000 WTE staff serving a c. 600,000 Sheffield catchment plus extended tertiary referrals across South Yorkshire and East Midlands; c. 200,000 ED attendances/yr at Northern General ED; c. 175,000 admissions/yr; Northern General is one of the UK's four Major Trauma Centres serving South Yorkshire and East Midlands.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · IFRS 16 Leases (pool fleet) · NHS Act 2006 · NHSE Patient Transport Services Eligibility Framework 2022 · HMRC AMAP · NHS AfC Section 17 · Mental Health Act 1983 (s.135/136 conveyance)",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£3.17M"},
            {"label": "Trust scale", "value": "Five-site academic acute (Royal Hallamshire + Northern General + Weston Park + Jessop Wing + Charles Clifford); c. 19,000 WTE"},
            {"label": "Major Trauma Centre", "value": "Northern General = one of UK's four MTCs serving South Yorkshire + East Midlands — drives major-trauma transfer demand"},
            {"label": "Tertiary specialties", "value": "Cancer (Weston Park) + Neurosciences + Renal + Spinal injuries — substantial inter-trust PTS"},
            {"label": "Inter-campus transfers", "value": "Hallamshire ↔ Northern General continuous patient transfer for emergency-medicine + tertiary specialty pathways"},
            {"label": "PTS provider mix", "value": "Yorkshire Ambulance Service PTS + accredited NEPTS contractors + trust pool fleet (AHP + community-team)"},
            {"label": "Pool fleet (IFRS 16)", "value": "Right-of-use depreciation + interest on leased pool vehicles"},
            {"label": "Staff mileage rate", "value": "AfC Section 17 / HMRC AMAP 45p first 10,000 miles + 25p thereafter"},
            {"label": "Funding trajectory", "value": "2021-22 c. £2.7M → 2023-24 £3.0M → 2024-25 £3.17M — fuel CPI + activity recovery"},
            {"label": "Delivery body", "value": "Trust E&F + Travel team + YAS PTS + accredited NEPTS contractors"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + NHSE NEPTS framework + South Yorkshire ICB"},
            {"label": "Evaluation evidence", "value": "NHSE NEPTS Eligibility Framework 2022 review; CQC inspection RHQ; NHS Confederation MTC reports; Trust ARA"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2001 separate Royal Hallamshire + Northern General + Children's baselines · Successor: SY ICS shared-fleet pooling + EV transition"}
        ],
        "notes": "STH's transport baseline is structurally elevated by the trust's five-site academic footprint, Major Trauma Centre status at Northern General — one of the UK's four MTCs serving South Yorkshire and East Midlands — and tertiary referral flows for cancer (Weston Park, one of three specialist cancer hospitals in England), neurosciences, renal and spinal injuries. Continuous inter-campus transfers between the Hallamshire and Northern General sites for emergency-medicine and tertiary specialty pathways drive baseline PTS demand. The 2001 merger consolidating Royal Hallamshire with Northern General and Sheffield Children's baselined the current footprint. April 2025 NIC step-up affects PTS-contractor pass-through; SY ICS shared-fleet pooling and EV transition are medium-term levers.",
        "sources": [
            {"publisher": "Sheffield Teaching Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.sth.nhs.uk/about-us/publications"},
            {"publisher": "NHS England", "title": "Non-Emergency Patient Transport Services Eligibility Framework 2022", "url": "https://www.england.nhs.uk/long-read/non-emergency-patient-transport-services-eligibility-framework/"},
            {"publisher": "Yorkshire Ambulance Service NHS Trust", "title": "Annual Report 2023-24", "url": "https://www.yas.nhs.uk/about-us/our-publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Sheffield Teaching Hospitals provider profile (RHQ)", "url": "https://www.cqc.org.uk/provider/RHQ"}
        ],
        "related": ["Sheffield Teaching Hospitals NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Transport (business + patient) — Imperial College Healthcare NHS Trust", "Transport (business + patient) — North Bristol NHS Trust", "Yorkshire Ambulance Service NHS Trust"]
    },
    "Amortisation — Northumbria Healthcare NHS Foundation Trust": {
        "aliases": [{"name": "Amortisation", "parent": "Northumbria Healthcare NHS Foundation Trust"}],
        "description": "Northumbria Healthcare's £3.16M amortisation line reflects systematic IAS 38 write-down of capitalised intangibles — EPR clinical software (the trust runs a notable Cerner Millennium Northumbria-led implementation), specialist clinical systems, capitalised software development and licences. The trust opened the Northumbria Specialist Emergency Care Hospital (NSECH, Cramlington) in 2015 — the first purpose-built specialist emergency-care hospital in England — alongside a multi-site community + acute footprint, and is recognised as an NHSE digital exemplar trust.",
        "beneficiaries": "c. 11,000 WTE staff serving a c. 500,000 Northumberland and North Tyneside catchment plus tertiary specialty referrals across the North East; c. 130,000 ED attendances/yr at NSECH (the first purpose-built specialist emergency hospital in England); c. 80,000 admissions/yr; integrated acute + community + adult social care provider model.",
        "legal_basis": "IAS 38 Intangible Assets · DHSC Group Accounting Manual 2024-25 ch.5 · IFRS 16 (cloud-SaaS interaction) · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£3.16M"},
            {"label": "Trust scale", "value": "NSECH Cramlington + Wansbeck (Ashington) + North Tyneside + Hexham + Berwick + community sites; c. 11,000 WTE"},
            {"label": "Composition", "value": "Capitalised Cerner Millennium EPR + specialist clinical software + capitalised software development + licences"},
            {"label": "EPR context", "value": "Cerner Millennium Northumbria-led implementation; NHSE digital exemplar trust; capitalised cost amortised c. 7-10yr useful life"},
            {"label": "NSECH context", "value": "Northumbria Specialist Emergency Care Hospital opened 2015 — first purpose-built specialist emergency hospital in England; capitalised commissioning IT contributes"},
            {"label": "Useful economic life", "value": "Software/licences typically 3-7yr; bespoke EPR clinical config 7-10yr per DHSC GAM ch.5"},
            {"label": "Frontline Digitisation funding", "value": "FD national programme + trust-funded; mature multi-year amortisation cycle as digital exemplar"},
            {"label": "Integrated provider model", "value": "Acute + community + (until 2024) adult social care — broader capitalised software base"},
            {"label": "Funding trajectory", "value": "Mature post-NSECH-go-live amortisation cycle; c. £2.9M 2021-22 → £3.16M 2024-25"},
            {"label": "Delivery body", "value": "Trust IT + Finance + Cerner partnership + Northumbria digital team"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC GAM + NHSE Frontline Digitisation programme + North East and North Cumbria ICB"},
            {"label": "Evaluation evidence", "value": "NHSE FD programme returns; NHSE digital exemplar evaluation; CQC inspection RTF (Outstanding-rated); NAO Digital transformation reports"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2015 dispersed-DGH baseline · Successor: full-mature exemplar EPR cycle + cloud-SaaS IFRS 16 interaction"}
        ],
        "notes": "Northumbria Healthcare's amortisation profile reflects the trust's recognised position as an NHSE digital exemplar — the Cerner Millennium implementation Northumbria led has been cited across Frontline Digitisation as a reference pattern, with capitalised costs feeding mature 7-10yr amortisation cycle per DHSC GAM ch.5. The 2015 opening of NSECH (the first purpose-built specialist emergency-care hospital in England, at Cramlington) brought commissioning IT into the capitalised base. The integrated acute + community + (until 2024) adult social care model broadens the software footprint relative to acute-only peers. CQC Outstanding reflects clinical and digital maturity; cloud-SaaS shift (IFRS 16) reshapes mix.",
        "sources": [
            {"publisher": "Northumbria Healthcare NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.northumbria.nhs.uk/about-us/our-publications/annual-reports/"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme + Global Digital Exemplars", "url": "https://www.england.nhs.uk/digitaltechnology/connecting-health-and-care/frontline-digitisation/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 5 — Intangible assets)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "National Audit Office", "title": "Digital transformation in the NHS (HC 1591, 2020)", "url": "https://www.nao.org.uk/reports/the-use-of-digital-technology-in-the-nhs/"},
            {"publisher": "Care Quality Commission", "title": "Northumbria Healthcare provider profile (RTF) — Outstanding rated", "url": "https://www.cqc.org.uk/provider/RTF"}
        ],
        "related": ["Northumbria Healthcare NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Amortisation — Royal Cornwall Hospitals NHS Trust", "Amortisation — University College London Hospitals NHS Foundation Trust", "NHS England"]
    },
    "Amortisation — Blackpool Teaching Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Amortisation", "parent": "Blackpool Teaching Hospitals NHS Foundation Trust"}],
        "description": "Blackpool Teaching Hospitals' £3.16M amortisation line reflects systematic IAS 38 write-down of capitalised intangibles — EPR clinical software, specialist clinical systems, capitalised software development and licences across the Victoria Hospital (Blackpool) main acute site, Clifton Hospital and a community + integrated-care footprint serving Blackpool, Fylde and Wyre. The trust runs Lancashire Cardiac Centre as a tertiary cardiac specialty alongside acute services, with capitalised cardiac-IT systems contributing. NHP cohort 2 — Victoria Hospital rebuild caught by Jan 2025 Reset deferral.",
        "beneficiaries": "c. 6,500 WTE staff serving a c. 330,000 Blackpool + Fylde + Wyre catchment plus tertiary cardiac referrals from across Lancashire and South Cumbria; c. 110,000 ED attendances/yr at Victoria Hospital ED; c. 60,000 admissions/yr; Blackpool catchment among most deprived coastal areas in England.",
        "legal_basis": "IAS 38 Intangible Assets · DHSC Group Accounting Manual 2024-25 ch.5 · IFRS 16 (cloud-SaaS interaction) · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£3.16M"},
            {"label": "Trust scale", "value": "Victoria Hospital (Blackpool) + Clifton + community + integrated-care footprint; c. 6,500 WTE"},
            {"label": "Composition", "value": "Capitalised EPR + Lancashire Cardiac Centre cardiac-IT + clinical software + licences + capitalised software development"},
            {"label": "Lancashire Cardiac Centre", "value": "Tertiary cardiac specialty; capitalised cardiac-IT systems contribute to amortisation base"},
            {"label": "Useful economic life", "value": "Software/licences typically 3-7yr; bespoke EPR clinical config 7-10yr per DHSC GAM ch.5"},
            {"label": "NHP Reset Jan 2025", "value": "Victoria Hospital rebuild caught by Jan 2025 NHP Reset deferral; capitalisation cycle path affected"},
            {"label": "Catchment deprivation", "value": "Blackpool — among most deprived coastal areas in England; integrated-care provider model with broad capitalised digital footprint"},
            {"label": "Frontline Digitisation funding", "value": "FD national programme + trust-funded; multi-year amortisation cycle"},
            {"label": "Funding trajectory", "value": "Rising amortisation as FD-era + cardiac-IT capitalisation matures; c. £2.8M 2021-22 → £3.16M 2024-25"},
            {"label": "Delivery body", "value": "Trust IT + Finance + EPR programme team + Lancashire Cardiac Centre IT + Lancashire and South Cumbria ICS digital"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC GAM + NHSE Frontline Digitisation programme + Lancashire and South Cumbria ICB"},
            {"label": "Evaluation evidence", "value": "NHSE FD programme returns; CQC inspection RXL; NAO Digital transformation reports; Trust ARA intangibles note"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-FD legacy clinical-systems amortisation · Successor: full-mature FD EPR cycle + cloud-SaaS IFRS 16 interaction + post-NHP rebuild capital"}
        ],
        "notes": "Blackpool Teaching Hospitals' amortisation profile reflects layered intangibles from Frontline Digitisation EPR rollout plus capitalised Lancashire Cardiac Centre tertiary cardiac-IT systems — Lancashire Cardiac Centre serves cardiac referrals from across Lancashire and South Cumbria. IAS 38 systematic amortisation runs over 3-7yr for software/licences and 7-10yr for bespoke EPR clinical configuration per DHSC GAM ch.5. The January 2025 NHP Reset deferral affects the medium-term capitalisation cycle path for Victoria Hospital rebuild — the trust continues operating from ageing fabric serving one of England's most deprived coastal catchments. The cloud-SaaS shift (IFRS 16 interaction) reshapes mix between intangibles amortisation and right-of-use depreciation.",
        "sources": [
            {"publisher": "Blackpool Teaching Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.bfwh.nhs.uk/about-us/our-publications/"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/connecting-health-and-care/frontline-digitisation/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 5 — Intangible assets)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "National Audit Office", "title": "Progress with the New Hospital Programme (HC 1662, 2023)", "url": "https://www.nao.org.uk/reports/progress-with-the-new-hospital-programme/"},
            {"publisher": "Care Quality Commission", "title": "Blackpool Teaching Hospitals provider profile (RXL)", "url": "https://www.cqc.org.uk/provider/RXL"}
        ],
        "related": ["Blackpool Teaching Hospitals NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Amortisation — Northumbria Healthcare NHS Foundation Trust", "Amortisation — Royal Cornwall Hospitals NHS Trust", "New Hospital Programme"]
    },
}
