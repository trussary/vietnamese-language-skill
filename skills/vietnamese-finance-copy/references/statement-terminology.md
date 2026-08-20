<!-- vlc-disable: DIA001, CAL001, NUM001, NUM002 -->

# Statement terminology — Thông tư 99/2025/TT-BTC

**Thông tư 200/2014/TT-BTC is replaced by Thông tư 99/2025/TT-BTC from 01/01/2026.** Any
Vietnamese financial statement wording an LLM produces from pre-2026 training data is stale,
and the most visible case is the balance sheet, which was renamed.

## The rename that matters most

| EN | ❌ Pre-2026 | ✅ From 01/01/2026 |
|---|---|---|
| Balance sheet | `Bảng cân đối kế toán` | `Báo cáo tình hình tài chính` |

Form code **B01-DN**. This is `FIN003`, and it is an **error** rather than a warning: unlike a
register choice, there is no context in which the old name is the correct one for a statement
dated 2026 or later.

The exception is a historical reference — "the 2024 `Bảng cân đối kế toán`" is correct as a
description of a past document. Suppress the rule on that line rather than working around it.

## Statement names

| EN | ✅ Vietnamese |
|---|---|
| Financial statements | `Báo cáo tài chính` |
| Statement of financial position (balance sheet) | `Báo cáo tình hình tài chính` |
| Income statement | `Báo cáo kết quả hoạt động kinh doanh` |
| Cash flow statement | `Báo cáo lưu chuyển tiền tệ` |
| Notes to the financial statements | `Thuyết minh báo cáo tài chính` |
| Chart of accounts | `Hệ thống tài khoản kế toán` |
| Trial balance | `Bảng cân đối số phát sinh` |
| General ledger | `Sổ cái` |
| Fiscal year | `Năm tài chính` |
| Accounting period | `Kỳ kế toán` |

## Line items

| EN | ✅ Vietnamese |
|---|---|
| Revenue | `Doanh thu` |
| Net revenue | `Doanh thu thuần` |
| Cost of goods sold | `Giá vốn hàng bán` |
| Gross profit | `Lợi nhuận gộp` |
| Operating expenses | `Chi phí hoạt động` |
| Selling expenses | `Chi phí bán hàng` |
| Administrative expenses | `Chi phí quản lý doanh nghiệp` |
| Financial income / expense | `Doanh thu / Chi phí tài chính` |
| Profit before tax | `Lợi nhuận trước thuế` |
| Profit after tax | `Lợi nhuận sau thuế` |
| Total assets | `Tổng tài sản` |
| Current assets | `Tài sản ngắn hạn` |
| Non-current assets | `Tài sản dài hạn` |
| Liabilities | `Nợ phải trả` |
| Owner's equity | `Vốn chủ sở hữu` |
| Retained earnings | `Lợi nhuận sau thuế chưa phân phối` |
| Accounts receivable | `Phải thu khách hàng` |
| Accounts payable | `Phải trả người bán` |
| Cash and cash equivalents | `Tiền và tương đương tiền` |
| Depreciation | `Khấu hao` |
| Provision | `Dự phòng` |

## Tax terminology

Use the standard abbreviations. Spelling them out in full, or importing the English
abbreviation, both read as non-native.

| EN | ✅ Vietnamese | Note |
|---|---|---|
| Value-added tax | `Thuế GTGT` | giá trị gia tăng; mandatory e-invoice field |
| Corporate income tax | `Thuế TNDN` | thu nhập doanh nghiệp |
| Personal income tax | `Thuế TNCN` | thu nhập cá nhân — never `PIT` |
| Special consumption tax | `Thuế TTĐB` | tiêu thụ đặc biệt |
| Tax code | `MST` | mã số thuế; mandatory e-invoice field |
| Tax authority | `Cơ quan thuế` | |
| Tax finalisation | `Quyết toán thuế` | |
| Withholding | `Khấu trừ` | |

## Quarters and periods

`Quý I`, `Quý II`, `Quý III`, `Quý IV` — Roman numerals, capitalised `Quý`. Not `Q1`, and not
`Quý 1` in a formal statement.

```
✅  Quý IV năm tài chính 2026
❌  Q4 fiscal year 2026
❌  Quarter 4 năm 2026
```

## What is not verified here

Honest limits, so nobody encodes a guess as a rule:

- **The full account-code mapping under TT 99/2025 is not enumerated in this skill.** The
  balance-sheet rename is confirmed, and the 215x series was added while some 111x/112x
  sub-accounts were removed — but the complete list of renamed, added, and removed accounts
  needs an accountant to build. Do not infer a code from this file.
- Whether a given company may self-design its chart of accounts under TT 99/2025, and within
  what limits, is a question for its auditor.
- **IFRS adoption timing is genuinely ambiguous.** Quyết định 345/QĐ-BTC set "after 2025", but
  as of 2026 adoption remains largely voluntary rather than universally mandatory. Treat
  "IFRS is mandatory from 2026" claims with caution. This is separate from the TT 99/2025
  chart-of-accounts change, which **is** mandatory from 01/01/2026.
