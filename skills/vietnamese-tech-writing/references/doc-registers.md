<!-- vlc-disable: TONE001, DIA001 -->

# Document registers — where `bạn` is wrong

The landing-page default is inverted here, and this is the delta most worth reading.

Marketing copy addresses a reader. Most engineering documents do not. An RFC, a design doc,
and a postmortem describe a **system**, and Vietnamese has natural impersonal constructions
for exactly that. Reaching for `bạn` in those documents is the tell that the text was
translated from English, where "you" is unavoidable.

The full matrix is in [register-matrix.md](register-matrix.md). This file says which document
gets which row.

## Which register for which document

| Document | Register | Addresses the reader as |
|---|---|---|
| RFC, design doc, architecture note | `eng-impersonal` | nothing — the system is the subject |
| Postmortem | `eng-impersonal` | nothing; name systems, never people |
| Runbook, operational procedure | `eng-impersonal` | nothing — imperative verbs |
| Internal spec, PRD | `eng-impersonal` | nothing |
| README, tutorial, getting-started | `eng-readme` | `bạn` |
| API reference | `eng-readme` | `bạn`, sparingly |
| UI microcopy, error messages | `eng-readme` | `bạn` |
| Release notes, changelog | `eng-readme` | `bạn`, or no address at all |
| Help-centre article | `eng-readme` | `bạn` |
| Status page (customer-facing) | `re` or `formal` | `quý khách` — this one is not an engineering document |
| User-interview script | varies by participant | `anh/chị` for older participants, `bạn` for peers |

Status pages are the exception worth remembering: the audience is customers, not engineers,
so the customer-facing register applies even though an SRE writes it.

## Impersonal constructions

These are what replaces `bạn` in a specification. All of them are ordinary Vietnamese.

| Instead of | Write |
|---|---|
| `Bạn sẽ thấy một lỗi` | `Hệ thống sẽ trả về lỗi` |
| `Bạn cần cấu hình biến môi trường` | `Cần cấu hình biến môi trường` |
| `Bạn có thể gọi endpoint này` | `Endpoint này có thể được gọi` |
| `Chúng ta sẽ retry request` | `Request sẽ được retry tự động` |
| `Bạn nên chạy migration trước` | `Chạy migration trước` |

The subject is `hệ thống`, `dịch vụ`, `request`, `job` — or there is no subject at all, which
Vietnamese permits far more comfortably than English.

## Runbooks take the imperative

A runbook is a list of commands to execute under pressure. Every step is a bare imperative
verb, with no hedging and no address:

```
❌  Bạn nên kiểm tra log của service trước khi restart.
✅  Kiểm tra log của service trước khi restart.

❌  Bạn có thể chạy lệnh sau để rollback.
✅  Chạy lệnh sau để rollback:
```

`bạn nên` in a runbook is worse than merely unidiomatic: it makes a required step look
optional to someone reading it at 3am.

## READMEs and tutorials take `bạn`

The inverse holds just as firmly. A README written impersonally reads like a standards
document and stops being welcoming:

```
❌  Cần cài đặt Node 20 trước khi tiếp tục.        (in a getting-started guide)
✅  Bạn cần cài đặt Node 20 trước khi tiếp tục.
```

## Never `quý khách` in a developer-facing surface

`Quý khách` is a commercial register. In a CLI, an SDK error, or a developer dashboard it
reads as parody. Errors are `bạn` or impersonal:

```
❌  Kính thưa quý khách, đã có lỗi xảy ra.
✅  Đã có lỗi xảy ra. Vui lòng thử lại.
```

## Pronouns in code review

Peer register: `mình` for self, `bạn` for the author — or, more commonly and more safely,
neither. Native Vietnamese code review addresses the **change**, not the person:

```
Chỗ này nên tách ra một hàm riêng.
Có thể dùng map thay cho vòng lặp ở đây không?
```

That is not evasive; it is how the register works. Naming the author in a criticism carries
more weight in Vietnamese than the English equivalent does, and hierarchy makes it heavier
still when the reviewer is senior.
