# -*- coding: utf-8 -*-
# Phase 2 Acute slice 2 — chunk 46 (17 NHS Acute Trust orphan sub-lines)
# Hand-curated trust-specific PROGRAMME-archetype enrichment entries.
# Structural contract per docs/archetype_briefs.md.

NEW = {}

NEW["Lease expenditure — Oxford University Hospitals NHS Foundation Trust"] = {
    "aliases": [{"name": "Lease expenditure", "parent": "Oxford University Hospitals NHS Foundation Trust"}],
    "description": "Operating lease expenditure (post-IFRS 16) at OUH — covering short-life and low-value leased equipment, clinic and office space held outside Right-of-Use balances under DHSC GAM treatment, plus operating leases on the trust's vehicle fleet and modular plant supporting the John Radcliffe, Churchill, Nuffield Orthopaedic Centre and Horton General sites across the BOB ICS footprint.",
    "beneficiaries": "Adult acute, paediatric quaternary, specialist cardiothoracic, oncology (Churchill), orthopaedic (NOC) and obstetric inpatients across Oxfordshire and beyond (~750,000 catchment with national tertiary draw); c. 1.4M outpatient + inpatient + day-case contacts/yr; c. 13,500 WTE across 4 main sites.",
    "legal_basis": "IFRS 16 Leases (as adapted by FReM and DHSC GAM ch.7) · DHSC Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · Landlord and Tenant Act 1954",
    "key_stats": [
        {"label": "Lease expenditure 2024-25", "value": "£0.159M"},
        {"label": "Share of trust total opex", "value": "<0.02% of c. £1.6B"},
        {"label": "Coverage", "value": "Short-life (<12 months) and low-value (<£5k) leases excluded from RoU under GAM treatment"},
        {"label": "Site footprint", "value": "John Radcliffe (Headington) + Churchill + Nuffield Orthopaedic Centre + Horton General (Banbury) + research clinic estate"},
        {"label": "Specific driver", "value": "Modular research and clinic equipment hire + minor vehicle fleet + temp office space leases supporting University of Oxford-OUH academic partnership"},
        {"label": "YoY change", "value": "c. +5-7% (lease re-pricing, fleet electrification mix shift)"},
        {"label": "Delivery body", "value": "OUH Estates & Facilities + Procurement + NHS Supply Chain framework leasing"},
        {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Buckinghamshire, Oxfordshire and Berkshire West (BOB) ICB"},
        {"label": "Funding trajectory", "value": "Stable to slight uplift; AHSC/AHSN partnership with University of Oxford drives modular research-equipment leases; CNZ fleet electrification gradually re-prices"},
        {"label": "Evaluation evidence", "value": "OUH ARA 2023-24 Note (lease disclosures); CQC inspection (RTH); NHSE Operational Plan returns; Model Hospital benchmarking"},
        {"label": "Predecessor / successor", "value": "Predecessor: pre-IFRS 16 operating-lease classification (pre-2022) · Successor: continued GAM treatment of low-value/short-life items + ongoing OUH 2024-29 estates strategy refresh"}
    ],
    "notes": "OUH's £0.159M lease line is a small but recurring operational charge covering items that fall outside the IFRS 16 Right-of-Use threshold under DHSC GAM ch.7 — short-life equipment hire, low-value leases and minor fleet items. The trust's complex 4-site academic-medical-centre footprint and deep research partnership with the University of Oxford generate a long tail of small leased items across labs, modular research clinics and shared equipment. OUH is part of BOB ICB and a national tertiary anchor for transplantation, cardiothoracic, neurosciences and orthopaedics; the line is shaped by the academic-research workload mix and the Carbon Net Zero fleet electrification programme. The OUH Improvement Programme and the 2024-29 estates strategy refresh further shape lease vs RoU classification.",
    "sources": [
        {"publisher": "Oxford University Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.ouh.nhs.uk/about/publications/annual-report.aspx"},
        {"publisher": "Care Quality Commission", "title": "OUH provider profile (RTH)", "url": "https://www.cqc.org.uk/provider/RTH"},
        {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (ch.7 Leases)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
        {"publisher": "HM Treasury", "title": "FReM IFRS 16 adaptation", "url": "https://www.gov.uk/government/publications/government-financial-reporting-manual-2024-25"},
        {"publisher": "NHS England", "title": "BOB ICB system overview", "url": "https://www.bobicb.nhs.uk/"}
    ],
    "related": [
        "Oxford University Hospitals NHS Foundation Trust",
        "Premises & Infrastructure",
        "NHS England",
        "Department of Health and Social Care"
    ]
}

NEW["PFI / LIFT charges — Hampshire Hospitals NHS Foundation Trust"] = {
    "aliases": [{"name": "PFI / LIFT charges", "parent": "Hampshire Hospitals NHS Foundation Trust"}],
    "description": "Hampshire Hospitals' £0.158M residual PFI / LIFT charges line covers small ancillary service-concession arrangements (residual NHS LIFT primary-care/community premises, small modular schemes) outside the trust's main estate. The trust runs Royal Hampshire County Hospital (Winchester), Basingstoke and North Hampshire Hospital and Andover War Memorial Hospital across the Hampshire and Isle of Wight ICS — neither main acute hospital is on a major PFI scheme, so this line is a residual tail of historic LIFT/IFRIC 12 arrangements.",
    "beneficiaries": "Acute inpatients across Royal Hampshire County (Winchester ~430 beds), Basingstoke and North Hampshire (~450 beds — incl. national peritoneal-malignancy centre), and Andover War Memorial; serving c. 600,000 across Hampshire; c. 95,000 ED attendances/yr (combined); c. 5,800 WTE.",
    "legal_basis": "IFRIC 12 Service Concession Arrangements · IFRS 16 Leases (post-2022 adaptation) · DHSC PFI guidance · DHSC Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · Local Improvement Finance Trust (LIFT) framework (DH 2001)",
    "key_stats": [
        {"label": "PFI / LIFT charges 2024-25", "value": "£0.158M"},
        {"label": "Share of trust total opex", "value": "<0.05% of c. £550M"},
        {"label": "Scheme type", "value": "Residual NHS LIFT and small ancillary IFRIC 12 service-concession arrangements (no major main-site PFI)"},
        {"label": "Site footprint", "value": "Royal Hampshire County (Winchester) + Basingstoke and North Hampshire + Andover War Memorial + community/satellite sites"},
        {"label": "Tertiary specialty anchor", "value": "Basingstoke peritoneal malignancy unit (national centre) + general acute services across two main DGHs"},
        {"label": "FM / hard FM", "value": "Mostly in-house and direct-contract — minimal PFI FM exposure compared to peer trusts"},
        {"label": "Delivery body", "value": "Trust Estates & Facilities + LIFTCo SPV + DHSC PFI Centre of Best Practice"},
        {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Hampshire and Isle of Wight ICB"},
        {"label": "Funding trajectory", "value": "Slow decay as LIFT contracts expire; no major scheme inflation exposure"},
        {"label": "Evaluation evidence", "value": "HHFT ARA 2023-24 Note (PFI/IFRIC 12 disclosures); NAO PFI/PF2 reports; HMT PFI data reports; Model Hospital"},
        {"label": "Predecessor / successor", "value": "Predecessor: pre-IFRS 16 operating-lease/service-concession split · Successor: New Hospital Programme — Hampshire Together (Winchester / Basingstoke reconfiguration) potentially reshaping estate post-Reset"}
    ],
    "notes": "HHFT's PFI / LIFT line is unusually small for a multi-site acute trust because neither of the two main acute hospitals (Royal Hampshire County, Basingstoke) is on a major PFI deal — the line is residual LIFT and small IFRIC 12 ancillary arrangements. The trust's Hampshire Together programme is the successor strategic question: it sits within the New Hospital Programme cohort with proposals for major reconfiguration of Winchester and Basingstoke acute services, deferred under the January 2025 NHP Reset. Recent context includes industrial-action backfill cost pressure on staff costs (separate sub-line) and growth in Basingstoke's national peritoneal malignancy referrals.",
    "sources": [
        {"publisher": "Hampshire Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.hampshirehospitals.nhs.uk/about-us/publications/"},
        {"publisher": "Care Quality Commission", "title": "HHFT provider profile (RN5)", "url": "https://www.cqc.org.uk/provider/RN5"},
        {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
        {"publisher": "HM Treasury", "title": "PFI and PF2 current projects (March 2024)", "url": "https://www.gov.uk/government/publications/private-finance-initiative-and-private-finance-2-projects-2024-summary-data"},
        {"publisher": "NHS England", "title": "New Hospital Programme: Hampshire Together", "url": "https://www.england.nhs.uk/new-hospital-programme/"}
    ],
    "related": [
        "Hampshire Hospitals NHS Foundation Trust",
        "Premises & Infrastructure",
        "New Hospital Programme",
        "Department of Health and Social Care"
    ]
}

NEW["Termination & post-employment — West Suffolk NHS Foundation Trust"] = {
    "aliases": [{"name": "Termination & post-employment", "parent": "West Suffolk NHS Foundation Trust"}],
    "description": "West Suffolk NHSFT's £0.157M termination & post-employment line captures IAS 19 staff-cost charges for redundancy/exit settlements, MARS/VR exits, MHO retirements and post-employment benefit accruals — a Staff Costs sub-line scoped tightly under the Public Sector Exit Payments framework. The trust runs West Suffolk Hospital (Bury St Edmunds) — a critical-RAAC-list hospital in the New Hospital Programme cohort with major workforce implications for the rebuild.",
    "beneficiaries": "Acute inpatients across West Suffolk Hospital (~430 beds — A&E, maternity, paediatrics, general medicine, general surgery, T&O) plus integrated community services across West Suffolk; serving c. 280,000 catchment; c. 4,800 WTE; c. 60,000 ED attendances/yr.",
    "legal_basis": "IAS 19 Employee Benefits · NHS Pension Scheme Regulations 2015 (and 1995/2008 sections) · Public Sector Exit Payments Regulations 2020 (revoked 2021 — guidance still applies) · NHS Act 2006 · Health and Care Act 2022 · DHSC Group Accounting Manual 2024-25",
    "key_stats": [
        {"label": "Termination & post-employment 2024-25", "value": "£0.157M"},
        {"label": "Composition", "value": "Redundancy/exit settlements + MARS/VR (mutually-agreed resignation) costs + MHO/special-class retirement enhancements + post-employment benefit accruals"},
        {"label": "Site anchor", "value": "West Suffolk Hospital (Bury St Edmunds) — RAAC-affected, NHP cohort"},
        {"label": "Workforce", "value": "c. 4,800 WTE across acute + community"},
        {"label": "RAAC / NHP context", "value": "WSH on Sep 2023 HSSIB RAAC-critical list; NHP rebuild cohort; major medium-term workforce reshape implied"},
        {"label": "Exit Payments cap context", "value": "Post-2021 revocation of £95k cap, NHS retains pre-cap settlement-approval rules; MARS schemes locally agreed with NHSE Provider Finance"},
        {"label": "Funding trajectory", "value": "Modest base; potential medium-term uplift if NHP rebuild triggers role consolidation; watch for industrial-action settlement tail"},
        {"label": "Delivery body", "value": "WSFT HR + Finance + NHS Business Services Authority (NHSBSA) Pensions + NHS Resolution"},
        {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + Suffolk and North East Essex ICB + HM Treasury (exit payment guidance)"},
        {"label": "Beneficiary count", "value": "Indirect — typical year c. 10-30 individual exits across c. 4,800 WTE workforce"},
        {"label": "Evaluation evidence", "value": "WSFT ARA Note 8 (staff costs); NHSE / DHSC exit payment governance; Cassel inquiry/Trust Inquiry follow-up evaluation"},
        {"label": "Predecessor / successor", "value": "Predecessor: pre-2020 exit-payment framework · Successor: NHP rebuild workforce reshape and Suffolk-Essex group-model integration questions"}
    ],
    "notes": "WSFT's Termination & post-employment line at £0.157M reflects modest exit activity in the trust's c. £400M cost base. The forward driver is the NHP rebuild for West Suffolk Hospital — RAAC-critical and confirmed in the NHP cohort but with delivery deferred under the January 2025 NHP Reset. A rebuild typically generates medium-term workforce consolidation costs (theatre/ward reconfiguration, role rationalisation). Recent context also includes the legacy of the 2018-2020 letter-leak governance scandal and Trust Inquiry, which prompted senior-management changes and oversight tightening. Industrial-action settlements (junior doctor/consultant) generate a tail of associated costs.",
    "sources": [
        {"publisher": "West Suffolk NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.wsh.nhs.uk/About-us/Publications/Annual-reports.aspx"},
        {"publisher": "Care Quality Commission", "title": "WSFT provider profile (RGR)", "url": "https://www.cqc.org.uk/provider/RGR"},
        {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (IAS 19)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
        {"publisher": "NHS Business Services Authority", "title": "NHS Pension Scheme regulations and guidance", "url": "https://www.nhsbsa.nhs.uk/nhs-pensions"},
        {"publisher": "NHS England", "title": "New Hospital Programme: West Suffolk", "url": "https://www.england.nhs.uk/new-hospital-programme/"}
    ],
    "related": [
        "West Suffolk NHS Foundation Trust",
        "Staff Costs",
        "NHS Pension Scheme",
        "New Hospital Programme"
    ]
}

NEW["Transport (business + patient) — Southport And Ormskirk Hospital NHS Trust"] = {
    "aliases": [{"name": "Transport (business + patient)", "parent": "Southport And Ormskirk Hospital NHS Trust"}],
    "description": "Southport and Ormskirk Hospital NHS Trust's £0.156M Transport line covers AfC Section 17 staff business mileage (AMAP rates), pool fleet operating costs, NHSE-eligibility patient transport service charges, courier/sample logistics across Southport District General Hospital, Ormskirk District General Hospital and Renal/Dialysis services. The trust completed dissolution and transfer of services into Mersey and West Lancashire Teaching Hospitals (MWL) and Liverpool University Hospitals (LUH) by July 2024 — this line is the run-out tail.",
    "beneficiaries": "Acute inpatients across Southport DGH (~330 beds — A&E, general medicine, surgery), Ormskirk DGH (children's and women's services, urgent care, elective day-case) and renal services; serving c. 258,000 across Sefton/West Lancashire; c. 3,200 WTE pre-dissolution; c. 65,000 ED attendances/yr (Southport).",
    "legal_basis": "NHS Act 2006 · NHSE Patient Transport Services Eligibility Criteria 2022 · Agenda for Change Section 17 + AMAP rates (HMRC) · IFRS 16 Leases (pool fleet RoU) · DHSC Group Accounting Manual 2024-25 · Health and Care Act 2022 (trust dissolution/transfer powers)",
    "key_stats": [
        {"label": "Transport (business + patient) 2024-25", "value": "£0.156M (run-out year)"},
        {"label": "Composition", "value": "Staff business mileage (AMAP) + pool fleet operating + NHSE-eligibility PTS + courier/sample logistics"},
        {"label": "Trust status", "value": "Dissolved July 2024 — services transferred to Mersey and West Lancashire (MWL) and Liverpool University Hospitals (LUH)"},
        {"label": "Pre-dissolution sites", "value": "Southport DGH (A&E + medical/surgical) + Ormskirk DGH (children's, women's, urgent care, day surgery) + community satellites"},
        {"label": "PTS provider", "value": "North West Ambulance Service (NWAS) PTS contract + commissioned third-party providers"},
        {"label": "Catchment", "value": "c. 258,000 across Sefton and West Lancashire"},
        {"label": "Workforce", "value": "c. 3,200 WTE pre-dissolution"},
        {"label": "Delivery body", "value": "Trust Estates & Facilities + NWAS PTS + private courier contracts + NHS Supply Chain"},
        {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + Cheshire and Merseyside ICB + Lancashire and South Cumbria ICB"},
        {"label": "Funding trajectory", "value": "Sharply declining as services transfer to MWL and LUH; legacy run-out only"},
        {"label": "Evaluation evidence", "value": "S&O ARA 2023-24 final accounts; CQC pre-dissolution inspection; NHSE dissolution case; Future Pathways acute services review"},
        {"label": "Predecessor / successor", "value": "Predecessor: standalone S&O Trust transport spend · Successor: subsumed into MWL Teaching Hospitals NHSFT and Liverpool University Hospitals NHSFT post-July 2024 transfer"}
    ],
    "notes": "Southport and Ormskirk's £0.156M transport line is the run-out tail of a dissolved organisation — the trust formally dissolved on 1 July 2024 with services transferring to Mersey and West Lancashire Teaching Hospitals NHSFT (Southport DGH adult acute, A&E) and Liverpool University Hospitals NHSFT (Ormskirk children's/women's/urgent care). The Future Pathways acute-services review (NHSE 2020-22) drove the dissolution rationale after years of financial deficit and CQC concerns. Patient transport demand was material because of the dispersed Sefton/West Lancashire geography and the Renal Unit at Southport. Successor trusts now absorb the spend within their own consolidated lines.",
    "sources": [
        {"publisher": "Southport and Ormskirk Hospital NHS Trust", "title": "Annual Report and Accounts 2023-24 (final)", "url": "https://www.southportandormskirk.nhs.uk/about/publications/"},
        {"publisher": "NHS England", "title": "Future Pathways and Southport/Ormskirk dissolution announcement", "url": "https://www.england.nhs.uk/north-west/"},
        {"publisher": "Care Quality Commission", "title": "S&O provider profile (RVY)", "url": "https://www.cqc.org.uk/provider/RVY"},
        {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
        {"publisher": "NHSE", "title": "NHS Patient Transport Services Eligibility Criteria 2022", "url": "https://www.england.nhs.uk/publication/non-emergency-patient-transport-services-eligibility-criteria/"}
    ],
    "related": [
        "Southport And Ormskirk Hospital NHS Trust",
        "Premises & Infrastructure",
        "Mersey and West Lancashire Teaching Hospitals NHS Foundation Trust",
        "Liverpool University Hospitals NHS Foundation Trust"
    ]
}

NEW["Lease expenditure — Great Western Hospitals NHS Foundation Trust"] = {
    "aliases": [{"name": "Lease expenditure", "parent": "Great Western Hospitals NHS Foundation Trust"}],
    "description": "Operating lease expenditure (post-IFRS 16) at Great Western Hospitals NHSFT — covering short-life and low-value leased equipment, clinic and office space held outside Right-of-Use balances under DHSC GAM treatment. The trust runs the PFI-built Great Western Hospital (Swindon) plus integrated community services across Wiltshire (post-2016 community-services TUPE), generating a long tail of small leased items across community hospital sites and dispersed teams.",
    "beneficiaries": "Acute inpatients at Great Western Hospital Swindon (~430 beds — A&E, maternity, paediatrics, general medicine, surgery, T&O) plus integrated community services (Chippenham, Trowbridge, Warminster, Savernake, Devizes); serving c. 380,000 in Swindon and c. 700,000 across Wiltshire BSW ICS; c. 5,500 WTE; c. 95,000 ED attendances/yr.",
    "legal_basis": "IFRS 16 Leases (as adapted by FReM and DHSC GAM ch.7) · DHSC Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · Landlord and Tenant Act 1954",
    "key_stats": [
        {"label": "Lease expenditure 2024-25", "value": "£0.153M"},
        {"label": "Share of trust total opex", "value": "<0.05% of c. £550M"},
        {"label": "Coverage", "value": "Short-life (<12 months) and low-value (<£5k) leases excluded from RoU under GAM treatment"},
        {"label": "Site footprint", "value": "Great Western Hospital (Swindon, PFI) + Wiltshire community hospitals (Chippenham, Trowbridge, Warminster, Savernake, Devizes)"},
        {"label": "Specific driver", "value": "Modular equipment hire + minor vehicle fleet across dispersed Wiltshire community estate + temp office space leases"},
        {"label": "Hybrid acute/community", "value": "Post-2016 Wiltshire community-services TUPE brought in dispersed estate not held on PFI"},
        {"label": "Delivery body", "value": "GWH Estates & Facilities + Procurement + NHS Supply Chain framework leasing"},
        {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Bath and North East Somerset, Swindon and Wiltshire (BSW) ICB"},
        {"label": "Funding trajectory", "value": "Stable to slight uplift on lease re-pricing; CNZ fleet electrification gradually shifts vehicle mix"},
        {"label": "Evaluation evidence", "value": "GWH ARA 2023-24 Note (lease disclosures); CQC inspection (RN3); NHSE Operational Plan returns; Model Hospital benchmarking"},
        {"label": "Predecessor / successor", "value": "Predecessor: pre-IFRS 16 operating-lease classification (pre-2022) · Successor: continued GAM treatment of low-value/short-life items + potential BSW community services reorganisation"}
    ],
    "notes": "GWH's £0.153M lease line is small but recurring under DHSC GAM ch.7 — covering short-life and low-value items outside the RoU balance. The trust's hybrid acute-plus-community profile generates more lease tail than a pure DGH because the 2016 Wiltshire community-services TUPE brought in dispersed sites with their own equipment-hire patterns. The main acute hospital is on a PFI scheme (separate sub-line) so PFI-property leases sit elsewhere; this line covers operational hire across community-team sites. Recent context includes BSW ICB-driven discussions about acute-community-mental-health integration which may reshape lease holdings; CNZ fleet electrification and lease re-pricing drive marginal year-on-year movement.",
    "sources": [
        {"publisher": "Great Western Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.gwh.nhs.uk/about-us/publications/"},
        {"publisher": "Care Quality Commission", "title": "GWH provider profile (RN3)", "url": "https://www.cqc.org.uk/provider/RN3"},
        {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (ch.7 Leases)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
        {"publisher": "HM Treasury", "title": "FReM IFRS 16 adaptation", "url": "https://www.gov.uk/government/publications/government-financial-reporting-manual-2024-25"},
        {"publisher": "NHS England", "title": "BSW ICB system overview", "url": "https://bsw.icb.nhs.uk/"}
    ],
    "related": [
        "Great Western Hospitals NHS Foundation Trust",
        "Premises & Infrastructure",
        "NHS England",
        "Department of Health and Social Care"
    ]
}

NEW["Lease expenditure — North Middlesex University Hospital NHS Trust"] = {
    "aliases": [{"name": "Lease expenditure", "parent": "North Middlesex University Hospital NHS Trust"}],
    "description": "Operating lease expenditure (post-IFRS 16) at North Middlesex — covering short-life and low-value leased equipment, modular clinic and office space held outside Right-of-Use balances under DHSC GAM treatment, plus minor vehicle fleet supporting the single-site Edmonton hospital. The trust merged into Royal Free London NHS Foundation Trust on 1 November 2024, so 2024-25 reflects part-year run-out activity prior to consolidation.",
    "beneficiaries": "Acute inpatients at North Middlesex Hospital (Edmonton ~370 beds — A&E one of the busiest in London, maternity, paediatrics, general medicine and surgery); serving c. 350,000 across Enfield and Haringey (deprived North London catchment); c. 3,500 WTE; c. 130,000 ED attendances/yr.",
    "legal_basis": "IFRS 16 Leases (as adapted by FReM and DHSC GAM ch.7) · DHSC Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 (transactions powers) · Landlord and Tenant Act 1954",
    "key_stats": [
        {"label": "Lease expenditure 2024-25", "value": "£0.152M (part-year pre-RFL merger)"},
        {"label": "Trust status", "value": "Merged with Royal Free London NHS FT on 1 November 2024 — final standalone reporting period"},
        {"label": "Share of trust total opex", "value": "<0.05% of c. £350M"},
        {"label": "Coverage", "value": "Short-life (<12 months) and low-value (<£5k) leases excluded from RoU under GAM treatment"},
        {"label": "Site footprint", "value": "North Middlesex Hospital (Edmonton, single site)"},
        {"label": "Specific driver", "value": "Modular clinic and office hire + minor vehicle fleet + temp diagnostic equipment leases"},
        {"label": "ED scale", "value": "c. 130,000 attendances/yr — among the busiest in London"},
        {"label": "Delivery body", "value": "NMUH Estates & Facilities + Procurement + NHS Supply Chain framework leasing"},
        {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + North Central London (NCL) ICB"},
        {"label": "Funding trajectory", "value": "Decay post-merger; absorbed into RFL group-model lease line from November 2024"},
        {"label": "Evaluation evidence", "value": "NMUH ARA 2023-24 Note (lease disclosures); CQC inspection (RAP); NHSE merger transaction case 2024; Model Hospital benchmarking"},
        {"label": "Predecessor / successor", "value": "Predecessor: pre-IFRS 16 operating-lease classification (pre-2022) · Successor: subsumed into Royal Free London NHS Foundation Trust group-model lease accounting from Nov 2024"}
    ],
    "notes": "North Middlesex's £0.152M lease line is the final standalone-reporting tail before the 1 November 2024 merger with Royal Free London NHSFT created a unified North Central London acute group. NMUH serves a deprived North London catchment with one of the busiest A&Es in London (c. 130,000 attendances). The lease line covers small operational items outside the IFRS 16 RoU threshold — modular clinics, equipment hire and minor fleet. The merger rationale, set out in the NHSE 2024 transaction case, was financial sustainability and clinical-resilience improvement; from November 2024 the spend rolls into RFL's consolidated lease line. CQC has historically rated NMUH 'Requires Improvement' with sustained pressures on emergency flow.",
    "sources": [
        {"publisher": "North Middlesex University Hospital NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.northmid.nhs.uk/"},
        {"publisher": "Royal Free London NHS Foundation Trust", "title": "NMUH merger transaction case (NHSE Nov 2024)", "url": "https://www.royalfree.nhs.uk/about-us/north-middlesex-university-hospital-merger/"},
        {"publisher": "Care Quality Commission", "title": "NMUH provider profile (RAP)", "url": "https://www.cqc.org.uk/provider/RAP"},
        {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (ch.7 Leases)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
        {"publisher": "NHS England", "title": "North Central London ICB system overview", "url": "https://www.northcentrallondon.icb.nhs.uk/"}
    ],
    "related": [
        "North Middlesex University Hospital NHS Trust",
        "Royal Free London NHS Foundation Trust",
        "Premises & Infrastructure",
        "NHS England"
    ]
}

NEW["Inventories written down — Countess of Chester Hospital NHS Foundation Trust"] = {
    "aliases": [{"name": "Inventories written down", "parent": "Countess of Chester Hospital NHS Foundation Trust"}],
    "description": "Countess of Chester Hospital NHSFT's £0.152M inventories-written-down line captures the IAS 2 charge for stock written off below cost — chiefly time-expired pharmaceuticals (general acute drugs, anti-infectives, anaesthetic agents), expired theatre consumables and surgical kit, expired wound-care and catheter stock, and obsolete bespoke implants. The trust runs Countess of Chester Hospital (Chester) and Ellesmere Port Hospital across Cheshire and Wirral ICB.",
    "beneficiaries": "Acute inpatients across Countess of Chester Hospital (~600 beds — A&E, maternity, paediatrics, general medicine, general surgery, T&O) and Ellesmere Port Hospital (community/rehab); serving c. 450,000 across Cheshire West and Chester plus Welsh cross-border catchment; c. 4,300 WTE; c. 75,000 ED attendances/yr.",
    "legal_basis": "IAS 2 Inventories · DHSC Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · Drug Tariff (NHS Act 2006 Sch 1) · MHRA medicines regulation",
    "key_stats": [
        {"label": "Inventories written down 2024-25", "value": "£0.152M"},
        {"label": "Site anchor", "value": "Countess of Chester Hospital (Chester) + Ellesmere Port Hospital"},
        {"label": "Catchment", "value": "c. 450,000 across Cheshire West and Chester plus Welsh cross-border draw"},
        {"label": "Workforce", "value": "c. 4,300 WTE across acute + rehab/community"},
        {"label": "Stock profile", "value": "Generic + branded drugs (acute formulary), theatre consumables (T&O, general surgery, gynae), wound-care, catheter and IV kits, bespoke T&O implants"},
        {"label": "Write-down driver", "value": "Time-expiry of low-turnover drugs + theatre kit obsolescence + bespoke implant size mix obsolescence + ongoing pharmacy harmonisation"},
        {"label": "Procurement route", "value": "NHS Supply Chain (national framework) + ICB-led joint procurement + direct-to-supplier (specialist implants)"},
        {"label": "Funding trajectory", "value": "Stable to slight uplift on drug-price inflation; Frontline Digitisation EPR rollout improves stock visibility medium-term"},
        {"label": "Delivery body", "value": "CoCH Pharmacy + Procurement + Theatres stock control + NHS Supply Chain"},
        {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Cheshire and Merseyside ICB + NHS Supply Chain"},
        {"label": "Evaluation evidence", "value": "CoCH ARA Note (inventories); CQC inspection (RJR); NHSE Operational Plan returns; Model Hospital procurement benchmarks"},
        {"label": "Predecessor / successor", "value": "Predecessor: pre-Frontline Digitisation manual stock control · Successor: EPR-driven stock-management improvements + ICB-wide pooled procurement"}
    ],
    "notes": "The Countess of Chester's £0.152M write-down reflects routine IAS 2 NRV adjustment for an acute trust of its scale (c. £350M turnover). Drivers include drug-price inflation on generic anti-infectives and analgesics, T&O implant size-mix obsolescence and routine theatre kit expiry. Recent context is dominated by the legacy of the Lucy Letby case (CoCH neonatal nurse convicted in 2023; Thirlwall Inquiry started Sep 2024) which has shaped governance, neonatal-service pathway reorganisation and trust leadership change — these have indirect operational implications for procurement and stock-control rigour. The Frontline Digitisation EPR rollout is improving stock visibility.",
    "sources": [
        {"publisher": "Countess of Chester Hospital NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.coch.nhs.uk/about-us/publications/"},
        {"publisher": "Care Quality Commission", "title": "CoCH provider profile (RJR)", "url": "https://www.cqc.org.uk/provider/RJR"},
        {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (IAS 2 inventories)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
        {"publisher": "NHS Supply Chain", "title": "National framework annual report", "url": "https://www.supplychain.nhs.uk/"},
        {"publisher": "Thirlwall Inquiry", "title": "Public inquiry into events at the Countess of Chester Hospital", "url": "https://thirlwall.public-inquiry.uk/"}
    ],
    "related": [
        "Countess of Chester Hospital NHS Foundation Trust",
        "Clinical Supplies & Drugs",
        "NHS Supply Chain",
        "NHS England"
    ]
}

NEW["PFI / LIFT charges — East And North Hertfordshire NHS Trust"] = {
    "aliases": [{"name": "PFI / LIFT charges", "parent": "East And North Hertfordshire NHS Trust"}],
    "description": "East and North Hertfordshire NHS Trust's £0.151M residual PFI / LIFT charges line covers small ancillary service-concession arrangements (residual NHS LIFT primary-care/community premises, small modular schemes) outside the trust's main estate. The trust runs the Lister Hospital (Stevenage), Hertford County Hospital and Mount Vernon Cancer Centre — Lister is the main acute and is not on a major-PFI deal, so this line is a residual tail of historic LIFT/IFRIC 12 arrangements.",
    "beneficiaries": "Acute inpatients at the Lister Hospital (Stevenage ~580 beds — A&E, maternity, paediatrics, general medicine, surgery), specialist cancer outpatients/inpatients at Mount Vernon Cancer Centre, plus outpatient services at Hertford County and New QEII; serving c. 600,000 in East and North Herts; c. 5,400 WTE; c. 105,000 ED attendances/yr.",
    "legal_basis": "IFRIC 12 Service Concession Arrangements · IFRS 16 Leases (post-2022 adaptation) · DHSC PFI guidance · DHSC Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · Local Improvement Finance Trust (LIFT) framework (DH 2001)",
    "key_stats": [
        {"label": "PFI / LIFT charges 2024-25", "value": "£0.151M"},
        {"label": "Share of trust total opex", "value": "<0.05% of c. £600M"},
        {"label": "Scheme type", "value": "Residual NHS LIFT and small ancillary IFRIC 12 service-concession arrangements"},
        {"label": "Site footprint", "value": "Lister Hospital (Stevenage) + Mount Vernon Cancer Centre + Hertford County + New QEII Welwyn Garden City"},
        {"label": "Tertiary anchor", "value": "Mount Vernon Cancer Centre (cancer specialty draws regional tertiary referrals from Beds, Bucks, Herts, NW London)"},
        {"label": "FM exposure", "value": "Mostly in-house and direct-contract — minimal PFI FM exposure compared to peer DGHs"},
        {"label": "Delivery body", "value": "Trust Estates & Facilities + LIFTCo SPV + DHSC PFI Centre of Best Practice"},
        {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Hertfordshire and West Essex ICB"},
        {"label": "Funding trajectory", "value": "Slow decay as LIFT contracts expire; no major scheme inflation exposure; potential reshape if NHP New Hospital Programme adopts Lister redevelopment"},
        {"label": "Evaluation evidence", "value": "ENHT ARA 2023-24 Note (PFI/IFRIC 12 disclosures); NAO PFI/PF2 reports; HMT PFI data reports; Model Hospital"},
        {"label": "Mount Vernon context", "value": "Cancer service review (2020-2024) recommended transfer of cancer services elsewhere (potentially UCLH/RFL) — long-term reshape of trust footprint"},
        {"label": "Predecessor / successor", "value": "Predecessor: pre-IFRS 16 operating-lease/service-concession split · Successor: continued LIFT tail; potential Mount Vernon transfer; Lister site investment"}
    ],
    "notes": "ENHT's PFI / LIFT line is small because the main Lister site is not a major-PFI build — the line is residual LIFT and small IFRIC 12 ancillary arrangements. The trust's strategic question is the Mount Vernon Cancer Centre service review (2020-2024) which proposed transfer of cancer services to UCLH/RFL with associated estate consequences, and the Lister Hospital's potential inclusion in future estate investment programmes. Hertfordshire and West Essex ICB integration discussions and ongoing emergency-flow pressure (Lister A&E remains under sustained 4-hour standard pressure) shape the broader operational context.",
    "sources": [
        {"publisher": "East and North Hertfordshire NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.enherts-tr.nhs.uk/about-us/our-publications/"},
        {"publisher": "Care Quality Commission", "title": "ENHT provider profile (RWH)", "url": "https://www.cqc.org.uk/provider/RWH"},
        {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
        {"publisher": "HM Treasury", "title": "PFI and PF2 current projects (March 2024)", "url": "https://www.gov.uk/government/publications/private-finance-initiative-and-private-finance-2-projects-2024-summary-data"},
        {"publisher": "NHS England", "title": "Mount Vernon Cancer Centre Review final report", "url": "https://www.england.nhs.uk/london/our-work/cancer/"}
    ],
    "related": [
        "East And North Hertfordshire NHS Trust",
        "Premises & Infrastructure",
        "Mount Vernon Cancer Centre",
        "Department of Health and Social Care"
    ]
}

NEW["Termination & post-employment — Gateshead Health NHS Foundation Trust"] = {
    "aliases": [{"name": "Termination & post-employment", "parent": "Gateshead Health NHS Foundation Trust"}],
    "description": "Gateshead Health NHSFT's £0.143M termination & post-employment line captures IAS 19 staff-cost charges for redundancy/exit settlements, MARS/VR exits, MHO retirements and post-employment benefit accruals — a Staff Costs sub-line scoped under the Public Sector Exit Payments framework. The trust runs Queen Elizabeth Hospital Gateshead plus Bensham Hospital and several integrated community sites across the North East and North Cumbria ICB.",
    "beneficiaries": "Acute inpatients at Queen Elizabeth Hospital Gateshead (~530 beds — A&E, maternity, paediatrics, general medicine, surgery, T&O, ENT, ophthalmology) plus rehab/community services at Bensham; serving c. 200,000 in Gateshead Borough; c. 4,200 WTE; c. 80,000 ED attendances/yr.",
    "legal_basis": "IAS 19 Employee Benefits · NHS Pension Scheme Regulations 2015 (and 1995/2008 sections) · Public Sector Exit Payments Regulations 2020 (revoked 2021 — guidance still applies) · NHS Act 2006 · Health and Care Act 2022 · DHSC Group Accounting Manual 2024-25",
    "key_stats": [
        {"label": "Termination & post-employment 2024-25", "value": "£0.143M"},
        {"label": "Composition", "value": "Redundancy/exit settlements + MARS/VR (mutually-agreed resignation) costs + MHO/special-class retirement enhancements + post-employment benefit accruals"},
        {"label": "Site anchor", "value": "Queen Elizabeth Hospital Gateshead + Bensham Hospital + community sites"},
        {"label": "Workforce", "value": "c. 4,200 WTE across acute + community + rehab"},
        {"label": "Scale anchor", "value": "c. £350M turnover (2023-24)"},
        {"label": "Exit Payments cap context", "value": "Post-2021 revocation of £95k cap, NHS retains pre-cap settlement-approval rules; MARS schemes locally agreed with NHSE Provider Finance"},
        {"label": "Funding trajectory", "value": "Modest base; potential medium-term uplift on industrial-action settlement tail and any group-model integration discussions in NE/NC ICB"},
        {"label": "Delivery body", "value": "Gateshead Health HR + Finance + NHS Business Services Authority (NHSBSA) Pensions + NHS Resolution"},
        {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + North East and North Cumbria ICB + HM Treasury (exit payment guidance)"},
        {"label": "Beneficiary count", "value": "Indirect — typical year c. 10-25 individual exits across c. 4,200 WTE workforce"},
        {"label": "Evaluation evidence", "value": "Gateshead Health ARA Note 8 (staff costs); NHSE / DHSC exit payment governance"},
        {"label": "Predecessor / successor", "value": "Predecessor: pre-2020 exit-payment framework · Successor: NE/NC ICB acute provider collaborative structures and any future group-model arrangements"}
    ],
    "notes": "Gateshead Health's £0.143M Termination & post-employment line reflects modest exit activity in a medium-sized DGH with c. £350M cost base. The trust's longstanding partnership with Newcastle Hospitals (specialist tertiary referrals) and participation in the North East and North Cumbria provider collaborative shape the workforce environment. Recent context includes industrial-action settlement tails (junior doctor, consultant) and the trust's continued operation of Queen Elizabeth Hospital — there is no major NHP rebuild on this site, so termination volume is driven by routine workforce management rather than a structural reshape event.",
    "sources": [
        {"publisher": "Gateshead Health NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.gateshead.gov.uk/article/15125/Gateshead-Health-NHS-Foundation-Trust-Annual-reports"},
        {"publisher": "Care Quality Commission", "title": "Gateshead Health provider profile (RR7)", "url": "https://www.cqc.org.uk/provider/RR7"},
        {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (IAS 19)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
        {"publisher": "NHS Business Services Authority", "title": "NHS Pension Scheme regulations and guidance", "url": "https://www.nhsbsa.nhs.uk/nhs-pensions"},
        {"publisher": "NHS England", "title": "North East and North Cumbria ICB system overview", "url": "https://northeastnorthcumbria.nhs.uk/"}
    ],
    "related": [
        "Gateshead Health NHS Foundation Trust",
        "Staff Costs",
        "NHS Pension Scheme",
        "North East and North Cumbria ICB"
    ]
}

NEW["Other & adjustments — Wirral University Teaching Hospital NHS Foundation Trust"] = {
    "aliases": [{"name": "Other & adjustments", "parent": "Wirral University Teaching Hospital NHS Foundation Trust"}],
    "description": "Wirral University Teaching Hospital NHSFT's £0.142M Other & adjustments line is a Staff Costs disclosure cleanup covering prior-year payroll corrections, AME / DEL reclassifications, ESA10-aligned reclassifications, accruals true-ups and immaterial residual employer-cost items below DHSC GAM materiality thresholds for substantive sub-category disclosure. The trust runs Arrowe Park Hospital (Upton) and Clatterbridge Hospital (Bebington) across the Cheshire and Merseyside ICS.",
    "beneficiaries": "Indirect — adjustments affect net-cost allocation across c. 6,200 substantive WTE serving c. 320,000 across the Wirral Peninsula plus cross-border Welsh draw; supports c. 110,000 ED attendances/yr at Arrowe Park.",
    "legal_basis": "DHSC Group Accounting Manual 2024-25 disclosure rules · ESA10 sector-classification framework · IAS 1 Presentation of Financial Statements · IAS 19 Employee Benefits · NHS Act 2006 · Health and Care Act 2022",
    "key_stats": [
        {"label": "Other & adjustments 2024-25", "value": "£0.142M"},
        {"label": "Composition", "value": "Prior-year payroll corrections + AME / DEL reclassifications + accruals true-ups + immaterial residual employer-cost items"},
        {"label": "ESA10 framework", "value": "European System of Accounts 2010 — sector-classification rules cascading through DHSC GAM into trust disclosure"},
        {"label": "Trust scale anchor", "value": "c. 6,200 WTE across Arrowe Park and Clatterbridge sites"},
        {"label": "Site footprint", "value": "Arrowe Park Hospital (Upton, main acute, A&E ~700 beds) + Clatterbridge Hospital (Bebington, elective + rehab) + community sites"},
        {"label": "DHSC GAM disclosure rule", "value": "Other & adjustments is a permitted catchall for items below materiality thresholds for substantive disclosure under DHSC GAM 2024-25"},
        {"label": "Funding trajectory", "value": "Variable year-on-year per cleanup volume; 2024-25 £0.142M reflects routine cleanup activity post-financial-recovery"},
        {"label": "Delivery body", "value": "WUTH HR + Finance teams + NHSE Provider Finance + DHSC consolidation"},
        {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + Cheshire and Merseyside ICB"},
        {"label": "Beneficiary count", "value": "Indirect — affects net-cost allocation rather than direct-service delivery"},
        {"label": "Evaluation evidence", "value": "WUTH ARA Note 8 staff-costs disclosure; DHSC GAM compliance; NHSE Provider Finance returns; CQC inspection (RBL)"},
        {"label": "Predecessor / successor", "value": "Predecessor: pre-DHSC GAM 2024-25 cleanup categorisation · Successor: continued residual disclosure under standard GAM rules; potential C&M ICB acute-collaborative reorganisation cleanup"}
    ],
    "notes": "WUTH's Other & adjustments staff-costs line is recurring cleanup covering prior-year payroll corrections, ESA10 reclassifications and immaterial residuals below substantive sub-category materiality. The trust has been through sustained financial recovery and oversight following the 2018-2022 period of CQC concerns and financial deficit, and the 2024-25 disclosure reflects routine post-recovery cleanup. Cheshire and Merseyside ICB acute-collaborative discussions and ongoing Frontline Digitisation EPR rollout shape forward cleanup volume; the line is not a substantive policy lever but provides disclosure transparency under DHSC GAM 2024-25.",
    "sources": [
        {"publisher": "Wirral University Teaching Hospital NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.wuth.nhs.uk/about-us/publications/"},
        {"publisher": "Care Quality Commission", "title": "WUTH provider profile (RBL)", "url": "https://www.cqc.org.uk/provider/RBL"},
        {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
        {"publisher": "NHS England", "title": "Cheshire and Merseyside ICB system overview", "url": "https://www.cheshireandmerseyside.nhs.uk/"},
        {"publisher": "HM Treasury", "title": "FReM 2024-25 ESA10 disclosure framework", "url": "https://www.gov.uk/government/publications/government-financial-reporting-manual-2024-25"}
    ],
    "related": [
        "Wirral University Teaching Hospital NHS Foundation Trust",
        "Staff Costs",
        "Department of Health and Social Care",
        "NHS England"
    ]
}

NEW["Lease expenditure — Royal United Hospitals Bath NHS Foundation Trust"] = {
    "aliases": [{"name": "Lease expenditure", "parent": "Royal United Hospitals Bath NHS Foundation Trust"}],
    "description": "Operating lease expenditure (post-IFRS 16) at RUH Bath — covering short-life and low-value leased equipment, modular clinic and office space held outside Right-of-Use balances under DHSC GAM treatment, plus minor vehicle fleet supporting the Combe Park (Bath) site and small satellite clinics across the BSW ICS footprint.",
    "beneficiaries": "Acute inpatients across RUH Bath (~750 beds — A&E, maternity, paediatrics, general medicine, general surgery, T&O, Royal National Hospital for Rheumatic Diseases (RNHRD) regional specialty); serving c. 500,000 across BANES, North East Somerset and Wiltshire; c. 5,300 WTE; c. 80,000 ED attendances/yr.",
    "legal_basis": "IFRS 16 Leases (as adapted by FReM and DHSC GAM ch.7) · DHSC Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · Landlord and Tenant Act 1954",
    "key_stats": [
        {"label": "Lease expenditure 2024-25", "value": "£0.140M"},
        {"label": "Share of trust total opex", "value": "<0.05% of c. £500M"},
        {"label": "Coverage", "value": "Short-life (<12 months) and low-value (<£5k) leases excluded from RoU under GAM treatment"},
        {"label": "Site footprint", "value": "Combe Park (Bath) main site + RNHRD specialty unit + Sulis Hospital (joint venture) + community satellites"},
        {"label": "Specific driver", "value": "Modular clinic and equipment hire + minor vehicle fleet + temp diagnostic equipment leases supporting Frontline Digitisation EPR rollout"},
        {"label": "Specialty anchor", "value": "Royal National Hospital for Rheumatic Diseases — regional specialty centre integrated into RUH from 2015"},
        {"label": "Delivery body", "value": "RUH Estates & Facilities + Procurement + NHS Supply Chain framework leasing"},
        {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Bath and North East Somerset, Swindon and Wiltshire (BSW) ICB"},
        {"label": "Funding trajectory", "value": "Stable to slight uplift on lease re-pricing; CNZ fleet electrification gradually shifts vehicle mix; Dyson Cancer Centre completion (2024) shaped pre-opening modular hire"},
        {"label": "Evaluation evidence", "value": "RUH ARA 2023-24 Note (lease disclosures); CQC inspection (RD1); NHSE Operational Plan returns; Model Hospital benchmarking"},
        {"label": "Predecessor / successor", "value": "Predecessor: pre-IFRS 16 operating-lease classification (pre-2022) · Successor: continued GAM treatment of low-value/short-life items + post-Dyson-Cancer-Centre operational steady state"}
    ],
    "notes": "RUH Bath's £0.140M lease line is a small but recurring operational charge under DHSC GAM ch.7 — covering items outside the IFRS 16 RoU threshold. The trust's Combe Park site recently completed the Dyson Cancer Centre (opened 2024) which shaped a pulse of pre-opening modular and equipment-hire activity. The integration of the Royal National Hospital for Rheumatic Diseases (2015) and the joint-venture Sulis Hospital generate a long tail of small leased items. Recent context includes BSW ICB acute-collaborative discussions and ongoing CNZ fleet electrification, plus continued elective-recovery activity.",
    "sources": [
        {"publisher": "Royal United Hospitals Bath NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.ruh.nhs.uk/about/publications/"},
        {"publisher": "Care Quality Commission", "title": "RUH Bath provider profile (RD1)", "url": "https://www.cqc.org.uk/provider/RD1"},
        {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (ch.7 Leases)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
        {"publisher": "HM Treasury", "title": "FReM IFRS 16 adaptation", "url": "https://www.gov.uk/government/publications/government-financial-reporting-manual-2024-25"},
        {"publisher": "NHS England", "title": "BSW ICB system overview", "url": "https://bsw.icb.nhs.uk/"}
    ],
    "related": [
        "Royal United Hospitals Bath NHS Foundation Trust",
        "Premises & Infrastructure",
        "NHS England",
        "Department of Health and Social Care"
    ]
}

NEW["Termination & post-employment — University Hospitals Birmingham NHS Foundation Trust"] = {
    "aliases": [{"name": "Termination & post-employment", "parent": "University Hospitals Birmingham NHS Foundation Trust"}],
    "description": "University Hospitals Birmingham NHSFT's £0.138M termination & post-employment line captures IAS 19 staff-cost charges for redundancy/exit settlements, MARS/VR exits, MHO retirements and post-employment benefit accruals. UHB is one of the largest acute trusts in England — running Queen Elizabeth Hospital Birmingham, Heartlands, Good Hope and Solihull Hospitals — so a relatively small £0.138M figure suggests substantial cleanup or specific-case activity rather than mass redundancy.",
    "beneficiaries": "Acute inpatients across QEHB (~1,200 beds — major trauma centre, transplantation, military Royal Centre for Defence Medicine), Heartlands Hospital (~700 beds), Good Hope Hospital (~430 beds) and Solihull Hospital (~300 beds); serving c. 2.2M Birmingham and Solihull catchment plus tertiary draw; c. 22,000 WTE; c. 320,000 ED attendances/yr.",
    "legal_basis": "IAS 19 Employee Benefits · NHS Pension Scheme Regulations 2015 (and 1995/2008 sections) · Public Sector Exit Payments Regulations 2020 (revoked 2021 — guidance still applies) · NHS Act 2006 · Health and Care Act 2022 · DHSC Group Accounting Manual 2024-25",
    "key_stats": [
        {"label": "Termination & post-employment 2024-25", "value": "£0.138M"},
        {"label": "Composition", "value": "Redundancy/exit settlements + MARS/VR (mutually-agreed resignation) costs + MHO/special-class retirement enhancements + post-employment benefit accruals"},
        {"label": "Site footprint", "value": "Queen Elizabeth Hospital Birmingham (Edgbaston) + Heartlands + Good Hope + Solihull + community sites"},
        {"label": "Workforce", "value": "c. 22,000 WTE — one of the largest in England post-2018 HEFT acquisition"},
        {"label": "Scale anchor", "value": "c. £1.95B turnover (2023-24) — largest acute trust in the West Midlands"},
        {"label": "Reform context", "value": "Bewick / Mackey 2022-23 review of UHB culture and governance triggered substantial leadership change and HR governance overhaul"},
        {"label": "Exit Payments cap context", "value": "Post-2021 revocation of £95k cap; UHB exits subject to NHSE Provider Finance approval given trust scale"},
        {"label": "Funding trajectory", "value": "Modest base; potential medium-term volatility on continued post-Bewick governance change and any future group/system reorganisation"},
        {"label": "Delivery body", "value": "UHB HR + Finance + NHS Business Services Authority (NHSBSA) Pensions + NHS Resolution"},
        {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + Birmingham and Solihull ICB + HM Treasury (exit payment guidance)"},
        {"label": "Beneficiary count", "value": "Indirect — a small number of high-profile senior exits in any given year against c. 22,000 WTE"},
        {"label": "Evaluation evidence", "value": "UHB ARA Note 8 (staff costs); Bewick / Mackey reviews 2022-23; PHSO / GMC follow-up; CQC inspection (RRK)"},
        {"label": "Predecessor / successor", "value": "Predecessor: pre-2018 separate UHB (QEHB) and HEFT trusts · Successor: post-Bewick / Mackey governance reset and Birmingham and Solihull ICB acute collaborative"}
    ],
    "notes": "UHB's £0.138M Termination & post-employment line is a relatively small figure for a c. £1.95B turnover trust and reflects targeted exit activity rather than mass redundancy. The 2022-23 Bewick (clinical) and Mackey (governance) reviews — commissioned after high-profile staff and patient-safety concerns — triggered a multi-year governance and leadership reset including senior departures, with associated termination accounting. UHB is the largest acute trust in the West Midlands following the 2018 Heart of England (HEFT) acquisition, with a complex 4-site footprint and the Royal Centre for Defence Medicine military relationship. Industrial-action settlement tails and ongoing Frontline Digitisation EPR change-management add a small workforce-reshape component.",
    "sources": [
        {"publisher": "University Hospitals Birmingham NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.uhb.nhs.uk/annual-reports.htm"},
        {"publisher": "NHS England", "title": "Independently-led review of UHB (Bewick / Mackey reviews)", "url": "https://www.england.nhs.uk/midlands/our-work/uhb/"},
        {"publisher": "Care Quality Commission", "title": "UHB provider profile (RRK)", "url": "https://www.cqc.org.uk/provider/RRK"},
        {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (IAS 19)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
        {"publisher": "NHS Business Services Authority", "title": "NHS Pension Scheme regulations and guidance", "url": "https://www.nhsbsa.nhs.uk/nhs-pensions"}
    ],
    "related": [
        "University Hospitals Birmingham NHS Foundation Trust",
        "Staff Costs",
        "NHS Pension Scheme",
        "NHS England"
    ]
}

NEW["Termination & post-employment — Barnsley Hospital NHS Foundation Trust"] = {
    "aliases": [{"name": "Termination & post-employment", "parent": "Barnsley Hospital NHS Foundation Trust"}],
    "description": "Barnsley Hospital NHSFT's £0.137M termination & post-employment line captures IAS 19 staff-cost charges for redundancy/exit settlements, MARS/VR exits, MHO retirements and post-employment benefit accruals. The trust runs Barnsley Hospital — a single-site DGH serving Barnsley Borough — and operates within a long-running group/management partnership with Sheffield Teaching Hospitals (joint CEO arrangement from 2017-18, partnership agreement evolved since).",
    "beneficiaries": "Acute inpatients at Barnsley Hospital (~410 beds — A&E, maternity, paediatrics, general medicine, general surgery, T&O); serving c. 245,000 in Barnsley Borough; c. 3,400 WTE; c. 75,000 ED attendances/yr.",
    "legal_basis": "IAS 19 Employee Benefits · NHS Pension Scheme Regulations 2015 (and 1995/2008 sections) · Public Sector Exit Payments Regulations 2020 (revoked 2021 — guidance still applies) · NHS Act 2006 · Health and Care Act 2022 · DHSC Group Accounting Manual 2024-25",
    "key_stats": [
        {"label": "Termination & post-employment 2024-25", "value": "£0.137M"},
        {"label": "Composition", "value": "Redundancy/exit settlements + MARS/VR (mutually-agreed resignation) costs + MHO/special-class retirement enhancements + post-employment benefit accruals"},
        {"label": "Site anchor", "value": "Barnsley Hospital (single site)"},
        {"label": "Workforce", "value": "c. 3,400 WTE"},
        {"label": "Scale anchor", "value": "c. £290M turnover (2023-24)"},
        {"label": "Group context", "value": "Long-running joint CEO/management partnership with Sheffield Teaching Hospitals NHSFT — corporate-services sharing and clinical pathways"},
        {"label": "Exit Payments cap context", "value": "Post-2021 revocation of £95k cap, NHS retains pre-cap settlement-approval rules"},
        {"label": "Funding trajectory", "value": "Modest base; potential medium-term volatility on South Yorkshire ICB acute-collaborative integration with Sheffield/Doncaster/Rotherham"},
        {"label": "Delivery body", "value": "Barnsley HR + Finance + NHS Business Services Authority (NHSBSA) Pensions + NHS Resolution"},
        {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + South Yorkshire ICB + HM Treasury (exit payment guidance)"},
        {"label": "Beneficiary count", "value": "Indirect — typical year c. 10-20 individual exits across c. 3,400 WTE workforce"},
        {"label": "Evaluation evidence", "value": "Barnsley ARA Note 8 (staff costs); NHSE Provider Finance returns; CQC inspection (RFF); Joint working with STH"},
        {"label": "Predecessor / successor", "value": "Predecessor: pre-2017 standalone Barnsley · Successor: continued STH joint partnership; potential South Yorkshire ICB-wide acute collaborative deepening"}
    ],
    "notes": "Barnsley Hospital's £0.137M Termination & post-employment line reflects modest exit activity in a single-site DGH with c. £290M cost base. The trust's longstanding partnership with Sheffield Teaching Hospitals (joint CEO and corporate-services sharing) shapes the workforce environment without merging the trusts formally. Recent context includes South Yorkshire ICB acute-collaborative discussions (Barnsley, Doncaster and Bassetlaw, Rotherham, Sheffield), industrial-action settlement tails (junior doctor, consultant) and routine senior-management churn. The line is not a substantive policy lever but provides annual disclosure under IAS 19 and DHSC GAM ch.5.",
    "sources": [
        {"publisher": "Barnsley Hospital NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.barnsleyhospital.nhs.uk/about-us/publications/"},
        {"publisher": "Care Quality Commission", "title": "Barnsley provider profile (RFF)", "url": "https://www.cqc.org.uk/provider/RFF"},
        {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (IAS 19)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
        {"publisher": "NHS Business Services Authority", "title": "NHS Pension Scheme regulations and guidance", "url": "https://www.nhsbsa.nhs.uk/nhs-pensions"},
        {"publisher": "NHS England", "title": "South Yorkshire ICB system overview", "url": "https://syicb.nhs.uk/"}
    ],
    "related": [
        "Barnsley Hospital NHS Foundation Trust",
        "Staff Costs",
        "Sheffield Teaching Hospitals NHS Foundation Trust",
        "NHS Pension Scheme"
    ]
}

NEW["Lease expenditure — James Paget University Hospitals NHS Foundation Trust"] = {
    "aliases": [{"name": "Lease expenditure", "parent": "James Paget University Hospitals NHS Foundation Trust"}],
    "description": "Operating lease expenditure (post-IFRS 16) at James Paget University Hospitals — covering short-life and low-value leased equipment, modular clinic and office space held outside Right-of-Use balances under DHSC GAM treatment, plus minor vehicle fleet supporting the Gorleston-on-Sea hospital. The trust is on the Sep 2023 RAAC-critical hospital list and is in the New Hospital Programme cohort with rebuild planning underway, so lease activity reflects RAAC mitigation and decant preparation.",
    "beneficiaries": "Acute inpatients at James Paget Hospital (Gorleston ~480 beds — A&E, maternity, paediatrics, general medicine, surgery, T&O); serving c. 230,000 across Great Yarmouth and Waveney (East Suffolk and North Norfolk coastal); c. 3,300 WTE; c. 60,000 ED attendances/yr.",
    "legal_basis": "IFRS 16 Leases (as adapted by FReM and DHSC GAM ch.7) · DHSC Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · Landlord and Tenant Act 1954",
    "key_stats": [
        {"label": "Lease expenditure 2024-25", "value": "£0.137M"},
        {"label": "Share of trust total opex", "value": "<0.05% of c. £290M"},
        {"label": "Coverage", "value": "Short-life (<12 months) and low-value (<£5k) leases excluded from RoU under GAM treatment"},
        {"label": "RAAC / NHP context", "value": "JPH on Sep 2023 HSSIB RAAC-critical list — concrete-plank failure risk drives modular decant infrastructure leases"},
        {"label": "Site footprint", "value": "James Paget Hospital (Gorleston-on-Sea, single site)"},
        {"label": "Specific driver", "value": "RAAC mitigation modular building leases + minor vehicle fleet + temp diagnostic equipment leases + decant preparation"},
        {"label": "Delivery body", "value": "JPUH Estates & Facilities + Procurement + NHS Supply Chain framework leasing"},
        {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Norfolk and Waveney ICB + New Hospital Programme team"},
        {"label": "Funding trajectory", "value": "Rising — RAAC mitigation and pre-NHP rebuild decant activity drive lease growth; January 2025 NHP Reset deferral may extend trajectory"},
        {"label": "Evaluation evidence", "value": "JPUH ARA 2023-24 Note (lease disclosures); HSSIB RAAC inspection; CQC inspection (RGP); NHP gateway reviews; NAO Hospital estate reports"},
        {"label": "Predecessor / successor", "value": "Predecessor: pre-RAAC-list lease profile · Successor: NHP rebuild new-build asset replacing leased modular infrastructure (deferred under January 2025 Reset)"}
    ],
    "notes": "JPUH's £0.137M lease line reflects the trust's specific RAAC-mitigation context — Gorleston Hospital is on the Sep 2023 HSSIB RAAC-critical list with reinforced autoclaved aerated concrete plank ceilings posing structural failure risk, and the trust is in the New Hospital Programme rebuild cohort. Lease activity is shaped by modular decant building hire, temporary equipment leases and minor fleet — a higher proportion of lease activity than a non-RAAC peer. The January 2025 NHP Reset deferred the rebuild timeline, extending the period over which mitigation lease costs accumulate. Norfolk and Waveney ICB integration discussions and CNZ fleet electrification add secondary drivers.",
    "sources": [
        {"publisher": "James Paget University Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.jpaget.nhs.uk/about-us/publications/"},
        {"publisher": "Care Quality Commission", "title": "JPUH provider profile (RGP)", "url": "https://www.cqc.org.uk/provider/RGP"},
        {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (ch.7 Leases)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
        {"publisher": "NHS England", "title": "New Hospital Programme: James Paget", "url": "https://www.england.nhs.uk/new-hospital-programme/"},
        {"publisher": "Health Services Safety Investigations Body", "title": "RAAC in NHS estates investigation", "url": "https://www.hssib.org.uk/"}
    ],
    "related": [
        "James Paget University Hospitals NHS Foundation Trust",
        "Premises & Infrastructure",
        "New Hospital Programme",
        "NHS England"
    ]
}

NEW["Termination & post-employment — University Hospitals Coventry And Warwickshire NHS Trust"] = {
    "aliases": [{"name": "Termination & post-employment", "parent": "University Hospitals Coventry And Warwickshire NHS Trust"}],
    "description": "University Hospitals Coventry and Warwickshire NHS Trust's £0.136M termination & post-employment line captures IAS 19 staff-cost charges for redundancy/exit settlements, MARS/VR exits, MHO retirements and post-employment benefit accruals. UHCW runs the PFI-built University Hospital (Walsgrave, Coventry) and the Hospital of St Cross (Rugby) — a large teaching trust with deep University of Warwick / Warwick Medical School academic links.",
    "beneficiaries": "Acute inpatients across University Hospital Coventry (~1,100 beds — A&E, major trauma centre, transplantation, cardiothoracic, neurosciences, maternity) and St Cross Rugby (~110 beds — elective and rehab); serving c. 1.0M across Coventry, Rugby and Warwickshire; c. 9,500 WTE; c. 165,000 ED attendances/yr.",
    "legal_basis": "IAS 19 Employee Benefits · NHS Pension Scheme Regulations 2015 (and 1995/2008 sections) · Public Sector Exit Payments Regulations 2020 (revoked 2021 — guidance still applies) · NHS Act 2006 · Health and Care Act 2022 · DHSC Group Accounting Manual 2024-25",
    "key_stats": [
        {"label": "Termination & post-employment 2024-25", "value": "£0.136M"},
        {"label": "Composition", "value": "Redundancy/exit settlements + MARS/VR (mutually-agreed resignation) costs + MHO/special-class retirement enhancements + post-employment benefit accruals"},
        {"label": "Site anchor", "value": "University Hospital (Walsgrave, Coventry, PFI) + Hospital of St Cross (Rugby)"},
        {"label": "Workforce", "value": "c. 9,500 WTE"},
        {"label": "Scale anchor", "value": "c. £1.05B turnover (2023-24)"},
        {"label": "Tertiary anchor", "value": "Major Trauma Centre + transplantation + cardiothoracic + neurosciences + Warwick Medical School academic partnership"},
        {"label": "Exit Payments cap context", "value": "Post-2021 revocation of £95k cap; UHCW exits subject to NHSE Provider Finance approval given trust scale"},
        {"label": "Funding trajectory", "value": "Modest base; potential medium-term volatility on Coventry & Warwickshire ICB acute-collaborative integration with Wye Valley/SWFT/GEH"},
        {"label": "Delivery body", "value": "UHCW HR + Finance + NHS Business Services Authority (NHSBSA) Pensions + NHS Resolution"},
        {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + Coventry and Warwickshire ICB + HM Treasury (exit payment guidance)"},
        {"label": "Beneficiary count", "value": "Indirect — typical year c. 20-40 individual exits across c. 9,500 WTE workforce"},
        {"label": "Evaluation evidence", "value": "UHCW ARA Note 8 (staff costs); NHSE Provider Finance returns; CQC inspection (RKB); NHS Resolution maternity safety reviews"},
        {"label": "Predecessor / successor", "value": "Predecessor: pre-2006 separate UHC and Rugby NHS Trusts · Successor: continued group-model considerations within Coventry and Warwickshire ICB"}
    ],
    "notes": "UHCW's £0.136M Termination & post-employment line reflects modest exit activity in a c. £1.05B turnover teaching trust. The trust's strategic context includes ongoing scrutiny of maternity services (CQC concerns 2022-2024), the major trauma and transplantation tertiary role, and the Warwick Medical School academic partnership. Industrial-action settlement tails (junior doctor, consultant) and routine senior-management churn drive most of the line; group/system reorganisation conversations within Coventry and Warwickshire ICB (with peer trusts SWFT, GEH, Wye Valley) shape the medium-term workforce-reshape question. The University Hospital Walsgrave site is a major PFI scheme but PFI obligations sit on a separate sub-line.",
    "sources": [
        {"publisher": "University Hospitals Coventry and Warwickshire NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.uhcw.nhs.uk/about-us/publications/"},
        {"publisher": "Care Quality Commission", "title": "UHCW provider profile (RKB)", "url": "https://www.cqc.org.uk/provider/RKB"},
        {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (IAS 19)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
        {"publisher": "NHS Business Services Authority", "title": "NHS Pension Scheme regulations and guidance", "url": "https://www.nhsbsa.nhs.uk/nhs-pensions"},
        {"publisher": "NHS England", "title": "Coventry and Warwickshire ICB system overview", "url": "https://www.happyhealthylives.uk/"}
    ],
    "related": [
        "University Hospitals Coventry And Warwickshire NHS Trust",
        "Staff Costs",
        "NHS Pension Scheme",
        "NHS England"
    ]
}

NEW["Lease expenditure — Royal Cornwall Hospitals NHS Trust"] = {
    "aliases": [{"name": "Lease expenditure", "parent": "Royal Cornwall Hospitals NHS Trust"}],
    "description": "Operating lease expenditure (post-IFRS 16) at Royal Cornwall Hospitals NHS Trust — covering short-life and low-value leased equipment, modular clinic and office space held outside Right-of-Use balances under DHSC GAM treatment, plus minor vehicle fleet supporting the dispersed Cornwall geography. The trust runs the Royal Cornwall Hospital (Treliske, Truro), West Cornwall Hospital (Penzance) and St Michael's Hospital (Hayle) across the Cornwall and Isles of Scilly ICS.",
    "beneficiaries": "Acute inpatients across Royal Cornwall Hospital (Treliske ~750 beds — A&E, maternity, paediatrics, cancer, general medicine, surgery, T&O), West Cornwall (~70 beds urgent/community), and St Michael's (elective/day case); serving c. 530,000 across Cornwall and Isles of Scilly with significant rural access challenge; c. 5,400 WTE; c. 80,000 ED attendances/yr.",
    "legal_basis": "IFRS 16 Leases (as adapted by FReM and DHSC GAM ch.7) · DHSC Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · Landlord and Tenant Act 1954",
    "key_stats": [
        {"label": "Lease expenditure 2024-25", "value": "£0.133M"},
        {"label": "Share of trust total opex", "value": "<0.05% of c. £550M"},
        {"label": "Coverage", "value": "Short-life (<12 months) and low-value (<£5k) leases excluded from RoU under GAM treatment"},
        {"label": "Site footprint", "value": "Royal Cornwall Hospital (Treliske, Truro) + West Cornwall Hospital (Penzance) + St Michael's (Hayle) + community satellites + Isles of Scilly"},
        {"label": "Specific driver", "value": "Modular clinic/equipment hire + vehicle fleet (extensive for rural Cornwall geography) + temp diagnostic equipment leases"},
        {"label": "Geographic context", "value": "Most rural and peninsular acute trust footprint in England — dispersed sites and longer travel distances drive higher fleet/lease activity vs urban peers"},
        {"label": "Delivery body", "value": "RCHT Estates & Facilities + Procurement + NHS Supply Chain framework leasing"},
        {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Cornwall and Isles of Scilly ICB"},
        {"label": "Funding trajectory", "value": "Stable to slight uplift on lease re-pricing and CNZ fleet electrification; rural electrification challenges shape vehicle procurement mix"},
        {"label": "Evaluation evidence", "value": "RCHT ARA 2023-24 Note (lease disclosures); CQC inspection (REF) — historical 'Requires Improvement' rating now improved; NHSE Operational Plan returns; Model Hospital benchmarking"},
        {"label": "Predecessor / successor", "value": "Predecessor: pre-IFRS 16 operating-lease classification (pre-2022) · Successor: continued GAM treatment of low-value/short-life items + Women and Children's Hospital scheme delivery"}
    ],
    "notes": "RCHT's £0.133M lease line reflects the trust's dispersed Cornwall geography — a peninsular footprint with two main and several satellite sites generates a long tail of small leased items, particularly fleet, modular clinic hire and temporary equipment. The trust has been under sustained operational and financial scrutiny (historical CQC 'Requires Improvement') with recent improvement, and is delivering the Women and Children's Hospital scheme on the Treliske site. Rural fleet electrification challenges (charging infrastructure across remote Cornwall) shape vehicle lease mix differently from urban peers. CNZ targets and Model Hospital benchmarking add forward drivers.",
    "sources": [
        {"publisher": "Royal Cornwall Hospitals NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.royalcornwall.nhs.uk/about-us/publications/"},
        {"publisher": "Care Quality Commission", "title": "RCHT provider profile (REF)", "url": "https://www.cqc.org.uk/provider/REF"},
        {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (ch.7 Leases)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
        {"publisher": "HM Treasury", "title": "FReM IFRS 16 adaptation", "url": "https://www.gov.uk/government/publications/government-financial-reporting-manual-2024-25"},
        {"publisher": "NHS England", "title": "Cornwall and Isles of Scilly ICB system overview", "url": "https://www.cios.icb.nhs.uk/"}
    ],
    "related": [
        "Royal Cornwall Hospitals NHS Trust",
        "Premises & Infrastructure",
        "NHS England",
        "Department of Health and Social Care"
    ]
}

NEW["Inventories written down — James Paget University Hospitals NHS Foundation Trust"] = {
    "aliases": [{"name": "Inventories written down", "parent": "James Paget University Hospitals NHS Foundation Trust"}],
    "description": "James Paget University Hospitals NHSFT's £0.132M inventories-written-down line captures the IAS 2 charge for stock written off below cost — chiefly time-expired pharmaceuticals (general acute drugs, anti-infectives, anaesthetic agents), expired theatre consumables and surgical kit, expired wound-care and catheter stock, and obsolete bespoke implants at the Gorleston-on-Sea hospital. The trust is RAAC-critical (Sep 2023 HSSIB list) and in the New Hospital Programme cohort.",
    "beneficiaries": "Acute inpatients at James Paget Hospital (Gorleston ~480 beds — A&E, maternity, paediatrics, general medicine, surgery, T&O); serving c. 230,000 across Great Yarmouth and Waveney coastal catchment; c. 3,300 WTE; c. 60,000 ED attendances/yr.",
    "legal_basis": "IAS 2 Inventories · DHSC Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · Drug Tariff (NHS Act 2006 Sch 1) · MHRA medicines regulation",
    "key_stats": [
        {"label": "Inventories written down 2024-25", "value": "£0.132M"},
        {"label": "Site anchor", "value": "James Paget Hospital (Gorleston-on-Sea, single site, RAAC-critical)"},
        {"label": "Catchment", "value": "c. 230,000 across Great Yarmouth and Waveney coastal area"},
        {"label": "Workforce", "value": "c. 3,300 WTE"},
        {"label": "Stock profile", "value": "Generic + branded drugs (acute formulary), theatre consumables (T&O, general surgery, gynae), wound-care, catheter and IV kits, bespoke T&O implants"},
        {"label": "Write-down driver", "value": "Time-expiry of low-turnover drugs + theatre kit obsolescence + bespoke implant size mix obsolescence + RAAC-decant disruption affecting stock rotation"},
        {"label": "Procurement route", "value": "NHS Supply Chain (national framework) + East of England joint procurement (with Norfolk and Norwich UHG) + direct-to-supplier (specialist implants)"},
        {"label": "RAAC / NHP context", "value": "Decant and modular operations during RAAC mitigation can disrupt normal stock rotation and increase short-shelf-life write-down volume"},
        {"label": "Delivery body", "value": "JPUH Pharmacy + Procurement + Theatres stock control + NHS Supply Chain"},
        {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Norfolk and Waveney ICB + NHS Supply Chain"},
        {"label": "Funding trajectory", "value": "Stable to slight uplift on drug-price inflation and RAAC-decant disruption tail; NHP rebuild medium-term may improve stock-management infrastructure"},
        {"label": "Evaluation evidence", "value": "JPUH ARA Note (inventories); CQC inspection (RGP); NHSE Operational Plan returns; Model Hospital procurement benchmarks"},
        {"label": "Predecessor / successor", "value": "Predecessor: pre-RAAC-decant standard stock control · Successor: NHP rebuild new-build stock-management infrastructure (deferred under January 2025 Reset)"}
    ],
    "notes": "JPUH's £0.132M write-down reflects routine IAS 2 NRV adjustment plus an additional component driven by the trust's RAAC-mitigation context — Gorleston Hospital is on the Sep 2023 HSSIB RAAC-critical list and decant operations and modular ward use can disrupt normal stock rotation, increasing short-shelf-life write-down volume modestly. The trust is in the New Hospital Programme cohort with rebuild deferred under the January 2025 Reset. Drivers also include drug-price inflation on generic anti-infectives and analgesics, T&O implant size-mix obsolescence and ongoing East of England procurement collaborative discussions with Norfolk and Norwich UHG. Frontline Digitisation EPR rollout will improve forward stock visibility.",
    "sources": [
        {"publisher": "James Paget University Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.jpaget.nhs.uk/about-us/publications/"},
        {"publisher": "Care Quality Commission", "title": "JPUH provider profile (RGP)", "url": "https://www.cqc.org.uk/provider/RGP"},
        {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (IAS 2 inventories)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
        {"publisher": "NHS Supply Chain", "title": "National framework annual report", "url": "https://www.supplychain.nhs.uk/"},
        {"publisher": "NHS England", "title": "New Hospital Programme: James Paget", "url": "https://www.england.nhs.uk/new-hospital-programme/"}
    ],
    "related": [
        "James Paget University Hospitals NHS Foundation Trust",
        "Clinical Supplies & Drugs",
        "NHS Supply Chain",
        "New Hospital Programme"
    ]
}
