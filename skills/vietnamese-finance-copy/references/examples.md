<!-- vlc-disable: all -->
<!-- GENERATED FILE — do not edit by hand.
     Source: evals/vietnamese-finance-copy/pairs.jsonl. Regenerate with: python tools/build_examples.py -->

# Examples — bad to good

The highest-value file in this skill. Each pair names the failure mode it fixes; the
diagnosis generalizes further than the string does. Read this before writing anything
long in Vietnamese.

Every ❌ string here is a deliberate defect, so this file is exempt from its own linter.

**24 pairs.** Contributions welcome — see [CONTRIBUTING.md](../../../CONTRIBUTING.md).

## Regulated advertising claims and legal copy

### The highest interest rate on the market

❌ **Lãi suất cao nhất thị trường**

✅ **Lãi suất cạnh tranh, từ 5,8%/năm**

A regulated ranking claim under Luật Quảng cáo Điều 8 khoản 11. Publishing the rate is both more persuasive and legal.

<sub>id: `fin-superlative-rate` · caught by: `LAW001`</sub>

## Locale formatting

### Revenue 2,500,000,000 VND

❌ **Doanh thu 2,500,000,000 VND**

✅ **Doanh thu 2.500.000.000 ₫ (2,5 tỷ đồng)**

Vietnamese groups with periods. In a finance document the US format is a factor-of-a-thousand ambiguity, not a style slip.

<sub>id: `fin-number-format` · caught by: `NUM001`</sub>

### Loss of 1,234 million

❌

```text
Đơn vị tính: triệu đồng

| Lợi nhuận sau thuế | -1.234 |
```

✅

```text
Đơn vị tính: triệu đồng

| Lợi nhuận sau thuế | (1.234) |
```

Statements write negatives in parentheses. A minus sign mid-column is read as a typo or missed entirely.

<sub>id: `fin-negative-parens` · caught by: `FIN006`</sub>

### Statement table without a unit header

❌

```text
| Chỉ tiêu | Số tiền |
|---|---|
| Doanh thu | 2.500 |
```

✅

```text
Đơn vị tính: triệu đồng

| Chỉ tiêu | Số tiền |
|---|---|
| Doanh thu | 2.500 |
```

Without `Đơn vị tính` the reader cannot tell a million from a billion, and 2.500 is ambiguous by a factor of a thousand.

<sub>id: `fin-unit-header` · caught by: `FIN005`</sub>

### Revenue figures in a table column

❌

```text
| Quý III | 2,5 tỷ |
| Quý IV | 2.500.000.000 |
```

✅

```text
Đơn vị tính: tỷ đồng

| Quý III | 2,5 |
| Quý IV | 2,5 |
```

A column that alternates between the colloquial scale and grouped digits cannot be read or summed. Prose takes `tỷ`; tables take a declared unit.

<sub>id: `fin-mixed-scale` · caught by: _not machine-detectable_</sub>

## Register

### Statement addressed to the customer

❌ **Bạn vui lòng kiểm tra sao kê tài khoản.**

✅ **Quý khách vui lòng kiểm tra sao kê tài khoản.**

`bạn` never appears in a statement, invoice, disclosure, or loan document. The register floor in finance is `Quý khách` or impersonal third person.

<sub>id: `fin-register-ban` · caught by: `PRO002`</sub>

## Finance and regulated financial copy

### Guaranteed 12% annual return

❌ **Cam kết lợi nhuận 12%/năm cho nhà đầu tư**

✅ **Lợi nhuận kỳ vọng 12%/năm. Đầu tư có rủi ro; kết quả trong quá khứ không đảm bảo kết quả trong tương lai.**

Guaranteed-return language in investment solicitation. Prohibited via Luật Chứng khoán Điều 12, NĐ 155/2020 and NĐ 38/2018 Điều 2 khoản 4 — assembled from three instruments, which is why the rule warns and routes to legal review rather than blocking.

<sub>id: `fin-guaranteed-return` · caught by: `FIN001`</sub>

### A risk-free investment

❌ **Kênh đầu tư không rủi ro, bảo toàn vốn 100%**

✅ **Sản phẩm phù hợp với nhà đầu tư có khẩu vị rủi ro thấp. Vốn đầu tư không được bảo đảm.**

Two prohibited claims in one line. `bảo toàn vốn` is a guarantee even when hedged with a percentage.

<sub>id: `fin-risk-free` · caught by: `FIN001`</sub>

### 0% interest installment

❌ **Trả góp lãi suất 0% cho mọi đơn hàng**

✅ **Trả góp lãi suất 0% — phí chuyển đổi 3%/khoản. Tổng chi phí phải trả: 10.300.000 ₫.**

TT 43/2016/TT-NHNN as amended by TT 18/2019 requires the fee schedule and calculation method to be published. A 0% headline without the fees that replace it is the documented consumer-harm case.

<sub>id: `fin-zero-interest` · caught by: `FIN002`</sub>

### Balance sheet

❌ **Bảng cân đối kế toán tại ngày 31/12/2026**

✅ **Báo cáo tình hình tài chính tại ngày 31/12/2026**

Renamed by Thông tư 99/2025/TT-BTC, in force 01/01/2026, replacing TT 200/2014. Every model writing from pre-2026 data produces the old name.

<sub>id: `fin-balance-sheet` · caught by: `CAL001`</sub>

### VAT invoice for a customer

❌

```text
Hóa đơn bán hàng

Tổng tiền: 8.250.000
```

✅

```text
Hóa đơn giá trị gia tăng

MST: 0123456789
Thuế suất GTGT: 10%
Tiền thuế GTGT: 750.000
Tổng cộng tiền thanh toán: 8.250.000
```

MST and the GTGT lines are mandatory e-invoice fields under NĐ 123/2020 as amended by NĐ 70/2025. An invoice missing them is rejected.

<sub>id: `fin-invoice-fields` · caught by: `FIN007`</sub>

### Investment-linked insurance pitch

❌ **Vừa bảo hiểm vừa sinh lời chắc chắn, tiền đẻ ra tiền**

✅ **Sản phẩm bảo hiểm liên kết đầu tư. Kết quả đầu tư không được đảm bảo và do bên mua bảo hiểm chịu rủi ro.**

Selling an investment-linked policy as a savings product. TT 67/2023 Điều 53 requires an explicit statement that it is an insurance product, plus risk disclosure.

<sub>id: `fin-investment-linked` · caught by: `FIN001`, `CAL001`</sub>

### Buy crypto on our platform

❌ **Đầu tư crypto sinh lời trên sàn quốc tế uy tín**

✅ **Giao dịch tài sản số chỉ thực hiện qua tổ chức được Bộ Tài chính cấp phép theo Nghị quyết 05/2025/NQ-CP. Tài sản số không phải là phương tiện thanh toán hợp pháp.**

Solicitation outside the NQ 05/2025 pilot. Digital assets are recognised as tài sản số under Luật 71/2025 from 01/01/2026 but are not legal tender.

<sub>id: `fin-crypto-solicitation` · caught by: `CAL001`</sub>

### Q4 fiscal year 2026

❌ **Quarter 4 fiscal year 2026**

✅ **Quý IV năm tài chính 2026**

Vietnamese statements use Roman numerals with a capitalised `Quý`, and `năm tài chính` rather than a borrowed English phrase.

<sub>id: `fin-quarter-naming` · caught by: _not machine-detectable_</sub>

### Personal income tax withheld

❌ **Thuế thu nhập cá nhân (PIT) đã khấu trừ**

✅ **Thuế TNCN đã khấu trừ**

The standard abbreviation is TNCN. Importing the English abbreviation reads as a translated document.

<sub>id: `fin-pit-abbreviation` · caught by: `CAL001`</sub>

### Owner's equity

❌ **Sự công bằng của chủ sở hữu**

✅ **Vốn chủ sở hữu**

`sự công bằng` is *fairness* — the other sense of the English word. A polysemy failure that no spellcheck catches because the output is a real Vietnamese phrase.

<sub>id: `fin-equity-polysemy` · caught by: `CAL001`</sub>

### Principal and interest

❌ **Hiệu trưởng và lãi**

✅ **Tiền gốc và lãi**

`hiệu trưởng` is a school principal. Same polysemy failure, and more visibly absurd only because the wrong sense is concrete.

<sub>id: `fin-principal-polysemy` · caught by: `CAL001`</sub>

### Interest rate

❌ **Tỷ lệ quan tâm**

✅ **Lãi suất**

*Interest* rendered in its attention sense. The output is fluent Vietnamese meaning something else entirely.

<sub>id: `fin-interest-rate-polysemy` · caught by: `CAL001`</sub>

### Cash flow statement

❌ **Báo cáo dòng chảy tiền mặt**

✅ **Báo cáo lưu chuyển tiền tệ**

A literal rendering of the English metaphor. The statement has an official name.

<sub>id: `fin-cash-flow` · caught by: `CAL001`</sub>

### Getting rich is easy

❌ **Làm giàu không khó, ai cũng có thể đầu tư**

✅ **Sản phẩm phù hợp với nhà đầu tư đã đánh giá khẩu vị rủi ro.**

Classic solicitation framing. Suitability is a regulated concept, and `ai cũng có thể đầu tư` asserts its opposite.

<sub>id: `fin-get-rich` · caught by: `CAL001`</sub>

### Bank statement

❌ **Tuyên bố ngân hàng tháng 8**

✅ **Sao kê tài khoản tháng 8**

*Statement* rendered in its declaration sense. `sao kê` is the banking term.

<sub>id: `fin-bank-statement` · caught by: `CAL001`</sub>

### Collateral required

❌ **Yêu cầu tài sản phụ**

✅ **Yêu cầu tài sản bảo đảm**

`tài sản phụ` reads as a secondary or minor asset. The legal term is `tài sản bảo đảm`.

<sub>id: `fin-collateral` · caught by: `CAL001`</sub>

### Audited financial statements

❌ **Báo cáo tài chính đã kiểm tra sổ sách**

✅ **Báo cáo tài chính đã kiểm toán**

`kiểm tra sổ sách` describes an activity; `kiểm toán` names the statutory process. Only one of them means the statements can be filed.

<sub>id: `fin-audit` · caught by: `CAL001`</sub>

### Withdraw any time with no fee

❌ **Rút vốn bất cứ lúc nào không mất phí**

✅ **Phí rút trước hạn: 1% giá trị rút, áp dụng trong 12 tháng đầu.**

Almost always false, and the fee it conceals is exactly what the transparency rules exist to surface. State the fee.

<sub>id: `fin-no-withdrawal-fee` · caught by: `CAL001`</sub>
