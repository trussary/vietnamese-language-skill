# Contributing

The most valuable contributions to this repo are **linguistic, not code**. A single accurate
glossary row helps more than a refactor. You do not need to write Python to improve this skill
meaningfully — the blocklists are Markdown tables that the validator reads at runtime.

## The review bar

**A native Vietnamese speaker must approve any change to `references/glossary.md`,
`references/examples.md`, or `evals/pairs.jsonl`.** Shipping wrong Vietnamese in a skill whose
entire purpose is to stop wrong Vietnamese is the one failure we cannot recover from. If you
are not a native speaker, open the PR anyway and say so — a reviewer will be found.

Everything else (scripts, CI, docs, formatting rules with a citation) follows ordinary review.

## Setup

```bash
git clone https://github.com/trussary/vietnamese-language-skill
cd vietnamese-language-skill
python -m pip install pytest
python -m pytest tests/ -q
```

The skill's own scripts are standard library only and must stay that way — a test enforces it.
`pytest` is a development dependency, never a runtime one.

To check your working copy is still discoverable and installable, point the `skills` CLI at
the local checkout:

```bash
npx skills add . --list       # should list every skill under skills/
npx skills add . --skill vietnamese-landing-copy   # install your working copy to try it
```

If `--list` stops finding a skill, its `SKILL.md` frontmatter is malformed — run
`python -m pytest tests/test_skill_spec.py -q` for the specific reason.

## Add a glossary row

Edit the table under `<!-- machine-readable: glossary -->` in
[`references/glossary.md`](skills/vietnamese-landing-copy/references/glossary.md):

```markdown
| Get a quote | `Lấy báo giá` | `Nhận báo giá` / `Nhận bảng giá` | re |
```

- **Column 2 (❌)** becomes a lint rule. Wrap it in backticks, one phrase per cell.
- **Column 3 (✅)** becomes the fix hint. Separate alternatives with ` / `.
- **Column 4** is the register tag: `universal`, `re`, `saas`, `legal`, or `formal`.
- Use `—` in column 2 when there is no common bad form.

**Then add a good example that proves the rule does not misfire.** The single most important
constraint on this blocklist:

> A blocklisted phrase must never be a substring of ordinary Vietnamese, or of the phrase we
> recommend instead.

`Thử miễn phí` looks like a fine entry until you notice it fires inside the recommended
`Dùng thử miễn phí`. `Tính chất` looks fine until you notice it means "nature, property" and
appears in `Hình ảnh mang tính chất minh hoạ`. Both are `—` rows for exactly this reason.
`tests/test_validate_copy.py::test_no_calque_is_contained_in_a_suggestion` catches the first
case automatically; only a good example catches the second.

## Add an examples pair

`references/examples.md` is **generated**. Edit [`evals/pairs.jsonl`](evals/pairs.jsonl)
instead, one JSON object per line:

```json
{"id": "cal-learn-more", "category": "calque", "en": "Learn more about our project", "bad": "Học thêm về dự án của chúng tôi", "good": "Tìm hiểu thêm về dự án", "diagnosis": "Học thêm means study more. Tìm hiểu is the verb for finding out about something.", "expected_rules": ["CAL001"]}
```

| Field | Meaning |
|---|---|
| `id` | Unique kebab-case slug |
| `category` | One of the keys in `tools/build_examples.py::CATEGORY_TITLES` |
| `en` | The English source or intent |
| `bad` | The defective Vietnamese |
| `good` | The native rewrite |
| `diagnosis` | **Required.** *Why* it is wrong — the part that generalizes |
| `expected_rules` | Rule ids that must fire on `bad`. `[]` if not machine-detectable |
| `register` | Optional; makes the test run with `--register` |
| `filename` | Optional; e.g. `vi.json` for i18n-file rules |

Then regenerate and test:

```bash
python tools/build_examples.py
python -m pytest tests/ -q
```

The corpus doubles as the validator's fixture set. Every pair asserts that the listed rules
fire on `bad`, **and that no rule at all fires on `good`**. That second assertion is what keeps
the linter trustworthy.

Never edit `references/examples.md` by hand — CI checks it matches the corpus.

## Add a superlative or calque pattern

Edit the tables under `<!-- machine-readable: superlatives -->` or
`<!-- machine-readable: calques -->` in
[`references/banned-phrases.md`](skills/vietnamese-landing-copy/references/banned-phrases.md).

Superlative cells are **regular expressions**, case-insensitive. Escape pipes inside a regex
as `\|` so the Markdown table still parses:

```markdown
| `số\s*(?:một\|1)\b` | "number one" | Named verbatim in the statute |
```

Legal patterns must cite a source. Add the statute, decree, or enforcement decision to the
prose above the table — the citations are why anyone trusts this file.

## Propose a register profile

New verticals (government, education, medical, F&B) are welcome. Open a `register-profile`
issue with:

- the pronoun and the self-reference;
- five real headlines from live Vietnamese sites in that vertical, with links;
- the vocabulary that distinguishes it from the profiles we already have.

Then add it to `references/register-guide.md` and to `REGISTERS` in `validate_copy.py`.

## Things we will not merge

- **A change that makes one tone-mark convention "correct."** `hòa` and `hoà` are both right.
  The only defect is mixing them within one document.
- **Hard-blocking superlatives.** `LAW001` warns by design; a test enforces it.
- **A blocklist entry with no good example**, or one that fires on correct Vietnamese.
- **Runtime dependencies in `skills/*/scripts/`.** Standard library only.
- **A SKILL.md body over 500 lines.** Detail belongs in `references/`; the body is a router.

## Commit and PR

- Conventional-ish commit subjects are appreciated: `glossary: add F&B CTA terms`.
- One concern per PR. A glossary batch and a validator change are two PRs.
- CI runs the test suite, regenerates `examples.md` to check it is current, and lints the
  skill's own documentation with the skill's own linter. All three must pass.

## Code of conduct

By participating you agree to the [Code of Conduct](CODE_OF_CONDUCT.md).
