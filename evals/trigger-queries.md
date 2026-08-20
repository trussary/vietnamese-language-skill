# Trigger eval

The `description` in `SKILL.md` is the only signal Claude uses to decide whether to load this
skill. Claude tends to **under**-trigger, so the description is deliberately keyword-dense.
This file is how we know whether it works.

## How to run

1. Install the skill in a **fresh session** with no other Vietnamese context loaded.
2. Send each prompt below verbatim, one per session (context bleeds between turns).
3. Record whether the skill loaded. In Claude Code, a loaded skill shows in the transcript as
   a Skill tool call.
4. Score: **target ≥ 18/20 correct.** Log the result in `CHANGELOG.md` for the release.

If it under-triggers, add the missed keywords to the description. If it over-triggers on the
should-not list, the description is claiming territory it does not cover — tighten the scope
words rather than deleting keywords wholesale.

## Should trigger (10)

| # | Prompt | Why it should |
|---|---|---|
| 1 | Viết landing page cho dự án căn hộ cao cấp tại Quận 7 | Core case: Vietnamese real-estate landing page |
| 2 | Translate our pricing page into Vietnamese for a SaaS audience | Translation into vi with an explicit register |
| 3 | Review this `vi.json` for register consistency | i18n file review |
| 4 | Our Vietnamese hero copy reads like Google Translate — fix it | Translationese, named without jargon |
| 5 | What should the CTA button say in Vietnamese for a lead form? | CTA conventions |
| 6 | Format these prices for a Vietnamese property listing | VND and colloquial tỷ/triệu formatting |
| 7 | Write the consent line for a Vietnamese lead capture form | Nghị định 13 legal copy |
| 8 | Is "Thương hiệu số 1 Việt Nam" safe to put on our homepage? | Advertising-law check |
| 9 | Đặt tên các section cho trang bán hàng dự án bất động sản | Real-estate section labels, prompt in Vietnamese |
| 10 | Localize this marketing site to vi-VN | Explicit locale tag |

## Should NOT trigger (10)

| # | Prompt | Why it should not |
|---|---|---|
| 11 | Translate this technical manual into Vietnamese | Not marketing copy — different register entirely |
| 12 | How do I say thank you in Vietnamese? | Casual language question, no page involved |
| 13 | Write a landing page for our SaaS product | No Vietnamese in scope |
| 14 | Set up next-intl in my Next.js app | i18n plumbing, no Vietnamese copy |
| 15 | Explain Vietnamese tone marks to me | Linguistics question, not a writing task |
| 16 | Fix the CSS on our pricing page | Unrelated |
| 17 | What is the VAT rate in Vietnam? | Tax question, not copy |
| 18 | Summarize this Vietnamese news article | Reading comprehension, not authoring |
| 19 | Write a Vietnamese poem for my mother | Vietnamese, but not marketing copy |
| 20 | Review my Python code for bugs | Unrelated |

Prompts 11, 18, and 19 are the interesting ones: all three are Vietnamese-language tasks that
this skill would *degrade* by imposing a marketing register. If it fires on those, the
description is over-claiming.

## Results log

| Date | Skill version | Score | Notes |
|---|---|---|---|
| _not yet run_ | 1.0.0 | — | Run before tagging a release |
