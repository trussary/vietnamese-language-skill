<!-- vlc-disable: CAL001, DIA001, LAW001 -->

# Glossary — finance wording

The first table is machine-readable: `validate_copy.py` parses it, so every row is a lint
rule. The `Severity` column matters more here than in any other skill — a stale statutory term
is an `error`, while a merely unidiomatic rendering is a `warn`.

## Stale, calqued, and wrong-sense terms

<!-- machine-readable: glossary -->

| EN | ❌ Wrong or stale | ✅ Correct | Severity |
|---|---|---|---|
| balance sheet | `Bảng cân đối kế toán` | `Báo cáo tình hình tài chính` | error |
| personal income tax | `thuế thu nhập cá nhân (PIT)` | `thuế TNCN` | warn |
| deposit (bank) | `tiền ký gửi` | `tiền gửi` | error |
| deposit (sales) | `tiền gửi đặt trước` | `đặt cọc` | error |
| revenue | `thu nhập bán hàng` | `doanh thu` | error |
| net profit | `lợi nhuận ròng sạch` | `lợi nhuận sau thuế` | error |
| cash flow | `dòng chảy tiền mặt` | `lưu chuyển tiền tệ` | error |
| accounts receivable | `tài khoản phải thu` | `phải thu khách hàng` | error |
| accounts payable | `tài khoản phải trả` | `phải trả người bán` | error |
| retained earnings | `thu nhập giữ lại` | `lợi nhuận sau thuế chưa phân phối` | error |
| equity | `sự công bằng` | `vốn chủ sở hữu` | error |
| interest rate | `tỷ lệ quan tâm` | `lãi suất` | error |
| principal (of a loan) | `hiệu trưởng` | `tiền gốc` | error |
| security (financial) | `sự an toàn` | `chứng khoán` | error |
| bond | `trái phiếu liên kết` | `trái phiếu` | warn |
| return on investment | `sự trở lại của đầu tư` | `tỷ suất lợi nhuận` | error |
| fiscal year | `năm tài khóa tài chính` | `năm tài chính` | warn |
| audit | `kiểm tra sổ sách` | `kiểm toán` | error |
| invoice | `phiếu tính tiền` | `hóa đơn` | error |
| statement (bank) | `tuyên bố ngân hàng` | `sao kê` | error |
| overdue | `quá thời hạn cuối` | `quá hạn` | warn |
| installment | `phần trả góp` | `trả góp` | warn |
| disbursement | `sự giải ngân ra` | `giải ngân` | warn |
| collateral | `tài sản phụ` | `tài sản bảo đảm` | error |

`sự công bằng` for *equity*, `hiệu trưởng` for *principal*, `tỷ lệ quan tâm` for *interest
rate* and `sự an toàn` for *security* are the classic polysemy failures — each is a real
Vietnamese word for the **other** sense of the English term, so none of them looks misspelled.

## Guaranteed-return language

Prohibited phrasings, kept separate because they are a legal check rather than a wording
preference. See [financial-promotion.md](financial-promotion.md) for the instruments and for
why `FIN001` warns rather than blocks.

<!-- machine-readable: guaranteed-return -->

| Pattern | Matches | Note |
|---|---|---|
| `cam kết\s+(?:lợi nhuận\|lãi suất\|sinh lời\|hoàn vốn)` | "we guarantee a return" | Luật CK Đ12; NĐ 38/2018 Đ2 kh.4 |
| `đảm bảo\s+(?:lợi nhuận\|sinh lời\|lãi suất)` | "guaranteed profit" | Same |
| `bảo toàn vốn\s*(?:100\s*%)?` | "capital fully protected" | Same |
| `đầu tư không (?:có )?rủi ro` | "risk-free investment" | Same |
| `chắc chắn (?:sinh lời\|có lãi\|lãi)` | "certain to profit" | Same |
| `lợi nhuận\s+(?:cố định\|cam kết)` | "fixed / committed return" | Same |
| `không bao giờ (?:lỗ\|mất vốn)` | "you can never lose" | Same |
| `sinh lời chắc chắn` | "guaranteed to earn" | Same |

## Correct financial vocabulary

| EN | ✅ Vietnamese |
|---|---|
| Expected return | `Lợi nhuận kỳ vọng` |
| Historical performance | `Kết quả trong quá khứ` |
| Risk disclosure | `Công bố rủi ro` |
| Risk appetite | `Khẩu vị rủi ro` |
| Diversification | `Đa dạng hóa danh mục` |
| Portfolio | `Danh mục đầu tư` |
| Net asset value | `Giá trị tài sản ròng` |
| Management fee | `Phí quản lý` |
| Early-withdrawal fee | `Phí rút trước hạn` |
| Total cost | `Tổng chi phí` |
| Effective interest rate | `Lãi suất thực tế` |
| Credit limit | `Hạn mức tín dụng` |
| Repayment schedule | `Lịch trả nợ` |
| Insurance premium | `Phí bảo hiểm` |
| Sum insured | `Số tiền bảo hiểm` |
| Policyholder | `Bên mua bảo hiểm` |
| Investment-linked insurance | `Bảo hiểm liên kết đầu tư` |
| Digital asset | `Tài sản số` |
| Licensed provider | `Tổ chức được cấp phép` |
