#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Check that every codepoint in your copy falls inside a font's declared unicode-range.

Standard library only, Python 3.9+.

Vietnamese stacks up to two marks on one vowel. Fonts advertised as "Latin Extended"
routinely miss part of the Vietnamese block — Google Fonts historically omitted
Ỳ ỳ Ỵ ỵ Ỷ ỷ Ỹ ỹ entirely (google/fonts#189). The failure mode is silent: the browser
substitutes a fallback face mid-word and the line looks subtly broken.

    python check_font_coverage.py copy.md
    python check_font_coverage.py src/ --range "U+0102-0103,U+1EA0-1EF9,U+20AB"
    python check_font_coverage.py copy.md --from-css app/globals.css
    python check_font_coverage.py --list-required

Exit codes: 0 = every codepoint covered, 1 = uncovered codepoints found, 2 = bad invocation.
"""
from __future__ import annotations

import argparse
import pathlib
import re
import sys
import unicodedata
from typing import Iterable, List, Sequence, Set, Tuple

# The Latin + Vietnamese subsets Google Fonts serves for a Vietnamese-capable face,
# including the combining marks some faces rely on.
DEFAULT_RANGE = (
    "U+0000-00FF, U+0102-0103, U+0110-0111, U+0128-0129, U+0168-0169, "
    "U+01A0-01A1, U+01AF-01B0, U+0300-0301, U+0303-0304, U+0308-0309, "
    "U+0323, U+0329, U+1EA0-1EF9, U+2018-2019, U+201C-201D, U+2013-2014, "
    "U+2026, U+00B2, U+20AB"
)

# Codepoints a Vietnamese face must carry, over and above unaccented ASCII.
REQUIRED_SAMPLE = "ăâđêôơưĂÂĐÊÔƠƯáàảãạấầẩẫậắằẳẵặéèẻẽẹếềểễệíìỉĩị" \
                  "óòỏõọốồổỗộớờởỡợúùủũụứừửữựýỳỷỹỵĐ₫"

# The glyphs most often missing from otherwise-Vietnamese fonts.
KNOWN_GAP = "ỲỳỴỵỶỷỸỹ"

RANGE_TOKEN_RE = re.compile(r"[uU]\+([0-9A-Fa-f]{1,6})(?:-([0-9A-Fa-f]{1,6}))?")
UNICODE_RANGE_DECL_RE = re.compile(r"unicode-range\s*:\s*([^;}]+)", re.IGNORECASE)

DEFAULT_EXTENSIONS = (".md", ".mdx", ".markdown", ".txt", ".json", ".html", ".htm",
                      ".yaml", ".yml", ".ts", ".tsx", ".js", ".jsx", ".vue", ".svelte")


def parse_range(spec: str) -> List[Tuple[int, int]]:
    """Parse a CSS unicode-range value into inclusive (start, end) pairs."""
    ranges: List[Tuple[int, int]] = []
    for match in RANGE_TOKEN_RE.finditer(spec):
        start = int(match.group(1), 16)
        end = int(match.group(2), 16) if match.group(2) else start
        ranges.append((start, end))
    if not ranges:
        raise ValueError(f"no U+ tokens found in range spec: {spec!r}")
    return ranges


def ranges_from_css(path: pathlib.Path) -> List[Tuple[int, int]]:
    """Union every unicode-range declaration in a CSS file."""
    text = path.read_text(encoding="utf-8", errors="replace")
    declarations = UNICODE_RANGE_DECL_RE.findall(text)
    if not declarations:
        raise ValueError(f"no unicode-range declarations in {path}")
    ranges: List[Tuple[int, int]] = []
    for decl in declarations:
        ranges.extend(parse_range(decl))
    return ranges


def covered(codepoint: int, ranges: Sequence[Tuple[int, int]]) -> bool:
    return any(start <= codepoint <= end for start, end in ranges)


def describe(codepoint: int) -> str:
    try:
        name = unicodedata.name(chr(codepoint))
    except ValueError:
        name = "<unnamed>"
    char = chr(codepoint)
    shown = repr(char) if char.isprintable() else "<non-printing>"
    return f"U+{codepoint:04X} {shown:>6}  {name}"


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


def _force_utf8_output() -> None:
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError, OSError):
            pass


def main(argv: Sequence[str] = None) -> int:
    _force_utf8_output()
    ap = argparse.ArgumentParser(prog="check_font_coverage.py", description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("paths", nargs="*", help="files or directories of copy to check")
    ap.add_argument("--range", default=DEFAULT_RANGE,
                    help="CSS unicode-range to test against (default: Google Fonts vietnamese)")
    ap.add_argument("--from-css", metavar="FILE",
                    help="read unicode-range declarations from a CSS file instead")
    ap.add_argument("--list-required", action="store_true",
                    help="print the codepoints a Vietnamese face must carry, then exit")
    ap.add_argument("--ext", default=",".join(DEFAULT_EXTENSIONS),
                    help="comma-separated extensions to scan in directories")
    args = ap.parse_args(argv)

    if args.list_required:
        for ch in sorted(set(REQUIRED_SAMPLE)):
            print(describe(ord(ch)))
        return 0

    if not args.paths:
        ap.error("give at least one file or directory (or use --list-required)")

    try:
        ranges = (ranges_from_css(pathlib.Path(args.from_css)) if args.from_css
                  else parse_range(args.range))
    except (ValueError, OSError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    extensions = tuple(e if e.startswith(".") else "." + e
                       for e in (x.strip() for x in args.ext.split(",")) if e)
    files = collect(args.paths, extensions)
    if not files:
        print("no files to check", file=sys.stderr)
        return 2

    used: Set[int] = set()
    for path in files:
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError) as exc:
            print(f"warning: skipping {path}: {exc}", file=sys.stderr)
            continue
        used.update(ord(ch) for ch in unicodedata.normalize("NFC", text))

    used.discard(0x0A)
    used.discard(0x0D)
    used.discard(0x09)

    uncovered = sorted(cp for cp in used if not covered(cp, ranges))

    print(f"{len(files)} file(s) · {len(used)} distinct codepoints · "
          f"{len(ranges)} range(s) in the font subset")

    gaps_in_font = [ch for ch in KNOWN_GAP if not covered(ord(ch), ranges)]
    if gaps_in_font:
        print(f"\nnote: this subset does not cover {''.join(gaps_in_font)} — the glyphs "
              "Google Fonts historically omitted (google/fonts#189). Verify the actual "
              "font binary, not just the declared range.")

    if not uncovered:
        print("\nclean — every codepoint is inside the declared subset")
        return 0

    print(f"\n{len(uncovered)} uncovered codepoint(s):")
    for cp in uncovered:
        print(f"  {describe(cp)}")
    print("\nThese will render from a fallback face, breaking the line visually.")
    print("Pick a font with a complete Vietnamese subset (Be Vietnam Pro is purpose-built)")
    print("or extend the subset request — see references/locale-formatting.md.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
