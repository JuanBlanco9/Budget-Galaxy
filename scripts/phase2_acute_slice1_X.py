# -*- coding: utf-8 -*-
# Phase 2 NHS Acute orphan enrichment — slice 1_X (66 trust-specific entries)
# Hand-curated tailor-made depth-5 entries for NHS Acute Trust sub-lines.

NEW = {
    "Premises (other) — Guy's & St Thomas' NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Guy's & St Thomas' NHS Foundation Trust"}],
        "description": "Premises running costs across GSTT's central-London tertiary estate — St Thomas' (Westminster, the riverside acute and ED), Guy's Hospital (London Bridge, with the Guy's Cancer Centre tower), Evelina London Children's Hospital, Royal Brompton (Chelsea, cardiothoracic) and Harefield (Hillingdon, transplant), following the 2021 Royal Brompton & Harefield merger. Estate carries Grade-listed Florence Nightingale-era fabric at St Thomas' alongside modern Cancer Centre and Evelina.",
        "beneficiaries": "c. 2.6m patient contacts a year across south-east London and specialist-referral catchments — major trauma at St Thomas', specialist heart-and-lung at Royal Brompton/Harefield, paediatric tertiary at Evelina, Guy's Cancer.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15 · Listed Buildings and Conservation Areas Act 1990",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£173.83M"},
            {"label": "Share of trust total opex", "value": "c. 6%"},
            {"label": "Estate scale", "value": "5 hospital sites incl. St Thomas' + Guy's + Evelina + Royal Brompton + Harefield"},
            {"label": "Listed fabric", "value": "St Thomas' East/North Wings Grade II · Guy's House Grade I"},
            {"label": "Specialist tertiary", "value": "Cardiothoracic (Brompton/Harefield) · paediatric (Evelina) · cancer (Guy's)"},
            {"label": "Hard FM model", "value": "Mixed in-house + specialist sub-contracts; no headline acute PFI on St Thomas'"},
            {"label": "Net Zero", "value": "Guy's & St Thomas' Charity-supported decarbonisation · LED + heat-pump pilots"},
            {"label": "YoY change", "value": "c. +6-8% (energy reset + Brompton/Harefield consolidation)"},
            {"label": "Peer benchmark", "value": "Above teaching-trust median per m² (listed estate + specialist estate)"}
        ],
        "notes": "GSTT's premises cost is structurally elevated by the listed Florence Nightingale-era riverside estate at St Thomas' (Grade II East/North Wings facing Parliament) and by absorbing the Royal Brompton & Harefield specialist heart-and-lung estate after the 2021 merger. Compliance backlog at St Thomas' is material, and Cancer Centre + Evelina lifecycle works contribute. RM6011 energy reset and 5-7% hard-FM inflation drive the 2024-25 uplift.",
        "sources": [
            {"publisher": "Guy's & St Thomas' NHS Foundation Trust", "title": "Annual report and accounts 2024-25", "url": "https://www.guysandstthomas.nhs.uk/about-us/our-publications"},
            {"publisher": "NHS England", "title": "Provider financial accounts", "url": "https://www.england.nhs.uk/financial-accounts/"},
            {"publisher": "Guy's & St Thomas' Charity", "title": "Programmes and impact", "url": "https://www.gsttcharity.org.uk/"}
        ],
        "related": ["Guy's & St Thomas' NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Social security & levy — Manchester University NHS Foundation Trust": {
        "aliases": [{"name": "Social security & levy", "parent": "Manchester University NHS Foundation Trust"}],
        "description": "Employer secondary Class 1 National Insurance + Apprenticeship Levy on MFT's c. 28,000-strong workforce — England's largest acute trust by headcount, spanning Manchester Royal Infirmary, Saint Mary's Hospital, Royal Manchester Children's Hospital, Manchester Royal Eye Hospital, University Dental Hospital, Wythenshawe Hospital (cardiothoracic + transplant), Trafford General, Withington Community and North Manchester General (since the 2021 NMGH merger).",
        "beneficiaries": "c. 28,000 staff (medical, nursing, AHP, scientific, AfC bands 1-9 + VSM) — headcount-weighted on-cost reflecting Manchester pay tilt and 2024 Agenda for Change uplift.",
        "legal_basis": "Social Security Contributions and Benefits Act 1992 · Finance Act 2016 (Apprenticeship Levy) · NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Social security & levy 2024-25", "value": "£134.51M"},
            {"label": "Headcount", "value": "c. 28,000 (largest acute trust in England by FTE)"},
            {"label": "Employer NIC rate", "value": "13.8% on earnings >£9,100 (2024-25, Class 1 secondary)"},
            {"label": "Apprenticeship Levy", "value": "0.5% of paybill (>£3M threshold)"},
            {"label": "April 2025 step-up", "value": "Employer NIC rises to 15% with threshold cut to £5,000"},
            {"label": "Pay drivers 2024-25", "value": "AfC 5.5% · medical 6% (junior doctor settlement)"},
            {"label": "Backfill drag", "value": "2023-24 industrial action backfill at premium rates lifts NIable pay"},
            {"label": "Site count", "value": "9 hospital sites + community estate (Greater Manchester)"},
            {"label": "Group context", "value": "Lead provider in GM ICS · merged with North Manchester General 2021"}
        ],
        "notes": "MFT's social security & levy line scales mechanically with the largest acute paybill in England — c. 28,000 FTE across nine hospital sites — and was lifted in 2024-25 by the 5.5% AfC award and the junior-doctor settlement, both of which uplift NIable pay. The 2023-24 industrial-action backfill (premium-rate locums and bank shifts) is still working through. April 2025 employer NIC step-up to 15% with the £5,000 threshold compounds the cost base materially in 2025-26.",
        "sources": [
            {"publisher": "Manchester University NHS Foundation Trust", "title": "Annual report and accounts", "url": "https://mft.nhs.uk/the-trust/corporate-publications/"},
            {"publisher": "HMRC", "title": "Rates and thresholds for employers 2024 to 2025", "url": "https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2024-to-2025"},
            {"publisher": "NHS Employers", "title": "Pay and Conditions Circulars (AfC + medical)", "url": "https://www.nhsemployers.org/publications/pay-and-conditions-circulars"}
        ],
        "related": ["Manchester University NHS Foundation Trust", "Staff Costs"]
    },
    "Social security & levy — University Hospitals Birmingham NHS Foundation Trust": {
        "aliases": [{"name": "Social security & levy", "parent": "University Hospitals Birmingham NHS Foundation Trust"}],
        "description": "Employer NIC + Apprenticeship Levy on UHB's c. 22,000-strong workforce across Queen Elizabeth Hospital Birmingham (the major trauma centre and adult tertiary tower with on-site military Royal Centre for Defence Medicine), Heartlands, Good Hope (Sutton Coldfield) and Solihull — the post-2018 enlarged trust formed by the HEFT merger.",
        "beneficiaries": "c. 22,000 staff including military medical personnel via RCDM — headcount-weighted on-cost across QEHB tertiary specialists, Heartlands acute, Good Hope and Solihull elective.",
        "legal_basis": "Social Security Contributions and Benefits Act 1992 · Finance Act 2016 (Apprenticeship Levy) · NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Social security & levy 2024-25", "value": "£123.99M"},
            {"label": "Headcount", "value": "c. 22,000 (4-site post-HEFT-merger acute group)"},
            {"label": "Employer NIC rate", "value": "13.8% on earnings >£9,100 (2024-25)"},
            {"label": "Apprenticeship Levy", "value": "0.5% of paybill (>£3M threshold)"},
            {"label": "April 2025 step-up", "value": "Employer NIC 15% · threshold cut to £5,000"},
            {"label": "Tertiary tilt", "value": "QEHB major trauma + liver transplant + military RCDM lifts consultant FTE share"},
            {"label": "Pay drivers 2024-25", "value": "AfC 5.5% · medical 6% (junior doctor settlement)"},
            {"label": "Backfill drag", "value": "2022-24 culture review and IA backfill keep premium-rate spend elevated"},
            {"label": "Group context", "value": "Birmingham and Solihull ICS · CQC-regulated improvement journey post-2022 reviews"}
        ],
        "notes": "UHB's social-security line is shaped by a tertiary consultant tilt (major trauma, liver transplant, RCDM military medicine at QEHB) which raises the average NIable salary versus a typical district acute. The trust has been working through the post-Bewick/Mannion culture-review programme and elevated bank/agency backfill alongside 2024-25 pay awards. April 2025 employer NIC step-up adds materially to the run-rate.",
        "sources": [
            {"publisher": "University Hospitals Birmingham NHS Foundation Trust", "title": "Annual report and accounts", "url": "https://www.uhb.nhs.uk/annual-report.htm"},
            {"publisher": "HMRC", "title": "Rates and thresholds for employers 2024 to 2025", "url": "https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2024-to-2025"},
            {"publisher": "NHS England", "title": "Bewick / Mannion reviews of UHB", "url": "https://www.england.nhs.uk/midlands/our-work/uhb-reviews/"}
        ],
        "related": ["University Hospitals Birmingham NHS Foundation Trust", "Staff Costs"]
    },
    "Social security & levy — Imperial College Healthcare NHS Trust": {
        "aliases": [{"name": "Social security & levy", "parent": "Imperial College Healthcare NHS Trust"}],
        "description": "Employer NIC + Apprenticeship Levy on ICHT's c. 14,500-strong central-west-London workforce across St Mary's (Paddington, major trauma + acute; the priority NHP scheme), Charing Cross (Hammersmith), Hammersmith Hospital (cardiac + renal tertiary) and Queen Charlotte's & Chelsea (women's + neonatal) plus Western Eye — anchored by the AHSC partnership with Imperial College London.",
        "beneficiaries": "c. 14,500 staff with elevated London weighting — academic-clinical tilt via Imperial AHSC raises consultant + research-active senior FTE share.",
        "legal_basis": "Social Security Contributions and Benefits Act 1992 · Finance Act 2016 (Apprenticeship Levy) · NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Social security & levy 2024-25", "value": "£96.98M"},
            {"label": "Headcount", "value": "c. 14,500 (5-site central/west London AHSC trust)"},
            {"label": "Employer NIC rate", "value": "13.8% on earnings >£9,100 (2024-25)"},
            {"label": "Apprenticeship Levy", "value": "0.5% of paybill"},
            {"label": "April 2025 step-up", "value": "15% NIC · £5,000 threshold"},
            {"label": "London weighting", "value": "Inner London HCAS uplift on AfC — pushes NIable pay above national median"},
            {"label": "Pay drivers 2024-25", "value": "AfC 5.5% · medical 6%"},
            {"label": "NHP cohort", "value": "St Mary's confirmed in priority cohort (originally Cohort 1 NHP)"},
            {"label": "Group context", "value": "NW London ICS · AHSC with Imperial College London"}
        ],
        "notes": "ICHT's social-security cost reflects a high-pay academic-clinical workforce on Inner London weighting and a heavy major-trauma + tertiary case-mix at St Mary's, plus research-active senior staff via the Imperial AHSC. The 2023-24 industrial-action backfill at premium agency rates lifts NIable pay; 2024-25 pay awards compound. April 2025 NIC step-up adds c. 8-9% to employer on-costs in 2025-26.",
        "sources": [
            {"publisher": "Imperial College Healthcare NHS Trust", "title": "Annual report and accounts", "url": "https://www.imperial.nhs.uk/about-us/our-publications"},
            {"publisher": "HMRC", "title": "Rates and thresholds for employers 2024 to 2025", "url": "https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2024-to-2025"},
            {"publisher": "NHS England", "title": "New Hospital Programme — schemes", "url": "https://www.england.nhs.uk/new-hospital-programme/"}
        ],
        "related": ["Imperial College Healthcare NHS Trust", "Staff Costs"]
    },
    "Premises (other) — Barts Health NHS Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Barts Health NHS Trust"}],
        "description": "Premises running costs across Barts Health's east-London estate — The Royal London (Whitechapel, major trauma + air-ambulance HEMS pad, the c. £1bn 2010s PFI tower), St Bartholomew's (Smithfield; the historic 1123-founded Barts site and the trust's specialist cardiothoracic + cancer centre, partly listed), Whipps Cross (Leytonstone; an older RAAC/decanting pre-1900s estate awaiting NHP rebuild), Newham (Plaistow) and Mile End. England's largest acute trust by income.",
        "beneficiaries": "c. 2.5m people across north-east London plus tertiary cardiothoracic + cancer referrals — major trauma at Royal London, specialist cardiac at Barts, district at Whipps Cross + Newham.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15 · Listed Buildings and Conservation Areas Act 1990",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£95.00M"},
            {"label": "Estate scale", "value": "5 hospital sites incl. Royal London, Barts, Whipps Cross, Newham, Mile End"},
            {"label": "PFI carve-out", "value": "Royal London + Barts under the c. £1bn 2010s PFI (separate PFI line)"},
            {"label": "Whipps Cross RAAC", "value": "Confirmed RAAC mitigation programme · NHP rebuild scheme"},
            {"label": "Listed fabric", "value": "St Bartholomew's North Wing + Henry VIII Gate Grade I"},
            {"label": "Hard FM model", "value": "PFI hard-FM at RLH/Barts (Skanska/Engie) · in-house at Whipps Cross/Newham"},
            {"label": "NHP cohort", "value": "Whipps Cross — confirmed priority NHP scheme post-2025 reset"},
            {"label": "Net Zero", "value": "PSDS + Barts Charity-supported decarbonisation"},
            {"label": "YoY change", "value": "c. +6-8% (RAAC works + energy reset)"}
        ],
        "notes": "Barts Health's premises-other line carries the operating premises overhead outside the PFI envelope — dominated by Whipps Cross (an end-of-life Victorian estate with confirmed RAAC and active mitigation while the NHP rebuild progresses) and the listed Grade I fabric at St Bartholomew's. The 2023 NHP reset placed Whipps Cross in the priority cohort. RM6011 energy reset and 5-7% hard-FM inflation drive the 2024-25 uplift.",
        "sources": [
            {"publisher": "Barts Health NHS Trust", "title": "Annual report and accounts", "url": "https://www.bartshealth.nhs.uk/our-performance"},
            {"publisher": "NHS England", "title": "New Hospital Programme — Whipps Cross", "url": "https://www.england.nhs.uk/new-hospital-programme/"},
            {"publisher": "DHSC", "title": "RAAC in NHS estate", "url": "https://www.gov.uk/government/publications/raac-in-the-nhs-estate"}
        ],
        "related": ["Barts Health NHS Trust", "Premises & Infrastructure"]
    },
    "Impairments net of reversals — West Suffolk NHS Foundation Trust": {
        "aliases": [{"name": "Impairments net of reversals", "parent": "West Suffolk NHS Foundation Trust"}],
        "description": "Non-cash IFRS impairment charges on West Suffolk's estate — principally driven by the West Suffolk Hospital (Bury St Edmunds), one of England's most heavily RAAC-affected hospitals (built 1970s, almost entirely RAAC-plank construction) and a confirmed New Hospital Programme rebuild scheme. Impairments capture the gap between Modern Equivalent Asset valuation and depreciated replacement cost on RAAC-compromised buildings.",
        "beneficiaries": "Patients across west Suffolk (c. 280,000 catchment) — emergency, maternity and elective at WSH plus community and outpatient sites in Bury St Edmunds, Newmarket and Sudbury.",
        "legal_basis": "IAS 36 Impairment of Assets · IFRS / FReM (HM Treasury) · NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code",
        "key_stats": [
            {"label": "Impairments 2024-25", "value": "£89.64M"},
            {"label": "Driver", "value": "RAAC-compromised West Suffolk Hospital — MEA write-down to DRC"},
            {"label": "RAAC exposure", "value": "Confirmed widespread RAAC plank construction · multi-year mitigation"},
            {"label": "NHP cohort", "value": "Priority RAAC rebuild scheme (NHP Cohort 1)"},
            {"label": "Estate", "value": "WSH (Bury St Edmunds) + Newmarket Community + Sudbury Health Centre"},
            {"label": "Accounting", "value": "Non-cash · valuation movement only · no PDC/cash impact"},
            {"label": "Valuation cycle", "value": "Quinquennial revaluation + interim desktop · DV/Cushman valuer"},
            {"label": "Group context", "value": "Suffolk and North East Essex ICS · joint working with ESNEFT"}
        ],
        "notes": "West Suffolk's impairment charge is structurally driven by the RAAC-pervasive Bury St Edmunds tower — one of the most acute RAAC cases nationally and a confirmed NHP priority rebuild. Each revaluation cycle widens the gap between MEA and DRC as RAAC mitigation continues and the rebuild capital is recognised on a phased basis. This is a non-cash charge with no cash or PDC implication, but it is the largest single line in the trust's premises totals.",
        "sources": [
            {"publisher": "West Suffolk NHS Foundation Trust", "title": "Annual report and accounts", "url": "https://www.wsh.nhs.uk/About-us/Our-publications.aspx"},
            {"publisher": "NHS England", "title": "New Hospital Programme — RAAC schemes", "url": "https://www.england.nhs.uk/new-hospital-programme/"},
            {"publisher": "DHSC", "title": "RAAC in NHS estate", "url": "https://www.gov.uk/government/publications/raac-in-the-nhs-estate"}
        ],
        "related": ["West Suffolk NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — Cambridge University Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Cambridge University Hospitals NHS Foundation Trust"}],
        "description": "Premises running costs across CUH's Cambridge Biomedical Campus estate — Addenbrooke's Hospital (the major adult tertiary, including the regional major-trauma centre, transplant and neurosciences) and the Rosie Hospital (women's + maternity), embedded in the wider campus alongside Royal Papworth, the LMB, MRC, AstraZeneca DISC, Wellcome/Sanger and the new Cambridge Children's Hospital build.",
        "beneficiaries": "c. 1m+ patient contacts/year — major trauma, transplant (renal, liver, BMT, CAR-T), neurosciences, specialist paediatrics. Catchment beyond Cambridgeshire as a tertiary referral centre.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£88.51M"},
            {"label": "Estate scale", "value": "Addenbrooke's + Rosie + Cambridge Biomedical Campus shared infrastructure"},
            {"label": "Tertiary tilt", "value": "Major trauma · transplant (renal/liver/BMT/CAR-T) · neurosciences"},
            {"label": "Hard FM model", "value": "In-house Estates with specialist sub-contracts (no acute PFI)"},
            {"label": "NHP cohort", "value": "Cambridge Children's Hospital (joint with CPFT) confirmed in NHP"},
            {"label": "Campus dynamics", "value": "Shared services + utilities apportionment with Royal Papworth + research tenants"},
            {"label": "Net Zero", "value": "PSDS-funded heat decarbonisation · LED rollout"},
            {"label": "YoY change", "value": "c. +6-8% (energy reset + rising research-tenant infrastructure)"},
            {"label": "Group context", "value": "Cambridgeshire & Peterborough ICS · AHSC with University of Cambridge"}
        ],
        "notes": "CUH's premises spend is shaped by the unique Cambridge Biomedical Campus dynamic — Addenbrooke's runs an in-house estate but shares utilities and infrastructure with Royal Papworth, the LMB and a dense research-tenant base, requiring complex apportionment. Cambridge Children's Hospital construction is live and decant pressures add to operating premises. RM6011 energy reset and 5-7% hard-FM inflation drive the 2024-25 uplift.",
        "sources": [
            {"publisher": "Cambridge University Hospitals NHS Foundation Trust", "title": "Annual report and accounts", "url": "https://www.cuh.nhs.uk/about-us/publications/"},
            {"publisher": "NHS England", "title": "New Hospital Programme — Cambridge Children's Hospital", "url": "https://www.england.nhs.uk/new-hospital-programme/"},
            {"publisher": "Salix Finance", "title": "Public Sector Decarbonisation Scheme", "url": "https://www.salixfinance.co.uk/PSDS"}
        ],
        "related": ["Cambridge University Hospitals NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "PFI / LIFT charges — King’s College Hospital NHS Foundation Trust": {
        "aliases": [{"name": "PFI / LIFT charges", "parent": "King’s College Hospital NHS Foundation Trust"}],
        "description": "PFI unitary-payment charges on King's PFI estate — most materially the Princess Royal University Hospital (Farnborough/Orpington, the c. 2003 Catalyst Healthcare Bromley PFI which transferred to King's at the 2013 Bromley Hospitals merger) plus PFI elements on the Denmark Hill site (Golden Jubilee Wing, 2003). Charges cover availability, lifecycle and hard-FM under c. 30-year concessions.",
        "beneficiaries": "Patients across south-east London, Bromley and Kent referrals — major trauma + tertiary liver/HPB/neuro at Denmark Hill, district + ED at PRUH.",
        "legal_basis": "IFRIC 12 (PFI) · IFRS 16 · NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · individual PFI Project Agreements",
        "key_stats": [
            {"label": "PFI / LIFT charges 2024-25", "value": "£81.76M"},
            {"label": "Major contract", "value": "PRUH (Bromley) — Catalyst Healthcare · c. 2003 close · ~30-year concession"},
            {"label": "Denmark Hill PFI", "value": "Golden Jubilee Wing (2003) — Octagon Healthcare-equivalent SPV"},
            {"label": "RPI exposure", "value": "Unitary payment partly RPI-linked — uplift on 2022-23 RPI peak"},
            {"label": "Concession end", "value": "c. 2032-2033 PRUH expiry — handback condition surveys live"},
            {"label": "FM scope", "value": "Hard FM + lifecycle + availability deductions framework"},
            {"label": "Trust merger", "value": "PRUH joined King's in 2013 from Bromley Hospitals"},
            {"label": "Group context", "value": "South East London ICS · partnership with GSTT + Lewisham & Greenwich"}
        ],
        "notes": "King's PFI line is dominated by the Princess Royal University Hospital concession inherited from the 2013 Bromley merger, with a smaller Denmark Hill PFI element. The 2022-23 RPI peak feeds through the unitary indexation in 2024-25, lifting the charge. With c. 2032-33 concession expiry approaching, handback condition surveys and lifecycle disputes are live operational pressures.",
        "sources": [
            {"publisher": "King's College Hospital NHS Foundation Trust", "title": "Annual report and accounts", "url": "https://www.kch.nhs.uk/about/corporate/annual-reports"},
            {"publisher": "HM Treasury", "title": "Private Finance Initiative and Private Finance 2 projects", "url": "https://www.gov.uk/government/publications/private-finance-initiative-and-private-finance-2-projects-2018-summary-data"},
            {"publisher": "NHS England", "title": "PFI / LIFT in the NHS", "url": "https://www.england.nhs.uk/financial-accounts/"}
        ],
        "related": ["King’s College Hospital NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — University Hospitals Birmingham NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "University Hospitals Birmingham NHS Foundation Trust"}],
        "description": "Premises running costs across UHB's four-site enlarged estate — Queen Elizabeth Hospital Birmingham (the 2010 Edgbaston tower with major trauma, liver transplant and the on-site military Royal Centre for Defence Medicine, under PFI), Heartlands (Bordesley Green), Good Hope (Sutton Coldfield) and Solihull. Spend is shaped by the post-2018 HEFT merger absorbing three older non-PFI sites alongside the modern QEHB.",
        "beneficiaries": "c. 2.2m residents across Birmingham + Solihull + tertiary referrals + UK military medical patients via RCDM — major trauma + tertiary at QEHB, district acute at Heartlands, elective + community at Good Hope/Solihull.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£73.94M"},
            {"label": "Estate scale", "value": "4 hospital sites — QEHB (PFI) + Heartlands + Good Hope + Solihull"},
            {"label": "PFI carve-out", "value": "QEHB under c. 2010 PFI (separate PFI line) — Consort Healthcare"},
            {"label": "Heartlands fabric", "value": "1930s-onwards build · ageing MEP · backlog pressure"},
            {"label": "Hard FM model", "value": "PFI hard-FM at QEHB · in-house at Heartlands/Good Hope/Solihull"},
            {"label": "RCDM tenant", "value": "Defence Medical Services co-tenanted at QEHB"},
            {"label": "Net Zero", "value": "PSDS-funded heat decarbonisation across non-PFI sites"},
            {"label": "YoY change", "value": "c. +6-8% (energy reset + ageing Heartlands fabric)"},
            {"label": "Group context", "value": "Birmingham and Solihull ICS"}
        ],
        "notes": "UHB's premises-other line covers the operating premises overhead outside the QEHB PFI envelope — dominated by the ageing Heartlands estate (1930s-onwards build with material backlog) and the Good Hope/Solihull sites absorbed at the 2018 HEFT merger. The post-2022 Bewick/Mannion-era programme has driven estate investment alongside the operating run-rate. RM6011 energy reset and 5-7% hard-FM inflation lift the 2024-25 charge.",
        "sources": [
            {"publisher": "University Hospitals Birmingham NHS Foundation Trust", "title": "Annual report and accounts", "url": "https://www.uhb.nhs.uk/annual-report.htm"},
            {"publisher": "NHS England", "title": "Provider financial accounts", "url": "https://www.england.nhs.uk/financial-accounts/"},
            {"publisher": "Salix Finance", "title": "Public Sector Decarbonisation Scheme", "url": "https://www.salixfinance.co.uk/PSDS"}
        ],
        "related": ["University Hospitals Birmingham NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Social security & levy — Oxford University Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Social security & levy", "parent": "Oxford University Hospitals NHS Foundation Trust"}],
        "description": "Employer NIC + Apprenticeship Levy on OUH's c. 13,500-strong workforce across the John Radcliffe (the major trauma centre and adult acute), Churchill Hospital (oncology, renal, transplant), Nuffield Orthopaedic Centre and Horton General (Banbury) — anchored by the AHSC partnership with the University of Oxford and the BRC.",
        "beneficiaries": "c. 13,500 staff with high research-active senior FTE share — academic-clinical tilt via Oxford AHSC raises consultant + research salaries.",
        "legal_basis": "Social Security Contributions and Benefits Act 1992 · Finance Act 2016 (Apprenticeship Levy) · NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Social security & levy 2024-25", "value": "£71.77M"},
            {"label": "Headcount", "value": "c. 13,500 (4-site teaching trust)"},
            {"label": "Employer NIC rate", "value": "13.8% on earnings >£9,100 (2024-25)"},
            {"label": "Apprenticeship Levy", "value": "0.5% of paybill"},
            {"label": "April 2025 step-up", "value": "15% NIC · £5,000 threshold"},
            {"label": "Tertiary tilt", "value": "Major trauma + transplant + tertiary cancer + neurosciences raise consultant share"},
            {"label": "Pay drivers 2024-25", "value": "AfC 5.5% · medical 6%"},
            {"label": "Backfill drag", "value": "2023-24 IA backfill at premium rates"},
            {"label": "Group context", "value": "Buckinghamshire, Oxfordshire and Berkshire West ICS · AHSC with University of Oxford"}
        ],
        "notes": "OUH's social-security cost reflects a high-pay academic-clinical workforce — Oxford BRC research-active consultants, major trauma + transplant senior teams — and a 2024-25 paybill lifted by AfC 5.5% and the junior-doctor settlement. April 2025 employer NIC step-up to 15% with £5,000 threshold compounds the run-rate materially, particularly for the specialist consultant base.",
        "sources": [
            {"publisher": "Oxford University Hospitals NHS Foundation Trust", "title": "Annual report and accounts", "url": "https://www.ouh.nhs.uk/about/publications/"},
            {"publisher": "HMRC", "title": "Rates and thresholds for employers 2024 to 2025", "url": "https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2024-to-2025"},
            {"publisher": "NHS Employers", "title": "Pay and Conditions Circulars", "url": "https://www.nhsemployers.org/publications/pay-and-conditions-circulars"}
        ],
        "related": ["Oxford University Hospitals NHS Foundation Trust", "Staff Costs"]
    },
    "Social security & levy — University Hospital Southampton NHS Foundation Trust": {
        "aliases": [{"name": "Social security & levy", "parent": "University Hospital Southampton NHS Foundation Trust"}],
        "description": "Employer NIC + Apprenticeship Levy on UHS's c. 12,500-strong workforce across Southampton General (the major trauma + adult tertiary), Princess Anne (women's + maternity) and Royal South Hants — anchored by the AHSC partnership with the University of Southampton and the Wessex BRC. UHS hosts regional cardiac, neurosciences, paediatric and burn services for central southern England.",
        "beneficiaries": "c. 12,500 staff with research-active senior FTE share lifted by Wessex BRC; tertiary case-mix raises consultant share.",
        "legal_basis": "Social Security Contributions and Benefits Act 1992 · Finance Act 2016 (Apprenticeship Levy) · NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Social security & levy 2024-25", "value": "£67.15M"},
            {"label": "Headcount", "value": "c. 12,500 (3-site teaching trust)"},
            {"label": "Employer NIC rate", "value": "13.8% (2024-25)"},
            {"label": "Apprenticeship Levy", "value": "0.5% of paybill"},
            {"label": "April 2025 step-up", "value": "15% NIC · £5,000 threshold"},
            {"label": "Tertiary tilt", "value": "Major trauma + cardiac + neurosciences + regional paediatrics + burn unit"},
            {"label": "Pay drivers 2024-25", "value": "AfC 5.5% · medical 6%"},
            {"label": "Backfill drag", "value": "Industrial-action backfill at premium rates lifts NIable pay"},
            {"label": "Group context", "value": "Hampshire and IoW ICS · AHSC with University of Southampton + Wessex BRC"}
        ],
        "notes": "UHS's social-security cost reflects a Wessex-tertiary case-mix with research-active academic-clinical staff via the BRC, and a 2024-25 paybill lifted by AfC 5.5% and the junior-doctor settlement. The 2023-24 industrial-action backfill at premium rates is still working through. April 2025 NIC step-up to 15% with £5,000 threshold adds materially to the run-rate.",
        "sources": [
            {"publisher": "University Hospital Southampton NHS Foundation Trust", "title": "Annual report and accounts", "url": "https://www.uhs.nhs.uk/about-us/who-we-are/annual-reports-and-publications/"},
            {"publisher": "HMRC", "title": "Rates and thresholds for employers 2024 to 2025", "url": "https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2024-to-2025"},
            {"publisher": "NHS Employers", "title": "Pay and Conditions Circulars", "url": "https://www.nhsemployers.org/publications/pay-and-conditions-circulars"}
        ],
        "related": ["University Hospital Southampton NHS Foundation Trust", "Staff Costs"]
    },
    "Social security & levy — University Hospitals of Derby and Burton NHS Foundation Trust": {
        "aliases": [{"name": "Social security & levy", "parent": "University Hospitals of Derby and Burton NHS Foundation Trust"}],
        "description": "Employer NIC + Apprenticeship Levy on UHDB's c. 13,000-strong workforce across the Royal Derby Hospital (Mickleover, the consolidated 2009-onwards PFI acute), Queen's Hospital Burton, Florence Nightingale Community, Sir Robert Peel Community (Tamworth) and Samuel Johnson Community (Lichfield) — the post-2018 enlarged trust formed by the merger of Derby + Burton.",
        "beneficiaries": "c. 13,000 staff across an unusual multi-site geography — district acute at both ends (Derby + Burton) plus three community hospitals.",
        "legal_basis": "Social Security Contributions and Benefits Act 1992 · Finance Act 2016 (Apprenticeship Levy) · NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Social security & levy 2024-25", "value": "£64.32M"},
            {"label": "Headcount", "value": "c. 13,000 (5-site post-2018 merger)"},
            {"label": "Employer NIC rate", "value": "13.8% (2024-25)"},
            {"label": "Apprenticeship Levy", "value": "0.5% of paybill"},
            {"label": "April 2025 step-up", "value": "15% NIC · £5,000 threshold"},
            {"label": "Pay drivers 2024-25", "value": "AfC 5.5% · medical 6%"},
            {"label": "Backfill drag", "value": "Industrial-action backfill keeps premium-rate spend elevated"},
            {"label": "Group context", "value": "Joined Up Care Derbyshire ICS + Staffordshire/Stoke ICS (split footprint)"},
            {"label": "Merger context", "value": "Derby + Burton merger 2018 — integration efficiencies still being realised"}
        ],
        "notes": "UHDB's social-security cost reflects a stable 13,000-strong workforce across the post-2018-merger Derby + Burton footprint, with the 2024-25 paybill lifted by AfC 5.5% and the junior-doctor settlement. The trust spans two ICS footprints (Derbyshire + Staffordshire), adding workforce-planning complexity. April 2025 NIC step-up to 15% with £5,000 threshold compounds the on-cost.",
        "sources": [
            {"publisher": "University Hospitals of Derby and Burton NHS Foundation Trust", "title": "Annual report and accounts", "url": "https://www.uhdb.nhs.uk/annual-report-and-accounts"},
            {"publisher": "HMRC", "title": "Rates and thresholds for employers 2024 to 2025", "url": "https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2024-to-2025"},
            {"publisher": "NHS Employers", "title": "Pay and Conditions Circulars", "url": "https://www.nhsemployers.org/publications/pay-and-conditions-circulars"}
        ],
        "related": ["University Hospitals of Derby and Burton NHS Foundation Trust", "Staff Costs"]
    },
    "Premises (other) — Frimley Health NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Frimley Health NHS Foundation Trust"}],
        "description": "Premises running costs across Frimley Health's three-acute estate — Frimley Park (Camberley, the major 1970s RAAC tower confirmed in the NHP priority cohort), Wexham Park (Slough) and Heatherwood (Ascot, the 2022 elective treatment centre rebuild). RAAC mitigation at Frimley Park is the structural cost driver; Heatherwood's modern build pulls in the opposite direction.",
        "beneficiaries": "c. 900,000 catchment across north Hampshire, Surrey, east Berkshire and south Buckinghamshire — major emergency at Frimley Park + Wexham Park, elective at Heatherwood.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£62.50M"},
            {"label": "Estate scale", "value": "3 hospital sites — Frimley Park (RAAC) + Wexham Park + Heatherwood (2022 rebuild)"},
            {"label": "Frimley Park RAAC", "value": "Confirmed widespread RAAC · multi-year mitigation programme"},
            {"label": "NHP cohort", "value": "Frimley Park — confirmed priority RAAC rebuild scheme"},
            {"label": "Heatherwood", "value": "2022 elective treatment centre — modern fabric · low backlog"},
            {"label": "Hard FM model", "value": "Mixed in-house + specialist sub-contracts (no acute PFI)"},
            {"label": "Net Zero", "value": "PSDS-funded heat decarbonisation at Wexham + Heatherwood"},
            {"label": "YoY change", "value": "c. +6-9% (RAAC mitigation + energy reset)"},
            {"label": "Group context", "value": "Frimley ICS — host trust"}
        ],
        "notes": "Frimley Health's premises spend is structurally dominated by the Frimley Park RAAC mitigation programme — propping, monitoring and decanting works while the NHP rebuild progresses through pre-construction. Heatherwood's 2022 modern build offsets some of the cost run-rate but Frimley Park dominates. RM6011 energy reset and 5-7% hard-FM inflation drive the 2024-25 uplift on top of RAAC works.",
        "sources": [
            {"publisher": "Frimley Health NHS Foundation Trust", "title": "Annual report and accounts", "url": "https://www.fhft.nhs.uk/about-us/our-board-of-directors/board-papers-and-publications/"},
            {"publisher": "NHS England", "title": "New Hospital Programme — RAAC schemes (Frimley Park)", "url": "https://www.england.nhs.uk/new-hospital-programme/"},
            {"publisher": "DHSC", "title": "RAAC in NHS estate", "url": "https://www.gov.uk/government/publications/raac-in-the-nhs-estate"}
        ],
        "related": ["Frimley Health NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "PFI / LIFT charges — Oxford University Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "PFI / LIFT charges", "parent": "Oxford University Hospitals NHS Foundation Trust"}],
        "description": "PFI unitary-payment charges on OUH's John Radcliffe and Churchill PFI estate — most materially the 2007 West Wing / Children's Hospital and Women's Centre developments at the JR site, and the c. 2007 Churchill Cancer & Haematology Centre / Oxford Heart Centre. Charges cover availability, lifecycle and hard-FM under c. 30-year concessions.",
        "beneficiaries": "Patients across Oxfordshire + tertiary referrals — JR West Wing for neurosciences/cardiac, Children's Hospital + Women's Centre, Churchill cancer + transplant.",
        "legal_basis": "IFRIC 12 (PFI) · IFRS 16 · NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · individual PFI Project Agreements",
        "key_stats": [
            {"label": "PFI / LIFT charges 2024-25", "value": "£60.64M"},
            {"label": "Major contracts", "value": "JR West Wing/Children's/Women's (2007) + Churchill Cancer & Haematology (2007)"},
            {"label": "Concession term", "value": "c. 30-year — expiry mid-2030s"},
            {"label": "RPI exposure", "value": "Unitary payment partly RPI-linked — 2022-23 RPI peak feeds 2024-25"},
            {"label": "FM scope", "value": "Hard FM + lifecycle + availability deductions framework"},
            {"label": "Tertiary tilt", "value": "Specialist cancer + cardiac + neurosciences housed in PFI estate"},
            {"label": "Group context", "value": "Buckinghamshire, Oxfordshire and Berkshire West ICS"},
            {"label": "Concession end", "value": "Handback condition surveys live for mid-2030s expiry"}
        ],
        "notes": "OUH's PFI line is dominated by the 2007-vintage JR West Wing / Children's Hospital / Women's Centre and the Churchill Cancer Centre developments, with c. 30-year concessions expiring mid-2030s. The 2022-23 RPI peak feeds through the unitary indexation in 2024-25. Lifecycle and handback condition surveys are increasingly material as concessions mature.",
        "sources": [
            {"publisher": "Oxford University Hospitals NHS Foundation Trust", "title": "Annual report and accounts", "url": "https://www.ouh.nhs.uk/about/publications/"},
            {"publisher": "HM Treasury", "title": "PFI and PF2 projects 2018 summary data", "url": "https://www.gov.uk/government/publications/private-finance-initiative-and-private-finance-2-projects-2018-summary-data"},
            {"publisher": "NHS England", "title": "Provider financial accounts", "url": "https://www.england.nhs.uk/financial-accounts/"}
        ],
        "related": ["Oxford University Hospitals NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — University Hospitals of Leicester NHS Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "University Hospitals of Leicester NHS Trust"}],
        "description": "Premises running costs across UHL's three-site estate — Leicester Royal Infirmary (the city-centre acute and ED), Leicester General (the diabetes/renal site) and Glenfield Hospital (cardiac, respiratory, ECMO and lung transplant). The current estate carries the long-running 'Reconfiguration of Acute Services' programme that consolidates emergency care at LRI and elective at LGH, with major NHP capital flowing.",
        "beneficiaries": "c. 1.1m residents across Leicester, Leicestershire and Rutland + tertiary cardiac/respiratory referrals — major emergency at LRI, specialist cardiothoracic at Glenfield.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15 · Listed Buildings and Conservation Areas Act 1990",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£59.90M"},
            {"label": "Estate scale", "value": "3 hospital sites — LRI + LGH + Glenfield + community estate"},
            {"label": "Reconfiguration", "value": "NHP-funded acute reconfiguration · ED consolidation at LRI · elective at LGH"},
            {"label": "Hard FM model", "value": "In-house Estates with specialist sub-contracts (no acute PFI)"},
            {"label": "Listed fabric", "value": "LRI Victorian core · partial listing"},
            {"label": "Glenfield specialism", "value": "ECMO national centre · adult congenital cardiac"},
            {"label": "Net Zero", "value": "PSDS-funded heat decarbonisation · LED rollout"},
            {"label": "YoY change", "value": "c. +6-8% (energy reset + NHP enabling works)"},
            {"label": "Group context", "value": "Leicester, Leicestershire and Rutland ICS"}
        ],
        "notes": "UHL's premises spend is structurally lifted by the long-running tri-site reconfiguration — NHP capital is flowing for major rebuilds at LRI + LGH while ageing fabric continues to consume operating spend, and decant arrangements drive temporary works. Glenfield's specialist ECMO/cardiothoracic estate carries higher utility load. RM6011 energy reset and 5-7% hard-FM inflation drive the 2024-25 uplift.",
        "sources": [
            {"publisher": "University Hospitals of Leicester NHS Trust", "title": "Annual report and accounts", "url": "https://www.leicestershospitals.nhs.uk/aboutus/our-news-publications/our-publications/"},
            {"publisher": "NHS England", "title": "New Hospital Programme — Leicester schemes", "url": "https://www.england.nhs.uk/new-hospital-programme/"},
            {"publisher": "Salix Finance", "title": "Public Sector Decarbonisation Scheme", "url": "https://www.salixfinance.co.uk/PSDS"}
        ],
        "related": ["University Hospitals of Leicester NHS Trust", "Premises & Infrastructure"]
    },
    "General supplies & services — St George's University Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "St George's University Hospitals NHS Foundation Trust"}],
        "description": "Non-clinical general consumables and supplies across St George's Tooting — the Tooting major-trauma centre, regional cardiac/cardiothoracic, neurosciences and one of England's HCID (High Consequence Infectious Diseases) units alongside Royal Free + NCH Liverpool. Now part of the GESH (St George's, Epsom and St Helier) group from 2023.",
        "beneficiaries": "c. 3.5m people across south-west London + Surrey + tertiary referrals — major trauma, HCID isolation, regional cardiac, plus group services across Epsom + St Helier sites under GESH from 2023.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · Public Contracts Regulations 2015 / Procurement Act 2023 · NHS Supply Chain framework",
        "key_stats": [
            {"label": "General supplies & services 2024-25", "value": "£58.20M"},
            {"label": "Coverage", "value": "Office consumables · stationery · printing · uniforms · housekeeping non-clinical · catering provisions"},
            {"label": "HCID overhead", "value": "PPE + isolation consumables uplift versus standard acute"},
            {"label": "Major trauma overhead", "value": "Trauma-team consumables (non-clinical scope) at higher run-rate"},
            {"label": "Procurement framework", "value": "NHS Supply Chain · NHS Shared Business Services · CCS frameworks"},
            {"label": "Group context", "value": "GESH group with Epsom & St Helier from 2023 — group-level procurement"},
            {"label": "Site count", "value": "St George's Tooting + linked sites under GESH"},
            {"label": "YoY change", "value": "c. +4-6% (consumables inflation + GESH group ramp)"}
        ],
        "notes": "St George's general-supplies line is shaped by the Tooting major-trauma + HCID case-mix, which lifts non-clinical consumables (PPE, housekeeping, isolation supplies) above district-acute peers. The 2023 GESH group with Epsom & St Helier is driving group-level procurement consolidation but cost separation between trusts is still being realised. NHS Supply Chain volume uplifts plus general consumables inflation drive the 2024-25 charge.",
        "sources": [
            {"publisher": "St George's, Epsom and St Helier University Hospitals and Health Group", "title": "Annual reports and publications", "url": "https://www.stgeorges.nhs.uk/about/publications/"},
            {"publisher": "NHS Supply Chain", "title": "About NHS Supply Chain", "url": "https://www.supplychain.nhs.uk/"},
            {"publisher": "UK Health Security Agency", "title": "High consequence infectious diseases", "url": "https://www.gov.uk/guidance/high-consequence-infectious-diseases-hcid"}
        ],
        "related": ["St George's University Hospitals NHS Foundation Trust", "Clinical Supplies & Drugs"]
    },
    "Social security & levy — East Kent Hospitals University NHS Foundation Trust": {
        "aliases": [{"name": "Social security & levy", "parent": "East Kent Hospitals University NHS Foundation Trust"}],
        "description": "Employer NIC + Apprenticeship Levy on EKHUFT's c. 9,500-strong workforce across the William Harvey Hospital (Ashford), the Queen Elizabeth The Queen Mother Hospital (Margate), the Kent and Canterbury Hospital, and Buckland Hospital (Dover). Workforce on-cost reflects an unusual three-acute coastal Kent footprint with associated rota gaps and premium-rate cover.",
        "beneficiaries": "c. 9,500 staff — district acute consultant + nursing teams across three EDs and a community/elective fourth site.",
        "legal_basis": "Social Security Contributions and Benefits Act 1992 · Finance Act 2016 (Apprenticeship Levy) · NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Social security & levy 2024-25", "value": "£55.49M"},
            {"label": "Headcount", "value": "c. 9,500 (3-acute + 1-community trust)"},
            {"label": "Employer NIC rate", "value": "13.8% (2024-25)"},
            {"label": "Apprenticeship Levy", "value": "0.5% of paybill"},
            {"label": "April 2025 step-up", "value": "15% NIC · £5,000 threshold"},
            {"label": "Pay drivers 2024-25", "value": "AfC 5.5% · medical 6%"},
            {"label": "Backfill drag", "value": "Rota-gap-driven locum spend on three-ED footprint lifts NIable pay"},
            {"label": "Maternity inquiry", "value": "Reading review (2022) recovery costs flow through workforce uplift"},
            {"label": "Group context", "value": "Kent & Medway ICS"}
        ],
        "notes": "EKHUFT's social-security cost is structurally lifted by the three-acute coastal Kent geography — duplicated rotas across William Harvey, QEQM and (historically) Kent & Canterbury require premium-rate locum cover that flows through NIable pay. The post-Reading-review (2022) maternity recovery has lifted midwifery establishment. April 2025 NIC step-up to 15% with £5,000 threshold compounds the run-rate.",
        "sources": [
            {"publisher": "East Kent Hospitals University NHS Foundation Trust", "title": "Annual report and accounts", "url": "https://www.ekhuft.nhs.uk/patients-and-visitors/about-us/publications/"},
            {"publisher": "HMRC", "title": "Rates and thresholds for employers 2024 to 2025", "url": "https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2024-to-2025"},
            {"publisher": "Department of Health and Social Care", "title": "Reading review of East Kent maternity services", "url": "https://www.gov.uk/government/publications/maternity-and-neonatal-services-in-east-kent-reading-the-signals-report"}
        ],
        "related": ["East Kent Hospitals University NHS Foundation Trust", "Staff Costs"]
    },
    "Social security & levy — East Lancashire Hospitals NHS Trust": {
        "aliases": [{"name": "Social security & levy", "parent": "East Lancashire Hospitals NHS Trust"}],
        "description": "Employer NIC + Apprenticeship Levy on ELHT's c. 9,000-strong workforce across the Royal Blackburn Hospital (the major acute and ED with regional vascular and stroke), Burnley General (the Lancashire Women & Newborn Centre), Pendle Community, Clitheroe and Accrington — serving Pennine Lancashire.",
        "beneficiaries": "c. 9,000 staff — district acute + tertiary-tilt vascular/stroke + regional maternity at Burnley.",
        "legal_basis": "Social Security Contributions and Benefits Act 1992 · Finance Act 2016 (Apprenticeship Levy) · NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Social security & levy 2024-25", "value": "£52.32M"},
            {"label": "Headcount", "value": "c. 9,000 (5-site district acute + community)"},
            {"label": "Employer NIC rate", "value": "13.8% (2024-25)"},
            {"label": "Apprenticeship Levy", "value": "0.5% of paybill"},
            {"label": "April 2025 step-up", "value": "15% NIC · £5,000 threshold"},
            {"label": "Pay drivers 2024-25", "value": "AfC 5.5% · medical 6%"},
            {"label": "Backfill drag", "value": "Pennine geography drives bank/agency cover on rural sites"},
            {"label": "Maternity centralisation", "value": "Regional Lancashire Women & Newborn Centre at Burnley General"},
            {"label": "Group context", "value": "Lancashire and South Cumbria ICS"}
        ],
        "notes": "ELHT's social-security cost reflects a 9,000-strong Pennine workforce, with the 2024-25 paybill lifted by AfC 5.5% and medical 6%. The trust hosts the regional Lancashire Women & Newborn Centre at Burnley which raises midwifery FTE share. Pennine geography drives premium-rate cover on smaller community sites. April 2025 NIC step-up adds materially to the run-rate.",
        "sources": [
            {"publisher": "East Lancashire Hospitals NHS Trust", "title": "Annual report and accounts", "url": "https://elht.nhs.uk/about-us/publications-and-reports"},
            {"publisher": "HMRC", "title": "Rates and thresholds for employers 2024 to 2025", "url": "https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2024-to-2025"},
            {"publisher": "NHS Employers", "title": "Pay and Conditions Circulars", "url": "https://www.nhsemployers.org/publications/pay-and-conditions-circulars"}
        ],
        "related": ["East Lancashire Hospitals NHS Trust", "Staff Costs"]
    },
    "Social security & levy — The Royal Wolverhampton NHS Trust": {
        "aliases": [{"name": "Social security & levy", "parent": "The Royal Wolverhampton NHS Trust"}],
        "description": "Employer NIC + Apprenticeship Levy on RWT's c. 9,500-strong vertically-integrated workforce — New Cross Hospital (Wolverhampton, the major acute), Cannock Chase Hospital and an unusually large primary-care arm (RWT runs a network of GP practices across Wolverhampton + Walsall under the Vertically Integrated Care model). Group structure with The Royal Walsall and Walsall Healthcare under the Black Country Provider Collaborative.",
        "beneficiaries": "c. 9,500 staff including GP/practice-staff TUPE'd into the trust under vertical integration — broader workforce mix than peer acutes.",
        "legal_basis": "Social Security Contributions and Benefits Act 1992 · Finance Act 2016 (Apprenticeship Levy) · NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS (General Medical Services Contracts) Regulations 2015",
        "key_stats": [
            {"label": "Social security & levy 2024-25", "value": "£51.59M"},
            {"label": "Headcount", "value": "c. 9,500 (acute + primary-care vertical integration)"},
            {"label": "Employer NIC rate", "value": "13.8% (2024-25)"},
            {"label": "Apprenticeship Levy", "value": "0.5% of paybill"},
            {"label": "April 2025 step-up", "value": "15% NIC · £5,000 threshold"},
            {"label": "Pay drivers 2024-25", "value": "AfC 5.5% · medical 6% · GP partner remuneration via VIC"},
            {"label": "Vertical integration", "value": "Network of c. 17 GP practices TUPE'd into RWT — primary-care workforce in scope"},
            {"label": "Group context", "value": "Black Country Provider Collaborative · Black Country ICS"},
            {"label": "Workforce mix", "value": "Unusual primary-care staff share lifts overall NIable pay base"}
        ],
        "notes": "RWT's social-security cost is structurally distinctive because of the trust's vertical-integration model — c. 17 GP practices have been TUPE'd into the trust and primary-care staff sit on the NHS paybill, broadening the workforce mix versus peer acutes. The 2024-25 AfC + medical pay awards lift NIable pay; April 2025 NIC step-up adds materially. Black Country Provider Collaborative is driving group efficiencies.",
        "sources": [
            {"publisher": "The Royal Wolverhampton NHS Trust", "title": "Annual report and accounts", "url": "https://www.royalwolverhampton.nhs.uk/about-us/our-publications/"},
            {"publisher": "HMRC", "title": "Rates and thresholds for employers 2024 to 2025", "url": "https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2024-to-2025"},
            {"publisher": "NHS Confederation", "title": "Vertical integration in NHS", "url": "https://www.nhsconfed.org/publications/vertical-integration-primary-and-secondary-care"}
        ],
        "related": ["The Royal Wolverhampton NHS Trust", "Staff Costs"]
    },
    "Social security & levy — Chelsea and Westminster Hospital NHS Foundation Trust": {
        "aliases": [{"name": "Social security & levy", "parent": "Chelsea and Westminster Hospital NHS Foundation Trust"}],
        "description": "Employer NIC + Apprenticeship Levy on CWFT's c. 7,500-strong central/west London workforce across the Chelsea and Westminster Hospital (Fulham Road; the 1990s acute incorporating regional HIV + paediatrics) and West Middlesex University Hospital (Isleworth, joined 2015). The trust hosts the John Hunter HIV Clinic and 56 Dean Street GUM service via CW+ (charity arm) — distinctive workforce mix.",
        "beneficiaries": "c. 7,500 staff with elevated Inner London weighting — sexual health, HIV, paediatrics and dermatology specialists.",
        "legal_basis": "Social Security Contributions and Benefits Act 1992 · Finance Act 2016 (Apprenticeship Levy) · NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Social security & levy 2024-25", "value": "£50.29M"},
            {"label": "Headcount", "value": "c. 7,500 (2-site west London acute)"},
            {"label": "Employer NIC rate", "value": "13.8% (2024-25)"},
            {"label": "Apprenticeship Levy", "value": "0.5% of paybill"},
            {"label": "April 2025 step-up", "value": "15% NIC · £5,000 threshold"},
            {"label": "London weighting", "value": "Inner London HCAS at Chelsea + Outer London at West Middlesex"},
            {"label": "Pay drivers 2024-25", "value": "AfC 5.5% · medical 6%"},
            {"label": "Specialism", "value": "National HIV + sexual health (56 Dean Street, John Hunter Clinic)"},
            {"label": "Group context", "value": "NW London ICS · partnership with Imperial College Healthcare"}
        ],
        "notes": "CWFT's social-security cost reflects a 7,500-strong workforce on Inner + Outer London weighting plus the distinctive HIV/sexual-health specialist workforce supporting national tertiary services. The 2024-25 AfC + medical pay awards lift NIable pay. April 2025 NIC step-up to 15% with £5,000 threshold compounds employer on-cost in 2025-26.",
        "sources": [
            {"publisher": "Chelsea and Westminster Hospital NHS Foundation Trust", "title": "Annual report and accounts", "url": "https://www.chelwest.nhs.uk/about-us/publications"},
            {"publisher": "HMRC", "title": "Rates and thresholds for employers 2024 to 2025", "url": "https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2024-to-2025"},
            {"publisher": "NHS Employers", "title": "Pay and Conditions Circulars", "url": "https://www.nhsemployers.org/publications/pay-and-conditions-circulars"}
        ],
        "related": ["Chelsea and Westminster Hospital NHS Foundation Trust", "Staff Costs"]
    },
    "Social security & levy — University Hospitals Coventry And Warwickshire NHS Trust": {
        "aliases": [{"name": "Social security & levy", "parent": "University Hospitals Coventry And Warwickshire NHS Trust"}],
        "description": "Employer NIC + Apprenticeship Levy on UHCW's c. 9,000-strong workforce across University Hospital Coventry (the Walsgrave PFI tower with major trauma, neurosciences, cancer and IVF/CRM services) and the Hospital of St Cross (Rugby). Workforce on-cost reflects tertiary case-mix at Walsgrave plus the distinctive Centre for Reproductive Medicine.",
        "beneficiaries": "c. 9,000 staff — major trauma + tertiary specialty consultants at UHC, district + elective at Rugby.",
        "legal_basis": "Social Security Contributions and Benefits Act 1992 · Finance Act 2016 (Apprenticeship Levy) · NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Social security & levy 2024-25", "value": "£48.07M"},
            {"label": "Headcount", "value": "c. 9,000 (2-site teaching trust)"},
            {"label": "Employer NIC rate", "value": "13.8% (2024-25)"},
            {"label": "Apprenticeship Levy", "value": "0.5% of paybill"},
            {"label": "April 2025 step-up", "value": "15% NIC · £5,000 threshold"},
            {"label": "Tertiary tilt", "value": "Major trauma + neurosciences + IVF/CRM raise consultant share"},
            {"label": "Pay drivers 2024-25", "value": "AfC 5.5% · medical 6%"},
            {"label": "Backfill drag", "value": "Industrial-action backfill at premium rates"},
            {"label": "Group context", "value": "Coventry and Warwickshire ICS · AHSC links with Warwick Medical School"}
        ],
        "notes": "UHCW's social-security cost reflects a 9,000-strong tertiary-tilted workforce — major trauma, neurosciences and IVF/CRM raise consultant share. The 2024-25 paybill is lifted by AfC 5.5% and the junior-doctor settlement, plus 2023-24 industrial-action backfill at premium rates. April 2025 NIC step-up to 15% with £5,000 threshold adds materially to the run-rate.",
        "sources": [
            {"publisher": "University Hospitals Coventry and Warwickshire NHS Trust", "title": "Annual report and accounts", "url": "https://www.uhcw.nhs.uk/about/publications/"},
            {"publisher": "HMRC", "title": "Rates and thresholds for employers 2024 to 2025", "url": "https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2024-to-2025"},
            {"publisher": "NHS Employers", "title": "Pay and Conditions Circulars", "url": "https://www.nhsemployers.org/publications/pay-and-conditions-circulars"}
        ],
        "related": ["University Hospitals Coventry And Warwickshire NHS Trust", "Staff Costs"]
    },
    "Premises (other) — Manchester University NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Manchester University NHS Foundation Trust"}],
        "description": "Premises running costs across MFT's nine-hospital Greater Manchester estate — Manchester Royal Infirmary, Saint Mary's, Royal Manchester Children's Hospital, Manchester Royal Eye Hospital and University Dental Hospital (the Oxford Road campus PFI), Wythenshawe Hospital (cardiothoracic + transplant), Trafford General, Withington Community and North Manchester General (which has confirmed RAAC and is in the NHP rebuild cohort).",
        "beneficiaries": "c. 2.6m residents across Greater Manchester + tertiary referrals — major trauma + transplant + paediatrics + specialist eye/dental/maternity tertiary services.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£47.71M"},
            {"label": "Estate scale", "value": "9 hospital sites — largest acute trust in England"},
            {"label": "PFI carve-out", "value": "Oxford Road campus 2009 PFI — Catalyst Healthcare (separate PFI line)"},
            {"label": "RAAC exposure", "value": "North Manchester General confirmed RAAC · NHP rebuild scheme"},
            {"label": "Hard FM model", "value": "PFI hard-FM at MRI/RMCH/Saint Mary's · in-house elsewhere"},
            {"label": "Listed fabric", "value": "MRI Victorian core · partial listing"},
            {"label": "Net Zero", "value": "PSDS-funded heat decarbonisation across non-PFI sites"},
            {"label": "YoY change", "value": "c. +6-8% (NMGH RAAC + energy reset)"},
            {"label": "Group context", "value": "GM ICS — lead provider"}
        ],
        "notes": "MFT's premises-other line covers operating premises overhead outside the Oxford Road PFI envelope — dominated by North Manchester General's RAAC mitigation programme, the ageing Wythenshawe estate (cardiothoracic + transplant infrastructure with high utility load), and the Trafford/Withington community estate. RM6011 energy reset and 5-7% hard-FM inflation drive the 2024-25 uplift on top of RAAC works.",
        "sources": [
            {"publisher": "Manchester University NHS Foundation Trust", "title": "Annual report and accounts", "url": "https://mft.nhs.uk/the-trust/corporate-publications/"},
            {"publisher": "NHS England", "title": "New Hospital Programme — RAAC schemes (NMGH)", "url": "https://www.england.nhs.uk/new-hospital-programme/"},
            {"publisher": "DHSC", "title": "RAAC in NHS estate", "url": "https://www.gov.uk/government/publications/raac-in-the-nhs-estate"}
        ],
        "related": ["Manchester University NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — University Hospitals Sussex NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "University Hospitals Sussex NHS Foundation Trust"}],
        "description": "Premises running costs across UHSussex's seven-hospital coastal-Sussex estate — the Royal Sussex County Hospital (Brighton, the major trauma + tertiary, mid-build of the 3Ts new acute), Princess Royal Hospital (Haywards Heath), Worthing Hospital, St Richard's (Chichester), Southlands (Shoreham) and the Sussex Cancer Centre. The trust formed via the 2021 Brighton & Sussex / Western Sussex merger.",
        "beneficiaries": "c. 1.8m residents across coastal Sussex + tertiary referrals — major trauma at Royal Sussex, district acute at PRH/Worthing/St Richard's, regional cancer at Sussex Cancer Centre.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15 · Listed Buildings and Conservation Areas Act 1990",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£47.42M"},
            {"label": "Estate scale", "value": "7 hospital sites — coastal Sussex acute network"},
            {"label": "3Ts programme", "value": "Royal Sussex County Hospital £760M+ rebuild · Stage 1 opened 2023, Stage 2 in build"},
            {"label": "Coastal corrosion", "value": "Salt-air exposure on Brighton + Worthing + Chichester estate"},
            {"label": "Listed fabric", "value": "Royal Sussex Barry Building Grade II* · Worthing core listed"},
            {"label": "Hard FM model", "value": "In-house Estates with specialist sub-contracts (no acute PFI)"},
            {"label": "Net Zero", "value": "PSDS-funded heat decarbonisation"},
            {"label": "YoY change", "value": "c. +6-8% (3Ts decant + coastal corrosion + energy reset)"},
            {"label": "Group context", "value": "Sussex ICS · post-2021 Brighton/Sussex/Western Sussex merger"}
        ],
        "notes": "UHSussex's premises spend is shaped by the live 3Ts (Trauma, Teaching and Tertiary care) major rebuild at Royal Sussex (Stage 1 opened 2023, Stage 2 mid-build), coastal-corrosion driven fabric maintenance across the seven-hospital network, and the Grade II* listed Barry Building. Decant/temporary works during 3Ts add to the operating run-rate. RM6011 energy reset and 5-7% hard-FM inflation drive the 2024-25 uplift.",
        "sources": [
            {"publisher": "University Hospitals Sussex NHS Foundation Trust", "title": "Annual report and accounts", "url": "https://www.uhsussex.nhs.uk/about-us/publications/"},
            {"publisher": "University Hospitals Sussex NHS Foundation Trust", "title": "3Ts Hospital Redevelopment Programme", "url": "https://www.uhsussex.nhs.uk/3ts/"},
            {"publisher": "Salix Finance", "title": "Public Sector Decarbonisation Scheme", "url": "https://www.salixfinance.co.uk/PSDS"}
        ],
        "related": ["University Hospitals Sussex NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Social security & levy — University Hospitals Dorset NHS Foundation Trust": {
        "aliases": [{"name": "Social security & levy", "parent": "University Hospitals Dorset NHS Foundation Trust"}],
        "description": "Employer NIC + Apprenticeship Levy on UHD's c. 8,500-strong workforce across Royal Bournemouth Hospital, Poole Hospital and Christchurch Hospital — the post-2020 Bournemouth + Poole merger trust mid-way through the BEACH (Bournemouth Emergency Acute Care Hospital) reconfiguration that consolidates emergency at Bournemouth and elective at Poole.",
        "beneficiaries": "c. 8,500 staff across the BCP conurbation — district acute consultant + nursing teams transitioning to a hot/cold split.",
        "legal_basis": "Social Security Contributions and Benefits Act 1992 · Finance Act 2016 (Apprenticeship Levy) · NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Social security & levy 2024-25", "value": "£46.32M"},
            {"label": "Headcount", "value": "c. 8,500 (3-site post-2020 merger)"},
            {"label": "Employer NIC rate", "value": "13.8% (2024-25)"},
            {"label": "Apprenticeship Levy", "value": "0.5% of paybill"},
            {"label": "April 2025 step-up", "value": "15% NIC · £5,000 threshold"},
            {"label": "Pay drivers 2024-25", "value": "AfC 5.5% · medical 6%"},
            {"label": "BEACH reconfiguration", "value": "Hot/cold split · staff transition between sites driving establishment review"},
            {"label": "Backfill drag", "value": "Industrial-action backfill at premium rates"},
            {"label": "Group context", "value": "Dorset ICS"}
        ],
        "notes": "UHD's social-security cost reflects an 8,500-strong workforce mid-way through the BEACH reconfiguration — staff are transitioning between Bournemouth (emergency) and Poole (elective) which creates establishment volatility. The 2024-25 paybill is lifted by AfC 5.5% and medical 6%; April 2025 NIC step-up adds materially to the run-rate.",
        "sources": [
            {"publisher": "University Hospitals Dorset NHS Foundation Trust", "title": "Annual report and accounts", "url": "https://www.uhd.nhs.uk/about/publications/"},
            {"publisher": "HMRC", "title": "Rates and thresholds for employers 2024 to 2025", "url": "https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2024-to-2025"},
            {"publisher": "NHS Employers", "title": "Pay and Conditions Circulars", "url": "https://www.nhsemployers.org/publications/pay-and-conditions-circulars"}
        ],
        "related": ["University Hospitals Dorset NHS Foundation Trust", "Staff Costs"]
    },
    "Social security & levy — York and Scarborough Teaching Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Social security & levy", "parent": "York and Scarborough Teaching Hospitals NHS Foundation Trust"}],
        "description": "Employer NIC + Apprenticeship Levy on YSTH's c. 8,500-strong workforce spread across an unusually large geography — York Hospital (the major acute), Scarborough Hospital (the coastal acute c. 40 miles away), Bridlington Hospital, Selby Community, Malton Community and St Monica's (Easingwold). Workforce on-cost is shaped by York–Scarborough rota duplication and rural premium-rate cover.",
        "beneficiaries": "c. 8,500 staff across an unusually wide York–North Yorkshire–East Riding footprint with two-site ED rotas.",
        "legal_basis": "Social Security Contributions and Benefits Act 1992 · Finance Act 2016 (Apprenticeship Levy) · NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Social security & levy 2024-25", "value": "£45.86M"},
            {"label": "Headcount", "value": "c. 8,500 (6-site rural acute network)"},
            {"label": "Employer NIC rate", "value": "13.8% (2024-25)"},
            {"label": "Apprenticeship Levy", "value": "0.5% of paybill"},
            {"label": "April 2025 step-up", "value": "15% NIC · £5,000 threshold"},
            {"label": "Pay drivers 2024-25", "value": "AfC 5.5% · medical 6%"},
            {"label": "Geography premium", "value": "York–Scarborough 40-mile separation drives premium-rate locum cover"},
            {"label": "Coastal exposure", "value": "Scarborough + Bridlington — North Sea coastal sites"},
            {"label": "Group context", "value": "Humber and North Yorkshire ICS"}
        ],
        "notes": "YSTH's social-security cost is structurally elevated by the wide York–Scarborough geography requiring duplicated ED + obstetrics rotas across two acutes 40 miles apart, plus rural-site premium-rate locum cover. The 2024-25 paybill is lifted by AfC 5.5% and medical 6%. April 2025 NIC step-up to 15% with £5,000 threshold adds materially to the run-rate, particularly for the high-locum-share workforce.",
        "sources": [
            {"publisher": "York and Scarborough Teaching Hospitals NHS Foundation Trust", "title": "Annual report and accounts", "url": "https://www.yorkhospitals.nhs.uk/about-us/publications/"},
            {"publisher": "HMRC", "title": "Rates and thresholds for employers 2024 to 2025", "url": "https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2024-to-2025"},
            {"publisher": "NHS Employers", "title": "Pay and Conditions Circulars", "url": "https://www.nhsemployers.org/publications/pay-and-conditions-circulars"}
        ],
        "related": ["York and Scarborough Teaching Hospitals NHS Foundation Trust", "Staff Costs"]
    },
    "Social security & levy — South Tees Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Social security & levy", "parent": "South Tees Hospitals NHS Foundation Trust"}],
        "description": "Employer NIC + Apprenticeship Levy on South Tees's c. 9,000-strong workforce across the James Cook University Hospital (Middlesbrough — the major trauma centre and tertiary cardiothoracic, neurosciences and spinal injuries hub for the North East) and the Friarage Hospital (Northallerton, the rural acute serving North Yorkshire's Dales/Moors).",
        "beneficiaries": "c. 9,000 staff — major-trauma + tertiary consultant teams at James Cook plus rural acute workforce at the Friarage.",
        "legal_basis": "Social Security Contributions and Benefits Act 1992 · Finance Act 2016 (Apprenticeship Levy) · NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Social security & levy 2024-25", "value": "£45.19M"},
            {"label": "Headcount", "value": "c. 9,000 (2-site major-trauma + rural acute)"},
            {"label": "Employer NIC rate", "value": "13.8% (2024-25)"},
            {"label": "Apprenticeship Levy", "value": "0.5% of paybill"},
            {"label": "April 2025 step-up", "value": "15% NIC · £5,000 threshold"},
            {"label": "Pay drivers 2024-25", "value": "AfC 5.5% · medical 6%"},
            {"label": "Tertiary tilt", "value": "Major trauma + cardiothoracic + neurosciences + spinal injuries lift consultant share"},
            {"label": "Friarage cover", "value": "Rural acute cover · premium-rate locum reliance"},
            {"label": "Group context", "value": "North East and North Cumbria ICS"}
        ],
        "notes": "South Tees's social-security cost reflects a 9,000-strong North East workforce with a strong tertiary tilt at James Cook (major trauma, cardiothoracic, spinal injuries) plus rural-cover premium at the Friarage. The 2024-25 AfC 5.5% and medical 6% awards lift NIable pay; April 2025 NIC step-up to 15% with £5,000 threshold compounds the run-rate.",
        "sources": [
            {"publisher": "South Tees Hospitals NHS Foundation Trust", "title": "Annual report and accounts", "url": "https://www.southtees.nhs.uk/about/publications/"},
            {"publisher": "HMRC", "title": "Rates and thresholds for employers 2024 to 2025", "url": "https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2024-to-2025"},
            {"publisher": "NHS Employers", "title": "Pay and Conditions Circulars", "url": "https://www.nhsemployers.org/publications/pay-and-conditions-circulars"}
        ],
        "related": ["South Tees Hospitals NHS Foundation Trust", "Staff Costs"]
    },
    "Premises (other) — Royal Free London NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Royal Free London NHS Foundation Trust"}],
        "description": "Premises running costs across Royal Free London's three-site north-London estate — Royal Free Hospital (Hampstead, the 1970s tower hosting the high-level isolation HCID unit, regional liver/HPB transplant and tertiary services), Barnet Hospital (Edgware Road, the c. 1999 PFI district acute) and Chase Farm Hospital (Enfield, the 2018 modern 'digital-first' rebuild). Group of trusts with North Mid + West Herts under Royal Free London Group.",
        "beneficiaries": "c. 1.6m residents across north London + tertiary referrals — HCID isolation, liver transplant, and amyloidosis at Royal Free, district at Barnet, elective at Chase Farm.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15 · Health Protection (Notification) Regulations 2010",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£44.11M"},
            {"label": "Estate scale", "value": "3 hospital sites — Royal Free + Barnet (PFI) + Chase Farm (2018 rebuild)"},
            {"label": "PFI carve-out", "value": "Barnet 1999 PFI (separate PFI line) — Catalyst-equivalent SPV"},
            {"label": "HCID overhead", "value": "High-level isolation unit · enhanced ventilation + decontamination cost"},
            {"label": "Hard FM model", "value": "Mixed PFI hard-FM at Barnet · in-house at Royal Free + Chase Farm"},
            {"label": "Royal Free fabric", "value": "1970s tower · ageing MEP · backlog pressure"},
            {"label": "Net Zero", "value": "PSDS + Royal Free Charity-supported decarbonisation"},
            {"label": "YoY change", "value": "c. +6-8% (energy reset + 1970s tower MEP)"},
            {"label": "Group context", "value": "North Central London ICS · Royal Free London Group"}
        ],
        "notes": "Royal Free London's premises-other line is shaped by the 1970s Hampstead tower (ageing MEP, ward fabric backlog, plus the HCID high-level-isolation unit's enhanced ventilation/decontamination overhead) and the modern 2018 Chase Farm digital build at the other end of the spectrum. RM6011 energy reset and 5-7% hard-FM inflation drive the 2024-25 uplift. Barnet PFI sits in the separate PFI line.",
        "sources": [
            {"publisher": "Royal Free London NHS Foundation Trust", "title": "Annual report and accounts", "url": "https://www.royalfree.nhs.uk/about-us/corporate-information-and-publications/"},
            {"publisher": "UK Health Security Agency", "title": "High consequence infectious diseases — HCID network", "url": "https://www.gov.uk/guidance/high-consequence-infectious-diseases-hcid"},
            {"publisher": "Salix Finance", "title": "Public Sector Decarbonisation Scheme", "url": "https://www.salixfinance.co.uk/PSDS"}
        ],
        "related": ["Royal Free London NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Social security & levy — United Lincolnshire Hospitals NHS Trust": {
        "aliases": [{"name": "Social security & levy", "parent": "United Lincolnshire Hospitals NHS Trust"}],
        "description": "Employer NIC + Apprenticeship Levy on ULH's c. 8,500-strong workforce across Lincoln County Hospital, Pilgrim Hospital (Boston, with confirmed coastal-corrosion fabric pressures), Grantham and District Hospital and Louth County Hospital — serving rural Lincolnshire with an unusually wide geography and material rota gaps.",
        "beneficiaries": "c. 8,500 staff across rural Lincolnshire — district acute consultant + nursing teams with persistent rota challenges.",
        "legal_basis": "Social Security Contributions and Benefits Act 1992 · Finance Act 2016 (Apprenticeship Levy) · NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Social security & levy 2024-25", "value": "£43.66M"},
            {"label": "Headcount", "value": "c. 8,500 (4-site rural acute network)"},
            {"label": "Employer NIC rate", "value": "13.8% (2024-25)"},
            {"label": "Apprenticeship Levy", "value": "0.5% of paybill"},
            {"label": "April 2025 step-up", "value": "15% NIC · £5,000 threshold"},
            {"label": "Pay drivers 2024-25", "value": "AfC 5.5% · medical 6%"},
            {"label": "Rota-gap premium", "value": "Lincolnshire rural geography · persistent locum reliance lifts NIable pay"},
            {"label": "Grantham ED", "value": "Reduced overnight cover · workforce reconfiguration"},
            {"label": "Group context", "value": "Lincolnshire ICS · planned merger with Lincolnshire Community + NLAG"}
        ],
        "notes": "ULH's social-security cost is structurally elevated by Lincolnshire's rural geography — persistent rota gaps drive premium-rate locum reliance which inflates NIable pay versus headcount. The 2024-25 paybill is lifted by AfC 5.5% and medical 6%. April 2025 NIC step-up to 15% with £5,000 threshold compounds the run-rate. Planned Lincolnshire group structure may unlock workforce efficiencies.",
        "sources": [
            {"publisher": "United Lincolnshire Hospitals NHS Trust", "title": "Annual report and accounts", "url": "https://www.ulh.nhs.uk/about/governance/publications/"},
            {"publisher": "HMRC", "title": "Rates and thresholds for employers 2024 to 2025", "url": "https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2024-to-2025"},
            {"publisher": "NHS Employers", "title": "Pay and Conditions Circulars", "url": "https://www.nhsemployers.org/publications/pay-and-conditions-circulars"}
        ],
        "related": ["United Lincolnshire Hospitals NHS Trust", "Staff Costs"]
    },
    "Social security & levy — Hull University Teaching Hospitals NHS Trust": {
        "aliases": [{"name": "Social security & levy", "parent": "Hull University Teaching Hospitals NHS Trust"}],
        "description": "Employer NIC + Apprenticeship Levy on HUTH's c. 8,500-strong workforce across Hull Royal Infirmary (the major acute and ED in central Hull) and Castle Hill Hospital (Cottingham, the cancer + cardiac tertiary site). Operating under the Humber Health Partnership group with NLAG (Northern Lincolnshire & Goole) from 2023, the trust is a confirmed New Hospital Programme rebuild candidate.",
        "beneficiaries": "c. 8,500 staff across the Humber estuary footprint — district acute at HRI, tertiary cardiac/cancer at Castle Hill.",
        "legal_basis": "Social Security Contributions and Benefits Act 1992 · Finance Act 2016 (Apprenticeship Levy) · NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Social security & levy 2024-25", "value": "£43.15M"},
            {"label": "Headcount", "value": "c. 8,500 (2-site teaching trust)"},
            {"label": "Employer NIC rate", "value": "13.8% (2024-25)"},
            {"label": "Apprenticeship Levy", "value": "0.5% of paybill"},
            {"label": "April 2025 step-up", "value": "15% NIC · £5,000 threshold"},
            {"label": "Pay drivers 2024-25", "value": "AfC 5.5% · medical 6%"},
            {"label": "Tertiary tilt", "value": "Cardiac surgery + oncology at Castle Hill raise consultant share"},
            {"label": "Group structure", "value": "Humber Health Partnership group with NLAG (2023)"},
            {"label": "NHP cohort", "value": "Hull Royal Infirmary confirmed in NHP rebuild programme"}
        ],
        "notes": "HUTH's social-security cost reflects an 8,500-strong Humber-estuary workforce with a tertiary cardiac/cancer tilt at Castle Hill. The Humber Health Partnership group with NLAG (formed 2023) is driving group-level workforce planning and shared roles across the two trusts. The 2024-25 AfC + medical pay awards lift NIable pay; April 2025 NIC step-up adds materially to the run-rate.",
        "sources": [
            {"publisher": "Hull University Teaching Hospitals NHS Trust", "title": "Annual report and accounts", "url": "https://www.hey.nhs.uk/about-us/our-publications/"},
            {"publisher": "HMRC", "title": "Rates and thresholds for employers 2024 to 2025", "url": "https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2024-to-2025"},
            {"publisher": "NHS England", "title": "New Hospital Programme — Hull", "url": "https://www.england.nhs.uk/new-hospital-programme/"}
        ],
        "related": ["Hull University Teaching Hospitals NHS Trust", "Staff Costs"]
    },
    "PFI / LIFT charges — University Hospitals of Derby and Burton NHS Foundation Trust": {
        "aliases": [{"name": "PFI / LIFT charges", "parent": "University Hospitals of Derby and Burton NHS Foundation Trust"}],
        "description": "PFI unitary-payment charges on UHDB's Royal Derby Hospital — the c. 2003 Derby Healthcare PFI (Skanska / Innisfree consortium) which built the consolidated Royal Derby site at Mickleover, replacing the old DRI city-centre campus. The Burton sites (Queen's, Florence Nightingale, Sir Robert Peel, Samuel Johnson) are not under PFI.",
        "beneficiaries": "Patients across Derbyshire — major acute, women's, paediatrics, ED at the post-2009-consolidation Royal Derby PFI estate.",
        "legal_basis": "IFRIC 12 (PFI) · IFRS 16 · NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · individual PFI Project Agreement",
        "key_stats": [
            {"label": "PFI / LIFT charges 2024-25", "value": "£41.42M"},
            {"label": "Major contract", "value": "Royal Derby (Mickleover) — Derby Healthcare consortium · Skanska/Innisfree"},
            {"label": "Concession start", "value": "Financial close c. 2003 · operations from 2009-2010"},
            {"label": "Concession term", "value": "c. 30-year — expiry early 2030s"},
            {"label": "RPI exposure", "value": "Unitary payment partly RPI-linked — 2022-23 RPI peak feeds 2024-25"},
            {"label": "FM scope", "value": "Hard FM + lifecycle + availability deductions framework"},
            {"label": "Burton sites", "value": "Outside PFI — operating premises in 'Premises (other)' line"},
            {"label": "Group context", "value": "Joined Up Care Derbyshire ICS"},
            {"label": "Concession end", "value": "Handback condition surveys live"}
        ],
        "notes": "UHDB's PFI line is dominated by the Royal Derby concession at Mickleover — the 2003-financed, 2009-operational consolidation of acute services that closed the historic DRI city-centre site. The 2022-23 RPI peak feeds through the unitary indexation in 2024-25. With the c. 2030s concession expiry approaching, handback surveys and lifecycle disputes are material operational pressures.",
        "sources": [
            {"publisher": "University Hospitals of Derby and Burton NHS Foundation Trust", "title": "Annual report and accounts", "url": "https://www.uhdb.nhs.uk/annual-report-and-accounts"},
            {"publisher": "HM Treasury", "title": "PFI and PF2 projects 2018 summary data", "url": "https://www.gov.uk/government/publications/private-finance-initiative-and-private-finance-2-projects-2018-summary-data"},
            {"publisher": "NHS England", "title": "Provider financial accounts", "url": "https://www.england.nhs.uk/financial-accounts/"}
        ],
        "related": ["University Hospitals of Derby and Burton NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — Lancashire Teaching Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Lancashire Teaching Hospitals NHS Foundation Trust"}],
        "description": "Premises running costs across LTH's two-site estate — the Royal Preston Hospital (Fulwood, the major-trauma centre and regional tertiary for neurosciences, renal/transplant, plastics + burns) and Chorley and South Ribble Hospital. Royal Preston is a confirmed New Hospital Programme rebuild scheme; ED reconfiguration at Chorley has been a long-running operational story.",
        "beneficiaries": "c. 1.5m residents across central Lancashire + tertiary referrals — major trauma, neurosciences, transplant + plastics/burns at Royal Preston.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£40.42M"},
            {"label": "Estate scale", "value": "2 hospital sites — Royal Preston + Chorley & South Ribble"},
            {"label": "NHP cohort", "value": "Royal Preston confirmed NHP rebuild scheme"},
            {"label": "Hard FM model", "value": "In-house Estates with specialist sub-contracts (no acute PFI)"},
            {"label": "Tertiary tilt", "value": "Major trauma + neurosciences + transplant + burns drive higher utility load"},
            {"label": "Royal Preston fabric", "value": "1980s build · ageing MEP · backlog pressure"},
            {"label": "Net Zero", "value": "PSDS-funded heat decarbonisation · LED rollout"},
            {"label": "YoY change", "value": "c. +6-8% (energy reset + ageing tower MEP)"},
            {"label": "Group context", "value": "Lancashire and South Cumbria ICS"}
        ],
        "notes": "LTH's premises spend is shaped by Royal Preston's 1980s tower (ageing MEP, ward fabric backlog) and the higher utility load of major trauma + tertiary specialty estate. Royal Preston's NHP rebuild is in pre-construction phases. Chorley ED reconfiguration drives ongoing temporary works. RM6011 energy reset and 5-7% hard-FM inflation drive the 2024-25 uplift.",
        "sources": [
            {"publisher": "Lancashire Teaching Hospitals NHS Foundation Trust", "title": "Annual report and accounts", "url": "https://www.lancsteachinghospitals.nhs.uk/about-us/our-publications"},
            {"publisher": "NHS England", "title": "New Hospital Programme — Royal Preston", "url": "https://www.england.nhs.uk/new-hospital-programme/"},
            {"publisher": "Salix Finance", "title": "Public Sector Decarbonisation Scheme", "url": "https://www.salixfinance.co.uk/PSDS"}
        ],
        "related": ["Lancashire Teaching Hospitals NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "General supplies & services — Gloucestershire Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "Gloucestershire Hospitals NHS Foundation Trust"}],
        "description": "Non-clinical general consumables and supplies across GHFT's two-site Gloucestershire estate — Gloucestershire Royal (Gloucester) and Cheltenham General (with the regional cancer centre and oncology day-case unit). Spend covers stationery, uniforms, housekeeping non-clinical, catering provisions and office consumables.",
        "beneficiaries": "c. 700,000 residents across Gloucestershire + tertiary cancer referrals — district acute at Gloucester Royal, oncology + cardiac at Cheltenham.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · Public Contracts Regulations 2015 / Procurement Act 2023 · NHS Supply Chain framework",
        "key_stats": [
            {"label": "General supplies & services 2024-25", "value": "£39.81M"},
            {"label": "Coverage", "value": "Office consumables · stationery · printing · uniforms · housekeeping · catering provisions"},
            {"label": "Estate scale", "value": "2 acute hospitals + community/clinic estate"},
            {"label": "Procurement framework", "value": "NHS Supply Chain · NHS Shared Business Services · CCS"},
            {"label": "Cancer centre", "value": "Cheltenham Oncology Centre — regional referrals lift consumables"},
            {"label": "Site reconfiguration", "value": "Long-running One Place programme · service splits between Gloucester + Cheltenham"},
            {"label": "Group context", "value": "Gloucestershire ICS"},
            {"label": "YoY change", "value": "c. +4-6% (consumables inflation)"}
        ],
        "notes": "GHFT's general-supplies line covers non-clinical consumables across the two-site Gloucestershire estate, with the long-running One Place reconfiguration (allocating services between Gloucester and Cheltenham) creating duplicated supply lines and modest inefficiency. Cheltenham's regional cancer centre lifts oncology day-case consumables. NHS Supply Chain volume uplifts plus consumables inflation drive the 2024-25 charge.",
        "sources": [
            {"publisher": "Gloucestershire Hospitals NHS Foundation Trust", "title": "Annual report and accounts", "url": "https://www.gloshospitals.nhs.uk/about-us/board-and-governance/annual-reports/"},
            {"publisher": "NHS Supply Chain", "title": "About NHS Supply Chain", "url": "https://www.supplychain.nhs.uk/"},
            {"publisher": "NHS England", "title": "Provider financial accounts", "url": "https://www.england.nhs.uk/financial-accounts/"}
        ],
        "related": ["Gloucestershire Hospitals NHS Foundation Trust", "Clinical Supplies & Drugs"]
    },
    "Premises (other) — Royal Berkshire NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Royal Berkshire NHS Foundation Trust"}],
        "description": "Premises running costs across RBFT's Reading-centred estate — Royal Berkshire Hospital (the central-Reading Victorian-core acute, partially Grade II listed and a confirmed New Hospital Programme rebuild scheme), Prince Charles Eye Unit (Windsor), West Berkshire Community Hospital (Newbury) and Townlands Memorial Hospital (Henley). The constrained Reading site and listed fabric drive cost.",
        "beneficiaries": "c. 600,000 residents across Reading, West Berkshire and South Oxfordshire — district acute, ED + maternity at Royal Berkshire.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15 · Listed Buildings and Conservation Areas Act 1990",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£38.15M"},
            {"label": "Estate scale", "value": "Royal Berkshire (Reading) + community estate (Windsor, Newbury, Henley)"},
            {"label": "Listed fabric", "value": "Royal Berkshire 1839 Greek-Revival core Grade II listed"},
            {"label": "NHP cohort", "value": "Royal Berkshire Hospital confirmed in NHP rebuild programme"},
            {"label": "Site constraint", "value": "Reading central site · land-locked · severe decant constraints"},
            {"label": "Hard FM model", "value": "In-house Estates with specialist sub-contracts (no acute PFI)"},
            {"label": "Net Zero", "value": "PSDS-funded heat decarbonisation · LED rollout"},
            {"label": "YoY change", "value": "c. +6-8% (energy reset + listed-fabric maintenance)"},
            {"label": "Group context", "value": "Buckinghamshire, Oxfordshire and Berkshire West ICS"}
        ],
        "notes": "RBFT's premises spend is structurally lifted by the Grade II listed 1839 Greek-Revival core and the constrained land-locked central-Reading site, which limits decant options and forces in-situ refurbishment of ageing fabric. The NHP rebuild scheme is in pre-construction. RM6011 energy reset and 5-7% hard-FM inflation drive the 2024-25 uplift on top of listed-fabric maintenance.",
        "sources": [
            {"publisher": "Royal Berkshire NHS Foundation Trust", "title": "Annual report and accounts", "url": "https://www.royalberkshire.nhs.uk/about-us/publications/"},
            {"publisher": "NHS England", "title": "New Hospital Programme — Royal Berkshire", "url": "https://www.england.nhs.uk/new-hospital-programme/"},
            {"publisher": "Historic England", "title": "Royal Berkshire Hospital list entry", "url": "https://historicengland.org.uk/listing/the-list/"}
        ],
        "related": ["Royal Berkshire NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "General supplies & services — Royal Free London NHS Foundation Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "Royal Free London NHS Foundation Trust"}],
        "description": "Non-clinical general consumables and supplies across Royal Free London's three-site estate — Royal Free Hospital (with the HCID high-level isolation unit, regional liver/HPB transplant and amyloidosis services), Barnet Hospital (PFI-managed catering/non-clinical scope) and Chase Farm Hospital. Group structure with North Mid + West Herts under Royal Free London Group.",
        "beneficiaries": "c. 1.6m residents across north London + tertiary referrals — HCID isolation, transplant, amyloidosis at Royal Free; district at Barnet; elective at Chase Farm.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · Public Contracts Regulations 2015 / Procurement Act 2023 · NHS Supply Chain framework",
        "key_stats": [
            {"label": "General supplies & services 2024-25", "value": "£37.77M"},
            {"label": "Coverage", "value": "Office consumables · stationery · printing · uniforms · housekeeping · catering provisions"},
            {"label": "HCID overhead", "value": "PPE + isolation consumables uplift versus standard acute"},
            {"label": "PFI carve-out", "value": "Barnet PFI scope sits in PFI line · in-house at Royal Free + Chase Farm"},
            {"label": "Procurement framework", "value": "NHS Supply Chain · NHS Shared Business Services · CCS"},
            {"label": "London weighting", "value": "Inner London supply pricing premium"},
            {"label": "Group context", "value": "North Central London ICS · Royal Free London Group"},
            {"label": "YoY change", "value": "c. +4-6% (consumables inflation + group ramp)"}
        ],
        "notes": "Royal Free London's general-supplies line is shaped by the HCID isolation unit (PPE and isolation consumables run at higher levels than peer acutes) and the in-house housekeeping/catering at Royal Free + Chase Farm (Barnet's PFI scope sits in the separate PFI line). Group consolidation efficiencies are still being realised. NHS Supply Chain volume uplifts plus consumables inflation drive the 2024-25 charge.",
        "sources": [
            {"publisher": "Royal Free London NHS Foundation Trust", "title": "Annual report and accounts", "url": "https://www.royalfree.nhs.uk/about-us/corporate-information-and-publications/"},
            {"publisher": "NHS Supply Chain", "title": "About NHS Supply Chain", "url": "https://www.supplychain.nhs.uk/"},
            {"publisher": "UK Health Security Agency", "title": "High consequence infectious diseases", "url": "https://www.gov.uk/guidance/high-consequence-infectious-diseases-hcid"}
        ],
        "related": ["Royal Free London NHS Foundation Trust", "Clinical Supplies & Drugs"]
    },
    "PFI / LIFT charges — Mersey and West Lancashire Teaching Hospitals NHS Trust": {
        "aliases": [{"name": "PFI / LIFT charges", "parent": "Mersey and West Lancashire Teaching Hospitals NHS Trust"}],
        "description": "PFI unitary-payment charges on MWL's PFI estate — most materially the 2011 Whiston Hospital PFI (Prescot, the consolidated St Helens & Knowsley acute, replacing the old 1970s site) and the Newton Community PFI element. The trust formed in 2023 from the merger of St Helens and Knowsley + Southport and Ormskirk, inheriting two PFI footprints.",
        "beneficiaries": "Patients across St Helens, Knowsley, Southport, Formby and West Lancashire — major emergency at Whiston, district at Southport.",
        "legal_basis": "IFRIC 12 (PFI) · IFRS 16 · NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · individual PFI Project Agreements",
        "key_stats": [
            {"label": "PFI / LIFT charges 2024-25", "value": "£35.78M"},
            {"label": "Major contract", "value": "Whiston Hospital — c. 2008 close · operations from 2010-2011 · Taylor Woodrow/Innisfree-equivalent SPV"},
            {"label": "Newton Community", "value": "Smaller PFI scheme included in MWL footprint"},
            {"label": "Concession term", "value": "c. 30-year — Whiston expiry late 2030s"},
            {"label": "RPI exposure", "value": "Unitary payment partly RPI-linked — 2022-23 RPI peak feeds 2024-25"},
            {"label": "FM scope", "value": "Hard FM + lifecycle + availability deductions framework"},
            {"label": "Trust merger", "value": "Mersey and West Lancashire formed 2023 (St Helens & Knowsley + Southport & Ormskirk)"},
            {"label": "Group context", "value": "Cheshire & Merseyside ICS"}
        ],
        "notes": "MWL's PFI line is dominated by the Whiston Hospital concession — a c. 2010 PFI rebuild that consolidated emergency and acute services across St Helens & Knowsley. The 2023 trust merger absorbed the Southport & Ormskirk footprint (no major PFI). The 2022-23 RPI peak feeds through the unitary indexation in 2024-25; lifecycle and handback surveys are increasingly material.",
        "sources": [
            {"publisher": "Mersey and West Lancashire Teaching Hospitals NHS Trust", "title": "Annual report and accounts", "url": "https://www.merseywestlancs.nhs.uk/about/board/publications/"},
            {"publisher": "HM Treasury", "title": "PFI and PF2 projects 2018 summary data", "url": "https://www.gov.uk/government/publications/private-finance-initiative-and-private-finance-2-projects-2018-summary-data"},
            {"publisher": "NHS England", "title": "Provider financial accounts", "url": "https://www.england.nhs.uk/financial-accounts/"}
        ],
        "related": ["Mersey and West Lancashire Teaching Hospitals NHS Trust", "Premises & Infrastructure"]
    },
    "PFI / LIFT charges — Barts Health NHS Trust": {
        "aliases": [{"name": "PFI / LIFT charges", "parent": "Barts Health NHS Trust"}],
        "description": "PFI unitary-payment charges on Barts Health's c. £1bn 2010s 'Capital City' PFI — the integrated Skanska/Capital Hospitals consortium contract covering The Royal London (Whitechapel) major-trauma rebuild and the St Bartholomew's specialist cardiothoracic + cancer centre redevelopment. One of the largest single NHS PFI deals.",
        "beneficiaries": "Patients across north-east London + tertiary cardiothoracic + cancer referrals — major trauma at the Royal London (with the air-ambulance helipad), specialist cardiac at Barts.",
        "legal_basis": "IFRIC 12 (PFI) · IFRS 16 · NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · Project Agreement (Capital Hospitals consortium)",
        "key_stats": [
            {"label": "PFI / LIFT charges 2024-25", "value": "£34.54M"},
            {"label": "Major contract", "value": "Royal London + Barts integrated PFI · Skanska-led Capital Hospitals · c. £1bn capital"},
            {"label": "Concession start", "value": "Financial close 2006 · Royal London tower opened 2012"},
            {"label": "Concession term", "value": "c. 35-year — expiry early 2040s"},
            {"label": "RPI exposure", "value": "Unitary payment partly RPI-linked — 2022-23 RPI peak feeds 2024-25"},
            {"label": "FM scope", "value": "Hard FM + lifecycle + availability deductions"},
            {"label": "Refinancing", "value": "Capital Hospitals refinanced post-financial-crisis"},
            {"label": "NHP cohort", "value": "Whipps Cross (separate from PFI) confirmed NHP rebuild"},
            {"label": "Group context", "value": "North East London ICS"}
        ],
        "notes": "Barts Health's PFI line covers the c. £1bn integrated Capital Hospitals concession at Royal London (major-trauma tower) and St Bartholomew's (specialist cardiothoracic + cancer). With c. 2040s expiry, this is one of the longest-dated NHS PFI envelopes. The 2022-23 RPI peak feeds through 2024-25 indexation; refinancing has previously reset the cost profile but RPI exposure remains the principal driver.",
        "sources": [
            {"publisher": "Barts Health NHS Trust", "title": "Annual report and accounts", "url": "https://www.bartshealth.nhs.uk/our-performance"},
            {"publisher": "HM Treasury", "title": "PFI and PF2 projects 2018 summary data", "url": "https://www.gov.uk/government/publications/private-finance-initiative-and-private-finance-2-projects-2018-summary-data"},
            {"publisher": "NHS England", "title": "Provider financial accounts", "url": "https://www.england.nhs.uk/financial-accounts/"}
        ],
        "related": ["Barts Health NHS Trust", "Premises & Infrastructure"]
    },
    "Impairments net of reversals — Mid Cheshire Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Impairments net of reversals", "parent": "Mid Cheshire Hospitals NHS Foundation Trust"}],
        "description": "Non-cash IFRS impairment charges on Mid Cheshire's estate — driven by Leighton Hospital (Crewe), one of the most acutely RAAC-affected hospitals in England (1970s build with widespread RAAC plank construction) and a confirmed New Hospital Programme priority rebuild scheme. Impairments capture the gap between MEA and DRC on RAAC-compromised buildings.",
        "beneficiaries": "Patients across south Cheshire (c. 450,000 catchment) — emergency, maternity and elective at Leighton plus community sites at Victoria Infirmary (Northwich) and Elmhurst (Winsford).",
        "legal_basis": "IAS 36 Impairment of Assets · IFRS / FReM (HM Treasury) · NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code",
        "key_stats": [
            {"label": "Impairments 2024-25", "value": "£33.90M"},
            {"label": "Driver", "value": "RAAC-compromised Leighton Hospital — MEA write-down to DRC"},
            {"label": "RAAC exposure", "value": "Confirmed widespread RAAC plank construction at Leighton"},
            {"label": "NHP cohort", "value": "Leighton — confirmed priority RAAC rebuild scheme (NHP Cohort 1)"},
            {"label": "Estate", "value": "Leighton (Crewe) + Victoria Infirmary (Northwich) + Elmhurst (Winsford)"},
            {"label": "Accounting", "value": "Non-cash · valuation movement only · no PDC/cash impact"},
            {"label": "Valuation cycle", "value": "Quinquennial revaluation + interim desktop · DV/Cushman valuer"},
            {"label": "Group context", "value": "Cheshire and Merseyside ICS"}
        ],
        "notes": "Mid Cheshire's impairment charge is structurally driven by the Leighton RAAC tower — one of the most acute RAAC cases nationally and a confirmed NHP Cohort 1 priority rebuild. Each revaluation cycle widens the gap between MEA and DRC as RAAC mitigation continues. This is a non-cash charge with no cash or PDC implication, but it is the largest single line in the trust's premises totals.",
        "sources": [
            {"publisher": "Mid Cheshire Hospitals NHS Foundation Trust", "title": "Annual report and accounts", "url": "https://www.mcht.nhs.uk/about-us/our-publications"},
            {"publisher": "NHS England", "title": "New Hospital Programme — RAAC schemes", "url": "https://www.england.nhs.uk/new-hospital-programme/"},
            {"publisher": "DHSC", "title": "RAAC in NHS estate", "url": "https://www.gov.uk/government/publications/raac-in-the-nhs-estate"}
        ],
        "related": ["Mid Cheshire Hospitals NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — Kingston Hospital NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Kingston Hospital NHS Foundation Trust"}],
        "description": "Premises running costs at Kingston Hospital (Galsworthy Road, Kingston upon Thames) — a south-west London district acute with major obstetrics + paediatrics + ED. Operating in a group structure with Hounslow & Richmond Community Healthcare from 2024 (Kingston and Richmond NHS Foundation Trust), broadening the operating estate.",
        "beneficiaries": "c. 350,000 residents across Kingston, Richmond, Merton and parts of Surrey — district acute, ED, regional maternity at Kingston.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£32.75M"},
            {"label": "Estate scale", "value": "Kingston Hospital + (from 2024) Hounslow & Richmond community estate"},
            {"label": "Hard FM model", "value": "In-house Estates with specialist sub-contracts (no acute PFI)"},
            {"label": "Site fabric", "value": "Mixed 1970s tower + 2010s maternity/Sir William Rous Unit"},
            {"label": "Group merger", "value": "Kingston and Richmond NHS Foundation Trust formed 2024 — community estate added"},
            {"label": "Net Zero", "value": "PSDS-funded heat decarbonisation · LED rollout"},
            {"label": "London weighting", "value": "Outer London supply pricing premium"},
            {"label": "YoY change", "value": "c. +6-8% (energy reset + group integration)"},
            {"label": "Group context", "value": "South West London ICS"}
        ],
        "notes": "Kingston's premises spend is shaped by the mixed-vintage Galsworthy Road site (1970s tower with newer maternity/oncology blocks) and the 2024 group merger that brought Hounslow & Richmond community estate into scope, expanding the operating premises footprint. RM6011 energy reset and 5-7% hard-FM inflation drive the 2024-25 uplift; group integration adds modest one-off cost.",
        "sources": [
            {"publisher": "Kingston Hospital NHS Foundation Trust", "title": "Annual report and accounts", "url": "https://kingstonhospital.nhs.uk/about-us/publications/"},
            {"publisher": "NHS England", "title": "Provider financial accounts", "url": "https://www.england.nhs.uk/financial-accounts/"},
            {"publisher": "Salix Finance", "title": "Public Sector Decarbonisation Scheme", "url": "https://www.salixfinance.co.uk/PSDS"}
        ],
        "related": ["Kingston Hospital NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Impairments net of reversals — University Hospitals Dorset NHS Foundation Trust": {
        "aliases": [{"name": "Impairments net of reversals", "parent": "University Hospitals Dorset NHS Foundation Trust"}],
        "description": "Non-cash IFRS impairment charges on UHD's three-site estate — driven by valuation movements during the live BEACH (Bournemouth Emergency Acute Care Hospital) reconfiguration that consolidates emergency at Royal Bournemouth and elective at Poole. Major capital build-in-progress is creating significant valuation re-bases as services migrate.",
        "beneficiaries": "Patients across BCP conurbation — Royal Bournemouth (emergency hub post-BEACH), Poole (elective hub), Christchurch (community/rehab).",
        "legal_basis": "IAS 36 Impairment of Assets · IFRS / FReM (HM Treasury) · NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Impairments 2024-25", "value": "£31.91M"},
            {"label": "Driver", "value": "BEACH reconfiguration capital · MEA-DRC valuation gap on new builds"},
            {"label": "BEACH programme", "value": "£250M+ acute reconfiguration · hot/cold split between Bournemouth + Poole"},
            {"label": "Estate", "value": "Royal Bournemouth + Poole + Christchurch"},
            {"label": "Accounting", "value": "Non-cash · valuation movement only · no PDC/cash impact"},
            {"label": "Valuation cycle", "value": "Quinquennial revaluation + interim desktop"},
            {"label": "Service migration", "value": "ED, ITU, maternity moving between sites"},
            {"label": "Group context", "value": "Dorset ICS"}
        ],
        "notes": "UHD's impairment charge reflects valuation movements during the live BEACH reconfiguration — significant new-build capital creates an MEA-DRC gap as buildings are constructed and brought into operational use. This is a non-cash charge with no cash or PDC implication. Each phase of BEACH delivery in 2024-26 will continue to generate valuation movements through impairments.",
        "sources": [
            {"publisher": "University Hospitals Dorset NHS Foundation Trust", "title": "Annual report and accounts", "url": "https://www.uhd.nhs.uk/about/publications/"},
            {"publisher": "University Hospitals Dorset NHS Foundation Trust", "title": "BEACH programme", "url": "https://www.uhd.nhs.uk/about/the-beach-programme/"},
            {"publisher": "NHS England", "title": "Provider financial accounts", "url": "https://www.england.nhs.uk/financial-accounts/"}
        ],
        "related": ["University Hospitals Dorset NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Impairments net of reversals — North West Anglia NHS Foundation Trust": {
        "aliases": [{"name": "Impairments net of reversals", "parent": "North West Anglia NHS Foundation Trust"}],
        "description": "Non-cash IFRS impairment charges on NWAFT's estate — driven by Hinchingbrooke Hospital (Huntingdon), confirmed RAAC-affected and a New Hospital Programme rebuild scheme, plus Peterborough City Hospital (the c. 2010 PFI tower) and Stamford & Rutland (rural community). Hinchingbrooke RAAC drives the MEA-DRC valuation gap.",
        "beneficiaries": "Patients across Cambridgeshire + Peterborough + Rutland — district acute at Hinchingbrooke + Peterborough City (PFI), community at Stamford.",
        "legal_basis": "IAS 36 Impairment of Assets · IFRS / FReM (HM Treasury) · NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Impairments 2024-25", "value": "£31.05M"},
            {"label": "Driver", "value": "Hinchingbrooke RAAC · MEA write-down to DRC"},
            {"label": "RAAC exposure", "value": "Hinchingbrooke confirmed widespread RAAC plank construction"},
            {"label": "NHP cohort", "value": "Hinchingbrooke — confirmed priority RAAC rebuild"},
            {"label": "Peterborough PFI", "value": "Peterborough City Hospital c. 2010 PFI (separate PFI line)"},
            {"label": "Estate", "value": "Hinchingbrooke + Peterborough City (PFI) + Stamford & Rutland"},
            {"label": "Accounting", "value": "Non-cash · valuation movement only · no PDC/cash impact"},
            {"label": "Group context", "value": "Cambridgeshire & Peterborough ICS"}
        ],
        "notes": "NWAFT's impairment charge is structurally driven by the Hinchingbrooke RAAC tower — a confirmed NHP priority rebuild — where each revaluation cycle widens the MEA-DRC gap as RAAC mitigation continues. Peterborough's PFI tower also contributes valuation movements. This is a non-cash charge with no cash or PDC implication.",
        "sources": [
            {"publisher": "North West Anglia NHS Foundation Trust", "title": "Annual report and accounts", "url": "https://www.nwangliaft.nhs.uk/about-us/publications/"},
            {"publisher": "NHS England", "title": "New Hospital Programme — RAAC schemes (Hinchingbrooke)", "url": "https://www.england.nhs.uk/new-hospital-programme/"},
            {"publisher": "DHSC", "title": "RAAC in NHS estate", "url": "https://www.gov.uk/government/publications/raac-in-the-nhs-estate"}
        ],
        "related": ["North West Anglia NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "PFI / LIFT charges — Buckinghamshire Healthcare NHS Trust": {
        "aliases": [{"name": "PFI / LIFT charges", "parent": "Buckinghamshire Healthcare NHS Trust"}],
        "description": "PFI unitary-payment charges on Buckinghamshire Healthcare's PFI estate — most materially the Stoke Mandeville Hospital developments (the regional spinal injuries centre, partially PFI-rebuilt) and the Wycombe Hospital PFI. The trust runs Stoke Mandeville (Aylesbury), Wycombe Hospital and Amersham Community.",
        "beneficiaries": "Patients across Buckinghamshire + national spinal injuries referrals — major spinal at Stoke Mandeville, district at Wycombe.",
        "legal_basis": "IFRIC 12 (PFI) · IFRS 16 · NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · individual PFI Project Agreements",
        "key_stats": [
            {"label": "PFI / LIFT charges 2024-25", "value": "£30.76M"},
            {"label": "Major contracts", "value": "Stoke Mandeville + Wycombe PFI schemes"},
            {"label": "Concession term", "value": "c. 30-year — expiry mid-to-late 2030s"},
            {"label": "RPI exposure", "value": "Unitary payment partly RPI-linked — 2022-23 RPI peak feeds 2024-25"},
            {"label": "FM scope", "value": "Hard FM + lifecycle + availability deductions framework"},
            {"label": "Stoke Mandeville", "value": "National Spinal Injuries Centre (post-Jimmy Savile inquiry estate review)"},
            {"label": "Wycombe", "value": "Cardiac PCI + minor injuries · PFI envelope"},
            {"label": "Group context", "value": "Buckinghamshire, Oxfordshire and Berkshire West ICS"}
        ],
        "notes": "Buckinghamshire Healthcare's PFI line covers the Stoke Mandeville and Wycombe concessions, with the 2022-23 RPI peak feeding through 2024-25 unitary indexation. The Stoke Mandeville National Spinal Injuries Centre carries specialist requirements (long-stay rehab, ventilation) that drive lifecycle costs. Concessions expire mid-to-late 2030s; handback condition surveys are starting to be material.",
        "sources": [
            {"publisher": "Buckinghamshire Healthcare NHS Trust", "title": "Annual report and accounts", "url": "https://www.buckshealthcare.nhs.uk/about-us/publications/"},
            {"publisher": "HM Treasury", "title": "PFI and PF2 projects 2018 summary data", "url": "https://www.gov.uk/government/publications/private-finance-initiative-and-private-finance-2-projects-2018-summary-data"},
            {"publisher": "NHS England", "title": "Provider financial accounts", "url": "https://www.england.nhs.uk/financial-accounts/"}
        ],
        "related": ["Buckinghamshire Healthcare NHS Trust", "Premises & Infrastructure"]
    },
    "Impairments net of reversals — University Hospitals Bristol and Weston NHS Foundation Trust": {
        "aliases": [{"name": "Impairments net of reversals", "parent": "University Hospitals Bristol and Weston NHS Foundation Trust"}],
        "description": "Non-cash IFRS impairment charges on UHBW's estate — driven by the Bristol Royal Infirmary tower (1970s acute, with structural fabric pressures), the Weston General coastal site (post-2020 merger, with confirmed coastal-corrosion fabric issues) and ongoing capital-investment valuation movements at the Bristol Heart Institute and BRHC paediatrics tower.",
        "beneficiaries": "Patients across Bristol, North Somerset + tertiary referrals — major emergency and tertiary at BRI, paediatrics at BRHC, district at Weston.",
        "legal_basis": "IAS 36 Impairment of Assets · IFRS / FReM (HM Treasury) · NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Impairments 2024-25", "value": "£30.34M"},
            {"label": "Driver", "value": "BRI tower + Weston coastal-corrosion fabric · MEA-DRC valuation gap"},
            {"label": "Estate", "value": "BRI + Bristol Heart Institute + BRHC + Weston General + South Bristol Community"},
            {"label": "Weston merger", "value": "2020 merger absorbed Weston General coastal site"},
            {"label": "Coastal corrosion", "value": "Weston General — North Somerset salt-air exposure"},
            {"label": "Accounting", "value": "Non-cash · valuation movement only · no PDC/cash impact"},
            {"label": "Valuation cycle", "value": "Quinquennial revaluation + interim desktop"},
            {"label": "Group context", "value": "Bristol, North Somerset and South Gloucestershire ICS"}
        ],
        "notes": "UHBW's impairment charge reflects valuation movements on the 1970s BRI tower (ageing fabric, ward-floor backlog) and the post-2020-merger Weston General estate (coastal corrosion driving fabric write-downs). Capital investment in the Bristol Heart Institute and BRHC paediatrics tower also contributes valuation re-bases. This is a non-cash charge with no cash or PDC implication.",
        "sources": [
            {"publisher": "University Hospitals Bristol and Weston NHS Foundation Trust", "title": "Annual report and accounts", "url": "https://www.uhbw.nhs.uk/about-us/our-publications"},
            {"publisher": "NHS England", "title": "Provider financial accounts", "url": "https://www.england.nhs.uk/financial-accounts/"},
            {"publisher": "DHSC", "title": "NHS estate condition reports", "url": "https://www.gov.uk/government/collections/nhs-estate-data"}
        ],
        "related": ["University Hospitals Bristol and Weston NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — University Hospitals Dorset NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "University Hospitals Dorset NHS Foundation Trust"}],
        "description": "Premises running costs across UHD's three-site BCP estate — Royal Bournemouth Hospital (the post-BEACH emergency hub, mid-major-build), Poole Hospital (the post-BEACH elective hub) and Christchurch Hospital (rehabilitation + community). The active BEACH reconfiguration is creating large decant + temporary works pressures alongside ageing fabric on both legacy acutes.",
        "beneficiaries": "c. 800,000 residents across BCP conurbation + east Dorset — emergency at Bournemouth (post-BEACH), elective at Poole, rehab at Christchurch.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£29.94M"},
            {"label": "Estate scale", "value": "3 hospital sites — Royal Bournemouth + Poole + Christchurch"},
            {"label": "BEACH programme", "value": "£250M+ reconfiguration · hot/cold split · live build"},
            {"label": "Hard FM model", "value": "In-house Estates with specialist sub-contracts (no acute PFI)"},
            {"label": "Decant works", "value": "Service migration between sites drives temporary-fabric spend"},
            {"label": "Coastal exposure", "value": "BCP coastal sites — modest salt-air exposure"},
            {"label": "Net Zero", "value": "PSDS-funded heat decarbonisation at Bournemouth + Poole"},
            {"label": "YoY change", "value": "c. +6-8% (BEACH decant + energy reset)"},
            {"label": "Group context", "value": "Dorset ICS · post-2020 Bournemouth + Poole merger"}
        ],
        "notes": "UHD's premises spend is shaped by the live BEACH reconfiguration — hot/cold split between Bournemouth and Poole — which drives substantial decant and temporary-fabric works on top of the operating run-rate. RM6011 energy reset and 5-7% hard-FM inflation lift the 2024-25 charge. Coastal salt-air exposure adds modestly. Christchurch's rehabilitation estate carries lower fabric load.",
        "sources": [
            {"publisher": "University Hospitals Dorset NHS Foundation Trust", "title": "Annual report and accounts", "url": "https://www.uhd.nhs.uk/about/publications/"},
            {"publisher": "University Hospitals Dorset NHS Foundation Trust", "title": "BEACH programme", "url": "https://www.uhd.nhs.uk/about/the-beach-programme/"},
            {"publisher": "Salix Finance", "title": "Public Sector Decarbonisation Scheme", "url": "https://www.salixfinance.co.uk/PSDS"}
        ],
        "related": ["University Hospitals Dorset NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "General supplies & services — University Hospital Southampton NHS Foundation Trust": {
        "aliases": [{"name": "General supplies & services", "parent": "University Hospital Southampton NHS Foundation Trust"}],
        "description": "Non-clinical general consumables and supplies across UHS's three-site Wessex teaching estate — Southampton General (major trauma + tertiary cardiac/neurosciences/paediatrics/burn unit), Princess Anne (women's + maternity) and Royal South Hants. Spend covers stationery, uniforms, housekeeping non-clinical, catering provisions and office consumables.",
        "beneficiaries": "c. 1.9m residents across central southern England + tertiary referrals — major trauma, regional cardiac/neuro/paeds/burns at SGH.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · Public Contracts Regulations 2015 / Procurement Act 2023 · NHS Supply Chain framework",
        "key_stats": [
            {"label": "General supplies & services 2024-25", "value": "£29.35M"},
            {"label": "Coverage", "value": "Office consumables · stationery · printing · uniforms · housekeeping · catering provisions"},
            {"label": "Major trauma overhead", "value": "Trauma-team consumables (non-clinical scope) at higher run-rate"},
            {"label": "Burn unit", "value": "Wessex Regional Burn Unit consumables overhead"},
            {"label": "Procurement framework", "value": "NHS Supply Chain · NHS Shared Business Services · CCS"},
            {"label": "BRC research tenant", "value": "Wessex BRC research consumables sit in this line"},
            {"label": "Group context", "value": "Hampshire and IoW ICS · AHSC with University of Southampton"},
            {"label": "YoY change", "value": "c. +4-6% (consumables inflation)"}
        ],
        "notes": "UHS's general-supplies line is shaped by the Wessex tertiary case-mix — major trauma, regional burns, cardiothoracic + neuro — which lifts non-clinical consumables (housekeeping, sterile supplies, uniforms) above district-acute peers. Wessex BRC research adds modest research-active consumables. NHS Supply Chain volume uplifts plus consumables inflation drive the 2024-25 charge.",
        "sources": [
            {"publisher": "University Hospital Southampton NHS Foundation Trust", "title": "Annual report and accounts", "url": "https://www.uhs.nhs.uk/about-us/who-we-are/annual-reports-and-publications/"},
            {"publisher": "NHS Supply Chain", "title": "About NHS Supply Chain", "url": "https://www.supplychain.nhs.uk/"},
            {"publisher": "NHS England", "title": "Provider financial accounts", "url": "https://www.england.nhs.uk/financial-accounts/"}
        ],
        "related": ["University Hospital Southampton NHS Foundation Trust", "Clinical Supplies & Drugs"]
    },
    "Impairments net of reversals — University Hospitals Sussex NHS Foundation Trust": {
        "aliases": [{"name": "Impairments net of reversals", "parent": "University Hospitals Sussex NHS Foundation Trust"}],
        "description": "Non-cash IFRS impairment charges on UHSussex's seven-site coastal estate — driven principally by the live 3Ts (Trauma, Teaching and Tertiary care) major rebuild at the Royal Sussex County Hospital (Stage 1 opened 2023, Stage 2 mid-build), where significant new-build capital is creating large MEA-DRC valuation movements. Coastal-corrosion fabric write-downs at Worthing and Chichester also contribute.",
        "beneficiaries": "Patients across coastal Sussex + tertiary referrals — major trauma at Royal Sussex, district acute at PRH/Worthing/St Richard's.",
        "legal_basis": "IAS 36 Impairment of Assets · IFRS / FReM (HM Treasury) · NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Impairments 2024-25", "value": "£164.05M"},
            {"label": "Driver", "value": "3Ts capital build · MEA-DRC valuation gap on Stage 1 + 2 new builds"},
            {"label": "3Ts programme", "value": "Royal Sussex County Hospital £760M+ rebuild · live multi-stage build"},
            {"label": "Coastal corrosion", "value": "Worthing + Chichester — salt-air fabric write-downs"},
            {"label": "Estate", "value": "7 hospital sites — coastal Sussex acute network"},
            {"label": "Listed fabric", "value": "Royal Sussex Barry Building Grade II*"},
            {"label": "Accounting", "value": "Non-cash · valuation movement only · no PDC/cash impact"},
            {"label": "Trust merger", "value": "Post-2021 Brighton/Sussex/Western Sussex merger"},
            {"label": "Group context", "value": "Sussex ICS"}
        ],
        "notes": "UHSussex's £164M impairment is one of the largest acute-trust charges in the slice — driven by the 3Ts major-rebuild capital crystallising as buildings open and MEA-DRC valuation gaps are recognised, plus coastal-corrosion write-downs at Worthing and Chichester. This is a non-cash charge but its scale makes it the dominant single line in the trust's premises totals. Each phase of 3Ts delivery in 2024-26 will continue to generate valuation movements.",
        "sources": [
            {"publisher": "University Hospitals Sussex NHS Foundation Trust", "title": "Annual report and accounts", "url": "https://www.uhsussex.nhs.uk/about-us/publications/"},
            {"publisher": "University Hospitals Sussex NHS Foundation Trust", "title": "3Ts Hospital Redevelopment Programme", "url": "https://www.uhsussex.nhs.uk/3ts/"},
            {"publisher": "NHS England", "title": "Provider financial accounts", "url": "https://www.england.nhs.uk/financial-accounts/"}
        ],
        "related": ["University Hospitals Sussex NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Social security & levy — Barts Health NHS Trust": {
        "aliases": [{"name": "Social security & levy", "parent": "Barts Health NHS Trust"}],
        "description": "Employer NIC + Apprenticeship Levy on Barts Health's c. 19,000-strong workforce — England's largest acute trust by income — across The Royal London (major trauma + air-ambulance), St Bartholomew's (specialist cardiothoracic + cancer), Whipps Cross, Newham and Mile End. London weighting plus tertiary case-mix drives a high NIable paybill.",
        "beneficiaries": "c. 19,000 staff with elevated Inner London weighting and tertiary consultant share.",
        "legal_basis": "Social Security Contributions and Benefits Act 1992 · Finance Act 2016 (Apprenticeship Levy) · NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Social security & levy 2024-25", "value": "£131.58M"},
            {"label": "Headcount", "value": "c. 19,000 (5-site east London acute group)"},
            {"label": "Employer NIC rate", "value": "13.8% (2024-25)"},
            {"label": "Apprenticeship Levy", "value": "0.5% of paybill"},
            {"label": "April 2025 step-up", "value": "15% NIC · £5,000 threshold"},
            {"label": "London weighting", "value": "Inner London HCAS · pushes NIable pay above national median"},
            {"label": "Pay drivers 2024-25", "value": "AfC 5.5% · medical 6%"},
            {"label": "Tertiary tilt", "value": "Major trauma + cardiothoracic + tertiary cancer raise consultant share"},
            {"label": "Group context", "value": "North East London ICS · trust under turnaround"}
        ],
        "notes": "Barts Health's social-security cost is among the largest in the NHS — 19,000 FTE on Inner London weighting with a strong tertiary tilt at Royal London (major trauma) and St Bartholomew's (cardiothoracic + cancer). The 2024-25 paybill is lifted by AfC 5.5% and medical 6%; April 2025 NIC step-up to 15% with £5,000 threshold compounds materially. Industrial-action backfill at premium rates remains a drag.",
        "sources": [
            {"publisher": "Barts Health NHS Trust", "title": "Annual report and accounts", "url": "https://www.bartshealth.nhs.uk/our-performance"},
            {"publisher": "HMRC", "title": "Rates and thresholds for employers 2024 to 2025", "url": "https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2024-to-2025"},
            {"publisher": "NHS Employers", "title": "Pay and Conditions Circulars", "url": "https://www.nhsemployers.org/publications/pay-and-conditions-circulars"}
        ],
        "related": ["Barts Health NHS Trust", "Staff Costs"]
    },
    "Impairments net of reversals — St George's University Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Impairments net of reversals", "parent": "St George's University Hospitals NHS Foundation Trust"}],
        "description": "Non-cash IFRS impairment charges on St George's Tooting estate — driven by ageing 1970s tower fabric (the principal Tooting building, with persistent backlog and structural-services pressures), HCID-isolation infrastructure write-downs and the GESH (St George's, Epsom and St Helier) group structure from 2023 which has prompted estate revaluations.",
        "beneficiaries": "Patients across south-west London + tertiary referrals — major trauma, HCID isolation, regional cardiac, plus group services across Epsom + St Helier under GESH.",
        "legal_basis": "IAS 36 Impairment of Assets · IFRS / FReM (HM Treasury) · NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Impairments 2024-25", "value": "£115.86M"},
            {"label": "Driver", "value": "1970s Tooting tower fabric · MEA-DRC valuation gap"},
            {"label": "Estate", "value": "St George's Tooting + linked sites under GESH from 2023"},
            {"label": "Tertiary tilt", "value": "Major trauma + HCID + regional cardiac infrastructure"},
            {"label": "Accounting", "value": "Non-cash · valuation movement only · no PDC/cash impact"},
            {"label": "Valuation cycle", "value": "Quinquennial revaluation + interim desktop"},
            {"label": "Group structure", "value": "GESH group with Epsom & St Helier from 2023 prompted estate review"},
            {"label": "Group context", "value": "South West London ICS"}
        ],
        "notes": "St George's £116M impairment is structurally driven by the 1970s Tooting tower (one of the largest single hospital buildings in the country, with persistent backlog and an ageing MEP/structural envelope) and by valuation re-bases prompted by the 2023 GESH group with Epsom & St Helier. This is a non-cash charge with no cash or PDC implication, but its scale makes it dominant in the trust's premises totals.",
        "sources": [
            {"publisher": "St George's, Epsom and St Helier University Hospitals and Health Group", "title": "Annual reports and publications", "url": "https://www.stgeorges.nhs.uk/about/publications/"},
            {"publisher": "NHS England", "title": "Provider financial accounts", "url": "https://www.england.nhs.uk/financial-accounts/"},
            {"publisher": "DHSC", "title": "NHS estate condition reports", "url": "https://www.gov.uk/government/collections/nhs-estate-data"}
        ],
        "related": ["St George's University Hospitals NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Social security & levy — King’s College Hospital NHS Foundation Trust": {
        "aliases": [{"name": "Social security & levy", "parent": "King’s College Hospital NHS Foundation Trust"}],
        "description": "Employer NIC + Apprenticeship Levy on King's c. 14,000-strong workforce across Denmark Hill (the major trauma + tertiary liver/HPB/neurosciences anchor) and the Princess Royal University Hospital (Farnborough/Orpington) — anchored by the AHSC partnership with King's College London and the King's Health Partners group.",
        "beneficiaries": "c. 14,000 staff with elevated Inner London weighting and tertiary research-active consultant share.",
        "legal_basis": "Social Security Contributions and Benefits Act 1992 · Finance Act 2016 (Apprenticeship Levy) · NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Social security & levy 2024-25", "value": "£96.31M"},
            {"label": "Headcount", "value": "c. 14,000 (2-site teaching trust)"},
            {"label": "Employer NIC rate", "value": "13.8% (2024-25)"},
            {"label": "Apprenticeship Levy", "value": "0.5% of paybill"},
            {"label": "April 2025 step-up", "value": "15% NIC · £5,000 threshold"},
            {"label": "London weighting", "value": "Inner London HCAS at Denmark Hill"},
            {"label": "Pay drivers 2024-25", "value": "AfC 5.5% · medical 6%"},
            {"label": "Tertiary tilt", "value": "Major trauma + liver transplant + neurosciences raise consultant share"},
            {"label": "Group context", "value": "South East London ICS · AHSC via King's Health Partners"}
        ],
        "notes": "King's social-security cost reflects a 14,000-strong workforce with Inner London weighting at Denmark Hill and a strong tertiary tilt (major trauma, liver transplant, neurosciences), plus a research-active senior staff base via King's Health Partners AHSC. The 2024-25 pay awards lift NIable pay; April 2025 NIC step-up to 15% with £5,000 threshold compounds employer on-cost in 2025-26.",
        "sources": [
            {"publisher": "King's College Hospital NHS Foundation Trust", "title": "Annual report and accounts", "url": "https://www.kch.nhs.uk/about/corporate/annual-reports"},
            {"publisher": "HMRC", "title": "Rates and thresholds for employers 2024 to 2025", "url": "https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2024-to-2025"},
            {"publisher": "NHS Employers", "title": "Pay and Conditions Circulars", "url": "https://www.nhsemployers.org/publications/pay-and-conditions-circulars"}
        ],
        "related": ["King’s College Hospital NHS Foundation Trust", "Staff Costs"]
    },
    "Social security & levy — The Leeds Teaching Hospitals NHS Trust": {
        "aliases": [{"name": "Social security & levy", "parent": "The Leeds Teaching Hospitals NHS Trust"}],
        "description": "Employer NIC + Apprenticeship Levy on LTHT's c. 18,000-strong workforce across Leeds General Infirmary (the major trauma centre and tertiary cardiac/neurosciences anchor) and St James's University Hospital ('Jimmy's' — the largest teaching hospital in Europe by floor area, with regional cancer + transplant). LGI is a confirmed New Hospital Programme rebuild scheme (Hospitals of the Future).",
        "beneficiaries": "c. 18,000 staff — major trauma, cardiac, neuro, transplant, oncology consultant teams plus AHSC research-active senior staff via University of Leeds.",
        "legal_basis": "Social Security Contributions and Benefits Act 1992 · Finance Act 2016 (Apprenticeship Levy) · NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Social security & levy 2024-25", "value": "£91.47M"},
            {"label": "Headcount", "value": "c. 18,000 (2-site largest single-trust teaching hospital)"},
            {"label": "Employer NIC rate", "value": "13.8% (2024-25)"},
            {"label": "Apprenticeship Levy", "value": "0.5% of paybill"},
            {"label": "April 2025 step-up", "value": "15% NIC · £5,000 threshold"},
            {"label": "Pay drivers 2024-25", "value": "AfC 5.5% · medical 6%"},
            {"label": "Tertiary tilt", "value": "Major trauma + transplant + tertiary cancer + neurosciences"},
            {"label": "NHP cohort", "value": "Hospitals of the Future (LGI rebuild) confirmed in NHP"},
            {"label": "Group context", "value": "West Yorkshire ICS · AHSC with University of Leeds"}
        ],
        "notes": "LTHT's social-security cost reflects an 18,000-strong workforce — one of the largest acute paybills outside London — with a strong tertiary tilt (major trauma, cancer, transplant) and AHSC research-active staff via the University of Leeds. The 2024-25 paybill is lifted by AfC 5.5% and medical 6%; April 2025 NIC step-up adds materially to the run-rate. The Hospitals of the Future programme is in pre-construction.",
        "sources": [
            {"publisher": "The Leeds Teaching Hospitals NHS Trust", "title": "Annual report and accounts", "url": "https://www.leedsth.nhs.uk/about-us/our-publications/"},
            {"publisher": "HMRC", "title": "Rates and thresholds for employers 2024 to 2025", "url": "https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2024-to-2025"},
            {"publisher": "NHS England", "title": "New Hospital Programme — Leeds", "url": "https://www.england.nhs.uk/new-hospital-programme/"}
        ],
        "related": ["The Leeds Teaching Hospitals NHS Trust", "Staff Costs"]
    },
    "Social security & levy — University Hospitals Sussex NHS Foundation Trust": {
        "aliases": [{"name": "Social security & levy", "parent": "University Hospitals Sussex NHS Foundation Trust"}],
        "description": "Employer NIC + Apprenticeship Levy on UHSussex's c. 17,500-strong workforce across the seven-hospital coastal-Sussex network — Royal Sussex County (Brighton, major trauma + tertiary), Princess Royal (Haywards Heath), Worthing, St Richard's (Chichester), Southlands, Sussex Cancer Centre. Trust formed via 2021 Brighton & Sussex / Western Sussex merger.",
        "beneficiaries": "c. 17,500 staff across coastal Sussex — major trauma + tertiary at Brighton, district acute at the network sites.",
        "legal_basis": "Social Security Contributions and Benefits Act 1992 · Finance Act 2016 (Apprenticeship Levy) · NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Social security & levy 2024-25", "value": "£89.49M"},
            {"label": "Headcount", "value": "c. 17,500 (7-site coastal Sussex network post-2021 merger)"},
            {"label": "Employer NIC rate", "value": "13.8% (2024-25)"},
            {"label": "Apprenticeship Levy", "value": "0.5% of paybill"},
            {"label": "April 2025 step-up", "value": "15% NIC · £5,000 threshold"},
            {"label": "Pay drivers 2024-25", "value": "AfC 5.5% · medical 6%"},
            {"label": "Tertiary tilt", "value": "Major trauma + Sussex Cancer Centre at Brighton raise consultant share"},
            {"label": "Geography premium", "value": "Coastal-Sussex multi-site network drives bank/agency cover"},
            {"label": "Group context", "value": "Sussex ICS · post-2021 Brighton/Sussex/Western Sussex merger"}
        ],
        "notes": "UHSussex's social-security cost reflects a 17,500-strong post-merger workforce across seven coastal sites, with the 2024-25 paybill lifted by AfC 5.5% and medical 6%. Multi-site geography drives premium-rate cover at smaller sites. April 2025 NIC step-up to 15% with £5,000 threshold compounds the run-rate; merger workforce-integration efficiencies are still being realised.",
        "sources": [
            {"publisher": "University Hospitals Sussex NHS Foundation Trust", "title": "Annual report and accounts", "url": "https://www.uhsussex.nhs.uk/about-us/publications/"},
            {"publisher": "HMRC", "title": "Rates and thresholds for employers 2024 to 2025", "url": "https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2024-to-2025"},
            {"publisher": "NHS Employers", "title": "Pay and Conditions Circulars", "url": "https://www.nhsemployers.org/publications/pay-and-conditions-circulars"}
        ],
        "related": ["University Hospitals Sussex NHS Foundation Trust", "Staff Costs"]
    },
    "Social security & levy — Royal Free London NHS Foundation Trust": {
        "aliases": [{"name": "Social security & levy", "parent": "Royal Free London NHS Foundation Trust"}],
        "description": "Employer NIC + Apprenticeship Levy on Royal Free London's c. 13,000-strong workforce across Royal Free Hospital (Hampstead — HCID isolation, liver transplant, amyloidosis), Barnet Hospital and Chase Farm. Group structure with North Mid + West Herts under Royal Free London Group (one of the early NHS group models).",
        "beneficiaries": "c. 13,000 staff with Inner London weighting at Hampstead and Outer London at Barnet/Chase Farm — HCID + tertiary specialist clinical workforce.",
        "legal_basis": "Social Security Contributions and Benefits Act 1992 · Finance Act 2016 (Apprenticeship Levy) · NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Social security & levy 2024-25", "value": "£88.17M"},
            {"label": "Headcount", "value": "c. 13,000 (3-site north London teaching trust)"},
            {"label": "Employer NIC rate", "value": "13.8% (2024-25)"},
            {"label": "Apprenticeship Levy", "value": "0.5% of paybill"},
            {"label": "April 2025 step-up", "value": "15% NIC · £5,000 threshold"},
            {"label": "London weighting", "value": "Inner London HCAS at Hampstead"},
            {"label": "Pay drivers 2024-25", "value": "AfC 5.5% · medical 6%"},
            {"label": "HCID specialism", "value": "High-level isolation unit consultant + nursing share"},
            {"label": "Group context", "value": "North Central London ICS · Royal Free London Group"}
        ],
        "notes": "Royal Free London's social-security cost reflects a 13,000-strong workforce with Inner London weighting at Hampstead and a distinctive HCID + transplant + amyloidosis tertiary tilt. The 2024-25 AfC + medical pay awards lift NIable pay; April 2025 NIC step-up to 15% with £5,000 threshold compounds the run-rate. Group integration with North Mid + West Herts is driving workforce-planning consolidation.",
        "sources": [
            {"publisher": "Royal Free London NHS Foundation Trust", "title": "Annual report and accounts", "url": "https://www.royalfree.nhs.uk/about-us/corporate-information-and-publications/"},
            {"publisher": "HMRC", "title": "Rates and thresholds for employers 2024 to 2025", "url": "https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2024-to-2025"},
            {"publisher": "NHS Employers", "title": "Pay and Conditions Circulars", "url": "https://www.nhsemployers.org/publications/pay-and-conditions-circulars"}
        ],
        "related": ["Royal Free London NHS Foundation Trust", "Staff Costs"]
    },
    "PFI / LIFT charges — Manchester University NHS Foundation Trust": {
        "aliases": [{"name": "PFI / LIFT charges", "parent": "Manchester University NHS Foundation Trust"}],
        "description": "PFI unitary-payment charges on MFT's Oxford Road campus PFI — the c. 2009 Catalyst Healthcare consortium that delivered the integrated rebuild of Manchester Royal Infirmary, Saint Mary's, Royal Manchester Children's Hospital, Manchester Royal Eye Hospital and the linked Eye + Dental teaching estate. One of the largest single integrated NHS PFI campuses.",
        "beneficiaries": "Patients across Greater Manchester + tertiary referrals — adult major acute (MRI), regional paediatrics (RMCH), regional eye (MREH), women's + maternity (Saint Mary's).",
        "legal_basis": "IFRIC 12 (PFI) · IFRS 16 · NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · Project Agreement (Catalyst Healthcare consortium)",
        "key_stats": [
            {"label": "PFI / LIFT charges 2024-25", "value": "£78.49M"},
            {"label": "Major contract", "value": "Oxford Road campus — Catalyst Healthcare consortium · c. 2004 close · operations from 2009"},
            {"label": "Buildings in scope", "value": "MRI + Saint Mary's + RMCH + MREH + Dental"},
            {"label": "Concession term", "value": "c. 35-year — expiry late 2030s/early 2040s"},
            {"label": "RPI exposure", "value": "Unitary payment partly RPI-linked — 2022-23 RPI peak feeds 2024-25"},
            {"label": "FM scope", "value": "Hard FM + lifecycle + availability deductions framework"},
            {"label": "NMGH carve-out", "value": "North Manchester General is outside this PFI · separate NHP rebuild scheme"},
            {"label": "Group context", "value": "GM ICS — lead provider"}
        ],
        "notes": "MFT's PFI line covers the integrated Oxford Road campus concession — one of the largest NHS PFI envelopes by capital value, delivering the central-Manchester teaching campus rebuild from 2009. The 2022-23 RPI peak feeds through 2024-25 indexation. With c. 2040 concession expiry approaching, lifecycle and handback condition surveys are starting to be material. North Manchester General sits outside this contract.",
        "sources": [
            {"publisher": "Manchester University NHS Foundation Trust", "title": "Annual report and accounts", "url": "https://mft.nhs.uk/the-trust/corporate-publications/"},
            {"publisher": "HM Treasury", "title": "PFI and PF2 projects 2018 summary data", "url": "https://www.gov.uk/government/publications/private-finance-initiative-and-private-finance-2-projects-2018-summary-data"},
            {"publisher": "NHS England", "title": "Provider financial accounts", "url": "https://www.england.nhs.uk/financial-accounts/"}
        ],
        "related": ["Manchester University NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Social security & levy — Liverpool University Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Social security & levy", "parent": "Liverpool University Hospitals NHS Foundation Trust"}],
        "description": "Employer NIC + Apprenticeship Levy on LUHFT's c. 13,500-strong workforce across the new Royal Liverpool University Hospital (the 2022-opened post-Carillion-collapse rebuild, with major trauma, regional renal/transplant and tertiary specialties), Aintree University Hospital (with major trauma) and Broadgreen Hospital (elective + outpatients). Trust formed via 2019 Royal Liverpool + Aintree merger.",
        "beneficiaries": "c. 13,500 staff across Merseyside acute network — major trauma + tertiary specialties at New Royal, district + trauma at Aintree.",
        "legal_basis": "Social Security Contributions and Benefits Act 1992 · Finance Act 2016 (Apprenticeship Levy) · NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Social security & levy 2024-25", "value": "£73.67M"},
            {"label": "Headcount", "value": "c. 13,500 (3-site post-2019 merger)"},
            {"label": "Employer NIC rate", "value": "13.8% (2024-25)"},
            {"label": "Apprenticeship Levy", "value": "0.5% of paybill"},
            {"label": "April 2025 step-up", "value": "15% NIC · £5,000 threshold"},
            {"label": "Pay drivers 2024-25", "value": "AfC 5.5% · medical 6%"},
            {"label": "Tertiary tilt", "value": "Major trauma + transplant + tertiary HCID-adjacent specialties"},
            {"label": "Carillion legacy", "value": "Post-2018 collapse delayed RLUH opening to 2022 · workforce stabilising"},
            {"label": "Group context", "value": "Cheshire & Merseyside ICS"}
        ],
        "notes": "LUHFT's social-security cost reflects a 13,500-strong post-2019-merger workforce with the new Royal Liverpool stabilising operations after the 2018 Carillion collapse and 2022 building opening. The 2024-25 paybill is lifted by AfC 5.5% and medical 6%; April 2025 NIC step-up adds materially. Industrial-action backfill and post-Carillion stabilisation premium remain drags.",
        "sources": [
            {"publisher": "Liverpool University Hospitals NHS Foundation Trust", "title": "Annual report and accounts", "url": "https://www.liverpoolft.nhs.uk/about-us/our-publications/"},
            {"publisher": "HMRC", "title": "Rates and thresholds for employers 2024 to 2025", "url": "https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2024-to-2025"},
            {"publisher": "NHS Employers", "title": "Pay and Conditions Circulars", "url": "https://www.nhsemployers.org/publications/pay-and-conditions-circulars"}
        ],
        "related": ["Liverpool University Hospitals NHS Foundation Trust", "Staff Costs"]
    },
    "Social security & levy — Cambridge University Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Social security & levy", "parent": "Cambridge University Hospitals NHS Foundation Trust"}],
        "description": "Employer NIC + Apprenticeship Levy on CUH's c. 12,000-strong Addenbrooke's + Rosie workforce — anchored by the AHSC partnership with the University of Cambridge and the Cambridge BRC. Tertiary case-mix (major trauma, transplant, neurosciences) plus heavy research-active senior staff drive a high NIable paybill.",
        "beneficiaries": "c. 12,000 staff with research-active senior FTE share lifted by Cambridge BRC and AHSC.",
        "legal_basis": "Social Security Contributions and Benefits Act 1992 · Finance Act 2016 (Apprenticeship Levy) · NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Social security & levy 2024-25", "value": "£70.96M"},
            {"label": "Headcount", "value": "c. 12,000 (Addenbrooke's + Rosie + Cambridge campus)"},
            {"label": "Employer NIC rate", "value": "13.8% (2024-25)"},
            {"label": "Apprenticeship Levy", "value": "0.5% of paybill"},
            {"label": "April 2025 step-up", "value": "15% NIC · £5,000 threshold"},
            {"label": "Pay drivers 2024-25", "value": "AfC 5.5% · medical 6%"},
            {"label": "Research tilt", "value": "Cambridge BRC + AHSC raise consultant + senior research-active share"},
            {"label": "Tertiary tilt", "value": "Major trauma + transplant + neurosciences raise consultant share"},
            {"label": "Group context", "value": "Cambridgeshire & Peterborough ICS · AHSC with University of Cambridge"}
        ],
        "notes": "CUH's social-security cost reflects a 12,000-strong workforce with a research-active and tertiary-tilted consultant share (Cambridge BRC, major trauma, transplant). The 2024-25 paybill is lifted by AfC 5.5% and medical 6%; April 2025 NIC step-up to 15% with £5,000 threshold adds materially. Cambridge Children's Hospital build is starting to drive additional workforce planning.",
        "sources": [
            {"publisher": "Cambridge University Hospitals NHS Foundation Trust", "title": "Annual report and accounts", "url": "https://www.cuh.nhs.uk/about-us/publications/"},
            {"publisher": "HMRC", "title": "Rates and thresholds for employers 2024 to 2025", "url": "https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2024-to-2025"},
            {"publisher": "NHS Employers", "title": "Pay and Conditions Circulars", "url": "https://www.nhsemployers.org/publications/pay-and-conditions-circulars"}
        ],
        "related": ["Cambridge University Hospitals NHS Foundation Trust", "Staff Costs"]
    },
    "Social security & levy — St George's University Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Social security & levy", "parent": "St George's University Hospitals NHS Foundation Trust"}],
        "description": "Employer NIC + Apprenticeship Levy on St George's c. 10,500-strong Tooting workforce — major trauma, regional cardiac/cardiothoracic, neurosciences, plus the HCID (High Consequence Infectious Diseases) network alongside Royal Free + NCH Liverpool. Now operating in the GESH (St George's, Epsom and St Helier) group from 2023.",
        "beneficiaries": "c. 10,500 staff with Inner London weighting and tertiary + HCID consultant + nursing share.",
        "legal_basis": "Social Security Contributions and Benefits Act 1992 · Finance Act 2016 (Apprenticeship Levy) · NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Social security & levy 2024-25", "value": "£66.09M"},
            {"label": "Headcount", "value": "c. 10,500 (Tooting + linked GESH sites)"},
            {"label": "Employer NIC rate", "value": "13.8% (2024-25)"},
            {"label": "Apprenticeship Levy", "value": "0.5% of paybill"},
            {"label": "April 2025 step-up", "value": "15% NIC · £5,000 threshold"},
            {"label": "London weighting", "value": "Inner London HCAS at Tooting"},
            {"label": "Pay drivers 2024-25", "value": "AfC 5.5% · medical 6%"},
            {"label": "HCID specialism", "value": "High-level isolation unit consultant + nursing share"},
            {"label": "Group context", "value": "South West London ICS · GESH group with Epsom & St Helier from 2023"}
        ],
        "notes": "St George's social-security cost reflects a 10,500-strong Tooting workforce with Inner London weighting, a tertiary major-trauma + cardiac tilt and the distinctive HCID isolation specialty. The 2024-25 pay awards lift NIable pay; April 2025 NIC step-up to 15% with £5,000 threshold compounds the run-rate. GESH group integration is driving workforce-planning consolidation.",
        "sources": [
            {"publisher": "St George's, Epsom and St Helier University Hospitals and Health Group", "title": "Annual reports and publications", "url": "https://www.stgeorges.nhs.uk/about/publications/"},
            {"publisher": "HMRC", "title": "Rates and thresholds for employers 2024 to 2025", "url": "https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2024-to-2025"},
            {"publisher": "NHS Employers", "title": "Pay and Conditions Circulars", "url": "https://www.nhsemployers.org/publications/pay-and-conditions-circulars"}
        ],
        "related": ["St George's University Hospitals NHS Foundation Trust", "Staff Costs"]
    },
    "Social security & levy — Somerset NHS Foundation Trust": {
        "aliases": [{"name": "Social security & levy", "parent": "Somerset NHS Foundation Trust"}],
        "description": "Employer NIC + Apprenticeship Levy on Somerset NHS FT's c. 11,500-strong vertically-integrated workforce — the unusual 'integrated provider' formed by the 2020 merger of Taunton & Somerset (acute) with Somerset Partnership (community + mental health) plus the 2023 Yeovil District Hospital merger. Workforce spans acute (Musgrove Park, Yeovil), community hospitals across Somerset and full mental-health services.",
        "beneficiaries": "c. 11,500 staff covering an unusually broad scope — acute, community, mental-health, learning disability + autism, plus paediatrics — all within a single trust.",
        "legal_basis": "Social Security Contributions and Benefits Act 1992 · Finance Act 2016 (Apprenticeship Levy) · NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Social security & levy 2024-25", "value": "£63.26M"},
            {"label": "Headcount", "value": "c. 11,500 (post-2020/2023 merger integrated provider)"},
            {"label": "Employer NIC rate", "value": "13.8% (2024-25)"},
            {"label": "Apprenticeship Levy", "value": "0.5% of paybill"},
            {"label": "April 2025 step-up", "value": "15% NIC · £5,000 threshold"},
            {"label": "Pay drivers 2024-25", "value": "AfC 5.5% · medical 6%"},
            {"label": "Integrated scope", "value": "Acute + community + MH + LD/autism + paediatrics in one trust"},
            {"label": "Yeovil merger", "value": "Yeovil District Hospital absorbed 2023"},
            {"label": "Group context", "value": "Somerset ICS — distinctive single-provider model"}
        ],
        "notes": "Somerset NHS FT's social-security cost is structurally distinctive because of the trust's integrated scope — acute, community and mental-health workforces all sit on a single paybill following the 2020 acute-community merger and the 2023 Yeovil acute merger. The 2024-25 AfC + medical pay awards lift NIable pay across all staff groups; April 2025 NIC step-up to 15% with £5,000 threshold compounds the run-rate.",
        "sources": [
            {"publisher": "Somerset NHS Foundation Trust", "title": "Annual report and accounts", "url": "https://www.somersetft.nhs.uk/about-us/our-publications/"},
            {"publisher": "HMRC", "title": "Rates and thresholds for employers 2024 to 2025", "url": "https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2024-to-2025"},
            {"publisher": "NHS Employers", "title": "Pay and Conditions Circulars", "url": "https://www.nhsemployers.org/publications/pay-and-conditions-circulars"}
        ],
        "related": ["Somerset NHS Foundation Trust", "Staff Costs"]
    },
    "Premises (other) — Imperial College Healthcare NHS Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Imperial College Healthcare NHS Trust"}],
        "description": "Premises running costs across ICHT's central/west London estate — St Mary's (Paddington, the major trauma centre and a confirmed New Hospital Programme priority rebuild scheme; ageing 1840s-onwards Victorian fabric), Charing Cross (Hammersmith — long-running reconfiguration story), Hammersmith Hospital (Du Cane Road; cardiac + renal tertiary), Queen Charlotte's & Chelsea (women's + neonatal) and Western Eye.",
        "beneficiaries": "c. 1.5m residents across central/west London + tertiary referrals — major trauma at St Mary's, cardiac/renal at Hammersmith, women's at Queen Charlotte's.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15 · Listed Buildings and Conservation Areas Act 1990",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£61.59M"},
            {"label": "Estate scale", "value": "5 hospital sites — St Mary's + Charing Cross + Hammersmith + QCCH + Western Eye"},
            {"label": "St Mary's NHP", "value": "Confirmed priority NHP rebuild · originally Cohort 1"},
            {"label": "Listed fabric", "value": "St Mary's Victorian core 1845-onwards · multiple listed buildings"},
            {"label": "Hard FM model", "value": "In-house Estates with specialist sub-contracts (no acute PFI)"},
            {"label": "Backlog pressure", "value": "St Mary's reported among highest backlog maintenance £/m² in NHS"},
            {"label": "Net Zero", "value": "PSDS-funded heat decarbonisation · LED rollout"},
            {"label": "YoY change", "value": "c. +6-9% (energy reset + St Mary's backlog)"},
            {"label": "Group context", "value": "NW London ICS · AHSC with Imperial College London"}
        ],
        "notes": "ICHT's premises spend is structurally elevated by St Mary's Victorian fabric (1845-onwards core, listed; reportedly among the highest backlog-maintenance burdens in the NHS) where the NHP rebuild is the long-term answer but operating maintenance continues to absorb spend. Hammersmith and Charing Cross also carry ageing 1970s fabric. RM6011 energy reset and 5-7% hard-FM inflation drive the 2024-25 uplift.",
        "sources": [
            {"publisher": "Imperial College Healthcare NHS Trust", "title": "Annual report and accounts", "url": "https://www.imperial.nhs.uk/about-us/our-publications"},
            {"publisher": "NHS England", "title": "New Hospital Programme — St Mary's", "url": "https://www.england.nhs.uk/new-hospital-programme/"},
            {"publisher": "Salix Finance", "title": "Public Sector Decarbonisation Scheme", "url": "https://www.salixfinance.co.uk/PSDS"}
        ],
        "related": ["Imperial College Healthcare NHS Trust", "Premises & Infrastructure"]
    },
    "Social security & levy — London North West University Healthcare NHS Trust": {
        "aliases": [{"name": "Social security & levy", "parent": "London North West University Healthcare NHS Trust"}],
        "description": "Employer NIC + Apprenticeship Levy on LNWH's c. 9,500-strong workforce across Northwick Park (Harrow — the major acute and ED), Ealing Hospital (Southall, with reduced services post-Shaping a Healthier Future), Central Middlesex Hospital and St Mark's Hospital (national bowel-disease specialty centre, relocated to Northwick Park). Trust formed via 2014 Ealing + North West London merger.",
        "beneficiaries": "c. 9,500 staff with Outer London weighting — district acute, regional bowel-disease tertiary at St Mark's.",
        "legal_basis": "Social Security Contributions and Benefits Act 1992 · Finance Act 2016 (Apprenticeship Levy) · NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Social security & levy 2024-25", "value": "£60.43M"},
            {"label": "Headcount", "value": "c. 9,500 (3-site north-west London acute network)"},
            {"label": "Employer NIC rate", "value": "13.8% (2024-25)"},
            {"label": "Apprenticeship Levy", "value": "0.5% of paybill"},
            {"label": "April 2025 step-up", "value": "15% NIC · £5,000 threshold"},
            {"label": "London weighting", "value": "Outer London HCAS"},
            {"label": "Pay drivers 2024-25", "value": "AfC 5.5% · medical 6%"},
            {"label": "Specialism", "value": "St Mark's national bowel-disease centre relocated to Northwick Park"},
            {"label": "Group context", "value": "NW London ICS"}
        ],
        "notes": "LNWH's social-security cost reflects a 9,500-strong post-2014-merger workforce on Outer London weighting, with a national bowel-disease specialty tilt via St Mark's. The 2024-25 paybill is lifted by AfC 5.5% and medical 6%; April 2025 NIC step-up to 15% with £5,000 threshold compounds the run-rate. Industrial-action backfill at premium rates remains a drag.",
        "sources": [
            {"publisher": "London North West University Healthcare NHS Trust", "title": "Annual report and accounts", "url": "https://www.lnwh.nhs.uk/about-us/publications-and-reports"},
            {"publisher": "HMRC", "title": "Rates and thresholds for employers 2024 to 2025", "url": "https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2024-to-2025"},
            {"publisher": "NHS Employers", "title": "Pay and Conditions Circulars", "url": "https://www.nhsemployers.org/publications/pay-and-conditions-circulars"}
        ],
        "related": ["London North West University Healthcare NHS Trust", "Staff Costs"]
    },
    "Premises (other) — Nottingham University Hospitals NHS Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Nottingham University Hospitals NHS Trust"}],
        "description": "Premises running costs across NUH's two-major-site estate — Queen's Medical Centre (the Adult major-trauma centre + Nottingham Children's Hospital + East Midlands stroke + neurosciences; the 1970s tower block) and Nottingham City Hospital (oncology + cardiac centre). Both sites are confirmed New Hospital Programme rebuild schemes (Tomorrow's NUH).",
        "beneficiaries": "c. 2.5m residents across Nottinghamshire + tertiary referrals — major trauma and paediatrics at QMC, oncology and cardiac at City.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£59.56M"},
            {"label": "Estate scale", "value": "QMC + Nottingham City Hospital + Ropewalk House"},
            {"label": "NHP cohort", "value": "Tomorrow's NUH — both QMC + City confirmed in NHP rebuild programme"},
            {"label": "QMC fabric", "value": "1970s tower · among Europe's largest hospital buildings · ageing MEP"},
            {"label": "Hard FM model", "value": "In-house Estates with specialist sub-contracts (no acute PFI)"},
            {"label": "Tertiary tilt", "value": "Major trauma + paediatrics + neurosciences + oncology raise utility load"},
            {"label": "Maternity inquiry", "value": "Ockenden / Donna Ockenden review live · estate investment for maternity"},
            {"label": "Net Zero", "value": "PSDS-funded heat decarbonisation · LED rollout"},
            {"label": "YoY change", "value": "c. +6-8% (1970s tower MEP + energy reset)"}
        ],
        "notes": "NUH's premises spend is dominated by the QMC 1970s tower (one of Europe's largest hospital buildings, with extensive ageing MEP and ward fabric backlog) and the City Hospital site, both confirmed in the Tomorrow's NUH NHP rebuild programme. The live Donna Ockenden maternity review is driving additional estate investment. RM6011 energy reset and 5-7% hard-FM inflation drive the 2024-25 uplift.",
        "sources": [
            {"publisher": "Nottingham University Hospitals NHS Trust", "title": "Annual report and accounts", "url": "https://www.nuh.nhs.uk/our-publications"},
            {"publisher": "NHS England", "title": "New Hospital Programme — Tomorrow's NUH", "url": "https://www.england.nhs.uk/new-hospital-programme/"},
            {"publisher": "Donna Ockenden", "title": "Independent review of NUH maternity services", "url": "https://www.ockendenmaternityreview.org.uk/"}
        ],
        "related": ["Nottingham University Hospitals NHS Trust", "Premises & Infrastructure"]
    },
    "Social security & levy — University Hospitals of North Midlands NHS Trust": {
        "aliases": [{"name": "Social security & levy", "parent": "University Hospitals of North Midlands NHS Trust"}],
        "description": "Employer NIC + Apprenticeship Levy on UHNM's c. 11,500-strong workforce across Royal Stoke University Hospital (the major trauma centre and tertiary anchor with PFI elements) and County Hospital Stafford (district acute, smaller site). Workforce on-cost reflects tertiary tilt at Royal Stoke plus dual-site rota duplication.",
        "beneficiaries": "c. 11,500 staff — major trauma + tertiary specialty consultants at Royal Stoke, district at Stafford.",
        "legal_basis": "Social Security Contributions and Benefits Act 1992 · Finance Act 2016 (Apprenticeship Levy) · NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Social security & levy 2024-25", "value": "£57.43M"},
            {"label": "Headcount", "value": "c. 11,500 (2-site major-trauma + district)"},
            {"label": "Employer NIC rate", "value": "13.8% (2024-25)"},
            {"label": "Apprenticeship Levy", "value": "0.5% of paybill"},
            {"label": "April 2025 step-up", "value": "15% NIC · £5,000 threshold"},
            {"label": "Pay drivers 2024-25", "value": "AfC 5.5% · medical 6%"},
            {"label": "Tertiary tilt", "value": "Royal Stoke major trauma + cardiothoracic + neurosciences raise consultant share"},
            {"label": "Two-site rota", "value": "Royal Stoke + Stafford rota duplication drives bank/agency cover"},
            {"label": "Group context", "value": "Staffordshire and Stoke ICS"}
        ],
        "notes": "UHNM's social-security cost reflects an 11,500-strong workforce with a tertiary tilt at Royal Stoke (major trauma, cardiothoracic, neurosciences) and dual-site rota cover for the smaller Stafford acute. The 2024-25 paybill is lifted by AfC 5.5% and medical 6%; April 2025 NIC step-up to 15% with £5,000 threshold adds materially to the run-rate.",
        "sources": [
            {"publisher": "University Hospitals of North Midlands NHS Trust", "title": "Annual report and accounts", "url": "https://www.uhnm.nhs.uk/about-us/publications/"},
            {"publisher": "HMRC", "title": "Rates and thresholds for employers 2024 to 2025", "url": "https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2024-to-2025"},
            {"publisher": "NHS Employers", "title": "Pay and Conditions Circulars", "url": "https://www.nhsemployers.org/publications/pay-and-conditions-circulars"}
        ],
        "related": ["University Hospitals of North Midlands NHS Trust", "Staff Costs"]
    },
    "Premises (other) — University Hospital Southampton NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "University Hospital Southampton NHS Foundation Trust"}],
        "description": "Premises running costs across UHS's three-site Wessex teaching estate — Southampton General (the major trauma centre + regional tertiary cardiothoracic, neurosciences, paediatric and Wessex Regional Burn Unit; mixed-vintage 1970s-onwards build), Princess Anne (women's + maternity) and Royal South Hants. Confirmed candidate for major estate investment under the NHP.",
        "beneficiaries": "c. 1.9m residents across central southern England + tertiary referrals — major trauma, regional cardiac/neuro/paeds/burns at SGH.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£54.48M"},
            {"label": "Estate scale", "value": "3 hospital sites — SGH + Princess Anne + Royal South Hants"},
            {"label": "Hard FM model", "value": "In-house Estates with specialist sub-contracts (no acute PFI)"},
            {"label": "Tertiary tilt", "value": "Major trauma + cardiothoracic + neuro + paeds + burns raise utility load"},
            {"label": "SGH fabric", "value": "1970s-onwards build · mixed-vintage MEP · backlog pressure"},
            {"label": "BRC tenant", "value": "Wessex BRC research infrastructure on SGH campus"},
            {"label": "Net Zero", "value": "PSDS-funded heat decarbonisation"},
            {"label": "YoY change", "value": "c. +6-8% (energy reset + ageing tower MEP)"},
            {"label": "Group context", "value": "Hampshire and IoW ICS · AHSC with University of Southampton"}
        ],
        "notes": "UHS's premises spend is shaped by the mixed-vintage SGH 1970s-onwards estate where major-trauma, cardiothoracic, paediatric and burn-unit infrastructure drives high utility load and lifecycle MEP costs. The Wessex BRC research presence adds research-active infrastructure spend. RM6011 energy reset and 5-7% hard-FM inflation drive the 2024-25 uplift.",
        "sources": [
            {"publisher": "University Hospital Southampton NHS Foundation Trust", "title": "Annual report and accounts", "url": "https://www.uhs.nhs.uk/about-us/who-we-are/annual-reports-and-publications/"},
            {"publisher": "NHS England", "title": "Provider financial accounts", "url": "https://www.england.nhs.uk/financial-accounts/"},
            {"publisher": "Salix Finance", "title": "Public Sector Decarbonisation Scheme", "url": "https://www.salixfinance.co.uk/PSDS"}
        ],
        "related": ["University Hospital Southampton NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Social security & levy — East Suffolk and North Essex NHS Foundation Trust": {
        "aliases": [{"name": "Social security & levy", "parent": "East Suffolk and North Essex NHS Foundation Trust"}],
        "description": "Employer NIC + Apprenticeship Levy on ESNEFT's c. 10,500-strong workforce across Ipswich Hospital and Colchester Hospital (the ESNE merger of 2018) plus Felixstowe Community, Bluebird Lodge and a wider community estate. Distinctive cross-border ICS footprint covering Suffolk + north Essex.",
        "beneficiaries": "c. 10,500 staff across an unusually wide rural geography — district acute consultants + nursing teams plus large community workforce.",
        "legal_basis": "Social Security Contributions and Benefits Act 1992 · Finance Act 2016 (Apprenticeship Levy) · NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Social security & levy 2024-25", "value": "£52.14M"},
            {"label": "Headcount", "value": "c. 10,500 (post-2018 merger acute + community)"},
            {"label": "Employer NIC rate", "value": "13.8% (2024-25)"},
            {"label": "Apprenticeship Levy", "value": "0.5% of paybill"},
            {"label": "April 2025 step-up", "value": "15% NIC · £5,000 threshold"},
            {"label": "Pay drivers 2024-25", "value": "AfC 5.5% · medical 6%"},
            {"label": "Geography premium", "value": "Suffolk-Essex rural network drives bank/agency cover"},
            {"label": "Community scope", "value": "Integrated community workforce TUPE'd in"},
            {"label": "Group context", "value": "Suffolk and North East Essex ICS — cross-county"}
        ],
        "notes": "ESNEFT's social-security cost reflects a 10,500-strong post-2018-merger workforce spanning two acute sites (Ipswich + Colchester) plus integrated community services across rural east Suffolk + north Essex. The 2024-25 paybill is lifted by AfC 5.5% and medical 6%; April 2025 NIC step-up to 15% with £5,000 threshold compounds the run-rate. Rural-site cover drives premium-rate spend.",
        "sources": [
            {"publisher": "East Suffolk and North Essex NHS Foundation Trust", "title": "Annual report and accounts", "url": "https://www.esneft.nhs.uk/about-us/publications/"},
            {"publisher": "HMRC", "title": "Rates and thresholds for employers 2024 to 2025", "url": "https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2024-to-2025"},
            {"publisher": "NHS Employers", "title": "Pay and Conditions Circulars", "url": "https://www.nhsemployers.org/publications/pay-and-conditions-circulars"}
        ],
        "related": ["East Suffolk and North Essex NHS Foundation Trust", "Staff Costs"]
    },
    "Premises (other) — Liverpool University Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Liverpool University Hospitals NHS Foundation Trust"}],
        "description": "Premises running costs across LUHFT's three-site Merseyside estate — the new Royal Liverpool University Hospital (the 2022-opened replacement after the 2018 Carillion collapse and rebuild stall, with major trauma and tertiary specialties), Aintree University Hospital (with major trauma + a 1990s-onwards estate) and Broadgreen Hospital (elective + outpatients). Trust formed via 2019 Royal Liverpool + Aintree merger.",
        "beneficiaries": "c. 1.5m residents across Merseyside + tertiary referrals — major trauma at New Royal + Aintree, elective at Broadgreen.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£50.34M"},
            {"label": "Estate scale", "value": "3 hospital sites — New Royal Liverpool + Aintree + Broadgreen"},
            {"label": "Carillion legacy", "value": "Old Royal demolition + new build snagging post-2022 opening"},
            {"label": "Hard FM model", "value": "In-house Estates with specialist sub-contracts (no acute PFI on new build)"},
            {"label": "Tertiary tilt", "value": "Major trauma + transplant + tertiary services raise utility load"},
            {"label": "Aintree fabric", "value": "1990s-onwards estate · ageing MEP backlog"},
            {"label": "Net Zero", "value": "PSDS-funded heat decarbonisation across non-new-build sites"},
            {"label": "YoY change", "value": "c. +5-8% (new build snagging + energy reset)"},
            {"label": "Group context", "value": "Cheshire & Merseyside ICS"}
        ],
        "notes": "LUHFT's premises spend covers the post-Carillion-collapse new Royal Liverpool (which opened 2022 — snagging and lifecycle issues continue) plus the older Aintree estate (1990s-onwards with ageing MEP) and Broadgreen elective. The legacy of the 2018 Carillion collapse and prolonged build delay continues to influence operating spend through transition costs. RM6011 energy reset and 5-7% hard-FM inflation drive the 2024-25 uplift.",
        "sources": [
            {"publisher": "Liverpool University Hospitals NHS Foundation Trust", "title": "Annual report and accounts", "url": "https://www.liverpoolft.nhs.uk/about-us/our-publications/"},
            {"publisher": "NHS England", "title": "Provider financial accounts", "url": "https://www.england.nhs.uk/financial-accounts/"},
            {"publisher": "Salix Finance", "title": "Public Sector Decarbonisation Scheme", "url": "https://www.salixfinance.co.uk/PSDS"}
        ],
        "related": ["Liverpool University Hospitals NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Social security & levy — North Bristol NHS Trust": {
        "aliases": [{"name": "Social security & levy", "parent": "North Bristol NHS Trust"}],
        "description": "Employer NIC + Apprenticeship Levy on NBT's c. 9,000-strong workforce at Southmead Hospital (Westbury-on-Trym; the 2014 PFI rebuild incorporating major trauma, regional neurosciences, plastic surgery + burns, renal transplant) plus Cossham Hospital and a community-MIU footprint. Workforce on-cost reflects tertiary case-mix concentrated at Southmead.",
        "beneficiaries": "c. 9,000 staff — major trauma + tertiary consultant teams at Southmead.",
        "legal_basis": "Social Security Contributions and Benefits Act 1992 · Finance Act 2016 (Apprenticeship Levy) · NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Social security & levy 2024-25", "value": "£49.84M"},
            {"label": "Headcount", "value": "c. 9,000 (Southmead-anchored teaching trust)"},
            {"label": "Employer NIC rate", "value": "13.8% (2024-25)"},
            {"label": "Apprenticeship Levy", "value": "0.5% of paybill"},
            {"label": "April 2025 step-up", "value": "15% NIC · £5,000 threshold"},
            {"label": "Pay drivers 2024-25", "value": "AfC 5.5% · medical 6%"},
            {"label": "Tertiary tilt", "value": "Major trauma + neurosciences + plastics/burns + renal transplant"},
            {"label": "Backfill drag", "value": "Industrial-action backfill at premium rates"},
            {"label": "Group context", "value": "BNSSG ICS · Bristol-area provider collaborative"}
        ],
        "notes": "NBT's social-security cost reflects a 9,000-strong workforce concentrated at the 2014-built Southmead PFI tower with a strong tertiary tilt (major trauma, neurosciences, transplant, burns). The 2024-25 paybill is lifted by AfC 5.5% and medical 6%; April 2025 NIC step-up to 15% with £5,000 threshold adds materially to the run-rate.",
        "sources": [
            {"publisher": "North Bristol NHS Trust", "title": "Annual report and accounts", "url": "https://www.nbt.nhs.uk/about-us/publications/"},
            {"publisher": "HMRC", "title": "Rates and thresholds for employers 2024 to 2025", "url": "https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2024-to-2025"},
            {"publisher": "NHS Employers", "title": "Pay and Conditions Circulars", "url": "https://www.nhsemployers.org/publications/pay-and-conditions-circulars"}
        ],
        "related": ["North Bristol NHS Trust", "Staff Costs"]
    },
    "Social security & levy — University Hospitals Plymouth NHS Trust": {
        "aliases": [{"name": "Social security & levy", "parent": "University Hospitals Plymouth NHS Trust"}],
        "description": "Employer NIC + Apprenticeship Levy on UHP's c. 9,500-strong workforce at Derriford Hospital (the major trauma centre and tertiary anchor for the South West Peninsula, serving patients across south Devon, north Devon, Cornwall + the Isles of Scilly) plus Royal Eye Infirmary and the Mount Gould community estate. South West Peninsula's geography drives recruitment + retention costs.",
        "beneficiaries": "c. 9,500 staff serving the South West Peninsula population — major trauma, regional cardiac/cancer/neurosciences at Derriford.",
        "legal_basis": "Social Security Contributions and Benefits Act 1992 · Finance Act 2016 (Apprenticeship Levy) · NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Social security & levy 2024-25", "value": "£48.04M"},
            {"label": "Headcount", "value": "c. 9,500 (Derriford-anchored peninsula tertiary)"},
            {"label": "Employer NIC rate", "value": "13.8% (2024-25)"},
            {"label": "Apprenticeship Levy", "value": "0.5% of paybill"},
            {"label": "April 2025 step-up", "value": "15% NIC · £5,000 threshold"},
            {"label": "Pay drivers 2024-25", "value": "AfC 5.5% · medical 6%"},
            {"label": "Tertiary tilt", "value": "Major trauma + cardiac + cancer + neurosciences raise consultant share"},
            {"label": "Geography premium", "value": "South West Peninsula isolation drives recruitment + retention costs"},
            {"label": "Group context", "value": "Devon ICS · partnership with Royal Devon"}
        ],
        "notes": "UHP's social-security cost reflects a 9,500-strong workforce concentrated at Derriford, with the South West Peninsula's geographic isolation lifting recruitment + retention costs (premium-rate locum reliance, especially for medical specialties). The 2024-25 paybill is lifted by AfC 5.5% and medical 6%; April 2025 NIC step-up to 15% with £5,000 threshold compounds the run-rate.",
        "sources": [
            {"publisher": "University Hospitals Plymouth NHS Trust", "title": "Annual report and accounts", "url": "https://www.plymouthhospitals.nhs.uk/about-us/publications/"},
            {"publisher": "HMRC", "title": "Rates and thresholds for employers 2024 to 2025", "url": "https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2024-to-2025"},
            {"publisher": "NHS Employers", "title": "Pay and Conditions Circulars", "url": "https://www.nhsemployers.org/publications/pay-and-conditions-circulars"}
        ],
        "related": ["University Hospitals Plymouth NHS Trust", "Staff Costs"]
    },
    "Impairments net of reversals — Cambridge University Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Impairments net of reversals", "parent": "Cambridge University Hospitals NHS Foundation Trust"}],
        "description": "Non-cash IFRS impairment charges on CUH's Cambridge Biomedical Campus estate — driven by capital-investment valuation movements (the Cambridge Children's Hospital build with Cambridgeshire & Peterborough NHS FT, plus ongoing campus infrastructure investment shared with Royal Papworth, the LMB and research tenants). MEA-DRC valuation gaps drive the charge.",
        "beneficiaries": "Patients across Cambridgeshire + tertiary referrals — major trauma, transplant (renal/liver/BMT/CAR-T), neurosciences and (from build completion) regional paediatrics at Cambridge Children's.",
        "legal_basis": "IAS 36 Impairment of Assets · IFRS / FReM (HM Treasury) · NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022",
        "key_stats": [
            {"label": "Impairments 2024-25", "value": "£47.53M"},
            {"label": "Driver", "value": "Cambridge Children's Hospital build + campus infrastructure · MEA-DRC valuation gap"},
            {"label": "Estate", "value": "Addenbrooke's + Rosie + Cambridge Biomedical Campus shared infrastructure"},
            {"label": "NHP scheme", "value": "Cambridge Children's Hospital (joint with CPFT) confirmed in NHP"},
            {"label": "Campus dynamics", "value": "Shared capital with Royal Papworth, LMB, research tenants"},
            {"label": "Accounting", "value": "Non-cash · valuation movement only · no PDC/cash impact"},
            {"label": "Valuation cycle", "value": "Quinquennial revaluation + interim desktop"},
            {"label": "Group context", "value": "Cambridgeshire & Peterborough ICS · AHSC with University of Cambridge"}
        ],
        "notes": "CUH's impairment charge reflects valuation movements on the live Cambridge Biomedical Campus capital programme — Cambridge Children's Hospital build (joint with CPFT) and ongoing campus infrastructure shared with Royal Papworth + research tenants are creating MEA-DRC valuation gaps as buildings move through construction stages. This is a non-cash charge with no cash or PDC implication, but is material in scale.",
        "sources": [
            {"publisher": "Cambridge University Hospitals NHS Foundation Trust", "title": "Annual report and accounts", "url": "https://www.cuh.nhs.uk/about-us/publications/"},
            {"publisher": "NHS England", "title": "New Hospital Programme — Cambridge Children's Hospital", "url": "https://www.england.nhs.uk/new-hospital-programme/"},
            {"publisher": "Cambridge Children's Hospital", "title": "About the project", "url": "https://www.cambridgechildrens.org.uk/"}
        ],
        "related": ["Cambridge University Hospitals NHS Foundation Trust", "Premises & Infrastructure"]
    },
}
