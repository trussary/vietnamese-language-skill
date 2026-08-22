#!/usr/bin/env python3
"""Regenerate each skill's references/examples.md from its eval corpus.

evals/<skill-name>/pairs.jsonl is the single source of truth for that skill's
bad->good corpus: it feeds both the human-readable examples file and the validator's
test fixtures. Edit the JSONL, then run this script. Never edit examples.md by hand.

    python tools/build_examples.py                 # rewrite every skill's examples.md
    python tools/build_examples.py --check         # exit 1 if any is stale (used in CI)
    python tools/build_examples.py --skill NAME    # just one skill
"""
from __future__ import annotations

import argparse
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
EVALS = ROOT / "evals"
SKILLS = ROOT / "skills"

# Categories are shared across skills so that a reader who knows one corpus can read
# another. A category not listed here still renders — it just sorts last, under a title
# derived from its slug — so adding a corpus does not require editing this file first.
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
    "marketing": "Marketing and campaign copy",
    "sales": "Sales and B2B outreach",
    "engineering": "Engineering documentation",
    "product": "Product and research writing",
    "finance": "Finance and regulated financial copy",
    "k12": "K-12 school communications",
    "higher-ed": "Higher education and academic writing",
}
ORDER = ["calque", "passive", "grammar", "word-order", "legal", "formatting",
         "register", "i18n", "encoding", "marketing", "sales", "engineering",
         "product", "finance", "k12", "higher-ed"]


def title_for(category: str) -> str:
    return CATEGORY_TITLES.get(category, category.replace("-", " ").capitalize())


def order_for(pairs: list[dict]) -> list[str]:
    seen = {p["category"] for p in pairs}
    return [c for c in ORDER if c in seen] + sorted(seen - set(ORDER))


def corpora() -> list[tuple[str, pathlib.Path, pathlib.Path]]:
    """(skill name, pairs.jsonl, examples.md) for every skill that has a corpus."""
    out = []
    if not SKILLS.is_dir():
        return out
    for skill in sorted(p for p in SKILLS.iterdir() if p.is_dir()):
        pairs = EVALS / skill.name / "pairs.jsonl"
        if pairs.is_file():
            out.append((skill.name, pairs, skill / "references" / "examples.md"))
    return out


def load_pairs(PAIRS: pathlib.Path) -> list[dict]:
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

    return pairs


def render(pairs: list[dict], source: str) -> str:
    lines = [
        "<!-- vlc-disable: all -->",
        "<!-- GENERATED FILE — do not edit by hand.",
        f"     Source: {source}. Regenerate with: python tools/build_examples.py -->",
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
    for cat in order_for(pairs):
        rows = [p for p in pairs if p["category"] == cat]
        if not rows:
            continue
        lines += [f"## {title_for(cat)}", ""]
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
                    help="exit 1 if any examples.md is out of date instead of rewriting it")
    ap.add_argument("--skill", help="only process this skill")
    args = ap.parse_args()

    found = [c for c in corpora() if args.skill in (None, c[0])]
    if not found:
        print(f"no eval corpus found{f' for {args.skill}' if args.skill else ''}",
              file=sys.stderr)
        return 1

    stale, written = [], []
    for name, pairs_path, examples_path in found:
        source = f"evals/{name}/pairs.jsonl"
        content = render(load_pairs(pairs_path), source)
        current = examples_path.read_text(encoding="utf-8") if examples_path.exists() else ""
        if current == content:
            continue
        if args.check:
            stale.append(examples_path)
            continue
        examples_path.parent.mkdir(parents=True, exist_ok=True)
        # Path.write_text(newline=...) is 3.10+; Path.open keeps this working on 3.9.
        with examples_path.open("w", encoding="utf-8", newline="\n") as handle:
            handle.write(content)
        written.append(examples_path)

    if args.check:
        for path in stale:
            print(f"{path.relative_to(ROOT)} is stale", file=sys.stderr)
        if stale:
            print("run: python tools/build_examples.py", file=sys.stderr)
            return 1
        print(f"{len(found)} examples.md file(s) up to date")
        return 0

    for path in written:
        print(f"wrote {path.relative_to(ROOT)}")
    print(f"{len(written)} written, {len(found) - len(written)} already current")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
