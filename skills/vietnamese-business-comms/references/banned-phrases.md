<!-- vlc-disable: LAW001, CAL001, DIA001 -->

# Banned phrases — campaigns and outbound

Two lists, failing for different reasons. Superlatives are a **legal** problem: the copy reads
fine and still draws a fine. Everything else here is a **credibility** problem: the copy is
legal and reads as a mass mailing.

Citations are in [compliance.md](compliance.md) and [promo-law.md](promo-law.md).

## Superlatives — regulated advertising claims

Luật Quảng cáo 16/2012/QH13, Điều 8 khoản 11. Prohibited **without documentary proof**, which
is why `LAW001` warns rather than blocks and why `<!-- proof: ... -->` suppresses it.

<!-- machine-readable: superlatives -->

| Pattern | Matches | Note |
|---|---|---|
| `(?:tốt\|hay\|đẹp\|rẻ\|lớn\|to\|nhanh\|mạnh\|cao\|sang\|xịn\|uy tín\|chất lượng\|hiện đại\|cao cấp\|sang trọng\|đẳng cấp\|hoàn hảo\|tuyệt vời\|an toàn\|bền\|bán chạy\|yêu thích\|nổi tiếng)\s+nhất` | "the best / cheapest / best-selling ..." | The core banned construction; `bán chạy nhất` is the campaign-specific case |
| `duy nhất` | "the only" | Named verbatim in the statute |
| `số\s*(?:một\|1)\b` | "number one" | Named verbatim in the statute |
| `hàng đầu` | "leading" | Wording of similar meaning |
| `đứng đầu` | "ranks first" | Same |
| `vô địch` | "unbeatable" | Same |
| `không ai sánh bằng` | "second to none" | Same |
| `top\s*1\b` | "top 1" | Common Vietnamese-market phrasing |
| `\bno\.?\s*1\b` | "No.1" | Foreign equivalent |
| `(?<!#)#\s*1\b` | "#1" | Foreign equivalent; the lookbehind spares Markdown headings |
| `\bnumber\s+one\b` | "number one" | Foreign equivalent |
| `\bbest\s+seller\b` | "best seller" | Foreign equivalent of a ranking claim |

## Phrases that mark a mass mailing

<!-- machine-readable: calques -->

| ❌ Phrase | ✅ Use instead | Why |
|---|---|---|
| `kính gửi quý khách hàng thân mến` | `kính gửi anh/chị` | Two registers stacked; reads as a template nobody edited |
| `chúng tôi rất vui mừng thông báo` | `công ty xin thông báo` | Translated press-release filler |
| `hy vọng email này tìm thấy bạn` | `(bỏ hẳn câu này)` | Word-for-word "hope this email finds you well" |
| `theo như email trước của tôi` | `như em đã trao đổi` | Calque of "per my last email", and the wrong register |
| `vui lòng xem xét đề nghị của chúng tôi` | `anh/chị xem giúp em đề xuất đính kèm` | Stiff and impersonal for Vietnamese B2B |
| `chúng tôi là công ty hàng đầu` | `công ty chúng tôi hoạt động trong lĩnh vực` | Unproven ranking claim as a self-introduction |
| `cơ hội có một không hai` | `số lượng có hạn` | Overheated; reads as a scam |
| `mua ngay kẻo lỡ` | `số lượng có hạn` | Aggressive urgency that Vietnamese e-commerce has moved past |
| `giá rẻ bất ngờ` | `giá ưu đãi` | Reads as a low-trust listing |
| `cam kết hoàn tiền 100% nếu không hiệu quả` | `chính sách đổi trả trong 7 ngày` | An outcome guarantee, and for a health or finance product a regulated claim |
| `bạn phải thanh toán ngay` | `kính đề nghị quý khách thanh toán trước ngày` | Rude in dunning; ends the relationship rather than accelerating payment |
| `chào bạn, mình muốn gửi bạn báo giá` | `kính gửi anh/chị, em xin gửi báo giá` | `bạn`/`mình` in B2B outreach is an instant tell of automation |

## Health and outcome claims

Never in ordinary campaign copy, regardless of product category:

`chữa khỏi`, `điều trị tận gốc`, `khỏi bệnh sau 7 ngày`, `không tác dụng phụ`,
`thay thế thuốc chữa bệnh`, `cam kết khỏi 100%`.

These require sector pre-approval when they are permitted at all, and a supplement is not a
medicine. The rewrite is to describe the product, not the outcome:
`hỗ trợ bổ sung vitamin D` rather than `giúp hết đau xương khớp`.

## Financial claims

`cam kết lợi nhuận`, `lãi suất 0%` without total-cost disclosure, `đầu tư không rủi ro` — all
regulated, and all belong to `vietnamese-finance-copy`. If campaign copy contains any of them,
route it there and to legal review rather than editing it here.

## Comparative advertising

Naming a competitor in a comparison is prohibited. So is using a person's image, name, or
words without consent — including a customer's testimonial photo.

```
❌  Rẻ hơn [Đối thủ] 30%
✅  Rẻ hơn 30% so với giá niêm yết trước đây
```
