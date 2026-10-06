"""Assemble Guruji_Price_Action_Manual.pdf from content_*.py and charts/*.png."""
from pathlib import Path

from PIL import Image as PILImage
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (BaseDocTemplate, CondPageBreak, Flowable, Frame, Image, KeepTogether, NextPageTemplate,
                                PageBreak, PageTemplate, Paragraph, Spacer, Table, TableStyle)
from reportlab.platypus.tableofcontents import TableOfContents

import content_a
import content_b

HERE = Path(__file__).parent
CHARTS = HERE / "charts"
OUT = HERE / "Guruji_Price_Action_Manual.pdf"

FD = "/usr/share/fonts/truetype/crosextra/"
pdfmetrics.registerFont(TTFont("Body", FD + "Carlito-Regular.ttf"))
pdfmetrics.registerFont(TTFont("Body-Bold", FD + "Carlito-Bold.ttf"))
pdfmetrics.registerFont(TTFont("Body-Italic", FD + "Carlito-Italic.ttf"))
pdfmetrics.registerFont(TTFont("Body-BoldItalic", FD + "Carlito-BoldItalic.ttf"))
from reportlab.pdfbase.pdfmetrics import registerFontFamily  # noqa: E402
pdfmetrics.registerFont(TTFont("Sym", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"))
registerFontFamily("Body", normal="Body", bold="Body-Bold", italic="Body-Italic", boldItalic="Body-BoldItalic")

NAVY = colors.HexColor("#13233f")
INK = colors.HexColor("#1d2433")
MUTE = colors.HexColor("#5b6475")
AMBER = colors.HexColor("#d9902b")
AMBER_BG = colors.HexColor("#fff6e6")
RED = colors.HexColor("#c0392b")
RED_BG = colors.HexColor("#fdecea")
GREEN = colors.HexColor("#1f8a6e")
GREEN_BG = colors.HexColor("#e8f6f1")
BLUE_BG = colors.HexColor("#eef2f9")
LINE = colors.HexColor("#d5dae3")
DARK = colors.HexColor("#0b0f17")

PART_NAMES = {1: "How the Market Really Works", 2: "Retail Traps", 3: "Smart-Money Price Action",
              4: "Turning It Into Trades"}
PART_COL = {1: colors.HexColor("#2f5597"), 2: colors.HexColor("#b03a2e"), 3: colors.HexColor("#1f7a6a"),
            4: colors.HexColor("#8a5a12")}

PAGE_W, PAGE_H = A4
LM = RM = 17 * mm
TM, BM = 19 * mm, 17 * mm
FW = PAGE_W - LM - RM

S = {}
S["body"] = ParagraphStyle("body", fontName="Body", fontSize=10, leading=13.2, textColor=INK, spaceAfter=4)
S["bullet"] = ParagraphStyle("bullet", parent=S["body"], leftIndent=12, bulletIndent=1, spaceAfter=2.5,
                             bulletFontName="Sym", bulletFontSize=8.5, bulletColor=RED)
S["h_sec"] = ParagraphStyle("h_sec", fontName="Body-Bold", fontSize=11.4, leading=13.6, textColor=NAVY,
                            spaceBefore=6, spaceAfter=3)
S["cap"] = ParagraphStyle("cap", fontName="Body-Italic", fontSize=8.6, leading=10.8, textColor=MUTE,
                          spaceBefore=2, spaceAfter=7)
S["call"] = ParagraphStyle("call", fontName="Body", fontSize=9.9, leading=13, textColor=INK)
S["call_h"] = ParagraphStyle("call_h", fontName="Body-Bold", fontSize=9.4, leading=12, spaceAfter=1.5)
S["cell"] = ParagraphStyle("cell", fontName="Body", fontSize=9.4, leading=12, textColor=INK)
S["cell_b"] = ParagraphStyle("cell_b", parent=S["cell"], fontName="Body-Bold")
S["small"] = ParagraphStyle("small", fontName="Body", fontSize=9.2, leading=11.6, textColor=INK)
S["small_b"] = ParagraphStyle("small_b", parent=S["small"], fontName="Body-Bold")
S["toc0"] = ParagraphStyle("toc0", fontName="Body-Bold", fontSize=11, leading=13.5, textColor=NAVY, spaceBefore=5)
S["toc1"] = ParagraphStyle("toc1", fontName="Body", fontSize=10, leading=12.6, leftIndent=14, textColor=INK)


# ------------------------------------------------------------------ flowables
class Bookmark(Flowable):
    """Zero-size marker: records TOC entry + PDF outline + running header text."""

    def __init__(self, level, text, key, header=None):
        super().__init__()
        self.level, self.text, self.key, self.header = level, text, key, header

    def wrap(self, *_):
        return 0, 0

    def draw(self):
        c = self.canv
        c.bookmarkPage(self.key)
        c.addOutlineEntry(self.text, self.key, level=self.level, closed=False)


class ChapterHeader(Flowable):
    def __init__(self, ch):
        super().__init__()
        self.ch = ch
        self.h = 37 * mm

    def wrap(self, aw, ah):
        self.aw = aw
        return aw, self.h

    def draw(self):
        c, ch = self.canv, self.ch
        col = PART_COL[ch["part"]]
        c.setFillColor(NAVY)
        c.roundRect(0, 0, self.aw, self.h, 4, stroke=0, fill=1)
        c.setFillColor(col)
        c.rect(0, 0, 6, self.h, stroke=0, fill=1)
        c.setFillColor(colors.HexColor("#f2c27b"))
        c.setFont("Body-Bold", 9.5)
        c.drawString(14, self.h - 15, f"PART {ch['part']}  ·  {PART_NAMES[ch['part']].upper()}")
        c.setFillColor(colors.white)
        c.setFont("Body-Bold", 44)
        c.drawString(14, 15, f"{ch['num']:02d}")
        title = ch["title"]
        fs = 21
        while pdfmetrics.stringWidth(title, "Body-Bold", fs) > self.aw - 90 and fs > 13:
            fs -= 0.5
        c.setFont("Body-Bold", fs)
        c.drawString(78, 31, title)
        c.setFont("Body-Italic", 11)
        c.setFillColor(colors.HexColor("#c9d3e6"))
        c.drawString(78, 14, ch["tagline"])


def callout(kind, text, width=FW, keep=True):
    cfg = {"guruji": ("GURUJI SAYS", AMBER, AMBER_BG), "mistake": ("RETAIL MISTAKE", RED, RED_BG),
           "rule": ("RULE", GREEN, GREEN_BG)}[kind]
    head = Paragraph(f'<font color="{cfg[1].hexval()}">{cfg[0]}</font>', S["call_h"])
    t = Table([[[head, Paragraph(text, S["call"])]]], colWidths=[width])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), cfg[2]),
        ("LINEBEFORE", (0, 0), (0, -1), 3.2, cfg[1]),
        ("LEFTPADDING", (0, 0), (-1, -1), 9), ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 5.5), ("BOTTOMPADDING", (0, 0), (-1, -1), 6.5),
    ]))
    if not keep:
        return t
    return KeepTogether([Spacer(1, 2), t, Spacer(1, 6)])


def sec(label, text):
    return Paragraph(f'<font color="{AMBER.hexval()}">{label}</font>&nbsp;&nbsp;{text}', S["h_sec"])


def chart(name, caption, scale=0.9):
    width = FW * scale
    p = CHARTS / f"{name}.png"
    w, h = PILImage.open(p).size
    img = Image(str(p), width=width, height=width * h / w)
    img.hAlign = "CENTER"
    return [img, Paragraph(caption, S["cap"])]


def kv_table(rows, head="Rule-based trade", col1=33 * mm):
    data = [[Paragraph(f"<b>{k}</b>", S["cell"]), Paragraph(v, S["cell"])] for k, v in rows]
    t = Table(data, colWidths=[col1, FW - col1])
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("BACKGROUND", (0, 0), (0, -1), BLUE_BG),
        ("LINEBELOW", (0, 0), (-1, -2), 0.5, LINE),
        ("BOX", (0, 0), (-1, -1), 0.8, NAVY),
        ("LEFTPADDING", (0, 0), (-1, -1), 6), ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 3.2), ("BOTTOMPADDING", (0, 0), (-1, -1), 3.6),
    ]))
    return t


def summary_box(items):
    rows = [[Paragraph('<font color="#f2c27b"><b>SUMMARY: 3 THINGS TO REMEMBER</b></font>',
                       ParagraphStyle("sb", parent=S["call"], textColor=colors.white))]]
    for i, s in enumerate(items, 1):
        rows.append([Paragraph(f'<font color="#f2c27b"><b>{i}.</b></font>&nbsp; {s}',
                               ParagraphStyle("sb2", parent=S["call"], textColor=colors.white))])
    t = Table(rows, colWidths=[FW])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), NAVY),
        ("LEFTPADDING", (0, 0), (-1, -1), 10), ("RIGHTPADDING", (0, 0), (-1, -1), 10),
        ("TOPPADDING", (0, 0), (-1, -1), 3), ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
        ("TOPPADDING", (0, 0), (-1, 0), 7), ("BOTTOMPADDING", (0, -1), (-1, -1), 8),
    ]))
    return [Spacer(1, 4), t]


def paras(lst):
    out = []
    for p in lst:
        out.append(Paragraph(p, S["body"]))
    return out


# ------------------------------------------------------------------ page decoration
def on_page(c, doc):
    c.saveState()
    c.setStrokeColor(LINE)
    c.setLineWidth(0.6)
    c.line(LM, PAGE_H - 12 * mm, PAGE_W - RM, PAGE_H - 12 * mm)
    c.setFont("Body-Bold", 8)
    c.setFillColor(NAVY)
    c.drawString(LM, PAGE_H - 10.4 * mm, "GURUJI'S PRICE-ACTION MANUAL")
    c.setFont("Body", 8)
    c.setFillColor(MUTE)
    c.drawRightString(PAGE_W - RM, PAGE_H - 10.4 * mm, getattr(doc, "cur_header", ""))
    c.line(LM, 11 * mm, PAGE_W - RM, 11 * mm)
    c.setFont("Body", 8)
    c.drawString(LM, 7 * mm, "Educational material · not investment advice · synthetic chart data")
    c.setFont("Body-Bold", 9)
    c.setFillColor(NAVY)
    c.drawRightString(PAGE_W - RM, 7 * mm, str(doc.page))
    c.restoreState()


def on_cover(c, doc):
    c.saveState()
    c.setFillColor(DARK)
    c.rect(0, 0, PAGE_W, PAGE_H, stroke=0, fill=1)
    c.setFillColor(AMBER)
    c.rect(0, PAGE_H - 9 * mm, PAGE_W, 9 * mm, stroke=0, fill=1)
    c.setFillColor(colors.HexColor("#f2c27b"))
    c.setFont("Body-Bold", 11)
    c.drawString(LM, PAGE_H - 36 * mm, "NIFTY WEEKLY OPTIONS  ·  PRICE ACTION  ·  SMART MONEY  ·  RISK")
    c.setFillColor(colors.white)
    c.setFont("Body-Bold", 40)
    c.drawString(LM, PAGE_H - 56 * mm, "Guruji's")
    c.drawString(LM, PAGE_H - 72 * mm, "Price-Action Manual")
    c.setFont("Body", 15)
    c.setFillColor(colors.HexColor("#c9d3e6"))
    c.drawString(LM, PAGE_H - 84 * mm, "How the market traps traders, and how to trade with smart money")
    img = CHARTS / "c10a.png"
    w, h = PILImage.open(img).size
    iw = PAGE_W - LM - RM
    ih = iw * h / w
    c.drawImage(str(img), LM, PAGE_H - 96 * mm - ih, iw, ih)
    y = PAGE_H - 104 * mm - ih
    c.setFillColor(colors.HexColor("#f2c27b"))
    c.setFont("Body-Italic", 12.5)
    c.drawString(LM, y, "“You earn in theta. You lose in gamma. You survive with rules.”")
    c.setFillColor(colors.HexColor("#8b93a5"))
    c.setFont("Body", 9.5)
    c.drawString(LM, 24 * mm, "26 chapters · 43 annotated charts · 5 A+ setups · one-page cheat sheet · glossary")
    c.drawString(LM, 18 * mm, "Edition: October 2026 · Lot size 65 · Weekly expiry Tuesday · Educational use only")
    c.restoreState()


class Doc(BaseDocTemplate):
    def __init__(self, path):
        super().__init__(str(path), pagesize=A4, leftMargin=LM, rightMargin=RM, topMargin=TM, bottomMargin=BM,
                         title="Guruji's Price-Action Manual", author="Guruji (educational persona)",
                         subject="NIFTY weekly options price action, traps, smart money and risk management")
        frame = Frame(LM, BM, FW, PAGE_H - TM - BM, id="f", leftPadding=0, rightPadding=0, topPadding=0,
                      bottomPadding=0)
        self.addPageTemplates([PageTemplate("cover", [frame], onPage=on_cover),
                               PageTemplate("body", [frame], onPageEnd=on_page)])
        self.cur_header = ""

    def afterFlowable(self, f):
        if isinstance(f, Bookmark):
            if f.header is not None:
                self.cur_header = f.header
            self.notify("TOCEntry", (f.level, f.text, self.page, f.key))


# ------------------------------------------------------------------ story
def front_matter(story):
    story += [NextPageTemplate("body"), PageBreak()]
    story.append(Bookmark(0, "Before you begin", "front", "Before you begin"))
    story.append(Paragraph("Before you begin", ParagraphStyle("t", fontName="Body-Bold", fontSize=22, leading=26,
                                                              textColor=NAVY, spaceAfter=6)))
    story += paras([
        "This manual is written in the voice of <b>Guruji</b>, a fictional composite of a price-action trader with 30+ "
        "years in Indian markets. It is for one reader: a NIFTY weekly-options trader who lost about 46% of capital "
        "through oversized positions, missing stop-losses, expiry-day gamma spikes and revenge trading, and wants to "
        "understand how those losses were engineered and how to stop being the liquidity.",
        "Every chapter follows the same pattern: <b>(a)</b> the concept, <b>(b)</b> why it works, "
        "<b>(c)</b> annotated chart(s), <b>(d)</b> a NIFTY example with realistic levels, <b>(e)</b> a rule-based "
        "entry, stop-loss and target, <b>(f)</b> common mistakes and <b>(g)</b> a three-point summary. All charts are "
        "generated from <b>synthetic</b> NIFTY data designed to show each pattern clearly; option premiums in "
        "Chapters 10, 11 and 22 are computed with the Black-Scholes model from the spot path.",
    ])
    story.append(sec("", "Market facts verified for this edition (6 Oct 2026)"))
    story.append(kv_table(content_b.FACTS, col1=34 * mm))
    story.append(Spacer(1, 7))
    story.append(callout("guruji", "Rules change; principles don't. Liquidity, structure and risk worked in the "
                                   "ring at Dalal Street in 1994 and they work on Kite in 2026. But lot sizes, expiry "
                                   "days and margins change every year, so re-check them every June and December."))
    story.append(sec("", "How to read the callouts"))
    cw = FW / 3 - 4
    legend = Table([[callout("guruji", "Experience and perspective from the trading floor.", cw, False),
                     callout("mistake", "What retail traders typically do wrong.", cw, False),
                     callout("rule", "A non-negotiable rule to copy into your plan.", cw, False)]],
                   colWidths=[FW / 3] * 3)
    legend.setStyle(TableStyle([("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 4),
                                ("VALIGN", (0, 0), (-1, -1), "TOP")]))
    story.append(legend)
    story.append(sec("", "Risk disclaimer"))
    story.append(Paragraph(
        "This manual is for education only. It is not investment advice, a recommendation, or a research report, "
        "and the author persona is not a SEBI-registered investment adviser or research analyst. Trading futures and "
        "options involves substantial risk of loss and is not suitable for most investors; SEBI's FY25 study found "
        "about 91% of individual F&amp;O traders made net losses. Any win rates mentioned are <b>illustrative only</b>, "
        "not promises, and no setup in this book guarantees profit. Past patterns don't predict future results. "
        "Verify every contract specification and rule with NSE, SEBI and your broker before trading, and never risk "
        "money you cannot afford to lose.", S["body"]))


def toc(story):
    story.append(PageBreak())
    story.append(Paragraph("Contents", ParagraphStyle("t", fontName="Body-Bold", fontSize=22, leading=26,
                                                      textColor=NAVY, spaceAfter=8)))
    t = TableOfContents()
    t.levelStyles = [S["toc0"], S["toc1"]]
    t.dotsMinLevel = 1
    story.append(t)


def setup_block(st):
    out = [CondPageBreak(95 * mm), Paragraph(st["name"], ParagraphStyle(
        "sn", fontName="Body-Bold", fontSize=13.5, leading=17, textColor=PART_COL[4], spaceBefore=6, spaceAfter=3))]
    out += chart(st["chart"], st["caption"])
    check = "<br/>".join(f'<font name="Sym" size="8.5">☐</font>&nbsp; {c}' for c in st["checklist"])
    rows = [("Checklist", check), ("Entry trigger", st["trigger"]), ("Stop-loss", st["sl"]),
            ("Target", st["target"]), ("R:R", st["rr"]), ("Best time", st["time"]),
            ("When NOT to take it", st["avoid"]), ("Win rate", st["winrate"])]
    out.append(kv_table(rows, col1=33 * mm))
    out.append(Spacer(1, 8))
    return out


def cheat_page(story):
    story.append(PageBreak())
    story.append(Paragraph("One-page cheat sheet", ParagraphStyle(
        "t", fontName="Body-Bold", fontSize=17, leading=20, textColor=NAVY, spaceAfter=4)))
    hdr = [Paragraph(f"<b>{h}</b>", S["small"]) for h in ("Trap", "What you see", "What it means", "What to do")]
    rows = [hdr] + [[Paragraph(f"<b>{a}</b>", S["small"]), Paragraph(b, S["small"]), Paragraph(c, S["small"]),
                     Paragraph(d, S["small"])] for a, b, c, d in content_b.CHEAT_TRAPS]
    t = Table(rows, colWidths=[34 * mm, 50 * mm, 37 * mm, FW - 121 * mm], repeatRows=1)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#f6dcd8")), ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("GRID", (0, 0), (-1, -1), 0.4, LINE), ("BOX", (0, 0), (-1, -1), 0.8, RED),
        ("TOPPADDING", (0, 0), (-1, -1), 2.2), ("BOTTOMPADDING", (0, 0), (-1, -1), 2.6),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#fbf7f6")]),
    ]))
    story.append(Paragraph("<b>TRAPS: recognise, don't participate</b>", S["small_b"]))
    story.append(Spacer(1, 2))
    story.append(t)
    story.append(Spacer(1, 6))
    hdr = [Paragraph(f"<b>{h}</b>", S["small"]) for h in ("Setup", "Checklist core", "Trigger", "Stop-loss",
                                                          "Target / R:R", "Time")]
    rows = [hdr] + [[Paragraph(f"<b>{r[0]}</b>", S["small"])] + [Paragraph(x, S["small"]) for x in r[1:]]
                    for r in content_b.CHEAT_SETUPS]
    t = Table(rows, colWidths=[30 * mm, 40 * mm, 30 * mm, 27 * mm, 28 * mm, FW - 155 * mm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#d8efe8")), ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("GRID", (0, 0), (-1, -1), 0.4, LINE), ("BOX", (0, 0), (-1, -1), 0.8, GREEN),
        ("TOPPADDING", (0, 0), (-1, -1), 2.2), ("BOTTOMPADDING", (0, 0), (-1, -1), 2.6),
    ]))
    story.append(Paragraph("<b>A+ SETUPS: grade A = 1% risk, B = half, C = no trade</b>", S["small_b"]))
    story.append(Spacer(1, 2))
    story.append(t)
    story.append(Spacer(1, 6))
    risk = [
        ("Capital ₹2,70,000", "1R = ₹2,700 · daily limit ₹5,400 · weekly ₹16,200 · max 2 lots · max 3 trades · "
                              "2 losses in a row = stop"),
        ("Position size", "Lots = floor(₹2,700 ÷ (premium SL pts × 65)); spot SL × delta ≈ premium SL; spreads: "
                          "(width − credit) × 65 per lot"),
        ("Expiry Tuesday", "Half size · no new shorts after 14:00 · trail after 40% decay · flat by 14:45"),
        ("Option selling", "Strike beyond swept liquidity + OI wall + VIX 1-SD range · always hedged · exit at 2x"),
        ("Never", "Average losers · widen SL · trade first 15 min / event first 30 min · trade after STOP flag"),
    ]
    rows = [[Paragraph(f"<b>{a}</b>", S["small"]), Paragraph(b, S["small"])] for a, b in risk]
    t = Table(rows, colWidths=[34 * mm, FW - 34 * mm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (0, -1), colors.HexColor("#fff0d6")), ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("GRID", (0, 0), (-1, -1), 0.4, LINE), ("BOX", (0, 0), (-1, -1), 0.8, AMBER),
        ("TOPPADDING", (0, 0), (-1, -1), 2.2), ("BOTTOMPADDING", (0, 0), (-1, -1), 2.6),
    ]))
    story.append(Paragraph("<b>RISK CARD</b>", S["small_b"]))
    story.append(Spacer(1, 2))
    story.append(t)


def chapter(story, ch, first_in_part):
    story.append(PageBreak() if first_in_part else CondPageBreak(115 * mm))
    if not first_in_part:
        story.append(Spacer(1, 4))
    if first_in_part:
        story.append(Bookmark(0, f"Part {ch['part']} · {PART_NAMES[ch['part']]}", f"part{ch['part']}"))
    story.append(Bookmark(1, f"{ch['num']}. {ch['title']}", f"ch{ch['num']}",
                          f"Part {ch['part']} · Chapter {ch['num']}: {ch['title']}"))
    story.append(ChapterHeader(ch))
    story.append(Spacer(1, 6))
    def head(label, text, items, n=1):
        items = list(items)
        story.append(KeepTogether([sec(label, text)] + items[:n]))
        story.extend(items[n:])

    head("(a)", "The concept", [Paragraph(p, S["body"]) for p in ch["concept"]])
    story.append(callout("guruji", ch["guruji"]))
    head("(b)", "Why it works: the psychology", paras(ch["why"]))
    charts = ch.get("charts", [])
    if charts:
        head("(c)", "Annotated chart" + ("s" if len(charts) > 1 else ""), chart(*charts[0]), n=2)
    if ch.get("setups"):
        story.append(sec("(c-e)", "The five setups: chart, checklist, entry, stop-loss, target"))
        for st in ch["setups"]:
            story += setup_block(st)
    if ch.get("example"):
        head("(d)", "NIFTY example", paras(ch["example"]))
    for c in charts[1:]:
        story.append(KeepTogether(chart(*c)))
    if ch.get("trade"):
        head("(e)", "Rule-based entry, stop-loss and target", [kv_table(ch["trade"]), Spacer(1, 5)])
    story.append(callout("rule", ch["rule"]))
    head("(f)", "Common mistakes", [Paragraph(m, S["bullet"], bulletText="✗") for m in ch["mistakes"]])
    story.append(callout("mistake", ch["retail"]))
    story.append(KeepTogether([sec("(g)", "Summary")] + summary_box(ch["summary"])))
    if ch.get("cheatsheet"):
        cheat_page(story)


def glossary(story):
    story.append(PageBreak())
    story.append(Bookmark(0, "Glossary", "glossary", "Glossary"))
    story.append(Paragraph("Glossary", ParagraphStyle("t", fontName="Body-Bold", fontSize=22, leading=26,
                                                      textColor=NAVY, spaceAfter=6)))
    items = content_b.GLOSSARY
    rows = [[Paragraph(f"<b>{a}</b>", S["cell"]), Paragraph(b, S["cell"])] for a, b in items]
    t = Table(rows, colWidths=[38 * mm, FW - 38 * mm])
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"), ("LINEBELOW", (0, 0), (-1, -1), 0.4, LINE),
        ("TOPPADDING", (0, 0), (-1, -1), 2.4), ("BOTTOMPADDING", (0, 0), (-1, -1), 2.8),
        ("ROWBACKGROUNDS", (0, 0), (-1, -1), [colors.white, colors.HexColor("#f7f8fb")]),
    ]))
    story.append(t)
    story.append(Spacer(1, 10))
    story.append(sec("", "Sources and further reading"))
    src = [
        "NSE circulars on lot-size revision (Jan-2026 series: NIFTY 75 → 65) and expiry-day changes; "
        "nseindia.com.",
        "SEBI circular on strengthening the equity index derivatives framework (1 Oct 2024) and the May 2025 "
        "circulars on expiry days and position-limit monitoring; sebi.gov.in.",
        "SEBI study on profit and loss of individual traders in equity F&amp;O, FY25 (July 2025).",
        "Union Budget 2026-27: STT on options raised to 0.15% from 1 Apr 2026.",
        "NSE: pre-open session in equity derivatives from 8 Dec 2025; revised order-entry phases from 7 Sep 2026.",
        "Richard D. Wyckoff, the Wyckoff method (accumulation/distribution); Mark Douglas, <i>Trading in the "
        "Zone</i> (2000); Brett N. Steenbarger, <i>The Daily Trading Coach</i> (2009); Van K. Tharp, <i>Trade "
        "Your Way to Financial Freedom</i> (R-multiples and position sizing).",
    ]
    story += [Paragraph(s_, S["bullet"], bulletText="•") for s_ in src]
    story.append(Spacer(1, 6))
    story.append(callout("guruji", "Beta, the book ends here; the work starts tomorrow at 08:30. Map the levels, "
                                   "size at 1%, wait for your five setups, and be flat by 14:45 on Tuesday. Do that "
                                   "for six months and the market will stop collecting fees from you."))


def build():
    doc = Doc(OUT)
    story = []
    story.append(Spacer(1, 1))
    front_matter(story)
    toc(story)
    seen = set()
    for ch in content_a.CH + content_b.CH:
        chapter(story, ch, ch["part"] not in seen)
        seen.add(ch["part"])
    glossary(story)
    doc.multiBuild(story)
    print("pages:", doc.page)


if __name__ == "__main__":
    build()
