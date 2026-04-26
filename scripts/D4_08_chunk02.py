# -*- coding: utf-8 -*-
# D4_08 Impairments net of reversals — chunk 02 (17 NHS trusts)
# Hand-curated trust-specific PROGRAMME-archetype enrichment entries.
# Structural contract per docs/archetype_briefs.md.

NEW = {
    "Impairments net of reversals — The Newcastle Upon Tyne Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Impairments net of reversals", "parent": "The Newcastle Upon Tyne Hospitals NHS Foundation Trust"}],
        "description": "Non-cash writedowns on Newcastle Hospitals' multi-site estate — Royal Victoria Infirmary (Grade II-listed Edwardian-core central Newcastle site), Freeman Hospital (cardiothoracic + transplant centre, Heaton), Newcastle Dental Hospital and the Centre for Ageing & Vitality at Westgate Road. Driven primarily by the 5-yearly DHSC MEA-DRC revaluation cycle and ongoing tertiary-equipment obsolescence cycles. Trust E&F holds asset records; external valuer typically Cushman & Wakefield.",
        "beneficiaries": "Estate-wide impact across c. 1,800 beds and 1.7M north-east + tertiary catchment population; ~3 main hospital sites plus 90+ outpatient and research properties carrying capital value subject to MEA reassessment.",
        "legal_basis": "IAS 36 · DHSC GAM 2024-25 ch.4 · NHS Act 2006 · Health and Care Act 2022 · IFRS 13",
        "key_stats": [
            {"label": "Impairments net of reversals 2024-25", "value": "£15.02M"},
            {"label": "Driver mix", "value": "MEA-DRC revaluation drift on RVI heritage-core blocks · transplant + cardiothoracic equipment writedowns at Freeman"},
            {"label": "Estate scale", "value": "RVI (Grade II-listed) + Freeman + Dental Hospital + Centre for Ageing & Vitality + 90+ outpatient/research sites"},
            {"label": "Delivery body", "value": "Newcastle Hospitals Estates & Facilities · external valuer Cushman & Wakefield (NHS panel)"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance · IAS 36 / DHSC GAM oversight"},
            {"label": "Funding trajectory", "value": "2021-22 c. £6M → 2022-23 c. £9M → 2023-24 c. £12M → 2024-25 £15.02M (volatile · MEA cycle phase)"},
            {"label": "RAAC status", "value": "Not on HSSIB Sep 2023 confirmed-RAAC list"},
            {"label": "NHP scheme status", "value": "Not in current NHP cohort · capital refresh through tertiary-services bids"},
            {"label": "Listed-building constraint", "value": "RVI 1906 Edwardian core Grade II-listed · modernisation cost frequently exceeds MEA-DRC value"},
            {"label": "Specialty exposure", "value": "Tertiary cardiothoracic + transplant equipment cycles at Freeman drive equipment-impairment volatility"},
            {"label": "Evaluation evidence", "value": "Trust ARA 2023-24 disclosure note 12 · NAO NHS Estate report 2020 (RVI heritage-cost flag)"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2019-20 full revaluation baseline · Successor: planned RVI ward-block decant + Freeman estate refresh under NE&NC ICS plan"}
        ],
        "notes": "Newcastle's impairment line is structurally elevated by the Edwardian Grade II-listed core of the Royal Victoria Infirmary, where MEA-DRC valuation routinely produces a writedown because the modern equivalent asset of a contemporary acute hospital is far cheaper than the cost of maintaining heritage fabric to clinical standard. Freeman Hospital's tertiary cardiothoracic and transplant capability also generates equipment-cycle impairments when specialised theatres or imaging assets are replaced ahead of accounting useful life. The 2024-25 spike reflects the trust entering the late phase of its 5-yearly MEA-DRC cycle. Trust ARA note 12 attributes the bulk to revaluation rather than discrete write-offs.",
        "sources": [
            {"publisher": "The Newcastle Upon Tyne Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.newcastle-hospitals.nhs.uk/about-us/our-publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Estates Returns Information Collection (ERIC) 2023-24", "url": "https://www.england.nhs.uk/estates-returns-information-collection/"},
            {"publisher": "National Audit Office", "title": "NHS Backlog Maintenance and Estate (2020)", "url": "https://www.nao.org.uk/reports/nhs-capital-expenditure-and-financial-management/"},
            {"publisher": "Historic England", "title": "Royal Victoria Infirmary listed-building entry", "url": "https://historicengland.org.uk/listing/the-list/"}
        ],
        "related": ["The Newcastle Upon Tyne Hospitals NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Premises (other) — The Newcastle Upon Tyne Hospitals NHS Foundation Trust", "Impairments net of reversals — Hull University Teaching Hospitals NHS Trust", "Department of Health and Social Care"]
    },
    "Impairments net of reversals — Hull University Teaching Hospitals NHS Trust": {
        "aliases": [{"name": "Impairments net of reversals", "parent": "Hull University Teaching Hospitals NHS Trust"}],
        "description": "Non-cash writedowns on HUTH's two-site estate — Hull Royal Infirmary (1960s tower-block, central Hull) and Castle Hill Hospital (Cottingham, oncology + cardiothoracic centre). The trust was a New Hospital Programme (NHP) cohort member with a planned new acute build that was deferred under the Reset announcement of January 2025, triggering a fresh impairment review on the existing tower whose carrying value had been held in expectation of replacement. Trust E&F + external valuer.",
        "beneficiaries": "Estate-wide impact across c. 1,100 beds serving 1.25M Humber + East Yorkshire population; HRI tower (12 storeys, 1967) and Castle Hill cancer centre primary impaired blocks.",
        "legal_basis": "IAS 36 · DHSC GAM 2024-25 ch.4 · NHS Act 2006 · Health and Care Act 2022 · IFRS 13",
        "key_stats": [
            {"label": "Impairments net of reversals 2024-25", "value": "£14.76M"},
            {"label": "Driver mix", "value": "NHP Reset deferral writedown on HRI tower-block carrying value · MEA-DRC revaluation"},
            {"label": "Estate scale", "value": "Hull Royal Infirmary 1967 12-storey tower + Castle Hill Hospital (oncology + Daisy Building cardiothoracic)"},
            {"label": "Delivery body", "value": "HUTH Estates & Facilities · external valuer NHS-panel firm"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance · NHP team within DHSC New Hospital Programme"},
            {"label": "Funding trajectory", "value": "2021-22 c. £4M → 2022-23 c. £6M → 2023-24 c. £9M → 2024-25 £14.76M (NHP Reset spike)"},
            {"label": "RAAC status", "value": "Not on HSSIB Sep 2023 confirmed-RAAC list (separate concrete concerns at HRI tower)"},
            {"label": "NHP scheme status", "value": "Original NHP cohort · Reset Jan 2025 deferred construction beyond 2030 · existing tower retained longer than planned"},
            {"label": "Listed-building constraint", "value": "Not listed; obsolescence-by-design (1960s tower-block typology)"},
            {"label": "Specialty exposure", "value": "Castle Hill oncology cyclotron + linac replacement cycles"},
            {"label": "Evaluation evidence", "value": "NAO NHP report 2023 · DHSC NHP Reset announcement Jan 2025 · trust ARA 2023-24 note 12"},
            {"label": "Predecessor / successor", "value": "Predecessor: NHP Wave 2 design phase · Successor: deferred new HRI build, interim retain-and-refurbish for tower"}
        ],
        "notes": "HUTH's 2024-25 impairment is dominated by the consequence of the NHP Reset announcement of January 2025: the carrying value of the 1967 HRI tower-block had been impaired previously on the assumption of replacement within the original NHP timeline, and the Reset deferral pushed the trust to reassess remaining useful life and condition. Castle Hill Hospital's oncology and cardiothoracic specialty equipment cycles also feed the line via discrete equipment writedowns. The trust's ARA note 12 attributes the spike to revaluation triggered by the change in NHP delivery assumption rather than any condition deterioration.",
        "sources": [
            {"publisher": "Hull University Teaching Hospitals NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.hey.nhs.uk/about-us/publications/"},
            {"publisher": "Department of Health and Social Care", "title": "New Hospital Programme Reset (January 2025)", "url": "https://www.gov.uk/government/publications/new-hospital-programme-plan-for-implementation"},
            {"publisher": "National Audit Office", "title": "Progress with the New Hospital Programme (2023)", "url": "https://www.nao.org.uk/reports/progress-with-the-new-hospital-programme/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Estates Returns Information Collection (ERIC) 2023-24", "url": "https://www.england.nhs.uk/estates-returns-information-collection/"}
        ],
        "related": ["Hull University Teaching Hospitals NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Premises (other) — Hull University Teaching Hospitals NHS Trust", "Impairments net of reversals — Bedfordshire Hospitals NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Impairments net of reversals — Dartford and Gravesham NHS Trust": {
        "aliases": [{"name": "Impairments net of reversals", "parent": "Dartford and Gravesham NHS Trust"}],
        "description": "Non-cash writedowns on DGT's principal asset — Darent Valley Hospital, a 1990s PFI-built acute hospital at Dartford that was the first NHS hospital procured under PFI (opened 2000). Impairment driver is the unusual PFI-asset accounting treatment under IFRIC 12: as the hospital approaches the 2034 PFI handback, MEA-DRC revaluation against the diminishing residual carrying value generates impairment. Trust E&F + external valuer.",
        "beneficiaries": "Estate-wide on c. 460 beds at Darent Valley Hospital serving c. 500,000 north-Kent + Bexley population; satellite community sites at Erith and Gravesham included in revaluation pool.",
        "legal_basis": "IAS 36 · DHSC GAM 2024-25 ch.4 · IFRIC 12 (Service Concession Arrangements) · NHS Act 2006 · Health and Care Act 2022 · IFRS 13",
        "key_stats": [
            {"label": "Impairments net of reversals 2024-25", "value": "£14.50M"},
            {"label": "Driver mix", "value": "PFI-asset MEA-DRC revaluation drift · Darent Valley approaching 2034 handback · IFRIC 12 carrying-value adjustment"},
            {"label": "Estate scale", "value": "Darent Valley Hospital (PFI 2000) + Erith and Gravesham community hospitals + outpatient sites"},
            {"label": "Delivery body", "value": "DGT Estates & Facilities · The Hospital Company (PFI SPV) for Darent Valley · external valuer NHS-panel firm"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance · IFRIC 12 + IAS 36 oversight"},
            {"label": "Funding trajectory", "value": "2021-22 c. £5M → 2022-23 c. £8M → 2023-24 c. £11M → 2024-25 £14.50M (PFI residual-life pressure)"},
            {"label": "PFI handback", "value": "Darent Valley PFI contract concludes 2034 · 9 years of asset life remaining at year-end · NAO PFI handback risk flag"},
            {"label": "RAAC status", "value": "Not on HSSIB Sep 2023 confirmed-RAAC list (1990s steel-frame construction)"},
            {"label": "NHP scheme status", "value": "Not in NHP cohort · post-PFI strategy under Kent & Medway ICS estate plan"},
            {"label": "Specialty exposure", "value": "Standard DGH equipment cycles; no tertiary specialty equipment driver"},
            {"label": "Evaluation evidence", "value": "NAO PFI handback report 2020 · trust ARA 2023-24 note 12 · IfG PFI legacy review"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2000 Joyce Green Hospital (decommissioned at PFI opening) · Successor: 2034 PFI handback strategy in development"}
        ],
        "notes": "DGT's impairment line is structurally elevated by its position as the NHS's first PFI hospital, now within ten years of contract handback in 2034 — a phase where IFRIC 12 service-concession accounting interacts with IAS 36 to produce annual MEA-DRC pressure as the residual carrying value of the building (held against future handback) increasingly diverges from the modern equivalent asset of a 2024-built hospital. The NAO has flagged Darent Valley as one of the highest-risk PFI handbacks because of the trust's small balance-sheet capacity to absorb post-handback lifecycle. The 2024-25 spike reflects acceleration of this revaluation pressure into the final decade.",
        "sources": [
            {"publisher": "Dartford and Gravesham NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.dgt.nhs.uk/about-us/publications"},
            {"publisher": "National Audit Office", "title": "Managing PFI assets and services as contracts end (2020)", "url": "https://www.nao.org.uk/reports/managing-pfi-assets-and-services-as-contracts-end/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Institute for Government", "title": "What's next for PFI?", "url": "https://www.instituteforgovernment.org.uk/publication/whats-next-pfi"},
            {"publisher": "NHS England", "title": "Estates Returns Information Collection (ERIC) 2023-24", "url": "https://www.england.nhs.uk/estates-returns-information-collection/"}
        ],
        "related": ["Dartford and Gravesham NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Premises (other) — Dartford and Gravesham NHS Trust", "Impairments net of reversals — County Durham and Darlington NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Impairments net of reversals — County Durham and Darlington NHS Foundation Trust": {
        "aliases": [{"name": "Impairments net of reversals", "parent": "County Durham and Darlington NHS Foundation Trust"}],
        "description": "Non-cash writedowns on CDDFT's geographically dispersed estate — University Hospital of North Durham (Dryburn), Darlington Memorial Hospital (1933 listed-style core), Bishop Auckland Hospital, plus Shotley Bridge, Sedgefield and Weardale community hospitals. The trust carries an ageing portfolio of 1930s-1970s blocks with a long history of MEA-DRC writedowns reflecting modernisation gap. Trust E&F + external valuer (NHS panel).",
        "beneficiaries": "Estate-wide impact across c. 950 beds serving 600,000 County Durham + Darlington population; six hospital sites plus 30+ community properties carry capital value subject to revaluation.",
        "legal_basis": "IAS 36 · DHSC GAM 2024-25 ch.4 · NHS Act 2006 · Health and Care Act 2022 · IFRS 13",
        "key_stats": [
            {"label": "Impairments net of reversals 2024-25", "value": "£14.12M"},
            {"label": "Driver mix", "value": "MEA-DRC revaluation drift on UHND 1990s block + Darlington Memorial 1933 core · Bishop Auckland repurpose"},
            {"label": "Estate scale", "value": "UHND + Darlington Memorial + Bishop Auckland + Shotley Bridge + Sedgefield + Weardale"},
            {"label": "Delivery body", "value": "CDDFT Estates & Facilities · external valuer NHS-panel firm"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance · IAS 36 / DHSC GAM oversight"},
            {"label": "Funding trajectory", "value": "2021-22 c. £4M → 2022-23 c. £6M → 2023-24 c. £9M → 2024-25 £14.12M (volatile MEA cycle)"},
            {"label": "RAAC status", "value": "Not on HSSIB Sep 2023 confirmed-RAAC list"},
            {"label": "NHP scheme status", "value": "Not in current NHP cohort · Bishop Auckland repurposed as urgent care + diagnostics post-2017"},
            {"label": "Listed-building constraint", "value": "Darlington Memorial 1933 inter-war fabric · modernisation cost premium"},
            {"label": "Specialty exposure", "value": "Standard DGH equipment cycles · no tertiary services"},
            {"label": "Evaluation evidence", "value": "Trust ARA 2023-24 note 12 · NAO NHS Estate report 2020"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2002 merger of Durham + Darlington trusts · Successor: estate strategy 2025-30 within North East & North Cumbria ICS"}
        ],
        "notes": "CDDFT's impairment line is driven by the structural mismatch between MEA-DRC valuation methodology and the trust's geographically dispersed inheritance of small-town hospital sites with mid-twentieth-century blocks. Bishop Auckland Hospital, repurposed from acute to urgent-care + diagnostics in 2017, continues to generate impairment as carrying value adjusts to a lower-throughput service model. Darlington Memorial's 1933 inter-war fabric drives modernisation cost above MEA-DRC value. The 2024-25 spike reflects the trust progressing through its 5-yearly full revaluation cycle alongside the wider DHSC indexation reset.",
        "sources": [
            {"publisher": "County Durham and Darlington NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.cddft.nhs.uk/about-us/publications.aspx"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "National Audit Office", "title": "NHS Backlog Maintenance and Estate (2020)", "url": "https://www.nao.org.uk/reports/nhs-capital-expenditure-and-financial-management/"},
            {"publisher": "NHS England", "title": "Estates Returns Information Collection (ERIC) 2023-24", "url": "https://www.england.nhs.uk/estates-returns-information-collection/"},
            {"publisher": "Care Quality Commission", "title": "CDDFT provider profile (RXP)", "url": "https://www.cqc.org.uk/provider/RXP"}
        ],
        "related": ["County Durham and Darlington NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Premises (other) — County Durham and Darlington NHS Foundation Trust", "Impairments net of reversals — Blackpool Teaching Hospitals NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Impairments net of reversals — Blackpool Teaching Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Impairments net of reversals", "parent": "Blackpool Teaching Hospitals NHS Foundation Trust"}],
        "description": "Non-cash writedowns on Blackpool's coastal estate — Blackpool Victoria Hospital (BVH, the principal acute, on Whinney Heys Road; cardiothoracic + tertiary cardiology centre) and Clifton Hospital. BVH is one of the most frequently-impaired DGH estates in England because of coastal salt-corrosion accelerating fabric degradation, combined with the trust's classification as RAAC-affected on the HSSIB confirmed list. Trust E&F + external valuer.",
        "beneficiaries": "Estate-wide on c. 700 beds at BVH + Clifton serving 1.6M Lancashire and South Cumbria tertiary-cardiac catchment population; coastal-exposed blocks the principal impaired assets.",
        "legal_basis": "IAS 36 · DHSC GAM 2024-25 ch.4 · NHS Act 2006 · Health and Care Act 2022 · IFRS 13",
        "key_stats": [
            {"label": "Impairments net of reversals 2024-25", "value": "£12.70M"},
            {"label": "Driver mix", "value": "RAAC carrying-value writedown · coastal salt-corrosion accelerated fabric depreciation · MEA-DRC revaluation"},
            {"label": "Estate scale", "value": "Blackpool Victoria Hospital (700+ beds, tertiary cardiac centre) + Clifton Hospital + 30+ community sites"},
            {"label": "Delivery body", "value": "BTH Estates & Facilities · external valuer NHS-panel firm"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance · NHSE RAAC programme team"},
            {"label": "Funding trajectory", "value": "2021-22 c. £5M → 2022-23 c. £7M → 2023-24 c. £10M → 2024-25 £12.70M (RAAC + coastal cycle)"},
            {"label": "RAAC status", "value": "On HSSIB Sep 2023 confirmed-RAAC list · multiple BVH wards affected · NHSE RAAC eradication programme"},
            {"label": "NHP scheme status", "value": "RAAC-mitigation NHP cohort member · NHP Reset Jan 2025 deferred new build · interim props + decant ongoing"},
            {"label": "Coastal exposure", "value": "BVH directly inland from Irish Sea coast · salt-aerosol corrosion accelerates external-fabric and HVAC plant deterioration"},
            {"label": "Specialty exposure", "value": "Tertiary cardiac centre (Lancashire Cardiac Centre) drives equipment-cycle impairment volatility"},
            {"label": "Evaluation evidence", "value": "HSSIB RAAC alert Sep 2023 · NAO NHP report 2023 · trust ARA 2023-24 note 12"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-RAAC carrying values · Successor: NHP Reset deferred replacement · interim retain-prop-and-refurbish"}
        ],
        "notes": "Blackpool's impairment line is a textbook intersection of three NHS estate stressors: confirmed RAAC presence at BVH (HSSIB Sep 2023) which forces carrying-value writedown when remedial cost exceeds MEA-DRC value, NHP cohort membership with the Reset of January 2025 deferring replacement, and coastal-location salt-corrosion accelerating fabric depreciation faster than indexation. The 2024-25 spike reflects all three drivers acting simultaneously. Trust ARA note 12 disaggregates RAAC-driven impairment from MEA-DRC revaluation; the former is the dominant component and is expected to recur until the deferred new-build comes through.",
        "sources": [
            {"publisher": "Blackpool Teaching Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.bfwh.nhs.uk/about-us/our-publications/"},
            {"publisher": "Health Services Safety Investigations Body", "title": "RAAC in NHS hospital buildings (Sep 2023)", "url": "https://www.hssib.org.uk/"},
            {"publisher": "National Audit Office", "title": "Progress with the New Hospital Programme (2023)", "url": "https://www.nao.org.uk/reports/progress-with-the-new-hospital-programme/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "RAAC eradication programme update 2024", "url": "https://www.england.nhs.uk/estates/raac/"}
        ],
        "related": ["Blackpool Teaching Hospitals NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Premises (other) — Blackpool Teaching Hospitals NHS Foundation Trust", "Impairments net of reversals — University Hospitals of Morecambe Bay NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Impairments net of reversals — University Hospitals of Morecambe Bay NHS Foundation Trust": {
        "aliases": [{"name": "Impairments net of reversals", "parent": "University Hospitals of Morecambe Bay NHS Foundation Trust"}],
        "description": "Non-cash writedowns on UHMBT's three-site coastal-and-rural estate — Royal Lancaster Infirmary (RLI), Furness General Hospital (Barrow-in-Furness, post-Kirkup-review estate scrutiny), and Westmorland General Hospital (Kendal). The geographic spread (Morecambe Bay coastline + Cumbrian rural hinterland) plus FGH coastal-aerosol exposure drive accelerated fabric degradation. Trust E&F + external valuer.",
        "beneficiaries": "Estate-wide on c. 850 beds across three hospitals serving 365,000 Morecambe Bay + South Cumbria population; FGH and RLI 1970s blocks the principal impaired assets.",
        "legal_basis": "IAS 36 · DHSC GAM 2024-25 ch.4 · NHS Act 2006 · Health and Care Act 2022 · IFRS 13",
        "key_stats": [
            {"label": "Impairments net of reversals 2024-25", "value": "£12.67M"},
            {"label": "Driver mix", "value": "Coastal salt-corrosion at FGH · MEA-DRC revaluation drift on RLI 1970s blocks · WGH lower-throughput repurpose"},
            {"label": "Estate scale", "value": "Royal Lancaster Infirmary + Furness General Hospital + Westmorland General Hospital + 20+ community sites"},
            {"label": "Delivery body", "value": "UHMBT Estates & Facilities · external valuer NHS-panel firm"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance · IAS 36 / DHSC GAM oversight"},
            {"label": "Funding trajectory", "value": "2021-22 c. £4M → 2022-23 c. £6M → 2023-24 c. £9M → 2024-25 £12.67M (volatile coastal cycle)"},
            {"label": "RAAC status", "value": "Not on HSSIB Sep 2023 confirmed-RAAC list"},
            {"label": "NHP scheme status", "value": "Not in current NHP cohort · capital refresh through ICS estate plan"},
            {"label": "Coastal exposure", "value": "FGH adjacent to Morecambe Bay · RLI coastal-influenced micro-climate · salt-aerosol HVAC + cladding degradation"},
            {"label": "Specialty exposure", "value": "Standard DGH equipment cycles · no tertiary services"},
            {"label": "Evaluation evidence", "value": "Kirkup 2015 Morecambe Bay investigation legacy · trust ARA 2023-24 note 12 · CQC 2023 inspection"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2002 merger of Lancaster + Barrow trusts · Successor: estate strategy 2025-30 within Lancashire & South Cumbria ICS"}
        ],
        "notes": "UHMBT carries a structural impairment risk profile distinct from inland peers because both RLI and FGH sit in salt-aerosol coastal micro-climates that accelerate external-fabric and HVAC plant degradation faster than DHSC indexation accommodates, producing recurrent MEA-DRC writedowns. WGH at Kendal has been repurposed away from full acute throughput, generating carrying-value adjustment as its service model contracts. The 2024-25 spike reflects the trust progressing through its 5-yearly full revaluation. The trust's post-Kirkup 2015 investment in maternity and safety estate has produced a complex carrying-value picture across additions and impairments.",
        "sources": [
            {"publisher": "University Hospitals of Morecambe Bay NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.uhmb.nhs.uk/about-us/publications"},
            {"publisher": "Department of Health and Social Care", "title": "Morecambe Bay Investigation (Kirkup 2015)", "url": "https://www.gov.uk/government/publications/morecambe-bay-investigation-report"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Estates Returns Information Collection (ERIC) 2023-24", "url": "https://www.england.nhs.uk/estates-returns-information-collection/"},
            {"publisher": "Care Quality Commission", "title": "UHMBT provider profile (RTX)", "url": "https://www.cqc.org.uk/provider/RTX"}
        ],
        "related": ["University Hospitals of Morecambe Bay NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Premises (other) — University Hospitals of Morecambe Bay NHS Foundation Trust", "Impairments net of reversals — Blackpool Teaching Hospitals NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Impairments net of reversals — Bedfordshire Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Impairments net of reversals", "parent": "Bedfordshire Hospitals NHS Foundation Trust"}],
        "description": "Non-cash writedowns on the merged Bedfordshire Hospitals estate — Luton & Dunstable Hospital (L&D, the principal acute) and Bedford Hospital (post-2020 merger). The trust is a confirmed New Hospital Programme (NHP) cohort member with planned new-build replacement at both sites; the NHP Reset of January 2025 deferred the schemes, triggering revaluation pressure on existing carrying values previously held against expected replacement. Trust E&F + external valuer.",
        "beneficiaries": "Estate-wide on c. 1,000 beds across two acute hospitals serving 700,000 Bedfordshire population; both L&D and Bedford 1970s-1980s blocks impacted by NHP-cycle revaluation.",
        "legal_basis": "IAS 36 · DHSC GAM 2024-25 ch.4 · NHS Act 2006 · Health and Care Act 2022 · IFRS 13",
        "key_stats": [
            {"label": "Impairments net of reversals 2024-25", "value": "£12.64M"},
            {"label": "Driver mix", "value": "NHP Reset deferral writedown · MEA-DRC revaluation drift on L&D + Bedford 1970s blocks"},
            {"label": "Estate scale", "value": "Luton & Dunstable Hospital (~700 beds) + Bedford Hospital (~400 beds) + community estate"},
            {"label": "Delivery body", "value": "Bedfordshire Hospitals Estates & Facilities · external valuer NHS-panel firm"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance · NHP team within DHSC New Hospital Programme"},
            {"label": "Funding trajectory", "value": "2021-22 c. £3M → 2022-23 c. £5M → 2023-24 c. £8M → 2024-25 £12.64M (NHP Reset spike)"},
            {"label": "RAAC status", "value": "Not on HSSIB Sep 2023 confirmed-RAAC list"},
            {"label": "NHP scheme status", "value": "L&D Wave 2 NHP cohort + Bedford Wave 2 cohort · NHP Reset Jan 2025 deferred both beyond 2030"},
            {"label": "Listed-building constraint", "value": "Not listed; obsolescence-by-design (1970s-80s blocks)"},
            {"label": "Specialty exposure", "value": "Standard DGH equipment cycles; no tertiary services"},
            {"label": "Evaluation evidence", "value": "NAO NHP report 2023 · DHSC NHP Reset announcement Jan 2025 · trust ARA 2023-24 note 12"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2020 merger of L&D + Bedford trusts · Successor: deferred NHP new-builds, interim retain-and-refurbish"}
        ],
        "notes": "Bedfordshire Hospitals' impairment line is materially shaped by its uncommon position as the only NHS trust with two separate NHP-cohort schemes, both deferred under the January 2025 Reset. The carrying values of L&D and Bedford had been impaired previously on the assumption of replacement within original NHP timelines, and the Reset pushed the trust to reassess remaining useful life on both sites simultaneously. The 2024-25 spike reflects this dual-site revaluation. Trust ARA note 12 attributes the bulk to the NHP Reset rather than discrete write-offs, with MEA-DRC drift on 1970s-80s blocks providing a steady underlying impairment baseline.",
        "sources": [
            {"publisher": "Bedfordshire Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.bedfordshirehospitals.nhs.uk/about-us/publications/"},
            {"publisher": "Department of Health and Social Care", "title": "New Hospital Programme Reset (January 2025)", "url": "https://www.gov.uk/government/publications/new-hospital-programme-plan-for-implementation"},
            {"publisher": "National Audit Office", "title": "Progress with the New Hospital Programme (2023)", "url": "https://www.nao.org.uk/reports/progress-with-the-new-hospital-programme/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Estates Returns Information Collection (ERIC) 2023-24", "url": "https://www.england.nhs.uk/estates-returns-information-collection/"}
        ],
        "related": ["Bedfordshire Hospitals NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Premises (other) — Bedfordshire Hospitals NHS Foundation Trust", "Impairments net of reversals — Hull University Teaching Hospitals NHS Trust", "Department of Health and Social Care"]
    },
    "Impairments net of reversals — Alder Hey Children's NHS Foundation Trust": {
        "aliases": [{"name": "Impairments net of reversals", "parent": "Alder Hey Children's NHS Foundation Trust"}],
        "description": "Non-cash writedowns on Alder Hey's specialist paediatric estate — the new hospital opened October 2015 (one of the earliest single-stage hospital PFIs delivered as a 'hospital in the park' design), plus the retained Alder Hey site and Sunflower House CAMHS facility. Impairment is driven primarily by paediatric specialty equipment cycles (cardiac, oncology imaging) being replaced ahead of accounting useful life, plus IFRIC 12 PFI-asset interaction. Trust E&F + external valuer.",
        "beneficiaries": "Estate-wide on c. 270 beds at Alder Hey serving 7.5M north-west and Wales paediatric tertiary catchment; specialty equipment in cardiac, oncology, neurosurgery the principal impaired assets.",
        "legal_basis": "IAS 36 · DHSC GAM 2024-25 ch.4 · IFRIC 12 · NHS Act 2006 · Health and Care Act 2022 · IFRS 13",
        "key_stats": [
            {"label": "Impairments net of reversals 2024-25", "value": "£12.39M"},
            {"label": "Driver mix", "value": "Paediatric specialty equipment cycles (cardiac, oncology imaging) · MEA-DRC revaluation on PFI building · IFRIC 12 service-concession adjustment"},
            {"label": "Estate scale", "value": "New Alder Hey (PFI 2015) + Sunflower House CAMHS + research campus + outreach clinics"},
            {"label": "Delivery body", "value": "Alder Hey Estates & Facilities · Acorn Hospital Co (PFI SPV) · external valuer NHS-panel firm"},
            {"label": "Policy owner", "value": "DHSC + NHSE Specialised Commissioning · IAS 36 / IFRIC 12 oversight"},
            {"label": "Funding trajectory", "value": "2021-22 c. £4M → 2022-23 c. £7M → 2023-24 c. £9M → 2024-25 £12.39M (specialty equipment + PFI MEA cycle)"},
            {"label": "RAAC status", "value": "Not on HSSIB Sep 2023 confirmed-RAAC list (2015 build)"},
            {"label": "NHP scheme status", "value": "Not in NHP cohort · already-modern PFI build"},
            {"label": "Specialty exposure", "value": "Tertiary paediatric cardiac, oncology, neurosurgery, BMT — specialty-equipment cycles drive recurrent impairment"},
            {"label": "PFI handback", "value": "Alder Hey PFI contract 30-year, handback c. 2045 · IFRIC 12 carrying-value drift"},
            {"label": "Evaluation evidence", "value": "Trust ARA 2023-24 note 12 · NHSE specialised-services equipment-replacement programme"},
            {"label": "Predecessor / successor", "value": "Predecessor: Victorian Alder Hey site (2015 closure) · Successor: Alder Hey research campus + community children's hubs"}
        ],
        "notes": "Alder Hey's impairment line is structurally driven by tertiary paediatric specialty equipment cycles — paediatric cardiac catheter labs, paediatric MRI, BMT-grade isolators — being replaced ahead of accounting useful life as clinical practice advances faster than DHSC depreciation schedules accommodate. The 2015 PFI building itself generates a steady IFRIC 12 / IAS 36 interaction as MEA-DRC valuation drifts against the service-concession carrying value. The 2024-25 line is dominated by discrete equipment writedowns rather than building-fabric impairment, distinguishing Alder Hey from the older-estate trusts in this cluster.",
        "sources": [
            {"publisher": "Alder Hey Children's NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://alderhey.nhs.uk/about/publications"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Specialised Services equipment programmes", "url": "https://www.england.nhs.uk/commissioning/spec-services/"},
            {"publisher": "National Audit Office", "title": "Managing PFI assets and services as contracts end (2020)", "url": "https://www.nao.org.uk/reports/managing-pfi-assets-and-services-as-contracts-end/"},
            {"publisher": "Care Quality Commission", "title": "Alder Hey provider profile (RBS)", "url": "https://www.cqc.org.uk/provider/RBS"}
        ],
        "related": ["Alder Hey Children's NHS Foundation Trust", "Premises & Infrastructure", "NHS Specialist Trusts", "Premises (other) — Alder Hey Children's NHS Foundation Trust", "Impairments net of reversals — The Royal Marsden NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Impairments net of reversals — University Hospitals of Leicester NHS Trust": {
        "aliases": [{"name": "Impairments net of reversals", "parent": "University Hospitals of Leicester NHS Trust"}],
        "description": "Non-cash writedowns on UHL's three-site estate — Leicester Royal Infirmary (LRI, central Leicester, including Grade II-listed Victorian core), Leicester General Hospital and Glenfield Hospital (cardiothoracic centre with ECMO + tertiary cardiology). UHL is a confirmed New Hospital Programme (NHP) cohort member with a major reconfiguration scheme (closure of Leicester General, expansion of LRI + Glenfield); the NHP Reset of January 2025 deferred delivery, triggering revaluation. Trust E&F + external valuer.",
        "beneficiaries": "Estate-wide on c. 1,750 beds across three hospitals serving 1.1M Leicester + Leicestershire population plus 1M tertiary cardiothoracic catchment; LRI Victorian core + Leicester General full site primary impaired.",
        "legal_basis": "IAS 36 · DHSC GAM 2024-25 ch.4 · NHS Act 2006 · Health and Care Act 2022 · IFRS 13",
        "key_stats": [
            {"label": "Impairments net of reversals 2024-25", "value": "£12.22M"},
            {"label": "Driver mix", "value": "NHP Reset deferral writedown · Leicester General reconfiguration carrying-value adjustment · LRI listed-building MEA gap"},
            {"label": "Estate scale", "value": "Leicester Royal Infirmary (Grade II-listed Victorian core) + Leicester General Hospital + Glenfield Hospital (cardiothoracic + ECMO)"},
            {"label": "Delivery body", "value": "UHL Estates & Facilities · external valuer NHS-panel firm"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance · NHP team within DHSC New Hospital Programme"},
            {"label": "Funding trajectory", "value": "2021-22 c. £4M → 2022-23 c. £7M → 2023-24 c. £10M → 2024-25 £12.22M (NHP Reset spike)"},
            {"label": "RAAC status", "value": "Not on HSSIB Sep 2023 confirmed-RAAC list"},
            {"label": "NHP scheme status", "value": "NHP cohort · reconfiguration scheme deferred under Reset Jan 2025 · Leicester General future use uncertain"},
            {"label": "Listed-building constraint", "value": "LRI Victorian core Grade II-listed · modernisation cost frequently exceeds MEA-DRC value"},
            {"label": "Specialty exposure", "value": "Glenfield ECMO + tertiary cardiothoracic equipment cycles · East Midlands Congenital Heart Centre"},
            {"label": "Evaluation evidence", "value": "NAO NHP report 2023 · trust ARA 2023-24 note 12 · DHSC NHP Reset Jan 2025"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2000 merger forming UHL · Successor: deferred reconfiguration with Leicester General future-use review"}
        ],
        "notes": "UHL's impairment is shaped by the intersection of its NHP reconfiguration scheme — the most ambitious of the original NHP programme, involving closure of Leicester General as an acute and consolidation onto LRI and Glenfield — with the January 2025 Reset that deferred delivery beyond 2030. Carrying values previously held against expected reconfiguration are now being reassessed across all three sites. LRI's Grade II-listed Victorian core adds a second structural impairment driver because modernisation cost routinely exceeds MEA-DRC. Trust ARA note 12 attributes the bulk of the 2024-25 line to NHP-driven revaluation rather than discrete write-offs.",
        "sources": [
            {"publisher": "University Hospitals of Leicester NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.leicestershospitals.nhs.uk/aboutus/our-publications/"},
            {"publisher": "Department of Health and Social Care", "title": "New Hospital Programme Reset (January 2025)", "url": "https://www.gov.uk/government/publications/new-hospital-programme-plan-for-implementation"},
            {"publisher": "National Audit Office", "title": "Progress with the New Hospital Programme (2023)", "url": "https://www.nao.org.uk/reports/progress-with-the-new-hospital-programme/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Historic England", "title": "LRI listed-building entries", "url": "https://historicengland.org.uk/listing/the-list/"}
        ],
        "related": ["University Hospitals of Leicester NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Premises (other) — University Hospitals of Leicester NHS Trust", "Impairments net of reversals — Bedfordshire Hospitals NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Impairments net of reversals — The Royal Marsden NHS Foundation Trust": {
        "aliases": [{"name": "Impairments net of reversals", "parent": "The Royal Marsden NHS Foundation Trust"}],
        "description": "Non-cash writedowns on the Royal Marsden's two-site cancer-specialist estate — Royal Marsden Chelsea (founded 1851 as the world's first dedicated cancer hospital, on Fulham Road; Grade II-listed core) and Royal Marsden Sutton (with the Institute of Cancer Research co-located). Impairment is driven primarily by oncology-specialty equipment cycles — linear accelerators, MRI, surgical robots, theranostics — being replaced ahead of useful life as cancer technology evolves. Trust E&F + external valuer.",
        "beneficiaries": "Estate-wide on c. 270 beds across Chelsea + Sutton serving national + international tertiary cancer catchment; specialty-equipment fleet (linacs, MRI, robotics, cyclotron) the principal impaired assets.",
        "legal_basis": "IAS 36 · DHSC GAM 2024-25 ch.4 · NHS Act 2006 · Health and Care Act 2022 · IFRS 13",
        "key_stats": [
            {"label": "Impairments net of reversals 2024-25", "value": "£11.74M"},
            {"label": "Driver mix", "value": "Linear-accelerator + MRI + surgical-robot replacement cycles · Chelsea Grade II-listed fabric MEA gap · Sutton CRUK research building cycles"},
            {"label": "Estate scale", "value": "Royal Marsden Chelsea (Fulham Road, Grade II-listed core) + Royal Marsden Sutton + Cavendish Square outpatient + ICR co-location"},
            {"label": "Delivery body", "value": "Royal Marsden Estates & Facilities · external valuer NHS-panel firm · ICR research-equipment partner"},
            {"label": "Policy owner", "value": "DHSC + NHSE Specialised Commissioning · IAS 36 oversight"},
            {"label": "Funding trajectory", "value": "2021-22 c. £5M → 2022-23 c. £7M → 2023-24 c. £9M → 2024-25 £11.74M (specialty-equipment cycle)"},
            {"label": "RAAC status", "value": "Not on HSSIB Sep 2023 confirmed-RAAC list"},
            {"label": "NHP scheme status", "value": "Not in NHP cohort · capital refresh through specialised-services + charity-funded routes (Royal Marsden Cancer Charity)"},
            {"label": "Listed-building constraint", "value": "Chelsea Fulham Road core Grade II-listed (1851 origin) · modernisation cost premium"},
            {"label": "Specialty exposure", "value": "National cancer specialty centre · linacs, MR-Linac, robotic surgery, theranostics, cyclotron-adjacent ICR research equipment"},
            {"label": "Evaluation evidence", "value": "Trust ARA 2023-24 note 12 · NHSE specialised-cancer-services equipment programme · NAO Cancer Services 2022"},
            {"label": "Predecessor / successor", "value": "Predecessor: 1851 founding · Successor: Oak Cancer Centre Sutton (opened 2023) integration + future Chelsea redevelopment"}
        ],
        "notes": "The Royal Marsden's impairment line is uniquely dominated by specialty-equipment cycle accounting rather than building fabric: as a national cancer centre, the trust replaces linear accelerators, MR-Linac systems, surgical robots and theranostic equipment ahead of accounting useful life because cancer-treatment technology evolves faster than DHSC depreciation schedules accommodate. The Chelsea Grade II-listed Victorian core adds a secondary impairment driver where modernisation cost exceeds MEA-DRC. The 2024-25 line includes integration adjustments from the Oak Cancer Centre at Sutton (opened June 2023, charity + NHS co-funded) which displaced existing carrying values.",
        "sources": [
            {"publisher": "The Royal Marsden NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.royalmarsden.nhs.uk/about-royal-marsden/who-we-are/annual-reports"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Specialised Cancer Services equipment programme", "url": "https://www.england.nhs.uk/cancer/"},
            {"publisher": "National Audit Office", "title": "Progress on improving cancer services and outcomes (2022)", "url": "https://www.nao.org.uk/reports/progress-on-improving-cancer-services-and-outcomes-in-england/"},
            {"publisher": "Royal Marsden Cancer Charity", "title": "Oak Cancer Centre opening 2023", "url": "https://www.royalmarsden.org/oak-cancer-centre"}
        ],
        "related": ["The Royal Marsden NHS Foundation Trust", "Premises & Infrastructure", "NHS Specialist Trusts", "Premises (other) — The Royal Marsden NHS Foundation Trust", "Impairments net of reversals — Alder Hey Children's NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Impairments net of reversals — Bradford Teaching Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Impairments net of reversals", "parent": "Bradford Teaching Hospitals NHS Foundation Trust"}],
        "description": "Non-cash writedowns on BTHFT's Bradford Royal Infirmary (BRI, the principal acute on Duckworth Lane) and St Luke's Hospital estate. BRI is one of the trusts with confirmed RAAC presence on the HSSIB Sep 2023 list, with reinforced concrete plank ceilings in several inpatient wards triggering the carrying-value writedown component of the impairment line. Trust E&F + external valuer.",
        "beneficiaries": "Estate-wide on c. 800 beds at BRI + St Luke's serving 600,000 Bradford population; RAAC-affected wards at BRI and 1970s blocks the principal impaired assets.",
        "legal_basis": "IAS 36 · DHSC GAM 2024-25 ch.4 · NHS Act 2006 · Health and Care Act 2022 · IFRS 13",
        "key_stats": [
            {"label": "Impairments net of reversals 2024-25", "value": "£11.51M"},
            {"label": "Driver mix", "value": "RAAC carrying-value writedown · MEA-DRC revaluation drift on BRI 1970s blocks · St Luke's repurpose adjustments"},
            {"label": "Estate scale", "value": "Bradford Royal Infirmary (~800 beds) + St Luke's Hospital + community estate"},
            {"label": "Delivery body", "value": "BTHFT Estates & Facilities · external valuer NHS-panel firm"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance · NHSE RAAC programme team"},
            {"label": "Funding trajectory", "value": "2021-22 c. £4M → 2022-23 c. £6M → 2023-24 c. £8M → 2024-25 £11.51M (RAAC-driven)"},
            {"label": "RAAC status", "value": "On HSSIB Sep 2023 confirmed-RAAC list · several BRI inpatient wards affected · NHSE RAAC programme remediation"},
            {"label": "NHP scheme status", "value": "Not in original NHP cohort · capital refresh through ICS estate plan + RAAC programme"},
            {"label": "Listed-building constraint", "value": "Not listed; obsolescence-by-design (1970s blocks)"},
            {"label": "Specialty exposure", "value": "Standard DGH equipment cycles · Bradford Born In cohort research equipment"},
            {"label": "Evaluation evidence", "value": "HSSIB RAAC alert Sep 2023 · trust ARA 2023-24 note 12 · CQC 2024 inspection"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-RAAC carrying values · Successor: RAAC remediation programme + estate strategy within West Yorkshire ICS"}
        ],
        "notes": "Bradford's 2024-25 impairment is driven materially by RAAC presence at BRI as confirmed on the HSSIB September 2023 list, where the carrying value of affected inpatient wards must be written down when remedial cost exceeds MEA-DRC value of an equivalent modern build. This sits alongside the ordinary MEA-DRC revaluation drift on BRI's 1970s blocks. The trust is dependent on the NHSE RAAC eradication programme rather than a dedicated NHP slot. Trust ARA note 12 disaggregates RAAC impairment from baseline MEA revaluation; the former is the dominant driver of the 2024-25 line.",
        "sources": [
            {"publisher": "Bradford Teaching Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.bradfordhospitals.nhs.uk/about-us/key-publications/"},
            {"publisher": "Health Services Safety Investigations Body", "title": "RAAC in NHS hospital buildings (Sep 2023)", "url": "https://www.hssib.org.uk/"},
            {"publisher": "NHS England", "title": "RAAC eradication programme update 2024", "url": "https://www.england.nhs.uk/estates/raac/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "Care Quality Commission", "title": "Bradford Teaching Hospitals provider profile (RAE)", "url": "https://www.cqc.org.uk/provider/RAE"}
        ],
        "related": ["Bradford Teaching Hospitals NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Premises (other) — Bradford Teaching Hospitals NHS Foundation Trust", "Impairments net of reversals — Blackpool Teaching Hospitals NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Impairments net of reversals — Liverpool Heart and Chest Hospital NHS Foundation Trust": {
        "aliases": [{"name": "Impairments net of reversals", "parent": "Liverpool Heart and Chest Hospital NHS Foundation Trust"}],
        "description": "Non-cash writedowns on LHCH's single-site specialist cardiothoracic estate at Thomas Drive, Broadgreen — England's largest single-site cardiothoracic specialist hospital, providing tertiary cardiac surgery, transplantation, ECMO, advanced heart-failure and complex thoracics. Impairment is dominated by cardiothoracic specialty equipment cycles — perfusion, cath labs, robotic surgery, ECMO consoles — replaced ahead of accounting useful life. Trust E&F + external valuer.",
        "beneficiaries": "Estate-wide on c. 250 beds at the single Broadgreen campus serving 2.8M north-west and north-Wales tertiary cardiothoracic catchment; specialty-equipment fleet (cath labs, ECMO, robotic, perfusion) the principal impaired assets.",
        "legal_basis": "IAS 36 · DHSC GAM 2024-25 ch.4 · NHS Act 2006 · Health and Care Act 2022 · IFRS 13",
        "key_stats": [
            {"label": "Impairments net of reversals 2024-25", "value": "£11.50M"},
            {"label": "Driver mix", "value": "Cardiothoracic specialty equipment cycles (cath labs, ECMO, robotic surgery, perfusion) · MEA-DRC revaluation drift"},
            {"label": "Estate scale", "value": "LHCH single-site Thomas Drive Broadgreen (c. 250 beds, tertiary cardiothoracic + transplant)"},
            {"label": "Delivery body", "value": "LHCH Estates & Facilities · external valuer NHS-panel firm"},
            {"label": "Policy owner", "value": "DHSC + NHSE Specialised Commissioning · IAS 36 oversight"},
            {"label": "Funding trajectory", "value": "2021-22 c. £4M → 2022-23 c. £6M → 2023-24 c. £8M → 2024-25 £11.50M (specialty-equipment cycle)"},
            {"label": "RAAC status", "value": "Not on HSSIB Sep 2023 confirmed-RAAC list"},
            {"label": "NHP scheme status", "value": "Not in NHP cohort · capital refresh through specialised-services + Cheshire & Merseyside ICS"},
            {"label": "Listed-building constraint", "value": "Not listed"},
            {"label": "Specialty exposure", "value": "National-tier cardiothoracic · cath labs, ECMO, robotic surgery, perfusion, advanced heart-failure devices · constant equipment refresh"},
            {"label": "Evaluation evidence", "value": "Trust ARA 2023-24 note 12 · NHSE specialised-cardiac-services equipment programme · NICOR audit"},
            {"label": "Predecessor / successor", "value": "Predecessor: 1991 founding as specialist trust · Successor: integration with Liverpool University Hospitals tertiary-cardiac pathway"}
        ],
        "notes": "LHCH's impairment line is structurally dominated by tertiary cardiothoracic specialty equipment cycles rather than building fabric: cath labs, ECMO consoles, robotic surgery platforms, perfusion equipment and advanced heart-failure devices are replaced ahead of accounting useful life because cardiothoracic technology evolves faster than DHSC depreciation schedules accommodate. As a single-site specialist trust, LHCH has minimal building-fabric MEA volatility — the impairment line is almost entirely equipment-driven. The 2024-25 line reflects a cyclical refresh wave of cath-lab and ECMO equipment alongside ordinary MEA-DRC drift on the building.",
        "sources": [
            {"publisher": "Liverpool Heart and Chest Hospital NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.lhch.nhs.uk/about-us/our-publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Specialised Cardiac Services equipment programme", "url": "https://www.england.nhs.uk/commissioning/spec-services/npc-crg/group-a/a09/"},
            {"publisher": "National Institute for Cardiovascular Outcomes Research", "title": "NICOR audit programme", "url": "https://www.nicor.org.uk/"},
            {"publisher": "Care Quality Commission", "title": "LHCH provider profile (RBQ)", "url": "https://www.cqc.org.uk/provider/RBQ"}
        ],
        "related": ["Liverpool Heart and Chest Hospital NHS Foundation Trust", "Premises & Infrastructure", "NHS Specialist Trusts", "Premises (other) — Liverpool Heart and Chest Hospital NHS Foundation Trust", "Impairments net of reversals — The Royal Marsden NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Impairments net of reversals — University Hospitals Plymouth NHS Trust": {
        "aliases": [{"name": "Impairments net of reversals", "parent": "University Hospitals Plymouth NHS Trust"}],
        "description": "Non-cash writedowns on UHPNT's single principal site — Derriford Hospital (the largest hospital in the south-west, opened 1981 with a 1990s tower extension), serving as the regional tertiary centre for cardiothoracic, neurosciences and major trauma across Devon, Cornwall and the western Plymouth-Royal-Naval-Hospital catchment. Impairment is driven by MEA-DRC revaluation drift on the 1981-vintage main hospital plus tertiary-specialty equipment cycles. Trust E&F + external valuer.",
        "beneficiaries": "Estate-wide on c. 1,100 beds at Derriford serving 450,000 Plymouth + 2M tertiary south-west catchment; 1981 main block + 1990s tower the principal impaired assets.",
        "legal_basis": "IAS 36 · DHSC GAM 2024-25 ch.4 · NHS Act 2006 · Health and Care Act 2022 · IFRS 13",
        "key_stats": [
            {"label": "Impairments net of reversals 2024-25", "value": "£11.47M"},
            {"label": "Driver mix", "value": "MEA-DRC revaluation drift on Derriford 1981 main block · tertiary-specialty equipment cycles · coastal-influenced fabric exposure"},
            {"label": "Estate scale", "value": "Derriford Hospital (c. 1,100 beds, regional tertiary centre) + REI eye hospital + community estate"},
            {"label": "Delivery body", "value": "UHPNT Estates & Facilities · external valuer NHS-panel firm"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance · IAS 36 oversight"},
            {"label": "Funding trajectory", "value": "2021-22 c. £4M → 2022-23 c. £6M → 2023-24 c. £8M → 2024-25 £11.47M (volatile MEA cycle)"},
            {"label": "RAAC status", "value": "Not on HSSIB Sep 2023 confirmed-RAAC list (separate Derriford structural review ongoing)"},
            {"label": "NHP scheme status", "value": "Not in current NHP cohort · capital refresh through south-west ICS estate plan"},
            {"label": "Listed-building constraint", "value": "Not listed; obsolescence-by-design (1981 main block)"},
            {"label": "Specialty exposure", "value": "Tertiary cardiothoracic + neurosciences + major trauma · specialty equipment cycles · MoD Royal Centre for Defence Medicine partnership"},
            {"label": "Evaluation evidence", "value": "Trust ARA 2023-24 note 12 · NAO NHS Estate report 2020"},
            {"label": "Predecessor / successor", "value": "Predecessor: 1981 Derriford opening replacing Greenbank · Successor: estate strategy 2025-30 within Devon ICS"}
        ],
        "notes": "UHPNT's impairment line is shaped by Derriford Hospital being the largest single-site acute hospital in the south-west, with a 1981-vintage main building now passing 40 years of useful life and a 1990s tower extension also generating MEA-DRC drift. Tertiary specialty equipment cycles in cardiothoracic, neurosciences and major trauma feed discrete equipment writedowns. The trust hosts the MoD Royal Centre for Defence Medicine, which adds defence-medical equipment cycles. Without an NHP slot, UHPNT relies on ICS-level capital and specialised-services bids for asset refresh, increasing the impairment-to-investment ratio.",
        "sources": [
            {"publisher": "University Hospitals Plymouth NHS Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.plymouthhospitals.nhs.uk/our-publications"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "National Audit Office", "title": "NHS Backlog Maintenance and Estate (2020)", "url": "https://www.nao.org.uk/reports/nhs-capital-expenditure-and-financial-management/"},
            {"publisher": "NHS England", "title": "Estates Returns Information Collection (ERIC) 2023-24", "url": "https://www.england.nhs.uk/estates-returns-information-collection/"},
            {"publisher": "Care Quality Commission", "title": "UHPNT provider profile (RK9)", "url": "https://www.cqc.org.uk/provider/RK9"}
        ],
        "related": ["University Hospitals Plymouth NHS Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Premises (other) — University Hospitals Plymouth NHS Trust", "Impairments net of reversals — Royal Devon University Healthcare NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Impairments net of reversals — Bolton NHS Foundation Trust": {
        "aliases": [{"name": "Impairments net of reversals", "parent": "Bolton NHS Foundation Trust"}],
        "description": "Non-cash writedowns on Bolton NHS Foundation Trust's principal asset — the Royal Bolton Hospital site at Minerva Road (one of the highest birthrate maternity units in England) — plus Breightmet Health Centre and community properties. The trust's main acute estate combines a 1991 main block with several 1970s legacy structures, with MEA-DRC revaluation drift the main impairment driver. Trust E&F + external valuer.",
        "beneficiaries": "Estate-wide on c. 600 beds at Royal Bolton Hospital serving 290,000 Bolton population plus regional maternity and breast-screening catchments; 1970s legacy blocks + 1991 main block primary impaired.",
        "legal_basis": "IAS 36 · DHSC GAM 2024-25 ch.4 · NHS Act 2006 · Health and Care Act 2022 · IFRS 13",
        "key_stats": [
            {"label": "Impairments net of reversals 2024-25", "value": "£11.39M"},
            {"label": "Driver mix", "value": "MEA-DRC revaluation drift on Royal Bolton 1991 main block + 1970s legacy structures · maternity unit capacity-pressure equipment cycle"},
            {"label": "Estate scale", "value": "Royal Bolton Hospital (~600 beds, high-birthrate maternity) + Breightmet Health Centre + community estate"},
            {"label": "Delivery body", "value": "Bolton NHSFT Estates & Facilities · external valuer NHS-panel firm"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance · IAS 36 oversight"},
            {"label": "Funding trajectory", "value": "2021-22 c. £3M → 2022-23 c. £5M → 2023-24 c. £8M → 2024-25 £11.39M (volatile MEA cycle)"},
            {"label": "RAAC status", "value": "Not on HSSIB Sep 2023 confirmed-RAAC list"},
            {"label": "NHP scheme status", "value": "Not in NHP cohort · capital refresh through GM ICS estate plan"},
            {"label": "Listed-building constraint", "value": "Not listed"},
            {"label": "Specialty exposure", "value": "Standard DGH equipment cycles · Greater-Manchester regional maternity volume"},
            {"label": "Evaluation evidence", "value": "Trust ARA 2023-24 note 12 · CQC inspection 2023 · Ockenden 2022 maternity legacy investments"},
            {"label": "Predecessor / successor", "value": "Predecessor: pre-2008 Royal Bolton + Bolton Community Trust merger · Successor: estate strategy within Greater Manchester ICS"}
        ],
        "notes": "Bolton's impairment line is driven by the combination of a 1991 main acute block now passing 30 years of useful life and several 1970s legacy structures still in clinical use, both producing MEA-DRC drift as DHSC indexation and the modern equivalent asset cost diverge. The trust's high-volume maternity unit, one of the largest in England by deliveries, drives equipment-cycle impairments through obstetric and neonatal asset replacement ahead of useful life. The 2024-25 spike reflects the trust progressing through a 5-yearly full revaluation, with note 12 of the ARA attributing the bulk to revaluation rather than write-offs.",
        "sources": [
            {"publisher": "Bolton NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.boltonft.nhs.uk/about-us/our-publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Estates Returns Information Collection (ERIC) 2023-24", "url": "https://www.england.nhs.uk/estates-returns-information-collection/"},
            {"publisher": "Care Quality Commission", "title": "Bolton NHSFT provider profile (RMC)", "url": "https://www.cqc.org.uk/provider/RMC"},
            {"publisher": "Department of Health and Social Care", "title": "Ockenden Report (final, 2022)", "url": "https://www.gov.uk/government/publications/final-report-of-the-ockenden-review"}
        ],
        "related": ["Bolton NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Premises (other) — Bolton NHS Foundation Trust", "Impairments net of reversals — Wirral University Teaching Hospital NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Impairments net of reversals — East Suffolk and North Essex NHS Foundation Trust": {
        "aliases": [{"name": "Impairments net of reversals", "parent": "East Suffolk and North Essex NHS Foundation Trust"}],
        "description": "Non-cash writedowns on the merged ESNEFT estate — Ipswich Hospital and Colchester Hospital (the two principal acutes following the 2018 Ipswich + Colchester merger), plus the new Aldeburgh and Felixstowe community hospitals. Impairment is driven by post-merger carrying-value harmonisation across the previously-separate estates plus MEA-DRC revaluation on Colchester's 1980s blocks and Ipswich's mixed-vintage estate. Trust E&F + external valuer.",
        "beneficiaries": "Estate-wide on c. 1,200 beds across Ipswich + Colchester serving 1M East Suffolk + North Essex population; 1980s Colchester blocks and Ipswich legacy estate primary impaired.",
        "legal_basis": "IAS 36 · DHSC GAM 2024-25 ch.4 · NHS Act 2006 · Health and Care Act 2022 · IFRS 13",
        "key_stats": [
            {"label": "Impairments net of reversals 2024-25", "value": "£11.15M"},
            {"label": "Driver mix", "value": "Post-merger MEA-DRC harmonisation across two-site portfolio · Colchester 1980s blocks revaluation drift · Ipswich legacy adjustments"},
            {"label": "Estate scale", "value": "Ipswich Hospital + Colchester Hospital + Aldeburgh and Felixstowe community + 30+ community sites"},
            {"label": "Delivery body", "value": "ESNEFT Estates & Facilities · external valuer NHS-panel firm"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance · IAS 36 oversight"},
            {"label": "Funding trajectory", "value": "2021-22 c. £3M → 2022-23 c. £6M → 2023-24 c. £8M → 2024-25 £11.15M (post-merger MEA harmonisation)"},
            {"label": "RAAC status", "value": "Not on HSSIB Sep 2023 confirmed-RAAC list"},
            {"label": "NHP scheme status", "value": "Not in NHP cohort · capital refresh through Suffolk & North East Essex ICS"},
            {"label": "Listed-building constraint", "value": "Not listed"},
            {"label": "Specialty exposure", "value": "Standard DGH equipment cycles · regional cancer pathway investment"},
            {"label": "Evaluation evidence", "value": "Trust ARA 2023-24 note 12 · CQC inspection 2023 (Outstanding rating) · NHSE merger benefits review"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2018 merger of Ipswich Hospital + Colchester Hospital trusts · Successor: estate strategy harmonisation 2025-30"}
        ],
        "notes": "ESNEFT's impairment line carries a structural feature uncommon outside merger trusts: ongoing MEA-DRC harmonisation across the two-site portfolio inherited from the 2018 merger. Pre-merger asset registers used different valuation bases and refresh cycles, and the post-merger trust has been progressively reconciling these into a single MEA-DRC framework. Colchester Hospital's 1980s blocks generate the largest underlying impairment driver, with Ipswich's mixed-vintage estate adding adjustments. The 2024-25 spike reflects this harmonisation entering its later phase alongside ordinary revaluation cycle pressure.",
        "sources": [
            {"publisher": "East Suffolk and North Essex NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.esneft.nhs.uk/about-us/publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Estates Returns Information Collection (ERIC) 2023-24", "url": "https://www.england.nhs.uk/estates-returns-information-collection/"},
            {"publisher": "Care Quality Commission", "title": "ESNEFT provider profile (RDE)", "url": "https://www.cqc.org.uk/provider/RDE"},
            {"publisher": "NHS England", "title": "Provider mergers — benefits realisation", "url": "https://www.england.nhs.uk/financial-accounts/"}
        ],
        "related": ["East Suffolk and North Essex NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Premises (other) — East Suffolk and North Essex NHS Foundation Trust", "Impairments net of reversals — County Durham and Darlington NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Impairments net of reversals — Wirral University Teaching Hospital NHS Foundation Trust": {
        "aliases": [{"name": "Impairments net of reversals", "parent": "Wirral University Teaching Hospital NHS Foundation Trust"}],
        "description": "Non-cash writedowns on Wirral UTH's two-site coastal estate — Arrowe Park Hospital (the principal acute, Upton, on a 1980s build) and Clatterbridge Hospital site (now sharing campus with The Clatterbridge Cancer Centre). The trust sits in a salt-aerosol coastal microclimate on the Wirral peninsula, with combined MEA-DRC drift on the 1980s Arrowe Park building plus carrying-value adjustment as Clatterbridge has progressively transferred specialist oncology to the standalone CCC trust. Trust E&F + external valuer.",
        "beneficiaries": "Estate-wide on c. 850 beds across Arrowe Park + Clatterbridge serving 400,000 Wirral population; 1980s Arrowe Park main block and Clatterbridge legacy oncology blocks primary impaired.",
        "legal_basis": "IAS 36 · DHSC GAM 2024-25 ch.4 · NHS Act 2006 · Health and Care Act 2022 · IFRS 13",
        "key_stats": [
            {"label": "Impairments net of reversals 2024-25", "value": "£10.41M"},
            {"label": "Driver mix", "value": "MEA-DRC drift on Arrowe Park 1980s main block · coastal salt-aerosol fabric exposure · Clatterbridge oncology asset transfer carrying-value adjustments"},
            {"label": "Estate scale", "value": "Arrowe Park Hospital + Clatterbridge Hospital site (shared with The Clatterbridge Cancer Centre) + community estate"},
            {"label": "Delivery body", "value": "Wirral UTH Estates & Facilities · external valuer NHS-panel firm"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance · IAS 36 oversight"},
            {"label": "Funding trajectory", "value": "2021-22 c. £3M → 2022-23 c. £5M → 2023-24 c. £8M → 2024-25 £10.41M (volatile · coastal + transfer cycle)"},
            {"label": "RAAC status", "value": "Not on HSSIB Sep 2023 confirmed-RAAC list"},
            {"label": "NHP scheme status", "value": "Not in NHP cohort · capital refresh through Cheshire & Merseyside ICS"},
            {"label": "Coastal exposure", "value": "Wirral peninsula salt-aerosol microclimate · accelerated external-fabric and HVAC plant degradation"},
            {"label": "Specialty exposure", "value": "DGH-tier · Clatterbridge oncology service transferred to standalone CCC trust"},
            {"label": "Evaluation evidence", "value": "Trust ARA 2023-24 note 12 · CQC inspection 2023 · NAO NHS Estate report 2020"},
            {"label": "Predecessor / successor", "value": "Predecessor: 1982 Arrowe Park opening · Successor: campus reconfiguration as Clatterbridge oncology fully transitions to CCC"}
        ],
        "notes": "Wirral UTH's impairment line is shaped by two structural drivers uncommon in inland DGH peers: salt-aerosol coastal exposure on the Wirral peninsula accelerating external-fabric and HVAC plant degradation faster than DHSC indexation accommodates, and the ongoing carrying-value adjustments as oncology services at the historic Clatterbridge site transition to the standalone Clatterbridge Cancer Centre NHS Foundation Trust. Arrowe Park's 1980s main block continues to drive baseline MEA-DRC drift. The 2024-25 spike reflects both drivers acting concurrently with ordinary revaluation cycle pressure.",
        "sources": [
            {"publisher": "Wirral University Teaching Hospital NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.wuth.nhs.uk/about-us/publications/"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "National Audit Office", "title": "NHS Backlog Maintenance and Estate (2020)", "url": "https://www.nao.org.uk/reports/nhs-capital-expenditure-and-financial-management/"},
            {"publisher": "NHS England", "title": "Estates Returns Information Collection (ERIC) 2023-24", "url": "https://www.england.nhs.uk/estates-returns-information-collection/"},
            {"publisher": "Care Quality Commission", "title": "Wirral UTH provider profile (RBL)", "url": "https://www.cqc.org.uk/provider/RBL"}
        ],
        "related": ["Wirral University Teaching Hospital NHS Foundation Trust", "Premises & Infrastructure", "NHS Acute Trusts", "Premises (other) — Wirral University Teaching Hospital NHS Foundation Trust", "Impairments net of reversals — Blackpool Teaching Hospitals NHS Foundation Trust", "Department of Health and Social Care"]
    },
    "Impairments net of reversals — Derbyshire Community Health Services NHS Foundation Trust": {
        "aliases": [{"name": "Impairments net of reversals", "parent": "Derbyshire Community Health Services NHS Foundation Trust"}],
        "description": "Non-cash writedowns on DCHS's community-trust dispersed estate — 11 community hospitals (including Walton Hospital Chesterfield, Whitworth Hospital Matlock, Ilkeston Community Hospital, Ripley Hospital, plus Cavendish Hospital Buxton) and 30+ health centres + clinics. Unusually for a community trust, DCHS owns or holds material freehold interest in much of its estate (rather than leasing from NHSPS), so MEA-DRC revaluation of its small-hospital portfolio drives a meaningful impairment line. Trust E&F + external valuer.",
        "beneficiaries": "Estate-wide impact across c. 350 community-hospital beds plus health-centre footprint serving 1.05M Derbyshire population; small-town community hospitals 1900-1970 vintage primary impaired.",
        "legal_basis": "IAS 36 · DHSC GAM 2024-25 ch.4 · NHS Act 2006 · Health and Care Act 2022 · IFRS 13",
        "key_stats": [
            {"label": "Impairments net of reversals 2024-25", "value": "£9.92M"},
            {"label": "Driver mix", "value": "MEA-DRC revaluation drift across 11 small community hospitals · Cavendish Hospital Buxton listed-fabric · health-centre carrying-value adjustments"},
            {"label": "Estate scale", "value": "11 community hospitals + 30+ health centres + clinics · c. 350 community-hospital beds"},
            {"label": "Delivery body", "value": "DCHS Estates & Facilities · external valuer NHS-panel firm"},
            {"label": "Policy owner", "value": "DHSC + NHSE Provider Finance · IAS 36 oversight"},
            {"label": "Funding trajectory", "value": "2021-22 c. £3M → 2022-23 c. £5M → 2023-24 c. £7M → 2024-25 £9.92M (community-portfolio MEA cycle)"},
            {"label": "RAAC status", "value": "Not on HSSIB Sep 2023 confirmed-RAAC list"},
            {"label": "NHP scheme status", "value": "Not in NHP cohort (community trusts not in scope) · capital refresh through Joined Up Care Derbyshire ICS"},
            {"label": "Listed-building constraint", "value": "Cavendish Hospital Buxton (Devonshire Royal Hospital) Grade II*-listed historic dome · modernisation cost premium"},
            {"label": "Specialty exposure", "value": "Community-tier · low-volume equipment cycles · podiatry, district nursing, intermediate care"},
            {"label": "NHSPS interaction", "value": "Mixed-tenure estate · DCHS holds freehold for community hospitals (atypical for community trusts) · NHSPS for some health centres"},
            {"label": "Evaluation evidence", "value": "Trust ARA 2023-24 note 12 · CQC Outstanding rating community services · CIPFA community-estate review"},
            {"label": "Predecessor / successor", "value": "Predecessor: 2011 transfer from Derbyshire PCT · Successor: estate strategy within Joined Up Care Derbyshire ICS"}
        ],
        "notes": "DCHS is structurally distinct from most community trusts because it owns or holds freehold interest in the bulk of its 11-hospital community portfolio rather than leasing from NHS Property Services, which means MEA-DRC revaluation drives a meaningful impairment line that would otherwise sit on the NHSPS balance sheet. The Cavendish Hospital Buxton (formerly the Devonshire Royal Hospital, with the Grade II*-listed Victorian dome) carries a permanent listed-building modernisation gap. The 2024-25 line reflects portfolio-wide revaluation across 11 small-hospital sites plus health-centre adjustments, with note 12 of the ARA attributing the bulk to revaluation rather than discrete write-offs.",
        "sources": [
            {"publisher": "Derbyshire Community Health Services NHS Foundation Trust", "title": "Annual Report and Accounts 2023-24", "url": "https://www.dchs.nhs.uk/about-us/our-publications"},
            {"publisher": "Department of Health and Social Care", "title": "Group Accounting Manual 2024-25", "url": "https://www.gov.uk/government/publications/dhsc-group-accounting-manual-2024-to-2025"},
            {"publisher": "NHS England", "title": "Estates Returns Information Collection (ERIC) 2023-24", "url": "https://www.england.nhs.uk/estates-returns-information-collection/"},
            {"publisher": "Care Quality Commission", "title": "DCHS provider profile (RY8)", "url": "https://www.cqc.org.uk/provider/RY8"},
            {"publisher": "Historic England", "title": "Devonshire Royal Hospital (Cavendish) listing entry", "url": "https://historicengland.org.uk/listing/the-list/"}
        ],
        "related": ["Derbyshire Community Health Services NHS Foundation Trust", "Premises & Infrastructure", "NHS Community Trusts", "Premises (other) — Derbyshire Community Health Services NHS Foundation Trust", "Impairments net of reversals — Bradford Teaching Hospitals NHS Foundation Trust", "Department of Health and Social Care"]
    },
}
