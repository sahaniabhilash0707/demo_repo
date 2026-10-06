"""Charts for Part 3 (ch 14-20) and Part 4 (ch 21-26)."""
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FuncFormatter

from charts_engine import (AMBER, BG, BLUE, CYAN, DN, GRID, MAG, MUTED, ORANGE, PANEL, PURPLE, TXT, UP, WHITE,
                           YEL, _fmt, candles, figure, frame, gen, level, note, save, setb, step, stops, times,
                           tline, trade, vline, volume, vwap, zone)
from charts_part12 import day_ticks, expiry_series


def _style(a):
    a.yaxis.tick_right()
    a.tick_params(length=0)
    a.yaxis.set_major_formatter(FuncFormatter(_fmt))


def _titles(fig, title, sub, note_txt="Synthetic NIFTY data · illustration only"):
    fig.text(0.012, 0.975, title, fontsize=11.5, fontweight="bold", color=WHITE, va="top")
    if sub:
        fig.text(0.012, 0.935, sub, fontsize=8, color=MUTED, va="top")
    fig.text(0.988, 0.012, note_txt, fontsize=6.5, color=MUTED, ha="right")


# ---------------------------------------------------------------- ch14
def c14():
    n = 60
    d = gen([(0, 25760), (5, 25715), (8, 25735), (12, 25618), (13, 25615), (17, 25705), (21, 25722), (25, 25742),
             (30, 25700), (34, 25672), (38, 25634), (40, 25660), (46, 25700), (52, 25735), (59, 25762)],
            n, noise=4, wick=3, seed=141)
    setb(d, 8, h=25742)
    setb(d, 9, o=25726, h=25729, l=25638, c=25642, v=260)
    setb(d, 10, o=25642, h=25644, l=25622, c=25628, v=150)
    setb(d, 11, o=25628, h=25634, l=25612, c=25626, v=140)
    setb(d, 12, o=25626, h=25632, l=25610, c=25618, v=130)
    setb(d, 13, o=25622, h=25636, l=25606, c=25612, v=170)
    setb(d, 14, o=25612, h=25646, l=25610, c=25643, v=380)
    setb(d, 15, o=25643, h=25676, l=25641, c=25672, v=420)
    setb(d, 16, o=25672, h=25702, l=25670, c=25698, v=400)
    setb(d, 38, o=25646, h=25648, l=25628, c=25641, v=230)
    setb(d, 39, o=25641, h=25662, l=25638, c=25659, v=260)
    fig, ax, ax2 = figure(lower=True)
    candles(ax, d)
    ax.set_xlim(-1, n + 9)
    ax.set_ylim(25580, 25790)
    volume(ax2, d, highlight=[14, 15, 16])
    zone(ax, 25606, 25636, UP, None, x0=12.6, x1=n + 8, alpha=0.18)
    ax.text(17.5, 25621, "Demand zone / order block 25,606-25,636", color=UP, fontsize=7.6, fontweight="bold", va="center")
    level(ax, 25742, "Prior LH 25,742", MUTED, x0=8, x1=24, side="right")
    ax.text(24.3, 25744, "BOS", color=UP, fontsize=7.6, fontweight="bold", va="bottom")
    step(ax, 13, 25660, 1, AMBER, "Base: last red candle\nbefore the explosion", tx=1, ty=25690)
    step(ax, 15, 25690, 2, UP, "Displacement: 3 big candles,\nvolume 3x = institutions buying", tx=18, ty=25662)
    step(ax, 38, 25618, 3, YEL, "Return to zone: unfilled\norders defend it", tx=41, ty=25603)
    trade(ax, 39, 25645, 25598, 25740, x1=n - 1, side="long")
    frame(fig, ax, "Ch 14 · Demand zone and order block",
          "5-min · A base that launched a displacement leaves unfilled buy orders behind", times(n, "10:00"),
          step=6, ax2=ax2)
    save(fig, "c14")


# ---------------------------------------------------------------- ch15
def c15():
    n = 46
    d = gen([(0, 25700), (5, 25718), (9, 25712), (12, 25735), (13, 25786), (15, 25790), (20, 25815), (24, 25796),
             (28, 25770), (30, 25758), (33, 25785), (38, 25812), (45, 25850)], n, noise=3.5, wick=3, seed=151)
    setb(d, 12, o=25725, h=25742, l=25722, c=25738, v=160)
    setb(d, 13, o=25738, h=25792, l=25736, c=25788, v=520)
    setb(d, 14, o=25788, h=25796, l=25768, c=25790, v=260)
    setb(d, 30, o=25763, h=25766, l=25752, c=25761, v=170)
    setb(d, 31, o=25761, h=25779, l=25759, c=25777, v=230)
    fig, ax, ax2 = figure(lower=True)
    candles(ax, d)
    ax.set_xlim(-1, n + 9)
    ax.set_ylim(25670, 25870)
    volume(ax2, d, highlight=[13])
    zone(ax, 25742, 25768, CYAN, None, x0=12.6, x1=n + 8, alpha=0.2)
    ax.text(1, 25684, "FVG 25,742-25,768 (50% = 25,755)", color=CYAN, fontsize=7.6, fontweight="bold", va="center")
    level(ax, 25755, None, CYAN, ls=":", x0=14, x1=n + 8)
    step(ax, 12, 25752, 1, MUTED, "Candle 1 high 25,742", tx=1, ty=25790)
    step(ax, 13, 25805, 2, YEL, "Candle 2: displacement\n(+50 pts, huge volume)", tx=2, ty=25840)
    step(ax, 14, 25760, 3, MUTED, "Candle 3 low 25,768", tx=17, ty=25700)
    step(ax, 30, 25745, 4, UP, "Rebalance: price returns,\nfills orders, resumes", tx=33, ty=25722)
    trade(ax, 31, 25757, 25734, 25812, x1=n - 1, side="long", tgt2=25850)
    frame(fig, ax, "Ch 15 · Fair value gap (imbalance)",
          "5-min · Three-candle pattern: gap between candle 1 high and candle 3 low", times(n, "09:30"), step=6,
          ax2=ax2)
    save(fig, "c15")


# ---------------------------------------------------------------- ch16
def c16():
    n = 75
    d = gen([(0, 25800), (4, 25760), (8, 25700), (10, 25645), (16, 25700), (24, 25650), (30, 25690), (36, 25655),
             (42, 25695), (47, 25640), (52, 25660), (56, 25712), (59, 25722), (62, 25702), (68, 25740),
             (74, 25785)], n, noise=4, wick=3, seed=161)
    setb(d, 10, o=25668, h=25672, l=25630, c=25652, v=520)
    setb(d, 47, o=25650, h=25653, l=25622, c=25647, v=330)
    setb(d, 48, o=25647, h=25662, l=25645, c=25660, v=260)
    setb(d, 52, o=25664, h=25668, l=25652, c=25662, v=90)
    setb(d, 56, o=25690, h=25716, l=25688, c=25712, v=420)
    d["v"][24:46] *= 0.65
    fig, ax, ax2 = figure(lower=True)
    candles(ax, d)
    ax.set_xlim(-1, n + 9)
    ax.set_ylim(25600, 25820)
    volume(ax2, d, highlight=[10, 47, 56])
    zone(ax, 25645, 25700, PURPLE, None, x0=9.5, x1=55, alpha=0.1)
    labels = {10: ("SC", -1), 16: ("AR", 1), 24: ("ST", -1), 47: ("Spring", -1), 52: ("Test", -1), 56: ("SOS", 1),
              62: ("LPS", -1)}
    for i, (t, sgn) in labels.items():
        y = d["h"][i] + 7 if sgn > 0 else d["l"][i] - 7
        ax.text(i, y, t, color=YEL if t in ("Spring", "SOS") else TXT, fontsize=7.8, fontweight="bold",
                ha="center", va="bottom" if sgn > 0 else "top")
    for x0, x1, ph in ((0, 16, "A"), (16, 44, "B"), (44, 54, "C"), (54, 63, "D"), (63, 75, "E")):
        ax.text((x0 + x1) / 2, 25812, f"Phase {ph}", color=MUTED, fontsize=7.4, ha="center", va="top")
        ax.axvline(x1 - 0.5, color=GRID, lw=0.8, ls=":")
    level(ax, 25700, "Range high 25,700", PURPLE, x0=9.5, x1=55, side="left", dy=8)
    note(ax, "Spring: break below the SC low traps\nshort sellers; closes back in range",
         (47, 25621), (24, 25612), ec=YEL)
    trade(ax, 53, 25664, 25618, 25755, x1=n - 1, side="long")
    frame(fig, ax, "Ch 16 · Wyckoff accumulation on a 5-min chart",
          "SC selling climax · AR automatic rally · ST secondary test · SOS sign of strength · LPS last point of "
          "support", times(n), step=6, ax2=ax2)
    save(fig, "c16")


# ---------------------------------------------------------------- ch17
def c17():
    n = 50
    d = gen([(0, 25600), (12, 25700), (22, 25780), (36, 25690), (49, 25640)], n, noise=6, wick=4, seed=171)
    oi = np.concatenate([np.linspace(120, 138, 13), np.linspace(138, 124, 10)[1:], np.linspace(124, 142, 15)[1:],
                         np.linspace(142, 128, 15)[1:]])[:n]
    oi = oi + np.random.default_rng(3).normal(0, 0.6, n)
    fig, ax, ax2 = figure(lower=True, h=5.8, ratios=(2.6, 1.2))
    candles(ax, d)
    ax.set_xlim(-1, n + 1)
    ax.set_ylim(25560, 25830)
    ax2.plot(np.arange(n), oi, color=YEL, lw=1.8)
    ax2.set_ylabel("Fut OI (lakh)", color=MUTED, fontsize=7.5)
    ax2.set_ylim(112, 150)
    segs = [(0, 12, UP, "LONG BUILD-UP\nPrice ↑  OI ↑\nfresh longs: strong"),
            (12, 22, CYAN, "SHORT COVERING\nPrice ↑  OI ↓\nweak rally"),
            (22, 36, DN, "SHORT BUILD-UP\nPrice ↓  OI ↑\nfresh shorts: strong"),
            (36, 49, ORANGE, "LONG UNWINDING\nPrice ↓  OI ↓\nweak fall")]
    for a, b, col, t in segs:
        ax.axvspan(a - 0.5, b - 0.5, color=col, alpha=0.07)
        ax2.axvspan(a - 0.5, b - 0.5, color=col, alpha=0.07)
        ax.text((a + b) / 2 - 0.5, 25822, t, color=col, fontsize=7.2, ha="center", va="top", fontweight="bold")
    frame(fig, ax, "Ch 17 · Price + open interest: four combinations",
          "15-min, two sessions · NIFTY futures OI. Read OI change together with price, never alone", ax2=ax2)
    day_ticks(ax2, n, 25, ["Mon", "Tue"])
    save(fig, "c17")


# ---------------------------------------------------------------- ch18
def c18a():
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(10, 4.4), gridspec_kw={"wspace": 0.16})
    for a in (a1, a2):
        _style(a)
    n = 30
    d = gen([(0, 25720), (8, 25670), (14, 25640), (17, 25606), (18, 25622), (22, 25650), (29, 25690)], n, noise=3,
            wick=2.5, seed=181)
    setb(d, 17, o=25615, h=25619, l=25582, c=25614, v=400)
    setb(d, 18, o=25614, h=25634, l=25612, c=25631)
    candles(a1, d)
    a1.set_xlim(-1, n + 1)
    a1.set_ylim(25560, 25740)
    level(a1, 25600, "PDL 25,600", BLUE, side="left", dy=-8)
    note(a1, "Pin bar AT the level, after a\nsweep of PDL = high-quality signal", (17, 25584), (12, 25700), ec=UP)
    a1.set_title("Location: at key liquidity → TRADE", color=UP, fontsize=9, fontweight="bold")
    d2 = gen([(0, 25720), (6, 25690), (12, 25705), (17, 25672), (20, 25680), (24, 25640), (29, 25610)], n, noise=3,
             wick=2.5, seed=182)
    setb(d2, 17, o=25676, h=25680, l=25648, c=25675)
    candles(a2, d2)
    a2.set_xlim(-1, n + 1)
    a2.set_ylim(25560, 25740)
    note(a2, "Identical pin bar in the middle\nof nowhere = noise; price ignores it", (17, 25650), (2, 25585),
         ec=DN)
    a2.set_title("Location: middle of range → IGNORE", color=DN, fontsize=9, fontweight="bold")
    for a in (a1, a2):
        a.set_xticks([])
    _titles(fig, "Ch 18 · Same candle, different location", None)
    fig.subplots_adjust(left=0.02, right=0.93, top=0.85, bottom=0.05)
    save(fig, "c18a")


def c18b():
    fig, axs = plt.subplots(1, 4, figsize=(10, 3.6), gridspec_kw={"wspace": 0.08})
    specs = [
        ("Pin bar (hammer)", [(25660, 25668, 25652, 25655), (25655, 25658, 25640, 25643), (25643, 25646, 25612, 25641),
                              (25641, 25660, 25639, 25657)], "Long lower wick ≥ 2x body.\nValid at support / after sweep"),
        ("Bullish engulfing", [(25660, 25663, 25648, 25651), (25651, 25654, 25638, 25642), (25640, 25664, 25637, 25662),
                               (25662, 25670, 25659, 25668)], "Body swallows prior body.\nValid at demand / VWAP"),
        ("Inside bar", [(25640, 25676, 25636, 25672), (25668, 25671, 25652, 25656), (25656, 25668, 25654, 25666),
                        (25666, 25685, 25664, 25682)], "Range inside mother bar.\nTrade the break, SL other side"),
        ("Marubozu", [(25640, 25646, 25636, 25644), (25644, 25648, 25640, 25642), (25642, 25680, 25642, 25679),
                      (25679, 25686, 25672, 25684)], "Full body, no wicks.\nShows displacement / intent"),
    ]
    for a, (t, bars, cap) in zip(axs, specs):
        o, h, l_, c = map(np.array, zip(*bars))
        d = {"o": o.astype(float), "h": h.astype(float), "l": l_.astype(float), "c": c.astype(float), "n": len(bars)}
        candles(a, d, width=0.55)
        hl = 2 if t != "Inside bar" else 1
        a.axvspan(hl - 0.45, hl + 0.45 + (1 if t == "Inside bar" else 0), color=YEL, alpha=0.08)
        a.set_xlim(-0.8, 3.8)
        a.set_ylim(25560, 25700)
        a.set_xticks([])
        a.set_yticks([])
        a.set_title(t, color=YEL, fontsize=9, fontweight="bold")
        a.text(1.5, 25563, cap, color=TXT, fontsize=7.2, ha="center", va="bottom")
    _titles(fig, "Ch 18 · Four candles worth knowing (only at a level)", None, "Schematic")
    fig.subplots_adjust(left=0.01, right=0.99, top=0.8, bottom=0.03)
    save(fig, "c18b")


# ---------------------------------------------------------------- ch19
def c19():
    fig = plt.figure(figsize=(10, 6.6))
    gs = fig.add_gridspec(2, 2, height_ratios=[1, 1.05], hspace=0.28, wspace=0.12)
    a1 = fig.add_subplot(gs[0, :])
    a2 = fig.add_subplot(gs[1, 0])
    a3 = fig.add_subplot(gs[1, 1])
    for a in (a1, a2, a3):
        _style(a)
    dd = gen([(0, 24700), (8, 25050), (12, 24920), (20, 25350), (24, 25220), (31, 25720), (35, 25600), (38, 25640)],
             40, noise=40, wick=35, seed=191)
    candles(a1, dd)
    a1.set_xlim(-1, 44)
    a1.set_ylim(24550, 25850)
    zone(a1, 25550, 25620, UP, "Daily demand 25,550-25,620", x0=23, x1=44, side="right", alpha=0.18, ty=25500)
    a1.text(1, 25780, "DAILY: uptrend (HH/HL). Bias = only longs / sell puts", color=UP, fontsize=8.2,
            fontweight="bold")
    a1.set_xticks([])
    d2 = gen([(0, 25720), (8, 25660), (14, 25600), (16, 25585), (19, 25628), (22, 25608), (26, 25650), (29, 25672)],
             30, noise=7, wick=5, seed=192)
    candles(a2, d2)
    a2.set_xlim(-1, 31)
    a2.set_ylim(25550, 25750)
    zone(a2, 25550, 25620, UP, None, alpha=0.15)
    level(a2, 25640, "CHoCH up", YEL, x0=8, x1=30, side="right")
    a2.text(0, 25740, "15-MIN: pullback into daily zone,\nthen CHoCH up = structure turns", color=TXT, fontsize=7.6,
            va="top")
    a2.set_xticks([])
    d3 = gen([(0, 25630), (5, 25612), (8, 25604), (9, 25596), (11, 25620), (16, 25640), (24, 25668)], 25, noise=3,
             wick=2.5, seed=193)
    setb(d3, 9, o=25606, h=25608, l=25588, c=25603, v=300)
    setb(d3, 10, o=25603, h=25624, l=25601, c=25622)
    candles(a3, d3)
    a3.set_xlim(-1, 26)
    a3.set_ylim(25560, 25700)
    stops(a3, 2, 8, 25600, None)
    trade(a3, 11, 25624, 25586, 25680, x1=21, side="long", fs=6.6)
    a3.text(0, 25694, "5-MIN: sweep + engulfing = trigger", color=TXT, fontsize=7.6, va="top")
    a3.set_xticks([])
    _titles(fig, "Ch 19 · Multi-timeframe alignment: daily → 15-min → 5-min",
            "Higher timeframe gives direction and location; lower timeframe gives the trigger")
    fig.subplots_adjust(left=0.02, right=0.93, top=0.88, bottom=0.03)
    save(fig, "c19")


# ---------------------------------------------------------------- ch20
def c20():
    n = 75
    d = gen([(0, 25805), (4, 25792), (6, 25795), (14, 25840), (20, 25868), (30, 25882), (36, 25860), (42, 25852),
             (48, 25875), (54, 25898), (60, 25912), (66, 25900), (74, 25930)], n, noise=4, wick=3, seed=201)
    vw = vwap(d)
    setb(d, 4, o=25800, h=25802, l=25786, c=25796)
    fig, ax, _ = figure(h=4.9)
    candles(ax, d)
    ax.set_xlim(-1, n + 9)
    ax.set_ylim(25680, 25960)
    ax.plot(np.arange(n), vw, color=YEL, lw=1.6, zorder=5)
    ax.text(n + 0.2, vw[-1], "VWAP", color=YEL, fontsize=7.4, fontweight="bold", va="center")
    zone(ax, 25783, 25790, PURPLE, None, alpha=0.5)
    ax.text(12, 25762, "Narrow CPR 25,783-25,790 (BC/TC), P 25,787: trend day likely", color=PURPLE, fontsize=7.4,
            fontweight="bold", va="top")
    level(ax, 25880, "PDH 25,880", ORANGE, side="right")
    level(ax, 25780, "PDC 25,780", WHITE, side="right", ls=":", dy=-9)
    level(ax, 25700, "PDL 25,700", BLUE, side="right")
    step(ax, 4, 25776, 1, UP, "Dip holds CPR + VWAP", tx=6, ty=25728)
    step(ax, 42, 25840, 2, YEL, "VWAP pullback holds:\nlongs defend average", tx=40, ty=25812)
    step(ax, 54, 25912, 3, ORANGE, "PDH 25,880 breaks and\nholds = buy-stops above fuel", tx=40, ty=25945)
    frame(fig, ax, "Ch 20 · VWAP, PDH/PDL/PDC and CPR as reference levels",
          "5-min · Levels from yesterday tell you where the liquidity is today", times(n), step=6)
    save(fig, "c20")


# ---------------------------------------------------------------- ch21 setups
def s1():
    n = 50
    d = gen([(0, 25690), (3, 25668), (5, 25640), (6, 25658), (10, 25672), (16, 25700), (22, 25712), (28, 25730),
             (34, 25722), (40, 25745), (49, 25765)], n, noise=3.5, wick=3, seed=211)
    setb(d, 5, o=25652, h=25655, l=25628, c=25650, v=420)
    setb(d, 6, o=25650, h=25666, l=25648, c=25664, v=330)
    fig, ax, ax2 = figure(lower=True)
    candles(ax, d)
    ax.set_xlim(-1, n + 9)
    ax.set_ylim(25600, 25790)
    volume(ax2, d, highlight=[5])
    level(ax, 25650, "PDL 25,650", BLUE, side="left", dy=-9)
    level(ax, 25730, "PDC 25,730", WHITE, ls=":", side="left", dy=8)
    stops(ax, 0, 4, 25644, None)
    step(ax, 5, 25618, 1, MAG, "09:40 wick to 25,628 sweeps PDL\nwith volume spike", tx=8, ty=25618)
    step(ax, 6, 25676, 2, UP, "Close back above PDL;\nnext candle breaks its high", tx=9, ty=25770)
    trade(ax, 7, 25667, 25626, 25730, x1=n - 1, side="long", tgt2=25760)
    frame(fig, ax, "Setup 1 · PDH/PDL liquidity-sweep reversal (long example)",
          "5-min · Entry above the reclaim candle high; SL below the sweep wick", times(n), step=6, ax2=ax2)
    save(fig, "s1")


def s2():
    n = 48
    d = gen([(0, 25720), (1, 25700), (2, 25732), (3, 25718), (4, 25694), (5, 25688), (7, 25712), (9, 25735),
             (11, 25748), (16, 25765), (24, 25780), (32, 25772), (40, 25800), (47, 25815)], n, noise=3.5, wick=3,
            seed=221)
    setb(d, 0, o=25724, h=25740, l=25716, c=25722, v=300)
    setb(d, 1, o=25722, h=25726, l=25700, c=25705, v=270)
    setb(d, 2, o=25705, h=25735, l=25703, c=25730, v=260)
    setb(d, 4, o=25712, h=25714, l=25686, c=25692, v=160)
    setb(d, 5, o=25692, h=25698, l=25683, c=25696, v=150)
    setb(d, 7, o=25704, h=25720, l=25702, c=25716, v=260)
    setb(d, 8, o=25716, h=25744, l=25714, c=25742, v=340)
    fig, ax, ax2 = figure(lower=True)
    candles(ax, d)
    ax.set_xlim(-1, n + 9)
    ax.set_ylim(25660, 25840)
    volume(ax2, d)
    zone(ax, 25700, 25740, PURPLE, "OR", x0=-0.5, x1=2.5, side="left", alpha=0.25, ty=25747)
    level(ax, 25740, "OR high 25,740", PURPLE, x0=2.5, x1=30, side="right")
    level(ax, 25700, "OR low 25,700", PURPLE, x0=2.5, x1=30, side="right")
    step(ax, 5, 25676, 1, MAG, "ORB shorts sell below 25,700:\nno volume, no follow-through", tx=8, ty=25672)
    step(ax, 7, 25726, 2, YEL, "Back inside OR within 3 candles", tx=11, ty=25712)
    step(ax, 8, 25752, 3, UP, "OR high breaks: trapped shorts cover", tx=11, ty=25822)
    trade(ax, 9, 25744, 25694, 25815, x1=n - 1, side="long")
    frame(fig, ax, "Setup 2 · Failed opening-range breakout (fade)",
          "5-min · Trade the reversal through the OPPOSITE side of the opening range", times(n), step=6, ax2=ax2)
    save(fig, "s2")


def s3():
    n = 54
    d = gen([(0, 25900), (6, 25860), (10, 25878), (16, 25820), (18, 25812), (20, 25836), (24, 25848), (26, 25846),
             (31, 25800), (35, 25782), (40, 25800), (42, 25804), (46, 25770), (53, 25735)], n, noise=3.5, wick=3,
            seed=231)
    setb(d, 10, l=25866, h=25881)
    setb(d, 15, o=25866, h=25868, l=25828, c=25832, v=420)
    setb(d, 24, o=25842, h=25852, l=25840, c=25848, v=120)
    setb(d, 25, o=25848, h=25850, l=25836, c=25838, v=200)
    fig, ax, ax2 = figure(lower=True)
    candles(ax, d)
    ax.set_xlim(-1, n + 9)
    ax.set_ylim(25710, 25930)
    volume(ax2, d, highlight=[15])
    level(ax, 25866, "HL 25,866", MUTED, x0=8, x1=19, side="left", dy=-8)
    ax.text(19.3, 25866, "BOS ↓", color=DN, fontsize=7.6, fontweight="bold", va="center")
    zone(ax, 25840, 25856, DN, None, x0=13.6, x1=n + 8, alpha=0.2)
    ax.text(36, 25848, "Bearish OB / FVG 25,840-25,856", color=DN, fontsize=7.6, fontweight="bold", va="center")
    step(ax, 15, 25822, 1, DN, "Displacement down breaks HL", tx=1, ty=25790)
    step(ax, 24, 25866, 2, YEL, "Pullback into supply\non falling volume", tx=26, ty=25900)
    trade(ax, 26, 25840, 25864, 25785, x1=n - 1, side="short", tgt2=25740)
    frame(fig, ax, "Setup 3 · Break of structure + pullback to order block / FVG",
          "5-min · Continuation trade: join the institution at its own price", times(n, "10:15"), step=6, ax2=ax2)
    save(fig, "s3")


def s4():
    n = 66
    d = gen([(0, 25700), (6, 25748), (12, 25738), (18, 25785), (24, 25768), (30, 25812), (36, 25800), (40, 25790),
             (46, 25830), (54, 25858), (65, 25880)], n, noise=3.5, wick=3, seed=241)
    vw = vwap(d)
    i = 40
    setb(d, i, o=vw[i] + 2, h=vw[i] + 4, l=vw[i] - 6, c=vw[i] + 1)
    setb(d, i + 1, o=vw[i] + 1, h=vw[i] + 18, l=vw[i] - 1, c=vw[i] + 16, v=300)
    vw = vwap(d)
    fig, ax, ax2 = figure(lower=True)
    candles(ax, d)
    ax.set_xlim(-1, n + 9)
    ax.set_ylim(25670, 25905)
    volume(ax2, d)
    ax.plot(np.arange(n), vw, color=YEL, lw=1.6, zorder=5)
    ax.text(n + 0.2, vw[-1], "VWAP", color=YEL, fontsize=7.4, fontweight="bold", va="center")
    step(ax, 12, vw[12] - 12, 1, MUTED, "Touch 1 of VWAP holds", tx=14, ty=25700)
    step(ax, i, vw[i] - 14, 2, YEL, "Touch 2: bullish engulfing at VWAP\n= entry trigger", tx=43, ty=25740)
    entry = d["c"][i + 1]
    trade(ax, i + 1, round(entry), round(d["l"][i] - 6), round(entry + 2 * (entry - d["l"][i] + 6)), x1=n - 1,
          side="long")
    frame(fig, ax, "Setup 4 · VWAP pullback on a trend day",
          "5-min · Higher highs above a rising VWAP. Buy the pullback, not the breakout", times(n), step=6, ax2=ax2)
    save(fig, "s4")


def s5():
    n = 60
    d = gen([(0, 25930), (6, 25965), (10, 25992), (12, 26012), (14, 25985), (20, 25962), (28, 25975), (34, 25950),
             (42, 25968), (50, 25945), (59, 25952)], n, noise=4, wick=3, seed=251)
    setb(d, 12, o=25994, h=26022, l=25992, c=25996, v=420)
    setb(d, 13, o=25996, h=25998, l=25976, c=25980, v=320)
    fig, ax, ax2 = figure(lower=True)
    candles(ax, d)
    ax.set_xlim(-1, n + 11)
    ax.set_ylim(25900, 26160)
    volume(ax2, d, highlight=[12])
    level(ax, 26000, "Round no. 26,000 + PDH 25,995", YEL, ls="-.", side="left", dy=-9)
    zone(ax, 26100, 26110, DN, "SELL 26,100 CE (above sweep + OI wall)", x0=14, side="left", alpha=0.45, ty=26118)
    zone(ax, 26300, 26310, UP, None, x0=14, alpha=0.4)
    level(ax, 26022, "Sweep high 26,022 = invalidation", MAG, x0=12, side="right")
    step(ax, 12, 26036, 1, MAG, "10:15 sweep of 26,000 / PDH,\nwick rejection", tx=1, ty=26080)
    step(ax, 14, 25970, 2, DN, "Next candle closes below 25,995", tx=17, ty=25915)
    ax.text(15, 26146, "Hedge: buy 26,300 CE (bear call spread, max loss defined)", color=UP, fontsize=7.3,
            fontweight="bold")
    frame(fig, ax, "Setup 5 · Expiry-day round-number rejection (option-seller version)",
          "5-min, expiry Tuesday · Spot SL = 15-min close above 26,022. Exit the spread by 14:45 regardless",
          times(n), step=6, ax2=ax2)
    save(fig, "s5")


# ---------------------------------------------------------------- ch22
def c22a():
    n = 50
    d = gen([(0, 25940), (6, 25985), (10, 26015), (11, 26040), (13, 26000), (20, 25975), (28, 25990), (36, 25960),
             (44, 25975), (49, 25965)], n, noise=4, wick=3, seed=261)
    setb(d, 11, o=26018, h=26044, l=26012, c=26020, v=380)
    fig, ax, _ = figure(h=4.9)
    candles(ax, d)
    ax.set_xlim(-1, n + 10)
    ax.set_ylim(25880, 26260)
    zone(ax, 25905, 26085, AMBER, None, alpha=0.04)
    ax.text(1, 26080, "Today's expected range (VIX 1-SD ≈ ±90 from 25,995): NEVER sell strikes inside it",
            color=AMBER, fontsize=7.4, fontweight="bold")
    level(ax, 26044, "Swept high 26,044", MAG, side="right")
    level(ax, 26100, "Round no. + call OI wall 26,100", YEL, ls="-.", side="left", dy=8)
    zone(ax, 26145, 26155, DN, "SELL 26,150 CE", x0=12, side="right", alpha=0.6, ty=26165)
    zone(ax, 26245, 26255, UP, "BUY 26,350 CE hedge (off-chart)", x0=12, side="right", alpha=0.0, ty=26240)
    level(ax, 26000, None, MUTED, ls=":")
    note(ax, "Strike = beyond the liquidity that was\nalready swept + beyond the OI wall +\noutside the expected range",
         (12, 26150), (14, 26205), ec=DN)
    frame(fig, ax, "Ch 22 · Strike selection: sell where price must work hardest to reach",
          "5-min · Bear call spread 26,150/26,350 after a sweep-and-reject at 26,044", times(n, "09:30"), step=6)
    save(fig, "c22a")


def c22b():
    d, p, iv, *_ = expiry_series()
    n = d["n"]
    entry_i, entry = 17, 51.0
    sl = [np.nan] * n
    cur, low, exit_i = 66.0, entry, None
    for i in range(entry_i, n):
        if exit_i is None:
            low = min(low, p["l"][i])
            if (entry - low) / entry >= 0.40:
                cur = min(cur, low + (entry - low) / 2)
            sl[i] = cur
            if i > entry_i and p["h"][i] >= cur:
                exit_i = i
    fig, ax, _ = figure(h=4.6)
    ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: f"{v:.0f}"))
    candles(ax, p)
    ax.set_xlim(-1, n + 9)
    ax.set_ylim(0, 100)
    ax.plot(np.arange(n), sl, color=DN, lw=1.6, drawstyle="steps-post", zorder=6)
    ax.plot([entry_i, n], [entry, entry], color=BLUE, lw=1)
    ax.text(n + 0.4, entry, "SOLD 51", color=BLUE, fontsize=7.4, fontweight="bold", va="center")
    step(ax, entry_i, 60, 1, DN, "Initial SL 66\n(premium +30%)", tx=1, ty=80)
    lowi = int(np.nanargmin(p["l"][:exit_i]))
    step(ax, 47, 22, 2, UP, f"40% captured → trail: SL = low + half\nthe open profit (≈{sl[exit_i]:.1f})",
         tx=20, ty=14)
    step(ax, exit_i, sl[exit_i] + 8, 3, YEL, f"{times(n)[exit_i]} trailing SL hit at {sl[exit_i]:.1f}:\n"
         f"+{entry - sl[exit_i]:.1f} pts x 130 qty = +₹{(entry - sl[exit_i]) * 130:,.0f}", tx=36, ty=72)
    vline(ax, 66, "14:45 hard exit\n(if still open)", YEL, ls="--", y=97, ha="right", lw=1.2)
    note(ax, "Without the trail: 79 by 15:15", (72, 79), (40, 90), ec=DN)
    frame(fig, ax, "Ch 22 · Managing the short: trail, and never hold past the cutoff",
          "5-min, same expiry-day path as Ch 10 · 2 lots x 65 = 130 qty", times(n), step=6)
    save(fig, "c22b")


# ---------------------------------------------------------------- ch23
def c23a():
    rng = np.random.default_rng(14)
    N = 150
    r = np.where(rng.random(N) < 0.45, 1.4, -1.0)
    r[40:47] = -1.0
    curves = {}
    for f in (0.01, 0.02, 0.10):
        eq = [270000.0]
        for x in r:
            eq.append(eq[-1] * (1 + f * x))
        curves[f] = np.array(eq)
    fig, ax = plt.subplots(figsize=(10, 4.4))
    _style(ax)
    for f, col in ((0.01, UP), (0.02, BLUE), (0.10, DN)):
        ax.plot(curves[f], color=col, lw=1.8, label=f"{f * 100:.0f}% risk per trade")
    ax.axhline(270000, color=MUTED, ls=":", lw=1)
    ax.axvspan(39.5, 46.5, color=DN, alpha=0.1)
    dd10 = 1 - curves[0.10][47] / curves[0.10][40]
    dd1 = 1 - curves[0.01][47] / curves[0.01][40]
    ax.annotate(f"7 losses in a row:\n1% risk → -{dd1 * 100:.1f}%\n10% risk → -{dd10 * 100:.0f}%",
                xy=(46, curves[0.10][47]), xytext=(96, 150000), fontsize=7.8,
                bbox=dict(boxstyle="round,pad=0.3", fc=BG, ec=DN), arrowprops=dict(arrowstyle="->", color=DN))
    for f, col in ((0.01, UP), (0.02, BLUE), (0.10, DN)):
        v = curves[f][-1]
        v += {0.01: -9000, 0.02: 7000}.get(f, 0)
        ax.text(N + 2, v, f"{f * 100:.0f}%: ₹{curves[f][-1] / 1e5:.2f}L", color=col, fontsize=7.4, fontweight="bold", va="center")
    ax.set_xlim(-5, N + 22)
    ax.legend(loc="lower left")
    ax.set_xlabel("Trade number", fontsize=8)
    _titles(fig, "Ch 23 · Same trades, different risk: why 1% survives",
            "Identical 150 trades from a small-edge system (45% win rate, +1.4R / -1R, illustrative). Start ₹2,70,000",
            "Illustrative simulation")
    fig.subplots_adjust(left=0.02, right=0.9, top=0.86, bottom=0.11)
    save(fig, "c23a")


def c23b():
    n = 40
    d = gen([(0, 38), (6, 46), (12, 55), (18, 62), (24, 72), (30, 84), (36, 92), (39, 96)], n, noise=1.5, wick=1.5,
            seed=231)
    fig, ax, _ = figure(h=4.4)
    ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: f"{v:.0f}"))
    candles(ax, d)
    ax.set_xlim(-1, n + 12)
    ax.set_ylim(20, 110)
    adds = [(0, 40, 1), (12, 55, 1), (24, 72, 2), (32, 86, 2)]
    lots, cost = 0, 0
    for k, (i, px, l_) in enumerate(adds, 1):
        lots += l_
        cost += px * l_
        avg = cost / lots
        step(ax, i, px - 7, k, YEL, f"Sell {l_} lot @ {px}\navg {avg:.1f}, total {lots} lot" + ("s" if lots > 1 else ""), tx=i + 1.5,
             ty=px - 18 if k < 4 else px - 32)
    loss = (d["c"][-1] - cost / lots) * lots * 65
    ax.plot([0, n + 1], [cost / lots] * 2, color=AMBER, ls="--", lw=1.2)
    ax.text(n + 1.3, cost / lots, f"Final avg {cost / lots:.1f}", color=AMBER, fontsize=7.4, va="center",
            fontweight="bold")
    ax.text(n + 1.3, d["c"][-1], f"Now {d['c'][-1]:.0f}\nloss ₹{loss:,.0f}", color=DN, fontsize=7.4, va="center",
            fontweight="bold")
    note(ax, "Plan was 1 lot with SL 52 (₹780 risk).\nAveraging turned it into 6 lots and a\n"
             "loss ~14x bigger than planned.", (12, 55), (1, 95), ec=DN)
    frame(fig, ax, "Ch 23 · Averaging a losing short: how ₹780 of risk becomes ₹10,700",
          "Short CE premium, 5-min · Each add lowers nothing; it multiplies exposure in the wrong direction",
          times(n, "11:00"), step=6)
    save(fig, "c23b")


# ---------------------------------------------------------------- ch24
def c24a():
    trades = [("10:05\n1 lot, plan", -1300, "Calm"), ("10:20\n2 lots, 'get it back'", -2600, "Angry"),
              ("10:40\n4 lots, no SL", -7800, "Revenge"), ("11:30\n2 lots, win", 2100, "Relief"),
              ("12:10\n6 lots, all-in", -14900, "Tilt"), ("14:50\n8 lots, expiry", -26000, "Desperate")]
    fig, ax = plt.subplots(figsize=(10, 4.4))
    _style(ax)
    x = np.arange(len(trades))
    pnl = np.array([t[1] for t in trades])
    ax.bar(x, pnl, color=[UP if v > 0 else DN for v in pnl], width=0.55)
    cum = np.cumsum(pnl)
    ax.plot(x, cum, color=YEL, marker="o", lw=1.8, label="Cumulative P&L")
    ax.axhline(-5400, color=AMBER, ls="--", lw=1.3)
    ax.text(-0.4, -5400 - 900, "Daily limit -₹5,400: should have\nstopped after trade 3", color=AMBER, fontsize=7.4,
            ha="left", va="top", fontweight="bold")
    for i, (lab, v, emo) in enumerate(trades):
        ax.text(i, 3600, f"{emo}\n{'+' if v > 0 else '-'}₹{abs(v):,.0f}", ha="center", va="bottom", fontsize=7.4,
                color=UP if v > 0 else DN, fontweight="bold")
    ax.set_xticks(x)
    ax.set_xticklabels([t[0] for t in trades], fontsize=7.2)
    ax.set_ylim(-62000, 11500)
    ax.legend(loc="lower left")
    _titles(fig, "Ch 24 · Anatomy of a tilt day: size grows as discipline shrinks",
            f"Illustrative day on ₹2.7 lakh · Total {cum[-1]:,.0f} = {cum[-1] / 270000 * 100:.0f}% of capital in "
            "one session", "Illustrative")
    fig.subplots_adjust(left=0.02, right=0.9, top=0.86, bottom=0.14)
    save(fig, "c24a")


def c24b():
    dd = np.array([5, 10, 20, 30, 40, 46, 50, 60])
    need = dd / (100 - dd) * 100
    fig, ax = plt.subplots(figsize=(10, 3.9))
    _style(ax)
    ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: f"{v:.0f}%"))
    cols = [UP if v < 25 else (AMBER if v < 60 else DN) for v in need]
    x = np.arange(len(dd))
    ax.bar(x, need, color=cols, width=0.55)
    for i, v in enumerate(need):
        ax.text(i, v + 3, f"+{v:.0f}%", ha="center", fontsize=8, color=TXT, fontweight="bold")
    ax.set_xticks(x)
    ax.set_xticklabels([f"-{v}%" + (" (you)" if v == 46 else "") for v in dd], fontsize=8)
    ax.set_xlabel("Drawdown", fontsize=8)
    ax.set_ylim(0, 170)
    _titles(fig, "Ch 24 · The math of recovery: gain needed to get back to the peak",
            "Required gain = DD ÷ (1 − DD). From ₹5 lakh to ₹2.7 lakh needs +85%", "Arithmetic")
    fig.subplots_adjust(left=0.02, right=0.93, top=0.84, bottom=0.14)
    save(fig, "c24b")


# ---------------------------------------------------------------- ch25
def c25():
    n = 75
    d = gen([(0, 25800), (2, 25830), (4, 25790), (8, 25815), (18, 25860), (26, 25850), (36, 25858), (44, 25845),
             (52, 25870), (60, 25890), (66, 25880), (70, 25920), (74, 25900)], n, noise=5, wick=4, seed=271)
    fig, ax, _ = figure(h=4.6)
    candles(ax, d)
    ax.set_xlim(-1, n + 1)
    ax.set_ylim(25740, 25990)
    blocks = [(-0.5, 2.5, PURPLE, "09:15-09:30\nOBSERVE\nno trades"), (2.5, 27.5, UP, "09:30-11:30\nPRIME WINDOW\nA+ setups 1-3"),
              (27.5, 51.5, MUTED, "11:30-13:30\nLUNCH CHOP\nhalf size or none"),
              (51.5, 66.5, BLUE, "13:30-14:45\n2nd WINDOW\nsetups 4-5"),
              (66.5, 74.5, DN, "14:45-15:30\nEXPIRY: FLAT\nno new trades")]
    for a, b, col, t in blocks:
        ax.axvspan(a, b, color=col, alpha=0.1)
        ax.text((a + b) / 2, 25984, t, ha="center", va="top", fontsize=7.2, color=col if col != MUTED else TXT,
                fontweight="bold")
    frame(fig, ax, "Ch 25 · The trading day as time zones",
          "5-min · Your edge is not equally available all day. Trade the windows, protect the rest", times(n),
          step=6)
    save(fig, "c25")


# ---------------------------------------------------------------- ch26
def c26():
    fig, axs = plt.subplots(3, 4, figsize=(10, 6.2), gridspec_kw={"hspace": 0.42, "wspace": 0.1})
    S = {
        "1 Bull trap": ([0, 3, 2, 3.2, 4.2, 2.5, 1], (3.6, 4.4), DN),
        "2 Bear trap": ([4, 1, 2, 0.8, -0.2, 1.5, 3], (0.4, -0.4), UP),
        "3 SL hunt below support": ([3, 1, 2, 1, 2, 1, -0.5, 2, 3.5], (1, 1), UP),
        "4 Gap-up trap": ([1, 1.2, None, 4, 4.4, 3.2, 2, 1.2], (1.2, 1.2), DN),
        "5 Opening-range fake": ([2, 2.6, 1.8, 3.2, 2.4, 1.2, 0.4], (2.6, 1.8), DN),
        "6 Round-number pin": ([1, 2.1, 1.7, 2.5, 1.5, 2.4, 1.9, 2.05], (2, 2), YEL),
        "7 Expiry gamma spike": ([3, 2.4, 1.8, 1.4, 1.3, 1.6, 2.6, 4.2], (3, 3), DN),
        "8 Event whipsaw": ([2, 2.1, 1.9, 4, 0.5, 1.5, 1.2], (2, 2), MAG),
        "9 Pattern (triangle) fake": ([0, 3.5, 1, 3, 1.6, 2.6, 3.3, 1.2, 0], (2.6, 2.6), DN),
        "10 Demand zone (OB)": ([3, 1, 0.8, 3.5, 4, 1.2, 3.6, 4.6], (1, 1), UP),
        "11 Fair value gap": ([0.5, 0.8, 3.2, 3.6, 2.2, 3.8, 4.4], (1.2, 2.6), UP),
        "12 Wyckoff spring": ([4, 1.2, 2.6, 1.4, 2.4, 0.6, 1.8, 2.8, 4], (1.2, 2.6), UP),
    }
    for a, (t, (ys, zone_y, col)) in zip(axs.flat, S.items()):
        a.set_facecolor(PANEL)
        xs = [i for i, y in enumerate(ys) if y is not None]
        yy = [y for y in ys if y is not None]
        if None in ys:
            k = ys.index(None)
            a.plot(range(k), ys[:k], color=TXT, lw=1.8)
            a.plot(range(k + 1, len(ys)), ys[k + 1:], color=TXT, lw=1.8)
        else:
            a.plot(xs, yy, color=TXT, lw=1.8)
        lo, hi = sorted(zone_y)
        a.axhspan(lo - 0.12, hi + 0.12, color=col, alpha=0.22)
        a.annotate("", xy=(len(ys) - 1, yy[-1]), xytext=(len(ys) - 2, yy[-2]),
                   arrowprops=dict(arrowstyle="->", color=col, lw=2))
        a.set_title(t, fontsize=8, color=col if col != YEL else YEL, fontweight="bold", pad=3)
        a.set_xticks([])
        a.set_yticks([])
        a.set_ylim(-1, 5)
        a.grid(False)
    _titles(fig, "Ch 26 · Cheat-sheet thumbnails: the 12 shapes to recognise", None, "Schematic")
    fig.subplots_adjust(left=0.01, right=0.99, top=0.9, bottom=0.02)
    save(fig, "c26")


ALL = [c14, c15, c16, c17, c18a, c18b, c19, c20, s1, s2, s3, s4, s5, c22a, c22b, c23a, c23b, c24a, c24b, c25, c26]

if __name__ == "__main__":
    import sys
    sel = sys.argv[1:]
    for f in ALL:
        if not sel or f.__name__ in sel:
            f()
            print("ok", f.__name__)
