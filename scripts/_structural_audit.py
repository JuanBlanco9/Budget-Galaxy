#!/usr/bin/env python3
"""Structural archetype classifier + first-principles audit of all Tier A entries."""
import json
import re
from pathlib import Path
from collections import defaultdict

ROOT = Path(__file__).resolve().parent.parent
FILE = ROOT / "data/uk/node_enrichment_extended.json"
d = json.loads(FILE.read_text(encoding="utf-8"))

DEPARTMENTS = {
    "DEPARTMENT FOR WORK AND PENSIONS","DEPARTMENT OF HEALTH","DEPARTMENT FOR EDUCATION",
    "HOME OFFICE","MINISTRY OF HOUSING, COMMUNITIES AND LOCAL GOVERNMENT","MINISTRY OF JUSTICE",
    "HM TREASURY","DEPARTMENT FOR TRANSPORT","DEPARTMENT FOR ENERGY SECURITY AND NET ZERO",
    "DEPARTMENT FOR CULTURE, MEDIA AND SPORT","DEPARTMENT FOR SCIENCE, INNOVATION AND TECHNOLOGY",
    "DEPARTMENT FOR ENVIRONMENT, FOOD AND RURAL AFFAIRS","MINISTRY OF DEFENCE",
    "HM REVENUE AND CUSTOMS","DEPARTMENT FOR BUSINESS AND TRADE",
    "FOREIGN, COMMONWEALTH AND DEVELOPMENT OFFICE","CABINET OFFICE",
    "NHS Provider Sector","Local Government (England)","SCOTTISH GOVERNMENT",
    "NORTHERN IRELAND EXECUTIVE","WELSH ASSEMBLY GOVERNMENT"
}

def archetype(key, entry):
    name = key
    desc = (entry.get("description") or "").lower()
    benef = (entry.get("beneficiaries") or "").lower()
    legal = (entry.get("legal_basis") or "").lower()
    blob = f"{name.lower()} {desc} {benef} {legal}"

    if name in DEPARTMENTS:
        return "DEPT"
    if name.isupper() and len(name) > 20:
        # Non-ministerial dept / parliamentary body / court — subset of DEPT
        NON_MIN_MARKERS = ["non-ministerial","court","parliamentary","house of commons","house of lords",
                          "electoral commission","charity commission","food standards","office for",
                          "national archives","procurator","commissioner","local government boundary",
                          "supreme court","actuary","statistics","export credits","land registry",
                          "ordnance survey","savings and investments","met office","companies house",
                          "ofsted","ofqual","ofgem","ofwat","ofcom","debt management","ipsa","parole board"]
        if any(m in blob for m in NON_MIN_MARKERS):
            return "NON_MIN_DEPT"
        return "DEPT"
    if re.match(r"^\d+\.\d+", name):
        return "COFOG"
    TAX_KEYWORDS = ["isa","tax relief","tax credit","tax-free","expenditure credit","rdec","avec","capital allowance","sdlt"]
    if any(kw in name.lower() for kw in TAX_KEYWORDS) or "tax relief" in desc:
        return "TAX"
    BENEFIT_KEYWORDS = ["universal credit","state pension"," pip ","personal independence","esa","jsa","housing benefit",
                       "carer","attendance allowance","dla","disability living","child disability","pension credit",
                       "fire pension","teachers pension","transitional protection","bereavement","maternity",
                       "paternity","child benefit","winter fuel","cold weather","funeral","healthy start","sure start",
                       "ema","child payment","independent living","pupil premium","dedicated schools","iidb"]
    if any(kw in name.lower() for kw in BENEFIT_KEYWORDS):
        return "BENEFIT"
    CULTURAL = ["museum","gallery","heritage","orchestra","ballet","theatre","film institute","english heritage",
                "botanic","war graves","lottery","sport england","uk sport","tate","academy limited","bbc"]
    if any(kw in name.lower() for kw in CULTURAL):
        return "CULTURAL"
    REGULATOR = ["regulator","authority","inspector","commissioner","commission","agency","ombudsman",
                 "office for","ofsted","ofcom","ofgem","ofwat","cma","fca","services agency","executive"]
    if any(kw in name.lower() for kw in REGULATOR) and "NHS" not in name:
        return "REGULATOR"
    if any(x in blob for x in ["scottish government","welsh government","northern ireland executive",
                               "barnett","scottish child payment","adult disability","nhs scotland","nhs wales"]):
        return "DEVOLVED"
    if any(kw in name.lower() for kw in ["defence","military","navy","army","raf","astute","trident","dreadnought","ajax","f-35"]):
        return "MILITARY"
    if any(kw in name.lower() for kw in ["hs2","crossrail","network rail","highways england","east west rail","heathrow"]):
        return "INFRA"
    return "PROGRAMME"


ARCHETYPE_DEMANDS = {
    "DEPT": ["ministers","perm_sec","mog_history","alb_inventory","policy_priorities","barnett_interaction","recent_reshuffle"],
    "NON_MIN_DEPT": ["leadership","founding_reform_history","statutory_powers","policy_priorities","recent_policy_change"],
    "COFOG": ["cofog_definition","sub_components","cross_dept_scope","revision_history","international_comparability"],
    "TAX": ["fiscal_cost_trajectory","take_up_rate","hmrc_stats_ref","tsc_or_obr_eval","predecessor_scheme","market_providers","interaction_other"],
    "BENEFIT": ["caseload_trajectory","rate_uprating","eligibility_specifics","fraud_error_rate","transition_roadmap","devolved_equivalent","recent_policy_change"],
    "CULTURAL": ["governance_leadership","founding_story","collection_scope","access_ticketing","funding_mix","recent_controversy","international_peers"],
    "REGULATOR": ["leadership","funding_mix","statutory_powers","enforcement_cadence","cross_regulator_boundaries","founding_reform_history","nao_pac_review"],
    "DEVOLVED": ["barnett_calc","policy_divergence","cross_uk_compare","delivery_body","recent_reform"],
    "MILITARY": ["prime_contractor","in_service_date","cost_growth","nao_pac_review","nato_context","replacement_legacy"],
    "INFRA": ["programme_phase","cost_baseline","delivery_body","nao_pac_review","economic_case","political_history"],
    "PROGRAMME": ["delivery_body","policy_owner_dept","beneficiary_count","funding_trajectory","evaluation_evidence","predecessor_successor"],
}


def make_tests():
    def any_of(*kws):
        return lambda b: any(kw in b for kw in kws)
    return {
        "ministers": any_of("secretary of state","minister","home secretary","chancellor","foreign secretary","defence secretary"),
        "perm_sec": any_of("permanent secretary","perm sec"),
        "mog_history": any_of("machinery of gov","reshuffle","split from","merged","renamed from","formerly","created in 20","successor to"),
        "alb_inventory": any_of("arms-length","arm length","ndpb","agencies","oversees","sponsors"),
        "policy_priorities": any_of("priority","strategy","white paper","review","reform"),
        "barnett_interaction": any_of("barnett","devolved","scotland","wales","northern ireland"),
        "recent_reshuffle": any_of("2024","2025","reshuffle","reset"),
        "cofog_definition": any_of("cofog","classification of functions","un system"),
        "sub_components": any_of("includes","comprises","covers","sub-line","component","of which"),
        "cross_dept_scope": any_of("across","multi-dept","cross-government","whole-of-government"),
        "revision_history": any_of("revised","restated","reclassif"),
        "international_comparability": any_of("oecd","un sna","international"),
        "fiscal_cost_trajectory": any_of("cost 2024","forecast","trajectory","obr","projection","up from","fell from","grew from"),
        "take_up_rate": any_of("take-up","take up","uptake","eligible","coverage","penetration"),
        "hmrc_stats_ref": any_of("hmrc","tax statistics","annual tax"),
        "tsc_or_obr_eval": any_of("tsc","treasury committee","obr","nao","pac"),
        "predecessor_scheme": any_of("predecessor","successor","replaced","replacing","help-to-buy","prior to","formerly"),
        "market_providers": any_of("providers","managers","partners","issuer","operator","authorised"),
        "interaction_other": any_of("interact","alongside","overlap","combined","workplace"),
        "caseload_trajectory": any_of("caseload","claimants","recipients","trajectory","grew","fell","rising","falling"),
        "rate_uprating": any_of("uplift","uprating","triple lock","cpi","indexed","annual rate"),
        "eligibility_specifics": any_of("eligible","criteria","means-test","threshold","earnings","qualifying","aged "),
        "fraud_error_rate": any_of("fraud","error","overpayment","f&e rate"),
        "transition_roadmap": any_of("move to uc","migration","legacy","transitional","roadmap"),
        "devolved_equivalent": any_of("scottish","welsh","ni equivalent","equivalent in","adp"),
        "recent_policy_change": any_of("2024","2025","review","reformed","autumn budget","spring budget"),
        "governance_leadership": any_of("chair","trustee","director","board","governance","ceo","chief exec"),
        "founding_story": any_of("founded","established","created","launched","origin","act 19","act 20","charter"),
        "collection_scope": any_of("collection","objects","works","holdings","catalogue","permanent"),
        "access_ticketing": any_of("free admission","free entry","ticket","visitors","admission","membership"),
        "funding_mix": any_of("grant-in-aid","self-generated","philanthropy","sponsorship","trading","commercial"),
        "recent_controversy": any_of("scandal","controversy","contested","criticism","resigned","inquiry"),
        "international_peers": any_of("louvre","metropolitan","smithsonian","pompidou","peer","compared"),
        "leadership": any_of("chair","ceo","chief exec","director-general"),
        "statutory_powers": any_of("enforcement","powers","licens","regulat","inspect"),
        "enforcement_cadence": any_of("inspections","notices","prosecut","fine","penalty","cadence"),
        "cross_regulator_boundaries": any_of("boundary","alongside","remit","overlap"),
        "founding_reform_history": any_of("founded","formed","act 19","act 20","reformed","split from"),
        "nao_pac_review": any_of("nao","public accounts","pac","value for money","vfm"),
        "barnett_calc": any_of("barnett"),
        "policy_divergence": any_of("diverge","unlike england","scottish-only","welsh-only","unique to"),
        "cross_uk_compare": any_of("england equivalent","uk-wide","compared to"),
        "delivery_body": any_of("delivered by","administered","delivery","agency","operator"),
        "recent_reform": any_of("2024","2025","reform","review"),
        "prime_contractor": any_of("bae","rolls-royce","lockheed","raytheon","contractor","prime","leonardo"),
        "in_service_date": any_of("service date","expected","operational from","commission","in service"),
        "cost_growth": any_of("overrun","cost growth","baseline","original estimate"),
        "nato_context": any_of("nato"),
        "replacement_legacy": any_of("replace","successor","legacy","retired","out of service"),
        "programme_phase": any_of("phase","tranche","stage","wave"),
        "cost_baseline": any_of("baseline","overspent","original","budgeted","outturn"),
        "economic_case": any_of("bcr","benefit-cost","economic case"),
        "political_history": any_of("announced","manifesto","cancelled","reinstated","paused"),
        "policy_owner_dept": any_of("department","dwp","dfe","dhsc","defra","mod","dft"),
        "beneficiary_count": any_of("beneficiaries","claimants","users","recipients","visitors","million","thousand"),
        "funding_trajectory": any_of("up from","down from","fell from","grew from","trajectory","2021-22","2022-23","2023-24"),
        "evaluation_evidence": any_of("evaluation","impact","outcome","what works","evidence"),
        "predecessor_successor": any_of("predecessor","successor","replaced","formerly","prior"),
        "funding_mix_regulator": any_of("levy","levies","exchequer","industry-funded"),
    }

TESTS = make_tests()

def analyse(key, entry):
    atype = archetype(key, entry)
    demands = ARCHETYPE_DEMANDS.get(atype, [])
    parts = [
        entry.get("description") or "",
        entry.get("notes") or "",
        entry.get("legal_basis") or "",
        entry.get("beneficiaries") or "",
    ]
    for s in entry.get("key_stats") or []:
        if isinstance(s, dict):
            parts.append((s.get("label") or "") + " " + (s.get("value") or ""))
    blob = " ".join(parts).lower()
    gaps = []
    for dim in demands:
        test = TESTS.get(dim)
        if test and not test(blob):
            gaps.append(dim)
    return {"archetype": atype, "gaps": gaps, "gap_count": len(gaps), "demand_count": len(demands)}


results = {}
by_archetype = defaultdict(list)
for key, entry in d["entries"].items():
    a = analyse(key, entry)
    results[key] = a
    by_archetype[a["archetype"]].append((key, a["gap_count"], a["gaps"]))

print("=" * 80)
print(f"STRUCTURAL AUDIT - {len(d['entries'])} Tier A entries x archetype demand")
print("=" * 80)
for arch in sorted(by_archetype.keys()):
    entries = by_archetype[arch]
    entries.sort(key=lambda x: -x[1])
    demand_n = len(ARCHETYPE_DEMANDS.get(arch, []))
    avg_gap = sum(x[1] for x in entries) / max(len(entries),1)
    weak = [e for e in entries if e[1] >= max(2, demand_n * 0.4)]
    print(f"\n[{arch}] count={len(entries)} demands={demand_n} avg_gaps={avg_gap:.1f} weak_count={len(weak)}")
    for e in entries[:8]:
        print(f"  {e[1]}/{demand_n}  {e[0][:55]:55s}  missing: {','.join(e[2][:4])}")

(ROOT / "data/uk/_structural_audit.json").write_text(
    json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8"
)
print(f"\nFull audit: data/uk/_structural_audit.json")
