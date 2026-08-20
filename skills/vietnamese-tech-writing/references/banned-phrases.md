<!-- vlc-disable: LAW001, CAL001, DIA001 -->

# Banned phrases — technical and product writing

Engineering writing sits almost entirely outside advertising law. The exceptions are the two
places where a product document becomes a marketing document: an **app-store listing** and any
**in-product claim** about the product itself. Both are advertising under Luật Quảng cáo, and
both are where LLM output reaches for a superlative.

The cross-cutting rules are in [compliance.md](compliance.md). This file adds what the
engineering and product genres get wrong specifically.

## Superlatives

Same statute, same test, same annotation as everywhere else in this repo — see
[compliance.md](compliance.md). An app-store subtitle claiming
`ứng dụng quản lý tài chính tốt nhất Việt Nam` is a regulated claim, not a tagline.

<!-- machine-readable: superlatives -->

| Pattern | Matches | Note |
|---|---|---|
| `(?:tốt\|nhanh\|mạnh\|an toàn\|thông minh\|dễ dùng\|dễ sử dụng\|tiện lợi\|tiện dụng\|hiện đại\|đầy đủ\|chính xác\|ổn định\|phổ biến)\s+nhất` | "the best / fastest / safest ..." | The core banned construction |
| `duy nhất` | "the only" | Named verbatim in the statute |
| `số\s*(?:một\|1)\b` | "number one" | Named verbatim in the statute |
| `hàng đầu` | "leading" | Wording of similar meaning |
| `(?<!#)#\s*1\b` | "#1" | Foreign equivalent; the lookbehind spares Markdown headings |
| `\bno\.?\s*1\b` | "No.1" | Foreign equivalent |

## Phrases that leak the internal vocabulary into the product

The single most common product-copy defect: shipping the term the team uses in Jira to the
person using the app.

<!-- machine-readable: calques -->

| ❌ Internal term in user-facing copy | ✅ What the user should read | Why |
|---|---|---|
| `trạng thái rỗng` | `Chưa có mục nào` | `empty state` is a design term, not a message |
| `người dùng cuối` | `bạn` | Nobody calls themselves an end user |
| `luồng onboarding` | `hướng dẫn bắt đầu` | Internal flow name leaking into the UI |
| `xử lý ngoại lệ` | `đã có lỗi xảy ra` | Implementation detail as an error message |
| `mã lỗi không xác định` | `đã có lỗi xảy ra, vui lòng thử lại` | Tells the user nothing actionable |
| `yêu cầu không hợp lệ` | `thông tin chưa đúng, vui lòng kiểm tra lại` | HTTP semantics as user copy |

## Error messages

Three rules, all of which LLM output breaks:

1. **Say what happened, then what to do.** `Đã có lỗi xảy ra. Vui lòng thử lại.` — not one
   without the other.
2. **Never `Quý khách` in a developer tool or a technical error.** The register for errors is
   `bạn`, or impersonal. `Kính thưa quý khách, đã có lỗi` is absurd in a CLI.
3. **Never blame the user.** `Bạn đã nhập sai` becomes `Thông tin chưa đúng`.

## Postmortems

Vietnamese workplace writing is more hierarchy-aware than English, which makes a blameless
postmortem harder to write and easier to get wrong. Name systems and events, never people —
`dịch vụ thanh toán timeout`, not `bạn Minh deploy nhầm`. Use the impersonal register
throughout (`eng-impersonal`); a postmortem that addresses anyone as `bạn` has already
stopped being blameless.
