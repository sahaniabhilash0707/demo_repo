from model import single, multi, yesno, match, order, case

TITLE = "Core — reading SQL, KQL, DAX and PySpark"
SUBTITLE = "The same syllabus with more code on the page: you must read all four languages fluently, even if you only write one."
LEVEL = "Level 2 · Core"
CASE_NAME = "Tailspin Airlines"

ITEMS = [
# ---------------- M1 (5 + 1 in case)
multi("M1",
 "Which two workspace roles can manage OneLake security roles on a lakehouse?",
 ["Admin", "Member", "Contributor", "Viewer", "Any user with the Build permission"], "AB",
 "Admin and Member can manage OneLake security. Contributor can read and write data but can't manage OneLake security. Viewers and Build-permission users are the people those roles restrict."),

order("M1",
 "You must make sure each regional manager sees only their own region's rows when querying `dbo.Sales` in a Fabric Warehouse through T-SQL. Put the required actions in order.",
 ["Create a schema to hold the security objects",
  "Create an inline table-valued function that returns 1 when the row's Region matches the user's region",
  "Create a security policy that adds the function as a FILTER PREDICATE on dbo.Sales, with STATE = ON"],
 "Warehouse RLS is predicate-based. You create an inline table-valued function as the predicate, in a dedicated security schema (recommended practice), then bind it to the table with CREATE SECURITY POLICY ... ADD FILTER PREDICATE. Dynamic data masking and DENY on the table are different tools: one masks values and the other blocks the whole table.",
 extra=["Add dynamic data masking to the Region column", "DENY SELECT on dbo.Sales to the managers"]),

yesno("M1",
 "A OneLake security role with a row filter is defined on a lakehouse. For each user, select Yes if the row filter restricts what they see.",
 [("A user with the workspace Viewer role who is a member of the security role", True),
  ("A user with the workspace Contributor role", False),
  ("A user with no workspace role who was given access to the lakehouse through item sharing and is a member of the security role", True)],
 "Admin, Member and Contributor already have full read and write access to the workspace's data, so OneLake security roles don't restrict them. The filter applies to Viewers and to users who get access through item permissions."),

single("M1",
 "The compliance team requires every new or edited Power BI and Fabric item to carry a sensitivity label before it's saved. What should you configure?",
 ["A Purview label policy with mandatory labelling for Fabric", "Certification required in the tenant settings", "A OneLake security role on every workspace", "Workspace-level RLS with a label filter"], "A",
 "A Purview label policy that makes labelling mandatory forces users to choose a label when they create or edit content. Certification is an endorsement setting. OneLake security and RLS control access to data, not classification."),

single("M1",
 "A data governance team must be the only people who can certify items. What must happen first?",
 ["An admin enables certification in tenant settings for the team's security group", "Each workspace admin certifies items, then the team reviews them", "The team gets the Contributor role in every workspace", "A sensitivity label named Certified is published to the team"], "A",
 "Certification is turned on in the tenant settings, where the administrator names who may certify. Without that, nobody can certify. Workspace roles alone don't grant the right to certify, and a label is unrelated to endorsement."),

# ---------------- M2 (6)
yesno("M2",
 "A workspace is connected to a Git branch. For each statement about the source control pane, select Yes if it is true.",
 [("Commit pushes changes made in the workspace to the connected branch.", True),
  ("Update brings changes from the connected branch into the workspace.", True),
  ("Git integration promotes items from a Test workspace to a Production workspace with deployment rules.", False)],
 "Commit sends workspace changes to the branch, and Update applies branch changes to the workspace. Promoting items between stages with deployment rules is what deployment pipelines do. Git keeps the history and handles review, and pipelines handle promotion."),

multi("M2",
 "Which two can a deployment rule change when content is deployed to a target stage?",
 ["A semantic model's data source connection", "A parameter value in a semantic model or dataflow", "The DAX of a measure", "The RLS role membership", "The visuals on a report page"], "AB",
 "Deployment rules are data source rules and parameter rules, plus default lakehouse rules for notebooks. They let one artefact point at each stage's own sources. They don't edit DAX, role membership or report layout."),

order("M2",
 "You need to put an existing workspace under version control in Azure DevOps. Put the actions in order.",
 ["Open the workspace settings and choose Git integration",
  "Choose Azure DevOps and sign in",
  "Select the organisation, project, repository, branch and folder",
  "Connect and sync, then commit the workspace items to the branch"],
 "The connection is made in the workspace settings: pick the provider, choose the repo, branch and folder, then connect. After the first sync you commit to put the existing items into the branch. Deployment pipelines and .pbit files have nothing to do with setting up Git.",
 extra=["Create a deployment pipeline and assign the workspace", "Export each report as a .pbit file"]),

single("M2",
 "Impact analysis on a lakehouse shows 14 downstream semantic models and reports. You want their owners to know about a schema change scheduled for next week. Which built-in option helps?",
 ["Notify contacts from the impact analysis pane", "Add the owners to the workspace as Admins", "Apply a sensitivity label", "Create a deployment pipeline"], "A",
 "The impact analysis pane can email the contacts of the affected items. It's built for exactly this, before a breaking change. The other options don't communicate anything."),

match("M2",
 "Match each reuse requirement to the asset that meets it.",
 [("Teams need a starting report with the corporate theme, measures and layout, but no data", ".pbit template"),
  ("Analysts must open Desktop already pointed at the approved warehouse", ".pbids file"),
  ("Forty reports must use one governed set of measures and relationships", "Shared semantic model"),
  ("A model's definition must be diffable in pull requests", ".pbip project")],
 [".pbit template", ".pbids file", "Shared semantic model", ".pbip project", ".pbix file"],
 "A template carries the definition without data. A .pbids carries only a connection. A shared model is a live, governed dependency. A project stores definitions as text (TMDL and PBIR) for source control. A .pbix bundles everything, data included."),

yesno("M2",
 "A capacity's XMLA endpoint is set to Read only. For each task, select Yes if it is possible.",
 [("Run DAX queries against a semantic model from DAX Studio", True),
  ("Deploy a changed table partition from Tabular Editor", False),
  ("Connect SQL Server Management Studio and browse the model's metadata", True)],
 "Read lets client tools connect, browse metadata and run queries. Any change to the model, such as deploying, processing partitions or editing roles, needs the XMLA endpoint set to Read Write."),

# ---------------- P1 (7)
single("P1",
 "Security engineers need to search terabytes of firewall logs with free-text filters and time-window aggregations, with results in seconds. Which store fits best?",
 ["Eventhouse (KQL database)", "Warehouse", "Lakehouse Files area with CSV", "Fabric SQL database"], "A",
 "Eventhouses are built for high-volume, append-only log and time-series data. Columnar indexing and KQL operators like has, contains and bin make text search and time bucketing fast. Warehouses suit structured dimensional data. SQL databases are operational OLTP stores."),

single("P1",
 "A new line-of-business application needs a transactional relational database inside Fabric, and its data should be available in OneLake for analytics with no extra work. Which item should you create?",
 ["A SQL database in Fabric", "A warehouse with stored procedures", "A lakehouse with its SQL analytics endpoint", "An Eventhouse with update policies"], "A",
 "SQL database in Fabric is the operational (OLTP) database. Its data is replicated into OneLake as Delta automatically, ready for analytics. A warehouse is an analytical store, not a database for an application's day-to-day transactions."),

single("P1",
 "A user tries to create an external shortcut to an ADLS Gen2 account through an existing cloud connection and is refused. Other users can create shortcuts through the same connection. What is the most likely cause?",
 ["The user doesn't have permission to use that cloud connection", "ADLS Gen2 isn't a supported target", "Shortcuts can only be created by tenant administrators", "The lakehouse already has a shortcut"], "A",
 "External shortcuts sign in through a cloud connection, and only users who have permission on that connection can bind shortcuts to it. ADLS Gen2 is a supported target. Creating shortcuts doesn't need a tenant admin."),

single("P1",
 "A transformation merges 2 billion clickstream rows with session data and needs custom Python logic and unit tests. Which tool should you use?",
 ["A notebook (PySpark)", "A Dataflow Gen2", "The Visual Query Editor", "A KQL queryset"], "A",
 "Very large volumes, custom code and testability all point to Spark notebooks. Dataflow Gen2 is great for low-code, analyst-owned work at moderate scale. The Visual Query Editor and querysets only query data. They don't run transformation pipelines."),

multi("P1",
 "Which three are supported targets for an external OneLake shortcut?",
 ["Google Cloud Storage", "Dataverse", "Amazon S3", "An Azure SQL Database table", "A Salesforce object"], "ABC",
 "External shortcuts point at storage: ADLS Gen2, Blob Storage, Amazon S3 and S3-compatible storage, Google Cloud Storage, Dataverse, OneDrive or SharePoint, and on-premises locations through a gateway. Relational tables and SaaS objects are reached through mirroring or ingestion, not shortcuts."),

single("P1",
 "Point-of-sale events arrive in Azure Event Hubs. They must be routed with no code into an Eventhouse table and filtered on the way in. Which item should you use?",
 ["An Eventstream", "A Dataflow Gen2", "A deployment pipeline", "A Spark job definition"], "A",
 "An Eventstream takes in streaming sources such as Event Hubs, applies no-code transformations and routes the events to destinations including Eventhouse and lakehouse. Dataflows are batch tools, and deployment pipelines handle ALM."),

single("P1",
 "You created a cloud connection to a source database. A colleague must use it in their pipelines without ever seeing the credentials. What should you do?",
 ["Add the colleague to the connection with the User role", "Send them the credentials so they can create their own connection", "Give them the Admin role on your workspace", "Create a .pbids file that points at the database"], "A",
 "Connections are shareable objects with roles: Owner, User, and User with resharing. A User can choose the connection in their own items without seeing the stored credentials. Workspace roles don't govern connections."),

# ---------------- P2 (7 + 1 in case)
yesno("P2",
 "For each statement about a lakehouse's SQL analytics endpoint, select Yes if it is true.",
 [("You can create views on the endpoint.", True),
  ("You can run INSERT and UPDATE statements against the lakehouse's Delta tables through the endpoint.", False),
  ("Spark notebooks or Dataflow Gen2 are the usual ways to write data to the lakehouse tables.", True)],
 "The SQL analytics endpoint is read-only for table data, although you can create views and set permissions there. Lakehouse tables are written with Spark, with Dataflow Gen2 or pipelines that use a lakehouse destination, or with other tools that write Delta. T-SQL writes need a warehouse."),

single("P2",
 "In a lakehouse notebook you upsert changes into the Delta table `dim_customer`. Which clause inserts customers that don't exist in the target yet?",
 [".whenNotMatchedInsertAll()", ".whenMatchedDelete()", ".whenNotMatchedBySourceDelete()", ".whenMatchedUpdateAll()"], "A",
 "In a Delta MERGE, the not-matched clause handles source rows that have no match in the target, which here means new customers to insert. whenMatchedUpdateAll updates existing customers. NotMatchedBySource handles target rows that are missing from the source.",
 code="""from delta.tables import DeltaTable
tgt = DeltaTable.forName(spark, "dim_customer")
(tgt.alias("t")
    .merge(updates.alias("s"), "t.CustomerID = s.CustomerID")
    .whenMatchedUpdateAll()
    ______
    .execute())"""),

single("P2",
 "In PySpark, you need to keep only the latest row per OrderID based on `ModifiedAt`. Complete the expression.",
 ["F.row_number().over(Window.partitionBy(\"OrderID\").orderBy(F.col(\"ModifiedAt\").desc()))",
  "F.rank().over(Window.orderBy(F.col(\"ModifiedAt\").desc()))",
  "F.row_number().over(Window.partitionBy(\"ModifiedAt\").orderBy(\"OrderID\"))",
  "F.max(\"ModifiedAt\").over(Window.partitionBy(\"OrderID\"))"], "A",
 "row_number over a window partitioned by the key and ordered newest-first gives 1 to the latest row. Then you filter rn == 1. A window without a partition by OrderID ranks across all orders. Partitioning by ModifiedAt groups the wrong rows. max over the partition returns a timestamp, not a row number to filter on.",
 code="""w_rn = ______
latest = df.withColumn("rn", w_rn).filter("rn = 1").drop("rn")"""),

single("P2",
 "A Dataflow Gen2 imports a text column holding dates in day/month/year order, such as 31/03/2026. Changing the type to Date gives errors. What should you do?",
 ["Use Change type > Using locale, with a day/month/year locale such as English (UK)", "Change the type to Date, then remove the rows that have errors", "Leave the column as text and convert it in the semantic model", "Split the column by the / delimiter and keep only the first part"], "A",
 "Change type using locale tells Power Query how to read the text, so 31/03/2026 is understood as 31 March. Removing error rows loses data. Leaving it as text pushes the problem downstream."),

single("P2",
 "You are designing a new fact table for order lines in the gold layer. What should you decide first?",
 ["The grain: what exactly one row represents", "The visuals the first report will use", "The number of partitions in the semantic model", "The DAX measures that will reference it"], "A",
 "Declaring the grain is the first step in dimensional design. It decides which dimensions apply and which measures are additive. Everything else follows from it."),

single("P2",
 "Some fact rows arrive with a CustomerID that doesn't exist in DimCustomer yet. Reports must not lose these sales. What is the recommended gold-layer handling?",
 ["Map them to an Unknown member in DimCustomer, such as key -1", "Delete the fact rows until the customer arrives", "Leave the fact's customer key NULL for now", "Move them to a separate fact table for unmatched rows"], "A",
 "An Unknown (or inferred) member keeps the rows joinable, so totals stay correct and the relationship stays valid. NULL keys turn into a blank member and can break Direct Lake relationship rules. Deleting the rows understates sales."),

single("P2",
 "Which T-SQL creates a view that the semantic model can read, exposing only completed orders with a derived Year column?",
 ["CREATE VIEW gold.vCompletedOrders AS SELECT o.*, YEAR(o.OrderDate) AS OrderYear FROM gold.FactOrders o WHERE o.Status = 'Completed';",
  "CREATE TABLE gold.vCompletedOrders AS SELECT * FROM gold.FactOrders;",
  "CREATE PROCEDURE gold.vCompletedOrders AS SELECT * FROM gold.FactOrders WHERE Status = 'Completed';",
  "ALTER TABLE gold.FactOrders ADD OrderYear AS YEAR(OrderDate);"], "A",
 "A view encapsulates the filter and the derived column and is always current. A CTAS creates a copy with neither. A procedure can't be selected from like a table. A computed column changes the table itself and doesn't filter anything."),

# ---------------- P3 (5 + 1 in case)
yesno("P3",
 "For each statement about the Visual Query Editor, select Yes if it is true.",
 [("It's available on a warehouse and on a lakehouse's SQL analytics endpoint.", True),
  ("It generates T-SQL that you can view.", True),
  ("It can only run KQL queries.", False)],
 "The Visual Query Editor is a no-code, Power Query-style canvas over warehouses and SQL analytics endpoints. It generates SQL you can inspect, and you can save the result as a view. KQL is written in querysets."),

single("P3",
 "Which KQL query shows the distinct number of users per day as a line chart?",
 ["PageViews | summarize Users = dcount(UserId) by bin(Timestamp, 1d) | render timechart",
  "PageViews | distinct UserId, bin(Timestamp, 1d) | render piechart",
  "PageViews | summarize count() by UserId, bin(Timestamp, 1d) | render timechart",
  "PageViews | project Users = dcount(UserId), Timestamp | render timechart"], "A",
 "dcount gives a distinct count, bin groups by day, and render timechart draws a line over time. count() counts page views, not distinct users. distinct returns the unique values themselves, not a count. project can't aggregate."),

single("P3",
 "A query must return each category's revenue and its share of all revenue, in one pass. Which expression gives the share?",
 ["SUM(Revenue) * 1.0 / SUM(SUM(Revenue)) OVER ()", "SUM(Revenue) / COUNT(*)", "RANK() OVER (ORDER BY SUM(Revenue))", "SUM(Revenue) OVER (PARTITION BY Category)"], "A",
 "Inside a GROUP BY query, SUM(SUM(Revenue)) OVER () applies a window over the grouped rows, which gives the grand total. Dividing each group's sum by it gives the share. Multiplying by 1.0 avoids integer division. The other options give an average, a rank or a per-category total.",
 code="""SELECT Category,
       SUM(Revenue) AS Revenue,
       ______ AS ShareOfTotal
FROM gold.FactSales f JOIN gold.DimProduct p ON p.ProductKey = f.ProductKey
GROUP BY Category;"""),

single("P3",
 "Which DAX query returns sales by month for 2026 only?",
 ["EVALUATE SUMMARIZECOLUMNS('Date'[Month], TREATAS({2026}, 'Date'[Year]), \"Sales\", [Total Sales])",
  "EVALUATE FILTER([Total Sales], 'Date'[Year] = 2026)",
  "EVALUATE CALCULATE([Total Sales], 'Date'[Year] = 2026)",
  "SUMMARIZECOLUMNS('Date'[Month], \"Sales\", [Total Sales]) WHERE 'Date'[Year] = 2026"], "A",
 "SUMMARIZECOLUMNS accepts filter tables as arguments, and TREATAS({2026}, 'Date'[Year]) is one. FILTER needs a table, not a measure. CALCULATE returns a scalar. DAX queries have no WHERE clause."),

single("P3",
 "A warehouse query must label each order as Small (under 100), Medium (100 to 999) or Large (1,000 or more). Which construct should you use?",
 ["A CASE expression", "A PIVOT", "A CROSS APPLY to a table-valued function", "A recursive CTE"], "A",
 "CASE WHEN ... THEN ... ELSE ... END is the standard way to bucket values in a SELECT. PIVOT turns rows into columns. The other two are much more complex than this needs."),

# ---------------- S1 (6)
single("S1",
 "Budgets are stored at the Category × Month grain, while the Product dimension is at product grain. You must filter budgets by Product[Category] without creating a new table. What should you do?",
 ["A many-to-many relationship on Category, filtering from Product to Budget", "A one-to-many relationship from Budget to Product on Category", "Duplicate each budget row for every product in the category", "Merge the Budget table into the Sales fact"], "A",
 "A many-to-many relationship (many-to-many cardinality) lets you relate facts stored at a higher grain to a dimension on a non-unique column. Filtering in a single direction keeps it predictable. Duplicating budget rows inflates totals, and merging facts with different grains breaks both."),

single("S1",
 "Complete the calculation item for year-to-date so it works with any measure.",
 ["CALCULATE(SELECTEDMEASURE(), DATESYTD('Date'[Date]))", "TOTALYTD([Sales], 'Date'[Date])", "CALCULATE(SELECTEDMEASURENAME(), DATESYTD('Date'[Date]))", "CALCULATE(SELECTEDMEASURE(), ALL('Date'))"], "A",
 "Calculation items use SELECTEDMEASURE() so the same logic applies to whatever measure is in the visual, and DATESYTD gives the year-to-date dates. A hard-coded [Sales] only works for one measure. SELECTEDMEASURENAME returns text. ALL('Date') removes the date filter instead of applying YTD.",
 code="""-- Calculation group: Time Intelligence
-- Calculation item: YTD
______"""),

single("S1",
 "You create a field parameter in Power BI Desktop to let users switch between three measures. What does Desktop generate?",
 ["A calculated table that references each field with NAMEOF()", "A calculation group with one item per field", "Three bookmarks and a bookmark navigator", "A table built with GENERATESERIES"], "A",
 "Field parameters are calculated tables with rows like (\"Revenue\", NAMEOF([Revenue]), 0). The slicer drives which field the visual shows. GENERATESERIES is what what-if parameters use."),

single("S1",
 "Which measure gives each product a rank by revenue among the products visible in the visual, with ties sharing a rank and no gaps?",
 ["RANK(DENSE, ALLSELECTED('Product'[Name]), ORDERBY([Revenue], DESC))", "ROWNUMBER(ALL('Product'[Name]), ORDERBY([Revenue], DESC))", "RANK(SKIP, ALL(Sales), ORDERBY(Sales[Qty]))", "INDEX(1, ALLSELECTED('Product'[Name]), ORDERBY([Revenue], DESC))"], "A",
 "RANK with DENSE gives tied values the same rank with no gaps. ALLSELECTED limits the ranking to what the user can see. ROWNUMBER never ties. INDEX returns a row, not a rank. Ranking over all Sales rows by quantity answers a different question."),

yesno("S1",
 "For each statement about relationships in a semantic model, select Yes if it is true.",
 [("Setting every relationship to filter in both directions can create ambiguous filter paths and slow queries down.", True),
  ("A model can contain several relationships between the same two tables, but only one can be active.", True),
  ("Relationships in a star schema normally go from the fact table (one side) to the dimension (many side).", False)],
 "Use bidirectional filtering sparingly, because it can cause ambiguity and expensive queries. You can have several relationships between two tables, with one active and the rest used through USERELATIONSHIP. In a star schema the dimension is the one side and the fact is the many side."),

single("S1",
 "Month names in a visual sort alphabetically (April, August, December, …). What should you do?",
 ["Set Sort by column on MonthName to MonthNumber", "Rename the months with numeric prefixes", "Create a calculated table of months", "Change MonthName to the Date data type"], "A",
 "Sort by column orders a text column by another column, here the month number. Prefixes are a workaround that spoils the labels. MonthName isn't a date."),

# ---------------- S2 (5 + 1 in case)
single("S2",
 "You want to turn on query scale-out (read-only replicas) for a busy semantic model. What is a prerequisite?",
 ["The model must use large storage format", "The model must use DirectQuery mode", "The workspace must be Git-connected", "The model must not have RLS roles"], "A",
 "Query scale-out requires large semantic model storage format on the model. RLS and Git integration are unaffected."),

single("S2",
 "A measure calculates `[Sales]` for the prior year three times in a long IF expression. What is the simplest way to improve both performance and readability?",
 ["Store the prior-year value in a VAR and reuse it", "Wrap each prior-year call in IFERROR", "Turn the prior-year logic into a calculated column", "Make the Date relationship bidirectional"], "A",
 "A variable is evaluated once in its context and then reused, so the calculation doesn't run three times. IFERROR hides errors and blocks some optimisations. Calculated columns are stored per row and can't respond to filters the way a measure does."),

single("S2",
 "An Import model is far larger than expected. VertiPaq Analyzer shows dozens of hidden LocalDateTable tables. What should you change?",
 ["Turn off Auto date/time and use one shared date table", "Turn on large semantic model storage format", "Relate each LocalDateTable to the main date table", "Switch every date table to Dual storage mode"], "A",
 "Auto date/time creates a hidden date table for every date column, which inflates the model. Turning it off and using a single marked date table removes them. Large model format raises the size limit but doesn't fix the bloat, and relating or changing the storage mode of the hidden tables doesn't remove them."),

single("S2",
 "An ETL pipeline writes several gold tables one after another. Reports must never show a mix of old and new tables halfway through the load. What should you configure for the Direct Lake model?",
 ["Turn off automatic updates and refresh the model from the pipeline at the end", "Turn on automatic page refresh every minute during the load", "Set DirectLakeBehavior to DirectQueryOnly while the load runs", "Switch the model to Import with a nightly refresh"], "A",
 "With automatic updates on, the model can reframe while the load is still running. Turning them off and triggering a refresh (framing) at the end of the pipeline makes all the tables move to their new versions together. That keeps reports consistent without copying any data."),

single("S2",
 "For good Direct Lake performance, what row-group size does Microsoft's table-maintenance guidance recommend for gold Delta tables?",
 ["Roughly 1 to 16 million rows per row group", "Fewer than 10,000 rows per row group", "Exactly one row group per file regardless of size", "Over 1 billion rows per row group"], "A",
 "Microsoft's guidance aims for row groups of about 1 to 16 million rows, with large target file sizes. Tiny row groups create many segments and raise transcoding overhead."),

# ---------------- Case study (M1, P2, P3, S2)
case("Tailspin Airlines",
 "Tailspin Airlines streams aircraft status messages into an Eventhouse, KQL_Ops. Bookings land in a lakehouse, LH_Bookings, through a PySpark pipeline, and a warehouse, WH_Gold, holds the dimensional model. An Import semantic model has DAX RLS roles that filter by station (airport).\n\nAll 120 station managers have the workspace Member role so they could “see everything quickly” during the launch. The flight-status report page has 28 visuals and takes 20 seconds to load.",
 ["R1. Station managers must see only their own station's data in reports.",
  "R2. Missing tail numbers in WH_Gold must be shown as 'UNKNOWN'.",
  "R3. Operations needs the latest status message per aircraft from KQL_Ops.",
  "R4. The flight-status page must load faster without losing information."],
 [
  single("M1", "The RLS roles are set up correctly, but managers still see every station. What must you change to satisfy R1?",
   ["Change the managers from Member to Viewer, or to app access", "Add the managers to a second, stricter RLS role", "Apply a Confidential sensitivity label to the model", "Republish the model so the roles take effect"], "A",
   "RLS doesn't apply to workspace Admins, Members or Contributors, who can edit the model. Moving the managers to Viewer, or to app consumers, makes the existing roles take effect."),
  single("P2", "Which T-SQL expression satisfies R2 in a view over the aircraft dimension?",
   ["COALESCE(TailNumber, 'UNKNOWN')", "NULLIF(TailNumber, 'UNKNOWN')", "IIF(ISNUMERIC(TailNumber) = 1, TailNumber, NULL)", "TRIM(ISNULL(TailNumber, ''))"], "A",
   "COALESCE returns the first non-null value, so NULL tail numbers become 'UNKNOWN'. NULLIF does the reverse: it turns 'UNKNOWN' into NULL. TRIM(ISNULL(..., '')) gives an empty string, not 'UNKNOWN'. The IIF/ISNUMERIC expression creates more NULLs instead of fewer."),
  single("P3", "Which KQL query satisfies R3?",
   ["AircraftStatus | summarize arg_max(Timestamp, *) by TailNumber", "AircraftStatus | top 1 by Timestamp desc", "AircraftStatus | distinct TailNumber, Status", "AircraftStatus | summarize max(Timestamp) by Status"], "A",
   "arg_max(Timestamp, *) returns the whole row with the latest timestamp for each tail number. top 1 returns only the single latest row across all aircraft. distinct returns every combination seen, not the latest. max(Timestamp) by Status groups by the wrong column and returns no other fields."),
  multi("S2", "Which two actions best address R4?",
   ["Use Performance Analyzer to find the slowest visuals and tune their DAX", "Cut the number of visuals, for example by combining cards into one multi-row card or moving detail to a drill-through page", "Add a slicer for every column", "Make every relationship bidirectional", "Turn off query caching"], "AB",
   "Every visual sends at least one query, so fewer visuals means less work. Performance Analyzer shows which visuals cost the most. More slicers add queries, and bidirectional relationships make queries more expensive."),
 ]),
]
