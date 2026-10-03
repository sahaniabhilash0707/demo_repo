"""Validate the set files that exist so far: python3 check.py"""
import importlib, os, collections
import build
seen = collections.Counter()
for i in range(1, 11):
    if not os.path.exists(f"sets/set{i:02d}.py"):
        continue
    m = importlib.import_module(f"sets.set{i:02d}")
    _, subs = build.render_set(i, m)
    flat = list(build.flatten(m.ITEMS))
    letters = collections.Counter(q["answer"] for q, _ in flat if q["kind"] == "single")
    kinds = collections.Counter(q["kind"] for q, _ in flat)
    for q, _ in flat:
        seen[q["stem"].strip()] += 1
    print(f"set{i:02d} ok", dict(kinds), "single letters:", dict(sorted(letters.items())))
dups = [s[:70] for s, c in seen.items() if c > 1]
print("duplicate stems:", dups or "none")
