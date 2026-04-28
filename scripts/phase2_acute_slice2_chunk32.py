# -*- coding: utf-8 -*-
# Phase 2 Acute slice 2 — chunk 32 (17 NHS Acute Trust orphan sub-lines)
# Hand-curated trust-specific PROGRAMME-archetype enrichment entries.
# Structural contract per docs/archetype_briefs.md.

NEW = {
    "Establishment costs — Stockport NHS Foundation Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "Stockport NHS Foundation Trust"}],
        "description": "Stockport NHS FT's £1.765M establishment costs line covers GAM operating expenses outside the Establishment-payroll chain — chiefly office consumables, postage, telephony, training and conferences, recruitment advertising, subscriptions, books and publications, courier services and minor furniture / equipment below the capitalisation threshold across Stepping Hill Hospital and the trust's community footprint. Backfill agency administrative cost from the 2023-24 industrial-action cycle plus Frontline Digitisation EPR change-management training feeds the line.",
        "beneficiaries": "c. 5,200 WTE staff serving a c. 320,000 Stockport + south-east Greater Manchester catchment; c. 95,000 ED attendances/yr at Stepping Hill ED; c. 70,000 admissions/yr; trust runs Stepping Hill Hospital plus community services across the Stockport metropolitan footprint within the Greater Manchester ICS.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 — IAS 1 Presentation of Financial Statements — IAS 16 Property Plant and Equipment (capitalisation threshold) — NHS Act 2006 — Health and Care Act 2022 — HMRC training and subsistence rules",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£1.765M"},
            {"label": "Trust scale", "value": "Stepping Hill Hospital + Stockport community services; c. 5,200 WTE"},
            {"label": "Composition", "value": "Office consumables + postage + telephony + training & conferences + recruitment advertising + subscriptions + books/publications + minor furniture/equipment below cap threshold"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove cancellation rebooking + admin backfill + recruitment advertising spike"},
            {"label": "Frontline Digitisation EPR", "value": "EPR change-management training, conference and travel costs feed forward into Establishment line"},
            {"label": "April 2025 NIC step-up", "value": "Indirect via training-provider and recruitment-advertising contractor pass-through"},
            {"label": "Funding trajectory", "value": "2021-22 c. £1.4M → 2023-24 c. £1.65M → 2024-25 £1.765M — strike backfill + EPR training + CPI on consumables"},
            {"label": "Greater Manchester ICS", "value": "Member of Greater Manchester ICB; collaborative procurement, training and recruitment frameworks across GM"},
            {"label": "Delivery body", "value": "Trust Workforce + Procurement + Training & Development + IT + Communications + Finance"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + Greater Manchester ICB + DHSC + NHS Supply Chain (where used)"},
            {"label": "Evaluation evidence", "value": "Carter Lord review legacy on running costs; Model Hospital establishment-cost benchmark; Trust ARA 2023-24; CQC RWJ inspections"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-EPR baseline establishment-cost profile · Successor: post-EPR-stabilisation training-cost normalisation + GM-ICS shared-service consolidation"}
        ],
        "notes": "Stockport NHS FT's establishment-cost line is shaped by the convergence of three drivers — 2023-24 industrial-action backfill (44 days junior-doctor + 10 days consultant strikes drove admin rebooking, recruitment advertising and casual training spend), Frontline Digitisation EPR change-management training cycles, and HMRC subsistence and training-provider CPI uplifts. Stepping Hill Hospital sits within the Greater Manchester ICS with collaborative procurement and recruitment frameworks; the trust has a long-running history (Beverley Allitt-style nurse-poisoning investigation 2011-15 and subsequent governance overhaul) shaping its training and induction footprint. April 2025 employer NIC step-up (15% over £5k threshold) feeds indirectly via training-provider and recruitment-advertising contractor pass-through.",
        "sources": [
            {"publisher": "Stockport NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.stockport.nhs.uk/about-us/publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/frontline-digitisation/"},
            {"publisher": "Care Quality Commission", "title": "Stockport NHS Foundation Trust provider profile (RWJ)", "url": "https://www.cqc.org.uk/provider/RWJ"},
            {"publisher": "NHS Confederation", "title": "Greater Manchester Integrated Care System", "url": "https://www.nhsconfed.org/system/integrated-care-systems"}
        ],
        "related": ["Stockport NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Establishment costs — Barnsley Hospital NHS Foundation Trust", "PFI / LIFT charges — Stockport NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Business rates — Surrey And Sussex Healthcare NHS Trust": {
        "aliases": [{"name": "Business rates", "parent": "Surrey And Sussex Healthcare NHS Trust"}],
        "description": "SASH's £1.757M business-rates line covers non-domestic rate liability on East Surrey Hospital (Redhill) — the trust's principal acute site — plus modest community-clinic outposts in Crawley, Caterham and Horley. Rateable values are set by the VOA on the 2023 list (effective 1 April 2023) with rates calculated against the small / standard non-domestic multiplier set under the Local Government Finance Act 1988 (Sch 6) as amended by the Non-Domestic Rating (Multipliers and Private Finance) Act 2024. Surrey Heartlands ICS context.",
        "beneficiaries": "c. 4,500 WTE staff serving a c. 535,000 east Surrey + west Sussex catchment (Redhill, Reigate, Crawley, Horley, Horsham, Caterham); c. 130,000 ED attendances/yr at East Surrey Hospital ED; c. 75,000 admissions/yr; East Surrey is a designated Trauma Unit feeding St George's Major Trauma Centre.",
        "legal_basis": "Local Government Finance Act 1988 (Sch 6) — Non-Domestic Rating (Multipliers and Private Finance) Act 2024 — Valuation Office Agency 2023 rating list — DHSC Group Accounting Manual 2024-25 — NHS Act 2006 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£1.757M"},
            {"label": "Trust scale", "value": "East Surrey Hospital (Redhill) + Crawley/Caterham/Horley community outposts; c. 4,500 WTE"},
            {"label": "Principal hereditament", "value": "East Surrey Hospital (Redhill) — main acute site, Trauma Unit feeding St George's MTC"},
            {"label": "Rating list", "value": "VOA 2023 list (effective 1 April 2023); next revaluation 1 April 2026"},
            {"label": "Multiplier", "value": "Standard non-domestic multiplier per LGFA 1988 Sch 6 + NDR (Multipliers and Private Finance) Act 2024"},
            {"label": "Charitable relief", "value": "NHS trusts not eligible for mandatory 80% charitable relief — full liability borne (cf. independent-sector charity hospitals)"},
            {"label": "Funding trajectory", "value": "2021-22 c. £1.55M → 2023-24 c. £1.7M → 2024-25 £1.757M — 2023 list revaluation + multiplier uplift"},
            {"label": "Surrey Heartlands ICS", "value": "Member of Surrey Heartlands ICB (also serves Sussex residents — cross-ICS-border patient flow)"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + Finance + VOA (rateable-value setter) + Reigate & Banstead BC / Tandridge DC (billing authorities)"},
            {"label": "Policy owner", "value": "MHCLG (rates policy + multiplier) + VOA (valuations) + DHSC + NHSE Provider Finance + Surrey Heartlands ICB"},
            {"label": "Evaluation evidence", "value": "VOA rating-list publications; NAO local government finance reports; Trust ARA 2023-24 disclosure; CQC RTP inspections"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2017 VOA rating list · Successor: 2026 VOA revaluation + ongoing trust appeal of rateable values"}
        ],
        "notes": "SASH's business-rates line is a function of the VOA 2023 rating-list valuations on East Surrey Hospital (Redhill) — the trust's principal hereditament — with smaller liabilities on Crawley, Caterham and Horley community outposts. NHS trusts are not eligible for the mandatory 80% charitable rate relief enjoyed by independent-sector charity hospitals, so the full liability is borne by the trust. The Non-Domestic Rating (Multipliers and Private Finance) Act 2024 introduced the higher multiplier on £500k+ properties from April 2025 — material for East Surrey Hospital's main hereditament. The 1 April 2026 next revaluation is the medium-term lever for the trust to challenge valuations. Cross-ICS patient flow (serves both Surrey and West Sussex residents) shapes the operational footprint underpinning the rating value.",
        "sources": [
            {"publisher": "Surrey and Sussex Healthcare NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.surreyandsussex.nhs.uk/about-us/publications/"},
            {"publisher": "Valuation Office Agency", "title": "Find a business rates valuation (rating list)", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "Department for Levelling Up, Housing and Communities", "title": "Business rates: Non-Domestic Rating Act 2023 + 2024 Multipliers Act", "url": "https://www.gov.uk/government/collections/business-rates"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Surrey and Sussex Healthcare NHS Trust provider profile (RTP)", "url": "https://www.cqc.org.uk/provider/RTP"}
        ],
        "related": ["Surrey And Sussex Healthcare NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Business rates — East Sussex Healthcare NHS Trust", "Business rates — Royal Cornwall Hospitals NHS Trust", "Valuation Office Agency"]
    },
    "Business rates — East Sussex Healthcare NHS Trust": {
        "aliases": [{"name": "Business rates", "parent": "East Sussex Healthcare NHS Trust"}],
        "description": "ESHT's £1.754M business-rates line covers non-domestic rate liability across the trust's twin-DGH footprint — Conquest Hospital (Hastings) and Eastbourne DGH — plus Bexhill Hospital, Uckfield Community Hospital, Crowborough War Memorial Hospital and a network of Sussex community outposts. Rateable values are set by the VOA on the 2023 list with rates calculated against the LGFA 1988 (Sch 6) multiplier as amended by the NDR (Multipliers and Private Finance) Act 2024. Sussex ICS context.",
        "beneficiaries": "c. 7,500 WTE staff serving a c. 525,000 East Sussex catchment (Hastings, Eastbourne, Bexhill, Rother, Wealden, Lewes); c. 145,000 ED attendances/yr across Conquest ED + Eastbourne DGH ED; c. 90,000 admissions/yr; serves a high-deprivation Hastings + Bexhill coastal-strip population.",
        "legal_basis": "Local Government Finance Act 1988 (Sch 6) — Non-Domestic Rating (Multipliers and Private Finance) Act 2024 — Valuation Office Agency 2023 rating list — DHSC Group Accounting Manual 2024-25 — NHS Act 2006 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£1.754M"},
            {"label": "Trust scale", "value": "Conquest Hospital (Hastings) + Eastbourne DGH + Bexhill + Uckfield + Crowborough + community outposts; c. 7,500 WTE"},
            {"label": "Twin-DGH model", "value": "Conquest (Hastings) + Eastbourne DGH — historic 2014-2018 service-reconfiguration disputes (stroke, A&E, maternity)"},
            {"label": "Rating list", "value": "VOA 2023 list (effective 1 April 2023); next revaluation 1 April 2026"},
            {"label": "Multiplier", "value": "Standard non-domestic multiplier per LGFA 1988 Sch 6 + NDR (Multipliers and Private Finance) Act 2024 (higher tier on £500k+ hereditaments from April 2025)"},
            {"label": "Charitable relief", "value": "NHS trusts not eligible for mandatory 80% charitable relief — full liability borne"},
            {"label": "Funding trajectory", "value": "2021-22 c. £1.55M → 2023-24 c. £1.7M → 2024-25 £1.754M — 2023 list revaluation + multiplier uplift"},
            {"label": "Sussex ICS", "value": "Member of NHS Sussex ICB (Sussex Health and Care Partnership)"},
            {"label": "Delivery body", "value": "Trust E&F + Finance + VOA + Hastings BC / Eastbourne BC / Wealden DC / Rother DC (billing authorities)"},
            {"label": "Policy owner", "value": "MHCLG (rates policy + multiplier) + VOA (valuations) + DHSC + NHSE Provider Finance + NHS Sussex ICB"},
            {"label": "Evaluation evidence", "value": "VOA rating-list publications; CQC RXC inspections (2018 'inadequate' rating + subsequent improvement); Trust ARA 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2017 VOA rating list · Successor: 2026 VOA revaluation + East Sussex twin-DGH future review (ICS-led)"}
        ],
        "notes": "ESHT's business-rates line reflects the trust's twin-DGH footprint (Conquest Hastings + Eastbourne DGH) plus a network of community outposts in Bexhill, Uckfield and Crowborough — each separately rated by the VOA on the 2023 list. The trust has a long history of service-reconfiguration disputes (stroke services, A&E, maternity 2014-2018) and was rated 'inadequate' by CQC in 2018 with subsequent governance overhaul; the Sussex ICS-led twin-DGH future review is the medium-term lever. NHS trusts are not eligible for mandatory 80% charitable relief, so the full liability is borne. The April 2025 NDR (Multipliers and Private Finance) Act 2024 higher-tier multiplier on £500k+ hereditaments is material for both Conquest and Eastbourne DGH main sites.",
        "sources": [
            {"publisher": "East Sussex Healthcare NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.esht.nhs.uk/about-us/publications/"},
            {"publisher": "Valuation Office Agency", "title": "Find a business rates valuation (rating list)", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "Department for Levelling Up, Housing and Communities", "title": "Business rates: Non-Domestic Rating Act 2023 + 2024 Multipliers Act", "url": "https://www.gov.uk/government/collections/business-rates"},
            {"publisher": "Care Quality Commission", "title": "East Sussex Healthcare NHS Trust provider profile (RXC)", "url": "https://www.cqc.org.uk/provider/RXC"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"}
        ],
        "related": ["East Sussex Healthcare NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Business rates — Surrey And Sussex Healthcare NHS Trust", "Business rates — Royal Cornwall Hospitals NHS Trust", "Valuation Office Agency"]
    },
    "Business rates — Royal Cornwall Hospitals NHS Trust": {
        "aliases": [{"name": "Business rates", "parent": "Royal Cornwall Hospitals NHS Trust"}],
        "description": "RCHT's £1.740M business-rates line covers non-domestic rate liability across the trust's geographically dispersed Cornwall footprint — principally the Royal Cornwall Hospital Treliske (Truro), West Cornwall Hospital (Penzance) and St Michael's Hospital (Hayle) — plus community-outpatient outposts. As the only acute trust in Cornwall, the Royal Cornwall Hospital Treliske is the sole hereditament hosting trauma, stroke, cancer and tertiary services for the Cornish peninsula. Cornwall and Isles of Scilly ICS context.",
        "beneficiaries": "c. 6,000 WTE staff serving a c. 570,000 Cornwall + Isles of Scilly catchment plus c. 5M annual visitor surge; c. 90,000 ED attendances/yr at Treliske ED + c. 30,000 at West Cornwall MIU; c. 75,000 admissions/yr; sole acute provider for Cornwall — long ambulance and patient travel times reflect peninsula geography.",
        "legal_basis": "Local Government Finance Act 1988 (Sch 6) — Non-Domestic Rating (Multipliers and Private Finance) Act 2024 — Valuation Office Agency 2023 rating list — DHSC Group Accounting Manual 2024-25 — NHS Act 2006 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£1.740M"},
            {"label": "Trust scale", "value": "Royal Cornwall Hospital Treliske (Truro) + West Cornwall Hospital (Penzance) + St Michael's (Hayle) + community outposts; c. 6,000 WTE"},
            {"label": "Sole acute provider", "value": "Only acute trust in Cornwall — Treliske hosts all trauma, stroke, cancer and tertiary services for the peninsula"},
            {"label": "Rating list", "value": "VOA 2023 list (effective 1 April 2023); next revaluation 1 April 2026"},
            {"label": "Multiplier", "value": "Standard non-domestic multiplier per LGFA 1988 Sch 6 + NDR (Multipliers and Private Finance) Act 2024 higher tier on £500k+ from April 2025"},
            {"label": "Charitable relief", "value": "NHS trusts not eligible for mandatory 80% charitable relief — full liability borne"},
            {"label": "Funding trajectory", "value": "2021-22 c. £1.55M → 2023-24 c. £1.7M → 2024-25 £1.740M — 2023 list revaluation + multiplier uplift"},
            {"label": "Cornwall + IoS ICS", "value": "Member of Cornwall and the Isles of Scilly ICB; peninsula geography drives transport-cost interaction with rates"},
            {"label": "Delivery body", "value": "Trust E&F + Finance + VOA + Cornwall Council (unitary billing authority for whole peninsula)"},
            {"label": "Policy owner", "value": "MHCLG (rates policy + multiplier) + VOA (valuations) + DHSC + NHSE Provider Finance + Cornwall and IoS ICB"},
            {"label": "Evaluation evidence", "value": "VOA rating-list publications; CQC REF inspections (long history of 'requires improvement' to current rating); Trust ARA 2023-24; NAO ambulance response report"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2017 VOA rating list · Successor: 2026 VOA revaluation + Cornwall and IoS ICS estate-rationalisation"}
        ],
        "notes": "RCHT's business-rates line reflects the trust's status as the sole acute provider for Cornwall — the Royal Cornwall Hospital Treliske hereditament is the principal liability, with smaller assessments on West Cornwall Hospital (Penzance), St Michael's (Hayle) and community outposts. Cornwall Council is the unitary billing authority for the whole peninsula. The April 2025 higher-tier multiplier on £500k+ hereditaments under the NDR (Multipliers and Private Finance) Act 2024 is material for the Treliske main site. Peninsula geography drives long ambulance response times and patient travel, with the summer-visitor population surge inflating ED demand without corresponding rates relief. The 2026 VOA revaluation is the medium-term lever for the trust to challenge valuations.",
        "sources": [
            {"publisher": "Royal Cornwall Hospitals NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.royalcornwall.nhs.uk/about-us/publications/"},
            {"publisher": "Valuation Office Agency", "title": "Find a business rates valuation (rating list)", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "Department for Levelling Up, Housing and Communities", "title": "Business rates: Non-Domestic Rating Act 2023 + 2024 Multipliers Act", "url": "https://www.gov.uk/government/collections/business-rates"},
            {"publisher": "Care Quality Commission", "title": "Royal Cornwall Hospitals NHS Trust provider profile (REF)", "url": "https://www.cqc.org.uk/provider/REF"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"}
        ],
        "related": ["Royal Cornwall Hospitals NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Business rates — Surrey And Sussex Healthcare NHS Trust", "Business rates — East Sussex Healthcare NHS Trust", "Valuation Office Agency"]
    },
    "Lease expenditure — West Suffolk NHS Foundation Trust": {
        "aliases": [{"name": "Lease expenditure", "parent": "West Suffolk NHS Foundation Trust"}],
        "description": "WSFT's £1.722M lease-expenditure line covers IFRS 16 right-of-use lease costs across the trust's estate — operational lease components on community-clinic outposts, modular ward decant facilities, equipment leases and short-term tenancies linked to the West Suffolk Hospital (Bury St Edmunds) RAAC-driven decant programme. WSFT is one of the 27 RAAC-listed trusts (HSSIB Sep 2023) and a New Hospital Programme cohort trust — the post-Reset January 2025 deferral shapes the 2025-30 lease trajectory as decant facilities continue.",
        "beneficiaries": "c. 4,500 WTE staff serving a c. 280,000 west Suffolk catchment (Bury St Edmunds, Haverhill, Sudbury, Newmarket, Mildenhall); c. 75,000 ED attendances/yr at West Suffolk Hospital ED; c. 50,000 admissions/yr; trust runs West Suffolk Hospital plus Newmarket Community Hospital and a network of community outposts within the Suffolk and North East Essex ICS.",
        "legal_basis": "IFRS 16 Leases — DHSC Group Accounting Manual 2024-25 chapter 7 — Landlord and Tenant Act 1954 — NHS Property Services lease-plus framework — NHS Act 2006 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Lease expenditure 2024-25", "value": "£1.722M"},
            {"label": "Trust scale", "value": "West Suffolk Hospital (Bury St Edmunds) + Newmarket Community Hospital + community outposts; c. 4,500 WTE"},
            {"label": "RAAC status", "value": "On HSSIB Sep 2023 RAAC list — 27 trusts; West Suffolk Hospital has significant RAAC plank presence"},
            {"label": "NHP cohort", "value": "New Hospital Programme cohort (8 RAAC trusts prioritised) — Jan 2025 NHP Reset confirmed RAAC trusts retain prioritisation; full new build construction planning continues"},
            {"label": "IFRS 16 transition", "value": "1 April 2022 transition under DHSC GAM brought operating leases onto balance sheet; decant-facility tenancies driven by RAAC remediation feed forward"},
            {"label": "Composition", "value": "Modular ward decant facility leases + community-clinic operating leases + equipment short leases + short-term tenancy on temporary clinical space"},
            {"label": "Decant programme", "value": "RAAC remediation + ward closures driving need for modular decant + short-term equipment leases — drives 2024-25 line vs pre-RAAC baseline"},
            {"label": "Funding trajectory", "value": "2021-22 c. £1.0M → 2023-24 c. £1.6M → 2024-25 £1.722M — RAAC-decant demand step-up + IFRS 16 reclassification + indexation"},
            {"label": "Delivery body", "value": "Trust E&F + lessor counterparties (NHSPS + Community Health Partnerships + private modular suppliers + equipment leasing partners) + Trust Finance"},
            {"label": "Policy owner", "value": "DHSC + NHSE NHP team + NHSE Provider Finance + Suffolk and North East Essex ICB + HSSIB (RAAC technical lead)"},
            {"label": "Evaluation evidence", "value": "HSSIB RAAC report Sep 2023; NAO New Hospital Programme 2023; Trust ARA 2023-24 + IFRS 16 disclosure note; CQC RGR inspections"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-IFRS-16 + pre-RAAC operating-lease baseline · Successor: post-NHP-rebuild estate consolidation + decant lease run-off"}
        ],
        "notes": "WSFT's lease-expenditure line is dominated by RAAC-driven decant facility demand — West Suffolk Hospital (Bury St Edmunds) is one of the 27 trusts listed by HSSIB in September 2023 with significant RAAC plank presence in the original 1970s build, and full ward closures or downtime have driven additional modular decant-facility leases on top of normal community-clinic operating leases. WSFT sits in the NHP cohort with the January 2025 NHP Reset retaining prioritisation for the 8 RAAC trusts (publication May 2025). IFRS 16 transition (1 April 2022) brought operating leases onto the balance sheet under DHSC GAM ch.7. Indexation on long leases plus equipment-lease cycle interaction with EPR rollout shape year-on-year movement. Trust governance was reshaped following the 'Sting' anonymous-letter scandal (2018-2019) that drew national attention.",
        "sources": [
            {"publisher": "West Suffolk NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.wsh.nhs.uk/About-us/Annual-Report.aspx"},
            {"publisher": "Health Services Safety Investigations Body", "title": "RAAC investigation report (September 2023)", "url": "https://www.hssib.org.uk/"},
            {"publisher": "National Audit Office", "title": "New Hospital Programme", "url": "https://www.nao.org.uk/reports/new-hospital-programme/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 7 — Leases and service concessions)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "West Suffolk NHS Foundation Trust provider profile (RGR)", "url": "https://www.cqc.org.uk/provider/RGR"}
        ],
        "related": ["West Suffolk NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Lease expenditure — The Newcastle Upon Tyne Hospitals NHS Foundation Trust", "New Hospital Programme", "Department of Health and Social Care"]
    },
    "Establishment costs — Barnsley Hospital NHS Foundation Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "Barnsley Hospital NHS Foundation Trust"}],
        "description": "Barnsley Hospital NHS FT's £1.720M establishment-costs line covers GAM operating expenses outside the Establishment-payroll chain — chiefly office consumables, postage, telephony, training and conferences, recruitment advertising, subscriptions, books and publications, courier services and minor furniture / equipment below capitalisation threshold across Barnsley Hospital (Gawber Road, Barnsley) and the trust's community footprint. Backfill agency administrative cost from the 2023-24 industrial-action cycle plus EPR change-management training feeds the line.",
        "beneficiaries": "c. 3,500 WTE staff serving a c. 245,000 Barnsley borough catchment; c. 95,000 ED attendances/yr at Barnsley Hospital ED; c. 60,000 admissions/yr; trust runs Barnsley Hospital plus a network of Barnsley community outposts within the South Yorkshire ICS.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 — IAS 1 Presentation of Financial Statements — IAS 16 Property Plant and Equipment (capitalisation threshold) — NHS Act 2006 — Health and Care Act 2022 — HMRC training and subsistence rules",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£1.720M"},
            {"label": "Trust scale", "value": "Barnsley Hospital (Gawber Road) + Barnsley community outposts; c. 3,500 WTE"},
            {"label": "Composition", "value": "Office consumables + postage + telephony + training & conferences + recruitment advertising + subscriptions + books/publications + minor furniture/equipment below cap threshold"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove cancellation rebooking + admin backfill + recruitment advertising spike"},
            {"label": "Frontline Digitisation EPR", "value": "EPR change-management training, conference and travel costs feed forward into Establishment line"},
            {"label": "April 2025 NIC step-up", "value": "Indirect via training-provider and recruitment-advertising contractor pass-through"},
            {"label": "Funding trajectory", "value": "2021-22 c. £1.4M → 2023-24 c. £1.6M → 2024-25 £1.720M — strike backfill + EPR training + CPI on consumables"},
            {"label": "South Yorkshire ICS", "value": "Member of South Yorkshire ICB (alongside STH, Doncaster & Bassetlaw, Rotherham); collaborative procurement and recruitment frameworks"},
            {"label": "Delivery body", "value": "Trust Workforce + Procurement + Training & Development + IT + Communications + Finance"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + South Yorkshire ICB + DHSC + NHS Supply Chain (where used)"},
            {"label": "Evaluation evidence", "value": "Carter Lord review legacy on running costs; Model Hospital establishment-cost benchmark; Trust ARA 2023-24; CQC RFF inspections"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-EPR baseline establishment-cost profile · Successor: post-EPR-stabilisation training-cost normalisation + SY-ICS shared-service consolidation"}
        ],
        "notes": "Barnsley Hospital NHS FT's establishment-cost line is shaped by the convergence of three drivers — 2023-24 industrial-action backfill (44 days junior-doctor + 10 days consultant strikes drove admin rebooking, recruitment advertising and casual training spend), Frontline Digitisation EPR change-management training cycles, and HMRC subsistence and training-provider CPI uplifts. Barnsley Hospital sits within the South Yorkshire ICS alongside Sheffield Teaching Hospitals, Doncaster & Bassetlaw and Rotherham, with collaborative procurement and recruitment frameworks shared across the four trusts. Barnsley borough is a high-deprivation former-coalfield population with significant unmet need shaping the trust's recruitment advertising profile. April 2025 employer NIC step-up feeds indirectly via training-provider and recruitment-advertising contractor pass-through.",
        "sources": [
            {"publisher": "Barnsley Hospital NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.barnsleyhospital.nhs.uk/about-us/publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/frontline-digitisation/"},
            {"publisher": "Care Quality Commission", "title": "Barnsley Hospital NHS Foundation Trust provider profile (RFF)", "url": "https://www.cqc.org.uk/provider/RFF"},
            {"publisher": "NHS Confederation", "title": "South Yorkshire Integrated Care System", "url": "https://www.nhsconfed.org/system/integrated-care-systems"}
        ],
        "related": ["Barnsley Hospital NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Establishment costs — Stockport NHS Foundation Trust", "Amortisation — Sheffield Teaching Hospitals NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Business rates — Gateshead Health NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "Gateshead Health NHS Foundation Trust"}],
        "description": "Gateshead Health NHS FT's £1.704M business-rates line covers non-domestic rate liability across the trust's Gateshead footprint — principally the Queen Elizabeth Hospital (Sheriff Hill, Gateshead) plus Bensham Hospital, Blaydon Primary Care Centre and a network of community outposts. Rateable values are set by the VOA on the 2023 list with rates calculated against the LGFA 1988 (Sch 6) multiplier as amended by the NDR (Multipliers and Private Finance) Act 2024. North East and North Cumbria ICS context.",
        "beneficiaries": "c. 4,500 WTE staff serving a c. 200,000 Gateshead borough catchment plus tertiary referrals from across the North East; c. 75,000 ED attendances/yr at QE Hospital ED; c. 55,000 admissions/yr; trust runs Queen Elizabeth Hospital + Bensham Hospital + community outposts within the North East and North Cumbria ICS.",
        "legal_basis": "Local Government Finance Act 1988 (Sch 6) — Non-Domestic Rating (Multipliers and Private Finance) Act 2024 — Valuation Office Agency 2023 rating list — DHSC Group Accounting Manual 2024-25 — NHS Act 2006 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£1.703592M"},
            {"label": "Trust scale", "value": "Queen Elizabeth Hospital (Sheriff Hill, Gateshead) + Bensham Hospital + Blaydon Primary Care Centre + community outposts; c. 4,500 WTE"},
            {"label": "Principal hereditament", "value": "Queen Elizabeth Hospital Gateshead — main acute site, designated Trauma Unit feeding Royal Victoria Infirmary MTC"},
            {"label": "Rating list", "value": "VOA 2023 list (effective 1 April 2023); next revaluation 1 April 2026"},
            {"label": "Multiplier", "value": "Standard non-domestic multiplier per LGFA 1988 Sch 6 + NDR (Multipliers and Private Finance) Act 2024 higher tier on £500k+ from April 2025"},
            {"label": "Charitable relief", "value": "NHS trusts not eligible for mandatory 80% charitable relief — full liability borne"},
            {"label": "Funding trajectory", "value": "2021-22 c. £1.5M → 2023-24 c. £1.65M → 2024-25 £1.704M — 2023 list revaluation + multiplier uplift"},
            {"label": "NENC ICS", "value": "Member of North East and North Cumnria ICB; collaborative estate-rationalisation across NE acute trusts"},
            {"label": "Delivery body", "value": "Trust E&F + Finance + VOA + Gateshead Council (unitary billing authority)"},
            {"label": "Policy owner", "value": "MHCLG (rates policy + multiplier) + VOA (valuations) + DHSC + NHSE Provider Finance + North East and North Cumbria ICB"},
            {"label": "Evaluation evidence", "value": "VOA rating-list publications; CQC RR7 inspections; Trust ARA 2023-24 disclosure; Model Hospital estate benchmark"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2017 VOA rating list · Successor: 2026 VOA revaluation + NENC-ICS estate-rationalisation"}
        ],
        "notes": "Gateshead Health NHS FT's business-rates line is a function of the VOA 2023 rating-list valuations on the Queen Elizabeth Hospital Gateshead — the trust's principal hereditament — with smaller liabilities on Bensham Hospital, Blaydon Primary Care Centre and community outposts. NHS trusts are not eligible for the mandatory 80% charitable rate relief enjoyed by independent-sector charity hospitals, so the full liability is borne by the trust. The NDR (Multipliers and Private Finance) Act 2024 introduced the higher multiplier on £500k+ properties from April 2025 — material for the QE Hospital main hereditament. Gateshead Council (unitary billing authority) collects the rates. The 1 April 2026 next revaluation is the medium-term lever for the trust to challenge valuations.",
        "sources": [
            {"publisher": "Gateshead Health NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.qegateshead.nhs.uk/about-us/publications/"},
            {"publisher": "Valuation Office Agency", "title": "Find a business rates valuation (rating list)", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "Department for Levelling Up, Housing and Communities", "title": "Business rates: Non-Domestic Rating Act 2023 + 2024 Multipliers Act", "url": "https://www.gov.uk/government/collections/business-rates"},
            {"publisher": "Care Quality Commission", "title": "Gateshead Health NHS Foundation Trust provider profile (RR7)", "url": "https://www.cqc.org.uk/provider/RR7"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"}
        ],
        "related": ["Gateshead Health NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Business rates — Northampton General Hospital NHS Trust", "Transport (business + patient) — Gateshead Health NHS Foundation Trust", "Valuation Office Agency"]
    },
    "PFI / LIFT charges — Stockport NHS Foundation Trust": {
        "aliases": [{"name": "PFI / LIFT charges", "parent": "Stockport NHS Foundation Trust"}],
        "description": "Stockport NHS FT's £1.699M PFI / LIFT charges line covers unitary-charge pass-through on a smaller LIFT-vehicle community / outpatient extension concession within the Stockport estate (Stepping Hill Hospital + Stockport community). The bulk of the trust's main acute estate at Stepping Hill is publicly owned — the £1.699M figure reflects the residual LIFT-vehicle community-clinic / outpatient-extension element rather than a major hospital PFI. RPI-indexed soft-FM components and lifecycle hard-FM cycles drive year-on-year movement.",
        "beneficiaries": "c. 5,200 WTE staff serving a c. 320,000 Stockport + south-east Greater Manchester catchment; c. 95,000 ED attendances/yr at Stepping Hill ED; c. 70,000 admissions/yr; LIFT estate covers community/outpatient extension premises supporting the wider Stepping Hill acute footprint within the Greater Manchester ICS.",
        "legal_basis": "IFRIC 12 Service Concession Arrangements — IFRS 16 Leases (post-2022 transition for service-concession components) — DHSC Group Accounting Manual 2024-25 ch.7 — Private Finance Initiative / NHS LIFT guidance (HM Treasury) — NHS Act 2006 — Health and Care Act 2022",
        "key_stats": [
            {"label": "PFI / LIFT charges 2024-25", "value": "£1.699M"},
            {"label": "Trust scale", "value": "Stepping Hill Hospital + Stockport community LIFT footprint; c. 5,200 WTE"},
            {"label": "LIFT vehicle", "value": "Manchester / Stockport LIFT-style community-clinic concession — far smaller than the trust's mainstream publicly-owned Stepping Hill acute estate"},
            {"label": "Estate covered", "value": "LIFT-vehicle community / outpatient extension premises (modest hereditament base relative to trust-wide opex)"},
            {"label": "Unitary charge composition", "value": "Senior debt service + lifecycle hard-FM + indexed soft-FM (cleaning, security, minor maintenance)"},
            {"label": "Indexation mechanism", "value": "RPI-linked annual uplift on indexed components per LIFT lease-plus agreement"},
            {"label": "Funding trajectory", "value": "2021-22 c. £1.45M → 2023-24 c. £1.6M → 2024-25 £1.699M — RPI-linked uplift on indexed soft-FM components"},
            {"label": "Greater Manchester ICS", "value": "Member of Greater Manchester ICB; ICS-wide LIFT estate-stewardship via Manchester LIFT-Co + Community Health Partnerships"},
            {"label": "Delivery body", "value": "LIFT Co (SPV) + LIFT FM contractor + trust E&F oversight + Community Health Partnerships (HMG holding co for LIFT)"},
            {"label": "Policy owner", "value": "DHSC + HM Treasury PFI/LIFT guidance + NHSE Provider Finance + Greater Manchester ICB"},
            {"label": "Evaluation evidence", "value": "NAO PFI 2018 + PFI hand-back report 2020; PAC PFI hearings; Trust ARA disclosure; CQC RWJ inspections"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-LIFT community estate baseline · Successor: LIFT hand-back + GM-ICS estate-rationalisation"}
        ],
        "notes": "Stockport NHS FT's PFI / LIFT line reflects a residual LIFT (Local Improvement Finance Trust) community-clinic / outpatient-extension concession indexed to RPI on soft-FM components rather than a major hospital PFI — the trust's mainstream Stepping Hill Hospital acute estate is publicly owned. RPI-linked uplifts on indexed soft-FM components drive cost growth and lifecycle hard-FM cycles produce year-on-year volatility. Community Health Partnerships (HMG holding co) governs LIFT-Co stewardship; Manchester LIFT-Co operates the SPV. The Greater Manchester ICS estate-rationalisation programme is the medium-term lever for re-baselining LIFT use across the conurbation. Stepping Hill Hospital itself has a long history of high-deprivation patient profile (Beverley-Allitt-style nurse-poisoning investigation 2011-15) shaping its broader institutional context.",
        "sources": [
            {"publisher": "Stockport NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.stockport.nhs.uk/about-us/publications/"},
            {"publisher": "National Audit Office", "title": "PFI and PF2 (HC 718, 2018)", "url": "https://www.nao.org.uk/reports/pfi-and-pf2/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 7 — Leases and service concessions)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Community Health Partnerships", "title": "About LIFT — NHS Local Improvement Finance Trust", "url": "https://www.communityhealthpartnerships.co.uk/"},
            {"publisher": "Care Quality Commission", "title": "Stockport NHS Foundation Trust provider profile (RWJ)", "url": "https://www.cqc.org.uk/provider/RWJ"}
        ],
        "related": ["Stockport NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Establishment costs — Stockport NHS Foundation Trust", "PFI / LIFT charges — Worcestershire Acute Hospitals NHS Trust", "Department of Health and Social Care"]
    },
    "Business rates — Northampton General Hospital NHS Trust": {
        "aliases": [{"name": "Business rates", "parent": "Northampton General Hospital NHS Trust"}],
        "description": "NGH's £1.690M business-rates line covers non-domestic rate liability across the trust's Northampton footprint — principally the Northampton General Hospital (Cliftonville, Northampton) plus a small number of Northamptonshire community outposts. NGH operates within the University Hospitals of Northamptonshire group with Kettering General Hospital (separate trust, separate accounts). Rateable values are set by the VOA on the 2023 list with rates calculated against the LGFA 1988 (Sch 6) multiplier as amended by the NDR (Multipliers and Private Finance) Act 2024.",
        "beneficiaries": "c. 5,500 WTE staff serving a c. 380,000 Northampton + south Northamptonshire catchment plus tertiary referrals; c. 105,000 ED attendances/yr at Northampton General ED; c. 75,000 admissions/yr; trust runs Northampton General Hospital plus small community-outpost network within the Northamptonshire ICS.",
        "legal_basis": "Local Government Finance Act 1988 (Sch 6) — Non-Domestic Rating (Multipliers and Private Finance) Act 2024 — Valuation Office Agency 2023 rating list — DHSC Group Accounting Manual 2024-25 — NHS Act 2006 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£1.690225M"},
            {"label": "Trust scale", "value": "Northampton General Hospital (Cliftonville) + Northamptonshire community outposts; c. 5,500 WTE"},
            {"label": "Principal hereditament", "value": "Northampton General Hospital — main acute site, Trauma Unit feeding University Hospitals of Coventry & Warwickshire MTC"},
            {"label": "University Hospitals of Northamptonshire", "value": "Group model with Kettering General Hospital NHS FT (separate legal entities, shared executive arrangements 2021-)"},
            {"label": "Rating list", "value": "VOA 2023 list (effective 1 April 2023); next revaluation 1 April 2026"},
            {"label": "Multiplier", "value": "Standard non-domestic multiplier per LGFA 1988 Sch 6 + NDR (Multipliers and Private Finance) Act 2024 higher tier on £500k+ from April 2025"},
            {"label": "Charitable relief", "value": "NHS trusts not eligible for mandatory 80% charitable relief — full liability borne"},
            {"label": "Funding trajectory", "value": "2021-22 c. £1.5M → 2023-24 c. £1.65M → 2024-25 £1.690M — 2023 list revaluation + multiplier uplift"},
            {"label": "Northamptonshire ICS", "value": "Member of Northamptonshire ICB; collaborative estate-rationalisation across NGH + KGH + community/MH trusts"},
            {"label": "Delivery body", "value": "Trust E&F + Finance + VOA + West Northamptonshire Council (unitary billing authority since 2021)"},
            {"label": "Policy owner", "value": "MHCLG (rates policy + multiplier) + VOA (valuations) + DHSC + NHSE Provider Finance + Northamptonshire ICB"},
            {"label": "Evaluation evidence", "value": "VOA rating-list publications; CQC RNS inspections; Trust ARA 2023-24 disclosure; Model Hospital estate benchmark"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2017 VOA rating list · Successor: 2026 VOA revaluation + UHN group estate-rationalisation"}
        ],
        "notes": "NGH's business-rates line is a function of the VOA 2023 rating-list valuation on Northampton General Hospital — the trust's principal hereditament — with smaller liabilities on community outposts. NGH operates within the University Hospitals of Northamptonshire group model (with Kettering General Hospital, separate legal entities and accounts since 2021) which shapes shared estate-rationalisation strategy. NHS trusts are not eligible for the mandatory 80% charitable rate relief, so the full liability is borne by the trust. The April 2025 NDR (Multipliers and Private Finance) Act 2024 higher-tier multiplier on £500k+ hereditaments is material for the NGH main site. West Northamptonshire Council (formed 2021 from former Northampton BC + South Northants + Daventry) is the unitary billing authority.",
        "sources": [
            {"publisher": "Northampton General Hospital NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.northamptongeneral.nhs.uk/About/Performance-and-publications/"},
            {"publisher": "Valuation Office Agency", "title": "Find a business rates valuation (rating list)", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "Department for Levelling Up, Housing and Communities", "title": "Business rates: Non-Domestic Rating Act 2023 + 2024 Multipliers Act", "url": "https://www.gov.uk/government/collections/business-rates"},
            {"publisher": "Care Quality Commission", "title": "Northampton General Hospital NHS Trust provider profile (RNS)", "url": "https://www.cqc.org.uk/provider/RNS"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"}
        ],
        "related": ["Northampton General Hospital NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Business rates — Gateshead Health NHS Foundation Trust", "Business rates — The Dudley Group NHS Foundation Trust", "Valuation Office Agency"]
    },
    "Amortisation — The Dudley Group NHS Foundation Trust": {
        "aliases": [{"name": "Amortisation", "parent": "The Dudley Group NHS Foundation Trust"}],
        "description": "The Dudley Group's £1.686M amortisation line covers the IAS 38 systematic write-down of intangible assets — chiefly capitalised software licences for the trust's electronic patient record (EPR), PACS imaging system, e-prescribing, theatre management and pathology LIMS — across Russells Hall Hospital (Dudley) and the trust's community footprint. The Frontline Digitisation programme drives EPR build / migration phases; capitalised intangible assets feed the amortisation line over a typical 5-7 year useful life.",
        "beneficiaries": "c. 5,500 WTE staff serving a c. 460,000 Dudley + Tipton catchment; c. 130,000 ED attendances/yr at Russells Hall ED; c. 80,000 admissions/yr; trust runs Russells Hall Hospital + Corbett Hospital + Guest Hospital + Dudley community services within the Black Country ICS.",
        "legal_basis": "IAS 38 Intangible Assets — DHSC Group Accounting Manual 2024-25 chapter 5 — IAS 36 Impairment of Assets (interaction) — NHS Act 2006 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£1.686M"},
            {"label": "Trust scale", "value": "Russells Hall Hospital (Dudley) + Corbett + Guest + Dudley community services; c. 5,500 WTE"},
            {"label": "Composition", "value": "Capitalised software licences (EPR + PACS + e-prescribing + theatre + LIMS) + capitalised in-house development + capitalised implementation costs (IFRIC interpretations on SaaS configuration)"},
            {"label": "Useful life convention", "value": "Typically 5-7 years for clinical software licences; aligned to NHS GAM useful-life table"},
            {"label": "Frontline Digitisation EPR", "value": "EPR build/migration phases drive intangible-asset additions which feed amortisation over 5-7 years; cycle peaks 2024-26 for cohort trusts"},
            {"label": "PFI context", "value": "Russells Hall Hospital is a fully PFI-financed acute (Summit Healthcare SPV; opened 2005; expiry c. 2046) — PFI accounting interacts with amortisation via service-concession asset treatment"},
            {"label": "Funding trajectory", "value": "2021-22 c. £1.4M → 2023-24 c. £1.55M → 2024-25 £1.686M — Frontline Digitisation EPR amort cycle"},
            {"label": "Black Country ICS", "value": "Member of Black Country ICB (with SWBH + Walsall + Sandwell)"},
            {"label": "Delivery body", "value": "Trust IT + Finance + EPR vendor (e.g. SystemC / Cerner / Oracle Health / Epic) + NHSE Frontline Digitisation team"},
            {"label": "Policy owner", "value": "NHSE Frontline Digitisation + DHSC + NHSE Provider Finance + NHS England Digital + Black Country ICB"},
            {"label": "Evaluation evidence", "value": "NHSE Frontline Digitisation programme reviews; NAO Digital transformation in the NHS; Trust ARA 2023-24 + intangibles note; CQC RNA inspections"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-EPR baseline software amort · Successor: post-EPR-stabilisation steady-state amort + next-cycle reinvestment"}
        ],
        "notes": "The Dudley Group's amortisation line is shaped by the trust's intangible-asset portfolio — capitalised software licences for EPR, PACS, e-prescribing and ancillary clinical systems amortised over 5-7 years per DHSC GAM ch.5 useful-life convention. The Frontline Digitisation programme drives intangible-asset additions for cohort trusts with EPR build/migration phases; cycle peaks 2024-26. Russells Hall Hospital is a fully PFI-financed acute (Summit Healthcare SPV; opened 2005; expiry c. 2046) so PFI service-concession accounting interacts with amortisation via the underlying right-of-use / service-concession asset treatment. The Black Country ICS context (with SWBH MMUH new build, Walsall and Sandwell) shapes shared digital-transformation strategy.",
        "sources": [
            {"publisher": "The Dudley Group NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://dgft.nhs.uk/about-us/publications/"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/frontline-digitisation/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 5 — Property, plant and equipment + intangible assets)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "National Audit Office", "title": "Digital transformation in the NHS", "url": "https://www.nao.org.uk/reports/the-digital-transformation-in-the-nhs/"},
            {"publisher": "Care Quality Commission", "title": "The Dudley Group NHS Foundation Trust provider profile (RNA)", "url": "https://www.cqc.org.uk/provider/RNA"}
        ],
        "related": ["The Dudley Group NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Amortisation — Worcestershire Acute Hospitals NHS Trust", "Business rates — The Dudley Group NHS Foundation Trust", "NHS England"]
    },
    "Amortisation — Worcestershire Acute Hospitals NHS Trust": {
        "aliases": [{"name": "Amortisation", "parent": "Worcestershire Acute Hospitals NHS Trust"}],
        "description": "Worcestershire Acute Hospitals' £1.674M amortisation line covers the IAS 38 systematic write-down of intangible assets — chiefly capitalised software licences for the trust's EPR, PACS imaging, e-prescribing, theatre management and pathology LIMS — across the Worcestershire Royal Hospital (Worcester), Alexandra Hospital (Redditch) and Kidderminster Treatment Centre. The Frontline Digitisation programme drives EPR build / migration phases; the trust's PFI acute estate (Worcestershire Royal) interacts with amortisation via service-concession asset treatment.",
        "beneficiaries": "c. 7,000 WTE staff serving a c. 600,000 Worcestershire catchment (Worcester, Redditch, Bromsgrove, Kidderminster, Malvern, Evesham); c. 175,000 ED attendances/yr across Worcestershire Royal ED + Alexandra ED; c. 100,000 admissions/yr; trust within the Herefordshire and Worcestershire ICS.",
        "legal_basis": "IAS 38 Intangible Assets — DHSC Group Accounting Manual 2024-25 chapter 5 — IAS 36 Impairment of Assets (interaction) — IFRIC 12 Service Concession Arrangements (PFI interaction) — NHS Act 2006 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£1.674M"},
            {"label": "Trust scale", "value": "Worcestershire Royal Hospital (Worcester, PFI) + Alexandra Hospital (Redditch) + Kidderminster Treatment Centre; c. 7,000 WTE"},
            {"label": "PFI context", "value": "Worcestershire Royal Hospital is a fully PFI-financed acute (Catalyst Healthcare SPV; opened 2002; FM via Sodexo / Engie post-Carillion novation 2018) — PFI service-concession accounting interacts with amortisation"},
            {"label": "Composition", "value": "Capitalised software licences (EPR + PACS + e-prescribing + theatre + LIMS) + capitalised in-house development + capitalised implementation costs"},
            {"label": "Useful life convention", "value": "Typically 5-7 years for clinical software licences; aligned to NHS GAM useful-life table"},
            {"label": "Frontline Digitisation EPR", "value": "EPR build/migration phases drive intangible-asset additions which feed amortisation over 5-7 years"},
            {"label": "Service-reconfiguration history", "value": "Long-running A&E + maternity + paediatrics reconfiguration disputes 2014-2018; Kidderminster Hospital downgrade 2000 backdrop"},
            {"label": "Funding trajectory", "value": "2021-22 c. £1.35M → 2023-24 c. £1.55M → 2024-25 £1.674M — Frontline Digitisation EPR amort cycle"},
            {"label": "Delivery body", "value": "Trust IT + Finance + EPR vendor (e.g. SystemC / Cerner / Oracle Health / Epic) + NHSE Frontline Digitisation team"},
            {"label": "Policy owner", "value": "NHSE Frontline Digitisation + DHSC + NHSE Provider Finance + NHS England Digital + Herefordshire and Worcestershire ICB"},
            {"label": "Evaluation evidence", "value": "NHSE Frontline Digitisation programme reviews; NAO Digital transformation in the NHS; Trust ARA 2023-24 + intangibles note; CQC RWP inspections"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-EPR baseline software amort · Successor: post-EPR-stabilisation steady-state amort + next-cycle reinvestment"}
        ],
        "notes": "Worcestershire Acute Hospitals' amortisation line reflects the trust's intangible-asset portfolio (capitalised software licences amortised over 5-7 years per DHSC GAM ch.5) on top of the underlying Worcestershire Royal Hospital PFI service-concession accounting (Catalyst Healthcare SPV; opened 2002; FM via Sodexo / Engie post-Carillion 2018 novation). The Frontline Digitisation programme drives intangible-asset additions for cohort trusts with EPR build/migration phases. The trust has a long-running history of A&E and maternity service-reconfiguration disputes (2014-2018) and the Kidderminster Hospital downgrade (2000) backdrop shaping its broader institutional context. Herefordshire and Worcestershire ICS context shapes shared digital-transformation and estate strategy.",
        "sources": [
            {"publisher": "Worcestershire Acute Hospitals NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.worcsacute.nhs.uk/about-us/publications/"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/frontline-digitisation/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 5 — Property, plant and equipment + intangible assets)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "National Audit Office", "title": "Digital transformation in the NHS", "url": "https://www.nao.org.uk/reports/the-digital-transformation-in-the-nhs/"},
            {"publisher": "Care Quality Commission", "title": "Worcestershire Acute Hospitals NHS Trust provider profile (RWP)", "url": "https://www.cqc.org.uk/provider/RWP"}
        ],
        "related": ["Worcestershire Acute Hospitals NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Amortisation — The Dudley Group NHS Foundation Trust", "Transport (business + patient) — Worcestershire Acute Hospitals NHS Trust", "NHS England"]
    },
    "Amortisation — East Kent Hospitals University NHS Foundation Trust": {
        "aliases": [{"name": "Amortisation", "parent": "East Kent Hospitals University NHS Foundation Trust"}],
        "description": "EKHUFT's £1.673M amortisation line covers the IAS 38 systematic write-down of intangible assets — chiefly capitalised software licences for the trust's EPR, PACS imaging, e-prescribing, theatre management, maternity (BadgerNet) and pathology LIMS — across the William Harvey Hospital (Ashford), Queen Elizabeth The Queen Mother Hospital (Margate), Kent and Canterbury Hospital, Royal Victoria Hospital (Folkestone) and the trust's community footprint. Frontline Digitisation EPR drives capitalised intangible additions feeding amortisation over 5-7 year useful life.",
        "beneficiaries": "c. 8,500 WTE staff serving a c. 760,000 east Kent catchment (Ashford, Canterbury, Dover, Folkestone, Hythe, Margate, Ramsgate, Sandwich, Thanet); c. 200,000 ED attendances/yr across William Harvey ED + QEQM ED; c. 130,000 admissions/yr; trust within the Kent and Medway ICS.",
        "legal_basis": "IAS 38 Intangible Assets — DHSC Group Accounting Manual 2024-25 chapter 5 — IAS 36 Impairment of Assets (interaction) — NHS Act 2006 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£1.673M"},
            {"label": "Trust scale", "value": "William Harvey Hospital (Ashford) + QEQM (Margate) + Kent and Canterbury Hospital + Royal Victoria (Folkestone); c. 8,500 WTE"},
            {"label": "Composition", "value": "Capitalised software licences (EPR + PACS + e-prescribing + theatre + LIMS + BadgerNet maternity) + capitalised in-house development + capitalised implementation costs"},
            {"label": "Useful life convention", "value": "Typically 5-7 years for clinical software licences; aligned to NHS GAM useful-life table"},
            {"label": "Frontline Digitisation EPR", "value": "EPR build/migration phases drive intangible-asset additions which feed amortisation over 5-7 years"},
            {"label": "Maternity context", "value": "Reading the Signals report (Bill Kirkup 2022) on EKHUFT maternity services — additional clinical-systems investment in BadgerNet maternity software"},
            {"label": "Service reconfiguration", "value": "Long-running 'three sites + central' reconfiguration debate (William Harvey, QEQM, Kent and Canterbury) shapes capitalised investment priorities"},
            {"label": "Funding trajectory", "value": "2021-22 c. £1.35M → 2023-24 c. £1.55M → 2024-25 £1.673M — Frontline Digitisation EPR amort cycle"},
            {"label": "Delivery body", "value": "Trust IT + Finance + EPR vendor (e.g. Cerner / SystemC / Oracle Health / Epic) + NHSE Frontline Digitisation team"},
            {"label": "Policy owner", "value": "NHSE Frontline Digitisation + DHSC + NHSE Provider Finance + NHS England Digital + Kent and Medway ICB"},
            {"label": "Evaluation evidence", "value": "NHSE Frontline Digitisation programme reviews; NAO Digital transformation in the NHS; Reading the Signals (Kirkup 2022); Trust ARA 2023-24; CQC RVV inspections"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-EPR baseline software amort · Successor: post-EPR-stabilisation steady-state amort + next-cycle reinvestment"}
        ],
        "notes": "EKHUFT's amortisation line reflects the trust's intangible-asset portfolio (capitalised software licences amortised over 5-7 years per DHSC GAM ch.5) — chiefly clinical systems (EPR, PACS, e-prescribing, theatre, LIMS) plus BadgerNet maternity software which received additional investment following Bill Kirkup's 'Reading the Signals' report (October 2022) into maternity services at the trust. The Frontline Digitisation programme drives intangible-asset additions for cohort trusts with EPR build/migration phases. The trust's long-running 'three-sites + central' service-reconfiguration debate (William Harvey, QEQM, Kent and Canterbury) shapes capitalised investment priorities. Kent and Medway ICS context shapes shared digital-transformation strategy.",
        "sources": [
            {"publisher": "East Kent Hospitals University NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.ekhuft.nhs.uk/about-us/publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Reading the Signals — Maternity and neonatal services in East Kent (Bill Kirkup 2022)", "url": "https://www.gov.uk/government/publications/maternity-and-neonatal-services-in-east-kent-reading-the-signals-report"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/frontline-digitisation/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 5)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "East Kent Hospitals University NHS Foundation Trust provider profile (RVV)", "url": "https://www.cqc.org.uk/provider/RVV"}
        ],
        "related": ["East Kent Hospitals University NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Amortisation — Worcestershire Acute Hospitals NHS Trust", "Amortisation — Sheffield Teaching Hospitals NHS Foundation Trust", "NHS England"]
    },
    "Transport (business + patient) — Worcestershire Acute Hospitals NHS Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "Worcestershire Acute Hospitals NHS Trust"}],
        "description": "Worcestershire Acute Hospitals' £1.669M transport line covers business mileage (AfC Section 17 + AMAP), pool-fleet IFRS 16 lease costs, NEPTS contract pass-through and patient travel reimbursements across the Worcestershire Royal Hospital (Worcester), Alexandra Hospital (Redditch) and Kidderminster Treatment Centre. Inter-site transfers between Worcester and Redditch (and tertiary referrals to UHB / UHCW) generate distinctive volume. NEPTS is commissioned through the Herefordshire and Worcestershire ICS lead-commissioner.",
        "beneficiaries": "c. 7,000 WTE staff serving a c. 600,000 Worcestershire catchment (Worcester, Redditch, Bromsgrove, Kidderminster, Malvern, Evesham); c. 175,000 ED attendances/yr across Worcestershire Royal ED + Alexandra ED; c. 100,000 admissions/yr; rural / dispersed footprint drives patient-travel reimbursements.",
        "legal_basis": "NHS Act 2006 — NHSE Patient Transport Services Eligibility Criteria 2021 — Agenda for Change Section 17 (business mileage) — HMRC AMAP rates — IFRS 16 Leases (pool fleet) — DHSC Group Accounting Manual 2024-25 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£1.669M"},
            {"label": "Trust scale", "value": "Worcestershire Royal Hospital (Worcester, PFI) + Alexandra Hospital (Redditch) + Kidderminster Treatment Centre; c. 7,000 WTE"},
            {"label": "Inter-site transfers", "value": "Worcester ↔ Redditch ↔ Kidderminster + tertiary referrals to UHB (Birmingham) / UHCW (Coventry) / Russells Hall (Dudley) generate distinctive transport volume"},
            {"label": "NEPTS commissioning", "value": "Herefordshire and Worcestershire ICS lead-commissioner NEPTS contract; eligibility per NHSE 2021 criteria"},
            {"label": "Composition", "value": "Business mileage (AfC S17 + AMAP 45p/25p frozen since 2011) + pool-fleet IFRS 16 leases + NEPTS pass-through + patient travel reimbursements"},
            {"label": "Service-reconfiguration history", "value": "Long-running A&E + maternity + paediatrics reconfiguration disputes 2014-2018; Kidderminster Hospital downgrade 2000 backdrop drives inter-site transfer volume"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove cancellation rebooking + agency travel claims"},
            {"label": "Funding trajectory", "value": "2021-22 c. £1.35M → 2023-24 c. £1.55M → 2024-25 £1.669M — fuel CPI + NEPTS contract uplift + activity recovery"},
            {"label": "Delivery body", "value": "Trust E&F + outsourced NEPTS provider (Herefordshire and Worcestershire ICS lead-commissioner) + pool-fleet leasing partner + Trust HR (mileage)"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + NHSE Urgent and Emergency Care (NEPTS) + Herefordshire and Worcestershire ICB + DHSC"},
            {"label": "Evaluation evidence", "value": "NAO NEPTS 2019; CQC RWP inspections; NHSE NEPTS Eligibility Review 2021; Trust ARA 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-ICS CCG-commissioned NEPTS contracts · Successor: ICS-collaborative NEPTS retender + service-reconfiguration outcome"}
        ],
        "notes": "Worcestershire Acute Hospitals' transport line is shaped by the trust's tri-site footprint (Worcester, Redditch, Kidderminster) — Kidderminster Hospital's 2000 downgrade and the unresolved 2014-2018 reconfiguration dispute over A&E, maternity and paediatrics drive distinctive inter-site transfer volume. Tertiary referrals to UHB Queen Elizabeth (Birmingham), UHCW (Coventry MTC) and Russells Hall (Dudley) generate additional cross-trust patient transport demand. Industrial action 2023-24 drove cancellation-rebooking journeys and agency travel claims; HMRC AMAP-rate freeze at 45p/mile since 2011 sustains internal-rate dispute pressure. Diesel CPI and the April 2025 NIC step-up feed forward via NEPTS contractor pass-through.",
        "sources": [
            {"publisher": "Worcestershire Acute Hospitals NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.worcsacute.nhs.uk/about-us/publications/"},
            {"publisher": "NHS England", "title": "Non-Emergency Patient Transport Services — National Framework + Eligibility Criteria 2021", "url": "https://www.england.nhs.uk/publication/non-emergency-patient-transport-services-nepts/"},
            {"publisher": "National Audit Office", "title": "NHS England's management of the primary care support services contract with Capita", "url": "https://www.nao.org.uk/reports/nhs-englands-management-of-the-primary-care-support-services-contract-with-capita/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Worcestershire Acute Hospitals NHS Trust provider profile (RWP)", "url": "https://www.cqc.org.uk/provider/RWP"}
        ],
        "related": ["Worcestershire Acute Hospitals NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Amortisation — Worcestershire Acute Hospitals NHS Trust", "Transport (business + patient) — Gateshead Health NHS Foundation Trust", "NHS England"]
    },
    "Lease expenditure — The Newcastle Upon Tyne Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Lease expenditure", "parent": "The Newcastle Upon Tyne Hospitals NHS Foundation Trust"}],
        "description": "NUTH's £1.668M lease-expenditure line covers IFRS 16 right-of-use lease costs across the trust's large multi-site estate — operational lease components on Royal Victoria Infirmary outreach clinics, Freeman Hospital satellite footprints, Great North Children's Hospital ancillary tenancies, equipment leases (especially research / clinical-trials equipment) and short-term tenancies. NUTH is a major tertiary trust and host of the Major Trauma Centre, regional cancer centre, Newcastle transplant unit (heart, lung, liver, kidney, pancreas) and Great North Children's Hospital.",
        "beneficiaries": "c. 17,000 WTE staff serving a c. 1.5M Newcastle + Tyne and Wear catchment plus tertiary referrals from across the North East and North Cumbria; c. 250,000 ED attendances/yr at RVI ED (regional Major Trauma Centre); c. 200,000 admissions/yr; trust hosts UK's largest solid-organ transplant programme.",
        "legal_basis": "IFRS 16 Leases — DHSC Group Accounting Manual 2024-25 chapter 7 — Landlord and Tenant Act 1954 — NHS Property Services lease-plus framework — NHS Act 2006 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Lease expenditure 2024-25", "value": "£1.668M"},
            {"label": "Trust scale", "value": "Royal Victoria Infirmary (RVI) + Freeman Hospital + Great North Children's Hospital + Newcastle Dental Hospital + Centre for Ageing & Vitality + community outreach; c. 17,000 WTE"},
            {"label": "Tertiary specialty profile", "value": "Major Trauma Centre + UK's largest solid-organ transplant programme (heart/lung/liver/kidney/pancreas) + regional cancer centre + Great North Children's Hospital + neurosciences"},
            {"label": "IFRS 16 transition", "value": "1 April 2022 transition under DHSC GAM brought operating leases onto balance sheet; small remaining short-term + low-value exemption population recognised in expense line"},
            {"label": "Composition", "value": "Equipment leases (research / clinical trials / specialist diagnostics) + community-clinic operating leases + short-term tenancies + low-value exemption assets"},
            {"label": "Research lease footprint", "value": "Substantial NIHR + research-charity-funded equipment lease portfolio reflecting trust's major academic-research role with Newcastle University"},
            {"label": "Funding trajectory", "value": "2021-22 c. £1.4M → 2023-24 c. £1.55M → 2024-25 £1.668M — IFRS 16 reclassification + research-equipment cycle + indexation"},
            {"label": "NENC ICS", "value": "Member of North East and North Cumbria ICB — region's tertiary anchor"},
            {"label": "Delivery body", "value": "Trust E&F + research equipment leasing partners + lessor counterparties (NHSPS + Community Health Partnerships + private modular suppliers + equipment leasing partners) + Trust Finance"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + North East and North Cumbria ICB + NIHR (research equipment policy)"},
            {"label": "Evaluation evidence", "value": "Trust ARA 2023-24 + IFRS 16 disclosure note; CQC RTD inspections (Outstanding rated); Carter Lord review legacy on running costs; Model Hospital benchmark"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-IFRS-16 operating-lease baseline · Successor: estate-rationalisation + research-equipment refresh cycles"}
        ],
        "notes": "NUTH's lease-expenditure line reflects the trust's large multi-site footprint and major tertiary research role — Royal Victoria Infirmary (Major Trauma Centre), Freeman Hospital (UK's largest solid-organ transplant programme; cardio-thoracic), Great North Children's Hospital, Newcastle Dental Hospital and a network of community outreach clinics. The IFRS 16 transition (1 April 2022) under DHSC GAM ch.7 brought operating leases onto the balance sheet — the £1.668M expense line is the residual short-term + low-value exemption population plus indexed elements. The trust's substantial NIHR and research-charity-funded equipment lease portfolio (reflecting its academic role with Newcastle University) drives a distinct cycle of refresh activity. CQC rates the trust 'Outstanding'.",
        "sources": [
            {"publisher": "The Newcastle Upon Tyne Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.newcastle-hospitals.nhs.uk/about-us/publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 7 — Leases and service concessions)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "The Newcastle Upon Tyne Hospitals NHS Foundation Trust provider profile (RTD)", "url": "https://www.cqc.org.uk/provider/RTD"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme + NIHR Biomedical Research Centre Newcastle", "url": "https://www.england.nhs.uk/digitaltechnology/frontline-digitisation/"},
            {"publisher": "National Institute for Health and Care Research", "title": "Newcastle Biomedical Research Centre", "url": "https://www.nihr.ac.uk/explore-nihr/infrastructure/biomedical-research-centres.htm"}
        ],
        "related": ["The Newcastle Upon Tyne Hospitals NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Lease expenditure — West Suffolk NHS Foundation Trust", "Amortisation — Sheffield Teaching Hospitals NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Business rates — The Dudley Group NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "The Dudley Group NHS Foundation Trust"}],
        "description": "The Dudley Group's £1.666M business-rates line covers non-domestic rate liability on Russells Hall Hospital (Dudley) — the trust's principal acute site (PFI) — plus Corbett Hospital (Stourbridge), Guest Hospital and Dudley community outposts. Russells Hall Hospital is a fully PFI-financed acute (Summit Healthcare SPV; opened 2005) — under PFI accounting the trust holds the rateable interest as occupier. Rateable values per VOA 2023 list with rates calculated against the LGFA 1988 (Sch 6) multiplier as amended by NDR (Multipliers and Private Finance) Act 2024.",
        "beneficiaries": "c. 5,500 WTE staff serving a c. 460,000 Dudley + Tipton catchment; c. 130,000 ED attendances/yr at Russells Hall ED; c. 80,000 admissions/yr; trust runs Russells Hall Hospital + Corbett Hospital + Guest Hospital + Dudley community services within the Black Country ICS.",
        "legal_basis": "Local Government Finance Act 1988 (Sch 6) — Non-Domestic Rating (Multipliers and Private Finance) Act 2024 — Valuation Office Agency 2023 rating list — DHSC Group Accounting Manual 2024-25 — NHS Act 2006 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£1.666M"},
            {"label": "Trust scale", "value": "Russells Hall Hospital (Dudley, PFI) + Corbett Hospital (Stourbridge) + Guest Hospital + community outposts; c. 5,500 WTE"},
            {"label": "Principal hereditament", "value": "Russells Hall Hospital — main acute site (PFI Summit Healthcare SPV opened 2005)"},
            {"label": "PFI rateable interest", "value": "Trust holds the rateable interest as occupier under PFI service-concession arrangement; PFI Co does not bear rates"},
            {"label": "Rating list", "value": "VOA 2023 list (effective 1 April 2023); next revaluation 1 April 2026"},
            {"label": "Multiplier", "value": "Standard non-domestic multiplier per LGFA 1988 Sch 6 + NDR (Multipliers and Private Finance) Act 2024 higher tier on £500k+ from April 2025"},
            {"label": "Charitable relief", "value": "NHS trusts not eligible for mandatory 80% charitable relief — full liability borne"},
            {"label": "Funding trajectory", "value": "2021-22 c. £1.5M → 2023-24 c. £1.6M → 2024-25 £1.666M — 2023 list revaluation + multiplier uplift"},
            {"label": "Black Country ICS", "value": "Member of Black Country ICB (with SWBH + Walsall + Sandwell)"},
            {"label": "Delivery body", "value": "Trust E&F + Finance + VOA + Dudley MBC (unitary billing authority)"},
            {"label": "Policy owner", "value": "MHCLG (rates policy + multiplier) + VOA (valuations) + DHSC + NHSE Provider Finance + Black Country ICB"},
            {"label": "Evaluation evidence", "value": "VOA rating-list publications; CQC RNA inspections; Trust ARA 2023-24 disclosure"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2017 VOA rating list · Successor: 2026 VOA revaluation + Black Country ICS estate-rationalisation"}
        ],
        "notes": "The Dudley Group's business-rates line is dominated by Russells Hall Hospital — the trust's fully PFI-financed acute (Summit Healthcare SPV; opened 2005; expiry c. 2046). Under PFI service-concession accounting the trust holds the rateable interest as occupier and bears the rates liability directly (the PFI SPV does not). Smaller liabilities sit on Corbett Hospital (Stourbridge), Guest Hospital and community outposts. NHS trusts are not eligible for the mandatory 80% charitable relief, so full liability is borne. The April 2025 NDR (Multipliers and Private Finance) Act 2024 higher-tier multiplier on £500k+ hereditaments is material for the Russells Hall main site. Dudley MBC is the unitary billing authority. The 2026 VOA revaluation is the medium-term lever for the trust to challenge valuations.",
        "sources": [
            {"publisher": "The Dudley Group NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://dgft.nhs.uk/about-us/publications/"},
            {"publisher": "Valuation Office Agency", "title": "Find a business rates valuation (rating list)", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "Department for Levelling Up, Housing and Communities", "title": "Business rates: Non-Domestic Rating Act 2023 + 2024 Multipliers Act", "url": "https://www.gov.uk/government/collections/business-rates"},
            {"publisher": "Care Quality Commission", "title": "The Dudley Group NHS Foundation Trust provider profile (RNA)", "url": "https://www.cqc.org.uk/provider/RNA"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"}
        ],
        "related": ["The Dudley Group NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Amortisation — The Dudley Group NHS Foundation Trust", "Business rates — Northampton General Hospital NHS Trust", "Valuation Office Agency"]
    },
    "Amortisation — Sheffield Teaching Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Amortisation", "parent": "Sheffield Teaching Hospitals NHS Foundation Trust"}],
        "description": "Sheffield Teaching Hospitals' £1.651M amortisation line covers the IAS 38 systematic write-down of intangible assets — chiefly capitalised software licences for the trust's EPR, PACS imaging, e-prescribing, theatre management, robotics control systems and pathology LIMS — across the Royal Hallamshire Hospital, Northern General Hospital, Jessop Wing, Charles Clifford Dental Hospital and Weston Park Cancer Centre. STH is one of the largest NHS trusts and a major academic-research centre with NIHR Biomedical Research Centre status.",
        "beneficiaries": "c. 18,500 WTE staff serving a c. 640,000 Sheffield catchment plus tertiary referrals from across South Yorkshire and beyond; c. 200,000 ED attendances/yr at Northern General ED (regional Major Trauma Centre); c. 180,000 admissions/yr; trust hosts NIHR Sheffield BRC + leading academic-research hospital.",
        "legal_basis": "IAS 38 Intangible Assets — DHSC Group Accounting Manual 2024-25 chapter 5 — IAS 36 Impairment of Assets (interaction) — NHS Act 2006 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£1.651M"},
            {"label": "Trust scale", "value": "Royal Hallamshire Hospital + Northern General Hospital + Jessop Wing + Charles Clifford Dental + Weston Park Cancer Centre; c. 18,500 WTE"},
            {"label": "Tertiary specialty profile", "value": "Major Trauma Centre (Northern General) + Weston Park Cancer Centre + spinal injuries unit + neurosciences + NIHR Sheffield BRC academic research"},
            {"label": "Composition", "value": "Capitalised software licences (EPR + PACS + e-prescribing + theatre + LIMS + robotics control systems + research-data platforms) + capitalised in-house development + capitalised implementation costs"},
            {"label": "Useful life convention", "value": "Typically 5-7 years for clinical software licences; aligned to NHS GAM useful-life table"},
            {"label": "Frontline Digitisation EPR", "value": "EPR build/migration phases drive intangible-asset additions which feed amortisation over 5-7 years; STH on Lorenzo (DXC) historically; transition planning"},
            {"label": "Research portfolio", "value": "NIHR Sheffield Biomedical Research Centre; substantial research-data platforms and academic-software intangibles"},
            {"label": "Funding trajectory", "value": "2021-22 c. £1.35M → 2023-24 c. £1.55M → 2024-25 £1.651M — Frontline Digitisation EPR amort cycle + research-platform investment"},
            {"label": "South Yorkshire ICS", "value": "Member of South Yorkshire ICB (with Barnsley + Doncaster & Bassetlaw + Rotherham); academic anchor"},
            {"label": "Delivery body", "value": "Trust IT + Finance + EPR vendor + NHSE Frontline Digitisation team + University of Sheffield (joint research-platform infrastructure)"},
            {"label": "Policy owner", "value": "NHSE Frontline Digitisation + DHSC + NHSE Provider Finance + NHS England Digital + South Yorkshire ICB + NIHR"},
            {"label": "Evaluation evidence", "value": "NHSE Frontline Digitisation programme reviews; NAO Digital transformation in the NHS; Trust ARA 2023-24 + intangibles note; CQC RHQ inspections (Outstanding rated)"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-EPR baseline software amort + Lorenzo (DXC) historic deployment · Successor: post-EPR-stabilisation steady-state amort + next-cycle reinvestment"}
        ],
        "notes": "Sheffield Teaching Hospitals' amortisation line reflects the trust's intangible-asset portfolio across one of the largest and most academically-active NHS trusts — capitalised software licences for clinical systems (EPR, PACS, e-prescribing, theatre, LIMS, robotics control systems) plus a substantial research-data platform footprint reflecting NIHR Sheffield Biomedical Research Centre status and joint infrastructure with University of Sheffield. The trust historically deployed Lorenzo (DXC) as its core EPR; transition planning under Frontline Digitisation drives the medium-term intangible-asset cycle. Useful lives are 5-7 years per DHSC GAM ch.5. CQC rates the trust 'Outstanding'. South Yorkshire ICS context (alongside Barnsley, Doncaster & Bassetlaw, Rotherham) shapes shared digital-transformation strategy.",
        "sources": [
            {"publisher": "Sheffield Teaching Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.sth.nhs.uk/about-us/publications/"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/frontline-digitisation/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 5)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "National Audit Office", "title": "Digital transformation in the NHS", "url": "https://www.nao.org.uk/reports/the-digital-transformation-in-the-nhs/"},
            {"publisher": "Care Quality Commission", "title": "Sheffield Teaching Hospitals NHS Foundation Trust provider profile (RHQ)", "url": "https://www.cqc.org.uk/provider/RHQ"}
        ],
        "related": ["Sheffield Teaching Hospitals NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Amortisation — East Kent Hospitals University NHS Foundation Trust", "Establishment costs — Barnsley Hospital NHS Foundation Trust", "NHS England"]
    },
    "Transport (business + patient) — Gateshead Health NHS Foundation Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "Gateshead Health NHS Foundation Trust"}],
        "description": "Gateshead Health NHS FT's £1.642M transport line covers business mileage (AfC Section 17 + AMAP), pool-fleet IFRS 16 lease costs, NEPTS contract pass-through and patient travel reimbursements across the Queen Elizabeth Hospital (Sheriff Hill, Gateshead), Bensham Hospital, Blaydon Primary Care Centre and a network of community outposts. Inter-trust transfers to the regional Major Trauma Centre at Royal Victoria Infirmary (NUTH) generate distinctive volume. NEPTS is commissioned through the North East and North Cumbria ICS lead-commissioner.",
        "beneficiaries": "c. 4,500 WTE staff serving a c. 200,000 Gateshead borough catchment plus tertiary referrals from across the North East; c. 75,000 ED attendances/yr at QE Hospital ED; c. 55,000 admissions/yr; trust runs Queen Elizabeth Hospital + Bensham Hospital + community outposts within the North East and North Cumbria ICS.",
        "legal_basis": "NHS Act 2006 — NHSE Patient Transport Services Eligibility Criteria 2021 — Agenda for Change Section 17 (business mileage) — HMRC AMAP rates — IFRS 16 Leases (pool fleet) — DHSC Group Accounting Manual 2024-25 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£1.642017M"},
            {"label": "Trust scale", "value": "Queen Elizabeth Hospital (Sheriff Hill, Gateshead) + Bensham Hospital + Blaydon Primary Care Centre + community outposts; c. 4,500 WTE"},
            {"label": "Trauma Unit role", "value": "QE Gateshead is a designated Trauma Unit feeding Royal Victoria Infirmary (NUTH) Major Trauma Centre — drives inter-trust transfer volume"},
            {"label": "NEPTS commissioning", "value": "North East and North Cumbria ICS lead-commissioner NEPTS contract; eligibility per NHSE 2021 criteria"},
            {"label": "Composition", "value": "Business mileage (AfC S17 + AMAP 45p/25p frozen since 2011) + pool-fleet IFRS 16 leases + NEPTS pass-through + patient travel reimbursements"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove cancellation rebooking + agency travel claims"},
            {"label": "April 2025 NIC + fuel CPI", "value": "Indirect via NEPTS contractor pass-through + diesel CPI feed forward unit-cost pressure"},
            {"label": "Funding trajectory", "value": "2021-22 c. £1.3M → 2023-24 c. £1.55M → 2024-25 £1.642M — fuel CPI + NEPTS contract uplift + activity recovery"},
            {"label": "Delivery body", "value": "Trust E&F + outsourced NEPTS provider (NENC ICS lead-commissioner) + pool-fleet leasing partner + Trust HR (mileage)"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + NHSE Urgent and Emergency Care (NEPTS) + North East and North Cumbria ICB + DHSC"},
            {"label": "Evaluation evidence", "value": "NAO NEPTS 2019; CQC RR7 inspections; NHSE NEPTS Eligibility Review 2021; Trust ARA 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-ICS CCG-commissioned NEPTS contracts · Successor: ICS-collaborative NEPTS retender + NENC tertiary-network transfer protocol refresh"}
        ],
        "notes": "Gateshead Health NHS FT's transport line is shaped by the trust's Trauma Unit role feeding the regional Major Trauma Centre at Royal Victoria Infirmary (Newcastle Upon Tyne Hospitals) — inter-trust transfers across the Tyne to NUTH RVI generate distinctive volume on top of routine business mileage between QE Gateshead, Bensham and Blaydon. The North East and North Cumbria ICS lead-commissioner NEPTS contract is the medium-term lever, with NHSE 2021 eligibility criteria tightening the patient-paid threshold. Industrial action 2023-24 drove cancellation-rebooking journeys and agency travel claims; HMRC AMAP-rate freeze at 45p/mile since 2011 sustains internal-rate dispute pressure. Diesel CPI and the April 2025 NIC step-up feed forward via NEPTS contractor pass-through.",
        "sources": [
            {"publisher": "Gateshead Health NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.qegateshead.nhs.uk/about-us/publications/"},
            {"publisher": "NHS England", "title": "Non-Emergency Patient Transport Services — National Framework + Eligibility Criteria 2021", "url": "https://www.england.nhs.uk/publication/non-emergency-patient-transport-services-nepts/"},
            {"publisher": "National Audit Office", "title": "NHS England's management of the primary care support services contract with Capita", "url": "https://www.nao.org.uk/reports/nhs-englands-management-of-the-primary-care-support-services-contract-with-capita/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Gateshead Health NHS Foundation Trust provider profile (RR7)", "url": "https://www.cqc.org.uk/provider/RR7"}
        ],
        "related": ["Gateshead Health NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Business rates — Gateshead Health NHS Foundation Trust", "Transport (business + patient) — Worcestershire Acute Hospitals NHS Trust", "NHS England"]
    },
}
