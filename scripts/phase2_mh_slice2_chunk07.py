# -*- coding: utf-8 -*-
# Phase 2 MH slice 2 — chunk 07 (17 NHS Mental Health Trust orphan sub-lines)
# Hand-curated trust-specific PROGRAMME-archetype enrichment entries.
# Structural contract per docs/archetype_briefs.md.

NEW = {
    "Amortisation — Kent and Medway NHS and Social Care Partnership Trust": {
        "aliases": [{"name": "Amortisation", "parent": "Kent and Medway NHS and Social Care Partnership Trust"}],
        "description": "KMPT's £1.32M 2024-25 amortisation charge is IAS 38 depreciation of the trust's intangible-asset base — predominantly capitalised electronic patient record (Rio EPR) software, NHSmail integration, e-prescribing modules and capitalised training under the Frontline Digitisation programme. KMPT was a wave-1 Frontline Digitisation beneficiary in 2022-23, with software deployed across St Martin's Hospital (Canterbury), Priority House (Maidstone), Littlebrook (Dartford) and community-MH bases — generating recurring 5-7 year amortisation charges.",
        "beneficiaries": "c. 3,800 staff using the Rio EPR + ancillary clinical-systems estate across c. 70 inpatient + community-MH sites; serves a registered population c. 1.85M across Kent and Medway; clinical record covers c. 50,000 active service users.",
        "legal_basis": "IAS 38 Intangible Assets · DHSC Group Accounting Manual 2024-25 ch.5 · NHS Act 2006 · Health and Care Act 2022 · Data Protection Act 2018 (clinical-system data-controller obligations)",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£1.32M"},
            {"label": "Useful-economic-life policy", "value": "5-7 years software per DHSC GAM 2024-25 ch.5; longer for fundamental EPR platforms"},
            {"label": "Primary intangible asset", "value": "Rio EPR (Servelec / now Access Group) — KMPT instance with Frontline Digitisation enhancements"},
            {"label": "Frontline Digitisation wave", "value": "Wave-1 beneficiary 2022-23 — c. £4-6M capitalised software + implementation cost driving recurring amortisation"},
            {"label": "Site footprint covered", "value": "St Martin's Hospital (Canterbury) + Priority House (Maidstone) + Littlebrook (Dartford) + c. 60 community bases"},
            {"label": "Composition", "value": "EPR software + e-prescribing modules + NHSmail integration + capitalised training + bespoke development"},
            {"label": "Funding trajectory", "value": "Pre-2022 c. £0.4M → 2022-23 c. £0.9M → 2024-25 £1.32M — step-up tracking Frontline Digitisation capitalisation cycle"},
            {"label": "Delivery body", "value": "Trust Digital + Finance teams; vendor Access Group (Rio); programme oversight via NHSE Frontline Digitisation"},
            {"label": "Policy owner", "value": "DHSC + NHSE Transformation Directorate · Kent and Medway ICB · Frontline Digitisation programme"},
            {"label": "Evaluation evidence", "value": "NHSE Frontline Digitisation programme reporting; trust ARA 2023-24 intangible-asset note; Digital Maturity Assessment"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2018 paper-heavy clinical record + legacy patient-administration · Successor: full digital-maturity-level-5 EPR by 2026 under Frontline Digitisation completion"}
        ],
        "notes": "KMPT's amortisation line stepped up sharply after wave-1 Frontline Digitisation capitalisation in 2022-23 — capitalised EPR software, integration work and training now feed a 5-7 year amortisation tail per IAS 38 + DHSC GAM ch.5. The trust uses Rio (Access Group, formerly Servelec) as its core MH EPR; the Frontline Digitisation enhancements added e-prescribing, integrated risk-assessment and outcome-measure modules. KMPT's history of CQC scrutiny on community-MH safety (sustained inspection cycle 2019-2024) made digital-maturity progression a priority, with Kent and Medway ICB co-investing under the integrated-care-record programme. Recurring amortisation will plateau c. 2026-27 then taper as wave-1 software fully amortises.",
        "sources": [
            {"publisher": "Kent and Medway NHS and Social Care Partnership Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.kmpt.nhs.uk/about-us/publications/"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/frontline-digitisation/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 5 — Intangible assets)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "KMPT provider profile (RXY)", "url": "https://www.cqc.org.uk/provider/RXY"},
            {"publisher": "Kent and Medway Integrated Care Board", "title": "Digital and integrated-care-record strategy", "url": "https://www.kentandmedway.icb.nhs.uk/"}
        ],
        "related": ["Kent and Medway NHS and Social Care Partnership Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Department of Health and Social Care", "Amortisation — Oxford Health NHS Foundation Trust", "Frontline Digitisation programme"]
    },
    "Business rates — Tavistock and Portman NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "Tavistock and Portman NHS Foundation Trust"}],
        "description": "Tavistock and Portman's £1.30M 2024-25 business-rates charge is structurally elevated by the trust's central-London hereditament concentration — the Tavistock Centre (120 Belsize Lane, NW3) and the Portman Clinic (8 Fitzjohn's Avenue, NW3), plus ancillary training space. Camden's high commercial rateable values, applied at 49.9p small / 54.6p standard 2024-25 UBR, dominate. The 2024 closure of the Gender Identity Development Service (GIDS) following the Cass Review reshaped occupancy patterns but left the core hereditaments rated.",
        "beneficiaries": "c. 750 staff at the Tavistock Centre + Portman Clinic plus dispersed national training and consultancy services; serves c. 6,000 active service users in psychotherapy, child + adolescent psychotherapy, complex trauma and forensic psychotherapy across a national catchment for specialist tertiary-MH services.",
        "legal_basis": "Local Government Finance Act 1988 (Schedule 6 valuation) · Non-Domestic Rating (Multipliers and Private Finance) Act 2024 · Non-Domestic Rating Act 2023 · NHS Act 2006 · Health and Care Act 2022 · DHSC GAM 2024-25",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£1.30M"},
            {"label": "Hereditament profile", "value": "Tavistock Centre (120 Belsize Lane, NW3) + Portman Clinic (8 Fitzjohn's Avenue, NW3) + ancillary training space"},
            {"label": "Billing authority", "value": "London Borough of Camden"},
            {"label": "UBR 2024-25", "value": "49.9p small-multiplier / 54.6p standard-multiplier — frozen at 2023-24 levels under Autumn Statement 2023"},
            {"label": "London RV premium", "value": "Belsize / Fitzjohn's Avenue postcodes carry 2-3× national-average RV per m² for institutional occupiers"},
            {"label": "Charitable exemption", "value": "Not applicable — NHS FTs are not registered charities under Charities Act 2011"},
            {"label": "VOA 2023 revaluation impact", "value": "Camden NHS hereditament RVs rebased modestly downward post-pandemic"},
            {"label": "Cass Review / GIDS context", "value": "GIDS closed Mar 2024 following Cass Review; hereditaments retained for residual psychotherapy + training services"},
            {"label": "Funding trajectory", "value": "2020-21 c. £1.05M → 2024-25 £1.30M — uplift tracks frozen UBR + small ancillary-space additions"},
            {"label": "Delivery body", "value": "Trust Estates + VOA (rateable value) + LB Camden (billing)"},
            {"label": "Policy owner", "value": "DHSC + MHCLG (business rates policy) + NHSE Provider Finance + North Central London ICB"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2017 antecedent valuation date list · Successor: 2026 next revaluation under NDRA 2023 3-year cycle; potential trust-merger restructuring under NCL ICB review"}
        ],
        "notes": "Tavistock and Portman is one of the smallest NHS FTs by turnover but carries a disproportionately high business-rates ratio because both core hereditaments sit in Camden's premium commercial RV band. The trust's national tertiary-psychotherapy role does not generate Section 65A charitable exemption (NHS FTs are not registered charities). The 2024 closure of the Gender Identity Development Service following the Cass Review and the planned trust-merger under North Central London ICB strategic review have created uncertainty about future hereditament occupancy, but rates remain payable on currently-occupied space at full UBR. The 2026 VOA revaluation under the NDRA 2023 3-year cycle is the next reset point.",
        "sources": [
            {"publisher": "Tavistock and Portman NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://tavistockandportman.nhs.uk/about-us/publications/"},
            {"publisher": "Valuation Office Agency", "title": "Find a business rates valuation (Camden NHS hereditaments)", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "Department for Levelling Up, Housing and Communities", "title": "Business rates — multipliers and reliefs 2024-25", "url": "https://www.gov.uk/introduction-to-business-rates"},
            {"publisher": "NHS England", "title": "Cass Review independent review of gender identity services", "url": "https://cass.independent-review.uk/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"}
        ],
        "related": ["Tavistock and Portman NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Department of Health and Social Care", "Business rates — Central and North West London NHS Foundation Trust", "Valuation Office Agency"]
    },
    "Amortisation — Berkshire Healthcare NHS Foundation Trust": {
        "aliases": [{"name": "Amortisation", "parent": "Berkshire Healthcare NHS Foundation Trust"}],
        "description": "Berkshire Healthcare's £1.29M 2024-25 amortisation charge is IAS 38 depreciation of the trust's intangible-asset base — capitalised electronic patient record software (Rio EPR), e-prescribing modules, integration to BOB (Buckinghamshire, Oxfordshire and Berkshire) shared-care record, capitalised training and bespoke development under the Frontline Digitisation programme. As a CQC 'Outstanding'-rated trust, Berkshire Healthcare has invested ahead of peers in digital maturity, accelerating the capitalisation cycle and the recurring 5-7 year amortisation tail.",
        "beneficiaries": "c. 4,500 staff using the Rio EPR + integrated clinical systems across c. 100+ inpatient + community sites covering all 6 Berkshire unitary authorities (Reading, Slough, Bracknell Forest, Windsor and Maidenhead, West Berkshire, Wokingham); active clinical record covers c. 200,000 service-user contacts/yr.",
        "legal_basis": "IAS 38 Intangible Assets · DHSC Group Accounting Manual 2024-25 ch.5 · NHS Act 2006 · Health and Care Act 2022 · Data Protection Act 2018",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£1.29M"},
            {"label": "Useful-economic-life policy", "value": "5-7 years software per DHSC GAM 2024-25 ch.5"},
            {"label": "Primary intangible asset", "value": "Rio EPR (Access Group) — Berkshire Healthcare instance with Frontline Digitisation enhancements"},
            {"label": "Frontline Digitisation status", "value": "Trust progressed digital-maturity investment ahead of national programme; sustained capitalisation 2020-2024"},
            {"label": "Site footprint covered", "value": "Prospect Park Hospital + Wokingham CH + Bracknell Healthspace + Upton + West Berks CH + 100+ community bases"},
            {"label": "Composition", "value": "EPR software + e-prescribing + BOB shared-care-record integration + capitalised training + bespoke development"},
            {"label": "BOB shared-care-record", "value": "Connection to Buckinghamshire, Oxfordshire and Berkshire West ICB shared-care-record platform — capitalised integration cost amortised"},
            {"label": "Funding trajectory", "value": "2020-21 c. £0.6M → 2024-25 £1.29M — sustained growth tracking digital-maturity investment + ongoing capitalisation"},
            {"label": "Delivery body", "value": "Trust Digital Services + Finance + vendor Access Group (Rio); programme oversight via NHSE Frontline Digitisation"},
            {"label": "Policy owner", "value": "DHSC + NHSE Transformation Directorate · Buckinghamshire, Oxfordshire and Berkshire West ICB / Frimley ICB · Frontline Digitisation programme"},
            {"label": "Evaluation evidence", "value": "CQC 'Outstanding' rating sustained 2019-2024 cites digital-maturity investment; NHSE Digital Maturity Assessment; trust ARA 2023-24"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2017 paper-based clinical record · Successor: full digital-maturity-level-5 EPR by 2026 + ICS-wide shared-care-record integration"}
        ],
        "notes": "Berkshire Healthcare's amortisation line reflects deliberate above-peer investment in digital maturity, which underpins the trust's CQC 'Outstanding' rating sustained since 2019. The capitalisation cycle has been continuous rather than concentrated in a single Frontline Digitisation wave — Rio EPR enhancements, e-prescribing, BOB shared-care-record integration and bespoke clinical-decision-support tools have been progressively capitalised and entered amortisation. The trust split across two ICBs (BOB for the western boroughs, Frimley for the eastern boroughs) creates dual integration overheads, both capitalised. Amortisation will plateau c. 2026-27 as the bulk of wave-1 software fully amortises and Frontline Digitisation programme funding completes.",
        "sources": [
            {"publisher": "Berkshire Healthcare NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.berkshirehealthcare.nhs.uk/about-us/publications-and-policies/"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/frontline-digitisation/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 5 — Intangible assets)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Berkshire Healthcare NHS FT provider profile (RWX)", "url": "https://www.cqc.org.uk/provider/RWX"},
            {"publisher": "Buckinghamshire, Oxfordshire and Berkshire West ICB", "title": "Digital and shared-care-record strategy", "url": "https://www.bucksoxonberksw.icb.nhs.uk/"}
        ],
        "related": ["Berkshire Healthcare NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Department of Health and Social Care", "Amortisation — Oxford Health NHS Foundation Trust", "Frontline Digitisation programme"]
    },
    "Transport (business + patient) — South West London and St George's Mental Health NHS Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "South West London and St George's Mental Health NHS Trust"}],
        "description": "SWLSTG's £1.23M transport line covers staff business mileage for community-MH and crisis teams across Wandsworth, Merton, Sutton, Kingston and Richmond, plus inter-site transfers between Springfield University Hospital (Tooting), the Phoenix Wing, Tolworth Hospital and dispersed community-MH bases. The Springfield Village redevelopment (2018-2024, with Sir William Atkinson Wing 2024) has reshaped site occupancy; transport demand was sustained by ongoing community-team home visits and MHA conveyance of detained patients across the south-west London footprint.",
        "beneficiaries": "c. 2,700 staff serving c. 1.1M residents across 5 SW London boroughs; c. 350 inpatient beds at Springfield + Tolworth + Phoenix Wing; serves national specialist eating-disorders + perinatal-MH catchments.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · NHS Act 2006 · Mental Health Act 1983 (s.135/136 conveyance) · Health and Care Act 2022 · HMRC Approved Mileage Allowance Payments",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£1.23M"},
            {"label": "Site footprint", "value": "Springfield University Hospital (Tooting) + Tolworth Hospital + Phoenix Wing + community-MH bases across 5 boroughs"},
            {"label": "Catchment", "value": "Wandsworth + Merton + Sutton + Kingston + Richmond — c. 1.1M residents"},
            {"label": "Springfield Village context", "value": "Major redevelopment 2018-2024; new acute-MH wards + Trinity Building + Sir William Atkinson Wing — reshaped inter-site movement"},
            {"label": "MHA conveyance share", "value": "s.136 / s.135 conveyance contracted via LAS + private secure-transport providers"},
            {"label": "Staff mileage rate", "value": "NHS Agenda for Change Section 17 / HMRC AMAP 45p first 10,000 miles, 25p thereafter"},
            {"label": "ULEZ / EV transition", "value": "Trust fleet operating within London-wide ULEZ; salary-sacrifice EV scheme supports staff personal-fleet transition"},
            {"label": "Funding trajectory", "value": "2020-21 c. £0.95M → 2024-25 £1.23M — uplift driven by post-pandemic visit recovery + fuel CPI + ULEZ-compatible fleet renewal"},
            {"label": "Delivery body", "value": "Trust Estates + Travel team; PTS contracted with London Ambulance Service + accredited secure-transport providers"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + South West London ICB"},
            {"label": "Evaluation evidence", "value": "CQC inspection reports; Springfield Village impact assessment; SWL ICS estate review"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-redevelopment dispersed Springfield campus · Successor: consolidated Springfield Village + ICS shared-fleet pooling"}
        ],
        "notes": "SWLSTG's transport line reflects the realities of running specialist + general MH services across south-west London while delivering a £150M+ Springfield Village redevelopment. The new acute-MH wards (Trinity Building + Sir William Atkinson Wing 2024) consolidate inpatient capacity but do not eliminate inter-site movement to Tolworth Hospital and the Phoenix Wing. London-wide ULEZ enforcement adds compliance cost for older trust-fleet vehicles; the salary-sacrifice EV scheme and London Ambulance Service-contracted PTS for s.136 conveyance are the principal levers. The trust serves national specialist eating-disorders and perinatal-MH catchments which generate inter-region transfer-team mileage on top of borough-level community visits.",
        "sources": [
            {"publisher": "South West London and St George's Mental Health NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.swlstg.nhs.uk/about-us/publications"},
            {"publisher": "Care Quality Commission", "title": "SWLSTG provider profile (RQY)", "url": "https://www.cqc.org.uk/provider/RQY"},
            {"publisher": "South West London Integrated Care Board", "title": "Estate and travel review 2024", "url": "https://www.southwestlondon.icb.nhs.uk/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Greater London Authority", "title": "Ultra Low Emission Zone (ULEZ) policy", "url": "https://tfl.gov.uk/modes/driving/ultra-low-emission-zone"}
        ],
        "related": ["South West London and St George's Mental Health NHS Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Department of Health and Social Care", "Transport (business + patient) — Greater Manchester Mental Health NHS Foundation Trust", "Mental Health Act 1983"]
    },
    "Establishment costs — South West London and St George's Mental Health NHS Trust": {
        "aliases": [{"name": "Establishment costs", "parent": "South West London and St George's Mental Health NHS Trust"}],
        "description": "SWLSTG's £1.22M establishment line covers stationery, postage, telephony, mobile devices, printing and courier across Springfield University Hospital (Tooting), Tolworth Hospital, Phoenix Wing and community-MH bases in Wandsworth, Merton, Sutton, Kingston and Richmond. The Springfield Village redevelopment (2018-2024) reset office and clinical-administration space; mobile-working investment for community-MH and crisis teams sustains a higher device + connectivity spend than legacy paper-based workflows.",
        "beneficiaries": "c. 2,700 staff supporting c. 1.1M residents across 5 SW London boroughs; combined acute-MH + community-MH + national specialist eating-disorders + perinatal-MH service across Springfield, Tolworth, Phoenix Wing + c. 40 community bases.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses disclosure) · IAS 1 Presentation of Financial Statements · NHS Act 2006 · Health and Care Act 2022 · Public Contracts Regulations 2015",
        "key_stats": [
            {"label": "Establishment costs 2024-25", "value": "£1.22M"},
            {"label": "Site footprint", "value": "Springfield University Hospital + Tolworth Hospital + Phoenix Wing + c. 40 community-MH bases"},
            {"label": "Headcount served", "value": "c. 2,700 substantive WTE"},
            {"label": "Composition", "value": "Stationery + printing + postage + courier + telephony + mobile-device estate + photocopying + minor office consumables"},
            {"label": "Springfield Village reset", "value": "2018-2024 redevelopment reset office + clinical-administration space; modernised IT infrastructure reduces legacy print volumes"},
            {"label": "Mobile-device estate", "value": "Smartphone + laptop rollout for community-MH + crisis teams; supports remote working"},
            {"label": "Procurement route", "value": "NHS Supply Chain framework + Crown Commercial Service telephony framework"},
            {"label": "Funding trajectory", "value": "2020-21 c. £0.9M → 2024-25 £1.22M — uplift tracking community-mobile-working + CPI + post-redevelopment occupancy"},
            {"label": "Delivery body", "value": "Trust Finance + Procurement + Digital Services teams"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + South West London ICB"},
            {"label": "Evaluation evidence", "value": "Trust ARA 2023-24 disclosure; NHSE Model Hospital benchmarking; Springfield Village post-occupancy evaluation"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-redevelopment paper-heavy workflow on Victorian Springfield estate · Successor: digitised workflows under Frontline Digitisation EPR rollout"}
        ],
        "notes": "SWLSTG's establishment line reflects the operational running cost of an MH trust managing a major redevelopment — the £150M+ Springfield Village programme has reset both the physical estate and the clinical-administration workflow, with new wards (Trinity Building + Sir William Atkinson Wing 2024) commissioned with modernised IT infrastructure reducing legacy print volume. Community-MH and crisis-team mobile-working drives the device + connectivity component upward; the trust's national specialist eating-disorders and perinatal-MH services add cross-region postage and courier cost. Frontline Digitisation EPR completion will compress printing further but raise software-licensing recurring cost.",
        "sources": [
            {"publisher": "South West London and St George's Mental Health NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.swlstg.nhs.uk/about-us/publications"},
            {"publisher": "NHS England", "title": "Model Hospital — community + mental health benchmarking", "url": "https://www.england.nhs.uk/applications/model-hospital/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "SWLSTG provider profile (RQY)", "url": "https://www.cqc.org.uk/provider/RQY"},
            {"publisher": "NHS Supply Chain", "title": "Office consumables and stationery framework", "url": "https://www.supplychain.nhs.uk/"}
        ],
        "related": ["South West London and St George's Mental Health NHS Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Department of Health and Social Care", "Establishment costs — Camden and Islington NHS Foundation Trust", "Frontline Digitisation programme"]
    },
    "Business rates — Pennine Care NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "Pennine Care NHS Foundation Trust"}],
        "description": "Pennine Care's £1.22M 2024-25 business-rates charge reflects VOA-set rateable values × 49.9p / 54.6p UBR across the trust's hereditaments in Bury, Oldham, Rochdale, Stockport, Tameside and Glossop. Site footprint covers the Meadowbrook Unit (Salford), Tameside General-co-located MH wards, Stepping Hill MH wards (Stockport) and dispersed community-MH + CAMHS clinics. Greater Manchester rateable values sit below central-London peers but the multi-borough hereditament count drives a sustained line.",
        "beneficiaries": "c. 70 occupied hereditaments across 5 Greater Manchester boroughs + High Peak; serves c. 1.3M registered population; c. 3,500 staff providing community-MH, CAMHS, addictions and inpatient services.",
        "legal_basis": "Local Government Finance Act 1988 (Schedule 6 valuation) · Non-Domestic Rating (Multipliers and Private Finance) Act 2024 · Non-Domestic Rating Act 2023 · NHS Act 2006 · Health and Care Act 2022 · DHSC GAM 2024-25",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£1.22M"},
            {"label": "Hereditament count", "value": "c. 70 occupied sites across Bury, Oldham, Rochdale, Stockport, Tameside + High Peak"},
            {"label": "Geographic spread", "value": "5 Greater Manchester boroughs + Derbyshire High Peak (Glossop)"},
            {"label": "Site footprint", "value": "Meadowbrook (Salford) + Tameside General MH wards + Stepping Hill MH wards + dispersed community + CAMHS clinics"},
            {"label": "UBR 2024-25", "value": "49.9p small-multiplier / 54.6p standard-multiplier — frozen at 2023-24 levels under Autumn Statement 2023"},
            {"label": "Charitable exemption", "value": "Not applicable — NHS FTs are not registered charities under Charities Act 2011"},
            {"label": "VOA 2023 revaluation impact", "value": "GM commercial RVs broadly stable post-pandemic; modest rebasing"},
            {"label": "NHSPS interaction", "value": "Significant share of community estate held via NHSPS lease; rates passed through to trust as occupier"},
            {"label": "Funding trajectory", "value": "2020-21 c. £0.95M → 2024-25 £1.22M — tracks frozen UBR + community-clinic additions"},
            {"label": "Delivery body", "value": "Trust Estates + VOA + 6 billing authorities (Bury, Oldham, Rochdale, Stockport, Tameside, High Peak)"},
            {"label": "Policy owner", "value": "DHSC + MHCLG (business rates) + NHSE Provider Finance + Greater Manchester ICB + Derby & Derbyshire ICB"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2017 antecedent valuation date list · Successor: 2026 next revaluation under NDRA 2023 3-year cycle"}
        ],
        "notes": "Pennine Care's business-rates line is structurally driven by the multi-borough hereditament count rather than premium RV per site — Greater Manchester commercial RVs sit modestly below central-London peers but the trust occupies hereditaments across 6 different billing authorities, generating administrative complexity and 6 separate liability streams. The trust also uniquely covers Derbyshire High Peak (Glossop), which sits in a different ICB and billing-authority regime. NHSPS-leased community clinics pass rates through to Pennine Care as occupier, complicating service-charge boundaries. The 2026 VOA revaluation under the NDRA 2023 3-year cycle is the next reset; UBR remains frozen at 49.9p / 54.6p through 2024-25 under Autumn Statement 2023.",
        "sources": [
            {"publisher": "Pennine Care NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.penninecare.nhs.uk/about-us/publications"},
            {"publisher": "Valuation Office Agency", "title": "Find a business rates valuation (NHS hereditaments)", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "Department for Levelling Up, Housing and Communities", "title": "Business rates — multipliers and reliefs 2024-25", "url": "https://www.gov.uk/introduction-to-business-rates"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS Property Services", "title": "Service charge and rates pass-through methodology", "url": "https://www.property.nhs.uk/"}
        ],
        "related": ["Pennine Care NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Department of Health and Social Care", "Business rates — Central and North West London NHS Foundation Trust", "Valuation Office Agency"]
    },
    "Business rates — Camden and Islington NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "Camden and Islington NHS Foundation Trust"}],
        "description": "Camden and Islington's £1.22M 2024-25 business-rates charge sits high relative to the trust's modest size because of the central-London hereditament concentration — Highgate Mental Health Centre (St Pancras), the Peckwater Centre, the Lowther Road site and dispersed community-MH bases all carry inner-London RV per m² premiums. The trust is also part of the proposed C&I + Barnet, Enfield and Haringey merger to form a new North London Mental Health Partnership (effective 2024), which will not by itself reduce rates.",
        "beneficiaries": "c. 25 occupied hereditaments across Camden + Islington; serves c. 480,000 residents; c. 2,200 staff providing acute, community-MH, CAMHS, eating disorders and rehabilitation services.",
        "legal_basis": "Local Government Finance Act 1988 (Schedule 6 valuation) · Non-Domestic Rating (Multipliers and Private Finance) Act 2024 · Non-Domestic Rating Act 2023 · NHS Act 2006 · Health and Care Act 2022 · DHSC GAM 2024-25",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£1.22M"},
            {"label": "Hereditament profile", "value": "Highgate Mental Health Centre + Peckwater Centre + Lowther Road + dispersed community-MH bases"},
            {"label": "Billing authorities", "value": "London Borough of Camden + London Borough of Islington"},
            {"label": "UBR 2024-25", "value": "49.9p small-multiplier / 54.6p standard-multiplier — frozen at 2023-24 levels under Autumn Statement 2023"},
            {"label": "London RV premium", "value": "Camden + Islington commercial RVs carry 2-3× national-average RV per m²"},
            {"label": "Charitable exemption", "value": "Not applicable — NHS FTs are not registered charities under Charities Act 2011"},
            {"label": "VOA 2023 revaluation impact", "value": "Inner London commercial RVs partially rebased downward post-pandemic"},
            {"label": "North London MH Partnership context", "value": "Group-arrangement merger with Barnet, Enfield and Haringey MH Trust effective 2024 — does not by itself reduce hereditament rates"},
            {"label": "Funding trajectory", "value": "2020-21 c. £0.9M → 2024-25 £1.22M — tracks frozen UBR + Highgate redevelopment"},
            {"label": "Delivery body", "value": "Trust Estates + VOA + LB Camden + LB Islington (billing)"},
            {"label": "Policy owner", "value": "DHSC + MHCLG (business rates) + NHSE Provider Finance + North Central London ICB"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2017 antecedent valuation date list · Successor: 2026 next revaluation; potential consolidation under NLMHP"}
        ],
        "notes": "Camden and Islington's business-rates line is structurally elevated by central-London hereditament RV per m², not by site count — the trust occupies relatively few hereditaments but each one sits in inner-London commercial-rate territory. The 2024 group arrangement with Barnet, Enfield and Haringey MH Trust to form the North London Mental Health Partnership creates governance consolidation but does not by itself trigger any hereditament merger — rates remain payable on each occupied hereditament at full UBR. The Highgate Mental Health Centre redevelopment is a medium-term restructure that may consolidate footprint. The 2026 VOA revaluation under the NDRA 2023 3-year cycle is the next reset.",
        "sources": [
            {"publisher": "Camden and Islington NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.candi.nhs.uk/about-us/publications"},
            {"publisher": "Valuation Office Agency", "title": "Find a business rates valuation (Camden + Islington NHS hereditaments)", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "Department for Levelling Up, Housing and Communities", "title": "Business rates — multipliers and reliefs 2024-25", "url": "https://www.gov.uk/introduction-to-business-rates"},
            {"publisher": "North Central London Integrated Care Board", "title": "North London Mental Health Partnership group arrangement", "url": "https://nclhealthandcare.org.uk/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"}
        ],
        "related": ["Camden and Islington NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Department of Health and Social Care", "Business rates — Central and North West London NHS Foundation Trust", "Valuation Office Agency"]
    },
    "PFI / LIFT charges — Pennine Care NHS Foundation Trust": {
        "aliases": [{"name": "PFI / LIFT charges", "parent": "Pennine Care NHS Foundation Trust"}],
        "description": "Pennine Care's £1.20M PFI / LIFT charge represents the unitary-payment element on Community Health Partnerships LIFT-vehicle premises and any residual PFI-financed estate within the trust's Greater Manchester footprint. Most NHS LIFT vehicles in GM cover community-MH and primary-care space jointly; the unitary payment splits availability + service-charge components. IFRIC 12 service-concession accounting governs the recognition.",
        "beneficiaries": "Community-MH, CAMHS, addictions and primary-care-co-located teams across Bury, Oldham, Rochdale, Stockport, Tameside and High Peak; serves c. 1.3M registered population through c. 70 hereditaments including LIFT-financed clinics.",
        "legal_basis": "IFRIC 12 Service Concession Arrangements · DHSC Group Accounting Manual 2024-25 ch.6 · NHS (Private Finance) Act 1997 · NHS Act 2006 · Health and Care Act 2022 · LIFT model (DHSC programme 2001)",
        "key_stats": [
            {"label": "PFI / LIFT charges 2024-25", "value": "£1.20M"},
            {"label": "LIFT vehicle counterparties", "value": "Community Health Partnerships LIFT companies operating in GM (multiple SPVs by district)"},
            {"label": "Geographic spread", "value": "Bury, Oldham, Rochdale, Stockport, Tameside + High Peak"},
            {"label": "Composition", "value": "Availability payment + service-charge element + lifecycle-replacement contribution"},
            {"label": "IFRIC 12 treatment", "value": "On-balance-sheet service concession — finance-lease-like recognition + interest + service expense split per DHSC GAM ch.6"},
            {"label": "Original LIFT signing", "value": "GM LIFT companies signed 2003-2007 under DHSC LIFT programme; contracts run 25-30 years"},
            {"label": "Funding trajectory", "value": "Stable c. £1.0-1.3M annual run-rate — RPI/CPI uplifts within unitary-payment formula"},
            {"label": "Delivery body", "value": "Trust Estates + Community Health Partnerships + LIFT SPV partners"},
            {"label": "Policy owner", "value": "DHSC + Community Health Partnerships + NHSE Provider Finance + Greater Manchester ICB"},
            {"label": "NAO scrutiny", "value": "NAO LIFT review series — fixed unitary payments + lifecycle uplifts limit value-for-money flexibility"},
            {"label": "Evaluation evidence", "value": "Trust ARA 2023-24 PFI/LIFT note; CHP annual review; NAO LIFT/PFI scrutiny"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2003 capital-funded NHS estate · Successor: contract expiry 2028-2032 — handback + asset-condition negotiations"}
        ],
        "notes": "Pennine Care's LIFT exposure is typical of GM MH/community trusts — community clinics in the LIFT estate are shared with primary-care occupancy, with the trust paying its share of the unitary payment for available consultation space. IFRIC 12 service-concession accounting requires on-balance-sheet recognition under DHSC GAM ch.6, splitting the unitary payment into finance-charge interest, service expense and lifecycle-replacement contribution. The first wave of LIFT contracts (signed 2003-2007) reach handback in 2028-2032, and the asset-condition negotiations under the LIFT exit framework are the principal medium-term risk. NAO has flagged limited value-for-money flexibility within the fixed unitary-payment formula.",
        "sources": [
            {"publisher": "Pennine Care NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.penninecare.nhs.uk/about-us/publications"},
            {"publisher": "Community Health Partnerships", "title": "LIFT estate annual review", "url": "https://www.communityhealthpartnerships.co.uk/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 6 — Service concessions)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "National Audit Office", "title": "PFI and PF2 / LIFT review series", "url": "https://www.nao.org.uk/reports/pfi-and-pf2/"},
            {"publisher": "HM Treasury", "title": "Standardisation of PFI Contracts (SoPC) and LIFT framework", "url": "https://www.gov.uk/government/publications/standardisation-of-pf2-contracts"}
        ],
        "related": ["Pennine Care NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Community Health Partnerships", "PFI / LIFT charges — Cornwall Partnership NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Amortisation — Oxleas NHS Foundation Trust": {
        "aliases": [{"name": "Amortisation", "parent": "Oxleas NHS Foundation Trust"}],
        "description": "Oxleas's £1.20M 2024-25 amortisation charge is IAS 38 depreciation of the trust's intangible-asset base — capitalised electronic patient record software (Rio EPR), e-prescribing, integration with the South East London shared-care record, capitalised training and bespoke development under the Frontline Digitisation programme. Oxleas's combined MH + community + LD remit across Bexley, Bromley and Greenwich plus prison-MH services at HMP Belmarsh + HMP Isis drive a complex multi-system intangible-asset portfolio.",
        "beneficiaries": "c. 4,400 staff using the Rio EPR + integrated systems across c. 100 sites; serves c. 950,000 residents in 3 SE London boroughs plus prison-MH catchments at HMP Belmarsh and HMP Isis (Thamesmead).",
        "legal_basis": "IAS 38 Intangible Assets · DHSC Group Accounting Manual 2024-25 ch.5 · NHS Act 2006 · Health and Care Act 2022 · Data Protection Act 2018",
        "key_stats": [
            {"label": "Amortisation 2024-25", "value": "£1.20M"},
            {"label": "Useful-economic-life policy", "value": "5-7 years software per DHSC GAM 2024-25 ch.5"},
            {"label": "Primary intangible asset", "value": "Rio EPR (Access Group) — Oxleas instance with Frontline Digitisation enhancements"},
            {"label": "Frontline Digitisation status", "value": "Wave-1 / wave-2 beneficiary — sustained software capitalisation 2022-2024"},
            {"label": "Site footprint covered", "value": "Oxleas House (Bexley) + Memorial Hospital + Goldie Leigh + community-MH + LD bases + prison-MH services"},
            {"label": "Composition", "value": "EPR software + e-prescribing + SE London shared-care-record integration + capitalised training + prison-MH SystmOne integration"},
            {"label": "Prison-MH integration", "value": "HMP Belmarsh + HMP Isis MH services use SystmOne (TPP) — additional integration layer capitalised"},
            {"label": "Funding trajectory", "value": "2020-21 c. £0.5M → 2024-25 £1.20M — step-up tracking Frontline Digitisation capitalisation cycle"},
            {"label": "Delivery body", "value": "Trust Digital + Finance teams; vendor Access Group (Rio) + TPP (SystmOne for prisons); programme oversight via NHSE Frontline Digitisation"},
            {"label": "Policy owner", "value": "DHSC + NHSE Transformation Directorate · South East London ICB · Frontline Digitisation programme + NHSE Health & Justice"},
            {"label": "Evaluation evidence", "value": "NHSE Frontline Digitisation programme reporting; trust ARA 2023-24 intangible-asset note; CQC inspection findings on digital maturity"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2017 paper-heavy clinical record · Successor: full digital-maturity-level-5 EPR + prison-MH integrated record by 2026-27"}
        ],
        "notes": "Oxleas's amortisation line stepped up in line with Frontline Digitisation capitalisation in 2022-24 — capitalised EPR software, integration work and training feed a 5-7 year amortisation tail per IAS 38. The trust runs a particularly complex digital estate because of the prison-MH services at HMP Belmarsh and HMP Isis, which use SystmOne (TPP) under the prison-healthcare digital framework rather than the trust's mainstream Rio EPR — additional integration layers and capitalised bespoke development feed both amortisation and operating cost. The South East London shared-care-record integration is the next capitalisation wave, with completion planned mid-2020s. Recurring amortisation will plateau c. 2026-27.",
        "sources": [
            {"publisher": "Oxleas NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.oxleas.nhs.uk/about-us/publications/"},
            {"publisher": "NHS England", "title": "Frontline Digitisation programme", "url": "https://www.england.nhs.uk/digitaltechnology/frontline-digitisation/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 5 — Intangible assets)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England Health and Justice Commissioning", "title": "Health and Justice digital strategy", "url": "https://www.england.nhs.uk/commissioning/health-just/"},
            {"publisher": "South East London Integrated Care Board", "title": "Digital and shared-care-record strategy", "url": "https://www.selondonics.org/"}
        ],
        "related": ["Oxleas NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Department of Health and Social Care", "Amortisation — Mersey Care NHS Foundation Trust", "Frontline Digitisation programme"]
    },
    "PFI / LIFT charges — Southern Health NHS Foundation Trust": {
        "aliases": [{"name": "PFI / LIFT charges", "parent": "Southern Health NHS Foundation Trust"}],
        "description": "Southern Health's £1.19M PFI / LIFT charge represents the unitary-payment element on Hampshire LIFT-vehicle premises (Hampshire Hospitals + community LIFT companies) and any residual PFI-financed estate. Community-MH and learning-disability clinics across Hampshire and Isle of Wight occupy LIFT-financed buildings jointly with primary-care occupiers; IFRIC 12 service-concession accounting governs recognition under DHSC GAM 2024-25 ch.6.",
        "beneficiaries": "Community-MH, CAMHS, learning-disability and addictions services across Hampshire + Isle of Wight; serves c. 1.4M registered population through c. 90 hereditaments including LIFT-financed clinics in Basingstoke, Andover, Eastleigh and Portsmouth area.",
        "legal_basis": "IFRIC 12 Service Concession Arrangements · DHSC Group Accounting Manual 2024-25 ch.6 · NHS (Private Finance) Act 1997 · NHS Act 2006 · Health and Care Act 2022 · LIFT model (DHSC programme 2001)",
        "key_stats": [
            {"label": "PFI / LIFT charges 2024-25", "value": "£1.19M"},
            {"label": "LIFT vehicle counterparties", "value": "Hampshire LIFT companies (Community Health Partnerships + private equity partners)"},
            {"label": "Geographic spread", "value": "Hampshire + Isle of Wight"},
            {"label": "Composition", "value": "Availability payment + service-charge element + lifecycle-replacement contribution"},
            {"label": "IFRIC 12 treatment", "value": "On-balance-sheet service concession — finance-lease-like recognition + interest + service expense split per DHSC GAM ch.6"},
            {"label": "Original LIFT signing", "value": "Hampshire LIFT companies signed 2003-2008 under DHSC LIFT programme; contracts run 25-30 years"},
            {"label": "Connor Sparrowhawk context", "value": "Trust's 2013 Mazars-investigated unexpected-deaths history (Connor Sparrowhawk inquest 2015) frames sustained estate-and-safety scrutiny — separate from PFI line but contextual to remediation programme"},
            {"label": "Funding trajectory", "value": "Stable c. £1.0-1.2M annual run-rate — RPI/CPI uplifts within unitary-payment formula"},
            {"label": "Delivery body", "value": "Trust Estates + Community Health Partnerships + LIFT SPV partners"},
            {"label": "Policy owner", "value": "DHSC + Community Health Partnerships + NHSE Provider Finance + Hampshire and Isle of Wight ICB"},
            {"label": "NAO scrutiny", "value": "NAO LIFT review series — fixed unitary payments + lifecycle uplifts limit value-for-money flexibility"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2003 capital-funded NHS estate · Successor: contract expiry 2028-2033 — handback + asset-condition negotiations"}
        ],
        "notes": "Southern Health's LIFT exposure spans Hampshire and the Isle of Wight, with community clinics shared with primary-care occupancy under joint-occupancy unitary-payment models. IFRIC 12 service-concession accounting splits the unitary payment into finance-charge interest, service expense and lifecycle-replacement contribution. The trust's wider context is shaped by the Mazars 2015 unexpected-deaths review (Connor Sparrowhawk inquest 2015 + Mazars report Dec 2015) which led to sustained CQC and DHSC scrutiny on estate and safety — the LIFT line itself is unaffected, but estate-related remediation has reshaped occupancy patterns. The first wave of LIFT contracts reach handback in 2028-2033.",
        "sources": [
            {"publisher": "Southern Health NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.southernhealth.nhs.uk/about-us/who-we-are/publications/annual-reports"},
            {"publisher": "Community Health Partnerships", "title": "LIFT estate annual review", "url": "https://www.communityhealthpartnerships.co.uk/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 6 — Service concessions)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "National Audit Office", "title": "PFI and PF2 / LIFT review series", "url": "https://www.nao.org.uk/reports/pfi-and-pf2/"},
            {"publisher": "Mazars LLP / NHS England", "title": "Mazars review of Southern Health unexpected deaths (2015)", "url": "https://www.england.nhs.uk/south/wp-content/uploads/sites/6/2015/12/mazars-rep.pdf"}
        ],
        "related": ["Southern Health NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Community Health Partnerships", "PFI / LIFT charges — Pennine Care NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Lease expenditure — Cumbria, Northumberland, Tyne and Wear NHS Foundation Trust": {
        "aliases": [{"name": "Lease expenditure", "parent": "Cumbria, Northumberland, Tyne and Wear NHS Foundation Trust"}],
        "description": "CNTW's £1.16M lease line reflects IFRS 16 right-of-use depreciation + interest on the trust's leased estate following the 2022 on-balance-sheet transition. The portfolio covers NHS Property Services and CHP LIFT-vehicle premises across Cumbria (north + west), Northumberland, Newcastle, Gateshead, North Tyneside, South Tyneside and Sunderland. Geographic spread across one of England's largest MH-trust catchments creates a high leased-site count; the NHSPS market-rent dispute affects the recurring-cost trajectory.",
        "beneficiaries": "c. 8,500 staff serving c. 1.7M registered population across Cumbria + NE England; c. 60+ NHSPS + CHP-LIFT leased sites including community-MH bases in Carlisle, Workington, Whitehaven, Hexham, Newcastle, Gateshead, Sunderland.",
        "legal_basis": "IFRS 16 Leases · DHSC Group Accounting Manual 2024-25 ch.7 · Landlord and Tenant Act 1954 · NHS Act 2006 · Health and Care Act 2022 · Property Services Act (NHSPS founding 2013)",
        "key_stats": [
            {"label": "Lease expenditure 2024-25", "value": "£1.16M"},
            {"label": "IFRS 16 transition jump", "value": "2022 on-balance-sheet adoption — operating leases reclassified to ROU asset + lease liability with corresponding depreciation + interest split"},
            {"label": "Leased site count", "value": "c. 60+ NHSPS + CHP-LIFT premises across Cumbria + NE England"},
            {"label": "Major lessor", "value": "NHS Property Services Ltd (majority) + Community Health Partnerships (LIFT) + private landlords"},
            {"label": "NHSPS rates dispute", "value": "Sustained NHSPS / MH-trust dispute on community-clinic market-rent uplift + service-charge methodology"},
            {"label": "Geographic spread", "value": "Cumbria (north + west) + Northumberland + 5 North East boroughs (Newcastle, Gateshead, North Tyneside, South Tyneside, Sunderland)"},
            {"label": "Discount rate applied", "value": "HM Treasury PES discount rate per DHSC GAM 2024-25 ch.7 — recalibrated annually"},
            {"label": "Lease term profile", "value": "Mix of 5-year + 10-year community clinic leases; longer-term LIFT contracts to 25+ years"},
            {"label": "Funding trajectory", "value": "2021-22 (pre-IFRS16) c. £0.6M operating lease → 2022-23 c. £1.0M ROU first year → 2024-25 £1.16M"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + NHSPS + CHP for LIFT vehicles"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + North East and North Cumbria ICB · IFRS 16 / DHSC GAM ch.7 oversight"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2022 IAS 17 operating-lease expense · Successor: NHSPS market-rent reform + ICS estate consolidation"}
        ],
        "notes": "CNTW operates one of England's largest MH-trust catchments by area, covering Cumbria and the North East — the geographic spread alone forces a high leased-site count, and the IFRS 16 2022 transition pushed previously off-balance-sheet operating leases on-balance-sheet. The NHSPS / mental-health-trust dispute over service-charge methodology and market-rent rebasing is particularly acute for trusts with high NHSPS-leased footprint such as CNTW. Cumbria's rural community-clinic base requires more dispersed leased premises than urban-concentrated peers. The North East and North Cumbria ICB estate consolidation programme is the medium-term lever; market-rent reform under NHSPS is the wild-card.",
        "sources": [
            {"publisher": "Cumbria, Northumberland, Tyne and Wear NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.cntw.nhs.uk/about/publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 7 — Leases)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS Property Services", "title": "Annual Report 2023-24 + market-rent methodology", "url": "https://www.property.nhs.uk/about/our-publications/"},
            {"publisher": "Community Health Partnerships", "title": "LIFT estate annual review", "url": "https://www.communityhealthpartnerships.co.uk/"},
            {"publisher": "North East and North Cumbria Integrated Care Board", "title": "Estate strategy and consolidation review", "url": "https://www.northeastnorthcumbria.nhs.uk/"}
        ],
        "related": ["Cumbria, Northumberland, Tyne and Wear NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "NHS Property Services Ltd", "Lease expenditure — Mersey Care NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Business rates — South West Yorkshire Partnership NHS Foundation Trust": {
        "aliases": [{"name": "Business rates", "parent": "South West Yorkshire Partnership NHS Foundation Trust"}],
        "description": "SWYPFT's £1.16M 2024-25 business-rates charge reflects VOA-set rateable values × 49.9p / 54.6p UBR across hereditaments in Barnsley, Calderdale, Kirklees and Wakefield. The trust occupies The Dales (Calderdale Royal Hospital), Fieldhead Hospital (Wakefield), Priestley Unit (Dewsbury), Newton Lodge medium-secure unit and dispersed community-MH + CAMHS clinics. South Yorkshire commercial RVs sit below central-London but the multi-borough hereditament count drives a sustained line.",
        "beneficiaries": "c. 50 occupied hereditaments across 4 West Yorkshire authorities + Barnsley; serves c. 1.1M registered population through community-MH, CAMHS, LD and forensic services; c. 4,500 staff.",
        "legal_basis": "Local Government Finance Act 1988 (Schedule 6 valuation) · Non-Domestic Rating (Multipliers and Private Finance) Act 2024 · Non-Domestic Rating Act 2023 · NHS Act 2006 · Health and Care Act 2022 · DHSC GAM 2024-25",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£1.16M"},
            {"label": "Hereditament count", "value": "c. 50 occupied sites across Barnsley + Calderdale + Kirklees + Wakefield"},
            {"label": "Geographic spread", "value": "4 West Yorkshire authorities + Barnsley (South Yorkshire)"},
            {"label": "Site footprint", "value": "The Dales (Calderdale Royal) + Fieldhead Hospital (Wakefield) + Priestley Unit (Dewsbury) + Newton Lodge medium-secure + dispersed community + CAMHS"},
            {"label": "UBR 2024-25", "value": "49.9p small-multiplier / 54.6p standard-multiplier — frozen at 2023-24 levels"},
            {"label": "Charitable exemption", "value": "Not applicable — NHS FTs are not registered charities under Charities Act 2011"},
            {"label": "VOA 2023 revaluation impact", "value": "West Yorkshire commercial RVs broadly stable post-pandemic"},
            {"label": "NHSPS interaction", "value": "Significant share of community estate held via NHSPS lease; rates passed through to trust as occupier"},
            {"label": "Funding trajectory", "value": "2020-21 c. £0.9M → 2024-25 £1.16M — tracks frozen UBR + community-clinic additions"},
            {"label": "Delivery body", "value": "Trust Estates + VOA + 5 billing authorities (Barnsley, Calderdale, Kirklees, Wakefield, Bradford-edge)"},
            {"label": "Policy owner", "value": "DHSC + MHCLG (business rates) + NHSE Provider Finance + West Yorkshire ICB + South Yorkshire ICB"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2017 antecedent valuation date list · Successor: 2026 next revaluation under NDRA 2023 3-year cycle"}
        ],
        "notes": "SWYPFT's business-rates line is driven by hereditament count rather than premium per-site RV — West Yorkshire commercial values sit modestly below central-London peers, but the trust occupies sites across 4 different billing authorities (plus Barnsley sitting under South Yorkshire ICB), generating administrative complexity. Newton Lodge medium-secure unit (Wakefield) and Fieldhead Hospital are the highest-value hereditaments; the dispersed community-MH + CAMHS + LD bases account for the bulk of the count. NHSPS-leased clinics pass rates through to SWYPFT under occupier-pays methodology. The 2026 VOA revaluation under the NDRA 2023 3-year cycle is the next reset point.",
        "sources": [
            {"publisher": "South West Yorkshire Partnership NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.southwestyorkshire.nhs.uk/about-us/publications/"},
            {"publisher": "Valuation Office Agency", "title": "Find a business rates valuation (NHS hereditaments)", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "Department for Levelling Up, Housing and Communities", "title": "Business rates — multipliers and reliefs 2024-25", "url": "https://www.gov.uk/introduction-to-business-rates"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS Property Services", "title": "Service charge and rates pass-through methodology", "url": "https://www.property.nhs.uk/"}
        ],
        "related": ["South West Yorkshire Partnership NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Department of Health and Social Care", "Business rates — Tees, Esk and Wear Valleys NHS Foundation Trust", "Valuation Office Agency"]
    },
    "Transport (business + patient) — North Staffordshire Combined Healthcare NHS Trust": {
        "aliases": [{"name": "Transport (business + patient)", "parent": "North Staffordshire Combined Healthcare NHS Trust"}],
        "description": "NSCHT's £1.14M transport line covers staff business mileage for community-MH, CAMHS, addictions, learning-disability and crisis teams across Stoke-on-Trent and North Staffordshire, plus inter-site transfers between the Harplands Hospital (Hartshill, Stoke), the Bennett Centre, Sutherland Centre and dispersed community-MH bases. The trust is one of England's smaller MH-specialist trusts but its mixed urban + rural North Staffordshire footprint generates sustained per-WTE community-team mileage.",
        "beneficiaries": "c. 1,800 staff serving c. 470,000 residents across Stoke-on-Trent + Newcastle-under-Lyme + Staffordshire Moorlands; c. 230 inpatient beds at Harplands + Bennett + Sutherland; community-MH + CAMHS + LD service across c. 25 community bases.",
        "legal_basis": "DHSC Group Accounting Manual 2024-25 (operating expenses) · IAS 1 Presentation of Financial Statements · NHS Act 2006 · Mental Health Act 1983 (s.135/136 conveyance) · Health and Care Act 2022 · HMRC Approved Mileage Allowance Payments",
        "key_stats": [
            {"label": "Transport (business + patient) 2024-25", "value": "£1.14M"},
            {"label": "Catchment area", "value": "Stoke-on-Trent + Newcastle-under-Lyme + Staffordshire Moorlands — c. 470,000 residents"},
            {"label": "Site footprint", "value": "Harplands Hospital (Hartshill, Stoke) + Bennett Centre + Sutherland Centre + c. 25 community bases"},
            {"label": "Mixed urban + rural driver", "value": "Stoke-on-Trent urban + rural Staffordshire Moorlands generates higher per-WTE community mileage than urban-only trusts"},
            {"label": "MHA conveyance share", "value": "s.136 / s.135 conveyance contracted via West Midlands Ambulance Service + private secure-transport providers"},
            {"label": "Staff mileage rate", "value": "NHS Agenda for Change Section 17 / HMRC AMAP 45p first 10,000 miles, 25p thereafter"},
            {"label": "Pool car + lease-vehicle fleet", "value": "Crown Commercial Service vehicle framework — gradual EV transition; salary-sacrifice scheme for staff personal-fleet"},
            {"label": "Funding trajectory", "value": "2020-21 c. £0.85M → 2024-25 £1.14M — uplift driven by post-pandemic in-person assessment recovery + fuel CPI"},
            {"label": "Delivery body", "value": "Trust Estates + Travel team; PTS contracted with WMAS + accredited secure-transport providers"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + Staffordshire and Stoke-on-Trent ICB"},
            {"label": "Evaluation evidence", "value": "CQC inspection reports (RRE); Staffordshire ICS estate + travel review; ICS shared-fleet pooling discussions"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2017 dispersed-fleet baseline · Successor: ICS shared-fleet pooling + EV transition under Staffordshire ICB"}
        ],
        "notes": "NSCHT's transport line reflects the running cost of an MH-specialist trust covering a mixed urban + rural Staffordshire footprint — Stoke-on-Trent urban density is offset by rural Staffordshire Moorlands community-team travel. Per-WTE mileage runs higher than urban-only peers because of the rural component. WMAS handles s.136 conveyance under the Staffordshire all-age PTS contract; secure-transfer requirements between Harplands and the regional medium-secure forensic estate (St Andrew's Northampton, Reaside Birmingham) generate cross-region inter-site movement. The Staffordshire and Stoke-on-Trent ICS shared-fleet pooling is the medium-term lever; EV transition will raise capital cost upfront before yielding mileage savings.",
        "sources": [
            {"publisher": "North Staffordshire Combined Healthcare NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.combined.nhs.uk/about-us/publications/"},
            {"publisher": "Care Quality Commission", "title": "NSCHT provider profile (RRE)", "url": "https://www.cqc.org.uk/provider/RRE"},
            {"publisher": "Staffordshire and Stoke-on-Trent Integrated Care Board", "title": "ICS estate and travel review", "url": "https://www.staffsstoke.icb.nhs.uk/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "West Midlands Ambulance Service University NHS Foundation Trust", "title": "PTS contract data", "url": "https://wmas.nhs.uk/"}
        ],
        "related": ["North Staffordshire Combined Healthcare NHS Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Department of Health and Social Care", "Transport (business + patient) — Coventry and Warwickshire Partnership NHS Trust", "Mental Health Act 1983"]
    },
    "Business rates — Avon and Wiltshire Mental Health Partnership NHS Trust": {
        "aliases": [{"name": "Business rates", "parent": "Avon and Wiltshire Mental Health Partnership NHS Trust"}],
        "description": "AWP's £1.13M 2024-25 business-rates charge reflects VOA-set rateable values × 49.9p / 54.6p UBR across hereditaments in Bristol, North Somerset, South Gloucestershire, Bath and North East Somerset, Swindon and Wiltshire. Site footprint covers Callington Road Hospital (Bristol), Southmead Hospital MH wards, Fountain Way (Salisbury), Sandalwood Court (Swindon) and dispersed community-MH bases. The 6-authority spread drives a sustained line; Bristol commercial RVs sit modestly above non-London average.",
        "beneficiaries": "c. 90 occupied hereditaments across 6 unitary authorities in the SW; serves c. 1.8M registered population through community-MH, CAMHS, addictions, eating disorders and inpatient services; c. 4,800 staff.",
        "legal_basis": "Local Government Finance Act 1988 (Schedule 6 valuation) · Non-Domestic Rating (Multipliers and Private Finance) Act 2024 · Non-Domestic Rating Act 2023 · NHS Act 2006 · Health and Care Act 2022 · DHSC GAM 2024-25",
        "key_stats": [
            {"label": "Business rates 2024-25", "value": "£1.13M"},
            {"label": "Hereditament count", "value": "c. 90 occupied sites across 6 SW unitary authorities"},
            {"label": "Geographic spread", "value": "Bristol, North Somerset, South Gloucestershire, BANES, Swindon, Wiltshire"},
            {"label": "Site footprint", "value": "Callington Road Hospital (Bristol) + Southmead MH wards + Fountain Way (Salisbury) + Sandalwood Court (Swindon) + community bases"},
            {"label": "UBR 2024-25", "value": "49.9p small-multiplier / 54.6p standard-multiplier — frozen at 2023-24 levels under Autumn Statement 2023"},
            {"label": "Charitable exemption", "value": "Not applicable — NHS FTs are not registered charities under Charities Act 2011"},
            {"label": "VOA 2023 revaluation impact", "value": "Bristol commercial RVs modestly elevated; rural Wiltshire stable"},
            {"label": "NHSPS interaction", "value": "Significant share of community estate held via NHSPS lease; rates passed through to trust as occupier"},
            {"label": "Funding trajectory", "value": "2020-21 c. £0.9M → 2024-25 £1.13M — tracks frozen UBR + 6-authority hereditament additions"},
            {"label": "Delivery body", "value": "Trust Estates + VOA + 6 billing authorities (Bristol CC, North Somerset, South Glos, BANES, Swindon, Wiltshire)"},
            {"label": "Policy owner", "value": "DHSC + MHCLG (business rates) + NHSE Provider Finance + Bristol/N.Somerset/S.Glos ICB + BSW ICB"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2017 antecedent valuation date list · Successor: 2026 next revaluation under NDRA 2023 3-year cycle"}
        ],
        "notes": "AWP's business-rates line is driven by the unusually large 6-authority hereditament spread — covering both Avon (4 unitary authorities post-1996) and Wiltshire (Swindon + Wiltshire Council), the trust occupies hereditaments across an area straddling two ICBs. Bristol commercial RVs sit modestly above non-London average and rural Wiltshire RVs are lower; the blended rate-per-hereditament is mid-range. NHSPS-leased clinics pass rates through under occupier-pays methodology. The 2026 VOA revaluation under the NDRA 2023 3-year cycle is the next reset point. AWP's 2018-2024 CQC special-measures cycle has reshaped some site occupancy but the underlying hereditament base remains broadly stable.",
        "sources": [
            {"publisher": "Avon and Wiltshire Mental Health Partnership NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.awp.nhs.uk/about-us/publications"},
            {"publisher": "Valuation Office Agency", "title": "Find a business rates valuation (NHS hereditaments)", "url": "https://www.gov.uk/correct-your-business-rates"},
            {"publisher": "Department for Levelling Up, Housing and Communities", "title": "Business rates — multipliers and reliefs 2024-25", "url": "https://www.gov.uk/introduction-to-business-rates"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "AWP provider profile (RVN)", "url": "https://www.cqc.org.uk/provider/RVN"}
        ],
        "related": ["Avon and Wiltshire Mental Health Partnership NHS Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Department of Health and Social Care", "Business rates — Cornwall Partnership NHS Foundation Trust", "Valuation Office Agency"]
    },
    "Impairments net of reversals — Cornwall Partnership NHS Foundation Trust": {
        "aliases": [{"name": "Impairments net of reversals", "parent": "Cornwall Partnership NHS Foundation Trust"}],
        "description": "Cornwall Partnership's £1.13M 2024-25 impairments-net-of-reversals line reflects DHSC GAM ch.4 / IAS 36 / IAS 16 revaluation losses and downward modified-equivalent-asset (MEA) adjustments on the trust's MH and community estate following the annual desktop revaluation. Cornwall's coastal + rural estate carries higher impairment volatility than urban peers due to specialist building-cost-index movements and Modern Methods of Construction adjustments. The £1.13M is net — gross gross impairments may be partially offset by reversals on previously-impaired assets.",
        "beneficiaries": "Estate-wide accounting impact across Longreach House (Redruth), Bodmin Hospital MH wards, Trengweath (Redruth) and dispersed community-MH + community-physical-health sites serving c. 570,000 Cornish residents; affects depreciation base for c. 4,000 staff's clinical estate.",
        "legal_basis": "IAS 36 Impairment of Assets · IAS 16 Property, Plant and Equipment (revaluation model) · DHSC Group Accounting Manual 2024-25 ch.4 · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Impairments net of reversals 2024-25", "value": "£1.13M"},
            {"label": "Accounting basis", "value": "IAS 36 / IAS 16 revaluation losses recognised in operating expenses below the line under DHSC GAM ch.4"},
            {"label": "Revaluation cycle", "value": "Annual desktop revaluation by VOA / external valuer; full revaluation every 5 years"},
            {"label": "MEA basis", "value": "Modified-Equivalent-Asset valuation — adjustments for surplus accommodation + locational factors"},
            {"label": "Cornwall coastal / rural premium", "value": "Specialist building-cost-index movements + remote-site logistics drive higher impairment volatility"},
            {"label": "Site footprint", "value": "Longreach House + Bodmin Hospital MH + Trengweath (Redruth) + dispersed community-MH and community-physical-health bases"},
            {"label": "AME treatment", "value": "Impairments above the operating-cost ceiling fall in AME; below-ceiling sit in DEL"},
            {"label": "Funding trajectory", "value": "Volatile year-on-year — driven by valuation index movements rather than activity; 2023-24 c. £0.4M → 2024-25 £1.13M reflects modest write-down"},
            {"label": "Delivery body", "value": "Trust Finance + VOA / external valuer + Estates team"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + Cornwall and Isles of Scilly ICB · DHSC GAM ch.4 oversight"},
            {"label": "Evaluation evidence", "value": "Trust ARA 2023-24 PPE + impairments note; NAO consolidated NHS provider accounts"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-IFRS revaluation regime · Successor: ICS estate consolidation may rebase MEA assumptions"}
        ],
        "notes": "Cornwall Partnership's impairments line is volatile by nature — annual desktop revaluations under IAS 16 / IAS 36 generate accounting movements driven by building-cost indices, surplus-accommodation adjustments and locational factors rather than by clinical activity. The Cornish coastal + rural estate carries higher volatility than urban peers because specialist construction-cost indices and remote-site logistics adjustments amplify both upward and downward movements. The £1.13M 2024-25 figure is net — gross impairments may be partially offset by reversals on previously-impaired assets that have recovered value. The split between DEL and AME depends on whether impairments exceed the operating-cost ceiling under HMT consolidated budgeting guidance. ICS estate consolidation may rebase MEA assumptions in coming years.",
        "sources": [
            {"publisher": "Cornwall Partnership NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.cornwallft.nhs.uk/about-us/publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 4 — PPE + impairments)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Valuation Office Agency", "title": "VOA NHS estate valuation methodology", "url": "https://www.gov.uk/government/organisations/valuation-office-agency"},
            {"publisher": "National Audit Office", "title": "Consolidated NHS provider accounts review", "url": "https://www.nao.org.uk/reports/department-of-health-and-social-care-annual-report-and-accounts-2023-24/"},
            {"publisher": "HM Treasury", "title": "Consolidated budgeting guidance — DEL / AME treatment", "url": "https://www.gov.uk/government/publications/consolidated-budgeting-guidance"}
        ],
        "related": ["Cornwall Partnership NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Department of Health and Social Care", "Impairments net of reversals — Leeds and York Partnership NHS Foundation Trust", "Valuation Office Agency"]
    },
    "PFI / LIFT charges — Lancashire and South Cumbria NHS Foundation Trust": {
        "aliases": [{"name": "PFI / LIFT charges", "parent": "Lancashire and South Cumbria NHS Foundation Trust"}],
        "description": "LSCFT's £1.12M PFI / LIFT charge represents the unitary-payment element on Community Health Partnerships LIFT-vehicle premises across Lancashire and South Cumbria, including community-MH clinics co-located with primary-care space in Preston, Blackpool, Blackburn-with-Darwen, Burnley and Lancaster. IFRIC 12 service-concession accounting governs recognition under DHSC GAM 2024-25 ch.6, splitting the unitary payment into finance-charge interest, service expense and lifecycle-replacement contribution.",
        "beneficiaries": "Community-MH, CAMHS, addictions and learning-disability services across Lancashire + South Cumbria; serves c. 1.8M registered population through community-MH bases and inpatient sites including The Harbour (Blackpool), Avondale Unit (Preston), Royal Blackburn MH wards.",
        "legal_basis": "IFRIC 12 Service Concession Arrangements · DHSC Group Accounting Manual 2024-25 ch.6 · NHS (Private Finance) Act 1997 · NHS Act 2006 · Health and Care Act 2022 · LIFT model (DHSC programme 2001)",
        "key_stats": [
            {"label": "PFI / LIFT charges 2024-25", "value": "£1.12M"},
            {"label": "LIFT vehicle counterparties", "value": "Community Health Partnerships LIFT companies operating in Lancashire + South Cumbria"},
            {"label": "Geographic spread", "value": "Preston + Blackpool + Blackburn-with-Darwen + Burnley + Lancaster + South Cumbria"},
            {"label": "Composition", "value": "Availability payment + service-charge element + lifecycle-replacement contribution"},
            {"label": "IFRIC 12 treatment", "value": "On-balance-sheet service concession — finance-lease-like recognition + interest + service expense split per DHSC GAM ch.6"},
            {"label": "Original LIFT signing", "value": "Lancashire LIFT companies signed 2003-2008 under DHSC LIFT programme; contracts run 25-30 years"},
            {"label": "Edenfield-adjacent context", "value": "Trust runs Guild Lodge medium-secure unit (Whittingham) — separate from PFI line but contextual to NW MH safety scrutiny post-Edenfield 2022"},
            {"label": "Funding trajectory", "value": "Stable c. £1.0-1.2M annual run-rate — RPI/CPI uplifts within unitary-payment formula"},
            {"label": "Delivery body", "value": "Trust Estates + Community Health Partnerships + LIFT SPV partners"},
            {"label": "Policy owner", "value": "DHSC + Community Health Partnerships + NHSE Provider Finance + Lancashire and South Cumbria ICB"},
            {"label": "NAO scrutiny", "value": "NAO LIFT review series — fixed unitary payments + lifecycle uplifts limit value-for-money flexibility"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2003 capital-funded NHS estate · Successor: contract expiry 2028-2033 — handback + asset-condition negotiations"}
        ],
        "notes": "LSCFT's LIFT exposure spans Lancashire and South Cumbria, with community-MH clinics co-located with primary-care occupancy under joint-occupancy unitary-payment models. IFRIC 12 service-concession accounting splits the unitary payment into finance-charge interest, service expense and lifecycle-replacement contribution per DHSC GAM ch.6. The trust's wider NW context includes the Edenfield Panorama 2022 fallout (operated by neighbouring GMMH but with cross-trust safe-staffing implications) and sustained CQC scrutiny on Guild Lodge medium-secure unit at Whittingham — both contextual to the trust's wider remediation cost base, though the LIFT line itself is unaffected. The first wave of LIFT contracts reach handback in 2028-2033 under the LIFT exit framework.",
        "sources": [
            {"publisher": "Lancashire and South Cumbria NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.lscft.nhs.uk/about-us/publications"},
            {"publisher": "Community Health Partnerships", "title": "LIFT estate annual review", "url": "https://www.communityhealthpartnerships.co.uk/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 6 — Service concessions)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "National Audit Office", "title": "PFI and PF2 / LIFT review series", "url": "https://www.nao.org.uk/reports/pfi-and-pf2/"},
            {"publisher": "Care Quality Commission", "title": "LSCFT provider profile (RW5)", "url": "https://www.cqc.org.uk/provider/RW5"}
        ],
        "related": ["Lancashire and South Cumbria NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "Community Health Partnerships", "PFI / LIFT charges — Pennine Care NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Lease expenditure — Midlands Partnership NHS Foundation Trust": {
        "aliases": [{"name": "Lease expenditure", "parent": "Midlands Partnership NHS Foundation Trust"}],
        "description": "MPFT's £1.12M lease line reflects IFRS 16 right-of-use depreciation + interest on the trust's leased estate following the 2022 on-balance-sheet transition. The portfolio covers NHS Property Services and CHP LIFT-vehicle premises across Staffordshire, Stoke-on-Trent, Shropshire, Telford & Wrekin and parts of Worcestershire — one of England's largest combined MH + community-physical-health footprints. The NHSPS market-rent dispute is material given the high NHSPS-leased proportion of community sites.",
        "beneficiaries": "c. 9,000 staff serving c. 1.5M registered population across Staffordshire + Shropshire + parts of Worcestershire; c. 70+ NHSPS + CHP-LIFT leased sites including community-MH bases, district-nursing hubs, CAMHS clinics and learning-disability community sites.",
        "legal_basis": "IFRS 16 Leases · DHSC Group Accounting Manual 2024-25 ch.7 · Landlord and Tenant Act 1954 · NHS Act 2006 · Health and Care Act 2022 · Property Services Act (NHSPS founding 2013)",
        "key_stats": [
            {"label": "Lease expenditure 2024-25", "value": "£1.12M"},
            {"label": "IFRS 16 transition jump", "value": "2022 on-balance-sheet adoption — operating leases reclassified to ROU asset + lease liability with corresponding depreciation + interest split"},
            {"label": "Leased site count", "value": "c. 70+ NHSPS + CHP-LIFT premises across Staffs + Shropshire + Worcs-edge"},
            {"label": "Major lessor", "value": "NHS Property Services Ltd (majority) + Community Health Partnerships (LIFT) + private landlords"},
            {"label": "NHSPS rates dispute", "value": "Sustained NHSPS / MH-trust dispute on community-clinic market-rent uplift + service-charge methodology"},
            {"label": "Combined MH + community remit", "value": "MPFT runs MH + community-physical-health + LD across a large footprint — broader leased-base than MH-only peers"},
            {"label": "Discount rate applied", "value": "HM Treasury PES discount rate per DHSC GAM 2024-25 ch.7 — recalibrated annually"},
            {"label": "Lease term profile", "value": "Mix of 5-year + 10-year community clinic leases; longer-term LIFT contracts to 25+ years"},
            {"label": "Funding trajectory", "value": "2021-22 (pre-IFRS16) c. £0.6M operating lease → 2022-23 c. £0.95M ROU first year → 2024-25 £1.12M"},
            {"label": "Delivery body", "value": "Trust Estates & Facilities + NHSPS + CHP for LIFT vehicles"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance + Staffordshire and Stoke-on-Trent ICB + Shropshire, Telford & Wrekin ICB · IFRS 16 / DHSC GAM ch.7 oversight"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2022 IAS 17 operating-lease expense + 2018 South Staffordshire + Shropshire amalgamation · Successor: NHSPS market-rent reform + ICS estate consolidation"}
        ],
        "notes": "MPFT's lease line reflects the running cost of one of England's largest combined MH + community-physical-health trusts — the post-2018 amalgamation of South Staffordshire & Shropshire Healthcare with Staffordshire and Stoke-on-Trent Partnership Trust created a footprint spanning two ICBs and over 70 leased sites. The IFRS 16 2022 transition pushed previously off-balance-sheet operating leases on-balance-sheet, with corresponding depreciation + interest recognition. The NHSPS / mental-health-trust dispute over service-charge methodology and market-rent rebasing is particularly material here given the high NHSPS-leased proportion. Cross-ICB estate consolidation under Staffordshire and Stoke-on-Trent ICB and Shropshire, Telford & Wrekin ICB is the medium-term lever.",
        "sources": [
            {"publisher": "Midlands Partnership NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.mpft.nhs.uk/about-us/publications"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25 (chapter 7 — Leases)", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS Property Services", "title": "Annual Report 2023-24 + market-rent methodology", "url": "https://www.property.nhs.uk/about/our-publications/"},
            {"publisher": "Community Health Partnerships", "title": "LIFT estate annual review", "url": "https://www.communityhealthpartnerships.co.uk/"},
            {"publisher": "Care Quality Commission", "title": "MPFT provider profile (RRE)", "url": "https://www.cqc.org.uk/provider/RRE"}
        ],
        "related": ["Midlands Partnership NHS Foundation Trust", "Premises & Infrastructure", "NHS Mental Health Trusts", "NHS Property Services Ltd", "Lease expenditure — Cumbria, Northumberland, Tyne and Wear NHS Foundation Trust", "Department of Health and Social Care"]
    },
}
