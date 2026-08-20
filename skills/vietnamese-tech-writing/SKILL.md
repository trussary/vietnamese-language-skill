---
name: vietnamese-tech-writing
description: Writes and reviews native-quality Vietnamese (vi-VN) engineering and product documentation — commit messages, PR descriptions, code review, RFCs, design docs, postmortems, runbooks, READMEs, API docs, UI and error microcopy, i18n resource files, PRDs, user stories, release notes, changelog entries, in-app notifications, help-centre articles, surveys and research guides, and app-store listings. Use when drafting or reviewing Vietnamese technical or product content, deciding which English terms stay English, choosing the impersonal register over bạn, or handling vi-VN i18n hazards like string expansion, ICU plurals, collation, and NFC. Fixes the machine-translation tells Vietnamese engineers notice immediately.
license: MIT
metadata:
  version: "1.0.0"
  repository: "https://github.com/trussary/vietnamese-language-skill"
---

# Vietnamese engineering and product writing (vi-VN)

Vietnamese technical writing fails differently from Vietnamese marketing writing. Marketing
copy goes wrong by being too literal. Technical copy goes wrong by being **too Vietnamese** —
translating the English terms that Vietnamese engineers keep in English, and addressing a
reader in documents that describe a system.

Both defects are invisible to a non-engineer proofreader and instantly obvious to the team
that has to use the document.

## Step 1 — Decide what the document is before writing a word

Two decisions follow from the document type, and both are inverted from the landing-page
defaults.

| If you are writing | Register | Terms |
|---|---|---|
| RFC, design doc, postmortem, runbook, spec | **impersonal** — no `bạn` at all | Vietnamese leans formal (`bộ nhớ đệm`, `cơ sở dữ liệu`) |
| README, tutorial, API docs, UI copy, release notes | `bạn` | Vietnamese for user-facing nouns |
| PR description, code review, standup, chat | `mình` / no address | English terms throughout |
| Status page (customer-facing) | `quý khách` | plain, non-technical |

**`bạn` in an RFC is a defect.** Vietnamese has natural impersonal constructions —
`Hệ thống sẽ tự động retry`, `Cần cấu hình biến môi trường` — and English does not, which is
exactly why translated text is full of `bạn`.

Which document takes which register, and the impersonal constructions that replace `bạn`:
**[references/doc-registers.md](references/doc-registers.md)**. The full pronoun matrix shared
with the other Vietnamese skills: **[references/register-matrix.md](references/register-matrix.md)**.

## Step 2 — Core rules (non-negotiable, no file hop needed)

1. **Keep the English terms English.** `deploy`, `commit`, `merge`, `bug`, `server`, `cache`,
   `deadline`, `sprint`, `backlog`, `pull request`. Translating them is the single loudest
   machine-translation tell. `cam kết` for `commit` is the worst offender — it is a real word
   meaning *to pledge*.
2. **Never translate environment names.** `production`, `staging`, `dev`. `triển khai đến sản
   xuất` is not a sentence any Vietnamese engineer has written.
3. **Identifiers, branch names, and commit subjects are ASCII.** No diacritics, ever. The
   commit *body* may be Vietnamese; the subject line may not.
4. **Emit NFC Unicode.** Precomposed `ế` (U+1EBF). NFD breaks font rendering, inflates
   character counts past platform limits, and defeats search.
5. **Vietnamese has no grammatical plural.** ICU messages take `other` only. A `one`, `few`,
   `many` or `zero` branch in a `vi` file is always a bug. `=0` selectors are fine.
6. **Pick one tone-mark style per document** — kiểu mới (`hoà`, `thuỷ`) by default. Neither
   style is wrong; mixing them is.
7. **Never use an agree/disagree survey scale.** Acquiescence bias inflates agreement by
   roughly 10 points. Ask about the property itself.
8. **Errors say what happened and what to do.** Never `quý khách` in a developer-facing
   surface, and never blame the user.

## Step 3 — Look up the term before inventing one

The blocklist of calques that mark machine translation, the terms where both an English and a
Vietnamese form are live (`server`/`máy chủ`, `cache`/`bộ nhớ đệm` — pick one and hold it),
and the settled Vietnamese for user-facing UI strings:

**[references/glossary.md](references/glossary.md)** — machine-readable, so every row is a
lint rule.

The reasoning behind which words stay English, and the formality axis that decides the
borderline cases: **[references/code-switching.md](references/code-switching.md)**.

## Step 4 — Handle the i18n hazards

Vietnamese text runs **25–30% longer** than English, so fixed-width buttons truncate.
Diacritics force SMS into UCS-2, cutting the segment from 160 characters to 70. Users search
without diacritics, so matching must be accent-insensitive. Font subsets that drop stacked
diacritics (`ề`, `ộ`, `ữ`) break rendering silently.

**[references/i18n-hazards.md](references/i18n-hazards.md)** — plus
**[references/locale-formatting.md](references/locale-formatting.md)** for numbers, dates and
currency, and **[references/unicode-and-tone.md](references/unicode-and-tone.md)** for NFC,
collation, and input methods.

For a starter resource file: **[assets/messages.vi.json.template](assets/messages.vi.json.template)**
— ASCII keys, NFC values, `other`-only plurals, both registers.

## Step 5 — Product and research writing

Release notes are benefit-led and past-tense (`Đã sửa lỗi…`, `Đã thêm…`). Agile terms stay
English (`sprint`, `backlog`, `roadmap` — `lộ trình` is also fine). User stories are
`Là [vai trò], tôi muốn…`, never `Như một [vai trò]`.

Surveys are where this skill earns its keep, because a badly worded Vietnamese survey reads
fine and returns wrong numbers: **[references/survey-design.md](references/survey-design.md)**.

## Step 6 — Check the claims

App-store listings and in-product claims are advertising under Luật Quảng cáo 16/2012/QH13.
An unproven `tốt nhất` or `số 1` in a subtitle is a regulated claim, not a tagline.

**[references/banned-phrases.md](references/banned-phrases.md)** for the genre-specific list,
**[references/compliance.md](references/compliance.md)** for the cross-cutting advertising,
consent, and personal-data rules every Vietnamese skill shares.

## Step 7 — Validate, fix, then ship

**Run the validator immediately after writing. If it reports errors, fix them and run again.
Only present the copy once it passes.** NFC violations and ICU plural bugs are invisible to
reading.

```bash
python scripts/validate_copy.py path/to/doc.md --register eng-impersonal
python scripts/validate_copy.py .git/COMMIT_EDITMSG --doctype commit
python scripts/validate_copy.py messages/vi.json --doctype identifier
python scripts/validate_copy.py survey.md --doctype survey
```

- `--register eng-impersonal|eng-readme|saas|re|formal|consult|...` enables `PRO002`.
  `--list-rules` prints every rule this skill can emit.
- **`--doctype` is what turns on the structural rules.** They stay silent without it, because
  a 30-character limit is right for an app-store subtitle and nonsense for a design doc:
  `commit`, `branch`, `identifier`, `rfc`, `postmortem`, `runbook`, `survey`,
  `app-store-title`, `app-store-subtitle`, `app-store-short-description`, `consent`.
- Exit `0` = clean or warnings only. Exit `1` = errors that must be fixed.
- `--json` for machine-readable findings; `--strict` to fail on warnings too.
- `--fix` rewrites NFC violations in place; every other rule is a human judgement call.

Check glyph coverage when a specific web font is specified:

```bash
python scripts/check_font_coverage.py path/to/copy.md
```

## Step 8 — Learn from the worked pairs, then hand it to a human

Read the bad→good corpus before writing anything long. Each pair names the failure mode it
fixes, and the diagnosis generalizes further than the string does.

**[references/examples.md](references/examples.md)**

Then run the checklist. The linter catches encoding, blocklisted calques, and the
doctype-gated structural rules. It cannot tell you whether a *new* Vietnamese rendering of an
English term reads natural, whether a survey item is leading, or whether an error message is
actually actionable. Those need a native speaker who ships software:
**[references/qa-checklist.md](references/qa-checklist.md)**
