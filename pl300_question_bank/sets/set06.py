from model import single, multi, yesno, match, order, case

TITLE = "Service, sharing and security"
SUBTITLE = "Gateways, credentials, apps, subscriptions, alerts, roles, RLS and external sharing, alongside the full modelling and reporting outline."
LEVEL = "Level 2 · Core"
CASE_NAME = "Adventure Works Cycles"

ITEMS = [
# ---------------- P1 Get or connect to data (4)
single("P1",
 "Opportunity and account data lives in Dynamics 365 Sales. Which connector is the recommended way to bring it into Power BI?",
 ["Dataverse", "Web", "OData feed to the user's mailbox", "Folder"], "A",
 "Dynamics 365 apps store their data in Dataverse, and the Dataverse connector reads tables, relationships and choice labels directly. Web and Folder are generic connectors, and a mailbox isn't the data source."),

single("P1",
 "A model merges a SQL Server table and a SharePoint list. Both contain internal company data that may safely be combined, and you want folding to work. Which privacy levels should you set?",
 ["Organizational for both sources", "Private for both sources", "Public for the SQL source and Private for SharePoint", "None for both"], "A",
 "Organizational sources can share data with other Organizational sources during evaluation, which allows the merge to fold. Private sources never share data, which blocks folding and can raise firewall errors. Mixing Public with Private restricts the merge as well."),

order("P1",
 "You published a semantic model that imports from an Azure SQL Database, and scheduled refresh fails because no credentials are stored in the service. Put the actions in order to get it refreshing daily.",
 ["Open the semantic model's settings in the workspace",
  "Expand Data source credentials and choose Edit credentials",
  "Choose the authentication method and sign in",
  "Turn on scheduled refresh and set the daily time"],
 "Cloud data source credentials for refresh are stored on the semantic model's settings page. Once they're valid, you can turn on scheduled refresh there. An Azure SQL Database with a public endpoint doesn't need a gateway, and Publish to web has nothing to do with refresh.",
 extra=["Install a personal-mode gateway", "Use Publish to web"]),

single("P1",
 "Your company has an Azure Analysis Services model with all enterprise measures. Report authors must build reports on it without creating a local model. How should they connect?",
 ["Connect live to the Analysis Services model", "Import the model's tables with the SQL Server connector", "Use a dataflow to copy the model", "Use the Excel connector on an exported workbook"], "A",
 "A live connection to Analysis Services uses the model as-is, with no local copy, and report-level measures can still be added. Importing the underlying tables recreates the model outside governance. Dataflows and Excel exports copy data."),

# ---------------- P2 Profile and clean (3)
single("P2",
 "A PaymentType column contains Card, card and CARD. Power Query treats them as three values, and the totals don't reconcile. What is the best fix?",
 ["Apply Format → Capitalize Each Word or Uppercase", "Remove duplicates on PaymentType, keeping the first spelling", "Change the column to Whole Number", "Filter out the lowercase and mixed-case values"], "A",
 "Power Query is case-sensitive, so the three spellings are different values. Standardising the case makes them one. The model's engine compares text without regard to case, which can make results confusing until the source text is consistent. Removing or filtering rows loses data."),

single("P2",
 "Column profile shows negative values in Quantity. The business confirms they are product returns, not errors. Returns must stay in the data but be easy to analyse separately. What should you do?",
 ["Add a conditional column flagging rows with Quantity < 0 as \"Return\"", "Move the negative rows into a separate Returns query that isn't loaded", "Replace negative values with 0 and keep the rows", "Change Quantity to Text"], "A",
 "Resolving an inconsistency doesn't always mean deleting it. The values are valid, so labelling them keeps every row and lets reports split sales and returns. Removing or zeroing them changes the totals."),

single("P2",
 "The automatic Changed Type step detected a ProductCode column as Whole Number because the first rows look numeric. Later rows contain codes such as \"A1023\", which become errors. What should you do?",
 ["Change the column's type to Text", "Remove errors", "Replace errors with 0 after the Changed Type step", "Turn off Column quality"], "A",
 "Type detection looks at a sample of rows, so it guessed wrongly. Codes are identifiers, so the type should be Text, which makes the errors disappear. Removing or replacing errors destroys valid rows."),

# ---------------- P3 Transform and load (4 + 1 in case)
single("P3",
 "You need one row per Region showing total sales and the most recent order date. Which Power Query approach does this in one step?",
 ["Group by Region (Advanced): Sum of Sales, Max of OrderDate", "Group by Region (Basic) with Sum of Sales, then sort by OrderDate", "Pivot Region", "Remove duplicates on Region"], "A",
 "The Advanced option of Group by allows several aggregations, here a sum and a maximum, in one step. Basic allows one aggregation. Pivot and Remove duplicates don't aggregate correctly."),

single("P3",
 "In Power Query, Sales must look up a price from a Price query where the match is on both Region and ProductCode. What should you do?",
 ["Merge on Region and ProductCode, selected in the same order", "Merge on ProductCode only", "Append Price to Sales", "Create two separate merges, one per column, and combine the results"], "A",
 "Merge supports multi-column keys: select the columns in each table (Ctrl-click) in the same order. Matching on one column would return several prices per row. Append stacks rows, which is a different operation."),

multi("P3",
 "A file has these queries: Staging_Customers (referenced by Customers and Contacts), FX_Lookup (used only in a merge into Sales), Sales, Customers and Date. Which two queries should have Enable load cleared?",
 ["Staging_Customers", "FX_Lookup", "Sales", "Customers", "Date"], "AB",
 "Queries that exist only as inputs to other queries don't need to be loaded into the model. Clearing Enable load keeps them out of memory and the field list, and they still run when the queries that use them refresh. Sales, Customers and Date are model tables."),

single("P3",
 "Product codes must be six characters, padded with leading zeros (\"42\" becomes \"000042\"). Complete the custom column formula.",
 ["Text.PadStart ( [Code], 6, \"0\" )", "Text.PadEnd ( [Code], 6, \"0\" )", "Number.Round ( [Code], 6 )", "Text.Start ( [Code], 6 )"], "A",
 "Text.PadStart adds the pad character to the start of the text until it reaches the given length. PadEnd pads at the end. Number.Round works on numbers. Text.Start truncates rather than pads.",
 code="= Table.AddColumn ( Source, \"ProductCode\", each ____ )"),

# ---------------- M1 Design and implement a model (3 + 1 in case)
single("M1",
 "Power BI created a many-to-many relationship between Customer and Sales because CustomerID isn't unique in the Customer table. Investigation shows the duplicates are exact copies of the same customers. What should you do?",
 ["Remove duplicate customers, then make it one-to-many", "Keep the many-to-many relationship and set it to Both", "Delete the relationship", "Use TREATAS in every measure"], "A",
 "A dimension must be unique on its key. Fixing the duplicates at load lets you create the correct one-to-many relationship. Many-to-many relationships cost performance and can give confusing totals when they only hide a data-quality problem."),

single("M1",
 "A Size column has values S, M, L and XL, and visuals sort them alphabetically (L, M, S, XL). What should you do?",
 ["Add a SizeOrder column and sort Size by it", "Rename the values 1-S, 2-M, 3-L and 4-XL", "Sort each visual by a measure that returns 1–4", "Change Size to a number"], "A",
 "Sort by column lets a text column follow the order of another column with one value per text value. Renaming values works but changes what users see. Sorting by a measure doesn't give a fixed category order."),

single("M1",
 "When authors drag UnitPrice into a visual, Power BI sums it, which is meaningless. Authors should get the average by default. What should you change?",
 ["Set UnitPrice's Summarize by property to Average", "Hide UnitPrice", "Change UnitPrice to Text", "Mark UnitPrice as a key column"], "A",
 "The default summarisation decides how a numeric column is aggregated when it's added to a visual. Average suits a price. Authors can still change it per visual, and explicit measures remain the best practice for reusable calculations."),

# ---------------- M2 DAX (6)
single("M2",
 "A matrix shows months on rows. A column must show the full previous year's total sales on every month row. Which filter should the measure use inside CALCULATE?",
 ["PARALLELPERIOD ( 'Date'[Date], -1, YEAR )", "SAMEPERIODLASTYEAR ( 'Date'[Date] )", "DATEADD ( 'Date'[Date], -1, MONTH )", "DATESYTD ( 'Date'[Date] )"], "A",
 "PARALLELPERIOD returns whole periods. Shifting back one year from any month returns all dates of the previous year. SAMEPERIODLASTYEAR returns only the same month last year. DATEADD by a month shifts to the prior month. DATESYTD accumulates the current year."),

single("M2",
 "You need a model measure, usable in any visual, that returns the average of the last three months' monthly sales, ending at the last month in context. Which expression is correct?",
 ["CALCULATE ( AVERAGEX ( VALUES ( 'Date'[YearMonth] ), [Total Sales] ), DATESINPERIOD ( 'Date'[Date], MAX ( 'Date'[Date] ), -3, MONTH ) )", "AVERAGEX ( DATESINPERIOD ( 'Date'[Date], MAX ( 'Date'[Date] ), -3, MONTH ), [Total Sales] )", "MOVINGAVERAGE ( [Total Sales], 3 )", "CALCULATE ( AVERAGEX ( VALUES ( Sales[OrderDateKey] ), [Total Sales] ), DATESINPERIOD ( 'Date'[Date], MAX ( 'Date'[Date] ), -3, MONTH ) )"], "A",
 "The three-month window is applied as a filter, and AVERAGEX then averages the sales of each month in it. Iterating DATESINPERIOD directly averages daily sales, not monthly. MOVINGAVERAGE is a visual calculation function, not a model measure. Iterating the order dates inside the window also averages per day rather than per month."),

single("M2",
 "Products must be ranked by sales against all products, and the ranks must not change when users filter the visual with a slicer. Which expression should you use?",
 ["RANKX ( ALL ( 'Product'[Name] ), [Total Sales] )", "RANKX ( ALLSELECTED ( 'Product'[Name] ), [Total Sales] )", "RANKX ( VALUES ( 'Product'[Name] ), [Total Sales] )", "TOPN ( 1, 'Product', [Total Sales] )"], "A",
 "ALL removes filters from the product names, so each product is ranked against the full list whatever the slicer shows. ALLSELECTED ranks within the user's selection. VALUES ranks within the visual's current context, usually giving every row rank 1. TOPN returns a table."),

single("M2",
 "An analyst who doesn't write DAX needs a running total of sales by date. What is the fastest built-in way to create the measure?",
 ["Use a quick measure (Running total)", "Create a calculated column with SUM over Sales", "Use a visual-level filter", "Turn on Auto date/time"], "A",
 "Quick measures generate the DAX for common patterns, including running totals, from a dialog, and the result is an ordinary measure you can inspect. A calculated column with SUM returns the grand total on every row. Filters and Auto date/time don't create running totals."),

yesno("M2",
 "For each statement about CALCULATE, select Yes if it is true.",
 [("A filter argument on a column replaces any existing filter on that same column.", True),
  ("A filter argument on a dimension column also filters related fact tables through relationships.", True),
  ("A boolean filter argument can reference a measure, for example [Total Sales] > 1000.", False)],
 "CALCULATE replaces filters on the columns it filters, and the new filter propagates through relationships like any other. Boolean filter arguments must compare columns. To filter by a measure, use a table filter such as FILTER over the column's values."),

single("M2",
 "You need a calculated column in Customer that shows how many sales rows each customer has. Product and Customer relate one-to-many to Sales. Which expression is correct?",
 ["COUNTROWS ( RELATEDTABLE ( Sales ) )", "COUNTROWS ( Sales )", "RELATED ( Sales[OrderID] )", "DISTINCTCOUNT ( Customer[CustomerKey] )"], "A",
 "RELATEDTABLE returns the Sales rows related to the current customer row, and COUNTROWS counts them. COUNTROWS(Sales) counts the whole table on every row. RELATED works from the many side to the one side, not the reverse."),

# ---------------- M3 Optimize (2)
single("M3",
 "A sensor table stores temperatures with eight decimal places, so almost every value is unique and the column is large. Reports only need two decimals. What should you do?",
 ["Round to two decimals in Power Query", "Change the column to Text", "Hide the column", "Add a measure that rounds the value to two decimals"], "A",
 "Rounding at load reduces the number of distinct values, which improves compression and shrinks the model. Text is larger. Hiding doesn't change storage. A rounding measure leaves the stored column as large as before."),

multi("M3",
 "Which two actions improve the performance of a DirectQuery report against a well-maintained SQL database?",
 ["Turn on Assume referential integrity on relationships where every fact key exists in the dimension", "Reduce the number of visuals on each page, or add Apply buttons through query reduction", "Set every relationship to Both", "Add complex calculated columns to the DirectQuery tables", "Turn on automatic page refresh every second"], "AB",
 "Inner joins from referential integrity and fewer queries per interaction both reduce load on the source. Bidirectional relationships, complex calculated columns and very frequent page refresh all add queries or complexity."),

# ---------------- V1 Create reports (5)
single("V1",
 "Sales managers want to see how the ranking of the top five products changes from month to month, with the highest-ranked product on top each month. Which visual fits best?",
 ["Ribbon chart", "Pie chart", "Gauge", "Card"], "A",
 "A ribbon chart orders categories by value within each period and connects them with ribbons, so rank changes stand out. Pie charts, gauges and cards don't show rank over time."),

single("V1",
 "A report has a helper page used only as a drillthrough target. It must not appear in the page tabs for readers, but drillthrough must still work. What should you do?",
 ["Hide the page", "Delete the page", "Move the page to another report", "Lock the page"], "A",
 "Hidden pages don't appear in the page navigation for readers, but drillthrough, buttons and bookmarks can still take users there. Deleting it removes the target. Pages can't be locked."),

single("V1",
 "Which tool do you use to author a paginated report (.rdl) for Power BI?",
 ["Power BI Report Builder", "Power BI Desktop's Report view", "Tabular Editor", "Power Query Online"], "A",
 "Paginated reports are authored in Power BI Report Builder and published to the service. Desktop authors interactive reports, Tabular Editor edits models, and Power Query Online is for dataflows and data preparation."),

single("V1",
 "When you open the Copilot pane in Power BI Desktop for the first time, it asks you to select a workspace. Why?",
 ["Copilot needs a workspace on a capacity that supports it", "The report will be published there automatically", "The semantic model will be moved to that workspace to run Copilot", "To choose where personal bookmarks are stored"], "A",
 "In Desktop, Copilot needs a workspace on an eligible capacity (F2 or higher, or P1 or higher) to run against. Choosing the workspace doesn't publish or move anything."),

match("V1",
 "Match each formatting requirement for a table column to the conditional-formatting type that meets it.",
 [("An arrow next to each value shows whether growth is up or down", "Icons"),
  ("Cells are shaded from light to dark as the value increases", "Background colour (gradient)"),
  ("A bar inside each cell is proportional to the value", "Data bars"),
  ("Each value opens a related web page when selected", "Web URL")],
 ["Icons", "Background colour (gradient)", "Data bars", "Web URL", "Font colour (rules)"],
 "Icons add symbols based on rules or a field value. A background gradient shades cells by value. Data bars draw an in-cell bar. Web URL turns a value into a link. Font colour changes the text colour, which none of these requirements ask for.",
 left="Requirement", right="Formatting type"),

# ---------------- V2 Usability and storytelling (5)
single("V2",
 "While arranging a complex page, you keep moving visuals by accident. You want to stop visuals being moved or resized while you work on formatting. What should you do?",
 ["Turn on View → Lock objects", "Group every visual in the Selection pane", "Hide the visuals", "Create a bookmark"], "A",
 "Lock objects stops visuals being moved or resized on the canvas while you keep editing their properties. Grouping, hiding and bookmarking don't prevent accidental moves."),

single("V2",
 "A matrix has Category, Subcategory and Product on rows. Users want to see all levels at once with indentation, instead of drilling one level at a time. What should they do?",
 ["Use Expand all down one level in the hierarchy", "Use drillthrough to a page with a flat table", "Use a bookmark", "Use a report-page tooltip that lists every level"], "A",
 "Expanding all down one level shows the next level for every parent, and repeating it shows all levels in a stepped layout. Drillthrough opens another page. Bookmarks and tooltips don't expand hierarchies."),

single("V2",
 "In a table visual, users want rows sorted by Region and then, within each region, by Sales descending. How do they sort by more than one column?",
 ["Sort by Region, then Shift-click the Sales header", "Create a calculated column combining Region and Sales, and sort by it", "Use Sort by column in the model", "Use a bookmark"], "A",
 "Table visuals support multi-column sorting by holding Shift while selecting additional column headers. Combining columns or changing model sort order doesn't give an on-the-fly secondary sort."),

single("V2",
 "A slide deck for the monthly review must show report pages with data that updates when the deck is opened, not static images. Which export option should you use?",
 ["Export to PowerPoint with Embed live data", "Export to PDF", "Export to PowerPoint as images", "Print to paper"], "A",
 "Embed live data inserts the report into PowerPoint through the Power BI add-in, so the slide shows current, interactive data. PDF and image exports are snapshots."),

yesno("V2",
 "For each statement about Personalize visuals, select Yes if it is true.",
 [("The feature must be enabled in the report's settings before readers can use it.", True),
  ("A change a reader makes is visible to every other user of the report.", False),
  ("Readers can change the visual type, for example from a column chart to a line chart.", True)],
 "Personalize visuals is turned on per report, and can be turned off per visual. Readers' changes are their own and can be saved as personal bookmarks. They can swap measures, dimensions and visual types, without edit permission."),

# ---------------- V3 Patterns and trends (3)
single("V3",
 "The Key influencers visual must explain what drives a numeric outcome, house sale price, rather than a category. Is this supported, and what does the visual show?",
 ["Yes: it shows how each factor moves the average price", "No: Key influencers only supports categorical outcomes", "Yes, but only as a pie chart", "No: you must use a decomposition tree"], "A",
 "Key influencers analyses numeric (continuous) metrics as well as categorical outcomes. For numeric targets, it reports how each factor moves the average of the metric."),

single("V3",
 "A column chart shows product mix by region. North looks different from the others. A user wants Power BI to find where North's distribution differs most. What should they use?",
 ["Analyze → Find where this distribution is different", "Right-click North → Analyze → Explain the increase", "Add a forecast for each region from the Analytics pane", "Group the regions"], "A",
 "Find where this distribution is different compares the selected value's distribution with the rest and highlights the categories that differ most. Explain the increase applies to changes between two data points, for example in a time series."),

single("V3",
 "A line chart of daily output must show horizontal lines at the period's highest and lowest values, updating as filters change. What should you add?",
 ["Max line and Min line from the Analytics pane", "Two constant lines typed manually", "Data labels", "A forecast"], "A",
 "Max and min lines are dynamic: they recalculate for the data in the visual. Constant lines stay where you typed them. Data labels and forecasts don't add reference lines."),

# ---------------- S1 Workspaces and assets (3 + 1 in case)
single("S1",
 "A report author keeps the .pbix file on a SharePoint Online site. Changes saved to the file must reach the published report automatically, without republishing. How should the report be brought into the workspace?",
 ["Upload it from SharePoint in the service", "Publish from Desktop each time the file changes", "Email the file to the workspace", "Use Publish to web with the SharePoint file's link"], "A",
 "Uploading from OneDrive or SharePoint creates a connection to the file, and the service picks up saved changes automatically. Publishing from Desktop works but must be repeated. The other options don't keep the report in sync."),

single("S1",
 "After publishing a model that imports from an on-premises SQL Server, the settings page shows the gateway connection isn't configured, so refresh can't be scheduled. A gateway is installed and running. What should you do?",
 ["Map the source to a gateway connection for the server", "Install a personal gateway on your laptop and sign in to it", "Switch the model to DirectQuery so no gateway is needed", "Republish the model from Desktop with credentials saved"], "A",
 "The model's on-premises source must be mapped to a gateway connection for that server and database, created by a gateway admin, with credentials. A personal gateway isn't for shared production refresh. Switching modes or republishing doesn't create the mapping."),

single("S1",
 "A manager sets a data alert on a dashboard tile and expects her whole team to be notified, but only she receives the email. Why?",
 ["Data alerts are personal: only their creator is notified", "Alerts work only on report visuals", "The team needs the Admin role on the dashboard's workspace", "The tile must be a pie chart"], "A",
 "Each data alert belongs to the user who created it, and only that user is notified. An alert can trigger a Power Automate flow to notify others. Alerts are set on dashboard tiles like cards, KPIs and gauges, not on pie charts."),

# ---------------- S2 Secure and govern (3 + 1 in case)
single("S2",
 "A report developer must publish reports from Power BI Desktop to a workspace and edit content there. They must not manage access or publish the app. Which role meets this with least privilege?",
 ["Contributor", "Member", "Admin", "Viewer"], "A",
 "Contributors can publish, create, edit and delete content, and schedule refresh, but can't add users or, by default, update the app. Member and Admin grant more. Viewer can't publish."),

single("S2",
 "An external auditing firm must view three reports using their own company credentials, with access you can revoke. What should you do?",
 ["Invite them as Entra B2B guests and share the reports", "Use Publish to web", "Create Power BI accounts in your tenant with shared passwords", "Email them PDF exports of the three reports each month"], "A",
 "B2B guest access lets external users sign in with their own identity while you control and revoke their permissions. Publish to web is public. Shared accounts break accountability. PDF emails can't be revoked once sent."),

single("S2",
 "A report with the Highly Confidential label, configured with encryption, is exported to Excel. What happens to the exported file?",
 ["It keeps the label and its protection", "The label is removed during export", "The export is always blocked for encrypted labels", "The file is converted to PDF"], "A",
 "Sensitivity labels persist to supported export formats, and a label with encryption protects the file outside Power BI. Labels don't block export by themselves. Export settings and tenant settings control that."),

# ---------------- Case study (P3, M1, S1, S2)
case("Adventure Works Cycles",
 "Adventure Works sells bicycles through 300 independent dealers. Web orders arrive as JSON with an OrderTimestamp field holding Unix epoch seconds. Each dealer can belong to several sales territories, and each territory has many dealers. Dealers are external companies whose staff sign in as Microsoft Entra B2B guests.",
 ["Order dates must be real date/time values in the model.",
  "Sales must be analysable by territory, even though dealers belong to several territories.",
  "Each dealer's purchasing contact wants a PDF of the whole Dealer report emailed every Monday.",
  "Each dealer must see only their own sales rows. A DealerUsers table maps guest email addresses to DealerID."],
 [
  single("P3",
   "Which custom column formula converts OrderTimestamp to a datetime?",
   ["#datetime ( 1970, 1, 1, 0, 0, 0 ) + #duration ( 0, 0, 0, [OrderTimestamp] )", "DateTime.From ( [OrderTimestamp] )", "Date.From ( Text.From ( [OrderTimestamp] ) )", "#date ( [OrderTimestamp], 1, 1 )"], "A",
   "Unix time counts seconds from 1 January 1970, so adding a duration of that many seconds to the epoch gives the datetime. DateTime.From on a number treats it as days since 1899, which gives wrong dates. The other expressions produce invalid or wrong values."),
  single("M1",
   "How should you model dealers and territories?",
   ["Add a DealerTerritory bridge, with bridge–Dealer filtering set to Both", "Add a TerritoryID column to Dealer and keep only the first territory", "Relate Territory directly to Sales with a many-to-many relationship on DealerID", "Merge Territory into Sales"], "A",
   "A bridge table resolves the many-to-many relationship between dealers and territories. Letting the bridge filter Dealer passes the territory selection through to Sales. Keeping only one territory loses data. Direct many-to-many or merging duplicates sales across territories in uncontrolled ways."),
  single("S1",
   "How do you deliver the Monday PDF to each dealer contact?",
   ["A weekly subscription with the report attached as PDF", "Set a data alert that emails the PDF to every dealer contact on Mondays", "Use Export to PowerPoint", "Use Publish to web"], "A",
   "Report subscriptions can attach the full report as a PDF (or PowerPoint) on a schedule, and recipients still only see data their access allows. Data alerts trigger on thresholds. Manual export doesn't schedule. Publish to web is public."),
  single("S2",
   "Which role filter, on the Dealer table, meets the security requirement?",
   ["Dealer[DealerID] IN CALCULATETABLE ( VALUES ( DealerUsers[DealerID] ), DealerUsers[Email] = USERPRINCIPALNAME () )", "Dealer[DealerID] = USERNAME ()", "Dealer[DealerID] = CUSTOMDATA ()", "TRUE ()"], "A",
   "USERPRINCIPALNAME() returns the signed-in user's sign-in name. Looking it up in the mapping table returns that user's DealerIDs, which then filter Dealer and, through it, Sales. A DealerID never equals a user name. CUSTOMDATA is for embedded scenarios. TRUE() shows everything."),
 ]),
]
