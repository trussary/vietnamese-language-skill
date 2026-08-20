# Expanding vietnamese-language-skill: five business functions

## TL;DR
- Build as **three skills, not five**: a broad `vietnamese-business-comms` (Marketing + Sales), a `vietnamese-tech-writing` (Engineering + Product), and a standalone `vietnamese-finance-copy` — because Marketing/Sales share the register+ad-law engine, Engineering/Product share the code-switching engine, and Finance is a legal-risk island that must not share a validator profile with anything.
- **Finance is the highest-value, highest-risk build and should ship first** — the regulated-phrasing surface is dense and machine-checkable (guaranteed-return bans, e-invoice field names, `lãi suất 0%` disclosure), and getting it wrong carries statutory penalties.
- **The single biggest 2025–2026 legal change cluster:** Thông tư 200/2014 (chart of accounts) is REPLACED by Thông tư 99/2025/TT-BTC from 01/01/2026; Luật Quảng cáo sửa đổi 2025 (Luật 75/2025/QH15) adds KOL/KOC disclosure duties from 01/01/2026; Zalo ZNS is replaced by ZBS Template Message from 01/01/2026. Any skill citing the old regime is already stale.
- Engineering's central finding is **code-switching is not optional**: `deploy`, `commit`, `merge`, `bug`, `server`, `cache`, `deadline` stay English in native writing; forced calques (`cam kết` for commit, `triển khai đến sản xuất` for deploy to production) mark machine translation. Identifiers/branches/commit subjects must never carry diacritics.
- Product's headline finding is a **measurement hazard, not a copy hazard**: documented Vietnamese acquiescence/positivity bias (Krosnick's handbook puts the average acquiescence effect at ~10%) means agree/disagree Likert scales inflate scores; the skill must force item-specific scales, not "đồng ý/không đồng ý."
- **Register deltas are small per-domain** — the existing matrix covers most cases; the real new work is (a) B2B xưng hô (`anh/chị` + `em` for junior sellers, seniority overrides role) and (b) impersonal register for engineering docs where `bạn` is often wrong.
- **Validator reuse:** `LAW`, `NUM`, `CAL`, tone-mark and NFC rules are universal; each domain needs a new rule family (`ZNS`, `MKT`, `SALES`, `ENG`, `PROD`, `FIN`). Many high-value checks (guaranteed-return claims, survey bias, calque naturalness) are **NOT regex-feasible** and belong in a human QA checklist.
- Superlative handling from the existing skill (warn, `<!-- proof -->` suppresses) extends cleanly to finance's guaranteed-return language and marketing's `nhất`/`số 1`.
- **Do not build a standalone "Legal/Compliance Vietnamese" skill** — compliance is a cross-cutting reference (`references/compliance.md`) shared by all three, not a genre a practitioner writes in. Also fold Product into tech-writing rather than shipping it standalone.
- Shared references should be **duplicated via a build step**, not symlinked — the repo's one-level-deep `references/` rule and relative-link tests make a generated copy the only safe option.

## Recommended architecture

### Skill count and rationale
Five sibling skills would triplicate the register matrix, tone-mark rule, NFC rule, and number-format reference into five folders, and their `description` triggers would collide (Marketing vs Sales both fire on "email"; Engineering vs Product both fire on "release notes"). One mega-skill would blow the ~500-line SKILL.md budget and force one validator profile across incompatible registers.

**Recommendation: three skills**, grouped by shared failure-mode engine:

1. **`vietnamese-business-comms`** — Marketing (beyond landing) + Sales. Both run on the register/pronoun engine + advertising/promotion law + CTA/promotional-formula conventions. A Zalo broadcast and a cold email are the same register problem.
2. **`vietnamese-tech-writing`** — Engineering + Product. Both run on the code-switching engine + impersonal-vs-`bạn` register + i18n mechanics. A PRD and an RFC share terminology.
3. **`vietnamese-finance-copy`** — Finance alone. A legal-risk island: statement terminology, e-invoice fields, regulated financial-promotion phrasing. Its validator must be legally conservative in ways that would produce false positives elsewhere.

### Proposed frontmatter

```yaml
# skills/vietnamese-business-comms/SKILL.md
name: vietnamese-business-comms
description: >-
  Write native vi-VN marketing and sales copy: email campaigns, Zalo OA/ZBS
  broadcasts, Facebook/TikTok ads, Shopee/Lazada/TikTok Shop listings, press
  releases, cold outreach, báo giá/quotes, proposals, đề xuất, dunning and Tết
  greetings. Use when drafting Vietnamese promotional, outbound, or B2B sales
  content, choosing anh/chị vs bạn register, or checking khuyến mại / ad-law /
  anti-spam compliance. Not for landing pages (see vietnamese-landing-copy).
```

```yaml
# skills/vietnamese-tech-writing/SKILL.md
name: vietnamese-tech-writing
description: >-
  Write native vi-VN engineering and product docs: commit messages, PR
  descriptions, code review, RFCs, postmortems, runbooks, READMEs, API docs,
  UI error microcopy, i18n files, PRDs, user stories, release notes, in-app
  notifications, help-centre articles, surveys, and app-store listings. Use
  when drafting Vietnamese technical or product content, deciding which terms
  stay English vs Vietnamese, or handling vi-VN i18n hazards.
```

```yaml
# skills/vietnamese-finance-copy/SKILL.md
name: vietnamese-finance-copy
description: >-
  Write native vi-VN finance content: hóa đơn điện tử, báo cáo tài chính,
  management reports, investor updates, board decks, pricing/payment-terms,
  fintech/banking/insurance product copy, loan and credit disclosures. Use
  when drafting Vietnamese financial statements or financial promotion,
  applying Thông tư 99/2025 account terminology, e-invoice field names, or
  checking guaranteed-return / interest-rate / insurance advertising limits.
```

Triggers are keyword-partitioned: business-comms owns campaign/ad/sales words, tech-writing owns commit/PRD/API words, finance owns invoice/statement/disclosure words. No overlap fires two skills on the same artifact.

### Shared-reference plan
The register matrix, tone-mark rule, NFC rule, and number-format reference apply to all three. Options: (a) duplicate by hand — drifts; (b) symlink — breaks the "relative links resolve" test on checkout/zip; (c) one skill names another — the spec keeps references inside each skill folder, so cross-skill paths won't resolve; (d) **a generated build step** that copies canonical `shared/*.md` into each skill's `references/` at build time, with a test asserting the copies match the source hash.

**Recommendation: (d) a build step.** Honest, non-trivial cost: a `scripts/sync_shared.py` (stdlib-only, matches repo policy) plus a CI check that fails if any skill's `references/register-matrix.md` diverges from `shared/register-matrix.md`. This keeps every skill self-contained (spec-compliant, links resolve) while giving one source of truth. The cost is one extra CI job and the discipline of editing only the canonical copy, never the generated one.

## Priority order
Ranked by (value of fixing) × (density of hard, checkable rules) ÷ (research + native-review cost):

1. **Finance (build first).** Highest legal risk, densest machine-checkable surface (e-invoice mandatory fields, account terminology under TT 99/2025, guaranteed-return/interest-rate disclosure). Errors have statutory penalties, not just awkwardness. Review cost is concentrated (one accountant + one securities/insurance lawyer).
2. **Marketing.** High value (largest volume of Vietnamese output), dense checkable rules (ZBS template constraints, khuyến mại 50% ceiling, anti-spam windows, `nhất`/`số 1`). Ad-law engine mostly inherited from the landing skill.
3. **Sales.** Shares Marketing's engine; incremental cost is low once business-comms exists. Fewer hard regex rules (xưng hô is context-dependent, largely a human-QA concern), so it rides along rather than leading.
4. **Engineering.** High value for tech teams, but the central rule (code-switching) is a large glossary needing heavy native review and only partially regex-checkable (diacritics-in-identifiers is checkable; "is this calque natural?" is not).
5. **Product (build last, or fold into tech-writing).** Genuine value but the highest ratio of not-machine-checkable findings (survey bias, interview pronoun choice, release-note voice). Much of it is judgment, not lint.

**Negative recommendation:** do not build a standalone **"Vietnamese Legal/Compliance"** skill. Compliance phrasing is a reference consumed by the other skills, not an artifact type a practitioner sits down to write; a separate skill would collide on triggers and duplicate citations. Also do not split Product into its own skill — its checkable surface is too thin to justify a separate validator profile.

---

## Function: Marketing

### Genre inventory
| Artifact | Who writes it | Register | Length / format norms |
|---|---|---|---|
| Email campaign / newsletter | Marketing/CRM | `bạn` (SaaS/e-comm/youth), `anh/chị` (mid-market) | Subject ~40 chars; preview text distinct; single register |
| Zalo OA / ZBS Template Message | CRM/CSKH | `Quý khách`/`anh/chị` | Max 400 chars có dấu; template pre-approved by Zalo; no marketing content in transactional tag |
| Facebook / TikTok ad copy | Performance/agency | `bạn` | Short; emoji common; hook in first line |
| Shopee/Lazada/TikTok Shop listing title | Seller/ops | 3rd-person / keyword string | Formula: loại SP + thương hiệu + tên/mã + mô tả; no ALL-CAPS; no icon spam |
| SEO long-form article | Content | `bạn`/impersonal | H2/H3; keyword in title; slug unaccented-lowercase-hyphenated |
| Social caption | Social | `bạn`/`mình` | Hashtag cluster at end; emoji moderate |
| Push notification | Product/CRM | `bạn` | ~40–120 chars |
| Press release (thông cáo báo chí) | PR/Comms | `Quý vị`/institutional 3rd person | Formal; dateline; boilerplate "Về [công ty]" |
| KOL/KOC brief | Influencer mktg | `anh/chị`/`bạn` | Internal; must now specify disclosure per Luật QC 2025 |
| Livestream script | Seller/host | `mọi người`/`cả nhà` | Spoken register; CTA repetition |

### Register and address (deltas from existing matrix only)
- **Zalo ZBS/ZNS** skews to `Quý khách` even for brands using `bạn` on their landing page — the channel reads as a service notification, not marketing. A channel-override the base matrix doesn't capture.
- **Press release** uses institutional 3rd-person (`Công ty… trân trọng thông báo`), closer to `quý vị` register than any landing-page register.
- **Livestream** is the one genre where spoken plural address (`cả nhà`, `mọi người`) is native and correct; written registers read stiff.

### Terminology
| EN | ❌ calque | ✅ native | register |
|---|---|---|---|
| `Free shipping` | `giao hàng miễn phí` (weak) | `Freeship` / `Miễn phí vận chuyển` | e-comm, `bạn` |
| `Flash sale` | `bán chớp nhoáng` | `Săn sale` / `Flash Sale` | e-comm |
| `Deal` | — | `Deal hời` / `Ưu đãi` | e-comm |
| `Limited offer` | `lời đề nghị giới hạn` | `Ưu đãi có hạn` / `Số lượng có hạn` | all |
| `Voucher` | phiếu giảm giá (formal, fine) | `Voucher` / `Mã giảm giá` | e-comm |
| `Subscribe` (newsletter) | `đăng ký thuê bao` | `Đăng ký nhận tin` | all |
| `Best seller` | `người bán tốt nhất` | `Bán chạy nhất` (⚠ superlative — needs proof) | e-comm |

### Regulated and banned language
| Phrase / practice | Instrument | Article | Effective | Penalty | Safe rewrite |
|---|---|---|---|---|---|
| `nhất`/`duy nhất`/`tốt nhất`/`số 1` without licensed proof | Luật Quảng cáo 16/2012/QH13 | Điều 8 khoản 11 | 2013 (in force) | per NĐ 87/2026 Điều 50 kh.2 (see caveat) | drop, or add `<!-- proof: ... -->` |
| Discount > 50% (outside concentrated promo) | NĐ 81/2018/NĐ-CP as amended by NĐ 128/2024/NĐ-CP | Điều 7 kh.2 | 128/2024 eff. 01/12/2024 | admin fine | cap at 50%; up to 100% only for chương trình khuyến mại tập trung |
| Marketing SMS/email/call without opt-in; outside windows | NĐ 91/2020/NĐ-CP | Điều 13 (windows); Điều 32 (penalty) | 01/10/2020 | 80–100M VND organisations for DoNotCall violations (individuals half) | opt-in; SMS 07:00–22:00, calls 08:00–17:00; ≤3 SMS/24h, ≤1 call/24h |
| Marketing content in a ZNS/ZBS transactional template | Zalo ZBS policy | — | ZBS from 01/01/2026 | template rejected | use post-sale/hậu mãi tag; register separate template |
| KOL/KOC undisclosed paid promotion | Luật Quảng cáo sửa đổi 2025 (Luật 75/2025/QH15) | Điều 15a | 01/01/2026 | admin, possible criminal | disclose "quảng cáo"/tài trợ; must have used product |
| Health/food/supplement/pharma claims without pre-approval | Luật QC + sector rules | — | in force | admin | route to pre-approval; no therapeutic claims |

The NĐ 128/2024/NĐ-CP amendment reads verbatim: *"Mức giảm giá tối đa đối với hàng hóa, dịch vụ được khuyến mại không được vượt quá 50% giá hàng hóa, dịch vụ đó ngay trước thời gian khuyến mại… Trong trường hợp tổ chức chương trình khuyến mại tập trung… áp dụng mức giảm tối đa… là 100%."*

### Formatting conventions (not already in locale-formatting.md)
- Marketplace titles: **accented + unaccented keyword duplication is common practice but risks Shopee spam flags**; ALL-CAPS lowers search rank; icons in titles read as clone/spam.
- Hashtags: clustered at the end of a caption, not inline; mixing Vietnamese-unaccented and English tags is native.
- Emoji density: 1–3 per short ad/caption reads native; heavy strings read as spam.
- Preview/preheader text should differ from the subject line.

### Observed failure modes
- Google Translate auto-translation producing "câu từ vô nghĩa, sai nội dung" — documented by Vietnamese press (Báo Thanh Hóa), including cases where official documents were rendered meaningless; the same MT surface underlies LLM translationese.
- CTA calques: literal `Học thêm` / over-used `Tìm hiểu thêm` where native e-comm uses `Xem ngay` / `Mua ngay` (inherited from prior research).
- LLMs producing `giao hàng miễn phí` where the market says `Freeship`; over-formalizing youth/e-comm register.
- Emitting a marketing promo inside a ZNS template (auto-rejected by Zalo).

### Proposed lint rules
| ID | Severity | Catches | Regex-feasible? | False-positive risk |
|---|---|---|---|---|
| LAW001 (reuse) | warn | `nhất`/`số 1`/`tốt nhất`/`duy nhất` w/o proof annotation | Yes | Med (idiomatic `nhất là`) |
| ZNS001 | warn | Marketing verbs (`ưu đãi`,`giảm giá`,`khuyến mãi`) in a transactional-tagged doc | Yes | Med |
| ZNS002 | error | ZBS/ZNS body > 400 chars có dấu | Yes | Low |
| MKT001 | warn | Marketplace title ALL-CAPS or containing emoji | Yes | Low |
| MKT002 | warn | Discount > 50% without khuyến-mại-tập-trung annotation | Yes (number parse) | Med |
| MKT003 | info | CTA calque `Học thêm`/literal `Tìm hiểu thêm` | Yes | Med |
| SPAM001 | warn | Missing opt-out/opt-in marker in bulk SMS/email template | Partial | High |
| MKT004 (human) | n/a | KOL disclosure present & product actually used | No | — |

### Eval pairs
```jsonl
{"id":"mkt-001","category":"marketing","en":"The best coffee in Vietnam","bad":"Cà phê số 1 Việt Nam","good":"Cà phê được yêu thích tại Việt Nam","diagnosis":"số 1 superlative without licensed proof (Luật QC Đ8 kh11)","expected_rules":["LAW001"]}
{"id":"mkt-002","category":"marketing","en":"Free shipping nationwide","bad":"Giao hàng miễn phí trên toàn quốc","good":"Freeship toàn quốc","diagnosis":"e-comm register uses Freeship; calque reads weak","expected_rules":["MKT003"]}
{"id":"mkt-003","category":"marketing","en":"Order confirmation + 50% promo","bad":"Đơn hàng đã xác nhận. Ưu đãi giảm 50% hôm nay!","good":"Đơn hàng #{order} của bạn đã được xác nhận.","diagnosis":"marketing content in transactional ZNS template","expected_rules":["ZNS001"]}
{"id":"mkt-004","category":"marketing","en":"Learn more","bad":"Học thêm","good":"Xem ngay","diagnosis":"CTA calque; Học thêm means take extra classes","expected_rules":["MKT003"]}
{"id":"mkt-005","category":"marketing","en":"Limited time offer","bad":"Lời đề nghị giới hạn thời gian","good":"Ưu đãi có hạn","diagnosis":"translationese; standard formula is Ưu đãi có hạn","expected_rules":[]}
{"id":"mkt-006","category":"marketing","en":"SALE UP TO 70%","bad":"SALE SỐC GIẢM 70% DUY NHẤT HÔM NAY","good":"Sale đến 70% – số lượng có hạn","diagnosis":"ALL-CAPS + duy nhất superlative; title-case native","expected_rules":["LAW001","MKT001"]}
{"id":"mkt-007","category":"marketing","en":"Product title: Nike running shoes men","bad":"GIÀY NIKE 🔥🔥 CHÍNH HÃNG SALE SỐC","good":"Giày thể thao nam Nike chính hãng - running","diagnosis":"ALL-CAPS + emoji in marketplace title lowers rank","expected_rules":["MKT001"]}
{"id":"mkt-008","category":"marketing","en":"90% off everything","bad":"Giảm giá 90% toàn bộ sản phẩm","good":"Giảm giá đến 50% toàn bộ sản phẩm","diagnosis":"exceeds 50% ceiling outside concentrated promo (NĐ 81/2018 as amended by NĐ 128/2024)","expected_rules":["MKT002"]}
{"id":"mkt-009","category":"marketing","en":"Subscribe to our newsletter","bad":"Đăng ký thuê bao bản tin của chúng tôi","good":"Đăng ký nhận tin","diagnosis":"thuê bao = phone subscription; wrong sense","expected_rules":[]}
{"id":"mkt-010","category":"marketing","en":"Press release header","bad":"Bọn mình vừa ra mắt sản phẩm mới nè!","good":"Công ty [X] trân trọng thông báo ra mắt sản phẩm mới.","diagnosis":"press release requires institutional register, not bạn/mình","expected_rules":[]}
```

### Open questions for a native speaker
- Is accented+unaccented keyword duplication in Shopee titles currently rewarded or penalized by the 2026 algorithm? (Practice sources conflict.)
- Current native default emoji density for TikTok Shop vs Shopee.
- Whether `Săn sale`/`Deal hời` read as native or dated to a South/North audience.

---

## Function: Sales

### Genre inventory
| Artifact | Who writes it | Register | Length / format norms |
|---|---|---|---|
| Cold email / Zalo outreach | Sales/BD | `anh/chị` (+ `em` if junior) | Kính gửi… / Trân trọng; 3-part (mở/thân/kết) |
| Follow-up sequence | Sales | `anh/chị` | Short; references prior touch |
| Báo giá / bảng giá | Sales/ops | `Quý khách`/`anh/chị` | Table; VAT line; validity period |
| Proposal / đề xuất | Sales/BD | `anh/chị`/formal | Structured; exec summary |
| Hợp đồng nguyên tắc / SOW | Legal/Sales | formal 3rd-person | Boilerplate per Luật Thương mại 2005 |
| Biên bản nghiệm thu | Ops/Sales | formal | Standardized acceptance form |
| Payment terms / dunning | Finance/Sales | `Quý khách`/`anh/chị` | Polite-but-firm; escalating |
| Tết / holiday greeting | Sales/Mktg | `Quý khách`/`anh/chị` | Formulaic well-wishes |
| Meeting request / recap | Sales | `anh/chị` | Concise; action items |
| Objection-handling script | Sales enablement | `anh/chị` | Internal |

### Register and address (deltas only)
- **B2B xưng hô is the whole game and the base matrix doesn't cover it.** Default when seniority unknown: `anh/chị`. A junior seller correctly uses `em` for self toward an older/more senior buyer (`em gửi anh báo giá`). Age and seniority override role — a junior buyer who is clearly older may still get `anh/chị`. Group address: `anh/chị` or `Quý anh/chị`.
- **Openings/closings tier:** `Kính gửi` (most formal, cold/first contact) > `Dear` (accepted in VN business email, mid-formal) > `Chào anh/chị` (warm, established). Closings: `Trân trọng` (formal default) > `Thân mến`/`Thân` (warm, established relationship).
- Native cold email is **more relational up front** than an English one — a brief courtesy/context line before the ask; a hard first-line pitch reads rude.

### Terminology
| EN | ❌ calque | ✅ native | register |
|---|---|---|---|
| `Quote` | `trích dẫn` (wrong sense) | `Báo giá` | sales |
| `Price list` | `danh sách giá` | `Bảng giá` | sales |
| `Proposal` | — | `Đề xuất` / `Proposal` | B2B |
| `VAT invoice` | — | `Hóa đơn GTGT` | sales/finance |
| `Deposit` | `tiền gửi` (wrong sense) | `Đặt cọc` / `Tạm ứng` | sales |
| `Follow up` | `theo lên` | `Theo dõi` / `Follow up` | internal |
| `Best regards` | `lời chào tốt nhất` | `Trân trọng` | all |

### Regulated and banned language
| Phrase / practice | Instrument | Article | Effective | Penalty | Safe rewrite |
|---|---|---|---|---|---|
| Cold outreach SMS/email/call without opt-in | NĐ 91/2020/NĐ-CP | Điều 13 | 01/10/2020 | up to 80–100M VND | obtain consent; respect windows |
| VAT-invoice wording on quotes | NĐ 123/2020/NĐ-CP + NĐ 70/2025/NĐ-CP | Điều 10 | e-invoice mandatory 01/07/2022 | admin | use `thuế GTGT`, `MST`, mandated field names |
| Contract boilerplate authority | Luật Thương mại 2005 | — | in force | contract void/unenforceable | standard hợp đồng nguyên tắc structure |
| Superlatives in sales decks | Luật Quảng cáo 16/2012 | Điều 8 kh.11 | in force | admin | same as marketing |

### Formatting conventions (not already covered)
- Báo giá must show price + VAT treatment (`đã bao gồm VAT` / `chưa bao gồm VAT`) and a validity date (`Báo giá có hiệu lực đến…`).
- E-signature and hóa đơn GTGT references belong in the contract close, not the body.
- Currency follows locale (`2.500.000 ₫`), but B2B prose often uses colloquial `2,5 tỷ` / `35 triệu`.

### Observed failure modes
- LLMs default to `bạn` in B2B outreach where `anh/chị` is required — an instant tell of automated origin.
- Over-direct first-line pitch (English cold-email structure) transplanted without the courtesy opener.
- `trích dẫn` for "quote," `theo lên` for "follow up," `lời chào tốt nhất` for "best regards" — literal calques.
- Wrong closing register (`Thân mến` to a cold prospect).

### Proposed lint rules
| ID | Severity | Catches | Regex-feasible? | False-positive risk |
|---|---|---|---|---|
| SALES001 | warn | `bạn` in a doc typed cold/B2B outreach | Partial | High (needs doc-type flag) |
| SALES002 | warn | `trích dẫn`/`theo lên`/`lời chào tốt nhất` calques | Yes | Low |
| SALES003 | info | Missing `Kính gửi`/greeting in formal outreach | Partial | Med |
| SALES004 | info | Báo giá missing VAT treatment or validity date | Partial | Med |
| SALES005 (human) | n/a | xưng hô correct for age/seniority context | No | — |

### Eval pairs
```jsonl
{"id":"sal-001","category":"sales","en":"Hi, I want to send you our quote","bad":"Chào bạn, mình muốn gửi bạn báo giá","good":"Kính gửi anh/chị, em xin gửi báo giá của bên em","diagnosis":"B2B cold outreach requires anh/chị + em, not bạn/mình","expected_rules":["SALES001"]}
{"id":"sal-002","category":"sales","en":"Please find our quotation attached","bad":"Vui lòng xem trích dẫn đính kèm","good":"Anh/chị vui lòng xem báo giá đính kèm","diagnosis":"trích dẫn = citation; quote is báo giá","expected_rules":["SALES002"]}
{"id":"sal-003","category":"sales","en":"I'll follow up next week","bad":"Em sẽ theo lên vào tuần sau","good":"Em sẽ theo dõi/liên hệ lại vào tuần sau","diagnosis":"theo lên is a calque of follow up","expected_rules":["SALES002"]}
{"id":"sal-004","category":"sales","en":"Best regards","bad":"Lời chào tốt nhất","good":"Trân trọng","diagnosis":"calque; standard closing is Trân trọng","expected_rules":["SALES002"]}
{"id":"sal-005","category":"sales","en":"Price list (VAT included)","bad":"Bảng giá","good":"Bảng giá (đã bao gồm thuế GTGT), hiệu lực đến 31/12/2026","diagnosis":"quote must state VAT treatment and validity","expected_rules":["SALES004"]}
{"id":"sal-006","category":"sales","en":"Dear Sir, buy now!","bad":"Anh ơi mua ngay đi!","good":"Kính gửi anh, em xin phép giới thiệu giải pháp phù hợp với nhu cầu của bên anh","diagnosis":"over-direct first-line pitch reads rude in VN B2B","expected_rules":["SALES003"]}
{"id":"sal-007","category":"sales","en":"Warm regards to a cold prospect","bad":"Thân mến,","good":"Trân trọng,","diagnosis":"Thân mến is for established relationships, not cold contact","expected_rules":[]}
{"id":"sal-008","category":"sales","en":"Payment reminder","bad":"Bạn phải trả tiền ngay lập tức.","good":"Kính đề nghị Quý khách thanh toán trước ngày [X]. Trân trọng.","diagnosis":"dunning must stay polite-but-firm; bạn + imperative reads rude","expected_rules":["SALES001"]}
{"id":"sal-009","category":"sales","en":"Happy Lunar New Year","bad":"Chúc mừng năm mới bạn nhé!","good":"Kính chúc Quý khách một năm mới an khang thịnh vượng.","diagnosis":"B2B Tết greeting uses Quý khách + formulaic well-wishes","expected_rules":["SALES001"]}
{"id":"sal-010","category":"sales","en":"Deposit required","bad":"Yêu cầu tiền gửi trước","good":"Quý khách vui lòng đặt cọc trước","diagnosis":"tiền gửi = bank deposit; sales deposit is đặt cọc","expected_rules":["SALES002"]}
```

### Open questions for a native speaker
- Exact threshold at which a young seller switches from `em` to `tôi` with a same-age buyer.
- North vs South tolerance for `Dear` in Vietnamese business email.
- Whether `Quý anh/chị` reads natural or stiff for group address in a mid-market deck.

---

## Function: Engineering

### Genre inventory
| Artifact | Who writes it | Register | Length / format norms |
|---|---|---|---|
| Commit message | Dev | imperative, English subject common | Conventional Commits; subject ASCII, no diacritics |
| PR description | Dev | mixed VN prose + English terms | What/why; links |
| Code review comment | Dev | `mình`/`bạn` peer, or impersonal | Terse; English technical terms |
| Design doc / RFC | Senior dev | impersonal/formal | Structured; VN prose, English terms |
| Postmortem | SRE/dev | impersonal | Timeline; blameless |
| Status page | SRE/support | `Quý khách`/impersonal | User-facing; plain |
| API docs | Dev/DevRel | impersonal / `bạn` | Reference; English identifiers |
| Runbook | SRE | imperative | Step list |
| README | Dev | `bạn`/impersonal | Setup steps |
| UI error / microcopy | Dev/Product | `bạn`/impersonal | Short; actionable |
| i18n resource file | Dev | matches product register | ICU; `other`-only plural |

### Register and address (deltas only)
- **`bạn` is often WRONG in engineering docs.** RFCs, postmortems, and design docs use impersonal constructions (`Hệ thống sẽ…`, `Cần cấu hình…`), not `bạn`. `bạn` belongs in READMEs, tutorials, and user-facing docs. This is the inverse of the landing-page default and the base matrix doesn't flag it.
- Runbooks/instructions use **imperative mood** (`Chạy lệnh…`, `Kiểm tra log…`), not `bạn nên`.
- Error messages address the user with `bạn` (SaaS) or impersonally; never `quý khách` in a dev tool.

### Terminology
Evidence drawn from Viblo / live Vietnamese engineering writing, not dictionaries.
| EN | ❌ calque (marks MT) | ✅ native usage | register |
|---|---|---|---|
| `deploy` | `triển khai` (OK in prose, but `deploy` dominates) | `deploy` | eng |
| `commit` | `cam kết` (wrong sense) | `commit` | eng |
| `merge` | `hợp nhất` (stiff) | `merge` | eng |
| `bug` | `con bọ` (jokey only) | `bug` / `lỗi` | eng |
| `server` | — | `server` / `máy chủ` (both live) | eng |
| `database` | — | `database` / `cơ sở dữ liệu` (both live) | eng |
| `cache` | `bộ nhớ đệm` (formal docs) | `cache` (speech/PR) | eng |
| `deadline` | — | `deadline` | internal |
| `error` (UI) | — | `lỗi` | user-facing |
| `patch` | — | `bản vá` / `patch` | eng |
| `deploy to production` | `triển khai đến sản xuất` (MT tell) | `deploy lên production` | eng |

**Calques that mark machine translation:** `triển khai đến sản xuất` (for deploy to production), `cam kết` (for commit), `con bọ`/`sự cố` for a routine bug, `hàng đợi thông điệp` (for message queue), translating `production`/`staging` environment names.

### Regulated and banned language
Engineering copy is largely outside advertising/finance law. The hard rules are technical, not legal:
| Practice | Rule | Feasible check | Notes |
|---|---|---|---|
| Diacritics in identifiers/branches/commit subjects | Must be ASCII (unaccented) | Yes | Breaks tooling; universal native practice |
| Mixed tone-mark style | Inherit base NFC + kiểu mới/cũ rule | Yes | Same as base |

### Formatting conventions (i18n hazards, not in locale-formatting.md)
- **String-length expansion:** English→Vietnamese text typically expands ~25–30% (Gengo cites ~30%; Transphere's 2026 guide gives 25–30%, more for very short UI labels) — flag fixed-width buttons.
- **Diacritic-insensitive search/sort (collation):** Vietnamese needs accent-insensitive matching (`cà phê` findable via `ca phe`); default byte-sort mis-orders.
- **NFC vs NFD:** `ế` can be one precomposed or multiple combining codepoints; `len()` differs; base skill mandates NFC — engineering must enforce NFC in i18n files and DB.
- **Telex/VNI input:** forms must accept both input methods; don't strip diacritics on input.
- **`vi-VN` vs `vi`:** prefer `vi-VN` where region formatting matters; `vi` acceptable for language-only.
- **Font subsets** that drop stacked diacritics (ề, ộ, ữ) break rendering — flag web-font subsetting.
- **ICU plurals:** Vietnamese has no grammatical plural — messages carry `other` only (inherited from base).
- Number/date handling: `dd/MM/yyyy`, `.` grouping, `,` decimal in common libs (inherited).

### Observed failure modes
- LLM/MT emitting `cam kết` for `commit`, `triển khai đến sản xuất` for deploy — the exact MT tells Vietnamese devs cite.
- Over-translating standard English terms (`hàng đợi thông điệp` for message queue) where devs say `message queue`.
- Using `bạn` in an RFC/postmortem where impersonal is correct.
- Accented commit subjects/branch names.
- Fixed-width UI truncating expanded Vietnamese strings.

### Proposed lint rules
| ID | Severity | Catches | Regex-feasible? | False-positive risk |
|---|---|---|---|---|
| ENG001 | error | Diacritics in commit subject / branch / identifier | Yes | Low |
| ENG002 | warn | `cam kết` near git context; `triển khai đến sản xuất` | Yes | Low |
| ENG003 | warn | `bạn` in a doc typed RFC/postmortem/design | Partial | Med (needs doc-type) |
| ENG004 | warn | Non-NFC codepoints in i18n resource values | Yes | Low |
| ENG005 | info | ICU plural with keys other than `other` in a vi file | Yes | Low |
| ENG006 (human) | n/a | Is a given Vietnamese calque natural vs MT? | No | — |

### Eval pairs
```jsonl
{"id":"eng-001","category":"engineering","en":"commit your changes","bad":"cam kết các thay đổi của bạn","good":"commit các thay đổi","diagnosis":"cam kết is wrong sense; commit stays English","expected_rules":["ENG002"]}
{"id":"eng-002","category":"engineering","en":"deploy to production","bad":"triển khai đến sản xuất","good":"deploy lên production","diagnosis":"MT tell; production is not translated","expected_rules":["ENG002"]}
{"id":"eng-003","category":"engineering","en":"branch name feat/add-login","bad":"feat/thêm-đăng-nhập","good":"feat/add-login","diagnosis":"branch names must be ASCII, no diacritics","expected_rules":["ENG001"]}
{"id":"eng-004","category":"engineering","en":"RFC: the system will retry","bad":"Bạn sẽ thử lại yêu cầu","good":"Hệ thống sẽ tự động thử lại request","diagnosis":"RFC uses impersonal register, not bạn","expected_rules":["ENG003"]}
{"id":"eng-005","category":"engineering","en":"Fix the bug in the cache","bad":"Sửa con bọ trong bộ nhớ đệm","good":"Fix bug ở cache","diagnosis":"con bọ is jokey; over-translation of cache","expected_rules":["ENG002"]}
{"id":"eng-006","category":"engineering","en":"error message: Something went wrong","bad":"Kính thưa quý khách, đã có lỗi","good":"Đã có lỗi xảy ra. Vui lòng thử lại.","diagnosis":"quý khách wrong register for a dev-tool error","expected_rules":[]}
{"id":"eng-007","category":"engineering","en":"1 file changed / 5 files changed","bad":"{count} tập tin đã thay đổi|{count} các tập tin","good":"{count} tệp đã thay đổi","diagnosis":"Vietnamese has no plural; ICU other-only","expected_rules":["ENG005"]}
{"id":"eng-008","category":"engineering","en":"message queue","bad":"hàng đợi thông điệp","good":"message queue","diagnosis":"over-translation; devs keep English","expected_rules":["ENG002"]}
{"id":"eng-009","category":"engineering","en":"Run the migration","bad":"Bạn nên chạy migration","good":"Chạy migration","diagnosis":"runbook uses imperative, not bạn nên","expected_rules":[]}
{"id":"eng-010","category":"engineering","en":"i18n value with combining marks","bad":"Đăng nhập (NFD combining ế)","good":"Đăng nhập (NFC)","diagnosis":"i18n values must be NFC-normalized","expected_rules":["ENG004"]}
```

### Open questions for a native speaker
- Which of `server`/`máy chủ`, `database`/`cơ sở dữ liệu` a given team's docs prefer (house-style, not universal).
- Whether `bản vá` or `patch` dominates in current release-note writing.
- Acceptable amount of English in user-facing (not internal) error text.

---

## Function: Product

### Genre inventory
| Artifact | Who writes it | Register | Length / format norms |
|---|---|---|---|
| PRD / spec | PM | impersonal/formal | Structured |
| User story / acceptance criteria | PM | impersonal | "Là [vai trò], tôi muốn…" |
| Release notes / changelog | PM/dev | `bạn`/impersonal | Concise; benefit-led |
| In-app notification / empty state / paywall / permission prompt | PM/Product | `bạn` | Short; actionable |
| Onboarding flow | PM/UX | `bạn` | Friendly |
| Help-centre article / support macro | Support | `bạn`/`Quý khách` | Step-by-step |
| Survey / NPS wording | PM/Research | `bạn`/`Quý khách` | Neutral; unbiased |
| User-interview script / discussion guide | Research | `anh/chị`/`bạn` by age | Open questions |
| Persona | PM | 3rd person | Profile |
| App-store listing (ASO) | PM/Mktg | `bạn` | Char limits; keywords |

### Register and address (deltas only)
- **User-interview moderator pronoun varies by participant age** — `anh/chị` for older participants, `bạn` for peers; using one register for all reads wrong. A research-specific delta.
- Release notes lean `bạn` or impersonal benefit-led (`Đã sửa lỗi…`, `Bạn giờ có thể…`).
- Permission prompts stay short and `bạn`; over-formal `Quý khách` reads odd in-app for youth/SaaS.

### Terminology
| EN | ❌ calque | ✅ native usage | register |
|---|---|---|---|
| `sprint` | `chạy nước rút` | `sprint` | product/agile |
| `backlog` | `tồn đọng` | `backlog` | product |
| `roadmap` | `bản đồ đường` | `roadmap` / `lộ trình` | product |
| `feature` | — | `tính năng` | product |
| `user experience` | — | `trải nghiệm người dùng` / `UX` | product |
| `onboarding` | `lên tàu` | `onboarding` | product |
| `empty state` | `trạng thái trống` | `empty state` (internal) | product |

### Regulated and banned language
| Practice | Instrument | Article | Effective | Penalty | Safe rewrite |
|---|---|---|---|---|---|
| Consent copy in lead/permission forms | NĐ 13/2023/NĐ-CP (personal data) | — | in force | admin | explicit consent; state purpose |
| Superlatives in app-store listing | Luật Quảng cáo 16/2012 | Điều 8 kh.11 | in force | admin | drop or prove |
| Health/medical claims in health-app copy | sector pre-approval | — | in force | admin | avoid therapeutic claims |

### Formatting conventions (not already covered)
- **App-store metadata:** diacritics count against character limits; accented+unaccented keyword duplication is used for ASO but risks truncation. Title/subtitle limits interact with Vietnamese ~25–30% length expansion.
- In-app notification length: keep under one line on mobile; expansion truncates.
- Survey scales: label every point, don't rely on numeric-only.

### Observed failure modes
- **Acquiescence/positivity bias**: documented tendency of respondents to agree with statements; Krosnick's handbook puts the average acquiescence effect at ~10% (across 10 studies, 52% agreed with an assertion while only 42% disagreed with its opposite). Agree/disagree Likert scales inflate scores; LLMs default to "đồng ý/không đồng ý" scales that maximize this bias.
- Over-translating agile terms (`chạy nước rút` for sprint, `tồn đọng` for backlog) — reads non-native to Vietnamese product teams.
- `lên tàu` for onboarding, `bản đồ đường` for roadmap.
- Over-formal permission prompts.

### Proposed lint rules
| ID | Severity | Catches | Regex-feasible? | False-positive risk |
|---|---|---|---|---|
| PROD001 | warn | agile calques `chạy nước rút`/`tồn đọng`/`bản đồ đường`/`lên tàu` | Yes | Low |
| PROD002 | warn | agree/disagree Likert wording in a survey doc | Partial | High |
| PROD003 | info | app-store title/subtitle over char limit (diacritic-aware) | Yes | Low |
| PROD004 | warn | Missing explicit-consent phrasing in permission/lead form | Partial | High |
| PROD005 (human) | n/a | Is a survey item leading / biased? | No | — |

### Eval pairs
```jsonl
{"id":"prd-001","category":"product","en":"Add to the sprint backlog","bad":"Thêm vào tồn đọng chạy nước rút","good":"Thêm vào sprint backlog","diagnosis":"agile terms stay English in VN product teams","expected_rules":["PROD001"]}
{"id":"prd-002","category":"product","en":"Do you agree the app is easy to use?","bad":"Bạn có đồng ý ứng dụng dễ dùng không? (Đồng ý/Không đồng ý)","good":"Mức độ dễ sử dụng của ứng dụng? (Rất khó – Rất dễ)","diagnosis":"agree/disagree scale triggers acquiescence bias","expected_rules":["PROD002"]}
{"id":"prd-003","category":"product","en":"Onboarding roadmap","bad":"Bản đồ đường lên tàu","good":"Lộ trình onboarding","diagnosis":"bản đồ đường/lên tàu are calques","expected_rules":["PROD001"]}
{"id":"prd-004","category":"product","en":"Allow notifications?","bad":"Kính thưa Quý khách, cho phép thông báo?","good":"Cho phép [App] gửi thông báo cho bạn?","diagnosis":"in-app permission prompt over-formal","expected_rules":[]}
{"id":"prd-005","category":"product","en":"We fixed bugs and improved speed","bad":"Chúng tôi đã sửa những con bọ","good":"Đã sửa một số lỗi và cải thiện tốc độ","diagnosis":"release notes: con bọ jokey; use lỗi","expected_rules":["PROD001"]}
{"id":"prd-006","category":"product","en":"As a user I want to reset my password","bad":"Như một người dùng tôi muốn đặt lại mật khẩu","good":"Là người dùng, tôi muốn đặt lại mật khẩu","diagnosis":"Như một = calque of 'as a'; native is Là","expected_rules":[]}
{"id":"prd-007","category":"product","en":"We collect your data to improve service","bad":"Chúng tôi lấy dữ liệu của bạn","good":"Bạn đồng ý cho [App] thu thập dữ liệu nhằm mục đích [X]?","diagnosis":"consent copy must be explicit + purpose (NĐ 13/2023)","expected_rules":["PROD004"]}
{"id":"prd-008","category":"product","en":"How likely are you to recommend us? 0-10","bad":"Bạn có giới thiệu chúng tôi không? Có/Không","good":"Khả năng bạn giới thiệu [App] cho bạn bè? (0–10)","diagnosis":"NPS must be 0-10 scale, not yes/no","expected_rules":["PROD002"]}
{"id":"prd-009","category":"product","en":"App store subtitle","bad":"Ứng dụng quản lý tài chính cá nhân tốt nhất số 1 Việt Nam","good":"Quản lý tài chính cá nhân đơn giản","diagnosis":"superlative + over-length subtitle","expected_rules":["PROD003"]}
{"id":"prd-010","category":"product","en":"Empty state: no items yet","bad":"Trạng thái trống","good":"Chưa có mục nào. Nhấn + để thêm.","diagnosis":"empty-state UI text must be user-facing, not the internal term","expected_rules":["PROD001"]}
```

### Open questions for a native speaker
- Magnitude of positivity skew for Vietnamese NPS vs regional benchmark (needs local research citation).
- Whether `lộ trình` fully displaces `roadmap` in current product-team speech.
- App-store keyword duplication (accented/unaccented): rewarded or penalized under current store rules.

---

## Function: Finance

### Genre inventory
| Artifact | Who writes it | Register | Length / format norms |
|---|---|---|---|
| Hóa đơn điện tử | Accounting | formal 3rd-person | Mandated fields; MST; thuế GTGT |
| Báo cáo tài chính | Accounting | formal | TT 99/2025 account names; `Đơn vị tính` |
| Management report / budget / forecast | Finance | formal/impersonal | Tables; `triệu`/`tỷ` |
| Investor update / board deck | CFO/IR | formal | Narrative + tables |
| Pricing / payment-terms page | Finance/Product | `Quý khách` | Clear fees |
| Fintech/banking/insurance product copy | Marketing/Compliance | `Quý khách` | Regulated |
| Loan / credit disclosure | Compliance | `Quý khách`/formal | Mandated transparency |
| Tax filing / correspondence | Accounting | formal | Official terms |
| Expense policy | Finance/HR | impersonal | Rules |

### Register and address (deltas only)
- Finance is almost entirely **`Quý khách`** (customer-facing) or **impersonal formal 3rd-person** (statements, policy). `bạn` appears only in fintech apps targeting youth — and even there, money screens skew formal. A hard register floor the base matrix should note.

### Terminology (authoritative statement terms — TT 99/2025/TT-BTC, in force 01/01/2026)
| EN | ✅ native (authoritative) | Notes |
|---|---|---|
| Balance sheet | `Báo cáo tình hình tài chính` (was `Bảng cân đối kế toán`) | TT 99/2025 renamed it — Mẫu B01-DN |
| Income statement | `Báo cáo kết quả hoạt động kinh doanh` | |
| Cash flow statement | `Báo cáo lưu chuyển tiền tệ` | |
| Chart of accounts | `Hệ thống tài khoản kế toán` | TT 99/2025 restructured; firms may self-design |
| VAT | `Thuế GTGT` (giá trị gia tăng) | e-invoice mandatory field |
| Corporate income tax | `Thuế TNDN` | |
| Personal income tax | `Thuế TNCN` | |
| Tax code | `MST` (mã số thuế) | e-invoice mandatory |
| Unit: million VND | `Đơn vị tính: triệu đồng` | table header convention |
| Fiscal year | `Năm tài chính` | |

### Regulated and banned language (HEADLINE — highest legal risk)
| Phrase / practice | Instrument | Article | Effective | Status 2026 | Safe rewrite |
|---|---|---|---|---|---|
| Guaranteed-return / "cam kết lợi nhuận" soliciting securities/fund purchase | Luật Chứng khoán 54/2019/QH14 (amended Luật 56/2024/QH15) | Điều 12 | 01/01/2021 | in force | state risk; no profit commitment |
| Profit commitment in fund fund-raising materials | NĐ 38/2018/NĐ-CP | Điều 2 kh.4 | 2018 | in force | "Không được cam kết lợi nhuận…" — drop it |
| Disclosure containing advertising/solicitation | NĐ 155/2020/NĐ-CP (amended NĐ 245/2025) | disclosure provisions | 01/01/2021 | in force | separate disclosure from marketing |
| False/misleading insurance advertising | Luật KDBH 08/2022/QH15 (amended Luật 139/2025) | Điều 9; Điều 129 kh.3 | 01/01/2023 | in force | accurate scope/terms |
| Investment-linked insurance without risk disclosure / "là sản phẩm bảo hiểm" statement | TT 67/2023/TT-BTC | Điều 53 | 02/11/2023 | in force | mandatory recording, risk disclosure, not-a-bank-product statement, 60-day bank ban |
| Consumer-credit rate advertised without transparent framework | TT 43/2016/TT-NHNN (amended TT 18/2019/TT-NHNN) | Điều 9, 10a | 15/03/2017 | in force | publicly post rate framework, fees, calc method |
| Misleading "lãi suất 0%" without total-cost disclosure | Luật QC + TT 43/2016 transparency | — | in force | disclose all fees; state effective rate |
| Crypto/virtual-asset solicitation via unlicensed platform | NQ 05/2025/NQ-CP; NĐ 284/2026/NĐ-CP | NQ Đ7; NĐ Đ9 | pilot 09/09/2025; penalties 01/09/2026 | in force | only MOF-licensed providers; not legal tender |

Crypto is legally recognized as "tài sản số" under Luật Công nghiệp công nghệ số 2025 (Luật 71/2025/QH15, Chương V, eff. 01/01/2026), but it is **not legal tender**; issuance/trading/solicitation is permitted only within the NQ 05/2025 pilot through MOF-licensed Vietnamese entities.

### Formatting conventions (not already in locale-formatting.md)
- **`Đơn vị tính: triệu đồng`** (or `tỷ đồng`) header on statement tables — mandatory reading aid.
- **Negative numbers in parentheses** `(1.234)` in statements, not a minus sign.
- `tỷ`/`triệu` in narrative prose; grouped digits (`2.500.000`) in tables — do not mix within one context.
- VND vs USD: state currency explicitly; conversion rate footnoted.
- Quarter naming: `Quý I/II/III/IV`, `năm tài chính`.
- Rounding disclosed in notes.

### Observed failure modes
- LLMs using `Bảng cân đối kế toán` (pre-2026 term) instead of `Báo cáo tình hình tài chính` — stale after TT 99/2025.
- Guaranteed-return phrasing (`cam kết lợi nhuận X%`) in fund/investment copy — statutory violation.
- `lãi suất 0%` headline without fee disclosure — misleading-advertising exposure; documented consumer-harm ("cái bẫy") in Vietnamese press (Báo Đầu Tư, VietnamNet).
- English number format (`2,500,000.00`) instead of `2.500.000` (inherited number rule, high-stakes here).
- Minus-sign negatives instead of parentheses in statements.

### Proposed lint rules
| ID | Severity | Catches | Regex-feasible? | False-positive risk |
|---|---|---|---|---|
| FIN001 | warn | Guaranteed-return `cam kết lợi nhuận`/`cam kết lãi suất`/`lợi nhuận X%/năm` in promo | Yes | Med |
| FIN002 | warn | `lãi suất 0%`/`0đ` without adjacent fee/total-cost disclosure | Partial | High |
| FIN003 | error | Stale statement term `Bảng cân đối kế toán` | Yes | Low |
| FIN004 | warn | Number not in VN format in a finance doc (`2,500,000`) | Yes | Med |
| FIN005 | info | Statement table missing `Đơn vị tính` header | Partial | Med |
| FIN006 | warn | Negative in statement with minus sign not parentheses | Partial | Med |
| FIN007 | error | E-invoice missing mandatory field (`MST`, `thuế GTGT`) | Partial | Med |
| FIN008 (human) | n/a | Is investment-linked/insurance disclosure complete? | No | — |
| FIN009 (human) | n/a | Crypto solicitation via licensed provider only? | No | — |

### Eval pairs
```jsonl
{"id":"fin-001","category":"finance","en":"Guaranteed 12% annual return","bad":"Cam kết lợi nhuận 12%/năm","good":"Lợi nhuận kỳ vọng; đầu tư có rủi ro, không cam kết lợi nhuận","diagnosis":"guaranteed-return banned (Luật CK Đ12; NĐ 38/2018)","expected_rules":["FIN001"]}
{"id":"fin-002","category":"finance","en":"0% interest installment","bad":"Trả góp lãi suất 0%","good":"Trả góp lãi suất 0% (đã bao gồm mọi phí; tổng chi phí: [X])","diagnosis":"0% without fee disclosure is misleading","expected_rules":["FIN002"]}
{"id":"fin-003","category":"finance","en":"Balance sheet","bad":"Bảng cân đối kế toán","good":"Báo cáo tình hình tài chính","diagnosis":"renamed by TT 99/2025 effective 01/01/2026","expected_rules":["FIN003"]}
{"id":"fin-004","category":"finance","en":"Revenue 2,500,000,000 VND","bad":"Doanh thu 2,500,000,000 VND","good":"Doanh thu 2.500.000.000 ₫ (2,5 tỷ đồng)","diagnosis":"English number format in finance doc","expected_rules":["FIN004"]}
{"id":"fin-005","category":"finance","en":"Loss of 1,234 million","bad":"Lỗ -1.234","good":"(1.234)","diagnosis":"statement negatives use parentheses","expected_rules":["FIN006"]}
{"id":"fin-006","category":"finance","en":"Table header, unit million VND","bad":"(no unit header)","good":"Đơn vị tính: triệu đồng","diagnosis":"statement tables require Đơn vị tính header","expected_rules":["FIN005"]}
{"id":"fin-007","category":"finance","en":"VAT invoice for customer","bad":"Hóa đơn (no MST, no thuế GTGT line)","good":"Hóa đơn GTGT — MST: [x] — Thuế GTGT: [x]","diagnosis":"e-invoice mandatory fields (NĐ 123/2020, NĐ 70/2025)","expected_rules":["FIN007"]}
{"id":"fin-008","category":"finance","en":"Investment-linked insurance pitch","bad":"Vừa bảo hiểm vừa sinh lời chắc chắn","good":"Sản phẩm bảo hiểm liên kết đầu tư; kết quả đầu tư không được đảm bảo, do bên mua chịu rủi ro","diagnosis":"must disclose risk + is-insurance-product (TT 67/2023 Đ53)","expected_rules":["FIN001"]}
{"id":"fin-009","category":"finance","en":"Buy crypto on our platform","bad":"Đầu tư crypto sinh lời trên sàn quốc tế","good":"Giao dịch tài sản mã hóa chỉ qua tổ chức được Bộ Tài chính cấp phép (NQ 05/2025)","diagnosis":"crypto solicitation only via licensed providers","expected_rules":["FIN001"]}
{"id":"fin-010","category":"finance","en":"Q4 fiscal year","bad":"Quarter 4 fiscal year","good":"Quý IV năm tài chính 2026","diagnosis":"use Vietnamese quarter/fiscal-year naming","expected_rules":[]}
{"id":"fin-011","category":"finance","en":"Personal income tax withheld","bad":"Thuế thu nhập cá nhân (PIT)","good":"Thuế TNCN","diagnosis":"use standard abbreviation TNCN","expected_rules":[]}
{"id":"fin-012","category":"finance","en":"Highest interest rate on the market","bad":"Lãi suất cao nhất thị trường","good":"Lãi suất cạnh tranh","diagnosis":"superlative without proof (Luật QC Đ8 kh11)","expected_rules":["LAW001"]}
```

### Open questions for a native speaker (accountant + securities/insurance lawyer)
- Full mapping of renamed/added/removed accounts under TT 99/2025 (215x series added; some 111x/112x sub-accounts removed) — needs an accountant to build the glossary.
- Whether any public-fund advertising rule verbatim bans `cam kết lợi nhuận` (the ban is assembled from Điều 12 Luật CK + NĐ 155/2020 + type-specific NĐ 38/2018, not one article).
- Exact mandated e-invoice field label strings under the NĐ 70/2025 amendment.
- Current SBV stance on `lãi suất 0%` headline advertising (practice widespread; enforcement uneven).

---

## Cross-cutting findings

**1. Architecture.** Three skills (business-comms, tech-writing, finance-copy), rationale and frontmatter above. Grouping is by shared failure-mode engine, not by org chart. Finance stays alone because its validator profile must be legally conservative in ways that would produce false positives elsewhere.

**2. Shared references.** Use a generated build step (`scripts/sync_shared.py`, stdlib-only) copying `shared/*.md` into each skill's `references/`, with a CI hash check. Honest cost: one CI job + edit-the-canonical discipline. Chosen over duplication (drifts), symlinks (break relative-link tests), and cross-skill naming (spec keeps references one-level-deep inside each folder).

**3. Validator reuse.** Universal (keep as-is): NFC rule, tone-mark single-style rule, `NUM` number-format, `LAW001` superlative (warn + `<!-- proof -->` suppress), `CAL` calque base. Need per-domain profiles: register set must extend beyond `re|saas|formal|consult` to add `zns`, `b2b`, `eng-impersonal`, `finance-formal`. New rule families: `ZNS*`, `MKT*`, `SALES*`, `ENG*`, `PROD*`, `FIN*`. **Not machine-checkable (→ human QA checklist):** xưng hô age/seniority correctness (SALES005), calque naturalness (ENG006), survey-item bias (PROD005), insurance/crypto disclosure completeness (FIN008/009), KOL disclosure truthfulness (MKT004).

**4. Failure-mode evidence.** Observed (not inferred): MT producing "câu từ vô nghĩa, sai nội dung" (Báo Thanh Hóa); Viblo corpus confirming `deploy`/`commit`/`bug` stay English; documented acquiescence bias (~10% average per Krosnick's handbook); `lãi suất 0%` "cái bẫy" consumer-harm reporting; the exact ZNS/ZBS content restrictions from Zalo's own policy pages. Inferred (labeled): specific per-genre emoji-density norms; exact `em`→`tôi` switch threshold; app-store keyword-duplication reward/penalty (sources conflict).

**5. Prioritisation.** Finance → Marketing → Sales → Engineering → Product. Build Finance first (highest legal risk, densest checkable rules). Fold Product into tech-writing rather than shipping standalone. Do not build a standalone Legal/Compliance skill (it's a shared reference, not an artifact type).

## Sources
| URL | Publisher | Accessed | Type | Confidence |
|---|---|---|---|---|
| oa.zalo.me/home/documents/guides/zbs-template-message | Zalo (primary) | 2026-08-20 | primary | high |
| zalo.solutions/news/quy-dinh-chung-khi-kiem-duyet-mau-tin-zns | Zalo (primary) | 2026-08-20 | primary | high |
| baochinhphu.vn / luatvietnam.vn (NĐ 128/2024 sửa NĐ 81/2018) | Báo Chính Phủ / LuatVietnam | 2026-08-20 | near-primary | high |
| thuvienphapluat.vn (TT 99/2025 thay TT 200/2014) | Thư Viện Pháp Luật | 2026-08-20 | near-primary | high |
| thuvienphapluat.vn (Luật QC sửa đổi 2025, Điều 15a) | Thư Viện Pháp Luật | 2026-08-20 | near-primary | high |
| luatvietnam.vn / mst.gov.vn (NĐ 91/2020 anti-spam, Điều 13/32) | LuatVietnam / Bộ KH&CN | 2026-08-20 | near-primary | high |
| einvoice.vn / luatvietnam.vn (NĐ 123/2020 + NĐ 70/2025 e-invoice) | E-invoice / LuatVietnam | 2026-08-20 | secondary | med-high |
| thuvienphapluat.vn (Luật Chứng khoán 54/2019 Đ12) | Thư Viện Pháp Luật | 2026-08-20 | near-primary | high |
| thuvienphapluat.vn (Luật KDBH 08/2022 Đ9; TT 67/2023 Đ53) | Thư Viện Pháp Luật | 2026-08-20 | near-primary | high |
| xaydungchinhsach.chinhphu.vn (NQ 05/2025 crypto pilot) | Chính phủ | 2026-08-20 | primary | high |
| luatvietnam.vn (Luật 71/2025/QH15 tài sản số) | LuatVietnam | 2026-08-20 | near-primary | high |
| viblo.asia (deploy/commit/CI-CD term usage) | Viblo | 2026-08-20 | primary (corpus) | high |
| baothanhhoa.vn (Google Translate sai lệch nội dung) | Báo Thanh Hóa | 2026-08-20 | secondary | med |
| Krosnick 1999 (Annual Review Psych 50:537–567) & 2009 Handbook of Survey Research (acquiescence ~10%) | Stanford / academic | 2026-08-20 | secondary | high |
| gengo.com / transphere (VN string expansion 25–30%) | Gengo / Transphere | 2026-08-20 | secondary | med |
| baodautu.vn / vietnamnet.vn (lãi suất 0% cái bẫy) | Báo Đầu Tư / VietnamNet | 2026-08-20 | secondary | med |
| sapo.vn / misaeshop.vn (Shopee title conventions) | Sapo / MISA | 2026-08-20 | secondary | med |
| pwc.com/vn / deloitte.com (IFRS timeline) | PwC / Deloitte | 2026-08-20 | near-primary | high |

## Caveats and what I could not verify
- **NĐ 87/2026/NĐ-CP Điều 50 khoản 2** penalty figures and the specific competition-law fines (Washima, Cosmos Japan, Lotte) are inherited from the existing research brief; I did not independently re-verify them and they should be checked against the primary decree before encoding.
- The exact renamed/added/removed account codes under TT 99/2025 need an accountant to enumerate; I confirmed the balance-sheet rename and that 215x accounts were added and some 111x/112x sub-accounts removed, but not the full mapping.
- For public securities funds, **no single article verbatim bans `cam kết lợi nhuận`** — the prohibition is assembled from Luật CK Điều 12 (anti-fraud/solicitation) + NĐ 155/2020 (disclosure-content) + NĐ 38/2018 (express ban for startup funds). Encode FIN001 as a warn, not a hard block, and route to legal review.
- Shopee accented/unaccented keyword-duplication: practice sources say it's done, but whether the 2026 algorithm rewards or penalizes it is unverified — flagged as an open question.
- Emoji-density and North/South promotional-formula norms are practitioner lore; I found consistent patterns but no authoritative source — labeled inferred.
- IFRS mandatory-adoption timing is genuinely ambiguous: Quyết định 345/QĐ-BTC set "after 2025," but as of 2026 adoption remains largely voluntary/permitted (per PwC and Deloitte on Quyết định 2014/QĐ-TTg, 2025) rather than universally mandatory — treat "IFRS mandatory 2026" claims with caution. Note this is separate from the TT 99/2025 chart-of-accounts change, which IS mandatory from 01/01/2026.
- The VN string-expansion figure (~25–30%) comes from translation-industry sources (Gengo, Transphere), not a Vietnamese-specific academic study; treat as a planning heuristic for UI width, not a precise constant.