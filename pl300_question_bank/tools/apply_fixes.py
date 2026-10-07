"""Apply scoped text replacements to set files.

Each fix is (stem_prefix, old, new). The replacement happens only inside the
question whose stem starts with stem_prefix (up to the next question), so an
option text that also appears in other questions is never touched there.
Text is given unescaped; double quotes are escaped to match the source.

    python3 tools/apply_fixes.py tools/fixes_set01.py
"""
import re
import runpy
import sys

STARTS = re.compile(r'\n(?:\s*)(single|multi|yesno|match|order|case)\("')


def esc(s):
    return s.replace("\\", "\\\\").replace('"', '\\"')


def apply(path, fixes):
    src = open(path, encoding="utf-8").read()
    for stem, old, new in fixes:
        key = esc(stem)
        i = src.find(key)
        assert i >= 0, f"stem not found: {stem[:60]}"
        assert src.find(key, i + 1) < 0, f"stem not unique: {stem[:60]}"
        m = STARTS.search(src, i + len(key))
        j = m.start() if m else len(src)
        block = src[i:j]
        o, n = esc(old), esc(new)
        if block.count(o) != 1:  # fall back to a whole quoted string
            o, n = f'"{o}"', f'"{n}"'
        assert block.count(o) == 1, f"'{old[:50]}' found {block.count(o)}x in: {stem[:50]}"
        src = src[:i] + block.replace(o, n) + src[j:]
    open(path, "w", encoding="utf-8").write(src)
    print(f"{path}: {len(fixes)} replacements")


if __name__ == "__main__":
    for f in sys.argv[1:]:
        ns = runpy.run_path(f)
        apply(ns["TARGET"], ns["FIXES"])
