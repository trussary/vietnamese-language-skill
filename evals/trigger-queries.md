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

# `vietnamese-business-comms`

## Should trigger (10)

| # | Prompt | Why it should |
|---|---|---|
| 1 | Viết email chào hàng tiếng Việt gửi khách doanh nghiệp | Core case: B2B cold outreach, prompt in Vietnamese |
| 2 | Write a Vietnamese cold email to a prospect | Same, in English |
| 3 | Soạn mẫu ZNS xác nhận đơn hàng cho Zalo OA | Zalo template, transactional tag |
| 4 | Viết tiêu đề sản phẩm cho gian hàng Shopee | Marketplace listing conventions |
| 5 | Làm báo giá tiếng Việt cho khách, có VAT | Quote structure and VAT treatment |
| 6 | Is a 70% discount legal in a Vietnamese promotion? | The khuyến mại ceiling |
| 7 | Write a polite payment reminder in Vietnamese | Dunning register and escalation |
| 8 | Draft a Vietnamese press release for our product launch | Institutional register |
| 9 | Viết caption TikTok tiếng Việt cho chiến dịch sale | Social copy, emoji and hashtag norms |
| 10 | What must a Vietnamese KOL disclose in a sponsored post? | Luật 75/2025 disclosure duty |

## Should NOT trigger (10)

| # | Prompt | Why it should not |
|---|---|---|
| 11 | Viết landing page cho dự án căn hộ tại Quận 7 | `vietnamese-landing-copy` owns website page copy |
| 12 | Write a Vietnamese commit message for this change | `vietnamese-tech-writing` owns it |
| 13 | Format this Vietnamese invoice with the right VAT fields | `vietnamese-finance-copy` owns invoices |
| 14 | Can we advertise a guaranteed 12% annual return? | Financial promotion — finance skill plus legal |
| 15 | Write a cold email to a prospect | No Vietnamese in scope |
| 16 | How do I set up a Zalo OA account? | Platform ops question, not copy |
| 17 | What is the VAT rate in Vietnam? | Tax question, not copy |
| 18 | Summarize this Vietnamese news article | Reading comprehension, not authoring |
| 19 | Translate this contract into Vietnamese | Legal drafting, not commercial writing |
| 20 | Review my Python code for bugs | Unrelated |

Prompts 11–14 are the routing tests. Prompt 14 is the sharpest: it is marketing in form and
regulated financial promotion in substance, and it must go to the finance skill.

---

# `vietnamese-finance-copy`

## Should trigger (10)

| # | Prompt | Why it should |
|---|---|---|
| 1 | Lập hóa đơn GTGT tiếng Việt cho khách doanh nghiệp | Core case: e-invoice fields |
| 2 | Dịch báo cáo tài chính sang tiếng Việt | Statement terminology under TT 99/2025 |
| 3 | What is the balance sheet called in Vietnamese in 2026? | The TT 99/2025 rename |
| 4 | Can we advertise a guaranteed 12% annual return in Vietnam? | Guaranteed-return prohibition |
| 5 | Viết copy cho sản phẩm vay trả góp lãi suất 0% | Interest-rate transparency |
| 6 | Write Vietnamese copy for our investment-linked insurance product | TT 67/2023 disclosure duties |
| 7 | Format this Vietnamese P&L table — units and negatives | Statement formatting conventions |
| 8 | Soạn thông báo thuế TNCN gửi nhân viên | Tax terminology and abbreviations |
| 9 | Is it legal to promote a crypto exchange to Vietnamese users? | NQ 05/2025 pilot and licensing |
| 10 | Viết bản công bố thông tin cho quỹ đầu tư | Disclosure document, no solicitation content |

## Should NOT trigger (10)

| # | Prompt | Why it should not |
|---|---|---|
| 11 | Viết landing page cho dự án căn hộ tại Quận 7 | `vietnamese-landing-copy`, even though property involves money |
| 12 | Làm báo giá gửi khách hàng | `vietnamese-business-comms` owns quotes |
| 13 | Write a Vietnamese commit message | `vietnamese-tech-writing` |
| 14 | Viết email khuyến mãi giảm 30% | Campaign copy — business-comms |
| 15 | Create a VAT invoice | No Vietnamese in scope |
| 16 | What is the corporate tax rate in Vietnam? | A tax-rate question, not a writing task |
| 17 | Explain how VAT works | Explanatory, not authoring |
| 18 | Build me a spreadsheet model | Modelling, not copy |
| 19 | Summarize this Vietnamese annual report | Reading comprehension, not authoring |
| 20 | Review my Python code for bugs | Unrelated |

Prompts 12 and 14 are the sharpest routing tests in the repo. A quote and a promotional email
both contain money and VAT, and both belong to `vietnamese-business-comms`. The dividing line
is that this skill owns **regulated financial content** — statements, invoices, and financial
promotion — not every document with a price in it.

---

# `vietnamese-education-copy`

## Should trigger (10)

| # | Prompt | Why it should |
|---|---|---|
| 1 | Viết nhận xét học bạ cho học sinh lớp 9 môn Toán | Core case: secondary report-card remark |
| 2 | Soạn sổ liên lạc gửi phụ huynh về buổi họp tuần tới | Parent-facing school communication |
| 3 | Write the syllabus for an undergraduate economics course | University syllabus (đề cương) |
| 4 | Dịch bảng điểm đại học này sang tiếng Việt, kiểm tra định dạng GPA | Transcript and GPA locale formatting |
| 5 | A student lost their diploma — what can the university legally reissue? | Diploma-reissuance terminology |
| 6 | Draft a Vietnamese absence notice from a teacher to a parent | Disciplinary/absence notice register |
| 7 | What's the correct way for a teacher to address a 3rd grader in Vietnamese? | Primary vs. secondary pronoun choice |
| 8 | Viết thông báo đăng ký học phần cho sinh viên năm nhất | University registration announcement |
| 9 | Review this Vietnamese report card — does it use the right grading terms? | Statutory grading-term check |
| 10 | Soạn lời nhận xét cuối năm cho học sinh tiểu học | Primary-school qualitative assessment |

## Should NOT trigger (10)

| # | Prompt | Why it should not |
|---|---|---|
| 11 | Write the onboarding flow copy for our language-learning app | EdTech product UI — `vietnamese-tech-writing` |
| 12 | Viết quảng cáo Facebook cho trung tâm luyện thi IELTS | Tutoring-centre advertising — `vietnamese-business-comms` |
| 13 | Translate the subtitles for this online course video | E-learning subtitles — `vietnamese-tech-writing` |
| 14 | Soạn tin nhắn Zalo quảng bá khóa học tiếng Anh giảm 30% | Marketing campaign — `vietnamese-business-comms` |
| 15 | Format this Vietnamese tuition invoice with VAT fields | Regulated finance — `vietnamese-finance-copy` |
| 16 | Viết landing page giới thiệu trường mầm non | Landing-page marketing — `vietnamese-landing-copy` |
| 17 | What year was the current Vietnamese national curriculum introduced? | A history question, not a writing task |
| 18 | Review my Python grading script for bugs | Unrelated |
| 19 | Summarize this Vietnamese education news article | Reading comprehension, not authoring |
| 20 | Explain how Vietnamese university credit hours work | Explanatory, not authoring |

Prompts 11–14 are the sharpest routing tests here: an EdTech app, a tutoring ad, a course
subtitle, and a course-promotion broadcast all mention "học" or "khóa học" the way a genuine
school document does, but none of them are school or academic administration — they are
software UI, advertising, and localization wearing an education topic, and belong to the two
skills that already own those registers.

---

## Results log

| Date | Skill | Version | Score | Notes |
|---|---|---|---|---|
| _not yet run_ | vietnamese-landing-copy | 1.0.0 | — | Run before tagging a release |
| _not yet run_ | vietnamese-tech-writing | 1.0.0 | — | Run before tagging a release |
| _not yet run_ | vietnamese-business-comms | 1.0.0 | — | Run before tagging a release |
| _not yet run_ | vietnamese-finance-copy | 1.0.0 | — | Run before tagging a release |
| _not yet run_ | vietnamese-education-copy | 1.0.0 | — | Run before tagging a release |
