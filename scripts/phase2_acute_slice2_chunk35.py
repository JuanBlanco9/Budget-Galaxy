# -*- coding: utf-8 -*-
# Phase 2 Acute slice 2 — chunk 35 (17 NHS Acute Trust orphan sub-lines)
# Hand-curated trust-specific PROGRAMME-archetype enrichment entries.
# Structural contract per docs/archetype_briefs.md.

NEW = {
    "Amortisation — North Middlesex University Hospital NHS Trust": {
        "aliases": [{"name": "Amortisation", "parent": "North Middlesex University Hospital NHS Trust"}],
        "description": "North Middlesex's £1.358M amortisation line covers the systematic write-down of intangible assets — chiefly capitalised software licences, EPR / clinical-system implementation costs, internally-developed software and information-system intangibles — across the Sterling Way, Edmonton acute site. The trust's Frontline Digitisation EPR programme (Cerner / Oracle Health-aligned with North Central London ICS partner-trust roadmap) and historic NHS Improvement Programme spend feed the amortisation profile under IAS 38.",
        "beneficiaries": "c. 3,300 WTE staff serving a c. 350,000 Enfield + Haringey + Waltham Forest catchment; c. 165,000 ED attendances/yr at North Middlesex ED — among the busiest in north London; c. 60,000 admissions/yr; trust merging into Royal Free London NHS Foundation Trust group (clinical merger announced, integration in progress) — North Central London ICS context.",
        "legal_basis": "IAS 38 Intangible Assets — DHSC Group Accounting Manual 2024-25 ch.5 — IAS 36 Impairment of Assets (interaction) — NHS Act 2006 — Health and Care Act 2022 — DHSC capital-accounting guidance",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£1.358M"},
            {"label": "Trust scale", "value": "North Middlesex Hospital (Sterling Way, Edmonton); c. 3,300 WTE; one of busiest EDs in north London"},
            {"label": "Composition", "value": "Capitalised software licences + EPR/clinical-system implementation costs + internally-developed software + IT intangibles amortised straight-line over useful economic life (3-10 yrs typical)"},
            {"label": "Frontline Digitisation EPR", "value": "EPR programme aligned with Royal Free London group / North Central London ICS — capitalised intangible feeds amortisation cycle"},
            {"label": "Useful-economic-life policy", "value": "Software and licences typically 3-5 yrs; bespoke/implementation costs 5-10 yrs per IAS 38 + DHSC GAM ch.5"},
            {"label": "Royal Free London merger", "value": "Clinical merger with Royal Free London NHS FT announced — group-wide intangible-asset register being reviewed for amortisation harmonisation"},
            {"label": "Funding trajectory", "value": "2021-22 c. £1.05M → 2023-24 c. £1.25M → 2024-25 £1.358M — Frontline Digitisation capitalisation + cumulative IT-asset stock build-up"},
            {"label": "North Central London ICS", "value": "Member of NCL ICB (Barnet, Camden, Enfield, Haringey, Islington); shared digital roadmap with RFL, UCLH, Whittington"},
            {"label": "Delivery body", "value": "Trust Finance + IT/Digital + RFL group Finance (post-merger) + Cerner / Oracle Health (EPR vendor) + capital-asset register team"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + NHSE Frontline Digitisation programme + NCL ICB"},
            {"label": "Evaluation evidence", "value": "Trust ARA 2023-24 intangible-asset note; CQC RAP inspections; NAO Digital transformation in the NHS report; NHSE Frontline Digitisation programme returns"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-EPR baseline software-amortisation profile · Successor: RFL-group integrated EPR + amortisation-policy harmonisation post-merger"}
        ],
        "notes": "North Middlesex's amortisation line reflects the trust's accumulated capitalised-intangible stock — chiefly clinical-system software, EPR implementation costs and internally-developed information assets — written down on a straight-line basis over 3-10 year useful economic lives per IAS 38 and DHSC GAM ch.5. The trust's Frontline Digitisation EPR programme and clinical-system harmonisation work with Royal Free London (clinical merger announced) drive ongoing capitalised-intangible additions feeding the amortisation cycle. North Central London ICS shared digital roadmap with RFL, UCLH and Whittington shapes the medium-term software-asset register. The April 2025 employer NIC step-up affects the underlying software-vendor and implementation-contractor cost base feeding capitalisation, with a knock-on on future amortisation profile.",
        "sources": [
            {"publisher": "North Middlesex University Hospital NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.northmid.nhs.uk/about-us/publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/frontline-digitisation/"},
            {"publisher": "Care Quality Commission", "title": "North Middlesex University Hospital NHS Trust provider profile (RAP)", "url": "https://www.cqc.org.uk/provider/RAP"},
            {"publisher": "National Audit Office", "title": "Digital transformation in the NHS", "url": "https://www.nao.org.uk/reports/digital-transformation-in-the-nhs/"}
        ],
        "related": ["North Middlesex University Hospital NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Amortisation — West Hertfordshire Hospitals NHS Trust", "Amortisation — Royal Free London NHS Foundation Trust", "NHS England"]
    },
    "Business rates — Royal Free London NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "Royal Free London NHS Foundation Trust"}],
        "description": "Royal Free London's £1.335M business-rates line covers non-domestic rate liability across the trust's three-site teaching-hospital footprint — Royal Free Hospital (Hampstead), Barnet Hospital and Chase Farm Hospital (Enfield) — plus community-clinic outposts. Rateable values are set by the VOA on the 2023 list (effective 1 April 2023) with rates calculated against the LGFA 1988 (Sch 6) standard non-domestic multiplier as amended by the Non-Domestic Rating (Multipliers and Private Finance) Act 2024. North Central London ICS context.",
        "beneficiaries": "c. 11,000 WTE staff serving a c. 1.6M North Central London catchment (Camden, Barnet, Enfield, Haringey, Islington); c. 230,000 ED attendances/yr across Royal Free + Barnet EDs; c. 175,000 admissions/yr; trust hosts the Royal Free London group (with Barnet Hospital + Chase Farm) and is the lead provider for HIV, hepatology, infectious diseases and amyloidosis nationally.",
        "legal_basis": "Local Government Finance Act 1988 (Sch 6) — Non-Domestic Rating (Multipliers and Private Finance) Act 2024 — Valuation Office Agency 2023 rating list — DHSC Group Accounting Manual 2024-25 — NHS Act 2006 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£1.335M"},
            {"label": "Trust scale", "value": "Royal Free Hospital (Hampstead) + Barnet Hospital + Chase Farm Hospital (Enfield) + community outposts; c. 11,000 WTE"},
            {"label": "Group structure", "value": "Royal Free London Group (RFL + Barnet + Chase Farm); North Middlesex clinical merger announced — group will expand to four-site footprint"},
            {"label": "Rating list", "value": "VOA 2023 list (effective 1 April 2023); next revaluation 1 April 2026"},
            {"label": "Multiplier", "value": "Standard non-domestic multiplier per LGFA 1988 Sch 6 + NDR (Multipliers and Private Finance) Act 2024 higher tier on £500k+ from April 2025"},
            {"label": "Charitable relief", "value": "NHS trusts not eligible for mandatory 80% charitable relief (cf. independent-sector charity hospitals) — full liability borne"},
            {"label": "Funding trajectory", "value": "2021-22 c. £1.15M → 2023-24 c. £1.28M → 2024-25 £1.335M — 2023 list revaluation + multiplier uplift"},
            {"label": "North Central London ICS", "value": "Member of NCL ICB; lead provider for HIV / hepatology / amyloidosis nationally"},
            {"label": "Delivery body", "value": "Trust E&F + Finance + VOA (rateable-value setter) + LB Camden / LB Barnet / LB Enfield (billing authorities)"},
            {"label": "Policy owner", "value": "MHCLG (rates policy + multiplier) + VOA (valuations) + DHSC + NHSE Provider Finance + NCL ICB"},
            {"label": "Evaluation evidence", "value": "VOA rating-list publications; Trust ARA 2023-24 disclosure; CQC RAL inspections; NAO local government finance reports"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2017 VOA rating list · Successor: 2026 VOA revaluation + RFL group expansion to include North Middlesex post-merger"}
        ],
        "notes": "Royal Free London's business-rates line reflects the three-site teaching-hospital footprint with the Royal Free Hospital (Hampstead) main hereditament being the largest single liability — well above the £500k threshold that triggers the higher multiplier under the NDR (Multipliers and Private Finance) Act 2024 from April 2025. NHS trusts are not eligible for the mandatory 80% charitable rate relief enjoyed by independent-sector charity hospitals, so the full liability is borne. The pending North Middlesex clinical merger will expand the group's rateable footprint and may trigger a fresh wave of VOA reassessments. The 1 April 2026 next revaluation is the medium-term lever to challenge valuations across all three sites — Hampstead's high-value central-London location is the key amortisation driver.",
        "sources": [
            {"publisher": "Royal Free London NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.royalfree.nhs.uk/about-us/publications/"},
            {"publisher": "Valuation Office Agency", "title": "Find a business rates valuation (rating list)", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "Department for Levelling Up, Housing and Communities", "title": "Business rates: Non-Domestic Rating Act 2023 + 2024 Multipliers Act", "url": "https://www.gov.uk/government/collections/business-rates"},
            {"publisher": "Care Quality Commission", "title": "Royal Free London NHS Foundation Trust provider profile (RAL)", "url": "https://www.cqc.org.uk/provider/RAL"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"}
        ],
        "related": ["Royal Free London NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Business rates — The Hillingdon Hospitals NHS Foundation Trust", "Business rates — King’s College Hospital NHS Foundation Trust", "Valuation Office Agency"]
    },
    "Amortisation — West Hertfordshire Hospitals NHS Trust": {
        "aliases": [{"name": "Amortisation", "parent": "West Hertfordshire Hospitals NHS Trust"}],
        "description": "West Hertfordshire's £1.326M amortisation line covers the systematic write-down of intangible assets — chiefly capitalised software licences, EPR / clinical-system implementation costs, and internally-developed software — across the trust's Watford General, Hemel Hempstead and St Albans City Hospital sites. The trust is in the New Hospital Programme cohort (Watford General rebuild) and post-January-2025 NHP Reset deferral; pre-rebuild capitalised intangibles continue to amortise on a straight-line basis under IAS 38 and DHSC GAM ch.5.",
        "beneficiaries": "c. 5,000 WTE staff serving a c. 500,000 west Hertfordshire catchment (Watford, St Albans, Hemel Hempstead, Three Rivers, Dacorum); c. 145,000 ED attendances/yr at Watford General ED; c. 75,000 admissions/yr; trust runs Watford General Hospital (acute), Hemel Hempstead Hospital (planned care + UTC) and St Albans City Hospital (elective + day-case) within the Hertfordshire and West Essex ICS.",
        "legal_basis": "IAS 38 Intangible Assets — DHSC Group Accounting Manual 2024-25 ch.5 — IAS 36 Impairment of Assets (interaction) — NHS Act 2006 — Health and Care Act 2022 — DHSC capital-accounting guidance — DHSC NHP capital framework",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£1.326M"},
            {"label": "Trust scale", "value": "Watford General + Hemel Hempstead + St Albans City Hospital; c. 5,000 WTE"},
            {"label": "NHP cohort + Reset", "value": "Watford General in original 40-hospitals NHP cohort; January 2025 NHP Reset deferred Watford rebuild — pre-rebuild intangibles continue to amortise"},
            {"label": "Composition", "value": "Capitalised software licences + EPR/clinical-system implementation + internally-developed software + IT intangibles amortised straight-line over 3-10 yr useful economic life"},
            {"label": "Frontline Digitisation EPR", "value": "EPR programme drives capitalised intangible additions feeding amortisation cycle"},
            {"label": "Useful-economic-life policy", "value": "Software and licences typically 3-5 yrs; bespoke/implementation costs 5-10 yrs per IAS 38 + DHSC GAM ch.5"},
            {"label": "Funding trajectory", "value": "2021-22 c. £1.05M → 2023-24 c. £1.22M → 2024-25 £1.326M — Frontline Digitisation capitalisation + cumulative IT-asset stock build-up"},
            {"label": "Hertfordshire and West Essex ICS", "value": "Member of HWE ICB; co-ordination with East and North Hertfordshire NHS Trust on west-Hertfordshire pathways"},
            {"label": "Delivery body", "value": "Trust Finance + IT/Digital + capital-asset register team + EPR vendor (System C / SystemC Liquidlogic) + Frontline Digitisation programme team"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + NHSE Frontline Digitisation programme + DHSC NHP team + HWE ICB"},
            {"label": "Evaluation evidence", "value": "Trust ARA 2023-24 intangible-asset note; CQC RWG inspections; NAO Digital transformation in the NHS report; NAO New Hospital Programme report"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-EPR baseline software-amortisation profile · Successor: post-NHP-rebuild new-build EPR + intangible-asset reset"}
        ],
        "notes": "West Hertfordshire's amortisation line reflects the trust's accumulated capitalised-intangible stock — chiefly EPR, clinical-system software and internally-developed information assets — written down on a straight-line basis over 3-10 year useful economic lives per IAS 38 and DHSC GAM ch.5. The trust's New Hospital Programme cohort status (Watford General rebuild) is now subject to January 2025 NHP Reset deferral — pre-rebuild capitalised intangibles continue to amortise without the planned new-build reset. The Frontline Digitisation EPR programme drives ongoing capitalised-intangible additions feeding the amortisation cycle. Hertfordshire and West Essex ICS shared digital roadmap shapes co-ordination with East and North Herts NHS Trust on west-Hertfordshire patient pathways.",
        "sources": [
            {"publisher": "West Hertfordshire Teaching Hospitals NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.westhertshospitals.nhs.uk/about-us/publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/frontline-digitisation/"},
            {"publisher": "National Audit Office", "title": "Progress with the New Hospital Programme", "url": "https://www.nao.org.uk/reports/progress-with-the-new-hospital-programme/"},
            {"publisher": "Care Quality Commission", "title": "West Hertfordshire Teaching Hospitals NHS Trust provider profile (RWG)", "url": "https://www.cqc.org.uk/provider/RWG"}
        ],
        "related": ["West Hertfordshire Hospitals NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Amortisation — North Middlesex University Hospital NHS Trust", "Amortisation — Calderdale and Huddersfield NHS Foundation Trust", "New Hospital Programme"]
    },
    "Lease expenditure — King’s College Hospital NHS Foundation Trust": {
        "aliases": [{"name": "Lease expenditure", "parent": "King’s College Hospital NHS Foundation Trust"}],
        "description": "King's College Hospital's £1.319M lease-expenditure line covers IFRS 16 short-life and low-value lease charges plus residual operating-lease costs not capitalised on the balance sheet — chiefly office accommodation, satellite outpatient clinic space, equipment leases (medical devices, MRI/CT mobile units) and pool-vehicle / fleet rentals across the Denmark Hill, Princess Royal University Hospital (Orpington) and Orpington Hospital footprint plus south-east-London community outposts. South East London ICS context.",
        "beneficiaries": "c. 14,500 WTE staff serving a c. 700,000 south-east London + Bromley + Lambeth + Southwark catchment; c. 270,000 ED attendances/yr across King's Denmark Hill ED + PRUH ED; c. 200,000 admissions/yr; trust hosts a Major Trauma Centre (Denmark Hill — south London MTC) and tertiary services for liver, neurosciences, cardiology and haematology nationally.",
        "legal_basis": "IFRS 16 Leases — DHSC Group Accounting Manual 2024-25 ch.7 — Landlord and Tenant Act 1954 — NHS Act 2006 — Health and Care Act 2022 — IAS 36 (interaction) — DHSC capital-accounting guidance",
        "key_stats": [
            {"label": "Lease expenditure 2024-25", "value": "£1.319M"},
            {"label": "Trust scale", "value": "King's College Hospital (Denmark Hill) + Princess Royal University Hospital (Orpington) + Orpington Hospital + community outposts; c. 14,500 WTE"},
            {"label": "Major Trauma Centre", "value": "Denmark Hill is south London Major Trauma Centre — drives high-spec equipment-lease profile"},
            {"label": "IFRS 16 transition", "value": "Most operating leases capitalised on balance sheet from April 2022; this line covers short-life (<12mo) + low-value + residual operating-lease costs"},
            {"label": "Composition", "value": "Office accommodation + satellite outpatient clinic space + equipment leases (MRI/CT mobile, pool medical devices) + pool-vehicle/fleet rentals"},
            {"label": "Funding trajectory", "value": "2021-22 c. £1.5M (pre-IFRS 16) → 2022-23 c. £1.1M (post-IFRS 16 reclass) → 2024-25 £1.319M — short-life lease + equipment-lease growth"},
            {"label": "South East London ICS", "value": "Member of SEL ICB; co-ordination with Guy's & St Thomas' and Lewisham + Greenwich on south-east-London pathways"},
            {"label": "Tertiary services", "value": "National lead for liver transplantation, neurosciences, cardiology and haematology — equipment-lease intensity"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + Procurement + Finance + NHS Supply Chain (medical-equipment leasing framework) + commercial landlords"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + SEL ICB + NHS Supply Chain (medical-equipment leasing)"},
            {"label": "Evaluation evidence", "value": "Trust ARA 2023-24 IFRS 16 disclosure; CQC RJZ inspections; NAO IFRS 16 implementation report; Trust quality account"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-IFRS 16 operating-lease cost profile · Successor: continued short-life + low-value lease profile + estate-rationalisation post-deficit-recovery"}
        ],
        "notes": "King's College Hospital's lease-expenditure line covers IFRS 16 short-life (<12 months) and low-value lease charges plus residual operating-lease costs that escape balance-sheet capitalisation — chiefly office accommodation, satellite outpatient clinic space, medical-equipment leases (mobile MRI/CT, pool devices) and fleet rentals across the Denmark Hill, PRUH and Orpington footprint. The trust's Major Trauma Centre status and tertiary-service lead role (liver transplantation, neurosciences, cardiology, haematology) drive a high-spec equipment-lease profile. King's has historically run a deficit and has been the subject of multiple NHSE financial-recovery interventions; estate-rationalisation and lease consolidation are part of the medium-term recovery plan. South East London ICS shared-service co-ordination with Guy's & St Thomas' and Lewisham + Greenwich shapes lease portfolio decisions.",
        "sources": [
            {"publisher": "King’s College Hospital NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.kch.nhs.uk/about-us/publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "IFRS Foundation", "title": "IFRS 16 Leases", "url": "https://www.ifrs.org/issued-standards/list-of-standards/ifrs-16-leases/"},
            {"publisher": "Care Quality Commission", "title": "King’s College Hospital NHS Foundation Trust provider profile (RJZ)", "url": "https://www.cqc.org.uk/provider/RJZ"},
            {"publisher": "National Audit Office", "title": "NHS financial sustainability", "url": "https://www.nao.org.uk/reports/nhs-financial-sustainability/"}
        ],
        "related": ["King’s College Hospital NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Lease expenditure — Royal Free London NHS Foundation Trust", "Lease expenditure — Guy's & St Thomas' NHS Foundation Trust", "Premises & Infrastructure — King’s College Hospital NHS Foundation Trust"]
    },
    "PFI / LIFT charges — Bedfordshire Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "PFI / LIFT charges", "parent": "Bedfordshire Hospitals NHS Foundation Trust"}],
        "description": "Bedfordshire Hospitals' £1.299M PFI / LIFT charges line covers residual unitary-charge components on legacy LIFT (Local Improvement Finance Trust) and small-scale PFI scheme arrangements at Luton & Dunstable and Bedford Hospital sites — chiefly community-clinic lease-back arrangements via NHS LIFT vehicles, plus residual service-concession unitary-charge tail under IFRIC 12 and IFRS 16 (post-2022). Bedfordshire, Luton and Milton Keynes ICS context; trust formed by Luton & Dunstable + Bedford merger April 2020.",
        "beneficiaries": "c. 7,500 WTE staff serving a c. 700,000 Bedfordshire + Luton catchment (Luton, Bedford, Central Bedfordshire); c. 200,000 ED attendances/yr across L&D ED + Bedford ED; c. 130,000 admissions/yr; trust runs Luton & Dunstable Hospital (acute) + Bedford Hospital (acute) post-April-2020 merger within the Bedfordshire, Luton and Milton Keynes ICS.",
        "legal_basis": "IFRIC 12 Service Concession Arrangements — IFRS 16 Leases (post-2022) — DHSC PFI guidance — DHSC Group Accounting Manual 2024-25 ch.7 — NHS Act 2006 — Health and Care Act 2022 — NHS LIFT contractual framework",
        "key_stats": [
            {"label": "PFI / LIFT charges 2024-25", "value": "£1.299M"},
            {"label": "Trust scale", "value": "Luton & Dunstable Hospital + Bedford Hospital + community outposts; c. 7,500 WTE"},
            {"label": "Merger context", "value": "Trust formed April 2020 by merger of Luton & Dunstable University Hospital NHS FT + Bedford Hospital NHS Trust"},
            {"label": "LIFT scheme exposure", "value": "Bedfordshire community-clinic LIFT vehicle lease-back arrangements feed unitary-charge tail"},
            {"label": "PFI tail", "value": "Residual small-scale PFI scheme components — full unitary charges much smaller than e.g. NBT Brunel or Royal Liverpool"},
            {"label": "IFRIC 12 + IFRS 16 treatment", "value": "Service-concession unitary charge components recognised per IFRIC 12; lease components reclassified under IFRS 16 from April 2022"},
            {"label": "Funding trajectory", "value": "2021-22 c. £1.15M → 2023-24 c. £1.27M → 2024-25 £1.299M — RPI uplift on unitary charges + IFRS 16 reclassification adjustments"},
            {"label": "BLMK ICS", "value": "Member of Bedfordshire, Luton and Milton Keynes ICB"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + Finance + Community Health Partnerships (LIFT central body) + LIFT private-sector partners + FM contractors"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + Community Health Partnerships + BLMK ICB + HM Treasury (PFI policy legacy)"},
            {"label": "Evaluation evidence", "value": "Trust ARA 2023-24 PFI/LIFT disclosure; NAO PFI and PF2 report; CQC RC9 inspections; HoC PAC PFI follow-up"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-merger separate L&D + Bedford LIFT/PFI arrangements · Successor: contract expiry + handback / refinancing within BLMK ICS estate strategy"}
        ],
        "notes": "Bedfordshire Hospitals' PFI / LIFT line is comparatively small relative to the major full-PFI Acute trusts (NBT Brunel, Royal Liverpool, MMUH SWBH) — the trust's exposure is chiefly via legacy NHS LIFT (Local Improvement Finance Trust) community-clinic lease-back arrangements rather than full hospital-scale PFI. Both Luton & Dunstable and Bedford Hospital sites have small-scale residual PFI scheme components. The April 2020 merger consolidated two pre-existing PFI/LIFT exposures into a single trust contract register. IFRS 16 reclassification from April 2022 split the unitary charge into service and lease components per IFRIC 12 and IFRS 16. The medium-term lever is contract expiry and handback within the BLMK ICS estate strategy.",
        "sources": [
            {"publisher": "Bedfordshire Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.bedfordshirehospitals.nhs.uk/about-us/publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Community Health Partnerships", "title": "NHS LIFT programme overview", "url": "https://communityhealthpartnerships.co.uk/"},
            {"publisher": "National Audit Office", "title": "PFI and PF2", "url": "https://www.nao.org.uk/reports/pfi-and-pf2/"},
            {"publisher": "Care Quality Commission", "title": "Bedfordshire Hospitals NHS Foundation Trust provider profile (RC9)", "url": "https://www.cqc.org.uk/provider/RC9"}
        ],
        "related": ["Bedfordshire Hospitals NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "PFI / LIFT charges — Torbay and South Devon NHS Foundation Trust", "PFI / LIFT charges — Salisbury NHS Foundation Trust", "Community Health Partnerships"]
    },
    "PFI / LIFT charges — Torbay and South Devon NHS Foundation Trust": {
        "aliases": [{"name": "PFI / LIFT charges", "parent": "Torbay and South Devon NHS Foundation Trust"}],
        "description": "Torbay and South Devon's £1.298M PFI / LIFT charges line covers residual unitary-charge components on legacy LIFT (Local Improvement Finance Trust) community-clinic lease-back arrangements plus small-scale PFI scheme tails at Torbay Hospital and South Devon community sites. The trust is an integrated-care organisation (acute + community), the only full ICO model in England — the LIFT exposure reflects the dispersed community-clinic estate. Devon ICS context.",
        "beneficiaries": "c. 6,400 WTE staff serving a c. 375,000 South Devon catchment (Torbay, Teignbridge, South Hams, parts of West Devon); c. 80,000 ED attendances/yr at Torbay Hospital ED; c. 65,000 admissions/yr; trust is the only fully integrated acute + community provider in England (ICO model) — runs Torbay Hospital + community-hospital network at Newton Abbot, Totnes, Brixham, Dartmouth, Paignton.",
        "legal_basis": "IFRIC 12 Service Concession Arrangements — IFRS 16 Leases (post-2022) — DHSC PFI guidance — DHSC Group Accounting Manual 2024-25 ch.7 — NHS Act 2006 — Health and Care Act 2022 — NHS LIFT contractual framework",
        "key_stats": [
            {"label": "PFI / LIFT charges 2024-25", "value": "£1.298M"},
            {"label": "Trust scale", "value": "Torbay Hospital + Newton Abbot + Totnes + Brixham + Dartmouth + Paignton community hospitals; c. 6,400 WTE"},
            {"label": "ICO model", "value": "Only fully integrated acute + community + adult-social-care trust in England — Torbay Care Trust legacy"},
            {"label": "LIFT scheme exposure", "value": "Devon community-clinic LIFT vehicle lease-back arrangements across dispersed community-hospital estate"},
            {"label": "PFI tail", "value": "Small-scale residual PFI scheme components at Torbay Hospital + community sites"},
            {"label": "IFRIC 12 + IFRS 16 treatment", "value": "Service-concession unitary charge per IFRIC 12; lease components reclassified under IFRS 16 from April 2022"},
            {"label": "Funding trajectory", "value": "2021-22 c. £1.15M → 2023-24 c. £1.27M → 2024-25 £1.298M — RPI uplift on unitary charges + IFRS 16 reclassification adjustments"},
            {"label": "Devon ICS", "value": "Member of NHS Devon ICB; co-ordination with Royal Devon University Healthcare NHS FT and University Hospitals Plymouth on Devon-wide pathways"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + Finance + Community Health Partnerships (LIFT central body) + LIFT private-sector partners + FM contractors"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + Community Health Partnerships + Devon ICB + HM Treasury (PFI policy legacy)"},
            {"label": "Evaluation evidence", "value": "Trust ARA 2023-24 PFI/LIFT disclosure; NAO PFI and PF2 report; CQC RA9 inspections; NHSE ICO model evaluation"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2015 separate Torbay Hospital + Torbay & Southern Devon Health and Care NHS Trust LIFT arrangements · Successor: contract expiry + handback / Devon ICB estate-rationalisation"}
        ],
        "notes": "Torbay and South Devon NHS FT's PFI / LIFT line reflects the trust's dispersed community-hospital estate (Newton Abbot, Totnes, Brixham, Dartmouth, Paignton) — its LIFT exposure is geographically widespread relative to peer acute-only trusts. As the only fully integrated acute + community + adult-social-care trust in England (ICO model since 2015 Torbay Hospital + Torbay & Southern Devon merger), the trust inherited LIFT contracts from both predecessor bodies. The April 2022 IFRS 16 reclassification split unitary charges into service and lease components per IFRIC 12 and IFRS 16. Devon ICS estate-rationalisation is the medium-term lever, with contract expiry and handback decisions co-ordinated with Royal Devon University Healthcare NHS FT.",
        "sources": [
            {"publisher": "Torbay and South Devon NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.torbayandsouthdevon.nhs.uk/about-us/publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Community Health Partnerships", "title": "NHS LIFT programme overview", "url": "https://communityhealthpartnerships.co.uk/"},
            {"publisher": "National Audit Office", "title": "PFI and PF2", "url": "https://www.nao.org.uk/reports/pfi-and-pf2/"},
            {"publisher": "Care Quality Commission", "title": "Torbay and South Devon NHS Foundation Trust provider profile (RA9)", "url": "https://www.cqc.org.uk/provider/RA9"}
        ],
        "related": ["Torbay and South Devon NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "PFI / LIFT charges — Bedfordshire Hospitals NHS Foundation Trust", "PFI / LIFT charges — Salisbury NHS Foundation Trust", "Community Health Partnerships"]
    },
    "Business rates — The Rotherham NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "The Rotherham NHS Foundation Trust"}],
        "description": "The Rotherham NHS FT's £1.294M business-rates line covers non-domestic rate liability on Rotherham Hospital (Moorgate Road) — the trust's single principal acute site — plus modest community-clinic outposts. Rateable values are set by the VOA on the 2023 list (effective 1 April 2023) with rates calculated against the LGFA 1988 (Sch 6) standard non-domestic multiplier as amended by the Non-Domestic Rating (Multipliers and Private Finance) Act 2024. South Yorkshire ICS context.",
        "beneficiaries": "c. 4,500 WTE staff serving a c. 265,000 Rotherham metropolitan-borough catchment; c. 100,000 ED attendances/yr at Rotherham Hospital ED; c. 60,000 admissions/yr; trust runs Rotherham Hospital (acute) plus community services across the Rotherham metropolitan footprint within the South Yorkshire ICS.",
        "legal_basis": "Local Government Finance Act 1988 (Sch 6) — Non-Domestic Rating (Multipliers and Private Finance) Act 2024 — Valuation Office Agency 2023 rating list — DHSC Group Accounting Manual 2024-25 — NHS Act 2006 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£1.294M"},
            {"label": "Trust scale", "value": "Rotherham Hospital (Moorgate Road) + community outposts; c. 4,500 WTE"},
            {"label": "Single-site acute", "value": "Rotherham Hospital is the principal hereditament — sole acute site for Rotherham metropolitan borough"},
            {"label": "Rating list", "value": "VOA 2023 list (effective 1 April 2023); next revaluation 1 April 2026"},
            {"label": "Multiplier", "value": "Standard non-domestic multiplier per LGFA 1988 Sch 6 + NDR (Multipliers and Private Finance) Act 2024 higher tier on £500k+ from April 2025"},
            {"label": "Charitable relief", "value": "NHS trusts not eligible for mandatory 80% charitable relief — full liability borne"},
            {"label": "Funding trajectory", "value": "2021-22 c. £1.13M → 2023-24 c. £1.24M → 2024-25 £1.294M — 2023 list revaluation + multiplier uplift"},
            {"label": "South Yorkshire ICS", "value": "Member of South Yorkshire ICB; co-ordination with Doncaster & Bassetlaw, Sheffield Teaching, Barnsley on South Yorkshire pathways"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + Finance + VOA (rateable-value setter) + Rotherham MBC (unitary billing authority)"},
            {"label": "Policy owner", "value": "MHCLG (rates policy + multiplier) + VOA (valuations) + DHSC + NHSE Provider Finance + South Yorkshire ICB"},
            {"label": "Evaluation evidence", "value": "VOA rating-list publications; Trust ARA 2023-24 disclosure; CQC RFR inspections; NAO local government finance reports"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2017 VOA rating list · Successor: 2026 VOA revaluation + South Yorkshire ICS estate-rationalisation"}
        ],
        "notes": "The Rotherham NHS FT's business-rates line is concentrated on the single Rotherham Hospital (Moorgate Road) hereditament — the only acute site in Rotherham metropolitan borough — with smaller liabilities on community-clinic outposts. NHS trusts are not eligible for the mandatory 80% charitable rate relief enjoyed by independent-sector charity hospitals, so the full liability is borne. The April 2025 higher-tier multiplier on £500k+ hereditaments under the NDR (Multipliers and Private Finance) Act 2024 is material for the main hospital site. The trust has been the subject of historic concerns over financial sustainability (deficit-recovery support from NHSE) and is part of the South Yorkshire ICS with co-ordination across Doncaster & Bassetlaw, Sheffield Teaching and Barnsley on regional patient pathways.",
        "sources": [
            {"publisher": "The Rotherham NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.therotherhamft.nhs.uk/about-us/publications/"},
            {"publisher": "Valuation Office Agency", "title": "Find a business rates valuation (rating list)", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "Department for Levelling Up, Housing and Communities", "title": "Business rates: Non-Domestic Rating Act 2023 + 2024 Multipliers Act", "url": "https://www.gov.uk/government/collections/business-rates"},
            {"publisher": "Care Quality Commission", "title": "The Rotherham NHS Foundation Trust provider profile (RFR)", "url": "https://www.cqc.org.uk/provider/RFR"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"}
        ],
        "related": ["The Rotherham NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Business rates — The Hillingdon Hospitals NHS Foundation Trust", "Amortisation — The Rotherham NHS Foundation Trust", "Valuation Office Agency"]
    },
    "Business rates — The Hillingdon Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "The Hillingdon Hospitals NHS Foundation Trust"}],
        "description": "The Hillingdon Hospitals' £1.291M business-rates line covers non-domestic rate liability on Hillingdon Hospital (Pield Heath Road, Uxbridge) and Mount Vernon Hospital (Northwood) — the trust's two principal sites — plus community-clinic outposts. Hillingdon Hospital is in the New Hospital Programme cohort (rebuild post-RAAC) and post-January-2025 NHP Reset. Rateable values are set by the VOA on the 2023 list (effective 1 April 2023). North West London ICS context.",
        "beneficiaries": "c. 3,500 WTE staff serving a c. 305,000 LB Hillingdon catchment plus Heathrow Airport workforce; c. 105,000 ED attendances/yr at Hillingdon Hospital ED; c. 50,000 admissions/yr; trust runs Hillingdon Hospital (acute) + Mount Vernon Hospital (planned care + cancer centre) — Mount Vernon Cancer Centre operated jointly with East and North Hertfordshire NHS Trust.",
        "legal_basis": "Local Government Finance Act 1988 (Sch 6) — Non-Domestic Rating (Multipliers and Private Finance) Act 2024 — Valuation Office Agency 2023 rating list — DHSC Group Accounting Manual 2024-25 — NHS Act 2006 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£1.291M"},
            {"label": "Trust scale", "value": "Hillingdon Hospital (Uxbridge) + Mount Vernon Hospital (Northwood) + community outposts; c. 3,500 WTE"},
            {"label": "RAAC + NHP cohort", "value": "Hillingdon Hospital in 27-trust HSSIB Sep 2023 RAAC list + original 40-hospitals NHP rebuild cohort + post-Jan 2025 NHP Reset"},
            {"label": "Rating list", "value": "VOA 2023 list (effective 1 April 2023); next revaluation 1 April 2026"},
            {"label": "Multiplier", "value": "Standard non-domestic multiplier per LGFA 1988 Sch 6 + NDR (Multipliers and Private Finance) Act 2024 higher tier on £500k+ from April 2025"},
            {"label": "Charitable relief", "value": "NHS trusts not eligible for mandatory 80% charitable relief — full liability borne"},
            {"label": "Funding trajectory", "value": "2021-22 c. £1.12M → 2023-24 c. £1.24M → 2024-25 £1.291M — 2023 list revaluation + multiplier uplift; rebuild may trigger reassessment"},
            {"label": "North West London ICS", "value": "Member of NWL ICB; co-ordination with Imperial, LNWH, CWH, Chelsea & Westminster on NWL pathways"},
            {"label": "Heathrow proximity", "value": "Trust serves Heathrow Airport workforce + travellers — high public-health-event exposure (e.g. COVID, mpox)"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + Finance + VOA + LB Hillingdon (billing authority for Hillingdon Hospital) + LB Hillingdon/Three Rivers (Mount Vernon)"},
            {"label": "Policy owner", "value": "MHCLG (rates policy + multiplier) + VOA (valuations) + DHSC + NHSE Provider Finance + DHSC NHP team + NWL ICB"},
            {"label": "Evaluation evidence", "value": "VOA rating-list publications; Trust ARA 2023-24 disclosure; CQC RAS inspections; HSSIB RAAC list; NAO NHP report"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2017 VOA rating list · Successor: 2026 VOA revaluation + post-NHP-rebuild new-build hereditament"}
        ],
        "notes": "The Hillingdon Hospitals' business-rates line covers the two-site footprint with Hillingdon Hospital (Uxbridge) being the principal liability — the site is in the 27-trust HSSIB Sep 2023 RAAC concrete-plank failure list and the original 40-hospitals NHP rebuild cohort, with January 2025 NHP Reset deferring the rebuild timeline. NHS trusts are not eligible for the mandatory 80% charitable rate relief enjoyed by independent-sector charity hospitals. Mount Vernon Hospital (Northwood) hosts the Mount Vernon Cancer Centre (operated jointly with East and North Hertfordshire NHS Trust) — a separate hereditament. Trust serves Heathrow Airport workforce and travellers — high public-health-event exposure. Post-rebuild hereditament reassessment is the medium-term lever.",
        "sources": [
            {"publisher": "The Hillingdon Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.thh.nhs.uk/about/publications.php"},
            {"publisher": "Valuation Office Agency", "title": "Find a business rates valuation (rating list)", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "Health Services Safety Investigations Body", "title": "Risks from RAAC in NHS hospital buildings", "url": "https://www.hssib.org.uk/"},
            {"publisher": "National Audit Office", "title": "Progress with the New Hospital Programme", "url": "https://www.nao.org.uk/reports/progress-with-the-new-hospital-programme/"},
            {"publisher": "Care Quality Commission", "title": "The Hillingdon Hospitals NHS Foundation Trust provider profile (RAS)", "url": "https://www.cqc.org.uk/provider/RAS"}
        ],
        "related": ["The Hillingdon Hospitals NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Business rates — Royal Free London NHS Foundation Trust", "Amortisation — The Hillingdon Hospitals NHS Foundation Trust", "New Hospital Programme"]
    },
    "PFI / LIFT charges — Salisbury NHS Foundation Trust": {
        "aliases": [{"name": "PFI / LIFT charges", "parent": "Salisbury NHS Foundation Trust"}],
        "description": "Salisbury NHS FT's £1.290M PFI / LIFT charges line covers residual unitary-charge components on legacy LIFT (Local Improvement Finance Trust) community-clinic lease-back arrangements plus small-scale PFI scheme tails at Salisbury District Hospital and Wiltshire community sites. The trust's PFI / LIFT exposure is comparatively modest — Salisbury District Hospital is not a full-PFI scheme. Bath and North East Somerset, Swindon and Wiltshire (BSW) ICS context.",
        "beneficiaries": "c. 4,500 WTE staff serving a c. 270,000 south Wiltshire + Hampshire-border catchment (Salisbury, Amesbury, Tisbury, Mere, Wilton); c. 60,000 ED attendances/yr at Salisbury DH ED; c. 50,000 admissions/yr; trust hosts the Wessex Spinal Cord Injury Centre, the Burns Service for the South West and the Genetics laboratory — small DGH with strong regional specialty footprint.",
        "legal_basis": "IFRIC 12 Service Concession Arrangements — IFRS 16 Leases (post-2022) — DHSC PFI guidance — DHSC Group Accounting Manual 2024-25 ch.7 — NHS Act 2006 — Health and Care Act 2022 — NHS LIFT contractual framework",
        "key_stats": [
            {"label": "PFI / LIFT charges 2024-25", "value": "£1.290M"},
            {"label": "Trust scale", "value": "Salisbury District Hospital + community outposts; c. 4,500 WTE"},
            {"label": "Specialty footprint", "value": "Wessex Spinal Cord Injury Centre + Burns Service for the South West + Salisbury Genetics Laboratory — regional-tertiary specialty mix at small DGH scale"},
            {"label": "LIFT scheme exposure", "value": "South Wiltshire community-clinic LIFT vehicle lease-back arrangements"},
            {"label": "PFI tail", "value": "Small-scale residual PFI scheme components — full unitary charges much smaller than e.g. NBT Brunel or Royal Liverpool"},
            {"label": "IFRIC 12 + IFRS 16 treatment", "value": "Service-concession unitary charge per IFRIC 12; lease components reclassified under IFRS 16 from April 2022"},
            {"label": "Funding trajectory", "value": "2021-22 c. £1.15M → 2023-24 c. £1.26M → 2024-25 £1.290M — RPI uplift on unitary charges + IFRS 16 reclassification adjustments"},
            {"label": "BSW ICS", "value": "Member of Bath and North East Somerset, Swindon and Wiltshire ICB; co-ordination with Royal United Hospitals Bath, Great Western Hospitals on BSW pathways"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + Finance + Community Health Partnerships (LIFT central body) + LIFT private-sector partners + FM contractors"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + Community Health Partnerships + BSW ICB + HM Treasury (PFI policy legacy)"},
            {"label": "Evaluation evidence", "value": "Trust ARA 2023-24 PFI/LIFT disclosure; NAO PFI and PF2 report; CQC RNZ inspections; NHSE specialised commissioning evaluation (spinal + burns)"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2010 separate LIFT/PFI arrangements · Successor: contract expiry + handback / BSW ICS estate-rationalisation"}
        ],
        "notes": "Salisbury NHS FT's PFI / LIFT line is comparatively modest — Salisbury District Hospital is not a full hospital-scale PFI scheme like NBT Brunel or Royal Liverpool. The exposure is chiefly via legacy NHS LIFT (Local Improvement Finance Trust) community-clinic lease-back arrangements across south Wiltshire plus residual small-scale PFI scheme components. The trust's regional specialty footprint (Wessex Spinal Cord Injury Centre, South West Burns Service, Salisbury Genetics Laboratory) shapes the underlying estate. The April 2022 IFRS 16 reclassification split unitary charges into service and lease components per IFRIC 12 and IFRS 16. BSW ICS estate-rationalisation is the medium-term lever for contract expiry and handback decisions.",
        "sources": [
            {"publisher": "Salisbury NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.salisbury.nhs.uk/about-us/publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Community Health Partnerships", "title": "NHS LIFT programme overview", "url": "https://communityhealthpartnerships.co.uk/"},
            {"publisher": "National Audit Office", "title": "PFI and PF2", "url": "https://www.nao.org.uk/reports/pfi-and-pf2/"},
            {"publisher": "Care Quality Commission", "title": "Salisbury NHS Foundation Trust provider profile (RNZ)", "url": "https://www.cqc.org.uk/provider/RNZ"}
        ],
        "related": ["Salisbury NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "PFI / LIFT charges — Bedfordshire Hospitals NHS Foundation Trust", "PFI / LIFT charges — Torbay and South Devon NHS Foundation Trust", "Community Health Partnerships"]
    },
    "Amortisation — Calderdale and Huddersfield NHS Foundation Trust": {
        "aliases": [{"name": "Amortisation", "parent": "Calderdale and Huddersfield NHS Foundation Trust"}],
        "description": "Calderdale and Huddersfield NHS FT's £1.278M amortisation line covers the systematic write-down of intangible assets — chiefly capitalised software licences, EPR / clinical-system implementation costs (Cerner-aligned with regional integrated-care record), and internally-developed software — across the Calderdale Royal Hospital (Halifax) and Huddersfield Royal Infirmary footprint. The trust's New Hospital Programme cohort status and Reset deferral shape the medium-term amortisation profile under IAS 38 and DHSC GAM ch.5.",
        "beneficiaries": "c. 6,200 WTE staff serving a c. 470,000 Calderdale + Kirklees catchment (Halifax, Huddersfield, Brighouse, Holmfirth); c. 145,000 ED attendances/yr across Calderdale Royal ED + Huddersfield Royal ED; c. 80,000 admissions/yr; trust runs Calderdale Royal Hospital (acute) + Huddersfield Royal Infirmary (acute) within the West Yorkshire ICS.",
        "legal_basis": "IAS 38 Intangible Assets — DHSC Group Accounting Manual 2024-25 ch.5 — IAS 36 Impairment of Assets (interaction) — NHS Act 2006 — Health and Care Act 2022 — DHSC capital-accounting guidance — DHSC NHP capital framework",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£1.278M"},
            {"label": "Trust scale", "value": "Calderdale Royal Hospital (Halifax) + Huddersfield Royal Infirmary; c. 6,200 WTE"},
            {"label": "NHP cohort + Reset", "value": "Trust in original 40-hospitals NHP cohort (Hospitals for Calderdale and Huddersfield reconfiguration scheme); January 2025 NHP Reset deferred timeline"},
            {"label": "Composition", "value": "Capitalised software licences + EPR/clinical-system implementation + internally-developed software + IT intangibles amortised straight-line over 3-10 yr useful economic life"},
            {"label": "Frontline Digitisation EPR", "value": "Cerner-aligned EPR with West Yorkshire integrated-care record + Yorkshire-Humberside shared-care record"},
            {"label": "Useful-economic-life policy", "value": "Software and licences typically 3-5 yrs; bespoke/implementation costs 5-10 yrs per IAS 38 + DHSC GAM ch.5"},
            {"label": "Funding trajectory", "value": "2021-22 c. £1.0M → 2023-24 c. £1.18M → 2024-25 £1.278M — Frontline Digitisation capitalisation + cumulative IT-asset stock build-up"},
            {"label": "West Yorkshire ICS", "value": "Member of West Yorkshire ICB; co-ordination with Mid Yorkshire, Bradford Teaching, Leeds Teaching, Airedale on West Yorkshire pathways"},
            {"label": "Delivery body", "value": "Trust Finance + IT/Digital + capital-asset register team + Cerner / Oracle Health (EPR vendor) + Frontline Digitisation programme team"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + NHSE Frontline Digitisation programme + DHSC NHP team + West Yorkshire ICB"},
            {"label": "Evaluation evidence", "value": "Trust ARA 2023-24 intangible-asset note; CQC RWY inspections; NAO Digital transformation in the NHS report; NAO New Hospital Programme report"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-EPR baseline software-amortisation profile · Successor: post-NHP-reconfiguration new-build EPR + intangible-asset reset"}
        ],
        "notes": "Calderdale and Huddersfield's amortisation line reflects the trust's accumulated capitalised-intangible stock — chiefly Cerner-aligned EPR, clinical-system software and internally-developed information assets — written down on a straight-line basis over 3-10 year useful economic lives per IAS 38 and DHSC GAM ch.5. The trust's New Hospital Programme cohort status (Hospitals for Calderdale and Huddersfield reconfiguration scheme — A&E + emergency consolidation at Calderdale Royal, planned-care consolidation at Huddersfield Royal) is now subject to January 2025 NHP Reset deferral. The Cerner EPR aligns with the West Yorkshire integrated-care record and the Yorkshire-Humberside shared-care record. April 2025 NIC step-up affects underlying vendor-cost base feeding capitalisation.",
        "sources": [
            {"publisher": "Calderdale and Huddersfield NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.cht.nhs.uk/about-us/publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/frontline-digitisation/"},
            {"publisher": "National Audit Office", "title": "Progress with the New Hospital Programme", "url": "https://www.nao.org.uk/reports/progress-with-the-new-hospital-programme/"},
            {"publisher": "Care Quality Commission", "title": "Calderdale and Huddersfield NHS Foundation Trust provider profile (RWY)", "url": "https://www.cqc.org.uk/provider/RWY"}
        ],
        "related": ["Calderdale and Huddersfield NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Amortisation — North Cumbria Integrated Care NHS Foundation Trust", "Amortisation — West Hertfordshire Hospitals NHS Trust", "New Hospital Programme"]
    },
    "Amortisation — North Cumbria Integrated Care NHS Foundation Trust": {
        "aliases": [{"name": "Amortisation", "parent": "North Cumbria Integrated Care NHS Foundation Trust"}],
        "description": "North Cumbria Integrated Care NHS FT's £1.272M amortisation line covers the systematic write-down of intangible assets — chiefly capitalised software licences, EPR / clinical-system implementation costs (TPP / SystemOne for community + acute integration), and internally-developed software — across the Cumberland Infirmary (Carlisle) and West Cumberland Hospital (Whitehaven) footprint plus integrated-community services. North East and North Cumbria ICS context; trust formed by acute + community integration October 2019.",
        "beneficiaries": "c. 6,800 WTE staff serving a c. 320,000 north Cumbria catchment (Carlisle, Whitehaven, Workington, Penrith, Wigton); c. 105,000 ED attendances/yr across Cumberland Infirmary ED + West Cumberland Hospital ED; c. 50,000 admissions/yr; trust is an integrated acute + community provider serving rural-remote Cumbria with significant cross-Pennine referral flow to Newcastle-upon-Tyne Hospitals NHS FT for tertiary services.",
        "legal_basis": "IAS 38 Intangible Assets — DHSC Group Accounting Manual 2024-25 ch.5 — IAS 36 Impairment of Assets (interaction) — NHS Act 2006 — Health and Care Act 2022 — DHSC capital-accounting guidance",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£1.272M"},
            {"label": "Trust scale", "value": "Cumberland Infirmary (Carlisle) + West Cumberland Hospital (Whitehaven) + community services across north Cumbria; c. 6,800 WTE"},
            {"label": "Integration date", "value": "Trust formed October 2019 by integration of North Cumbria University Hospitals NHS Trust + community services from Cumbria Partnership NHS FT"},
            {"label": "Composition", "value": "Capitalised software licences + EPR/clinical-system implementation + internally-developed software + IT intangibles amortised straight-line over 3-10 yr useful economic life"},
            {"label": "Frontline Digitisation EPR", "value": "TPP / SystemOne primary care + community alignment with acute EPR — cross-modality integrated-care record"},
            {"label": "Useful-economic-life policy", "value": "Software and licences typically 3-5 yrs; bespoke/implementation costs 5-10 yrs per IAS 38 + DHSC GAM ch.5"},
            {"label": "Funding trajectory", "value": "2021-22 c. £1.0M → 2023-24 c. £1.17M → 2024-25 £1.272M — Frontline Digitisation + integrated-care record capitalisation"},
            {"label": "NENC ICS", "value": "Member of North East and North Cumbria ICB — geographically the largest English ICS by area"},
            {"label": "Tertiary referral flow", "value": "Cross-Pennine referrals to Newcastle Hospitals (RTG) for major-trauma + cardiothoracic + neurosciences + transplantation"},
            {"label": "Delivery body", "value": "Trust Finance + IT/Digital + capital-asset register team + TPP / SystemC / Cerner (EPR vendor) + Frontline Digitisation programme team"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + NHSE Frontline Digitisation programme + NENC ICB"},
            {"label": "Evaluation evidence", "value": "Trust ARA 2023-24 intangible-asset note; CQC RNN / R1L inspections; NAO Digital transformation in the NHS report"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2019 separate North Cumbria UH + Cumbria Partnership intangible registers · Successor: continued integrated-care record build-out + cumulative amortisation"}
        ],
        "notes": "North Cumbria Integrated Care NHS FT's amortisation line reflects the trust's accumulated capitalised-intangible stock — chiefly EPR, clinical-system software and internally-developed information assets across acute + community modalities — written down on a straight-line basis over 3-10 year useful economic lives per IAS 38 and DHSC GAM ch.5. The October 2019 integration of acute + community services consolidated two pre-existing intangible-asset registers. The Frontline Digitisation EPR programme (TPP / SystemOne primary-care + community alignment with acute EPR) drives ongoing capitalised-intangible additions. NENC ICS context shapes shared-digital roadmap; cross-Pennine tertiary referrals to Newcastle Hospitals shape the underlying clinical-system integration footprint.",
        "sources": [
            {"publisher": "North Cumbria Integrated Care NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.ncic.nhs.uk/about-us/publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/frontline-digitisation/"},
            {"publisher": "National Audit Office", "title": "Digital transformation in the NHS", "url": "https://www.nao.org.uk/reports/digital-transformation-in-the-nhs/"},
            {"publisher": "Care Quality Commission", "title": "North Cumbria Integrated Care NHS Foundation Trust provider profile (RNN)", "url": "https://www.cqc.org.uk/provider/RNN"}
        ],
        "related": ["North Cumbria Integrated Care NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Amortisation — Calderdale and Huddersfield NHS Foundation Trust", "Amortisation — North Middlesex University Hospital NHS Trust", "NHS England"]
    },
    "Amortisation — The Rotherham NHS Foundation Trust": {
        "aliases": [{"name": "Amortisation", "parent": "The Rotherham NHS Foundation Trust"}],
        "description": "The Rotherham NHS FT's £1.266M amortisation line covers the systematic write-down of intangible assets — chiefly capitalised software licences, EPR / clinical-system implementation costs, and internally-developed software — at the Rotherham Hospital (Moorgate Road) site. The trust's Frontline Digitisation EPR programme (Yorkshire-Humberside shared-care record alignment) and historic NHS Improvement Programme spend feed the amortisation profile under IAS 38 and DHSC GAM ch.5. South Yorkshire ICS context.",
        "beneficiaries": "c. 4,500 WTE staff serving a c. 265,000 Rotherham metropolitan-borough catchment; c. 100,000 ED attendances/yr at Rotherham Hospital ED; c. 60,000 admissions/yr; trust runs Rotherham Hospital (acute) plus community services across the Rotherham metropolitan footprint within the South Yorkshire ICS.",
        "legal_basis": "IAS 38 Intangible Assets — DHSC Group Accounting Manual 2024-25 ch.5 — IAS 36 Impairment of Assets (interaction) — NHS Act 2006 — Health and Care Act 2022 — DHSC capital-accounting guidance",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£1.266M"},
            {"label": "Trust scale", "value": "Rotherham Hospital (Moorgate Road) + community outposts; c. 4,500 WTE"},
            {"label": "Composition", "value": "Capitalised software licences + EPR/clinical-system implementation + internally-developed software + IT intangibles amortised straight-line over 3-10 yr useful economic life"},
            {"label": "Frontline Digitisation EPR", "value": "Yorkshire-Humberside shared-care record alignment + South Yorkshire ICS digital roadmap"},
            {"label": "Useful-economic-life policy", "value": "Software and licences typically 3-5 yrs; bespoke/implementation costs 5-10 yrs per IAS 38 + DHSC GAM ch.5"},
            {"label": "Funding trajectory", "value": "2021-22 c. £1.0M → 2023-24 c. £1.17M → 2024-25 £1.266M — Frontline Digitisation capitalisation + cumulative IT-asset stock build-up"},
            {"label": "South Yorkshire ICS", "value": "Member of South Yorkshire ICB; co-ordination with Doncaster & Bassetlaw, Sheffield Teaching, Barnsley on South Yorkshire pathways"},
            {"label": "Historic context", "value": "Trust history of financial-recovery-support intervention — IT-asset capitalisation choices shaped by 'fix-the-basics' digital priorities"},
            {"label": "Delivery body", "value": "Trust Finance + IT/Digital + capital-asset register team + EPR vendor + Frontline Digitisation programme team"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + NHSE Frontline Digitisation programme + South Yorkshire ICB"},
            {"label": "Evaluation evidence", "value": "Trust ARA 2023-24 intangible-asset note; CQC RFR inspections; NAO Digital transformation in the NHS report"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-EPR baseline software-amortisation profile · Successor: continued Frontline Digitisation build-out + cumulative amortisation through 2030s"}
        ],
        "notes": "The Rotherham NHS FT's amortisation line reflects the trust's accumulated capitalised-intangible stock — chiefly EPR, clinical-system software and internally-developed information assets at the single Rotherham Hospital site — written down on a straight-line basis over 3-10 year useful economic lives per IAS 38 and DHSC GAM ch.5. The trust has a history of financial-recovery-support intervention from NHSE which has shaped IT-asset capitalisation choices, with 'fix-the-basics' digital priorities (PAS, EPR clinical-system foundations) feeding the intangible register. Yorkshire-Humberside shared-care record alignment and South Yorkshire ICS digital roadmap shape the medium-term software-asset trajectory. April 2025 NIC step-up affects underlying vendor-cost base feeding capitalisation.",
        "sources": [
            {"publisher": "The Rotherham NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.therotherhamft.nhs.uk/about-us/publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/frontline-digitisation/"},
            {"publisher": "National Audit Office", "title": "Digital transformation in the NHS", "url": "https://www.nao.org.uk/reports/digital-transformation-in-the-nhs/"},
            {"publisher": "Care Quality Commission", "title": "The Rotherham NHS Foundation Trust provider profile (RFR)", "url": "https://www.cqc.org.uk/provider/RFR"}
        ],
        "related": ["The Rotherham NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Business rates — The Rotherham NHS Foundation Trust", "Amortisation — The Hillingdon Hospitals NHS Foundation Trust", "Amortisation — Calderdale and Huddersfield NHS Foundation Trust"]
    },
    "Amortisation — The Hillingdon Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Amortisation", "parent": "The Hillingdon Hospitals NHS Foundation Trust"}],
        "description": "The Hillingdon Hospitals' £1.248M amortisation line covers the systematic write-down of intangible assets — chiefly capitalised software licences, EPR / clinical-system implementation costs, and internally-developed software — across the Hillingdon Hospital (Uxbridge) and Mount Vernon Hospital (Northwood) footprint. The trust's New Hospital Programme cohort status (Hillingdon Hospital RAAC rebuild) and post-January-2025 NHP Reset deferral shape the medium-term amortisation profile under IAS 38 and DHSC GAM ch.5. North West London ICS context.",
        "beneficiaries": "c. 3,500 WTE staff serving a c. 305,000 LB Hillingdon catchment plus Heathrow Airport workforce; c. 105,000 ED attendances/yr at Hillingdon Hospital ED; c. 50,000 admissions/yr; trust runs Hillingdon Hospital (acute, RAAC rebuild cohort) + Mount Vernon Hospital (planned care + cancer centre operated jointly with East and North Hertfordshire NHS Trust).",
        "legal_basis": "IAS 38 Intangible Assets — DHSC Group Accounting Manual 2024-25 ch.5 — IAS 36 Impairment of Assets (interaction) — NHS Act 2006 — Health and Care Act 2022 — DHSC capital-accounting guidance — DHSC NHP capital framework",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£1.248M"},
            {"label": "Trust scale", "value": "Hillingdon Hospital (Uxbridge) + Mount Vernon Hospital (Northwood); c. 3,500 WTE"},
            {"label": "RAAC + NHP cohort", "value": "Hillingdon Hospital in 27-trust HSSIB Sep 2023 RAAC list + original 40-hospitals NHP rebuild cohort + Jan 2025 NHP Reset"},
            {"label": "Composition", "value": "Capitalised software licences + EPR/clinical-system implementation + internally-developed software + IT intangibles amortised straight-line over 3-10 yr useful economic life"},
            {"label": "Frontline Digitisation EPR", "value": "EPR programme aligned with NWL ICS shared-digital roadmap (Imperial / LNWH / CWH peer alignment)"},
            {"label": "Useful-economic-life policy", "value": "Software and licences typically 3-5 yrs; bespoke/implementation costs 5-10 yrs per IAS 38 + DHSC GAM ch.5"},
            {"label": "Funding trajectory", "value": "2021-22 c. £1.0M → 2023-24 c. £1.15M → 2024-25 £1.248M — Frontline Digitisation capitalisation + RAAC-rebuild planning intangibles"},
            {"label": "North West London ICS", "value": "Member of NWL ICB; co-ordination with Imperial College Healthcare, LNWH, CWH, Chelsea & Westminster on NWL pathways"},
            {"label": "Heathrow proximity", "value": "Trust serves Heathrow Airport workforce + travellers — high public-health-event exposure"},
            {"label": "Delivery body", "value": "Trust Finance + IT/Digital + capital-asset register team + EPR vendor + Frontline Digitisation programme team"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + NHSE Frontline Digitisation programme + DHSC NHP team + NWL ICB"},
            {"label": "Evaluation evidence", "value": "Trust ARA 2023-24 intangible-asset note; CQC RAS inspections; HSSIB RAAC list; NAO NHP report"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-EPR baseline software-amortisation profile · Successor: post-NHP-rebuild new-build EPR + intangible-asset reset"}
        ],
        "notes": "The Hillingdon Hospitals' amortisation line reflects the trust's accumulated capitalised-intangible stock — chiefly EPR, clinical-system software and internally-developed information assets across the Hillingdon Hospital (Uxbridge) and Mount Vernon Hospital (Northwood) footprint — written down on a straight-line basis over 3-10 year useful economic lives per IAS 38 and DHSC GAM ch.5. The trust's NHP cohort status (Hillingdon Hospital is in the 27-trust HSSIB Sep 2023 RAAC list and the original 40-hospitals NHP rebuild cohort) is now subject to January 2025 NHP Reset deferral — pre-rebuild capitalised intangibles continue to amortise. NWL ICS shared-digital roadmap with Imperial, LNWH and CWH shapes the medium-term software-asset trajectory. Mount Vernon Cancer Centre (joint with East and North Hertfordshire) feeds a separate intangible-asset stream.",
        "sources": [
            {"publisher": "The Hillingdon Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.thh.nhs.uk/about/publications.php"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/frontline-digitisation/"},
            {"publisher": "Health Services Safety Investigations Body", "title": "Risks from RAAC in NHS hospital buildings", "url": "https://www.hssib.org.uk/"},
            {"publisher": "Care Quality Commission", "title": "The Hillingdon Hospitals NHS Foundation Trust provider profile (RAS)", "url": "https://www.cqc.org.uk/provider/RAS"}
        ],
        "related": ["The Hillingdon Hospitals NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Business rates — The Hillingdon Hospitals NHS Foundation Trust", "Amortisation — The Rotherham NHS Foundation Trust", "New Hospital Programme"]
    },
    "Establishment costs — Airedale NHS Foundation Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "Airedale NHS Foundation Trust"}],
        "description": "Airedale NHS FT's £1.244M establishment costs line covers GAM operating expenses outside the payroll chain — chiefly office consumables, postage, telephony, training and conferences, recruitment advertising, subscriptions, books and publications, courier services and minor furniture / equipment below the capitalisation threshold across Airedale General Hospital (Steeton, near Keighley). The trust is in the original 40-hospitals New Hospital Programme cohort due to Reinforced Autoclaved Aerated Concrete (RAAC) issues; rebuild planning + Frontline Digitisation feed establishment costs.",
        "beneficiaries": "c. 3,200 WTE staff serving a c. 200,000 west Yorkshire (Bradford district) + east Lancashire + North Yorkshire Dales catchment; c. 65,000 ED attendances/yr at Airedale General Hospital ED; c. 50,000 admissions/yr; trust runs Airedale General Hospital plus a national Digital Care Hub (telemedicine) supporting care homes and community services across multiple regions.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 — IAS 1 Presentation of Financial Statements — IAS 16 Property Plant and Equipment (capitalisation threshold) — NHS Act 2006 — Health and Care Act 2022 — HMRC training and subsistence rules",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£1.244M"},
            {"label": "Trust scale", "value": "Airedale General Hospital (Steeton, near Keighley) + Digital Care Hub; c. 3,200 WTE"},
            {"label": "RAAC + NHP cohort", "value": "Airedale General Hospital in 27-trust HSSIB Sep 2023 RAAC list + original 40-hospitals NHP rebuild cohort + Jan 2025 NHP Reset (Airedale was prioritised in Reset for earliest delivery)"},
            {"label": "Digital Care Hub", "value": "National telemedicine hub supporting care homes + community services across multiple regions — high training-cost intensity"},
            {"label": "Composition", "value": "Office consumables + postage + telephony + training & conferences + recruitment advertising + subscriptions + books/publications + minor furniture/equipment below cap threshold"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove cancellation rebooking + admin backfill + recruitment advertising spike"},
            {"label": "Frontline Digitisation EPR", "value": "EPR change-management training, conference and travel costs feed forward into Establishment line"},
            {"label": "Funding trajectory", "value": "2021-22 c. £0.95M → 2023-24 c. £1.15M → 2024-25 £1.244M — strike backfill + EPR training + RAAC-rebuild planning + Digital Care Hub training"},
            {"label": "West Yorkshire ICS", "value": "Member of West Yorkshire ICB; collaborative procurement, training and recruitment frameworks across WY"},
            {"label": "Delivery body", "value": "Trust Workforce + Procurement + Training & Development + Communications + IT + Finance + Digital Care Hub team"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + West Yorkshire ICB + DHSC + DHSC NHP team + NHS Supply Chain (where used)"},
            {"label": "Evaluation evidence", "value": "Trust ARA 2023-24; CQC RCF inspections; HSSIB RAAC list; NAO NHP report; Carter Lord review legacy"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-Digital-Care-Hub baseline establishment-cost profile · Successor: post-NHP-rebuild new-build induction-cost spike + Digital Care Hub continued growth"}
        ],
        "notes": "Airedale NHS FT's establishment-cost line is shaped by the convergence of three drivers — 2023-24 industrial-action backfill, Frontline Digitisation EPR change-management training, and the Airedale General Hospital RAAC-rebuild planning workload. The trust is in the 27-trust HSSIB Sep 2023 RAAC concrete-plank failure list and the original 40-hospitals NHP rebuild cohort; the January 2025 NHP Reset prioritised Airedale for earliest delivery given the safety-critical RAAC failure mode. The trust also runs a national Digital Care Hub (telemedicine for care homes + community), which drives high training, conference and travel-cost intensity. April 2025 employer NIC step-up feeds indirectly via training-provider and recruitment-advertising contractor pass-through.",
        "sources": [
            {"publisher": "Airedale NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.airedale-trust.nhs.uk/about-us/publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Health Services Safety Investigations Body", "title": "Risks from RAAC in NHS hospital buildings", "url": "https://www.hssib.org.uk/"},
            {"publisher": "National Audit Office", "title": "Progress with the New Hospital Programme", "url": "https://www.nao.org.uk/reports/progress-with-the-new-hospital-programme/"},
            {"publisher": "Care Quality Commission", "title": "Airedale NHS Foundation Trust provider profile (RCF)", "url": "https://www.cqc.org.uk/provider/RCF"}
        ],
        "related": ["Airedale NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Establishment costs — Stockport NHS Foundation Trust", "Establishment costs — Calderdale and Huddersfield NHS Foundation Trust", "New Hospital Programme"]
    },
    "Inventories written down — Guy's & St Thomas' NHS Foundation Trust": {
        "aliases": [{"name": "Inventories written down", "parent": "Guy's & St Thomas' NHS Foundation Trust"}],
        "description": "Guy's & St Thomas' £1.236M inventories-written-down line covers IAS 2 net-realisable-value adjustments and obsolescence write-offs on clinical-supplies, drug, surgical-implant, prosthesis and consumable stockholdings across Guy's Hospital, St Thomas' Hospital, Royal Brompton and Harefield Hospitals (post-2021 merger) and Evelina London Children's Hospital. The trust's tertiary-services scale, cardiothoracic specialty and paediatric-surgery profile drive a high-value implant + bespoke-prosthesis inventory at risk of write-down.",
        "beneficiaries": "c. 22,000 WTE staff serving a c. 1.1M Lambeth + Southwark + national-tertiary catchment; c. 350,000 ED attendances/yr at St Thomas' ED + Evelina ED; c. 280,000 admissions/yr; trust hosts the largest cardiac centre in Europe (Royal Brompton + Harefield), Evelina London Children's Hospital, the south-east London cancer service and the Lambeth + Southwark + Lewisham community services footprint.",
        "legal_basis": "IAS 2 Inventories — DHSC Group Accounting Manual 2024-25 — IAS 36 Impairment of Assets (interaction) — NHS Act 2006 — Health and Care Act 2022 — DHSC capital-accounting guidance — MHRA medicinal-product expiry rules",
        "key_stats": [
            {"label": "Inventories written down 2024-25", "value": "£1.236M"},
            {"label": "Trust scale", "value": "Guy's Hospital + St Thomas' Hospital + Royal Brompton + Harefield Hospitals + Evelina London Children's Hospital + community services; c. 22,000 WTE"},
            {"label": "Royal Brompton + Harefield merger", "value": "Joined GSTT February 2021 — added Europe's largest cardiac + cardiothoracic specialty stockholding (heart-valve implants, ECMO consumables, transplant supplies)"},
            {"label": "Composition", "value": "IAS 2 net-realisable-value adjustments + obsolescence write-offs on clinical supplies + drugs + surgical implants + prostheses + consumables"},
            {"label": "Drivers of write-down", "value": "Drug expiry + medical-device end-of-life + implant-product recall (e.g. cardiac-valve recalls) + bespoke-prosthesis cancellation + COVID PPE legacy stock"},
            {"label": "Tertiary specialty intensity", "value": "Cardiothoracic + paediatric-cardiac + transplant + complex-cancer drives high-value implant inventory"},
            {"label": "Funding trajectory", "value": "2021-22 c. £0.95M → 2023-24 c. £1.15M → 2024-25 £1.236M — RB+H merger expanded inventory base; COVID PPE legacy write-down tail"},
            {"label": "South East London ICS", "value": "Member of SEL ICB; lead provider for SEL acute services + national tertiary specialties"},
            {"label": "Delivery body", "value": "Trust Pharmacy + Procurement + Theatres + Cardiothoracic + Paediatric Surgery + Finance + NHS Supply Chain + DHL (logistics partner)"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + NHS Supply Chain + MHRA (medicinal-product regulation) + SEL ICB"},
            {"label": "Evaluation evidence", "value": "Trust ARA 2023-24 inventory note; CQC RJ1 inspections; NAO NHS Supply Chain report; HoC PAC PPE write-down report"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2021 separate GSTT + Royal Brompton + Harefield inventory registers · Successor: post-merger consolidated inventory + Carter / Model Hospital benchmarking"}
        ],
        "notes": "Guy's & St Thomas' inventories-written-down line reflects the trust's exceptional scale and tertiary-specialty intensity following the February 2021 merger with Royal Brompton + Harefield Hospitals — adding Europe's largest cardiac + cardiothoracic specialty stockholding (heart-valve implants, ECMO consumables, transplant supplies) on top of the existing GSTT + Evelina London paediatric-cardiac, transplant and complex-cancer inventory. Drivers of write-down include drug expiry, medical-device end-of-life, implant-product recall, bespoke-prosthesis cancellation and the residual COVID PPE legacy stock tail. Carter Lord review legacy and Model Hospital benchmarking shape the procurement-and-stock-management framework. April 2025 NIC step-up affects underlying logistics and pharmacy-services contractor cost base.",
        "sources": [
            {"publisher": "Guy's and St Thomas' NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.guysandstthomas.nhs.uk/about-us/our-publications"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS Supply Chain", "title": "About NHS Supply Chain", "url": "https://www.supplychain.nhs.uk/about/"},
            {"publisher": "National Audit Office", "title": "The supply of personal protective equipment during the COVID-19 pandemic", "url": "https://www.nao.org.uk/reports/the-supply-of-personal-protective-equipment-ppe-during-the-covid-19-pandemic/"},
            {"publisher": "Care Quality Commission", "title": "Guy's and St Thomas' NHS Foundation Trust provider profile (RJ1)", "url": "https://www.cqc.org.uk/provider/RJ1"}
        ],
        "related": ["Guy's & St Thomas' NHS Foundation Trust", "Clinical Supplies & Drugs", "NHS Acute Trusts", "General supplies & services — Guy's & St Thomas' NHS Foundation Trust", "Inventories written down — King’s College Hospital NHS Foundation Trust", "NHS Supply Chain"]
    },
    "General supplies & services — Dartford and Gravesham NHS Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "Dartford and Gravesham NHS Trust"}],
        "description": "Dartford and Gravesham NHS Trust's £1.217M general-supplies-and-services line covers GAM operating expenses on non-clinical supplies — chiefly stationery, household goods, laundry consumables, catering supplies, hardware, ironmongery, gardening and cleaning materials — across Darent Valley Hospital (Dartford) and Erith + Gravesham + Queen Mary's Sidcup community outposts. The Darent Valley Hospital site is a long-running PFI scheme (Carillion-novated to Equans) — interaction with the FM-bundled supply contract shapes the cost profile. Kent and Medway ICS context.",
        "beneficiaries": "c. 3,400 WTE staff serving a c. 500,000 north-Kent + south-east-London-border catchment (Dartford, Gravesham, Bexley, Swanley); c. 110,000 ED attendances/yr at Darent Valley Hospital ED; c. 65,000 admissions/yr; trust runs Darent Valley Hospital plus Erith + Queen Mary's Sidcup community outposts within the Kent and Medway ICS.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 — IAS 2 Inventories (interaction) — NHS Act 2006 — Health and Care Act 2022 — Public Contracts Regulations 2015 — Procurement Act 2023 (transition)",
        "key_stats": [
            {"label": "General supplies & services 2024-25", "value": "£1.217M"},
            {"label": "Trust scale", "value": "Darent Valley Hospital (Dartford) + Erith + Queen Mary's Sidcup outposts; c. 3,400 WTE"},
            {"label": "PFI context", "value": "Darent Valley Hospital is a full-PFI scheme (Carillion-novated to Equans) — FM-bundled supply contract shapes general-supplies cost profile"},
            {"label": "Composition", "value": "Stationery + household goods + laundry consumables + catering supplies + hardware + ironmongery + gardening + cleaning materials"},
            {"label": "Carillion 2018 collapse + Equans novation", "value": "FM contract novated to Equans (ex-Engie) following Carillion 2018 collapse; ongoing dispute over FM service quality"},
            {"label": "Funding trajectory", "value": "2021-22 c. £0.95M → 2023-24 c. £1.15M → 2024-25 £1.217M — CPI on consumables + Carillion-Equans transition residual costs"},
            {"label": "Kent and Medway ICS", "value": "Member of Kent and Medway ICB; co-ordination with Medway, EKHUFT, Maidstone and Tunbridge Wells on Kent pathways"},
            {"label": "NHS Supply Chain integration", "value": "Trust uses NHS Supply Chain Tower 1 (food/catering) + Tower 6 (general supplies) for non-FM-bundled items"},
            {"label": "Delivery body", "value": "Trust Procurement + Estates & Facilities + Equans (PFI FM contractor) + NHS Supply Chain + DHL (logistics) + Finance"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + NHS Supply Chain + Cabinet Office (procurement policy) + Kent and Medway ICB"},
            {"label": "Evaluation evidence", "value": "Trust ARA 2023-24; CQC RN7 inspections; NAO NHS Supply Chain report; NAO PFI and PF2 report; Carter Lord review legacy"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-Carillion-collapse 2018 supply-contract baseline · Successor: PFI contract expiry + handback (Darent Valley PFI ends c. 2031) + estate strategy"}
        ],
        "notes": "Dartford and Gravesham NHS Trust's general-supplies-and-services line is shaped by the unusual interaction with the Darent Valley Hospital PFI scheme — the trust's FM-bundled supply contract (Carillion-novated to Equans following the 2018 Carillion collapse) covers part of the general-supplies envelope, with NHS Supply Chain Tower 1 and Tower 6 covering the residual non-FM-bundled spend. Carillion 2018 collapse and the subsequent Equans (ex-Engie) novation drove ongoing service-quality disputes feeding the residual cost tail. Kent and Medway ICS shared procurement framework shapes co-ordination with peer trusts (Medway, EKHUFT, MTW). The Darent Valley PFI contract expires c. 2031 — handback planning is the medium-term lever for the trust to consolidate supply contracts.",
        "sources": [
            {"publisher": "Dartford and Gravesham NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.dgt.nhs.uk/about-us/publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS Supply Chain", "title": "About NHS Supply Chain", "url": "https://www.supplychain.nhs.uk/about/"},
            {"publisher": "National Audit Office", "title": "PFI and PF2", "url": "https://www.nao.org.uk/reports/pfi-and-pf2/"},
            {"publisher": "Care Quality Commission", "title": "Dartford and Gravesham NHS Trust provider profile (RN7)", "url": "https://www.cqc.org.uk/provider/RN7"}
        ],
        "related": ["Dartford and Gravesham NHS Trust", "Clinical Supplies & Drugs", "NHS Acute Trusts", "PFI / LIFT charges — Dartford and Gravesham NHS Trust", "General supplies & services — Wirral University Teaching Hospital NHS Foundation Trust", "NHS Supply Chain"]
    },
    "Transport (business + patient) — Wirral University Teaching Hospital NHS Foundation Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "Wirral University Teaching Hospital NHS Foundation Trust"}],
        "description": "WUTH's £1.199M transport (business + patient) line covers AfC Section 17 staff mileage, AMAP-rate business-mileage reimbursement, pool-fleet costs (IFRS 16 capitalised + low-value lease), patient-transport-services reimbursement (eligibility-tested non-emergency transfer), inter-site courier and specimen-transport services across Arrowe Park Hospital (Upton, Wirral) and Clatterbridge Hospital site. The Mersey Tunnel toll, Wirral peninsula geography and cross-Mersey patient flow to Liverpool tertiary services shape the transport-cost profile. Cheshire and Merseyside ICS context.",
        "beneficiaries": "c. 5,500 WTE staff serving a c. 320,000 Wirral peninsula catchment (Birkenhead, Wallasey, Heswall, West Kirby, Hoylake); c. 110,000 ED attendances/yr at Arrowe Park Hospital ED; c. 65,000 admissions/yr; trust runs Arrowe Park Hospital (acute) + Clatterbridge Hospital site (planned care; cancer services delivered by The Clatterbridge Cancer Centre NHS FT — separate trust co-located).",
        "legal_basis": "NHS Act 2006 — NHSE Patient Transport Services (PTS) Eligibility Criteria — AfC Section 17 (staff travel + subsistence) — HMRC AMAP rates — IFRS 16 Leases (pool fleet) — DHSC Group Accounting Manual 2024-25",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£1.199M"},
            {"label": "Trust scale", "value": "Arrowe Park Hospital (Upton, Wirral) + Clatterbridge Hospital site; c. 5,500 WTE"},
            {"label": "Peninsula geography", "value": "Wirral peninsula bounded by River Mersey + River Dee; cross-Mersey tunnel-toll patient flow to Liverpool tertiary services"},
            {"label": "Composition", "value": "AfC Section 17 staff mileage + AMAP business-mileage + pool-fleet (IFRS 16) + Patient Transport Services + courier + specimen transport"},
            {"label": "PTS eligibility", "value": "Per NHSE Patient Transport Services Eligibility Criteria — non-emergency reimbursable transport for clinically eligible patients"},
            {"label": "AMAP rate", "value": "HMRC 45p/mile first 10,000 miles + 25p/mile beyond — unchanged 2011→2024-25"},
            {"label": "Industrial action 2023-24 effect", "value": "Junior-doctor + consultant strikes drove cancellation rebooking + patient-transport rerouting + locum-travel reimbursement spike"},
            {"label": "Funding trajectory", "value": "2021-22 c. £0.95M → 2023-24 c. £1.13M → 2024-25 £1.199M — fuel-cost spike + IFRS 16 reclassification + strike rerouting"},
            {"label": "Cheshire and Merseyside ICS", "value": "Member of C&M ICB; cross-trust patient flow to Liverpool University Hospitals NHS FT (tertiary), The Clatterbridge Cancer Centre NHS FT (cancer)"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + Procurement + NWAS (NEPTS contractor) + commercial PTS contractors + Finance + Wirral Council (Mersey Tunnel toll)"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + NHSE PTS team + C&M ICB + HMRC (AMAP rates)"},
            {"label": "Evaluation evidence", "value": "Trust ARA 2023-24 transport disclosure; CQC RBL inspections; NAO PTS report; NHSE PTS service review"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2018 separate Wirral Community Trust transport arrangements · Successor: C&M ICS shared transport framework + post-strike normalisation"}
        ],
        "notes": "WUTH's transport line reflects the trust's twin-site footprint (Arrowe Park + Clatterbridge Hospital site) and the unique Wirral peninsula geography — bounded by the River Mersey and River Dee, with cross-Mersey-tunnel patient flow to Liverpool tertiary services driving a high inter-trust transfer profile. The Clatterbridge Hospital site hosts The Clatterbridge Cancer Centre NHS FT (a separate trust) — co-location requires inter-trust patient and specimen transport. The 2023-24 industrial action cycle (44 days junior-doctor + 10 days consultant strikes) drove cancellation rebooking, patient-transport rerouting and locum-travel reimbursement spikes feeding the AfC Section 17 line. Fuel-cost spike and IFRS 16 pool-fleet reclassification from April 2022 also shape the trajectory. C&M ICS shared transport framework with LUH NHS FT and The Clatterbridge Cancer Centre is the medium-term lever.",
        "sources": [
            {"publisher": "Wirral University Teaching Hospital NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.wuth.nhs.uk/about-us/publications/"},
            {"publisher": "NHS England", "title": "Non-Emergency Patient Transport Services (NEPTS) eligibility framework", "url": "https://www.england.nhs.uk/publication/non-emergency-patient-transport-services/"},
            {"publisher": "HMRC", "title": "Approved Mileage Allowance Payments (AMAP) rates", "url": "https://www.gov.uk/government/publications/rates-and-allowances-travel-mileage-and-fuel-allowances"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Wirral University Teaching Hospital NHS Foundation Trust provider profile (RBL)", "url": "https://www.cqc.org.uk/provider/RBL"}
        ],
        "related": ["Wirral University Teaching Hospital NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Transport (business + patient) — North Cumbria Integrated Care NHS Foundation Trust", "Transport (business + patient) — Calderdale and Huddersfield NHS Foundation Trust", "Lease expenditure — Wirral University Teaching Hospital NHS Foundation Trust"]
    },
}
