<!-- vlc-disable: LAW001, DIA001 -->

# QA checklist — human review rubric

The validator catches mechanical defects. Idiomaticity, register fit, and persuasiveness need
a human — ideally a native speaker. Score each dimension 1–5; anything below 4 blocks
publication.

## 1. Register appropriateness

- [ ] The pronoun matches the audience (see [register-guide.md](register-guide.md)).
- [ ] **One** register throughout — hero, body, FAQ, form, and footer agree.
- [ ] Self-reference is `chúng tôi`, not `chúng ta`, unless the reader is genuinely included.
- [ ] Hán-Việt density matches the vertical: heavy for luxury/RE, light for SaaS.
- [ ] No direct address using `khách hàng`.

## 2. Idiomaticity — does it read as written, not translated?

The test: read it aloud. Translationese is fluent but rhythmically wrong.

- [ ] No English word order — modifiers follow nouns.
- [ ] No `được ... bởi ...` passive-agent constructions.
- [ ] Sentence length matches the register: RE tolerates long ornate clauses, SaaS does not.
- [ ] Idioms are Vietnamese idioms, not translated English ones.
- [ ] Classifiers are present and correct (`căn`, `lô`, `nền`, `tòa`).
- [ ] No orphaned English loanwords where a settled Vietnamese term exists.

## 3. CTA conventionality

- [ ] Every CTA appears in [glossary.md](glossary.md) or is a deliberate, justified variant.
- [ ] Real-estate lead CTAs are specific (`Đăng ký nhận báo giá`), not generic (`Gửi`).
- [ ] Button text fits without wrapping at 375px width.
- [ ] Section headings use the standardized Vietnamese labels.

## 4. Legal safety

- [ ] No unproven superlative anywhere, including alt text, meta description, and image files.
- [ ] Any proven superlative carries a `<!-- proof: ... -->` annotation naming the document.
- [ ] No named-competitor comparison.
- [ ] Lead form has an unticked consent checkbox with a stated purpose.
- [ ] `Chính sách bảo mật` link resolves to a real page.
- [ ] Renders carry `Hình ảnh mang tính chất minh hoạ`.
- [ ] Sector-specific mandatory disclaimers present (see [legal-copy.md](legal-copy.md)).

## 5. Formatting correctness

- [ ] All text is NFC — `validate_copy.py` exits clean.
- [ ] One tone-mark style throughout.
- [ ] Currency groups with `.`, decimals with `,`; headline prices use `tỷ`/`triệu`.
- [ ] Dates `dd/MM/yyyy`, times 24-hour.
- [ ] Phone numbers `0xxx xxx xxx` or `+84`.
- [ ] Addresses run small-to-large.
- [ ] Slugs unaccented, lowercase, hyphenated, no stop words.
- [ ] `<html lang="vi">` set.
- [ ] `vi.json` has no `one {}` plural branches.

## 6. Rendering

- [ ] Font carries the full Vietnamese subset — `check_font_coverage.py` clean.
- [ ] Stacked diacritics are not clipped at any breakpoint (test `Nguyễn`, `Quỹ`, `Ữ`).
- [ ] Uppercase styling preserves `Đ Ơ Ư Ế Ỹ`.
- [ ] No layout break from 15–20% text expansion.

## Reviewer sign-off

| Dimension | Score | Reviewer | Notes |
|---|---|---|---|
| Register | | | |
| Idiomaticity | | | |
| CTA conventionality | | | |
| Legal safety | | | |
| Formatting | | | |
| Rendering | | | |

A native Vietnamese speaker must sign off on register and idiomaticity. The other four can be
reviewed by anyone following this checklist.
