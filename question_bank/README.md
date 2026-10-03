# DP-600 practice test sets: source

The source behind `../DP-600_Practice_Test_Sets.pdf`: 10 practice sets of 45 questions each, with answer keys and explanations.

- `sets/set01.py` … `sets/set10.py`: the questions. Every set has the same blueprint split (M1 6, M2 6, P1 7, P2 8, P3 6, S1 6, S2 6), and that includes a four-question case study.
- `model.py`: the question types (single, multi, yes/no, match, order, case). Options are shuffled deterministically when the PDF is built.
- `build.py`: renders the HTML and balances the single-answer letters across each set.
- `print.js`: prints the HTML to PDF with Playwright and Chromium.
- `check.py`: validates the sets. It checks the counts per sub-area, duplicate stems, and explanations that refer to an option letter.

To regenerate the PDF:

```
python3 check.py
python3 build.py
node print.js        # writes ../DP-600_Practice_Test_Sets.pdf
```
