# Vision board: May 2029

`Vision_Board_May_2029.png` (2480×1754, for a screen or wallpaper) and `Vision_Board_May_2029.pdf` (the same layout, edge to edge on one page, A3 landscape proportions).

The message: protect the capital, follow the plan, take small daily wins, and walk out of the rat race by the first week of May 2029.

- **The art:** a line drawing. The rat race is a closed loop; one line breaks out of it and climbs ~640 small steps (a few small red ones) to a gold point marked May 2029. A black floor line is the capital, which the steps never go below. A grey dashed line is the gamble: it spikes, then crashes through the floor to −46%.
- **Card 1:** recovery math. A loss of 46% needs +85% just to get back.
- **Card 2:** the daily rules from the Guruji manual's risk card (1% risk = ₹2,700 on ₹2,70,000, daily stop, max 3 trades, flat by 14:45 on expiry Tuesday).
- **Card 3:** small daily wins, singles not sixes.
- **Card 4:** a 31-month discipline tracker (Oct 2026 to Apr 2029, then May 2029) to tick by hand.

Rebuild: `python3 build_board.py` (Node Playwright for the PNG, Chromium at /opt/pw-browsers for the PDF). Capital, risk and session count are constants at the top of the script.

## Desktop wallpaper

`Wallpaper_15_Points_a_Week.png` (2880×1800, 16:10, dark): the weekly rule. 15 points a week, then stop. It shows the loop-to-May-2029 line art, a "singles, not sixes" dot grid, a weekly meter where 15 points is the stop line and anything beyond is the greed zone, and four rules. The left ~500 px and bottom ~120 px are kept clear for desktop icons and the taskbar. Rebuild with `python3 build_wallpaper.py`; the target is `TARGET` at the top of the script.
