# -*- coding: utf-8 -*-
"""Rules for Vietnamese finance copy that a calque table cannot express.

Loaded automatically by validate_copy.py because the filename starts with `rules_`.
Standard library only, no imports from the engine — the contract is plain tuples.

This profile is deliberately more conservative than the others in the repo. Several
checks here would produce unacceptable false positives in a marketing skill and are
worth the noise in a finance one, because the cost of a miss is statutory rather than
stylistic.

FIN001 is the exception to the doctype rule: guaranteed-return language is prohibited
wherever it appears, so it is never gated. Every other rule waits for --doctype.

Two rules from the research are not implemented here because the engine already covers
them, and duplicating a rule id would let one be disabled while the other stays on:

    FIN003 (stale statement terminology) is a glossary row firing CAL001 at `error`.
    FIN004 (English number format)       is NUM001, which is already an error.
"""
from __future__ import annotations

import pathlib
import re

ERROR = "error"
WARN = "warning"

REF_DIR = pathlib.Path(__file__).resolve().parent.parent / "references"

RULE_DOCS = {
    "FIN001": "guaranteed-return language — route to legal review (Luật CK Đ12; NĐ 38/2018)",
    "FIN002": "promotional rate with no fee or total-cost disclosure (TT 43/2016 Đ9, 10a)",
    "FIN005": "statement table with no “Đơn vị tính” header",
    "FIN006": "negative written with a minus sign; statements use parentheses",
    "FIN007": "invoice missing a mandatory field (MST, thuế GTGT)",
}

DOCTYPES = {
    "statement": "a financial statement or reporting table",
    "e-invoice": "an electronic invoice (hóa đơn điện tử)",
    "financial-promotion": "marketing for a financial, banking, or insurance product",
    "disclosure": "a regulatory disclosure document",
    "loan": "loan, credit, or installment product copy",
}

# Loaded from references/glossary.md so the patterns stay editable in Markdown, the
# same way the calque and superlative blocklists do.
GUARANTEED_MARKER = "<!-- machine-readable: guaranteed-return -->"

# Fallback if the reference file is missing, so the highest-risk rule never silently
# switches itself off.
FALLBACK_GUARANTEED = (
    r"cam kết\s+(?:lợi nhuận|lãi suất|sinh lời)",
    r"đầu tư không (?:có )?rủi ro",
    r"bảo toàn vốn",
)

RATE_ZERO_RE = re.compile(
    r"(?<!\w)(?:lãi suất\s*0\s*%|0\s*%\s*lãi suất|trả góp\s*0\s*%|0\s*đ(?!\w))",
    re.IGNORECASE)
COST_DISCLOSURE_RE = re.compile(
    r"(?<!\w)(phí|tổng chi phí|lãi suất thực tế|chi phí chuyển đổi|"
    r"tổng số tiền phải trả)(?!\w)", re.IGNORECASE)

UNIT_HEADER_RE = re.compile(r"đơn vị tính", re.IGNORECASE)
TABLE_ROW_RE = re.compile(r"^\s*\|.*\|\s*$")

# A grouped or bare number carrying a leading minus. Guarded so that 2020-2026 and a
# table separator row do not match.
MINUS_NUMBER_RE = re.compile(r"(?<![\w\d.,])[-−–]\s?\d{1,3}(?:\.\d{3})*(?:,\d+)?(?![\w])")

MST_RE = re.compile(r"(?<!\w)MST(?!\w)", re.IGNORECASE)
VAT_RE = re.compile(r"(?<!\w)(thuế\s*GTGT|giá trị gia tăng)(?!\w)", re.IGNORECASE)


def _load_guaranteed_patterns():
    """Parse the guaranteed-return table out of references/glossary.md."""
    path = REF_DIR / "glossary.md"
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        text = ""
    index = text.find(GUARANTEED_MARKER)
    raw = []
    if index != -1:
        started = False
        for line in text[index + len(GUARANTEED_MARKER):].splitlines():
            line = line.strip()
            if not line.startswith("|"):
                if started:
                    break
                continue
            started = True
            if set(line) <= set("|-: "):
                continue
            cells = [c.replace(r"\|", "|").strip()
                     for c in re.split(r"(?<!\\)\|", line)[1:-1]]
            if cells:
                raw.append(cells[0].strip().strip("`").strip())
        raw = raw[1:]                                # drop the header row
    compiled = []
    for pattern in raw or FALLBACK_GUARANTEED:
        try:
            compiled.append(re.compile(pattern, re.IGNORECASE))
        except re.error:
            continue
    return compiled or [re.compile(p, re.IGNORECASE) for p in FALLBACK_GUARANTEED]


GUARANTEED = _load_guaranteed_patterns()


def _is_comment_or_blank(line):
    stripped = line.strip()
    return not stripped or stripped.startswith(("#", "<!--", "//"))


def check_line(ctx, lineno, raw, masked):
    # Never gated: this phrasing is prohibited wherever it appears.
    for regex in GUARANTEED:
        for match in regex.finditer(masked):
            yield ("FIN001", WARN, match.start() + 1, match.group(0),
                   f"guaranteed-return language “{match.group(0)}”",
                   "prohibited in investment solicitation (Luật Chứng khoán Đ12; "
                   "NĐ 38/2018 Đ2 kh.4). Write “lợi nhuận kỳ vọng” with a risk "
                   "statement, and send this to legal review — the linter is not the "
                   "authority here")

    if ctx.doctype == "statement":
        if _is_comment_or_blank(raw):
            return
        for match in MINUS_NUMBER_RE.finditer(masked):
            yield ("FIN006", WARN, match.start() + 1, match.group(0).strip(),
                   f"negative written as “{match.group(0).strip()}”",
                   "statements write negatives in parentheses — (1.234), not -1.234")


def check_document(ctx):
    doctype = ctx.doctype
    body = "\n".join(ctx.masked)
    first = next((i for i, raw in enumerate(ctx.lines, 1)
                  if not _is_comment_or_blank(raw)), 1)

    # A promotional rate needs its total cost, in any finance document type.
    if doctype in ("financial-promotion", "loan", "statement", "e-invoice", "disclosure"):
        match = RATE_ZERO_RE.search(body)
        if match and not COST_DISCLOSURE_RE.search(body):
            line = body[:match.start()].count("\n") + 1
            yield ("FIN002", WARN, line, 1, match.group(0),
                   f"“{match.group(0)}” with no fee or total-cost disclosure",
                   "TT 43/2016/TT-NHNN (as amended by TT 18/2019) requires the fee "
                   "schedule and calculation method to be published — state the fees "
                   "and the total amount payable next to the rate")

    if doctype == "statement":
        has_table = any(TABLE_ROW_RE.match(raw) for raw in ctx.lines)
        if has_table and not UNIT_HEADER_RE.search(body):
            yield ("FIN005", WARN, first, 1, "",
                   "statement table with no “Đơn vị tính” header",
                   "add Đơn vị tính: triệu đồng (or tỷ đồng / VND) — without it a "
                   "reader cannot tell a million from a billion")

    if doctype == "e-invoice" and body.strip():
        if not MST_RE.search(body):
            yield ("FIN007", WARN, first, 1, "",
                   "invoice does not name a tax code (MST)",
                   "MST is a mandatory e-invoice field under NĐ 123/2020 as amended "
                   "by NĐ 70/2025")
        if not VAT_RE.search(body):
            yield ("FIN007", WARN, first, 1, "",
                   "invoice does not name the VAT treatment (thuế GTGT)",
                   "thuế GTGT is a mandatory e-invoice field under NĐ 123/2020 as "
                   "amended by NĐ 70/2025")
