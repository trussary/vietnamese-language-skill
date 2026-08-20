# Glossary — EN → VI conventional wording

Vietnamese UI and marketing strings have settled conventions. Translating them fresh from
English produces calques that native readers instantly clock as machine output. Look the
string up here first.

**Format contract:** the tables below are parsed at runtime by `scripts/validate_copy.py`.
The ❌ column is the calque blocklist and the ✅ column is the suggested fix — adding a row
here is all it takes to add a lint rule. Keep every Vietnamese cell wrapped in backticks,
one phrase per cell, and use `—` when there is no known bad form. Separate alternative good
answers with ` / `.

## CTAs and UI strings

<!-- machine-readable: glossary -->

| EN | ❌ Calque | ✅ Native | Register |
|---|---|---|---|
| Get started | `Bắt đầu được` | `Bắt đầu ngay` / `Dùng thử ngay` | saas |
| Learn more | `Học thêm` | `Tìm hiểu thêm` / `Xem thêm` | universal |
| See details | `Nhìn chi tiết` | `Xem chi tiết` | universal |
| Read more | `Đọc nhiều hơn` | `Đọc tiếp` / `Xem thêm` | universal |
| Sign up | `Ký lên` | `Đăng ký` | universal |
| Sign up | `Đăng ký lên` | `Đăng ký` | universal |
| Register now | `Đăng ký bây giờ` | `Đăng ký ngay` | universal |
| Book a demo | `Đặt một demo` | `Đặt lịch demo` / `Đăng ký trải nghiệm` | saas |
| Contact us | `Liên lạc chúng tôi` | `Liên hệ` / `Liên hệ với chúng tôi` | universal |
| Get a quote | `Lấy báo giá` | `Nhận báo giá` / `Nhận bảng giá` | re |
| Explore | — | `Khám phá` | universal |
| Coming soon | `Đến sớm` | `Sắp ra mắt` / `Sắp mở bán` | universal |
| Trusted by | `Tin tưởng bởi` | `Được tin dùng bởi` / `Đối tác của chúng tôi` | universal |
| Testimonials | `Lời chứng thực` | `Cảm nhận khách hàng` / `Đánh giá của khách hàng` | universal |
| FAQ | `Câu hỏi hỏi thường` | `Câu hỏi thường gặp` | universal |
| Terms & Conditions | — | `Điều khoản & Điều kiện` / `Điều khoản sử dụng` | legal |
| Privacy Policy | `Chính sách riêng tư` | `Chính sách bảo mật` | legal |
| Submit | `Nộp` | `Gửi` / `Gửi thông tin` | universal |
| Send | `Gửi đi` | `Gửi` | universal |
| Loading | — | `Đang tải...` | universal |
| Limited offer | `Ưu đãi giới hạn` | `Ưu đãi có hạn` / `Số lượng có hạn` | universal |
| Free trial | — | `Dùng thử miễn phí` | saas |
| Pricing | `Định giá` | `Bảng giá` / `Chi phí` | universal |
| Features | — | `Tính năng` | saas |
| About us | — | `Về chúng tôi` / `Giới thiệu` | universal |
| Our services | — | `Dịch vụ của chúng tôi` | universal |
| Download brochure | `Tải xuống tài liệu quảng cáo` | `Tải brochure` / `Tải tài liệu dự án` | re |
| Get directions | `Lấy chỉ đường` | `Xem đường đi` / `Chỉ đường` | universal |
| Subscribe | `Đăng ký thuê bao` | `Đăng ký nhận tin` | universal |
| Log in | `Đăng nhập vào` | `Đăng nhập` | universal |
| Back to top | `Trở lại đỉnh` | `Về đầu trang` | universal |
| Share | `Chia sẻ ra` | `Chia sẻ` | universal |
| Search | `Tìm kiếm ra` | `Tìm kiếm` | universal |
| Required field | `Trường bắt buộc` | `Vui lòng nhập thông tin` / `Bắt buộc` | universal |
| Thank you | `Cảm ơn bạn nhiều` | `Cảm ơn quý khách` / `Cảm ơn bạn` | universal |

Note: rows with `—` in the ❌ column carry no blocklist entry. Either the literal
translation is already correct, or the plausible bad form is a substring of ordinary
Vietnamese (`tính chất` means "nature, property") or of the recommended phrase itself
(`thử miễn phí` sits inside `dùng thử miễn phí`). Blocklisting those would fire on correct
copy, which is worse than not catching the error — see CONTRIBUTING.md.

## Real-estate section labels

These are near-universal across Vietnamese project landing pages. Deviating from them makes
a page read as a foreign import. Use them verbatim as section headings.

| EN | ✅ Vietnamese | Notes |
|---|---|---|
| Project overview | `Tổng quan dự án` | Always the first section |
| Highlights | `Điểm nổi bật` | Optional, follows overview |
| Location | `Vị trí` / `Vị trí & Liên kết vùng` | The longer form when regional links matter |
| Amenities | `Tiện ích` | Split `tiện ích nội khu` / `tiện ích ngoại khu` |
| Floor plans | `Mặt bằng` | Often a downloadable PDF |
| Model unit design | `Thiết kế căn hộ mẫu` | |
| Construction progress | `Tiến độ` / `Tiến độ xây dựng` | |
| Sales policy | `Chính sách bán hàng` / `Chính sách & Ưu đãi` | |
| Developer | `Chủ đầu tư` | |
| Legal status | `Pháp lý` | Buyers look for this specifically |
| Lead form | `Đăng ký nhận thông tin` / `Đăng ký nhận tư vấn` | |

Recommended narrative order: tổng quan → điểm nổi bật → vị trí → tiện ích → mặt bằng →
pháp lý → chính sách ưu đãi → form đăng ký.

## Real-estate lead CTAs

Seen on live Vietnamese project pages. Prefer these over generic `Đăng ký`.

| Intent | ✅ Vietnamese |
|---|---|
| Request pricing | `Đăng ký nhận báo giá` |
| Reserve a unit | `Đăng ký giữ chỗ` |
| Book a showroom visit | `Đặt lịch xem nhà mẫu` |
| Request project info | `Nhận thông tin dự án` |
| Request promotions | `Đăng ký nhận ưu đãi` |
| Request a callback | `Đăng ký nhận tư vấn` |

## Form field labels

| EN | ✅ Vietnamese |
|---|---|
| Full name | `Họ và tên` |
| Phone number | `Số điện thoại` |
| Email address | `Địa chỉ email` / `Email` |
| Message | `Nội dung` / `Lời nhắn` |
| Interested unit type | `Loại căn quan tâm` |
| Budget | `Ngân sách dự kiến` |
| How did you hear about us | `Bạn biết đến chúng tôi qua đâu` |
