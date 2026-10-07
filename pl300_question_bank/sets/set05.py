from model import single, multi, yesno, match, order, case

TITLE = "Report craft and storytelling"
SUBTITLE = "Visual choice, formatting, tooltips, bookmarks and navigation, accessibility and AI visuals, plus the core of every other domain."
LEVEL = "Level 2 · Core"
CASE_NAME = "Litware Healthcare"

ITEMS = [
# ---------------- P1 Get or connect to data (3 + 1 in case)
single("P1",
 "A government web page publishes a table of regional population figures in HTML. You want to load it into Power BI and refresh it. Which connector should you use?",
 ["Web, then pick the table in the Navigator", "Text/CSV, pointing at the page's URL", "Blank query with the figures typed in by hand", "SharePoint folder"], "A",
 "The Web connector reads an HTML page and offers the tables it detects in the Navigator, and the query refreshes from the page. Text/CSV expects a file. A typed table never refreshes. SharePoint folder is for document libraries."),

single("P1",
 "While developing, you want Power BI Desktop to load only the first 1,000 rows of a 200-million-row source, but the published model must load everything. What is a clean way to do this?",
 ["A RowLimit parameter in a Keep top rows step, set high in the service", "Delete rows in the source during development, then restore them before publishing", "Use a slicer to show 1,000 rows", "Turn off Enable load in Desktop and turn it back on in the service"], "A",
 "A parameter-driven row limit keeps development fast, and the parameter can be changed in the semantic model settings after publishing, without editing the query. A slicer only filters what's shown. Disabling load removes the table altogether."),

single("P1",
 "A composite model has a DirectQuery Sales fact and an Import aggregation table. The Product dimension relates to both. To avoid limited relationships and let the engine choose the fastest path, which storage mode should Product use?",
 ["Dual", "Import", "DirectQuery", "Live connection"], "A",
 "Dual tables act as Import or DirectQuery depending on the query. Queries that hit the Import aggregation use the in-memory copy, and queries that reach the DirectQuery fact can join at the source. A pure Import or pure DirectQuery dimension forces one of the two paths to be inefficient."),

# ---------------- P2 Profile and clean (3)
single("P2",
 "A Comments column contains empty text (\"\") rather than null, so Column quality reports it as 0% empty. You want empty strings treated as missing values. What should you do?",
 ["Use Replace values, replacing empty text with null", "Use Trim", "Change the type to Whole Number", "Use Remove empty from the filter menu on every column"], "A",
 "Replacing empty text with null makes missing values consistent, so profiling, filters and DAX treat them as blank. Trim only removes spaces. Changing the type to a number creates errors. Removing empty rows deletes data."),

single("P2",
 "A source export sometimes contains exact duplicate rows, identical in every column, because of a bug. What is the correct fix in Power Query?",
 ["Select all columns, then Remove duplicates", "Select only the first column, then Remove duplicates", "Keep duplicates", "Group by every column with Count rows and keep the count"], "A",
 "Removing duplicates across all columns removes only rows that are identical in every column. Using a single column could delete legitimate rows that share a value. Keep duplicates does the opposite."),

single("P2",
 "A query previews without errors in Power Query, but refresh fails with \"DataFormat.Error: We couldn't convert to Number\". What is the most likely cause?",
 ["A value outside the preview rows can't be converted", "The gateway is offline, so the source can't be read during refresh", "The model has too many relationships for the refresh to complete", "The report theme is invalid"], "A",
 "The editor previews and profiles a sample of rows, and the full refresh processes everything. A bad value later in the data, such as text in a numeric column, only fails during refresh. Profiling the entire data set or checking the source's values finds it."),

# ---------------- P3 Transform and load (5)
single("P3",
 "After merging Sales with Region and expanding RegionName, the new column is named \"Region.RegionName\". You want it named \"RegionName\" without adding a rename step. What should you do when expanding?",
 ["Clear Use original column name as prefix", "Select Aggregate instead of Expand", "Expand every column", "Choose a Left anti join"], "A",
 "The expand dialog adds the merged column's name as a prefix by default. Clearing that option keeps the original field names. Aggregate summarises the nested table instead of expanding it. Join kind doesn't change column names."),

single("P3",
 "A ProductLabel column holds text like \"Trail Bike [TB-200]\". You need just the code inside the square brackets. Which transformation needs no code?",
 ["Extract → Text between delimiters, using [ and ]", "Split column → By number of characters", "Replace values", "Format → Clean"], "A",
 "Text between delimiters returns the part between the start and end delimiter, whatever the label's length. A fixed character count fails for labels of different lengths. Replace values and Clean don't extract substrings."),

match("P3",
 "Match each column to the most appropriate data type.",
 [("Postal code such as 01234", "Text"),
  ("Unit price stored to four decimal places", "Fixed decimal number"),
  ("Order timestamp where the hour matters", "Date/Time"),
  ("IsActive flag with values TRUE and FALSE", "True/False")],
 ["Text", "Fixed decimal number", "Date/Time", "True/False", "Whole number"],
 "Identifiers with leading zeros are text. Currency-style amounts are best as fixed decimal. A timestamp needs Date/Time when the time part is used. Flags are True/False. Whole number would lose decimals and leading zeros.",
 left="Column", right="Data type"),

single("P3",
 "An XML file contains Orders elements, each with nested OrderLine elements. You need one row per order line, with the order number on each row. What should you do after connecting?",
 ["Expand the nested OrderLine table column", "Transpose the table", "Pivot the OrderLine column on the order number", "Append the query to itself"], "A",
 "Semi-structured data arrives as nested tables or records. Expanding the nested column produces one row per child element, alongside its parent's fields. Transposing and pivoting reshape flat tables and don't flatten nesting."),

order("P3",
 "An Excel export has three title rows, then a header row, then one column per month. You need a clean table with Product, Month and Value. Put the actions in order.",
 ["Remove the top 3 rows",
  "Use first row as headers",
  "Select Product and choose Unpivot other columns",
  "Rename Attribute to Month and set the data types"],
 "Title rows must go before the real header row can be promoted. Unpivot other columns then turns the month columns into rows, and the final step names and types the result.",
 extra=["Transpose the table", "Remove duplicates on Product"]),

# ---------------- M1 Design and implement a model (4)
single("M1",
 "In model view, a relationship between Sales and Date is drawn as a dashed line. What does that mean?",
 ["It is inactive and only used when a measure calls USERELATIONSHIP", "It is a many-to-many relationship", "It is a bidirectional relationship", "It is a limited relationship, because one side is a DirectQuery source"], "A",
 "Inactive relationships are drawn with a dashed line and are only used when activated with USERELATIONSHIP in a calculation. Cardinality and direction are shown with markers and arrows. Limited relationships are shown with different markers, not a dashed line."),

single("M1",
 "A Product table has a column of image addresses. Table visuals must show the product picture. Which property should you set?",
 ["Data category: Image URL", "Data category: Web URL", "Format: Text", "Summarize by: Count"], "A",
 "With the Image URL data category, table, matrix, slicer and card visuals render the address as an image. Web URL shows a clickable link. Format and summarisation don't render images."),

single("M1",
 "A model has 60 measures in one table, and authors struggle to find them. You want them grouped as Sales, Margin and Inventory in the field list, without changing any DAX. What should you use?",
 ["Display folders on the measures", "Calculation groups", "Three new tables with one measure each", "Perspectives in Desktop"], "A",
 "Display folders organise fields into folders in the field list, purely for navigation. Calculation groups change how measures calculate. Moving measures into many tables is clumsy. Perspectives aren't authored in the Desktop UI and aren't a security feature."),

yesno("M1",
 "For each statement about relationships in Power BI, select Yes if it is true.",
 [("Only one relationship between two tables can be active at a time.", True),
  ("On the one side of a one-to-many relationship, the column must contain unique values.", True),
  ("You can create a relationship between a Text column and a Whole Number column.", False)],
 "Power BI allows one active relationship between two tables, and others stay inactive. The one side must be unique, or the model can't treat it as one. Relationship columns must have matching data types, so text and number columns must first be converted to the same type."),

# ---------------- M2 DAX (6)
single("M2",
 "In a matrix with Category and Product rows, a measure must show each product's share of its own category. Which expression is correct?",
 ["DIVIDE ( [Sales], CALCULATE ( [Sales], ALLEXCEPT ( 'Product', 'Product'[Category] ) ) )", "DIVIDE ( [Sales], CALCULATE ( [Sales], ALL ( 'Product' ) ) )", "DIVIDE ( [Sales], CALCULATE ( [Sales], ALLSELECTED () ) )", "DIVIDE ( [Sales], [Sales] )"], "A",
 "ALLEXCEPT removes every filter on Product except Category, so the denominator is the current category's total. ALL('Product') gives the grand total. ALLSELECTED gives the visible total. Dividing a measure by itself returns 1."),

single("M2",
 "A card's title must read \"Sales for North\" when one region is selected, and \"Sales for all regions\" otherwise. Which measure should drive the title?",
 ["\"Sales for \" & SELECTEDVALUE ( Region[Region], \"all regions\" )", "\"Sales for \" & VALUES ( Region[Region] )", "\"Sales for \" & MAX ( Region[Region] )", "\"Sales for \" & FIRSTNONBLANK ( Region[Region], 1 )"], "A",
 "SELECTEDVALUE returns the single selected value, or the alternate text when there are zero or several. VALUES errors when more than one value is visible. MAX and FIRSTNONBLANK return a region name even when several are selected, which would mislead."),

single("M2",
 "You need the number of customers with no sales in the selected period. Which measure is correct?",
 ["COUNTROWS ( FILTER ( Customer, ISBLANK ( [Total Sales] ) ) )", "COUNTBLANK ( Sales[Amount] )", "COUNTROWS ( Customer ) - COUNTROWS ( Sales )", "DISTINCTCOUNT ( Sales[CustomerKey] )"], "A",
 "FILTER iterates customers, and context transition evaluates [Total Sales] for each customer in the period, so ISBLANK finds those with no sales. COUNTBLANK counts blank amounts in fact rows. Subtracting row counts mixes customers with order lines. DISTINCTCOUNT counts customers who did buy."),

single("M2",
 "Survey scores come from a random sample of customers, and analysts want the standard deviation as an estimate for the whole customer base. Which function should you use?",
 ["STDEV.S", "STDEV.P", "VAR.P", "MEDIAN"], "A",
 "STDEV.S estimates standard deviation from a sample, using n − 1. STDEV.P assumes the data is the whole population. VAR.P is population variance, not standard deviation. MEDIAN is a measure of central tendency."),

single("M2",
 "You need the average sales per customer, counting only customers who bought in the current filter context. Which measure is correct?",
 ["AVERAGEX ( VALUES ( Sales[CustomerKey] ), [Total Sales] )", "AVERAGE ( Sales[Amount] )", "[Total Sales] / COUNTROWS ( Customer )", "AVERAGEX ( Sales, Sales[Amount] )"], "A",
 "VALUES returns the customers present in the filtered sales, and AVERAGEX averages each customer's total. AVERAGE over Sales[Amount] is the average line value. Dividing by all customers includes those who didn't buy. AVERAGEX over Sales rows is still a line average."),

single("M2",
 "Complete the YTD calculation item in a calculation group so it applies to whatever measure is in the visual.",
 ["SELECTEDMEASURE ()", "[Total Sales]", "SELECTEDVALUE ( 'Date'[Date] )", "ISSELECTEDMEASURE ()"], "A",
 "SELECTEDMEASURE returns the measure currently being evaluated, which is how one calculation item applies to every measure. Hard-coding [Total Sales] would make the item work for only one measure. SELECTEDVALUE returns a date. ISSELECTEDMEASURE tests which measure is in use.",
 code="CALCULATE ( ____, DATESYTD ( 'Date'[Date] ) )"),

# ---------------- M3 Optimize (2)
single("M3",
 "Performance Analyzer shows a map visual with 30,000 points has a short DAX query time but a very long Visual display time. What should you do?",
 ["Render fewer points by aggregating or filtering", "Rewrite the measure with variables to cut query time", "Add an index column to the location table to speed lookups", "Turn off Auto date/time"], "A",
 "Visual display time is spent drawing the result, and too many points is a common cause. Showing fewer points speeds rendering. The query is already fast, so rewriting DAX won't help."),

single("M3",
 "Performance Analyzer identifies a slow visual. You want to inspect and rerun the exact DAX that the visual sends to the model. What is the quickest route?",
 ["Copy query, then run it in DAX query view", "Open Power Query and refresh", "Export the visual's data to CSV and inspect it in Excel", "Use Analyze in Excel and inspect the PivotTable's query"], "A",
 "Copy query captures the DAX the visual generated, and DAX query view lets you run and edit it inside Desktop, including trying alternative measure definitions. The other options don't show the visual's query."),

# ---------------- V1 Create reports (5)
single("V1",
 "For one report only, you want to change the eight data colours. The corporate theme must stay unchanged for other reports. What is quickest?",
 ["Customize current theme and change the data colours", "Edit the corporate JSON theme file, then re-import it here", "Apply conditional formatting to every visual", "Change the Windows display colours"], "A",
 "Customize current theme changes the theme saved in this report only, without editing the shared JSON file. Editing the corporate file would affect every report that uses it. Conditional formatting per visual is laborious."),

single("V1",
 "A chart title must change to reflect the selected region. You have a measure that returns the title text. How do you use it?",
 ["Title → fx → Field value, choosing the measure", "Type the measure name in square brackets into the title text", "Create a bookmark per region, each with its own typed title", "Put the measure in the Tooltips well"], "A",
 "Titles, like many text properties, accept conditional formatting by field value, so a measure can supply dynamic text. Typing the name shows it literally. Bookmarks per region don't scale. Tooltips appear on hover only."),

single("V1",
 "A Region slicer must allow only one region to be selected at a time. What should you configure?",
 ["Turn on Single select in the slicer settings", "Set the slicer style to Dropdown in the format settings", "Add a visual-level filter", "Lock the slicer in the Filters pane"], "A",
 "Single select limits a slicer to one value. Dropdown changes how it's displayed, not how many values can be picked. Filters and locking don't change slicer selection behaviour."),

single("V1",
 "A visual must colour each state of a country by its sales value, filling the state's shape. Which visual fits best?",
 ["Filled map", "Map (bubble map)", "Scatter chart", "Gauge"], "A",
 "A filled map (choropleth) shades geographic areas such as states by value. A bubble map places circles sized by value at locations. Scatter charts and gauges aren't geographic."),

single("V1",
 "A table shows profit variance, which can be negative or positive. The background must be red for negatives, white at zero and green for positives, with smooth shading. What should you configure?",
 ["Gradient background colour with a middle colour at 0", "Data bars with red negative and green positive bars", "Icon conditional formatting with three rules (below, at and above 0)", "A theme with three colours"], "A",
 "Gradient formatting with minimum, centre and maximum colours (centre fixed at 0) gives diverging shading. Data bars show length, not colour scales. Icons are discrete symbols. A theme doesn't colour cells by value."),

# ---------------- V2 Usability and storytelling (4 + 1 in case)
single("V2",
 "You built a report-page tooltip called Trend Tooltip. It must appear only when users hover over the Sales by Month chart, not on other visuals. What should you do?",
 ["On the chart, set the tooltip to the Trend Tooltip page", "Turn on Allow use as tooltip on every page of the report", "Add the chart to a bookmark", "Set the Trend Tooltip page's canvas size to Letter"], "A",
 "Setting a visual's tooltip to a specific report page connects that page to that visual only. Allow use as tooltip is required on the tooltip page itself, but it doesn't choose which visuals use it. Bookmarks and page sizes don't control this."),

single("V2",
 "During a presentation, you want one visual to stand out while the others on the page fade into the background, and you want to save that state. What should you use?",
 ["Spotlight, captured in a bookmark", "Focus mode exported to PDF", "Hide all other visuals permanently", "Change the theme to dark"], "A",
 "Spotlight fades every other visual on the page, and a bookmark can capture that display state for the presentation. Focus mode opens one visual full screen but isn't stored with Display state in the same way. Hiding visuals permanently removes them."),

single("V2",
 "Users' slicer and filter changes are kept when they return to a report, but management wants every visit to start with the author's default filters. What should you change?",
 ["Turn off persistent filters in the report settings", "Lock every slicer", "Delete the bookmarks", "Remove the users' Build permission on the semantic model"], "A",
 "Persistent filters keep each user's last filter state by default. Turning the setting off means everyone starts from the published state. Locking applies to filter-pane filters, not to slicers. Bookmarks and permissions don't control this."),

single("V2",
 "On a kiosk-style report, viewers keep opening visual menus (export, focus mode, sort) from the icons above each visual. The author wants those icons gone for viewers. What should you change?",
 ["Turn off the visual header in the format settings", "Lock and hide the Filters pane in the report settings", "Set Edit interactions to None for every visual", "Remove the report theme"], "A",
 "The visual header holds the icons and menus above a visual. Turning it off hides them in the service. Locking filters or changing interactions doesn't remove the header."),

# ---------------- V3 Patterns and trends (2 + 1 in case)
single("V3",
 "A scatter chart of advertising spend against sales should show the overall direction of the relationship as a straight line. Where do you add it?",
 ["Analytics pane → Trend line", "Format pane → Data labels", "Analytics pane → Forecast", "Filters pane → Top N"], "A",
 "A trend line fits a linear trend through the scatter points. Forecasts apply to line charts with a time axis. Data labels and top N filters don't show a trend."),

single("V3",
 "A user typed a question in the Q&A visual and got a good bar chart. You want to keep it as a normal visual on the page. What should you do?",
 ["Turn this Q&A result into a standard visual", "Take a screenshot", "Pin the Q&A visual to a dashboard as a new tile", "Create a bookmark"], "A",
 "Q&A can convert its current answer into a regular visual with the same fields, which you can then format like any other. A screenshot is static. Pinning and bookmarks keep the Q&A visual rather than converting it."),

# ---------------- S1 Workspaces and assets (4)
single("S1",
 "A new workspace must run on the organisation's Fabric capacity so that features such as Copilot and free-licence viewing are available. Where do you set this?",
 ["Workspace settings → License info, choosing Fabric capacity", "Report settings in Power BI Desktop, before publishing", "The data gateway's connection settings for the workspace", "The app's audience settings, choosing a capacity per audience"], "A",
 "A workspace's licence mode and capacity assignment are set in the workspace settings. Reports, gateways and app audiences don't decide which capacity a workspace uses."),

single("S1",
 "A dashboard tile must keep the interactivity of a whole report page, including its slicers, rather than being a static visual. What should you pin?",
 ["The whole report page, as a live page tile", "Each visual separately", "A screenshot of the page uploaded as an image tile", "A Q&A answer"], "A",
 "Pinning a live page puts the whole page on the dashboard as an interactive tile that keeps its slicers and visuals. Pinning individual visuals creates separate tiles. A screenshot isn't interactive."),

single("S1",
 "A workspace admin wants to know which reports are actually viewed, by how many people, and how often. What should they use?",
 ["Usage metrics for the reports in the workspace", "Performance Analyzer", "The deployment pipeline's compare view between stages", "Query dependencies"], "A",
 "Usage metrics reports show views, viewers and trends for reports and dashboards. Performance Analyzer measures load times in Desktop. Pipeline compare shows differences between stages. Query dependencies shows Power Query lineage."),

multi("S1",
 "Which two types of content can you include in a workspace app?",
 ["Reports", "Dashboards", "On-premises data gateways", "Deployment pipelines", "Tenant settings"], "AB",
 "Apps package content from a workspace, such as reports, dashboards, paginated reports and workbooks, for consumers. Gateways, pipelines and tenant settings are infrastructure and administration items, not app content."),

# ---------------- S2 Secure and govern (3 + 1 in case)
single("S2",
 "A semantic model's report users currently have Build permission, but only the analytics team should be able to create new reports on it. Everyone else must keep viewing the existing reports. What should you do?",
 ["Remove Build from all but the analytics team, keeping Read", "Remove everyone except the analytics team from the workspace", "Apply a sensitivity label that restricts report creation", "Turn off Publish to web"], "A",
 "Read lets users view reports built on the model, and Build lets them create new content on it. Managing these on the model gives the right split. Removing workspace access would also stop viewing. Labels and Publish to web don't control Build."),

single("S2",
 "Your organisation wants new Power BI reports and models to receive the General sensitivity label automatically, so users only change it when needed. What should be configured?",
 ["A default label in the Purview label policy", "A certification setting in the tenant admin portal", "An app audience", "A deployment rule"], "A",
 "Label policies can set a default label applied to new content, so nothing starts unlabelled. Certification is endorsement. App audiences control visibility. Deployment rules change data sources between pipeline stages."),

single("S2",
 "One RLS role must show both the North and South regions. Which filter expression on the Region table is correct?",
 ["Region[Region] IN { \"North\", \"South\" }", "Region[Region] = \"North\" && Region[Region] = \"South\"", "Region[Region] = \"North, South\"", "CONTAINSSTRING ( \"North\", \"South\" )"], "A",
 "IN with a list returns TRUE for either value. Two equality tests joined with AND can never both be true on one row. Comparing to one combined string matches nothing. The CONTAINSSTRING expression doesn't reference the column."),

# ---------------- Case study (P1, V2, V3, S2)
case("Litware Healthcare",
 "Litware runs 25 clinics. Appointments are stored in Azure SQL Database. After each visit, patients complete a satisfaction survey stored in a SharePoint Online list. The report has six pages. Each clinic has a manager, and a small head-office team oversees all clinics.",
 ["Survey responses must refresh with the rest of the model, with no gateway to maintain.",
  "At the monthly board meeting, the analyst must walk through six saved views of the report in a fixed order, some of which switch between a chart and a table.",
  "Operations wants to break average wait time down by clinic, then doctor, then appointment type, to see which contributes most.",
  "Clinic managers must see only their own clinic. The head-office team must see all clinics through the same report."],
 [
  single("P1",
   "How should you connect to the survey responses?",
   ["The SharePoint Online list connector", "Export the list to CSV every month", "The on-premises data gateway with the Folder connector", "A blank query with the data pasted in"], "A",
   "The SharePoint Online list connector reads the list directly from the cloud, so scheduled refresh needs no gateway. CSV exports and pasted data don't refresh. A gateway and the Folder connector are for on-premises files."),
  single("V2",
   "How should you support the board walk-through?",
   ["A bookmark per view, stepped through in order", "Create six separate reports and link them with buttons", "Use Edit interactions", "Use automatic page refresh to cycle through the views"], "A",
   "Bookmarks capture each view, including chart/table visibility and filter state, and can be stepped through in order like slides. Separate reports or interaction settings don't create a sequence. Page refresh is unrelated."),
  single("V3",
   "Which visual meets the operations requirement?",
   ["Decomposition tree", "Key influencers", "Ribbon chart", "Card"], "A",
   "A decomposition tree breaks a measure down across several dimensions in the order the user chooses, showing each level's contribution. Key influencers ranks factors for an outcome rather than drilling hierarchically. A ribbon chart shows rank over time."),
  single("S2",
   "You have a dynamic Clinic role that filters by the signed-in manager's email. How do you let the head-office team see all clinics?",
   ["Add the group to a second role, AllClinics, with no filter", "Give the head-office team the workspace Viewer role", "Remove RLS from the model", "Add the head-office team to the existing Clinic role as members"], "A",
   "A role with no filter grants access to all rows, and adding the head-office group to it gives them every clinic, since RLS roles are additive. Viewer access alone is still filtered by RLS. Removing RLS exposes everything to everyone. Adding head office to the Clinic role filters them by their own email, which matches no clinic."),
 ]),
]
