# vietnamese-language-skill

Agent Skills that make Claude write Vietnamese a Vietnamese marketer would actually ship.

Vietnamese is a low-resource language for LLMs. Unguided, the output is fluent-sounding
translationese: English word order in Vietnamese words, the wrong pronoun for the audience,
CTAs translated literally, advertising superlatives that are **illegal under Vietnamese law**,
and currency formatted the American way.

```diff
- Học thêm về dự án của chúng tôi
+ Tìm hiểu thêm về dự án

- Được thiết kế bởi các kiến trúc sư hàng đầu
+ Do đội ngũ kiến trúc sư danh tiếng kiến tạo

- Chúng tôi cung cấp những căn hộ tốt nhất số 1 thị trường
+ Không gian sống đẳng cấp giữa lòng thành phố

- Giá: 2,500,000,000 VND
+ Giá chỉ từ 2,5 tỷ đồng
```

The left column is not a strawman. It is what you get by default.

## What is in here

| Skill | What it does |
|---|---|
| [`vietnamese-landing-copy`](skills/vietnamese-landing-copy/) | Writes and reviews Vietnamese landing-page copy — real-estate (bất động sản), SaaS, and e-commerce registers. Terminology glossary, pronoun matrix, locale formatting, advertising-law compliance, and a dependency-free linter. |

More Vietnamese skills are planned. The repo is laid out to hold several.

## Install

### `npx skills` (any agent)

The [`skills`](https://www.npmjs.com/package/skills) CLI installs into Claude Code, Cursor,
and other agents from one command — no plugin system needed:

```bash
npx skills add trussary/vietnamese-language-skill
```

Useful flags:

```bash
npx skills add trussary/vietnamese-language-skill --list       # see what is in the repo first
npx skills add trussary/vietnamese-language-skill -g           # install globally, not per-project
npx skills add trussary/vietnamese-language-skill -a '*' --all # every agent, no prompts
```

Then `npx skills list` to confirm, `npx skills update` to pull newer versions, and
`npx skills remove vietnamese-landing-copy` to uninstall.

To try the skill in one session without installing anything:

```bash
npx skills use trussary/vietnamese-language-skill@vietnamese-landing-copy
```

### Claude Code plugin

```bash
/plugin marketplace add trussary/vietnamese-language-skill
```

Then install the `vietnamese-language-skill` plugin from the marketplace. The skill appears
as `vietnamese-language-skill:vietnamese-landing-copy`.

### Plain skill folder

Copy the skill into your personal or project skills directory:

```bash
cp -r skills/vietnamese-landing-copy ~/.claude/skills/
```

Use `.claude/skills/` inside a repo instead if you want it scoped to one project.

### Claude.ai / Claude Cowork

Zip the skill folder and upload it in skill settings:

```bash
cd skills && zip -r vietnamese-landing-copy.zip vietnamese-landing-copy
```

## Use it

Once installed, it triggers on its own. Ask for Vietnamese copy in the normal way:

> Viết landing page cho dự án căn hộ cao cấp tại Quận 7

> Translate this pricing page to Vietnamese for a SaaS audience

> Review vi.json for register consistency

You can also run the linter directly, with no Claude involved:

```bash
python skills/vietnamese-landing-copy/scripts/validate_copy.py path/to/copy.md --register re
```

```text
copy.md:3:1: error CAL001  calque "Học thêm"
      → use "Tìm hiểu thêm / Xem thêm" (glossary.md)
copy.md:7:12: warn  LAW001  regulated superlative "số 1"
      → needs a licensed market survey or award certificate; annotate with
        <!-- proof: ... --> or rewrite as a countable fact
copy.md:11:8: error NUM001  comma-grouped number "2,500,000"
      → write "2.500.000"
```

Python 3.9+, standard library only. No install step.

## What the linter checks

| Rule | Catches |
|---|---|
| `NFC001` | Decomposed Unicode that breaks web-font rendering |
| `CAL001` | English calques, from the glossary blocklist |
| `LAW001` | Regulated superlatives (Luật Quảng cáo Điều 8 khoản 11) — warns, never blocks |
| `DIA001` | Vietnamese written without diacritics |
| `TONE001` | Both tone-mark conventions mixed in one document |
| `NUM001`–`NUM004` | Comma thousands separators, ungrouped amounts, period decimals, ASCII `m2` |
| `DATE001` | `MM/dd/yyyy` where Vietnamese uses `dd/MM/yyyy` |
| `PHONE001` | Trunk zero kept after `+84` |
| `ICU001` | ICU `one` plural branch — Vietnamese has only `other` |
| `PRO001`/`PRO002` | Mixed register, or a pronoun that does not fit the declared one |

Suppress a rule where it is genuinely wrong:

```markdown
<!-- vlc-disable: TONE001 -->            file-level
Text here <!-- vlc-disable-line NUM001 -->
Thương hiệu số 1 <!-- proof: Khảo sát Nielsen VN 2026 -->
```

Directives work in HTML, `//`, `/* */`, `#`, and JSON string values.

## Design notes

Three decisions worth knowing before you contribute:

1. **The blocklists live in Markdown, not Python.** `validate_copy.py` parses the tables in
   `references/glossary.md` and `references/banned-phrases.md` at runtime. Adding a lint rule
   is adding a table row — no code change, no test change.
2. **Superlatives warn, they never block.** The law does not ban `số 1`; it bans `số 1`
   *without proof*. A linter that hard-blocks a legitimate proven claim gets disabled
   wholesale, which helps nobody.
3. **Tone-mark style is not a correctness question.** `hòa` (kiểu cũ) and `hoà` (kiểu mới) are
   both right. The skill defaults to kiểu mới and only ever flags *mixing* the two.

## Contributing

The most valuable contributions here are **linguistic, not code**: a glossary row, a bad→good
example pair, a register profile for a vertical we do not cover. See
[CONTRIBUTING.md](CONTRIBUTING.md).

A native Vietnamese speaker must approve any change to the glossary or the examples corpus.

```bash
python -m pytest tests/ -q                # 100+ assertions, mostly the eval corpus
python tools/build_examples.py            # regenerate examples.md from evals/pairs.jsonl
```

## Background

[`research/research.md`](research/research.md) is the design rationale: the documented failure
modes, the native conventions that fix them, the legal citations, and the Agent Skill spec
this repo is built to.

## Licence

MIT — see [LICENSE](LICENSE). Legal references are provided for copywriting guidance and are
not legal advice.
