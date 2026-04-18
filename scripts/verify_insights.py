#!/usr/bin/env python3
"""
verify_insights.py — Recompute every number in the 15 pilot insights
directly from the committed data files.

Goal: produce `data/insights/PILOT_15_VERIFIED.md` with numbers that
match what the calculator / JSONs actually return — so we catch the
kind of drift that snuck into PILOT_15_DRAFT.md.

Run: python scripts/verify_insights.py
Output: data/insights/PILOT_15_VERIFIED.md  (+ audit JSON alongside)
"""
from __future__ import annotations

import hashlib
import json
import os
import statistics
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FISCAL = ROOT / 'data' / 'uk' / 'fiscal'
OUT = ROOT / 'data' / 'insights' / 'PILOT_15_VERIFIED.md'
AUDIT = ROOT / 'data' / 'insights' / '_verification_audit.json'


# ─────────────────────────────────────────────────────────────
# Helpers
# ─────────────────────────────────────────────────────────────

def _sha16(p: Path) -> str:
    """SHA256 first 16 hex chars, for human-readable audit."""
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for c in iter(lambda: f.read(1 << 20), b''):
            h.update(c)
    return h.hexdigest()[:16]


def _gbp(v: float, dp: int = 0) -> str:
    """Format a GBP value with commas."""
    if v is None:
        return '—'
    if dp == 0:
        return f'£{v:,.0f}'
    return f'£{v:,.{dp}f}'


def load_json(path: Path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


# ─────────────────────────────────────────────────────────────
# Python reimplementation of uk_calc.js (strict mirror)
# ─────────────────────────────────────────────────────────────

_bands = load_json(FISCAL / 'uk_tax_bands.json')


def effective_pa(gross: float, base_pa: float, taper_start: float) -> float:
    if not taper_start or gross <= taper_start:
        return base_pa
    reduction = (gross - taper_start) // 2
    return max(0, base_pa - reduction)


def calc_income_tax_ruk(gross: float, year: str = '2024-25') -> float:
    b = _bands['rUK'][year]
    pa = effective_pa(gross, b['personal_allowance'], b['pa_taper_start'])
    taxable = max(0, gross - pa)
    basic_cap = b['basic_rate_limit']
    higher_cap = b['higher_rate_limit']
    basic = min(taxable, basic_cap) * b['basic_rate']
    higher = max(0, min(taxable, higher_cap) - basic_cap) * b['higher_rate']
    addl = max(0, taxable - higher_cap) * b['additional_rate']
    return basic + higher + addl


def calc_income_tax_scotland(gross: float, year: str = '2024-25') -> float:
    b = _bands['scotland'][year]
    pa = effective_pa(gross, b['personal_allowance'], 100_000)
    taxable = max(0, gross - pa)
    lower = 0
    total = 0.0
    for band in b['bands']:
        upper = band['upper_taxable'] if band['upper_taxable'] is not None else float('inf')
        slice_top = min(taxable, upper)
        slice_amt = max(0, slice_top - lower)
        total += slice_amt * band['rate']
        lower = upper
        if slice_top >= taxable:
            break
    return total


def calc_ni(gross: float, year: str = '2024-25') -> float:
    b = _bands['rUK'][year]
    pt = b['ni_primary_threshold']
    uel = b['ni_upper_earnings_limit']
    main = max(0, min(gross, uel) - pt) * b['ni_employee_main_rate']
    upper = max(0, gross - uel) * b['ni_employee_above_uel_rate']
    return main + upper


def calc_total_ruk(gross: float, year: str = '2024-25') -> dict:
    it = calc_income_tax_ruk(gross, year)
    ni = calc_ni(gross, year)
    return {'it': it, 'ni': ni, 'total': it + ni, 'rate': (it + ni) / gross if gross else 0}


def calc_total_scotland(gross: float, year: str = '2024-25') -> dict:
    it = calc_income_tax_scotland(gross, year)
    ni = calc_ni(gross, year)  # NI is UK-wide, not devolved
    return {'it': it, 'ni': ni, 'total': it + ni, 'rate': (it + ni) / gross if gross else 0}


# ─────────────────────────────────────────────────────────────
# Verifiers: one function per insight, returns {verified, payload}
# ─────────────────────────────────────────────────────────────

def v1_tax_ladder_ruk():
    rows = []
    for s in [15_000, 25_000, 35_000, 50_270, 75_000, 100_000, 125_140, 200_000]:
        r = calc_total_ruk(s, '2024-25')
        rows.append({
            'salary': s,
            'it': round(r['it'], 2),
            'ni': round(r['ni'], 2),
            'total': round(r['total'], 2),
            'rate_pct': round(r['rate'] * 100, 1),
        })
    return {'insight': '#1 Tax ladder rUK 2024-25', 'rows': rows}


def v2_scotland_vs_ruk():
    rows = []
    for s in [25_000, 35_000, 50_000, 75_000, 100_000, 125_140, 200_000]:
        rk = calc_total_ruk(s, '2024-25')
        sc = calc_total_scotland(s, '2024-25')
        rows.append({
            'salary': s,
            'ruk_it': round(rk['it'], 2),
            'scot_it': round(sc['it'], 2),
            'delta_it': round(sc['it'] - rk['it'], 2),
        })
    return {'insight': '#2 Scotland vs rUK IT delta 2024-25', 'rows': rows}


def v3_indirect_by_decile():
    d = load_json(FISCAL / 'uk_indirect_tax_shares_by_decile.json')
    rows = []
    # We define indirect taxes strictly: VAT + fuel + tobacco + alcohol (beer+wines+cider)
    # + VED + TV licence + SDLT + customs + betting + IPT + APD + lottery + other.
    # Commercial/industrial rates and employer NI are intermediate taxes (excluded here).
    keys = [
        'vat', 'tobacco_duty', 'beer_cider_duty', 'wines_spirits_duty', 'fuel_duty',
        'ved', 'tv_license', 'sdlt', 'customs', 'betting',
        'insurance_premium_tax', 'air_passenger_duty', 'national_lottery', 'other',
    ]
    for dec in d['deciles']:
        disp = dec['disposable_income_gbp']
        eq_disp = dec['equivalised_disposable_income_gbp']
        vat = dec['indirect_taxes_gbp']['vat']
        total_ind = sum(dec['indirect_taxes_gbp'][k] or 0 for k in keys)
        rows.append({
            'decile': dec['decile'],
            'label': dec['label'],
            'disposable': disp,
            'equivalised_disposable': eq_disp,
            'vat': vat,
            'total_indirect': round(total_ind, 0),
            'indirect_pct_of_disposable': round(total_ind / disp * 100, 1) if disp else None,
        })
    return {
        'insight': '#3 Indirect tax by decile',
        'rows': rows,
        'definition': 'Indirect taxes = VAT + fuel + tobacco + beer/cider + wines/spirits + VED + TV licence + SDLT + customs + betting + IPT + APD + national lottery + other. Excludes commercial/industrial rates and employer NI (intermediate taxes).',
    }


def v4_receipts_composition_evolution():
    # Compute shares for 2005-06 and 2024-25 for the headline tax types
    def shares(path):
        t = load_json(path)
        total = t['value_gbp_m']
        # Walk tree and extract key tax node totals
        flat = {}

        def walk(node):
            flat[node.get('id', '')] = node.get('value_gbp_m', 0)
            for c in node.get('children', []) or []:
                walk(c)

        walk(t)
        return flat, total

    old, old_total = shares(FISCAL / 'uk_revenue_2005_2006.json')
    new, new_total = shares(FISCAL / 'uk_revenue_2024_2025.json')
    picks = [
        ('uk_rev_income_tax', 'Income Tax'),
        ('uk_rev_nic', 'National Insurance'),
        ('uk_rev_vat', 'VAT'),
        ('uk_rev_corp_tax', 'Corporation Tax'),
        ('uk_rev_fuel_duty', 'Fuel duty'),
        ('uk_rev_tobacco', 'Tobacco duty'),
        ('uk_rev_sdlt', 'Stamp Duty Land Tax'),
        ('uk_rev_sds', 'Stamp Duty (Shares)'),
        ('uk_rev_iht', 'Inheritance Tax'),
        ('uk_rev_apd', 'Air Passenger Duty'),
        ('uk_rev_ipt', 'Insurance Premium Tax'),
    ]
    rows = []
    for key, label in picks:
        old_v = old.get(key, 0) or 0
        new_v = new.get(key, 0) or 0
        rows.append({
            'tax': label,
            'old_gbp_m': old_v,
            'new_gbp_m': new_v,
            'old_share_pct': round(old_v / old_total * 100, 1),
            'new_share_pct': round(new_v / new_total * 100, 1),
            'delta_pp': round((new_v / new_total - old_v / old_total) * 100, 1),
        })
    return {
        'insight': '#4 HMRC receipts composition 2005-06 vs 2024-25',
        'total_old_gbp_b': round(old_total / 1000, 1),
        'total_new_gbp_b': round(new_total / 1000, 1),
        'growth_multiple': round(new_total / old_total, 2),
        'rows': rows,
    }


def v5_psnb_trajectory():
    d = load_json(FISCAL / 'uk_psnb_historical.json')
    picks = {s['fiscal_year_label']: s for s in d['series']}
    out = []
    for y in ['2000-01', '2007-08', '2009-10', '2014-15', '2019-20', '2020-21', '2022-23']:
        r = picks.get(y)
        if r:
            out.append({
                'year': y,
                'psnb_gbp_m': r['psnb_gbp_m'],
                'psnb_gbp_b': round(r['psnb_gbp_m'] / 1000, 1),
                'psnb_pct_gdp': r['psnb_pct_of_gdp'],
                'psnd_gbp_m': r['psnd_gbp_m'],
                'psnd_gbp_b': round(r['psnd_gbp_m'] / 1000, 1),
                'psnd_pct_gdp': r['psnd_pct_of_gdp'],
            })
    return {'insight': '#5 PSNB + PSND trajectory 2000-01 to 2022-23', 'rows': out}


def v6_dept_real_terms():
    """
    Department real-terms growth 2017 → 2024.
    Reconciliations:
      (A) Health: combine 2024's 'DEPARTMENT OF HEALTH' + 'NHS Provider Sector'
          into a single Health-comparable vs 2017's 'DEPARTMENT OF HEALTH'.
      (B) HM Treasury: flag non-comparable (2017 net-negative from receipts
          inflow; 2024 net-positive from debt interest outflow).
      (C) Skip any department with |value| < 5B in 2024 (noise floor).
    """
    t17 = load_json(ROOT / 'data' / 'uk' / 'uk_budget_tree_2017.json')
    t24 = load_json(ROOT / 'data' / 'uk' / 'uk_budget_tree_2024.json')
    idx17 = {c['name'].upper(): c['value'] for c in t17.get('children', []) if c.get('value')}
    idx24 = {c['name'].upper(): c['value'] for c in t24.get('children', []) if c.get('value')}
    DEFLATOR_17_TO_24 = 1.222

    # Reconciliation A: combine 2024 DoH + NHS Provider Sector
    doh24 = idx24.get('DEPARTMENT OF HEALTH', 0)
    nhs24 = idx24.get('NHS PROVIDER SECTOR', 0)
    doh17 = idx17.get('DEPARTMENT OF HEALTH', 0)

    rows = []
    # Add the reconciled Health row first
    if doh17 > 0 and (doh24 + nhs24) > 0:
        v17_real = doh17 * DEFLATOR_17_TO_24
        v24_combined = doh24 + nhs24
        rows.append({
            'name': 'Health (DoH + NHS Provider Sector, combined)',
            'v2017_real_2024_gbp_b': round(v17_real / 1e9, 1),
            'v2024_gbp_b': round(v24_combined / 1e9, 1),
            'real_delta_pct': round((v24_combined - v17_real) / v17_real * 100, 1),
            'note': '2017 reported DoH as single bucket; 2024 splits out NHS Provider Sector.',
        })

    # Now walk every other top-level dept
    excluded = {
        'DEPARTMENT OF HEALTH', 'NHS PROVIDER SECTOR',  # handled above
        'HM TREASURY',  # sign convention flip — flagged separately
    }
    for name24, v24 in sorted(idx24.items(), key=lambda kv: -abs(kv[1])):
        if name24 in excluded or v24 < 5_000_000_000:
            continue
        v17 = idx17.get(name24)
        if not v17 or v17 < 1_000_000_000:
            continue
        v17_real = v17 * DEFLATOR_17_TO_24
        delta_pct = (v24 - v17_real) / v17_real * 100
        rows.append({
            'name': name24.title(),
            'v2017_real_2024_gbp_b': round(v17_real / 1e9, 1),
            'v2024_gbp_b': round(v24 / 1e9, 1),
            'real_delta_pct': round(delta_pct, 1),
        })

    # HMT non-comparable note row
    hmt17 = idx17.get('HM TREASURY')
    hmt24 = idx24.get('HM TREASURY')
    hmt_flag = None
    if hmt17 is not None and hmt24 is not None:
        hmt_flag = {
            'v2017_gbp_b': round(hmt17 / 1e9, 1),
            'v2024_gbp_b': round(hmt24 / 1e9, 1),
            'note': 'Sign convention differs across editions (2017 net-of-receipts vs 2024 gross-of-debt-interest). Not included in growth ranking.',
        }

    return {
        'insight': '#6 Department real-terms growth 2017 → 2024',
        'deflator_assumption': DEFLATOR_17_TO_24,
        'deflator_source': 'ONS MM23 GDP deflator series (approx)',
        'rows': rows[:12],
        'hm_treasury_non_comparable': hmt_flag,
    }


def v7_supplier_concentration():
    r = load_json(ROOT / 'data' / 'recipients' / 'uk' / 'supplier_ranking.json')
    return {
        'insight': '#7 UK central-gov supplier concentration (L5 top recipients, 2024)',
        'source_scope': r['source'],
        'unique_suppliers': r['unique_suppliers'],
        'total_gbp_b': round(r['total_gbp'] / 1e9, 1),
        'top100_gbp_b': round(r['top100_gbp'] / 1e9, 1),
        'top100_pct': r['top100_pct'],
        'top500_gbp_b': round(r['top500_gbp'] / 1e9, 1),
        'top500_pct': r['top500_pct'],
    }


def v8_ubo_jurisdictions():
    # Parse the supplier_ubo.jsonl — count resolutions by terminal location
    jsonl = ROOT / 'data' / 'recipients' / 'uk' / 'supplier_ubo.jsonl'
    if not jsonl.exists():
        return {'insight': '#8 UBO map', 'status': 'file not present'}
    counts = {}
    enriched = 0
    multi_chain = 0
    gov_terminals = 0
    with open(jsonl, 'r', encoding='utf-8') as f:
        for line in f:
            try:
                rec = json.loads(line)
            except json.JSONDecodeError:
                continue
            enriched += 1
            chains = rec.get('ubo_chains') or []
            if len(chains) > 1:
                multi_chain += 1
            for chain in chains:
                if not chain:
                    continue
                term = chain[-1]
                res = term.get('resolution')
                if res == 'government':
                    gov_terminals += 1
                    continue
                # Country inference (rough — ubo_chains records country rarely)
                key = res or 'unresolved'
                counts[key] = counts.get(key, 0) + 1
    return {
        'insight': '#8 UBO resolution summary (pipeline output)',
        'enriched_suppliers': enriched,
        'with_multiple_chains': multi_chain,
        'government_terminals': gov_terminals,
        'terminal_resolution_types': counts,
        'note': 'UBO country breakdown needs second pass: cross-ref `resolution` values with country codes. Present stats verify the pipeline ran and ~how many resolved.',
    }


def v9_incorporation_years():
    """
    Supplier profiles store incorporation date at identity.incorporated
    (ISO string like '1920-05-07'). Also: identity.age_years as precomputed years.
    Also rolls up cumulative spend (spend_profile.total_gbp_2024) per bucket.
    """
    sup_dir = ROOT / 'data' / 'suppliers'
    if not sup_dir.exists():
        return {'insight': '#9 Incorporation year', 'status': 'folder missing'}
    years = []
    year_to_spend = []
    total_with_year = 0
    total_profiles = 0
    oldest_name, oldest_year = None, 9999
    newest_name, newest_year = None, 0
    for p in sup_dir.glob('*.json'):
        total_profiles += 1
        try:
            d = load_json(p)
            ident = d.get('identity') or {}
            incorp = ident.get('incorporated')
            if not isinstance(incorp, str) or len(incorp) < 4:
                continue
            try:
                y = int(incorp[:4])
            except ValueError:
                continue
            years.append(y)
            spend = (d.get('spend_profile') or {}).get('total_gbp_2024') or 0
            year_to_spend.append((y, spend))
            total_with_year += 1
            name = d.get('display_name') or ident.get('official_name') or p.stem
            if y < oldest_year:
                oldest_year, oldest_name = y, name
            if y > newest_year:
                newest_year, newest_name = y, name
        except Exception:
            continue
    if not years:
        return {'insight': '#9 Incorporation year', 'status': 'no incorporation fields found'}
    years.sort()
    bounds = [
        ('< 1970', lambda y: y < 1970),
        ('1970-79', lambda y: 1970 <= y < 1980),
        ('1980-89', lambda y: 1980 <= y < 1990),
        ('1990-99', lambda y: 1990 <= y < 2000),
        ('2000-09', lambda y: 2000 <= y < 2010),
        ('2010-19', lambda y: 2010 <= y < 2020),
        ('2020-24', lambda y: 2020 <= y < 2025),
    ]
    buckets = {}
    for label, pred in bounds:
        in_bucket = [(y, s) for (y, s) in year_to_spend if pred(y)]
        buckets[label] = {
            'count': len(in_bucket),
            'spend_gbp_b': round(sum(s for _, s in in_bucket) / 1e9, 2),
        }
    # How many incorporated less than 4 years before entering the spend dataset?
    # 2024 data → threshold year 2021. Count those.
    recent_entrants = sum(1 for y in years if y >= 2021)
    return {
        'insight': '#9 Supplier incorporation years',
        'total_profiles': total_profiles,
        'profile_count_with_year': total_with_year,
        'oldest_year': years[0],
        'oldest_name': oldest_name,
        'median_year': int(statistics.median(years)),
        'newest_year': years[-1],
        'newest_name': newest_name,
        'recent_entrants_lt_4yr': recent_entrants,
        'buckets': buckets,
    }


def v10_band_d_english():
    d = load_json(FISCAL / 'council_tax' / 'uk_council_tax_2024_25.json')
    values = [(c['name'], c['band_D']) for c in d['councils'] if c.get('band_D')]
    vals_sorted = sorted(values, key=lambda x: x[1])
    bvals = [v for _, v in vals_sorted]
    lowest = vals_sorted[0]
    highest = vals_sorted[-1]
    return {
        'insight': '#10 Band D distribution, English councils 2024-25',
        'council_count': len(values),
        'lowest': {'name': lowest[0], 'value': round(lowest[1], 2)},
        'p10': round(statistics.quantiles(bvals, n=10)[0], 2),
        'p25': round(statistics.quantiles(bvals, n=4)[0], 2),
        'median': round(statistics.median(bvals), 2),
        'p75': round(statistics.quantiles(bvals, n=4)[2], 2),
        'p90': round(statistics.quantiles(bvals, n=10)[8], 2),
        'highest': {'name': highest[0], 'value': round(highest[1], 2)},
        'range_gbp': round(highest[1] - lowest[1], 2),
        'multiple': round(highest[1] / lowest[1], 2),
    }


def v11_band_d_scotland_vs_england():
    eng = load_json(FISCAL / 'council_tax' / 'uk_council_tax_2024_25.json')
    scot = load_json(FISCAL / 'council_tax' / 'scotland_council_tax_2024_25.json')
    eng_vals = sorted([(c['name'], c['band_D']) for c in eng['councils'] if c.get('band_D')], key=lambda x: x[1])
    scot_vals = sorted([(c['name'], c['band_D']) for c in scot['councils'] if c.get('band_D')], key=lambda x: x[1])
    eng_bvals = [v for _, v in eng_vals]
    scot_bvals = [v for _, v in scot_vals]
    # How many English councils are LOWER than Scotland's lowest?
    scot_lowest = scot_vals[0][1]
    eng_below = sum(1 for v in eng_bvals if v < scot_lowest)
    return {
        'insight': '#11 Band D Scotland vs England 2024-25',
        'scotland': {
            'count': len(scot_vals),
            'lowest': {'name': scot_vals[0][0], 'value': round(scot_vals[0][1], 2)},
            'median': round(statistics.median(scot_bvals), 2),
            'highest': {'name': scot_vals[-1][0], 'value': round(scot_vals[-1][1], 2)},
            'range': round(scot_vals[-1][1] - scot_vals[0][1], 2),
        },
        'england': {
            'count': len(eng_vals),
            'lowest': {'name': eng_vals[0][0], 'value': round(eng_vals[0][1], 2)},
            'median': round(statistics.median(eng_bvals), 2),
            'highest': {'name': eng_vals[-1][0], 'value': round(eng_vals[-1][1], 2)},
            'range': round(eng_vals[-1][1] - eng_vals[0][1], 2),
        },
        'english_councils_below_scotland_lowest': eng_below,
        'median_delta_gbp': round(statistics.median(eng_bvals) - statistics.median(scot_bvals), 2),
    }


def v12_grant_dependency():
    cf = load_json(FISCAL / 'uk_council_finance_2023_24.json')
    # For each council: compute grant share = grants_in / (grants_in + net_current_expenditure_other)
    # Simplified: grants_in / net_current_expenditure (where net_cur_exp > 0)
    shares = []
    for c in cf['councils']:
        g = c.get('central_grants_in_gbp') or 0
        nce = c.get('net_current_expenditure_gbp') or 0
        if nce > 100_000_000:  # skip tiny entries to avoid noise
            share = g / nce * 100 if nce else 0
            shares.append(share)
    if not shares:
        return {'insight': '#12 Grant dependency', 'status': 'no values'}
    buckets = {
        '> 70%': sum(1 for s in shares if s > 70),
        '50-70%': sum(1 for s in shares if 50 <= s <= 70),
        '30-50%': sum(1 for s in shares if 30 <= s < 50),
        '10-30%': sum(1 for s in shares if 10 <= s < 30),
        '< 10%': sum(1 for s in shares if s < 10),
    }
    return {
        'insight': '#12 Central-grant share of net current expenditure, English councils 2023-24',
        'councils_in_scope': len(shares),
        'median_pct': round(statistics.median(shares), 1),
        'p25_pct': round(statistics.quantiles(shares, n=4)[0], 1),
        'p75_pct': round(statistics.quantiles(shares, n=4)[2], 1),
        'buckets': buckets,
    }


def v13_receipts_composition_2024_25():
    t = load_json(FISCAL / 'uk_revenue_2024_2025.json')
    total = t['value_gbp_m']
    cats = {}
    for top in t.get('children', []):
        cats[top['id']] = {
            'name': top['name'],
            'gbp_m': top['value_gbp_m'],
            'pct': round(top['value_gbp_m'] / total * 100, 1),
            'children': [
                {'name': c['name'], 'gbp_m': c.get('value_gbp_m', 0),
                 'pct': round(c.get('value_gbp_m', 0) / total * 100, 1)}
                for c in top.get('children', [])
            ],
        }
    return {
        'insight': '#13 HMRC receipts composition, 2024-25',
        'total_gbp_b': round(total / 1000, 1),
        'categories': cats,
    }


def v14_per_household_borrowing():
    d = load_json(FISCAL / 'uk_psnb_historical.json')
    # ONS household estimates (approx, rounded to 100k): 2000 → 24.4M climbing to 28.3M by 2022
    household_m_by_year = {
        '2000-01': 24.4, '2007-08': 26.1, '2009-10': 26.6, '2014-15': 27.3,
        '2019-20': 28.0, '2020-21': 28.1, '2022-23': 28.3,
    }
    out = []
    for s in d['series']:
        y = s['fiscal_year_label']
        if y not in household_m_by_year:
            continue
        psnb_m = s['psnb_gbp_m']
        h = household_m_by_year[y] * 1e6
        per_house = psnb_m * 1e6 / h
        out.append({
            'year': y,
            'psnb_gbp_b': round(psnb_m / 1000, 1),
            'households_m': household_m_by_year[y],
            'per_household_gbp': round(per_house, 0),
        })
    # Cumulative
    cum_psnb = sum(s['psnb_gbp_m'] for s in d['series']
                   if s['fiscal_year_start'] >= 2000 and s['fiscal_year_start'] <= 2022)
    avg_households = sum(household_m_by_year.values()) / len(household_m_by_year) * 1e6
    cum_per_house = cum_psnb * 1e6 / avg_households
    return {
        'insight': '#14 Per-household borrowing 2000-01 → 2022-23',
        'rows': out,
        'cumulative_psnb_23yr_gbp_b': round(cum_psnb / 1000, 1),
        'cumulative_per_household_gbp': round(cum_per_house, 0),
    }


def v15_la_tree_composition():
    t = load_json(ROOT / 'data' / 'uk' / 'local_authorities' / 'uk_la_tree_2024.json')
    total = t['value']
    rows = [{'name': c['name'], 'value_gbp_b': round(c['value'] / 1e9, 1),
             'pct': round(c['value'] / total * 100, 1)}
            for c in t['children']]
    rows.sort(key=lambda x: -x['value_gbp_b'])
    return {
        'insight': '#15 LA net current expenditure composition 2024',
        'total_gbp_b': round(total / 1e9, 1),
        'rows': rows,
    }


# ─────────────────────────────────────────────────────────────
# Main
# ─────────────────────────────────────────────────────────────

VERIFIERS = [v1_tax_ladder_ruk, v2_scotland_vs_ruk, v3_indirect_by_decile,
             v4_receipts_composition_evolution, v5_psnb_trajectory, v6_dept_real_terms,
             v7_supplier_concentration, v8_ubo_jurisdictions, v9_incorporation_years,
             v10_band_d_english, v11_band_d_scotland_vs_england, v12_grant_dependency,
             v13_receipts_composition_2024_25, v14_per_household_borrowing, v15_la_tree_composition]


def main():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    audit = {'generated_at': date.today().isoformat(), 'insights': []}
    for v in VERIFIERS:
        try:
            payload = v()
        except Exception as e:
            payload = {'insight': v.__name__, 'error': str(e)}
        audit['insights'].append(payload)
        # Brief progress log
        title = payload.get('insight', v.__name__)
        status = 'OK' if 'error' not in payload else f'ERROR: {payload["error"]}'
        print(f'  {title:60s} {status}')

    with open(AUDIT, 'w', encoding='utf-8') as f:
        json.dump(audit, f, indent=2, ensure_ascii=False)
    print(f'\nAudit JSON written to {AUDIT.relative_to(ROOT)}')
    print(f'Next: read that file, patch PILOT_15_VERIFIED.md with real numbers.')


if __name__ == '__main__':
    main()
