---
name: vietnamese-finance-copy
description: Writes and reviews native-quality Vietnamese (vi-VN) finance content — hóa đơn điện tử and e-invoice fields, báo cáo tài chính and management reports, investor updates and board decks, pricing and payment-terms pages, fintech, banking and insurance product copy, loan and credit disclosures, and thuế GTGT, TNDN and TNCN tax correspondence. Use when drafting Vietnamese financial statements or financial promotion, applying Thông tư 99/2025 statement terminology, checking guaranteed-return, lãi suất, insurance or digital-asset advertising limits, or formatting statement tables, negatives and đơn vị tính. Flags regulated phrasing and routes it to legal review rather than editing around it.
license: MIT
metadata:
  version: "1.0.0"
  repository: "https://github.com/trussary/vietnamese-language-skill"
---

# Vietnamese finance copy (vi-VN)

Finance is the one domain in this repo where getting the words wrong has **statutory**
consequences rather than commercial ones, and where the two most common defects both look
like competent writing:

- **Stale terminology.** Thông tư 200/2014 was replaced by **Thông tư 99/2025/TT-BTC from
  01/01/2026**, and the balance sheet was renamed. Any model writing from pre-2026 data
  produces `Bảng cân đối kế toán`, which is now the wrong name for the statement.
- **Prohibited phrasing that reads as ordinary marketing.** `Cam kết lợi nhuận 12%/năm` is a
  sentence a marketer writes without hesitating. It is also prohibited.

**This skill is a copywriting aid, not legal advice.** Its job is to get copy to legal review
already clean of the known problems. Several rules below route to that review rather than
offering a rewrite, and that is the intended behaviour, not a gap.

## Step 1 — Register: there is effectively one

Finance is **`Quý khách`** for customer-facing copy and **impersonal third person** for
statements, disclosures, and policy. `bạn` appears only in youth-facing fintech, and even
there the money screens and every regulated disclosure revert to formal.

`bạn` in a statement, an invoice, a disclosure, or a loan document is always wrong. Use
`--register finance-formal`. The shared matrix:
**[references/register-matrix.md](references/register-matrix.md)**.

## Step 2 — Core rules (non-negotiable, no file hop needed)

1. **`Báo cáo tình hình tài chính`, not `Bảng cân đối kế toán`**, for any statement dated 2026
   or later. TT 99/2025/TT-BTC, form B01-DN. This is an error, not a preference.
2. **Never write guaranteed-return language.** `cam kết lợi nhuận`, `đảm bảo sinh lời`,
   `bảo toàn vốn`, `đầu tư không rủi ro`, `chắc chắn có lãi`. Write `lợi nhuận kỳ vọng` with a
   risk statement — and send it to legal review anyway.
3. **A promotional rate needs its total cost beside it.** `Lãi suất 0%` without the fees that
   replace it is a transparency breach under TT 43/2016 as amended by TT 18/2019.
4. **Numbers group with periods.** `2.500.000.000`, never `2,500,000,000`. In a finance
   document a comma-grouped number is a factor-of-a-thousand ambiguity, not a style slip.
5. **Negatives use parentheses.** `(1.234)`, never `-1.234`.
6. **Every statement table declares `Đơn vị tính`** — `triệu đồng`, `tỷ đồng`, or `VND`.
7. **Standard tax abbreviations only**: `thuế GTGT`, `thuế TNDN`, `thuế TNCN`, `MST`. Never
   `PIT`, never the English abbreviations.
8. **`Quý I/II/III/IV`**, Roman numerals. Not `Q4`.
9. **No superlatives.** `Lãi suất cao nhất thị trường` is regulated under Luật Quảng cáo Điều 8
   khoản 11. Publish the rate instead — it is more persuasive and it is legal.
10. **Digital assets are not legal tender**, and may only be solicited through a Bộ Tài
    chính–licensed provider under the NQ 05/2025 pilot.

## Step 3 — Get the statement terminology right

The TT 99/2025 renames, statement names, line items, tax abbreviations, and period naming —
plus an explicit statement of what this skill does **not** carry (the full account-code
mapping, which needs an accountant):

**[references/statement-terminology.md](references/statement-terminology.md)**

Wrong-sense renderings that no spellcheck catches — `sự công bằng` for equity, `hiệu trưởng`
for principal, `tỷ lệ quan tâm` for interest rate — are in
**[references/glossary.md](references/glossary.md)**, machine-readable so every row is a lint
rule.

## Step 4 — Format the numbers as a statement, not as prose

Grouped digits, parenthesised negatives, `Đơn vị tính` headers, currency handling, rounding
disclosure, and the e-invoice field labels:

**[references/statement-formatting.md](references/statement-formatting.md)** — plus
**[references/locale-formatting.md](references/locale-formatting.md)** for the general locale
rules and **[references/unicode-and-tone.md](references/unicode-and-tone.md)** for NFC.

## Step 5 — Check the regulated phrasing

Guaranteed returns, interest-rate transparency, insurance and investment-linked disclosure
under TT 67/2023 Điều 53, and the digital-asset position under Luật 71/2025 and NQ 05/2025 —
with the instruments, the effective dates, and an honest account of which prohibitions are
assembled from several sources rather than stated in one article:

**[references/financial-promotion.md](references/financial-promotion.md)** and
**[references/banned-phrases.md](references/banned-phrases.md)**.

Cross-cutting rules shared with the other Vietnamese skills:
**[references/compliance.md](references/compliance.md)**.

## Step 6 — Validate, fix, then route to review

**Run the validator immediately after writing. If it reports errors, fix them and run again.**

```bash
python scripts/validate_copy.py bctc.md --doctype statement --register finance-formal
python scripts/validate_copy.py hoa-don.md --doctype e-invoice
python scripts/validate_copy.py landing-vay.md --doctype financial-promotion
```

- **`FIN001` — guaranteed-return language — is never gated on `--doctype`.** It fires
  everywhere, because the phrasing is prohibited everywhere.
- Other doctypes: `statement`, `e-invoice`, `financial-promotion`, `disclosure`, `loan`.
  `--list-rules` prints everything this skill can emit.
- Exit `0` = clean or warnings only. Exit `1` = errors that must be fixed.
- `--json` for machine-readable findings; `--strict` to fail on warnings too.

**`FIN001` is a warning rather than an error on purpose.** No single article states the
guaranteed-return prohibition verbatim — it is assembled from Luật Chứng khoán Điều 12,
NĐ 155/2020 and NĐ 38/2018. Hard-blocking would over-claim a legal position the sources do not
support in one place. **A `FIN001` warning means "a lawyer decides this", not "reword it until
the linter is quiet."**

For a starter invoice: **[assets/hoa-don-gtgt.md.template](assets/hoa-don-gtgt.md.template)**.

## Step 7 — Two reviewers, then ship

**[references/examples.md](references/examples.md)** for the worked bad→good pairs.

Then the checklist — and unlike the other skills in this repo, this one names **two**
professionals. Statement terminology needs an accountant; anything soliciting investment,
describing insurance, or presenting a credit rate needs a lawyer. A fluent Vietnamese speaker
is not a substitute for either.

**[references/qa-checklist.md](references/qa-checklist.md)**
