from model import single, multi, yesno, match, order, case

TITLE = "Modelling and relationships"
SUBTITLE = "Cardinality, filter direction, role-playing and snowflaked dimensions, virtual relationships and the filter-modifier functions."
LEVEL = "Level 2 · Core"
CASE_NAME = "Fabrikam Manufacturing"

ITEMS = [
# ---------------- P1 Get or connect to data (3 + 1 in case)
multi("P1",
 "A semantic model will refresh on a schedule in the Power BI service. Which two of its sources require an on-premises data gateway?",
 ["A SQL Server database in the company data centre", "Excel files on a network file share (\\\\fileserver\\finance)", "A SharePoint Online document library", "An Azure SQL Database reachable over a public endpoint", "A OneDrive for Business folder"], "AB",
 "Anything on the private network, such as an on-premises database or a UNC file share, is reached through a gateway. SharePoint Online, OneDrive and a publicly reachable Azure SQL Database are cloud sources the service can reach directly."),

single("P1",
 "An Excel workbook contains a formatted table named tblSales on Sheet1. Users sometimes add notes below the table. In the Navigator, which object should you select?",
 ["Sheet1", "tblSales", "Both, then append them", "The workbook's named range Print_Area"], "B",
 "Selecting the table object returns exactly the table's rows and columns, however the sheet around it changes. Selecting the sheet returns every used cell, including the notes, and breaks when the layout changes."),

single("P1",
 "A Power BI Desktop file combines two sources you fully trust. Combining them is slow because privacy checks stop query folding. Where can you tell Power BI to ignore privacy levels for this file?",
 ["File → Options and settings → Options → Current file → Privacy", "Data source settings → Edit Permissions → Credentials", "Transform data → Query properties", "Model view → Table properties"], "A",
 "The Current file privacy option can be set to ignore privacy levels, which may improve performance. Use it only when every source can safely be combined. Credentials, query properties and table properties don't control privacy evaluation."),

# ---------------- P2 Profile and clean (3)
single("P2",
 "You need the minimum, maximum, average and standard deviation of a Quantity column, plus its most frequent values. Which Power Query feature shows these together?",
 ["Column profile", "Column quality", "Column distribution", "Query dependencies"], "A",
 "Column profile shows column statistics (count, errors, empty, distinct, unique, min, max, average, standard deviation and more) and a value distribution chart for the selected column. Column quality and distribution show summaries in the header area only."),

single("P2",
 "In an exported report, the section name appears only on the last row of each block of rows, and the rows above it are null. Which transformation fills the nulls correctly?",
 ["Fill down", "Fill up", "Replace errors", "Transpose"], "B",
 "Fill up copies a value upward into the null cells above it, which is what you need when the label is on the last row of each block. Fill down copies downward, for labels on the first row. Replace errors and Transpose don't fill gaps."),

single("P2",
 "A Country column contains about 40 spellings of the same countries (US, U.S., USA, United States…). The business maintains a list of correct names. What is the most maintainable fix?",
 ["Add a Replace values step for each of the 40 spellings", "Merge a mapping table of variant and correct names", "Use Capitalize Each Word, then Trim and Clean", "Remove duplicates on Country"], "B",
 "A mapping table puts the rules in data the business can maintain, and one merge applies them all. Dozens of Replace values steps are hard to maintain. Changing case or removing duplicates doesn't standardise spellings."),

# ---------------- P3 Transform and load (5)
order("P3",
 "A query has columns Product, Attribute and Value, with Attribute holding Colour, Size and Weight. You need one column per attribute and one row per product, without summing anything. Put the actions in order.",
 ["Select the Attribute column",
  "Choose Transform → Pivot column",
  "Choose Value as the values column",
  "Under Advanced options, set the aggregation to Don't aggregate"],
 "Pivot turns the values of the selected column into new column headers. The values column supplies the cell contents. Don't aggregate is needed because the values are text and there is one value per product and attribute.",
 extra=["Choose Unpivot other columns", "Promote the first row to headers"]),

single("P3",
 "A file has 30 queries, and you need to see which queries feed which, and which are loaded to the model. Which Power Query feature shows this?",
 ["View → Query dependencies", "View → Column profile", "Home → Manage parameters", "Model view"], "A",
 "Query dependencies shows a diagram of every query, its sources and the queries that reference it, and indicates which are loaded. Column profile describes one column. Manage parameters lists parameters. Model view shows relationships between loaded tables, not query lineage."),

single("P3",
 "A FullName column holds values like \"Sahani, Abhilash Kumar\". You need LastName and FirstNames columns, splitting only at the first comma. Which option should you use?",
 ["Split column → By delimiter, comma, at the left-most delimiter", "Split column → By delimiter, comma, at each occurrence", "Split column → By number of characters", "Extract → Last characters"], "A",
 "Splitting at the left-most delimiter produces exactly two columns: the text before the first comma and everything after it. Splitting at each occurrence would create extra columns if there were more commas. Fixed-width splits don't work for names of different lengths."),

single("P3",
 "A Price column is detected as Decimal Number. Totals over millions of rows show tiny rounding differences against the finance system, which stores four decimal places. Which data type should you use?",
 ["Fixed decimal number", "Whole number", "Text", "Percentage"], "A",
 "Fixed decimal number (currency) stores four decimal places exactly, which avoids floating-point rounding in totals. Whole number loses the decimals. Text can't be summed. Percentage is a format, not a precision fix."),

single("P3",
 "The source view keeps gaining new columns, but the model must only ever load six specific columns. Which step keeps the query stable when new columns appear?",
 ["Choose columns (Remove other columns)", "Remove columns, selecting the ones you don't need", "Promote headers", "Change type on all columns"], "A",
 "Choose columns, or Remove other columns, records the columns to keep, so new source columns are ignored automatically. Remove columns records the columns to drop, so any new column would flow into the model."),

# ---------------- M1 Design and implement a model (3 + 1 in case)
single("M1",
 "Product filters Sales, and Customer filters Sales, both one-to-many in a single direction. A measure COUNTROWS(Customer) returns the same value for every product colour. You must count customers who bought each colour, without changing the relationship for the rest of the model. What should you do?",
 ["Set the Customer–Sales relationship's cross-filter direction to Both in the model", "Use CROSSFILTER with BOTH on that relationship inside the measure's CALCULATE", "Create a many-to-many relationship between Product and Customer", "Merge Customer into Product"], "B",
 "CROSSFILTER changes the filter direction only while that measure is evaluated, so Sales can filter Customer for this calculation alone. Setting the relationship to Both affects every visual and can create ambiguity. (Counting distinct Sales[CustomerKey] is another valid approach.)"),

single("M1",
 "Customer and CustomerDetails share CustomerID with exactly one row each per customer, and they're related one-to-one. Reports always use both. What is the recommended change?",
 ["Keep the one-to-one relationship and set it to Both", "Merge CustomerDetails into Customer in Power Query", "Create a many-to-many relationship", "Hide CustomerDetails"], "B",
 "A one-to-one relationship between two tables describing the same entity usually means they should be one table. Merging them simplifies the model and removes a relationship. The other options keep the unnecessary split."),

yesno("M1",
 "For each statement about the Assume referential integrity relationship property, select Yes if it is true.",
 [("It is available on relationships between DirectQuery tables from the same source.", True),
  ("It makes Power BI generate inner joins instead of outer joins in the SQL it sends.", True),
  ("Turning it on is safe even when the fact contains keys that aren't in the dimension.", False)],
 "Assume referential integrity applies to DirectQuery and lets the engine use inner joins, which are faster. If the fact has keys missing from the dimension, those rows silently disappear from results, so only use it when integrity is guaranteed."),

# ---------------- M2 DAX (5 + 1 in case)
match("M2",
 "Match each requirement to the DAX function you would use inside CALCULATE.",
 [("Percent of the grand total, ignoring every slicer on Product", "REMOVEFILTERS"),
  ("Percent of the total of the products the user has selected in the slicer", "ALLSELECTED"),
  ("Red-product sales that still respect a Colour slicer (blank when another colour is chosen)", "KEEPFILTERS")],
 ["REMOVEFILTERS", "ALLSELECTED", "KEEPFILTERS", "VALUES", "RELATEDTABLE"],
 "REMOVEFILTERS clears filters, as ALL does when used as a modifier. ALLSELECTED restores the selection made outside the visual, so totals match what the user selected. KEEPFILTERS intersects a new filter with the existing one instead of replacing it. VALUES and RELATEDTABLE return tables but don't change filter behaviour like this.",
 left="Requirement", right="Function"),

single("M2",
 "You need a calculated column in Sales that holds the list price from the related Product table (Product to Sales is one-to-many). Which expression should you use?",
 ["RELATED ( 'Product'[ListPrice] )", "RELATEDTABLE ( 'Product' )", "LOOKUPVALUE ( 'Product'[ListPrice] )", "VALUES ( 'Product'[ListPrice] )"], "A",
 "In a row context on the many side, RELATED follows the relationship to the one side and returns the single related value. RELATEDTABLE goes the other way and returns a table. LOOKUPVALUE needs search arguments. VALUES returns a column of values, not the related one."),

single("M2",
 "Balances has one row per account per day. You need the average daily balance across the dates in the current selection, where [Balance] sums the balance for a day. Which measure is correct?",
 ["AVERAGEX ( VALUES ( 'Date'[Date] ), [Balance] )", "AVERAGE ( Balances[Amount] )", "SUM ( Balances[Amount] ) / 365", "AVERAGEX ( Balances, Balances[Amount] )"], "A",
 "Balances are semi-additive: they mustn't be summed over time. AVERAGEX over the selected dates evaluates the daily total for each date, then averages those totals. AVERAGE over rows averages individual account rows, not daily totals. Dividing by 365 assumes a full year is selected."),

single("M2",
 "A Targets table has a MonthStart column but no relationship to the Date table, and you can't add one. A measure must return targets for the months selected through the Date table. Which expression should you use?",
 ["CALCULATE ( SUM ( Targets[Amount] ), TREATAS ( VALUES ( 'Date'[MonthStart] ), Targets[MonthStart] ) )", "SUM ( Targets[Amount] )", "CALCULATE ( SUM ( Targets[Amount] ), ALL ( 'Date' ) )", "CALCULATE ( SUM ( Targets[Amount] ), USERELATIONSHIP ( 'Date'[MonthStart], Targets[MonthStart] ) )"], "A",
 "TREATAS applies the values selected in Date[MonthStart] as a filter on Targets[MonthStart]. That's a virtual relationship for this measure. A plain SUM ignores the date selection. ALL removes the filter. USERELATIONSHIP only activates an existing inactive relationship, and there isn't one."),

single("M2",
 "In a matrix with Category and Product on the rows, a measure must show values on product rows but blank on category subtotals and the grand total. Which pattern works?",
 ["IF ( ISINSCOPE ( 'Product'[Product] ), [Total Sales] )", "IF ( HASONEVALUE ( 'Product'[Category] ), [Total Sales] )", "IF ( ISBLANK ( [Total Sales] ), BLANK () )", "SELECTEDVALUE ( 'Product'[Product] )"], "A",
 "ISINSCOPE returns TRUE only when the Product level is being grouped, so subtotals and totals return blank. HASONEVALUE on Category is also true on product rows and on the category subtotal. ISBLANK doesn't detect the level. SELECTEDVALUE returns a name, not the measure."),

# ---------------- M3 Optimize (2)
single("M3",
 "Performance Analyzer shows that most visuals on a page have a short DAX query time but a long Other time. What does this usually mean, and what helps?",
 ["Visuals wait on other visuals, so use fewer visuals", "The DAX measures are slow, so rewrite them with variables", "The custom theme is too complex, so revert to the default", "The model needs more relationships"], "A",
 "Other is time spent waiting, mostly for other visuals' queries or background work. A page with many visuals queues them. Reducing or combining visuals helps. Slow measures show as DAX query time instead."),

single("M3",
 "A DirectQuery report sends a query to the source each time a user changes any of six slicers, which overloads the database. Users don't mind clicking once when they've finished choosing. What should you configure?",
 ["Query reduction: add Apply buttons to slicers", "Turn on automatic page refresh", "Switch the slicers to dropdown style so fewer queries run", "Turn on Auto date/time"], "A",
 "The query-reduction options in Options can add Apply buttons to slicers and to the filter pane, so queries are sent only when the user applies their choices. Page refresh would add queries. Slicer style and Auto date/time don't reduce queries."),

# ---------------- V1 Create reports (5)
single("V1",
 "A matrix shows monthly sales. You need a column showing the change from the previous month, defined only on this visual, with no new model measure. Which visual calculation should you write?",
 ["[Sales] - PREVIOUS ( [Sales] )", "[Sales] - CALCULATE ( [Sales], PREVIOUSMONTH ( 'Date'[Date] ) )", "RUNNINGSUM ( [Sales] )", "[Sales] - SAMEPERIODLASTYEAR ( [Sales] )"], "A",
 "Visual calculations work on the data in the visual. PREVIOUS returns the value from the previous row along the axis, so the difference is the month-on-month change. PREVIOUSMONTH inside CALCULATE is model DAX, which the requirement rules out. RUNNINGSUM accumulates rather than compares. SAMEPERIODLASTYEAR doesn't take a measure."),

single("V1",
 "An analyst wants to see whether marketing spend and revenue move together across 200 stores. Which visual is most appropriate?",
 ["Scatter chart with one point per store", "Stacked column chart of spend and revenue by store", "Donut chart of revenue by store", "Card"], "A",
 "A scatter chart plots two measures against each other, one point per store, so correlation and outliers are visible. Column, donut and card visuals show values by category or a single value, not a relationship between two measures."),

single("V1",
 "In a table of stores, the Revenue column must show a horizontal bar in each cell proportional to the value. What should you apply?",
 ["Conditional formatting → Data bars", "Conditional formatting → Icons", "Conditional formatting → Web URL", "A KPI visual"], "A",
 "Data bars draw a bar in the cell scaled to the value, which makes magnitudes easy to compare. Icons show symbols based on rules. Web URL turns a value into a link. A KPI visual is a separate visual."),

single("V1",
 "Which requirement points to a Power BI report rather than a paginated report?",
 ["Users must click a bar and have every other visual cross-filter", "A 200-page statement must print with page numbers", "An invoice layout must match a pre-printed form exactly", "A list of 80,000 rows must export to Excel in one go"], "A",
 "Interactive cross-filtering and exploration is what Power BI reports are for. Long printable documents, pixel-perfect forms and exporting very large tables are classic paginated-report requirements."),

multi("V1",
 "You want to use Copilot in Power BI to suggest content for a new report page. Which two conditions must be met?",
 ["The tenant setting that allows users to use Copilot and other Azure OpenAI features is enabled", "The report is in a workspace on a paid Fabric capacity (F2 or higher) or Premium P1 or higher", "The semantic model uses DirectQuery", "Every viewer has a Fabric trial", "The report has been published to the web"], "AB",
 "Copilot needs the tenant setting enabled and a workspace on supported paid capacity. Storage mode doesn't matter, trial capacities aren't supported, and Publish to web is unrelated (and public)."),

# ---------------- V2 Usability and storytelling (5)
single("V2",
 "A report reader personalised a chart to show Profit by Channel instead of Revenue by Region, and wants to come back to that view later. What should they do?",
 ["Save it as a personal bookmark", "Ask the author to save the report", "Export the chart to PowerPoint", "Pin the chart to a dashboard"], "A",
 "Personalised visuals can be kept by saving a personal bookmark, which belongs to that reader only. The author's saved report doesn't include a reader's personalisation. Exporting or pinning creates a copy elsewhere, not a reusable view in the report."),

single("V2",
 "Keyboard users report that tabbing moves around the page in a confusing order and stops on decorative shapes. What should you fix?",
 ["The tab order in the Selection pane", "The page size and canvas alignment", "The report theme colours", "The visual interactions in Edit interactions mode"], "A",
 "The Selection pane has a Tab order view where you set the sequence and can stop decorative objects receiving focus. That's a core accessibility setting. Page size, colours and interactions don't control keyboard navigation."),

order("V2",
 "Users of a Sales report must right-click a customer and open a Customer Detail page that lives in a separate report. Put the required steps in order.",
 ["In the Customer Detail report, add Customer to the drillthrough well and set Cross-report to On",
  "In the Sales report's options, allow visuals to use drillthrough targets from other reports",
  "Publish both reports to the same workspace",
  "In the Sales report in the service, right-click a customer and choose Drill through"],
 "Cross-report drillthrough needs the target page set as a cross-report target, the source report allowed to use such targets, and both reports in the same workspace. Then the option appears in the right-click menu.",
 extra=["Create a bookmark in the Sales report", "Pin the detail page to a dashboard"]),

single("V2",
 "A report has 12 pages and gets new pages often. You need a row of navigation buttons, one per page, that updates automatically when pages are added or hidden. What should you insert?",
 ["A page navigator", "A bookmark navigator", "Twelve blank buttons with page navigation actions", "A drillthrough button"], "A",
 "The page navigator creates one button per page and stays in sync as pages are added, renamed or hidden. A bookmark navigator lists bookmarks. Individual buttons must be maintained by hand. Drillthrough is contextual navigation, not a page menu."),

single("V2",
 "A DirectQuery report in a Pro workspace (shared capacity) must refresh its visuals every 5 minutes. Automatic page refresh won't accept 5 minutes. What is required?",
 ["Move the workspace to Premium or Fabric capacity", "Change the report to Import", "Create a dashboard tile", "Increase the scheduled refresh count to 48 per day"], "A",
 "In shared capacity, automatic page refresh has a 30-minute minimum. On Premium or Fabric capacity, the capacity admin sets the minimum, which can be much lower. Import mode doesn't use automatic page refresh for new data. Scheduled refresh is a different feature."),

# ---------------- V3 Patterns and trends (3)
single("V3",
 "A line chart shows monthly demand estimates. Each estimate has a low and a high value in the model. You want the chart to show this range around each point. What should you add?",
 ["Error bars using the bound fields", "A median line", "A forecast with a confidence interval", "A constant line"], "A",
 "Error bars draw a range around each data point from upper and lower bound fields. A median line, constant line or forecast doesn't show the per-point range."),

single("V3",
 "A slicer lists 30 product subcategories. Five low-volume subcategories must appear together as \"Other\". Users must not need a new column in the source. What should you use?",
 ["Groups (Group data) on the subcategory field", "Bins on the subcategory field", "Clustering", "A top N filter"], "A",
 "Grouping combines selected category values into a named group in the model, with the rest kept as they are, or as Other. Bins are for numeric and date ranges. Clustering finds groups on a scatter chart. A top N filter hides values rather than combining them."),

single("V3",
 "A new analyst wants a quick plain-language overview of what a published semantic model contains: its tables, key measures and what it can answer. What can they use?",
 ["Copilot, asked to summarise the model", "Performance Analyzer", "Query dependencies view in Power Query", "The Analytics pane"], "A",
 "Summarising the underlying semantic model is one of the Copilot tasks in the outline. It describes the model in plain language from its metadata. Performance Analyzer measures speed, query dependencies is a Power Query view, and the Analytics pane adds lines to visuals."),

# ---------------- S1 Workspaces and assets (4)
single("S1",
 "Five hundred employees with free licences must view reports. The company doesn't want to buy Pro licences for them. What is required?",
 ["An F64 (or P1) or larger capacity, shared through an app", "Give them the Viewer role in a Pro workspace, through an app", "Use Publish to web", "Email them PDF exports"], "A",
 "Free users can view content in workspaces on F64 or P1 and larger capacities. In a Pro workspace, every viewer needs a Pro (or PPU) licence, whatever their role. Publish to web exposes the content publicly, and PDF emails lose interactivity."),

single("S1",
 "You publish Sales.pbix to a workspace that already contains a report and semantic model called Sales. What happens when you confirm Replace?",
 ["Both the report and the semantic model are replaced", "Only the report is replaced", "A second report and model named Sales (1) are created", "Only the model's data is refreshed"], "A",
 "Publishing a .pbix with the same name replaces both the existing report and its semantic model. Settings such as scheduled refresh and credentials are kept, but the model definition and data come from the file."),

match("S1",
 "Match each sharing scenario to the most appropriate distribution method.",
 [("A whole department needs a curated set of reports, kept separate from work in progress", "Workspace app"),
  ("One colleague needs to see one report today", "Direct share of the report"),
  ("Reports must appear on the intranet's SharePoint Online page, respecting each user's permissions", "Embed in SharePoint Online"),
  ("Non-sensitive public statistics must appear on a public website", "Publish to web")],
 ["Workspace app", "Direct share of the report", "Embed in SharePoint Online", "Publish to web", "Workspace Admin role"],
 "Apps are for curated, scalable distribution. Direct share suits one-off access. The SharePoint Online web part embeds reports securely, so users still need permission. Publish to web is public and only for non-sensitive data. Admin is a management role, not a way to distribute content.",
 left="Scenario", right="Method"),

single("S1",
 "You want only the Data Governance team to be able to certify content. What must happen first?",
 ["A Fabric admin enables certification for that team's group", "Each workspace Admin enables certification in workspace settings", "The Data Governance team is given Contributor in every workspace", "Content is labelled Highly Confidential"], "A",
 "Certification is controlled by a tenant setting in the admin portal, which also defines who can certify. Workspace roles don't grant the right to certify, and sensitivity labels are unrelated to endorsement."),

# ---------------- S2 Secure and govern (3 + 1 in case)
yesno("S2",
 "A semantic model has RLS. For each statement, select Yes if it is true.",
 [("RLS applies to a user who has Build permission and creates a report in their own workspace.", True),
  ("RLS applies to workspace Members of the model's workspace.", False),
  ("A user who belongs to two roles sees the rows allowed by either role.", True)],
 "RLS applies to users who only read the model, including Build users querying it from elsewhere. Workspace Admins, Members and Contributors have edit rights and bypass it. Role membership is additive, so a user in two roles sees the union of the rows each role allows."),

single("S2",
 "Each manager must see their own sales and the sales of everyone who reports to them, at any depth. An Employee table has EmployeeID, ManagerID and Email. What should the role use?",
 ["PATH and PATHCONTAINS with the signed-in user's EmployeeID", "One static role per manager, listing each team member", "Employee[Email] = USERPRINCIPALNAME() on the Employee table", "A many-to-many relationship between Employee and Sales"], "A",
 "PATH creates a delimited list of each employee's management chain. PATHCONTAINS tests whether the signed-in manager's ID appears in that chain, so all descendants are visible. Matching only the email shows the manager's own rows. Static roles don't scale."),

single("S2",
 "A Highly Confidential label is applied to a semantic model. Report authors create new reports from it. With label inheritance from data sources and semantic models enabled, what happens?",
 ["New reports inherit the Highly Confidential label", "The label is removed from the model when a report is created", "Report authors lose Build permission", "Exports from the reports are blocked"], "A",
 "Downstream inheritance applies the label of the semantic model to content created from it, so classification flows with the data. Labels don't change permissions. Exported files carry the label, with whatever protection it defines."),

# ---------------- Case study (P1, M1, M2, S2)
case("Fabrikam Manufacturing",
 "Fabrikam has four plants. Machine sensor readings (about 3 billion rows) are loaded every 15 minutes into Delta tables in a Microsoft Fabric lakehouse. Production orders are in Azure SQL Database. Quality inspections record inspected and defective units per batch. The model currently has Machine related to Plant, and Plant related to Region, as separate tables. Several managers run more than one plant.",
 ["Sensor reports must show data within minutes of each load, with Import-like performance, without copying the data into the model.",
  "Report authors find the Machine → Plant → Region chain confusing, and filtering by region is slow.",
  "A Defect Rate measure must divide defective units by inspected units and show blank where nothing was inspected.",
  "Plant managers must see only the plants they manage, including managers with more than one plant."],
 [
  single("P1",
   "Which storage mode should you use for the sensor fact table?",
   ["Direct Lake", "Import with scheduled refresh 48 times a day", "DirectQuery to the SQL analytics endpoint", "Dual"], "A",
   "Direct Lake reads the Delta tables in OneLake directly with Import-like speed and no data copy. A refresh only reframes the model to the latest table version. Import copies 3 billion rows. DirectQuery would be slower. Dual is for dimensions in composite models."),
  single("M1",
   "How should you fix the Machine → Plant → Region chain?",
   ["Merge Plant and Region into the Machine table in Power Query", "Set every relationship in the chain to Both for faster filtering", "Add a direct relationship from Region to the fact table", "Hide the Plant and Region tables"], "A",
   "Flattening a snowflaked dimension into one table makes the model simpler for authors and removes relationship hops. Bidirectional filters add ambiguity. A second path to the fact creates an ambiguous model. Hiding tables removes the attributes authors need."),
  single("M2",
   "Complete the Defect Rate measure.",
   ["DIVIDE ( SUM ( Inspections[Defective] ), SUM ( Inspections[Inspected] ) )", "SUM ( Inspections[Defective] ) / SUM ( Inspections[Inspected] )", "AVERAGE ( Inspections[Defective] )", "DIVIDE ( Inspections[Defective], Inspections[Inspected] )"], "A",
   "DIVIDE returns blank when the denominator is zero, which meets the requirement. The / operator returns an error or infinity. AVERAGE of defects isn't a rate. DIVIDE needs scalar expressions, so passing columns without aggregating fails in a measure.",
   code="Defect Rate = ____"),
  single("S2",
   "Which design meets the plant-manager security requirement?",
   ["A manager–plant mapping table, filtered by USERPRINCIPALNAME() in one role", "One static role per plant, with managers added to each role they need", "A filter Plant[ManagerEmail] = USERPRINCIPALNAME() on the Plant table, in one role", "Give each manager the Viewer role in a separate workspace per plant"], "A",
   "A mapping table with one row per manager per plant handles managers with several plants in one dynamic role, with a filter on Plant such as [PlantID] IN CALCULATETABLE ( VALUES ( PlantSecurity[PlantID] ), PlantSecurity[Email] = USERPRINCIPALNAME () ). A single ManagerEmail column on Plant allows only one manager per plant. Static roles per plant work but need maintenance. Separate workspaces duplicate content."),
 ]),
]
