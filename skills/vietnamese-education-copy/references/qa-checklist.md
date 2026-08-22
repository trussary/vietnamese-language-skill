<!-- vlc-disable: DIA001, CAL001 -->

# QA checklist — what the linter cannot check

The validator catches encoding, calques, statutory grading terms, and a handful of
doctype-gated structural rules. Everything below needs a human, and most of it needs a human
who has actually taught, studied, or worked administration inside this system — fluency in
Vietnamese is not the same skill as knowing what a homeroom teacher would actually write.

Work top to bottom. Sections 1–2 catch more real defects than the rest combined.

## 1. Register

- [ ] Does the document match its register in [doc-registers.md](doc-registers.md) — schooling
      stage decides `em` vs. `con`, not the student's actual age?
- [ ] Is `bạn` absent from every direct teacher-to-student message?
- [ ] Does a parent-facing notice use `quý phụ huynh`, not a literal `các bậc cha mẹ`?
- [ ] Does a teacher refer to themself as `thầy`/`cô`, never `tôi`, when addressing a student?
- [ ] Is university administrative prose free of direct address (`bạn`, `em`, `con`) and using
      third-person `sinh viên` throughout?

## 2. Statutory terms

- [ ] Secondary (THCS/THPT) overall classification uses `Tốt` / `Khá` / `Đạt` / `Chưa đạt` —
      never `Học sinh Tiên tiến` or an overall `Giỏi`/`Trung bình`.
- [ ] Primary routine assessment is qualitative and says `cần cố gắng`, never `cần cải thiện`.
- [ ] GPA is written with a Vietnamese decimal comma and mapped to `xuất sắc`/`giỏi`/`khá`, not
      left as an untranslated `X.X/4.0`.
- [ ] A lost diploma is replaced by a copy from the master register (`bản sao từ sổ gốc`),
      never described as a reissued original.
- [ ] Academic credit is `tín chỉ`; `tín dụng` is reserved for genuinely financial contexts.

## 3. Tone — the part a regex cannot judge

- [ ] Does negative feedback name the behavior or competency, never the child
      (`em cần cố gắng hơn ở môn Toán`, not `học sinh học kém`)?
- [ ] Does a disciplinary notice reference the rule violated and the actual Vietnamese
      mechanism (`vi phạm nội quy`, `hạ hạnh kiểm`), not a translated "detention"/"suspension"?
- [ ] Does a parent notice read as genuinely informative, or as a form letter with the name
      swapped in?
- [ ] Read the report-card remark or notice aloud — would the actual student or parent
      recognize themselves in it?

## 4. Minor data and consent

- [ ] Does a portal or app reporting a specific child's grades or attendance to a parent state
      the purpose of processing that data (Nghị định 13/2023/NĐ-CP)?
- [ ] Is consent sought from the parent, not the (minor) student?

## 5. Formatting

- [ ] Tuition, fees, and other currency amounts follow
      [locale-formatting.md](locale-formatting.md) (period grouping, `đ`/`VNĐ`, not `VND` with
      comma grouping).
- [ ] Dates are `dd/MM/yyyy`.
- [ ] Subject names (`Toán`, `Ngữ văn`, `Khoa học Tự nhiên`) are capitalized consistently.
- [ ] `GVCN` and `PHHS` are only used where the reader already knows the abbreviation —
      spell out on first use in anything leaving the school's internal channels.

## 6. Anything that makes a claim

- [ ] An admissions notice, newsletter, or "why choose us" paragraph is free of unproven
      superlatives — see [banned-phrases.md](banned-phrases.md) and
      [compliance.md](compliance.md).
- [ ] If the document is actually tutoring-centre or study-abroad advertising rather than
      school administration, hand it to `vietnamese-business-comms` instead — its compliance
      engine, not this skill's, carries the 2024–2026 tutoring and outcome-guarantee rules.

## Sign-off

A change to the glossary, the grading-terminology tables, or the examples corpus needs a
**native Vietnamese speaker with direct classroom, parenting, or university-admin experience**
to approve it — the terminology here is legally and institutionally specific, not a matter of
fluency.

| Reviewer | Checks | Date |
|---|---|---|
| | Sections 1–2 | |
| | Sections 3–4 | |
| | Sections 5–6 | |
