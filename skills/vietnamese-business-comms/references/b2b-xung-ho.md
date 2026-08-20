<!-- vlc-disable: TONE001, DIA001, CAL001 -->

# B2B xưng hô — how to address a business counterpart

The biggest register gap in this repo, and the one an LLM gets wrong most reliably. The
shared matrix in [register-matrix.md](register-matrix.md) covers *which* pronoun a register
uses. This file covers the harder question: which pronoun **you** are, when writing to
someone whose age and seniority you may not know.

## The default

**`anh/chị` for them, and for yourself either `em` or `tôi`.**

`bạn` in B2B outreach is an instant tell of automated origin. No Vietnamese salesperson opens
a cold email to a company with `Chào bạn`. It reads as either a mass mailing or a peer
addressing a peer, and in a commercial context it costs the deal before the pitch starts.

| Their position | Address them as | Refer to yourself as |
|---|---|---|
| Unknown, first contact | `anh/chị` | `em` if you are plausibly younger, `tôi` otherwise |
| Clearly senior or older | `anh` / `chị` | `em` |
| Peer, similar age and level | `anh` / `chị` | `tôi` or `mình` |
| A group, mixed | `anh/chị` or `Quý anh/chị` | `chúng tôi` |
| A company, in formal writing | `Quý công ty` / `Quý khách` | `chúng tôi` / `bên em` |

`anh/chị` written with the slash is standard when the recipient's gender is unknown, and is
not a fudge — it is the conventional written form.

## `em` is not self-deprecation

A junior seller writing `em xin gửi anh báo giá` is using the register correctly. English
instinct reads `em` (younger sibling) as diminishing yourself; Vietnamese does not. It signals
appropriate deference in a commercial relationship and makes the message *more* credible, not
less.

The mistake in the other direction is real too: a senior person writing `em` to a junior buyer
reads as odd or sarcastic.

## Age and seniority override role

This is the rule that surprises people:

- A **junior buyer who is visibly older** than you still gets `anh/chị`, and you may still use
  `em`. Age wins.
- A **senior seller writing to a junior buyer** uses `anh/chị` for them anyway — the customer
  relationship outranks the age gap in the other direction.
- When both signals conflict and you genuinely cannot tell, `anh/chị` + `tôi` is the safe pair.
  It is slightly formal and never wrong.

`bên em` / `bên anh` (our side / your side) is a useful hedge that keeps the register warm
without committing to a personal pronoun: `bên em sẽ gửi hợp đồng trong hôm nay`.

## Openings, by formality

| Opening | Formality | Use when |
|---|---|---|
| `Kính gửi anh/chị …` | Highest | Cold first contact, formal proposals, anything to a title you do not know |
| `Dear anh/chị …` | Mid | Accepted in Vietnamese business email, common in multinationals and tech |
| `Chào anh/chị …` | Warm | An established relationship, a second or third touch |
| `Anh/chị ơi` | Casual | Zalo chat with someone you already work with — never in email |

`Dear` really is used in Vietnamese business email. It is not an error to correct.

## Closings

| Closing | Use when |
|---|---|
| `Trân trọng` | The formal default. Correct in almost every case. |
| `Trân trọng cảm ơn` | Slightly warmer, after the other party has done something |
| `Thân mến` / `Thân` | An established, friendly relationship only |
| `Best regards` | Acceptable in a bilingual thread |

`Thân mến` to a cold prospect is a register error — it claims a closeness that does not exist.
And `Lời chào tốt nhất` is not a closing; it is `Best regards` run through a dictionary.

## Structure: relationship before the ask

Native Vietnamese cold outreach is **more relational up front** than the English equivalent.
The English convention of leading with the value proposition in the first line reads abrupt
to the point of rudeness.

The conventional three-part shape:

1. **Mở** — greeting, who you are, and one line of context or courtesy.
2. **Thân** — the actual proposition, kept short.
3. **Kết** — a specific, low-commitment next step, then `Trân trọng`.

```
Kính gửi anh Minh,

Em là Lan, phụ trách giải pháp doanh nghiệp tại Công ty ABC. Em được biết bên anh
đang mở rộng hệ thống bán lẻ tại khu vực phía Nam.

Bên em có giải pháp quản lý kho phù hợp với quy mô này, hiện đang được khoảng 200
chuỗi bán lẻ sử dụng. Em xin phép gửi anh tài liệu tóm tắt trong file đính kèm.

Nếu thuận tiện, anh cho em xin 15 phút trao đổi trong tuần này được không ạ?

Trân trọng,
Lan
```

The courtesy line in paragraph one is not padding. Removing it is what makes translated
outreach read cold.

## Dunning: polite but firm, and escalating

Payment chasing keeps `Quý khách` or `anh/chị` throughout. It never becomes an imperative to a
`bạn`. Firmness comes from specificity — a named date, a named amount — not from tone.

| Stage | Wording |
|---|---|
| First reminder | `Bên em xin phép nhắc anh/chị về khoản thanh toán … đến hạn ngày …` |
| Second | `Kính đề nghị Quý khách thanh toán trước ngày [X].` |
| Final | `Trường hợp chưa nhận được thanh toán trước ngày [X], bên em buộc phải tạm dừng dịch vụ theo điều khoản hợp đồng.` |

`Bạn phải trả tiền ngay lập tức` is not firm. It is rude, and in Vietnamese business culture
it ends the relationship rather than accelerating the payment.

## Tết and holiday greetings

Formulaic by design. Do not innovate.

```
Kính chúc Quý khách và gia đình một năm mới An khang – Thịnh vượng – Vạn sự như ý.
```

`Chúc mừng năm mới bạn nhé!` is a message to a friend, not to an account.

## What the linter can and cannot do

`SALES001` flags `bạn` in a document declared `--doctype cold-outreach`, `bao-gia`, or
`dunning`. It cannot judge whether `em` or `tôi` was the right self-reference for a particular
recipient — that needs the age and seniority context only the writer has. It goes on the QA
checklist as a human check.
