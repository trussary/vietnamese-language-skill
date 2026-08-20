<!-- vlc-disable: all -->
<!-- GENERATED FILE — do not edit by hand.
     Source: evals/vietnamese-business-comms/pairs.jsonl. Regenerate with: python tools/build_examples.py -->

# Examples — bad to good

The highest-value file in this skill. Each pair names the failure mode it fixes; the
diagnosis generalizes further than the string does. Read this before writing anything
long in Vietnamese.

Every ❌ string here is a deliberate defect, so this file is exempt from its own linter.

**28 pairs.** Contributions welcome — see [CONTRIBUTING.md](../../../CONTRIBUTING.md).

## Calqued CTAs and UI strings

### Learn more

❌ **Học thêm**

✅ **Xem ngay**

`Học thêm` means *take extra classes*. In e-commerce the converting CTA is `Xem ngay` or `Mua ngay`, not a translation of the English button.

<sub>id: `mkt-cta-hoc-them` · caught by: `CAL001`</sub>

### Limited time offer

❌ **Lời đề nghị giới hạn thời gian**

✅ **Ưu đãi có hạn**

`Lời đề nghị` is a formal proposal, not a commercial offer. The standard formula exists and is three words shorter.

<sub>id: `mkt-limited-offer` · caught by: `CAL001`</sub>

### Subscribe to our newsletter

❌ **Đăng ký thuê bao bản tin của chúng tôi**

✅ **Đăng ký nhận tin**

`thuê bao` is a telecoms subscription. The wrong sense of a polysemous English word.

<sub>id: `mkt-subscribe` · caught by: `CAL001`</sub>

### Welcome to our website

❌ **Chào mừng đến với trang web của chúng tôi**

✅ **Giải pháp quản lý kho cho chuỗi bán lẻ**

Dead English boilerplate, translated. It occupies the most valuable line on the page and says nothing.

<sub>id: `mkt-welcome-website` · caught by: `CAL001`</sub>

## Regulated advertising claims and legal copy

### 90% off everything

❌ **Giảm giá 90% toàn bộ sản phẩm**

✅ **Giảm đến 50% toàn bộ sản phẩm**

Exceeds the 50% ceiling in NĐ 81/2018 as amended by NĐ 128/2024. Above 50% requires a registered chương trình khuyến mại tập trung.

<sub>id: `mkt-discount-ceiling` · caught by: `MKT002`</sub>

### Our best-selling product

❌ **Sản phẩm bán chạy nhất thị trường**

✅ **Sản phẩm bán chạy**

A sales-rank claim is exactly what the statute regulates. Dropping `nhất` keeps the copy and removes the claim.

<sub>id: `mkt-best-seller` · caught by: `LAW001`</sub>

### Bulk SMS campaign body

❌ **ABC giảm 30% toàn bộ sản phẩm đến hết 30/08. Đặt ngay tại abc.vn**

✅ **ABC giảm 30% toàn bộ sản phẩm đến hết 30/08. Đặt tại abc.vn. Từ chối nhận tin: soạn TC gửi 8888**

Nghị định 91/2020 Điều 13 requires a working refusal mechanism in every advertising message. A footer nobody can act on does not count.

<sub>id: `mkt-bulk-optout` · caught by: `SPAM001`</sub>

### 30% cheaper than [Competitor]

❌ **Rẻ hơn đối thủ 30%**

✅ **Rẻ hơn 30% so với giá niêm yết trước đây**

Comparative advertising against a named competitor is prohibited, and enforcement is current. Compare against your own baseline instead.

<sub>id: `mkt-comparative` · caught by: _not machine-detectable_</sub>

### Cures joint pain in 7 days

❌ **Hết đau xương khớp sau 7 ngày, cam kết khỏi 100%**

✅ **Thực phẩm bổ sung canxi và vitamin D3**

A therapeutic claim on a supplement. Restricted regardless of approval, and the outcome guarantee compounds it. Describe the product, not the outcome.

<sub>id: `mkt-health-claim` · caught by: _not machine-detectable_</sub>

## Register

### Press release: we've launched a new product

❌ **Bọn mình vừa ra mắt sản phẩm mới nè!**

✅ **Công ty Cổ phần ABC trân trọng thông báo ra mắt sản phẩm mới.**

A press release is institutional third person. `bọn mình` is a social caption wearing a press release's clothes.

<sub>id: `mkt-press-register` · caught by: `PRO002`</sub>

### Livestream: only 20 left

❌ **Kính thưa Quý vị, số lượng sản phẩm còn lại là 20.**

✅ **Cả nhà ơi, mã này chỉ còn 20 suất thôi nha!**

Livestream is the one genre where spoken plural address is correct. The written formal register reads stiff and kills the format.

<sub>id: `mkt-livestream` · caught by: `PRO002`</sub>

## Marketing and campaign copy

### The best coffee in Vietnam

❌ **Cà phê số 1 Việt Nam**

✅ **Cà phê được hơn 10.000 khách hàng lựa chọn mỗi ngày**

`số 1` is a ranking claim, prohibited without documentary proof under Luật Quảng cáo Điều 8 khoản 11. The fix is a countable fact, which is stronger copy anyway.

<sub>id: `mkt-so-1` · caught by: `LAW001`</sub>

### Free shipping nationwide

❌ **Giao hàng miễn phí trên toàn quốc**

✅ **Freeship toàn quốc**

Not wrong, just weak. `Freeship` is the naturalized loanword the market uses; the formal rendering reads like a policy page.

<sub>id: `mkt-freeship` · caught by: `CAL001`</sub>

### Order confirmation with a promo appended

❌ **Đơn hàng đã xác nhận. Ưu đãi giảm 50% hôm nay, đặt ngay!**

✅ **Đơn hàng của Quý khách đã được xác nhận. Dự kiến giao trước 20/08.**

Marketing content under a transactional Zalo tag gets the whole template rejected at review. Promotions need their own template and their own opt-in.

<sub>id: `mkt-zns-promo` · caught by: `ZNS001`</sub>

### SALE UP TO 70%

❌ **SALE SỐC GIẢM 70% DUY NHẤT HÔM NAY**

✅ **Sale đến 50% – số lượng có hạn**

Three defects at once: ALL-CAPS, a `duy nhất` superlative, and a discount over the 50% ceiling.

<sub>id: `mkt-caps-superlative` · caught by: `LAW001`, `MKT002`</sub>

### Product title: Nike running shoes, men's

❌ **GIÀY NIKE 🔥🔥 CHÍNH HÃNG SALE SỐC**

✅ **Giày thể thao nam Nike Air Zoom chính hãng - đế êm**

ALL-CAPS lowers search ranking and emoji in a title read as a clone listing. The conventional order is product type, brand, model, then features.

<sub>id: `mkt-title-emoji` · caught by: `MKT001`</sub>

### An over-long Zalo template

❌ **Kính chào Quý khách, Công ty Cổ phần Thương mại và Dịch vụ ABC xin trân trọng thông báo tới Quý khách về chương trình chăm sóc khách hàng thân thiết được triển khai trong tháng 8 năm 2026 trên toàn bộ hệ thống cửa hàng của chúng tôi tại khu vực Thành phố Hồ Chí Minh, Hà Nội, Đà Nẵng, Cần Thơ và Hải Phòng, áp dụng cho tất cả các sản phẩm thuộc ngành hàng gia dụng, điện tử, thời trang và mỹ phẩm, với nhiều phần quà hấp dẫn dành riêng cho Quý khách hàng đã đồng hành cùng chúng tôi trong suốt thời gian vừa qua, xin Quý khách vui lòng liên hệ tổng đài để biết thêm chi tiết.**

✅ **Kính chào Quý khách. Chương trình chăm sóc khách hàng thân thiết tháng 8 đã bắt đầu. Xem chi tiết tại abc.vn hoặc liên hệ 1900 1234.**

Zalo caps the body at 400 characters có dấu. Detail belongs on a landing page behind the CTA, not inside the template.

<sub>id: `mkt-zns-length` · caught by: `ZNS002`</sub>

## Sales and B2B outreach

### Hi, I'd like to send you our quote

❌ **Chào bạn, mình muốn gửi bạn báo giá của công ty mình.**

✅ **Kính gửi anh/chị, em xin phép gửi anh/chị báo giá của bên em.**

`bạn`/`mình` in B2B outreach is the clearest tell of an automated send. `anh/chị` for them, `em` for a plausibly junior sender.

<sub>id: `sal-ban-outreach` · caught by: `SALES001`</sub>

### Please find our quotation attached

❌ **Vui lòng xem trích dẫn đính kèm**

✅ **Anh/chị vui lòng xem báo giá đính kèm**

`trích dẫn` is a citation. Asking a customer to review your citation is a different email entirely.

<sub>id: `sal-trich-dan` · caught by: `CAL001`</sub>

### I'll follow up next week

❌ **Em sẽ theo lên vào tuần sau**

✅ **Em sẽ liên hệ lại với anh/chị vào tuần sau**

`theo lên` is a morpheme-by-morpheme rendering of *follow up* that means nothing in Vietnamese.

<sub>id: `sal-theo-len` · caught by: `CAL001`</sub>

### Best regards

❌ **Lời chào tốt nhất**

✅ **Trân trọng**

`Best regards` run through a dictionary. The Vietnamese business closing is a fixed form.

<sub>id: `sal-best-regards` · caught by: `CAL001`</sub>

### Price list

❌ **Bảng giá dịch vụ tháng 8**

✅ **Bảng giá dịch vụ tháng 8 (đã bao gồm thuế GTGT). Báo giá có hiệu lực đến 30/09/2026.**

A quote that states neither VAT treatment nor a validity date gets renegotiated later. Both are conventional and expected.

<sub>id: `sal-bao-gia-vat` · caught by: `SALES004`</sub>

### Dear Sir, buy now!

❌ **Sản phẩm của bên em đang giảm 20%, anh mua ngay đi ạ!**

✅ **Kính gửi anh Minh, em là Lan từ Công ty ABC. Em được biết bên anh đang mở rộng hệ thống bán lẻ. Em xin phép gửi anh tài liệu tóm tắt về giải pháp quản lý kho.**

A first line that goes straight to the pitch reads abrupt to the point of rudeness in Vietnamese B2B. The courtesy line is not padding.

<sub>id: `sal-no-greeting` · caught by: `SALES003`</sub>

### Payment reminder

❌ **Bạn phải thanh toán ngay lập tức.**

✅ **Kính đề nghị Quý khách thanh toán khoản 35.000.000 ₫ trước ngày 30/08/2026. Trân trọng.**

Firmness in Vietnamese dunning comes from a named date and a named amount, not from tone. The imperative to a `bạn` ends the relationship rather than accelerating payment.

<sub>id: `sal-dunning-tone` · caught by: `SALES001`</sub>

### Happy Lunar New Year

❌ **Chúc mừng năm mới bạn nhé!**

✅ **Kính chúc Quý khách và gia đình một năm mới An khang – Thịnh vượng.**

A B2B Tết greeting uses the formulaic well-wishes. The casual version is a message to a friend, not to an account.

<sub>id: `sal-tet-greeting` · caught by: `SALES001`</sub>

### A deposit is required

❌ **Yêu cầu tiền gửi trước khi triển khai**

✅ **Quý khách vui lòng đặt cọc trước khi triển khai**

`tiền gửi` is a bank deposit. A sales deposit is `đặt cọc`, and the imperative softens to `vui lòng`.

<sub>id: `sal-deposit` · caught by: `CAL001`</sub>

### See the attached price list

❌ **Xem danh sách giá đính kèm**

✅ **Anh/chị xem bảng giá đính kèm giúp em**

`danh sách giá` is a literal compound. The artifact has a name: `bảng giá`.

<sub>id: `sal-price-list` · caught by: `CAL001`</sub>

### I hope this email finds you well

❌ **Hy vọng email này tìm thấy bạn khỏe mạnh**

✅ **Kính gửi anh/chị, chúc anh/chị một tuần làm việc hiệu quả**

A word-for-word rendering of an English formula that has no Vietnamese counterpart. It reads as a template nobody edited.

<sub>id: `mkt-hope-this-finds` · caught by: `CAL001`</sub>
