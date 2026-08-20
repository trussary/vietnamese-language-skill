# What this changes

<!-- One or two sentences. If it touches Vietnamese wording, say what and why. -->

## Type

- [ ] Glossary / terminology
- [ ] Examples corpus (`evals/pairs.jsonl`)
- [ ] Banned phrases or superlative patterns
- [ ] Register guide or a new register profile
- [ ] Locale formatting or legal reference
- [ ] Validator or font-coverage script
- [ ] SKILL.md, packaging, CI, or docs

## Checks

- [ ] `python -m pytest tests/ -q` passes
- [ ] `python tools/build_examples.py` run if `evals/pairs.jsonl` changed
      (`examples.md` is generated — never edit it by hand)
- [ ] `python skills/vietnamese-landing-copy/scripts/validate_copy.py skills/vietnamese-landing-copy/ --ext .md,.json,.template` is clean

## If this adds a blocklist entry

- [ ] The blocked phrase is **not** a substring of the phrase we recommend instead
- [ ] The blocked phrase is **not** ordinary Vietnamese in some other context —
      or it is, and the entry is a warning rather than an error
- [ ] I added a `good` example to `evals/pairs.jsonl` proving it does not misfire

## If this adds a legal or formatting rule

- [ ] The statute, decree, or standard is cited in the reference file

## Native speaker review

Changes to `glossary.md`, `examples.md`, or `evals/pairs.jsonl` require approval from a native
Vietnamese speaker before merge.

- [ ] I am a native Vietnamese speaker
- [ ] I am not — this needs native review

<!--
Reminder on two things we will not merge:
  - a change declaring one tone-mark convention (hòa vs hoà) correct — both are valid,
    only mixing them within one document is a defect;
  - making LAW001 an error — the law bans unproven superlatives, not the words themselves.
-->
