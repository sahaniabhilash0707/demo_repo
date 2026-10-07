"""Trading vision board: protect capital, small daily wins, out of the rat race by May 2029.

Run:  python3 build_board.py   -> Vision_Board_May_2029.png / .pdf
The canvas is A3 landscape at 150 dpi (2480 x 1754), so the PNG and the PDF fill the page edge to edge.
"""
import subprocess
from pathlib import Path

HERE = Path(__file__).parent
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
W, H = 2480, 1754

PAPER, INK, SOFT, MUTED, RULE = "#f3efe7", "#14161a", "#4a4d55", "#8d897f", "#d9d3c7"
GREEN, RED, GOLD = "#1d6a51", "#b9473b", "#b5843a"

CAPITAL = 270000          # trading capital in the Guruji manual's risk card
RISK = CAPITAL // 100     # 1% per trade
SESSIONS = 640            # approx. NSE trading sessions, 8 Oct 2026 - 7 May 2029
MONTHS = ([f"{m} 26" for m in ("Oct", "Nov", "Dec")]
          + [f"{m} {y}" for y in ("27", "28") for m in
             ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")]
          + [f"{m} 29" for m in ("Jan", "Feb", "Mar", "Apr")])


def inr(n):
    s = str(n)
    head, tail = s[:-3], s[-3:]
    parts = []
    while len(head) > 2:
        parts.insert(0, head[-2:])
        head = head[:-2]
    return ",".join(([head] if head else []) + parts + [tail])


# ------------------------------------------------------------------ the art
def art():
    w, h = 1560, 1030
    floor, x0, x1, ytop = 820, 330, 1440, 150

    def mx(m):  # month index (0 = Oct 2026, 31 = May 2029) -> x
        return x0 + m / 31 * (x1 - x0)

    o = [f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid meet">',
         '<defs><linearGradient id="fill" x1="0" y1="0" x2="0" y2="1">'
         f'<stop offset="0" stop-color="{GREEN}" stop-opacity=".16"/>'
         f'<stop offset="1" stop-color="{GREEN}" stop-opacity="0"/></linearGradient></defs>']

    # the floor: capital
    o.append(f'<line x1="40" y1="{floor}" x2="1540" y2="{floor}" stroke="{INK}" stroke-width="2"/>')
    o.append(f'<text x="1540" y="{floor + 84}" text-anchor="end" class="cap">CAPITAL · THE FLOOR YOU NEVER BREAK</text>')
    o.append(f'<text x="{x0 - 10}" y="{floor + 44}" text-anchor="end" class="cap muted">OCT 2026</text>')
    for m, lab in ((0, ""), (3, "2027"), (15, "2028"), (27, "2029")):
        x = mx(m)
        o.append(f'<line x1="{x:.0f}" y1="{floor}" x2="{x:.0f}" y2="{floor + 14}" stroke="{INK}" stroke-width="2"/>')
        o.append(f'<text x="{x + 8:.0f}" y="{floor + 44}" class="cap muted">{lab}</text>')

    # the rat race: a closed loop
    cx, cy = 190, 690
    for r, op in ((122, 1), (98, .7), (74, .45), (50, .25)):
        o.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{MUTED}" stroke-width="2" opacity="{op}"/>')
    o.append(f'<text x="{cx}" y="{cy - 150}" text-anchor="middle" class="it">the rat race</text>')
    o.append(f'<text x="{cx}" y="{cy - 118}" text-anchor="middle" class="cap muted">SALARY · BILLS · REPEAT</text>')

    # the gamble: spike, then a crash through the floor
    o.append(f'<path d="M{x0} {floor} L392 640 L425 700 L486 430 L520 500 L575 210 L606 268 L640 120 '
             f'L668 228 L700 470 L742 760 L778 990" fill="none" stroke="{MUTED}" stroke-width="2" '
             'stroke-dasharray="7 7"/>')
    o.append('<text x="652" y="96" class="it muted">the gamble</text>')
    o.append(f'<circle cx="778" cy="990" r="7" fill="{RED}"/>')
    o.append('<text x="798" y="984" class="num red">−46%</text>')
    o.append('<text x="798" y="1018" class="cap red">NEEDS +85% JUST TO GET BACK</text>')

    # the plan: small steps out of the loop, a few small red ones, never below the floor
    n, dips = 62, {6, 13, 21, 28, 34, 41, 47, 55}
    up = (floor - ytop) / (n - len(dips) * 1.35)
    dx = (x1 - x0) / n
    pts, segs, y = [(x0, floor)], [], floor
    for i in range(n):
        y = y + up * 0.35 if i in dips else y - up
        a, b = x0 + i * dx, x0 + (i + 1) * dx
        pts += [(a, y), (b, y)]
        segs.append((a, b, y, i in dips))
    line = "M" + " L".join(f"{a:.1f} {b:.1f}" for a, b in pts)
    o.append(f'<path d="{line} L{x1} {floor} Z" fill="url(#fill)"/>')
    o.append(f'<path d="M{cx + 61} {cy + 106} Q {cx + 100} {floor} {x0} {floor}" fill="none" stroke="{GREEN}" '
             'stroke-width="4" stroke-linecap="round"/>')
    o.append(f'<path d="{line}" fill="none" stroke="{GREEN}" stroke-width="4" stroke-linejoin="round"/>')
    for a, b, yy, red in segs:
        if red:
            o.append(f'<line x1="{a:.1f}" y1="{yy:.1f}" x2="{b:.1f}" y2="{yy:.1f}" stroke="{RED}" stroke-width="5"/>')
    o.append(f'<circle cx="{cx + 61}" cy="{cy + 106}" r="7" fill="{GREEN}"/>')
    o.append(f'<text x="1010" y="610" class="it green">~{SESSIONS} small steps.</text>')
    o.append('<text x="1010" y="648" class="cap soft">A FEW SMALL RED ONES · NEVER A CLIFF</text>')

    # the destination
    ex, ey = x1, segs[-1][2]
    o.append(f'<circle cx="{ex}" cy="{ey}" r="30" fill="none" stroke="{GOLD}" stroke-width="2"/>')
    o.append(f'<circle cx="{ex}" cy="{ey}" r="12" fill="{GOLD}"/>')
    o.append(f'<text x="{ex - 50}" y="{ey - 62}" text-anchor="end" class="cap gold">FIRST WEEK OF MAY 2029</text>')
    o.append(f'<text x="{ex - 50}" y="{ey - 14}" text-anchor="end" class="big">Financially free</text>')
    o.append('</svg>')
    return "\n".join(o)


# ------------------------------------------------------------------ html
def recovery():
    rows = [(10, 11), (20, 25), (30, 43), (46, 85), (50, 100)]
    return "".join(
        f'<div class="rec{" hl" if loss == 46 else ""}"><span>−{loss}%</span>'
        f'<i><b class="l" style="width:{loss}%"></b></i><i><b class="n" style="width:{need}%"></b></i>'
        f'<span class="r">+{need}%</span></div>' for loss, need in rows)


def dots():
    red, flat = {5, 12, 19, 23, 31, 38, 44}, {9, 27, 36}
    return "".join('<u class="r"></u>' if k in red else '<u class="o"></u>' if k in flat else '<u></u>'
                   for k in range(48))


def html():
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>
@page{{size:{W}px {H}px;margin:0}}
@font-face{{font-family:'Cormorant';font-weight:500;src:url('fonts/CormorantGaramond-500.ttf');}}
@font-face{{font-family:'Cormorant';font-weight:500;font-style:italic;src:url('fonts/CormorantGaramond-500i.ttf');}}
@font-face{{font-family:'Cormorant';font-weight:600;src:url('fonts/CormorantGaramond-600.ttf');}}
@font-face{{font-family:'Inter';font-weight:300;src:url('fonts/Inter-Light.otf');}}
@font-face{{font-family:'Inter';font-weight:400;src:url('fonts/Inter-Regular.otf');}}
@font-face{{font-family:'Inter';font-weight:500;src:url('fonts/Inter-Medium.otf');}}
@font-face{{font-family:'Inter';font-weight:600;src:url('fonts/Inter-SemiBold.otf');}}
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{width:{W}px;height:{H}px;background:{PAPER};color:{INK};font-family:'Inter';overflow:hidden;
  -webkit-print-color-adjust:exact;print-color-adjust:exact}}
body{{display:grid;grid-template-rows:1fr auto auto;padding:80px 96px 56px}}
.top{{display:grid;grid-template-columns:720px 1fr;gap:48px;min-height:0;padding-bottom:30px}}
.top>div:first-child{{display:flex;flex-direction:column}}
.eyebrow{{font-size:19px;letter-spacing:5px;font-weight:500;color:{MUTED}}}
h1{{font-family:'Cormorant';font-weight:600;font-size:140px;line-height:.92;letter-spacing:-2px;margin-top:28px}}
h1 em{{font-style:italic;font-weight:500;color:{GREEN};display:block;margin-top:14px}}
.lede{{font-size:29px;line-height:1.5;color:{SOFT};font-weight:300;margin-top:36px;max-width:600px}}
.lede b{{font-weight:500;color:{INK}}}
.count{{display:flex;align-items:baseline;gap:22px;margin-top:auto;padding-top:26px;border-top:1.5px solid {INK}}}
.count .n{{font-family:'Cormorant';font-size:104px;font-weight:600;line-height:.8;color:{GOLD}}}
.count .t{{font-size:19px;letter-spacing:4px;font-weight:500;line-height:1.5;color:{SOFT}}}
.art svg{{width:100%;height:100%;display:block}}
svg .cap{{font-family:'Inter';font-size:17px;letter-spacing:3px;font-weight:500;fill:{INK}}}
svg .it{{font-family:'Cormorant';font-style:italic;font-weight:500;font-size:36px;fill:{INK}}}
svg .big{{font-family:'Cormorant';font-style:italic;font-weight:500;font-size:64px;fill:{INK}}}
svg .num{{font-family:'Cormorant';font-weight:600;font-size:40px}}
svg .muted{{fill:{MUTED}}} svg .soft{{fill:{SOFT}}} svg .red{{fill:{RED}}} svg .green{{fill:{GREEN}}} svg .gold{{fill:{GOLD}}}
.cols{{display:grid;grid-template-columns:repeat(4,1fr);gap:72px;border-top:1.5px solid {INK};padding-top:30px;margin-top:12px}}
.k{{font-size:17px;letter-spacing:4px;font-weight:600;color:{GREEN}}}
h2{{font-family:'Cormorant';font-weight:600;font-size:46px;line-height:1.02;margin:10px 0 20px;letter-spacing:-.3px}}
.rec{{display:grid;grid-template-columns:70px 1fr 1fr 70px;gap:12px;align-items:center;font-size:19px;color:{SOFT};margin:11px 0;
  font-variant-numeric:tabular-nums}}
.rec i{{height:6px;background:{RULE};display:block}}
.rec b{{display:block;height:100%}}
.rec .l{{background:{RED}}} .rec .n{{background:{INK}}}
.rec .r{{text-align:right}}
.rec.hl{{color:{INK};font-weight:600}}
.leg{{display:grid;grid-template-columns:70px 1fr 1fr 70px;gap:12px;font-size:14px;letter-spacing:2.5px;color:{MUTED};font-weight:500}}
ol{{list-style:none;counter-reset:r}}
ol li{{counter-increment:r;font-size:21px;line-height:1.35;color:{SOFT};padding:11px 0 11px 46px;position:relative;border-bottom:1px solid {RULE}}}
ol li:first-child{{padding-top:0}} ol li:first-child:before{{top:1px}}
ol li:last-child{{border:none}}
ol li:before{{content:counter(r,decimal-leading-zero);position:absolute;left:0;top:13px;font-size:15px;font-weight:600;color:{GREEN};letter-spacing:1px}}
ol li b{{color:{INK};font-weight:600}}
.dots{{display:grid;grid-template-columns:repeat(12,1fr);gap:12px 0;justify-items:start;margin:4px 0 20px}}
.dots u{{width:22px;height:22px;border-radius:50%;background:{GREEN};display:block}}
.dots u.r{{background:{RED};transform:scale(.55)}}
.dots u.o{{background:none;border:1.5px solid {MUTED}}}
.p{{font-size:20px;line-height:1.5;color:{SOFT};font-weight:300}}
.p b{{color:{INK};font-weight:600}}
.months{{display:grid;grid-template-columns:repeat(8,1fr);gap:8px;margin:2px 0 20px}}
.months div{{height:54px;border:1.5px solid {RULE};font-size:13px;line-height:1.25;color:{MUTED};padding:6px 7px;letter-spacing:.4px}}
.months div b{{display:block;font-weight:600;color:{SOFT}}}
.months div:last-child{{border-color:{GOLD};background:{GOLD};color:#fff}}
.months div:last-child b{{color:#fff}}
footer{{display:flex;justify-content:space-between;align-items:baseline;margin-top:28px;padding-top:18px;border-top:1px solid {RULE}}}
footer .q{{font-family:'Cormorant';font-style:italic;font-size:36px}}
footer .s{{font-size:16px;letter-spacing:4px;font-weight:500;color:{MUTED}}}
</style></head><body>
<section class="top">
  <div>
    <div class="eyebrow">THE PLAN · OCT 2026 → MAY 2029</div>
    <h1>Protect the capital.<em>Win small.<br>Every day.</em></h1>
    <p class="lede">Follow the plan with discipline and walk out of the rat race. <b>Financially free by the first
      week of May 2029.</b></p>
    <div class="count"><span class="n">~{SESSIONS}</span><span class="t">TRADING SESSIONS<br>TO GO</span></div>
  </div>
  <div class="art">{art()}</div>
</section>
<section class="cols">
  <div><div class="k">01 · CAPITAL FIRST</div><h2>A loss avoided is a gain you never have to make.</h2>
    <div class="leg"><span>LOSE</span><span></span><span>TO RECOVER</span><span></span></div>{recovery()}</div>
  <div><div class="k">02 · THE PLAN</div><h2>Same rules. Every session.</h2>
    <ol><li>Risk <b>1% per trade</b>: ₹{inr(RISK)} on ₹{inr(CAPITAL)}</li>
      <li><b>Stop for the day</b> at −₹{inr(RISK * 2)} or two losses</li>
      <li>At most <b>three trades</b>, only the five A+ setups</li>
      <li>Stop-loss set <b>before</b> entry, never widened</li>
      <li>Flat by <b>14:45</b> on expiry Tuesday</li></ol></div>
  <div><div class="k">03 · SMALL DAILY WINS</div><h2>Singles, not sixes.</h2>
    <div class="dots">{dots()}</div>
    <p class="p">Green, a small win. Red, a <b>small</b> planned loss. Hollow, no setup and no trade.
      No day needs to be a jackpot. <b>No day</b> is allowed to be a disaster.</p></div>
  <div><div class="k">04 · DISCIPLINE</div><h2>Tick a month only if every day kept the plan.</h2>
    <div class="months">{"".join(f"<div><b>{m[:3]}</b>&#8217;{m[-2:]}</div>" for m in MONTHS)}<div><b>May</b>&#8217;29</div></div></div>
</section>
<footer><span class="q">The market pays the patient. Stay in the game long enough to win it.</span>
  <span class="s">PLAN OVER PREDICTION · PROCESS OVER P&amp;L</span></footer>
</body></html>"""


def main():
    page = HERE / "board.html"
    page.write_text(html(), encoding="utf-8")
    png = HERE / "Vision_Board_May_2029.png"
    pdf = HERE / "Vision_Board_May_2029.pdf"
    common = [CHROME, "--headless=new", "--no-sandbox", "--disable-gpu", "--hide-scrollbars",
              "--allow-file-access-from-files", "--virtual-time-budget=4000"]
    # PNG via Playwright, so the viewport is exactly W x H (headless --window-size crops the bottom)
    js = (f"const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();"
          f"const p=await b.newPage({{viewport:{{width:{W},height:{H}}}}});await p.goto('{page.as_uri()}');"
          f"await p.waitForTimeout(800);await p.screenshot({{path:'{png}'}});await b.close();}})();")
    npm_root = subprocess.run(["npm", "root", "-g"], capture_output=True, text=True).stdout.strip()
    subprocess.run(["node", "-e", js], check=True, env={"NODE_PATH": npm_root, "PATH": "/usr/bin:/usr/local/bin",
                                                         "PLAYWRIGHT_BROWSERS_PATH": "/opt/pw-browsers"})
    subprocess.run(common + ["--no-pdf-header-footer", f"--print-to-pdf={pdf}", page.as_uri()], check=True,
                   capture_output=True)
    page.unlink()
    print("wrote", png.name, pdf.name)


if __name__ == "__main__":
    main()
