# NIFTY Weekly Option Selling: Journal & Risk Research

*Prepared 6 Oct 2026 for a ₹2.7 lakh intraday NIFTY option-selling account (down from ₹5 lakh). The workbook `NIFTY_Options_Trading_Journal.xlsx` puts all of this into practice.*

---

## 0. Verified facts (as of 6 Oct 2026)

| Item | Current value | Source |
|---|---|---|
| NIFTY lot size | **65** (cut from 75 starting with the Jan-2026 series. The first weekly at 65 was the 6 Jan 2026 expiry) | [NSE circular via HDFC Sky](https://hdfcsky.com/news/nse-revises-market-lot-sizes-for-major-index-derivatives-effective-january-2026), [Business Standard](https://www.business-standard.com/markets/capital-market-news/nse-announces-reduction-in-derivative-lot-size-for-four-key-indices-125100701081_1.html), [Sahi 2026 list](https://www.sahi.com/blogs/nifty-lot-size-2026-bank-nifty-sensex) |
| NIFTY weekly expiry | **Tuesday** (moved from Thursday in Sep 2025. Monthly expiry is the last Tuesday of the month) | [Business Standard](https://www.business-standard.com/amp/markets/news/nse-bids-adieu-to-thursday-expiry-as-dates-swap-come-into-effect-explained-125082800635_1.html), [TradingQnA (Zerodha)](https://tradingqna.com/t/sebi-confirms-derivatives-expiries-tuesday-for-nse-thursday-for-bse/183366) |
| Weekly index expiries | One per exchange. NSE keeps only NIFTY weekly. BANKNIFTY, FINNIFTY and MIDCPNIFTY are monthly only | [Zerodha Z-Connect](https://zerodha.com/z-connect/business-updates/sebis-new-rules-for-index-derivatives-heres-whats-changing) |
| STT on options | **0.15% of premium, sell side**, from 1 Apr 2026 (was 0.10%). STT on exercise is also 0.15% (was 0.125%) | [5paisa](https://www.5paisa.com/news/stt-hike-on-fo-to-take-effect-from-april-1-amid-rising-options-activity), [HDFC Bank](https://www.hdfc.bank.in/blogs/union-budget/budget-2026-27-income-tax-act-2026-tax-slabs-stt) |
| Other Zerodha F&O option charges | ₹20 per executed order · NSE txn 0.03503% of premium · SEBI ₹10/crore · stamp 0.003% buy side · GST 18% on (brokerage + exchange + SEBI) | [Zerodha charges](https://zerodha.com/charges), [Chittorgarh summary](https://www.chittorgarh.com/stockbroker/zerodha/18/?p=4) |

> The STT hike landed after many online brokerage calculators were written. If a calculator shows 0.1%, it is out of date. Every rate is an editable input on the `RULES` sheet.

---

## 1. How professional and prop-desk traders structure journals

Prop-firm coaching, mainly Brett Steenbarger's work with SMB Capital and other desks, treats the journal as a **performance-improvement tool, not a diary**. Steenbarger's five elements are:

1. Observations about yourself and the market
2. Notes on your **best** trades, to find what to repeat
3. A plan for the next day
4. Specific self-improvement steps
5. Performance metrics tracked over time

([Journalytix interview](https://journalytix.me/2019/04/23/dr-brett-steenbarger-taking-your-performance-to-the-next-level/))

Prop traders also file a **Daily Report Card**: they work on one goal and grade themselves against it every day ([SMB Training webinar](https://www.smbtraining.com/blog/webinar-the-learning-process-of-a-professional-trader-with-dr-steenbarger-and-smb)). Steenbarger's book *The Daily Trading Coach* (Wiley, 2009) expands this.

**Fields desks typically log, and why:**

| Group | Fields | Why |
|---|---|---|
| Identification | date, time, instrument, side, size | Lets you slice results by time, day and setup |
| Plan | setup name/grade, thesis, entry trigger, stop, target, planned risk | Separates *process* quality from *outcome* |
| Execution | actual entry and exit, slippage, exit reason | Exposes impulsive exits (panic or revenge) |
| Path | MAE and MFE | Shows whether stops are too wide and how much profit was left or given back. This is John Sweeney's *Maximum Adverse Excursion* method ([Wiley, 1997](https://gov.wiley.com/WileyCDA/WileyTitle/productCd-0471141526.html)). MAE/MFE history tells you where stops and targets belong ([LuxAlgo summary](https://www.luxalgo.com/library/concept/mae-mfe-informed-management.md)) |
| Result | gross, costs, net, R-multiple | Net of costs is the only P&L that counts. R makes trades comparable |
| Behaviour | rule followed?, rule broken, emotion, lesson | The two things a retail account fails on are size and discipline, not analysis |

## 2. Fields specific to option sellers

| Field | Why it matters to a seller |
|---|---|
| Premium received (entry price) and net credit for spreads | Your maximum possible gain |
| Strike, CE/PE, distance from spot (points and %) | How much room NIFTY has before you are tested. On expiry day 35–100 points is close to the money |
| IV at entry and India VIX | Sell when premium is rich. Low-IV sells pay little for the same gamma risk |
| DTE (trading days to expiry) | Theta and gamma both rise sharply as DTE goes to 0 |
| Greeks at entry: delta (and gamma if you can) | Delta ≈ rough chance of finishing ITM. 0.15–0.25 is typical for credit sellers. Gamma tells you how fast delta will turn on you |
| Max loss defined? (spread or naked) | A naked short has open-ended risk, which is the main source of a 24% day |
| Margin used | Large margin relative to capital is oversizing, even when the stop is "small" |
| Hard SL placed (Y/N), stop price, target | Lets you prove that the stop existed as an order |
| MAE / MFE in premium | Catches the 51 → 30 → 70 pattern of open profit turning into a loss |

## 3. Behavioural and psychological tracking

- **Mark Douglas, *Trading in the Zone* (2000):** each trade is one outcome from a probability distribution. The edge only shows over many trades, so results depend on **consistent rule execution**, not on being right. In your journal this becomes the *Followed rules Y/N* field and the comparison of P&L for rules followed vs rules broken.
- **Brett Steenbarger:** journal your **best** trades as well as your worst. Set one process goal at a time (the Report Card). Notice your state *before* trading, because poor sleep, stress and frustration lead to impulsive trades.
- **Van Tharp:** measure each result as an **R-multiple**. 1R is the planned loss at the stop, and expectancy is the average R across trades ([Van Tharp Institute](https://vantharp.com/Weekly_update/Weekly_273_May_31_2006.htm), [CrossTrade primer](https://crosstrade.io/learn/performance-metrics/r-multiple)). Tharp also stresses that position sizing, not entries, decides whether an account survives.

**Tilt and revenge indicators the workbook flags automatically:**

- A new trade on a day already at or below the daily loss limit (`Day P&L Before This Trade`)
- More than the allowed number of trades in a day (`Trade # of Day`)
- Exit reason of Panic, Revenge or Rule break
- Emotion before entry of Angry/Revenge, FOMO or Greedy
- Lots or risk above the rule, or no stop (`Size Check` = OVERSIZED or NO SL)
- A loss streak at or above the limit, which triggers the dashboard STOP flag
- PRE-MARKET answers of "Trading to recover = Y", state ≤ 2 or sleep < 6 hours, which give NO TRADE / HALF SIZE

## 4. Key performance metrics and formulas

| Metric | Formula |
|---|---|
| Win rate | Wins ÷ Total trades |
| Average win / average loss | Σ winning net ÷ #wins; Σ losing net ÷ #losses |
| Payoff ratio | Avg win ÷ \|Avg loss\| |
| Expectancy (₹) | Win% × Avg win − Loss% × \|Avg loss\| |
| R-multiple | Net P&L ÷ Planned risk (1R = \|SL − entry\| × qty). If you set no stop, the workbook uses your rule 1R |
| Expectancy (R) | Average of all R-multiples. Above 0 means you have an edge; +0.2R to +0.5R is good for discretionary trading |
| Profit factor | Σ winning net ÷ \|Σ losing net\|. Below 1 loses money; aim for above 1.5 |
| Max drawdown | max(Peak equity − Equity), in ₹ and as % of the peak |
| Recovery factor | Net P&L ÷ Max drawdown |
| Largest loss % of capital | min(Net) ÷ Capital. With 1% risk this should stay near −1% |
| Max consecutive losses | Longest run of trades with Net < 0 |
| % of P&L from top 5 | Σ five largest net ÷ total net. Above 100% means the rest of the trades lose money |
| Profit given back | max(0, MFE ₹ − Gross P&L) for each trade |

**Why sellers need these numbers:** short premium usually has a **high win rate and low payoff**. At a 70% win rate you need payoff above 0.43 just to break even (0.7 × W = 0.3 × L). A single uncapped loss, such as your ₹1.2 lakh day, wipes out months of small wins. That is why the workbook tracks largest loss as % of capital and profit factor alongside win rate.

## 5. Position sizing and risk rules for a ₹2–5 lakh account

- **Fixed-fractional risk of 1% (2% at most):** at ₹2.7 lakh, 1R = **₹2,700**. With 65 units per lot, 1 lot can carry at most a 41.5-point premium stop. Lots = floor(₹2,700 ÷ (SL points × 65)). The `RULES` sheet has a calculator that also caps lots at Max lots.
- **Daily loss limit of 2% (₹5,400):** once hit, stop trading for the day. This protects you most from tilt.
- **Weekly circuit breaker of 6% (₹16,200):** three max-loss days and you are out until Monday. Many prop desks also cut size by half after a losing week.
- **Naked shorts on a small account:** one naked NIFTY lot needs roughly ₹2 lakh of margin, which is about 75% of your capital in one position with open-ended risk. Defined-risk spreads and condors keep the maximum loss known before entry, which is what makes fixed-fractional sizing possible.
- **Survival math:** a 46% drawdown (₹5 lakh to ₹2.7 lakh) needs an **85% gain** to recover. At 1% risk per trade, even 10 straight losses cost only about 9.6%.

## 6. Expiry-day risks in Indian index options

- **Gamma:** near expiry an at- or near-the-money option's delta can swing from 0.3 to 0.8 on a 50–80 point index move. A short option priced at ₹30 at 13:00 can be ₹70+ by 15:00. This is the 51 → 30 → 70 trade, and most of that move tends to happen in the **last 60–90 minutes**.
- **Last-hour spikes:** liquidity thins and short covering bunches up. Spreads widen, so SL-M orders can fill well past the trigger. Hence the hard exit at **14:45** (an editable input) and no new shorts after 14:00.
- **SEBI rule changes, 2024–26:**
  - Oct 2024 circular, effective from 20 Nov 2024 ([Zerodha](https://zerodha.com/z-connect/business-updates/sebis-new-rules-for-index-derivatives-heres-whats-changing), [Angel One](https://www.angelone.in/news/market-updates/sebi-strengthens-index-derivative-rules)):
    - Minimum contract value raised to ₹15 lakh
    - One weekly expiry per exchange
    - **+2% extreme loss margin on short options on expiry day**
    - Upfront premium collection
    - From Feb 2025: no calendar-spread margin benefit on expiry day
    - From Apr 2025: intraday position-limit monitoring
  - May 2025: SEBI required all equity-derivative expiries to fall on Tuesday or Thursday, and NSE moved to Tuesday from Sep 2025. Position limits are now measured on a delta (future-equivalent) basis, effective 1 Oct 2025 ([KS&K](https://ksandk.com/newsletter/sebi-position-limits-index-derivatives-guide/), [Outlook Money](https://www.outlookmoney.com/invest/equity/sebi-outlines-new-framework-for-monitoring-of-intraday-position-limits-for-index-derivatives)).
  - Dec 2025 NSE circular: NIFTY lot size cut from 75 to 65 for the Jan-2026 series.
  - Budget 2026-27: options STT raised to 0.15% from 1 Apr 2026.
  - **Watch:** in Aug 2026 there were *reports* that regulators were considering removing weekly expiries altogether ([Lapaas Voice, unconfirmed](https://lapaasvoice.com/sebi-may-remove-weekly-fo-expiry-to-curb-retail-investor-losses-reports)). This had not been enacted as of this date. NSE also reviews lot sizes every June and December, so re-check `LotSize` then.
- **Context:** SEBI's FY25 study found **91% of individual F&O traders lost money**, with an average loss of about ₹1.1 lakh ([Business Standard](https://www.business-standard.com/amp/markets/news/net-losses-of-traders-in-fo-widens-in-fy25-sebi-study-125070701221_1.html)). The base rate is against you, which is why process control comes before strategy.

## 7. Common journaling mistakes, and a habit that takes under 5 minutes

| Mistake | Fix built into the workbook |
|---|---|
| Logging only P&L | MAE/MFE, rule and emotion fields are next to P&L |
| Journaling only bad days, or skipping days after a loss | The Daily Summary and STOP flag only work if every trade is logged. Make logging part of closing the position |
| Too many fields, so you quit within a week | You fill about 20 inputs, mostly dropdowns. The other 40+ columns are automatic |
| No review loop | The Weekly Review pulls rule-break cost by rule. You choose **one** change for next week |
| Rationalising: "followed rules = Y" when you did not | `Auto Rule Check` flags oversizing, no SL, expiry breach, over-trading and trading after the daily limit, whatever you typed |
| Gross instead of net | Charges are computed automatically from current rates |

**Routine:**

- Before 09:15: 2 minutes on PRE-MARKET
- Before entry: 30 seconds with the size calculator
- After exit: 2–3 minutes on the TRADE LOG row (copy MAE/MFE from the Kite chart), then glance at the DASHBOARD
- Weekend: 20 minutes on the WEEKLY REVIEW
