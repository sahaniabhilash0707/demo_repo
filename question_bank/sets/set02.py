from model import single, multi, yesno, match, order, case

TITLE = "Foundations — stores, routes and the gold layer"
SUBTITLE = "Choosing the right item and the right ingestion route, and the T-SQL and PySpark you need to shape gold tables."
LEVEL = "Level 1 · Foundation"
CASE_NAME = "Fabrikam Health"

ITEMS = [
# ---------------- M1 (6)
single("M1",
 "A team lead must be able to add colleagues to a workspace as Contributors and share individual items. They must not be able to delete the workspace or manage other admins. Which role is the least privileged one that meets the requirement?",
 ["Viewer", "Contributor", "Member", "Admin"], "C",
 "Member can add users with Member, Contributor or Viewer roles and can share items. Only Admin can delete the workspace or manage other admins. Contributors can create and edit content but can't manage access."),

single("M1",
 "A lakehouse holds a Files/legal/contracts folder. Only the Legal group may read that folder, but every analyst may read all the tables. The analysts are workspace Viewers. What should you configure?",
 ["A OneLake security role on the folder for the Legal group, with the default reader role edited to exclude it", "A row-level security role in the semantic model that filters on the folder path", "Object-level security in Tabular Editor on the contracts table", "A separate workspace for the contracts with Legal as Viewers"], "A",
 "OneLake security roles can be scoped to folders and tables inside an item. That's the file and folder-level access control in the skills outline. The default reader role has to stop granting the folder, or everyone keeps access. RLS and OLS work inside semantic models, not on lake folders. A separate workspace duplicates structure for no benefit."),

single("M1",
 "In a Fabric Warehouse, members of the Analysts role must query `dbo.Employee` but must not see the `Salary` or `NationalID` columns. Which statement meets the requirement?",
 ["GRANT SELECT ON dbo.Employee (EmployeeID, Name, Department, HireDate) TO Analysts;", "DENY SELECT ON dbo.Employee TO Analysts;", "GRANT SELECT ON dbo.Employee TO Analysts WITH GRANT OPTION;", "ALTER TABLE dbo.Employee DROP COLUMN Salary, NationalID;"], "A",
 "Column-level security in the warehouse is done with a GRANT on a list of columns. The analysts can query the granted columns, and any query that references Salary or NationalID fails. DENY on the whole table blocks everything. WITH GRANT OPTION grants every column and lets them pass the permission on. Dropping the columns destroys the data."),

single("M1",
 "The customer lakehouse must be flagged as the single authoritative source for customer data across the organisation. Which endorsement badge is designed for this?",
 ["Promoted", "Certified", "Master data", "Featured"], "C",
 "Master data marks an item as the authoritative source for a core business entity, such as customers or products. Certified shows that an item meets quality standards. Promoted is a self-service signal. Like Certified, Master data can only be applied by users the administrator authorises."),

yesno("M1",
 "Your tenant has grown to 900 workspaces. For each statement about Fabric domains, select Yes if it is true.",
 [("A domain groups workspaces by business area, such as Finance or Supply Chain.", True),
  ("Domain admins can be delegated some settings without becoming Fabric administrators.", True),
  ("Assigning a workspace to a domain grants domain admins read access to all of its data.", False)],
 "Domains are a governance and discovery layer above workspaces, with delegated administration for domain-level settings. They don't grant data access. Workspace roles, item permissions and OneLake security still decide who can see data."),

single("M1",
 "Support staff query a warehouse table that contains customer email addresses. They must see values like `aXXX@XXXX.com` instead of the real address, while a privileged group sees the full value. What should you implement?",
 ["Dynamic data masking on Email with the email() function, plus UNMASK for the privileged group", "Row-level security with a predicate function on the Email column", "A Highly Confidential sensitivity label on the warehouse", "Column-level security that denies SELECT on Email to support staff"], "A",
 "Dynamic data masking hides column values in query results without changing the stored data, and users with UNMASK see the real values. Column-level security blocks the column entirely, so support staff would get an error instead of a masked value. RLS filters rows, not values. Labels classify and protect exports."),

# ---------------- M2 (5 + 1 in case)
yesno("M2",
 "A developer saves a report as a Power BI project (.pbip). For each statement, select Yes if it is true.",
 [("The semantic model definition can be stored in TMDL, a human-readable text format.", True),
  ("The report definition can be stored in the PBIR format, as text files.", True),
  ("The project folder contains the imported data, so it can be opened offline with full data.", False)],
 "A .pbip saves definitions as text: TMDL for the model and PBIR for the report. That's what makes diffs and pull-request review work. The data isn't part of the definition. A local cache file is excluded from source control, and data is reloaded by refresh."),

single("M2",
 "In a deployment pipeline, a report named Sales exists in Development and a separately created report also named Sales exists in Test. They were never paired. What happens when you deploy from Development to Test?",
 ["The existing Test report is overwritten.", "Deployment fails with a name conflict.", "A second report named Sales is created in Test.", "The two reports are paired, then merged."], "C",
 "Deployment pipelines overwrite only paired items. Items are paired when a workspace is assigned to a stage, or when content is first deployed. An unpaired item with the same name doesn't get overwritten, so you end up with a duplicate."),

single("M2",
 "Your workspace is connected to the main branch of a GitHub repository. A developer needs an isolated workspace to work on a feature branch without affecting the shared workspace. What should they do?",
 ["Use Branch out to another workspace from the source control pane", "Export every item as a .pbix and re-import it", "Create a deployment pipeline with a Feature stage", "Turn off Git integration while they work"], "A",
 "Branch out creates a new branch and connects a new (or existing) workspace to it, giving the developer an isolated copy that they later merge through a pull request. Deployment pipelines promote content between stages. They don't give you feature isolation."),

single("M2",
 "Analysts often connect to the same certified warehouse and get the server address wrong. You want them to open Power BI Desktop already pointed at the correct source. What should you distribute?",
 ["A .pbids file", "A .pbit file", "A .pbix file containing data", "A deployment rule"], "A",
 "A .pbids (Power BI data source) file holds only a connection, so Desktop opens with the source already chosen. A .pbit is a full template without data. A .pbix includes the data. Deployment rules apply to pipeline stages."),

single("M2",
 "A semantic model in a Fabric workspace was edited through the XMLA endpoint with Tabular Editor. What is a consequence you should plan for?",
 ["The model can no longer be downloaded as a .pbix file.", "The model's storage mode switches to DirectQuery.", "The reports connected to it must be republished.", "The workspace is disconnected from its Git branch."], "A",
 "Once a model has been changed through the XMLA endpoint, you can't download it as a .pbix any more. From then on, you manage it as source (a .pbip or TMDL in Git, or a .bim) and deploy it with tools. The other options don't happen."),

# ---------------- P1 (6 + 1 in case)
single("P1",
 "The finance systems team writes T-SQL. They need stored procedures that insert, update and delete rows in gold tables, with transactions that span tables. Which item should they build the gold layer in?",
 ["A lakehouse, using its SQL analytics endpoint", "A warehouse", "An eventhouse", "A KQL queryset"], "B",
 "Only the warehouse supports full T-SQL DML and DDL with multi-table transactions. The lakehouse SQL analytics endpoint is read-only for tables. Eventhouses are for event and time-series data. A queryset only runs queries."),

single("P1",
 "A gold table in a lakehouse in the Finance workspace must be readable from a lakehouse in the Marketing workspace. Nobody may maintain a copy, and schema changes must show up automatically. What should you create?",
 ["An internal shortcut in the Marketing lakehouse to the Finance table", "A nightly Copy activity into the Marketing lakehouse", "A Dataflow Gen2 into the Marketing lakehouse", "A mirrored database of the Finance lakehouse"], "A",
 "An internal shortcut points to data in another Fabric item, in any workspace, with no copy and no sync job, and it reflects schema changes. Copies need maintaining and go out of date. Mirroring is for external operational databases."),

single("P1",
 "A user can open Lakehouse B, which contains a shortcut to a table in Lakehouse A, but gets an access error when reading the shortcut from a notebook. What is the most likely reason?",
 ["The user has no permission on the table in Lakehouse A.", "Shortcuts can only be read through the SQL endpoint.", "The shortcut expired after 30 days without use.", "Both lakehouses are assigned to the same capacity."], "A",
 "Reading through an internal shortcut needs permission on both the shortcut location and the target. The user's own identity is checked against the target. Shortcuts don't expire, and Spark can read them."),

single("P1",
 "Telemetry is ingested into an Eventhouse. A Direct Lake semantic model must report on the same data without a separate copy pipeline. What should you do?",
 ["Turn on OneLake availability for the KQL database or table", "Export the KQL tables to CSV in a lakehouse every hour", "Build a DirectQuery semantic model on the KQL database", "Create a shortcut from the Eventhouse to a warehouse"], "A",
 "OneLake availability writes the Eventhouse data to OneLake as Delta tables, which Direct Lake can read. That's the skill named “Implement OneLake integration for Eventhouse and semantic models”. Exporting to CSV duplicates the data and loses the Delta format. DirectQuery gives up Direct Lake."),

single("P1",
 "A pipeline must copy 50 tables from a source database. The list of tables is kept in a control table. Which pattern should you use?",
 ["A Lookup on the control table, then a ForEach running a parameterised Copy", "Fifty pipelines, each with one Copy activity, run in parallel", "A single Copy activity configured with 50 sources", "A Dataflow Gen2 with one query and destination per table"], "A",
 "This is the standard metadata-driven pattern. Lookup returns the list, and ForEach runs a Copy activity with the source and destination parameterised from each item, so one pipeline handles any number of tables. A single Copy activity can't take 50 sources."),

yesno("P1",
 "You are creating shortcuts in a lakehouse. For each statement, select Yes if it is true.",
 [("A shortcut in the Tables folder must be created at the top level, not inside a subfolder.", True),
  ("A shortcut in the Files folder can be created at any folder level and can point to any file format.", True),
  ("Deleting a shortcut also deletes the data at the target location.", False)],
 "Tables-folder shortcuts sit at the top level and are meant for Delta tables. Files-folder shortcuts can go at any depth and point to any format. Deleting a shortcut only removes the pointer. Deleting or moving the target is what breaks the shortcut."),

# ---------------- P2 (8)
single("P2",
 "Complete the query so that only the most recent row per OrderID is returned.",
 ["WHERE rn = 1", "WHERE rn > 1", "HAVING COUNT(*) = 1", "WHERE rn IS NULL"], "A",
 "ROW_NUMBER numbers the rows in each OrderID partition from newest to oldest, with the tie-breaker making it deterministic. Keeping rn = 1 leaves exactly one row, the latest, per order. rn > 1 returns the duplicates instead.",
 code="""WITH x AS (
  SELECT *, ROW_NUMBER() OVER (PARTITION BY OrderID
                               ORDER BY ModifiedAt DESC, LoadID DESC) AS rn
  FROM stg.Orders)
SELECT * FROM x
______ ;"""),

single("P2",
 "A product's colour changes from time to time. The business only ever reports on the current colour and doesn't need history. Which dimension handling is appropriate?",
 ["Slowly changing dimension Type 1: overwrite the attribute in place", "Slowly changing dimension Type 2: add a new row with validity dates", "Store the colour on the fact table", "Create a new dimension table each month"], "A",
 "Type 1 overwrites the value and keeps no history, which is right when only the current value matters. Type 2 keeps history by adding versioned rows, which isn't needed here. Putting attributes on the fact breaks the star schema."),

single("P2",
 "Which key design is best for joining a gold dimension to a very large fact table?",
 ["A string key made by joining the source system code and the business key", "An integer surrogate key generated during the load", "A GUID from the source system", "No key; join on the customer name"], "B",
 "Integer surrogate keys are compact, compress well in both Delta and VertiPaq, and keep the gold layer independent of source keys. Composite string keys and GUIDs have high cardinality and are wide. GUID isn't a supported data type in Direct Lake either."),

single("P2",
 "In a notebook, you need to add a column `Margin` equal to `Revenue - Cost` to a DataFrame. Which line is correct?",
 ["df = df.withColumn(\"Margin\", F.col(\"Revenue\") - F.col(\"Cost\"))", "df = df.select(\"Margin\")", "df = df.groupBy(\"Revenue\").agg(F.sum(\"Cost\"))", "df = df.drop(\"Revenue\", \"Cost\")"], "A",
 "withColumn adds or replaces a column using a column expression (F is pyspark.sql.functions). select(\"Margin\") fails because the column doesn't exist yet. groupBy aggregates. drop removes columns."),

single("P2",
 "Complete the PySpark that produces total Amount and order count per Region.",
 [".groupBy(\"Region\").agg(F.sum(\"Amount\").alias(\"Amount\"), F.count(\"*\").alias(\"Orders\"))",
  ".select(\"Region\", F.sum(\"Amount\"), F.count(\"*\"))",
  ".orderBy(\"Region\").agg(F.sum(\"Amount\"), F.count(\"*\"))",
  ".withColumn(\"Amount\", F.sum(\"Amount\")).withColumn(\"Orders\", F.count(\"*\"))"], "A",
 "groupBy followed by agg is the PySpark aggregation pattern, and you can compute several aggregates in one pass. Selecting Region next to aggregates without groupBy fails. orderBy only sorts, so agg after it returns one total row with no Region. Aggregate functions can't be used in withColumn without a window.",
 code="""summary = (spark.read.table("silver_orders")
           ______ )"""),

single("P2",
 "A Dataflow Gen2 reads a large SQL source, but the business only needs the last two years. Where should the date filter go to cut the most data movement?",
 ["As an early step that folds back to the source", "As the last step, after the merge and pivot", "As a report-level filter in the semantic model", "In a DAX measure that ignores older dates"], "A",
 "Putting filters early, in steps that fold, pushes them to the source as a WHERE clause, so only the needed rows leave the database. Filtering later moves all the data first. Report filters and measures don't reduce what's loaded at all."),

match("P2",
 "Match each Power Query transformation to the requirement it meets in a Dataflow Gen2.",
 [("Add the customer's segment from a lookup table to each order row", "Merge queries"),
  ("Stack the January, February and March extracts, which share the same columns, into one table", "Append queries"),
  ("Produce one row per region with total sales", "Group by"),
  ("Turn the month values in a column into separate columns", "Pivot column")],
 ["Merge queries", "Append queries", "Group by", "Pivot column", "Unpivot columns"],
 "Merge is a join, so it adds columns from another table. Append is a union, so it adds rows. Group by aggregates. Pivot turns values into columns, and unpivot does the opposite."),

single("P2",
 "An `Amount` column was read from CSV as a string. It must become a decimal with two decimal places before it's written to the silver table. Which expression is correct?",
 ["F.col(\"Amount\").cast(\"decimal(18,2)\")", "F.col(\"Amount\").alias(\"decimal\")", "F.lit(\"Amount\").cast(\"int\")", "F.col(\"Amount\").substr(1, 2)"], "A",
 "cast changes the column's data type, and decimal(18,2) keeps two decimal places exactly. alias only renames. lit creates a constant, here the literal text “Amount”. substr extracts characters."),

# ---------------- P3 (5 + 1 in case)
single("P3",
 "Which T-SQL expression returns a running total of Revenue by date?",
 ["SUM(Revenue) OVER (ORDER BY OrderDate ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)", "SUM(Revenue) OVER (PARTITION BY OrderDate ORDER BY OrderDate)", "RANK() OVER (ORDER BY OrderDate ROWS UNBOUNDED PRECEDING)", "LAG(Revenue) OVER (ORDER BY OrderDate ROWS UNBOUNDED PRECEDING)"], "A",
 "A windowed SUM with a frame that starts at UNBOUNDED PRECEDING and ends at the CURRENT ROW gives a running total. Using ROWS rather than RANGE avoids surprises when dates repeat. Partitioning by OrderDate restarts the sum on every date. RANK and LAG don't accept a frame clause, and neither adds anything up."),

single("P3",
 "Which KQL query returns the five devices with the most error events?",
 ["Logs | where Level == \"Error\" | summarize Errors = count() by DeviceId | top 5 by Errors desc",
  "Logs | where Level == \"Error\" | top 5 by DeviceId desc",
  "Logs | where Level == \"Error\" | take 5 | project DeviceId, Level",
  "Logs | where Level == \"Error\" | project DeviceId, count() | limit 5"], "A",
 "Filter first, then summarize the count per device, then top 5 by the count. top 5 by DeviceId sorts by the ID, not by errors. take returns arbitrary rows. project can't aggregate."),

single("P3",
 "In the DAX query view you want to test a new measure definition against the model without saving it. Which query structure lets you do that?",
 ["DEFINE MEASURE Sales[Test] = ...  EVALUATE SUMMARIZECOLUMNS('Date'[Year], \"Test\", [Test])", "CREATE MEASURE Sales[Test] = ... ; SELECT [Test] FROM 'Date'", "EVALUATE MEASURE Sales[Test] = ... SUMMARIZECOLUMNS('Date'[Year], \"Test\", [Test])", "ALTER MODEL ADD MEASURE Sales[Test] = ... ; EVALUATE [Test]"], "A",
 "DEFINE MEASURE declares a measure that exists only for that query, and EVALUATE returns a table that uses it. That's how you test changes in the DAX query view before updating the model. The other syntaxes don't exist in DAX queries."),

single("P3",
 "In KQL, you need to add the device's site name from the `Devices` table to each row of `Telemetry`, keeping only rows that match. Which operator should you use?",
 ["join kind=inner Devices on DeviceId", "union Devices", "extend SiteName = Devices.SiteName", "mv-expand Devices"], "A",
 "join kind=inner matches rows on the key and returns only the matches. union stacks tables. extend adds computed columns from the same row. mv-expand expands arrays into rows."),

single("P3",
 "A warehouse named WH_Gold and a lakehouse named LH_Raw are in the same workspace. From a query in WH_Gold, you need to join to the `orders` table in LH_Raw without copying it. Which reference works?",
 ["LH_Raw.dbo.orders", "OPENROWSET('LH_Raw', 'orders')", "external_table('orders')", "[LH_Raw]::orders"], "A",
 "Within a workspace, warehouses and SQL analytics endpoints support cross-database queries with three-part names (database.schema.table). external_table() is KQL. The other syntaxes are invalid here."),

# ---------------- S1 (5 + 1 in case)
single("S1",
 "You mark a table as the model's date table. What must its date column contain?",
 ["Unique, contiguous dates covering every date in the facts", "Only the dates on which sales actually happened", "Unique text values in the format yyyy-mm-dd", "Exactly one row per month, on the first day"], "A",
 "A date table needs one row per day, with no duplicates or gaps, covering every date the facts use. Time-intelligence functions depend on that. Including only sales dates leaves gaps. The column must have the Date data type."),

single("S1",
 "In a composite model, a large fact uses DirectQuery and an aggregation table uses Import. A shared dimension relates to both. Which storage mode should the dimension use?",
 ["Import", "DirectQuery", "Dual", "Direct Lake"], "C",
 "Dual lets the engine use the dimension from memory when the query hits the Import aggregation, and as DirectQuery when the query goes to the detail fact. That avoids weak (limited) relationships and keeps queries that hit the aggregation in memory."),

single("S1",
 "Which measure returns each product category's share of sales across all categories, ignoring any category filter while still respecting other filters, such as year?",
 ["DIVIDE([Sales], CALCULATE([Sales], REMOVEFILTERS('Product'[Category])))", "DIVIDE([Sales], CALCULATE([Sales], ALL(Sales)))", "DIVIDE([Sales], CALCULATE(SUM(Sales[Amount])))", "DIVIDE([Sales], CALCULATE([Sales], ALLSELECTED('Date')))"], "A",
 "REMOVEFILTERS on the Category column clears only that filter, so the denominator is all categories in the current year or other context. ALL(Sales) removes every filter on the fact, including year. CALCULATE(SUM(...)) keeps the category filter, so the share is always 1. ALLSELECTED('Date') changes the date filter, not the category filter."),

single("S1",
 "A Direct Lake model over a gold lakehouse must also include a small Import table of sales targets loaded from Excel. Which Direct Lake variant supports this?",
 ["Direct Lake on OneLake", "Direct Lake on the SQL analytics endpoint", "Both variants", "Neither variant"], "A",
 "Composite models (Direct Lake tables plus Import tables) are supported with Direct Lake on OneLake, not with Direct Lake on the SQL analytics endpoint.", fixed=True),

single("S1",
 "A card must show the selected region's name, or \"All regions\" when zero or several regions are selected. Which expression is the most concise?",
 ["SELECTEDVALUE('Geo'[Region], \"All regions\")", "VALUES('Geo'[Region])", "FIRSTNONBLANK('Geo'[Region], 1)", "MAX('Geo'[Region])"], "A",
 "SELECTEDVALUE returns the value when exactly one is in the filter context, and otherwise returns the alternate result. VALUES returns a table and errors in a card when several regions are selected. FIRSTNONBLANK and MAX return one arbitrary value when several are selected."),

# ---------------- S2 (6)
single("S2",
 "In a development workspace, any query that a Direct Lake on SQL model can't answer in Direct Lake mode should fail, so the problem gets noticed. Which DirectLakeBehavior setting should you choose?",
 ["Automatic", "DirectLakeOnly", "DirectQueryOnly", "ImportOnly"], "B",
 "DirectLakeOnly turns off fallback to DirectQuery, so unsupported queries fail and regressions show up. Automatic (the default) quietly falls back to DirectQuery. DirectQueryOnly forces every query to use DirectQuery. ImportOnly isn't a valid value.", fixed=True),

single("S2",
 "A semantic model must read gold data through SQL views that join and filter several warehouse tables. Which Direct Lake variant can read the views?",
 ["Direct Lake on OneLake", "Direct Lake on the SQL analytics endpoint", "Both variants equally", "Neither; views need Import mode"], "B",
 "Direct Lake on the SQL analytics endpoint can use SQL views, although queries against non-materialised views fall back to DirectQuery. Direct Lake on OneLake reads Delta tables directly and can't connect to views.", fixed=True),

single("S2",
 "Which rewrite usually improves performance most for `CALCULATE([Sales], FILTER(Sales, Sales[Channel] = \"Online\"))`?",
 ["CALCULATE([Sales], Sales[Channel] = \"Online\")", "CALCULATE([Sales], FILTER(ALL(Sales), Sales[Channel] = \"Online\"))", "SUMX(FILTER(Sales, Sales[Channel] = \"Online\"), [Sales])", "IFERROR([Sales], 0)"], "A",
 "A Boolean filter on a column is applied to that column only and becomes a simple predicate for the storage engine. FILTER over the whole fact table builds the full table. FILTER(ALL(Sales)) also removes existing filters, which changes the result. SUMX with a measure triggers context transition on every row."),

yesno("S2",
 "For each statement about V-Order in Fabric, select Yes if it is true.",
 [("V-Order is a write-time optimisation of Parquet files that speeds up reads by engines such as Direct Lake.", True),
  ("V-Order can be turned on for a table with the table property delta.parquet.vorder.enabled.", True),
  ("V-Order makes writes faster than normal Parquet writes.", False)],
 "V-Order sorts, distributes and compresses Parquet data when it's written, so reads are faster. Writes cost more, about 15% by Microsoft's figure. You can set it per session, per table or per write. Its default state has changed over time, so set it on purpose for read-heavy tables."),

single("S2",
 "An incremental refresh policy refreshes the last 10 days of a large fact, but most days have no changes. What reduces wasted refresh work?",
 ["Turn on Detect data changes using a LastModified column", "Increase the incremental window to 60 days", "Turn on automatic page refresh for the report", "Turn off query folding on the source query"], "A",
 "Detect data changes checks a date/time column, such as LastModified, per partition and refreshes only the partitions whose maximum value has changed. A wider window does more work. Query folding is required for incremental refresh to work efficiently, so it shouldn't be turned off."),

single("S2",
 "A Direct Lake on OneLake model frames a table whose row count is over the capacity's guardrail. What happens?",
 ["Queries fall back to DirectQuery automatically, more slowly.", "Framing fails, and the model can't be queried until the table fits the guardrails.", "The capacity scales up to the next SKU automatically.", "The model switches that table to Import mode."], "B",
 "Direct Lake on OneLake has no DirectQuery fallback, so going over a guardrail causes a failure, not a slowdown. Direct Lake on the SQL analytics endpoint can fall back to DirectQuery if fallback is enabled. That difference is why table maintenance matters so much for the OneLake variant."),

# ---------------- Case study (M2, P1, P3, S1)
case("Fabrikam Health",
 "Fabrikam Health runs 60 clinics. Appointment data lives in an Azure SQL Database that backs the booking application. The database team won't allow analytical queries against it. A Fabric warehouse, WH_Clinic, holds the gold layer and is maintained by T-SQL developers.\n\nThe team works in three workspaces (Dev, Test and Prod) connected by a deployment pipeline. Finance keeps monthly visit targets in an Excel file on SharePoint.",
 ["R1. Appointment data must reach OneLake within minutes, with no ETL pipeline to build.",
  "R2. Analysts must be able to list visits per clinic for the last 7 days with T-SQL.",
  "R3. The semantic model must point at WH_Clinic in each stage's own workspace after deployment, without manual edits.",
  "R4. The semantic model must combine the gold tables, in Direct Lake mode, with the Excel targets."],
 [
  single("P1", "Which approach satisfies R1?",
   ["Mirror the Azure SQL Database into Fabric", "Create an external shortcut to the Azure SQL Database", "Build a pipeline that copies the data every five minutes", "Create a DirectQuery semantic model over the database"], "A",
   "Mirroring replicates supported operational databases into OneLake in near real time with no pipeline to build. It reads the database's change data rather than running analytical queries against it. Shortcuts point at storage, not at Azure SQL databases. A five-minute pipeline is ETL."),
  single("P3", "Which query satisfies R2 in WH_Clinic?",
   ["SELECT ClinicID, COUNT(*) AS Visits FROM gold.FactVisit WHERE VisitDate >= DATEADD(day, -7, CAST(GETDATE() AS date)) GROUP BY ClinicID;",
    "SELECT ClinicID, COUNT(*) FROM gold.FactVisit WHERE VisitDate > ago(7d) GROUP BY ClinicID;",
    "FactVisit | where VisitDate > ago(7d) | summarize count() by ClinicID",
    "SELECT ClinicID, COUNT(*) FROM gold.FactVisit GROUP BY ClinicID HAVING VisitDate >= GETDATE() - 7;"], "A",
   "DATEADD on today's date gives the cutoff, and GROUP BY counts per clinic. ago() is a KQL function. The pipe syntax is KQL. HAVING filters groups and can't reference a non-aggregated column that isn't grouped."),
  single("M2", "Which configuration satisfies R3?",
   ["Deployment rules on Test and Prod that repoint the model's data source", "Three Git branches, one per stage, merged on each release", "Republishing the model from Desktop to each stage's workspace", "A .pbids file for each stage's warehouse"], "A",
   "Deployment rules (data source or parameter rules) are set on the target stage. They change where the deployed item points, so you promote the same model each time. Git branches don't rewrite connections. Republishing manually is what R3 rules out."),
  single("S1", "Which design satisfies R4?",
   ["A Direct Lake on OneLake model with an Import table for the targets", "A Direct Lake on SQL endpoint model with an Import table for the targets", "Two semantic models, one for gold and one for targets", "An Import model for every table, dropping Direct Lake"], "A",
   "Only Direct Lake on OneLake supports composite models that mix in Import tables. The SQL endpoint variant can't be combined with Import tables. Two models split the experience, and importing everything gives up Direct Lake."),
 ]),
]
