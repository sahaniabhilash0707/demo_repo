from model import single, multi, yesno, match, order, case

TITLE = "Power Query in depth"
SUBTITLE = "Connectors, privacy levels, dataflows, profiling, cleaning, joins, grouping and keys, with the other domains at full weight."
LEVEL = "Level 1 · Foundation"
CASE_NAME = "Northwind Traders"

ITEMS = [
# ---------------- P1 Get or connect to data (4)
single("P1",
 "A query reads an Excel workbook of employee salaries. The workbook must never be sent to any other data source during query evaluation. Which privacy level should you set for it?",
 ["Public", "Organizational", "Private", "None"], "C",
 "Private data is never shared with any other source when Power Query combines data. Organizational data can be shared with other Organizational sources. Public data can be shared with anything. Setting the correct level is how you stop sensitive data leaking during folding."),

single("P1",
 "Each month a new CSV file with the same columns is saved to the same SharePoint Online folder. The report must include every file, and new files must be picked up automatically on refresh. How should you connect?",
 ["Connect to each file with the Text/CSV connector and append them", "Use the SharePoint folder connector, filter to the folder, and use Combine files", "Use the Web connector with the URL of the newest file", "Ask the business to paste each month into one workbook"], "B",
 "The SharePoint folder connector lists every file, and Combine files applies the same transformation to all of them through a sample file. New files in the folder are included on the next refresh. Connecting file by file means editing the query every month."),

single("P1",
 "Ten semantic models in different workspaces each clean the same Customer table from the ERP system with the same 25 Power Query steps. You want the logic in one place in the Power BI service, reusable by all ten models. What should you create?",
 ["A dataflow that produces the cleaned Customer table", "A .pbit template containing the query", "A calculated table in each model", "A bookmark containing the steps"], "A",
 "A dataflow runs Power Query in the service and stores the result, so any semantic model can connect to the cleaned table. Changes are made once. A template is a starting point that still copies the steps into each file. Calculated tables are DAX and can't call the ERP connector."),

single("P1",
 "Regulations say a patient-records table must not be copied out of the hospital's SQL database, but reports must show it. The database is reachable through a gateway. Which storage mode should you use for this table?",
 ["Import", "DirectQuery", "Dual", "Import with incremental refresh"], "B",
 "DirectQuery leaves the data in the source and sends a query each time a visual needs it, so no copy is stored in Power BI. Import, with or without incremental refresh, copies the data into the model. Dual also keeps an imported copy."),

# ---------------- P2 Profile and clean (3)
single("P2",
 "A numeric Discount column has a few cells that show Error after a type change. Every row must be kept, and the failed cells must become null. Which action should you use?",
 ["Remove errors", "Replace errors, with the value null", "Remove blank rows", "Keep errors"], "B",
 "Replace errors keeps the rows and substitutes a value of your choice, here null. Remove errors deletes the rows that contain errors, which breaks the requirement. Keep errors does the opposite, keeping only the failing rows, which is useful for investigation but not as a fix."),

single("P2",
 "A CSV from the German subsidiary stores amounts as 1.234,56. On your English (United States) machine they load as text or wrong numbers. What should you do?",
 ["Use Replace values to swap commas and dots", "Use Change Type → Using Locale, with type Decimal Number and locale German (Germany)", "Change the Windows regional settings of the gateway", "Set the column's data category to Currency"], "B",
 "Change Type Using Locale tells Power Query which culture the source text uses, so the separators are interpreted correctly wherever the file is refreshed. Replacing characters by hand is fragile. Machine settings shouldn't decide how data is parsed. A data category doesn't parse text."),

single("P2",
 "Customer IDs should be unique, but you suspect some appear more than once. You want a quick list of only the rows whose CustomerID is repeated. What should you do in Power Query?",
 ["Select CustomerID and choose Keep Rows → Keep duplicates", "Select CustomerID and choose Remove duplicates", "Turn on Column quality", "Group by CustomerID with the All rows operation"], "A",
 "Keep duplicates returns only the rows whose values in the selected column occur more than once, which is the investigation you want. Remove duplicates hides the problem. Column quality shows valid, error and empty percentages, not repeats. Grouping can find them but needs more steps."),

# ---------------- P3 Transform and load (4 + 1 in case)
yesno("P3",
 "You merge Orders (left table) with Customers (right table) on CustomerID. For each statement, select Yes if it is true.",
 [("A Left outer join keeps every order, with nulls where no customer matches.", True),
  ("An Inner join keeps every customer, even those with no orders.", False),
  ("A Right anti join returns customers that have no orders.", True)],
 "Left outer keeps all left rows. Inner keeps only rows that match on both sides, so customers without orders drop out. Right anti returns rows from the right table with no match in the left, which here means customers who never ordered."),

single("P3",
 "You need, for each customer, only their most recent order row, with all of that row's columns. Which approach works in Power Query?",
 ["Group by CustomerID with All rows, then extract the row with the latest OrderDate from each nested table", "Remove duplicates on CustomerID without sorting", "Pivot OrderDate", "Append the Orders query to itself"], "A",
 "Group by with the All rows operation keeps each customer's rows as a nested table, from which you can take the row with the maximum date (for example with Table.Max). Removing duplicates without a guaranteed sort order isn't reliable for picking the latest row. Pivoting and appending don't solve the problem."),

single("P3",
 "Without writing M code, you must add a SizeBand column: \"Small\" when Quantity is below 10, \"Medium\" below 100, otherwise \"Large\". Which feature should you use?",
 ["Add Column → Conditional column", "Transform → Pivot column", "Add Column → Index column", "Transform → Unpivot columns"], "A",
 "A conditional column builds if-then-else logic through a dialog, with one rule per row and an Else value. Pivot and unpivot reshape the table. An index column adds row numbers."),

order("P3",
 "You must give the Product dimension an integer surrogate key and replace the text ProductCode in Sales with that key. Put the required actions in order.",
 ["In the Product query, remove duplicates on ProductCode",
  "In the Product query, add an Index column starting from 1 and rename it ProductKey",
  "In the Sales query, merge with Product on ProductCode",
  "Expand only ProductKey from the merged column",
  "Remove the ProductCode column from Sales"],
 "The dimension must have one row per code before the key is numbered. The fact then looks up the key through a merge, keeps only the key, and drops the text code. Narrow integer keys make relationships smaller and faster.",
 extra=["Append Product to Sales"]),

# ---------------- M1 Design and implement a model (4)
single("M1",
 "A Budget table holds amounts per product Category per month. The Product table has one row per product, including a Category column. Users must filter both budget and actual sales by category with one slicer. What is the recommended design?",
 ["Create a Category dimension with one row per category, related one-to-many to both Product and Budget", "Relate Budget to Sales directly on Category", "Merge Budget into Product", "Create a one-to-one relationship between Budget and Product"], "A",
 "A Category dimension at the budget's grain can filter Budget directly and Product (and through it Sales). The slicer uses Category[Category]. Relating two facts directly, or merging budget values into a product-grain table, breaks the grain. A one-to-one relationship isn't possible because many products share a category."),

single("M1",
 "Report authors are confused by ProductKey, CustomerKey and DateKey columns in the Sales table field list. The columns must stay for the relationships. What should you do?",
 ["Delete the columns", "Hide the columns in report view", "Rename them with a leading underscore", "Move them to a display folder named Keys"], "B",
 "Hiding a column removes it from the report field list while it still works in relationships and DAX. Deleting it would break the relationships. Renaming or using a display folder still leaves the keys visible to authors."),

single("M1",
 "Sales managers want a slider on the report to try discount rates from 0% to 30% and see the effect on projected revenue. Which feature creates the table and measure they need?",
 ["A numeric range parameter (what-if parameter)", "A calculation group", "A bookmark", "Incremental refresh"], "A",
 "A numeric range parameter creates a calculated table of values, a measure that returns the selected value, and a slider slicer. Your revenue measure then references the parameter measure. Calculation groups apply logic to existing measures. Bookmarks and incremental refresh solve different problems."),

single("M1",
 "A Margin % measure shows 0.2381 in visuals. It must always show as 23.8% wherever it's used. What should you change?",
 ["The measure's Format to Percentage with one decimal place", "Each visual's data label format", "The DAX to multiply by 100", "The data type of the Sales table"], "A",
 "A format string on the measure applies wherever the measure is used, in every visual and report built on the model. Formatting each visual must be repeated. Multiplying by 100 shows 23.81 without a % sign and breaks other calculations."),

# ---------------- M2 DAX (5 + 1 in case)
single("M2",
 "Sales has an Amount column. You need the number of sales rows where Amount is greater than 1,000, in the current filter context. Which measure is correct?",
 ["CALCULATE ( COUNTROWS ( Sales ), Sales[Amount] > 1000 )", "COUNTROWS ( Sales ) > 1000", "COUNTX ( Sales, 1000 )", "SUM ( Sales[Amount] ) > 1000"], "A",
 "The filter argument keeps only rows with Amount above 1,000, and COUNTROWS counts them while respecting the visual's existing filters. The other expressions return TRUE or FALSE, or count every row."),

single("M2",
 "Sales has Quantity and UnitPrice columns but no revenue column. You need a Revenue measure without adding a column. Which expression is correct?",
 ["SUM ( Sales[Quantity] ) * SUM ( Sales[UnitPrice] )", "SUMX ( Sales, Sales[Quantity] * Sales[UnitPrice] )", "SUMMARIZE ( Sales, Sales[Quantity] )", "CALCULATE ( SUM ( Sales[Quantity] ), Sales[UnitPrice] )"], "B",
 "SUMX iterates the table, multiplies quantity by price for each row and then adds the results. Multiplying the two totals gives a wrong number whenever there's more than one row. SUMMARIZE returns a table. The CALCULATE expression isn't valid."),

single("M2",
 "You need a rolling 12-month sales measure ending at the last date in the current filter context. Complete the expression.",
 ["DATESINPERIOD ( 'Date'[Date], MAX ( 'Date'[Date] ), -12, MONTH )", "DATESYTD ( 'Date'[Date] )", "SAMEPERIODLASTYEAR ( 'Date'[Date] )", "PARALLELPERIOD ( 'Date'[Date], -12, MONTH )"], "A",
 "DATESINPERIOD returns the dates from the end date back 12 months, which CALCULATE uses as the filter. DATESYTD resets each January. SAMEPERIODLASTYEAR shifts to last year. PARALLELPERIOD returns whole periods shifted back, not a rolling window.",
 code="Sales R12M =\nCALCULATE ( [Total Sales],\n    ____ )"),

single("M2",
 "What is the main benefit of the VAR in this measure?",
 ["The variable is evaluated once and reused, which makes the measure easier to read and avoids calculating [Total Sales] twice", "Variables are stored in the model and reused by other measures", "VAR forces the measure to ignore slicers", "VAR turns the measure into a calculated column"], "A",
 "A variable is evaluated once, where it's defined, and can be referenced several times in the RETURN. That improves readability and performance. Variables exist only inside that measure's evaluation. They don't change filter context or storage.",
 code="Sales Growth % =\nVAR Curr = [Total Sales]\nVAR Prev = [Sales PY]\nRETURN DIVIDE ( Curr - Prev, Prev )"),

single("M2",
 "A measure must return \"High\" when [Margin %] is at least 40%, \"Medium\" when it's at least 20%, otherwise \"Low\". Which pattern is the clearest?",
 ["SWITCH ( TRUE (), [Margin %] >= 0.4, \"High\", [Margin %] >= 0.2, \"Medium\", \"Low\" )", "SWITCH ( [Margin %], 0.4, \"High\", 0.2, \"Medium\", \"Low\" )", "IF ( [Margin %], \"High\", \"Low\" )", "LOOKUPVALUE ( [Margin %], \"High\" )"], "A",
 "SWITCH(TRUE(), ...) tests each condition in order and returns the first match, which handles ranges. SWITCH on the value itself only matches exact values like 0.4. IF with no comparison isn't a range test. LOOKUPVALUE retrieves column values."),

# ---------------- M3 Optimize (2)
single("M3",
 "You want to run and test a DAX query against the model inside Power BI Desktop, including a measure definition you haven't added yet. Which statement starts the query in DAX query view?",
 ["EVALUATE", "SELECT", "RETURN", "MEASURE"], "A",
 "A DAX query begins with EVALUATE followed by a table expression. A DEFINE block before it can hold MEASURE definitions to test before you add them to the model. SELECT is SQL. RETURN belongs inside a VAR expression."),

single("M3",
 "A 200-million-row fact table has a TransactionDateTime column with a different value on almost every row. It's the largest column in the model. Reports filter by date and by hour. What should you do?",
 ["Split it into a Date column and a Time column (or hour) in Power Query, and remove the original", "Change it to Text", "Mark the table as a date table", "Set the column's Summarize by to None"], "A",
 "Column size is driven by cardinality. Splitting date and time gives two columns with far fewer distinct values, which compress much better, and the Date column can relate to the date table. Text would be larger. Marking a date table or changing summarisation doesn't change storage."),

# ---------------- V1 Create reports (5)
single("V1",
 "A table shows revenue growth by product. Users want a green up arrow when growth is positive and a red down arrow when it's negative. What should you configure?",
 ["Conditional formatting → Icons, with rules on the growth value", "Data bars on the growth column", "A bookmark for positive growth", "Sort the table by growth"], "A",
 "Icon conditional formatting places icons such as arrows next to values, based on rules or a field value. Data bars show magnitude, not direction. Bookmarks and sorting don't add indicators."),

match("V1",
 "Match each requirement to the most appropriate visual.",
 [("Show this month's revenue against target, with the trend behind it, in one compact element", "KPI"),
  ("Show how last year's profit becomes this year's profit through increases and decreases by driver", "Waterfall chart"),
  ("Show one value on a dial between a minimum and a maximum, with a target marker", "Gauge")],
 ["KPI", "Waterfall chart", "Gauge", "Funnel chart", "Ribbon chart"],
 "A KPI shows a value, its goal and a trend. A waterfall shows a running total built from positive and negative contributions. A gauge shows a single value within a range against a target. A funnel shows sequential stages, and a ribbon chart shows how ranking changes over time.",
 left="Requirement", right="Visual"),

single("V1",
 "A report will be shown on a wall display with an ultra-wide 32:9 screen. The page must fill the screen without letterboxing. What should you change?",
 ["Canvas settings → Type: Custom, with a width and height matching 32:9", "The page view to Actual size", "The theme", "The mobile layout"], "A",
 "Canvas settings control the page size. A custom size can match any aspect ratio. Page view changes how the page is displayed in the editor, not its dimensions. Themes change styling. Mobile layout is for phones."),

single("V1",
 "You plan to use Copilot to create a new report page from a prompt. What change to the semantic model will most improve the quality of what Copilot builds?",
 ["Add clear names, descriptions and synonyms to tables, columns and measures", "Switch every table to DirectQuery", "Turn on Auto date/time", "Remove all relationships"], "A",
 "Copilot works from the model's metadata. Descriptive names, descriptions and synonyms help it choose the right fields and measures. Storage mode and Auto date/time don't help it understand the data, and removing relationships breaks the model."),

single("V1",
 "A page must always show the last 7 days of data, moving forward automatically each day, with no change by the author. Which slicer setting meets this?",
 ["A relative date slicer set to Last 7 days", "A between date slicer with fixed start and end dates", "A list slicer on Date", "A page-level filter Date is after 1 January"], "A",
 "A relative date slicer, or a relative date filter, evaluates the period relative to today each time the report is used. Fixed dates or lists need manual updates."),

# ---------------- V2 Usability and storytelling (4 + 1 in case)
single("V2",
 "You create a drillthrough page with Product[Category] in its Drill through well. What does Power BI add to the page automatically?",
 ["A Back button that returns users to the page they came from", "A slicer on Category", "A bookmark for every category", "A tooltip page"], "A",
 "When you add a field to the Drill through well, Power BI adds a Back button that takes users back to the source page. Category filtering comes from the drillthrough action itself, not from a slicer."),

single("V2",
 "A Year slicer must keep the same selection on pages 1, 2 and 3, but page 4 must be filtered independently by its own Year slicer. What should you do?",
 ["In the Sync slicers pane, sync the slicer on pages 1–3 and leave page 4 unsynced", "Copy the slicer to every page", "Use a report-level filter on Year", "Use drillthrough from page 1"], "A",
 "The Sync slicers pane controls, per page, whether a slicer shares its selection (Sync) and whether it's shown (Visible). Pages 1–3 sync and page 4 stays independent. A report-level filter applies to every page. Copying a slicer without syncing doesn't share the selection."),

single("V2",
 "Report authors want a slicer that lets viewers choose whether a chart shows Revenue, Profit or Units, and the chart's axis title must change to match. Which feature should you use?",
 ["A field parameter with the three measures", "Three bookmarks", "A calculation group with three items", "Personalize visuals"], "A",
 "A field parameter creates a table of fields that a slicer can switch between. The visual uses the chosen field, including its name. Bookmarks need three copies of the chart. Personalize visuals lets each viewer change the visual themselves, but the requirement is a designed slicer. A calculation group would keep one measure name."),

single("V2",
 "A bar chart shows Revenue by Region. When users hover over a bar, the tooltip must also show the Margin % measure, which isn't on the chart. What is the simplest way?",
 ["Add Margin % to the visual's Tooltips well", "Create a report-page tooltip", "Add Margin % to the Y-axis", "Create a bookmark"], "A",
 "Fields in the Tooltips well appear in the default tooltip without being plotted. A report-page tooltip is for richer custom content. Adding the measure to the axis would plot it."),

# ---------------- V3 Patterns and trends (3)
single("V3",
 "A line chart shows daily website orders over a year. You want Power BI to flag unexpected spikes and dips automatically and suggest possible explanations. What should you use?",
 ["Find anomalies on the line chart", "A forecast in the Analytics pane", "An average line", "Binning on the date axis"], "A",
 "Anomaly detection marks points outside the expected range, with a sensitivity setting, and lists possible explanations from fields you choose. Forecasting projects future values. An average line is a static reference. Binning groups the axis."),

single("V3",
 "A column chart shows a sharp drop in revenue from March to April. A manager wants Power BI to suggest which dimensions contributed most to the drop. What should they do?",
 ["Right-click the April column and choose Analyze → Explain the decrease", "Add a trend line", "Add a forecast", "Turn on data labels"], "A",
 "Analyze → Explain the decrease runs an analysis of the change between the two points and shows which categories contributed. Trend lines, forecasts and data labels describe the series but don't explain the change."),

single("V3",
 "Users ask the Q&A visual about \"turnover\", but the measure is called Revenue, so Q&A doesn't understand. What should you configure?",
 ["Add turnover as a synonym for the Revenue measure in Q&A setup or the model's synonyms", "Rename the Revenue measure Turnover", "Add a smart narrative", "Create a bookmark named turnover"], "A",
 "Synonyms teach Q&A the alternative words users type, without renaming the measure for everyone else. Renaming breaks the business's standard terminology. Smart narrative and bookmarks don't change how Q&A interprets questions."),

# ---------------- S1 Workspaces and assets (3 + 1 in case)
multi("S1",
 "Which two workspace roles can publish or update the workspace app by default?",
 ["Admin", "Member", "Contributor", "Viewer", "App audience member"], "AB",
 "By default, Admins and Members can publish and update the app. Contributors can create and edit content but can't update the app unless an admin turns on the setting that allows it. Viewers and app audience members only consume content."),

single("S1",
 "A sales manager wants a snapshot of a report page emailed to her and her team every Monday at 08:00. What should you set up?",
 ["A subscription on the report page", "A data alert", "A Publish to web link", "A deployment pipeline"], "A",
 "A subscription emails a snapshot and link on a schedule, and the owner can include other recipients. A data alert fires when a dashboard tile crosses a threshold, not on a schedule. Publish to web is public. Deployment pipelines promote content between stages."),

single("S1",
 "A semantic model uses DirectQuery to an on-premises Oracle database and is used by 200 people. Which gateway setup is appropriate?",
 ["A standard on-premises data gateway, installed on a server and managed centrally", "A personal-mode gateway on the developer's laptop", "No gateway; DirectQuery connects from each user's browser", "A virtual network gateway in Azure only"], "A",
 "DirectQuery to an on-premises source needs a standard (enterprise) gateway. Personal mode supports only Import refresh for one user, and a laptop isn't always on. Browsers never connect to the database directly."),

# ---------------- S2 Secure and govern (4)
single("S2",
 "You have created RLS roles in Power BI Desktop. How can you check what a member of the Europe role will see before you publish?",
 ["Modeling → View as, and select the Europe role", "Publish and ask a colleague to log in", "Open DAX query view and run EVALUATE Europe", "Use Performance Analyzer"], "A",
 "View as applies one or more roles (and optionally another user name) to the report in Desktop, so you can check the result. You can also test in the service later with Test as role. DAX query view and Performance Analyzer don't apply roles."),

single("S2",
 "Users in the India role must see only rows where Customer[Country] is India. Countries rarely change and only three roles are needed. Which role filter is correct?",
 ["[Country] = \"India\" on the Customer table", "[Country] = USERPRINCIPALNAME() on the Customer table", "FILTER ( ALL ( Customer ), TRUE () )", "[Country] <> \"India\" on the Sales table"], "A",
 "A static role filter is a DAX boolean expression on a table. Rows where it's TRUE are visible, and the filter flows to related tables. Comparing a country to the user name is meaningless. FILTER(ALL(...)) returns a table, not a row condition. The last filter shows every other country."),

single("S2",
 "You share a report with a consultant. The consultant must be able to view it but must not be able to share it with anyone else. What should you do when sharing?",
 ["Clear \"Allow recipients to share this report\"", "Give the consultant the workspace Member role", "Apply a sensitivity label", "Grant Build permission on the semantic model"], "A",
 "The share dialog lets you control resharing. Clearing that option gives view access without the right to share further. The Member role grants far more. Labels don't control sharing. Build lets the consultant create content, which goes beyond what's needed."),

single("S2",
 "A model must hide the Salary column completely from some users. The column must not even appear in their field list or be queryable. Row filters aren't needed. Which feature, and where is it authored?",
 ["Object-level security, authored with an external tool such as Tabular Editor", "Row-level security, authored in Manage roles", "A sensitivity label on the model", "Hiding the column in report view"], "A",
 "Object-level security secures tables or columns for a role, so they aren't visible or queryable. It's set through the XMLA endpoint or tools like Tabular Editor rather than the Desktop UI. RLS filters rows. Hidden columns can still be queried, and labels classify content."),

# ---------------- Case study (P3, M2, V2, S1)
case("Northwind Traders",
 "Northwind Traders distributes food products from three warehouses. Every night the warehouse system saves a CSV of the day's orders to a SharePoint folder. Each file has a header row, the order lines, and a final row that starts with the word Total. Orders contain OrderDate, DueDate, ShipDate, Warehouse, Product and Quantity. A Power BI Pro workspace is used.",
 ["All nightly files must be included automatically on each refresh.",
  "Managers need the number of orders that shipped after their due date.",
  "From a summary page, managers must open a detailed page for one warehouse, filtered to that warehouse.",
  "The operations manager wants an email whenever late orders for the day exceed 50."],
 [
  single("P3",
   "After combining the files from the folder, every combined file still includes its Total row. Where and how should you remove it?",
   ["In the Transform Sample File query, use Remove Rows → Remove bottom rows (1 row)", "In the final combined query, remove the last row", "Filter the Warehouse column to remove blanks", "Delete the Total rows in each CSV by hand"], "A",
   "Steps in Transform Sample File run against every file before they are appended, so removing the bottom row there drops each file's Total row. Removing the last row of the combined query only removes the final file's total. Editing the files by hand isn't sustainable."),
  single("M2",
   "Which measure counts orders that shipped late?",
   ["COUNTROWS ( FILTER ( Orders, Orders[ShipDate] > Orders[DueDate] ) )", "COUNT ( Orders[ShipDate] ) > COUNT ( Orders[DueDate] )", "CALCULATE ( COUNTROWS ( Orders ), ALL ( Orders ) )", "DATEDIFF ( Orders[DueDate], Orders[ShipDate], DAY )"], "A",
   "FILTER iterates Orders and keeps rows where the ship date is after the due date, and COUNTROWS counts them within the current filter context. Comparing two counts returns TRUE or FALSE. ALL removes every filter. DATEDIFF needs scalar dates, not columns, in a measure."),
  single("V2",
   "How should you build the warehouse detail page?",
   ["Add Warehouse to the Drill through well of the detail page", "Create a bookmark for each warehouse", "Add a Warehouse slicer to the summary page and sync it", "Create a tooltip page"], "A",
   "Drillthrough lets users right-click a warehouse on the summary page and open the detail page filtered to it, with a Back button. Bookmarks per warehouse don't scale. A synced slicer filters but doesn't navigate. Tooltip pages appear on hover."),
  single("S1",
   "How do you meet the operations manager's alert requirement?",
   ["Pin a card showing today's late orders to a dashboard and set a data alert on the tile above 50", "Create a subscription to the report page", "Add conditional formatting to the card", "Use Publish to web"], "A",
   "Power BI data alerts are set on dashboard tiles such as cards, KPIs and gauges, and email the user when the value crosses the threshold. A subscription sends a scheduled snapshot whatever the value. Conditional formatting changes colour but sends nothing."),
 ]),
]
