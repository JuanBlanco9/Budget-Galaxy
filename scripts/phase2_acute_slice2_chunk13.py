# -*- coding: utf-8 -*-
# Phase 2 Acute slice 2 — chunk 13 (17 NHS Acute Trust orphan sub-lines)
# Hand-curated trust-specific PROGRAMME-archetype enrichment entries.
# Structural contract per docs/archetype_briefs.md.

NEW = {
    "Business rates — Imperial College Healthcare NHS Trust": {
        "aliases": [{"name": "Business rates", "parent": "Imperial College Healthcare NHS Trust"}],
        "description": "Imperial's £6.42M business rates line covers non-domestic rating liability under the Local Government Finance Act 1988 across the trust's five-site footprint — St Mary's (Paddington), Charing Cross, Hammersmith, Queen Charlotte's & Chelsea and Western Eye. The 2023 rating list revaluation lifted hereditament rateable values across central and west London, and Imperial's prime-London estate carries some of the highest hospital RVs in the NHS. NHS trusts are not registered charities, so no mandatory 80% rate relief applies on hospital hereditaments — full liability flows to the trust.",
        "beneficiaries": "c. 14,000 WTE staff serving a c. 2.0M north-west London catchment plus tertiary specialty referrals national/international; estate covers St Mary's (incl. major-trauma centre), Charing Cross (neuroscience), Hammersmith (cardiac/renal), Queen Charlotte's & Chelsea (women's), Western Eye; c. 350,000 ED attendances/yr.",
        "legal_basis": "Local Government Finance Act 1988 (Schedule 6 — non-domestic rating) · Non-Domestic Rating (Multipliers and Private Finance) Act 2024 · Non-Domestic Rating Act 2023 · DHSC Group Accounting Manual 2024-25 · NHS Act 2006",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£6.42M"},
            {"label": "Trust scale", "value": "Five-site academic acute (St Mary's + Charing Cross + Hammersmith + Queen Charlotte's + Western Eye); c. 14,000 WTE"},
            {"label": "Major Trauma Centre", "value": "St Mary's = one of London's four MTCs — drives higher hereditament intensity at Paddington"},
            {"label": "2023 revaluation effect", "value": "Apr 2023 rating list revaluation lifted prime-London hospital RVs; transitional relief tapering"},
            {"label": "Multiplier 2024-25", "value": "Standard multiplier 54.6p; small business multiplier 49.9p — hospital hereditaments above £51k threshold use standard"},
            {"label": "VOA hereditaments", "value": "Five separate main site listings + ancillary clinic listings (Valuation Office Agency); billing authorities: Westminster, Hammersmith & Fulham, Kensington & Chelsea"},
            {"label": "Mandatory 80% relief", "value": "Not applicable — NHS trusts are not registered charities"},
            {"label": "Listed-building context", "value": "Charing Cross + St Mary's heritage / listed elements affect hereditament treatment but not rate liability"},
            {"label": "Funding trajectory", "value": "2021-22 c. £5.4M → 2023-24 £6.1M (post-revaluation) → 2024-25 £6.42M"},
            {"label": "Delivery body", "value": "Trust E&F + Finance + Valuation Office Agency (HMRC) + Westminster, H&F and RBKC billing authorities"},
            {"label": "Policy owner", "value": "MHCLG (rates policy) + HM Treasury + DHSC + North West London ICB"},
            {"label": "Evaluation evidence", "value": "VOA rating list 2023; HM Treasury non-domestic rating review; Trust ARA 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2007 separate Hammersmith Hospitals + St Mary's NHS Trust rates baselines · Successor: 2026 rating list revaluation + post-2024 NDR multiplier reform"}
        ],
        "notes": "Imperial's business-rates baseline reflects the trust's five-site prime-London estate consolidated by the 2007 merger of Hammersmith Hospitals NHS Trust with St Mary's NHS Trust — placing some of the NHS's highest hereditament RVs across Westminster, H&F and RBKC billing authorities. The April 2023 rating list revaluation lifted RVs across central and west London hospital hereditaments, with transitional relief tapering through 2024-25. NHS trusts are not registered charities and therefore receive no mandatory 80% relief — full liability flows. The Non-Domestic Rating (Multipliers and Private Finance) Act 2024 and pending 2026 revaluation shape the medium-term trajectory.",
        "sources": [
            {"publisher": "Imperial College Healthcare NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.imperial.nhs.uk/about-us/our-publications"},
            {"publisher": "Valuation Office Agency", "title": "Find a business rates valuation (rating list 2023)", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "Ministry of Housing, Communities and Local Government", "title": "Business rates: rating multiplier 2024-25", "url": "https://www.gov.uk/government/publications/business-rates-the-rating-multiplier"},
            {"publisher": "HM Treasury", "title": "Non-Domestic Rating Act 2023 + 2024 reform", "url": "https://www.gov.uk/government/publications/business-rates-review-final-report"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"}
        ],
        "related": ["Imperial College Healthcare NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Business rates — Liverpool University Hospitals NHS Foundation Trust", "Business rates — North Bristol NHS Trust", "Valuation Office Agency"]
    },
    "Establishment costs — Portsmouth Hospitals University NHS Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "Portsmouth Hospitals University NHS Trust"}],
        "description": "PHU's £6.42M establishment costs line covers training, professional development, recruitment, printing, postage, telecoms, subscriptions, agency-finder fees and corporate-services running costs supporting the c. 8,500-WTE workforce at Queen Alexandra Hospital (PFI-built, opened 2009) plus ancillary clinic estate. The line is structurally elevated by the trust's University status (academic-partnership administration), Frontline Digitisation EPR training/change-management, and 2023-24 industrial-action backfill recruitment driving agency-finder fees through the establishment line.",
        "beneficiaries": "c. 8,500 WTE staff serving a c. 675,000 Portsmouth, south-east Hampshire and Isle of Wight catchment within Hampshire and Isle of Wight ICS; c. 165,000 ED attendances/yr at Queen Alexandra ED — among South East's busiest single-site EDs; c. 80,000 admissions/yr; large maternity service.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25 · Equality Act 2010 (training duty)",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£6.42M"},
            {"label": "Trust scale", "value": "Single main acute site (Queen Alexandra Hospital, Cosham) + ancillary clinics; c. 8,500 WTE"},
            {"label": "Queen Alexandra PFI", "value": "Opened 2009 — Carillion-led consortium build; FM novation post-Carillion 2018 collapse to Engie/Equans drives ongoing FM contract-management establishment overhead"},
            {"label": "University status", "value": "PHU title from 2021 — academic-partnership with University of Portsmouth + KSS Deanery — drives education + training establishment baseline"},
            {"label": "Frontline Digitisation effect", "value": "EPR training + change-management feeds establishment line via agency-finder + corporate-training spend"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove agency-finder fee + recruitment establishment churn"},
            {"label": "Apr 2025 NIC + CPI uplift", "value": "Employer-NIC step-up + non-clinical CPI feed forward unit-cost pressure on establishment running costs"},
            {"label": "ED throughput", "value": "c. 165,000 attendances/yr — among South East's busiest single-site EDs"},
            {"label": "Funding trajectory", "value": "2021-22 c. £5.0M → 2023-24 £6.0M → 2024-25 £6.42M — strikes + Frontline Digitisation training driving uplift"},
            {"label": "Delivery body", "value": "Trust HR + Comms + IT + Finance + agency-finder framework providers + telecoms + printing contractors"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + NHSE Workforce + Hampshire and Isle of Wight ICB"},
            {"label": "Evaluation evidence", "value": "CQC inspection RHU; Carter / Lord review legacy non-pay benchmarks; Model Hospital corporate-services benchmarks; Trust ARA disclosure"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2009 multi-site Portsmouth (St Mary's + QA Cosham) baselines · Successor: continued NHP / digitisation-driven training cycle + post-Apr 2025 NIC environment"}
        ],
        "notes": "PHU's establishment costs line reflects the consolidation of multiple Portsmouth acute sites onto Queen Alexandra Hospital following the PFI's 2009 opening (Carillion-led consortium build, FM novation to Engie/Equans after Carillion's Jan 2018 collapse). The trust's University status from 2021 broadens the academic-partnership administration footprint, lifting education and training establishment costs versus non-University DGH peers. Frontline Digitisation EPR training and change-management costs feed via corporate-training spend. Industrial action 2023-24 drove agency-finder fees and recruitment establishment churn. April 2025 employer-NIC step-up affects pass-through on establishment contractor pricing.",
        "sources": [
            {"publisher": "Portsmouth Hospitals University NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.porthosp.nhs.uk/about-us/our-publications.htm"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://transform.england.nhs.uk/digitise-connect-transform/frontline-digitisation/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "National Audit Office", "title": "Investigation into the rescue of Carillion's PFI hospital contracts", "url": "https://www.nao.org.uk/reports/investigation-into-the-rescue-of-carillions-pfi-hospital-contracts/"},
            {"publisher": "Care Quality Commission", "title": "Portsmouth Hospitals University provider profile (RHU)", "url": "https://www.cqc.org.uk/provider/RHU"}
        ],
        "related": ["Portsmouth Hospitals University NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Establishment costs — Homerton Healthcare NHS Foundation Trust", "Establishment costs — The Mid Yorkshire Hospitals NHS Trust", "Department of Health and Social Care"]
    },
    "General supplies & services — Northern Lincolnshire and Goole NHS Foundation Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "Northern Lincolnshire and Goole NHS Foundation Trust"}],
        "description": "NLAG's £6.40M general supplies & services line covers non-clinical consumables, linen, catering provisions, hotel-services materials, IT consumables, office supplies and minor expensed equipment across Diana, Princess of Wales Hospital (Grimsby), Scunthorpe General Hospital and Goole and District Hospital. The trust operates a three-site DGH model in the Humber and North Yorkshire ICS with a Hospital Group Model arrangement with Hull University Teaching Hospitals — driving collaborative procurement scaling alongside NHS Supply Chain framework spend.",
        "beneficiaries": "c. 6,500 WTE staff serving a c. 410,000 north Lincolnshire + East Riding catchment within Humber and North Yorkshire ICS; c. 160,000 ED attendances/yr (Grimsby + Scunthorpe EDs); c. 70,000 admissions/yr.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 2 Inventories · Procurement Act 2023 · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "General supplies & services 2024-25", "value": "£6.40M"},
            {"label": "Trust scale", "value": "Three-site acute (Diana Princess of Wales Grimsby + Scunthorpe + Goole); c. 6,500 WTE"},
            {"label": "Hospital Group Model", "value": "Group arrangement with Hull University Teaching Hospitals NHS Trust under Humber Acute Services collaboration"},
            {"label": "ED throughput", "value": "c. 160,000 attendances/yr (Grimsby + Scunthorpe EDs)"},
            {"label": "Procurement route", "value": "NHS Supply Chain national framework + Humber Acute Services collaborative + trust-direct contracts"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove cancellation re-stocking + agency backfill consumable churn"},
            {"label": "April 2025 NIC + CPI uplift", "value": "Employer-NIC step-up + non-clinical CPI feed forward unit-cost pressure on contractor pass-through"},
            {"label": "CQC special-measures legacy", "value": "Trust exited recurring special-measures cycles 2018-21 — drove residual quality + governance establishment-spend interaction with consumables baseline"},
            {"label": "Funding trajectory", "value": "2021-22 c. £5.4M → 2023-24 £6.2M → 2024-25 £6.40M — sustained CPI + activity recovery uplift"},
            {"label": "Delivery body", "value": "Trust Procurement + NHS Supply Chain (DHSC ALB) + Humber Acute Services collaborative + Humber and North Yorkshire ICS"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Humber and North Yorkshire ICB"},
            {"label": "Evaluation evidence", "value": "Model Hospital benchmarks; CQC inspection RJL; Trust ARA 2023-24; Humber Acute Services Review business case"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2001 separate Grimsby + Scunthorpe baselines · Successor: continued Humber Acute Services scaling + ICS-collaborative procurement"}
        ],
        "notes": "NLAG's general supplies & services baseline is shaped by the three-site DGH footprint across north Lincolnshire (Grimsby, Scunthorpe, Goole) and the Hospital Group Model arrangement with Hull University Teaching Hospitals NHS Trust under the Humber Acute Services collaboration — providing collaborative procurement scaling alongside NHS Supply Chain national framework spend. The trust's recurring special-measures cycles 2018-21 left residual quality-governance interaction with consumables baseline. Industrial action 2023-24 drove cancellation re-stocking and agency-backfill consumable churn. April 2025 NIC step-up and CPI feed forward through framework pricing; medium-term lever is the Humber Acute Services reconfiguration agenda.",
        "sources": [
            {"publisher": "Northern Lincolnshire and Goole NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.nlg.nhs.uk/about-us/our-publications/"},
            {"publisher": "NHS Supply Chain", "title": "Annual Report 2023-24", "url": "https://www.supplychain.nhs.uk/about-us/our-publications/"},
            {"publisher": "NHS England", "title": "Humber Acute Services Review", "url": "https://humberandnorthyorkshire.org.uk/our-work/humber-acute-services/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "NLAG provider profile (RJL)", "url": "https://www.cqc.org.uk/provider/RJL"}
        ],
        "related": ["Northern Lincolnshire and Goole NHS Foundation Trust", "Clinical Supplies & Drugs", "NHS Acute Trusts", "NHS Supply Chain", "General supplies & services — Doncaster and Bassetlaw Teaching Hospitals NHS Foundation Trust", "Hull University Teaching Hospitals NHS Trust"]
    },
    "General supplies & services — The Princess Alexandra Hospital NHS Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "The Princess Alexandra Hospital NHS Trust"}],
        "description": "PAH's £6.40M general supplies & services line covers non-clinical consumables, linen, catering provisions, hotel-services materials, IT consumables, office supplies and minor expensed equipment at the single-site Princess Alexandra Hospital (Harlow) plus Herts and Essex Hospital and St Margaret's Hospital outpatient sites. The trust is in the New Hospital Programme cohort awaiting a replacement Princess Alexandra Hospital build — current building dates from 1965 and is among the most ageing acute estates in England, driving elevated repair-related minor consumables churn.",
        "beneficiaries": "c. 3,500 WTE staff serving a c. 350,000 west Essex + east Hertfordshire catchment within Hertfordshire and West Essex ICS; c. 110,000 ED attendances/yr at Princess Alexandra ED; c. 50,000 admissions/yr; large maternity service.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 2 Inventories · Procurement Act 2023 · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "General supplies & services 2024-25", "value": "£6.40M"},
            {"label": "Trust scale", "value": "Single main acute site (Princess Alexandra Hospital, Harlow) + Herts & Essex + St Margaret's outpatient sites; c. 3,500 WTE"},
            {"label": "New Hospital Programme cohort", "value": "Princess Alexandra Hospital scheme in NHP cohort — 1965 building among most ageing acute estates in England awaiting replacement"},
            {"label": "Ageing-estate effect", "value": "1965 building drives elevated repair-related minor consumables churn vs peer DGH baseline"},
            {"label": "ED throughput", "value": "c. 110,000 attendances/yr"},
            {"label": "Procurement route", "value": "NHS Supply Chain national framework + Hertfordshire & West Essex ICS collaborative + trust-direct contracts"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove cancellation re-stocking + agency backfill consumable churn"},
            {"label": "April 2025 NIC + CPI uplift", "value": "Employer-NIC step-up + non-clinical CPI feed forward unit-cost pressure on contractor pass-through"},
            {"label": "Funding trajectory", "value": "2021-22 c. £5.4M → 2023-24 £6.2M → 2024-25 £6.40M — sustained CPI + activity recovery + ageing-estate repair churn"},
            {"label": "Delivery body", "value": "Trust Procurement + NHS Supply Chain (DHSC ALB) + Hertfordshire & West Essex ICS collaborative"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Hertfordshire and West Essex ICB"},
            {"label": "Evaluation evidence", "value": "Model Hospital benchmarks; CQC inspection RQW; Trust ARA 2023-24; NHP business case"},
            {"label": "Predecessor / successor", "value": "Predecessor: 1965 Princess Alexandra Hospital baseline · Successor: post-NHP rebuild consumables baseline (NHP Reset 2025 cohort)"}
        ],
        "notes": "PAH's general supplies & services baseline is shaped by the single-site DGH operation at one of the most ageing acute estates in England — the 1965-built Princess Alexandra Hospital was placed in the New Hospital Programme cohort with replacement build pending under the post-2025 NHP Reset prioritisation. Repair-related minor consumables churn linked to the ageing estate sits above peer DGH baseline. Industrial action 2023-24 drove cancellation re-stocking and agency-backfill consumable use. April 2025 NIC step-up and CPI feed forward through framework pricing. The post-NHP rebuild will reset the trajectory once the replacement build delivers.",
        "sources": [
            {"publisher": "The Princess Alexandra Hospital NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.pah.nhs.uk/about-us/our-publications/annual-reports/"},
            {"publisher": "NHS Supply Chain", "title": "Annual Report 2023-24", "url": "https://www.supplychain.nhs.uk/about-us/our-publications/"},
            {"publisher": "NHS England", "title": "New Hospital Programme — Princess Alexandra Hospital", "url": "https://www.england.nhs.uk/new-hospital-programme/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Princess Alexandra Hospital provider profile (RQW)", "url": "https://www.cqc.org.uk/provider/RQW"}
        ],
        "related": ["The Princess Alexandra Hospital NHS Trust", "Clinical Supplies & Drugs", "NHS Acute Trusts", "NHS Supply Chain", "General supplies & services — Northern Lincolnshire and Goole NHS Foundation Trust", "New Hospital Programme"]
    },
    "PFI / LIFT charges — Maidstone And Tunbridge Wells NHS Trust": {
        "aliases": [{"name": "PFI / LIFT charges", "parent": "Maidstone And Tunbridge Wells NHS Trust"}],
        "description": "MTW's £6.37M PFI charge reflects the unitary-charge pass-through on the Tunbridge Wells Hospital at Pembury PFI (signed 2007, operational 2011) — a c. £225M Grade-A all-single-room acute build, one of the first NHS PFI hospitals constructed entirely with single en-suite rooms. The contract was originally with Equion / John Laing consortium with hard-FM and soft-FM via Equans (post-Carillion era subcontractor adjustments), and runs to 2041. The line covers debt service, lifecycle and indexed soft-FM components for the Pembury site within the trust's two-site footprint.",
        "beneficiaries": "c. 6,500 WTE staff serving a c. 600,000 west Kent + East Sussex catchment (Tunbridge Wells, Maidstone, Sevenoaks, Tonbridge); c. 160,000 ED attendances/yr (Tunbridge Wells Pembury + Maidstone EDs); c. 75,000 admissions/yr; PFI estate covers Tunbridge Wells Hospital at Pembury (main acute site, 512 beds, all-single-room).",
        "legal_basis": "IFRIC 12 Service Concession Arrangements · IFRS 16 Leases (post-2022 transition for service-concession components) · DHSC Group Accounting Manual 2024-25 ch.7 · Private Finance Initiative guidance (HM Treasury) · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "PFI / LIFT charges 2024-25", "value": "£6.37M"},
            {"label": "PFI vehicle", "value": "Tunbridge Wells Hospital at Pembury PFI signed 2007, operational Sep 2011; SPV Hospital Company (Pembury) Ltd — Equion / John Laing consortium"},
            {"label": "Contract end date", "value": "c. 2041 (30-year operational concession)"},
            {"label": "All-single-room build", "value": "First major NHS PFI hospital built entirely with single en-suite rooms (512 beds) — drives elevated soft-FM unitary baseline"},
            {"label": "Capital value", "value": "c. £225M build cost — relatively contained vs peer-cohort PFIs"},
            {"label": "Estate covered", "value": "Tunbridge Wells Hospital at Pembury (main acute, 512 beds); Maidstone Hospital is non-PFI separately funded"},
            {"label": "Unitary charge composition", "value": "Senior + subordinated debt service + lifecycle hard-FM + indexed soft-FM (cleaning, catering, portering)"},
            {"label": "Indexation mechanism", "value": "RPI-linked annual uplift on indexed components per concession agreement"},
            {"label": "Funding trajectory", "value": "Mature PFI in stable annual range £6-7M for the £6.37M accounted line element after IFRS 16 split"},
            {"label": "Delivery body", "value": "Hospital Company (Pembury) SPV + Equans (hard + soft FM) + trust E&F oversight"},
            {"label": "Policy owner", "value": "DHSC + HM Treasury PFI guidance + NHSE Provider Finance + Kent and Medway ICB"},
            {"label": "Evaluation evidence", "value": "NAO PFI 2018 + PFI hand-back report 2020; CQC inspection RWF; Trust ARA disclosure"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2011 Kent & Sussex Hospital + Pembury Hospital legacy estates · Successor: 2041 hand-back + post-PFI public-sector ownership"}
        ],
        "notes": "MTW's Pembury PFI is notable as one of the first NHS hospitals built entirely with single en-suite rooms — the 2007-signed, 2011-operational Tunbridge Wells Hospital at Pembury replaced the legacy Kent & Sussex Hospital and the older Pembury site, with the all-single-room design driving elevated soft-FM unitary baseline relative to multi-bed-bay peer PFIs. The contract runs to 2041 with RPI-linked uplifts on indexed soft-FM components. The IFRS 16 2022 transition and DHSC GAM ch.7 split reshaped the headline figure but not the underlying obligation. Hand-back planning is on the medium-term horizon (2041), with HMT/IPA PFI Hand-Back Resource Centre engagement governing the path. April 2025 NIC step-up affects FM-contractor pass-through but is not directly indexed in PFI components.",
        "sources": [
            {"publisher": "Maidstone And Tunbridge Wells NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.mtw.nhs.uk/about-us/publications/annual-report/"},
            {"publisher": "National Audit Office", "title": "PFI and PF2 (HC 718, 2018)", "url": "https://www.nao.org.uk/reports/pfi-and-pf2/"},
            {"publisher": "National Audit Office", "title": "Managing PFI assets and services as contracts end", "url": "https://www.nao.org.uk/reports/managing-pfi-assets-and-services-as-contracts-end/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 7 — Leases and service concessions)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "MTW provider profile (RWF)", "url": "https://www.cqc.org.uk/provider/RWF"}
        ],
        "related": ["Maidstone And Tunbridge Wells NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "PFI / LIFT charges — Sherwood Forest Hospitals NHS Foundation Trust", "PFI / LIFT charges — Worcestershire Acute Hospitals NHS Trust", "Department of Health and Social Care"]
    },
    "Amortisation — St George's University Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Amortisation", "parent": "St George's University Hospitals NHS Foundation Trust"}],
        "description": "St George's £6.33M amortisation line covers IAS 38 charges on intangible assets — capitalised software, EPR licences and development costs — across the St George's Hospital (Tooting) + Queen Mary's Hospital (Roehampton) footprint. Operating under the GESH (St George's, Epsom and St Helier) hospital group arrangement from 2024, the trust runs Cerner / Oracle Health EPR with Frontline Digitisation cohort additions feeding the IAS 38 charge. St George's tertiary trauma + cardiac + neuroscience services drive specialty clinical-systems capitalisation alongside generic EPR.",
        "beneficiaries": "c. 9,500 WTE staff serving a c. 1.3M south-west London catchment plus regional tertiary referrals; c. 230,000 ED attendances/yr at St George's ED — South West London Major Trauma Centre; c. 100,000 admissions/yr; specialty regional services in cardiac, neuroscience, stroke.",
        "legal_basis": "IAS 38 Intangible Assets · DHSC Group Accounting Manual 2024-25 ch.5 (intangible assets) · NHS Act 2006 · Health and Care Act 2022 · Companies Act 2006 (FT accounts framework)",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£6.33M"},
            {"label": "Trust scale", "value": "Two-site academic acute (St George's Tooting + Queen Mary's Roehampton); c. 9,500 WTE"},
            {"label": "Major Trauma Centre", "value": "St George's = South West London MTC — drives specialty trauma + clinical-systems capitalisation"},
            {"label": "GESH group model", "value": "St George's, Epsom and St Helier hospital group arrangement (operational from 2024) — shared CEO + group corporate functions; medium-term shared-systems capitalisation pathway"},
            {"label": "Frontline Digitisation effect", "value": "Cerner / Oracle Health EPR + Frontline Digitisation programme drive post-2020 capitalised intangible additions"},
            {"label": "IAS 38 useful-life policy", "value": "Software typically 3-7 years; major EPR systems 5-10 years per DHSC GAM"},
            {"label": "Capitalisation threshold", "value": "Trust capitalisation policy c. £5,000 per item per GAM guidance"},
            {"label": "Tertiary specialty load", "value": "Cardiac, neuroscience, stroke regional services drive specialty clinical-systems intangibles"},
            {"label": "Funding trajectory", "value": "2021-22 c. £4.5M → 2023-24 £5.8M → 2024-25 £6.33M — Frontline Digitisation cohort additions feeding through"},
            {"label": "Delivery body", "value": "Trust IT + Finance + EPR provider (Cerner / Oracle Health) + NHSE Frontline Digitisation programme"},
            {"label": "Policy owner", "value": "DHSC + NHSE Frontline Digitisation + South West London ICB"},
            {"label": "Evaluation evidence", "value": "NHSE Frontline Digitisation programme reviews; NAO digital transformation in NHS reports; CQC inspection RJ7; Trust ARA note 14 (intangible assets)"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2024 stand-alone St George's amortisation profile · Successor: GESH group shared-systems amortisation pathway + continued Frontline Digitisation cohort additions"}
        ],
        "notes": "St George's amortisation line reflects the trust's tertiary academic profile — Major Trauma Centre status at Tooting and regional cardiac, neuroscience and stroke services drive specialty clinical-systems capitalisation alongside generic Cerner / Oracle Health EPR. The GESH (St George's, Epsom and St Helier) group model arrangement from 2024 — sharing CEO and group corporate functions under SWL ICS — sets up a medium-term shared-systems capitalisation pathway that will reshape post-2025 amortisation profiles. Cerner / Oracle Health EPR licensing capitalised under DHSC GAM ch.5 typically uses 5-10 year useful lives. Forward trajectory continues elevated as Frontline Digitisation cohort feeds through.",
        "sources": [
            {"publisher": "St George's University Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.stgeorges.nhs.uk/about/our-publications/"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://transform.england.nhs.uk/digitise-connect-transform/frontline-digitisation/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 5 — intangible assets)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "National Audit Office", "title": "Digital transformation in the NHS", "url": "https://www.nao.org.uk/reports/the-digital-transformation-in-the-nhs/"},
            {"publisher": "Care Quality Commission", "title": "St George's provider profile (RJ7)", "url": "https://www.cqc.org.uk/provider/RJ7"}
        ],
        "related": ["St George's University Hospitals NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Amortisation — Chelsea and Westminster Hospital NHS Foundation Trust", "Amortisation — Nottingham University Hospitals NHS Trust", "Epsom and St Helier University Hospitals NHS Trust"]
    },
    "Business rates — Mid and South Essex NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "Mid and South Essex NHS Foundation Trust"}],
        "description": "MSE's £6.33M business rates line covers non-domestic rating liability under the Local Government Finance Act 1988 across the three-site footprint — Basildon University Hospital, Broomfield Hospital (Chelmsford) and Southend University Hospital. The 2023 rating list revaluation lifted hereditament RVs for Essex healthcare premises, and three large acute hereditaments across three billing authorities (Basildon, Chelmsford, Southend) drive a substantial baseline. NHS trusts are not registered charities, so no mandatory 80% relief applies.",
        "beneficiaries": "c. 14,000 WTE staff serving a c. 1.2M Mid and South Essex catchment within Mid and South Essex ICS; estate covers Basildon Hospital + Broomfield Hospital (Chelmsford) + Southend Hospital + ancillary clinic premises; c. 290,000 ED attendances/yr (three EDs combined).",
        "legal_basis": "Local Government Finance Act 1988 (Schedule 6 — non-domestic rating) · Non-Domestic Rating (Multipliers and Private Finance) Act 2024 · Non-Domestic Rating Act 2023 · DHSC Group Accounting Manual 2024-25 · NHS Act 2006",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£6.33M"},
            {"label": "Trust scale", "value": "Three-site acute (Basildon + Broomfield Chelmsford + Southend) post-2020 merger; c. 14,000 WTE"},
            {"label": "Merger context", "value": "Apr 2020 merger of Basildon + Broomfield + Southend trusts to form MSE — consolidated three large hereditaments under single trust"},
            {"label": "2023 revaluation effect", "value": "Apr 2023 rating list revaluation lifted RVs across Essex healthcare hereditaments; transitional relief tapering"},
            {"label": "Multiplier 2024-25", "value": "Standard multiplier 54.6p; small business multiplier 49.9p — hospital hereditaments above £51k threshold use standard"},
            {"label": "VOA hereditaments", "value": "Three main site listings + ancillary clinic listings (Valuation Office Agency); billing authorities: Basildon Borough, Chelmsford City, Southend-on-Sea City"},
            {"label": "Mandatory 80% relief", "value": "Not applicable — NHS trusts are not registered charities"},
            {"label": "Burns + cardiothoracic specialty", "value": "Broomfield burns service + Basildon cardiothoracic service drive specialty hereditament treatment"},
            {"label": "Funding trajectory", "value": "2021-22 c. £5.5M → 2023-24 £6.1M (post-revaluation full year) → 2024-25 £6.33M"},
            {"label": "Delivery body", "value": "Trust E&F + Finance + Valuation Office Agency (HMRC) + Basildon, Chelmsford, Southend billing authorities"},
            {"label": "Policy owner", "value": "MHCLG (rates policy) + HM Treasury + DHSC + Mid and South Essex ICB"},
            {"label": "Evaluation evidence", "value": "VOA rating list 2023; HM Treasury non-domestic rating review; CQC inspection RAJ; Trust ARA 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2020 separate Basildon + Broomfield + Southend rates baselines · Successor: 2026 rating list revaluation + post-2024 NDR multiplier reform"}
        ],
        "notes": "MSE's business-rates baseline reflects the April 2020 merger of Basildon, Mid Essex and Southend trusts to form Mid and South Essex NHS FT — consolidating three large acute hereditaments across Basildon, Chelmsford and Southend billing authorities under a single trust. The April 2023 rating list revaluation lifted RVs across Essex healthcare hereditaments, with transitional relief tapering through 2024-25. Broomfield's burns service and Basildon's cardiothoracic service drive specialty hereditament-treatment within VOA assessment. NHS trusts are not registered charities and receive no mandatory 80% relief. The 2024 NDR Act and pending 2026 revaluation shape the medium-term trajectory.",
        "sources": [
            {"publisher": "Mid and South Essex NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.mse.nhs.uk/about-us/our-publications/annual-reports/"},
            {"publisher": "Valuation Office Agency", "title": "Find a business rates valuation (rating list 2023)", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "Ministry of Housing, Communities and Local Government", "title": "Business rates: rating multiplier 2024-25", "url": "https://www.gov.uk/government/publications/business-rates-the-rating-multiplier"},
            {"publisher": "HM Treasury", "title": "Non-Domestic Rating Act 2023 + 2024 reform", "url": "https://www.gov.uk/government/publications/business-rates-review-final-report"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"}
        ],
        "related": ["Mid and South Essex NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Business rates — Imperial College Healthcare NHS Trust", "Business rates — Liverpool University Hospitals NHS Foundation Trust", "Valuation Office Agency"]
    },
    "Establishment costs — South Tyneside and Sunderland NHS Foundation Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "South Tyneside and Sunderland NHS Foundation Trust"}],
        "description": "STSFT's £6.27M establishment costs line covers training, professional development, recruitment, printing, postage, telecoms, subscriptions, agency-finder fees and corporate-services running costs supporting the c. 8,500-WTE workforce across Sunderland Royal Hospital, South Tyneside District Hospital and integrated community services. Formed by the 2019 merger of South Tyneside and City Hospitals Sunderland under the Path to Excellence acute-services reconfiguration, the trust's group footprint drives elevated training/recruitment establishment baseline.",
        "beneficiaries": "c. 8,500 WTE staff serving a c. 600,000 South Tyneside and Sunderland catchment within North East and North Cumbria ICS; c. 175,000 ED attendances/yr (Sunderland Royal main ED + South Tyneside ED); c. 80,000 admissions/yr; integrated community-team workforce.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25 · Equality Act 2010 (training duty)",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£6.27M"},
            {"label": "Trust scale", "value": "Two-site acute (Sunderland Royal + South Tyneside DGH) + integrated community services; c. 8,500 WTE"},
            {"label": "Path to Excellence merger", "value": "Apr 2019 merger of South Tyneside NHS FT + City Hospitals Sunderland NHS FT to form STSFT — consolidated acute-services reconfiguration under Path to Excellence programme"},
            {"label": "Frontline Digitisation effect", "value": "EPR training + change-management feeds establishment line via agency-finder + corporate-training spend"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove agency-finder fee + recruitment establishment churn"},
            {"label": "Apr 2025 NIC + CPI uplift", "value": "Employer-NIC step-up + non-clinical CPI feed forward unit-cost pressure on establishment running costs"},
            {"label": "ED throughput", "value": "c. 175,000 attendances/yr (Sunderland Royal main + South Tyneside)"},
            {"label": "Integrated community workforce", "value": "Community services across South Tyneside + Sunderland — broadens training + corporate establishment baseline"},
            {"label": "Funding trajectory", "value": "2021-22 c. £5.0M → 2023-24 £5.9M → 2024-25 £6.27M — strikes + Frontline Digitisation training driving uplift"},
            {"label": "Delivery body", "value": "Trust HR + Comms + IT + Finance + agency-finder framework providers + telecoms + printing contractors"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + NHSE Workforce + North East and North Cumbria ICB"},
            {"label": "Evaluation evidence", "value": "CQC inspection R0B; Carter / Lord review legacy non-pay benchmarks; Model Hospital corporate-services benchmarks; Path to Excellence post-merger review"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2019 separate South Tyneside + City Hospitals Sunderland baselines · Successor: continued NENC ICS workforce planning + post-Apr 2025 NIC environment"}
        ],
        "notes": "STSFT's establishment costs line reflects the April 2019 Path to Excellence merger of South Tyneside NHS FT with City Hospitals Sunderland NHS FT — consolidating acute-services reconfiguration across the two-site footprint and integrated community workforce. The integrated community-team workforce broadens the training and corporate establishment baseline versus acute-only peers of similar scale. Frontline Digitisation EPR training and change-management costs feed via corporate-training and agency-finder spend. Industrial action 2023-24 drove additional agency-finder fees and recruitment establishment churn. The April 2025 employer-NIC step-up affects pass-through on establishment contractor pricing. North East and North Cumbria ICS workforce planning shapes the medium-term path.",
        "sources": [
            {"publisher": "South Tyneside and Sunderland NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.stsft.nhs.uk/about-us/key-publications/annual-reports"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://transform.england.nhs.uk/digitise-connect-transform/frontline-digitisation/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Path to Excellence acute services reconfiguration", "url": "https://pathtoexcellence.org.uk/"},
            {"publisher": "Care Quality Commission", "title": "South Tyneside and Sunderland provider profile (R0B)", "url": "https://www.cqc.org.uk/provider/R0B"}
        ],
        "related": ["South Tyneside and Sunderland NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Establishment costs — Portsmouth Hospitals University NHS Trust", "Establishment costs — Homerton Healthcare NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "General supplies & services — Ashford and St Peter's Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "Ashford and St Peter's Hospitals NHS Foundation Trust"}],
        "description": "ASPH's £6.27M general supplies & services line covers non-clinical consumables, linen, catering provisions, hotel-services materials, IT consumables, office supplies and minor expensed equipment across the two-site Ashford Hospital + St Peter's Hospital (Chertsey) footprint serving north-west Surrey. The trust runs Surrey Heartlands ICS-aligned procurement collaborative scaling alongside NHS Supply Chain national framework spend, with consumables baseline shaped by the c. 130,000-attendance ED at St Peter's and large maternity service.",
        "beneficiaries": "c. 4,500 WTE staff serving a c. 410,000 north-west Surrey catchment (Runnymede, Spelthorne, Surrey Heath, Woking) within Surrey Heartlands ICS; c. 130,000 ED attendances/yr (St Peter's main ED + Ashford Walk-in); c. 65,000 admissions/yr; large maternity service.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 2 Inventories · Procurement Act 2023 · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "General supplies & services 2024-25", "value": "£6.27M"},
            {"label": "Trust scale", "value": "Two-site DGH (St Peter's Chertsey + Ashford); c. 4,500 WTE"},
            {"label": "ED throughput", "value": "c. 130,000 attendances/yr (St Peter's main + Ashford Walk-in)"},
            {"label": "Procurement route", "value": "NHS Supply Chain national framework + Surrey Heartlands ICS collaborative + trust-direct contracts"},
            {"label": "Surrey Heartlands collaborative", "value": "Multi-trust procurement collaborative under Surrey Heartlands ICS — scales NHS Supply Chain framework + bespoke trust deals"},
            {"label": "April 2025 NIC + CPI uplift", "value": "Employer-NIC step-up + non-clinical CPI feed forward unit-cost pressure on contractor pass-through"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove cancellation re-stocking + agency backfill consumable churn"},
            {"label": "Capitalisation threshold", "value": "Trust capitalisation policy c. £5,000 per item per GAM guidance — items below expensed through this line"},
            {"label": "Funding trajectory", "value": "2021-22 c. £5.3M → 2023-24 £6.0M → 2024-25 £6.27M — sustained CPI + activity recovery uplift"},
            {"label": "Delivery body", "value": "Trust Procurement + NHS Supply Chain (DHSC ALB) + Surrey Heartlands ICS collaborative"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Surrey Heartlands ICB"},
            {"label": "Evaluation evidence", "value": "Model Hospital benchmarks; CQC inspection RTK; Trust ARA 2023-24; Surrey Heartlands ICS procurement plan"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-1998 separate Ashford + St Peter's baselines · Successor: continued NHS Supply Chain + Surrey Heartlands ICS scaling"}
        ],
        "notes": "ASPH's general supplies & services baseline is shaped by the two-site DGH operation (Ashford and St Peter's, Chertsey) serving north-west Surrey within Surrey Heartlands ICS. The Surrey Heartlands ICS-aligned procurement collaborative scales NHS Supply Chain national framework spend alongside trust-direct contracts. Industrial action 2023-24 drove cancellation re-stocking and agency-backfill consumable churn across emergency medicine and surgical rotas. April 2025 NIC step-up and CPI feed forward through framework pricing and trust-direct contractor pass-through; medium-term lever is deeper Surrey Heartlands collaborative scaling.",
        "sources": [
            {"publisher": "Ashford and St Peter's Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.ashfordstpeters.nhs.uk/annual-reports"},
            {"publisher": "NHS Supply Chain", "title": "Annual Report 2023-24", "url": "https://www.supplychain.nhs.uk/about-us/our-publications/"},
            {"publisher": "Surrey Heartlands Integrated Care System", "title": "ICS strategy + procurement plan", "url": "https://www.surreyheartlands.org/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "ASPH provider profile (RTK)", "url": "https://www.cqc.org.uk/provider/RTK"}
        ],
        "related": ["Ashford and St Peter's Hospitals NHS Foundation Trust", "Clinical Supplies & Drugs", "NHS Acute Trusts", "NHS Supply Chain", "General supplies & services — The Princess Alexandra Hospital NHS Trust", "Social security & levy — Ashford and St Peter's Hospitals NHS Foundation Trust"]
    },
    "General supplies & services — Northern Care Alliance NHS Foundation Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "Northern Care Alliance NHS Foundation Trust"}],
        "description": "NCA's £6.25M general supplies & services line covers non-clinical consumables, linen, catering provisions, hotel-services materials, IT consumables, office supplies and minor expensed equipment across the four-site group footprint — Salford Royal, Royal Oldham, Fairfield General (Bury) and Rochdale Infirmary. NCA is one of England's largest acute trusts following the 2021 reorganisation that transferred Pennine Acute Hospitals' non-Manchester sites into Salford Royal NHS FT to form Northern Care Alliance — driving collaborative procurement scaling under Greater Manchester ICS.",
        "beneficiaries": "c. 19,000 WTE staff serving a c. 1.0M Salford + Oldham + Bury + Rochdale catchment within Greater Manchester ICS; c. 350,000 ED attendances/yr (Salford Royal + Royal Oldham + Fairfield + Rochdale UTC); c. 150,000 admissions/yr; tertiary services in neuroscience + intestinal failure at Salford Royal.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 2 Inventories · Procurement Act 2023 · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "General supplies & services 2024-25", "value": "£6.25M"},
            {"label": "Trust scale", "value": "Four-site acute (Salford Royal + Royal Oldham + Fairfield + Rochdale Infirmary); c. 19,000 WTE — among England's largest"},
            {"label": "2021 reorganisation", "value": "Oct 2021 transfer of Pennine Acute Hospitals' non-Manchester sites (Oldham, Bury, Rochdale) into Salford Royal NHS FT to form NCA"},
            {"label": "Tertiary specialty load", "value": "Salford Royal = North West tertiary neuroscience + intestinal failure centre — drives specialty consumables capitalisation"},
            {"label": "Procurement route", "value": "NHS Supply Chain national framework + Greater Manchester ICS collaborative + trust-direct contracts"},
            {"label": "Greater Manchester collaborative", "value": "GM provider collaborative procurement scaling — covers NCA + MFT + Bolton + Tameside + Wrightington under GM ICS"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove cancellation re-stocking + agency backfill consumable churn"},
            {"label": "April 2025 NIC + CPI uplift", "value": "Employer-NIC step-up + non-clinical CPI feed forward unit-cost pressure on contractor pass-through"},
            {"label": "Funding trajectory", "value": "2021-22 c. £5.3M (post-reorg first year) → 2023-24 £6.0M → 2024-25 £6.25M"},
            {"label": "Delivery body", "value": "Trust Procurement + NHS Supply Chain (DHSC ALB) + Greater Manchester ICS collaborative"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Greater Manchester ICB"},
            {"label": "Evaluation evidence", "value": "Model Hospital benchmarks; CQC inspection R0A; Trust ARA 2023-24; GM ICS procurement plan"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2021 separate Salford Royal + Pennine Acute baselines · Successor: continued GM ICS collaborative scaling"}
        ],
        "notes": "NCA's general supplies & services baseline reflects the October 2021 reorganisation transferring Pennine Acute Hospitals' Oldham, Bury and Rochdale sites into Salford Royal NHS FT — forming Northern Care Alliance as one of England's largest acute trusts. Salford Royal's tertiary North West neuroscience and national intestinal failure centre drive specialty consumables alongside generic non-clinical baseline across the four-site group footprint. The Greater Manchester ICS provider-collaborative procurement — alongside MFT, Bolton, Tameside, Wrightington — provides scaling beyond NHS Supply Chain framework. Industrial action 2023-24 drove cancellation re-stocking and agency-backfill churn. April 2025 NIC + CPI feed forward.",
        "sources": [
            {"publisher": "Northern Care Alliance NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.northerncarealliance.nhs.uk/about-us/key-publications"},
            {"publisher": "NHS Supply Chain", "title": "Annual Report 2023-24", "url": "https://www.supplychain.nhs.uk/about-us/our-publications/"},
            {"publisher": "Greater Manchester Integrated Care", "title": "GM ICS strategy + provider collaborative procurement", "url": "https://gmintegratedcare.org.uk/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Northern Care Alliance provider profile (R0A)", "url": "https://www.cqc.org.uk/provider/R0A"}
        ],
        "related": ["Northern Care Alliance NHS Foundation Trust", "Clinical Supplies & Drugs", "NHS Acute Trusts", "NHS Supply Chain", "General supplies & services — Ashford and St Peter's Hospitals NHS Foundation Trust", "Manchester University NHS Foundation Trust"]
    },
    "Amortisation — Imperial College Healthcare NHS Trust": {
        "aliases": [{"name": "Amortisation", "parent": "Imperial College Healthcare NHS Trust"}],
        "description": "Imperial's £6.23M amortisation line covers IAS 38 charges on intangible assets — capitalised software, EPR licences, capitalised development costs and licensing rights — across the trust's five-site footprint (St Mary's, Charing Cross, Hammersmith, Queen Charlotte's & Chelsea, Western Eye). As one of the NHS's leading academic medical centres, Imperial runs Cerner / Oracle Health EPR plus extensive specialty clinical-systems intangibles supporting tertiary cardiac, neuroscience and major-trauma services. Frontline Digitisation cohort additions feed the IAS 38 charge.",
        "beneficiaries": "c. 14,000 WTE staff serving a c. 2.0M north-west London catchment plus tertiary specialty referrals national/international; c. 350,000 ED attendances/yr (St Mary's, Charing Cross, Hammersmith); c. 200,000 admissions/yr; St Mary's Major Trauma Centre + Hammersmith cardiac/renal tertiary + Charing Cross neuroscience.",
        "legal_basis": "IAS 38 Intangible Assets · DHSC Group Accounting Manual 2024-25 ch.5 (intangible assets) · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£6.23M"},
            {"label": "Trust scale", "value": "Five-site academic acute (St Mary's + Charing Cross + Hammersmith + Queen Charlotte's + Western Eye); c. 14,000 WTE"},
            {"label": "Major Trauma Centre", "value": "St Mary's = one of London's four MTCs — drives specialty trauma + clinical-systems capitalisation"},
            {"label": "Imperial College academic partnership", "value": "Joint working with Imperial College London — drives capitalised research/clinical-systems integration intangibles"},
            {"label": "Frontline Digitisation effect", "value": "Cerner / Oracle Health EPR + Frontline Digitisation programme drive post-2020 capitalised intangible additions"},
            {"label": "IAS 38 useful-life policy", "value": "Software typically 3-7 years; major EPR systems 5-10 years per DHSC GAM"},
            {"label": "Capitalisation threshold", "value": "Trust capitalisation policy c. £5,000 per item per GAM guidance"},
            {"label": "Tertiary specialty load", "value": "Cardiac (Hammersmith), neuroscience (Charing Cross), trauma (St Mary's) — drive specialty clinical-systems intangibles"},
            {"label": "Funding trajectory", "value": "2021-22 c. £4.5M → 2023-24 £5.7M → 2024-25 £6.23M — Frontline Digitisation cohort additions feeding through"},
            {"label": "Delivery body", "value": "Trust IT + Finance + EPR provider (Cerner / Oracle Health) + NHSE Frontline Digitisation programme"},
            {"label": "Policy owner", "value": "DHSC + NHSE Frontline Digitisation + North West London ICB"},
            {"label": "Evaluation evidence", "value": "NHSE Frontline Digitisation programme reviews; NAO digital transformation in NHS reports; CQC inspection RYJ; Trust ARA note 14 (intangible assets)"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2007 separate Hammersmith Hospitals + St Mary's amortisation profiles · Successor: continued Frontline Digitisation cohort additions + NWL ICS shared-systems pathway"}
        ],
        "notes": "Imperial's amortisation line reflects the trust's status as one of the NHS's leading academic medical centres — five-site academic acute footprint consolidated by the 2007 merger of Hammersmith Hospitals with St Mary's NHS Trust, Major Trauma Centre status at St Mary's, and tertiary cardiac (Hammersmith), neuroscience (Charing Cross) and renal services driving specialty clinical-systems capitalisation alongside generic Cerner / Oracle Health EPR. The Imperial College London academic partnership drives capitalised research/clinical-systems integration intangibles. EPR licensing capitalised under DHSC GAM ch.5 typically uses 5-10 year useful lives. Forward trajectory continues elevated through 2026.",
        "sources": [
            {"publisher": "Imperial College Healthcare NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.imperial.nhs.uk/about-us/our-publications"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://transform.england.nhs.uk/digitise-connect-transform/frontline-digitisation/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 5 — intangible assets)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "National Audit Office", "title": "Digital transformation in the NHS", "url": "https://www.nao.org.uk/reports/the-digital-transformation-in-the-nhs/"},
            {"publisher": "Care Quality Commission", "title": "Imperial College Healthcare provider profile (RYJ)", "url": "https://www.cqc.org.uk/provider/RYJ"}
        ],
        "related": ["Imperial College Healthcare NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Amortisation — St George's University Hospitals NHS Foundation Trust", "Amortisation — Chelsea and Westminster Hospital NHS Foundation Trust", "Business rates — Imperial College Healthcare NHS Trust"]
    },
    "General supplies & services — University Hospitals Coventry And Warwickshire NHS Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "University Hospitals Coventry And Warwickshire NHS Trust"}],
        "description": "UHCW's £6.20M general supplies & services line covers non-clinical consumables, linen, catering provisions, hotel-services materials, IT consumables, office supplies and minor expensed equipment across University Hospital Coventry (Walsgrave PFI, opened 2006) and Hospital of St Cross (Rugby). The trust runs the West Midlands tertiary cardiac centre and major-trauma centre at Coventry, driving specialty consumables baseline alongside generic non-clinical baseline. Coventry & Warwickshire ICS-aligned procurement collaborative scaling supplements NHS Supply Chain national framework.",
        "beneficiaries": "c. 10,500 WTE staff serving a c. 1.0M Coventry, Rugby and Warwickshire catchment within Coventry & Warwickshire ICS; c. 200,000 ED attendances/yr at University Hospital Coventry — West Midlands Major Trauma Centre + tertiary cardiac centre; c. 90,000 admissions/yr.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 2 Inventories · Procurement Act 2023 · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "General supplies & services 2024-25", "value": "£6.20M"},
            {"label": "Trust scale", "value": "Two-site acute (University Hospital Coventry + Hospital of St Cross Rugby); c. 10,500 WTE"},
            {"label": "Walsgrave PFI", "value": "University Hospital Coventry built under PFI signed 2002, operational 2006 (Project Co Coventry & Rugby Hospital Company)"},
            {"label": "Tertiary specialty load", "value": "West Midlands Major Trauma Centre + tertiary cardiac centre — drives specialty consumables baseline above peer DGH"},
            {"label": "Procurement route", "value": "NHS Supply Chain national framework + Coventry & Warwickshire ICS collaborative + trust-direct contracts"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove cancellation re-stocking + agency backfill consumable churn"},
            {"label": "April 2025 NIC + CPI uplift", "value": "Employer-NIC step-up + non-clinical CPI feed forward unit-cost pressure on contractor pass-through"},
            {"label": "ED throughput", "value": "c. 200,000 attendances/yr — among West Midlands' busiest"},
            {"label": "Funding trajectory", "value": "2021-22 c. £5.3M → 2023-24 £6.0M → 2024-25 £6.20M — sustained CPI + activity recovery uplift"},
            {"label": "Delivery body", "value": "Trust Procurement + NHS Supply Chain (DHSC ALB) + Coventry & Warwickshire ICS collaborative"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Coventry and Warwickshire ICB"},
            {"label": "Evaluation evidence", "value": "Model Hospital benchmarks; CQC inspection RKB; Trust ARA 2023-24; Coventry & Warwickshire ICS procurement plan"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2006 Walsgrave + Coventry & Warwickshire Hospital legacy baselines · Successor: continued NHS Supply Chain + ICS collaborative scaling"}
        ],
        "notes": "UHCW's general supplies & services baseline reflects the 2006 Walsgrave PFI consolidation onto a single Coventry acute site (with Hospital of St Cross at Rugby providing local DGH services) and the tertiary West Midlands Major Trauma Centre + cardiac centre status driving specialty consumables baseline above peer DGH. The Coventry & Warwickshire ICS-aligned procurement collaborative provides scaling alongside NHS Supply Chain national framework spend. Industrial action 2023-24 drove cancellation re-stocking and agency-backfill consumable use. April 2025 NIC step-up and CPI feed forward through framework pricing; medium-term lever is deeper ICS collaborative scaling.",
        "sources": [
            {"publisher": "University Hospitals Coventry and Warwickshire NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.uhcw.nhs.uk/about-us/our-publications/annual-report/"},
            {"publisher": "NHS Supply Chain", "title": "Annual Report 2023-24", "url": "https://www.supplychain.nhs.uk/about-us/our-publications/"},
            {"publisher": "Coventry and Warwickshire Integrated Care Board", "title": "ICS strategy + procurement plan", "url": "https://www.happyhealthylives.uk/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "UHCW provider profile (RKB)", "url": "https://www.cqc.org.uk/provider/RKB"}
        ],
        "related": ["University Hospitals Coventry And Warwickshire NHS Trust", "Clinical Supplies & Drugs", "NHS Acute Trusts", "NHS Supply Chain", "General supplies & services — Northern Care Alliance NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Business rates — Northern Care Alliance NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "Northern Care Alliance NHS Foundation Trust"}],
        "description": "NCA's £6.20M business rates line covers non-domestic rating liability under the Local Government Finance Act 1988 across the four-site acute footprint — Salford Royal, Royal Oldham, Fairfield General (Bury) and Rochdale Infirmary — formed by the October 2021 reorganisation transferring Pennine Acute non-Manchester sites into Salford Royal. The 2023 revaluation lifted hereditament RVs across Greater Manchester healthcare premises, with four large hospital hereditaments across four billing authorities driving the baseline.",
        "beneficiaries": "c. 19,000 WTE staff serving a c. 1.0M Salford + Oldham + Bury + Rochdale catchment within Greater Manchester ICS; estate covers Salford Royal Hospital + Royal Oldham + Fairfield General + Rochdale Infirmary + ancillary clinic premises; c. 350,000 ED attendances/yr.",
        "legal_basis": "Local Government Finance Act 1988 (Schedule 6 — non-domestic rating) · Non-Domestic Rating (Multipliers and Private Finance) Act 2024 · Non-Domestic Rating Act 2023 · DHSC Group Accounting Manual 2024-25 · NHS Act 2006",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£6.20M"},
            {"label": "Trust scale", "value": "Four-site acute (Salford Royal + Royal Oldham + Fairfield + Rochdale Infirmary); c. 19,000 WTE"},
            {"label": "2021 reorganisation", "value": "Oct 2021 transfer of Pennine Acute Hospitals' non-Manchester sites into Salford Royal NHS FT — consolidated four large hereditaments under single trust"},
            {"label": "2023 revaluation effect", "value": "Apr 2023 rating list revaluation lifted RVs across Greater Manchester healthcare hereditaments; transitional relief tapering"},
            {"label": "Multiplier 2024-25", "value": "Standard multiplier 54.6p; small business multiplier 49.9p — hospital hereditaments above £51k threshold use standard"},
            {"label": "VOA hereditaments", "value": "Four main site listings + ancillary clinic listings (Valuation Office Agency); billing authorities: Salford City, Oldham MBC, Bury MBC, Rochdale MBC"},
            {"label": "Mandatory 80% relief", "value": "Not applicable — NHS trusts are not registered charities"},
            {"label": "Tertiary specialty", "value": "Salford Royal = North West tertiary neuroscience + intestinal failure centre — drives specialty hereditament treatment"},
            {"label": "Funding trajectory", "value": "2021-22 c. £5.4M (post-reorg first year) → 2023-24 £6.0M (post-revaluation) → 2024-25 £6.20M"},
            {"label": "Delivery body", "value": "Trust E&F + Finance + Valuation Office Agency (HMRC) + Salford, Oldham, Bury, Rochdale billing authorities"},
            {"label": "Policy owner", "value": "MHCLG (rates policy) + HM Treasury + DHSC + Greater Manchester ICB"},
            {"label": "Evaluation evidence", "value": "VOA rating list 2023; HM Treasury non-domestic rating review; CQC inspection R0A; Trust ARA 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2021 separate Salford Royal + Pennine Acute rates baselines · Successor: 2026 rating list revaluation + post-2024 NDR multiplier reform"}
        ],
        "notes": "NCA's business-rates baseline reflects the October 2021 reorganisation transferring Pennine Acute's Oldham, Bury and Rochdale sites into Salford Royal NHS FT to form NCA — consolidating four large acute hereditaments across Salford, Oldham, Bury and Rochdale billing authorities. The April 2023 rating list revaluation lifted RVs across Greater Manchester healthcare hereditaments, with transitional relief tapering through 2024-25. Salford Royal's tertiary neuroscience and intestinal failure centre drive specialty hereditament-treatment within VOA assessment. NHS trusts are not registered charities and receive no mandatory 80% relief. The 2024 NDR Act and pending 2026 revaluation shape medium-term trajectory.",
        "sources": [
            {"publisher": "Northern Care Alliance NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.northerncarealliance.nhs.uk/about-us/key-publications"},
            {"publisher": "Valuation Office Agency", "title": "Find a business rates valuation (rating list 2023)", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "Ministry of Housing, Communities and Local Government", "title": "Business rates: rating multiplier 2024-25", "url": "https://www.gov.uk/government/publications/business-rates-the-rating-multiplier"},
            {"publisher": "HM Treasury", "title": "Non-Domestic Rating Act 2023 + 2024 reform", "url": "https://www.gov.uk/government/publications/business-rates-review-final-report"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"}
        ],
        "related": ["Northern Care Alliance NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Business rates — Mid and South Essex NHS Foundation Trust", "Business rates — Imperial College Healthcare NHS Trust", "Valuation Office Agency"]
    },
    "Amortisation — West Suffolk NHS Foundation Trust": {
        "aliases": [{"name": "Amortisation", "parent": "West Suffolk NHS Foundation Trust"}],
        "description": "West Suffolk's £6.13M amortisation line covers IAS 38 charges on intangible assets — capitalised software, EPR licences and capitalised development costs — at the single-site West Suffolk Hospital (Bury St Edmunds). The hospital is in the New Hospital Programme cohort (RAAC-affected estate listed in HSSIB 2023 inventory), and the trust runs Cerner / Oracle Health EPR with substantial Frontline Digitisation cohort additions. The trust's high digital-maturity profile relative to peer DGHs lifts the intangible-asset stock and amortisation charge.",
        "beneficiaries": "c. 4,500 WTE staff serving a c. 280,000 west Suffolk catchment within Suffolk and North East Essex ICS; c. 80,000 ED attendances/yr at West Suffolk ED; c. 35,000 admissions/yr; large maternity service.",
        "legal_basis": "IAS 38 Intangible Assets · DHSC Group Accounting Manual 2024-25 ch.5 (intangible assets) · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£6.13M"},
            {"label": "Trust scale", "value": "Single acute site (West Suffolk Hospital, Bury St Edmunds); c. 4,500 WTE"},
            {"label": "RAAC + NHP context", "value": "West Suffolk Hospital listed in HSSIB Sep 2023 RAAC inventory + New Hospital Programme cohort awaiting replacement build"},
            {"label": "Frontline Digitisation effect", "value": "Cerner / Oracle Health EPR + Frontline Digitisation programme drive post-2020 capitalised intangible additions; trust digitally mature relative to peer DGH"},
            {"label": "IAS 38 useful-life policy", "value": "Software typically 3-7 years; major EPR systems 5-10 years per DHSC GAM"},
            {"label": "Capitalisation threshold", "value": "Trust capitalisation policy c. £5,000 per item per GAM guidance"},
            {"label": "Asset class breakdown", "value": "Software + EPR licences + capitalised development costs + assets under construction (in-progress amortisation begins on operational date)"},
            {"label": "ED throughput", "value": "c. 80,000 attendances/yr"},
            {"label": "Funding trajectory", "value": "2021-22 c. £4.0M → 2023-24 £5.5M → 2024-25 £6.13M — Frontline Digitisation cohort additions feeding through; relatively elevated for trust scale"},
            {"label": "Delivery body", "value": "Trust IT + Finance + EPR provider (Cerner / Oracle Health) + NHSE Frontline Digitisation programme"},
            {"label": "Policy owner", "value": "DHSC + NHSE Frontline Digitisation + Suffolk and North East Essex ICB"},
            {"label": "Evaluation evidence", "value": "NHSE Frontline Digitisation programme reviews; NAO digital transformation in NHS reports; CQC inspection RGR; Trust ARA note 14 (intangible assets); HSSIB RAAC inventory"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2020 limited intangible-asset stock · Successor: continued Frontline Digitisation cohort additions + post-NHP rebuild systems baseline"}
        ],
        "notes": "West Suffolk's amortisation line is structurally elevated for a single-site DGH of c. 4,500 WTE — reflecting the trust's relatively high digital-maturity profile with substantial Cerner / Oracle Health EPR + Frontline Digitisation cohort additions feeding the IAS 38 charge. The trust's listing in the HSSIB September 2023 RAAC inventory and New Hospital Programme cohort participation drives medium-term capitalised digital-systems additions linked to replacement-build planning. EPR licensing capitalised under DHSC GAM ch.5 typically uses 5-10 year useful lives. Post-NHP rebuild will reset systems baseline once replacement build delivers under post-2025 NHP Reset prioritisation.",
        "sources": [
            {"publisher": "West Suffolk NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.wsh.nhs.uk/About-us/Publications/Annual-Reports.aspx"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://transform.england.nhs.uk/digitise-connect-transform/frontline-digitisation/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 5 — intangible assets)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Health Services Safety Investigations Body / DHSC", "title": "RAAC NHS England estate inventory and management", "url": "https://www.gov.uk/government/publications/reinforced-autoclaved-aerated-concrete-management-information"},
            {"publisher": "Care Quality Commission", "title": "West Suffolk provider profile (RGR)", "url": "https://www.cqc.org.uk/provider/RGR"}
        ],
        "related": ["West Suffolk NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Amortisation — Imperial College Healthcare NHS Trust", "Amortisation — St George's University Hospitals NHS Foundation Trust", "New Hospital Programme"]
    },
    "General supplies & services — Milton Keynes University Hospital NHS Foundation Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "Milton Keynes University Hospital NHS Foundation Trust"}],
        "description": "MKUH's £6.12M general supplies & services line covers non-clinical consumables, linen, catering provisions, hotel-services materials, IT consumables, office supplies and minor expensed equipment at the single-site Milton Keynes University Hospital. The trust serves one of England's fastest-growing populations, with continual estate expansion and new clinical-block additions driving consumables baseline above peer single-site DGHs of similar bed count. Bedfordshire, Luton and Milton Keynes ICS-aligned procurement scaling supplements NHS Supply Chain framework.",
        "beneficiaries": "c. 4,000 WTE staff serving a c. 290,000 Milton Keynes catchment within Bedfordshire, Luton and Milton Keynes ICS — among England's fastest-growing populations; c. 105,000 ED attendances/yr; c. 50,000 admissions/yr; large maternity service.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 2 Inventories · Procurement Act 2023 · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "General supplies & services 2024-25", "value": "£6.12M"},
            {"label": "Trust scale", "value": "Single acute site (Milton Keynes University Hospital, Eaglestone) + ancillary clinics; c. 4,000 WTE"},
            {"label": "Population growth", "value": "MK among England's fastest-growing — drives continual activity expansion + consumables-baseline elevation vs peer DGH bed count"},
            {"label": "University status", "value": "MKUH title from 2018 — academic-partnership with University of Buckingham Medical School"},
            {"label": "Procurement route", "value": "NHS Supply Chain national framework + BLMK ICS collaborative + trust-direct contracts"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove cancellation re-stocking + agency backfill consumable churn"},
            {"label": "April 2025 NIC + CPI uplift", "value": "Employer-NIC step-up + non-clinical CPI feed forward unit-cost pressure on contractor pass-through"},
            {"label": "ED throughput", "value": "c. 105,000 attendances/yr"},
            {"label": "Funding trajectory", "value": "2021-22 c. £5.0M → 2023-24 £5.8M → 2024-25 £6.12M — sustained CPI + activity recovery + population-growth uplift"},
            {"label": "Delivery body", "value": "Trust Procurement + NHS Supply Chain (DHSC ALB) + BLMK ICS collaborative"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Bedfordshire, Luton and Milton Keynes ICB"},
            {"label": "Evaluation evidence", "value": "Model Hospital benchmarks; CQC inspection RD8; Trust ARA 2023-24; BLMK ICS procurement plan"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2018 pre-University-status MKH baseline · Successor: continued NHS Supply Chain + BLMK ICS scaling"}
        ],
        "notes": "MKUH's general supplies & services baseline is shaped by the single-site DGH operation serving one of England's fastest-growing populations — Milton Keynes' continual demographic expansion drives activity growth and consumables baseline elevation above peer DGH bed count. The 2018 University status (academic-partnership with University of Buckingham Medical School) broadens the education-related establishment + consumables footprint. The Bedfordshire, Luton and Milton Keynes ICS-aligned procurement collaborative provides scaling alongside NHS Supply Chain national framework. Industrial action 2023-24 drove cancellation re-stocking and agency-backfill consumable use. April 2025 NIC and CPI feed forward.",
        "sources": [
            {"publisher": "Milton Keynes University Hospital NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.mkuh.nhs.uk/about-us/key-publications"},
            {"publisher": "NHS Supply Chain", "title": "Annual Report 2023-24", "url": "https://www.supplychain.nhs.uk/about-us/our-publications/"},
            {"publisher": "Bedfordshire, Luton and Milton Keynes ICB", "title": "ICS strategy + procurement plan", "url": "https://www.bedfordshirelutonandmiltonkeynes.icb.nhs.uk/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "MKUH provider profile (RD8)", "url": "https://www.cqc.org.uk/provider/RD8"}
        ],
        "related": ["Milton Keynes University Hospital NHS Foundation Trust", "Clinical Supplies & Drugs", "NHS Acute Trusts", "NHS Supply Chain", "General supplies & services — University Hospitals Coventry And Warwickshire NHS Trust", "Department of Health and Social Care"]
    },
    "Establishment costs — North Cumbria Integrated Care NHS Foundation Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "North Cumbria Integrated Care NHS Foundation Trust"}],
        "description": "NCIC's £6.10M establishment costs line covers training, professional development, recruitment, printing, postage, telecoms, subscriptions, agency-finder fees and corporate-services running costs supporting the c. 7,000-WTE workforce across Cumberland Infirmary (Carlisle), West Cumberland Hospital (Whitehaven) and integrated community services across north Cumbria. Formed in 2019 by the merger of North Cumbria University Hospitals with Cumbria Partnership community mental-health services, the trust's geographically dispersed integrated workforce drives elevated establishment baseline.",
        "beneficiaries": "c. 7,000 WTE staff serving a c. 320,000 north Cumbria catchment within North East and North Cumbria ICS; c. 100,000 ED attendances/yr (Cumberland Infirmary + West Cumberland EDs); c. 50,000 admissions/yr; integrated community + mental-health workforce.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25 · Equality Act 2010 (training duty)",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£6.10M"},
            {"label": "Trust scale", "value": "Two-site acute (Cumberland Infirmary Carlisle + West Cumberland Hospital Whitehaven) + integrated community + mental-health services; c. 7,000 WTE"},
            {"label": "2019 merger context", "value": "Apr 2019 merger of North Cumbria University Hospitals NHS Trust + Cumbria Partnership community + mental-health functions to form NCIC"},
            {"label": "Cumberland Infirmary PFI", "value": "Cumberland Infirmary opened 2000 under PFI — Carillion-era contractor + post-Carillion novation; first major NHS PFI hospital"},
            {"label": "Geographic dispersion", "value": "North Cumbria geographically remote — drives travel + recruitment + training establishment overhead vs urban peers"},
            {"label": "Frontline Digitisation effect", "value": "EPR training + change-management feeds establishment line via agency-finder + corporate-training spend"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove agency-finder fee + recruitment establishment churn"},
            {"label": "Apr 2025 NIC + CPI uplift", "value": "Employer-NIC step-up + non-clinical CPI feed forward unit-cost pressure on establishment running costs"},
            {"label": "Funding trajectory", "value": "2021-22 c. £5.0M → 2023-24 £5.8M → 2024-25 £6.10M — strikes + Frontline Digitisation training driving uplift"},
            {"label": "Delivery body", "value": "Trust HR + Comms + IT + Finance + agency-finder framework providers + telecoms + printing contractors"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + NHSE Workforce + North East and North Cumbria ICB"},
            {"label": "Evaluation evidence", "value": "CQC inspection RNN; Carter / Lord review legacy non-pay benchmarks; Model Hospital corporate-services benchmarks; NENC ICS workforce plan"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2019 separate North Cumbria University Hospitals + Cumbria Partnership baselines · Successor: continued NENC ICS workforce planning + post-Apr 2025 NIC environment"}
        ],
        "notes": "NCIC's establishment costs line reflects the April 2019 merger of North Cumbria University Hospitals NHS Trust with Cumbria Partnership community + mental-health functions — making it one of England's distinctive integrated acute + community + mental-health trusts. The geographically remote north Cumbria footprint drives elevated travel, recruitment and training establishment overhead versus urban peers of similar workforce scale. Cumberland Infirmary PFI (opened 2000) carries Carillion-era contractor history with post-Carillion novation layering FM establishment overhead. Frontline Digitisation EPR training feeds via corporate-training spend. Industrial action 2023-24 drove agency-finder fees and recruitment churn. April 2025 NIC step-up affects pass-through.",
        "sources": [
            {"publisher": "North Cumbria Integrated Care NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.ncic.nhs.uk/about-us/key-publications/annual-reports-and-accounts"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://transform.england.nhs.uk/digitise-connect-transform/frontline-digitisation/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "National Audit Office", "title": "PFI and PF2 (HC 718, 2018)", "url": "https://www.nao.org.uk/reports/pfi-and-pf2/"},
            {"publisher": "Care Quality Commission", "title": "NCIC provider profile (RNN)", "url": "https://www.cqc.org.uk/provider/RNN"}
        ],
        "related": ["North Cumbria Integrated Care NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Establishment costs — South Tyneside and Sunderland NHS Foundation Trust", "Establishment costs — Portsmouth Hospitals University NHS Trust", "Department of Health and Social Care"]
    },
    "Transport (business + patient) — University Hospitals of North Midlands NHS Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "University Hospitals of North Midlands NHS Trust"}],
        "description": "UHNM's £6.08M transport line covers business mileage, inter-site patient transfers and Non-Emergency Patient Transport Services across the trust's two-site footprint (Royal Stoke University Hospital + County Hospital Stafford). Royal Stoke is the West Midlands North Major Trauma Centre and a tertiary cardiac, neuroscience and renal centre — driving inter-hospital and inter-trust PTS demand; West Midlands Ambulance Service NHS FT and accredited NEPTS contractors are the primary carriers. AHP and community mileage covers Staffordshire ICS catchment.",
        "beneficiaries": "c. 11,000 WTE staff serving a c. 900,000 north Staffordshire + Stoke-on-Trent + south Cheshire catchment plus regional tertiary referrals; c. 230,000 ED attendances/yr (Royal Stoke main + County Hospital EDs); c. 100,000 admissions/yr; Royal Stoke = West Midlands North Major Trauma Centre.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · IFRS 16 Leases (pool fleet) · NHS Act 2006 · Mental Health Act 1983 (s.135/136 conveyance) · NHSE Patient Transport Services Eligibility Framework 2022 · HMRC AMAP · NHS Agenda for Change Section 17",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£6.08M"},
            {"label": "Trust scale", "value": "Two-site academic acute (Royal Stoke University Hospital + County Hospital Stafford); c. 11,000 WTE"},
            {"label": "Major Trauma Centre", "value": "Royal Stoke = West Midlands North MTC — drives inter-site major-trauma transfer demand"},
            {"label": "Tertiary referrals", "value": "Royal Stoke cardiac + neuroscience + renal — substantial inter-hospital + inter-trust PTS"},
            {"label": "2014 Mid Staffs absorption", "value": "Nov 2014 acquisition of Mid Staffordshire NHS FT (post-Francis Inquiry dissolution) — established two-site footprint requiring inter-site PTS"},
            {"label": "PTS provider mix", "value": "West Midlands Ambulance Service NHS FT + accredited NEPTS contractors — re-tendered via Staffordshire and Stoke-on-Trent ICS"},
            {"label": "Staff mileage rate", "value": "NHS Agenda for Change Section 17 / HMRC AMAP 45p first 10,000 miles + 25p thereafter"},
            {"label": "Industrial action 2023-24 effect", "value": "Strike days drove ad-hoc inter-site transfers + locum mileage claims"},
            {"label": "Funding trajectory", "value": "2021-22 c. £5.0M → 2023-24 £5.8M → 2024-25 £6.08M — fuel CPI + activity recovery"},
            {"label": "Delivery body", "value": "Trust E&F + Travel team + WMAS NHS FT + accredited NEPTS contractors"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + NHSE NEPTS framework + Staffordshire and Stoke-on-Trent ICB"},
            {"label": "Evaluation evidence", "value": "NHSE NEPTS Eligibility Framework 2022 review; CQC inspection RJE; Trust ARA disclosure"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2014 separate North Staffs + Mid Staffs transport baselines · Successor: Staffordshire ICS shared-fleet pooling + EV transition"}
        ],
        "notes": "UHNM's transport line is structurally elevated by the trust's two-site footprint following the November 2014 acquisition of Mid Staffordshire NHS Foundation Trust — the Trust Special Administrator-led dissolution of Mid Staffs after the Francis Inquiry transferred County Hospital (Stafford) into UHNM, requiring continuous inter-site clinical transfers between Royal Stoke (Major Trauma Centre + tertiary cardiac, neuroscience, renal) and County Hospital. Industrial action 2023-24 added ad-hoc transfer demand and locum mileage. April 2025 NIC step-up affects WMAS PTS-contractor pass-through; CPI fuel pressure remains the dominant driver. Staffordshire ICS shared-fleet pooling and EV transition are the medium-term levers.",
        "sources": [
            {"publisher": "University Hospitals of North Midlands NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.uhnm.nhs.uk/about-us/key-publications/annual-reports-and-accounts/"},
            {"publisher": "NHS England", "title": "Non-Emergency Patient Transport Services Eligibility Framework 2022", "url": "https://www.england.nhs.uk/long-read/non-emergency-patient-transport-services-eligibility-framework/"},
            {"publisher": "West Midlands Ambulance Service NHS FT", "title": "Annual Report 2023-24", "url": "https://wmas.nhs.uk/about-us/publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "UHNM provider profile (RJE)", "url": "https://www.cqc.org.uk/provider/RJE"}
        ],
        "related": ["University Hospitals of North Midlands NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Transport (business + patient) — Imperial College Healthcare NHS Trust", "Transport (business + patient) — University Hospitals Birmingham NHS Foundation Trust", "Department of Health and Social Care"]
    },
}
