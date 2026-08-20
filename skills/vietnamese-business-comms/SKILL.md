---
name: vietnamese-business-comms
description: Writes and reviews native-quality Vietnamese (vi-VN) marketing and sales copy — email campaigns and newsletters, Zalo OA ZNS/ZBS templates, Facebook and TikTok ads, Shopee and Lazada listings, SEO articles, social captions, push notifications, press releases, KOL/KOC briefs, livestream scripts, cold outreach, follow-up sequences, báo giá and quotes, proposals, payment reminders, and Tết greetings. Use when drafting Vietnamese promotional, outbound, or B2B sales content, choosing anh/chị versus bạn, or checking khuyến mại discount limits, anti-spam windows, influencer disclosure, and advertising-law compliance. For website hero and section copy, use vietnamese-landing-copy instead.
license: MIT
metadata:
  version: "1.0.0"
  repository: "https://github.com/trussary/vietnamese-language-skill"
---

# Vietnamese marketing and sales copy (vi-VN)

Campaign and outbound copy fails in two directions at once. It fails **commercially** by
reading as a mass mailing — wrong pronoun, translated CTA, formal vocabulary where the market
uses loanwords. And it fails **legally**, because Vietnamese advertising law regulates ordinary
marketing enthusiasm: unproven superlatives, discounts over 50%, messages sent outside the
legal window, and, from 01/01/2026, undisclosed influencer content.

Both failures are invisible to a fluency check. Every rule below exists to stop a specific one.

## Step 1 — The channel picks the register, not the brand

Vietnamese has no neutral "you", and in this skill the choice is made by **where the message
lands** rather than by the brand's usual voice.

| Channel or genre | Register | Address |
|---|---|---|
| Zalo ZNS/ZBS template | `zns` | `Quý khách` — even for a brand that says `bạn` everywhere else |
| B2B cold email, quote, proposal, dunning | `b2b` | `anh/chị`, self as `em` or `tôi` |
| E-commerce, social, ads, push | `saas` | `bạn` |
| Mid-market services, consulting | `consult` | `anh/chị` |
| Press release | `press` | Institutional third person, `Quý vị` if anyone |
| Livestream script | `livestream` | `cả nhà`, `mọi người` — spoken register |

**`bạn` in B2B outreach is the single clearest tell of an automated send.** No Vietnamese
salesperson opens a cold email with `Chào bạn`.

Who you are in the sentence — `em` versus `tôi`, and why age outranks job title —
**[references/b2b-xung-ho.md](references/b2b-xung-ho.md)**. The shared pronoun matrix:
**[references/register-matrix.md](references/register-matrix.md)**.

## Step 2 — Core rules (non-negotiable, no file hop needed)

1. **Never `bạn` or `mình` in B2B outreach, a quote, or a dunning notice.** `anh/chị` for
   them; `em` if you are plausibly junior, `tôi` otherwise.
2. **Open with courtesy, not with the pitch.** Vietnamese cold outreach puts a line of context
   before the ask. An English-style first-line value proposition reads rude.
3. **Never write `nhất`, `số 1`, `duy nhất`, `hàng đầu`, `bán chạy nhất` as an unproven
   claim.** Illegal under Điều 8 khoản 11 Luật Quảng cáo 16/2012/QH13, with current fines.
   `bán chạy nhất` is a ranking claim like any other.
4. **A discount over 50% needs a registered `chương trình khuyến mại tập trung`.** NĐ 81/2018
   as amended by NĐ 128/2024. A headline number over 50 is a compliance question.
5. **No marketing content in a transactional Zalo template.** It gets the template rejected.
   ZNS/ZBS bodies cap at **400 characters có dấu**.
6. **Advertising messages need prior opt-in, a working opt-out, and the legal window** — SMS
   07:00–22:00, calls 08:00–17:00, ≤3 SMS and ≤1 call per number per 24h.
7. **Use market vocabulary, not formal translations.** `Freeship`, `Deal`, `Voucher`,
   `Mua ngay`. `Học thêm` means *take extra classes* and is never a CTA.
8. **Never name a competitor in a comparison**, and never use a person's image, name, or words
   without consent.

## Step 3 — Look up the conventional wording

Calques with settled native equivalents (`trích dẫn` → `báo giá`, `theo lên` → `theo dõi`,
`lời chào tốt nhất` → `Trân trọng`), the e-commerce vocabulary the market actually uses, sales
artifact names, and CTAs by register:

**[references/glossary.md](references/glossary.md)** — machine-readable, so every row is a
lint rule.

Phrases that mark a mass mailing, plus the health and outcome claims that are never
permissible: **[references/banned-phrases.md](references/banned-phrases.md)**.

## Step 4 — Respect the channel's mechanics

Each channel imposes hard limits that copy has to be written into, not trimmed to afterwards:
the ZNS 400-character cap and transactional/promotional split, marketplace title conventions
(no ALL-CAPS, no emoji), SMS at **70 characters per segment** once diacritics force UCS-2,
email subject truncation, emoji density, and the livestream spoken register.

**[references/channel-guide.md](references/channel-guide.md)**

## Step 5 — Get the campaign legally clean

The 50% ceiling and its `<!-- khuyen-mai-tap-trung: ... -->` exemption, anti-spam windows, the
KOL/KOC disclosure duty new from 01/01/2026, comparative-advertising limits, and sector
pre-approval for health and supplement claims:

**[references/promo-law.md](references/promo-law.md)** — and
**[references/compliance.md](references/compliance.md)** for the cross-cutting citations shared
with every Vietnamese skill.

Financial promotion — `cam kết lợi nhuận`, `lãi suất 0%`, investment products — is **not
handled here**. Route it to `vietnamese-finance-copy` and to legal review.

## Step 6 — Format numbers, dates, and prices correctly

VND groups with periods and decimalizes with commas: `2.500.000 ₫`. Prose uses `2,5 tỷ` and
`35 triệu`, tables use grouped digits, and the two are never mixed in one context. Dates are
`dd/MM/yyyy`. Phones are `0xxx xxx xxx` or `+84` with the trunk zero dropped.

**[references/locale-formatting.md](references/locale-formatting.md)**, plus
**[references/unicode-and-tone.md](references/unicode-and-tone.md)** for NFC and the tone-mark
consistency rule.

## Step 7 — Validate, fix, then ship

**Run the validator immediately after writing. If it reports errors, fix them and run again.
Only present the copy once it passes.**

```bash
python scripts/validate_copy.py campaign.md --register saas
python scripts/validate_copy.py outreach.md --doctype cold-outreach --register b2b
python scripts/validate_copy.py template.txt --doctype zns-transactional
python scripts/validate_copy.py title.txt --doctype marketplace-title
```

- **`--doctype` is what turns on the structural rules**, and they stay silent without it:
  `zns`, `zns-transactional`, `marketplace-title`, `cold-outreach`, `bao-gia`, `dunning`,
  `bulk-message`, `promo`. `--list-rules` prints everything this skill can emit.
- `--register zns|b2b|press|livestream|saas|consult|…` enables `PRO002`.
- Exit `0` = clean or warnings only. Exit `1` = errors that must be fixed.
- `--json` for machine-readable findings; `--strict` to fail on warnings too.
- `--fix` rewrites NFC violations in place; every other rule is a human judgement call.

Two annotations suppress a legal warning where the paperwork genuinely exists. Neither creates
the paperwork:

```markdown
Thương hiệu số 1 Việt Nam <!-- proof: Khảo sát Nielsen VN 2026, chứng chỉ 123/NS -->
Giảm đến 90% <!-- khuyen-mai-tap-trung: QĐ 123/SCT ngày 01/06/2026 -->
```

## Step 8 — Learn from the worked pairs, then hand it to a human

**[references/examples.md](references/examples.md)** — read the bad→good corpus before writing
anything long.

Then run the checklist. The linter cannot tell you whether the xưng hô fits this particular
recipient, whether a KOL actually used the product, whether an opt-in genuinely exists, or
whether a `<!-- proof: -->` annotation has anything behind it. Those are the four checks that
matter most: **[references/qa-checklist.md](references/qa-checklist.md)**
