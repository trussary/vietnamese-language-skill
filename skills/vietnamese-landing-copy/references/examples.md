<!-- vlc-disable: all -->
<!-- GENERATED FILE — do not edit by hand.
     Source: evals/pairs.jsonl. Regenerate with: python tools/build_examples.py -->

# Examples — bad to good

The highest-value file in this skill. Each pair names the failure mode it fixes; the
diagnosis generalizes further than the string does. Read this before writing anything
long in Vietnamese.

Every ❌ string here is a deliberate defect, so this file is exempt from its own linter.

**35 pairs.** Contributions welcome — see [CONTRIBUTING.md](../../../CONTRIBUTING.md).

## Calqued CTAs and UI strings

### Learn more about our project

❌ **Học thêm về dự án của chúng tôi**

✅ **Tìm hiểu thêm về dự án**

`Học thêm` is 'study more'. `Tìm hiểu` is the verb for finding out about something.

<sub>id: `cal-learn-more` · caught by: `CAL001`</sub>

### Sign up to receive information

❌ **Đăng ký lên để nhận thông tin**

✅ **Đăng ký nhận thông tin dự án**

The English particle 'up' has no Vietnamese counterpart; `đăng ký` is already complete.

<sub>id: `cal-sign-up` · caught by: `CAL001`</sub>

### Contact us today!

❌ **Liên lạc chúng tôi ngay hôm nay!**

✅ **Liên hệ ngay để nhận tư vấn**

`Liên lạc` means contact-as-communication (a radio link, a phone line). Enquiries use `liên hệ`.

<sub>id: `cal-contact-us` · caught by: `CAL001`</sub>

### See details

❌ **Nhìn chi tiết**

✅ **Xem chi tiết**

`Nhìn` is to look at something physically. Viewing a page or a listing is always `xem`.

<sub>id: `cal-see-details` · caught by: `CAL001`</sub>

### Testimonials

❌ **Lời chứng thực**

✅ **Cảm nhận khách hàng**

`Chứng thực` is notarial certification. Customer quotes are `cảm nhận` or `đánh giá`.

<sub>id: `cal-testimonials` · caught by: `CAL001`</sub>

### Trusted by 500 businesses

❌ **Tin tưởng bởi 500 doanh nghiệp**

✅ **Được 500 doanh nghiệp tin dùng**

The English passive-agent 'by' calqued as `bởi`; Vietnamese fronts the agent instead.

<sub>id: `cal-trusted-by` · caught by: `CAL001`</sub>

### Coming soon

❌ **Đến sớm**

✅ **Sắp mở bán**

`Đến sớm` means arriving early. Real estate says `sắp mở bán`; products say `sắp ra mắt`.

<sub>id: `cal-coming-soon` · caught by: `CAL001`</sub>

### Get started

❌ **Bắt đầu được**

✅ **Bắt đầu ngay**

`Được` here translates the English particle and lands as 'able to begin'.

<sub>id: `cal-get-started` · caught by: `CAL001`</sub>

### Click here to view pricing

❌ **Nhấp vào đây để xem bảng giá**

✅ **Xem bảng giá**

'Click here' is weak UX in any language and reads as translated boilerplate in Vietnamese.

<sub>id: `cal-click-here` · caught by: `CAL001`</sub>

### Privacy Policy

❌ **Chính sách riêng tư**

✅ **Chính sách bảo mật**

`Riêng tư` is privacy in the intimate sense; the legal term of art is `bảo mật`.

<sub>id: `cal-privacy` · caught by: `CAL001`</sub>

### Welcome to our website!

❌ **Chào mừng đến với trang web của chúng tôi!**

✅ **Kiến tạo chốn an cư đẳng cấp giữa lòng thành phố**

Translated 1990s English boilerplate. Vietnamese landing pages open with the value claim.

<sub>id: `cal-welcome` · caught by: `CAL001`</sub>

### A one-stop solution

❌ **Giải pháp một cửa**

✅ **Giải pháp trọn gói**

`Một cửa` is single-window government administration, not a product benefit.

<sub>id: `cal-one-stop` · caught by: `CAL001`</sub>

### Submit

❌ **Nộp**

✅ **Đăng ký nhận báo giá**

`Nộp` is filing paperwork with an authority. Name the outcome instead of the mechanic.

<sub>id: `cal-submit` · caught by: `CAL001`</sub>

## Passive-agent constructions

### Designed by leading architects

❌ **Được thiết kế bởi các kiến trúc sư hàng đầu**

✅ **Do đội ngũ kiến trúc sư danh tiếng kiến tạo**

`được ... bởi ...` imports the English passive wholesale; `hàng đầu` is also a regulated claim.

<sub>id: `pas-designed-by` · caught by: `CAL001`, `LAW001`</sub>

### Built by Company X

❌ **Được xây dựng bởi Công ty X**

✅ **Do Công ty X xây dựng**

Same passive-agent calque. `Do X + verb` is the natural Vietnamese frame.

<sub>id: `pas-built-by` · caught by: `CAL001`</sub>

## Grammar and pronouns

### We provide management software

❌ **Chúng ta cung cấp phần mềm quản lý**

✅ **Chúng tôi cung cấp phần mềm quản lý**

`Chúng ta` includes the reader. A company speaking about itself always uses `chúng tôi`.

<sub>id: `gra-chung-ta` · caught by: `CAL001`</sub>

## Word order

### Premium apartments with modern design

❌ **Cao cấp căn hộ với thiết kế hiện đại**

✅ **Căn hộ cao cấp với thiết kế hiện đại**

English puts adjectives before nouns; Vietnamese puts them after. The most frequent LLM error.

<sub>id: `gra-word-order` · caught by: `CAL001`</sub>

## Regulated advertising claims and legal copy

### We offer the best apartments on the market

❌ **Chúng tôi cung cấp những căn hộ tốt nhất số 1 thị trường**

✅ **Không gian sống đẳng cấp giữa lòng thành phố**

Unproven superlative, illegal under Luật Quảng cáo Điều 8 khoản 11. Replace with an aspirational noun phrase.

<sub>id: `law-best-market` · caught by: `LAW001`, `CAL001`</sub>

### Vietnam's No.1 massage chair brand

❌ **Thương hiệu ghế massage số 1 Việt Nam**

✅ **Thương hiệu ghế massage được hơn 50.000 gia đình Việt tin dùng**

This exact claim drew a 200 million VND fine in 2026. Swap the ranking for a countable fact.

<sub>id: `law-number-one` · caught by: `LAW001`</sub>

### Leading real estate developer

❌ **Chủ đầu tư hàng đầu Việt Nam**

✅ **Chủ đầu tư với 25 năm kinh nghiệm và 40 dự án đã bàn giao**

`Hàng đầu` is wording of similar meaning to the banned terms and needs the same proof.

<sub>id: `law-leading` · caught by: `LAW001`</sub>

### The only project with a rooftop pool

❌ **Dự án duy nhất có hồ bơi trên mái**

✅ **Dự án sở hữu hồ bơi vô cực trên tầng thượng**

`Duy nhất` is named verbatim in the statute. Describe the feature, do not rank it.

<sub>id: `law-only` · caught by: `LAW001`</sub>

### The fastest platform on the market

❌ **Nền tảng nhanh nhất thị trường**

✅ **Nhanh hơn 3 lần so với quy trình thủ công**

A measured comparison is both legal and more persuasive than a superlative.

<sub>id: `law-fastest` · caught by: `LAW001`</sub>

### Send us your information.

❌ **Gửi thông tin của bạn cho chúng tôi.**

✅ **Tôi đồng ý cho phép Công ty thu thập và xử lý thông tin cá nhân của tôi theo Chính sách bảo mật nhằm mục đích tư vấn sản phẩm/dịch vụ.**

Nghị định 13/2023/NĐ-CP requires an explicit, informed, revocable consent statement on every lead form.

<sub>id: `legal-no-consent` · caught by: _not machine-detectable_</sub>

### Artist's impression

❌ **Hình ảnh thực tế dự án**

✅ **Hình ảnh mang tính chất minh hoạ**

Labelling a render as an actual photo creates liability. Vietnamese pages carry this disclaimer by convention.

<sub>id: `legal-render-disclaimer` · caught by: _not machine-detectable_</sub>

## Locale formatting

### Price: 2,500,000,000 VND

❌ **Giá: 2,500,000,000 VND**

✅ **Giá chỉ từ 2,5 tỷ đồng**

Comma grouping is the US convention; Vietnamese groups with periods, and headline prices use the tỷ scale.

<sub>id: `num-full-price` · caught by: `NUM001`</sub>

### From 2.5 billion

❌ **Chỉ từ 2.5 tỷ**

✅ **Chỉ từ 2,5 tỷ**

The decimal separator in Vietnamese is a comma, not a period.

<sub>id: `num-decimal-dot` · caught by: `NUM003`</sub>

### 35,000,000 VND/m2

❌ **35,000,000 VND/m2**

✅ **35 triệu/m²**

Comma grouping plus ASCII `m2`; Vietnamese listings use the triệu scale and a real superscript.

<sub>id: `num-per-sqm` · caught by: `NUM001`, `NUM004`</sub>

### Launch date: 05/15/2026

❌ **Ngày mở bán: 05/15/2026**

✅ **Ngày mở bán: 15/05/2026**

Vietnamese dates are dd/MM/yyyy. A second field above 12 proves the US order was used.

<sub>id: `date-us-order` · caught by: `DATE001`</sub>

### Hotline: +84 0912 345 678

❌ **Hotline: +84 0912 345 678**

✅ **Hotline: +84 912 345 678**

The trunk zero is dropped after the +84 country code.

<sub>id: `phone-plus84-zero` · caught by: `PHONE001`</sub>

### 12 Nguyen Hue St, Ben Nghe Ward, District 1, Ho Chi Minh City

❌ **TP. Hồ Chí Minh, Quận 1, phường Bến Nghé, đường Nguyễn Huệ, số 12**

✅ **Số 12, đường Nguyễn Huệ, phường Bến Nghé, Quận 1, TP. Hồ Chí Minh**

Vietnamese addresses run small to large, the reverse of English. Not machine-detectable — learn the order.

<sub>id: `addr-order` · caught by: _not machine-detectable_</sub>

## Register

### Welcome! Sign up now for offers.

❌ **Kính chào quý khách! Bạn hãy đăng ký ngay để nhận ưu đãi nhé.**

✅ **Kính chào quý khách! Quý khách vui lòng đăng ký để nhận ưu đãi.**

Formal `quý khách` and casual `bạn` in one breath. Pick one register and hold it for the whole page.

<sub>id: `reg-mixed` · caught by: `PRO001`</sub>

### Start your free trial today

❌ **Quý khách hãy bắt đầu dùng thử miễn phí ngay hôm nay**

✅ **Dùng thử miễn phí ngay hôm nay**

`Quý khách` on a developer product reads stiff and salesy; SaaS uses `bạn` or no pronoun at all.

<sub>id: `reg-saas-too-formal` · caught by: `PRO002`</sub>

### Customers, please register

❌ **Khách hàng hãy đăng ký để nhận tư vấn**

✅ **Quý khách vui lòng đăng ký để nhận tư vấn**

`Khách hàng` is a third-person noun. Direct address takes `quý khách`. Not machine-detectable.

<sub>id: `reg-khach-hang-address` · caught by: _not machine-detectable_</sub>

## Structured localization files

### {count, plural, one {# apartment} other {# apartments}}

❌

```json
{
  "unitCount": "{count, plural, one {# căn hộ} other {# căn hộ}}"
}
```

✅

```json
{
  "unitCount": "{count, plural, other {# căn hộ}}"
}
```

Vietnamese has no grammatical plural — CLDR gives it only the `other` category.

<sub>id: `icu-one-branch` · caught by: `ICU001`</sub>

## Unicode encoding

### Register to receive project information

❌ **Đăng ký nhận thông tin dự án**

✅ **Đăng ký nhận thông tin dự án**

Decomposed (NFD) Vietnamese renders with detached marks in many web fonts and breaks string length. Always emit NFC.

<sub>id: `nfc-decomposed` · caught by: `NFC001`</sub>
