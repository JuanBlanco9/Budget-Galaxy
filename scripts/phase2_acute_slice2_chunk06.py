# -*- coding: utf-8 -*-
# Phase 2 Acute slice 2 — chunk 06 (17 NHS Acute Trust orphan sub-lines)
# Hand-curated trust-specific PROGRAMME-archetype enrichment entries.
# Structural contract per docs/archetype_briefs.md.

NEW = {
    "Transport (business + patient) — University College London Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "University College London Hospitals NHS Foundation Trust"}],
        "description": "UCLH's £13.38M transport line covers business mileage, inter-site patient transfers and Non-Emergency Patient Transport Services across the trust's central London teaching-hospital footprint (UCH, NHNN Queen Square, EGA Wing, RNTNE Hospital at Huntley Street, Macmillan Cancer Centre, RNOH co-located clinics, Proton Beam Therapy centre). Tertiary-specialty referrals — neurology/neurosurgery (NHNN), women's health (EGA), proton-beam oncology — drive substantial inter-trust PTS demand from across England, with London Ambulance Service NEPTS and accredited contractors as primary carriers.",
        "beneficiaries": "c. 11,000 WTE staff serving a c. 1.5M central + north London catchment plus tertiary national/international referrals; c. 200,000 ED attendances/yr at UCH ED; c. 130,000 admissions/yr; UCH = London Major Trauma System hyper-acute support + national specialist commissioning for proton-beam therapy and rare neurology.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) — IAS 1 Presentation of Financial Statements — IFRS 16 Leases (pool fleet) — NHS Act 2006 — Mental Health Act 1983 (s.135/136 conveyance) — NHSE Patient Transport Services Eligibility Framework 2022 — HMRC AMAP — NHS AfC Section 17",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£13.38M"},
            {"label": "Trust scale", "value": "Multi-site academic acute (UCH + NHNN + EGA + Macmillan + Proton Beam Therapy centre + RNTNE); c. 11,000 WTE"},
            {"label": "Tertiary referral driver", "value": "NHNN Queen Square neurology/neurosurgery + EGA women's health + Macmillan + Proton Beam — substantial inter-trust + cross-country PTS"},
            {"label": "Proton Beam Therapy", "value": "UCLH = one of two NHS Proton Beam Therapy centres (Christie Manchester other) — drives long-distance patient + family travel reimbursement"},
            {"label": "PTS provider mix", "value": "London Ambulance Service NEPTS + accredited NEPTS contractors (ERS Medical / DHL etc.) — re-tendered via NCL ICS"},
            {"label": "Staff mileage rate", "value": "NHS AfC Section 17 / HMRC AMAP 45p first 10,000 miles + 25p thereafter; pool-fleet IFRS 16 ROU depreciation"},
            {"label": "Industrial action + Apr 2025 NIC + fuel CPI", "value": "44 days junior-doctor + 10 days consultant strikes drove ad-hoc transfers + locum mileage; Apr 2025 NIC + fuel CPI feed forward"},
            {"label": "Funding trajectory", "value": "2021-22 c. £10M → 2023-24 £12M → 2024-25 £13.38M — fuel CPI + tertiary activity recovery + Proton Beam ramp-up"},
            {"label": "Delivery body", "value": "Trust E&F + Travel team + LAS PTS + accredited NEPTS contractors + NCL ICS procurement collaborative"},
            {"label": "Policy owner", "value": "NHSE Specialised Commissioning + DHSC + North Central London ICB"},
            {"label": "Evaluation evidence", "value": "CQC inspection RRV; NHSE PTS Eligibility Framework 2022; NCL ICS PTS recommissioning; Trust ARA"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2015 pre-Macmillan + pre-Proton Beam baseline · Successor: NCL group-model PTS consolidation"}
        ],
        "notes": "UCLH's transport baseline is shaped by national specialist commissioning — the trust hosts one of two NHS Proton Beam Therapy centres (the other being The Christie in Manchester), drawing rare-cancer paediatric and adult patients from across England with associated travel + accommodation reimbursement, alongside National Hospital for Neurology and Neurosurgery (Queen Square) referrals for rare neurological surgery. London Ambulance Service NEPTS is the dominant PTS carrier, supplemented by accredited contractors re-tendered through North Central London ICS. Industrial action 2023-24 drove ad-hoc inter-site transfer surges and locum mileage claims. The April 2025 employer-NIC step-up flows through to contractor pricing alongside continued fuel CPI, sustaining 2025-26 unit-cost pressure.",
        "sources": [
            {"publisher": "University College London Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.uclh.nhs.uk/about-us/our-publications/annual-reports-and-accounts"},
            {"publisher": "NHS England", "title": "Patient Transport Services Eligibility Framework", "url": "https://www.england.nhs.uk/publication/non-emergency-patient-transport-services-eligibility-criteria-framework/"},
            {"publisher": "NHS England", "title": "Proton Beam Therapy service specification", "url": "https://www.england.nhs.uk/commissioning/spec-services/npc-crg/group-b/b01/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "UCLH provider profile (RRV)", "url": "https://www.cqc.org.uk/provider/RRV"}
        ],
        "related": ["University College London Hospitals NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Transport (business + patient) — Imperial College Healthcare NHS Trust", "London Ambulance Service NHS Trust", "NHS England"]
    },
    "General supplies & services — Frimley Health NHS Foundation Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "Frimley Health NHS Foundation Trust"}],
        "description": "Frimley Health's £13.30M general supplies & services line covers non-clinical consumables, linen, catering, hotel-services materials, office supplies and minor expensed equipment across the trust's three-site footprint — Frimley Park Hospital, Wexham Park Hospital and Heatherwood Hospital (rebuilt 2022). The trust's RAAC exposure at Frimley Park (HSSIB 2023 list, full rebuild planned under New Hospital Programme) drives decant and re-stocking churn, while the recent Heatherwood elective-orthopaedic rebuild establishes a modern hotel-services baseline.",
        "beneficiaries": "c. 9,500 WTE staff serving a c. 900,000 catchment across Surrey, Berkshire and Hampshire; c. 230,000 ED attendances/yr (Frimley Park + Wexham Park EDs combined); c. 110,000 admissions/yr; Heatherwood specialises in high-volume elective orthopaedic + day-case work post-2022 rebuild.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) — IAS 2 Inventories — Procurement Act 2023 — NHS Act 2006 — Health and Care Act 2022 — NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "General supplies & services 2024-25", "value": "£13.30M"},
            {"label": "Trust scale", "value": "Three-site acute (Frimley Park + Wexham Park + Heatherwood); c. 9,500 WTE; c. 230,000 ED attendances/yr combined"},
            {"label": "RAAC exposure", "value": "Frimley Park on HSSIB Sep 2023 RAAC list; full rebuild in NHP cohort — Jan 2025 NHP Reset retained in earlier rebuild tranche"},
            {"label": "Heatherwood rebuild context", "value": "Heatherwood Hospital rebuilt 2022 (£100M+ scheme) as elective-orthopaedic centre — modern hotel-services baseline"},
            {"label": "Procurement route", "value": "NHS Supply Chain national framework + Frimley ICS collaborative + trust-direct contracts"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove cancellation re-stocking + agency backfill"},
            {"label": "April 2025 NIC + CPI uplift", "value": "Employer-NIC step-up + non-clinical CPI feed forward unit-cost pressure"},
            {"label": "Funding trajectory", "value": "2021-22 c. £11M → 2022-23 Heatherwood opening £12M → 2024-25 £13.30M"},
            {"label": "Delivery body", "value": "Trust Procurement + NHS Supply Chain + Frimley ICS procurement collaborative"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Frimley ICB + (RAAC) New Hospital Programme team"},
            {"label": "Evaluation evidence", "value": "CQC RDU inspection; NAO RAAC report 2023; NHP Reset Jan 2025; Trust ARA"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2014 separate Frimley Park + Heatherwood + Wexham (acquired 2014) baselines · Successor: post-Frimley Park rebuild consolidated baseline"}
        ],
        "notes": "Frimley Health's non-clinical consumables baseline reflects the trust's distinctive estate-mix — Heatherwood Hospital was rebuilt and reopened in 2022 as a high-volume elective-orthopaedic centre with modern hotel-services standards, while Frimley Park Hospital sits on the HSSIB September 2023 RAAC list and is in the New Hospital Programme cohort for full rebuild. The January 2025 NHP Reset retained Frimley Park in an earlier rebuild tranche, with decant and re-stocking churn shaping the 2024-25 baseline. Industrial action 2023-24 drove cancellation re-stocking and agency backfill. NHS Supply Chain is the dominant procurement vehicle, with Frimley ICS collaborative scaling as a medium-term lever; April 2025 NIC step-up and sustained non-clinical CPI feed forward unit-cost pressure.",
        "sources": [
            {"publisher": "Frimley Health NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.fhft.nhs.uk/about-us/corporate-information/annual-reports/"},
            {"publisher": "Health Services Safety Investigations Body / NHS England", "title": "RAAC in NHS estate — affected sites", "url": "https://www.england.nhs.uk/estates/reinforced-autoclaved-aerated-concrete/"},
            {"publisher": "NHS Supply Chain", "title": "Annual Report 2023-24", "url": "https://www.supplychain.nhs.uk/about-us/our-publications/"},
            {"publisher": "Department of Health and Social Care", "title": "New Hospital Programme — plan for implementation (Jan 2025 Reset)", "url": "https://www.gov.uk/government/publications/new-hospital-programme-plan-for-implementation"},
            {"publisher": "Care Quality Commission", "title": "Frimley Health provider profile (RDU)", "url": "https://www.cqc.org.uk/provider/RDU"}
        ],
        "related": ["Frimley Health NHS Foundation Trust", "Clinical Supplies & Drugs", "NHS Acute Trusts", "New Hospital Programme", "NHS Supply Chain", "General supplies & services — Liverpool University Hospitals NHS Foundation Trust"]
    },
    "Establishment costs — North West Anglia NHS Foundation Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "North West Anglia NHS Foundation Trust"}],
        "description": "North West Anglia's £13.17M establishment costs line covers postage, telephony, printing, stationery, training/courses, advertising, subscriptions and external audit fees across the trust's three-site footprint — Peterborough City Hospital (PFI-built, opened 2010), Hinchingbrooke Hospital (RAAC-affected) and Stamford and Rutland Hospital. Hinchingbrooke's RAAC exposure (HSSIB Sep 2023 list, NHP Reset rebuild cohort) drives change-management and decant communication costs, while Frontline Digitisation EPR rollout adds training-related establishment cost.",
        "beneficiaries": "c. 7,500 WTE staff serving a c. 800,000 catchment across Peterborough, Huntingdonshire, Fenland, Stamford and Rutland; c. 200,000 ED attendances/yr (Peterborough + Hinchingbrooke EDs combined); c. 95,000 admissions/yr; trust formed 2017 by merger of Peterborough & Stamford with Hinchingbrooke Health Care.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) — IAS 1 Presentation of Financial Statements — NHS Act 2006 — Health and Care Act 2022 — NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£13.17M"},
            {"label": "Trust scale", "value": "Three-site acute (Peterborough City + Hinchingbrooke + Stamford and Rutland); c. 7,500 WTE"},
            {"label": "Merger context", "value": "Trust formed 1 April 2017 by merger of Peterborough & Stamford NHS FT with Hinchingbrooke Health Care NHS Trust"},
            {"label": "RAAC exposure", "value": "Hinchingbrooke on HSSIB Sep 2023 RAAC list; NHP rebuild cohort — Jan 2025 Reset retained in earlier tranche; drives decant communication"},
            {"label": "Peterborough PFI + EPR", "value": "Peterborough City Hospital PFI 2007/2010 — Progress Health SPV — large-PFI contract overhead; Frontline Digitisation EPR training cost"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove communication + scheduling overheads"},
            {"label": "April 2025 NIC + CPI uplift", "value": "Employer-NIC step-up + telephony/postage CPI feed forward unit-cost pressure"},
            {"label": "Funding trajectory", "value": "2021-22 c. £10M → 2023-24 £12M → 2024-25 £13.17M — RAAC + EPR overheads"},
            {"label": "Delivery body", "value": "Trust Corporate Services + Communications + Finance + Cambridgeshire & Peterborough ICS"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Cambridgeshire and Peterborough ICB + NHP team"},
            {"label": "Evaluation evidence", "value": "CQC RGN inspection; HSSIB RAAC list 2023; NHP Reset Jan 2025; Trust ARA"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2017 separate baselines · Successor: post-Hinchingbrooke rebuild (NHP cohort) consolidated baseline"}
        ],
        "notes": "North West Anglia's establishment-costs baseline carries the dual overhead of post-2017 merger-integration corporate services (combining the former Peterborough & Stamford and Hinchingbrooke trusts) and active RAAC remediation programme management at Hinchingbrooke Hospital, which sits on the HSSIB September 2023 RAAC list with full rebuild confirmed in the January 2025 NHP Reset earlier tranche. Decant and re-stocking change-management communication, alongside Frontline Digitisation EPR rollout training, drive headline cost growth. Peterborough's 2010-opened PFI adds large-contract management establishment overhead. April 2025 NIC step-up and sustained CPI on postage/telephony/training feed forward unit-cost pressure into 2025-26.",
        "sources": [
            {"publisher": "North West Anglia NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.nwangliaft.nhs.uk/about-us/our-publications/"},
            {"publisher": "Health Services Safety Investigations Body / NHS England", "title": "RAAC in NHS estate — affected sites", "url": "https://www.england.nhs.uk/estates/reinforced-autoclaved-aerated-concrete/"},
            {"publisher": "Department of Health and Social Care", "title": "New Hospital Programme — plan for implementation (Jan 2025 Reset)", "url": "https://www.gov.uk/government/publications/new-hospital-programme-plan-for-implementation"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme (EPR)", "url": "https://www.england.nhs.uk/digitaltechnology/connecting-health-and-care-through-technology/electronic-patient-record-systems/"},
            {"publisher": "Care Quality Commission", "title": "North West Anglia provider profile (RGN)", "url": "https://www.cqc.org.uk/provider/RGN"}
        ],
        "related": ["North West Anglia NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "New Hospital Programme", "Establishment costs — Cambridge University Hospitals NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Establishment costs — Hampshire Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "Hampshire Hospitals NHS Foundation Trust"}],
        "description": "Hampshire Hospitals' £12.82M establishment costs line covers postage, telephony, printing, stationery, training/courses, advertising, subscriptions and external audit fees across the trust's three-site footprint — Royal Hampshire County Hospital (Winchester), Basingstoke and North Hampshire Hospital (Basingstoke) and Andover War Memorial Hospital. The trust is in active reconfiguration planning for a new mid-Hampshire critical-treatment hospital with two-site adjusted footprint, and Frontline Digitisation EPR rollout drives training-related establishment cost.",
        "beneficiaries": "c. 5,500 WTE staff serving a c. 600,000 catchment across north and mid Hampshire; c. 150,000 ED attendances/yr (Winchester + Basingstoke EDs combined); c. 75,000 admissions/yr; trust formed 2012 by merger of Winchester and Eastleigh with Basingstoke and North Hampshire NHS FTs.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) — IAS 1 Presentation of Financial Statements — NHS Act 2006 — Health and Care Act 2022 — NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£12.82M"},
            {"label": "Trust scale", "value": "Three-site acute (Royal Hampshire County + Basingstoke and North Hampshire + Andover War Memorial); c. 5,500 WTE"},
            {"label": "Merger context", "value": "Trust formed Jan 2012 by merger of Winchester & Eastleigh with Basingstoke and North Hampshire NHS FTs"},
            {"label": "Reconfiguration context", "value": "Active mid-Hampshire critical-treatment hospital reconfiguration planning — drives consultation + change-mgmt establishment overhead"},
            {"label": "Frontline Digitisation EPR", "value": "EPR rollout drives training/change-management establishment cost"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove communication + scheduling overheads"},
            {"label": "April 2025 NIC + CPI uplift", "value": "Employer-NIC step-up + telephony/postage CPI feed forward unit-cost pressure"},
            {"label": "Funding trajectory", "value": "2021-22 c. £10M → 2023-24 £12M → 2024-25 £12.82M — reconfig + EPR overheads"},
            {"label": "Delivery body", "value": "Trust Corporate Services + Communications + Finance + Hampshire and Isle of Wight ICS"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Hampshire and Isle of Wight ICB"},
            {"label": "Evaluation evidence", "value": "CQC RN5 inspection; NHSE major-service-change assurance for mid-Hampshire reconfig; Trust ARA"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2012 separate Winchester + Basingstoke baselines · Successor: post-reconfig new critical-treatment hospital baseline"}
        ],
        "notes": "Hampshire Hospitals' establishment-costs baseline reflects active reconfiguration planning — the trust has been working through proposals for a new mid-Hampshire critical-treatment hospital with two-site adjusted footprint, sustaining elevated consultation, communication and change-management spend across multiple iterations. Frontline Digitisation EPR rollout adds training-related establishment cost. The trust formed in January 2012 by merger of Winchester & Eastleigh and Basingstoke and North Hampshire NHS FTs, and the corporate-services consolidation continues to evolve through ICS group arrangements. Industrial action 2023-24 drove communication and scheduling overheads. April 2025 NIC step-up and sustained CPI on postage/telephony/training feed forward unit-cost pressure.",
        "sources": [
            {"publisher": "Hampshire Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.hampshirehospitals.nhs.uk/about-us/publications"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme (EPR)", "url": "https://www.england.nhs.uk/digitaltechnology/connecting-health-and-care-through-technology/electronic-patient-record-systems/"},
            {"publisher": "Hampshire and Isle of Wight Integrated Care Board", "title": "ICS strategy and major service change", "url": "https://www.hantsiowhealthandcare.org.uk/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Hampshire Hospitals provider profile (RN5)", "url": "https://www.cqc.org.uk/provider/RN5"}
        ],
        "related": ["Hampshire Hospitals NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Establishment costs — North West Anglia NHS Foundation Trust", "Establishment costs — Cambridge University Hospitals NHS Foundation Trust", "NHS England"]
    },
    "General supplies & services — North Bristol NHS Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "North Bristol NHS Trust"}],
        "description": "North Bristol's £12.79M general supplies & services line covers non-clinical consumables, linen, catering, hotel-services materials, office supplies and minor expensed equipment, predominantly at Southmead Hospital — the trust's PFI-built (Brunel building, opened 2014) main acute site, with subsidiary footprint at Cossham Hospital and community-clinic sites. The PFI hard-FM/soft-FM contract structure (originally Carillion → Sodexo novation post-2018 collapse) shapes the trust-direct vs SPV-bundled split of non-clinical consumables.",
        "beneficiaries": "c. 8,500 WTE staff serving a c. 900,000 catchment across north Bristol and South Gloucestershire plus tertiary referrals (renal, plastics, neurosciences, major trauma); c. 130,000 ED attendances/yr at Southmead ED; c. 80,000 admissions/yr; Southmead = Severn Major Trauma Centre.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) — IAS 2 Inventories — Procurement Act 2023 — NHS Act 2006 — Health and Care Act 2022 — NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "General supplies & services 2024-25", "value": "£12.79M"},
            {"label": "Trust scale", "value": "Single-large-site acute (Southmead Hospital, Brunel PFI building) + Cossham + community clinics; c. 8,500 WTE"},
            {"label": "Major Trauma Centre", "value": "Southmead = Severn MTC — drives high-acuity consumables baseline; tertiary renal + plastics + neurosciences broaden mix"},
            {"label": "Brunel PFI", "value": "Brunel building Southmead PFI signed 2009, operational 2014; Carillion Jan 2018 collapse → Sodexo novation; splits some hotel-services to SPV"},
            {"label": "Procurement route", "value": "NHS Supply Chain national framework + Bristol, North Somerset and South Gloucestershire ICS collaborative + trust-direct contracts"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove cancellation re-stocking + agency backfill"},
            {"label": "April 2025 NIC + CPI uplift", "value": "Employer-NIC step-up + non-clinical CPI feed forward unit-cost pressure"},
            {"label": "Funding trajectory", "value": "2021-22 c. £11M → 2023-24 £12M → 2024-25 £12.79M"},
            {"label": "Delivery body", "value": "Trust Procurement + NHS Supply Chain + Sodexo (PFI soft-FM) + BNSSG ICS collaborative"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Bristol, North Somerset and South Gloucestershire ICB"},
            {"label": "Evaluation evidence", "value": "CQC RVJ inspection; NAO Carillion + Brunel PFI reports; Model Hospital benchmarks; Trust ARA"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2014 multi-site (Frenchay + Southmead old + Cossham) baseline · Successor: post-Brunel-PFI consolidated procurement"}
        ],
        "notes": "North Bristol's non-clinical consumables baseline is shaped by the Brunel building PFI at Southmead, which opened in 2014 consolidating the former Frenchay and Southmead estates onto a single large modern site — modern hotel-services standards combined with Severn Major Trauma Centre status drive sustained baseline. Carillion's January 2018 collapse triggered FM novation to Sodexo on PFI soft-FM elements, shifting some hotel-services consumables onto the SPV side of the boundary. Tertiary specialty mix (renal, plastics, neurosciences) broadens the baseline further. Industrial action 2023-24 drove cancellation re-stocking and agency backfill. April 2025 NIC step-up and sustained non-clinical CPI feed forward unit-cost pressure.",
        "sources": [
            {"publisher": "North Bristol NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.nbt.nhs.uk/about-us/publications"},
            {"publisher": "National Audit Office", "title": "Investigation into the rescue of Carillion's PFI hospital contracts", "url": "https://www.nao.org.uk/reports/investigation-into-the-rescue-of-carillions-pfi-hospital-contracts/"},
            {"publisher": "NHS Supply Chain", "title": "Annual Report 2023-24", "url": "https://www.supplychain.nhs.uk/about-us/our-publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "North Bristol provider profile (RVJ)", "url": "https://www.cqc.org.uk/provider/RVJ"}
        ],
        "related": ["North Bristol NHS Trust", "Clinical Supplies & Drugs", "NHS Acute Trusts", "NHS Supply Chain", "General supplies & services — Liverpool University Hospitals NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "PFI / LIFT charges — Lewisham and Greenwich NHS Trust": {
        "aliases": [{"name": "PFI / LIFT charges", "parent": "Lewisham and Greenwich NHS Trust"}],
        "description": "Lewisham and Greenwich's £12.75M PFI charge covers unitary-charge pass-through on the Queen Elizabeth Hospital Woolwich PFI (signed 1998, operational 2001) — one of the south-east's earliest PFI-built acute sites under the Meridian Hospital Company SPV — plus residual LIFT-scheme costs across the trust's south-east London community-clinic estate. The 30-year QEH concession expires around 2031, putting the trust in the active hand-back planning window. The line covers debt service, lifecycle hard-FM and indexed soft-FM components.",
        "beneficiaries": "c. 6,500 WTE staff serving a c. 750,000 south-east London catchment across Lewisham and Greenwich boroughs; c. 220,000 ED attendances/yr (Lewisham + Queen Elizabeth Woolwich EDs combined); c. 90,000 admissions/yr; trust formed 2013 by merger of Lewisham Healthcare with Queen Elizabeth Hospital (former South London Healthcare Trust dissolution).",
        "legal_basis": "IFRIC 12 Service Concession Arrangements — IFRS 16 Leases (post-2022 transition) — DHSC Group Accounting Manual 2024-25 ch.7 — Private Finance Initiative guidance (HM Treasury) — NHS Act 2006 — Health and Care Act 2022",
        "key_stats": [
            {"label": "PFI / LIFT charges 2024-25", "value": "£12.75M"},
            {"label": "Trust scale", "value": "Two-site acute (Lewisham + Queen Elizabeth Woolwich, c. 510 beds) + LIFT community estate; c. 6,500 WTE"},
            {"label": "QEH PFI vehicle", "value": "Queen Elizabeth Hospital Woolwich PFI signed 1998, operational 2001; SPV Meridian Hospital Company"},
            {"label": "Contract end date", "value": "c. 2031 (30-year concession from 2001 operational date) — active hand-back planning window"},
            {"label": "Trust formation context", "value": "Trust formed 1 Oct 2013 by merger of Lewisham Healthcare with QEH (inherited from dissolved South London Healthcare NHS Trust)"},
            {"label": "Unitary charge composition", "value": "Senior + subordinated debt service + lifecycle hard-FM + indexed soft-FM; RPI-linked annual uplift on indexed FM"},
            {"label": "PAC/NAO scrutiny context", "value": "South London Healthcare Trust dissolved 2013 partly due to QEH + Princess Royal Bromley PFI affordability — NAO/PAC formative case"},
            {"label": "Funding trajectory", "value": "Mature PFI; line £12-14M range as RPI uplift continues vs declining debt-service balance"},
            {"label": "Delivery body", "value": "Meridian Hospital Company SPV + FM contractor cohort + trust E&F"},
            {"label": "Policy owner", "value": "DHSC + HM Treasury PFI guidance + IPA PFI Hand-Back unit + NHSE Provider Finance + South East London ICB"},
            {"label": "Evaluation evidence", "value": "NAO PFI 2018 + PFI hand-back 2020; PAC South London Healthcare hearings; Trust ARA"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2013 SLH Trust + Lewisham Healthcare baselines · Successor: c. 2031 hand-back to public-sector ownership"}
        ],
        "notes": "Lewisham and Greenwich's PFI charge reflects the formative-case Queen Elizabeth Hospital Woolwich PFI — the affordability pressure of QEH's unitary charge (alongside Princess Royal Bromley's PFI) was a primary cause of the 2013 dissolution of the predecessor South London Healthcare NHS Trust under the Unsustainable Provider Regime, with QEH transferring to the merged Lewisham and Greenwich entity. The 30-year concession expires around 2031, putting the trust in the active hand-back planning window with IPA/HMT PFI Hand-Back unit engagement underway. RPI indexation continues to lift soft-FM components even as debt-service amortises down. Hand-back governance and post-2031 estate ownership transition are the medium-term questions, shaped by NAO 2020.",
        "sources": [
            {"publisher": "Lewisham and Greenwich NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.lewishamandgreenwich.nhs.uk/about-us/our-publications/"},
            {"publisher": "National Audit Office", "title": "Managing PFI assets and services as contracts end (HC 632, 2020)", "url": "https://www.nao.org.uk/reports/managing-pfi-assets-and-services-as-contracts-end/"},
            {"publisher": "National Audit Office", "title": "PFI and PF2 (HC 718, 2018)", "url": "https://www.nao.org.uk/reports/pfi-and-pf2/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 7)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Lewisham and Greenwich provider profile (RJ2)", "url": "https://www.cqc.org.uk/provider/RJ2"}
        ],
        "related": ["Lewisham and Greenwich NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "PFI / LIFT charges — Sherwood Forest Hospitals NHS Foundation Trust", "PFI / LIFT charges — Worcestershire Acute Hospitals NHS Trust", "Infrastructure and Projects Authority"]
    },
    "General supplies & services — The Newcastle Upon Tyne Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "The Newcastle Upon Tyne Hospitals NHS Foundation Trust"}],
        "description": "Newcastle Hospitals' £12.71M general supplies & services line covers non-clinical consumables, linen, catering, hotel-services materials, office supplies and minor expensed equipment across the trust's two-site academic-tertiary footprint — the Royal Victoria Infirmary (city-centre Major Trauma Centre) and the Freeman Hospital (national-cardiothoracic + transplantation). Tertiary specialties (transplant, cardiothoracic, paediatric oncology, BRC research) drive elevated non-clinical baseline, and the trust's 'Climate Emergency' net-zero leadership shapes procurement choices.",
        "beneficiaries": "c. 16,000 WTE staff serving a c. 1.5M Newcastle and North East catchment plus tertiary national + international referrals (heart-lung transplant, paediatric oncology, BRC research); c. 290,000 ED attendances/yr at RVI ED; c. 200,000 admissions/yr; RVI = North East and North Cumbria Major Trauma Centre.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) — IAS 2 Inventories — Procurement Act 2023 — NHS Act 2006 — Health and Care Act 2022 — NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "General supplies & services 2024-25", "value": "£12.71M"},
            {"label": "Trust scale", "value": "Two-site academic-tertiary acute (Royal Victoria Infirmary + Freeman Hospital); c. 16,000 WTE; RVI = NENC MTC"},
            {"label": "Tertiary specialty", "value": "National heart-lung transplant + cardiothoracic + paediatric oncology + BRC research at Freeman — broaden non-clinical baseline"},
            {"label": "Net-zero leadership", "value": "Trust declared NHS Climate Emergency 2019; Greener NHS exemplar — drives sustainable-procurement reformulation"},
            {"label": "Procurement route", "value": "NHS Supply Chain national framework + North East and North Cumbria ICS collaborative + trust-direct contracts"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove cancellation re-stocking + agency backfill"},
            {"label": "April 2025 NIC + CPI uplift", "value": "Employer-NIC step-up + non-clinical CPI feed forward unit-cost pressure"},
            {"label": "Funding trajectory", "value": "2021-22 c. £11M → 2023-24 £12M → 2024-25 £12.71M"},
            {"label": "Delivery body", "value": "Trust Procurement + NHS Supply Chain + NENC ICS procurement collaborative"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Greener NHS + North East and North Cumbria ICB"},
            {"label": "Evaluation evidence", "value": "CQC RTD Outstanding rated; Greener NHS reporting; Model Hospital benchmarks; Trust ARA"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-1998 separate RVI + Freeman + Newcastle General baselines · Successor: ICS collaborative + Greener NHS scaling"}
        ],
        "notes": "Newcastle Hospitals operates one of the UK's largest academic-tertiary acute trusts, with tertiary specialty mix (national heart-lung transplant, cardiothoracic, paediatric oncology, NIHR BRC research) broadening the non-clinical consumables baseline alongside Major Trauma Centre status at the RVI. The trust's 2019 NHS Climate Emergency declaration and Greener NHS exemplar status drive sustainable-procurement reformulation across catering, linen and packaging. Industrial action 2023-24 drove cancellation re-stocking and agency backfill. NHS Supply Chain remains dominant, with NENC ICS collaborative as scaling lever; April 2025 NIC step-up and CPI feed forward unit-cost pressure.",
        "sources": [
            {"publisher": "The Newcastle Upon Tyne Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.newcastle-hospitals.nhs.uk/about-us/our-publications/"},
            {"publisher": "NHS England", "title": "Greener NHS programme", "url": "https://www.england.nhs.uk/greenernhs/"},
            {"publisher": "NHS Supply Chain", "title": "Annual Report 2023-24", "url": "https://www.supplychain.nhs.uk/about-us/our-publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Newcastle Hospitals provider profile (RTD) — Outstanding rated", "url": "https://www.cqc.org.uk/provider/RTD"}
        ],
        "related": ["The Newcastle Upon Tyne Hospitals NHS Foundation Trust", "Clinical Supplies & Drugs", "NHS Acute Trusts", "NHS Supply Chain", "General supplies & services — Liverpool University Hospitals NHS Foundation Trust", "NHS England"]
    },
    "General supplies & services — University Hospitals Sussex NHS Foundation Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "University Hospitals Sussex NHS Foundation Trust"}],
        "description": "UHSussex's £12.69M general supplies & services line covers non-clinical consumables, linen, catering, hotel-services materials, office supplies and minor expensed equipment across the trust's seven-site footprint — Royal Sussex County (Brighton, with new 3T's Building opened 2023), Princess Royal (Haywards Heath), Worthing Hospital, Southlands (Shoreham), St Richard's (Chichester) and Bognor War Memorial. The trust formed April 2021 by merger of Brighton and Sussex University Hospitals with Western Sussex Hospitals — operational integration ongoing with high-profile patient-safety scrutiny.",
        "beneficiaries": "c. 12,500 WTE staff serving a c. 1.8M Sussex coastal catchment; c. 360,000 ED attendances/yr (RSCH + Worthing + Princess Royal + St Richard's EDs combined); c. 165,000 admissions/yr; trust formed 1 April 2021 by merger of BSUH with Western Sussex Hospitals NHS FTs.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) — IAS 2 Inventories — Procurement Act 2023 — NHS Act 2006 — Health and Care Act 2022 — NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "General supplies & services 2024-25", "value": "£12.69M"},
            {"label": "Trust scale", "value": "Seven-site post-merger acute (RSCH Brighton + Princess Royal + Worthing + Southlands + St Richard's + Bognor); c. 12,500 WTE"},
            {"label": "Merger context", "value": "Trust formed 1 April 2021 by merger of BSUH (Brighton) with Western Sussex Hospitals NHS FTs"},
            {"label": "RSCH 3T's Building + safety scrutiny", "value": "New RSCH 3T's redevelopment Phase 1 opened 2023; Operation Bramber Police investigation — drives compliance + change-mgmt overhead"},
            {"label": "Procurement route", "value": "NHS Supply Chain national framework + Sussex ICS collaborative + trust-direct contracts"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove cancellation re-stocking + agency backfill"},
            {"label": "April 2025 NIC + CPI uplift", "value": "Employer-NIC step-up + non-clinical CPI feed forward unit-cost pressure"},
            {"label": "Funding trajectory", "value": "2021-22 post-merger c. £10M → 2023-24 £12M → 2024-25 £12.69M"},
            {"label": "Delivery body", "value": "Trust Procurement + NHS Supply Chain + Sussex ICS procurement collaborative"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Sussex ICB"},
            {"label": "Evaluation evidence", "value": "CQC RYR inspection; NHSE Operation Bramber assurance reviews; Model Hospital benchmarks; Trust ARA"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2021 separate BSUH + Western Sussex baselines · Successor: full-merger consolidated procurement"}
        ],
        "notes": "UHSussex's non-clinical baseline reflects post-2021 merger integration of Brighton and Sussex University Hospitals with Western Sussex Hospitals NHS FTs, creating one of England's largest geographic-spread acute trusts across seven Sussex coastal sites. The Royal Sussex County Hospital 3T's redevelopment Phase 1 opened in 2023 with modern hotel-services standards, lifting the local baseline. Operation Bramber (Sussex Police investigation into neurosurgery and GI surgery practice) sustains compliance and change-management overhead alongside operational consolidation. Industrial action 2023-24 drove cancellation re-stocking and agency backfill. April 2025 NIC step-up and sustained non-clinical CPI feed forward unit-cost pressure.",
        "sources": [
            {"publisher": "University Hospitals Sussex NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.uhsussex.nhs.uk/about-our-trust/publications/"},
            {"publisher": "NHS Supply Chain", "title": "Annual Report 2023-24", "url": "https://www.supplychain.nhs.uk/about-us/our-publications/"},
            {"publisher": "Care Quality Commission", "title": "UHSussex provider profile (RYR)", "url": "https://www.cqc.org.uk/provider/RYR"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Sussex Integrated Care Board", "title": "ICS strategy + procurement collaborative", "url": "https://www.sussex.ics.nhs.uk/"}
        ],
        "related": ["University Hospitals Sussex NHS Foundation Trust", "Clinical Supplies & Drugs", "NHS Acute Trusts", "NHS Supply Chain", "General supplies & services — Liverpool University Hospitals NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "General supplies & services — Nottingham University Hospitals NHS Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "Nottingham University Hospitals NHS Trust"}],
        "description": "NUH's £12.56M general supplies & services line covers non-clinical consumables, linen, catering, hotel-services materials, office supplies and minor expensed equipment across the trust's two-site academic-tertiary footprint — Queen's Medical Centre (East Midlands Major Trauma Centre) and Nottingham City Hospital. The trust has been in NHSE Recovery Support Programme since 2021 over maternity-services concerns (Donna Ockenden review of NUH maternity ongoing 2022-2025) and recent CQC s.29A warning notices, sustaining elevated change-management and compliance overhead.",
        "beneficiaries": "c. 17,000 WTE staff serving a c. 2.5M Nottinghamshire and East Midlands catchment plus tertiary referrals (East Midlands Major Trauma Centre, BRC research, transplant); c. 360,000 ED attendances/yr (QMC + City EDs combined); c. 200,000 admissions/yr; QMC = East Midlands MTC.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) — IAS 2 Inventories — Procurement Act 2023 — NHS Act 2006 — Health and Care Act 2022 — NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "General supplies & services 2024-25", "value": "£12.56M"},
            {"label": "Trust scale", "value": "Two-site academic-tertiary acute (Queen's Medical Centre + Nottingham City Hospital); c. 17,000 WTE; QMC = East Midlands MTC"},
            {"label": "Recovery Support Programme", "value": "NHSE RSP (NOF4) since 2021; CQC s.29A warning notices on maternity + ED — drives compliance + change-mgmt overhead"},
            {"label": "Donna Ockenden review", "value": "Independent review of NUH maternity services (Donna Ockenden, 2022-2025) — sustained quality + supplies-traceability scrutiny"},
            {"label": "Procurement route", "value": "NHS Supply Chain national framework + Nottingham and Nottinghamshire ICS collaborative + trust-direct contracts"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove cancellation re-stocking + agency backfill"},
            {"label": "April 2025 NIC + CPI uplift", "value": "Employer-NIC step-up + non-clinical CPI feed forward unit-cost pressure"},
            {"label": "Funding trajectory", "value": "2021-22 c. £11M → 2023-24 £12M → 2024-25 £12.56M"},
            {"label": "Delivery body", "value": "Trust Procurement + NHS Supply Chain + Nottingham ICS procurement collaborative"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + NHSE Recovery Support team + Nottingham and Nottinghamshire ICB"},
            {"label": "Evaluation evidence", "value": "CQC RX1 inspection (s.29A notices); Donna Ockenden review reports; NHSE RSP intensive support; Trust ARA"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2006 separate QMC + Nottingham City baselines · Successor: post-RSP exit + ICS scaling"}
        ],
        "notes": "NUH operates one of England's largest academic-tertiary trusts but has been in NHSE Recovery Support Programme since 2021, with CQC s.29A warning notices on maternity and emergency department services and the Donna Ockenden independent review of maternity services running 2022-2025. This sustains elevated compliance, supplies-traceability and change-management overhead on the non-clinical consumables baseline alongside East Midlands Major Trauma Centre activity. Industrial action 2023-24 drove cancellation re-stocking and agency backfill. NHS Supply Chain remains dominant, with Nottingham and Nottinghamshire ICS collaborative scaling as a medium-term lever; April 2025 NIC step-up and sustained non-clinical CPI feed forward unit-cost pressure into 2025-26.",
        "sources": [
            {"publisher": "Nottingham University Hospitals NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.nuh.nhs.uk/our-publications/"},
            {"publisher": "Donna Ockenden / NHS England", "title": "Independent review of maternity services at Nottingham University Hospitals", "url": "https://www.ockendenmaternityreview.org.uk/"},
            {"publisher": "Care Quality Commission", "title": "NUH provider profile (RX1) — Requires Improvement", "url": "https://www.cqc.org.uk/provider/RX1"},
            {"publisher": "NHS Supply Chain", "title": "Annual Report 2023-24", "url": "https://www.supplychain.nhs.uk/about-us/our-publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"}
        ],
        "related": ["Nottingham University Hospitals NHS Trust", "Clinical Supplies & Drugs", "NHS Acute Trusts", "NHS Supply Chain", "General supplies & services — Liverpool University Hospitals NHS Foundation Trust", "Care Quality Commission"]
    },
    "General supplies & services — Sandwell And West Birmingham Hospitals NHS Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "Sandwell And West Birmingham Hospitals NHS Trust"}],
        "description": "Sandwell and West Birmingham's £12.55M general supplies & services line covers non-clinical consumables, linen, catering, hotel-services materials, office supplies and minor expensed equipment across the trust's footprint — Sandwell General Hospital, City Hospital (Birmingham), Birmingham Treatment Centre and the new Midland Metropolitan University Hospital (MMUH) which opened October 2024 after Carillion-collapse rescue. The MMUH opening drives a step-change in the non-clinical baseline as City + Sandwell acute services consolidate.",
        "beneficiaries": "c. 8,500 WTE staff serving a c. 530,000 catchment across Sandwell, west Birmingham and Ladywood; c. 220,000 ED attendances/yr (Sandwell + City + new MMUH ED); c. 90,000 admissions/yr; MMUH opened October 2024 — Carillion-rescue completion, replaces City + Sandwell acute services.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) — IAS 2 Inventories — Procurement Act 2023 — NHS Act 2006 — Health and Care Act 2022 — NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "General supplies & services 2024-25", "value": "£12.55M"},
            {"label": "Trust scale", "value": "Multi-site acute transitioning to MMUH-centred (Sandwell + City + Birmingham Treatment Centre + new MMUH); c. 8,500 WTE"},
            {"label": "MMUH opening Oct 2024", "value": "Midland Metropolitan University Hospital opened October 2024 — Carillion-rescue completion (Carillion Jan 2018 collapse + Balfour Beatty completion); modern hotel-services baseline"},
            {"label": "Catchment deprivation", "value": "Sandwell + west Birmingham — among UK's most deprived urban catchments; high IMD drives ED + maternity throughput"},
            {"label": "Procurement route", "value": "NHS Supply Chain national framework + Black Country ICS collaborative + trust-direct contracts"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove cancellation re-stocking + agency backfill"},
            {"label": "April 2025 NIC + CPI uplift", "value": "Employer-NIC step-up + non-clinical CPI feed forward unit-cost pressure"},
            {"label": "Funding trajectory", "value": "2021-22 c. £11M → 2023-24 £12M → 2024-25 £12.55M; 2025-26 step-up expected from MMUH first full operational year"},
            {"label": "Delivery body", "value": "Trust Procurement + NHS Supply Chain + Black Country ICS procurement collaborative + (post-MMUH) FM contractor cohort"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Black Country ICB"},
            {"label": "Evaluation evidence", "value": "CQC RXK inspection; NAO Carillion + MMUH completion reports; Trust ARA"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-MMUH separate Sandwell + City acute baselines · Successor: post-MMUH consolidated single-site procurement (City + Sandwell acute decant)"}
        ],
        "notes": "Sandwell and West Birmingham's non-clinical baseline is in mid-transition as the new Midland Metropolitan University Hospital opened in October 2024, completing the Carillion-rescue saga (Carillion's Jan 2018 collapse abandoned the original PFI build, with Balfour Beatty taking over completion). MMUH consolidates City and Sandwell acute services, with the 2024-25 figure capturing the transition's first months and 2025-26 expected to step up as City Hospital decants. The catchment is among the UK's most deprived, sustaining ED and maternity throughput. Industrial action 2023-24 drove cancellation re-stocking and agency backfill. April 2025 NIC step-up and sustained CPI feed forward unit-cost pressure.",
        "sources": [
            {"publisher": "Sandwell and West Birmingham Hospitals NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.swbh.nhs.uk/about-us/key-publications/"},
            {"publisher": "National Audit Office", "title": "Investigation into the rescue of Carillion's PFI hospital contracts", "url": "https://www.nao.org.uk/reports/investigation-into-the-rescue-of-carillions-pfi-hospital-contracts/"},
            {"publisher": "NHS Supply Chain", "title": "Annual Report 2023-24", "url": "https://www.supplychain.nhs.uk/about-us/our-publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Sandwell and West Birmingham provider profile (RXK)", "url": "https://www.cqc.org.uk/provider/RXK"}
        ],
        "related": ["Sandwell And West Birmingham Hospitals NHS Trust", "Clinical Supplies & Drugs", "NHS Acute Trusts", "NHS Supply Chain", "General supplies & services — Liverpool University Hospitals NHS Foundation Trust", "New Hospital Programme"]
    },
    "Establishment costs — St George's University Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "St George's University Hospitals NHS Foundation Trust"}],
        "description": "St George's £12.48M establishment costs line covers postage, telephony, printing, stationery, training/courses, advertising, subscriptions and external audit fees at the trust's Tooting academic-tertiary site, plus QMH Roehampton and Nelson Health Centre community footprint. The trust operates as part of the GESH (St George's, Epsom and St Helier) group arrangement (chair-in-common since 2021) which is reshaping shared corporate-services overhead, while Frontline Digitisation EPR rollout drives training-related establishment cost.",
        "beneficiaries": "c. 9,000 WTE staff serving a c. 3.5M south-west London + Surrey catchment plus tertiary national referrals (cardiac surgery, neurosciences, major trauma); c. 200,000 ED attendances/yr at St George's ED; c. 110,000 admissions/yr; St George's = SW London + Surrey Major Trauma Centre.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) — IAS 1 Presentation of Financial Statements — NHS Act 2006 — Health and Care Act 2022 — NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£12.48M"},
            {"label": "Trust scale", "value": "Single academic-tertiary site (St George's, Tooting) + QMH Roehampton + Nelson Health Centre; c. 9,000 WTE; SW London + Surrey MTC"},
            {"label": "GESH group arrangement", "value": "St George's + Epsom and St Helier chair-in-common since 2021 → GESH group; shared corporate functions developing"},
            {"label": "Frontline Digitisation EPR", "value": "EPR rollout drives training/change-management establishment cost"},
            {"label": "Tertiary specialty", "value": "Cardiac surgery + neurosciences + major trauma + St George's University of London medical school colocation"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove communication + scheduling overheads"},
            {"label": "April 2025 NIC + CPI uplift", "value": "Employer-NIC step-up + telephony/postage CPI feed forward unit-cost pressure"},
            {"label": "Funding trajectory", "value": "2021-22 c. £10M → 2023-24 £11M → 2024-25 £12.48M — EPR + GESH integration overheads"},
            {"label": "Delivery body", "value": "Trust Corporate Services + Communications + Finance + (developing) GESH shared functions"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + South West London ICB + Surrey Heartlands ICB"},
            {"label": "Evaluation evidence", "value": "CQC RJ7 inspection; GESH group-model business case; Trust ARA"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2021 stand-alone establishment baseline · Successor: GESH group consolidated overhead"}
        ],
        "notes": "St George's establishment-costs baseline reflects the trust's status as a south-west London + Surrey Major Trauma Centre and academic teaching hospital co-located with St George's, University of London medical school, alongside the developing GESH group arrangement (chair-in-common with Epsom and St Helier University Hospitals NHS Trust since 2021) which is reshaping shared back-office and corporate-services consolidation. Frontline Digitisation EPR rollout adds training-related establishment cost. Industrial action 2023-24 drove communication and scheduling overheads. April 2025 NIC step-up and sustained CPI on postage/telephony/training feed forward unit-cost pressure into 2025-26 as GESH group-model integration matures.",
        "sources": [
            {"publisher": "St George's University Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.stgeorges.nhs.uk/about/publications/"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme (EPR)", "url": "https://www.england.nhs.uk/digitaltechnology/connecting-health-and-care-through-technology/electronic-patient-record-systems/"},
            {"publisher": "South West London Integrated Care Board", "title": "GESH group arrangement", "url": "https://www.southwestlondon.icb.nhs.uk/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "St George's provider profile (RJ7)", "url": "https://www.cqc.org.uk/provider/RJ7"}
        ],
        "related": ["St George's University Hospitals NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Epsom and St Helier University Hospitals NHS Trust", "Establishment costs — North West Anglia NHS Foundation Trust", "NHS England"]
    },
    "General supplies & services — Guy's & St Thomas' NHS Foundation Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "Guy's & St Thomas' NHS Foundation Trust"}],
        "description": "GSTT's £12.47M general supplies & services line covers non-clinical consumables, linen, catering, hotel-services materials, office supplies and minor expensed equipment across the trust's central London academic-tertiary footprint — Guy's Hospital (Southwark, including Cancer Centre 2016 and Tower Wing), St Thomas' Hospital (Lambeth, opposite Parliament), Royal Brompton (national heart-lung specialist, joined 2021) and Harefield (Hillingdon). Tertiary specialties (cardiac, transplant, oncology, fetal medicine) drive elevated non-clinical baseline alongside teaching-hospital scale.",
        "beneficiaries": "c. 22,500 WTE staff serving a c. 1.4M central + south-east London catchment plus tertiary national + international referrals (cardiac, transplant, fetal medicine, oncology); c. 215,000 ED attendances/yr at St Thomas' ED; c. 230,000 admissions/yr; merged with Royal Brompton & Harefield NHS FT 1 February 2021.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) — IAS 2 Inventories — Procurement Act 2023 — NHS Act 2006 — Health and Care Act 2022 — NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "General supplies & services 2024-25", "value": "£12.47M"},
            {"label": "Trust scale", "value": "Multi-site academic-tertiary acute (Guy's + St Thomas' + Royal Brompton + Harefield); c. 22,500 WTE"},
            {"label": "Royal Brompton merger", "value": "Royal Brompton & Harefield NHS FT merged into GSTT 1 Feb 2021 — national heart-lung specialist consolidation"},
            {"label": "Tertiary specialty", "value": "Cardiac (Royal Brompton + Harefield) + transplant + fetal medicine (Evelina London) + oncology (Guy's Cancer Centre 2016) + KCL BRC"},
            {"label": "Procurement route", "value": "NHS Supply Chain + SEL ICS collaborative + GSTT Procurement (one of UK's larger NHS procurement teams) + trust-direct"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove cancellation re-stocking + agency backfill"},
            {"label": "April 2025 NIC + CPI uplift", "value": "Employer-NIC step-up + non-clinical CPI feed forward unit-cost pressure; Greener NHS sustainable-procurement reformulation"},
            {"label": "Funding trajectory", "value": "2021-22 post-Brompton-merger c. £11M → 2023-24 £12M → 2024-25 £12.47M"},
            {"label": "Delivery body", "value": "GSTT Procurement + NHS Supply Chain + SEL ICS procurement collaborative"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + Specialised Commissioning (cardiac/transplant) + DHSC + South East London ICB"},
            {"label": "Evaluation evidence", "value": "CQC RJ1 inspection; KCL BRC + GSTT Charity reporting; Greener NHS reporting; Model Hospital benchmarks"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2021 separate GSTT + Royal Brompton & Harefield baselines · Successor: post-merger consolidated procurement"}
        ],
        "notes": "GSTT's non-clinical consumables baseline reflects post-2021 consolidation of Royal Brompton & Harefield NHS Foundation Trust (national heart-lung specialist) into the trust, alongside the trust's central London academic-tertiary scale and tertiary specialty mix (cardiac, transplant, fetal medicine, oncology) that broadens the baseline beyond standard acute peers. The trust runs one of the UK's larger NHS procurement teams alongside NHS Supply Chain framework call-offs. Industrial action 2023-24 drove cancellation re-stocking and agency backfill. April 2025 NIC step-up and sustained non-clinical CPI feed forward unit-cost pressure; GSTT's Greener NHS engagement shapes sustainable-procurement reformulation across catering, linen and packaging.",
        "sources": [
            {"publisher": "Guy's & St Thomas' NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.guysandstthomas.nhs.uk/about-us/our-publications/"},
            {"publisher": "NHS England", "title": "Greener NHS programme", "url": "https://www.england.nhs.uk/greenernhs/"},
            {"publisher": "NHS Supply Chain", "title": "Annual Report 2023-24", "url": "https://www.supplychain.nhs.uk/about-us/our-publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Guy's & St Thomas' provider profile (RJ1)", "url": "https://www.cqc.org.uk/provider/RJ1"}
        ],
        "related": ["Guy's & St Thomas' NHS Foundation Trust", "Clinical Supplies & Drugs", "NHS Acute Trusts", "NHS Supply Chain", "General supplies & services — Liverpool University Hospitals NHS Foundation Trust", "NHS England"]
    },
    "Establishment costs — Oxford University Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "Oxford University Hospitals NHS Foundation Trust"}],
        "description": "OUH's £12.38M establishment costs line covers postage, telephony, printing, stationery, training/courses, advertising, subscriptions and external audit fees across the trust's four-site academic-tertiary footprint — John Radcliffe Hospital (Headington, including Children's, Women's and Major Trauma), Churchill Hospital (oncology + renal), Nuffield Orthopaedic Centre and Horton General Hospital (Banbury). Frontline Digitisation EPR (Oracle Health/Cerner Millennium) rollout drives training-related establishment cost, alongside University of Oxford BRC research-administration overhead.",
        "beneficiaries": "c. 13,500 WTE staff serving a c. 750,000 Oxfordshire catchment plus tertiary national + international referrals (oncology, transplant, neurosciences, major trauma); c. 200,000 ED attendances/yr (John Radcliffe + Horton EDs combined); c. 130,000 admissions/yr; John Radcliffe = Thames Valley Major Trauma Centre.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) — IAS 1 Presentation of Financial Statements — NHS Act 2006 — Health and Care Act 2022 — NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£12.38M"},
            {"label": "Trust scale", "value": "Four-site academic-tertiary acute (John Radcliffe + Churchill + Nuffield Orthopaedic + Horton General); c. 13,500 WTE; JR = Thames Valley MTC"},
            {"label": "University of Oxford BRC", "value": "NIHR Oxford Biomedical Research Centre + Oxford Medical School colocation — drives research-admin establishment overhead"},
            {"label": "Frontline Digitisation EPR", "value": "Oracle Health (Cerner Millennium) EPR rollout drives training/change-management establishment cost"},
            {"label": "Tertiary specialty", "value": "Oncology (Churchill) + transplant + neurosciences + major trauma + paediatric quaternary (Children's Hospital)"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove communication + scheduling overheads"},
            {"label": "April 2025 NIC + CPI uplift", "value": "Employer-NIC step-up + telephony/postage CPI feed forward unit-cost pressure"},
            {"label": "Funding trajectory", "value": "2021-22 c. £10M → 2023-24 £12M → 2024-25 £12.38M — EPR + research-admin overheads"},
            {"label": "Delivery body", "value": "Trust Corporate Services + Communications + Finance + Buckinghamshire, Oxfordshire and Berkshire West ICS"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + BOB ICB + NIHR (BRC)"},
            {"label": "Evaluation evidence", "value": "CQC RTH inspection; NIHR BRC reporting; NHSE Frontline Digitisation reporting; Trust ARA"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2007 separate Oxford Radcliffe + Nuffield Orthopaedic baselines · Successor: post-EPR digitised baseline"}
        ],
        "notes": "OUH's establishment-costs baseline reflects its position as one of England's largest academic-tertiary acute trusts, co-located with University of Oxford Medical School and the NIHR Oxford Biomedical Research Centre, sustaining substantial research-administration and clinical-trials governance overhead alongside Thames Valley Major Trauma Centre activity. Frontline Digitisation EPR rollout (Oracle Health/Cerner Millennium platform) drives training-related establishment cost. Industrial action 2023-24 drove communication and scheduling overheads. April 2025 NIC step-up and sustained CPI on postage/telephony/training feed forward unit-cost pressure into 2025-26 as the EPR rollout completes deployment phases.",
        "sources": [
            {"publisher": "Oxford University Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.ouh.nhs.uk/about/publications/"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme (EPR)", "url": "https://www.england.nhs.uk/digitaltechnology/connecting-health-and-care-through-technology/electronic-patient-record-systems/"},
            {"publisher": "NIHR Oxford Biomedical Research Centre", "title": "Oxford BRC overview", "url": "https://oxfordbrc.nihr.ac.uk/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "OUH provider profile (RTH)", "url": "https://www.cqc.org.uk/provider/RTH"}
        ],
        "related": ["Oxford University Hospitals NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Establishment costs — Cambridge University Hospitals NHS Foundation Trust", "Establishment costs — Hampshire Hospitals NHS Foundation Trust", "NHS England"]
    },
    "General supplies & services — Epsom and St Helier University Hospitals NHS Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "Epsom and St Helier University Hospitals NHS Trust"}],
        "description": "ESTH's £12.25M general supplies & services line covers non-clinical consumables, linen, catering, hotel-services materials, office supplies and minor expensed equipment across the trust's two acute sites (Epsom Hospital + St Helier Hospital, Carshalton) plus Sutton and community-clinic footprint. The trust is in the New Hospital Programme cohort with a planned new specialist emergency-care hospital at Sutton, with Jan 2025 NHP Reset confirming continued planning under revised timelines, and operates the GESH group with St George's since 2021.",
        "beneficiaries": "c. 5,500 WTE staff serving a c. 490,000 south-west London + Surrey catchment (Epsom, Sutton, Merton); c. 175,000 ED attendances/yr (Epsom + St Helier EDs combined); c. 60,000 admissions/yr; St Helier Hospital one of NHS's oldest 1930s estates with significant condition backlog.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) — IAS 2 Inventories — Procurement Act 2023 — NHS Act 2006 — Health and Care Act 2022 — NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "General supplies & services 2024-25", "value": "£12.25M"},
            {"label": "Trust scale", "value": "Two-site acute (Epsom + St Helier) + Sutton Hospital + community; c. 5,500 WTE; c. 175,000 ED attendances/yr"},
            {"label": "NHP cohort + estate condition", "value": "Planned new specialist emergency-care hospital at Sutton in NHP — Jan 2025 Reset continued; St Helier 1930s estate driving decant churn"},
            {"label": "GESH group arrangement", "value": "ESTH + St George's chair-in-common since 2021 → GESH group; shared procurement functions developing"},
            {"label": "Procurement route", "value": "NHS Supply Chain national framework + South West London ICS collaborative + GESH shared procurement"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove cancellation re-stocking + agency backfill"},
            {"label": "April 2025 NIC + CPI uplift", "value": "Employer-NIC step-up + non-clinical CPI feed forward unit-cost pressure"},
            {"label": "Funding trajectory", "value": "2021-22 c. £10M → 2023-24 £11M → 2024-25 £12.25M"},
            {"label": "Delivery body", "value": "Trust Procurement + (developing) GESH shared procurement + NHS Supply Chain + SWL ICS collaborative"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + South West London ICB + Surrey Heartlands ICB + NHP team"},
            {"label": "Evaluation evidence", "value": "CQC RVR inspection; NHP business case + Reset Jan 2025; GESH group-model business case; Trust ARA"},
            {"label": "Predecessor / successor", "value": "Predecessor: stand-alone trust pre-GESH · Successor: GESH consolidated procurement + post-Sutton rebuild baseline"}
        ],
        "notes": "ESTH's non-clinical consumables baseline is shaped by aging St Helier Hospital estate (1930s build with significant condition backlog driving decant + interim-works re-stocking churn) alongside the New Hospital Programme planning for a new specialist emergency-care hospital at Sutton — January 2025 NHP Reset confirmed continued planning under revised timelines, with planning + business-case overhead feeding establishment + supplies churn. The GESH group arrangement (chair-in-common with St George's University Hospitals NHS FT since 2021) is reshaping shared procurement and corporate functions. Industrial action 2023-24 drove cancellation re-stocking and agency backfill. NHS Supply Chain remains dominant; April 2025 NIC step-up and sustained non-clinical CPI feed forward unit-cost pressure.",
        "sources": [
            {"publisher": "Epsom and St Helier University Hospitals NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.epsom-sthelier.nhs.uk/publications"},
            {"publisher": "Department of Health and Social Care", "title": "New Hospital Programme — plan for implementation (Jan 2025 Reset)", "url": "https://www.gov.uk/government/publications/new-hospital-programme-plan-for-implementation"},
            {"publisher": "NHS Supply Chain", "title": "Annual Report 2023-24", "url": "https://www.supplychain.nhs.uk/about-us/our-publications/"},
            {"publisher": "Care Quality Commission", "title": "ESTH provider profile (RVR)", "url": "https://www.cqc.org.uk/provider/RVR"},
            {"publisher": "South West London Integrated Care Board", "title": "GESH group arrangement", "url": "https://www.southwestlondon.icb.nhs.uk/"}
        ],
        "related": ["Epsom and St Helier University Hospitals NHS Trust", "Clinical Supplies & Drugs", "NHS Acute Trusts", "St George's University Hospitals NHS Foundation Trust", "New Hospital Programme", "NHS Supply Chain"]
    },
    "Social security & levy — East Cheshire NHS Trust": {
        "aliases": [{"name": "Social security & levy", "parent": "East Cheshire NHS Trust"}],
        "description": "East Cheshire's £12.24M social security & levy line covers employer NIC and Apprenticeship Levy on the trust's c. 2,800-WTE integrated acute + community workforce. The trust runs Macclesfield District General Hospital plus Congleton War Memorial Hospital and integrated community services across east Cheshire. Group-model integration with Mid Cheshire Hospitals NHS FT is in development under Cheshire & Merseyside ICS arrangements. April 2025 NIC step-up dominates the forward-cost picture for one of England's smaller acute trusts.",
        "beneficiaries": "c. 2,800 WTE staff serving a c. 200,000 east Cheshire catchment (Macclesfield, Congleton, Wilmslow, Knutsford); c. 65,000 ED attendances/yr at Macclesfield ED; c. 30,000 admissions/yr; integrated community workforce (district nursing + community-paediatric + therapies).",
        "legal_basis": "Social Security Contributions and Benefits Act 1992 (employer NIC) — Apprenticeship Levy (Finance Act 2016, s.99) — DHSC Group Accounting Manual 2024-25 — NHS Act 2006 — Health and Care Act 2022 — NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "Social security & levy 2024-25", "value": "£12.24M"},
            {"label": "Trust scale", "value": "Single acute site (Macclesfield DGH) + Congleton War Memorial + integrated east Cheshire community services; c. 2,800 WTE"},
            {"label": "Composition + Apprenticeship Levy", "value": "Employer NIC (Class 1 secondary) + Apprenticeship Levy (0.5% pay bill > £3M, c. £0.7-1.0M/yr)"},
            {"label": "April 2025 NIC step-up", "value": "Rate 13.8% → 15.0% + secondary threshold £9,100 → £5,000; partial NHSE compensation via Cheshire & Merseyside ICB"},
            {"label": "Group-model context", "value": "Group-model integration with Mid Cheshire Hospitals NHS FT in development under Cheshire & Merseyside ICS — leadership arrangements evolving"},
            {"label": "Integrated community workforce", "value": "District nursing + therapies + community-paediatric — broadens NIC base vs acute-only peers"},
            {"label": "Industrial action 2023-24 effect", "value": "Junior-doctor + consultant strikes drove agency-locum backfill"},
            {"label": "Funding trajectory", "value": "2021-22 c. £10M → 2023-24 £11.5M → 2024-25 £12.24M; 2025-26 forward step-up"},
            {"label": "Delivery body", "value": "Trust HR + Payroll + NHSBSA Employment Services + HMRC remittance"},
            {"label": "Policy owner", "value": "HM Treasury (NIC + Levy) + DHSC + NHSE Workforce + Cheshire and Merseyside ICB"},
            {"label": "Evaluation evidence", "value": "CQC RJN inspection; NHSE workforce returns; OBR EFO NIC line; Trust ARA workforce remuneration"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2017 pre-Apprenticeship Levy regime · Successor: post-Apr 2025 NIC + Mid Cheshire group-model"}
        ],
        "notes": "East Cheshire is one of England's smaller acute trusts and operates an integrated acute + community workforce model alongside Macclesfield DGH, with district nursing, therapies and community-paediatric teams broadening the employer-NIC base. Group-model integration with Mid Cheshire Hospitals NHS Foundation Trust is in development under Cheshire & Merseyside ICS, with chair and leadership arrangements evolving; medium-term consolidation will reshape the workforce-cost reporting boundary. Industrial action 2023-24 drove agency-locum backfill on acute-medicine and emergency-medicine rotas. The April 2025 employer-NIC step-up to 15% with the threshold drop to £5,000 is the dominant 2025-26 forward driver, with partial NHSE NIC compensation flowing through Cheshire & Merseyside ICB allocation.",
        "sources": [
            {"publisher": "East Cheshire NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.eastcheshire.nhs.uk/About-The-Trust/publications/annual-reports.htm"},
            {"publisher": "HM Revenue and Customs", "title": "Employer NIC rates and thresholds 2025-26", "url": "https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2025-to-2026"},
            {"publisher": "Office for Budget Responsibility", "title": "Economic and Fiscal Outlook (employer NIC effect)", "url": "https://obr.uk/efo/economic-and-fiscal-outlook/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "East Cheshire provider profile (RJN)", "url": "https://www.cqc.org.uk/provider/RJN"}
        ],
        "related": ["East Cheshire NHS Trust", "Staff Costs", "NHS Acute Trusts", "Mid Cheshire Hospitals NHS Foundation Trust", "Social security & levy — Ashford and St Peter's Hospitals NHS Foundation Trust", "HM Revenue and Customs"]
    },
    "General supplies & services — Northumbria Healthcare NHS Foundation Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "Northumbria Healthcare NHS Foundation Trust"}],
        "description": "Northumbria Healthcare's £12.20M general supplies & services line covers non-clinical consumables, linen, catering, hotel-services materials, office supplies and minor expensed equipment across the trust's distinctive emergency-care + planned-care site model — Northumbria Specialist Emergency Care Hospital (Cramlington, opened 2015 — England's first purpose-built specialist emergency-care hospital), Wansbeck General, North Tyneside General and Hexham General. The trust runs Northumbria Healthcare Facilities Management (NHFM) wholly-owned subsidiary, shaping non-clinical service delivery.",
        "beneficiaries": "c. 11,000 WTE staff serving a c. 500,000 Northumberland and North Tyneside catchment plus integrated community + adult social care services; c. 250,000 ED attendances/yr (Cramlington main + walk-in centres); c. 90,000 admissions/yr; CQC Outstanding rated; integrated adult social care delivery via partnership with Northumberland County Council.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) — IAS 2 Inventories — Procurement Act 2023 — NHS Act 2006 — Health and Care Act 2022 — NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "General supplies & services 2024-25", "value": "£12.20M"},
            {"label": "Trust scale", "value": "Multi-site acute (Cramlington Specialist Emergency + Wansbeck + North Tyneside + Hexham); c. 11,000 WTE; CQC Outstanding"},
            {"label": "Cramlington model + NHFM SubCo", "value": "Cramlington opened 2015 — England's first purpose-built specialist emergency-care hospital; NHFM wholly-owned subsidiary employs FM workforce"},
            {"label": "Integrated services model", "value": "Trust integrates community services + adult social care under Northumberland County Council partnership — broadens consumables baseline"},
            {"label": "Procurement route", "value": "NHS Supply Chain national framework + North East and North Cumbria ICS collaborative + NHFM SubCo + trust-direct"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove cancellation re-stocking + agency backfill"},
            {"label": "April 2025 NIC + CPI uplift", "value": "Employer-NIC step-up + non-clinical CPI feed forward unit-cost pressure"},
            {"label": "Funding trajectory", "value": "2021-22 c. £10M → 2023-24 £11M → 2024-25 £12.20M"},
            {"label": "Delivery body", "value": "Trust Procurement + NHFM SubCo + NHS Supply Chain + NENC ICS procurement collaborative"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + North East and North Cumbria ICB + Northumberland County Council"},
            {"label": "Evaluation evidence", "value": "CQC RTF Outstanding rated; NIHR research collaborative; Model Hospital benchmarks; Trust ARA"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2015 traditional DGH-emergency model · Successor: ongoing care-separation maturation"}
        ],
        "notes": "Northumbria Healthcare's non-clinical baseline reflects its distinctive emergency-care + planned-care separation model — Cramlington opened 2015 as England's first purpose-built specialist emergency-care hospital, with Wansbeck General, North Tyneside General and Hexham General delivering planned care. Northumbria Healthcare Facilities Management (NHFM) wholly-owned subsidiary employs the FM workforce under SubCo VAT/cost arrangements scrutinised in the wider NHS SubCo policy debate. The trust integrates community services and adult social care under partnership with Northumberland County Council, broadening the consumables baseline. Industrial action 2023-24 drove cancellation re-stocking; April 2025 NIC step-up and CPI feed forward.",
        "sources": [
            {"publisher": "Northumbria Healthcare NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.northumbria.nhs.uk/about-us/who-we-are/our-publications/"},
            {"publisher": "Care Quality Commission", "title": "Northumbria Healthcare provider profile (RTF) — Outstanding rated", "url": "https://www.cqc.org.uk/provider/RTF"},
            {"publisher": "NHS Supply Chain", "title": "Annual Report 2023-24", "url": "https://www.supplychain.nhs.uk/about-us/our-publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "North East and North Cumbria Integrated Care Board", "title": "ICS strategy + procurement collaborative", "url": "https://northeastnorthcumbria.nhs.uk/"}
        ],
        "related": ["Northumbria Healthcare NHS Foundation Trust", "Clinical Supplies & Drugs", "NHS Acute Trusts", "NHS Supply Chain", "General supplies & services — The Newcastle Upon Tyne Hospitals NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "General supplies & services — Medway NHS Foundation Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "Medway NHS Foundation Trust"}],
        "description": "Medway's £11.92M general supplies & services line covers non-clinical consumables, linen, catering, hotel-services materials, office supplies and minor expensed equipment at Medway Maritime Hospital (Gillingham) — the trust's single-site acute footprint serving the Medway towns and Swale. The trust exited NHSE Recovery Support Programme (NOF4) in 2023 after a long period in special measures from 2013, with continued post-RSP focus on operational consistency and CQC-driven compliance reshaping non-clinical operating disciplines.",
        "beneficiaries": "c. 5,500 WTE staff serving a c. 460,000 catchment across Medway towns (Chatham, Gillingham, Rochester, Strood) and Swale; c. 130,000 ED attendances/yr at Medway Maritime ED; c. 75,000 admissions/yr; trust exited NHSE Recovery Support Programme 2023 after 10 years in heightened scrutiny.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) — IAS 2 Inventories — Procurement Act 2023 — NHS Act 2006 — Health and Care Act 2022 — NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "General supplies & services 2024-25", "value": "£11.92M"},
            {"label": "Trust scale", "value": "Single-site acute (Medway Maritime Hospital, Gillingham); c. 5,500 WTE; c. 130,000 ED attendances/yr"},
            {"label": "Recovery Support Programme exit", "value": "Trust exited NHSE RSP / NOF4 2023 after 10 years in heightened scrutiny (special measures from 2013) — sustained operational overhead"},
            {"label": "Catchment deprivation", "value": "Medway towns + Swale — significant IMD deprivation; high ED + maternity activity"},
            {"label": "Procurement route", "value": "NHS Supply Chain national framework + Kent and Medway ICS collaborative + trust-direct contracts"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove cancellation re-stocking + agency backfill"},
            {"label": "April 2025 NIC + CPI uplift", "value": "Employer-NIC step-up + non-clinical CPI feed forward unit-cost pressure"},
            {"label": "Funding trajectory", "value": "2021-22 c. £10M → 2023-24 £11M → 2024-25 £11.92M"},
            {"label": "Delivery body", "value": "Trust Procurement + NHS Supply Chain + Kent and Medway ICS procurement collaborative"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Kent and Medway ICB"},
            {"label": "Evaluation evidence", "value": "CQC RPA inspection (post-RSP exit); NHSE RSP exit assurance review; Trust ARA"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2023 RSP-period baseline · Successor: post-RSP-exit operational baseline + ICS scaling"}
        ],
        "notes": "Medway's non-clinical baseline reflects the trust's 2023 emergence from one of the longest periods in NHS heightened scrutiny — the trust entered special measures in 2013 and exited NHSE Recovery Support Programme in 2023 after a decade of intensive support, with continued post-RSP focus on operational consistency, CQC-driven compliance and supplies-traceability reshaping non-clinical operating disciplines. The Medway towns and Swale catchment carries significant IMD deprivation, sustaining ED and maternity activity. Industrial action 2023-24 drove cancellation re-stocking and agency backfill. NHS Supply Chain remains dominant, with Kent and Medway ICS collaborative scaling as a medium-term lever; April 2025 NIC step-up and CPI feed forward.",
        "sources": [
            {"publisher": "Medway NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.medway.nhs.uk/about-us/publications/"},
            {"publisher": "Care Quality Commission", "title": "Medway provider profile (RPA)", "url": "https://www.cqc.org.uk/provider/RPA"},
            {"publisher": "NHS England", "title": "Recovery Support Programme — exits 2023", "url": "https://www.england.nhs.uk/publication/nhs-oversight-framework/"},
            {"publisher": "NHS Supply Chain", "title": "Annual Report 2023-24", "url": "https://www.supplychain.nhs.uk/about-us/our-publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"}
        ],
        "related": ["Medway NHS Foundation Trust", "Clinical Supplies & Drugs", "NHS Acute Trusts", "NHS Supply Chain", "General supplies & services — Liverpool University Hospitals NHS Foundation Trust", "Care Quality Commission"]
    },
}
