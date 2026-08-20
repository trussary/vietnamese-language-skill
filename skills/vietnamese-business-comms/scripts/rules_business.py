# -*- coding: utf-8 -*-
"""Rules for Vietnamese marketing and sales copy that a table row cannot express.

Loaded automatically by validate_copy.py because the filename starts with `rules_`.
Standard library only, no imports from the engine — the contract is plain tuples.

Everything here is gated on `--doctype`. A 400-character limit is right for a Zalo
template and meaningless for a landing page; an ALL-CAPS check is right for a
marketplace title and wrong for a headline. A rule that fires on documents it was
never meant for gets the whole linter switched off.
"""
from __future__ import annotations

import re
import unicodedata

ERROR = "error"
WARN = "warning"

RULE_DOCS = {
    "ZNS001": "marketing content inside a transactional Zalo template",
    "ZNS002": "Zalo ZNS/ZBS body over the 400-character limit",
    "MKT001": "ALL-CAPS or emoji in a marketplace listing title",
    "MKT002": "discount over the 50% ceiling (NĐ 81/2018 as amended by NĐ 128/2024)",
    "SALES001": "casual pronoun in B2B outreach, a quote, or a dunning notice",
    "SALES003": "formal outreach with no greeting line",
    "SALES004": "quote missing its VAT treatment or validity date",
    "SPAM001": "bulk message with no opt-out mechanism (NĐ 91/2020 Điều 13)",
}

DOCTYPES = {
    "zns": "a Zalo ZNS/ZBS template of any tag",
    "zns-transactional": "a Zalo template under a transactional tag — no marketing",
    "marketplace-title": "a Shopee/Lazada/TikTok Shop listing title",
    "cold-outreach": "a first-contact B2B email or Zalo message",
    "bao-gia": "a quote (báo giá) or price list",
    "dunning": "a payment reminder",
    "bulk-message": "a bulk SMS or email template sent to a list",
    "promo": "promotional copy carrying a discount claim",
}

ZNS_LIMIT = 400

B2B_DOCTYPES = ("cold-outreach", "bao-gia", "dunning")

# `bạn` and `mình` in B2B outreach are the clearest tell of an automated send.
CASUAL_RE = re.compile(r"(?<!\w)(bạn|mình|bọn mình)(?!\w)", re.IGNORECASE)

# Marketing verbs that must not appear under a transactional template tag.
PROMO_RE = re.compile(
    r"(?<!\w)(ưu đãi|giảm giá|khuyến mãi|khuyến mại|sale|flash sale|mua ngay|"
    r"đặt ngay|săn deal|voucher|mã giảm giá|freeship|deal)(?!\w)", re.IGNORECASE)

# "giảm 70%", "sale 70%", "giảm đến 70 %"
DISCOUNT_RE = re.compile(
    r"(?<!\w)(?:giảm|sale|off|khuyến mãi|khuyến mại)\s*(?:giá\s*)?(?:đến|tới|lên đến|up to)?\s*"
    r"(\d{1,3})\s*%", re.IGNORECASE)
# The counterpart of <!-- proof: ... --> for the concentrated-promotion exemption.
TAP_TRUNG_RE = re.compile(
    r"(?:<!--|//|/\*|#)\s*khuyen-mai-tap-trung\s*:", re.IGNORECASE)

GREETING_RE = re.compile(
    r"(?<!\w)(kính gửi|kính chào|dear|chào anh|chào chị|chào quý|thưa anh|thưa chị)",
    re.IGNORECASE)

VAT_RE = re.compile(r"(?<!\w)(thuế\s*gtgt|vat|giá trị gia tăng)(?!\w)", re.IGNORECASE)
VALIDITY_RE = re.compile(
    r"(?<!\w)(hiệu lực|có giá trị đến|áp dụng đến|báo giá có hiệu lực)", re.IGNORECASE)

OPT_OUT_RE = re.compile(
    r"(?<!\w)(từ chối nhận|hủy nhận tin|huỷ nhận tin|soạn\s+t[uư]\s+g[uư]i|"
    r"unsubscribe|ngừng nhận|dừng nhận)", re.IGNORECASE)

# Emoji and pictographic ranges that read as clone-listing spam in a title.
EMOJI_RE = re.compile(
    "[\U0001F000-\U0001FAFF☀-➿⬀-⯿️←-⇿]")

CAPS_RE = re.compile(r"(?<![\w])[A-ZÀ-Ỹ]{4,}(?![\w])")


def _is_comment_or_blank(line):
    stripped = line.strip()
    return not stripped or stripped.startswith(("#", "<!--", "//"))


def _visible_text(ctx):
    """The template body, minus comment and directive lines."""
    return [(i, raw) for i, raw in enumerate(ctx.lines, 1) if not _is_comment_or_blank(raw)]


def check_line(ctx, lineno, raw, masked):
    doctype = ctx.doctype
    if not doctype:
        return

    if doctype == "zns-transactional":
        for match in PROMO_RE.finditer(masked):
            yield ("ZNS001", WARN, match.start() + 1, match.group(0),
                   f"marketing wording “{match.group(0)}” in a transactional template",
                   "Zalo rejects promotional content under a transactional tag — move the "
                   "offer to a promotional template with its own opt-in")

    if doctype in B2B_DOCTYPES:
        for match in CASUAL_RE.finditer(masked):
            yield ("SALES001", WARN, match.start() + 1, match.group(0),
                   f"“{match.group(0)}” in a {doctype}",
                   "B2B writing uses anh/chị for the recipient and em or tôi for yourself — "
                   "see references/b2b-xung-ho.md")

    if doctype == "marketplace-title" and not _is_comment_or_blank(raw):
        for match in EMOJI_RE.finditer(raw):
            yield ("MKT001", WARN, match.start() + 1, match.group(0),
                   "emoji in a marketplace listing title",
                   "icons in a title read as a clone listing and risk a spam flag")
        for match in CAPS_RE.finditer(raw):
            yield ("MKT001", WARN, match.start() + 1, match.group(0),
                   f"ALL-CAPS “{match.group(0)}” in a marketplace listing title",
                   "capitals lower search ranking — use the conventional order: "
                   "loại sản phẩm + thương hiệu + tên + đặc điểm")

    if doctype in ("promo", "zns", "zns-transactional", "bulk-message", "marketplace-title"):
        if TAP_TRUNG_RE.search(raw):
            return
        for match in DISCOUNT_RE.finditer(masked):
            percent = int(match.group(1))
            if percent > 50:
                yield ("MKT002", WARN, match.start() + 1, match.group(0),
                       f"discount of {percent}% exceeds the 50% ceiling",
                       "NĐ 81/2018 as amended by NĐ 128/2024 caps a discount at 50% outside "
                       "a chương trình khuyến mại tập trung; annotate with "
                       "<!-- khuyen-mai-tap-trung: ... --> if one is registered")


def check_document(ctx):
    doctype = ctx.doctype
    if not doctype:
        return

    visible = _visible_text(ctx)
    body = "\n".join(raw for _, raw in visible)
    first_line = visible[0][0] if visible else 1

    if doctype in ("zns", "zns-transactional"):
        # Count after NFC: a decomposed ế is one character to Zalo and three to len().
        length = len(unicodedata.normalize("NFC", body))
        if length > ZNS_LIMIT:
            yield ("ZNS002", ERROR, first_line, 1, body[:40],
                   f"template body is {length} characters, over the {ZNS_LIMIT}-character limit",
                   "Zalo counts characters có dấu; shorten the body or move detail to a "
                   "landing page behind the CTA")

    if doctype == "cold-outreach" and body.strip() and not GREETING_RE.search(body):
        yield ("SALES003", WARN, first_line, 1, body.strip().splitlines()[0][:40],
               "cold outreach with no greeting line",
               "open with Kính gửi anh/chị … — a first line that goes straight to the pitch "
               "reads abrupt to the point of rudeness in Vietnamese B2B")

    if doctype == "bao-gia" and body.strip():
        if not VAT_RE.search(body):
            yield ("SALES004", WARN, first_line, 1, body.strip().splitlines()[0][:40],
                   "quote does not state its VAT treatment",
                   "state đã bao gồm thuế GTGT or chưa bao gồm thuế GTGT — a quote that "
                   "leaves it open is renegotiated later")
        if not VALIDITY_RE.search(body):
            yield ("SALES004", WARN, first_line, 1, body.strip().splitlines()[0][:40],
                   "quote does not state a validity period",
                   "add Báo giá có hiệu lực đến [ngày]")

    if doctype == "bulk-message" and body.strip() and not OPT_OUT_RE.search(body):
        yield ("SPAM001", WARN, first_line, 1, body.strip().splitlines()[0][:40],
               "bulk message with no visible opt-out mechanism",
               "NĐ 91/2020 Điều 13 requires a working refusal mechanism in every "
               "advertising message")
