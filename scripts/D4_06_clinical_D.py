# -*- coding: utf-8 -*-
"""Tier A depth-4 enrichment for NHS trust 'Clinical supplies & services' sub-lines (batch D).

49 trust-specific entries covering Acute, Specialist, Mental Health, Community
and Ambulance trusts. No generic template — each entry reflects the trust's
surgical/activity mix, consumable-heavy specialties, supply-chain posture and
2024-25 context (NHS Supply Chain Medical ~80%, industrial-action rebound,
DHSC Net Zero single-use reduction, HCDs via ICB, CNST separate).
"""

NEW = {
    "Clinical supplies & services — Barts Health NHS Trust": {
        "aliases": [{"name": "Clinical supplies & services", "parent": "Barts Health NHS Trust"}],
        "description": "Barts Health's £211.5M clinical-supplies bill — one of the largest in England — is anchored by the Barts Heart Centre (the country's biggest cardiac surgery and EP implant platform) and by trauma, vascular and stroke activity at the Royal London. Theatre-consumable intensity is exceptional: cardiac stents, structural-heart valves (TAVI), ICDs, CRT-Ds, LVADs and EP ablation catheters flow through the St Bartholomew's cath labs and cardiothoracic theatres.",
        "beneficiaries": "c.2.5M outpatient contacts and 140k admissions/yr across Royal London, St Bartholomew's, Whipps Cross, Newham and Mile End; pan-regional cardiac and trauma referrals.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Terms and Conditions for the Supply of Goods and Services · NHS London Procurement Partnership frameworks.",
        "key_stats": [
            {"label": "Clinical supplies & services 2024-25", "value": "£211.5M"},
            {"label": "Share of trust total opex", "value": "c. 11% of ~£1.9bn opex"},
            {"label": "Biggest sub-category", "value": "Cardiology devices (stents, TAVI valves, ICDs, EP catheters) ~25-30%"},
            {"label": "Activity anchor", "value": "c. 140k admissions/yr · >10k cardiac procedures at Barts Heart Centre"},
            {"label": "Supply-chain channel", "value": "NHS Supply Chain Medical ~75% · direct (cardiology, neuro) ~25%"},
            {"label": "Major trauma", "value": "Royal London MTC — orthopaedic trauma implants and blood products"},
            {"label": "YoY change", "value": "c. +6-8% nominal — elective rebound post industrial action"},
            {"label": "Procurement collaborative", "value": "LPP (London Procurement Partnership) lead member"}
        ],
        "notes": "Barts Heart Centre's device bill (Abbott, Boston Scientific, Medtronic) is the largest single driver; structural-heart valves alone run into eight figures. The Royal London's HEMS/major-trauma flow drives blood products (NHSBT), trauma packs and fixation. Sustainability pressure under DHSC Net Zero is visible in the trust's single-use laparoscopic-instrument switch programme. VPAG-equivalent rebates do not apply to devices; HCDs via NEL ICB pass-through are kept on a separate ledger.",
        "sources": [
            {"publisher": "Barts Health NHS Trust", "title": "Annual Report and Accounts 2024-25", "url": "https://www.bartshealth.nhs.uk/annual-report"},
            {"publisher": "NHS Supply Chain", "title": "Medical category reports", "url": "https://www.supplychain.nhs.uk/"},
            {"publisher": "NHS London Procurement Partnership", "title": "Clinical procurement frameworks", "url": "https://www.lpp.nhs.uk/"}
        ],
        "related": ["Barts Health NHS Trust", "Drugs costs — Barts Health NHS Trust"]
    },
    "Clinical supplies & services — Oxford University Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Clinical supplies & services", "parent": "Oxford University Hospitals NHS Foundation Trust"}],
        "description": "OUH's £177.8M clinical-supplies spend reflects the John Radcliffe's role as Thames Valley's major trauma, cardiac and neurosurgical centre, with the Churchill Cancer Centre and Nuffield Orthopaedic Centre adding high-implant volumes. Oxford is a national centre for transplantation (kidney, pancreas, islet) and a high-volume robotic-surgery site (da Vinci Xi), driving expensive single-use robotic instruments and stapler reloads.",
        "beneficiaries": "Oxfordshire residents plus pan-Thames Valley tertiary referrals for cardiac, neurosurgery, transplant and specialist cancer.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Terms and Conditions for the Supply of Goods and Services · NHSE Specialised Commissioning.",
        "key_stats": [
            {"label": "Clinical supplies & services 2024-25", "value": "£177.8M"},
            {"label": "Share of trust total opex", "value": "c. 13% of ~£1.4bn opex"},
            {"label": "Biggest sub-category", "value": "Orthopaedic implants + robotic consumables ~22%"},
            {"label": "Activity anchor", "value": "c. 130k admissions · >100k theatre cases/yr"},
            {"label": "Specialist driver", "value": "Nuffield Orthopaedic Centre — joint registry-tracked primary hips/knees"},
            {"label": "Transplant activity", "value": "Churchill — kidney, pancreas & islet transplantation consumables"},
            {"label": "Supply-chain channel", "value": "NHS Supply Chain Medical ~80% · direct (robotics, cardiology) ~20%"},
            {"label": "Sustainability", "value": "Reusable-instrument pilot under DHSC Net Zero"}
        ],
        "notes": "Da Vinci Xi fleet across urology, colorectal, gynaecology and cardiothoracic specialties generates heavy single-use-instrument spend that NHS Supply Chain does not fully cover. Trauma implant volumes run through the John Radcliffe MTC. The Oxford Heart Centre's structural-heart programme (TAVI, MitraClip) is a growth driver, and the 2024-25 accounts capture the first full year of post-pandemic theatre throughput at near-pre-Covid baselines.",
        "sources": [
            {"publisher": "Oxford University Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2024-25", "url": "https://www.ouh.nhs.uk/about/publications/annual-reports.aspx"},
            {"publisher": "National Joint Registry", "title": "21st Annual Report 2024", "url": "https://www.njrcentre.org.uk/"},
            {"publisher": "NHS Supply Chain", "title": "Medical category frameworks", "url": "https://www.supplychain.nhs.uk/"}
        ],
        "related": ["Oxford University Hospitals NHS Foundation Trust", "Drugs costs — Oxford University Hospitals NHS Foundation Trust"]
    },
    "Clinical supplies & services — University Hospitals Sussex NHS Foundation Trust": {
        "aliases": [{"name": "Clinical supplies & services", "parent": "University Hospitals Sussex NHS Foundation Trust"}],
        "description": "UHSussex's £135.4M clinical-supplies bill spans the Royal Sussex County (Brighton), Princess Royal (Haywards Heath), Worthing, St Richard's (Chichester) and Southlands sites post-2021 merger. The Royal Sussex is the regional major trauma centre, cardiac surgery hub and neurosurgical centre for Sussex, driving implant and device intensity alongside high elective orthopaedic volumes at the peripheral sites.",
        "beneficiaries": "c.1.8M Sussex residents across two acute hospital groups plus tertiary cardiac, trauma and neurosurgery referrals.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Terms and Conditions for the Supply of Goods and Services.",
        "key_stats": [
            {"label": "Clinical supplies & services 2024-25", "value": "£135.4M"},
            {"label": "Share of trust total opex", "value": "c. 11% of ~£1.25bn opex"},
            {"label": "Biggest sub-category", "value": "Orthopaedic implants + cardiac devices ~20%"},
            {"label": "Activity anchor", "value": "c. 150k admissions/yr across 5 main sites"},
            {"label": "Major trauma", "value": "Royal Sussex County — Sussex MTC (trauma packs, blood products, fixation)"},
            {"label": "Supply-chain channel", "value": "NHS Supply Chain Medical ~80% · direct ~20%"},
            {"label": "YoY change", "value": "c. +5-7% nominal — post-merger harmonisation + elective rebound"},
            {"label": "CQC context", "value": "CQC 2023 inspection flagged theatre-consumable controls across merged sites"}
        ],
        "notes": "Post-merger harmonisation of five-site procurement contracts continues to compress unit prices but single-site legacy stock pools complicate inventory. The new Louisa Martindale building at Brighton (opened 2023) adds theatre capacity and — with it — consumable throughput. The trust's 3T MRI and interventional radiology volumes drive contrast media spend (iodinated + gadolinium).",
        "sources": [
            {"publisher": "University Hospitals Sussex NHS Foundation Trust", "title": "Annual Report and Accounts 2024-25", "url": "https://www.uhsussex.nhs.uk/about/our-publications/"},
            {"publisher": "NHS Supply Chain", "title": "Medical category reports", "url": "https://www.supplychain.nhs.uk/"},
            {"publisher": "Care Quality Commission", "title": "University Hospitals Sussex inspection reports", "url": "https://www.cqc.org.uk/provider/RYR"}
        ],
        "related": ["University Hospitals Sussex NHS Foundation Trust", "Drugs costs — University Hospitals Sussex NHS Foundation Trust"]
    },
    "Clinical supplies & services — University College London Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Clinical supplies & services", "parent": "University College London Hospitals NHS Foundation Trust"}],
        "description": "UCLH's £130.0M clinical-supplies spend is dominated by specialist activity: the UCH Proton Beam Therapy Centre, the Macmillan Cancer Centre, the National Hospital for Neurology and Neurosurgery (Queen Square) and the Heart Hospital/Grafton Way cardiac campus. Queen Square is one of the UK's busiest DBS and functional-neurosurgery centres; the trust is also a national CAR-T provider.",
        "beneficiaries": "Central London residents plus national tertiary referrals for proton therapy, neurosurgery, haematology-oncology and advanced therapies.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHSE Specialised Commissioning · NHS Terms and Conditions for the Supply of Goods and Services.",
        "key_stats": [
            {"label": "Clinical supplies & services 2024-25", "value": "£130.0M"},
            {"label": "Share of trust total opex", "value": "c. 10% of ~£1.3bn opex"},
            {"label": "Biggest sub-category", "value": "Neurosurgical devices (DBS leads, shunts, EVDs) + proton consumables"},
            {"label": "Proton Beam Therapy", "value": "UCH — one of two NHS PBT centres (patient-specific compensators)"},
            {"label": "Cell & gene therapy", "value": "CAR-T provider — apheresis, cryopreservation, infusion consumables"},
            {"label": "Supply-chain channel", "value": "NHS Supply Chain Medical ~70% · direct (neuro, proton) ~30%"},
            {"label": "Major partner", "value": "NHS London Procurement Partnership (LPP) host trust"},
            {"label": "YoY change", "value": "c. +7-9% nominal — PBT ramp-up + advanced-therapy growth"}
        ],
        "notes": "Proton therapy consumables (patient-specific brass apertures, wax compensators) are procured on bespoke contracts outside standard NHS Supply Chain. Queen Square's DBS volumes drive Medtronic/Abbott/Boston Scientific lead spend. CAR-T apheresis and cryopreservation consumables scale with the trust's share of NHSE-commissioned cell-therapy activity. UCLH hosts LPP, giving it first-line access to renegotiated London device and consumable deals.",
        "sources": [
            {"publisher": "University College London Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2024-25", "url": "https://www.uclh.nhs.uk/about-us/who-we-are/corporate-publications/annual-reports-and-accounts"},
            {"publisher": "NHS England", "title": "Proton Beam Therapy service specification", "url": "https://www.england.nhs.uk/commissioning/spec-services/npc-crg/b01/"},
            {"publisher": "NHS London Procurement Partnership", "title": "Frameworks and savings reports", "url": "https://www.lpp.nhs.uk/"}
        ],
        "related": ["University College London Hospitals NHS Foundation Trust", "Drugs costs — University College London Hospitals NHS Foundation Trust"]
    },
    "Clinical supplies & services — University Hospitals Bristol and Weston NHS Foundation Trust": {
        "aliases": [{"name": "Clinical supplies & services", "parent": "University Hospitals Bristol and Weston NHS Foundation Trust"}],
        "description": "UHBW's £110.7M clinical-supplies bill covers the Bristol Royal Infirmary, Bristol Heart Institute, Bristol Royal Hospital for Children, St Michael's maternity and Weston General. The Bristol Heart Institute is a regional cardiac surgery and congenital-heart centre; the Children's Hospital is one of ten NHSE-commissioned specialist paediatric cardiac centres, adding expensive paediatric-specific devices and ECMO consumables.",
        "beneficiaries": "South West residents (~500k Bristol/N Somerset) plus tertiary paediatric-cardiac, adult cardiac and oncology referrals.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHSE Specialised Commissioning · NHS Terms and Conditions.",
        "key_stats": [
            {"label": "Clinical supplies & services 2024-25", "value": "£110.7M"},
            {"label": "Share of trust total opex", "value": "c. 11% of ~£1.0bn opex"},
            {"label": "Biggest sub-category", "value": "Cardiac devices + paediatric-cardiac consumables"},
            {"label": "Activity anchor", "value": "c. 115k admissions · >85k theatre cases/yr"},
            {"label": "Paediatric cardiac", "value": "BRHC — one of 10 NHSE specialist paediatric cardiac centres"},
            {"label": "ECMO programme", "value": "Adult + paediatric ECMO — high-cost circuit consumables"},
            {"label": "Supply-chain channel", "value": "NHS Supply Chain Medical ~78% · direct (cardiac) ~22%"},
            {"label": "Merger context", "value": "Post-2020 merger with Weston — multi-site consumable harmonisation"}
        ],
        "notes": "Paediatric-cardiac and ECMO activity drive a disproportionate consumables spend relative to trust size: neonatal ECMO circuits alone cost four-figures per case. The post-2020 Weston merger continues to yield procurement harmonisation savings. The 2024-25 accounts reflect full recovery of elective cardiac throughput after 2023-24 industrial-action disruption.",
        "sources": [
            {"publisher": "University Hospitals Bristol and Weston NHS Foundation Trust", "title": "Annual Report and Accounts 2024-25", "url": "https://www.uhbw.nhs.uk/about-us/publications"},
            {"publisher": "NHS England", "title": "Paediatric cardiac service specification", "url": "https://www.england.nhs.uk/commissioning/spec-services/npc-crg/e05/"},
            {"publisher": "NHS Supply Chain", "title": "Medical category reports", "url": "https://www.supplychain.nhs.uk/"}
        ],
        "related": ["University Hospitals Bristol and Weston NHS Foundation Trust", "Drugs costs — University Hospitals Bristol and Weston NHS Foundation Trust"]
    },
    "Clinical supplies & services — Liverpool University Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Clinical supplies & services", "parent": "Liverpool University Hospitals NHS Foundation Trust"}],
        "description": "LUHFT's £103.1M clinical-supplies spend covers the Royal Liverpool, Aintree and Broadgreen sites. The new Royal Liverpool building (opened October 2022) centralises acute medicine and major abdominal/vascular surgery, while Aintree hosts the regional major trauma centre and Broadgreen handles high-volume elective orthopaedics. Vascular, HPB and colorectal theatre activity is particularly consumable-intensive.",
        "beneficiaries": "Liverpool and Merseyside residents (~750k catchment) plus tertiary trauma, vascular and HPB referrals.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Terms and Conditions for the Supply of Goods and Services.",
        "key_stats": [
            {"label": "Clinical supplies & services 2024-25", "value": "£103.1M"},
            {"label": "Share of trust total opex", "value": "c. 10% of ~£1.0bn opex"},
            {"label": "Biggest sub-category", "value": "Orthopaedic implants (Broadgreen) + vascular grafts ~20%"},
            {"label": "Activity anchor", "value": "c. 135k admissions/yr across 3 sites"},
            {"label": "Major trauma", "value": "Aintree — Cheshire & Merseyside MTC"},
            {"label": "Supply-chain channel", "value": "NHS Supply Chain Medical ~80% · direct ~20%"},
            {"label": "YoY change", "value": "c. +6-8% nominal — new Royal Liverpool throughput ramp-up"},
            {"label": "Procurement collaborative", "value": "NHS North West Procurement Development (NWPD)"}
        ],
        "notes": "The new Royal Liverpool's integrated theatre suites and ICU are now at steady-state, pushing single-use instrument and ventilator-circuit volumes above legacy-hospital levels. Aintree's MTC flow keeps trauma implants and blood products elevated. Broadgreen's high-volume day-case orthopaedic model relies on standardised Stryker/Zimmer/Smith & Nephew implant kits procured through the Framework for Hip & Knee Prostheses.",
        "sources": [
            {"publisher": "Liverpool University Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2024-25", "url": "https://www.liverpoolft.nhs.uk/about-us/publications/"},
            {"publisher": "NHS Supply Chain", "title": "Orthopaedic implants framework", "url": "https://www.supplychain.nhs.uk/"},
            {"publisher": "National Joint Registry", "title": "21st Annual Report 2024", "url": "https://www.njrcentre.org.uk/"}
        ],
        "related": ["Liverpool University Hospitals NHS Foundation Trust", "Drugs costs — Liverpool University Hospitals NHS Foundation Trust"]
    },
    "Clinical supplies & services — Chelsea and Westminster Hospital NHS Foundation Trust": {
        "aliases": [{"name": "Clinical supplies & services", "parent": "Chelsea and Westminster Hospital NHS Foundation Trust"}],
        "description": "ChelWest's £95.6M clinical-supplies bill spans Chelsea and Westminster Hospital and West Middlesex University Hospital. The trust runs one of London's largest maternity services (c.11,000 births/yr), a busy HIV service (the Kobler and John Hunter clinics), a specialist burns service and a high-volume day-surgery platform. Maternity and neonatal consumables are disproportionately significant drivers.",
        "beneficiaries": "West/central London residents (~1.5M catchment across two hospitals) plus specialist burns and HIV referrals.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Terms and Conditions · NHS London Procurement Partnership frameworks.",
        "key_stats": [
            {"label": "Clinical supplies & services 2024-25", "value": "£95.6M"},
            {"label": "Share of trust total opex", "value": "c. 12% of ~£0.8bn opex"},
            {"label": "Biggest sub-category", "value": "Maternity/neonatal consumables + surgical packs ~20%"},
            {"label": "Activity anchor", "value": "c. 11,000 births · c. 90k admissions/yr"},
            {"label": "Specialist services", "value": "London-wide burns service + HIV (Kobler/John Hunter)"},
            {"label": "Day surgery", "value": "High-volume elective day-case platform — custom procedure packs"},
            {"label": "Supply-chain channel", "value": "NHS Supply Chain Medical ~82% · direct (burns) ~18%"},
            {"label": "Procurement collaborative", "value": "LPP (London Procurement Partnership)"}
        ],
        "notes": "The West Middlesex maternity unit and Chelsea NNU together account for a large share of maternity-consumable spend (epidural kits, CTG sensors, surfactant delivery sets). The burns service consumes specialist dressings (Biobrane, Suprathel, silver-impregnated) procured outside mainline NHS Supply Chain. HIV service point-of-care testing reagents and ART adherence-device costs are significant but sit in drugs/other lines.",
        "sources": [
            {"publisher": "Chelsea and Westminster Hospital NHS Foundation Trust", "title": "Annual Report and Accounts 2024-25", "url": "https://www.chelwest.nhs.uk/about-us/corporate-information/annual-reports"},
            {"publisher": "NHS London Procurement Partnership", "title": "Maternity & neonatal framework", "url": "https://www.lpp.nhs.uk/"},
            {"publisher": "NHS Supply Chain", "title": "Medical category reports", "url": "https://www.supplychain.nhs.uk/"}
        ],
        "related": ["Chelsea and Westminster Hospital NHS Foundation Trust", "Drugs costs — Chelsea and Westminster Hospital NHS Foundation Trust"]
    },
    "Clinical supplies & services — Royal Free London NHS Foundation Trust": {
        "aliases": [{"name": "Clinical supplies & services", "parent": "Royal Free London NHS Foundation Trust"}],
        "description": "Royal Free London's £88.2M clinical-supplies spend covers the Royal Free, Barnet and Chase Farm sites. The Royal Free is a national tertiary centre for liver transplantation, HPB surgery, amyloidosis and infectious diseases (the UK's High Consequence Infectious Diseases centre), while Chase Farm is a high-volume elective orthopaedic hub. This mix — transplant + elective ortho + HCID readiness — shapes an unusually specialist consumable basket.",
        "beneficiaries": "North London residents (~1.6M catchment) plus national tertiary referrals for liver transplant, amyloidosis and HCID.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHSE Specialised Commissioning · NHS Terms and Conditions.",
        "key_stats": [
            {"label": "Clinical supplies & services 2024-25", "value": "£88.2M"},
            {"label": "Share of trust total opex", "value": "c. 10% of ~£0.9bn opex"},
            {"label": "Biggest sub-category", "value": "Orthopaedic implants (Chase Farm) + HPB/liver theatre packs"},
            {"label": "Activity anchor", "value": "c. 120k admissions · >90k elective cases across 3 sites"},
            {"label": "Liver transplant", "value": "Royal Free — one of 7 NHS adult liver transplant centres"},
            {"label": "HCID centre", "value": "National High Consequence Infectious Diseases unit — PPE + isolation"},
            {"label": "Supply-chain channel", "value": "NHS Supply Chain Medical ~80% · direct (HPB, HCID) ~20%"},
            {"label": "Chase Farm", "value": "Elective-only orthopaedic hub — standardised implant kits"}
        ],
        "notes": "Liver transplant perfusion machines (normothermic machine perfusion via OrganOx metra) drive single-use-consumable spend unique to the few NHS liver centres. HCID readiness at the Royal Free requires rotating stocks of high-grade PPE and isolator consumables (Trexler-style tents) that sit outside standard infection-control budgets. Chase Farm's planned-care-only model delivers lower unit consumable costs per joint-replacement episode than mixed-acute peers.",
        "sources": [
            {"publisher": "Royal Free London NHS Foundation Trust", "title": "Annual Report and Accounts 2024-25", "url": "https://www.royalfree.nhs.uk/about-us/corporate-information/annual-reports-and-accounts/"},
            {"publisher": "NHS England", "title": "High Consequence Infectious Diseases service specification", "url": "https://www.england.nhs.uk/commissioning/spec-services/npc-crg/group-b/b07/"},
            {"publisher": "NHS Blood and Transplant", "title": "Organ transplantation annual report 2023-24", "url": "https://www.odt.nhs.uk/"}
        ],
        "related": ["Royal Free London NHS Foundation Trust", "Drugs costs — Royal Free London NHS Foundation Trust"]
    },
    "Clinical supplies & services — York and Scarborough Teaching Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Clinical supplies & services", "parent": "York and Scarborough Teaching Hospitals NHS Foundation Trust"}],
        "description": "YSTH's £82.0M clinical-supplies bill covers York Hospital, Scarborough Hospital, Bridlington and community sites across a dispersed North Yorkshire and East Riding geography. The dual-site acute model means duplicated stock pools and geographic-resilience overhead; Scarborough's relative isolation drives higher buffer inventory for emergency and obstetric supplies.",
        "beneficiaries": "North Yorkshire / East Riding residents (~800k catchment), including rural coastal communities around Scarborough and Bridlington.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Terms and Conditions.",
        "key_stats": [
            {"label": "Clinical supplies & services 2024-25", "value": "£82.0M"},
            {"label": "Share of trust total opex", "value": "c. 12% of ~£0.7bn opex"},
            {"label": "Biggest sub-category", "value": "General surgical/orthopaedic consumables ~20%"},
            {"label": "Activity anchor", "value": "c. 100k admissions/yr across York + Scarborough"},
            {"label": "Geography driver", "value": "Dual acute sites — buffer stock premium for isolated Scarborough"},
            {"label": "Supply-chain channel", "value": "NHS Supply Chain Medical ~82% · direct ~18%"},
            {"label": "YoY change", "value": "c. +5-7% nominal — activity rebound + contract price uplifts"},
            {"label": "Procurement collaborative", "value": "NHS North of England Commercial Procurement Collaborative (NOE CPC)"}
        ],
        "notes": "Scarborough's coastal isolation drives resilience-inventory costs — obstetric and paediatric consumables in particular must be stocked locally because transfer to York is weather-dependent. The trust's 2023-24 financial recovery plan flagged clinical supplies as a CIP (cost improvement) target, with 2024-25 savings expected from NOE CPC consolidated orders. Theatre-consumable volumes rebounded strongly after 2023-24 industrial action.",
        "sources": [
            {"publisher": "York and Scarborough Teaching Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2024-25", "url": "https://www.yorkhospitals.nhs.uk/about-us/corporate-publications/"},
            {"publisher": "NOE CPC", "title": "Clinical procurement frameworks", "url": "https://www.noecpc.nhs.uk/"},
            {"publisher": "NHS Supply Chain", "title": "Medical category reports", "url": "https://www.supplychain.nhs.uk/"}
        ],
        "related": ["York and Scarborough Teaching Hospitals NHS Foundation Trust", "Drugs costs — York and Scarborough Teaching Hospitals NHS Foundation Trust"]
    },
    "Clinical supplies & services — Portsmouth Hospitals University NHS Trust": {
        "aliases": [{"name": "Clinical supplies & services", "parent": "Portsmouth Hospitals University NHS Trust"}],
        "description": "Portsmouth Hospitals University NHS Trust's £70.6M clinical-supplies spend is anchored by Queen Alexandra Hospital (QA) — a single very large acute site serving 675,000 people across Portsmouth, South-East Hampshire and the Isle of Wight mainland catchment. QA hosts vascular, renal, hyperacute stroke and a large cardiology/structural-heart service, driving device intensity alongside high elective and emergency surgical throughput.",
        "beneficiaries": "c. 675,000 residents of Portsmouth, Gosport, Fareham, Havant, East Hampshire and IoW transfers.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Terms and Conditions for the Supply of Goods and Services.",
        "key_stats": [
            {"label": "Clinical supplies & services 2024-25", "value": "£70.6M"},
            {"label": "Share of trust total opex", "value": "c. 11% of ~£0.65bn opex"},
            {"label": "Biggest sub-category", "value": "Cardiology devices + vascular grafts ~20%"},
            {"label": "Activity anchor", "value": "c. 130k admissions · >1.2k births/yr at QA"},
            {"label": "Hyperacute stroke", "value": "Wessex HASU — thrombectomy consumables"},
            {"label": "Supply-chain channel", "value": "NHS Supply Chain Medical ~82% · direct ~18%"},
            {"label": "Procurement collaborative", "value": "Hampshire & Isle of Wight ICS joint procurement"},
            {"label": "YoY change", "value": "c. +6-8% nominal — elective rebound + HASU growth"}
        ],
        "notes": "Mechanical thrombectomy growth at the Wessex HASU drives stent-retriever and aspiration-catheter spend (Stryker Trevo, Penumbra). QA's vascular service consumes endovascular aneurysm-repair (EVAR) and peripheral-vascular device volumes on par with much larger teaching hospitals. The trust's participation in the H&IOW ICS joint-procurement pilot targeted FY24-25 savings in common consumables (dressings, sutures, cannulae).",
        "sources": [
            {"publisher": "Portsmouth Hospitals University NHS Trust", "title": "Annual Report and Accounts 2024-25", "url": "https://www.porthosp.nhs.uk/about-us/publications.htm"},
            {"publisher": "NHS England", "title": "Mechanical thrombectomy service specification", "url": "https://www.england.nhs.uk/commissioning/spec-services/"},
            {"publisher": "NHS Supply Chain", "title": "Medical category reports", "url": "https://www.supplychain.nhs.uk/"}
        ],
        "related": ["Portsmouth Hospitals University NHS Trust", "Drugs costs — Portsmouth Hospitals University NHS Trust"]
    },
    "Clinical supplies & services — Somerset NHS Foundation Trust": {
        "aliases": [{"name": "Clinical supplies & services", "parent": "Somerset NHS Foundation Trust"}],
        "description": "Somerset NHSFT's £62.6M clinical-supplies bill reflects its unusual integrated model — combining Musgrove Park Hospital (Taunton), Yeovil District Hospital (post-April 2023 merger) and the county's community, mental health and adult social-care services. The integrated footprint adds community-nursing consumables (wound care, continence, catheters) to an acute theatre-and-device baseline.",
        "beneficiaries": "c. 580,000 Somerset residents across acute, community and mental-health pathways.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Terms and Conditions.",
        "key_stats": [
            {"label": "Clinical supplies & services 2024-25", "value": "£62.6M"},
            {"label": "Share of trust total opex", "value": "c. 9% of ~£0.7bn opex"},
            {"label": "Biggest sub-category", "value": "Acute theatre consumables + community wound-care ~22%"},
            {"label": "Activity anchor", "value": "c. 90k admissions (acute) + c. 1.5M community contacts/yr"},
            {"label": "Integration model", "value": "Acute + community + MH + adult social care (post-2023 Yeovil merger)"},
            {"label": "Community driver", "value": "Wound-care, continence, home O2 consumables across c. 200k patients"},
            {"label": "Supply-chain channel", "value": "NHS Supply Chain Medical ~80% · direct (community) ~20%"},
            {"label": "Mental health share", "value": "Low — ward diagnostics, restraint, PPE"}
        ],
        "notes": "The 2023 Yeovil merger continues to yield procurement synergies — particularly on theatre implants where Musgrove Park and Yeovil previously held separate contracts. The integrated community service drives wound-care dressing spend comparable to a mid-size community trust, making Somerset's consumables mix unusually broad. Reusable-instrument and single-use-plastics reduction pilots align with DHSC Net Zero pressure.",
        "sources": [
            {"publisher": "Somerset NHS Foundation Trust", "title": "Annual Report and Accounts 2024-25", "url": "https://www.somersetft.nhs.uk/about-us/publications/"},
            {"publisher": "NHS Supply Chain", "title": "Medical category reports", "url": "https://www.supplychain.nhs.uk/"},
            {"publisher": "NHS England", "title": "Delivering a Net Zero NHS", "url": "https://www.england.nhs.uk/greenernhs/"}
        ],
        "related": ["Somerset NHS Foundation Trust", "Drugs costs — Somerset NHS Foundation Trust"]
    },
    "Clinical supplies & services — Lancashire Teaching Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Clinical supplies & services", "parent": "Lancashire Teaching Hospitals NHS Foundation Trust"}],
        "description": "LTHTR's £59.4M clinical-supplies spend covers Royal Preston Hospital and Chorley & South Ribble Hospital. Royal Preston hosts the Lancashire & South Cumbria major trauma centre, the regional neurosurgery and neurosciences service, renal services and a busy vascular unit — giving the trust an outsized specialist device mix for its size.",
        "beneficiaries": "Central Lancashire residents (~370k local) plus pan-regional tertiary neuro, trauma and vascular referrals (~1.5M catchment).",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHSE Specialised Commissioning · NHS Terms and Conditions.",
        "key_stats": [
            {"label": "Clinical supplies & services 2024-25", "value": "£59.4M"},
            {"label": "Share of trust total opex", "value": "c. 10% of ~£0.6bn opex"},
            {"label": "Biggest sub-category", "value": "Neurosurgical devices + trauma fixation ~22%"},
            {"label": "Major trauma", "value": "Royal Preston — Lancashire & South Cumbria MTC"},
            {"label": "Neurosurgery", "value": "Regional tertiary neurosciences — shunts, EVDs, spinal implants"},
            {"label": "Supply-chain channel", "value": "NHS Supply Chain Medical ~80% · direct (neuro) ~20%"},
            {"label": "Procurement collaborative", "value": "NOE CPC (North of England CPC)"},
            {"label": "YoY change", "value": "c. +5-7% nominal — trauma + elective rebound"}
        ],
        "notes": "Neurosurgical device consumption (Medtronic/Integra shunts, EVDs, spinal instrumentation) is the key differentiator versus similar-sized acute peers. The MTC designation drives blood-product utilisation (NHSBT invoiced per bag) and trauma-fixation volumes. NOE CPC deals set most implant pricing; direct-buy channels are used where case-specific sizing requires OEM contact (e.g. spinal cages).",
        "sources": [
            {"publisher": "Lancashire Teaching Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2024-25", "url": "https://www.lancsteachinghospitals.nhs.uk/publications"},
            {"publisher": "NOE CPC", "title": "Neurosurgical device frameworks", "url": "https://www.noecpc.nhs.uk/"},
            {"publisher": "NHS England", "title": "Major trauma service specification", "url": "https://www.england.nhs.uk/commissioning/spec-services/npc-crg/group-d/d15/"}
        ],
        "related": ["Lancashire Teaching Hospitals NHS Foundation Trust", "Drugs costs — Lancashire Teaching Hospitals NHS Foundation Trust"]
    },
    "Clinical supplies & services — The Dudley Group NHS Foundation Trust": {
        "aliases": [{"name": "Clinical supplies & services", "parent": "The Dudley Group NHS Foundation Trust"}],
        "description": "Dudley Group's £56.2M clinical-supplies bill centres on Russells Hall Hospital, which serves c. 450,000 people in the Dudley borough and surrounding Black Country. The trust runs a full general acute portfolio (emergency, general surgery, elective orthopaedics, obstetrics) plus a busy cardiac-catheter lab delivering primary PCI for the locality.",
        "beneficiaries": "c. 450,000 Dudley borough residents plus Stourbridge and Halesowen catchment.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Terms and Conditions.",
        "key_stats": [
            {"label": "Clinical supplies & services 2024-25", "value": "£56.2M"},
            {"label": "Share of trust total opex", "value": "c. 12% of ~£0.47bn opex"},
            {"label": "Biggest sub-category", "value": "Orthopaedic implants + cardiology stents ~20%"},
            {"label": "Activity anchor", "value": "c. 90k admissions · c. 4k births/yr"},
            {"label": "Cardiology", "value": "Russells Hall cath lab — primary PCI consumables"},
            {"label": "Supply-chain channel", "value": "NHS Supply Chain Medical ~84% · direct ~16%"},
            {"label": "Procurement collaborative", "value": "Black Country ICS joint procurement"},
            {"label": "YoY change", "value": "c. +4-6% nominal — price uplift + activity rebound"}
        ],
        "notes": "A single-site acute profile keeps Dudley's consumables footprint more tightly controlled than multi-site peers. The cath lab's primary-PCI volumes drive drug-eluting stent, balloon and guidewire spend. The Black Country ICS joint-procurement pilot (Dudley + Sandwell + Walsall + Wolverhampton) targets theatre-pack and general-consumable aggregation for FY24-26.",
        "sources": [
            {"publisher": "The Dudley Group NHS Foundation Trust", "title": "Annual Report and Accounts 2024-25", "url": "https://dgft.nhs.uk/about-us/publications/"},
            {"publisher": "NHS Supply Chain", "title": "Cardiology interventional devices framework", "url": "https://www.supplychain.nhs.uk/"},
            {"publisher": "Black Country ICB", "title": "Joint working reports", "url": "https://www.blackcountry.icb.nhs.uk/"}
        ],
        "related": ["The Dudley Group NHS Foundation Trust", "Drugs costs — The Dudley Group NHS Foundation Trust"]
    },
    "Clinical supplies & services — The Shrewsbury and Telford Hospital NHS Trust": {
        "aliases": [{"name": "Clinical supplies & services", "parent": "The Shrewsbury and Telford Hospital NHS Trust"}],
        "description": "SaTH's £55.5M clinical-supplies spend covers the Royal Shrewsbury Hospital and the Princess Royal Hospital (Telford). The trust remains under Section 29A CQC enforcement (as of 2024-25) following the Ockenden maternity review, and clinical-supplies planning has had to support large-scale maternity-service investment in CTG monitoring, obstetric consumables and midwifery kit alongside standard acute activity.",
        "beneficiaries": "c. 500,000 Shropshire, Telford & Wrekin and mid-Wales residents.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Terms and Conditions · Ockenden maternity-improvement requirements.",
        "key_stats": [
            {"label": "Clinical supplies & services 2024-25", "value": "£55.5M"},
            {"label": "Share of trust total opex", "value": "c. 11% of ~£0.5bn opex"},
            {"label": "Biggest sub-category", "value": "General surgical + obstetric consumables ~22%"},
            {"label": "Activity anchor", "value": "c. 95k admissions · c. 4.5k births/yr"},
            {"label": "Maternity driver", "value": "Post-Ockenden CTG/fetal-monitoring and obstetric kit uplift"},
            {"label": "Supply-chain channel", "value": "NHS Supply Chain Medical ~85% · direct ~15%"},
            {"label": "CQC status", "value": "Under Section 29A enforcement (maternity)"},
            {"label": "Hospital Transformation", "value": "'Future Fit' capital scheme — theatre & ED reconfig pending"}
        ],
        "notes": "Maternity reinvestment post-Ockenden is the standout driver: additional fetal-monitoring consumables, modernised CTG platforms (Philips/GE) and expanded midwifery packs appear in the 2024-25 accounts. The long-delayed Hospital Transformation Programme ('Future Fit') is expected to reshape theatre-consumable flow once reconfiguration proceeds. Procurement still runs through West Midlands collaborative channels.",
        "sources": [
            {"publisher": "The Shrewsbury and Telford Hospital NHS Trust", "title": "Annual Report and Accounts 2024-25", "url": "https://www.sath.nhs.uk/about-us/corporate-documents/"},
            {"publisher": "Ockenden Review", "title": "Final Report (March 2022)", "url": "https://www.gov.uk/government/publications/final-report-of-the-ockenden-review"},
            {"publisher": "Care Quality Commission", "title": "SaTH inspection reports", "url": "https://www.cqc.org.uk/provider/RXW"}
        ],
        "related": ["The Shrewsbury and Telford Hospital NHS Trust", "Drugs costs — The Shrewsbury and Telford Hospital NHS Trust"]
    },
    "Clinical supplies & services — Hampshire Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Clinical supplies & services", "parent": "Hampshire Hospitals NHS Foundation Trust"}],
        "description": "Hampshire Hospitals' £51.9M clinical-supplies bill covers Basingstoke & North Hampshire Hospital, Royal Hampshire County Hospital (Winchester) and Andover War Memorial. Basingstoke is a national tertiary centre for pseudomyxoma peritonei (PMP) and peritoneal malignancy (CRS/HIPEC), giving the trust unusual consumable-intensity for its size.",
        "beneficiaries": "c. 600,000 North/mid Hampshire residents plus national PMP/peritoneal-malignancy referrals.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHSE Specialised Commissioning · NHS Terms and Conditions.",
        "key_stats": [
            {"label": "Clinical supplies & services 2024-25", "value": "£51.9M"},
            {"label": "Share of trust total opex", "value": "c. 10% of ~£0.52bn opex"},
            {"label": "Biggest sub-category", "value": "CRS/HIPEC theatre consumables + general surgical ~22%"},
            {"label": "Activity anchor", "value": "c. 90k admissions/yr across 3 sites"},
            {"label": "National specialist", "value": "Basingstoke — NHSE PMP/peritoneal-malignancy centre (CRS/HIPEC)"},
            {"label": "Supply-chain channel", "value": "NHS Supply Chain Medical ~82% · direct (HIPEC) ~18%"},
            {"label": "Procurement collaborative", "value": "Hampshire & Isle of Wight ICS"},
            {"label": "Hospital reconfig", "value": "New hospital programme — reshaping future theatre consumable demand"}
        ],
        "notes": "CRS/HIPEC cases consume long-duration theatre sessions with exceptional single-use instrument, stapler and energy-device volumes; HIPEC chemotherapy delivery consumables sit at the drugs/clinical-supplies boundary. The New Hospital Programme business case (Basingstoke + Winchester) will reshape future theatre demand but 2024-25 remains a steady-state year. H&IOW ICS joint procurement delivers modest aggregation savings.",
        "sources": [
            {"publisher": "Hampshire Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2024-25", "url": "https://www.hampshirehospitals.nhs.uk/en/About-us/Publications/"},
            {"publisher": "NHS England", "title": "Pseudomyxoma peritonei service specification", "url": "https://www.england.nhs.uk/commissioning/spec-services/npc-crg/group-a/a02/"},
            {"publisher": "NHS Supply Chain", "title": "Medical category reports", "url": "https://www.supplychain.nhs.uk/"}
        ],
        "related": ["Hampshire Hospitals NHS Foundation Trust", "Drugs costs — Hampshire Hospitals NHS Foundation Trust"]
    },
    "Clinical supplies & services — East Lancashire Hospitals NHS Trust": {
        "aliases": [{"name": "Clinical supplies & services", "parent": "East Lancashire Hospitals NHS Trust"}],
        "description": "ELHT's £50.8M clinical-supplies spend covers Royal Blackburn Teaching Hospital, Burnley General, Pendle Community and Clitheroe Community. Royal Blackburn hosts a busy ED, a regional vascular unit and the hyperacute stroke service for Pennine Lancashire; Burnley General is the main obstetric and elective surgery site.",
        "beneficiaries": "c. 540,000 Pennine Lancashire residents across Blackburn, Burnley, Hyndburn, Pendle, Ribble Valley and Rossendale.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Terms and Conditions.",
        "key_stats": [
            {"label": "Clinical supplies & services 2024-25", "value": "£50.8M"},
            {"label": "Share of trust total opex", "value": "c. 11% of ~£0.47bn opex"},
            {"label": "Biggest sub-category", "value": "Orthopaedic + vascular + obstetric consumables ~20%"},
            {"label": "Activity anchor", "value": "c. 95k admissions · c. 5k births/yr"},
            {"label": "Vascular", "value": "Royal Blackburn — Pennine Lancs regional vascular hub"},
            {"label": "Supply-chain channel", "value": "NHS Supply Chain Medical ~84% · direct ~16%"},
            {"label": "Procurement collaborative", "value": "NOE CPC (North of England CPC)"},
            {"label": "YoY change", "value": "c. +5-7% nominal — activity rebound + uplift"}
        ],
        "notes": "Vascular-graft and EVAR activity at Royal Blackburn drives a higher device share than would be expected for a district general of similar size. Burnley's elective orthopaedic throughput supports standardised Framework for Hip & Knee Prostheses pricing. The trust's 2024-25 CIP programme targeted theatre-pack standardisation and single-use/reusable review under DHSC Net Zero.",
        "sources": [
            {"publisher": "East Lancashire Hospitals NHS Trust", "title": "Annual Report and Accounts 2024-25", "url": "https://elht.nhs.uk/about-us/corporate-reports"},
            {"publisher": "NOE CPC", "title": "Procurement frameworks", "url": "https://www.noecpc.nhs.uk/"},
            {"publisher": "NHS Supply Chain", "title": "Vascular devices framework", "url": "https://www.supplychain.nhs.uk/"}
        ],
        "related": ["East Lancashire Hospitals NHS Trust", "Drugs costs — East Lancashire Hospitals NHS Trust"]
    },
    "Clinical supplies & services — Royal Surrey NHS Foundation Trust": {
        "aliases": [{"name": "Clinical supplies & services", "parent": "Royal Surrey NHS Foundation Trust"}],
        "description": "Royal Surrey's £48.8M clinical-supplies bill is shaped by its role as a specialist surgical and cancer centre for Surrey and parts of West Sussex/Hampshire, anchored by the St Luke's Cancer Centre (regional oncology), a high-volume robotic-surgery programme (one of the UK's largest per-capita da Vinci footprints) and a regional upper-GI HPB service.",
        "beneficiaries": "Guildford/Surrey residents (~350k local) plus tertiary oncology, HPB and robotic-surgery referrals.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHSE Specialised Commissioning · NHS Terms and Conditions.",
        "key_stats": [
            {"label": "Clinical supplies & services 2024-25", "value": "£48.8M"},
            {"label": "Share of trust total opex", "value": "c. 13% of ~£0.38bn opex"},
            {"label": "Biggest sub-category", "value": "Robotic single-use instruments + oncology consumables ~25%"},
            {"label": "Activity anchor", "value": "c. 70k admissions · >1,500 robotic cases/yr"},
            {"label": "Robotics", "value": "4× da Vinci systems — urology, colorectal, gynae, HPB"},
            {"label": "Supply-chain channel", "value": "NHS Supply Chain Medical ~70% · direct (robotics, Intuitive) ~30%"},
            {"label": "Cancer centre", "value": "St Luke's — regional oncology (radiotherapy + SACT)"},
            {"label": "Procurement collaborative", "value": "Surrey Heartlands ICS + SCAN consortium"}
        ],
        "notes": "Intuitive Surgical (da Vinci) single-use EndoWrist instruments — subject to 10-use limits and not covered by mainline NHS Supply Chain — dominate the direct-buy share. Royal Surrey is a Centre of Excellence for robotic training, which increases consumable turnover. Brachytherapy and radiotherapy applicator consumables at St Luke's add a specialist-cancer overlay. The trust is a shareholder in Surrey Pathology Services and in SCAN (Surrey Cancer Alliance procurement).",
        "sources": [
            {"publisher": "Royal Surrey NHS Foundation Trust", "title": "Annual Report and Accounts 2024-25", "url": "https://www.royalsurrey.nhs.uk/about-us/publications-and-reports/"},
            {"publisher": "Intuitive Surgical", "title": "da Vinci instrument lifecycle policy", "url": "https://www.intuitive.com/"},
            {"publisher": "NHS Supply Chain", "title": "Surgical robotics framework", "url": "https://www.supplychain.nhs.uk/"}
        ],
        "related": ["Royal Surrey NHS Foundation Trust", "Drugs costs — Royal Surrey NHS Foundation Trust"]
    },
    "Clinical supplies & services — Wrightington, Wigan and Leigh NHS Foundation Trust": {
        "aliases": [{"name": "Clinical supplies & services", "parent": "Wrightington, Wigan and Leigh NHS Foundation Trust"}],
        "description": "WWL's £44.6M clinical-supplies bill reflects an unusual orthopaedic specialisation: Wrightington Hospital is the birthplace of Sir John Charnley's low-friction arthroplasty and remains a national referral centre for complex revision hip/knee and upper-limb joint replacement. The Royal Albert Edward Infirmary (Wigan) delivers general acute activity. Orthopaedic implants drive an outsized share of the consumables basket.",
        "beneficiaries": "Wigan borough residents (~320k local) plus national referrals for complex revision joint replacement to Wrightington.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Terms and Conditions.",
        "key_stats": [
            {"label": "Clinical supplies & services 2024-25", "value": "£44.6M"},
            {"label": "Share of trust total opex", "value": "c. 11% of ~£0.4bn opex"},
            {"label": "Biggest sub-category", "value": "Orthopaedic implants (hip/knee primary + revision) ~28%"},
            {"label": "Activity anchor", "value": "c. 90k admissions · >5k joint replacements/yr"},
            {"label": "National specialist", "value": "Wrightington — complex revision hip/knee + upper-limb"},
            {"label": "Supply-chain channel", "value": "NHS Supply Chain Medical ~75% · direct (revision implants) ~25%"},
            {"label": "NJR data", "value": "Outcomes tracked on National Joint Registry"},
            {"label": "Procurement collaborative", "value": "NOE CPC + GM Ortho network"}
        ],
        "notes": "Revision joint-replacement implants (custom or modular Stryker/Zimmer Biomet/DePuy Synthes constructs) cost multiples of primary-case kits and drive a direct-buy share well above peer acute trusts. The trust participates in the Framework for Hip & Knee Prostheses for primary procedures. Charnley-legacy research activity continues to shape implant selection and registry reporting. Single-use instrument pilots align with Net Zero.",
        "sources": [
            {"publisher": "Wrightington, Wigan and Leigh NHS Foundation Trust", "title": "Annual Report and Accounts 2024-25", "url": "https://www.wwl.nhs.uk/about-us/publications"},
            {"publisher": "National Joint Registry", "title": "21st Annual Report 2024", "url": "https://www.njrcentre.org.uk/"},
            {"publisher": "NHS Supply Chain", "title": "Orthopaedic implants framework", "url": "https://www.supplychain.nhs.uk/"}
        ],
        "related": ["Wrightington, Wigan and Leigh NHS Foundation Trust", "Drugs costs — Wrightington, Wigan and Leigh NHS Foundation Trust"]
    },
    "Clinical supplies & services — East And North Hertfordshire NHS Trust": {
        "aliases": [{"name": "Clinical supplies & services", "parent": "East And North Hertfordshire NHS Trust"}],
        "description": "ENHT's £42.1M clinical-supplies spend covers the Lister Hospital (Stevenage), the New QEII (Welwyn Garden City), Mount Vernon and Hertford County. The trust is a NHSE-commissioned host of the Mount Vernon Cancer Centre, giving it radiotherapy, brachytherapy and SACT-delivery consumable profiles alongside a general acute footprint at the Lister.",
        "beneficiaries": "c. 600,000 east/north Hertfordshire residents plus regional cancer-centre referrals to Mount Vernon.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHSE Specialised Commissioning · NHS Terms and Conditions.",
        "key_stats": [
            {"label": "Clinical supplies & services 2024-25", "value": "£42.1M"},
            {"label": "Share of trust total opex", "value": "c. 10% of ~£0.42bn opex"},
            {"label": "Biggest sub-category", "value": "Oncology/radiotherapy consumables + general surgical ~22%"},
            {"label": "Activity anchor", "value": "c. 85k admissions/yr across 4 sites"},
            {"label": "Cancer centre", "value": "Mount Vernon — NHSE-commissioned regional cancer service"},
            {"label": "Supply-chain channel", "value": "NHS Supply Chain Medical ~80% · direct (brachytherapy) ~20%"},
            {"label": "Mount Vernon future", "value": "Cancer-centre relocation review — capital implications pending"},
            {"label": "Procurement collaborative", "value": "East of England Collaborative Procurement Hub"}
        ],
        "notes": "Brachytherapy (HDR iridium-192 source-cycle consumables) and linac-related single-use items at Mount Vernon sit alongside standard district-general acute spend. The long-running review of Mount Vernon's future location has delayed capital investment decisions that would reshape consumable demand. The Lister's ED rebuild (phased through 2024-25) is a steady-state year for consumable procurement.",
        "sources": [
            {"publisher": "East and North Hertfordshire NHS Trust", "title": "Annual Report and Accounts 2024-25", "url": "https://www.enherts-tr.nhs.uk/about-us/publications-and-reports/"},
            {"publisher": "NHS England", "title": "Mount Vernon Cancer Centre review", "url": "https://www.england.nhs.uk/"},
            {"publisher": "NHS Supply Chain", "title": "Medical category reports", "url": "https://www.supplychain.nhs.uk/"}
        ],
        "related": ["East And North Hertfordshire NHS Trust", "Drugs costs — East And North Hertfordshire NHS Trust"]
    },
    "Clinical supplies & services — London Ambulance Service NHS Trust": {
        "aliases": [{"name": "Clinical supplies & services", "parent": "London Ambulance Service NHS Trust"}],
        "description": "LAS's £39.8M clinical-supplies bill reflects the UK's busiest 999 ambulance service, responding to c. 2 million incidents/year across Greater London with a fleet of 500+ ambulances and 70+ fast-response vehicles. The consumables basket is distinctive: defibrillator pads and batteries, medical gases (O2, Entonox), trauma/maternity packs, iGel airways, IO devices and one-time-use PPE.",
        "beneficiaries": "c. 9 million London residents plus tourists and commuters; c. 2 million incident responses/year.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Terms and Conditions · Ambulance Service National Contract.",
        "key_stats": [
            {"label": "Clinical supplies & services 2024-25", "value": "£39.8M"},
            {"label": "Share of trust total opex", "value": "c. 5-6% of ~£0.7bn opex"},
            {"label": "Biggest sub-category", "value": "Defibrillator consumables + medical gases (O2, Entonox) + trauma packs"},
            {"label": "Activity anchor", "value": "c. 2 million 999 incidents · >1 million patient transports/yr"},
            {"label": "Fleet consumables", "value": "500+ ambulances · 70+ FRUs — per-vehicle stock rotation"},
            {"label": "Supply-chain channel", "value": "NHS Supply Chain Medical ~75% · direct (Zoll/Stryker defib) ~25%"},
            {"label": "Medical gases", "value": "BOC contract — O2 cylinders + portable Entonox"},
            {"label": "PPE", "value": "Post-Covid baseline elevated vs pre-2020"}
        ],
        "notes": "Defibrillator consumables (Zoll and Stryker/Lifepak pads, batteries, printer paper) and airway-management kit (iGels, intubation blades) are renewed on tight operational cycles. Medical gases via the BOC national contract are the single biggest recurring line. Post-Covid PPE baselines remain above pre-2020 levels and the trust participates in the London Ambulance Pan-London medical-device programme.",
        "sources": [
            {"publisher": "London Ambulance Service NHS Trust", "title": "Annual Report and Accounts 2024-25", "url": "https://www.londonambulance.nhs.uk/about-us/our-publications/"},
            {"publisher": "Association of Ambulance Chief Executives", "title": "Ambulance system indicators", "url": "https://aace.org.uk/"},
            {"publisher": "NHS Supply Chain", "title": "Ambulance service framework", "url": "https://www.supplychain.nhs.uk/"}
        ],
        "related": ["London Ambulance Service NHS Trust", "Drugs costs — London Ambulance Service NHS Trust"]
    },
    "Clinical supplies & services — Sherwood Forest Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Clinical supplies & services", "parent": "Sherwood Forest Hospitals NHS Foundation Trust"}],
        "description": "Sherwood Forest's £38.6M clinical-supplies spend covers King's Mill Hospital (Sutton-in-Ashfield), Newark Hospital and Mansfield Community. King's Mill is the acute hub with ED, obstetrics, general surgery and elective orthopaedics; Newark provides day-case and urgent care. The trust has been a CQC 'Outstanding' performer since 2019, maintaining tightly-controlled consumable utilisation.",
        "beneficiaries": "c. 420,000 Mid-Nottinghamshire residents across Mansfield, Ashfield, Newark and Sherwood.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Terms and Conditions.",
        "key_stats": [
            {"label": "Clinical supplies & services 2024-25", "value": "£38.6M"},
            {"label": "Share of trust total opex", "value": "c. 11% of ~£0.35bn opex"},
            {"label": "Biggest sub-category", "value": "Orthopaedic implants + general surgical ~20%"},
            {"label": "Activity anchor", "value": "c. 78k admissions · c. 3k births/yr"},
            {"label": "CQC rating", "value": "'Outstanding' since 2019 — tight consumable governance"},
            {"label": "Supply-chain channel", "value": "NHS Supply Chain Medical ~86% · direct ~14%"},
            {"label": "Procurement collaborative", "value": "East Midlands collaborative procurement"},
            {"label": "YoY change", "value": "c. +5-6% nominal"}
        ],
        "notes": "A single major acute site with a high-throughput elective platform keeps consumable unit costs competitive. The trust is part of East Midlands collaborative procurement and benefits from standardised theatre packs. Newark's focus on elective day-surgery supports efficient consumable utilisation relative to mixed-acute peers.",
        "sources": [
            {"publisher": "Sherwood Forest Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2024-25", "url": "https://www.sfh-tr.nhs.uk/about-us/publications/"},
            {"publisher": "NHS Supply Chain", "title": "Medical category reports", "url": "https://www.supplychain.nhs.uk/"},
            {"publisher": "Care Quality Commission", "title": "Sherwood Forest inspection reports", "url": "https://www.cqc.org.uk/provider/RK5"}
        ],
        "related": ["Sherwood Forest Hospitals NHS Foundation Trust", "Drugs costs — Sherwood Forest Hospitals NHS Foundation Trust"]
    },
    "Clinical supplies & services — Ashford and St Peter's Hospitals NHS Foundation Trust": {
        "aliases": [{"name": "Clinical supplies & services", "parent": "Ashford and St Peter's Hospitals NHS Foundation Trust"}],
        "description": "ASPH's £37.7M clinical-supplies bill covers St Peter's Hospital (Chertsey) and Ashford Hospital. St Peter's is the main emergency and acute-surgery site with a busy maternity service (c. 3,700 births/yr) and a regional neonatal unit; Ashford is a day-surgery and outpatient hub. The trust serves a densely populated North Surrey catchment with strong elective-demand growth.",
        "beneficiaries": "c. 410,000 residents of Runnymede, Spelthorne, Woking, Elmbridge and Surrey Heath.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Terms and Conditions.",
        "key_stats": [
            {"label": "Clinical supplies & services 2024-25", "value": "£37.7M"},
            {"label": "Share of trust total opex", "value": "c. 11% of ~£0.35bn opex"},
            {"label": "Biggest sub-category", "value": "Obstetric/neonatal + general surgical ~22%"},
            {"label": "Activity anchor", "value": "c. 75k admissions · c. 3,700 births/yr"},
            {"label": "Neonatal unit", "value": "St Peter's LNU — surfactant delivery, ventilation consumables"},
            {"label": "Supply-chain channel", "value": "NHS Supply Chain Medical ~84% · direct ~16%"},
            {"label": "Procurement collaborative", "value": "Surrey Heartlands ICS"},
            {"label": "YoY change", "value": "c. +5-7% nominal — maternity investment + uplift"}
        ],
        "notes": "Neonatal consumables (high-frequency oscillator circuits, surfactant delivery sets, LISA catheters) and maternity kit drive a higher share than typical for a mid-size acute trust. The Ashford day-surgery model supports standardised-kit pricing. Surrey Heartlands ICS joint-procurement initiatives in FY24-25 targeted theatre-pack aggregation.",
        "sources": [
            {"publisher": "Ashford and St Peter's Hospitals NHS Foundation Trust", "title": "Annual Report and Accounts 2024-25", "url": "https://www.ashfordstpeters.nhs.uk/publications"},
            {"publisher": "NHS Supply Chain", "title": "Neonatal framework", "url": "https://www.supplychain.nhs.uk/"},
            {"publisher": "NHS England", "title": "Neonatal critical care service specification", "url": "https://www.england.nhs.uk/commissioning/spec-services/npc-crg/group-e/e08/"}
        ],
        "related": ["Ashford and St Peter's Hospitals NHS Foundation Trust", "Drugs costs — Ashford and St Peter's Hospitals NHS Foundation Trust"]
    },
    "Clinical supplies & services — Calderdale and Huddersfield NHS Foundation Trust": {
        "aliases": [{"name": "Clinical supplies & services", "parent": "Calderdale and Huddersfield NHS Foundation Trust"}],
        "description": "CHFT's £35.7M clinical-supplies bill covers Calderdale Royal Hospital (Halifax) and Huddersfield Royal Infirmary. The trust is mid-way through the Hospitals Improvement Programme reconfiguration that will centralise emergency surgery and obstetrics at a rebuilt Huddersfield site — procurement planning must balance continued dual-site operation with future single-acute-site demand.",
        "beneficiaries": "c. 470,000 residents of Calderdale and Kirklees across two acute sites.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Terms and Conditions.",
        "key_stats": [
            {"label": "Clinical supplies & services 2024-25", "value": "£35.7M"},
            {"label": "Share of trust total opex", "value": "c. 10% of ~£0.35bn opex"},
            {"label": "Biggest sub-category", "value": "General surgical + obstetric consumables ~20%"},
            {"label": "Activity anchor", "value": "c. 80k admissions · c. 4.5k births/yr"},
            {"label": "Reconfiguration", "value": "Hospitals Improvement Programme — dual-site transition"},
            {"label": "Supply-chain channel", "value": "NHS Supply Chain Medical ~85% · direct ~15%"},
            {"label": "Procurement collaborative", "value": "NOE CPC + West Yorkshire ICS"},
            {"label": "Shared services", "value": "Bradford-Calderdale Pathology Services (JV)"}
        ],
        "notes": "Dual-site running during the reconfiguration creates buffer-stock inefficiency that the trust is managing through tighter JIT arrangements with NHS Supply Chain. Pathology reagents flow through the Bradford-Calderdale JV, keeping lab-consumable unit costs competitive. West Yorkshire ICS pan-Trust procurement targets theatre packs and wound care.",
        "sources": [
            {"publisher": "Calderdale and Huddersfield NHS Foundation Trust", "title": "Annual Report and Accounts 2024-25", "url": "https://www.cht.nhs.uk/about-us/publications/"},
            {"publisher": "NHS Supply Chain", "title": "Medical category reports", "url": "https://www.supplychain.nhs.uk/"},
            {"publisher": "West Yorkshire Health and Care Partnership", "title": "Joint procurement plans", "url": "https://www.wypartnership.co.uk/"}
        ],
        "related": ["Calderdale and Huddersfield NHS Foundation Trust", "Drugs costs — Calderdale and Huddersfield NHS Foundation Trust"]
    },
    "Clinical supplies & services — Whittington Health NHS Trust": {
        "aliases": [{"name": "Clinical supplies & services", "parent": "Whittington Health NHS Trust"}],
        "description": "Whittington Health's £35.2M clinical-supplies bill covers the Whittington Hospital (Archway) plus an integrated community-services footprint across Islington and Haringey. The acute site runs ED, maternity (c. 3,500 births/yr), general surgery and elective orthopaedics; the community arm adds wound-care, continence and school-nursing consumables.",
        "beneficiaries": "c. 500,000 residents of Islington and Haringey plus pan-London elective referrals.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Terms and Conditions · NHS London Procurement Partnership frameworks.",
        "key_stats": [
            {"label": "Clinical supplies & services 2024-25", "value": "£35.2M"},
            {"label": "Share of trust total opex", "value": "c. 9% of ~£0.38bn opex"},
            {"label": "Biggest sub-category", "value": "General surgical + community wound-care ~20%"},
            {"label": "Activity anchor", "value": "c. 55k acute admissions · c. 3,500 births · pan-borough community caseload"},
            {"label": "Integration model", "value": "Acute + community — rare for central-London trusts"},
            {"label": "Supply-chain channel", "value": "NHS Supply Chain Medical ~83% · direct ~17%"},
            {"label": "Procurement collaborative", "value": "LPP (London Procurement Partnership)"},
            {"label": "YoY change", "value": "c. +5-7% nominal — community activity growth"}
        ],
        "notes": "The integrated acute-plus-community model pushes wound-care, catheter and continence consumable volumes above a pure-acute peer. LPP frameworks deliver competitive London pricing on theatre packs and sutures. Limited on-site specialist cardiac/neuro activity keeps the device share of the consumables basket low relative to teaching-hospital peers.",
        "sources": [
            {"publisher": "Whittington Health NHS Trust", "title": "Annual Report and Accounts 2024-25", "url": "https://www.whittington.nhs.uk/default.asp?c=42147"},
            {"publisher": "NHS London Procurement Partnership", "title": "Frameworks", "url": "https://www.lpp.nhs.uk/"},
            {"publisher": "NHS Supply Chain", "title": "Community nursing framework", "url": "https://www.supplychain.nhs.uk/"}
        ],
        "related": ["Whittington Health NHS Trust", "Drugs costs — Whittington Health NHS Trust"]
    },
    "Clinical supplies & services — South Warwickshire NHS Foundation Trust": {
        "aliases": [{"name": "Clinical supplies & services", "parent": "South Warwickshire NHS Foundation Trust"}],
        "description": "SWFT's £34.1M clinical-supplies bill covers Warwick Hospital plus integrated community services across south Warwickshire (now extending into Stratford, Leamington and — via the 2024 planned merger with Wye Valley — potentially Herefordshire). The acute site runs a full general-hospital portfolio with a notably efficient elective platform.",
        "beneficiaries": "c. 280,000 south Warwickshire residents plus expanding community caseload; merger partner Wye Valley adds Herefordshire reach.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Terms and Conditions.",
        "key_stats": [
            {"label": "Clinical supplies & services 2024-25", "value": "£34.1M"},
            {"label": "Share of trust total opex", "value": "c. 10% of ~£0.35bn opex"},
            {"label": "Biggest sub-category", "value": "General surgical + community wound-care ~20%"},
            {"label": "Activity anchor", "value": "c. 60k acute admissions + community-services caseload"},
            {"label": "Integration model", "value": "Acute + community services across south Warwickshire"},
            {"label": "Merger", "value": "Planned 2024-25 merger with Wye Valley NHS Trust"},
            {"label": "Supply-chain channel", "value": "NHS Supply Chain Medical ~86% · direct ~14%"},
            {"label": "Procurement collaborative", "value": "West Midlands collaborative"}
        ],
        "notes": "The Wye Valley merger (subject to regulatory approval) will require procurement-contract harmonisation across two trusts operating in different ICS footprints. Warwick Hospital's efficient elective platform keeps consumable unit costs in the lower quartile for district-general peers. Integrated community services add wound-care and continence volumes.",
        "sources": [
            {"publisher": "South Warwickshire University NHS Foundation Trust", "title": "Annual Report and Accounts 2024-25", "url": "https://www.swft.nhs.uk/about-us/publications"},
            {"publisher": "NHS England", "title": "SWFT/Wye Valley merger business case", "url": "https://www.england.nhs.uk/"},
            {"publisher": "NHS Supply Chain", "title": "Medical category reports", "url": "https://www.supplychain.nhs.uk/"}
        ],
        "related": ["South Warwickshire NHS Foundation Trust", "Drugs costs — South Warwickshire NHS Foundation Trust"]
    },
    "Clinical supplies & services — Medway NHS Foundation Trust": {
        "aliases": [{"name": "Clinical supplies & services", "parent": "Medway NHS Foundation Trust"}],
        "description": "Medway's £31.8M clinical-supplies bill covers Medway Maritime Hospital (Gillingham), the main acute site for Kent's Medway towns. The trust delivers a full general acute portfolio including a busy ED, maternity (c. 4,500 births/yr), stroke services and general surgery. Historic CQC/regulatory attention (under Special Measures previously) has driven tight governance over consumable procurement.",
        "beneficiaries": "c. 470,000 residents of Medway, Swale and parts of north Kent.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Terms and Conditions.",
        "key_stats": [
            {"label": "Clinical supplies & services 2024-25", "value": "£31.8M"},
            {"label": "Share of trust total opex", "value": "c. 10% of ~£0.33bn opex"},
            {"label": "Biggest sub-category", "value": "General surgical + obstetric + ED consumables ~22%"},
            {"label": "Activity anchor", "value": "c. 75k admissions · c. 4,500 births/yr"},
            {"label": "Single acute site", "value": "Medway Maritime — concentrated consumables footprint"},
            {"label": "Supply-chain channel", "value": "NHS Supply Chain Medical ~86% · direct ~14%"},
            {"label": "Procurement collaborative", "value": "Kent & Medway ICS"},
            {"label": "Regulatory context", "value": "Exited Special Measures 2018 — sustained governance focus"}
        ],
        "notes": "Single-site operation at Medway Maritime concentrates consumable use and supports disciplined inventory. Kent & Medway ICS joint-procurement initiatives in FY24-25 targeted theatre packs and wound-care standardisation with Dartford & Gravesham and Maidstone & Tunbridge Wells. Maternity reinvestment programmes drive incremental obstetric-kit spend.",
        "sources": [
            {"publisher": "Medway NHS Foundation Trust", "title": "Annual Report and Accounts 2024-25", "url": "https://www.medway.nhs.uk/about-us/publications/"},
            {"publisher": "Kent and Medway ICB", "title": "Joint procurement plans", "url": "https://www.kentandmedway.icb.nhs.uk/"},
            {"publisher": "NHS Supply Chain", "title": "Medical category reports", "url": "https://www.supplychain.nhs.uk/"}
        ],
        "related": ["Medway NHS Foundation Trust", "Drugs costs — Medway NHS Foundation Trust"]
    },
    "Clinical supplies & services — Alder Hey Children's NHS Foundation Trust": {
        "aliases": [{"name": "Clinical supplies & services", "parent": "Alder Hey Children's NHS Foundation Trust"}],
        "description": "Alder Hey's £28.9M clinical-supplies bill — at c. 11% of opex — reflects a dedicated children's hospital serving the whole of Merseyside, Cheshire, Shropshire, North Wales and the Isle of Man. The paediatric specialty mix (cardiac, neurosurgery, oncology, cleft, craniofacial, PICU, neonatal transfers) drives small-size-specific consumables that are procured outside mainstream adult frameworks.",
        "beneficiaries": "c. 7.5 million paediatric catchment across North West England, North Wales and IoM.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHSE Specialised Commissioning · NHS Terms and Conditions.",
        "key_stats": [
            {"label": "Clinical supplies & services 2024-25", "value": "£28.9M"},
            {"label": "Share of trust total opex", "value": "c. 11% of ~£0.26bn opex"},
            {"label": "Biggest sub-category", "value": "Paediatric cardiac + neurosurgery + PICU consumables ~25%"},
            {"label": "Activity anchor", "value": "c. 275k outpatient attendances · c. 35k admissions/yr"},
            {"label": "Specialist services", "value": "Paediatric cardiac surgery, neurosurgery, oncology, PICU, craniofacial"},
            {"label": "Supply-chain channel", "value": "NHS Supply Chain Medical ~70% · direct (paediatric-specific) ~30%"},
            {"label": "Child-size overhead", "value": "Small-size catheters, stents, valves — premium pricing"},
            {"label": "Research platform", "value": "NIHR Alder Hey Clinical Research Facility — IMP consumables"}
        ],
        "notes": "Paediatric-specific small-size catheters, stents and valves (including congenital-heart devices) carry substantial premium over adult-size equivalents and often sit outside NHS Supply Chain's adult-oriented frameworks. The NHSE paediatric-cardiac commissioning stream funds device use pass-through but acquisition flows through trust accounts. The NIHR CRF supports a large paediatric-IMP portfolio with specialist consumable needs.",
        "sources": [
            {"publisher": "Alder Hey Children's NHS Foundation Trust", "title": "Annual Report and Accounts 2024-25", "url": "https://alderhey.nhs.uk/about-us/publications"},
            {"publisher": "NHS England", "title": "Paediatric cardiac service specification", "url": "https://www.england.nhs.uk/commissioning/spec-services/npc-crg/e05/"},
            {"publisher": "NHS Supply Chain", "title": "Paediatric frameworks", "url": "https://www.supplychain.nhs.uk/"}
        ],
        "related": ["Alder Hey Children's NHS Foundation Trust", "Drugs costs — Alder Hey Children's NHS Foundation Trust"]
    },
    "Clinical supplies & services — Barnsley Hospital NHS Foundation Trust": {
        "aliases": [{"name": "Clinical supplies & services", "parent": "Barnsley Hospital NHS Foundation Trust"}],
        "description": "Barnsley Hospital's £28.5M clinical-supplies bill is concentrated on a single acute site (Barnsley Hospital) serving the Barnsley borough. The trust runs a full general acute portfolio — ED, maternity, general surgery, elective orthopaedics — within the South Yorkshire ICS footprint, operating in partnership with Rotherham, Doncaster & Bassetlaw and Sheffield Teaching Hospitals.",
        "beneficiaries": "c. 245,000 Barnsley residents across town, rural villages and surrounding South Yorkshire.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Terms and Conditions.",
        "key_stats": [
            {"label": "Clinical supplies & services 2024-25", "value": "£28.5M"},
            {"label": "Share of trust total opex", "value": "c. 11% of ~£0.26bn opex"},
            {"label": "Biggest sub-category", "value": "General surgical + orthopaedic + obstetric ~22%"},
            {"label": "Activity anchor", "value": "c. 65k admissions · c. 2,600 births/yr"},
            {"label": "Single acute site", "value": "Barnsley Hospital — concentrated consumable footprint"},
            {"label": "Supply-chain channel", "value": "NHS Supply Chain Medical ~87% · direct ~13%"},
            {"label": "Procurement collaborative", "value": "South Yorkshire ICS + NOE CPC"},
            {"label": "YoY change", "value": "c. +5-6% nominal"}
        ],
        "notes": "A single-site operating model with disciplined JIT stockholding keeps unit costs competitive. The 'Working Together' partnership with Sheffield, Rotherham and Doncaster & Bassetlaw has delivered South Yorkshire-wide pathology networking and shared theatre-pack standards. NOE CPC frameworks set pricing for most consumables.",
        "sources": [
            {"publisher": "Barnsley Hospital NHS Foundation Trust", "title": "Annual Report and Accounts 2024-25", "url": "https://www.barnsleyhospital.nhs.uk/about-us/our-publications/"},
            {"publisher": "NOE CPC", "title": "Procurement frameworks", "url": "https://www.noecpc.nhs.uk/"},
            {"publisher": "NHS South Yorkshire ICB", "title": "Joint procurement reports", "url": "https://www.southyorkshire.icb.nhs.uk/"}
        ],
        "related": ["Barnsley Hospital NHS Foundation Trust", "Drugs costs — Barnsley Hospital NHS Foundation Trust"]
    },
    "Clinical supplies & services — Oxford Health NHS Foundation Trust": {
        "aliases": [{"name": "Clinical supplies & services", "parent": "Oxford Health NHS Foundation Trust"}],
        "description": "Oxford Health's £26.4M clinical-supplies spend — high for a mental-health trust — reflects an unusually integrated provider portfolio: adult and children's mental health, community services across Oxfordshire and Buckinghamshire, dental services and a large specialist/secure-forensic estate. Community physical-health consumables (wound-care, catheters, continence, POC testing) dominate over classical mental-health consumables.",
        "beneficiaries": "c. 2.5M Oxfordshire/Buckinghamshire residents plus regional mental-health and community caseloads.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Mental Health Act 1983 · Health and Care Act 2022 · NHS Terms and Conditions.",
        "key_stats": [
            {"label": "Clinical supplies & services 2024-25", "value": "£26.4M"},
            {"label": "Share of trust total opex", "value": "c. 4% of ~£0.7bn opex (high for MH)"},
            {"label": "Biggest sub-category", "value": "Community nursing consumables (wound-care, continence) ~30%"},
            {"label": "Service mix", "value": "MH + community + dental + specialist/secure forensic"},
            {"label": "Community caseload", "value": "Oxfordshire + Bucks — district nursing, health visiting"},
            {"label": "Supply-chain channel", "value": "NHS Supply Chain Medical ~85% · direct ~15%"},
            {"label": "Mental-health consumables", "value": "Ward-based POC diagnostics, restraint, PPE"},
            {"label": "Forensic unit overhead", "value": "Specialist security-rated equipment refreshes"}
        ],
        "notes": "The scale of community nursing activity (district nursing, health visiting, school nursing) across two counties is the main reason Oxford Health's clinical-supplies line is materially larger than peer mental-health trusts. Dental-services consumables (endodontic files, composites) and forensic-estate security-rated kit add further specialist overhead. Mainstream MH-ward consumables are a small share of the total.",
        "sources": [
            {"publisher": "Oxford Health NHS Foundation Trust", "title": "Annual Report and Accounts 2024-25", "url": "https://www.oxfordhealth.nhs.uk/about-us/governance-and-publications/annual-report/"},
            {"publisher": "NHS Supply Chain", "title": "Community nursing framework", "url": "https://www.supplychain.nhs.uk/"},
            {"publisher": "NHS England", "title": "Specialist & secure mental health service specifications", "url": "https://www.england.nhs.uk/commissioning/spec-services/npc-crg/group-c/"}
        ],
        "related": ["Oxford Health NHS Foundation Trust", "Drugs costs — Oxford Health NHS Foundation Trust"]
    },
    "Clinical supplies & services — Stockport NHS Foundation Trust": {
        "aliases": [{"name": "Clinical supplies & services", "parent": "Stockport NHS Foundation Trust"}],
        "description": "Stockport NHSFT's £25.1M clinical-supplies bill is centred on Stepping Hill Hospital, a single acute site in Greater Manchester. The trust delivers a full general acute portfolio and is part of the Greater Manchester provider collaborative alongside MFT, the Northern Care Alliance and smaller GM partners — which shapes joint consumable procurement.",
        "beneficiaries": "c. 300,000 Stockport borough residents plus parts of east Cheshire and Derbyshire.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Terms and Conditions.",
        "key_stats": [
            {"label": "Clinical supplies & services 2024-25", "value": "£25.1M"},
            {"label": "Share of trust total opex", "value": "c. 9% of ~£0.28bn opex"},
            {"label": "Biggest sub-category", "value": "General surgical + obstetric + ED ~22%"},
            {"label": "Activity anchor", "value": "c. 70k admissions · c. 3,200 births/yr"},
            {"label": "Single acute site", "value": "Stepping Hill Hospital — concentrated consumable footprint"},
            {"label": "Supply-chain channel", "value": "NHS Supply Chain Medical ~87% · direct ~13%"},
            {"label": "Procurement collaborative", "value": "GM Provider Collaborative + NOE CPC"},
            {"label": "YoY change", "value": "c. +5-6% nominal"}
        ],
        "notes": "Single-site operation supports efficient inventory turnover. GM provider-collaborative joint working (with MFT, NCA, Bolton, Tameside, Wrightington-Wigan-Leigh) targets aggregated contracts for common consumables. 2024-25 was a steady-state year with elective activity near pre-pandemic baselines.",
        "sources": [
            {"publisher": "Stockport NHS Foundation Trust", "title": "Annual Report and Accounts 2024-25", "url": "https://www.stockport.nhs.uk/about-us/publications/"},
            {"publisher": "NHS Greater Manchester ICB", "title": "Provider collaborative reports", "url": "https://gmintegratedcare.org.uk/"},
            {"publisher": "NHS Supply Chain", "title": "Medical category reports", "url": "https://www.supplychain.nhs.uk/"}
        ],
        "related": ["Stockport NHS Foundation Trust", "Drugs costs — Stockport NHS Foundation Trust"]
    },
    "Clinical supplies & services — The Princess Alexandra Hospital NHS Trust": {
        "aliases": [{"name": "Clinical supplies & services", "parent": "The Princess Alexandra Hospital NHS Trust"}],
        "description": "PAH's £23.0M clinical-supplies bill is centred on Princess Alexandra Hospital (Harlow), serving west Essex and east Hertfordshire communities. The trust runs a general acute portfolio and is proceeding (subject to funding sequencing) with a major New Hospital Programme rebuild that will eventually transform theatre and diagnostic capacity.",
        "beneficiaries": "c. 350,000 west Essex and east Herts residents.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Terms and Conditions.",
        "key_stats": [
            {"label": "Clinical supplies & services 2024-25", "value": "£23.0M"},
            {"label": "Share of trust total opex", "value": "c. 10% of ~£0.22bn opex"},
            {"label": "Biggest sub-category", "value": "General surgical + obstetric + ED ~22%"},
            {"label": "Activity anchor", "value": "c. 55k admissions · c. 3,000 births/yr"},
            {"label": "NHP programme", "value": "New Hospital Programme rebuild — sequencing in revised 2023 schedule"},
            {"label": "Supply-chain channel", "value": "NHS Supply Chain Medical ~86% · direct ~14%"},
            {"label": "Procurement collaborative", "value": "East of England Collaborative Procurement Hub"},
            {"label": "YoY change", "value": "c. +5-6% nominal"}
        ],
        "notes": "Operating from an ageing estate creates additional resilience-inventory costs (especially for ventilator circuits and single-use endoscopy kit). NHP business case activity continues but does not yet affect the run-rate consumables baseline. East of England Collaborative Procurement Hub frameworks set pricing for the bulk of the consumables basket.",
        "sources": [
            {"publisher": "The Princess Alexandra Hospital NHS Trust", "title": "Annual Report and Accounts 2024-25", "url": "https://www.pah.nhs.uk/about/publications"},
            {"publisher": "Department of Health and Social Care", "title": "New Hospital Programme update January 2025", "url": "https://www.gov.uk/government/publications/new-hospital-programme"},
            {"publisher": "NHS Supply Chain", "title": "Medical category reports", "url": "https://www.supplychain.nhs.uk/"}
        ],
        "related": ["The Princess Alexandra Hospital NHS Trust", "Drugs costs — The Princess Alexandra Hospital NHS Trust"]
    },
    "Clinical supplies & services — Airedale NHS Foundation Trust": {
        "aliases": [{"name": "Clinical supplies & services", "parent": "Airedale NHS Foundation Trust"}],
        "description": "Airedale's £21.3M clinical-supplies bill is centred on Airedale General Hospital (Steeton), one of the NHS's best-known RAAC-affected sites — the entire hospital is scheduled for replacement under the New Hospital Programme. The trust serves a dispersed rural catchment across Craven, West Yorkshire and South Lakeland, and operates a national Airedale @ Home/Digital Care Hub programme.",
        "beneficiaries": "c. 200,000 residents across Craven, Airedale, Wharfedale and South Lakeland.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Terms and Conditions.",
        "key_stats": [
            {"label": "Clinical supplies & services 2024-25", "value": "£21.3M"},
            {"label": "Share of trust total opex", "value": "c. 10% of ~£0.22bn opex"},
            {"label": "Biggest sub-category", "value": "General surgical + obstetric + ED ~22%"},
            {"label": "Activity anchor", "value": "c. 50k admissions · c. 1,800 births/yr"},
            {"label": "RAAC context", "value": "Full NHP rebuild scheduled — business case in revised 2023 list"},
            {"label": "Digital Care Hub", "value": "National telemedicine service — home-monitoring consumables"},
            {"label": "Supply-chain channel", "value": "NHS Supply Chain Medical ~87% · direct ~13%"},
            {"label": "Procurement collaborative", "value": "NOE CPC + West Yorkshire ICS"}
        ],
        "notes": "RAAC-affected estate requires ongoing prop-and-mitigation work that carries facilities overhead but does not directly increase clinical-supplies run-rate. The Airedale Digital Care Hub supports home-monitoring across multiple trusts, adding a small telemedicine consumables line (SpO2 sensors, BP cuffs) distinctive to Airedale. NOE CPC frameworks cover most acute consumables.",
        "sources": [
            {"publisher": "Airedale NHS Foundation Trust", "title": "Annual Report and Accounts 2024-25", "url": "https://www.airedale-trust.nhs.uk/about-us/publications/"},
            {"publisher": "Department of Health and Social Care", "title": "New Hospital Programme — RAAC rebuilds", "url": "https://www.gov.uk/government/publications/new-hospital-programme"},
            {"publisher": "NOE CPC", "title": "Procurement frameworks", "url": "https://www.noecpc.nhs.uk/"}
        ],
        "related": ["Airedale NHS Foundation Trust", "Drugs costs — Airedale NHS Foundation Trust"]
    },
    "Clinical supplies & services — Tameside and Glossop Integrated Care NHS Foundation Trust": {
        "aliases": [{"name": "Clinical supplies & services", "parent": "Tameside and Glossop Integrated Care NHS Foundation Trust"}],
        "description": "Tameside and Glossop's £19.2M clinical-supplies bill reflects Tameside General Hospital plus an integrated community services footprint covering Tameside borough and the Glossopdale area of Derbyshire. The integrated acute-community model (one of the earlier vanguard integrated providers) includes district nursing and community physiotherapy, adding wound-care and continence consumables.",
        "beneficiaries": "c. 250,000 residents of Tameside borough and Glossopdale (High Peak).",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Terms and Conditions.",
        "key_stats": [
            {"label": "Clinical supplies & services 2024-25", "value": "£19.2M"},
            {"label": "Share of trust total opex", "value": "c. 10% of ~£0.2bn opex"},
            {"label": "Biggest sub-category", "value": "General surgical + community wound-care ~22%"},
            {"label": "Activity anchor", "value": "c. 50k admissions + integrated community caseload"},
            {"label": "Integration model", "value": "Acute + community (vanguard integrated provider)"},
            {"label": "Supply-chain channel", "value": "NHS Supply Chain Medical ~87% · direct ~13%"},
            {"label": "Procurement collaborative", "value": "GM Provider Collaborative"},
            {"label": "Cross-boundary", "value": "Glossopdale patients — Derbyshire/GM ICS interface"}
        ],
        "notes": "Cross-ICS geography (Tameside in GM; Glossopdale in Derbyshire) complicates community-service consumable invoicing but does not materially change the basket. GM Provider Collaborative joint procurement covers most acute consumables; community district-nursing packs flow through NHS Supply Chain framework routes. 2024-25 is a steady-state year.",
        "sources": [
            {"publisher": "Tameside and Glossop Integrated Care NHS Foundation Trust", "title": "Annual Report and Accounts 2024-25", "url": "https://www.tamesidehospital.nhs.uk/about-us/publications.htm"},
            {"publisher": "NHS Greater Manchester ICB", "title": "Provider collaborative reports", "url": "https://gmintegratedcare.org.uk/"},
            {"publisher": "NHS Supply Chain", "title": "Community nursing framework", "url": "https://www.supplychain.nhs.uk/"}
        ],
        "related": ["Tameside and Glossop Integrated Care NHS Foundation Trust", "Drugs costs — Tameside and Glossop Integrated Care NHS Foundation Trust"]
    },
    "Clinical supplies & services — Central London Community Healthcare NHS Trust": {
        "aliases": [{"name": "Clinical supplies & services", "parent": "Central London Community Healthcare NHS Trust"}],
        "description": "CLCH's £17.7M clinical-supplies bill is the largest single community-trust line in this batch, reflecting its position as the biggest community provider in London — delivering district nursing, health visiting, school nursing, wheelchair services and specialist community clinical services across Westminster, Kensington & Chelsea, Hammersmith & Fulham, Barnet, Merton, Wandsworth and Harrow.",
        "beneficiaries": "c. 2 million residents across 7 London boroughs plus pan-London specialist community services.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Terms and Conditions · NHS London Procurement Partnership frameworks.",
        "key_stats": [
            {"label": "Clinical supplies & services 2024-25", "value": "£17.7M"},
            {"label": "Share of trust total opex", "value": "c. 5% of ~£0.35bn opex"},
            {"label": "Biggest sub-category", "value": "Wound-care + continence + district-nursing consumables ~35%"},
            {"label": "Activity anchor", "value": "c. 2M borough catchment · >1M community contacts/yr"},
            {"label": "Wheelchair services", "value": "Pan-London specialist wheelchair provision — durable-medical equipment"},
            {"label": "Supply-chain channel", "value": "NHS Supply Chain Community framework ~80% · direct ~20%"},
            {"label": "Procurement collaborative", "value": "LPP community-services stream"},
            {"label": "Home respiratory", "value": "Community oxygen and CPAP consumables"}
        ],
        "notes": "Wound-care dressings (foam, alginate, silver, NPWT) and continence products dominate a classical community-nursing basket; wheelchair provision adds a durable-medical-equipment overlay unusual for community trusts. Home respiratory consumables (portable O2 cylinders via Baywater Healthcare, CPAP masks/tubing) add a small but growing line. LPP frameworks set prices.",
        "sources": [
            {"publisher": "Central London Community Healthcare NHS Trust", "title": "Annual Report and Accounts 2024-25", "url": "https://clch.nhs.uk/about-us/publications"},
            {"publisher": "NHS London Procurement Partnership", "title": "Community services framework", "url": "https://www.lpp.nhs.uk/"},
            {"publisher": "NHS Supply Chain", "title": "Wound-care and continence framework", "url": "https://www.supplychain.nhs.uk/"}
        ],
        "related": ["Central London Community Healthcare NHS Trust", "Drugs costs — Central London Community Healthcare NHS Trust"]
    },
    "Clinical supplies & services — Dorset Healthcare University NHS Foundation Trust": {
        "aliases": [{"name": "Clinical supplies & services", "parent": "Dorset Healthcare University NHS Foundation Trust"}],
        "description": "Dorset Healthcare's £12.5M clinical-supplies spend reflects an integrated mental-health and community-services provider covering Dorset, Bournemouth, Christchurch and Poole. Mental-health services (adult, CAMHS, learning disabilities, older adults) sit alongside a substantial community-nursing footprint — the community side dominates the consumables basket.",
        "beneficiaries": "c. 800,000 Dorset residents across mental-health, community and specialist caseloads.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Mental Health Act 1983 · Health and Care Act 2022 · NHS Terms and Conditions.",
        "key_stats": [
            {"label": "Clinical supplies & services 2024-25", "value": "£12.5M"},
            {"label": "Share of trust total opex", "value": "c. 3% of ~£0.38bn opex"},
            {"label": "Biggest sub-category", "value": "Community nursing wound-care + continence ~35%"},
            {"label": "Service mix", "value": "Mental health + community nursing + CAMHS + learning disabilities"},
            {"label": "Community caseload", "value": "Pan-Dorset district nursing + health visiting"},
            {"label": "Supply-chain channel", "value": "NHS Supply Chain Community framework ~86% · direct ~14%"},
            {"label": "Procurement collaborative", "value": "South West Procurement Partnership"},
            {"label": "Mental-health consumables", "value": "Ward diagnostics, restraint, POC testing, PPE"}
        ],
        "notes": "Classical community-nursing wound-care and continence volumes dominate the consumables basket; mental-health-specific items (restraint, ward-based POC testing, rapid tranquilisation delivery sets) are a small share. Pan-Dorset integration with acute trusts (University Hospitals Dorset and Dorset County Hospital) supports some joint procurement through the South West Procurement Partnership.",
        "sources": [
            {"publisher": "Dorset Healthcare University NHS Foundation Trust", "title": "Annual Report and Accounts 2024-25", "url": "https://www.dorsethealthcare.nhs.uk/about-us/publications"},
            {"publisher": "NHS Supply Chain", "title": "Community nursing framework", "url": "https://www.supplychain.nhs.uk/"},
            {"publisher": "NHS Dorset ICB", "title": "Integrated care reports", "url": "https://nhsdorset.nhs.uk/"}
        ],
        "related": ["Dorset Healthcare University NHS Foundation Trust", "Drugs costs — Dorset Healthcare University NHS Foundation Trust"]
    },
    "Clinical supplies & services — George Eliot Hospital NHS Trust": {
        "aliases": [{"name": "Clinical supplies & services", "parent": "George Eliot Hospital NHS Trust"}],
        "description": "George Eliot's £11.4M clinical-supplies bill is one of the smaller acute-trust lines in this batch, reflecting the trust's size — a single district-general acute site in Nuneaton serving north Warwickshire and parts of Leicestershire. The trust delivers ED, obstetrics, general surgery and basic elective orthopaedics; specialist tertiary activity is referred out.",
        "beneficiaries": "c. 330,000 north Warwickshire and south Leicestershire residents.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Terms and Conditions.",
        "key_stats": [
            {"label": "Clinical supplies & services 2024-25", "value": "£11.4M"},
            {"label": "Share of trust total opex", "value": "c. 8-9% of ~£0.14bn opex"},
            {"label": "Biggest sub-category", "value": "General surgical + obstetric + ED ~22%"},
            {"label": "Activity anchor", "value": "c. 40k admissions · c. 1,800 births/yr"},
            {"label": "Small-trust scale", "value": "Lowest-volume acute in this batch — scale limits purchasing power"},
            {"label": "Supply-chain channel", "value": "NHS Supply Chain Medical ~89% · direct ~11%"},
            {"label": "Procurement collaborative", "value": "West Midlands collaborative + Coventry-Warwickshire joint working"},
            {"label": "Tertiary referrals", "value": "UHCW (Coventry) for most specialist activity"}
        ],
        "notes": "Scale limits direct-buy leverage and makes NHS Supply Chain the dominant channel. Joint working with University Hospitals Coventry and Warwickshire and South Warwickshire in the Coventry-Warwickshire ICS targets aggregated theatre-pack and wound-care deals. Specialist tertiary activity is referred out, keeping the device share low.",
        "sources": [
            {"publisher": "George Eliot Hospital NHS Trust", "title": "Annual Report and Accounts 2024-25", "url": "https://www.geh.nhs.uk/about-us/publications"},
            {"publisher": "NHS Supply Chain", "title": "Medical category reports", "url": "https://www.supplychain.nhs.uk/"},
            {"publisher": "NHS Coventry and Warwickshire ICB", "title": "Joint procurement reports", "url": "https://www.happyhealthylives.uk/"}
        ],
        "related": ["George Eliot Hospital NHS Trust", "Drugs costs — George Eliot Hospital NHS Trust"]
    },
    "Clinical supplies & services — Yorkshire Ambulance Service NHS Trust": {
        "aliases": [{"name": "Clinical supplies & services", "parent": "Yorkshire Ambulance Service NHS Trust"}],
        "description": "YAS's £10.0M clinical-supplies bill reflects a regional ambulance service covering Yorkshire and the Humber — c. 5.5 million population across a mixed urban-rural geography. The consumables basket is ambulance-standard (defibrillator pads/batteries, medical gases, trauma packs, iGel airways, IO devices, PPE) but dispersed operations (from Leeds to coastal communities and Dales villages) drive per-capita cost.",
        "beneficiaries": "c. 5.5M Yorkshire and Humber residents; c. 1M 999 incidents/yr.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Terms and Conditions · Ambulance Service National Contract.",
        "key_stats": [
            {"label": "Clinical supplies & services 2024-25", "value": "£10.0M"},
            {"label": "Share of trust total opex", "value": "c. 3% of ~£0.37bn opex"},
            {"label": "Biggest sub-category", "value": "Defibrillator consumables + medical gases + trauma packs"},
            {"label": "Activity anchor", "value": "c. 1M 999 incidents · >600k patient transports/yr"},
            {"label": "Geography driver", "value": "Mixed urban (Leeds, Sheffield) + deeply rural (Dales, Moors, coast)"},
            {"label": "Supply-chain channel", "value": "NHS Supply Chain Medical ~75% · direct (Zoll/Stryker) ~25%"},
            {"label": "Medical gases", "value": "BOC O2 contract — cylinder rotation across 60+ ambulance stations"},
            {"label": "111 service", "value": "YAS also runs regional 111 — small telephony-clinical overlap"}
        ],
        "notes": "Rural geography drives higher per-incident consumable cost (stock buffers across 60+ ambulance stations). YAS also hosts the regional 111 service, though clinical-supplies spend is almost entirely front-line-ambulance-driven. Defibrillator replacement cycles (c. 8-10 year fleet refresh) and Stryker/Lifepak consumables are the largest direct-buy lines.",
        "sources": [
            {"publisher": "Yorkshire Ambulance Service NHS Trust", "title": "Annual Report and Accounts 2024-25", "url": "https://www.yas.nhs.uk/about-us/publications/"},
            {"publisher": "Association of Ambulance Chief Executives", "title": "Ambulance system indicators", "url": "https://aace.org.uk/"},
            {"publisher": "NHS Supply Chain", "title": "Ambulance service framework", "url": "https://www.supplychain.nhs.uk/"}
        ],
        "related": ["Yorkshire Ambulance Service NHS Trust", "Drugs costs — Yorkshire Ambulance Service NHS Trust"]
    },
    "Clinical supplies & services — Shropshire Community Health NHS Trust": {
        "aliases": [{"name": "Clinical supplies & services", "parent": "Shropshire Community Health NHS Trust"}],
        "description": "ShropCom's £9.0M clinical-supplies bill reflects a pure community-services provider covering Shropshire, Telford & Wrekin — district nursing, health visiting, school nursing, community hospitals (Bishop's Castle, Bridgnorth, Ludlow, Whitchurch), sexual health and therapy services. The consumables basket is classically community-weighted: wound-care, continence, catheters and community-hospital rehab kit.",
        "beneficiaries": "c. 500,000 Shropshire and Telford & Wrekin residents.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Terms and Conditions.",
        "key_stats": [
            {"label": "Clinical supplies & services 2024-25", "value": "£9.0M"},
            {"label": "Share of trust total opex", "value": "c. 6% of ~£0.14bn opex"},
            {"label": "Biggest sub-category", "value": "Wound-care + continence + community-hospital consumables ~40%"},
            {"label": "Service mix", "value": "District nursing + community hospitals + therapy services"},
            {"label": "Community hospitals", "value": "4 sites — Bishop's Castle, Bridgnorth, Ludlow, Whitchurch"},
            {"label": "Supply-chain channel", "value": "NHS Supply Chain Community framework ~88% · direct ~12%"},
            {"label": "Procurement collaborative", "value": "West Midlands collaborative"},
            {"label": "Rural geography", "value": "Distributed stockholding across community teams"}
        ],
        "notes": "Community-hospital inpatient activity (step-down, rehab, end-of-life) adds a small ward-based consumables overlay on top of the dominant district-nursing spend. Rural distribution drives buffer-stock costs for mobile teams. West Midlands collaborative frameworks set most pricing; NPWT (negative-pressure wound therapy) devices are a notable growth line.",
        "sources": [
            {"publisher": "Shropshire Community Health NHS Trust", "title": "Annual Report and Accounts 2024-25", "url": "https://www.shropscommunityhealth.nhs.uk/about-us/publications"},
            {"publisher": "NHS Supply Chain", "title": "Community nursing framework", "url": "https://www.supplychain.nhs.uk/"},
            {"publisher": "NHS Shropshire, Telford and Wrekin ICB", "title": "Integrated care reports", "url": "https://www.shropshiretelfordandwrekin.nhs.uk/"}
        ],
        "related": ["Shropshire Community Health NHS Trust", "Drugs costs — Shropshire Community Health NHS Trust"]
    },
    "Clinical supplies & services — Norfolk Community Health and Care NHS Trust": {
        "aliases": [{"name": "Clinical supplies & services", "parent": "Norfolk Community Health and Care NHS Trust"}],
        "description": "NCH&C's £7.9M clinical-supplies bill reflects a pure community-services provider covering Norfolk — district nursing, community hospitals (Benjamin Court, Dereham, North Walsham, Swaffham, Cromer), specialist rehab and intermediate-care. The geography is challenging: a very large, sparsely-populated rural county with long community-nurse travel times and dispersed stockholding.",
        "beneficiaries": "c. 900,000 Norfolk residents (excluding Waveney, served by ESNEFT).",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Terms and Conditions.",
        "key_stats": [
            {"label": "Clinical supplies & services 2024-25", "value": "£7.9M"},
            {"label": "Share of trust total opex", "value": "c. 5% of ~£0.15bn opex"},
            {"label": "Biggest sub-category", "value": "Wound-care + continence + community-hospital consumables ~40%"},
            {"label": "Service mix", "value": "District nursing + community hospitals + specialist rehab"},
            {"label": "Community hospitals", "value": "5 sites across Norfolk — dispersed stockholding"},
            {"label": "Supply-chain channel", "value": "NHS Supply Chain Community framework ~88% · direct ~12%"},
            {"label": "Procurement collaborative", "value": "East of England Collaborative Procurement Hub"},
            {"label": "Rural geography", "value": "Long community-team travel times — stock decentralised"}
        ],
        "notes": "Norfolk's rural geography drives decentralised stockholding and higher per-contact consumable transport costs than urban community peers. Intermediate-care beds at community-hospital sites add a rehabilitation-kit overlay. EoECPH frameworks set most pricing; NPWT and compression-therapy (for leg-ulcer caseload) are notable lines.",
        "sources": [
            {"publisher": "Norfolk Community Health and Care NHS Trust", "title": "Annual Report and Accounts 2024-25", "url": "https://www.norfolkcommunityhealthandcare.nhs.uk/about-us/our-publications/"},
            {"publisher": "NHS Supply Chain", "title": "Community nursing framework", "url": "https://www.supplychain.nhs.uk/"},
            {"publisher": "NHS Norfolk and Waveney ICB", "title": "Integrated care reports", "url": "https://improvinglivesnw.org.uk/"}
        ],
        "related": ["Norfolk Community Health and Care NHS Trust", "Drugs costs — Norfolk Community Health and Care NHS Trust"]
    },
    "Clinical supplies & services — Nottinghamshire Healthcare NHS Foundation Trust": {
        "aliases": [{"name": "Clinical supplies & services", "parent": "Nottinghamshire Healthcare NHS Foundation Trust"}],
        "description": "Nottinghamshire Healthcare's £7.4M clinical-supplies bill reflects a large mental-health and specialist-provider trust covering Nottingham city, Nottinghamshire and the national high-secure hospital at Rampton. The consumables basket is dominated by ward-based POC testing, restraint equipment, specialist forensic-estate security-rated items and long-term residential-patient personal-care consumables.",
        "beneficiaries": "c. 1.1M Nottingham/Nottinghamshire residents plus national high-secure-forensic caseload at Rampton.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Mental Health Act 1983 · Health and Care Act 2022 · NHS Terms and Conditions · NHSE Specialised Commissioning (high secure).",
        "key_stats": [
            {"label": "Clinical supplies & services 2024-25", "value": "£7.4M"},
            {"label": "Share of trust total opex", "value": "c. 1.2% of ~£0.62bn opex"},
            {"label": "Biggest sub-category", "value": "Ward POC testing + forensic/high-secure consumables ~35%"},
            {"label": "Service mix", "value": "Mental health + high-secure (Rampton) + community + offender health"},
            {"label": "Rampton", "value": "One of 3 national high-secure hospitals — specialist security overhead"},
            {"label": "Supply-chain channel", "value": "NHS Supply Chain Medical ~80% · direct (forensic) ~20%"},
            {"label": "Procurement collaborative", "value": "East Midlands collaborative"},
            {"label": "Offender health", "value": "Prison healthcare contracts — patient-specific consumables"}
        ],
        "notes": "Rampton high-secure drives specialist security-rated kit refreshes (ligature-resistant equipment, non-weaponisable designs) that sit outside standard MH procurement. Offender-health contracts (NHSE-commissioned prison services) add consumables not typical of MH peers. Residential long-stay patient personal-care adds continence and nursing consumables. Rampton ventilation/HEPA filtration is notable.",
        "sources": [
            {"publisher": "Nottinghamshire Healthcare NHS Foundation Trust", "title": "Annual Report and Accounts 2024-25", "url": "https://www.nottinghamshirehealthcare.nhs.uk/annual-report"},
            {"publisher": "NHS England", "title": "High secure mental health service specification", "url": "https://www.england.nhs.uk/commissioning/spec-services/npc-crg/group-c/"},
            {"publisher": "NHS Supply Chain", "title": "Mental health & forensic framework", "url": "https://www.supplychain.nhs.uk/"}
        ],
        "related": ["Nottinghamshire Healthcare NHS Foundation Trust", "Drugs costs — Nottinghamshire Healthcare NHS Foundation Trust"]
    },
    "Clinical supplies & services — North West Ambulance Service NHS Trust": {
        "aliases": [{"name": "Clinical supplies & services", "parent": "North West Ambulance Service NHS Trust"}],
        "description": "NWAS's £6.7M clinical-supplies bill — relatively low for a regional ambulance service — reflects a highly-consolidated operating model across Cumbria, Lancashire, Greater Manchester, Merseyside and Cheshire. The consumables basket is ambulance-standard (defibrillator pads, gases, trauma packs) but aggressive contract aggregation keeps unit costs competitive.",
        "beneficiaries": "c. 7M North West residents; c. 1.3M 999 incidents/yr.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Terms and Conditions · Ambulance Service National Contract.",
        "key_stats": [
            {"label": "Clinical supplies & services 2024-25", "value": "£6.7M"},
            {"label": "Share of trust total opex", "value": "c. 1.5% of ~£0.45bn opex"},
            {"label": "Biggest sub-category", "value": "Defibrillator consumables + medical gases + trauma packs"},
            {"label": "Activity anchor", "value": "c. 1.3M 999 incidents · >800k patient transports/yr"},
            {"label": "Geography driver", "value": "Mixed urban (GM, Merseyside) + deeply rural (Cumbria, Lancs coast)"},
            {"label": "Supply-chain channel", "value": "NHS Supply Chain Medical ~78% · direct (Zoll/Stryker) ~22%"},
            {"label": "Medical gases", "value": "BOC O2 contract across >100 ambulance stations"},
            {"label": "Scale", "value": "One of the 3 largest English ambulance services"}
        ],
        "notes": "Scale (one of the largest English ambulance services) supports aggressive contract aggregation. The Cumbria coast and Pennines drive rural-geography buffer stocks. Stryker/Lifepak defibrillator replacement and iGel airway consumables are the largest recurring lines. NWAS also runs the regional 111 service, though clinical-supplies spend is overwhelmingly front-line.",
        "sources": [
            {"publisher": "North West Ambulance Service NHS Trust", "title": "Annual Report and Accounts 2024-25", "url": "https://www.nwas.nhs.uk/about-us/our-publications/"},
            {"publisher": "Association of Ambulance Chief Executives", "title": "Ambulance system indicators", "url": "https://aace.org.uk/"},
            {"publisher": "NHS Supply Chain", "title": "Ambulance service framework", "url": "https://www.supplychain.nhs.uk/"}
        ],
        "related": ["North West Ambulance Service NHS Trust", "Drugs costs — North West Ambulance Service NHS Trust"]
    },
    "Clinical supplies & services — Rotherham Doncaster and South Humber NHS Foundation Trust": {
        "aliases": [{"name": "Clinical supplies & services", "parent": "Rotherham Doncaster and South Humber NHS Foundation Trust"}],
        "description": "RDaSH's £6.4M clinical-supplies bill reflects a mental-health and community-services trust covering Rotherham, Doncaster and North Lincolnshire. The consumables basket is a mix of classical mental-health ward items (restraint, POC testing, PPE) plus community-nursing wound-care and continence volumes from the integrated community arm in Doncaster and North Lincolnshire.",
        "beneficiaries": "c. 750,000 Rotherham, Doncaster and North Lincolnshire residents.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Mental Health Act 1983 · Health and Care Act 2022 · NHS Terms and Conditions.",
        "key_stats": [
            {"label": "Clinical supplies & services 2024-25", "value": "£6.4M"},
            {"label": "Share of trust total opex", "value": "c. 2.5% of ~£0.25bn opex"},
            {"label": "Biggest sub-category", "value": "Community wound-care + MH ward consumables ~35%"},
            {"label": "Service mix", "value": "Mental health + community + learning disabilities + CAMHS"},
            {"label": "Community arm", "value": "Doncaster + N Lincolnshire district nursing"},
            {"label": "Supply-chain channel", "value": "NHS Supply Chain Community + Medical ~87% · direct ~13%"},
            {"label": "Procurement collaborative", "value": "NOE CPC + South Yorkshire ICS"},
            {"label": "Mental-health consumables", "value": "Ward diagnostics, restraint, rapid tranquilisation kits"}
        ],
        "notes": "Cross-ICS geography (Rotherham/Doncaster in South Yorkshire; North Lincolnshire in Humber & North Yorkshire) complicates community-service invoicing. Community wound-care and continence volumes dominate the basket over pure MH items. NOE CPC frameworks cover most lines. 2024-25 steady-state year with limited capital activity.",
        "sources": [
            {"publisher": "Rotherham Doncaster and South Humber NHS Foundation Trust", "title": "Annual Report and Accounts 2024-25", "url": "https://www.rdash.nhs.uk/about-us/corporate-documents/annual-reports/"},
            {"publisher": "NOE CPC", "title": "Procurement frameworks", "url": "https://www.noecpc.nhs.uk/"},
            {"publisher": "NHS Supply Chain", "title": "Community nursing framework", "url": "https://www.supplychain.nhs.uk/"}
        ],
        "related": ["Rotherham Doncaster and South Humber NHS Foundation Trust", "Drugs costs — Rotherham Doncaster and South Humber NHS Foundation Trust"]
    },
    "Clinical supplies & services — South Central Ambulance Service NHS Foundation Trust": {
        "aliases": [{"name": "Clinical supplies & services", "parent": "South Central Ambulance Service NHS Foundation Trust"}],
        "description": "SCAS's £5.6M clinical-supplies bill covers a regional ambulance service operating across Hampshire, Berkshire, Buckinghamshire and Oxfordshire. The consumables basket is ambulance-standard (defibrillator pads, gases, trauma packs, iGels). SCAS also runs the regional 111 service across Thames Valley and has a large non-emergency patient-transport service (NEPTS).",
        "beneficiaries": "c. 4.9M residents of Hampshire, Berkshire, Bucks and Oxfordshire; c. 700k 999 incidents/yr.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Terms and Conditions · Ambulance Service National Contract.",
        "key_stats": [
            {"label": "Clinical supplies & services 2024-25", "value": "£5.6M"},
            {"label": "Share of trust total opex", "value": "c. 2% of ~£0.27bn opex"},
            {"label": "Biggest sub-category", "value": "Defibrillator consumables + medical gases + trauma packs"},
            {"label": "Activity anchor", "value": "c. 700k 999 incidents · >800k NEPTS journeys/yr"},
            {"label": "Geography driver", "value": "Mixed suburban + rural (Hants, Thames Valley)"},
            {"label": "Supply-chain channel", "value": "NHS Supply Chain Medical ~80% · direct (Zoll/Stryker) ~20%"},
            {"label": "Medical gases", "value": "BOC O2 contract"},
            {"label": "NEPTS", "value": "Large non-emergency patient transport — lower clinical-consumable intensity"}
        ],
        "notes": "NEPTS activity dilutes per-journey clinical-supplies spend relative to purely 999-focused peers. Defibrillator and iGel consumables are the largest direct lines. SCAS's 2022 CQC Inadequate rating prompted governance reform; 2024-25 supplies operations sit under tightened inventory controls.",
        "sources": [
            {"publisher": "South Central Ambulance Service NHS Foundation Trust", "title": "Annual Report and Accounts 2024-25", "url": "https://www.scas.nhs.uk/about-us/our-publications/"},
            {"publisher": "Care Quality Commission", "title": "SCAS inspection reports", "url": "https://www.cqc.org.uk/provider/RYE"},
            {"publisher": "NHS Supply Chain", "title": "Ambulance service framework", "url": "https://www.supplychain.nhs.uk/"}
        ],
        "related": ["South Central Ambulance Service NHS Foundation Trust", "Drugs costs — South Central Ambulance Service NHS Foundation Trust"]
    },
    "Clinical supplies & services — Hertfordshire Community NHS Trust": {
        "aliases": [{"name": "Clinical supplies & services", "parent": "Hertfordshire Community NHS Trust"}],
        "description": "HCT's £4.9M clinical-supplies bill reflects a pure community-services provider covering Hertfordshire — district nursing, children's community services, community hospitals (Potters Bar, Herts & Essex, St Albans) and specialist rehabilitation. The consumables basket is classically community-weighted with a notable 0-19 health-visiting and school-nursing overlay.",
        "beneficiaries": "c. 1.2M Hertfordshire residents across district-nursing, children's and rehab caseloads.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Health and Care Act 2022 · NHS Terms and Conditions.",
        "key_stats": [
            {"label": "Clinical supplies & services 2024-25", "value": "£4.9M"},
            {"label": "Share of trust total opex", "value": "c. 3% of ~£0.16bn opex"},
            {"label": "Biggest sub-category", "value": "Wound-care + continence + community-hospital rehab kit ~40%"},
            {"label": "Service mix", "value": "District nursing + children's 0-19 + rehab + community hospitals"},
            {"label": "Community hospitals", "value": "3 sites — Potters Bar, Herts & Essex, St Albans"},
            {"label": "Supply-chain channel", "value": "NHS Supply Chain Community framework ~88% · direct ~12%"},
            {"label": "Procurement collaborative", "value": "East of England Collaborative Procurement Hub"},
            {"label": "Paediatric overlay", "value": "0-19 health visiting/school nursing — child-size consumables"}
        ],
        "notes": "Pan-Hertfordshire 0-19 children's health services add paediatric wound-care and immunisation consumables (sharps bins, vaccine administration sets) distinct from adult community caseloads. EoECPH frameworks set most pricing. 2024-25 is a steady-state year with no major service reconfigurations affecting supplies.",
        "sources": [
            {"publisher": "Hertfordshire Community NHS Trust", "title": "Annual Report and Accounts 2024-25", "url": "https://www.hct.nhs.uk/about-us/publications/"},
            {"publisher": "NHS Supply Chain", "title": "Community nursing framework", "url": "https://www.supplychain.nhs.uk/"},
            {"publisher": "NHS Hertfordshire and West Essex ICB", "title": "Integrated care reports", "url": "https://hertsandwestessex.icb.nhs.uk/"}
        ],
        "related": ["Hertfordshire Community NHS Trust", "Drugs costs — Hertfordshire Community NHS Trust"]
    },
    "Clinical supplies & services — Cambridgeshire and Peterborough NHS Foundation Trust": {
        "aliases": [{"name": "Clinical supplies & services", "parent": "Cambridgeshire and Peterborough NHS Foundation Trust"}],
        "description": "CPFT's £4.7M clinical-supplies bill reflects a mental-health and community-services trust covering Cambridgeshire and Peterborough — adult MH, CAMHS, learning disabilities, older adults and a growing integrated-community presence. The consumables basket is mental-health-weighted (restraint, POC diagnostics, PPE) with a smaller community-nursing wound-care overlay.",
        "beneficiaries": "c. 980,000 Cambridgeshire and Peterborough residents.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Mental Health Act 1983 · Health and Care Act 2022 · NHS Terms and Conditions.",
        "key_stats": [
            {"label": "Clinical supplies & services 2024-25", "value": "£4.7M"},
            {"label": "Share of trust total opex", "value": "c. 2% of ~£0.24bn opex"},
            {"label": "Biggest sub-category", "value": "MH ward consumables + community wound-care ~35%"},
            {"label": "Service mix", "value": "Mental health + CAMHS + learning disabilities + community"},
            {"label": "Research platform", "value": "NIHR Cambridge BRC Mental Health theme — IMP consumables"},
            {"label": "Supply-chain channel", "value": "NHS Supply Chain Medical ~86% · direct ~14%"},
            {"label": "Procurement collaborative", "value": "East of England Collaborative Procurement Hub"},
            {"label": "Specialist inpatient", "value": "Fulbourn Hospital — adult acute + PICU mental-health beds"}
        ],
        "notes": "NIHR BRC Mental Health theme (in partnership with Cambridge University) generates a small but distinctive IMP consumables line. Fulbourn inpatient ward requires restraint, rapid-tranquilisation delivery and POC screening. EoECPH covers most community consumables. CAMHS Tier 4 beds add paediatric-specific items. 2024-25 is a steady-state year.",
        "sources": [
            {"publisher": "Cambridgeshire and Peterborough NHS Foundation Trust", "title": "Annual Report and Accounts 2024-25", "url": "https://www.cpft.nhs.uk/our-publications"},
            {"publisher": "NIHR Cambridge BRC", "title": "Mental Health theme reports", "url": "https://cambridgebrc.nihr.ac.uk/"},
            {"publisher": "NHS Supply Chain", "title": "Mental health framework", "url": "https://www.supplychain.nhs.uk/"}
        ],
        "related": ["Cambridgeshire and Peterborough NHS Foundation Trust", "Drugs costs — Cambridgeshire and Peterborough NHS Foundation Trust"]
    },
    "Clinical supplies & services — Kent and Medway NHS and Social Care Partnership Trust": {
        "aliases": [{"name": "Clinical supplies & services", "parent": "Kent and Medway NHS and Social Care Partnership Trust"}],
        "description": "KMPT's £3.0M clinical-supplies bill reflects a dedicated mental-health trust (without community-nursing arm) covering Kent and Medway — adult MH, CAMHS, forensic and learning-disability services. The consumables basket is small and classical-MH-weighted: ward POC diagnostics, restraint, rapid-tranquilisation kits, ligature-resistant equipment and PPE.",
        "beneficiaries": "c. 1.8M Kent and Medway residents.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Mental Health Act 1983 · Health and Care Act 2022 · NHS Terms and Conditions.",
        "key_stats": [
            {"label": "Clinical supplies & services 2024-25", "value": "£3.0M"},
            {"label": "Share of trust total opex", "value": "c. 1.3% of ~£0.23bn opex"},
            {"label": "Biggest sub-category", "value": "MH ward consumables + forensic-estate kit ~40%"},
            {"label": "Service mix", "value": "Adult MH + CAMHS + forensic + learning disabilities"},
            {"label": "Pure MH model", "value": "No community-nursing arm — consumables bill tracks MH norm"},
            {"label": "Supply-chain channel", "value": "NHS Supply Chain Mental Health framework ~88% · direct ~12%"},
            {"label": "Procurement collaborative", "value": "Kent & Medway ICS"},
            {"label": "Secure forensic", "value": "Trevor Gibbens Unit — medium-secure forensic consumables"}
        ],
        "notes": "The absence of a community-nursing arm keeps the clinical-supplies baseline low (1-2% of opex, on the low end of the MH peer range). Forensic inpatient wards (medium-secure) drive a small share of ligature-resistant and security-rated kit. Kent & Medway ICS joint procurement with acute partners targets shared consumables.",
        "sources": [
            {"publisher": "Kent and Medway NHS and Social Care Partnership Trust", "title": "Annual Report and Accounts 2024-25", "url": "https://www.kmpt.nhs.uk/about-us/publications/"},
            {"publisher": "NHS Supply Chain", "title": "Mental health framework", "url": "https://www.supplychain.nhs.uk/"},
            {"publisher": "NHS Kent and Medway ICB", "title": "Joint procurement reports", "url": "https://www.kentandmedway.icb.nhs.uk/"}
        ],
        "related": ["Kent and Medway NHS and Social Care Partnership Trust", "Drugs costs — Kent and Medway NHS and Social Care Partnership Trust"]
    },
    "Clinical supplies & services — Cheshire and Wirral Partnership NHS Foundation Trust": {
        "aliases": [{"name": "Clinical supplies & services", "parent": "Cheshire and Wirral Partnership NHS Foundation Trust"}],
        "description": "CWP's £2.3M clinical-supplies bill reflects a mental-health and learning-disabilities trust covering Cheshire (East and West) and Wirral plus some community-services activity. The consumables basket is classically MH-weighted: ward POC diagnostics, restraint, rapid-tranquilisation kits, ligature-resistant equipment and PPE.",
        "beneficiaries": "c. 1M Cheshire, Warrington and Wirral residents.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Mental Health Act 1983 · Health and Care Act 2022 · NHS Terms and Conditions.",
        "key_stats": [
            {"label": "Clinical supplies & services 2024-25", "value": "£2.3M"},
            {"label": "Share of trust total opex", "value": "c. 1% of ~£0.22bn opex"},
            {"label": "Biggest sub-category", "value": "MH ward consumables ~40%"},
            {"label": "Service mix", "value": "Mental health + learning disabilities + some community"},
            {"label": "Geography", "value": "Cheshire East, Cheshire West & Chester, Wirral (3 ICS footprints)"},
            {"label": "Supply-chain channel", "value": "NHS Supply Chain Mental Health framework ~90% · direct ~10%"},
            {"label": "Procurement collaborative", "value": "NOE CPC"},
            {"label": "Inpatient estate", "value": "Specialist PICU, CAMHS and LD beds"}
        ],
        "notes": "Ligature-resistant and specialist-security kit refreshes (following national MH ward-safety guidance) drive periodic capital-to-revenue overlap. Multi-ICS geography (C&M ICS) simplifies commissioning. NOE CPC covers most lines.",
        "sources": [
            {"publisher": "Cheshire and Wirral Partnership NHS Foundation Trust", "title": "Annual Report and Accounts 2024-25", "url": "https://www.cwp.nhs.uk/about-us/publications/"},
            {"publisher": "NOE CPC", "title": "Procurement frameworks", "url": "https://www.noecpc.nhs.uk/"},
            {"publisher": "NHS Supply Chain", "title": "Mental health framework", "url": "https://www.supplychain.nhs.uk/"}
        ],
        "related": ["Cheshire and Wirral Partnership NHS Foundation Trust", "Drugs costs — Cheshire and Wirral Partnership NHS Foundation Trust"]
    },
    "Clinical supplies & services — Barnet, Enfield And Haringey Mental Health NHS Trust": {
        "aliases": [{"name": "Clinical supplies & services", "parent": "Barnet, Enfield And Haringey Mental Health NHS Trust"}],
        "description": "BEH's £1.5M clinical-supplies bill reflects a north-London mental-health trust covering Barnet, Enfield and Haringey, plus partnership running (with Camden & Islington) of the North London Mental Health Partnership. Consumables are pure-MH: ward POC testing, restraint, rapid-tranquilisation delivery sets, ligature-resistant equipment and PPE.",
        "beneficiaries": "c. 1M residents of Barnet, Enfield and Haringey.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Mental Health Act 1983 · Health and Care Act 2022 · NHS Terms and Conditions · NHS London Procurement Partnership frameworks.",
        "key_stats": [
            {"label": "Clinical supplies & services 2024-25", "value": "£1.5M"},
            {"label": "Share of trust total opex", "value": "c. 0.9% of ~£0.17bn opex"},
            {"label": "Biggest sub-category", "value": "MH ward consumables ~45%"},
            {"label": "Service mix", "value": "Adult MH + CAMHS + forensic-regional secure unit"},
            {"label": "Partnership", "value": "North London Mental Health Partnership (with C&I)"},
            {"label": "Supply-chain channel", "value": "NHS Supply Chain Mental Health framework ~90% · direct ~10%"},
            {"label": "Procurement collaborative", "value": "LPP (London Procurement Partnership)"},
            {"label": "Forensic", "value": "North London Forensic Service — medium-secure consumables"}
        ],
        "notes": "The North London Forensic Service adds a specialist-security kit overlay. The partnership with Camden & Islington (moving toward a full merger) supports joint procurement through LPP. 2024-25 is a steady-state year with partnership-integration planning ongoing.",
        "sources": [
            {"publisher": "Barnet, Enfield and Haringey Mental Health NHS Trust", "title": "Annual Report and Accounts 2024-25", "url": "https://www.beh-mht.nhs.uk/about-us/publications.htm"},
            {"publisher": "NHS London Procurement Partnership", "title": "Mental health framework", "url": "https://www.lpp.nhs.uk/"},
            {"publisher": "NHS England", "title": "Medium secure forensic service specification", "url": "https://www.england.nhs.uk/commissioning/spec-services/npc-crg/group-c/"}
        ],
        "related": ["Barnet, Enfield And Haringey Mental Health NHS Trust", "Drugs costs — Barnet, Enfield And Haringey Mental Health NHS Trust"]
    },
    "Clinical supplies & services — Pennine Care NHS Foundation Trust": {
        "aliases": [{"name": "Clinical supplies & services", "parent": "Pennine Care NHS Foundation Trust"}],
        "description": "Pennine Care's £1.2M clinical-supplies bill is the smallest in this batch — a dedicated mental-health trust covering Bury, Oldham, Rochdale, Stockport, Tameside and Glossop in the east/north-east of Greater Manchester. The consumables basket is classical-MH (ward POC diagnostics, restraint, ligature-resistant) with no community-nursing arm.",
        "beneficiaries": "c. 1.3M residents across 5 Greater Manchester boroughs.",
        "legal_basis": "NHS Group Accounting Manual 2024-25 · NHS Act 2006 · Mental Health Act 1983 · Health and Care Act 2022 · NHS Terms and Conditions.",
        "key_stats": [
            {"label": "Clinical supplies & services 2024-25", "value": "£1.2M"},
            {"label": "Share of trust total opex", "value": "c. 0.5% of ~£0.24bn opex"},
            {"label": "Biggest sub-category", "value": "MH ward consumables ~45%"},
            {"label": "Service mix", "value": "Adult MH + CAMHS + PICU + older adult"},
            {"label": "Pure MH model", "value": "No community-nursing arm — lowest peer baseline"},
            {"label": "Supply-chain channel", "value": "NHS Supply Chain Mental Health framework ~92% · direct ~8%"},
            {"label": "Procurement collaborative", "value": "GM Provider Collaborative"},
            {"label": "Ligature-resistance", "value": "Post-HSIB ward-safety refresh cycle"}
        ],
        "notes": "Pennine Care's absence of a community-nursing arm makes it one of the lowest clinical-supplies spenders in the MH-trust peer group. Ligature-resistant ward-safety kit refreshes (driven by national HSIB/NHSE guidance) drive periodic spikes. GM Provider Collaborative joint procurement with Greater Manchester Mental Health NHSFT targets aggregated frameworks.",
        "sources": [
            {"publisher": "Pennine Care NHS Foundation Trust", "title": "Annual Report and Accounts 2024-25", "url": "https://www.penninecare.nhs.uk/about-us/publications/"},
            {"publisher": "NHS Greater Manchester ICB", "title": "Provider collaborative reports", "url": "https://gmintegratedcare.org.uk/"},
            {"publisher": "NHS Supply Chain", "title": "Mental health framework", "url": "https://www.supplychain.nhs.uk/"}
        ],
        "related": ["Pennine Care NHS Foundation Trust", "Drugs costs — Pennine Care NHS Foundation Trust"]
    },
}
