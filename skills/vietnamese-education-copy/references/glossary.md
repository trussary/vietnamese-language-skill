<!-- vlc-disable: CAL001, DIA001 -->

# Glossary — school and academic terms

Two tables. The first is machine-readable: `validate_copy.py` parses it, so every row is a
lint rule and adding a row needs no code change. The second is guidance the linter cannot
enforce, because the correct term depends on context the linter cannot see.

An optional `Severity` column overrides the default. Use `error` for a calque no Vietnamese
teacher, registrar, or admin office would ever write, `warn` for one that is merely unnatural
or that a native reader would notice but not consider broken.

## Calques that mark machine translation

<!-- machine-readable: glossary -->

| EN | ❌ Calque | ✅ Native usage | Severity |
|---|---|---|---|
| report card | `thẻ báo cáo` | `học bạ / sổ liên lạc` | error |
| homeroom teacher | `giáo viên phòng nhà` | `giáo viên chủ nhiệm` | error |
| parents (collective, formal) | `các bậc cha mẹ` | `quý phụ huynh` | warn |
| dear parents | `thân gửi các cha mẹ` | `kính gửi quý phụ huynh` | warn |
| plagiarism | `ăn cắp ý tưởng` | `đạo văn` | error |
| reissue a lost original diploma | `cấp lại bằng gốc` | `cấp bản sao từ sổ gốc` | error |
| reissue a lost original diploma (alt.) | `cấp lại bản chính` | `cấp bản sao từ sổ gốc` | error |
| academic credit | `tín dụng học tập` | `tín chỉ` | error |
| learning outcomes (syllabus) | `kết quả học tập mong muốn` | `chuẩn đầu ra` | warn |

## Terms where context decides — do not blocklist

These are legitimate Vietnamese words with a genuine second meaning, so they are deliberately
**not** in the machine-readable table above; a blanket rule would fire on correct usage as
often as on the calque.

| EN | Wrong here | Right here | Why it is not a lint rule |
|---|---|---|---|
| syllabus / course outline | `giáo trình` (this is *textbook*, not *syllabus*) — write `đề cương môn học` / `đề cương chi tiết học phần` | — | `giáo trình` is correct whenever the writer actually means "textbook"; the linter cannot tell the two apart |
| university course registration | `đăng ký khóa học` reads as an EdTech phrase, not a registrar one — write `đăng ký học phần` | — | `khóa học` is the right word for an e-learning or short course; only university-registrar prose wants `học phần` |
| academic vs. financial credit | `tín dụng` in a higher-ed document | `tín chỉ` (academic) — but `tín dụng sinh viên` (student credit/loan) is a real, correct phrase | gated behind `--doctype higher-ed`/`transcript` instead of blocklisted — see `scripts/rules_education.py` (`EDU005`) |

## Statutory grading and credential terms

These are not calques to fix in passing — they are the actual legal wording. See
**[grading-terminology.md](grading-terminology.md)** for the full circular-by-circular tables;
the highest-risk ones are enforced by `scripts/rules_education.py` (`EDU001`, `EDU003`,
`EDU006`) because they are only correct or incorrect for one schooling stage.
