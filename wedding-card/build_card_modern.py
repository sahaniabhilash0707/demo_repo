"""Modern minimalist version of the wedding card (blush arch, line-art botanicals, editorial type).

Run:  python3 build_card_modern.py   -> Abhishek_Sonali_Wedding_Card_Modern.png / .pdf
Event details are shared with build_card.py (DETAILS).
"""
import math
import subprocess
from pathlib import Path

from build_card import CHROME, DETAILS

HERE = Path(__file__).parent
W, H = 1500, 2100
CREAM, BLUSH, BLUSH_D = "#f8f2ea", "#f1ddd2", "#e8c9ba"
INK, TERRA, SAGE, GOLD = "#3b2a25", "#b5634a", "#7f9472", "#b8935a"


def leaf_path(x, y, ang, length, width):
    """Almond-shaped leaf outline, base at (x, y), pointing along ang (degrees)."""
    return (f'<path d="M0 0 Q {length * 0.5} {-width} {length} 0 Q {length * 0.5} {width} 0 0 Z '
            f'M0 0 L{length * 0.85} 0" transform="translate({x:.1f} {y:.1f}) rotate({ang:.1f})"/>')


def sprig(x0, y0, ang, length, bend=0.25, leaves=7, leaf_len=46, flip=1):
    """Curved stem with alternating leaves (stroke-only line art)."""
    a = math.radians(ang)
    x1, y1 = x0 + math.cos(a) * length, y0 + math.sin(a) * length
    nx, ny = -math.sin(a) * length * bend * flip, math.cos(a) * length * bend * flip
    cx, cy = (x0 + x1) / 2 + nx, (y0 + y1) / 2 + ny
    out = [f'<path d="M{x0:.1f} {y0:.1f} Q{cx:.1f} {cy:.1f} {x1:.1f} {y1:.1f}" fill="none"/>']
    for i in range(1, leaves + 1):
        t = i / (leaves + 1)
        px = (1 - t) ** 2 * x0 + 2 * (1 - t) * t * cx + t * t * x1
        py = (1 - t) ** 2 * y0 + 2 * (1 - t) * t * cy + t * t * y1
        dx = 2 * (1 - t) * (cx - x0) + 2 * t * (x1 - cx)
        dy = 2 * (1 - t) * (cy - y0) + 2 * t * (y1 - cy)
        tang = math.degrees(math.atan2(dy, dx))
        side = 1 if i % 2 else -1
        ll = leaf_len * (1.1 - 0.5 * t)
        out.append(leaf_path(px, py, tang + 48 * side, ll, ll * 0.32))
    out.append(leaf_path(x1, y1, math.degrees(math.atan2(y1 - cy, x1 - cx)), leaf_len * 0.6, leaf_len * 0.2))
    return "\n".join(out)


def bloom(cx, cy, r, petals=8, rot=0):
    """Line-art flower (marigold/jasmine-like): outlined petals + dotted centre."""
    out = []
    for i in range(petals):
        a = 360 / petals * i + rot
        out.append(f'<path d="M0 0 C {r * 0.35} {-r * 0.28} {r * 0.85} {-r * 0.3} {r} 0 '
                   f'C {r * 0.85} {r * 0.3} {r * 0.35} {r * 0.28} 0 0 Z" '
                   f'transform="translate({cx} {cy}) rotate({a})"/>')
    out.append(f'<circle cx="{cx}" cy="{cy}" r="{r * 0.22:.1f}" fill="{CREAM}"/>')
    for i in range(6):
        a = math.radians(60 * i)
        out.append(f'<circle cx="{cx + math.cos(a) * r * 0.1:.1f}" cy="{cy + math.sin(a) * r * 0.1:.1f}" '
                   f'r="2.2" fill="{TERRA}" stroke="none"/>')
    return "\n".join(out)


def lotus_line(cx, cy, s=1.0):
    p = []
    for ang, l in ((0, 50), (-30, 42), (30, 42), (-62, 30), (62, 30)):
        p.append(f'<path d="M0 0 C -12 -{l * 0.45} -10 -{l * 0.8} 0 -{l} C 10 -{l * 0.8} 12 -{l * 0.45} 0 0 Z" '
                 f'transform="rotate({ang})"/>')
    return (f'<g transform="translate({cx} {cy}) scale({s})" fill="none" stroke="{TERRA}" stroke-width="1.6">'
            f'{"".join(p)}<path d="M-40 4 Q0 16 40 4"/></g>')


def arch(x0, x1, top, bottom):
    r = (x1 - x0) / 2
    return f"M{x0} {bottom} L{x0} {top + r} A{r} {r} 0 0 1 {x1} {top + r} L{x1} {bottom} Z"


def svg():
    cx = W / 2
    ax0, ax1, atop, abot = 210, W - 210, 170, H - 290
    botanics = f'''
<g fill="none" stroke="{SAGE}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
  {sprig(ax0 - 40, abot - 40, -78, 520, bend=0.18, leaves=9, leaf_len=56)}
  {sprig(ax0 - 20, abot - 30, -58, 210, bend=-0.2, leaves=5, leaf_len=44)}
  {sprig(ax0 - 30, abot + 10, -8, 170, bend=0.25, leaves=4, leaf_len=38)}
  {sprig(ax1 + 40, atop + 470, -102, 330, bend=-0.2, leaves=7, leaf_len=46)}
  {sprig(ax1 + 30, atop + 500, -150, 260, bend=0.25, leaves=5, leaf_len=40)}
</g>
<g fill="{CREAM}" stroke="{TERRA}" stroke-width="1.8">
  {bloom(ax0 + 48, abot - 535, 42, 9, 10)}
  {bloom(ax0 + 85, abot - 215, 30, 8, 25)}
  {bloom(ax0 - 5, abot - 300, 26, 7, 0)}
  {bloom(ax1 + 18, atop + 150, 40, 9, 5)}
  {bloom(ax1 - 150, atop + 270, 28, 8, 20)}
</g>
<g fill="{TERRA}">
  <circle cx="{ax0 + 120}" cy="{abot - 420}" r="5"/><circle cx="{ax0 + 150}" cy="{abot - 395}" r="3.5"/>
  <circle cx="{ax1 - 70}" cy="{atop + 360}" r="5"/><circle cx="{ax1 - 95}" cy="{atop + 335}" r="3.5"/>
</g>'''
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
<defs>
  <filter id="grain"><feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="2" stitchTiles="stitch"/>
    <feColorMatrix values="0 0 0 0 0.45  0 0 0 0 0.35  0 0 0 0 0.3  0 0 0 0.05 0"/></filter>
  <linearGradient id="archfill" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%" stop-color="#f4e4db"/><stop offset="100%" stop-color="{BLUSH}"/></linearGradient>
</defs>
<rect width="{W}" height="{H}" fill="{CREAM}"/>
<path d="{arch(ax0, ax1, atop, abot)}" fill="url(#archfill)"/>
<path d="{arch(ax0 + 26, ax1 + 26, atop - 26, abot - 26)}" fill="none" stroke="{GOLD}" stroke-width="1.6"/>
{botanics}
{lotus_line(cx, 1352, 0.5)}
<line x1="{cx}" y1="1395" x2="{cx}" y2="1740" stroke="{GOLD}" stroke-width="1.4"/>
<rect width="{W}" height="{H}" filter="url(#grain)"/>
</svg>'''


def html(d):
    fonts = (HERE / "fonts" / "fonts.css").read_text() + (HERE / "fonts" / "fonts_modern.css").read_text()
    g_first, g_last = d["groom"].split(" ", 1)
    b_first, b_last = d["bride"].split(" ", 1)
    return f'''<!doctype html><html><head><meta charset="utf-8"><title>Abhishek &amp; Sonali: Wedding Invitation</title>
<style>
{fonts}
@page {{ size: 5in 7in; margin: 0; }}
html, body {{ margin: 0; background: {CREAM}; }}
.card {{ position: relative; width: {W}px; height: {H}px; overflow: hidden; }}
.card > svg {{ position: absolute; inset: 0; }}
.c {{ position: absolute; left: 250px; right: 250px; top: 255px; text-align: center; color: {INK}; }}
.mono {{ width: 150px; height: 150px; margin: 0 auto; border: 1.5px solid {GOLD}; border-radius: 50%;
        position: relative; font-family: 'Bodoni Moda', serif; font-style: italic; font-size: 58px; color: {TERRA}; }}
.mono span {{ position: absolute; }}
.mono .a {{ left: 32px; top: 22px; }} .mono .s {{ right: 34px; bottom: 26px; }}
.mono::after {{ content: ''; position: absolute; left: 50%; top: 22px; height: 106px; width: 1.4px;
               background: {GOLD}; transform: rotate(32deg); }}
.ganesh {{ font-family: 'Tiro Devanagari Sanskrit', serif; font-size: 30px; color: {TERRA}; margin-top: 34px;
          letter-spacing: 1px; }}
.small {{ font-family: 'Jost', sans-serif; font-weight: 400; font-size: 23px; letter-spacing: 9px;
         text-transform: uppercase; color: #7a5d52; }}
.eyebrow {{ margin-top: 40px; }}
.first {{ font-family: 'Bodoni Moda', serif; font-weight: 400; font-size: 140px; line-height: 1; color: {INK};
         letter-spacing: -1px; }}
.f1 {{ margin-top: 40px; }}
.last {{ font-family: 'Jost', sans-serif; font-weight: 400; font-size: 26px; letter-spacing: 14px;
        text-transform: uppercase; color: {TERRA}; margin-top: 10px; }}
.amp {{ font-family: 'Bodoni Moda', serif; font-style: italic; font-size: 88px; color: {GOLD}; line-height: 1;
       margin: 26px 0 18px; }}
.invite {{ font-family: 'Bodoni Moda', serif; font-style: italic; font-size: 34px; line-height: 1.45;
          color: #5b443c; margin-top: 52px; }}
.events {{ display: grid; grid-template-columns: 1fr 1fr; margin-top: 110px; }}
.ev {{ padding: 0 30px; }}
.ev .small {{ font-size: 21px; letter-spacing: 8px; color: {TERRA}; font-weight: 500; }}
.ev .day {{ font-family: 'Jost', sans-serif; font-size: 24px; letter-spacing: 6px; text-transform: uppercase;
           color: #7a5d52; margin-top: 26px; }}
.ev .date {{ font-family: 'Bodoni Moda', serif; font-size: 96px; line-height: 1; margin-top: 8px; color: {INK}; }}
.ev .month {{ font-family: 'Bodoni Moda', serif; font-style: italic; font-size: 36px; color: {INK}; margin-top: 6px; }}
.ev .time {{ font-family: 'Jost', sans-serif; font-weight: 300; font-size: 24px; letter-spacing: 4px;
            text-transform: uppercase; color: #7a5d52; margin-top: 14px; }}
.ev .venue {{ font-family: 'Bodoni Moda', serif; font-size: 31px; line-height: 1.3; margin-top: 22px; color: {INK}; }}
.foot {{ position: absolute; left: 0; right: 0; bottom: 140px; text-align: center; }}
.foot .bless {{ font-family: 'Bodoni Moda', serif; font-style: italic; font-size: 30px; color: #5b443c; }}
.foot .small {{ margin-top: 16px; font-size: 20px; letter-spacing: 8px; }}
</style></head><body><div class="card">
{svg()}
<div class="c">
  <div class="mono"><span class="a">A</span><span class="s">S</span></div>
  <div class="ganesh">॥ श्री गणेशाय नमः ॥</div>
  <div class="small eyebrow">Together with their families</div>
  <div class="first f1">{g_first}</div>
  <div class="last">{g_last}</div>
  <div class="amp">&amp;</div>
  <div class="first">{b_first}</div>
  <div class="last">{b_last}</div>
  <div class="invite">joyfully invite you to celebrate their wedding<br/>and bless them as they begin forever</div>
  <div class="events">
    <div class="ev">
      <div class="small">The Wedding</div>
      <div class="day">{d["wedding_day"]}</div>
      <div class="date">{d["wedding_date"].split()[0][:-2].zfill(2)}</div>
      <div class="month">{" ".join(d["wedding_date"].split()[1:])}</div>
      <div class="time">{d["wedding_time"]}</div>
      <div class="venue">{d["wedding_venue"]}</div>
    </div>
    <div class="ev">
      <div class="small">The Reception</div>
      <div class="day">{d["reception_day"]}</div>
      <div class="date">{d["reception_date"].split()[0][:-2].zfill(2)}</div>
      <div class="month">{" ".join(d["reception_date"].split()[1:])}</div>
      <div class="time">{d["reception_time"]}</div>
      <div class="venue">{d["reception_venue"]}</div>
    </div>
  </div>
</div>
<div class="foot">
  <div class="bless">Your presence and blessings are our greatest gift</div>
  <div class="small">With love · {d["families"]}</div>
</div>
</div></body></html>'''


def main():
    page = HERE / "card_modern.html"
    page.write_text(html(DETAILS), encoding="utf-8")
    png = HERE / "Abhishek_Sonali_Wedding_Card_Modern.png"
    pdf = HERE / "Abhishek_Sonali_Wedding_Card_Modern.pdf"
    common = [CHROME, "--headless=new", "--no-sandbox", "--disable-gpu", "--hide-scrollbars",
              "--allow-file-access-from-files", "--virtual-time-budget=4000"]
    subprocess.run(common + [f"--window-size={W},{H}", f"--screenshot={png}", page.as_uri()], check=True,
                   capture_output=True)
    tmp = HERE / "card_modern_print.html"
    tmp.write_text(html(DETAILS).replace(
        "<body>", f'<body><div style="width:480px;height:672px;overflow:hidden"><div style="transform:scale({480 / W});'
                  f'transform-origin:0 0">').replace("</body>", "</div></div></body>"), encoding="utf-8")
    subprocess.run(common + ["--no-pdf-header-footer", f"--print-to-pdf={pdf}", tmp.as_uri()], check=True,
                   capture_output=True)
    tmp.unlink()
    print("wrote", png.name, pdf.name)


if __name__ == "__main__":
    main()
