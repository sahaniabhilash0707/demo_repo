"""Question constructors used by the set files.

Domains:  P = Prepare the data          M = Model the data
          V = Visualize and analyze the data   S = Manage and secure Power BI
Sub-areas follow the PL-300 skills outline (April 2026 revision).
"""
import random
import zlib

SUBAREAS = {
    "P1": ("P", "Get or connect to data"),
    "P2": ("P", "Profile and clean the data"),
    "P3": ("P", "Transform and load the data"),
    "M1": ("M", "Design and implement a data model"),
    "M2": ("M", "Create model calculations by using DAX"),
    "M3": ("M", "Optimize model performance"),
    "V1": ("V", "Create reports"),
    "V2": ("V", "Enhance reports for usability and storytelling"),
    "V3": ("V", "Identify patterns and trends"),
    "S1": ("S", "Create and manage workspaces and assets"),
    "S2": ("S", "Secure and govern Power BI items"),
}
DOMAINS = {
    "P": ("Prepare the data", "25–30%"),
    "M": ("Model the data", "25–30%"),
    "V": ("Visualize and analyze the data", "25–30%"),
    "S": ("Manage and secure Power BI", "15–20%"),
}
L = "ABCDEFGHIJ"


def _q(kind, sub, stem, expl, **kw):
    assert sub in SUBAREAS, sub
    return dict(kind=kind, sub=sub, dom=SUBAREAS[sub][0], stem=stem, expl=expl, **kw)


def _shuffle(stem, options, answer):
    """Deterministically reorder options so answer letters spread evenly.
    answer is a string of letters relative to the authored order."""
    rnd = random.Random(zlib.crc32(stem.encode()))
    idx = list(range(len(options)))
    rnd.shuffle(idx)
    new_opts = [options[i] for i in idx]
    new_ans = "".join(sorted(L[idx.index(L.index(a))] for a in answer))
    return new_opts, new_ans


def single(sub, stem, options, answer, expl, code=None, fixed=False):
    """One correct option. answer is a letter (in authored order)."""
    assert answer in L[: len(options)]
    if not fixed:
        options, answer = _shuffle(stem, options, answer)
    return _q("single", sub, stem, expl, options=options, answer=answer, code=code, fixed=fixed)


def multi(sub, stem, options, answer, expl, code=None, fixed=False):
    """Several correct options. answer is a string of letters, e.g. 'AC'."""
    assert all(a in L[: len(options)] for a in answer)
    if not fixed:
        options, answer = _shuffle(stem, options, answer)
    n = len(answer)
    word = {2: "TWO", 3: "THREE", 4: "FOUR"}[n]
    return _q("multi", sub, stem, expl, options=options, answer=answer, code=code, choose=word)


def yesno(sub, stem, statements, expl, code=None):
    """Hot-area grid: statements is a list of (text, bool)."""
    return _q("yesno", sub, stem, expl, statements=statements, code=code)


def match(sub, stem, rows, options, expl, left="Requirement", right="Choice"):
    """Drag and drop. rows: list of (prompt, correct option text). options: all
    option texts (each may be used once, more than once or not at all)."""
    for _, ans in rows:
        assert ans in options, ans
    rnd = random.Random(zlib.crc32(stem.encode()))
    options = list(options)
    natural = [a for _, a in rows]
    for _ in range(20):
        rnd.shuffle(options)
        if options[: len(natural)] != natural:
            break
    return _q("match", sub, stem, expl, rows=rows, options=options, left=left, right=right)


def order(sub, stem, steps, expl, extra=(), seed=0):
    """Build list: steps in the correct order; extra are distractor actions.
    Displayed shuffled; answer is the sequence of letters."""
    pool = list(steps) + list(extra)
    rnd = random.Random(seed or zlib.crc32(stem.encode()))
    shown = pool[:]
    while True:
        rnd.shuffle(shown)
        if shown[: len(steps)] != list(steps):
            break
    seq = "".join(L[shown.index(s)] for s in steps)
    return _q("order", sub, stem, expl, options=shown, answer=seq, nsteps=len(steps))


def case(title, environment, requirements, questions):
    return dict(kind="case", title=title, environment=environment,
                requirements=requirements, questions=questions)
