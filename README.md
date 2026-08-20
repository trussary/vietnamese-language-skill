# vietnamese-language-skill

*[Tiếng Việt](README.vi.md)*

Agent Skills that make Claude write Vietnamese a Vietnamese professional would actually ship.

Vietnamese is a low-resource language for LLMs. Unguided, the output is fluent-sounding
translationese: English word order in Vietnamese words, the wrong pronoun for the audience,
CTAs translated literally, advertising superlatives that are **illegal under Vietnamese law**,
and currency formatted the American way.

The left column is not a strawman. It is what you get by default — one example per skill:

`vietnamese-landing-copy`

```diff
- Học thêm về dự án của chúng tôi
+ Tìm hiểu thêm về dự án

- Chúng tôi cung cấp những căn hộ tốt nhất số 1 thị trường
+ Không gian sống đẳng cấp giữa lòng thành phố

- Giá: 2,500,000,000 VND
+ Giá chỉ từ 2,5 tỷ đồng
```

`vietnamese-tech-writing`

```diff
- cam kết các thay đổi
+ commit các thay đổi

- triển khai đến sản xuất
+ deploy lên production

- Bạn sẽ thử lại request khi gặp lỗi.
+ Hệ thống sẽ tự động retry request khi gặp lỗi.
```

`vietnamese-business-comms`

```diff
- Cà phê số 1 Việt Nam
+ Cà phê được hơn 10.000 khách hàng lựa chọn mỗi ngày

- Học thêm
+ Xem ngay

- Đơn hàng đã xác nhận. Ưu đãi giảm 50% hôm nay, đặt ngay!
+ Đơn hàng của Quý khách đã được xác nhận. Dự kiến giao trước 20/08.
```

`vietnamese-finance-copy`

```diff
- Cam kết lợi nhuận 12%/năm cho nhà đầu tư
+ Lợi nhuận kỳ vọng 12%/năm. Đầu tư có rủi ro; kết quả trong quá khứ không đảm bảo kết quả trong tương lai.

- Trả góp lãi suất 0% cho mọi đơn hàng
+ Trả góp lãi suất 0% — phí chuyển đổi 3%/khoản. Tổng chi phí phải trả: 10.300.000 ₫.

- Bảng cân đối kế toán tại ngày 31/12/2026
+ Báo cáo tình hình tài chính tại ngày 31/12/2026
```

## What is in here

| Skill | What it does |
|---|---|
| [`vietnamese-landing-copy`](skills/vietnamese-landing-copy/) | Landing-page copy — real-estate (bất động sản), SaaS, and e-commerce registers. Terminology glossary, conventional CTAs, section labels, lead-form legal copy. |
| [`vietnamese-tech-writing`](skills/vietnamese-tech-writing/) | Engineering and product docs — commits, PRs, RFCs, postmortems, runbooks, READMEs, API docs, UI microcopy, i18n files, PRDs, release notes, surveys. Code-switching rules and vi-VN i18n hazards. |
| [`vietnamese-business-comms`](skills/vietnamese-business-comms/) | Marketing and sales — email campaigns, Zalo ZNS/ZBS, ads, marketplace listings, press releases, cold outreach, báo giá, dunning, Tết greetings. B2B xưng hô and promotion law. |
| [`vietnamese-finance-copy`](skills/vietnamese-finance-copy/) | Regulated finance — hóa đơn điện tử, báo cáo tài chính, investor updates, fintech and insurance copy, credit disclosures. Thông tư 99/2025 terminology and financial-promotion limits. |

They share one validator engine and four references (register matrix, Unicode and tone marks,
locale formatting, compliance), which live in [`shared/`](shared/) and are copied into each
skill by a build step — every skill folder stays independently installable.

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

To try one skill in a single session without installing anything:

```bash
npx skills use trussary/vietnamese-language-skill@vietnamese-landing-copy
npx skills use trussary/vietnamese-language-skill@vietnamese-tech-writing
npx skills use trussary/vietnamese-language-skill@vietnamese-business-comms
npx skills use trussary/vietnamese-language-skill@vietnamese-finance-copy
```

### Claude Code plugin

```bash
/plugin marketplace add trussary/vietnamese-language-skill
```

Then install the `vietnamese-language-skill` plugin from the marketplace. Each skill appears
prefixed with the plugin name — `vietnamese-language-skill:vietnamese-landing-copy`, and so on.

### Plain skill folder

Copy the skills you want into your personal or project skills directory. Each folder is
self-contained — there is nothing to copy alongside it:

```bash
cp -r skills/vietnamese-landing-copy ~/.claude/skills/
cp -r skills/vietnamese-tech-writing ~/.claude/skills/
```

Use `.claude/skills/` inside a repo instead if you want it scoped to one project.

### Claude.ai / Claude Cowork

Zip a skill folder and upload it in skill settings:

```bash
cd skills && zip -r vietnamese-landing-copy.zip vietnamese-landing-copy
```

## Use it

Once installed, they trigger on their own. Ask for Vietnamese writing in the normal way, and
the keywords route to the right skill:

> Viết landing page cho dự án căn hộ cao cấp tại Quận 7

> Our Vietnamese README reads like Google Translate — should we translate "deploy"?

> Viết email chào hàng gửi khách doanh nghiệp, kèm báo giá có VAT

> Can we advertise a guaranteed 12% annual return in Vietnam?

Each skill's linter runs directly too, with no Claude involved:

```bash
python skills/vietnamese-landing-copy/scripts/validate_copy.py copy.md --register re
python skills/vietnamese-tech-writing/scripts/validate_copy.py CHANGELOG.md --doctype commit
python skills/vietnamese-business-comms/scripts/validate_copy.py email.md --doctype cold-outreach
python skills/vietnamese-finance-copy/scripts/validate_copy.py bctc.md --doctype statement
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
| `ICU001` | Any non-`other` ICU plural branch — Vietnamese has only `other` |
| `PRO001`/`PRO002` | Mixed register, or a pronoun that does not fit the declared one |

Each skill adds its own rules on top. Run `--list-rules` against a skill's validator to see
everything it can emit:

| Skill | Adds |
|---|---|
| `vietnamese-tech-writing` | `ENG001` non-ASCII commit subject, branch or identifier · `ENG003` direct address in an RFC or postmortem · `ENG007` hedged runbook step · `PROD002` agree/disagree survey scale · `PROD003` app-store metadata over the platform limit · `PROD004` consent copy with no purpose |
| `vietnamese-business-comms` | `ZNS001` marketing in a transactional Zalo template · `ZNS002` template over 400 characters · `MKT001` ALL-CAPS or emoji in a marketplace title · `MKT002` discount over the 50% ceiling · `SALES001` casual pronoun in B2B · `SALES003` outreach with no greeting · `SALES004` quote missing VAT or validity · `SPAM001` bulk message with no opt-out |
| `vietnamese-finance-copy` | `FIN001` guaranteed-return language · `FIN002` promotional rate with no total-cost disclosure · `FIN005` statement table with no `Đơn vị tính` · `FIN006` minus-signed negative · `FIN007` invoice missing `MST` or `thuế GTGT` |

**Rules that only make sense for one kind of document are gated behind `--doctype` and stay
silent without it.** A 400-character limit is right for a Zalo template and nonsense for a
design doc. The one exception is `FIN001`: guaranteed-return language is prohibited wherever
it appears, so it is never gated.

Suppress a rule where it is genuinely wrong:

```markdown
<!-- vlc-disable: TONE001 -->            file-level
Text here <!-- vlc-disable-line NUM001 -->
Thương hiệu số 1 <!-- proof: Khảo sát Nielsen VN 2026 -->
Giảm đến 90% <!-- khuyen-mai-tap-trung: QĐ 123/SCT ngày 01/06/2026 -->
```

Directives work in HTML, `//`, `/* */`, `#`, and JSON string values. The `proof` and
`khuyen-mai-tap-trung` annotations record that paperwork exists; they do not create it, and a
reviewer is expected to check.

## Design notes

Five decisions worth knowing before you contribute:

1. **The rule data lives in Markdown, not Python.** `validate_copy.py` parses the tables in
   `references/glossary.md`, `references/banned-phrases.md` and `references/register-matrix.md`
   at runtime. Adding a lint rule, or a whole register, is adding a table row — no code change,
   no test change. Rules that genuinely need logic go in a skill's own `scripts/rules_*.py`,
   which the engine imports automatically.
2. **Superlatives warn, they never block.** The law does not ban `số 1`; it bans `số 1`
   *without proof*. A linter that hard-blocks a legitimate proven claim gets disabled
   wholesale, which helps nobody. `FIN001` warns for a different reason: the guaranteed-return
   prohibition is assembled from three instruments rather than stated in one, so a warning that
   routes to a lawyer is the honest output.
3. **Tone-mark style is not a correctness question.** `hòa` (kiểu cũ) and `hoà` (kiểu mới) are
   both right. The skills default to kiểu mới and only ever flag *mixing* the two.
4. **Doctype gating is what keeps the linter switched on.** A rule that fires on documents it
   was never meant for gets the whole tool disabled, so structural rules stay silent until the
   caller declares what the artifact is.
5. **Shared files are generated, not symlinked.** `npx skills use`, the Claude.ai zip upload,
   and a plain `cp -r` each install exactly one folder, so every skill carries real copies of
   the shared references and engine. `tools/sync_shared.py` writes them and CI fails if a copy
   has drifted — edit `shared/`, never the copy.

## Contributing

The most valuable contributions here are **linguistic, not code**: a glossary row, a bad→good
example pair, a register profile for a vertical we do not cover. See
[CONTRIBUTING.md](CONTRIBUTING.md).

A native Vietnamese speaker must approve any change to the glossary or the examples corpus.

```bash
python -m pytest tests/ -q                # 500+ assertions, mostly the eval corpora
python tools/build_examples.py            # regenerate examples.md from evals/<skill>/pairs.jsonl
python tools/sync_shared.py               # copy shared/ into every skill
```

The finance skill has a higher bar: statement terminology needs an accountant, and anything
soliciting investment, describing insurance, or presenting a credit rate needs a lawyer.

## Background

[`research/research.md`](research/research.md) is the original design rationale: the documented
failure modes, the native conventions that fix them, the legal citations, and the Agent Skill
spec this repo is built to.

[`research/exnpansion-research.md`](research/exnpansion-research.md) is the research behind the
three newer skills — genre inventories, register deltas, regulated-language tables, and an
explicit list of what could not be verified.
[`research/expansion-plan.md`](research/expansion-plan.md) is how that research was turned into
the current layout, including why the build order was inverted.

## Licence

MIT — see [LICENSE](LICENSE). Legal references are provided for copywriting guidance and are
not legal advice.
