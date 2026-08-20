<!-- vlc-disable: LAW001, DIA001, CAL001, NUM002 -->

# Promotion and advertising law for campaigns

The cross-cutting rules — superlatives, consent, anti-spam windows, the 50% discount ceiling,
influencer disclosure — are in [compliance.md](compliance.md), which every skill in this repo
shares. **Read that first.** This file covers only what campaign and outbound writing has to
do differently.

## The 50% ceiling in practice

Nghị định 81/2018/NĐ-CP as amended by Nghị định 128/2024/NĐ-CP caps a discount at **50%** of
the pre-promotion price, rising to 100% only inside a `chương trình khuyến mại tập trung`.

The copy consequence is specific: **a headline number over 50 is a compliance question, not a
creative one.**

```
❌  Giảm giá 90% toàn bộ sản phẩm
✅  Giảm đến 50% toàn bộ sản phẩm
✅  Giảm đến 90% — Chương trình khuyến mại tập trung  <!-- khuyen-mai-tap-trung: QĐ 123/SCT -->
```

`MKT002` flags a discount over 50% and is suppressed by a
`<!-- khuyen-mai-tap-trung: ... -->` annotation naming the programme, exactly as
`<!-- proof: ... -->` suppresses a superlative. The annotation does not create the
registration; it records that one exists.

`Giảm đến 50%` (up to 50%) and `Giảm 50%` (50% off) are different claims. `đến` covers a range
where only some items reach the ceiling; without it, every item must.

## Anti-spam: the operational rules

Full citations in [compliance.md](compliance.md). What a campaign writer needs on the page:

- **Opt-in before any advertising message.** A purchase is not consent to marketing.
- **SMS 07:00–22:00, calls 08:00–17:00.** Schedule accordingly.
- **≤ 3 advertising SMS per number per 24h, ≤ 1 call.**
- **Every message needs a working refusal mechanism.** In SMS, that is a real instruction, not
  a footer nobody can act on.

`SPAM001` looks for an opt-out marker in a document declared `--doctype bulk-message`. It is a
weak check with real false positives, which is why it is doctype-gated and advisory — the
substantive check is on the QA checklist.

## Influencer and KOL/KOC briefs — new for 2026

Luật Quảng cáo sửa đổi 2025 (Luật 75/2025/QH15) adds an express disclosure duty from
**01/01/2026**: content conveying paid advertising must be identifiable as such, and the
person must actually have used the product they endorse.

A brief written before 2026 that says "mention naturally, don't make it feel like an ad" is
now instructing the creator to break the law. Every brief must specify:

- the disclosure wording the creator will use (`Quảng cáo`, `Tài trợ bởi …`, `#quangcao`);
- where it appears — visible without expanding a caption;
- confirmation the creator has used the product;
- what claims they may not make.

This is `MKT004`: not machine-checkable, and on the QA checklist.

## Sector pre-approval

Health, food supplement, pharmaceutical, cosmetic, and medical-service advertising needs
content approval before publication, and therapeutic claims are restricted regardless of
approval. This skill does not lint it. If the product is in one of those categories, the copy
goes to the sector regulator before it goes to media buying.

Common failure: a supplement ad written in ordinary marketing language
(`giúp khỏi bệnh`, `điều trị tận gốc`) that is a therapeutic claim in law.

## Superlatives

Identical to the rest of the repo. `nhất`, `duy nhất`, `số 1`, `hàng đầu`, `#1`, `No.1` are
prohibited without documentary proof under Luật Quảng cáo 16/2012/QH13 Điều 8 khoản 11.

The campaign-specific note: **`bán chạy nhất` is a superlative.** So is `được yêu thích nhất`.
Sales-rank claims are exactly what the statute is about, and marketplace listings are full of
them.

```
❌  Sản phẩm bán chạy nhất thị trường
✅  Sản phẩm bán chạy         (no ranking claim)
✅  Top 3 sản phẩm bán chạy trên Shopee tháng 6/2026  <!-- proof: Shopee seller dashboard -->
```

## Comparative advertising

Directly naming a competitor to compare against is prohibited, and enforcement here is real
and current. Compare against your own previous version, or against an unnamed baseline:

```
❌  Nhanh hơn [Đối thủ] 2 lần
✅  Nhanh hơn phiên bản trước 2 lần
```

Also prohibited: using a person's image, name, or words in advertising without their consent.

## Prices in promotional copy

The formatting rules are in [locale-formatting.md](locale-formatting.md). The compliance-side
point: a "was/now" price claim requires the "was" price to be the genuine pre-promotion price.
An inflated anchor is a separate violation from the discount ceiling, and the two are usually
found together.
