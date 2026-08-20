<!-- vlc-disable: LAW001, DIA001, CAL001, NUM002 -->

# Financial promotion — the regulated phrasing

**The highest-legal-risk file in this repo.** Everything here carries statutory consequences
rather than reputational ones, and several of the rules prohibit phrasings that read as
ordinary marketing enthusiasm.

**This is a copywriting reference, not legal advice.** Its purpose is to get copy to legal
review already clean of the known problems. It does not replace that review, and several
entries below explicitly route to it.

## Guaranteed returns

| Prohibited | Instrument |
|---|---|
| `cam kết lợi nhuận`, `cam kết lãi suất`, `lợi nhuận X%/năm` presented as certain, `đầu tư không rủi ro`, `bảo toàn vốn 100%`, `chắc chắn sinh lời` | Luật Chứng khoán 54/2019/QH14 (as amended by Luật 56/2024/QH15) Điều 12; Nghị định 155/2020/NĐ-CP (as amended by NĐ 245/2025); Nghị định 38/2018/NĐ-CP Điều 2 khoản 4 for startup investment funds |

```
❌  Cam kết lợi nhuận 12%/năm
✅  Lợi nhuận kỳ vọng 12%/năm. Đầu tư có rủi ro; kết quả trong quá khứ không đảm bảo
    kết quả trong tương lai.
```

**`FIN001` is a warning, not an error, and this is deliberate.** No single article states the
prohibition verbatim — it is assembled from the anti-fraud and solicitation provisions of Luật
Chứng khoán Điều 12, the disclosure-content rules in NĐ 155/2020, and the express ban for
startup funds in NĐ 38/2018. A hard block would be over-claiming a legal position the sources
do not support in one place. **Route every `FIN001` finding to legal review** rather than
editing around it.

Also prohibited: mixing a **disclosure** document with advertising or solicitation content.
Regulatory disclosures under NĐ 155/2020 are their own document and must not carry marketing.

## Interest-rate and consumer-credit copy

| Requirement | Instrument |
|---|---|
| Publicly posted rate framework, fee schedule, and calculation method for consumer credit | Thông tư 43/2016/TT-NHNN as amended by Thông tư 18/2019/TT-NHNN, Điều 9 and 10a |
| No misleading rate headline | Luật Quảng cáo, plus the transparency duty above |

The `lãi suất 0%` headline is the specific case, and Vietnamese consumer reporting has
documented the harm it causes — a 0% rate advertised without the fees that replace it.

```
❌  Trả góp lãi suất 0%
✅  Trả góp lãi suất 0% — phí chuyển đổi 3%/khoản. Tổng chi phí phải trả: 10.300.000 ₫.
```

`FIN002` flags `lãi suất 0%` or `0đ` with no fee or total-cost disclosure nearby. It has a real
false-positive rate — a document may disclose the cost several paragraphs later — so it is a
warning and the substantive check is on the QA checklist.

Note that enforcement of the 0% headline is uneven and the practice is widespread. That is not
a defence; it is a reason the copy is likely to reach a customer before anyone objects.

## Insurance

| Requirement | Instrument |
|---|---|
| No false or misleading insurance advertising | Luật Kinh doanh bảo hiểm 08/2022/QH15 (as amended by Luật 139/2025) Điều 9; Điều 129 khoản 3 |
| Investment-linked products: mandatory risk disclosure, an explicit statement that the product **is an insurance product**, session recording, and a 60-day bank-channel restriction | Thông tư 67/2023/TT-BTC Điều 53 |

The failure mode is copy that sells an investment-linked policy as a savings or investment
product:

```
❌  Vừa bảo hiểm vừa sinh lời chắc chắn
✅  Sản phẩm bảo hiểm liên kết đầu tư. Kết quả đầu tư không được đảm bảo và do bên mua
    bảo hiểm chịu rủi ro.
```

Whether a given disclosure is **complete** is `FIN008` — not machine-checkable, and on the QA
checklist.

## Crypto and digital assets

The position as of 2026, stated carefully because it changed recently:

- Crypto is legally recognised as **`tài sản số`** under Luật Công nghiệp công nghệ số 2025
  (Luật 71/2025/QH15, Chương V), effective 01/01/2026.
- It is **not legal tender**. Copy implying it can be used as money is wrong.
- Issuance, trading, and solicitation are permitted **only within the pilot** under Nghị quyết
  05/2025/NQ-CP, through providers licensed by the Bộ Tài chính. Penalties under Nghị định
  284/2026/NĐ-CP apply from 01/09/2026.

```
❌  Đầu tư crypto sinh lời trên sàn quốc tế
✅  Giao dịch tài sản số chỉ thực hiện qua tổ chức được Bộ Tài chính cấp phép theo
    Nghị quyết 05/2025/NQ-CP. Tài sản số không phải là phương tiện thanh toán hợp pháp.
```

Whether the platform being promoted is actually licensed is `FIN009` — a fact about the world,
not about the text.

## Superlatives

The general rule applies unchanged, and finance is a category where it is broken constantly:
`lãi suất cao nhất thị trường`, `ngân hàng số 1`, `app đầu tư hàng đầu`. All regulated under
Luật Quảng cáo 16/2012/QH13 Điều 8 khoản 11, all fire `LAW001`.

```
❌  Lãi suất cao nhất thị trường
✅  Lãi suất cạnh tranh, từ 5,8%/năm
```

A rate is a number. Publishing it is both more persuasive and legal.

## Register

Finance is `Quý khách` or impersonal third person, effectively without exception. `bạn` appears
only in youth-facing fintech, and even there the money screens skew formal. A statement,
disclosure, or invoice is never addressed to a `bạn`.

## What routes to a lawyer regardless of what the linter says

- Any document soliciting investment from the public.
- Any insurance product description, especially investment-linked.
- Any consumer-credit rate presentation.
- Any crypto or digital-asset promotion.
- Any `FIN001` finding, without exception.

The linter's job here is to catch the phrasings that are known problems. It cannot tell you
whether a disclosure is complete, whether a licence exists, or whether an expected return is
defensible.
