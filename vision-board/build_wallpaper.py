"""Dark desktop wallpaper: 15 points a week, then stop.

Run:  python3 build_wallpaper.py   -> Wallpaper_15_Points_a_Week.png (2880 x 1800, 16:10)
Layout keeps the left ~16% clear for desktop icons and the bottom ~6% clear for the taskbar.
"""
import subprocess
from pathlib import Path

HERE = Path(__file__).parent
W, H = 2880, 1800
SAFE_L, SAFE_B = 500, 120          # px kept free for icons (left) and taskbar (bottom)

BG, INK, SOFT, MUTED, RULE = "#0b0e14", "#eef0f4", "#a9afbd", "#6b7282", "#252b38"
GREEN, GREEN_L, RED, GOLD = "#3fbf93", "#7fe0bf", "#e0645a", "#e3b25c"
TARGET = 15


def art():
    """Loop (rat race) -> small steps above the capital floor -> May 2029; the gamble crashes through."""
    w, h = 1240, 820
    floor, x0, x1, ytop = 640, 270, 1150, 120
    o = [f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg">',
         '<defs><linearGradient id="f" x1="0" y1="0" x2="0" y2="1">'
         f'<stop offset="0" stop-color="{GREEN}" stop-opacity=".22"/><stop offset="1" stop-color="{GREEN}" '
         'stop-opacity="0"/></linearGradient>'
         '<radialGradient id="g" cx=".5" cy=".5" r=".5">'
         f'<stop offset="0" stop-color="{GOLD}" stop-opacity=".45"/><stop offset="1" stop-color="{GOLD}" '
         'stop-opacity="0"/></radialGradient></defs>']
    o.append(f'<line x1="30" y1="{floor}" x2="1230" y2="{floor}" stroke="{SOFT}" stroke-width="2"/>')
    o.append(f'<text x="1230" y="{floor + 42}" text-anchor="end" class="cap">CAPITAL · THE FLOOR YOU NEVER BREAK</text>')
    cx, cy = 150, 530
    for r, op in ((100, .9), (80, .6), (60, .38), (40, .2)):
        o.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" stroke="{MUTED}" stroke-width="2" opacity="{op}"/>')
    o.append(f'<text x="{cx}" y="{cy - 124}" text-anchor="middle" class="it soft">the rat race</text>')
    # the gamble, as it actually happened before
    o.append(f'<path d="M{x0} {floor} L318 520 L345 560 L392 360 L420 410 L466 190 L492 236 L520 120 '
             f'L545 210 L572 420 L606 650 L636 800" fill="none" stroke="{RED}" stroke-width="2.5" '
             'stroke-dasharray="8 8" opacity=".75"/>')
    o.append('<text x="500" y="112" text-anchor="end" class="cap red">A FEW WINS → OPTION BUYING → THE FALL</text>')
    o.append(f'<circle cx="636" cy="800" r="7" fill="{RED}"/>')
    o.append(f'<text x="656" y="790" class="cap red">−46% · NEVER AGAIN</text>')
    # the plan: small weekly steps
    n, dips = 48, {6, 13, 21, 29, 36, 43}
    up = (floor - ytop) / (n - len(dips) * 1.35)
    dx = (x1 - x0) / n
    pts, segs, y = [(x0, floor)], [], floor
    for i in range(n):
        y = y + up * 0.35 if i in dips else y - up
        a, b = x0 + i * dx, x0 + (i + 1) * dx
        pts += [(a, y), (b, y)]
        segs.append((a, b, y, i in dips))
    line = "M" + " L".join(f"{a:.1f} {b:.1f}" for a, b in pts)
    o.append(f'<path d="{line} L{x1} {floor} Z" fill="url(#f)"/>')
    o.append(f'<path d="M{cx + 50} {cy + 87} Q {cx + 85} {floor} {x0} {floor}" fill="none" stroke="{GREEN}" '
             'stroke-width="4" stroke-linecap="round"/>')
    o.append(f'<path d="{line}" fill="none" stroke="{GREEN}" stroke-width="4" stroke-linejoin="round"/>')
    for a, b, yy, red in segs:
        if red:
            o.append(f'<line x1="{a:.1f}" y1="{yy:.1f}" x2="{b:.1f}" y2="{yy:.1f}" stroke="{RED}" stroke-width="5"/>')
    o.append(f'<text x="800" y="500" class="it green">one small week at a time</text>')
    ex, ey = x1, segs[-1][2]
    o.append(f'<circle cx="{ex}" cy="{ey}" r="90" fill="url(#g)"/>')
    o.append(f'<circle cx="{ex}" cy="{ey}" r="26" fill="none" stroke="{GOLD}" stroke-width="2"/>')
    o.append(f'<circle cx="{ex}" cy="{ey}" r="11" fill="{GOLD}"/>')
    o.append(f'<text x="{ex - 44}" y="{ey - 56}" text-anchor="end" class="cap gold">FIRST WEEK OF MAY 2029</text>')
    o.append(f'<text x="{ex - 44}" y="{ey - 12}" text-anchor="end" class="big">Out of the rat race</text>')
    o.append('</svg>')
    return "\n".join(o)


def fisherman():
    """Line art: a fisherman waiting on a jetty; a fish is about to take the bait."""
    st = f'stroke="{SOFT}" stroke-width="3" fill="none" stroke-linecap="round" stroke-linejoin="round"'
    o = ['<svg viewBox="0 0 440 300" xmlns="http://www.w3.org/2000/svg">']
    # jetty and posts
    o.append(f'<path d="M10 140 L170 140 M30 140 L30 196 M150 140 L150 196" {st}/>')
    # water surface and depth lines
    o.append(f'<path d="M10 176 Q 40 170 70 176 T 130 176 T 190 176 T 250 176 T 310 176 T 370 176 T 430 176" '
             f'stroke="#4fa3ff" stroke-width="2.5" fill="none" opacity=".7"/>')
    for y, op in ((214, .25), (250, .15), (284, .1)):
        o.append(f'<path d="M60 {y} Q 120 {y - 5} 180 {y} T 300 {y} T 420 {y}" stroke="#4fa3ff" stroke-width="1.5" '
                 f'fill="none" opacity="{op}"/>')
    # the fisherman, a still seated silhouette
    fig = "#c9cfdb"
    o.append(f'<ellipse cx="97" cy="57" rx="25" ry="4.5" fill="{fig}"/>')
    o.append(f'<path d="M85 57 Q 87 38 97 38 Q 107 38 109 57 Z" fill="{fig}"/>')
    o.append(f'<circle cx="98" cy="70" r="11" fill="{fig}"/>')
    o.append(f'<path d="M86 84 Q 102 78 109 96 L113 136 L84 139 Q 78 112 86 84 Z" fill="{fig}"/>')
    o.append(f'<path d="M104 94 L124 116" stroke="{fig}" stroke-width="8" stroke-linecap="round"/>')
    o.append(f'<path d="M94 134 L134 136" stroke="{fig}" stroke-width="13" stroke-linecap="round"/>')
    o.append(f'<path d="M133 137 L137 168" stroke="{fig}" stroke-width="9" stroke-linecap="round"/>')
    # rod, line, float
    o.append(f'<path d="M124 116 Q 225 40 340 22" {st}/>')
    o.append(f'<path d="M340 22 L340 172" stroke="{SOFT}" stroke-width="1.5" opacity=".8"/>')
    o.append(f'<path d="M340 186 L340 248" stroke="{SOFT}" stroke-width="1.5" opacity=".6"/>')
    o.append(f'<ellipse cx="340" cy="179" rx="6" ry="9" fill="{RED}"/>')
    # hook and bait
    o.append(f'<path d="M340 248 L340 262 Q 340 272 332 270" stroke="{SOFT}" stroke-width="2" fill="none"/>')
    o.append(f'<circle cx="345" cy="258" r="6" fill="{GOLD}"/>')
    # the fish, mouth open, about to bite
    o.append(f'<path d="M322 258 Q 300 240 268 252 Q 250 258 268 266 Q 300 276 322 260" stroke="{GREEN_L}" '
             'stroke-width="3" fill="#3fbf93" fill-opacity=".18" stroke-linejoin="round"/>')
    o.append(f'<path d="M268 252 L246 240 L250 259 L246 276 L268 266" stroke="{GREEN_L}" stroke-width="3" fill="none" '
             'stroke-linejoin="round"/>')
    o.append(f'<circle cx="308" cy="252" r="2.6" fill="{GREEN_L}"/>')
    for x, y, r in ((316, 232, 3), (322, 218, 2.4), (318, 204, 1.8)):
        o.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="none" stroke="{GREEN_L}" stroke-width="1.3" opacity=".7"/>')
    o.append('</svg>')
    return "".join(o)


def meter():
    """This week's points: fill to the target, then the greed zone the past account died in."""
    mx = 25
    pct = TARGET / mx * 100
    ticks = "".join(f'<span style="left:{v / mx * 100}%">{v}</span>' for v in (0, 5, 10, 15, 20, 25))
    return f"""<div class="meter">
  <div class="bar"><div class="ok" style="width:{pct}%"></div><div class="greed" style="left:{pct}%"></div>
    <div class="flag" style="left:{pct}%"><b>{TARGET} PTS · TARGET HIT</b><i>CLOSE THE DAY. CLOSE THE WEEK.</i></div>
    <div class="gz" style="left:{pct}%">GREED ZONE · WHERE THE LAST ACCOUNT DIED</div></div>
  <div class="ticks">{ticks}</div>
</div>"""


def dots():
    """Two rows of sessions: mostly small wins, a few small planned losses, some days with no trade."""
    red, flat = {5, 12, 19, 26, 33, 37}, {9, 23, 30}
    return "".join('<u class="r"></u>' if k in red else '<u class="o"></u>' if k in flat else '<u></u>'
                   for k in range(40))


def html():
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:'Cormorant';font-weight:500;src:url('fonts/CormorantGaramond-500.ttf');}}
@font-face{{font-family:'Cormorant';font-weight:500;font-style:italic;src:url('fonts/CormorantGaramond-500i.ttf');}}
@font-face{{font-family:'Cormorant';font-weight:600;src:url('fonts/CormorantGaramond-600.ttf');}}
@font-face{{font-family:'Inter';font-weight:300;src:url('fonts/Inter-Light.otf');}}
@font-face{{font-family:'Inter';font-weight:400;src:url('fonts/Inter-Regular.otf');}}
@font-face{{font-family:'Inter';font-weight:500;src:url('fonts/Inter-Medium.otf');}}
@font-face{{font-family:'Inter';font-weight:600;src:url('fonts/Inter-SemiBold.otf');}}
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{width:{W}px;height:{H}px;overflow:hidden;color:{INK};font-family:'Inter'}}
body{{background:radial-gradient(ellipse 60% 70% at 80% 30%, #142033 0%, rgba(11,14,20,0) 70%),
  radial-gradient(ellipse 50% 50% at 40% 90%, #10261f 0%, rgba(11,14,20,0) 70%), {BG};
  padding:130px 150px {SAFE_B + 70}px {SAFE_L + 60}px;display:grid;grid-template-rows:1fr auto;gap:60px}}
.top{{display:grid;grid-template-columns:1fr 1240px;gap:70px;align-items:center}}
.wait{{display:grid;grid-template-columns:400px 1fr;gap:40px;align-items:center;margin-bottom:24px}}
.wait svg{{width:400px;display:block}}
.wk{{font-size:20px;letter-spacing:6px;font-weight:600;color:{GREEN}}}
.wt{{font-family:'Cormorant';font-weight:600;font-size:62px;line-height:1.02;margin-top:12px;color:{INK}}}
.wt em{{font-style:italic;font-weight:500;color:{GREEN_L}}}
.wait p{{font-size:24px;line-height:1.45;color:{SOFT};font-weight:300;margin-top:16px}}
.eyebrow{{font-size:24px;letter-spacing:7px;font-weight:500;color:{MUTED}}}
h1{{font-family:'Cormorant';font-weight:600;line-height:.86;margin-top:26px;letter-spacing:-3px}}
h1 .n{{font-size:360px;color:{GOLD};display:block;line-height:.78;font-variant-numeric:lining-nums;font-feature-settings:"lnum" 1}}
h1 .w{{font-size:132px;display:block;margin-top:10px}}
h1 em{{font-size:132px;font-style:italic;font-weight:500;color:{GREEN};display:block;margin-top:18px}}
.lede{{font-size:34px;line-height:1.5;color:{SOFT};font-weight:300;margin-top:40px;max-width:860px}}
.lede b{{color:{INK};font-weight:500}}
.singles{{margin-top:54px;padding-top:30px;border-top:1px solid {RULE};max-width:900px}}
.sh{{font-family:'Cormorant';font-style:italic;font-weight:500;font-size:54px;color:{GREEN_L};white-space:nowrap;margin-bottom:22px}}
.lg{{display:flex;gap:44px;margin-top:22px;font-size:15px;letter-spacing:2.5px;color:{MUTED};font-weight:500}}
.lg span{{display:flex;align-items:center;gap:12px}}
.lg u{{width:16px;height:16px;border-radius:50%;background:{GREEN};display:block}}
.lg u.r{{background:{RED};transform:scale(.6)}}
.lg u.o{{background:none;border:2px solid {MUTED}}}
.dots{{display:grid;grid-template-columns:repeat(20,1fr);gap:16px 0;justify-items:start}}
.dots u{{width:26px;height:26px;border-radius:50%;background:{GREEN};display:block}}
.dots u.r{{background:{RED};transform:scale(.5)}}
.dots u.o{{background:none;border:2px solid {MUTED}}}
svg .cap{{font-family:'Inter';font-size:17px;letter-spacing:3.5px;font-weight:500;fill:{SOFT}}}
svg .it{{font-family:'Cormorant';font-style:italic;font-weight:500;font-size:34px}}
svg .big{{font-family:'Cormorant';font-style:italic;font-weight:500;font-size:56px;fill:{INK}}}
svg .soft{{fill:{SOFT}}} svg .red{{fill:{RED}}} svg .green{{fill:{GREEN_L}}} svg .gold{{fill:{GOLD}}}
.bottom{{display:grid;grid-template-columns:1.25fr 1fr;gap:110px;align-items:end;border-top:1.5px solid {RULE};padding-top:46px}}
.k{{font-size:20px;letter-spacing:6px;font-weight:600;color:{GREEN};margin-bottom:64px}}
.meter .bar{{position:relative;height:22px;background:{RULE};border-radius:11px}}
.meter .ok{{position:absolute;left:0;top:0;bottom:0;background:linear-gradient(90deg,#1f6f56,{GREEN});border-radius:11px 0 0 11px}}
.meter .greed{{position:absolute;right:0;top:0;bottom:0;border-radius:0 11px 11px 0;
  background:repeating-linear-gradient(135deg,rgba(224,100,90,.55) 0 10px,rgba(224,100,90,.12) 10px 20px)}}
.meter .flag{{position:absolute;bottom:-14px;width:4px;height:50px;background:{GOLD};transform:translateX(-2px)}}
.meter .flag b{{position:absolute;bottom:96px;left:50%;transform:translateX(-50%);white-space:nowrap;font-size:24px;
  letter-spacing:3px;color:{GOLD};font-weight:600}}
.meter .flag i{{position:absolute;bottom:62px;left:50%;transform:translateX(-50%);white-space:nowrap;font-style:normal;
  font-size:17px;letter-spacing:3px;color:{INK};font-weight:500}}
.meter .gz{{position:absolute;top:78px;right:0;white-space:nowrap;font-size:15px;letter-spacing:2.5px;color:{RED};font-weight:600;text-align:right;
  padding-left:20px}}
.ticks{{position:relative;height:30px;margin-top:14px}}
.ticks span{{position:absolute;transform:translateX(-50%);font-size:17px;color:{MUTED};font-variant-numeric:tabular-nums}}
.ticks span:first-child{{transform:none}} .ticks span:last-child{{transform:translateX(-100%)}}
.rules{{list-style:none;counter-reset:r}}
.rules li{{counter-increment:r;font-size:28px;line-height:1.3;color:{SOFT};padding:15px 0 15px 62px;position:relative;
  border-bottom:1px solid {RULE}}}
.rules li:last-child{{border:none;padding-bottom:0}}
.rules li:before{{content:counter(r,decimal-leading-zero);position:absolute;left:0;top:20px;font-size:19px;font-weight:600;
  letter-spacing:1px;color:{GREEN}}}
.rules li b{{color:{INK};font-weight:600}}
</style></head><body>
<section class="top">
  <div>
    <div class="eyebrow">THE GOAL · NO DEVIATION</div>
    <h1><span class="n">{TARGET}</span><span class="w">points a week.</span><em>Then stop.</em></h1>
    <p class="lede">Every step away from this plan is a step toward disaster. <b>A few wins, then option buying,
      then the fall: it has happened before.</b> This is the last chance out of the rat race. Don't spend it.</p>
    <div class="singles"><div class="sh">Singles, not sixes.</div>
      <div class="dots">{dots()}</div>
      <div class="lg"><span><u></u>SMALL WIN</span><span><u class="r"></u>SMALL PLANNED LOSS</span><span><u class="o"></u>NO SETUP, NO TRADE</span></div></div>
  </div>
  <div class="right">
    <div class="wait">{fisherman()}
      <div><div class="wk">THE REAL SKILL</div>
        <div class="wt">The edge isn't the strategy.<br><em>It's the patience to wait.</em></div>
        <p>Self-control to sit through the noise, and trade only when the best setup comes at the right time.
          The fisherman doesn't chase the fish. He waits, still, until it takes the bait.</p></div></div>
    <div class="art">{art()}</div></div>
</section>
<section class="bottom">
  <div><div class="k">THIS WEEK ONLY</div>{meter()}</div>
  <ol class="rules">
    <li>Think <b>only about this week</b>. Not the month, not the dream.</li>
    <li><b>Target hit? Close the day.</b> No “one more trade”.</li>
    <li>A winning streak is a warning, <b>not a licence</b> to buy options.</li>
    <li>Protect the capital. <b>The plan is the only edge.</b></li>
  </ol>
</section>
</body></html>"""


def main():
    page = HERE / "wallpaper.html"
    page.write_text(html(), encoding="utf-8")
    png = HERE / "Wallpaper_15_Points_a_Week.png"
    js = (f"const {{chromium}}=require('playwright');(async()=>{{const b=await chromium.launch();"
          f"const p=await b.newPage({{viewport:{{width:{W},height:{H}}}}});await p.goto('{page.as_uri()}');"
          f"await p.waitForTimeout(800);await p.screenshot({{path:'{png}'}});await b.close();}})();")
    npm_root = subprocess.run(["npm", "root", "-g"], capture_output=True, text=True).stdout.strip()
    subprocess.run(["node", "-e", js], check=True, env={"NODE_PATH": npm_root, "PATH": "/usr/bin:/usr/local/bin",
                                                         "PLAYWRIGHT_BROWSERS_PATH": "/opt/pw-browsers"})
    page.unlink()
    print("wrote", png.name)


if __name__ == "__main__":
    main()
