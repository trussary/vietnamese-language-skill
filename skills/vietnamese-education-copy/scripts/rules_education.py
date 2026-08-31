# -*- coding: utf-8 -*-
"""Rules for Vietnamese school, academic, and EdTech writing that a calque table cannot express.

Loaded automatically by validate_copy.py because the filename starts with `rules_`.
Standard library only, no imports from the engine — the contract is plain tuples.

Every rule here is gated on `--doctype`, because the correct term depends on the schooling
stage and educational context: `cần cố gắng` is mandatory on a primary report card and simply
absent from a university transcript. A rule firing on a document it was never meant for is how
a whole linter gets switched off, so nothing here is checked without the caller declaring what
it is looking at.

Two things the research proposed are deliberately NOT custom rules here, because the engine's
existing mechanisms already cover them and duplicating a rule id would let one copy be disabled
while the other stays on:

    diploma-reissuance wording   is a glossary row firing CAL001 at error (see glossary.md) —
                                  the phrase is short and unconditionally wrong, so it needs no
                                  doctype gate.
    parent-address calques       are glossary rows firing CAL001 at warn, for the same reason.
"""
from __future__ import annotations

import re

ERROR = "error"
WARN = "warning"

RULE_DOCS = {
    "EDU001": "abolished secondary (THCS/THPT) overall grading term (Thông tư 22/2021)",
    "EDU002": "“bạn” addressing a student in a teacher's voice",
    "EDU003": "“cần cải thiện” on a primary report card instead of “cần cố gắng” (Thông tư 27/2020)",
    "EDU005": "“tín dụng” for academic credit instead of “tín chỉ” (Thông tư 08/2021)",
    "EDU006": "GPA written with a dot decimal instead of the Vietnamese comma",
    "EDU007": "literal empty-state phrase on EdTech UI without an actionable CTA",
    "EDU009": "unpedagogical or harsh pronunciation feedback violating the Sandwich model",
}

DOCTYPES = {
    "primary-report-card": "a primary-school (tiểu học) report card or sổ liên lạc entry",
    "secondary-report-card": "a secondary/high-school (THCS/THPT) report card or học bạ entry",
    "teacher-to-student": "a teacher addressing a student directly",
    "transcript": "a university transcript or GPA statement",
    "diploma": "diploma issuance or reissuance copy",
    "higher-ed": "university administrative prose — syllabi, course descriptions, registration",
    "pronunciation-feedback": "AI / teacher pronunciation diagnostic feedback",
    "edtech-microcopy": "EdTech product UI strings, empty states, and notifications",
    "pedagogical-nudge": "pedagogical reminder and habit-loop notifications",
    "parental-analytics": "learning analytics and progress reports for parents",
}

# The new (Thông tư 22/2021) overall scale is Tốt / Khá / Đạt / Chưa đạt. "Khá" carries over
# unchanged, so it is deliberately absent from this list — only the replaced tiers are a defect.
LEGACY_OVERALL_RE = re.compile(
    r"(?:xếp loại|đạt loại)\s+(giỏi|trung bình|yếu|kém)(?!\w)", re.IGNORECASE)
LEGACY_TITLE_RE = re.compile(r"(?<!\w)học sinh\s+tiên tiến(?!\w)", re.IGNORECASE)

ADDRESS_BAN_RE = re.compile(r"(?<!\w)bạn(?!\w)", re.IGNORECASE)

NEEDS_IMPROVEMENT_CALQUE_RE = re.compile(r"(?<!\w)cần\s+cải\s+thiện(?!\w)", re.IGNORECASE)

# "tín dụng sinh viên" (a student loan/credit product) is a real, correct phrase that this
# pattern will also match — accepted as a doctype-gated warn rather than an unconditional
# blocklist entry, since the false-positive is occasional and the miss (silently teaching
# "tín dụng" as the word for academic credit) is not.
CREDIT_CALQUE_RE = re.compile(r"(?<!\w)tín\s+dụng(?!\w)", re.IGNORECASE)

# A GPA is always written as one decimal over another (3.6/4.0, 8.5/10). The generic NUM003
# rule only fires next to tỷ/triệu/%/m², none of which sit next to a GPA.
GPA_DOT_RE = re.compile(r"(?<!\d)\d\.\d{1,2}\s*/\s*\d(?:\.\d{1,2})?(?!\d)")

# EdTech empty-state literal translations
EMPTY_STATE_CALQUE_RE = re.compile(r"(?<!\w)(?:trạng\s+thái\s+trống|không\s+có\s+dữ\s+liệu)(?!\w)", re.IGNORECASE)

# Unpedagogical harsh pronunciation feedback
HARSH_FEEDBACK_RE = re.compile(
    r"(?<!\w)(?:sai\s+rồi|bạn\s+(?:đã\s+)?phát\s+âm\s+sai|điểm\s+(?:phát\s+âm\s+)?của\s+bạn\s+là)(?!\w)",
    re.IGNORECASE,
)


def check_line(ctx, lineno, raw, masked):
    doctype = ctx.doctype
    if not doctype:
        return

    if doctype == "secondary-report-card":
        for match in LEGACY_TITLE_RE.finditer(masked):
            yield ("EDU001", ERROR, match.start() + 1, match.group(0),
                   f"abolished title “{match.group(0)}”",
                   "Thông tư 22/2021/TT-BGDĐT abolished “Học sinh Tiên tiến” as an "
                   "overall classification — use Tốt / Khá / Đạt / Chưa đạt")
        for match in LEGACY_OVERALL_RE.finditer(masked):
            yield ("EDU001", ERROR, match.start() + 1, match.group(0),
                   f"abolished overall classification “{match.group(0)}”",
                   "the overall scale is now Tốt / Khá / Đạt / Chưa đạt (Thông tư "
                   "22/2021/TT-BGDĐT Điều 9) — “Khá” itself is unaffected")

    if doctype == "teacher-to-student":
        for match in ADDRESS_BAN_RE.finditer(masked):
            yield ("EDU002", WARN, match.start() + 1, match.group(0),
                   f"“{match.group(0)}” addressing a student",
                   "a teacher addresses a student as em (secondary) or con (primary), never "
                   "bạn — see references/doc-registers.md")

    if doctype == "primary-report-card":
        for match in NEEDS_IMPROVEMENT_CALQUE_RE.finditer(masked):
            yield ("EDU003", ERROR, match.start() + 1, match.group(0),
                   f"“{match.group(0)}” instead of the statutory term",
                   "Thông tư 27/2020/TT-BGDĐT Điều 7 uses “cần cố gắng” for primary "
                   "routine assessment")

    if doctype in ("higher-ed", "transcript"):
        for match in CREDIT_CALQUE_RE.finditer(masked):
            yield ("EDU005", WARN, match.start() + 1, match.group(0),
                   f"“{match.group(0)}” for academic credit",
                   "academic credit is tín chỉ (Thông tư 08/2021/TT-BGDĐT); tín dụng is "
                   "financial credit — reserve it for genuinely financial phrases like "
                   "“tín dụng sinh viên”")

    if doctype == "transcript":
        for match in GPA_DOT_RE.finditer(masked):
            yield ("EDU006", ERROR, match.start() + 1, match.group(0),
                   f"GPA written with a dot decimal “{match.group(0)}”",
                   "Vietnamese transcripts use a decimal comma — write "
                   f"“{match.group(0).replace('.', ',')}”")

    if doctype == "edtech-microcopy":
        for match in EMPTY_STATE_CALQUE_RE.finditer(masked):
            yield ("EDU007", WARN, match.start() + 1, match.group(0),
                   f"literal empty-state phrase “{match.group(0)}”",
                   "never display raw “Trạng thái trống” / “Không có dữ liệu” — provide an "
                   "encouraging, actionable Call to Action (see references/edtech-pedagogy.md)")

    if doctype == "pronunciation-feedback":
        for match in HARSH_FEEDBACK_RE.finditer(masked):
            yield ("EDU009", WARN, match.start() + 1, match.group(0),
                   f"unpedagogical negative feedback “{match.group(0)}”",
                   "apply the Sandwich Feedback model (praise effort, provide constructive "
                   "phoneme/tone tip, encourage growth mindset — see references/edtech-pedagogy.md)")
