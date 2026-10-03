"""Question constructors used by the set files.

Domains:  M = Maintain a data analytics solution
          P = Prepare data
          S = Implement and manage semantic models
Sub-areas: M1 security & governance, M2 development lifecycle,
           P1 get data, P2 transform data, P3 query and analyze data,
           S1 design and build semantic models, S2 optimize enterprise-scale models
"""
import random
import zlib

SUBAREAS = {
    "M1": ("M", "Implement security and governance"),
    "M2": ("M", "Maintain the analytics development lifecycle"),
    "P1": ("P", "Get data"),
    "P2": ("P", "Transform data"),
    "P3": ("P", "Query and analyze data"),
    "S1": ("S", "Design and build semantic models"),
    "S2": ("S", "Optimize enterprise-scale semantic models"),
}
DOMAINS = {
    "M": ("Maintain a data analytics solution", "25–30%"),
    "P": ("Prepare data", "45–50%"),
    "S": ("Implement and manage semantic models", "25–30%"),
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
