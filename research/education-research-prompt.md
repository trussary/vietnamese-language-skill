# Deep-research brief: adding an education skill to `vietnamese-language-skill`

Copy everything below the line into Claude deep research (or an equivalent long-horizon
research agent). It is self-contained.

---

## Role and objective

You are researching whether and how to add **a sixth Vietnamese-language domain — Education —**
to the open-source repo `trussary/vietnamese-language-skill` (v2.0.0). The repo currently ships
four Agent Skills, each making Claude write native-quality vi-VN copy for one business function:

| Skill | Covers |
|---|---|
| `vietnamese-landing-copy` | Real-estate, SaaS, e-commerce landing pages |
| `vietnamese-tech-writing` | Engineering + product docs (commits, PRDs, RFCs, i18n, surveys) |
| `vietnamese-business-comms` | Marketing + sales (email, Zalo, ads, marketplace, press, outreach) |
| `vietnamese-finance-copy` | Regulated finance (invoices, statements, investor updates, credit) |

Education was **never scoped in the prior expansion research** (`exnpansion-research.md`, which
covered only Marketing/Sales/Engineering/Product/Finance). Your job is to do for Education what
that report did for those five: produce a **research report a skill author can build from
directly**, using the exact method this repo already runs on — documented failure modes →
reference tables → machine-checkable rules → bad→good eval pairs. Every section must end in
something concrete: a glossary row, a lint rule, a citation, a bad→good pair. If a claim cannot
become one of those four things, cut it.

## What already exists (do not re-research this; build on it)

- **Register/pronoun matrix** (`shared/references/register-matrix.md`). `quý khách` (real
  estate, finance, luxury, healthcare) · `quý vị` (institutional/broadcast) · `anh/chị`
  (sales, mid-market) · `bạn` (SaaS, tech, e-commerce, youth) · `khách hàng` (3rd-person policy
  prose). Education needs its **own address terms** not yet in this matrix — `thầy/cô` ↔ `em`
  (teacher-to-student), `thầy/cô` ↔ `con` (younger children, or from a teacher senior in age),
  `quý phụ huynh` (school-to-parent), `bạn` (peer-to-peer, EdTech apps), `sinh viên` (3rd-person,
  higher-ed admin prose) — treat mapping these onto or extending the shared matrix as a required
  deliverable, not an aside.
- **Core mechanical rules** (`shared/references/unicode-and-tone.md`,
  `shared/references/locale-formatting.md`): NFC-only Unicode; one tone-mark style per document
  (*kiểu mới* `hoà`/`thuỷ` default, *kiểu cũ* `hòa`/`thủy` equally valid, mixing is the defect);
  modifier follows noun; no grammatical plural (ICU `other` only); `dd/MM/yyyy` dates;
  `2.500.000 ₫` grouping.
- **Compliance engine** (`shared/references/compliance.md`): Luật Quảng cáo 16/2012/QH13 Điều 8
  khoản 11 (superlative ban, `nhất`/`duy nhất`/`tốt nhất`/`số một` without licensed proof),
  Nghị định 87/2026/NĐ-CP penalties, Nghị định 13/2023/NĐ-CP consent requirements. Education
  advertising (luyện thi centers, du học consultancies, private tutoring) will trigger this
  engine directly — verify whether it needs education-specific additions rather than a new file.
- **Repo mechanics, current state (v2.0.0):**
  - `skills/<name>/SKILL.md` (YAML frontmatter `name` matching the folder, plus a keyword-dense
    `description` — the *only* signal the description-based triggering test
    `tests/test_trigger_keywords.py` uses to prevent two skills from claiming the same keyword);
    body under ~500 lines; `references/` one level deep with resolvable relative links;
    `scripts/` (Python 3.9+, stdlib only, enforced by `tests/test_scripts_are_stdlib_only.py`);
    `assets/`.
  - `shared/` is the single source of truth for the register matrix, tone/Unicode rules, locale
    formatting, compliance, and the validator engine itself; `tools/sync_shared.py` copies it
    into each skill folder (`--check` fails CI on drift). A new domain reuses `shared/`, it does
    not fork it.
  - `scripts/validate_copy.py` is byte-identical across skills. It loads three kinds of data at
    runtime, so nothing domain-specific lives in the Python file itself: calque/superlative
    blocklists from `references/glossary.md` and `references/banned-phrases.md`; register
    profiles from `references/register-matrix.md`; and a domain hook — any sibling
    `scripts/rules_<domain>.py` is imported for logic-shaped rules (character counts, number
    parsing) that a Markdown table can't express. A `--doctype` flag gates rules that are only
    correct for one artifact type (see `vietnamese-tech-writing`'s `rules_tech.py` and
    `--doctype commit` for the existing pattern to follow).
  - Suppression directives (`<!-- vlc-disable: RULE_ID -->`, `<!-- proof: ... -->`) work in any
    comment syntax already; superlative-class rules warn, never block.
  - `evals/pairs.jsonl` holds one JSONL corpus per skill:
    `{id, category, en, bad, good, diagnosis, expected_rules}`, run as tests — every `bad` fires
    its `expected_rules`, every `good` lints clean under the skill's own registers.
    `evals/trigger-queries.md` holds 20 should-trigger/should-not-trigger prompts per skill,
    scored against a ≥18/20 target, specifically to catch a new skill stealing another's
    territory (or vice versa).
  - Packaging is already multi-skill: `npx skills add`, a Claude Code plugin manifest
    (`.claude-plugin/marketplace.json`, currently describing four skills), a plain skill folder,
    and a claude.ai zip.
- **Prior research** (`research/research.md`, `research/exnpansion-research.md`,
  `research/expansion-plan.md`) covers low-resource translationese, the tone-mark debate,
  NFC/NFD, the pronoun system, CTA calques, the two ad-law citations, the Agent Skill spec, and
  the decision to fold Product into `vietnamese-tech-writing` rather than ship it standalone
  (its checkable surface was too thin). **Do not repeat any of this. Cite it and move on.**

## The core research question

**What does a Vietnamese person writing *inside the education system* actually write, and what
specifically goes wrong when an LLM writes it instead?** "Education" spans at least four
different writers — a K-12 teacher, a university admin office, an EdTech product team, and a
tutoring-center marketer — who do not share a register, an audience, or a regulator. Do not
treat "education" as one voice. The existing skills exist because their failure modes were
*specific and observable* (`Học thêm`, `2,500,000,000 VND`, `số 1` with no proof). Hunt for the
same grade of specificity here: named artifacts, named conventions, named wrong outputs — not
"be more respectful to teachers."

## Scope

Investigate all of the following sub-areas. The bullets are the floor, not the ceiling — add
genres a Vietnamese educator, student, or EdTech PM would say are missing.

### 1. K-12 school communications

- **Genres:** sổ liên lạc / school-to-parent notifications (paper, Zalo, SMS, app-based —
  VNEDU, Enetviet, K12Online, and similar platforms actually used in Vietnamese schools);
  học bạ (report card) remarks and grading comments; disciplinary and absence notices;
  permission slips and consent forms for field trips; announcements for exam schedules,
  tuition/fee notices, and school events; teacher-to-parent one-on-one messages.
- **Questions:** What is the exact register and structure of a `sổ liên lạc` entry versus a
  Zalo broadcast to parents versus a formal school announcement? How does address change between
  a teacher writing to a parent (`quý phụ huynh của em [tên]`) versus to a student directly
  (`thầy/cô` ↔ `em`/`con`, and where the age/seniority line falls)? What are the conventional
  opening/closing formulas for school-to-home communication? What tone markers separate a
  genuinely native notice from a stilted, translated one?

### 2. Higher education and academic writing

- **Genres:** course syllabi (đề cương môn học) and course descriptions; academic transcripts
  and diploma/certificate wording; admissions and scholarship-application copy; thesis/luận văn
  abstracts and academic prose register; university administrative announcements (đăng ký học
  phần, học bổng, miễn giảm học phí); recommendation letters; academic integrity and plagiarism
  notices.
- **Questions:** What distinguishes native Vietnamese academic prose (a formal, Hán-Việt-heavy
  register) from an English-structured translation? What are the standardized transcript and
  diploma terminology and formatting conventions (credit hours = `tín chỉ`, GPA conventions,
  degree classifications) mandated or conventional under Vietnamese higher-ed practice? What is
  the correct address register for university-to-student administrative prose (likely closer to
  `sinh viên` 3rd-person / `anh/chị` than the K-12 `em`/`con`)?

### 3. EdTech and e-learning product copy

- **Genres:** course-platform UI strings (lesson titles, progress indicators, streaks/gamification
  microcopy); quiz and exam interfaces (instructions, timers, result screens); MOOC/video-lecture
  subtitles and dubbing scripts; certificates of completion; onboarding flows for learning apps;
  push notifications and reminder nudges; parent-dashboard copy in child-learning apps.
- **Questions:** This sub-area overlaps `vietnamese-tech-writing` (product UI, i18n) and
  `vietnamese-business-comms` (app push notifications, onboarding) — the research must say
  explicitly where EdTech copy is genuinely new territory (age-appropriate register for a
  child-facing app talking to a `con`/`em`; academic-content-specific vocabulary; subtitle timing
  and reading-speed norms for Vietnamese) versus where it is just an existing skill's doctype
  applied to an education artifact. Which established Vietnamese EdTech products (VioEdu, Kyna,
  ELSA, MindX, Hocmai, Kahoot Việt hoá, Duolingo vi-VN) provide observable native conventions to
  cite?

### 4. Private tutoring, test-prep, and study-abroad marketing

- **Genres:** trung tâm luyện thi / gia sư advertising (Facebook ads, banners, brochures);
  du học (study-abroad) consultancy marketing and consultation-service copy; english-center and
  vocational-training center marketing; scholarship and "cam kết đầu ra" (outcome-guarantee)
  claims.
- **Regulation — this is likely the highest-risk sub-area, treat it as a headline finding, not
  an appendix:** Luật Giáo dục 2019 provisions on advertising education services; the private
  tutoring reform (verify the current status of **Thông tư 29/2024/TT-BGDĐT** restricting dạy
  thêm/học thêm, its 2025 effective date, and any 2025–2026 amendments); Bộ GD&ĐT rules on what
  a training center may claim about outcomes, pass rates, or certification value; general
  advertising law (Luật Quảng cáo 16/2012/QH13, penalties under Nghị định 87/2026/NĐ-CP) as
  applied specifically to "cam kết đỗ", "cam kết đầu ra", guaranteed-score, and guaranteed-visa
  language; consumer-protection rules for du học consultancy contracts. **Verify every instrument
  is still in force as of 2026** and name what replaced anything that is not.

### 5. Curriculum, textbook, and government-facing education content

- **Genres:** textbook and curriculum content approved under Bộ GD&ĐT's Chương trình giáo dục
  phổ thông; official exam materials and instructions (kỳ thi tốt nghiệp THPT); ministry/school
  circular language.
- **Questions:** Is there a distinct, highly formal register and terminology set mandated for
  government/ministry-facing or textbook-published education content, separate from the
  classroom-facing registers above? Is this sub-area worth a skill's attention at all, or is its
  checkable surface too thin/too low-frequency for an individual or team using Claude to ever
  need it (a negative recommendation here is a valid finding — say so if true)?

## Cross-cutting questions (answer once, for the whole domain)

1. **Architecture.** Should Education be a standalone `vietnamese-education-copy` skill, split
   across two (e.g., K-12/academic vs. EdTech-product vs. tutoring-marketing), or folded into
   existing skills the way Product was folded into `vietnamese-tech-writing`? Score this the way
   the prior report did: shared validator profile compatibility, register overlap, and whether
   `description` keywords would collide with `vietnamese-tech-writing` (EdTech UI/i18n) or
   `vietnamese-business-comms` (tutoring/du học marketing, which is fundamentally *advertising*
   copy already in that skill's territory). Give a recommendation with reasoning, and propose
   exact `name`/`description` frontmatter for whatever you recommend — descriptions are the
   trigger signal, keyword-rich, with trigger conditions that will not collide with the four
   existing skills. Run the same collision check `tests/test_trigger_keywords.py` enforces:
   list the keywords your proposed description would claim and flag any already claimed by an
   existing skill's `SKILL.md`.
2. **Register-matrix extension.** Specify the exact new rows the education address terms
   (`thầy/cô ↔ em`, `thầy/cô ↔ con`, `quý phụ huynh`, peer `bạn`, 3rd-person `sinh viên`/`học
   sinh`) need in `shared/references/register-matrix.md`, and confirm none of them conflicts
   with an existing row's forbidden-pronoun list.
3. **Validator reuse.** Which existing rule families (`NFC001`, `CAL001`, `LAW001`, `NUM00x`,
   `PRO00x`, etc.) apply unchanged, which need a new `rules_education.py` (age-register
   consistency, transcript/GPA number formatting, subtitle character-per-line limits), and which
   need a `--doctype` value (e.g. `--doctype report-card`, `--doctype tutoring-ad`)? Propose rule
   IDs (namespaced, e.g. `EDU001`), severities, and a one-line regex-feasibility verdict for
   each — mark anything not machine-checkable for the human QA checklist instead.
4. **Failure-mode evidence.** Find or construct evidence of what unguided LLM Vietnamese
   education writing actually produces — translated-sounding parent notices, wrong-register
   teacher-student address, mistranslated academic terminology, outcome-guarantee ad copy that
   is illegal as written. Prefer observed artifacts (forum complaints, Vietnamese teacher/parent
   commentary, published examples) over speculation, and label anything you infer rather than
   observe.
5. **Prioritisation.** Rank the five sub-areas by (value of fixing) × (density of hard,
   checkable rules) ÷ (research and native-review cost), the same formula the prior report used.
   State plainly whether Education clears the bar to build at all relative to deepening the four
   existing skills, and name any sub-area that is a **bad idea** for a standalone skill.

## Required output format

One Markdown report, in exactly this structure (mirrors `exnpansion-research.md`'s per-function
block so it can be reviewed and built the same way):

```
# Adding education to vietnamese-language-skill

## TL;DR                        (≤10 bullets — the decisions, not a summary)
## Recommended architecture     (skill count, names, frontmatter, keyword-collision check)
## Register-matrix extension    (exact new rows for shared/references/register-matrix.md)
## Priority order               (ranked sub-areas, reasoning, any "do not build")

## Sub-area: K-12 school communications        (repeat this block verbatim for all five sub-areas)
### Genre inventory             (table: artifact | who writes it | register | length/format norms)
### Register and address        (deltas from the existing/extended matrix ONLY)
### Terminology                 (EN | ❌ calque | ✅ native | register — repo table format, backticked cells)
### Regulated and restricted language  (phrase | instrument | article | effective date | penalty | safe rewrite)
### Formatting conventions      (anything not already in shared/references/locale-formatting.md)
### Observed failure modes      (what LLMs get wrong here, with evidence)
### Proposed lint rules         (ID | severity | what it catches | regex-feasible? | false-positive risk)
### Eval pairs                  (8–12, in evals/pairs.jsonl schema, ready to paste)
### Open questions for a native speaker (teacher, parent, or EdTech PM as relevant)

## Cross-cutting findings       (the five questions above)
## Sources                      (URL | publisher | date accessed | primary/secondary | confidence)
## Caveats and what I could not verify
```

## Evidence standards

- **Search in Vietnamese.** The best sources for every genre above are Vietnamese-language
  (teacher forums, VNEDU/Enetviet product pages, Bộ GD&ĐT circulars, university websites,
  EdTech product blogs). English-language sources about Vietnamese education are a distant
  second.
- **Legal claims need the instrument number, the article (Điều/khoản), and the effective date**,
  from a primary or near-primary source (thuvienphapluat.vn, chinhphu.vn, luatvietnam.vn, or
  moet.gov.vn for Bộ GD&ĐT circulars). Today is 2026 — the tutoring reform and related circulars
  moved substantially in 2024–2025, so **verify every instrument you cite is still in force**
  and name what replaced anything that is not. Flag amendments whose effective date is still in
  the future.
- **Distinguish prescription from practice.** "A ministry circular says X" and "live Vietnamese
  schools/apps do X" are different findings; when they conflict, say so and recommend which to
  encode.
- **Terminology needs a real attestation** — a live page, a real app, a published circular,
  observed classroom/parent-communication language. Never invent a Vietnamese term to fill a
  table cell. An empty cell with a note is correct; a plausible fabrication is the worst possible
  output for this repo.
- **Mark confidence inline** (high/medium/low) on any row a reviewer should double-check, and
  collect everything a native speaker (ideally an actual teacher, parent, or EdTech practitioner)
  must sign off on into the per-sub-area open-questions section — the repo requires native-speaker
  approval for glossary and example changes, so this is a real work queue, not a disclaimer.
- Note where a convention differs **North versus South** (Hà Nội versus TP.HCM), by school type
  (public/công lập vs. private/tư thục vs. international), or by education level (mầm non /
  tiểu học / THCS / THPT / đại học), when it changes the wording.

## Out of scope

Do not write code, SKILL.md files, or reference files — that is the build step, and it happens
after a native speaker (ideally with direct classroom, university-admin, or EdTech experience)
reviews this report. Do not restate the existing research (`research.md`,
`exnpansion-research.md`, `expansion-plan.md`). Do not produce general "how to write good
Vietnamese" advice untethered from a specific artifact type.
