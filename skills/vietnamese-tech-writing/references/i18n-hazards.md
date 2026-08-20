<!-- vlc-disable: NUM001, NUM002, DIA001, CAL001, ICU001 -->

# i18n hazards specific to vi-VN

The number, date, and currency rules are in [locale-formatting.md](locale-formatting.md), and
the encoding rules are in [unicode-and-tone.md](unicode-and-tone.md). This file is the
engineering-side failure list: the things that break in a build rather than in a sentence.

## String expansion: budget 25–30%

English → Vietnamese text grows by roughly **25–30%**, and short UI labels grow by more —
`Save` is four characters, `Lưu` is three, but `Cancel` (6) becomes `Huỷ bỏ` (6) and
`Settings` (8) becomes `Cài đặt` (7) while `Sign out` (8) becomes `Đăng xuất` (9) and
`Forgot password?` (16) becomes `Quên mật khẩu?` (14). Long strings expand reliably; short
ones are unpredictable in both directions.

Consequences to design for:

- **No fixed-width buttons or tabs.** Anything sized to fit the English string will truncate.
- **Two-line headings.** A hero headline that fits on one line in English usually does not.
- **Table column widths** need to be content-driven, not hard-coded.
- **Character-limited surfaces** (app-store title, push notification, SMS) must be counted in
  Vietnamese, not estimated from English.

## Diacritics count against character limits

A diacritic is part of the letter, not an extra glyph — `ế` is one character. But:

- In **NFD**, it is three codepoints, so a naive `.length` check rejects valid copy. Normalize
  to NFC before counting. See [unicode-and-tone.md](unicode-and-tone.md).
- In **SMS**, any Vietnamese diacritic forces UCS-2 encoding, cutting the segment size from
  160 characters to **70**. A message that fits in one segment in English may take three in
  Vietnamese, at three times the cost.
- In **app-store metadata**, the limit is characters, so diacritics are free — but the
  expansion above still applies.

## Plurals: `other` only

Vietnamese has no grammatical plural. In CLDR it has exactly one plural category.

```json
✅  { "fileCount": "{count, plural, other {# tệp}}" }
❌  { "fileCount": "{count, plural, one {# tệp} other {# tệp}}" }
```

An `one`, `few`, `many`, `zero` or `two` branch in a `vi` file is always a bug — usually a
copy-paste from `en.json` that a translator filled in twice. Rule `ICU001` flags every
non-`other` CLDR category.

Explicit-value selectors are different and are legitimately useful:

```json
✅  { "fileCount": "{count, plural, =0 {Chưa có tệp nào} other {# tệp}}" }
```

## Collation and search

Covered in [unicode-and-tone.md](unicode-and-tone.md), but the engineering consequence is
worth stating plainly: **users type without diacritics.** A search box that only matches
`cà phê` when the user types `cà phê` is broken for most of its users. Use a locale-aware
accent-insensitive collation, or index a normalized unaccented form alongside the display
form.

Sorting is the same problem: `đ` belongs between `d` and `e`, and a byte sort puts it after
`z`.

## Locale tags

- Use **`vi-VN`** wherever region formatting matters (currency, dates, number grouping).
- **`vi`** is fine for language-only negotiation and for content that carries no formatting.
- There is no meaningful `vi-US` or regional split to support. North/South differences are
  lexical, not locale-level, and no platform models them.

## Fonts

Vietnamese stacks two marks on one letter (`ề`, `ộ`, `ữ`). A web-font subset generated from
Latin-1 or "Latin Extended" will silently drop them, and the browser falls back per glyph —
producing a headline where three characters are visibly a different typeface.

Check coverage before shipping:

```bash
python scripts/check_font_coverage.py path/to/copy.md
```

Also verify the line-height. Stacked diacritics need more vertical space than Latin text, and
a tight `line-height` clips them at the top of the line box.

## Input

Accept both **Telex** (`aa` → `â`, `dd` → `đ`) and **VNI** (`a6` → `â`, `d9` → `đ`). Do not
intercept keystrokes in a way that fights the IME, do not strip diacritics on input, and do
not normalize a user's name to ASCII on save. `Nguyễn` is the name.

## Identifiers stay ASCII

Keys, filenames, branch names, and commit subjects are ASCII. Values are Vietnamese. See
[code-switching.md](code-switching.md).

```json
✅  { "auth.signIn.title": "Đăng nhập" }
❌  { "xácThực.đăngNhập.tiêuĐề": "Đăng nhập" }
```
