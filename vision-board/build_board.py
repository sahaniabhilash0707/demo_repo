"""Trading vision board: protect capital, small daily wins, out of the rat race by May 2029.

Run:  python3 build_board.py   -> Vision_Board_May_2029.png / .pdf
"""
import math
import subprocess
from pathlib import Path

HERE = Path(__file__).parent
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
W, H = 2400, 1520

NAVY, NAVY2, INK = "#0f1b33", "#1a2b4c", "#e9edf5"
GOLD, GOLD_L, GREEN, GREEN_L, RED, MUTED = "#e8b04b", "#ffd98a", "#2fae8a", "#7fe0bf", "#e0645a", "#8d98ad"

CAPITAL = 270000          # trading capital in the risk card (Guruji manual, ch 24)
RISK = CAPITAL // 100     # 1% per trade
START, END = "Oct 2026", "May 2029"
SESSIONS = 640            # approx. NSE trading sessions, 8 Oct 2026 - 7 May 2029
MONTHS = [f"{m} {y % 100:02d}" for y, ms in ((2026, "Oct Nov Dec"), (2027, "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec"),
                                              (2028, "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec"),
                                              (2029, "Jan Feb Mar Apr")) for m in ms.split()]


def inr(n):
    s = str(n)
    if len(s) <= 3:
        return s
    head, tail = s[:-3], s[-3:]
    parts = []
    while len(head) > 2:
        parts.insert(0, head[-2:])
        head = head[:-2]
    if head:
        parts.insert(0, head)
    return ",".join(parts) + "," + tail


# ------------------------------------------------------------------ the art
def art():
    w, h = 2240, 700
    out = [f'<svg viewBox="0 0 {w} {h}" width="{w}" height="{h}" xmlns="http://www.w3.org/2000/svg">',
           '<defs>'
           '<linearGradient id="sky" x1="0" y1="0" x2="1" y2="1">'
           '<stop offset="0" stop-color="#0d1730"/><stop offset=".55" stop-color="#233a63"/>'
           '<stop offset=".85" stop-color="#b8735a"/><stop offset="1" stop-color="#f2b16b"/></linearGradient>'
           '<radialGradient id="sun" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#fff3cf"/>'
           '<stop offset=".6" stop-color="#ffd27a"/><stop offset="1" stop-color="#f0a24a"/></radialGradient>'
           '<radialGradient id="glow" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#ffd98a" stop-opacity=".55"/>'
           '<stop offset="1" stop-color="#ffd98a" stop-opacity="0"/></radialGradient>'
           '<linearGradient id="step" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#1f7f66"/>'
           '<stop offset="1" stop-color="#46d1a4"/></linearGradient>'
           '<clipPath id="r"><rect width="2240" height="700" rx="28"/></clipPath>'
           '</defs><g clip-path="url(#r)">',
           f'<rect width="{w}" height="{h}" fill="url(#sky)"/>']
    # stars on the dark side
    for i in range(70):
        x = (i * 397) % 1300 + 10
        y = (i * 211) % 330 + 12
        r = 1.2 + (i % 3) * 0.6
        out.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#ffffff" opacity="{0.25 + (i % 4) * 0.12:.2f}"/>')
    # sun + rays
    sx, sy = 2010, 205
    out.append(f'<circle cx="{sx}" cy="{sy}" r="300" fill="url(#glow)"/>')
    for k in range(18):
        a = math.radians(k * 20)
        x1, y1 = sx + math.cos(a) * 135, sy + math.sin(a) * 135
        x2, y2 = sx + math.cos(a) * 190, sy + math.sin(a) * 190
        out.append(f'<line x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" stroke="#ffe3a3" '
                   f'stroke-width="5" stroke-linecap="round" opacity=".7"/>')
    out.append(f'<circle cx="{sx}" cy="{sy}" r="112" fill="url(#sun)"/>')
    # hills
    out.append('<path d="M0 640 C 300 590 520 650 820 620 S 1400 560 1700 600 S 2100 560 2240 580 L2240 700 L0 700Z" '
               'fill="#0b1426" opacity=".9"/>')

    # the gamble: spike then crash (behind the stairs)
    out.append('<path d="M470 612 C 560 560 640 300 760 150 C 800 110 830 120 850 170 C 900 330 960 560 1030 668" '
               f'fill="none" stroke="{RED}" stroke-width="5" stroke-dasharray="14 10" opacity=".85"/>')
    out.append('<path d="M985 668 L1075 668 L1060 700 L1000 700Z" fill="#3a1a1f"/>')
    out.append(f'<text x="782" y="118" fill="{RED}" font-family="Jost" font-size="25" font-weight="500" '
               'text-anchor="middle">The gamble: big size, no stop</text>')
    out.append(f'<text x="1092" y="610" fill="{RED}" font-family="Jost" font-size="25" font-weight="500">−46%</text>')
    out.append('<text x="1092" y="640" fill="#f2b7b1" font-family="Jost" font-size="19">needs +85% just to get back</text>')

    # staircase of small daily wins, with a few small controlled losses
    x0, y0, x1, y1 = 470, 612, 1880, 262
    n = 42
    dx = (x1 - x0) / n
    rise = (y0 - y1) / (n - 6 * 0.35 * 2)
    y = y0
    pts = [(x0, y0)]
    losses = {7, 15, 22, 29, 35, 39}
    tops = []
    for i in range(n):
        y = y + rise * 0.35 if i in losses else y - rise
        xa, xb = x0 + i * dx, x0 + (i + 1) * dx
        pts += [(xa, y), (xb, y)]
        tops.append((xa, xb, y, i in losses))
    band = [(a, b + 62) for a, b in reversed(pts)]
    out.append('<path d="M' + " L".join(f"{a:.1f} {b:.1f}" for a, b in pts + band) + 'Z" fill="url(#step)" opacity=".95"/>')
    for xa, xb, yy, loss in tops:
        c = "#f08a7e" if loss else GREEN_L
        out.append(f'<line x1="{xa + 3:.1f}" y1="{yy:.1f}" x2="{xb - 3:.1f}" y2="{yy:.1f}" stroke="{c}" '
                   'stroke-width="5" stroke-linecap="round"/>')
    # milestones along the stairs
    for frac, lab in ((0.0, START), (3 / 31, "2027"), (15 / 31, "2028"), (27 / 31, "2029")):
        i = min(int(frac * n), n - 1)
        xa, xb, yy, _ = tops[i]
        out.append(f'<line x1="{xa:.0f}" y1="{yy + 8:.0f}" x2="{xa:.0f}" y2="{yy + 50:.0f}" stroke="#0b1426" stroke-width="2"/>')
        out.append(f'<text x="{xa + 6:.0f}" y="{yy + 44:.0f}" fill="#0b1426" font-family="Jost" font-size="20" '
                   f'font-weight="500">{lab}</text>')
    out.append(f'<text x="1420" y="540" fill="#e9fff7" font-family="Jost" font-size="24" font-weight="500" '
               'text-anchor="middle">~640 small steps · a few small red ones · never a cliff</text>')

    # the rat wheel (left), with an opening the walker has stepped out of
    cx, cy, R = 250, 430, 170
    gap = (-38, 18)
    a0, a1 = math.radians(gap[1]), math.radians(360 + gap[0])
    out.append(f'<path d="M{cx + R * math.cos(a0):.1f} {cy + R * math.sin(a0):.1f} '
               f'A{R} {R} 0 1 1 {cx + R * math.cos(a1):.1f} {cy + R * math.sin(a1):.1f}" fill="none" '
               f'stroke="{MUTED}" stroke-width="12" stroke-linecap="round"/>')
    out.append(f'<path d="M{cx + (R - 26) * math.cos(a0):.1f} {cy + (R - 26) * math.sin(a0):.1f} '
               f'A{R - 26} {R - 26} 0 1 1 {cx + (R - 26) * math.cos(a1):.1f} {cy + (R - 26) * math.sin(a1):.1f}" '
               f'fill="none" stroke="{MUTED}" stroke-width="4" stroke-dasharray="3 14" stroke-linecap="round"/>')
    for k in range(8):
        a = math.radians(k * 45 + 22)
        out.append(f'<line x1="{cx}" y1="{cy}" x2="{cx + (R - 8) * math.cos(a):.0f}" y2="{cy + (R - 8) * math.sin(a):.0f}" '
                   f'stroke="{MUTED}" stroke-width="3" opacity=".55"/>')
    out.append(f'<circle cx="{cx}" cy="{cy}" r="14" fill="{MUTED}"/>')
    out.append(f'<path d="M{cx - 30} {cy + R} L{cx} {cy} L{cx + 30} {cy + R}" stroke="{MUTED}" stroke-width="8" fill="none"/>')
    # the old self, still running inside, in grey
    out.append(f'<g transform="translate({cx - 20} {cy + 52}) scale(.8)" stroke="#6f7a91" stroke-width="6" '
               'stroke-linecap="round" fill="none"><circle cx="0" cy="-70" r="14" fill="#6f7a91" stroke="none"/>'
               '<path d="M0 -55 L-6 -10 M-6 -10 L-28 18 M-6 -10 L14 16 M-2 -46 L-26 -30 M-2 -46 L22 -36"/></g>')
    out.append(f'<text x="{cx}" y="{cy + R + 70}" fill="{INK}" font-family="Jost" font-size="25" font-weight="500" '
               'text-anchor="middle" letter-spacing="3">THE RAT RACE</text>')
    out.append(f'<text x="{cx}" y="{cy + R + 98}" fill="#b9c2d4" font-family="Jost" font-size="19" '
               'text-anchor="middle">salary → bills → repeat</text>')

    # the walker on the stairs, carrying the CAPITAL shield
    wi = 9
    xa, xb, wy, _ = tops[wi]
    wx = (xa + xb) / 2
    out.append(f'<g transform="translate({wx:.0f} {wy - 4:.0f})" stroke="#fff6e3" stroke-width="7" '
               'stroke-linecap="round" stroke-linejoin="round" fill="none">'
               '<circle cx="0" cy="-118" r="17" fill="#fff6e3" stroke="none"/>'
               '<path d="M0 -100 L4 -50 M4 -50 L-14 -22 L-12 0 M4 -50 L22 -26 L34 -6"/>'
               '<path d="M1 -88 L26 -70"/></g>')
    shx, shy = wx + 44, wy - 112
    out.append(f'<g transform="translate({shx:.0f} {shy:.0f})">'
               f'<path d="M0 0 L46 -14 L92 0 C 92 52 70 84 46 98 C 22 84 0 52 0 0Z" fill="{GOLD}" stroke="#fff6e3" stroke-width="4"/>'
               '<text x="46" y="52" fill="#3b2a10" font-family="Jost" font-size="40" font-weight="500" text-anchor="middle">₹</text>'
               '<text x="46" y="78" fill="#3b2a10" font-family="Jost" font-size="13" font-weight="500" '
               'text-anchor="middle" letter-spacing="1">CAPITAL</text></g>')
    # arrow out of the wheel onto the first step
    out.append(f'<path d="M{cx + 150} {cy + 40} C 380 520 420 600 465 606" fill="none" stroke="#fff6e3" '
               'stroke-width="3" stroke-dasharray="6 8" opacity=".7"/>')

    # the flag at the top: May 2029
    fx, fy = tops[-1][1] - 30, tops[-1][2]
    out.append(f'<line x1="{fx:.0f}" y1="{fy:.0f}" x2="{fx:.0f}" y2="{fy - 190:.0f}" stroke="#fff6e3" stroke-width="6"/>')
    out.append(f'<path d="M{fx:.0f} {fy - 190:.0f} L{fx + 190:.0f} {fy - 162:.0f} L{fx:.0f} {fy - 120:.0f}Z" fill="{GOLD}"/>')
    out.append(f'<text x="{fx + 14:.0f}" y="{fy - 152:.0f}" fill="#3b2a10" font-family="Jost" font-size="24" '
               'font-weight="500">MAY 2029</text>')
    out.append(f'<text x="{fx + 30:.0f}" y="{fy + 120:.0f}" fill="#fff6e3" font-family="Cormorant Garamond" '
               'font-size="46" font-style="italic" text-anchor="middle">Financially free</text>')
    out.append('</g></svg>')
    return "\n".join(out)


# ------------------------------------------------------------------ the cards
def recovery_bars():
    rows = [(10, 11), (20, 25), (30, 43), (46, 85), (50, 100)]
    out = []
    for loss, need in rows:
        hl = ' class="hl"' if loss == 46 else ""
        out.append(f'<div class="bar"{hl}><span class="l">−{loss}%</span>'
                   f'<span class="track"><span class="loss" style="width:{loss}%"></span></span>'
                   f'<span class="track"><span class="need" style="width:{need}%"></span></span>'
                   f'<span class="n">+{need}%</span></div>')
    return "\n".join(out)


def month_grid():
    return "".join(f'<div class="m"><span>{m}</span></div>' for m in MONTHS)


def html():
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:'Cormorant Garamond';font-weight:500;src:url('fonts/CormorantGaramond-500.ttf');}}
@font-face{{font-family:'Cormorant Garamond';font-weight:500;font-style:italic;src:url('fonts/CormorantGaramond-500i.ttf');}}
@font-face{{font-family:'Cormorant Garamond';font-weight:600;src:url('fonts/CormorantGaramond-600.ttf');}}
@font-face{{font-family:'Jost';font-weight:300;src:url('fonts/Jost-300.ttf');}}
@font-face{{font-family:'Jost';font-weight:400;src:url('fonts/Jost-400.ttf');}}
@font-face{{font-family:'Jost';font-weight:500;src:url('fonts/Jost-500.ttf');}}
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{width:{W}px;height:{H}px;background:{NAVY};color:{INK};font-family:'Jost';overflow:hidden}}
.wrap{{padding:54px 80px 0}}
header{{display:flex;justify-content:space-between;align-items:flex-end;margin-bottom:26px}}
h1{{font-family:'Cormorant Garamond';font-weight:600;font-size:96px;line-height:.95;letter-spacing:-.5px}}
h1 em{{color:{GOLD};font-style:italic;font-weight:500}}
.sub{{font-size:27px;font-weight:300;color:#c4ccdb;margin-top:14px;letter-spacing:.3px}}
.sub b{{color:{GOLD_L};font-weight:500}}
.count{{text-align:right}}
.count .big{{font-family:'Cormorant Garamond';font-size:120px;font-weight:600;color:{GOLD};line-height:.9}}
.count .lab{{font-size:21px;letter-spacing:3px;color:#c4ccdb;text-transform:uppercase}}
.art{{border-radius:28px;overflow:hidden;box-shadow:0 20px 50px rgba(0,0,0,.35)}}
.cards{{display:grid;grid-template-columns:1.05fr 1fr 1fr 1.15fr;gap:26px;margin-top:30px}}
.card{{background:{NAVY2};border-radius:22px;padding:26px 28px;height:380px;position:relative}}
.card h3{{font-size:20px;letter-spacing:3px;text-transform:uppercase;color:{GOLD};font-weight:500}}
.card h2{{font-family:'Cormorant Garamond';font-size:43px;font-weight:600;line-height:1.02;margin:8px 0 16px}}
.card p{{font-size:20px;line-height:1.4;color:#c4ccdb;font-weight:300}}
.card p b{{color:{INK};font-weight:500}}
.bar{{display:grid;grid-template-columns:62px 1fr 1fr 64px;gap:10px;align-items:center;margin:9px 0;font-size:19px}}
.bar .track{{height:16px;background:#0f1b33;border-radius:8px;overflow:hidden}}
.bar .loss{{display:block;height:100%;background:{RED};border-radius:8px}}
.bar .need{{display:block;height:100%;background:{GOLD};border-radius:8px}}
.bar .n{{text-align:right;color:{GOLD_L}}}
.bar.hl .l,.bar.hl .n{{font-weight:500;color:#fff}}
.legend{{display:grid;grid-template-columns:62px 1fr 1fr 64px;gap:10px;font-size:15px;color:{MUTED};letter-spacing:1px;text-transform:uppercase}}
.rules{{list-style:none}}
.rules li{{font-size:20px;line-height:1.25;padding:7px 0 7px 40px;position:relative;border-bottom:1px solid #2a3d63;color:#dfe5f0}}
.rules li:last-child{{border:none}}
.rules li:before{{content:'✓';position:absolute;left:4px;top:7px;color:{GREEN_L};font-weight:500}}
.rules li b{{color:#fff;font-weight:500}}
.dots{{display:grid;grid-template-columns:repeat(20,1fr);gap:7px;margin:14px 0 16px}}
.dots i{{display:block;aspect-ratio:1;border-radius:50%;background:{GREEN}}}
.dots i.r{{background:#c9605a;transform:scale(.7)}}
.dots i.z{{background:#3a4d74}}
.months{{display:grid;grid-template-columns:repeat(8,1fr);gap:8px;margin-top:6px}}
.m{{height:52px;border:2px solid #3a4d74;border-radius:10px;display:flex;align-items:flex-end;justify-content:center;padding-bottom:4px}}
.m span{{font-size:13.5px;color:{MUTED};letter-spacing:.5px}}
.m:last-child{{border-color:{GOLD};background:rgba(232,176,75,.12)}}
.m:last-child span{{color:{GOLD_L}}}
footer{{display:flex;justify-content:space-between;align-items:center;margin-top:22px;font-size:19px;color:{MUTED}}}
footer .q{{font-family:'Cormorant Garamond';font-style:italic;font-size:34px;color:{INK}}}
</style></head><body><div class="wrap">
<header>
  <div>
    <h1>Protect the capital. <em>Win small. Every day.</em></h1>
    <div class="sub">Follow the plan with discipline and walk out of the rat race: <b>financially free by the first week of May 2029.</b></div>
  </div>
  <div class="count"><div class="big">~{SESSIONS}</div><div class="lab">trading sessions to go</div></div>
</header>
<div class="art">{art()}</div>
<div class="cards">
  <div class="card">
    <h3>1 · Capital first</h3>
    <h2>A loss you avoid is a gain you never have to make.</h2>
    <div class="legend"><span>Lose</span><span></span><span>Need to recover</span><span></span></div>
    {recovery_bars()}
  </div>
  <div class="card">
    <h3>2 · The plan, every day</h3>
    <h2>Same rules. Every session.</h2>
    <ul class="rules">
      <li>Risk <b>1% per trade</b>: ₹{inr(RISK)} on ₹{inr(CAPITAL)}</li>
      <li><b>Stop for the day</b> at −₹{inr(RISK * 2)} or 2 losses</li>
      <li>Max <b>3 trades</b>. Only the five A+ setups</li>
      <li>Stop-loss placed <b>before</b> entry. Never widened</li>
      <li>Flat by <b>14:45</b> on expiry Tuesday</li>
    </ul>
  </div>
  <div class="card">
    <h3>3 · Small daily wins</h3>
    <h2>Singles, not sixes.</h2>
    <div class="dots">{"".join('<i class="r"></i>' if k in (6, 13, 17, 24, 31, 38) else ('<i class="z"></i>' if k in (9, 27) else '<i></i>') for k in range(40))}</div>
    <p>Green = a small win. Red = a <b>small</b>, planned loss. Grey = no setup, no trade. Not one day needs to be a jackpot; <b>no day</b> is allowed to be a disaster.</p>
  </div>
  <div class="card">
    <h3>4 · Discipline tracker</h3>
    <p>Tick a month only if <b>every day</b> followed the plan.</p>
    <div class="months">{month_grid()}<div class="m"><span>May 29 ★</span></div></div>
  </div>
</div>
<footer><span class="q">“The market pays the patient. Stay in the game long enough to win it.”</span>
<span>Plan &gt; prediction · Process &gt; P&amp;L</span></footer>
</div></body></html>"""


def main():
    page = HERE / "board.html"
    page.write_text(html(), encoding="utf-8")
    png = HERE / "Vision_Board_May_2029.png"
    pdf = HERE / "Vision_Board_May_2029.pdf"
    common = [CHROME, "--headless=new", "--no-sandbox", "--disable-gpu", "--hide-scrollbars",
              "--allow-file-access-from-files", "--virtual-time-budget=4000"]
    subprocess.run(common + [f"--window-size={W},{H}", f"--screenshot={png}", page.as_uri()], check=True,
                   capture_output=True)
    # PDF: A3 landscape (420x297 mm = 1587x1123 CSS px)
    pw, ph = 1587, 1123
    sc = min(pw / W, ph / H)
    pp = HERE / "board_print.html"
    pp.write_text(html().replace("<style>", f"<style>@page{{size:420mm 297mm;margin:0}}", 1).replace(
        "<body>", f'<body style="width:{pw}px;height:{ph}px;background:{NAVY}"><div style="transform:scale({sc});'
                  f'transform-origin:0 0;width:{W}px;height:{H}px">').replace("</body>", "</div></body>"),
        encoding="utf-8")
    subprocess.run(common + ["--no-pdf-header-footer", f"--print-to-pdf={pdf}", pp.as_uri()], check=True,
                   capture_output=True)
    pp.unlink()
    print("wrote", png.name, pdf.name)


if __name__ == "__main__":
    main()
