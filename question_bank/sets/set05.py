from model import single, multi, yesno, match, order, case

TITLE = "Exam standard — constraints decide"
SUBTITLE = "Longer stems where two options both work and one qualifier rules one out. Includes repeated-scenario Yes/No series."
LEVEL = "Level 3 · Exam standard"
CASE_NAME = "Litware Energy"

ITEMS = [
# ---------------- M1 (5 + 1 in case)
single("M1",
 "You share a report with a colleague who has no access to the workspace or to the report's semantic model. What access to the semantic model does sharing the report give the colleague?",
 ["Read permission on the semantic model", "Build permission on the semantic model", "Read and Write permission on the semantic model", "No access to the model at all"], "A",
 "Sharing a report gives the recipient Read on the underlying semantic model so the visuals can query it, and RLS still applies. Build (needed to create new content) and Write aren't granted unless you choose to grant them."),

yesno("M1",
 "Goal: analysts must read only the tables in the gold schema of a lakehouse, through both Spark and SQL, following least privilege. For each proposed solution, select Yes if it meets the goal.",
 [("Give the analysts the workspace Viewer role and a OneLake security role that grants read on the gold schema only.", True),
  ("Give the analysts the workspace Contributor role.", False),
  ("Share the lakehouse with the ReadAll permission and no OneLake security role.", False)],
 "A Viewer with a OneLake security role scoped to the gold schema gets exactly that, and OneLake security is enforced across engines. Contributor can read and write everything and bypasses OneLake roles. ReadAll on its own covers all of the lakehouse's data."),

single("M1",
 "A user exports a report labelled Confidential – Finance to PDF. What happens to the file?",
 ["The PDF keeps the label and the label's protection", "The label is removed, but the PDF is encrypted", "The export is blocked, as for every labelled item", "The PDF is relabelled with the tenant's default label"], "A",
 "Sensitivity labels and their protection carry through to supported exports such as Excel, PowerPoint and PDF. That's the main reason labels exist. Blocking exports is a separate policy decision, not something every label does."),

single("M1",
 "A team in another workspace must create its own reports from your certified semantic model, but must not be able to change the model. Which permission should you grant on the model?",
 ["Build", "Write", "Reshare only", "Workspace Contributor on your workspace"], "A",
 "Build lets users create new reports and run queries against the model. Write lets them change it. A Contributor role in your workspace would let them edit everything there."),

single("M1",
 "You have created RLS roles in a semantic model published to the service. Before going live, you want to check what a specific user in the Sales-North role will see. What should you do?",
 ["Use Test as role in the model's security settings", "Add yourself to the role and reopen the report", "Download the .pbix and view the role in Desktop", "Check the role's members in lineage view"], "A",
 "Test as role renders the report as a member of the role, or as a named user, so you can check filters without changing memberships. Workspace admins see all data by default, so adding yourself to the role tells you nothing."),

# ---------------- M2 (6)
yesno("M2",
 "You deploy a lakehouse from the Development stage to Test with a deployment pipeline. For each statement, select Yes if it is true.",
 [("The lakehouse item is created in the Test workspace.", True),
  ("The data in the lakehouse's Delta tables is copied to Test.", False),
  ("Items in the target stage are overwritten only if they're paired with the source items.", True)],
 "Deployment pipelines deploy item definitions and metadata, not data. You load data into each stage's lakehouse with that stage's own pipelines or notebooks. Pairing decides whether a deployment overwrites or creates a new item."),

single("M2",
 "A lakehouse is committed to a Git repository through Fabric Git integration. What does the repository contain for it?",
 ["The item's definition, but no table data or files", "The definition plus a copy of every Delta table", "A .pbix file of the default semantic model", "A shortcut that points back to the lakehouse"], "A",
 "Git integration stores item definitions as text. Data stays in OneLake. That's why each environment loads its own data, and why repositories stay small."),

order("M2",
 "You need to set up a four-stage release process: Dev, Test, UAT and Prod. Put the actions in order.",
 ["Create a deployment pipeline",
  "Set the number of stages to four and name them Dev, Test, UAT and Prod",
  "Assign the existing development workspace to the Dev stage",
  "Deploy from Dev to Test"],
 "You set the pipeline's stages when you create it: between 2 and 10, renamed as you like. Then you assign workspaces and deploy stage by stage. Git connects for version control but isn't a step in creating the pipeline, and downloading .pbix files is the manual process pipelines replace.",
 extra=["Download each report as a .pbix file", "Disconnect the Dev workspace from Git"]),

single("M2",
 "An Azure DevOps release pipeline must deploy semantic model changes through the XMLA endpoint using a service principal. Apart from the XMLA endpoint being set to Read Write, what is required?",
 ["The service principal tenant setting turned on, and the principal given a workspace role with write access", "A Power BI Pro licence assigned to the service principal in Entra ID", "A personal gateway registered to the service principal", "Only an Azure DevOps service connection that stores the principal's secret"], "A",
 "Service principals need the tenant setting that lets them use the APIs, often limited to a security group, plus a workspace role with write access. They can't be assigned licences, and gateways have nothing to do with XMLA deployments."),

single("M2",
 "Why does the PBIR report format make team development easier than a single report.json file?",
 ["Each page, visual and bookmark is stored in its own file", "PBIR stores a data snapshot, so tests run offline", "PBIR encrypts the report so it's safe in public repositories", "PBIR embeds the semantic model, so no live connection is needed"], "A",
 "PBIR breaks the report definition into separate, documented JSON files for each object. Two developers editing different visuals no longer clash on one big file. It holds no data and doesn't replace the model."),

single("M2",
 "Reports in six other workspaces connect to your shared semantic model. You plan to remove a measure. How do you find every report that might break?",
 ["Run impact analysis on the semantic model", "Open lineage view in each of the six workspaces", "Check the Capacity Metrics app for queries", "Check the model's refresh history for callers"], "A",
 "Impact analysis on a semantic model shows downstream items across workspaces, with counts of workspaces and views. You can also notify their contacts from there. Refresh history and capacity metrics don't show dependencies."),

# ---------------- P1 (6 + 1 in case)
yesno("P1",
 "Goal: the gold layer must support multi-table transactions and T-SQL UPDATE statements written by SQL developers. For each proposed solution, select Yes if it meets the goal.",
 [("Build the gold layer in a Fabric Warehouse.", True),
  ("Build the gold layer in a lakehouse and run the UPDATE statements through its SQL analytics endpoint.", False),
  ("Build the gold layer in an Eventhouse.", False)],
 "Only the warehouse supports T-SQL DML with multi-table transactions. A lakehouse SQL analytics endpoint is read-only for table data, and an eventhouse is built for ingesting events."),

single("P1",
 "Your company keeps curated tables in Azure Databricks Unity Catalog. Fabric users must query them without copying the data or building pipelines. What should you create?",
 ["A mirrored Azure Databricks catalog item", "A pipeline that copies the tables nightly", "A Dataflow Gen2 for each table", "An Eventstream"], "A",
 "Mirroring an Azure Databricks catalog brings the Unity Catalog metadata into Fabric, with shortcuts to the underlying Delta data. Nothing is copied and no pipeline is needed. Copying with pipelines or dataflows duplicates the data."),

single("P1",
 "Clickstream events must land continuously as Delta tables in a lakehouse, so Spark jobs can process them in batches later. Which approach should you use?",
 ["An Eventstream with a lakehouse destination", "A Dataflow Gen2 scheduled every minute", "A KQL queryset", "A deployment pipeline"], "A",
 "Eventstreams take in streaming data and can write it continuously to a lakehouse as Delta, as well as to Eventhouse or other destinations. Dataflows are batch tools. Querysets and deployment pipelines don't ingest data."),

single("P1",
 "A Dataflow Gen2 that copies a 300-million-row table without changing it runs very slowly. Which feature is designed to speed up this kind of large, simple load?",
 ["Fast copy in Dataflow Gen2", "Turning off staging and adding more Power Query steps", "A personal gateway", "Automatic page refresh"], "A",
 "Fast copy uses the pipeline Copy activity's engine for large loads with simple transformations, which is much faster than the mashup engine. Adding steps slows it down. A personal gateway doesn't support dataflows."),

single("P1",
 "An Azure SQL Database is reachable only through a private endpoint inside a virtual network. A Fabric dataflow must read from it without exposing it publicly. What should you use?",
 ["A virtual network (VNet) data gateway", "A personal-mode gateway", "A public firewall rule that allows all IP addresses", "A OneLake shortcut"], "A",
 "A VNet data gateway lets Fabric reach data sources inside an Azure virtual network without a public endpoint and without a server to manage. Opening the firewall to everyone breaks the security requirement. Shortcuts don't point at SQL databases."),

single("P1",
 "Finance users want to drag CSV files from their desktop into a lakehouse's Files folder, the same way they use OneDrive. What should you give them?",
 ["OneLake file explorer for Windows", "A Spark job definition that uploads files", "A KQL database with one-click ingestion", "Mirroring of their OneDrive folder"], "A",
 "OneLake file explorer shows OneLake as a folder in Windows File Explorer, so users can upload, open and sync files with no code. The other options are engineering tools."),

# ---------------- P2 (8)
single("P2",
 "This warehouse script maintains a Type 2 dimension. Which step is missing at the marked line?",
 ["UPDATE the changed current rows: SET ValidTo = @LoadDate, IsCurrent = 0", "DELETE the current rows for customers whose attributes changed", "TRUNCATE TABLE dim.Customer, then reload every version", "UPDATE the changed current rows: SET Segment = s.Segment, City = s.City"], "A",
 "Type 2 needs two steps: expire the current version of changed customers (set ValidTo and IsCurrent = 0), then insert new versions. Updating in place is Type 1. Deleting or truncating destroys history.",
 code="""-- 1) ______
-- 2) Insert new versions for changed and brand-new customers
INSERT INTO dim.Customer (CustomerID, Segment, City, ValidFrom, ValidTo, IsCurrent)
SELECT s.CustomerID, s.Segment, s.City, @LoadDate, '9999-12-31', 1
FROM   stg.Customer s
LEFT JOIN dim.Customer d ON d.CustomerID = s.CustomerID AND d.IsCurrent = 1
WHERE  d.CustomerID IS NULL;"""),

single("P2",
 "Orders carry five low-cardinality flags: IsGift, IsExpress, IsReturned, PaymentType and Channel. Adding five tiny dimensions makes the model cluttered. What is the dimensional design pattern for this?",
 ["A junk dimension of the flag combinations, with one key on the fact", "A separate factless fact table for each of the five flags", "Drop the flags, which reports rarely use", "Add the five flags as extra columns on the date dimension"], "A",
 "A junk dimension collects unrelated low-cardinality attributes into one small table of their combinations. That gives one join instead of five and keeps the fact narrow. Putting them on the date dimension would be wrong, because they have nothing to do with dates."),

single("P2",
 "A Rating column has 100 rows: 80 have a value and 20 are NULL. What does AVG(Rating) in T-SQL divide by?",
 ["80, because AVG ignores NULLs", "100, treating NULLs as zero", "It returns NULL", "It raises an error"], "A",
 "Aggregate functions other than COUNT(*) ignore NULLs, so AVG divides by the 80 non-null values. If NULL should count as zero, write AVG(COALESCE(Rating, 0)). That's a business decision to make explicitly."),

yesno("P2",
 "For each statement about de-duplication in PySpark, select Yes if it is true.",
 [("df.distinct() removes only rows that are identical in every column.", True),
  ("df.dropDuplicates([\"OrderID\"]) keeps one row per OrderID, even when other columns differ.", True),
  ("dropDuplicates([\"OrderID\"]) always keeps the most recent row per OrderID.", False)],
 "distinct compares whole rows. dropDuplicates on a subset keeps one row per key, but doesn't guarantee which row survives. To keep the latest, use row_number over a window ordered by the timestamp."),

single("P2",
 "An event column `epoch_s` holds Unix time in seconds. Which PySpark expression converts it to a timestamp?",
 ["F.timestamp_seconds(\"epoch_s\")", "F.to_date(\"epoch_s\", \"yyyy-MM-dd\")", "F.col(\"epoch_s\").cast(\"string\")", "F.current_timestamp()"], "A",
 "timestamp_seconds converts seconds since the Unix epoch into a timestamp. from_unixtime followed by a cast also works. to_date with a pattern expects text. current_timestamp ignores the column completely."),

single("P2",
 "A warehouse view must return orders from 2026. Which filter lets the engine skip non-matching data most effectively?",
 ["WHERE OrderDate >= '2026-01-01' AND OrderDate < '2027-01-01'", "WHERE YEAR(OrderDate) = 2026", "WHERE CONVERT(varchar(4), OrderDate, 120) = '2026'", "WHERE DATEDIFF(year, OrderDate, '2026-12-31') = 0"], "A",
 "A range on the bare column can be checked against file and row-group minimum and maximum values, so whole chunks of data can be skipped. Wrapping the column in a function (YEAR, CONVERT, DATEDIFF) hides the raw values, so every row has to be evaluated."),

single("P2",
 "In a notebook, a 2-billion-row fact DataFrame is joined to a 300-row currency table. Which technique avoids shuffling the large table?",
 ["facts.join(F.broadcast(currency), \"CurrencyCode\")", "facts.repartition(10000).join(currency, \"CurrencyCode\")", "facts.toPandas().merge(currency.toPandas(), on=\"CurrencyCode\")", "facts.crossJoin(currency).filter(\"CurrencyCode = CurrencyCode\")"], "A",
 "Broadcasting the small table sends a copy to every executor, so the large table is joined where it sits, with no shuffle. Converting 2 billion rows to pandas won't fit in memory. A cross join multiplies the rows."),

match("P2",
 "Match each data-quality problem to the transformation that fixes it.",
 [("The same customer appears three times after repeated loads", "De-duplicate on the business key"),
  ("Discount is NULL where no discount was given", "Replace null with 0"),
  ("A date arrives as text in dd/MM/yyyy format", "Convert the data type, specifying the format or locale"),
  ("Order rows reference a product code missing from the dimension", "Map to an Unknown member")],
 ["De-duplicate on the business key", "Replace null with 0", "Convert the data type, specifying the format or locale", "Map to an Unknown member", "Drop the column"],
 "Each problem has a targeted fix. Dropping a column hides the problem and loses information, so it isn't the right answer for any of them."),

# ---------------- P3 (5 + 1 in case)
single("P3",
 "For each order you need one string listing all its product names, separated by commas. Which T-SQL function should you use?",
 ["STRING_AGG(ProductName, ', ')", "CONCAT(ProductName, ', ')", "STRING_SPLIT(ProductName, ',')", "COALESCE(ProductName, ', ')"], "A",
 "STRING_AGG concatenates values across the rows of a group. CONCAT works within a single row. STRING_SPLIT does the reverse. COALESCE replaces nulls."),

single("P3",
 "Which KQL query returns the 95th-percentile request latency in 5-minute buckets?",
 ["Requests | summarize p95 = percentile(DurationMs, 95) by bin(Timestamp, 5m)", "Requests | top 95 by DurationMs | summarize by bin(Timestamp, 5m)", "Requests | summarize p95 = max(DurationMs) * 0.95 by bin(Timestamp, 5m)", "Requests | where DurationMs > 95 | summarize count() by bin(Timestamp, 5m)"], "A",
 "percentile() inside summarize ... by bin() gives the 95th percentile for each 5-minute bucket. 95% of the maximum isn't a percentile. top 95 keeps only the 95 slowest requests. Counting requests over 95 ms answers a different question."),

single("P3",
 "A KQL table has 40 columns. You need every column except RawPayload and DebugInfo. Which operator is most concise?",
 ["project-away RawPayload, DebugInfo", "project RawPayload, DebugInfo", "extend RawPayload = \"\"", "summarize by RawPayload"], "A",
 "project-away removes the columns you name and keeps the rest. project keeps only the columns you list. extend and summarize don't remove columns the way you need."),

single("P3",
 "You want to list every measure in a semantic model, with its expression, from the DAX query view. Which query should you run?",
 ["EVALUATE INFO.VIEW.MEASURES()", "EVALUATE ALLMEASURES()", "SELECT * FROM MEASURES", "EVALUATE SELECTEDMEASURE()"], "A",
 "The INFO family of DAX functions returns model metadata as tables. INFO.VIEW.MEASURES (or INFO.MEASURES) lists the measures and their expressions. ALLMEASURES doesn't exist. SELECTEDMEASURE only works inside calculation items."),

single("P3",
 "Which T-SQL returns customers whose first-ever order was placed in 2026?",
 ["SELECT CustomerKey FROM gold.FactSales GROUP BY CustomerKey HAVING MIN(OrderDate) >= '2026-01-01' AND MIN(OrderDate) < '2027-01-01';",
  "SELECT DISTINCT CustomerKey FROM gold.FactSales WHERE OrderDate >= '2026-01-01' AND OrderDate < '2027-01-01';",
  "SELECT CustomerKey FROM gold.FactSales WHERE MIN(OrderDate) >= '2026-01-01' GROUP BY CustomerKey;",
  "SELECT TOP (1) WITH TIES CustomerKey FROM gold.FactSales WHERE OrderDate >= '2026-01-01' ORDER BY OrderDate;"], "A",
 "The first order date is MIN(OrderDate) per customer, filtered with HAVING. The DISTINCT query returns everyone who ordered in 2026, including long-standing customers. An aggregate can't be used in WHERE. TOP (1) WITH TIES returns only the customers who ordered on the first day of 2026."),

# ---------------- S1 (6)
yesno("S1",
 "Goal: report on a Snowflake data warehouse, where data must not be copied out of Snowflake and visuals must show values that are at most a minute old. Mirroring isn't allowed. For each proposed storage mode, select Yes if it meets the goal.",
 [("DirectQuery to Snowflake", True),
  ("Import with an hourly refresh", False),
  ("Direct Lake over a lakehouse loaded nightly", False)],
 "DirectQuery leaves the data in the source and queries it live. Import copies the data and is only as fresh as the last refresh. Direct Lake needs the data in OneLake, which means copying or mirroring it, and both are ruled out."),

single("S1",
 "A report page needs an Order Date slicer and a Ship Date slicer side by side, each filtering sales by its own date at the same time. What is the clearest model design?",
 ["Two role-playing date tables, Order Date and Ship Date, each related through an active relationship to its key", "One date table with an inactive relationship, and USERELATIONSHIP in every measure", "A field parameter", "A calculation group"], "A",
 "When users must filter by both roles at once, separate role-playing tables with active relationships are simplest. USERELATIONSHIP switches the active relationship inside a measure, so it doesn't support two independent slicers at the same time."),

single("S1",
 "Which measure returns the average revenue per customer, rather than per transaction line?",
 ["AVERAGEX(VALUES(Sales[CustomerKey]), [Revenue])", "AVERAGE(Sales[Revenue])", "DIVIDE([Revenue], COUNTROWS(Sales))", "SUMX(Sales, Sales[Revenue]) / 2"], "A",
 "AVERAGEX over the distinct customers evaluates [Revenue] for each customer (context transition happens because it's a measure) and then averages the results. AVERAGE and dividing by COUNTROWS both work per line."),

single("S1",
 "A measure must return Red-product sales, but must not override the user's own colour selection. If the user selects Blue, the result should be blank. Which filter argument does this?",
 ["CALCULATE([Sales], KEEPFILTERS('Product'[Color] = \"Red\"))", "CALCULATE([Sales], 'Product'[Color] = \"Red\")", "CALCULATE([Sales], ALL('Product'[Color]), 'Product'[Color] = \"Red\")", "CALCULATE([Sales], REMOVEFILTERS('Product'), 'Product'[Color] = \"Red\")"], "A",
 "A plain Boolean filter replaces the existing filter on Color, so it would show Red sales even when Blue is selected. Adding ALL or REMOVEFILTERS alongside it clears the user's selection in the same way. KEEPFILTERS combines the new filter with the existing one, so Blue AND Red gives blank."),

single("S1",
 "A title measure must say \"Filtered by region\" only when a slicer directly filters the Region column, and not when another filter only cross-filters it. Which function should you use?",
 ["ISFILTERED('Geo'[Region])", "ISCROSSFILTERED('Geo'[Region])", "HASONEVALUE('Geo'[Region])", "ISBLANK('Geo'[Region])"], "A",
 "ISFILTERED is TRUE only when the column is filtered directly. ISCROSSFILTERED is also TRUE when another column or table filters it indirectly. HASONEVALUE tests for a single value, which can be true without any filter."),

single("S1",
 "Report authors use a live connection to a certified shared semantic model, and they need to add their own small Import table of regional targets. What should they do?",
 ["Convert to a composite model (DirectQuery to the shared model) and import the targets", "Download a copy of the certified model and add the targets", "Ask for Write permission and add the targets to the certified model", "Use a .pbids file to connect to both sources"], "A",
 "DirectQuery for Power BI semantic models lets authors extend a shared model with local tables in a composite model. The governed model stays untouched and authors can add their own data. Copying the model creates the duplicates certification is meant to prevent."),

# ---------------- S2 (5 + 1 in case)
yesno("S2",
 "Goal: a production Direct Lake on SQL analytics endpoint model must stay available even when some queries can't run in Direct Lake mode. For each proposed DirectLakeBehavior setting, select Yes if it meets the goal.",
 [("Automatic", True),
  ("DirectLakeOnly", False),
  ("DirectQueryOnly", False)],
 "Automatic falls back to DirectQuery when needed, so queries keep working, if more slowly. DirectLakeOnly turns those queries into errors, which is useful in development. DirectQueryOnly gives up Direct Lake performance completely."),

single("S2",
 "A Direct Lake model fails on visuals that use DimStore. You find that StoreKey contains duplicate values. What should you do?",
 ["De-duplicate DimStore in the gold layer so StoreKey is unique", "Make the DimStore relationship filter in both directions", "Change the relationship's cardinality to many-to-many", "Set DirectLakeBehavior to DirectQueryOnly for the model"], "A",
 "Direct Lake needs the one-side key to be unique, and duplicates make queries fail. The right fix is upstream, in the gold table. Changing the relationship hides a data-quality problem, and forcing DirectQuery throws away the performance."),

single("S2",
 "A measure divides margin by revenue with IF(ISERROR(...)) to avoid division-by-zero errors, and it's slow. What is the recommended rewrite?",
 ["DIVIDE([Margin], [Revenue])", "IFERROR([Margin] / [Revenue], BLANK())", "[Margin] / [Revenue]", "FORMAT([Margin] / [Revenue], \"0%\")"], "A",
 "DIVIDE handles a zero denominator internally and is optimised for it. ISERROR and IFERROR force extra evaluation and can stop the engine using faster plans. A plain / errors on zero. FORMAT returns text."),

single("S2",
 "An incremental refresh policy is set to Archive data starting 5 years before the refresh date, and Incrementally refresh data starting 10 days before. What happens at each refresh?",
 ["The last 10 days are refreshed, 5 years are kept, and older data is dropped", "All 5 years are refreshed, and anything older is dropped", "The last 10 days are refreshed and kept, and the rest is dropped", "Ten yearly partitions are refreshed, and 5 years are kept"], "A",
 "The archive range sets how much history is kept, and the incremental range sets what's reprocessed. Partitions older than the archive range are dropped as time moves on."),

multi("S2",
 "A streaming job writes many tiny files to a Delta table on every micro-batch. Which two Spark Delta features reduce the small-file problem automatically, without a separate maintenance job?",
 ["Optimize write", "Auto compaction", "VACUUM", "Time travel", "Shortcut caching"], "AB",
 "Optimize write combines data into fewer, larger files at write time. Auto compaction checks fragmentation after each write and compacts when it's needed. VACUUM removes files nobody references, time travel reads old versions, and shortcut caching reduces external egress. None of those three fix small files."),

# ---------------- Case study (M1, P1, P3, S2)
case("Litware Energy",
 "Litware Energy collects readings from 2 million smart meters. Each meter sends a reading every minute. Regional analysts use a Direct Lake semantic model built on the SQL analytics endpoint of the warehouse WH_Grid. Row-level security by region is defined in WH_Grid with a security policy.\n\nThe model's main fact table, FactReading, holds 9 billion rows at minute grain. The tenant has an F64 capacity. Refresh history shows queries regularly falling back to DirectQuery, and the reason given is that the table is over the row guardrail.",
 ["R1. Each regional analyst must see only their region through the semantic model, enforced by the SQL security policy.",
  "R2. Meter readings must be queryable within seconds of arrival for operational monitoring.",
  "R3. Operations needs average consumption per meter in 15-minute buckets over the last 24 hours.",
  "R4. Reports used by analysts must stop falling back to DirectQuery."],
 [
  single("M1", "How must the semantic model connect to WH_Grid to satisfy R1?",
   ["With Microsoft Entra single sign-on (SSO) to the SQL endpoint", "With a fixed identity on a shareable cloud connection", "As Direct Lake on OneLake with SSO", "As an Import model refreshed nightly with SSO"], "A",
   "SQL-defined RLS can only filter per user if the SQL endpoint knows who the user is. That needs SSO. A fixed identity makes every user look like the same account. Direct Lake on OneLake reads files directly and bypasses SQL RLS."),
  single("P1", "Which architecture satisfies R2?",
   ["An Eventstream that ingests into an Eventhouse", "A nightly pipeline that loads into WH_Grid", "A Dataflow Gen2 that runs every 15 minutes", "An hourly Import refresh of the semantic model"], "A",
   "Eventstream plus Eventhouse is Fabric's real-time pattern: continuous ingestion and KQL queries within seconds. Nightly, 15-minute or hourly batches can't meet a seconds-level requirement."),
  single("P3", "Which KQL query over the Readings table satisfies R3?",
   ["Readings | where Timestamp > ago(24h) | summarize AvgKWh = avg(KWh) by MeterId, bin(Timestamp, 15m)",
    "Readings | where Timestamp > ago(24h) | project AvgKWh = avg(KWh) by MeterId, bin(Timestamp, 15m)",
    "Readings | summarize AvgKWh = avg(KWh) by MeterId | where Timestamp > ago(24h)",
    "Readings | where Timestamp > ago(24h) | top 15 by KWh by MeterId"], "A",
   "Filter to the last 24 hours, then summarize the average by meter and 15-minute bin. project can't aggregate. Filtering on Timestamp after summarize fails, because summarize has removed that column. top doesn't take a by clause and doesn't average anything."),
  single("S2", "Which change best satisfies R4 without changing capacity size?",
   ["Point the analysts' model at an hourly gold aggregate, keeping minute detail elsewhere", "Set DirectLakeBehavior to DirectLakeOnly so the fallback stops", "Run VACUUM on FactReading to remove old rows", "Add pre-aggregated measures to the model for each report page"], "A",
   "The fallback happens because FactReading is over the F64 row guardrail. Cutting the rows the model reads, with a gold table at the grain analysts actually use, brings it within the guardrail. DirectLakeOnly turns fallbacks into errors. VACUUM removes unreferenced files, not rows, and measures don't change what the model scans."),
 ]),
]
