# -*- coding: utf-8 -*-
# Phase 2 Acute slice 2 — chunk 17 (17 NHS Acute Trust orphan sub-lines)
# Hand-curated trust-specific PROGRAMME-archetype enrichment entries.
# Structural contract per docs/archetype_briefs.md.

NEW = {
    "Establishment costs — University Hospitals of Derby and Burton NHS Foundation Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "University Hospitals of Derby and Burton NHS Foundation Trust"}],
        "description": "UHDB's £4.797M establishment costs line covers postage, printing, stationery, telephony, training & professional fees, subscriptions, recruitment advertising and minor non-clinical office overhead across the four-site Royal Derby + Queen's Burton + Florence Nightingale + Sir Robert Peel footprint. The trust formed via the 2018 merger of Derby Teaching Hospitals and Burton Hospitals — the line still reflects integration overhead and Frontline Digitisation EPR change-management training cycles within the Joined Up Care Derbyshire ICS.",
        "beneficiaries": "c. 12,500 WTE staff serving a c. 1.05M Derbyshire and east Staffordshire catchment; c. 250,000 ED attendances/yr (Royal Derby + Queen's Burton EDs combined); c. 130,000 admissions/yr; multi-site footprint across four hospitals — substantial training, telephony and postage overhead.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£4.797M"},
            {"label": "Trust scale", "value": "Four-site acute + community (Royal Derby + Queen's Burton + Florence Nightingale + Sir Robert Peel); c. 12,500 WTE"},
            {"label": "Merger context", "value": "Formed 1 Jul 2018 from Derby Teaching Hospitals + Burton Hospitals — establishment line still carries integration overhead"},
            {"label": "Composition", "value": "Postage + telephony + stationery + training & professional fees + subscriptions + recruitment + minor non-clinical overhead"},
            {"label": "Frontline Digitisation EPR", "value": "EPR programme drives substantial training & change-management spend through establishment line"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove recruitment + training churn"},
            {"label": "Funding trajectory", "value": "2021-22 c. £4.0M → 2023-24 £4.5M → 2024-25 £4.797M — sustained CPI on professional fees + telephony"},
            {"label": "April 2025 NIC + CPI uplift", "value": "Apr 2025 NIC step-up not direct hit, but feeds into agency/recruitment supplier pricing absorbed here"},
            {"label": "Delivery body", "value": "Trust Corporate Services + HR + Finance + IT (telephony) + external training providers"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Joined Up Care Derbyshire ICB"},
            {"label": "Evaluation evidence", "value": "Model Hospital benchmarks (corporate services); CQC inspection (RTG); Trust ARA disclosure"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2018 separate Derby Teaching + Burton establishment baselines · Successor: Joined Up Care Derbyshire ICS shared corporate services"}
        ],
        "notes": "UHDB's establishment cost baseline reflects the still-maturing 2018 merger of Derby Teaching Hospitals NHS FT with Burton Hospitals NHS FT — corporate-services integration carried multi-year training, recruitment-advertising and telephony-consolidation overhead that has only partially worked through. The Frontline Digitisation EPR programme drives substantial training and change-management spend booked here rather than capitalised. Industrial action 2023-24 added recruitment churn and onboarding cycles for new locum and substantive cohorts. Joined Up Care Derbyshire ICS shared-corporate-services scaling is the medium-term lever, with April 2025 NIC step-up feeding indirectly via supplier and agency pricing.",
        "sources": [
            {"publisher": "University Hospitals of Derby and Burton NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.uhdb.nhs.uk/annual-reports"},
            {"publisher": "Care Quality Commission", "title": "UHDB provider profile (RTG)", "url": "https://www.cqc.org.uk/provider/RTG"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/connecteddigitalsystems/frontline-digitisation/"},
            {"publisher": "Joined Up Care Derbyshire ICB", "title": "ICB strategy + system plans", "url": "https://joinedupcarederbyshire.co.uk/"}
        ],
        "related": ["University Hospitals of Derby and Burton NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Establishment costs — Northern Lincolnshire and Goole NHS Foundation Trust", "Frontline Digitisation programme", "Joined Up Care Derbyshire ICB"]
    },
    "Business rates — Cambridge University Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "Cambridge University Hospitals NHS Foundation Trust"}],
        "description": "CUH's £4.793M business rates line covers non-domestic rates payable on the Addenbrooke's Hospital and Rosie Hospital estate on the Cambridge Biomedical Campus, set on the Valuation Office Agency 2023 rating list (effective Apr 2023, antecedent valuation 1 Apr 2021) and uplifted by the small business / standard multiplier set under LGFA 1988. As one of England's largest research-intensive teaching trusts, CUH carries a substantial rateable-value footprint reflecting its acute, specialist and research estate, partially offset by mandatory charity-relief mechanisms unavailable to NHS trusts.",
        "beneficiaries": "c. 12,500 WTE staff serving a c. 1.0M Cambridgeshire catchment plus East of England tertiary referrals (transplant, neurosciences, cancer, paediatrics); c. 130,000 ED attendances/yr at Addenbrooke's ED + major trauma centre; c. 145,000 admissions/yr; large biomedical campus footprint.",
        "legal_basis": "Local Government Finance Act 1988 (Sch 6 — non-domestic rating) · Non-Domestic Rating Act 2023 · Non-Domestic Rating (Multipliers and Private Finance) Act 2024 · DHSC Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£4.793M"},
            {"label": "Trust scale", "value": "Two-hospital + research campus (Addenbrooke's + Rosie) on Cambridge Biomedical Campus; c. 12,500 WTE"},
            {"label": "Major Trauma Centre", "value": "Addenbrooke's = East of England MTC — drives extensive resus + theatre + ICU footprint contributing to RV"},
            {"label": "VOA list cycle", "value": "2023 rating list (effective Apr 2023, AVD 1 Apr 2021); next revaluation 2026"},
            {"label": "Charity-relief gap", "value": "NHS trusts excluded from 80% mandatory charity relief — direct fiscal cost vs charity-status providers"},
            {"label": "Funding trajectory", "value": "2021-22 c. £4.2M → 2023-24 £4.5M → 2024-25 £4.793M (post-2023 list rebasing + multiplier uplift)"},
            {"label": "NDRA 2024 effect", "value": "Non-Domestic Rating (Multipliers and Private Finance) Act 2024 split multipliers; large hereditaments face higher multiplier from 2026"},
            {"label": "Research estate effect", "value": "Cambridge Biomedical Campus shared facilities + research labs add RV beyond pure clinical footprint"},
            {"label": "Delivery body", "value": "Trust E&F + Finance team + Valuation Office Agency (VOA) + South Cambridgeshire DC billing authority"},
            {"label": "Policy owner", "value": "MHCLG (rating policy) + HM Treasury (multiplier) + DHSC + NHSE Provider Finance"},
            {"label": "Evaluation evidence", "value": "VOA rating-list disclosure; Trust ARA premises note; NHSE Estates Return (ERIC)"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2017 rating list baseline · Successor: 2026 revaluation + NDRA 2024 split-multiplier regime"}
        ],
        "notes": "Cambridge University Hospitals carries one of England's largest acute-trust business-rates baselines, reflecting the Addenbrooke's + Rosie footprint on the Cambridge Biomedical Campus and the trust's role as East of England Major Trauma Centre. The 2023 rating list's 1 April 2021 antecedent valuation embedded post-pandemic rental and capital-value benchmarks, and standard-multiplier uplifts to 54.6p feed annual cost growth. NHS trusts remain excluded from the 80% mandatory charity relief — a structural cost gap. The Non-Domestic Rating (Multipliers and Private Finance) Act 2024 introduces a split-multiplier regime from 2026 placing large hereditaments on a higher multiplier, exposing CUH to further rate growth.",
        "sources": [
            {"publisher": "Cambridge University Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.cuh.nhs.uk/about-us/publications/annual-report/"},
            {"publisher": "Valuation Office Agency", "title": "2023 rating list — Cambridge University Hospitals (Addenbrooke's)", "url": "https://www.tax.service.gov.uk/business-rates-find/"},
            {"publisher": "Ministry of Housing, Communities and Local Government", "title": "Business rates — non-domestic rating multipliers 2024-25", "url": "https://www.gov.uk/government/publications/business-rates-multipliers"},
            {"publisher": "HM Treasury", "title": "Non-Domestic Rating (Multipliers and Private Finance) Act 2024 explanatory notes", "url": "https://www.legislation.gov.uk/ukpga/2024/9/contents"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"}
        ],
        "related": ["Cambridge University Hospitals NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Business rates — University Hospitals of Leicester NHS Trust", "Business rates — Northumbria Healthcare NHS Foundation Trust", "Valuation Office Agency"]
    },
    "General supplies & services — Warrington and Halton Teaching Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "Warrington and Halton Teaching Hospitals NHS Foundation Trust"}],
        "description": "WHTH's £4.787M general supplies & services line covers non-clinical consumables, office supplies, linen, catering provisions, hotel-services materials, IT consumables and minor expensed equipment across the two-site Warrington Hospital + Halton Hospital footprint serving the Cheshire & Merseyside ICS. The trust achieved teaching-hospital status in 2024, and the line reflects modest two-site activity volumes with NHS Supply Chain national framework as the dominant procurement route plus Cheshire & Merseyside ICS collaborative scaling.",
        "beneficiaries": "c. 4,500 WTE staff serving a c. 330,000 Warrington and Halton catchment; c. 110,000 ED attendances/yr at Warrington ED + Halton Urgent Treatment Centre; c. 55,000 admissions/yr; teaching-hospital status achieved 2024 — drives marginal training-overhead consumable demand.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 2 Inventories · Procurement Act 2023 · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "General supplies & services 2024-25", "value": "£4.787M"},
            {"label": "Trust scale", "value": "Two-site DGH (Warrington + Halton); c. 4,500 WTE; teaching-hospital status from 2024"},
            {"label": "ED throughput", "value": "c. 110,000 ED attendances/yr (Warrington main + Halton UTC)"},
            {"label": "Composition", "value": "Non-clinical consumables + linen + catering + hotel-services + office + minor IT consumables"},
            {"label": "Procurement route", "value": "NHS Supply Chain national framework + trust-direct contracts + Cheshire & Merseyside ICS regional collaboration"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove cancellation re-stocking + agency backfill"},
            {"label": "April 2025 NIC + CPI uplift", "value": "Apr 2025 employer-NIC step-up feeds supplier pricing; non-clinical CPI ongoing"},
            {"label": "Funding trajectory", "value": "2021-22 c. £4.0M → 2023-24 £4.5M → 2024-25 £4.787M — sustained CPI + activity recovery"},
            {"label": "Delivery body", "value": "Trust Procurement + NHS Supply Chain + Cheshire & Merseyside ICS procurement collaborative"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Cheshire & Merseyside ICB"},
            {"label": "Evaluation evidence", "value": "Model Hospital benchmarks (non-pay); CQC inspection (RWW); Trust ARA disclosure"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-Procurement Act 2023 OJEU regime · Successor: ICS-collaborative scaling under PA 2023 + Cheshire & Merseyside group commercial"}
        ],
        "notes": "Warrington and Halton Teaching Hospitals' general supplies & services baseline reflects the steady two-site activity profile — Warrington Hospital DGH and Halton Hospital — within Cheshire & Merseyside ICS. Achievement of teaching-hospital status in 2024 added a marginal training-overhead consumable demand layer. NHS Supply Chain remains the dominant procurement route, with Cheshire & Merseyside ICS collaborative scaling as the medium-term lever — consistent with the wider ICS group-commercial direction also driving Liverpool University Hospitals procurement consolidation. Industrial action 2023-24 drove cancellation re-stocking churn; April 2025 NIC step-up feeds supplier pricing alongside ongoing CPI.",
        "sources": [
            {"publisher": "Warrington and Halton Teaching Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.whh.nhs.uk/about-us/publications-policies-and-strategies"},
            {"publisher": "NHS Supply Chain", "title": "Annual Report 2023-24", "url": "https://www.supplychain.nhs.uk/about-us/our-publications/"},
            {"publisher": "Care Quality Commission", "title": "WHTH provider profile (RWW)", "url": "https://www.cqc.org.uk/provider/RWW"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Cheshire and Merseyside ICB", "title": "ICS strategy + provider collaborative", "url": "https://www.cheshireandmerseyside.nhs.uk/"}
        ],
        "related": ["Warrington and Halton Teaching Hospitals NHS Foundation Trust", "Clinical Supplies & Drugs", "NHS Acute Trusts", "General supplies & services — Liverpool University Hospitals NHS Foundation Trust", "NHS Supply Chain", "Cheshire and Merseyside ICB"]
    },
    "General supplies & services — Walsall Healthcare NHS Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "Walsall Healthcare NHS Trust"}],
        "description": "Walsall Healthcare's £4.708M general supplies & services line covers non-clinical consumables, linen, catering, hotel-services materials, office supplies and minor expensed equipment at the single-site Manor Hospital DGH plus the trust's Walsall community-services footprint. The trust is part of the Black Country Provider Collaborative within the Black Country ICS, and operates a group-model arrangement with The Royal Wolverhampton NHS Trust (RWT) — shaping medium-term procurement consolidation. NHS Supply Chain dominates routing, with Black Country collaborative scaling layered.",
        "beneficiaries": "c. 5,000 WTE staff serving a c. 285,000 Walsall borough catchment; c. 130,000 ED attendances/yr at Manor Hospital ED; c. 60,000 admissions/yr; integrated community services across Walsall (district nursing, community paediatric).",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 2 Inventories · Procurement Act 2023 · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "General supplies & services 2024-25", "value": "£4.708M"},
            {"label": "Trust scale", "value": "Single-site acute (Manor Hospital) + integrated Walsall community services; c. 5,000 WTE"},
            {"label": "Group-model context", "value": "Black Country Provider Collaborative + RWT/Walsall group-model arrangement (shared CEO + corporate functions)"},
            {"label": "ED throughput", "value": "c. 130,000 ED attendances/yr at Manor Hospital ED"},
            {"label": "Procurement route", "value": "NHS Supply Chain national framework + Black Country collaborative + RWT-shared procurement scaling"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove cancellation re-stocking churn"},
            {"label": "April 2025 NIC + CPI uplift", "value": "Apr 2025 employer-NIC step-up feeds supplier pricing; non-clinical CPI ongoing"},
            {"label": "Funding trajectory", "value": "2021-22 c. £4.0M → 2023-24 £4.4M → 2024-25 £4.708M — CPI + group-scaling partial offset"},
            {"label": "Delivery body", "value": "Trust Procurement + NHS Supply Chain + Black Country procurement collaborative + RWT-shared functions"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Black Country ICB"},
            {"label": "Evaluation evidence", "value": "Model Hospital benchmarks; CQC inspection (RBK); Trust ARA disclosure; Black Country group-model business case"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-group stand-alone trust procurement · Successor: RWT/Walsall group consolidated procurement under Black Country collaborative"}
        ],
        "notes": "Walsall Healthcare's general supplies & services baseline reflects the single-site Manor Hospital DGH plus integrated Walsall community-services footprint, sitting within the maturing RWT/Walsall group-model arrangement that shares a chief executive and a growing set of corporate functions across the Black Country ICS. The medium-term path is consolidated procurement via the Black Country Provider Collaborative, with RWT-led shared procurement scaling. Industrial action 2023-24 drove cancellation re-stocking churn at the acute site; April 2025 NIC step-up feeds supplier pricing pressure on non-clinical inputs alongside ongoing CPI. NHS Supply Chain national framework remains the dominant procurement route in the near term.",
        "sources": [
            {"publisher": "Walsall Healthcare NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.walsallhealthcare.nhs.uk/about-us/publications/"},
            {"publisher": "Black Country ICB", "title": "Black Country Provider Collaborative + group-model arrangements", "url": "https://blackcountry.icb.nhs.uk/"},
            {"publisher": "NHS Supply Chain", "title": "Annual Report 2023-24", "url": "https://www.supplychain.nhs.uk/about-us/our-publications/"},
            {"publisher": "Care Quality Commission", "title": "Walsall Healthcare provider profile (RBK)", "url": "https://www.cqc.org.uk/provider/RBK"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"}
        ],
        "related": ["Walsall Healthcare NHS Trust", "Clinical Supplies & Drugs", "NHS Acute Trusts", "The Royal Wolverhampton NHS Trust", "General supplies & services — Warrington and Halton Teaching Hospitals NHS Foundation Trust", "NHS Supply Chain"]
    },
    "General supplies & services — Countess of Chester Hospital NHS Foundation Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "Countess of Chester Hospital NHS Foundation Trust"}],
        "description": "Countess of Chester's £4.705M general supplies & services line covers non-clinical consumables, linen, catering, hotel-services materials, office supplies and minor expensed equipment at the Countess of Chester Hospital plus the Ellesmere Port satellite. The trust sits within the Cheshire & Merseyside ICS, and the operational baseline carries residual reputational and governance overhead from the Lucy Letby case (Thirlwall Inquiry ongoing 2024-25), with NHS Supply Chain as primary procurement route plus ICS collaborative scaling.",
        "beneficiaries": "c. 4,500 WTE staff serving a c. 365,000 west Cheshire catchment plus parts of north Wales (cross-border flow); c. 90,000 ED attendances/yr at Countess of Chester ED; c. 50,000 admissions/yr; large neonatal unit historically — focus of ongoing Thirlwall Inquiry.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 2 Inventories · Procurement Act 2023 · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "General supplies & services 2024-25", "value": "£4.705M"},
            {"label": "Trust scale", "value": "Single-site DGH + Ellesmere Port satellite; c. 4,500 WTE"},
            {"label": "ED throughput", "value": "c. 90,000 ED attendances/yr at Countess of Chester ED"},
            {"label": "Thirlwall Inquiry context", "value": "Statutory inquiry into Lucy Letby case ongoing 2024-25 — drives governance overhead but limited direct supplies impact"},
            {"label": "Procurement route", "value": "NHS Supply Chain national framework + Cheshire & Merseyside ICS collaborative + trust-direct contracts"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove cancellation re-stocking churn"},
            {"label": "April 2025 NIC + CPI uplift", "value": "Apr 2025 employer-NIC step-up feeds supplier pricing; non-clinical CPI ongoing"},
            {"label": "Funding trajectory", "value": "2021-22 c. £4.0M → 2023-24 £4.4M → 2024-25 £4.705M — sustained CPI + activity recovery"},
            {"label": "Delivery body", "value": "Trust Procurement + NHS Supply Chain + Cheshire & Merseyside ICS procurement collaborative"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Cheshire & Merseyside ICB"},
            {"label": "Evaluation evidence", "value": "Model Hospital benchmarks; CQC inspection (RJR); Trust ARA disclosure; Thirlwall Inquiry evidence"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-Procurement Act 2023 OJEU regime · Successor: ICS-collaborative scaling under PA 2023"}
        ],
        "notes": "Countess of Chester's general supplies & services baseline reflects the steady single-site DGH activity profile plus Ellesmere Port satellite within the Cheshire & Merseyside ICS, with material cross-border patient flow from Flintshire shaping demand. The Thirlwall Inquiry into the Lucy Letby case drives substantial governance, evidence-management and external-legal overhead at trust level, but the direct supplies-line impact is modest. NHS Supply Chain remains the dominant procurement route, with ICS-collaborative scaling as the medium-term lever. Industrial action 2023-24 drove cancellation re-stocking churn; April 2025 NIC step-up feeds supplier pricing alongside ongoing non-clinical CPI.",
        "sources": [
            {"publisher": "Countess of Chester Hospital NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.coch.nhs.uk/about-us/publications-and-reports"},
            {"publisher": "Thirlwall Inquiry", "title": "Public inquiry into events at Countess of Chester Hospital", "url": "https://thirlwall.public-inquiry.uk/"},
            {"publisher": "NHS Supply Chain", "title": "Annual Report 2023-24", "url": "https://www.supplychain.nhs.uk/about-us/our-publications/"},
            {"publisher": "Care Quality Commission", "title": "Countess of Chester provider profile (RJR)", "url": "https://www.cqc.org.uk/provider/RJR"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"}
        ],
        "related": ["Countess of Chester Hospital NHS Foundation Trust", "Clinical Supplies & Drugs", "NHS Acute Trusts", "General supplies & services — Warrington and Halton Teaching Hospitals NHS Foundation Trust", "NHS Supply Chain", "Cheshire and Merseyside ICB"]
    },
    "General supplies & services — Norfolk and Norwich University Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "Norfolk and Norwich University Hospitals NHS Foundation Trust"}],
        "description": "NNUH's £4.704M general supplies & services line covers non-clinical consumables, linen, catering, hotel-services materials, office supplies and minor expensed equipment at the Norfolk and Norwich University Hospital (PFI-built, opened 2001) plus the Cromer & District Hospital. The trust is one of England's larger acute footprints serving a dispersed Norfolk catchment, and the line reflects the PFI hotel-services interface (catering and linen partly delivered through Serco PFI sub-contracts) plus trust-direct procurement via NHS Supply Chain.",
        "beneficiaries": "c. 9,500 WTE staff serving a c. 1.0M Norfolk catchment plus Suffolk/north-Cambs cross-flow; c. 165,000 ED attendances/yr at NNUH ED; c. 105,000 admissions/yr; large maternity unit and East of England specialist services (cancer, neurosciences referrals).",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 2 Inventories · Procurement Act 2023 · NHS Act 2006 · Health and Care Act 2022 · IFRIC 12 (PFI hotel-services interface)",
        "key_stats": [
            {"label": "General supplies & services 2024-25", "value": "£4.704M"},
            {"label": "Trust scale", "value": "Two-site (NNUH + Cromer & District); c. 9,500 WTE"},
            {"label": "PFI context", "value": "NNUH PFI signed 1998, operational 2001; Octagon SPV with Serco hard + soft FM — catering/linen partly through PFI sub-contracts"},
            {"label": "ED throughput", "value": "c. 165,000 ED attendances/yr at NNUH ED"},
            {"label": "Procurement route", "value": "NHS Supply Chain national framework + trust-direct + Norfolk & Waveney ICS collaborative + PFI sub-contract residual"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove cancellation re-stocking churn"},
            {"label": "April 2025 NIC + CPI uplift", "value": "Apr 2025 employer-NIC step-up feeds supplier pricing; non-clinical CPI ongoing"},
            {"label": "Funding trajectory", "value": "2021-22 c. £4.0M → 2023-24 £4.4M → 2024-25 £4.704M — CPI + activity recovery"},
            {"label": "Delivery body", "value": "Trust Procurement + NHS Supply Chain + Norfolk & Waveney ICS collaborative + Serco PFI-residual sub-contract"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + Norfolk and Waveney ICB"},
            {"label": "Evaluation evidence", "value": "Model Hospital benchmarks; CQC inspection (RM1); Trust ARA disclosure; NAO PFI hand-back report 2020"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-PFI hospital city-centre site · Successor: post-2031 PFI hand-back + consolidated trust-direct procurement of hotel-services"}
        ],
        "notes": "Norfolk and Norwich University Hospital is a PFI-built (1998 signed, 2001 operational) site whose hotel-services interface — catering and linen — is partly delivered through Serco sub-contracts under the Octagon SPV concession running to c. 2031. The general supplies & services line sits alongside that PFI flow rather than replacing it: trust-direct procurement covers non-PFI consumable lines through NHS Supply Chain plus Norfolk & Waveney ICS collaborative scaling. The 2031 PFI expiry is in the active hand-back planning window (NAO 2020 flagged early-expiry cohort); post-hand-back, hotel-services routing returns fully to trust-direct procurement, lifting this line. Industrial action 2023-24 drove cancellation re-stocking churn; April 2025 NIC feeds supplier pricing.",
        "sources": [
            {"publisher": "Norfolk and Norwich University Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.nnuh.nhs.uk/about-us/our-publications/"},
            {"publisher": "National Audit Office", "title": "Managing PFI assets and services as contracts end (HC 632, 2020)", "url": "https://www.nao.org.uk/reports/managing-pfi-assets-and-services-as-contracts-end/"},
            {"publisher": "NHS Supply Chain", "title": "Annual Report 2023-24", "url": "https://www.supplychain.nhs.uk/about-us/our-publications/"},
            {"publisher": "Care Quality Commission", "title": "NNUH provider profile (RM1)", "url": "https://www.cqc.org.uk/provider/RM1"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"}
        ],
        "related": ["Norfolk and Norwich University Hospitals NHS Foundation Trust", "Clinical Supplies & Drugs", "NHS Acute Trusts", "General supplies & services — Countess of Chester Hospital NHS Foundation Trust", "NHS Supply Chain", "Norfolk and Waveney ICB"]
    },
    "Amortisation — United Lincolnshire Hospitals NHS Trust": {
        "aliases": [{"name": "Amortisation", "parent": "United Lincolnshire Hospitals NHS Trust"}],
        "description": "ULHT's £4.683M amortisation line covers the systematic write-down of capitalised intangible assets — software licences, EPR configuration costs, radiology PACS, internally-generated clinical applications and acquired digital systems — across the four-site Lincoln County + Pilgrim Boston + Grantham + County hospitals estate. The trust is in active group-model formation with Northern Lincolnshire and Goole NHS FT under a single Lincolnshire group, and Frontline Digitisation EPR rollout cycles drive the intangible-asset baseline through IAS 38 over typical 5-10 year UELs.",
        "beneficiaries": "c. 9,000 WTE staff serving a c. 770,000 dispersed rural Lincolnshire catchment; c. 200,000 ED attendances/yr (Lincoln + Pilgrim Boston + Grantham EDs combined); c. 100,000 admissions/yr; multi-site rural footprint — major Frontline Digitisation EPR programme cost driver.",
        "legal_basis": "IAS 38 Intangible Assets · DHSC Group Accounting Manual 2024-25 ch.5 · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£4.683M"},
            {"label": "Trust scale", "value": "Four-site rural acute (Lincoln + Pilgrim Boston + Grantham + County); c. 9,000 WTE"},
            {"label": "Group-model formation", "value": "ULHT + Northern Lincs and Goole NHS FT shared CEO + group-model formation 2023-25 (Lincolnshire group)"},
            {"label": "Frontline Digitisation EPR", "value": "EPR procurement (Nervecentre / SystemC pathway) drives capitalised intangible baseline + multi-year amortisation cycle"},
            {"label": "UEL convention", "value": "Typical 5-10 year UEL per DHSC GAM ch.5; EPR licences typically 5-7 yr; PACS 5 yr"},
            {"label": "Funding trajectory", "value": "2021-22 c. £3.5M → 2023-24 £4.3M → 2024-25 £4.683M — Frontline Digitisation capitalisation feeding amortisation"},
            {"label": "RAAC + NHP context", "value": "Pilgrim Boston flagged in RAAC concrete-plank cohort (Sep 2023 HSSIB list); NHP Reset deferred any Lincolnshire rebuild"},
            {"label": "April 2025 NIC + CPI uplift", "value": "Indirect via supplier maintenance pricing absorbed in IT operating contracts (not amortisation)"},
            {"label": "Delivery body", "value": "Trust IT + Finance + Frontline Digitisation programme + EPR vendor (Nervecentre / SystemC pathway)"},
            {"label": "Policy owner", "value": "NHSE Frontline Digitisation + DHSC + NHSE Provider Finance + Lincolnshire ICB"},
            {"label": "Evaluation evidence", "value": "NHSE digital maturity assessment; HSSIB RAAC report; Trust ARA intangible-asset note; NAO digital health reports"},
            {"label": "Predecessor / successor", "value": "Predecessor: legacy WebV + paper-light record · Successor: full Nervecentre / SystemC EPR with capitalised configuration + multi-year amortisation"}
        ],
        "notes": "ULHT's amortisation line is principally driven by the Frontline Digitisation EPR procurement programme — capitalising configuration, deployment and licence costs that flow through IAS 38 over typical 5-10 year UELs. The trust's four-site rural Lincolnshire footprint and the active group-model formation with Northern Lincolnshire and Goole NHS FT under a single Lincolnshire group reshape the capital-investment trajectory. Pilgrim Boston was flagged in the September 2023 HSSIB RAAC concrete-plank cohort, but the New Hospital Programme January 2025 Reset deferred any Lincolnshire rebuild, leaving residual existing-estate digital investment as the dominant capital-amortisation driver. Indirect supplier maintenance CPI sits in operating contracts rather than amortisation.",
        "sources": [
            {"publisher": "United Lincolnshire Hospitals NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.ulh.nhs.uk/about/publications/"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/connecteddigitalsystems/frontline-digitisation/"},
            {"publisher": "Health Services Safety Investigations Body", "title": "RAAC in NHS healthcare buildings (Sep 2023 listing)", "url": "https://www.hssib.org.uk/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 5 — Intangible assets)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "ULHT provider profile (RWD)", "url": "https://www.cqc.org.uk/provider/RWD"}
        ],
        "related": ["United Lincolnshire Hospitals NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Northern Lincolnshire and Goole NHS Foundation Trust", "Frontline Digitisation programme", "Amortisation — Frimley Health NHS Foundation Trust"]
    },
    "Transport (business + patient) — Royal Cornwall Hospitals NHS Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "Royal Cornwall Hospitals NHS Trust"}],
        "description": "RCHT's £4.678M transport line covers business mileage, inter-site patient transfers and Non-Emergency Patient Transport Services across the Royal Cornwall Hospital (Truro) + West Cornwall (Penzance) + St Michael's (Hayle) footprint. Cornwall's geography — long peninsular distances, major-trauma transfers to University Hospitals Plymouth, dispersed rural population and seasonal tourism surge — drives one of the highest transport-cost-per-WTE profiles in English acute trusts. SWASFT handles emergency conveyance; accredited NEPTS contractors handle non-emergency patient transport.",
        "beneficiaries": "c. 5,500 WTE staff serving a c. 570,000 Cornwall and Isles of Scilly catchment plus seasonal tourism surge (>5M visitors/yr); c. 80,000 ED attendances/yr at RCH Treliske ED; c. 65,000 admissions/yr; major-trauma transfers via SWASFT + RAF/coastguard helimed to UHP MTC.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · IFRS 16 Leases (pool fleet) · NHS Act 2006 · NHSE Patient Transport Services Eligibility Framework 2022 · HMRC AMAP · NHS AfC Section 17 · Mental Health Act 1983 (s.135/136 conveyance)",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£4.678M"},
            {"label": "Trust scale", "value": "Three-site rural acute (RCH Truro + West Cornwall Penzance + St Michael's Hayle); c. 5,500 WTE"},
            {"label": "Geography + seasonal surge", "value": "Cornwall peninsula — longest mainland NHS trust distances; major-trauma transfers to UHP Derriford (c. 80 miles); >5M tourist visitors/yr drives summer ED + transfer demand uplift"},
            {"label": "PTS provider mix", "value": "SWASFT (emergency) + E-zec Medical / accredited NEPTS (non-emergency); Cornwall Air Ambulance"},
            {"label": "Staff mileage rate", "value": "NHS AfC Section 17 / HMRC AMAP 45p first 10,000 miles + 25p thereafter"},
            {"label": "Pool fleet (IFRS 16)", "value": "Right-of-use depreciation + interest on leased pool vehicles for AHPs + community teams"},
            {"label": "Industrial action 2023-24 effect", "value": "Strike days drove ad-hoc inter-site transfers + locum mileage claims"},
            {"label": "Funding trajectory", "value": "2021-22 c. £3.8M → 2023-24 £4.3M → 2024-25 £4.678M — fuel CPI + activity recovery + tourism surge"},
            {"label": "Delivery body", "value": "Trust E&F + Travel team + SWASFT + E-zec Medical / accredited NEPTS + Cornwall Air Ambulance"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + NHSE UEC + Cornwall and Isles of Scilly ICB"},
            {"label": "Evaluation evidence", "value": "NAO Urgent and Emergency Care reports; CQC inspection (REF); NHSE PTS framework review"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2022 NHSE eligibility framework PTS · Successor: 2024-25 Cornwall NEPTS re-tender"}
        ],
        "notes": "Royal Cornwall's transport line is structurally elevated by the peninsula's geography — long mainland distances, dispersed rural population and the absence of a major-trauma centre within Cornwall (transfers go to UHP's MTC at Derriford, c. 80 miles). Seasonal tourism surge above 5 million visitors per year layers an additional summer ED and transfer demand uplift. SWASFT handles emergency conveyance; non-emergency patient transport runs through E-zec Medical and accredited NEPTS contractors under the 2022 NHSE eligibility framework — a 2024-25 Cornwall NEPTS re-tender reshapes the medium-term price path. The IFRS 16 2022 pool-fleet transition split right-of-use depreciation and interest into the line. Fuel CPI and the April 2025 NIC step-up feed forward via contractor pricing.",
        "sources": [
            {"publisher": "Royal Cornwall Hospitals NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.royalcornwall.nhs.uk/about-us/key-publications/"},
            {"publisher": "NHS England", "title": "Non-Emergency Patient Transport Services — Eligibility Framework 2022", "url": "https://www.england.nhs.uk/publication/non-emergency-patient-transport-services-eligibility-framework/"},
            {"publisher": "Care Quality Commission", "title": "Royal Cornwall Hospitals provider profile (REF)", "url": "https://www.cqc.org.uk/provider/REF"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Cornwall and Isles of Scilly ICB", "title": "ICB strategy + system plans", "url": "https://www.cios.icb.nhs.uk/"}
        ],
        "related": ["Royal Cornwall Hospitals NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Transport (business + patient) — Lewisham and Greenwich NHS Trust", "South Western Ambulance Service NHS Foundation Trust", "Cornwall and Isles of Scilly ICB"]
    },
    "General supplies & services — Calderdale and Huddersfield NHS Foundation Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "Calderdale and Huddersfield NHS Foundation Trust"}],
        "description": "CHFT's £4.665M general supplies & services line covers non-clinical consumables, linen, catering, hotel-services materials, office supplies and minor expensed equipment at the two-site Calderdale Royal Hospital (Halifax, PFI 2001) + Huddersfield Royal Infirmary footprint. The trust is the lead provider for West Yorkshire ICS Frontline Digitisation EPR (Cerner / Oracle Health Millennium) — drives associated training-overhead consumables on top of the core acute baseline. NHS Supply Chain national framework dominates routing, with West Yorkshire ICS collaborative scaling layered.",
        "beneficiaries": "c. 6,500 WTE staff serving a c. 470,000 Calderdale + Kirklees catchment; c. 175,000 ED attendances/yr (Calderdale Royal + Huddersfield EDs); c. 80,000 admissions/yr; lead Cerner / Oracle Health Millennium digital provider for West Yorkshire ICS — c. 8 acute trusts.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 2 Inventories · Procurement Act 2023 · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "General supplies & services 2024-25", "value": "£4.665M"},
            {"label": "Trust scale", "value": "Two-site DGH (Calderdale Royal Halifax + Huddersfield Royal Infirmary); c. 6,500 WTE"},
            {"label": "ED throughput", "value": "c. 175,000 ED attendances/yr (CRH + HRI combined)"},
            {"label": "EPR lead provider", "value": "Cerner / Oracle Health Millennium — CHFT is West Yorkshire ICS shared-tenant lead serving multiple regional trusts"},
            {"label": "Procurement route", "value": "NHS Supply Chain national framework + West Yorkshire ICS collaborative + trust-direct + PFI sub-contract residual"},
            {"label": "Industrial action 2023-24 effect", "value": "Strike days drove cancellation re-stocking churn"},
            {"label": "April 2025 NIC + CPI uplift", "value": "Apr 2025 employer-NIC step-up feeds supplier pricing; non-clinical CPI ongoing"},
            {"label": "Funding trajectory", "value": "2021-22 c. £4.0M → 2023-24 £4.4M → 2024-25 £4.665M — sustained CPI + activity recovery"},
            {"label": "Delivery body", "value": "Trust Procurement + NHS Supply Chain + West Yorkshire ICS collaborative + Catalyst Healthcare PFI residual"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + West Yorkshire ICB"},
            {"label": "Evaluation evidence", "value": "Model Hospital benchmarks; CQC inspection (RWY); Trust ARA disclosure; NHSE EPR shared-tenant reviews"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-Procurement Act 2023 OJEU regime · Successor: ICS-collaborative scaling under PA 2023 + post-2031 Calderdale PFI hand-back"}
        ],
        "notes": "Calderdale and Huddersfield's general supplies & services baseline reflects the two-site DGH footprint (Calderdale Royal Halifax PFI-built + Huddersfield Royal Infirmary), with the trust's role as Cerner / Oracle Health Millennium EPR lead provider for West Yorkshire ICS adding modest training-overhead consumable demand. The Calderdale Royal PFI (Catalyst Healthcare SPV) runs to c. 2031 and is in the active hand-back planning window — post-hand-back, hotel-services routing returns to trust-direct procurement, lifting this line. NHS Supply Chain remains dominant, with West Yorkshire ICS collaborative scaling as the medium-term lever. Industrial action 2023-24 drove cancellation re-stocking churn; April 2025 NIC step-up feeds supplier pricing alongside non-clinical CPI.",
        "sources": [
            {"publisher": "Calderdale and Huddersfield NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.cht.nhs.uk/about-us/our-publications/"},
            {"publisher": "NHS Supply Chain", "title": "Annual Report 2023-24", "url": "https://www.supplychain.nhs.uk/about-us/our-publications/"},
            {"publisher": "Care Quality Commission", "title": "CHFT provider profile (RWY)", "url": "https://www.cqc.org.uk/provider/RWY"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/connecteddigitalsystems/frontline-digitisation/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"}
        ],
        "related": ["Calderdale and Huddersfield NHS Foundation Trust", "Clinical Supplies & Drugs", "NHS Acute Trusts", "General supplies & services — Norfolk and Norwich University Hospitals NHS Foundation Trust", "Frontline Digitisation programme", "NHS Supply Chain"]
    },
    "Business rates — University Hospitals of Leicester NHS Trust": {
        "aliases": [{"name": "Business rates", "parent": "University Hospitals of Leicester NHS Trust"}],
        "description": "UHL's £4.654M business rates line covers non-domestic rates payable on the Leicester Royal Infirmary + Glenfield Hospital + Leicester General Hospital estate, set on the Valuation Office Agency 2023 rating list (effective Apr 2023, AVD 1 Apr 2021) and uplifted by the standard multiplier under LGFA 1988. UHL is among England's largest acute trusts, a New Hospital Programme cohort site (Leicester reconfiguration deferred under January 2025 NHP Reset), and carries an extensive rateable-value footprint across three major hospital sites.",
        "beneficiaries": "c. 17,000 WTE staff serving a c. 1.1M Leicester, Leicestershire and Rutland catchment plus East Midlands tertiary referrals; c. 220,000 ED attendances/yr at Leicester Royal Infirmary ED — among England's busiest single-site EDs; c. 170,000 elective + day-case admissions/yr; Glenfield = East Midlands Congenital Heart Centre.",
        "legal_basis": "Local Government Finance Act 1988 (Sch 6 — non-domestic rating) · Non-Domestic Rating Act 2023 · Non-Domestic Rating (Multipliers and Private Finance) Act 2024 · DHSC Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£4.654M"},
            {"label": "Trust scale", "value": "Three-site major acute (LRI + Glenfield + Leicester General); c. 17,000 WTE"},
            {"label": "VOA list cycle", "value": "2023 rating list (effective Apr 2023, AVD 1 Apr 2021); next revaluation 2026; standard multiplier 54.6p"},
            {"label": "NHP cohort (deferred)", "value": "Leicester reconfiguration in original NHP 40-hospitals; January 2025 NHP Reset deferred rebuild beyond 2030"},
            {"label": "Charity-relief gap", "value": "NHS trusts excluded from 80% mandatory charity relief — direct fiscal cost vs charitable healthcare providers"},
            {"label": "Funding trajectory", "value": "2021-22 c. £4.1M → 2023-24 £4.4M → 2024-25 £4.654M (post-2023 list rebasing + multiplier uplift)"},
            {"label": "NDRA 2024 effect", "value": "Non-Domestic Rating (Multipliers and Private Finance) Act 2024 split multipliers; large hereditaments face higher multiplier from 2026"},
            {"label": "Specialist estate effect", "value": "Glenfield congenital heart + LRI emergency footprint contribute to high RV vs general DGH peers"},
            {"label": "Delivery body", "value": "Trust E&F + Finance + Valuation Office Agency (VOA) + Leicester City Council billing authority"},
            {"label": "Policy owner", "value": "MHCLG (rating policy) + HM Treasury (multiplier) + DHSC + NHSE Provider Finance"},
            {"label": "Evaluation evidence", "value": "VOA rating-list disclosure; Trust ARA premises note; NHSE Estates Return (ERIC); NHP Reset announcement Jan 2025"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2017 rating list baseline · Successor: 2026 revaluation + post-NHP Reset deferred Leicester rebuild trajectory"}
        ],
        "notes": "UHL carries one of England's largest acute-trust business-rates footprints across the three-site Leicester Royal Infirmary + Glenfield + Leicester General estate, reflecting the tertiary specialty mix (East Midlands Congenital Heart Centre at Glenfield, vascular, renal, transplant, neonatal). The 2023 rating list embedded post-pandemic rental and capital-value benchmarks at 1 April 2021 AVD; standard-multiplier uplifts to 54.6p drive annual cost growth. The January 2025 NHP Reset deferred Leicester reconfiguration beyond 2030, freezing the existing-estate rates baseline. The NDRA 2024 split-multiplier regime from 2026 places large hereditaments on a higher multiplier; charity-relief exclusion remains a structural cost gap.",
        "sources": [
            {"publisher": "University Hospitals of Leicester NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.leicestershospitals.nhs.uk/aboutus/our-publications/"},
            {"publisher": "Valuation Office Agency", "title": "2023 rating list — University Hospitals of Leicester (LRI + Glenfield)", "url": "https://www.tax.service.gov.uk/business-rates-find/"},
            {"publisher": "Department of Health and Social Care", "title": "New Hospital Programme — January 2025 Reset", "url": "https://www.gov.uk/government/news/new-hospital-programme-update"},
            {"publisher": "HM Treasury", "title": "Non-Domestic Rating (Multipliers and Private Finance) Act 2024 explanatory notes", "url": "https://www.legislation.gov.uk/ukpga/2024/9/contents"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"}
        ],
        "related": ["University Hospitals of Leicester NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Business rates — Cambridge University Hospitals NHS Foundation Trust", "Business rates — Northumbria Healthcare NHS Foundation Trust", "New Hospital Programme"]
    },
    "Establishment costs — Northern Lincolnshire and Goole NHS Foundation Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "Northern Lincolnshire and Goole NHS Foundation Trust"}],
        "description": "NLAG's £4.630M establishment costs line covers postage, printing, stationery, telephony, training & professional fees, subscriptions, recruitment advertising and minor non-clinical office overhead across the three-site Diana, Princess of Wales (Grimsby) + Scunthorpe General + Goole and District footprint. The trust shares a CEO with United Lincolnshire Hospitals under group-model formation 2023-25, and the line carries integration overhead plus Frontline Digitisation EPR training spend.",
        "beneficiaries": "c. 6,000 WTE staff serving a c. 410,000 northern Lincolnshire catchment (NE Lincs, North Lincs, East Riding cross-flow); c. 145,000 ED attendances/yr (DPoW Grimsby + Scunthorpe EDs); c. 75,000 admissions/yr; long-running operational performance challenges drive inspection + remediation overhead.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£4.630M"},
            {"label": "Trust scale", "value": "Three-site rural acute (Grimsby + Scunthorpe + Goole); c. 6,000 WTE"},
            {"label": "Group-model formation", "value": "Shared CEO with United Lincolnshire Hospitals NHS Trust 2023-25 (Lincolnshire group) — corporate-services integration overhead"},
            {"label": "Frontline Digitisation EPR", "value": "EPR programme drives substantial training & change-management spend through establishment line"},
            {"label": "Operational context", "value": "NHSE Recovery Support Programme + CQC inspection scrutiny — drives enhanced governance + external-advisory professional fees"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove recruitment + training churn"},
            {"label": "April 2025 NIC + CPI uplift", "value": "Indirect via supplier pricing on telephony, training contracts; recruitment-advertising CPI"},
            {"label": "Funding trajectory", "value": "2021-22 c. £3.9M → 2023-24 £4.4M → 2024-25 £4.630M — sustained CPI + group-model integration overhead"},
            {"label": "Delivery body", "value": "Trust Corporate Services + HR + Finance + IT + ULHT-shared functions (post-group) + external training providers"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + NHSE Recovery Support + Humber and North Yorkshire ICB"},
            {"label": "Evaluation evidence", "value": "Model Hospital benchmarks; CQC inspection (RJL); NHSE RSP review; Trust ARA disclosure; group-model business case"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-group stand-alone trust corporate services · Successor: ULHT/NLAG Lincolnshire group consolidated corporate services"}
        ],
        "notes": "NLAG's establishment cost baseline reflects the three-site rural acute footprint (Grimsby + Scunthorpe + Goole) plus the maturing group-model formation with United Lincolnshire Hospitals NHS Trust under shared CEO arrangement 2023-25. Long-running operational performance challenges have placed the trust under NHSE Recovery Support Programme oversight, driving enhanced governance, external-advisory and CQC-remediation professional-fee overhead booked through this line. The Frontline Digitisation EPR programme drives further training spend; industrial action 2023-24 added recruitment churn. Group-consolidated corporate services is the medium-term lever; April 2025 NIC step-up feeds indirectly via supplier pricing.",
        "sources": [
            {"publisher": "Northern Lincolnshire and Goole NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.nlg.nhs.uk/about-us/our-publications/"},
            {"publisher": "Care Quality Commission", "title": "NLAG provider profile (RJL)", "url": "https://www.cqc.org.uk/provider/RJL"},
            {"publisher": "NHS England", "title": "Recovery Support Programme oversight", "url": "https://www.england.nhs.uk/financial-accounting-and-reporting/recovery-support-programme/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Humber and North Yorkshire ICB", "title": "ICB strategy + system plans", "url": "https://humberandnorthyorkshire.icb.nhs.uk/"}
        ],
        "related": ["Northern Lincolnshire and Goole NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "United Lincolnshire Hospitals NHS Trust", "Establishment costs — University Hospitals of Derby and Burton NHS Foundation Trust", "Frontline Digitisation programme"]
    },
    "General supplies & services — North Cumbria Integrated Care NHS Foundation Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "North Cumbria Integrated Care NHS Foundation Trust"}],
        "description": "NCIC's £4.630M general supplies & services line covers non-clinical consumables, linen, catering, hotel-services materials, office supplies and minor expensed equipment across the Cumberland Infirmary Carlisle (PFI 2000) + West Cumberland Hospital Whitehaven + integrated community-services footprint stretching the Cumbrian rural geography. The trust formed 2019 from acute + community integration, and the line spans both acute hotel-services and community-team consumables. NHS Supply Chain national framework dominates routing, with North East and North Cumbria ICS collaborative scaling.",
        "beneficiaries": "c. 6,500 WTE staff serving a c. 320,000 north Cumbria catchment (Carlisle, Eden, Allerdale, Copeland) plus integrated community workforce; c. 90,000 ED attendances/yr (Cumberland Infirmary + West Cumberland EDs); c. 50,000 admissions/yr; community workforce (district nursing) broadens consumables base.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 2 Inventories · Procurement Act 2023 · NHS Act 2006 · Health and Care Act 2022 · IFRIC 12 (PFI hotel-services interface)",
        "key_stats": [
            {"label": "General supplies & services 2024-25", "value": "£4.630M"},
            {"label": "Trust scale", "value": "Two-site acute (Cumberland Infirmary Carlisle + West Cumberland Whitehaven) + integrated community services; c. 6,500 WTE"},
            {"label": "Trust formation", "value": "Formed 1 Oct 2019 from acute + community integration (predecessor North Cumbria University Hospitals + Cumbria Partnership)"},
            {"label": "PFI context", "value": "Cumberland Infirmary PFI signed 1997, operational 2000; Health Management (Carlisle) Ltd SPV — earliest-wave PFI hospital, hand-back nearing"},
            {"label": "Procurement route", "value": "NHS Supply Chain national framework + NENC ICS collaborative + trust-direct + PFI sub-contract residual"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove cancellation re-stocking churn"},
            {"label": "April 2025 NIC + CPI uplift", "value": "Apr 2025 employer-NIC step-up feeds supplier pricing; non-clinical CPI ongoing"},
            {"label": "Funding trajectory", "value": "2021-22 c. £4.0M → 2023-24 £4.4M → 2024-25 £4.630M — sustained CPI + activity recovery"},
            {"label": "Delivery body", "value": "Trust Procurement + NHS Supply Chain + NENC ICS procurement collaborative + Health Management Carlisle PFI residual"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + North East and North Cumbria ICB"},
            {"label": "Evaluation evidence", "value": "Model Hospital benchmarks; CQC inspection (RNN); Trust ARA disclosure; NAO PFI hand-back report 2020"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2019 separate acute + community trusts · Successor: post-2030 PFI hand-back + NENC ICS consolidated procurement"}
        ],
        "notes": "NCIC's general supplies & services baseline reflects the integrated acute + community model formed 2019 — Cumberland Infirmary Carlisle (earliest-wave PFI, signed 1997 / operational 2000 under Health Management (Carlisle) Ltd SPV) plus West Cumberland Hospital Whitehaven plus integrated community workforce. The PFI hotel-services interface routes catering and linen partly through SPV sub-contracts; the c. 2030 expiry sits in the active hand-back planning window flagged by NAO 2020. Post-hand-back, hotel-services routing returns to trust-direct procurement, lifting this line. Industrial action 2023-24 drove re-stocking churn; April 2025 NIC step-up feeds supplier pricing.",
        "sources": [
            {"publisher": "North Cumbria Integrated Care NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.ncic.nhs.uk/about-us/our-publications"},
            {"publisher": "National Audit Office", "title": "Managing PFI assets and services as contracts end (HC 632, 2020)", "url": "https://www.nao.org.uk/reports/managing-pfi-assets-and-services-as-contracts-end/"},
            {"publisher": "NHS Supply Chain", "title": "Annual Report 2023-24", "url": "https://www.supplychain.nhs.uk/about-us/our-publications/"},
            {"publisher": "Care Quality Commission", "title": "NCIC provider profile (RNN)", "url": "https://www.cqc.org.uk/provider/RNN"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"}
        ],
        "related": ["North Cumbria Integrated Care NHS Foundation Trust", "Clinical Supplies & Drugs", "NHS Acute Trusts", "General supplies & services — Calderdale and Huddersfield NHS Foundation Trust", "NHS Supply Chain", "North East and North Cumbria ICB"]
    },
    "Transport (business + patient) — Lewisham and Greenwich NHS Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "Lewisham and Greenwich NHS Trust"}],
        "description": "LGT's £4.610M transport line covers business mileage, inter-site patient transfers and Non-Emergency Patient Transport Services across the University Hospital Lewisham + Queen Elizabeth Hospital Woolwich (PFI-built 2001) two-site acute footprint plus community-team mileage across south-east London. Inter-site clinical transfers between UHL and QEH for specialty pathways, plus tertiary referrals to King's College Hospital MTC, drive PTS demand. London Ambulance Service handles emergency conveyance; accredited NEPTS contractors (re-tendered through SE London ICS) handle non-emergency transport.",
        "beneficiaries": "c. 6,500 WTE staff serving a c. 750,000 Lewisham + Greenwich catchment (high IMD deprivation); c. 240,000 ED attendances/yr (UHL + QEH EDs combined — among London's busiest 2-site combined volumes); c. 95,000 admissions/yr; large maternity unit at QEH.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · IFRS 16 Leases (pool fleet) · NHS Act 2006 · NHSE Patient Transport Services Eligibility Framework 2022 · HMRC AMAP · NHS AfC Section 17 · Mental Health Act 1983 (s.135/136 conveyance)",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£4.610M"},
            {"label": "Trust scale", "value": "Two-site acute (UHL Lewisham + QEH Woolwich); c. 6,500 WTE"},
            {"label": "PFI context", "value": "QEH Woolwich PFI signed 1998, operational 2001; Meridian Hospital Company SPV — drives inter-site transfer profile"},
            {"label": "ED throughput + tertiary referrals", "value": "c. 240,000 ED attendances/yr (UHL + QEH combined); major-trauma transfers to King's MTC; cardiothoracic to St Thomas'/Royal Brompton"},
            {"label": "PTS provider mix", "value": "London Ambulance Service (emergency) + accredited NEPTS contractors (ERS Medical / DHL) re-tendered via SE London ICS"},
            {"label": "Pool fleet (IFRS 16)", "value": "Right-of-use depreciation + interest on leased pool vehicles for AHPs + community teams; AfC S17 / HMRC AMAP staff mileage"},
            {"label": "Industrial action 2023-24 effect", "value": "Strike days drove ad-hoc inter-site transfers + locum mileage claims"},
            {"label": "Funding trajectory", "value": "2021-22 c. £3.7M → 2023-24 £4.3M → 2024-25 £4.610M — fuel CPI + activity recovery"},
            {"label": "Delivery body", "value": "Trust E&F + Travel team + LAS + accredited NEPTS contractors + SE London ICS NEPTS commissioning"},
            {"label": "Policy owner", "value": "NHSE London + DHSC + NHSE Urgent and Emergency Care + South East London ICB"},
            {"label": "Evaluation evidence", "value": "NHSE PTS framework review; CQC inspection (RJ2); Trust ARA disclosure; SE London ICS NEPTS contract outcome"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2013 split (formed from South London Healthcare reconfiguration) · Successor: SE London ICS NEPTS re-tender"}
        ],
        "notes": "Lewisham and Greenwich's transport line is shaped by the two-site acute footprint — University Hospital Lewisham plus the PFI-built Queen Elizabeth Hospital Woolwich (Meridian Hospital Company SPV from 2001) — and inter-site clinical transfer profile for specialty pathways and admission balancing. Tertiary referrals to King's MTC for major trauma and to St Thomas'/Royal Brompton for cardiothoracic add a further inter-trust PTS demand layer. LAS handles emergency conveyance; accredited NEPTS contractors operate under SE London ICS commissioning. The IFRS 16 2022 pool-fleet transition split right-of-use depreciation and interest into the line; fuel CPI and April 2025 NIC step-up feed forward via contractor pricing.",
        "sources": [
            {"publisher": "Lewisham and Greenwich NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.lewishamandgreenwich.nhs.uk/our-publications"},
            {"publisher": "NHS England", "title": "Non-Emergency Patient Transport Services — Eligibility Framework 2022", "url": "https://www.england.nhs.uk/publication/non-emergency-patient-transport-services-eligibility-framework/"},
            {"publisher": "Care Quality Commission", "title": "Lewisham and Greenwich provider profile (RJ2)", "url": "https://www.cqc.org.uk/provider/RJ2"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "South East London ICB", "title": "ICB strategy + system plans", "url": "https://www.selondonics.org/"}
        ],
        "related": ["Lewisham and Greenwich NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Transport (business + patient) — Royal Cornwall Hospitals NHS Trust", "London Ambulance Service NHS Trust", "South East London ICB"]
    },
    "PFI / LIFT charges — Tameside and Glossop Integrated Care NHS Foundation Trust": {
        "aliases": [{"name": "PFI / LIFT charges", "parent": "Tameside and Glossop Integrated Care NHS Foundation Trust"}],
        "description": "Tameside and Glossop's £4.587M PFI/LIFT charge reflects the unitary-charge pass-through on the Tameside Hospital PFI (the new acute hospital build, signed 2003, operational 2007 — Catalyst Healthcare (Tameside) Ltd SPV with Carillion as original FM). Carillion's January 2018 collapse triggered FM novation to Engie/Equans, mid-contract. The 2007-2042 35-year concession runs c. 18 more years, with debt-service amortising and indexed soft-FM uplifts feeding modest annual cost growth. Trust integrates Glossop community services (north-west Derbyshire pocket).",
        "beneficiaries": "c. 4,500 WTE staff serving a c. 250,000 Tameside borough catchment plus c. 30,000 Glossop community-services population; c. 100,000 ED attendances/yr at Tameside ED; c. 50,000 admissions/yr; PFI estate covers main Tameside Hospital site (acute + women's & children's + maternity).",
        "legal_basis": "IFRIC 12 Service Concession Arrangements · IFRS 16 Leases (post-2022 transition) · DHSC Group Accounting Manual 2024-25 ch.7 · Private Finance Initiative guidance (HM Treasury) · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "PFI / LIFT charges 2024-25", "value": "£4.587M"},
            {"label": "PFI vehicle", "value": "Tameside Hospital PFI signed 2003, operational 2007; Catalyst Healthcare (Tameside) Ltd SPV"},
            {"label": "Contract end date", "value": "c. 2042 (35-year concession from operational date)"},
            {"label": "Carillion 2018 effect", "value": "Carillion (original FM contractor) Jan 2018 collapse → Engie/Equans novation; ongoing FM contract churn"},
            {"label": "Estate covered", "value": "Tameside Hospital — main acute site (acute medicine + W&C + maternity, c. 470 beds)"},
            {"label": "Unitary charge composition", "value": "Senior + subordinated debt service + lifecycle hard-FM + RPI-indexed soft-FM (cleaning, catering, portering)"},
            {"label": "Funding trajectory", "value": "Recent line c. £4-5M post-IFRS 16 split; whole-PFI annual unitary charge significantly larger pre-split"},
            {"label": "IFRS 16 split", "value": "Post-2022 IFRS 16 transition: lease element to depreciation/interest; service-concession soft-FM remains in PFI/LIFT line"},
            {"label": "Delivery body", "value": "Catalyst Healthcare (Tameside) Ltd SPV + Engie/Equans (post-Carillion FM) + trust E&F oversight"},
            {"label": "Policy owner", "value": "DHSC + HM Treasury PFI guidance + NHSE Provider Finance + Greater Manchester ICB"},
            {"label": "Evaluation evidence", "value": "NAO PFI 2018 + PFI hand-back report 2020; Trust ARA disclosure; CQC inspection (RMP)"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-PFI Tameside General Hospital (1950s estate) · Successor: 2042 hand-back + Greater Manchester ICS group-level estate planning"}
        ],
        "notes": "Tameside and Glossop's PFI/LIFT line reflects the Tameside Hospital PFI (signed 2003, operational 2007) under the Catalyst Healthcare (Tameside) Ltd SPV — a 35-year concession running to c. 2042 with c. 18 years remaining. Carillion's January 2018 collapse triggered FM novation to Engie/Equans on the hard and soft FM elements, adding contract-management complexity layered on the SPV structure. Post-2022 IFRS 16 split moves the lease element to depreciation/interest, leaving service-concession soft-FM in this line. RPI-linked indexation on soft-FM continues to lift cost; debt-service balance amortises down. Greater Manchester ICS estate-planning shapes medium-term direction; hand-back planning starts mid-contract per IPA/HMT framework.",
        "sources": [
            {"publisher": "Tameside and Glossop Integrated Care NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.tamesidehospital.nhs.uk/About-Us/our-publications.htm"},
            {"publisher": "National Audit Office", "title": "PFI and PF2 (HC 718, 2018)", "url": "https://www.nao.org.uk/reports/pfi-and-pf2/"},
            {"publisher": "National Audit Office", "title": "Managing PFI assets and services as contracts end (HC 632, 2020)", "url": "https://www.nao.org.uk/reports/managing-pfi-assets-and-services-as-contracts-end/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 7 — Leases and service concessions)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Tameside and Glossop provider profile (RMP)", "url": "https://www.cqc.org.uk/provider/RMP"}
        ],
        "related": ["Tameside and Glossop Integrated Care NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "PFI / LIFT charges — Sherwood Forest Hospitals NHS Foundation Trust", "PFI / LIFT charges — Worcestershire Acute Hospitals NHS Trust", "Greater Manchester ICB"]
    },
    "Amortisation — Frimley Health NHS Foundation Trust": {
        "aliases": [{"name": "Amortisation", "parent": "Frimley Health NHS Foundation Trust"}],
        "description": "Frimley Health's £4.582M amortisation line covers the systematic write-down of capitalised intangible assets — software licences, the Cerner / Oracle Health Millennium EPR (Frimley is the Surrey Heartlands and Frimley ICS Cerner shared-tenant lead), capitalised configuration costs, radiology PACS, internally-generated clinical applications and acquired digital systems — across Frimley Park Hospital + Wexham Park Hospital + Heatherwood Hospital. Frimley Park is in the New Hospital Programme cohort (Cohort 2 — RAAC; Heatherwood replacement opened 2022).",
        "beneficiaries": "c. 9,500 WTE staff serving a c. 900,000 Surrey + Berkshire + Hampshire catchment; c. 220,000 ED attendances/yr (Frimley Park + Wexham Park EDs combined); c. 130,000 admissions/yr; lead Cerner / Oracle Health Millennium digital provider for Frimley + Surrey Heartlands ICS shared tenant.",
        "legal_basis": "IAS 38 Intangible Assets · DHSC Group Accounting Manual 2024-25 ch.5 · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£4.582M"},
            {"label": "Trust scale", "value": "Three-site acute (Frimley Park + Wexham Park + Heatherwood); c. 9,500 WTE"},
            {"label": "EPR lead provider", "value": "Cerner / Oracle Health Millennium — Frimley is Surrey Heartlands + Frimley ICS shared-tenant lead serving multiple ICS trusts"},
            {"label": "RAAC + NHP context", "value": "Frimley Park flagged in RAAC concrete-plank cohort (Sep 2023 HSSIB list); Cohort 2 NHP rebuild — Jan 2025 Reset confirmed"},
            {"label": "Heatherwood replacement", "value": "New Heatherwood Hospital opened Mar 2022 (£94M new-build) — capitalised intangible config + digital fit-out feeding amortisation"},
            {"label": "UEL convention", "value": "Typical 5-10 year UEL per DHSC GAM ch.5; EPR licences typically 5-7 yr; PACS 5 yr"},
            {"label": "Funding trajectory", "value": "2021-22 c. £3.5M → 2023-24 £4.3M → 2024-25 £4.582M — Frontline Digitisation + Heatherwood replacement capitalisation feeding amortisation"},
            {"label": "April 2025 NIC + CPI uplift", "value": "Indirect via supplier maintenance pricing absorbed in IT operating contracts (not amortisation)"},
            {"label": "Delivery body", "value": "Trust IT + Finance + Frontline Digitisation programme + Cerner / Oracle Health vendor"},
            {"label": "Policy owner", "value": "NHSE Frontline Digitisation + DHSC + NHSE Provider Finance + Frimley ICB + Surrey Heartlands ICB"},
            {"label": "Evaluation evidence", "value": "NHSE digital maturity assessment; HSSIB RAAC report; NHP Reset Jan 2025; Trust ARA intangible-asset note"},
            {"label": "Predecessor / successor", "value": "Predecessor: legacy paper-light + early Cerner deployment · Successor: full Cerner/OH shared-tenant ICS rollout + post-NHP Frimley Park rebuild capitalised digital fit-out"}
        ],
        "notes": "Frimley Health's amortisation line is principally driven by capitalised Cerner / Oracle Health Millennium EPR licences and configuration costs — Frimley is the Surrey Heartlands and Frimley ICS Cerner shared-tenant lead, serving multiple regional acute trusts under one tenant. The Heatherwood Hospital replacement (£94M new-build opened March 2022) added capitalised intangible configuration and digital fit-out costs flowing through IAS 38 over typical 5-10 year UELs. Frimley Park is in the September 2023 HSSIB RAAC concrete-plank cohort and was confirmed in Cohort 2 of the NHP under the January 2025 Reset, fixing the rebuild trajectory. Indirect supplier maintenance CPI sits in operating contracts rather than amortisation.",
        "sources": [
            {"publisher": "Frimley Health NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.fhft.nhs.uk/about-us/publications/"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/connecteddigitalsystems/frontline-digitisation/"},
            {"publisher": "Department of Health and Social Care", "title": "New Hospital Programme — January 2025 Reset", "url": "https://www.gov.uk/government/news/new-hospital-programme-update"},
            {"publisher": "Health Services Safety Investigations Body", "title": "RAAC in NHS healthcare buildings (Sep 2023 listing)", "url": "https://www.hssib.org.uk/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 5 — Intangible assets)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"}
        ],
        "related": ["Frimley Health NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Amortisation — United Lincolnshire Hospitals NHS Trust", "Frontline Digitisation programme", "New Hospital Programme"]
    },
    "Establishment costs — Gateshead Health NHS Foundation Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "Gateshead Health NHS Foundation Trust"}],
        "description": "Gateshead Health's £4.571M establishment costs line covers postage, telephony, stationery, training & professional fees, subscriptions, recruitment advertising and minor non-clinical office overhead at the Queen Elizabeth Hospital Gateshead plus Bensham Hospital and community-services footprint. The trust runs a regional pathology hub serving multiple NENC ICS trusts — drives non-clinical professional-fee and training overhead. Frontline Digitisation EPR rollout and industrial-action 2023-24 recruitment churn shape the recent trajectory.",
        "beneficiaries": "c. 4,500 WTE staff serving a c. 200,000 Gateshead borough catchment plus regional pathology service to multiple NENC trusts; c. 95,000 ED attendances/yr at QE Gateshead ED; c. 50,000 admissions/yr; pathology hub serves regional NENC tertiary networks.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · NHS Act 2006 · Health and Care Act 2022 · NHS Standard Contract 2024-25",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£4.571M"},
            {"label": "Trust scale", "value": "Single-site acute (QE Gateshead) + Bensham Hospital + community services; c. 4,500 WTE"},
            {"label": "Pathology hub", "value": "Trust pathology service operates as regional hub across NENC ICS — drives professional fees + training overhead"},
            {"label": "Frontline Digitisation EPR", "value": "EPR programme drives substantial training & change-management spend through establishment line"},
            {"label": "Industrial action 2023-24 effect", "value": "44 days junior-doctor + 10 days consultant strikes drove recruitment + training churn"},
            {"label": "April 2025 NIC + CPI uplift", "value": "Indirect via supplier pricing on telephony, training, recruitment-advertising contracts"},
            {"label": "Funding trajectory", "value": "2021-22 c. £3.9M → 2023-24 £4.3M → 2024-25 £4.571M — sustained CPI on professional fees + telephony + training"},
            {"label": "NHSE NENC group context", "value": "Trust within North East and North Cumbria ICS provider collaborative — shared corporate-services scaling potential"},
            {"label": "Delivery body", "value": "Trust Corporate Services + HR + Finance + IT (telephony) + external training providers"},
            {"label": "Policy owner", "value": "NHSE Provider Finance + DHSC + North East and North Cumbria ICB"},
            {"label": "Evaluation evidence", "value": "Model Hospital benchmarks (corporate services); CQC inspection (RR7); Trust ARA disclosure"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-Frontline Digitisation paper-baseline · Successor: NENC ICS shared-corporate-services scaling"}
        ],
        "notes": "Gateshead Health's establishment cost baseline reflects the QE Gateshead acute site plus Bensham Hospital and community-services footprint, with the trust's regional pathology hub serving multiple North East and North Cumbria ICS trusts adding non-clinical professional-fee and training overhead. The Frontline Digitisation EPR programme drives training and change-management spend booked through this line. Industrial action 2023-24 added recruitment-cycle churn and locum-onboarding overhead. NENC ICS provider-collaborative shared-corporate-services scaling is the medium-term lever, with April 2025 NIC step-up feeding indirectly via supplier and agency pricing on telephony, training and recruitment-advertising contracts.",
        "sources": [
            {"publisher": "Gateshead Health NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.gateshealth.nhs.uk/about-us/publications/"},
            {"publisher": "Care Quality Commission", "title": "Gateshead Health provider profile (RR7)", "url": "https://www.cqc.org.uk/provider/RR7"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/connecteddigitalsystems/frontline-digitisation/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "North East and North Cumbria ICB", "title": "ICB strategy + provider collaborative", "url": "https://northeastnorthcumbria.nhs.uk/"}
        ],
        "related": ["Gateshead Health NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Establishment costs — University Hospitals of Derby and Burton NHS Foundation Trust", "Establishment costs — Northern Lincolnshire and Goole NHS Foundation Trust", "North East and North Cumbria ICB"]
    },
    "Business rates — Northumbria Healthcare NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "Northumbria Healthcare NHS Foundation Trust"}],
        "description": "Northumbria Healthcare's £4.569M business rates line covers non-domestic rates payable on the Northumbria Specialist Emergency Care Hospital (Cramlington, opened 2015) + Wansbeck General + North Tyneside General + Hexham General + community-hospital footprint, set on the Valuation Office Agency 2023 rating list (effective Apr 2023, AVD 1 Apr 2021) and uplifted by the standard multiplier under LGFA 1988. The trust runs England's first purpose-built specialist emergency care hospital, with a distinctive multi-site rural-urban estate spanning Northumberland and North Tyneside.",
        "beneficiaries": "c. 11,500 WTE staff serving a c. 500,000 Northumberland + North Tyneside catchment; c. 200,000 ED attendances/yr (NSECH 24/7 emergency + minor injury units across sites); c. 90,000 admissions/yr; large rural community-hospital footprint adds RV breadth.",
        "legal_basis": "Local Government Finance Act 1988 (Sch 6 — non-domestic rating) · Non-Domestic Rating Act 2023 · Non-Domestic Rating (Multipliers and Private Finance) Act 2024 · DHSC Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£4.569M"},
            {"label": "Trust scale", "value": "Multi-site (NSECH + Wansbeck + N Tyneside + Hexham + 5 community hospitals); c. 11,500 WTE"},
            {"label": "NSECH context", "value": "Northumbria Specialist Emergency Care Hospital (Cramlington, opened Jun 2015) — England's first purpose-built specialist emergency care hospital"},
            {"label": "VOA list cycle", "value": "2023 rating list (effective Apr 2023, AVD 1 Apr 2021); next revaluation 2026; standard multiplier 54.6p"},
            {"label": "Rural community-hospital footprint", "value": "Substantial rural community-hospital + minor-injury-unit footprint adds RV breadth across Northumberland"},
            {"label": "Charity-relief gap", "value": "NHS trusts excluded from 80% mandatory charity relief — direct fiscal cost vs charitable healthcare providers"},
            {"label": "Funding trajectory", "value": "2021-22 c. £4.0M → 2023-24 £4.3M → 2024-25 £4.569M (post-2023 list rebasing + multiplier uplift)"},
            {"label": "NDRA 2024 effect", "value": "Non-Domestic Rating (Multipliers and Private Finance) Act 2024 split multipliers; large hereditaments face higher multiplier from 2026"},
            {"label": "Delivery body", "value": "Trust E&F + Finance + Valuation Office Agency (VOA) + Northumberland CC + North Tyneside Council billing authorities"},
            {"label": "Policy owner", "value": "MHCLG (rating policy) + HM Treasury (multiplier) + DHSC + NHSE Provider Finance"},
            {"label": "Evaluation evidence", "value": "VOA rating-list disclosure; Trust ARA premises note; NHSE Estates Return (ERIC)"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2017 rating list baseline + pre-NSECH multi-site emergency model · Successor: 2026 revaluation + NDRA 2024 split-multiplier regime"}
        ],
        "notes": "Northumbria Healthcare's business-rates baseline reflects England's most distinctive multi-site emergency-care estate — the Northumbria Specialist Emergency Care Hospital (NSECH) at Cramlington, opened June 2015 as England's first purpose-built specialist emergency-care hospital, plus legacy Wansbeck, North Tyneside and Hexham General sites retaining minor-injury, day-case and elective functions, plus a Northumberland rural community-hospital footprint. The 2023 rating list embedded post-pandemic capital-value benchmarks at 1 April 2021 AVD; 54.6p multiplier uplifts drive annual growth. NHS-trust exclusion from 80% charity relief is a structural cost gap. NDRA 2024 from 2026 places larger hereditaments on a higher multiplier.",
        "sources": [
            {"publisher": "Northumbria Healthcare NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.northumbria.nhs.uk/about-us/our-publications/"},
            {"publisher": "Valuation Office Agency", "title": "2023 rating list — Northumbria Healthcare (NSECH + sites)", "url": "https://www.tax.service.gov.uk/business-rates-find/"},
            {"publisher": "Ministry of Housing, Communities and Local Government", "title": "Business rates — non-domestic rating multipliers 2024-25", "url": "https://www.gov.uk/government/publications/business-rates-multipliers"},
            {"publisher": "HM Treasury", "title": "Non-Domestic Rating (Multipliers and Private Finance) Act 2024 explanatory notes", "url": "https://www.legislation.gov.uk/ukpga/2024/9/contents"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"}
        ],
        "related": ["Northumbria Healthcare NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Business rates — Cambridge University Hospitals NHS Foundation Trust", "Business rates — University Hospitals of Leicester NHS Trust", "Valuation Office Agency"]
    },
}
