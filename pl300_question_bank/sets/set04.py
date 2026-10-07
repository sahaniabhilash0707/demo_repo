from model import single, multi, yesno, match, order, case

TITLE = "DAX essentials"
SUBTITLE = "CALCULATE, context transition, iterators, time intelligence and semi-additive balances, with the rest of the outline at full weight."
LEVEL = "Level 2 · Core"
CASE_NAME = "Woodgrove Bank"

ITEMS = [
# ---------------- P1 Get or connect to data (4)
single("P1",
 "In Power BI Desktop, you want to browse the Fabric lakehouses, warehouses and semantic models you have access to and connect to one of them. Which Get data entry point lists them?",
 ["OneLake catalog", "Blank query", "Web", "Folder"], "A",
 "The OneLake catalog in Power BI Desktop lists Fabric items you can access, including lakehouses, warehouses and semantic models, and connects to them. Blank query, Web and Folder are generic connectors with no catalog of Fabric items."),

single("P1",
 "You are configuring incremental refresh. RangeStart and RangeEnd are Date/Time parameters. Which filter on OrderDateTime stops rows on a partition boundary from loading twice?",
 ["[OrderDateTime] >= RangeStart and [OrderDateTime] < RangeEnd", "[OrderDateTime] >= RangeStart and [OrderDateTime] <= RangeEnd", "[OrderDateTime] > RangeStart and [OrderDateTime] <= RangeEnd + 1", "[OrderDateTime] = RangeStart"], "A",
 "One side of the range must be inclusive and the other exclusive, so a row exactly on a boundary lands in exactly one partition. Making both inclusive loads boundary rows into two partitions. An equality filter would load almost nothing."),

single("P1",
 "A report is live-connected to a shared semantic model. The author must add a small Excel table of regional targets and relate it to the model's Region table. What should the author do?",
 ["Select Make changes to this model", "Import the shared model's tables into a new file", "Ask for workspace Admin on the shared model", "Paste the targets into a DAX calculated column"], "A",
 "Make changes to this model converts the live connection into DirectQuery for Power BI semantic models, so local tables like the Excel targets can be added and related. The shared model stays unchanged. Importing creates an ungoverned copy. Admin rights aren't needed."),

single("P1",
 "Twelve queries in a file connect to SQL server SQLPROD01, which is being renamed SQLPROD02. You want to change all twelve in one place without editing each query. Where do you do this?",
 ["Data source settings → select the source → Change Source", "Each query's Source step in the Advanced editor", "Model view → Properties", "Options → Global → Data load"], "A",
 "Change Source in Data source settings updates every query that uses that source in one action. Editing each query's Source step works but repeats the change twelve times. (A server-name parameter would also work, if it had been set up earlier.)"),

# ---------------- P2 Profile and clean (2 + 1 in case)
single("P2",
 "Text exported from a mainframe contains non-printable control characters, so values that look identical don't match in merges. Which transformation removes them?",
 ["Clean", "Trim", "Lowercase", "Replace errors"], "A",
 "Clean removes non-printable characters. Trim removes only leading and trailing spaces. Changing case doesn't remove characters, and the values aren't errors, so Replace errors does nothing here."),

single("P2",
 "After applying changes, Power BI reports that 37 rows of the Orders query contain errors. You need to see exactly which rows failed and why. What should you do?",
 ["Select View errors to open an errors query", "Turn on Column quality and Column distribution", "Delete the Orders query and import it again", "Open Performance Analyzer"], "A",
 "View errors builds an errors query that isolates the problem rows and shows each error. That's the fastest way to diagnose import errors. Column quality and distribution show percentages and counts, not failing rows. Performance Analyzer measures report performance."),

# ---------------- P3 Transform and load (5)
single("P3",
 "A Suppliers query must be matched to an Invoices query on company name, but names differ slightly (\"Contoso Ltd\" vs \"Contoso Limited\"). Which Merge option helps?",
 ["Use fuzzy matching, with a similarity threshold", "Use a Left anti join", "Append the two queries", "Use Group by on the name"], "A",
 "Fuzzy matching in a merge pairs values that are similar rather than identical, with a threshold and optional transformation table. An anti join returns rows that don't match. Append stacks rows. Grouping doesn't compare two tables."),

single("P3",
 "The Sales OrderDate column is Date/Time and every value has a 00:00 time. The Date table's Date column is of type Date. You want a clean relationship and smaller storage. What should you do in Power Query?",
 ["Change the OrderDate column type to Date", "Change the Date table's column to Text", "Add an index column", "Change the OrderDate column type to Text"], "A",
 "Converting to Date matches the date table's type, drops the meaningless time part and reduces storage. Text columns relate less efficiently and break time-intelligence logic. An index column doesn't help."),

single("P3",
 "You append NorthSales and SouthSales. NorthSales has a column named Amount and SouthSales has Amt. After the append, half the rows have null Amount. What is the fix?",
 ["Rename Amt to Amount in SouthSales before appending", "Use Merge queries instead of Append", "Replace nulls with 0 after appending", "Change both columns to Text"], "A",
 "Append matches columns by name. Different names produce two partly empty columns. Renaming them first fixes the cause. Replacing nulls with 0 hides the problem and gives wrong totals. Merge joins tables rather than stacking them."),

multi("P3",
 "Sales and Price can only be matched on the combination of Region and ProductCode. Power BI relationships use a single column. Which two actions together create a working relationship?",
 ["Add a combined key column (Region & \"|\" & ProductCode) in both queries in Power Query", "Relate the two tables on the new combined key columns", "Create two active relationships, one on Region and one on ProductCode", "Set the relationship on Region to Both", "Create a many-to-many relationship on ProductCode alone"], "AB",
 "A relationship needs one column on each side, so build a combined key in both tables and relate on it. Power BI allows only one active relationship between two tables. Relating on one column alone would match the wrong rows."),

order("P3",
 "No date table exists in any source. You decide to build one in Power Query and use it for time intelligence. Put the required actions in order.",
 ["Create a list of dates with List.Dates covering whole years",
  "Convert the list to a table and set the column type to Date",
  "Add Year, Month and MonthNumber columns",
  "Load the table and mark it as a date table in the model"],
 "Generate the dates, convert them to a typed table, add the attributes reports need, then mark the table as a date table after loading so time intelligence uses it. Marking happens in the model, not in Power Query.",
 extra=["Turn on Auto date/time", "Merge the date list with the Sales query"]),

# ---------------- M1 Design and implement a model (4)
single("M1",
 "You set the sort-by column of MonthName to MonthKey (values like 202501, 202601). Power BI shows an error. What should you do?",
 ["Sort MonthName by MonthNumber (1–12) instead", "Sort MonthName by Date", "Change MonthName to a number", "Remove the relationship to Sales"], "A",
 "A sort-by column must have exactly one value for each value of the column being sorted. \"January\" has several MonthKey values (one per year), so the sort fails. MonthNumber has one value per month name. Date has many values per month name too."),

single("M1",
 "Report users want to drill from Year to Quarter to Month in visuals without adding three fields each time. What should you create in the model?",
 ["A Year–Quarter–Month hierarchy on the Date table", "Three calculated columns", "A calculation group with Year, Quarter and Month items", "A bookmark"], "A",
 "A hierarchy groups levels so authors drag one field and users can drill up and down. Calculated columns add fields but not drill behaviour. Calculation groups change measures. Bookmarks store views."),

single("M1",
 "Which is a good use case for a calculated table?",
 ["A role-playing ShipDate table copied from the Date table", "Cleaning text values that come from a CSV", "Combining the monthly CSV files in a folder", "Removing duplicate customers before they're loaded from the source"], "A",
 "Calculated tables are DAX tables built from data already in the model, such as a copy of the Date table for another role, or a disconnected parameter table. Cleaning and combining source files is a Power Query task done before loading."),

yesno("M1",
 "For each statement about column properties, select Yes if it is true.",
 [("A Year column that is summed in visuals should have Summarize by set to Don't summarize.", True),
  ("Setting a column's data category to Country/Region changes its data type to Text.", False),
  ("A format string set on a column applies in every visual that uses that column.", True)],
 "Numeric attributes such as Year or ID shouldn't be aggregated, so set them to Don't summarize. Data category only describes the meaning of the values, mainly for maps, and doesn't change the data type. Model-level formats apply everywhere the column is used."),

# ---------------- M2 DAX (5 + 1 in case)
single("M2",
 "Which measure returns quarter-to-date sales?",
 ["TOTALQTD ( [Total Sales], 'Date'[Date] )", "TOTALYTD ( [Total Sales], 'Date'[Date], \"3/31\" )", "DATESQTD ( [Total Sales] )", "CALCULATE ( [Total Sales], QUARTER ( 'Date'[Date] ) )"], "A",
 "TOTALQTD accumulates from the start of the quarter to the last date in context. TOTALYTD with a year-end date is a fiscal year-to-date. DATESQTD takes a date column, not a measure, and returns dates. QUARTER returns a number, which isn't a valid filter."),

single("M2",
 "In the Customer table, a calculated column CustSales = [Total Sales] returns each customer's own sales, but CustSales2 = SUM ( Sales[Amount] ) returns the grand total on every row. Why?",
 ["Measure references trigger context transition; SUM doesn't", "Measures are stored in the Customer table", "SUM ignores relationships in every case", "Calculated columns can't use aggregation functions such as SUM"], "A",
 "A measure reference is wrapped in an implicit CALCULATE, which converts the row context into a filter context on that customer. SUM in a calculated column has a row context but no filter context, so it sums the whole Sales table."),

single("M2",
 "A card must show the combined sales of the top five products by sales, whatever the visual is filtered to. Which measure is correct?",
 ["CALCULATE ( [Total Sales], TOPN ( 5, ALL ( 'Product'[Name] ), [Total Sales] ) )", "TOPN ( 5, 'Product', [Total Sales] )", "SUMX ( FILTER ( 'Product', RANKX ( 'Product', [Total Sales] ) <= 5 ), [Total Sales] )", "MAXX ( 'Product', [Total Sales] ) * 5"], "A",
 "TOPN returns the five products with the highest sales, and CALCULATE uses that table as a filter on the sales measure. TOPN on its own returns a table, not a value. Ranking over 'Product' without ALL follows the visual's filters, so the top five change with them. MAXX times five isn't the top-five total."),

single("M2",
 "Operations wants the delivery time, in days, below which 90% of deliveries fall. Which function should the measure use?",
 ["PERCENTILE.INC ( Deliveries[Days], 0.9 )", "AVERAGE ( Deliveries[Days] ) * 0.9", "MAX ( Deliveries[Days] )", "STDEV.P ( Deliveries[Days] )"], "A",
 "PERCENTILE.INC returns the value at the given percentile, here the 90th. Ninety percent of the average isn't a percentile. MAX returns the worst case. Standard deviation measures spread, not a threshold."),

match("M2",
 "Match each requirement to the time-intelligence function that fits it.",
 [("Opening balance on the first day of the selected period", "FIRSTDATE"),
  ("Closing balance on the last date that actually has data", "LASTNONBLANK"),
  ("Sales for the same dates shifted back one quarter", "DATEADD"),
  ("Sales during a fixed promotion window, 1 to 15 March", "DATESBETWEEN")],
 ["FIRSTDATE", "LASTNONBLANK", "DATEADD", "DATESBETWEEN", "TOTALYTD"],
 "FIRSTDATE returns the first date in context. LASTNONBLANK finds the last date where an expression isn't blank. DATEADD shifts dates by an interval. DATESBETWEEN returns a fixed range. TOTALYTD accumulates the year, which none of these need.",
 left="Requirement", right="Function"),

# ---------------- M3 Optimize (2)
single("M3",
 "A fact table stores one row per sensor reading per second, but every report shows daily totals by machine. The model is too large. What is the most effective change?",
 ["Group to one row per machine per day in Power Query", "Hide the timestamp column", "Change the table to DirectQuery", "Add a calculated column with the date and hide the timestamp"], "A",
 "Reducing granularity to what the reports use can cut row count by orders of magnitude, which shrinks the model and speeds up queries. Hiding a column doesn't reduce storage. DirectQuery moves the problem to the source. A calculated column adds size."),

single("M3",
 "Two large tables are related many-to-many on a long text column, and visuals using them are slow. Which change is most likely to help?",
 ["A dimension with integer keys, one-to-many to both tables", "Change the many-to-many relationship's cross-filter direction to Both", "Turn on Auto date/time", "Add more measures"], "A",
 "Many-to-many relationships on high-cardinality text keys are expensive. A proper dimension with integer keys gives efficient one-to-many relationships. Bidirectional filtering usually adds cost. The other options don't address the relationship."),

# ---------------- V1 Create reports (4 + 1 in case)
single("V1",
 "A matrix shows sales by Category and Product. You need a column showing each row's share of the grand total, written as a visual calculation. Complete the expression.",
 ["DIVIDE ( [Sales], COLLAPSEALL ( [Sales], ROWS ) )", "DIVIDE ( [Sales], CALCULATE ( [Sales], ALL ( 'Product' ) ) )", "RUNNINGSUM ( [Sales] )", "DIVIDE ( [Sales], PREVIOUS ( [Sales] ) )"], "A",
 "COLLAPSEALL evaluates the expression at the top of the row axis, the grand total, so dividing by it gives the share of total. The CALCULATE version is model DAX, not a visual calculation. RUNNINGSUM accumulates. PREVIOUS compares with the previous row.",
 code="% of total = ____"),

single("V1",
 "You need the same column chart of monthly sales repeated for each of six regions, in a grid with shared axes. Which feature should you use?",
 ["Small multiples on the column chart, with Region", "Six copies of the chart with visual-level filters", "A matrix", "A drillthrough page"], "A",
 "Small multiples split a visual into a grid of copies, one per value of a field, with consistent axes. Copying the chart six times is harder to maintain. A matrix shows numbers, not charts. Drillthrough shows one region at a time."),

single("V1",
 "A page filter limits the page to the current financial year. Viewers must see that the filter exists but must not be able to change it. What should you do in the Filters pane?",
 ["Lock the filter", "Hide the filter", "Delete the filter", "Convert it to a slicer"], "A",
 "A locked filter is visible to viewers but can't be changed. A hidden filter still applies but isn't shown. Deleting removes the restriction. A slicer is designed to be changed."),

single("V1",
 "Executives want an AI-written text summary of the visuals on a page that updates when they change slicers. What should you add?",
 ["A narrative visual with Copilot", "A text box with typed commentary", "A Q&A visual", "A bookmark navigator"], "A",
 "The narrative visual with Copilot generates a summary of the report's data and refreshes it as filters change. A text box is static. Q&A answers questions users type. A bookmark navigator moves between bookmarks."),

# ---------------- V2 Usability and storytelling (5)
single("V2",
 "A bookmark should apply a set of slicer selections but leave users on whatever page they're viewing when they use it from a bookmark navigator. Which bookmark option should you clear?",
 ["Current page", "Data", "Display", "All visuals"], "A",
 "With Current page cleared, the bookmark applies its captured state without switching to the page where it was created. Data controls filters and slicers, which you need. Display controls visibility. All visuals vs Selected visuals controls scope."),

single("V2",
 "When users select a bar in a column chart, another chart on the page dims the unrelated portions of its bars. They want the other chart to show only the filtered values instead. What should you change?",
 ["Edit interactions: set the chart to Filter", "Add a visual-level filter to the target chart", "Sync the slicers", "Turn off drillthrough"], "A",
 "Edit interactions offers Filter, Highlight and None for each target visual. Highlight dims the parts that don't match. Filter redraws the visual with only matching data. The other options don't change cross-visual behaviour."),

single("V2",
 "A line chart distinguishes Actual and Target only by red and green lines. Some users can't tell them apart. Which change best improves accessibility?",
 ["Distinct line styles or markers, with labels", "Make the lines thicker and the colours brighter", "Change the background to black for more contrast", "Remove the legend"], "A",
 "Accessible design never relies on colour alone: different marker shapes or line styles, plus clear labels, let everyone tell the series apart. Thickness and background don't solve the colour problem. Removing the legend makes it worse."),

single("V2",
 "Users don't know that they can right-click to drill through. You want a visible button that becomes active when a customer is selected and opens the Customer Detail page for that customer. How do you configure the button?",
 ["Set the action type to Drill through", "Set the action type to Bookmark", "Set the action type to Page navigation", "Set the action type to Q&A"], "A",
 "A button with the Drill through action is disabled until a valid selection is made, then opens the destination page filtered to the selection. Page navigation doesn't pass the selection. Bookmarks and Q&A do other things."),

order("V2",
 "Field engineers need a phone-friendly version of the Overview page. Put the steps in order.",
 ["Open the Overview page in Power BI Desktop",
  "Select View → Mobile layout",
  "Drag the four key visuals onto the phone canvas and resize them",
  "Publish the report so the Power BI mobile app uses the layout in portrait mode"],
 "The mobile layout is designed per page from the View ribbon. Visuals are placed on the phone canvas explicitly, then the layout is used by the mobile app after publishing.",
 extra=["Change the page size to 9:16", "Create a dashboard"]),

# ---------------- V3 Patterns and trends (3)
single("V3",
 "A churn analysis needs to find combinations of customer attributes, such as tenure under 6 months on the basic plan in the North region, where churn is much higher than average. Which view should you use?",
 ["Key influencers → Top segments", "Key influencers → Key influencers", "A decomposition tree with no AI splits", "A funnel chart"], "A",
 "Top segments finds groups of attribute combinations where the outcome is unusually likely, and describes their size and rate. The Key influencers tab ranks individual factors. A manual decomposition tree needs the user to guess the splits. A funnel shows stages."),

single("V3",
 "A column chart of delivery times by depot needs a line showing the 90th percentile across depots, so outliers stand out. Where do you add it?",
 ["The Analytics pane: a percentile line set to 90%", "The Format pane: data labels", "The Filters pane: a top N filter", "A calculated column on Depot"], "A",
 "The Analytics pane adds reference lines, including min, max, average, median and percentile lines, which recalculate as the data changes. Data labels and top N filters don't draw a reference line."),

single("V3",
 "You add a forecast to a line chart of monthly sales that peaks every December. The forecast looks flat. Which setting should you change?",
 ["Set the seasonality to 12 points", "Lower the confidence interval to 50%", "Change the line to a column chart", "Turn on data labels"], "A",
 "Seasonality tells the forecast how many points make one cycle. Monthly data with a yearly pattern has a seasonality of 12. The confidence interval only changes the band's width. Visual type and labels don't change the model."),

# ---------------- S1 Workspaces and assets (3 + 1 in case)
single("S1",
 "A data steward wants an email whenever a scheduled refresh of a semantic model fails, even though they don't own the model. What should you configure?",
 ["Refresh failure notifications, with the steward as a contact", "A data alert on a dashboard tile showing the last refresh date", "A subscription to the report", "Sync slicers"], "A",
 "Refresh failure notifications can go to the model owner and to listed contacts. Data alerts react to tile values, and subscriptions send report snapshots. Neither reports on refresh failures."),

single("S1",
 "Content moves through Development, Test and Production stages in a deployment pipeline. Each stage's semantic model must connect to a different SQL database. What should you configure?",
 ["Deployment rules in the Test and Production stages", "A separate .pbix file per stage, each with its own source", "A personal gateway per stage", "Sensitivity labels per stage"], "A",
 "Deployment rules change data sources or parameter values when content is deployed to a stage, so one model definition connects to the correct database in each stage. Separate files defeat the purpose of the pipeline. Gateways and labels don't change connections."),

single("S1",
 "You updated a report in a workspace, but app users still see the old version. What should you do?",
 ["Update the app", "Refresh the semantic model", "Clear the browser cache of each user", "Re-share the report directly"], "A",
 "An app shows a published snapshot of the workspace content. Changes reach app users only when the app is updated. Refreshing data doesn't publish report changes. Re-sharing bypasses the app."),

# ---------------- S2 Secure and govern (4)
single("S2",
 "A developer must add other colleagues to a workspace as Contributors and Viewers, but must not be able to delete the workspace or change its settings. Which role should you assign?",
 ["Member", "Admin", "Contributor", "Viewer"], "A",
 "Members can add people with the Member role or lower, share content and publish the app. Only Admins can delete the workspace and manage all its settings. Contributors and Viewers can't add people to the workspace."),

single("S2",
 "Where do you check, in the Power BI service, what a member of an RLS role will see in a published report?",
 ["Test as role, on the model's Security page", "In the workspace settings", "In the app's audience settings for that role", "In Performance Analyzer"], "A",
 "Test as role on the semantic model's Security page opens the report with that role's filters applied, and you can also test as a specific user. Workspace and app settings don't apply roles. Performance Analyzer is a Desktop timing tool."),

single("S2",
 "Compliance requires that every report published to the service has a sensitivity label. What should you configure?",
 ["A mandatory labelling policy in Microsoft Purview", "A certification process for every published report", "Workspace Viewer roles for all users", "Automatic page refresh"], "A",
 "A mandatory labelling policy makes users apply a label when they save or publish content, so nothing is left unlabelled. Certification is endorsement. Roles control access. Page refresh is unrelated."),

yesno("S2",
 "For each statement about Publish to web, select Yes if it is true.",
 [("Anyone with the link or embed code can view the report, without signing in.", True),
  ("Publish to web respects row-level security, so each viewer sees only their own rows.", False),
  ("A tenant administrator can turn Publish to web off, or limit it to specific users.", True)],
 "Publish to web creates a public, anonymous link, so it's only for non-sensitive content. Reports whose models use RLS can't be published to web. Admins control the feature through a tenant setting and can manage existing embed codes."),

# ---------------- Case study (P2, M2, V1, S1)
case("Woodgrove Bank",
 "Woodgrove Bank's core banking system exports a daily snapshot of every account balance, one row per account per calendar day, as CSV. The balance column is text such as \"12,450.75 CR\" or \"980.10 DR\", where DR means a negative balance. Transactions, Branch and Customer tables are also loaded. The model refreshes at 03:00 through a single on-premises data gateway installed on one server.",
 ["Balances must be numeric, with debit balances negative.",
  "Monthly reports must show each account's balance on the last day of each month, never the sum of daily balances.",
  "Risk managers want each customer's risk rating cell coloured using the colour the risk team stores for that rating.",
  "Last month the gateway server was patched overnight and the refresh failed. Refresh must continue even if one gateway machine is offline."],
 [
  single("P2",
   "How should you convert the balance text?",
   ["Split on the space, type the amount, negate DR amounts", "Change the column type to Decimal Number using a locale", "Use Replace errors with 0", "Use Fill down on the column"], "A",
   "Splitting separates the amount from the CR/DR indicator, the amount can then be typed as a number, and a conditional column applies the sign. Changing the type of the combined text fails with errors. Replacing errors with 0 loses every balance. Fill down doesn't apply."),
  single("M2",
   "Which measure returns the month-end balance?",
   ["CLOSINGBALANCEMONTH ( SUM ( Balances[Amount] ), 'Date'[Date] )", "SUM ( Balances[Amount] )", "TOTALMTD ( SUM ( Balances[Amount] ), 'Date'[Date] )", "AVERAGE ( Balances[Amount] )"], "A",
   "CLOSINGBALANCEMONTH evaluates the expression on the last date of the month. Snapshots exist for every calendar day, so that date always has data. A plain SUM or TOTALMTD adds daily balances together, which overstates the balance. An average is a different metric."),
  single("V1",
   "The risk team keeps a hex colour per rating in the RiskRating table. How should you colour the cells?",
   ["Field value formatting with a measure that returns the hex colour", "Use gradient formatting on the rating", "Create rules-based formatting with one rule per rating, typing each colour", "Apply a report theme"], "A",
   "Formatting by field value uses a measure or column that returns a colour, so the colours come from the risk team's data and change when they change. Typed rules would need editing whenever the colours change. A gradient doesn't use their colours, and a theme isn't per cell."),
  single("S1",
   "How do you make the scheduled refresh resilient to one gateway machine being offline?",
   ["Add a gateway on another server to the same cluster", "Switch to a personal-mode gateway", "Move the refresh to 04:00, when the gateway server is idle", "Give the data steward Admin on the workspace"], "A",
   "A gateway cluster with several members provides high availability: if one machine is unavailable, requests go to another member. A personal gateway is single-user and still one machine. Changing the time or roles doesn't remove the single point of failure."),
 ]),
]
