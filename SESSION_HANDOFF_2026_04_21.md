# Budget Galaxy — Session Handoff 2026-04-21

**Written by**: Claude Opus 4.7 (1M context window) — last session before rate-limit pause.
**Purpose**: Give the next Claude window everything it needs to continue exactly where we stopped, without repeating mistakes.

---

## 🔖 CURRENT STATE — READ THIS FIRST

- **Branch**: `claude/mystifying-ardinghelli-f4e66f` (worktree at `D:/germany-ngo-map/.claude/worktrees/mystifying-ardinghelli-f4e66f/`)
- **Last commit**: `80f37ed` — feat(uk): depth-4 Social security & levy partial — 52 new (2,569 → 2,621)
- **Tier A entries live in file**: **2,621**
- **Coverage**:
  - £-weighted resolution: **99.117%** (what "resolves to something")
  - **Tailor-made per-entity**: **82.12%** (£3.657T of £4.453T) ← this is the honest number
  - **Shared-parent** (18%): 6,948 tree nodes absorb content from a parent COFOG/dept aggregate instead of having their own specific entry
- **54 commits ahead of origin/main**. Nothing has been pushed/merged to main yet.

### Production status
- **Live URL**: https://budgetgalaxy.com (Vultr Atlanta · 96.30.199.112 · uvicorn on port 8088 behind nginx)
- **Last deployed enrichment data**: commit `7126451` era (~2,157 entries) — the depth-4 work (from 6784c93 onward) is committed but NOT yet deployed to production
- **SSH key**: `~/.ssh/id_agro_intel`
- **Deploy command**:
  ```bash
  scp -i ~/.ssh/id_agro_intel data/uk/node_enrichment_extended.json root@96.30.199.112:/opt/germany-ngo-map/data/uk/
  scp -i ~/.ssh/id_agro_intel frontend/index.html root@96.30.199.112:/opt/germany-ngo-map/frontend/
  ssh -i ~/.ssh/id_agro_intel root@96.30.199.112 "pkill -f 'uvicorn api.main:app'; sleep 3"
  ssh -i ~/.ssh/id_agro_intel root@96.30.199.112 "cd /opt/germany-ngo-map && ADMIN_STATS_TOKEN=c26a2a1d066f2e9b5aaa1839edd4b24be050b79db0d9a4126dbd1da6cffc795c nohup /opt/germany-ngo-map/venv/bin/uvicorn api.main:app --host 0.0.0.0 --port 8088 --workers 2 > /var/log/budgetgalaxy.log 2>&1 & disown; exit 0"
  ```

---

## 🎯 THE USER MANDATE — DO NOT DEVIATE

User has been consistent and explicit:
1. **Tailor-made per-entity for EVERY entry** — every council, every NHS trust, every sub-line, every sub-sub-line
2. **No cut corners** — don't propose reduced scope options unless asked
3. **Pace batches carefully to manage tokens** — 4-5 agents per batch max; always verify before next batch
4. **Audit-driven** — the archetype contract in `docs/archetype_briefs.md` is the canonical spec

User knows the gap. User has confirmed willingness to spend 5-7+ more sessions to close 100% tailor-made.

---

## 📋 PENDING WORK (PRIORITIZED)

### Rate limit schedule (observed)
Anthropic user-tier limits reset at **2pm and 7pm Buenos Aires time** (UTC-3). Two rate-limit hits observed in previous sessions — pace dispatches so agents complete within the 5-6 hour window between resets.

### Phase 1: Complete depth-4 NHS sub-sub-lines (~2,250 entries remaining)

Already done (committed):
- ✅ D4_01 Salaries & wages (206)
- ✅ D4_02 Agency & temporary staff (206)
- ✅ D4_03 Employer pensions (154 — D4_03b overlapped, producing 154 unique instead of 206)
- ✅ Depreciation depth-4 (206) — was covered incidentally in Batches A-E

**In progress / partial**:
- 🟡 D4_04 Social security & levy: 52 merged · **154 still pending re-dispatch**

**Not started** (in order by £):
- D4_05 Drugs costs (206 · £10.77B)
- D4_06 Clinical supplies & services (206 · £9.44B)
- D4_07 Premises (other) (206 · £4.63B)
- D4_08 Impairments net of reversals (165 · £2.22B)
- D4_09 General supplies & services (205 · £1.99B)
- D4_10 Establishment costs (206 · £1.29B)
- D4_11 PFI / LIFT charges (96 · £1.14B)
- D4_12 Transport (business + patient) (205 · £0.97B)
- D4_13 Business rates (204 · £0.48B)
- D4_14 Amortisation (196 · £0.40B)
- D4_15 Lease expenditure (159 · £0.19B)
- D4_16 Termination & post-employment (60 · £0.03B)
- D4_17 Inventories written down (96 · £0.02B)
- D4_18+ Other residuals (~30 · negligible £)

**Estimate**: ~12-13 categories × ~4 agents each = ~50 agents. Each agent takes ~5-8 min. Need ~12-15 batches paced across 3-4 sessions.

### Phase 2: Close 18% shared-parent gap (6,948 entries)

This is the gap the user saw visually when Social Fund - Cold Weather Payment / Community Care Grant / Net Lending all rendered IDENTICAL content (they all inherit the parent COFOG 10.7 entry).

Priority ranking by count + £:

| Rank | Parent being absorbed | # orphans | £ absorbed | Difficulty |
|---|---|---:|---:|---|
| 1 | NHS Mental Health Trusts | 3,190 | £122B | High — many multi-level sub-lines |
| 2 | Shire Districts | 948 | £3.5B | Medium — council service sub-lines |
| 3 | Unitary Authorities | 652 | £30.0B | Medium |
| 4 | Metropolitan Districts | 369 | £24.4B | Medium |
| 5 | London Boroughs | 322 | £19.9B | Medium |
| 6 | Other Authorities | 237 | £17.5B | Medium (PCCs/FRAs sub-items) |
| 7 | Shire Counties | 216 | £31.4B | Medium |
| 8 | NHS Acute Trusts | 132 | £6.0B | Low |
| 9 | NHS Provider Sector | 111 | £1.7B | Low |
| 10 | Dept residuals (MHCLG/DEFRA/DCMS/DBT) | ~300 | £15B | Medium |

Detection command:
```bash
py -c "
import sys, json
sys.stdout.reconfigure(encoding='utf-8')
from collections import defaultdict
tree = json.load(open('data/uk/uk_budget_tree_2024.json', encoding='utf-8'))
ext = json.load(open('data/uk/node_enrichment_extended.json', encoding='utf-8'))
keys = set(ext['entries'].keys())
aliases_scoped = defaultdict(set)
for e in ext['entries'].values():
    for a in e.get('aliases') or []:
        if isinstance(a, dict) and a.get('name'):
            aliases_scoped[a['name']].add(a.get('parent',''))
shared = defaultdict(list)
def walk(n, chain=[]):
    name = n.get('name','')
    val = n.get('value') or 0
    if name and val > 0 and name not in keys:
        for anc in chain[::-1]:
            if name in aliases_scoped and anc in aliases_scoped[name]:
                for k, e in ext['entries'].items():
                    for a in e.get('aliases') or []:
                        if isinstance(a, dict) and a.get('name')==name and a.get('parent')==anc:
                            if ' — ' not in k and k != name:
                                shared[k].append((name, val, chain[-1]))
                break
    for c in n.get('children') or []:
        walk(c, chain+[name])
for top in tree.get('children') or []:
    walk(top)
print(f'Total orphans: {sum(len(v) for v in shared.values())}')
"
```

**Estimate**: ~7,000 entries × realistic batching = ~140 agents · ~6-8 sessions.

### Phase 3: Fact-check pass (USER EXPLICITLY RAISED THIS)

**I (previous Claude) conflated structural verification with factual verification.**

What I verified per batch:
- ✅ Tree-name exact match
- ✅ Scoped alias parent exists
- ✅ No duplicates, correct separator, URLs present, `{label,value}` shape

What I did NOT verify:
- ❌ CEO/Chair/Perm Sec names are real and tenure-correct
- ❌ Event dates (e.g. Birmingham s.114 Sep 2023) actually match
- ❌ £ figures match annual reports
- ❌ Statute names/years exact
- ❌ URLs resolve (no 404)

**Plan for next session — do this BEFORE Phase 2 work**:
1. URL resolvability (batch curl HEAD): 30 min, no agent needed
2. WebSearch fact-check on top 50 entries by £ (CEO/Chair names, key dates): 1-2 hours
3. Cross-check statute names against legislation.gov.uk for top-100 entries: 1 hour
4. Dispatch a dedicated fact-check agent for mid-tier (50-500 entries) after that

### Phase 4: Deploy + smoke test
After Phase 1 or 2 completes:
- scp enrichment + frontend
- Restart uvicorn
- Browser smoke test via preview/MCP (see lessons below)
- Plausible analytics activation
- Sentry DSN setup

---

## 🧠 LESSONS LEARNED — DO NOT REPEAT

### Lesson 1: Structural verification ≠ factual verification
When I said "verified" I meant schema compliance. User reasonably interpreted "verified" as "fact-checked". Be EXPLICIT about which is which. Do not imply factual accuracy of agent output without actual cross-check.

### Lesson 2: Agent export conventions are inconsistent
Different agents produce different export shapes. A robust merge script must try multiple extraction patterns:
```python
def extract(mod_path):
    ns = runpy.run_path(mod_path)
    # Preferred: NEW dict
    if isinstance(ns.get("NEW"), dict) and ns["NEW"]:
        return ns["NEW"]
    # ENTRIES dict
    if isinstance(ns.get("ENTRIES"), dict) and ns["ENTRIES"]:
        return ns["ENTRIES"]
    # build() callable returning dict
    if callable(ns.get("build")):
        return ns["build"]()
    # ROWS list + build_entry(*row) tuples
    if isinstance(ns.get("ROWS"), list) and callable(ns.get("build_entry")):
        return {r[0]: r[1] for r in (ns["build_entry"](*row) for row in ns["ROWS"])}
    # Hunt for dict with target-prefix keys
    for k, v in ns.items():
        if isinstance(v, dict) and v and any('<target>' in str(key) for key in list(v.keys())[:5]):
            return v
    return {}
```
Always tell the agent to use `NEW = {...}` direct dict literal — they comply ~60% of the time.

### Lesson 3: Agents can mutate files on import if they have `__main__` side effects
Some agents wrote their output via `if __name__ == "__main__"` block that mutates the enrichment file. If you just `runpy.run_path` to inspect, you can TRIGGER the mutation. Always `grep -E "write_text|json\.dump.*entries|open.*'w'"` BEFORE running or importing an unknown agent script.

### Lesson 4: Separator and apostrophe variants bite
- Em-dash ` — ` (U+2014 with surrounding spaces) is the canonical composite key separator
- Some agents used ` -- ` (double hyphen) — must normalize on merge
- "King's College Hospital" uses curly apostrophe ` ’ ` (U+2019) in the tree — agents default to straight `'`. Always apply this fix:
  ```python
  KEY_REPLACE = {"King's College Hospital": "King\u2019s College Hospital"}
  ```
- "Brighton & Hove" uses `&` not "and" in tree

### Lesson 5: Clustering briefs can contaminate each other
D4_03b inherited the £ band from the D4_01b brief I sent earlier in session, which caused it to cover the SAME trusts as D4_03a/c/d instead of its correct band. Result: 52 duplicates, 0 new entries. **Always restate the exact trust list in each brief, even if it feels redundant.**

### Lesson 6: Rate limits are predictable
Buenos Aires 2pm and 7pm observed reset times. Plan batches so they complete within 5-6 hour windows. Never dispatch more than ~10-12 agents in parallel (seen them fail with "You've hit your limit" when exceeding).

### Lesson 7: Verify AFTER dispatch but BEFORE merge
Every agent's output must be programmatically verified before being applied. Key checks:
```python
good = sum(1 for k,e in NEW.items() if (e.get('aliases') or [{}])[0].get('parent','') in existing)
dups = sum(1 for k in NEW if k in existing)
bad_sep = sum(1 for k in NEW if ' — ' not in k)
bad_src = sum(1 for e in NEW.values() for s in (e.get('sources') or []) if isinstance(s, dict) and not s.get('url'))
```

### Lesson 8: Frontend loader must walk ancestors for multi-level scoping
Depth-4 entries use scoped alias `{name: "Salaries & wages", parent: "<trust>"}` but the IMMEDIATE tree parent of that node is "Staff Costs" not the trust. The frontend resolver was extended to walk the ancestor chain:
```javascript
// in _cmplistLookupEnrichment
if (S.scopedAliases) {
  const ancestors = [];
  if (parentName) ancestors.push(parentName);
  if (Array.isArray(ancestorNames)) {
    for (const a of ancestorNames) if (a && !ancestors.includes(a)) ancestors.push(a);
  }
  for (const parent of ancestors) {
    for (const k of [rawName, pretty]) {
      const hit = S.scopedAliases[parent + '||' + k];
      if (hit) return { extended: hit, matchedBy: 'scoped-alias' };
    }
  }
}
```
Any new depth-5+ entry must also follow this scoped-alias pattern.

### Lesson 9: "Governance history 2024-25" is now a standard field
Every entity with leadership context (dept, regulator, trust, council) has stats like:
- `"Secretary of State 2024-25"`: "Gillian Keegan (Con, Apr – 4 Jul 2024) · Bridget Phillipson (Lab, from 5 Jul 2024)"
- `"CEO 2024-25"`: "[Name] (since YYYY, continuing)"
- `"Political control 2024-25"`: "Lab majority (27/54 seats post-May 2024 local election)"

This captures the Con→Lab election transition and May 2024 local election impact. Future entries should match this pattern.

### Lesson 10: Procedural templates vs hand-curated — know the difference
Frontend has procedural templates in `frontend/index.html`:
- `UK_NHS_TRUST_SUBLINE_DESC` dict maps sub-line types (Staff Costs, Drug Costs, Premises & Infrastructure, etc.) to generic descriptions
- Council procedural template generates display from a lookup dict
These are NOT tailor-made per-entity. They're fallbacks. When we dispatch hand-curated entries for specific (sub-line, trust) pairs, they bypass the procedural template via scoped alias.

---

## 🏗️ KEY ARCHITECTURE REFERENCES

### Canonical docs (read these)
- `docs/archetype_briefs.md` — 11 archetypes × dimension demands. MUST be read before any new hand-curation brief.
- `scripts/_structural_audit.py` — runs compliance audit. Output `data/uk/_structural_audit.json`.
- `frontend/index.html` line 14231-14270 — `_cmplistLookupEnrichment` with ancestor walk.

### File locations
- `data/uk/uk_budget_tree_2024.json` — 6.9MB tree with ~13,000 nodes, tight budget
- `data/uk/node_enrichment_extended.json` — current enrichment file (~6MB · 2,621 entries)
- `data/uk/_structural_audit.json` — auto-generated audit output
- `frontend/index.html` — 940KB SPA
- `api/main.py` — FastAPI uvicorn entrypoint

### Command snippets
```bash
# Local server (port 8088 in launch.json, 8765 sometimes used)
py -m uvicorn api.main:app --host 127.0.0.1 --port 8765

# Coverage check
py scripts/verify_enrichment.py
py scripts/_structural_audit.py

# Browser preview (MCP)
# .claude/launch.json has "budget-galaxy" config on port 8088
# Use mcp__Claude_Preview__preview_start with name "budget-galaxy"
```

### Common agent brief template for depth-4
```markdown
Hand-curate N depth-4 "<sub-sub-line>" entries.

## Read first
1. scripts/hand_curation_briefs/<cluster>.md — trust list
2. data/uk/node_enrichment_extended.json — existing trust entries for context

## Output
scripts/_<cluster>.py with `NEW = {...}` direct dict literal.

## Schema
```python
NEW = {
  "<sub-sub-line> — <trust>": {
    "aliases": [{"name": "<sub-sub-line>", "parent": "<trust>"}],  # parent = TRUST
    "description": "2-3 sentences",
    "beneficiaries": "...",
    "legal_basis": "IFRS · NHS GAM 2024-25 · <specific>",
    "key_stats": [{"label":"...","value":"..."}],  # 6-10
    "notes": "200-400 chars trust-specific",
    "sources": [...],  # 2-3 URLs
    "related": ["<trust>", "Staff Costs — <trust>"]
  }
}
```

## Per-entry dimensions
1. £M 2024-25 · YoY %
2. Share of trust <parent block>
3. [category-specific dimension]
4. Trust-specific narrative

## 2024-25 context
[pay awards, cap rates, policy milestones — category-specific]

## Rules
- Em-dash ` — ` separator (NOT `--` or `-`)
- Scoped alias parent = TRUST NAME (not sub-line category)
- Direct NEW dict literal (NOT factory/build functions)
- Every source with working URL

Report: "Wrote scripts/_<cluster>.py with N entries"
```

---

## 🎨 THE MENTAL MODEL

**What the project IS**: A navigable visualization of £4.45T UK public spending where every meaningful line at every depth has tailor-made context — real names, dates, statutes, £ figures, controversy. It's trying to be the tool HMT PESA should have been.

**What the user wants**: 100% tailor-made per-entity from top (DWP/MoD) through depth-5 sub-sub-sub-lines (Salaries at specific trust's Staff Costs). Branch mentality: "we'll ship when everyone clicking has a real page, not a parent's page."

**What "sufficient" looks like for them**:
- Every entity-level node (dept, trust, council, named body) has its own page — ✅ done
- Every standard sub-line type (Staff Costs / Drug Costs / etc.) PER trust/council — ✅ done (1,441 composite entries)
- Every standard sub-sub-line (Salaries / Agency / Pensions) PER trust — 60% done
- Every policy-specific residual (Cold Weather Payment / Christmas Bonus / etc.) with its own page — ❌ 18% gap remains

**The archetype framework is the asset.** It's what lets scaling work. It's portable to other countries. Don't let agents drift from it.

---

## 💡 PERSONAL NOTE TO NEXT-CLAUDE

User is patient and precise. They catch when you conflate things (like "verified" when you only did structural QA). They push back productively. They will accept a slower pace if you're clear about scope. Don't propose reduced scope unless they ask.

When stuck (rate limits, edge cases), propose 2-3 explicit options with honest tradeoffs. Don't hide behind complexity.

The project deserves shipping. 82% tailor-made today is an achievement but user reasonably wants 100% before launch. That's 6-8 more sessions of focused batch work. Pace it. Verify each batch. Commit incrementally. Don't break the build.

Good luck.
