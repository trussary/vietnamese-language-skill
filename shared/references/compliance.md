<!-- vlc-disable: TONE001, DIA001 -->

# Compliance — the cross-cutting legal reference

Shared by every skill in this repo. Vietnamese commercial writing is regulated in ways that
English-language copy practice does not prepare you for: some phrasings that read as ordinary
marketing enthusiasm are administrative violations with current, issued fines.

**This is a copywriting reference, not legal advice.** It exists so that copy arrives at legal
review already clean of the obvious problems, not so that it can skip legal review.

There is deliberately **no separate "Vietnamese legal" skill**. Compliance is not a genre
anyone sits down to write — it is a constraint on every genre, so it lives here and every
skill loads it.

## Advertising superlatives — the rule every skill inherits

**Điều 8 khoản 11, Luật Quảng cáo 16/2012/QH13** prohibits advertising that uses
`nhất`, `duy nhất`, `tốt nhất`, `số một` or equivalent wording **without lawful documentary
proof**.

The prohibition is on the *unproven* claim, not the word. A licensed market survey or an award
certificate makes `số 1` legal. This is why `LAW001` warns and never blocks, and why the
`<!-- proof: ... -->` annotation suppresses it:

```markdown
Thương hiệu số 1 Việt Nam <!-- proof: Khảo sát Nielsen VN 2026, chứng chỉ số 123/NS -->
```

Idiomatic `nhất` (`nhất là`, `trước nhất`) is not a superlative claim. Expect occasional
false positives and suppress them per line rather than disabling the rule.

## Personal data and consent — Nghị định 13/2023/NĐ-CP

Any form collecting a name, phone number, or email needs **express, informed, revocable**
consent that states the purpose and links a `Chính sách bảo mật`. Silence, pre-ticked boxes,
and bundled consent are not consent.

Marketing consent is **separate** from service consent: agreeing to be contacted about an
order is not agreement to receive campaigns. Collect them as two checkboxes, not one.

## Unsolicited messaging — Nghị định 91/2020/NĐ-CP

| Constraint | Rule |
|---|---|
| Consent | Opt-in required before any advertising message |
| SMS window | 07:00–22:00 |
| Voice-call window | 08:00–17:00 |
| Frequency | ≤ 3 advertising SMS per number per 24h; ≤ 1 call per 24h |
| Opt-out | Every message must carry a working refusal mechanism |
| Penalty | Điều 32 — up to 80–100 million VND for organisations breaching the DoNotCall list (individuals half) |

## Promotions and discounts — Nghị định 81/2018/NĐ-CP, amended by 128/2024/NĐ-CP

The discount ceiling is **50%** of the pre-promotion price. It rises to **100%** only inside a
`chương trình khuyến mại tập trung` (a concentrated promotion programme, state-organised or
state-acknowledged).

> *"Mức giảm giá tối đa đối với hàng hóa, dịch vụ được khuyến mại không được vượt quá 50% giá
> hàng hóa, dịch vụ đó ngay trước thời gian khuyến mại… Trong trường hợp tổ chức chương trình
> khuyến mại tập trung… áp dụng mức giảm tối đa… là 100%."*

NĐ 128/2024 has been in force since 01/12/2024.

## Influencer disclosure — Luật 75/2025/QH15, from 01/01/2026

The 2025 amendment to Luật Quảng cáo adds an express duty on KOL/KOC and anyone conveying paid
advertising: **disclose that the content is advertising or sponsored**, and do not endorse a
product you have not actually used. This is new law — content written against pre-2026
practice is stale.

## Sector pre-approval

Health, food-supplement, pharmaceutical, cosmetic, and medical-service advertising requires
sector-specific content approval before publication, and therapeutic claims are restricted
regardless. No skill in this repo attempts to lint that. Route it to the sector regulator.

## Financial promotion

Financial content carries its own statutory surface — guaranteed-return prohibitions,
interest-rate transparency, insurance disclosure. It is deliberately **not** summarised here,
because a partial summary is more dangerous than none. See the finance skill's
`financial-promotion.md`.

## What is not verified

Honesty about the evidence base, so that nobody encodes an unverified figure as a hard rule:

- **NĐ 87/2026/NĐ-CP penalty amounts** for advertising violations are carried over from an
  earlier research brief and have **not** been re-verified against the primary decree. Do not
  quote specific figures from it to a client.
- The prohibition on `cam kết lợi nhuận` in fund materials is **assembled** from Luật Chứng
  khoán Điều 12, NĐ 155/2020 and NĐ 38/2018 — no single article states it verbatim. That is
  why `FIN001` is a warning that routes to legal review, not an error.
- Marketplace and app-store keyword practices (accented/unaccented duplication) are
  **platform policy, not law**, and sources conflict on whether current ranking rewards or
  penalises them. Treated as an open question throughout this repo.

## Reviewer note

Any change to a citation in this file — instrument number, article, effective date, penalty —
needs a source link in the pull request. Legal content that nobody can trace back to
`thuvienphapluat.vn` or an official gazette does not get merged.
