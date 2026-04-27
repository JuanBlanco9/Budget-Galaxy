# -*- coding: utf-8 -*-
# Phase 2 Acute slice 2 — chunk 19 (17 NHS Acute Trust orphan sub-lines)
# Hand-curated trust-specific PROGRAMME-archetype enrichment entries.
# Structural contract per docs/archetype_briefs.md.

NEW = {
    "General supplies & services — Bolton NHS Foundation Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "Bolton NHS Foundation Trust"}],
        "description": "Bolton NHS FT's £4.21M general supplies & services line covers non-clinical consumables, linen, catering provisions, hotel-services materials, office and IT consumables, and minor expensed equipment at the single-site Royal Bolton Hospital plus integrated Bolton borough community services. The trust is one of Greater Manchester's high-volume district general hospitals, with one of the busiest single-site EDs in the North West and a major maternity unit, both of which sustain non-clinical consumables baseline above pure-acute peers of similar bed count.",
        "beneficiaries": "c. 5,500 WTE staff serving a c. 290,000 Bolton borough catchment plus referrals from Bury and Salford; c. 130,000 ED attendances/yr at Royal Bolton ED; c. 60,000 admissions/yr; large maternity unit (c. 5,500 deliveries/yr — among GM's busiest); integrated borough community workforce.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 2 Inventories · Procurement Act 2023 · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "General supplies & services 2024-25", "value": "£4.21M"},
            {"label": "Trust scale", "value": "Single acute site (Royal Bolton Hospital, Farnworth) + integrated Bolton community services; c. 5,500 WTE"},
            {"label": "ED throughput", "value": "c. 130,000 attendances/yr — among Greater Manchester's busiest single-site EDs"},
            {"label": "Maternity volume", "value": "c. 5,500 deliveries/yr — high-volume regional maternity unit"},
            {"label": "Procurement route", "value": "NHS Supply Chain national framework + GM Provider Collaborative procurement + trust-direct contracts"},
            {"label": "GM ICS context", "value": "Greater Manchester ICS / NHS GM — strong devolved provider-collaborative procurement scaling vs national peers"},
            {"label": "Industrial action 2023-24 + Apr 2025 NIC", "value": "44 days junior-doctor + 10 days consultant strikes drove agency-backfill churn; Apr 2025 NIC step-up + non-clinical CPI feed forward unit-cost pressure"},
            {"label": "Funding trajectory", "value": "2021-22 c. £3.4M → 2023-24 £3.9M → 2024-25 £4.21M — sustained CPI + activity recovery"},
            {"label": "Delivery body", "value": "Trust Procurement + Supply Chain team + NHS Supply Chain (DHSC ALB) + GM Provider Collaborative procurement"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + NHS Greater Manchester ICB"},
            {"label": "Evaluation evidence", "value": "Model Hospital benchmarks; NHS Supply Chain ARA; Trust ARA 2023-24; CQC inspection (RMC)"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2011 separate Royal Bolton + Bolton PCT community baselines · Successor: GM Provider Collaborative consolidated procurement scaling 2025-30"}
        ],
        "notes": "Bolton's general supplies & services baseline reflects integrated acute + community workforce alongside one of Greater Manchester's highest-volume maternity units — c. 5,500 deliveries/yr drives nappy, sterile-pack, linen and catering consumable demand well above pure-acute DGH peers. NHS Supply Chain remains dominant carrier for national-framework lines, with GM Provider Collaborative scaling collaborative procurement under the devolved NHS GM model. Industrial action 2023-24 drove additional cancellation re-stocking churn and agency-backfill consumable use across acute medicine and surgery. The April 2025 employer-NIC step-up and sustained CPI on non-clinical inputs feed forward unit-cost pressure into the trust's 2025-26 efficiency assumption.",
        "sources": [
            {"publisher": "Bolton NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.boltonft.nhs.uk/about-us/publications/annual-report/"},
            {"publisher": "NHS Supply Chain", "title": "Annual Report 2023-24", "url": "https://www.supplychain.nhs.uk/about-us/our-publications/"},
            {"publisher": "NHS Greater Manchester ICB", "title": "GM Provider Collaborative + procurement scaling", "url": "https://gmintegratedcare.org.uk/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Bolton NHS FT provider profile (RMC)", "url": "https://www.cqc.org.uk/provider/RMC"}
        ],
        "related": ["Bolton NHS Foundation Trust", "Clinical Supplies & Drugs", "NHS Acute Trusts", "NHS Supply Chain", "General supplies & services — Liverpool University Hospitals NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "General supplies & services — County Durham and Darlington NHS Foundation Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "County Durham and Darlington NHS Foundation Trust"}],
        "description": "CDDFT's £4.19M general supplies & services line covers non-clinical consumables, linen, catering provisions, hotel-services materials, office and IT consumables across the trust's multi-site footprint — University Hospital of North Durham, Darlington Memorial Hospital, Bishop Auckland Hospital plus a network of community hospitals across County Durham and Darlington. The dispersed multi-site geography and integrated community-hospital network drive logistics, distribution and hotel-services consumable patterns above single-site DGH peers.",
        "beneficiaries": "c. 7,500 WTE staff serving a c. 650,000 County Durham + Darlington catchment; c. 200,000 ED attendances/yr (Durham + Darlington EDs combined); c. 100,000 admissions/yr; multi-site footprint includes University Hospital of North Durham, Darlington Memorial Hospital, Bishop Auckland Hospital plus community hospitals (Shotley Bridge, Chester-le-Street, Sedgefield, Weardale).",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 2 Inventories · Procurement Act 2023 · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "General supplies & services 2024-25", "value": "£4.19M"},
            {"label": "Trust scale", "value": "Three acute sites (UH North Durham + Darlington Memorial + Bishop Auckland) + community-hospital network; c. 7,500 WTE"},
            {"label": "ED throughput", "value": "c. 200,000 attendances/yr (Durham + Darlington EDs combined)"},
            {"label": "Multi-site logistics driver", "value": "Dispersed County Durham + Darlington geography + community-hospital network drives distribution + hotel-services consumable patterns above single-site DGH peers"},
            {"label": "PFI context", "value": "Bishop Auckland Hospital PFI (signed 1999, operational 2002) — first-wave PFI; soft-FM consumables interact with PFI hotel-services contract"},
            {"label": "Procurement route", "value": "NHS Supply Chain national framework + North East and North Cumbria ICS collaborative + trust-direct contracts"},
            {"label": "Industrial action 2023-24 + Apr 2025 NIC", "value": "44 days junior-doctor + 10 days consultant strikes drove multi-site backfill churn; Apr 2025 NIC step-up + CPI feed forward unit-cost pressure"},
            {"label": "Funding trajectory", "value": "2021-22 c. £3.4M → 2023-24 £3.9M → 2024-25 £4.19M — sustained CPI + multi-site activity recovery"},
            {"label": "Delivery body", "value": "Trust Procurement + Supply Chain team + NHS Supply Chain (DHSC ALB) + NENC ICS procurement collaborative"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + North East and North Cumbria ICB"},
            {"label": "Evaluation evidence", "value": "Model Hospital benchmarks; NAO PFI hand-back report 2020 (Bishop Auckland cohort); Trust ARA 2023-24; CQC inspection (RXP)"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2002 separate North Durham + Darlington trusts (merged 2002) · Successor: NENC ICS collaborative procurement + Bishop Auckland PFI hand-back planning towards 2032"}
        ],
        "notes": "CDDFT's general supplies & services baseline is shaped by its dispersed multi-site footprint across County Durham and Darlington — three acute sites plus a network of community hospitals — driving distribution and hotel-services consumable patterns above single-site DGH peers. The Bishop Auckland Hospital PFI (1999-signed, first-wave) layers PFI soft-FM contract interaction onto trust-managed consumables on that site, with hand-back planning towards 2032 expiry now in scope. NHS Supply Chain remains dominant carrier; NENC ICS collaborative procurement provides regional scaling. Industrial action 2023-24 drove additional cancellation re-stocking churn across multi-site rotas; April 2025 NIC step-up and CPI on non-clinical inputs feed forward unit-cost pressure.",
        "sources": [
            {"publisher": "County Durham and Darlington NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.cddft.nhs.uk/about-us/publications/annual-report-and-accounts.aspx"},
            {"publisher": "NHS Supply Chain", "title": "Annual Report 2023-24", "url": "https://www.supplychain.nhs.uk/about-us/our-publications/"},
            {"publisher": "National Audit Office", "title": "Managing PFI assets and services as contracts end (HC 632, 2020)", "url": "https://www.nao.org.uk/reports/managing-pfi-assets-and-services-as-contracts-end/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "CDDFT provider profile (RXP)", "url": "https://www.cqc.org.uk/provider/RXP"}
        ],
        "related": ["County Durham and Darlington NHS Foundation Trust", "Clinical Supplies & Drugs", "NHS Acute Trusts", "NHS Supply Chain", "General supplies & services — Bolton NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Amortisation — Gloucestershire Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Amortisation", "parent": "Gloucestershire Hospitals NHS Foundation Trust"}],
        "description": "Gloucestershire Hospitals' £4.16M amortisation line is the systematic write-down of capitalised intangible assets — primarily software, EPR (Sunrise / Allscripts then Sunrise EPR rollout), PACS, capitalised software development and licences — under IAS 38 with useful economic lives of 5-10 years per DHSC GAM ch.5. The trust runs Gloucestershire Royal Hospital (Gloucester) and Cheltenham General Hospital under a two-site reconfiguration model. The line scales with NHSE Frontline Digitisation EPR investment and the IFRIC 22 SaaS configuration agenda decision (March 2021).",
        "beneficiaries": "c. 8,500 WTE staff serving a c. 660,000 Gloucestershire catchment; c. 170,000 ED attendances/yr (Gloucester + Cheltenham combined — Cheltenham now Type 1 model after reconfiguration); c. 80,000 admissions/yr; two-site acute footprint plus community-hospital interface.",
        "legal_basis": "IAS 38 Intangible Assets · IFRIC 22 SaaS configuration/customisation costs (March 2021 agenda decision) · DHSC Group Accounting Manual 2024-25 ch.5 · NHS Act 2006 · Health and Care Act 2022 · NHSE Frontline Digitisation programme guidance",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£4.16M"},
            {"label": "Trust scale", "value": "Two acute sites (Gloucestershire Royal + Cheltenham General); c. 8,500 WTE"},
            {"label": "Asset base composition", "value": "Sunrise EPR (Allscripts / Altera) + radiology PACS + capitalised software + capitalised software development; 5-10yr UEL per IAS 38 / DHSC GAM ch.5"},
            {"label": "IFRIC 22 effect", "value": "March 2021 IFRIC SaaS configuration/customisation agenda decision reshaped capitalisation boundary; some costs reclassified opex"},
            {"label": "Frontline Digitisation context", "value": "NHSE Frontline Digitisation funds EPR rollouts to 'core' standard by 2026 — Gloucestershire receiving FD investment for Sunrise rollout"},
            {"label": "Two-site reconfiguration", "value": "Centres of Excellence reconfiguration (Cheltenham + Gloucester specialty consolidation) drives capitalised IT integration costs"},
            {"label": "Industrial action 2023-24 effect", "value": "Strike days had limited direct effect on intangible asset additions but delayed some go-live milestones"},
            {"label": "Funding trajectory", "value": "2021-22 c. £3.2M → 2023-24 £3.7M → 2024-25 £4.16M — sustained intangible-asset additions through Frontline Digitisation"},
            {"label": "Delivery body", "value": "Trust IT + Digital programme office + Allscripts/Altera (Sunrise EPR vendor) + DHSC Frontline Digitisation funding + Gloucestershire ICB digital pillar"},
            {"label": "Policy owner", "value": "DHSC + NHSE Frontline Digitisation + NHSE Provider Finance + NHS Gloucestershire ICB"},
            {"label": "Evaluation evidence", "value": "NHSE Frontline Digitisation programme evaluation; NAO Digital Transformation in the NHS (HC 8, 2020); Trust ARA disclosure; CQC inspection (RTE)"},
            {"label": "Predecessor / successor", "value": "Predecessor: legacy departmental clinical systems · Successor: convergent Sunrise EPR + integrated PACS + AI-clinical-decision modules amortising 2024-2030+"}
        ],
        "notes": "Gloucestershire Hospitals' amortisation line is being reshaped by NHSE Frontline Digitisation — Sunrise EPR (Allscripts / Altera) rollout drives capitalised intangible additions which feed forward into amortisation cycles over IAS 38 / DHSC GAM ch.5 useful-economic-life assumptions of 5-10 years. IFRIC 22 March 2021 SaaS agenda decision reshaped the capitalisation/opex boundary on cloud-platform additions. The two-site Centres of Excellence reconfiguration between Gloucester and Cheltenham drives capitalised IT integration costs as specialty services consolidate. FD 'core' standard target by 2026 sustains forward investment; NAO's 2020 Digital Transformation in the NHS report frames oversight.",
        "sources": [
            {"publisher": "Gloucestershire Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.gloshospitals.nhs.uk/about-us/who-we-are/publications/"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/connecting-health-and-care-providers/frontline-digitisation/"},
            {"publisher": "National Audit Office", "title": "Digital transformation in the NHS (HC 8, 2020)", "url": "https://www.nao.org.uk/reports/the-use-of-digital-technology-in-the-nhs/"},
            {"publisher": "IFRS Foundation / IFRIC", "title": "Configuration or customisation costs in a cloud computing arrangement (IFRIC March 2021 agenda decision)", "url": "https://www.ifrs.org/news-and-events/news/2021/04/ifric-update-march-2021/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 5)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Gloucestershire Hospitals provider profile (RTE)", "url": "https://www.cqc.org.uk/provider/RTE"}
        ],
        "related": ["Gloucestershire Hospitals NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Frontline Digitisation Programme", "Amortisation — Liverpool University Hospitals NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "General supplies & services — Queen Elizabeth Hospital King's Lynn NHS Foundation Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "Queen Elizabeth Hospital King's Lynn NHS Foundation Trust"}],
        "description": "QEH King's Lynn's £4.16M general supplies & services line covers non-clinical consumables, linen, catering, hotel-services materials, office and IT consumables across the single-site DGH serving west Norfolk and the Fens. The trust is one of the most-cited RAAC-affected sites — September 2023 HSSIB list — with the New QEH NHP rebuild scheme designed to replace the failing 1980s plank roof estate, putting consumables baseline in transition between the legacy estate and decant arrangements through 2030 NHP delivery.",
        "beneficiaries": "c. 4,000 WTE staff serving a c. 330,000 west Norfolk + Fens catchment (King's Lynn, Fakenham, Wisbech borders); c. 80,000 ED attendances/yr; c. 40,000 admissions/yr; rural/remote catchment with significant elderly demographic.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 2 Inventories · Procurement Act 2023 · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "General supplies & services 2024-25", "value": "£4.16M"},
            {"label": "Trust scale", "value": "Single acute site (Queen Elizabeth Hospital, King's Lynn); c. 4,000 WTE"},
            {"label": "ED throughput", "value": "c. 80,000 attendances/yr — rural catchment, lower volume but high acuity in elderly cohort"},
            {"label": "RAAC context", "value": "QEH on Sep 2023 HSSIB RAAC list — one of seven worst-affected sites with 'imminent risk of structural failure' designation; >1,500 steel/timber props"},
            {"label": "NHP New QEH scheme", "value": "New Hospital Programme — full rebuild scheme; Jan 2025 NHP Reset confirmed continued delivery for RAAC cohort with completion targeted late 2020s"},
            {"label": "Procurement route + ICS context", "value": "NHS Supply Chain national framework + Norfolk and Waveney ICS collaborative + trust-direct contracts"},
            {"label": "Industrial action 2023-24 + Apr 2025 NIC", "value": "44 days junior-doctor + 10 days consultant strikes drove backfill churn; Apr 2025 NIC step-up + CPI feed forward unit-cost pressure"},
            {"label": "Funding trajectory", "value": "2021-22 c. £3.4M → 2023-24 £3.9M → 2024-25 £4.16M — RAAC-related operational disruption + CPI"},
            {"label": "Delivery body", "value": "Trust Procurement + Supply Chain team + NHS Supply Chain (DHSC ALB) + Norfolk and Waveney ICB procurement"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + NHP team + NHS Norfolk and Waveney ICB"},
            {"label": "Evaluation evidence", "value": "HSSIB RAAC report Sep 2023; NAO New Hospital Programme report (Jul 2023); NHP Reset Jan 2025; Trust ARA"},
            {"label": "Predecessor / successor", "value": "Predecessor: 1980 RAAC-built QEH baseline · Successor: New QEH NHP rebuild operational late 2020s + post-rebuild consolidated procurement footprint"}
        ],
        "notes": "QEH King's Lynn is one of the seven worst-affected RAAC trusts on the September 2023 HSSIB list, with over 1,500 structural props supporting the failing 1980s reinforced-autoclaved-aerated-concrete plank roof — a state DHSC and NHSE designated as 'imminent risk of structural failure' grade. The New QEH rebuild is in the New Hospital Programme RAAC cohort, with the January 2025 NHP Reset confirming continued delivery for the RAAC seven (Hinchingbrooke, QEH King's Lynn, James Paget, Frimley, Airedale, Mid Cheshire, West Suffolk) on a late-2020s completion path. Operational disruption from RAAC remediation and decant arrangements feed into elevated consumable churn alongside national CPI on hotel-services inputs. NHS Supply Chain dominant carrier; Norfolk & Waveney ICS scaling.",
        "sources": [
            {"publisher": "Queen Elizabeth Hospital King's Lynn NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.qehkl.nhs.uk/about-us/key-publications/"},
            {"publisher": "National Audit Office", "title": "Progress with the New Hospital Programme (HC 1662, July 2023)", "url": "https://www.nao.org.uk/reports/the-new-hospital-programme/"},
            {"publisher": "Health Services Safety Investigations Body", "title": "RAAC concrete in NHS hospital estate (Sep 2023)", "url": "https://www.hssib.org.uk/"},
            {"publisher": "NHS Supply Chain", "title": "Annual Report 2023-24", "url": "https://www.supplychain.nhs.uk/about-us/our-publications/"},
            {"publisher": "Care Quality Commission", "title": "QEH King's Lynn provider profile (RCX)", "url": "https://www.cqc.org.uk/provider/RCX"}
        ],
        "related": ["Queen Elizabeth Hospital King's Lynn NHS Foundation Trust", "Clinical Supplies & Drugs", "NHS Acute Trusts", "New Hospital Programme", "General supplies & services — Bolton NHS Foundation Trust", "NHS Supply Chain"]
    },
    "Establishment costs — Sandwell And West Birmingham Hospitals NHS Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "Sandwell And West Birmingham Hospitals NHS Trust"}],
        "description": "SWBH's £4.15M establishment costs line covers postage, telephony, print, recruitment-advertising, training and conferences, subscriptions and legal & professional fees across the trust's footprint at Sandwell General Hospital, City Hospital and (from 2024) the Midland Metropolitan University Hospital (MMUH). The trust's establishment-cost profile is dominated by the May 2024 MMUH opening — the post-Carillion-collapse rebuild of the originally-2018-targeted PFI hospital — driving consolidation, recruitment and migration-related professional-fee spend.",
        "beneficiaries": "c. 7,500 WTE staff serving a c. 530,000 Sandwell + west Birmingham catchment (Smethwick, West Bromwich, Ladywood, Soho); c. 200,000 ED attendances/yr (City + Sandwell EDs pre-MMUH consolidation); c. 100,000 admissions/yr; high IMD deprivation across Sandwell catchment.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25 · Public Contracts Regulations 2015 / Procurement Act 2023",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£4.15M"},
            {"label": "Trust scale", "value": "Two acute sites pre-MMUH (Sandwell General + City Hospital) + Midland Metropolitan University Hospital (opened May 2024); c. 7,500 WTE"},
            {"label": "Composition", "value": "Postage + telephony + print + recruitment-advertising + training + conferences + subscriptions + legal & professional fees"},
            {"label": "MMUH opening context", "value": "Midland Metropolitan University Hospital opened May 2024 — Laing O'Rourke completion of post-Carillion-collapse build; original PFI 2010 cancelled, public-capital rescue route since 2018"},
            {"label": "Carillion 2018 effect", "value": "Carillion's Jan 2018 insolvency abandoned MMUH PFI build with structure 60% complete; sustained legal + professional-fee residue on contract unwinding + Laing O'Rourke novation"},
            {"label": "Industrial action 2023-24", "value": "44 days junior-doctor + 10 days consultant strikes drove agency-engagement + recruitment-advertising professional fees"},
            {"label": "April 2025 NIC + CPI", "value": "Apr 2025 NIC step-up raises forward professional-fee + recruitment-retainer cost; CPI on print/post/conference inputs"},
            {"label": "Funding trajectory", "value": "2021-22 c. £3.3M → 2023-24 £3.9M → 2024-25 £4.15M — MMUH transition drove material professional-fee spike"},
            {"label": "Delivery body", "value": "Trust Corporate Services + HR + Finance + IT + Communications + external counsel + MMUH transition team + Laing O'Rourke project team"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + NHP team + Black Country ICB"},
            {"label": "Evaluation evidence", "value": "NAO Carillion + MMUH completion reports; CQC inspection (RXK); Trust ARA disclosure; Model Hospital corporate-services benchmarks"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-MMUH dual-site Sandwell General + City Hospital establishment baseline · Successor: post-MMUH consolidated single-acute-tower establishment + post-Carillion close-out"}
        ],
        "notes": "SWBH's establishment cost line is in active transition through the May 2024 opening of the Midland Metropolitan University Hospital (MMUH) — the most prominent post-Carillion-collapse rescue rebuild in the NHS, completed by Laing O'Rourke after the original PFI consortium collapse abandoned the 60%-complete structure in January 2018. The transition from dual-site (Sandwell General + City Hospital) to consolidated MMUH operation drove material professional-fee, recruitment-advertising and migration-related establishment spend through 2023-24 into 2024-25. NAO scrutiny of Carillion and MMUH completion shaped governance; April 2025 NIC step-up and CPI feed forward residual cost pressure as post-MMUH consolidated establishment baseline emerges in 2025-26.",
        "sources": [
            {"publisher": "Sandwell and West Birmingham Hospitals NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.swbh.nhs.uk/about-us/publications-and-policies/annual-reports/"},
            {"publisher": "National Audit Office", "title": "Investigation into the rescue of Carillion's PFI hospital contracts", "url": "https://www.nao.org.uk/reports/investigation-into-the-rescue-of-carillions-pfi-hospital-contracts/"},
            {"publisher": "National Audit Office", "title": "Progress with the New Hospital Programme (HC 1662, July 2023)", "url": "https://www.nao.org.uk/reports/the-new-hospital-programme/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "SWBH provider profile (RXK)", "url": "https://www.cqc.org.uk/provider/RXK"}
        ],
        "related": ["Sandwell And West Birmingham Hospitals NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "New Hospital Programme", "Establishment costs — Chelsea and Westminster Hospital NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "General supplies & services — South Tees Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "South Tees Hospitals NHS Foundation Trust"}],
        "description": "South Tees Hospitals' £4.13M general supplies & services line covers non-clinical consumables, linen, catering, hotel-services materials, office and IT consumables across the trust's two-site footprint — James Cook University Hospital (Middlesbrough, c. 1,000 beds) and the Friarage Hospital (Northallerton). James Cook is the regional Major Trauma Centre for the North East and North Yorkshire and a tertiary cardiothoracic centre, sustaining a complex consumable mix across critical care, theatres and inter-hospital transfer support.",
        "beneficiaries": "c. 9,500 WTE staff serving a c. 1.5M Tees Valley + North Yorkshire catchment plus tertiary cardiothoracic + neurosciences referrals; c. 150,000 ED attendances/yr (James Cook + Friarage); c. 100,000 admissions/yr; James Cook = Major Trauma Centre for NENC + NYHT region.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 2 Inventories · Procurement Act 2023 · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "General supplies & services 2024-25", "value": "£4.13M"},
            {"label": "Trust scale", "value": "Two acute sites (James Cook University Hospital + Friarage Hospital); c. 9,500 WTE"},
            {"label": "Major Trauma Centre", "value": "James Cook = North East & N Yorkshire MTC — drives critical-care + theatre consumable mix"},
            {"label": "Tertiary specialty", "value": "Regional cardiothoracic + neurosciences + spinal injuries centre — broadens consumable mix vs DGH peers"},
            {"label": "Procurement route", "value": "NHS Supply Chain national framework + North East and North Cumbria ICS collaborative + trust-direct contracts"},
            {"label": "PFI context", "value": "James Cook PFI signed 1998 (first-wave), operational 2003 — soft-FM consumables interact with PFI hotel-services contract"},
            {"label": "Industrial action 2023-24 + Apr 2025 NIC", "value": "44 days junior-doctor + 10 days consultant strikes drove backfill churn at MTC; Apr 2025 NIC step-up + CPI feed forward unit-cost pressure"},
            {"label": "Funding trajectory", "value": "2021-22 c. £3.4M → 2023-24 £3.8M → 2024-25 £4.13M — sustained CPI + tertiary-activity recovery"},
            {"label": "Delivery body", "value": "Trust Procurement + Supply Chain team + NHS Supply Chain (DHSC ALB) + NENC ICS procurement collaborative"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + NHS North East and North Cumbria ICB"},
            {"label": "Evaluation evidence", "value": "Model Hospital benchmarks; NAO PFI hand-back report 2020 (James Cook cohort); Trust ARA 2023-24; CQC inspection (RTR)"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2002 separate South Tees + Northallerton hospital baselines · Successor: NENC ICS collaborative procurement + James Cook PFI hand-back planning towards 2033"}
        ],
        "notes": "South Tees' general supplies & services baseline is shaped by James Cook University Hospital's role as the North East's Major Trauma Centre and regional tertiary cardiothoracic, neurosciences and spinal injuries centre — a specialty mix that broadens critical-care, theatre and hotel-services consumable demand above pure-DGH peers. The James Cook PFI (1998-signed, first-wave) layers PFI soft-FM contract interaction onto trust-managed consumables on that site, with hand-back planning towards 2033 expiry now in scope. NHS Supply Chain remains dominant carrier; NENC ICS collaborative procurement provides regional scaling. Industrial action 2023-24 had a high impact on this MTC site. April 2025 NIC step-up and CPI feed forward unit-cost pressure.",
        "sources": [
            {"publisher": "South Tees Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.southtees.nhs.uk/about/publications/"},
            {"publisher": "NHS Supply Chain", "title": "Annual Report 2023-24", "url": "https://www.supplychain.nhs.uk/about-us/our-publications/"},
            {"publisher": "National Audit Office", "title": "Managing PFI assets and services as contracts end (HC 632, 2020)", "url": "https://www.nao.org.uk/reports/managing-pfi-assets-and-services-as-contracts-end/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "South Tees provider profile (RTR)", "url": "https://www.cqc.org.uk/provider/RTR"}
        ],
        "related": ["South Tees Hospitals NHS Foundation Trust", "Clinical Supplies & Drugs", "NHS Acute Trusts", "NHS Supply Chain", "General supplies & services — County Durham and Darlington NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Transport (business + patient) — Maidstone And Tunbridge Wells NHS Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "Maidstone And Tunbridge Wells NHS Trust"}],
        "description": "MTW's £4.12M transport line covers business mileage, inter-site patient transfers between Maidstone Hospital and Tunbridge Wells Hospital (the latter a 2011-opened PFI), and Non-Emergency Patient Transport Services across the trust's west Kent footprint. The two-site clinical model with split specialty configuration (Tunbridge Wells = trauma + urology + maternity; Maidstone = oncology + cardiac) sustains substantial inter-site clinical-staff and patient-transfer demand. South East Coast Ambulance Service and accredited PTS contractors are primary carriers.",
        "beneficiaries": "c. 6,000 WTE staff serving a c. 580,000 west Kent catchment (Maidstone, Tunbridge Wells, Tonbridge, Sevenoaks); c. 130,000 ED attendances/yr (Tunbridge Wells main ED + Maidstone urgent treatment); c. 70,000 admissions/yr; specialty-split between sites drives inter-site transfer demand.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · IFRS 16 Leases (pool fleet) · NHS Act 2006 · Mental Health Act 1983 (s.135/136 conveyance) · NHSE Patient Transport Services Eligibility Framework 2022 · HMRC AMAP · NHS AfC Section 17",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£4.12M"},
            {"label": "Trust scale", "value": "Two acute sites (Maidstone Hospital + Tunbridge Wells Hospital); c. 6,000 WTE"},
            {"label": "Specialty split", "value": "Tunbridge Wells = trauma + urology + maternity ED; Maidstone = oncology + cardiac — split-site model drives inter-site transfer demand"},
            {"label": "Tunbridge Wells PFI", "value": "Tunbridge Wells Hospital PFI opened 2011 — modern facility hotel-services consumes related transport"},
            {"label": "PTS provider mix", "value": "South East Coast Ambulance Service NHS FT (SECAmb) + accredited NEPTS contractors — re-tendered via Kent and Medway ICS"},
            {"label": "Staff mileage rate", "value": "NHS Agenda for Change Section 17 / HMRC AMAP 45p first 10,000 miles + 25p thereafter"},
            {"label": "Pool fleet + industrial action 2023-24", "value": "IFRS 16 right-of-use depreciation on leased pool vehicles for AHPs + community teams; strike days drove ad-hoc inter-site transfers + locum mileage claims across split-site rotas"},
            {"label": "Funding trajectory", "value": "2021-22 c. £3.3M → 2023-24 £3.8M → 2024-25 £4.12M — fuel CPI + activity recovery + split-site demand"},
            {"label": "Delivery body", "value": "Trust E&F + Travel team + SECAmb PTS + accredited NEPTS contractors + Kent and Medway ICS PTS commissioning"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + NHSE Ambulance + NHS Kent and Medway ICB"},
            {"label": "Evaluation evidence", "value": "NHSE PTS Eligibility Framework 2022; Kent and Medway ICS PTS recommissioning; Trust ARA disclosure; CQC inspection (RWF)"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2011 pre-Tunbridge Wells PFI dual-site model · Successor: K&M ICS PTS recommissioning + ongoing inter-site clinical-flow optimisation"}
        ],
        "notes": "MTW's transport line is shaped by the trust's split-site clinical configuration — Tunbridge Wells Hospital (2011 PFI opening) hosts trauma, urology and maternity while Maidstone hosts oncology and cardiac, sustaining substantial inter-site clinical-staff and patient-transfer demand on top of standard NEPTS eligibility throughput. South East Coast Ambulance Service operates as primary PTS carrier alongside accredited NEPTS contractors recommissioned through Kent and Medway ICS. NHS AfC Section 17 / HMRC AMAP staff mileage rate caps unit-rate, with fuel CPI and split-site activity recovery driving 2023-25 trajectory. Industrial action 2023-24 drove ad-hoc inter-site transfers and locum mileage claims.",
        "sources": [
            {"publisher": "Maidstone and Tunbridge Wells NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.mtw.nhs.uk/about-us/publications/annual-reports/"},
            {"publisher": "NHS England", "title": "Patient Transport Services Eligibility Framework 2022", "url": "https://www.england.nhs.uk/publication/non-emergency-patient-transport-services-nepts/"},
            {"publisher": "South East Coast Ambulance Service NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.secamb.nhs.uk/about-us/publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "MTW provider profile (RWF)", "url": "https://www.cqc.org.uk/provider/RWF"}
        ],
        "related": ["Maidstone And Tunbridge Wells NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "South East Coast Ambulance Service NHS Foundation Trust", "Transport (business + patient) — Liverpool University Hospitals NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "General supplies & services — King’s College Hospital NHS Foundation Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "King’s College Hospital NHS Foundation Trust"}],
        "description": "King's College Hospital's £4.12M general supplies & services line covers non-clinical consumables, linen, catering, hotel-services materials, office and IT consumables across the trust's two-site academic acute footprint — Denmark Hill (south-east London) and Princess Royal University Hospital (Orpington, Bromley). King's is one of London's two liver-transplant centres, a Major Trauma Centre and a tertiary neurosciences/cardiac/haematology hub, sustaining a complex consumable mix across critical care, theatres and tertiary specialty interfaces.",
        "beneficiaries": "c. 14,000 WTE staff serving a c. 700,000 south-east London + Bromley catchment plus tertiary national + international referrals (liver, neuro, cardiac, haem); c. 280,000 ED attendances/yr (Denmark Hill + PRUH combined); c. 130,000 admissions/yr; Denmark Hill = London MTC + national liver-transplant centre.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 2 Inventories · Procurement Act 2023 · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "General supplies & services 2024-25", "value": "£4.12M"},
            {"label": "Trust scale", "value": "Two academic acute sites (Denmark Hill + Princess Royal University Hospital, Orpington); c. 14,000 WTE"},
            {"label": "Major Trauma Centre", "value": "Denmark Hill = one of London's four MTCs — drives critical-care + theatre consumable mix"},
            {"label": "National specialty centre", "value": "Liver transplant + tertiary neurosciences + cardiac + haematology — broadens consumable mix vs DGH peers"},
            {"label": "Procurement route", "value": "NHS Supply Chain national framework + South East London ICS collaborative + trust-direct contracts (specialty consumables)"},
            {"label": "King's Health Partners AHSC context", "value": "King's Health Partners academic health-science partnership with GSTT + SLAM + KCL — joint procurement + research-trial consumables"},
            {"label": "Industrial action 2023-24 + Apr 2025 NIC", "value": "44 days junior-doctor + 10 days consultant strikes drove backfill churn at MTC + tertiary site; Apr 2025 NIC step-up + CPI feed forward unit-cost pressure"},
            {"label": "Funding trajectory", "value": "2021-22 c. £3.3M → 2023-24 £3.8M → 2024-25 £4.12M — sustained CPI + tertiary-activity recovery; trust under recovery-support oversight (CFP cohort)"},
            {"label": "Delivery body", "value": "Trust Procurement + Supply Chain team + NHS Supply Chain (DHSC ALB) + SEL ICS procurement collaborative + KHP joint procurement"},
            {"label": "Policy owner", "value": "NHSE Provider Finance (recovery-support oversight) + DHSC + NHS South East London ICB"},
            {"label": "Evaluation evidence", "value": "Model Hospital benchmarks; CQC inspection (RJZ); NHSE Recovery Support Programme oversight; Trust ARA 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2013 PRUH acquisition baseline (KCH acquired PRUH from SLHT 2013) · Successor: SEL ICS collaborative + KHP joint procurement scaling 2025-30"}
        ],
        "notes": "King's College Hospital's general supplies & services baseline reflects its academic + Major Trauma Centre + national specialty centre profile (liver transplant, tertiary neurosciences, cardiac, haematology) — driving critical-care, theatre and research-grade consumable demand well above pure-DGH peers. The 2013 acquisition of Princess Royal University Hospital (Orpington) from the dissolved South London Healthcare Trust extended the footprint into Bromley; the trust has been in NHSE recovery-support programme oversight since 2018-19 financial deterioration. King's Health Partners academic health-science partnership with GSTT, SLaM and KCL frames joint procurement. Industrial action 2023-24 had high impact; April 2025 NIC step-up and CPI feed forward.",
        "sources": [
            {"publisher": "King's College Hospital NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.kch.nhs.uk/about/corporate/annual-report"},
            {"publisher": "NHS Supply Chain", "title": "Annual Report 2023-24", "url": "https://www.supplychain.nhs.uk/about-us/our-publications/"},
            {"publisher": "NHS England", "title": "Recovery Support Programme oversight", "url": "https://www.england.nhs.uk/publication/recovery-support-programme/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "King's College Hospital provider profile (RJZ)", "url": "https://www.cqc.org.uk/provider/RJZ"}
        ],
        "related": ["King’s College Hospital NHS Foundation Trust", "Clinical Supplies & Drugs", "NHS Acute Trusts", "NHS Supply Chain", "General supplies & services — South Tees Hospitals NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Transport (business + patient) — Liverpool University Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "Liverpool University Hospitals NHS Foundation Trust"}],
        "description": "LUHFT's £4.10M transport line covers business mileage, inter-site patient transfers between Royal Liverpool, Aintree and Broadgreen, and Non-Emergency Patient Transport Services across the Cheshire & Merseyside ICS catchment. The October 2022 opening of the New Royal Liverpool University Hospital reshaped inter-site clinical-flow patterns; North West Ambulance Service is the primary PTS carrier alongside accredited NEPTS contractors recommissioned via Cheshire & Merseyside ICS PTS framework.",
        "beneficiaries": "c. 13,500 WTE staff serving a c. 1.5M Cheshire & Merseyside catchment; c. 250,000 ED attendances/yr across Royal Liverpool + Aintree EDs (two of the highest-volume EDs in Northwest England); c. 130,000 elective + day-case admissions/yr; three-site footprint plus community-clinic interface drives sustained inter-site transfer demand.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · IFRS 16 Leases (pool fleet) · NHS Act 2006 · Mental Health Act 1983 (s.135/136 conveyance) · NHSE Patient Transport Services Eligibility Framework 2022 · HMRC AMAP · NHS AfC Section 17",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£4.10M"},
            {"label": "Trust scale", "value": "Three-site acute (Royal Liverpool + Aintree + Broadgreen) post-2019 merger; c. 13,500 WTE"},
            {"label": "ED throughput", "value": "c. 250,000 ED attendances/yr (Royal + Aintree combined — among highest Northwest)"},
            {"label": "New Royal context", "value": "New Royal Liverpool University Hospital opened Oct 2022 after Carillion 2018 collapse — reshaped inter-site clinical-flow + PTS demand patterns"},
            {"label": "PTS provider mix", "value": "North West Ambulance Service NHS Trust (NWAS) + accredited NEPTS contractors — re-tendered via Cheshire & Merseyside ICS PTS framework"},
            {"label": "Staff mileage rate", "value": "NHS Agenda for Change Section 17 / HMRC AMAP 45p first 10,000 miles + 25p thereafter"},
            {"label": "Pool fleet + industrial action 2023-24", "value": "IFRS 16 right-of-use depreciation on leased pool vehicles for AHPs + community teams; 44 days junior-doctor + 10 days consultant strikes drove ad-hoc inter-site transfers + locum mileage claims"},
            {"label": "Funding trajectory", "value": "2021-22 c. £3.2M → 2023-24 £3.8M → 2024-25 £4.10M — fuel CPI + activity recovery + post-merger inter-site flow"},
            {"label": "Delivery body", "value": "Trust E&F + Travel team + NWAS PTS + accredited NEPTS contractors + Cheshire & Merseyside ICS PTS commissioning"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + NHSE Ambulance + NHS Cheshire and Merseyside ICB"},
            {"label": "Evaluation evidence", "value": "NHSE PTS Eligibility Framework 2022; Cheshire & Merseyside ICS PTS recommissioning; Trust ARA disclosure; CQC inspection (REM)"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2019 separate Royal Liverpool + Aintree transport baselines · Successor: full-merger consolidated logistics + ICS PTS framework scaling"}
        ],
        "notes": "LUHFT's transport line is shaped by the trust's three-site geography and the October 2022 opening of the New Royal Liverpool University Hospital — the post-Carillion-collapse rebuild completed by Laing O'Rourke — which reshaped inter-site clinical-flow patterns between Royal Liverpool, Aintree and Broadgreen. North West Ambulance Service operates as primary PTS carrier alongside accredited NEPTS contractors recommissioned through Cheshire & Merseyside ICS PTS framework. Industrial action 2023-24 drove ad-hoc inter-site transfers and locum mileage claims. NHS AfC Section 17 / HMRC AMAP staff mileage rate caps unit-rate; fuel CPI and post-merger flow drove the 2023-25 trajectory. IFRS 16 pool-fleet right-of-use depreciation forms a smaller IFRS-presented sub-component.",
        "sources": [
            {"publisher": "Liverpool University Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.liverpoolft.nhs.uk/about-us/our-publications/"},
            {"publisher": "NHS England", "title": "Patient Transport Services Eligibility Framework 2022", "url": "https://www.england.nhs.uk/publication/non-emergency-patient-transport-services-nepts/"},
            {"publisher": "North West Ambulance Service NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.nwas.nhs.uk/about-us/publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "LUHFT provider profile (REM)", "url": "https://www.cqc.org.uk/provider/REM"}
        ],
        "related": ["Liverpool University Hospitals NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "North West Ambulance Service NHS Trust", "Transport (business + patient) — Maidstone And Tunbridge Wells NHS Trust", "Department of Health and Social Care"]
    },
    "Social security & levy — Southport And Ormskirk Hospital NHS Trust": {
        "aliases": [{"name": "Social security & levy", "parent": "Southport And Ormskirk Hospital NHS Trust"}],
        "description": "Southport & Ormskirk's £4.10M social security & levy line covers employer NIC and Apprenticeship Levy on the trust's c. 3,200-WTE pay bill across the two-site Southport DGH + Ormskirk District General Hospital footprint. The trust is in active vertical-integration transaction — confirmed July 2024 dissolution and merger to create Mersey and West Lancashire Teaching Hospitals NHS Trust with St Helens & Knowsley Teaching Hospitals — reshaping the medium-term workforce-cost reporting boundary. April 2025 NIC step-up dominates forward picture.",
        "beneficiaries": "c. 3,200 WTE staff serving a c. 260,000 Sefton + West Lancashire catchment (Southport, Formby, Ormskirk, Skelmersdale); c. 90,000 ED attendances/yr (Southport ED + Ormskirk Children's ED); c. 40,000 admissions/yr; Ormskirk = regional Children's ED for West Lancs / South Sefton.",
        "legal_basis": "Social Security Contributions and Benefits Act 1992 (employer NIC) · Apprenticeship Levy (Finance Act 2016, s.99) · DHSC Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "Social security & levy 2024-25", "value": "£4.10M"},
            {"label": "Trust scale", "value": "Two-site DGH (Southport + Ormskirk District General); c. 3,200 WTE"},
            {"label": "Composition", "value": "Employer NIC (Class 1 secondary) + Apprenticeship Levy (0.5% of pay bill > £3M)"},
            {"label": "April 2025 NIC step-up", "value": "Rate 13.8% → 15.0% + secondary threshold £9,100 → £5,000; partial NHSE compensation flowing through Cheshire & Merseyside ICB"},
            {"label": "Merger transaction", "value": "Southport & Ormskirk dissolved Jul 2024 into Mersey and West Lancashire Teaching Hospitals NHS Trust (with St Helens & Knowsley); 2024-25 is the final standalone reporting year"},
            {"label": "Children's ED + industrial action 2023-24", "value": "Ormskirk = regional Children's ED for West Lancs / South Sefton; 44 days junior-doctor + 10 days consultant strikes drove agency + overtime backfill, lifting NIC base"},
            {"label": "Apprenticeship Levy", "value": "0.5% of pay bill > £3M — c. £1.0-1.3M/yr at this trust scale"},
            {"label": "Funding trajectory", "value": "2021-22 c. £3.4M → 2023-24 £3.8M → 2024-25 £4.10M; 2025-26 reported under new MWL Trust entity"},
            {"label": "Delivery body", "value": "Trust HR + Payroll + (post-merger) MWL Teaching Hospitals consolidated functions + NHSBSA + HMRC remittance"},
            {"label": "Policy owner", "value": "HM Treasury (NIC + Levy) + DHSC + NHSE Workforce + NHS Cheshire and Merseyside ICB"},
            {"label": "Evaluation evidence", "value": "CQC inspection (RVY); NHSE workforce returns; MWL merger business case; OBR EFO NIC line; Trust ARA"},
            {"label": "Predecessor / successor", "value": "Predecessor: standalone Southport & Ormskirk pre-July 2024 · Successor: Mersey and West Lancashire Teaching Hospitals NHS Trust (with St Helens & Knowsley) consolidated workforce baseline"}
        ],
        "notes": "Southport & Ormskirk's 2024-25 is the final standalone reporting year before dissolution and merger into Mersey and West Lancashire Teaching Hospitals NHS Trust (with St Helens & Knowsley) confirmed July 2024 — completing a long vertical-integration trajectory under the Cheshire & Merseyside ICS provider-collaborative model. The two-site footprint (Southport DGH + Ormskirk with regional Children's ED) sustains a paediatric-skewed workforce profile. Industrial action 2023-24 drove agency and overtime backfill. The April 2025 employer-NIC step-up to 15% with threshold drop to £5,000 is the dominant forward-cost driver; partial NHSE NIC compensation flows through C&M ICB. From 2025-26 the line consolidates under MWL Teaching Hospitals.",
        "sources": [
            {"publisher": "Southport and Ormskirk Hospital NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.southportandormskirk.nhs.uk/about-us/publications/"},
            {"publisher": "Mersey and West Lancashire Teaching Hospitals NHS Trust", "title": "Trust merger transaction (July 2024)", "url": "https://www.mwl.nhs.uk/"},
            {"publisher": "HM Revenue and Customs", "title": "Employer NIC rates and thresholds 2025-26", "url": "https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2025-to-2026"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Southport & Ormskirk provider profile (RVY)", "url": "https://www.cqc.org.uk/provider/RVY"}
        ],
        "related": ["Southport And Ormskirk Hospital NHS Trust", "Staff Costs", "NHS Acute Trusts", "Mersey and West Lancashire Teaching Hospitals NHS Trust", "Apprenticeship Levy", "HM Revenue and Customs"]
    },
    "Amortisation — Lewisham and Greenwich NHS Trust": {
        "aliases": [{"name": "Amortisation", "parent": "Lewisham and Greenwich NHS Trust"}],
        "description": "Lewisham and Greenwich NHS Trust's £4.09M amortisation line is the systematic write-down of capitalised intangible assets — primarily software, EPR, PACS, capitalised software development and licences — under IAS 38 with useful economic lives of 5-10 years per DHSC GAM ch.5. The trust runs University Hospital Lewisham and Queen Elizabeth Hospital Woolwich (formed 2013 from former South London Healthcare Trust dissolution). The line scales with NHSE Frontline Digitisation EPR investment and the IFRIC 22 SaaS configuration agenda decision (March 2021).",
        "beneficiaries": "c. 6,500 WTE staff serving a c. 530,000 Lewisham + Greenwich + Bexley borough catchment; c. 200,000 ED attendances/yr (Lewisham + QEH Woolwich combined); c. 90,000 admissions/yr; QEH Woolwich = high IMD deprivation catchment driving emergency-care + maternity demand.",
        "legal_basis": "IAS 38 Intangible Assets · IFRIC 22 SaaS configuration/customisation costs (March 2021 agenda decision) · DHSC Group Accounting Manual 2024-25 ch.5 · NHS Act 2006 · Health and Care Act 2022 · NHSE Frontline Digitisation programme guidance",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£4.09M"},
            {"label": "Trust scale", "value": "Two acute sites (University Hospital Lewisham + Queen Elizabeth Hospital Woolwich); c. 6,500 WTE"},
            {"label": "Asset base composition", "value": "EPR (Allscripts Sunrise / Oracle Health Millennium pathway) + radiology PACS + capitalised software + capitalised software development; 5-10yr UEL per IAS 38 / DHSC GAM ch.5"},
            {"label": "IFRIC 22 effect", "value": "March 2021 IFRIC SaaS configuration/customisation agenda decision reshaped capitalisation boundary; some costs reclassified opex"},
            {"label": "Frontline Digitisation context", "value": "NHSE Frontline Digitisation funds EPR rollouts to 'core' standard by 2026 — LGT receiving FD investment"},
            {"label": "QEH Woolwich PFI context", "value": "QEH Woolwich PFI signed 1998, operational 2001 — first-wave PFI; capitalised IT integration interacts with PFI estate envelope"},
            {"label": "SLHT 2013 dissolution legacy", "value": "Trust formed Oct 2013 from dissolution of South London Healthcare Trust; legacy asset transfers + revaluations shape amortisation profile"},
            {"label": "Funding trajectory", "value": "2021-22 c. £3.2M → 2023-24 £3.7M → 2024-25 £4.09M — sustained intangible-asset additions through Frontline Digitisation"},
            {"label": "Delivery body", "value": "Trust IT + Digital programme office + EPR vendor + DHSC Frontline Digitisation funding + South East London ICB digital pillar"},
            {"label": "Policy owner", "value": "DHSC + NHSE Frontline Digitisation + NHSE Provider Finance + NHS South East London ICB"},
            {"label": "Evaluation evidence", "value": "NHSE Frontline Digitisation programme evaluation; NAO Digital Transformation in the NHS (HC 8, 2020); Trust ARA disclosure; CQC inspection (RJ2)"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-Oct 2013 South London Healthcare Trust + Lewisham Healthcare separate baselines · Successor: convergent FD-funded EPR + integrated PACS amortising 2024-2030+"}
        ],
        "notes": "Lewisham and Greenwich's amortisation line reflects intangible-asset additions in the post-2013 era — the trust formed October 2013 from dissolution of the failing South London Healthcare Trust (QEH Woolwich joining Lewisham Healthcare) and continues to absorb legacy asset-transfer and revaluation effects. The QEH Woolwich PFI (1998-signed, first-wave) layers PFI estate envelope on capitalised IT integration. NHSE Frontline Digitisation programme drives EPR-related intangible additions over IAS 38 / DHSC GAM ch.5 useful-economic-life assumptions of 5-10 years. IFRIC 22 March 2021 reshaped capitalisation/opex boundary; NAO's 2020 Digital Transformation in the NHS report frames oversight.",
        "sources": [
            {"publisher": "Lewisham and Greenwich NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.lewishamandgreenwich.nhs.uk/about-us/our-publications/"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/connecting-health-and-care-providers/frontline-digitisation/"},
            {"publisher": "National Audit Office", "title": "Digital transformation in the NHS (HC 8, 2020)", "url": "https://www.nao.org.uk/reports/the-use-of-digital-technology-in-the-nhs/"},
            {"publisher": "IFRS Foundation / IFRIC", "title": "Configuration or customisation costs in a cloud computing arrangement (IFRIC March 2021 agenda decision)", "url": "https://www.ifrs.org/news-and-events/news/2021/04/ifric-update-march-2021/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 5)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Lewisham and Greenwich provider profile (RJ2)", "url": "https://www.cqc.org.uk/provider/RJ2"}
        ],
        "related": ["Lewisham and Greenwich NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Frontline Digitisation Programme", "Amortisation — Gloucestershire Hospitals NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Establishment costs — Chelsea and Westminster Hospital NHS Foundation Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "Chelsea and Westminster Hospital NHS Foundation Trust"}],
        "description": "Chelsea and Westminster's £4.07M establishment costs line covers postage, telephony, print, recruitment-advertising, training and conferences, subscriptions and legal & professional fees across the trust's two-site footprint — Chelsea and Westminster Hospital (Fulham Road, PFI-built) and West Middlesex University Hospital (Isleworth, PFI-built). The trust's establishment-cost profile reflects sustained PFI contract-management, professional-fee residue from the dual-PFI estate and recruitment churn across high-cost-of-living north-west London catchment.",
        "beneficiaries": "c. 6,500 WTE staff serving a c. 1.0M north-west and inner-west London catchment (Hammersmith, Fulham, Wandsworth, Hounslow, Richmond); c. 280,000 ED attendances/yr (Chelsea + West Mid combined); c. 90,000 admissions/yr; large maternity (c. 8,000 deliveries/yr) + national HIV/sexual-health centre (56 Dean Street outpatient).",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25 · Public Contracts Regulations 2015 / Procurement Act 2023",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£4.07M"},
            {"label": "Trust scale", "value": "Two-site academic acute (Chelsea & Westminster + West Middlesex University Hospital); c. 6,500 WTE"},
            {"label": "Composition", "value": "Postage + telephony + print + recruitment-advertising + training + conferences + subscriptions + legal & professional fees"},
            {"label": "Dual-PFI context", "value": "Both sites PFI-built — Chelsea (1993, original Wessex Health PFI) + West Middlesex (operational 2003); sustained PFI contract-management professional fees on both estates"},
            {"label": "Specialty profile", "value": "Large maternity (c. 8,000 deliveries/yr) + national HIV/sexual-health centre (56 Dean Street) — drives specialty-recruitment + professional-fee patterns"},
            {"label": "Industrial action 2023-24 + Apr 2025 NIC", "value": "44 days junior-doctor + 10 days consultant strikes drove agency + recruitment-advertising fees; Apr 2025 NIC step-up + CPI feed forward"},
            {"label": "London cost-of-living premium", "value": "Inner-west London recruitment + retention drives advertising + agency-fee premium vs national peers"},
            {"label": "Funding trajectory", "value": "2021-22 c. £3.2M → 2023-24 £3.8M → 2024-25 £4.07M — sustained recruitment churn + dual-PFI contract management"},
            {"label": "Delivery body", "value": "Trust Corporate Services + HR + Finance + IT + Communications + external counsel + dual PFI contract-management teams"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + NHS North West London ICB + IPA PFI Hand-Back unit"},
            {"label": "Evaluation evidence", "value": "Model Hospital corporate-services benchmarks; NAO PFI hand-back report 2020 (Chelsea + West Mid both in early-expiry cohort); Trust ARA; CQC inspection (RQM)"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2015 Chelsea & Westminster standalone (West Mid acquired Sep 2015) · Successor: NWL ICB shared corporate-services + dual-PFI hand-back planning"}
        ],
        "notes": "Chelsea and Westminster's establishment cost line reflects the two-site footprint following the September 2015 acquisition of West Middlesex University Hospital — both sites PFI-built (Chelsea 1993 original Wessex Health PFI; West Mid operational 2003) sustaining dual PFI contract-management and professional-fee residue. The trust's specialty mix — c. 8,000 maternity deliveries/yr and the national HIV/sexual-health centre at 56 Dean Street — drives specialty-recruitment churn alongside inner-west London cost-of-living premium on agency and advertising fees. Industrial action 2023-24 drove agency + recruitment-advertising spend. NAO's 2020 PFI hand-back report flagged early-expiry planning. April 2025 NIC + CPI feed forward.",
        "sources": [
            {"publisher": "Chelsea and Westminster Hospital NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.chelwest.nhs.uk/about-us/publications/annual-reports-and-accounts"},
            {"publisher": "National Audit Office", "title": "Managing PFI assets and services as contracts end (HC 632, 2020)", "url": "https://www.nao.org.uk/reports/managing-pfi-assets-and-services-as-contracts-end/"},
            {"publisher": "Infrastructure and Projects Authority", "title": "PFI Hand-Back Resource Centre", "url": "https://www.gov.uk/government/collections/pfi-and-pf2"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Chelsea and Westminster provider profile (RQM)", "url": "https://www.cqc.org.uk/provider/RQM"}
        ],
        "related": ["Chelsea and Westminster Hospital NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Establishment costs — Sandwell And West Birmingham Hospitals NHS Trust", "PFI / LIFT charges — Chelsea and Westminster Hospital NHS Foundation Trust", "Infrastructure and Projects Authority"]
    },
    "Amortisation — Homerton Healthcare NHS Foundation Trust": {
        "aliases": [{"name": "Amortisation", "parent": "Homerton Healthcare NHS Foundation Trust"}],
        "description": "Homerton Healthcare's £4.07M amortisation line is the systematic write-down of capitalised intangible assets — primarily software, EPR, PACS, capitalised software development and licences — under IAS 38 with useful economic lives of 5-10 years per DHSC GAM ch.5. The trust runs Homerton University Hospital (Hackney) plus integrated Hackney + City community services. The line scales with NHSE Frontline Digitisation EPR investment and the IFRIC 22 SaaS configuration agenda decision (March 2021).",
        "beneficiaries": "c. 3,500 WTE staff serving a c. 280,000 Hackney + City of London catchment plus regional neonatal referrals; c. 130,000 ED attendances/yr at Homerton ED; c. 50,000 admissions/yr; large maternity unit (c. 6,000 deliveries/yr) + tertiary neonatal centre; integrated borough community workforce.",
        "legal_basis": "IAS 38 Intangible Assets · IFRIC 22 SaaS configuration/customisation costs (March 2021 agenda decision) · DHSC Group Accounting Manual 2024-25 ch.5 · NHS Act 2006 · Health and Care Act 2022 · NHSE Frontline Digitisation programme guidance",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£4.07M"},
            {"label": "Trust scale", "value": "Single acute site (Homerton University Hospital, Hackney) + integrated Hackney + City community services; c. 3,500 WTE"},
            {"label": "Asset base composition", "value": "Cerner Millennium / Oracle Health EPR + radiology PACS + capitalised software + capitalised software development; 5-10yr UEL per IAS 38 / DHSC GAM ch.5"},
            {"label": "IFRIC 22 effect", "value": "March 2021 IFRIC SaaS configuration/customisation agenda decision reshaped capitalisation boundary; some costs reclassified opex"},
            {"label": "Frontline Digitisation context", "value": "NHSE Frontline Digitisation funds EPR rollouts to 'core' standard by 2026 — Homerton receiving FD investment"},
            {"label": "Specialty profile", "value": "Large maternity (c. 6,000 deliveries/yr) + tertiary neonatal centre — drives specialty-software capitalisation (BadgerNet maternity + neonatal systems)"},
            {"label": "NEL acute provider collaborative", "value": "Homerton in North East London ICS acute provider collaborative (with Barts Health + BHRUT) — joint-procurement digital scaling"},
            {"label": "Funding trajectory", "value": "2021-22 c. £3.2M → 2023-24 £3.7M → 2024-25 £4.07M — sustained intangible-asset additions through Frontline Digitisation"},
            {"label": "Delivery body", "value": "Trust IT + Digital programme office + Cerner / Oracle Health + DHSC Frontline Digitisation funding + North East London ICB digital pillar"},
            {"label": "Policy owner", "value": "DHSC + NHSE Frontline Digitisation + NHSE Provider Finance + NHS North East London ICB"},
            {"label": "Evaluation evidence", "value": "NHSE Frontline Digitisation programme evaluation; NAO Digital Transformation in the NHS (HC 8, 2020); Trust ARA disclosure; CQC inspection (RQX)"},
            {"label": "Predecessor / successor", "value": "Predecessor: legacy departmental clinical systems · Successor: convergent Cerner/Oracle Health EPR + maternity/neonatal specialty modules amortising 2024-2030+"}
        ],
        "notes": "Homerton Healthcare's amortisation line is shaped by the trust's integrated acute + community footprint serving Hackney and the City of London — a smaller-scale inner-London FT but with a tertiary neonatal centre and high-volume maternity (c. 6,000 deliveries/yr) that drives specialty-software capitalisation including BadgerNet maternity and neonatal systems alongside the Cerner Millennium / Oracle Health EPR pathway. NHSE Frontline Digitisation programme drives EPR-related intangible additions over IAS 38 / DHSC GAM ch.5 UEL assumptions. North East London ICS acute provider collaborative (with Barts + BHRUT) provides joint-procurement digital scaling. IFRIC 22 March 2021 reshaped capitalisation/opex boundary.",
        "sources": [
            {"publisher": "Homerton Healthcare NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.homerton.nhs.uk/our-publications"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/connecting-health-and-care-providers/frontline-digitisation/"},
            {"publisher": "National Audit Office", "title": "Digital transformation in the NHS (HC 8, 2020)", "url": "https://www.nao.org.uk/reports/the-use-of-digital-technology-in-the-nhs/"},
            {"publisher": "IFRS Foundation / IFRIC", "title": "Configuration or customisation costs in a cloud computing arrangement (IFRIC March 2021 agenda decision)", "url": "https://www.ifrs.org/news-and-events/news/2021/04/ifric-update-march-2021/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 5)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Homerton Healthcare provider profile (RQX)", "url": "https://www.cqc.org.uk/provider/RQX"}
        ],
        "related": ["Homerton Healthcare NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Frontline Digitisation Programme", "Amortisation — Lewisham and Greenwich NHS Trust", "Department of Health and Social Care"]
    },
    "Amortisation — Liverpool University Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Amortisation", "parent": "Liverpool University Hospitals NHS Foundation Trust"}],
        "description": "LUHFT's £4.05M amortisation line is the systematic write-down of capitalised intangible assets — primarily software, EPR, PACS, capitalised software development and licences — under IAS 38 with useful economic lives of 5-10 years per DHSC GAM ch.5. The trust runs the New Royal Liverpool University Hospital (Oct 2022 opening), Aintree, Broadgreen and community-clinic footprint. The line scales with NHSE Frontline Digitisation EPR investment and the 2019 merger consolidation (former Royal Liverpool & Broadgreen + Aintree).",
        "beneficiaries": "c. 13,500 WTE staff serving a c. 1.5M Cheshire & Merseyside catchment; c. 250,000 ED attendances/yr across Royal Liverpool + Aintree EDs; c. 130,000 elective + day-case admissions/yr; three-site footprint with New Royal as flagship academic acute since Oct 2022.",
        "legal_basis": "IAS 38 Intangible Assets · IFRIC 22 SaaS configuration/customisation costs (March 2021 agenda decision) · DHSC Group Accounting Manual 2024-25 ch.5 · NHS Act 2006 · Health and Care Act 2022 · NHSE Frontline Digitisation programme guidance",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£4.05M"},
            {"label": "Trust scale", "value": "Three-site acute (Royal Liverpool + Aintree + Broadgreen) post-2019 merger; c. 13,500 WTE"},
            {"label": "Asset base composition", "value": "Cerner Millennium / Oracle Health EPR + radiology PACS + capitalised software + capitalised software development; 5-10yr UEL per IAS 38 / DHSC GAM ch.5"},
            {"label": "IFRIC 22 effect", "value": "March 2021 IFRIC SaaS configuration/customisation agenda decision reshaped capitalisation boundary; some costs reclassified opex"},
            {"label": "Frontline Digitisation context", "value": "NHSE Frontline Digitisation funds EPR rollouts to 'core' standard by 2026 — LUHFT receiving FD investment for tri-site convergence"},
            {"label": "New Royal opening", "value": "New Royal Liverpool University Hospital opened Oct 2022 after Carillion 2018 collapse — material capital additions feeding 2023-25 amortisation cycle"},
            {"label": "2019 merger integration", "value": "Royal Liverpool & Broadgreen + Aintree merged Oct 2019 — sustained capitalised IT integration costs through 2020s convergence"},
            {"label": "Funding trajectory", "value": "2021-22 c. £3.0M → 2022-23 £3.5M (post-New Royal opening) → 2023-24 £3.8M → 2024-25 £4.05M — sustained intangible additions"},
            {"label": "Delivery body", "value": "Trust IT + Digital programme office + Cerner / Oracle Health + DHSC Frontline Digitisation funding + Cheshire & Merseyside ICB digital pillar"},
            {"label": "Policy owner", "value": "DHSC + NHSE Frontline Digitisation + NHSE Provider Finance + NHS Cheshire and Merseyside ICB"},
            {"label": "Evaluation evidence", "value": "NHSE Frontline Digitisation programme evaluation; NAO Digital Transformation in the NHS (HC 8, 2020); NAO Carillion + New Royal completion reports; Trust ARA disclosure"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2019 separate Royal Liverpool + Aintree intangible-asset baselines · Successor: convergent FD-funded EPR + integrated PACS + AI-clinical-decision modules amortising 2024-2030+"}
        ],
        "notes": "LUHFT's amortisation line reflects the post-2019 merger consolidation of capitalised intangible assets — Cerner Millennium / Oracle Health EPR, radiology PACS and capitalised software development — alongside material additions from the October 2022 New Royal Liverpool opening, the post-Carillion-collapse rebuild completed by Laing O'Rourke. NHSE Frontline Digitisation programme drives EPR-related intangible additions over IAS 38 / DHSC GAM ch.5 useful-economic-life assumptions of 5-10 years. The IFRIC 22 March 2021 SaaS agenda decision reshaped the boundary between capitalised configuration and opex. Tri-site convergence (Royal + Aintree + Broadgreen) sustains capitalised IT integration costs through the 2020s. NAO's 2020 Digital Transformation in the NHS report frames programme oversight.",
        "sources": [
            {"publisher": "Liverpool University Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.liverpoolft.nhs.uk/about-us/our-publications/"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/connecting-health-and-care-providers/frontline-digitisation/"},
            {"publisher": "National Audit Office", "title": "Investigation into the rescue of Carillion's PFI hospital contracts", "url": "https://www.nao.org.uk/reports/investigation-into-the-rescue-of-carillions-pfi-hospital-contracts/"},
            {"publisher": "IFRS Foundation / IFRIC", "title": "Configuration or customisation costs in a cloud computing arrangement (IFRIC March 2021 agenda decision)", "url": "https://www.ifrs.org/news-and-events/news/2021/04/ifric-update-march-2021/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 5)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "LUHFT provider profile (REM)", "url": "https://www.cqc.org.uk/provider/REM"}
        ],
        "related": ["Liverpool University Hospitals NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Frontline Digitisation Programme", "Amortisation — Homerton Healthcare NHS Foundation Trust", "General supplies & services — Liverpool University Hospitals NHS Foundation Trust"]
    },
    "General supplies & services — James Paget University Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "James Paget University Hospitals NHS Foundation Trust"}],
        "description": "James Paget's £4.03M general supplies & services line covers non-clinical consumables, linen, catering, hotel-services materials, office and IT consumables across the single-site DGH at Gorleston (Great Yarmouth + Waveney). The trust is one of seven worst-affected RAAC sites on the September 2023 HSSIB list with the New James Paget University Hospital NHP rebuild scheme designed to replace the failing 1980s plank roof estate, putting consumables baseline in transition through the 2020s decant + rebuild cycle.",
        "beneficiaries": "c. 3,500 WTE staff serving a c. 250,000 Great Yarmouth + Waveney coastal catchment; c. 80,000 ED attendances/yr; c. 35,000 admissions/yr; rural/coastal catchment with significant elderly demographic and seasonal tourism population pressure.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 2 Inventories · Procurement Act 2023 · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "General supplies & services 2024-25", "value": "£4.03M"},
            {"label": "Trust scale", "value": "Single acute site (James Paget University Hospital, Gorleston); c. 3,500 WTE"},
            {"label": "ED throughput", "value": "c. 80,000 attendances/yr — coastal catchment, seasonal-tourism demand spikes"},
            {"label": "RAAC context", "value": "JPUH on Sep 2023 HSSIB RAAC list — one of seven worst-affected sites with 'imminent risk of structural failure' designation; extensive structural propping"},
            {"label": "NHP New JPUH scheme", "value": "New Hospital Programme — full rebuild scheme; Jan 2025 NHP Reset confirmed continued delivery for RAAC cohort with completion targeted late 2020s"},
            {"label": "Procurement route", "value": "NHS Supply Chain national framework + Norfolk and Waveney ICS collaborative + trust-direct contracts"},
            {"label": "Industrial action 2023-24 + Apr 2025 NIC", "value": "44 days junior-doctor + 10 days consultant strikes drove backfill churn; Apr 2025 NIC step-up + CPI feed forward unit-cost pressure"},
            {"label": "Funding trajectory", "value": "2021-22 c. £3.3M → 2023-24 £3.8M → 2024-25 £4.03M — RAAC-related operational disruption + CPI"},
            {"label": "Delivery body", "value": "Trust Procurement + Supply Chain team + NHS Supply Chain (DHSC ALB) + Norfolk and Waveney ICB procurement"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + NHP team + NHS Norfolk and Waveney ICB"},
            {"label": "Evaluation evidence", "value": "HSSIB RAAC report Sep 2023; NAO New Hospital Programme report (Jul 2023); NHP Reset Jan 2025; Trust ARA"},
            {"label": "Predecessor / successor", "value": "Predecessor: 1982 RAAC-built JPUH baseline · Successor: New JPUH NHP rebuild operational late 2020s + post-rebuild consolidated procurement footprint"}
        ],
        "notes": "James Paget University Hospital is one of the seven worst-affected RAAC trusts on the September 2023 HSSIB list, with the failing 1982 reinforced-autoclaved-aerated-concrete plank roof requiring extensive structural propping while the New JPUH NHP rebuild progresses. The January 2025 NHP Reset confirmed continued delivery for the RAAC seven (Hinchingbrooke, QEH King's Lynn, James Paget, Frimley, Airedale, Mid Cheshire, West Suffolk) on a late-2020s completion path. Operational disruption from RAAC remediation and decant arrangements feeds into elevated consumable churn alongside national CPI on hotel-services inputs and seasonal-tourism demand spikes on the Norfolk coast catchment. NHS Supply Chain dominant carrier; Norfolk & Waveney ICS scaling (shared with QEH King's Lynn).",
        "sources": [
            {"publisher": "James Paget University Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.jpaget.nhs.uk/about-us/publications-and-reports/"},
            {"publisher": "National Audit Office", "title": "Progress with the New Hospital Programme (HC 1662, July 2023)", "url": "https://www.nao.org.uk/reports/the-new-hospital-programme/"},
            {"publisher": "Health Services Safety Investigations Body", "title": "RAAC concrete in NHS hospital estate (Sep 2023)", "url": "https://www.hssib.org.uk/"},
            {"publisher": "NHS Supply Chain", "title": "Annual Report 2023-24", "url": "https://www.supplychain.nhs.uk/about-us/our-publications/"},
            {"publisher": "Care Quality Commission", "title": "James Paget UH provider profile (RGP)", "url": "https://www.cqc.org.uk/provider/RGP"}
        ],
        "related": ["James Paget University Hospitals NHS Foundation Trust", "Clinical Supplies & Drugs", "NHS Acute Trusts", "New Hospital Programme", "General supplies & services — Queen Elizabeth Hospital King's Lynn NHS Foundation Trust", "NHS Supply Chain"]
    },
    "Establishment costs — Isle of Wight NHS Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "Isle of Wight NHS Trust"}],
        "description": "Isle of Wight NHS Trust's £4.02M establishment costs line covers postage, telephony, print, recruitment-advertising, training and conferences, subscriptions and legal & professional fees across the trust's uniquely-scoped footprint — the only English NHS provider running integrated acute, ambulance, community and mental-health services on a single-island geography. The trust is in active partnership/group-model relationship with Portsmouth Hospitals University NHS Trust to support clinical resilience and corporate-services scaling, shaping recruitment and professional-fee patterns.",
        "beneficiaries": "c. 3,000 WTE staff serving the c. 142,000 Isle of Wight population (sole NHS provider); c. 60,000 ED attendances/yr at St Mary's (Newport) ED; c. 28,000 admissions/yr; integrated acute + ambulance + community + mental-health workforce on single-island geography.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25 · Public Contracts Regulations 2015 / Procurement Act 2023",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£4.02M"},
            {"label": "Trust scale", "value": "Single acute site (St Mary's, Newport) + island-wide ambulance + community + mental-health services; c. 3,000 WTE"},
            {"label": "Composition", "value": "Postage + telephony + print + recruitment-advertising + training + conferences + subscriptions + legal & professional fees"},
            {"label": "Unique integrated model", "value": "Only English NHS provider with integrated acute + ambulance + community + mental-health services on a single-island catchment — shapes corporate-services + recruitment-advertising spend pattern"},
            {"label": "Portsmouth Hospitals partnership", "value": "Group-model partnership with Portsmouth Hospitals University NHS Trust supports clinical resilience + corporate-services scaling"},
            {"label": "Island recruitment driver", "value": "Hard-to-fill consultant + middle-grade recruitment to island catchment — agency-recruitment + advertising fees materially above mainland peers"},
            {"label": "Industrial action 2023-24 + Apr 2025 NIC", "value": "44 days junior-doctor + 10 days consultant strikes drove agency + recruitment-advertising fees; Apr 2025 NIC step-up + CPI feed forward"},
            {"label": "Funding trajectory", "value": "2021-22 c. £3.2M → 2023-24 £3.8M → 2024-25 £4.02M — sustained recruitment churn + Portsmouth partnership integration costs"},
            {"label": "Delivery body", "value": "Trust Corporate Services + HR + Finance + IT + Communications + external counsel + (developing) Portsmouth-Isle of Wight shared corporate functions"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + NHS Hampshire and Isle of Wight ICB"},
            {"label": "Evaluation evidence", "value": "Model Hospital corporate-services benchmarks; CQC inspection (R1F); Trust ARA disclosure; Portsmouth-IoW partnership business case"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2017 stand-alone Isle of Wight trust · Successor: ongoing Portsmouth Hospitals group-model partnership consolidation + HIOW ICB shared corporate-services"}
        ],
        "notes": "Isle of Wight NHS Trust occupies a unique position in the English NHS — the only provider running integrated acute, ambulance, community and mental-health services on a single-island catchment of c. 142,000 — and that uniqueness materially shapes the establishment cost line: hard-to-fill consultant and middle-grade recruitment drives agency and advertising spend significantly above mainland DGH peers. The active group-model partnership with Portsmouth Hospitals University NHS Trust provides clinical resilience and corporate-services scaling, with shared corporate functions developing. CQC inspections have flagged sustained quality-improvement work. April 2025 NIC step-up + CPI feed forward into 2025-26 baseline.",
        "sources": [
            {"publisher": "Isle of Wight NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.iow.nhs.uk/our-publications/"},
            {"publisher": "Portsmouth Hospitals University NHS Trust", "title": "Isle of Wight partnership", "url": "https://www.porthosp.nhs.uk/"},
            {"publisher": "Care Quality Commission", "title": "Isle of Wight NHS Trust provider profile (R1F)", "url": "https://www.cqc.org.uk/provider/R1F"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS Hampshire and Isle of Wight ICB", "title": "ICB strategic plan + Portsmouth-IoW partnership", "url": "https://www.hantsiowhealthandcare.org.uk/"}
        ],
        "related": ["Isle of Wight NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Portsmouth Hospitals University NHS Trust", "Establishment costs — Chelsea and Westminster Hospital NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Transport (business + patient) — The Rotherham NHS Foundation Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "The Rotherham NHS Foundation Trust"}],
        "description": "The Rotherham NHS Foundation Trust's £3.99M transport line covers business mileage, inter-hospital patient transfers (especially tertiary referrals to Sheffield Teaching Hospitals + Doncaster & Bassetlaw), and Non-Emergency Patient Transport Services across Rotherham borough and the wider South Yorkshire ICS catchment. Yorkshire Ambulance Service is the primary PTS carrier alongside accredited NEPTS contractors recommissioned via South Yorkshire ICS PTS framework. The trust's integrated acute + community footprint sustains AHP and community-team mileage demand.",
        "beneficiaries": "c. 4,500 WTE staff serving a c. 265,000 Rotherham borough catchment; c. 100,000 ED attendances/yr at Rotherham Hospital ED; c. 45,000 admissions/yr; integrated borough community workforce; tertiary referrals to Sheffield Teaching Hospitals (cardiac, neuro, oncology, vascular).",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · IFRS 16 Leases (pool fleet) · NHS Act 2006 · Mental Health Act 1983 (s.135/136 conveyance) · NHSE Patient Transport Services Eligibility Framework 2022 · HMRC AMAP · NHS AfC Section 17",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£3.99M"},
            {"label": "Trust scale", "value": "Single acute site (Rotherham Hospital, Moorgate) + integrated Rotherham community services; c. 4,500 WTE"},
            {"label": "ED throughput", "value": "c. 100,000 attendances/yr"},
            {"label": "Tertiary referral pattern", "value": "Onward referrals to Sheffield Teaching Hospitals (cardiac + neuro + oncology + vascular) drive sustained inter-trust PTS demand"},
            {"label": "PTS provider mix", "value": "Yorkshire Ambulance Service NHS Trust (YAS) + accredited NEPTS contractors — re-tendered via South Yorkshire ICS PTS framework"},
            {"label": "Staff mileage rate", "value": "NHS Agenda for Change Section 17 / HMRC AMAP 45p first 10,000 miles + 25p thereafter"},
            {"label": "Pool fleet + community workforce + industrial action", "value": "IFRS 16 right-of-use depreciation on leased pool vehicles for AHPs + community teams (district nursing + therapies + community-paediatric + sexual-health); 44 days junior-doctor + 10 days consultant strikes drove ad-hoc inter-site transfers + locum mileage claims"},
            {"label": "Funding trajectory", "value": "2021-22 c. £3.2M → 2023-24 £3.7M → 2024-25 £3.99M — fuel CPI + activity recovery + sustained tertiary-referral PTS demand"},
            {"label": "Delivery body", "value": "Trust E&F + Travel team + YAS PTS + accredited NEPTS contractors + South Yorkshire ICS PTS commissioning"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + NHSE Ambulance + NHS South Yorkshire ICB"},
            {"label": "Evaluation evidence", "value": "NHSE PTS Eligibility Framework 2022; South Yorkshire ICS PTS recommissioning; Trust ARA disclosure; CQC inspection (RFR)"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2011 separate Rotherham Hospital + Rotherham PCT community baselines · Successor: South Yorkshire ICS PTS framework + Sheffield-Rotherham-Doncaster acute provider collaborative"}
        ],
        "notes": "The Rotherham NHS Foundation Trust's transport line is shaped by three drivers: integrated acute + community workforce mileage across Rotherham borough; sustained tertiary-referral PTS demand to Sheffield Teaching Hospitals (cardiac, neuro, oncology, vascular) under the South Yorkshire ICS provider-collaborative model; and standard NEPTS eligibility throughput for outpatient and discharge transport. Yorkshire Ambulance Service operates as primary PTS carrier alongside accredited NEPTS contractors recommissioned through South Yorkshire ICS PTS framework. NHS AfC Section 17 / HMRC AMAP staff mileage rate caps unit-rate; fuel CPI and activity recovery drove 2023-25 trajectory. Industrial action 2023-24 drove ad-hoc inter-site transfers.",
        "sources": [
            {"publisher": "The Rotherham NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.therotherhamft.nhs.uk/about-us/publications/"},
            {"publisher": "NHS England", "title": "Patient Transport Services Eligibility Framework 2022", "url": "https://www.england.nhs.uk/publication/non-emergency-patient-transport-services-nepts/"},
            {"publisher": "Yorkshire Ambulance Service NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.yas.nhs.uk/about-us/publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Rotherham NHS FT provider profile (RFR)", "url": "https://www.cqc.org.uk/provider/RFR"}
        ],
        "related": ["The Rotherham NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Yorkshire Ambulance Service NHS Trust", "Transport (business + patient) — Liverpool University Hospitals NHS Foundation Trust", "Department of Health and Social Care"]
    },
}
