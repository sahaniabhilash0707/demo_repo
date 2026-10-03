from model import single, multi, yesno, match, order, case

TITLE = "Exam standard — build, release, repeat"
SUBTITLE = "Development lifecycle in practice (Git, pipelines, XMLA, reusable assets) alongside the full data and modelling syllabus."
LEVEL = "Level 3 · Exam standard"
CASE_NAME = "Adventure Works Cycles"

ITEMS = [
# ---------------- M1 (6)
multi("M1",
 "Which two can a user with the workspace Viewer role do by default?",
 ["View reports and other content in the workspace", "Query lakehouse and warehouse data through the SQL analytics endpoint", "Read lakehouse files directly with Spark notebooks", "Edit semantic models", "Share items with other users"], "AB",
 "Viewers can view content and connect to SQL analytics endpoints with T-SQL, where SQL permissions and RLS apply. Reading OneLake files with Spark needs ReadAll or a OneLake security role. Editing and sharing need higher roles or extra permissions."),

single("M1",
 "Most new Fabric items should start as General unless the author picks something else. Which Microsoft Purview setting does this?",
 ["A default label in the Purview label policy", "Certification set as the tenant default", "A domain admin assigned to label items", "A workspace-level default sensitivity setting"], "A",
 "A Purview label policy can set a default label that's applied to new content automatically. Users can still change it, as the policy allows. The other options are about endorsement, delegated administration or data access."),

match("M1",
 "Match each scenario to the endorsement it calls for. Some scenarios don't call for endorsement.",
 [("A self-service author wants colleagues to know a dataflow is ready to reuse", "Promoted"),
  ("The data governance board has reviewed a finance model against its quality standards", "Certified"),
  ("The product lakehouse is the single authoritative source for product data", "Master data"),
  ("Only HR may open the salary semantic model", "No endorsement: use access controls")],
 ["Promoted", "Certified", "Master data", "No endorsement: use access controls"],
 "Endorsement signals trust and helps people find content. Promoted is self-service. Certified follows a review by authorised certifiers. Master data marks the authoritative source for an entity. Restricting who can open an item is a permissions question, and endorsement never controls access."),

single("M1",
 "A developer must create and edit notebooks, lakehouses and reports in a workspace and write data. They must not be able to add users or change permissions. Which role should you assign?",
 ["Contributor", "Member", "Admin", "Viewer"], "A",
 "Contributor gives full content creation and data read and write without access management. Member can add users and share. Admin controls everything. Viewer can't create items."),

yesno("M1",
 "A semantic model has a dynamic RLS role. For each statement, select Yes if it is true.",
 [("You define roles and their DAX filters in Power BI Desktop, or with external tools.", True),
  ("You add users or groups to roles after publishing, in the semantic model's security settings in the service.", True),
  ("The RLS filters apply to workspace Contributors who open the report.", False)],
 "Roles are defined in the model and members are assigned in the service. Admin, Member and Contributor have edit rights on the model, so RLS doesn't restrict them. Only Viewers and users with Read or Build permission are filtered."),

single("M1",
 "An analyst belongs to two warehouse database roles. One role has GRANT SELECT ON SCHEMA::sales. The other has DENY SELECT ON sales.Commission. What happens when the analyst queries sales.Commission?",
 ["Access is denied, because DENY takes precedence over GRANT", "Access is allowed, because GRANT at schema level wins", "The query returns only the columns granted", "The more recently created role wins"], "A",
 "In SQL permissions, an explicit DENY overrides any GRANT, wherever the GRANT comes from. That's useful for carving exceptions out of broad grants. Role creation order has no effect."),

# ---------------- M2 (5 + 1 in case)
single("M2",
 "You try to add a data source rule for a semantic model in the Test stage of a deployment pipeline, but the option is greyed out. Which requirement is most likely missing?",
 ["You must be the owner of the semantic model in the target stage", "The model must be in Import mode", "The workspace must be connected to GitHub, not Azure DevOps", "The pipeline must have exactly three stages"], "A",
 "Deployment rules can only be created by the owner of the item in the target stage. Take over the item first, or ask the owner to create the rule. Storage mode, Git provider and the number of stages don't affect rule creation."),

order("M2",
 "A gold table column must be renamed. Reports in several workspaces depend on it. Put the steps of a safe change in order.",
 ["Run impact analysis on the lakehouse to find the dependent items",
  "Notify the contacts of the affected items",
  "Make the change in the Development workspace and test it",
  "Promote the change through the deployment pipeline to Test, then Production"],
 "Find what depends on the table, warn the owners, change and test in Dev, then promote. Changing Production directly skips testing. Deleting reports isn't a change process.",
 extra=["Make the change directly in Production", "Delete the dependent reports"]),

single("M2",
 "A .pbit template must ask the user which server and database to connect to when they open it. What should the template contain?",
 ["Power Query parameters used in the source step", "A .pbids file embedded in the template", "Hard-coded connection strings in the source step", "A deployment rule for the server and database"], "A",
 "When you save a report with parameters as a .pbit, Desktop asks for the parameter values when the template is opened. A .pbids is a separate file type. Hard-coded strings can't prompt for anything."),

single("M2",
 "Only the latest partition of a 2-billion-row Import table needs reprocessing after a late correction. The rest of the model must not be refreshed. What should you use?",
 ["A partition-level refresh through XMLA, or the enhanced refresh REST API", "An on-demand refresh of the semantic model", "Republishing the .pbix with only that partition's data loaded", "A deployment pipeline redeploy of the model to the same stage"], "A",
 "With XMLA read-write you can refresh individual tables or partitions. The enhanced refresh REST API can too. A scheduled refresh processes whatever the policy says. Republishing replaces the whole model."),

match("M2",
 "Match each lifecycle requirement to the Fabric capability that meets it.",
 [("Keep a full change history of notebooks and models, and review changes in pull requests", "Git integration"),
  ("Promote the same tested content from Test to Production, pointing at each stage's own lakehouse", "Deployment pipeline with rules"),
  ("Change one measure in a shared model without republishing any report", "XMLA endpoint (read-write)"),
  ("List every report that will be affected before a warehouse table is dropped", "Impact analysis")],
 ["Git integration", "Deployment pipeline with rules", "XMLA endpoint (read-write)", "Impact analysis", "Capacity Metrics app"],
 "Each lifecycle capability has a distinct job: Git for history and review, pipelines for promotion, XMLA for changing the model's metadata in place, and impact analysis for dependencies. The Capacity Metrics app reports on compute and solves none of these."),

# ---------------- P1 (7)
multi("P1",
 "Which two requirements point to a lakehouse rather than a warehouse?",
 ["The data includes images and semi-structured JSON files", "The engineering team works mainly in PySpark", "Stored procedures must update rows inside multi-table transactions", "Report authors write T-SQL views only", "Data must be stored in Delta-Parquet format"], "AB",
 "Unstructured and semi-structured data and a Spark-first team both point to a lakehouse. T-SQL DML with transactions points to a warehouse. Both items store Delta-Parquet, so format doesn't decide anything. Views work in both."),

single("P1",
 "Lakehouse A has a OneLake security role that limits analysts to the EU rows of the Customers table. Lakehouse B contains a shortcut to that table. An analyst reads the shortcut from Lakehouse B. What does the analyst see?",
 ["Only the EU rows, because the target's security applies", "All rows, because Lakehouse B has no role defined", "No rows, because shortcuts can't carry row filters", "Only the rows created after the shortcut was made"], "A",
 "Internal shortcuts check access against the target using the user's identity, so OneLake security defined at the source applies. That stops shortcuts from becoming a way around security."),

yesno("P1",
 "For each statement about a mirrored database in Fabric, select Yes if it is true.",
 [("The replicated data is stored in OneLake in Delta format.", True),
  ("You can run UPDATE statements against the mirrored tables through the SQL analytics endpoint.", False),
  ("The mirrored data can be used in semantic models and joined with other Fabric data.", True)],
 "Mirroring lands the source data in OneLake as Delta, with a read-only SQL analytics endpoint. It's a replica, so changes come only from the source, and you can't update it through the endpoint. Because it's Delta in OneLake, other engines and semantic models can use it."),

single("P1",
 "A pipeline must start as soon as a new file arrives in a storage folder, not on a schedule. What should you configure?",
 ["An event trigger on file creation in the folder", "A schedule trigger that runs every minute", "A deployment rule on the storage path", "An Until loop that polls the folder"], "A",
 "Storage event triggers, configured through the Real-Time hub and Activator, start a pipeline when a file is created. Polling on a schedule adds delay and wastes runs."),

single("P1",
 "In a notebook attached to a lakehouse, which path reads the Delta table behind a Tables-folder shortcut named `partner_prices`?",
 ["spark.read.format(\"delta\").load(\"Tables/partner_prices\")", "spark.read.csv(\"Files/partner_prices.csv\")", "external_table(\"partner_prices\")", "SELECT * FROM OPENROWSET('partner_prices')"], "A",
 "A Tables shortcut appears as a table under Tables/, so Spark reads it like any Delta table. You can also use spark.read.table(\"partner_prices\"). external_table is KQL, and the CSV path assumes a file that doesn't exist."),

single("P1",
 "Data engineers want to be alerted, and to start a clean-up job, whenever an item is deleted in a production workspace. Which Fabric surface exposes these workspace item events so you can act on them?",
 ["The Real-Time hub, with an Activator rule", "The OneLake catalog's Govern tab", "The deployment pipeline history", "The workspace's lineage view"], "A",
 "The Real-Time hub lists streaming sources and system events, including Fabric workspace item events and OneLake events. Activator rules can respond to them with alerts or actions. The OneLake catalog is for discovering stored data."),

single("P1",
 "A team is choosing a store for a new self-service relational data mart that analysts will manage with SQL in Fabric. Which item fits the current platform?",
 ["A warehouse", "A Power BI datamart", "An Eventhouse", "A KQL queryset"], "A",
 "Microsoft now points self-service SQL workloads to the Fabric warehouse. Power BI datamarts are the legacy option and are being replaced. Eventhouse is for event data, and a queryset isn't a store."),

# ---------------- P2 (7 + 1 in case)
single("P2",
 "A notebook rebuilds the silver table `customers_clean` from scratch every night. Which write mode replaces the existing contents?",
 [".mode(\"overwrite\").saveAsTable(\"customers_clean\")", ".mode(\"append\").saveAsTable(\"customers_clean\")", ".mode(\"ignore\").saveAsTable(\"customers_clean\")", ".mode(\"errorifexists\").saveAsTable(\"customers_clean\")"], "A",
 "overwrite replaces the table's contents, and Delta keeps the old version for time travel. append would add duplicates every night. ignore skips the write if the table exists. errorifexists fails."),

single("P2",
 "A source has added a new column, and appending to the existing Delta table now fails with a schema-mismatch error. The new column must be added to the table. What should you do?",
 ["Write with .option(\"mergeSchema\", \"true\")", "Drop the new column every time", "Convert the table to CSV", "Use .mode(\"ignore\")"], "A",
 "Delta enforces the table schema by default. mergeSchema allows an additive change, such as a new column, to evolve the schema during the write. Dropping the column loses data, and ignore skips the write entirely."),

single("P2",
 "A 3-billion-row gold table is almost always filtered by month. When does partitioning the Delta table by a Year/Month column make sense?",
 ["When each partition stays large, well above about 1 GB", "Always, by the most detailed date column", "When the column has millions of distinct values", "Never, because Direct Lake can't read partitions"], "A",
 "Partitioning helps when queries filter on a low-cardinality column and each partition is still large. Partitioning by high-cardinality columns creates many small files, which hurts Direct Lake and Spark. Fabric supports partitioned Delta tables."),

single("P2",
 "A Dataflow Gen2 imports a budget sheet with the columns Department, Jan, Feb, …, Dec. The gold table needs Department, Month and Amount columns. Which step should you use?",
 ["Select Department, then Unpivot other columns", "Select Department, then Pivot column", "Transpose, then promote headers", "Group by Department, summing the months"], "A",
 "Unpivot other columns turns the 12 month columns into Month and Value rows, while Department stays as it is. It also keeps working if new months are added. Pivot does the opposite. Transpose swaps rows and columns completely. Grouping by Department sums the months away."),

single("P2",
 "Two DataFrames hold the same customer columns in a different order, and one also has an extra column, Loyalty. They must be stacked into one DataFrame. Which call is correct?",
 ["df1.unionByName(df2, allowMissingColumns=True)", "df1.union(df2).distinct()", "df1.join(df2, \"CustomerID\", \"outer\")", "df1.crossJoin(df2).dropDuplicates()"], "A",
 "unionByName matches columns by name rather than position, and allowMissingColumns fills absent columns with null. union matches by position, so it would misalign the columns, and distinct doesn't fix that. Joins combine columns, not rows."),

single("P2",
 "A warehouse load must add an AgeBand attribute (\"<25\", \"25–44\", \"45–64\", \"65+\") to DimCustomer, based on BirthDate. Where should this enrichment happen?",
 ["In the gold load, as a CASE expression in the DimCustomer procedure", "As a DAX calculated column in each semantic model", "In each report as a visual calculation", "In a Power Query step in each user's report"], "A",
 "Enriching the data in the gold layer means it's calculated once, stored, and available to every consumer and tool. Calculated columns in each model repeat the logic, and a Direct Lake on SQL model can't have them anyway."),

single("P2",
 "A table records each order's dates as it moves through its lifecycle: ordered, packed, shipped and delivered. Each row is updated as the order progresses. Which fact table type is this?",
 ["Accumulating snapshot fact", "Transaction fact", "Periodic snapshot fact", "Factless fact"], "A",
 "An accumulating snapshot has one row per process instance, with several date keys that are filled in as milestones happen. A transaction fact records events that are never updated. A periodic snapshot records state at regular intervals. A factless fact records events with no measures."),

# ---------------- P3 (5 + 1 in case)
single("P3",
 "You need customers who bought both Product A and Product B, in any orders. Which T-SQL pattern is correct?",
 ["SELECT CustomerKey FROM gold.FactSales WHERE ProductKey IN (@A, @B) GROUP BY CustomerKey HAVING COUNT(DISTINCT ProductKey) = 2;",
  "SELECT DISTINCT CustomerKey FROM gold.FactSales WHERE ProductKey = @A AND ProductKey = @B;",
  "SELECT DISTINCT CustomerKey FROM gold.FactSales WHERE ProductKey IN (@A, @B) ORDER BY CustomerKey;",
  "SELECT CustomerKey FROM gold.FactSales WHERE ProductKey IN (@A, @B) GROUP BY CustomerKey HAVING COUNT(*) = 2;"], "A",
 "Filtering to the two products and requiring two distinct products per customer finds the customers who bought both. A single row can't equal A AND B. IN without HAVING returns customers who bought either one. COUNT(*) = 2 counts rows, so a customer who bought A twice also qualifies."),

single("P3",
 "A KQL query ends with `| summarize count() by Country`. What is the name of the count column in the result, if you don't name it?",
 ["count_", "Count", "rows", "_count"], "A",
 "KQL names an unnamed aggregate by its function plus an underscore, so count() becomes count_. You'd then write | order by count_ desc. Give it a name, such as Events = count(), for clarity.", fixed=True),

single("P3",
 "Which KQL filter returns only today's events, from midnight UTC onwards?",
 ["| where Timestamp >= startofday(now())", "| where Timestamp > ago(1d)", "| where Timestamp == today()", "| where day(Timestamp) = 1"], "A",
 "startofday(now()) is midnight today, UTC. ago(1d) is a rolling 24 hours, which includes part of yesterday. today() isn't a KQL function, and == against a timestamp would match only one instant."),

single("P3",
 "A DAX query must list every product category, including those with no sales, which should show 0. Which query does this?",
 ["EVALUATE ADDCOLUMNS(VALUES('Product'[Category]), \"Sales\", [Total Sales] + 0)",
  "EVALUATE SUMMARIZECOLUMNS('Product'[Category], \"Sales\", [Total Sales])",
  "EVALUATE FILTER(VALUES('Product'[Category]), [Total Sales] > 0)",
  "EVALUATE TOPN(10, VALUES('Product'[Category]))"], "A",
 "ADDCOLUMNS over VALUES keeps every category, and + 0 turns blanks into zeros. SUMMARIZECOLUMNS drops rows where the measure is blank. The FILTER query removes categories with no sales on purpose. TOPN returns ten arbitrary categories."),

single("P3",
 "In the Visual Query Editor, a business user needs total quantity per warehouse location. Which operation should they add after selecting the table?",
 ["Group by Location, with Sum of Quantity", "Merge queries on Location", "Append queries, one per location", "Remove duplicates on Location"], "A",
 "Group by with an aggregation produces one row per location with the total. The editor turns it into a GROUP BY in the generated SQL."),

# ---------------- S1 (5 + 1 in case)
single("S1",
 "A model has FactSales and FactReturns. Users want to compare sales and returns by Product and Date. How should the facts be connected?",
 ["Through shared (conformed) Product and Date dimensions, each related to both facts", "With a direct relationship between FactSales and FactReturns on OrderID", "By merging the two facts into one table", "With a bidirectional many-to-many relationship between the facts"], "A",
 "In a star schema, facts are analysed together through conformed dimensions. Relating facts directly creates ambiguous paths and grain problems. Merging facts with different grains corrupts both."),

single("S1",
 "Which measure returns revenue for the previous month, using standard time intelligence over a marked date table?",
 ["CALCULATE([Revenue], DATEADD('Date'[Date], -1, MONTH))", "CALCULATE([Revenue], PREVIOUSYEAR('Date'[Date]))", "[Revenue] - 1", "CALCULATE([Revenue], 'Date'[MonthNumber] - 1)"], "A",
 "DATEADD shifts the current dates back by one month. PREVIOUSYEAR returns the previous year. Subtracting 1 from the measure, or from a MonthNumber column inside CALCULATE, isn't a valid way to shift the date context."),

single("S1",
 "In a calculation group, most items should keep the base measure's own format string, and only the YoY % item should show as a percentage. What should the format string expression of the other items return?",
 ["SELECTEDMEASUREFORMATSTRING()", "\"0.00%\"", "SELECTEDMEASURENAME()", "FORMAT(SELECTEDMEASURE(), \"General\")"], "A",
 "SELECTEDMEASUREFORMATSTRING() returns the format string of the measure being modified, so currency stays currency and counts stay counts. A fixed percentage format would mislabel everything else. FORMAT returns text."),

single("S1",
 "Users choose N (5, 10 or 20) from a slicer, and a measure must show sales only for the top N products. The slicer's table must not filter the model. What should you build?",
 ["A disconnected table of N values, read with SELECTEDVALUE in a TOPN measure", "An N table related to Product, read with SELECTEDVALUE", "A calculation group with Top 5, Top 10 and Top 20 items", "A field parameter over Top 5, Top 10 and Top 20 measures"], "A",
 "A disconnected table drives the slicer without filtering any data. The measure reads the chosen value with SELECTEDVALUE and applies it with TOPN or a rank test. A relationship would filter products by the numbers 5, 10 or 20."),

multi("S1",
 "Which two are valid reasons to turn on large semantic model storage format?",
 ["The model is expected to grow past the default size limit after refresh in the service", "You want to use query scale-out for the model", "The model is a small DirectQuery model in a shared (Pro) workspace", "You want to add RLS roles", "The model is published to My workspace"], "AB",
 "Large format lifts the size ceiling and is a prerequisite for query scale-out. Microsoft also recommends it for models managed through XMLA. It isn't available on shared capacity or My workspace, and it has nothing to do with RLS."),

# ---------------- S2 (6)
single("S2",
 "Performance Analyzer shows a visual with a short DAX query time but a long Other time. What does this usually mean?",
 ["It was waiting on other visuals, often because the page has too many", "The storage engine is slow to scan the fact table", "The model has outgrown small storage format", "The DAX measure is evaluated twice and needs variables"], "A",
 "Other is time spent waiting, mostly for other visuals to finish, along with background work. A high Other with a fast query points to too many visuals on the page, not to slow DAX."),

yesno("S2",
 "Goal: a Direct Lake model over a central lakehouse must include calculated tables and an Import table of targets. Security is managed in the semantic model. For each proposed configuration, select Yes if it meets the goal.",
 [("Direct Lake on OneLake", True),
  ("Direct Lake on the SQL analytics endpoint", False),
  ("DirectQuery over the SQL analytics endpoint, with no Direct Lake", False)],
 "Direct Lake on OneLake supports composite models and calculated tables, and here security lives in the model rather than in SQL. The SQL endpoint variant supports neither composite models nor calculated tables. DirectQuery gives up Direct Lake."),

single("S2",
 "A model has several many-to-many relationships set to filter in both directions, added “just in case”. Queries are slow and some totals look wrong. What should you do first?",
 ["Make relationships single-direction, using CROSSFILTER in the measures that need it", "Turn on large semantic model storage format", "Add more bidirectional relationships so every path is equally valid", "Convert the slow measures into calculated columns on the facts"], "A",
 "Bidirectional filtering adds work to queries and can create ambiguous paths. Single-direction relationships, with CROSSFILTER only where a measure needs it, are faster and more predictable."),

single("S2",
 "An incremental refresh on a SQL-sourced table takes as long as a full refresh. What is the most likely cause?",
 ["The RangeStart/RangeEnd filter doesn't fold to the source", "The table has too few rows to split into partitions", "Detect data changes is switched on for the table", "The model uses large semantic model storage format"], "A",
 "If the filter doesn't fold, each partition query brings back everything and filters it locally, so incremental refresh becomes slower than a full refresh. Check folding (View native query) and move steps that break folding later in the query."),

single("S2",
 "A Delta table gets frequent updates and deletes, which leave deletion vectors behind. Queries have slowed down, although there are few small files. Which maintenance action is designed to rewrite the affected files?",
 ["Run OPTIMIZE to rewrite files and purge their deletion vectors", "Run VACUUM with a retention of 0 hours to clear the vectors", "Turn off V-Order so update and delete rewrites are cheaper", "Refresh the Direct Lake model more often"], "A",
 "OPTIMIZE compacts files and purges deletion vectors from files where enough rows are marked deleted. Auto compaction may not trigger without small files. VACUUM removes unreferenced files and, with zero retention, puts time travel and running readers at risk."),

single("S2",
 "A table visual on a report returns every one of 1.2 million transaction rows, and users only ever look at the largest ones. What change helps most?",
 ["Apply a Top N filter, or summarise with drill-through to detail", "Split the table into two side-by-side tables of half the rows", "Turn off query caching for the report", "Add a slicer for every column so users can narrow the rows"], "A",
 "Returning fewer rows means less work in the query and in rendering. A Top N filter, or aggregation with drill-through, keeps the visual responsive. Extra columns make it worse."),

# ---------------- Case study (M2, P2, P3, S1)
case("Adventure Works Cycles",
 "Adventure Works Cycles builds bicycles in three plants. A lakehouse, LH_Gold, is built with notebooks. A Direct Lake semantic model serves sales and inventory reports. The workspaces Dev, Test and Prod are linked by a deployment pipeline, and Dev is connected to an Azure DevOps repository.\n\nFour developers currently edit the Dev workspace at the same time and overwrite each other's work. Inventory is counted at the end of every day for each product and warehouse.",
 ["R1. Each developer must work in isolation, and their changes must be reviewed before they reach the shared Dev workspace.",
  "R2. Daily inventory levels must be stored so trends over time can be analysed.",
  "R3. A SQL report must compare each month's revenue with the same month in the previous year.",
  "R4. The inventory measure must show the level on the last day of the selected period, not a sum across days."],
 [
  single("M2", "Which practice satisfies R1?",
   ["Each developer branches out to their own workspace and merges through a pull request", "Everyone keeps editing the Dev workspace, but commits after every change", "Add a Feature stage before Dev in the deployment pipeline", "Turn off Git integration and share .pbip folders by email"], "A",
   "Branch out gives each developer an isolated branch and workspace, and pull requests are where review happens. Committing more often doesn't stop people overwriting each other. Pipeline stages are for promotion, not for isolating feature work."),
  single("P2", "Which gold-layer design satisfies R2?",
   ["A periodic snapshot fact: one row per product, warehouse and day", "A transaction fact of stock movements only", "An accumulating snapshot fact with one row per product", "One row per product and warehouse, overwritten daily"], "A",
   "A periodic snapshot records the state at regular intervals, which is exactly daily inventory levels. Movements alone would have to be summed from the start of time for every query. Overwriting destroys the history."),
  single("P3", "Which T-SQL expression satisfies R3, given a monthly table with one row per month and no gaps?",
   ["LAG(Revenue, 12) OVER (ORDER BY MonthStart) AS RevenueSameMonthLastYear", "LEAD(Revenue, 12) OVER (ORDER BY MonthStart)", "SUM(Revenue) OVER (ORDER BY MonthStart ROWS 12 PRECEDING)", "RANK() OVER (ORDER BY MonthStart)"], "A",
   "LAG with an offset of 12 returns the value from 12 rows earlier, which is the same month last year when the months are contiguous. LEAD looks forward. The SUM gives a rolling total. If months could be missing, use a date-keyed join instead."),
  single("S1", "Which measure satisfies R4?",
   ["CALCULATE(SUM(FactInventory[QtyOnHand]), LASTNONBLANK('Date'[Date], CALCULATE(SUM(FactInventory[QtyOnHand]))))", "CALCULATE(SUM(FactInventory[QtyOnHand]), DATESBETWEEN('Date'[Date], MIN('Date'[Date]), MAX('Date'[Date])))", "AVERAGEX(VALUES('Date'[Date]), CALCULATE(SUM(FactInventory[QtyOnHand])))", "MAXX(VALUES('Date'[Date]), CALCULATE(SUM(FactInventory[QtyOnHand])))"], "A",
   "Inventory is semi-additive: you can add it across products and warehouses, but not across time. LASTNONBLANK finds the last date in the period that has data and evaluates the quantity there. DATESBETWEEN over the period still adds the days together. The daily average and the highest daily level aren't the closing balance."),
 ]),
]
