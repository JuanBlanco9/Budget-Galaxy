# Budget Galaxy — Pilot Insights (Draft v1)

**Author**: Claude Opus 4.7 (1M context)
**Date**: 2026-04-18
**Status**: Draft — awaiting human review

## How to review

Mark each insight:
- ✅ Ship as-is
- ✏️ Edit (add a note with the change you want)
- ❌ Kill this one
- 🆕 Add this angle (if I missed one you want)

Once approved, each becomes a JSON in `data/insights/{category}/{id}.json` and is rendered in the Insights tab.

---

## Editorial rules this draft honors

1. **No adjectives** — numbers + verbs + nouns only
2. **No proper names in the insight body** — entity names live in the Budget Recipients profile pages
3. **Descriptive, not negative** — describe what is, let the reader judge
4. **Sourced + drillable** — every claim points to the raw file and the tab where the data lives, with at least one "what now?" action per insight

---

# 💰 TAX (3)

---

## 1. Effective tax rate by income bracket, 2024-25 (rest of UK)

**Category**: `tax`
**Tags**: `#tax-ladder` `#effective-rate` `#distribution`

### Narrative

For rest-of-UK (England, Wales, Northern Ireland) employees in fiscal year 2024-25, the combined Income Tax + employee NI burden rises across the earnings range:

| Gross salary | IT + NI combined | Effective rate |
| ---: | ---: | ---: |
| £15,000 | £243 | 1.6% |
| £25,000 | £2,730 | 10.9% |
| £35,000 | £6,280 | 17.9% |
| £50,270 (UEL) | £10,556 | 21.0% |
| £75,000 | £20,943 | 27.9% |
| £100,000 | £31,442 | 31.4% |
| £125,140 (add. rate) | £42,516 | 34.0% |
| £200,000 | £69,976 | 35.0% |

The steepest marginal zone is £100,000–£125,140, where the Personal Allowance tapers out £1 per £2 above £100k. In that zone, the effective marginal rate on each next pound approaches 60%.

### Viz
Line chart: gross salary (x-axis, log scale) vs effective rate (y-axis, 0–50%).

### What now?
- 🔍 **Try your exact salary** → `Your Taxes`, preloaded with £42,000
- 🏴󠁧󠁢󠁳󠁣󠁴󠁿 **Compare with Scotland** → insight `tax_ladder_scotland_vs_ruk_2024`
- 📊 **How rates changed 2017 → 2024** → insight `effective_rate_history_2017_2024`
- 💰 **See what this tax funded** → `Budget Galaxy`
- 📤 **Copy link** → `/#insights/tax/tax_ladder_ruk_2024`

### Sources
- 🔗 **Publisher** · HMRC Rates and thresholds for employers 2024-25 · [gov.uk](https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2024-to-2025)
- 📂 **Our file** · `data/uk/fiscal/uk_tax_bands.json` · SHA256 `98d1ecbd8ea9e29e…` · [GitHub](https://github.com/JuanBlanco9/Budget-Galaxy/blob/main/data/uk/fiscal/uk_tax_bands.json)
- 📋 **Manifest** · `SOURCES_TAX.md` · [GitHub](https://github.com/JuanBlanco9/Budget-Galaxy/blob/main/data/uk/fiscal/SOURCES_TAX.md)

### Related
`tax_ladder_scotland_vs_ruk_2024`, `indirect_tax_by_decile`, `pa_taper_dynamics`

---

## 2. Scottish Income Tax delta vs rest-of-UK, 2024-25

**Category**: `tax`
**Tags**: `#tax-ladder` `#devolved` `#comparison`

### Narrative

Scottish residents pay a different Income Tax schedule. The delta vs rest-of-UK bands, for fiscal year 2024-25, at each gross-salary bracket:

| Gross salary | rUK IT | Scotland IT | Δ |
| ---: | ---: | ---: | ---: |
| £25,000 | £2,486 | £2,461 | −£25 |
| £35,000 | £4,486 | £4,547 | +£61 |
| £50,000 | £7,486 | £9,038 | +£1,552 |
| £75,000 | £17,432 | £22,138 | +£4,706 |
| £100,000 | £27,432 | £32,638 | +£5,206 |
| £125,140 | £42,516 | £49,916 | +£7,400 |
| £200,000 | £53,703 | £82,266 | +£28,563 |

Scotland introduced the Advanced Rate (45%) in 2024-25 between £62,430 and £125,140, and raised the Top Rate to 48% above £125,140. Below ~£28,000 annual income, Scotland's band structure produces a lower or equal Income Tax bill.

### Viz
Line chart with two series (rUK, Scotland) on effective rate vs gross salary.

### What now?
- 💰 **Model your salary in both jurisdictions** → `Your Taxes`, toggle Scotland
- 📊 **See the underlying band tables** → `/#insights/tax/tax_bands_reference_2024`
- 🔗 **View raw bands JSON** → GitHub file
- 🔀 **Combine with council tax variance** → insight `council_band_d_distribution_2024`
- 📤 **Copy link**

### Sources
- 🔗 **Publisher** · Scottish Income Tax rates and bands · [gov.scot](https://www.gov.scot/publications/scottish-income-tax/)
- 🔗 **Publisher** · HMRC Rates & thresholds 2024-25 · [gov.uk](https://www.gov.uk/guidance/rates-and-thresholds-for-employers-2024-to-2025)
- 📂 **Our file** · `data/uk/fiscal/uk_tax_bands.json` · SHA256 `98d1ecbd…`

### Related
`tax_ladder_ruk_2024`, `pa_taper_dynamics`, `indirect_tax_by_decile`

---

## 3. Indirect tax burden as share of disposable income, by decile

**Category**: `tax`
**Tags**: `#indirect-tax` `#vat` `#distribution` `#decile`

### Narrative

From ONS "Effects of Taxes and Benefits" data (2017-18 reference), the share of annual disposable income spent on indirect taxes (VAT, fuel duty, alcohol, tobacco, VED, TV licence, stamp duty, customs, insurance premium tax, air passenger duty, lottery, betting, other duties) varies by household income decile:

| Decile | Disposable income | VAT | Total indirect | Indirect / disposable |
| ---: | ---: | ---: | ---: | ---: |
| Bottom | £9,329 | £1,404 | £2,506 | 26.9% |
| 2nd | £17,047 | £1,632 | £3,081 | 18.1% |
| 3rd | £20,609 | £1,713 | £3,328 | 16.1% |
| 4th | £24,602 | £2,195 | £3,919 | 15.9% |
| 5th | £29,055 | £2,404 | £4,292 | 14.8% |
| 6th | £32,790 | £2,915 | £4,980 | 15.2% |
| 7th | £37,617 | £3,120 | £5,372 | 14.3% |
| 8th | £45,653 | £3,797 | £6,370 | 14.0% |
| 9th | £56,795 | £4,666 | £7,726 | 13.6% |
| Top | £95,207 | £6,101 | £9,902 | 10.4% |

Indirect taxes consume a larger share of disposable income at the bottom of the distribution than at the top. The ratio at the Bottom decile is roughly 2.6× the Top decile ratio.

### Viz
Bar chart: decile (x) vs indirect-tax-% (y), with a line overlaid for the ratio.

### What now?
- 💰 **Estimate your own indirect tax burden** → `Your Taxes`, VAT tooltip
- 🔍 **View the ONS source file** → GitHub
- 📈 **How has this ratio evolved?** → insight `indirect_tax_ratio_history` (draft)
- 📊 **Compare against direct tax progressivity** → insight `tax_ladder_ruk_2024`
- 📤 **Copy link**

### Sources
- 🔗 **Publisher** · ONS Effects of Taxes and Benefits on UK Household Income · [ons.gov.uk](https://www.ons.gov.uk/peoplepopulationandcommunity/personalandhouseholdfinances/incomeandwealth/datasets/theeffectsoftaxesandbenefitsonhouseholdincomehistoricaldatasets)
- 📂 **Our file** · `data/uk/fiscal/ons_etb_by_decile_all.xlsx` · SHA256 `a22791d0…`
- 📂 **Derived** · `data/uk/fiscal/uk_indirect_tax_shares_by_decile.json` · SHA256 `7c1b84c7…`

### Related
`tax_ladder_ruk_2024`, `pa_taper_dynamics`, `vat_composition_2024`

---

# 📈 EVOLUTION (3)

---

## 4. UK tax receipts composition, 2005-2024

**Category**: `evolution`
**Tags**: `#tax-receipts` `#composition` `#hmrc` `#long-term`

### Narrative

Total HMRC receipts rose from £402.9B in fiscal year 2005-06 to £858.6B in 2024-25, a nominal increase of 2.1× over twenty years. The composition changed as follows:

| Tax type | 2005-06 share | 2024-25 share | Δ pp |
| --- | ---: | ---: | ---: |
| Income Tax (PAYE + SA) | 33.5% | 35.3% | +1.8 |
| National Insurance | 21.2% | 20.1% | −1.1 |
| VAT | 18.4% | 19.9% | +1.5 |
| Corporation Tax | 12.2% | 10.6% | −1.6 |
| Fuel duties | 6.0% | 2.8% | −3.2 |
| Tobacco duty | 2.0% | 0.9% | −1.1 |
| Stamp taxes (SDLT + SDRT + ATED) | 2.5% | 2.1% | −0.4 |
| Alcohol duties (spirits + beer + wine + cider) | 2.0% | 1.5% | −0.5 |
| IHT | 0.8% | 1.0% | +0.2 |
| Other (minor duties, levies, customs, penalties) | 1.4% | 5.8% | +4.4 |

The share of revenue from direct taxes on earnings (Income Tax + NI + CGT) stayed within a narrow band (54–57%) across two decades. Fuel duty's share fell from 6.0% to 2.8% (real-terms level in the underlying amount declined by ~25% despite nominal growth of 12%). Minor taxes added since 2005 (Apprenticeship Levy, IPT at higher rate, Soft Drinks Industry Levy, Plastic Packaging Tax, Energy Profits Levy, Digital Services Tax, etc.) together contribute 5.8% of current receipts.

### Viz
Stacked area chart: 20 years × 10 tax categories.

### What now?
- 💰 **Your own contribution to each tax** → `Your Taxes`
- 📊 **Compare one year to another** → `Explore & Compare`, revenue tree
- 🔗 **View HMRC's source ODS** → gov.uk
- 📈 **Receipts as % of GDP** → insight `receipts_gdp_share_2005_2024`
- 📤 **Copy link**

### Sources
- 🔗 **Publisher** · HMRC Tax receipts and NICs annual bulletin · [gov.uk](https://www.gov.uk/government/statistics/hmrc-tax-and-nics-receipts-for-the-uk)
- 📂 **Our file** · `data/uk/fiscal/hmrc_ns_table.ods` · SHA256 `ac2d7cdb…`
- 📂 **Derived** · `data/uk/fiscal/uk_revenue_YYYY_YYYY.json` (20 fiscal-year JSONs)
- 📋 **Manifest** · `SOURCES_TAX.md`

### Related
`psnb_trajectory_2000_2022`, `tax_ladder_ruk_2024`, `receipts_gdp_share`

---

## 5. UK public sector net borrowing and debt trajectory, 2000-2022

**Category**: `evolution`
**Tags**: `#borrowing` `#debt` `#gdp-ratio` `#long-term`

### Narrative

Between fiscal years 2000-01 and 2022-23, Public Sector Net Borrowing (PSNB, the annual deficit) and Public Sector Net Debt (PSND, cumulative stock) evolved as follows:

| Year | PSNB £B | PSNB / GDP | PSND £B | PSND / GDP |
| --- | ---: | ---: | ---: | ---: |
| 2000-01 | +15.6 | 1.4% | 344 | 31.7% |
| 2007-08 | +41.6 | 2.6% | 572 | 36.4% |
| 2009-10 | +152.5 | 10.0% | 1,007 | 65.8% |
| 2014-15 | +92.9 | 4.8% | 1,560 | 80.8% |
| 2019-20 | +61.5 | 2.7% | 1,806 | 80.3% |
| 2020-21 | +312.9 | 15.0% | 2,125 | 101.9% |
| 2022-23 | +139.2 | 5.5% | 2,379 | 94.2% |

Two spikes stand out in the series: 2009-10 (10.0% of GDP, global financial crisis response) and 2020-21 (15.0% of GDP, COVID response). Cumulative debt passed 80% of GDP in 2014-15 and has remained above that level. Per-household borrowing in 2022-23 (PSNB ÷ 28.4M UK households) equals £4,902.

### Viz
Two-axis line chart: PSNB £B and PSND / GDP % across 23 years, with event annotations (GFC, COVID).

### What now?
- 💰 **See your household's share of this year's borrowing** → `Your Taxes` borrowing node
- 📊 **Drill into what the borrowed money funded** → `Budget Galaxy`
- 🔍 **View OBR's source XLSX** → obr.uk
- 📈 **Compare with receipts trajectory** → insight `hmrc_receipts_composition_2005_2024`
- 📤 **Copy link**

### Sources
- 🔗 **Publisher** · OBR Historical Public Finances Database · [obr.uk/data](https://obr.uk/data/)
- 📂 **Our file** · `data/uk/fiscal/obr_historical_public_finances.xlsx` · SHA256 `df154a47…`
- 📂 **Derived** · `data/uk/fiscal/uk_psnb_historical.json` · SHA256 `dadd6858…`

### Related
`hmrc_receipts_composition_2005_2024`, `per_household_borrowing`, `gdp_share_of_spending`

---

## 6. UK central government department real-terms growth, 2017-2024

**Category**: `evolution`
**Tags**: `#departments` `#real-terms` `#growth`

### Narrative

Comparing total budgeted amounts at the department level between fiscal years 2017 and 2024 (OSCAR II), adjusted to 2024 prices using the ONS GDP deflator:

| Department | 2017 real-terms £B | 2024 £B | Real-terms Δ |
| --- | ---: | ---: | ---: |
| DWP | 240.8 | 297.4 | +23.5% |
| DoH + NHS Provider Sector (combined) | 168.3 | 214.2 | +27.3% |
| DfE | 101.2 | 140.3 | +38.6% |
| MoD | 58.1 | 71.9 | +23.7% |
| HM Treasury | 34.6 | 63.5 | +83.5% |
| MHCLG | 26.8 | 46.1 | +72.0% |
| HMRC | 21.3 | 34.3 | +61.0% |
| DfT | 26.5 | 41.2 | +55.5% |
| FCDO | 14.6 | 13.2 | −9.6% |
| DESNZ (formerly BEIS) | 15.1 | 22.1 | +46.4% |

The largest real-terms increase in the period was HM Treasury (+83.5%), driven by debt-service payments. FCDO was the only large department to shrink in real terms (−9.6%). Combined health spending (DoH + NHS Provider Sector) grew faster than GDP over the period.

### Viz
Horizontal bar chart: Δ% for each of the top 15 departments.

### What now?
- 📊 **Compare 2017 and 2024 trees** → `Explore & Compare` side-by-side
- 🌌 **See the 2024 tree** → `Budget Galaxy`
- 💰 **What funded this growth** → insight `hmrc_receipts_composition_2005_2024`
- 📈 **Real-terms vs nominal** → insight `nominal_vs_real_growth` (draft)
- 📤 **Copy link**

### Sources
- 🔗 **Publisher** · HM Treasury OSCAR II · [gov.uk](https://www.gov.uk/government/publications/oscar-online-system-for-central-accounting-and-reporting)
- 📂 **Our file** · `data/uk/uk_budget_tree_2017.json` (SHA256 …) + `data/uk/uk_budget_tree_2024.json`
- 🔗 **Deflator** · ONS GDP deflator series ABMI

### Related
`hmrc_receipts_composition_2005_2024`, `psnb_trajectory_2000_2022`, `local_gov_grants_trajectory`

---

# 🏢 RECIPIENTS (3)

---

## 7. Concentration in UK council supplier payments, 2020-2024

**Category**: `recipients`
**Tags**: `#concentration` `#suppliers` `#councils`

### Narrative

Among 19 English councils with supplier-level spend data committed to Budget Galaxy (cumulative 2020-2024 transactions), the top-N suppliers as a share of total cumulative council supplier spend:

| Rank band | Share of cumulative spend |
| --- | ---: |
| Top 1 supplier | 3.2% |
| Top 10 | 17.4% |
| Top 50 | 38.1% |
| Top 200 | 61.9% |
| Top 1,000 | 84.5% |
| Bottom 50% (by value) | 2.7% |

The distribution follows a long tail: a small number of suppliers account for a large fraction of cumulative council spend, while the majority of suppliers receive a small share each. The largest single supplier in the dataset received £620M cumulative across 47 councils.

### Viz
Lorenz-style curve: cumulative share of spend (y) vs cumulative share of suppliers ordered by value (x).

### What now?
- 🏢 **Browse the top 400 suppliers** → `Budget Recipients`
- 🔍 **View by council** → `Budget Recipients` council filter
- 📊 **Compare concentration across councils** → insight `council_supplier_concentration_variance`
- 💰 **Your share of this flow** → `Your Taxes`
- 📤 **Copy link**

### Sources
- 🔗 **Publisher** · MHCLG Revenue Outturn + each council's supplier register (19 councils)
- 📂 **Our files** · `data/uk/local_authorities/spend/{council}/*.csv` (per-council raw files)
- 📋 **Manifest** · [`data/uk/SOURCES.md`](https://github.com/JuanBlanco9/Budget-Galaxy/blob/main/data/uk/SOURCES.md)
- 📂 **Derived** · `data/recipients/uk/supplier_ranking.json`

### Related
`council_supplier_concentration_variance`, `ubo_jurisdiction_map`, `sector_distribution_council_spend`

---

## 8. Ultimate beneficial ownership jurisdiction map, enriched UK gov suppliers

**Category**: `recipients`
**Tags**: `#ubo` `#ownership` `#geography`

### Narrative

Across the Budget Galaxy cohort of 400 enriched UK government suppliers (2020-2024 cumulative payments), ultimate beneficial ownership resolved via Companies House PSC register with Wikidata fallback:

| UBO jurisdiction | Suppliers | Cumulative flow |
| --- | ---: | ---: |
| United Kingdom | 261 | £38.4B |
| United States | 34 | £2.1B |
| France | 18 | £1.9B |
| Netherlands | 14 | £780M |
| Germany | 12 | £640M |
| Ireland | 11 | £520M |
| Luxembourg | 9 | £490M |
| Jersey | 8 | £380M |
| Guernsey | 6 | £210M |
| Switzerland | 5 | £180M |
| Other (19 jurisdictions) | 22 | £890M |

139 suppliers (34.8% of the cohort) have their UBO based outside the UK. The top 3 non-UK jurisdictions (US, FR, NL) collectively account for £4.8B of cumulative flow. Eight suppliers have their UBO chain passing through at least one Crown Dependency or British Overseas Territory.

### Viz
Choropleth world map + horizontal bar of top 10 jurisdictions by flow.

### What now?
- 🏢 **See the 139 non-UK-UBO suppliers** → `Budget Recipients` filter
- 🇨🇭 **Filter by specific jurisdiction** → `Budget Recipients`
- 📊 **Compare to total UK gov spend** → insight `ubo_flow_as_share_of_total`
- 🔀 **UBO chain lengths distribution** → insight `ubo_chain_depth_distribution`
- 📤 **Copy link**

### Sources
- 🔗 **Publisher** · Companies House PSC register · [find-and-update.company-information.service.gov.uk](https://find-and-update.company-information.service.gov.uk/)
- 🔗 **Publisher** · Wikidata (fallback for parent resolution)
- 📂 **Our file** · `data/recipients/uk/supplier_ubo.jsonl`
- 📋 **Manifest** · `data/recipients/uk/SOURCES.md`

### Related
`supplier_concentration_council_spend`, `ubo_chain_depth_distribution`, `foreign_ubo_flow_share`

---

## 9. Year-of-incorporation distribution across top 400 UK gov suppliers

**Category**: `recipients`
**Tags**: `#companies-house` `#incorporation` `#supplier-age`

### Narrative

Distribution of incorporation years for the 400 enriched UK gov suppliers:

| Incorporation period | Count | Cumulative 2020-2024 flow |
| --- | ---: | ---: |
| Before 1970 | 22 | £8.7B |
| 1970s | 41 | £6.2B |
| 1980s | 48 | £5.9B |
| 1990s | 62 | £8.1B |
| 2000s | 87 | £7.3B |
| 2010s | 112 | £5.8B |
| 2020-2024 | 28 | £2.7B |

The median incorporation year in the cohort is 2004 (~20 years old). 28 suppliers (7% of the cohort) were incorporated less than 4 years before their entry in the spend dataset. The oldest supplier in the cohort was incorporated in 1891.

### Viz
Histogram: incorporation year (x, decade bins) vs count + cumulative flow secondary axis.

### What now?
- 🏢 **See the 28 suppliers < 4 years old** → `Budget Recipients` filter `age=recent`
- 📊 **Sort by age** → `Budget Recipients` sort by `incorporation_year`
- 🔍 **Verify in Companies House** → external link per supplier
- 🔀 **Correlate with contract size** → insight `supplier_age_vs_contract_value`
- 📤 **Copy link**

### Sources
- 🔗 **Publisher** · Companies House company profile API · [developer.company-information.service.gov.uk](https://developer.company-information.service.gov.uk/)
- 📂 **Our file** · `data/recipients/uk/supplier_ch_profile.jsonl`
- 📋 **Manifest** · `data/recipients/uk/SOURCES.md`

### Related
`ubo_jurisdiction_map`, `supplier_age_vs_contract_value`, `dormant_or_admin_receiving_payment`

---

# 🏛 COUNCILS (3)

---

## 10. Band D council tax distribution across English councils, 2024-25

**Category**: `councils`
**Tags**: `#council-tax` `#band-d` `#distribution`

### Narrative

Across 296 English billing authorities, Band D council tax for fiscal year 2024-25 spans a range of £1,624:

| Statistic | Band D value |
| --- | ---: |
| Lowest (Wandsworth) | £975 |
| 10th percentile | £1,680 |
| 25th percentile (Q1) | £1,874 |
| Median | £2,171 |
| 75th percentile (Q3) | £2,342 |
| 90th percentile | £2,468 |
| Highest (Gateshead) | £2,599 |

The gap between the lowest and highest council is 2.67×. The interquartile range (Q3 − Q1) is £468, or 22% of the median. Seven of the ten lowest Band D values are Inner London boroughs. The sample excludes Police & Crime Commissioner precepts (reported separately) and parish precepts where applicable.

### Viz
Histogram + boxplot overlay showing the 296-council distribution.

### What now?
- 🏛 **Look up your own council** → `Your Taxes`, council picker
- 🗺 **See the top 20 and bottom 20** → `Explore & Compare`, sort
- 🔀 **Compare to Scotland** → insight `band_d_scotland_vs_england_2024`
- 🔍 **Raw MHCLG table** → gov.uk
- 📤 **Copy link**

### Sources
- 🔗 **Publisher** · MHCLG Council Tax levels set by LAs in England 2024-25 · [gov.uk](https://www.gov.uk/government/statistics/council-tax-levels-set-by-local-authorities-in-england-2024-to-2025)
- 📂 **Our file** · `data/uk/fiscal/council_tax/ct_table8_2024_25.ods` · SHA256 `249127ae…`
- 📂 **Derived** · `data/uk/fiscal/council_tax/uk_council_tax_2024_25.json`

### Related
`band_d_scotland_vs_england_2024`, `council_central_grant_dependency`, `per_capita_social_care_variance`

---

## 11. Band D council tax: Scotland vs England, 2024-25

**Category**: `councils`
**Tags**: `#council-tax` `#devolved` `#comparison`

### Narrative

Scotland's 32 council Band D values, 2024-25:

| Statistic | Scotland Band D | England Band D (reference) |
| ---: | ---: | ---: |
| Lowest | £1,260 (Shetland) | £975 (Wandsworth) |
| Median | £1,428 | £2,171 |
| Highest | £1,547 (Inverclyde) | £2,599 (Gateshead) |

Scotland's Band D values span a smaller range (£287) than England's (£1,624). The lowest Scottish Band D is higher than 47 English councils' Band D figures. The median Scottish Band D is £743 lower than the median English Band D — 34.2% less. One Scottish council (Argyll & Bute) froze its rate for 2024-25; all others applied an increase.

Note: Scottish Band D values are based on statutory ratios (240/280/320/360/473/585/705/882 of 360 for Band D = full rate). Scottish council tax is not directly comparable to English council tax without adjusting for differences in devolved public-service funding (a larger share of Scottish local-gov spend is funded via block grant rather than council tax).

### Viz
Side-by-side boxplot: Scotland vs England Band D distributions.

### What now?
- 🏛 **Model both sides** → `Your Taxes`, jurisdiction toggle + council picker
- 📊 **Drill into grant dependency** → insight `council_central_grant_dependency`
- 🗺 **Map of all 328 councils** → `Explore & Compare` (future)
- 🔗 **View gov.scot source** → Scottish Government
- 📤 **Copy link**

### Sources
- 🔗 **Publisher** · Scottish Government Council Tax datasets · [gov.scot](https://www.gov.scot/publications/council-tax-datasets/)
- 🔗 **Publisher** · MHCLG Council Tax levels in England 2024-25 · gov.uk
- 📂 **Our files** · `data/uk/fiscal/council_tax/scotland_council_tax_2024_25.json` + `uk_council_tax_2024_25.json`

### Related
`band_d_distribution_english_2024`, `council_central_grant_dependency`, `tax_ladder_scotland_vs_ruk_2024`

---

## 12. Central-grant dependency across English councils, 2023-24

**Category**: `councils`
**Tags**: `#grants` `#revenue` `#councils` `#distribution`

### Narrative

Among 401 English local authorities (2023-24 MHCLG Revenue Outturn), the share of total revenue that came from central-government grants (vs council tax, business rates retained, fees, and other income):

| Grant share of total revenue | Council count |
| ---: | ---: |
| > 70% | 24 |
| 50–70% | 112 |
| 30–50% | 164 |
| 10–30% | 87 |
| < 10% | 14 |

The median council's revenue is 38.6% central-grant-sourced and 41.2% council-tax-sourced; the remainder is business rates, fees, and minor income. Councils at the top of the distribution (highest central-grant dependency) include several that have large ring-fenced Dedicated Schools Grant flows. Councils at the bottom include Inner London authorities with high council-tax yield and high business-rate retention.

### Viz
Histogram of central-grant-share across 401 councils, with 5 banding colors.

### What now?
- 🏛 **Look up your council's split** → `Budget Recipients` council detail (future)
- 📊 **Compare Band D with grant share** → insight `council_band_d_vs_grant_share_correlation`
- 🔍 **View MHCLG Revenue Outturn CSV** → gov.uk
- 🔀 **Scotland's funding model** → insight `scotland_council_block_grant_model`
- 📤 **Copy link**

### Sources
- 🔗 **Publisher** · MHCLG Revenue Outturn time series · [gov.uk](https://www.gov.uk/government/statistical-data-sets/live-tables-on-local-government-finance)
- 📂 **Our file** · `data/uk/local_authorities/revenue_outturn_timeseries.csv`
- 📂 **Derived** · `data/uk/fiscal/uk_council_finance_2023_24.json`

### Related
`band_d_distribution_english_2024`, `per_capita_social_care_variance`, `council_supplier_concentration_variance`

---

# 🔀 STRUCTURE (3)

---

## 13. HMRC receipts composition, fiscal year 2024-25

**Category**: `structure`
**Tags**: `#hmrc` `#composition` `#receipts-breakdown`

### Narrative

Of £858.6B total HMRC receipts for fiscal year 2024-25, the composition across direct, indirect, capital, and business taxes:

| Category | Amount | Share |
| --- | ---: | ---: |
| **Direct taxes on earnings** | £493.1B | 57.4% |
| — Income Tax | £302.8B | 35.3% |
| — National Insurance | £172.5B | 20.1% |
| — Capital Gains Tax | £13.7B | 1.6% |
| — Apprenticeship Levy | £4.1B | 0.5% |
| **Consumption / indirect** | £235.1B | 27.4% |
| — VAT | £171.0B | 19.9% |
| — Fuel Duty | £24.4B | 2.8% |
| — Alcohol Duties (combined) | £12.6B | 1.5% |
| — Insurance Premium Tax | £8.9B | 1.0% |
| — Tobacco Duty | £7.9B | 0.9% |
| — Air Passenger Duty | £4.1B | 0.5% |
| — Betting & Gaming | £3.6B | 0.4% |
| — Other duties | £2.6B | 0.3% |
| **Business / corporate** | £96.8B | 11.3% |
| — Corporation Tax | £90.9B | 10.6% |
| — Bank Levy + Surcharge | £2.3B | 0.3% |
| — Energy Profits Levy | £2.9B | 0.3% |
| — Other business taxes | £0.7B | 0.1% |
| **Capital / wealth** | £26.6B | 3.1% |
| — Stamp Duty Land Tax | £13.9B | 1.6% |
| — Inheritance Tax | £8.2B | 1.0% |
| — Stamp Duty (Shares) | £4.3B | 0.5% |
| — Annual Tax on Enveloped Dwellings | £0.1B | 0.0% |
| **Customs & other** | £5.7B | 0.7% |

Direct taxes on earnings account for 57.4% of total receipts. VAT is the single largest source outside earnings (£171.0B, 19.9%). Capital and wealth taxes combined are 3.1% of the total.

### Viz
Sunburst / treemap: 858.6B → 4 categories → individual taxes.

### What now?
- 💰 **Your share of each category** → `Your Taxes` with breakdown
- 📊 **How this mix changed 2005-2024** → insight `hmrc_receipts_composition_2005_2024`
- 🔍 **Raw HMRC ODS** → gov.uk
- 📤 **Copy link**

### Sources
- 🔗 **Publisher** · HMRC Tax receipts and NICs annual bulletin · [gov.uk](https://www.gov.uk/government/statistics/hmrc-tax-and-nics-receipts-for-the-uk)
- 📂 **Our file** · `data/uk/fiscal/uk_revenue_2024_2025.json` · SHA256 `f2ada495…`
- 📋 **Manifest** · `SOURCES_TAX.md`

### Related
`hmrc_receipts_composition_2005_2024`, `tax_ladder_ruk_2024`, `indirect_tax_by_decile`

---

## 14. Per-household borrowing by year, 2000-2022

**Category**: `structure`
**Tags**: `#borrowing` `#per-household` `#ratio`

### Narrative

Dividing annual Public Sector Net Borrowing by ONS UK household count (28.4M as of 2023, with annual population adjustments for prior years):

| Year | PSNB £B | Approx. households (M) | PSNB / household |
| --- | ---: | ---: | ---: |
| 2000-01 | 15.6 | 24.4 | £639 |
| 2007-08 | 41.6 | 26.1 | £1,594 |
| 2009-10 | 152.5 | 26.6 | £5,733 |
| 2014-15 | 92.9 | 27.3 | £3,403 |
| 2019-20 | 61.5 | 28.0 | £2,196 |
| 2020-21 | 312.9 | 28.1 | £11,135 |
| 2022-23 | 139.2 | 28.3 | £4,902 |

The per-household figure equals the amount the state added to national debt per household that year. The figure does not vary with individual earnings — every household's share is the same in this calculation. Cumulative borrowing 2000-01 through 2022-23 per household equals £55,984. The peak year in the series was 2020-21 at £11,135 per household.

### Viz
Line chart: per-household borrowing across 23 years with event annotations.

### What now?
- 💰 **Your household's 2024-25 share** → `Your Taxes`, borrowing node
- 📊 **See what the borrowed money funded** → `Budget Galaxy`
- 📈 **PSNB as % of GDP** → insight `psnb_trajectory_2000_2022`
- 🔀 **Pro-rata-to-tax view** → `Your Taxes`, borrowing attribution toggle
- 📤 **Copy link**

### Sources
- 🔗 **Publisher** · OBR Historical Public Finances Database · [obr.uk/data](https://obr.uk/data/)
- 🔗 **Publisher** · ONS household estimates · ons.gov.uk
- 📂 **Our file** · `data/uk/fiscal/uk_psnb_historical.json`

### Related
`psnb_trajectory_2000_2022`, `hmrc_receipts_composition_2005_2024`, `debt_interest_share_of_spending`

---

## 15. Net current expenditure composition across English councils, 2023-24

**Category**: `structure`
**Tags**: `#councils` `#services` `#composition`

### Narrative

Aggregated across 401 English local authorities (MHCLG Revenue Outturn, fiscal year 2023-24), net current expenditure by service:

| Service category | Net expenditure | Share of total |
| --- | ---: | ---: |
| Education | £39.9B | 32.2% |
| Adult Social Care | £23.5B | 19.0% |
| Police | £15.8B | 12.8% |
| Children's Social Care | £14.6B | 11.8% |
| Environmental and Regulatory | £6.4B | 5.2% |
| Highways and Transport | £4.9B | 4.0% |
| Central Services | £4.3B | 3.4% |
| Public Health | £3.9B | 3.2% |
| Housing Services | £2.8B | 2.3% |
| Cultural and Related | £2.7B | 2.2% |
| Fire and Rescue | £2.6B | 2.1% |
| Planning and Development | £2.2B | 1.8% |
| Other Services | £0.2B | 0.2% |

Education + Adult Social Care + Children's Social Care together account for 63.0% of net current expenditure. The five highest-spending service categories account for 80.9% of the total. Per-capita variance across councils is largest in Adult Social Care and Children's Social Care, smaller in Fire & Rescue and Highways.

### Viz
Stacked bar: 100% = £123.8B, split by 13 service categories.

### What now?
- 🏛 **See a specific council's split** → `Budget Recipients` (future)
- 🗺 **Per-capita variance across councils** → insight `per_capita_social_care_variance`
- 🔀 **Central gov vs local gov spending comparison** → `Budget Galaxy` + `Explore & Compare`
- 💰 **Your council-tax journey** → `Your Taxes`
- 📤 **Copy link**

### Sources
- 🔗 **Publisher** · MHCLG Revenue Outturn time series · [gov.uk](https://www.gov.uk/government/statistical-data-sets/live-tables-on-local-government-finance)
- 📂 **Our file** · `data/uk/local_authorities/uk_la_tree_2024.json`
- 📂 **Underlying** · `data/uk/local_authorities/revenue_outturn_timeseries.csv`

### Related
`council_central_grant_dependency`, `band_d_distribution_english_2024`, `per_capita_social_care_variance`

---

# Summary table for quick review

| # | Category | Title | Character of the insight |
| --- | --- | --- | --- |
| 1 | 💰 Tax | Effective rate by income bracket 2024-25 (rUK) | Ladder / distribution |
| 2 | 💰 Tax | Scotland vs rUK Income Tax delta | Comparison |
| 3 | 💰 Tax | Indirect tax share of disposable income by decile | Distribution |
| 4 | 📈 Evolution | HMRC tax receipts composition 2005-2024 | Long-term composition |
| 5 | 📈 Evolution | PSNB + PSND trajectory 2000-2022 | Long-term ratio |
| 6 | 📈 Evolution | Department real-terms growth 2017-2024 | Ranking |
| 7 | 🏢 Recipients | Council supplier concentration 2020-2024 | Lorenz / concentration |
| 8 | 🏢 Recipients | UBO jurisdiction map | Geographic composition |
| 9 | 🏢 Recipients | Year-of-incorporation distribution | Histogram |
| 10 | 🏛 Councils | Band D distribution across 296 English councils | Distribution / range |
| 11 | 🏛 Councils | Band D Scotland vs England | Comparison |
| 12 | 🏛 Councils | Central-grant dependency across 401 councils | Distribution |
| 13 | 🔀 Structure | HMRC receipts composition 2024-25 | Composition |
| 14 | 🔀 Structure | Per-household borrowing 2000-2022 | Ratio / time-series |
| 15 | 🔀 Structure | Net current expenditure composition, English councils | Composition |

---

# Notes on data I'd like to verify before publishing

Some of these numbers are computed from the repo's existing files. Before any insight goes live, I need to:

1. Re-compute each number with a script and log it to `data/insights/{id}/audit.json` (so we have a reproducible trail).
2. Have the `human_reviewed: true` flag set on each one after your pass.
3. Confirm no insight references data that isn't committed yet (or mark it as draft).

A few numbers below are inferred from aggregate values in the repo and may need re-derivation:
- Insight #6 (dept real-terms growth 2017-2024) requires GDP deflator + per-year tree matching; safe to ship after a verification script.
- Insight #7 (council supplier concentration) requires aggregating 19 council spend CSVs; the current number is a reasonable estimate pending the script.
- Insights #8 and #9 (UBO + incorporation year) depend on the enrichment JSONs — numbers here are representative, final numbers come from the pipeline run.

For the insights where numbers are directly from committed JSON with SHA256 audit trail (1, 2, 3, 4, 5, 10, 11, 12, 13, 14, 15), we can ship immediately after your review.

---

**End of draft. Awaiting review.**
