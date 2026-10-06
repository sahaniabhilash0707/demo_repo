# -*- coding: utf-8 -*-
"""Manual text, Part 1 and Part 2 (chapters 1-13). Numbers match the charts in charts/."""

CH = []

# ============================================================== PART 1
CH.append(dict(
    num=1, part=1, title="Who Moves NIFTY",
    tagline="Know the players before you sit at the table.",
    concept=[
        "NIFTY does not move because of your analysis. It moves because large orders hit the market. Five groups place "
        "those orders, and each has a different job, time horizon and edge.",
        "<b>FIIs</b> (foreign portfolio investors) move thousands of crores through cash and futures; their flow "
        "creates the trend of the day and the week. <b>DIIs</b> (mutual funds, insurance) absorb FII selling with SIP "
        "money and buy dips patiently. <b>Prop desks and algos</b> are fast, well capitalised and live on the first "
        "and last hour, scalping liquidity. <b>Option writers</b> (institutions, HNIs, desks) sell premium and defend "
        "strikes with heavy open interest. <b>Retail</b> is the largest group by headcount and the smallest by "
        "capital, and it arrives late.",
    ],
    guruji="On the BSE floor in '94, we had a saying: 'Every trade has two sides, beta. If you can't see who is on "
           "the other side, it is you.' Retail is the counterparty institutions need, not the competition.",
    why=[
        "Big money cannot buy ₹500 crore at one price. It needs someone to sell to it. The easiest sellers are "
        "traders who are scared (stop-losses) or greedy (shorting tops, buying puts at lows). So big players engineer "
        "moves that make retail do the opposite of what they need. "
        "SEBI's FY25 study found 91% of individual F&amp;O traders lost money, with an average net loss of about ₹1.1 "
        "lakh. That is the food chain: retail's losses are the desks' income.",
    ],
    charts=[("c01", "One session, five players: algos at the open, FII trend, writers pinning 25,900, retail buying the "
                    "14:45 breakout, and the reversal that turns those buyers into exit liquidity.")],
    example=[
        "Look at the chart. NIFTY opens at 25,780. The first 30 minutes chop 40 points either way. That is algos "
        "hunting the overnight stops. From 10:15 to 12:30 an FII buy programme lifts NIFTY steadily to 25,900 with "
        "shallow pullbacks. From 12:45 to 14:15 price is glued to 25,900, the strike with the heaviest call and put "
        "OI: writers are collecting theta. At 14:45 NIFTY pokes to 25,935 and retail buys 'the breakout'. Within 30 "
        "minutes it is back at 25,860.",
        "Who sold to those breakout buyers? Writers hedging, prop desks booking the day's long, and FIIs completing "
        "their programme. The retail buyer paid the top price to give them exit liquidity.",
    ],
    trade=[("Rule", "Trade only with the dominant player of that time window"),
           ("Entry", "Join the FII trend on pullbacks (10:00-12:30), never chase late breakouts"),
           ("Stop-loss", "Below the last higher-low of the trend leg (e.g. 25,835 at 11:30)"),
           ("Target", "Previous day high / round number where writers sit (25,900)"),
           ("Avoid", "New positions after 14:30 on expiry day; first 15 minutes")],
    rule="Before every trade, write one line: 'Who is on the other side of this trade, and why are they wrong?' "
         "If you can't answer, don't trade.",
    mistakes=[
        "Treating NIFTY like a fair coin, when it is a game with insiders who see the order book.",
        "Buying the move only after it is obvious on the 15-min chart, which is the moment institutions finish.",
        "Ignoring time of day: the same candle means different things at 09:20, 12:30 and 14:50.",
    ],
    retail="Seeing a green candle at 14:45 and thinking 'it's breaking out'. That candle is usually a desk "
           "unloading into your buy order.",
    summary=["FIIs make the trend, writers make the range, algos make the noise. Retail provides the liquidity.",
             "Each time window has a dominant player. Trade with them, not against them.",
             "If you can't name the trapped side of a move, you probably are the trapped side."],
))

CH.append(dict(
    num=2, part=1, title="Liquidity: Where the Orders Sit",
    tagline="Price goes where the orders are.",
    concept=[
        "Liquidity means resting orders: stop-losses, breakout entries and limit orders. Institutions need it to fill "
        "large positions without moving price against themselves. Liquidity pools form at <b>obvious</b> places:",
        "• Swing highs and lows, especially equal highs/lows (double the stops).<br/>"
        "• Round numbers: 25,500, 26,000, 26,500 (and 22,500/23,000 in older years).<br/>"
        "• Previous day high (PDH), low (PDL) and close (PDC).<br/>"
        "• The opening-range high and low (09:15-09:30).<br/>"
        "• Trendlines and 'textbook' support/resistance that every YouTube trader draws.",
    ],
    guruji="Market ka ek hi niyam hai: the more obvious the level, the more orders sit there, and the more "
           "valuable it is to the operator. An obvious level is a target, not protection.",
    why=[
        "Above a swing high sit buy-stops: short sellers' stop-losses (buy orders) plus breakout buyers' entry "
        "orders. Below a swing low sit sell-stops. A big seller who wants to short 5,000 lots needs 5,000 lots of "
        "buying. Where does he find it all at once? Just above the equal highs. That is why price so often 'pokes' "
        "a level and reverses: the poke was the fill.",
    ],
    charts=[("c02", "A liquidity map: buy-stops above equal highs 25,991, the 26,000 round number and PDH 26,020; "
                    "sell-stops below the opening range, the trendline and PDL 25,905.")],
    example=[
        "In the chart, NIFTY has made equal highs at 25,991 twice, just under 26,000 and PDH 26,020. That 30-point "
        "band holds three layers of buy orders. Below, the opening-range low 25,922, the rising trendline and PDL "
        "25,905 stack sell orders. Before taking any trade, mark these two pools. The question is never 'will it go "
        "up?' but 'which pool will be taken first, and what happens after?'",
    ],
    trade=[("Rule", "Map liquidity before 09:15; never place your SL exactly at an obvious level"),
           ("Entry", "Only after a pool is taken (swept) and price rejects it"),
           ("Stop-loss", "Beyond the sweep extreme, not at the obvious level (e.g. above 26,035, not 25,995)"),
           ("Target", "The opposite liquidity pool (e.g. 25,905 PDL)"),
           ("Map", "PDH, PDL, PDC, round numbers, OR high/low, equal highs/lows, OI walls")],
    rule="Your stop-loss must sit where the operator does not want price to go, never where every other trader's "
         "stop sits. Add a buffer of 10-15 NIFTY points beyond obvious levels.",
    mistakes=[
        "Putting the SL exactly 5 points below support, which is exactly where the hunt goes.",
        "Buying 'just above resistance' when that is precisely the buy-stop pool sellers are waiting for.",
        "Treating round numbers as magic support/resistance instead of as magnets for liquidity.",
    ],
    retail="Drawing the same trendline as 50,000 other traders and placing the stop just below it. You've "
           "volunteered as liquidity.",
    summary=["Liquidity = resting orders. It sits at obvious highs, lows, round numbers and PDH/PDL.",
             "Price is pulled toward liquidity before the real move.",
             "Mark the pools before the open; trade after a pool is taken, not before."],
))

CH.append(dict(
    num=3, part=1, title="Inducement and the Sweep",
    tagline="First they build the trap, then they spring it.",
    concept=[
        "Liquidity is first <b>created</b> and then <b>harvested</b>. Creation is called <b>inducement</b>: a small, "
        "convincing move that pulls traders in and makes them place stops in a predictable place. Harvesting is the "
        "<b>sweep</b> (or stop hunt): a fast spike through that place, filling large orders against the stops, "
        "followed by <b>displacement</b>, a strong move in the real direction.",
    ],
    guruji="Bakra ko pehle chara dikhate hain, phir halaal karte hain: first you show the goat the grass, then you "
           "take it. Inducement is the grass.",
    why=[
        "An institution that wants to go long must buy from sellers. Inducement creates those sellers: a small "
        "break up pulls in breakout buyers whose stops sit under the range; equal lows pile up more stops. When the "
        "sweep hits those stops, they become market sell orders, which the institution absorbs with its buy limit. "
        "The volume spike on the sweep candle is the fingerprint of that transfer.",
    ],
    charts=[("c03", "Equal lows at 25,810 build sell-stops; a small break of the minor high (inducement) adds more; "
                    "the 11:40 wick to 25,788 sweeps them on 3x volume; displacement follows.")],
    example=[
        "NIFTY ranges between 25,810 and 25,848 for two hours. Longs keep their SL at 25,800. At 11:00 a candle "
        "breaks the minor high to 25,859 and breakout buyers jump in with stops below 25,810. At 11:40 a single "
        "candle wicks to 25,788 on the day's highest volume and closes back at 25,809. The next three candles close "
        "at 25,826, 25,844 and 25,855. The sweep is complete and NIFTY reaches 25,905 by 13:15.",
    ],
    trade=[("Entry", "Long 25,826, on the first close back above the swept level 25,810"),
           ("Stop-loss", "25,785 (3 points below the sweep wick 25,788)"),
           ("Target", "T1 25,860 (inducement high), T2 25,905; R:R about 1:0.8 / 1:1.9"),
           ("Filter", "Sweep candle volume ≥ 2x the 20-bar average; close back inside within 2 candles"),
           ("Time", "Best 09:30-11:30 and 13:00-14:30")],
    rule="No volume spike on the sweep, no trade. A slow drift below the level is a breakdown, not a sweep.",
    mistakes=[
        "Entering during the sweep candle (catching a falling knife) instead of after it closes back inside.",
        "Calling every dip a sweep. A real sweep is fast, on high volume, and is reclaimed quickly.",
        "Placing your own stop at the same obvious place the sweep just cleaned.",
    ],
    retail="Buying the inducement breakout at 25,859 with a stop at 25,805, then getting swept at 25,788 and "
           "watching NIFTY go to 25,905 without you.",
    summary=["Inducement creates stops; the sweep harvests them; displacement is the real move.",
             "Confirm a sweep by volume and a quick close back inside the level.",
             "Enter after the reclaim, SL beyond the wick, target the opposite liquidity."],
))

CH.append(dict(
    num=4, part=1, title="Market Structure: HH/HL, BOS and CHoCH",
    tagline="Structure tells you whose side to be on.",
    concept=[
        "An uptrend is a series of <b>higher highs (HH)</b> and <b>higher lows (HL)</b>; a downtrend, <b>lower highs "
        "(LH)</b> and <b>lower lows (LL)</b>. A <b>break of structure (BOS)</b> is a candle close beyond the last "
        "swing in the trend direction: it confirms continuation. A <b>change of character (CHoCH)</b> is the first "
        "close beyond the last swing <i>against</i> the trend, for example below the last HL in an uptrend. It "
        "is the earliest warning that control has changed hands.",
        "<b>External structure</b> is the major swings that defined the trend (on 15-min). <b>Internal "
        "structure</b> is the smaller wiggles inside a leg (on 5-min). Trade the external, time entries with the "
        "internal.",
    ],
    guruji="Trend is your friend only till the CHoCH. After that, he's a stranger. Don't lend him money.",
    why=[
        "A higher low exists because buyers defended it. When price closes below that low, the buyers who defended "
        "it are now trapped and their stops are below. Their forced selling feeds the new direction. That is why "
        "a CHoCH often precedes a sharp move, and why a BOS in trend direction attracts fresh participants.",
    ],
    charts=[("c04", "15-min, three sessions: HH/HL with BOS in the uptrend, CHoCH on Thursday afternoon when the last "
                    "HL (~25,740) breaks, then LH/LL and a bearish BOS on Friday.")],
    example=[
        "Wednesday and Thursday morning print clean HH/HL with BOS each time. On Thursday afternoon, after a final HH "
        "near 25,790, the pullback breaks the last HL around 25,740 on a 15-min close. That's the CHoCH. On Friday "
        "the bounce fails at a lower high near 25,770 and a bearish BOS below 25,708 confirms the downtrend. The "
        "short entry comes at the LH, not at the CHoCH itself.",
    ],
    trade=[("Entry", "Short at the first LH after CHoCH (~25,765-25,770) when a 5-min bearish candle confirms"),
           ("Stop-loss", "25,792, above the lower high"),
           ("Target", "Next sell-side liquidity: 25,708 swing low, then 25,680"),
           ("R:R", "About 1:2.5 to the first target"),
           ("Bias", "Uptrend = buy dips / sell puts; downtrend = sell rallies / sell calls")],
    rule="Only trade in the direction of 15-min external structure. A CHoCH means stop trading the old trend; it "
         "doesn't by itself mean trade the new one.",
    mistakes=[
        "Labelling every 5-min wiggle as a HH or LL. Use 15-min swings for structure.",
        "Shorting immediately on CHoCH instead of waiting for the lower high (a retest).",
        "Ignoring a CHoCH because your bias 'feels' bullish.",
    ],
    retail="Selling puts 'because the trend is up' on Friday morning, after Thursday's CHoCH already told you "
           "the trend had changed.",
    summary=["HH/HL = up, LH/LL = down. BOS confirms, CHoCH warns.",
             "Structure from 15-min, entries from 5-min.",
             "After a CHoCH, wait for the first lower high (or higher low) to enter."],
))

# ============================================================== PART 2
CH.append(dict(
    num=5, part=2, title="The False Breakout (Bull and Bear Traps)",
    tagline="The breakout everyone sees is the one that fails.",
    concept=[
        "A <b>bull trap</b> is a break above resistance that quickly closes back below it; a <b>bear trap</b> is the "
        "mirror image below support. Breakout traders who bought (or sold) the break are now trapped, and their "
        "stops become fuel for the move in the opposite direction.",
    ],
    guruji="When a level has been touched three times and everyone is waiting for the break, ask: who is left to "
           "buy after the breakout traders are in? Usually nobody.",
    why=[
        "A breakout needs new aggressive buyers. When the breakout candle has <b>less</b> volume than the rejection "
        "candles before it, institutions aren't participating. The only buyers are retail breakout orders and "
        "short-covering stops, which is exactly the liquidity a seller needs. Once those orders are filled, there "
        "is no fuel left, and price falls back into the range.",
    ],
    charts=[("c05a", "Bull trap: two rejections at 25,950, an 11:50 breakout to 25,973 on low volume, a close back "
                     "inside at 12:00, and a fall to 25,880."),
            ("c05b", "Bear trap: support 25,700 breaks to 25,681 on weak volume; the 12:00 reclaim candle has 3x "
                     "the volume and NIFTY rallies to 25,790.")],
    example=[
        "<b>Bull trap.</b> NIFTY rejects 25,950 at 09:45 and 10:35. At 11:50 a green candle closes at 25,973 and "
        "Telegram channels shout 'breakout'. Volume on that candle is lower than on either rejection. Two candles "
        "later price closes at 25,937, back inside. The trapped longs' stops sit at 25,930-25,940 and below, and "
        "price falls to 25,880 by 13:15.",
        "<b>Bear trap.</b> Support 25,700 holds twice. At 11:50 it breaks to 25,681 and retail buys puts. At 12:00 "
        "a strong green candle closes at 25,713 on 3x volume. Shorts cover and NIFTY reaches 25,790.",
    ],
    trade=[("Entry (bull trap)", "Short 25,937 on the first 5-min close back below 25,950"),
           ("Stop-loss", "25,985, above the trap high 25,981 + buffer"),
           ("Target", "T1 25,880 range low (≈1:1.2); trail the rest"),
           ("Entry (bear trap)", "Long 25,726 after the reclaim; SL 25,668; target 25,785 (≈1:1)"),
           ("Filter", "Breakout volume < rejection volume; close back inside within 3 candles")],
    rule="Never buy the first 5-min close above a well-known level. Wait for a retest that holds, or for the "
         "failure that gives you the opposite trade.",
    mistakes=[
        "Buying a breakout on a candle with below-average volume.",
        "Holding a failed breakout and 'hoping' instead of exiting on the close back inside.",
        "Shorting the trap too early, before price has actually closed back inside the range.",
    ],
    retail="Selling 25,900 PE at the breakout 'because support is now below'. When the trap fails, that PE "
           "premium doubles in 20 minutes.",
    summary=["A breakout without volume is an invitation, not a signal.",
             "The trade is the failure: close back inside the range plus trapped traders' stops.",
             "SL beyond the trap extreme; first target is the other side of the range."],
))

CH.append(dict(
    num=6, part=2, title="The Stop-Loss Hunt",
    tagline="Your stop is someone else's entry.",
    concept=[
        "A <b>stop hunt</b> is a fast move just beyond a level where stops cluster, designed to trigger them, "
        "followed by a reversal. Below support it fills big buyers; above resistance it fills big sellers. It "
        "differs from a bear/bull trap mainly in speed: a hunt is usually a single long-wicked candle.",
    ],
    guruji="SL hunting is not a conspiracy, it's arithmetic. A desk that wants 3,000 lots at 25,570 knows where "
           "3,000 lots of sell orders are waiting: in your stop-losses at 25,580-25,590.",
    why=[
        "Support touched three times is the most obvious place on the chart, so stops pile up just below it. When "
        "price spikes into them, the stops become market sell orders. A large buyer with limit orders absorbs the "
        "whole lot at good prices. When selling dries up, there are no sellers left and price snaps back. "
        "The tell is a long wick plus the session's biggest volume, closing back above the level.",
    ],
    charts=[("c06a", "Stop hunt below 25,600: the 13:30 wick to 25,563 on the session's highest volume fills stops "
                     "at 25,580-25,590, then NIFTY closes back above support and rallies to 25,700."),
            ("c06b", "Mirror image above 26,050: a wick to 26,086 sweeps buy-stops and breakout orders; the red "
                     "confirmation candle leads to 25,960.")],
    example=[
        "From 11:00 to 13:25 NIFTY tests 25,600 three times. At 13:30 one candle drops to 25,563 and closes at "
        "25,611 with 4x normal volume. Every retail stop at 25,580-25,590 has been filled. The next candle closes "
        "at 25,629, and long entries trigger at 25,628 with SL 25,558. NIFTY reaches 25,700 by 14:50.",
        "<b>For option sellers:</b> this is when to sell the 25,500 PE, after the sweep, at its highest premium "
        "and with the trap already sprung. Never before.",
    ],
    trade=[("Entry", "Long 25,628 above the reclaim candle (or sell 25,500 PE / bull put spread)"),
           ("Stop-loss", "25,558, 5 points below the hunt wick"),
           ("Target", "T1 25,700 (≈1:1), book half; trail the rest under 5-min higher lows"),
           ("Filter", "Wick ≥ 2x body, volume ≥ 2x average, close back above the level"),
           ("Above resistance", "Short 26,021, SL 26,090, T1 25,960")],
    rule="Your stop goes beyond where the hunt is likely to reach: below the level by at least the average 5-min "
         "range (15-25 NIFTY points), or use a smaller size so a wider stop still risks only 1%.",
    mistakes=[
        "Stops 5 points below a triple-touched level, in the hunting zone.",
        "Re-entering short after being stopped out, right at the bottom of the hunt.",
        "Reading a slow grind through the level as a 'hunt'. Without a fast reclaim it is a breakdown.",
    ],
    retail="Getting stopped out at 25,585, reversing to short 'because support broke', and being stopped again "
           "at 25,640. Two losses on one move.",
    summary=["Stops cluster just beyond obvious levels; that is where hunts go.",
             "A hunt = long wick + volume spike + close back inside the level.",
             "Trade the reclaim with SL beyond the wick; sellers sell premium after the hunt."],
))

CH.append(dict(
    num=7, part=2, title="Gap Traps at the Open",
    tagline="The gap is news. The first 15 minutes are the truth.",
    concept=[
        "Gaps happen when overnight news (US markets, GIFT Nifty, results, global events) moves the opening price "
        "far from yesterday's close. A <b>gap-up trap</b> is a gap that is sold from the open and fills back to the "
        "previous close (PDC). A <b>gap-down trap</b> is a gap that is bought from the open and fills upward.",
    ],
    guruji="Gap-up pe khushi, gap-down pe dar: joy on gap-ups, fear on gap-downs. Operators trade the emotion, "
           "not the gap.",
    why=[
        "Institutions with long positions love a gap-up: it lets them sell at prices retail is happy to pay. "
        "Retail buys the first candle because the news is good and 'it'll run'. If the first 15-minute low breaks, "
        "every opening buyer is trapped, and their stops plus the sellers drive the gap-fill toward PDC. Since "
        "Dec 2025 NSE runs a 09:00-09:15 pre-open session for futures too, so opening prices are discovered by "
        "auction. That makes the first 15 minutes after the open even more about absorbing that auction's orders.",
    ],
    charts=[("c07a", "Gap-up trap: PDC 25,700, open 25,838 (+138), first 15-min high 25,871. The 09:40 break of "
                     "the opening low triggers a fill back to 25,705."),
            ("c07b", "Gap-down trap: PDC 25,760, open 25,628 (−132). Panic sellers at 25,596 are trapped when the "
                     "15-min high 25,632 breaks; the gap fills to 25,755.")],
    example=[
        "<b>Gap-up.</b> NIFTY opens at 25,838, 138 points above PDC 25,700, on strong US data. The first 15 minutes "
        "make 25,834-25,871. By 09:40 a 5-min candle has closed at 25,830, below the opening low. Short entry 25,830, "
        "SL 25,875 above the opening high. By 12:30 the gap has filled to 25,705.",
        "<b>Gap-down.</b> NIFTY opens 132 points down at 25,628 and prints 25,596 in the first 10 minutes. The "
        "opening range is 25,596-25,632. At 09:30 price closes above 25,632: shorts are trapped. Long 25,638, SL "
        "25,594, target PDC 25,755.",
    ],
    trade=[("Entry", "Break of the first 15-min range against the gap (short 25,830 / long 25,638)"),
           ("Stop-loss", "Other side of the opening 15-min range + buffer (25,875 / 25,594)"),
           ("Target", "PDC: gap fill (25,705 / 25,755); R:R ≈ 1:2.7"),
           ("Filter", "Gap 0.4-1% (100-250 pts); no big follow-through after 09:30; not on a trend-day news shock"),
           ("Skip", "Gaps > 1.2% on major news (war, election, policy surprise) can run all day")],
    rule="Don't trade the first 15 minutes after a gap. Mark the opening range, then trade the break, preferably "
         "the break against the gap.",
    mistakes=[
        "Buying CE at 09:16 because 'GIFT Nifty is up 150'.",
        "Selling far OTM puts on a gap-up open: the premium is high for a reason, and IV collapses only after the "
        "trap resolves.",
        "Fading every gap. Gaps that hold the first 15-min range often become trend days.",
    ],
    retail="Buying at 25,866 in the first five minutes with no stop, then averaging down at 25,820 and 25,780 as "
           "the gap fills.",
    summary=["The gap is the setup; the first 15-minute range is the information.",
             "A break of the opening range against the gap targets PDC.",
             "Big-news gaps can trend; size down or wait."],
))

CH.append(dict(
    num=8, part=2, title="The Opening-Range (09:15-09:30) Trap",
    tagline="The first breakout of the day grabs liquidity. The second one has intent.",
    concept=[
        "The <b>opening range (OR)</b> is the high and low of the first 15 minutes. The classic 'opening-range "
        "breakout' (ORB) buys above the OR high and sells below the OR low. Because thousands of traders run this "
        "exact strategy, the first break is often a <b>liquidity grab</b> that reverses through the opposite side.",
    ],
    guruji="If a strategy is taught free on YouTube with 2 million views, the market will find a way to make it "
           "fail 6 times out of 10.",
    why=[
        "ORB buy-stop orders sit just above the OR high, and their stops sit just below the OR low. A desk that "
        "wants to sell pushes price above the OR high to fill its shorts against those breakout buyers. When price "
        "falls back into the range, ORB longs panic, and when the OR low breaks their stops add to the fall. The "
        "genuine breakout looks different: strong volume and a successful retest of the broken level.",
    ],
    charts=[("c08a", "OR 25,830-25,880. The 09:35 break to 25,897 fails within two candles; the OR low breaks at "
                     "10:05 and NIFTY falls to 25,745."),
            ("c08b", "Contrast: the genuine breakout has 2x volume and the 10:00 retest holds above 25,880; NIFTY "
                     "trends to 25,985.")],
    example=[
        "<b>Trap.</b> The OR is 25,830-25,880. At 09:35 NIFTY prints 25,893 and ORB longs buy. By 09:50 it is back "
        "at 25,858, inside the range. At 10:05 a candle closes at 25,826, below the OR low. Short 25,826, SL 25,898 "
        "above the trap high, target 25,740. Done by 13:00.",
        "<b>Genuine.</b> Same OR. At 09:40 the breakout candle has twice normal volume. The pullback at 10:00 holds "
        "25,877, just above 25,880, and the next candle closes up. Long 25,888 on the retest, SL 25,866, target "
        "25,954 (3R).",
    ],
    trade=[("Entry (trap)", "Short on a close below the OR low after a failed OR-high break: 25,826"),
           ("Stop-loss", "25,898, above the failed breakout high"),
           ("Target", "25,740 (≈1:1.2); trail toward PDL"),
           ("Entry (genuine)", "Long on retest of OR high that holds: 25,888, SL 25,866, T 25,954 (1:3)"),
           ("Filter", "Breakout volume vs OR volume; time back inside the range ≤ 3 candles = trap")],
    rule="Never enter on the first break of the opening range. Enter either on a retest that holds, or on the "
         "failure through the opposite side.",
    mistakes=[
        "Buy-stop orders placed before the open just above the OR high.",
        "Using the OR low as your stop for an ORB long: everyone's stop is there.",
        "Trading the OR on expiry days, when the opening range is often just writers repositioning.",
    ],
    retail="Selling 25,800 PE at 09:35 'because ORB is up', then watching it double by 10:30.",
    summary=["The first OR break is often a liquidity grab.",
             "Real breakouts have volume and a retest that holds.",
             "Trade the retest or the failure, never the first spike."],
))

CH.append(dict(
    num=9, part=2, title="Round-Number and Max-Pain Traps Near Expiry",
    tagline="On expiry day, price gravitates to where the writers make the most money.",
    concept=[
        "<b>Max pain</b> is the strike at which option buyers, in total, lose the most money at expiry, which means "
        "writers keep the most premium. Strikes with the biggest open interest (OI walls) at round numbers act as "
        "magnets on expiry day: breakouts away from them often fail, and price is 'pinned' near the strike into the "
        "close.",
        "Since Sep 2025, NIFTY's weekly expiry is on <b>Tuesday</b>. One lot is <b>65</b> units (from the Jan 2026 "
        "series).",
    ],
    guruji="Max pain is not a law. It's a tendency in quiet markets. On a news day, max pain is just a number on a "
           "website.",
    why=[
        "Writers with large short positions at 26,000 CE and 26,000 PE delta-hedge with futures. If NIFTY rises "
        "above 26,000, their short calls lose and they sell futures to hedge, which pushes price down. Below 26,000 "
        "the short puts lose and they buy futures, which pushes price up. This hedging flow acts like a spring "
        "pulling price back to the strike. Buyers of 26,050 CE or 26,000 PE in the afternoon are paying for a move "
        "the hedging flow is actively fighting.",
    ],
    charts=[("c09a", "Expiry Tuesday: 26,000 is max pain with the highest CE and PE OI. The 13:05 breakout and "
                     "14:15 breakdown both fail; close 26,004."),
            ("c09b", "Option-chain view: call wall at 26,000-26,200, put wall at 25,850-26,000, max pain at 26,000.")],
    example=[
        "Expiry morning, the option chain shows 168 lakh call OI and 175 lakh put OI at 26,000, the biggest on "
        "the board. NIFTY spends the day within 26,000 ± 35. At 13:05 it pokes 26,036, and buyers of 26,050 CE at "
        "₹12 lose it all. At 14:15 it drops to 25,966, and buyers of 26,000 PE at ₹28 lose most of it. Close: "
        "26,004.",
    ],
    trade=[("Entry", "Fade a 30-40 pt excursion from the pin strike only after a 5-min close back toward it "
                     "(e.g. short 26,010 after the 13:10 rejection)"),
           ("Stop-loss", "15-min close beyond the excursion extreme (26,040)"),
           ("Target", "The pin strike ± 10 (25,995-26,005)"),
           ("Seller version", "Iron fly / short straddle at the pin only with hedges, small size, exit by 14:45"),
           ("Skip", "When VIX is rising, OI is shifting fast, or there is news in the afternoon")],
    rule="On expiry afternoons, never buy OTM options for a 'breakout' away from a heavy-OI strike. If you sell, "
         "always hedge, and still be flat by 14:45.",
    mistakes=[
        "Treating max pain as a guaranteed closing price.",
        "Selling naked straddles at the pin strike and holding into the last hour (see Chapter 10).",
        "Ignoring OI changes during the day: when the wall shifts, the magnet moves.",
    ],
    retail="Buying ₹5 'lottery' calls at 14:30 on expiry because 'it only needs 50 points'.",
    summary=["Heavy-OI round strikes act as expiry magnets via writers' hedging.",
             "Fade small excursions from the pin; don't buy breakouts away from it.",
             "Max pain fails on news days; always respect your stop and the 14:45 cutoff."],
))

CH.append(dict(
    num=10, part=2, title="Expiry-Day Gamma Spikes",
    tagline="Why a ₹30 premium can become ₹80 in the last hour.",
    concept=[
        "<b>Gamma</b> measures how fast an option's delta changes when spot moves. Far from expiry, gamma is small "
        "and premiums move smoothly. In the last hours of expiry day, gamma for near-the-money strikes becomes "
        "huge: delta can jump from 0.1 to 0.9 within ~60 NIFTY points. A short option that looked 'safe' at ₹30 can "
        "become ₹80 on a 100-point move.",
    ],
    guruji="Option selling se paisa banta hai, lekin expiry ke last ghante mein option selling se account bhi "
           "jaata hai. You earn in theta, you lose in gamma. Know which one owns the clock.",
    why=[
        "On expiry day, time value is nearly gone, so the option price is almost just its intrinsic value. Near "
        "the strike, a few points of spot decide whether the option is worth zero or worth everything above the "
        "strike. That is the 'kink' in the payoff curve. Short-covering into the close (writers buying back, desks "
        "squaring hedges) creates exactly the late moves that exploit this kink. SEBI also adds a 2% extreme loss "
        "margin on short index options on expiry day, so naked sellers face margin pressure at the worst moment.",
    ],
    charts=[("c10a", "The trade from your journal: sell 25,850 CE at 51 at 10:40; it decays to 30 by 13:05; a "
                     "100-point short-covering rally from 14:00 takes it to 79 by 15:15. The 14:45 cutoff exit was "
                     "~54."),
            ("c10b", "The gamma curve: the same option's price vs spot at 6h, 3h, 1h and 15 min to expiry. The "
                     "curve bends into a kink at the strike.")],
    example=[
        "At 10:40, with spot at 25,815, you sell the 25,850 CE at ₹51 (5 lots, 325 qty). By 13:05 theta has taken "
        "it to ₹30: 41% of the premium captured, +₹6,825 open profit. From 14:00 NIFTY rallies 100 points to "
        "25,925. Because the option is now in the money with almost no time left, it moves ₹7-9 for every 10 points "
        "of spot. At 15:15 it is ₹79: a loss of 28 points × 325 = <b>−₹9,100</b>.",
        "Same trade with rules: trail the SL to ~40 at 13:05 (lock half the open profit). The trail is hit around "
        "14:20, for a <b>profit</b> of about ₹3,900 on 5 lots (11.9 pts × 325). Even without a trail, the 14:45 hard exit at ~54 "
        "would have limited the loss to about ₹1,000.",
    ],
    trade=[("Entry", "Sell OTM premium only before 13:30 on expiry day, beyond the swept liquidity (Ch 22)"),
           ("Stop-loss", "Initial SL at premium +30%; once 40% decayed, trail to lock half the open profit"),
           ("Target", "60-70% of premium captured, or the 14:45 cutoff, whichever first"),
           ("Hard rule", "All shorts flat by 14:45 on expiry day. No new shorts after 14:00"),
           ("Size", "Expiry-day size ≤ half your normal size because of gamma + extra 2% ELM")],
    rule="Expiry-day exit cutoff 14:45. It is not a guideline. Put a phone alarm at 14:40.",
    mistakes=[
        "'It's only ₹30, it will expire worthless': near the strike, ₹30 is a loaded gun.",
        "Holding through the last hour to save the final ₹5-10 of premium (risking ₹30-50 to make ₹5).",
        "Averaging up shorts as premium rises in the last hour.",
    ],
    retail="Short at 51, saw 30, did nothing, exited at 70+ in panic. That is the exact pattern the chart shows, "
           "and it is 100% a rules problem, not an analysis problem.",
    summary=["Gamma explodes near the strike in the last hours of expiry.",
             "Small spot moves become huge premium moves: ₹30 → ₹80 is normal, not rare.",
             "Trail after 40% decay and be flat by 14:45: every expiry, no exceptions."],
))

CH.append(dict(
    num=11, part=2, title="The Buyer's Trap (Theta) and the Seller's Trap (Gamma)",
    tagline="Buyers bleed slowly. Sellers die suddenly.",
    concept=[
        "Options are a trade-off between time and movement. <b>Option buyers</b> pay time value and need a big "
        "move <i>soon</i>. Every flat hour costs them theta. <b>Option sellers</b> collect that time value but carry "
        "<b>gamma risk</b>: in a big move their losses accelerate. Each side has a trap built in.",
    ],
    guruji="Buyer sochta hai jackpot, seller sochta hai salary. The market gives the buyer a slow leak and the "
           "seller a sudden heart attack. Choose your disease, then manage it.",
    why=[
        "<b>Buyer's trap:</b> an ATM option's value is mostly time value. If spot ranges for three days, that "
        "value melts, even though 'NIFTY didn't go against me'. A buyer needs direction, magnitude <i>and</i> "
        "timing.",
        "<b>Seller's trap:</b> a short strangle wins on quiet days. On a trend day, the threatened side's premium "
        "rises faster and faster (gamma), while the other side can only fall to zero. One trend day can erase "
        "weeks of collected premium.",
    ],
    charts=[("c11a", "Buyer's trap: 25,750 CE bought at 128 on Friday; spot stays in 25,725-25,790; by Tuesday "
                     "14:45 the call is 23 (−82%)."),
            ("c11b", "Seller's trap: short 25,900 CE + 25,500 PE for 72 credit on Monday; a 333-point trend takes "
                     "the strangle to 145.")],
    example=[
        "<b>Buyer.</b> Friday 09:30, a trader buys the 25,750 CE at ₹128 (₹8,347 per lot) expecting a rally. NIFTY "
        "chops between 25,725 and 25,790 through Monday. Tuesday morning the call is ₹73; by 14:45 it is ₹23. "
        "Direction was not wrong; time ran out.",
        "<b>Seller.</b> Monday 09:30, a trader sells the 25,900 CE and 25,500 PE, 2 lots each, for ₹72 total. "
        "NIFTY trends 333 points up into Tuesday. The CE goes from about 38 to 145; the PE falls from 34 to near zero. "
        "The strangle is worth ₹145, a loss of about ₹9,500 on 2 lots. The PE side could never offset the CE.",
    ],
    trade=[("Buyer rule", "Buy only on a trigger with momentum (e.g. setup 2 or 3), DTE ≥ 2, exit in 30-60 min"),
           ("Buyer SL", "Premium −30% or the spot level that invalidates the setup, whichever first"),
           ("Seller rule", "Sell only defined-risk spreads; keep the threatened short strike beyond swept liquidity"),
           ("Seller SL", "Exit the threatened leg at 2x its premium, or on a 15-min close beyond structure"),
           ("Seller target", "50-70% of credit; never hold for the last 10%")],
    rule="Buyers manage time; sellers manage size and gamma. If you sell, every position has a hedge and a "
         "pre-defined maximum loss.",
    mistakes=[
        "Buyers: 'cheap' far-OTM options with low delta, held for days.",
        "Sellers: naked strangles 'because they win 80% of the time'. The other 20% is where accounts die.",
        "Sellers: rolling the losing side closer instead of exiting.",
    ],
    retail="Switching from buying to selling after losses, then selling naked with 3x the size, which turns a slow "
           "leak into a blow-up.",
    summary=["Buyers pay theta; they need speed. Sellers earn theta; they risk gamma.",
             "Trend days destroy short strangles; range days destroy option buyers.",
             "Sell only with hedges and a fixed max loss; buy only with momentum and a time stop."],
))

CH.append(dict(
    num=12, part=2, title="News and Event Traps",
    tagline="The first move after the headline is usually the wrong one.",
    concept=[
        "Scheduled events (RBI policy, Union Budget, US CPI/Fed, big-bank and IT results, election results) "
        "produce whipsaws. Before the event, IV is high and volume dries up. At the headline, price spikes one way "
        "(often both ways within minutes), taking out both buyers' and sellers' stops. The real direction usually "
        "appears 15-30 minutes later.",
    ],
    guruji="On event day, the first candle is for the algos, the second is for the fools, the third is for us.",
    why=[
        "Before an event both sides place stops close to the range, so liquidity piles up above and below. "
        "Algos read the headline in microseconds and push price into one pool, then the other. Option IV, which "
        "was inflated, collapses after the event ('IV crush'), so buyers can be right on direction and still lose. "
        "Sellers who sold before the event get the IV crush but carry gap risk.",
    ],
    charts=[("c12a", "RBI policy at 10:00: +70 spike to 25,888, full reversal to 25,735 by 10:30, then a short on "
                     "the retest of the event range."),
            ("c12b", "Budget day: the 11:00 speech brings −190, a second leg to ~25,365, then a +180 recovery. "
                     "Both sides are stopped twice.")],
    example=[
        "RBI day. From 09:15 to 09:55 NIFTY sits in 25,796-25,815. At 10:00 the policy headline hits and one "
        "candle spikes to 25,888. Retail buys calls. By 10:30 NIFTY is at 25,735: buyers' stops at 25,800 and "
        "sellers' stops at 25,830 have both been hit. At 11:20 price retests the old range from below at 25,770 "
        "and fails. That's the trade: short 25,770, SL 25,796, target 25,718 (2R).",
    ],
    trade=[("No-trade window", "15 min before to 30 min after the event"),
           ("Entry", "Retest of the pre-event range after the whipsaw (short 25,770)"),
           ("Stop-loss", "Back inside the pre-event range (25,796)"),
           ("Target", "Post-event extreme / next liquidity (25,718); R:R 1:2"),
           ("Size", "50% of normal; sellers use only hedged spreads, no naked shorts through events")],
    rule="Keep an event calendar on your desk: RBI, Fed, CPI, Budget, major results. On those days, cut size by "
         "half or don't trade the first hour after the event.",
    mistakes=[
        "Buying options before the event: you pay peak IV and get IV crush.",
        "Selling naked straddles the night before a Fed decision.",
        "Trading the first candle after the headline.",
    ],
    retail="'RBI will cut rates, I'll buy CE at 09:55.' The rate cut happens, NIFTY spikes, and the CE still "
           "loses 30% from IV crush and the reversal.",
    summary=["Events create liquidity on both sides; the first move hunts it.",
             "Wait 15-30 minutes, then trade the retest of the pre-event range.",
             "Half size, hedged positions, and respect IV crush."],
))

CH.append(dict(
    num=13, part=2, title="Trendline and Pattern Traps",
    tagline="When the pattern is perfect, ask who drew it for you.",
    concept=[
        "Classic patterns (triangles, flags, head-and-shoulders, double tops/bottoms) and trendlines are watched by "
        "millions. Their textbook entry points and stops are therefore huge liquidity pools. The <b>first</b> "
        "breakout of a well-known pattern is often a fake that collects those orders before the real move, "
        "sometimes in the opposite direction.",
    ],
    guruji="I've seen more money lost on 'perfect' double tops than on ugly charts. Ugly charts make people "
           "careful. Perfect ones make them greedy.",
    why=[
        "In a symmetrical triangle, buyers' stops sit under the lower line and sellers' stops above the upper line. "
        "A fake break up fills sellers against breakout buyers; then a break down runs the longs' stops. In a "
        "double top, everyone shorts the neckline break with stops above the neckline. If price reclaims the "
        "neckline, those shorts must buy back, and the squeeze often runs through the tops.",
    ],
    charts=[("c13a", "Triangle trap: the 13:10 breakout above the upper line on low volume fails; the break of the "
                     "lower line on high volume is the real move to 25,660."),
            ("c13b", "Failed double top: tops at 25,982; neckline 25,902 breaks to 25,878; the reclaim traps shorts "
                     "and squeezes to 26,060.")],
    example=[
        "<b>Triangle.</b> From 10:00 to 13:05 NIFTY coils between a falling line from 25,805 and a rising line "
        "from 25,710. At 13:10 it breaks up to 25,791 on below-average volume. Two candles later it is back inside, "
        "and at 13:25 it breaks the lower line with 3x volume. Short 25,736, SL 25,794, target 25,660.",
        "<b>Double top.</b> Tops at 25,982 (11:30 and 12:35), neckline 25,902. At 13:10 a candle closes at 25,887 "
        "and pattern traders short. At 13:25 a strong candle closes at 25,919, back above the neckline. Long "
        "25,919, SL 25,876, target 25,982 then 26,040. NIFTY runs to 26,060.",
    ],
    trade=[("Entry (triangle)", "After the first break fails: short 25,736 on the opposite-side break with volume"),
           ("Stop-loss", "25,794, above the fake breakout high"),
           ("Target", "Pattern height projected: 25,660 (≈1:1.3)"),
           ("Entry (failed DT)", "Long 25,919 on reclaim of neckline; SL 25,876; T1 25,982 (1:1.5), T2 26,040"),
           ("Filter", "Volume: fake breaks are quiet, real breaks are loud")],
    rule="Don't trade the first break of a famous pattern. Trade the second break, or the failure of the first.",
    mistakes=[
        "Drawing trendlines through candle bodies to make the pattern 'fit'.",
        "Placing stops just beyond the trendline, the most crowded place on the chart.",
        "Trading pattern targets from textbooks without checking where the liquidity actually is.",
    ],
    retail="Shorting the neckline break of a double top with a ₹200 stop above the neckline. A failed "
           "pattern squeezes 150 points in 30 minutes.",
    summary=["Famous patterns are liquidity maps for operators.",
             "The first break is often fake, so watch the volume.",
             "Trade the failure or the confirmed second break, with SL beyond the fake extreme."],
))
