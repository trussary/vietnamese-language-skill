<!-- vlc-disable: LAW001, CAL001, DIA001 -->

# Banned phrases

Two lists that fail for entirely different reasons. Calques are a **quality** problem: the
copy is legal but reads as machine output. Superlatives are a **legal** problem: the copy may
read fine and still draw a fine.

---

## 1. Calques — English syntax wearing Vietnamese words

These are the phrases that make a reader say "this was translated." The authoritative list is
the ❌ column of [glossary.md](glossary.md), which `validate_copy.py` loads directly. The
table below adds patterns that are not tied to a single UI string.

<!-- machine-readable: calques -->

| ❌ Calque | ✅ Use instead | Why |
|---|---|---|
| `được thiết kế bởi` | `do ... thiết kế` | Direct calque of the English passive "designed by" |
| `được xây dựng bởi` | `do ... xây dựng` | Same passive-agent calque |
| `được phát triển bởi` | `do ... phát triển` | Same passive-agent calque |
| `được tạo ra bởi` | `do ... tạo ra` | Same passive-agent calque |
| `chúng tôi cung cấp những` | `chúng tôi mang đến` | Literal "we provide the" — stiff and rare in native copy |
| `đừng bỏ lỡ cơ hội này` | `cơ hội có hạn` | Word-for-word "don't miss this opportunity" |
| `hãy liên lạc với chúng tôi` | `liên hệ ngay` | `liên lạc` is contact-as-communication, not contact-as-enquiry |
| `chào mừng đến với trang web của chúng tôi` | (delete it) | Dead 1990s English boilerplate, translated |
| `nhấp vào đây` | `xem chi tiết` | "Click here" — poor UX and poor Vietnamese |
| `tìm hiểu nhiều hơn` | `tìm hiểu thêm` | `nhiều hơn` translates comparative "more", wrong sense |
| `chúng ta cung cấp` | `chúng tôi cung cấp` | Inclusive `chúng ta` where exclusive `chúng tôi` is meant |
| `giải pháp một cửa` | `giải pháp trọn gói` | Calque of "one-stop solution" |
| `dịch vụ khách hàng 24/7 tốt` | `hỗ trợ 24/7` | Adjective stacking imported from English |
| `trong thời gian thực` | `theo thời gian thực` | Wrong preposition on "in real time" |
| `cao cấp căn hộ` | `căn hộ cao cấp` | English adjective-before-noun order |
| `hiện đại căn hộ` | `căn hộ hiện đại` | English adjective-before-noun order |
| `mới dự án` | `dự án mới` | English adjective-before-noun order |
| `đẹp vị trí` | `vị trí đẹp` | English adjective-before-noun order |

Adding a row here or in `glossary.md` adds a lint rule — no Python change needed.

---

## 2. Superlatives — regulated advertising claims

### The rule

**Luật Quảng cáo số 16/2012/QH13, Điều 8, khoản 11** prohibits advertising that uses:

> `nhất`, `duy nhất`, `tốt nhất`, `số một` — or wording of similar meaning — without lawful
> documentation proving it, per Bộ Văn hóa, Thể thao và Du lịch requirements.

This covers foreign-language equivalents (`No.1`, `Best`, `#1`) on Vietnamese-market pages.
Penalties are set by **Nghị định 87/2026/NĐ-CP, Điều 50 khoản 2** (effective 15/5/2026,
superseding NĐ 38/2021): **10–20 million VND for individuals, doubled to 20–40 million VND
for organisations**. Thông tư 12/2026/TT-BVHTTDL (effective 5/7/2026) clarifies what counts
as proof.

### This is enforced, currently, at scale

Under Luật Cạnh tranh 2018 (điểm a khoản 5 Điều 45), the Ủy ban Cạnh tranh Quốc gia has
issued **200 million VND** fines for exactly this:

| Company | Claim | Decision |
|---|---|---|
| Công ty TNHH Thương hiệu Vàng Washima | `Washima - Thương hiệu ghế massage số 1 Việt Nam` | 22/7/2026 |
| Cosmos Japan Creation | `Trim Ion - sự lựa chọn số 1 của người dùng Việt` | QĐ 175/QĐ-CT, 22/6/2026 |
| Lotte (Kid A+) | superlative product claim | QĐ 178/QĐ-CT, 24/6/2026 |

Also prohibited: **direct comparative advertising** naming a competitor, and using a person's
image, name, or words without their consent.

### Flag, do not hard-block

The law does not forbid these words. It forbids them **without proof**. Valid proof is a
market survey by a licensed research firm, or an award certificate — **valid for one year**.

`validate_copy.py` rule `LAW001` is therefore a **warning, never an error**. Annotate a
proven claim rather than deleting it:

```markdown
Thương hiệu ghế massage số 1 Việt Nam <!-- proof: Khảo sát Nielsen VN 2026, chứng chỉ 123/NS -->
```

The annotation must sit on the same line, or the line immediately above, and should name the
actual document. It suppresses the warning; it does not create the proof.

### Patterns

<!-- machine-readable: superlatives -->

| Pattern | Matches | Note |
|---|---|---|
| `(?:tốt\|hay\|đẹp\|rẻ\|lớn\|to\|nhanh\|mạnh\|cao\|sang\|xịn\|uy tín\|chất lượng\|hiện đại\|cao cấp\|sang trọng\|tiện nghi\|đẳng cấp\|hoàn hảo\|tuyệt vời\|an toàn\|thông minh\|bền)\s+nhất` | "the best / cheapest / fastest ..." | The core banned construction |
| `duy nhất` | "the only" | Named verbatim in the statute |
| `số\s*(?:một\|1)\b` | "number one" | Named verbatim in the statute |
| `hàng đầu` | "leading / top" | "Wording of similar meaning" — treat as covered |
| `đứng đầu` | "ranks first" | Same |
| `vô địch` | "unbeatable" | Same |
| `không ai sánh bằng` | "second to none" | Same |
| `top\s*1\b` | "top 1" | Common Vietnamese-market phrasing |
| `\bno\.?\s*1\b` | "No.1" | Foreign equivalent, explicitly covered |
| `(?<!#)#\s*1\b` | "#1" | Foreign equivalent. The lookbehind spares Markdown headings — `## 1.` is not a superlative claim |
| `\bnumber\s+one\b` | "number one" | Foreign equivalent |
| `\bbest\s+in\b` | "best in ..." | Foreign equivalent |

### Safe alternatives

| ❌ Unproven superlative | ✅ Provable or aspirational |
|---|---|
| `Căn hộ tốt nhất thị trường` | `Không gian sống đẳng cấp giữa lòng thành phố` |
| `Nền tảng nhanh nhất` | `Nhanh hơn 3 lần so với quy trình thủ công` |
| `Thương hiệu số 1 Việt Nam` | `Được hơn 10.000 khách hàng tin dùng` |
| `Vị trí đẹp nhất Quận 7` | `Vị trí trung tâm, kết nối 3 tuyến đường huyết mạch` |
| `Dịch vụ hàng đầu` | `Dịch vụ đạt chứng nhận ISO 9001` |

The pattern: replace the ranking claim with a **countable fact** or an **aspirational noun
phrase**. Both are stronger copy anyway.
