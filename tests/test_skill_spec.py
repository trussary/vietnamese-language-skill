# -*- coding: utf-8 -*-
"""Agent Skill spec compliance, checked without a YAML dependency.

Mirrors the requirements at agentskills.io/specification: `name` and `description` are
required, `name` must match the folder, the body must stay inside the progressive-disclosure
budget, and every relative link must resolve. A broken link in SKILL.md is a silent failure —
Claude follows the reference and finds nothing.
"""
from __future__ import annotations

import pathlib
import re

import pytest

ROOT = pathlib.Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
SKILL_DIRS = sorted(p for p in SKILLS_DIR.iterdir() if p.is_dir())

NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")

MAX_NAME = 64
MAX_DESCRIPTION = 1024
MAX_BODY_LINES = 500


def parse_frontmatter(text: str) -> tuple[dict, str]:
    """Parse the flat subset of YAML a SKILL.md frontmatter is allowed to use."""
    if not text.startswith("---\n"):
        raise AssertionError("SKILL.md must open with a YAML frontmatter fence")
    end = text.find("\n---\n", 4)
    assert end != -1, "unterminated YAML frontmatter"
    block, body = text[4:end], text[end + 5:]

    data: dict = {}
    key = None
    for line in block.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if re.match(r"^\s+", line) and key:          # continuation or nested mapping
            data[key] = (str(data[key]) + " " + line.strip()).strip()
            continue
        match = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        assert match, f"unparseable frontmatter line: {line!r}"
        key, value = match.group(1), match.group(2).strip()
        data[key] = value
    return data, body


@pytest.fixture(scope="module", params=SKILL_DIRS, ids=lambda p: p.name)
def skill(request):
    path = request.param
    md = path / "SKILL.md"
    assert md.is_file(), f"{path.name} has no SKILL.md"
    front, body = parse_frontmatter(md.read_text(encoding="utf-8"))
    return {"dir": path, "file": md, "front": front, "body": body}


def test_repo_has_at_least_one_skill():
    assert SKILL_DIRS, "no skills found under skills/"


def test_required_frontmatter_fields(skill):
    for field in ("name", "description"):
        assert field in skill["front"], f"missing required frontmatter field: {field}"
        assert skill["front"][field], f"empty required frontmatter field: {field}"


def test_name_matches_folder_and_charset(skill):
    name = skill["front"]["name"]
    assert name == skill["dir"].name, "frontmatter name must match the folder name"
    assert len(name) <= MAX_NAME, f"name exceeds {MAX_NAME} characters"
    assert NAME_RE.match(name), (
        "name must be lowercase a-z 0-9 and single hyphens, no leading or trailing hyphen")


def test_description_length_and_content(skill):
    description = skill["front"]["description"]
    assert len(description) <= MAX_DESCRIPTION, (
        f"description is {len(description)} chars, over the {MAX_DESCRIPTION} limit")
    assert len(description) >= 80, "description is too thin to trigger reliably"
    lowered = description.lower()
    assert "use" in lowered or "trigger" in lowered, (
        "description must say WHEN to use the skill, not only what it does")


def test_no_angle_brackets_in_frontmatter(skill):
    """Angle brackets in frontmatter are an injection risk and are disallowed."""
    for key, value in skill["front"].items():
        assert "<" not in str(value) and ">" not in str(value), (
            f"angle bracket in frontmatter field {key!r}")


def test_body_within_progressive_disclosure_budget(skill):
    lines = skill["body"].splitlines()
    assert len(lines) <= MAX_BODY_LINES, (
        f"SKILL.md body is {len(lines)} lines, over the {MAX_BODY_LINES} budget — "
        "move detail into references/")


def test_optional_dirs_only(skill):
    allowed = {"references", "scripts", "assets"}
    subdirs = {p.name for p in skill["dir"].iterdir()
               if p.is_dir() and not p.name.startswith((".", "__"))}
    assert subdirs <= allowed, f"unexpected directories in the skill: {sorted(subdirs - allowed)}"


def test_references_are_one_level_deep(skill):
    refs = skill["dir"] / "references"
    if not refs.is_dir():
        pytest.skip("no references/")
    nested = [p for p in refs.rglob("*")
              if p.is_dir() and not p.name.startswith((".", "__"))]
    assert not nested, f"references/ must stay flat, found {[p.name for p in nested]}"


@pytest.mark.parametrize("scope", ["skill_md", "references"])
def test_relative_links_resolve(skill, scope):
    files = ([skill["file"]] if scope == "skill_md"
             else sorted((skill["dir"] / "references").glob("*.md")))
    if not files:
        pytest.skip("nothing to check")

    broken = []
    for path in files:
        for target in LINK_RE.findall(path.read_text(encoding="utf-8")):
            target = target.split("#", 1)[0].strip()
            if not target or target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            if not (path.parent / target).resolve().exists():
                broken.append(f"{path.relative_to(ROOT)} -> {target}")
    assert not broken, "broken relative links:\n  " + "\n  ".join(broken)


def test_scripts_are_stdlib_only(skill):
    """A skill script that needs pip install does not get run."""
    scripts = skill["dir"] / "scripts"
    if not scripts.is_dir():
        pytest.skip("no scripts/")
    third_party = re.compile(r"^\s*(?:import|from)\s+(?!__future__)([a-zA-Z0-9_]+)", re.M)
    stdlib = set(getattr(__import__("sys"), "stdlib_module_names", ()))
    for path in scripts.glob("*.py"):
        for module in set(third_party.findall(path.read_text(encoding="utf-8"))):
            assert module in stdlib, (
                f"{path.name} imports non-stdlib module {module!r}; keep scripts dependency-free")
