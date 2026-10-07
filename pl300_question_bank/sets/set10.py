from model import single, multi, yesno, match, order, case

TITLE = "Exam simulation B — final rehearsal"
SUBTITLE = "The hardest paper in the bank: subtle distinctions, multi-step DAX, composite models and governance edge cases. Sit it last."
LEVEL = "Level 3 · Exam simulation"
CASE_NAME = "Relecloud Logistics"

ITEMS = [
# ---------------- P1 Get or connect to data (3 + 1 in case)
single("P1",
 "Cleaned tables produced by a Power BI dataflow (Gen1) in the service must be used in a new Desktop model. Which connector should you use?",
 ["Dataflows (Power BI dataflows)", "SQL Server", "Web", "Text/CSV"], "A",
 "The Dataflows connector lists the dataflows you have access to and their entities (tables), so you reuse the cleaned output. The generic connectors can't see dataflow outputs."),

single("P1",
 "An Azure SQL Database requires multi-factor authentication through the company's Microsoft Entra ID, and SQL logins are disabled. How should you authenticate in Power BI Desktop?",
 ["Microsoft account (organisational account) sign-in", "Database: SQL username and password", "Windows (current credentials)", "Anonymous"], "A",
 "Signing in with an organisational account uses Microsoft Entra ID, which supports MFA and works when SQL authentication is disabled. Database credentials need SQL logins. Windows authentication is for on-premises domain-joined sources. Anonymous gives no access."),

single("P1",
 "A query reads an Excel file from a local path with File.Contents. The file is moving to a SharePoint Online library, and refresh must work without a gateway. What must change?",
 ["The Source step must read the file's SharePoint URL (for example with Web.Contents or the SharePoint connectors) instead of File.Contents", "Only the file name in Data source settings", "Nothing; File.Contents works for SharePoint URLs", "Set the privacy level to Public"], "A",
 "File.Contents reads file-system paths, which the service treats as on-premises sources. Switching the Source step to read the cloud URL lets the service refresh it directly. Renaming the file or changing privacy levels doesn't change how the file is read."),

# ---------------- P2 Profile and clean (3)
single("P2",
 "Refresh fails with DataSource.NotFound in the Source step. Adding Remove errors at the end of the query doesn't help. Why?",
 ["It's a step-level error that stops the query from loading at all, whereas Remove errors only handles cell-level errors in rows", "Remove errors only works on text columns", "Remove errors must be the first step", "The model has too many relationships"], "A",
 "Cell-level errors affect individual values, so the rows can be removed or replaced. Step-level errors, like an unreachable source, mean there are no rows to clean. Fix the connection, path or credentials instead."),

single("P2",
 "After merging Orders with Customers and expanding a column, Orders has more rows than before. What is the most likely cause, and how do you confirm it?",
 ["Customers has duplicate CustomerID values; check with Column distribution (unique vs distinct) or Keep duplicates on the key", "The join kind was Inner", "The data types differ", "Privacy levels are wrong"], "A",
 "Each duplicate key on the right side produces an extra joined row when expanded, multiplying orders. Profiling or Keep duplicates on the key exposes the duplicates. An inner join can only reduce the row count."),

single("P2",
 "CSV files from a vendor change often, and the automatic Changed Type step keeps assigning wrong types. You want Power BI to stop detecting types automatically for unstructured sources, and set them yourself. Where is this?",
 ["Options → Data Load → Type detection: Never detect column types and headers for unstructured sources", "Data source settings → Privacy", "Model view → Properties", "Report settings → Visuals"], "A",
 "The type detection option controls whether Power Query adds an automatic type step for sources such as CSV and Excel. Turning it off lets you define types explicitly. The other settings don't affect type detection."),

# ---------------- P3 Transform and load (5)
single("P3",
 "Two queries have the same columns but in a different order: Region, Product, Amount in one, and Amount, Region, Product in the other. What happens when you append them?",
 ["Columns are matched by name, so the rows line up correctly", "Columns are matched by position, so values end up in the wrong columns", "The append fails", "Power Query merges them on Region"], "A",
 "Append aligns columns by name, not position, so a different order isn't a problem. Different names are the real issue: they create separate, partly null columns."),

single("P3",
 "A mainframe export is a fixed-width text file: characters 1–8 are the account number, 9–20 the name and 21–30 the balance. Which transformation splits it correctly?",
 ["Split column → By positions, at 0, 8 and 20", "Split column → By delimiter (space)", "Split column → By lowercase to uppercase", "Unpivot columns"], "A",
 "Fixed-width records are split by character position. Splitting on spaces breaks names that contain spaces and padded fields. Case transitions don't apply here."),

order("P3",
 "The Customer query needs an OrderCount column showing how many orders each customer has, without loading order rows into Customer. Put the actions in order.",
 ["Merge Customers with Orders on CustomerID using a Left outer join",
  "Select the expand button on the merged column and choose Aggregate",
  "Choose Count of OrderID",
  "Rename the new column OrderCount and set it to Whole Number"],
 "The expand dialog's Aggregate option summarises the nested Orders table per customer instead of expanding rows, which keeps one row per customer. A Left outer join keeps customers with no orders, who get a count of 0.",
 extra=["Expand all Orders columns", "Append Orders to Customers"]),

multi("P3",
 "A source regularly gains extra columns, and the query must keep working and keep loading only the intended data. Which two techniques make the query resilient?",
 ["Choose columns (Remove other columns) to keep the named columns you need", "Unpivot other columns, when the new columns are additional months to be unpivoted", "Remove columns by selecting the unwanted ones", "Hard-code a Changed Type step that lists every column", "Use Transpose"], "AB",
 "Remove other columns ignores any new column, and Unpivot other columns automatically includes new month columns. Removing columns by name lets new columns through. A Changed Type step listing every column breaks when columns are removed and doesn't type the new ones."),

single("P3",
 "A custom column must return the number of whole days between OrderDate and ShipDate, both of type Date. Complete the formula.",
 ["Duration.Days ( [ShipDate] - [OrderDate] )", "[ShipDate] - [OrderDate]", "Date.Day ( [ShipDate] ) - Date.Day ( [OrderDate] )", "Number.From ( [ShipDate] )"], "A",
 "Subtracting two dates in M returns a duration, and Duration.Days extracts the whole days as a number. The bare subtraction leaves a duration value. Subtracting day-of-month numbers fails across months.",
 code="= Table.AddColumn ( Source, \"DaysToShip\", each ____, Int64.Type )"),

# ---------------- M1 Design and implement a model (3 + 1 in case)
single("M1",
 "Power BI won't let you make a relationship active and says it would create ambiguous paths between two tables. What should you do?",
 ["Keep one path active and leave the other relationship inactive, using USERELATIONSHIP where the second path is needed", "Set every relationship to Both", "Create a second Date table for every fact", "Delete the fact tables"], "A",
 "Only one filter path between two tables can be active. Leaving the alternative path inactive removes the ambiguity, and measures can still activate it with USERELATIONSHIP. Bidirectional filters usually cause ambiguity rather than fix it."),

single("M1",
 "Business analysts need a small, static mapping table of 12 KPI names and their display order in the model. It has no source system, and they want to edit it occasionally. What is the simplest option?",
 ["Create the table with Enter data in Power BI Desktop", "Build a SQL table and a gateway", "Write the values in DAX measures", "Use a calculation group"], "A",
 "Enter data creates a small table stored in the model's Power Query, which can be edited later through the same dialog. Building database infrastructure for twelve rows is overkill. Measures and calculation groups aren't lookup tables."),

yesno("M1",
 "For each statement about relationships, select Yes if it is true.",
 [("A many-to-one relationship from Sales to Product is the same relationship as one-to-many from Product to Sales.", True),
  ("A Product slicer can only filter Sales if the relationship's cross-filter direction is Both.", False),
  ("A many-to-many relationship can be set to filter in a single direction.", True)],
 "Cardinality is the same relationship described from either end. Filters flow from the one side to the many side by default, so Single direction is enough for a dimension slicer to filter the fact. Many-to-many relationships support either Single or Both direction."),

# ---------------- M2 DAX (6)
single("M2",
 "A table visual shows sales by day. Sales PrevMonth = CALCULATE ( [Sales], PREVIOUSMONTH ( 'Date'[Date] ) ) and Sales Shifted = CALCULATE ( [Sales], DATEADD ( 'Date'[Date], -1, MONTH ) ). What do you see on the row for 15 March?",
 ["Sales PrevMonth shows all of February's sales; Sales Shifted shows sales for 15 February", "Both show sales for 15 February", "Both show all of February's sales", "Sales PrevMonth shows sales for 15 February; Sales Shifted shows all of February"], "A",
 "PREVIOUSMONTH returns every date of the month before the first date in context, whatever the granularity. DATEADD shifts the dates in context, so at day level it returns the same day a month earlier. This difference often catches people out."),

single("M2",
 "A measure must count new customers: those whose first-ever purchase falls within the selected period. Which expression is correct?",
 ["COUNTROWS ( FILTER ( VALUES ( Sales[CustomerKey] ), CALCULATE ( MIN ( Sales[OrderDate] ), ALL ( 'Date' ) ) >= MIN ( 'Date'[Date] ) ) )", "DISTINCTCOUNT ( Sales[CustomerKey] )", "COUNTROWS ( FILTER ( Customer, ISBLANK ( [Total Sales] ) ) )", "CALCULATE ( DISTINCTCOUNT ( Sales[CustomerKey] ), ALL ( 'Date' ) )"], "A",
 "For each customer active in the period, the first purchase date is computed over all dates. Customers whose first purchase is on or after the period start are new. DISTINCTCOUNT counts all active customers. The ISBLANK pattern counts customers with no sales. ALL('Date') counts customers across all time."),

single("M2",
 "A card must show \"Select a region\" when no region is filtered, and the region's sales otherwise. Cross-filters from other visuals on Region must not count as a selection. Which function tests this correctly?",
 ["ISFILTERED ( Region[Region] )", "ISCROSSFILTERED ( Region[Region] )", "HASONEFILTER ( Sales[Amount] )", "ISBLANK ( Region[Region] )"], "A",
 "ISFILTERED is TRUE only when the column is filtered directly. ISCROSSFILTERED is also TRUE when filters reach it through related tables or other columns. HASONEFILTER on an amount column and ISBLANK on a column don't test the selection."),

single("M2",
 "In a slicer built on a calculation group, the items appear in alphabetical order (PY, Current, YoY %, YTD). They must appear as Current, PY, YTD, YoY %. What should you set?",
 ["The Ordinal property of each calculation item", "The Precedence of the calculation group", "A sort-by column on the measure table", "The format string expression"], "A",
 "Each calculation item's ordinal controls the order in which items are displayed. Precedence decides which of several calculation groups applies first. Format strings control display formatting, not order."),

single("M2",
 "A measure fails with \"A table of multiple values was supplied where a single value was expected\" when several products are visible. The measure uses VALUES ( Product[Category] ) inside a text concatenation. What is the best fix for a single-value context?",
 ["Use SELECTEDVALUE ( Product[Category], \"Multiple\" ) instead of VALUES", "Use ALL ( Product[Category] )", "Use COUNTROWS ( Product )", "Wrap the measure in IFERROR"], "A",
 "VALUES returns a table, which errors when it holds more than one row and is used as a scalar. SELECTEDVALUE returns the single value when there is exactly one, or the alternate result otherwise. IFERROR hides the problem without defining the multi-value behaviour."),

single("M2",
 "Before field parameters existed, a report used a disconnected table MetricPicker[Metric] with values Revenue, Profit and Units in a slicer. Which measure returns the chosen metric?",
 ["SWITCH ( SELECTEDVALUE ( MetricPicker[Metric] ), \"Revenue\", [Revenue], \"Profit\", [Profit], \"Units\", [Units], [Revenue] )", "SUM ( MetricPicker[Metric] )", "IF ( MetricPicker[Metric] = \"Revenue\", [Revenue] )", "CALCULATE ( [Revenue], MetricPicker[Metric] )"], "A",
 "SELECTEDVALUE reads the slicer's choice, and SWITCH returns the matching measure, with a default when nothing or several are selected. The other expressions are invalid or ignore the selection. Field parameters now offer a built-in alternative."),

# ---------------- M3 Optimize (2)
single("M3",
 "In DAX query view, you've rewritten a slow measure under DEFINE MEASURE and confirmed it is faster and returns the same results. How do you apply it to the model?",
 ["Use the CodeLens option above the definition to update the model with the changed measure", "Copy it into a calculated column", "Republish the report without changes", "Restart Power BI Desktop"], "A",
 "DAX query view shows an option above a DEFINE MEASURE block to add or overwrite the measure in the model, so a tested definition can be applied directly. The other actions don't change the measure."),

single("M3",
 "A matrix with Customer and Product on the rows becomes very slow after Show items with no data was turned on. Why, and what should you do?",
 ["It forces every Customer × Product combination to be evaluated, even empty ones; turn it off unless empty rows are truly required", "It disables the model's compression; reload the model", "It turns on DirectQuery; switch back to Import", "It removes the relationship; recreate it"], "A",
 "Show items with no data asks for the cross join of the row fields, which can be enormous, and evaluates measures for each combination. Turning it off returns only combinations with data. It doesn't change compression, storage mode or relationships."),

# ---------------- V1 Create reports (4 + 1 in case)
single("V1",
 "A paginated report must reuse the measures and RLS of an existing Power BI semantic model rather than defining new queries against the database. How should you build it in Power BI Report Builder?",
 ["Use the Power BI semantic model as the paginated report's data source", "Connect Report Builder directly to the source SQL tables", "Export the model to Excel and use the workbook", "Use a dataflow as the source"], "A",
 "Report Builder can connect to a published Power BI semantic model, so the paginated report reuses its measures and respects its RLS. Querying the source tables duplicates logic and bypasses model security."),

single("V1",
 "For each region, a chart must show what share of revenue comes from each of four product lines, with every region's bar adding up to 100%. Which visual fits best?",
 ["100% stacked bar chart", "Clustered bar chart", "Line chart", "Gauge"], "A",
 "A 100% stacked bar normalises each bar to the region's total, so you compare shares across regions directly. A clustered bar compares absolute values. Line charts and gauges don't show composition."),

single("V1",
 "A filter card on Fiscal Year in the Filters pane must allow exactly one year to be selected. What should you set?",
 ["Turn on Require single selection on the filter card", "Lock the filter", "Hide the filter", "Use a Top N filter"], "A",
 "Basic filter cards have a Require single selection option that turns their check boxes into single-choice. Locking stops changes altogether. Hiding removes the card from view. Top N limits by value."),

single("V1",
 "Every visual title across the company's reports must use the Segoe UI Semibold font at 14 pt by default. Which part of a JSON theme sets this most efficiently?",
 ["textClasses (for example the title class)", "dataColors", "visualStyles for a single visual only", "A background image"], "A",
 "textClasses define fonts, sizes and colours for text categories such as titles, labels and callouts across all visuals in one place. dataColors only sets the palette. Per-visual visualStyles would need repeating for every visual type."),

# ---------------- V2 Usability and storytelling (5)
single("V2",
 "A report has 20 bookmarks. A bookmark navigator on the Sales page must show only the five Sales bookmarks. What should you do?",
 ["Put the five bookmarks in a bookmark group and set the navigator to show that group", "Delete the other 15 bookmarks", "Hide the other pages", "Create five separate buttons"], "A",
 "A bookmark navigator can be limited to a bookmark group, so organising bookmarks into groups controls which ones it shows. Deleting bookmarks affects other pages. Separate buttons work but don't update automatically."),

single("V2",
 "Personalize visuals is on for the report, but one regulatory chart must not be changeable by readers. What should you do?",
 ["Turn off personalisation for that visual (in its visual header options)", "Turn off Personalize visuals for the whole report", "Lock the Filters pane", "Hide the chart"], "A",
 "Personalisation can be turned off per visual, keeping it available for every other visual. Turning it off for the report is too broad. Locking filters or hiding the chart doesn't meet the need."),

single("V2",
 "A screen-reader user needs to hear the data values behind a column chart. Which built-in feature presents the chart's data in an accessible table?",
 ["Show as a table (keyboard shortcut Alt+Shift+F11)", "Focus mode only", "Spotlight", "Export to PDF"], "A",
 "Show as a table displays the visual's data in a table that screen readers can navigate, and it has a keyboard shortcut. Focus mode only enlarges the chart. Spotlight dims other visuals. A PDF export isn't the accessible in-report option."),

single("V2",
 "A bar chart shows sales by product, but users want it sorted by Margin %, which isn't on the axis or in the values. What should you do?",
 ["Add Margin % to the visual's Tooltips well, then sort the visual by Margin %", "Create a Sort by column on Product", "Add Margin % as a second Y-axis series", "Sort the Product table in Power Query"], "A",
 "A visual can be sorted by any field it contains, including tooltip fields, without plotting it. Sort by column fixes a column's order permanently. Adding it as a series changes the chart, and Power Query order doesn't control visual sorting."),

match("V2",
 "Match each requirement to the report feature that meets it.",
 [("Selecting a slicer value must not change one particular chart", "Edit interactions"),
  ("A Year slicer's selection must carry across five pages", "Sync slicers"),
  ("Right-clicking a customer must open a detailed page filtered to that customer", "Drillthrough"),
  ("Hovering over a bar must show a small custom page with a trend chart", "Report page tooltip")],
 ["Edit interactions", "Sync slicers", "Drillthrough", "Report page tooltip", "Bookmark"],
 "Edit interactions controls cross-filtering between visuals. Sync slicers shares a slicer's selection across pages. Drillthrough navigates with context. Report page tooltips show a custom page on hover. Bookmarks capture states and aren't needed for any of these.",
 left="Requirement", right="Feature"),

# ---------------- V3 Patterns and trends (3)
single("V3",
 "Anomaly detection flags a spike in daily returns, but the explanation pane is empty. You want Power BI to suggest which product categories or channels might explain it. What should you do?",
 ["Add Category and Channel to the anomaly detection's Explain by fields", "Increase the sensitivity", "Add a forecast", "Change the chart to a table"], "A",
 "Anomaly explanations are drawn from the fields you list in Explain by. Without them, Power BI has nothing to analyse. Sensitivity changes which points are flagged, not the explanations."),

single("V3",
 "In a decomposition tree, the first level must always be Region and users must not be able to remove it, though they can explore any dimensions below it. What should you configure?",
 ["Lock the Region level in the decomposition tree", "Use a page filter on Region", "Hide the Region field", "Turn off AI splits"], "A",
 "Locking a level stops consumers removing it while still letting them expand further levels. Filters and hidden fields don't control the tree's structure. Turning off AI splits only removes the AI options."),

single("V3",
 "New users don't know what to ask the Q&A visual. You want a few example questions to appear in it. What should you configure?",
 ["Suggested questions in Q&A setup", "Synonyms only", "A smart narrative", "A tooltip page"], "A",
 "Q&A setup lets you add suggested questions, which appear in the Q&A visual as clickable prompts. Synonyms help Q&A understand terms but don't suggest questions. Smart narratives and tooltips are unrelated."),

# ---------------- S1 Workspaces and assets (4)
single("S1",
 "An executive dashboard must appear prominently on the Power BI Home page for everyone who has access to it. What should you do?",
 ["Feature the dashboard on Home (feature content)", "Certify the dashboard", "Pin it to every user's favourites", "Use Publish to web"], "A",
 "Featured content appears on Home for users who have access. Certification marks trust but doesn't place content on Home. You can't set other users' favourites. Publish to web is public."),

single("S1",
 "Ten semantic models import from ten different databases on the same on-premises SQL Server. How many gateways do you need?",
 ["One standard gateway (or one cluster), with a connection for each database", "Ten gateways, one per database", "Ten personal-mode gateways", "No gateway, because they share a server"], "A",
 "A single gateway, ideally a cluster for resilience, can host many connections to different databases and serve many models. One gateway per database adds administration for no benefit. On-premises sources always need a gateway."),

single("S1",
 "The Deployment pipelines option is unavailable for a workspace in Pro licence mode. What is required?",
 ["Assign the workspace to Premium, Premium Per User or Fabric capacity", "Make every user an Admin", "Install a gateway", "Turn on the XMLA endpoint in Desktop"], "A",
 "Deployment pipelines need the workspaces to be on Premium, Premium Per User or Fabric capacity. Roles, gateways and Desktop settings don't enable them in a Pro workspace."),

yesno("S1",
 "For each statement about report subscriptions, select Yes if it is true.",
 [("A subscription can attach the full report as a PDF or PowerPoint file.", True),
  ("A recipient without access to the report still sees its data in the email.", False),
  ("A subscription can be scheduled to send after the semantic model refreshes.", True)],
 "Subscriptions can include full-report attachments, and they can run on a schedule or after data refresh. Recipients must have access to the content, and what they see respects their permissions."),

# ---------------- S2 Secure and govern (3 + 1 in case)
single("S2",
 "Compliance must find out who viewed or exported a sensitive report over the last 30 days. Where should they look?",
 ["The Microsoft Purview audit log (or the Fabric activity log)", "Performance Analyzer", "The report's bookmarks", "Query dependencies"], "A",
 "User activities such as viewing and exporting Power BI content are recorded in the audit and activity logs, which administrators and compliance teams can search. The other tools don't record user activity."),

single("S2",
 "A report in workspace B uses a semantic model in workspace A. Users who are Viewers of workspace B see errors in every visual. They have no access to workspace A. What should you grant?",
 ["Read permission on the semantic model in workspace A (for example by sharing the model or through an app)", "Admin on workspace B", "Build permission on the report", "A sensitivity label"], "A",
 "Viewing a report requires Read access to the semantic model it uses, wherever that model lives. Granting Read on the model in workspace A fixes the errors. Roles in workspace B don't cover workspace A."),

single("S2",
 "An analyst applies the Confidential sensitivity label to a .pbix file in Power BI Desktop and then publishes it. What happens?",
 ["The label is applied to the report and semantic model in the service when they are new there, and protection travels with the file", "The label is removed on publishing", "The label only exists in Desktop", "Publishing is blocked until certification"], "A",
 "Labels set in Desktop protect the .pbix file and are carried to the service on publish, for content that doesn't already have a label there. They aren't stripped or blocked, and certification is unrelated."),

# ---------------- Case study (P1, M1, V1, S2)
case("Relecloud Logistics",
 "Relecloud runs 60 depots across India. Shipments are stored in an on-premises Oracle database: about 80 million rows, plus live updates for in-transit shipments. Each shipment has an OriginDepot and a DestinationDepot. Finance uses an April–March fiscal year. IT has approved a box-and-whisker visual from AppSource. A DepotUsers table maps each manager's email to the DepotIDs they manage.",
 ["The control-tower page must show in-transit shipments with data at most five minutes old, while historical analysis must stay fast.",
  "Most measures analyse shipments by origin depot. A few must analyse by destination depot, using the same single Depot slicer.",
  "Every report author must have the approved box-and-whisker visual available in Power BI without importing it themselves.",
  "Each depot manager must see shipments that start or end at their depots."],
 [
  single("P1",
   "Which design meets the control-tower requirement?",
   ["A composite model: historical shipment data in Import, in-transit shipments in DirectQuery with automatic page refresh, and shared dimensions set to Dual", "Import everything with eight refreshes a day", "DirectQuery for the whole model with no aggregation", "A Publish to web report refreshed hourly"], "A",
   "A composite model keeps history fast in memory while querying live in-transit data directly, refreshed by automatic page refresh. Dual dimensions serve both sides efficiently. Import alone can't be five minutes fresh. All-DirectQuery slows historical analysis."),
  single("M1",
   "How should you relate the Depot table to Shipments?",
   ["An active relationship on OriginDepot and an inactive one on DestinationDepot, with destination measures using USERELATIONSHIP", "Two active relationships", "Two separate Depot tables with separate slicers", "A many-to-many relationship on both columns"], "A",
   "With one Depot slicer and mostly origin-based analysis, the origin relationship is active, and destination measures activate the second relationship with USERELATIONSHIP. Two active relationships aren't allowed. Two Depot tables would need two slicers, which the requirement rules out."),
  single("V1",
   "How do you make the approved visual available to every author?",
   ["A Fabric administrator adds it to Organizational visuals in the admin portal", "Each author downloads it from AppSource", "Embed it in the corporate theme", "Create it as a calculation group"], "A",
   "Organizational visuals are deployed centrally by an admin, so every author gets the approved version in their visualisation pane. Downloading individually doesn't scale and bypasses governance. Themes and calculation groups can't add visuals."),
  single("S2",
   "Which RLS design meets the depot-manager requirement?",
   ["A role filter on the Shipments table: VAR D = CALCULATETABLE ( VALUES ( DepotUsers[DepotID] ), DepotUsers[Email] = USERPRINCIPALNAME () ) RETURN Shipments[OriginDepot] IN D || Shipments[DestinationDepot] IN D", "A role filter on Depot: [DepotID] = USERPRINCIPALNAME ()", "A filter on Depot through the active origin relationship only", "Static roles per depot pair"], "A",
   "Because the requirement covers both origin and destination, the filter must test both columns on the fact table, using the depots mapped to the signed-in user. Filtering Depot through the active relationship only covers the origin. Comparing a DepotID with a user name matches nothing."),
 ]),
]
