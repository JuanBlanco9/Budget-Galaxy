# -*- coding: utf-8 -*-
# Phase 2 Acute slice 2 — chunk 30 (17 NHS Acute Trust orphan sub-lines)
# Hand-curated trust-specific PROGRAMME-archetype enrichment entries.
# Structural contract per docs/archetype_briefs.md.

NEW = {
    "Amortisation — Bolton NHS Foundation Trust": {
        "aliases": [{"name": "Amortisation", "parent": "Bolton NHS Foundation Trust"}],
        "description": "Bolton NHS Foundation Trust's £2.003M amortisation line covers IAS 38 intangible-asset amortisation across capitalised software licences, EPR (electronic patient record) implementation costs and SaaS capitalised customisations across the Royal Bolton Hospital site and integrated community services footprint. Bolton operates an integrated acute + community model under Greater Manchester ICS and runs Allscripts Sunrise / Cerner-derived EPR plus capitalised corporate systems, generating a sustained capitalised-intangible amortisation cycle aligned with NHSE Frontline Digitisation funding waves.",
        "beneficiaries": "c. 6,000 WTE staff serving a c. 290,000 Bolton borough catchment plus integrated community services; c. 130,000 ED attendances/yr at Royal Bolton ED; c. 65,000 admissions/yr; integrated acute + community + maternity (Royal Bolton is a tertiary maternity unit for Greater Manchester) footprint.",
        "legal_basis": "IAS 38 Intangible Assets — DHSC Group Accounting Manual 2024-25 ch.5 — NHS Act 2006 — Health and Care Act 2022 — IAS 36 (impairment trigger interaction) — IFRIC SaaS configuration agenda decision 2021",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£2.003M"},
            {"label": "Trust scale", "value": "Royal Bolton Hospital + integrated Bolton community services; c. 6,000 WTE"},
            {"label": "EPR estate", "value": "Allscripts Sunrise / Cerner-derived EPR + capitalised corporate-system licences (HR, ESR feeds, finance ledger)"},
            {"label": "Frontline Digitisation funding", "value": "NHSE FD Programme funded EPR uplift + integration work — capitalised under IAS 38, amortised over useful life (typically 5-10 yrs for software)"},
            {"label": "Composition", "value": "Capitalised software licences + EPR implementation + capitalised SaaS configuration costs (post-IFRIC 2021 clarification) + capitalised website / patient-portal builds"},
            {"label": "Useful-life policy", "value": "Software typically 3-5 yrs; EPR major implementations 5-10 yrs per trust accounting policy disclosed in ARA"},
            {"label": "Integrated care context", "value": "Integrated Acute + Community trust under Greater Manchester ICS — community-IT systems share capitalised-intangible base with acute"},
            {"label": "Maternity tertiary role", "value": "Royal Bolton maternity is a tertiary referral hub for Greater Manchester — Donna Ockenden / Kirkup-era systems work feeds capitalised maternity-IT spend"},
            {"label": "Funding trajectory", "value": "2021-22 c. £1.5M → 2023-24 c. £1.85M → 2024-25 £2.003M — sustained EPR uplift + corporate SaaS capitalisation cycle"},
            {"label": "Delivery body", "value": "Trust Digital + Finance functions + EPR vendor (Allscripts/Altera) + NHSE Frontline Digitisation team + GM ICS Digital"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + NHSE Transformation Directorate (Frontline Digitisation) + DHSC + Greater Manchester ICB"},
            {"label": "Evaluation evidence", "value": "NAO Frontline Digitisation review 2024; Trust ARA 2023-24 intangible-asset note; Model Hospital digital benchmarks; CQC RMC inspections"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-FD-baseline capitalised PAS / corporate licences · Successor: full GM ICS digital convergence + post-FD-stabilisation amortisation tail"}
        ],
        "notes": "Bolton's amortisation profile is shaped by the trust's integrated acute + community + tertiary-maternity model under Greater Manchester ICS — the IAS 38 intangible base aggregates EPR, community-IT and maternity-systems capitalised licences. NHSE Frontline Digitisation funding has driven a sustained capitalised-intangible amortisation cycle, with EPR major-implementation useful lives typically 5-10 yrs producing a long tail. The IFRS Interpretations Committee's 2021 SaaS configuration clarification reshaped what trusts can capitalise vs expense. Greater Manchester ICS digital convergence work is the medium-term lever, alongside the post-2024 NHSE Frontline Digitisation pivot to convergence rather than first-deployment funding. Maternity-system capitalisation following Ockenden-era recommendations adds a distinctive trust-specific layer.",
        "sources": [
            {"publisher": "Bolton NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.boltonft.nhs.uk/about-us/corporate-information/annual-report/"},
            {"publisher": "National Audit Office", "title": "Progress on Frontline Digitisation in the NHS", "url": "https://www.nao.org.uk/reports/digital-transformation-in-the-nhs/"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/connecting-health-and-care/frontline-digitisation/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 5 — Intangible assets)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Bolton NHS Foundation Trust provider profile (RMC)", "url": "https://www.cqc.org.uk/provider/RMC"}
        ],
        "related": ["Bolton NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Frontline Digitisation Programme", "Amortisation — Northern Care Alliance NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Amortisation — York and Scarborough Teaching Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Amortisation", "parent": "York and Scarborough Teaching Hospitals NHS Foundation Trust"}],
        "description": "York and Scarborough Teaching Hospitals' £1.990M amortisation line covers IAS 38 intangible-asset amortisation across capitalised software licences, EPR (Cerner Millennium) implementation costs and SaaS capitalised customisations across the York Hospital, Scarborough Hospital, Bridlington Hospital, Selby War Memorial and Malton Community Hospital footprint. The trust is a Cerner Millennium EPR site and runs a geographically dispersed multi-site footprint covering North Yorkshire's coast and rural inland — driving a multi-year capitalised intangible amortisation cycle.",
        "beneficiaries": "c. 9,000 WTE staff serving a c. 800,000 North Yorkshire and Ryedale catchment plus East Riding coastal flow; c. 175,000 ED attendances/yr (York ED + Scarborough ED); c. 90,000 admissions/yr; geographically dispersed multi-site footprint with rural patient-flow logistics between York city and Scarborough coast.",
        "legal_basis": "IAS 38 Intangible Assets — DHSC Group Accounting Manual 2024-25 ch.5 — NHS Act 2006 — Health and Care Act 2022 — IAS 36 (impairment trigger interaction) — IFRIC SaaS configuration agenda decision 2021",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£1.990M"},
            {"label": "Trust scale", "value": "York Hospital + Scarborough Hospital + Bridlington + Selby + Malton Community Hospital; c. 9,000 WTE"},
            {"label": "EPR estate", "value": "Cerner Millennium EPR (Oracle Health) + capitalised corporate-system licences"},
            {"label": "Frontline Digitisation funding", "value": "NHSE FD Programme funded EPR uplift + integration work — capitalised under IAS 38, amortised over useful life (typically 5-10 yrs for software)"},
            {"label": "Composition", "value": "Capitalised software licences + EPR implementation + capitalised SaaS configuration costs (post-IFRIC 2021 clarification)"},
            {"label": "Scarborough rebuild context", "value": "Scarborough Hospital part of NHP cohort historically — Reset Jan 2025 affected scheme prioritisation, but capitalised digital assets continue independent of capital build"},
            {"label": "Multi-site IT integration", "value": "York + Scarborough merger 2012 (East Coast Hospitals) drove ongoing system convergence + capitalisation tail"},
            {"label": "Useful-life policy", "value": "Software typically 3-5 yrs; EPR major implementations 5-10 yrs per trust accounting policy disclosed in ARA"},
            {"label": "Funding trajectory", "value": "2021-22 c. £1.65M → 2023-24 c. £1.85M → 2024-25 £1.990M — sustained EPR uplift + corporate SaaS capitalisation cycle"},
            {"label": "Delivery body", "value": "Trust Digital + Finance functions + Oracle Health (Cerner) + NHSE Frontline Digitisation team + Humber and North Yorkshire ICS Digital"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + NHSE Transformation Directorate (Frontline Digitisation) + DHSC + Humber and North Yorkshire ICB"},
            {"label": "Evaluation evidence", "value": "NAO Frontline Digitisation review 2024; Trust ARA 2023-24 intangible-asset note; CQC RCB inspections"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-merger separate York + Scarborough digital ledgers · Successor: full HNY ICS digital convergence + post-FD-stabilisation amortisation tail"}
        ],
        "notes": "York and Scarborough's amortisation profile is shaped by the post-2012 East Coast merger, the trust's Cerner Millennium EPR investment and the geographically dispersed footprint requiring sustained system-convergence capitalisation across York city, Scarborough coast and rural community sites. NHSE Frontline Digitisation funding has driven a sustained capitalised-intangible amortisation cycle, with EPR major-implementation useful lives typically 5-10 yrs producing a long tail. The IFRS Interpretations Committee's 2021 SaaS configuration clarification reshaped what trusts can capitalise vs expense. Humber and North Yorkshire ICS digital convergence work is the medium-term lever, alongside the post-2024 NHSE Frontline Digitisation pivot to convergence rather than first-deployment funding. The NHP Reset January 2025 affected Scarborough scheme prioritisation but capitalised digital assets run independent of capital-build deferral.",
        "sources": [
            {"publisher": "York and Scarborough Teaching Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.yorkhospitals.nhs.uk/about-us/publications/annual-reports-and-accounts/"},
            {"publisher": "National Audit Office", "title": "Progress on Frontline Digitisation in the NHS", "url": "https://www.nao.org.uk/reports/digital-transformation-in-the-nhs/"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/connecting-health-and-care/frontline-digitisation/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 5 — Intangible assets)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "York and Scarborough Teaching Hospitals NHS FT provider profile (RCB)", "url": "https://www.cqc.org.uk/provider/RCB"}
        ],
        "related": ["York and Scarborough Teaching Hospitals NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Frontline Digitisation Programme", "Amortisation — Bolton NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Business rates — The Shrewsbury and Telford Hospital NHS Trust": {
        "aliases": [{"name": "Business rates", "parent": "The Shrewsbury and Telford Hospital NHS Trust"}],
        "description": "Shrewsbury and Telford Hospital's £1.988M business-rates line covers non-domestic rates on the Royal Shrewsbury Hospital and Princess Royal Hospital Telford sites plus ancillary outpatient and education premises. The Valuation Office Agency assesses rateable values (2023 list effective 1 April 2023) and Shropshire Council and Telford & Wrekin Council bill respectively. SaTH was the subject of the Donna Ockenden review of maternity services 2022 and is in long-term Recovery Support Programme oversight, with the Future Fit / Hospitals Transformation Programme reshaping the future hereditament footprint.",
        "beneficiaries": "c. 6,500 WTE staff serving a c. 500,000 Shropshire, Telford & Wrekin and Mid Wales catchment; c. 165,000 ED attendances/yr (RSH ED + PRH ED — twin EDs across two sites); c. 90,000 admissions/yr; cross-border English NHS provider serving substantial Powys mid-Wales population.",
        "legal_basis": "Local Government Finance Act 1988 (Schedule 6) — Non-Domestic Rating (Multipliers and Private Finance) Act 2024 — Non-Domestic Rating Act 2023 — DHSC Group Accounting Manual 2024-25 — NHS Act 2006 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£1.988M"},
            {"label": "Trust scale", "value": "Royal Shrewsbury Hospital + Princess Royal Hospital Telford; c. 6,500 WTE"},
            {"label": "Billing authorities", "value": "Shropshire Council (Royal Shrewsbury Hospital) + Telford & Wrekin Council (Princess Royal Hospital)"},
            {"label": "2023 revaluation", "value": "VOA 2023 revaluation (effective 1 Apr 2023) re-set rateable values from 2017 list — transitional uplift on West Midlands hereditaments"},
            {"label": "Multiplier 2024-25", "value": "Standard non-domestic multiplier 54.6p (England, 2024-25); NHS pays full rate (no charitable relief); NDR 2024 Act splits multipliers"},
            {"label": "Hospitals Transformation Programme", "value": "Future Fit / HTP reshapes single-site emergency vs planned-care split between RSH and PRH — long-running planning-and-funding workstream affecting future hereditament base"},
            {"label": "Ockenden + RSP context", "value": "Donna Ockenden final maternity report Mar 2022; trust in Recovery Support Programme; affects management bandwidth + hereditament-appeal capacity"},
            {"label": "Funding trajectory", "value": "2021-22 c. £1.7M → 2023-24 c. £1.88M → 2024-25 £1.988M — multiplier + transitional uplift on twin-site hereditament"},
            {"label": "Delivery body", "value": "Trust E&F (rates appeals) + Valuation Office Agency + Shropshire Council + Telford & Wrekin Council"},
            {"label": "Policy owner", "value": "MHCLG (NDR policy) + HM Treasury + DHSC + NHSE Provider Finance + Shropshire, Telford and Wrekin ICB"},
            {"label": "Evaluation evidence", "value": "VOA Rating List 2023; NAO Business Rates Reform; Ockenden Report 2022; Trust ARA 2023-24; CQC RXW inspections"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2017 VOA list base + Future Fit pre-business-case · Successor: 2026 revaluation cycle + NDR 2024 Act multiplier-split + post-HTP single-emergency-site hereditament reset"}
        ],
        "notes": "Shrewsbury and Telford's rates line carries two distinct hereditaments under separate billing authorities (Shropshire Council for Royal Shrewsbury, Telford & Wrekin Council for Princess Royal). The VOA 2023 revaluation lifted rateable values across the West Midlands estate with transitional relief tapering, while the Non-Domestic Rating (Multipliers and Private Finance) Act 2024 introduces a multiplier split that reshapes future bills for large hereditaments. The Hospitals Transformation Programme (Future Fit) — long-running emergency vs planned-care reconfiguration — will eventually reshape the hereditament base. Donna Ockenden's 2022 maternity review and Recovery Support Programme oversight constrain management bandwidth on rates appeals. NHS pays the full 54.6p standard multiplier with no charitable relief.",
        "sources": [
            {"publisher": "The Shrewsbury and Telford Hospital NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.sath.nhs.uk/about-us/corporate-information/publications/"},
            {"publisher": "Valuation Office Agency", "title": "2023 Rating List", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "Ministry of Housing, Communities and Local Government", "title": "Non-Domestic Rating Act 2023 + Multipliers and Private Finance Act 2024", "url": "https://www.gov.uk/government/collections/business-rates"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Ockenden Review", "title": "Final Report — Independent Review of Maternity Services at the Shrewsbury and Telford Hospital NHS Trust", "url": "https://www.gov.uk/government/publications/final-report-of-the-ockenden-review"}
        ],
        "related": ["The Shrewsbury and Telford Hospital NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Business rates — Royal Berkshire NHS Foundation Trust", "Business rates — Bedfordshire Hospitals NHS Foundation Trust", "Valuation Office Agency"]
    },
    "Business rates — Royal Berkshire NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "Royal Berkshire NHS Foundation Trust"}],
        "description": "Royal Berkshire's £1.974M business-rates line covers non-domestic rates on the Royal Berkshire Hospital Reading central site plus West Berkshire Community Hospital, Prince Charles Eye Unit Windsor and ancillary outpatient premises across Berkshire West. The Valuation Office Agency assesses rateable values (2023 list effective 1 April 2023) and Reading Borough Council bills on the main hereditament. The trust is on the New Hospital Programme cohort with Reading rebuild deferred under January 2025 NHP Reset, reshaping the future hereditament base.",
        "beneficiaries": "c. 5,500 WTE staff serving a c. 600,000 Berkshire West catchment (Reading, West Berkshire, Wokingham); c. 130,000 ED attendances/yr at RBH ED; c. 80,000 admissions/yr; central Reading site dates from 1839 with very high rateable value reflecting prime urban location.",
        "legal_basis": "Local Government Finance Act 1988 (Schedule 6) — Non-Domestic Rating (Multipliers and Private Finance) Act 2024 — Non-Domestic Rating Act 2023 — DHSC Group Accounting Manual 2024-25 — NHS Act 2006 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£1.974M"},
            {"label": "Trust scale", "value": "Royal Berkshire Hospital Reading + West Berkshire Community Hospital + Prince Charles Eye Unit Windsor; c. 5,500 WTE"},
            {"label": "Billing authority", "value": "Reading Borough Council (RBH main hereditament) + West Berkshire Council + Royal Borough of Windsor and Maidenhead (ancillary)"},
            {"label": "2023 revaluation", "value": "VOA 2023 revaluation (effective 1 Apr 2023) re-set rateable values from 2017 list — central Reading hereditament reflects prime-urban uplift"},
            {"label": "Multiplier 2024-25", "value": "Standard non-domestic multiplier 54.6p (England, 2024-25); NHS pays full rate (no charitable relief); NDR 2024 Act splits multipliers"},
            {"label": "NHP cohort + Reset", "value": "Royal Berkshire on NHP cohort; Jan 2025 NHP Reset confirmed deferral — rebuild hereditament reset will eventually reshape rateable footprint"},
            {"label": "Heritage estate", "value": "RBH central site opened 1839 — Grade II listed elements + estate-aged infrastructure constrain hereditament-modernisation appeals"},
            {"label": "Funding trajectory", "value": "2021-22 c. £1.7M → 2023-24 c. £1.87M → 2024-25 £1.974M — multiplier + transitional uplift on prime-urban Reading hereditament"},
            {"label": "Delivery body", "value": "Trust E&F (rates appeals) + Valuation Office Agency + Reading Borough Council + West Berkshire Council"},
            {"label": "Policy owner", "value": "MHCLG (NDR policy) + HM Treasury + DHSC + NHSE Provider Finance + Buckinghamshire, Oxfordshire and Berkshire West ICB"},
            {"label": "Evaluation evidence", "value": "VOA Rating List 2023; NAO Business Rates Reform; NAO NHP 2025; Trust ARA 2023-24; CQC RHW inspections"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2017 VOA list + pre-NHP heritage hereditament base · Successor: 2026 revaluation + NDR 2024 Act multiplier-split + post-NHP-rebuild hereditament reset"}
        ],
        "notes": "Royal Berkshire's rates line is shaped by the trust's prime central Reading hereditament — RBH main site has high rateable value reflecting prime urban location. The VOA 2023 revaluation lifted rateable values across the Berkshire estate with transitional relief tapering, while the Non-Domestic Rating (Multipliers and Private Finance) Act 2024 introduces a multiplier split that reshapes future bills for large hereditaments. The trust is on the New Hospital Programme cohort but the January 2025 NHP Reset confirmed deferral, with the future Reading rebuild eventually resetting the hereditament base. Heritage Grade II listed elements and 1839-origin estate constrain hereditament-modernisation appeals. NHS pays the full 54.6p standard multiplier with no charitable relief.",
        "sources": [
            {"publisher": "Royal Berkshire NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.royalberkshire.nhs.uk/about-us/who-we-are/annual-reports-and-accounts/"},
            {"publisher": "Valuation Office Agency", "title": "2023 Rating List", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "Ministry of Housing, Communities and Local Government", "title": "Non-Domestic Rating Act 2023 + Multipliers and Private Finance Act 2024", "url": "https://www.gov.uk/government/collections/business-rates"},
            {"publisher": "National Audit Office", "title": "New Hospital Programme", "url": "https://www.nao.org.uk/reports/new-hospital-programme/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"}
        ],
        "related": ["Royal Berkshire NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Business rates — The Shrewsbury and Telford Hospital NHS Trust", "Business rates — Dartford and Gravesham NHS Trust", "New Hospital Programme"]
    },
    "Business rates — Dartford and Gravesham NHS Trust": {
        "aliases": [{"name": "Business rates", "parent": "Dartford and Gravesham NHS Trust"}],
        "description": "Dartford and Gravesham's £1.970M business-rates line covers non-domestic rates on the Darent Valley Hospital site at Dartford plus ancillary outpatient premises across north-west Kent. The Valuation Office Agency assesses rateable values (2023 list effective 1 April 2023) and Dartford Borough Council bills on the main hereditament. Darent Valley is a 1990s-era PFI hospital — the PFI vehicle owns the building but the trust as occupier remains liable for non-domestic rates, with the rates ledger sitting alongside the unitary-charge PFI line.",
        "beneficiaries": "c. 4,000 WTE staff serving a c. 500,000 north-west Kent and Bexley catchment (Dartford, Gravesham, Swanley, Bexley flow); c. 130,000 ED attendances/yr at Darent Valley ED; c. 65,000 admissions/yr; single-site PFI trust with substantial outpatient and elective volume.",
        "legal_basis": "Local Government Finance Act 1988 (Schedule 6) — Non-Domestic Rating (Multipliers and Private Finance) Act 2024 — Non-Domestic Rating Act 2023 — DHSC Group Accounting Manual 2024-25 — NHS Act 2006 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£1.970M"},
            {"label": "Trust scale", "value": "Darent Valley Hospital (Dartford) + ancillary outpatient/clinic premises; c. 4,000 WTE"},
            {"label": "Billing authority", "value": "Dartford Borough Council (Darent Valley Hospital hereditament)"},
            {"label": "PFI estate context", "value": "Darent Valley is a 1990s-era PFI hospital (The Hospital Company SPV) — PFI Co owns building, trust as occupier pays NDR; rates ledger sits alongside unitary-charge PFI line"},
            {"label": "2023 revaluation", "value": "VOA 2023 revaluation (effective 1 Apr 2023) re-set rateable values from 2017 list — south-east hereditament uplift"},
            {"label": "Multiplier 2024-25", "value": "Standard non-domestic multiplier 54.6p (England, 2024-25); NHS pays full rate (no charitable relief); NDR 2024 Act splits multipliers"},
            {"label": "Funding trajectory", "value": "2021-22 c. £1.7M → 2023-24 c. £1.87M → 2024-25 £1.970M — multiplier + transitional uplift on Darent Valley hereditament"},
            {"label": "Delivery body", "value": "Trust E&F (rates appeals) + Valuation Office Agency + Dartford Borough Council + The Hospital Company (PFI Co) for occupancy interface"},
            {"label": "Policy owner", "value": "MHCLG (NDR policy) + HM Treasury + DHSC + NHSE Provider Finance + Kent and Medway ICB"},
            {"label": "Evaluation evidence", "value": "VOA Rating List 2023; NAO Business Rates Reform; NAO PFI 2018; Trust ARA 2023-24; CQC RN7 inspections"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2017 VOA list + pre-revaluation PFI-occupier ledger · Successor: 2026 revaluation + NDR 2024 Act multiplier-split + 2030 PFI hand-back occupancy reset"}
        ],
        "notes": "Dartford and Gravesham's rates line is uncomplicated single-site at Darent Valley Hospital but distinctive in PFI-occupier interface — the building is owned by The Hospital Company SPV under the 1990s PFI deal, with the trust as occupier liable for non-domestic rates separately from unitary-charge PFI payments. The VOA 2023 revaluation lifted rateable values across the south-east estate with transitional relief tapering, while the Non-Domestic Rating (Multipliers and Private Finance) Act 2024 introduces a multiplier split that reshapes future bills for large hereditaments. PFI hand-back due c. 2030 will reset the occupancy interface. NHS pays the full 54.6p standard multiplier with no charitable relief. The trust is one of the original wave-1 PFI hospitals and a benchmark for late-1990s PFI cost trajectory.",
        "sources": [
            {"publisher": "Dartford and Gravesham NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.dgt.nhs.uk/about-us/publications-and-policies/"},
            {"publisher": "Valuation Office Agency", "title": "2023 Rating List", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "Ministry of Housing, Communities and Local Government", "title": "Non-Domestic Rating Act 2023 + Multipliers and Private Finance Act 2024", "url": "https://www.gov.uk/government/collections/business-rates"},
            {"publisher": "National Audit Office", "title": "PFI and PF2 (HC 718, 2018)", "url": "https://www.nao.org.uk/reports/pfi-and-pf2/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"}
        ],
        "related": ["Dartford and Gravesham NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Business rates — Royal Berkshire NHS Foundation Trust", "Business rates — Royal Surrey NHS Foundation Trust", "Private Finance Initiative"]
    },
    "Lease expenditure — Royal Free London NHS Foundation Trust": {
        "aliases": [{"name": "Lease expenditure", "parent": "Royal Free London NHS Foundation Trust"}],
        "description": "Royal Free London's £1.966M lease expenditure line covers IFRS 16 right-of-use lease costs across modular building leases, satellite-clinic premises rentals, equipment leases and short-term operational leases across the group's Royal Free Hospital Hampstead, Barnet Hospital, Chase Farm Hospital and integrated North London community footprint. Royal Free is the lead provider in the Royal Free London group model and runs a substantial outpatient and diagnostic estate that pulls in third-party leased premises across the catchment, with NHSPS rent disputes feeding the line.",
        "beneficiaries": "c. 11,000 WTE staff serving a c. 1.6M North London catchment (Camden, Barnet, Enfield, Haringey flow); c. 280,000 ED attendances/yr (Royal Free ED + Barnet ED + Chase Farm UTC); c. 145,000 admissions/yr; tertiary specialism in liver transplantation, HIV, infectious diseases (RFH HCID unit) and renal.",
        "legal_basis": "IFRS 16 Leases — DHSC Group Accounting Manual 2024-25 ch.7 — Landlord and Tenant Act 1954 — NHS Act 2006 — Health and Care Act 2022 — NHSPS rent-charging framework",
        "key_stats": [
            {"label": "Lease expenditure 2024-25", "value": "£1.966M"},
            {"label": "Trust scale", "value": "Royal Free Hospital Hampstead + Barnet Hospital + Chase Farm Hospital + NL community footprint; c. 11,000 WTE"},
            {"label": "IFRS 16 transition", "value": "DHSC adopted IFRS 16 from 2022-23 — consolidated previously off-balance-sheet operating leases onto trust balance sheet; line reflects right-of-use asset lease cost"},
            {"label": "Tertiary HCID role", "value": "RFH hosts national HCID (High Consequence Infectious Diseases) network unit + liver transplantation tertiary specialism — drives specialist leased-equipment and decant footprint"},
            {"label": "Group model context", "value": "Royal Free London group model with North Mid + Royal Free + Barnet + Chase Farm collaboration; satellite outpatient and diagnostic premises across NCL ICS"},
            {"label": "NHSPS estate interface", "value": "NHS Property Services owns multiple satellite community/outpatient hereditaments rented to RFL — rent-dispute (2018-2024 ongoing) affects lease accounting and arrears recognition"},
            {"label": "Composition", "value": "Modular building leases + satellite-clinic premises rentals + medical equipment leases (MRI/CT mobile units) + short-term operational leases"},
            {"label": "Funding trajectory", "value": "2021-22 c. £1.65M (pre-IFRS 16 mix) → 2022-23 IFRS 16 step-up → 2023-24 c. £1.85M → 2024-25 £1.966M — modular footprint + diagnostic-equipment lease growth"},
            {"label": "Delivery body", "value": "Trust E&F + Trust Procurement + NHS Property Services + private modular/equipment lease providers + NHSE Provider Finance"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + NCL ICB + HM Treasury (IFRS 16 adoption guidance)"},
            {"label": "Evaluation evidence", "value": "NAO NHS estates 2020; Trust ARA 2023-24 IFRS 16 disclosure; NHS Property Services rent-charging review; CQC RAL inspections"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-IFRS 16 operating-lease note disclosure · Successor: NCL ICS estate consolidation + 2030s diagnostic-equipment-lease refresh + NHSPS framework reform"}
        ],
        "notes": "Royal Free London's lease line is shaped by the trust's group-model integration across three hospital sites and an extensive satellite-outpatient and diagnostic footprint, plus the IFRS 16 transition (DHSC adopted from 2022-23) which moved previously off-balance-sheet operating leases on-book. NHS Property Services owns multiple community/outpatient hereditaments rented to RFL — the long-running NHSPS rent dispute (2018-2024) affects lease accounting and arrears recognition. The trust's national HCID network role at Royal Free Hospital and liver-transplantation tertiary specialism drive specialist leased-equipment footprint. Modular building leases for capacity expansion and elective recovery feed the line, alongside diagnostic-equipment leases (mobile MRI/CT) shared across the group.",
        "sources": [
            {"publisher": "Royal Free London NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.royalfree.nhs.uk/about-us/corporate-information/annual-report/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 7 — Leases)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "HM Treasury", "title": "Application of IFRS 16 Leases in the public sector", "url": "https://www.gov.uk/government/publications/government-financial-reporting-manual-2024-25"},
            {"publisher": "NHS Property Services", "title": "About NHSPS — estate and rent-charging", "url": "https://www.property.nhs.uk/"},
            {"publisher": "Care Quality Commission", "title": "Royal Free London NHS FT provider profile (RAL)", "url": "https://www.cqc.org.uk/provider/RAL"}
        ],
        "related": ["Royal Free London NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "NHS Property Services", "Lease expenditure — Imperial College Healthcare NHS Trust", "Department of Health and Social Care"]
    },
    "Business rates — Royal Surrey NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "Royal Surrey NHS Foundation Trust"}],
        "description": "Royal Surrey's £1.955M business-rates line covers non-domestic rates on the Royal Surrey County Hospital Guildford site plus ancillary outpatient, oncology and education premises. The Valuation Office Agency assesses rateable values (2023 list effective 1 April 2023) and Guildford Borough Council bills on the main hereditament. Royal Surrey hosts the St Luke's Cancer Centre — a regional oncology specialism — and entered an integrated provider agreement with Ashford and St Peter's Hospitals NHS FT in 2020 forming the Royal Surrey + Ashford and St Peter's integrated care model.",
        "beneficiaries": "c. 4,500 WTE staff serving a c. 330,000 west Surrey catchment plus regional oncology referrals via St Luke's Cancer Centre; c. 95,000 ED attendances/yr at Royal Surrey ED; c. 60,000 admissions/yr; St Luke's Cancer Centre is a regional oncology hub for west Surrey, north Hampshire and Sussex flow.",
        "legal_basis": "Local Government Finance Act 1988 (Schedule 6) — Non-Domestic Rating (Multipliers and Private Finance) Act 2024 — Non-Domestic Rating Act 2023 — DHSC Group Accounting Manual 2024-25 — NHS Act 2006 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£1.955M"},
            {"label": "Trust scale", "value": "Royal Surrey County Hospital Guildford + St Luke's Cancer Centre + ancillary outpatient premises; c. 4,500 WTE"},
            {"label": "Billing authority", "value": "Guildford Borough Council (Royal Surrey hereditament)"},
            {"label": "St Luke's oncology hereditament", "value": "Regional oncology specialism — radiotherapy and proton-relevant infrastructure adds distinctive specialist hereditament weight"},
            {"label": "2023 revaluation", "value": "VOA 2023 revaluation (effective 1 Apr 2023) re-set rateable values from 2017 list — south-east hereditament uplift on prime-Guildford location"},
            {"label": "Multiplier 2024-25", "value": "Standard non-domestic multiplier 54.6p (England, 2024-25); NHS pays full rate (no charitable relief); NDR 2024 Act splits multipliers"},
            {"label": "Integrated provider agreement", "value": "Royal Surrey + Ashford and St Peter's Hospitals NHS FT integrated provider agreement (2020) — shared CEO + group corporate functions; rates ledgers remain separate"},
            {"label": "Funding trajectory", "value": "2021-22 c. £1.7M → 2023-24 c. £1.85M → 2024-25 £1.955M — multiplier + transitional uplift on Guildford hereditament"},
            {"label": "Delivery body", "value": "Trust E&F (rates appeals) + Valuation Office Agency + Guildford Borough Council"},
            {"label": "Policy owner", "value": "MHCLG (NDR policy) + HM Treasury + DHSC + NHSE Provider Finance + Surrey Heartlands ICB"},
            {"label": "Evaluation evidence", "value": "VOA Rating List 2023; NAO Business Rates Reform; Trust ARA 2023-24; CQC RA2 inspections"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2017 VOA list + pre-integration Royal Surrey ledger · Successor: 2026 revaluation + NDR 2024 Act multiplier-split + further integration with Ashford and St Peter's hereditament management"}
        ],
        "notes": "Royal Surrey's rates line is shaped by the trust's central Guildford hereditament plus the St Luke's Cancer Centre regional oncology specialism — radiotherapy and specialist oncology infrastructure adds distinctive hereditament weight beyond the routine acute footprint. The VOA 2023 revaluation lifted rateable values across the south-east estate with transitional relief tapering, while the Non-Domestic Rating (Multipliers and Private Finance) Act 2024 introduces a multiplier split that reshapes future bills. The 2020 integrated provider agreement with Ashford and St Peter's Hospitals NHS FT shares CEO and corporate functions but rates ledgers remain separate trust by trust. NHS pays the full 54.6p standard multiplier with no charitable relief.",
        "sources": [
            {"publisher": "Royal Surrey NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.royalsurrey.nhs.uk/about-the-trust/publications/annual-report-and-accounts/"},
            {"publisher": "Valuation Office Agency", "title": "2023 Rating List", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "Ministry of Housing, Communities and Local Government", "title": "Non-Domestic Rating Act 2023 + Multipliers and Private Finance Act 2024", "url": "https://www.gov.uk/government/collections/business-rates"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Royal Surrey NHS FT provider profile (RA2)", "url": "https://www.cqc.org.uk/provider/RA2"}
        ],
        "related": ["Royal Surrey NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Business rates — Dartford and Gravesham NHS Trust", "Business rates — Bradford Teaching Hospitals NHS Foundation Trust", "Valuation Office Agency"]
    },
    "Transport (business + patient) — United Lincolnshire Hospitals NHS Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "United Lincolnshire Hospitals NHS Trust"}],
        "description": "United Lincolnshire Hospitals' £1.954M transport line covers business mileage (AfC Section 17 + AMAP), pool-fleet IFRS 16 lease costs, NEPTS contract pass-through and patient travel reimbursements across Lincoln County Hospital, Pilgrim Hospital Boston, Grantham & District Hospital and County Hospital Louth — a large, geographically dispersed multi-site footprint covering rural Lincolnshire. The trust's distinctive rural geography drives substantial inter-site staff travel, NEPTS volume and patient travel costs. NEPTS is commissioned through the Lincolnshire ICS lead-commissioner.",
        "beneficiaries": "c. 8,500 WTE staff serving a c. 770,000 Lincolnshire catchment (one of the largest geographically of any English acute trust); c. 220,000 ED attendances/yr (Lincoln + Pilgrim Boston + Grantham); c. 100,000 admissions/yr; rural multi-site DGH footprint with substantial inter-site patient-flow and staff-mileage demand.",
        "legal_basis": "NHS Act 2006 — NHSE Patient Transport Services Eligibility Criteria 2021 — Agenda for Change Section 17 (business mileage) — HMRC AMAP rates — IFRS 16 Leases (pool fleet) — DHSC Group Accounting Manual 2024-25 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£1.954M"},
            {"label": "Trust scale", "value": "Lincoln County Hospital + Pilgrim Hospital Boston + Grantham & District Hospital + County Hospital Louth; c. 8,500 WTE"},
            {"label": "Rural geography", "value": "One of the largest geographic catchments of any English acute trust — drives high staff-mileage and inter-site clinical-rotation transport demand"},
            {"label": "NEPTS commissioning", "value": "Lincolnshire ICS lead-commissioner NEPTS contract; eligibility per NHSE 2021 criteria"},
            {"label": "Composition", "value": "Business mileage (AfC S17 + AMAP 45p/25p frozen since 2011) + pool-fleet IFRS 16 leases + NEPTS pass-through + patient travel reimbursements"},
            {"label": "RSP context", "value": "Trust in long-term Recovery Support Programme; group arrangements with Northern Lincolnshire & Goole NHS FT under shared CEO since 2021 — drives inter-trust senior-management mileage"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove cancellation rebooking + agency travel claims"},
            {"label": "April 2025 NIC + fuel CPI", "value": "Indirect via NEPTS contractor pass-through + diesel CPI feed forward unit-cost pressure"},
            {"label": "Funding trajectory", "value": "2021-22 c. £1.65M → 2023-24 c. £1.85M → 2024-25 £1.954M — fuel CPI + NEPTS contract uplift + activity recovery"},
            {"label": "Delivery body", "value": "Trust E&F + outsourced NEPTS provider (Lincolnshire ICS lead-commissioner) + pool-fleet leasing partner + Trust HR (mileage)"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + NHSE Urgent and Emergency Care (NEPTS) + Lincolnshire ICB + DHSC"},
            {"label": "Evaluation evidence", "value": "NAO NEPTS 2019; CQC RWD inspections; NHSE NEPTS Eligibility Review 2021; Trust ARA 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-ICS CCG-commissioned NEPTS contracts · Successor: ICS-collaborative NEPTS retender + ULHT/NLAG group-model footprint rationalisation"}
        ],
        "notes": "United Lincolnshire's transport line is shaped by the trust's exceptional rural geography — one of the largest geographic catchments of any English acute trust — driving substantial inter-site staff mileage between Lincoln, Pilgrim Boston, Grantham and Louth, plus NEPTS volume for patient travel across remote Lincolnshire wolds and fens. The Lincolnshire ICS lead-commissioner NEPTS contract retender is the medium-term lever, with NHSE 2021 eligibility criteria tightening the patient-paid threshold. ULHT in long-term Recovery Support Programme oversight + group arrangements with Northern Lincolnshire & Goole NHS FT under a shared CEO since 2021 add distinctive inter-trust senior-management mileage. HMRC AMAP-rate freeze at 45p/mile since 2011 sustains internal-rate dispute pressure. Diesel CPI and April 2025 NIC step-up feed forward via NEPTS contractor pass-through.",
        "sources": [
            {"publisher": "United Lincolnshire Hospitals NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.ulh.nhs.uk/about/publications/"},
            {"publisher": "NHS England", "title": "Non-Emergency Patient Transport Services — National Framework + Eligibility Criteria 2021", "url": "https://www.england.nhs.uk/publication/non-emergency-patient-transport-services-nepts/"},
            {"publisher": "National Audit Office", "title": "NHS Transport Services", "url": "https://www.nao.org.uk/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "United Lincolnshire Hospitals NHS Trust provider profile (RWD)", "url": "https://www.cqc.org.uk/provider/RWD"}
        ],
        "related": ["United Lincolnshire Hospitals NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Transport (business + patient) — Calderdale and Huddersfield NHS Foundation Trust", "Transport (business + patient) — Great Western Hospitals NHS Foundation Trust", "NHS England"]
    },
    "Amortisation — Great Western Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Amortisation", "parent": "Great Western Hospitals NHS Foundation Trust"}],
        "description": "Great Western Hospitals' £1.952M amortisation line covers IAS 38 intangible-asset amortisation across capitalised software licences, EPR (electronic patient record) implementation costs and SaaS capitalised customisations across the Great Western Hospital Swindon main site and integrated community services footprint covering Wiltshire. GWH operates an integrated acute + community model under Bath, Swindon and Wiltshire ICS, runs a PFI hospital (built 2002 under one of the early acute PFI deals) and is on a sustained EPR uplift cycle aligned with NHSE Frontline Digitisation funding.",
        "beneficiaries": "c. 5,500 WTE staff serving a c. 350,000 Swindon and Wiltshire catchment plus integrated community services for c. 470,000 across Wiltshire; c. 100,000 ED attendances/yr at Great Western ED; c. 65,000 admissions/yr; integrated acute + community + sexual-health + prison-healthcare footprint.",
        "legal_basis": "IAS 38 Intangible Assets — DHSC Group Accounting Manual 2024-25 ch.5 — NHS Act 2006 — Health and Care Act 2022 — IAS 36 (impairment trigger interaction) — IFRIC SaaS configuration agenda decision 2021",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£1.952M"},
            {"label": "Trust scale", "value": "Great Western Hospital Swindon (PFI build 2002) + integrated Wiltshire community services; c. 5,500 WTE"},
            {"label": "EPR estate", "value": "EPR implementation + capitalised corporate-system licences + integrated community-IT (TPP SystmOne community footprint)"},
            {"label": "Frontline Digitisation funding", "value": "NHSE FD Programme funded EPR uplift + integration work — capitalised under IAS 38, amortised over useful life (typically 5-10 yrs for software)"},
            {"label": "Composition", "value": "Capitalised software licences + EPR implementation + capitalised SaaS configuration costs (post-IFRIC 2021 clarification) + integrated community-IT capitalised builds"},
            {"label": "Integrated care context", "value": "Integrated Acute + Community trust under BSW ICS — community-IT systems share capitalised-intangible base with acute (TPP SystmOne community footprint)"},
            {"label": "PFI building context", "value": "GWH is a 2002 PFI build (one of the early acute PFI deals); intangible line is separate from PFI unitary-charge premises line but shares trust digital footprint"},
            {"label": "Useful-life policy", "value": "Software typically 3-5 yrs; EPR major implementations 5-10 yrs per trust accounting policy disclosed in ARA"},
            {"label": "Funding trajectory", "value": "2021-22 c. £1.55M → 2023-24 c. £1.83M → 2024-25 £1.952M — sustained EPR uplift + corporate SaaS capitalisation cycle"},
            {"label": "Delivery body", "value": "Trust Digital + Finance functions + EPR vendor + NHSE Frontline Digitisation team + BSW ICS Digital"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + NHSE Transformation Directorate (Frontline Digitisation) + DHSC + Bath, Swindon and Wiltshire ICB"},
            {"label": "Evaluation evidence", "value": "NAO Frontline Digitisation review 2024; Trust ARA 2023-24 intangible-asset note; CQC RN3 inspections"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-FD baseline + integrated-community-acquisition capitalised systems · Successor: BSW ICS digital convergence + post-FD-stabilisation amortisation tail"}
        ],
        "notes": "Great Western Hospitals' amortisation profile is shaped by the trust's integrated acute + community model under Bath, Swindon and Wiltshire ICS — the IAS 38 intangible base aggregates EPR, integrated-community-IT (TPP SystmOne footprint) and corporate-system capitalised licences. NHSE Frontline Digitisation funding has driven a sustained capitalised-intangible amortisation cycle, with EPR major-implementation useful lives typically 5-10 yrs producing a long tail. The IFRS Interpretations Committee's 2021 SaaS configuration clarification reshaped what trusts can capitalise vs expense. GWH is also a 2002 PFI build (one of the early acute PFI deals) — the intangible line sits separately from the PFI unitary-charge premises line. Bath, Swindon and Wiltshire ICS digital convergence work is the medium-term lever.",
        "sources": [
            {"publisher": "Great Western Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.gwh.nhs.uk/about-us/publications/annual-report-and-accounts/"},
            {"publisher": "National Audit Office", "title": "Progress on Frontline Digitisation in the NHS", "url": "https://www.nao.org.uk/reports/digital-transformation-in-the-nhs/"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/connecting-health-and-care/frontline-digitisation/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 5 — Intangible assets)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Great Western Hospitals NHS FT provider profile (RN3)", "url": "https://www.cqc.org.uk/provider/RN3"}
        ],
        "related": ["Great Western Hospitals NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Frontline Digitisation Programme", "Amortisation — York and Scarborough Teaching Hospitals NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Amortisation — University Hospitals Plymouth NHS Trust": {
        "aliases": [{"name": "Amortisation", "parent": "University Hospitals Plymouth NHS Trust"}],
        "description": "University Hospitals Plymouth's £1.951M amortisation line covers IAS 38 intangible-asset amortisation across capitalised software licences, EPR implementation costs (Cerner / SystemC blend) and SaaS capitalised customisations across the Derriford Hospital main site plus tertiary-specialty footprint. UHP is a major regional tertiary centre serving the South West Peninsula — neurosciences, kidney transplantation, paediatric surgery and Major Trauma Centre status — and runs the South West's largest hospital site with substantial digital-asset capitalisation cycle aligned with NHSE Frontline Digitisation.",
        "beneficiaries": "c. 9,500 WTE staff serving a c. 450,000 Plymouth, South West Devon and East Cornwall catchment plus tertiary referrals across the South West Peninsula (c. 2.0M tertiary catchment); c. 130,000 ED attendances/yr at Derriford ED; c. 110,000 admissions/yr; Major Trauma Centre + neurosciences + kidney transplant + paediatric-surgery tertiary specialism.",
        "legal_basis": "IAS 38 Intangible Assets — DHSC Group Accounting Manual 2024-25 ch.5 — NHS Act 2006 — Health and Care Act 2022 — IAS 36 (impairment trigger interaction) — IFRIC SaaS configuration agenda decision 2021",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£1.951M"},
            {"label": "Trust scale", "value": "Derriford Hospital Plymouth (largest hospital site in the South West) + tertiary specialty footprint; c. 9,500 WTE"},
            {"label": "EPR estate", "value": "Cerner / SystemC blend + capitalised corporate-system licences + tertiary-specialty IT (PACS, RIS, oncology systems)"},
            {"label": "Frontline Digitisation funding", "value": "NHSE FD Programme funded EPR uplift + integration work — capitalised under IAS 38, amortised over useful life (typically 5-10 yrs for software)"},
            {"label": "Composition", "value": "Capitalised software licences + EPR implementation + capitalised SaaS configuration costs (post-IFRIC 2021 clarification) + tertiary-specialty IT capitalised builds"},
            {"label": "Tertiary specialism context", "value": "Major Trauma Centre + kidney transplantation + neurosciences + paediatric surgery — drives specialist clinical-system capitalisation beyond routine acute estate"},
            {"label": "Useful-life policy", "value": "Software typically 3-5 yrs; EPR major implementations 5-10 yrs per trust accounting policy disclosed in ARA"},
            {"label": "Devon ICS context", "value": "Devon ICB — UHP collaborates with Royal Devon University Healthcare under regional digital roadmap; capitalisation reflects Devon-wide LHCRE-era investments"},
            {"label": "Funding trajectory", "value": "2021-22 c. £1.6M → 2023-24 c. £1.83M → 2024-25 £1.951M — sustained EPR uplift + tertiary-specialty IT capitalisation cycle"},
            {"label": "Delivery body", "value": "Trust Digital + Finance functions + EPR vendors (Cerner / SystemC) + NHSE Frontline Digitisation team + Devon ICS Digital"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + NHSE Transformation Directorate (Frontline Digitisation) + DHSC + Devon ICB"},
            {"label": "Evaluation evidence", "value": "NAO Frontline Digitisation review 2024; Trust ARA 2023-24 intangible-asset note; CQC RK9 inspections"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-FD-baseline capitalised tertiary-specialty IT · Successor: Devon ICS digital convergence + post-FD-stabilisation amortisation tail"}
        ],
        "notes": "University Hospitals Plymouth's amortisation profile is shaped by the trust's tertiary regional role across the South West Peninsula — Major Trauma Centre, kidney transplantation, neurosciences and paediatric surgery all drive substantial specialist clinical-system capitalisation on top of the routine EPR investment. NHSE Frontline Digitisation funding has driven a sustained capitalised-intangible amortisation cycle, with EPR major-implementation useful lives typically 5-10 yrs producing a long tail. The IFRS Interpretations Committee's 2021 SaaS configuration clarification reshaped what trusts can capitalise vs expense. UHP collaborates with Royal Devon University Healthcare under a regional Devon ICS digital roadmap — capitalisation reflects Devon-wide LHCRE-era and post-LHCRE investments. The post-2024 NHSE Frontline Digitisation pivot to convergence rather than first-deployment funding is the medium-term lever.",
        "sources": [
            {"publisher": "University Hospitals Plymouth NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.plymouthhospitals.nhs.uk/about-us/annual-reports-and-accounts/"},
            {"publisher": "National Audit Office", "title": "Progress on Frontline Digitisation in the NHS", "url": "https://www.nao.org.uk/reports/digital-transformation-in-the-nhs/"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/connecting-health-and-care/frontline-digitisation/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 5 — Intangible assets)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "University Hospitals Plymouth NHS Trust provider profile (RK9)", "url": "https://www.cqc.org.uk/provider/RK9"}
        ],
        "related": ["University Hospitals Plymouth NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Frontline Digitisation Programme", "Amortisation — Great Western Hospitals NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Transport (business + patient) — Great Western Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "Great Western Hospitals NHS Foundation Trust"}],
        "description": "Great Western Hospitals' £1.941M transport line covers business mileage (AfC Section 17 + AMAP), pool-fleet IFRS 16 lease costs, NEPTS contract pass-through and patient travel reimbursements across the Great Western Hospital Swindon main site plus integrated Wiltshire community footprint serving rural Wiltshire. The integrated acute + community model under Bath, Swindon and Wiltshire ICS drives substantial inter-site community-staff mileage on top of routine acute NEPTS volume. NEPTS is commissioned through the BSW ICS lead-commissioner.",
        "beneficiaries": "c. 5,500 WTE staff serving a c. 350,000 Swindon catchment plus integrated community services for c. 470,000 across Wiltshire; c. 100,000 ED attendances/yr at Great Western ED; c. 65,000 admissions/yr; integrated acute + community + sexual-health + prison-healthcare footprint with rural Wiltshire community-staff mileage demand.",
        "legal_basis": "NHS Act 2006 — NHSE Patient Transport Services Eligibility Criteria 2021 — Agenda for Change Section 17 (business mileage) — HMRC AMAP rates — IFRS 16 Leases (pool fleet) — DHSC Group Accounting Manual 2024-25 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£1.941M"},
            {"label": "Trust scale", "value": "Great Western Hospital Swindon + integrated Wiltshire community services; c. 5,500 WTE"},
            {"label": "Integrated care model", "value": "Integrated acute + community trust under BSW ICS — community-staff mileage across rural Wiltshire drives distinctive line composition vs pure-acute trust"},
            {"label": "NEPTS commissioning", "value": "Bath, Swindon and Wiltshire ICS lead-commissioner NEPTS contract; eligibility per NHSE 2021 criteria"},
            {"label": "Composition", "value": "Business mileage (AfC S17 + AMAP 45p/25p frozen since 2011 — heavy community-staff weighting) + pool-fleet IFRS 16 leases + NEPTS pass-through + patient travel reimbursements"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove cancellation rebooking + agency travel claims (acute side)"},
            {"label": "April 2025 NIC + fuel CPI", "value": "Indirect via NEPTS contractor pass-through + diesel CPI feed forward unit-cost pressure"},
            {"label": "Funding trajectory", "value": "2021-22 c. £1.65M → 2023-24 c. £1.83M → 2024-25 £1.941M — fuel CPI + NEPTS contract uplift + community-recovery activity"},
            {"label": "Delivery body", "value": "Trust E&F + outsourced NEPTS provider (BSW ICS lead-commissioner) + pool-fleet leasing partner + Trust HR (mileage)"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + NHSE Urgent and Emergency Care (NEPTS) + Bath, Swindon and Wiltshire ICB + DHSC"},
            {"label": "Evaluation evidence", "value": "NAO NEPTS 2019; CQC RN3 inspections; NHSE NEPTS Eligibility Review 2021; Trust ARA 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-ICS CCG-commissioned NEPTS contracts + pre-2016 acute-only mileage base · Successor: BSW ICS-collaborative NEPTS retender + integrated-community mileage rationalisation"}
        ],
        "notes": "Great Western's transport line is shaped by the trust's integrated acute + community model under Bath, Swindon and Wiltshire ICS — community-staff mileage across rural Wiltshire drives distinctive line composition vs pure-acute trusts, on top of routine acute NEPTS volume from Great Western Hospital. The Bath, Swindon and Wiltshire ICS lead-commissioner NEPTS contract retender is the medium-term lever, with NHSE 2021 eligibility criteria tightening the patient-paid threshold. HMRC AMAP-rate freeze at 45p/mile since 2011 is particularly material for an integrated-community trust given the heavy community-staff mileage weighting. Diesel CPI and April 2025 NIC step-up feed forward via NEPTS contractor pass-through. The line sits alongside the GWH PFI premises footprint within the broader Premises & Infrastructure category.",
        "sources": [
            {"publisher": "Great Western Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.gwh.nhs.uk/about-us/publications/annual-report-and-accounts/"},
            {"publisher": "NHS England", "title": "Non-Emergency Patient Transport Services — National Framework + Eligibility Criteria 2021", "url": "https://www.england.nhs.uk/publication/non-emergency-patient-transport-services-nepts/"},
            {"publisher": "National Audit Office", "title": "NHS Transport Services", "url": "https://www.nao.org.uk/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Great Western Hospitals NHS FT provider profile (RN3)", "url": "https://www.cqc.org.uk/provider/RN3"}
        ],
        "related": ["Great Western Hospitals NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Transport (business + patient) — United Lincolnshire Hospitals NHS Trust", "Amortisation — Great Western Hospitals NHS Foundation Trust", "NHS England"]
    },
    "Business rates — Bradford Teaching Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "Bradford Teaching Hospitals NHS Foundation Trust"}],
        "description": "Bradford Teaching Hospitals' £1.939M business-rates line covers non-domestic rates on the Bradford Royal Infirmary main site and St Luke's Hospital plus ancillary outpatient and education premises. The Valuation Office Agency assesses rateable values (2023 list effective 1 April 2023) and Bradford Metropolitan District Council bills on the main hereditament. Bradford Teaching Hospitals is a major teaching hospital with affiliations to the University of Bradford and Bradford Institute for Health Research, hosting the Born in Bradford longitudinal study and tertiary specialism in burns and plastics for the Yorkshire region.",
        "beneficiaries": "c. 6,000 WTE staff serving a c. 540,000 Bradford district catchment plus regional referrals via the Yorkshire Plastic Surgery and Burns Service; c. 145,000 ED attendances/yr at BRI ED; c. 80,000 admissions/yr; major teaching hospital with Bradford Institute for Health Research and Born in Bradford research footprint.",
        "legal_basis": "Local Government Finance Act 1988 (Schedule 6) — Non-Domestic Rating (Multipliers and Private Finance) Act 2024 — Non-Domestic Rating Act 2023 — DHSC Group Accounting Manual 2024-25 — NHS Act 2006 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£1.938606M"},
            {"label": "Trust scale", "value": "Bradford Royal Infirmary + St Luke's Hospital + ancillary outpatient/education premises; c. 6,000 WTE"},
            {"label": "Billing authority", "value": "Bradford Metropolitan District Council (BRI + St Luke's hereditaments)"},
            {"label": "2023 revaluation", "value": "VOA 2023 revaluation (effective 1 Apr 2023) re-set rateable values from 2017 list — Yorkshire & Humber hereditament uplift"},
            {"label": "Multiplier 2024-25", "value": "Standard non-domestic multiplier 54.6p (England, 2024-25); NHS pays full rate (no charitable relief); NDR 2024 Act splits multipliers"},
            {"label": "Teaching + tertiary specialism", "value": "Yorkshire Plastic Surgery and Burns Service (regional tertiary specialism) + Bradford Institute for Health Research + Born in Bradford research cohort — adds research/teaching hereditament weight"},
            {"label": "WYAA ICS context", "value": "West Yorkshire Association of Acute Trusts (WYAAT) shared-services + collaboration footprint within West Yorkshire ICS"},
            {"label": "Funding trajectory", "value": "2021-22 c. £1.7M → 2023-24 c. £1.85M → 2024-25 £1.939M — multiplier + transitional uplift on Bradford hereditament"},
            {"label": "Delivery body", "value": "Trust E&F (rates appeals) + Valuation Office Agency + Bradford Metropolitan District Council"},
            {"label": "Policy owner", "value": "MHCLG (NDR policy) + HM Treasury + DHSC + NHSE Provider Finance + West Yorkshire ICB"},
            {"label": "Evaluation evidence", "value": "VOA Rating List 2023; NAO Business Rates Reform; Trust ARA 2023-24; CQC RAE inspections"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2017 VOA list base · Successor: 2026 revaluation cycle + NDR 2024 Act multiplier-split implementation"}
        ],
        "notes": "Bradford Teaching Hospitals' rates line is shaped by the trust's central Bradford Royal Infirmary and St Luke's hereditaments, plus the regional Yorkshire Plastic Surgery and Burns Service tertiary specialism that adds distinctive specialist hereditament weight. The Bradford Institute for Health Research and Born in Bradford research cohort add further research/teaching footprint. The VOA 2023 revaluation lifted rateable values across the Yorkshire & Humber estate with transitional relief tapering, while the Non-Domestic Rating (Multipliers and Private Finance) Act 2024 introduces a multiplier split that reshapes future bills. WYAAT (West Yorkshire Association of Acute Trusts) shared-services collaboration within West Yorkshire ICS sits alongside individual-trust hereditament management. NHS pays the full 54.6p standard multiplier with no charitable relief.",
        "sources": [
            {"publisher": "Bradford Teaching Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.bradfordhospitals.nhs.uk/about-us/our-publications/annual-report-and-accounts/"},
            {"publisher": "Valuation Office Agency", "title": "2023 Rating List", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "Ministry of Housing, Communities and Local Government", "title": "Non-Domestic Rating Act 2023 + Multipliers and Private Finance Act 2024", "url": "https://www.gov.uk/government/collections/business-rates"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Bradford Teaching Hospitals NHS FT provider profile (RAE)", "url": "https://www.cqc.org.uk/provider/RAE"}
        ],
        "related": ["Bradford Teaching Hospitals NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Business rates — Royal Surrey NHS Foundation Trust", "Business rates — North Cumbria Integrated Care NHS Foundation Trust", "Valuation Office Agency"]
    },
    "Transport (business + patient) — Calderdale and Huddersfield NHS Foundation Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "Calderdale and Huddersfield NHS Foundation Trust"}],
        "description": "Calderdale and Huddersfield's £1.932M transport line covers business mileage (AfC Section 17 + AMAP), pool-fleet IFRS 16 lease costs, NEPTS contract pass-through and patient travel reimbursements across Calderdale Royal Hospital Halifax and Huddersfield Royal Infirmary plus integrated community services. The trust's twin-DGH model with cross-borough patient flow between Calderdale and Kirklees, and the long-running Hospital and Community Services Strategy reconfiguration (Calderdale planned care vs HRI emergency centralisation), shape inter-site staff and patient transport demand.",
        "beneficiaries": "c. 6,000 WTE staff serving a c. 470,000 Calderdale + Greater Huddersfield catchment; c. 175,000 ED attendances/yr (Calderdale ED + HRI ED — twin-ED inter-site flow); c. 95,000 admissions/yr; integrated acute + community footprint with twin-DGH cross-borough patient flow.",
        "legal_basis": "NHS Act 2006 — NHSE Patient Transport Services Eligibility Criteria 2021 — Agenda for Change Section 17 (business mileage) — HMRC AMAP rates — IFRS 16 Leases (pool fleet) — DHSC Group Accounting Manual 2024-25 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£1.93196M"},
            {"label": "Trust scale", "value": "Calderdale Royal Hospital (Halifax) + Huddersfield Royal Infirmary + integrated community services; c. 6,000 WTE"},
            {"label": "Twin-DGH inter-site flow", "value": "Twin EDs at CRH and HRI generate distinctive inter-site patient transfer + cross-borough staff mileage between Calderdale and Kirklees councils"},
            {"label": "HCS reconfiguration", "value": "Hospital and Community Services Strategy — long-running planned-emergency split between CRH and HRI; reshapes inter-site transport demand"},
            {"label": "NEPTS commissioning", "value": "West Yorkshire ICS lead-commissioner NEPTS contract; eligibility per NHSE 2021 criteria"},
            {"label": "Composition", "value": "Business mileage (AfC S17 + AMAP 45p/25p frozen since 2011) + pool-fleet IFRS 16 leases + NEPTS pass-through + patient travel reimbursements"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove cancellation rebooking + agency travel claims"},
            {"label": "April 2025 NIC + fuel CPI", "value": "Indirect via NEPTS contractor pass-through + diesel CPI feed forward unit-cost pressure"},
            {"label": "Funding trajectory", "value": "2021-22 c. £1.65M → 2023-24 c. £1.83M → 2024-25 £1.932M — fuel CPI + NEPTS contract uplift + activity recovery"},
            {"label": "Delivery body", "value": "Trust E&F + outsourced NEPTS provider (West Yorkshire ICS lead-commissioner) + pool-fleet leasing partner + Trust HR (mileage)"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + NHSE Urgent and Emergency Care (NEPTS) + West Yorkshire ICB + DHSC"},
            {"label": "Evaluation evidence", "value": "NAO NEPTS 2019; CQC RWY inspections; NHSE NEPTS Eligibility Review 2021; Trust ARA 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-ICS CCG-commissioned NEPTS contracts · Successor: West Yorkshire ICS-collaborative NEPTS retender + post-HCS reconfiguration single-emergency-site mileage profile"}
        ],
        "notes": "Calderdale and Huddersfield's transport line is shaped by the trust's twin-DGH model — twin EDs at Calderdale Royal Hospital (Halifax) and Huddersfield Royal Infirmary generating distinctive inter-site patient transfer and cross-borough staff mileage between Calderdale and Kirklees councils. The long-running Hospital and Community Services Strategy (HCS) reconfiguration — planned-care concentration at one site, emergency at the other — will eventually reshape inter-site transport demand. NEPTS is commissioned through the West Yorkshire ICS lead-commissioner. HMRC AMAP-rate freeze at 45p/mile since 2011 sustains internal-rate dispute pressure. Diesel CPI and April 2025 NIC step-up feed forward via NEPTS contractor pass-through. WYAAT shared-services collaboration adds a peer-trust mileage layer.",
        "sources": [
            {"publisher": "Calderdale and Huddersfield NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.cht.nhs.uk/about-us/publications/annual-report-and-accounts/"},
            {"publisher": "NHS England", "title": "Non-Emergency Patient Transport Services — National Framework + Eligibility Criteria 2021", "url": "https://www.england.nhs.uk/publication/non-emergency-patient-transport-services-nepts/"},
            {"publisher": "National Audit Office", "title": "NHS Transport Services", "url": "https://www.nao.org.uk/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Calderdale and Huddersfield NHS FT provider profile (RWY)", "url": "https://www.cqc.org.uk/provider/RWY"}
        ],
        "related": ["Calderdale and Huddersfield NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Transport (business + patient) — United Lincolnshire Hospitals NHS Trust", "Transport (business + patient) — Great Western Hospitals NHS Foundation Trust", "NHS England"]
    },
    "Business rates — North Cumbria Integrated Care NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "North Cumbria Integrated Care NHS Foundation Trust"}],
        "description": "North Cumbria Integrated Care's £1.929M business-rates line covers non-domestic rates on the Cumberland Infirmary Carlisle (PFI hospital) and West Cumberland Hospital Whitehaven sites plus integrated community premises across North Cumbria. The Valuation Office Agency assesses rateable values (2023 list effective 1 April 2023) and Cumberland Council bills on both main hereditaments. NCIC is an integrated acute + community trust covering an exceptional rural geography in North Cumbria, with the Cumberland Infirmary 2000 PFI build adding distinctive PFI-occupier hereditament dynamics.",
        "beneficiaries": "c. 6,500 WTE staff serving a c. 320,000 North Cumbria catchment (Carlisle, Whitehaven, Workington, Penrith); c. 110,000 ED attendances/yr (Cumberland Infirmary ED + WCH ED); c. 60,000 admissions/yr; integrated acute + community + mental-health-liaison footprint across exceptional rural geography.",
        "legal_basis": "Local Government Finance Act 1988 (Schedule 6) — Non-Domestic Rating (Multipliers and Private Finance) Act 2024 — Non-Domestic Rating Act 2023 — DHSC Group Accounting Manual 2024-25 — NHS Act 2006 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£1.929221M"},
            {"label": "Trust scale", "value": "Cumberland Infirmary Carlisle (PFI) + West Cumberland Hospital Whitehaven + integrated community premises; c. 6,500 WTE"},
            {"label": "Billing authority", "value": "Cumberland Council (post-Apr 2023 unitary reorganisation — formerly Carlisle City Council + Allerdale + Copeland)"},
            {"label": "PFI estate context", "value": "Cumberland Infirmary 2000 PFI build (Health Management Carlisle SPV) — PFI Co owns building, trust as occupier pays NDR; rates ledger sits alongside unitary-charge PFI line"},
            {"label": "2023 revaluation", "value": "VOA 2023 revaluation (effective 1 Apr 2023) re-set rateable values from 2017 list — North West hereditament uplift"},
            {"label": "Multiplier 2024-25", "value": "Standard non-domestic multiplier 54.6p (England, 2024-25); NHS pays full rate (no charitable relief); NDR 2024 Act splits multipliers"},
            {"label": "Cumberland unitary reorganisation", "value": "April 2023 Cumberland Council unitary creation merged Carlisle + Allerdale + Copeland — single billing authority now for both NCIC main hereditaments"},
            {"label": "WCH NHP context", "value": "West Cumberland Hospital — phased rebuild already underway pre-NHP (Phase 2 outstanding); affects future hereditament base"},
            {"label": "Funding trajectory", "value": "2021-22 c. £1.65M → 2023-24 c. £1.83M → 2024-25 £1.929M — multiplier + transitional uplift on twin-site hereditament"},
            {"label": "Delivery body", "value": "Trust E&F (rates appeals) + Valuation Office Agency + Cumberland Council + Health Management Carlisle (PFI Co) for occupancy interface"},
            {"label": "Policy owner", "value": "MHCLG (NDR policy) + HM Treasury + DHSC + NHSE Provider Finance + North East and North Cumbria ICB"},
            {"label": "Evaluation evidence", "value": "VOA Rating List 2023; NAO Business Rates Reform; NAO PFI 2018; Trust ARA 2023-24; CQC RNN inspections"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2023 separate Carlisle/Allerdale/Copeland billing + 2017 VOA list · Successor: 2026 revaluation + NDR 2024 Act multiplier-split + WCH Phase 2 rebuild hereditament reset"}
        ],
        "notes": "North Cumbria Integrated Care's rates line is shaped by the trust's twin-site footprint — Cumberland Infirmary Carlisle (2000 PFI build) and West Cumberland Hospital Whitehaven — across an exceptional rural geography. The Cumberland Infirmary PFI building is owned by Health Management Carlisle SPV with the trust as occupier liable for non-domestic rates separately from unitary-charge payments. The April 2023 Cumberland Council unitary reorganisation (merging Carlisle, Allerdale and Copeland) consolidated the billing authority for both hereditaments. The VOA 2023 revaluation lifted rateable values across the North West estate, while the NDR 2024 Act multiplier split reshapes future bills. West Cumberland Hospital Phase 2 rebuild outstanding from pre-NHP scheme will eventually reset that hereditament. NHS pays the full 54.6p standard multiplier with no charitable relief.",
        "sources": [
            {"publisher": "North Cumbria Integrated Care NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.ncic.nhs.uk/about-us/publications/"},
            {"publisher": "Valuation Office Agency", "title": "2023 Rating List", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "Ministry of Housing, Communities and Local Government", "title": "Non-Domestic Rating Act 2023 + Multipliers and Private Finance Act 2024", "url": "https://www.gov.uk/government/collections/business-rates"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "North Cumbria Integrated Care NHS FT provider profile (RNN)", "url": "https://www.cqc.org.uk/provider/RNN"}
        ],
        "related": ["North Cumbria Integrated Care NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Business rates — Bradford Teaching Hospitals NHS Foundation Trust", "Business rates — Great Western Hospitals NHS Foundation Trust", "Private Finance Initiative"]
    },
    "Business rates — Great Western Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "Great Western Hospitals NHS Foundation Trust"}],
        "description": "Great Western Hospitals' £1.926M business-rates line covers non-domestic rates on the Great Western Hospital Swindon (2002 PFI build) site plus integrated Wiltshire community premises. The Valuation Office Agency assesses rateable values (2023 list effective 1 April 2023) and Swindon Borough Council bills on the main hereditament. Great Western is one of the early-wave acute PFI hospitals (Carillion legacy initially, novated to Skanska/Engie post-2018 collapse) — the PFI vehicle owns the building but the trust as occupier remains liable for non-domestic rates, with the rates ledger sitting alongside the unitary-charge PFI line.",
        "beneficiaries": "c. 5,500 WTE staff serving a c. 350,000 Swindon catchment plus integrated community services for c. 470,000 across Wiltshire; c. 100,000 ED attendances/yr at Great Western ED; c. 65,000 admissions/yr; integrated acute + community + sexual-health + prison-healthcare footprint with 2002 PFI build hereditament.",
        "legal_basis": "Local Government Finance Act 1988 (Schedule 6) — Non-Domestic Rating (Multipliers and Private Finance) Act 2024 — Non-Domestic Rating Act 2023 — DHSC Group Accounting Manual 2024-25 — NHS Act 2006 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£1.926M"},
            {"label": "Trust scale", "value": "Great Western Hospital Swindon (2002 PFI build) + integrated Wiltshire community premises; c. 5,500 WTE"},
            {"label": "Billing authority", "value": "Swindon Borough Council (Great Western Hospital hereditament) + Wiltshire Council (community premises)"},
            {"label": "PFI estate context", "value": "GWH is a 2002 PFI build (Hospital Company Swindon SPV; Carillion legacy FM, novated to Skanska/Engie post-2018 collapse) — PFI Co owns building, trust as occupier pays NDR"},
            {"label": "2023 revaluation", "value": "VOA 2023 revaluation (effective 1 Apr 2023) re-set rateable values from 2017 list — South West hereditament uplift"},
            {"label": "Multiplier 2024-25", "value": "Standard non-domestic multiplier 54.6p (England, 2024-25); NHS pays full rate (no charitable relief); NDR 2024 Act splits multipliers"},
            {"label": "Carillion novation legacy", "value": "Post-2018 Carillion collapse FM contract novated through Engie / Equans — affects occupancy-management interface, not hereditament directly"},
            {"label": "Funding trajectory", "value": "2021-22 c. £1.65M → 2023-24 c. £1.82M → 2024-25 £1.926M — multiplier + transitional uplift on Swindon hereditament"},
            {"label": "Delivery body", "value": "Trust E&F (rates appeals) + Valuation Office Agency + Swindon Borough Council + Hospital Company Swindon (PFI Co) for occupancy interface"},
            {"label": "Policy owner", "value": "MHCLG (NDR policy) + HM Treasury + DHSC + NHSE Provider Finance + Bath, Swindon and Wiltshire ICB"},
            {"label": "Evaluation evidence", "value": "VOA Rating List 2023; NAO Business Rates Reform; NAO PFI 2018; Trust ARA 2023-24; CQC RN3 inspections"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2017 VOA list + pre-revaluation PFI-occupier ledger · Successor: 2026 revaluation + NDR 2024 Act multiplier-split + 2030s PFI hand-back occupancy reset"}
        ],
        "notes": "Great Western's rates line is uncomplicated single-acute-site at Swindon but distinctive in PFI-occupier interface — the building is owned by Hospital Company Swindon SPV under the 2002 PFI deal, with the trust as occupier liable for non-domestic rates separately from unitary-charge PFI payments. Carillion was the original FM contractor; post-2018 collapse the FM has been novated through Engie / Equans, affecting occupancy management but not hereditament directly. The VOA 2023 revaluation lifted rateable values across the South West estate with transitional relief tapering, while the Non-Domestic Rating (Multipliers and Private Finance) Act 2024 introduces a multiplier split that reshapes future bills. PFI hand-back due c. 2032 will reset the occupancy interface. NHS pays the full 54.6p standard multiplier with no charitable relief.",
        "sources": [
            {"publisher": "Great Western Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.gwh.nhs.uk/about-us/publications/annual-report-and-accounts/"},
            {"publisher": "Valuation Office Agency", "title": "2023 Rating List", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "National Audit Office", "title": "PFI and PF2 (HC 718, 2018)", "url": "https://www.nao.org.uk/reports/pfi-and-pf2/"},
            {"publisher": "Ministry of Housing, Communities and Local Government", "title": "Non-Domestic Rating Act 2023 + Multipliers and Private Finance Act 2024", "url": "https://www.gov.uk/government/collections/business-rates"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"}
        ],
        "related": ["Great Western Hospitals NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Business rates — North Cumbria Integrated Care NHS Foundation Trust", "Business rates — Dartford and Gravesham NHS Trust", "Private Finance Initiative"]
    },
    "Business rates — Milton Keynes University Hospital NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "Milton Keynes University Hospital NHS Foundation Trust"}],
        "description": "Milton Keynes University Hospital's £1.917M business-rates line covers non-domestic rates on the Milton Keynes University Hospital Eaglestone main site plus ancillary outpatient and education premises. The Valuation Office Agency assesses rateable values (2023 list effective 1 April 2023) and Milton Keynes City Council bills on the main hereditament. MKUH is a single-site DGH on the New Hospital Programme cohort with capacity expansion and rebuild plans deferred under the January 2025 NHP Reset, with a fast-growing Milton Keynes population driving sustained activity-and-hereditament expansion.",
        "beneficiaries": "c. 4,500 WTE staff serving a c. 360,000 Milton Keynes city catchment plus surrounding Bedfordshire / Buckinghamshire flow (one of the fastest-growing populations in England); c. 110,000 ED attendances/yr at MKUH ED; c. 65,000 admissions/yr; single-site DGH with university teaching affiliation (University of Buckingham medical school).",
        "legal_basis": "Local Government Finance Act 1988 (Schedule 6) — Non-Domestic Rating (Multipliers and Private Finance) Act 2024 — Non-Domestic Rating Act 2023 — DHSC Group Accounting Manual 2024-25 — NHS Act 2006 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£1.917M"},
            {"label": "Trust scale", "value": "Milton Keynes University Hospital Eaglestone + ancillary outpatient/education premises; c. 4,500 WTE"},
            {"label": "Billing authority", "value": "Milton Keynes City Council (MKUH hereditament — became unitary city status May 2022)"},
            {"label": "Population growth context", "value": "Milton Keynes population among fastest-growing in England (c. 280k 2011 → c. 290k 2021 → projected c. 360k+ by 2031); drives sustained activity + hereditament-expansion pressure"},
            {"label": "NHP cohort + Reset", "value": "MKUH on NHP cohort for capacity expansion and partial rebuild; Jan 2025 NHP Reset confirmed deferral — capacity-build hereditament reset will eventually reshape rateable footprint"},
            {"label": "2023 revaluation", "value": "VOA 2023 revaluation (effective 1 Apr 2023) re-set rateable values from 2017 list — South East hereditament uplift"},
            {"label": "Multiplier 2024-25", "value": "Standard non-domestic multiplier 54.6p (England, 2024-25); NHS pays full rate (no charitable relief); NDR 2024 Act splits multipliers"},
            {"label": "Funding trajectory", "value": "2021-22 c. £1.6M → 2023-24 c. £1.81M → 2024-25 £1.917M — multiplier + transitional uplift + capacity-expansion modular hereditament additions"},
            {"label": "Delivery body", "value": "Trust E&F (rates appeals) + Valuation Office Agency + Milton Keynes City Council"},
            {"label": "Policy owner", "value": "MHCLG (NDR policy) + HM Treasury + DHSC + NHSE Provider Finance + Bedfordshire, Luton and Milton Keynes ICB"},
            {"label": "Evaluation evidence", "value": "VOA Rating List 2023; NAO Business Rates Reform; NAO NHP 2025; Trust ARA 2023-24; CQC RD8 inspections"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2017 VOA list + pre-NHP capacity baseline · Successor: 2026 revaluation + NDR 2024 Act multiplier-split + post-NHP-rebuild capacity-expansion hereditament"}
        ],
        "notes": "Milton Keynes University Hospital's rates line is shaped by the trust's single-site DGH model serving one of the fastest-growing populations in England — Milton Keynes population growth from c. 280k (2011) to projected c. 360k+ (2031) drives sustained activity and hereditament-expansion pressure. The VOA 2023 revaluation lifted rateable values across the South East estate with transitional relief tapering, while the Non-Domestic Rating (Multipliers and Private Finance) Act 2024 introduces a multiplier split. The trust is on the New Hospital Programme cohort for capacity expansion and partial rebuild; the January 2025 NHP Reset confirmed deferral, with future rebuild eventually resetting the hereditament base. Milton Keynes Council's May 2022 unitary city-status reorganisation consolidated billing-authority status. NHS pays the full 54.6p standard multiplier with no charitable relief.",
        "sources": [
            {"publisher": "Milton Keynes University Hospital NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.mkuh.nhs.uk/about-us/our-publications/annual-reports-and-accounts/"},
            {"publisher": "Valuation Office Agency", "title": "2023 Rating List", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "Ministry of Housing, Communities and Local Government", "title": "Non-Domestic Rating Act 2023 + Multipliers and Private Finance Act 2024", "url": "https://www.gov.uk/government/collections/business-rates"},
            {"publisher": "National Audit Office", "title": "New Hospital Programme", "url": "https://www.nao.org.uk/reports/new-hospital-programme/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"}
        ],
        "related": ["Milton Keynes University Hospital NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Business rates — Bedfordshire Hospitals NHS Foundation Trust", "Business rates — Great Western Hospitals NHS Foundation Trust", "New Hospital Programme"]
    },
    "Establishment costs — Milton Keynes University Hospital NHS Foundation Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "Milton Keynes University Hospital NHS Foundation Trust"}],
        "description": "Milton Keynes University Hospital's £1.908M establishment costs line covers postage, telecoms, courier, training and development, printing, recruitment advertising and broader trust-running corporate-services consumption across the MKUH Eaglestone main site. As a single-site DGH serving one of the fastest-growing populations in England plus a New Hospital Programme cohort trust (deferred under January 2025 NHP Reset), MKUH faces distinctive establishment-cost pressures around recruitment retention, capacity-expansion communications, EPR change-management and university-teaching affiliation overheads.",
        "beneficiaries": "c. 4,500 WTE staff serving a c. 360,000 Milton Keynes city catchment plus surrounding Bedfordshire / Buckinghamshire flow; c. 110,000 ED attendances/yr at MKUH ED; c. 65,000 admissions/yr; single-site DGH with University of Buckingham medical school teaching affiliation; one of fastest-growing populations in England.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) — IAS 1 Presentation of Financial Statements — NHS Act 2006 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£1.908M"},
            {"label": "Trust scale", "value": "Milton Keynes University Hospital Eaglestone single-site DGH; c. 4,500 WTE"},
            {"label": "Population growth pressure", "value": "Milton Keynes population among fastest-growing in England — drives recruitment-advertising demand + capacity-expansion communications + new-staff-onboarding training"},
            {"label": "NHP cohort + Reset", "value": "MKUH on NHP cohort for capacity expansion and partial rebuild; Jan 2025 NHP Reset confirmed deferral — communications cost continues independent of capital build"},
            {"label": "Composition", "value": "Postage + telecoms + courier + training and development + printing + recruitment advertising + corporate-services consumption + university-teaching-affiliation overheads"},
            {"label": "University teaching affiliation", "value": "University of Buckingham medical school partnership — drives distinctive teaching-overhead establishment cost (printing, training collateral, governance liaison)"},
            {"label": "Frontline Digitisation EPR", "value": "MKUH on Frontline Digitisation programme — training and change-management feeds establishment line during EPR rollout"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove communications + cancellation rebooking + agency-recruitment advertising"},
            {"label": "April 2025 NIC step-up", "value": "Indirect via supplier-side cost pass-through on telecoms + courier + training contracts"},
            {"label": "Funding trajectory", "value": "2021-22 c. £1.6M → 2023-24 c. £1.8M → 2024-25 £1.908M — population-growth recruitment + EPR training + NHP comms"},
            {"label": "Delivery body", "value": "Trust Corporate Services + Trust IT (telecoms) + Trust HR (training + recruitment) + NHP delivery team + University of Buckingham liaison"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + NHP delivery + Bedfordshire, Luton and Milton Keynes ICB + NHSE Transformation (Frontline Digitisation)"},
            {"label": "Evaluation evidence", "value": "NAO NHP 2025; NAO Frontline Digitisation 2024; Trust ARA 2023-24; CQC RD8 inspections; Model Hospital corporate benchmarks"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-NHP-cohort baseline + pre-Buckingham medical school affiliation · Successor: post-NHP capacity-expansion steady-state + EPR steady-state training"}
        ],
        "notes": "Milton Keynes University Hospital's establishment line is shaped by the trust's distinctive operating context — a single-site DGH serving one of the fastest-growing populations in England with sustained recruitment-advertising demand, plus the New Hospital Programme cohort capacity-expansion communications continuing independent of the January 2025 NHP Reset deferral, plus the University of Buckingham medical school teaching affiliation that drives unique teaching-overhead establishment cost (printing, training collateral, governance liaison). Frontline Digitisation EPR rollout adds training and change-management cost. Industrial action 2023-24 drove communications and agency-recruitment advertising. April 2025 NIC step-up (15%, £5k threshold) feeds forward via supplier-side pass-through on telecoms, courier and training contracts. The line sits alongside MKUH's distinctive business-rates hereditament-expansion dynamics within the broader Premises & Infrastructure category.",
        "sources": [
            {"publisher": "Milton Keynes University Hospital NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.mkuh.nhs.uk/about-us/our-publications/annual-reports-and-accounts/"},
            {"publisher": "National Audit Office", "title": "New Hospital Programme", "url": "https://www.nao.org.uk/reports/new-hospital-programme/"},
            {"publisher": "Department of Health and Social Care", "title": "New Hospital Programme — Plan for Implementation (Jan 2025 Reset)", "url": "https://www.gov.uk/government/publications/new-hospital-programme-plan-for-implementation"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Milton Keynes University Hospital NHS FT provider profile (RD8)", "url": "https://www.cqc.org.uk/provider/RD8"}
        ],
        "related": ["Milton Keynes University Hospital NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "New Hospital Programme", "Business rates — Milton Keynes University Hospital NHS Foundation Trust", "Frontline Digitisation Programme"]
    }
}
