<!-- vlc-disable: DIA001, CAL001 -->

# QA checklist — what the linter cannot check

The validator catches encoding, formatting, calques from the blocklist, and a handful of
doctype-gated structural rules. Everything below needs a human, and most of it needs a human
who writes Vietnamese and ships software.

Work top to bottom. The first two sections catch more real defects than the rest combined.

## 1. Code-switching naturalness

- [ ] Read every sentence aloud. Would a Vietnamese engineer say it in a standup?
- [ ] Is any English term translated that should have stayed English (`commit`, `deploy`,
      `merge`, `sprint`, `backlog`)?
- [ ] Is any term left in English that this document's formality calls for in Vietnamese
      (`bộ nhớ đệm`, `cơ sở dữ liệu` in a published spec)?
- [ ] Are the both-forms-live terms (`server`/`máy chủ`, `cache`/`bộ nhớ đệm`) used
      **consistently** within the document?
- [ ] Does the document match the surrounding repo's existing house style?

This is `ENG006` in the research: the check no regex can make. A calque blocklist catches the
calques we have already seen. It cannot tell you whether a *new* translation reads natural.

## 2. Register

- [ ] Does the document type match its register in
      [doc-registers.md](doc-registers.md)?
- [ ] Is `bạn` absent from every RFC, design doc, postmortem, and runbook?
- [ ] Is `bạn` **present** in the README, tutorial, and user-facing microcopy?
- [ ] Is `quý khách` absent from everything except a customer-facing status page?
- [ ] One register per document, start to finish?

## 3. Error and empty-state copy

- [ ] Does each error say what happened **and** what to do next?
- [ ] Is any internal term (`empty state`, `end user`, `exception`, `invalid request`)
      leaking into user-visible text?
- [ ] Does any message blame the user rather than describing the state?
- [ ] Is the copy still meaningful with no context — read the string on its own?

## 4. i18n mechanics

- [ ] All values NFC-normalized.
- [ ] All keys ASCII.
- [ ] Every ICU plural is `other`-only.
- [ ] Longest string rendered in the narrowest container it can appear in.
- [ ] Font subset covers stacked diacritics (`ề`, `ộ`, `ữ`); line-height does not clip them.
- [ ] Search works when the user types without diacritics.
- [ ] Any character-limited surface counted in Vietnamese, after NFC normalization.

## 5. Commits, branches, identifiers

- [ ] Commit subjects and branch names ASCII, no diacritics.
- [ ] Identifiers ASCII.
- [ ] Vietnamese in the commit **body** is fine and does not need removing.

## 6. Product and research

- [ ] No agree/disagree scale anywhere in a survey.
- [ ] Every scale point labelled; endpoints name the property measured.
- [ ] No leading questions, and no question that presupposes its answer.
- [ ] NPS is 0–10, and is not being compared to a regional benchmark.
- [ ] Interview guide marks the address as a variable rather than fixing one pronoun.
- [ ] Consent copy states purpose, recording, and withdrawal.

## 7. Anything user-facing that makes a claim

- [ ] App-store listing free of unproven superlatives — see
      [banned-phrases.md](banned-phrases.md) and [compliance.md](compliance.md).
- [ ] Release notes describe what changed, not how good it is.
- [ ] No health, financial, or performance claim that nobody can document.

## Sign-off

A change to the glossary or the examples corpus needs a **native Vietnamese speaker who works
in software** to approve it. Fluency alone is not enough here: the whole skill turns on which
English words a Vietnamese engineer keeps, and that is trade knowledge, not language
knowledge.

| Reviewer | Checks | Date |
|---|---|---|
| | Sections 1–2 | |
| | Sections 3–5 | |
| | Sections 6–7 | |
