<!-- vlc-disable: LAW001, CAL001, DIA001 -->

# Banned phrases — school and academic writing

Instructional and administrative writing sits mostly outside advertising law. The exception is
school-branding language — an admissions notice, a school newsletter, or a "why choose us"
paragraph is advertising the moment it makes a comparative or ranking claim, and Luật Quảng cáo
does not carve out an exception for schools. Tutoring-centre and study-abroad *marketing* is
out of scope for this skill entirely — see `vietnamese-business-comms`, whose compliance engine
carries the private-tutoring and outcome-guarantee rules (Thông tư 29/2024/TT-BGDĐT, Nghị định
87/2026/NĐ-CP).

The cross-cutting rules are in [compliance.md](compliance.md). This file adds what school and
academic writing gets wrong specifically.

## Superlatives

Same statute, same test, same annotation as everywhere else in this repo — see
[compliance.md](compliance.md). `Trường tiểu học tốt nhất quận` in an admissions notice is a
regulated claim, not a tagline, whether or not money changed hands for it.

<!-- machine-readable: superlatives -->

| Pattern | Matches | Note |
|---|---|---|
| `(?:tốt\|giỏi\|xuất sắc\|uy tín\|chất lượng)\s+nhất` | "the best / most prestigious ..." | The core banned construction |
| `duy nhất` | "the only" | Named verbatim in the statute |
| `số\s*(?:một\|1)\b` | "number one" | Named verbatim in the statute |
| `hàng đầu` | "leading" | Wording of similar meaning |
| `trường chuẩn quốc gia` | "nationally-standard school" | A specific accreditation status, not a compliment — requires the actual MoET recognition decision, not just the phrase |

## Disciplinary and assessment language

Not a lint rule — a linter cannot judge tone — but the failure mode is specific enough to name.
Vietnamese report-card and disciplinary writing is expected to name the behavior or the
competency, never the child: `em cần cố gắng hơn ở môn Toán`, not `học sinh học kém`. A
disciplinary notice records the rule violated (`vi phạm nội quy`) and the consequence
(`hạ hạnh kiểm`), not a US-style "detention" or "suspension" translated wholesale — Vietnamese
schools do not run either mechanism.

## Minor data and consent

A K-12 portal, report-card app, or Zalo group that reports a specific child's grades,
attendance, or behavior to a parent is processing a minor's personal data. Nghị định
13/2023/NĐ-CP requires the parent's (not the child's) explicit, informed consent, naming the
purpose — see [compliance.md](compliance.md) for the standard consent line.
