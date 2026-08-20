# Deep-research brief: expanding `vietnamese-language-skill` beyond landing copy

Copy everything below the line into Claude deep research (or an equivalent long-horizon
research agent). It is self-contained.

---

## Role and objective

You are researching the design of **five new Agent Skills** for an existing open-source repo,
`trussary/vietnamese-language-skill`. The repo currently ships exactly one skill,
`vietnamese-landing-copy`, which makes Claude write native-quality Vietnamese (vi-VN)
*marketing landing-page* copy. It works. The task now is to extend the same method — documented
failure modes → reference tables → machine-checkable rules → bad→good eval pairs — into five
business functions where Vietnamese-language output is currently unguided:

1. **Marketing** (beyond the landing page)
2. **Sales**
3. **Engineering**
4. **Product**
5. **Finance**

Your deliverable is a **research report that a skill author can build from directly** — not an
essay about Vietnamese. Every section must end in something concrete: a glossary row, a lint
rule, a citation, a bad→good pair. If a claim cannot be turned into one of those four things,
cut it.

## What already exists (do not re-research this; build on it)

The existing skill establishes conventions your output must fit:

- **Register/pronoun matrix.** `quý khách` (real estate, finance, luxury, healthcare) ·
  `quý vị` (institutional/broadcast) · `anh/chị` (sales consulting, mid-market) · `bạn`
  (SaaS, tech, e-commerce, youth) · `khách hàng` (3rd-person policy prose). Never mix two
  registers in one document. The Hán-Việt ↔ thuần Việt axis controls prestige.
- **Core mechanical rules.** NFC Unicode only; one tone-mark style per document (*kiểu mới*
  `hoà`/`thuỷ` default, *kiểu cũ* `hòa`/`thủy` equally valid, mixing is the defect);
  modifier follows noun; recast English passives (`được X bởi Y` → `do Y X`); Vietnamese has
  no grammatical plural, so ICU messages carry only `other`.
- **Locale formatting.** `2.500.000 ₫` (period grouping, comma decimal), colloquial
  `2,5 tỷ` / `35 triệu/m²`, dates `dd/MM/yyyy`, phones `0xxx xxx xxx` or `+84` without the
  trunk zero, addresses small-to-large, slugs unaccented-lowercase-hyphenated.
- **Advertising law.** Luật Quảng cáo 16/2012/QH13 Điều 8 khoản 11 bans `nhất` / `duy nhất` /
  `tốt nhất` / `số một` and foreign equivalents *without licensed proof*; penalties now under
  Nghị định 87/2026/NĐ-CP Điều 50 khoản 2 (10–20M VND individuals, 20–40M organisations),
  with live 200M VND competition-law fines (Washima 22/7/2026, Cosmos Japan 22/6/2026,
  Lotte 24/6/2026). Nghị định 13/2023/NĐ-CP governs lead-form consent.
- **Repo mechanics.** `skills/<name>/SKILL.md` (YAML frontmatter `name` matching the folder,
  plus `description`; body under ~500 lines) alongside `references/` (one level deep, relative
  links must resolve), `scripts/` (**Python 3.9+, standard library only** — enforced by a test),
  and `assets/`. Blocklists live in **Markdown tables parsed at runtime** by `validate_copy.py`
  — adding a lint rule is adding a table row. Eval pairs live in `evals/pairs.jsonl` as
  `{id, category, en, bad, good, diagnosis, expected_rules}` and are executed as tests: every
  `bad` string must fire its `expected_rules`, and every `good` string must lint clean. Rule IDs
  are namespaced (`CAL001`, `LAW001`, `NUM001`, `PRO001`, …); superlatives **warn, never
  block**, and a `<!-- proof: ... -->` annotation suppresses the warning.
- **The prior research** (`research/research.md`) covers low-resource translationese, the
  tone-mark debate, NFC/NFD, the pronoun system, CTA calques, SEO slug rules, the two ad-law
  citations, and the Agent Skill spec. **Do not repeat it.** Cite it and move on.

## The core research question

For each of the five functions, answer: **what does a Vietnamese professional in that function
actually write, and what specifically goes wrong when an LLM writes it instead?**

The landing-copy skill exists because the failure modes were *specific and observable*
(`Học thêm`, `2,500,000,000 VND`, `số 1` with no proof). Vague findings ("be more formal") are
worthless. Hunt for the same grade of specificity: named artifacts, named conventions, named
wrong outputs.

## Per-function scope

Treat each of the five as a mini-investigation. The bullets are the floor, not the ceiling —
add genres you find that a Vietnamese practitioner would say are missing.

### 1. Marketing (beyond landing pages)

- **Genres:** email campaigns and newsletters; Zalo OA broadcasts and ZNS templates (a distinct,
  template-approved format with its own rules); Facebook/TikTok ad copy; TikTok Shop and
  Shopee/Lazada listings and titles; SEO long-form articles; social captions; push
  notifications; press releases (thông cáo báo chí); KOL/KOC briefs; livestream scripts.
- **Questions:** How does register shift between a Zalo broadcast and a press release? What are
  the native conventions for subject lines, preview text, hashtags, and emoji density in
  Vietnamese? What are the standardised promotional formulas (`Ưu đãi có hạn`, `Săn sale`,
  `Deal hời`, `Freeship`) and where does English code-switching read as native rather than lazy?
  How do marketplace title conventions work (keyword stacking, accented + unaccented duplicates)?
- **Regulation:** promotion/khuyến mại limits (Nghị định 81/2018/NĐ-CP — discount ceilings,
  registration duties), spam email/SMS/call rules (Nghị định 91/2020/NĐ-CP — opt-in,
  identification prefixes, sending windows), e-commerce disclosure (NĐ 52/2013, NĐ 85/2021),
  pre-approval regimes for health/food/supplement/pharma advertising, influencer-disclosure
  duties. **Verify current status as of 2026 — several of these have been amended or replaced.**

### 2. Sales

- **Genres:** cold outreach by email and Zalo; follow-up sequences; báo giá / bảng giá; proposals
  and đề xuất; sales decks; hợp đồng nguyên tắc and SOW-equivalents; biên bản nghiệm thu;
  payment-terms and dunning language; Tết and holiday greetings; meeting-request and recap
  messages; objection-handling scripts.
- **Questions:** How does B2B Vietnamese xưng hô actually work — `anh/chị` plus title, when `em`
  is correct for a junior seller, how age and seniority override role, how to address a group,
  and the safe default when seniority is unknown? What does a native Vietnamese cold email look
  like structurally versus an English one translated? How direct can a price ask or a payment
  chase be before it reads rude? What are the conventional openings and closings (`Kính gửi`,
  `Trân trọng`, `Thân mến`) and their register tiers? What contract boilerplate is standard
  (Luật Thương mại 2005, VAT terms, e-signature practice, hoá đơn GTGT language)?

### 3. Engineering

- **Genres:** commit messages; PR descriptions and code-review comments; technical design docs
  and RFCs; incident postmortems and status pages; API documentation; runbooks; READMEs; UI
  error messages and microcopy; i18n resource files.
- **Questions:** **The central one is code-switching.** Which technical terms stay English in
  native Vietnamese engineering writing (`deploy`, `commit`, `merge`, `bug`, `server`,
  `database`, `cache`, `deadline`), which have genuinely used Vietnamese equivalents (`lỗi`,
  `máy chủ`, `cơ sở dữ liệu`, `bản vá`), and which Vietnamese calques mark a document as
  machine-translated? Draw the evidence from real Vietnamese engineering writing (Viblo,
  Kipalog, VnExpress Số hoá, Vietnamese company engineering blogs, Vietnamese OSS repos) rather
  than from dictionaries. Also: register in docs (`bạn` versus impersonal), imperative mood for
  instructions, how error messages address the user, whether identifiers/branches/commit
  subjects are ever accented (they should not be), and Vietnamese-specific i18n engineering
  hazards — string-length expansion versus English, collation and diacritic-insensitive
  search/sorting, telex/VNI input handling, `vi-VN` versus `vi` tags, font subsets that break
  stacked diacritics, ICU `other`-only plurals, date/number handling in common libraries.

### 4. Product

- **Genres:** PRDs and specs; user stories and acceptance criteria; release notes and changelogs;
  in-app notifications, empty states, permission prompts, paywalls; onboarding flows; help-centre
  articles and support macros; survey instruments and NPS wording; user-interview scripts and
  discussion guides; personas; app-store listings (Vietnamese ASO).
- **Questions:** How do you write a Vietnamese survey question that does not bias the answer —
  what does Vietnamese politeness do to Likert scales and NPS, and is there a documented
  acquiescence or positivity skew among Vietnamese respondents? What pronoun should a moderator
  use in a user interview across participant ages? What is the native convention for release-note
  voice, in-app notification length, and permission-request phrasing? What are the app-store
  metadata rules for Vietnamese (character limits interacting with diacritics, accented plus
  unaccented keyword duplication)? Which product terms have settled Vietnamese forms and which
  stay English inside Vietnamese product teams (`sprint`, `backlog`, `roadmap`, `tính năng`,
  `trải nghiệm người dùng`)?

### 5. Finance

- **Genres:** invoices and hoá đơn điện tử; financial statements and management reports; budgets
  and forecasts; investor updates and board decks; pricing and payment-terms pages;
  fintech/banking/insurance product copy; loan and credit disclosures; tax filings and
  correspondence; expense policies.
- **Questions:** What is the authoritative Vietnamese chart-of-accounts and statement terminology
  (Thông tư 200/2014/TT-BTC and its successors; VAS versus IFRS naming — verify the current
  Vietnamese IFRS adoption timetable as of 2026)? What are the exact conventions for financial
  number presentation: `Đơn vị tính: triệu đồng` headers, `tỷ`/`triệu` in prose versus grouped
  digits in tables, negative numbers in parentheses, rounding, VND-versus-USD presentation,
  `năm tài chính` and quarter naming? What must an e-invoice legally say (Nghị định
  123/2020/NĐ-CP and amendments — the mandated field names and tax terminology: `thuế GTGT`,
  `TNDN`, `TNCN`, `MST`)? What claims are **restricted** in financial promotion — guaranteed-
  return language under Luật Chứng khoán 2019, SBV consumer-credit and interest-rate advertising
  rules, insurance-product disclosure duties, crypto and investment solicitation limits? This is
  the highest-legal-risk domain in the set; treat regulated phrasing as the headline finding, not
  an appendix.

## Cross-cutting questions (answer once, for all five)

1. **Architecture.** Should this be five sibling skills, fewer broader ones, or a router? Give a
   recommendation with reasoning, and propose exact `name` and `description` frontmatter for each
   skill you recommend — descriptions are the trigger signal, so make them keyword-rich and
   slightly pushy, with trigger conditions that will not collide across the five.
2. **Shared references.** The register matrix, tone-mark rule, NFC rule, and number formatting
   apply to all five, but the skill spec keeps `references/` inside each skill folder and one
   level deep, and the repo's tests enforce that relative links resolve. Research how existing
   multi-skill plugins handle shared reference material (duplication, a plugin-level shared
   directory, one skill naming another, a generated build step) and recommend one, stating the
   maintenance cost honestly.
3. **Validator reuse.** `validate_copy.py` is landing-copy shaped (registers `re|saas|formal|
   consult`). Which of its rules are universal, which need per-domain profiles, and what new rule
   families does each domain need? Propose **rule IDs, severities, and a one-line
   regex-feasibility verdict** for each — and explicitly mark rules that are *not*
   machine-checkable so they land in a human QA checklist instead.
4. **Failure-mode evidence.** For each domain, find or construct evidence of what unguided LLM
   Vietnamese actually produces. Prefer observed artifacts (forum complaints, Vietnamese
   translator and reviewer commentary, published MT-error studies, before/after rewrites) over
   speculation. Label anything you infer rather than observe.
5. **Prioritisation.** Rank the five by (value of fixing) × (density of hard, checkable rules) ÷
   (research and native-review cost). Say which to build first and why, and name any domain where
   a skill is a **bad idea** — a negative recommendation is a valid finding.

## Required output format

One Markdown report, in exactly this structure.

```
# Expanding vietnamese-language-skill: five business functions

## TL;DR                      (≤10 bullets — the decisions, not a summary)
## Recommended architecture   (skill count, names, frontmatter, shared-reference plan)
## Priority order             (ranked, with reasoning and any "do not build")

## Function: Marketing        (repeat this block verbatim for all five)
### Genre inventory           (table: artifact | who writes it | register | length/format norms)
### Register and address      (deltas from the existing matrix ONLY)
### Terminology               (EN | ❌ calque | ✅ native | register — repo table format, backticked cells)
### Regulated and banned language  (phrase | instrument | article | effective date | penalty | safe rewrite)
### Formatting conventions    (anything not already in locale-formatting.md)
### Observed failure modes    (what LLMs get wrong here, with evidence)
### Proposed lint rules       (ID | severity | what it catches | regex-feasible? | false-positive risk)
### Eval pairs                (8–12, in evals/pairs.jsonl schema, ready to paste)
### Open questions for a native speaker

## Cross-cutting findings     (the five questions above)
## Sources                    (URL | publisher | date accessed | primary/secondary | confidence)
## Caveats and what I could not verify
```

## Evidence standards

- **Search in Vietnamese.** The best sources for every one of these domains are
  Vietnamese-language. English-language sources about Vietnamese are a distant second.
- **Legal claims need the instrument number, the article (Điều/khoản), and the effective date**,
  from a primary or near-primary source (thuvienphapluat.vn, chinhphu.vn, luatvietnam.vn, the
  issuing ministry). Today is 2026 — Vietnamese law moved substantially in 2025–2026, so
  **verify every instrument you cite is still in force** and name what replaced anything that is
  not. Flag amendments whose effective date is still in the future.
- **Distinguish prescription from practice.** "A style guide says X" and "live Vietnamese sites
  do X" are different findings; when they conflict, say so and recommend which to encode.
- **Terminology needs a real attestation** — a live page, a real repo, a published document.
  Never invent a Vietnamese term to fill a table cell. An empty cell with a note is correct; a
  plausible fabrication is the worst possible output for this repo.
- **Mark confidence inline** (high/medium/low) on any row a reviewer should double-check, and
  collect everything a native speaker must sign off on into the per-domain open-questions
  section. The repo requires native-speaker approval for glossary and example changes, so that
  section is a real work queue, not a disclaimer.
- Note where a convention differs **North versus South** (Hà Nội versus TP.HCM) or by company
  type (state-owned, domestic SME, foreign-invested, startup) when it changes the wording.

## Out of scope

Do not write code, SKILL.md files, or reference files — that is the build step, and it happens
after a native speaker reviews this report. Do not restate the existing research. Do not produce
general "how to write good Vietnamese" advice untethered from a specific artifact type.
