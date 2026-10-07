from model import single, multi, yesno, match, order, case

TITLE = "Performance and storage modes"
SUBTITLE = "Import, DirectQuery, Direct Lake, Dual and hybrid tables; query folding, aggregations, model size and the DAX patterns that scale."
LEVEL = "Level 3 · Advanced"
CASE_NAME = "Tailspin Toys"

ITEMS = [
# ---------------- P1 Get or connect to data (3 + 1 in case)
single("P1",
 "A Direct Lake semantic model built on a lakehouse's SQL analytics endpoint is fast most of the time. Visuals that use one table, which is actually a SQL view, are consistently slower. What explains this?",
 ["Views fall back to DirectQuery; Direct Lake reads Delta tables only", "Direct Lake re-imports views on every query instead of caching them", "Views are always imported", "The capacity is paused"], "A",
 "Direct Lake loads column data from Delta tables in OneLake. Views aren't Delta tables, so a Direct Lake on SQL model answers those queries through DirectQuery fallback. Materialising the view as a Delta table restores Direct Lake behaviour."),

single("P1",
 "A DirectQuery report queries a large SQL function that takes a CountryCode argument. A slicer selection must be passed into the M query so the source only computes the chosen country. What should you use?",
 ["A dynamic M query parameter bound to the slicer", "A what-if parameter whose value the M query reads", "A calculation group", "A report-level filter"], "A",
 "Dynamic M query parameters let a slicer or filter value be bound to an M parameter, which is then used inside the source query or function. What-if parameters are DAX tables. Calculation groups change measures. A report filter is applied to the generated query, not passed as a function argument."),

single("P1",
 "On Premium capacity, a sales table holds five years of history. Imported performance is needed for history, but today's orders must appear immediately without waiting for a refresh. What should you configure?",
 ["Incremental refresh with real-time DirectQuery data (a hybrid table)", "Import with 48 scheduled refreshes a day, one every 30 minutes", "DirectQuery for the whole table, including the five years of history", "A separate DirectQuery report for today's orders only"], "A",
 "A hybrid table keeps historical partitions imported and adds a DirectQuery partition for the most recent period, so the latest rows are queried live. Scheduled refresh still lags. Full DirectQuery gives up Import performance for history. Separate reports fragment the analysis."),

# ---------------- P2 Profile and clean (3)
single("P2",
 "A ShipDate text column uses \"00/00/0000\" for orders not yet shipped, and these become errors when the column is typed as Date. Unshipped orders must stay in the data with no ship date. What should you do?",
 ["Replace \"00/00/0000\" with null before the type change", "Remove errors after the type change", "Change the type to Text permanently", "Fill down the ShipDate column"], "A",
 "Converting the placeholder to null first means the type change succeeds and unshipped orders keep an empty ship date. Removing errors deletes those orders. Keeping the column as text breaks date logic. Fill down invents dates that don't exist."),

single("P2",
 "With profiling switched to the entire data set, a CustomerID column in a 1,000,000-row table shows 1,000,000 distinct and 1,000,000 unique values, with 0% empty. What can you conclude?",
 ["Every value occurs once, so it can be a dimension key", "The column has many duplicates, so it can't be used as a key", "Half the values are blank", "The column must be split before use"], "A",
 "When distinct and unique both equal the row count and nothing is empty, every value appears once: the definition of a usable key. Duplicates would make unique lower than distinct."),

single("P2",
 "The data team must review rows that fail type conversion each day, but the model must load only valid rows. What is the cleanest Power Query design?",
 ["Keep errors in an unloaded reference query; Remove errors in the main query", "Use Replace errors with 0 in the main query", "Turn off Column quality", "Load both valid and invalid rows into the model, and hide the invalid ones with a report filter"], "A",
 "A reference query that keeps errors gives the team a review list, and the main query removes them so only valid rows load. Replacing errors with 0 hides problems and distorts totals. Loading invalid rows pollutes the model."),

# ---------------- P3 Transform and load (5)
single("P3",
 "When you configure incremental refresh, Power BI warns that the query can't be folded. The query filters on RangeStart and RangeEnd, but an Added Index Column step comes before the filter. What should you do?",
 ["Move the date filter before the index step, or remove the index", "Ignore the warning; folding only affects DirectQuery, not incremental refresh", "Change the parameters to Text", "Turn off Enable load"], "A",
 "Adding an index column usually stops folding, so later steps run locally and each refresh would read the full table. The RangeStart/RangeEnd filter must fold so each partition reads only its own rows. Parameter types must stay Date/Time."),

single("P3",
 "You must combine Sales_EU and Sales_US into a new third query, leaving both original queries unchanged. Which command should you use?",
 ["Append queries as new", "Append queries", "Merge queries", "Duplicate"], "A",
 "Append queries as new creates a separate query containing the combined rows, leaving the originals as they are. Plain Append adds the rows to the selected query itself. Merge joins columns. Duplicate copies one query."),

single("P3",
 "A JSON field named tags holds a list such as {\"red\", \"sale\", \"new\"} for each product. You need one text column per product containing \"red, sale, new\", keeping one row per product. What should you do?",
 ["Extract Values on the list, with a comma delimiter", "Expand the list to new rows, then remove duplicates", "Pivot the tags column", "Use Split column into rows"], "A",
 "Extract Values concatenates the items of a list into one text value with a delimiter, keeping the row count unchanged. Expanding to new rows creates one row per tag. Pivot and split don't apply to a list column here."),

match("P3",
 "You merge Orders (first table) with Customers (second table) on CustomerID. Match each requirement to the join kind.",
 [("Only orders that have a matching customer", "Inner"),
  ("Every order, with customer details where available", "Left outer"),
  ("Orders whose CustomerID doesn't exist in Customers (orphans)", "Left anti"),
  ("Every order and every customer, matched where possible", "Full outer")],
 ["Inner", "Left outer", "Left anti", "Full outer", "Right anti"],
 "Inner keeps matched rows only. Left outer keeps all orders. Left anti keeps orders with no match, which finds orphaned keys. Full outer keeps everything from both sides. Right anti would return customers with no orders.",
 left="Requirement", right="Join kind"),

order("P3",
 "Put the steps to set up incremental refresh on a large Sales table in order.",
 ["Create RangeStart and RangeEnd parameters of type Date/Time",
  "Filter the OrderDate column using the two parameters in Power Query",
  "Define the incremental refresh policy on the Sales table in Power BI Desktop",
  "Publish the model; the first refresh in the service creates the partitions"],
 "The parameters must exist, with those exact names and the Date/Time type, before the filter can use them. The policy is defined on the table in Desktop, and partitions are created by the first refresh in the service, not in Desktop.",
 extra=["Turn off Enable load on Sales", "Switch Sales to DirectQuery"]),

# ---------------- M1 Design and implement a model (4)
single("M1",
 "In a composite model, an imported Budget table is related to a DirectQuery Sales table from a different source. Power BI marks the relationship as limited. Which statement is true?",
 ["RELATED can't cross it, and no blank row is added for unmatched values", "The relationship behaves exactly like a regular one-to-many relationship", "The relationship is automatically converted to Import", "Limited relationships only exist in Direct Lake models"], "A",
 "Relationships across source groups are limited: the join is evaluated as an inner join between groups, unmatched rows don't produce a blank member, and functions such as RELATED aren't available across them. This affects totals and DAX, so design with it in mind."),

single("M1",
 "RLS is defined on a Users table that relates to a UserRegion bridge table, which relates to Region and then Sales. The role's filter doesn't reach Sales because one relationship filters the wrong way. What should you configure on that relationship?",
 ["Set it to Both and turn on Apply security filter in both directions", "Make the relationship inactive and activate it with USERELATIONSHIP in the role", "Change cardinality to one-to-one", "Hide the bridge table"], "A",
 "For a security filter to travel against a relationship's default direction, the relationship must be bidirectional and set to apply security filters in both directions. Making it inactive or hiding the table stops the filter altogether."),

single("M1",
 "An AgeBand column (\"18–24\", \"25–34\"…) is used in many slicers. Where should you create it for the best model compression and reuse?",
 ["In the source or Power Query", "As a measure that returns the band for each customer", "As a visual calculation", "In each report, as a group on the Age column"], "A",
 "Columns created in the source or Power Query are compressed together with the rest of the table and are available to every downstream tool. DAX calculated columns are computed after load and are generally less efficient. Measures and visual calculations can't be used as slicer fields."),

yesno("M1",
 "For each statement about storage modes in Power BI Desktop, select Yes if it is true.",
 [("A Dual table can serve a query either from its imported copy or by querying the source.", True),
  ("A composite model can't contain Import tables.", False),
  ("After a table has been switched to Import, it can't be switched back to DirectQuery.", True)],
 "Dual tables are answered from memory or the source depending on the query. Composite models mix Import with DirectQuery (or Dual) tables by definition. Desktop allows a table to change from DirectQuery or Dual to Import, but not from Import back to DirectQuery."),

# ---------------- M2 DAX (6)
single("M2",
 "Which filter is generally the most efficient way to keep only red products inside CALCULATE?",
 ["'Product'[Color] = \"Red\"", "FILTER ( ALL ( 'Product' ), 'Product'[Color] = \"Red\" )", "FILTER ( 'Product', 'Product'[Color] = \"Red\" )", "FILTER ( Sales, RELATED ( 'Product'[Color] ) = \"Red\" )"], "A",
 "A boolean filter on a single column is internally a filter over just that column's values, which is cheap. FILTER over a whole table iterates every row and can carry extra columns into the filter. Filtering the fact table is the most expensive option."),

single("M2",
 "A calculation group has items Current, PY and YoY %. YoY % must display as a percentage, while the others keep the original measure's currency format. What should you configure?",
 ["A dynamic format string on the YoY % calculation item", "A separate measure for every combination", "The Format property of the calculation group column in the model", "A theme"], "A",
 "Calculation items can have a format string expression that overrides the measure's format for that item only, for example \"0.0%\". Setting a column format would apply to every item. Separate measures defeat the purpose of the group."),

single("M2",
 "A model has two calculation groups: Time Intelligence (YTD, PY) and Currency (USD, EUR). Users report that YTD in EUR is wrong because conversion runs before the YTD calculation. What controls the order in which the groups apply?",
 ["The calculation groups' Precedence property", "The order of items within each group", "The name of each group", "The sort-by column of the Date table"], "A",
 "When several calculation groups apply to one measure, the group with the higher precedence is applied first. Item ordinal only controls display order within a group. Names and sort order don't affect evaluation."),

single("M2",
 "A calculation must be available when users connect to the model with Analyze in Excel, and in every report built on the model. Which should you create?",
 ["A model measure", "A visual calculation", "A report-level measure in a live-connected report", "A quick filter"], "A",
 "Model measures are part of the semantic model, so Excel and every report can use them. Visual calculations exist only on their visual. Report-level measures exist only in that report. Filters aren't calculations."),

single("M2",
 "Bonus = IF ( [Total Sales] > 10000, [Total Sales] * 0.05, 0 ). Rows per salesperson are correct, but the grand total applies the rule to total sales instead of adding each person's bonus. How do you fix the total?",
 ["Bonus = SUMX ( VALUES ( Salesperson[ID] ), IF ( [Total Sales] > 10000, [Total Sales] * 0.05, 0 ) )", "Turn off totals in the visual", "Bonus = CALCULATE ( IF ( [Total Sales] > 10000, [Total Sales] * 0.05 ), ALL ( Salesperson ) )", "Change the visual to a matrix"], "A",
 "Non-additive logic evaluated at the total level sees the total, not each person. Iterating the salespeople with SUMX applies the rule per person and adds the results, at every level. Hiding totals avoids the issue rather than solving it. ALL computes one value for everyone."),

single("M2",
 "A converted-sales measure must only return a value when exactly one currency is selected in the Currency slicer, and blank otherwise. Which pattern should you use?",
 ["IF ( HASONEVALUE ( Currency[Code] ), [Sales] * SELECTEDVALUE ( Currency[Rate] ) )", "[Sales] * MAX ( Currency[Rate] )", "[Sales] * SUM ( Currency[Rate] )", "IF ( ISBLANK ( Currency[Code] ), [Sales] )"], "A",
 "HASONEVALUE checks that exactly one currency is in context before converting, and SELECTEDVALUE returns that rate. MAX or SUM of rates gives a meaningless number when several are selected. ISBLANK on a column needs a row context and doesn't test the selection."),

# ---------------- M3 Optimize (1 + 1 in case)
single("M3",
 "A DirectQuery fact table has 5 billion rows. Most visuals show sales by month and product category. You add an imported summary table at that grain. What else is needed so those visuals use the summary automatically?",
 ["Manage aggregations on the summary table, mapped to the detail table", "Rename the summary table Sales", "Create a relationship between the summary and the detail table on their keys", "Turn on Auto date/time"], "A",
 "User-defined aggregations need the summary table's columns mapped (Sum, GroupBy and so on) to the detail table's columns in Manage aggregations. The engine then redirects matching queries to the in-memory summary. Renaming or relating the tables doesn't enable aggregation awareness."),

# ---------------- V1 Create reports (4 + 1 in case)
single("V1",
 "A Power BI report page must show an operational paginated report, with its parameters passed from the page's slicers. What should you add?",
 ["The Paginated report visual, with fields mapped to its parameters", "An image of the paginated report", "A web URL to Report Builder with the parameters in the query string", "A Q&A visual"], "A",
 "The Paginated report visual renders a published paginated report inside a Power BI report and can pass field values into its parameters, so slicers drive it. Images and links don't stay in sync with the page's filters."),

single("V1",
 "Across 40 reports, every new card visual must have its category label turned off and a specific font size, by default. What is the most maintainable approach?",
 ["Add card visualStyles to the corporate JSON theme", "Format each card manually", "Copy one formatted card into every report and use it as a template", "Use a bookmark"], "A",
 "A JSON theme can set default formatting for specific visual types through visualStyles, so every new card follows the standard. Manual formatting and copying don't scale and drift over time."),

single("V1",
 "An author wants Copilot to propose several outlines of possible report pages from the model, then pick one to build. Which Copilot capability is this?",
 ["Suggest content for a new report page", "Summarise the semantic model", "Create a narrative visual", "Explain a DAX query"], "A",
 "Suggesting content for a new report page gives the author candidate page ideas to choose from before Copilot builds one. Summarising describes the model. A narrative visual describes data on a page."),

single("V1",
 "A Customer slicer lists 5,000 names, and users can't find the one they need. What is the simplest improvement?",
 ["Turn on Search in the slicer", "Split the slicer into 26 slicers by first letter", "Change it to a between slicer", "Remove the slicer"], "A",
 "Search lets users type to find a value in a long list. Splitting by letter is clumsy. A between slicer is for numeric and date ranges."),

# ---------------- V2 Usability and storytelling (5)
single("V2",
 "In an Import-mode report, the Page refresh option is missing from the page's format settings. Why?",
 ["It's only available for DirectQuery and similar sources", "The theme disables it", "Page refresh needs a mobile layout before it appears in settings", "The page has more than ten visuals"], "A",
 "Automatic page refresh re-queries the source. Imported data only changes on refresh, so the feature applies to DirectQuery and similar sources. The other options aren't related."),

single("V2",
 "Each chart's alt text must describe its current values for screen-reader users, for example \"Revenue this month: 1.2M\", and update as filters change. What should you do?",
 ["Set the Alt text with fx to a measure that builds the description", "Type a fixed alt text for each chart that includes this month's value", "Add a text box under each chart", "Use a high-contrast theme"], "A",
 "Alt text can be driven by a measure, so screen readers announce current, filtered values. Fixed alt text goes stale. Text boxes add clutter and aren't tied to the visual. High contrast helps low-vision users but doesn't add descriptions."),

single("V2",
 "Two different slicers, one on page 1 and one on page 3, both use Date[Year] and must share a selection. They aren't copies of each other. What should you configure?",
 ["Give both slicers the same group name in Sync slicers", "Copy one slicer over the other", "Use a report-level filter on Date[Year] instead of slicers", "Use drillthrough"], "A",
 "Sync slicers groups let separate slicers on the same field share their selection, even if they weren't copied from each other. A report filter applies everywhere but isn't interactive in the same way."),

single("V2",
 "Across a whole report, selecting a data point should cross-filter other visuals instead of cross-highlighting them, without setting Edit interactions for every pair of visuals. What should you change?",
 ["The report's default visual interaction setting", "Each visual's format pane, under the Interactions card", "The theme", "The persistent filters setting for the report"], "A",
 "A report-level setting switches the default interaction for every visual to filtering. Edit interactions is still available for exceptions. Themes and persistent filters don't control interactions."),

multi("V2",
 "Which two changes help screen-reader users understand a report?",
 ["Add alt text to each visual", "Give every visual a meaningful title", "Use colour as the only way to show status", "Remove the tab order", "Put text into background images"], "AB",
 "Screen readers announce alt text and titles. Colour-only encoding, broken tab order and text embedded in images are all accessibility problems."),

# ---------------- V3 Patterns and trends (3)
single("V3",
 "Anomaly detection on a daily line chart flags too many points as anomalies, most of them normal weekend dips. What should you change first?",
 ["Lower the anomaly detection sensitivity", "Raise the sensitivity", "Remove the date axis", "Add a forecast"], "A",
 "Sensitivity controls how far a point must be from the expected range to be flagged. Lowering it reduces false positives. Raising it flags even more points. The date axis is required for the feature."),

single("V3",
 "A monthly sales line includes the current, incomplete month, which drags the forecast down. How should you configure the forecast?",
 ["Set Ignore the last to 1 point", "Increase the confidence interval", "Set the seasonality to 1", "Turn off the forecast"], "A",
 "Ignoring the last point excludes the incomplete month from the model used for the forecast. The confidence interval only changes the shaded band. A seasonality of 1 removes the seasonal pattern."),

single("V3",
 "A DaysLate column ranges from 0 to 60. Managers want a histogram of late deliveries in weekly buckets (0–6, 7–13 and so on). What should you create?",
 ["Bins on DaysLate with a bin size of 7", "A group with 60 manual items", "Clusters on DaysLate", "A slicer on DaysLate"], "A",
 "Binning creates equal-size numeric ranges, here 7 days wide, which a column chart then shows as a histogram. Manual grouping is tedious. Clustering is for scatter charts. A slicer filters rather than buckets."),

# ---------------- S1 Workspaces and assets (4)
single("S1",
 "On Premium capacity, an imported semantic model is expected to grow past 10 GB. What should you enable so it can grow and refresh efficiently?",
 ["Large semantic model storage format", "Publish to web", "Personal gateway", "Auto date/time"], "A",
 "The large semantic model storage format lets models grow beyond the default size limit, up to the capacity's limits, and improves XMLA write operations. The other options don't affect model size limits."),

single("S1",
 "The team wants to deploy metadata changes, such as new measures and partitions, to a published model with Tabular Editor, without republishing the .pbix. What must be enabled?",
 ["XMLA endpoint set to Read Write", "Publish to web", "Persistent filters on the semantic model", "Usage metrics"], "A",
 "External tools write to published models through the XMLA endpoint, which must be set to Read Write in the capacity settings. The other features don't let tools change models."),

single("S1",
 "In a deployment pipeline, the compare view shows that only one of 12 reports changed in Development. You want to deploy just that report to Test. What should you do?",
 ["Select only the changed report and deploy it", "Deploy all content every time", "Recreate the Test workspace", "Publish the report from Desktop directly to the Test workspace"], "A",
 "Deployment pipelines let you choose which items to deploy, so only the changed report moves to Test. Deploying everything works but risks overwriting other work. Publishing directly bypasses the pipeline."),

single("S1",
 "On Premium capacity, a Sales dashboard must show data no more than 15 minutes old. Why can't a 15-minute scheduled refresh be configured for an Import model, and what is a better fit?",
 ["Refresh runs in 30-minute slots; use DirectQuery or a hybrid table", "Premium allows only 8 refreshes per day; use a Pro workspace instead", "Scheduled refresh can't run on weekdays", "Import models can't be refreshed on Premium"], "A",
 "The scheduled refresh UI allows up to 48 refreshes a day, in 30-minute slots, on Premium or Fabric capacity. Fresher data calls for DirectQuery, a hybrid table, or API-driven refreshes. Eight a day is the Pro limit."),

# ---------------- S2 Secure and govern (3 + 1 in case)
single("S2",
 "A DirectQuery model uses an on-premises SQL Server that already applies row filtering based on the connecting user. Each report user must reach SQL Server with their own identity. What should you configure?",
 ["SSO for DirectQuery on the gateway data source", "A personal gateway", "RLS roles with USERNAME() that copy the SQL filters", "Publish to web"], "A",
 "With SSO for DirectQuery through the gateway, each user's identity is passed to the source, so the source's own security applies. Otherwise every query runs under the stored credentials. Recreating the rules as RLS duplicates logic. A personal gateway doesn't support DirectQuery."),

single("S2",
 "The organisation must stop all content from being shared with external guest users. Where is this controlled?",
 ["In the Fabric admin portal tenant settings", "In each report's settings", "In each workspace's licence mode and access settings", "In Power Query privacy levels"], "A",
 "Tenant settings in the admin portal control whether content can be shared with external users and what guests can do. Report, workspace and privacy-level settings don't govern external sharing for the whole organisation."),

single("S2",
 "One workspace app must show the Sales audience three reports and the Finance audience five, and some reports appear in both. Each group must not see the other's reports. What should you configure?",
 ["App audiences, each with the right reports and security group", "Two separate workspaces and apps, each with copies of the shared reports", "RLS roles named Sales and Finance", "Sensitivity labels"], "A",
 "Audiences in one app control which content each group of users can see, without duplicating reports. RLS filters rows inside a model rather than hiding reports. Labels classify content."),

# ---------------- Case study (P1, M3, V1, S2)
case("Tailspin Toys",
 "Tailspin Toys sells toys online. Orders are stored as Delta tables in a Fabric lakehouse and loaded hourly. Website click events stream into a Fabric Eventhouse (KQL database). Reports run on an F64 capacity. The executive overview page has 14 separate card visuals. Marketing analysts are Contributors in the model's workspace.",
 ["The live traffic page must show click activity that is no more than one minute old.",
  "The executive overview page must load faster. Performance Analyzer shows each card's DAX query takes about 300 ms, but most of the page's time is listed as Other.",
  "Marketing needs a visual of how many sessions move from product view to cart, to checkout, to purchase.",
  "Regional marketing analysts must see only their region's data, including in reports they build themselves."],
 [
  single("P1",
   "How should the live traffic page get its data?",
   ["DirectQuery to the KQL database with automatic page refresh", "Import from the Eventhouse with scheduled refresh every minute", "A CSV export every minute", "A dashboard tile with a data alert"], "A",
   "DirectQuery to the KQL database queries the latest events, and automatic page refresh (allowed at short intervals on capacity) re-queries regularly. Scheduled Import refresh can't run every minute. CSV exports and alerts don't provide live visuals."),
  single("M3",
   "Which change will most reduce the overview page's load time?",
   ["Replace the 14 cards with a few multi-value visuals", "Rewrite each card's measure with variables to cut its query time", "Convert the model to Import", "Add a forecast to each card"], "A",
   "Other is mostly time spent waiting for other visuals, so the number of visuals is the problem, not individual queries. Fewer visuals means fewer queries competing. The DAX is already fast, and storage mode isn't the bottleneck."),
  single("V1",
   "Which visual meets marketing's requirement?",
   ["Funnel chart", "Waterfall chart", "Scatter chart", "Treemap"], "A",
   "A funnel chart shows how many items reach each stage of a sequential process, making drop-off between stages visible. Waterfall charts show contributions to a total. Scatter charts compare two measures. Treemaps show part-to-whole."),
  single("S2",
   "You add dynamic RLS for regions, but analysts still see every region. What should you change?",
   ["Make the analysts Viewers with Build permission on the model", "Add the analysts to a second role with the same region filter", "Use USERNAME() instead of USERPRINCIPALNAME()", "Apply a sensitivity label"], "A",
   "Contributors, like Members and Admins, have edit rights and bypass RLS. As Viewers with Build permission, the analysts can create their own reports on the model, and RLS filters their data. The function choice and labels don't change the bypass."),
 ]),
]
