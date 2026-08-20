#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Copy shared/ into every skill, so each skill folder stays self-contained.

Four references and the validator engine are identical in every skill. They have one
source of truth in shared/ and are *generated* into skills/<name>/ from there.

    python tools/sync_shared.py           # regenerate every copy
    python tools/sync_shared.py --check   # exit 1 if any copy has drifted (CI)

Why generated copies rather than the obvious alternatives:

  * A symlink breaks `npx skills use`, the Claude.ai zip upload, and
    tests/test_skill_spec.py::test_relative_links_resolve, all of which need a real
    file inside the skill folder.
  * A cross-skill path (`../vietnamese-landing-copy/references/...`) does not resolve
    either: the Agent Skill spec keeps references one level deep inside one folder.
  * Hand-duplication drifts inside a single release. This is the failure this script
    exists to make impossible.

The cost is one discipline: **edit shared/, never the generated copy.** Every generated
file says so in its first line, and --check names the canonical path when it fails.

Standard library only, Python 3.9+, matching the repo's no-install policy.
"""
from __future__ import annotations

import argparse
import hashlib
import pathlib
import sys
from typing import List, Tuple

ROOT = pathlib.Path(__file__).resolve().parents[1]
SHARED = ROOT / "shared"
SKILLS = ROOT / "skills"

BANNER_MD = (
    "<!-- GENERATED FILE — do not edit. Source: {source} (sha256 {digest}). "
    "Edit the source and run `python tools/sync_shared.py`. -->\n"
)
BANNER_PY = (
    "# GENERATED FILE — do not edit. Source: {source} (sha256 {digest}).\n"
    "# Edit the source and run `python tools/sync_shared.py`.\n"
)


def digest_of(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:16]


def banner_for(relative: pathlib.Path, source_text: str) -> str:
    template = BANNER_PY if relative.suffix == ".py" else BANNER_MD
    return template.format(source=f"shared/{relative.as_posix()}",
                           digest=digest_of(source_text))


def render(relative: pathlib.Path, source_text: str) -> str:
    """The exact bytes the generated copy should contain."""
    banner = banner_for(relative, source_text)
    if relative.suffix != ".py":
        return banner + source_text
    # Keep the shebang and coding declaration on lines 1-2 where they are meaningful.
    lines = source_text.splitlines(keepends=True)
    head: List[str] = []
    while lines and (lines[0].startswith("#!") or "coding" in lines[0][:30]):
        head.append(lines.pop(0))
    return "".join(head) + banner + "".join(lines)


def strip_banner(text: str, relative: pathlib.Path) -> str:
    """Inverse of render(), so a drifted copy can be diffed against its source."""
    marker = "# GENERATED FILE" if relative.suffix == ".py" else "<!-- GENERATED FILE"
    lines = text.splitlines(keepends=True)
    out, skipped = [], 0
    for line in lines:
        if skipped < 2 and line.startswith(marker):
            skipped = 1
            continue
        if skipped == 1 and line.startswith("# Edit the source"):
            skipped = 2
            continue
        out.append(line)
    return "".join(out)


def shared_files() -> List[pathlib.Path]:
    if not SHARED.is_dir():
        return []
    return sorted(p.relative_to(SHARED) for p in SHARED.rglob("*") if p.is_file())


def skill_dirs() -> List[pathlib.Path]:
    if not SKILLS.is_dir():
        return []
    return sorted(p for p in SKILLS.iterdir() if p.is_dir() and (p / "SKILL.md").is_file())


def targets() -> List[Tuple[pathlib.Path, pathlib.Path, str]]:
    """(relative shared path, destination, rendered content) for every copy."""
    out = []
    for relative in shared_files():
        source_text = (SHARED / relative).read_text(encoding="utf-8")
        content = render(relative, source_text)
        for skill in skill_dirs():
            out.append((relative, skill / relative, content))
    return out


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="sync_shared.py", description=__doc__.splitlines()[0])
    ap.add_argument("--check", action="store_true",
                    help="do not write; exit 1 if any generated copy is stale")
    args = ap.parse_args(argv)

    if not SHARED.is_dir():
        print(f"no shared/ directory at {SHARED}", file=sys.stderr)
        return 2

    stale, written = [], []
    for relative, destination, content in targets():
        current = destination.read_text(encoding="utf-8") if destination.is_file() else None
        if current == content:
            continue
        if args.check:
            reason = "missing" if current is None else "differs from"
            stale.append((relative, destination, reason))
            continue
        destination.parent.mkdir(parents=True, exist_ok=True)
        with destination.open("w", encoding="utf-8", newline="") as handle:
            handle.write(content)
        written.append(destination)

    if args.check:
        if stale:
            print("generated copies are out of date:\n", file=sys.stderr)
            for relative, destination, reason in stale:
                print(f"  {destination.relative_to(ROOT)}", file=sys.stderr)
                print(f"      {reason} shared/{relative.as_posix()}", file=sys.stderr)
            print("\nEdit the file under shared/, then run:\n"
                  "    python tools/sync_shared.py\n", file=sys.stderr)
            return 1
        print(f"{len(targets())} generated file(s) in sync")
        return 0

    for destination in written:
        print(f"wrote {destination.relative_to(ROOT)}")
    print(f"{len(written)} written, {len(targets()) - len(written)} already current")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
