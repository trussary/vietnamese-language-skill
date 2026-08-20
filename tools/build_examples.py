#!/usr/bin/env python3
"""Regenerate references/examples.md from evals/pairs.jsonl.

evals/pairs.jsonl is the single source of truth for the bad->good corpus: it feeds
both the human-readable examples file and the validator's test fixtures. Edit the
JSONL, then run this script. Never edit examples.md by hand.

    python tools/build_examples.py          # rewrite examples.md
    python tools/build_examples.py --check  # exit 1 if examples.md is stale (used in CI)
"""
from __future__ import annotations

import argparse
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
PAIRS = ROOT / "evals" / "pairs.jsonl"
EXAMPLES = ROOT / "skills" / "vietnamese-landing-copy" / "references" / "examples.md"

CATEGORY_TITLES = {
    "calque": "Calqued CTAs and UI strings",
    "passive": "Passive-agent constructions",
    "grammar": "Grammar and pronouns",
    "word-order": "Word order",
    "legal": "Regulated advertising claims and legal copy",
    "formatting": "Locale formatting",
    "register": "Register",
    "i18n": "Structured localization files",
    "encoding": "Unicode encoding",
}
ORDER = ["calque", "passive", "grammar", "word-order", "legal", "formatting",
         "register", "i18n", "encoding"]


def load_pairs() -> list[dict]:
    pairs = []
    with PAIRS.open(encoding="utf-8") as f:
        for lineno, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            try:
                pairs.append(json.loads(line))
            except json.JSONDecodeError as exc:
                raise SystemExit(f"{PAIRS}:{lineno}: invalid JSON — {exc}") from exc

    ids = [p["id"] for p in pairs]
    dupes = {i for i in ids if ids.count(i) > 1}
    if dupes:
        raise SystemExit(f"duplicate pair ids: {sorted(dupes)}")

    unknown = {p["category"] for p in pairs} - set(CATEGORY_TITLES)
    if unknown:
        raise SystemExit(
            f"unknown categories {sorted(unknown)} — add them to CATEGORY_TITLES and ORDER"
        )
    return pairs


def render(pairs: list[dict]) -> str:
    lines = [
        "<!-- vlc-disable: all -->",
        "<!-- GENERATED FILE — do not edit by hand.",
        "     Source: evals/pairs.jsonl. Regenerate with: python tools/build_examples.py -->",
        "",
        "# Examples — bad to good",
        "",
        "The highest-value file in this skill. Each pair names the failure mode it fixes; the",
        "diagnosis generalizes further than the string does. Read this before writing anything",
        "long in Vietnamese.",
        "",
        "Every ❌ string here is a deliberate defect, so this file is exempt from its own linter.",
        "",
        f"**{len(pairs)} pairs.** Contributions welcome — see "
        "[CONTRIBUTING.md](../../../CONTRIBUTING.md).",
        "",
    ]
    for cat in ORDER:
        rows = [p for p in pairs if p["category"] == cat]
        if not rows:
            continue
        lines += [f"## {CATEGORY_TITLES[cat]}", ""]
        for r in rows:
            lines += [f"### {r['en']}", ""]
            for mark, key in (("❌", "bad"), ("✅", "good")):
                value = r[key]
                if "\n" in value:
                    lang = "json" if r.get("filename", "").endswith(".json") else "text"
                    lines += [mark, "", f"```{lang}", value, "```", ""]
                else:
                    lines += [f"{mark} **{value}**", ""]
            rules = ", ".join(f"`{x}`" for x in r["expected_rules"]) or "_not machine-detectable_"
            lines += [r["diagnosis"], "", f"<sub>id: `{r['id']}` · caught by: {rules}</sub>", ""]
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--check", action="store_true",
                    help="exit 1 if examples.md is out of date instead of rewriting it")
    args = ap.parse_args()

    content = render(load_pairs())

    if args.check:
        current = EXAMPLES.read_text(encoding="utf-8") if EXAMPLES.exists() else ""
        if current != content:
            print("examples.md is stale — run: python tools/build_examples.py", file=sys.stderr)
            return 1
        print("examples.md is up to date")
        return 0

    EXAMPLES.write_text(content, encoding="utf-8", newline="\n")
    print(f"wrote {EXAMPLES.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
