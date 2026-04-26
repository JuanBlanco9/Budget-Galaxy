# -*- coding: utf-8 -*-
# Phase 2 MH slice 2 — chunk 10 (17 NHS Mental Health Trust orphan sub-lines)
# Hand-curated trust-specific PROGRAMME-archetype enrichment entries.
# Structural contract per docs/archetype_briefs.md.

NEW = {
    "Amortisation — Derbyshire Healthcare NHS Foundation Trust": {
        "aliases": [{"name": "Amortisation", "parent": "Derbyshire Healthcare NHS Foundation Trust"}],
        "description": "Derbyshire Healthcare's £0.74M amortisation line is the IAS 38 charge on capitalised intangibles — chiefly software licences, EPR build-out under NHS England's Frontline Digitisation programme, capitalised configuration of clinical systems and small training-asset balances. The trust's EPR migration to TPP SystmOne (community + MH integrated record) and incremental modules added across CAMHS and crisis pathways are the principal asset cohorts driving the amortisation charge over a typical 5-7 year useful-economic-life profile.",
        "beneficiaries": "c. 2,800 staff serving a registered catchment c. 1.05M across Derby city and Derbyshire (including rural Peak District and High Peak); EPR-rolled-out clinical user base spans inpatient MH wards, community-MH teams, CAMHS, crisis services and learning-disability community bases — c. 2,000 active clinical users.",
        "legal_basis": "IAS 38 Intangible Assets · DHSC Group Accounting Manual 2024-25 ch.5 · NHS Act 2006 · Health and Care Act 2022 · NHSE Frontline Digitisation programme governance · HM Treasury FReM (capitalisation thresholds)",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£0.74M"},
            {"label": "Asset composition", "value": "Software licences (TPP SystmOne configuration + ancillary clinical systems) + capitalised EPR build + capitalised configuration + minor capitalised training balances"},
            {"label": "Useful economic life applied", "value": "Software 5-7 years per DHSC GAM 2024-25 ch.5 — straight-line amortisation"},
            {"label": "Frontline Digitisation context", "value": "NHSE Frontline Digitisation programme funds EPR upgrades + 'core capabilities' (e-prescribing, e-observations) — capitalised under IAS 38, amortised over UEL"},
            {"label": "Clinical user base", "value": "c. 2,000 active clinical users across MH inpatient + community + CAMHS + crisis + LD pathways"},
            {"label": "EPR vendor", "value": "TPP SystmOne (community + MH integrated record) — common Derbyshire-wide platform with primary care + community physical-health"},
            {"label": "Capitalisation threshold", "value": "£5,000 individual / £25,000 pooled per DHSC GAM 2024-25 (FReM-aligned)"},
            {"label": "Funding trajectory", "value": "2020-21 c. £0.4M → 2022-23 c. £0.55M → 2024-25 £0.74M — uplift driven by FD-funded EPR module additions"},
            {"label": "Delivery body", "value": "Trust Digital + Finance teams + NHSE Frontline Digitisation programme office + TPP (vendor)"},
            {"label": "Policy owner", "value": "DHSC + NHSE Transformation Directorate (digital) + Derby & Derbyshire ICB"},
            {"label": "Evaluation evidence", "value": "NHSE Frontline Digitisation milestone reporting; trust ARA digital disclosure 2023-24; What Good Looks Like (WGLL) framework benchmarking"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-FD legacy paper + standalone systems · Successor: FD core-capabilities completion + Federated Data Platform interoperability"}
        ],
        "notes": "Derbyshire Healthcare's amortisation line has grown materially since 2022 as the trust drew down NHS England Frontline Digitisation funding to extend TPP SystmOne EPR — the same platform used by Derbyshire primary care and community physical-health partners — adding e-prescribing, e-observations and patient-portal modules that capitalise under IAS 38 and unwind through this line. Useful-economic-life of 5-7 years for software per DHSC GAM ch.5 means recent FD-funded build will continue feeding amortisation through the late 2020s. Common-platform alignment with Derbyshire primary care is a strategic strength under the Derby & Derbyshire ICS. Federated Data Platform interoperability is the next driver.",
        "sources": [
            {"publisher": "Derbyshire Healthcare NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.derbyshirehealthcareft.nhs.uk/about-us/corporate-information/our-publications"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/connecting-health-and-care-providers/frontline-digitisation/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 5 — Intangible assets)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "TPP", "title": "SystmOne mental health module", "url": "https://www.tpp-uk.com/products/systmone"},
            {"publisher": "Care Quality Commission", "title": "Derbyshire Healthcare provider profile (RXM)", "url": "https://www.cqc.org.uk/provider/RXM"}
        ],
        "related": ["Derbyshire Healthcare NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "NHS England", "Amortisation — Oxford Health NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Lease expenditure — Avon and Wiltshire Mental Health Partnership NHS Trust": {
        "aliases": [{"name": "Lease expenditure", "parent": "Avon and Wiltshire Mental Health Partnership NHS Trust"}],
        "description": "AWP's £0.73M lease line reflects IFRS 16 right-of-use depreciation + interest on the trust's leased estate following the 2022 on-balance-sheet transition. The portfolio is dominated by NHS Property Services-leased community-MH and CAMHS premises across Bristol, North Somerset, South Gloucestershire, Bath & North East Somerset, Swindon and Wiltshire, plus minor private landlord and Community Health Partnerships LIFT components. The wide West-Country geography sustains a high site count for a mid-sized trust.",
        "beneficiaries": "c. 4,500 staff serving c. 1.8M residents across Bristol, North Somerset, South Gloucestershire, B&NES, Swindon and Wiltshire; leased-estate component includes c. 40+ community-MH, CAMHS, IAPT and recovery bases plus minor inpatient ancillary leased space.",
        "legal_basis": "IFRS 16 Leases · DHSC Group Accounting Manual 2024-25 ch.7 · Landlord and Tenant Act 1954 · NHS Act 2006 · Health and Care Act 2022 · Property Services Act (NHSPS founding 2013)",
        "key_stats": [
            {"label": "Lease expenditure 2024-25", "value": "£0.73M"},
            {"label": "IFRS 16 transition jump", "value": "2022 on-balance-sheet adoption — operating leases reclassified to ROU asset + lease liability with depreciation + interest split"},
            {"label": "Leased site count", "value": "c. 40+ community premises across BNSSG + B&NES + Swindon + Wiltshire ICS footprints"},
            {"label": "Major lessor", "value": "NHS Property Services Ltd (majority) + private landlords + Community Health Partnerships (minor LIFT exposure)"},
            {"label": "NHSPS rates dispute", "value": "Sustained NHSPS / MH-trust dispute on community-clinic market-rent uplift + service-charge methodology — feeds annual line volatility"},
            {"label": "Discount rate applied", "value": "HM Treasury PES discount rate per DHSC GAM 2024-25 ch.7 — recalibrated annually"},
            {"label": "Lease term profile", "value": "Mix of 5-year + 10-year community-clinic leases with break clauses; minor longer-term LIFT contracts"},
            {"label": "Funding trajectory", "value": "2021-22 (pre-IFRS16) c. £0.3M operating lease → 2022-23 c. £0.6M ROU first year → 2024-25 £0.73M"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + NHSPS + CHP for LIFT vehicles"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + BNSSG ICB / B&NES, Swindon & Wiltshire ICB"},
            {"label": "Evaluation evidence", "value": "Trust ARA 2023-24; CQC inspection reports (RVN); BNSSG ICS estate strategy"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2022 IAS 17 operating-lease expense · Successor: NHSPS market-rent reform + cross-ICB estate consolidation"}
        ],
        "notes": "AWP's lease line jumped at the IFRS 16 2022 transition and has continued to grow under sustained NHSPS market-rent uplifts across the trust's geographically dispersed community-clinic footprint. The trust's coverage of two distinct ICBs — BNSSG (Bristol, N Somerset, S Glos) and B&NES, Swindon & Wiltshire — increases administrative complexity on estate consolidation, since the rationalisation logic differs between the urban Bristol core and the more dispersed Wiltshire / Swindon pattern. AWP also incurred reputational scrutiny via the 2022-23 CQC enforcement at Callington Road and Fromeside, with knock-on estate-investment pressure. The 2026 NHSPS market-rent review and any cross-ICB estate consolidation are the medium-term levers.",
        "sources": [
            {"publisher": "Avon and Wiltshire Mental Health Partnership NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.awp.nhs.uk/about-us/our-publications"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 7 — Leases)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS Property Services", "title": "Annual Report 2023-24 + market-rent methodology", "url": "https://www.property.nhs.uk/about/our-publications/"},
            {"publisher": "Care Quality Commission", "title": "AWP NHS Trust provider profile (RVN)", "url": "https://www.cqc.org.uk/provider/RVN"},
            {"publisher": "BNSSG Integrated Care Board", "title": "ICS estate strategy", "url": "https://bnssg.icb.nhs.uk/"}
        ],
        "related": ["Avon and Wiltshire Mental Health Partnership NHS Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "NHS Property Services Ltd", "Lease expenditure — Pennine Care NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "PFI / LIFT charges — Kent and Medway NHS and Social Care Partnership Trust": {
        "aliases": [{"name": "PFI / LIFT charges", "parent": "Kent and Medway NHS and Social Care Partnership Trust"}],
        "description": "KMPT's £0.73M PFI / LIFT charge reflects the trust's occupation of LIFT-procured community-MH bases across Kent and Medway under Express LIFT (East Kent) and other Kent LIFT vehicles (Community Health Partnerships shareholding + private partners + local-authority co-investment). The line covers the unitary-charge pass-through — debt service, FM lifecycle and soft-FM components — for those LIFT premises hosting MH community teams, CAMHS bases and crisis pathways across the county.",
        "beneficiaries": "c. 3,800 staff and a registered catchment c. 1.9M across Kent and Medway; LIFT-procured estate hosts community-MH team bases, CAMHS clinics and crisis-team workstations across both East Kent (Canterbury, Ashford, Thanet, Dover, Shepway) and West Kent (Maidstone, Tunbridge Wells, Sevenoaks, Medway, Swale).",
        "legal_basis": "IFRS 16 Leases (post-2022 transition for finance-lease + service-concession arrangements) · IFRIC 12 Service Concession Arrangements · DHSC Group Accounting Manual 2024-25 ch.7 · NHS (Local Improvement Finance Trust) regulations · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "PFI / LIFT charges 2024-25", "value": "£0.73M"},
            {"label": "Procurement vehicle", "value": "Express LIFT (East Kent) + Kent LIFT vehicles — CHP shareholding + private investor + LA partnership"},
            {"label": "Estate covered", "value": "Community-MH team bases + CAMHS clinics + crisis-team workstations across East + West Kent + Medway"},
            {"label": "Unitary charge composition", "value": "Debt-service component + lifecycle (hard-FM building maintenance) + soft-FM (cleaning, security where contracted)"},
            {"label": "Contract duration profile", "value": "LIFT contracts typically 25-year initial with extension option; Kent LIFTs signed mid-2000s — c. 8-12 years remaining"},
            {"label": "IFRS 16 / IFRIC 12 treatment", "value": "Service-concession assets recognised on-balance-sheet under IFRIC 12; lease-component re-evaluated under IFRS 16 ch.7 GAM"},
            {"label": "Lifecycle indexation", "value": "Annual RPI / CPI indexation per LIFT contract terms — material driver of year-on-year line movement"},
            {"label": "Funding trajectory", "value": "2020-21 c. £0.55M → 2024-25 £0.73M — sustained CPI-linked uplift"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + Community Health Partnerships + private LIFT investor consortium"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + Kent & Medway ICB; LIFT policy oversight at DHSC"},
            {"label": "Evaluation evidence", "value": "NAO LIFT review 2017-18; trust ARA disclosure 2023-24; Kent & Medway ICS estate strategy"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-LIFT mid-2000s NHS-Estates community-clinic model · Successor: end-of-LIFT-contract review + ICS estate consolidation early 2030s"}
        ],
        "notes": "KMPT's PFI / LIFT line is dominated by Express LIFT (East Kent) and complementary Kent LIFT vehicles, which procured community-health bases in the mid-2000s under the Local Improvement Finance Trust model — service-concession structures where CHP co-invests with private + LA partners, and the trust occupies as tenant under unitary-charge contracts. CPI / RPI indexation is the main driver of cost growth, layered on fixed debt-service and lifecycle components. As contracts approach their 25-year endpoint in the early 2030s, the trust and Kent & Medway ICB face the hand-back / extension / consolidation choice now confronting most LIFT-using MH trusts. KMPT major inpatient sites (St Martin's, Priority House) sit outside LIFT.",
        "sources": [
            {"publisher": "Kent and Medway NHS and Social Care Partnership Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.kmpt.nhs.uk/about-us/publications/"},
            {"publisher": "Community Health Partnerships", "title": "LIFT estate annual review", "url": "https://www.communityhealthpartnerships.co.uk/"},
            {"publisher": "National Audit Office", "title": "PFI and PF2 / LIFT review", "url": "https://www.nao.org.uk/reports/pfi-and-pf2/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 7 — Leases and service concessions)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "KMPT provider profile (RXY)", "url": "https://www.cqc.org.uk/provider/RXY"}
        ],
        "related": ["Kent and Medway NHS and Social Care Partnership Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Community Health Partnerships", "PFI / LIFT charges — Mersey Care NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Clinical supplies & services — Surrey and Borders Partnership NHS Foundation Trust": {
        "aliases": [{"name": "Clinical supplies & services", "parent": "Surrey and Borders Partnership NHS Foundation Trust"}],
        "description": "SABP's £0.72M clinical supplies & services line covers ward clinical consumables — anti-ligature equipment, single-use restraint-safe items, ward observation tooling, ECT consumables, dressings and minor clinical instruments — across Farnham Road Hospital (Guildford), Abraham Cowley Unit (Chertsey), Hellingly Centre (East Sussex border) and the trust's secure-LD inpatient service plus c. 60+ community-MH, CAMHS and addictions sites across Surrey and NE Hampshire. The combined acute-MH + secure-LD remit drives a higher per-bed clinical-consumables cost than community-only peers.",
        "beneficiaries": "c. 2,800 staff serving c. 1.3M Surrey + NE Hampshire residents; clinical-consumables consumption concentrated at c. 200 inpatient MH + secure-LD beds plus 60+ community + addictions clinic bases delivering c. 280,000 contacts annually.",
        "legal_basis": "IAS 2 Inventories · DHSC Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · Public Contracts Regulations 2015 + Procurement Act 2023 (in force Oct 2024) · Mental Health Units (Use of Force) Act 2018",
        "key_stats": [
            {"label": "Clinical supplies & services 2024-25", "value": "£0.72M"},
            {"label": "Site footprint generating consumption", "value": "Farnham Road (Guildford) + Abraham Cowley (Chertsey) + Hellingly + secure-LD inpatient + 60+ community sites"},
            {"label": "Bed-stock generating consumption", "value": "c. 200 inpatient MH + secure-LD beds plus 60+ community-clinic bases"},
            {"label": "Composition", "value": "Anti-ligature ward equipment + single-use restraint-safe items + observation tooling + ECT consumables + dressings + minor instruments"},
            {"label": "Use-of-Force Act driver", "value": "Mental Health Units (Use of Force) Act 2018 (Seni's Law) raises requirement for restraint-safe + de-escalation-supportive consumables"},
            {"label": "Secure-LD driver", "value": "Trust hosts secure-LD inpatient capability — specialist consumables raise per-bed cost above pure-acute-MH peers"},
            {"label": "Procurement route", "value": "NHS Supply Chain framework (majority) + Crown Commercial Service + minor local spot-buy"},
            {"label": "Funding trajectory", "value": "2020-21 c. £0.55M → 2024-25 £0.72M — uplift driven by Use-of-Force Act compliance + supplies CPI"},
            {"label": "Delivery body", "value": "Trust Procurement + Pharmacy + Estates teams; NHS Supply Chain framework operator"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + Surrey Heartlands ICB / Frimley ICB · NHS Supply Chain governance"},
            {"label": "Evaluation evidence", "value": "CQC inspection reports (RXX); NHS Supply Chain framework data; trust ARA 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-Seni's Law 2018 baseline · Successor: NHS Supply Chain Future Operating Model + Procurement Act 2023 transition + Mental Health Bill restraint-reduction agenda"}
        ],
        "notes": "SABP's clinical supplies & services line carries a structural premium over pure community-MH peers because the trust operates secure learning-disability inpatient capability alongside acute MH wards, generating specialist consumables demand (specialist incontinence, sensory-room consumables, restraint-safe items). The Mental Health Units (Use of Force) Act 2018 — Seni's Law — raised the bar on restraint-safe consumables and de-escalation tooling. SABP also faced scrutiny on inpatient ward safety, keeping consumables investment elevated. NHS Supply Chain Future Operating Model and Procurement Act 2023 (Oct 2024) reshape the framework; supplies CPI remains the dominant driver.",
        "sources": [
            {"publisher": "Surrey and Borders Partnership NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.sabp.nhs.uk/about-us/publications-and-corporate-information"},
            {"publisher": "NHS Supply Chain", "title": "Future Operating Model + category framework", "url": "https://www.supplychain.nhs.uk/"},
            {"publisher": "Department of Health and Social Care", "title": "Mental Health Units (Use of Force) Act 2018 statutory guidance", "url": "https://www.gov.uk/government/publications/mental-health-units-use-of-force-act-2018-statutory-guidance"},
            {"publisher": "Care Quality Commission", "title": "SABP provider profile (RXX)", "url": "https://www.cqc.org.uk/provider/RXX"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"}
        ],
        "related": ["Surrey and Borders Partnership NHS Foundation Trust", "Clinical Supplies & Drugs", "NHS Mental Health Trusts", "NHS Supply Chain", "Clinical supplies & services — South West London and St George's Mental Health NHS Trust", "Department of Health and Social Care"]
    },
    "Lease expenditure — Kent and Medway NHS and Social Care Partnership Trust": {
        "aliases": [{"name": "Lease expenditure", "parent": "Kent and Medway NHS and Social Care Partnership Trust"}],
        "description": "KMPT's £0.71M lease line reflects IFRS 16 right-of-use depreciation + interest on the trust's leased estate following the 2022 on-balance-sheet transition. The portfolio mixes NHS Property Services-leased community-MH and CAMHS premises, private landlord clinic space and minor co-located bases on partner-trust sites across Kent and Medway. Major inpatient hubs (St Martin's Canterbury, Priority House Maidstone, Littlebrook Dartford) sit outside the lease line on owned freehold; the line is therefore community-clinic dominated.",
        "beneficiaries": "c. 3,800 staff serving c. 1.9M residents across Kent and Medway; leased-estate component includes c. 35+ community-MH, CAMHS, IAPT and recovery bases plus minor co-located workstations on partner-NHS sites.",
        "legal_basis": "IFRS 16 Leases · DHSC Group Accounting Manual 2024-25 ch.7 · Landlord and Tenant Act 1954 · NHS Act 2006 · Health and Care Act 2022 · Property Services Act (NHSPS founding 2013)",
        "key_stats": [
            {"label": "Lease expenditure 2024-25", "value": "£0.71M"},
            {"label": "IFRS 16 transition jump", "value": "2022 on-balance-sheet adoption — operating leases reclassified to ROU asset + lease liability with depreciation + interest split"},
            {"label": "Leased site count", "value": "c. 35+ community premises across East + West Kent + Medway"},
            {"label": "Major lessor", "value": "NHS Property Services Ltd (majority) + private landlords + occasional partner-NHS sub-let"},
            {"label": "NHSPS rates dispute", "value": "Sustained NHSPS / MH-trust dispute on community-clinic market-rent uplift + service-charge methodology"},
            {"label": "Discount rate applied", "value": "HM Treasury PES discount rate per DHSC GAM 2024-25 ch.7 — recalibrated annually"},
            {"label": "Lease term profile", "value": "Mix of 5-year + 10-year community clinic leases with break clauses"},
            {"label": "Funding trajectory", "value": "2021-22 (pre-IFRS16) c. £0.3M → 2022-23 c. £0.55M ROU first year → 2024-25 £0.71M"},
            {"label": "Owned freehold context", "value": "St Martin's (Canterbury), Priority House (Maidstone), Littlebrook (Dartford) major inpatient sites are freehold — NOT in lease line"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + NHSPS"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + Kent & Medway ICB"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2022 IAS 17 operating-lease expense · Successor: NHSPS market-rent reform + K&M ICS estate consolidation"}
        ],
        "notes": "KMPT's lease line jumped at the IFRS 16 2022 transition and is community-clinic dominated, since the trust holds its major inpatient hubs (St Martin's, Priority House, Littlebrook) on owned freehold. The geographic spread across both East and West Kent plus Medway sustains the high site count even though individual community-clinic rents are modest. NHSPS market-rent uplift on community-clinic estate is the biggest cost-driver and a sector-wide friction with the Department, with ongoing recharge methodology disputes. The 2026 NHSPS market-rent review and the Kent & Medway ICB estate strategy will determine the medium-term trajectory; LIFT estate (separate £0.73M PFI / LIFT line) is treated under IFRIC 12 and reported separately.",
        "sources": [
            {"publisher": "Kent and Medway NHS and Social Care Partnership Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.kmpt.nhs.uk/about-us/publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 7 — Leases)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS Property Services", "title": "Annual Report 2023-24 + market-rent methodology", "url": "https://www.property.nhs.uk/about/our-publications/"},
            {"publisher": "Care Quality Commission", "title": "KMPT provider profile (RXY)", "url": "https://www.cqc.org.uk/provider/RXY"},
            {"publisher": "Kent and Medway Integrated Care Board", "title": "ICS estate strategy", "url": "https://www.kentandmedway.icb.nhs.uk/"}
        ],
        "related": ["Kent and Medway NHS and Social Care Partnership Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "NHS Property Services Ltd", "Lease expenditure — Avon and Wiltshire Mental Health Partnership NHS Trust", "Department of Health and Social Care"]
    },
    "Amortisation — Lancashire and South Cumbria NHS Foundation Trust": {
        "aliases": [{"name": "Amortisation", "parent": "Lancashire and South Cumbria NHS Foundation Trust"}],
        "description": "LSCFT's £0.71M amortisation line is the IAS 38 charge on capitalised intangibles — chiefly software licences, EPR build-out under NHS England's Frontline Digitisation programme, capitalised configuration of clinical systems, and minor capitalised training-asset balances. The 2018 Lancashire-Cumbria merger consolidated the previous separate amortisation cohorts, and ongoing FD investment to migrate to a Lancashire-and-South-Cumbria-wide EPR plus the trust's continued capitalised investment in care-record interoperability are the principal drivers.",
        "beneficiaries": "c. 7,000 staff serving c. 1.8M residents across Lancashire, Blackpool, Blackburn with Darwen and South Cumbria; EPR-rolled-out clinical user base spans inpatient MH wards (The Harbour, Guild Lodge), CAMHS, crisis pathways and community-MH teams — c. 4,500 active clinical users.",
        "legal_basis": "IAS 38 Intangible Assets · DHSC Group Accounting Manual 2024-25 ch.5 · NHS Act 2006 · Health and Care Act 2022 · NHSE Frontline Digitisation programme governance · HM Treasury FReM (capitalisation thresholds)",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£0.71M"},
            {"label": "Asset composition", "value": "Software licences (EPR + clinical-systems portfolio) + capitalised configuration + minor capitalised training balances + interoperability tooling"},
            {"label": "Useful economic life applied", "value": "Software 5-7 years per DHSC GAM 2024-25 ch.5 — straight-line amortisation"},
            {"label": "Frontline Digitisation context", "value": "NHSE FD funds EPR upgrades + 'core capabilities' (e-prescribing, e-observations) — capitalised under IAS 38, amortised over UEL"},
            {"label": "Clinical user base", "value": "c. 4,500 active clinical users across MH inpatient + community + CAMHS + crisis + secure pathways"},
            {"label": "2018 merger context", "value": "Lancashire Care + Cumbria Partnership MH services merged 2018-2019 — system rationalisation drove capitalised configuration spend"},
            {"label": "Capitalisation threshold", "value": "£5,000 individual / £25,000 pooled per DHSC GAM 2024-25 (FReM-aligned)"},
            {"label": "Funding trajectory", "value": "2020-21 c. £0.4M → 2022-23 c. £0.55M → 2024-25 £0.71M — uplift driven by FD-funded EPR module additions + post-merger system consolidation"},
            {"label": "Delivery body", "value": "Trust Digital + Finance teams + NHSE Frontline Digitisation programme office + EPR vendor"},
            {"label": "Policy owner", "value": "DHSC + NHSE Transformation Directorate (digital) + Lancashire & South Cumbria ICB"},
            {"label": "Evaluation evidence", "value": "NHSE Frontline Digitisation milestone reporting; trust ARA digital disclosure 2023-24; What Good Looks Like (WGLL) framework benchmarking"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2018 separate Lancashire Care + Cumbria Partnership systems · Successor: FD core-capabilities completion + Federated Data Platform interoperability"}
        ],
        "notes": "LSCFT's amortisation line reflects two compounding drivers — the post-2018-merger system-consolidation spend that capitalised under IAS 38 and unwinds over a 5-7 year useful-economic-life, and ongoing NHS England Frontline Digitisation funding for EPR core-capability extensions (e-prescribing, e-observations, patient-portal). Useful-economic-life of 5-7 years for software per DHSC GAM ch.5 means recent FD-funded build will continue feeding amortisation through the late 2020s. LSCFT also faced sustained CQC scrutiny on inpatient-services quality 2018-2024, which drove additional digital investment for clinical-records assurance — itself capitalised and amortised. Federated Data Platform interoperability is the next driver.",
        "sources": [
            {"publisher": "Lancashire and South Cumbria NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.lscft.nhs.uk/About-Us/publications/"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/connecting-health-and-care-providers/frontline-digitisation/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 5 — Intangible assets)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "LSCFT provider profile (RW5)", "url": "https://www.cqc.org.uk/provider/RW5"},
            {"publisher": "Lancashire and South Cumbria ICB", "title": "ICS digital strategy", "url": "https://www.lancashireandsouthcumbria.icb.nhs.uk/"}
        ],
        "related": ["Lancashire and South Cumbria NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "NHS England", "Amortisation — Derbyshire Healthcare NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Business rates — Cheshire and Wirral Partnership NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "Cheshire and Wirral Partnership NHS Foundation Trust"}],
        "description": "CWP's £0.69M business-rates charge reflects VOA-set rateable values × 49.9p UBR (small) / 54.6p (standard) on the trust's occupied estate — the Countess of Chester Health Park (specialist MH unit), Bowmere Hospital (Chester), Springview (Wirral), Soss Moss (Nether Alderley), Millbrook Unit (Macclesfield) and c. 30+ community-MH, CAMHS, LD and addictions bases across Cheshire and the Wirral. NHS FTs do not receive charitable exemption; the line is rebased at each VOA revaluation cycle.",
        "beneficiaries": "Approximately 30+ occupied hereditaments (acute MH, secure-LD inpatient, community clinics, CAMHS sites, addictions bases) across Cheshire West & Chester, Cheshire East and Wirral; serves a registered catchment c. 1.0M.",
        "legal_basis": "Local Government Finance Act 1988 (Schedule 6 valuation) · Non-Domestic Rating (Multipliers and Private Finance) Act 2024 · Non-Domestic Rating Act 2023 · NHS Act 2006 · Health and Care Act 2022 · DHSC GAM 2024-25",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£0.69M"},
            {"label": "Hereditament count", "value": "c. 30+ occupied sites across Cheshire West, Cheshire East + Wirral"},
            {"label": "Major rated sites", "value": "Bowmere Hospital (Chester) + Springview (Wirral) + Soss Moss (Nether Alderley) + Millbrook (Macclesfield) + community bases"},
            {"label": "UBR 2024-25", "value": "49.9p small-multiplier / 54.6p standard-multiplier — frozen at 2023-24 levels under Autumn Statement 2023"},
            {"label": "Charitable exemption", "value": "Not applicable — NHS FTs are not registered charities under Charities Act 2011"},
            {"label": "Billing authorities", "value": "Cheshire West & Chester + Cheshire East + Wirral MBC (3 authorities, post-2009 unitary reorganisation)"},
            {"label": "VOA 2023 revaluation impact", "value": "Mixed urban Wirral / Chester premises and rural Cheshire community clinics; net broadly neutral post-pandemic"},
            {"label": "NHSPS interaction", "value": "Some community clinic estate held via NHSPS lease; rates passed through to CWP as occupier"},
            {"label": "Funding trajectory", "value": "2020-21 c. £0.55M → 2024-25 £0.69M — tracks UBR + new-site additions"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + VOA + 3 unitary billing authorities"},
            {"label": "Policy owner", "value": "DHSC + MHCLG (business rates policy) + NHSE Provider Finance"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2017 antecedent valuation date list · Successor: 2026 next revaluation (3-year cycle under NDRA 2023)"}
        ],
        "notes": "CWP's business-rates line is shaped by a relatively concentrated three-unitary-authority footprint — Cheshire West & Chester, Cheshire East and Wirral — which simplifies billing-authority engagement compared to multi-district trusts elsewhere. Bowmere Hospital (Chester) and Springview (Wirral) are the two largest hereditaments by RV, with Soss Moss carrying meaningful RV as a specialist learning-disability site. The Autumn Statement 2023 UBR freeze gave a one-year reprieve, but the 2026 revaluation under NDRA 2023's three-year cycle is expected to rebase upward. NHSPS-leased community clinics pass rates through to CWP under occupier-rule, consistent with the sector-wide service-charge friction.",
        "sources": [
            {"publisher": "Cheshire and Wirral Partnership NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.cwp.nhs.uk/about-us/publications/"},
            {"publisher": "Valuation Office Agency", "title": "Find a business rates valuation (NHS hereditaments)", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "Department for Levelling Up, Housing and Communities", "title": "Business rates — multipliers and reliefs 2024-25", "url": "https://www.gov.uk/introduction-to-business-rates"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "CWP provider profile (RXA)", "url": "https://www.cqc.org.uk/provider/RXA"}
        ],
        "related": ["Cheshire and Wirral Partnership NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Department of Health and Social Care", "Business rates — Coventry and Warwickshire Partnership NHS Trust", "Valuation Office Agency"]
    },
    "Lease expenditure — Greater Manchester Mental Health NHS Foundation Trust": {
        "aliases": [{"name": "Lease expenditure", "parent": "Greater Manchester Mental Health NHS Foundation Trust"}],
        "description": "GMMH's £0.68M lease line reflects IFRS 16 right-of-use depreciation + interest on the trust's leased estate following the 2022 on-balance-sheet transition. The portfolio is dominated by NHS Property Services-leased community-MH and CAMHS premises across Manchester, Salford, Trafford, Bolton and Wigan, plus minor private-landlord and Community Health Partnerships LIFT exposure. GMMH's reputation following the 2022 Edenfield Centre Panorama exposé and the Lampard Inquiry context drove additional estate-investment scrutiny that cycles through this line.",
        "beneficiaries": "c. 5,500 staff serving c. 1.4M residents across Manchester, Salford, Trafford, Bolton and Wigan; leased-estate component includes c. 40+ community-MH, CAMHS, IAPT and recovery bases plus minor co-located workstations on partner-NHS sites.",
        "legal_basis": "IFRS 16 Leases · DHSC Group Accounting Manual 2024-25 ch.7 · Landlord and Tenant Act 1954 · NHS Act 2006 · Health and Care Act 2022 · Property Services Act (NHSPS founding 2013)",
        "key_stats": [
            {"label": "Lease expenditure 2024-25", "value": "£0.68M"},
            {"label": "IFRS 16 transition jump", "value": "2022 on-balance-sheet adoption — operating leases reclassified to ROU asset + lease liability with depreciation + interest split"},
            {"label": "Leased site count", "value": "c. 40+ community premises across five GM boroughs"},
            {"label": "Major lessor", "value": "NHS Property Services Ltd (majority) + private landlords + Community Health Partnerships (minor LIFT exposure)"},
            {"label": "Edenfield context", "value": "Sept 2022 BBC Panorama exposé of Edenfield Centre abuse → CQC enforcement + sustained estate-quality scrutiny → leasehold remediation pressure"},
            {"label": "Discount rate applied", "value": "HM Treasury PES discount rate per DHSC GAM 2024-25 ch.7 — recalibrated annually; NHSPS market-rent dispute drives volatility"},
            {"label": "Lease term profile", "value": "Mix of 5-year + 10-year community clinic leases; minor longer-term LIFT contracts"},
            {"label": "Funding trajectory", "value": "2021-22 (pre-IFRS16) c. £0.3M → 2022-23 c. £0.55M ROU first year → 2024-25 £0.68M"},
            {"label": "Owned freehold context", "value": "Major inpatient hubs (Park House, Edenfield, Meadowbrook) freehold — NOT in lease line"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + NHSPS + CHP for LIFT vehicles"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + Greater Manchester ICB"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2022 IAS 17 operating-lease expense · Successor: NHSPS market-rent reform + GM ICS estate consolidation"}
        ],
        "notes": "GMMH's lease line jumped at the IFRS 16 2022 transition and is community-clinic dominated, since the trust holds its major inpatient hubs (Park House at North Manchester General; Edenfield Centre and Meadowbrook at Prestwich) on owned freehold. The September 2022 Edenfield Centre Panorama exposé and the subsequent CQC enforcement and Lampard-Inquiry-related context drove sustained estate-quality scrutiny, with knock-on effects on leasehold remediation and additional satellite-clinic leases as the trust moved community services. GMMH covers five Greater Manchester boroughs, generating a high site count for a relatively modest line value. NHSPS market-rent uplift on community estate is the biggest cost-driver going forward.",
        "sources": [
            {"publisher": "Greater Manchester Mental Health NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.gmmh.nhs.uk/annual-reports"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 7 — Leases)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Edenfield Centre / GMMH enforcement reports", "url": "https://www.cqc.org.uk/provider/RXV"},
            {"publisher": "NHS Property Services", "title": "Annual Report 2023-24 + market-rent methodology", "url": "https://www.property.nhs.uk/about/our-publications/"},
            {"publisher": "BBC Panorama", "title": "Undercover Hospital: Patients at Risk (Edenfield Centre)", "url": "https://www.bbc.co.uk/programmes/m001cpkj"}
        ],
        "related": ["Greater Manchester Mental Health NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "NHS Property Services Ltd", "Lease expenditure — Avon and Wiltshire Mental Health Partnership NHS Trust", "Department of Health and Social Care"]
    },
    "Business rates — Sheffield Health and Social Care NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "Sheffield Health and Social Care NHS Foundation Trust"}],
        "description": "SHSC's £0.68M business-rates charge reflects VOA-set rateable values × 49.9p UBR (small) / 54.6p (standard) on the trust's occupied estate within Sheffield — the Michael Carlisle Centre, Longley Centre, Forest Lodge (LD), Hillsborough adult-MH bases and c. 25+ community-MH, CAMHS, addictions and LD bases across the city. As a single-city unitary trust, billing is concentrated on Sheffield City Council. NHS FTs do not receive charitable exemption; the line is rebased at each VOA revaluation cycle.",
        "beneficiaries": "Approximately 25+ occupied hereditaments (acute MH wards, LD inpatient, community clinics, CAMHS sites, addictions bases) across the city of Sheffield; serves a registered catchment c. 580,000 (city population).",
        "legal_basis": "Local Government Finance Act 1988 (Schedule 6 valuation) · Non-Domestic Rating (Multipliers and Private Finance) Act 2024 · Non-Domestic Rating Act 2023 · NHS Act 2006 · Health and Care Act 2022 · DHSC GAM 2024-25",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£0.68M"},
            {"label": "Hereditament count", "value": "c. 25+ occupied sites across the city of Sheffield"},
            {"label": "Major rated sites", "value": "Michael Carlisle Centre + Longley Centre + Forest Lodge (LD) + Hillsborough sites + community bases"},
            {"label": "UBR 2024-25", "value": "49.9p small-multiplier / 54.6p standard-multiplier — frozen at 2023-24 levels under Autumn Statement 2023"},
            {"label": "Charitable exemption", "value": "Not applicable — NHS FTs are not registered charities under Charities Act 2011"},
            {"label": "Billing authority", "value": "Sheffield City Council (single unitary)"},
            {"label": "VOA 2023 revaluation impact", "value": "Sheffield-specific commercial RV movement post-pandemic; net broadly neutral; Forest Lodge custom-built LD facility carries higher £/m² RV than community clinics"},
            {"label": "NHSPS interaction", "value": "Some community clinic estate held via NHSPS lease; rates passed through to SHSC as occupier"},
            {"label": "Funding trajectory", "value": "2020-21 c. £0.55M → 2024-25 £0.68M — tracks UBR + new-site additions"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + VOA + Sheffield City Council billing"},
            {"label": "Policy owner", "value": "DHSC + MHCLG (business rates policy) + NHSE Provider Finance"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2017 antecedent valuation date list · Successor: 2026 next revaluation (3-year cycle under NDRA 2023)"}
        ],
        "notes": "SHSC's business-rates line benefits from operational simplicity as a single-unitary-billing-authority trust — Sheffield City Council handles all rates billing — but is structurally elevated by the city's dense inpatient and community-MH footprint. The Michael Carlisle Centre and Longley Centre constitute the two largest hereditaments, with Forest Lodge LD facility carrying above-average RV per m² as a specialist custom-built site. The Autumn Statement 2023 UBR freeze gave a one-year reprieve, but the 2026 revaluation under NDRA 2023's three-year cycle is expected to rebase upward. SHSC has been under sustained quality scrutiny following the 2022-23 CQC enforcement, which has knock-on estate-investment implications for the rates line via new or refurbished hereditaments.",
        "sources": [
            {"publisher": "Sheffield Health and Social Care NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.shsc.nhs.uk/about-us/our-publications"},
            {"publisher": "Valuation Office Agency", "title": "Find a business rates valuation (NHS hereditaments)", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "Department for Levelling Up, Housing and Communities", "title": "Business rates — multipliers and reliefs 2024-25", "url": "https://www.gov.uk/introduction-to-business-rates"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "SHSC provider profile (RXG)", "url": "https://www.cqc.org.uk/provider/RXG"}
        ],
        "related": ["Sheffield Health and Social Care NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Department of Health and Social Care", "Business rates — Cheshire and Wirral Partnership NHS Foundation Trust", "Valuation Office Agency"]
    },
    "Lease expenditure — Surrey and Borders Partnership NHS Foundation Trust": {
        "aliases": [{"name": "Lease expenditure", "parent": "Surrey and Borders Partnership NHS Foundation Trust"}],
        "description": "SABP's £0.665M lease line reflects IFRS 16 right-of-use depreciation + interest on the trust's leased estate following the 2022 on-balance-sheet transition. The portfolio is dominated by NHS Property Services-leased community-MH and CAMHS premises across Surrey and NE Hampshire, plus minor private landlord and partner-NHS co-located bases. Major inpatient hubs (Farnham Road, Abraham Cowley) sit on owned freehold; the line is therefore community-clinic + ancillary-base dominated.",
        "beneficiaries": "c. 2,800 staff serving c. 1.3M residents across Surrey and NE Hampshire; leased-estate component includes c. 35+ community-MH, CAMHS, IAPT and addictions bases plus minor co-located workstations on partner-NHS sites.",
        "legal_basis": "IFRS 16 Leases · DHSC Group Accounting Manual 2024-25 ch.7 · Landlord and Tenant Act 1954 · NHS Act 2006 · Health and Care Act 2022 · Property Services Act (NHSPS founding 2013)",
        "key_stats": [
            {"label": "Lease expenditure 2024-25", "value": "£0.665M"},
            {"label": "IFRS 16 transition jump", "value": "2022 on-balance-sheet adoption — operating leases reclassified to ROU asset + lease liability with depreciation + interest split"},
            {"label": "Leased site count", "value": "c. 35+ community premises across Surrey + NE Hampshire"},
            {"label": "Major lessor", "value": "NHS Property Services Ltd (majority) + private landlords + partner-NHS co-located workstations"},
            {"label": "NHSPS rates dispute", "value": "Sustained NHSPS / MH-trust dispute on community-clinic market-rent uplift + service-charge methodology — feeds line volatility"},
            {"label": "Discount rate + lease term", "value": "HM Treasury PES discount rate per DHSC GAM 2024-25 ch.7; mix of 5- and 10-year clinic leases with break clauses"},
            {"label": "Funding trajectory", "value": "2021-22 (pre-IFRS16) c. £0.3M → 2022-23 c. £0.5M ROU first year → 2024-25 £0.665M"},
            {"label": "Owned freehold context", "value": "Farnham Road (Guildford) + Abraham Cowley Unit (Chertsey) major inpatient sites freehold — NOT in lease line"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + NHSPS"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + Surrey Heartlands ICB / Frimley ICB"},
            {"label": "Evaluation evidence", "value": "Trust ARA 2023-24; Surrey Heartlands ICS estate strategy"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2022 IAS 17 operating-lease expense · Successor: NHSPS market-rent reform + cross-ICB estate consolidation"}
        ],
        "notes": "SABP's lease line jumped at the IFRS 16 2022 transition and is community-clinic dominated, since the trust holds Farnham Road and Abraham Cowley on owned freehold. The trust's coverage of two ICBs — Surrey Heartlands and Frimley — increases administrative complexity on estate consolidation. SABP also faced reputational scrutiny following the 2022-23 CQC enforcement and inquest findings on inpatient ward safety, with knock-on estate-investment pressure. The 2026 NHSPS market-rent review and any cross-ICB estate consolidation are the medium-term levers; CPI uplift on existing leases remains the dominant driver in the meantime.",
        "sources": [
            {"publisher": "Surrey and Borders Partnership NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.sabp.nhs.uk/about-us/publications-and-corporate-information"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 7 — Leases)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS Property Services", "title": "Annual Report 2023-24 + market-rent methodology", "url": "https://www.property.nhs.uk/about/our-publications/"},
            {"publisher": "Care Quality Commission", "title": "SABP provider profile (RXX)", "url": "https://www.cqc.org.uk/provider/RXX"},
            {"publisher": "Surrey Heartlands ICB", "title": "ICS estate strategy", "url": "https://www.surreyheartlands.org/"}
        ],
        "related": ["Surrey and Borders Partnership NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "NHS Property Services Ltd", "Lease expenditure — Kent and Medway NHS and Social Care Partnership Trust", "Department of Health and Social Care"]
    },
    "Transport (business + patient) — Camden and Islington NHS Foundation Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "Camden and Islington NHS Foundation Trust"}],
        "description": "C&I's £0.66M transport line covers community-MH, crisis-team and CAMHS mileage plus inter-site patient transfers across the trust's Camden and Islington footprint plus inter-trust flow into other London-MH trust pathways. C&I operates the Highgate Mental Health Centre and St Pancras Hospital sites, with significant patient-transfer activity to Highgate as the trust's main acute-MH hub, plus Mental Health Act s.135/136 conveyance contracted via London Ambulance Service and accredited secure-transport providers.",
        "beneficiaries": "c. 1,950 staff serving c. 480,000 residents across Camden + Islington; transport-line beneficiaries include c. 16,000 community-MH service-users plus inter-site transfers and London-pan-region forensic / specialist referrals. C&I is currently in pre-merger phase with NELFT under the North London MH Partnership.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · NHS Act 2006 · Mental Health Act 1983 (s.135/136 conveyance) · Health and Care Act 2022 · HMRC Approved Mileage Allowance Payments",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£0.66M"},
            {"label": "Catchment area", "value": "Camden + Islington (c. 480,000 population) — dense urban inner-London footprint"},
            {"label": "Site footprint", "value": "Highgate Mental Health Centre (acute hub) + St Pancras Hospital (community + specialist) + community-MH bases"},
            {"label": "Urban transport profile", "value": "Inner-London dense footprint = lower per-WTE community mileage than rural peers; offset by ULEZ-compliant fleet cost + central-London parking / congestion costs"},
            {"label": "MHA conveyance share", "value": "s.136 / s.135 conveyance via London Ambulance Service contract + accredited secure-transport providers"},
            {"label": "Staff mileage rate", "value": "NHS Agenda for Change Section 17 / HMRC AMAP 45p first 10,000 miles"},
            {"label": "ULEZ context", "value": "Aug 2023 ULEZ expansion to Greater London — fleet replacement to ULEZ-compliant vehicles + grant uplift driver"},
            {"label": "Funding trajectory", "value": "2020-21 c. £0.45M → 2024-25 £0.66M — uplift driven by ULEZ-compliant fleet cost + post-pandemic activity recovery + fuel CPI"},
            {"label": "Delivery body", "value": "Trust Estates + Travel team; PTS contracted with London Ambulance Service NHS Trust + accredited secure-transport providers"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + North Central London ICB + GLA / TfL (ULEZ)"},
            {"label": "Evaluation evidence", "value": "CQC inspection reports (RWK); NCL ICS estate + travel review"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-ULEZ-expansion 2023 baseline · Successor: North London MH Partnership merger with NELFT (announced 2023) — consolidated transport regime"}
        ],
        "notes": "C&I's transport line carries a distinctive London-cost profile — short distances mean per-WTE community mileage is among the lowest in the MH-trust sector, but central-London parking costs, ULEZ compliance (since the August 2023 expansion to all Greater London) and London Ambulance Service PTS contract pricing partially offset that geographic advantage. The trust's planned merger with NELFT under the North London MH Partnership (board-level merger announced 2023, completion target 2024-25) is the most consequential structural change, consolidating two separate transport regimes across a wider North London footprint. Inter-site patient transfers between St Pancras and Highgate are the recurring flow; pan-London forensic referrals are episodic but high-value.",
        "sources": [
            {"publisher": "Camden and Islington NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.candi.nhs.uk/about-us/our-publications"},
            {"publisher": "Care Quality Commission", "title": "C&I provider profile (RWK)", "url": "https://www.cqc.org.uk/provider/RWK"},
            {"publisher": "Greater London Authority / Transport for London", "title": "ULEZ expansion 2023 — guidance + scrappage scheme", "url": "https://tfl.gov.uk/modes/driving/ultra-low-emission-zone"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "North London Mental Health Partnership", "title": "C&I + NELFT merger programme", "url": "https://www.northlondonmentalhealth.nhs.uk/"}
        ],
        "related": ["Camden and Islington NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Department of Health and Social Care", "Transport (business + patient) — Lancashire and South Cumbria NHS Foundation Trust", "Mental Health Act 1983"]
    },
    "Establishment costs — Sheffield Health and Social Care NHS Foundation Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "Sheffield Health and Social Care NHS Foundation Trust"}],
        "description": "SHSC's £0.66M establishment costs line covers premises-related operational overhead — utility bills (electricity, gas, water, sewerage), waste-management, telephony, postage, internal print + reprographics, statutory premises maintenance fees and minor estate-running consumables — across the Michael Carlisle Centre, Longley Centre, Forest Lodge LD inpatient and c. 25+ community-MH, CAMHS and addictions bases across Sheffield. Energy CPI through 2022-23 and the partial easing in 2024-25 are the dominant year-on-year drivers.",
        "beneficiaries": "c. 2,800 staff plus c. 16,000 active service-users across the city of Sheffield; establishment-cost beneficiaries include all staff and service-users at c. 25+ occupied sites incl. acute MH wards, LD inpatient, community clinics, CAMHS sites and addictions bases.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses chapter) · IAS 1 Presentation of Financial Statements · NHS Act 2006 · Health and Care Act 2022 · Climate Change Act 2008 (NHS net-zero by 2040 statutory target via Health and Care Act 2022 s.116)",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£0.66M"},
            {"label": "Composition", "value": "Utilities (electricity, gas, water, sewerage) + waste management + telephony + postage + reprographics + statutory premises maintenance fees + minor running consumables"},
            {"label": "Site footprint generating consumption", "value": "Michael Carlisle Centre + Longley Centre + Forest Lodge (LD) + Hillsborough sites + 25+ community bases"},
            {"label": "Energy cost driver", "value": "Wholesale gas + electricity unit-cost surge 2022-23, partial easing 2024-25; NHS net-zero 2040 statutory target drives capital investment + opex shift"},
            {"label": "Energy Bill Discount Scheme", "value": "Replaced Energy Bill Relief Scheme Apr 2023 → ended Mar 2024; trust now exposed to wholesale prices subject to NHSE risk-pool guidance"},
            {"label": "NHS net-zero context", "value": "NHS Long Term Plan + Health and Care Act 2022 s.116 — net-zero direct emissions 2040, scope-3 by 2045; drives heat-pump + LED + insulation investment"},
            {"label": "Funding trajectory", "value": "2020-21 c. £0.5M → 2022-23 c. £0.7M (energy spike) → 2024-25 £0.66M (partial easing)"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + utility suppliers + waste contractors"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + South Yorkshire ICB"},
            {"label": "Evaluation evidence", "value": "Trust ARA 2023-24 sustainability disclosure; NHS Greener Plan reporting; CQC inspection reports (RXG)"},
            {"label": "CQC enforcement context", "value": "2022-23 CQC enforcement on inpatient wards drove additional estate-running cost on remediation"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2022 wholesale-energy market baseline · Successor: NHS net-zero capital investment + ICB-level energy-procurement consolidation"}
        ],
        "notes": "SHSC's establishment costs line tracked the wholesale-energy market closely through the 2022-23 spike and the 2024-25 partial easing. The Energy Bill Discount Scheme (which replaced the temporary Energy Bill Relief Scheme in April 2023) ended in March 2024, leaving the trust exposed to wholesale prices subject to NHS England risk-pool guidance and the trust's own forward-purchasing strategy. The NHS Long Term Plan net-zero by 2040 commitment, given statutory force by section 116 of the Health and Care Act 2022, is the structural driver — heat-pump retrofits, LED replacements and insulation investment lower opex over the medium term but require capital. The 2022-23 CQC enforcement on SHSC inpatient wards drove additional estate-running cost on remediation.",
        "sources": [
            {"publisher": "Sheffield Health and Social Care NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.shsc.nhs.uk/about-us/our-publications"},
            {"publisher": "NHS England", "title": "Greener NHS — Delivering a Net Zero National Health Service", "url": "https://www.england.nhs.uk/greenernhs/"},
            {"publisher": "Department for Energy Security and Net Zero", "title": "Energy Bill Discount Scheme (closed Mar 2024)", "url": "https://www.gov.uk/government/publications/energy-bill-discount-scheme"},
            {"publisher": "Care Quality Commission", "title": "SHSC provider profile (RXG)", "url": "https://www.cqc.org.uk/provider/RXG"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"}
        ],
        "related": ["Sheffield Health and Social Care NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "NHS England", "Establishment costs — Avon and Wiltshire Mental Health Partnership NHS Trust", "Department of Health and Social Care"]
    },
    "Business rates — Barnet, Enfield And Haringey Mental Health NHS Trust": {
        "aliases": [{"name": "Business rates", "parent": "Barnet, Enfield And Haringey Mental Health NHS Trust"}],
        "description": "BEH-MHT's £0.64M business-rates charge reflects VOA-set rateable values × 49.9p UBR (small) / 54.6p (standard) on the trust's occupied estate — Chase Farm Mental Health Centre, St Ann's Hospital (Haringey), Edgware Community Hospital MH wards and c. 20+ community-MH, CAMHS and IAPT bases across the three north-London boroughs of Barnet, Enfield and Haringey. NHS Trusts do not receive charitable exemption; the line is rebased at each VOA revaluation cycle. BEH-MHT is in pre-merger phase under the North London MH Partnership.",
        "beneficiaries": "Approximately 20+ occupied hereditaments (acute MH wards, recovery houses, community clinics, CAMHS sites, IAPT bases) across Barnet, Enfield and Haringey; serves a registered catchment c. 1.0M north-London residents.",
        "legal_basis": "Local Government Finance Act 1988 (Schedule 6 valuation) · Non-Domestic Rating (Multipliers and Private Finance) Act 2024 · Non-Domestic Rating Act 2023 · NHS Act 2006 · Health and Care Act 2022 · DHSC GAM 2024-25",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£0.64M"},
            {"label": "Hereditament count", "value": "c. 20+ occupied sites across three north-London boroughs"},
            {"label": "Major rated sites", "value": "Chase Farm MH Centre + St Ann's Hospital (Haringey) + Edgware Community Hospital MH wards + community bases"},
            {"label": "UBR 2024-25", "value": "49.9p small-multiplier / 54.6p standard-multiplier — frozen at 2023-24 levels under Autumn Statement 2023"},
            {"label": "Charitable exemption", "value": "Not applicable — NHS Trusts are not registered charities under Charities Act 2011"},
            {"label": "Billing authorities", "value": "London Borough of Barnet + LB Enfield + LB Haringey"},
            {"label": "VOA 2023 revaluation impact", "value": "London-wide commercial RV uplift post-pandemic, partly offset by hybrid-working impact on office space; net upward for BEH-MHT inpatient hereditaments"},
            {"label": "St Ann's redevelopment + NHSPS", "value": "St Ann's partial-disposal + Catalyst Housing redevelopment compressed footprint; NHSPS-leased clinics pass rates through to occupier"},
            {"label": "Funding trajectory", "value": "2020-21 c. £0.55M → 2024-25 £0.64M — tracks UBR + St Ann's compression"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + VOA + 3 LB billing authorities"},
            {"label": "Policy owner", "value": "DHSC + MHCLG (business rates policy) + NHSE Provider Finance"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2017 antecedent valuation date list · Successor: 2026 next revaluation + North London MH Partnership merger with C&I + NELFT"}
        ],
        "notes": "BEH-MHT's business-rates line is shaped by inner-north-London land values and the substantial St Ann's Hospital site, with major hereditaments at Chase Farm and St Ann's plus dispersed community clinics across three London boroughs. The St Ann's redevelopment programme (with Catalyst Housing) consolidated MH services onto a smaller core footprint while disposing of surplus land for housing, compressing the rates footprint over recent years. The Autumn Statement 2023 UBR freeze gave a one-year reprieve, but the 2026 revaluation under NDRA 2023's 3-year cycle is expected to rebase upward. The North London MH Partnership merger (BEH-MHT + C&I + NELFT) will consolidate the rates regime across an enlarged trust from 2024-25 onward.",
        "sources": [
            {"publisher": "Barnet, Enfield and Haringey Mental Health NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.beh-mht.nhs.uk/about-us/publications"},
            {"publisher": "Valuation Office Agency", "title": "Find a business rates valuation (NHS hereditaments)", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "Department for Levelling Up, Housing and Communities", "title": "Business rates — multipliers and reliefs 2024-25", "url": "https://www.gov.uk/introduction-to-business-rates"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "North London Mental Health Partnership", "title": "BEH-MHT + C&I + NELFT merger programme", "url": "https://www.northlondonmentalhealth.nhs.uk/"}
        ],
        "related": ["Barnet, Enfield And Haringey Mental Health NHS Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Department of Health and Social Care", "Business rates — Sheffield Health and Social Care NHS Foundation Trust", "Valuation Office Agency"]
    },
    "Business rates — Greater Manchester Mental Health NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "Greater Manchester Mental Health NHS Foundation Trust"}],
        "description": "GMMH's £0.63M business-rates charge reflects VOA-set rateable values × 49.9p UBR (small) / 54.6p (standard) on the trust's occupied estate — Park House (North Manchester General), Edenfield Centre and Meadowbrook (Prestwich), plus c. 40+ community-MH, CAMHS and addictions bases across Manchester, Salford, Trafford, Bolton and Wigan. NHS FTs do not receive charitable exemption; the line is rebased at each VOA revaluation cycle. The Edenfield Centre Panorama exposé (Sept 2022) drove sustained estate-quality investment that interacts with the rates footprint.",
        "beneficiaries": "Approximately 40+ occupied hereditaments (acute MH wards, secure-services inpatient, community clinics, CAMHS sites, addictions bases) across five Greater Manchester boroughs; serves a registered catchment c. 1.4M.",
        "legal_basis": "Local Government Finance Act 1988 (Schedule 6 valuation) · Non-Domestic Rating (Multipliers and Private Finance) Act 2024 · Non-Domestic Rating Act 2023 · NHS Act 2006 · Health and Care Act 2022 · DHSC GAM 2024-25",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£0.63M"},
            {"label": "Hereditament count", "value": "c. 40+ occupied sites across five GM boroughs (Manchester, Salford, Trafford, Bolton, Wigan)"},
            {"label": "Major rated sites", "value": "Park House (NMG site) + Edenfield Centre (Prestwich, secure) + Meadowbrook (Prestwich) + community bases"},
            {"label": "UBR 2024-25", "value": "49.9p small-multiplier / 54.6p standard-multiplier — frozen at 2023-24 levels under Autumn Statement 2023"},
            {"label": "Charitable exemption", "value": "Not applicable — NHS FTs are not registered charities under Charities Act 2011"},
            {"label": "Billing authorities", "value": "Manchester CC + Salford CC + Trafford MBC + Bolton MBC + Wigan MBC (5 unitaries)"},
            {"label": "VOA 2023 revaluation impact", "value": "Mixed urban GM commercial RV; net broadly neutral; Edenfield Centre custom-built secure-services facility carries higher £/m² RV than community clinics"},
            {"label": "Edenfield context", "value": "Sept 2022 BBC Panorama exposé → CQC enforcement → estate-quality remediation investment cycles through rates footprint"},
            {"label": "NHSPS interaction", "value": "Some community clinic estate held via NHSPS lease; rates passed through to GMMH as occupier"},
            {"label": "Funding trajectory", "value": "2020-21 c. £0.5M → 2024-25 £0.63M — tracks UBR + new-site additions + remediation footprint"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + VOA + 5 GM unitary billing authorities"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2017 antecedent valuation date list · Successor: 2026 next revaluation (3-year cycle under NDRA 2023)"}
        ],
        "notes": "GMMH's business-rates line is shaped by the trust's role as the lead MH provider for five Greater Manchester boroughs, with the Edenfield Centre carrying above-average RV per m² as a custom-built secure-services facility. The September 2022 BBC Panorama exposé of patient abuse at Edenfield triggered CQC enforcement and a sustained estate-quality remediation programme, with knock-on additions to the rates footprint as remediated wards came back into use. The Autumn Statement 2023 UBR freeze gave a one-year reprieve, but the 2026 revaluation under NDRA 2023's 3-year cycle is expected to rebase upward. NHSPS-leased community clinics pass rates through to GMMH under occupier-rule.",
        "sources": [
            {"publisher": "Greater Manchester Mental Health NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.gmmh.nhs.uk/annual-reports"},
            {"publisher": "Valuation Office Agency", "title": "Find a business rates valuation (NHS hereditaments)", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "Department for Levelling Up, Housing and Communities", "title": "Business rates — multipliers and reliefs 2024-25", "url": "https://www.gov.uk/introduction-to-business-rates"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "GMMH provider profile (RXV) + Edenfield enforcement", "url": "https://www.cqc.org.uk/provider/RXV"}
        ],
        "related": ["Greater Manchester Mental Health NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Department of Health and Social Care", "Business rates — Sheffield Health and Social Care NHS Foundation Trust", "Valuation Office Agency"]
    },
    "Clinical supplies & services — Tavistock and Portman NHS Foundation Trust": {
        "aliases": [{"name": "Clinical supplies & services", "parent": "Tavistock and Portman NHS Foundation Trust"}],
        "description": "T&P's £0.63M clinical supplies & services line covers psychotherapy + child-and-adolescent specialist clinical consumables — assessment-room equipment, therapy-toolkit consumables, training-clinic materials, observation tooling and specialist gender-services consumables (until the GIDS service closure March 2024 and transfer to NHS England-commissioned regional hubs). T&P is unique among MH FTs as a specialist psychotherapy + training trust without acute inpatient capacity; the consumables profile is therapy-led rather than ward-led.",
        "beneficiaries": "c. 700 staff serving a national catchment for specialist psychotherapy training + adult and family therapy services; c. 18,000 active clinical interactions annually across the Tavistock Centre (NW3) + Gloucester House CAMHS + outpatient + training-clinic streams.",
        "legal_basis": "IAS 2 Inventories · DHSC Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · Public Contracts Regulations 2015 + Procurement Act 2023 (in force Oct 2024)",
        "key_stats": [
            {"label": "Clinical supplies & services 2024-25", "value": "£0.63M"},
            {"label": "Site footprint generating consumption", "value": "Tavistock Centre (Belsize Lane, NW3) + Gloucester House (CAMHS) + outpatient + training-clinic streams"},
            {"label": "Service profile", "value": "No acute inpatient — psychotherapy + family therapy + CAMHS + training; consumables therapy-led not ward-led"},
            {"label": "Composition", "value": "Assessment-room equipment + therapy-toolkit consumables + training-clinic materials + observation tooling + minor specialist instruments"},
            {"label": "GIDS closure context", "value": "Gender Identity Development Service closed Mar 2024 following Cass Review (Apr 2024); replaced by NHS England regional hubs (Royal London Children's Hospital + Alder Hey)"},
            {"label": "Cass Review", "value": "Apr 2024 final report by Dr Hilary Cass — phased closure of GIDS + research-clinic model + new regional service architecture"},
            {"label": "Procurement route", "value": "NHS Supply Chain framework + Crown Commercial Service + minor specialist supplier spot-buy"},
            {"label": "Funding trajectory", "value": "2020-21 c. £0.55M → 2023-24 elevated through GIDS closure transition costs → 2024-25 £0.63M"},
            {"label": "Delivery body", "value": "Trust Procurement + Pharmacy + Estates teams; NHS Supply Chain framework operator"},
            {"label": "Policy owner", "value": "DHSC + NHSE Specialised Commissioning + NCL ICB · NHS Supply Chain governance"},
            {"label": "Evaluation evidence", "value": "Cass Review final report 2024; CQC inspection reports (RNK); trust ARA 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-Cass-Review service architecture · Successor: NHSE-commissioned regional gender-hubs + Tavistock as psychotherapy + training-only specialist trust"}
        ],
        "notes": "T&P's clinical supplies & services line carries a service profile unique among MH FTs — no acute inpatient ward consumables, instead specialist psychotherapy and family-therapy materials, observation tooling for training-clinic supervision and assessment-room equipment. The closure of GIDS in March 2024, following Dr Hilary Cass's April 2024 review, materially changed the trust's service architecture — GIDS clinical-consumables drop out, but T&P retained training-research and broader psychotherapy services. The trust's role as a psychotherapy training institution sustains a higher per-clinical-FTE consumables profile than a typical community-MH peer.",
        "sources": [
            {"publisher": "Tavistock and Portman NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://tavistockandportman.nhs.uk/about-us/publications/annual-reports/"},
            {"publisher": "NHS England", "title": "Independent review of gender identity services for children and young people (Cass Review final report Apr 2024)", "url": "https://cass.independent-review.uk/"},
            {"publisher": "NHS Supply Chain", "title": "Future Operating Model + category framework", "url": "https://www.supplychain.nhs.uk/"},
            {"publisher": "Care Quality Commission", "title": "Tavistock and Portman provider profile (RNK)", "url": "https://www.cqc.org.uk/provider/RNK"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"}
        ],
        "related": ["Tavistock and Portman NHS Foundation Trust", "Clinical Supplies & Drugs", "NHS Mental Health Trusts", "NHS Supply Chain", "Clinical supplies & services — Surrey and Borders Partnership NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Business rates — Devon Partnership NHS Trust": {
        "aliases": [{"name": "Business rates", "parent": "Devon Partnership NHS Trust"}],
        "description": "DPT's £0.62M business-rates charge reflects VOA-set rateable values × 49.9p UBR (small) / 54.6p (standard) on the trust's occupied estate — the Cedars (Exeter), Glenbourne Unit (Plymouth), Langdon Hospital (Dawlish, secure-MH), Wonford House (Exeter, lapsed) and c. 25+ community-MH, CAMHS and addictions bases across Devon. NHS Trusts do not receive charitable exemption; the line is rebased at each VOA revaluation cycle. DPT is the lead provider for adult-MH services across Devon, working alongside Livewell Southwest in Plymouth.",
        "beneficiaries": "Approximately 25+ occupied hereditaments (acute MH wards, secure-MH inpatient, community clinics, CAMHS sites, addictions bases) across Devon's 8 districts plus Plymouth (where DPT shares delivery with Livewell Southwest); serves a registered catchment c. 1.2M.",
        "legal_basis": "Local Government Finance Act 1988 (Schedule 6 valuation) · Non-Domestic Rating (Multipliers and Private Finance) Act 2024 · Non-Domestic Rating Act 2023 · NHS Act 2006 · Health and Care Act 2022 · DHSC GAM 2024-25",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£0.62M"},
            {"label": "Hereditament count", "value": "c. 25+ occupied sites across Devon (incl. 8 districts) + Plymouth"},
            {"label": "Major rated sites", "value": "The Cedars (Exeter) + Glenbourne Unit (Plymouth) + Langdon Hospital (Dawlish, secure-MH) + community bases"},
            {"label": "UBR 2024-25", "value": "49.9p small-multiplier / 54.6p standard-multiplier — frozen at 2023-24 levels under Autumn Statement 2023"},
            {"label": "Charitable exemption", "value": "Not applicable — NHS Trusts are not registered charities under Charities Act 2011"},
            {"label": "Billing authorities", "value": "Devon County 8 districts (Exeter, Mid Devon, North Devon, South Hams, Teignbridge, Torridge, West Devon, East Devon) + Plymouth City + Torbay (3 unitaries)"},
            {"label": "VOA 2023 revaluation impact", "value": "Mixed urban Exeter / Plymouth + rural Devon hereditaments; net broadly neutral; Langdon secure-MH carries higher £/m² RV"},
            {"label": "Rural mileage / RV interaction", "value": "Rural Devon community clinic RVs lower than Exeter / Plymouth core but generate site count"},
            {"label": "NHSPS interaction", "value": "Some community clinic estate held via NHSPS lease; rates passed through to DPT as occupier"},
            {"label": "Funding trajectory", "value": "2020-21 c. £0.5M → 2024-25 £0.62M — tracks UBR + new-site additions"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + VOA + 11 billing authorities"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2017 antecedent valuation date list · Successor: 2026 next revaluation (3-year cycle under NDRA 2023)"}
        ],
        "notes": "DPT's business-rates line is structurally elevated by Langdon Hospital — the medium-secure men's MH inpatient resource at Dawlish carries an above-average rateable value per m² as a custom-built specialist secure facility. The Cedars (Exeter) and Glenbourne Unit (Plymouth) are the two main acute-MH hereditaments, with c. 22 smaller community bases generating residual RV. Multi-billing-authority coverage (8 Devon districts + Plymouth + Torbay) creates administrative complexity. The Autumn Statement 2023 UBR freeze gave a one-year reprieve, but the 2026 revaluation under NDRA 2023's 3-year cycle is expected to rebase upward. NHSPS-leased community clinics pass rates through to DPT under occupier-rule.",
        "sources": [
            {"publisher": "Devon Partnership NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.dpt.nhs.uk/about-us/publications/annual-report"},
            {"publisher": "Valuation Office Agency", "title": "Find a business rates valuation (NHS hereditaments)", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "Department for Levelling Up, Housing and Communities", "title": "Business rates — multipliers and reliefs 2024-25", "url": "https://www.gov.uk/introduction-to-business-rates"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Devon Partnership provider profile (RWV)", "url": "https://www.cqc.org.uk/provider/RWV"}
        ],
        "related": ["Devon Partnership NHS Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Department of Health and Social Care", "Business rates — Greater Manchester Mental Health NHS Foundation Trust", "Valuation Office Agency"]
    },
    "Business rates — Rotherham Doncaster and South Humber NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "Rotherham Doncaster and South Humber NHS Foundation Trust"}],
        "description": "RDaSH's £0.61M business-rates charge reflects VOA-set rateable values × 49.9p UBR (small) / 54.6p (standard) on the trust's occupied estate — Tickhill Road Hospital (Doncaster), Swallownest Court (Sheffield border), Great Oaks (Scunthorpe) and c. 30+ community-MH, CAMHS, LD and addictions bases across Rotherham, Doncaster and North Lincolnshire. NHS FTs do not receive charitable exemption; the line is rebased at each VOA revaluation cycle. RDaSH is one of the more dispersed mid-sized MH-trust footprints in Yorkshire and the Humber.",
        "beneficiaries": "Approximately 30+ occupied hereditaments (acute MH wards, LD inpatient, community clinics, CAMHS sites, addictions bases) across Rotherham, Doncaster + North Lincolnshire (Scunthorpe + Isle of Axholme); serves a registered catchment c. 850,000.",
        "legal_basis": "Local Government Finance Act 1988 (Schedule 6 valuation) · Non-Domestic Rating (Multipliers and Private Finance) Act 2024 · Non-Domestic Rating Act 2023 · NHS Act 2006 · Health and Care Act 2022 · DHSC GAM 2024-25",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£0.61M"},
            {"label": "Hereditament count", "value": "c. 30+ occupied sites across Rotherham + Doncaster + N Lincolnshire"},
            {"label": "Major rated sites", "value": "Tickhill Road Hospital (Doncaster) + Swallownest Court + Great Oaks (Scunthorpe) + community bases"},
            {"label": "UBR 2024-25", "value": "49.9p small-multiplier / 54.6p standard-multiplier — frozen at 2023-24 levels under Autumn Statement 2023"},
            {"label": "Charitable exemption", "value": "Not applicable — NHS FTs are not registered charities under Charities Act 2011"},
            {"label": "Billing authorities", "value": "Rotherham MBC + Doncaster MBC + North Lincolnshire Council (3 unitaries)"},
            {"label": "VOA 2023 revaluation impact", "value": "Mixed Yorkshire / N Lincs commercial RV; net broadly neutral; Tickhill Road custom-built MH hospital carries above-average £/m² RV"},
            {"label": "Cross-ICS context", "value": "Trust crosses South Yorkshire ICB (Rotherham + Doncaster) and Humber and North Yorkshire ICB (N Lincs) boundary — billing-authority engagement spans 2 ICBs"},
            {"label": "NHSPS interaction", "value": "Some community clinic estate held via NHSPS lease; rates passed through to RDaSH as occupier"},
            {"label": "Funding trajectory", "value": "2020-21 c. £0.5M → 2024-25 £0.61M — tracks UBR + new-site additions"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + VOA + 3 unitary billing authorities"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2017 antecedent valuation date list · Successor: 2026 next revaluation (3-year cycle under NDRA 2023)"}
        ],
        "notes": "RDaSH's business-rates line is shaped by an unusual cross-ICS footprint — Rotherham and Doncaster sit in South Yorkshire ICB while North Lincolnshire (Scunthorpe + Isle of Axholme) falls under Humber and North Yorkshire ICB. Tickhill Road Hospital (Doncaster) is the main acute-MH hereditament by RV, with Swallownest Court and Great Oaks (Scunthorpe) carrying meaningful additional RV alongside dozens of community clinics. The Autumn Statement 2023 UBR freeze gave a one-year reprieve, but the 2026 revaluation under NDRA 2023's 3-year cycle is expected to rebase upward. NHSPS-leased community clinics pass rates through to RDaSH under occupier-rule, consistent with the sector-wide service-charge friction.",
        "sources": [
            {"publisher": "Rotherham Doncaster and South Humber NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.rdash.nhs.uk/about-us/publications-and-accounts/"},
            {"publisher": "Valuation Office Agency", "title": "Find a business rates valuation (NHS hereditaments)", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "Department for Levelling Up, Housing and Communities", "title": "Business rates — multipliers and reliefs 2024-25", "url": "https://www.gov.uk/introduction-to-business-rates"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "RDaSH provider profile (RXE)", "url": "https://www.cqc.org.uk/provider/RXE"}
        ],
        "related": ["Rotherham Doncaster and South Humber NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Department of Health and Social Care", "Business rates — Devon Partnership NHS Trust", "Valuation Office Agency"]
    },
}
