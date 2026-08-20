---
name: vietnamese-landing-copy
description: Writes and reviews native-quality Vietnamese (vi-VN) marketing copy for landing pages — especially real-estate (bất động sản) project pages, plus SaaS and e-commerce. Use whenever generating, translating, or reviewing Vietnamese website copy, headlines, CTAs, section labels, lead-form or legal text, or locale formatting (VND, dates, phone numbers). Fixes translationese, wrong pronouns and register, calqued CTAs, illegal ad superlatives, and broken Unicode or number formatting. Trigger on any Vietnamese landing page, đăng ký, tiện ích, căn hộ, dự án, or vi.json localization task.
license: MIT
metadata:
  version: "1.0.0"
  repository: "https://github.com/trussary/vietnamese-language-skill"
---

# Vietnamese landing-page copy (vi-VN)

Vietnamese is a low-resource language for LLMs. Left unguided, output defaults to
English-calqued translationese: fluent-sounding but obviously machine-written. It picks the
wrong pronoun, translates CTAs word-for-word, writes illegal advertising superlatives, and
formats currency the American way. Every rule below exists to stop a specific, observed defect.

## Step 1 — Pick the register before writing a single word

Vietnamese has **no neutral "you."** The pronoun is the first decision, not a detail.

| Audience | Address the reader as | Vocabulary |
|---|---|---|
| Real estate, finance, luxury, airlines, healthcare | `quý khách` | Hán-Việt heavy, ornate |
| Institutional, government, broadcast announcements | `quý vị` | Formal, plural |
| Sales consulting, mid-market services, local business | `anh/chị` | Warm, respectful |
| SaaS, tech, e-commerce, youth brands | `bạn` | Thuần Việt, terse |
| Policy, terms, descriptive prose (never direct address) | `khách hàng` | Neutral 3rd person |

If the brief does not say, infer from the product. A căn hộ cao cấp page is `quý khách`.
A developer tool is `bạn`. **Never mix two registers in one page** — that is the single most
visible amateur tell.

Full pronoun matrix, including the registers the other Vietnamese skills use:
**[references/register-matrix.md](references/register-matrix.md)**. The Hán-Việt vs thuần Việt
prestige axis, classifiers, and the section-order house style:
**[references/register-guide.md](references/register-guide.md)**

## Step 2 — Core rules (non-negotiable, no file hop needed)

1. **Emit NFC Unicode.** Precomposed `ế` (U+1EBF), never base + combining marks. NFD breaks
   web font rendering and string length. Normalize everything you output.
2. **Pick one tone-mark style and hold it for the whole document.** Default to *kiểu mới*
   (`hoà`, `thuỷ`, `khoẻ`) matching post-2022 Bộ GD&ĐT textbooks. *Kiểu cũ* (`hòa`, `thủy`,
   `khỏe`) is equally correct and still dominant commercially — match the client's existing
   site when there is one. **Neither is wrong. Inconsistency within one page is the defect.**
3. **Modifier follows the noun.** `căn hộ cao cấp`, never `cao cấp căn hộ`.
4. **Recast English passives.** `được thiết kế bởi X` → `do X thiết kế`, or make it active:
   `X kiến tạo`.
5. **Never write `số 1`, `tốt nhất`, `duy nhất`, `hàng đầu` as an unproven claim.** This is
   illegal under Điều 8 khoản 11 Luật Quảng cáo 16/2012/QH13, not merely tacky. Real fines,
   currently issued. See [references/banned-phrases.md](references/banned-phrases.md).
6. **Vietnamese has no grammatical plural.** ICU messages take only `other`. An `one {}`
   branch in `vi.json` is always a bug.
7. **Write CTAs from the conventional list, not from the English.** `Learn more` is
   `Tìm hiểu thêm`, never `Học thêm`.

## Step 3 — Look up the conventional wording

Do not invent Vietnamese for a UI string that already has a settled convention. The EN→VI
table covers CTAs, nav labels, form fields, and the standardized real-estate section names
(`Tổng quan dự án`, `Vị trí`, `Tiện ích`, `Mặt bằng`, `Tiến độ`, `Chính sách bán hàng`,
`Chủ đầu tư`, `Pháp lý`).

**[references/glossary.md](references/glossary.md)**

## Step 4 — Format numbers, dates, and locale data correctly

VND groups with periods and decimalizes with commas: `2.500.000 ₫`. Real-estate prices are
colloquial: `Chỉ từ 2,5 tỷ`, `35 triệu/m²`. Dates are `dd/MM/yyyy`. Phones are `0xxx xxx xxx`
or `+84`. Addresses run small-to-large. Slugs are unaccented, lowercase, hyphenated.

**[references/locale-formatting.md](references/locale-formatting.md)** — also covers
`Intl.NumberFormat('vi-VN')`, BCP-47 tags, font subsets and stacked-diacritic typography,
and the accented/unaccented dual-keyword SEO rule. The NFC and tone-mark rules behind points
1 and 2 above are in **[references/unicode-and-tone.md](references/unicode-and-tone.md)**.

## Step 5 — Get the legal copy right

Lead forms are regulated. Nghị định 13/2023/NĐ-CP requires express, informed, revocable
consent with a stated purpose and a linked `Chính sách bảo mật`. Advertising superlatives
require documented proof.

**[references/legal-copy.md](references/legal-copy.md)** and
**[references/banned-phrases.md](references/banned-phrases.md)** for the landing-page
specifics; **[references/compliance.md](references/compliance.md)** for the cross-cutting
advertising, consent, promotion and anti-spam rules every Vietnamese skill shares.

## Step 6 — Validate, fix, then ship

**Run the validator immediately after writing. If it reports errors, fix them and run again.
Only present the copy once it passes.** Do not skip this because the output "looks fine" —
NFC violations and comma-grouped numbers are invisible to reading.

```bash
python scripts/validate_copy.py path/to/copy.md --register re
```

- `--register re|saas|formal|consult` enables the register-consistency check.
- Exit `0` = clean or warnings only. Exit `1` = errors that must be fixed.
- `--json` for machine-readable findings; `--strict` to fail on warnings too.
- `--fix` rewrites NFC violations in place; every other rule is a human judgement call.

Check glyph coverage when a specific web font is specified:

```bash
python scripts/check_font_coverage.py path/to/copy.md
```

If a flagged superlative is backed by a licensed market survey or award certificate, keep it
and annotate the source instead of deleting it:

```markdown
Thương hiệu số 1 Việt Nam <!-- proof: Khảo sát Nielsen VN 2026, chứng chỉ số 123/NS -->
```

## Step 7 — Learn from the worked pairs

Before writing anything long, read the bad→good corpus. Each pair names *which* failure mode
it fixes, and the diagnosis generalizes further than the string does.

**[references/examples.md](references/examples.md)**

For structured localization files, start from
**[assets/vi.json.template](assets/vi.json.template)** — next-intl shaped, both registers,
`other`-only plurals.

For human review before publishing: **[references/qa-checklist.md](references/qa-checklist.md)**

## Quick self-check

Before returning Vietnamese copy, confirm:

- [ ] One register throughout; the pronoun matches the audience.
- [ ] Every CTA is from the glossary, not translated fresh.
- [ ] No unproven superlative anywhere on the page.
- [ ] Prices grouped with `.`, decimals with `,`, `₫` or `tỷ`/`triệu` colloquial form.
- [ ] Dates `dd/MM/yyyy`, phones `0xxx`/`+84`, address small-to-large.
- [ ] One tone-mark style, consistently.
- [ ] Lead form has a consent checkbox, a purpose statement, and a privacy-policy link.
- [ ] `validate_copy.py` exits clean.
