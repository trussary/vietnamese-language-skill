<!-- vlc-disable: CAL001, DIA001, LAW001 -->

# Glossary — marketing and sales wording

The first table is machine-readable: `validate_copy.py` parses it, so every row is a lint
rule. The optional `Severity` column overrides the default — `error` for a rendering no
Vietnamese marketer or seller would write, `warn` for one that is merely weak or
context-dependent.

## Calques and wrong-sense renderings

<!-- machine-readable: glossary -->

| EN | ❌ Calque | ✅ Native | Severity |
|---|---|---|---|
| quote (a price) | `trích dẫn` | `báo giá` | warn |
| price list | `danh sách giá` | `bảng giá` | error |
| follow up | `theo lên` | `theo dõi` | error |
| best regards | `lời chào tốt nhất` | `trân trọng` | error |
| deposit (sales) | `tiền gửi trước` | `đặt cọc` | error |
| limited offer | `lời đề nghị giới hạn` | `ưu đãi có hạn` | error |
| subscribe to our newsletter | `đăng ký thuê bao bản tin` | `đăng ký nhận tin` | error |
| free shipping | `giao hàng miễn phí` | `freeship` | warn |
| flash sale | `bán chớp nhoáng` | `flash sale` | error |
| best seller | `người bán tốt nhất` | `bán chạy` | error |
| learn more (CTA) | `học thêm` | `xem ngay` | error |
| click here | `nhấp vào đây` | `xem chi tiết` | error |
| call to action | `cuộc gọi hành động` | `nút kêu gọi hành động` | error |
| landing (a deal) | `hạ cánh hợp đồng` | `chốt hợp đồng` | error |
| reach out | `vươn ra` | `liên hệ` | error |
| touch base | `chạm căn cứ` | `trao đổi nhanh` | error |
| pain point | `điểm đau` | `vấn đề đang gặp` | warn |
| we provide the best | `chúng tôi cung cấp những` | `chúng tôi mang đến` | warn |
| don't miss this opportunity | `đừng bỏ lỡ cơ hội này` | `cơ hội có hạn` | warn |
| contact us today | `liên lạc chúng tôi ngay hôm nay` | `liên hệ ngay để nhận tư vấn` | error |
| dear customer | `khách hàng thân yêu` | `kính gửi quý khách` | error |
| welcome to our website | `chào mừng đến với trang web của chúng tôi` | `(bỏ hẳn câu này)` | error |
| VAT invoice | `hóa đơn thuế giá trị` | `hóa đơn GTGT` | error |

`trích dẫn` and `theo lên` are the two sharpest. `trích dẫn` means *citation* — asking a
customer to review your citation is a different email entirely. `theo lên` is a
morpheme-by-morpheme rendering of *follow up* that means nothing in Vietnamese.

`trích dẫn` is a **warning**, not an error, because it is a perfectly good word in its own
sense. In a document that genuinely discusses citations, suppress it per line.

## E-commerce and promotional vocabulary

Conventional, not calqued. Use these rather than inventing a translation.

| EN | ✅ Vietnamese | Register |
|---|---|---|
| Free shipping | `Freeship` / `Miễn phí vận chuyển` | e-comm / formal |
| Flash sale | `Flash Sale` / `Săn sale` | e-comm |
| Deal | `Deal hời` / `Ưu đãi` | e-comm |
| Voucher | `Voucher` / `Mã giảm giá` | e-comm |
| Limited offer | `Ưu đãi có hạn` / `Số lượng có hạn` | all |
| Best seller | `Bán chạy` | e-comm |
| Buy now | `Mua ngay` | e-comm |
| Add to cart | `Thêm vào giỏ` | e-comm |
| Order now | `Đặt ngay` | e-comm |
| See details | `Xem chi tiết` | all |
| Register for a consultation | `Đăng ký tư vấn` | services |
| Genuine / authentic | `Chính hãng` | e-comm |
| Pre-order | `Đặt trước` | e-comm |
| Out of stock | `Hết hàng` | e-comm |
| Combo | `Combo` | e-comm |
| Installment | `Trả góp` | retail / finance |

`Freeship` is a naturalized loanword and is what the market actually says. `Giao hàng miễn
phí` is not wrong, just weaker and more formal.

## Sales artifacts

| EN | ✅ Vietnamese |
|---|---|
| Quote / quotation | `Báo giá` |
| Price list | `Bảng giá` |
| Proposal | `Đề xuất` / `Proposal` |
| Statement of work | `Phạm vi công việc` |
| Framework agreement | `Hợp đồng nguyên tắc` |
| Acceptance record | `Biên bản nghiệm thu` |
| Deposit | `Đặt cọc` / `Tạm ứng` |
| Payment terms | `Điều khoản thanh toán` |
| Validity period | `Hiệu lực báo giá` |
| VAT included | `Đã bao gồm thuế GTGT` |
| VAT excluded | `Chưa bao gồm thuế GTGT` |
| Tax code | `MST` |
| Purchase order | `Đơn đặt hàng` |
| Invoice | `Hóa đơn` |

Deep invoice and statement terminology belongs to `vietnamese-finance-copy`; the rows here are
only what a seller writes on a quote.

## CTAs by register

| Register | CTA |
|---|---|
| E-commerce, `bạn` | `Mua ngay`, `Đặt ngay`, `Săn deal`, `Xem ngay` |
| SaaS, `bạn` | `Dùng thử miễn phí`, `Bắt đầu ngay`, `Đăng ký nhận tin` |
| Services, `anh/chị` | `Đăng ký tư vấn`, `Nhận báo giá`, `Liên hệ ngay` |
| Real estate, `quý khách` | `Đăng ký nhận bảng giá`, `Đặt lịch tham quan` |

`Tìm hiểu thêm` is correct but overused — in e-commerce, `Xem ngay` and `Mua ngay` are what
converts. `Học thêm` means *take extra classes* and is never a CTA.
