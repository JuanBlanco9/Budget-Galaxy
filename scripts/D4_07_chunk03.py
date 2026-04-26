# -*- coding: utf-8 -*-
# D4_07 Premises (other) — chunk 03 (20 NHS trusts)
# Hand-curated trust-specific enrichment entries.

NEW = {
    "Premises (other) — South London and Maudsley NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "South London and Maudsley NHS Foundation Trust"}],
        "description": "Mental-health premises operating costs across SLaM's south-London estate — Maudsley Hospital (Denmark Hill), Bethlem Royal Hospital (Beckenham, 270-acre parkland), Lambeth Hospital (closure underway, services moving to Lambeth Mental Health Hub), and Ladywell Unit (Lewisham). Spend is shaped by the very large rural-style Bethlem estate and the long-running Lambeth decant.",
        "beneficiaries": "1.3M residents of Lambeth, Southwark, Lewisham and Croydon plus national specialist tertiary referrals (national psychosis, eating disorders, mother-and-baby unit, CAMHS).",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£29.72M"},
            {"label": "Share of trust total opex", "value": "c. 6%"},
            {"label": "Estate scale", "value": "4 main hospital sites + 60+ community/clinic sites · Bethlem 270 acres"},
            {"label": "Hard FM model", "value": "Mixed in-house Estates + specialist contractors"},
            {"label": "MH-specific", "value": "s.136 suites · PICU · MBU (mother-baby) · eating-disorder unit utilities"},
            {"label": "Lambeth Hospital", "value": "Decommissioning under way; new Lambeth Mental Health Hub on Kennington Lane in design"},
            {"label": "Net Zero milestone", "value": "Bethlem heat decarbonisation feasibility under PSDS; LED rollout"},
            {"label": "YoY change", "value": "c. +5-7% (energy + Lambeth decant temporary works)"},
            {"label": "Peer benchmark", "value": "Above MH-trust median per inpatient bed (Bethlem grounds + tertiary specialty mix)"}
        ],
        "notes": "SLaM's premises cost is structurally elevated by Bethlem's parkland (gardens, trees, perimeter security) and by the parallel running of Lambeth Hospital alongside the new MH hub design. The Maudsley itself is dense Victorian-to-modern build with KCL IoPPN co-location adding shared-services complexity. RAAC clearance survey 2024 cleared SLaM inpatient blocks.",
        "sources": [
            "https://slam.nhs.uk/about-us/our-publications",
            "https://www.england.nhs.uk/financial-accounts/",
            "https://www.salixfinance.co.uk/PSDS"
        ],
        "related": ["South London and Maudsley NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — University Hospitals of Derby and Burton NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "University Hospitals of Derby and Burton NHS Foundation Trust"}],
        "description": "Premises running costs across UHDB's two-acute-site estate post the 2018 merger — Royal Derby Hospital (Mickleover, ~2003 PFI new-build) and Queen's Hospital Burton, plus Florence Nightingale Community Hospital, London Road Community Hospital and Sir Robert Peel (Tamworth). Note: Royal Derby PFI unitary charges sit in D4_11, not here.",
        "beneficiaries": "1.1M+ catchment across southern Derbyshire and east Staffordshire — major emergency, maternity, and tertiary cancer services.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£28.81M"},
            {"label": "Share of trust total opex", "value": "c. 3%"},
            {"label": "Estate scale", "value": "2 acute hospitals + 3 community hospitals + ambulatory clinics"},
            {"label": "Hard FM model", "value": "Derby PFI services within PFI envelope; Burton + community in-house Estates"},
            {"label": "PFI footprint", "value": "Royal Derby PFI (Skanska/Catalyst) — unitary charge in D4_11"},
            {"label": "Burton estate", "value": "Queen's Hospital Burton 1990s build · backlog maintenance pressure"},
            {"label": "Net Zero milestone", "value": "PSDS-funded LED + heat-pump feasibility at Burton"},
            {"label": "YoY change", "value": "c. +5% (energy reset on non-PFI sites)"},
            {"label": "Peer benchmark", "value": "Below acute-trust median per m² (PFI absorbs much hard FM at Derby)"}
        ],
        "notes": "UHDB's Premises (other) line is moderated by the large Derby PFI envelope which captures the bulk of hard-FM, soft-FM, utilities and lifecycle within the unitary charge — leaving this line dominated by Burton + community sites. Burton has been a focus for backlog and decarbonisation feasibility post-merger. The 2018 Derby–Burton merger continues to generate estate-rationalisation work captured here.",
        "sources": [
            "https://www.uhdb.nhs.uk/publications",
            "https://www.england.nhs.uk/financial-accounts/",
            "https://www.salixfinance.co.uk/PSDS"
        ],
        "related": ["University Hospitals of Derby and Burton NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — Calderdale and Huddersfield NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Calderdale and Huddersfield NHS Foundation Trust"}],
        "description": "Premises running costs across CHFT's two-site estate — Calderdale Royal Hospital (Halifax, PFI new-build 2001) and Huddersfield Royal Infirmary (1960s-vintage RAAC-affected estate). The Hospitals of the Future programme (now NHP cohort) plans new builds at both, but Reset Jan 2025 has deferred timelines and extended life of the Huddersfield estate.",
        "beneficiaries": "470,000+ patients across Calderdale and Kirklees — A&E + maternity at Calderdale, planned care + acute at Huddersfield, plus community estate.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£28.76M"},
            {"label": "Share of trust total opex", "value": "c. 5%"},
            {"label": "Estate scale", "value": "2 acute hospitals + 4 community/clinic sites"},
            {"label": "Hard FM model", "value": "Calderdale PFI envelope; HRI in-house Estates"},
            {"label": "PFI footprint", "value": "Calderdale Royal PFI (Catalyst) — unitary charge in D4_11"},
            {"label": "RAAC status", "value": "Huddersfield Royal Infirmary HSSIB-listed RAAC site · mitigation works ongoing"},
            {"label": "NHP scheme status", "value": "New Calderdale + new Huddersfield (CHFT Hospitals of the Future) deferred under NHP Reset"},
            {"label": "Net Zero milestone", "value": "PSDS-funded LED + BMS works at HRI"},
            {"label": "YoY change", "value": "c. +6-8% (RAAC mitigation + energy)"},
            {"label": "Peer benchmark", "value": "Above acute median per m² at HRI (RAAC + age)"}
        ],
        "notes": "CHFT is one of the trusts most-exposed to the NHP Reset because both its acute sites are in the cohort and Huddersfield has confirmed RAAC. Reset deferral means continued RAAC props, monitoring, decant within Premises (other). Calderdale's PFI absorbs most of its hard-FM cost (in D4_11), so this line is disproportionately HRI-driven.",
        "sources": [
            "https://www.cht.nhs.uk/about-us/publications",
            "https://www.gov.uk/government/news/new-hospital-programme-update",
            "https://www.hssib.org.uk/patient-safety-investigations/raac-in-the-nhs/"
        ],
        "related": ["Calderdale and Huddersfield NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — East Kent Hospitals University NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "East Kent Hospitals University NHS Foundation Trust"}],
        "description": "Premises running costs across EKHUFT's three-acute-hospital estate — William Harvey Hospital (Ashford), Queen Elizabeth The Queen Mother Hospital (Margate, RAAC-affected), and Kent and Canterbury Hospital — plus Royal Victoria Hospital Folkestone, Buckland Hospital Dover, and community clinics. Spend is shaped by ageing 1970s tower-blocks and confirmed RAAC.",
        "beneficiaries": "750,000+ patients across east Kent — major emergency at WHH and QEQM, planned and specialty care at Canterbury, community at Folkestone/Dover.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£28.74M"},
            {"label": "Share of trust total opex", "value": "c. 3%"},
            {"label": "Estate scale", "value": "3 acute hospitals + 2 secondary hospitals + community clinics"},
            {"label": "Hard FM model", "value": "In-house Estates with specialist sub-contracts"},
            {"label": "RAAC status", "value": "QEQM Margate confirmed RAAC (HSSIB Sep 2023 list) · ongoing mitigation"},
            {"label": "Maternity context", "value": "Trust under sustained scrutiny post Kirkup 2022 · estate investment a CQC theme"},
            {"label": "Net Zero milestone", "value": "PSDS-funded heat works at WHH; LED rollout multi-site"},
            {"label": "YoY change", "value": "c. +6-8% (RAAC + energy)"},
            {"label": "Peer benchmark", "value": "Above acute-trust median per m² (estate age + RAAC)"}
        ],
        "notes": "EKHUFT carries one of the higher RAAC-mitigation operating burdens in the south-east, with QEQM Margate requiring continuous structural monitoring, props and decant. The trust's recovery from the Kirkup maternity review (2022) has placed estate condition under added regulatory focus. The NHP Reset deferred any single-site replacement, leaving the three-site model running with rising hard-FM costs.",
        "sources": [
            "https://www.ekhuft.nhs.uk/about-us/publications/",
            "https://www.hssib.org.uk/patient-safety-investigations/raac-in-the-nhs/",
            "https://www.gov.uk/government/news/new-hospital-programme-update"
        ],
        "related": ["East Kent Hospitals University NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — Dartford and Gravesham NHS Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Dartford and Gravesham NHS Trust"}],
        "description": "Premises running costs at Dartford and Gravesham — Darent Valley Hospital (Dartford, opened 2000 under one of the earliest NHS PFI deals) plus Gravesham Community Hospital and Erith Hospital. The Premises (other) line is unusually shaped because the Darent Valley PFI bundles hard FM into the unitary charge, so non-PFI premises spend is concentrated on community estate and PFI variations.",
        "beneficiaries": "500,000+ patients across north Kent and southern Bexley — A&E, maternity, planned care at Darent Valley; rehabilitation and outpatients at community sites.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£28.70M"},
            {"label": "Share of trust total opex", "value": "c. 7%"},
            {"label": "Estate scale", "value": "1 acute (Darent Valley · 463 beds) + 2 community hospitals"},
            {"label": "Hard FM model", "value": "PFI partner Hospital Company (Dartford) Ltd · Carillion successor"},
            {"label": "PFI footprint", "value": "Darent Valley PFI unitary charge in D4_11 — variations + non-PFI sites here"},
            {"label": "PFI expiry", "value": "2031 — handback planning live"},
            {"label": "Net Zero milestone", "value": "PFI-led BMS + LED programme; constrained by PFI variation pricing"},
            {"label": "YoY change", "value": "c. +5% (energy + PFI variations)"},
            {"label": "Peer benchmark", "value": "High % of opex due to small trust scale"}
        ],
        "notes": "Dartford's Premises (other) line is materially shaped by the legacy 2000 PFI — handback in 2031 is now a live planning issue, with condition surveys and dilapidations work starting to appear in operating spend. Carillion's 2018 collapse forced re-letting of FM sub-contracts within the PFI, indirectly pushing some costs into this line. Community-hospital backlog is a board-level concern.",
        "sources": [
            "https://www.dgt.nhs.uk/about-us/publications",
            "https://www.england.nhs.uk/financial-accounts/",
            "https://www.nao.org.uk/reports/managing-pfi-assets-and-services-as-contracts-end/"
        ],
        "related": ["Dartford and Gravesham NHS Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — East Lancashire Hospitals NHS Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "East Lancashire Hospitals NHS Trust"}],
        "description": "Premises running costs across ELHT's multi-site estate — Royal Blackburn Teaching Hospital (the trust's principal acute site, with significant 2006 build), Burnley General Teaching Hospital, Pendle Community Hospital, Clitheroe Community Hospital and Accrington Victoria. Estate operating costs are weighted toward Royal Blackburn's emergency centre and Burnley's specialist women and newborn block.",
        "beneficiaries": "550,000+ patients across East Lancashire and Ribble Valley — major emergency + critical care at Blackburn, women & newborn + day surgery at Burnley, rehabilitation at community sites.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£28.04M"},
            {"label": "Share of trust total opex", "value": "c. 4%"},
            {"label": "Estate scale", "value": "2 acute teaching hospitals + 3 community hospitals"},
            {"label": "Hard FM model", "value": "In-house Estates with specialist sub-contracts (no acute PFI)"},
            {"label": "Royal Blackburn", "value": "Emergency Care Centre opened 2006 · ongoing reconfiguration spend"},
            {"label": "Burnley General", "value": "Mix of legacy + new women & newborn block"},
            {"label": "Net Zero milestone", "value": "Salix / PSDS heat decarbonisation grant works at Royal Blackburn"},
            {"label": "YoY change", "value": "c. +5-7% (energy reset + soft-FM uplift)"},
            {"label": "Peer benchmark", "value": "Mid-range vs north-west acute peers"}
        ],
        "notes": "ELHT's premises spend reflects a mature estate with no major PFI burden — meaning hard FM, utilities and soft FM all flow through this line rather than being captured in unitary charges. The trust has been a regular Salix / PSDS grant recipient for heat decarbonisation works at Royal Blackburn. The 2024-25 uplift reflects RM6011 energy renewal pricing and 5-7% construction inflation feeding into hard-FM contracts.",
        "sources": [
            "https://elht.nhs.uk/about-us/publications",
            "https://www.salixfinance.co.uk/PSDS",
            "https://www.england.nhs.uk/financial-accounts/"
        ],
        "related": ["East Lancashire Hospitals NHS Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — South Tyneside and Sunderland NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "South Tyneside and Sunderland NHS Foundation Trust"}],
        "description": "Premises running costs across the post-2019 merged STSFT estate — Sunderland Royal Hospital (the trust's principal acute centre), South Tyneside District Hospital (South Shields), Sunderland Eye Infirmary and a community footprint. The merger drove an estate-rationalisation programme (Path to Excellence) shifting acute services between sites, with operating-cost implications visible in this line.",
        "beneficiaries": "450,000+ patients across Sunderland and South Tyneside — major emergency + maternity at Sunderland, urgent care + planned services at South Tyneside, regional ophthalmology at the Eye Infirmary.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£27.76M"},
            {"label": "Share of trust total opex", "value": "c. 4%"},
            {"label": "Estate scale", "value": "2 acute hospitals + Sunderland Eye Infirmary + community sites"},
            {"label": "Hard FM model", "value": "In-house Estates (no acute PFI)"},
            {"label": "Reconfiguration", "value": "Path to Excellence Phase 2 — stroke/maternity centralisation at Sunderland"},
            {"label": "Sunderland Eye Infirmary", "value": "Specialist single-site ophthalmology · listed status feeds into estate cost"},
            {"label": "Net Zero milestone", "value": "PSDS-funded heat-pump feasibility at South Tyneside"},
            {"label": "YoY change", "value": "c. +5% (energy + reconfiguration decant)"},
            {"label": "Peer benchmark", "value": "Mid-range vs north-east acute peers"}
        ],
        "notes": "STSFT's premises cost is shaped by the dual challenge of Path to Excellence reconfiguration (decant + temporary works as services move) and the unusual single-specialty Sunderland Eye Infirmary site. The 2024-25 uplift reflects energy reset and 5-7% hard-FM inflation. South Tyneside's ageing estate carries higher per-m² operating cost than Sunderland.",
        "sources": [
            "https://www.stsft.nhs.uk/about-us/our-publications",
            "https://pathtoexcellence.org.uk/",
            "https://www.england.nhs.uk/financial-accounts/"
        ],
        "related": ["South Tyneside and Sunderland NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — University Hospitals of North Midlands NHS Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "University Hospitals of North Midlands NHS Trust"}],
        "description": "Premises running costs across UHNM's two-site estate — Royal Stoke University Hospital (a 1,200-bed PFI-redeveloped site, one of England's largest single-site acute hospitals) and County Hospital Stafford. The Royal Stoke PFI absorbs most hard-FM and soft-FM into D4_11, so Premises (other) is dominated by County Hospital, satellite estate and PFI variations.",
        "beneficiaries": "3M+ catchment across Staffordshire, Cheshire, Shropshire and beyond — major trauma, regional cardiothoracic, neurosurgery, and tertiary specialties at Royal Stoke.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£27.74M"},
            {"label": "Share of trust total opex", "value": "c. 2%"},
            {"label": "Estate scale", "value": "2 acute hospitals (Royal Stoke 1,200 beds + County Stafford)"},
            {"label": "Hard FM model", "value": "Royal Stoke under PFI envelope · County in-house Estates"},
            {"label": "PFI footprint", "value": "Royal Stoke PFI (Project Co — Vinci/Equitix) — unitary charge in D4_11"},
            {"label": "Trauma centre", "value": "Major Trauma Centre · 24/7 utilities resilience requirements"},
            {"label": "Net Zero milestone", "value": "Heat decarbonisation feasibility at County · LED rollout"},
            {"label": "YoY change", "value": "c. +5% (energy + PFI variations)"},
            {"label": "Peer benchmark", "value": "Below large-acute median per m² (PFI carries hard FM)"}
        ],
        "notes": "UHNM's low Premises (other) ratio relative to its scale reflects how much of its operating estate cost is captured inside the Royal Stoke PFI unitary charge. Real estate-management focus has been on County Hospital Stafford backlog and the residual 28% post-PFI estate at Royal Stoke. Trauma-centre requirements drive resilience upgrades (gensets, ICU power, oxygen plant) that hit this line at the non-PFI margins.",
        "sources": [
            "https://www.uhnm.nhs.uk/about-us/publications/",
            "https://www.england.nhs.uk/financial-accounts/",
            "https://www.nao.org.uk/reports/managing-pfi-assets-and-services-as-contracts-end/"
        ],
        "related": ["University Hospitals of North Midlands NHS Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — University Hospitals Coventry And Warwickshire NHS Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "University Hospitals Coventry And Warwickshire NHS Trust"}],
        "description": "Premises running costs at UHCW — University Hospital Coventry (the principal acute site, a 2006 PFI redevelopment under one of the largest NHS PFI deals) and the Hospital of St Cross in Rugby. The Coventry PFI envelope captures the majority of hard FM, soft FM and lifecycle into the unitary charge (D4_11), leaving Premises (other) dominated by Rugby, satellite estate and PFI variations.",
        "beneficiaries": "1M+ catchment across Coventry, Warwickshire and beyond — major trauma, tertiary cardiology, kidney and stem-cell transplant services.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£27.67M"},
            {"label": "Share of trust total opex", "value": "c. 2%"},
            {"label": "Estate scale", "value": "1 acute (UHCW Coventry) + Hospital of St Cross Rugby + clinical research facility"},
            {"label": "Hard FM model", "value": "Coventry PFI envelope · St Cross in-house Estates"},
            {"label": "PFI footprint", "value": "UHCW PFI (Project Co — Skanska/Innisfree) — unitary charge in D4_11"},
            {"label": "PFI expiry", "value": "2042 — handback distant"},
            {"label": "Major trauma", "value": "Major Trauma Centre · 24/7 power and oxygen resilience drivers"},
            {"label": "Net Zero milestone", "value": "PSDS-funded heat works at St Cross Rugby"},
            {"label": "YoY change", "value": "c. +5% (energy + PFI variations)"},
            {"label": "Peer benchmark", "value": "Below acute median per m² (PFI absorbs hard FM)"}
        ],
        "notes": "UHCW's relatively low Premises (other) line reflects the dominance of one of England's largest acute PFI envelopes (Coventry, ~£280M+ unitary charge in D4_11). Estate-management attention sits on St Cross Rugby and clinical-research facility additions, plus PFI variations as service patterns evolve. RM6011 energy reset feeds the YoY uplift on non-PFI sites.",
        "sources": [
            "https://www.uhcw.nhs.uk/about-us/publications/",
            "https://www.england.nhs.uk/financial-accounts/",
            "https://www.salixfinance.co.uk/PSDS"
        ],
        "related": ["University Hospitals Coventry And Warwickshire NHS Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — Royal Devon University Healthcare NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Royal Devon University Healthcare NHS Foundation Trust"}],
        "description": "Premises running costs across the merged Royal Devon estate (post 2022 RD&E + Northern Devon merger) — Royal Devon and Exeter Hospital (Wonford, Exeter), North Devon District Hospital (Barnstaple, RAAC-affected and an NHP cohort scheme), plus Honiton, Tiverton, Sidmouth, Exmouth, Okehampton and Holsworthy community hospitals. Among the largest geographic estate footprints in England.",
        "beneficiaries": "615,000+ patients across Devon — major emergency at Exeter, rural acute at Barnstaple, plus an extensive 17-community-hospital network.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£27.33M"},
            {"label": "Share of trust total opex", "value": "c. 3%"},
            {"label": "Estate scale", "value": "2 acute + 17 community hospitals · very large rural footprint"},
            {"label": "Hard FM model", "value": "In-house Estates with specialist sub-contracts"},
            {"label": "RAAC status", "value": "North Devon District Hospital confirmed RAAC (HSSIB Sep 2023) · ongoing mitigation"},
            {"label": "NHP scheme status", "value": "NDDH replacement in NHP cohort · Reset Jan 2025 deferred timeline"},
            {"label": "Rural premium", "value": "17 community sites carry travel/grounds/winter-resilience costs"},
            {"label": "Net Zero milestone", "value": "PSDS-funded heat works · LED rollout multi-site"},
            {"label": "YoY change", "value": "c. +6% (RAAC + energy)"},
            {"label": "Peer benchmark", "value": "Above acute median per site (rural dispersion + RAAC)"}
        ],
        "notes": "Royal Devon's Premises (other) line carries a double burden — RAAC mitigation at Barnstaple and operating-cost overhead from one of the longest community-hospital estates in NHS England (17 sites). The NHP Reset deferred any imminent transition to a new NDDH, leaving extending operating life of an at-risk concrete frame. The 2022 merger continues to drive estate-rationalisation work captured here.",
        "sources": [
            "https://www.royaldevon.nhs.uk/about-us/publications/",
            "https://www.hssib.org.uk/patient-safety-investigations/raac-in-the-nhs/",
            "https://www.gov.uk/government/news/new-hospital-programme-update"
        ],
        "related": ["Royal Devon University Healthcare NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — University Hospitals Plymouth NHS Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "University Hospitals Plymouth NHS Trust"}],
        "description": "Premises running costs at UHP — Derriford Hospital (Plymouth's single principal acute site, 1981-vintage with subsequent additions), the Royal Eye Infirmary, and a network of community/outreach clinics across south-west Devon and east Cornwall. Spend is shaped by Derriford's ageing infrastructure and the trust's status as the south-west peninsula's only major trauma centre.",
        "beneficiaries": "2M+ peninsula catchment (Devon + Cornwall) — major trauma, neurosurgery, cardiothoracic, regional cancer, plus military medicine (NHS-MOD relationship).",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£27.25M"},
            {"label": "Share of trust total opex", "value": "c. 3%"},
            {"label": "Estate scale", "value": "1 acute (Derriford ~1,000 beds) + Royal Eye Infirmary + 12 community sites"},
            {"label": "Hard FM model", "value": "In-house Estates with specialist sub-contracts"},
            {"label": "Major trauma", "value": "Sole peninsula MTC · 24/7 utility + helipad resilience drivers"},
            {"label": "Backlog maintenance", "value": "Among highest absolute backlog in south-west (NHS ERIC return)"},
            {"label": "NHP scheme status", "value": "Derriford redevelopment deferred under Reset; MOD partnership site work continues"},
            {"label": "Net Zero milestone", "value": "PSDS-funded heat-pump feasibility at Derriford"},
            {"label": "YoY change", "value": "c. +6% (backlog + energy)"},
            {"label": "Peer benchmark", "value": "Above acute median per m² (estate age + MTC resilience requirements)"}
        ],
        "notes": "Plymouth's Derriford carries a high backlog-maintenance burden reported repeatedly in NHS ERIC returns, with ageing tower-block plant rooms requiring ongoing intervention. The MTC role drives elevated standby-power, oxygen and helipad-resilience costs which all hit this line. NHP Reset deferred the planned Derriford redevelopment, extending operating life of fabric scheduled to be replaced.",
        "sources": [
            "https://www.plymouthhospitals.nhs.uk/publications",
            "https://www.england.nhs.uk/estates-returns-information-collection/",
            "https://www.gov.uk/government/news/new-hospital-programme-update"
        ],
        "related": ["University Hospitals Plymouth NHS Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — St George's University Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "St George's University Hospitals NHS Foundation Trust"}],
        "description": "Premises running costs at St George's — the Tooting site (St George's Hospital, an extensive multi-decade central-Tooting estate with the Lanesborough Wing tower and Atkinson Morley wing for neurosciences) and Queen Mary's Hospital Roehampton. Now part of the GESH (St George's, Epsom and St Helier) group, with shared corporate estate functions emerging.",
        "beneficiaries": "1.3M+ south-west London catchment plus tertiary referrals — major trauma, hyperacute stroke, cardiothoracic, neurosciences and one of England's largest infection-isolation centres.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£27.21M"},
            {"label": "Share of trust total opex", "value": "c. 3%"},
            {"label": "Estate scale", "value": "St George's Tooting + Queen Mary's Roehampton + community clinics"},
            {"label": "Hard FM model", "value": "In-house Estates with specialist contractors (no acute PFI)"},
            {"label": "Lanesborough Wing", "value": "1980 multi-storey tower · ageing fabric and lift/MEP refresh pressure"},
            {"label": "GESH group", "value": "Operating in group with Epsom and St Helier · shared estate strategy emerging"},
            {"label": "HCID centre", "value": "High Consequence Infectious Diseases unit · resilient HVAC drives utilities cost"},
            {"label": "Net Zero milestone", "value": "PSDS heat-pump feasibility at Tooting · LED programme rolling"},
            {"label": "YoY change", "value": "c. +5-7% (energy + ageing-tower MEP)"},
            {"label": "Peer benchmark", "value": "Mid-range vs London teaching peers per m²"}
        ],
        "notes": "St George's premises spend reflects an ageing 1970s-80s tower estate (Lanesborough) where MEP refresh is a perennial requirement, plus the running cost of HCID-grade isolation HVAC (one of England's tertiary centres for high-consequence pathogens). GESH group formation with Epsom and St Helier has begun yielding shared estate roles, though the cost effects are slow.",
        "sources": [
            "https://www.stgeorges.nhs.uk/about/publications/",
            "https://www.england.nhs.uk/financial-accounts/",
            "https://www.salixfinance.co.uk/PSDS"
        ],
        "related": ["St George's University Hospitals NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — Norfolk and Norwich University Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Norfolk and Norwich University Hospitals NHS Foundation Trust"}],
        "description": "Premises running costs at NNUH — Norfolk and Norwich University Hospital (a 2001 single-site PFI build at Colney, one of the earliest and best-known NHS PFI deals) plus Cromer Hospital. The PFI envelope captures hard FM, soft FM and lifecycle into the D4_11 unitary charge, with Premises (other) covering Cromer, satellites and PFI variations — but NNUH is also a confirmed RAAC site.",
        "beneficiaries": "1M+ Norfolk and north Suffolk catchment — major emergency, regional cancer, and University of East Anglia teaching partnership.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£26.91M"},
            {"label": "Share of trust total opex", "value": "c. 3%"},
            {"label": "Estate scale", "value": "1 acute (NNUH Colney ~1,000 beds) + Cromer Hospital + clinics"},
            {"label": "Hard FM model", "value": "PFI partner Octagon Healthcare · soft FM Serco within PFI"},
            {"label": "PFI footprint", "value": "NNUH PFI unitary charge in D4_11 — variations + non-PFI sites here"},
            {"label": "PFI expiry", "value": "2037 — handback planning starting"},
            {"label": "RAAC status", "value": "RAAC confirmed in NNUH plant rooms / non-clinical (HSSIB list) · mitigation works ongoing"},
            {"label": "Net Zero milestone", "value": "PFI-led BMS upgrades · constrained by PFI variation pricing"},
            {"label": "YoY change", "value": "c. +6% (RAAC + energy + PFI variations)"},
            {"label": "Peer benchmark", "value": "Below acute median per m² (PFI absorbs hard FM)"}
        ],
        "notes": "NNUH is unusual in being both a major PFI hospital and a confirmed RAAC site — meaning RAAC mitigation work has involved complex commercial discussions with the PFI partner over which entity bears the cost. Some mitigation works flow through Premises (other) as variations or trust-borne items. PFI handback in 2037 is an emerging board-level planning theme.",
        "sources": [
            "https://www.nnuh.nhs.uk/publication-scheme/",
            "https://www.hssib.org.uk/patient-safety-investigations/raac-in-the-nhs/",
            "https://www.nao.org.uk/reports/managing-pfi-assets-and-services-as-contracts-end/"
        ],
        "related": ["Norfolk and Norwich University Hospitals NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — United Lincolnshire Hospitals NHS Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "United Lincolnshire Hospitals NHS Trust"}],
        "description": "Premises running costs across ULHT's geographically dispersed estate — Lincoln County Hospital, Pilgrim Hospital Boston, Grantham and District Hospital, plus Louth and Skegness sites. Among the largest geographic acute footprints in England, with significant rural-resilience cost. Long-running 'Acute Services Review' has shaped estate planning for over a decade.",
        "beneficiaries": "750,000+ patients across Lincolnshire — major emergency at Lincoln + Boston, planned care at Grantham, rural acute and community at smaller sites.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£26.80M"},
            {"label": "Share of trust total opex", "value": "c. 4%"},
            {"label": "Estate scale", "value": "3 main acute + 2 secondary acute hospitals · large rural footprint"},
            {"label": "Hard FM model", "value": "In-house Estates (no acute PFI)"},
            {"label": "Pilgrim Boston", "value": "Coastal location · saline-air corrosion drives premium hard-FM cost"},
            {"label": "Grantham", "value": "A&E reconfiguration ongoing · estate decant pressure"},
            {"label": "NHP scheme status", "value": "Lincoln + Boston in NHP pipeline · Reset Jan 2025 deferred"},
            {"label": "Net Zero milestone", "value": "PSDS heat works at Lincoln County · LED rollout"},
            {"label": "YoY change", "value": "c. +6-7% (energy + dispersed-estate uplift)"},
            {"label": "Peer benchmark", "value": "Above acute median per site (rural dispersion)"}
        ],
        "notes": "ULHT's premises cost is structurally elevated by one of NHS England's largest geographic acute footprints, multi-decade Acute Services Review uncertainty, and the corrosion-driven hard-FM premium at coastal Pilgrim Boston. The NHP Reset deferred the planned Lincoln/Boston rebuilds, extending operating life of estate that was scheduled for replacement. Grantham A&E reconfiguration continues to drive decant cost.",
        "sources": [
            "https://www.ulh.nhs.uk/about/publications/",
            "https://www.gov.uk/government/news/new-hospital-programme-update",
            "https://www.england.nhs.uk/financial-accounts/"
        ],
        "related": ["United Lincolnshire Hospitals NHS Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — South Tees Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "South Tees Hospitals NHS Foundation Trust"}],
        "description": "Premises running costs across South Tees — James Cook University Hospital (Middlesbrough, the principal acute and major trauma centre for the north-east) and the Friarage Hospital (Northallerton, smaller-acute estate post 2019 reconfiguration). Premises spend is weighted to James Cook's tertiary services and 24/7 trauma resilience.",
        "beneficiaries": "1.5M+ catchment across Tees Valley + North Yorkshire — major trauma, regional cardiothoracic, neurosurgery, vascular and spinal services at James Cook; rural acute at Friarage.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£26.71M"},
            {"label": "Share of trust total opex", "value": "c. 3%"},
            {"label": "Estate scale", "value": "1 acute MTC (James Cook ~1,000 beds) + Friarage Hospital + community clinics"},
            {"label": "Hard FM model", "value": "PFI envelope at James Cook · Friarage in-house Estates"},
            {"label": "PFI footprint", "value": "James Cook PFI (Endeavour Healthcare) — unitary charge in D4_11"},
            {"label": "Major trauma", "value": "Regional MTC · 24/7 power, oxygen, helipad-resilience drivers"},
            {"label": "Friarage reconfiguration", "value": "A&E to urgent care 2019 · estate footprint adjustments ongoing"},
            {"label": "Net Zero milestone", "value": "PSDS heat works at Friarage · PFI-led BMS at James Cook"},
            {"label": "YoY change", "value": "c. +5% (energy + PFI variations)"},
            {"label": "Peer benchmark", "value": "Below acute median per m² at MTC (PFI absorbs hard FM)"}
        ],
        "notes": "South Tees' Premises (other) line is shaped by the split between PFI-bundled hard FM at James Cook (in D4_11) and in-house Estates at Friarage. The Friarage A&E to urgent-treatment-centre conversion (2019) continues to ripple through estate-utilisation costs. James Cook's MTC resilience requirements drive elevated standby-power and oxygen-plant operating costs at the PFI-trust margin.",
        "sources": [
            "https://www.southtees.nhs.uk/about/publications/",
            "https://www.england.nhs.uk/financial-accounts/",
            "https://www.salixfinance.co.uk/PSDS"
        ],
        "related": ["South Tees Hospitals NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — County Durham and Darlington NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "County Durham and Darlington NHS Foundation Trust"}],
        "description": "Premises running costs across CDDFT's distinctive multi-site estate — University Hospital of North Durham (Durham), Darlington Memorial Hospital, Bishop Auckland Hospital, plus Shotley Bridge, Chester-le-Street, Sedgefield and other community hospitals. Among NHS England's most-multi-site acute trusts, with significant rural and small-acute estate.",
        "beneficiaries": "650,000+ patients across County Durham and Darlington — major emergency at Durham + Darlington, planned care at Bishop Auckland, community and rehabilitation at smaller sites.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£26.21M"},
            {"label": "Share of trust total opex", "value": "c. 4%"},
            {"label": "Estate scale", "value": "2 acute + 1 elective + 4-5 community hospitals · large rural footprint"},
            {"label": "Hard FM model", "value": "Mixed: Bishop Auckland PFI envelope + in-house Estates elsewhere"},
            {"label": "PFI footprint", "value": "Bishop Auckland PFI (Catalyst) — unitary charge in D4_11"},
            {"label": "Estate consolidation", "value": "Ongoing rationalisation of small community-hospital footprint"},
            {"label": "Net Zero milestone", "value": "PSDS heat works at Durham + Darlington · LED rollout multi-site"},
            {"label": "YoY change", "value": "c. +5-7% (rural premium + energy)"},
            {"label": "Peer benchmark", "value": "Above acute median per site (multi-site dispersion)"}
        ],
        "notes": "CDDFT's premises cost is structurally elevated by one of the highest site-counts in NHS acute estate, mixing small community hospitals (Shotley Bridge, Chester-le-Street, Sedgefield) with two main acutes and a PFI elective site at Bishop Auckland. Estate-rationalisation pressure has been a perennial board theme but politically constrained. Rural winter resilience adds material cost.",
        "sources": [
            "https://www.cddft.nhs.uk/about-us/publications.aspx",
            "https://www.england.nhs.uk/financial-accounts/",
            "https://www.salixfinance.co.uk/PSDS"
        ],
        "related": ["County Durham and Darlington NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — York and Scarborough Teaching Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "York and Scarborough Teaching Hospitals NHS Foundation Trust"}],
        "description": "Premises running costs across YSTHFT — York Hospital, Scarborough General Hospital (a remote coastal acute), Bridlington Hospital, plus Selby, Malton, Whitby and other community hospitals. The York–Scarborough geography is one of the most-stretched acute footprints in England (50+ miles between main sites), with associated travel, logistics and resilience costs.",
        "beneficiaries": "800,000+ patients across North Yorkshire and the East Riding — emergency + maternity at York and Scarborough, community and rehabilitation at smaller sites.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£25.74M"},
            {"label": "Share of trust total opex", "value": "c. 4%"},
            {"label": "Estate scale", "value": "2 main acute + 5+ community hospitals · 50-mile site separation"},
            {"label": "Hard FM model", "value": "In-house Estates with specialist sub-contracts"},
            {"label": "Scarborough coastal", "value": "Saline-air corrosion drives premium hard-FM cost · rural acute resilience"},
            {"label": "Estate condition", "value": "Both main sites have HSSIB-recognised structural concerns / backlog"},
            {"label": "NHP scheme status", "value": "Scarborough not in NHP cohort · trust pursuing capital business cases"},
            {"label": "Net Zero milestone", "value": "PSDS heat works at York · LED rollout multi-site"},
            {"label": "YoY change", "value": "c. +5-7% (coastal premium + energy)"},
            {"label": "Peer benchmark", "value": "Above acute median per m² (dispersion + coastal)"}
        ],
        "notes": "YSTHFT's premises cost is shaped by one of NHS England's most geographically-stretched acute footprints — Scarborough's coastal exposure adds 5-10% hard-FM premium versus inland equivalents (saline corrosion of MEP, building fabric). Backlog maintenance at both main sites is a persistent board-level concern. Without an NHP slot, capital recovery falls on operating spend captured here.",
        "sources": [
            "https://www.yorkhospitals.nhs.uk/about-us/publications/",
            "https://www.england.nhs.uk/financial-accounts/",
            "https://www.salixfinance.co.uk/PSDS"
        ],
        "related": ["York and Scarborough Teaching Hospitals NHS Foundation Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — Leicestershire Partnership NHS Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Leicestershire Partnership NHS Trust"}],
        "description": "Mental-health and community premises operating costs across LPT's Leicester, Leicestershire and Rutland estate — Bradgate Mental Health Unit (Glenfield Hospital site), Agnes Unit, Beaumont Ward (CAMHS), Coalville Community Hospital, Loughborough Hospital, Melton Mowbray, Rutland Memorial Hospital, plus extensive community-clinic estate.",
        "beneficiaries": "1.1M residents of Leicester + Leicestershire + Rutland — adult acute MH inpatients, CAMHS, learning disability, older-people's MH, community physical-health services.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Mental Health Act 1983 (s.136 places of safety) · Health and Care Act 2022 · CQC Reg 15",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£25.72M"},
            {"label": "Share of trust total opex", "value": "c. 6%"},
            {"label": "Estate scale", "value": "Bradgate MH unit + 5+ community hospitals + 100+ community clinic sites"},
            {"label": "Hard FM model", "value": "Mixed in-house + UHL shared services on co-located sites"},
            {"label": "MH-specific", "value": "s.136 suites · PICU · CAMHS Beaumont Ward · LD inpatient utilities"},
            {"label": "Bradgate Unit", "value": "Repeated CQC concerns on environment · refurbishment programme"},
            {"label": "Net Zero milestone", "value": "PSDS heat works at Coalville + Loughborough · LED community rollout"},
            {"label": "YoY change", "value": "c. +5-6% (energy + Bradgate environmental works)"},
            {"label": "Peer benchmark", "value": "Above MH median per inpatient bed (community-hospital footprint)"}
        ],
        "notes": "LPT's premises spend is unusual among MH trusts in carrying a substantial community-hospital estate (Coalville, Loughborough, Melton, Rutland, Hinckley, Market Harborough) inherited from PCT-era reorganisation. The Bradgate MH Unit has been the subject of repeated CQC concerns about environment and ligature risk, driving capital and operating spend. Co-location with UHL at Glenfield brings shared estate-services cost.",
        "sources": [
            "https://www.leicspart.nhs.uk/about/our-publications/",
            "https://www.england.nhs.uk/financial-accounts/",
            "https://www.cqc.org.uk/provider/RT5"
        ],
        "related": ["Leicestershire Partnership NHS Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — East Sussex Healthcare NHS Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "East Sussex Healthcare NHS Trust"}],
        "description": "Premises running costs across ESHT's two-acute estate — Conquest Hospital (Hastings) and Eastbourne District General Hospital — plus Bexhill Hospital, Uckfield Community Hospital, Crowborough Birth Centre, Rye Memorial Care Centre and others. ESHT is unusual in operating an integrated acute + community model with substantial small-hospital estate.",
        "beneficiaries": "525,000+ patients across East Sussex — A&E + maternity at Conquest and Eastbourne, planned and community care across smaller sites.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£25.70M"},
            {"label": "Share of trust total opex", "value": "c. 4%"},
            {"label": "Estate scale", "value": "2 acute + 5+ community hospitals · coastal + rural mix"},
            {"label": "Hard FM model", "value": "In-house Estates with specialist sub-contracts (no acute PFI)"},
            {"label": "Coastal corrosion", "value": "Conquest + Eastbourne both coastal · saline-air premium on hard FM"},
            {"label": "Estate age", "value": "Eastbourne DGH 1970s + Conquest 1980s vintage · backlog pressure"},
            {"label": "Net Zero milestone", "value": "PSDS heat works at Eastbourne · LED multi-site"},
            {"label": "YoY change", "value": "c. +6% (coastal premium + energy)"},
            {"label": "Peer benchmark", "value": "Above acute median per m² (estate age + coastal + multi-site)"}
        ],
        "notes": "ESHT's premises cost is shaped by the dual coastal exposure of both main acutes (saline-air corrosion drives 5-10% MEP premium), 1970s-80s build vintage with persistent backlog, and an integrated acute + community model that adds small-site overhead. Without an NHP slot, capital recovery falls on operating spend. Recent CQC inspections have flagged premises issues at multiple sites.",
        "sources": [
            "https://www.esht.nhs.uk/about-us/publications/",
            "https://www.england.nhs.uk/financial-accounts/",
            "https://www.cqc.org.uk/provider/RXC"
        ],
        "related": ["East Sussex Healthcare NHS Trust", "Premises & Infrastructure"]
    },
    "Premises (other) — Doncaster and Bassetlaw Teaching Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Premises (other)", "parent": "Doncaster and Bassetlaw Teaching Hospitals NHS Foundation Trust"}],
        "description": "Premises running costs across DBTH — Doncaster Royal Infirmary (the principal acute), Bassetlaw Hospital (Worksop), Montagu Hospital (Mexborough) and Retford Hospital. The trust spans two ICS footprints (South Yorkshire + Nottinghamshire) which adds estate-strategy complexity.",
        "beneficiaries": "420,000+ patients across Doncaster and north Nottinghamshire — major emergency at DRI, planned care + maternity at Bassetlaw, rehabilitation at Montagu and Retford.",
        "legal_basis": "NHS GAM 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Estates Code · CQC Reg 15",
        "key_stats": [
            {"label": "Premises (other) 2024-25", "value": "£24.43M"},
            {"label": "Share of trust total opex", "value": "c. 4%"},
            {"label": "Estate scale", "value": "2 acute hospitals + 2 community hospitals · cross-ICS footprint"},
            {"label": "Hard FM model", "value": "In-house Estates with specialist sub-contracts (no acute PFI)"},
            {"label": "DRI estate", "value": "1930s-onwards multi-vintage · ongoing backlog and ward-block refurbishment"},
            {"label": "Bassetlaw", "value": "Smaller-acute estate · CQC has raised ward-environment concerns historically"},
            {"label": "Net Zero milestone", "value": "PSDS heat works at DRI · LED rollout multi-site"},
            {"label": "YoY change", "value": "c. +5-6% (energy + backlog refresh)"},
            {"label": "Peer benchmark", "value": "Mid-range vs acute peers per m²"}
        ],
        "notes": "DBTH's premises cost is shaped by DRI's long maintenance history (parts of the estate dating to the 1930s), Bassetlaw's smaller-acute resilience requirements, and the cross-ICS geography that complicates capital prioritisation. Without an NHP slot, capital recovery falls on operating-line spend. Energy reset under RM6011 and 5-7% hard-FM inflation drive the 2024-25 uplift.",
        "sources": [
            "https://www.dbth.nhs.uk/about-us/publications/",
            "https://www.england.nhs.uk/financial-accounts/",
            "https://www.salixfinance.co.uk/PSDS"
        ],
        "related": ["Doncaster and Bassetlaw Teaching Hospitals NHS Foundation Trust", "Premises & Infrastructure"]
    }
}
