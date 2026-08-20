<!-- vlc-disable: NUM001, NUM002, NUM003, DIA001 -->

# Statement formatting

The general locale rules are in [locale-formatting.md](locale-formatting.md) and apply here
with no exceptions. This file adds the conventions specific to financial statements and
tables, where a formatting error is a **reporting** error rather than a cosmetic one.

## Numbers

Vietnamese groups with periods and decimalizes with commas — the opposite of US English.

```
✅  2.500.000.000        ❌  2,500,000,000
✅  2.500.000,50         ❌  2,500,000.50
```

In a finance document this rule is not a style preference. `2,500` read as a Vietnamese number
is two and a half, and the difference between 2,5 and 2.500 is a factor of a thousand.
`FIN004` therefore reports comma-grouped numbers wherever they appear in a finance document.

## Negatives use parentheses, not a minus sign

The statement convention:

```
✅  (1.234)              ❌  -1.234
✅  (1.234.567)          ❌  −1.234.567
```

`FIN006` flags a minus-signed number under `--doctype statement`. Parentheses are what an
accountant reading the column expects, and a minus sign mid-column is read as a typo or missed
entirely.

## Every table declares its unit

A statement table carries a unit header. Without it the reader cannot tell whether a cell says
one million or one billion.

```
Đơn vị tính: triệu đồng
Đơn vị tính: tỷ đồng
Đơn vị tính: VND
```

`FIN005` flags a statement table with no `Đơn vị tính` header.

## Do not mix the colloquial and grouped forms

Narrative prose takes the colloquial scale; tables take grouped digits. Switching between them
inside one context is the defect.

| Context | ✅ |
|---|---|
| Narrative | `Doanh thu đạt 2,5 tỷ đồng trong Quý IV.` |
| Table cell | `2.500.000.000` |
| Table cell, with a unit header of `triệu đồng` | `2.500` |
| Both, deliberately | `2.500.000.000 ₫ (2,5 tỷ đồng)` |

The last row is a legitimate pattern for a headline figure. A **column** that alternates
between `2.500` and `2,5 tỷ` is not.

## Currency

- State the currency explicitly. `₫` (U+20AB) or `VND` or `đồng` — pick one per document.
- The symbol follows the amount: `2.500.000 ₫`, not `₫2.500.000`.
- When a document mixes VND and a foreign currency, **footnote the conversion rate and its
  date**. An unfootnoted USD figure in a VND statement is unauditable.
- `Đơn vị tính: USD` is as necessary as the VND version.

## Rounding

Disclose it in the notes. If figures are presented in `triệu đồng`, say whether they are
rounded or truncated, and keep it consistent — a column that rounds some rows and truncates
others will not sum.

## Dates and periods

- `dd/MM/yyyy` throughout. `12/25/2026` is not a date in Vietnam.
- `Quý I/II/III/IV`, `Năm tài chính 2026`.
- A period label states both endpoints: `Từ 01/01/2026 đến 31/12/2026`.

## E-invoice fields

An electronic invoice under NĐ 123/2020/NĐ-CP as amended by NĐ 70/2025/NĐ-CP carries mandatory
fields. The ones that matter for copy:

| Field | Label |
|---|---|
| Invoice name | `Hóa đơn giá trị gia tăng` / `Hóa đơn GTGT` |
| Seller tax code | `MST` |
| Buyer tax code | `MST người mua` |
| Tax rate | `Thuế suất GTGT` |
| Tax amount | `Tiền thuế GTGT` |
| Total before tax | `Cộng tiền hàng` |
| Total payable | `Tổng cộng tiền thanh toán` |
| Amount in words | `Số tiền viết bằng chữ` |

`FIN007` flags an invoice document that names no `MST` and no `thuế GTGT`.

**The exact mandated label strings under the NĐ 70/2025 amendment are not verified in this
skill.** The labels above are the conventional forms in current use. Before encoding them into
an invoice template that will be filed, check them against the decree — a mislabelled
mandatory field is a rejected invoice.

## Amount in words

Vietnamese invoices carry the amount written out, ending with `đồng` and, conventionally,
`./.` to close the line against tampering:

```
Số tiền viết bằng chữ: Hai tỷ năm trăm triệu đồng ./.
```
