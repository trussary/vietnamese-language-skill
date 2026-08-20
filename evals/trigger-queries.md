# Trigger eval

The `description` in each `SKILL.md` is the only signal Claude uses to decide whether to load
that skill. Claude tends to **under**-trigger, so descriptions are deliberately keyword-dense.
This file is how we know whether they work.

With several Vietnamese skills in one repo there is a second failure mode beyond
under-triggering: the **wrong** skill loading, or two loading at once. Every section below
therefore has a should-NOT-trigger list that includes the neighbouring skills' territory, and
`tests/test_trigger_keywords.py` fails the build if two descriptions claim the same keyword.

## How to run

1. Install the skills in a **fresh session** with no other Vietnamese context loaded.
2. Send each prompt below verbatim, one per session (context bleeds between turns).
3. Record which skill loaded, if any. In Claude Code, a loaded skill shows in the transcript
   as a Skill tool call.
4. Score: **target ≥ 18/20 correct per skill.** A prompt that loads the wrong skill counts as
   a failure for both. Log the result in `CHANGELOG.md` for the release.

If a skill under-triggers, add the missed keywords to its description. If it over-triggers on
the should-not list, the description is claiming territory it does not cover — tighten the
scope words rather than deleting keywords wholesale. If two skills fire on one prompt, the
split is wrong, not the wording.

---

# `vietnamese-landing-copy`

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
this skill would *degrade* by imposing a marketing register. Prompt 11 should now load
`vietnamese-tech-writing` instead — if this skill fires on it, the two descriptions overlap.

---

# `vietnamese-tech-writing`

## Should trigger (10)

| # | Prompt | Why it should |
|---|---|---|
| 1 | Viết commit message tiếng Việt cho thay đổi này | Core case: commit conventions, prompt in Vietnamese |
| 2 | Translate this technical manual into Vietnamese | Technical documentation, the register this skill owns |
| 3 | Dịch error message này sang tiếng Việt cho app | UI microcopy, user-facing register |
| 4 | Write a postmortem in Vietnamese for yesterday's outage | Impersonal register, blameless conventions |
| 5 | Review our Vietnamese README — does it read natural to a VN dev? | Code-switching naturalness |
| 6 | Should we translate "deploy" and "commit" in our Vietnamese docs? | The central code-switching question |
| 7 | Localize this app's `vi.json` — check the ICU plurals | i18n mechanics and the other-only plural rule |
| 8 | Write Vietnamese release notes for version 2.4 | Release notes register and tense |
| 9 | Draft a Vietnamese NPS survey for our mobile app | Survey wording and acquiescence bias |
| 10 | Our Vietnamese app-store subtitle is getting truncated — rewrite it | String expansion and platform limits |

## Should NOT trigger (10)

| # | Prompt | Why it should not |
|---|---|---|
| 11 | Viết landing page cho dự án căn hộ tại Quận 7 | Marketing copy — `vietnamese-landing-copy` owns this |
| 12 | Write a Vietnamese cold email to a prospect | Sales outreach — `vietnamese-business-comms` owns this |
| 13 | Format this Vietnamese invoice with the right VAT fields | Finance — `vietnamese-finance-copy` owns this |
| 14 | Write a commit message for this change | No Vietnamese in scope |
| 15 | Set up next-intl in my Next.js app | i18n plumbing with no Vietnamese copy |
| 16 | Explain Vietnamese tone marks to me | Linguistics question, not a writing task |
| 17 | Review my Python code for bugs | Unrelated |
| 18 | Summarize this Vietnamese news article | Reading comprehension, not authoring |
| 19 | What's the difference between NFC and NFD Unicode? | General Unicode question, no Vietnamese artifact |
| 20 | Deploy my app to production | An instruction to act, not to write |

Prompts 11–13 are the ones that matter: they are the neighbouring skills' territory, and a
hit on any of them means the descriptions have started competing.

---

## Results log

| Date | Skill | Version | Score | Notes |
|---|---|---|---|---|
| _not yet run_ | vietnamese-landing-copy | 1.0.0 | — | Run before tagging a release |
| _not yet run_ | vietnamese-tech-writing | 1.0.0 | — | Run before tagging a release |
