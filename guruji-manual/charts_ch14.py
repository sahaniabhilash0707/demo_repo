"""Charts for Ch 14 (the round-number overshoot trap)."""
import shutil
from pathlib import Path

from charts_engine import (AMBER, BLUE, DN, MAG, MUTED, OUT, UP, YEL, candles, figure, frame, gen, level, note,
                           save, setb, step, stops, times, trade, volume, zone)

HERE = Path(__file__).parent


def c14a():
    """Synthetic replay of the reader's 5-min chart: bear trap at 22,600, bull trap at 22,700."""
    n = 66
    d = gen([(0, 22640), (1, 22606), (4, 22618), (7, 22596), (10, 22612), (12, 22604), (14, 22622), (19, 22668),
             (23, 22700), (27, 22684), (31, 22698), (35, 22680), (38, 22696), (40, 22704), (42, 22690),
             (45, 22668), (48, 22660), (52, 22610), (55, 22575), (58, 22566), (61, 22585), (65, 22612)],
            n, noise=4, wick=3, seed=1401)
    setb(d, 0, o=22700, h=22706, l=22636, c=22640, v=520)
    setb(d, 1, o=22640, h=22644, l=22598, c=22606, v=380)
    setb(d, 11, o=22606, h=22608, l=22583, c=22587, v=180)
    setb(d, 12, o=22587, h=22610, l=22585, c=22608, v=210)
    setb(d, 13, o=22608, h=22624, l=22604, c=22620, v=260)
    setb(d, 40, o=22698, h=22721, l=22696, c=22712, v=60)
    setb(d, 41, o=22712, h=22716, l=22688, c=22690, v=340)
    setb(d, 42, o=22690, h=22694, l=22672, c=22676, v=300)
    setb(d, 50, o=22640, h=22642, l=22606, c=22610, v=360)
    fig, ax, ax2 = figure(lower=True)
    candles(ax, d)
    ax.set_xlim(-1, n + 10)
    ax.set_ylim(22540, 22760)
    volume(ax2, d, highlight=[11, 40, 41])
    zone(ax, 22700, 22722, AMBER, None, x0=20, x1=n + 9, alpha=0.20)
    zone(ax, 22580, 22600, AMBER, None, x0=2, x1=20, alpha=0.20)
    level(ax, 22700, "22,700 · round no. + pivot", YEL, x0=-1, x1=n + 9, side="left", dy=6)
    level(ax, 22600, "22,600 · round no.", YEL, x0=-1, x1=n + 9, side="right", dy=-6)
    step(ax, 11, 22578, 1, YEL, "Flush ~15-20 pts under 22,600:\nshorts sell the 'breakdown'", tx=16, ty=22556)
    step(ax, 13, 22630, 2, UP, "Back above 22,600 in 2 bars:\nshorts trapped → 100-pt rally", tx=2, ty=22672)
    step(ax, 40, 22730, 3, YEL, "Poke ~20 pts over 22,700 on\nLOW volume: breakout buyers in", tx=19, ty=22745)
    step(ax, 41, 22680, 4, DN, "Close back under 22,700:\nthe trap is sprung", tx=52, ty=22711)
    stops(ax, 30, 39, 22668, "Longs' SL under\nthe range", side="left", ty=22650)
    trade(ax, 42, 22690, 22728, 22580, x1=n - 1, side="short")
    note(ax, "120 pts from 22,700", (55, 22578), (56, 22630), color=DN)
    frame(fig, ax, "Ch 14 · The 20-point overshoot trap at round numbers",
          "5-min · Price pokes ~20 points through a hundred-level, then runs 100-120 points the other way",
          times(n), step=6, ax2=ax2)
    save(fig, "c14a")


def c14b():
    """The reader's own chart, copied in as the real-market example."""
    src = HERE / "source" / "reader_chart_nifty_5m.png"
    shutil.copyfile(src, OUT / "c14b.png")


ALL = [c14a, c14b]

if __name__ == "__main__":
    for f in ALL:
        f()
        print("ok", f.__name__)
