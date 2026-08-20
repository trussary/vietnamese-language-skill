# -*- coding: utf-8 -*-
"""Generated copies of shared/ must match their source.

Each skill folder is self-contained — it has to be, because `npx skills use`, the
Claude.ai zip upload, and the plain `cp -r` install path each take exactly one folder.
That means the four shared references and the validator engine physically exist inside
every skill, and physical copies drift.

tools/sync_shared.py regenerates them; this is the local mirror of the CI check that
fails when someone edits a copy instead of the source.
"""
from __future__ import annotations

import importlib.util
import pathlib
import sys

import pytest

ROOT = pathlib.Path(__file__).resolve().parents[1]
SHARED = ROOT / "shared"
SKILLS = ROOT / "skills"


def _load_sync():
    path = ROOT / "tools" / "sync_shared.py"
    spec = importlib.util.spec_from_file_location("sync_shared", path)
    module = importlib.util.module_from_spec(spec)
    sys.modules["sync_shared"] = module
    spec.loader.exec_module(module)
    return module


SYNC = _load_sync()
TARGETS = SYNC.targets()


def test_shared_directory_exists():
    assert SHARED.is_dir(), "shared/ is the source of truth and must exist"
    assert SYNC.shared_files(), "shared/ has no files to sync"


def test_every_skill_is_a_sync_target():
    skills = {p.name for p in SKILLS.iterdir() if p.is_dir() and (p / "SKILL.md").is_file()}
    covered = {d.relative_to(SKILLS).parts[0] for _, d, _ in TARGETS}
    assert skills == covered, f"skills not receiving shared files: {sorted(skills - covered)}"


@pytest.mark.parametrize(
    "item", TARGETS,
    ids=[str(d.relative_to(ROOT)) for _, d, _ in TARGETS])
def test_generated_copy_matches_source(item):
    relative, destination, expected = item
    assert destination.is_file(), (
        f"{destination.relative_to(ROOT)} is missing — run: python tools/sync_shared.py")
    actual = destination.read_text(encoding="utf-8")
    assert actual == expected, (
        f"{destination.relative_to(ROOT)} has drifted from shared/{relative.as_posix()}.\n"
        "Edit the file under shared/, then run: python tools/sync_shared.py")


@pytest.mark.parametrize(
    "item", TARGETS,
    ids=[str(d.relative_to(ROOT)) for _, d, _ in TARGETS])
def test_generated_copy_says_it_is_generated(item):
    _, destination, _ = item
    head = destination.read_text(encoding="utf-8")[:400]
    assert "GENERATED FILE" in head, (
        f"{destination.relative_to(ROOT)} must warn readers not to edit it")


def test_check_mode_passes_on_a_clean_tree():
    assert SYNC.main(["--check"]) == 0, (
        "generated files are stale — run: python tools/sync_shared.py")
