# Building a `vietnamese-landing-copy` Agent Skill: Why Claude Writes Bad Vietnamese and How to Fix It

## TL;DR
- Claude's bad Vietnamese landing copy is a **predictable, fixable failure pattern**, not randomness: Vietnamese is a low-resource language, so the model defaults to English-calqued "translationese" (dịch máy), wrong pronoun/register choices, over-literal CTA translations, and broken locale formatting (VND, dates, phone). The single highest-leverage fix is a well-structured Agent Skill that bundles a terminology glossary, a register guide, a locale-formatting reference, a banned-phrase list, and scriptable validators.
- **The most valuable asset in the skill is concrete bad→good example pairs** plus a machine-checkable QA layer (Unicode NFC normalization, diacritic presence, banned-superlative check per Luật Quảng cáo, VND/number regex, forbidden-calque list). Prioritize real-estate (bất động sản) register — ornate, Hán-Việt-heavy, prestige-signaling ("quý khách", "kiến tạo", "chốn an cư đẳng cấp") — while keeping a switchable casual SaaS register ("bạn", short sentences).
- Build it to the official Anthropic/agentskills.io SKILL.md spec: a folder with SKILL.md (YAML frontmatter `name`+`description` required, body <500 lines) plus `references/`, `scripts/`, `assets/`. Ship v0 as a minimum viable skill (SKILL.md + glossary + locale reference + banned list), then v1 with validator scripts and a before/after eval set. Model the structure on `senshinji/claude-translation-skill` and Anthropic's `docx` validate-loop.

## Key Findings

1. **Why it happens — low-resource + translationese.** Vietnamese is classified as a low-resource language for LLMs. The ResearchSquare preprint "Are LLMs Good for Low-resource Vietnamese and Other Translations?" (rs-5355866) finds LLM translation "is comparable to that of traditional MT systems in some high-resource languages but lags behind significantly in low-resource languages." A well-documented failure is that unfaithful translations "tend to be highly fluent" — the output *sounds* confident but reads as machine-translated. Vietnamese-specific weaknesses: English-calqued syntax, over-literal marketing idioms, wrong/missing diacritics, and Unicode normalization (NFC vs NFD) issues that break rendering in web fonts.

2. **The register/pronoun problem is the biggest "tone" failure.** Vietnamese has no neutral "you." Choosing wrong among quý khách / quý vị / anh–chị / bạn / khách hàng instantly signals amateur copy. Luxury real estate uses "quý khách" and Hán-Việt vocabulary for prestige; SaaS/e-commerce uses "bạn" and shorter sentences.

3. **CTA/UI terms are mistranslated literally.** Native Vietnamese sites use conventional phrasings ("Đăng ký ngay", "Tìm hiểu thêm", "Xem chi tiết", "Nhận báo giá", "Đăng ký nhận thông tin") that Claude often replaces with awkward word-for-word calques.

4. **Legal constraints are real and enforced.** Luật Quảng cáo số 16/2012/QH13 (Điều 8, khoản 11) bans superlatives "nhất/duy nhất/tốt nhất/số một" (and foreign equivalents like "No.1"/"Best") without legal proof; fines run 10–20 million VND (double for organizations). Nghị định 13/2023/NĐ-CP requires explicit consent on lead-capture forms.

5. **Locale formatting is objectively wrong by default.** VND uses period as thousands separator and comma as decimal (2.500.000 ₫), colloquial prices use "tỷ/triệu" ("2 tỷ 5", "giá/m²"), dates are dd/MM/yyyy, phones use 0xxx or +84. Correct BCP-47 tag is `vi-VN`, and many Google Fonts have incomplete Vietnamese subsets that break stacked diacritics.

## Details

### PART A — Failure modes of LLM-generated Vietnamese marketing copy

**A1. Documented weaknesses.** Vietnamese is repeatedly classified as "low-resource" for LLMs. A Fortune analysis by Cecilia Hult (July 15, 2025) states that "the world's best AI models operate in English" and that "widely spoken languages like Cantonese, Vietnamese and Bahasa Indonesia are also considered low-resource"; the same piece quotes Aliya Bhatia of the Center for Democracy & Technology that when models "encounter a word they don't know... they will simply make up a translation." The translationese literature is important: translated text is "lexically and syntactically simpler," "follows a more conventional style," and is trivially distinguishable from native writing by classifiers; a key ethical finding is that "unfaithful translations often tend to be highly fluent" — dangerous for marketing because the output looks polished but reads foreign. For Vietnamese specifically, MT systems "fall back on English syntax," producing English-calqued word order.

**Diacritics and tone-mark placement (the "hòa" vs "hoà" debate).** There are two accepted conventions for placing the tone mark on diphthongs like "oa/oe/uy": the "old style" (kiểu cũ) centers the mark visually → "hòa", "thủy"; the "new style" (kiểu mới) follows phonetics → "hoà", "thuỷ", "quý". Both appear in the wild — the Vietnamese National Assembly website historically used "cộng hoà" (new) while the Government website used "cộng hòa" (old). Since ~2022, Vietnamese school textbooks use the new style ("hoá học" not "hóa học") per Bộ GD&ĐT Quyết định 1989/QĐ-BGDĐT. **Implication for the skill:** pick one convention (recommend matching modern textbook = new style, or matching the client's existing site) and enforce it consistently; inconsistency within one page is the actual defect.

**Unicode NFC vs NFD.** Vietnamese can be encoded as precomposed (NFC, single codepoint like ế U+1EBF) or decomposed/combining (NFD, base + combining marks U+0065 U+0302 U+0301). NFD can render with misplaced/detached marks in some fonts and CSS, and breaks naive string length/regex. Vietnamese font subsets in Google Fonts use ranges like `U+1EA0-1EF9, U+0300-0301, U+0303-0304, U+0308-0309, U+0323, U+0329, U+01A0-01A1, U+01AF-01B0, U+0102-0103, U+0110-0111, U+20AB` (the ₫ sign). **The skill should mandate NFC normalization of all output.**

**A2. Register/pronoun pitfalls.** Vietnamese pronouns "connote a degree of family relationship or kinship" and encode social status; "a speaker must carefully assess these factors." For landing pages:
- **quý khách** — "esteemed customer," formal/deferential; default for real estate, finance, luxury, airlines.
- **quý vị** — very formal, plural/broadcast ("ladies and gentlemen"); used for announcements, institutional.
- **anh/chị** — "brother/sister," warm-but-respectful; sales consulting, mid-market, when addressing a known-ish adult.
- **bạn** — "friend," casual peer; SaaS, tech, e-commerce, youth brands.
- **khách hàng** — "customer" (3rd-person noun, not direct address); used in policy/descriptive text.

The **Hán-Việt (Sino-Vietnamese) vs thuần Việt (pure Vietnamese)** axis controls prestige. Luxury real estate leans Hán-Việt: "kiến tạo" (create), "an cư" (settle/reside), "đẳng cấp" (class/prestige), "thịnh vượng" (prosperity), "tinh hoa" (quintessence), "biểu tượng" (symbol), "phồn vinh." Casual copy uses thuần Việt equivalents ("xây dựng", "sống", "sang"). Classifiers (căn, lô, nền, tòa) and modifier-after-noun order (căn hộ cao cấp, not cao cấp căn hộ) are frequent LLM error sites. English passive imports ("được thiết kế bởi...") are often better recast active or as "do ... thiết kế."

**A3. CTA/UI term mistranslations.** Native conventions (confirmed on Vietnamese marketing/CTA guides and live real-estate pages):

| English | ❌ Literal/bad LLM output | ✅ Native idiomatic | Register note |
|---|---|---|---|
| Get started | Bắt đầu được | Bắt đầu ngay / Dùng thử ngay | SaaS |
| Learn more | Học thêm | Tìm hiểu thêm / Xem thêm | universal |
| See details | Nhìn chi tiết | Xem chi tiết | universal |
| Read more | Đọc nhiều hơn | Đọc tiếp / Xem thêm | blog |
| Sign up | Ký lên | Đăng ký | universal |
| Register now | Đăng ký bây giờ | Đăng ký ngay | universal |
| Book a demo | Đặt một demo | Đặt lịch demo / Đăng ký trải nghiệm | SaaS |
| Contact us | Liên lạc chúng tôi | Liên hệ (với chúng tôi) | universal |
| Get a quote | Lấy báo giá | Nhận báo giá / Nhận bảng giá | real estate |
| Explore | Khám phá (ok) | Khám phá | universal |
| Coming soon | Đến sớm | Sắp ra mắt / Sắp mở bán | RE: "Sắp mở bán" |
| Trusted by | Tin tưởng bởi | Được tin dùng bởi / Đối tác của chúng tôi | universal |
| Testimonials | Lời chứng thực | Cảm nhận khách hàng / Đánh giá của khách hàng | universal |
| FAQ | — | Câu hỏi thường gặp | universal |
| Terms & Conditions | Điều khoản và Điều kiện | Điều khoản & Điều kiện / Điều khoản sử dụng | legal |
| Privacy Policy | Chính sách riêng tư | Chính sách bảo mật | legal |
| Submit | Nộp / Gửi đi | Gửi / Gửi thông tin | forms |
| Loading | Đang tải (ok) | Đang tải... | universal |
| Limited offer | Ưu đãi giới hạn | Ưu đãi có hạn / Số lượng có hạn | promo |
| Register to receive info | — | Đăng ký nhận thông tin / Đăng ký nhận tư vấn | real estate lead form |

Real-estate-specific lead CTAs seen on live templates: "Đăng ký nhận báo giá", "Đăng ký giữ chỗ", "Đặt lịch xem nhà mẫu", "Nhận thông tin dự án", "Đăng ký nhận ưu đãi".

**A4. SEO/slug conventions.** Vietnamese users frequently search *without* diacritics ("chung cu quan 7", "gia can ho vinhomes"), so pages should target both accented and unaccented keyword forms in content/meta. URL slugs are **always unaccented, lowercase, hyphen-separated**, with stop words ("và", "của", "những", "một") removed: e.g., "Căn hộ The Origami Quận 9" → `/can-ho-the-origami-quan-9`. Slugs use only `a-z`, `0-9`, `-`. Changing a slug requires a 301 redirect. Do not use underscores.

### PART B — What excellent Vietnamese landing-page copy looks like

**B5. Real-estate (bất động sản) house style.** Section-naming conventions are highly standardized across Vietnamese project landing pages: **Tổng quan dự án** (project overview), **Vị trí** (location) / **Vị trí & Liên kết vùng**, **Tiện ích** (amenities, nội khu/ngoại khu), **Mặt bằng** (floor plans, often downloadable PDF), **Thiết kế căn hộ mẫu** (model unit design), **Tiến độ** (construction progress), **Chính sách bán hàng** / **Chính sách & Ưu đãi** (sales policy/incentives), **Chủ đầu tư** (developer), **Pháp lý** (legal status), and the lead form **Đăng ký nhận thông tin / Đăng ký nhận tư vấn**. Recommended narrative order (per Vietnamese LP guides): tổng quan → điểm nổi bật → vị trí → tiện ích → mặt bằng → pháp lý → chính sách ưu đãi → form đăng ký. Tone is **ornate and prestige-signaling**: headlines like "Kiến tạo chốn an cư đẳng cấp", "Biểu tượng sống thịnh vượng", "Nơi phồn vinh hội tụ". Urgency/scarcity language: "Số lượng có hạn", "Ưu đãi mở bán", "Chỉ từ X tỷ", "Nhanh tay đặt chỗ". This differs sharply from Western SaaS tone (benefit-led, terse, casual).

**B6. SaaS/tech/e-commerce register (contrast).** Uses "bạn", short declarative sentences, thuần Việt verbs, benefit-first headlines, minimal Hán-Việt. CTAs: "Dùng thử miễn phí", "Bắt đầu ngay", "Đăng ký miễn phí". The skill must switch register by audience parameter.

**B7. Legal/compliance copy.**
- **Nghị định 13/2023/NĐ-CP (Personal Data Protection, effective 01/7/2023):** Điều 11 requires consent that is voluntary and informed, and may be given by "ticking a consent box" (đánh dấu vào ô đồng ý). Lead forms must obtain express, informed consent, link a "Chính sách bảo mật", state the purpose/scope of data use, must not sell data, and must let users withdraw consent. Standard consent line: *"Tôi đồng ý cho phép [Công ty] thu thập và xử lý thông tin cá nhân của tôi theo Chính sách bảo mật nhằm mục đích tư vấn sản phẩm/dịch vụ."*
- **Luật Quảng cáo số 16/2012/QH13 (Điều 8, khoản 11):** verbatim — *"Quảng cáo có sử dụng các từ ngữ 'nhất', 'duy nhất', 'tốt nhất', 'số một' hoặc từ ngữ có ý nghĩa tương tự mà không có tài liệu hợp pháp chứng minh theo quy định của Bộ Văn hóa, Thể thao và Du lịch."* This includes foreign equivalents ("No.1"/"Best"). Penalties are now set by Điều 50, khoản 2 of **Nghị định 87/2026/NĐ-CP** (effective 15/5/2026, superseding NĐ 38/2021): 10–20 million VND for individuals, doubled to 20–40 million VND for organizations, absent valid proof. Enforcement is real and current: the National Competition Commission (Ủy ban Cạnh tranh Quốc gia) fined **Công ty TNHH Thương hiệu Vàng Washima 200 million VND** (decision dated 22/7/2026) for the website claim "Washima - Thương hiệu ghế massage số 1 Việt Nam" under điểm a khoản 5 Điều 45 Luật Cạnh tranh 2018; parallel 200M VND fines hit Cosmos Japan Creation ("Trim Ion - sự lựa chọn số 1 của người dùng Việt", Quyết định 175/QĐ-CT, 22/6/2026) and Lotte Kid A+ (Quyết định 178/QĐ-CT, 24/6/2026). Valid proof is a market survey by a licensed research firm or an award certificate, valid 1 year. Also banned: direct comparative advertising against named competitors, and using someone's image/words without consent. Thông tư 12/2026/TT-BVHTTDL (effective 5/7/2026) clarifies proof requirements. **The banned-superlative check is therefore both a quality AND compliance feature.**

### PART C — Locale/formatting correctness

**C8. Formatting rules.**
- **Numbers/currency:** decimal separator = comma, thousands = period. `Intl.NumberFormat('vi-VN')` → "1.234.567"; with `{style:'currency', currency:'VND'}` → symbol ₫, 0 fraction digits (VND ISO-4217 minor unit = 0). Confirmed: `NumberFormatter('vi_VN')` gives grouping character "." and symbol ₫ after the number.
- **Colloquial real-estate prices:** "2 tỷ 500 triệu" / "2,5 tỷ" / "2 tỷ 5"; per-area "giá/m²", "35 triệu/m²"; "2.500.000 ₫". Live listings write "1,4 tỷ đồng (tương đương 22,5 triệu đồng/m²)", "6,7 tỷ đồng".
- **Dates:** dd/MM/yyyy. **Time:** 24h HH:mm. **Phone:** domestic 0xxx xxx xxx; international +84 (drop leading 0). **Address order:** số nhà → đường → phường → quận/huyện → tỉnh/thành phố (small-to-large).

**C9. Technical i18n.**
- **BCP-47:** use `vi` (language) or `vi-VN` (language+region). For `Intl` and HTML `lang`, `vi-VN` is safest for number/date formatting; `<html lang="vi">` is standard.
- **Fonts:** prefer fonts with a complete Vietnamese subset. **Be Vietnam Pro** is purpose-built ("refined Vietnamese letterforms with diacritics"). Google Fonts serves a `/* vietnamese */` `@font-face` with `unicode-range: U+0102-0103, U+0110-0111, U+0128-0129, U+0168-0169, U+01A0-01A1, U+01AF-01B0, U+1EA0-1EF9, U+20AB` (some add the combining-mark ranges U+0300–0329). Historically Google's subset even omitted Ỳ ỳ Ỵ ỵ Ỷ ỷ Ỹ ỹ (google/fonts issue #189) — so **verify glyph coverage**. Fonts needing `.case` marks and mark-to-mark (mkmk) attachment handle stacked diacritics (e.g., "Nguyễn"); poorly-hinted fonts collide marks with the line above.
- **Typography:** Vietnamese stacked diacritics need adequate line-height (avoid tight leading that clips marks). **`text-transform: uppercase`** is risky — must preserve diacritics (Đ, Ơ, Ư, Ế) and combining marks; verify the font's uppercase-with-diacritic glyphs. Vietnamese text is roughly comparable in length to English but Hán-Việt can be more compact; still allow ~15–20% expansion headroom in buttons.
- **`next/font/google`** historically didn't expose `unicode-range` control; ensure the `vietnamese` subset is requested.

**C10. i18n file conventions (Next.js/React).**
- **next-intl / i18next**: structure `vi.json` by page/section (e.g., `hero.title`, `cta.register`, `sections.overview.title`) so a reviewer can scan register consistency. next-intl uses `Intl.NumberFormat` under the hood (`format.number(price, {style:'currency', currency:'VND'})`).
- **Plurals:** **Vietnamese has no grammatical plural / no morphological number.** In ICU/CLDR, Vietnamese has only the `other` plural category. So ICU messages should use only `{count, plural, other {...}}` (or just interpolate `{count}` + a classifier word). Do NOT copy English `one`/`other` branches — reviewers should flag `one {}` branches in vi.json as a smell.

### PART D — Implementing it as an Anthropic Agent Skill

**D11. The spec.** Per agentskills.io/specification and anthropics/skills: a skill is a folder with a required `SKILL.md` (YAML frontmatter + Markdown body). **Required frontmatter:** `name` (max 64 chars, lowercase `a-z 0-9 -`, no leading/trailing/consecutive hyphens, must match folder name) and `description` (max 1024 chars, must state *what it does AND when to use it*). **Optional:** `license`, `compatibility` (≤500 chars), `metadata` (string map, e.g. version/author), `allowed-tools` (experimental, space-separated). Optional dirs: `scripts/` (executable), `references/` (docs loaded on demand), `assets/` (templates/fonts/data). **Progressive disclosure:** name+description (~100 tokens) preloaded for all skills; full SKILL.md body (recommend <5000 tokens / <500 lines) loaded on trigger; reference/script/asset files loaded only when needed. Keep references one level deep. Avoid `<`/`>` angle brackets in frontmatter (injection risk). Skills work across Claude Code (`~/.claude/skills/` personal, `.claude/skills/` project), Claude.ai (upload), Claude Cowork, and the API (Skills API). Validate with `skills-ref validate ./my-skill`.

**D12. Description-writing for reliable triggering.** The `description` is the primary trigger signal; Claude tends to *under*-trigger, so make it slightly "pushy" and keyword-rich, stating both function and trigger contexts. Put the key use case first (descriptions are truncated ~1024–1536 chars in listings).

**D13. Prior art / structural templates.**
- **`senshinji/claude-translation-skill`** (github.com/senshinji/claude-translation-skill) — cleanest template: `references/` holds `glossary-schema.md`, `review-feedback-schema.md`, `anti-fabrication-checklist.md`, `typesetting-rules.md`, plus shell validators `test-translation-structure.sh` and `test-skill-integrity.sh`.
- **`minruixu/translator.skill`** — `prompts/` split by mode (`native_localization.md`, `voice_transfer.md`, `terminology_grounding.md`, `quality_check.md`) + zero-dependency Python `tools/` (`glossary_manager.py`).
- **Anthropic `brand-guidelines`** (anthropics/skills) — flat single-file SKILL.md with palette/typography/voice inline; the documented template to "fork and drop in your voice and banned phrases."
- **Anthropic `docx`** — thin routing SKILL.md → reference files + `ooxml/scripts/validate.py`, with the validate-loop: "Validate immediately → if fails, fix → only proceed when validation passes." Copy this loop for the copy linter.
- **`KyaniteLabs/DialectOS`** (Apache-2.0) — localization QA with 4 weighted quality gates (token integrity, glossary fidelity, structure integrity, semantic similarity), i18n JSON `detect-missing`/placeholder-mismatch checks, and a CI GitHub Action. Strong model for the automated-QA layer.
- **agensi.io "Localization QA Auditor"** — SKILL.md that flags missing keys, placeholder mismatches, untranslated-identical-to-source, length overflow, plural-category gaps.

**D14. Validation/eval approach.** Build a small before/after eval set (10–20 pairs of bad LLM Vietnamese vs native rewrite). Scriptable automated checks: (1) **Unicode NFC normalization** (fail if any NFD codepoints); (2) **diacritic presence** (flag suspiciously ASCII-only Vietnamese words that lost tone marks); (3) **banned-superlative/compliance check** (regex for "nhất|duy nhất|tốt nhất|số một|No.?1|#1|best" without a proof annotation); (4) **forbidden-calque list** (e.g., "học thêm" for Learn more, "ký lên", "nhìn chi tiết", "lời chứng thực", "liên lạc chúng tôi"); (5) **number/currency regex** (VND must use `.` grouping, ₫ or "đồng"/"tỷ"/"triệu"; reject `,` as thousands sep); (6) **font-coverage check** (all output codepoints ∈ chosen font's Vietnamese range); (7) **plural smell** (flag ICU `one {}` in vi.json). Human rubric: register-appropriateness (pronoun/Hán-Việt match to audience), idiomaticity (no translationese), CTA conventionality, legal safety, formatting correctness.

## Recommendations

**Proposed skill (`vietnamese-landing-copy`) directory structure:**
```
vietnamese-landing-copy/
├── SKILL.md                          # router + core rules (<500 lines)
├── references/
│   ├── glossary.md                   # EN→VI terminology table (UI/CTA/RE terms) + register tags
│   ├── register-guide.md             # pronoun matrix, Hán-Việt vs thuần Việt, RE vs SaaS tone
│   ├── locale-formatting.md          # VND, dates, phone, address, Intl usage, slug rules
│   ├── banned-phrases.md             # calques + illegal superlatives (Luật Quảng cáo)
│   ├── legal-copy.md                 # NĐ 13/2023 consent lines, disclaimers
│   ├── examples.md                   # ⭐ bad→good pairs (the most valuable file)
│   └── qa-checklist.md               # human review rubric
├── scripts/
│   ├── validate_copy.py              # NFC, diacritic, banned-word, number regex, plural smell
│   └── check_font_coverage.py        # codepoints vs Vietnamese unicode-range
└── assets/
    └── vi.json.template              # sample next-intl structure w/ correct register
```

**Proposed SKILL.md frontmatter:**
```yaml
---
name: vietnamese-landing-copy
description: Writes and reviews native-quality Vietnamese (vi-VN) marketing copy for
  landing pages — especially real-estate (bất động sản) project pages, plus SaaS and
  e-commerce. Use whenever generating, translating, or reviewing Vietnamese website
  copy, headlines, CTAs, section labels, lead-form/legal text, or locale formatting
  (VND, dates, phone). Fixes translationese, wrong pronouns/register, calqued CTAs,
  illegal ad superlatives, and broken Unicode/number formatting. Trigger on any
  Vietnamese landing page, đăng ký, tiện ích, or vi.json localization task.
license: Apache-2.0
metadata:
  version: "0.1"
---
```

**SKILL.md body outline:** (1) When to use / audience-register decision tree; (2) Core rules: always NFC, pick tone-mark style, default "quý khách" for RE / "bạn" for SaaS; (3) Terminology — link glossary.md; (4) Register — link register-guide.md; (5) Formatting — link locale-formatting.md; (6) Legal — link legal-copy.md + banned-phrases.md; (7) Validate-loop: after writing, run `scripts/validate_copy.py`, fix failures, only ship when it passes (copy the docx pattern); (8) Point to examples.md.

**Phased rollout:**
- **v0 (MVP, ~1 day):** SKILL.md + glossary.md + register-guide.md + locale-formatting.md + banned-phrases.md + examples.md (10 bad→good pairs). No scripts yet — rules only. This alone fixes the majority of complaints.
- **v0.5:** add legal-copy.md, qa-checklist.md, vi.json template.
- **v1 (with evals):** add `validate_copy.py` + `check_font_coverage.py`, wire the mandatory validate-loop, expand examples.md to 25+ pairs, add a 20-query trigger eval (should/should-not-trigger) to tune the description. Optional: adopt DialectOS-style weighted QA gates.
- **Change thresholds:** if the skill under-triggers, make the description pushier/add keywords; if the validator false-positives on legitimate copy (e.g., "duy nhất" in a proven claim), add a proof-annotation escape hatch; if a new register emerges (e.g., government/institutional), add a register profile.

**Concrete example pairs to seed examples.md:**
- ❌ "Học thêm về dự án của chúng tôi" → ✅ "Tìm hiểu thêm về dự án"
- ❌ "Chúng tôi cung cấp những căn hộ tốt nhất số 1 thị trường" (illegal + calqued) → ✅ "Không gian sống đẳng cấp giữa lòng thành phố"
- ❌ "Được thiết kế bởi các kiến trúc sư hàng đầu" (passive calque) → ✅ "Do đội ngũ kiến trúc sư hàng đầu kiến tạo"
- ❌ "Giá: 2,500,000,000 VND" → ✅ "Giá chỉ từ 2,5 tỷ đồng"
- ❌ "Liên lạc chúng tôi ngay hôm nay!" → ✅ "Liên hệ ngay để nhận tư vấn"
- ❌ "Đăng ký lên để nhận thông tin" → ✅ "Đăng ký nhận thông tin dự án"

## Caveats
- Tone-mark style (hòa vs hoà) has no single legal standard; the skill must let the user pick and then enforce consistency — do not treat one as "wrong."
- Superlative rules: the law does not *forbid* "số 1"/"tốt nhất" outright — it forbids them *without valid proof*. The validator should flag, not hard-block, and allow a documented-proof exception. Penalty basis is now Nghị định 87/2026/NĐ-CP (from 15/5/2026), replacing NĐ 38/2021; the underlying ban itself dates to Luật Quảng cáo 2012, so the rule is long-standing while the citation and enforcement have been refreshed.
- The Washima/Cosmos/Lotte fines were levied under competition law (Luật Cạnh tranh 2018) as well as advertising law, showing self-declared "số 1" claims carry live, six-figure-VND risk.
- Marketplace skills cited (agensi.io) are paid listings; their feature specs are inspiration, not verified source. Exact current file layout of Anthropic `brand-guidelines` was partly confirmed via mirrors (GitHub tree pages block automated fetch) — all sources agree it is a flat single-file skill.
- LLM Vietnamese quality is improving and varies by model/version; the skill is a durable mitigation regardless, because register/locale/legal conventions are stable even as raw fluency improves.