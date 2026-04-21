# Tier A Entry Archetype Briefs

Canonical structural demand per entry type. **Every new Tier A entry must satisfy
its archetype's dimension list before being considered complete.** Apply this
template at draft time, not at retrofit time.

## 1. DEPT — Top-level departments + named UPPER-case organisations

Required dimensions:
1. **Ministers** — current Secretary of State + top 2-3 junior ministers (by portfolio)
2. **Permanent Secretary** — name + tenure dates
3. **MoG history** — machinery-of-gov lineage: when the dept was created, what it
   split from / merged with, recent name changes
4. **ALB inventory** — executive agencies + NDPBs + public corporations sponsored
   (list top 5-8 by scale)
5. **Policy priorities** — 3-5 current strategy / white paper / review lines
6. **Barnett / devolution interaction** — which functions are reserved vs devolved,
   Barnett consequentials generated
7. **Recent reshuffle / reform** — 2024-25 machinery changes, manifesto commitments

## 2. COFOG — UN SNA / CP-COFOG classification aggregates

Required dimensions:
1. **COFOG definition** — what the UN/OECD code technically means (cite manual)
2. **Sub-components** — what's inside this code (of-which breakdowns)
3. **Cross-dept scope** — which departments contribute to this code
4. **Revision history** — recent reclassifications (e.g. DEL/AME migrations, ESA10
   changes)
5. **International comparability** — how this UK aggregate maps to OECD peers

## 3. TAX — Tax reliefs, credits, exemptions

Required dimensions:
1. **Fiscal cost trajectory** — HMRC Tax Reliefs statistics 3-year trend + OBR
   forecast
2. **Take-up rate** — % of eligible population claiming, known distribution gaps
3. **HMRC statistics reference** — exact publication to cite
4. **TSC / OBR / NAO evaluation** — any formal review, critique, recommendation
5. **Predecessor scheme** — what this replaced, what was reformed
6. **Market providers** — who delivers (ISA managers, accredited bodies, etc.)
7. **Interaction with other reliefs** — pension/ISA/EIS overlap, combined caps

## 4. BENEFIT — Social-security payments + income-transfer programmes

Required dimensions:
1. **Caseload trajectory** — current count + 3-5 year trend
2. **Rate + uprating** — current payment rate + uprating mechanism (CPI, triple
   lock, etc.)
3. **Eligibility specifics** — means-test, earnings thresholds, age bands
4. **Fraud + error rate** — DWP / HMRC F&E bulletin figure
5. **Transition roadmap** — Move-to-UC timeline, legacy benefit phase-out
6. **Devolved equivalent** — Scottish/Welsh/NI version if any (ADP, SCP, etc.)
7. **Recent policy change** — 2024-25 reform, Autumn Statement / Budget change

## 5. CULTURAL — Museums, galleries, heritage bodies, lottery distributors

Required dimensions:
1. **Governance leadership** — Chair + Director/CEO by name + tenure
2. **Founding story** — year + statute + why it was created
3. **Collection / programme scope** — holdings size, sites, catalogue
4. **Access / ticketing** — free vs paid, membership tiers, visitor demographics
5. **Funding mix** — grant-in-aid % + self-generated % + philanthropy %
6. **Recent controversy** — current scandal / restitution debate / governance dispute
7. **International peer frame** — comparable institution + stand-out UK differentiator

## 6. REGULATOR — Arm's-length regulators, inspectorates, commissions

Required dimensions:
1. **Leadership** — Chair + CEO + Chief Inspector (where applicable)
2. **Funding mix** — exchequer vs levy/fee share
3. **Statutory powers** — main Acts + enforcement tools
4. **Enforcement cadence** — inspections/yr, notices issued, prosecutions, fines
5. **Cross-regulator boundaries** — adjacent regulators, joint/shared remit
6. **Founding / reform history** — originating Act + major subsequent reforms
7. **NAO / PAC review** — most recent formal scrutiny + findings

## 7. DEVOLVED — Scottish / Welsh / NI specific programme lines

Required dimensions:
1. **Barnett calculation** — how this line is generated from the Barnett formula
2. **Policy divergence** — how this differs from the England equivalent
3. **Cross-UK compare** — direct equivalent + spend-per-head comparison
4. **Delivery body** — which agency/board/trust delivers
5. **Recent reform** — 2024-25 policy change

## 8. MILITARY — Defence capability programmes, equipment, personnel

Required dimensions:
1. **Prime contractor** — BAE / Rolls-Royce / Lockheed / etc.
2. **In-service date** — ISD (planned or achieved)
3. **Cost growth** — baseline vs current NAO / PAC cost estimate
4. **NAO / PAC review** — Major Projects Report entry
5. **NATO context** — NATO 2% GDP target, framework nation roles
6. **Replacement / legacy** — what it replaces, what will replace it

## 9. INFRA — Major capital infrastructure programmes

Required dimensions:
1. **Programme phase** — current stage (scheme development, construction, operation)
2. **Cost baseline** — vs IPA / NAO / PAC current figure
3. **Delivery body** — Network Rail / HS2 Ltd / National Highways / etc.
4. **NAO / PAC review** — most recent scrutiny outcome
5. **Economic case** — BCR at approval and revised
6. **Political history** — manifesto commitment / cancellation / reinstatement

## 10. PROGRAMME — Catch-all funded policy lines not in above archetypes

Required dimensions:
1. **Delivery body** — which agency administers
2. **Policy owner department** — primary sponsor dept
3. **Beneficiary count** — users, recipients, businesses reached
4. **Funding trajectory** — 3-year trend + outlook
5. **Evaluation evidence** — What Works Centre / NAO / IfG eval
6. **Predecessor / successor** — scheme lineage

---

## Quality floors (ALL archetypes)

- `description`: 3-5 sentences, 250-600 chars
- `beneficiaries`: 1-2 sentences with concrete count where possible
- `legal_basis`: statute name + year + (if applicable) amending Acts
- `key_stats`: 8-12 entries in `{label, value}` shape with populated value field
- `notes`: 3-5 sentences covering recent controversy / change / evaluation,
  300-800 chars
- `sources`: 4-6 sources, every entry with a working URL
- `related`: 3-6 cross-links to other Tier A entries

## Process rule (binding on all future waves)

> Before drafting a new Tier A entry, classify its archetype, pull the brief
> above, and include every dimension in the draft. No "standard schema" dispatch
> — each agent receives an archetype-tailored brief.

**This document is the contract.** Audit script at `scripts/_structural_audit.py`
verifies compliance against the heuristic tests encoded per dimension.
