# Guruji's Price-Action Manual

`Guruji_Price_Action_Manual.pdf`: a 60-page manual on how the NIFTY weekly-options market traps retail traders and how to trade with smart money. It has 27 chapters in four parts, 45 annotated charts, five A+ setups, a one-page cheat sheet and a glossary.

Each chapter covers seven things in order:

- (a) the concept
- (b) why it works
- (c) annotated chart(s)
- (d) a NIFTY example with realistic levels
- (e) a rule-based entry, stop-loss and target
- (f) common mistakes
- (g) a three-point summary

## Rebuild

```bash
pip install matplotlib reportlab pillow
python3 charts_part12.py   # charts for chapters 1-13 -> charts/
python3 charts_ch14.py     # chapter 14 (overshoot trap; copies source/reader_chart_nifty_5m.png)
python3 charts_part34.py   # charts for chapters 15-27 -> charts/
python3 build_pdf.py       # -> Guruji_Price_Action_Manual.pdf
```

| File | Purpose |
|---|---|
| `charts_engine.py` | Synthetic OHLC generator, dark-theme candlesticks, annotation helpers, Black-Scholes pricing |
| `charts_part12.py`, `charts_ch14.py`, `charts_part34.py` | One function per chart (data scenario + annotations) |
| `source/reader_chart_nifty_5m.png` | The reader's own NIFTY 5-min chart, used as the real example in chapter 14 |
| `content_a.py`, `content_b.py` | All chapter text, the verified-facts table, the cheat sheet and the glossary |
| `build_pdf.py` | ReportLab layout: cover, TOC, chapter template, callouts, page numbers |

All chart data is synthetic, except the reader's own chart in chapter 14. The option premiums in chapters 10, 11 and 23 are computed with Black-Scholes from the spot path. The market facts (lot size 65, Tuesday expiry, SEBI rules, STT 0.15%) were verified on 6 Oct 2026. Re-check them every June and December.

This manual is educational material, not investment advice.
