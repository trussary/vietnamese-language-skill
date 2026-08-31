---
name: vietnamese-education-copy
description: Writes and reviews native-quality Vietnamese (vi-VN) educational, school, academic, and EdTech communication — K-12 report-card remarks and học bạ entries, sổ liên lạc entries and school-to-parent broadcasts, pedagogical nudges, diagnostic pronunciation feedback, adaptive assessment, parental analytics reports, university syllabi (đề cương) and course registration, transcripts and GPA statements, diploma reissuance, thesis and academic notices. Use when drafting or reviewing Vietnamese content for a school, teacher, EdTech app, university, parent, or student audience, choosing thầy/cô-em versus thầy/cô-con versus quý phụ huynh, or applying MoET statutory grading terms (Thông tư 22/2021, 27/2020, 08/2021, 21/2019) and EdTech learning science frameworks. Do NOT use this skill for general software developer docs (use vietnamese-tech-writing) or for tutoring-centre and study-abroad advertising (use vietnamese-business-comms).
license: MIT
metadata:
  version: "2.0.0"
  repository: "https://github.com/trussary/vietnamese-language-skill"
---

# Vietnamese educational, academic, and EdTech writing (vi-VN)

Vietnamese education writing fails by flattening a rigidly hierarchical, legally codified, and
pedagogically sensitive system into one generic voice. A teacher writing to a 9-year-old, an EdTech
AI assistant tutoring pronunciation, a school broadcasting to parents, and a university registrar
addressing an adult student represent distinct registers with distinct pronouns and legal rules.

**This skill covers educational, instructional, academic, and EdTech pedagogical writing.** General
developer documentation (PRDs, RFCs, API docs) belongs to `vietnamese-tech-writing`; commercial
tutoring-center and study-abroad advertising campaigns belong to `vietnamese-business-comms`.

## Step 1 — Identify the writer, the reader, and the pedagogical context

| Writer → Reader | Register | Notes |
|---|---|---|
| Teacher → secondary student (THCS/THPT) | `edu-k12` (`em`) | The default K-12 classroom register |
| Teacher → primary student (tiểu học) | `edu-k12-primary` (`con`) | Set by schooling stage, not the student's actual age |
| School / Teacher → parents (collective) | `edu-parent` (`quý phụ huynh`) | sổ liên lạc, Zalo broadcasts, report-card notices |
| EdTech Mascot / AI Tutor → learner | `edu-k12` / `edu-k12-primary` (`em` / `bạn nhỏ`) | Encouraging mentor persona, Growth Mindset |
| EdTech Dashboard → parent | `edu-parent` (`quý phụ huynh` / `anh/chị`) | Weekly learning analytics, transparent & actionable |
| University → student (administrative prose) | `edu-uni` (no direct address) | Transcripts, syllabi, registration — third-person `sinh viên` |

`bạn` addressed to a student in a teacher's voice is the single most common machine-translation
tell in this domain. Full register matrix: **[references/register-matrix.md](references/register-matrix.md)**.
Detailed educational registers and persona guidance: **[references/doc-registers.md](references/doc-registers.md)**.

## Step 2 — Use statutory grading terms, not the ones that sound right

Grading and credential terminology in Vietnam is codified by Bộ GD&ĐT circulars:

- **Secondary (THCS/THPT), Thông tư 22/2021/TT-BGDĐT:** Overall classification is `Tốt` / `Khá` /
  `Đạt` / `Chưa đạt`. `Học sinh Tiên tiến` and an overall `Giỏi`/`Trung bình` label are **abolished**.
- **Primary (tiểu học), Thông tư 27/2020/TT-BGDĐT:** Routine assessment is qualitative:
  `Hoàn thành tốt` / `Hoàn thành` / `Cần cố gắng`. `Cần cải thiện` is the calque; the statutory phrase is `Cần cố gắng`.
- **Higher education, Thông tư 08/2021/TT-BGDĐT:** Academic credit is `tín chỉ`, never `tín dụng`.
  GPA is written with a Vietnamese decimal **comma** (`3,6/4,0`), mapping to `Xuất sắc` / `Giỏi` / `Khá`.
- **Diplomas, Thông tư 21/2019/TT-BGDĐT:** A lost diploma is replaced only by `cấp bản sao từ sổ gốc`
  (a copy from the master register), never "reissued as an original".

Full circular tables: **[references/grading-terminology.md](references/grading-terminology.md)**.

## Step 3 — Apply Learning Science & EdTech Pedagogical Intelligence

When generating interactive learning copy or AI feedback:

1. **Pedagogical Nudges (Spaced Repetition & Habit Loops):** Frame reminder notifications with positive psychology. Mention specific topics (e.g. `âm tr/ch`) and streak continuations without shame or guilt.
2. **Diagnostic Pronunciation Feedback (Sandwich Model):** When interpreting GOP/ASR acoustic scores:
   - *Layer 1:* Praise effort and identify correctly pronounced phonemes.
   - *Layer 2:* Provide concrete, phoneme-level guidance (e.g., pitch/tone adjustment, vocal tract airflow).
   - *Layer 3:* Encourage with a Growth Mindset. Never use blunt negative tags (`Sai rồi`, `Điểm của bạn là 30%`).
3. **Adaptive Assessment & Scaffolding (IRT & ZPD):** Route question difficulty using 3PL IRT ($b, a, c$) and provide 3-tier fading hints (Rule $\rightarrow$ Keyword $\rightarrow$ Correction) towards Mastery Learning.
4. **Parental Analytics Translation:** Translate raw learning telemetry into empathetic, constructive updates for parents with concrete home-support suggestions.
5. **Prevent Overjustification (SDT):** When learners master a topic, transition from extrinsic XP rewards to intrinsic mastery challenges.
6. **Actionable Empty States:** Never display raw `"Trạng thái trống"` or `"Không có dữ liệu"` — provide a helpful Call to Action.

Full framework and capability maps: **[references/edtech-pedagogy.md](references/edtech-pedagogy.md)**.

## Step 4 — Check the EdTech Lexicon and Avoid Translationese

Avoid the 15 notorious translationese traps: `nộp bài` (not `đệ trình`), `tổng quan` (not `bảng táp-lô`),
`xem tiến độ học tập` (not `theo dấu sự tiến bộ`), `bảng xếp hạng` (not `bảng lãnh đạo`), `học tập thông hiểu`
(not `học tập làm chủ`), `đánh giá quá trình` (not `đánh giá định hình`), `chuỗi học tập` (not `vệt học tập`),
`hỗ trợ từng bước` (not `giàn giáo`). Complete 60-term glossary: **[references/glossary.md](references/glossary.md)**.

## Step 5 — Verify Legal Compliance and Child Data Protection

- **Minor Double Consent (Nghị định 13/2023/NĐ-CP Điều 20):** Collecting data from children $\ge 7$ years old requires verified consent from both the child AND parent/guardian.
- **Biometric Voice Data:** Audio recordings must be automatically purged after GOP scoring.
- **Advertising Superlatives:** School admissions claims must adhere to Luật Quảng cáo (no unproven `số 1`, `tốt nhất`).

Full compliance guidelines: **[references/compliance.md](references/compliance.md)** and **[references/banned-phrases.md](references/banned-phrases.md)**.

## Step 6 — Validate, Fix, then Ship

Run the validator to catch statutory terms, calques, empty-state errors, and encoding defects:

```bash
python scripts/validate_copy.py hoc-ba.md --doctype secondary-report-card
python scripts/validate_copy.py so-lien-lac.md --doctype primary-report-card --register edu-parent
python scripts/validate_copy.py nhan-xet.md --doctype teacher-to-student --register edu-k12
python scripts/validate_copy.py phat-am.md --doctype pronunciation-feedback
python scripts/validate_copy.py ui-app.md --doctype edtech-microcopy
python scripts/validate_copy.py bang-diem.md --doctype transcript
python scripts/validate_copy.py de-cuong.md --doctype higher-ed --register edu-uni
```

- `--register edu-k12|edu-k12-primary|edu-parent|edu-uni` enables `PRO002`.
- `--doctype` activates statutory and structural checks: `primary-report-card`, `secondary-report-card`, `teacher-to-student`, `pronunciation-feedback`, `edtech-microcopy`, `transcript`, `diploma`, `higher-ed`.

## Step 7 — Review Worked Examples and QA Checklist

- **[references/examples.md](references/examples.md)** — Bad $\rightarrow$ Good pairs with diagnostic explanations.
- **[references/qa-checklist.md](references/qa-checklist.md)** — Human review checklist for pedagogical tone, empathy, and regulatory compliance.
