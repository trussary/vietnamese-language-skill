<!-- GENERATED FILE — do not edit. Source: shared/references/locale-formatting.md (sha256 e03c611eb6eef309). Edit the source and run `python tools/sync_shared.py`. -->
<!-- vlc-disable: NUM001, NUM002, DIA001 -->

# Locale formatting — vi-VN

These rules are objective. Getting them wrong is not a matter of taste, and default LLM output
gets several of them wrong every time.

## Numbers and currency

**Decimal separator is a comma. Thousands separator is a period.** The opposite of US English.

| ❌ Wrong | ✅ Correct |
|---|---|
| `2,500,000 VND` | `2.500.000 ₫` |
| `2500000 VND` | `2.500.000 ₫` |
| `2.5 tỷ` | `2,5 tỷ` |
| `35,000,000/m2` | `35 triệu/m²` |

- VND has **zero minor units** (ISO 4217) — never write `2.500.000,00 ₫`.
- The `₫` symbol (U+20AB) goes **after** the number, with a space. `đồng` spelled out is
  equally correct and often warmer: `2,5 tỷ đồng`.
- `VND` in Latin letters is acceptable in tables, invoices, and technical contexts, but `₫`
  or `đồng` reads more natural in marketing copy.

```js
new Intl.NumberFormat('vi-VN').format(1234567);
// "1.234.567"

new Intl.NumberFormat('vi-VN', {
  style: 'currency', currency: 'VND', maximumFractionDigits: 0,
}).format(2500000);
// "2.500.000 ₫"
```

## Colloquial scale: tỷ and triệu

Large amounts are almost never written in full digits in Vietnamese prose. Use the
`tỷ` (billion) / `triệu` (million) scale.

| Context | ✅ Form |
|---|---|
| Headline price | `Chỉ từ 2,5 tỷ` / `Giá từ 2,5 tỷ đồng` |
| Precise price | `2 tỷ 500 triệu` / `2,5 tỷ đồng` |
| Per square metre | `35 triệu/m²` / `giá/m²` |
| Combined, as seen on live listings | `1,4 tỷ đồng (tương đương 22,5 triệu đồng/m²)` |
| B2B deal value in prose | `hợp đồng 35 triệu` / `doanh thu 2,5 tỷ` |

**Do not mix the two within one context.** Narrative prose takes `2,5 tỷ`; a table column
takes `2.500.000.000`. A table that switches between them mid-column is unreadable, and in a
financial statement it is a defect — see the finance skill for the statement rules.

Write `m²` with the superscript character (U+00B2), not `m2`.

## Dates, times, phones, addresses

| Type | Format | Example |
|---|---|---|
| Date | `dd/MM/yyyy` | `15/05/2026` |
| Date, long | `ngày D tháng M năm YYYY` | `ngày 15 tháng 5 năm 2026` |
| Time | 24-hour `HH:mm` | `14:30` |
| Phone, domestic | `0xxx xxx xxx` | `0912 345 678` |
| Phone, international | `+84` and drop the leading zero | `+84 912 345 678` |
| Hotline | grouped for memorability | `1900 1234` |
| Address | small → large | `Số 12, đường Nguyễn Huệ, phường Bến Nghé, Quận 1, TP. Hồ Chí Minh` |

Address order is the reverse of English and reliably wrong in machine output: house number →
street → ward → district → province/city. `TP.` abbreviates `Thành phố`; `Q.` abbreviates
`Quận`.

## Language tags

- `<html lang="vi">` — the standard document tag.
- `vi-VN` for `Intl` APIs and anywhere region-specific number and date formatting matters.
- Both are valid BCP-47. Do not invent `vn`, `vi_VN` (underscore), or `vi-VI`.

## URL slugs and SEO

Vietnamese slugs are **always unaccented, lowercase, hyphen-separated**, with stop words
removed. Characters allowed: `a-z`, `0-9`, `-`. Never underscores.

```text
"Căn hộ The Origami Quận 9"  →  /can-ho-the-origami-quan-9
"Bảng giá và chính sách bán hàng"  →  /bang-gia-chinh-sach-ban-hang
```

Stop words to drop: `và`, `của`, `những`, `một`, `các`, `với`, `cho`. Transliterate `đ` → `d`,
strip all diacritics, collapse whitespace to single hyphens. Changing a published slug
requires a 301 redirect.

**Dual-keyword rule:** Vietnamese users very frequently search *without* diacritics —
`chung cu quan 7`, `gia can ho vinhomes`. Body copy and headings carry the accented form;
make sure meta description, alt text, and internal anchor text cover the unaccented form too.
Never strip diacritics from visible body copy to chase this — it looks illiterate.

## Fonts and typography

Vietnamese stacks up to two marks on one vowel (`ế`, `ộ`, `ữ`, `Nguyễn`). Font choice is a
correctness issue, not a style one.

- **Prefer a font with a genuine Vietnamese subset.** `Be Vietnam Pro` is purpose-built.
  `Inter`, `Roboto`, `Open Sans`, `Nunito Sans`, and `Montserrat` ship usable Vietnamese.
- Google Fonts serves a `/* vietnamese */` `@font-face` with a `unicode-range` of roughly
  `U+0102-0103, U+0110-0111, U+0128-0129, U+0168-0169, U+01A0-01A1, U+01AF-01B0,
  U+1EA0-1EF9, U+20AB` — some faces add combining ranges `U+0300-0301, U+0303-0304,
  U+0308-0309, U+0323, U+0329`.
- **Verify glyph coverage.** Google's subset historically omitted `Ỳ ỳ Ỵ ỵ Ỷ ỷ Ỹ ỹ`
  (google/fonts issue #189). Run `scripts/check_font_coverage.py` against your copy.
- With `next/font/google`, request the `vietnamese` subset explicitly:
  `Be_Vietnam_Pro({ subsets: ['latin', 'vietnamese'] })`.
- **Line height:** stacked diacritics clip under tight leading. Keep `line-height` ≥ 1.4 for
  body and ≥ 1.2 for display sizes. Never set a fixed pixel height on a text container.
- **`text-transform: uppercase` is risky.** Confirm the font has uppercase glyphs carrying
  diacritics (`Đ`, `Ơ`, `Ư`, `Ế`, `Ỹ`). Many display faces do not, and marks silently vanish.
- **Length:** Vietnamese runs roughly comparable to English, but leave ~15–20% expansion
  headroom in buttons and nav — Hán-Việt compresses, thuần Việt expands.

## Unicode normalization

Vietnamese text can be encoded two ways:

- **NFC (precomposed):** `ế` is one codepoint, U+1EBF. **Always emit this.**
- **NFD (decomposed):** `ế` is U+0065 U+0302 U+0301. Renders with detached or misplaced marks
  in some fonts, breaks naive string length and regex, and sorts unpredictably.

Normalize on the way out: `text.normalize('NFC')` in JS, `unicodedata.normalize('NFC', s)` in
Python. Rule `NFC001` in `validate_copy.py` catches violations and `--fix` repairs them.

Collation, input methods, and the tone-mark convention rule live in `unicode-and-tone.md`.

## i18n files (next-intl / i18next)

Structure `vi.json` by page and section so a reviewer can scan register consistency in one
pass — `hero.title`, `cta.register`, `sections.overview.title`. Skills that ship a starter
file put it in their own `assets/` directory.

**Vietnamese has no grammatical plural.** In CLDR it has exactly one plural category:
`other`. ICU messages must therefore look like this:

```json
{ "unitCount": "{count, plural, other {# căn hộ}}" }
```

An `one {}` branch copied from the English file is always a bug — rule `ICU001` flags it.
Simple interpolation with a classifier is usually better than a plural block at all:
`"{count} căn hộ"`.

Other checks worth running on `vi.json`: missing keys versus `en.json`, placeholder mismatch
(`{name}` present in source but absent in target), values identical to the source string
(untranslated), and length overflow against UI constraints.
