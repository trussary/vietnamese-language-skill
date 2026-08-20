# Changelog

All notable changes to this project are documented here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to
[Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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
