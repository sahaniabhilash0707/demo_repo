from model import single, multi, yesno, match, order, case

TITLE = "Exam simulation A"
SUBTITLE = "A mixed paper at real exam difficulty: every sub-area, every question format, no theme. Sit it under timed conditions."
LEVEL = "Level 3 · Exam simulation"
CASE_NAME = "Alpine Ski House"

ITEMS = [
# ---------------- P1 Get or connect to data (4)
single("P1",
 "A supplier sends a monthly price list as a PDF containing a formatted table. You need the table in Power BI. Which connector should you use?",
 ["PDF, then pick the table in the Navigator", "Text/CSV, with the delimiter set to a tab", "Web", "Blank query with the table typed in"], "A",
 "The PDF connector detects tables and pages in a PDF and lets you choose one in the Navigator. Text/CSV and Web expect other formats. A blank query would require typing the data."),

single("P1",
 "An Excel workbook is stored in OneDrive for Business. Scheduled refresh in the service must not need a gateway. How should you connect in Power BI Desktop?",
 ["Use the file's OneDrive/SharePoint web URL", "Use the C:\\Users\\…\\OneDrive path with the Excel connector", "Copy the file to a network share", "Email the file to yourself each month"], "A",
 "Connecting through the cloud URL lets the service read the file directly, so no gateway is needed. A local synced path is an on-premises file path in the service's eyes and needs a gateway. Network shares also need one."),

multi("P1",
 "Which two statements about Direct Lake storage mode are true?",
 ["It requires the semantic model to be on Microsoft Fabric capacity", "It reads data from Delta tables in OneLake", "It can connect to any on-premises SQL Server database", "It copies the data into the model on a refresh schedule, like Import", "It works in a Pro workspace on shared capacity"], "AB",
 "Direct Lake is a Fabric capability that loads Delta-Parquet column data from OneLake into memory on demand. Refresh only reframes the model to the latest table version, without copying data. It doesn't connect to arbitrary databases and needs Fabric capacity."),

single("P1",
 "A report is live-connected to a published semantic model. An author wants to add a calculated column. Which statement is correct?",
 ["Only report-level measures can be added, not columns", "Calculated columns can be added freely in a live connection", "Nothing can be added in a live connection", "Calculated columns are added automatically to the shared model"], "A",
 "Live-connected reports have no local model, so only report-level measures are allowed. Adding columns or tables needs either a composite model (Make changes to this model) or a change by the model's owner."),

# ---------------- P2 Profile and clean (3)
single("P2",
 "Refresh fails with \"Expression.Error: The column 'Region' of the table wasn't found\". What has most likely happened?",
 ["A source column was renamed or removed", "The gateway is offline, so the source can't be read", "Region contains null values", "The model has an RLS role on Region"], "A",
 "Power Query steps refer to columns by name. When the source renames or drops a column, the first step that references it fails with this error. Fix the step, or make the query resilient with Choose columns or a rename map. Nulls and RLS don't cause this error."),

single("P2",
 "In an order-lines source, a null Quantity means the line was entered without units. The business says these should be treated as 0. Where and how should you fix this?",
 ["In Power Query, replace null with 0", "In each visual, set Show items with no data", "In DAX, wrap every measure in IF(ISBLANK())", "Delete the rows with a null Quantity"], "A",
 "Applying the business rule once at load means every measure and visual agrees. Fixing it in each measure or visual is repetitive and error-prone. Deleting rows loses data the business wants kept."),

single("P2",
 "A custom column divides Revenue by Units, and rows with zero units produce errors. The column must be null for those rows instead. Complete the custom column formula.",
 ["try [Revenue] / [Units] otherwise null", "if [Units] then [Revenue] / [Units]", "[Revenue] / [Units] ?? null", "Number.From ( [Revenue] / [Units] )"], "A",
 "try … otherwise catches the error raised for each row and returns the fallback value, here null. The if expression is invalid because [Units] isn't a logical value. The ?? operator only replaces null results, not errors. Number.From doesn't handle the error.",
 code="= Table.AddColumn ( Source, \"PricePerUnit\", each ____ )"),

# ---------------- P3 Transform and load (4 + 1 in case)
single("P3",
 "A merge must match supplier names such as \"IBM\" to \"International Business Machines\". The data team keeps a two-column list of known equivalents. What should you use?",
 ["Fuzzy merge with a transformation table", "A Left anti join against the list of equivalents", "Remove duplicates", "Group by supplier name and keep the first row"], "A",
 "A transformation table maps known values to their equivalents during a fuzzy merge, handling cases that similarity alone can't. Anti joins find non-matches. Removing duplicates and grouping don't pair different spellings."),

single("P3",
 "You need an OrderSequence column numbering each customer's orders in date order (1 for their first order, 2 for the second, and so on). What is a correct Power Query approach?",
 ["Sort by OrderDate, group by CustomerID (All rows), and index each group", "Sort by CustomerID and OrderDate, then add one index column to the whole table", "Pivot OrderDate", "Merge the table with itself on OrderDate"], "A",
 "Grouping keeps each customer's rows in a nested table, and an index added inside each table restarts at 1 per customer. A single index column numbers all rows continuously, even after sorting. Pivoting and self-merging don't produce sequences."),

match("P3",
 "Match each query to the load setting it should have.",
 [("Staging query used only as the source of three reference queries", "Clear Enable load"),
  ("Historical archive table, loaded once, whose source never changes", "Clear Include in report refresh"),
  ("Sales fact table refreshed nightly", "Leave Enable load and Include in report refresh on")],
 ["Clear Enable load", "Clear Include in report refresh", "Leave Enable load and Include in report refresh on", "Delete the query"],
 "Staging queries feed other queries, so they don't need to load. A static archive stays in the model but can skip refresh. The fact table needs both settings on. Deleting any of these queries would break the model.",
 left="Query", right="Setting"),

single("P3",
 "A Notes column contains free text, and you need the first ten characters as a ShortNote column, without writing M. Which option should you use?",
 ["Add Column → Extract → First characters (10)", "Split column → By delimiter", "Transform → Trim", "Add Column → Index column"], "A",
 "Extract First characters returns a fixed number of leading characters. Splitting needs a delimiter. Trim only removes spaces. An index column numbers rows."),

# ---------------- M1 Design and implement a model (4)
single("M1",
 "An Employee table has EmployeeID and ManagerID, a parent-child hierarchy of up to four levels. Users want a Level 1 to Level 4 hierarchy in a matrix. What should you do?",
 ["Use PATH and PATHITEM to build Level1–Level4 columns", "Create a many-to-many relationship from Employee to itself", "Set the relationship to Both", "Use a calculation group with one item per level"], "A",
 "Power BI hierarchies need one column per level. PATH flattens the parent-child chain, and PATHITEM extracts each level, which you can then turn into a hierarchy. Self-relationships and calculation groups don't flatten a parent-child structure."),

single("M1",
 "Users must slice customers by the year of their first purchase. Which object should you create in the Customer table?",
 ["A calculated column using CALCULATE ( MIN ( Sales[OrderDate] ) )", "A measure: CALCULATE ( MIN ( Sales[OrderDate] ), ALLEXCEPT ( Sales, Sales[CustomerKey] ) )", "A visual calculation on a table of customers", "A what-if parameter"], "A",
 "Slicers need column values. A calculated column evaluates each customer's first purchase date through context transition, and a year column can be derived from it. A measure can't be placed on a slicer. Visual calculations and what-if parameters don't create customer attributes."),

single("M1",
 "The fiscal year starts in April. Month names in visuals must run April, May … March. What should you do?",
 ["Sort MonthName by a fiscal month number", "Sort MonthName alphabetically", "Sort MonthName by MonthNumber (January = 1)", "Rename the months with numbers"], "A",
 "Sort by column applies the order of another column. A fiscal month number puts April first. Sorting by the calendar month number starts with January. Alphabetical sorting is wrong in both cases."),

yesno("M1",
 "For each statement about calculated tables, select Yes if it is true.",
 [("A calculated table is recalculated whenever the model is refreshed.", True),
  ("A calculated table can be used as the source of a slicer.", True),
  ("A calculated table can have its own incremental refresh policy.", False)],
 "Calculated tables are evaluated from model data after each refresh and behave like any table in visuals, including slicers. Incremental refresh applies to tables loaded through Power Query with RangeStart and RangeEnd, not to DAX tables."),

# ---------------- M2 DAX (5 + 1 in case)
single("M2",
 "You need a cumulative (all-time running) sales total that ends at the last date in the current filter context. Which measure is correct?",
 ["CALCULATE ( [Total Sales], FILTER ( ALL ( 'Date'[Date] ), 'Date'[Date] <= MAX ( 'Date'[Date] ) ) )", "TOTALYTD ( [Total Sales], 'Date'[Date] )", "CALCULATE ( [Total Sales], FILTER ( ALL ( 'Date'[Date] ), 'Date'[Date] <= MIN ( 'Date'[Date] ) ) )", "CALCULATE ( [Total Sales], ALL ( 'Date' ) )"], "A",
 "Removing the date filter and keeping every date up to the current maximum gives an all-time running total. TOTALYTD resets each year. Using MIN ends the total at the first date in the current context rather than the last. ALL('Date') returns the all-time total on every row."),

single("M2",
 "Sales[ProductKey] contains some blanks for unmatched lines. A measure must count the distinct products sold, excluding the blank. Which function should you use?",
 ["DISTINCTCOUNTNOBLANK ( Sales[ProductKey] )", "DISTINCTCOUNT ( Sales[ProductKey] )", "COUNTROWS ( Sales )", "COUNT ( Sales[ProductKey] )"], "A",
 "DISTINCTCOUNT counts a blank as one more distinct value. DISTINCTCOUNTNOBLANK leaves it out. COUNTROWS and COUNT count rows, not distinct products."),

single("M2",
 "A Rates table has one row per Date and Currency, with a Rate column. In the Sales table, a calculated column must fetch the rate for each row's OrderDate and Currency. There is no relationship on both columns. Which expression is correct?",
 ["LOOKUPVALUE ( Rates[Rate], Rates[Date], Sales[OrderDate], Rates[Currency], Sales[Currency] )", "RELATED ( Rates[Rate] )", "LOOKUPVALUE ( Rates[Rate], Rates[Date], MAX ( Sales[OrderDate] ), Rates[Currency], Sales[Currency] )", "VALUES ( Rates[Rate] )"], "A",
 "LOOKUPVALUE returns the value from the row that matches every search condition, which works without a relationship. RELATED needs a relationship. MAX ( Sales[OrderDate] ) returns the latest order date in the table, not the row's own date. VALUES ignores the row's date and currency."),

single("M2",
 "Finance wants the spend of a typical customer, unaffected by a few very large accounts. Which measure fits?",
 ["MEDIANX ( VALUES ( Customer[CustomerKey] ), [Total Sales] )", "AVERAGE ( Sales[Amount] )", "MAXX ( Customer, [Total Sales] )", "SUM ( Sales[Amount] ) / 2"], "A",
 "MEDIANX evaluates each customer's total and returns the middle value, which large outliers barely affect. AVERAGE over lines is skewed by large values and works at the wrong grain. MAXX returns the largest customer."),

match("M2",
 "Match each requirement to the DAX pattern that meets it.",
 [("Revenue computed row by row from Quantity and UnitPrice", "SUMX"),
  ("Highest single-day sales within the selected month", "MAXX over dates"),
  ("Average sales per store", "AVERAGEX over stores"),
  ("Number of stores whose sales beat their target", "COUNTROWS with FILTER")],
 ["SUMX", "MAXX over dates", "AVERAGEX over stores", "COUNTROWS with FILTER", "CONCATENATEX"],
 "Iterators evaluate an expression per row of a table and then aggregate: SUMX adds, MAXX takes the highest and AVERAGEX averages. Counting rows that meet a measure-based condition uses COUNTROWS over a FILTER. CONCATENATEX joins text.",
 left="Requirement", right="Pattern"),

# ---------------- M3 Optimize (2)
single("M3",
 "A 100-million-row Sales table has 12 calculated columns that use RELATED to copy attributes from Product and Customer. The model is large and refresh is slow. What should you do?",
 ["Remove the copied columns", "Add more calculated columns", "Set the Product and Customer relationships to Both", "Switch Product and Customer to DirectQuery storage"], "A",
 "Copying dimension attributes onto a huge fact table duplicates data at the fact's row count. The relationships already let visuals use the dimension columns directly, so removing the copies shrinks the model and speeds up refresh."),

single("M3",
 "Fact and dimension tables are joined on 36-character GUID text keys. What change typically reduces model size and speeds up relationships most?",
 ["Replace the GUIDs with integer surrogate keys", "Convert the GUIDs to uppercase", "Hide the key columns", "Add an index to the GUIDs in DAX"], "A",
 "Long, high-cardinality text keys compress poorly and make joins expensive. Integer surrogate keys are compact and efficient. Changing case or hiding columns doesn't change storage."),

# ---------------- V1 Create reports (5)
single("V1",
 "A visual calculation must use Product[ListPrice], which isn't currently in the matrix. What should you do?",
 ["Add ListPrice to the visual, hidden if needed", "Use RELATED ( Product[ListPrice] ) in the visual calculation", "Create a calculated column", "Visual calculations can reference any model column directly"], "A",
 "Visual calculations can reference only fields that are on the visual, but fields can be added and hidden. RELATED isn't supported in visual calculations. A calculated column doesn't put the value on the visual."),

single("V1",
 "A report needs an automatically generated text summary of key figures, but your organisation has no Fabric or Premium capacity for Copilot. Which visual should you use?",
 ["Smart narrative", "Narrative visual with Copilot", "Q&A with Copilot", "Key influencers"], "A",
 "The smart narrative visual generates text summaries with dynamic values and doesn't require Copilot capacity. The Copilot narrative needs eligible capacity. Key influencers analyses drivers rather than summarising."),

single("V1",
 "Background colour formatting on a matrix's Margin % column must also colour the subtotal and total rows. What should you set in the conditional formatting dialog?",
 ["Apply to: Values and totals", "Apply to: Values only", "Format style: Gradient", "Summarization: Sum"], "A",
 "Conditional formatting has an Apply to option. Values only leaves totals uncoloured, and Values and totals includes subtotals and the grand total. Format style and summarisation don't control that."),

single("V1",
 "A bar chart must show only the ten customers with the highest sales, and stay correct as data changes. What should you configure?",
 ["A visual-level Top N filter by Sales", "A page filter selecting ten customer names", "Sort descending and resize the chart", "A slicer"], "A",
 "A Top N filter keeps the top N items by a measure and re-evaluates as data and other filters change. Hand-picked names go stale. Sorting doesn't limit the items, and a slicer depends on users."),

single("V1",
 "A model has 80 measures with no descriptions, and Copilot gives poor results. You want descriptions added quickly, with the option to review them. What can you use?",
 ["Copilot to draft each measure's description", "Performance Analyzer", "Sync slicers", "DAX query view, with EVALUATE over INFO.MEASURES ()"], "A",
 "Copilot can draft a description for a measure from its formula in the measure's properties, and the author reviews and keeps it. Good descriptions in turn improve Copilot's other results. The other tools don't write descriptions."),

# ---------------- V2 Usability and storytelling (4 + 1 in case)
single("V2",
 "You changed which visuals a bookmark hides, but clicking the bookmark still shows the old state. What should you do?",
 ["Use Update on the bookmark", "Delete the page", "Rename the bookmark to refresh its state", "Sync the slicers"], "A",
 "Bookmarks store a snapshot. After changing the page, use the bookmark's Update command to capture the new state. Renaming doesn't change the stored state."),

single("V2",
 "A button must open the company's SharePoint policy page in a new browser tab. Which action type should you use?",
 ["Web URL", "Page navigation", "Bookmark", "Drill through"], "A",
 "The Web URL action opens an external address. Page navigation, bookmarks and drillthrough only move within Power BI content."),

single("V2",
 "To meet WCAG guidance for normal-size text, what minimum contrast ratio should text have against its background in your report theme?",
 ["4.5:1", "1.5:1", "2:1", "10:1 for every element"], "A",
 "WCAG AA asks for at least 4.5:1 for normal text (3:1 for large text). Lower ratios are hard to read for many users. 10:1 isn't the threshold. Power BI's accessible themes are designed around these ratios."),

yesno("V2",
 "For each statement about drillthrough, select Yes if it is true.",
 [("With Keep all filters on, the target page receives every filter applied to the source visual, not just the drillthrough field.", True),
  ("A hidden page can still be a drillthrough target.", True),
  ("Adding a field to the Drill through well automatically adds a slicer for that field to the page.", False)],
 "Keep all filters passes the full filter context of the source. Hidden pages are often used as drillthrough targets. Power BI adds a Back button, not a slicer, when you set up drillthrough."),

# ---------------- V3 Patterns and trends (3)
single("V3",
 "In a decomposition tree of defect rate, you want Power BI to choose, at the next level, the dimension where the defect rate is lowest. Which split should you use?",
 ["The AI split Low value", "The AI split High value", "A manual split by Plant", "A Top N filter"], "A",
 "AI splits pick the next dimension automatically: High value finds the highest value of the measure, and Low value finds the lowest. A manual split uses the dimension you choose. Top N filters don't drive the tree."),

single("V3",
 "Users type \"big orders\" in Q&A and expect orders over 10,000. Q&A doesn't understand the phrase. What should you do?",
 ["Use Teach Q&A to define \"big orders\"", "Rename the Sales table Big Orders", "Add a smart narrative that explains the term", "Create a bookmark"], "A",
 "Teach Q&A lets you define what a term means, including conditions such as Amount > 10,000, so later questions use it. Renaming tables or adding narratives and bookmarks doesn't teach Q&A new terms."),

single("V3",
 "On a scatter chart of stores, points more than three standard deviations from the mean margin must appear in red. What should you do?",
 ["Colour markers by rule on a z-score measure", "Add a forecast", "Use clustering to group the stores automatically", "Increase the marker size for stores with high margin"], "A",
 "Outliers can be flagged with a measure, such as a z-score using STDEV.P, and highlighted through conditional formatting of the marker colour. Forecasts and marker size don't identify outliers. Clustering groups points rather than flagging extremes."),

# ---------------- S1 Workspaces and assets (3 + 1 in case)
single("S1",
 "The owner of a semantic model has left the company, and refresh credentials can no longer be updated. A workspace Member must now manage the model's settings. What should they do?",
 ["Use Take over on the semantic model's settings page", "Republish the model under a new name", "Delete and recreate the workspace", "Create a new gateway"], "A",
 "Take over makes the current user the model's owner, so they can update credentials, gateway mapping and refresh settings. Republishing under a new name breaks reports. Recreating the workspace or gateway isn't needed."),

single("S1",
 "A Pro workspace model's scheduled refresh stopped running. Nobody has opened its reports or dashboards for over two months. What is the most likely reason?",
 ["Refresh pauses after two months of inactivity", "Pro licences must be renewed by the admin every month", "The gateway was deleted automatically", "The model reached 48 refreshes"], "A",
 "Power BI deactivates refresh schedules for models whose content hasn't been used for about two months. Opening the content or re-enabling the schedule restarts it. Licences, gateways and refresh counts don't explain this pattern."),

single("S1",
 "When you set a data alert on a dashboard card tile, how often can Power BI check the alert condition?",
 ["At most once an hour, or at most once every 24 hours", "Every second", "Only when the report is opened", "Once a week"], "A",
 "Data alerts offer two notification frequencies, at most once an hour or at most once every 24 hours, and evaluate when the tile's data refreshes. Real-time, on-open or weekly options don't exist."),

# ---------------- S2 Secure and govern (4)
single("S2",
 "In a workspace, which role is the least-privileged one that can share items, such as giving another user access to a report, by default?",
 ["Member", "Contributor", "Viewer", "Admin"], "A",
 "Members can share items and add users with the Member role or lower. Contributors can create and edit, but can't reshare by default. Viewers only view. Admin also works but isn't least privilege."),

single("S2",
 "Viewers of a workspace must not see a draft report that's still in development. The draft must stay with the other content during development. What is the best approach?",
 ["Publish an app that excludes the draft", "Hide the draft report's pages", "Apply a sensitivity label to the draft", "Give consumers the Contributor role"], "A",
 "Workspace Viewers see every item in the workspace. An app lets you publish only finished content to consumers. Hidden pages and labels don't hide the report. Contributor access would make it worse."),

multi("S2",
 "Which two Power BI items can have Microsoft Purview sensitivity labels applied?",
 ["Semantic models", "Dashboards", "On-premises data gateways", "Workspace roles", "Capacities"], "AB",
 "Sensitivity labels apply to content items such as reports, dashboards, semantic models, dataflows and paginated reports. Gateways, roles and capacities aren't labelled content."),

single("S2",
 "Users find a certified semantic model in the OneLake catalog but can't open it. Why?",
 ["Certification doesn't grant access to the model", "Certified models are always read-only to everyone", "Certification hides the data", "The model must also be promoted"], "A",
 "Endorsement helps people find and trust content but has no effect on permissions. Access must be granted separately, often through an access request on a discoverable model."),

# ---------------- Case study (P3, M2, V2, S1)
case("Alpine Ski House",
 "Alpine Ski House runs three ski resorts. Lift-ticket sales are stored in an on-premises SQL Server. A Weather table in the same database has a Payload column containing JSON text, such as {\"snowCm\": 35, \"tempC\": -6}. The ski season runs from November to April. The model is in a workspace on a Fabric F64 capacity.",
 ["Snow depth and temperature must be separate numeric columns.",
  "Managers need season-to-date ticket revenue, where each season ends on 30 April.",
  "Hovering over a resort on the map must show a small chart of that resort's snow depth over the last 30 days.",
  "During opening hours (08:00–17:00), the model must refresh every 30 minutes."],
 [
  single("P3",
   "How should you turn Payload into columns?",
   ["Transform → Parse → JSON, then expand the record", "Split Payload by the comma delimiter, then by the colon", "Use Column from examples on Payload", "Unpivot Payload"], "A",
   "Parse JSON turns the text into a record, and expanding the record creates one column per field, which can then be typed. Splitting by comma breaks on nested or reordered JSON. The other options don't parse JSON."),
  single("M2",
   "Which measure returns season-to-date revenue?",
   ["TOTALYTD ( [Ticket Revenue], 'Date'[Date], \"4/30\" )", "TOTALYTD ( [Ticket Revenue], 'Date'[Date] )", "TOTALMTD ( [Ticket Revenue], 'Date'[Date] )", "SAMEPERIODLASTYEAR ( [Ticket Revenue] )"], "A",
   "The year-end-date argument makes the accumulation year end on 30 April, so the year runs 1 May to 30 April and covers each full November–April season. Without it, the year resets in January, mid-season. MTD and SAMEPERIODLASTYEAR answer other questions."),
  single("V2",
   "How do you build the map hover experience?",
   ["A report page tooltip set on the map", "Add snow depth to the map's bubble size", "A drillthrough page with the 30-day snow chart", "A bookmark"], "A",
   "A report page tooltip shows a small custom page, here a trend chart, when users hover over a visual, filtered to the hovered resort. Drillthrough needs a click and navigates away. Size encoding and bookmarks don't show a trend on hover."),
  single("S1",
   "How do you meet the refresh requirement?",
   ["Half-hourly scheduled refresh through a standard gateway", "It isn't possible; the maximum is 8 refreshes a day on any capacity", "Use a personal-mode gateway with 48 refreshes", "Use Publish to web"], "A",
   "On Fabric or Premium capacity, scheduled refresh allows up to 48 slots a day, so 18 half-hourly refreshes fit. The on-premises SQL Server needs a standard gateway. Eight a day is the Pro limit. A personal gateway isn't for shared production refresh."),
 ]),
]
