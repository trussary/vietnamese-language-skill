<!-- vlc-disable: LAW001, CAL001, DIA001 -->

# Banned phrases — finance

Everything here is a legal check. Nothing on this page is a matter of taste, and nothing on it
should be edited around without a lawyer.

Instruments and reasoning: [financial-promotion.md](financial-promotion.md). Cross-cutting
rules shared with the other skills: [compliance.md](compliance.md).

## Superlatives

Luật Quảng cáo 16/2012/QH13 Điều 8 khoản 11 — prohibited without documentary proof. Finance
breaks this constantly, because a rate or a rank is the easiest thing to boast about and the
easiest to check.

<!-- machine-readable: superlatives -->

| Pattern | Matches | Note |
|---|---|---|
| `(?:tốt\|cao\|thấp\|nhanh\|an toàn\|uy tín\|lớn\|sinh lời\|hiệu quả\|minh bạch)\s+nhất` | "highest rate / safest / most reputable" | `lãi suất cao nhất` is the standard case |
| `duy nhất` | "the only" | Named verbatim in the statute |
| `số\s*(?:một\|1)\b` | "number one" | Named verbatim in the statute |
| `hàng đầu` | "leading" | Wording of similar meaning |
| `đứng đầu` | "ranks first" | Same |
| `(?<!#)#\s*1\b` | "#1" | Foreign equivalent; the lookbehind spares Markdown headings |
| `\bno\.?\s*1\b` | "No.1" | Foreign equivalent |

The rewrite is always the same: **publish the number.** `Lãi suất từ 5,8%/năm` is more
persuasive than `lãi suất tốt nhất` and is not a regulated claim.

## Phrases that are never permissible in financial promotion

<!-- machine-readable: calques -->

| ❌ Phrase | ✅ Use instead | Why |
|---|---|---|
| `lợi nhuận khủng` | `lợi nhuận kỳ vọng` | Sensational framing of a return |
| `x2 tài khoản` | `lợi nhuận kỳ vọng` | An outcome promise dressed as a slogan |
| `làm giàu không khó` | `(bỏ hẳn)` | Classic solicitation framing, and false |
| `tiền đẻ ra tiền` | `(bỏ hẳn)` | Same |
| `cơ hội đổi đời` | `(bỏ hẳn)` | Same |
| `ai cũng có thể đầu tư` | `sản phẩm phù hợp với nhà đầu tư có khẩu vị rủi ro` | Suitability is a regulated concept |
| `không cần kiến thức vẫn có lãi` | `(bỏ hẳn)` | Solicitation to an unsuitable investor |
| `vốn ít lời nhiều` | `(bỏ hẳn)` | Return promise |
| `rút vốn bất cứ lúc nào không mất phí` | `phí rút trước hạn: [x]` | Almost always false; state the fee |
| `bảo hiểm sinh lời` | `bảo hiểm liên kết đầu tư` | Sells an insurance product as an investment |
| `gửi tiết kiệm lãi cao hơn ngân hàng` | `(bỏ hẳn)` | Implies a deposit product that is not one |
| `sàn quốc tế uy tín` | `tổ chức được Bộ Tài chính cấp phép` | Offshore solicitation is outside the pilot |

## Words that must never be softened

The opposite failure: copy that removes a required warning because it dampens the pitch.

| Must appear | Where |
|---|---|
| `Đầu tư có rủi ro` | Any investment solicitation |
| `Kết quả trong quá khứ không đảm bảo kết quả trong tương lai` | Any performance figure |
| `Sản phẩm bảo hiểm liên kết đầu tư` | Any investment-linked insurance material |
| `Kết quả đầu tư không được đảm bảo và do bên mua bảo hiểm chịu rủi ro` | Same |
| `Tài sản số không phải là phương tiện thanh toán hợp pháp` | Any digital-asset copy |
| Total cost, fees, and effective rate | Any `lãi suất 0%` or promotional-rate claim |

Whether these are **present and complete** is a human check — `FIN008` and `FIN009` on the QA
checklist.

## Register

`bạn` does not appear in a statement, a disclosure, an invoice, or a loan document. The
register floor is `Quý khách` or impersonal third person. Youth-facing fintech may use `bạn`
in the app shell, but the money screens and every regulated disclosure revert to formal.
