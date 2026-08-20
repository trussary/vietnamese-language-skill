<!-- vlc-disable: CAL001, DIA001 -->

# Code-switching — which words stay English

The central rule of this skill, and the one that separates writing by a Vietnamese engineer
from writing by a translation engine.

Vietnamese engineering prose is **natively bilingual**. `deploy`, `commit`, `merge`, `bug`,
`server`, `cache`, `deadline` stay in English inside otherwise-Vietnamese sentences. This is
not laziness or a lack of vocabulary — the Vietnamese equivalents exist, and using them in
casual technical writing is what marks the text as machine-produced.

> Sau khi review xong thì mình sẽ merge vào nhánh main rồi deploy lên production.

That sentence is native. Every English word in it is correct, and translating any of them
makes it worse.

## The rule of thumb

| Situation | What to do |
|---|---|
| The term names a tool, command, or Git/CI concept | Keep English (`commit`, `merge`, `rebase`, `deploy`, `rollback`, `pipeline`) |
| The term is a user-visible noun in product copy | Translate (`lỗi`, `tệp`, `tài khoản`, `mật khẩu`) |
| Formal written spec, published documentation | Vietnamese is acceptable and often preferred (`bộ nhớ đệm`, `cơ sở dữ liệu`) |
| Team chat, PR description, code review | English term, Vietnamese grammar |
| It is an identifier, branch, or command | English, ASCII, always |

The axis is **formality**, not correctness. `bộ nhớ đệm` in a published architecture document
is good writing; `bộ nhớ đệm` in a PR comment reads like a textbook.

## Terminology

The calque blocklist lives in [glossary.md](glossary.md), which `validate_copy.py` loads
directly — adding a row there adds a lint rule. The sharpest entry in it is `cam kết` for
`commit`: a real Vietnamese word meaning *to pledge*, so it never looks misspelled, it just
means something else entirely. Nobody who writes Vietnamese and uses Git has produced it.

## Terms where both forms are live

Neither is a defect. Pick one per document and stay with it — the inconsistency is the
problem, not the choice.

| EN | English form | Vietnamese form | Leans |
|---|---|---|---|
| server | `server` | `máy chủ` | `máy chủ` in formal docs and to non-engineers |
| database | `database` | `cơ sở dữ liệu` | `cơ sở dữ liệu` in specs, `database` in chat |
| cache | `cache` | `bộ nhớ đệm` | `bộ nhớ đệm` in published docs only |
| patch | `patch` | `bản vá` | `bản vá` in security advisories |
| library | `library` | `thư viện` | `thư viện` is fully naturalized |
| network | `network` | `mạng` | `mạng` is fully naturalized |

House style decides these. If the repo already says `máy chủ`, keep saying `máy chủ`.

## Identifiers, branches, and commit subjects

**ASCII only. No diacritics, ever.** This is not a style preference:

- Vietnamese filenames and branch names break on case-insensitive filesystems and in tools
  that assume ASCII paths.
- Git, CI runners, and shell scripts mangle them in ways that surface much later.
- The NFC/NFD distinction means two visually identical branch names can be different strings.

```
❌  feat/thêm-đăng-nhập          ✅  feat/add-login
❌  git commit -m "Sửa lỗi đăng nhập"   ✅  git commit -m "fix: login validation"
❌  const tênNgườiDùng = ...      ✅  const userName = ...
```

Rule `ENG001` flags this, as an error, when you pass `--doctype commit`, `--doctype branch`
or `--doctype identifier`.

The **body** of a commit message is different — Vietnamese prose there is fine and common.
The constraint is on the subject line, the branch name, and code identifiers.

## What not to over-correct

Do not strip Vietnamese out of technical writing to sound more professional. Vietnamese
carries the grammar; English carries the nouns. A document that is 80% English terms with
Vietnamese connectives is as unnatural as one that translates `commit`.

The test is whether a Vietnamese engineer would say the sentence out loud.
