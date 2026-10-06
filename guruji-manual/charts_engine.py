"""Chart engine: synthetic NIFTY OHLC + dark-theme candlestick plotting + annotation helpers."""
from math import erf, log, sqrt
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
from matplotlib.ticker import FuncFormatter  # noqa: E402

OUT = Path(__file__).with_name("charts")
OUT.mkdir(exist_ok=True)

BG, PANEL, GRID = "#0b0f17", "#111724", "#242c3b"
TXT, MUTED = "#d6dbe4", "#8b93a5"
UP, DN = "#26a69a", "#ef5350"
AMBER, BLUE, MAG, YEL, CYAN, WHITE, ORANGE, PURPLE = (
    "#f5b041", "#4fa3ff", "#e45bd8", "#ffd54f", "#4dd0e1", "#ffffff", "#ff8a3d", "#9c7cff")

plt.rcParams.update({
    "font.family": "DejaVu Sans", "font.size": 8.5, "axes.facecolor": PANEL, "figure.facecolor": BG,
    "axes.edgecolor": GRID, "axes.labelcolor": TXT, "xtick.color": MUTED, "ytick.color": MUTED,
    "text.color": TXT, "axes.grid": True, "grid.color": GRID, "grid.linewidth": 0.6, "grid.alpha": 0.7,
    "savefig.facecolor": BG, "legend.facecolor": PANEL, "legend.edgecolor": GRID, "legend.fontsize": 7.5,
})
W, H1, H2 = 10, 4.6, 5.6  # inches: width, height single-panel, height with lower panel
DPI = 170


# ------------------------------------------------------------------ data
def gen(way, n, noise=5.0, wick=4.0, seed=1, vol=100.0):
    """Closes follow piecewise-linear waypoints [(idx, price), ...] plus noise that fades to 0 at waypoints."""
    rng = np.random.default_rng(seed)
    xs, ys = zip(*way)
    idx = np.arange(n)
    path = np.interp(idx, xs, ys)
    dist = np.min(np.abs(idx[:, None] - np.array(xs)[None, :]), axis=1)
    c = path + rng.normal(0, noise, n) * np.minimum(1, dist / 2.0)
    o = np.empty(n)
    o[0] = c[0] - rng.normal(0, noise)
    o[1:] = c[:-1]
    h = np.maximum(o, c) + np.abs(rng.normal(0, wick, n))
    l_ = np.minimum(o, c) - np.abs(rng.normal(0, wick, n))
    v = vol * (0.7 + 0.5 * rng.random(n)) * (1 + np.abs(c - o) / (noise * 3 + 1e-9))
    return {"o": o, "h": h, "l": l_, "c": c, "v": v, "n": n}


def setb(d, i, o=None, h=None, l=None, c=None, v=None, link=True):
    """Override one bar; keeps OHLC consistent and links next bar's open to this close."""
    for k, val in (("o", o), ("h", h), ("l", l), ("c", c), ("v", v)):
        if val is not None:
            d[k][i] = val
    d["h"][i] = max(d["h"][i], d["o"][i], d["c"][i])
    d["l"][i] = min(d["l"][i], d["o"][i], d["c"][i])
    if link and i + 1 < d["n"] and c is not None:
        d["o"][i + 1] = d["c"][i]
        d["h"][i + 1] = max(d["h"][i + 1], d["o"][i + 1])
        d["l"][i + 1] = min(d["l"][i + 1], d["o"][i + 1])


def vwap(d):
    tp = (d["h"] + d["l"] + d["c"]) / 3
    return np.cumsum(tp * d["v"]) / np.cumsum(d["v"])


def times(n, start="09:15", step=5):
    hh, mm = map(int, start.split(":"))
    out = []
    for i in range(n):
        t = hh * 60 + mm + i * step
        out.append(f"{t // 60:02d}:{t % 60:02d}")
    return out


def ncdf(x):
    return 0.5 * (1 + erf(x / sqrt(2)))


def bs_call(S, K, mins_left, iv):
    T = max(mins_left, 0.01) / (375 * 252)
    if T <= 0:
        return max(S - K, 0)
    s = iv * sqrt(T)
    d1 = (log(S / K) + 0.5 * s * s) / s
    return S * ncdf(d1) - K * ncdf(d1 - s)


def bs_put(S, K, mins_left, iv):
    return bs_call(S, K, mins_left, iv) - S + K


# ------------------------------------------------------------------ plotting
def _fmt(x, _):
    return f"{x:,.0f}"


def figure(lower=None, h=None, ratios=(3.3, 1)):
    if lower:
        fig, (ax, ax2) = plt.subplots(2, 1, figsize=(W, h or H2), sharex=True,
                                      gridspec_kw={"height_ratios": ratios, "hspace": 0.04})
    else:
        fig, ax = plt.subplots(figsize=(W, h or H1))
        ax2 = None
    for a in (ax, ax2):
        if a is None:
            continue
        a.yaxis.tick_right()
        a.yaxis.set_major_formatter(FuncFormatter(_fmt))
        a.tick_params(length=0)
    return fig, ax, ax2


def candles(ax, d, x0=0, width=0.62, alpha=1.0):
    x = np.arange(d["n"]) + x0
    up = d["c"] >= d["o"]
    col = np.where(up, UP, DN)
    ax.vlines(x, d["l"], d["h"], color=col, linewidth=0.9, alpha=alpha, zorder=3)
    body = d["c"] - d["o"]
    body = np.where(np.abs(body) < 0.6, np.where(up, 0.6, -0.6), body)
    ax.bar(x, body, bottom=d["o"], width=width, color=col, edgecolor=col, linewidth=0.5, alpha=alpha, zorder=4)
    return x


def volume(ax2, d, label="Volume", highlight=()):
    x = np.arange(d["n"])
    col = np.where(d["c"] >= d["o"], UP, DN)
    ax2.bar(x, d["v"], width=0.62, color=col, alpha=0.55, zorder=3)
    for i in highlight:
        ax2.bar([i], [d["v"][i]], width=0.62, color=YEL, alpha=0.95, zorder=4)
    ax2.set_ylabel(label, color=MUTED, fontsize=7.5)
    ax2.yaxis.set_major_formatter(FuncFormatter(lambda v, _: ""))
    ax2.set_ylim(0, max(d["v"]) * 1.25)


def frame(fig, ax, title, sub=None, xt=None, step=6, xlim=None, ylim=None, ax2=None, note=True):
    fig.text(0.012, 0.975, title, fontsize=11.5, fontweight="bold", color=WHITE, va="top")
    if sub:
        fig.text(0.012, 0.925 if ax2 is None else 0.94, sub, fontsize=8, color=MUTED, va="top")
    tgt = ax2 if ax2 is not None else ax
    if xt is not None:
        ticks = list(range(0, len(xt), step))
        tgt.set_xticks(ticks)
        tgt.set_xticklabels([xt[i] for i in ticks], fontsize=7.5)
    if xlim:
        ax.set_xlim(*xlim)
    if ylim:
        ax.set_ylim(*ylim)
    if note:
        fig.text(0.988, 0.012, "Synthetic NIFTY data · illustration only", fontsize=6.5, color=MUTED,
                 ha="right", va="bottom", alpha=0.8)
    top = 0.86 if sub else 0.9
    if ax2 is not None:
        top = 0.885 if sub else 0.91
    fig.subplots_adjust(left=0.02, right=0.925, top=top, bottom=0.08 if ax2 is None else 0.07)


def save(fig, name):
    fig.savefig(OUT / f"{name}.png", dpi=DPI)
    plt.close(fig)


# ------------------------------------------------------------------ annotations
BOX = dict(boxstyle="round,pad=0.3", fc="#0b0f17", ec=GRID, lw=0.8, alpha=0.92)


def zone(ax, y0, y1, color=AMBER, label=None, x0=None, x1=None, side="left", alpha=0.16, fs=7.5, ty=None):
    xl = ax.get_xlim()
    a, b = (x0 if x0 is not None else xl[0]), (x1 if x1 is not None else xl[1])
    ax.fill_between([a, b], y0, y1, color=color, alpha=alpha, lw=0, zorder=1)
    if label:
        tx = a + 0.4 if side == "left" else b - 0.4
        ax.text(tx, ty if ty is not None else (y0 + y1) / 2, label, color=color, fontsize=fs, va="center",
                ha="left" if side == "left" else "right", fontweight="bold", zorder=7,
                bbox=dict(boxstyle="round,pad=0.2", fc=PANEL, ec="none", alpha=0.8))


def level(ax, y, label=None, color=MUTED, ls="--", lw=1.0, x0=None, x1=None, side="right", fs=7.3, dy=0):
    xl = ax.get_xlim()
    a, b = (x0 if x0 is not None else xl[0]), (x1 if x1 is not None else xl[1])
    ax.plot([a, b], [y, y], color=color, ls=ls, lw=lw, zorder=2)
    if label:
        tx = b - 0.3 if side == "right" else a + 0.3
        ax.text(tx, y + dy, label, color=color, fontsize=fs, va="center", ha="right" if side == "right" else "left",
                zorder=7, bbox=dict(boxstyle="round,pad=0.18", fc=PANEL, ec=color, lw=0.6, alpha=0.95))


def step(ax, x, y, n, color=YEL, text=None, tx=None, ty=None, ha="left", fs=7.6):
    ax.scatter([x], [y], s=150, color=color, zorder=8, edgecolors=BG, linewidths=1)
    ax.text(x, y, str(n), color=BG, fontsize=7.5, fontweight="bold", ha="center", va="center", zorder=9)
    if text:
        ax.annotate(text, xy=(x, y), xytext=(tx if tx is not None else x + 1.2, ty if ty is not None else y),
                    fontsize=fs, color=TXT, ha=ha, va="center", zorder=9, bbox=BOX,
                    arrowprops=dict(arrowstyle="-", color=color, lw=0.8) if (tx is not None or ty is not None) else None)


def note(ax, text, xy, xytext, color=TXT, fs=7.6, ha="left", ec=None, arrow=True):
    ax.annotate(text, xy=xy, xytext=xytext, fontsize=fs, color=color, ha=ha, va="center", zorder=9,
                bbox=dict(boxstyle="round,pad=0.3", fc="#0b0f17", ec=ec or color, lw=0.8, alpha=0.95),
                arrowprops=dict(arrowstyle="->", color=ec or color, lw=1.0) if arrow else None)


def stops(ax, x0, x1, y, label="Retail SL here", color=MAG, side="right", fs=7.3, ty=None):
    xs = np.linspace(x0, x1, max(4, int((x1 - x0) * 1.2)))
    ax.scatter(xs, [y] * len(xs), marker="x", s=18, color=color, zorder=6, linewidths=1.1)
    if label:
        tx = x1 + 0.6 if side == "right" else x0 - 0.6
        ax.text(tx, ty if ty is not None else y, label, color=color, fontsize=fs, va="center",
                ha="left" if side == "right" else "right", fontweight="bold", zorder=7,
                bbox=dict(boxstyle="round,pad=0.18", fc=PANEL, ec="none", alpha=0.85))


def trade(ax, x0, entry, sl, tgt, x1=None, side="long", labels=True, tgt2=None, fs=7.3):
    x1 = x1 if x1 is not None else ax.get_xlim()[1] - 0.5
    for y, col, lab in ((entry, BLUE, "ENTRY"), (sl, DN, "SL"), (tgt, UP, "TARGET")) + (
            ((tgt2, UP, "T2"),) if tgt2 else ()):
        ax.plot([x0, x1], [y, y], color=col, lw=1.3, ls="-" if lab == "ENTRY" else "--", zorder=5)
        if labels:
            ax.text(x1 + 0.2, y, f"{lab} {y:,.0f}", color=col, fontsize=fs, va="center", ha="left", fontweight="bold",
                    zorder=8, bbox=dict(boxstyle="round,pad=0.18", fc=PANEL, ec=col, lw=0.6))
    lo, hi = sorted([entry, tgt])
    ax.fill_between([x0, x1], lo, hi, color=UP, alpha=0.07, zorder=1)
    lo, hi = sorted([entry, sl])
    ax.fill_between([x0, x1], lo, hi, color=DN, alpha=0.09, zorder=1)
    ax.scatter([x0], [entry], marker="^" if side == "long" else "v", s=70, color=BLUE, zorder=9,
               edgecolors=WHITE, linewidths=0.6)


def vline(ax, x, label=None, color=MUTED, ls=":", y=None, fs=7.2, ha="left", lw=1.0):
    ax.axvline(x, color=color, ls=ls, lw=lw, zorder=2)
    if label:
        yl = ax.get_ylim()
        ax.text(x + (0.3 if ha == "left" else -0.3), y if y is not None else yl[1] - (yl[1] - yl[0]) * 0.05, label,
                color=color, fontsize=fs, ha=ha, va="top", zorder=7,
                bbox=dict(boxstyle="round,pad=0.18", fc=PANEL, ec="none", alpha=0.85))


def tline(ax, x0, y0, x1, y1, color=CYAN, label=None, ext=0, fs=7.3, lw=1.2, ls="-"):
    slope = (y1 - y0) / (x1 - x0)
    xe = x1 + ext
    ax.plot([x0, xe], [y0, y0 + slope * (xe - x0)], color=color, lw=lw, ls=ls, zorder=5)
    if label:
        ax.text(xe, y0 + slope * (xe - x0), label, color=color, fontsize=fs, ha="left", va="bottom", zorder=7)
