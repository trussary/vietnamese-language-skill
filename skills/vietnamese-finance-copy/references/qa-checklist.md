<!-- vlc-disable: DIA001, CAL001, LAW001, NUM002 -->

# QA checklist — human review rubric

This skill's linter catches known phrasings. It cannot tell you whether a disclosure is
complete, whether a licence exists, or whether a projected return is defensible — and those
are the checks that carry the statutory consequences.

**Two reviewers, not one.** Statement terminology needs an accountant. Anything soliciting
investment, describing insurance, or presenting a credit rate needs a lawyer. A fluent
Vietnamese speaker is not a substitute for either.

## 1. Route to legal — do this before anything else

Tick the box only if the document has actually been through review, not if you believe it
would pass.

- [ ] Any document soliciting investment from the public → **lawyer**.
- [ ] Any insurance product description, especially investment-linked → **lawyer**.
- [ ] Any consumer-credit or installment rate presentation → **lawyer**.
- [ ] Any crypto or digital-asset promotion → **lawyer**.
- [ ] **Every `FIN001` finding, without exception**, regardless of how the sentence was
      reworded afterwards.
- [ ] Any financial statement intended for filing → **accountant**.

## 2. Prohibited language

- [ ] No guaranteed-return phrasing anywhere: `cam kết lợi nhuận`, `đảm bảo sinh lời`,
      `bảo toàn vốn`, `đầu tư không rủi ro`, `chắc chắn có lãi`.
- [ ] No sensational return framing: `lợi nhuận khủng`, `x2 tài khoản`, `làm giàu không khó`.
- [ ] No superlative without `<!-- proof: ... -->` naming a real, current document —
      `lãi suất cao nhất`, `ngân hàng số 1`, `app đầu tư hàng đầu`.
- [ ] No suitability claim: `ai cũng có thể đầu tư`, `không cần kiến thức vẫn có lãi`.
- [ ] No implied deposit product where there is none.

## 3. Required disclosures — `FIN008`

Presence is checkable by eye; **completeness is what needs the lawyer.**

- [ ] `Đầu tư có rủi ro` on any investment solicitation.
- [ ] `Kết quả trong quá khứ không đảm bảo kết quả trong tương lai` next to any performance
      figure.
- [ ] Investment-linked insurance: states that it **is an insurance product**, that investment
      results are not guaranteed, and that the policyholder bears the risk.
- [ ] Investment-linked insurance sold through a bank channel: session recording and the
      60-day restriction under TT 67/2023 Điều 53 are in place.
- [ ] Any `lãi suất 0%` or promotional rate: fees, calculation method, and **total amount
      payable** stated adjacent to the rate, not in a later section.
- [ ] Early-withdrawal and management fees stated wherever a return is stated.

## 4. Digital assets — `FIN009`

- [ ] The platform being promoted is **actually licensed by the Bộ Tài chính** under the
      NQ 05/2025 pilot. This is a fact about the world; verify it, do not assume it.
- [ ] Copy says digital assets are **not legal tender**.
- [ ] No offshore or unlicensed exchange named or implied.

## 5. Statement terminology — accountant

- [ ] `Báo cáo tình hình tài chính`, not `Bảng cân đối kế toán`, for any statement dated
      2026 or later (TT 99/2025, in force 01/01/2026).
- [ ] Account codes checked against TT 99/2025 directly. **This skill does not carry the full
      mapping** — do not infer a code from its glossary.
- [ ] Standard tax abbreviations: `thuế GTGT`, `thuế TNDN`, `thuế TNCN`, `MST`.
- [ ] Statement names and line items match the current forms.
- [ ] No claim that IFRS adoption is mandatory — as of 2026 it is largely voluntary, and that
      is separate from the TT 99/2025 change, which is mandatory.

## 6. Formatting — a reporting error, not a cosmetic one

- [ ] Numbers grouped with periods: `2.500.000.000`. **A comma-grouped number in a finance
      document is a factor-of-a-thousand ambiguity**, not a style slip.
- [ ] Negatives in parentheses: `(1.234)`, never `-1.234`.
- [ ] Every table carries `Đơn vị tính`.
- [ ] Colloquial `tỷ`/`triệu` in prose and grouped digits in tables, never mixed in one column.
- [ ] Currency stated explicitly; foreign-currency conversion rate and date footnoted.
- [ ] Rounding disclosed in the notes, and applied consistently — columns must sum.
- [ ] Dates `dd/MM/yyyy`; periods state both endpoints; `Quý I/II/III/IV`.

## 7. E-invoice fields

- [ ] `Hóa đơn GTGT` named as such.
- [ ] Seller and buyer `MST` present.
- [ ] `Thuế suất GTGT` and `Tiền thuế GTGT` present.
- [ ] `Tổng cộng tiền thanh toán` and `Số tiền viết bằng chữ` present.
- [ ] **Field labels verified against NĐ 70/2025 directly** before the template is used for
      real filing — this skill's labels are the conventional forms, not verified statutory
      strings.

## 8. Register

- [ ] `Quý khách` or impersonal third person throughout. No `bạn` in a statement, disclosure,
      invoice, or loan document.
- [ ] One register from start to finish.
- [ ] NFC throughout; one tone-mark style.

## Sign-off

| Reviewer | Role | Checks | Date |
|---|---|---|---|
| | Lawyer (securities / insurance) | Sections 1–4 | |
| | Accountant | Sections 5, 7 | |
| | Native reviewer | Sections 6, 8 | |

A change to this skill's glossary or corpus needs the relevant professional, not a translator.
