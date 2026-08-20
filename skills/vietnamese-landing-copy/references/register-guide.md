<!-- vlc-disable: TONE001 -->

# Register guide — pronouns, prestige vocabulary, house style

Register is the highest-impact decision in Vietnamese copy and the one LLMs get wrong most
often. English collapses every form of address into "you"; Vietnamese does not. Picking the
wrong pronoun does not read as slightly off — it reads as a different company.

## The pronoun matrix

| Pronoun | Literal sense | Connotation | Use for | Avoid for |
|---|---|---|---|---|
| `quý khách` | esteemed customer | Deferential, commercial, warm-formal | Real estate, finance, insurance, airlines, hospitality, luxury retail, healthcare | Developer tools, youth brands — reads stiff and salesy |
| `quý vị` | esteemed persons | Very formal, plural, broadcast | Institutional pages, government, conference and event announcements, press | Anything transactional — reads like a podium speech |
| `anh/chị` | elder brother / elder sister | Warm but respectful, one-to-one | Sales consulting, brokerage, local services, mid-market B2B, chat and email follow-up | Broad public headlines — presumes a relationship you do not have |
| `bạn` | friend | Casual peer, modern | SaaS, tech, e-commerce, education, youth and lifestyle brands | Luxury or real estate — reads cheap and presumptuous |
| `khách hàng` | the customer | Third-person noun, not direct address | Policy text, terms, descriptive prose, FAQ answers about process | Direct address — `Khách hàng hãy đăng ký` is wrong; say `Quý khách vui lòng đăng ký` |

**Self-reference** pairs with it: `chúng tôi` (we, exclusive — the company) for all registers.
Use `chúng ta` (we, inclusive) only when genuinely including the reader, which marketing copy
rarely does. `Chúng tôi` is correct on a company page; `chúng ta` there is a common LLM error.

**One register per page.** Mixing `quý khách` in the hero with `bạn` in the FAQ is the single
most visible amateur tell. If different sections need different warmth, vary sentence length
and vocabulary — not the pronoun.

## The prestige axis: Hán-Việt vs thuần Việt

Sino-Vietnamese (Hán-Việt) vocabulary signals formality, permanence, and prestige. Pure
Vietnamese (thuần Việt) signals plainness, warmth, and modernity. This axis, not the pronoun
alone, is what makes real-estate copy sound like real-estate copy.

| Concept | Hán-Việt (prestige, RE/luxury) | Thuần Việt (plain, SaaS/retail) |
|---|---|---|
| create / build | `kiến tạo` | `xây dựng` / `tạo` |
| reside / settle | `an cư` | `sống` / `ở` |
| class, prestige | `đẳng cấp` | `sang` / `cao cấp` |
| prosperity | `thịnh vượng` | `giàu có` |
| quintessence | `tinh hoa` | `điều đặc sắc` |
| symbol | `biểu tượng` | `hình ảnh` |
| flourishing | `phồn vinh` | `phát triển` |
| experience | `trải nghiệm` | `dùng thử` |
| convenient | `tiện nghi` | `tiện lợi` |
| perfect / complete | `hoàn mỹ` | `đầy đủ` |

Real-estate headlines lean hard on this register: `Kiến tạo chốn an cư đẳng cấp`,
`Biểu tượng sống thịnh vượng`, `Nơi phồn vinh hội tụ`. SaaS headlines do the opposite:
`Quản lý công việc dễ dàng hơn`, `Bắt đầu miễn phí trong 2 phút`.

Do not sprinkle Hán-Việt into casual copy for flavour — it reads as pretentious. Do not
strip it from luxury copy for clarity — it reads as budget.

## Word order and grammar traps

1. **Modifier follows the noun.** `căn hộ cao cấp` (premium apartment), not
   `cao cấp căn hộ`. `dự án mới`, not `mới dự án`. This is the most frequent LLM error.
2. **Classifiers are mandatory with counted nouns.** Real estate uses `căn` (unit/apartment),
   `lô` (lot), `nền` (plot), `tòa` (tower/block), `block`, `phân khu` (subdivision).
   `2 căn hộ`, not `2 hộ`. `Tòa A`, not `A tòa`.
3. **Recast English passives.** `được thiết kế bởi X` is a calque of "designed by X". Write
   `do X thiết kế` or make it active: `X kiến tạo`. `Được` is fine as a genuine passive
   (`được cấp phép`, `được tin dùng`) — the defect is specifically `được ... bởi ...`.
4. **No grammatical plural.** `3 căn hộ`, never a pluralized noun. Plurality is carried by
   the number, or by `những` / `các` for indefinite plurals.
5. **Avoid stacked English loanwords** unless the audience is technical. `giải pháp` beats
   `solution`, `nền tảng` beats `platform`. `Demo`, `brochure`, `voucher`, and `combo` are
   naturalized and fine.

## Tone-mark placement (kiểu cũ vs kiểu mới)

For open syllables containing `oa`, `oe`, `uy`, two conventions exist for where the tone mark
sits:

| Kiểu cũ (old, visually centred) | Kiểu mới (new, phonetic) |
|---|---|
| `hòa`, `tòa`, `khỏe`, `thủy`, `hóa` | `hoà`, `toà`, `khoẻ`, `thuỷ`, `hoá` |

**Neither is wrong.** Kiểu mới matches school textbooks since Quyết định 1989/QĐ-BGDĐT
(~2022); kiểu cũ remains dominant on commercial websites. This skill defaults to kiểu mới and
lets you override. When a syllable has a final consonant (`toàn`, `hoàng`, `khoản`,
`thuyền`), there is no ambiguity — the mark always sits on the second vowel.

The actual defect is **mixing both in one document**. `validate_copy.py` rule `TONE001`
flags that and only that.

## Real-estate house style

Ornate, prestige-signalling, urgency-inflected. Section order is highly standardized —
see [glossary.md](glossary.md) for the exact labels.

- **Headlines** are aspirational noun phrases, not benefit claims:
  `Kiến tạo chốn an cư đẳng cấp giữa lòng thành phố`.
- **Scarcity and urgency** are expected, not pushy: `Số lượng có hạn`, `Ưu đãi mở bán`,
  `Nhanh tay đặt chỗ`, `Chỉ từ 2,5 tỷ`.
- **Every section funnels toward the lead form.** The page exists to collect a phone number.
- **Pháp lý (legal status) is a selling point** in Vietnam and buyers look for it explicitly —
  `Sổ hồng riêng`, `Pháp lý hoàn thiện`.

## SaaS / tech / e-commerce house style

The near-inverse.

- **Benefit-first headlines**, short declarative sentences, thuần Việt verbs.
- `bạn` throughout, minimal Hán-Việt.
- CTAs: `Dùng thử miễn phí`, `Bắt đầu ngay`, `Đăng ký miễn phí`.
- Concrete numbers over adjectives — and note that an unproven superlative is illegal while
  `nhanh hơn 3 lần` is a provable claim.

## Adding a register profile

New verticals (government, education, medical) are welcome contributions. Open a
`register-profile` issue with: the pronoun, the self-reference, five sample headlines from
real Vietnamese sites in that vertical, and the vocabulary that distinguishes it. See
[CONTRIBUTING.md](../../../CONTRIBUTING.md).
