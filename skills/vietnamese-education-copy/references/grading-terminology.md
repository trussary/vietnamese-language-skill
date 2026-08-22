<!-- vlc-disable: CAL001, DIA001 -->

# Grading and credential terminology — statutory, not house style

Everything in this file is set by a Bộ GD&ĐT (MoET) circular, not by convention. An LLM's
training data still defaults to terms these circulars **abolished**, which is why the highest-
risk rows here are enforced by `scripts/rules_education.py` rather than left to a style guide.
Verify each instrument is still current before relying on it — Vietnamese education regulation
has moved substantially in the past few years, and a native reviewer should confirm no
newer amendment has superseded a row below.

## Primary school (tiểu học) — Thông tư 27/2020/TT-BGDĐT

Routine assessment is qualitative, not numeric.

| Concept | ❌ Do not write | ✅ Statutory term | Article |
|---|---|---|---|
| Overall competency, top tier | `xuất sắc` as the routine label | `hoàn thành tốt` | Điều 6 |
| Overall competency, meets expectation | — | `hoàn thành` | Điều 6 |
| Needs more effort | `cần cải thiện` | `cần cố gắng` | Điều 7 |

`EDU003` (error) fires on `cần cải thiện` when `--doctype primary-report-card` is set — it is
the calque a translator reaches for by default, and it is not the statutory phrase.

## Secondary (THCS/THPT) — Thông tư 22/2021/TT-BGDĐT

The overall classification changed. The old four/five-tier scale (`Giỏi` / `Khá` / `Trung
bình` / `Yếu` / `Kém`, and the title `Học sinh Tiên tiến`) no longer exists as an **overall**
label.

| Concept | ❌ Abolished | ✅ Statutory term | Article |
|---|---|---|---|
| Overall classification, top tier | `giỏi` / `học sinh tiên tiến` | `tốt` | Điều 9 |
| Overall classification, second tier | `khá` (as a distinct overall tier) | `khá` is retained one tier down — see the circular's full mapping | Điều 9 |
| Overall classification, meets requirement | `trung bình` | `đạt` | Điều 9 |
| Overall classification, does not meet | `yếu` / `kém` | `chưa đạt` | Điều 9 |

`Giỏi` is not banned outright — it is still correct as a **subject-specific** score descriptor
in some contexts. What is wrong is using it, or `Học sinh Tiên tiến`, as the **overall**
end-of-year classification, which is what `EDU001` (error, `--doctype secondary-report-card`)
catches.

## Higher education — Thông tư 08/2021/TT-BGDĐT

| Concept | ❌ Do not write | ✅ Statutory term | Article |
|---|---|---|---|
| Academic credit unit | `tín dụng` | `tín chỉ` | — |
| GPA classification, ~3.6–4.0 | — | `xuất sắc` | Điều 14 |
| GPA classification, ~3.2–3.59 | — | `giỏi` | Điều 14 |
| GPA classification, ~2.5–3.19 | — | `khá` | Điều 14 |

Vietnamese locale uses a **decimal comma**: `3,6/4,0`, never `3.6/4.0`. `EDU006` (error,
`--doctype transcript`) catches the dot-decimal GPA pattern specifically, because the generic
number-formatting rule (`NUM003`) only fires on a decimal followed by `tỷ`/`triệu`/`%`/`m²`,
none of which appear next to a GPA.

`EDU005` (warn, `--doctype higher-ed` or `transcript`) catches `tín dụng` used for academic
credit. It is gated rather than blocklisted outright because `tín dụng sinh viên` (student
credit/loan) is a real, correct phrase in the same documents — see
[glossary.md](glossary.md#terms-where-context-decides--do-not-blocklist).

## Diplomas — Thông tư 21/2019/TT-BGDĐT

A diploma's **original** (`bản chính`) is issued exactly once, at graduation, and recorded in a
master register (`sổ gốc`). Vietnamese law has no mechanism to reissue a second original — a
lost diploma is replaced with a **copy from the master register**, a legally distinct document
(Điều 18, Điều 31). The two-row glossary entry for this — the phrase itself is short enough to
blocklist outright — is `error` severity in [glossary.md](glossary.md), because there is no
context in which "reissue the original" is the correct thing to write.

## What this file deliberately does not cover

Curriculum content and Ministry-facing prose (Thông tư 32/2018/TT-BGDĐT, the Chương trình giáo
dục phổ thông 2018 competency vocabulary) is out of scope for this skill — see the repo's
`research/education-research` for the reasoning. If a document needs that register, an LLM
already handles dry, formal government prose adequately without this skill's intervention.
