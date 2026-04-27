# -*- coding: utf-8 -*-
# Phase 2 Acute slice 2 — chunk 21 (17 NHS Acute Trust orphan sub-lines)
# Hand-curated trust-specific PROGRAMME-archetype enrichment entries.
# Structural contract per docs/archetype_briefs.md.

NEW = {
    "Business rates — East Lancashire Hospitals NHS Trust": {
        "aliases": [{"name": "Business rates", "parent": "East Lancashire Hospitals NHS Trust"}],
        "description": "ELHT's £3.611M business rates line covers non-domestic rating liability across the trust's multi-site East Lancashire footprint — Royal Blackburn Teaching Hospital (main DGH), Burnley General (Lancashire Women and Newborn Centre), Pendle, Clitheroe and Accrington Victoria community hospitals. The line scales with rateable value under the LGFA 1988 multiplier mechanism, with the Non-Domestic Rating (Multipliers and Private Finance) Act 2024 reshaping the medium-term multiplier path.",
        "beneficiaries": "c. 9,000 WTE staff serving a c. 530,000 East Lancashire catchment (Blackburn with Darwen, Burnley, Pendle, Hyndburn, Rossendale, Ribble Valley); c. 165,000 ED attendances/yr at Royal Blackburn ED; c. 80,000 admissions/yr; c. 6,000 deliveries/yr at the Lancashire Women and Newborn Centre.",
        "legal_basis": "Local Government Finance Act 1988 (Schedule 6 — non-domestic rating) · Non-Domestic Rating (Multipliers and Private Finance) Act 2024 · Non-Domestic Rating Act 2023 · DHSC Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£3.611M"},
            {"label": "Trust scale", "value": "Multi-site (Royal Blackburn + Burnley General + 3 community hospitals); c. 9,000 WTE"},
            {"label": "Rateable estate", "value": "Royal Blackburn Teaching Hospital (main DGH) + Burnley General (Lancashire Women and Newborn Centre) + Pendle / Clitheroe / Accrington Victoria community hospitals"},
            {"label": "2023 revaluation effect", "value": "VOA 2023 list (effective Apr 2023) reset rateable values from 2017 list — drove step-up in 2023-24 baseline; standard multiplier 2024-25 = 54.6p"},
            {"label": "NDR (Multipliers and Private Finance) Act 2024", "value": "From Apr 2026 introduces lower multipliers for high-street retail/hospitality + higher multiplier for £500k+ RV — NHS large hospital sites likely caught by higher band"},
            {"label": "Charitable mandatory relief", "value": "NHS trusts NOT charities for NDR purposes (unlike GP practices / hospices) — pay full liability without 80% mandatory relief"},
            {"label": "Industrial action 2023-24 effect", "value": "Indirect — strike-driven activity disruption did not change rateable value but elevates pressure on cost base"},
            {"label": "Funding trajectory", "value": "2021-22 c. £3.1M → 2023-24 £3.4M (revaluation) → 2024-25 £3.611M (multiplier uplift)"},
            {"label": "Delivery body", "value": "Trust E&F finance + Valuation Office Agency (rateable value) + billing authorities (Blackburn with Darwen BC + Burnley BC + Pendle BC + Ribble Valley BC + Hyndburn BC)"},
            {"label": "Policy owner", "value": "MHCLG (NDR policy) + HM Treasury (multiplier-setting) + DHSC + NHSE Provider Finance + Lancashire & South Cumbria ICB"},
            {"label": "Evaluation evidence", "value": "VOA rating list disclosures; NAO local-government finance reports; Trust ARA premises-cost note; OBR EFO NDR forecasts"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2017-2023 revaluation list baseline · Successor: Apr 2026 NDR multiplier reform under 2024 Act + ongoing 3-year revaluation cycle"}
        ],
        "notes": "ELHT's business rates baseline reflects a multi-site East Lancashire estate dominated by Royal Blackburn DGH and Burnley General (Lancashire Women and Newborn Centre, c. 6,000 deliveries/yr) plus three community hospitals. NHS trusts do not benefit from charitable mandatory relief, so liability tracks rateable value at the prevailing multiplier in full. The April 2023 VOA revaluation drove a step-up carried into 2024-25. The 2024 NDR Act introduces from April 2026 a higher multiplier for properties with rateable value above £500,000 — most NHS large-hospital sites fall into this band, signalling forward-cost pressure. Five different billing authorities issue demand notices across the estate, creating year-end reconciliation complexity.",
        "sources": [
            {"publisher": "East Lancashire Hospitals NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://elht.nhs.uk/about-us/our-publications"},
            {"publisher": "Valuation Office Agency", "title": "Find a business rates valuation (2023 list)", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "Ministry of Housing, Communities and Local Government", "title": "Non-Domestic Rating (Multipliers and Private Finance) Act 2024", "url": "https://www.legislation.gov.uk/ukpga/2024/30"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "East Lancashire Hospitals provider profile (RXR)", "url": "https://www.cqc.org.uk/provider/RXR"}
        ],
        "related": ["East Lancashire Hospitals NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Valuation Office Agency", "Business rates — University Hospitals Plymouth NHS Trust", "Department of Health and Social Care"]
    },
    "Business rates — University Hospitals Plymouth NHS Trust": {
        "aliases": [{"name": "Business rates", "parent": "University Hospitals Plymouth NHS Trust"}],
        "description": "UHP's £3.590M business rates line covers non-domestic rating liability principally on Derriford Hospital — the south-west peninsula's tertiary acute centre — plus satellite facilities. Derriford is a c. 1,000-bed Major Trauma Centre serving Devon, Cornwall and the Isles of Scilly, with a large rateable footprint including the South West Cardiothoracic Centre, the Plymouth Oncology Centre and the Mortimer Building (Royal Eye Infirmary). Liability scales with rateable value under LGFA 1988 multiplier mechanism, with the 2024 NDR Act reshaping the post-Apr 2026 multiplier path.",
        "beneficiaries": "c. 9,500 WTE staff serving a c. 450,000 Plymouth + south-west Devon + east Cornwall direct catchment plus a c. 2.0M peninsula tertiary referral footprint; c. 130,000 ED attendances/yr at Derriford ED (Major Trauma Centre); c. 100,000 admissions/yr; the only MTC for Devon, Cornwall and the Isles of Scilly.",
        "legal_basis": "Local Government Finance Act 1988 (Schedule 6 — non-domestic rating) · Non-Domestic Rating (Multipliers and Private Finance) Act 2024 · Non-Domestic Rating Act 2023 · DHSC Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£3.590M"},
            {"label": "Trust scale", "value": "Tertiary acute (Derriford Hospital, Plymouth — c. 1,000 beds) + satellite sites; c. 9,500 WTE"},
            {"label": "Rateable estate", "value": "Derriford Hospital main site + South West Cardiothoracic Centre + Plymouth Oncology Centre + Mortimer Building (Royal Eye Infirmary)"},
            {"label": "2023 revaluation effect", "value": "VOA 2023 list (Apr 2023) reset rateable values; standard multiplier 2024-25 = 54.6p"},
            {"label": "Major Trauma Centre", "value": "Derriford = the only MTC for Devon, Cornwall and the Isles of Scilly — drives high-spec rateable footprint (helipad, MTC theatre suite, ICU)"},
            {"label": "NDR (Multipliers and Private Finance) Act 2024", "value": "Apr 2026 higher multiplier band for £500k+ RV — Derriford caught by higher band"},
            {"label": "NHS charitable relief absent", "value": "NHS trusts pay full NDR liability — no 80% charity relief unlike hospices/GPs"},
            {"label": "Funding trajectory", "value": "2021-22 c. £3.1M → 2023-24 £3.4M (revaluation) → 2024-25 £3.590M"},
            {"label": "Delivery body", "value": "Trust E&F finance + VOA (rateable value) + Plymouth City Council (billing authority for Derriford)"},
            {"label": "Policy owner", "value": "MHCLG (NDR policy) + HM Treasury (multipliers) + DHSC + NHSE Provider Finance + Devon ICB"},
            {"label": "Evaluation evidence", "value": "VOA list disclosures; NAO local-government finance reports; Trust ARA premises note; CQC RK9 inspection"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2017-2023 list baseline · Successor: Apr 2026 NDR multiplier reform"}
        ],
        "notes": "UHP's business rates baseline is anchored by Derriford Hospital — the south-west peninsula's only Major Trauma Centre and tertiary referral hub for Devon, Cornwall and the Isles of Scilly. The c. 1,000-bed site plus South West Cardiothoracic Centre, Plymouth Oncology Centre and Mortimer Building drive a substantial rateable footprint that the April 2023 VOA revaluation reset upwards. NHS trusts pay full NDR liability without charity relief. The Non-Domestic Rating (Multipliers and Private Finance) Act 2024 introduces from April 2026 a higher multiplier for £500,000+ RV properties, capturing Derriford and signalling forward-cost pressure beyond 2025-26. Plymouth City Council is the sole billing authority, simplifying year-end reconciliation relative to multi-authority peers.",
        "sources": [
            {"publisher": "University Hospitals Plymouth NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.plymouthhospitals.nhs.uk/annual-report"},
            {"publisher": "Valuation Office Agency", "title": "Find a business rates valuation (2023 list)", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "Ministry of Housing, Communities and Local Government", "title": "Non-Domestic Rating (Multipliers and Private Finance) Act 2024", "url": "https://www.legislation.gov.uk/ukpga/2024/30"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "University Hospitals Plymouth provider profile (RK9)", "url": "https://www.cqc.org.uk/provider/RK9"}
        ],
        "related": ["University Hospitals Plymouth NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Valuation Office Agency", "Business rates — East Lancashire Hospitals NHS Trust", "Department of Health and Social Care"]
    },
    "Business rates — Gloucestershire Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "Gloucestershire Hospitals NHS Foundation Trust"}],
        "description": "Gloucestershire Hospitals NHS FT's £3.590M business rates line covers non-domestic rating liability across the trust's two-DGH footprint — Gloucestershire Royal Hospital (Gloucester) and Cheltenham General Hospital (Cheltenham) — plus satellite sites. The two-site model spans urgent care, maternity, oncology and elective specialties split across the Gloucester/Cheltenham reconfiguration debate. Liability scales with rateable value under LGFA 1988 multiplier mechanism, with the 2024 NDR Act reshaping the post-Apr 2026 multiplier path.",
        "beneficiaries": "c. 8,000 WTE staff serving a c. 670,000 Gloucestershire catchment (Gloucester, Cheltenham, Cotswolds, Forest of Dean, Stroud, Tewkesbury); c. 160,000 ED attendances/yr (Gloucestershire Royal main ED + Cheltenham General ED — the latter in active reconfiguration debate); c. 80,000 admissions/yr.",
        "legal_basis": "Local Government Finance Act 1988 (Schedule 6 — non-domestic rating) · Non-Domestic Rating (Multipliers and Private Finance) Act 2024 · Non-Domestic Rating Act 2023 · DHSC Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£3.590M"},
            {"label": "Trust scale", "value": "Two-DGH (Gloucestershire Royal + Cheltenham General); c. 8,000 WTE"},
            {"label": "Rateable estate", "value": "Gloucestershire Royal Hospital + Cheltenham General Hospital + smaller community-site footprint"},
            {"label": "2023 revaluation effect", "value": "VOA 2023 list (Apr 2023) reset rateable values; standard multiplier 2024-25 = 54.6p"},
            {"label": "NDR (Multipliers and Private Finance) Act 2024", "value": "Apr 2026 higher multiplier for £500k+ RV — both DGH sites caught"},
            {"label": "Reconfiguration context", "value": "Cheltenham General ED downgrade debate (Fit for the Future programme) shapes future site footprint + rateable use mix"},
            {"label": "Industrial action 2023-24 effect", "value": "Indirect — strike-driven activity disruption did not change rateable value"},
            {"label": "Funding trajectory", "value": "2021-22 c. £3.1M → 2023-24 £3.4M (revaluation) → 2024-25 £3.590M"},
            {"label": "Delivery body", "value": "Trust E&F finance + VOA (rateable value) + Gloucester City Council + Cheltenham Borough Council (billing authorities)"},
            {"label": "Policy owner", "value": "MHCLG (NDR policy) + HM Treasury (multipliers) + DHSC + NHSE Provider Finance + Gloucestershire ICB"},
            {"label": "Evaluation evidence", "value": "VOA list disclosures; Trust ARA premises note; CQC RTE inspection; Fit for the Future business case"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2017-2023 list baseline · Successor: Apr 2026 NDR multiplier reform + Fit for the Future site reconfiguration"}
        ],
        "notes": "Gloucestershire Hospitals NHS FT operates a two-DGH model across Gloucestershire Royal (Gloucester) and Cheltenham General, with the Cheltenham ED downgrade debate under the Fit for the Future programme reshaping medium-term site-use mix. The April 2023 VOA revaluation reset rateable values upwards across both DGH sites. NHS trusts pay full NDR without charity relief. The Non-Domestic Rating (Multipliers and Private Finance) Act 2024 introduces from April 2026 a higher multiplier for £500,000+ RV properties, capturing both DGH sites and signalling forward-cost pressure beyond 2025-26. Gloucester City Council and Cheltenham Borough Council are the two billing authorities. The 2024-25 figure sits in line with peer multi-DGH trusts of similar bed-count post-revaluation.",
        "sources": [
            {"publisher": "Gloucestershire Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.gloshospitals.nhs.uk/about-us/key-publications/"},
            {"publisher": "Valuation Office Agency", "title": "Find a business rates valuation (2023 list)", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "Ministry of Housing, Communities and Local Government", "title": "Non-Domestic Rating (Multipliers and Private Finance) Act 2024", "url": "https://www.legislation.gov.uk/ukpga/2024/30"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Gloucestershire Hospitals provider profile (RTE)", "url": "https://www.cqc.org.uk/provider/RTE"}
        ],
        "related": ["Gloucestershire Hospitals NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Valuation Office Agency", "Business rates — East Lancashire Hospitals NHS Trust", "Department of Health and Social Care"]
    },
    "Business rates — The Mid Yorkshire Hospitals NHS Trust": {
        "aliases": [{"name": "Business rates", "parent": "The Mid Yorkshire Hospitals NHS Trust"}],
        "description": "Mid Yorkshire Teaching NHS Trust's £3.589M business rates line covers non-domestic rating liability across the trust's three-site footprint — Pinderfields Hospital (Wakefield, main DGH + regional Major Trauma Unit + spinal injuries), Dewsbury and District Hospital (Dewsbury) and Pontefract Hospital (Pontefract). Pinderfields was rebuilt under PFI (operational 2010), reshaping the rateable footprint at the main site. Liability scales with rateable value under LGFA 1988 multiplier mechanism, with the 2024 NDR Act reshaping the post-Apr 2026 multiplier path.",
        "beneficiaries": "c. 9,000 WTE staff serving a c. 540,000 Mid Yorkshire catchment (Wakefield, Dewsbury, Pontefract); c. 200,000 ED attendances/yr (Pinderfields + Dewsbury + Pontefract combined); c. 90,000 admissions/yr; Pinderfields hosts the Yorkshire Regional Spinal Injuries Centre.",
        "legal_basis": "Local Government Finance Act 1988 (Schedule 6 — non-domestic rating) · Non-Domestic Rating (Multipliers and Private Finance) Act 2024 · Non-Domestic Rating Act 2023 · DHSC Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£3.589M"},
            {"label": "Trust scale", "value": "Three-site (Pinderfields + Dewsbury + Pontefract); c. 9,000 WTE; trust granted 'Teaching' status 2023"},
            {"label": "Rateable estate", "value": "Pinderfields Hospital (PFI-rebuilt 2010, regional spinal injuries) + Dewsbury and District Hospital + Pontefract Hospital"},
            {"label": "PFI estate context", "value": "Pinderfields rebuilt under PFI (operational 2010) — modern footprint reset rateable value above the legacy site"},
            {"label": "2023 revaluation effect", "value": "VOA 2023 list (Apr 2023) reset rateable values; standard multiplier 2024-25 = 54.6p"},
            {"label": "NDR (Multipliers and Private Finance) Act 2024", "value": "Apr 2026 higher multiplier for £500k+ RV — Pinderfields caught"},
            {"label": "Industrial action 2023-24 effect", "value": "Indirect — strike disruption did not change rateable value"},
            {"label": "Funding trajectory", "value": "2021-22 c. £3.1M → 2023-24 £3.4M (revaluation) → 2024-25 £3.589M"},
            {"label": "Delivery body", "value": "Trust E&F finance + VOA + Wakefield Council (billing authority for all three sites — single MDC area)"},
            {"label": "Policy owner", "value": "MHCLG (NDR policy) + HM Treasury (multipliers) + DHSC + NHSE Provider Finance + West Yorkshire ICB"},
            {"label": "Evaluation evidence", "value": "VOA list disclosures; Trust ARA premises note; CQC RXF inspection; PFI annual review"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2017-2023 list baseline · Successor: Apr 2026 NDR multiplier reform"}
        ],
        "notes": "Mid Yorkshire Teaching NHS Trust operates a three-site footprint across Wakefield (Pinderfields), Dewsbury and Pontefract, with the Pinderfields PFI rebuild (operational 2010) resetting rateable value upwards relative to the legacy estate. The trust was granted 'Teaching' status in 2023 reflecting expanded medical-education and research footprint. The April 2023 VOA revaluation drove a step-up across all three sites carried into 2024-25. NHS trusts pay full NDR without charity relief. The Non-Domestic Rating (Multipliers and Private Finance) Act 2024 introduces from April 2026 a higher multiplier for £500,000+ RV properties, with Pinderfields likely caught. All three sites fall within Wakefield MDC as billing authority, simplifying year-end reconciliation.",
        "sources": [
            {"publisher": "The Mid Yorkshire Hospitals NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.midyorks.nhs.uk/annual-reports"},
            {"publisher": "Valuation Office Agency", "title": "Find a business rates valuation (2023 list)", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "Ministry of Housing, Communities and Local Government", "title": "Non-Domestic Rating (Multipliers and Private Finance) Act 2024", "url": "https://www.legislation.gov.uk/ukpga/2024/30"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Mid Yorkshire Hospitals provider profile (RXF)", "url": "https://www.cqc.org.uk/provider/RXF"}
        ],
        "related": ["The Mid Yorkshire Hospitals NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Valuation Office Agency", "Business rates — East Lancashire Hospitals NHS Trust", "Department of Health and Social Care"]
    },
    "Amortisation — North Bristol NHS Trust": {
        "aliases": [{"name": "Amortisation", "parent": "North Bristol NHS Trust"}],
        "description": "North Bristol's £3.582M amortisation line covers the systematic write-down of intangible assets — principally capitalised software licences, the trust's electronic patient record platform and major clinical-systems development costs — across the useful-economic-life set by IAS 38 and DHSC GAM ch.5. The trust runs Southmead Hospital (PFI-built, opened 2014) and Cossham Hospital, with EPR/digital-maturity investment under the NHSE Frontline Digitisation programme driving the recent intangible-asset capitalisation pipeline.",
        "beneficiaries": "c. 8,500 WTE staff serving a c. 950,000 north Bristol + South Gloucestershire + parts of Wiltshire and Somerset catchment; c. 130,000 ED attendances/yr at Southmead ED (Major Trauma Centre); c. 90,000 admissions/yr; Southmead = one of South West's MTCs, hosts regional plastics, neurosciences, renal.",
        "legal_basis": "IAS 38 Intangible Assets · DHSC Group Accounting Manual 2024-25 (chapter 5) · IAS 36 Impairment of Assets · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£3.582M"},
            {"label": "Trust scale", "value": "Tertiary acute (Southmead PFI-built 2014 + Cossham); c. 8,500 WTE; Major Trauma Centre"},
            {"label": "Asset class", "value": "Capitalised software licences + EPR (Cerner Millennium) + clinical systems development costs + capitalised website / patient-portal IP"},
            {"label": "EPR + Frontline Digitisation context", "value": "NBT runs Cerner Millennium EPR — capitalised licence + implementation costs amortised over useful economic life (typically 5-10 years)"},
            {"label": "IAS 38 useful-life convention", "value": "Software licences typically 3-5 years; EPR core 5-10 years; per DHSC GAM ch.5 conventions"},
            {"label": "PFI estate interaction", "value": "Southmead PFI build (operational 2014) — separate from intangible amortisation; runs through PFI/IFRIC 12 line"},
            {"label": "Funding trajectory", "value": "2021-22 c. £3.0M → 2023-24 £3.4M → 2024-25 £3.582M — sustained intangible capitalisation pipeline"},
            {"label": "Frontline Digitisation programme", "value": "NHSE Frontline Digitisation (DHSC capital) — drives EPR/digital intangible capitalisation across sector"},
            {"label": "Delivery body", "value": "Trust Finance + Digital + EPR programme team + DHSC Frontline Digitisation funding"},
            {"label": "Policy owner", "value": "DHSC + NHSE Transformation + NHSE Provider Finance + Bristol, North Somerset and South Gloucestershire ICB"},
            {"label": "Evaluation evidence", "value": "NAO Digital transformation in the NHS report; Trust ARA intangible-asset note; CQC RVJ inspection; HSSIB digital-readiness reports"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-EPR paper-record + smaller intangible base · Successor: continued Frontline Digitisation amortisation pipeline"}
        ],
        "notes": "North Bristol's amortisation baseline reflects sustained capitalisation of intangible assets — chief among them the Cerner Millennium EPR platform deployed at Southmead alongside ongoing clinical-systems development, amortised over IAS 38 useful-economic-life with DHSC GAM ch.5 setting NHS-wide conventions. The NHSE Frontline Digitisation programme has driven intangible-asset capitalisation since 2021, with NBT among the early Cerner-adopting trusts. The Southmead PFI build (operational 2014) is treated separately under IFRIC 12 and runs through the PFI/LIFT line, not amortisation. Useful-economic-life conventions (3-5 yrs software, 5-10 yrs EPR) shape the year-on-year profile. NAO's digital-transformation reviews provide cross-NHS evaluation context.",
        "sources": [
            {"publisher": "North Bristol NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.nbt.nhs.uk/about-us/publications-policies/our-publications"},
            {"publisher": "National Audit Office", "title": "Digital transformation in the NHS (HC 1295, 2020)", "url": "https://www.nao.org.uk/reports/the-use-of-digital-technology-in-the-nhs/"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/frontline-digitisation/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 5 — intangibles)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "North Bristol provider profile (RVJ)", "url": "https://www.cqc.org.uk/provider/RVJ"}
        ],
        "related": ["North Bristol NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Amortisation — University Hospitals Birmingham NHS Foundation Trust", "Amortisation — Milton Keynes University Hospital NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Establishment costs — Bolton NHS Foundation Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "Bolton NHS Foundation Trust"}],
        "description": "Bolton NHS FT's £3.576M establishment costs line covers non-clinical operating overheads — printing, postage, telephony, training and professional fees, conference and travel-related establishment, courier services, and ancillary office-based running costs — across the trust's Royal Bolton Hospital site plus integrated Bolton borough community services. The line scales with substantive headcount activity and corporate-functions footprint, with Frontline Digitisation EPR rollout and 2023-24 industrial-action backfill driving recent uplift through change-management and training cost.",
        "beneficiaries": "c. 5,500 WTE staff serving a c. 295,000 Bolton borough catchment; c. 130,000 ED attendances/yr at Royal Bolton ED; c. 50,000 admissions/yr; large maternity service (c. 6,000 deliveries/yr — among Greater Manchester's largest); integrated borough community services across Bolton.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£3.576M"},
            {"label": "Trust scale", "value": "Single acute (Royal Bolton Hospital, Farnworth) + integrated Bolton borough community services; c. 5,500 WTE"},
            {"label": "Composition", "value": "Printing + postage + telephony + training + professional fees + conference/travel + courier + corporate establishment"},
            {"label": "Maternity scale", "value": "c. 6,000 deliveries/yr — among Greater Manchester's largest maternity services"},
            {"label": "ED throughput", "value": "c. 130,000 attendances/yr"},
            {"label": "EPR + Frontline Digitisation", "value": "NHSE Frontline Digitisation drives training + change-mgmt + telephony cost during EPR rollout — feeds establishment line"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove training-backfill + agency-coordination establishment costs"},
            {"label": "Funding trajectory", "value": "2021-22 c. £2.9M → 2023-24 £3.3M → 2024-25 £3.576M"},
            {"label": "Delivery body", "value": "Trust corporate services + Finance + Digital + L&D + HR establishment functions"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Greater Manchester ICB + GM Combined Authority devolved health envelope"},
            {"label": "Evaluation evidence", "value": "Model Hospital corporate-services benchmarks; CQC RMC inspection; Trust ARA disclosure; NAO digital-transformation context"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2011 pre-community-integration baseline · Successor: continued Frontline Digitisation training + GM ICS shared back-office consolidation"}
        ],
        "notes": "Bolton NHS FT's establishment-costs line reflects an integrated acute + community workforce serving the Bolton borough within Greater Manchester ICS. The trust's large maternity service (c. 6,000 deliveries/yr — among GM's largest) and integrated community-team footprint shape the corporate-services baseline. The NHSE Frontline Digitisation EPR rollout has driven training, change-management and telephony establishment cost since 2022. Industrial action 2023-24 added training-backfill and agency-coordination cost across the 44 junior-doctor and 10 consultant strike days. April 2025 employer-NIC step-up and sustained CPI on professional services feed forward unit-cost pressure. GM ICS shared back-office consolidation under the GM Combined Authority devolved health envelope is the medium-term lever.",
        "sources": [
            {"publisher": "Bolton NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.boltonft.nhs.uk/about-us/publications/"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/frontline-digitisation/"},
            {"publisher": "Greater Manchester Combined Authority", "title": "Health and care devolution", "url": "https://www.greatermanchester-ca.gov.uk/what-we-do/health/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Bolton NHS FT provider profile (RMC)", "url": "https://www.cqc.org.uk/provider/RMC"}
        ],
        "related": ["Bolton NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Establishment costs — Calderdale and Huddersfield NHS Foundation Trust", "Establishment costs — Doncaster and Bassetlaw Teaching Hospitals NHS Foundation Trust", "Greater Manchester Integrated Care Board"]
    },
    "Establishment costs — Calderdale and Huddersfield NHS Foundation Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "Calderdale and Huddersfield NHS Foundation Trust"}],
        "description": "Calderdale and Huddersfield NHS FT's £3.557M establishment costs line covers non-clinical operating overheads — printing, postage, telephony, training, professional fees, conference and travel-related establishment, courier services and ancillary running costs — across the trust's two-DGH footprint at Calderdale Royal Hospital (Halifax, PFI-built 2001) and Huddersfield Royal Infirmary. The trust is in active estate-reconfiguration debate under the West Yorkshire Hospital Reconfiguration programme, shaping medium-term corporate-services footprint.",
        "beneficiaries": "c. 6,000 WTE staff serving a c. 470,000 Calderdale + Kirklees catchment; c. 165,000 ED attendances/yr (Calderdale Royal + Huddersfield Royal Infirmary EDs); c. 75,000 admissions/yr; cross-site clinical specialty split across Halifax and Huddersfield generates corporate-services coordination demand.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£3.557M"},
            {"label": "Trust scale", "value": "Two-DGH (Calderdale Royal PFI 2001 + Huddersfield Royal Infirmary); c. 6,000 WTE"},
            {"label": "Composition", "value": "Printing + postage + telephony + training + professional fees + conference/travel + corporate establishment"},
            {"label": "PFI estate context", "value": "Calderdale Royal PFI signed 1998, operational 2001 — affects soft-FM/professional-services boundary at Halifax"},
            {"label": "Reconfiguration context", "value": "Hospital Reconfiguration programme (HRI Halifax/Huddersfield ED + acute reconfig) pending NHP Reset funding decisions"},
            {"label": "EPR + Frontline Digitisation", "value": "Trust EPR rollout drives training + change-mgmt + telephony cost"},
            {"label": "Industrial action 2023-24 effect", "value": "Junior-doctor + consultant strikes drove training-backfill + agency-coordination cost"},
            {"label": "Funding trajectory", "value": "2021-22 c. £2.9M → 2023-24 £3.3M → 2024-25 £3.557M"},
            {"label": "Delivery body", "value": "Trust corporate services + Finance + Digital + L&D + HR establishment functions"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + West Yorkshire ICB"},
            {"label": "Evaluation evidence", "value": "Model Hospital corporate-services benchmarks; CQC RWY inspection; HRI reconfig business cases; Trust ARA disclosure"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2001 pre-PFI baseline · Successor: post-reconfiguration two-site rebalance + post-NHP-Reset capital trajectory"}
        ],
        "notes": "Calderdale and Huddersfield NHS FT's establishment-costs line reflects a two-DGH footprint with the Calderdale Royal PFI (operational 2001) shaping soft-FM/professional-services boundary at Halifax, while Huddersfield Royal Infirmary operates under direct-trust regimes. The Hospital Reconfiguration programme — long-running debate over the future split of ED, acute and elective services between Halifax and Huddersfield — sits within the West Yorkshire ICB strategic capital pipeline pending NHP Reset funding decisions. The NHSE Frontline Digitisation EPR rollout has driven training, change-management and telephony cost. Industrial action 2023-24 added training-backfill and agency-coordination cost. April 2025 employer-NIC step-up and CPI on professional services feed forward pressure into 2025-26.",
        "sources": [
            {"publisher": "Calderdale and Huddersfield NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.cht.nhs.uk/about-us/publications/"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/frontline-digitisation/"},
            {"publisher": "Department of Health and Social Care", "title": "New Hospital Programme — Plan for Implementation (Jan 2025 Reset)", "url": "https://www.gov.uk/government/publications/new-hospital-programme-plan-for-implementation"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Calderdale and Huddersfield provider profile (RWY)", "url": "https://www.cqc.org.uk/provider/RWY"}
        ],
        "related": ["Calderdale and Huddersfield NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Establishment costs — Bolton NHS Foundation Trust", "Establishment costs — Doncaster and Bassetlaw Teaching Hospitals NHS Foundation Trust", "New Hospital Programme"]
    },
    "Establishment costs — Doncaster and Bassetlaw Teaching Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "Doncaster and Bassetlaw Teaching Hospitals NHS Foundation Trust"}],
        "description": "Doncaster and Bassetlaw Teaching Hospitals NHS FT's £3.555M establishment costs line covers non-clinical operating overheads — printing, postage, telephony, training, professional fees, conference and travel-related establishment, courier services and ancillary running costs — across the trust's three-site footprint at Doncaster Royal Infirmary, Bassetlaw Hospital (Worksop) and Montagu Hospital (Mexborough). The cross-county footprint (South Yorkshire + Nottinghamshire/Bassetlaw) generates additional corporate-services coordination demand.",
        "beneficiaries": "c. 6,500 WTE staff serving a c. 420,000 Doncaster + Bassetlaw cross-county catchment; c. 175,000 ED attendances/yr (Doncaster Royal + Bassetlaw EDs combined); c. 80,000 admissions/yr; the trust spans South Yorkshire ICS + Nottinghamshire ICS through the Bassetlaw site.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£3.555M"},
            {"label": "Trust scale", "value": "Three-site (Doncaster Royal + Bassetlaw + Montagu); c. 6,500 WTE; teaching-trust status"},
            {"label": "Composition", "value": "Printing + postage + telephony + training + professional fees + conference/travel + corporate establishment"},
            {"label": "Cross-ICS footprint", "value": "Trust spans South Yorkshire ICS (Doncaster + Mexborough) + Nottinghamshire ICS (Bassetlaw, Worksop) — generates cross-ICB coordination cost"},
            {"label": "Teaching-trust status", "value": "Granted teaching status in association with Sheffield/Hull medical schools — supports training/L&D establishment cost"},
            {"label": "EPR + Frontline Digitisation", "value": "Trust EPR rollout drives training + change-mgmt + telephony cost"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove training-backfill + agency-coordination cost"},
            {"label": "Funding trajectory", "value": "2021-22 c. £2.9M → 2023-24 £3.3M → 2024-25 £3.555M"},
            {"label": "Delivery body", "value": "Trust corporate services + Finance + Digital + L&D + HR establishment functions"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + South Yorkshire ICB + Nottingham & Nottinghamshire ICB"},
            {"label": "Evaluation evidence", "value": "Model Hospital corporate-services benchmarks; CQC RP5 inspection; Trust ARA disclosure"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2017 stand-alone Doncaster + Bassetlaw arrangements · Successor: continued cross-ICS coordination + GM-style shared back-office options"}
        ],
        "notes": "Doncaster and Bassetlaw Teaching Hospitals NHS FT's establishment-costs line reflects a three-site footprint that uniquely spans two integrated care systems — Doncaster Royal Infirmary and Montagu sit within South Yorkshire ICS while Bassetlaw Hospital (Worksop) sits within Nottinghamshire ICS — generating cross-ICB coordination cost in corporate services, finance and digital. Teaching-hospital status supports a substantial training and L&D establishment baseline. The NHSE Frontline Digitisation EPR rollout has driven training, change-management and telephony cost. Industrial action 2023-24 drove training-backfill and agency-coordination cost across all three sites. April 2025 employer-NIC step-up and CPI on professional services feed forward pressure into 2025-26.",
        "sources": [
            {"publisher": "Doncaster and Bassetlaw Teaching Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.dbth.nhs.uk/about-us/publications/"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/frontline-digitisation/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Doncaster and Bassetlaw provider profile (RP5)", "url": "https://www.cqc.org.uk/provider/RP5"},
            {"publisher": "South Yorkshire ICB", "title": "Estate and digital strategy", "url": "https://syics.co.uk/"}
        ],
        "related": ["Doncaster and Bassetlaw Teaching Hospitals NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Establishment costs — Bolton NHS Foundation Trust", "Establishment costs — Calderdale and Huddersfield NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Transport (business + patient) — Hampshire Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "Hampshire Hospitals NHS Foundation Trust"}],
        "description": "Hampshire Hospitals NHS FT's £3.503M transport line covers business mileage, inter-site patient transfers and Non-Emergency Patient Transport Services across the trust's three-DGH footprint — Royal Hampshire County Hospital (Winchester), Basingstoke and North Hampshire Hospital, and Andover War Memorial Hospital. The dispersed rural Hampshire footprint generates substantial inter-site clinical-transfer demand, and the trust uses South Central Ambulance Service plus accredited NEPTS contractors for patient transport. AHP and community-team mileage adds to the line.",
        "beneficiaries": "c. 5,500 WTE staff serving a c. 600,000 north + mid Hampshire catchment (Winchester, Basingstoke, Andover, Alton, Romsey); c. 130,000 ED attendances/yr (Winchester + Basingstoke EDs combined); c. 60,000 admissions/yr; rural-spread catchment generates above-peer PTS demand.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · IFRS 16 Leases (pool fleet) · NHS Act 2006 · Mental Health Act 1983 (s.135/136 conveyance) · NHSE Patient Transport Services Eligibility Framework 2022 · HMRC AMAP · NHS AfC Section 17",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£3.503M"},
            {"label": "Trust scale", "value": "Three-DGH (Royal Hampshire County Winchester + Basingstoke + Andover War Memorial); c. 5,500 WTE"},
            {"label": "Inter-site transfers", "value": "Cross-site clinical specialty split (Winchester ↔ Basingstoke) drives inter-DGH PTS + business mileage; dispersed rural footprint elevates mileage vs urban peers"},
            {"label": "PTS provider mix", "value": "South Central Ambulance Service (SCAS) + accredited NEPTS contractors — re-tendered via Hampshire & Isle of Wight ICS"},
            {"label": "Staff mileage rate", "value": "NHS Agenda for Change Section 17 / HMRC AMAP 45p first 10,000 miles + 25p thereafter"},
            {"label": "Pool fleet (IFRS 16)", "value": "Right-of-use depreciation + interest on leased pool vehicles for AHPs + community teams"},
            {"label": "Industrial action 2023-24 effect", "value": "Strike days drove ad-hoc inter-site transfers + locum mileage claims"},
            {"label": "Funding trajectory", "value": "2021-22 c. £2.9M → 2023-24 £3.3M → 2024-25 £3.503M — fuel CPI + activity recovery"},
            {"label": "Delivery body", "value": "Trust E&F + Travel team + SCAS PTS + accredited NEPTS contractors"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + NHSE NEPTS framework + Hampshire & Isle of Wight ICB"},
            {"label": "Evaluation evidence", "value": "NHSE NEPTS Eligibility Framework 2022 review; CQC RN5 inspection; Trust ARA disclosure"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2012 separate Winchester + Basingstoke trust transport baselines (merger 2012) · Successor: HIOW ICS shared-fleet pooling + EV transition"}
        ],
        "notes": "Hampshire Hospitals NHS FT's transport line is structurally elevated by the dispersed rural three-DGH footprint, with cross-site clinical-specialty split between Winchester and Basingstoke driving inter-DGH PTS and business-mileage demand. The trust was formed by the 2012 merger of Winchester & Eastleigh Healthcare with Basingstoke & North Hampshire NHS FT plus Andover community services. South Central Ambulance Service runs PTS alongside accredited NEPTS contractors re-tendered via Hampshire & Isle of Wight ICS. Industrial action 2023-24 drove ad-hoc inter-site transfers and locum-mileage claims. April 2025 NIC step-up affects PTS-contractor pass-through; CPI fuel pressure remains the dominant driver. HIOW ICS shared-fleet pooling and EV transition are medium-term levers.",
        "sources": [
            {"publisher": "Hampshire Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.hampshirehospitals.nhs.uk/about-us/publications/"},
            {"publisher": "NHS England", "title": "Non-Emergency Patient Transport Services Eligibility Framework 2022", "url": "https://www.england.nhs.uk/long-read/non-emergency-patient-transport-services-eligibility-framework/"},
            {"publisher": "South Central Ambulance Service NHS Foundation Trust", "title": "Annual Report 2023-24", "url": "https://www.scas.nhs.uk/about-us/publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Hampshire Hospitals provider profile (RN5)", "url": "https://www.cqc.org.uk/provider/RN5"}
        ],
        "related": ["Hampshire Hospitals NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Transport (business + patient) — University Hospitals of Morecambe Bay NHS Foundation Trust", "South Central Ambulance Service NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Lease expenditure — Bedfordshire Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Lease expenditure", "parent": "Bedfordshire Hospitals NHS Foundation Trust"}],
        "description": "Bedfordshire Hospitals NHS FT's £3.496M lease expenditure line covers IFRS 16 right-of-use depreciation and interest plus residual operating-lease costs across the trust's two-DGH footprint at Bedford Hospital and Luton & Dunstable University Hospital, formed by the April 2020 merger of Bedford Hospital NHS Trust with Luton and Dunstable University Hospital NHS FT. The line covers leased property (NHSPS / community sites + clinical-equipment leases + pool-fleet vehicles + photocopier/IT leases) under the post-2022 IFRS 16 transition.",
        "beneficiaries": "c. 8,500 WTE staff serving a c. 690,000 Bedfordshire + parts of Hertfordshire catchment; c. 235,000 ED attendances/yr (Luton & Dunstable + Bedford EDs combined); c. 110,000 admissions/yr; the Luton & Dunstable site is in the original New Hospital Programme cohort.",
        "legal_basis": "IFRS 16 Leases (post-2022 transition) · DHSC Group Accounting Manual 2024-25 (chapter 7) · Landlord and Tenant Act 1954 (commercial tenancy) · IAS 36 Impairment of Assets · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "Lease expenditure 2024-25", "value": "£3.496M"},
            {"label": "Trust scale", "value": "Two-DGH (Bedford Hospital + Luton & Dunstable University Hospital) post-Apr 2020 merger; c. 8,500 WTE"},
            {"label": "Lease classes", "value": "Property (NHSPS + community sites + L&T 1954 commercial leases — Pt II security of tenure unless contracted out) + clinical equipment (MRI/CT/dialysis hybrid HMRC + IFRS 16) + pool fleet + photocopier/IT"},
            {"label": "IFRS 16 transition (2022)", "value": "Apr 2022 IFRS 16 adoption brought formerly-operating leases on-balance-sheet — split right-of-use asset depreciation + interest unwind"},
            {"label": "NHP context", "value": "Luton & Dunstable in original NHP cohort; Jan 2025 NHP Reset deferred new build — preserves current lease baseline"},
            {"label": "Merger context", "value": "Apr 2020 merger of Bedford Hospital NHS Trust + Luton & Dunstable NHS FT formed Bedfordshire Hospitals NHS FT — consolidated lease portfolio"},
            {"label": "April 2025 NIC + CPI uplift", "value": "Apr 2025 employer-NIC step-up affects pass-through on managed property leases; CPI feeds rent reviews"},
            {"label": "Funding trajectory", "value": "2021-22 c. £2.8M → 2022-23 IFRS 16 transition step-up → 2024-25 £3.496M"},
            {"label": "Delivery body", "value": "Trust E&F + Finance + NHS Property Services (NHSPS) + Community Health Partnerships (LIFT) + commercial landlords"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + Bedfordshire, Luton and Milton Keynes ICB"},
            {"label": "Evaluation evidence", "value": "NHSPS annual report; CQC RC9 inspection; Trust ARA lease note (IFRS 16 disclosure); merger benefits-realisation review"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-Apr 2020 separate Bedford + Luton & Dunstable lease portfolios + pre-2022 IAS 17 operating-lease treatment · Successor: post-NHP-Reset Luton & Dunstable rebuild + lease portfolio rationalisation"}
        ],
        "notes": "Bedfordshire Hospitals NHS FT's lease-expenditure line reflects the two-DGH portfolio formed by the April 2020 merger of Bedford Hospital NHS Trust with Luton and Dunstable NHS FT, with the post-Apr 2022 IFRS 16 transition having brought formerly-operating leases on-balance-sheet — splitting right-of-use asset depreciation from interest unwind under DHSC GAM ch.7. NHS Property Services holds the dominant property-lease portfolio for satellite sites alongside Community Health Partnerships LIFT vehicles, with smaller commercial leases benefiting from L&T 1954 Part II security of tenure unless contracted out. The Luton & Dunstable site sits in the original NHP cohort, with the January 2025 NHP Reset deferring the planned new build — preserving the current lease baseline.",
        "sources": [
            {"publisher": "Bedfordshire Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.bedfordshirehospitals.nhs.uk/about-us/publications/"},
            {"publisher": "NHS Property Services", "title": "Annual Report 2023-24", "url": "https://www.property.nhs.uk/about/annual-reports/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 7 — Leases)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Department of Health and Social Care", "title": "New Hospital Programme — Plan for Implementation (Jan 2025 Reset)", "url": "https://www.gov.uk/government/publications/new-hospital-programme-plan-for-implementation"},
            {"publisher": "Care Quality Commission", "title": "Bedfordshire Hospitals provider profile (RC9)", "url": "https://www.cqc.org.uk/provider/RC9"}
        ],
        "related": ["Bedfordshire Hospitals NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "NHS Property Services", "Lease expenditure — Northern Care Alliance NHS Foundation Trust", "New Hospital Programme"]
    },
    "Transport (business + patient) — University Hospitals of Morecambe Bay NHS Foundation Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "University Hospitals of Morecambe Bay NHS Foundation Trust"}],
        "description": "UHMB's £3.479M transport line covers business mileage, inter-site patient transfers and Non-Emergency Patient Transport Services across the trust's geographically dispersed three-site footprint — Royal Lancaster Infirmary (Lancaster), Furness General Hospital (Barrow-in-Furness) and Westmorland General Hospital (Kendal). The trust's catchment spans the Lake District and the Furness peninsula — one of England's most geographically challenging acute footprints — driving above-peer PTS demand for inter-site transfers and tertiary referrals to Manchester/Preston.",
        "beneficiaries": "c. 5,500 WTE staff serving a c. 365,000 north Lancashire + south Cumbria + Lake District catchment; c. 130,000 ED attendances/yr (Royal Lancaster + Furness General EDs); c. 60,000 admissions/yr; the Furness peninsula is one of England's most isolated acute footprints, sustaining inter-site transfer demand to Royal Lancaster + tertiary referrals.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · IFRS 16 Leases (pool fleet) · NHS Act 2006 · Mental Health Act 1983 (s.135/136 conveyance) · NHSE Patient Transport Services Eligibility Framework 2022 · HMRC AMAP · NHS AfC Section 17",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£3.479M"},
            {"label": "Trust scale", "value": "Three-site dispersed (Royal Lancaster + Furness General Barrow + Westmorland General Kendal); c. 5,500 WTE"},
            {"label": "Geographic context", "value": "Spans Lake District + Furness peninsula — one of England's most geographically isolated acute footprints (45-60 mile inter-site distances); cross-Lake-District inter-site transfers + tertiary referrals to Preston/Manchester drive above-peer PTS volume per WTE"},
            {"label": "PTS provider mix", "value": "North West Ambulance Service (NWAS) PTS + accredited NEPTS contractors — Lancashire & South Cumbria ICS commissioning"},
            {"label": "Staff mileage rate", "value": "NHS AfC Section 17 / HMRC AMAP 45p first 10,000 miles + 25p thereafter — high mileage claims given dispersed sites"},
            {"label": "Pool fleet (IFRS 16)", "value": "Right-of-use depreciation + interest on leased pool vehicles for AHPs + community teams"},
            {"label": "Industrial action 2023-24 effect", "value": "Strike days drove ad-hoc inter-site transfers + locum mileage claims"},
            {"label": "Funding trajectory", "value": "2021-22 c. £2.8M → 2023-24 £3.3M → 2024-25 £3.479M — fuel CPI + activity recovery"},
            {"label": "Delivery body", "value": "Trust E&F + Travel team + NWAS PTS + accredited NEPTS contractors"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + NHSE NEPTS framework + Lancashire & South Cumbria ICB"},
            {"label": "Evaluation evidence", "value": "NHSE NEPTS Eligibility Framework 2022 review; Morecambe Bay Investigation 2015 (Kirkup) historical context; CQC RTX inspection; Trust ARA disclosure"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-1998 separate Lancaster + Barrow trusts · Successor: LSC ICS shared-fleet pooling + EV transition"}
        ],
        "notes": "UHMB's transport line is structurally elevated by an exceptionally dispersed three-site footprint — Royal Lancaster Infirmary, Furness General (Barrow, c. 50 miles from Lancaster across the Lake District) and Westmorland General (Kendal) — generating above-peer PTS volume per WTE for inter-site transfers and tertiary referrals to Preston and Manchester. The Furness peninsula's geographic isolation has historically shaped clinical risk and service-design choices, including the 2015 Kirkup-led Morecambe Bay Investigation. NWAS runs PTS alongside accredited NEPTS contractors via LSC ICS. Industrial action 2023-24 added ad-hoc transfer demand. April 2025 NIC step-up affects pass-through; CPI fuel pressure dominates.",
        "sources": [
            {"publisher": "University Hospitals of Morecambe Bay NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.uhmb.nhs.uk/about-us/our-publications"},
            {"publisher": "NHS England", "title": "Non-Emergency Patient Transport Services Eligibility Framework 2022", "url": "https://www.england.nhs.uk/long-read/non-emergency-patient-transport-services-eligibility-framework/"},
            {"publisher": "North West Ambulance Service NHS Trust", "title": "Annual Report 2023-24", "url": "https://www.nwas.nhs.uk/about-us/publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "UHMB provider profile (RTX)", "url": "https://www.cqc.org.uk/provider/RTX"}
        ],
        "related": ["University Hospitals of Morecambe Bay NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Transport (business + patient) — Hampshire Hospitals NHS Foundation Trust", "North West Ambulance Service NHS Trust", "Department of Health and Social Care"]
    },
    "General supplies & services — Tameside and Glossop Integrated Care NHS Foundation Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "Tameside and Glossop Integrated Care NHS Foundation Trust"}],
        "description": "Tameside and Glossop Integrated Care NHS FT's £3.452M general supplies & services line covers non-clinical consumables, linen, catering, hotel-services materials, office supplies and minor expensed equipment at Tameside General Hospital plus integrated borough community services across Tameside (Greater Manchester) and Glossop (Derbyshire). The trust is one of the early integrated acute + community trusts under the GM Combined Authority devolved-health envelope, and the cross-county Glossop community footprint adds consumables consumption breadth.",
        "beneficiaries": "c. 4,500 WTE staff serving a c. 250,000 Tameside borough + Glossop catchment; c. 100,000 ED attendances/yr at Tameside General ED; c. 45,000 admissions/yr; integrated community services including district nursing + therapies + community-paediatric across Tameside borough + Glossop.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 2 Inventories · Procurement Act 2023 · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "General supplies & services 2024-25", "value": "£3.452M"},
            {"label": "Trust scale", "value": "Single acute (Tameside General Hospital, Ashton-under-Lyne) + Tameside borough + Glossop community services; c. 4,500 WTE"},
            {"label": "ED throughput", "value": "c. 100,000 ED attendances/yr"},
            {"label": "Cross-county footprint", "value": "Trust spans Tameside borough (GM ICS) + Glossop (Derbyshire ICS) — cross-ICB procurement coordination; integrated acute + community (re-branded 'Integrated Care' 2016) drives consumables breadth"},
            {"label": "Procurement route", "value": "NHS Supply Chain national framework + trust-direct contracts + GM ICS procurement collaborative + Derbyshire ICS interface"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove agency backfill + cancellation-related re-stocking churn"},
            {"label": "April 2025 NIC + CPI uplift", "value": "Apr 2025 employer-NIC step-up + sustained non-clinical CPI feed forward unit-cost pressure"},
            {"label": "Funding trajectory", "value": "2021-22 c. £2.8M → 2023-24 £3.2M → 2024-25 £3.452M"},
            {"label": "Delivery body", "value": "Trust Procurement + NHS Supply Chain + GM ICS procurement collaborative + Tameside MBC interface"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Greater Manchester ICB + Derbyshire ICB (Glossop)"},
            {"label": "Evaluation evidence", "value": "Model Hospital benchmarks; CQC RMP inspection; Trust ARA disclosure; GM Combined Authority devolved-health reviews"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2016 pre-integrated-care branding + pre-2011 separate acute + Tameside PCT community baselines · Successor: GM ICS collaborative procurement scaling + Derbyshire interface"}
        ],
        "notes": "Tameside and Glossop Integrated Care NHS FT's general supplies & services line reflects integrated acute + community workforce — Tameside General alongside borough-wide community services (district nursing, therapies, community-paediatric) across Tameside (GM) and Glossop (Derbyshire), making it one of the earliest acute + community integrated trusts. The cross-county footprint generates cross-ICB procurement coordination. Industrial action 2023-24 drove cancellation-related re-stocking and agency-backfill consumable use. The Procurement Act 2023 regime is reshaping framework call-off patterns. April 2025 NIC step-up and non-clinical CPI feed forward pressure. GM Combined Authority devolved-health shapes medium-term collaboration.",
        "sources": [
            {"publisher": "Tameside and Glossop Integrated Care NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.tamesidehospital.nhs.uk/about-us/publications.htm"},
            {"publisher": "NHS Supply Chain", "title": "Annual Report 2023-24", "url": "https://www.supplychain.nhs.uk/about-us/our-publications/"},
            {"publisher": "Greater Manchester Combined Authority", "title": "Health and care devolution", "url": "https://www.greatermanchester-ca.gov.uk/what-we-do/health/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Tameside and Glossop provider profile (RMP)", "url": "https://www.cqc.org.uk/provider/RMP"}
        ],
        "related": ["Tameside and Glossop Integrated Care NHS Foundation Trust", "Clinical Supplies & Drugs", "NHS Acute Trusts", "General supplies & services — Liverpool University Hospitals NHS Foundation Trust", "NHS Supply Chain", "Greater Manchester Integrated Care Board"]
    },
    "Transport (business + patient) — North West Anglia NHS Foundation Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "North West Anglia NHS Foundation Trust"}],
        "description": "North West Anglia NHS FT's £3.444M transport line covers business mileage, inter-site patient transfers and Non-Emergency Patient Transport Services across the trust's three-DGH cross-county footprint — Peterborough City Hospital (PFI-built 2010), Hinchingbrooke Hospital (Huntingdon) and Stamford and Rutland Hospital. Formed by the April 2017 merger of Peterborough and Stamford Hospitals NHS FT with Hinchingbrooke Healthcare NHS Trust, the dispersed Cambridgeshire + Peterborough + Lincolnshire/Rutland footprint generates substantial PTS demand.",
        "beneficiaries": "c. 6,500 WTE staff serving a c. 800,000 Peterborough + Cambridgeshire + south Lincolnshire + Rutland catchment; c. 200,000 ED attendances/yr (Peterborough City + Hinchingbrooke EDs combined); c. 90,000 admissions/yr; cross-county dispersed footprint generates above-peer PTS demand.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · IFRS 16 Leases (pool fleet) · NHS Act 2006 · Mental Health Act 1983 (s.135/136 conveyance) · NHSE Patient Transport Services Eligibility Framework 2022 · HMRC AMAP · NHS AfC Section 17",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£3.444M"},
            {"label": "Trust scale", "value": "Three-DGH dispersed (Peterborough City PFI 2010 + Hinchingbrooke + Stamford & Rutland); c. 6,500 WTE"},
            {"label": "Cross-county footprint", "value": "Spans Peterborough (C&P ICS) + Cambridgeshire (Hinchingbrooke) + Lincolnshire/Rutland (Stamford) — generates inter-county PTS + inter-DGH business mileage given clinical-specialty rotation"},
            {"label": "PTS provider mix", "value": "East of England Ambulance Service (EEAST) + accredited NEPTS contractors — Cambs & Peterborough ICS commissioning"},
            {"label": "Staff mileage rate", "value": "NHS AfC Section 17 / HMRC AMAP 45p first 10,000 miles + 25p thereafter"},
            {"label": "Pool fleet (IFRS 16)", "value": "Right-of-use depreciation + interest on leased pool vehicles for AHPs + community teams"},
            {"label": "Industrial action 2023-24 effect", "value": "Strike days drove ad-hoc inter-site transfers + locum mileage claims"},
            {"label": "Funding trajectory", "value": "2021-22 c. £2.8M → 2023-24 £3.2M → 2024-25 £3.444M — fuel CPI + activity recovery; Apr 2017 merger of Peterborough & Stamford NHS FT + Hinchingbrooke formed NWAFT"},
            {"label": "Delivery body", "value": "Trust E&F + Travel team + EEAST PTS + accredited NEPTS contractors"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + NHSE NEPTS framework + Cambridgeshire & Peterborough ICB"},
            {"label": "Evaluation evidence", "value": "NHSE NEPTS Eligibility Framework 2022 review; CQC RGN inspection; Trust ARA disclosure; merger benefits-realisation review"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-Apr 2017 separate Peterborough & Stamford + Hinchingbrooke baselines · Successor: C&P ICS shared-fleet pooling + EV transition"}
        ],
        "notes": "North West Anglia NHS FT was formed by the April 2017 merger of Peterborough and Stamford Hospitals NHS FT with Hinchingbrooke Healthcare NHS Trust — the latter notable as the site of the controversial Circle franchise hand-back in 2015 — consolidating a dispersed three-DGH footprint spanning Peterborough (C&P ICS), Cambridgeshire and Lincolnshire/Rutland. The cross-county footprint generates above-peer PTS demand and inter-DGH business-mileage volume given clinical-specialty rotation. EEAST runs PTS alongside accredited NEPTS contractors commissioned via C&P ICS. Industrial action 2023-24 drove ad-hoc inter-site transfers and locum-mileage claims. April 2025 NIC step-up affects pass-through; CPI fuel pressure dominates.",
        "sources": [
            {"publisher": "North West Anglia NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.nwangliaft.nhs.uk/about-us/publications/"},
            {"publisher": "NHS England", "title": "Non-Emergency Patient Transport Services Eligibility Framework 2022", "url": "https://www.england.nhs.uk/long-read/non-emergency-patient-transport-services-eligibility-framework/"},
            {"publisher": "East of England Ambulance Service NHS Trust", "title": "Annual Report 2023-24", "url": "https://www.eastamb.nhs.uk/about-us/our-publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "North West Anglia provider profile (RGN)", "url": "https://www.cqc.org.uk/provider/RGN"}
        ],
        "related": ["North West Anglia NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Transport (business + patient) — Hampshire Hospitals NHS Foundation Trust", "Transport (business + patient) — University Hospitals of Morecambe Bay NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Establishment costs — Ashford and St Peter's Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "Ashford and St Peter's Hospitals NHS Foundation Trust"}],
        "description": "ASPH's £3.440M establishment costs line covers non-clinical operating overheads — printing, postage, telephony, training, professional fees, conference and travel-related establishment, courier services and ancillary running costs — across the trust's two-site footprint at St Peter's Hospital (Chertsey, main acute) and Ashford Hospital (urgent treatment + outpatient). The trust is in the original New Hospital Programme cohort with planned major rebuild deferred under the January 2025 NHP Reset, preserving the current establishment baseline through 2025-26.",
        "beneficiaries": "c. 4,500 WTE staff serving a c. 410,000 north-west Surrey catchment (Runnymede, Spelthorne, Surrey Heath, Woking); c. 130,000 ED attendances/yr (St Peter's main ED + Ashford Walk-in); c. 65,000 admissions/yr; large maternity unit at St Peter's.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£3.440M"},
            {"label": "Trust scale", "value": "Two-site (St Peter's Hospital Chertsey + Ashford Hospital); c. 4,500 WTE"},
            {"label": "Composition", "value": "Printing + postage + telephony + training + professional fees + conference/travel + corporate establishment"},
            {"label": "NHP context", "value": "Original NHP cohort; Jan 2025 NHP Reset deferred new build into next financing window — preserves current establishment baseline"},
            {"label": "ED throughput", "value": "c. 130,000 attendances/yr (St Peter's main + Ashford Walk-in)"},
            {"label": "EPR + Frontline Digitisation", "value": "Trust EPR rollout drives training + change-mgmt + telephony establishment cost"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove training-backfill + agency-coordination cost"},
            {"label": "Funding trajectory", "value": "2021-22 c. £2.8M → 2023-24 £3.2M → 2024-25 £3.440M; Apr 2025 NIC step-up + CPI on professional services feed forward pressure"},
            {"label": "Delivery body", "value": "Trust corporate services + Finance + Digital + L&D + HR establishment functions"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Surrey Heartlands ICB"},
            {"label": "Evaluation evidence", "value": "Model Hospital corporate-services benchmarks; CQC RTK inspection; NHP Reset announcement Jan 2025; Trust ARA disclosure"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2007 separate Ashford Hospital Trust + St Peter's Hospital baselines · Successor: post-NHP-Reset rebuild path + Surrey Heartlands ICS shared back-office options"}
        ],
        "notes": "Ashford and St Peter's Hospitals NHS FT's establishment-costs line reflects a two-site footprint serving north-west Surrey, with the trust in the original New Hospital Programme cohort. The January 2025 NHP Reset deferred the planned new build into the next financing cycle, preserving the current establishment baseline through 2025-26 rather than triggering accelerated change-management cost. The NHSE Frontline Digitisation EPR rollout has driven training, change-management and telephony cost. Industrial action 2023-24 added training-backfill and agency-coordination cost across the 44 junior-doctor and 10 consultant strike days. April 2025 employer-NIC step-up and CPI on professional services feed forward pressure. Surrey Heartlands ICS shared back-office consolidation is a medium-term lever.",
        "sources": [
            {"publisher": "Ashford and St Peter's Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.ashfordstpeters.nhs.uk/annual-reports"},
            {"publisher": "Department of Health and Social Care", "title": "New Hospital Programme — Plan for Implementation (Jan 2025 Reset)", "url": "https://www.gov.uk/government/publications/new-hospital-programme-plan-for-implementation"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/frontline-digitisation/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "ASPH provider profile (RTK)", "url": "https://www.cqc.org.uk/provider/RTK"}
        ],
        "related": ["Ashford and St Peter's Hospitals NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Establishment costs — Bolton NHS Foundation Trust", "Establishment costs — Calderdale and Huddersfield NHS Foundation Trust", "New Hospital Programme"]
    },
    "Transport (business + patient) — York and Scarborough Teaching Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "York and Scarborough Teaching Hospitals NHS Foundation Trust"}],
        "description": "York and Scarborough Teaching Hospitals NHS FT's £3.409M transport line covers business mileage, inter-site patient transfers and Non-Emergency Patient Transport Services across the trust's geographically dispersed York + North Yorkshire footprint — York Hospital (main DGH), Scarborough Hospital (coastal DGH), Bridlington Hospital (East Riding), Selby War Memorial, Malton, Whitby and St Monica's Easingwold community hospitals. The c. 40-mile York-to-Scarborough split plus rural North Yorkshire Moors footprint generates above-peer PTS demand.",
        "beneficiaries": "c. 9,000 WTE staff serving a c. 800,000 York + North Yorkshire + parts of East Riding catchment; c. 200,000 ED attendances/yr (York Hospital + Scarborough Hospital EDs combined); c. 100,000 admissions/yr; rural-coastal dispersed footprint sustains substantial inter-site PTS volume.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · IFRS 16 Leases (pool fleet) · NHS Act 2006 · Mental Health Act 1983 (s.135/136 conveyance) · NHSE Patient Transport Services Eligibility Framework 2022 · HMRC AMAP · NHS AfC Section 17",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£3.409M"},
            {"label": "Trust scale", "value": "Two-DGH (York + Scarborough) + Bridlington + multiple community hospitals (Selby, Malton, Whitby, Easingwold); c. 9,000 WTE; teaching status"},
            {"label": "Geographic context", "value": "York-to-Scarborough c. 40 miles across North Yorkshire Moors + coastal Bridlington + dispersed rural community-hospital network"},
            {"label": "Inter-site PTS demand", "value": "Cross-Moors York ↔ Scarborough inter-site transfers + tertiary referrals to Hull/Leeds drive above-peer PTS volume"},
            {"label": "PTS provider mix", "value": "Yorkshire Ambulance Service (YAS) + accredited NEPTS contractors — Humber and North Yorkshire ICS commissioning"},
            {"label": "Staff mileage rate", "value": "NHS AfC Section 17 / HMRC AMAP 45p first 10,000 miles + 25p thereafter — high mileage given dispersed sites"},
            {"label": "Pool fleet (IFRS 16)", "value": "Right-of-use depreciation + interest on leased pool vehicles for AHPs + community teams"},
            {"label": "Industrial action 2023-24 effect", "value": "Strike days drove ad-hoc inter-site transfers + locum mileage claims"},
            {"label": "Funding trajectory", "value": "2021-22 c. £2.8M → 2023-24 £3.2M → 2024-25 £3.409M — fuel CPI + activity recovery"},
            {"label": "Delivery body", "value": "Trust E&F + Travel team + YAS PTS + accredited NEPTS contractors"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + NHSE NEPTS framework + Humber and North Yorkshire ICB"},
            {"label": "Evaluation evidence", "value": "NHSE NEPTS Eligibility Framework 2022 review; CQC RCB inspection; Trust ARA disclosure"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2012 York Hospitals NHS FT pre-Scarborough-acquisition baseline · Successor: HNY ICS shared-fleet pooling + EV transition"}
        ],
        "notes": "York and Scarborough Teaching Hospitals NHS FT's transport line is structurally elevated by an exceptionally dispersed York + North Yorkshire footprint — the c. 40-mile York-to-Scarborough split across the North Yorkshire Moors plus coastal Bridlington and a network of small community hospitals (Selby, Malton, Whitby, Easingwold) generates above-peer PTS volume per WTE for inter-site transfers and tertiary referrals to Hull and Leeds. The 2012 acquisition of Scarborough and North East Yorkshire NHS Trust by York Teaching Hospitals NHS FT baselined the current footprint. Yorkshire Ambulance Service runs PTS alongside accredited NEPTS contractors via Humber and North Yorkshire ICS. Industrial action 2023-24 added ad-hoc transfer demand. April 2025 NIC step-up affects pass-through; CPI fuel pressure dominates.",
        "sources": [
            {"publisher": "York and Scarborough Teaching Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.yorkhospitals.nhs.uk/about-us/publications/"},
            {"publisher": "NHS England", "title": "Non-Emergency Patient Transport Services Eligibility Framework 2022", "url": "https://www.england.nhs.uk/long-read/non-emergency-patient-transport-services-eligibility-framework/"},
            {"publisher": "Yorkshire Ambulance Service NHS Trust", "title": "Annual Report 2023-24", "url": "https://www.yas.nhs.uk/about-us/publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "York and Scarborough provider profile (RCB)", "url": "https://www.cqc.org.uk/provider/RCB"}
        ],
        "related": ["York and Scarborough Teaching Hospitals NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Transport (business + patient) — University Hospitals of Morecambe Bay NHS Foundation Trust", "Transport (business + patient) — North West Anglia NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Amortisation — University Hospitals Birmingham NHS Foundation Trust": {
        "aliases": [{"name": "Amortisation", "parent": "University Hospitals Birmingham NHS Foundation Trust"}],
        "description": "UHB's £3.395M amortisation line covers the systematic write-down of intangible assets — capitalised software licences, the trust's electronic patient record platform (Oracle Health/Cerner-based deployment), clinical-systems development costs and capitalised research informatics — under IAS 38 useful-economic-life conventions and DHSC GAM ch.5. UHB is one of the NHS's largest acute trusts (Queen Elizabeth Hospital Birmingham, Heartlands, Good Hope, Solihull) and a major Frontline Digitisation site, driving substantial intangible-asset capitalisation pipeline.",
        "beneficiaries": "c. 22,000 WTE staff serving a c. 2.2M Birmingham + Solihull catchment plus tertiary specialty referrals (cardiac, liver/renal transplant, MTC, military rehabilitation); c. 470,000 ED attendances/yr across QEHB + Heartlands + Good Hope EDs; c. 230,000 admissions/yr; QEHB hosts the Royal Centre for Defence Medicine.",
        "legal_basis": "IAS 38 Intangible Assets · DHSC Group Accounting Manual 2024-25 (chapter 5) · IAS 36 Impairment of Assets · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£3.395M"},
            {"label": "Trust scale", "value": "Four-site mega-trust (QEHB + Heartlands + Good Hope + Solihull) post-Apr 2018 HEFT acquisition; c. 22,000 WTE"},
            {"label": "Asset class", "value": "Capitalised software licences + EPR platform + clinical systems development + capitalised research informatics + capitalised website / patient-portal IP"},
            {"label": "EPR + Frontline Digitisation context", "value": "UHB is among the largest NHSE Frontline Digitisation deployers — capitalised licence + implementation + integration costs amortised over useful economic life"},
            {"label": "IAS 38 useful-life convention", "value": "Software licences typically 3-5 years; EPR core 5-10 years; per DHSC GAM ch.5 conventions"},
            {"label": "QEHB tertiary specialties", "value": "Major Trauma Centre + Royal Centre for Defence Medicine (UK military rehabilitation hub) + national liver transplant + cardiac — supports research-informatics intangible capitalisation"},
            {"label": "PFI estate interaction", "value": "QEHB PFI build (operational 2010) — separate IFRIC 12 line, not amortisation"},
            {"label": "Heartlands Foundation Group acquisition", "value": "Apr 2018 acquisition of Heart of England NHS FT (Heartlands + Good Hope + Solihull) consolidated estate + intangible portfolio"},
            {"label": "Funding trajectory", "value": "2021-22 c. £2.8M → 2023-24 £3.2M → 2024-25 £3.395M — sustained capitalisation pipeline"},
            {"label": "Delivery body", "value": "Trust Finance + Digital + EPR programme team + DHSC Frontline Digitisation funding + research-informatics partners (BHP)"},
            {"label": "Policy owner", "value": "DHSC + NHSE Transformation + NHSE Provider Finance + Birmingham and Solihull ICB"},
            {"label": "Evaluation evidence", "value": "NAO Digital transformation in the NHS report; Trust ARA intangible-asset note; CQC RRK inspection; Bewick Review 2022 (post-cultural-issues governance)"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-Apr 2018 stand-alone QEHB pre-Heartlands acquisition · Successor: continued Frontline Digitisation amortisation pipeline + group EPR consolidation"}
        ],
        "notes": "UHB's amortisation baseline reflects sustained capitalisation of intangible assets across one of the NHS's largest mega-trusts — the four-site footprint (Queen Elizabeth Hospital Birmingham, Heartlands, Good Hope and Solihull) was consolidated through the April 2018 acquisition of Heart of England NHS FT. The trust is among the largest NHSE Frontline Digitisation deployers, with capitalised EPR licences, implementation and integration cost amortised over IAS 38 useful-economic-life. The Royal Centre for Defence Medicine and tertiary specialties (cardiac, liver transplant, MTC) sustain a research-informatics intangible capitalisation pipeline through Birmingham Health Partners. QEHB's PFI build (operational 2010) is treated separately under IFRIC 12. The Bewick Review 2022 reshaped post-2022 governance oversight.",
        "sources": [
            {"publisher": "University Hospitals Birmingham NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.uhb.nhs.uk/about-us/publications/"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/frontline-digitisation/"},
            {"publisher": "National Audit Office", "title": "Digital transformation in the NHS (HC 1295, 2020)", "url": "https://www.nao.org.uk/reports/the-use-of-digital-technology-in-the-nhs/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 5 — intangibles)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "UHB provider profile (RRK)", "url": "https://www.cqc.org.uk/provider/RRK"}
        ],
        "related": ["University Hospitals Birmingham NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Amortisation — North Bristol NHS Trust", "Amortisation — Milton Keynes University Hospital NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Amortisation — Milton Keynes University Hospital NHS Foundation Trust": {
        "aliases": [{"name": "Amortisation", "parent": "Milton Keynes University Hospital NHS Foundation Trust"}],
        "description": "Milton Keynes University Hospital NHS FT's £3.375M amortisation line covers the systematic write-down of intangible assets — capitalised software licences, the trust's electronic patient record platform, clinical-systems development costs and capitalised digital-health programme work — under IAS 38 useful-economic-life conventions and DHSC GAM ch.5. The trust is a single-site DGH serving the Milton Keynes new-town catchment, with Frontline Digitisation EPR rollout driving recent intangible-asset capitalisation pipeline.",
        "beneficiaries": "c. 4,500 WTE staff serving a c. 320,000 Milton Keynes + parts of Buckinghamshire + Bedfordshire catchment; c. 110,000 ED attendances/yr; c. 50,000 admissions/yr; large maternity service serving the new-town's young demographic profile.",
        "legal_basis": "IAS 38 Intangible Assets · DHSC Group Accounting Manual 2024-25 (chapter 5) · IAS 36 Impairment of Assets · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£3.375M"},
            {"label": "Trust scale", "value": "Single-site DGH (Milton Keynes University Hospital, Eaglestone); c. 4,500 WTE; teaching status (associated with University of Buckingham + UCL)"},
            {"label": "Asset class", "value": "Capitalised software licences + EPR platform + clinical systems development + capitalised digital-health programme + capitalised website / patient-portal IP"},
            {"label": "EPR + Frontline Digitisation context", "value": "MKUH runs eCare EPR (one of NHSE Global Digital Exemplar successor sites) — capitalised licence + implementation amortised over useful economic life"},
            {"label": "IAS 38 useful-life convention", "value": "Software licences typically 3-5 years; EPR core 5-10 years; per DHSC GAM ch.5 conventions"},
            {"label": "Digital-maturity recognition", "value": "MKUH ranked among NHS digital-maturity leaders — drives intangible-asset capitalisation pipeline"},
            {"label": "New-town demographics", "value": "Milton Keynes new-town catchment with young demographic + sustained population growth — sustains digital-health investment case"},
            {"label": "Industrial action 2023-24 effect", "value": "Indirect — strike disruption affects clinical activity but not intangible-asset capitalisation"},
            {"label": "Funding trajectory", "value": "2021-22 c. £2.8M → 2023-24 £3.2M → 2024-25 £3.375M — sustained Frontline Digitisation capitalisation pipeline"},
            {"label": "Delivery body", "value": "Trust Finance + Digital + EPR programme team + DHSC Frontline Digitisation funding"},
            {"label": "Policy owner", "value": "DHSC + NHSE Transformation + NHSE Provider Finance + Bedfordshire, Luton and Milton Keynes ICB"},
            {"label": "Evaluation evidence", "value": "NAO Digital transformation in the NHS report; Trust ARA intangible-asset note; CQC RD8 inspection; NHSE digital-maturity assessments"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-EPR paper-record + smaller intangible base · Successor: continued Frontline Digitisation amortisation pipeline + BLMK ICS digital strategy"}
        ],
        "notes": "Milton Keynes University Hospital NHS FT's amortisation baseline reflects sustained capitalisation of intangible assets driven by the trust's position as one of the NHS's digital-maturity leaders. The eCare EPR platform — deployed during the NHSE Global Digital Exemplar wave and subsequently extended — drives the dominant intangible-asset class, with capitalised licence, implementation and integration cost amortised over IAS 38 useful-economic-life under DHSC GAM ch.5 conventions. The Milton Keynes new-town demographic profile — young population with sustained growth — supports the strategic digital-health investment case. The NHSE Frontline Digitisation programme funded through DHSC capital has driven post-2021 intangible-asset capitalisation. The trust holds teaching status with the University of Buckingham and UCL, supporting research-informatics work.",
        "sources": [
            {"publisher": "Milton Keynes University Hospital NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.mkuh.nhs.uk/about-us/publications"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/frontline-digitisation/"},
            {"publisher": "National Audit Office", "title": "Digital transformation in the NHS (HC 1295, 2020)", "url": "https://www.nao.org.uk/reports/the-use-of-digital-technology-in-the-nhs/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 5 — intangibles)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "MKUH provider profile (RD8)", "url": "https://www.cqc.org.uk/provider/RD8"}
        ],
        "related": ["Milton Keynes University Hospital NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Amortisation — North Bristol NHS Trust", "Amortisation — University Hospitals Birmingham NHS Foundation Trust", "Department of Health and Social Care"]
    },
}
