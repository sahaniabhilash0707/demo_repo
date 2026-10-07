# PL-300 practice test sets: source

The source behind `../PL-300_Practice_Test_Sets.pdf`: 10 practice sets of 45 questions each, with answer keys and explanations. The questions are written against the April 2026 PL-300 skills outline. They are original, and none of them repeats the 72 questions in the PL-300 Study and Question Guide.

- `sets/set01.py` … `sets/set10.py`: the questions. Every set has the same blueprint split (P1 4, P2 3, P3 5, M1 4, M2 6, M3 2, V1 5, V2 5, V3 3, S1 4, S2 4), and that includes a four-question case study.
- `model.py`: the sub-areas and the question types (single, multi, yes/no, match, order, case). Options are shuffled deterministically when the PDF is built.
- `build.py`: renders the HTML from `front.html` and the sets, and balances the single-answer letters across each set.
- `print.js`: prints the HTML to PDF with Playwright and Chromium.
- `check.py`: validates the sets. It checks the counts per sub-area, duplicate stems, and explanations that refer to an option letter.
- `tools/apply_fixes.py`: applies wording fixes to one question at a time, located by its stem. The `tools/fixes_setNN.py` files record the edits that stopped the correct answer from usually being the longest option.

To regenerate the PDF:

```
python3 check.py
python3 build.py
node print.js        # writes ../PL-300_Practice_Test_Sets.pdf
```
