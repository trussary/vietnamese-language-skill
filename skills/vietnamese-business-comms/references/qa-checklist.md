<!-- vlc-disable: DIA001, CAL001, LAW001 -->

# QA checklist — human review rubric

The validator catches encoding, formatting, blocklisted phrases, and the doctype-gated
structural rules. The four highest-value checks in this skill are **none of those**: whether
the xưng hô fits the recipient, whether a KOL actually used the product, whether an opt-in
genuinely exists, and whether a superlative has real proof behind it.

## 1. Register and address

- [ ] Is the register right for the **channel**, not just the brand? A Zalo template is
      `Quý khách` even for a `bạn` brand.
- [ ] One register throughout — no `Quý khách` opening with a `bạn` CTA.
- [ ] **B2B: is `bạn` absent?** `bạn` in outreach is the clearest automation tell.
- [ ] Is the self-reference (`em` / `tôi` / `chúng tôi` / `bên em`) right for the writer's age
      and seniority relative to the recipient? — `SALES005`, not machine-checkable.
- [ ] Opening formality matches the relationship stage (`Kính gửi` cold, `Chào anh/chị` warm).
- [ ] Closing matches too — `Thân mến` only to an established contact.
- [ ] Cold outreach has a courtesy line before the ask.

## 2. Legal — the expensive section

- [ ] Every superlative either removed or carrying `<!-- proof: ... -->` naming a real,
      current document. **A proof annotation with nothing behind it is worse than the
      superlative**, because it silences the warning.
- [ ] Any discount over 50% backed by a registered `chương trình khuyến mại tập trung`.
- [ ] The "was" price in any was/now claim is the genuine pre-promotion price.
- [ ] No competitor named in a comparison.
- [ ] No person's image, name, or words used without consent — including testimonials.
- [ ] **Opt-in genuinely exists** for this list, and the send is inside the legal window.
- [ ] A working refusal mechanism is present and actually works.
- [ ] KOL/KOC brief specifies disclosure wording and placement, and the creator has used the
      product — `MKT004`, required from 01/01/2026.
- [ ] Health, supplement, pharmaceutical, or cosmetic copy routed to sector pre-approval.
- [ ] No financial promotion language — route to `vietnamese-finance-copy` and legal.

## 3. Channel mechanics

- [ ] ZNS/ZBS body under 400 characters có dấu.
- [ ] No marketing content in a transactional template.
- [ ] SMS length counted in Vietnamese — 70 characters per UCS-2 segment, not 160.
- [ ] Email subject under ~40 characters; preview text differs from the subject.
- [ ] Marketplace title: no ALL-CAPS, no emoji, conventional keyword order.
- [ ] Emoji density 1–3 in short social copy.
- [ ] Hashtags clustered at the end.
- [ ] Push notification value visible before truncation.

## 4. Idiomaticity

- [ ] Read it aloud. Does it sound like a Vietnamese marketer wrote it, or like an English
      campaign translated well?
- [ ] CTAs from the conventional list — `Mua ngay`, `Xem ngay`, `Đăng ký tư vấn` — rather than
      translated from the English button.
- [ ] E-commerce register uses market vocabulary (`Freeship`, `Deal`, `Voucher`) rather than
      formal renderings.
- [ ] No stacked English adjectives, no `hy vọng email này tìm thấy bạn`.
- [ ] Livestream script reads as speech, not as written copy.
- [ ] Press release is institutional third person throughout.

## 5. Sales artifacts

- [ ] Báo giá states VAT treatment (`đã` / `chưa bao gồm thuế GTGT`).
- [ ] Báo giá states a validity date.
- [ ] Payment terms and deposit (`đặt cọc`) wording present where relevant.
- [ ] Dunning escalates by specificity — named date, named amount — not by tone.
- [ ] Tết greeting uses the formulaic well-wishes, not an invented one.

## 6. Formatting

- [ ] NFC throughout; one tone-mark style.
- [ ] Prices `2.500.000 ₫`; colloquial `2,5 tỷ` in prose but never mixed with grouped digits
      in one context.
- [ ] Dates `dd/MM/yyyy`.
- [ ] Phone numbers `0xxx xxx xxx` or `+84` with the trunk zero dropped.
- [ ] Diacritics present — unaccented Vietnamese in a customer message reads as spam.

## Sign-off

A native Vietnamese speaker must approve any change to the glossary or the examples corpus.
For the legal section, a marketing-compliance reviewer — not a translator.

| Reviewer | Checks | Date |
|---|---|---|
| | Sections 1, 4 | |
| | Section 2 — legal | |
| | Sections 3, 5, 6 | |
