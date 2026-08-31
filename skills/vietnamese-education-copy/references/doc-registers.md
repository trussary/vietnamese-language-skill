<!-- vlc-disable: TONE001, DIA001 -->

# Document registers — teacher, student, parent, and EdTech app

The pronoun in Vietnamese educational writing is set by **schooling stage, relationship, and pedagogical context**, not
by the writer's house style and not by the student's actual age. Getting the wrong one is not
a tone problem — it reads as a different kind of institution or a broken translation.

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
| EdTech learning app, mascot nudges, interactive tutoring to learner | `edu-k12` / `edu-k12-primary` | `em` / `bạn nhỏ` (mascot persona, encouraging) |
| EdTech parent analytics dashboard & weekly progress reports | `edu-parent` | `quý phụ huynh` / `anh/chị` |

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

## Teacher and Mascot self-reference

A teacher refers to themselves as `thầy` or `cô`, never `tôi` or `mình`, when addressing a
student directly:

```
❌  Tôi rất vui vì em đã tiến bộ.
✅  Thầy/Cô rất vui vì em đã tiến bộ.
```

In an EdTech application, an AI assistant or Mascot refers to itself by its named persona (e.g., `chú Voi con`, `Gấu Kiki`, `hệ thống`) or speaks as an encouraging mentor, addressing the learner as `em` or `bạn nhỏ`:

```
❌  Tôi thấy bạn đã không học 2 ngày.
✅  Chào bạn nhỏ! Chú Voi con thấy em đã vắng mặt 2 ngày rồi. Mình cùng vào ôn tập nhé!
```

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

## Parental Analytics: Translating Telemetry into Constructive Action

When an EdTech platform summarizes a child's weekly performance, diagnostic GOP pronunciation scores, or mastery milestones for parents:
- **Tone:** Respectful (`Kính gửi Quý phụ huynh` / `Anh/Chị [Tên]`), transparent, constructive.
- **Structure:** State achievements first $\rightarrow$ Identify growth areas $\rightarrow$ Provide a concrete home-learning Call to Action (CTA).

```
❌  Báo cáo: Bé Tuấn phát âm sai 30% âm tr/ch. Cần giám sát.
✅  Kính gửi Quý phụ huynh, tuần này bé Tuấn đã xuất sắc nắm vững cấu trúc câu đơn. Dù bé còn đôi chút nhầm lẫn giữa âm "tr" và "ch", hệ thống đã tự động bổ sung bài tập luyện đọc. Anh/Chị có thể cùng bé luyện đọc truyện tranh vào buổi tối nhé!
```

## University administrative prose takes no direct address

The K-12 `con`/`em` warmth is gone by the time a document is university-administrative. A
syllabus, a transcript, or a registration notice addresses no one directly — the student is
`sinh viên`, third person, the same way an RFC's reader is never named:

```
❌  Bạn cần đăng ký học phần trước ngày 15.
✅  Sinh viên cần hoàn tất đăng ký học phần trước ngày 15.
```

## Gamification & Overjustification Prevention (SDT)

When learners complete easy modules repeatedly, unpedagogical copy reinforces bad habits with superficial extrinsic rewards (`Bạn nhận được 100 XP!`).
Pedagogical copywriting redirects extrinsic motivation towards intrinsic mastery (Self-Determination Theory):

```
❌  Chúc mừng bạn nhận thêm 50 điểm kinh nghiệm! Làm tiếp để lên top 1 nhé!
✅  Em đã hoàn toàn tinh thông bài học này rồi! Thử thách Vượt cấp hấp dẫn hơn đang chờ em phía trước. Cùng khám phá ngay nhé!
```
