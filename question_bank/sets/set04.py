from model import single, multi, yesno, match, order, case

TITLE = "Core — governing what you build"
SUBTITLE = "Access control at every layer, ALM habits, and the modelling choices that keep numbers right."
LEVEL = "Level 2 · Core"
CASE_NAME = "Woodgrove Bank"

ITEMS = [
# ---------------- M1 (6)
single("M1",
 "An external auditor must run T-SQL queries against one warehouse for a month. They must not see any other item in the workspace. What should you do, following least privilege?",
 ["Share the warehouse with Read and ReadData, and no workspace role", "Add the auditor to the workspace with the Viewer role", "Add the auditor to the workspace with the Contributor role", "Share the warehouse with Read and Write permissions"], "A",
 "Sharing the item gives access to that one item only, and ReadData lets the auditor query it through T-SQL. Any workspace role exposes every item in the workspace. Write gives far more than querying."),

single("M1",
 "In a shared semantic model, the Payroll table and its measures must not appear in the field list for anyone outside HR. They mustn't even know the table exists. What should you implement?",
 ["Object-level security on the Payroll table, set in Tabular Editor", "Row-level security that filters out every Payroll row", "Hide the Payroll table and its measures in Desktop", "A Highly Confidential label on the Payroll table"], "A",
 "OLS takes the table and its dependent measures out of the model's metadata for users in the role, so they can't see it or query it. RLS still shows the table, just empty. Hiding a table only affects the field list in Desktop and isn't security. Labels can't be applied to individual tables."),

match("M1",
 "Match each requirement to the access-control mechanism that meets it.",
 [("Branch managers see only their branch's loan rows", "Row-level security"),
  ("The CreditScore column returns an error for most analysts, but their other columns still work", "Column-level security"),
  ("Agents see card numbers as XXXX-XXXX-XXXX-1234", "Dynamic data masking"),
  ("Only the Fraud team can read the Files/evidence folder in a lakehouse", "OneLake folder-level security"),
  ("The Bonus measure is invisible to everyone outside Compensation", "Object-level security")],
 ["Row-level security", "Column-level security", "Dynamic data masking", "OneLake folder-level security", "Object-level security"],
 "RLS filters rows. CLS blocks access to columns, so queries that reference them fail. Masking shows obscured values while the column can still be queried. OneLake security roles govern folders and tables in the lake. OLS removes model objects from users' view entirely."),

multi("M1",
 "Which two statements about endorsement in Fabric are true?",
 ["Any user with write permission on an item can mark it as Promoted.", "Only users the Fabric administrator authorises can certify items.", "Certifying a semantic model gives every user in the tenant read access to it.", "An item can carry both Promoted and Certified at the same time.", "Endorsement can only be applied to reports."], "AB",
 "Promoted is self-service. Certified (and Master data) is limited to users the administrator authorises. Endorsement helps people find and trust an item but grants no access. An item has one endorsement at a time. Many item types can be endorsed, not just reports."),

single("M1",
 "Fabric administrators want one place to see how sensitivity labels and endorsement are used across the tenant, with links into Microsoft Purview. What should they use?",
 ["The Microsoft Purview hub in Fabric", "The Capacity Metrics app", "A deployment pipeline", "The lineage view of one workspace"], "A",
 "The Purview hub shows governance insights, such as sensitivity label coverage and endorsement, with links to Purview solutions. Capacity Metrics covers compute. Lineage covers one workspace's dependencies."),

single("M1",
 "Each salesperson may cover several regions, and each region has several salespeople. The mapping is in a table UserRegion(UPN, RegionKey), which relates to DimRegion. How should you implement dynamic RLS in the semantic model?",
 ["A role filtering UserRegion[UPN] = USERPRINCIPALNAME(), flowing through DimRegion to the facts", "A role filtering DimRegion[Region] = USERNAME(), flowing to the facts", "One static role per region, with users added to each role by hand", "Object-level security that hides the other regions' columns"], "A",
 "Filtering the mapping table by the signed-in user's UPN and letting that filter reach DimRegion and the facts (using bidirectional filtering applied as a security filter where needed) handles many-to-many coverage with one role. Static roles per region become an administrative burden. USERNAME compared with a region name doesn't match users to their regions."),

# ---------------- M2 (5 + 1 in case)
yesno("M2",
 "For each statement about deployment pipelines, select Yes if it is true.",
 [("You can deploy only selected items from one stage to the next, not the whole workspace.", True),
  ("Deploying overwrites the paired items in the target stage.", True),
  ("A deployment pipeline keeps a line-by-line history of model changes for pull-request review.", False)],
 "Pipelines support selective deployment and overwrite paired items. They're for promoting content, not version control. Line-level history and pull requests come from Git integration."),

single("M2",
 "You select Update in a Git-connected workspace and are told there are conflicts. The same notebook was changed in the workspace and in the branch. What should you do?",
 ["Resolve the conflict in the source control pane, or in the repository, then update", "Delete the notebook from the workspace, then select Update again", "Disconnect Git, keep the workspace version, then reconnect", "Overwrite the notebook from a deployment pipeline, then commit"], "A",
 "Fabric reports conflicts when an item changed on both sides. You can keep one side from the workspace UI, or resolve it in Git (for example in a branch and pull request) and then update. Disconnecting Git, deleting the notebook or overwriting it from a pipeline throws away one side's changes without a decision."),

single("M2",
 "You must compare a development semantic model with production and deploy only the measures that changed, without touching partitions or data. Which tool is designed for this, through the XMLA endpoint?",
 ["ALM Toolkit", "The Capacity Metrics app", "Power BI Report Builder", "The OneLake file explorer"], "A",
 "ALM Toolkit compares two models' metadata and deploys only the selected differences through the XMLA endpoint. Report Builder is for paginated reports. The file explorer browses OneLake files."),

multi("M2",
 "The skills outline asks you to perform impact analysis of downstream dependencies. Which three item types does it name as starting points?",
 ["Lakehouses", "Warehouses", "Semantic models", "Individual DAX measures", "Report themes"], "ABC",
 "The outline names lakehouses, warehouses, dataflows and semantic models. Impact analysis works at the item level, not on single measures or themes."),

single("M2",
 "A developer works in Power BI Desktop with a .pbip project in a local clone of the repository. How do the changes reach the Git-connected Fabric workspace?",
 ["They commit and push from the local clone, often through a pull request, then select Update in the workspace", "They publish the .pbip file from the Publish button, which also commits to Git", "Deployment pipelines pull .pbip files from local disks", "They email the folder to the workspace admin"], "A",
 "Local projects go through the normal Git flow: commit, push and merge. The workspace then picks up the changes with Update from the source control pane. Publishing from Desktop puts content in the workspace without creating any Git commit."),

# ---------------- P1 (6 + 1 in case)
single("P1",
 "A data engineering team uses Spark for bronze and silver, and a BI team writes T-SQL and wants stored procedures for gold. What architecture fits both teams?",
 ["Lakehouse for bronze and silver, warehouse for gold", "Warehouse for every layer", "Eventhouse for every layer", "Lakehouse for every layer, with stored procedures on its SQL analytics endpoint"], "A",
 "Splitting the layers by skill set is the recommended approach. Both items store Delta in OneLake, so the split costs nothing downstream. Stored procedures on a lakehouse endpoint can't write data, and an eventhouse is for event data."),

multi("P1",
 "Which two sources can be mirrored into Fabric?",
 ["Azure SQL Database", "Snowflake", "An Amazon S3 bucket of CSV files", "A SharePoint folder of Excel files", "Google Cloud Storage"], "AB",
 "Mirroring replicates databases and data warehouses, including Azure SQL Database, Snowflake, Azure Cosmos DB and Azure Database for PostgreSQL. Object stores and file folders are reached with shortcuts or ingestion instead."),

single("P1",
 "Notebooks read the same Amazon S3 data through a shortcut many times a day, and the cloud egress charges are high. Which Fabric feature can reduce them?",
 ["Turn on shortcut caching for the workspace", "Convert the shortcut to a mirrored database", "Use V-Order on the S3 files", "Add more capacity units"], "A",
 "Shortcut caching keeps files read from external sources such as S3 or Google Cloud Storage in OneLake for a set period, so repeated reads don't pay egress again. V-Order is a write-time setting for Delta tables you write. You can't apply it to files you don't own."),

single("P1",
 "A Dataflow Gen2 loads the full daily product list into a lakehouse table, and the table must always hold just the current list. Which destination update method should you choose?",
 ["Replace", "Append", "Merge with history", "Insert only new rows"], "A",
 "Replace overwrites the table on each refresh, so it always holds the latest full list. Append adds the rows again on every run and creates duplicates."),

single("P1",
 "Parquet files land in ADLS Gen2 every hour and must be loaded into a Fabric Warehouse table with T-SQL, at high throughput. Which statement should you use?",
 ["COPY INTO", "BULK INSERT from a local path", "INSERT ... VALUES", "CREATE EXTERNAL TABLE"], "A",
 "COPY INTO is the warehouse's high-throughput command for loading files from external storage. INSERT ... VALUES inserts literal rows one statement at a time. BULK INSERT from a local path isn't the warehouse's pattern for cloud files."),

single("P1",
 "An analyst wants to find semantic models that are certified and belong to the Finance domain, then request access to one. Where should they start?",
 ["The OneLake catalog, filtered by domain and endorsement", "The Real-Time hub, filtered by domain", "The Capacity Metrics app, filtered by workspace", "A KQL queryset over the workspace metadata"], "A",
 "The OneLake catalog is the discovery surface for stored data items. It can be filtered by domain, item type and endorsement, and it supports access requests. The Real-Time hub is for streaming data."),

# ---------------- P2 (7 + 1 in case)
multi("P2",
 "You are building a Type 2 slowly changing customer dimension. Which three columns does the design need?",
 ["A surrogate key that's unique per version", "Validity dates such as ValidFrom and ValidTo", "A current-row flag such as IsCurrent", "A GUID copied from the source on every load", "The customer's total sales"], "ABC",
 "Each version needs its own surrogate key, so facts can point at the version that was current when the transaction happened. Validity dates and a current flag make history and current-state queries simple. Totals belong in facts, not dimensions."),

single("P2",
 "You need the product categories whose total revenue is over 1,000,000. Which clause filters on the aggregated value?",
 ["HAVING SUM(Revenue) > 1000000", "WHERE SUM(Revenue) > 1000000", "WHERE Revenue > 1000000", "ORDER BY SUM(Revenue) DESC"], "A",
 "HAVING filters groups after aggregation. WHERE runs before grouping and can't use aggregate functions. Filtering individual rows over 1,000,000 answers a different question.",
 code="""SELECT p.Category, SUM(f.Revenue) AS Revenue
FROM gold.FactSales f JOIN gold.DimProduct p ON p.ProductKey = f.ProductKey
GROUP BY p.Category
______;"""),

single("P2",
 "Each JSON order document holds an array `items`. You need one row per order item in a DataFrame. Which function should you use?",
 ["F.explode(\"items\")", "F.split(\"items\", \",\")", "F.collect_list(\"items\")", "F.flatten(\"orders\")"], "A",
 "explode turns each element of an array column into its own row. split turns a string into an array. collect_list does the reverse of explode. flatten merges nested arrays but doesn't create rows."),

single("P2",
 "A DataFrame read from JSON has a struct column `address` with fields `city` and `postcode`. How do you select the city as its own column?",
 ["F.col(\"address.city\").alias(\"City\")", "F.explode(\"address\").alias(\"City\")", "F.col(\"city.address\").alias(\"City\")", "F.split(\"address\", \".\").getItem(0)"], "A",
 "Dot notation reaches into struct fields. city.address reverses the path. explode is for arrays and maps, and split works on strings, not structs."),

single("P2",
 "A spreadsheet export lists Region only on the first row of each block, and the rows below have null Region. In Dataflow Gen2, how do you fill the nulls with the value above?",
 ["Select Region and use Fill down", "Select Region and use Replace errors", "Select Region and use Remove blank rows", "Select Region and use Unpivot other columns"], "A",
 "Fill down copies the last non-null value into the null cells below it, which is exactly what grouped spreadsheet exports need. The other steps remove or reshape data instead."),

single("P2",
 "Which data type should a gold warehouse table use for monetary amounts so that totals reconcile exactly?",
 ["decimal(19,4)", "float(53)", "varchar(50)", "real"], "A",
 "decimal is exact. float and real are approximate binary types and can give rounding differences when you add up large numbers of values. Storing money as text stops arithmetic and compresses badly."),

single("P2",
 "Testers need an instant copy of a large warehouse fact table to run destructive tests against, without duplicating the data files. Which statement should you use?",
 ["CREATE TABLE test.FactSales AS CLONE OF gold.FactSales;", "SELECT * INTO test.FactSales FROM gold.FactSales;", "CREATE VIEW test.FactSales AS SELECT * FROM gold.FactSales;", "BACKUP TABLE gold.FactSales;"], "A",
 "A zero-copy clone creates a new table that refers to the same underlying data files, so it's instant. Changes made afterwards affect only the clone. SELECT INTO copies all the data. A view can't take destructive writes. BACKUP TABLE isn't a warehouse command."),

# ---------------- P3 (6)
single("P3",
 "You need the top three products by revenue in each category, with tied products sharing a rank. Which T-SQL pattern is correct?",
 ["DENSE_RANK() OVER (PARTITION BY Category ORDER BY Revenue DESC) <= 3, filtered in an outer query", "SELECT TOP (3) WITH TIES ... ORDER BY Category, Revenue DESC", "GROUP BY Category, Product HAVING COUNT(*) <= 3, ordered by Revenue DESC", "ROW_NUMBER() OVER (PARTITION BY Category ORDER BY Revenue DESC) <= 3, in an outer query"], "A",
 "Partitioning by category restarts the ranking in each category, and DENSE_RANK lets tied products share a rank. ROW_NUMBER with the same partition is close, but it breaks ties arbitrarily, so a tied product can be dropped. TOP (3) WITH TIES returns three rows overall, not per category. The HAVING COUNT(*) query counts rows, not ranks."),

single("P3",
 "Which KQL query returns error messages that contain the term “timeout” from the last six hours?",
 ["AppLogs | where Timestamp between (ago(6h) .. now()) and Level == \"Error\" and Message has \"timeout\"",
  "AppLogs | where Timestamp > ago(6h) and Level = \"Error\" and Message = \"timeout\"",
  "SELECT * FROM AppLogs WHERE Level = 'Error' AND Message LIKE '%timeout%' AND Timestamp > ago(6h)",
  "AppLogs | where Timestamp > ago(6h) | project Level == \"Error\", Message has \"timeout\""], "A",
 "between with a time range and has for whole-term matching is idiomatic, efficient KQL. In KQL, = isn't a comparison operator (use ==), and Message == 'timeout' would match only messages that are exactly that word. The SELECT option is SQL. project can't filter rows."),

single("P3",
 "In KQL, you need a column `Status` that shows \"Hot\" when Temperature > 80 and \"OK\" otherwise. Which expression is correct?",
 ["| extend Status = iff(Temperature > 80, \"Hot\", \"OK\")", "| project Status = CASE WHEN Temperature > 80 THEN 'Hot' END", "| summarize Status = max(Temperature)", "| where Temperature > 80"], "A",
 "iff() is KQL's conditional function, and extend adds the result as a column. CASE WHEN is SQL syntax. summarize aggregates. where filters rows."),

single("P3",
 "A DAX query using SUMMARIZECOLUMNS('Product'[Name], \"Sales\", [Total Sales]) returns fewer products than the Product table holds. What is the most likely reason?",
 ["SUMMARIZECOLUMNS drops rows where all its measures return BLANK", "SUMMARIZECOLUMNS returns at most 1,000 rows", "The query needs ORDER BY to return all rows", "Products with duplicate names are merged into one row"], "A",
 "SUMMARIZECOLUMNS automatically drops rows where all the expressions return blank, which is usually what you want. To include products with no sales, make the measure return 0 or use ADDCOLUMNS over VALUES. There's no fixed row cap, ORDER BY only sorts, and products with the same name are grouped by design, not by accident."),

single("P3",
 "In the Visual Query Editor, an analyst needs to add each order's customer segment from the Customer table. Which step should they use?",
 ["Merge queries, joining Orders to Customer on CustomerKey", "Append queries, adding Customer to Orders", "Group by CustomerKey with a Max of Segment", "Keep top rows from Customer, ordered by CustomerKey"], "A",
 "Merge joins two queries on a key and adds columns from the second one. The Visual Query Editor turns it into a SQL JOIN. Append unions rows."),

single("P3",
 "An auditor asks what `gold.DimCustomer` looked like at 09:00 UTC yesterday. The warehouse's data retention period covers that time. Which T-SQL feature answers this without restoring a backup?",
 ["Time travel: OPTION (FOR TIMESTAMP AS OF '<yesterday 09:00 UTC>')", "SELECT * FROM gold.DimCustomer WHERE ModifiedAt <= '<yesterday 09:00>'", "SELECT * FROM gold.DimCustomer FOR SYSTEM_TIME AS OF '<yesterday 09:00>'", "Restore the warehouse to a new restore point first"], "A",
 "Warehouse time travel queries a table as it was at a past point in time, within the retention period, using the FOR TIMESTAMP AS OF query hint. A WHERE on ModifiedAt doesn't bring back rows that were updated or deleted since. Restoring to a restore point is a restore, which the stem rules out. FOR SYSTEM_TIME AS OF is temporal-table syntax, which the Fabric Warehouse doesn't use."),

# ---------------- S1 (5 + 1 in case)
single("S1",
 "Every order line carries an OrderNumber that has no other attributes. How should OrderNumber be modelled in the star schema?",
 ["As a degenerate dimension: keep it on the fact table", "As its own dimension table with one column", "As a calculated table", "Remove it, because facts shouldn't carry text"], "A",
 "An identifier with no attributes of its own stays on the fact as a degenerate dimension. A one-column dimension adds a join for nothing. Removing it stops drill-down to individual orders."),

yesno("S1",
 "For each statement about large semantic model storage format, select Yes if it is true.",
 [("It's needed for a model to grow past the default size limit in the service.", True),
  ("Microsoft recommends it for models deployed and managed through the XMLA endpoint, even small ones.", True),
  ("It's supported on shared (Pro-only) capacity.", False)],
 "Large format lifts the size ceiling to the capacity's limit and improves XMLA write performance. It needs a Fabric F, Premium P, Embedded A or Premium Per User capacity, not shared capacity."),

single("S1",
 "A model has two calculation groups: Time Intelligence (YTD, PY) and Currency Conversion. YTD must be computed on values that have already been converted to the selected currency. What controls the order in which they apply?",
 ["The precedence property of each calculation group", "The alphabetical order of the group names", "The order of the slicers on the page", "The sort order of the calculation items"], "A",
 "When several calculation groups apply to the same measure, each group's precedence property decides the order in which they're applied. Set it on purpose so the currency conversion happens inside the YTD calculation. Names, slicer positions and item order within a group have no effect on this."),

single("S1",
 "A [Revenue] measure must display as 1.2K, 3.4M or 5.6bn depending on its size, while staying numeric for sorting. What should you implement?",
 ["A dynamic format string on the measure, chosen by its value", "Wrap the measure in FORMAT() with a scaled format", "Three separate measures, one per unit of scale", "A field parameter over three scaled measures"], "A",
 "A dynamic format string changes only how the value displays, so the measure stays numeric for sorting, totals and charts. FORMAT() returns text, which breaks numeric behaviour. A field parameter swaps fields; it doesn't format them."),

single("S1",
 "Which measure returns a three-month moving average of [Revenue] using DAX window functions?",
 ["AVERAGEX(WINDOW(-2, REL, 0, REL, ALLSELECTED('Date'[YearMonth]), ORDERBY('Date'[YearMonth])), [Revenue])",
  "AVERAGEX(OFFSET(-2, ALLSELECTED('Date'[YearMonth]), ORDERBY('Date'[YearMonth])), [Revenue])",
  "AVERAGEX(INDEX(3, ALLSELECTED('Date'[YearMonth]), ORDERBY('Date'[YearMonth])), [Revenue])",
  "CALCULATE(AVERAGE(Sales[Revenue]), DATESINPERIOD('Date'[Date], MAX('Date'[Date]), -3, DAY))"], "A",
 "WINDOW(-2, REL, 0, REL, ...) returns the current month and the two before it, and AVERAGEX averages [Revenue] across them. OFFSET(-2) returns only the single row two months back. INDEX(3) returns the third month in the selection. DATESINPERIOD with -3 DAY covers three days, not three months, and averages individual rows."),

# ---------------- S2 (6)
single("S2",
 "A measure `SUMX(Sales, [Margin])` is slow over 400 million rows, where [Margin] = SUM(Sales[Revenue]) - SUM(Sales[Cost]). Which rewrite returns the same result faster?",
 ["SUMX(Sales, Sales[Revenue] - Sales[Cost])", "SUMX(Sales, CALCULATE([Margin]))", "AVERAGEX(Sales, [Margin]) * COUNTROWS(Sales)", "IFERROR(SUMX(Sales, [Margin]), 0)"], "A",
 "Calling a measure inside an iterator causes context transition on every row. Using column arithmetic gives the same total and lets the storage engine do the work. Adding CALCULATE explicitly is the same context transition. IFERROR blocks optimisation."),

single("S2",
 "A gold table has a TransactionDateTime column precise to the second. It's the biggest column in the Direct Lake model and is used only to filter by date and hour. What should you do?",
 ["Split it into separate Date and Hour columns in gold", "Convert it to text in ISO 8601 format", "Hide it in the model and use a measure", "Add a surrogate GUID key for each timestamp"], "A",
 "Splitting a high-cardinality datetime cuts the number of distinct values dramatically, which shrinks dictionaries and speeds up queries. Hiding a column doesn't reduce its size. Text and GUIDs make compression worse."),

single("S2",
 "An Import fact uses incremental refresh with a daily refresh, but the business wants today's transactions to appear in near real time without refreshing more often. What should you configure?",
 ["The real-time DirectQuery option, which makes a hybrid table", "Automatic page refresh on the Import table's report", "A scheduled refresh every minute during business hours", "Detect data changes on a LastModified column"], "A",
 "The real-time option in incremental refresh adds a DirectQuery partition for the most recent period, which makes it a hybrid table. Historical partitions stay in Import. Detect data changes cuts refresh work but doesn't make data real time."),

multi("S2",
 "Which three can cause a Direct Lake on SQL analytics endpoint model to fall back to DirectQuery?",
 ["Querying a SQL view that isn't materialised", "Row-level security defined at the SQL analytics endpoint", "A query that exceeds a capacity guardrail", "A calculation group in the model", "A measure that uses variables"], "ABC",
 "Views, SQL-based granular security and guardrail breaches are documented fallback triggers. Calculation groups and DAX variables are fine in Direct Lake."),

single("S2",
 "After every framing, the first report queries on a Direct Lake model are slower and later ones are fast. What explains this?",
 ["The first queries transcode columns from Delta into memory", "Framing copies all the table data into memory", "The first query runs in Import mode to warm the cache", "The model falls back to DirectQuery after each framing"], "A",
 "Direct Lake loads columns on demand. After framing, a column's first use triggers transcoding from Parquet into memory, and later queries reuse the cached, warm data. Framing itself copies no data."),

single("S2",
 "Most report queries filter a gold Delta table by CustomerKey, which has high cardinality. Which table optimisation groups related values into the same files, so queries can skip the files they don't need?",
 ["OPTIMIZE ... ZORDER BY (CustomerKey)", "VACUUM", "Partitioning by CustomerKey", "Turning off V-Order"], "A",
 "Z-Order puts similar values together in the same files, so filters can skip files. It works alongside V-Order. Partitioning by a high-cardinality key creates many tiny files. VACUUM only removes unreferenced files."),

# ---------------- Case study (M2, P1, P2, S1)
case("Woodgrove Bank",
 "Woodgrove Bank is building a customer-analytics platform in Fabric. A card-processing partner sends nested JSON transaction files and scanned statement PDFs. The data engineering team writes PySpark. The BI team keeps a gold warehouse, WH_Customer, using T-SQL.\n\nCustomers can share accounts. Customers' home addresses change, and risk reporting must show the address that applied when each transaction happened. Workspaces exist for Dev, Test and Prod.",
 ["R1. Partner files must be landed as received, including the PDFs.",
  "R2. Address history must be kept in the gold customer dimension.",
  "R3. Every change must be reviewable in pull requests, and promotion to Prod must not need manual rebuilds.",
  "R4. Balances must be analysable by customer even though accounts are shared."],
 [
  single("P1", "Where should the raw partner files land to satisfy R1?",
   ["The Files area of a lakehouse", "A warehouse staging table", "An Eventhouse table", "An Import semantic model"], "A",
   "A lakehouse's Files area holds files in any format, including JSON and PDF, as they arrive, and PySpark can process them from there. Warehouses and eventhouses hold structured tables."),
  single("P2", "Which approach to the customer dimension satisfies R2?",
   ["Type 2: expire the current row and insert a new row with a new surrogate key", "Type 1: update the address on the current row in place", "Store the address on each fact row instead of the dimension", "Delete the old row and insert a new one with the same surrogate key"], "A",
   "Type 2 keeps every version with its own surrogate key, so each transaction joins to the address that was current at the time. Updating in place, or deleting and re-inserting with the same key, is Type 1 and loses history."),
  yesno("M2", "For each proposed design for R3, select Yes if it meets the requirement.",
   [("Connect the Dev workspace to Git, and use a deployment pipeline to promote from Dev to Test to Prod.", True),
    ("Use a deployment pipeline alone.", False),
    ("Download .pbix files from Dev and upload them to Prod by hand.", False)],
   "Git gives change history and pull-request review, and pipelines give repeatable promotion with rules. A pipeline alone keeps no change history. Manual upload is neither reviewable nor automated."),
  single("S1", "Which model design satisfies R4?",
   ["A CustomerAccount bridge between DimCustomer and DimAccount, with FactBalance related to DimAccount", "Relate FactBalance directly to DimCustomer with a one-to-many relationship", "Duplicate each balance row once for every account holder", "Merge DimCustomer and DimAccount into one wide dimension"], "A",
   "Shared accounts make the customer-to-account relationship many-to-many, and the standard design for that is a bridge table. Duplicating balance rows inflates totals. A direct one-to-many relationship can't express shared ownership."),
 ]),
]
