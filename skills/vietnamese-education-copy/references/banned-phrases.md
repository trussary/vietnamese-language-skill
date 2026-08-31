<!-- vlc-disable: LAW001, CAL001, DIA001 -->

# Banned phrases — school, academic, and EdTech writing

Instructional, administrative, and EdTech writing sits mostly outside advertising law. The exception is
school-branding language — an admissions notice, a school newsletter, or a "why choose us"
paragraph is advertising the moment it makes a comparative or ranking claim, and Luật Quảng cáo
does not carve out an exception for schools. Tutoring-centre and study-abroad *marketing* is
out of scope for this skill entirely — see `vietnamese-business-comms`, whose compliance engine
carries the private-tutoring and outcome-guarantee rules (Thông tư 29/2024/TT-BGDĐT, Nghị định
87/2026/NĐ-CP).

The cross-cutting rules are in [compliance.md](compliance.md). This file adds what school,
academic, and EdTech writing gets wrong specifically.

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

Not a blanket lint rule — a linter cannot judge nuance — but the failure mode is specific enough to name.
Vietnamese report-card, disciplinary, and learning feedback writing is expected to name the behavior or the
competency, never the child: `em cần cố gắng hơn ở môn Toán`, not `học sinh học kém`. A
disciplinary notice records the rule violated (`vi phạm nội quy`) and the consequence
(`hạ hạnh kiểm`), not a US-style "detention" or "suspension" translated wholesale — Vietnamese
schools do not run either mechanism.

## Unpedagogical Pronunciation & Learning Feedback

In EdTech pronunciation scoring (GOP/ASR) and interactive tutoring, raw negative feedback destroys a child's
confidence and violates growth mindset principles.

- **Banned phrases in pronunciation feedback:**
  - `❌ Sai rồi` $\rightarrow$ `✅ Em đọc từ này gần đúng rồi!`
  - `❌ Bạn phát âm sai` $\rightarrow$ `✅ Em thử điều chỉnh luồng hơi ở âm này nhé`
  - `❌ Điểm phát âm của bạn là 30%` $\rightarrow$ `✅ Em đã phát âm rất tốt âm đầu, mình cùng luyện thêm dấu thanh nhé!`
- Enforced on `--doctype pronunciation-feedback` via `EDU009`.

## Empty State Microcopy (Giao diện rỗng)

Displaying literal translations of "Empty State" or "No Data" without a Call-to-Action leaves learners stranded.

- **Banned patterns on UI empty states:**
  - `❌ Trạng thái trống` / `❌ Không có dữ liệu`
  - `✅ Bạn chưa có bài tập nào hôm nay. Hãy bắt đầu với bài Ôn tập Thanh điệu nhé!`
- Enforced on `--doctype edtech-microcopy` via `EDU007`.

## Minor Data and Double Consent (Nghị định 13/2023/NĐ-CP)

A K-12 portal, report-card app, or learning analytics platform processing a child's ($\ge 7$ years old)
grades, voice recordings, or behavioral data requires **Double Consent (Sự đồng ý kép)**:
both the child and the parent/legal guardian must give verified, informed consent stating the specific purpose.
Voice audio files must be purged immediately after GOP analysis unless explicit parental consent is granted.
See [compliance.md](compliance.md) and [edtech-pedagogy.md](edtech-pedagogy.md).
