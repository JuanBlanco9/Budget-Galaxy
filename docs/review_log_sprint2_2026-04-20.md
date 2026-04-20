# Sprint 2 Review Log — 2026-04-20

**Scope**: 3 top-level UK departments promoted from Tier B-compact to Tier A (gold standard).

**Result**: 3/3 at gold · 45 total Tier A entries in the system (up from 42 post-Academies fix).

| Dept | Stats | Sources | Aliases | Gold | Tree-match |
|---|---|---|---|---|---|
| MINISTRY OF JUSTICE | 15 | 8 | 2 | ✅ | ✅ |
| HM TREASURY | 14 | 7 | 3 | ✅ | ✅ |
| DEPARTMENT FOR TRANSPORT | 16 | 7 | 2 | ✅ | ✅ |

## What agents self-corrected / flagged

### MoJ
- **Reoffending rate cohort ambiguity**: agent flagged 37.5% is from-custody, overall rate is ~25%. I used "adult from custody cohort" explicit in the value label.
- **Prison estate count variance**: 120-123 over recent years. Used "~122" with justification.
- **IPP residual ~2,700**: approximate, flagged.
- **Legal Aid 2024-25**: may now be published, I kept 2023-24 with explicit year.

### HMT
- **CRITICAL double-count flag**: HMT £63.5B OSCAR INCLUDES debt interest (£105.2B gross). Our separate "Debt Interest Payments" Tier A exists already. Added explicit scope note in HMT's description warning against adding the two cards. Stats show HMT standalone operating DEL is ~£6B.
- Agent also clarified HMT vs Consolidated Fund distinction ("HMT is the plumber; Consolidated Fund is the pipe") — incorporated.

### DfT
- **HS2 Phase 1 as a RANGE not a point**: NAO March 2024 cites £49-57B (2019 prices), not a single number. I used the range explicitly.
- **TfL Covid bailout**: ~£6B across 6 EFAs. Agent flagged NOT to confuse with ~£22B figure sometimes cited for national rail TOC subsidies. Incorporated as explicit stat.
- **Silvertown Tunnel**: opened 7 April 2025.
- **South Western Railway public ownership**: 25 May 2025 transfer confirmed.

## Verifier flags — all resolved or explained

The new entries trigger the same scope-mismatch pattern as Sprint 1:
- MoJ: no new flags
- HMT: no new flags (debt interest flag covered in description)
- DfT: no new flags (HS2 entry's 2015 lifetime budget £55.7B vs £6.9B tree was already flagged in Sprint 0)

All 45 Tier A entries remain GOLD.

## Load-bearing claims for spot-check

1. **Prison peak 88,521 on 6 September 2024** — MoJ Prison Population Weekly Bulletin
2. **SDS40 effective 10 September 2024** — auto-release 50% → 40%
3. **Truss-Kwarteng timeline**: mini-budget 23 Sept 2022 → BoE emergency buying 28 Sept → Kwarteng sacked 14 Oct → Truss resigns 20 Oct (49 days)
4. **Oct 2024 Budget fiscal rule change**: PSND → PSND ex-BoE (+£50B headroom)
5. **HS2 Phase 2 cancellation**: 4 October 2023 by Sunak at Conservative conference
6. **Silvertown Tunnel opened**: 7 April 2025
7. **South Western Railway public ownership**: 25 May 2025

## Status

**12 of 15 Sprint-1-and-2 UK top-level departments** now at gold standard:

✅ Sprint 1: DWP (pre-existing) · DoH · Home Office · DfE · MHCLG
✅ Sprint 2: MoJ · HMT · DfT
✅ Pre-existing: MINISTRY OF DEFENCE · HM REVENUE AND CUSTOMS · SCOTTISH GOVERNMENT · NORTHERN IRELAND EXECUTIVE · WELSH ASSEMBLY GOVERNMENT

Still Tier B-compact (Sprint 3 candidates):
- DESNZ (£22B)
- DCMS (£9B)
- DSIT (£13B)
- FCDO (£12B)
- DEFRA (£6B)
- DBT (£2.5B)
- CABINET OFFICE (£16B)

## Next sprint

Sprint 3 — Energy + Culture + Science + Farming: **DESNZ · DCMS · DEFRA · DBT · DSIT + FCDO · Cabinet Office** (7 remaining). Can split into 2 batches of 3-4 each.
