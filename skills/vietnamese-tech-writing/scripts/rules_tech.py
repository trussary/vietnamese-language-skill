# -*- coding: utf-8 -*-
"""Rules for Vietnamese engineering and product writing that a table row cannot express.

Loaded automatically by validate_copy.py because the filename starts with `rules_`.
Standard library only, and no imports from the engine — the contract is plain tuples.

Every rule here is gated on `--doctype`. That is deliberate: a 30-character limit is
correct for an App Store subtitle and nonsense for a design doc, and a rule that fires
on documents it was never meant for gets the whole linter switched off. If the caller
does not say what the artifact is, these rules stay silent.
"""
from __future__ import annotations

import re
import unicodedata

ERROR = "error"
WARN = "warning"

RULE_DOCS = {
    "ENG001": "diacritics in a commit subject, branch name, or identifier",
    "ENG003": "direct address in a document whose register is impersonal",
    "ENG007": "hedged instruction in a runbook; steps take the imperative",
    "PROD002": "agree/disagree scale in a survey — inflates scores via acquiescence bias",
    "PROD003": "app-store metadata over the platform character limit",
    "PROD004": "consent copy without an explicit purpose (Nghị định 13/2023/NĐ-CP)",
}

DOCTYPES = {
    "commit": "a git commit subject line — ASCII only",
    "branch": "a git branch name — ASCII only",
    "identifier": "code identifiers, i18n keys, filenames — ASCII only",
    "rfc": "an RFC or design doc — impersonal register",
    "postmortem": "a postmortem — impersonal register, no named individuals",
    "runbook": "an operational runbook — imperative steps",
    "survey": "a survey or research questionnaire",
    "app-store-title": "an app-store title (30 characters)",
    "app-store-subtitle": "an app-store subtitle (30 characters)",
    "app-store-short-description": "a Play Store short description (80 characters)",
    "consent": "consent or permission copy collecting personal data",
}

ASCII_ONLY = ("commit", "branch", "identifier")
IMPERSONAL = ("rfc", "postmortem")

# App-store limits are platform policy, not law. Sources: Apple App Store Connect
# (name 30, subtitle 30) and Google Play (title 30, short description 80).
CHAR_LIMITS = {
    "app-store-title": 30,
    "app-store-subtitle": 30,
    "app-store-short-description": 80,
}

# Direct address. `mình` is left out on purpose: it is normal in code review and in a
# PR description, neither of which is an impersonal document.
ADDRESS_RE = re.compile(r"(?<!\w)(bạn|quý khách|quý vị)(?!\w)", re.IGNORECASE)

# `bạn nên` / `bạn có thể` in a runbook makes a required step look optional at 3am.
HEDGE_RE = re.compile(r"(?<!\w)bạn\s+(nên|có thể|hãy)(?!\w)", re.IGNORECASE)

# The agree/disagree format, which is the one an LLM defaults to.
AGREE_SCALE_RE = re.compile(
    r"(?<!\w)(rất\s+)?(không\s+)?đồng\s*ý(?!\w)", re.IGNORECASE)
AGREE_QUESTION_RE = re.compile(
    r"(?<!\w)(có\s+)?đồng\s*ý\s+(rằng|với)(?!\w)", re.IGNORECASE)

# Consent copy has to name a purpose. These are the markers that a purpose is stated.
PURPOSE_RE = re.compile(
    r"(?<!\w)(nhằm mục đích|để|mục đích|phục vụ)(?!\w)", re.IGNORECASE)
CONSENT_RE = re.compile(r"(?<!\w)(đồng ý|cho phép|chấp thuận)(?!\w)", re.IGNORECASE)

# A commit subject may legitimately be a Conventional Commits prefix plus English.
NON_ASCII_RE = re.compile(r"[^\x00-\x7F]+")

# In a resource file only the KEY has to be ASCII — the value is supposed to be
# Vietnamese. Checking the whole line would flag every correct translation.
JSON_KEY_RE = re.compile(r'"([^"\\]*)"\s*:')


def _is_comment_or_blank(line: str) -> bool:
    stripped = line.strip()
    return not stripped or stripped.startswith("#") or stripped.startswith("<!--")


def _ascii_spans(doctype, raw):
    """(text, column offset) for the parts of the line that must be ASCII."""
    if doctype != "identifier":
        yield raw, 0
        return
    keys = list(JSON_KEY_RE.finditer(raw))
    if keys:
        for match in keys:
            yield match.group(1), match.start(1)
        return
    yield raw, 0                      # a bare identifier, not a resource-file line


def check_line(ctx, lineno, raw, masked):
    doctype = ctx.doctype
    if not doctype:
        return

    if doctype in ASCII_ONLY and not _is_comment_or_blank(raw):
        # Only the subject line of a commit is constrained; the body may be Vietnamese.
        if doctype == "commit" and lineno > 1:
            return
        for text, offset in _ascii_spans(doctype, raw):
            for match in NON_ASCII_RE.finditer(text):
                yield ("ENG001", ERROR, offset + match.start() + 1, match.group(0),
                       f"non-ASCII in a {doctype}: “{match.group(0)}”",
                       "commit subjects, branch names and identifiers must be ASCII. "
                       "In a resource file the key is ASCII and the value is Vietnamese; "
                       "in a commit the subject is ASCII and the body may be Vietnamese")

    if doctype in IMPERSONAL:
        for match in ADDRESS_RE.finditer(masked):
            yield ("ENG003", WARN, match.start() + 1, match.group(0),
                   f"“{match.group(0)}” in a {doctype}",
                   "this document describes a system, not a reader — write "
                   "“Hệ thống sẽ…”, “Cần cấu hình…”, or drop the subject entirely")

    if doctype == "runbook":
        for match in HEDGE_RE.finditer(masked):
            yield ("ENG007", WARN, match.start() + 1, match.group(0),
                   f"hedged instruction “{match.group(0)}” in a runbook",
                   "use the bare imperative — “Chạy migration trước”, not "
                   "“Bạn nên chạy migration trước”")

    if doctype == "survey":
        for match in AGREE_QUESTION_RE.finditer(masked):
            yield ("PROD002", WARN, match.start() + 1, match.group(0),
                   "agree/disagree question wording",
                   "ask about the property itself — “Mức độ dễ sử dụng của ứng dụng?” "
                   "with endpoints “Rất khó – Rất dễ”")
        for match in AGREE_SCALE_RE.finditer(masked):
            yield ("PROD002", WARN, match.start() + 1, match.group(0),
                   f"agree/disagree scale point “{match.group(0)}”",
                   "acquiescence bias inflates agreement by ~10 points; use an "
                   "item-specific scale instead — see references/survey-design.md")


def check_document(ctx):
    doctype = ctx.doctype
    if not doctype:
        return

    if doctype in CHAR_LIMITS:
        limit = CHAR_LIMITS[doctype]
        for lineno, raw in enumerate(ctx.lines, 1):
            text = raw.strip()
            if _is_comment_or_blank(raw):
                continue
            # Count after NFC: a decomposed ế is one character to a store, three to len().
            length = len(unicodedata.normalize("NFC", text))
            if length > limit:
                yield ("PROD003", WARN, lineno, 1, text[:40],
                       f"{length} characters, over the {limit}-character {doctype} limit",
                       "Vietnamese runs 25–30% longer than English — shorten rather "
                       "than relying on the platform to truncate")

    if doctype == "consent":
        text = "\n".join(ctx.masked)
        if CONSENT_RE.search(text) and not PURPOSE_RE.search(text):
            yield ("PROD004", WARN, 1, 1, text.strip().splitlines()[0][:40] if text.strip() else "",
                   "consent copy does not state a purpose",
                   "Nghị định 13/2023/NĐ-CP requires express, informed consent naming "
                   "the purpose — “… nhằm mục đích [X]”")
