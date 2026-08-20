<!-- vlc-disable: TONE001, DIA001, CAL001, NUM002 -->

# Channel guide — the constraints that come from the platform

The channel, not the brand, often sets the register and the format. A company whose website
says `bạn` still says `Quý khách` inside a Zalo template, because the channel reads as a
service notification rather than as marketing.

## Zalo OA — ZNS and ZBS

Zalo is the dominant messaging channel for Vietnamese business-to-consumer communication, and
it is template-gated: every message shape is pre-approved before it can be sent.

**ZNS is being replaced by ZBS Template Message from 01/01/2026.** Content written against
the old ZNS regime is stale.

| Constraint | Rule |
|---|---|
| Register | `Quý khách` or `anh/chị`, regardless of the brand's usual voice |
| Length | Body capped at **400 characters có dấu** |
| Approval | The template is approved before use; the variables are all that change |
| Content by tag | A **transactional** template may not carry marketing content |
| Diacritics | Required. Unaccented Vietnamese in a customer notification reads as spam |

The transactional/promotional split is the rule that gets violated most, usually by appending
an offer to an order confirmation:

```
❌  Đơn hàng #{order} đã được xác nhận. Ưu đãi giảm 50% hôm nay, đặt ngay!
✅  Đơn hàng #{order} của Quý khách đã được xác nhận. Dự kiến giao trước {date}.
```

The second sentence in the ❌ example gets the whole template rejected at review. Promotions
need their own template under a promotional tag, and a separate opt-in.

Rules `ZNS001` (marketing verbs in a transactional template) and `ZNS002` (over 400
characters) fire under `--doctype zns-transactional` and `--doctype zns`.

## SMS and email

Governed by Nghị định 91/2020/NĐ-CP — see [compliance.md](compliance.md) for the full table.
The operational summary:

- Advertising requires **prior opt-in**. There is no soft opt-in for a purchase.
- **SMS: 07:00–22:00. Calls: 08:00–17:00.** Outside those windows is a violation, not a
  best-practice miss.
- **≤ 3 advertising SMS per number per 24h; ≤ 1 call.**
- Every message carries a working refusal mechanism.
- Vietnamese diacritics push SMS into UCS-2: **70 characters per segment**, not 160. A
  three-segment Vietnamese message costs three times a one-segment English one.

Email: the subject line runs around 40 characters before mobile clients truncate, and the
preview text must differ from the subject — repeating it wastes the second line the inbox
gives you.

## Marketplace listings — Shopee, Lazada, TikTok Shop

Titles are a keyword string with a conventional shape, not a sentence:

```
loại sản phẩm + thương hiệu + tên/mã sản phẩm + đặc điểm chính
Giày thể thao nam Nike Air Zoom chính hãng - đế êm, size 39-44
```

| Practice | Effect |
|---|---|
| ALL-CAPS | Lowers search ranking; reads as spam |
| Emoji or icons in the title | Reads as a clone listing; risks a spam flag |
| Accented + unaccented keyword duplication | Widely practised, but **unverified** whether current ranking rewards or penalises it — see the open questions below |
| Superlatives (`tốt nhất`, `số 1`) | Regulated advertising claim, same as anywhere else |

`MKT001` flags ALL-CAPS and emoji under `--doctype marketplace-title`.

## Social and ads

- Emoji density: **1–3** in a short ad or caption reads native. Long emoji strings read as
  spam. (Practitioner norm, not a documented rule.)
- Hashtags cluster at the **end** of a caption, not inline. Mixing unaccented Vietnamese and
  English tags is normal.
- The hook belongs in the first line — Facebook and TikTok both truncate.
- Register is `bạn` for consumer brands, `anh/chị` for mid-market services.

## Livestream

The one genre where **spoken plural address** is correct and written registers read stiff.
`cả nhà`, `mọi người` are native here and nowhere else in this skill:

```
Cả nhà ơi, mã này chỉ còn 20 suất thôi nhé!
```

CTA repetition that would be excessive in written copy is normal in a livestream script.

## Press releases

Institutional third person, not direct address. The subject is the company:

```
Công ty Cổ phần ABC trân trọng thông báo ra mắt sản phẩm …
```

`Quý vị` where an audience is addressed at all. A press release written in `bạn` or `bọn mình`
is a social post wearing a press release's clothes. Standard furniture: dateline, body,
`Về [công ty]` boilerplate, media contact.

## Push notifications

40–120 characters, `bạn`, one idea, and the value visible before truncation. Vietnamese
expansion of 25–30% over English means a notification written in English and translated will
usually truncate — count the Vietnamese.

## Open questions

Flagged rather than guessed:

- Whether Shopee's current ranking rewards or penalises accented/unaccented keyword
  duplication in titles. Practitioner sources say it is done; none establish the effect.
- Current native emoji density norms for TikTok Shop versus Shopee.
- Whether `Săn sale` and `Deal hời` read as current or dated, and whether that differs
  North/South.
