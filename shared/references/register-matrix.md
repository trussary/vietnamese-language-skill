<!-- vlc-disable: TONE001 -->

# Register matrix — who the copy addresses

Shared by every skill in this repo. Vietnamese has **no neutral "you."** English collapses
every form of address into one word; Vietnamese does not. Picking the wrong pronoun does not
read as slightly off — it reads as a different company.

This file is the canonical list. Each skill's own register guide adds house style on top of
it; none of them redefine the matrix.

## The matrix

`validate_copy.py` parses the table below. Adding a register is adding a row — no code change.

- **Expects** — how this register addresses the reader. An empty cell means the register uses
  no direct address at all.
- **Forbids** — comma-separated pronouns that must not appear. `PRO002` fires on each.

<!-- machine-readable: registers -->

| Register | Expects | Forbids | Used for |
|---|---|---|---|
| `re` | `quý khách` | `bạn`, `mình` | Real estate, insurance, airlines, hospitality, luxury retail, healthcare |
| `formal` | `quý vị` | `bạn`, `mình` | Institutional pages, government, conference and press announcements |
| `consult` | `anh/chị` | `bạn`, `quý vị` | Sales consulting, brokerage, local services, chat and email follow-up |
| `saas` | `bạn` | `quý khách`, `quý vị` | SaaS, tech, e-commerce, education, youth and lifestyle brands |
| `b2b` | `anh/chị` | `bạn`, `quý vị` | B2B outreach, proposals, quotes — seniority-aware, see the sales skill |
| `zns` | `quý khách` | `bạn`, `mình` | Zalo ZNS/ZBS templates — the channel reads as a service notice, not marketing |
| `press` | `quý vị` | `bạn`, `mình`, `bọn mình` | Press releases, institutional third-person announcements |
| `livestream` | `cả nhà` | `quý vị`, `quý khách` | Livestream and spoken-register selling — written registers read stiff |
| `eng-impersonal` | | `bạn`, `quý khách`, `quý vị` | RFCs, design docs, postmortems, runbooks — no direct address at all |
| `eng-readme` | `bạn` | `quý khách`, `quý vị` | READMEs, tutorials, API docs, user-facing product and error copy |
| `finance-formal` | `quý khách` | `bạn`, `mình` | Statements, disclosures, financial promotion — a hard formality floor |

## Self-reference

`chúng tôi` (we, exclusive — the company) for all registers. `chúng ta` (we, inclusive) only
when genuinely including the reader, which commercial copy rarely does. `Chúng tôi` is correct
on a company page; `chúng ta` there is a common LLM error.

A junior seller writing to an older or more senior buyer correctly uses `em` for self
(`em gửi anh báo giá`). That is register-correct, not self-deprecating — see the
business-comms skill for the seniority rules.

## One register per document

Mixing `quý khách` in the hero with `bạn` in the FAQ is the single most visible amateur tell.
`PRO001` flags exactly this. If different sections need different warmth, vary sentence
length and vocabulary — not the pronoun.

The one deliberate exception is a **channel override**: a brand that uses `bạn` on its
landing page still uses `quý khách` inside a Zalo ZNS template, because the channel, not the
brand, sets the register there.

## Third-person address

`khách hàng`, `người dùng`, `nhà đầu tư` are third-person nouns, not forms of address. Use
them in policy text, terms, and descriptive prose. `Khách hàng hãy đăng ký` is wrong; write
`Quý khách vui lòng đăng ký`.

## Adding a register profile

Open a `register-profile` issue with: the pronoun, the self-reference, five sample headlines
from real Vietnamese sources in that vertical, and the vocabulary that distinguishes it. Then
add the row here — never in a generated copy under `skills/`.
