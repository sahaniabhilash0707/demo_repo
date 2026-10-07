from model import single, multi, yesno, match, order, case

TITLE = "Analytics, AI and Copilot"
SUBTITLE = "AI visuals, the Analytics pane, Copilot, advanced DAX patterns and distribution, at full blueprint weight."
LEVEL = "Level 3 · Advanced"
CASE_NAME = "Proseware Telecom"

ITEMS = [
# ---------------- P1 Get or connect to data (4)
single("P1",
 "One Excel workbook holds 12 monthly sheets with identical layouts, and a new sheet is added each month. You need all sheets, including future ones, in one table. What should you do?",
 ["Filter the navigation table to Kind = \"Sheet\", then expand Data", "Connect to each sheet separately and append the twelve queries together", "Use the Folder connector pointed at the workbook's file path", "Use Transpose on the first sheet"], "A",
 "The workbook's navigation table lists every sheet. Keeping the sheet rows and expanding their Data column combines all of them, and new sheets are picked up on refresh. Connecting to sheets one by one needs editing each month. The Folder connector expects a folder of files."),

single("P1",
 "The SharePoint folder connector asks for a URL. Your files are in https://contoso.sharepoint.com/sites/Finance/Shared Documents/Exports. What should you enter?",
 ["The site URL: https://contoso.sharepoint.com/sites/Finance", "The full folder URL: .../sites/Finance/Shared Documents/Exports", "The URL of one file", "A OneDrive personal URL"], "A",
 "The SharePoint folder connector expects the site root URL. It then lists all files in the site's libraries, and you filter on Folder Path to the Exports folder. Entering the folder or file URL fails or returns nothing."),

single("P1",
 "An Azure SQL Database is reachable only through a private endpoint in an Azure virtual network, and no on-premises servers exist. Scheduled refresh in the service must reach it. Which gateway option fits?",
 ["A virtual network (VNet) data gateway", "A personal-mode gateway on a laptop", "No gateway, because Azure SQL is always public", "Publish to web"], "A",
 "A VNet data gateway is a managed gateway injected into your virtual network, so the service can reach private Azure resources without installing anything. Personal mode is single-user and needs a machine that's always on. A private endpoint means the database isn't public."),

single("P1",
 "A 300 MB source is updated once a night. Reports need fast visuals and complex time-intelligence DAX. No real-time requirement exists. Which storage mode should you choose?",
 ["Import", "DirectQuery", "Dual for every table", "Live connection"], "A",
 "Import gives the best query performance and full DAX support, and nightly freshness matches the source. DirectQuery adds latency and restricts some DAX patterns for no benefit. Dual is for composite models, and live connection is for existing semantic models."),

# ---------------- P2 Profile and clean (2 + 1 in case)
single("P2",
 "A merge on Email misses many matches because one table has \"A.Kumar@contoso.com\" and the other has \"a.kumar@contoso.com\". What should you do before merging?",
 ["Convert the Email column to lowercase in both queries", "Use Trim on one query", "Change the join kind to Full outer", "Remove duplicates on Email"], "A",
 "Power Query comparisons are case-sensitive, so the values must be standardised before the merge. Lowercasing both sides is the simplest fix. Trim deals with spaces, not case. Changing the join kind or removing duplicates doesn't make the values match."),

single("P2",
 "An Excel export contains completely empty rows between blocks of data, and they appear as rows of nulls. What should you do?",
 ["Remove Rows → Remove blank rows", "Fill down", "Replace errors", "Use first row as headers"], "A",
 "Remove blank rows deletes rows where every column is null or empty, leaving the real data. Fill down would copy values into the empty rows. Replace errors and header promotion don't address them."),

# ---------------- P3 Transform and load (5)
single("P3",
 "Twenty CSV sources need the same 15 cleaning steps. You want to define the steps once and apply them to each source. What should you create?",
 ["A custom function, invoked on each source", "Twenty duplicated queries, one per CSV source", "A calculation group with one item per source", "A DAX calculated table"], "A",
 "A Power Query function wraps the steps with a parameter, such as a file path or table, and can be invoked for every source, so changes are made once. Duplicated queries repeat the logic twenty times. Calculation groups and DAX tables can't run Power Query steps."),

single("P3",
 "A Tickets table has a Status column (Open, Pending, Closed). You need one row per Team with a column per status holding the number of tickets. Which transformation should you use?",
 ["Pivot the Status column, counting TicketID", "Unpivot the Status column into attribute-value pairs", "Transpose the table", "Merge Tickets with itself"], "A",
 "Pivot turns each status into a column, and counting TicketID gives the number of tickets per team and status. Unpivot does the reverse. Transpose rotates the whole table. Merge joins tables."),

single("P3",
 "You need a MonthStart column (the first day of each order's month) for a monthly fact table, without writing M. Which option should you use?",
 ["Add Column → Date → Month → Start of Month", "Add Column → Index column", "Transform → Round", "Add Column → Statistics → Count"], "A",
 "The Date menu has Start of Month, which returns the first day of the month for each date. That's ideal as a monthly key. The other options don't produce dates."),

multi("P3",
 "A query against SQL Server must keep folding. Which two steps typically fold into the SQL sent to the server?",
 ["Filter rows on a column value", "Remove columns", "Add an index column", "A custom column that calls a custom M function", "Change type using a non-default locale"], "AB",
 "Row filters and column selection translate directly into WHERE and SELECT clauses. Index columns, custom M functions and locale-specific type conversions usually can't be expressed in SQL, so folding stops at that step."),

order("P3",
 "You need to combine 50 CSV files from a folder that share one layout. Put the actions in order.",
 ["Get data → Folder and select the folder",
  "Choose Combine & Transform Data",
  "Choose the sample file and confirm the delimiter and settings",
  "Apply cleaning steps in the Transform Sample File query so they run for every file"],
 "The Folder connector lists the files. Combine & Transform builds a sample-file query and a function. Cleaning steps go in the sample-file transform so they apply to each file before the files are appended.",
 extra=["Append each file manually", "Turn off Enable load on the combined query"]),

# ---------------- M1 Design and implement a model (4)
single("M1",
 "A fact table has eight low-cardinality Yes/No flag columns (IsOnline, IsPromo, IsGift…), and authors find them cluttered. Which modelling pattern groups them efficiently?",
 ["A junk dimension of the distinct flag combinations", "A separate dimension table for each of the eight flags", "Calculated columns in a Flags table", "Hiding all the flags"], "A",
 "A junk dimension collects unrelated low-cardinality attributes into one small table of their combinations, so the fact only needs one key. Eight separate dimensions add relationships. Hiding them removes useful slicing."),

single("M1",
 "Sales has an OrderNumber column used only to identify orders and to drill to order detail. Should you create an Order dimension for it?",
 ["No. Keep it in the fact table as a degenerate dimension.", "Yes. Every descriptive column must move to a dimension table.", "Yes, related to Sales with a many-to-many relationship", "No. Delete the column."], "A",
 "An identifier with no other attributes belongs in the fact as a degenerate dimension. A separate table would just duplicate the column and add a relationship. Deleting it removes drill capability."),

single("M1",
 "A Store table has Latitude and Longitude columns. Map visuals must place stores exactly at those coordinates. What should you set?",
 ["Data category Latitude and Longitude on the respective columns", "Data category City on both columns, placed in the map's Location well", "Summarize by Sum", "A hierarchy of the two columns"], "A",
 "Categorising the columns as Latitude and Longitude and placing them in those wells plots exact coordinates without geocoding. City categories would make Bing interpret numbers as place names. Coordinates should not be summed."),

single("M1",
 "A Revenue measure must display as 1.2K, 3.4M or 2.1B depending on its size, while keeping the value numeric for sorting and further calculations. What should you use?",
 ["A dynamic format string for the measure", "FORMAT ( [Revenue], \"#,0.0,,M\" ) as the measure itself", "A text column with the formatted value", "Three separate measures"], "A",
 "Dynamic format strings change how a measure is displayed based on a DAX expression while the value stays numeric. FORMAT returns text, which breaks sorting, totals and charts. Text columns and separate measures add complexity."),

# ---------------- M2 DAX (5 + 1 in case)
single("M2",
 "A calculation group's YTD item must not apply to the Margin % measure, which should be returned unchanged. Which item expression should you use?",
 ["IF ( SELECTEDMEASURENAME () = \"Margin %\", SELECTEDMEASURE (), CALCULATE ( SELECTEDMEASURE (), DATESYTD ( 'Date'[Date] ) ) )", "CALCULATE ( [Margin %], DATESYTD ( 'Date'[Date] ) )", "IF ( SELECTEDMEASURENAME () = \"Margin %\", CALCULATE ( SELECTEDMEASURE (), DATESYTD ( 'Date'[Date] ) ), SELECTEDMEASURE () )", "IF ( ISBLANK ( SELECTEDMEASURE () ), BLANK () )"], "A",
 "SELECTEDMEASURENAME returns the name of the measure being evaluated, so the item can skip Margin % and apply YTD to everything else. Hard-coding a measure breaks the item for every other measure. Swapping the IF branches applies YTD only to Margin %, and the ISBLANK test doesn't implement YTD."),

single("M2",
 "You need a calculated column on Customer that ranks each customer by lifetime sales across all customers (1 = highest). Which expression is correct?",
 ["RANKX ( ALL ( Customer ), [Total Sales] )", "RANKX ( Customer, SUM ( Sales[Amount] ) )", "RANK.EQ ( [Total Sales], Customer[CustomerKey] )", "TOPN ( 1, Customer, [Total Sales] )"], "A",
 "RANKX over all customers evaluates [Total Sales] for each one, with context transition from the measure reference, and ranks the current row against them. SUM without context transition returns the grand total for every row, so every customer would tie. RANK.EQ isn't used this way, and TOPN returns a table."),

single("M2",
 "Sales relates to Date on an integer DateKey (20260131). Sales YTD returns the same value as Sales on every row. Date[Date] is of Date type and holds unique, contiguous dates. What should you do?",
 ["Mark the Date table as a date table, using Date[Date]", "Change DateKey to Text", "Use TOTALYTD with DateKey", "Turn on Auto date/time"], "A",
 "When the relationship uses a non-date key, time-intelligence functions need the table marked as a date table, so the engine can remove filters from the whole Date table during the calculation. DateKey isn't a date, so TOTALYTD can't use it. Auto date/time doesn't apply to custom date tables."),

single("M2",
 "Which measure returns the quantity-weighted average selling price?",
 ["DIVIDE ( SUMX ( Sales, Sales[Quantity] * Sales[UnitPrice] ), SUM ( Sales[Quantity] ) )", "AVERAGE ( Sales[UnitPrice] )", "AVERAGEX ( Sales, Sales[UnitPrice] )", "DIVIDE ( SUMX ( Sales, Sales[Quantity] * Sales[UnitPrice] ), COUNTROWS ( Sales ) )"], "A",
 "A weighted average divides total revenue by total quantity, so lines with more units count more. AVERAGE and AVERAGEX give each order line's price equal weight, whatever its quantity, and dividing revenue by the row count gives revenue per line, not price per unit."),

single("M2",
 "A disconnected Band table has Band, Min and Max columns (Low 0–1,000, Mid 1,000–10,000, High 10,000+). A measure must count customers whose sales fall in the band on each row of a visual. Which expression is correct?",
 ["COUNTROWS ( FILTER ( VALUES ( Customer[CustomerKey] ), [Total Sales] >= MIN ( Band[Min] ) && [Total Sales] < MAX ( Band[Max] ) ) )", "COUNTROWS ( Band )", "COUNTROWS ( FILTER ( Customer, SUM ( Sales[Amount] ) >= MIN ( Band[Min] ) && SUM ( Sales[Amount] ) < MAX ( Band[Max] ) ) )", "DISTINCTCOUNT ( Band[Band] )"], "A",
 "Dynamic segmentation iterates customers, evaluates each one's sales, and keeps those within the current band's bounds, which come from the band row in the visual. SUM inside FILTER has no context transition, so it tests the same total for every customer rather than each customer's own sales. Counting the Band table or its bands doesn't evaluate customers."),

# ---------------- M3 Optimize (2)
single("M3",
 "A model loads ten years of transactions, but every report shows only the last two years, and the business confirms older data isn't needed. What is the most effective way to reduce model size?",
 ["Filter the query in Power Query to the last two years", "Add a report-level filter that keeps only the last two years", "Hide old rows in each visual", "Create measures that ignore dates older than two years"], "A",
 "Removing unnecessary rows at load cuts memory and refresh time. Report filters and measures still leave all ten years in the model. Pair this with a rolling date filter or incremental refresh so the window moves forward."),

single("M3",
 "A table visual lists every transaction (over a million rows) with eight columns, and the page is slow to render. Users only ever look at recent, filtered subsets. What is the best fix?",
 ["Add filters so the visual returns far fewer rows", "Add more columns", "Change the theme", "Turn off totals and keep the visual otherwise unchanged"], "A",
 "Huge row counts in table visuals are expensive to query and render. Limiting the rows returned, by filtering or requiring a selection first, solves both. Turning off totals helps a little at best."),

# ---------------- V1 Create reports (5)
single("V1",
 "A matrix shows months under years. You need a running total that restarts at the beginning of each year, as a visual calculation. Complete the expression.",
 ["RUNNINGSUM ( [Sales], HIGHESTPARENT )", "RUNNINGSUM ( [Sales] )", "MOVINGAVERAGE ( [Sales], 12 )", "COLLAPSE ( [Sales], ROWS )"], "A",
 "The reset parameter HIGHESTPARENT restarts the running sum when the top level of the row hierarchy, the year, changes. Without a reset it runs across all years. MOVINGAVERAGE averages, and COLLAPSE returns the parent's value.",
 code="YTD running = ____"),

single("V1",
 "A narrative visual with Copilot summarises the whole page, but executives want it to describe only the three KPI visuals at the top. What should you do?",
 ["Scope the visual to summarise selected visuals", "Delete the other visuals from the page", "Replace it with a text box that describes the KPIs", "Move the KPIs to a dashboard"], "A",
 "The Copilot narrative visual can summarise the entire report, the current page or selected visuals, so you can scope it to the three KPIs. Removing visuals or switching to static text loses functionality."),

single("V1",
 "A chart must show monthly revenue as columns and margin % as a line, each on its own axis scale. Which visual should you use?",
 ["Line and clustered column chart with a secondary axis", "Stacked area chart", "Two separate pie charts", "Clustered column chart with both measures on one axis"], "A",
 "Combo charts plot columns and a line together, and a secondary Y-axis lets a percentage share the chart with currency values. The other visuals can't show both measures on different scales together."),

single("V1",
 "A slicer must let users pick a year and then expand it to pick individual months within that year, in one control. What should you do?",
 ["Make a hierarchy slicer with Year and Month", "Use two slicers, one for Year and one for Month", "Use a relative date slicer", "Use a between date slicer on the Date column"], "A",
 "Adding several levels to a slicer creates a hierarchy slicer with expandable levels. Two separate slicers work but aren't one control. Relative and between date slicers select ranges, not a hierarchy."),

match("V1",
 "Match each layout requirement to the visual that fits it best.",
 [("Category in rows, year in columns, with subtotals on both", "Matrix"),
  ("A flat list of invoices with one column per field and a total row", "Table"),
  ("One headline number, such as total revenue this year", "Card"),
  ("Monthly revenue over three years, to show the trend", "Line chart")],
 ["Matrix", "Table", "Card", "Line chart", "Treemap"],
 "A matrix gives a cross-tab with row and column groups and subtotals. A table is a flat list. A card shows a single value. A line chart shows a trend over time. A treemap shows part-to-whole with nested rectangles, which none of these need.",
 left="Requirement", right="Visual"),

# ---------------- V2 Usability and storytelling (5)
single("V2",
 "Users get lost after choosing many slicer values and want one click to reset every slicer on the page. What is the simplest built-in solution?",
 ["Insert a button with the Clear all slicers action", "Ask users to refresh the browser", "Create a bookmark for every slicer", "Lock all slicers"], "A",
 "The Clear all slicers button action resets every slicer on the page in one click. Refreshing doesn't necessarily clear saved filters. A bookmark per slicer is overkill. Locking prevents use."),

single("V2",
 "A report-page tooltip about product categories must appear automatically on every visual that uses Product[Category], without configuring each visual. What should you do on the tooltip page?",
 ["Add Product[Category] to its Tooltip fields well", "Set the Tooltip option to Default on each visual that uses Category", "Hide the tooltip page", "Create a bookmark"], "A",
 "Fields in the tooltip page's Tooltip fields well make the page appear automatically on any visual that uses those fields. Visuals left on Auto pick it up. Setting Default turns the custom page off. Hiding the page has no effect on tooltips."),

single("V2",
 "When users drill down from Year to Quarter in a column chart, other visuals on the page don't change. They should be filtered to the drilled-into year. What should you configure?",
 ["Turn on Drilling filters other visuals", "Set Edit interactions to None for the chart", "Sync slicers", "A drillthrough page"], "A",
 "The Drilling filters other visuals option makes a drill-down action filter the other visuals on the page. It's off by default for some visuals. Setting interactions to None stops filtering altogether."),

single("V2",
 "A report is always saved by authors on whichever page they were last editing, so readers open it on random pages. Readers must always land on the Overview page. What is the simplest fix?",
 ["Save and publish with Overview as the active page", "Hide every other page", "Add a bookmark navigator with Overview as its first bookmark", "Use persistent filters"], "A",
 "The service opens a report on the page that was active when it was saved and published. Ending authoring on Overview fixes the landing page. Hiding pages removes them from navigation. Bookmark navigators and persistent filters don't control the landing page."),

yesno("V2",
 "For each statement about the Sync slicers pane, select Yes if it is true.",
 [("A slicer can be synced to a page without being visible on that page.", True),
  ("A slicer can be visible on a page without sharing its selection with the other pages.", True),
  ("Synced slicers share their selections across different reports in the same workspace.", False)],
 "Sync and Visible are independent check boxes, so a slicer can filter a page while hidden, or appear on a page independently. Syncing works only between pages of the same report."),

# ---------------- V3 Patterns and trends (2 + 1 in case)
single("V3",
 "You can't find the Find anomalies option for a column chart of daily orders. What should you change?",
 ["Use a line chart with a continuous date axis", "Add a legend", "Use a pie chart", "Switch the X-axis to categorical in the column chart"], "A",
 "Anomaly detection is available for line charts with a time series on a continuous axis. Column charts, legends and a categorical axis don't enable it."),

single("V3",
 "The service-level target is that 95% of tickets close within 48 hours. A line chart of the weekly on-time rate must show the target as a horizontal reference. What should you add?",
 ["A constant line at 0.95", "An average line from the Analytics pane", "A trend line on the weekly on-time rate", "A forecast"], "A",
 "A constant line marks a fixed value, such as a target, that doesn't change with the data. An average line moves with the data. Trend lines and forecasts describe the data's direction."),

# ---------------- S1 Workspaces and assets (3 + 1 in case)
single("S1",
 "Analysts outside the Finance workspace can't find the endorsed Finance semantic model in the OneLake catalog to request access. What should you configure on the model?",
 ["Make the endorsed model discoverable", "Publish it to the web", "Move it to My workspace", "Remove its endorsement so it shows in search"], "A",
 "Discoverability lets users who don't have access see that an endorsed item exists and request access. Publish to web makes it public. Moving it or removing endorsement makes discovery harder."),

single("S1",
 "Users requesting access to a workspace's content should reach the BI team's distribution list rather than individual admins. What should you configure?",
 ["The workspace contact list", "A data alert", "The app's theme", "A deployment rule in the pipeline"], "A",
 "The workspace contact list determines who receives notifications and requests about the workspace. Data alerts, themes and deployment rules don't route access requests."),

single("S1",
 "A newly published app must appear automatically for every member of the Sales security group, without them looking for it under Apps. What should you do?",
 ["Turn on automatic install for the app audience", "Share the workspace URL with the Sales group by email", "Add the Sales group to the workspace as Viewers", "Use Publish to web"], "A",
 "Push-installed apps appear in users' app lists automatically, if the tenant allows pushing apps. Workspace access gives a different experience and exposes all content. Publish to web is public."),

# ---------------- S2 Secure and govern (4)
single("S2",
 "Users belong to a Region role (filters Region) and a Product role (filters Category). They see the union of both roles' rows, but the business requires the intersection (their region and their category only). What should you do?",
 ["Create one role filtering both Region and Category", "Assign users to both roles and set role precedence", "Use bidirectional relationships", "Remove RLS and use page filters"], "A",
 "Membership in several roles is additive, which gives a union. To require both conditions, the filters must be in the same role, where filters on different tables combine as an intersection. Roles have no precedence setting."),

single("S2",
 "You're publishing a workspace app. App users must also be able to build their own reports on the app's semantic models. What can you do as part of publishing?",
 ["Grant app users Build permission on the semantic models", "Give app users the workspace Admin role", "Use Publish to web", "Turn on persistent filters so users can save their views"], "A",
 "App settings can grant Build permission on the underlying semantic models to everyone with app access, so they can create their own reports. Workspace Admin is far more access than needed. The other options don't grant Build."),

single("S2",
 "A new user can open a report on an RLS-secured model, but every visual shows an error or no data. Other users are fine. What is the most likely cause?",
 ["The user isn't a member of any RLS role on the model", "The user's browser is out of date", "The report theme failed to load", "The model has too many measures"], "A",
 "When RLS is defined, users with read access who aren't in any role get no data. Adding the user, or their group, to the right role fixes it. The other causes would affect everyone."),

single("S2",
 "Policy says users may lower a report's sensitivity label (for example from Confidential to General) only if they explain why. What should be configured?",
 ["A label policy that requires justification", "Certification of the report by a Fabric admin", "An app audience restricted to label owners", "A data alert"], "A",
 "Purview label policies can require users to provide a justification when they lower a classification or remove a label, and the action is audited. Certification, audiences and alerts are unrelated."),

# ---------------- Case study (P2, M2, V3, S1)
case("Proseware Telecom",
 "Proseware is a mobile operator with two million subscribers. The Customer table includes StartDate, ChurnDate (blank for active customers), TenureMonths and Phone. Phone numbers were captured in mixed formats, such as \"+91 98480 12345\", \"098480-12345\" and \"(98480) 12345\". Executives work mainly in Microsoft Teams.",
 ["Phone numbers must be stored as digits only, so they can be matched against the billing system.",
  "A measure must count customers who were active at the start of the selected period.",
  "Analysts want to see how churn varies across tenure, in six-month buckets.",
  "Executives must be able to open the churn report from their leadership channel in Teams."],
 [
  single("P2",
   "Which custom column formula keeps only the digits?",
   ["Text.Select ( [Phone], { \"0\"..\"9\" } )", "Text.Remove ( [Phone], { \"0\"..\"9\" } )", "Text.Trim ( [Phone] )", "Number.From ( [Phone] )"], "A",
   "Text.Select keeps only the characters in the given list, here the digits, removing spaces, brackets, dashes and plus signs. Text.Remove would remove the digits instead. Trim handles spaces only. Number.From fails on the formatting characters."),
  single("M2",
   "Which measure counts customers active at the start of the selected period? The Date table doesn't filter Customer.",
   ["VAR S = MIN ( 'Date'[Date] ) RETURN COUNTROWS ( FILTER ( Customer, Customer[StartDate] < S && ( ISBLANK ( Customer[ChurnDate] ) || Customer[ChurnDate] >= S ) ) )", "COUNTROWS ( Customer )", "CALCULATE ( COUNTROWS ( Customer ), ISBLANK ( Customer[ChurnDate] ) )", "VAR S = MAX ( 'Date'[Date] ) RETURN COUNTROWS ( FILTER ( Customer, Customer[StartDate] < S && ( ISBLANK ( Customer[ChurnDate] ) || Customer[ChurnDate] >= S ) ) )"], "A",
   "The period start comes from the Date selection, and a customer was active then if they started before it and had not churned before it. Using MAX tests the end of the period instead. COUNTROWS(Customer) counts everyone. Counting customers with a blank churn date gives today's active base, not the base at the start of the period."),
  single("V3",
   "How should you show churn by tenure bucket?",
   ["Create bins of size 6 on TenureMonths", "Create clusters on TenureMonths", "Add a forecast on tenure in six-month steps", "Use a gauge per bucket"], "A",
   "Bins of size 6 turn tenure into equal six-month buckets, which a column chart can show against churn rate. Clustering finds groups on a scatter chart. Forecasts project time series. Gauges show single values."),
  single("S1",
   "How do you meet the Teams requirement?",
   ["Add the report as a tab in the leadership Teams channel", "Email the .pbix to executives", "Use Publish to web and post the link in the channel", "Export the report to PDF weekly and post it in the channel"], "A",
   "Power BI reports can be added as tabs in Teams channels, respecting each user's Power BI permissions, and apps can be opened in the Power BI app for Teams. Emailing files, public links or PDFs lose interactivity, governance, or both."),
 ]),
]
