<!-- vlc-disable: all -->
<!-- GENERATED FILE — do not edit by hand.
     Source: evals/vietnamese-tech-writing/pairs.jsonl. Regenerate with: python tools/build_examples.py -->

# Examples — bad to good

The highest-value file in this skill. Each pair names the failure mode it fixes; the
diagnosis generalizes further than the string does. Read this before writing anything
long in Vietnamese.

Every ❌ string here is a deliberate defect, so this file is exempt from its own linter.

**28 pairs.** Contributions welcome — see [CONTRIBUTING.md](../../../CONTRIBUTING.md).

## Register

### error message: Something went wrong

❌ **Kính thưa quý khách, đã có lỗi xảy ra.**

✅ **Đã có lỗi xảy ra. Vui lòng thử lại.**

`quý khách` is a commercial register and reads as parody in a developer-facing surface. Errors say what happened, then what to do.

<sub>id: `eng-error-quy-khach` · caught by: `PRO002`</sub>

### Allow notifications?

❌ **Kính thưa Quý khách, cho phép gửi thông báo?**

✅ **Cho phép ứng dụng gửi thông báo cho bạn?**

In-app permission prompts are short and `bạn`. The formal commercial register reads absurd inside a mobile app.

<sub>id: `prd-permission-prompt` · caught by: `PRO002`</sub>

### README: you need Node 20

❌ **Cần cài đặt Node 20 trước khi tiếp tục.**

✅ **Bạn cần cài đặt Node 20 trước khi tiếp tục.**

The inverse defect. A README written impersonally reads like a standards document; getting-started guides take `bạn`.

<sub>id: `eng-readme-impersonal` · caught by: _not machine-detectable_</sub>

### code review: extract this into a function

❌ **Bạn viết hàm này dài quá, bạn nên tách ra.**

✅ **Chỗ này nên tách ra một hàm riêng.**

Native Vietnamese code review addresses the change, not the person. Naming the author in a criticism carries more weight than the English equivalent.

<sub>id: `eng-code-review-address` · caught by: _not machine-detectable_</sub>

## Structured localization files

### 1 file changed / 5 files changed

❌ **{"fileCount": "{count, plural, one {# tệp} other {# tệp}}"}**

✅ **{"fileCount": "{count, plural, other {# tệp}}"}**

Vietnamese has one CLDR plural category. Any `one`/`few`/`many`/`zero` branch in a vi file is a copy-paste from en.json.

<sub>id: `eng-icu-plural` · caught by: `ICU001`</sub>

### i18n key for the sign-in title

❌ **"đăngNhập.tiêuĐề": "Đăng nhập"**

✅ **"auth.signIn.title": "Đăng nhập"**

Keys are ASCII, values are Vietnamese. Non-ASCII keys break tooling and make NFC/NFD bugs unfindable.

<sub>id: `eng-identifier-ascii` · caught by: `ENG001`</sub>

## Engineering documentation

### commit your changes

❌ **cam kết các thay đổi**

✅ **commit các thay đổi**

`cam kết` means *to pledge*. Git's `commit` stays English in Vietnamese engineering writing — this is the single sharpest machine-translation tell.

<sub>id: `eng-commit-cam-ket` · caught by: `CAL001`</sub>

### deploy to production

❌ **triển khai đến sản xuất**

✅ **deploy lên production**

Environment names are never translated. `sản xuất` is manufacturing, not a deployment target.

<sub>id: `eng-deploy-production` · caught by: `CAL001`</sub>

### branch name for an add-login feature

❌ **feat/thêm-đăng-nhập**

✅ **feat/add-login**

Branch names must be ASCII. Diacritics break case-insensitive filesystems and tooling, and NFC/NFD makes two identical-looking names different strings.

<sub>id: `eng-branch-diacritics` · caught by: `ENG001`</sub>

### commit subject: fix login validation

❌ **sửa lỗi xác thực đăng nhập**

✅ **fix: login validation**

The commit subject is ASCII; the commit body may be Vietnamese. Tooling reads the subject.

<sub>id: `eng-commit-subject-diacritics` · caught by: `ENG001`</sub>

### RFC: the system will retry the request

❌ **Bạn sẽ thử lại request khi gặp lỗi.**

✅ **Hệ thống sẽ tự động retry request khi gặp lỗi.**

An RFC describes a system, not a reader. `bạn` here is a translation artefact of English's unavoidable "you".

<sub>id: `eng-rfc-ban` · caught by: `ENG003`</sub>

### postmortem: the payment service timed out

❌ **Bạn đã deploy nhầm khiến dịch vụ thanh toán timeout.**

✅ **Dịch vụ thanh toán timeout sau khi cấu hình mới được áp dụng.**

A postmortem that addresses anyone has stopped being blameless. Name systems and events, never people.

<sub>id: `eng-postmortem-ban` · caught by: `ENG003`</sub>

### Fix the bug in the cache

❌ **Sửa con bọ trong bộ nhớ đệm**

✅ **Fix bug ở cache**

`con bọ` is a joke, never written seriously. `bộ nhớ đệm` is correct in a published spec but reads like a textbook in a PR.

<sub>id: `eng-bug-cache` · caught by: `CAL001`</sub>

### the message queue is backed up

❌ **hàng đợi thông điệp đang bị tắc**

✅ **message queue đang bị tắc**

Over-translation. Vietnamese engineers say `message queue`; the calque appears only in machine output.

<sub>id: `eng-message-queue` · caught by: `CAL001`</sub>

### Run the migration before restarting

❌ **Bạn nên chạy migration trước khi restart.**

✅ **Chạy migration trước khi restart.**

Runbook steps are bare imperatives. `bạn nên` makes a required step look optional to someone reading it at 3am.

<sub>id: `eng-runbook-imperative` · caught by: `ENG007`</sub>

### open a pull request

❌ **mở một yêu cầu kéo**

✅ **mở pull request**

`yêu cầu kéo` is a dictionary rendering nobody uses. `pull request` or `PR` is universal.

<sub>id: `eng-pull-request` · caught by: `CAL001`</sub>

### Something went wrong

❌ **Cái gì đó đã đi sai**

✅ **Đã có lỗi xảy ra**

Word-for-word rendering of an English idiom. The settled Vietnamese string exists.

<sub>id: `eng-something-wrong` · caught by: `CAL001`</sub>

### Refresh the page

❌ **Làm tươi trang**

✅ **Tải lại trang**

`làm tươi` is a literal reading of *refresh* in its food sense.

<sub>id: `eng-refresh-page` · caught by: `CAL001`</sub>

## Product and research writing

### Add it to the sprint backlog

❌ **Thêm vào tồn đọng chạy nước rút**

✅ **Thêm vào sprint backlog**

Agile vocabulary stays English in Vietnamese product teams. `chạy nước rút` is a footrace.

<sub>id: `prd-sprint-backlog` · caught by: `CAL001`</sub>

### Do you agree the app is easy to use?

❌ **Bạn có đồng ý rằng ứng dụng dễ sử dụng không?**

✅ **Mức độ dễ sử dụng của ứng dụng? (Rất khó – Rất dễ)**

Acquiescence bias inflates agreement by ~10 points (Krosnick). An item-specific scale gives agreement nowhere to attach.

<sub>id: `prd-agree-scale` · caught by: `PROD002`</sub>

### Onboarding roadmap

❌ **Bản đồ đường lên tàu**

✅ **Lộ trình onboarding**

`bản đồ đường` and `lên tàu` are both literal renderings of metaphors that do not carry into Vietnamese.

<sub>id: `prd-roadmap-onboarding` · caught by: `CAL001`</sub>

### As a user, I want to reset my password

❌ **Như một người dùng, tôi muốn đặt lại mật khẩu**

✅ **Là người dùng, tôi muốn đặt lại mật khẩu**

`Như một` is a calque of "as a" in its comparative sense. The user-story convention is `Là`.

<sub>id: `prd-user-story` · caught by: `CAL001`</sub>

### We fixed bugs and improved speed

❌ **Chúng tôi đã sửa những con bọ**

✅ **Đã sửa một số lỗi và cải thiện tốc độ.**

Release notes are past-tense and benefit-led. `con bọ` is jokey; user-facing text says `lỗi`.

<sub>id: `prd-release-notes` · caught by: `CAL001`</sub>

### Empty state: no items yet

❌ **Trạng thái trống**

✅ **Chưa có mục nào. Nhấn + để thêm.**

`empty state` is a design term. Shipping it as the message tells the user nothing and reveals the internal vocabulary.

<sub>id: `prd-empty-state` · caught by: `CAL001`</sub>

### App Store subtitle

❌ **Ứng dụng quản lý tài chính cá nhân đơn giản và tiện lợi nhất hiện nay**

✅ **Quản lý tài chính cá nhân**

Over the 30-character subtitle limit, and `tiện lợi nhất` is a regulated superlative under Luật Quảng cáo Điều 8 khoản 11.

<sub>id: `prd-app-store-subtitle` · caught by: `PROD003`, `LAW001`</sub>

### We collect your data to improve the service

❌ **Bạn đồng ý cho ứng dụng thu thập dữ liệu.**

✅ **Bạn đồng ý cho ứng dụng thu thập dữ liệu nhằm mục đích cải thiện chất lượng dịch vụ.**

Nghị định 13/2023/NĐ-CP requires consent that names its purpose. Consent to nothing in particular is not consent.

<sub>id: `prd-consent-purpose` · caught by: `PROD004`</sub>

### How likely are you to recommend us?

❌ **Bạn có giới thiệu chúng tôi cho bạn bè không? (Có / Không)**

✅ **Khả năng bạn giới thiệu ứng dụng cho bạn bè hoặc đồng nghiệp? (0 – 10)**

NPS is a 0–10 scale. Collapsing it to yes/no destroys the metric it exists to produce.

<sub>id: `prd-nps-scale` · caught by: _not machine-detectable_</sub>

### align with stakeholders

❌ **thống nhất với những người nắm giữ cổ phần**

✅ **thống nhất với stakeholder**

`người nắm giữ cổ phần` means shareholder. The product sense stays English.

<sub>id: `eng-stakeholder` · caught by: `CAL001`</sub>
