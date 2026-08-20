<!-- vlc-disable: CAL001, DIA001 -->

# Glossary — engineering and product terms

Two tables. The first is machine-readable: `validate_copy.py` parses it, so every row is a
lint rule and adding a row needs no code change. The second is guidance the linter cannot
enforce.

An optional `Severity` column overrides the default. Use `error` for a calque no native
engineer would ever write, `warn` for one that is merely unidiomatic or context-dependent.

## Calques that mark machine translation

<!-- machine-readable: glossary -->

| EN | ❌ Calque | ✅ Native usage | Severity |
|---|---|---|---|
| commit | `cam kết` | `commit` | warn |
| deploy to production | `triển khai đến sản xuất` | `deploy lên production` | error |
| deploy to staging | `triển khai đến dàn dựng` | `deploy lên staging` | error |
| merge | `hợp nhất nhánh` | `merge` | error |
| bug | `con bọ` | `bug` | warn |
| message queue | `hàng đợi thông điệp` | `message queue` | error |
| sprint | `chạy nước rút` | `sprint` | error |
| backlog | `tồn đọng` | `backlog` | warn |
| roadmap | `bản đồ đường` | `lộ trình` | error |
| onboarding | `lên tàu` | `onboarding` | warn |
| empty state | `trạng thái trống` | `màn hình trống` | error |
| as a user | `như một người dùng` | `là người dùng` | error |
| pull request | `yêu cầu kéo` | `pull request` | error |
| rollback | `cuộn lại` | `rollback` | warn |
| hotfix | `sửa nóng` | `hotfix` | warn |
| endpoint | `điểm cuối` | `endpoint` | warn |
| timeout | `hết giờ` | `timeout` | warn |
| deadline | `hạn chót cuối cùng` | `deadline` | warn |
| stakeholder | `người nắm giữ cổ phần` | `stakeholder` | error |
| user story | `câu chuyện người dùng` | `user story` | error |
| release notes | `ghi chú phát hành` | `release notes` | warn |
| dark mode | `chế độ tối tăm` | `chế độ tối` | error |
| log in | `đăng nhập vào trong` | `đăng nhập` | error |
| sign out | `ký ra` | `đăng xuất` | error |
| refresh the page | `làm tươi trang` | `tải lại trang` | error |
| something went wrong | `cái gì đó đã đi sai` | `đã có lỗi xảy ra` | error |

## User-facing product strings

These are the strings a user reads. They get translated, and there are settled conventions —
do not invent new ones.

| EN | ✅ Vietnamese |
|---|---|
| Try again | `Thử lại` |
| Loading… | `Đang tải…` |
| Saving… | `Đang lưu…` |
| Saved | `Đã lưu` |
| Delete | `Xoá` |
| Cancel | `Huỷ` |
| Confirm | `Xác nhận` |
| Settings | `Cài đặt` |
| Sign in | `Đăng nhập` |
| Sign up | `Đăng ký` |
| Sign out | `Đăng xuất` |
| Forgot password | `Quên mật khẩu` |
| Search | `Tìm kiếm` |
| No results | `Không có kết quả` |
| Nothing here yet | `Chưa có gì ở đây` |
| Copy link | `Sao chép liên kết` |
| Download | `Tải xuống` |
| Upload | `Tải lên` |
| Permission required | `Cần cấp quyền` |
| Allow | `Cho phép` |
| Not now | `Để sau` |
| Learn more | `Tìm hiểu thêm` |
| What's new | `Có gì mới` |
| Fixed | `Đã sửa` |
| Improved | `Đã cải thiện` |
| Added | `Đã thêm` |

`Xoá`/`Huỷ` are written kiểu mới here to match the repo default. `Xóa`/`Hủy` are equally
correct — just do not mix the two styles inside one product.
