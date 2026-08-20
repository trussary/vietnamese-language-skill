# Implementation plan — expanding `vietnamese-language-skill` to five business functions

Implements [`expansion-research-prompt.md`](expansion-research-prompt.md). That document is a
*research brief*, not a spec: it ends before the build step and explicitly defers SKILL.md and
reference files until a native speaker has reviewed the report. This plan covers the whole arc —
prepare the repo, run the research, verify the law, get native sign-off, build, ship — and names
what is blocked on what.

**Status at the time of writing:** the research report the brief asks for **does not exist yet**.
`research/` holds the prior research (`research.md`) and the brief. Everything in Phases 1–5 is
downstream of producing it. Phase 0 is not, which is why it goes first.

---

## 1. What we are starting from

One shipped skill, `vietnamese-landing-copy` v1.0.0, with a build system that is genuinely good
and genuinely single-skill-shaped:

| Asset | State | Multi-skill readiness |
|---|---|---|
| `SKILL.md` router pattern, 135 lines | Solid, reusable as a template | ✅ copy the shape |
| 7 `references/*.md` | 4 are domain-specific, 3 are universal | ⚠️ needs a sharing story |
| `scripts/validate_copy.py` (575 lines) | Blocklists parsed from Markdown at runtime | ⚠️ `REF_DIR` is `__file__`-relative; registers are landing-copy shaped |
| `evals/pairs.jsonl` (35 pairs, 9 categories) | Doubles as the test fixture set | ⚠️ single hardcoded path |
| `tools/build_examples.py` | Generates `examples.md`, `--check` in CI | ⚠️ hardcodes one input and one output |
| `tests/` (105 passed, 4 skipped) | Spec test already globs `skills/*`; validator test does not | ⚠️ `test_validate_copy.py` hardcodes the skill |
| `.github/workflows/ci.yml` | 3 jobs | ⚠️ 4 steps hardcode `skills/vietnamese-landing-copy/` |

The repo's best idea — **lint rules live in Markdown tables, so adding a rule is adding a table
row** — is exactly what makes five more domains tractable. Preserve it everywhere.

---

## 2. Decisions this plan makes up front

The brief asks the research to recommend an architecture. Waiting for that answer blocks Phase 0,
so this plan commits to one now and treats the research as a chance to overturn it, not to
originate it.

### 2.1 Five sibling skills, not one big skill and not a router

```
skills/vietnamese-landing-copy/      (exists — scope narrows, see §7)
skills/vietnamese-marketing-copy/
skills/vietnamese-sales-comms/
skills/vietnamese-engineering-docs/
skills/vietnamese-finance-docs/
skills/vietnamese-product-writing/   (conditional — see §8)
```

Reasoning:

- **Triggering.** One `vietnamese-business-writing` skill would load a finance chart-of-accounts
  reference to write a commit message. Descriptions are the only routing signal; five narrow ones
  route better than one broad one.
- **Blocklist collision is quadratic.** `test_no_calque_is_contained_in_a_suggestion` enforces
  that no blocked phrase is a substring of a recommended one. That check is cheap across ~40 rows
  in one domain and brutal across ~250 rows pooled from five. Per-domain glossaries keep the
  collision surface small and keep a false positive in Finance from breaking Marketing.
- **Rule applicability genuinely differs.** `DIA001` (unaccented Vietnamese) is a defect in
  marketing copy and *correct* in a branch name. One skill cannot hold both defaults.

### 2.2 Shared core is duplicated by a generator, not referenced across folders

**The binding constraint: a skill folder is the unit of installation.** Installed to
`~/.claude/skills/vietnamese-finance-docs/`, a skill cannot reach
`../vietnamese-landing-copy/references/`. `test_optional_dirs_only` also forbids any directory
other than `references/`, `scripts/`, `assets/`, and `test_references_are_one_level_deep` forbids
nesting. So cross-skill references are out, and symlinks do not survive packaging.

Therefore: a repo-root `shared/` directory is the single source of truth, and a sync tool copies
it into each skill with a generated-file header.

```
shared/
├── references/
│   ├── core-rules.md          # NFC, tone-mark consistency, modifier order, passives, ICU plurals
│   ├── register-matrix.md     # the five-pronoun matrix + Hán-Việt ↔ thuần Việt axis
│   └── locale-formatting.md   # VND, dates, phones, addresses, slugs, BCP-47, fonts
└── scripts/
    ├── validate_copy.py       # the one canonical validator
    └── check_font_coverage.py
```

`tools/sync_shared.py` copies these into every `skills/*/` folder; `--check` fails CI on drift.
This is the exact pattern `tools/build_examples.py --check` already establishes, so it needs no
new concepts from a contributor.

**Honest maintenance cost:** every edit to a shared file produces a 6-file diff, and a
contributor who edits the copy instead of the source gets a red CI with a message telling them
which file to edit instead. That message must be good — it is the whole ergonomics of the scheme.

### 2.3 Rule enablement moves into Markdown, like everything else

`validate_copy.py` currently hardcodes `REGISTERS = {re, formal, consult, saas}` and a
landing-copy `DIACRITIC_PHRASES` list. Rather than fork the validator per domain, each skill
carries a `references/rule-config.md` with a `<!-- machine-readable: rule-config -->` table:

```markdown
| Rule | Severity | Note |
|---|---|---|
| `DIA001` | `off` | Unaccented Vietnamese is correct in identifiers, branches and slugs |
| `CAL001` | `warning` | English technical terms are native code-switching here, not calques |
| `ENG001` | `warning` | Accented identifier or commit subject |
```

The validator gains `--profile <skill>` which reads that table. One validator, six behaviours,
zero Python edits to add a domain. Severity may be lowered or a rule disabled per domain; the
mechanical rules (`NFC001`, `NUM001`, `NUM003`) may not be disabled anywhere.

### 2.4 Severity policy, inherited from `LAW001`

Legal and register rules **warn**; mechanical rules **error**. `test_law001_is_never_an_error`
already encodes this for advertising law and the same reasoning applies to every regulated-phrase
rule the new domains add: a linter that hard-blocks a legally defensible claim gets disabled, and
a disabled linter catches nothing. The `<!-- proof: ... -->` escape hatch extends to all of them.

---

## 3. Phase 0 — Make the repo multi-skill *(unblocked; start now)*

No research, no native reviewer, no legal question. Roughly 40% of the total engineering work and
it de-risks every later phase, because the first new skill then lands as content into a working
frame instead of as content *and* a refactor.

| # | Change | File | Detail |
|---|---|---|---|
| 0.1 | Extract the shared core | `shared/` (new) | Move the universal parts of `register-guide.md` / `locale-formatting.md` out of landing-copy; leave the real-estate house style behind as domain content |
| 0.2 | Write the sync tool | `tools/sync_shared.py` (new) | Copy `shared/**` into every `skills/*/`; `--check` for CI; generated-file header naming the source path |
| 0.3 | Per-skill eval corpora | `evals/<skill>/pairs.jsonl` | Move the existing 35 pairs to `evals/vietnamese-landing-copy/pairs.jsonl` |
| 0.4 | Generalize the examples build | `tools/build_examples.py` | Loop over `evals/*/pairs.jsonl` → `skills/<name>/references/examples.md`; `CATEGORY_TITLES` becomes per-domain-extensible |
| 0.5 | Parametrize the validator tests | `tests/test_validate_copy.py` | Replace `SKILL = ROOT/"skills"/"vietnamese-landing-copy"` with a fixture over `skills/*`; keep both assertions per pair |
| 0.6 | Add a sync-drift test | `tests/test_shared_sync.py` (new) | Fails if any skill's copy differs from `shared/` |
| 0.7 | Glob the CI steps | `.github/workflows/ci.yml` | Self-lint, font coverage, manifest-validation and skills-CLI-discovery steps iterate `skills/*/` instead of naming one skill |
| 0.8 | Rule-config support | `shared/scripts/validate_copy.py` | `--profile`, parsing `rule-config.md`; default profile preserves today's behaviour exactly |
| 0.9 | Document the contract | `CONTRIBUTING.md` | "Add a new domain skill" section; "never edit a synced copy" |

**Gate:** `python -m pytest tests/ -q` still reports **105 passed, 4 skipped**, and
`validate_copy.py` output on the landing-copy skill is byte-identical to before. Phase 0 is a
pure refactor — if landing-copy behaviour changes, the refactor is wrong.

---

## 4. Phase 1 — Run the research

Run the brief as **six scoped runs**, not one. The brief is written as a single prompt, but its
own required output format is five repeated per-function blocks plus a cross-cutting section —
and a single run across five domains will produce shallow coverage of all five rather than
buildable depth in any.

| Run | Scope | Output |
|---|---|---|
| 1.1–1.5 | One per function: Marketing, Sales, Engineering, Product, Finance | `research/expansion/<function>.md` |
| 1.6 | The five cross-cutting questions (architecture, shared references, validator reuse, failure-mode evidence, prioritisation) | `research/expansion/cross-cutting.md` |

Each run gets the brief's §"What already exists", §"Evidence standards" and the relevant
per-function block verbatim, plus this plan's §2 as the architecture the research should critique
rather than re-derive.

**Acceptance gate per run — reject and re-run if any fails:**

- Every terminology row has a real attestation (a live page, a repo, a published document).
  An empty cell with a note is acceptable; an invented Vietnamese term is a hard reject.
- Every legal claim carries instrument number, Điều/khoản, and effective date, and states
  explicitly whether it is still in force as of 2026.
- Every finding lands as one of: a glossary row, a lint rule, a citation, or a bad→good pair.
- Inferred material is labelled as inferred, separately from observed material.
- The open-questions section is populated — that section becomes the Phase 3 work queue.

---

## 5. Phase 2 — Legal verification *(parallel with Phase 1, separate reviewer)*

The highest-consequence and least-tolerant-of-error work in the project, and it applies to the
**existing** skill too, not just the new ones.

- `banned-phrases.md` and `legal-copy.md` currently cite Nghị định 87/2026/NĐ-CP (effective
  15/5/2026), Thông tư 12/2026/TT-BVHTTDL (5/7/2026), and enforcement decisions dated June–July
  2026 — all within months of today. **Re-verify every one is in force and unamended**, from
  thuvienphapluat.vn / chinhphu.vn / the issuing ministry.
- Verify the new instruments the brief names, several of which it flags as possibly superseded:
  NĐ 81/2018 (khuyến mại), NĐ 91/2020 (spam), NĐ 52/2013 + NĐ 85/2021 (e-commerce), NĐ 123/2020
  (e-invoice), Thông tư 200/2014/TT-BTC (chart of accounts), Luật Chứng khoán 2019, Luật Thương
  mại 2005, and the current Vietnamese IFRS adoption timetable.
- Flag any amendment whose effective date is still in the future, with the date.

**Output:** `research/expansion/legal-register.md` — one row per instrument: number, articles
cited, in force?, superseded by, effective date, verification date, source URL. This becomes the
citation source of truth for all six skills and gets re-checked at each release.

**Gate:** no regulated-phrase lint rule ships without a verified row here.

---

## 6. Phase 3 — Native-speaker review *(the critical path)*

`CONTRIBUTING.md` already requires native approval for `glossary.md`, `examples.md` and
`pairs.jsonl`. Five domains multiply that into roughly 250 glossary rows and 50+ eval pairs
needing sign-off. This is calendar-bound, not effort-bound, and it is the thing most likely to
stall the project — so schedule it as a resource rather than discovering it late.

Practical handling:

- **Batch by domain**, not by file. A reviewer reads one domain end to end and signs off once.
- **Two rounds**: round 1 on the research report's terminology tables and open questions (before
  any building), round 2 on the finished eval pairs (before merge). Round 1 catches fabricated
  terms while they are cheap to delete.
- **Finance and Engineering need domain-specialist natives**, not general ones — a Vietnamese
  accountant and a Vietnamese engineer respectively. Recruit these before Phase 1 finishes.
- **North/South and company-type variation** (state-owned / SME / FDI / startup) gets recorded
  as a note on the row, not resolved by picking one. The brief asks for this explicitly.
- Track sign-off in the PR, with the reviewer named and the domain stated.

---

## 7. Phase 4 — Build, one domain per PR

Each domain is an independent, shippable PR. Nothing about Marketing blocks Engineering.

### Definition of done for a domain skill

- [ ] `skills/<name>/SKILL.md` — router shape, body ≤ 500 lines, description ≥ 80 chars, no angle
      brackets, `name` matches the folder
- [ ] `references/` — domain glossary, domain register deltas, domain regulated language,
      `rule-config.md`, generated `examples.md`, `qa-checklist.md` for the non-machine-checkable rules
- [ ] Shared core synced in (`tools/sync_shared.py`)
- [ ] `evals/<name>/pairs.jsonl` — 8–12 pairs minimum, every `bad` fires its `expected_rules`,
      every `good` lints clean
- [ ] New rules registered in `RULE_DOCS` (a test enforces that every rule ID is documented)
- [ ] `evals/<name>/trigger-queries.md` — 10 should-trigger, 10 should-not, **including
      cross-skill cases** ("write a Vietnamese commit message" must route to engineering, not
      landing-copy)
- [ ] The skill's own docs pass the skill's own linter with zero errors
      (`test_skill_docs_are_clean` — note this bites when a reference file *documents* a calque;
      backtick it, inline code is masked)
- [ ] Native-speaker sign-off recorded, reviewer named
- [ ] Every legal citation traced to a Phase 2 verified row
- [ ] `CHANGELOG.md`, `plugin.json`, `marketplace.json` updated

### Reserved rule-ID namespaces

Reserve these now so domains built in parallel cannot collide:

| Namespace | Domain | Example rules |
|---|---|---|
| `NFC`, `TONE`, `NUM`, `DATE`, `PHONE`, `ICU`, `PRO`, `DIA`, `CAL`, `LAW`, `IO` | shared core (existing) | unchanged |
| `MKT###` | Marketing | promo-limit claims (NĐ 81/2018), spam-rule violations (NĐ 91/2020), channel length limits, missing advertiser identification |
| `SAL###` | Sales | salutation/closing register mismatch (`Kính gửi` vs `Thân mến`), `em`/`anh–chị` inconsistency within a thread |
| `ENG###` | Engineering | accented identifier / branch / commit subject, calqued technical term, `vi` vs `vi-VN` tag misuse |
| `FIN###` | Finance | missing `Đơn vị tính` header, negative numbers not parenthesised, guaranteed-return phrasing, non-standard statement terminology |
| `PRD###` | Product *(if built)* | leading survey wording, notification over length, missing accented/unaccented ASO pair |

### Register profiles to add

`REGISTERS` gains: `b2b` (`anh/chị`, sales), `eng` (`bạn`, tolerant of English code-switching),
`fin` (`quý khách` direct / `khách hàng` in prose). Each ships with its skill, in that skill's
`rule-config.md`.

---

## 8. Priority order

Ranked by (value of fixing) × (density of hard, checkable rules) ÷ (research + native-review cost).

| # | Domain | Why here |
|---|---|---|
| **1** | **Marketing** | Nearest neighbour to what already works — email, Zalo OA/ZNS, ads and marketplace listings reuse the existing glossary, `LAW001` and the whole register matrix. Cheapest research, highest reuse, general native reviewers suffice. Build first and use it to prove the Phase 0 frame. |
| **2** | **Engineering** | Rule density is high and the evidence is unusually accessible (Viblo, Kipalog, Vietnamese OSS). The code-switching question is genuinely unanswered and genuinely checkable. Needs an engineer reviewer, which is the easiest specialist to find here. |
| **3** | **Finance** | Highest value and highest legal risk, but gated on both the Phase 2 legal register and a scarce accountant reviewer. Do not start building before those two exist. |
| **4** | **Sales** | The xưng hô problem is the richest human rule set in the set and the least machine-checkable — it will land mostly as `qa-checklist.md` plus eval pairs, with few lint rules. Real value, low automation leverage. |
| **5** | **Product** | **Recommend not building as a separate skill unless the research overturns it.** Its genres already split across the others: UI microcopy and i18n → Engineering, ASO and release-note voice → Marketing, in-app notifications → Engineering. What is left that is genuinely its own — survey and interview instrument design, Vietnamese politeness bias on Likert/NPS — is a reference file, not a skill, and it would collide with three sibling descriptions for triggering. Fold it in and revisit if the research finds a distinct artifact set. A negative recommendation is a valid finding; this is one. |

---

## 9. Phase 5 — Trigger disambiguation and release

Easy to forget and it breaks the shipped skill if skipped.

`vietnamese-landing-copy`'s description is deliberately pushy and currently claims territory the
new siblings will own — notably `vi.json` localization, which is Engineering's. **Six skills all
matching the word "Vietnamese" will fight each other.**

1. Narrow the landing-copy description to landing pages proper; cede `vi.json`, i18n files and
   generic "Vietnamese copy" to their new owners.
2. Build a **cross-skill routing eval**: for each domain, 5 prompts that must load *that* skill
   and not a sibling. Score ≥ 18/20 per skill, per the existing `trigger-queries.md` bar.
3. Version bumps: minor for landing-copy (description change is user-visible behaviour), 1.0.0
   for each new skill, minor for the plugin.
4. `README.md` gets a skill-selection table; `CHANGELOG.md` logs the trigger-eval score per skill,
   as the existing process already requires.

---

## 10. Risks

| Risk | Impact | Handling |
|---|---|---|
| Research fabricates plausible Vietnamese terms | Catastrophic and quiet — the repo's whole premise is not shipping wrong Vietnamese | Attestation is a hard gate (§4); empty cell beats invention; native round 1 before building |
| Native reviewers unavailable, especially finance | Project stalls at 90% | Recruit during Phase 1, not Phase 3; batch by domain; Marketing needs no specialist so work continues |
| Legal citations go stale between research and release | Compliance rules that are themselves wrong | Phase 2 register with verification dates; re-check at each release; all legal rules warn, never block |
| Blocklist rows fire on correct Vietnamese | Contributors disable the linter and it stops catching anything | Per-domain glossaries; existing substring test; the "no rule fires on `good`" assertion per pair |
| Six skills under-trigger or cross-trigger | Users get no skill or the wrong one | §9 routing eval as a release gate |
| Shared-sync scheme rots (people edit copies) | Six diverging validators | `--check` in CI plus `tests/test_shared_sync.py`; error message must name the source file to edit |
| Scope inflation across five domains | Nothing ships | One domain per PR; Marketing ships alone and early |

---

## 11. Sequencing

```
Phase 0  ████████                          repo refactor — start immediately, blocks nothing
Phase 1      ████████████                  6 research runs, parallel
Phase 2      ████████████                  legal verification, parallel with 1
Phase 3            ██████        ██████    native review, round 1 then round 2 — CALENDAR-GATED
Phase 4                  ████ ████ ████    Marketing → Engineering → Finance → Sales
Phase 5                                ██  trigger disambiguation + release
```

| Phase | Engineering effort | Gated on |
|---|---|---|
| 0 — repo refactor | 1–2 days | nothing |
| 1 — research | ~1 day per run, parallelisable | nothing |
| 2 — legal | 2–3 days | nothing |
| 3 — native review | low effort, **high latency** | reviewer availability |
| 4 — build | 2–3 days per domain | Phases 0–3 for that domain |
| 5 — release | 1 day | all domains landed |

Phase 3 is the only item whose duration is not ours to set. Everything else is parallel or short.

---

## 12. Non-goals

- No new runtime dependencies. Scripts stay Python 3.9+ standard library — a test enforces it.
- No hard-blocking of legal phrasing. Warn plus `<!-- proof: ... -->`, everywhere.
- No declaring one tone-mark convention correct. Mixing remains the only defect.
- No skill for a domain where the honest finding is "this is a reference file" (see Product, §8).
- No `references/examples.md` edited by hand, in any skill. It is generated.
