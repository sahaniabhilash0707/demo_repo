from model import single, multi, yesno, match, order, case

TITLE = "Advanced — mixed scenarios"
SUBTITLE = "Every sub-area at full difficulty, with questions that cross domains the way the real paper does."
LEVEL = "Level 4 · Advanced"
CASE_NAME = "Margie's Travel"

ITEMS = [
# ---------------- M1 (5 + 1 in case)
single("M1",
 "A lakehouse contains an external shortcut to an ADLS Gen2 container, created with a cloud connection that uses a service principal. When a workspace Viewer reads data through that shortcut, which identity does ADLS Gen2 check?",
 ["The credentials of the shortcut's cloud connection", "The Viewer's own Entra identity, checked against ADLS ACLs", "The identity of the workspace's Admin", "None; the storage account must allow anonymous access"], "A",
 "External shortcuts pass authorisation to the connection's credential when they call the target. That's why you control end users on the Fabric side, with workspace roles, item permissions and OneLake security. Internal shortcuts are different: they check the calling user's identity."),

yesno("M1",
 "For each statement about workspace roles, select Yes if it is true.",
 [("Only the Admin role can delete the workspace.", True),
  ("A Member can add other users as workspace Admins.", False),
  ("A Viewer can create a new notebook in the workspace.", False)],
 "Admin is the only role that can delete the workspace or manage Admins. Members can add Members, Contributors and Viewers. Viewers can't create items."),

single("M1",
 "Workspace Viewers can query a lakehouse through its SQL analytics endpoint. They must be blocked from querying one table, dbo.Salaries, through SQL, while every other table stays available. What should you do?",
 ["DENY SELECT ON dbo.Salaries to the Viewers' group", "Move Salaries to the Files area of the lakehouse", "A Highly Confidential label on the Salaries table", "REVOKE CONNECT from the Viewers' group"], "A",
 "The SQL analytics endpoint supports granular T-SQL permissions such as GRANT and DENY on objects. Deleting the table or removing the users goes much too far, and labels don't block queries."),

single("M1",
 "Reports built on a semantic model labelled Highly Confidential should get the same label automatically. What should you turn on?",
 ["Downstream label inheritance in the tenant settings", "Certification of the semantic model", "A deployment rule that copies the label", "A mandatory labelling policy for reports"], "A",
 "With downstream inheritance, a label on an upstream item such as a semantic model is applied to downstream content, such as reports and dashboards built on it. A mandatory labelling policy makes authors pick a label but doesn't make it match the model's. Certification and deployment rules don't affect labels."),

single("M1",
 "A lakehouse table is protected with RLS defined at its SQL analytics endpoint. A group of analysts was also given ReadAll on the lakehouse. What is the risk?",
 ["They can read all rows through Spark, bypassing the SQL RLS", "None; SQL RLS is enforced for Spark reads too", "ReadAll replaces ReadData, so SQL access stops", "Their SQL queries fall back to DirectQuery"], "A",
 "SQL endpoint security only governs queries that go through the SQL endpoint. ReadAll gives direct OneLake access, where SQL RLS doesn't apply. Use OneLake security for rules that must hold across engines, or don't grant ReadAll."),

# ---------------- M2 (6)
multi("M2",
 "Which two conditions must hold before you can deploy changes to a semantic model through the XMLA endpoint?",
 ["The workspace is on a Fabric, Premium or Premium Per User capacity", "The XMLA endpoint is set to Read Write for that capacity", "The model uses DirectQuery", "The workspace is connected to Git", "The deploying user has the Viewer role"], "AB",
 "XMLA write needs a supported capacity and the Read Write setting, plus enough permission on the workspace. Storage mode and Git integration don't matter. Viewers can't write."),

single("M2",
 "Two workspaces, Finance-Dev and HR-Dev, must keep their items in the same Git repository without mixing their files. How should you connect them?",
 ["Connect each workspace to the repository with a different Git folder (directory)", "Create two repositories; one repository can't hold several workspaces", "Connect both workspaces to the repository root", "Use one workspace for both teams"], "A",
 "When you connect a workspace, you choose a branch and a folder, so several workspaces can share one repository in separate folders. Connecting both to the root would mix and overwrite their files."),

single("M2",
 "You want to deploy a report and every item it depends on (its semantic model and the lakehouse behind it) without picking each one by hand. Which deployment pipeline feature helps?",
 ["Select related", "Compare", "Deployment history", "Backward deployment"], "A",
 "Select related adds an item's dependencies to the selection, so a consistent set is deployed together. Compare shows differences between stages, and history shows past deployments."),

order("M2",
 "You need a reusable report template that asks for the server and database when it's opened. Put the steps in order.",
 ["Create Power Query parameters named Server and Database",
  "Change the source step to use the parameters instead of fixed values",
  "Save the report as a Power BI template (.pbit)",
  "Distribute the .pbit file to report authors"],
 "Parameters make the source configurable. Saving as a .pbit removes the data and keeps the parameter prompts, so authors fill in values when they open it. A .pbids or a deployment rule is a different mechanism.",
 extra=["Create a .pbids file with the server name", "Add a deployment rule for the template"]),

match("M2",
 "Match each file type to its description.",
 [("Report, model and data in one binary file", ".pbix"),
  ("A folder of text definitions (TMDL and PBIR) for source control", ".pbip"),
  ("Report and model definitions with no data, opened with parameter prompts", ".pbit"),
  ("A JSON file with data-source connection details only", ".pbids")],
 [".pbix", ".pbip", ".pbit", ".pbids", ".abf"],
 "Each reuse and ALM format carries something different. .abf is an Analysis Services backup file, used when backing up and restoring through XMLA, and doesn't fit any of these descriptions."),

single("M2",
 "A large Import semantic model must be moved, with its data, to a workspace on a capacity in another region, without a full re-refresh from source. What can you use?",
 ["XMLA backup to .abf and restore, with ADLS Gen2 storage attached", "A deployment pipeline between the two workspaces", "Git integration, syncing both workspaces to one branch", "Export each table to CSV and re-import it"], "A",
 "Backup and restore of semantic models works through XMLA and needs the workspaces connected to an ADLS Gen2 account. The .abf file includes the data. Pipelines and Git move metadata only."),

# ---------------- P1 (6 + 1 in case)
single("P1",
 "Data scientists will train models in Spark on two years of semi-structured JSON telemetry kept at rest. Nobody needs sub-second interactive queries. Where should the history be stored?",
 ["A lakehouse, as files or Delta tables", "An Eventhouse with a long retention policy", "A warehouse with JSON columns", "An Import semantic model"], "A",
 "Spark-first machine learning over semi-structured history fits a lakehouse. An Eventhouse is optimised for low-latency queries over streaming data. Warehouses hold structured tables and aren't built for Spark workloads."),

single("P1",
 "A data owner wants one view of their own items' sensitivity label coverage, endorsement and governance recommendations. Which surface provides this?",
 ["The Govern tab in the OneLake catalog", "The Real-Time hub", "Deployment pipeline compare", "The DAX query view"], "A",
 "The OneLake catalog has a Govern tab with insights and recommended actions about the items you own, such as labelling and endorsement. The other surfaces are for streaming data, ALM or querying."),

yesno("P1",
 "For each statement about Eventstreams, select Yes if it is true.",
 [("An Eventstream can apply no-code transformations, such as filters and aggregations, to events in flight.", True),
  ("One Eventstream can send events to more than one destination, such as an Eventhouse and a lakehouse.", True),
  ("An Eventstream needs custom C# code to read from Azure Event Hubs.", False)],
 "Eventstreams are a no-code canvas for streaming: sources such as Event Hubs and IoT Hub, inline transformations, and several destinations. Code is optional, not required."),

single("P1",
 "A production Spark batch job lives in .py files with command-line arguments and a main entry point, and the team doesn't want it in an interactive notebook. Which Fabric item should run it?",
 ["A Spark job definition", "A KQL queryset", "A Dataflow Gen2", "The Visual Query Editor"], "A",
 "A Spark job definition runs packaged Spark applications (Python, Scala or Java files) with arguments, on a schedule or from a pipeline. Notebooks are for interactive work. The other options aren't Spark runtimes."),

single("P1",
 "In a pipeline, a notebook must run only if the Copy activity succeeds, and a Teams message must be sent only if the Copy fails. How do you configure this?",
 ["Notebook on the Copy's On success path; Teams on its On failure path", "All three activities in parallel, with no dependencies", "Notebook and Teams both on the Copy's On completion path", "Teams on the Notebook's On failure path"], "A",
 "Activity dependency conditions (on success, on failure, on completion, on skip) control the flow in a pipeline. On completion runs whatever the outcome, and parallel activities ignore it. Hanging Teams off the notebook's failure path never fires when the Copy itself fails."),

single("P1",
 "An operational SQL database in Fabric runs an application. Analysts want to query its data for reporting without slowing the application. What should they use?",
 ["Its replicated copy in OneLake, via the SQL analytics endpoint", "The application's own database connection string", "A nightly CSV export into a lakehouse", "A KQL queryset connected directly to the database"], "A",
 "SQL database in Fabric replicates its data to OneLake as Delta in near real time. Analytical queries can use that copy through the SQL analytics endpoint or Direct Lake, which keeps the load off the transactional database."),

# ---------------- P2 (7 + 1 in case)
single("P2",
 "A warehouse load updates FactSales and inserts audit rows into etl.LoadLog. Both changes must succeed or fail together. What should you do?",
 ["Wrap both in BEGIN TRANSACTION ... COMMIT, rolling back on error", "Run them in two pipeline activities linked On success", "Run both on a lakehouse SQL analytics endpoint", "Run the audit insert first, then the update"], "A",
 "The Fabric Warehouse supports ACID transactions across several tables, so an explicit transaction gives all-or-nothing behaviour. Separate activities can partly fail, and the SQL analytics endpoint can't write."),

single("P2",
 "In PySpark, you need a column Tier that is \"Gold\" when Spend > 10000, \"Silver\" when Spend > 1000, and \"Bronze\" otherwise. Which expression is correct?",
 ["F.when(F.col(\"Spend\") > 10000, \"Gold\").when(F.col(\"Spend\") > 1000, \"Silver\").otherwise(\"Bronze\")", "F.expr(\"IF(Spend > 1000, 'Silver', IF(Spend > 10000, 'Gold', 'Bronze'))\")", "F.when(F.col(\"Spend\") > 1000, \"Silver\").when(F.col(\"Spend\") > 10000, \"Gold\").otherwise(\"Bronze\")", "F.when(F.col(\"Spend\") > 10000, \"Gold\").otherwise(\"Silver\").otherwise(\"Bronze\")"], "A",
 "Chained when and otherwise is how PySpark writes CASE logic. The conditions are checked in order, so the highest threshold has to come first. Testing > 1000 first labels every big spender Silver, in the when chain and in the nested IF alike. otherwise can only appear once."),

single("P2",
 "A string column holds dates such as \"14-03-2026\" (dd-MM-yyyy). Which PySpark expression converts it to a date?",
 ["F.to_date(\"OrderDateText\", \"dd-MM-yyyy\")", "F.to_date(\"OrderDateText\", \"yyyy-MM-dd\")", "F.col(\"OrderDateText\").cast(\"int\")", "F.date_format(\"OrderDateText\", \"dd-MM-yyyy\")"], "A",
 "to_date with a pattern that matches the input reads it correctly. The wrong pattern gives nulls. date_format converts a date to text, which is the opposite direction."),

match("P2",
 "Match each slowly changing dimension type to its behaviour.",
 [("The attribute never changes after the row is first loaded", "Type 0"),
  ("The old value is overwritten and no history is kept", "Type 1"),
  ("A new row is added with its own surrogate key and validity dates", "Type 2"),
  ("A PreviousValue column keeps one prior value alongside the current one", "Type 3")],
 ["Type 0", "Type 1", "Type 2", "Type 3", "Type 7"],
 "Type 0 keeps the original value, Type 1 overwrites, Type 2 versions rows, and Type 3 keeps limited history in extra columns. Type 7 is a hybrid that combines Type 1 and Type 2 access paths, and it doesn't fit any of these descriptions."),

single("P2",
 "In a notebook you need a 7-day rolling sum of Amount per store, ordered by date, with one row per store per day. Which window specification is correct?",
 ["Window.partitionBy(\"StoreID\").orderBy(\"Date\").rowsBetween(-6, 0)", "Window.orderBy(\"StoreID\").rowsBetween(0, 7)", "Window.partitionBy(\"Date\").orderBy(\"StoreID\")", "Window.partitionBy(\"StoreID\").rowsBetween(-7, 7)"], "A",
 "Partition by store, order by date, and take the current row plus the six before it, which is seven days when there's one row per day. The other specifications partition or frame the rows wrongly."),

yesno("P2",
 "For each statement about views, functions and stored procedures in Fabric, select Yes if it is true.",
 [("You can create stored procedures that write data in a Fabric Warehouse.", True),
  ("You can create views on a lakehouse's SQL analytics endpoint.", True),
  ("A stored procedure on a lakehouse's SQL analytics endpoint can INSERT rows into the lakehouse's Delta tables.", False)],
 "The warehouse supports views, functions and stored procedures with full DML. The lakehouse SQL analytics endpoint supports views and other read-only objects, but it can't modify Delta tables. Those are written with Spark or other Delta writers."),

single("P2",
 "Phone numbers arrive in mixed formats, such as \"(020) 555-0101\" and \"020.555.0101\". The silver table must store digits only. Which PySpark expression does this?",
 ["F.regexp_replace(\"Phone\", \"[^0-9]\", \"\")", "F.translate(\"Phone\", \"()\", \"\")", "F.regexp_extract(\"Phone\", \"[0-9]+\", 0)", "F.regexp_replace(\"Phone\", \"[0-9]\", \"\")"], "A",
 "regexp_replace with the pattern [^0-9] removes every character that isn't a digit. The [0-9] pattern does the opposite and deletes the digits. translate removes only the brackets. regexp_extract returns only the first run of digits, such as 020."),

# ---------------- P3 (6)
single("P3",
 "A query must return the top five products by revenue, plus any product tied with the fifth. Which clause should you use?",
 ["SELECT TOP (5) WITH TIES ... ORDER BY Revenue DESC", "SELECT TOP (5) ... ORDER BY Revenue DESC", "SELECT TOP (5) PERCENT ...", "SELECT DISTINCT TOP (5) ..."], "A",
 "WITH TIES returns extra rows that tie with the last row on the ORDER BY value. Plain TOP (5) cuts off at exactly five. PERCENT returns a share of the rows."),

single("P3",
 "Which KQL expression returns the percentage of failed requests per hour?",
 ["summarize FailedPct = 100.0 * countif(Status == \"Failed\") / count() by bin(Timestamp, 1h)", "summarize FailedPct = 100.0 * dcount(Status) / count() by bin(Timestamp, 1h)", "summarize FailedPct = countif(Status == \"Failed\") by bin(Timestamp, 1h)", "where Status == \"Failed\" | summarize FailedPct = 100.0 * count() / count() by bin(Timestamp, 1h)"], "A",
 "countif counts the rows that meet a condition, and dividing by count() gives the failure share per hour. Using 100.0 avoids integer division. dcount counts distinct status values. Filtering to failures first makes both counts the same, so the result is always 100. countif alone gives a count, not a percentage."),

single("P3",
 "Which KQL query finds the busiest hour of the day (0–23) across the last 30 days?",
 ["Events | where Timestamp > ago(30d) | summarize Events = count() by Hour = hourofday(Timestamp) | top 1 by Events desc", "Events | where Timestamp > ago(30d) | summarize Events = count() by bin(Timestamp, 1h) | top 1 by Events desc", "Events | where Timestamp > ago(30d) | summarize Events = dcount(hourofday(Timestamp)) | take 1", "Events | where Timestamp > ago(30d) | extend Hour = hourofday(Timestamp) | top 1 by Hour desc"], "A",
 "hourofday pulls out the hour number, so all days add up into 24 groups, and top 1 picks the busiest. bin(Timestamp, 1h) makes 720 separate hourly buckets, so it finds the busiest single hour, not hour of day. Sorting by Hour returns hour 23. dcount of the hour gives 24."),

single("P3",
 "Which DAX query returns the rows of the Customer table for customers who bought something in 2026?",
 ["EVALUATE CALCULATETABLE(VALUES(Customer[CustomerKey]), 'Date'[Year] = 2026, Sales)", "EVALUATE FILTER(Customer, 'Date'[Year] = 2026)", "EVALUATE CALCULATE(COUNTROWS(Customer), 'Date'[Year] = 2026)", "EVALUATE Customer WHERE 'Date'[Year] = 2026"], "A",
 "CALCULATETABLE evaluates the table expression with the year filter applied. Passing Sales as a filter (an expanded-table filter) limits the result to customers that have sales rows in that context. The FILTER query references a Date column that isn't in the row context. CALCULATE returns a scalar. DAX has no WHERE clause."),

single("P3",
 "You must find every column named like '%Email%' across all tables in a warehouse, for a privacy review. Which query should you run?",
 ["SELECT TABLE_SCHEMA, TABLE_NAME, COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE COLUMN_NAME LIKE '%Email%';", "SELECT * FROM sys.dm_exec_requests WHERE command LIKE '%Email%';", "SELECT s.name, t.name FROM sys.tables t JOIN sys.schemas s ON s.schema_id = t.schema_id WHERE t.name LIKE '%Email%';", "SELECT TABLE_SCHEMA, TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME LIKE '%Email%';"], "A",
 "INFORMATION_SCHEMA.COLUMNS (or sys.columns) lists the column metadata for every table and view. sys.tables and INFORMATION_SCHEMA.TABLES search table names, not column names. dm_exec_requests shows running requests, not schema."),

single("P3",
 "A warehouse in Workspace A must query a table in a lakehouse in Workspace B. A three-part name fails because cross-database queries only reach items in the same workspace. What is the supported approach?",
 ["Shortcut the table into a Workspace A lakehouse, then use a three-part name", "Use a four-part name that starts with Workspace B's name", "Use OPENROWSET with Workspace B's SQL endpoint address", "Add Workspace B's endpoint as a linked server"], "A",
 "Cross-database queries work within a workspace. A shortcut brings the other workspace's table into a local lakehouse without copying it, and from there it can be queried by name. Linked servers, OPENROWSET against another endpoint and workspace-qualified four-part names aren't supported."),

# ---------------- S1 (6)
multi("S1",
 "Which two are good reasons to choose Direct Lake for a new semantic model?",
 ["The gold data already sits as Delta tables in OneLake", "You want Import-like query speed without a data-copying refresh", "The data is in an on-premises database reached through a gateway", "The workspace is on shared (Pro) capacity", "Visuals must read live from an external Oracle database"], "AB",
 "Direct Lake is for Delta data in OneLake when you want fast, VertiPaq-class queries without copy-based refreshes. It needs a Fabric capacity, can't use gateways, and doesn't query external databases live."),

single("S1",
 "A product's price changes over time, and the PriceHistory table holds one row per product per change date. A measure must return the latest price within the selected period. Which function fits?",
 ["LASTNONBLANKVALUE('Date'[Date], MAX(PriceHistory[Price]))", "CALCULATE(SUM(PriceHistory[Price]), LASTDATE('Date'[Date]))", "FIRSTNONBLANKVALUE('Date'[Date], MAX(PriceHistory[Price]))", "AVERAGEX(VALUES('Date'[Date]), MAX(PriceHistory[Price]))"], "A",
 "LASTNONBLANKVALUE returns the expression's value at the last date that has data in context, which gives the latest price. LASTDATE takes the period's last calendar date, which is blank if the price didn't change that day. FIRSTNONBLANKVALUE gives the earliest price. An average of daily prices isn't the latest price."),

single("S1",
 "A disconnected table, SelectedRegions, drives a slicer. A measure must filter Sales by the regions chosen there, as if a relationship existed. Which function applies the filter?",
 ["TREATAS(VALUES(SelectedRegions[Region]), 'Geo'[Region])", "USERELATIONSHIP(SelectedRegions[Region], 'Geo'[Region])", "RELATED(SelectedRegions[Region])", "CROSSFILTER(SelectedRegions[Region], 'Geo'[Region], BOTH)"], "A",
 "TREATAS applies one table's values as a filter on another column, which works as a virtual relationship. USERELATIONSHIP and CROSSFILTER need an existing physical relationship. RELATED needs a row context and a relationship."),

single("S1",
 "A measure must number each customer's orders 1, 2, 3, … by order date, restarting for every customer, in a table visual with Customer and OrderID. Which window function and argument should you use?",
 ["ROWNUMBER with ORDERBY(OrderDate), PARTITIONBY(CustomerKey)", "RANK(DENSE) with ORDERBY(OrderDate) and no PARTITIONBY", "OFFSET(-1) with ORDERBY(OrderDate), PARTITIONBY(CustomerKey)", "INDEX(1) with ORDERBY(OrderDate), PARTITIONBY(CustomerKey)"], "A",
 "ROWNUMBER gives unique sequential numbers, and PARTITIONBY restarts the numbering per customer. RANK without a partition ranks across everyone. OFFSET and INDEX return rows, not sequence numbers, even with the right partition."),

yesno("S1",
 "For each statement about calculation items, field parameters and dynamic format strings, select Yes if it is true.",
 [("A calculation item can change the format string of the measure it modifies.", True),
  ("A field parameter changes which field a visual shows. It doesn't change how a measure is calculated.", True),
  ("Dynamic format strings convert the measure's result to text, so visuals can no longer sort it numerically.", False)],
 "Calculation items can carry format string expressions. Field parameters swap fields. Dynamic format strings change only the display, and the value stays numeric. That's how they differ from FORMAT()."),

single("S1",
 "A Direct Lake on SQL analytics endpoint model needs Order Date and Ship Date as separate role-playing date tables. Calculated tables aren't available in this variant. What should you do?",
 ["Create the second date table upstream and add it to the model", "Add a DAX calculated table that copies Date", "Add a calculation group with Order and Ship items", "Import just the Ship Date table, in a composite model"], "A",
 "Direct Lake on SQL doesn't support calculated tables or composite models, so role-playing copies have to exist upstream as tables or views. A view may fall back to DirectQuery, so a small physical table is often better. Calculation groups don't create tables."),

# ---------------- S2 (5 + 1 in case)
single("S2",
 "A measure loops over a 600-million-row fact with SUMX(Sales, IF([Customer Sales] > 1000, Sales[Amount])), where [Customer Sales] is a measure. What is the main performance problem, and a better approach?",
 ["Context transition per fact row; iterate VALUES(Sales[CustomerKey])", "IF inside SUMX; replace it with SWITCH(TRUE())", "Errors in IF; wrap the expression in IFERROR", "Model size; turn on large semantic model storage format"], "A",
 "Calling a measure inside an iterator over the fact table causes context transition on every row, which is hundreds of millions of times here. Iterating the distinct customers cuts the work to the number of customers. IF is allowed in SUMX, and SWITCH, IFERROR or storage format don't touch the real cost."),

multi("S2",
 "Which three statements about Delta table maintenance are true?",
 ["OPTIMIZE compacts small files into larger ones", "VACUUM removes data files that are no longer referenced and are older than the retention threshold", "Z-ordering puts related values in the same files to improve data skipping", "OPTIMIZE deletes the table's time-travel history", "VACUUM rearranges the active files to speed up reads"], "ABC",
 "OPTIMIZE improves the file layout, VACUUM reclaims storage, and Z-order improves data skipping. OPTIMIZE adds a new version and doesn't delete history; VACUUM is what eventually removes old files. VACUUM doesn't touch the layout of active files."),

single("S2",
 "You publish an Import model with an incremental refresh policy covering 10 years. The first refresh in the service times out. What is a recommended technique?",
 ["Apply the policy, then refresh the partitions in batches through XMLA", "Remove the policy and use a full refresh instead", "Shorten the archive range to one day, then widen it", "Switch the table to Direct Lake and keep the policy"], "A",
 "The first incremental refresh loads all the history. With XMLA you can apply the policy to create the partitions and then refresh them in manageable batches. After that, regular refreshes only touch the incremental window."),

single("S2",
 "A Direct Lake on SQL model reads a complex SQL view, and every query against it falls back to DirectQuery. What change keeps those queries in Direct Lake?",
 ["Materialise the view as a gold Delta table loaded by the ETL", "Rewrite the view with CTEs instead of subqueries", "Set DirectLakeBehavior to DirectLakeOnly", "Grant the users ReadAll on the warehouse"], "A",
 "Direct Lake can only read Delta tables directly, so non-materialised views cause fallback, however the view is written. Persisting the result as a table makes it readable by Direct Lake. DirectLakeOnly turns the fallback into errors, and ReadAll has nothing to do with it."),

single("S2",
 "A DirectQuery model over a well-maintained warehouse uses relationships whose keys always match. Queries use outer joins. Which relationship setting lets the engine generate more efficient inner joins?",
 ["Assume referential integrity", "Cross filter direction: Both", "Mark as date table", "Make this relationship active"], "A",
 "Assume referential integrity tells the engine that every fact key has a matching dimension row, so it can use inner joins in the SQL it sends to the source. Only turn it on when integrity really holds, or rows will go missing."),

# ---------------- Case study (M1, P1, P2, S2)
case("Margie's Travel",
 "Margie's Travel sells trips through 900 agents organised in a management hierarchy that's up to six levels deep. Bookings are written to a lakehouse, LH_Trips, by notebooks. A Direct Lake on OneLake semantic model serves agent and manager reports.\n\nA hotel partner publishes nightly rate tables in Apache Iceberg format in an Amazon S3 bucket. Customer names arrive from three booking channels with inconsistent spelling. A nightly pipeline writes several gold tables in sequence.",
 ["R1. Each manager must see bookings for themselves and everyone below them in the hierarchy.",
  "R2. Partner rate tables must be queryable in LH_Trips without copying them.",
  "R3. Customer records from the three channels must be matched, even when names are spelled slightly differently.",
  "R4. After the nightly load, reports must show all the new data together, never a partly loaded mix of tables."],
 [
  single("M1", "Which RLS filter on DimAgent satisfies R1? The table has an AgentPath column built with PATH(AgentKey, ManagerKey).",
   ["PATHCONTAINS(DimAgent[AgentPath], LOOKUPVALUE(DimAgent[AgentKey], DimAgent[UPN], USERPRINCIPALNAME()))", "DimAgent[UPN] = USERPRINCIPALNAME() || ISINSCOPE(DimAgent[AgentPath])", "PATHCONTAINS(DimAgent[AgentPath], USERPRINCIPALNAME())", "DimAgent[ManagerKey] = LOOKUPVALUE(DimAgent[AgentKey], DimAgent[UPN], USERPRINCIPALNAME())"], "A",
   "PATHCONTAINS keeps every agent whose path includes the signed-in manager's key, which is the manager and everyone below them. The path holds keys, so testing it for a UPN never matches. Matching ManagerKey shows only direct reports, not the whole chain or the manager. ISINSCOPE describes visual grouping and has no place in an RLS filter."),
  single("P1", "Which approach to the partner rate tables satisfies R2?",
   ["An external shortcut to the Iceberg tables in S3", "A pipeline that converts them to Delta each night", "Mirroring the S3 bucket into OneLake", "A Dataflow Gen2 that reads them into a warehouse"], "A",
   "OneLake shortcuts can expose Iceberg tables held in supported storage, such as S3, as tables, without copying them. The metadata is virtualised so Fabric engines can read them. Copying breaks R2, and mirroring is for databases."),
  single("P2", "Which Dataflow Gen2 feature best satisfies R3?",
   ["Merge queries with fuzzy matching", "Merge queries with an exact match", "Append the channels, then remove duplicates", "Change type with locale on names"], "A",
   "Fuzzy merge matches rows whose text values are similar rather than identical, with a similarity threshold you can tune and optional transformation tables. Exact merge and remove duplicates miss spelling variants, and locale settings affect type conversion, not matching."),
  single("S2", "Which configuration satisfies R4?",
   ["Turn off automatic updates; refresh the model as the pipeline's last step", "Schedule the model refresh for 06:00, after the usual finish", "Keep automatic updates on so tables reframe as they land", "Switch the model to DirectQuery for live data"], "A",
   "Triggering framing from the pipeline once all the tables are written moves every table to its new version together. With automatic updates on, reframing can happen part-way through the load. A fixed-time schedule guesses when the load ends. DirectQuery gives up Direct Lake and still shows partly loaded tables."),
 ]),
]
