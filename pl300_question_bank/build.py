"""Render the ten practice sets to HTML (print.js turns the HTML into a PDF).

    python3 build.py            -> out/pl300_test_sets.html
    node print.js               -> ../PL-300_Practice_Test_Sets.pdf
"""
import html
import importlib
import os
import random
import re
from collections import Counter

from model import DOMAINS, L, SUBAREAS

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")

TARGET = {"P1": 4, "P2": 3, "P3": 5, "M1": 4, "M2": 6, "M3": 2, "V1": 5, "V2": 5, "V3": 3, "S1": 4, "S2": 4}
KIND_LABEL = {
    "single": "Single answer",
    "multi": "Multiple response — choose {choose}",
    "yesno": "Hot area — Yes / No for each statement",
    "match": "Drag and drop — match",
    "order": "Build list — sequence",
}


def esc(s):
    """Escape text and turn `code` spans into <code>."""
    s = html.escape(s, quote=False)
    return re.sub(r"`([^`]+)`", r"<code>\1</code>", s)


def para(s):
    return "".join(f"<p>{esc(p.strip())}</p>" for p in s.split("\n\n") if p.strip())


def flatten(items):
    """Yield (question, case_or_None) in paper order."""
    for it in items:
        if it["kind"] == "case":
            for q in it["questions"]:
                yield q, it
        else:
            yield it, None


def answer_text(q):
    k = q["kind"]
    if k == "single":
        return q["answer"]
    if k == "multi":
        return ", ".join(q["answer"])
    if k == "yesno":
        return " · ".join("Yes" if v else "No" for _, v in q["statements"])
    if k == "match":
        return "  ".join(f"{i + 1}→{L[q['options'].index(a)]}" for i, (_, a) in enumerate(q["rows"]))
    if k == "order":
        return " → ".join(q["answer"])
    raise ValueError(k)


def render_question(n, q):
    k = q["kind"]
    label = KIND_LABEL[k].format(choose=q.get("choose", ""))
    h = [f'<div class="q"><div class="qhead"><span class="qn">Q{n}</span>'
         f'<span class="qtype">{label}</span></div>']
    h.append(f'<div class="stem">{para(q["stem"])}</div>')
    if q.get("code"):
        h.append(f'<pre class="code">{html.escape(q["code"])}</pre>')
    if k in ("single", "multi"):
        h.append('<ol class="opts">')
        for i, o in enumerate(q["options"]):
            h.append(f'<li><span class="ol">{L[i]}</span><span>{esc(o)}</span></li>')
        h.append("</ol>")
    elif k == "yesno":
        h.append('<table class="yn"><thead><tr><th>Statement</th><th>Yes</th><th>No</th></tr></thead><tbody>')
        for i, (s, _) in enumerate(q["statements"]):
            h.append(f'<tr><td><b>{i + 1}.</b> {esc(s)}</td><td class="c">○</td><td class="c">○</td></tr>')
        h.append("</tbody></table>")
    elif k == "match":
        h.append('<div class="match"><div class="pool"><div class="pt">Choices — each may be used once, more than once, or not at all</div><ol class="opts">')
        for i, o in enumerate(q["options"]):
            h.append(f'<li><span class="ol">{L[i]}</span><span>{esc(o)}</span></li>')
        h.append(f'</ol></div><table class="mt"><thead><tr><th>{esc(q["left"])}</th><th>{esc(q["right"])}</th></tr></thead><tbody>')
        for i, (r, _) in enumerate(q["rows"]):
            h.append(f'<tr><td><b>{i + 1}.</b> {esc(r)}</td><td class="blank"></td></tr>')
        h.append("</tbody></table></div>")
    elif k == "order":
        h.append(f'<div class="pt">Select the {q["nsteps"]} actions required and arrange them in the correct order.'
                 f'{" Not every action is used." if len(q["options"]) > q["nsteps"] else ""}</div><ol class="opts">')
        for i, o in enumerate(q["options"]):
            h.append(f'<li><span class="ol">{L[i]}</span><span>{esc(o)}</span></li>')
        h.append("</ol>")
    h.append("</div>")
    return "".join(h)


def render_case(c, first_n, count):
    req = "".join(f"<li>{esc(r)}</li>" for r in c["requirements"])
    return (f'<div class="case"><div class="casehead">Case study · {esc(c["title"])}'
            f'<span>Questions {first_n}–{first_n + count - 1}</span></div>'
            f'<div class="casecols"><div><h4>Existing environment</h4>{para(c["environment"])}</div>'
            f'<div><h4>Requirements</h4><ol class="req">{req}</ol></div></div>'
            f'<div class="casenote">Once you move past this case study you cannot return to it. '
            f'Read the requirements before the questions.</div></div>')


def balance(flat, idx):
    """Spread single-answer keys evenly across letters, in a seeded random order,
    by swapping the correct option into its target slot."""
    qs = [q for q, _ in flat if q["kind"] == "single" and not q.get("fixed")]
    targets = []
    while len(targets) < len(qs):
        targets += list("ABCD")
    targets = targets[: len(qs)]
    random.Random(300 + idx).shuffle(targets)
    for q, t in zip(qs, targets):
        n = len(q["options"])
        if L.index(t) >= n:
            continue
        a, b = L.index(q["answer"]), L.index(t)
        q["options"][a], q["options"][b] = q["options"][b], q["options"][a]
        q["answer"] = t


def render_set(idx, mod):
    items = mod.ITEMS
    flat = list(flatten(items))
    balance(flat, idx)
    assert len(flat) == 45, (idx, len(flat))
    subs = Counter(q["sub"] for q, _ in flat)
    assert dict(subs) == TARGET, (idx, dict(subs))
    doms = Counter(q["dom"] for q, _ in flat)
    for i, (q, _) in enumerate(flat):
        bad = re.search(r"\b[Oo]ptions? [A-E]\b|\([A-E]\)|\b(first|second|third|fourth|last|other two|last two|first two) options?\b", q["expl"])
        assert not bad, (idx, i + 1, "explanation refers to an option letter")

    out = [f'<section class="set" id="set{idx}">']
    out.append(f'<div class="sethead"><div class="setno">Set {idx:02d}</div>'
               f'<div class="settitle">{esc(mod.TITLE)}</div>'
               f'<div class="setsub">{esc(mod.SUBTITLE)}</div>'
               f'<div class="setmeta"><span>45 questions</span><span>100 minutes</span>'
               f'<span>Pass mark used here: 34 / 45 (75%)</span><span>{esc(mod.LEVEL)}</span></div>'
               f'<table class="mix"><tr>'
               + "".join(f'<td><b>{doms[d]}</b><br>{esc(DOMAINS[d][0])}<br><i>{DOMAINS[d][1]}</i></td>' for d in "PMVS")
               + '</tr></table></div>')

    n = 0
    for it in items:
        if it["kind"] == "case":
            out.append(render_case(it, n + 1, len(it["questions"])))
            for q in it["questions"]:
                n += 1
                out.append(render_question(n, q))
        else:
            n += 1
            out.append(render_question(n, it))
    out.append(f'<div class="endset">End of Set {idx:02d} — answers follow on the next page.</div></section>')

    # Answer key
    out.append(f'<section class="answers"><div class="anshead">Set {idx:02d} · Answer key</div>')
    out.append('<table class="grid"><thead><tr><th>Q</th><th>Answer</th><th>Area</th><th>✓</th>'
               '<th>Q</th><th>Answer</th><th>Area</th><th>✓</th>'
               '<th>Q</th><th>Answer</th><th>Area</th><th>✓</th></tr></thead><tbody>')
    for r in range(15):
        out.append("<tr>")
        for c in range(3):
            i = r + 15 * c
            q = flat[i][0]
            out.append(f'<td class="qn2">{i + 1}</td><td class="ak">{esc(answer_text(q))}</td>'
                       f'<td class="area">{q["sub"]}</td><td class="tick"></td>')
        out.append("</tr>")
    out.append("</tbody></table>")
    out.append('<table class="tally"><thead><tr><th>Sub-area</th><th>Questions</th><th>Your score</th></tr></thead><tbody>')
    for s in TARGET:
        out.append(f'<tr><td>{s} · {esc(SUBAREAS[s][1])}</td><td class="c">{subs[s]}</td><td></td></tr>')
    out.append('<tr class="tot"><td>Total — 34 or more is a pass on this paper</td><td class="c">45</td><td></td></tr></tbody></table>')
    out.append('<p class="scoring">Scoring: one mark per question. For multiple-response, Yes/No, matching and build-list items, '
               'score the fraction of parts you got right (the real exam gives partial credit on multi-part items and never penalises a wrong answer).</p>')

    out.append('<div class="exphead">Explanations</div>')
    for i, (q, _) in enumerate(flat):
        out.append(f'<div class="exp"><div class="ehead"><span class="qn">Q{i + 1}</span>'
                   f'<span class="eans">Answer: {esc(answer_text(q))}</span>'
                   f'<span class="earea">{q["sub"]} · {esc(SUBAREAS[q["sub"]][1])}</span></div>'
                   f'{para(q["expl"])}</div>')
    out.append("</section>")
    return "".join(out), subs


def build():
    sets = [importlib.import_module(f"sets.set{i:02d}") for i in range(1, 11)]
    body, all_subs = [], []
    for i, m in enumerate(sets, 1):
        b, subs = render_set(i, m)
        body.append(b)
        all_subs.append(subs)

    # duplicate-stem guard across the bank
    stems = Counter(q["stem"].strip() for m in sets for q, _ in flatten(m.ITEMS))
    dup = [s for s, c in stems.items() if c > 1]
    assert not dup, dup[:3]

    kinds = Counter(q["kind"] for m in sets for q, _ in flatten(m.ITEMS))
    toc = "".join(f'<tr><td>Set {i:02d}</td><td>{esc(m.TITLE)}</td><td>{esc(m.LEVEL)}</td>'
                  f'<td>{esc(m.CASE_NAME)}</td></tr>' for i, m in enumerate(sets, 1))
    cov = "".join(f'<tr><td>{s} · {esc(SUBAREAS[s][1])}</td>'
                  + "".join(f'<td class="c">{x[s]}</td>' for x in all_subs)
                  + f'<td class="c"><b>{sum(x[s] for x in all_subs)}</b></td></tr>' for s in TARGET)
    kindrow = " · ".join(f"{KIND_LABEL[k].split(' —')[0]}: {v}" for k, v in kinds.items())

    front = FRONT.format(toc=toc, cov=cov, kinds=kindrow,
                         heads="".join(f"<th>S{i}</th>" for i in range(1, 11)))
    doc = TEMPLATE.replace("/*CSS*/", open(os.path.join(HERE, "style.css")).read())
    doc = doc.replace("<!--BODY-->", front + "".join(body))
    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, "pl300_test_sets.html"), "w") as f:
        f.write(doc)
    print("ok:", sum(kinds.values()), "questions;", dict(kinds))


TEMPLATE = """<!doctype html><html lang="en"><head><meta charset="utf-8">
<title>PL-300 Practice Test Sets</title><style>/*CSS*/</style></head><body><!--BODY--></body></html>"""

FRONT = open(os.path.join(HERE, "front.html"), encoding="utf-8").read()

if __name__ == "__main__":
    build()
