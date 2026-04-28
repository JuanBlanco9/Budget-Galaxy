# -*- coding: utf-8 -*-
# Phase 2 Acute slice 2 — chunk 42 (17 NHS Acute Trust orphan sub-lines)
# Hand-curated trust-specific PROGRAMME-archetype enrichment entries.
# Structural contract per docs/archetype_briefs.md.

NEW = {
    "Lease expenditure — Tameside and Glossop Integrated Care NHS Foundation Trust": {
        "aliases": [{"name": "Lease expenditure", "parent": "Tameside and Glossop Integrated Care NHS Foundation Trust"}],
        "description": "Tameside and Glossop's £0.38M lease-expenditure line covers IFRS 16 right-of-use lease costs (medical equipment, IT hardware, vehicles and small property leases) outside the dominant Tameside General Hospital LIFT estate, brought on-balance-sheet from 2022-23 under DHSC GAM ch.7. The trust runs an integrated acute + community model from the Ashton-under-Lyne site serving Tameside and Glossop (East Cheshire) under Greater Manchester ICS, and uses the GM LIFTCo for community-clinic estate which sits outside this residual lease line.",
        "beneficiaries": "c. 3,300 WTE staff serving a c. 250,000 catchment (Tameside, Glossop, parts of east Manchester); c. 90,000 ED attendances/yr at Tameside General ED; c. 35,000 admissions/yr; integrated community-services footprint across Tameside MBC + High Peak (Glossop).",
        "legal_basis": "IFRS 16 Leases — DHSC Group Accounting Manual 2024-25 ch.7 — Landlord and Tenant Act 1954 — NHS Act 2006 — Health and Care Act 2022 — NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "Lease expenditure 2024-25", "value": "£0.38M"},
            {"label": "Trust scale", "value": "Tameside General Hospital (Ashton-under-Lyne) + community-clinic footprint; c. 3,300 WTE; integrated acute + community"},
            {"label": "Composition", "value": "Residual operating leases — medical equipment, IT hardware, fleet vehicles, small property leases (post-IFRS 16 right-of-use)"},
            {"label": "IFRS 16 jump 2022-23", "value": "On-balance-sheet right-of-use assets recognised — depreciation now sits in main premises lines; residual op-lease here is short-term + low-value exemption"},
            {"label": "GM LIFTCo context", "value": "Tameside community estate served under Greater Manchester LIFTCo (Equitix-led) — sits in PFI/LIFT line, not lease"},
            {"label": "Industrial action 2023-24 effect", "value": "Junior-doctor 44 days + consultant strikes drove short-term equipment-rental top-ups for backfill rotas"},
            {"label": "April 2025 NIC + CPI", "value": "Lease cashflows largely fixed via contracts; IT-equipment rentals exposed to CPI re-indexation"},
            {"label": "Funding trajectory", "value": "2021-22 (pre-IFRS 16) c. £1.5M → 2022-23 IFRS 16 reclassification → 2024-25 £0.38M residual"},
            {"label": "Delivery body", "value": "Trust E&F + Procurement + IT + (NHS Supply Chain framework for medical equipment leases)"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Greater Manchester ICB"},
            {"label": "Evaluation evidence", "value": "Model Hospital estates/leasing benchmark; CQC RMP inspections; NAO LIFT review; Trust ARA 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-IFRS 16 op-lease accounting · Successor: continued IFRS 16 perimeter normalisation + GM ICS shared-services lease pooling"}
        ],
        "notes": "Tameside and Glossop's residual lease-expenditure line reflects the post-IFRS 16 (2022-23) accounting reset that pulled most material leases on-balance-sheet — what remains here is short-term + low-value-exemption op-leases (medical equipment, IT hardware, fleet) outside the LIFT and PFI lines. The trust's integrated acute + community model under Greater Manchester ICS feeds shared-services lease pooling discussions through the GM Provider Collaborative. Industrial action 2023-24 lifted short-term equipment-rental top-ups for backfill rotas, while CPI re-indexation on IT-equipment rental contracts feeds forward into 2025-26. Tameside General sits in the older estate cohort with no current NHP allocation, so lease-driven equipment-replacement remains the recurrent capital substitute.",
        "sources": [
            {"publisher": "Tameside and Glossop Integrated Care NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.tamesidehospital.nhs.uk/about/annual-reports.htm"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "HM Treasury / FRAB", "title": "Application of IFRS 16 Leases in the public sector", "url": "https://www.gov.uk/government/publications/financial-reporting-advisory-board-frab"},
            {"publisher": "Care Quality Commission", "title": "Tameside and Glossop provider profile (RMP)", "url": "https://www.cqc.org.uk/provider/RMP"},
            {"publisher": "National Audit Office", "title": "PFI and PF2 (HC 718, 2018)", "url": "https://www.nao.org.uk/reports/pfi-and-pf2/"}
        ],
        "related": ["Tameside and Glossop Integrated Care NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Lease expenditure — Warrington and Halton Teaching Hospitals NHS Foundation Trust", "PFI / LIFT charges — Sherwood Forest Hospitals NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Lease expenditure — Warrington and Halton Teaching Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Lease expenditure", "parent": "Warrington and Halton Teaching Hospitals NHS Foundation Trust"}],
        "description": "Warrington and Halton's £0.38M lease-expenditure line covers post-IFRS 16 residual operating leases (medical equipment, IT hardware, fleet, small property) across the Warrington Hospital site and Halton Hospital site (Runcorn) serving Warrington & Halton borough councils within Cheshire & Merseyside ICS. The trust holds RAAC-affected estate at Warrington Hospital (HSSIB September 2023 list of 27 trusts) — RAAC remediation drives temporary modular-unit and decant-equipment lease spend feeding this residual line.",
        "beneficiaries": "c. 4,400 WTE staff serving a c. 330,000 catchment (Warrington c. 215,000 + Halton c. 130,000); c. 100,000 ED attendances/yr at Warrington Hospital ED; c. 50,000 admissions/yr; two-site footprint (Warrington Hospital DGH + Halton Hospital elective + diagnostics).",
        "legal_basis": "IFRS 16 Leases — DHSC Group Accounting Manual 2024-25 ch.7 — Landlord and Tenant Act 1954 — NHS Act 2006 — Health and Care Act 2022 — Building Safety Act 2022 (RAAC context)",
        "key_stats": [
            {"label": "Lease expenditure 2024-25", "value": "£0.38M"},
            {"label": "Trust scale", "value": "Two-site (Warrington Hospital DGH + Halton Hospital elective/diagnostics, Runcorn); c. 4,400 WTE"},
            {"label": "Composition", "value": "Residual operating leases — medical equipment, IT hardware, fleet, small property (post-IFRS 16 right-of-use)"},
            {"label": "RAAC HSSIB 2023 context", "value": "Warrington Hospital listed Sept 2023 — RAAC remediation drives modular-unit + decant-equipment lease spend in this line"},
            {"label": "NHP cohort + Reset", "value": "Warrington new-build added to NHP cohort 2023 (RAAC-cohort); Jan 2025 Reset rebaselined to later wave"},
            {"label": "IFRS 16 jump 2022-23", "value": "On-balance-sheet right-of-use assets recognised; residual op-lease here is short-term + low-value exemption"},
            {"label": "Industrial action 2023-24 effect", "value": "Junior-doctor 44 days + consultant strikes drove short-term equipment-rental top-ups for backfill rotas"},
            {"label": "April 2025 NIC + CPI", "value": "Lease cashflows largely fixed; IT-equipment + medical-equipment rentals exposed to CPI re-indexation"},
            {"label": "Funding trajectory", "value": "2021-22 (pre-IFRS 16) c. £1.4M → 2022-23 IFRS 16 reclassification → 2024-25 £0.38M residual; RAAC-decant lease pressure"},
            {"label": "Delivery body", "value": "Trust E&F + Procurement + IT + (NHS Supply Chain framework for medical equipment leases) + RAAC-cohort modular-build leasing"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Cheshire & Merseyside ICB + DHSC New Hospital Programme (RAAC cohort)"},
            {"label": "Evaluation evidence", "value": "HSSIB RAAC report; NAO RAAC and the schools/hospital estate report; Model Hospital estates/leasing benchmark; CQC RWW inspections; Trust ARA 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-IFRS 16 op-lease accounting · Successor: NHP RAAC-cohort rebuild + post-Reset deferred new-site lease re-baselining"}
        ],
        "notes": "Warrington and Halton's residual lease-expenditure line carries a particular RAAC-driven pressure — Warrington Hospital sits on the HSSIB September 2023 list of 27 RAAC-affected trusts, so modular-unit decant leasing and temporary medical-equipment leases feed this residual line above peer-trust comparators. The trust was added to the NHP cohort in 2023 under the RAAC programme, but the January 2025 NHP Reset rebaselined the Warrington new-build to a later wave, sustaining the modular-decant lease perimeter for longer. Industrial action 2023-24 drove short-term equipment-rental top-ups; CPI re-indexation on IT and medical-equipment rentals feeds forward into 2025-26.",
        "sources": [
            {"publisher": "Warrington and Halton Teaching Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.whh.nhs.uk/about-us/our-publications"},
            {"publisher": "Health Services Safety Investigations Body", "title": "Reinforced autoclaved aerated concrete (RAAC) in NHS estate", "url": "https://www.hssib.org.uk/"},
            {"publisher": "Department of Health and Social Care", "title": "New Hospital Programme — January 2025 Reset", "url": "https://www.gov.uk/government/publications/new-hospital-programme-plan-for-implementation"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Warrington and Halton provider profile (RWW)", "url": "https://www.cqc.org.uk/provider/RWW"}
        ],
        "related": ["Warrington and Halton Teaching Hospitals NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Lease expenditure — Tameside and Glossop Integrated Care NHS Foundation Trust", "Lease expenditure — Torbay and South Devon NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Inventories written down — Worcestershire Acute Hospitals NHS Trust": {
        "aliases": [{"name": "Inventories written down", "parent": "Worcestershire Acute Hospitals NHS Trust"}],
        "description": "Worcestershire Acute's £0.38M inventories-written-down line covers stock obsolescence and write-downs of clinical consumables, drugs, theatre supplies and implants across the Worcestershire Royal Hospital, Alexandra Hospital (Redditch) and Kidderminster Treatment Centre footprint serving Worcestershire ICS. The trust runs a long-running PFI on Worcestershire Royal (Catalyst Healthcare 2002-2032) and has been under recurrent NHSE financial-improvement scrutiny — drug expiry write-downs (especially high-cost specialty + paediatric drugs at Worcestershire Royal) and short-dated theatre consumables dominate the line.",
        "beneficiaries": "c. 5,500 WTE staff serving a c. 600,000 Worcestershire catchment; c. 165,000 ED attendances/yr (Worcestershire Royal + Alexandra Redditch); c. 75,000 admissions/yr; three-site footprint (Worcestershire Royal Worcester + Alexandra Redditch + Kidderminster Treatment Centre).",
        "legal_basis": "IAS 2 Inventories — DHSC Group Accounting Manual 2024-25 — NHS Act 2006 — Human Medicines Regulations 2012 — Health and Care Act 2022 — NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "Inventories written down 2024-25", "value": "£0.38M"},
            {"label": "Trust scale", "value": "Three-site (Worcestershire Royal Hospital + Alexandra Hospital Redditch + Kidderminster Treatment Centre); c. 5,500 WTE"},
            {"label": "Composition", "value": "Drug expiry (high-cost specialty + paediatric) + short-dated theatre consumables + obsolete implants + ward-stock obsolescence"},
            {"label": "PFI estate context", "value": "Worcestershire Royal Hospital PFI (Catalyst Healthcare, 2002-2032) — single-site stock-management dynamic shapes write-downs"},
            {"label": "NHSE scrutiny context", "value": "Recurrent NHSE financial-improvement intervention — stock-loss minimisation a recurring CIP target"},
            {"label": "Drug shortages context", "value": "DHSC SSP regime + ongoing UK drug-shortage notices drive emergency stock + expiry risk"},
            {"label": "April 2025 NIC + drug-tariff", "value": "Drug-tariff and CPI uplifts re-price stock baseline; expiry write-downs sensitive to demand-volume volatility"},
            {"label": "Funding trajectory", "value": "2021-22 c. £0.45M → 2023-24 c. £0.36M → 2024-25 £0.38M — sustained at low base via stock controls"},
            {"label": "Delivery body", "value": "Trust Procurement + Pharmacy + Theatres + (NHS Supply Chain Drugs/Theatre framework) + Drug & Therapeutics Committee"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC Medicines + NHS Supply Chain + Herefordshire & Worcestershire ICB"},
            {"label": "Evaluation evidence", "value": "Model Hospital pharmacy/inventory benchmark; CQC RWP inspections; NHSE Financial Improvement Trajectory; NAO inventory-management review; Trust ARA 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-Scan4Safety + pre-EPR stock-tracking baseline · Successor: GS1 Scan4Safety + EPR-integrated pharmacy + Frontline Digitisation stock-control"}
        ],
        "notes": "Worcestershire Acute's inventories-written-down line sits within recurrent NHSE financial-improvement scrutiny — stock-loss minimisation has been a perennial CIP target and the trust has invested in GS1 Scan4Safety and EPR-pharmacy integration to bring write-downs under tighter control. The Worcestershire Royal PFI (Catalyst Healthcare 2002-2032) shapes stock-management on the dominant single site, while drug-shortage notices and DHSC Serious Shortage Protocols feed emergency-buy + expiry exposure. Industrial action 2023-24 drove cancellation-rebooking which can lift theatre-consumable expiry. Drug-tariff and CPI uplifts re-price the stock baseline forward.",
        "sources": [
            {"publisher": "Worcestershire Acute Hospitals NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.worcsacute.nhs.uk/about-us/our-publications/annual-report"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Scan4Safety / GS1 adoption programme", "url": "https://www.scan4safety.nhs.uk/"},
            {"publisher": "Care Quality Commission", "title": "Worcestershire Acute provider profile (RWP)", "url": "https://www.cqc.org.uk/provider/RWP"},
            {"publisher": "National Audit Office", "title": "Investigation into NHS supply of personal protective equipment / inventory management", "url": "https://www.nao.org.uk/reports/investigation-into-government-procurement-during-the-covid-19-pandemic/"}
        ],
        "related": ["Worcestershire Acute Hospitals NHS Trust", "Clinical Supplies & Drugs", "NHS Acute Trusts", "Inventories written down — South Tyneside and Sunderland NHS Foundation Trust", "Inventories written down — Chelsea and Westminster Hospital NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Business rates — Queen Elizabeth Hospital King's Lynn NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "Queen Elizabeth Hospital King's Lynn NHS Foundation Trust"}],
        "description": "Queen Elizabeth King's Lynn's £0.37M business-rates line covers non-domestic rates (NDR) levied on the Queen Elizabeth Hospital King's Lynn site under the Local Government Finance Act 1988 and the 2024 NDR multipliers, paid through Borough Council of King's Lynn & West Norfolk to MHCLG. The trust is a designated RAAC-affected hospital (HSSIB September 2023 list — one of the most extensively RAAC-affected acute estates in England) and was confirmed in the New Hospital Programme 2025 Reset cohort for full rebuild — RAAC failsafe propping and decant modular blocks reshape the rateable estate footprint.",
        "beneficiaries": "c. 4,000 WTE staff serving a c. 350,000 catchment (West Norfolk + parts of Cambridgeshire Fenland + Lincolnshire South Holland); c. 80,000 ED attendances/yr at Queen Elizabeth ED (single-site DGH); c. 40,000 admissions/yr; severe RAAC-failsafe footprint with decant modular accommodation.",
        "legal_basis": "Local Government Finance Act 1988 (Schedule 6) — Non-Domestic Rating (Multipliers and Private Finance) Act 2024 — Building Safety Act 2022 (RAAC context) — NHS Act 2006 — Health and Care Act 2022 — DHSC Group Accounting Manual 2024-25",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£0.37M"},
            {"label": "Trust scale", "value": "Single-site DGH (Queen Elizabeth Hospital King's Lynn); c. 4,000 WTE"},
            {"label": "Composition", "value": "Non-Domestic Rates on hospital site + ancillary parking + plant rooms, billed by King's Lynn & West Norfolk Borough Council"},
            {"label": "RAAC HSSIB 2023 status", "value": "One of seven most extensively RAAC-affected hospitals — c. 13,000 props installed; reshapes rateable footprint via modular decant blocks"},
            {"label": "NHP 2025 Reset", "value": "Confirmed RAAC priority rebuild cohort — full new hospital target c. 2030; modular decant continues through 2025-30"},
            {"label": "NDR multiplier 2024-25", "value": "51.2p (large-property multiplier); transitional relief via 2024 Act + healthcare-specific MHCLG arrangements"},
            {"label": "Charitable rates relief", "value": "NHS trusts not eligible for full charitable 80% relief (R(NHS) Trusts charitable status excluded by case law) — pay full NDR"},
            {"label": "April 2025 multiplier uprating", "value": "CPI September-22 link sustains material multiplier rise; partial freeze for retail / hospitality not applied to NHS"},
            {"label": "Funding trajectory", "value": "2021-22 c. £0.30M → 2023-24 c. £0.35M → 2024-25 £0.37M — multiplier + RAAC-modular footprint uplift"},
            {"label": "Delivery body", "value": "King's Lynn & West Norfolk Borough Council (billing) + VOA (rateable-value) + Trust E&F (rate-mitigation appeals)"},
            {"label": "Policy owner", "value": "MHCLG (NDR policy) + DHSC + NHSE Provider Finance + Norfolk & Waveney ICB"},
            {"label": "Evaluation evidence", "value": "HSSIB RAAC report; NAO RAAC report; IPA Major Projects Report (NHP); Model Hospital estates benchmark; CQC RCX inspections; Trust ARA 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2023 stable rateable footprint · Successor: NHP rebuild new-site VOA-rebaseline post-2030; transitional decant-modular rateable additions"}
        ],
        "notes": "Queen Elizabeth King's Lynn carries a particularly distinctive rates dynamic — the trust is one of the seven worst RAAC-affected hospitals in England (c. 13,000 failsafe props installed) and was confirmed for full NHP rebuild under the January 2025 Reset, with priority status given the structural-risk profile. Decant modular accommodation added to the site since 2023 has reshaped the rateable footprint, lifting the line above pre-RAAC baseline. NHS trusts pay full NDR (no charitable 80% relief applies via case-law exclusion), so the September-22 CPI-linked multiplier uplift feeds directly through. NAO/HSSIB reports drive the rebuild urgency. King's Lynn & West Norfolk Borough Council bills directly; VOA rebases on substantial site change.",
        "sources": [
            {"publisher": "Queen Elizabeth Hospital King's Lynn NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.qehkl.nhs.uk/AnnualReports.asp"},
            {"publisher": "Health Services Safety Investigations Body", "title": "Reinforced autoclaved aerated concrete (RAAC) in NHS estate", "url": "https://www.hssib.org.uk/"},
            {"publisher": "Department of Health and Social Care", "title": "New Hospital Programme — January 2025 Reset", "url": "https://www.gov.uk/government/publications/new-hospital-programme-plan-for-implementation"},
            {"publisher": "Valuation Office Agency", "title": "How non-domestic property is valued", "url": "https://www.gov.uk/guidance/how-non-domestic-properties-are-valued"},
            {"publisher": "Care Quality Commission", "title": "Queen Elizabeth King's Lynn provider profile (RCX)", "url": "https://www.cqc.org.uk/provider/RCX"}
        ],
        "related": ["Queen Elizabeth Hospital King's Lynn NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Business rates — Southport And Ormskirk Hospital NHS Trust", "New Hospital Programme", "Department of Health and Social Care"]
    },
    "Transport (business + patient) — University Hospitals Plymouth NHS Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "University Hospitals Plymouth NHS Trust"}],
        "description": "University Hospitals Plymouth's £0.37M transport line covers business mileage (AfC Section 17 + AMAP), pool-fleet IFRS 16 lease costs, non-emergency patient transport service (NEPTS) cross-charges and patient travel reimbursements across the Derriford Hospital footprint serving Plymouth, South-West Devon and East Cornwall. Derriford is the major trauma centre and tertiary acute hub for the South West Peninsula — long patient travel distances (Cornwall, Devon, Isles of Scilly) feed elevated NEPTS pass-through and air-ambulance interface costs.",
        "beneficiaries": "c. 9,500 WTE staff serving a c. 450,000 Plymouth catchment + tertiary South West Peninsula referral; c. 130,000 ED attendances/yr at Derriford ED (regional Major Trauma Centre); c. 90,000 admissions/yr; single-site Derriford Hospital + community-clinic outreach.",
        "legal_basis": "NHS Act 2006 — NHSE Patient Transport Services Eligibility Criteria — Agenda for Change Section 17 (business mileage) — HMRC AMAP rates — IFRS 16 Leases (pool fleet) — DHSC Group Accounting Manual 2024-25 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£0.37M"},
            {"label": "Trust scale", "value": "Single-site Derriford Hospital (regional Major Trauma Centre + tertiary specialty); c. 9,500 WTE"},
            {"label": "South West Peninsula tertiary catchment", "value": "Tertiary referrals from Cornwall, Devon, Isles of Scilly — long patient-travel distances drive NEPTS + air-ambulance interface"},
            {"label": "NEPTS commissioning", "value": "Devon ICB lead-commissioner NEPTS contract — outsourced operator delivery (E-zec Medical historically)"},
            {"label": "Composition", "value": "Business mileage (AfC S17 + AMAP 45p/25p) + pool-fleet IFRS 16 leases + NEPTS pass-through + patient travel reimbursements + Cornwall Air Ambulance interface"},
            {"label": "AMAP rate context", "value": "HMRC AMAP rate frozen at 45p/mile (first 10k miles) since 2011 — real-terms erosion lifts NHS-internal mileage rate disputes"},
            {"label": "Industrial action 2023-24 effect", "value": "Junior-doctor 44 days + consultant strikes drove agency travel-claim spikes + cancellation rebooking transport"},
            {"label": "April 2025 NIC + fuel CPI", "value": "Indirect via NEPTS contractor pass-through + diesel CPI feed forward unit-cost pressure"},
            {"label": "Funding trajectory", "value": "2021-22 c. £0.30M → 2023-24 c. £0.34M → 2024-25 £0.37M — fuel CPI + NEPTS contract uplift"},
            {"label": "Delivery body", "value": "Trust E&F + outsourced NEPTS provider (Devon ICB lead-commissioner) + pool-fleet leasing partner + Trust HR (mileage)"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + NHSE Urgent and Emergency Care (NEPTS) + Devon ICB + DHSC"},
            {"label": "Evaluation evidence", "value": "NHSE NEPTS Eligibility Review 2021; CQC RK9 inspections; NAO South West tertiary acute review; Trust ARA 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-ICS CCG-commissioned NEPTS contracts · Successor: Devon ICS NEPTS retender + Peninsula tertiary-network transport-flow optimisation"}
        ],
        "notes": "University Hospitals Plymouth's transport line carries an elevated geographic-distance premium given Derriford's role as the South West Peninsula's regional Major Trauma Centre and tertiary specialty hub — long patient journeys from Cornwall, Devon and Isles of Scilly feed NEPTS pass-through and the Cornwall Air Ambulance interface. NEPTS is commissioned via Devon ICB lead-commissioner arrangement (E-zec Medical historically), with eligibility tightened under NHSE's 2021 criteria refresh. Industrial action 2023-24 drove cancellation-rebooking and agency-travel claims, while fuel CPI feed-through and the HMRC AMAP-rate freeze (45p/mile since 2011) sustain forward-cost pressure. The trust runs a Peninsula Acute Sustainability Programme with Royal Cornwall Hospitals shaping cross-trust transport flows.",
        "sources": [
            {"publisher": "University Hospitals Plymouth NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.plymouthhospitals.nhs.uk/annual-reports"},
            {"publisher": "NHS England", "title": "Non-Emergency Patient Transport Services — National Framework + Eligibility Criteria 2021", "url": "https://www.england.nhs.uk/publication/non-emergency-patient-transport-services-nepts/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "University Hospitals Plymouth provider profile (RK9)", "url": "https://www.cqc.org.uk/provider/RK9"},
            {"publisher": "National Audit Office", "title": "NHS England's management of major trauma services", "url": "https://www.nao.org.uk/"}
        ],
        "related": ["University Hospitals Plymouth NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Transport (business + patient) — West Hertfordshire Hospitals NHS Trust", "PFI / LIFT charges — Royal Cornwall Hospitals NHS Trust", "NHS England"]
    },
    "Business rates — Southport And Ormskirk Hospital NHS Trust": {
        "aliases": [{"name": "Business rates", "parent": "Southport And Ormskirk Hospital NHS Trust"}],
        "description": "Southport and Ormskirk's £0.36M business-rates line covers non-domestic rates levied on the Southport and Formby District General Hospital and Ormskirk District General Hospital sites under the Local Government Finance Act 1988 and 2024 NDR multipliers, billed by Sefton MBC (Southport) and West Lancashire BC (Ormskirk) to MHCLG. The trust dissolved on 1 July 2024 with services transferred to Mersey and West Lancashire Teaching Hospitals NHS Trust (formerly St Helens & Knowsley) — this 2024-25 line covers a part-year rates exposure during transition.",
        "beneficiaries": "Pre-dissolution c. 3,500 WTE staff serving a c. 270,000 catchment (Southport + Formby + West Lancashire); c. 90,000 ED attendances/yr at Southport ED + Ormskirk paediatric ED; c. 40,000 admissions/yr; two-site DGH footprint (Southport + Ormskirk) at dissolution.",
        "legal_basis": "Local Government Finance Act 1988 (Schedule 6) — Non-Domestic Rating (Multipliers and Private Finance) Act 2024 — National Health Service (Acquisitions, Mergers and Dissolutions) Regulations — NHS Act 2006 — Health and Care Act 2022 — DHSC Group Accounting Manual 2024-25",
        "key_stats": [
            {"label": "Business rates 2024-25 (part-year)", "value": "£0.36M"},
            {"label": "Trust scale (pre-dissolution)", "value": "Two-site DGH (Southport DGH Sefton + Ormskirk DGH West Lancs); c. 3,500 WTE"},
            {"label": "Dissolution 1 July 2024", "value": "Services transferred to Mersey and West Lancashire Teaching Hospitals NHS Trust under National Health Service (Acquisitions, Mergers and Dissolutions) Regulations"},
            {"label": "Composition", "value": "Non-Domestic Rates on Southport DGH (Sefton MBC) + Ormskirk DGH (West Lancashire BC) — two billing authorities"},
            {"label": "NDR multiplier 2024-25", "value": "51.2p (large-property multiplier); transitional relief via 2024 Act + healthcare-specific MHCLG arrangements"},
            {"label": "Charitable rates relief", "value": "NHS trusts not eligible for full charitable 80% relief — pay full NDR"},
            {"label": "April 2025 multiplier uprating", "value": "Post-dissolution rates fall under MWLTH from July 2024 — successor trust assumes liability + appeals"},
            {"label": "Funding trajectory", "value": "2021-22 c. £0.65M → 2023-24 c. £0.70M → 2024-25 (Apr-Jun part-year) £0.36M — proportional to dissolution date"},
            {"label": "Delivery body", "value": "Sefton MBC + West Lancashire BC (billing) + VOA (rateable-value) + Trust E&F → MWLTH E&F (post-dissolution)"},
            {"label": "Policy owner", "value": "MHCLG (NDR policy) + DHSC + NHSE Provider Finance + Cheshire & Merseyside ICB"},
            {"label": "Evaluation evidence", "value": "NHSE Provider Sustainability assessment driving merger; CQC RVY (legacy) + R0A (MWLTH) inspections; Trust ARA 2023-24 (final); NHSE Recovery Support Programme exit"},
            {"label": "Predecessor / successor", "value": "Predecessor: stand-alone Southport & Ormskirk NHS Trust 2003-2024 · Successor: Mersey and West Lancashire Teaching Hospitals NHS Trust (R0A) from 1 Jul 2024"}
        ],
        "notes": "Southport and Ormskirk's 2024-25 business-rates line covers only the April-June part-year before dissolution on 1 July 2024 under the National Health Service (Acquisitions, Mergers and Dissolutions) Regulations — services transferred to Mersey and West Lancashire Teaching Hospitals NHS Trust (formerly St Helens & Knowsley) following sustained NHSE Recovery Support Programme oversight and provider-sustainability assessment. The two-site footprint straddled two billing authorities (Sefton MBC for Southport, West Lancashire BC for Ormskirk), with VOA rebases pending under successor-trust ownership. NHS trusts pay full NDR (no 80% charitable relief). Post-dissolution rates liability sits with MWLTH from July 2024.",
        "sources": [
            {"publisher": "Southport and Ormskirk Hospital NHS Trust", "title": "Annual Report and Accounts 2023-24 (final)", "url": "https://www.southportandormskirk.nhs.uk/about-us/our-publications"},
            {"publisher": "Mersey and West Lancashire Teaching Hospitals NHS Trust", "title": "Acquisition / dissolution information", "url": "https://www.merseywestlancs.nhs.uk/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Valuation Office Agency", "title": "How non-domestic property is valued", "url": "https://www.gov.uk/guidance/how-non-domestic-properties-are-valued"},
            {"publisher": "Care Quality Commission", "title": "Mersey and West Lancashire Teaching Hospitals provider profile (R0A)", "url": "https://www.cqc.org.uk/provider/R0A"}
        ],
        "related": ["Southport And Ormskirk Hospital NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Business rates — Queen Elizabeth Hospital King's Lynn NHS Foundation Trust", "Mersey and West Lancashire Teaching Hospitals NHS Trust", "Department of Health and Social Care"]
    },
    "Amortisation — East Cheshire NHS Trust": {
        "aliases": [{"name": "Amortisation", "parent": "East Cheshire NHS Trust"}],
        "description": "East Cheshire's £0.35M amortisation line covers the systematic write-down of intangible assets — chiefly capitalised software, EPR / clinical-system deployments and licensed third-party intellectual property — across the Macclesfield District General Hospital site and community-services footprint serving East Cheshire. Under IAS 38 and DHSC GAM ch.5, this line tracks the in-year charge against the cumulative intangible asset base, with EPR / Frontline Digitisation deployments and digital-transformation capitalisation driving the trajectory.",
        "beneficiaries": "c. 2,300 WTE staff serving a c. 200,000 East Cheshire catchment (Macclesfield, Congleton, Knutsford, Wilmslow, Poynton); c. 55,000 ED attendances/yr at Macclesfield DGH ED; c. 25,000 admissions/yr; small-DGH plus integrated community-services footprint within Cheshire & Merseyside ICS.",
        "legal_basis": "IAS 38 Intangible Assets — DHSC Group Accounting Manual 2024-25 ch.5 — NHS Act 2006 — Health and Care Act 2022 — NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£0.35M"},
            {"label": "Trust scale", "value": "Macclesfield District General Hospital + integrated community-services footprint; c. 2,300 WTE"},
            {"label": "Composition", "value": "Capitalised software, EPR / clinical-system deployment costs, licensed third-party intellectual property amortisation"},
            {"label": "EPR / Frontline Digitisation", "value": "Digital-track adoption shapes intangible-base growth → amortisation feed-through over 5-10 year useful-life"},
            {"label": "Asset base context", "value": "Small-trust intangible base reflects scale; East Cheshire considered most-financially-challenged-trust in region historically"},
            {"label": "Useful-life convention", "value": "DHSC GAM typical 5-10 years for software; longer for capitalised configuration / data-migration"},
            {"label": "Industrial action 2023-24 effect", "value": "Indirect — amortisation profile insensitive to operational shocks; capitalisation cycle drives line"},
            {"label": "April 2025 NIC + CPI", "value": "Amortisation cashflow-insensitive; new-build software acquisitions feed forward intangible base"},
            {"label": "Funding trajectory", "value": "2021-22 c. £0.20M → 2023-24 c. £0.30M → 2024-25 £0.35M — sustained intangible-base growth from EPR + digital-transformation"},
            {"label": "Delivery body", "value": "Trust IT + Finance + (Cerner / Oracle Health / SystemC + NHS Digital framework) + Cheshire & Merseyside ICS shared-IT"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + NHSE Digital + DHSC + Cheshire & Merseyside ICB"},
            {"label": "Evaluation evidence", "value": "Frontline Digitisation programme reporting; NAO Digital Transformation in NHS; Model Hospital digital benchmark; CQC RJN inspections; Trust ARA 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2018 small-trust digital baseline · Successor: full Frontline Digitisation EPR + ICS shared digital platform amortisation cycle"}
        ],
        "notes": "East Cheshire's amortisation line reflects a small-trust intangible base — Macclesfield DGH plus integrated community services — where EPR / Frontline Digitisation adoption and ICS-shared digital-platform contributions feed the capitalised intangible base whose IAS 38 useful-life write-down (typically 5-10 years for software) sits in this line. The trust has long been one of the most financially-challenged smalls in Cheshire & Merseyside, with provider-merger discussions recurrent — the amortisation perimeter would migrate on any future MHA or merger transaction. NAO Digital Transformation in NHS scrutiny shapes capitalisation thresholds; useful-life judgement remains a key audit estimate per Trust ARA disclosures.",
        "sources": [
            {"publisher": "East Cheshire NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.eastcheshire.nhs.uk/About-The-Trust/Annual-Reports/index.htm"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/connecting-health-and-care/frontline-digitisation/"},
            {"publisher": "Care Quality Commission", "title": "East Cheshire NHS Trust provider profile (RJN)", "url": "https://www.cqc.org.uk/provider/RJN"},
            {"publisher": "National Audit Office", "title": "Digital transformation in the NHS", "url": "https://www.nao.org.uk/reports/digital-transformation-in-the-nhs/"}
        ],
        "related": ["East Cheshire NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Lease expenditure — Tameside and Glossop Integrated Care NHS Foundation Trust", "Frontline Digitisation programme", "Department of Health and Social Care"]
    },
    "Lease expenditure — Torbay and South Devon NHS Foundation Trust": {
        "aliases": [{"name": "Lease expenditure", "parent": "Torbay and South Devon NHS Foundation Trust"}],
        "description": "Torbay and South Devon's £0.35M lease-expenditure line covers post-IFRS 16 residual operating leases (medical equipment, IT hardware, fleet, small-property leases) outside the dominant Torbay Hospital estate, brought on-balance-sheet from 2022-23 under DHSC GAM ch.7. The trust is the long-running national pilot for fully integrated acute + adult-social-care + community-services delivery (under section 75 Health and Social Care Act 2008 since 2015), with leases shaped by the wide community-clinic footprint across Torbay Council and South Devon.",
        "beneficiaries": "c. 6,500 WTE staff serving a c. 375,000 catchment (Torbay c. 140,000 + South Devon districts c. 235,000); c. 80,000 ED attendances/yr at Torbay Hospital ED; c. 50,000 admissions/yr; main Torbay Hospital + c. 14 community-hospital sites + integrated adult-social-care delivery.",
        "legal_basis": "IFRS 16 Leases — DHSC Group Accounting Manual 2024-25 ch.7 — Landlord and Tenant Act 1954 — Health and Social Care Act 2008 (s.75 partnership) — NHS Act 2006 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Lease expenditure 2024-25", "value": "£0.35M"},
            {"label": "Trust scale", "value": "Torbay Hospital DGH + c. 14 community-hospital sites + integrated adult social care; c. 6,500 WTE"},
            {"label": "Composition", "value": "Residual operating leases — medical equipment, IT hardware, fleet, small property (post-IFRS 16 right-of-use)"},
            {"label": "Integrated care pilot context", "value": "National pilot for fully integrated acute + adult-social-care + community services since 2015 (s.75 Health and Social Care Act 2008)"},
            {"label": "Community-clinic footprint", "value": "Wide community-hospital + clinic estate across Torbay + South Devon shapes property/equipment lease perimeter"},
            {"label": "IFRS 16 jump 2022-23", "value": "On-balance-sheet right-of-use assets recognised; residual op-lease here is short-term + low-value exemption"},
            {"label": "Industrial action 2023-24 effect", "value": "Junior-doctor 44 days + consultant strikes drove short-term equipment-rental top-ups for backfill rotas"},
            {"label": "April 2025 NIC + CPI", "value": "Lease cashflows largely fixed; IT-equipment rentals exposed to CPI re-indexation"},
            {"label": "Funding trajectory", "value": "2021-22 (pre-IFRS 16) c. £1.3M → 2022-23 IFRS 16 reclassification → 2024-25 £0.35M residual"},
            {"label": "Delivery body", "value": "Trust E&F + Procurement + IT + (NHS Supply Chain framework for medical equipment leases) + Devon ICS"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Devon ICB + DHSC integrated-care pilot evaluation"},
            {"label": "Evaluation evidence", "value": "Nuffield Trust Torbay integrated-care evaluation; Model Hospital estates/leasing benchmark; CQC RA9 inspections; NAO integrated-care report; Trust ARA 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-IFRS 16 op-lease accounting; pre-2015 separate acute + community-trust footprint · Successor: continued IFRS 16 perimeter normalisation + Devon ICS shared-services lease pooling"}
        ],
        "notes": "Torbay and South Devon's residual lease-expenditure line reflects the post-IFRS 16 (2022-23) accounting reset that pulled material leases on-balance-sheet — what remains here is short-term + low-value-exemption op-leases (medical equipment, IT, fleet, small property) across the integrated acute + community-clinic footprint. Torbay has been the national pilot for fully-integrated acute + adult-social-care + community-services since 2015 under s.75 Health and Social Care Act 2008 — Nuffield Trust evaluations have shaped national integrated-care discourse. Industrial action 2023-24 drove short-term equipment-rental top-ups; CPI re-indexation on IT-equipment contracts feeds forward into 2025-26. Devon ICB shared-services lease pooling discussions shape the medium-term perimeter.",
        "sources": [
            {"publisher": "Torbay and South Devon NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.torbayandsouthdevon.nhs.uk/about-us/our-publications/annual-reports/"},
            {"publisher": "Nuffield Trust", "title": "The integrated care system in Torbay and South Devon", "url": "https://www.nuffieldtrust.org.uk/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "HM Treasury / FRAB", "title": "Application of IFRS 16 Leases in the public sector", "url": "https://www.gov.uk/government/publications/financial-reporting-advisory-board-frab"},
            {"publisher": "Care Quality Commission", "title": "Torbay and South Devon provider profile (RA9)", "url": "https://www.cqc.org.uk/provider/RA9"}
        ],
        "related": ["Torbay and South Devon NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Lease expenditure — Warrington and Halton Teaching Hospitals NHS Foundation Trust", "Lease expenditure — Tameside and Glossop Integrated Care NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Termination & post-employment — Royal Surrey NHS Foundation Trust": {
        "aliases": [{"name": "Termination & post-employment", "parent": "Royal Surrey NHS Foundation Trust"}],
        "description": "Royal Surrey's £0.35M termination & post-employment line covers IAS 19 employee-benefit termination payments, post-employment defined-benefit movements (NHS Pension Scheme actuarial increments, ill-health early-retirement enhancements) and Public Sector Exit Payments-regulated severance across the Royal Surrey County Hospital Guildford footprint. The trust is a regional cancer-centre with the Royal Surrey-led genomics laboratory hub, and runs a clinical-services collaboration with Ashford & St Peter's NHS FT (Surrey Health Partners group-model) shaping workforce-restructuring activity.",
        "beneficiaries": "c. 4,300 WTE staff serving a c. 320,000 Surrey catchment (Guildford, Waverley, Surrey Heath, parts of West Sussex/Hampshire); c. 80,000 ED attendances/yr at Royal Surrey ED; c. 50,000 admissions/yr; regional cancer centre + genomics-hub + Surrey Health Partners group with Ashford & St Peter's.",
        "legal_basis": "IAS 19 Employee Benefits — DHSC Group Accounting Manual 2024-25 — NHS Pension Scheme Regulations 2015 — Public Sector Exit Payments Regulations 2020 (and 2021 partial revocation) — Employment Rights Act 1996 — NHS Act 2006",
        "key_stats": [
            {"label": "Termination & post-employment 2024-25", "value": "£0.35M"},
            {"label": "Trust scale", "value": "Royal Surrey County Hospital (Guildford); c. 4,300 WTE; regional cancer centre + national genomics-laboratory hub"},
            {"label": "Composition", "value": "Termination payments (redundancy + MARS) + IAS 19 post-employment defined-benefit movements + ill-health early-retirement enhancements + tribunal settlements"},
            {"label": "Surrey Health Partners group", "value": "Clinical-services collaboration with Ashford & St Peter's NHS FT — group-model workforce-restructuring drives termination perimeter"},
            {"label": "NHS Pension Scheme context", "value": "2015 scheme + McCloud remediation period (1 Apr 2022) + 2024-25 contribution rebanding shape post-employment line"},
            {"label": "Public Sector Exit Payments Regs 2020", "value": "£95k cap revoked Feb 2021; HMT MARS guidance still applies — Treasury approval required for payments >£200k"},
            {"label": "Industrial action 2023-24 effect", "value": "Junior-doctor 44 days + consultant strikes drove agency dependency + selective restructuring; line low-volume but sensitive"},
            {"label": "April 2025 employer NIC step-up", "value": "15% rate from April 2025 + £5k threshold reduces severance-package employer cost residual"},
            {"label": "Funding trajectory", "value": "2021-22 c. £0.20M → 2023-24 c. £0.30M → 2024-25 £0.35M — sustained restructuring + IAS 19 movements"},
            {"label": "Delivery body", "value": "Trust HR + Pensions + Finance + (NHS Business Services Authority pension administration) + Surrey Health Partners HR"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + NHS Pensions Agency + HMT (PSEP regulations) + Surrey Heartlands ICB"},
            {"label": "Evaluation evidence", "value": "NHS Pension Scheme actuarial valuations; NAO Public Sector Exit Payments report; CQC RA2 inspections; Trust ARA 2023-24 + remuneration disclosures"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-McCloud + pre-2020 PSEP-regs framework · Successor: ongoing McCloud remediation + Surrey Health Partners group integration restructuring"}
        ],
        "notes": "Royal Surrey's termination & post-employment line carries the workforce-restructuring perimeter of a regional cancer-centre and national genomics-hub trust collaborating with Ashford & St Peter's NHS FT under the Surrey Health Partners group-model — group-integration moves drive selective restructuring activity. NHS Pension Scheme McCloud remediation (1 April 2022 onwards) and 2024-25 contribution rebanding shape post-employment movements through IAS 19 actuarial recognition. Public Sector Exit Payments Regulations 2020 (£95k cap) were revoked in February 2021, but HMT MARS guidance still applies. April 2025 employer-NIC step-up to 15% modestly reduces severance-package employer cost residual going forward.",
        "sources": [
            {"publisher": "Royal Surrey NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.royalsurrey.nhs.uk/about-us/board-of-directors/trust-board-papers/"},
            {"publisher": "NHS Business Services Authority", "title": "NHS Pension Scheme — annual report and accounts", "url": "https://www.nhsbsa.nhs.uk/nhs-pensions"},
            {"publisher": "HM Treasury", "title": "Public Sector Exit Payments — guidance and regulations", "url": "https://www.gov.uk/government/publications/guidance-on-public-sector-exit-payments"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Royal Surrey provider profile (RA2)", "url": "https://www.cqc.org.uk/provider/RA2"}
        ],
        "related": ["Royal Surrey NHS Foundation Trust", "Staff Costs", "NHS Acute Trusts", "Termination & post-employment — North Bristol NHS Trust", "Ashford and St Peter's Hospitals NHS Foundation Trust", "NHS Pension Scheme"]
    },
    "Lease expenditure — University Hospitals of North Midlands NHS Trust": {
        "aliases": [{"name": "Lease expenditure", "parent": "University Hospitals of North Midlands NHS Trust"}],
        "description": "University Hospitals of North Midlands' £0.35M lease-expenditure line covers post-IFRS 16 residual operating leases (medical equipment, IT hardware, fleet, small-property leases) outside the dominant Royal Stoke University Hospital and County Hospital (Stafford) PFI estates, brought on-balance-sheet from 2022-23 under DHSC GAM ch.7. UHNM is the second-largest acute trust in the West Midlands and runs major-trauma + tertiary-specialty services (neurosurgery, cardiothoracic) with two large PFI sites (Royal Stoke + Stafford) shaping the dominant premises-cost profile.",
        "beneficiaries": "c. 11,000 WTE staff serving a c. 900,000 catchment (Stoke-on-Trent + Staffordshire + Cheshire + Shropshire tertiary referrals); c. 235,000 ED attendances/yr (Royal Stoke Major Trauma Centre + County Hospital Stafford ED); c. 130,000 admissions/yr; two-site major acute (Royal Stoke + Stafford) + community satellites.",
        "legal_basis": "IFRS 16 Leases — DHSC Group Accounting Manual 2024-25 ch.7 — Landlord and Tenant Act 1954 — NHS Act 2006 — Health and Care Act 2022 — IFRIC 12 (PFI cross-ref)",
        "key_stats": [
            {"label": "Lease expenditure 2024-25", "value": "£0.35M"},
            {"label": "Trust scale", "value": "Royal Stoke University Hospital (Major Trauma Centre + tertiary) + County Hospital Stafford; c. 11,000 WTE; second-largest acute in West Midlands"},
            {"label": "Composition", "value": "Residual operating leases — medical equipment, IT hardware, fleet, small property (post-IFRS 16 right-of-use)"},
            {"label": "PFI estate context", "value": "Royal Stoke PFI (Project Co Healthcare Stoke 2007-2042) + County Hospital Stafford PFI — large unitary-charge perimeter sits in PFI/LIFT line"},
            {"label": "Tertiary specialty workforce", "value": "Major-trauma + neurosurgery + cardiothoracic specialty drives high-end equipment-leasing pressure (specialist devices outside main capital programme)"},
            {"label": "IFRS 16 jump 2022-23", "value": "On-balance-sheet right-of-use assets recognised; residual op-lease here is short-term + low-value exemption"},
            {"label": "Industrial action 2023-24 effect", "value": "Junior-doctor 44 days + consultant strikes drove short-term equipment-rental top-ups for backfill rotas in tertiary specialties"},
            {"label": "April 2025 NIC + CPI", "value": "Lease cashflows largely fixed; specialist medical-equipment rentals exposed to CPI re-indexation"},
            {"label": "Funding trajectory", "value": "2021-22 (pre-IFRS 16) c. £1.5M → 2022-23 IFRS 16 reclassification → 2024-25 £0.35M residual"},
            {"label": "Delivery body", "value": "Trust E&F + Procurement + IT + Specialty Equipment Leasing + (NHS Supply Chain framework) + Staffordshire & Stoke-on-Trent ICS"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + NHSE Specialised Commissioning + DHSC + Staffordshire & Stoke-on-Trent ICB"},
            {"label": "Evaluation evidence", "value": "NAO PFI/PF2 report; Model Hospital estates/leasing benchmark; CQC RJE inspections; NHSE Specialised Commissioning peer review; Trust ARA 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-IFRS 16 op-lease accounting; pre-2014 Mid Staffordshire NHS FT dissolution + County Hospital integration · Successor: continued IFRS 16 perimeter normalisation + ICS shared-services lease pooling"}
        ],
        "notes": "UHNM's residual lease-expenditure line reflects the post-IFRS 16 (2022-23) accounting reset that pulled material leases on-balance-sheet — what remains here is short-term + low-value-exemption op-leases (specialty equipment, IT, fleet) outside the two PFI premises footprints (Royal Stoke 2007-2042 + County Hospital Stafford). The trust's tertiary specialty mix (Major Trauma Centre, neurosurgery, cardiothoracic) drives selected high-end equipment-leasing pressure outside the main capital programme. The County Hospital Stafford portfolio integrated post-Mid Staffordshire NHS FT dissolution (2014) under the Francis Report aftermath. Industrial action 2023-24 lifted short-term equipment-rental top-ups; CPI re-indexation feeds forward into 2025-26.",
        "sources": [
            {"publisher": "University Hospitals of North Midlands NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.uhnm.nhs.uk/about-us/publications/annual-reports-and-accounts/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "National Audit Office", "title": "PFI and PF2 (HC 718, 2018)", "url": "https://www.nao.org.uk/reports/pfi-and-pf2/"},
            {"publisher": "Care Quality Commission", "title": "UHNM provider profile (RJE)", "url": "https://www.cqc.org.uk/provider/RJE"},
            {"publisher": "HM Treasury / FRAB", "title": "Application of IFRS 16 Leases in the public sector", "url": "https://www.gov.uk/government/publications/financial-reporting-advisory-board-frab"}
        ],
        "related": ["University Hospitals of North Midlands NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Lease expenditure — Torbay and South Devon NHS Foundation Trust", "Lease expenditure — United Lincolnshire Hospitals NHS Trust", "Department of Health and Social Care"]
    },
    "Inventories written down — South Tyneside and Sunderland NHS Foundation Trust": {
        "aliases": [{"name": "Inventories written down", "parent": "South Tyneside and Sunderland NHS Foundation Trust"}],
        "description": "South Tyneside and Sunderland's £0.33M inventories-written-down line covers stock obsolescence and write-downs of clinical consumables, drugs, theatre supplies and implants across the Sunderland Royal Hospital, South Tyneside District General Hospital (South Shields) and community-clinic footprint serving North East and North Cumbria ICS. The trust formed in April 2019 from the merger of City Hospitals Sunderland NHS FT and South Tyneside NHS FT — post-merger inventory-system harmonisation has shaped a sustained CIP focus on stock-loss reduction.",
        "beneficiaries": "c. 7,800 WTE staff serving a c. 430,000 catchment (Sunderland c. 275,000 + South Tyneside c. 155,000); c. 175,000 ED attendances/yr (Sunderland Royal ED + South Tyneside DGH ED); c. 80,000 admissions/yr; two-site DGH footprint + integrated community-clinic + maternity hub.",
        "legal_basis": "IAS 2 Inventories — DHSC Group Accounting Manual 2024-25 — NHS Act 2006 — Human Medicines Regulations 2012 — Health and Care Act 2022 — NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "Inventories written down 2024-25", "value": "£0.33M"},
            {"label": "Trust scale", "value": "Sunderland Royal Hospital + South Tyneside District General Hospital (South Shields) + community footprint; c. 7,800 WTE"},
            {"label": "Merger context", "value": "Formed April 2019 from City Hospitals Sunderland NHS FT + South Tyneside NHS FT merger — post-merger stock-system harmonisation"},
            {"label": "Composition", "value": "Drug expiry (high-cost specialty + paediatric) + short-dated theatre consumables + obsolete implants + ward-stock obsolescence"},
            {"label": "GS1 Scan4Safety adoption", "value": "Investment in barcode-tracking + EPR-pharmacy integration (regional pilot among NHSE programme cohort)"},
            {"label": "Drug shortages context", "value": "DHSC SSP regime + ongoing UK drug-shortage notices drive emergency stock + expiry risk"},
            {"label": "Industrial action 2023-24 effect", "value": "Cancellation-rebooking can lift theatre-consumable expiry; line low-volume but sensitive"},
            {"label": "April 2025 NIC + drug-tariff", "value": "Drug-tariff and CPI uplifts re-price stock baseline; expiry write-downs sensitive to demand-volume volatility"},
            {"label": "Funding trajectory", "value": "2021-22 c. £0.40M → 2023-24 c. £0.32M → 2024-25 £0.33M — sustained at low base via Scan4Safety + EPR controls"},
            {"label": "Delivery body", "value": "Trust Procurement + Pharmacy + Theatres + (NHS Supply Chain Drugs/Theatre framework) + Drug & Therapeutics Committee + GS1 Scan4Safety"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC Medicines + NHS Supply Chain + North East and North Cumbria ICB"},
            {"label": "Evaluation evidence", "value": "Model Hospital pharmacy/inventory benchmark; CQC R0B inspections; NHSE Scan4Safety pilot evaluation; NAO inventory management; Trust ARA 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2019 separate Sunderland + South Tyneside trust stock systems · Successor: continued NENC ICS shared-pharmacy + EPR convergence"}
        ],
        "notes": "South Tyneside and Sunderland's inventories-written-down line reflects post-merger (April 2019) stock-system harmonisation across the two-site footprint, with sustained CIP focus on stock-loss reduction supported by GS1 Scan4Safety adoption and EPR-pharmacy integration as a regional pilot within the NHSE Scan4Safety cohort. The trust sits within North East and North Cumbria ICS — the largest ICS in England by population — with shared-pharmacy and shared-procurement initiatives shaping medium-term stock-management economics. Industrial action 2023-24 cancellations modestly lifted theatre-consumable expiry risk. Drug-tariff and CPI uplifts re-price the stock baseline forward into 2025-26.",
        "sources": [
            {"publisher": "South Tyneside and Sunderland NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.stsft.nhs.uk/about-us/our-publications"},
            {"publisher": "NHS England", "title": "Scan4Safety / GS1 adoption programme", "url": "https://www.scan4safety.nhs.uk/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "South Tyneside and Sunderland provider profile (R0B)", "url": "https://www.cqc.org.uk/provider/R0B"},
            {"publisher": "National Audit Office", "title": "NHS supply chain and inventory management", "url": "https://www.nao.org.uk/"}
        ],
        "related": ["South Tyneside and Sunderland NHS Foundation Trust", "Clinical Supplies & Drugs", "NHS Acute Trusts", "Inventories written down — Worcestershire Acute Hospitals NHS Trust", "Inventories written down — Hampshire Hospitals NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Termination & post-employment — North Bristol NHS Trust": {
        "aliases": [{"name": "Termination & post-employment", "parent": "North Bristol NHS Trust"}],
        "description": "North Bristol's £0.32M termination & post-employment line covers IAS 19 employee-benefit termination payments, post-employment defined-benefit movements (NHS Pension Scheme actuarial increments, ill-health early-retirement enhancements) and Public Sector Exit Payments-regulated severance across the Southmead Hospital Brunel building footprint. The trust runs the dominant North Bristol acute footprint with a long-running PFI on Southmead Brunel (Carillion-built 2014, now Engie/Equans-novated post-Carillion 2018 collapse) and major-trauma + neurosciences tertiary specialty mix shaping workforce-restructuring activity.",
        "beneficiaries": "c. 8,500 WTE staff serving a c. 500,000 catchment (Bristol North + South Gloucestershire + parts of North Somerset); c. 100,000 ED attendances/yr at Southmead ED (regional Major Trauma Centre); c. 80,000 admissions/yr; main Southmead Hospital + Cossham Hospital + Frenchay community footprint.",
        "legal_basis": "IAS 19 Employee Benefits — DHSC Group Accounting Manual 2024-25 — NHS Pension Scheme Regulations 2015 — Public Sector Exit Payments Regulations 2020 (and 2021 partial revocation) — Employment Rights Act 1996 — NHS Act 2006",
        "key_stats": [
            {"label": "Termination & post-employment 2024-25", "value": "£0.32M"},
            {"label": "Trust scale", "value": "Southmead Hospital (Brunel building) + Cossham Hospital + Frenchay community; c. 8,500 WTE; regional Major Trauma Centre + neurosciences tertiary"},
            {"label": "Composition", "value": "Termination payments (redundancy + MARS) + IAS 19 post-employment defined-benefit movements + ill-health early-retirement enhancements + tribunal settlements"},
            {"label": "PFI / Carillion context", "value": "Brunel building PFI (HCP Healthcare Bristol 2010-2040); Carillion 2018 collapse drove FM novation to Engie/Equans — workforce-novation TUPE protected, no termination charge"},
            {"label": "NHS Pension Scheme context", "value": "2015 scheme + McCloud remediation period (1 Apr 2022) + 2024-25 contribution rebanding shape post-employment line"},
            {"label": "Public Sector Exit Payments Regs 2020", "value": "£95k cap revoked Feb 2021; HMT MARS guidance still applies"},
            {"label": "Industrial action 2023-24 effect", "value": "Junior-doctor 44 days + consultant strikes drove agency dependency in tertiary specialties; restructuring selectively applied"},
            {"label": "April 2025 employer NIC step-up", "value": "15% rate from April 2025 + £5k threshold reduces severance-package employer cost residual"},
            {"label": "Funding trajectory", "value": "2021-22 c. £0.20M → 2023-24 c. £0.28M → 2024-25 £0.32M — sustained restructuring + IAS 19 movements"},
            {"label": "Delivery body", "value": "Trust HR + Pensions + Finance + (NHS Business Services Authority pension administration) + Bristol, North Somerset and South Gloucestershire ICS HR"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + NHS Pensions Agency + HMT (PSEP regulations) + BNSSG ICB"},
            {"label": "Evaluation evidence", "value": "NHS Pension Scheme actuarial valuations; NAO Carillion fallout review; CQC RVJ inspections; Trust ARA 2023-24 + remuneration disclosures"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-McCloud + pre-2020 PSEP-regs framework · Successor: ongoing McCloud remediation + BNSSG ICS shared-services HR consolidation"}
        ],
        "notes": "North Bristol's termination & post-employment line carries the workforce-restructuring perimeter of a Major Trauma Centre and neurosciences-tertiary trust running on the Carillion-built Brunel PFI (now Engie/Equans-novated post-2018 collapse) — post-Carillion FM workforce novation was TUPE-protected so did not feed termination charges, but ongoing trust-side restructuring under BNSSG ICS shared-services consolidation drives selective activity. NHS Pension Scheme McCloud remediation (1 April 2022) and 2024-25 contribution rebanding shape post-employment movements through IAS 19 actuarial recognition. Public Sector Exit Payments Regulations 2020 (£95k cap) revoked February 2021. April 2025 employer-NIC step-up to 15% modestly reduces severance employer-cost residual.",
        "sources": [
            {"publisher": "North Bristol NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.nbt.nhs.uk/about-us/publications/annual-report-accounts"},
            {"publisher": "NHS Business Services Authority", "title": "NHS Pension Scheme — annual report and accounts", "url": "https://www.nhsbsa.nhs.uk/nhs-pensions"},
            {"publisher": "National Audit Office", "title": "Investigation into the government's handling of the collapse of Carillion", "url": "https://www.nao.org.uk/reports/investigation-into-the-governments-handling-of-the-collapse-of-carillion/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "North Bristol provider profile (RVJ)", "url": "https://www.cqc.org.uk/provider/RVJ"}
        ],
        "related": ["North Bristol NHS Trust", "Staff Costs", "NHS Acute Trusts", "Termination & post-employment — Royal Surrey NHS Foundation Trust", "PFI / LIFT charges — Royal Cornwall Hospitals NHS Trust", "NHS Pension Scheme"]
    },
    "Transport (business + patient) — West Hertfordshire Hospitals NHS Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "West Hertfordshire Hospitals NHS Trust"}],
        "description": "West Hertfordshire's £0.32M transport line covers business mileage (AfC Section 17 + AMAP), pool-fleet IFRS 16 lease costs, non-emergency patient transport service (NEPTS) cross-charges and patient travel reimbursements across the Watford General Hospital, Hemel Hempstead Hospital and St Albans City Hospital footprint serving West Hertfordshire. The trust sits in the New Hospital Programme cohort with the Watford-led 'Building Our Future' redevelopment — January 2025 NHP Reset rebaselined delivery to later wave but pre-construction transport-flow planning continues.",
        "beneficiaries": "c. 5,000 WTE staff serving a c. 600,000 West Hertfordshire catchment (Watford, Three Rivers, Dacorum, St Albans, Hertsmere); c. 130,000 ED attendances/yr at Watford General ED; c. 60,000 admissions/yr; three-site footprint (Watford General + Hemel Hempstead + St Albans City).",
        "legal_basis": "NHS Act 2006 — NHSE Patient Transport Services Eligibility Criteria — Agenda for Change Section 17 (business mileage) — HMRC AMAP rates — IFRS 16 Leases (pool fleet) — DHSC Group Accounting Manual 2024-25 — Health and Care Act 2022",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£0.32M"},
            {"label": "Trust scale", "value": "Three-site (Watford General + Hemel Hempstead + St Albans City Hospital); c. 5,000 WTE"},
            {"label": "NEPTS commissioning", "value": "Hertfordshire & West Essex ICB lead-commissioner NEPTS — outsourced operator delivery (E-zec Medical historically)"},
            {"label": "Composition", "value": "Business mileage (AfC S17 + AMAP 45p/25p) + pool-fleet IFRS 16 leases + NEPTS pass-through + patient travel + inter-site transfer transport"},
            {"label": "NHP cohort + Reset", "value": "Watford 'Building Our Future' redevelopment in NHP cohort; Jan 2025 Reset rebaselined to later wave; pre-construction planning continues"},
            {"label": "Inter-site transfers", "value": "Three-site model with maternity at Watford + elective at St Albans + outpatients at Hemel drives recurrent inter-site patient + staff transport"},
            {"label": "AMAP rate context", "value": "HMRC AMAP rate frozen at 45p/mile (first 10k miles) since 2011 — real-terms erosion"},
            {"label": "Industrial action 2023-24 effect", "value": "Junior-doctor 44 days + consultant strikes drove agency travel-claim spikes + cancellation rebooking transport"},
            {"label": "April 2025 NIC + fuel CPI", "value": "Indirect via NEPTS contractor pass-through + diesel CPI feed forward unit-cost pressure"},
            {"label": "Funding trajectory", "value": "2021-22 c. £0.27M → 2023-24 c. £0.30M → 2024-25 £0.32M — fuel CPI + NEPTS contract uplift"},
            {"label": "Delivery body", "value": "Trust E&F + outsourced NEPTS provider (Herts & West Essex ICB) + pool-fleet leasing partner + Trust HR (mileage)"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + NHSE Urgent and Emergency Care (NEPTS) + Hertfordshire & West Essex ICB + DHSC New Hospital Programme"},
            {"label": "Evaluation evidence", "value": "NHSE NEPTS Eligibility Review 2021; CQC RWG inspections; IPA Major Projects Report (NHP); Trust ARA 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-ICS CCG-commissioned NEPTS · Successor: post-NHP Reset Watford redevelopment new-site transport-flow re-baselining"}
        ],
        "notes": "West Hertfordshire's transport line carries an inter-site cross-flow burden distinctive to the three-site model (Watford General + Hemel Hempstead + St Albans City) where maternity, elective and outpatient services split across the footprint drives recurrent patient + staff inter-site transport. NEPTS is commissioned via Hertfordshire & West Essex ICB lead-commissioner arrangement (E-zec Medical historically). The 'Building Our Future' Watford redevelopment in the NHP cohort was rebaselined to a later wave under the January 2025 NHP Reset, sustaining the existing three-site transport-flow profile longer than originally planned. Industrial action 2023-24 drove cancellation-rebooking and agency-travel claims; HMRC AMAP-rate freeze (45p/mile since 2011) and fuel CPI feed forward into 2025-26.",
        "sources": [
            {"publisher": "West Hertfordshire Teaching Hospitals NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.westhertshospitals.nhs.uk/aboutus/publications/"},
            {"publisher": "NHS England", "title": "Non-Emergency Patient Transport Services — National Framework + Eligibility Criteria 2021", "url": "https://www.england.nhs.uk/publication/non-emergency-patient-transport-services-nepts/"},
            {"publisher": "Department of Health and Social Care", "title": "New Hospital Programme — January 2025 Reset", "url": "https://www.gov.uk/government/publications/new-hospital-programme-plan-for-implementation"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "West Hertfordshire provider profile (RWG)", "url": "https://www.cqc.org.uk/provider/RWG"}
        ],
        "related": ["West Hertfordshire Hospitals NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Transport (business + patient) — University Hospitals Plymouth NHS Trust", "New Hospital Programme", "NHS England"]
    },
    "Lease expenditure — United Lincolnshire Hospitals NHS Trust": {
        "aliases": [{"name": "Lease expenditure", "parent": "United Lincolnshire Hospitals NHS Trust"}],
        "description": "United Lincolnshire's £0.32M lease-expenditure line covers post-IFRS 16 residual operating leases (medical equipment, IT hardware, fleet, small-property leases) outside the four main hospital sites — Lincoln County, Pilgrim Hospital Boston, Grantham & District, and Louth County — brought on-balance-sheet from 2022-23 under DHSC GAM ch.7. The trust covers an exceptionally large rural geography (Greater Lincolnshire c. 7,800 km²) and runs Lincolnshire Acute Reconfiguration discussions where service reorganisation drives episodic equipment-leasing and modular-decant requirements.",
        "beneficiaries": "c. 8,500 WTE staff serving a c. 750,000 Greater Lincolnshire catchment (Lincoln, Boston, Grantham, Louth, Skegness, Spalding); c. 250,000 ED attendances/yr (Lincoln County + Pilgrim Boston ED + Grantham urgent care); c. 100,000 admissions/yr; four-site footprint covering a large rural geography.",
        "legal_basis": "IFRS 16 Leases — DHSC Group Accounting Manual 2024-25 ch.7 — Landlord and Tenant Act 1954 — NHS Act 2006 — Health and Care Act 2022 — NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "Lease expenditure 2024-25", "value": "£0.32M"},
            {"label": "Trust scale", "value": "Four sites (Lincoln County + Pilgrim Boston + Grantham & District + Louth County) + community footprint; c. 8,500 WTE; large rural geography"},
            {"label": "Composition", "value": "Residual operating leases — medical equipment, IT hardware, fleet, small property (post-IFRS 16 right-of-use)"},
            {"label": "Lincolnshire Acute Services Review", "value": "Long-running service-reconfiguration discussions (Grantham downgrade, Pilgrim Boston ED reconfiguration) drive episodic modular-decant + equipment-leasing"},
            {"label": "NHP cohort + Reset", "value": "Lincolnshire was outside the NHP 40-hospital programme; Jan 2025 Reset confirms continued reliance on existing-estate equipment-leasing"},
            {"label": "IFRS 16 jump 2022-23", "value": "On-balance-sheet right-of-use assets recognised; residual op-lease here is short-term + low-value exemption"},
            {"label": "Industrial action 2023-24 effect", "value": "Junior-doctor 44 days + consultant strikes drove short-term equipment-rental top-ups for backfill rotas"},
            {"label": "April 2025 NIC + CPI", "value": "Lease cashflows largely fixed; IT-equipment + medical-equipment rentals exposed to CPI re-indexation"},
            {"label": "Funding trajectory", "value": "2021-22 (pre-IFRS 16) c. £1.4M → 2022-23 IFRS 16 reclassification → 2024-25 £0.32M residual"},
            {"label": "Delivery body", "value": "Trust E&F + Procurement + IT + (NHS Supply Chain framework for medical equipment leases) + Lincolnshire ICS shared-services"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Lincolnshire ICB + NHSE Recovery Support Programme (legacy oversight)"},
            {"label": "Evaluation evidence", "value": "NAO Lincolnshire Acute Reconfiguration scrutiny; Model Hospital estates/leasing benchmark; CQC RWD inspections; NHSE Recovery Support Programme exit; Trust ARA 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-IFRS 16 op-lease accounting · Successor: post-Acute Services Review reconfigured-footprint lease perimeter + Lincolnshire ICS shared-services"}
        ],
        "notes": "United Lincolnshire's residual lease-expenditure line reflects the post-IFRS 16 (2022-23) accounting reset that pulled material leases on-balance-sheet — what remains is short-term + low-value-exemption op-leases (medical equipment, IT, fleet, small property) across an exceptionally large rural four-site footprint. The trust has been in long-running service-reconfiguration discussions (Grantham A&E downgrade, Pilgrim Boston ED restructuring) under the Lincolnshire Acute Services Review — episodic modular-decant and equipment-leasing requirements arise during reconfiguration windows. Lincolnshire was outside the original NHP 40-hospital programme, sustained by the January 2025 Reset, so equipment-leasing remains the recurrent capital substitute. Industrial action 2023-24 drove rental top-ups; CPI re-indexation feeds forward.",
        "sources": [
            {"publisher": "United Lincolnshire Hospitals NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.ulh.nhs.uk/about/annual-reports/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "HM Treasury / FRAB", "title": "Application of IFRS 16 Leases in the public sector", "url": "https://www.gov.uk/government/publications/financial-reporting-advisory-board-frab"},
            {"publisher": "Care Quality Commission", "title": "United Lincolnshire provider profile (RWD)", "url": "https://www.cqc.org.uk/provider/RWD"},
            {"publisher": "NHS England", "title": "Lincolnshire Acute Services Review", "url": "https://www.lincolnshire.icb.nhs.uk/"}
        ],
        "related": ["United Lincolnshire Hospitals NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Lease expenditure — University Hospitals of North Midlands NHS Trust", "Lease expenditure — Tameside and Glossop Integrated Care NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Inventories written down — Chelsea and Westminster Hospital NHS Foundation Trust": {
        "aliases": [{"name": "Inventories written down", "parent": "Chelsea and Westminster Hospital NHS Foundation Trust"}],
        "description": "Chelsea and Westminster's £0.31M inventories-written-down line covers stock obsolescence and write-downs of clinical consumables, drugs (including high-cost specialty + HIV medicines), theatre supplies and implants across the Chelsea and Westminster Hospital (Fulham Road) and West Middlesex University Hospital (Isleworth) sites serving North West London ICS. The trust is a national leader in HIV care + sexual health (56 Dean Street + 10 Hammersmith Broadway) — high-cost antiretroviral stock-management and SARMA-aligned PrEP supply shape an above-peer-trust expiry-risk profile.",
        "beneficiaries": "c. 6,400 WTE staff serving a c. 1,050,000 catchment (West London + parts of Hounslow, Hammersmith & Fulham, Kensington & Chelsea); c. 230,000 ED attendances/yr (Chelsea & Westminster ED + West Middlesex ED); c. 95,000 admissions/yr; two-site main acute + sexual-health centres + community footprint.",
        "legal_basis": "IAS 2 Inventories — DHSC Group Accounting Manual 2024-25 — NHS Act 2006 — Human Medicines Regulations 2012 — Health and Care Act 2022 — NHS Standard Contract 2024-25 — NHS Specialised Commissioning HIV/PrEP guidance",
        "key_stats": [
            {"label": "Inventories written down 2024-25", "value": "£0.31M"},
            {"label": "Trust scale", "value": "Two-site main acute (Chelsea & Westminster Hospital + West Middlesex University Hospital Isleworth); c. 6,400 WTE"},
            {"label": "Composition", "value": "High-cost ARV + PrEP drug expiry + paediatric specialty drugs + theatre consumables + obsolete implants + ward-stock obsolescence"},
            {"label": "HIV / sexual-health specialty", "value": "56 Dean Street + 10 Hammersmith Broadway — national leadership in HIV care + sexual health drives ARV + PrEP stock-management complexity"},
            {"label": "GS1 Scan4Safety adoption", "value": "Investment in barcode-tracking + EPR-pharmacy integration"},
            {"label": "Drug shortages context", "value": "DHSC SSP regime + ongoing UK drug-shortage notices drive emergency stock + expiry risk; ARV supply chain particularly sensitive"},
            {"label": "Industrial action 2023-24 effect", "value": "Cancellation-rebooking can lift theatre-consumable expiry"},
            {"label": "April 2025 NIC + drug-tariff", "value": "Drug-tariff and CPI uplifts re-price stock baseline; ARV demand-volume volatility a key sensitivity"},
            {"label": "Funding trajectory", "value": "2021-22 c. £0.40M → 2023-24 c. £0.30M → 2024-25 £0.31M — sustained at low base via stock controls + Scan4Safety"},
            {"label": "Delivery body", "value": "Trust Procurement + Pharmacy + Sexual-Health Pharmacy + (NHS Supply Chain Drugs/Theatre framework) + 56 Dean Street + NHS Specialised Commissioning HIV"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + NHSE Specialised Commissioning (HIV/PrEP) + DHSC Medicines + NHS Supply Chain + North West London ICB"},
            {"label": "Evaluation evidence", "value": "Model Hospital pharmacy/inventory benchmark; CQC RQM inspections; NAO HIV care review; NHSE Specialised Commissioning peer review; Trust ARA 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2015 separate Chelsea & Westminster + West Middlesex trust stock systems · Successor: NWL ICS shared-pharmacy + EPR convergence"}
        ],
        "notes": "Chelsea and Westminster's inventories-written-down line carries a distinctive HIV + sexual-health specialty signature — the trust hosts 56 Dean Street and 10 Hammersmith Broadway, England's leading HIV care + sexual-health centres, where high-cost ARV stock-management and SARMA-aligned PrEP supply create above-peer-trust expiry-risk exposure. The trust merged with West Middlesex in 2015 and continues to harmonise stock systems across the two-site footprint with GS1 Scan4Safety and EPR-pharmacy integration. Industrial action 2023-24 cancellation-rebooking modestly lifted theatre-consumable expiry. Drug-tariff and CPI uplifts re-price the stock baseline forward; ARV-demand volatility under PrEP-uptake variability remains a key sensitivity into 2025-26.",
        "sources": [
            {"publisher": "Chelsea and Westminster Hospital NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.chelwest.nhs.uk/about-us/corporate-information/annual-reports"},
            {"publisher": "NHS England", "title": "Scan4Safety / GS1 adoption programme", "url": "https://www.scan4safety.nhs.uk/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Chelsea and Westminster provider profile (RQM)", "url": "https://www.cqc.org.uk/provider/RQM"},
            {"publisher": "NHS England Specialised Commissioning", "title": "HIV PrEP and antiretroviral commissioning", "url": "https://www.england.nhs.uk/commissioning/spec-services/"}
        ],
        "related": ["Chelsea and Westminster Hospital NHS Foundation Trust", "Clinical Supplies & Drugs", "NHS Acute Trusts", "Inventories written down — Worcestershire Acute Hospitals NHS Trust", "Inventories written down — Hampshire Hospitals NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "PFI / LIFT charges — Royal Cornwall Hospitals NHS Trust": {
        "aliases": [{"name": "PFI / LIFT charges", "parent": "Royal Cornwall Hospitals NHS Trust"}],
        "description": "Royal Cornwall's £0.31M PFI/LIFT residual charges line covers small-scale LIFT (Local Improvement Finance Trust) community-clinic accommodation charges and ancillary service-concession contracts outside the dominant Royal Cornwall Hospital Treliske estate, accounted for under IFRIC 12 Service Concession Arrangements + IFRS 16 (post-2022) per DHSC GAM. Cornwall is geographically isolated as the South West Peninsula tertiary-acute provider with West Cornwall Hospital (Penzance) and St Michael's Hospital (Hayle) satellite sites — LIFT-funded community-clinic accommodation across Cornwall NHSPS-and-LIFTCo footprint feeds this residual line.",
        "beneficiaries": "c. 5,500 WTE staff serving a c. 565,000 Cornwall + Isles of Scilly catchment; c. 110,000 ED attendances/yr at Royal Cornwall ED (Treliske) + minor injuries at peripheral sites; c. 60,000 admissions/yr; main Royal Cornwall Hospital Treliske + West Cornwall Hospital Penzance + St Michael's Hospital Hayle + LIFT-funded community-clinic estate.",
        "legal_basis": "IFRIC 12 Service Concession Arrangements — IFRS 16 Leases (post-2022) — DHSC PFI / LIFT guidance — DHSC Group Accounting Manual 2024-25 — NHS Act 2006 — Health and Care Act 2022",
        "key_stats": [
            {"label": "PFI / LIFT charges 2024-25", "value": "£0.31M"},
            {"label": "Trust scale", "value": "Royal Cornwall Hospital Treliske + West Cornwall Hospital Penzance + St Michael's Hospital Hayle + community estate; c. 5,500 WTE; sole acute provider to Cornwall + Isles of Scilly"},
            {"label": "Composition", "value": "Small-scale LIFT community-clinic accommodation charges + ancillary service-concession arrangements (post-IFRS 16 treatment)"},
            {"label": "LIFTCo context", "value": "Cornwall LIFTCo (Express LIFT Co) primary-care-led community-estate vehicle — small acute-trust occupation drives this residual"},
            {"label": "Geographical isolation", "value": "Sole acute provider to c. 565,000 Cornwall + Isles of Scilly catchment — long patient distances; community-clinic LIFT estate reduces patient-travel burden"},
            {"label": "NHP cohort + Reset", "value": "Cornwall outside the NHP 40-hospital programme; Jan 2025 Reset confirms continued reliance on Treliske estate + community LIFT footprint"},
            {"label": "Industrial action 2023-24 effect", "value": "Indirect — PFI/LIFT charges contractually fixed; cancellations don't move line; no material strike-period reductions"},
            {"label": "April 2025 NIC + RPI re-indexation", "value": "Most LIFT/PFI contracts contractually RPI-indexed annually — feeds forward unit-cost pressure"},
            {"label": "Funding trajectory", "value": "2021-22 c. £0.27M → 2023-24 c. £0.30M → 2024-25 £0.31M — sustained RPI-linked uplift on stable LIFT footprint"},
            {"label": "Delivery body", "value": "Express LIFT Co (Cornwall LIFTCo) + Trust E&F + (Equitix-led infrastructure investor) + Cornwall ICS shared-estates"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC PFI/LIFT policy + Cornwall and the Isles of Scilly ICB"},
            {"label": "Evaluation evidence", "value": "NAO PFI and PF2 (HC 718, 2018); NAO LIFT review; CQC REF inspections; Trust ARA 2023-24; DHSC PFI / LIFT register"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-LIFT primary-care/community estate · Successor: continued LIFT-managed community estate + post-2032+ LIFT contract hand-back"}
        ],
        "notes": "Royal Cornwall's PFI/LIFT residual line covers small-scale community-clinic LIFT accommodation under the Cornwall LIFTCo (Express LIFT Co, Equitix-led) — the trust's main Treliske acute estate is not PFI-funded, so this line is the residual community footprint occupation rather than a major unitary-charge component. Cornwall's geographical isolation as sole acute provider to c. 565,000 Cornwall + Isles of Scilly catchment makes the community-LIFT estate strategically important for reducing long patient-travel distances. RPI-indexed contractual escalation continues to feed unit-cost pressure forward into 2025-26. The trust sits outside the NHP 40-hospital programme, sustained by the January 2025 Reset.",
        "sources": [
            {"publisher": "Royal Cornwall Hospitals NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.royalcornwall.nhs.uk/about-us/key-documents-publications/annual-reports/"},
            {"publisher": "National Audit Office", "title": "PFI and PF2 (HC 718, 2018)", "url": "https://www.nao.org.uk/reports/pfi-and-pf2/"},
            {"publisher": "Department of Health and Social Care", "title": "PFI and LIFT scheme registers", "url": "https://www.gov.uk/government/publications/pfi-and-pf2"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Royal Cornwall Hospitals provider profile (REF)", "url": "https://www.cqc.org.uk/provider/REF"}
        ],
        "related": ["Royal Cornwall Hospitals NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "PFI / LIFT charges — Sherwood Forest Hospitals NHS Foundation Trust", "Transport (business + patient) — University Hospitals Plymouth NHS Trust", "Department of Health and Social Care"]
    },
    "Inventories written down — Hampshire Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Inventories written down", "parent": "Hampshire Hospitals NHS Foundation Trust"}],
        "description": "Hampshire Hospitals' £0.31M inventories-written-down line covers stock obsolescence and write-downs of clinical consumables, drugs, theatre supplies and implants across the Royal Hampshire County Hospital (Winchester), Basingstoke and North Hampshire Hospital, and Andover War Memorial Hospital sites serving Hampshire & Isle of Wight ICS. The trust hosts the Pseudomyxoma Peritonei (PMP) national specialist centre at Basingstoke (one of two NHS England-commissioned PMP centres) — high-cost specialty oncology drug stock-management drives an above-peer-trust expiry-risk profile.",
        "beneficiaries": "c. 5,800 WTE staff serving a c. 600,000 catchment (mid + north Hampshire) + national PMP referrals; c. 145,000 ED attendances/yr (Royal Hampshire County + Basingstoke ED + Andover MIU); c. 70,000 admissions/yr; three-site footprint (Winchester + Basingstoke + Andover) + national PMP centre.",
        "legal_basis": "IAS 2 Inventories — DHSC Group Accounting Manual 2024-25 — NHS Act 2006 — Human Medicines Regulations 2012 — Health and Care Act 2022 — NHS Standard Contract 2024-25 — NHS Specialised Commissioning PMP guidance",
        "key_stats": [
            {"label": "Inventories written down 2024-25", "value": "£0.31M"},
            {"label": "Trust scale", "value": "Three-site (Royal Hampshire County Winchester + Basingstoke and North Hampshire + Andover War Memorial); c. 5,800 WTE"},
            {"label": "PMP national specialist centre", "value": "Pseudomyxoma Peritonei national centre at Basingstoke — one of two NHSE-commissioned PMP centres in England (with Christie Manchester); high-cost oncology drug stock"},
            {"label": "Composition", "value": "High-cost oncology drugs (PMP / cytoreductive surgery + HIPEC) + paediatric specialty drugs + theatre consumables + obsolete implants"},
            {"label": "GS1 Scan4Safety adoption", "value": "Investment in barcode-tracking + EPR-pharmacy integration"},
            {"label": "NHP cohort + Reset", "value": "Trust pursued joint Hampshire Hospitals + UHS reconfiguration discussions; Jan 2025 NHP Reset clarifies Basingstoke + Winchester future"},
            {"label": "Drug shortages context", "value": "DHSC SSP regime + ongoing UK drug-shortage notices drive emergency stock + expiry risk; specialty oncology supply chain particularly sensitive"},
            {"label": "Industrial action 2023-24 effect", "value": "Cancellation-rebooking lifted theatre-consumable expiry; PMP-cohort surgery cancellations drove specialty-drug expiry pressure"},
            {"label": "April 2025 NIC + drug-tariff", "value": "Drug-tariff and CPI uplifts re-price stock baseline; specialty oncology demand-volume volatility a key sensitivity"},
            {"label": "Funding trajectory", "value": "2021-22 c. £0.40M → 2023-24 c. £0.30M → 2024-25 £0.31M — sustained at low base via stock controls + Scan4Safety"},
            {"label": "Delivery body", "value": "Trust Procurement + Pharmacy + PMP Specialty Pharmacy + (NHS Supply Chain Drugs/Theatre framework) + NHS Specialised Commissioning"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + NHSE Specialised Commissioning (PMP) + DHSC Medicines + NHS Supply Chain + Hampshire & Isle of Wight ICB"},
            {"label": "Evaluation evidence", "value": "Model Hospital pharmacy/inventory benchmark; CQC RN5 inspections; NHSE Specialised Commissioning peer review; NAO inventory-management review; Trust ARA 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2012 Winchester + Basingstoke separate trust stock systems · Successor: post-NHP-Reset reconfiguration + HIOW ICS shared-pharmacy"}
        ],
        "notes": "Hampshire Hospitals' inventories-written-down line carries a distinctive specialty-oncology signature — the trust hosts the Pseudomyxoma Peritonei (PMP) national specialist centre at Basingstoke (one of two NHSE-commissioned PMP centres, with Christie Manchester), where high-cost cytoreductive-surgery and HIPEC drug stock-management drives above-peer expiry risk exposure. The trust pursued joint reconfiguration discussions with University Hospital Southampton — the January 2025 NHP Reset clarifies the Basingstoke + Winchester future. Industrial action 2023-24 cancellations and PMP-cohort surgery rescheduling lifted specialty-drug expiry pressure. Drug-tariff and CPI uplifts re-price the stock baseline forward; specialty oncology demand-volume volatility remains a key sensitivity into 2025-26.",
        "sources": [
            {"publisher": "Hampshire Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.hampshirehospitals.nhs.uk/about-us/our-publications/"},
            {"publisher": "NHS England Specialised Commissioning", "title": "Pseudomyxoma Peritonei service specification", "url": "https://www.england.nhs.uk/commissioning/spec-services/"},
            {"publisher": "NHS England", "title": "Scan4Safety / GS1 adoption programme", "url": "https://www.scan4safety.nhs.uk/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Hampshire Hospitals provider profile (RN5)", "url": "https://www.cqc.org.uk/provider/RN5"}
        ],
        "related": ["Hampshire Hospitals NHS Foundation Trust", "Clinical Supplies & Drugs", "NHS Acute Trusts", "Inventories written down — Chelsea and Westminster Hospital NHS Foundation Trust", "Inventories written down — South Tyneside and Sunderland NHS Foundation Trust", "Department of Health and Social Care"]
    },
}
