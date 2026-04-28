# -*- coding: utf-8 -*-
# Phase 2 Acute slice 2 — chunk 37 (17 NHS Acute Trust orphan sub-lines)
# Hand-curated trust-specific PROGRAMME-archetype enrichment entries.
# Structural contract per docs/archetype_briefs.md.

NEW = {
    "Termination & post-employment — Somerset NHS Foundation Trust": {
        "aliases": [{"name": "Termination & post-employment", "parent": "Somerset NHS Foundation Trust"}],
        "description": "Somerset NHS FT's £1.006M termination & post-employment line covers IAS 19 termination benefits (redundancies, MARS-style mutually agreed resignations and end-of-contract settlements) plus actuarial movement on residual post-employment defined-benefit obligations across the integrated acute + community + mental health footprint formed by the April 2020 merger of Taunton & Somerset NHS FT with Somerset Partnership NHS FT, then 1 April 2023 acquisition of Yeovil District Hospital NHS FT to create a single county-wide vertically integrated trust.",
        "beneficiaries": "c. 13,500 WTE staff serving the c. 580,000 population of Somerset (Musgrove Park Hospital, Taunton; Yeovil District Hospital; community + mental-health footprint countywide); c. 165,000 ED attendances/yr at Musgrove + Yeovil; c. 100,000 admissions/yr; sole vertically-integrated acute-community-MH provider for the county.",
        "legal_basis": "IAS 19 Employee Benefits — NHS Pension Scheme Regulations 2015 — Public Sector Exit Payments Regulations 2020 (revoked Feb 2021; HMT cap consultation ongoing) — DHSC Group Accounting Manual 2024-25 — NHS Act 2006 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Termination & post-employment 2024-25", "value": "£1.006M"},
            {"label": "Trust scale", "value": "Musgrove Park Hospital (Taunton) + Yeovil District Hospital + community + MH footprint; c. 13,500 WTE — sole county-wide vertically-integrated provider"},
            {"label": "Merger origin", "value": "April 2020 acute-MH-community merger (Taunton & Somerset + Somerset Partnership) + 1 April 2023 Yeovil District Hospital acquisition — workforce harmonisation feeds redundancy line"},
            {"label": "Composition", "value": "IAS 19 termination benefits (redundancies + MARS settlements + end-of-contract) + actuarial movement on residual post-employment DB obligations"},
            {"label": "NHS Pension Scheme", "value": "Most staff in NHS Pension Scheme (DB; funded employer contribution at 23.7% from April 2024); small residual legacy DB liabilities at trust level"},
            {"label": "Yeovil acquisition consolidation", "value": "Post-April-2023 specialty consolidation Musgrove ↔ Yeovil (e.g. stroke + maternity rationalisation under review) drives ongoing redundancy and redeployment"},
            {"label": "Public Sector Exit Payments", "value": "2020 £95k cap revoked Feb 2021; HMT consultation pending; £80k MARS scheme guidance currently applies"},
            {"label": "April 2025 NIC step-up", "value": "Direct hit on cost-of-employment + indirect on redundancy NIC component (15% over £5k threshold)"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes raised locum/agency dependency but limited direct termination impact"},
            {"label": "Funding trajectory", "value": "2021-22 c. £0.7M → 2023-24 c. £0.9M → 2024-25 £1.006M — Yeovil-acquisition harmonisation peak working through"},
            {"label": "Somerset ICS", "value": "Member of Somerset ICB; trust = lead provider for the system (acute + MH + community vertical)"},
            {"label": "Delivery body", "value": "Trust HR + NHSBSA Pensions + Government Actuary's Department (scheme actuarial) + NHS Resolution (employer liability)"},
            {"label": "Policy owner", "value": "DHSC + HM Treasury (exit payments cap) + NHSE Provider Finance + Somerset ICB"},
            {"label": "Evaluation evidence", "value": "NAO NHS Workforce report 2020; HMT Public Sector Exit Payments consultation; Trust ARA 2023-24; CQC RH5 inspections"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2020 separate Taunton & Somerset + Somerset Partnership + Yeovil baselines · Successor: Somerset ICB-aligned single workforce strategy"}
        ],
        "notes": "Somerset NHS FT's termination line carries the residual workforce-harmonisation cost from a two-step integration: the April 2020 acute + MH + community merger of Taunton & Somerset NHS FT with Somerset Partnership NHS FT, followed by the 1 April 2023 Yeovil District Hospital NHS FT acquisition that completed the county-wide vertically integrated provider. Specialty consolidation between Musgrove Park (Taunton) and Yeovil (under review for stroke and maternity pathway changes) drives ongoing redundancy and redeployment provisions. HMT's Public Sector Exit Payments £95k cap was revoked February 2021 and remains under consultation. April 2025 employer NIC step-up (15%, £5k threshold) hits cost-of-employment directly and indirectly through the redundancy NIC component. The trust's vertically integrated model is a national reference point for ICS-aligned provider design.",
        "sources": [
            {"publisher": "Somerset NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.somersetft.nhs.uk/about-us/publications/"},
            {"publisher": "HM Treasury", "title": "Public sector exit payments — guidance", "url": "https://www.gov.uk/government/publications/public-sector-exit-payments-guidance-on-special-severance-payments"},
            {"publisher": "NHS Business Services Authority", "title": "NHS Pension Scheme — employer hub", "url": "https://www.nhsbsa.nhs.uk/employer-hub"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Somerset NHS Foundation Trust provider profile (RH5)", "url": "https://www.cqc.org.uk/provider/RH5"}
        ],
        "related": ["Somerset NHS Foundation Trust", "Staff Costs", "NHS Acute Trusts", "Lease expenditure — Somerset NHS Foundation Trust", "NHS Pension Scheme", "Somerset ICB"]
    },
    "Lease expenditure — University Hospitals of Derby and Burton NHS Foundation Trust": {
        "aliases": [{"name": "Lease expenditure", "parent": "University Hospitals of Derby and Burton NHS Foundation Trust"}],
        "description": "UHDB's £0.997M lease expenditure line covers IFRS 16 right-of-use lease costs (interest unwind plus residual operating-lease elements outside the IFRS 16 capitalisation envelope) across the trust's five-hospital footprint formed by the July 2018 merger of Derby Teaching Hospitals and Burton Hospitals — Royal Derby Hospital, Queen's Hospital Burton, Sir Robert Peel Community Hospital (Tamworth), Samuel Johnson Community Hospital (Lichfield) and London Road Community Hospital (Derby). Pool fleet, modular clinical units, IT equipment and minor sites form the underlying portfolio.",
        "beneficiaries": "c. 13,500 WTE staff serving a c. 1.05M Derbyshire + East Staffordshire catchment (Derby, Burton, Tamworth, Lichfield, Uttoxeter, South Derbyshire); c. 220,000 ED attendances/yr at Royal Derby + Queen's Burton ED; c. 165,000 admissions/yr; cross-ICB-border footprint (Joined Up Care Derbyshire + Staffordshire ICS).",
        "legal_basis": "IFRS 16 Leases — DHSC Group Accounting Manual 2024-25 chapter 7 — Landlord and Tenant Act 1954 — NHS Act 2006 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Lease expenditure 2024-25", "value": "£0.997M"},
            {"label": "Trust scale", "value": "Royal Derby + Queen's Burton + Sir Robert Peel + Samuel Johnson + London Road; c. 13,500 WTE"},
            {"label": "IFRS 16 transition (1 Apr 2022)", "value": "DHSC mandated IFRS 16 adoption for NHS bodies from 1 Apr 2022 — bulk of operating leases now on-balance-sheet right-of-use assets; residual short-term + low-value leases remain in lease expenditure"},
            {"label": "Composition", "value": "IFRS 16 interest unwind + short-term lease cost (<12 months) + low-value lease cost + IFRS 16-out scope items (variable lease, very-low-value)"},
            {"label": "PFI overlap", "value": "Royal Derby is PFI-financed (Catalyst Healthcare Project Co) — PFI unitary charge sits in the PFI/LIFT line, not Lease expenditure"},
            {"label": "Modular clinical units", "value": "Post-pandemic modular ward and diagnostic capacity (e.g. CDC contributions) feed short-term lease element"},
            {"label": "Pool fleet + IT", "value": "Vehicle pool fleet (IFRS 16) + IT and medical-equipment leases — typical mid-sized trust portfolio"},
            {"label": "April 2025 NIC step-up", "value": "Indirect — landlord cost-pass-through on services associated with leased premises (15% over £5k)"},
            {"label": "Funding trajectory", "value": "Pre-IFRS 16 (FY22) higher reported operating-lease P&L → FY23 IFRS 16 step-down (most leases capitalised) → 2024-25 £0.997M — residual short-term + low-value tail"},
            {"label": "Joined Up Care Derbyshire ICS", "value": "Member of Joined Up Care Derbyshire ICB (Royal Derby footprint) and Staffordshire & Stoke-on-Trent ICB (Burton/Tamworth/Lichfield footprint)"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + Procurement + Finance (lease accounting) + NHS Property Services (where applicable)"},
            {"label": "Policy owner", "value": "DHSC + HM Treasury (IFRS 16 transition guidance) + NHSE Provider Finance + Joined Up Care Derbyshire ICB"},
            {"label": "Evaluation evidence", "value": "DHSC GAM IFRS 16 transition guidance; Trust ARA 2023-24 lease note; CQC RTG inspections; NAO NHS estates reports"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-IFRS 16 operating-lease accounting (FY22 baseline) · Successor: ongoing IFRS 16 reassessment cycle + ICB-wide pool-fleet consolidation"}
        ],
        "notes": "UHDB's lease expenditure line reflects the post-IFRS-16-transition residual — the bulk of the trust's former operating-lease portfolio was capitalised as right-of-use assets from 1 April 2022 under DHSC GAM mandate, leaving only short-term (<12 months) and low-value leases plus the IFRS 16 interest-unwind element in the P&L lease expenditure line. The Royal Derby PFI unitary charge sits in the separate PFI/LIFT line. Five-site geography (Derby, Burton, Tamworth, Lichfield, Uttoxeter via community sites) drives a structural pool-fleet and modular-unit lease portfolio. Post-pandemic modular ward and diagnostic capacity additions (Community Diagnostic Centres) feed the short-term lease element. April 2025 employer NIC step-up flows indirectly through landlord and FM-services pass-through.",
        "sources": [
            {"publisher": "University Hospitals of Derby and Burton NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.uhdb.nhs.uk/annual-reports-and-accounts/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 chapter 7 (leases)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "HM Treasury", "title": "IFRS 16 implementation in central government", "url": "https://www.gov.uk/government/publications/financial-reporting-manual-2024-25"},
            {"publisher": "Care Quality Commission", "title": "University Hospitals of Derby and Burton NHS FT provider profile (RTG)", "url": "https://www.cqc.org.uk/provider/RTG"},
            {"publisher": "National Audit Office", "title": "NHS estates and facilities", "url": "https://www.nao.org.uk/reports/nhs-financial-management-and-sustainability/"}
        ],
        "related": ["University Hospitals of Derby and Burton NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Business rates — University Hospitals of Derby and Burton NHS Foundation Trust", "PFI / LIFT charges — University Hospitals of Derby and Burton NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Transport (business + patient) — Dorset County Hospital NHS Foundation Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "Dorset County Hospital NHS Foundation Trust"}],
        "description": "Dorset County Hospital NHS FT's £0.985M transport line covers staff business mileage (AfC Section 17 + HMRC AMAP rates), pool-fleet leases (IFRS 16 right-of-use), inter-site courier and pathology specimen transport between Dorset County Hospital (Dorchester) and partner trusts, plus contracted non-emergency patient transport (NEPTS) for the rural Dorset catchment. The trust's geography — covering a large rural West Dorset area with long road distances and a single acute site — drives a structural travel premium per WTE compared with urban DGH peers.",
        "beneficiaries": "c. 3,000 WTE staff serving a c. 215,000 West and Mid Dorset catchment (Dorchester, Weymouth, Bridport, Sherborne, Portland) including a large geriatric/retiree demographic; c. 60,000 ED attendances/yr; c. 38,000 admissions/yr; c. 280,000 outpatient attendances/yr; rural catchment with significant tourism inflow over summer.",
        "legal_basis": "NHS Act 2006 — NHS England Patient Transport Services Eligibility Criteria — Agenda for Change Section 17 + HMRC AMAP rates — IFRS 16 Leases (pool fleet) — DHSC Group Accounting Manual 2024-25 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£0.985M"},
            {"label": "Trust scale", "value": "Dorset County Hospital (Dorchester) — single-site DGH plus outreach clinics; c. 3,000 WTE"},
            {"label": "Composition", "value": "Staff business mileage (AfC Sec 17 + AMAP) + pool fleet (IFRS 16) + inter-site pathology/blood-product courier + contracted NEPTS"},
            {"label": "NEPTS provider", "value": "E-zec Medical Transport Services / South Western Ambulance Service NHS FT (regional NEPTS framework)"},
            {"label": "Rural geography premium", "value": "Long road distances Bridport ↔ Dorchester ↔ Weymouth + Sherborne; outreach clinic mileage + courier flows drive structural premium per WTE"},
            {"label": "Tertiary referral patterns", "value": "Tertiary flow to UHD (Bournemouth/Poole) and Salisbury NHS FT (specialist services) — additional inter-trust transport demand"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove locum travel reimbursement + NEPTS rebooking spike"},
            {"label": "April 2025 NIC step-up", "value": "Indirect via NEPTS contractor + agency-driver pass-through (15% over £5k threshold)"},
            {"label": "AMAP rates 2024-25", "value": "HMRC AMAP unchanged at 45p/mile first 10,000 + 25p thereafter — frozen since 2011, eroding real-terms reimbursement"},
            {"label": "Funding trajectory", "value": "2021-22 c. £0.7M → 2023-24 c. £0.9M → 2024-25 £0.985M — strike backfill + fuel-cost pass-through + NEPTS uplift"},
            {"label": "Dorset ICS", "value": "Member of Dorset ICB; collaborative NEPTS commissioning with UHD and SWASFT"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + Pathology + Transport Office + E-zec Medical / SWASFT (NEPTS)"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + NHSE Patient Transport Services policy + DHSC + Dorset ICB"},
            {"label": "Evaluation evidence", "value": "NHSE Non-Emergency Patient Transport Services Review 2021; Trust ARA 2023-24; CQC RBD inspections"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-NEPTS-Review-2021 baseline · Successor: NEPTS-Review-aligned eligibility implementation + Dorset-wide pool-fleet consolidation"}
        ],
        "notes": "Dorset County Hospital NHS FT's transport line is shaped by the trust's rural geography — a single-site DGH in Dorchester serving a sparse, dispersed West/Mid Dorset population (Bridport, Weymouth, Sherborne, Portland) with long inter-clinic road distances, plus a tertiary-referral pattern out to UHD (Bournemouth/Poole) and Salisbury NHS FT. The 2023-24 industrial-action cycle (44 days junior-doctor + 10 days consultant strikes) added locum travel reimbursement and NEPTS rebooking cost. The NEPTS contract sits with E-zec Medical / SWASFT under the Dorset ICB framework, aligned with the NHSE Patient Transport Services Review eligibility criteria (2021). HMRC's AMAP rates have been frozen at 45p/25p since 2011, structurally compressing the staff-mileage element in real terms. April 2025 employer NIC step-up flows indirectly via NEPTS contractor pass-through.",
        "sources": [
            {"publisher": "Dorset County Hospital NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.dchft.nhs.uk/about-us/our-publications/"},
            {"publisher": "NHS England", "title": "Non-Emergency Patient Transport Services Review", "url": "https://www.england.nhs.uk/publication/non-emergency-patient-transport-services-review/"},
            {"publisher": "HMRC", "title": "Approved Mileage Allowance Payments (AMAP) rates", "url": "https://www.gov.uk/government/publications/rates-and-allowances-travel-mileage-and-fuel-allowances"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Dorset County Hospital NHS Foundation Trust provider profile (RBD)", "url": "https://www.cqc.org.uk/provider/RBD"}
        ],
        "related": ["Dorset County Hospital NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Dorset ICB", "Transport (business + patient) — University Hospitals Dorset NHS Foundation Trust", "South Western Ambulance Service NHS Foundation Trust"]
    },
    "Transport (business + patient) — Airedale NHS Foundation Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "Airedale NHS Foundation Trust"}],
        "description": "Airedale NHS FT's £0.980M transport line covers staff business mileage (AfC Section 17 + HMRC AMAP), pool-fleet leases (IFRS 16 right-of-use), inter-site courier and pathology specimen transport, plus contracted non-emergency patient transport (NEPTS) for the Airedale, Wharfedale and Craven catchment. Airedale General Hospital (Steeton, near Keighley) is on the RAAC HSSIB priority list — concrete-plank mitigation has driven decant/move-of-service transport and patient-shuttle costs since 2023, structurally elevating the line above peer DGHs.",
        "beneficiaries": "c. 3,500 WTE staff serving a c. 200,000 catchment across Airedale, Wharfedale, Craven and parts of South Lakeland (Keighley, Skipton, Settle, Ilkley); c. 70,000 ED attendances/yr; c. 45,000 admissions/yr; c. 290,000 outpatient attendances/yr; rural North Yorkshire / Pennines geography with long-distance referral flows to Bradford, Leeds and Lancaster.",
        "legal_basis": "NHS Act 2006 — NHS England Patient Transport Services Eligibility Criteria — Agenda for Change Section 17 + HMRC AMAP rates — IFRS 16 Leases (pool fleet) — DHSC Group Accounting Manual 2024-25 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£0.980M"},
            {"label": "Trust scale", "value": "Airedale General Hospital (Steeton) + community footprint across Airedale/Wharfedale/Craven; c. 3,500 WTE"},
            {"label": "RAAC priority", "value": "Airedale General is on the 2023 HSSIB RAAC critical-mitigation list — drives decant/shuttle transport + NHP rebuild (planned)"},
            {"label": "NHP cohort", "value": "Member of New Hospital Programme RAAC cohort — full rebuild planned; NHP Reset Jan 2025 confirmed RAAC trusts retain 2030 priority"},
            {"label": "Composition", "value": "Staff business mileage (AfC Sec 17 + AMAP) + pool fleet (IFRS 16) + inter-site pathology courier + contracted NEPTS + RAAC decant patient-shuttle"},
            {"label": "NEPTS provider", "value": "Yorkshire Ambulance Service NHS Trust / commissioned via West Yorkshire ICB framework"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove locum travel reimbursement + NEPTS rebooking spike"},
            {"label": "April 2025 NIC step-up", "value": "Indirect via NEPTS contractor + agency-driver pass-through (15% over £5k threshold)"},
            {"label": "AMAP rates 2024-25", "value": "HMRC AMAP unchanged at 45p/mile first 10,000 + 25p thereafter — frozen since 2011"},
            {"label": "Funding trajectory", "value": "2021-22 c. £0.6M → 2023-24 c. £0.9M → 2024-25 £0.980M — RAAC mitigation transport + strike backfill + fuel-cost pass-through"},
            {"label": "West Yorkshire ICS", "value": "Member of West Yorkshire ICB; collaborative NEPTS commissioning"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + Pathology + Transport Office + Yorkshire Ambulance Service (NEPTS)"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + NHSE NEPTS policy + DHSC + West Yorkshire ICB + NHP team (DHSC) for RAAC"},
            {"label": "Evaluation evidence", "value": "HSSIB RAAC site-list 2023; NHP Reset Jan 2025 update; Trust ARA 2023-24; CQC RCF inspections"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-RAAC-mitigation baseline (FY22) · Successor: NHP rebuild logistics + post-RAAC steady-state"}
        ],
        "notes": "Airedale NHS FT's transport line is uniquely shaped by the trust's RAAC exposure — Airedale General Hospital (Steeton) is on the 2023 HSSIB critical-mitigation list with extensive concrete-plank decant and service-relocation activity since 2023, driving a structural patient-shuttle and inter-site transport cost above peer DGHs of similar scale. The trust is in the New Hospital Programme RAAC cohort with a full rebuild planned; NHP Reset (January 2025) confirmed RAAC trusts retain the 2030 priority. The 2023-24 industrial-action cycle added locum travel reimbursement and NEPTS rebooking. NEPTS is delivered via Yorkshire Ambulance Service under West Yorkshire ICB framework. Frozen HMRC AMAP rates (45p/25p since 2011) compress the staff-mileage element in real terms. April 2025 NIC step-up flows indirectly via contractor pass-through.",
        "sources": [
            {"publisher": "Airedale NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.airedale-trust.nhs.uk/about-us/publications/"},
            {"publisher": "Health Services Safety Investigations Body", "title": "RAAC in NHS estates", "url": "https://www.hssib.org.uk/"},
            {"publisher": "Department of Health and Social Care", "title": "New Hospital Programme — Reset January 2025", "url": "https://www.gov.uk/government/publications/new-hospital-programme-update"},
            {"publisher": "NHS England", "title": "Non-Emergency Patient Transport Services Review", "url": "https://www.england.nhs.uk/publication/non-emergency-patient-transport-services-review/"},
            {"publisher": "Care Quality Commission", "title": "Airedale NHS Foundation Trust provider profile (RCF)", "url": "https://www.cqc.org.uk/provider/RCF"}
        ],
        "related": ["Airedale NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "New Hospital Programme", "Yorkshire Ambulance Service NHS Trust", "West Yorkshire Integrated Care Board"]
    },
    "Amortisation — Walsall Healthcare NHS Trust": {
        "aliases": [{"name": "Amortisation", "parent": "Walsall Healthcare NHS Trust"}],
        "description": "Walsall Healthcare NHS Trust's £0.963M amortisation line covers IAS 38 amortisation of capitalised intangible assets — chiefly the trust's EPR platform and associated digital-imaging, e-prescribing and Frontline Digitisation modules deployed at the Manor Hospital (Walsall) and community footprint, plus capitalised software licences for pathology, radiology and back-office systems. The trust operates within an evolving group arrangement with the Royal Wolverhampton NHS Trust under a Black Country Provider Collaborative integration trajectory. Black Country ICS context.",
        "beneficiaries": "c. 4,800 WTE staff serving a c. 285,000 Walsall borough catchment plus borders flow into Wolverhampton, Cannock and Sutton Coldfield; c. 100,000 ED attendances/yr at Manor Hospital ED; c. 65,000 admissions/yr; c. 360,000 outpatient attendances/yr; high-deprivation Black Country urban catchment with elevated coronary, respiratory and diabetes demand.",
        "legal_basis": "IAS 38 Intangible Assets — DHSC Group Accounting Manual 2024-25 chapter 5 — IFRS 3 Business Combinations (acquired-software treatment) — NHS Act 2006 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£0.963M"},
            {"label": "Trust scale", "value": "Manor Hospital (Walsall) + community footprint; c. 4,800 WTE"},
            {"label": "Principal intangibles", "value": "EPR platform + digital imaging (PACS/RIS) + e-prescribing + pathology LIMS + back-office software"},
            {"label": "Group arrangement", "value": "Group / collaborative arrangement with Royal Wolverhampton NHS Trust under Black Country Provider Collaborative — shared digital architecture under exploration"},
            {"label": "EPR platform", "value": "Frontline Digitisation participant — EPR upgrade pathway driving capitalised module additions"},
            {"label": "Useful economic life", "value": "Software typically 5-10 years per GAM; PACS image storage ~10 years; major EPR modules amortised over 7-10 yrs"},
            {"label": "Frontline Digitisation pipeline", "value": "Continued capitalised module additions (clinical noting, mobile apps, decision-support) feed forward intangibles balance"},
            {"label": "Funding trajectory", "value": "2021-22 c. £0.7M → 2023-24 c. £0.9M → 2024-25 £0.963M — Frontline Digitisation module additions"},
            {"label": "Black Country ICS", "value": "Member of Black Country ICB; collaborative pathology partnership and shared digital ambitions across RWT/Walsall/SWBH/Dudley"},
            {"label": "Delivery body", "value": "Trust IT + Finance + EPR vendor + Frontline Digitisation programme team + Black Country Pathology Services partnership"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + NHSE Frontline Digitisation + DHSC + Black Country ICB"},
            {"label": "Evaluation evidence", "value": "NAO Digital Transformation in NHS reports; Trust ARA 2023-24 intangibles note; CQC RBK inspections; DHSC GAM compliance"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-Frontline-Digitisation baseline · Successor: Frontline Digitisation Wave 4-5 module deployment + Black Country Provider Collaborative shared-EPR direction"}
        ],
        "notes": "Walsall Healthcare NHS Trust's amortisation line is dominated by capitalised digital-platform intangibles under IAS 38 — Frontline Digitisation module additions (clinical noting, mobile apps, decision-support) feed forward additions to the intangibles balance, with the typical 5-10 year useful-economic-life envelope per DHSC GAM. The trust's evolving group arrangement with Royal Wolverhampton NHS Trust under the Black Country Provider Collaborative is the strategic frame for digital architecture decisions; shared-EPR ambitions across RWT/Walsall/SWBH/Dudley remain under exploration. Capitalised pathology LIMS sits alongside the Black Country Pathology Services partnership. The Manor Hospital site has historic structural-engineering scrutiny (not RAAC-listed in 2023 HSSIB) but ongoing estates renewal feeds capitalised digital infrastructure.",
        "sources": [
            {"publisher": "Walsall Healthcare NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.walsallhealthcare.nhs.uk/about-us/publications-policies/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 chapter 5 (intangibles)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/frontline-digitisation/"},
            {"publisher": "Care Quality Commission", "title": "Walsall Healthcare NHS Trust provider profile (RBK)", "url": "https://www.cqc.org.uk/provider/RBK"},
            {"publisher": "National Audit Office", "title": "Digital transformation in the NHS", "url": "https://www.nao.org.uk/reports/digital-transformation-in-the-nhs/"}
        ],
        "related": ["Walsall Healthcare NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Frontline Digitisation", "Royal Wolverhampton NHS Trust", "Black Country Integrated Care Board"]
    },
    "General supplies & services — Southport And Ormskirk Hospital NHS Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "Southport And Ormskirk Hospital NHS Trust"}],
        "description": "Southport and Ormskirk Hospital NHS Trust's £0.947M general supplies & services line covers GAM operating expenses for non-medical consumables — stationery, cleaning supplies, laundry, food/catering supplies, hardware, gardening, signage and minor consumables across Southport and Formby District General Hospital and Ormskirk District General Hospital. The trust is in the middle of a structural reconfiguration: from 1 July 2024 acute services at Ormskirk transferred to Liverpool University Hospitals NHS FT (women's/children's/T&O) under a long-planned divisional transfer, with the Trust now repositioning its remaining footprint.",
        "beneficiaries": "c. 3,400 WTE staff serving a c. 250,000 Sefton + West Lancashire catchment (Southport, Formby, Ormskirk, Skelmersdale); c. 90,000 ED attendances/yr (Southport ED + Ormskirk paediatric urgent care pre-2024); c. 50,000 admissions/yr; cross-ICB-border footprint (Cheshire & Merseyside ICB + Lancashire & South Cumbria ICB).",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 — IAS 1 Presentation of Financial Statements — IAS 2 Inventories (interaction) — NHS Act 2006 — Health and Care Act 2022",
        "key_stats": [
            {"label": "General supplies & services 2024-25", "value": "£0.947M"},
            {"label": "Trust scale", "value": "Southport & Formby DGH + Ormskirk DGH (until 1 Jul 2024 service transfer); c. 3,400 WTE"},
            {"label": "Composition", "value": "Stationery + cleaning supplies + laundry + food/catering supplies + hardware + gardening + signage + minor consumables"},
            {"label": "Service transfer 1 Jul 2024", "value": "Acute women's, children's and T&O services at Ormskirk transferred to Liverpool University Hospitals NHS FT — reduces ongoing supplies footprint at Ormskirk"},
            {"label": "NHS Supply Chain", "value": "Primary procurement route for non-clinical consumables — Cheshire & Merseyside ICB collaborative procurement framework"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove cancellation rebooking + non-clinical consumables variability"},
            {"label": "Inflation pass-through", "value": "Catering + cleaning + laundry consumables exposed to food + chemical CPI; FY24 sticky inflation drives elevated unit cost"},
            {"label": "April 2025 NIC step-up", "value": "Indirect via supplier + outsourced FM cost pass-through (15% over £5k threshold)"},
            {"label": "Funding trajectory", "value": "2021-22 c. £0.8M → 2023-24 c. £0.9M → 2024-25 £0.947M — CPI on consumables; Ormskirk service-transfer effect from 2024-25 partial year"},
            {"label": "Cheshire & Merseyside ICS", "value": "Member of Cheshire & Merseyside ICB (Southport site) and Lancashire & South Cumbria ICB (Ormskirk site)"},
            {"label": "Delivery body", "value": "Trust Procurement + Estates & Facilities + NHS Supply Chain + Liverpool University Hospitals NHS FT (post-transfer Ormskirk shared services)"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + NHS Supply Chain + DHSC + Cheshire & Merseyside ICB + Lancashire & South Cumbria ICB"},
            {"label": "Evaluation evidence", "value": "NHS Supply Chain category-management benchmarks; Carter Lord review legacy on non-pay; Trust ARA 2023-24; CQC RVY inspections"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2024 full Southport+Ormskirk acute footprint · Successor: post-1-Jul-2024 reconfigured trust profile + ongoing strategic-future review"}
        ],
        "notes": "Southport and Ormskirk Hospital NHS Trust's general supplies & services line reflects a trust in mid-reconfiguration — from 1 July 2024 acute women's, children's and trauma & orthopaedic services at Ormskirk transferred to Liverpool University Hospitals NHS FT under a long-planned divisional rationalisation across the Cheshire & Merseyside / Lancashire & South Cumbria ICB border, reducing the ongoing supplies footprint at Ormskirk. NHS Supply Chain is the primary procurement route, with Cheshire & Merseyside ICB collaborative frameworks active. The 2023-24 industrial-action cycle (44 days junior-doctor + 10 days consultant strikes) added cancellation-rebooking and non-clinical consumables variability. Sticky FY24 food + chemical CPI elevates catering, cleaning and laundry consumables unit cost. April 2025 employer NIC step-up (15% over £5k) flows indirectly via outsourced FM and supplier pass-through. The trust's strategic future remains under regional review.",
        "sources": [
            {"publisher": "Southport And Ormskirk Hospital NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.southportandormskirk.nhs.uk/about-us/publications/"},
            {"publisher": "NHS Supply Chain", "title": "Category management — non-clinical consumables", "url": "https://www.supplychain.nhs.uk/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Southport And Ormskirk Hospital NHS Trust provider profile (RVY)", "url": "https://www.cqc.org.uk/provider/RVY"},
            {"publisher": "Liverpool University Hospitals NHS Foundation Trust", "title": "Service transfer from Ormskirk — programme update", "url": "https://www.liverpoolft.nhs.uk/"}
        ],
        "related": ["Southport And Ormskirk Hospital NHS Trust", "Clinical Supplies & Drugs", "NHS Acute Trusts", "Liverpool University Hospitals NHS Foundation Trust", "NHS Supply Chain", "Cheshire and Merseyside Integrated Care Board"]
    },
    "Business rates — George Eliot Hospital NHS Trust": {
        "aliases": [{"name": "Business rates", "parent": "George Eliot Hospital NHS Trust"}],
        "description": "George Eliot Hospital NHS Trust's £0.944M business-rates line covers non-domestic rate liability on the George Eliot Hospital site (Nuneaton, Warwickshire) plus a small Eliot Hospice / Charles Hayward outpatient footprint. The Valuation Office Agency assesses rateable values (2023 list effective 1 April 2023) and Nuneaton & Bedworth Borough Council bills as the local billing authority. NHS trusts pay the full multiplier with no charitable 80% relief, making the line sensitive to the 2023 revaluation, transitional uplifts and the Non-Domestic Rating (Multipliers and Private Finance) Act 2024.",
        "beneficiaries": "c. 2,000 WTE staff serving a c. 300,000 north Warwickshire + south Leicestershire catchment (Nuneaton, Bedworth, North Warwickshire, Hinckley, Atherstone); c. 75,000 ED attendances/yr; c. 45,000 admissions/yr; c. 280,000 outpatient attendances/yr; small DGH with structural reconfiguration history.",
        "legal_basis": "Local Government Finance Act 1988 (Schedule 6) — Non-Domestic Rating (Multipliers and Private Finance) Act 2024 — Non-Domestic Rating Act 2023 — Valuation Office Agency 2023 rating list — DHSC Group Accounting Manual 2024-25 — NHS Act 2006",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£0.944M"},
            {"label": "Trust scale", "value": "George Eliot Hospital (Nuneaton); c. 2,000 WTE; small DGH"},
            {"label": "Principal hereditament", "value": "George Eliot Hospital (Nuneaton) — single principal acute hereditament; rateable value likely below £500k threshold (small DGH tier)"},
            {"label": "Billing authority", "value": "Nuneaton and Bedworth Borough Council"},
            {"label": "Rating list", "value": "VOA 2023 list (effective 1 April 2023); next revaluation 1 April 2026"},
            {"label": "Multiplier 2024-25", "value": "Standard non-domestic multiplier per LGFA 1988 Sch 6 (54.6p, 2024-25 England)"},
            {"label": "Charitable relief", "value": "NHS trusts not eligible for mandatory 80% charitable rate relief — full liability borne"},
            {"label": "Funding trajectory", "value": "2021-22 c. £0.8M → 2023-24 c. £0.9M → 2024-25 £0.944M — 2023 list revaluation + transitional uplift"},
            {"label": "Coventry & Warwickshire ICS", "value": "Member of Coventry & Warwickshire ICB; close strategic relationship with UHCW NHS Trust"},
            {"label": "Foundation Group context", "value": "Trust historically explored merger/group with UHCW; current strategic configuration under continuing review"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + Finance + Valuation Office Agency + Nuneaton and Bedworth Borough Council"},
            {"label": "Policy owner", "value": "MHCLG (rates policy + multiplier) + VOA (valuations) + DHSC + NHSE Provider Finance + Coventry & Warwickshire ICB"},
            {"label": "Evaluation evidence", "value": "VOA rating-list publications; NAO local government finance reports; Trust ARA 2023-24 disclosure; CQC RLT inspections"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2017 VOA rating list · Successor: 2026 VOA revaluation + ongoing strategic configuration review with UHCW / South Warwickshire / Coventry & Warwickshire ICB"}
        ],
        "notes": "George Eliot Hospital NHS Trust's business-rates line reflects a single small-DGH hereditament in Nuneaton, with rateable value likely below the £500k threshold introduced by the NDR (Multipliers and Private Finance) Act 2024 — meaning the higher multiplier from April 2025 is unlikely to apply. NHS trusts are not eligible for mandatory 80% charitable rate relief — a structural full-liability disparity vs hospice and charity providers operating adjacent estate. The trust has a history of strategic reconfiguration discussions with UHCW NHS Trust and South Warwickshire NHS FT under the Coventry & Warwickshire ICB; outcomes shape the medium-term hereditament profile. The 1 April 2026 next VOA revaluation is the headline lever. April 2025 employer NIC step-up flows indirectly via FM and consumables supplier pass-through.",
        "sources": [
            {"publisher": "George Eliot Hospital NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.geh.nhs.uk/about-us/our-publications/"},
            {"publisher": "Valuation Office Agency", "title": "Find a business rates valuation (rating list)", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "Department for Levelling Up, Housing and Communities", "title": "Business rates: Non-Domestic Rating Act 2023 + 2024 Multipliers Act", "url": "https://www.gov.uk/government/collections/business-rates"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "George Eliot Hospital NHS Trust provider profile (RLT)", "url": "https://www.cqc.org.uk/provider/RLT"}
        ],
        "related": ["George Eliot Hospital NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Valuation Office Agency", "University Hospitals Coventry and Warwickshire NHS Trust", "Coventry and Warwickshire Integrated Care Board"]
    },
    "Business rates — West Suffolk NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "West Suffolk NHS Foundation Trust"}],
        "description": "West Suffolk NHS FT's £0.942M business-rates line covers non-domestic rate liability on West Suffolk Hospital (Bury St Edmunds) plus the Newmarket Community Hospital footprint. Rateable values are set by the VOA on the 2023 list (effective 1 April 2023) with West Suffolk Council and West Suffolk Borough Council acting as billing authorities. The Bury St Edmunds main site is a designated RAAC critical-mitigation hospital on the 2023 HSSIB list with full rebuild planned under the New Hospital Programme cohort, structurally shaping medium-term hereditament composition.",
        "beneficiaries": "c. 4,500 WTE staff serving a c. 280,000 West Suffolk + Thetford catchment (Bury St Edmunds, Newmarket, Sudbury, Haverhill, Thetford); c. 90,000 ED attendances/yr; c. 55,000 admissions/yr; c. 320,000 outpatient attendances/yr; rural East of England DGH catchment with significant elderly and racing-industry workforce demographic (Newmarket).",
        "legal_basis": "Local Government Finance Act 1988 (Schedule 6) — Non-Domestic Rating (Multipliers and Private Finance) Act 2024 — Non-Domestic Rating Act 2023 — Valuation Office Agency 2023 rating list — DHSC Group Accounting Manual 2024-25 — NHS Act 2006",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£0.942M"},
            {"label": "Trust scale", "value": "West Suffolk Hospital (Bury St Edmunds) + Newmarket Community Hospital; c. 4,500 WTE"},
            {"label": "Principal hereditaments", "value": "West Suffolk Hospital (Bury St Edmunds) — main acute hereditament; rateable value likely £500k+ tier"},
            {"label": "RAAC priority + NHP", "value": "West Suffolk Hospital is a 2023 HSSIB RAAC critical-mitigation hospital; full NHP rebuild planned, NHP Reset Jan 2025 confirmed RAAC trusts retain 2030 priority"},
            {"label": "Billing authorities", "value": "West Suffolk Council (Bury St Edmunds) + West Suffolk Council (Newmarket)"},
            {"label": "Rating list", "value": "VOA 2023 list (effective 1 April 2023); next revaluation 1 April 2026"},
            {"label": "Multiplier 2024-25", "value": "Standard non-domestic multiplier per LGFA 1988 Sch 6 + NDR (Multipliers and Private Finance) Act 2024 higher tier on £500k+ from April 2025"},
            {"label": "Charitable relief", "value": "NHS trusts not eligible for mandatory 80% charitable rate relief — full liability borne"},
            {"label": "Funding trajectory", "value": "2021-22 c. £0.8M → 2023-24 c. £0.9M → 2024-25 £0.942M — 2023 list revaluation + transitional uplift; medium-term: NHP rebuild changes hereditament"},
            {"label": "Suffolk & North East Essex ICS", "value": "Member of Suffolk & North East Essex ICB"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + Finance + Valuation Office Agency + West Suffolk Council"},
            {"label": "Policy owner", "value": "MHCLG (rates policy + multiplier) + VOA (valuations) + DHSC + NHSE Provider Finance + SNEE ICB + NHP team"},
            {"label": "Evaluation evidence", "value": "VOA rating-list publications; HSSIB RAAC site-list 2023; NHP Reset Jan 2025 update; Trust ARA 2023-24 disclosure; CQC RGR inspections"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2017 VOA rating list · Successor: 2026 VOA revaluation + NHP rebuild substituting RAAC-affected hereditament"}
        ],
        "notes": "West Suffolk NHS FT's business-rates line is shaped by the trust's RAAC exposure — West Suffolk Hospital (Bury St Edmunds) is on the 2023 HSSIB critical-mitigation list with a full New Hospital Programme rebuild planned; NHP Reset (January 2025) confirmed RAAC trusts retain the 2030 priority. The current rateable hereditament is structurally on the £500k+ tier potentially attracting the NDR (Multipliers and Private Finance) Act 2024 higher multiplier from April 2025, while the future NHP rebuild will substitute a new hereditament with revised VOA assessment. NHS trusts are not eligible for mandatory 80% charitable rate relief — a structural full-liability disparity. The trust has historic governance scrutiny (2019 'witch hunt' whistleblowing controversy) but this is unrelated to the rates line. April 2025 employer NIC step-up flows indirectly via FM supplier pass-through.",
        "sources": [
            {"publisher": "West Suffolk NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.wsh.nhs.uk/About-us/Trust-Documents/Annual-Reports-and-Accounts.aspx"},
            {"publisher": "Valuation Office Agency", "title": "Find a business rates valuation (rating list)", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "Health Services Safety Investigations Body", "title": "RAAC in NHS estates", "url": "https://www.hssib.org.uk/"},
            {"publisher": "Department of Health and Social Care", "title": "New Hospital Programme — Reset January 2025", "url": "https://www.gov.uk/government/publications/new-hospital-programme-update"},
            {"publisher": "Care Quality Commission", "title": "West Suffolk NHS Foundation Trust provider profile (RGR)", "url": "https://www.cqc.org.uk/provider/RGR"}
        ],
        "related": ["West Suffolk NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Lease expenditure — West Suffolk NHS Foundation Trust", "New Hospital Programme", "Valuation Office Agency"]
    },
    "Business rates — The Princess Alexandra Hospital NHS Trust": {
        "aliases": [{"name": "Business rates", "parent": "The Princess Alexandra Hospital NHS Trust"}],
        "description": "Princess Alexandra Hospital NHS Trust's £0.942M business-rates line covers non-domestic rate liability on the Princess Alexandra Hospital site (Hamstel Road, Harlow) plus the trust's outpatient/community footprint at St Margaret's Hospital (Epping) and Herts and Essex Hospital (Bishop's Stortford). Rateable values are set by the VOA on the 2023 list with Harlow District Council, Epping Forest District Council and East Hertfordshire District Council acting as billing authorities. Princess Alexandra is in the New Hospital Programme cohort (RAAC + estate condition).",
        "beneficiaries": "c. 3,800 WTE staff serving a c. 350,000 west Essex + east Hertfordshire catchment (Harlow, Epping Forest, Uttlesford, East Herts, Hertford, Sawbridgeworth, Bishop's Stortford); c. 95,000 ED attendances/yr; c. 60,000 admissions/yr; c. 320,000 outpatient attendances/yr; cross-ICB-border footprint (Hertfordshire & West Essex ICB).",
        "legal_basis": "Local Government Finance Act 1988 (Schedule 6) — Non-Domestic Rating (Multipliers and Private Finance) Act 2024 — Non-Domestic Rating Act 2023 — Valuation Office Agency 2023 rating list — DHSC Group Accounting Manual 2024-25 — NHS Act 2006",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£0.942M"},
            {"label": "Trust scale", "value": "Princess Alexandra Hospital (Harlow) + St Margaret's (Epping) + Herts & Essex (Bishop's Stortford); c. 3,800 WTE"},
            {"label": "Principal hereditament", "value": "Princess Alexandra Hospital (Harlow) — main acute hereditament; rateable value likely £500k+ tier"},
            {"label": "NHP cohort + RAAC", "value": "Trust on RAAC mitigation + NHP cohort — full rebuild on planned schedule; NHP Reset Jan 2025 confirmed RAAC trusts retain 2030 priority"},
            {"label": "Billing authorities", "value": "Harlow District Council (PAH) + Epping Forest DC (St Margaret's) + East Hertfordshire DC (Herts & Essex)"},
            {"label": "Rating list", "value": "VOA 2023 list (effective 1 April 2023); next revaluation 1 April 2026"},
            {"label": "Multiplier 2024-25", "value": "Standard non-domestic multiplier per LGFA 1988 Sch 6 + NDR (Multipliers and Private Finance) Act 2024 higher tier on £500k+ from April 2025"},
            {"label": "Charitable relief", "value": "NHS trusts not eligible for mandatory 80% charitable rate relief — full liability borne"},
            {"label": "Funding trajectory", "value": "2021-22 c. £0.8M → 2023-24 c. £0.9M → 2024-25 £0.942M — 2023 list revaluation + transitional uplift"},
            {"label": "Hertfordshire & West Essex ICS", "value": "Member of HWE ICB; collaborative procurement and estate strategy"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + Finance + Valuation Office Agency + Harlow DC / Epping Forest DC / East Herts DC"},
            {"label": "Policy owner", "value": "MHCLG (rates policy + multiplier) + VOA (valuations) + DHSC + NHSE Provider Finance + HWE ICB + NHP team"},
            {"label": "Evaluation evidence", "value": "VOA rating-list publications; HSSIB RAAC site-list 2023; NHP Reset Jan 2025 update; Trust ARA 2023-24; CQC RQW inspections"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2017 VOA rating list · Successor: 2026 VOA revaluation + NHP rebuild new hereditament"}
        ],
        "notes": "Princess Alexandra Hospital NHS Trust's business-rates line is shaped by the trust's RAAC exposure and New Hospital Programme cohort membership — the existing Harlow site has known structural and estate-condition issues that drove inclusion in the NHP rebuild cohort, with NHP Reset (January 2025) confirming RAAC trusts retain the 2030 priority. The current Harlow hereditament likely sits in the £500k+ tier attracting the NDR (Multipliers and Private Finance) Act 2024 higher multiplier from April 2025, while the future NHP rebuild will substitute a new hereditament. NHS trusts pay full liability with no charitable relief. The 1 April 2026 next VOA revaluation is the headline lever. The trust faces material tension between current-estate rates exposure and timing of the NHP replacement build. April 2025 employer NIC step-up flows indirectly via FM supplier pass-through.",
        "sources": [
            {"publisher": "The Princess Alexandra Hospital NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.pah.nhs.uk/about-us/our-publications/"},
            {"publisher": "Valuation Office Agency", "title": "Find a business rates valuation (rating list)", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "Department of Health and Social Care", "title": "New Hospital Programme — Reset January 2025", "url": "https://www.gov.uk/government/publications/new-hospital-programme-update"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "The Princess Alexandra Hospital NHS Trust provider profile (RQW)", "url": "https://www.cqc.org.uk/provider/RQW"}
        ],
        "related": ["The Princess Alexandra Hospital NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "New Hospital Programme", "Hertfordshire and West Essex Integrated Care Board", "Valuation Office Agency"]
    },
    "Transport (business + patient) — The Dudley Group NHS Foundation Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "The Dudley Group NHS Foundation Trust"}],
        "description": "The Dudley Group NHS FT's £0.933M transport line covers staff business mileage (AfC Section 17 + HMRC AMAP), pool-fleet leases (IFRS 16 right-of-use), inter-site courier and pathology specimen transport between Russells Hall Hospital (Dudley) and partner sites (Corbett Outpatient Centre, Guest Outpatient Centre, Dudley Group community footprint), plus contracted non-emergency patient transport (NEPTS) for the Dudley borough catchment. Russells Hall is PFI-financed (Summit Healthcare), with Engie/Equans the FM successor following Carillion 2018 collapse novation.",
        "beneficiaries": "c. 4,800 WTE staff serving a c. 320,000 Dudley metropolitan borough catchment (Dudley, Stourbridge, Halesowen, Brierley Hill, Kingswinford, Sedgley); c. 105,000 ED attendances/yr at Russells Hall ED; c. 70,000 admissions/yr; c. 380,000 outpatient attendances/yr; high-deprivation Black Country catchment.",
        "legal_basis": "NHS Act 2006 — NHS England Patient Transport Services Eligibility Criteria — Agenda for Change Section 17 + HMRC AMAP rates — IFRS 16 Leases (pool fleet) — DHSC Group Accounting Manual 2024-25 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£0.933M"},
            {"label": "Trust scale", "value": "Russells Hall (Dudley) + Corbett + Guest + community footprint; c. 4,800 WTE"},
            {"label": "Composition", "value": "Staff business mileage (AfC Sec 17 + AMAP) + pool fleet (IFRS 16) + inter-site pathology courier + contracted NEPTS"},
            {"label": "PFI overlap", "value": "Russells Hall is PFI-financed (Summit Healthcare Project Co); FM = Equans (post-Carillion novation 2018) — pool fleet + transport partly under FM service line"},
            {"label": "NEPTS provider", "value": "West Midlands Ambulance Service University NHS FT / commissioned via Black Country ICB framework"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove locum travel reimbursement + NEPTS rebooking spike"},
            {"label": "April 2025 NIC step-up", "value": "Indirect via NEPTS contractor + agency-driver + Equans FM pass-through (15% over £5k threshold)"},
            {"label": "AMAP rates 2024-25", "value": "HMRC AMAP unchanged at 45p/mile first 10,000 + 25p thereafter — frozen since 2011"},
            {"label": "Funding trajectory", "value": "2021-22 c. £0.7M → 2023-24 c. £0.9M → 2024-25 £0.933M — strike backfill + fuel-cost pass-through + NEPTS uplift"},
            {"label": "Black Country ICS", "value": "Member of Black Country ICB; collaborative NEPTS commissioning"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + Pathology + Transport Office + Equans (FM contractor) + WMAS (NEPTS)"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + NHSE Patient Transport Services policy + DHSC + Black Country ICB"},
            {"label": "Evaluation evidence", "value": "NHSE NEPTS Review 2021; NAO PFI reports; Trust ARA 2023-24; CQC RNA inspections"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-Carillion-collapse FM baseline (pre-Jan 2018) · Successor: NEPTS-Review-aligned eligibility implementation + Black Country shared-fleet consolidation"}
        ],
        "notes": "The Dudley Group NHS FT's transport line is shaped by the Russells Hall PFI structure (Summit Healthcare Project Co; FM novated to Equans following Carillion's January 2018 collapse) — pool-fleet and transport activity is partly delivered through the FM contract, with cost-pass-through subject to the PFI unitary-charge mechanism. The 2023-24 industrial-action cycle (44 days junior-doctor + 10 days consultant strikes) added locum travel reimbursement and NEPTS rebooking. NEPTS is delivered by West Midlands Ambulance Service under Black Country ICB framework. HMRC's frozen AMAP rates (45p/25p since 2011) compress the staff-mileage element in real terms. April 2025 employer NIC step-up flows indirectly via Equans FM contractor and NEPTS provider pass-through. Dudley sits in a high-deprivation Black Country catchment with elevated travel demand.",
        "sources": [
            {"publisher": "The Dudley Group NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.dgft.nhs.uk/about-us/publications/"},
            {"publisher": "NHS England", "title": "Non-Emergency Patient Transport Services Review", "url": "https://www.england.nhs.uk/publication/non-emergency-patient-transport-services-review/"},
            {"publisher": "HMRC", "title": "Approved Mileage Allowance Payments (AMAP) rates", "url": "https://www.gov.uk/government/publications/rates-and-allowances-travel-mileage-and-fuel-allowances"},
            {"publisher": "National Audit Office", "title": "Investigation into the government's handling of the collapse of Carillion", "url": "https://www.nao.org.uk/reports/investigation-into-the-governments-handling-of-the-collapse-of-carillion/"},
            {"publisher": "Care Quality Commission", "title": "The Dudley Group NHS Foundation Trust provider profile (RNA)", "url": "https://www.cqc.org.uk/provider/RNA"}
        ],
        "related": ["The Dudley Group NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Black Country Integrated Care Board", "West Midlands Ambulance Service University NHS Foundation Trust", "Carillion plc"]
    },
    "Business rates — Medway NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "Medway NHS Foundation Trust"}],
        "description": "Medway NHS FT's £0.923M business-rates line covers non-domestic rate liability on the Medway Maritime Hospital site (Gillingham, Kent) plus the trust's outpatient and community footprint. Rateable values are set by the VOA on the 2023 list (effective 1 April 2023) with Medway Council acting as the unitary billing authority. NHS trusts pay the full multiplier with no charitable 80% relief. Medway is in a long programme of estate renewal under the New Hospital Programme cohort prior to the January 2025 NHP Reset which deferred non-RAAC builds.",
        "beneficiaries": "c. 4,800 WTE staff serving a c. 460,000 Medway Towns + Swale catchment (Gillingham, Chatham, Rochester, Strood, Sittingbourne, Sheerness, Faversham); c. 130,000 ED attendances/yr — historically among the busiest EDs per WTE in England; c. 80,000 admissions/yr; c. 480,000 outpatient attendances/yr; high-deprivation urban Kent catchment.",
        "legal_basis": "Local Government Finance Act 1988 (Schedule 6) — Non-Domestic Rating (Multipliers and Private Finance) Act 2024 — Non-Domestic Rating Act 2023 — Valuation Office Agency 2023 rating list — DHSC Group Accounting Manual 2024-25 — NHS Act 2006",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£0.923M"},
            {"label": "Trust scale", "value": "Medway Maritime Hospital (Gillingham); c. 4,800 WTE; one of the busiest EDs in England"},
            {"label": "Principal hereditament", "value": "Medway Maritime Hospital — main acute hereditament; rateable value likely £500k+ tier"},
            {"label": "NHP cohort context", "value": "Trust in the wider NHP cohort under previous schedule; NHP Reset Jan 2025 deferred non-RAAC builds — Medway estate renewal trajectory revised"},
            {"label": "Billing authority", "value": "Medway Council (unitary authority)"},
            {"label": "Rating list", "value": "VOA 2023 list (effective 1 April 2023); next revaluation 1 April 2026"},
            {"label": "Multiplier 2024-25", "value": "Standard non-domestic multiplier per LGFA 1988 Sch 6 + NDR (Multipliers and Private Finance) Act 2024 higher tier on £500k+ from April 2025"},
            {"label": "Charitable relief", "value": "NHS trusts not eligible for mandatory 80% charitable rate relief — full liability borne"},
            {"label": "Funding trajectory", "value": "2021-22 c. £0.8M → 2023-24 c. £0.9M → 2024-25 £0.923M — 2023 list revaluation + transitional uplift"},
            {"label": "Kent & Medway ICS", "value": "Member of Kent & Medway ICB; close working with East Kent Hospitals University NHS FT and Dartford & Gravesham NHS Trust"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + Finance + Valuation Office Agency + Medway Council"},
            {"label": "Policy owner", "value": "MHCLG (rates policy + multiplier) + VOA (valuations) + DHSC + NHSE Provider Finance + Kent & Medway ICB"},
            {"label": "Evaluation evidence", "value": "VOA rating-list publications; NAO local government finance reports; Trust ARA 2023-24 disclosure; CQC RPA inspections"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2017 VOA rating list · Successor: 2026 VOA revaluation + post-NHP-Reset estate-renewal trajectory"}
        ],
        "notes": "Medway NHS FT's business-rates line reflects a single principal hereditament at Medway Maritime Hospital (Gillingham), likely sitting in the £500k+ tier attracting the NDR (Multipliers and Private Finance) Act 2024 higher multiplier from April 2025. NHS trusts pay full liability with no charitable relief. The NHP Reset (January 2025) deferred non-RAAC builds, revising Medway's estate-renewal trajectory and pushing back the timing of any hereditament substitution. Medway emerged from extended financial special-measures (lifted 2017) and quality special-measures (lifted 2018) — non-pay running-cost discipline carries forward. The 1 April 2026 next VOA revaluation is the headline lever. April 2025 employer NIC step-up flows indirectly via FM and consumables supplier pass-through.",
        "sources": [
            {"publisher": "Medway NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.medway.nhs.uk/about-us/our-publications/"},
            {"publisher": "Valuation Office Agency", "title": "Find a business rates valuation (rating list)", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "Department of Health and Social Care", "title": "New Hospital Programme — Reset January 2025", "url": "https://www.gov.uk/government/publications/new-hospital-programme-update"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Medway NHS Foundation Trust provider profile (RPA)", "url": "https://www.cqc.org.uk/provider/RPA"}
        ],
        "related": ["Medway NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Kent and Medway Integrated Care Board", "Valuation Office Agency", "New Hospital Programme"]
    },
    "Transport (business + patient) — North Tees and Hartlepool NHS Foundation Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "North Tees and Hartlepool NHS Foundation Trust"}],
        "description": "North Tees and Hartlepool NHS FT's £0.910M transport line covers staff business mileage (AfC Section 17 + HMRC AMAP), pool-fleet leases (IFRS 16 right-of-use), inter-site courier and pathology specimen transport between the University Hospital of North Tees (Stockton) and the University Hospital of Hartlepool, plus contracted non-emergency patient transport (NEPTS). The trust's twin-DGH split-site geography between Stockton and Hartlepool drives a structural inter-site courier and patient-shuttle premium; the trust is in the New Hospital Programme cohort with a planned new build to consolidate.",
        "beneficiaries": "c. 5,500 WTE staff serving a c. 400,000 Stockton-on-Tees + Hartlepool + East Durham catchment (Stockton, Billingham, Hartlepool, Peterlee, Wynyard); c. 130,000 ED attendances/yr at North Tees ED (Hartlepool ED downgraded to UTC 2011); c. 70,000 admissions/yr; c. 380,000 outpatient attendances/yr.",
        "legal_basis": "NHS Act 2006 — NHS England Patient Transport Services Eligibility Criteria — Agenda for Change Section 17 + HMRC AMAP rates — IFRS 16 Leases (pool fleet) — DHSC Group Accounting Manual 2024-25 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£0.910M"},
            {"label": "Trust scale", "value": "University Hospital of North Tees (Stockton) + University Hospital of Hartlepool; c. 5,500 WTE"},
            {"label": "Composition", "value": "Staff business mileage (AfC Sec 17 + AMAP) + pool fleet (IFRS 16) + inter-site pathology/courier + contracted NEPTS + Stockton↔Hartlepool patient-shuttle"},
            {"label": "Twin-site premium", "value": "Stockton ↔ Hartlepool inter-site flow (c. 11 miles) drives structural pathology courier + staff travel premium vs single-site DGHs"},
            {"label": "NHP cohort", "value": "Trust in NHP cohort with planned new build at Wynyard / Stockton site to consolidate; NHP Reset Jan 2025 deferred non-RAAC trusts — North Tees timing revised"},
            {"label": "NEPTS provider", "value": "North East Ambulance Service NHS FT / commissioned via NENC ICB framework"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove locum travel reimbursement + NEPTS rebooking spike"},
            {"label": "April 2025 NIC step-up", "value": "Indirect via NEPTS contractor + agency-driver pass-through (15% over £5k threshold)"},
            {"label": "AMAP rates 2024-25", "value": "HMRC AMAP unchanged at 45p/mile first 10,000 + 25p thereafter — frozen since 2011"},
            {"label": "Funding trajectory", "value": "2021-22 c. £0.7M → 2023-24 c. £0.9M → 2024-25 £0.910M — strike backfill + fuel-cost pass-through + NEPTS uplift"},
            {"label": "NENC ICS", "value": "Member of North East and North Cumbria ICB — largest ICS by area in England"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + Pathology + Transport Office + NEAS (NEPTS)"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + NHSE NEPTS policy + DHSC + NENC ICB"},
            {"label": "Evaluation evidence", "value": "NHSE NEPTS Review 2021; NHP Reset Jan 2025 update; Trust ARA 2023-24; CQC RVW inspections"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-NEPTS-Review-2021 baseline · Successor: NHP single-site consolidation removing twin-site courier premium (timing revised by Reset)"}
        ],
        "notes": "North Tees and Hartlepool NHS FT's transport line is shaped by the trust's twin-DGH split-site geography — University Hospital of North Tees (Stockton) and University Hospital of Hartlepool, c. 11 miles apart — which drives a structural inter-site pathology courier and staff travel premium relative to single-site DGHs. The trust is in the New Hospital Programme cohort with a planned consolidated new build (Wynyard/Stockton vicinity) that would eliminate the twin-site premium; NHP Reset (January 2025) deferred non-RAAC builds, revising the timing. Hartlepool ED was downgraded to a UTC in 2011, with most acute activity now at North Tees. The 2023-24 industrial-action cycle added locum travel reimbursement and NEPTS rebooking. NEPTS is delivered by NEAS under NENC ICB framework. April 2025 NIC step-up flows via contractor pass-through.",
        "sources": [
            {"publisher": "North Tees and Hartlepool NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.nth.nhs.uk/about-us/our-publications/"},
            {"publisher": "NHS England", "title": "Non-Emergency Patient Transport Services Review", "url": "https://www.england.nhs.uk/publication/non-emergency-patient-transport-services-review/"},
            {"publisher": "Department of Health and Social Care", "title": "New Hospital Programme — Reset January 2025", "url": "https://www.gov.uk/government/publications/new-hospital-programme-update"},
            {"publisher": "HMRC", "title": "Approved Mileage Allowance Payments (AMAP) rates", "url": "https://www.gov.uk/government/publications/rates-and-allowances-travel-mileage-and-fuel-allowances"},
            {"publisher": "Care Quality Commission", "title": "North Tees and Hartlepool NHS Foundation Trust provider profile (RVW)", "url": "https://www.cqc.org.uk/provider/RVW"}
        ],
        "related": ["North Tees and Hartlepool NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "New Hospital Programme", "North East Ambulance Service NHS Foundation Trust", "North East and North Cumbria Integrated Care Board"]
    },
    "Amortisation — Warrington and Halton Teaching Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Amortisation", "parent": "Warrington and Halton Teaching Hospitals NHS Foundation Trust"}],
        "description": "Warrington and Halton Teaching Hospitals NHS FT's £0.904M amortisation line covers IAS 38 amortisation of capitalised intangible assets — chiefly the trust's EPR and digital-imaging platform plus Frontline Digitisation modules deployed across Warrington Hospital (Lovely Lane) and Halton General Hospital (Runcorn), plus capitalised software licences for pathology, radiology and back-office systems. The trust acquired teaching status in 2022 and is part of the Cheshire & Merseyside ICB digital architecture programme.",
        "beneficiaries": "c. 4,000 WTE staff serving a c. 330,000 Warrington + Halton catchment (Warrington, Runcorn, Widnes, Lymm); c. 110,000 ED attendances/yr at Warrington ED + Halton UTC; c. 60,000 admissions/yr; c. 320,000 outpatient attendances/yr; teaching trust with Cheshire & Merseyside ICB pathology partnership.",
        "legal_basis": "IAS 38 Intangible Assets — DHSC Group Accounting Manual 2024-25 chapter 5 — IFRS 3 Business Combinations (acquired-software treatment) — NHS Act 2006 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£0.904M"},
            {"label": "Trust scale", "value": "Warrington Hospital (Lovely Lane) + Halton General (Runcorn); c. 4,000 WTE; teaching trust (designation 2022)"},
            {"label": "Principal intangibles", "value": "EPR platform + digital imaging (PACS/RIS) + e-prescribing + pathology LIMS + back-office software"},
            {"label": "EPR platform", "value": "Frontline Digitisation participant — EPR upgrade pathway driving capitalised module additions"},
            {"label": "Useful economic life", "value": "Software typically 5-10 years per GAM; PACS image storage ~10 years; major EPR modules amortised over 7-10 yrs"},
            {"label": "Frontline Digitisation pipeline", "value": "Continued capitalised module additions (clinical noting, mobile apps, decision-support) feed forward intangibles balance"},
            {"label": "Teaching status (2022)", "value": "Trust designated teaching trust 2022 — strengthens academic-software capitalisation case (research informatics, simulation tools)"},
            {"label": "Funding trajectory", "value": "2021-22 c. £0.6M → 2023-24 c. £0.85M → 2024-25 £0.904M — Frontline Digitisation module additions"},
            {"label": "Cheshire & Merseyside ICS", "value": "Member of Cheshire & Merseyside ICB; pathology + EPR collaborative partnership across LUHFT, MWL, WHHC, COCH"},
            {"label": "NHP Halton 'Hospital Without Walls'", "value": "Halton in NHP cohort under previous schedule; NHP Reset Jan 2025 deferred non-RAAC builds — affects future capitalised digital infrastructure timing"},
            {"label": "Delivery body", "value": "Trust IT + Finance + EPR vendor + Frontline Digitisation programme team + Cheshire & Merseyside ICB digital team"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + NHSE Frontline Digitisation + DHSC + Cheshire & Merseyside ICB"},
            {"label": "Evaluation evidence", "value": "NAO Digital Transformation in NHS reports; Trust ARA 2023-24 intangibles note; CQC RWW inspections; DHSC GAM compliance"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-Frontline-Digitisation baseline · Successor: Frontline Digitisation Wave 4-5 module deployment + Halton 'Hospital Without Walls' rebuild (post-Reset timing)"}
        ],
        "notes": "Warrington and Halton Teaching Hospitals NHS FT's amortisation line is dominated by capitalised digital-platform intangibles under IAS 38 — Frontline Digitisation module additions (clinical noting, mobile apps, decision-support) feed forward additions to the intangibles balance, with the typical 5-10 year useful-economic-life envelope per DHSC GAM. The trust's 2022 teaching designation strengthens the case for research-informatics and simulation-tool capitalisation. Halton General was in the New Hospital Programme cohort under the previous schedule with a 'Hospital Without Walls' design concept; NHP Reset (January 2025) deferred non-RAAC builds, revising the timing for replacement capitalised digital infrastructure. The Cheshire & Merseyside ICB digital architecture programme drives shared-pathology LIMS and EPR collaboration with Liverpool University Hospitals NHS FT, Mersey & West Lancs and Countess of Chester. April 2025 employer NIC step-up flows indirectly via vendor pass-through.",
        "sources": [
            {"publisher": "Warrington and Halton Teaching Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.whh.nhs.uk/about-us/publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 chapter 5 (intangibles)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/frontline-digitisation/"},
            {"publisher": "Care Quality Commission", "title": "Warrington and Halton Teaching Hospitals NHS Foundation Trust provider profile (RWW)", "url": "https://www.cqc.org.uk/provider/RWW"},
            {"publisher": "National Audit Office", "title": "Digital transformation in the NHS", "url": "https://www.nao.org.uk/reports/digital-transformation-in-the-nhs/"}
        ],
        "related": ["Warrington and Halton Teaching Hospitals NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Frontline Digitisation", "Cheshire and Merseyside Integrated Care Board", "New Hospital Programme"]
    },
    "Amortisation — Wrightington, Wigan and Leigh NHS Foundation Trust": {
        "aliases": [{"name": "Amortisation", "parent": "Wrightington, Wigan and Leigh NHS Foundation Trust"}],
        "description": "Wrightington, Wigan and Leigh NHS FT's £0.896M amortisation line covers IAS 38 amortisation of capitalised intangible assets — chiefly the trust's EPR platform and digital-imaging modules deployed across the Royal Albert Edward Infirmary (Wigan), Wrightington Hospital (Appley Bridge — internationally recognised orthopaedic centre) and Leigh Infirmary, plus Frontline Digitisation modules and capitalised software for pathology, radiology and back-office systems. The Wrightington orthopaedic specialty drives bespoke clinical-software capitalisation for prosthetics planning and outcome registries.",
        "beneficiaries": "c. 5,200 WTE staff serving a c. 320,000 Wigan + Leigh metropolitan borough catchment plus a national/international tertiary orthopaedic referral footprint at Wrightington (one of the world's leading hip/knee centres, Sir John Charnley legacy); c. 110,000 ED attendances/yr at Wigan ED; c. 70,000 admissions/yr; c. 360,000 outpatient attendances/yr.",
        "legal_basis": "IAS 38 Intangible Assets — DHSC Group Accounting Manual 2024-25 chapter 5 — IFRS 3 Business Combinations (acquired-software treatment) — NHS Act 2006 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£0.896M"},
            {"label": "Trust scale", "value": "Royal Albert Edward Infirmary (Wigan) + Wrightington (Appley Bridge) + Leigh Infirmary; c. 5,200 WTE; tertiary orthopaedic centre"},
            {"label": "Principal intangibles", "value": "EPR platform + digital imaging (PACS/RIS) + e-prescribing + pathology LIMS + bespoke orthopaedic-planning software + back-office software"},
            {"label": "Wrightington specialty", "value": "World-renowned hip/knee centre (Sir John Charnley legacy) — drives bespoke clinical-software capitalisation (prosthetics planning, NJR data feeds, outcome registries)"},
            {"label": "EPR platform", "value": "Frontline Digitisation participant — EPR upgrade pathway driving capitalised module additions"},
            {"label": "Useful economic life", "value": "Software typically 5-10 years per GAM; PACS image storage ~10 years; major EPR modules amortised over 7-10 yrs"},
            {"label": "Frontline Digitisation pipeline", "value": "Continued capitalised module additions (clinical noting, mobile apps, decision-support) feed forward intangibles balance"},
            {"label": "Funding trajectory", "value": "2021-22 c. £0.7M → 2023-24 c. £0.85M → 2024-25 £0.896M — Frontline Digitisation module additions + orthopaedic-software refresh"},
            {"label": "Greater Manchester ICS", "value": "Member of Greater Manchester ICB — large devolved-health system; collaborative pathology and EPR ambitions"},
            {"label": "National Joint Registry", "value": "Wrightington feeds NJR data — informatics integration drives capitalised software interfaces"},
            {"label": "Delivery body", "value": "Trust IT + Finance + EPR vendor + Frontline Digitisation programme team + GM Provider Collaborative digital team"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + NHSE Frontline Digitisation + DHSC + GM ICB"},
            {"label": "Evaluation evidence", "value": "NAO Digital Transformation in NHS reports; Trust ARA 2023-24 intangibles note; CQC RRF inspections; National Joint Registry data quality reports"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-Frontline-Digitisation baseline · Successor: Frontline Digitisation Wave 4-5 module deployment + GM Provider Collaborative shared-EPR direction"}
        ],
        "notes": "Wrightington, Wigan and Leigh NHS FT's amortisation line is dominated by capitalised digital-platform intangibles under IAS 38, with a distinctive specialist tilt driven by Wrightington's world-renowned orthopaedic centre — home of the Sir John Charnley hip-replacement legacy and a major National Joint Registry data feeder, requiring bespoke prosthetics-planning, outcome-registry and informatics-integration software that sits alongside the standard EPR/PACS/LIMS portfolio. Frontline Digitisation module additions feed forward intangibles balance under typical 5-10 year useful-economic-life conventions per DHSC GAM. Greater Manchester ICB collaborative pathology and EPR ambitions shape future architecture decisions across the GM Provider Collaborative. April 2025 employer NIC step-up flows indirectly via vendor pass-through.",
        "sources": [
            {"publisher": "Wrightington, Wigan and Leigh NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.wwl.nhs.uk/our-publications"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 chapter 5 (intangibles)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/frontline-digitisation/"},
            {"publisher": "National Joint Registry", "title": "Annual report — hip, knee, ankle, elbow, shoulder", "url": "https://www.njrcentre.org.uk/"},
            {"publisher": "Care Quality Commission", "title": "Wrightington, Wigan and Leigh NHS Foundation Trust provider profile (RRF)", "url": "https://www.cqc.org.uk/provider/RRF"}
        ],
        "related": ["Wrightington, Wigan and Leigh NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Frontline Digitisation", "National Joint Registry", "Greater Manchester Integrated Care Board"]
    },
    "Transport (business + patient) — Sherwood Forest Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "Sherwood Forest Hospitals NHS Foundation Trust"}],
        "description": "Sherwood Forest Hospitals NHS FT's £0.894M transport line covers staff business mileage (AfC Section 17 + HMRC AMAP), pool-fleet leases (IFRS 16 right-of-use), inter-site courier and pathology specimen transport between King's Mill Hospital (Sutton-in-Ashfield), Newark Hospital and Mansfield Community Hospital, plus contracted non-emergency patient transport (NEPTS) for the Mid Nottinghamshire catchment. King's Mill is one of England's largest PFI hospitals (Project Co — Healthcare Support Services), with Engie/Equans the FM successor following Carillion 2018 collapse novation.",
        "beneficiaries": "c. 5,200 WTE staff serving a c. 425,000 Mid Nottinghamshire catchment (Mansfield, Ashfield, Newark, Sherwood, Bassetlaw borders); c. 130,000 ED attendances/yr at King's Mill ED + Newark UTC; c. 75,000 admissions/yr; c. 380,000 outpatient attendances/yr; high-deprivation post-coalfield catchment.",
        "legal_basis": "NHS Act 2006 — NHS England Patient Transport Services Eligibility Criteria — Agenda for Change Section 17 + HMRC AMAP rates — IFRS 16 Leases (pool fleet) — DHSC Group Accounting Manual 2024-25 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£0.894M"},
            {"label": "Trust scale", "value": "King's Mill Hospital (Sutton-in-Ashfield) + Newark Hospital + Mansfield Community Hospital; c. 5,200 WTE"},
            {"label": "Composition", "value": "Staff business mileage (AfC Sec 17 + AMAP) + pool fleet (IFRS 16) + inter-site pathology/courier + contracted NEPTS"},
            {"label": "PFI overlap", "value": "King's Mill = one of England's largest PFI hospitals (HSS Project Co); FM = Equans (post-Carillion novation 2018) — pool-fleet/transport partly under FM contract"},
            {"label": "PFI / LIFT charges 2024-25", "value": "£27.75M (parent line context — Sherwood is a PFI-heavy trust shaping operating-cost mix)"},
            {"label": "NEPTS provider", "value": "East Midlands Ambulance Service NHS Trust (EMAS) — commissioned via Nottingham & Nottinghamshire ICB framework"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove locum travel reimbursement + NEPTS rebooking spike"},
            {"label": "April 2025 NIC step-up", "value": "Indirect via NEPTS contractor + Equans FM pass-through (15% over £5k threshold)"},
            {"label": "AMAP rates 2024-25", "value": "HMRC AMAP unchanged at 45p/mile first 10,000 + 25p thereafter — frozen since 2011"},
            {"label": "Funding trajectory", "value": "2021-22 c. £0.7M → 2023-24 c. £0.85M → 2024-25 £0.894M — strike backfill + fuel-cost pass-through + NEPTS uplift"},
            {"label": "Nottingham & Nottinghamshire ICS", "value": "Member of Nottingham & Nottinghamshire ICB; collaborative NEPTS commissioning with NUH"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + Pathology + Transport Office + Equans (FM via PFI) + EMAS (NEPTS)"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + NHSE NEPTS policy + DHSC + Nottingham & Nottinghamshire ICB"},
            {"label": "Evaluation evidence", "value": "NHSE NEPTS Review 2021; NAO PFI reports; Trust ARA 2023-24; CQC RK5 inspections"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-Carillion-collapse FM baseline (pre-Jan 2018) · Successor: NEPTS-Review-aligned eligibility implementation + ICB-wide pool-fleet consolidation"}
        ],
        "notes": "Sherwood Forest Hospitals NHS FT's transport line is shaped by the King's Mill PFI structure — one of England's largest hospital PFI deals (Healthcare Support Services Project Co) with FM novated to Equans following Carillion's January 2018 collapse — pool-fleet and transport activity is partly delivered through the FM contract, with cost-pass-through subject to the PFI unitary-charge mechanism. The 2023-24 industrial-action cycle (44 days junior-doctor + 10 days consultant strikes) added locum travel reimbursement and NEPTS rebooking. NEPTS is delivered by EMAS under Nottingham & Nottinghamshire ICB framework. HMRC's frozen AMAP rates (45p/25p since 2011) compress the staff-mileage element in real terms. April 2025 employer NIC step-up flows indirectly via Equans FM and EMAS contractor pass-through. The Mid Nottinghamshire post-coalfield catchment has elevated travel demand for outpatient and tertiary referral flows to NUH.",
        "sources": [
            {"publisher": "Sherwood Forest Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.sfh-tr.nhs.uk/about-us/our-publications"},
            {"publisher": "NHS England", "title": "Non-Emergency Patient Transport Services Review", "url": "https://www.england.nhs.uk/publication/non-emergency-patient-transport-services-review/"},
            {"publisher": "National Audit Office", "title": "Investigation into the government's handling of the collapse of Carillion", "url": "https://www.nao.org.uk/reports/investigation-into-the-governments-handling-of-the-collapse-of-carillion/"},
            {"publisher": "HMRC", "title": "Approved Mileage Allowance Payments (AMAP) rates", "url": "https://www.gov.uk/government/publications/rates-and-allowances-travel-mileage-and-fuel-allowances"},
            {"publisher": "Care Quality Commission", "title": "Sherwood Forest Hospitals NHS Foundation Trust provider profile (RK5)", "url": "https://www.cqc.org.uk/provider/RK5"}
        ],
        "related": ["Sherwood Forest Hospitals NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "PFI / LIFT charges — Sherwood Forest Hospitals NHS Foundation Trust", "East Midlands Ambulance Service NHS Trust", "Carillion plc"]
    },
    "PFI / LIFT charges — East Suffolk and North Essex NHS Foundation Trust": {
        "aliases": [{"name": "PFI / LIFT charges", "parent": "East Suffolk and North Essex NHS Foundation Trust"}],
        "description": "East Suffolk and North Essex NHS FT's £0.874M PFI / LIFT charges line covers the residual NHS LIFT (Local Improvement Finance Trust) unitary-charge element on community-hospital and outpatient infrastructure within the trust footprint, plus any PFI-financed building leases inherited from the predecessor trusts (Ipswich Hospital + Colchester Hospital University) at the July 2018 merger. ESNEFT is one of England's largest acute trusts by site count, formed from the merger of Ipswich Hospital NHS Trust and Colchester Hospital University NHS FT.",
        "beneficiaries": "c. 11,500 WTE staff serving a c. 1.0M east Suffolk + north Essex catchment (Ipswich, Colchester, Felixstowe, Clacton, Harwich, Sudbury, Aldeburgh, Tendring); c. 250,000 ED attendances/yr at Ipswich + Colchester ED; c. 165,000 admissions/yr; c. 1.0M outpatient attendances/yr; cross-ICB-border footprint (Suffolk & North East Essex ICB).",
        "legal_basis": "IFRIC 12 Service Concession Arrangements — IFRS 16 Leases (post-2022 lease elements) — DHSC PFI accounting guidance — DHSC Group Accounting Manual 2024-25 — NHS Act 2006 — Health and Care Act 2022",
        "key_stats": [
            {"label": "PFI / LIFT charges 2024-25", "value": "£0.874M"},
            {"label": "Trust scale", "value": "Ipswich Hospital + Colchester Hospital + Clacton Hospital + Aldeburgh Community Hospital + outreach; c. 11,500 WTE"},
            {"label": "Merger origin", "value": "ESNEFT formed 1 Jul 2018 — Ipswich Hospital NHS Trust + Colchester Hospital University NHS FT — combined PFI/LIFT ledger from that date"},
            {"label": "Composition", "value": "Residual NHS LIFT unitary charge on community/outpatient infrastructure + any inherited PFI building-lease elements + IFRIC 12 service-concession charges"},
            {"label": "LIFT context", "value": "NHS LIFT programme (originated 2000) — public-private vehicle for primary care + community estate; many LIFT contracts mid-life with c. 25-year horizons"},
            {"label": "Carillion novation", "value": "Engie/Equans is FM successor on PFI assets following Carillion 2018 collapse — applicable to legacy Ipswich/Colchester PFI elements"},
            {"label": "Funding trajectory", "value": "Post-merger 2018-19 baseline → declining residual LIFT amortisation → 2024-25 £0.874M (residual tail)"},
            {"label": "PFI policy", "value": "HMT confirmed October 2018 no new PFI/PF2 deals; existing contracts run to scheduled end + handback; HMT centre of excellence supports trusts"},
            {"label": "April 2025 NIC step-up", "value": "Indirect via FM contractor pass-through (15% over £5k threshold)"},
            {"label": "Suffolk & North East Essex ICS", "value": "Member of SNEE ICB — large rural/coastal footprint with Lowestoft + Great Yarmouth interfaces"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + Finance + LIFT Co + FM contractor (Equans/Sodexo etc.) + DHSC PFI Centre of Best Practice"},
            {"label": "Policy owner", "value": "DHSC + HM Treasury (PFI policy) + NHSE Provider Finance + SNEE ICB + Infrastructure & Projects Authority"},
            {"label": "Evaluation evidence", "value": "NAO PFI/PF2 reports; HMT PFI handback guidance; Trust ARA 2023-24 service-concession note; CQC RDE inspections"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2018 separate Ipswich + Colchester PFI/LIFT ledgers · Successor: end-of-life LIFT handback + post-PFI exit estate"}
        ],
        "notes": "ESNEFT's PFI / LIFT charges line is comparatively small at £0.874M, reflecting the trust's relatively low PFI exposure post-merger (1 July 2018, Ipswich Hospital NHS Trust + Colchester Hospital University NHS FT) — the residual is dominated by NHS LIFT unitary charges on community and outpatient infrastructure plus inherited building-lease elements. Engie/Equans is the FM successor on legacy PFI elements following Carillion's January 2018 collapse novation. HMT confirmed in October 2018 no new PFI/PF2 deals; existing contracts run to scheduled end with the HMT/IPA Centre of Best Practice supporting trusts on handback. April 2025 employer NIC step-up flows indirectly via FM contractor pass-through. The trust's main estate-renewal lever now sits outside the PFI/LIFT envelope (post-NHP-Reset estate strategy).",
        "sources": [
            {"publisher": "East Suffolk and North Essex NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.esneft.nhs.uk/about-us/publications/"},
            {"publisher": "HM Treasury", "title": "PFI and PF2 — handback and centre of best practice", "url": "https://www.gov.uk/government/publications/pfi-and-pf2"},
            {"publisher": "National Audit Office", "title": "PFI and PF2 (HC 718, 2018)", "url": "https://www.nao.org.uk/reports/pfi-and-pf2/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (service concessions)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "East Suffolk and North Essex NHS Foundation Trust provider profile (RDE)", "url": "https://www.cqc.org.uk/provider/RDE"}
        ],
        "related": ["East Suffolk and North Essex NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Suffolk and North East Essex Integrated Care Board", "Carillion plc", "HM Treasury"]
    },
    "Inventories written down — Sheffield Teaching Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Inventories written down", "parent": "Sheffield Teaching Hospitals NHS Foundation Trust"}],
        "description": "Sheffield Teaching Hospitals NHS FT's £0.849M inventories written-down line covers IAS 2 inventory write-downs and obsolescence provisions across the trust's substantial pharmacy, theatre, lab consumables and medical-device stockholdings — at the Royal Hallamshire Hospital, Northern General Hospital, Weston Park Cancer Centre, Charles Clifford Dental Hospital and Jessop Wing maternity. As one of England's largest teaching trusts, STH carries an outsized inventory base across high-cost oncology drugs, advanced therapy medicinal products (ATMPs), implantable devices and specialist surgical kits.",
        "beneficiaries": "c. 18,500 WTE staff serving a c. 580,000 Sheffield catchment plus a tertiary referral population of c. 5M for specialist services (cancer at Weston Park, neurosciences, transplantation, advanced therapies, paediatric services via SCH partnership); c. 230,000 ED attendances/yr at Northern General; c. 250,000 admissions/yr; c. 1.5M outpatient attendances/yr.",
        "legal_basis": "IAS 2 Inventories — DHSC Group Accounting Manual 2024-25 — IAS 36 Impairment of Assets (interaction) — NHS Act 2006 — Health and Care Act 2022 — Medicines Act 1968 (expiry rules)",
        "key_stats": [
            {"label": "Inventories written down 2024-25", "value": "£0.849M"},
            {"label": "Trust scale", "value": "Royal Hallamshire + Northern General + Weston Park Cancer + Charles Clifford Dental + Jessop Wing; c. 18,500 WTE — one of England's largest teaching trusts"},
            {"label": "Composition", "value": "Pharmacy expiry write-down + theatre kit obsolescence + lab consumables expiry + implantable device write-down + research/ATMP residuals"},
            {"label": "Weston Park (cancer)", "value": "Tertiary cancer centre — high-value oncology drug stockholding (incl. SACT) drives elevated expiry-write-down profile"},
            {"label": "Advanced Therapies", "value": "ATMP centre (CAR-T, gene therapy partnerships) — extremely high-value individualised products with strict cold-chain and expiry windows"},
            {"label": "NHS Supply Chain", "value": "Primary procurement route for non-pharmacy consumables; cancer/specialty drugs via NHS England Specialised Commissioning"},
            {"label": "FY24 disruption factors", "value": "Industrial action 2023-24 (44 days junior-doctor + 10 days consultant strikes) drove cancellation rebooking + theatre-kit re-allocation + some expiry exposure"},
            {"label": "Pharmacy stewardship", "value": "Trust pharmacy programmes (waste reduction, redistribution within ICB) target reducing the obsolescence ratio (Carter Lord legacy)"},
            {"label": "Funding trajectory", "value": "2021-22 c. £0.6M → 2023-24 c. £0.8M → 2024-25 £0.849M — strike-related theatre disruption + drug-price inflation on high-value oncology stock"},
            {"label": "South Yorkshire ICS", "value": "Member of South Yorkshire ICB; collaborative pathology + pharmacy procurement frameworks"},
            {"label": "Delivery body", "value": "Trust Pharmacy + Procurement + Theatres + Pathology + NHS Supply Chain + NHSE Specialised Commissioning"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + NHSE Specialised Commissioning + DHSC + South Yorkshire ICB + MHRA (medicines)"},
            {"label": "Evaluation evidence", "value": "Carter Lord review on operational productivity (pharmacy waste); Model Hospital pharmacy benchmarks; Trust ARA 2023-24 inventories note; CQC RHQ inspections"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-pandemic obsolescence baseline · Successor: ICB pharmacy redistribution + ATMP stewardship + Frontline Digitisation drug-tracking"}
        ],
        "notes": "Sheffield Teaching Hospitals NHS FT's inventories written-down line reflects the trust's outsized inventory base as one of England's largest teaching trusts — the Weston Park Cancer Centre drives a high-value oncology drug stockholding (Systemic Anti-Cancer Therapy regimens) with strict expiry windows, while ATMP activity (CAR-T, gene therapy partnerships) introduces individualised products with extreme cold-chain and short-window expiry exposure under IAS 2. The 2023-24 industrial-action cycle (44 days junior-doctor + 10 days consultant strikes) added theatre-kit re-allocation and drug-batch expiry exposure. Pharmacy stewardship programmes (waste reduction, ICB redistribution per Carter Lord legacy) target reducing the obsolescence ratio. Drug-price inflation on high-value oncology stock structurally raises the absolute write-down even when the obsolescence rate is stable. South Yorkshire ICB collaborative pharmacy procurement frameworks shape the medium-term trajectory.",
        "sources": [
            {"publisher": "Sheffield Teaching Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.sth.nhs.uk/about-us/who-we-are/publications"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Department of Health", "title": "Operational productivity and performance in English NHS acute hospitals (Lord Carter)", "url": "https://www.gov.uk/government/publications/productivity-in-nhs-hospitals"},
            {"publisher": "NHS England", "title": "Specialised commissioning — cancer drugs and ATMPs", "url": "https://www.england.nhs.uk/commissioning/spec-services/"},
            {"publisher": "Care Quality Commission", "title": "Sheffield Teaching Hospitals NHS Foundation Trust provider profile (RHQ)", "url": "https://www.cqc.org.uk/provider/RHQ"}
        ],
        "related": ["Sheffield Teaching Hospitals NHS Foundation Trust", "Clinical Supplies & Drugs", "NHS Acute Trusts", "Amortisation — Sheffield Teaching Hospitals NHS Foundation Trust", "NHS Supply Chain", "South Yorkshire Integrated Care Board"]
    },
}
