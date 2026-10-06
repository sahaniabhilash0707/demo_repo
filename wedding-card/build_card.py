"""Modern Indian wedding card for Abhishek & Sonali.

Edit the DETAILS block, then run:  python3 build_card.py
Outputs: card.html, Abhishek_Sonali_Wedding_Card.png (1500x2100, 5x7 in @300dpi) and .pdf (5x7 in, print).
"""
import math
import subprocess
from pathlib import Path

HERE = Path(__file__).parent
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"

# ------------------------------------------------------------------ details (edit here)
DETAILS = dict(
    groom="Abhishek Sahani",
    bride="Sonali Mahato",
    # NOTE: 7 Dec 2022 was a Wednesday and 9 Dec 2022 a Friday. The original card said Monday/Wednesday,
    # which matches 2020. Change the year or weekdays here if needed.
    wedding_day="Wednesday", wedding_date="7th December 2022", wedding_time="Evening",
    wedding_venue="Kalyani",
    reception_day="Friday", reception_date="9th December 2022", reception_time="Evening",
    reception_venue="At their residence<br/>Rajarhat, Madanpur",
    families="Sahani &amp; Mahato families",
)

W, H = 1500, 2100
MAROON, MAROON_D, GOLD, GOLD_L, IVORY = "#6b1020", "#4a0a16", "#c9a24d", "#e6c97a", "#fbf5e9"


# ------------------------------------------------------------------ svg helpers
def rosette(cx, cy, r, rings=5, color=GOLD, sw=1.6, fill_op=0.10):
    """Mandala: concentric rings of rotated petals."""
    parts = [f'<g stroke="{color}" stroke-width="{sw}" fill="{color}" fill-opacity="{fill_op}">']
    for k in range(rings):
        rr = r * (k + 1) / rings
        n = 8 + 4 * k
        pl = r / rings * 0.95
        pw = pl * 0.42
        for i in range(n):
            a = 360 / n * i + (180 / n if k % 2 else 0)
            parts.append(
                f'<ellipse cx="{cx}" cy="{cy - rr + pl / 2:.1f}" rx="{pw / 2:.1f}" ry="{pl / 2:.1f}" '
                f'transform="rotate({a:.2f} {cx} {cy})"/>')
        parts.append(f'<circle cx="{cx}" cy="{cy}" r="{rr - pl * 0.02:.1f}" fill="none" stroke-width="{sw * 0.6}"/>')
    parts.append(f'<circle cx="{cx}" cy="{cy}" r="{r * 0.08:.1f}" fill-opacity="0.9"/>')
    parts.append("</g>")
    return "\n".join(parts)


def marigold(x, y, r, col):
    """One marigold flower: frilled disc."""
    out = [f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}" fill="{col}"/>']
    for i in range(10):
        a = math.radians(36 * i)
        out.append(f'<circle cx="{x + math.cos(a) * r * 0.62:.1f}" cy="{y + math.sin(a) * r * 0.62:.1f}" '
                   f'r="{r * 0.42:.1f}" fill="{col}" stroke="#b5561a" stroke-opacity="0.35" stroke-width="1"/>')
    out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r * 0.28:.1f}" fill="#b5561a" fill-opacity="0.55"/>')
    return "".join(out)


def leaf(x, y, ang, s=1.0):
    return (f'<path d="M0 0 Q 12 -9 28 0 Q 12 9 0 0 Z" fill="#2f6b3a" stroke="#1f4d29" stroke-width="0.8" '
            f'transform="translate({x:.1f} {y:.1f}) rotate({ang:.1f}) scale({s})"/>')


def bell(x, y):
    return (f'<g transform="translate({x} {y})" fill="{GOLD}" stroke="#8a6a24" stroke-width="1">'
            f'<path d="M-14 22 Q-14 0 0 -4 Q14 0 14 22 Z"/><circle cx="0" cy="26" r="4"/>'
            f'<circle cx="0" cy="-7" r="4" fill="none"/></g>')


def toran(y0=70, sag=95, swags=4):
    """Marigold garland swags across the top with hanging strings and bells."""
    out = []
    x0, x1 = 60, W - 60
    seg = (x1 - x0) / swags
    cols = ["#f28c28", "#f6b83a", "#e86a1c"]
    for s in range(swags):
        a = x0 + s * seg
        n = 26
        for i in range(n + 1):
            t = i / n
            x = a + t * seg
            y = y0 + sag * 4 * t * (1 - t)
            if i % 4 == 2:
                out.append(leaf(x, y + 6, 70 + 40 * (t - 0.5)))
                out.append(leaf(x, y + 6, 110 + 40 * (t - 0.5)))
            out.append(marigold(x, y, 15, cols[(i + s) % 3]))
    # hanging strings at the joins
    for s in range(swags + 1):
        x = x0 + s * seg
        for j in range(5):
            out.append(marigold(x, y0 + 8 + j * 26, 12.5, cols[j % 3]))
        out.append(bell(x, y0 + 8 + 5 * 26))
    return "\n".join(out)


def lotus(cx, cy, s=1.0, color=GOLD):
    p = []
    for ang, l in ((0, 46), (-28, 40), (28, 40), (-56, 32), (56, 32)):
        p.append(f'<path d="M0 0 C -11 -{l * 0.45} -9 -{l * 0.8} 0 -{l} C 9 -{l * 0.8} 11 -{l * 0.45} 0 0 Z" '
                 f'transform="rotate({ang})"/>')
    return (f'<g transform="translate({cx} {cy}) scale({s})" fill="{color}" fill-opacity="0.18" stroke="{color}" '
            f'stroke-width="1.6">{"".join(p)}<path d="M-34 2 Q0 14 34 2" fill="none"/></g>')


def divider(cx, cy, half=230, color=GOLD):
    return (f'<g stroke="{color}" stroke-width="1.6" fill="{color}">'
            f'<line x1="{cx - half}" y1="{cy}" x2="{cx - 40}" y2="{cy}"/>'
            f'<line x1="{cx + 40}" y1="{cy}" x2="{cx + half}" y2="{cy}"/>'
            f'<circle cx="{cx - half}" cy="{cy}" r="3.5"/><circle cx="{cx + half}" cy="{cy}" r="3.5"/>'
            f'<path d="M{cx} {cy - 14} L{cx + 14} {cy} L{cx} {cy + 14} L{cx - 14} {cy} Z" fill-opacity="0.25"/>'
            f'<circle cx="{cx}" cy="{cy}" r="4"/></g>')


def diya(cx, cy, s=1.0):
    return (f'<g transform="translate({cx} {cy}) scale({s})">'
            f'<path d="M-46 0 Q0 44 46 0 Q24 6 0 6 Q-24 6 -46 0 Z" fill="{GOLD}" stroke="#8a6a24" stroke-width="1.5"/>'
            f'<path d="M-46 0 Q-55 -6 -58 -2" fill="none" stroke="{GOLD}" stroke-width="3"/>'
            f'<path d="M0 2 C -13 -18 -6 -38 0 -54 C 6 -38 13 -18 0 2 Z" fill="#f6b83a"/>'
            f'<path d="M0 0 C -6 -12 -3 -24 0 -34 C 3 -24 6 -12 0 0 Z" fill="#fff3c4"/></g>')


def arch_path(x0, x1, top, bottom, shoulder):
    """Mughal (jharokha) arch: pointed ogee top with cusped shoulders."""
    cx = (x0 + x1) / 2
    return (f"M{x0} {bottom} L{x0} {shoulder} "
            f"C{x0} {shoulder - 120} {x0 + 120} {shoulder - 150} {x0 + 230} {shoulder - 175} "
            f"C{x0 + 380} {shoulder - 210} {cx - 70} {top + 70} {cx} {top} "
            f"C{cx + 70} {top + 70} {x1 - 380} {shoulder - 210} {x1 - 230} {shoulder - 175} "
            f"C{x1 - 120} {shoulder - 150} {x1} {shoulder - 120} {x1} {shoulder} "
            f"L{x1} {bottom} Z")


def background_svg():
    ax0, ax1, top, bottom, sh = 150, W - 150, 330, H - 130, 640
    inner = arch_path(ax0 + 22, ax1 - 22, top + 30, bottom - 22, sh + 10)
    outer = arch_path(ax0, ax1, top, bottom, sh)
    corners = "".join(rosette(x, y, 250, rings=6, sw=1.4, fill_op=0.07) for x, y in
                      ((0, H), (W, H)))
    # small motif pattern on maroon
    pattern = (f'<pattern id="motif" width="60" height="60" patternUnits="userSpaceOnUse">'
               f'<path d="M30 18 L36 30 L30 42 L24 30 Z" fill="{GOLD}" fill-opacity="0.09"/>'
               f'<circle cx="0" cy="0" r="2" fill="{GOLD}" fill-opacity="0.12"/>'
               f'<circle cx="60" cy="60" r="2" fill="{GOLD}" fill-opacity="0.12"/></pattern>')
    cx = W / 2
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
<defs>
  <radialGradient id="bg" cx="50%" cy="40%" r="75%">
    <stop offset="0%" stop-color="{MAROON}"/><stop offset="100%" stop-color="{MAROON_D}"/></radialGradient>
  <linearGradient id="gold" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0%" stop-color="#f1d98f"/><stop offset="50%" stop-color="{GOLD}"/><stop offset="100%" stop-color="#9c7a2e"/></linearGradient>
  <radialGradient id="ivory" cx="50%" cy="45%" r="70%">
    <stop offset="0%" stop-color="#fffaf0"/><stop offset="100%" stop-color="#f4ead6"/></radialGradient>
  {pattern}
</defs>
<rect width="{W}" height="{H}" fill="url(#bg)"/>
<rect width="{W}" height="{H}" fill="url(#motif)"/>
{corners}
<rect x="30" y="30" width="{W - 60}" height="{H - 60}" fill="none" stroke="url(#gold)" stroke-width="3"/>
<rect x="44" y="44" width="{W - 88}" height="{H - 88}" fill="none" stroke="url(#gold)" stroke-width="1.2"/>
<path d="{outer}" fill="url(#ivory)" stroke="url(#gold)" stroke-width="7"/>
<path d="{inner}" fill="none" stroke="{GOLD}" stroke-width="1.6"/>
{rosette(cx, top + 2, 46, rings=3, sw=1.4, fill_op=0.25)}
{toran()}
{lotus(cx, 478, 0.62)}
{divider(cx, 1234, 300)}
{diya(330, bottom - 70, 0.9)}
{diya(W - 330, bottom - 70, 0.9)}
{rosette(ax0 + 70, bottom - 60, 36, rings=3, sw=1.1, fill_op=0.12)}
{rosette(ax1 - 70, bottom - 60, 36, rings=3, sw=1.1, fill_op=0.12)}
</svg>'''


def html(d):
    fonts_css = (HERE / "fonts" / "fonts.css").read_text()
    bg = background_svg()
    return f'''<!doctype html><html><head><meta charset="utf-8"><title>Abhishek &amp; Sonali: Wedding Invitation</title>
<style>
{fonts_css}
@page {{ size: 5in 7in; margin: 0; }}
html, body {{ margin: 0; padding: 0; background: {MAROON_D}; }}
.card {{ position: relative; width: {W}px; height: {H}px; overflow: hidden; }}
.card > svg {{ position: absolute; inset: 0; }}
.content {{ position: absolute; left: 190px; right: 190px; top: 492px; bottom: 150px; text-align: center;
           color: {MAROON}; font-family: 'Cormorant Garamond', serif; }}
.ganesh {{ font-family: 'Tiro Devanagari Sanskrit', serif; font-size: 40px; color: {MAROON}; letter-spacing: 2px; }}
.eyebrow {{ font-family: 'Cinzel', serif; font-weight: 600; font-size: 26px; letter-spacing: 7px; color: #9c7a2e;
           margin-top: 58px; }}
.name {{ font-family: 'Great Vibes', cursive; font-size: 132px; line-height: 1.0; color: {MAROON};
        text-shadow: 0 1px 0 rgba(201,162,77,.35); }}
.groom {{ margin-top: 22px; }}
.amp {{ font-family: 'Great Vibes', cursive; font-size: 92px; line-height: 0.9; color: {GOLD}; margin: 8px 0 4px; }}
.parents {{ font-style: italic; font-size: 30px; color: #7a4a3a; margin-top: 4px; }}
.invite {{ font-style: italic; font-weight: 500; font-size: 38px; line-height: 1.35; color: #5a2a22;
          margin: 40px auto 0; max-width: 860px; }}
.events {{ display: flex; gap: 46px; justify-content: center; margin-top: 100px; }}
.event {{ width: 450px; padding: 34px 20px 30px; border: 2px solid {GOLD}; border-radius: 210px 210px 18px 18px;
         background: rgba(201,162,77,.07); position: relative; }}
.event::before {{ content: ''; position: absolute; inset: 9px; border: 1px solid rgba(201,162,77,.6);
                  border-radius: 200px 200px 12px 12px; }}
.ev-hi {{ font-family: 'Tiro Devanagari Sanskrit', serif; font-size: 36px; color: {GOLD}; }}
.ev-title {{ font-family: 'Cinzel', serif; font-weight: 700; font-size: 34px; letter-spacing: 6px; color: {MAROON};
            margin-top: 4px; }}
.ev-day {{ font-family: 'Cinzel', serif; font-weight: 500; font-size: 22px; letter-spacing: 5px; color: #9c7a2e;
          margin-top: 22px; }}
.ev-date {{ font-weight: 600; font-size: 40px; margin-top: 4px; }}
.ev-time {{ font-style: italic; font-size: 30px; color: #7a4a3a; }}
.ev-rule {{ width: 90px; height: 1.5px; background: {GOLD}; margin: 18px auto; }}
.ev-venue {{ font-weight: 600; font-size: 32px; line-height: 1.25; }}
.blessing {{ font-style: italic; font-size: 33px; color: #5a2a22; margin-top: 62px; }}
.families {{ font-family: 'Cinzel', serif; font-weight: 600; font-size: 24px; letter-spacing: 5px; color: #9c7a2e;
            margin-top: 14px; }}
</style></head><body>
<div class="card">
{bg}
<div class="content">
  <div class="ganesh">॥ श्री गणेशाय नमः ॥</div>
  <div class="eyebrow">Together with their families</div>
  <div class="name groom">{d["groom"]}</div>
  <div class="amp">&amp;</div>
  <div class="name">{d["bride"]}</div>
  <div class="invite">joyfully invite you and your family to bless them<br/>as they begin their journey together</div>
  <div class="events">
    <div class="event">
      <div class="ev-hi">शुभ विवाह</div>
      <div class="ev-title">Wedding</div>
      <div class="ev-day">{d["wedding_day"]}</div>
      <div class="ev-date">{d["wedding_date"]}</div>
      <div class="ev-time">{d["wedding_time"]}</div>
      <div class="ev-rule"></div>
      <div class="ev-venue">{d["wedding_venue"]}</div>
    </div>
    <div class="event">
      <div class="ev-hi">प्रीतिभोज</div>
      <div class="ev-title">Reception</div>
      <div class="ev-day">{d["reception_day"]}</div>
      <div class="ev-date">{d["reception_date"]}</div>
      <div class="ev-time">{d["reception_time"]}</div>
      <div class="ev-rule"></div>
      <div class="ev-venue">{d["reception_venue"]}</div>
    </div>
  </div>
  <div class="blessing">Your presence and blessings will make our celebration complete</div>
  <div class="families">With love · {d["families"]}</div>
</div>
</div>
</body></html>'''


def main():
    page = HERE / "card.html"
    page.write_text(html(DETAILS), encoding="utf-8")
    png = HERE / "Abhishek_Sonali_Wedding_Card.png"
    pdf = HERE / "Abhishek_Sonali_Wedding_Card.pdf"
    common = [CHROME, "--headless=new", "--no-sandbox", "--disable-gpu", "--hide-scrollbars",
              "--allow-file-access-from-files", "--virtual-time-budget=4000"]
    subprocess.run(common + [f"--window-size={W},{H}", f"--screenshot={png}", page.as_uri()], check=True,
                   capture_output=True)
    # PDF: scale the 1500px card onto a 5x7in page (480x672 CSS px at 96dpi)
    pdf_page = HERE / "card_print.html"
    pdf_page.write_text(html(DETAILS).replace(
        "<body>", f'<body><div style="width:480px;height:672px;overflow:hidden"><div style="transform:scale({480 / W});'
                  f'transform-origin:0 0">').replace("</body>", "</div></div></body>"), encoding="utf-8")
    subprocess.run(common + ["--no-pdf-header-footer", f"--print-to-pdf={pdf}", pdf_page.as_uri()], check=True,
                   capture_output=True)
    pdf_page.unlink()
    print("wrote", png.name, pdf.name)


if __name__ == "__main__":
    main()
