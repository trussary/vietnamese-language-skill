# Changelog

All notable changes to this project are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to
[Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.1.0] — 2026-08-22

Expansion from four skills to five, adding school and academic writing.

### Added

- **`vietnamese-education-copy` skill** — K-12 report-card remarks and học bạ entries, sổ liên
  lạc entries and school-to-parent broadcasts, disciplinary and absence notices, university
  syllabi and course registration, transcripts and GPA statements, and diploma reissuance.
  Enforces MoET statutory grading terminology (Thông tư 22/2021, 27/2020, 08/2021, 21/2019).
  Five doctype-gated rules: `EDU001`, `EDU002`, `EDU003`, `EDU005`, `EDU006`. 18 eval pairs.
  EdTech product UI and tutoring-centre/study-abroad advertising were deliberately **not**
  folded into this skill — they route to `vietnamese-tech-writing` and
  `vietnamese-business-comms`, which already own those registers.
- **Four new register-matrix rows** — `edu-k12` (`em`), `edu-k12-primary` (`con`), `edu-parent`
  (`quý phụ huynh`), and `edu-uni` (no direct address, third-person `sinh viên`), plus a
  register-matrix section on teacher self-reference and the primary/secondary address line.
- **`research/education-research`** — the deep-research report behind this skill: genre
  inventories, register deltas, statutory-terminology tables, regulated-language findings for
  the 2024–2026 private-tutoring reform, and the reasoning for routing EdTech and tutoring
  marketing to the two existing skills rather than building them here.
- **`research/education-research-prompt.md`** — the deep-research brief that produced the report
  above, for the same audit trail the four earlier skills have.

### Changed

- `tools/build_examples.py` gained `k12` and `higher-ed` categories.

## [2.0.0] — 2026-08-20

Expansion from one skill to four, plus the repo-level work that made a second skill
possible at all.

### Added

- **`vietnamese-tech-writing` skill** — engineering and product documentation. Code-switching
  rules (which English terms stay English), the impersonal register that replaces `bạn` in
  RFCs, postmortems and runbooks, vi-VN i18n hazards, and survey design. Six doctype-gated
  rules: `ENG001`, `ENG003`, `ENG007`, `PROD002`, `PROD003`, `PROD004`. 28 eval pairs and a
  `messages.vi.json.template` starter resource file.
- **`vietnamese-business-comms` skill** — marketing and sales. Channel-driven register
  selection, B2B xưng hô, promotion and anti-spam law, and the sales artifacts a seller
  writes. Eight doctype-gated rules: `ZNS001`, `ZNS002`, `MKT001`, `MKT002`, `SALES001`,
  `SALES003`, `SALES004`, `SPAM001`. 28 eval pairs and a `bao-gia.md.template`.
- **`vietnamese-finance-copy` skill** — regulated finance. Thông tư 99/2025 statement
  terminology, e-invoice fields, statement formatting, and financial-promotion limits for
  securities, credit, insurance and digital assets. Five rules: `FIN001`, `FIN002`, `FIN005`,
  `FIN006`, `FIN007`. 24 eval pairs and a `hoa-don-gtgt.md.template`.
- **`shared/`** — one source of truth for the four references every skill needs
  (`register-matrix.md`, `unicode-and-tone.md`, `locale-formatting.md`, `compliance.md`) and
  for the validator engine.
- **`tools/sync_shared.py`** — copies `shared/` into every skill and `--check`s for drift in
  CI. Copies rather than symlinks because `npx skills use`, the Claude.ai zip upload and a
  plain `cp -r` each install exactly one folder.
- **`--doctype` flag** — gates rules that are only correct for one kind of artifact. They stay
  silent unless the caller declares the artifact type.
- **`--list-rules` flag** — prints the resolved rule set for a skill, including its domain
  rules.
- **Domain rule modules** — any `scripts/rules_*.py` beside the engine is imported
  automatically, giving each skill a home for rules that cannot be a Markdown table row.
- **Per-row severity** in the calque tables, so a stale statutory term can be an error while an
  unidiomatic rendering stays a warning.
- **`tests/test_shared_sync.py`** — every generated copy must match its source.
- **`tests/test_trigger_keywords.py`** — fails the build when two skills' descriptions claim
  the same trigger keyword.
- **`research/expansion-plan.md`** — the implementation plan, including why the research's
  build order was inverted.

### Changed

- **Register profiles moved from Python into `references/register-matrix.md`**, so adding a
  register is adding a table row. Adds `zns`, `b2b`, `press`, `livestream`, `eng-impersonal`,
  `eng-readme` and `finance-formal` to the original four.
- **`ICU001` now rejects every non-`other` CLDR plural category**, not only `one`, while still
  allowing explicit `=0` selectors.
- **CI iterates over `skills/*/`** instead of naming one skill, and gained checks for shared
  drift and eval-corpus validity.
- **`tools/build_examples.py`** builds every skill's `examples.md`, and tolerates new
  categories instead of requiring a code change first.
- README, `CONTRIBUTING.md`, the PR template, and both plugin manifests updated for four
  skills.

### Fixed

- **Tone-mark rule false positive on title-case `Quý`.** The `qu` digraph guard excluded only
  lowercase `q`, so any document containing both `Hóa` and `Quý khách` — which is most
  Vietnamese commercial writing — was reported as mixing the two tone-mark conventions.
- **Superlative rule false positive on numbered Markdown headings.** The `#1` pattern matched
  `## 1. Introduction`.
- **`ENG001` checked whole resource-file lines** when only the key must be ASCII, flagging
  every correct Vietnamese translation value.
- The `PRO001` hint pointed at a reference file only the landing skill has.

### Breaking

- **`evals/pairs.jsonl` moved to `evals/vietnamese-landing-copy/pairs.jsonl`.** Each skill now
  owns a corpus, because the good-string-is-clean assertion runs each pair through its own
  skill's validator and one corpus cannot serve four register profiles. Anything scripting
  against the old path needs updating.

### Not done

- **No native review yet.** Every glossary and corpus in the three new skills is drafted from
  research, not approved by a native speaker. The finance skill additionally needs an
  accountant for statement terminology and a lawyer for financial promotion, and its
  references say so explicitly.
- **Trigger evals not run.** `evals/trigger-queries.md` has a 20-prompt section per skill and
  an empty results log.
- The full TT 99/2025 account-code mapping and the exact NĐ 70/2025 e-invoice field labels are
  documented as unverified rather than guessed.

## [1.0.0] — 2026-08-20

First public release.

### Added

- **`vietnamese-landing-copy` skill** — router `SKILL.md` with the audience-to-register
  decision tree, seven core rules, and a mandatory validate-loop.
- **`references/glossary.md`** — EN→VI conventional wording for CTAs, UI strings, form fields,
  standardized real-estate section labels, and real-estate lead CTAs. The ❌ column is parsed
  at runtime as the calque blocklist.
- **`references/register-guide.md`** — pronoun matrix (`quý khách` / `quý vị` / `anh–chị` /
  `bạn` / `khách hàng`), the Hán-Việt vs thuần Việt prestige axis, classifiers, word-order
  traps, tone-mark conventions, and the real-estate vs SaaS house styles.
- **`references/locale-formatting.md`** — VND, colloquial tỷ/triệu pricing, dates, phones,
  addresses, BCP-47, slugs and the dual accented/unaccented SEO rule, Vietnamese font subsets
  and stacked-diacritic typography, NFC normalization, and the ICU `other`-only plural rule.
- **`references/banned-phrases.md`** — calque blocklist plus regulated superlatives, citing
  Luật Quảng cáo 16/2012/QH13 Điều 8 khoản 11, Nghị định 87/2026/NĐ-CP penalties, and the 2026
  Washima / Cosmos / Lotte enforcement decisions.
- **`references/legal-copy.md`** — Nghị định 13/2023/NĐ-CP consent requirements and standard
  consent lines, real-estate disclaimers, and required page furniture.
- **`references/examples.md`** — 35 bad-to-good pairs, each with a diagnosis. Generated from
  `evals/pairs.jsonl`.
- **`references/qa-checklist.md`** — six-dimension human review rubric with a sign-off table.
- **`scripts/validate_copy.py`** — dependency-free linter with 13 rules (`NFC001`, `CAL001`,
  `LAW001`, `DIA001`, `TONE001`, `NUM001`-`NUM004`, `DATE001`, `PHONE001`, `ICU001`,
  `PRO001`, `PRO002`), `--fix` for NFC, `--json`, `--strict`, `--register`, and suppression
  directives that work in any comment syntax.
- **`scripts/check_font_coverage.py`** — codepoint coverage against a CSS `unicode-range`,
  with `--from-css` and a warning for the glyphs Google Fonts historically omitted.
- **`assets/vi.json.template`** — next-intl structure in both registers, `other`-only plurals.
- **`evals/pairs.jsonl`** — 35-pair corpus that doubles as the validator's fixture set.
- **`evals/trigger-queries.md`** — 20 should-trigger / should-not-trigger prompts.
- **Tests** — corpus-driven rule assertions, false-positive guards, skill-spec compliance, and
  a check that the skill's own documentation passes its own linter.
- **Packaging** — four install paths: the `skills` CLI (`npx skills add`, works across Claude
  Code, Cursor, and other agents), a Claude Code plugin manifest with a single-plugin
  marketplace, a plain skill folder, and a claude.ai zip. CI checks that `npx skills add .
  --list` still discovers the skill, since that is the primary documented path.

### Notes

- Tone-mark convention defaults to kiểu mới (`hoà`); kiểu cũ (`hòa`) is equally valid and the
  validator only ever flags mixing the two.
- `LAW001` is a warning by design, and a test keeps it that way.
- Trigger eval: not yet run against a released build. Record the score here when it is.
