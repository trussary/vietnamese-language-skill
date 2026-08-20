# -*- coding: utf-8 -*-
"""The eval corpus IS the fixture set, for every skill in the repo.

Each skill owns a validator (`skills/<name>/scripts/validate_copy.py`) and a corpus
(`evals/<name>/pairs.jsonl`). Every pair drives two assertions:

  * every rule listed in `expected_rules` fires on the ❌ string;
  * NO rule fires on the ✅ string.

The second assertion is the important one. A linter that flags correct Vietnamese is
worse than no linter, because contributors will disable it.

The engine is byte-identical across skills (see tools/sync_shared.py), but the rule
data is not — so engine behaviour is re-checked against each skill's own references
rather than assumed from one. Checks that need a particular reference file present
skip rather than fail when a skill does not ship it.
"""
from __future__ import annotations

import importlib.util
import json
import pathlib
import sys

import pytest

ROOT = pathlib.Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
EVALS = ROOT / "evals"


def discover():
    """(name, skill dir, pairs path or None) for every skill with a validator."""
    out = []
    if not SKILLS.is_dir():
        return out
    for skill in sorted(p for p in SKILLS.iterdir() if p.is_dir()):
        if not (skill / "scripts" / "validate_copy.py").is_file():
            continue
        pairs = EVALS / skill.name / "pairs.jsonl"
        out.append((skill.name, skill, pairs if pairs.is_file() else None))
    return out


SKILL_SPECS = discover()
assert SKILL_SPECS, "no skill ships a validate_copy.py"


def _load_module(name: str, path: pathlib.Path):
    """Each skill gets its own module object: they load different domain rules."""
    unique = f"validate_copy__{name.replace('-', '_')}"
    spec = importlib.util.spec_from_file_location(unique, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[unique] = module
    spec.loader.exec_module(module)
    return module


class Harness:
    """One skill's validator, its blocklists, and its corpus."""

    def __init__(self, name, skill_dir, pairs_path):
        self.name = name
        self.dir = skill_dir
        self.refs = skill_dir / "references"
        self.V = _load_module(name, skill_dir / "scripts" / "validate_copy.py")
        self.blocklists = self.V.Blocklists(self.refs)
        self.pairs = self.load_pairs(pairs_path)

    @staticmethod
    def load_pairs(path):
        if path is None:
            return []
        with path.open(encoding="utf-8") as handle:
            return [json.loads(line) for line in handle if line.strip()]

    def run(self, tmp_path, text, filename="sample.md", register=None, doctype=None):
        path = tmp_path / filename
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w", encoding="utf-8", newline="") as handle:
            handle.write(text)
        return self.V.Validator(self.blocklists, register, doctype).check_file(path)

    def run_pair(self, tmp_path, pair, key):
        return self.run(tmp_path, pair[key],
                        filename=pair.get("filename", "sample.md"),
                        register=pair.get("register"),
                        doctype=pair.get("doctype"))


HARNESSES = {name: Harness(name, d, p) for name, d, p in SKILL_SPECS}
ALL_PAIRS = [(name, pair) for name, h in HARNESSES.items() for pair in h.pairs]


@pytest.fixture(params=sorted(HARNESSES), ids=lambda n: n)
def skill(request):
    return HARNESSES[request.param]


def rules_of(findings):
    return sorted({f.rule for f in findings})


def pair_id(item):
    return f"{item[0]}::{item[1]['id']}"


# --------------------------------------------------------------------------- #
# Reference files must actually parse
# --------------------------------------------------------------------------- #
def test_blocklists_loaded(skill):
    assert not skill.blocklists.missing, (
        f"{skill.name}: reference files not found: {skill.blocklists.missing}")
    assert skill.blocklists.calques, f"{skill.name}: no calques parsed"
    assert skill.blocklists.registers, f"{skill.name}: no registers parsed"


def test_registers_come_from_the_matrix(skill):
    """The matrix, not the Python fallback, is the source of truth."""
    assert set(skill.blocklists.registers) > set(skill.V.DEFAULT_REGISTERS), (
        f"{skill.name}: register-matrix.md did not load — falling back to the "
        "hardcoded defaults")
    for name, profile in skill.blocklists.registers.items():
        assert isinstance(profile["forbids"], tuple), name
        assert "expects" in profile, name


def test_no_calque_is_contained_in_a_suggestion(skill):
    """A blocklisted phrase must not appear inside any phrase we recommend.

    `Thử miễn phí` as a blocklist entry fires on the recommended `Dùng thử miễn phí`.
    A rule that flags its own suggested fix is worse than no rule at all.
    """
    suggestions = set()
    for _, good, _, _ in skill.blocklists.calques:
        for alternative in good.split("/"):
            alternative = alternative.strip()
            if alternative:
                suggestions.add(alternative.lower())

    offenders = []
    for regex, phrase, _, _, _ in skill.blocklists.compiled_calques():
        for suggestion in suggestions:
            if regex.search(suggestion):
                offenders.append((phrase, suggestion))
    assert not offenders, f"{skill.name}: blocklist entries fire on our own advice: {offenders}"


def test_every_rule_id_is_documented(skill):
    documented = set(skill.V.RULE_DOCS)
    used = {r for pair in skill.pairs for r in pair["expected_rules"]}
    assert used <= documented, (
        f"{skill.name}: undocumented rule ids in corpus: {sorted(used - documented)}")


def test_every_doctype_in_the_corpus_is_declared(skill):
    declared = set(skill.V.DOCTYPES)
    used = {p["doctype"] for p in skill.pairs if p.get("doctype")}
    assert used <= declared, (
        f"{skill.name}: corpus uses undeclared doctypes {sorted(used - declared)}; "
        f"declared: {sorted(declared)}")


def test_every_register_in_the_corpus_exists(skill):
    used = {p["register"] for p in skill.pairs if p.get("register")}
    known = set(skill.blocklists.registers)
    assert used <= known, (
        f"{skill.name}: corpus uses unknown registers {sorted(used - known)}")


# --------------------------------------------------------------------------- #
# The corpus
# --------------------------------------------------------------------------- #
@pytest.mark.parametrize("item", ALL_PAIRS, ids=[pair_id(i) for i in ALL_PAIRS])
def test_bad_string_fires_expected_rules(tmp_path, item):
    name, pair = item
    if not pair["expected_rules"]:
        pytest.skip("not machine-detectable by design")
    harness = HARNESSES[name]
    fired = set(rules_of(harness.run_pair(tmp_path, pair, "bad")))
    missing = set(pair["expected_rules"]) - fired
    assert not missing, (
        f"{pair['id']}: expected {sorted(missing)} to fire on {pair['bad']!r}, "
        f"got {sorted(fired)}")


@pytest.mark.parametrize("item", ALL_PAIRS, ids=[pair_id(i) for i in ALL_PAIRS])
def test_good_string_is_clean(tmp_path, item):
    name, pair = item
    findings = HARNESSES[name].run_pair(tmp_path, pair, "good")
    assert not findings, (
        f"{pair['id']}: false positives on correct copy {pair['good']!r} — "
        + "; ".join(f"{f.rule} {f.message}" for f in findings))


# --------------------------------------------------------------------------- #
# Rule behaviour that the corpus does not cover
# --------------------------------------------------------------------------- #
def _needs_superlatives(skill):
    if not skill.blocklists.superlatives:
        pytest.skip(f"{skill.name} ships no superlative patterns")


def test_proof_annotation_suppresses_law001(tmp_path, skill):
    _needs_superlatives(skill)
    bare = skill.run(tmp_path, "Thương hiệu số 1 Việt Nam")
    assert "LAW001" in rules_of(bare)
    annotated = skill.run(
        tmp_path, "Thương hiệu số 1 Việt Nam <!-- proof: Khảo sát Nielsen 2026 -->")
    assert "LAW001" not in rules_of(annotated)
    above = skill.run(
        tmp_path, "<!-- proof: Khảo sát Nielsen 2026 -->\nThương hiệu số 1 Việt Nam")
    assert "LAW001" not in rules_of(above)


def test_law001_is_never_an_error(tmp_path, skill):
    _needs_superlatives(skill)
    findings = skill.run(tmp_path, "Thương hiệu số 1 Việt Nam")
    law = [f for f in findings if f.rule == "LAW001"]
    assert law, "expected LAW001 to fire"
    assert all(f.severity == skill.V.WARN for f in law), "LAW001 must warn, never error"


def test_file_level_disable(tmp_path, skill):
    text = "<!-- vlc-disable: NUM001 -->\nGiá 2,500,000 VND"
    assert "NUM001" not in rules_of(skill.run(tmp_path, text))


def test_disable_all(tmp_path, skill):
    text = "<!-- vlc-disable: all -->\nGiá 2,500,000 VND"
    assert skill.run(tmp_path, text) == []


def test_line_level_disable(tmp_path, skill):
    text = "Giá 2,500,000 VND <!-- vlc-disable-line NUM001 -->\nGiá 3,500,000 VND"
    fired = skill.run(tmp_path, text)
    assert [f.line for f in fired if f.rule == "NUM001"] == [2]


def test_directives_work_in_json(tmp_path, skill):
    text = '{\n  "note": "vlc-disable: NUM001",\n  "price": "2,500,000 VND"\n}'
    assert "NUM001" not in rules_of(skill.run(tmp_path, text, filename="vi.json"))


def test_disable_directive_does_not_swallow_the_rest_of_the_line(tmp_path, skill):
    text = "<!-- vlc-disable: NUM001 --> Giá 2,500,000 VND và ngày 12/25/2026"
    assert "DATE001" in rules_of(skill.run(tmp_path, text))


def test_code_spans_are_not_linted(tmp_path, skill):
    assert skill.run(tmp_path, "Dùng `2,500,000` trong ví dụ") == []


def test_fenced_blocks_are_not_linted(tmp_path, skill):
    text = "```\nGiá 2,500,000 VND\n```"
    assert skill.run(tmp_path, text) == []


def test_tone_consistency_only_flags_mixing(tmp_path, skill):
    assert "TONE001" not in rules_of(skill.run(tmp_path, "Hoà bình, thuỷ chung, khoẻ mạnh"))
    assert "TONE001" not in rules_of(skill.run(tmp_path, "Hòa bình, thủy chung, khỏe mạnh"))
    assert "TONE001" in rules_of(skill.run(tmp_path, "Hoà bình nhưng thủy chung"))


def test_quy_does_not_trigger_tone_rule(tmp_path, skill):
    assert "TONE001" not in rules_of(skill.run(tmp_path, "Quý khách và quỹ đầu tư"))


def test_icu_rejects_every_non_other_category(tmp_path, skill):
    for category in ("one", "few", "many", "zero", "two"):
        text = '{"n": "{count, plural, %s {# tệp} other {# tệp}}"}' % category
        assert "ICU001" in rules_of(skill.run(tmp_path, text, filename="vi.json")), category


def test_icu_allows_explicit_value_selectors(tmp_path, skill):
    text = '{"n": "{count, plural, =0 {Chưa có tệp} other {# tệp}}"}'
    assert "ICU001" not in rules_of(skill.run(tmp_path, text, filename="vi.json"))


def test_nfc_fix_round_trip(tmp_path, skill):
    decomposed = "Đăng ký ngay"
    path = tmp_path / "nfd.md"
    with path.open("w", encoding="utf-8", newline="") as handle:
        handle.write(decomposed)
    assert skill.V.fix_nfc(path) is True
    assert skill.V.fix_nfc(path) is False
    assert skill.V.Validator(skill.blocklists).check_file(path) == []


def test_register_check_requires_the_flag(tmp_path, skill):
    text = "Bạn hãy đăng ký ngay"
    assert "PRO002" not in rules_of(skill.run(tmp_path, text))
    assert "PRO002" in rules_of(skill.run(tmp_path, text, register="re"))


def test_unknown_register_is_a_usage_error(tmp_path, skill, capsys):
    path = tmp_path / "x.md"
    path.write_text("Xin chào", encoding="utf-8")
    assert skill.V.main([str(path), "--refs", str(skill.refs),
                         "--register", "no-such-register"]) == 2


def test_exit_codes(tmp_path, skill, capsys):
    clean = tmp_path / "clean.md"
    clean.write_text("Tìm hiểu thêm về dự án", encoding="utf-8")
    assert skill.V.main([str(clean), "--refs", str(skill.refs)]) == 0

    warned = tmp_path / "warn.md"
    warned.write_text("can ho cao cap", encoding="utf-8")
    assert skill.V.main([str(warned), "--refs", str(skill.refs)]) == 0
    assert skill.V.main([str(warned), "--refs", str(skill.refs), "--strict"]) == 1

    broken = tmp_path / "broken.md"
    broken.write_text("Giá 2,500,000 VND", encoding="utf-8")
    assert skill.V.main([str(broken), "--refs", str(skill.refs)]) == 1


def test_json_output_is_parseable(tmp_path, skill, capsys):
    path = tmp_path / "x.md"
    path.write_text("Giá 2,500,000 VND", encoding="utf-8")
    skill.V.main([str(path), "--refs", str(skill.refs), "--json"])
    payload = json.loads(capsys.readouterr().out)
    assert payload["errors"] >= 1
    assert payload["findings"][0]["rule"] == "NUM001"


def test_list_rules_exits_clean(skill, capsys):
    assert skill.V.main(["--list-rules"]) == 0
    assert "NFC001" in capsys.readouterr().out


# --------------------------------------------------------------------------- #
# The skill's own documentation must pass its own linter
# --------------------------------------------------------------------------- #
DOC_PATHS = [(name, p)
             for name, d, _ in SKILL_SPECS
             for p in sorted(d.rglob("*.md")) + sorted(d.glob("assets/*"))]


@pytest.mark.parametrize(
    "item", DOC_PATHS,
    ids=[f"{name}::{p.name}" for name, p in DOC_PATHS])
def test_skill_docs_are_clean(item):
    name, path = item
    harness = HARNESSES[name]
    findings = harness.V.Validator(harness.blocklists).check_file(path)
    errors = [f for f in findings if f.severity == harness.V.ERROR]
    assert not errors, "\n".join(f.render() for f in errors)
