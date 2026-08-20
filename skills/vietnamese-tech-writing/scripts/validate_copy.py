#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# GENERATED FILE — do not edit. Source: shared/scripts/validate_copy.py (sha256 90b8d1555ba2cc58).
# Edit the source and run `python tools/sync_shared.py`.
"""Lint Vietnamese (vi-VN) copy for the defects LLMs reliably produce.

Standard library only, Python 3.9+. No install step — that is deliberate: a skill
script that needs `pip install` does not get run.

    python validate_copy.py copy.md
    python validate_copy.py src/messages/ --register saas --strict
    python validate_copy.py copy.md --doctype commit
    python validate_copy.py copy.md --json
    python validate_copy.py copy.md --fix        # repairs NFC violations in place

Exit codes: 0 = clean or warnings only, 1 = errors present (or any finding with
--strict), 2 = bad invocation.

Nothing domain-specific is hardcoded here. Three kinds of rule data are loaded at
runtime, so that this one file can be byte-identical in every skill:

  * calque and superlative blocklists — parsed from ../references/glossary.md and
    ../references/banned-phrases.md;
  * register profiles — parsed from ../references/register-matrix.md;
  * domain rules — any `rules_*.py` sitting next to this file is imported and its
    checks are run alongside the universal ones.

Adding a phrase rule means adding a Markdown table row. Adding a rule that needs
real logic (character counts, number parsing) means adding it to the skill's own
`rules_<domain>.py`. Neither means editing this file.

Several rules are only correct for one kind of artifact — a 400-character limit
applies to a Zalo template and nothing else. Those rules are gated behind
`--doctype`, and stay silent unless the caller declares the artifact type.

Suppression:
    <!-- vlc-disable: CAL001, LAW001 -->   file-level, anywhere in the file
    <!-- vlc-disable: all -->              file-level, everything
    <!-- vlc-disable-line NUM001 -->       that line only
    <!-- proof: Khảo sát Nielsen 2026 -->  suppresses LAW001 on that line or the next
"""
from __future__ import annotations

import argparse
import json
import pathlib
import re
import sys
import unicodedata
from typing import Iterable, List, Optional, Sequence

ERROR = "error"
WARN = "warning"

SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
REF_DIR = SCRIPT_DIR.parent / "references"

DEFAULT_EXTENSIONS = (".md", ".mdx", ".markdown", ".txt", ".json", ".html", ".htm",
                      ".yaml", ".yml", ".ts", ".tsx", ".js", ".jsx", ".vue", ".svelte")

# Registers and the pronouns each one expects / forbids. This is the fallback used
# when references/register-matrix.md is missing; normally the matrix is the source.
DEFAULT_REGISTERS = {
    "re":      {"expects": "quý khách", "forbids": ("bạn",)},
    "formal":  {"expects": "quý vị",    "forbids": ("bạn",)},
    "consult": {"expects": "anh/chị",   "forbids": ("bạn", "quý vị")},
    "saas":    {"expects": "bạn",       "forbids": ("quý khách", "quý vị")},
}

FORMAL_PRONOUNS = ("quý khách", "quý vị")
CASUAL_PRONOUNS = ("bạn",)


# --------------------------------------------------------------------------- #
# Findings
# --------------------------------------------------------------------------- #
class Finding:
    __slots__ = ("rule", "severity", "path", "line", "col", "text", "message", "hint")

    def __init__(self, rule, severity, path, line, col, text, message, hint=""):
        self.rule = rule
        self.severity = severity
        self.path = path
        self.line = line
        self.col = col
        self.text = text
        self.message = message
        self.hint = hint

    def as_dict(self) -> dict:
        return {"rule": self.rule, "severity": self.severity, "file": str(self.path),
                "line": self.line, "column": self.col, "text": self.text,
                "message": self.message, "hint": self.hint}

    def render(self) -> str:
        tag = "error" if self.severity == ERROR else "warn "
        head = f"{self.path}:{self.line}:{self.col}: {tag} {self.rule}  {self.message}"
        if self.hint:
            head += f"\n      → {self.hint}"
        return head


# --------------------------------------------------------------------------- #
# Reference-file parsing — the blocklists live in Markdown, not in code
# --------------------------------------------------------------------------- #
def _table_with_header(text: str, marker: str) -> tuple:
    """Return (header_cells, data_rows) for the first Markdown table after `marker`.

    Callers need the header because some tables carry an optional `severity`
    column, and column position is not stable across reference files.
    """
    idx = text.find(marker)
    if idx == -1:
        return [], []
    rows: List[List[str]] = []
    started = False
    for raw in text[idx + len(marker):].splitlines():
        line = raw.strip()
        if not line.startswith("|"):
            if started:
                break
            continue
        started = True
        if set(line) <= set("|-: "):          # the header underline
            continue
        # split on unescaped pipes, then unescape
        cells = [c.replace(r"\|", "|").strip()
                 for c in re.split(r"(?<!\\)\|", line)[1:-1]]
        if cells:
            rows.append(cells)
    if not rows:
        return [], []
    return [c.strip().lower() for c in rows[0]], rows[1:]


def _table_after_marker(text: str, marker: str) -> List[List[str]]:
    """Just the data rows — the common case."""
    return _table_with_header(text, marker)[1]


def _severity_column(header: Sequence[str]) -> int:
    """Index of an optional `severity` column, or -1."""
    for i, cell in enumerate(header):
        if cell in ("severity", "mức độ"):
            return i
    return -1


def _parse_severity(cell: str) -> Optional[str]:
    value = _unwrap(cell).lower()
    if value in ("error", "lỗi"):
        return ERROR
    if value in ("warn", "warning", "cảnh báo"):
        return WARN
    return None


def _unwrap(cell: str) -> str:
    return cell.strip().strip("`").strip()


def _split_alternatives(cell: str) -> List[str]:
    return [_unwrap(part) for part in cell.split("/") if _unwrap(part) and _unwrap(part) != "—"]


class Blocklists:
    """Calque phrases and superlative patterns, loaded from the reference Markdown."""

    def __init__(self, ref_dir: pathlib.Path = REF_DIR):
        self.calques: List[tuple] = []        # (phrase, suggestion, source, severity|None)
        self.superlatives: List[tuple] = []   # (compiled regex, note)
        self.registers: dict = dict(DEFAULT_REGISTERS)
        self.missing: List[str] = []
        self._load_glossary(ref_dir / "glossary.md")
        self._load_banned(ref_dir / "banned-phrases.md")
        self._load_registers(ref_dir / "register-matrix.md")

    def _read(self, path: pathlib.Path) -> Optional[str]:
        try:
            return path.read_text(encoding="utf-8")
        except OSError:
            self.missing.append(str(path))
            return None

    def _load_glossary(self, path: pathlib.Path) -> None:
        text = self._read(path)
        if text is None:
            return
        header, rows = _table_with_header(text, "<!-- machine-readable: glossary -->")
        sev_col = _severity_column(header)
        for row in rows:
            if len(row) < 3:
                continue
            bad, good = _unwrap(row[1]), row[2]
            alternatives = _split_alternatives(good)
            if not bad or bad == "—":
                continue
            if bad in alternatives:            # row contradicts itself; skip it
                continue
            severity = _parse_severity(row[sev_col]) if 0 <= sev_col < len(row) else None
            self.calques.append((bad, " / ".join(alternatives), "glossary.md", severity))

    def _load_banned(self, path: pathlib.Path) -> None:
        text = self._read(path)
        if text is None:
            return
        header, rows = _table_with_header(text, "<!-- machine-readable: calques -->")
        sev_col = _severity_column(header)
        for row in rows:
            if len(row) < 2:
                continue
            bad, good = _unwrap(row[0]), _unwrap(row[1])
            severity = _parse_severity(row[sev_col]) if 0 <= sev_col < len(row) else None
            if bad and bad != "—":
                self.calques.append((bad, good, "banned-phrases.md", severity))
        for row in _table_after_marker(text, "<!-- machine-readable: superlatives -->"):
            if not row:
                continue
            pattern = _unwrap(row[0])
            note = row[2] if len(row) > 2 else ""
            try:
                self.superlatives.append((re.compile(pattern, re.IGNORECASE), note))
            except re.error as exc:
                print(f"warning: bad superlative regex {pattern!r} in banned-phrases.md: {exc}",
                      file=sys.stderr)

    def _load_registers(self, path: pathlib.Path) -> None:
        """Register profiles live in Markdown too — adding one is adding a row."""
        text = self._read(path)
        if text is None:
            return
        loaded = {}
        for row in _table_after_marker(text, "<!-- machine-readable: registers -->"):
            if len(row) < 3:
                continue
            name = _unwrap(row[0])
            if not name:
                continue
            forbids = tuple(_unwrap(part) for part in row[2].split(",")
                            if _unwrap(part) and _unwrap(part) != "—")
            loaded[name] = {"expects": _unwrap(row[1]), "forbids": forbids}
        if loaded:
            self.registers = loaded

    def compiled_calques(self):
        for phrase, suggestion, source, severity in self.calques:
            body = r"\s+".join(re.escape(w) for w in phrase.split())
            yield (re.compile(rf"(?<!\w){body}(?!\w)", re.IGNORECASE),
                   phrase, suggestion, source, severity)


# --------------------------------------------------------------------------- #
# Masking: text rules must not fire inside code
# --------------------------------------------------------------------------- #
FENCE_RE = re.compile(r"^\s*(```|~~~)")
INLINE_CODE_RE = re.compile(r"`[^`\n]*`")
URL_RE = re.compile(r"(?:https?://|www\.)\S+")


def mask_code(lines: Sequence[str], is_markdown: bool) -> List[str]:
    """Blank out code spans/fences and URLs, preserving line and column offsets."""
    masked: List[str] = []
    in_fence = False
    for line in lines:
        if is_markdown and FENCE_RE.match(line):
            in_fence = not in_fence
            masked.append(" " * len(line))
            continue
        if in_fence:
            masked.append(" " * len(line))
            continue
        out = line
        if is_markdown:
            out = INLINE_CODE_RE.sub(lambda m: " " * len(m.group(0)), out)
        out = URL_RE.sub(lambda m: " " * len(m.group(0)), out)
        masked.append(out)
    return masked


# --------------------------------------------------------------------------- #
# Suppressions
# --------------------------------------------------------------------------- #
# Directives work in any comment syntax — HTML, //, /* */, #, or a JSON string value —
# so they can live in .md, .json, .ts and .css alike. Terminators stop at the closing
# delimiter of whichever host syntax is in use.
_END = r'[^>*"\n]*'
FILE_DISABLE_RE = re.compile(rf"vlc-disable:\s*({_END}?)(?:-->|\*/|\"|$)", re.IGNORECASE)
LINE_DISABLE_RE = re.compile(rf"vlc-disable-line\s+({_END}?)(?:-->|\*/|\"|$)", re.IGNORECASE)
PROOF_RE = re.compile(r"(?:<!--|//|/\*|#)\s*proof\s*:", re.IGNORECASE)


def file_disabled_rules(text: str) -> set:
    rules = set()
    for match in FILE_DISABLE_RE.finditer(text):
        for token in re.split(r"[,\s]+", match.group(1)):
            if token:
                rules.add(token.strip().upper())
    return rules


def line_disabled_rules(line: str) -> set:
    rules = set()
    for match in LINE_DISABLE_RE.finditer(line):
        for token in re.split(r"[,\s]+", match.group(1)):
            if token:
                rules.add(token.strip().upper())
    return rules


# --------------------------------------------------------------------------- #
# Static rule patterns
# --------------------------------------------------------------------------- #
DIACRITIC_PHRASES = (
    "dang ky", "dang nhap", "tim hieu", "tim hieu them", "lien he", "can ho", "du an",
    "tien ich", "chinh sach", "khach hang", "quy khach", "thong tin", "bat dong san",
    "mat bang", "phap ly", "chu dau tu", "tong quan", "uu dai", "bao gia", "xem chi tiet",
    "dat lich", "tu van", "nha mau", "tien do", "thiet ke", "vi tri", "mien phi",
    "gio hang", "thanh toan", "ho va ten", "so dien thoai", "cam on", "gioi thieu",
    "san pham", "dich vu", "lien ket vung", "nhan bao gia", "so luong co han",
)
DIACRITIC_RE = re.compile(
    r"(?<![\w-])(" + "|".join(re.escape(p) for p in DIACRITIC_PHRASES) + r")(?![\w-])",
    re.IGNORECASE)

# Open-syllable oa/oe/uy: the only place the two tone-mark conventions differ.
VN_LETTER = r"a-zA-ZÀ-ỹ"
TONE_OLD_RE = re.compile(rf"(?<![{VN_LETTER}])[{VN_LETTER}]*[òóỏõọ][ae](?![{VN_LETTER}])")
TONE_OLD_UY_RE = re.compile(rf"(?<![{VN_LETTER}])[{VN_LETTER}]*(?<![qQ])[ùúủũụ]y(?![{VN_LETTER}])")
TONE_NEW_RE = re.compile(rf"(?<![{VN_LETTER}])[{VN_LETTER}]*o[àáảãạèéẻẽẹ](?![{VN_LETTER}])")
TONE_NEW_UY_RE = re.compile(rf"(?<![{VN_LETTER}])[{VN_LETTER}]*(?<![qQ])u[ỳýỷỹỵ](?![{VN_LETTER}])")

NUM_COMMA_GROUP_RE = re.compile(r"(?<![\d.,])\d{1,3}(?:,\d{3})+(?![\d,])")
NUM_UNGROUPED_RE = re.compile(r"(?<![\d.,])(\d{5,})(?![\d.,])\s*(VND|vnd|₫|đồng)")
NUM_DOT_DECIMAL_RE = re.compile(r"(?<![\d.,])\d+\.\d{1,2}(?![\d])\s*(?:tỷ|tỉ|triệu|nghìn|%|m²)")
SQM_RE = re.compile(r"(?<![\w])m2(?![\w])", re.IGNORECASE)
DATE_RE = re.compile(r"(?<![\d/])(\d{1,2})/(\d{1,2})/(\d{4})(?![\d/])")
PHONE_RE = re.compile(r"\+84[\s.-]*0")
ICU_PLURAL_LINE_RE = re.compile(r",\s*plural\s*,")
# Explicit-value selectors (=0 {…}) are legal and used; the CLDR *keywords* are not.
ICU_NON_OTHER_RE = re.compile(r"(?<!\w)(zero|one|two|few|many)\s*\{")

RULE_DOCS = {
    "NFC001": "Unicode is decomposed (NFD); emit precomposed NFC",
    "CAL001": "English calque — use the conventional Vietnamese wording",
    "LAW001": "regulated superlative — needs documented proof (Luật Quảng cáo Đ8 K11)",
    "DIA001": "Vietnamese text written without diacritics",
    "TONE001": "both tone-mark conventions used in one document",
    "NUM001": "comma used as a thousands separator; Vietnamese uses a period",
    "NUM002": "long number not grouped; use periods every three digits",
    "NUM003": "period used as a decimal separator; Vietnamese uses a comma",
    "NUM004": "ASCII m2; use the superscript m²",
    "DATE001": "date appears to be MM/dd/yyyy; Vietnamese uses dd/MM/yyyy",
    "PHONE001": "trunk zero kept after the +84 country code",
    "ICU001": "ICU 'one' plural branch; Vietnamese has only 'other'",
    "PRO001": "formal and casual pronouns mixed in one document",
    "PRO002": "pronoun does not match the declared register",
}


# --------------------------------------------------------------------------- #
# Domain rules — anything that is not expressible as a Markdown table row
# --------------------------------------------------------------------------- #
# A skill may drop a `rules_<domain>.py` next to this file. It is imported from this
# directory only (no package, no sys.path surgery, stdlib only), so the skill folder
# stays self-contained and independently installable.
#
# The contract, all parts optional:
#     RULE_DOCS   : dict[str, str]         merged into the global table
#     DOCTYPES    : dict[str, str]         accepted --doctype values and their help text
#     check_line(ctx, lineno, raw, masked) -> iterable of
#                       (rule, severity, col, snippet, message, hint)
#     check_document(ctx)                  -> iterable of
#                       (rule, severity, lineno, col, snippet, message, hint)
DOMAIN_MODULES: List = []
DOCTYPES: dict = {}


class Context:
    """What a domain rule is allowed to know about the file under test."""

    __slots__ = ("path", "lines", "masked", "text", "register", "doctype", "is_markdown")

    def __init__(self, path, lines, masked, text, register, doctype, is_markdown):
        self.path = path
        self.lines = lines
        self.masked = masked
        self.text = text
        self.register = register
        self.doctype = doctype
        self.is_markdown = is_markdown


def load_domain_rules(directory: Optional[pathlib.Path] = None) -> List:
    """Import every rules_*.py sitting beside this script and register its rules."""
    import importlib.util

    directory = directory or SCRIPT_DIR
    modules = []
    for path in sorted(directory.glob("rules_*.py")):
        spec = importlib.util.spec_from_file_location(path.stem, path)
        if spec is None or spec.loader is None:
            continue
        module = importlib.util.module_from_spec(spec)
        try:
            spec.loader.exec_module(module)
        except Exception as exc:                       # a broken rule file must not
            print(f"warning: cannot load {path.name}: {exc}", file=sys.stderr)
            continue                                   # take the whole linter down
        RULE_DOCS.update(getattr(module, "RULE_DOCS", {}))
        DOCTYPES.update(getattr(module, "DOCTYPES", {}))
        modules.append(module)
    DOMAIN_MODULES[:] = modules
    return modules


load_domain_rules()


# --------------------------------------------------------------------------- #
# The checker
# --------------------------------------------------------------------------- #
class Validator:
    def __init__(self, blocklists: Blocklists, register: Optional[str] = None,
                 doctype: Optional[str] = None):
        self.bl = blocklists
        self.calques = list(blocklists.compiled_calques())
        self.register = register
        self.doctype = doctype

    def check_file(self, path: pathlib.Path) -> List[Finding]:
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError) as exc:
            return [Finding("IO001", ERROR, path, 1, 1, "", f"cannot read file: {exc}")]

        disabled = file_disabled_rules(text)
        if "ALL" in disabled:
            return []

        lines = text.splitlines()
        is_markdown = path.suffix.lower() in (".md", ".mdx", ".markdown")
        masked = mask_code(lines, is_markdown)
        findings: List[Finding] = []

        def emit(rule, severity, lineno, col, snippet, message, hint=""):
            if rule in disabled:
                return
            if rule in line_disabled_rules(lines[lineno - 1]):
                return
            findings.append(Finding(rule, severity, path, lineno, col, snippet, message, hint))

        self._check_nfc(lines, path, emit)
        self._check_text_rules(lines, masked, path, emit)
        self._check_tone_consistency(masked, path, emit)
        self._check_pronouns(masked, path, emit)
        self._check_domain_rules(lines, masked, text, path, is_markdown, emit)

        findings.sort(key=lambda f: (f.line, f.col, f.rule))
        return findings

    # -- individual rule groups --------------------------------------------- #
    def _check_nfc(self, lines, path, emit) -> None:
        for i, line in enumerate(lines, 1):
            if unicodedata.normalize("NFC", line) == line:
                continue
            col = 1
            for j, ch in enumerate(line):
                if unicodedata.combining(ch):
                    col = max(1, j)
                    break
            emit("NFC001", ERROR, i, col, line.strip()[:60],
                 "text is not NFC-normalized (decomposed diacritics)",
                 "run with --fix, or text.normalize('NFC') at the source")

    def _check_text_rules(self, lines, masked, path, emit) -> None:
        for i, line in enumerate(masked, 1):
            raw = lines[i - 1]

            # Blocklist entries overlap by design ("ký lên" sits inside "đăng ký lên").
            # Report only the longest match covering a given span, or the output is noise.
            hits = [(m.start(), m.end(), phrase, suggestion, source, declared)
                    for regex, phrase, suggestion, source, declared in self.calques
                    for m in regex.finditer(line)]
            for start, end, phrase, suggestion, source, declared in hits:
                if any(other_start <= start and end <= other_end and
                       (other_end - other_start) > (end - start)
                       for other_start, other_end, *_ in hits):
                    continue
                matched = line[start:end]
                # A table row may declare its own severity; otherwise fall back to the
                # heuristic that a multi-word calque is a harder error than one word.
                severity = declared or (WARN if " " not in phrase else ERROR)
                hint = f"use “{suggestion}”" if suggestion else ""
                if source == "glossary.md":
                    hint += " (glossary.md)" if hint else "see glossary.md"
                emit("CAL001", severity, i, start + 1, matched,
                     f"calque “{matched}”", hint)

            proof_here = bool(PROOF_RE.search(raw))
            proof_above = i > 1 and bool(PROOF_RE.search(lines[i - 2]))
            if not (proof_here or proof_above):
                for regex, note in self.bl.superlatives:
                    for m in regex.finditer(line):
                        emit("LAW001", WARN, i, m.start() + 1, m.group(0),
                             f"regulated superlative “{m.group(0)}”",
                             "needs a licensed market survey or award certificate; annotate "
                             "with <!-- proof: ... --> or rewrite as a countable fact")

            for m in DIACRITIC_RE.finditer(line):
                emit("DIA001", WARN, i, m.start() + 1, m.group(0),
                     f"Vietnamese written without diacritics: “{m.group(0)}”",
                     "restore the tone marks; unaccented forms belong in slugs and meta only")

            for m in NUM_COMMA_GROUP_RE.finditer(line):
                fixed = m.group(0).replace(",", ".")
                emit("NUM001", ERROR, i, m.start() + 1, m.group(0),
                     f"comma-grouped number “{m.group(0)}”", f"write “{fixed}”")

            for m in NUM_UNGROUPED_RE.finditer(line):
                emit("NUM002", WARN, i, m.start() + 1, m.group(0),
                     f"ungrouped currency amount “{m.group(0)}”",
                     "group with periods, or use the tỷ/triệu scale in marketing copy")

            for m in NUM_DOT_DECIMAL_RE.finditer(line):
                fixed = m.group(0).replace(".", ",", 1)
                emit("NUM003", ERROR, i, m.start() + 1, m.group(0),
                     f"period used as a decimal separator in “{m.group(0)}”",
                     f"write “{fixed}”")

            for m in SQM_RE.finditer(line):
                emit("NUM004", WARN, i, m.start() + 1, m.group(0),
                     "ASCII “m2”", "use the superscript “m²”")

            for m in DATE_RE.finditer(line):
                first, second = int(m.group(1)), int(m.group(2))
                if second > 12 and first <= 12:
                    emit("DATE001", ERROR, i, m.start() + 1, m.group(0),
                         f"date “{m.group(0)}” looks like MM/dd/yyyy",
                         f"write “{m.group(2)}/{m.group(1)}/{m.group(3)}” (dd/MM/yyyy)")

            for m in PHONE_RE.finditer(line):
                emit("PHONE001", ERROR, i, m.start() + 1, m.group(0),
                     "trunk zero kept after +84", "drop the leading 0: +84 912 345 678")

            if ICU_PLURAL_LINE_RE.search(raw):
                for m in ICU_NON_OTHER_RE.finditer(raw):
                    category = m.group(1)
                    emit("ICU001", ERROR, i, m.start() + 1, m.group(0),
                         f"ICU plural has a “{category}” branch",
                         "Vietnamese has only the 'other' category — delete the "
                         f"'{category}' branch")

    def _check_tone_consistency(self, masked, path, emit) -> None:
        old_hit = new_hit = None
        for i, line in enumerate(masked, 1):
            for regex in (TONE_OLD_RE, TONE_OLD_UY_RE):
                m = regex.search(line)
                if m and old_hit is None:
                    old_hit = (i, m.start() + 1, m.group(0))
            for regex in (TONE_NEW_RE, TONE_NEW_UY_RE):
                m = regex.search(line)
                if m and new_hit is None:
                    new_hit = (i, m.start() + 1, m.group(0))
            if old_hit and new_hit:
                break
        if old_hit and new_hit:
            later = max(old_hit, new_hit, key=lambda h: (h[0], h[1]))
            other = old_hit if later is new_hit else new_hit
            emit("TONE001", WARN, later[0], later[1], later[2],
                 f"mixed tone-mark conventions: “{other[2]}” and “{later[2]}”",
                 "pick kiểu mới (hoà) or kiểu cũ (hòa) and use it throughout — neither is wrong")

    def _check_pronouns(self, masked, path, emit) -> None:
        def find_first(term):
            body = r"\s+".join(re.escape(w) for w in term.split())
            regex = re.compile(rf"(?<!\w){body}(?!\w)", re.IGNORECASE)
            for i, line in enumerate(masked, 1):
                m = regex.search(line)
                if m:
                    return (i, m.start() + 1, m.group(0))
            return None

        formal = next((h for h in (find_first(p) for p in FORMAL_PRONOUNS) if h), None)
        casual = next((h for h in (find_first(p) for p in CASUAL_PRONOUNS) if h), None)

        if formal and casual:
            later = max(formal, casual, key=lambda h: (h[0], h[1]))
            other = formal if later is casual else casual
            emit("PRO001", WARN, later[0], later[1], later[2],
                 f"mixed register: “{other[2]}” and “{later[2]}” in one document",
                 "one register per document — see references/register-matrix.md")

        if self.register:
            profile = self.bl.registers.get(self.register)
            if profile is None:
                return
            for forbidden in profile["forbids"]:
                hit = find_first(forbidden)
                if hit:
                    emit("PRO002", WARN, hit[0], hit[1], hit[2],
                         f"“{hit[2]}” does not fit the {self.register} register",
                         (f"this register addresses the reader as “{profile['expects']}”"
                          if profile["expects"]
                          else "this register uses no direct address at all"))

    def _check_domain_rules(self, lines, masked, text, path, is_markdown, emit) -> None:
        if not DOMAIN_MODULES:
            return
        ctx = Context(path, lines, masked, text, self.register, self.doctype, is_markdown)
        for module in DOMAIN_MODULES:
            per_line = getattr(module, "check_line", None)
            if per_line is not None:
                for i, line in enumerate(masked, 1):
                    for found in per_line(ctx, i, lines[i - 1], line) or ():
                        rule, severity, col, snippet, message, hint = found
                        emit(rule, severity, i, col, snippet, message, hint)
            whole = getattr(module, "check_document", None)
            if whole is not None:
                for found in whole(ctx) or ():
                    rule, severity, lineno, col, snippet, message, hint = found
                    emit(rule, severity, lineno, col, snippet, message, hint)


# --------------------------------------------------------------------------- #
# File collection, fixing, CLI
# --------------------------------------------------------------------------- #
def collect(paths: Iterable[str], extensions: Sequence[str]) -> List[pathlib.Path]:
    out: List[pathlib.Path] = []
    for raw in paths:
        p = pathlib.Path(raw)
        if p.is_dir():
            out.extend(sorted(q for q in p.rglob("*")
                              if q.is_file() and q.suffix.lower() in extensions))
        elif p.exists():
            out.append(p)
        else:
            print(f"warning: no such path: {p}", file=sys.stderr)
    return out


def fix_nfc(path: pathlib.Path) -> bool:
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return False
    normalized = unicodedata.normalize("NFC", text)
    if normalized == text:
        return False
    # Path.write_text(newline=...) is 3.10+; Path.open keeps this working on 3.9.
    with path.open("w", encoding="utf-8", newline="") as handle:
        handle.write(normalized)
    return True


def _force_utf8_output() -> None:
    """Windows consoles default to cp1252 and would crash printing Vietnamese."""
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError, OSError):
            pass


def main(argv: Optional[Sequence[str]] = None) -> int:
    _force_utf8_output()
    ap = argparse.ArgumentParser(
        prog="validate_copy.py",
        description="Lint Vietnamese (vi-VN) marketing copy.",
        epilog="Rules: " + ", ".join(f"{k} ({v})" for k, v in RULE_DOCS.items()),
    )
    # nargs="*" so that --list-rules works without naming a file; the requirement is
    # re-imposed by hand below.
    ap.add_argument("paths", nargs="*", help="files or directories to check")
    # Not `choices=`: the register list lives in references/register-matrix.md, which
    # is not loaded until --refs has been parsed. Validated by hand below instead.
    ap.add_argument("--register",
                    help="enable the register-consistency check (PRO002); "
                         "values come from references/register-matrix.md")
    ap.add_argument("--doctype", choices=sorted(DOCTYPES) or None,
                    help="declare the artifact type, enabling the rules that only "
                         "apply to it" + (
                             "; one of: " + ", ".join(sorted(DOCTYPES)) if DOCTYPES
                             else " (this skill defines none)"))
    ap.add_argument("--json", action="store_true", dest="as_json",
                    help="emit findings as JSON")
    ap.add_argument("--strict", action="store_true",
                    help="exit non-zero on warnings as well as errors")
    ap.add_argument("--fix", action="store_true",
                    help="rewrite NFC violations in place, then re-check")
    ap.add_argument("--ext", default=",".join(DEFAULT_EXTENSIONS),
                    help="comma-separated file extensions to scan in directories")
    ap.add_argument("--refs", default=str(REF_DIR),
                    help="directory holding glossary.md, banned-phrases.md and "
                         "register-matrix.md")
    ap.add_argument("--list-rules", action="store_true",
                    help="print every rule this skill can emit, then exit")
    args = ap.parse_args(argv)

    if args.list_rules:
        for rule, doc in sorted(RULE_DOCS.items()):
            print(f"{rule}  {doc}")
        return 0

    if not args.paths:
        ap.print_usage(sys.stderr)
        print("validate_copy.py: error: no paths given", file=sys.stderr)
        return 2

    extensions = tuple(e if e.startswith(".") else "." + e
                       for e in (x.strip() for x in args.ext.split(",")) if e)
    files = collect(args.paths, extensions)
    if not files:
        print("no files to check", file=sys.stderr)
        return 2

    blocklists = Blocklists(pathlib.Path(args.refs))
    for missing in blocklists.missing:
        print(f"warning: reference file not found, some rules disabled: {missing}",
              file=sys.stderr)

    if args.register and args.register not in blocklists.registers:
        print(f"unknown register {args.register!r}; this skill defines: "
              + ", ".join(sorted(blocklists.registers)), file=sys.stderr)
        return 2

    if args.fix:
        for path in files:
            if fix_nfc(path):
                print(f"fixed NFC: {path}", file=sys.stderr)

    validator = Validator(blocklists, args.register, args.doctype)
    findings: List[Finding] = []
    for path in files:
        findings.extend(validator.check_file(path))

    errors = sum(1 for f in findings if f.severity == ERROR)
    warnings = len(findings) - errors

    if args.as_json:
        print(json.dumps({
            "files_checked": len(files),
            "errors": errors,
            "warnings": warnings,
            "findings": [f.as_dict() for f in findings],
        }, ensure_ascii=False, indent=2))
    else:
        for f in findings:
            print(f.render())
        if findings:
            print()
        print(f"{len(files)} file(s) checked · {errors} error(s) · {warnings} warning(s)")
        if not findings:
            print("clean")

    if errors:
        return 1
    if warnings and args.strict:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
