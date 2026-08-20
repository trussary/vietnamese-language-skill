# -*- coding: utf-8 -*-
"""Skills must not compete for the same trigger.

`description` is the only signal Claude uses to decide which skill to load. Two skills
claiming the same keyword is the specific failure that makes a multi-skill split worse
than one big skill: the wrong one loads, or both do, and neither result is what the
user asked for.

The table below is the ownership contract. A keyword belongs to exactly one skill, and
must not appear in any other skill's description. Add a row when a skill claims new
territory; if two skills genuinely need a word, the split is wrong, not the table.
"""
from __future__ import annotations

import pathlib
import re

import pytest

ROOT = pathlib.Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"

# keyword -> the one skill allowed to name it
KEYWORD_OWNERS = {
    # vietnamese-landing-copy
    "landing page": "vietnamese-landing-copy",
    "bất động sản": "vietnamese-landing-copy",
    "căn hộ": "vietnamese-landing-copy",
    "dự án": "vietnamese-landing-copy",
    "tiện ích": "vietnamese-landing-copy",

    # vietnamese-tech-writing
    "commit": "vietnamese-tech-writing",
    "postmortem": "vietnamese-tech-writing",
    "runbook": "vietnamese-tech-writing",
    "rfc": "vietnamese-tech-writing",
    "prd": "vietnamese-tech-writing",
    "release notes": "vietnamese-tech-writing",
    "changelog": "vietnamese-tech-writing",
    "api docs": "vietnamese-tech-writing",
    "survey": "vietnamese-tech-writing",

    # vietnamese-business-comms
    "zalo": "vietnamese-business-comms",
    "zns": "vietnamese-business-comms",
    "shopee": "vietnamese-business-comms",
    "báo giá": "vietnamese-business-comms",
    "khuyến mại": "vietnamese-business-comms",
    "cold outreach": "vietnamese-business-comms",
    "press release": "vietnamese-business-comms",

    # vietnamese-finance-copy
    "hóa đơn": "vietnamese-finance-copy",
    "báo cáo tài chính": "vietnamese-finance-copy",
    "thuế": "vietnamese-finance-copy",
    "lãi suất": "vietnamese-finance-copy",
    "invoice": "vietnamese-finance-copy",
}


def frontmatter_description(path: pathlib.Path) -> str:
    text = path.read_text(encoding="utf-8")
    end = text.find("\n---\n", 4)
    block = text[4:end] if end != -1 else text
    match = re.search(r"^description:\s*(.*(?:\n[ \t]+.*)*)", block, re.MULTILINE)
    assert match, f"{path} has no description"
    return " ".join(match.group(1).split()).lower()


DESCRIPTIONS = {
    p.name: frontmatter_description(p / "SKILL.md")
    for p in sorted(SKILLS.iterdir())
    if p.is_dir() and (p / "SKILL.md").is_file()
}


@pytest.mark.parametrize("keyword", sorted(KEYWORD_OWNERS), ids=lambda k: k)
def test_keyword_is_claimed_by_one_skill(keyword):
    owner = KEYWORD_OWNERS[keyword]
    if owner not in DESCRIPTIONS:
        pytest.skip(f"{owner} does not exist yet")
    intruders = [name for name, text in DESCRIPTIONS.items()
                 if name != owner and keyword in text]
    assert not intruders, (
        f"“{keyword}” belongs to {owner} but also appears in: {intruders}. "
        "Two skills competing for one trigger means the wrong one loads.")


@pytest.mark.parametrize("keyword", sorted(KEYWORD_OWNERS), ids=lambda k: k)
def test_owner_actually_claims_its_keyword(keyword):
    owner = KEYWORD_OWNERS[keyword]
    if owner not in DESCRIPTIONS:
        pytest.skip(f"{owner} does not exist yet")
    assert keyword in DESCRIPTIONS[owner], (
        f"{owner} is listed as owning “{keyword}” but its description never says it, "
        "so it will under-trigger. Add the keyword or drop the row.")


def test_descriptions_are_distinct():
    seen = {}
    for name, text in DESCRIPTIONS.items():
        assert text not in seen, f"{name} and {seen[text]} have identical descriptions"
        seen[text] = name
