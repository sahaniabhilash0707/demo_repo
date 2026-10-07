from model import single, multi, yesno, match, order, case

TITLE = "Foundations — the whole outline in one sitting"
SUBTITLE = "Core vocabulary across all four domains: connectors, Power Query basics, the star schema, first DAX, report features and the service."
LEVEL = "Level 1 · Foundation"
CASE_NAME = "Contoso Retail"

ITEMS = [
# ---------------- P1 Get or connect to data (3 + 1 in case)
single("P1",
 "Your organisation has a certified semantic model in the Power BI service. You must build a new report on it in Power BI Desktop without creating a copy of the data or a local model. How do you connect?",
 ["Get data → SQL Server, and import the model's source tables", "Get data → Power BI semantic models", "Export the model to a .pbix file and open it", "Use Analyze in Excel and publish the workbook"], "B",
 "Connecting to a published semantic model gives a live connection: the report uses the shared model directly, with no local copy of the data. Importing the source tables builds a second, ungoverned model. A .pbix download is a copy. Analyze in Excel produces an Excel workbook, not a Power BI report."),

single("P1",
 "The password of the SQL account used by a Power BI Desktop file was changed, and refresh now fails with a credentials error. Where do you enter the new password?",
 ["Data source settings → select the source → Edit Permissions", "Transform data → Advanced editor, then edit the Source step", "Model view → Properties pane of a table", "File → Options → Privacy, set the level to Public"], "A",
 "Credentials are stored per data source, not per query. Data source settings lists every source the file uses and lets you edit or clear its credentials. The Advanced editor shows the M code, which never contains the stored password. Privacy levels control how data is combined, not how you sign in."),

single("P1",
 "A report will be distributed as a Power BI template (.pbit). Whoever opens the template must choose a country from a fixed list, and the queries must load only that country's rows. What should you create?",
 ["A calculated column that filters by country", "A Power Query parameter used in a filter step", "A slicer on Country with Single select turned on", "A bookmark for each country"], "B",
 "When a .pbit file opens, Power BI prompts for the value of each parameter, and a parameter used in a filter step limits which rows are loaded. A slicer or bookmark filters the report after all the data is already loaded. A calculated column can't stop rows loading."),

# ---------------- P2 Profile and clean (3)
single("P2",
 "You need to see, for every column in the query, the percentage of values that are valid, errors and empty. Which Power Query view option shows this?",
 ["Column distribution", "Column quality", "Column profile", "Show whitespace"], "B",
 "Column quality shows the Valid, Error and Empty percentages under each column header. Column distribution shows distinct and unique counts with a small histogram. Column profile shows detailed statistics for one selected column. Show whitespace only reveals spaces and line feeds in cell values."),

single("P2",
 "Column distribution on a ProductCode column shows 120 distinct and 80 unique. What does the 80 mean?",
 ["80 values occur exactly once in the column", "80 values are not null", "There are 80 different values in the column", "80 rows contain errors"], "A",
 "Unique counts values that appear exactly once. Distinct counts how many different values exist, which is 120 here. Remember profiling looks at the first 1,000 rows unless you switch it to the entire data set."),

single("P2",
 "A Region slicer shows \"North\" twice. The source contains \"North\" and \"North \" with a trailing space. Which Power Query transformation fixes this with one step?",
 ["Transform → Format → Clean", "Transform → Format → Trim", "Transform → Format → Capitalize Each Word", "Remove duplicates on the Region column"], "B",
 "Trim removes leading and trailing whitespace, so both values become \"North\". Clean removes non-printable control characters, not spaces. Capitalisation changes letter case only. Removing duplicates on Region would delete fact rows rather than fix the value."),

# ---------------- P3 Transform and load (5)
single("P3",
 "You receive Sales2025 and Sales2026 extracts with identical columns. You need one Sales table containing the rows from both. What should you do?",
 ["Merge queries on OrderID", "Append queries", "Create a relationship between the two tables", "Pivot the Year column"], "B",
 "Append stacks rows from tables with the same shape. Merge joins columns from another table on a key, which isn't the requirement. A relationship keeps two separate tables in the model, so every measure would have to add them together."),

single("P3",
 "A Customer table has a PostalCode column. Some codes start with zero, for example 01234, and Power Query detected the column as Whole Number. What should the data type be?",
 ["Whole Number", "Decimal Number", "Text", "Fixed decimal number"], "C",
 "Postal codes are identifiers, not quantities. Stored as a number, 01234 becomes 1234 and the leading zero is lost. Text keeps the value exactly as it appears and stops it being summed by accident."),

match("P3",
 "Match each requirement to the Power Query transformation that meets it.",
 [("The source has one column per month; you need a Month column and a Value column", "Unpivot other columns"),
  ("Bring the RegionName from a Regions query into the Sales query using RegionID", "Merge queries"),
  ("Combine this year's and last year's extracts into one table", "Append queries"),
  ("Field names run down the first column and each record is a column", "Transpose")],
 ["Unpivot other columns", "Merge queries", "Append queries", "Transpose", "Pivot column"],
 "Unpivot turns columns into attribute/value rows, and Unpivot other columns copes with months added later. Merge joins columns on a key. Append stacks rows. Transpose rotates the whole table so rows become columns. Pivot does the opposite of unpivot and isn't needed here.",
 left="Requirement", right="Transformation"),

order("P3",
 "A REST API returns JSON with a top-level list of order records. You need a typed table with one row per order. Put the actions in order.",
 ["Connect with Web.Contents and parse the response with Json.Document",
  "Convert the list to a table",
  "Expand the record column into individual columns",
  "Set a data type on every column"],
 "Parsing gives a list of records. Converting the list to a table gives one column of records. Expanding that column creates one column per field. Setting data types comes last, so the types apply to the expanded columns rather than to the record column.",
 extra=["Unpivot the expanded columns", "Merge the query with itself"]),

single("P3",
 "A CurrencyRates query is loaded into the model and used by relationships. Its data never changes, and it slows every scheduled refresh because the source is slow. The table must stay in the model. What should you change?",
 ["Clear Enable load on the query", "Clear Include in report refresh on the query", "Delete the query and type the rates into a calculated table", "Set the query's privacy level to Private"], "B",
 "Clearing Include in report refresh keeps the table and its data in the model but skips it during refresh. Clearing Enable load would remove the table from the model, breaking the relationships. Retyping the data creates a maintenance problem, and privacy levels don't affect refresh frequency."),

# ---------------- M1 Design and implement a model (3 + 1 in case)
single("M1",
 "A Product table has one row per ProductKey. A Sales table has many rows per ProductKey. What relationship should Power BI create between them?",
 ["One-to-many from Product to Sales, single direction", "Many-to-many between Product and Sales, both directions", "One-to-one, both directions", "Many-to-one from Product to Sales, both directions"], "A",
 "The dimension side holds one row per key and the fact side holds many, so the relationship is one-to-many with filters flowing from Product to Sales. Single direction is the default and the safe choice. Both directions adds ambiguity and is rarely needed."),

single("M1",
 "A report page needs two date slicers at the same time: one for order date and one for due date, each filtering Sales independently. The Sales table has OrderDateKey and DueDateKey. What is the best model design?",
 ["One Date table with an active relationship to OrderDateKey and an inactive one to DueDateKey, used with USERELATIONSHIP", "Two date tables, Order Date and Due Date, each with an active relationship to its own key", "One Date table related to both keys with both relationships active", "A many-to-many relationship between Date and Sales"], "B",
 "USERELATIONSHIP activates the second relationship inside a measure, but a slicer can only filter through the active relationship. Two independent slicers need two role-playing date tables, each actively related. Power BI won't allow two active relationships between the same two tables."),

single("M1",
 "A Store table has a City column. On a map visual, some cities are placed in the wrong country. Which column property should you set first?",
 ["Sort by column", "Data category: City", "Summarize by: Don't summarize", "Display folder"], "B",
 "The data category tells Bing maps what kind of location the value is. City (plus country or state columns in the location well) reduces wrong guesses. Sort by column changes ordering. The summarisation setting controls default aggregation. Display folders only organise the field list."),

# ---------------- M2 DAX (6)
single("M2",
 "A measure must always return sales of red products, even when a report user selects a different colour in a slicer. Which expression should you use?",
 ["CALCULATE ( [Total Sales], 'Product'[Color] = \"Red\" )", "CALCULATE ( [Total Sales], KEEPFILTERS ( 'Product'[Color] = \"Red\" ) )", "FILTER ( 'Product', 'Product'[Color] = \"Red\" )", "SUMX ( 'Product', [Total Sales] )"], "A",
 "A filter argument in CALCULATE replaces any existing filter on the same column, so the slicer's colour is overridden by Red. KEEPFILTERS intersects with the slicer instead, giving blank when another colour is selected. FILTER on its own returns a table, not a value. SUMX adds sales for every product."),

single("M2",
 "Complete the measure so it returns year-to-date sales for a calendar year.",
 ["TOTALYTD", "DATESMTD", "SAMEPERIODLASTYEAR", "PREVIOUSYEAR"], "A",
 "TOTALYTD evaluates the expression from the start of the year to the last date in the current filter context. DATESMTD is month-to-date. SAMEPERIODLASTYEAR and PREVIOUSYEAR shift to last year rather than accumulating this year.",
 code="Sales YTD = ____ ( [Total Sales], 'Date'[Date] )"),

single("M2",
 "A Margin % measure divides profit by sales. Some products have zero sales, and the visual shows errors. Which expression returns blank instead of an error for those rows?",
 ["[Profit] / [Sales]", "DIVIDE ( [Profit], [Sales] )", "IFERROR ( [Profit] / [Sales], 0 )", "[Profit] / ( [Sales] + 1 )"], "B",
 "DIVIDE returns blank, or an optional alternate result, when the denominator is zero, and it's the recommended pattern. The / operator returns an error or infinity. IFERROR works but is slower and returns 0, which shows the product as 0% instead of hiding it. Adding 1 changes the answer."),

single("M2",
 "You need the number of different customers who bought something in the current filter context. Sales has one row per order line and a CustomerKey column. Which measure is correct?",
 ["CALCULATE ( COUNT ( Sales[CustomerKey] ), Sales[Amount] > 0 )", "COUNTROWS ( Sales )", "DISTINCTCOUNT ( Sales[CustomerKey] )", "COUNTROWS ( Customer )"], "C",
 "DISTINCTCOUNT counts each customer once, however many lines they have. COUNT and COUNTROWS count order lines. COUNTROWS(Customer) counts customers in the dimension whether or not they bought, unless a filter happens to flow from Sales, which it doesn't by default."),

single("M2",
 "Which measure returns sales for the same period in the previous year, for whatever period is selected (a month, a quarter or a year)?",
 ["CALCULATE ( [Total Sales], SAMEPERIODLASTYEAR ( 'Date'[Date] ) )", "CALCULATE ( [Total Sales], 'Date'[Year] = YEAR ( TODAY () ) - 1 )", "[Total Sales] - 365", "CALCULATE ( [Total Sales], ALL ( 'Date' ) )"], "A",
 "SAMEPERIODLASTYEAR shifts the current set of dates back one year, so it works at any granularity. Filtering on last calendar year ignores the period the user selected. Subtracting 365 changes the value, not the period. ALL('Date') removes the date filter and returns sales for all time."),

yesno("M2",
 "For each statement about calculated columns and measures, select Yes if it is true.",
 [("A calculated column is evaluated during refresh and stored in the model.", True),
  ("A measure can be placed on a slicer to filter other visuals.", False),
  ("A measure is evaluated at query time in the filter context of the visual.", True)],
 "Calculated columns are computed row by row at refresh and take memory. Measures are computed when a visual queries them, in that visual's filter context. Slicers need column values, so a measure can't be used directly as a slicer field."),

# ---------------- M3 Optimize (2)
single("M3",
 "Performance Analyzer shows a table visual taking 9,000 ms, of which DAX query is 8,700 ms and Visual display is 200 ms. Where should you focus?",
 ["The measures and model behind the visual", "The number of visuals on the page", "The report theme", "The visual's formatting options and conditional formatting"], "A",
 "When almost all the time is in DAX query, the engine is the bottleneck: the measure logic, relationships or model size. Visual display and Other are small, so reducing visuals or changing formatting won't help much. Copy the query into DAX query view to investigate further."),

multi("M3",
 "A model is larger than expected. Which two actions reduce its size without removing anything the reports use?",
 ["Remove columns that no report, measure or relationship uses", "Turn off Auto date/time in Options", "Set every relationship to Both directions", "Add a calculated column that concatenates key columns", "Change every Text column to the Whole Number data type"], "AB",
 "Unused columns cost memory for nothing, and Auto date/time creates a hidden date table for every date column. Cross-filter direction doesn't change size. Extra calculated columns add size. Changing data types wholesale would break the text columns."),

# ---------------- V1 Create reports (5)
single("V1",
 "Executives want to see monthly revenue for the last 24 months and spot the trend. Which visual is most appropriate?",
 ["Pie chart with one slice per month", "Line chart over the 24 months", "Table with one row per month", "Treemap"], "B",
 "A line chart over a continuous time axis is the standard way to show a trend. Pie charts and treemaps show part-to-whole at one point in time. A table shows exact values but makes a trend hard to see."),

single("V1",
 "The marketing team requires every new report to use the corporate colours, fonts and default visual formatting. What is the most efficient approach?",
 ["Format every visual manually in each report", "Create and apply a JSON report theme", "Create a bookmark with the formatting", "Use a background image in each report"], "B",
 "A report theme (JSON file) sets the colour palette, fonts and default visual formatting in one step, and it can be shared and reused. Formatting manually doesn't scale. Bookmarks capture view state, not formatting. A background image doesn't change the visuals."),

single("V1",
 "The operations team needs a formatted list of 50,000 order lines that prints across many pages with a header on every page, and exports cleanly to Excel. Which item should you build?",
 ["A Power BI report page with a large table visual", "A paginated report (Power BI Report Builder)", "A dashboard with a pinned table", "A Q&A visual"], "B",
 "Paginated reports are made for pixel-perfect, multi-page, printable output with repeating headers, and for exporting large tabular results. A report table visual scrolls on screen and isn't designed for printing long lists. Dashboards and Q&A are summary and exploration tools."),

single("V1",
 "A Product table has a column of web addresses. In a table visual, each address must appear as a clickable hyperlink. What should you do?",
 ["Set the column's Data category to Web URL", "Set the column's Data category to Image URL", "Apply a background colour rule to the column", "Create a bookmark for each address"], "A",
 "With the Web URL data category, table and matrix visuals display the value as a clickable link. Image URL renders the address as a picture. Background colour rules change formatting only. Bookmarks don't open external web addresses."),

single("V1",
 "You want to add a Copilot narrative visual to a report. Which environment supports Copilot in Power BI?",
 ["A workspace on a Fabric trial capacity with Copilot switched on", "Paid Fabric capacity (F2 or higher) or Premium (P1 or higher)", "Any workspace, as long as every author has a Pro licence", "My workspace with a free licence"], "B",
 "Copilot needs a paid Fabric capacity (F2 or above) or Premium (P1 or above), plus the tenant setting for Azure OpenAI features. Trial capacities aren't supported. A Pro licence on its own, without such a capacity, isn't enough."),

# ---------------- V2 Usability and storytelling (5)
single("V2",
 "When a user selects a value in a Region slicer, a card showing company-wide revenue must not change. Other visuals on the page must still be filtered. What should you configure?",
 ["Edit interactions: set the card to None", "Sync slicers so the slicer is hidden on the page", "A visual-level filter on the card", "Lock the card in the Selection pane"], "A",
 "Edit interactions controls how one visual affects each other visual on the page. Setting None on the card stops the slicer filtering it, while the other visuals stay filtered. A visual-level filter adds a filter but doesn't remove the slicer's effect. The Selection pane controls visibility and layering."),

single("V2",
 "Two buttons must switch the same page area between a chart and a table showing the same data. The current slicer selections must not change when a user clicks either button. How should you set up the bookmarks?",
 ["Two bookmarks with Data and Display both on, each hiding one visual", "Two bookmarks, Display only (Data cleared), each hiding one visual", "One bookmark per slicer value, each showing both visuals", "Use drillthrough instead of bookmarks"], "B",
 "With Data cleared, a bookmark doesn't capture or reapply filter and slicer state. With Display selected, it captures which visuals are visible. Each bookmark shows one visual and hides the other, and the buttons point to them. A Data bookmark would reset the slicers to their saved values."),

single("V2",
 "Field staff open a report on their phones. In the Power BI mobile app, the page shows the desktop layout shrunk down. What should you do?",
 ["Create a mobile layout for the page", "Change the page size to Letter", "Create a dashboard and pin the key visuals to it", "Increase the font size in the theme"], "A",
 "The mobile layout is a separate phone canvas for each page. Visuals must be placed on it explicitly, and the app uses it in portrait mode. Changing the page size or the theme doesn't create a phone-optimised layout."),

single("V2",
 "Report users can export the underlying rows from visuals, which exposes detail the business wants to keep hidden. Users must still be able to export the summarised data a visual shows. What should you change?",
 ["Set export data to summarised data only", "Remove the users' Build permission", "Apply a sensitivity label that blocks exports", "Hide the detailed columns in the model"], "A",
 "The export data setting controls whether users can export summarised data, summarised plus underlying data, or nothing. Choosing summarised only meets the requirement directly. Sensitivity labels protect exported files but don't stop the export. Hiding columns doesn't stop underlying-data export of the visible fields."),

single("V2",
 "A bar chart of sales by product category is sorted alphabetically. Users want the largest category at the top. What should you do?",
 ["Sort the visual by the Sales measure, descending", "Create a Sort by column on the category", "Rename the categories with numbers", "Apply a Top N filter showing the top 100 categories by sales"], "A",
 "The visual's sort setting (More options → Sort axis) can sort by the measure in descending order. Sort by column fixes the order of a column against another column, for example month name by month number, and doesn't sort by value. Renaming is a workaround. Top N filters rows but doesn't sort them."),

# ---------------- V3 Patterns and trends (2 + 1 in case)
single("V3",
 "A manager wants to explore profit across region, then product category, then sales channel, letting Power BI suggest the next split that explains the most. Which visual should you use?",
 ["Decomposition tree", "Ribbon chart", "Waterfall chart by region", "Gauge"], "A",
 "The decomposition tree lets users drill into a measure across dimensions in any order, and its AI splits (High value, Low value) suggest the next best dimension. A ribbon chart shows rank changes over time. A waterfall shows how values add up to a total. A gauge shows one value against a target."),

single("V3",
 "A scatter chart plots customers by annual spend and visit frequency. You want Power BI to find groups of similar customers automatically. What should you use?",
 ["Automatically find clusters", "Binning on annual spend", "A constant line on the Analytics pane", "Grouping on the customer name"], "A",
 "Clustering finds groups of similar points on a scatter chart and creates a new field identifying each cluster. Binning buckets one numeric column into equal ranges. Grouping combines values you pick manually. A constant line is a reference line, not a grouping."),

# ---------------- S1 Workspaces and assets (4)
single("S1",
 "Three hundred sales staff need to view a set of reports. They must not see draft content in the workspace. What is the most efficient way to distribute the reports?",
 ["Share each report individually with each user", "Publish an app and grant a security group access", "Add all 300 users to the workspace with the Viewer role", "Use Publish to web and email the link"], "B",
 "An app packages selected content for consumers, keeps drafts out of view, and can be granted to a security group in one step. Sharing reports one by one doesn't scale. Workspace Viewers see every item in the workspace, drafts included. Publish to web makes content public on the internet."),

single("S1",
 "A semantic model imports data from a SQL Server database on the company network. It must refresh every morning in the Power BI service. What is required?",
 ["An on-premises data gateway", "A Pro licence for every report viewer", "DirectQuery storage mode", "A OneLake shortcut"], "A",
 "The service reaches sources on a private network through an on-premises data gateway, using a connection mapped to the semantic model. Viewer licensing doesn't affect refresh. DirectQuery would also need the gateway. Shortcuts are a Fabric lakehouse feature and don't refresh a semantic model from SQL Server."),

single("S1",
 "A report author believes a new semantic model is ready for others to use. No formal review process exists. What can the author do to signal this?",
 ["Certify the semantic model", "Promote the semantic model", "Apply the Highly Confidential sensitivity label", "Mark the model as a date table"], "B",
 "Any user with write permission on an item can promote it. Certification is restricted to users the tenant admin authorises, usually after a review. Sensitivity labels classify content. They don't endorse it."),

single("S1",
 "Which statement about Power BI dashboards is correct?",
 ["Dashboards are created in Power BI Desktop and published with the report.", "A dashboard can contain tiles pinned from several reports.", "A dashboard can have several pages.", "Data alerts can be set on any report visual but not on dashboard tiles."], "B",
 "A dashboard is a single canvas of tiles, which can come from several reports and semantic models. It's created in the service, not in Desktop, and it has only one page. Power BI data alerts are set on dashboard tiles such as cards, KPIs and gauges."),

# ---------------- S2 Secure and govern (3 + 1 in case)
single("S2",
 "Finance analysts must build their own reports on the published Finance semantic model, in their own workspaces. They must not edit the model. Which permission should you grant on the model?",
 ["Read", "Build", "Write", "Reshare"], "B",
 "Build permission lets users create reports, use Analyze in Excel and query the model from other workspaces, without changing it. Read only lets them view existing content. Write lets them change the model. Reshare lets them share it further, which wasn't asked for."),

single("S2",
 "Internal auditors must open and interact with reports in a workspace. They must not create, edit or share anything. Which workspace role should you assign?",
 ["Admin", "Member", "Contributor", "Viewer"], "D",
 "Viewer is the least-privileged workspace role: view and interact only. Contributor can create and edit content. Member can also share and publish the app. Admin can do everything, including managing access."),

yesno("S2",
 "For each statement about sensitivity labels in Power BI, select Yes if it is true.",
 [("Labels are defined in Microsoft Purview, not in Power BI.", True),
  ("Applying a label to a report removes Viewer access for users outside the finance department.", False),
  ("A label on a report stays on a PowerPoint file exported from it.", True)],
 "Labels and their protection settings are defined in Microsoft Purview and applied to Power BI items. They classify content and protect exported files, but they don't change who can open the item inside Power BI. That's controlled by roles and permissions."),

# ---------------- Case study (P1, M1, V3, S2)
case("Contoso Retail",
 "Contoso Retail runs 120 stores in five regions. Point-of-sale data is written to a SQL Server database in the head-office data centre: about 40 million sales rows a year. Monthly sales targets per store are kept in an Excel workbook on SharePoint. A Store table lists every store and its region, and a mapping table lists the email address of each store manager. Reports are used mainly between 08:00 and 20:00.",
 ["Store managers need yesterday's data each morning. Intraday data is not required.",
  "Sales and targets must be analysed together by store and by month.",
  "The regional director wants to know which factors are associated with small basket sizes.",
  "Each store manager must see only their own store's data. Managers come and go every month, and the solution must need no change when they do."],
 [
  single("P1",
   "Which storage mode should you use for the sales fact table?",
   ["Import", "DirectQuery", "Live connection", "Dual"], "A",
   "Overnight data meets the requirement, so Import gives the best performance and full DAX with a scheduled refresh through the gateway. DirectQuery would send every visual query to the store database during trading hours with no benefit. Live connection applies to existing semantic models. Dual is only meaningful for dimensions in a composite model."),
  single("M1",
   "How should you model sales and targets so both can be analysed by store?",
   ["Merge the target into every sales row in Power Query", "A shared Store dimension related one-to-many to both tables", "Create a many-to-many relationship directly between Sales and Targets on StoreID", "Append Targets to Sales"], "B",
   "Two fact tables at different grains should share conformed dimensions. A Store dimension filtering both facts lets measures from each work side by side. Relating the facts directly creates a many-to-many relationship and ambiguous totals. Merging or appending mixes grains in one table."),
  single("V3",
   "Which visual meets the regional director's requirement?",
   ["Key influencers", "Smart narrative", "Funnel chart", "Matrix with conditional formatting"], "A",
   "Key influencers analyses which factors are associated with a metric being high or low, which is exactly the director's question. Smart narrative describes what is on the page. A funnel shows stages. A matrix shows values but leaves the analysis to the user."),
  single("S2",
   "You create one role with a DAX filter that compares the manager mapping table to USERPRINCIPALNAME(). Where do you assign the store managers to the role?",
   ["In Power BI Desktop, under Modeling → Manage roles, before publishing", "In the service, on the semantic model's Security page, adding a group", "In the workspace access pane, adding the managers as Contributors", "In the app's audience settings"], "B",
   "Roles are defined in Desktop, but members are assigned in the service on the semantic model's Security page. Adding a group means monthly staff changes are handled by group membership, not by editing Power BI. Contributors bypass RLS, and app audiences control which content is visible, not which rows."),
 ]),
]
