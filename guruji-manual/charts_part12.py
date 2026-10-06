"""Charts for Part 1 (ch 1-4) and Part 2 (ch 5-13)."""
import numpy as np

from charts_engine import (AMBER, BLUE, CYAN, DN, MAG, MUTED, ORANGE, PURPLE, UP, WHITE, YEL, GRID, PANEL, TXT,
                           bs_call, candles, figure, frame, gen, level, note, save, setb, step, stops, times,
                           tline, trade, vline, volume, vwap, zone, H2)


def day_ticks(ax, n, per, names):
    ticks, labs = [], []
    for k, nm in enumerate(names):
        for off, t in ((0, f"{nm} 09:15"), (12, "12:15")):
            if k * per + off < n:
                ticks.append(k * per + off)
                labs.append(t)
    ax.set_xticks(ticks)
    ax.set_xticklabels(labs, fontsize=7.5)
    for k in range(1, len(names)):
        ax.axvline(k * per - 0.5, color=GRID, lw=1.2)


# ---------------------------------------------------------------- ch1
def c01():
    n = 75
    d = gen([(0, 25780), (3, 25805), (5, 25768), (8, 25790), (12, 25800), (22, 25850), (30, 25842), (38, 25898),
             (44, 25890), (52, 25905), (58, 25895), (62, 25912), (66, 25932), (68, 25935), (72, 25872), (74, 25860)],
            n, noise=5, wick=4, seed=11)
    d["v"][1:7] *= 1.8
    d["v"][12:38] *= 1.4
    d["v"][62:68] *= 1.6
    d["v"][68:74] *= 2.2
    fig, ax, ax2 = figure(lower=True)
    candles(ax, d)
    ax.set_xlim(-1, n + 1)
    ax.set_ylim(25735, 25985)
    volume(ax2, d)
    zone(ax, 25735, 25985, x0=-1, x1=8.5, color=PURPLE, alpha=0.09)
    zone(ax, 25735, 25985, x0=11.5, x1=38.5, color=UP, alpha=0.06)
    zone(ax, 25735, 25985, x0=40, x1=61, color=AMBER, alpha=0.06)
    zone(ax, 25735, 25985, x0=63, x1=75, color=DN, alpha=0.07)
    level(ax, 25900, "25,900 CE/PE: heaviest OI", AMBER, x0=40, x1=61, side="left", dy=-24)
    step(ax, 4, 25822, 1, PURPLE, "Algos & prop desks\nfight at the open", tx=1, ty=25960)
    step(ax, 24, 25858, 2, UP, "FII flow: steady trend,\nshallow pullbacks", tx=14, ty=25945)
    step(ax, 50, 25918, 3, AMBER, "Writers pin the\nstrike, theta decays", tx=37, ty=25968)
    step(ax, 66, 25945, 4, YEL, "Retail buys the\n'breakout' at 14:45", tx=52, ty=25968)
    step(ax, 72, 25865, 5, DN, "Reversal: retail longs\n= exit liquidity", tx=60, ty=25800)
    frame(fig, ax, "Ch 1 · Who moves NIFTY: one session, five players",
          "5-min · Each shaded phase is dominated by a different participant", times(n), step=6, ax2=ax2)
    save(fig, "c01")


# ---------------------------------------------------------------- ch2
def c02():
    n = 60
    d = gen([(0, 25935), (3, 25958), (6, 25928), (12, 25975), (16, 25945), (22, 25988), (27, 25952), (33, 25989),
             (38, 25960), (44, 25972), (48, 25948), (53, 25968), (59, 25962)], n, noise=4, wick=3.5, seed=21)
    setb(d, 22, h=25991.5)
    setb(d, 33, h=25991)
    setb(d, 2, l=25924, h=25962)
    fig, ax, _ = figure(h=4.9)
    candles(ax, d)
    ax.set_xlim(-1, n + 9)
    ax.set_ylim(25880, 26060)
    zone(ax, 25992, 26035, AMBER, "BUY-STOP LIQUIDITY: shorts' SL + breakout buy orders", side="left", ty=26026)
    level(ax, 26020, "PDH 26,020", ORANGE)
    level(ax, 26000, "Round no. 26,000", YEL, ls="-.")
    level(ax, 25991, "Equal highs 25,991", AMBER, ls=":", x0=20, side="right", dy=-6)
    zone(ax, 25922, 25962, PURPLE, None, x0=-1, x1=3.5, alpha=0.22)
    ax.text(-0.6, 25966, "Opening range", color=PURPLE, fontsize=7.2, fontweight="bold")
    tline(ax, 6, 25926, 48, 25944, CYAN, "Rising trendline", ext=10)
    zone(ax, 25885, 25922, BLUE, "SELL-STOP LIQUIDITY: longs' SL below OR low / trendline / PDL", side="left",
         ty=25895)
    level(ax, 25905, "PDL 25,905", BLUE, x0=40)
    stops(ax, 21, 34, 25998, None, MAG)
    stops(ax, 0, 5, 25915, None, MAG)
    note(ax, "Every obvious level = a pool of orders.\nOperators need these orders to fill size.",
         (33, 25991), (37, 25995 - 75), color=TXT, ec=AMBER)
    frame(fig, ax, "Ch 2 · Liquidity map: where the orders sit",
          "5-min · Pink x = clusters of retail stop-losses. Price is drawn to these pools like a magnet.",
          times(n), step=6)
    save(fig, "c02")


# ---------------------------------------------------------------- ch3
def c03():
    n = 50
    d = gen([(0, 25840), (4, 25812), (8, 25838), (12, 25811), (16, 25832), (19, 25845), (21, 25856), (24, 25832),
             (27, 25818), (29, 25806), (30, 25815), (34, 25850), (37, 25872), (42, 25885), (49, 25905)],
            n, noise=4, wick=3, seed=31)
    setb(d, 4, l=25810)
    setb(d, 12, l=25810.5)
    setb(d, 21, o=25846, h=25859, l=25844, c=25857, v=150)
    setb(d, 29, o=25812, h=25814, l=25788, c=25809, v=420)
    setb(d, 30, o=25809, h=25828, l=25806, c=25826, v=330)
    setb(d, 31, o=25826, h=25846, l=25824, c=25844, v=300)
    setb(d, 32, o=25844, h=25858, l=25841, c=25855, v=260)
    fig, ax, ax2 = figure(lower=True)
    candles(ax, d)
    ax.set_xlim(-1, n + 1)
    ax.set_ylim(25770, 25920)
    volume(ax2, d, highlight=[29])
    level(ax, 25810, None, BLUE, x0=0, x1=30)
    stops(ax, 2, 15, 25803, "Equal lows 25,810: sell-stop pool", color=BLUE, side="right")
    level(ax, 25848, "Minor high", MUTED, x0=14, x1=24, side="left", dy=6)
    step(ax, 8, 25796, 1, BLUE, "Liquidity builds:\nlongs keep SL at 25,800", tx=3, ty=25782)
    step(ax, 21, 25861, 2, YEL, "INDUCEMENT: small break up\npulls in breakout buyers", tx=10, ty=25898)
    step(ax, 29, 25786, 3, MAG, "SWEEP: wick to 25,788 fires\nall stops; operators BUY them", tx=33, ty=25784)
    step(ax, 33, 25872, 4, UP, "Displacement up:\nthe real move starts", tx=36, ty=25830)
    frame(fig, ax, "Ch 3 · Inducement → sweep → displacement",
          "5-min · Liquidity is first created (stops pile up), then harvested (swept), then price moves",
          times(n), step=6, ax2=ax2)
    save(fig, "c03")


# ---------------------------------------------------------------- ch4
def c04():
    n = 64
    way = [(0, 25600), (5, 25668), (9, 25635), (15, 25712), (19, 25682), (25, 25760), (29, 25730), (34, 25790),
           (38, 25748), (43, 25772), (48, 25715), (52, 25742), (57, 25680), (60, 25700), (63, 25650)]
    d = gen(way, n, noise=5, wick=4, seed=41)
    fig, ax, _ = figure(h=4.9)
    candles(ax, d)
    ax.set_xlim(-1, n + 1)
    ax.set_ylim(25570, 25830)
    labs = {5: "HH", 9: "HL", 15: "HH", 19: "HL", 25: "HH", 29: "HL", 34: "HH", 38: "HL", 43: "LH", 48: "LL",
            52: "LH", 57: "LL"}
    for i, t in labs.items():
        hi = t in ("HH", "LH")
        y = d["h"][i] + 9 if hi else d["l"][i] - 9
        ax.text(i, y, t, color=UP if t in ("HH", "HL") else DN, fontsize=8, fontweight="bold", ha="center",
                va="bottom" if hi else "top", zorder=8)
    for a, b in ((5, 13), (15, 23), (25, 33)):
        y = d["h"][a]
        ax.plot([a, b], [y, y], color=UP, lw=1, ls="--")
        ax.text(b + 0.3, y + 2, "BOS", color=UP, fontsize=7.3, fontweight="bold", va="bottom")
    y = d["l"][38]
    ax.plot([38, 47], [y, y], color=YEL, lw=1.3, ls="--")
    ax.text(47.3, y - 1, "CHoCH", color=YEL, fontsize=8, fontweight="bold", va="top")
    y = d["l"][48]
    ax.plot([48, 56], [y, y], color=DN, lw=1, ls="--")
    ax.text(56.3, y - 2, "BOS", color=DN, fontsize=7.3, fontweight="bold", va="top")
    note(ax, "External (major) structure: swing points\nthat broke a prior swing. Small wiggles\n"
             "between them = internal structure.", (25, d["h"][25]), (1, 25790), ec=CYAN)
    note(ax, "CHoCH: first break of the last HL.\nUptrend is in doubt → stop buying dips.",
         (47, d["l"][38]), (50, 25790), ec=YEL)
    frame(fig, ax, "Ch 4 · Market structure: HH/HL, BOS and CHoCH",
          "15-min, three sessions · Uptrend = HH + HL; BOS confirms continuation; CHoCH warns of reversal")
    day_ticks(ax, n, 25, ["Wed", "Thu", "Fri"])
    save(fig, "c04")


# ---------------------------------------------------------------- ch5
def c05a():
    n = 50
    d = gen([(0, 25880), (6, 25945), (10, 25905), (16, 25948), (21, 25912), (27, 25940), (30, 25950),
             (34, 25945), (37, 25915), (42, 25890), (49, 25878)], n, noise=4, wick=3, seed=51)
    setb(d, 6, h=25951)
    setb(d, 16, h=25952)
    setb(d, 31, o=25949, h=25978, l=25947, c=25973, v=90)
    setb(d, 32, o=25973, h=25981, l=25958, c=25962, v=80)
    setb(d, 33, o=25962, h=25964, l=25934, c=25937, v=260)
    setb(d, 34, o=25937, h=25941, l=25915, c=25919, v=300)
    fig, ax, ax2 = figure(lower=True)
    candles(ax, d)
    ax.set_xlim(-1, n + 9)
    ax.set_ylim(25850, 26005)
    volume(ax2, d, highlight=[31, 33])
    zone(ax, 25945, 25955, AMBER, "Resistance 25,950", x1=31, side="left")
    step(ax, 11, 25951, 1, AMBER, "Two rejections:\nlevel is obvious", tx=6, ty=25990)
    step(ax, 31, 25984, 2, YEL, "Breakout on LOW volume:\nretail buys 25,970", tx=18, ty=25992)
    step(ax, 33, 25930, 3, DN, "Close back inside\n= trap confirmed", tx=35, ty=25985)
    step(ax, 36, 25905, 4, MAG, "Trapped longs' SL\n= fuel for the fall", tx=38, ty=25866)
    trade(ax, 34, 25937, 25985, 25880, x1=n - 1, side="short")
    frame(fig, ax, "Ch 5 · Bull trap: false breakout above resistance",
          "5-min · Breakout candle had less volume than the rejection candles: no institutional participation",
          times(n), step=6, ax2=ax2)
    save(fig, "c05a")


def c05b():
    n = 50
    d = gen([(0, 25790), (6, 25705), (11, 25745), (16, 25702), (22, 25740), (28, 25708), (31, 25700),
             (34, 25725), (38, 25750), (44, 25778), (49, 25790)], n, noise=4, wick=3, seed=52)
    setb(d, 6, l=25699)
    setb(d, 16, l=25698)
    setb(d, 31, o=25702, h=25704, l=25676, c=25681, v=95)
    setb(d, 32, o=25681, h=25690, l=25672, c=25688, v=110)
    setb(d, 33, o=25688, h=25716, l=25686, c=25713, v=280)
    setb(d, 34, o=25713, h=25729, l=25710, c=25726, v=260)
    fig, ax, ax2 = figure(lower=True)
    candles(ax, d)
    ax.set_xlim(-1, n + 9)
    ax.set_ylim(25645, 25810)
    volume(ax2, d, highlight=[31, 33])
    zone(ax, 25695, 25705, BLUE, "Support 25,700", x1=31, side="left", ty=25690)
    step(ax, 31, 25668, 1, YEL, "Breakdown on weak volume:\nretail shorts / buys PE", tx=17, ty=25658)
    step(ax, 33, 25722, 2, UP, "Close back above 25,700\n= bear trap", tx=20, ty=25792)
    step(ax, 36, 25740, 3, MAG, "Short covering\n(shorts' SL) fuels rally", tx=40, ty=25690)
    trade(ax, 34, 25726, 25668, 25785, x1=n - 1, side="long")
    frame(fig, ax, "Ch 5 · Bear trap: false breakdown below support",
          "5-min · Mirror image of the bull trap. The reclaim candle has 3x the volume of the breakdown",
          times(n), step=6, ax2=ax2)
    save(fig, "c05b")


# ---------------------------------------------------------------- ch6
def c06a():
    n = 46
    d = gen([(0, 25690), (5, 25603), (10, 25650), (15, 25604), (20, 25660), (25, 25606), (28, 25625),
             (30, 25610), (34, 25640), (39, 25680), (45, 25705)], n, noise=4, wick=3, seed=61)
    for i in (5, 15, 25):
        setb(d, i, l=25600 + (i % 3))
    setb(d, 30, o=25612, h=25616, l=25563, c=25611, v=460)
    setb(d, 31, o=25611, h=25632, l=25608, c=25629, v=310)
    fig, ax, ax2 = figure(lower=True)
    candles(ax, d)
    ax.set_xlim(-1, n + 9)
    ax.set_ylim(25535, 25725)
    volume(ax2, d, highlight=[30])
    zone(ax, 25596, 25606, BLUE, "Support 25,600 (3 touches)", x1=30, side="left", ty=25615)
    stops(ax, 1, 28, 25588, None)
    ax.text(1, 25577, "Retail SL here: 25,580-25,590", color=MAG, fontsize=7.4, fontweight="bold")
    step(ax, 30, 25557, 1, MAG, "Stop hunt: wick to 25,563,\nvolume spike = stops filled", tx=8, ty=25550)
    step(ax, 31, 25640, 2, UP, "Close back above support", tx=21, ty=25700)
    trade(ax, 32, 25628, 25558, 25700, x1=n - 1, side="long")
    frame(fig, ax, "Ch 6 · Stop-loss hunt below support",
          "5-min · Big players buy from the sellers created by triggered stop-losses",
          times(n, "11:00"), step=6, ax2=ax2)
    save(fig, "c06a")


def c06b():
    n = 46
    d = gen([(0, 25980), (5, 26046), (10, 26010), (15, 26047), (20, 26005), (25, 26045), (28, 26030),
             (30, 26040), (34, 26012), (39, 25985), (45, 25965)], n, noise=4, wick=3, seed=62)
    for i in (5, 15, 25):
        setb(d, i, h=26050 - (i % 3))
    setb(d, 30, o=26040, h=26086, l=26036, c=26039, v=440)
    setb(d, 31, o=26039, h=26042, l=26018, c=26021, v=300)
    fig, ax, ax2 = figure(lower=True)
    candles(ax, d)
    ax.set_xlim(-1, n + 9)
    ax.set_ylim(25935, 26115)
    volume(ax2, d, highlight=[30])
    zone(ax, 26044, 26054, AMBER, "Resistance 26,050", x1=30, side="left", ty=26037)
    stops(ax, 1, 28, 26062, None)
    ax.text(1, 26073, "Short sellers' SL + breakout buy orders 26,060-26,070", color=MAG, fontsize=7.4, fontweight="bold")
    step(ax, 30, 26093, 1, MAG, "Wick to 26,086 sweeps the\nbuy-stops; closes back below", tx=6, ty=26100)
    step(ax, 31, 26012, 2, DN, "Confirmation: red close", tx=21, ty=25965)
    trade(ax, 32, 26021, 26090, 25960, x1=n - 1, side="short")
    frame(fig, ax, "Ch 6 · Stop hunt above resistance",
          "5-min · Shorts' stop-loss orders are buy orders: they give sellers liquidity at the top",
          times(n, "11:30"), step=6, ax2=ax2)
    save(fig, "c06b")


# ---------------------------------------------------------------- ch7
def _gap(prev_way, prev_n, day_way, day_n, seed):
    a = gen(prev_way, prev_n, noise=4, wick=3, seed=seed)
    b = gen(day_way, day_n, noise=5, wick=4, seed=seed + 1)
    d = {k: np.concatenate([a[k], b[k]]) for k in ("o", "h", "l", "c", "v")}
    d["n"] = prev_n + day_n
    return d


def c07a():
    pn, dn = 12, 40
    d = _gap([(0, 25690), (6, 25712), (11, 25700)], pn,
             [(0, 25845), (2, 25866), (4, 25850), (6, 25820), (10, 25805), (16, 25790), (24, 25748), (32, 25712),
              (39, 25700)], dn, 71)
    setb(d, pn, o=25838, h=25858, l=25834, c=25852, v=230, link=True)
    setb(d, pn + 1, o=25852, h=25871, l=25848, c=25866, v=190)
    setb(d, pn + 2, o=25866, h=25868, l=25838, c=25842, v=210)
    fig, ax, ax2 = figure(lower=True)
    candles(ax, d)
    n = d["n"]
    ax.set_xlim(-1, n + 9)
    ax.set_ylim(25660, 25900)
    volume(ax2, d)
    vline(ax, pn - 0.5, "Next day 09:15", MUTED, y=25895)
    level(ax, 25700, "PDC 25,700", WHITE, x0=-1, side="left", dy=-9)
    zone(ax, 25700, 25838, AMBER, "GAP +138 pts", x0=pn - 0.5, x1=n + 8, side="right", alpha=0.07, ty=25770)
    zone(ax, 25834, 25871, PURPLE, None, x0=pn - 0.4, x1=pn + 2.4, alpha=0.25)
    step(ax, pn + 1, 25880, 1, YEL, "Gap-up on 'good news':\nretail buys the first candle", tx=1, ty=25870)
    step(ax, pn + 5, 25866, 2, DN, "No follow-through; 15-min\nlow 25,834 breaks", tx=pn + 7, ty=25880)
    step(ax, pn + 22, 25752, 3, MAG, "Gap fill: trapped longs\nexit at a loss", tx=pn + 7, ty=25690)
    trade(ax, pn + 4, 25830, 25875, 25705, x1=n - 1, side="short")
    frame(fig, ax, "Ch 7 · Gap-up trap: the open is the high",
          "5-min · Overnight gap is filled by sellers distributing into retail's opening euphoria",
          times(pn, "14:30") + times(dn), step=6, ax2=ax2)
    save(fig, "c07a")


def c07b():
    pn, dn = 12, 40
    d = _gap([(0, 25790), (6, 25770), (11, 25760)], pn,
             [(0, 25622), (2, 25603), (4, 25618), (6, 25640), (10, 25660), (16, 25672), (24, 25710), (32, 25750),
              (39, 25768)], dn, 73)
    setb(d, pn, o=25628, h=25632, l=25608, c=25612, v=240)
    setb(d, pn + 1, o=25612, h=25618, l=25596, c=25602, v=200)
    setb(d, pn + 2, o=25602, h=25630, l=25600, c=25627, v=220)
    setb(d, pn + 3, o=25627, h=25641, l=25624, c=25638, v=210)
    fig, ax, ax2 = figure(lower=True)
    candles(ax, d)
    n = d["n"]
    ax.set_xlim(-1, n + 9)
    ax.set_ylim(25570, 25810)
    volume(ax2, d)
    vline(ax, pn - 0.5, "Next day 09:15", MUTED, y=25805)
    level(ax, 25760, "PDC 25,760", WHITE, x0=-1, side="left", dy=9)
    zone(ax, 25628, 25760, BLUE, "GAP -132 pts", x0=pn - 0.5, x1=n + 8, side="right", alpha=0.07, ty=25690)
    zone(ax, 25596, 25632, PURPLE, None, x0=pn - 0.4, x1=pn + 2.4, alpha=0.25)
    step(ax, pn + 1, 25588, 1, YEL, "Panic open: retail buys PE /\nsells CE at the low", tx=1, ty=25600)
    step(ax, pn + 3, 25650, 2, UP, "15-min high 25,632\nbreaks: shorts trapped", tx=pn + 6, ty=25595)
    step(ax, pn + 25, 25735, 3, MAG, "Gap fill: short covering", tx=pn + 10, ty=25790)
    trade(ax, pn + 4, 25638, 25594, 25755, x1=n - 1, side="long")
    frame(fig, ax, "Ch 7 · Gap-down trap: selling the panic",
          "5-min · Gap below PDL with no follow-through below the first 15-min low = fade it",
          times(pn, "14:30") + times(dn), step=6, ax2=ax2)
    save(fig, "c07b")


# ---------------------------------------------------------------- ch8
def c08a():
    n = 48
    d = gen([(0, 25850), (1, 25868), (2, 25838), (3, 25862), (4, 25874), (5, 25890), (7, 25872), (9, 25848),
             (11, 25826), (15, 25808), (22, 25790), (28, 25800), (34, 25768), (40, 25758), (47, 25745)],
            n, noise=4, wick=3, seed=81)
    setb(d, 0, o=25846, h=25866, l=25840, c=25858, v=300)
    setb(d, 1, o=25858, h=25880, l=25852, c=25862, v=260)
    setb(d, 2, o=25862, h=25864, l=25830, c=25842, v=240)
    setb(d, 4, o=25864, h=25893, l=25862, c=25888, v=170)
    setb(d, 5, o=25888, h=25897, l=25876, c=25879, v=150)
    fig, ax, ax2 = figure(lower=True)
    candles(ax, d)
    ax.set_xlim(-1, n + 9)
    ax.set_ylim(25720, 25930)
    volume(ax2, d)
    zone(ax, 25830, 25880, PURPLE, "OR 09:15-09:30", x0=-0.5, x1=2.5, side="left", alpha=0.25,
         ty=25818)
    level(ax, 25880, "OR high 25,880", PURPLE, x0=2.5, x1=30, side="right")
    level(ax, 25830, "OR low 25,830", PURPLE, x0=2.5, x1=30, side="right")
    step(ax, 4, 25902, 1, YEL, "ORB buyers enter above\n25,880 at 09:35", tx=8, ty=25915)
    step(ax, 7, 25858, 2, DN, "Back inside the range\nwithin 2 candles", tx=11, ty=25890)
    step(ax, 10, 25820, 3, MAG, "OR low breaks: ORB longs'\nSL + new shorts", tx=14, ty=25850)
    trade(ax, 11, 25826, 25898, 25740, x1=n - 1, side="short")
    frame(fig, ax, "Ch 8 · Opening-range trap: the first breakout fails",
          "5-min · The first move out of the 15-min range often grabs liquidity, then reverses",
          times(n), step=6, ax2=ax2)
    save(fig, "c08a")


def c08b():
    n = 48
    d = gen([(0, 25850), (1, 25868), (2, 25838), (4, 25872), (6, 25892), (9, 25882), (11, 25886), (14, 25912),
             (20, 25935), (26, 25925), (32, 25958), (40, 25972), (47, 25985)], n, noise=4, wick=3, seed=83)
    setb(d, 0, o=25846, h=25866, l=25840, c=25858, v=280)
    setb(d, 1, o=25858, h=25880, l=25852, c=25862, v=260)
    setb(d, 2, o=25862, h=25864, l=25830, c=25842, v=240)
    setb(d, 5, o=25872, h=25896, l=25870, c=25893, v=420)
    setb(d, 9, o=25887, h=25890, l=25877, c=25886, v=140)
    fig, ax, ax2 = figure(lower=True)
    candles(ax, d)
    ax.set_xlim(-1, n + 9)
    ax.set_ylim(25810, 26005)
    volume(ax2, d, highlight=[5])
    zone(ax, 25830, 25880, PURPLE, "Opening range", x0=-0.5, x1=2.5, side="left", alpha=0.25, ty=25822)
    level(ax, 25880, "OR high 25,880", PURPLE, x0=2.5, x1=30, side="right")
    step(ax, 5, 25904, 1, YEL, "Breakout with 2x volume\n(real participation)", tx=1, ty=25975)
    step(ax, 9, 25870, 2, UP, "Retest holds above 25,880:\nold resistance = support", tx=11, ty=25840)
    trade(ax, 10, 25888, 25866, 25954, x1=n - 1, side="long")
    frame(fig, ax, "Ch 8 · Contrast: a genuine opening-range breakout",
          "5-min · Volume expansion + successful retest. Trade the retest, never the first spike",
          times(n), step=6, ax2=ax2)
    save(fig, "c08b")


# ---------------------------------------------------------------- ch9
def c09a():
    n = 75
    way = [(0, 25960), (6, 25995), (10, 25975), (16, 26010), (22, 25988), (30, 26008), (36, 25992),
           (46, 26030), (48, 26005), (54, 25996), (60, 25972), (62, 25992), (68, 26008), (74, 26004)]
    d = gen(way, n, noise=5, wick=4, seed=91)
    setb(d, 46, o=26018, h=26036, l=26015, c=26031, v=200)
    setb(d, 47, o=26031, h=26033, l=26008, c=26010)
    setb(d, 60, o=25985, h=25988, l=25966, c=25971, v=210)
    setb(d, 61, o=25971, h=25994, l=25969, c=25990)
    fig, ax, _ = figure(h=4.9)
    candles(ax, d)
    ax.set_xlim(-1, n + 9)
    ax.set_ylim(25930, 26070)
    zone(ax, 25985, 26015, AMBER, None, alpha=0.12)
    level(ax, 26000, "26,000: max pain + highest CE & PE OI", YEL, ls="-.", side="right", dy=-10)
    step(ax, 46, 26042, 1, YEL, "13:05 breakout buyers\nbuy 26,050 CE", tx=30, ty=26055)
    step(ax, 60, 25960, 2, MAG, "14:15 breakdown sellers\nbuy 26,000 PE", tx=44, ty=25945)
    step(ax, 74, 26014, 3, UP, "Close 26,004: both\nbuyers lose, writers win", tx=60, ty=26058)
    frame(fig, ax, "Ch 9 · Round-number pin on expiry day",
          "5-min, expiry Tuesday · Heavy writing at 26,000 both sides keeps price magnetised to the strike",
          times(n), step=9)
    save(fig, "c09a")


def c09b():
    import matplotlib.pyplot as plt
    from charts_engine import figure as _f  # noqa
    strikes = np.arange(25700, 26301, 50)
    ce = np.array([18, 22, 30, 42, 60, 95, 168, 120, 132, 110, 140, 90, 70], float)
    pe = np.array([92, 120, 86, 140, 118, 130, 175, 82, 58, 40, 30, 22, 14], float)
    fig, ax = plt.subplots(figsize=(10, 4.4))
    x = np.arange(len(strikes))
    ax.bar(x - 0.2, ce, 0.38, color=DN, label="Call OI (lakh)")
    ax.bar(x + 0.2, pe, 0.38, color=UP, label="Put OI (lakh)")
    ax.set_xticks(x)
    ax.set_xticklabels([f"{s:,}" for s in strikes], fontsize=7.5)
    ax.yaxis.tick_right()
    ax.tick_params(length=0)
    i = list(strikes).index(26000)
    ax.axvline(i, color=YEL, ls="-.", lw=1.2)
    ax.text(i + 0.15, 182, "Max pain 26,000", color=YEL, fontsize=8, fontweight="bold")
    ax.annotate("Call wall: writers sell\n26,000/26,100 CE -\nceiling for expiry", xy=(i + 0.8, 168), xytext=(8.6, 160),
                fontsize=7.6, bbox=dict(boxstyle="round,pad=0.3", fc="#0b0f17", ec=DN),
                arrowprops=dict(arrowstyle="->", color=DN))
    ax.annotate("Put wall: writers sell\n25,850/26,000 PE -\nfloor for expiry", xy=(i - 0.6, 150), xytext=(0.2, 165),
                fontsize=7.6, bbox=dict(boxstyle="round,pad=0.3", fc="#0b0f17", ec=UP),
                arrowprops=dict(arrowstyle="->", color=UP))
    ax.legend(loc="upper right", bbox_to_anchor=(0.99, 0.62))
    ax.set_ylim(0, 200)
    fig.text(0.012, 0.975, "Ch 9 · Option-chain view: OI walls and max pain", fontsize=11.5, fontweight="bold",
             color=WHITE, va="top")
    fig.text(0.012, 0.925, "Weekly NIFTY options, expiry morning · OI in lakh contracts (illustrative)",
             fontsize=8, color=MUTED, va="top")
    fig.text(0.988, 0.012, "Synthetic data · illustration only", fontsize=6.5, color=MUTED, ha="right")
    fig.subplots_adjust(left=0.02, right=0.95, top=0.86, bottom=0.08)
    save(fig, "c09b")


# ---------------------------------------------------------------- ch10
def expiry_series():
    """NIFTY spot on expiry day, solved so the 25,850 CE prices 51 -> 30 -> 79."""
    K, n = 25850, 75
    def left(i):
        return 375 - i * 5 - 5  # minutes to 15:30 at the close of bar i
    # calibrate IV so S=25815 at 10:40 (bar 17) -> 51
    lo_, hi_ = 0.03, 0.4
    for _ in range(60):
        iv = (lo_ + hi_) / 2
        lo_, hi_ = (iv, hi_) if bs_call(25815, K, left(17), iv) < 51 else (lo_, iv)
    def solve(target, i):
        a, b = 25500, 26200
        for _ in range(60):
            m = (a + b) / 2
            a, b = (m, b) if bs_call(m, K, left(i), iv) < target else (a, m)
        return m
    anchors = {17: 51, 24: 47, 32: 41, 38: 36, 45: 30, 49: 30.5, 53: 31, 57: 32, 60: 36, 63: 45, 66: 54,
               69: 66, 72: 79, 74: 77}
    way = [(0, 25790), (6, 25808), (12, 25796)] + [(i, solve(t, i)) for i, t in anchors.items()]
    s30, s79 = solve(30, 45), solve(79, 72)
    d = gen(way, n, noise=2.5, wick=2.5, seed=101)
    d["v"][58:74] *= 2.0
    p = {k: np.array([bs_call(d[k][i], K, left(i), iv) for i in range(n)]) for k in ("o", "h", "l", "c")}
    p["n"] = n
    p["v"] = d["v"]
    return d, p, iv, s30, s79


def c10a():
    d, p, iv, s30, s79 = expiry_series()
    n = d["n"]
    import matplotlib.pyplot as plt
    fig, (ax, ax2) = plt.subplots(2, 1, figsize=(10, 6.4), sharex=True, gridspec_kw={"height_ratios": [1, 1.25],
                                                                                      "hspace": 0.06})
    from charts_engine import _fmt
    from matplotlib.ticker import FuncFormatter
    for a in (ax, ax2):
        a.yaxis.tick_right()
        a.tick_params(length=0)
    ax.yaxis.set_major_formatter(FuncFormatter(_fmt))
    candles(ax, d)
    candles(ax2, p)
    ax.set_xlim(-1, n + 9)
    ax.set_ylim(min(d["l"]) - 15, max(d["h"]) + 25)
    ax2.set_ylim(0, 100)
    ax.text(0, max(d["h"]) + 14, "NIFTY spot (5-min)", color=MUTED, fontsize=7.8)
    level(ax, 25850, "Strike 25,850", AMBER, side="right")
    note(ax, "14:00 onward: spot rallies ~100 pts\n(short covering into the close)", (66, d["c"][66]), (40, d["c"][66] + 20),
         ec=YEL)
    ax2.text(0, 93, "25,850 CE premium (5-min), expiry day", color=MUTED, fontsize=7.8)
    xs = 17, 45, 72
    trade_y = (51, 30, 79)
    ax2.plot([17, n + 0.5], [51, 51], color=BLUE, lw=1.1)
    ax2.text(n + 0.8, 51, "SOLD 51", color=BLUE, fontsize=7.4, fontweight="bold", va="center",
             bbox=dict(boxstyle="round,pad=0.18", fc=PANEL, ec=BLUE, lw=0.6))
    step(ax2, xs[0], 51 + 6, 1, BLUE, "10:40 sell 25,850 CE at 51\n(spot 25,815, 35 pts OTM)", tx=1, ty=80)
    step(ax2, xs[1], 30 - 6, 2, UP, "13:05: 30 (41% captured).\nTrail SL to ~40 (lock half)", tx=24, ty=12)
    vline(ax2, 66, "14:45 cutoff:\nexit ~" + f"{p['c'][66]:.0f}", YEL, ls="--", y=97, ha="right", lw=1.3)
    step(ax2, xs[2], 79 + 6, 3, DN, "15:15: 79", tx=75, ty=95)
    note(ax2, "Last hour gamma: each 10-pt\nspot move = ₹7-9 premium", (69, p["c"][69]), (49, 70), ec=MAG)
    ax2.fill_between(np.arange(n), 51, np.maximum(p["c"], 51), where=p["c"] > 51, color=DN, alpha=0.18)
    from charts_engine import times as _t
    xt = _t(n)
    ticks = list(range(0, n, 6))
    ax2.set_xticks(ticks)
    ax2.set_xticklabels([xt[i] for i in ticks], fontsize=7.5)
    fig.text(0.012, 0.975, "Ch 10 · Expiry-day gamma spike: short 25,850 CE goes 51 → 30 → 79",
             fontsize=11.5, fontweight="bold", color=WHITE, va="top")
    fig.text(0.012, 0.94, f"Premium computed with Black-Scholes from the spot path (IV {iv * 100:.1f}%). "
                          "5 lots x 65 = 325 qty: -28 pts = -₹9,100", fontsize=8, color=MUTED, va="top")
    fig.text(0.988, 0.012, "Synthetic NIFTY data · illustration only", fontsize=6.5, color=MUTED, ha="right")
    fig.subplots_adjust(left=0.02, right=0.925, top=0.9, bottom=0.06)
    save(fig, "c10a")
    return iv


def c10b():
    import matplotlib.pyplot as plt
    _, _, iv, _, _ = expiry_series()
    K = 25850
    S = np.linspace(25700, 26000, 300)
    fig, ax = plt.subplots(figsize=(10, 4.4))
    cols = [MUTED, BLUE, AMBER, DN]
    for mins, col in zip((375, 180, 60, 15), cols):
        ax.plot(S, [bs_call(s, K, mins, iv) for s in S], color=col, lw=1.8,
                label=f"{mins // 60}h {mins % 60:02d}m to expiry" if mins >= 60 else f"{mins} min to expiry")
    ax.plot(S, np.maximum(S - K, 0), color=WHITE, lw=1, ls=":", label="Value at 15:30 (intrinsic)")
    ax.yaxis.tick_right()
    ax.tick_params(length=0)
    ax.set_xlabel("NIFTY spot", fontsize=8)
    ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f"{v:,.0f}"))
    d15 = (bs_call(25880, K, 15, iv) - bs_call(25860, K, 15, iv)) / 20
    d375 = (bs_call(25880, K, 375, iv) - bs_call(25860, K, 375, iv)) / 20
    ax.annotate(f"Near the strike in the last 15 min,\ndelta jumps from ~0.1 to ~0.9 within\n~60 pts: "
                f"at 25,870 delta ≈ {d15:.2f} vs {d375:.2f}\nin the morning", xy=(25872, bs_call(25872, K, 15, iv)),
                xytext=(25705, 105), fontsize=7.6, bbox=dict(boxstyle="round,pad=0.3", fc="#0b0f17", ec=DN),
                arrowprops=dict(arrowstyle="->", color=DN))
    ax.legend(loc="upper left", bbox_to_anchor=(0.01, 0.55))
    ax.set_ylim(0, 160)
    fig.text(0.012, 0.975, "Ch 10 · Why it happens: the gamma curve bends as expiry approaches",
             fontsize=11.5, fontweight="bold", color=WHITE, va="top")
    fig.text(0.012, 0.925, "25,850 CE price vs spot at different times on expiry day (Black-Scholes, same IV)",
             fontsize=8, color=MUTED, va="top")
    fig.text(0.988, 0.012, "Model illustration", fontsize=6.5, color=MUTED, ha="right")
    fig.subplots_adjust(left=0.02, right=0.95, top=0.86, bottom=0.12)
    save(fig, "c10b")


# ---------------------------------------------------------------- ch11
def _two_panel(title, sub, h=6.0, ratios=(1, 1.2)):
    import matplotlib.pyplot as plt
    from matplotlib.ticker import FuncFormatter
    from charts_engine import _fmt
    fig, (ax, ax2) = plt.subplots(2, 1, figsize=(10, h), sharex=True,
                                  gridspec_kw={"height_ratios": ratios, "hspace": 0.06})
    for a in (ax, ax2):
        a.yaxis.tick_right()
        a.tick_params(length=0)
        a.yaxis.set_major_formatter(FuncFormatter(_fmt))
    fig.text(0.012, 0.975, title, fontsize=11.5, fontweight="bold", color=WHITE, va="top")
    fig.text(0.012, 0.938, sub, fontsize=8, color=MUTED, va="top")
    fig.text(0.988, 0.012, "Synthetic NIFTY data · illustration only", fontsize=6.5, color=MUTED, ha="right")
    fig.subplots_adjust(left=0.02, right=0.925, top=0.9, bottom=0.06)
    return fig, ax, ax2


def _days_ticks(ax2, days, per):
    ticks = [i * per for i in range(len(days))]
    ax2.set_xticks(ticks)
    ax2.set_xticklabels([f"{dname} 09:15" for dname in days], fontsize=7.5)


def c11a():
    per, K, iv = 25, 25750, 0.115
    n = per * 3
    d = gen([(0, 25748), (6, 25790), (14, 25735), (22, 25772), (30, 25725), (38, 25780), (46, 25742), (54, 25768),
             (60, 25738), (66, 25762), (74, 25752)], n, noise=6, wick=4, seed=111)
    def left(i):
        return (3 * 375) - (i + 1) * 15  # minutes to Tue 15:30 (Fri, Mon, Tue sessions)
    p = {k: np.array([bs_call(d[k][i], K, left(i), iv) for i in range(n)]) for k in ("o", "h", "l", "c")}
    p["n"] = n
    fig, ax, ax2 = _two_panel("Ch 11 · Option buyer's trap: theta eats a 'cheap' ATM call",
                              "15-min, Friday → Tuesday expiry · Spot goes nowhere, premium melts")
    candles(ax, d)
    candles(ax2, p)
    ax.set_xlim(-1, n + 8)
    ax.set_ylim(25690, 25830)
    ax2.set_ylim(0, max(p["h"]) * 1.2)
    zone(ax, 25725, 25790, BLUE, "Range 25,725-25,790 for 3 days", alpha=0.08, side="left", ty=25815)
    for x in (per - 0.5, 2 * per - 0.5):
        ax.axvline(x, color=GRID, lw=1)
        ax2.axvline(x, color=GRID, lw=1)
    b0 = p["c"][1]
    ax2.plot([1, n], [b0, b0], color=BLUE, lw=1.1)
    ax2.text(n + 0.6, b0, f"BOUGHT {b0:.0f}", color=BLUE, fontsize=7.4, fontweight="bold", va="center",
             bbox=dict(boxstyle="round,pad=0.18", fc=PANEL, ec=BLUE, lw=0.6))
    step(ax2, 1, b0 + 8, 1, BLUE, f"Fri 09:30: buy 25,750 CE at {b0:.0f}\n'only ₹{b0 * 65:,.0f} per lot'",
         tx=4, ty=max(p['h']) * 1.08)
    step(ax2, 2 * per + 2, p["c"][2 * per + 2] + 6, 2, AMBER,
         f"Tue open: spot same,\npremium {p['c'][2 * per + 2]:.0f}", tx=30, ty=25)
    step(ax2, n - 3, p["c"][n - 3] + 6, 3, DN, f"Tue 14:45: {p['c'][n - 3]:.0f}\n(-{(1 - p['c'][n - 3] / b0) * 100:.0f}%)",
         tx=60, ty=max(p['h']) * 0.85)
    _days_ticks(ax2, ["Fri", "Mon", "Tue (expiry)"], per)
    save(fig, "c11a")


def c11b():
    per, Kc, Kp, iv = 25, 25900, 25500, 0.12
    n = per * 2
    d = gen([(0, 25705), (4, 25725), (8, 25712), (14, 25780), (18, 25768), (24, 25835), (28, 25850), (34, 25925),
             (38, 25910), (44, 26010), (49, 26045)], n, noise=6, wick=4, seed=113)
    def left(i):
        return 750 - (i + 1) * 15
    ce = np.array([bs_call(d["c"][i], Kc, left(i), iv) for i in range(n)])
    pe = np.array([bs_call(d["c"][i], Kp, left(i), iv) - d["c"][i] + Kp for i in range(n)])
    fig, ax, ax2 = _two_panel("Ch 11 · Option seller's trap: a short strangle meets a trend day",
                              "15-min, Monday → Tuesday expiry · Short 25,900 CE + 25,500 PE, 2 lots each")
    candles(ax, d)
    ax.set_xlim(-1, n + 8)
    ax.set_ylim(25650, 26080)
    level(ax, Kc, "Short CE 25,900", DN)
    ax.axvline(per - 0.5, color=GRID, lw=1)
    ax2.axvline(per - 0.5, color=GRID, lw=1)
    x = np.arange(n)
    ax2.plot(x, ce, color=DN, lw=1.8, label="25,900 CE premium")
    ax2.plot(x, pe, color=UP, lw=1.8, label="25,500 PE premium")
    ax2.plot(x, ce + pe, color=YEL, lw=1.4, ls="--", label="Strangle value (what you owe)")
    credit = ce[1] + pe[1]
    ax2.axhline(credit, color=BLUE, lw=1)
    ax2.text(n + 0.6, credit, f"CREDIT {credit:.0f}", color=BLUE, fontsize=7.4, fontweight="bold", va="center",
             bbox=dict(boxstyle="round,pad=0.18", fc=PANEL, ec=BLUE, lw=0.6))
    ax2.set_ylim(0, max(ce + pe) * 1.25)
    ax2.legend(loc="upper left")
    loss = (ce[-1] + pe[-1] - credit) * 130
    step(ax2, n - 1, ce[-1] + pe[-1] + 8, 1, DN,
         f"Spot +{d['c'][-1] - d['c'][1]:.0f} pts: strangle {credit:.0f} → {ce[-1] + pe[-1]:.0f}\n"
         f"loss ≈ ₹{loss:,.0f} on 2 lots;\nPE gain can't offset CE gamma", tx=25, ty=max(ce + pe) * 0.85)
    ticks = [0, per]
    ax2.set_xticks(ticks)
    ax2.set_xticklabels(["Mon 09:15", "Tue (expiry) 09:15"], fontsize=7.5)
    save(fig, "c11b")


# ---------------------------------------------------------------- ch12
def c12a():
    n = 44
    d = gen([(0, 25800), (3, 25812), (6, 25796), (8, 25808), (9, 25812), (10, 25880), (12, 25865), (15, 25790),
             (17, 25742), (20, 25760), (25, 25770), (31, 25740), (43, 25700)], n, noise=3, wick=2.5, seed=121)
    setb(d, 9, o=25810, h=25888, l=25806, c=25876, v=600)
    setb(d, 10, o=25876, h=25884, l=25858, c=25862, v=420)
    setb(d, 14, o=25820, h=25826, l=25780, c=25786, v=520)
    setb(d, 15, o=25786, h=25790, l=25735, c=25748, v=560)
    d["v"][:9] *= 0.5
    fig, ax, ax2 = figure(lower=True)
    candles(ax, d)
    ax.set_xlim(-1, n + 9)
    ax.set_ylim(25670, 25915)
    volume(ax2, d, highlight=[9, 15])
    vline(ax, 8.5, "10:00 RBI policy", YEL, y=25910, lw=1.3)
    zone(ax, 25790, 25820, PURPLE, "Pre-event squeeze:\nIV high, volume dries up", x0=-1, x1=8.4, side="left",
         ty=25846)
    zone(ax, 25670, 25915, DN, None, x0=8.5, x1=14.5, alpha=0.06)
    ax.text(11.5, 25676, "No-trade window\n10:00-10:30", color=DN, fontsize=7.2, ha="center", va="bottom")
    step(ax, 9, 25896, 1, YEL, "Headline spike +70:\nretail buys CE", tx=16, ty=25898)
    step(ax, 15, 25726, 2, MAG, "Full reversal: buyers' SL\n+ sellers' SL both hit", tx=17, ty=25700)
    step(ax, 25, 25784, 3, UP, "After the dust: short the\nretest of the event range", tx=27, ty=25850)
    trade(ax, 26, 25770, 25796, 25718, x1=n - 1, side="short", fs=7)
    frame(fig, ax, "Ch 12 · Event whipsaw: RBI policy at 10:00",
          "5-min · First move after the headline is often a liquidity grab in both directions",
          times(n, "09:15"), step=6, ax2=ax2)
    save(fig, "c12a")


def c12b():
    n = 25
    d = gen([(0, 25600), (3, 25640), (6, 25450), (9, 25520), (12, 25380), (15, 25470), (18, 25560), (21, 25520),
             (24, 25585)], n, noise=10, wick=12, seed=123)
    d["v"][6:16] *= 2
    fig, ax, ax2 = figure(lower=True)
    candles(ax, d, width=0.66)
    ax.set_xlim(-1, n + 4)
    ax.set_ylim(25330, 25700)
    volume(ax2, d)
    vline(ax, 6.5, "11:00 speech begins", YEL, y=25695)
    step(ax, 6, d["l"][6] - 15, 1, DN, "Tax headline: -190 pts", tx=8, ty=25660)
    step(ax, 12, d["l"][12] - 15, 2, MAG, "Second leg: put buyers\nchase at the low", tx=14, ty=25370)
    step(ax, 18, d["h"][18] + 15, 3, UP, "Clarification: +180 pts.\nBoth sides stopped twice", tx=19.5, ty=25640)
    frame(fig, ax, "Ch 12 · Budget day: a ~270-point two-way range",
          "15-min · Event days widen ranges and IV; size down by 50% or stay out", times(n, step=15), step=4,
          ax2=ax2)
    save(fig, "c12b")


# ---------------------------------------------------------------- ch13
def c13a():
    n = 56
    d = gen([(0, 25700), (5, 25800), (11, 25715), (17, 25785), (22, 25730), (27, 25772), (31, 25742), (34, 25765),
             (36, 25752), (38, 25785), (40, 25768), (44, 25718), (49, 25690), (55, 25668)], n, noise=3, wick=2.5,
            seed=131)
    setb(d, 38, o=25762, h=25791, l=25760, c=25787, v=110)
    setb(d, 39, o=25787, h=25790, l=25770, c=25772, v=120)
    setb(d, 41, o=25765, h=25766, l=25735, c=25738, v=300)
    fig, ax, ax2 = figure(lower=True)
    candles(ax, d)
    ax.set_xlim(-1, n + 9)
    ax.set_ylim(25640, 25830)
    volume(ax2, d, highlight=[38, 41])
    tline(ax, 5, 25805, 34, 25768, AMBER, ext=6)
    tline(ax, 11, 25710, 31, 25738, CYAN, ext=9)
    step(ax, 38, 25800, 1, YEL, "Breakout above triangle on\nlow volume: retail buys", tx=14, ty=25822)
    step(ax, 41, 25728, 2, DN, "Back inside + break of\nlower line = real move", tx=44, ty=25790)
    stops(ax, 30, 37, 25726, "Longs' SL under\nthe lower trendline", side="left", ty=25690)
    trade(ax, 42, 25736, 25794, 25660, x1=n - 1, side="short")
    frame(fig, ax, "Ch 13 · Triangle trap: the first breakout is the fake",
          "5-min · The apex is where every pattern-trader's orders sit, on both sides", times(n, "10:00"),
          step=6, ax2=ax2)
    save(fig, "c13a")


def c13b():
    n = 56
    d = gen([(0, 25860), (8, 25978), (14, 25905), (21, 25980), (27, 25902), (29, 25888), (31, 25895), (34, 25930),
             (39, 25985), (44, 26010), (50, 26045), (55, 26060)], n, noise=4, wick=3, seed=133)
    setb(d, 8, h=25982)
    setb(d, 21, h=25983)
    setb(d, 28, o=25901, h=25903, l=25884, c=25887, v=180)
    setb(d, 29, o=25887, h=25893, l=25878, c=25890, v=170)
    setb(d, 31, o=25896, h=25922, l=25894, c=25919, v=320)
    fig, ax, ax2 = figure(lower=True)
    candles(ax, d)
    ax.set_xlim(-1, n + 9)
    ax.set_ylim(25830, 26090)
    volume(ax2, d, highlight=[31])
    level(ax, 25982, "Double top 25,982", DN, x0=4, x1=n + 8, side="right")
    level(ax, 25902, "Neckline 25,902", AMBER, x0=10, x1=40, side="right")
    step(ax, 8, 25995, 1, DN, "Top 1", tx=2, ty=26040)
    step(ax, 21, 25996, 2, DN, "Top 2: 'textbook' pattern", tx=12, ty=26060)
    step(ax, 29, 25865, 3, YEL, "Neckline break: retail\nshorts / buys PE", tx=33, ty=25860)
    step(ax, 31, 25935, 4, UP, "Reclaim neckline:\nshorts trapped", tx=12, ty=25850)
    step(ax, 40, 25998, 5, MAG, "Squeeze through both tops:\nshorts' SL fuels it", tx=42, ty=25945)
    frame(fig, ax, "Ch 13 · Failed double top: when the pattern is the bait",
          "5-min · A neckline break with no follow-through below is a buy signal, not a sell",
          times(n, "10:50"), step=6, ax2=ax2)
    save(fig, "c13b")


ALL = [c01, c02, c03, c04, c05a, c05b, c06a, c06b, c07a, c07b, c08a, c08b, c09a, c09b, c10a, c10b, c11a, c11b,
       c12a, c12b, c13a, c13b]

if __name__ == "__main__":
    import sys
    sel = sys.argv[1:]
    for f in ALL:
        if not sel or f.__name__ in sel:
            f()
            print("ok", f.__name__)
