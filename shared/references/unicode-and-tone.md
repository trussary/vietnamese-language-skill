<!-- vlc-disable: TONE001 -->

# Unicode and tone marks

Shared by every skill in this repo. Both rules here are invisible to reading — you cannot
proofread your way to them, which is why they are linted rather than documented and hoped for.

## Emit NFC, always

Vietnamese letters carrying both a diacritic and a tone mark exist in two encodings:

| | Codepoints | `len()` |
|---|---|---|
| NFC (precomposed) | `ế` = U+1EBF | 1 |
| NFD (decomposed) | `ế` = U+0065 U+0302 U+0301 | 3 |

They render identically in most editors and compare unequal in every string API. NFD breaks
web-font rendering (many subsets ship precomposed glyphs only), inflates character counts
past platform limits, and silently defeats search and deduplication.

**Normalize everything you output to NFC.** `NFC001` is an error, not a warning, and
`validate_copy.py --fix` repairs it in place — the only rule in the repo that auto-fixes,
because it is the only one with no judgement in it.

macOS filesystems hand back NFD filenames, and copy-paste out of a PDF is a common NFD source.
Normalize at the boundary, not at the end.

## Pick one tone-mark style and hold it

For open syllables containing `oa`, `oe`, `uy`, two conventions exist for where the tone mark
sits:

| Kiểu cũ (old, visually centred) | Kiểu mới (new, phonetic) |
|---|---|
| `hòa`, `tòa`, `khỏe`, `thủy`, `hóa` | `hoà`, `toà`, `khoẻ`, `thuỷ`, `hoá` |

**Neither is wrong.** Kiểu mới matches school textbooks since Quyết định 1989/QĐ-BGDĐT
(~2022); kiểu cũ remains dominant on commercial websites. These skills default to kiểu mới
and let you override — match the client's existing site when there is one.

When a syllable has a final consonant (`toàn`, `hoàng`, `khoản`, `thuyền`), there is no
ambiguity: the mark always sits on the second vowel.

The actual defect is **mixing both in one document**. `TONE001` flags that and only that.

## Input methods

Forms must accept both Telex (`aa` → `â`, `dd` → `đ`) and VNI (`a6` → `â`, `d9` → `đ`).
Never strip diacritics on input, and never "helpfully" normalize a user's name to ASCII —
`Nguyễn` is the name; `Nguyen` is a slug.

## Collation and search

Vietnamese needs **accent-insensitive** matching: `cà phê` must be findable by typing
`ca phe`. A default byte sort also mis-orders the alphabet — `đ` sorts after `d` and before
`e`, not after `z`. Use a locale-aware collation (`vi_VN.utf8`, ICU `vi`) rather than
`LOWER()` plus luck.

Unaccented forms belong in slugs, meta keywords, and search indexes — never in display copy.
`DIA001` flags unaccented Vietnamese in prose.
