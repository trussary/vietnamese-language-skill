# Implementation plan — expanding to five business functions

Companion to [`exnpansion-research.md`](exnpansion-research.md). That document decides
*what* to build and *why*. This one decides *in what order*, *against which repo
constraints*, and *what has to change in the existing machinery first*.

**Headline:** the research treats "shared references" as the only shared-asset problem.
It is not. The validator, the eval-corpus test harness, the examples builder, and three of
four CI jobs are all hardcoded to `skills/vietnamese-landing-copy`. **No second skill can
ship until that is fixed.** Phase 0 below is a blocking prerequisite that produces zero
new Vietnamese content, and it is the largest single chunk of work in this plan.

---

## Contents

- [Where the repo is single-skill today](#where-the-repo-is-single-skill-today)
- [Phase 0 — make the repo multi-skill](#phase-0--make-the-repo-multi-skill)
- [Build order: a deviation from the research](#build-order-a-deviation-from-the-research)
- [Phase 1 — `vietnamese-tech-writing`](#phase-1--vietnamese-tech-writing)
- [Phase 2 — `vietnamese-business-comms`](#phase-2--vietnamese-business-comms)
- [Phase 3 — `vietnamese-finance-copy`](#phase-3--vietnamese-finance-copy)
- [Rule-by-rule cost table](#rule-by-rule-cost-table)
- [What this plan deliberately does not do](#what-this-plan-deliberately-does-not-do)
- [Open decisions](#open-decisions)

---

## Where the repo is single-skill today

Every item here is a hard blocker, not a tidiness concern.

| Coupling | Location | Why it breaks on skill #2 |
|---|---|---|
| Validator path | `tests/test_validate_copy.py:21` — `SKILL = ROOT/"skills"/"vietnamese-landing-copy"` | Every eval pair in the repo is run through the landing-copy validator. A finance pair with `expected_rules: ["FIN001"]` fails: that rule does not exist in that engine. |
| Single eval corpus | `evals/pairs.jsonl` | `test_good_string_is_clean` asserts the ✅ string fires **no** rule. A ✅ engineering string (`deploy lên production`) would trip landing-copy's `DIA001`/`CAL001`. One corpus cannot serve four register profiles. |
| Examples output path | `tools/build_examples.py:20` | Hardcoded to landing-copy's `references/examples.md`. |
| Category vocabulary | `tools/build_examples.py:22-34` — `CATEGORY_TITLES`/`ORDER` | The research's new categories (`marketing`, `sales`, `engineering`, `product`, `finance`) are not in the map; unmapped categories are dropped or crash. |
| CI `consistency` job | `.github/workflows/ci.yml` | Three steps name `skills/vietnamese-landing-copy/...` literally. Only the `spec` job loops over `skills/*/`. |
| Register set in Python | `scripts/validate_copy.py:45-50` — `REGISTERS` dict | Research needs `zns`, `b2b`, `eng-impersonal`, `finance-formal`. If registers stay in code, the four skills' validators diverge on that block and can no longer be one synced file. |
| Calque severity is heuristic | `scripts/validate_copy.py:355` — `WARN if " " not in phrase else ERROR` | `FIN003` (stale `Bảng cân đối kế toán`) must be an **error**; it is multi-word so it happens to land right, but `ENG002` (`cam kết`, single word) must be a warn and `FIN003`-class rules need to declare severity, not inherit it from word count. |
| Marketplace description | `.claude-plugin/marketplace.json` | Describes one landing-page plugin. Becomes wrong the moment a second skill ships. |

---

## Phase 0 — make the repo multi-skill

Ships no Vietnamese content. Everything after this is additive.

### 0.1 Create `shared/` as the single source of truth

```
shared/
  references/
    register-matrix.md        # canonical pronoun/register matrix (all four skills)
    unicode-and-tone.md       # NFC rule + kiểu mới/cũ consistency rule
    locale-formatting.md      # VND, dates, phones, slugs, ICU
    compliance.md             # cross-cutting ad-law / NĐ 13 / anti-spam citations
  scripts/
    validate_copy.py          # the engine, byte-identical in every skill
```

`compliance.md` is the research's negative recommendation made concrete: compliance is a
shared reference, **not** a fifth skill.

Extracting these means splitting today's `references/locale-formatting.md` (142 lines) and
`register-guide.md` (114 lines) into a shared core plus a landing-copy-specific remainder.
Budget real time for this — it is the fiddliest part of Phase 0.

### 0.2 `tools/sync_shared.py` (stdlib-only, matching repo policy)

```bash
python tools/sync_shared.py          # copy shared/* into every skills/*/
python tools/sync_shared.py --check  # exit 1 if any generated copy has drifted (CI)
```

- Copies `shared/references/*.md` → `skills/<name>/references/` and
  `shared/scripts/validate_copy.py` → `skills/<name>/scripts/`.
- Stamps each generated file with a `<!-- generated from shared/… — do not edit -->`
  header and a content hash.
- `--check` compares hashes and prints the exact `shared/` file to edit instead.

This is the research's recommendation (d). It is chosen over symlinks because
`tests/test_skill_spec.py::test_relative_links_resolve` and the zip/`npx skills` install
paths both need real files, and over hand-duplication because that drifts within one release.

**Honest cost:** one extra CI step, plus the discipline that a glossary fix goes in
`shared/`, never in the generated copy. Mitigate with the generated-file header and a
`--check` failure message that names the canonical path.

### 0.3 Generalize the validator engine

The engine must become byte-identical across skills. Three changes:

1. **Registers become data.** Move `REGISTERS` out of Python into a
   `<!-- machine-readable: registers -->` table in `references/register-guide.md`, parsed
   by the existing `_table_after_marker` helper. This extends the repo's stated design
   principle ("the blocklists live in Markdown, not Python") to the one remaining
   hardcoded table, and lets each skill declare `zns` / `b2b` / `eng-impersonal` /
   `finance-formal` without forking the engine.
2. **Per-row severity.** Add an optional severity column to the machine-readable calque
   tables, defaulting to today's word-count heuristic when absent. Required by `FIN003`
   and `ENG002`; back-compatible with every existing row.
3. **Domain rule hook.** After loading blocklists, the engine looks for a sibling
   `scripts/rules_<domain>.py` and, if present, loads it with `importlib` from its own
   directory. That module exports `RULE_DOCS` (merged, so
   `test_every_rule_id_is_documented` keeps passing) and a `check(line, ctx) -> [Finding]`
   entry point. Stdlib-only, same folder, so the skill stays self-contained and passes
   `test_scripts_are_stdlib_only`.

   This is where rules that are genuinely code — character counts, number parsing,
   parenthesised negatives — live. Rules that are just phrase lists stay in Markdown.

4. **A `--doctype` flag** alongside `--register`. Several proposed rules are only correct
   for one artifact type (`ZNS001` needs "this is a transactional template", `ENG001`
   needs "this is a commit subject", `MKT001` needs "this is a marketplace title"). Without
   a doctype flag these rules are unshippable false-positive generators. Values are
   declared per skill in the same machine-readable-table style as registers.

### 0.4 Split the eval corpus per skill

```
evals/
  vietnamese-landing-copy/pairs.jsonl      # today's 35 pairs, moved unchanged
  vietnamese-tech-writing/pairs.jsonl
  vietnamese-business-comms/pairs.jsonl
  vietnamese-finance-copy/pairs.jsonl
  trigger-queries.md                        # gains a section per skill
```

Three consumers to update: `tests/test_validate_copy.py`, `tools/build_examples.py`,
and the `Add an examples pair` section of `CONTRIBUTING.md`.

### 0.5 Parametrize the test harness

- `tests/test_validate_copy.py`: discover skills from `skills/*/scripts/validate_copy.py`,
  pair each with `evals/<skill-name>/pairs.jsonl`, and run today's two assertions per pair.
  Every existing test keeps its meaning; it just runs N times.
- New `tests/test_shared_sync.py`: assert every generated copy matches its `shared/` source
  hash (the local mirror of the CI `--check`).
- New `tests/test_trigger_keywords.py`: assert no two skills' `description` frontmatter
  claim the same trigger keyword, against a curated ownership table. The research flags
  trigger collision (Marketing vs Sales on "email", Engineering vs Product on "release
  notes") as the specific failure that makes the three-skill split fail in practice — this
  is what turns that warning into something CI catches.

### 0.6 CI

- Replace the three hardcoded paths in the `consistency` job with `for skill in skills/*/`
  loops, mirroring how the `spec` job already works.
- Add `python tools/sync_shared.py --check`.
- Add `python tools/build_examples.py --check` per skill (already `--check`-capable; needs
  the loop).
- The SKILL.md 500-line budget check already globs `skills/*/SKILL.md` — no change needed.
- Add the new skill JSON assets to the "Manifests are valid JSON" step.

### 0.7 Repo metadata

- `.claude-plugin/marketplace.json`: broaden the plugin description beyond landing pages.
- `.claude-plugin/plugin.json`: extend `keywords`.
- `README.md`: the skill table gains a row per skill; the install and "what the linter
  checks" sections need per-skill framing.
- `CHANGELOG.md`: Phase 0 is a `2.0.0` entry — `evals/pairs.jsonl` moving is a breaking
  change for anyone scripting against it.
- Optional tidy: rename `research/exnpansion-research.md` → `expansion-research.md` and fix
  inbound links.

**Phase 0 exit criteria:** a throwaway `skills/scratch-test/` skill with two eval pairs
passes the full suite and every CI job, without touching any file outside its own folder
and `evals/scratch-test/`.

---

## Build order: a deviation from the research

The research ranks **Finance → Marketing → Sales → Engineering → Product**, by
(value × rule density) ÷ (research + native-review cost).

That ranking is sound on its own terms, but it assumes the review resource exists. Its own
caveats say Finance needs *an accountant and a securities/insurance lawyer*, and that four
of its highest-value facts are unverified: the full TT 99/2025 account mapping, the
NĐ 87/2026 penalty figures, the exact NĐ 70/2025 e-invoice field labels, and whether any
instrument verbatim bans `cam kết lợi nhuận`. Shipping a finance skill first means shipping
the repo's highest-consequence guidance through its least-tested infrastructure, with its
citations unverified.

**Recommendation: invert the tail. Tech-writing → Business-comms → Finance.**

- Tech-writing is the **lowest-legal-risk** domain (the research explicitly notes
  engineering is largely outside advertising/finance law), so Phase 0's brand-new
  multi-skill machinery gets validated where a bug is embarrassing rather than actionable.
- Its rules reuse the **most existing engine primitives**: `ENG004` is today's `NFC001`,
  `ENG005` is a one-line extension of today's `ICU001`, `ENG002`/`PROD001` are Markdown
  table rows. Highest ratio of shipped rules to new code.
- It needs **no external professional reviewer** — a working Vietnamese developer, which
  is a far easier person to recruit than a securities lawyer.
- Finance last means it is built on infrastructure already proven by two skills, and its
  legal review can run in parallel with Phases 0–2 instead of blocking the whole programme.

If Finance genuinely must ship first for external reasons, the mitigation is: ship every
`FIN*` rule at `warn`, never `error` (the research already recommends this for `FIN001`),
and gate `FIN003`/`FIN007` behind a `<!-- reviewed-by: ... -->` annotation until an
accountant signs off. That is a real downgrade in the skill's value, which is the cost of
the ordering.

**This is the plan's one open decision — see [Open decisions](#open-decisions).**

---

## Per-skill deliverable template

Each of Phases 1–3 produces the same shape. Listed once here rather than three times.

1. `skills/<name>/SKILL.md` — frontmatter per the research (descriptions are already
   drafted there and are within the 1024-char limit); body ≤ 500 lines, router style,
   matching the existing skill's Step 1…Step 7 structure.
2. `skills/<name>/references/` — one level deep only. The four `shared/` files land here
   via `sync_shared.py`; domain-specific files are authored.
3. `skills/<name>/scripts/rules_<domain>.py` — only the rules that cannot be a table row.
4. `skills/<name>/assets/` — where a template earns its place.
5. `evals/<name>/pairs.jsonl` — the research supplies 10–12 drafted pairs per function.
   **These are drafts, not ship-ready**: each needs native review before merge, per the
   repo's existing bar ("a native Vietnamese speaker must approve any change to the
   glossary or the examples corpus").
6. `evals/trigger-queries.md` — a should-trigger/should-not section, target ≥ 18/20.
7. README row, `CHANGELOG.md` entry, marketplace keywords.

---

## Phase 1 — `vietnamese-tech-writing`

Engineering + Product, folded per the research (Product's checkable surface is too thin to
justify its own validator profile).

**References:** `code-switching.md` (the central artifact — the EN-stays-English glossary,
with `deploy`/`commit`/`merge`/`bug`/`cache`/`sprint`/`backlog`), `i18n-hazards.md`
(25–30% string expansion, accent-insensitive collation, Telex/VNI input, `vi-VN` vs `vi`,
font subsetting), `doc-registers.md` (the inverted default — impersonal for RFC/postmortem,
imperative for runbooks, `bạn` only in READMEs and user-facing docs), `survey-design.md`
(acquiescence bias; forbid agree/disagree Likert), `qa-checklist.md` (`ENG006`, `PROD005`).

**New registers:** `eng-impersonal`, `eng-readme`.
**New doctypes:** `commit`, `branch`, `rfc`, `postmortem`, `runbook`, `i18n`, `survey`,
`app-store`.

**Rules:** `ENG001`–`ENG005`, `PROD001`–`PROD004`. Of these, `ENG004` and `ENG005` are
existing engine rules reused or trivially extended; `ENG002`/`PROD001` are pure table rows;
only `ENG001`, `PROD003` and the doctype plumbing for `ENG003`/`PROD002`/`PROD004` are new
code.

**Watch item:** `ENG003` and `PROD002` are both flagged high-false-positive in the research.
Ship them `info`, not `warn`, until the corpus shows they behave.

---

## Phase 2 — `vietnamese-business-comms`

Marketing + Sales.

**References:** `channel-guide.md` (the ZBS/ZNS 400-char + template-tag rules, marketplace
title formula, press-release institutional register, livestream spoken register),
`b2b-xung-ho.md` (the research's biggest register gap — `anh/chị` + `em`, seniority
overrides role, the `Kính gửi` > `Dear` > `Chào anh/chị` opening tier and the
`Trân trọng` / `Thân mến` closing tier), `promo-law.md` (the 50% khuyến mại ceiling under
NĐ 81/2018 as amended by NĐ 128/2024, NĐ 91/2020 anti-spam windows, the KOL/KOC disclosure
duty new in Luật 75/2025/QH15 from 01/01/2026), `sales-artifacts.md` (báo giá VAT treatment
and validity date, dunning tone ladder, Tết formulas), `qa-checklist.md`.

**New registers:** `zns`, `b2b`, `press`, `livestream`.
**New doctypes:** `zns-transactional`, `zns-promotional`, `marketplace-title`,
`cold-outreach`, `bao-gia`, `press-release`.

**Rules:** `ZNS001`–`ZNS002`, `MKT001`–`MKT003`, `SPAM001`, `SALES001`–`SALES004`.
`LAW001` is inherited free. `MKT002` introduces the second annotation-suppressor in the
repo (`<!-- khuyến mại tập trung: ... -->`), deliberately mirroring the existing
`<!-- proof: ... -->` mechanism rather than inventing a new syntax.

**Currency of the legal content:** the 01/01/2026 changes (Luật 75/2025 KOL disclosure,
ZNS→ZBS migration) are the reason this skill cannot simply be copied from the landing
skill's `banned-phrases.md`.

---

## Phase 3 — `vietnamese-finance-copy`

Deliberately alone: its validator must be conservative in ways that would produce false
positives everywhere else.

**References:** `statement-terminology.md` (TT 99/2025/TT-BTC, in force 01/01/2026 —
including the `Bảng cân đối kế toán` → `Báo cáo tình hình tài chính` rename that makes every
pre-2026 LLM output stale), `e-invoice.md` (NĐ 123/2020 + NĐ 70/2025 mandatory fields),
`financial-promotion.md` (guaranteed-return bans, `lãi suất 0%` disclosure, investment-linked
insurance under TT 67/2023 Điều 53, the NQ 05/2025 crypto pilot),
`statement-formatting.md` (`Đơn vị tính: triệu đồng`, parenthesised negatives, `Quý I/II/III/IV`),
`qa-checklist.md` (`FIN008`, `FIN009` — the disclosure-completeness checks that are not
machine-checkable).

**New register:** `finance-formal`. **New doctypes:** `statement`, `e-invoice`,
`financial-promotion`.

**Rules:** `FIN001`–`FIN007`. `FIN004` is today's `NUM001` inherited. `FIN001` reuses the
existing superlative-regex machinery with a new `<!-- machine-readable: guaranteed-return -->`
table — no new code, just a second table of the same shape.

**Gate:** this skill does not merge without an accountant reviewing
`statement-terminology.md` and a securities/insurance lawyer reviewing
`financial-promotion.md`. Every claim the research marked unverified stays out of the
shipped skill, or ships annotated as unverified. `FIN001` ships `warn`, never `error`,
routing to legal review — the research is explicit that the ban is assembled from three
instruments rather than stated in one article.

---

## Rule-by-rule cost table

What each proposed rule actually costs once Phase 0 exists.

| Rule | Cost | Notes |
|---|---|---|
| `LAW001`, `NUM001`–`004`, `NFC001`, `TONE001`, `DIA001`, `ICU001` | **free** | Already in the engine; every skill inherits them. |
| `FIN004` | **free** | Is `NUM001`. |
| `ENG004` | **free** | Is `NFC001`. |
| `ENG005` | **1 line** | Extend `ICU001` from "flags `one`" to "flags any non-`other` key". |
| `ENG002`, `PROD001`, `SALES002`, `MKT003`, `FIN003` | **table rows** | Markdown only. `FIN003` needs the 0.3 severity column. |
| `FIN001` | **table + reuse** | New machine-readable table, existing superlative regex machinery. |
| `ENG001`, `ZNS002`, `MKT001`, `MKT002`, `PROD003`, `FIN002`, `FIN005`, `FIN006`, `FIN007` | **code** | `rules_<domain>.py`. Each needs a doctype to avoid firing everywhere. |
| `ENG003`, `SALES001` | **register data** | Free once 0.3 makes registers data — but both need a doctype flag to be usable. |
| `ZNS001`, `SPAM001`, `PROD002`, `PROD004`, `SALES003`, `SALES004` | **code, ship `info`** | All flagged medium-to-high false-positive by the research. Prove them against the corpus before promoting to `warn`. |
| `MKT004`, `SALES005`, `ENG006`, `PROD005`, `FIN008`, `FIN009` | **not code** | Human QA checklist entries. Do not attempt regexes for these. |

---

## What this plan deliberately does not do

- **No standalone Legal/Compliance skill.** Per the research: compliance is a cross-cutting
  reference, not an artifact type. It lands in `shared/references/compliance.md`.
- **No standalone Product skill.** Folded into tech-writing.
- **No five sibling skills.** Three, plus the existing landing skill — four total.
- **No symlinked references.** Breaks `test_relative_links_resolve` and the zip install path.
- **No cross-skill imports.** Each skill folder stays independently installable, because
  `npx skills use …@<skill>` and the Claude.ai zip upload both install exactly one folder.
- **No merging of the drafted eval pairs without native review.** The research's 42 drafted
  pairs are a starting corpus, not approved content.

---

## Open decisions

1. **Build order.** Research says Finance first; this plan recommends Finance last, for the
   review-capacity and infrastructure-maturity reasons above. This changes what Phase 1 is
   and should be settled before Phase 0 finishes.
2. **Phase 0 scope.** Is the throwaway-skill exit criterion worth it, or should Phase 0 and
   Phase 1 merge so the first real skill is the proving ground? Merging is faster but makes
   the Phase 1 diff hard to review.
3. **Native-reviewer pipeline.** Every phase is gated on review the repo does not currently
   have a named person for. The existing `.github/ISSUE_TEMPLATE/glossary-entry.yml` is the
   right mechanism; it needs reviewers attached to it.
