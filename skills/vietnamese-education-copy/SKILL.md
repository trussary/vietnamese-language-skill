---
name: vietnamese-education-copy
description: Writes and reviews native-quality Vietnamese (vi-VN) school and academic communication — K-12 report-card remarks and học bạ entries, sổ liên lạc entries and school-to-parent broadcasts, disciplinary and absence notices, university syllabi (đề cương) and course registration, transcripts and GPA statements, diploma reissuance, thesis and admin announcements. Use when drafting or reviewing Vietnamese content for a school, teacher, university, parent, or student audience, choosing thầy/cô-em versus thầy/cô-con versus quý phụ huynh, or applying MoET statutory grading terms (Thông tư 22/2021, 27/2020, 08/2021, 21/2019). Do NOT use this skill for e-learning app UI, gamification, or subtitles (use vietnamese-tech-writing) or for tutoring-centre and study-abroad advertising (use vietnamese-business-comms).
license: MIT
metadata:
  version: "1.0.0"
  repository: "https://github.com/trussary/vietnamese-language-skill"
---

# Vietnamese school and academic writing (vi-VN)

Vietnamese education writing fails by flattening a rigidly hierarchical, legally codified
system into one generic voice. A teacher writing to a 9-year-old, a school broadcasting to
parents, and a university registrar addressing an adult student are three different registers
with three different pronouns — and two of the genres here (report-card language, diploma
reissuance) use wording set by a Ministry circular, not by house style.

**This skill covers instructional and administrative writing only.** E-learning product UI,
gamification, and subtitles belong to `vietnamese-tech-writing`; tutoring-centre, test-prep, and
study-abroad advertising belong to `vietnamese-business-comms` — both are genuinely different
registers (software microcopy, regulated advertising) wearing an education topic.

## Step 1 — Identify the writer, the reader, and the schooling stage

| Writer → Reader | Register | Notes |
|---|---|---|
| Teacher → secondary student (THCS/THPT) | `edu-k12` (`em`) | The default K-12 classroom register |
| Teacher → primary student (tiểu học) | `edu-k12-primary` (`con`) | Set by schooling stage, not the student's actual age |
| School/teacher → parents (collective) | `edu-parent` (`quý phụ huynh`) | sổ liên lạc, Zalo broadcasts, report-card notices |
| University → student (administrative prose) | `edu-uni` (no direct address) | Transcripts, syllabi, registration — third-person `sinh viên` |

`bạn` addressed to a student in a teacher's voice is the single most common
machine-translation tell in this domain — it strips the hierarchical respect the relationship
requires. Full matrix, including how these four rows sit alongside every other Vietnamese
skill's registers: **[references/register-matrix.md](references/register-matrix.md)**. The
education-specific detail — the primary/secondary `con`/`em` line, `quý phụ huynh` versus a
known parent's own register, and a teacher's self-reference (`thầy`/`cô`, never `tôi`) — is in
**[references/doc-registers.md](references/doc-registers.md)**.

## Step 2 — Use the statutory grading terms, not the ones that sound right

Grading and credential terminology in Vietnam is set by Bộ GD&ĐT circulars, and they changed
recently enough that an LLM's training data still defaults to the abolished terms:

- **Secondary (THCS/THPT), Thông tư 22/2021/TT-BGDĐT:** overall classification is `Tốt` /
  `Khá` / `Đạt` / `Chưa đạt`. `Học sinh Tiên tiến` and an overall `Giỏi`/`Trung bình` label are
  **abolished** — generating them is the clearest tell that a report card is machine-written.
- **Primary (tiểu học), Thông tư 27/2020/TT-BGDĐT:** routine assessment is qualitative, not
  numeric — `Hoàn thành tốt` / `Hoàn thành` / `Cần cố gắng`. `Cần cải thiện` is the calque; the
  statutory phrase is `Cần cố gắng`.
- **Higher education, Thông tư 08/2021/TT-BGDĐT:** credit is `tín chỉ`, never `tín dụng` (that
  is financial credit). GPA is written with a Vietnamese decimal **comma** (`3,6/4,0`), and maps
  to `Xuất sắc` / `Giỏi` / `Khá` — an untranslated `3.6/4.0` is a locale bug, not a style choice.
- **Diplomas, Thông tư 21/2019/TT-BGDĐT:** an original diploma is issued once. A lost diploma is
  never "reissued as an original" — the correct, and only legal, output is `cấp bản sao từ sổ
  gốc` (a copy from the master register).

Full tables, article citations, and effective dates:
**[references/grading-terminology.md](references/grading-terminology.md)**.

## Step 3 — Look up the term before inventing one

`giáo trình` (textbook/course material) is not `đề cương` (syllabus/course outline); `đăng ký
khóa học` is the EdTech phrase, `đăng ký học phần` is the university-registration one; `ăn cắp ý
tưởng` is not the formal `đạo văn` (plagiarism). The calque table, with severities:
**[references/glossary.md](references/glossary.md)**.

## Step 4 — Check compliance and formatting

`quý phụ huynh` for parent-facing notices is close to a legal expectation, not just house style
— Điều 89 Luật Giáo dục 2019 frames school-home communication as formal coordination, and a
casual or literal `các bậc cha mẹ` reads as a failure to take that seriously. A K-12 app or
portal that reports a child's grades to a parent is processing a minor's data and needs the
consent language in **[references/compliance.md](references/compliance.md)** (Nghị định
13/2023/NĐ-CP). Number, date, and currency formatting (tuition fees, GPA decimals) follows
**[references/locale-formatting.md](references/locale-formatting.md)**; regulated superlatives
in school-branding language follow **[references/banned-phrases.md](references/banned-phrases.md)**.

## Step 5 — Validate, fix, then ship

**Run the validator immediately after writing. If it reports errors, fix them and run again.
Only present the copy once it passes.**

```bash
python scripts/validate_copy.py hoc-ba.md --doctype secondary-report-card
python scripts/validate_copy.py so-lien-lac.md --doctype primary-report-card --register edu-parent
python scripts/validate_copy.py nhan-xet.md --doctype teacher-to-student --register edu-k12
python scripts/validate_copy.py bang-diem.md --doctype transcript
python scripts/validate_copy.py cap-lai-bang.md --doctype diploma
python scripts/validate_copy.py de-cuong.md --doctype higher-ed --register edu-uni
```

- `--register edu-k12|edu-k12-primary|edu-parent|edu-uni` enables `PRO002`.
- **`--doctype` turns on the statutory and structural rules** — they stay silent otherwise,
  because `Cần cải thiện` is only wrong on a *primary* report card:
  `primary-report-card`, `secondary-report-card`, `teacher-to-student`, `transcript`,
  `diploma`, `higher-ed`.
- Exit `0` = clean or warnings only. Exit `1` = errors that must be fixed.
- `--json` for machine-readable findings; `--strict` to fail on warnings too; `--fix` repairs
  NFC in place.

## Step 6 — Learn from the worked pairs, then hand it to a human

**[references/examples.md](references/examples.md)** — bad→good pairs, each with the circular
or article it fixes. Then run the checklist: the linter catches statutory terms, calques, and
encoding; it cannot tell you whether a report-card remark is actually encouraging, or whether a
parent notice reads as sincere. Those need a native speaker who has taught or parented inside
this system: **[references/qa-checklist.md](references/qa-checklist.md)**
