<!-- vlc-disable: DIA001, CAL001 -->

# Survey and research writing

The one finding in this skill that is a **measurement** hazard rather than a copy hazard, and
the reason it is worth a reference of its own: a badly worded Vietnamese survey does not read
wrong. It reads fine and returns numbers that are wrong, which is far more expensive.

## Acquiescence bias

Respondents tend to agree with whatever statement they are shown. Krosnick's handbook puts
the average acquiescence effect at roughly **10 percentage points** — across ten studies, 52%
agreed with an assertion while only 42% disagreed with its opposite.

This is not specific to Vietnam, but Vietnamese survey practice runs into it constantly,
because the agree/disagree format is the one an LLM reaches for by default and because
politeness norms make outright disagreement with a written statement uncomfortable.

**Consequence: never use an agree/disagree scale.** Not `Bạn có đồng ý…` with
`Đồng ý / Không đồng ý`, ever.

## Use item-specific scales

Ask about the thing itself, with the endpoints naming the property being measured.

```
❌  Bạn có đồng ý rằng ứng dụng dễ sử dụng không?
    ( ) Rất đồng ý  ( ) Đồng ý  ( ) Không đồng ý  ( ) Rất không đồng ý

✅  Mức độ dễ sử dụng của ứng dụng?
    ( ) Rất khó  ( ) Khó  ( ) Bình thường  ( ) Dễ  ( ) Rất dễ
```

The second version cannot be answered by agreeing, so agreement bias has nowhere to attach.

## Label every point

Numeric-only scales (`1 – 5`) are interpreted inconsistently, and the direction is not
obvious to every respondent. Label every option, and keep the labels evenly spaced in
meaning — `Rất khó / Khó / Bình thường / Dễ / Rất dễ`, not `Khó / Bình thường / Dễ / Rất dễ /
Tuyệt vời`.

## NPS

NPS is a **0–10** scale. It is not a yes/no question, and converting it to one destroys the
metric.

```
❌  Bạn có giới thiệu chúng tôi cho bạn bè không? (Có / Không)
✅  Khả năng bạn giới thiệu [App] cho bạn bè hoặc đồng nghiệp? (0 – 10)
```

Treat any Vietnamese NPS number as **not comparable** to a regional benchmark without local
calibration. Positivity norms shift the distribution, and the standard promoter/detractor
cut-offs were not derived on a Vietnamese sample. Compare a Vietnamese NPS to your own
previous Vietnamese NPS, and nothing else.

## Do not lead the question

```
❌  Tính năng mới rất tiện lợi, bạn thấy thế nào?
✅  Bạn thấy tính năng mới thế nào?

❌  Bạn thích điểm nào nhất ở sản phẩm?
✅  Bạn thấy sản phẩm có điểm nào đáng chú ý — tốt hoặc chưa tốt?
```

The second pair is the subtler one: asking what the respondent *likes* presupposes that they
like something. Every question that assumes an answer gets it.

## Interview register follows the participant

A moderator guide written entirely in `bạn` is wrong for older participants, and one written
entirely in `anh/chị` is stilted with peers. Write the guide with the address marked as a
variable and brief the moderator to choose:

```
[XƯNG HÔ: anh/chị nếu người tham gia lớn tuổi hơn, bạn nếu ngang tuổi]
Hôm nay [xưng hô] có thể kể lại lần gần nhất [xưng hô] dùng ứng dụng không?
```

Getting this wrong costs data, not just politeness: a participant addressed too casually by a
younger moderator gives shorter answers.

## Consent

A research consent notice is a personal-data notice under Nghị định 13/2023/NĐ-CP — see
[compliance.md](compliance.md). State the purpose, say whether the session is recorded, and
make withdrawal possible. `Bạn đồng ý tham gia chứ?` is not consent copy.

## What the linter can and cannot do

`PROD002` catches literal agree/disagree wording in a document declared with
`--doctype survey`. It cannot tell whether a question is leading, whether a scale is
balanced, or whether the sample makes sense. Those go to the QA checklist and to a human.
