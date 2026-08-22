<!-- vlc-disable: TONE001, DIA001 -->

# Document registers — teacher, student, and parent

The pronoun in Vietnamese school writing is set by **schooling stage and relationship**, not
by the writer's house style and not by the student's actual age. Getting the wrong one is not
a tone problem — it reads as a different kind of institution.

The full matrix is in [register-matrix.md](register-matrix.md). This file says which document
gets which row, and why.

## Which register for which document

| Document | Register | Addresses the reader as |
|---|---|---|
| Report-card remark, feedback, in-class message — secondary (THCS/THPT) | `edu-k12` | `em` |
| Report-card remark, feedback — primary (tiểu học) | `edu-k12-primary` | `con` |
| Sổ liên lạc entry, Zalo broadcast, disciplinary/absence notice — to parents | `edu-parent` | `quý phụ huynh` |
| University syllabus, transcript, registration notice, admin announcement | `edu-uni` | nothing direct — third-person `sinh viên` |
| One-to-one message, a known parent already established as `anh/chị` | `edu-parent` with a channel override | `anh/chị` (the one parent, not the collective) |

`bạn` addressed to a student in a teacher's voice is the loudest machine-translation tell in
this domain:

```
❌  Bạn cần hoàn thành bài tập về nhà.
✅  Em cần hoàn thành bài tập về nhà.               (secondary)
✅  Con cần hoàn thành bài tập về nhà nhé.           (primary)
```

## The primary/secondary line is drawn at schooling stage, not age

A 22-year-old teaching first grade still writes `con`. A 24-year-old teaching 12th grade
still writes `em`. This is not a self-deprecation scale the way it is in sales — it is fixed by
which school the student attends.

## Teacher self-reference

A teacher refers to themselves as `thầy` or `cô`, never `tôi` or `mình`, when addressing a
student directly:

```
❌  Tôi rất vui vì em đã tiến bộ.
✅  Thầy/Cô rất vui vì em đã tiến bộ.
```

`tôi` is correct in impersonal, third-person administrative prose (a university notice, a
circular) — never in a direct message to a student.

## `quý phụ huynh` does not soften on its own

`quý phụ huynh` is a collective, formality-locked address for broadcasts and official notices.
It only relaxes to `anh/chị` in an established one-to-one thread with a specific, already-known
parent — the channel override the same way a Zalo ZNS template overrides a brand's usual
register elsewhere in this repo. Do not default a 1:1 message to `anh/chị` on a first contact;
start formal and let the parent set a more casual tone if they do.

```
❌  Các cha mẹ thân mến, con bạn hôm nay vắng học.
✅  Kính gửi Quý phụ huynh, em [Tên] vắng học hôm nay không phép.
```

## University administrative prose takes no direct address

The K-12 `con`/`em` warmth is gone by the time a document is university-administrative. A
syllabus, a transcript, or a registration notice addresses no one directly — the student is
`sinh viên`, third person, the same way an RFC's reader is never named:

```
❌  Bạn cần đăng ký học phần trước ngày 15.
✅  Sinh viên cần hoàn tất đăng ký học phần trước ngày 15.
```

A university that wants to sound less institutional in a specific message (an orientation
email, a student-life newsletter) can move to `anh/chị` deliberately — but that is a choice for
that one document, not the administrative default.
