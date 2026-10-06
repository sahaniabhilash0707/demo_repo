# -*- coding: utf-8 -*-
"""Manual text, Part 3 and Part 4 (chapters 14-26), front matter and glossary."""

CH = []

# ============================================================== PART 3
CH.append(dict(
    num=14, part=3, title="Supply and Demand Zones / Order Blocks",
    tagline="Where institutions bought before, they defend again.",
    concept=[
        "A <b>demand zone</b> is a small price area (a 'base' of a few quiet candles) from which price launched "
        "explosively upward. The <b>order block (OB)</b> is the last opposite-colour candle before that "
        "launch: the last red candle before a big rally, or the last green candle before a big fall (supply). "
        "When price returns to the zone, it often reacts strongly.",
    ],
    guruji="A base is where the big boy was still buying when the rocket left. He couldn't fill everything. "
           "When price comes back, his remaining orders are still waiting.",
    why=[
        "Large orders are filled in pieces. The displacement (big candles, 2-3x volume) shows the buyer became "
        "aggressive, often before the full order was filled. Unfilled buy limits remain at the base. On the "
        "return, those orders absorb selling. Because the move away was fast, few retail traders bought there, "
        "so there is little overhead supply from trapped buyers.",
    ],
    charts=[("c14", "Base at 25,606-25,636; the last red candle (OB) is followed by three displacement candles on "
                    "3x volume and a BOS above 25,742. The 13:10 return to the zone gives a 2R long.")],
    example=[
        "NIFTY falls from 25,760 to a base at 25,606-25,636 by 11:05. The last red candle closes at 25,612. From "
        "11:10 to 11:20 three green candles rip to 25,700 on 3x volume, and by 12:00 price breaks the prior lower "
        "high at 25,742 (BOS). In the afternoon NIFTY drifts back down and touches 25,628 at 13:10 with a hammer. "
        "Long 25,645, SL 25,598, target 25,740.",
    ],
    trade=[("Entry", "Long 25,645 on the first bullish 5-min close inside/above the zone"),
           ("Stop-loss", "25,598, below the zone low 25,606 + buffer"),
           ("Target", "25,740, the prior high / BOS level (≈1:2)"),
           ("Valid zone", "Displacement ≥ 3x avg candle size, BOS after it, first return only (fresh zone)"),
           ("Invalid", "Zone already tested twice; return comes with expanding red volume")],
    rule="Only trade fresh zones (first return) that caused a break of structure. Every retest uses up orders; "
         "the third touch usually breaks.",
    mistakes=[
        "Marking every small consolidation as a 'zone'. It must have launched a displacement and a BOS.",
        "Buying the zone against higher-timeframe structure (a demand zone in a 15-min downtrend).",
        "Using zones that are 80 points thick; your SL becomes too wide for 1% risk.",
    ],
    retail="Buying a 'support zone' for the fourth time because it worked three times. Each touch consumes the "
           "buyers, until there are none.",
    summary=["Demand/supply zones are bases that launched displacement and BOS.",
             "The OB is the last opposite candle before the move; the first return is the best.",
             "SL beyond the zone; target the liquidity that the BOS created."],
))

CH.append(dict(
    num=15, part=3, title="Fair Value Gaps (Imbalances)",
    tagline="Price skipped a level. It usually comes back to check it.",
    concept=[
        "A <b>fair value gap (FVG)</b> is a three-candle pattern where candle 2 moves so fast that the high of "
        "candle 1 and the low of candle 3 don't overlap (for a bullish FVG). The gap between them is an area where "
        "only one side traded: an <b>imbalance</b>. Price often returns to fill part of it (often to its 50% "
        "level) before continuing.",
    ],
    guruji="FVG is just a modern name for an old floor saying: 'Jahan market jaldi mein gaya, wahan wapas aayega.' "
           "Where the market went in a hurry, it comes back.",
    why=[
        "During the displacement candle, aggressive buyers lifted every offer. Some passive sellers never got "
        "filled, and some buyers missed the move. On the pullback, those late buyers and the original institution "
        "add at better prices inside the gap. That is why the reaction is often sharp at the FVG's midpoint.",
    ],
    charts=[("c15", "10:35 displacement creates an FVG 25,742-25,768. The 12:00 pullback taps 25,752 (inside "
                    "the gap) and NIFTY continues to 25,812, then 25,850.")],
    example=[
        "Candle 1 (10:30) high 25,742. Candle 2 (10:35) rockets +50 points on the session's largest volume. Candle 3 "
        "(10:40) low 25,768. FVG = 25,742-25,768, midpoint 25,755. NIFTY tops at 25,815 by 11:10, then pulls back "
        "for 50 minutes. At 12:00 a candle wicks to 25,752 and closes 25,761; the next candle closes 25,777. Long "
        "25,757, SL 25,734 (below the FVG), T1 25,812, T2 25,850.",
    ],
    trade=[("Entry", "Long at the FVG midpoint 25,757 with a bullish 5-min close, or limit at 50% of the gap"),
           ("Stop-loss", "25,734, below the FVG low (candle 1 high) + buffer"),
           ("Target", "T1 25,812 previous high (≈1:2.4), T2 25,850 (≈1:4)"),
           ("Filter", "FVG must be created by a displacement that broke structure; trade in trend direction"),
           ("Invalid", "A 5-min close below the FVG low: the imbalance has been fully filled and failed")],
    rule="An FVG is a location, not a signal. Combine it with structure (trend direction) and a confirmation "
         "candle before entering.",
    mistakes=[
        "Trading every tiny 3-point gap on the 1-min chart.",
        "Entering at the top of the FVG with the SL inside it, which almost always gets hit.",
        "Taking FVG longs in a 15-min downtrend.",
    ],
    retail="Chasing the displacement candle at 25,790 instead of waiting for the pullback into the gap at 25,757, "
           "which doubles the stop distance and halves the R:R.",
    summary=["FVG = gap between candle 1 and candle 3 after a displacement.",
             "Price often returns to its 50% level before continuing.",
             "Use it in trend direction, SL beyond the gap, with a confirmation candle."],
))

CH.append(dict(
    num=16, part=3, title="Wyckoff Accumulation and Distribution",
    tagline="Big players need a range to build a position. Learn to read the range.",
    concept=[
        "Richard Wyckoff described how large operators <b>accumulate</b> (buy) in a trading range after a fall and "
        "<b>distribute</b> (sell) in a range after a rise. Accumulation phases: <b>A</b> stopping the fall (selling "
        "climax SC, automatic rally AR, secondary test ST); <b>B</b> building the position inside the range; "
        "<b>C</b> the <b>spring</b>, a false break below the range that shakes out the last sellers; <b>D</b> "
        "sign of strength (SOS) and last point of support (LPS); <b>E</b> markup. Distribution is the mirror "
        "image, with an <b>upthrust</b> instead of a spring.",
    ],
    guruji="The spring is the operator's final exam for retail: 'Will you sell at the lowest price of the day?' "
           "Most people pass the exam by failing it.",
    why=[
        "An operator can't buy 10,000 lots in one candle. He buys slowly inside a range, letting retail sell to "
        "him. The spring triggers every stop below the range, which is the cheapest supply he will ever get. The "
        "low-volume 'test' after the spring shows no sellers are left. Then the SOS breaks the range high and markup "
        "begins. The same logic works on intraday charts, especially 5-min ranges of 2-3 hours.",
    ],
    charts=[("c16", "5-min accumulation: SC at 25,630 (10:05), AR 25,700, range B, spring to 25,622 at 13:10, "
                    "low-volume test at 13:35, SOS above 25,700, LPS and markup to 25,785.")],
    example=[
        "NIFTY falls 170 points to a selling climax at 25,630 (10:05) on the day's biggest volume. The automatic "
        "rally reaches 25,700. For three hours it ranges 25,645-25,700 with shrinking volume. At 13:10 a spring "
        "wicks to 25,622, below the SC low, and closes back inside at 25,647. At 13:35 the test holds 25,652 on "
        "very low volume. Long 25,664, SL 25,618, target 25,755 (range height of 55 projected above 25,700). The "
        "SOS at 13:55 confirms it.",
        "<b>Distribution (mirror):</b> after a rally, an upthrust above the range high on weak follow-through, a "
        "failed retest, then a sign of weakness below the range low. Short the last point of supply.",
    ],
    trade=[("Entry", "Long 25,664 after the low-volume test of the spring (or on the LPS after SOS)"),
           ("Stop-loss", "25,618, below the spring low"),
           ("Target", "25,755: range height projected from the range high (≈1:2)"),
           ("Confirm", "Spring volume < SC volume; test volume lowest of the range; SOS on rising volume"),
           ("Distribution", "Short after upthrust + failed test; SL above upthrust; target range low projection")],
    rule="Never trade inside Phase B. The edge is at the edges: the spring/upthrust (C) and the LPS/LPSY (D).",
    mistakes=[
        "Labelling every range as accumulation. In a downtrend most ranges are re-distribution.",
        "Buying the spring candle itself instead of waiting for the test.",
        "Ignoring volume. Wyckoff without volume is just guessing.",
    ],
    retail="Shorting the 13:10 breakdown below 25,645 'because the range broke', which is the exact sell order the "
           "operator needed to complete his buying.",
    summary=["Ranges after trends are where operators build positions.",
             "The spring/upthrust is a false break that collects the last stops.",
             "Enter on the low-volume test or LPS; SL beyond the spring; target the range projection."],
))

CH.append(dict(
    num=17, part=3, title="Volume and Open Interest Confirmation",
    tagline="Price shows what happened. OI shows who did it.",
    concept=[
        "<b>Open interest (OI)</b> is the number of open futures/options contracts. Reading the <b>change in OI "
        "with price</b> tells you whether new positions are being built or old ones closed:",
        "• Price ↑ + OI ↑ = <b>long build-up</b> (fresh buying, strong).<br/>"
        "• Price ↑ + OI ↓ = <b>short covering</b> (shorts exiting, rally can fade).<br/>"
        "• Price ↓ + OI ↑ = <b>short build-up</b> (fresh selling, strong).<br/>"
        "• Price ↓ + OI ↓ = <b>long unwinding</b> (longs exiting, fall can fade).",
        "In options, <b>writer positioning</b> shows where the walls are: the strike with the highest call OI acts "
        "as resistance, the highest put OI as support. <b>PCR</b> (put-call ratio of OI) gives a crude sentiment "
        "read: above ~1.2 often means heavy put writing (support), below ~0.7 heavy call writing (resistance). Use it "
        "for context, never as a trigger.",
    ],
    guruji="Volume is the noise in the hall. OI is the number of people who stayed seated. A loud rally where "
           "everyone leaves is a party ending, not starting.",
    why=[
        "A rally driven by short covering runs out of fuel when the shorts are done; nobody new committed money. "
        "A rally with rising OI has new longs who will defend their entry. In options, writers are generally "
        "better capitalised than buyers. Where they add OI aggressively, they have the money and the motive to "
        "defend that strike through hedging flows.",
    ],
    charts=[("c17", "Two sessions of NIFTY futures with OI: long build-up, short covering, short build-up and long "
                    "unwinding, each with a different meaning for the next move.")],
    example=[
        "Monday morning NIFTY rises from 25,600 to 25,700 while futures OI climbs from 120 to 138 lakh: long "
        "build-up. In the afternoon price continues to 25,780 but OI drops to 124: short covering, so don't chase. "
        "Tuesday price falls to 25,690 while OI rises to 142: short build-up, so sell rallies. Late Tuesday price "
        "drifts to 25,640 with OI falling: long unwinding, so the fall is losing energy and you should book "
        "profits on shorts.",
        "<b>Options read:</b> if 26,000 CE OI jumps by 40 lakh while NIFTY is at 25,950 and 25,800 PE OI also "
        "rises, writers expect a 25,800-26,000 range. Sell outside it, not inside.",
    ],
    trade=[("Use", "Confirmation filter for setups in Ch 21, not a standalone entry"),
           ("Long filter", "Long build-up or short covering into a demand zone/sweep"),
           ("Short filter", "Short build-up or long unwinding at a supply zone/sweep"),
           ("Option walls", "Highest CE OI = ceiling, highest PE OI = floor; watch intraday shifts every 30 min"),
           ("Caution", "OI data updates with a lag; PCR is sentiment, not timing")],
    rule="Never trade OI alone. OI tells you whose fight it is; price action tells you who is winning right now.",
    mistakes=[
        "Reading PCR = 1.4 as 'market must go up' and buying calls.",
        "Ignoring that call OI can be hedged (covered calls, spreads), not just naked writers.",
        "Checking OI only at 09:15. Writers shift strikes during the day.",
    ],
    retail="Seeing 'huge put writing' on a screener at 10:00, selling puts, and missing that by 13:00 those writers "
           "had rolled down two strikes.",
    summary=["Price + OI tells you whether moves are fresh positions or exits.",
             "Option OI walls show where writers will defend; PCR is context only.",
             "Use OI to confirm price-action setups, never to replace them."],
))

CH.append(dict(
    num=18, part=3, title="Candles in Context",
    tagline="A candle is a word. Location is the sentence.",
    concept=[
        "Four candles are worth knowing: the <b>pin bar</b> (long wick, small body: rejection), the <b>engulfing "
        "candle</b> (body swallows the previous body: control has changed), the <b>inside bar</b> (range inside "
        "the previous bar: compression before expansion), and the <b>marubozu</b> (full body, no wicks: "
        "displacement and intent).",
        "On its own, none of these means anything. A pin bar in the middle of a range is noise. The same pin bar "
        "after a sweep of PDL, at a demand zone, with a volume spike, is a high-quality signal.",
    ],
    guruji="Candlestick books sold millions because they make trading look easy: 'hammer = buy'. In 30 years "
           "I've never seen a hammer make money by itself. Hammer at the right place, with the right people "
           "trapped? That is money.",
    why=[
        "A candle shows the result of a fight within one period. At a liquidity level, that fight is between the "
        "operator and the trapped traders, so the result matters. In the middle of nowhere, the fight is between "
        "small random orders, and the result carries no information about what comes next.",
    ],
    charts=[("c18a", "Same pin bar, two locations: after a sweep of PDL 25,600 (trade) vs in the middle of a "
                     "drift (ignore)."),
            ("c18b", "The four candles worth knowing, schematically, and where each one is valid.")],
    example=[
        "NIFTY drifts down to PDL 25,600 and prints a pin bar: low 25,582, close 25,614, with 3x volume. The sweep "
        "below PDL plus the reclaim plus the volume make it an A-grade signal: long above 25,620, SL 25,578, "
        "target 25,680. An hour earlier, an identical-looking pin bar at 25,650 in the middle of the move led "
        "nowhere: no level, no trapped traders, no volume.",
    ],
    trade=[("Pin bar", "Entry above its high, SL below its wick; valid only at a level / after a sweep"),
           ("Engulfing", "Entry on close, SL beyond the engulfing low/high; valid at zones / VWAP"),
           ("Inside bar", "Entry on break of the mother bar, SL other side; valid in trend, at a level"),
           ("Marubozu", "Not an entry. It shows displacement, so mark the FVG/OB it leaves behind"),
           ("Location check", "PDH/PDL, round number, zone, VWAP, swept liquidity: at least one must be present")],
    rule="Location first, candle second. No level, no trade, however beautiful the candle.",
    mistakes=[
        "Trading candle patterns on the 1-min chart in the middle of the day.",
        "Calling any small body a 'doji reversal'.",
        "Ignoring the volume on the signal candle.",
    ],
    retail="Selling a 'shooting star' at 25,900 in an uptrend with no level above, and getting run over by the "
           "next marubozu.",
    summary=["Four candles: pin bar, engulfing, inside bar, marubozu.",
             "Each is meaningful only at a liquidity level, with volume.",
             "Location is the setup; the candle is just the trigger."],
))

CH.append(dict(
    num=19, part=3, title="Multi-Timeframe Alignment",
    tagline="Daily for direction, 15-min for structure, 5-min for the trigger.",
    concept=[
        "Use three timeframes, each with one job. The <b>daily</b> gives bias and big zones (where are we in the "
        "bigger trend, and where is daily demand/supply?). The <b>15-min</b> gives structure (is the intraday "
        "trend aligned, and has a CHoCH happened at the daily zone?). The <b>5-min</b> gives the trigger (sweep, "
        "engulfing, FVG entry) and a tight stop.",
    ],
    guruji="Bade timeframe ki baat suno, chhote se entry lo. Listen to the big timeframe, take entries from the "
           "small one. Never the other way round.",
    why=[
        "Trades aligned with the higher timeframe have the big money behind them, so pullbacks get bought and "
        "targets get reached. Trades against it fight that flow. The lower timeframe lets you enter with a stop "
        "of 20-40 points instead of 120, which makes 1% risk possible with real size.",
    ],
    charts=[("c19", "Daily uptrend pulls back into daily demand 25,550-25,620; the 15-min shows a CHoCH up at "
                    "25,640; the 5-min gives a sweep to 25,588 and an engulfing entry at 25,624.")],
    example=[
        "<b>Daily:</b> NIFTY is in an uptrend from 24,700 to 25,720 and pulls back to daily demand at "
        "25,550-25,620. Bias is long; for sellers, sell puts or bull put spreads. <b>15-min:</b> the pullback reaches "
        "25,585 and then closes above the last lower high at 25,640, a CHoCH up. <b>5-min:</b> after a sweep of "
        "the 25,600 lows to 25,588, a bullish engulfing closes at 25,622. Long 25,624, SL 25,586, target 25,680 "
        "(about 1.5R), with higher-timeframe targets beyond.",
    ],
    trade=[("Daily", "Trend + zone = bias (long / short / no trade)"),
           ("15-min", "Structure aligned with bias, or a CHoCH at the daily zone"),
           ("5-min", "Trigger: sweep + engulfing / FVG retest / OB reaction"),
           ("Entry/SL", "Long 25,624, SL 25,586 (below the 5-min sweep)"),
           ("Target", "25,680, then the 15-min swing high; R:R ≥ 1:1.5")],
    rule="If daily and 15-min disagree, trade smaller or don't trade. If 5-min is your only reason, it's not a "
         "reason.",
    mistakes=[
        "Taking 5-min short signals inside a daily uptrend at daily demand.",
        "Switching timeframes until one 'agrees' with the trade you want.",
        "Using daily stops with 5-min position size (or vice versa).",
    ],
    retail="Seeing a red 5-min engulfing and selling calls, unaware the daily chart just bounced off a "
           "major demand zone.",
    summary=["Daily = direction and zones; 15-min = structure; 5-min = trigger.",
             "Alignment puts institutional flow behind your trade.",
             "Lower-timeframe entries give tight stops and better R:R at the same 1% risk."],
))

CH.append(dict(
    num=20, part=3, title="VWAP, PDH/PDL/PDC and CPR",
    tagline="Yesterday's levels and today's average are where institutions measure themselves.",
    concept=[
        "<b>VWAP</b> (volume-weighted average price) is the average price paid today, weighted by volume. "
        "Institutions benchmark execution against it: buyers want to buy below VWAP, sellers to sell above it. "
        "<b>PDH/PDL/PDC</b> (previous day high, low, close) are the most-watched intraday liquidity levels.",
        "<b>CPR</b> (central pivot range) uses yesterday's H/L/C: Pivot P = (H+L+C)/3, BC = (H+L)/2, TC = 2P − BC. "
        "A <b>narrow CPR</b> (width under ~0.1% of price) often precedes a trend day; a wide CPR a range day.",
    ],
    guruji="VWAP is the institution's report card. Above it, the buyers are winning the day; below it, the sellers. "
           "Don't argue with the report card.",
    why=[
        "Funds executing large orders through the day use VWAP algorithms. On a trend day, every pullback to VWAP "
        "is where their algorithms buy more, so pullbacks hold there. PDH/PDL collect yesterday's stops, which "
        "is why they get swept or broken with force. CPR summarises yesterday's balance: a narrow CPR means "
        "yesterday was balanced, and balance usually resolves into imbalance (a trend).",
    ],
    charts=[("c20", "PDH 25,880, PDL 25,700, PDC 25,780; narrow CPR 25,783-25,790. The opening dip holds CPR + "
                    "VWAP, the 12:45 VWAP pullback holds, and the PDH break at 13:45 holds.", 0.8)],
    example=[
        "Yesterday: H 25,880, L 25,700, C 25,780, so P = 25,787, BC = 25,790, TC = 25,783: a narrow 7-point CPR. "
        "Today NIFTY opens at 25,805, above CPR. The 09:35 dip to 25,786 holds CPR and VWAP, a long trigger. "
        "NIFTY trends to 25,880 (PDH) by 11:30. At 12:45 a pullback touches VWAP (~25,846) and holds, so you add "
        "or re-enter. At 13:45 PDH breaks and holds, and the buy-stops above it fuel the move to 25,930.",
    ],
    trade=[("Entry", "Long on the first pullback to VWAP that holds with a bullish close (e.g. 25,848)"),
           ("Stop-loss", "15-20 pts below VWAP / below the pullback low (25,830)"),
           ("Target", "PDH 25,880 first, then the next round number / R1"),
           ("Bias", "Open above CPR + above VWAP = long bias; below both = short bias; between = range"),
           ("CPR width", "< 0.1% of spot: expect trend; > 0.4%: expect range (sellers' day)")],
    rule="Don't short above a rising VWAP or buy below a falling VWAP on a trend day. Fight the report card only "
         "at a major liquidity sweep.",
    mistakes=[
        "Using VWAP on the daily chart (it resets every day; it's an intraday tool).",
        "Treating CPR as a magic support instead of a context indicator.",
        "Ignoring PDH/PDL: they are the first places the day's liquidity will be tested.",
    ],
    retail="Shorting NIFTY at 25,880 'because it's PDH resistance' on a narrow-CPR trend day above VWAP. That "
           "short is the fuel for the breakout.",
    summary=["VWAP = today's institutional average; respect its slope.",
             "PDH/PDL/PDC are the first liquidity targets of the day.",
             "Narrow CPR → trend day likely; wide CPR → range day likely."],
))

# ============================================================== PART 4
SETUPS = [
    dict(name="Setup 1 · PDH/PDL Liquidity-Sweep Reversal", chart="s1",
         caption="09:40 wick to 25,628 sweeps PDL 25,650 on a volume spike; entry above the reclaim candle.",
         checklist=["PDH or PDL clearly marked; stops visibly clustered (equal highs/lows near it)",
                    "Wick beyond the level by 10-30 pts on ≥ 2x average volume",
                    "5-min close back inside the level within 1-2 candles",
                    "Not against a strong 15-min trend (or the sweep is at a daily zone)"],
         trigger="Break of the reclaim candle's high (long) / low (short): long 25,667",
         sl="3-5 pts beyond the sweep wick: 25,626 (risk 41 pts)",
         target="T1 PDC / VWAP 25,730 (≈1:1.5), T2 25,760 (≈1:2.3)",
         rr="1:1.5 to 1:2.5", time="09:30-11:00 (best), 13:30-14:30",
         avoid="Trend days with a narrow CPR where price opens beyond the level; event days; wick without volume",
         winrate="Illustrative: in my notes it works roughly 5-6 times out of 10 with proper filters; that is not a "
                 "promise."),
    dict(name="Setup 2 · Failed Opening-Range Breakout (Fade)", chart="s2",
         caption="OR 25,700-25,740; the break below 25,700 has no volume; back inside in 3 candles; the OR-high break "
                 "traps the shorts.",
         checklist=["Opening range 09:15-09:30 marked (width 30-70 pts)",
                    "First break of one side on below-average volume",
                    "Back inside the OR within 3 candles",
                    "Break of the opposite OR side with volume"],
         trigger="Close beyond the opposite OR side: long 25,744 above OR high 25,740",
         sl="Beyond the failed-break extreme: 25,694 (risk 50 pts)",
         target="25,815, next liquidity / 1.5x OR width (≈1:1.4); trail rest",
         rr="1:1.4 to 1:2", time="09:30-10:45 only",
         avoid="OR wider than 100 pts (risk too big for 1%), gap days > 1%, expiry mornings with OI shifting",
         winrate="Illustrative: roughly half the time; profits come from letting winners run to the trail."),
    dict(name="Setup 3 · BOS + Pullback to Order Block / FVG", chart="s3",
         caption="A displacement down breaks the HL at 25,866 (BOS); the pullback into the bearish OB/FVG "
                 "25,840-25,856 on falling volume gives the short.",
         checklist=["15-min trend aligned with the trade direction",
                    "Displacement candle breaks structure (BOS) with ≥ 2x volume",
                    "Clear OB or FVG left behind the displacement",
                    "Pullback into the zone on falling volume; first touch only"],
         trigger="Limit/stop entry inside the zone with a rejection candle: short 25,840",
         sl="Beyond the zone/OB extreme: 25,864 (risk 24 pts)",
         target="T1 25,785 (≈1:2.3), T2 25,740 (≈1:4)",
         rr="1:2 to 1:4", time="10:00-13:30",
         avoid="Zone already tested; pullback with rising volume (that is a reversal, not a pullback); lunch chop",
         winrate="Illustrative: lower win rate than reversals (≈4-5 in 10) but the largest R:R."),
    dict(name="Setup 4 · VWAP Pullback on a Trend Day", chart="s4",
         caption="Higher highs above a rising VWAP; the second touch at 12:35 prints a bullish engulfing; long with "
                 "SL under the touch.",
         checklist=["Open beyond CPR, narrow CPR or strong gap-and-go",
                    "Price holding above a rising VWAP (or below a falling one) for 60+ min",
                    "Pullback to VWAP on lower volume",
                    "Bullish engulfing / pin bar at VWAP"],
         trigger="Close of the engulfing candle at VWAP: long 25,783",
         sl="Below the pullback low: 25,755 (risk 28 pts)",
         target="25,839, previous high / 2R; trail under VWAP after",
         rr="1:2", time="10:30-14:00",
         avoid="Flat VWAP (range day), third touch or later, close below VWAP before entry",
         winrate="Illustrative: works well only on genuine trend days. Use CPR width and opening drive as filters."),
    dict(name="Setup 5 · Expiry-Day Round-Number Rejection (Option Sellers)", chart="s5",
         caption="10:15 sweep of 26,000/PDH to 26,022 with a wick rejection; sell the 26,100/26,300 bear call "
                 "spread above the sweep and the OI wall.",
         checklist=["Expiry Tuesday; heavy call OI at the round number / next strike",
                    "Sweep of PDH / round number with a wick and volume spike before 11:30",
                    "Next 5-min candle closes back below the level",
                    "VIX not rising; no event scheduled that afternoon"],
         trigger="Sell the bear call spread 26,100 / 26,300 after the close back below 25,995",
         sl="Spot: 15-min close above the sweep high 26,022; or spread value 2x the credit",
         target="60-70% of the credit, or 14:45, whichever first",
         rr="Defined: max loss = spread width − credit; size so that max loss ≤ 1% of capital",
         time="Enter 10:00-12:30; flat by 14:45",
         avoid="After 13:30, on news days, when VIX is rising, naked (unhedged) shorts, size > half normal",
         winrate="Illustrative: high win rate, small wins. One unhedged gamma spike can erase 10 wins, so the hedge "
                 "is not optional."),
]

CH.append(dict(
    num=21, part=4, title="Five A+ Setups",
    tagline="Fewer setups, done well, beat many setups done badly.",
    concept=[
        "Everything in Parts 1-3 reduces to a handful of repeatable trades. Each one has a <b>checklist</b> (all "
        "items must be true), a precise <b>trigger</b>, a <b>stop-loss</b> beyond the liquidity, a <b>target</b> at "
        "the next liquidity, a <b>time window</b>, and a list of conditions under which you <b>don't</b> take it. "
        "Grade each trade in your journal: A (all items), B (one missing: half size), C (two or more missing: no trade).",
    ],
    guruji="A professional is not someone who trades a lot. He is someone who waits for his trade, takes it "
           "without fear, and goes home. Five setups are enough for a lifetime.",
    why=[
        "Every setup here trades with the operator, after the liquidity has been taken. Trap reversals (1, 2) "
        "enter after retail has been trapped; continuation trades (3, 4) join institutions at their own price "
        "after a displacement; the expiry seller trade (5) sells premium beyond the liquidity that has already been "
        "swept, with a hedge and a hard time stop.",
    ],
    charts=[],
    setups=SETUPS,
    example=[],
    trade=[],
    rule="If a trade doesn't match one of the five checklists, it isn't a trade. It's entertainment, and "
         "entertainment costs money.",
    mistakes=[
        "Adding a sixth, seventh and eighth setup after a losing week instead of executing five better.",
        "Taking B and C setups at full size.",
        "Skipping the 'when NOT to take it' list because the chart 'looks so good'.",
    ],
    retail="Taking 12 trades a day across 8 'strategies' and calling it diversification. It is noise with "
           "brokerage.",
    summary=["Five setups: sweep reversal, failed ORB, BOS + OB/FVG, VWAP pullback, expiry rejection (sellers).",
             "Each has a checklist, trigger, SL beyond liquidity, target at liquidity, and a time window.",
             "Grade A/B/C; A = full size (1%), B = half, C = no trade."],
))

CH.append(dict(
    num=22, part=4, title="Applying the Setups to Option Selling",
    tagline="Sell where price must work hardest to reach, and leave before the gamma hour.",
    concept=[
        "Option selling is not a separate strategy; it is a different way to express the same price-action view. "
        "The rules are: <b>(1) strike selection</b> beyond the liquidity and beyond the expected range, "
        "<b>(2) always hedged</b> (spreads or condors, max loss known), <b>(3) adjust or exit by rule</b>, never "
        "by hope, and <b>(4) be flat before the expiry-day gamma hour</b>.",
    ],
    guruji="A seller's job is not to be right about where NIFTY goes. It is to be right about where it won't go, "
           "and to be out before he is wrong.",
    why=[
        "After a sweep-and-reject at a high, the liquidity above has been taken. To reach your short strike, price "
        "must find new buyers above a level that just failed. The <b>expected range</b> from India VIX (1-SD daily "
        "move ≈ spot × VIX ÷ 100 ÷ √252; at VIX 14 that is about ±0.9%, or roughly ±230 points) tells you where "
        "about two-thirds of days end. Selling inside it is selling coin flips. Beyond it, and beyond the OI wall, "
        "the odds turn in your favour, as long as you leave before the last-hour gamma spike.",
    ],
    charts=[("c22a", "Strike selection after a sweep to 26,044: sell 26,150 CE (beyond the sweep, the 26,100 OI "
                     "wall and the expected range); hedge with 26,350 CE."),
            ("c22b", "Management on the Chapter 10 path: initial SL 66, a trail after 40% decay to ~39, hit at "
                     "14:20 for +₹1,543 on 2 lots, instead of facing 79 at 15:15.")],
    example=[
        "Expiry Tuesday. NIFTY sweeps 26,044 at 10:25 and rejects. VIX implies about ±90 points for the rest of "
        "the session from 25,995, so roughly 25,905-26,085. The call OI wall is at 26,100. Sell the 26,150 CE / buy "
        "the 26,350 CE (bear call spread). The max loss is known before entry, so size it so that max loss ≤ ₹2,700.",
        "<b>Management</b> (from the c22b chart): sold at 51, initial SL 66 (+30%). Once the premium has decayed "
        "40% (to ~30), the SL trails to <i>low + half the open profit</i> (~39). The 14:20 rally hits it: +11.9 "
        "points × 130 = +₹1,543. Without the trail and cutoff, the same position would show −₹3,640 at 15:15.",
    ],
    trade=[("Strike", "Beyond swept liquidity + OI wall + VIX 1-SD range; delta ≤ 0.15-0.20 at entry"),
           ("Structure", "Bear call / bull put spread or iron condor; never naked on ₹2-5 lakh capital"),
           ("Stop-loss", "Premium +30% (short leg) or spot structure break (15-min close), whichever first"),
           ("Adjust", "Don't roll the threatened side closer. Exit it; re-enter only on a fresh setup"),
           ("Exit", "Trail after 40% decay; book at 60-70%; expiry day: flat by 14:45, no new shorts after 14:00")],
    rule="Sell strikes outside the expected range and beyond the liquidity. Size by max loss, not by margin "
         "available. Be flat by 14:45 on expiry day.",
    mistakes=[
        "Choosing strikes by premium ('I want ₹30') instead of by location.",
        "Using all available margin because 'the strike is far'.",
        "Rolling a losing short closer to collect more premium, which doubles gamma risk.",
    ],
    retail="Selling the 25,850 CE at 51, 35 points OTM on expiry morning. That strike was inside the expected range "
           "and inside the liquidity, so it was a coin flip with unlimited downside.",
    summary=["Strike = beyond swept liquidity, OI wall and the VIX expected range.",
             "Always hedged; size by max loss ≤ 1% of capital.",
             "Trail after 40% decay; book 60-70%; flat by 14:45 on expiry."],
))

CH.append(dict(
    num=23, part=4, title="Risk Management",
    tagline="Analysis decides if you make money. Risk management decides if you stay in the game.",
    concept=[
        "<b>Risk per trade = 1% of capital.</b> At ₹2,70,000 that is <b>₹2,700</b>. <b>Daily loss limit = 2%</b> "
        "(₹5,400): once hit, the day is over. <b>Weekly circuit breaker = 6%</b> (₹16,200): no trading until next "
        "Monday. <b>Expiry-day cutoff 14:45.</b> <b>No averaging losers, ever.</b>",
        "<b>Position-size formula:</b> Lots = floor( Risk₹ ÷ (SL distance in premium points × lot size) ), capped at "
        "your max-lots rule. With lot size 65: SL 15 premium points → ₹975 risk per lot → floor(2,700 ÷ 975) = "
        "<b>2 lots</b>. For a spot-based stop, convert: premium SL ≈ spot SL × option delta. A 40-point spot stop on "
        "a 0.35-delta option ≈ 14 premium points → ₹910 per lot → 2 lots. For spreads, use max loss per lot "
        "(spread width − credit) × 65.",
    ],
    guruji="I have seen brilliant analysts go broke and average analysts retire rich. The difference was never the "
           "chart. It was the size.",
    why=[
        "Losing streaks are guaranteed, even for good systems. With 1% risk, seven losses in a row cost ~6.8%; with "
        "10% risk they cost ~52%. And recovery is asymmetric: a 46% drawdown needs +85% to get back. Averaging "
        "a loser turns a planned 1R loss into an unplanned 5-15R loss, which no win rate can repay.",
    ],
    charts=[("c23a", "Same 150 trades (45% win rate, +1.4R / −1R): 1% risk ends at ₹2.84L (max drawdown ~21%); 10% "
                     "risk ends at ₹1.74L after falling to ~₹17,000 (−94%)."),
            ("c23b", "Averaging a losing short: 1 lot at 40 (risk ₹780) becomes 6 lots at an average of 68.5 and a "
                     "₹10,725 loss (~14x the plan).")],
    example=[
        "Your capital is ₹2,70,000. Setup 1 gives a long NIFTY trigger at 25,667 with SL 25,626 (41 spot points). "
        "You sell a bull put spread instead: the short 25,600 PE has delta ≈ 0.30, so the premium SL is ≈ 12 points. "
        "Risk per lot = 12 × 65 = ₹780. Lots = floor(2,700 ÷ 780) = 3, but your max-lots rule says 2 → <b>2 "
        "lots</b>, risk ₹1,560.",
        "Daily check: trade 1 loses ₹1,560, trade 2 loses ₹2,700 → day = −₹4,260. One more full loss would breach "
        "₹5,400, so the third trade is allowed only at a size that keeps the day above −₹5,400 (1 lot), or not at all.",
    ],
    trade=[("Risk/trade", "1% = ₹2,700 (max 2% only after 3 green months)"),
           ("Daily limit", "2% = ₹5,400 → stop for the day; 2 consecutive losses → stop"),
           ("Weekly", "6% = ₹16,200 → stop until next Monday; after a losing week, half size"),
           ("Expiry", "No new shorts after 14:00; flat by 14:45; expiry size ≤ half normal"),
           ("Never", "Average a loser · widen an SL · trade without an SL order placed in the system")],
    rule="The stop-loss is an order in Kite within 30 seconds of entry, not a number in your head. A mental "
         "stop is not a stop.",
    mistakes=[
        "Sizing by available margin ('I can afford 10 lots') instead of by stop distance.",
        "Moving the SL further away 'to give it room'.",
        "Raising size to recover losses faster. That is exactly how ₹5 lakh became ₹2.7 lakh.",
    ],
    retail="'Margin is ₹1.8 lakh, I have ₹2.7 lakh, so I can do 5 lots.' Margin tells you what the broker allows, "
           "not what your account can survive.",
    summary=["1% per trade, 2% per day, 6% per week. Hard limits.",
             "Lots = Risk₹ ÷ (premium SL × 65), capped by max lots.",
             "Never average losers; the SL is an order, not a thought."],
))

CH.append(dict(
    num=24, part=4, title="Trader Psychology",
    tagline="The market doesn't take your money. Your next trade after a loss does.",
    concept=[
        "Three psychological failures destroy small accounts: <b>revenge trading</b> (trading to win back a loss "
        "now), <b>tilt</b> (a state where emotion overrides rules and size rises as discipline falls), and "
        "the <b>recovery mindset</b> (seeing every trade as a chance to get back to the old peak instead of as "
        "one execution of an edge).",
    ],
    guruji="Loss ke baad market tumhe nahi bulata, tumhara ego bulata hai. After a loss, the market isn't calling "
           "you; your ego is. Let it ring.",
    why=[
        "After a loss, the brain treats the money as something that was taken from you and must be recovered now. "
        "That raises risk-taking, so you get bigger size, no SL and lower-quality setups, at exactly the moment "
        "your judgement is worst. Mark Douglas called this a failure to accept risk. Brett Steenbarger's work with "
        "prop traders shows the fix is process: pre-set limits, a forced break, and review of the decision, not the "
        "outcome.",
    ],
    charts=[("c24a", "A tilt day on ₹2.7 lakh: size grows 1 → 2 → 4 → 6 → 8 lots as emotions escalate; −₹50,500 "
                     "(−19%) in one session. The daily limit was hit after trade 3."),
            ("c24b", "The math of recovery: −46% needs +85%; −50% needs +100%. Small losses are recoverable, big "
                     "ones change your life.")],
    example=[
        "A 10:05 loss of ₹1,300 is a normal, planned loss. At 10:20 the trader doubles size 'to get it back' "
        "(−₹2,600). At 10:40 four lots without an SL (−₹7,800): the day is now −₹11,700, more than twice the daily "
        "limit. A small win at 11:30 feels like 'I'm back'. Six lots at 12:10, eight lots into expiry at 14:50: "
        "−₹50,500. Not one of these losses was caused by the market. All of them were caused by not stopping "
        "after trade 3.",
        "<b>How pros handle drawdowns:</b> cut size by half after a 5% drawdown, by half again after 10%; trade "
        "only A setups; review the journal daily; return to full size only after two green weeks.",
    ],
    trade=[("After a loss", "15-minute break, away from the screen; write one line about why it happened"),
           ("2 losses", "Done for the day: the daily limit and consecutive-loss limit both exist for this"),
           ("Drawdown 5%", "Half size; A setups only"),
           ("Drawdown 10%", "Quarter size or paper-trade one week; review every trade in the journal"),
           ("Recovery", "Target the process (100% rule adherence), not the money (₹ back to peak)")],
    rule="When the journal's STOP flag turns red, close the terminal. Log out of Kite. It is the most profitable "
         "click you will make all month.",
    mistakes=[
        "Reading every loss as personal ('the market is against me').",
        "Measuring a day by P&amp;L instead of by rule adherence.",
        "Sharing positions in groups for validation, then holding losers to save face.",
    ],
    retail="Trying to recover ₹2.3 lakh in a month. At 1% risk, recovery takes many months. Trying to do it in "
           "weeks needs 10% risk, and 10% risk is what caused the drawdown.",
    summary=["Revenge and tilt show up as rising size and falling rule adherence.",
             "Hard limits plus forced breaks beat willpower.",
             "Recovery is a process goal: execute well; the money follows slowly."],
))

CH.append(dict(
    num=25, part=4, title="The Daily Routine",
    tagline="Amateurs trade the market. Professionals trade their routine.",
    concept=[
        "A fixed routine removes decisions from emotional moments. It has three blocks: <b>pre-market</b> "
        "(08:30-09:15) to prepare the map, <b>in-session</b> to execute only inside defined time windows, and "
        "<b>post-market</b> (15:30-16:00) to journal and review.",
    ],
    guruji="I still write my levels by hand every morning after 30 years. Not because I forget them, but because "
           "writing them makes me commit before the noise starts.",
    why=[
        "Most bad trades are made in the first 15 minutes (reacting to the gap), in the lunch chop (boredom) and "
        "in the last hour on expiry (greed). A routine that blocks those windows removes most of the damage "
        "before it happens.",
    ],
    charts=[("c25", "The session as time zones: observe 09:15-09:30, prime window 09:30-11:30, lunch chop "
                    "11:30-13:30, second window 13:30-14:45, expiry exit after 14:45.")],
    example=[
        "<b>Pre-market (20 min):</b> GIFT Nifty and global cues; India VIX and the 1-SD range; PDH/PDL/PDC, CPR, "
        "round numbers, equal highs/lows; option chain: max pain, CE/PE OI walls; event calendar; the journal's "
        "PRE-MARKET row (emotional state, sleep, 'trading to recover?'). If the sheet says NO TRADE, the day is "
        "observation only.",
        "<b>In-session:</b> no trades 09:15-09:30. A+ setups 1-3 in the prime window; setups 4-5 in the second "
        "window; lunch only at half size. SL order within 30 seconds of entry. Check the DASHBOARD after each "
        "trade. Expiry: no new shorts after 14:00, flat by 14:45.",
        "<b>Post-market (15 min):</b> complete every TRADE LOG row (MAE/MFE from the Kite chart), screenshot each "
        "trade, write one lesson, grade the day on rule adherence. Friday: WEEKLY REVIEW, choose one change.",
    ],
    trade=[("08:30-09:15", "Map: levels, VIX range, OI walls, events, emotional check"),
           ("09:15-09:30", "Observe only; mark the opening range"),
           ("09:30-11:30", "Prime window: setups 1, 2, 3"),
           ("11:30-13:30", "Lunch chop: half size or none"),
           ("13:30-14:45", "Second window: setups 4, 5; expiry exits from 14:40")],
    rule="No pre-market map, no trading. If you missed the preparation, the day is observation only.",
    mistakes=[
        "Opening the terminal at 09:14 with no levels marked.",
        "Trading all session because the screen is open.",
        "Skipping the journal on losing days, which are exactly the days that teach the most.",
    ],
    retail="Spending the evening on Telegram tips instead of 15 minutes on the journal. Tips are someone "
           "else's liquidity plan.",
    summary=["Pre-market map, time-boxed execution, post-market journal.",
             "Block the dangerous windows: the first 15 minutes, lunch, and the expiry last hour.",
             "The routine is the edge that protects every other edge."],
))

CH.append(dict(
    num=26, part=4, title="The One-Page Cheat Sheet",
    tagline="Print it. Keep it next to the screen.",
    concept=[
        "Every trap in Part 2 and every setup in Part 4 fits in one table: what you see, what it means, and what "
        "to do. Print the next page and keep it beside your trading screen. Read it before the open and after "
        "every loss.",
    ],
    guruji="When the market is moving fast, nobody thinks clearly, including me. That's why pilots use "
           "checklists. Use yours.",
    why=[
        "Under stress, recognition beats reasoning. The 12 thumbnails train your eye to recognise the shapes "
        "quickly; the table tells you the response you decided on when you were calm.",
    ],
    charts=[("c26", "The 12 shapes to recognise: nine traps and three smart-money footprints.", 0.8)],
    example=[
        "Live use: at 09:40 NIFTY wicks below PDL on a volume spike. Glance at the sheet: 'SL hunt / PDL sweep → "
        "wait for close back inside → Setup 1'. The decision takes five seconds because you made it last night.",
    ],
    trade=[("Risk card", "1R = ₹2,700 · day −₹5,400 · week −₹16,200 · max 2 lots · max 3 trades"),
           ("Size", "Lots = floor(2,700 ÷ (premium SL × 65))"),
           ("Expiry", "Tuesday · no new shorts after 14:00 · flat by 14:45"),
           ("Never", "Average losers · trade without an SL order · trade after the STOP flag"),
           ("Verify", "Lot 65, Tuesday expiry, charges: re-check NSE/broker circulars each June & December")],
    rule="If it is not on the sheet, don't trade it.",
    mistakes=["Keeping the cheat sheet in a folder instead of next to the screen.",
              "Adding new patterns after a losing day.",
              "Reading it only after the trade, not before."],
    retail="Knowing every pattern and still trading by impulse. Knowledge without a checklist is a "
           "library, not a system.",
    summary=["Twelve shapes, five setups, one risk card.",
             "Decide calmly in advance; execute by recognition.",
             "The sheet beats the impulse, every time."],
    cheatsheet=True,
))

CHEAT_TRAPS = [
    ("Bull / bear trap (Ch 5)", "Break of a level on LOW volume, back inside in ≤3 candles",
     "Breakout buyers/sellers trapped", "Trade the failure; SL beyond trap extreme; target range opposite"),
    ("Stop-loss hunt (Ch 6)", "Long wick beyond triple-touched level + volume spike, close back inside",
     "Stops filled big orders", "Enter on reclaim; SL beyond wick; sellers sell premium after it"),
    ("Gap trap (Ch 7)", "Gap 0.4-1%, first 15-min range breaks against the gap",
     "Opening emotion was exit liquidity", "Trade toward PDC; SL other side of opening range"),
    ("Opening-range fake (Ch 8)", "First OR break fails within 3 candles",
     "ORB orders harvested", "Trade opposite OR break; genuine = volume + retest"),
    ("Round-number / max-pain pin (Ch 9)", "Expiry: heavy CE+PE OI at round strike, small excursions fail",
     "Writers' hedging pulls price back", "Fade excursions; don't buy OTM breakouts; flat by 14:45"),
    ("Expiry gamma spike (Ch 10)", "Short near the strike after 14:00; spot accelerating toward it",
     "Delta jumps 0.1 → 0.9 within ~60 pts", "Trail after 40% decay; hard exit 14:45; half size"),
    ("Theta / gamma trap (Ch 11)", "Buyer: flat range for days. Seller: trend day vs short strangle",
     "Time kills buyers; gamma kills sellers", "Buyers: momentum + time stop. Sellers: hedged, exit at 2x"),
    ("Event whipsaw (Ch 12)", "RBI / Budget / Fed / CPI headline spike then reversal",
     "Both sides' stops hunted; IV crush", "No trades ±15/30 min; trade retest of pre-event range"),
    ("Pattern / trendline fake (Ch 13)", "Perfect triangle / double top breaks quietly, then fails",
     "Pattern traders' orders harvested", "Trade the failure or the loud second break"),
]
CHEAT_SETUPS = [
    ("1 Sweep reversal", "PDH/PDL sweep + volume + reclaim", "Above/below reclaim candle", "Beyond wick",
     "PDC / VWAP, 1:1.5-2.5", "09:30-11:00"),
    ("2 Failed ORB", "First OR break fails, opposite side breaks", "Close beyond opposite OR side",
     "Failed-break extreme", "1.5x OR width, 1:1.4-2", "09:30-10:45"),
    ("3 BOS + OB/FVG", "Displacement BOS, pullback on low volume", "Rejection inside zone",
     "Beyond zone", "Next liquidity, 1:2-4", "10:00-13:30"),
    ("4 VWAP pullback", "Trend day, rising VWAP, 1st/2nd touch", "Engulfing at VWAP", "Below pullback low",
     "Prior high, 1:2", "10:30-14:00"),
    ("5 Expiry rejection (sell)", "Sweep of round no./PDH before 11:30", "Bear call / bull put spread",
     "15-min close beyond sweep / 2x credit", "60-70% credit or 14:45", "10:00-12:30, flat 14:45"),
]

FACTS = [
    ("NIFTY lot size", "65 units (from the Jan-2026 contract series; it was 75). NSE reviews lot sizes every "
                       "June and December."),
    ("Weekly expiry", "Tuesday (since Sep 2025). Monthly expiry: last Tuesday of the month."),
    ("Weekly contracts", "One weekly index expiry per exchange (since Nov 2024): NSE = NIFTY only; BANKNIFTY, "
                         "FINNIFTY, MIDCPNIFTY are monthly."),
    ("Expiry-day margin", "Additional 2% extreme loss margin on short index options on expiry day (since Nov 2024); "
                          "no calendar-spread margin benefit on expiry day (since Feb 2025)."),
    ("Other SEBI measures", "Minimum contract value ₹15 lakh at introduction; upfront collection of option premium; "
                            "intraday monitoring of position limits (Apr 2025); delta-based (FutEq) position limits "
                            "(Oct 2025)."),
    ("Pre-open session", "Index and stock futures have a 09:00-09:15 pre-open auction (since 8 Dec 2025); the "
                         "order-entry phases were revised from 7 Sep 2026."),
    ("STT on options", "0.15% of premium on the sell side (from 1 Apr 2026, Union Budget 2026-27; was 0.10%)."),
    ("Watch list", "Reports in Aug 2026 that regulators were considering further curbs on weekly expiries; not "
                   "enacted as of 6 Oct 2026. Always verify on nseindia.com and sebi.gov.in."),
]

GLOSSARY = [
    ("ATM / ITM / OTM", "At-, in-, out-of-the-money: strike at, favourable to, or beyond spot for the option holder."),
    ("Bakra", "Slang: the 'goat', the trader whose losses become someone else's profit."),
    ("BOS", "Break of structure: candle close beyond the last swing in the trend direction."),
    ("CHoCH", "Change of character: first close beyond the last swing against the trend."),
    ("CPR", "Central pivot range: Pivot (H+L+C)/3, BC (H+L)/2, TC 2P−BC from the previous day."),
    ("Delta", "Change in option price per 1-point move in spot (0 to 1 for calls)."),
    ("Demand / supply zone", "Base from which price displaced up / down; unfilled orders remain there."),
    ("Displacement", "Fast, large-bodied, high-volume move showing institutional intent."),
    ("DTE", "Days (trading) to expiry. 0 = expiry day."),
    ("ELM", "Extreme loss margin; +2% on short index options on expiry day."),
    ("Equal highs / lows", "Two or more swing points at the same price; double the resting stops."),
    ("FII / DII", "Foreign / domestic institutional investors."),
    ("FVG", "Fair value gap: gap between candle 1 and candle 3 after a displacement candle."),
    ("Gamma", "Rate of change of delta; explodes near the strike close to expiry."),
    ("Inducement", "A small move designed to attract traders and place their stops predictably."),
    ("IV / IV crush", "Implied volatility; its sharp fall after an event, which cuts option premiums."),
    ("Liquidity", "Resting orders (stops, limits, breakout entries) that large players need to fill size."),
    ("LPS / LPSY", "Last point of support / supply in Wyckoff phase D."),
    ("MAE / MFE", "Maximum adverse / favourable excursion during a trade."),
    ("Max pain", "Strike at which option buyers lose the most at expiry."),
    ("OI", "Open interest: number of outstanding contracts."),
    ("Operator", "Slang: a large player able to move price to harvest liquidity."),
    ("Order block (OB)", "Last opposite-colour candle before a displacement."),
    ("OR / ORB", "Opening range (09:15-09:30) / opening-range breakout."),
    ("PCR", "Put-call ratio of open interest; a sentiment gauge."),
    ("PDH / PDL / PDC", "Previous day high / low / close."),
    ("R / R-multiple", "1R = planned risk; result expressed in units of planned risk."),
    ("SL hunting", "Moving price through a stop cluster to fill large orders."),
    ("Spring / upthrust", "False break below / above a Wyckoff range that traps traders."),
    ("Sweep", "Fast move beyond a liquidity level that triggers stops, then reverses."),
    ("Theta", "Time decay: premium lost per day/hour, fastest near expiry."),
    ("Tilt", "Emotional state in which rules are abandoned; size rises as discipline falls."),
    ("VIX (India)", "Expected annualised volatility of NIFTY; 1-SD day ≈ spot × VIX ÷ 100 ÷ √252."),
    ("VWAP", "Volume-weighted average price for the session; institutional benchmark."),
    ("Writer", "Option seller; collects premium, carries the obligation."),
]
