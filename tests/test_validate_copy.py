# -*- coding: utf-8 -*-
"""The eval corpus IS the fixture set.

evals/pairs.jsonl drives two assertions per pair:
  * every rule listed in `expected_rules` fires on the ❌ string;
  * NO rule fires on the ✅ string.

The second assertion is the important one. A linter that flags correct Vietnamese is
worse than no linter, because contributors will disable it.
"""
from __future__ import annotations

import importlib.util
import json
import pathlib
import sys

import pytest

ROOT = pathlib.Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "vietnamese-landing-copy"
REFS = SKILL / "references"
PAIRS = ROOT / "evals" / "pairs.jsonl"


def _load_module():
    spec = importlib.util.spec_from_file_location(
        "validate_copy", SKILL / "scripts" / "validate_copy.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules["validate_copy"] = module
    spec.loader.exec_module(module)
    return module


V = _load_module()
BLOCKLISTS = V.Blocklists(REFS)


def load_pairs():
    with PAIRS.open(encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


PAIRS_DATA = load_pairs()


def run(tmp_path, text, filename="sample.md", register=None):
    path = tmp_path / filename
    with path.open("w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    validator = V.Validator(BLOCKLISTS, register)
    return validator.check_file(path)


def rules_of(findings):
    return sorted({f.rule for f in findings})


# --------------------------------------------------------------------------- #
# Reference files must actually parse
# --------------------------------------------------------------------------- #
def test_blocklists_loaded():
    assert not BLOCKLISTS.missing, f"reference files missing: {BLOCKLISTS.missing}"
    assert len(BLOCKLISTS.calques) >= 30, "glossary/banned-phrases tables failed to parse"
    assert len(BLOCKLISTS.superlatives) >= 10, "superlative table failed to parse"


def test_no_calque_is_contained_in_a_suggestion():
    """A blocklisted phrase must not appear inside any phrase we recommend.

    `Thử miễn phí` as a blocklist entry fires on the recommended `Dùng thử miễn phí`.
    A rule that flags its own suggested fix is worse than no rule at all.
    """
    suggestions = set()
    for _, good, _ in BLOCKLISTS.calques:
        suggestions.update(part.strip().lower() for part in good.split("/") if part.strip())
    for bad, _, source in BLOCKLISTS.calques:
        for suggestion in suggestions:
            assert bad.lower() not in suggestion, (
                f"{bad!r} ({source}) is a substring of the recommended {suggestion!r}")


def test_every_rule_id_is_documented():
    documented = set(V.RULE_DOCS)
    used = {r for pair in PAIRS_DATA for r in pair["expected_rules"]}
    assert used <= documented, f"undocumented rule ids in corpus: {sorted(used - documented)}"


# --------------------------------------------------------------------------- #
# The corpus
# --------------------------------------------------------------------------- #
@pytest.mark.parametrize("pair", PAIRS_DATA, ids=[p["id"] for p in PAIRS_DATA])
def test_bad_string_fires_expected_rules(tmp_path, pair):
    if not pair["expected_rules"]:
        pytest.skip("not machine-detectable by design")
    findings = run(tmp_path, pair["bad"],
                   filename=pair.get("filename", "sample.md"),
                   register=pair.get("register"))
    fired = set(rules_of(findings))
    missing = set(pair["expected_rules"]) - fired
    assert not missing, (
        f"{pair['id']}: expected {sorted(missing)} to fire on {pair['bad']!r}, "
        f"got {sorted(fired)}")


@pytest.mark.parametrize("pair", PAIRS_DATA, ids=[p["id"] for p in PAIRS_DATA])
def test_good_string_is_clean(tmp_path, pair):
    findings = run(tmp_path, pair["good"],
                   filename=pair.get("filename", "sample.md"),
                   register=pair.get("register"))
    assert not findings, (
        f"{pair['id']}: false positives on correct copy {pair['good']!r} — "
        + "; ".join(f"{f.rule} {f.message}" for f in findings))


# --------------------------------------------------------------------------- #
# Rule behaviour that the corpus does not cover
# --------------------------------------------------------------------------- #
def test_proof_annotation_suppresses_law001(tmp_path):
    bare = run(tmp_path, "Thương hiệu số 1 Việt Nam")
    assert "LAW001" in rules_of(bare)

    annotated = run(
        tmp_path, "Thương hiệu số 1 Việt Nam <!-- proof: Khảo sát Nielsen VN 2026 -->")
    assert "LAW001" not in rules_of(annotated)

    preceding = run(
        tmp_path, "<!-- proof: Khảo sát Nielsen VN 2026 -->\nThương hiệu số 1 Việt Nam")
    assert "LAW001" not in rules_of(preceding)


def test_law001_is_never_an_error(tmp_path):
    findings = run(tmp_path, "Căn hộ tốt nhất thị trường, chủ đầu tư hàng đầu")
    law = [f for f in findings if f.rule == "LAW001"]
    assert law, "expected the superlative to be flagged"
    assert all(f.severity == V.WARN for f in law), "LAW001 must warn, never error"


def test_file_level_disable(tmp_path):
    text = "<!-- vlc-disable: CAL001 -->\nHọc thêm về dự án"
    assert "CAL001" not in rules_of(run(tmp_path, text))


def test_disable_all(tmp_path):
    text = "<!-- vlc-disable: all -->\nHọc thêm về dự án tốt nhất, giá 2,500,000 VND"
    assert run(tmp_path, text) == []


def test_line_level_disable(tmp_path):
    text = "Học thêm về dự án <!-- vlc-disable-line CAL001 -->\nHọc thêm về dự án"
    findings = [f for f in run(tmp_path, text) if f.rule == "CAL001"]
    assert len(findings) == 1 and findings[0].line == 2


def test_overlapping_calques_report_once(tmp_path):
    """`ký lên` sits inside `đăng ký lên`; only the longest match should be reported."""
    findings = [f for f in run(tmp_path, "Vui lòng đăng ký lên để nhận thông tin")
                if f.rule == "CAL001"]
    assert len(findings) == 1, [f.text for f in findings]
    assert findings[0].text.lower() == "đăng ký lên"


def test_directives_work_in_json(tmp_path):
    """JSON has no comment syntax, so the directive must survive inside a string value."""
    noisy = '{"a": "Giá: 2,500,000 VND"}'
    assert "NUM001" in rules_of(run(tmp_path, noisy, filename="vi.json"))

    quiet = '{"_lint": "vlc-disable: NUM001", "a": "Giá: 2,500,000 VND"}'
    assert "NUM001" not in rules_of(run(tmp_path, quiet, filename="vi.json"))


def test_disable_directive_does_not_swallow_the_rest_of_the_line(tmp_path):
    """The directive must stop at its own delimiter, not disable everything after it."""
    text = '{"_lint": "vlc-disable: NUM001", "b": "Học thêm về dự án"}'
    assert "CAL001" in rules_of(run(tmp_path, text, filename="vi.json"))


def test_code_spans_are_not_linted(tmp_path):
    assert "CAL001" not in rules_of(run(tmp_path, "The calque `Học thêm` is wrong."))


def test_fenced_blocks_are_not_linted(tmp_path):
    text = "Intro\n\n```text\nHọc thêm về dự án\n```\n\nOutro"
    assert "CAL001" not in rules_of(run(tmp_path, text))


def test_tone_consistency_only_flags_mixing(tmp_path):
    assert "TONE001" not in rules_of(run(tmp_path, "hoà bình, thuỷ tinh, khoẻ mạnh"))
    assert "TONE001" not in rules_of(run(tmp_path, "hòa bình, thủy tinh, khỏe mạnh"))
    assert "TONE001" in rules_of(run(tmp_path, "hoà bình nhưng thủy tinh"))


def test_quy_does_not_trigger_tone_rule(tmp_path):
    """`quý` is spelled the same in both conventions — the qu- initial is not a diphthong."""
    assert "TONE001" not in rules_of(run(tmp_path, "quý khách và hòa bình"))


def test_nfc_fix_round_trip(tmp_path):
    import unicodedata
    path = tmp_path / "copy.md"
    path.write_text(unicodedata.normalize("NFD", "Đăng ký nhận thông tin"), encoding="utf-8")
    assert V.fix_nfc(path) is True
    assert V.fix_nfc(path) is False
    assert V.Validator(BLOCKLISTS).check_file(path) == []


def test_register_check_requires_the_flag(tmp_path):
    text = "Quý khách vui lòng đăng ký"
    assert "PRO002" not in rules_of(run(tmp_path, text))
    assert "PRO002" in rules_of(run(tmp_path, text, register="saas"))


def test_exit_codes(tmp_path, capsys):
    clean = tmp_path / "clean.md"
    clean.write_text("Tìm hiểu thêm về dự án", encoding="utf-8")
    assert V.main([str(clean), "--refs", str(REFS)]) == 0

    warned = tmp_path / "warn.md"
    warned.write_text("Chủ đầu tư hàng đầu Việt Nam", encoding="utf-8")
    assert V.main([str(warned), "--refs", str(REFS)]) == 0
    assert V.main([str(warned), "--refs", str(REFS), "--strict"]) == 1

    broken = tmp_path / "err.md"
    broken.write_text("Học thêm về dự án", encoding="utf-8")
    assert V.main([str(broken), "--refs", str(REFS)]) == 1


def test_json_output_is_parseable(tmp_path, capsys):
    path = tmp_path / "copy.md"
    path.write_text("Giá: 2,500,000 VND", encoding="utf-8")
    V.main([str(path), "--refs", str(REFS), "--json"])
    payload = json.loads(capsys.readouterr().out)
    assert payload["errors"] >= 1
    assert payload["findings"][0]["rule"] == "NUM001"


# --------------------------------------------------------------------------- #
# The skill's own documentation must pass its own linter
# --------------------------------------------------------------------------- #
@pytest.mark.parametrize(
    "path",
    sorted(p for p in SKILL.rglob("*.md")) + sorted(SKILL.glob("assets/*")),
    ids=lambda p: str(p.relative_to(SKILL)),
)
def test_skill_docs_are_clean(path):
    findings = V.Validator(BLOCKLISTS).check_file(path)
    errors = [f for f in findings if f.severity == V.ERROR]
    assert not errors, "\n".join(f.render() for f in errors)
