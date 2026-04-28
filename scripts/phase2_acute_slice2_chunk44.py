# -*- coding: utf-8 -*-
# Phase 2 Acute slice 2 — chunk 44 (17 NHS Acute Trust orphan sub-lines)
# Hand-curated trust-specific PROGRAMME-archetype enrichment entries.
# Structural contract per docs/archetype_briefs.md.

NEW = {}

NEW["Lease expenditure — University Hospitals Bristol and Weston NHS Foundation Trust"] = {
    "aliases": [{"name": "Lease expenditure", "parent": "University Hospitals Bristol and Weston NHS Foundation Trust"}],
    "description": "Operating lease expenditure (post-IFRS 16) at UHBW — covering short-life and low-value leased estate and equipment held outside Right-of-Use balances under DHSC GAM treatment, plus vehicle fleet operating leases supporting the merged Bristol Royal Infirmary, Bristol Royal Hospital for Children, St Michael's, Bristol Heart Institute, Bristol Eye Hospital, Bristol Dental Hospital and Weston General sites across the Severn region.",
    "beneficiaries": "Adult acute, paediatric quaternary (BRHC), specialist cardiothoracic, eye, dental and obstetric inpatients across Bristol, North Somerset and South Gloucestershire (~1.0M pop); c. 4M outpatient + inpatient + day-case contacts/yr; c. 14,000 WTE across 9 sites.",
    "legal_basis": "IFRS 16 Leases (as adapted by FReM and DHSC GAM ch.7) · DHSC Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · Landlord and Tenant Act 1954",
    "key_stats": [
        {"label": "Lease expenditure 2024-25", "value": "£0.26M"},
        {"label": "Share of trust total opex", "value": "<0.1% of c. £1.4B"},
        {"label": "Coverage", "value": "Short-life (<12 months) and low-value (<£5k) leases excluded from RoU under GAM treatment"},
        {"label": "Site footprint", "value": "9 sites — BRI, BRHC, St Michael's, BHI, BEH, BDH, Weston General, South Bristol Community Hospital, regional satellite clinics"},
        {"label": "Specific driver", "value": "Equipment hire (modular wards, decant during BRI redevelopment) + minor vehicle fleet + temp office space leases"},
        {"label": "YoY change", "value": "c. +5-7% (lease re-pricing, post-merger fleet rationalisation tail)"},
        {"label": "Delivery body", "value": "UHBW Estates & Facilities + Procurement + NHS Supply Chain framework leasing"},
        {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + BNSSG ICB"},
        {"label": "Funding trajectory", "value": "Stable to slight uplift; merger integration with Weston (Apr 2020) tail completed; redevelopment-related decant lifts equipment-hire share"},
        {"label": "Evaluation evidence", "value": "UHBW ARA 2023-24 Note (lease disclosures); CQC inspection; NHSE Operational Plan returns; Model Hospital benchmarking"},
        {"label": "Predecessor / successor", "value": "Predecessor: pre-IFRS 16 operating-lease classification (pre-2022) · Successor: continued GAM treatment of low-value/short-life items + Carbon Net Zero fleet electrification programme"}
    ],
    "notes": "UHBW's £0.26M lease line is a small but recurring operational charge covering items that fall outside the IFRS 16 Right-of-Use threshold under DHSC GAM ch.7 — short-life equipment hire, low-value leases and minor fleet items. The trust's complex 9-site footprint following the April 2020 merger with Weston Area Health NHS Trust generates a long tail of small leased items across estates, theatres equipment hire and fleet. UHBW is part of BNSSG ICB and a tertiary specialist anchor for paediatrics (BRHC), cardiothoracic (BHI) and ophthalmology (BEH); the line is shaped by ongoing decant activity around the Bristol Royal Infirmary redevelopment programme and Weston General's recovery plan. Carbon Net Zero fleet electrification is gradually shifting vehicle leases from ICE to BEV.",
    "sources": [
        {"publisher": "University Hospitals Bristol and Weston NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.uhbw.nhs.uk/about-us/annual-report-and-accounts"},
        {"publisher": "Care Quality Commission", "title": "UHBW provider profile (RA7)", "url": "https://www.cqc.org.uk/provider/RA7"},
        {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (ch.7 Leases)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
        {"publisher": "HM Treasury", "title": "FReM IFRS 16 adaptation", "url": "https://www.gov.uk/government/publications/government-financial-reporting-manual-2024-25"},
        {"publisher": "NHS England", "title": "BNSSG ICB system commissioning footprint", "url": "https://bnssg.icb.nhs.uk/"}
    ],
    "related": [
        "University Hospitals Bristol and Weston NHS Foundation Trust",
        "Premises & Infrastructure",
        "NHS England",
        "Department of Health and Social Care"
    ]
}

NEW["Other & adjustments — Great Western Hospitals NHS Foundation Trust"] = {
    "aliases": [{"name": "Other & adjustments", "parent": "Great Western Hospitals NHS Foundation Trust"}],
    "description": "Great Western Hospitals NHSFT's £0.25M Other & adjustments line is a Staff Costs disclosure cleanup covering prior-year payroll corrections, AME / DEL reclassifications, ESA10-aligned reclassifications, accruals true-ups and immaterial residual employer-cost items below DHSC GAM materiality thresholds for substantive sub-category disclosure. The trust runs the Great Western Hospital (Swindon) plus integrated community services across Wiltshire (post-2016 community-services TUPE).",
    "beneficiaries": "Indirect — adjustments affect net-cost allocation across c. 5,500 substantive WTE serving c. 380,000 residents across Swindon plus integrated community services for c. 700,000 across Wiltshire and BSW ICS footprint.",
    "legal_basis": "DHSC Group Accounting Manual 2024-25 disclosure rules · ESA10 sector-classification framework · IAS 1 Presentation of Financial Statements · IAS 19 Employee Benefits · NHS Act 2006 · Health and Care Act 2022",
    "key_stats": [
        {"label": "Other & adjustments 2024-25", "value": "£0.25M"},
        {"label": "Composition", "value": "Prior-year payroll corrections + AME / DEL reclassifications + accruals true-ups + immaterial residual employer-cost items"},
        {"label": "ESA10 framework", "value": "European System of Accounts 2010 — sector-classification rules cascading through DHSC GAM into trust disclosure"},
        {"label": "Trust scale anchor", "value": "c. 5,500 WTE across acute (Swindon) + Wiltshire integrated community services post-2016 TUPE"},
        {"label": "Site footprint", "value": "Great Western Hospital (Swindon) + community hospitals (Chippenham, Trowbridge, Warminster, Savernake, Devizes etc.) + community teams"},
        {"label": "DHSC GAM disclosure rule", "value": "Other & adjustments is a permitted catchall for items below materiality thresholds for substantive disclosure under DHSC GAM 2024-25"},
        {"label": "Funding trajectory", "value": "Variable year-on-year per cleanup volume; 2024-25 £0.25M reflects routine cleanup activity post-community-TUPE integration"},
        {"label": "Delivery body", "value": "GWH HR + Finance teams + NHSE Provider Finance + DHSC consolidation"},
        {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + Bath and North East Somerset, Swindon and Wiltshire (BSW) ICB"},
        {"label": "Beneficiary count", "value": "Indirect — affects net-cost allocation rather than direct-service delivery"},
        {"label": "Evaluation evidence", "value": "GWH ARA Note 8 staff-costs disclosure; DHSC GAM compliance; NHSE Provider Finance returns"},
        {"label": "Predecessor / successor", "value": "Predecessor: pre-DHSC GAM 2024-25 cleanup categorisation · Successor: continued residual disclosure under standard GAM rules; potential post-acute-MH partner reorganisation cleanup"}
    ],
    "notes": "GWH's Other & adjustments staff-costs line is recurring cleanup covering prior-year payroll corrections, ESA10 reclassifications and immaterial residuals below substantive sub-category materiality. The trust's hybrid acute-plus-community profile — Great Western Hospital (Swindon) PFI plus the c. 2016 Wiltshire community-services TUPE bringing in dispersed community hospitals and teams — generates more cleanup volume than a pure acute trust. The line is not a substantive policy lever but provides disclosure transparency under DHSC GAM 2024-25. BSW ICB reorganisation discussions and ongoing community-acute integration shape future cleanup volume.",
    "sources": [
        {"publisher": "Great Western Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.gwh.nhs.uk/about-us/publications/"},
        {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
        {"publisher": "NHS England", "title": "BSW ICB system overview", "url": "https://bsw.icb.nhs.uk/"},
        {"publisher": "Care Quality Commission", "title": "GWH provider profile (RN3)", "url": "https://www.cqc.org.uk/provider/RN3"},
        {"publisher": "HM Treasury", "title": "FReM 2024-25 ESA10 disclosure framework", "url": "https://www.gov.uk/government/publications/government-financial-reporting-manual-2024-25"}
    ],
    "related": [
        "Great Western Hospitals NHS Foundation Trust",
        "Staff Costs",
        "Department of Health and Social Care",
        "NHS England"
    ]
}

NEW["Inventories written down — Walsall Healthcare NHS Trust"] = {
    "aliases": [{"name": "Inventories written down", "parent": "Walsall Healthcare NHS Trust"}],
    "description": "Walsall Healthcare NHS Trust's £0.24M inventories-written-down line captures the IAS 2 charge for stock written off below cost — chiefly time-expired pharmaceuticals (general acute drugs, anti-infectives, anaesthetic agents), expired theatre consumables and surgical kit, expired wound-care and catheterisation stock, and obsolete bespoke implant inventory at Walsall Manor Hospital. The trust is mid-merger into the West Midlands group-model partnership with Royal Wolverhampton, sharing procurement and pharmacy frameworks.",
    "beneficiaries": "Acute inpatients across Walsall Manor Hospital (~550 beds — A&E, maternity, paediatrics, general medicine, general surgery, T&O) plus integrated community services across Walsall Borough (~285,000 pop); c. 95,000 ED attendances/yr; c. 4,000 WTE.",
    "legal_basis": "IAS 2 Inventories · DHSC Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · Drug Tariff (NHS Act 2006 Sch 1) · MHRA medicines regulation",
    "key_stats": [
        {"label": "Inventories written down 2024-25", "value": "£0.24M"},
        {"label": "Site anchor", "value": "Walsall Manor Hospital + integrated community estate across Walsall Borough"},
        {"label": "Catchment", "value": "c. 285,000 Walsall Borough residents; c. 95,000 ED attendances/yr"},
        {"label": "Workforce", "value": "c. 4,000 WTE across acute + community"},
        {"label": "Stock profile", "value": "Generic + branded drugs (acute formulary), theatre consumables (T&O, general surgery), wound-care, catheter and IV kits, bespoke T&O implants"},
        {"label": "Write-down driver", "value": "Time-expiry of low-turnover drugs + theatre kit obsolescence + bespoke implant size mix obsolescence + post-merger pharmacy harmonisation tail"},
        {"label": "Procurement route", "value": "NHS Supply Chain (national framework) + RWT-Walsall joint procurement (group-model alliance) + direct-to-supplier (specialist implants)"},
        {"label": "Funding trajectory", "value": "Stable to slight uplift on drug-price inflation; group-model integration with RWT may compress write-downs medium-term via pooled stock"},
        {"label": "Delivery body", "value": "Walsall Pharmacy + Procurement + Theatres stock control + NHS Supply Chain + RWT-Walsall joint pharmacy"},
        {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Black Country ICB + NHS Supply Chain"},
        {"label": "Evaluation evidence", "value": "Walsall ARA Note (inventories); CQC inspection (RBK); NHSE Operational Plan returns; Model Hospital procurement benchmarks"},
        {"label": "Predecessor / successor", "value": "Predecessor: pre-group-model standalone procurement · Successor: deeper RWT-Walsall group-model joint stock + Frontline Digitisation EPR-driven stock-management"}
    ],
    "notes": "Walsall's £0.24M write-down reflects routine IAS 2 NRV adjustment for an acute trust of this scale (c. £400M turnover). The trust operates within the West Midlands group-model alliance with Royal Wolverhampton (one CEO, joint pharmacy and procurement frameworks) which is gradually compressing duplicated stock and lifting bulk-buying scale. Drivers include drug-price inflation on generic anti-infectives and analgesics, T&O implant size-mix obsolescence (a long tail of bespoke sizes ages out), and ongoing post-Sandwell integration tail across the Black Country ICB pharmacy harmonisation. Recent context includes the Frontline Digitisation EPR rollout improving stock visibility and Model Hospital benchmarking driving Carter-style efficiency.",
    "sources": [
        {"publisher": "Walsall Healthcare NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.walsallhealthcare.nhs.uk/about-us/publications/"},
        {"publisher": "Care Quality Commission", "title": "Walsall Healthcare provider profile (RBK)", "url": "https://www.cqc.org.uk/provider/RBK"},
        {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (IAS 2 inventories)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
        {"publisher": "NHS Supply Chain", "title": "National framework annual report", "url": "https://www.supplychain.nhs.uk/"},
        {"publisher": "NHS England", "title": "Black Country ICB system overview", "url": "https://www.blackcountry.icb.nhs.uk/"}
    ],
    "related": [
        "Walsall Healthcare NHS Trust",
        "Clinical Supplies & Drugs",
        "NHS Supply Chain",
        "The Royal Wolverhampton NHS Trust"
    ]
}

NEW["Lease expenditure — North Cumbria Integrated Care NHS Foundation Trust"] = {
    "aliases": [{"name": "Lease expenditure", "parent": "North Cumbria Integrated Care NHS Foundation Trust"}],
    "description": "Operating lease expenditure (post-IFRS 16) at NCIC — covering short-life and low-value leased clinic, office and equipment estate held outside Right-of-Use balances under DHSC GAM treatment, plus operating leases on the trust's extensive vehicle fleet supporting community nursing, district nursing and integrated-community-physical services across the vast rural North Cumbria geography (Carlisle, West Cumbria, Penrith, Brampton, Wigton).",
    "beneficiaries": "Acute inpatients (Cumberland Infirmary Carlisle ~450 beds, West Cumberland Hospital Whitehaven ~210 beds), community hospital inpatients (Penrith, Workington, Wigton, Brampton, Maryport, Keswick, Alston) and dispersed community/district-nursing service users across c. 320,000 North Cumbrian residents over 2,500 sq miles.",
    "legal_basis": "IFRS 16 Leases (as adapted by FReM and DHSC GAM ch.7) · DHSC Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · Landlord and Tenant Act 1954",
    "key_stats": [
        {"label": "Lease expenditure 2024-25", "value": "£0.24M"},
        {"label": "Share of trust total opex", "value": "<0.1% of c. £450M"},
        {"label": "Coverage", "value": "Short-life (<12 months) and low-value (<£5k) leases excluded from RoU under GAM treatment"},
        {"label": "Site footprint", "value": "Cumberland Infirmary Carlisle (PFI 2000), West Cumberland Hospital Whitehaven, c. 8 community hospitals, dispersed clinic estate"},
        {"label": "Specific driver", "value": "Vehicle fleet operating leases (district nursing + community teams across rural geography) + minor clinic equipment hire"},
        {"label": "YoY change", "value": "c. +5-7% (lease re-pricing, fleet uplift, fuel-cost passthrough)"},
        {"label": "Delivery body", "value": "NCIC Estates & Facilities + Procurement + NHS Fleet Solutions + NHS Supply Chain framework leasing"},
        {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + North East and North Cumbria ICB"},
        {"label": "Funding trajectory", "value": "Slight upward — fleet electrification (Carbon Net Zero) and rural-mileage cost passthrough sustain growth"},
        {"label": "Evaluation evidence", "value": "NCIC ARA Note (lease disclosures); CQC inspection (RNL); NHSE Operational Plan returns; HSSIB RAAC list (excluded)"},
        {"label": "Predecessor / successor", "value": "Predecessor: pre-IFRS 16 operating-lease classification · Successor: continued GAM treatment + accelerating fleet electrification + potential New Hospital Programme replacement of West Cumberland"}
    ],
    "notes": "NCIC's £0.24M lease line is materially elevated by the trust's exceptionally rural footprint — covering c. 320,000 residents across 2,500 sq miles of North Cumbria. The trust's integrated acute + community + district-nursing remit sustains a large vehicle fleet across rural geography, captured under operating leases below IFRS 16 RoU thresholds. NCIC was created in 2019 from the merger of North Cumbria University Hospitals (acute) with Cumbria Partnership's North Cumbria community-services arm. Cumberland Infirmary Carlisle remains under a long-tail PFI (2000), and West Cumberland Hospital is in scope for the New Hospital Programme (deferred under the Jan 2025 NHP Reset, now post-2030 trajectory). Carbon Net Zero fleet electrification gradually shifts vehicle leases from ICE to BEV.",
    "sources": [
        {"publisher": "North Cumbria Integrated Care NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.ncic.nhs.uk/about-us/publications/annual-report-and-accounts"},
        {"publisher": "Care Quality Commission", "title": "NCIC provider profile (RNL)", "url": "https://www.cqc.org.uk/provider/RNL"},
        {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (ch.7 Leases)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
        {"publisher": "Department of Health and Social Care", "title": "New Hospital Programme review (Jan 2025 Reset)", "url": "https://www.gov.uk/government/publications/new-hospital-programme-plan-for-implementation"},
        {"publisher": "NHS England", "title": "North East and North Cumbria ICB system overview", "url": "https://northeastnorthcumbria.nhs.uk/"}
    ],
    "related": [
        "North Cumbria Integrated Care NHS Foundation Trust",
        "Premises & Infrastructure",
        "New Hospital Programme",
        "NHS England"
    ]
}

NEW["Inventories written down — Chesterfield Royal Hospital NHS Foundation Trust"] = {
    "aliases": [{"name": "Inventories written down", "parent": "Chesterfield Royal Hospital NHS Foundation Trust"}],
    "description": "Chesterfield Royal Hospital NHSFT's £0.24M inventories-written-down line captures the IAS 2 charge for stock written off below cost — chiefly time-expired pharmaceuticals (acute formulary including anti-infectives, anticoagulants, anaesthetic agents), expired theatre consumables, expired wound-care and IV stock, and bespoke implant/orthopaedic kit obsolescence. The trust runs a single-site DGH model serving North Derbyshire and parts of South Yorkshire from Chesterfield Royal Hospital.",
    "beneficiaries": "Acute inpatients (~550 beds — A&E, maternity, paediatrics, general medicine, T&O, general surgery, urology, gynaecology) plus elective and day-case patients across North Derbyshire and Bolsover (~410,000 catchment); c. 90,000 ED attendances/yr; c. 4,300 WTE.",
    "legal_basis": "IAS 2 Inventories · DHSC Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · Drug Tariff (NHS Act 2006 Sch 1) · MHRA medicines regulation",
    "key_stats": [
        {"label": "Inventories written down 2024-25", "value": "£0.24M"},
        {"label": "Site anchor", "value": "Chesterfield Royal Hospital — single-site DGH (Calow, Derbyshire)"},
        {"label": "Catchment", "value": "c. 410,000 North Derbyshire + Bolsover residents; c. 90,000 ED attendances/yr"},
        {"label": "Workforce", "value": "c. 4,300 WTE"},
        {"label": "Stock profile", "value": "Generic + branded drugs (acute formulary), theatre consumables (T&O, general surgery), wound-care, IV kits, bespoke T&O implants"},
        {"label": "Write-down driver", "value": "Time-expiry of low-turnover drugs + theatre kit obsolescence + bespoke implant size mix obsolescence"},
        {"label": "Procurement route", "value": "NHS Supply Chain (national framework) + East Midlands procurement collaboratives + direct-to-supplier (specialist implants)"},
        {"label": "Funding trajectory", "value": "Stable to slight uplift on drug-price inflation; Royal Primary Care wholly-owned-subsidiary integration tail completed"},
        {"label": "Delivery body", "value": "Chesterfield Pharmacy + Procurement + Theatres stock control + NHS Supply Chain"},
        {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Derby and Derbyshire ICB + NHS Supply Chain"},
        {"label": "Evaluation evidence", "value": "Chesterfield ARA Note (inventories); CQC inspection (RFS); NHSE Operational Plan returns; Model Hospital procurement benchmarks"},
        {"label": "Predecessor / successor", "value": "Predecessor: standalone DGH procurement · Successor: deeper East Midlands collaborative procurement + Frontline Digitisation EPR-driven stock-management"}
    ],
    "notes": "Chesterfield's £0.24M write-down reflects routine IAS 2 NRV adjustment for a single-site DGH of c. £350M turnover. The trust operates a wholly-owned-subsidiary primary-care arm (Royal Primary Care) which extends its procurement footprint beyond the acute formulary. Drivers include drug-price inflation on generic anti-infectives and analgesics, T&O implant size-mix obsolescence (a long tail of bespoke sizes ages out), and modest theatre-kit obsolescence on long-tail elective procedures. Recent context includes Frontline Digitisation EPR rollout improving stock visibility, Derby and Derbyshire ICB-wide pharmacy harmonisation, and Model Hospital benchmarking driving Carter-style efficiency targets.",
    "sources": [
        {"publisher": "Chesterfield Royal Hospital NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.chesterfieldroyal.nhs.uk/about-us/publications"},
        {"publisher": "Care Quality Commission", "title": "Chesterfield Royal provider profile (RFS)", "url": "https://www.cqc.org.uk/provider/RFS"},
        {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (IAS 2 inventories)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
        {"publisher": "NHS Supply Chain", "title": "National framework annual report", "url": "https://www.supplychain.nhs.uk/"},
        {"publisher": "NHS England", "title": "Derby and Derbyshire ICB system overview", "url": "https://joinedupcarederbyshire.co.uk/"}
    ],
    "related": [
        "Chesterfield Royal Hospital NHS Foundation Trust",
        "Clinical Supplies & Drugs",
        "NHS Supply Chain",
        "Department of Health and Social Care"
    ]
}

NEW["PFI / LIFT charges — Countess of Chester Hospital NHS Foundation Trust"] = {
    "aliases": [{"name": "PFI / LIFT charges", "parent": "Countess of Chester Hospital NHS Foundation Trust"}],
    "description": "Countess of Chester Hospital NHSFT's £0.24M residual PFI / LIFT charge captures the smaller LIFT (Local Improvement Finance Trust) and concession-related charges associated with primary-care/community estate adjuncts on the Countess of Chester campus and Ellesmere Port satellite — the trust does not host a major main-build PFI. The line covers the residual unitary-payment streams under IFRIC 12 / IFRS 16 service-concession treatment.",
    "beneficiaries": "Acute inpatients at Countess of Chester (~625 beds — A&E, maternity, paediatrics, general medicine, T&O, general surgery, neonatal) and Ellesmere Port satellite users across West Cheshire (~280,000 catchment); c. 90,000 ED attendances/yr; c. 4,000 WTE.",
    "legal_basis": "IFRIC 12 Service Concession Arrangements · IFRS 16 Leases (post-2022 reclassification) · DHSC Group Accounting Manual 2024-25 · DHSC PFI guidance · NHS (Private Finance) Act 1997 · NHS Act 2006",
    "key_stats": [
        {"label": "PFI / LIFT charges 2024-25", "value": "£0.24M"},
        {"label": "Scheme type", "value": "Residual LIFT and minor service-concession charges (no major main-build PFI on Countess campus)"},
        {"label": "Site anchor", "value": "Countess of Chester Hospital (Liverpool Road) + Ellesmere Port Hospital satellite"},
        {"label": "Catchment", "value": "c. 280,000 West Cheshire residents; c. 90,000 ED attendances/yr"},
        {"label": "Workforce", "value": "c. 4,000 WTE"},
        {"label": "Treatment", "value": "IFRIC 12 service-concession (where applicable) + IFRS 16 reclassification (post-2022) under DHSC GAM"},
        {"label": "Operator / counterparty", "value": "ProCure21+ legacy + LIFT vehicle (Express LIFT) for primary-care/community adjuncts"},
        {"label": "Funding trajectory", "value": "Declining as LIFT contracts approach end-of-term; stable charge over short-medium term"},
        {"label": "Delivery body", "value": "Trust E&F + LIFT operator + DHSC PFI Unit"},
        {"label": "Policy owner", "value": "DHSC PFI Unit + NHSE Provider Finance + Cheshire and Merseyside ICB"},
        {"label": "Evaluation evidence", "value": "Trust ARA Note (PFI/LIFT disclosures); HM Treasury PFI database; NAO PFI/PF2 reviews; CQC inspection (RJR)"},
        {"label": "Predecessor / successor", "value": "Predecessor: original LIFT contract initiation · Successor: end-of-LIFT-term hand-back to trust ownership; potential New Hospital Programme reconfiguration outside this line"}
    ],
    "notes": "Countess of Chester's £0.24M PFI/LIFT line is small relative to peers because the main hospital is not a substantial main-build PFI; the charge captures residual LIFT primary-care/community adjuncts and minor service-concession items. The trust bore intense national attention in 2023-25 around the Lucy Letby criminal proceedings and the resulting Thirlwall Inquiry into NHS governance, which has not directly affected the PFI/LIFT line but has reshaped the trust's executive leadership and oversight. The charge declines as LIFT terms approach end-of-contract hand-back. Cheshire and Merseyside ICB-level estate planning is shaping any successor New Hospital Programme reconfiguration.",
    "sources": [
        {"publisher": "Countess of Chester Hospital NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.coch.nhs.uk/about-us/publications/annual-report-accounts"},
        {"publisher": "HM Treasury", "title": "Private Finance Initiative database", "url": "https://www.gov.uk/government/publications/private-finance-initiative-and-private-finance-2-projects-2018-summary-data"},
        {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (PFI / IFRIC 12)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
        {"publisher": "Care Quality Commission", "title": "Countess of Chester provider profile (RJR)", "url": "https://www.cqc.org.uk/provider/RJR"},
        {"publisher": "Thirlwall Inquiry", "title": "Inquiry into the deaths and incidents at the Countess of Chester Hospital", "url": "https://thirlwall.public-inquiry.uk/"}
    ],
    "related": [
        "Countess of Chester Hospital NHS Foundation Trust",
        "Premises & Infrastructure",
        "HM Treasury",
        "Department of Health and Social Care"
    ]
}

NEW["Lease expenditure — Bradford Teaching Hospitals NHS Foundation Trust"] = {
    "aliases": [{"name": "Lease expenditure", "parent": "Bradford Teaching Hospitals NHS Foundation Trust"}],
    "description": "Operating lease expenditure (post-IFRS 16) at Bradford Teaching Hospitals NHSFT — covering short-life and low-value leased clinic, equipment and office estate held outside Right-of-Use balances under DHSC GAM treatment, plus operating leases on vehicle fleet supporting integrated community-physical services across Bradford. The trust runs Bradford Royal Infirmary, St Luke's Hospital and outpatient/community estate within the West Yorkshire Association of Acute Trusts (WYAAT).",
    "beneficiaries": "Acute inpatients at Bradford Royal Infirmary (~800 beds — A&E, maternity, paediatrics, general medicine, T&O, general surgery, oncology), St Luke's elective and rehab beds, plus community-physical service users across Bradford and Airedale, Wharfedale and Craven (~700,000 catchment); c. 130,000 ED attendances/yr; c. 6,500 WTE.",
    "legal_basis": "IFRS 16 Leases (as adapted by FReM and DHSC GAM ch.7) · DHSC Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · Landlord and Tenant Act 1954",
    "key_stats": [
        {"label": "Lease expenditure 2024-25", "value": "£0.24M"},
        {"label": "Share of trust total opex", "value": "<0.1% of c. £600M"},
        {"label": "Coverage", "value": "Short-life (<12 months) and low-value (<£5k) leases excluded from RoU under GAM treatment"},
        {"label": "Site footprint", "value": "Bradford Royal Infirmary + St Luke's Hospital + outpatient/community estate across Bradford district"},
        {"label": "Specific driver", "value": "Vehicle fleet operating leases (community-physical teams) + minor clinic equipment hire + temp office leases"},
        {"label": "YoY change", "value": "c. +5-7% (lease re-pricing, fleet uplift)"},
        {"label": "Delivery body", "value": "BTHFT Estates & Facilities + Procurement + NHS Fleet Solutions + NHS Supply Chain framework leasing"},
        {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + West Yorkshire ICB"},
        {"label": "Funding trajectory", "value": "Slight upward — Carbon Net Zero fleet electrification and equipment-hire passthrough"},
        {"label": "Evaluation evidence", "value": "BTHFT ARA Note (lease disclosures); CQC inspection (RAE); NHSE Operational Plan returns; Born-in-Bradford research-cohort programme"},
        {"label": "Predecessor / successor", "value": "Predecessor: pre-IFRS 16 operating-lease classification (pre-2022) · Successor: continued GAM treatment + NHP-deferred BRI rebuild trajectory + accelerating fleet electrification"}
    ],
    "notes": "Bradford's £0.24M lease line is small relative to overall opex but strategically anchored by the trust's diverse community-physical footprint and academic-research mission (Born-in-Bradford cohort, Wolfson Centre for Applied Health Research). The trust is part of the West Yorkshire Association of Acute Trusts (WYAAT) collaborative which shares procurement and is jointly addressing capacity at the regional level. Bradford Royal Infirmary was originally in the New Hospital Programme cohort; the Jan 2025 NHP Reset deferred the rebuild trajectory, sustaining the current site's operating-lease equipment-hire profile. Carbon Net Zero fleet electrification is gradually shifting community-team vehicle leases from ICE to BEV.",
    "sources": [
        {"publisher": "Bradford Teaching Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.bradfordhospitals.nhs.uk/about-us/annual-report-accounts/"},
        {"publisher": "Care Quality Commission", "title": "BTHFT provider profile (RAE)", "url": "https://www.cqc.org.uk/provider/RAE"},
        {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (ch.7 Leases)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
        {"publisher": "Department of Health and Social Care", "title": "New Hospital Programme review (Jan 2025 Reset)", "url": "https://www.gov.uk/government/publications/new-hospital-programme-plan-for-implementation"},
        {"publisher": "NHS England", "title": "West Yorkshire ICB system overview", "url": "https://www.wypartnership.co.uk/"}
    ],
    "related": [
        "Bradford Teaching Hospitals NHS Foundation Trust",
        "Premises & Infrastructure",
        "New Hospital Programme",
        "NHS England"
    ]
}

NEW["Inventories written down — Wirral University Teaching Hospital NHS Foundation Trust"] = {
    "aliases": [{"name": "Inventories written down", "parent": "Wirral University Teaching Hospital NHS Foundation Trust"}],
    "description": "Wirral University Teaching Hospital NHSFT's £0.24M inventories-written-down line captures the IAS 2 charge for stock written off below cost — chiefly time-expired pharmaceuticals (acute formulary anti-infectives, anaesthetic agents, anticoagulants), expired theatre consumables (T&O, vascular, gynaecology), wound-care and IV stock, and bespoke implant obsolescence. The trust runs Arrowe Park Hospital (Birkenhead) and Clatterbridge Hospital (Bebington — non-cancer) on the Wirral.",
    "beneficiaries": "Acute inpatients (~800 beds across Arrowe Park + Clatterbridge non-cancer wards — A&E, maternity, paediatrics, general medicine, T&O, general surgery, vascular) plus elective and day-case patients across the Wirral peninsula (~325,000 catchment); c. 100,000 ED attendances/yr; c. 5,500 WTE.",
    "legal_basis": "IAS 2 Inventories · DHSC Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · Drug Tariff (NHS Act 2006 Sch 1) · MHRA medicines regulation",
    "key_stats": [
        {"label": "Inventories written down 2024-25", "value": "£0.24M"},
        {"label": "Site anchor", "value": "Arrowe Park Hospital (Birkenhead) + Clatterbridge Hospital (Bebington — non-cancer wards)"},
        {"label": "Catchment", "value": "c. 325,000 Wirral residents; c. 100,000 ED attendances/yr"},
        {"label": "Workforce", "value": "c. 5,500 WTE"},
        {"label": "Stock profile", "value": "Generic + branded drugs (acute formulary), theatre consumables (T&O, vascular, gynae, general surgery), wound-care, IV kits, bespoke T&O + vascular implants"},
        {"label": "Write-down driver", "value": "Time-expiry of low-turnover drugs + theatre kit obsolescence + bespoke implant size-mix obsolescence + cross-Mersey procurement-harmonisation tail"},
        {"label": "Procurement route", "value": "NHS Supply Chain (national framework) + Cheshire and Merseyside collaborative procurement + direct-to-supplier (specialist implants)"},
        {"label": "Funding trajectory", "value": "Stable; £0.24M reflects routine IAS 2 cycle for c. £500M-turnover acute trust"},
        {"label": "Delivery body", "value": "WUTH Pharmacy + Procurement + Theatres stock control + NHS Supply Chain"},
        {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Cheshire and Merseyside ICB + NHS Supply Chain"},
        {"label": "Evaluation evidence", "value": "WUTH ARA Note (inventories); CQC inspection (RBL); NHSE Operational Plan returns; Model Hospital procurement benchmarks"},
        {"label": "Predecessor / successor", "value": "Predecessor: standalone Wirral procurement · Successor: deeper Cheshire and Merseyside collaborative + Frontline Digitisation EPR-driven stock-management"}
    ],
    "notes": "WUTH's £0.24M write-down reflects routine IAS 2 NRV adjustment for an acute trust of this scale (c. £500M turnover). The trust is anchored on the Arrowe Park acute site with elective work historically distributed across Clatterbridge (non-cancer) — note Clatterbridge Cancer Centre is a separate trust. Drivers include drug-price inflation on generic anti-infectives, T&O implant size-mix obsolescence, and cross-Mersey procurement-harmonisation tail under the Cheshire and Merseyside ICB collaborative. The trust's CQC profile and merger discussions with Countess of Chester (mooted historically) and ongoing system-level estate planning shape future stock-management investment.",
    "sources": [
        {"publisher": "Wirral University Teaching Hospital NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.wuth.nhs.uk/about-us/annual-reports-and-accounts/"},
        {"publisher": "Care Quality Commission", "title": "WUTH provider profile (RBL)", "url": "https://www.cqc.org.uk/provider/RBL"},
        {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (IAS 2 inventories)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
        {"publisher": "NHS Supply Chain", "title": "National framework annual report", "url": "https://www.supplychain.nhs.uk/"},
        {"publisher": "NHS England", "title": "Cheshire and Merseyside ICB system overview", "url": "https://www.cheshireandmerseyside.nhs.uk/"}
    ],
    "related": [
        "Wirral University Teaching Hospital NHS Foundation Trust",
        "Clinical Supplies & Drugs",
        "NHS Supply Chain",
        "Countess of Chester Hospital NHS Foundation Trust"
    ]
}

NEW["Inventories written down — Airedale NHS Foundation Trust"] = {
    "aliases": [{"name": "Inventories written down", "parent": "Airedale NHS Foundation Trust"}],
    "description": "Airedale NHSFT's £0.24M inventories-written-down line captures the IAS 2 charge for stock written off below cost — chiefly time-expired pharmaceuticals (acute formulary), expired theatre consumables, wound-care and IV stock, and bespoke implant obsolescence. The trust runs Airedale General Hospital (Steeton, near Keighley) — one of the c. 27 RAAC-affected sites identified in the September 2023 HSSIB list — alongside community services across Airedale, Wharfedale and Craven.",
    "beneficiaries": "Acute inpatients at Airedale General Hospital (~280 beds — A&E, maternity, paediatrics, general medicine, T&O, general surgery) plus community services across Airedale, Wharfedale, Craven and parts of West Yorkshire and East Lancashire (~200,000 catchment); c. 60,000 ED attendances/yr; c. 3,300 WTE.",
    "legal_basis": "IAS 2 Inventories · DHSC Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · Drug Tariff (NHS Act 2006 Sch 1) · MHRA medicines regulation",
    "key_stats": [
        {"label": "Inventories written down 2024-25", "value": "£0.24M"},
        {"label": "Site anchor", "value": "Airedale General Hospital (Steeton, near Keighley) — RAAC-affected site (HSSIB Sep 2023)"},
        {"label": "Catchment", "value": "c. 200,000 Airedale, Wharfedale, Craven residents; c. 60,000 ED attendances/yr"},
        {"label": "Workforce", "value": "c. 3,300 WTE"},
        {"label": "Stock profile", "value": "Generic + branded drugs (acute formulary), theatre consumables, wound-care, IV kits, bespoke T&O implants, telemedicine consumables (Airedale's Digital Care Hub)"},
        {"label": "Write-down driver", "value": "Time-expiry of low-turnover drugs + theatre kit obsolescence + bespoke implant size-mix obsolescence + RAAC-decant stock disruption"},
        {"label": "Procurement route", "value": "NHS Supply Chain (national framework) + WYAAT collaborative + direct-to-supplier (specialist implants)"},
        {"label": "Funding trajectory", "value": "Stable to slight uplift on drug-price inflation + RAAC-decant stock disruption tail"},
        {"label": "Delivery body", "value": "Airedale Pharmacy + Procurement + Theatres stock control + NHS Supply Chain"},
        {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + West Yorkshire ICB + NHS Supply Chain"},
        {"label": "Evaluation evidence", "value": "Airedale ARA Note (inventories); CQC inspection (RCF); NHSE Operational Plan returns; HSSIB RAAC list (Sep 2023); New Hospital Programme cohort"},
        {"label": "Predecessor / successor", "value": "Predecessor: standalone DGH procurement · Successor: NHP rebuild with new-build stock systems + WYAAT collaborative + Frontline Digitisation EPR-driven stock-management"}
    ],
    "notes": "Airedale's £0.24M write-down is shaped by both the routine IAS 2 NRV cycle and the operational disruption from RAAC mitigation — Airedale General was a structurally compromised concrete-plank site identified in the HSSIB September 2023 list, leading to ongoing decant, propping and ward-relocation activity. The trust has been confirmed in the New Hospital Programme cohort with construction priority retained through the January 2025 NHP Reset; rebuild on the existing site is planned to start within the next several years. Drivers include drug-price inflation, T&O implant size-mix obsolescence, and stock disruption around RAAC decant. Airedale also runs the national Digital Care Hub (telemedicine) which sustains a small specialist consumable footprint.",
    "sources": [
        {"publisher": "Airedale NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.airedale-trust.nhs.uk/about-us/publications-and-policies/"},
        {"publisher": "Care Quality Commission", "title": "Airedale provider profile (RCF)", "url": "https://www.cqc.org.uk/provider/RCF"},
        {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (IAS 2 inventories)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
        {"publisher": "Department of Health and Social Care", "title": "New Hospital Programme review (Jan 2025 Reset)", "url": "https://www.gov.uk/government/publications/new-hospital-programme-plan-for-implementation"},
        {"publisher": "Health Services Safety Investigations Body", "title": "RAAC concrete plank investigation (Sep 2023)", "url": "https://www.hssib.org.uk/"}
    ],
    "related": [
        "Airedale NHS Foundation Trust",
        "Clinical Supplies & Drugs",
        "New Hospital Programme",
        "NHS Supply Chain"
    ]
}

NEW["Lease expenditure — West Hertfordshire Hospitals NHS Trust"] = {
    "aliases": [{"name": "Lease expenditure", "parent": "West Hertfordshire Hospitals NHS Trust"}],
    "description": "Operating lease expenditure (post-IFRS 16) at West Hertfordshire Hospitals NHS Trust (now West Hertfordshire Teaching Hospitals NHS Trust) — covering short-life and low-value leased clinic, equipment and modular-ward estate held outside Right-of-Use balances under DHSC GAM treatment, plus operating leases on vehicle fleet and modular accommodation supporting the Watford General, St Albans and Hemel Hempstead sites pending the Watford rebuild under the New Hospital Programme.",
    "beneficiaries": "Acute inpatients at Watford General Hospital (~580 beds — A&E, maternity, paediatrics, general medicine, T&O), elective patients at St Albans City Hospital and outpatient/diagnostics users at Hemel Hempstead Hospital across South West Hertfordshire (~500,000 catchment); c. 130,000 ED attendances/yr; c. 5,000 WTE.",
    "legal_basis": "IFRS 16 Leases (as adapted by FReM and DHSC GAM ch.7) · DHSC Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · Landlord and Tenant Act 1954",
    "key_stats": [
        {"label": "Lease expenditure 2024-25", "value": "£0.23M"},
        {"label": "Share of trust total opex", "value": "<0.1% of c. £500M"},
        {"label": "Coverage", "value": "Short-life (<12 months) and low-value (<£5k) leases excluded from RoU under GAM treatment"},
        {"label": "Site footprint", "value": "Watford General Hospital + St Albans City Hospital + Hemel Hempstead Hospital + community estate"},
        {"label": "Specific driver", "value": "Modular-ward operating-lease elements + vehicle fleet + minor clinic equipment hire pending Watford rebuild"},
        {"label": "YoY change", "value": "c. +6-8% (modular accommodation uplift, lease re-pricing)"},
        {"label": "Delivery body", "value": "WHH Estates & Facilities + Procurement + NHS Fleet Solutions + NHS Supply Chain framework leasing"},
        {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Hertfordshire and West Essex ICB"},
        {"label": "Funding trajectory", "value": "Slight upward — Watford rebuild decant + modular elements + Carbon Net Zero fleet electrification"},
        {"label": "Evaluation evidence", "value": "WHH ARA Note (lease disclosures); CQC inspection (RWG); NHSE Operational Plan returns; New Hospital Programme cohort (Watford)"},
        {"label": "Predecessor / successor", "value": "Predecessor: pre-IFRS 16 operating-lease classification · Successor: continued GAM treatment + NHP-deferred Watford rebuild + accelerating fleet electrification"}
    ],
    "notes": "West Hertfordshire's £0.23M lease line is shaped by the trust's New Hospital Programme cohort status — Watford General Hospital is one of the original 40 hospitals committed to under NHP and was reprioritised under the January 2025 NHP Reset (construction-priority status retained but timeline shifted). The line captures modular-ward operating-lease elements and equipment hire supporting decant/expansion pending the Watford rebuild, plus vehicle fleet across the trust's three-site footprint. The trust took on a 'Teaching' designation in 2023 reflecting expanded medical-school placements with University of Hertfordshire. Carbon Net Zero fleet electrification is gradually shifting community-team vehicle leases.",
    "sources": [
        {"publisher": "West Hertfordshire Teaching Hospitals NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.westhertshospitals.nhs.uk/about/annualreport.asp"},
        {"publisher": "Care Quality Commission", "title": "WHH provider profile (RWG)", "url": "https://www.cqc.org.uk/provider/RWG"},
        {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (ch.7 Leases)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
        {"publisher": "Department of Health and Social Care", "title": "New Hospital Programme review (Jan 2025 Reset)", "url": "https://www.gov.uk/government/publications/new-hospital-programme-plan-for-implementation"},
        {"publisher": "NHS England", "title": "Hertfordshire and West Essex ICB system overview", "url": "https://hertsandwestessex.icb.nhs.uk/"}
    ],
    "related": [
        "West Hertfordshire Hospitals NHS Trust",
        "Premises & Infrastructure",
        "New Hospital Programme",
        "NHS England"
    ]
}

NEW["Inventories written down — Lewisham and Greenwich NHS Trust"] = {
    "aliases": [{"name": "Inventories written down", "parent": "Lewisham and Greenwich NHS Trust"}],
    "description": "Lewisham and Greenwich NHS Trust's £0.23M inventories-written-down line captures the IAS 2 charge for stock written off below cost — chiefly time-expired pharmaceuticals (acute formulary), expired theatre consumables (T&O, gynaecology, general surgery), wound-care and IV stock, and bespoke implant obsolescence. The trust runs University Hospital Lewisham and Queen Elizabeth Hospital Woolwich plus integrated community services across south-east London.",
    "beneficiaries": "Acute inpatients (~890 beds across UHL + QEH — A&E, maternity, paediatrics, general medicine, T&O, general surgery, gynae) plus community-services users across Lewisham and Royal Greenwich (~570,000 catchment); c. 230,000 ED attendances/yr; c. 6,500 WTE.",
    "legal_basis": "IAS 2 Inventories · DHSC Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · Drug Tariff (NHS Act 2006 Sch 1) · MHRA medicines regulation",
    "key_stats": [
        {"label": "Inventories written down 2024-25", "value": "£0.23M"},
        {"label": "Site anchor", "value": "University Hospital Lewisham + Queen Elizabeth Hospital Woolwich (PFI) + community estate"},
        {"label": "Catchment", "value": "c. 570,000 Lewisham + Royal Greenwich residents; c. 230,000 ED attendances/yr"},
        {"label": "Workforce", "value": "c. 6,500 WTE"},
        {"label": "Stock profile", "value": "Generic + branded drugs (acute formulary), theatre consumables (T&O, gynae, general surgery), wound-care, IV kits, bespoke T&O implants"},
        {"label": "Write-down driver", "value": "Time-expiry of low-turnover drugs + theatre kit obsolescence + bespoke implant size-mix obsolescence + cross-site (UHL + QEH) procurement-harmonisation tail"},
        {"label": "Procurement route", "value": "NHS Supply Chain (national framework) + South East London ICB collaborative + direct-to-supplier (specialist implants)"},
        {"label": "Funding trajectory", "value": "Stable to slight uplift on drug-price inflation; £0.23M reflects routine cycle for c. £700M-turnover trust"},
        {"label": "Delivery body", "value": "LGT Pharmacy + Procurement + Theatres stock control + NHS Supply Chain"},
        {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + South East London ICB + NHS Supply Chain"},
        {"label": "Evaluation evidence", "value": "LGT ARA Note (inventories); CQC inspection (RJ2); NHSE Operational Plan returns; Model Hospital procurement benchmarks"},
        {"label": "Predecessor / successor", "value": "Predecessor: pre-2013 separate Lewisham + South London Healthcare procurement · Successor: deeper SEL ICB collaborative + Frontline Digitisation EPR-driven stock-management"}
    ],
    "notes": "Lewisham and Greenwich's £0.23M write-down reflects routine IAS 2 NRV adjustment for an acute trust of c. £700M turnover. The trust was created in October 2013 from the merger of Lewisham Healthcare with the Queen Elizabeth Woolwich and Princess Royal Orpington elements following the South London Healthcare NHS Trust dissolution; ongoing post-merger procurement harmonisation continues to surface tail write-downs. Drivers include drug-price inflation on generic anti-infectives and analgesics, T&O implant size-mix obsolescence, and cross-site harmonisation tail. South East London ICB-wide collaborative procurement and Frontline Digitisation EPR rollout are the main forward levers.",
    "sources": [
        {"publisher": "Lewisham and Greenwich NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.lewishamandgreenwich.nhs.uk/about-us/our-publications/"},
        {"publisher": "Care Quality Commission", "title": "LGT provider profile (RJ2)", "url": "https://www.cqc.org.uk/provider/RJ2"},
        {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (IAS 2 inventories)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
        {"publisher": "NHS Supply Chain", "title": "National framework annual report", "url": "https://www.supplychain.nhs.uk/"},
        {"publisher": "NHS England", "title": "South East London ICB system overview", "url": "https://www.selondonics.org/"}
    ],
    "related": [
        "Lewisham and Greenwich NHS Trust",
        "Clinical Supplies & Drugs",
        "NHS Supply Chain",
        "Department of Health and Social Care"
    ]
}

NEW["Transport (business + patient) — Countess of Chester Hospital NHS Foundation Trust"] = {
    "aliases": [{"name": "Transport (business + patient)", "parent": "Countess of Chester Hospital NHS Foundation Trust"}],
    "description": "Countess of Chester Hospital NHSFT's £0.23M transport line covers business mileage reimbursement (AfC Section 17 + AMAP rates), pool fleet operating costs and non-emergency patient transport service (PTS) administration costs that fall onto trust ledgers — distinct from NHS England-commissioned PTS contracts handled by external providers. The trust serves West Cheshire from the Countess of Chester campus and the Ellesmere Port satellite.",
    "beneficiaries": "Acute inpatients and outpatients across the Countess of Chester (~625 beds) and Ellesmere Port satellite, plus c. 90,000 ED attendances/yr and outpatient transport users across West Cheshire (~280,000 catchment); c. 4,000 WTE eligible for business-mileage reimbursement.",
    "legal_basis": "NHS Act 2006 · NHSE Patient Transport Services Eligibility Criteria 2007 · Agenda for Change Section 17 (business mileage) + HMRC Approved Mileage Allowance Payments · IFRS 16 Leases (pool fleet) · DHSC Group Accounting Manual 2024-25",
    "key_stats": [
        {"label": "Transport (business + patient) 2024-25", "value": "£0.23M"},
        {"label": "Composition", "value": "Business mileage (AfC S17 + AMAP) + pool fleet operating cost + PTS-administration overheads"},
        {"label": "Site anchor", "value": "Countess of Chester Hospital + Ellesmere Port Hospital satellite"},
        {"label": "Catchment", "value": "c. 280,000 West Cheshire residents; c. 90,000 ED attendances/yr; outpatient + day-case transport demand"},
        {"label": "Workforce", "value": "c. 4,000 WTE eligible for business-mileage reimbursement"},
        {"label": "Specific driver", "value": "Two-site model + AMAP/AfC pence-per-mile uplift + community-and-clinic outreach mileage"},
        {"label": "YoY change", "value": "c. +5-7% (AMAP/AfC uplift, fuel passthrough)"},
        {"label": "Delivery body", "value": "Trust E&F + HR + Procurement + external NEPTS contractor (commissioned by ICB) + NHS Fleet Solutions"},
        {"label": "Policy owner", "value": "NHSE Patient Transport Services policy + Cheshire and Merseyside ICB (NEPTS commissioning) + DHSC"},
        {"label": "Funding trajectory", "value": "Slight upward — AMAP/AfC rate uplift, fleet electrification capex offset by lower running cost"},
        {"label": "Evaluation evidence", "value": "Trust ARA Note (operating costs disclosure); CQC inspection (RJR); NHSE NEPTS quality dashboards"},
        {"label": "Predecessor / successor", "value": "Predecessor: standalone PTS contract era · Successor: ICB-commissioned NEPTS framework + Carbon Net Zero fleet electrification + EV charging infrastructure"}
    ],
    "notes": "Countess of Chester's £0.23M transport line covers staff business mileage (AfC Section 17 + HMRC AMAP rates), pool fleet operating cost and PTS administration overhead falling onto the trust ledger — distinct from the NEPTS contract commissioned by Cheshire and Merseyside ICB and run by external providers. The two-site model (Countess + Ellesmere Port) sustains a higher business-mileage burden than a single-site DGH peer. Recent context includes the post-Letby Thirlwall Inquiry-era organisational scrutiny and ongoing executive change, alongside ICB-wide NEPTS commissioning reform and Carbon Net Zero fleet electrification gradually shifting pool vehicles from ICE to BEV.",
    "sources": [
        {"publisher": "Countess of Chester Hospital NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.coch.nhs.uk/about-us/publications/annual-report-accounts"},
        {"publisher": "NHS England", "title": "Patient Transport Services Eligibility Criteria + commissioning guidance", "url": "https://www.england.nhs.uk/commissioning/spec-services/npc-crg/group-d/d12/"},
        {"publisher": "HMRC", "title": "Approved Mileage Allowance Payments rates", "url": "https://www.gov.uk/expenses-and-benefits-business-travel-mileage"},
        {"publisher": "Care Quality Commission", "title": "Countess of Chester provider profile (RJR)", "url": "https://www.cqc.org.uk/provider/RJR"},
        {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"}
    ],
    "related": [
        "Countess of Chester Hospital NHS Foundation Trust",
        "Premises & Infrastructure",
        "NHS England",
        "Department of Health and Social Care"
    ]
}

NEW["Termination & post-employment — Great Western Hospitals NHS Foundation Trust"] = {
    "aliases": [{"name": "Termination & post-employment", "parent": "Great Western Hospitals NHS Foundation Trust"}],
    "description": "Great Western Hospitals NHSFT's £0.23M termination & post-employment line captures contractual exit-payment costs (redundancy, mutually agreed resignation scheme MARS-style settlements where applicable, payment-in-lieu) and post-employment benefit charges under IAS 19, distinct from ordinary NHS Pension Scheme employer contributions. The line covers acute (Swindon) plus integrated Wiltshire community-services workforce restructuring tail.",
    "beneficiaries": "Indirectly serves continuing service to c. 380,000 Swindon residents and c. 700,000 Wiltshire community-services users by enabling workforce reshape; immediate beneficiaries are c. 5,500 substantive WTE plus exiting staff receiving termination settlements.",
    "legal_basis": "IAS 19 Employee Benefits · NHS Pension Scheme Regulations 2008 / 2015 · DHSC Group Accounting Manual 2024-25 · NHS Act 2006 · Public Sector Exit Payments Regulations 2020 · HM Treasury approval framework for senior exits · TUPE 2006 · Health and Care Act 2022",
    "key_stats": [
        {"label": "Termination & post-employment 2024-25", "value": "£0.23M"},
        {"label": "Composition", "value": "Contractual redundancy + MARS-style settlements (where approved) + payment-in-lieu of notice + IAS 19 post-employment benefit charges (excl. ordinary pension contributions)"},
        {"label": "Trust scale anchor", "value": "c. 5,500 substantive WTE across acute (Swindon) + Wiltshire integrated community services post-2016 TUPE"},
        {"label": "Site footprint", "value": "Great Western Hospital (Swindon — PFI) + community hospitals across Wiltshire + community teams"},
        {"label": "HMT approval threshold", "value": "Senior exits >£95k floor and >£100k mandatory approval require HMT/DHSC sign-off (post-2020 framework)"},
        {"label": "Specific driver", "value": "Post-2016 community-services TUPE rebalancing tail + PFI-site management restructuring + finance-and-operations-leadership churn"},
        {"label": "YoY change", "value": "Variable — depends on annual restructuring volume; £0.23M reflects a routine operational year"},
        {"label": "Delivery body", "value": "GWH HR + Finance + DHSC consolidation + HMT (for senior cases) + NHSBSA (NHSPS post-employment processing)"},
        {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + BSW ICB + NHSBSA Pensions + HM Treasury"},
        {"label": "Beneficiary count", "value": "Variable annual exit caseload; indirect benefit to continuing c. 5,500 WTE workforce"},
        {"label": "Evaluation evidence", "value": "GWH ARA Note (staff costs disclosure); DHSC GAM compliance; HMT exit-payments compliance returns"},
        {"label": "Predecessor / successor", "value": "Predecessor: pre-2020 exit-payments framework · Successor: tighter post-2020 HMT control + ongoing acute-community integration restructuring"}
    ],
    "notes": "GWH's £0.23M termination and post-employment line covers contractual exit-payment costs and IAS 19 post-employment charges separate from ordinary NHS Pension Scheme employer contributions. The trust's hybrid acute-plus-community profile — Great Western Hospital (Swindon, PFI) plus the c. 2016 Wiltshire community-services TUPE — sustains a steady tail of restructuring activity as the integration matures. Senior exits above the post-2020 thresholds require HMT/DHSC approval. Recent context includes BSW ICB-wide reorganisation discussions, ongoing acute-community integration, and the April 2025 employer NIC step-up indirectly raising IAS 19 post-employment benefit obligations.",
    "sources": [
        {"publisher": "Great Western Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.gwh.nhs.uk/about-us/publications/"},
        {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (IAS 19 + exits)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
        {"publisher": "HM Treasury", "title": "Guidance on public sector exit payments", "url": "https://www.gov.uk/government/publications/guidance-on-public-sector-exit-payments"},
        {"publisher": "NHS Business Services Authority", "title": "NHS Pension Scheme employer guide", "url": "https://www.nhsbsa.nhs.uk/employer-hub"},
        {"publisher": "Care Quality Commission", "title": "GWH provider profile (RN3)", "url": "https://www.cqc.org.uk/provider/RN3"}
    ],
    "related": [
        "Great Western Hospitals NHS Foundation Trust",
        "Staff Costs",
        "NHS Business Services Authority",
        "HM Treasury"
    ]
}

NEW["Lease expenditure — East Suffolk and North Essex NHS Foundation Trust"] = {
    "aliases": [{"name": "Lease expenditure", "parent": "East Suffolk and North Essex NHS Foundation Trust"}],
    "description": "Operating lease expenditure (post-IFRS 16) at East Suffolk and North Essex NHSFT (ESNEFT) — covering short-life and low-value leased clinic, equipment and modular-ward estate held outside Right-of-Use balances under DHSC GAM treatment, plus operating leases on vehicle fleet supporting the Ipswich Hospital, Colchester Hospital, Aldeburgh, Bluebird Lodge and dispersed community estate across East Suffolk + North Essex.",
    "beneficiaries": "Acute inpatients (~1,200 beds across Ipswich + Colchester — A&E, maternity, paediatrics, general medicine, T&O, general surgery, oncology) plus community-services users across East Suffolk + North Essex (~1.0M catchment); c. 200,000 ED attendances/yr; c. 10,500 WTE.",
    "legal_basis": "IFRS 16 Leases (as adapted by FReM and DHSC GAM ch.7) · DHSC Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · Landlord and Tenant Act 1954",
    "key_stats": [
        {"label": "Lease expenditure 2024-25", "value": "£0.22M"},
        {"label": "Share of trust total opex", "value": "<0.1% of c. £900M"},
        {"label": "Coverage", "value": "Short-life (<12 months) and low-value (<£5k) leases excluded from RoU under GAM treatment"},
        {"label": "Site footprint", "value": "Ipswich Hospital + Colchester Hospital + community hospitals (Aldeburgh, Bluebird Lodge etc.) + dispersed community clinic estate"},
        {"label": "Specific driver", "value": "Vehicle fleet operating leases (community-physical teams) + minor clinic equipment hire + modular elements pending RAAC mitigation (Colchester scope)"},
        {"label": "YoY change", "value": "c. +5-7% (lease re-pricing, fleet uplift, RAAC-decant equipment)"},
        {"label": "Delivery body", "value": "ESNEFT Estates & Facilities + Procurement + NHS Fleet Solutions + NHS Supply Chain framework leasing"},
        {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Suffolk and North East Essex ICB"},
        {"label": "Funding trajectory", "value": "Slight upward — Carbon Net Zero fleet electrification + post-merger (2018) site-level estate harmonisation tail"},
        {"label": "Evaluation evidence", "value": "ESNEFT ARA Note (lease disclosures); CQC inspection (RDE); NHSE Operational Plan returns"},
        {"label": "Predecessor / successor", "value": "Predecessor: pre-merger Ipswich + Colchester separate lease portfolios (pre-2018) · Successor: continued GAM treatment + site-level estate harmonisation + accelerating fleet electrification"}
    ],
    "notes": "ESNEFT's £0.22M lease line is small relative to total opex but supported by a complex post-merger estate footprint. The trust was formed in July 2018 from the merger of Ipswich Hospital with Colchester Hospital University NHSFT, creating one of the largest NHS providers by site count in the East of England. Ipswich Hospital was originally part of the New Hospital Programme cohort under earlier prioritisation rounds. The trust operates a wholly-owned subsidiary (East Suffolk and North Essex Limited) for facilities management. Carbon Net Zero fleet electrification is gradually shifting community-team vehicle leases from ICE to BEV. The April 2025 employer NIC step-up indirectly raises the cost base around lease-supported community teams.",
    "sources": [
        {"publisher": "East Suffolk and North Essex NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.esneft.nhs.uk/about-us/our-publications/"},
        {"publisher": "Care Quality Commission", "title": "ESNEFT provider profile (RDE)", "url": "https://www.cqc.org.uk/provider/RDE"},
        {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (ch.7 Leases)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
        {"publisher": "NHS England", "title": "Suffolk and North East Essex ICB system overview", "url": "https://suffolkandnortheastessex.icb.nhs.uk/"},
        {"publisher": "Department of Health and Social Care", "title": "New Hospital Programme review (Jan 2025 Reset)", "url": "https://www.gov.uk/government/publications/new-hospital-programme-plan-for-implementation"}
    ],
    "related": [
        "East Suffolk and North Essex NHS Foundation Trust",
        "Premises & Infrastructure",
        "NHS England",
        "Department of Health and Social Care"
    ]
}

NEW["Inventories written down — Lancashire Teaching Hospitals NHS Foundation Trust"] = {
    "aliases": [{"name": "Inventories written down", "parent": "Lancashire Teaching Hospitals NHS Foundation Trust"}],
    "description": "Lancashire Teaching Hospitals NHSFT's £0.22M inventories-written-down line captures the IAS 2 charge for stock written off below cost — chiefly time-expired pharmaceuticals (acute formulary including specialist neurosciences, vascular, hepatobiliary stock), expired theatre consumables, wound-care and IV stock, and bespoke implant obsolescence. The trust runs Royal Preston Hospital (with major trauma centre, neurosciences, vascular) and Chorley & South Ribble Hospital.",
    "beneficiaries": "Acute inpatients (~870 beds across RPH + Chorley — A&E, MTC, neurosciences, vascular, HPB, T&O, general medicine, maternity, paediatrics) plus elective and day-case patients across Central Lancashire (~390,000 catchment); c. 170,000 ED attendances/yr; c. 8,500 WTE.",
    "legal_basis": "IAS 2 Inventories · DHSC Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · Drug Tariff (NHS Act 2006 Sch 1) · MHRA medicines regulation",
    "key_stats": [
        {"label": "Inventories written down 2024-25", "value": "£0.22M"},
        {"label": "Site anchor", "value": "Royal Preston Hospital (MTC, neurosciences, vascular, HPB) + Chorley & South Ribble Hospital"},
        {"label": "Catchment", "value": "c. 390,000 Central Lancashire residents direct + tertiary specialty referrals across Lancashire and South Cumbria; c. 170,000 ED attendances/yr"},
        {"label": "Workforce", "value": "c. 8,500 WTE"},
        {"label": "Stock profile", "value": "Acute formulary drugs + specialist neurosciences + vascular + HPB + MTC consumables + bespoke spinal/cranial implants + general theatre kit"},
        {"label": "Write-down driver", "value": "Time-expiry of low-turnover specialist drugs + bespoke neuro/vascular/spinal implant size-mix obsolescence + MTC trauma consumable rotation"},
        {"label": "Procurement route", "value": "NHS Supply Chain (national framework) + Lancashire and South Cumbria collaborative procurement + direct-to-supplier (specialist neuro/vascular implants)"},
        {"label": "Funding trajectory", "value": "Stable to slight uplift on drug-price inflation; MTC + tertiary specialty volume growth sustains specialist consumable turnover"},
        {"label": "Delivery body", "value": "LTH Pharmacy + Procurement + Theatres stock control + NHS Supply Chain"},
        {"label": "Policy owner", "value": "NHSE Provider Finance + Specialised Commissioning (neuro, vascular, MTC) + DHSC + Lancashire and South Cumbria ICB + NHS Supply Chain"},
        {"label": "Evaluation evidence", "value": "LTH ARA Note (inventories); CQC inspection (RXN); TARN MTC dashboards; NHSE Specialised Commissioning returns"},
        {"label": "Predecessor / successor", "value": "Predecessor: standalone Lancashire procurement · Successor: deeper Lancashire and South Cumbria ICB collaborative + Frontline Digitisation EPR-driven stock-management"}
    ],
    "notes": "Lancashire Teaching's £0.22M write-down reflects IAS 2 NRV adjustment for an acute trust of c. £750M turnover with substantial tertiary specialty footprint — Major Trauma Centre, neurosciences, vascular and hepatobiliary. The specialist mix raises the unit-cost profile of inventory while volume keeps individual write-downs constrained. Drivers include drug-price inflation on generic anti-infectives, bespoke neuro/spinal/vascular implant size-mix obsolescence, and MTC trauma-consumable rotation. The trust is a key anchor for Specialised Commissioning in Lancashire and South Cumbria ICB. The Royal Preston site has ageing estate elements and is in scope for longer-term New Hospital Programme replacement consideration (deferred under Jan 2025 Reset).",
    "sources": [
        {"publisher": "Lancashire Teaching Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.lancsteachinghospitals.nhs.uk/about-us/key-corporate-publications"},
        {"publisher": "Care Quality Commission", "title": "LTH provider profile (RXN)", "url": "https://www.cqc.org.uk/provider/RXN"},
        {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (IAS 2 inventories)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
        {"publisher": "NHS Supply Chain", "title": "National framework annual report", "url": "https://www.supplychain.nhs.uk/"},
        {"publisher": "NHS England", "title": "Lancashire and South Cumbria ICB system overview", "url": "https://www.healthierlsc.co.uk/"}
    ],
    "related": [
        "Lancashire Teaching Hospitals NHS Foundation Trust",
        "Clinical Supplies & Drugs",
        "NHS Supply Chain",
        "NHS England"
    ]
}

NEW["Termination & post-employment — Dorset County Hospital NHS Foundation Trust"] = {
    "aliases": [{"name": "Termination & post-employment", "parent": "Dorset County Hospital NHS Foundation Trust"}],
    "description": "Dorset County Hospital NHSFT's £0.22M termination & post-employment line captures contractual exit-payment costs (redundancy, MARS-style settlements where approved, payment-in-lieu) and IAS 19 post-employment benefit charges, distinct from ordinary NHS Pension Scheme employer contributions. The trust runs Dorset County Hospital (Dorchester) — a single-site DGH serving West Dorset, Weymouth and Portland and parts of Somerset.",
    "beneficiaries": "Indirectly serves continuing service to c. 215,000 Dorset, Weymouth, Portland residents by enabling workforce reshape; immediate beneficiaries are c. 3,000 substantive WTE plus exiting staff receiving termination settlements.",
    "legal_basis": "IAS 19 Employee Benefits · NHS Pension Scheme Regulations 2008 / 2015 · DHSC Group Accounting Manual 2024-25 · NHS Act 2006 · Public Sector Exit Payments Regulations 2020 · HM Treasury approval framework for senior exits · Health and Care Act 2022",
    "key_stats": [
        {"label": "Termination & post-employment 2024-25", "value": "£0.22M"},
        {"label": "Composition", "value": "Contractual redundancy + MARS-style settlements (where approved) + payment-in-lieu of notice + IAS 19 post-employment benefit charges"},
        {"label": "Trust scale anchor", "value": "c. 3,000 substantive WTE — single-site DGH + community midwifery/outreach"},
        {"label": "Site footprint", "value": "Dorset County Hospital (Dorchester) — single-site DGH"},
        {"label": "HMT approval threshold", "value": "Senior exits >£95k floor and >£100k mandatory approval require HMT/DHSC sign-off (post-2020 framework)"},
        {"label": "Specific driver", "value": "Smaller-trust staffing mix restructuring + Dorset ICB-wide pathway reform restructuring tail + executive churn across acute-and-system roles"},
        {"label": "YoY change", "value": "Variable — depends on annual restructuring volume; £0.22M reflects routine cycle"},
        {"label": "Delivery body", "value": "DCH HR + Finance + DHSC consolidation + HMT (for senior cases) + NHSBSA (NHSPS post-employment processing)"},
        {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + NHS Dorset ICB + NHSBSA Pensions + HM Treasury"},
        {"label": "Beneficiary count", "value": "Variable annual exit caseload; indirect benefit to continuing c. 3,000 WTE workforce"},
        {"label": "Evaluation evidence", "value": "DCH ARA Note (staff costs disclosure); DHSC GAM compliance; HMT exit-payments compliance returns"},
        {"label": "Predecessor / successor", "value": "Predecessor: pre-2020 exit-payments framework · Successor: tighter post-2020 HMT control + ongoing Dorset ICB pathway-reform restructuring"}
    ],
    "notes": "DCH's £0.22M termination and post-employment line covers contractual exit-payment costs and IAS 19 post-employment charges separate from ordinary NHS Pension Scheme employer contributions. As a single-site small acute trust serving West Dorset, Weymouth and Portland, DCH operates with a relatively lean workforce; restructuring volume is modest year-on-year. Senior exits above the post-2020 thresholds require HMT/DHSC approval. Recent context includes NHS Dorset ICB-wide acute pathway reorganisation and executive-leadership churn across the Dorset acute system (DCH alongside University Hospitals Dorset). The April 2025 employer NIC step-up indirectly raises IAS 19 obligations.",
    "sources": [
        {"publisher": "Dorset County Hospital NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.dchft.nhs.uk/about-us/publications/annual-report"},
        {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (IAS 19 + exits)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
        {"publisher": "HM Treasury", "title": "Guidance on public sector exit payments", "url": "https://www.gov.uk/government/publications/guidance-on-public-sector-exit-payments"},
        {"publisher": "NHS Business Services Authority", "title": "NHS Pension Scheme employer guide", "url": "https://www.nhsbsa.nhs.uk/employer-hub"},
        {"publisher": "Care Quality Commission", "title": "DCH provider profile (RBD)", "url": "https://www.cqc.org.uk/provider/RBD"}
    ],
    "related": [
        "Dorset County Hospital NHS Foundation Trust",
        "Staff Costs",
        "NHS Business Services Authority",
        "HM Treasury"
    ]
}

NEW["Inventories written down — United Lincolnshire Hospitals NHS Trust"] = {
    "aliases": [{"name": "Inventories written down", "parent": "United Lincolnshire Hospitals NHS Trust"}],
    "description": "United Lincolnshire Hospitals NHS Trust's £0.21M inventories-written-down line captures the IAS 2 charge for stock written off below cost — chiefly time-expired pharmaceuticals (acute formulary anti-infectives, anaesthetic agents), expired theatre consumables (T&O, general surgery, gynaecology), wound-care and IV stock, and bespoke implant obsolescence across the trust's distributed multi-site footprint covering Pilgrim Hospital Boston, Lincoln County Hospital, Grantham and District Hospital and County Hospital Louth.",
    "beneficiaries": "Acute inpatients (~1,000 beds across Lincoln + Boston + Grantham + Louth — A&E, maternity, paediatrics, general medicine, T&O, general surgery) across Lincolnshire (~750,000 catchment); c. 175,000 ED attendances/yr; c. 8,500 WTE.",
    "legal_basis": "IAS 2 Inventories · DHSC Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · Drug Tariff (NHS Act 2006 Sch 1) · MHRA medicines regulation",
    "key_stats": [
        {"label": "Inventories written down 2024-25", "value": "£0.21M"},
        {"label": "Site anchor", "value": "Lincoln County Hospital + Pilgrim Hospital Boston + Grantham and District Hospital + County Hospital Louth"},
        {"label": "Catchment", "value": "c. 750,000 Lincolnshire residents across rural footprint; c. 175,000 ED attendances/yr"},
        {"label": "Workforce", "value": "c. 8,500 WTE"},
        {"label": "Stock profile", "value": "Generic + branded drugs (acute formulary), theatre consumables, wound-care, IV kits, bespoke T&O implants distributed across 4 sites"},
        {"label": "Write-down driver", "value": "Time-expiry of low-turnover drugs + theatre kit obsolescence + multi-site stock-distribution inefficiency + bespoke implant size-mix obsolescence + Acute Services Review reconfiguration tail"},
        {"label": "Procurement route", "value": "NHS Supply Chain (national framework) + East Midlands procurement collaboratives + ULTRA (proposed merger with Lincolnshire Community Health Services pathway) + direct-to-supplier"},
        {"label": "Funding trajectory", "value": "Stable to slight uplift on drug-price inflation; multi-site distribution inefficiency may compress under proposed merger with LCHS"},
        {"label": "Delivery body", "value": "ULHT Pharmacy + Procurement + Theatres stock control + NHS Supply Chain"},
        {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Lincolnshire ICB + NHS Supply Chain"},
        {"label": "Evaluation evidence", "value": "ULHT ARA Note (inventories); CQC inspection (RWD); NHSE Operational Plan returns; Lincolnshire Acute Services Review"},
        {"label": "Predecessor / successor", "value": "Predecessor: standalone multi-site ULHT procurement · Successor: proposed merger with Lincolnshire Community Health Services + EMRAS reconfiguration + Frontline Digitisation EPR-driven stock-management"}
    ],
    "notes": "ULHT's £0.21M write-down reflects routine IAS 2 NRV adjustment shaped by the trust's distributed four-site rural Lincolnshire footprint, where stock-distribution inefficiency drives more write-down volume than peer single-site DGHs. Drivers include drug-price inflation, T&O implant size-mix obsolescence, and ongoing reconfiguration tail under the long-running Lincolnshire Acute Services Review (Pilgrim Boston paediatric and maternity reconfiguration debate). The trust has been in discussions about merger with Lincolnshire Community Health Services NHS Trust under Lincolnshire ICB direction. CQC has placed the trust in heightened oversight in recent years; Frontline Digitisation EPR rollout improving stock visibility is a key forward lever.",
    "sources": [
        {"publisher": "United Lincolnshire Hospitals NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.ulh.nhs.uk/about/publications/"},
        {"publisher": "Care Quality Commission", "title": "ULHT provider profile (RWD)", "url": "https://www.cqc.org.uk/provider/RWD"},
        {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (IAS 2 inventories)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
        {"publisher": "NHS Supply Chain", "title": "National framework annual report", "url": "https://www.supplychain.nhs.uk/"},
        {"publisher": "NHS England", "title": "Lincolnshire ICB system overview", "url": "https://lincolnshire.icb.nhs.uk/"}
    ],
    "related": [
        "United Lincolnshire Hospitals NHS Trust",
        "Clinical Supplies & Drugs",
        "NHS Supply Chain",
        "NHS England"
    ]
}
