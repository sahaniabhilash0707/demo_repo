from model import single, multi, yesno, match, order, case

TITLE = "Exam standard — shaping the gold layer"
SUBTITLE = "Dimensional design in the data store, transformation idioms in T-SQL, PySpark and Power Query, plus the rest of the outline."
LEVEL = "Level 3 · Exam standard"
CASE_NAME = "Wide World Importers"

ITEMS = [
# ---------------- M1 (5 + 1 in case)
yesno("M1",
 "For each statement about item permissions on a shared warehouse or lakehouse, select Yes if it is true.",
 [("Read lets a user see the item and its metadata.", True),
  ("ReadData lets a user query the data through the SQL analytics endpoint.", True),
  ("ReadAll is the right choice when a user needs only T-SQL access and must not read the files.", False)],
 "Read covers the item's metadata, ReadData allows SQL queries, and ReadAll allows OneLake and Spark file access. For a T-SQL-only user, ReadData is the least privilege. ReadAll would expose the files."),

single("M1",
 "Which users can apply a sensitivity label to a semantic model?",
 ["Users with edit rights on the item who have the label in their policy", "Only Fabric administrators, from the tenant admin portal", "Any user who can view the model in the workspace", "Only capacity administrators for the model's capacity"], "A",
 "Labelling needs edit rights on the item and the label must be in a policy published to the user. Viewers can't change labels, and labelling isn't limited to administrators."),

single("M1",
 "Four hundred analysts need Viewer access to a workspace, and people join and leave every week. How should you grant access with the least administrative effort?",
 ["Assign an Entra security group to the Viewer role", "Add each analyst to the Viewer role by name", "Share each item with every analyst directly", "Give team leads Member so they can add analysts"], "A",
 "Granting roles to groups means joiners and leavers are handled in one place. Adding people individually and sharing item by item don't scale. Contributor gives too much access."),

single("M1",
 "Members of the Analysts database role must be able to query every current and future table in the gold schema of a warehouse, and nothing outside it. Which statement should you use?",
 ["GRANT SELECT ON SCHEMA::gold TO Analysts;", "GRANT SELECT ON DATABASE::WH TO Analysts;", "GRANT CONTROL ON SCHEMA::gold TO Analysts;", "GRANT SELECT ON gold.FactSales TO Analysts;"], "A",
 "A schema-level grant covers every object in the schema, including tables created later. A database-level grant reaches beyond gold. CONTROL gives full ownership-like rights. A single-table grant misses the other tables."),

single("M1",
 "Compliance wants to detect semantic models that contain credit card numbers and alert their owners automatically. What should you use?",
 ["Purview data loss prevention (DLP) policies", "Row-level security on card columns", "Certification with a review checklist", "Deployment rules that scan each release"], "A",
 "DLP policies scan supported Fabric items for sensitive information types, such as credit card numbers, and can show policy tips and send alerts. RLS filters rows. Endorsement shows trust. Deployment rules repoint data sources."),

# ---------------- M2 (6)
single("M2",
 "You connect a new workspace to an existing Git branch and choose Update. The semantic models appear, but their refreshes fail. What is the most likely reason?",
 ["Credentials aren't stored in Git, so they must be set again", "Git integration removes the models' data source steps", "The models were converted to DirectQuery on sync", "Git syncs the definitions but not the partitions"], "A",
 "Git holds item definitions, not secrets. After you sync a workspace from Git, you configure connections and credentials (or bind the models to existing connections) in that workspace."),

single("M2",
 "In a deployment pipeline, a report and its semantic model are deployed together from Dev to Test. Which model does the deployed report use in Test?",
 ["The paired semantic model in the Test stage (autobinding)", "The Dev semantic model", "No model, so you must rebind it manually", "A copy of the model embedded in the report"], "A",
 "Deployment pipelines autobind: a deployed report connects to the paired model in the same stage, so Test reports use Test models. Rebinding by hand is only needed in unusual setups."),

order("M2",
 "A developer edits a model in Power BI Desktop as a .pbip project inside a local clone of the team's repository. Put the steps to get the change into the Git-connected Dev workspace in order.",
 ["Save the project in Desktop",
  "Commit the changed files and push the branch",
  "Open a pull request and merge it into the Dev branch after review",
  "In the Dev workspace, select Update in the source control pane"],
 "The local Git flow is save, commit, push and pull request. Once the change is merged, the workspace picks it up with Update. Publishing from Desktop or using pipelines for this step skips the review.",
 extra=["Publish the .pbix to Production from Desktop", "Deploy from Dev to Test in the deployment pipeline"]),

single("M2",
 "Which address do you use to connect Tabular Editor to semantic models in the Fabric workspace “Sales Analytics” through the XMLA endpoint?",
 ["powerbi://api.powerbi.com/v1.0/myorg/Sales Analytics", "https://app.fabric.microsoft.com/groups/Sales Analytics", "abfss://Sales Analytics@onelake.dfs.fabric.microsoft.com", "Data Source=localhost:2383"], "A",
 "The workspace connection is powerbi://api.powerbi.com/v1.0/myorg/<workspace name>, which you'll find in the workspace settings. abfss is the OneLake storage path. The other options are a portal URL and a local Analysis Services port."),

single("M2",
 "What does a .pbids file contain?",
 ["Data source connection details only, as JSON", "The report pages and model, without data", "The model, report, data and credentials", "The report theme and page layout"], "A",
 "A .pbids is a small JSON file describing a connection. Opening it starts Get data in Desktop with the source filled in, and users still sign in themselves. The other options describe a .pbit, a .pbix and a theme file."),

yesno("M2",
 "For each statement about lineage view and impact analysis, select Yes if it is true.",
 [("Lineage view shows how data flows from sources through Fabric items to reports in a workspace.", True),
  ("Impact analysis on a semantic model can include dependent items in other workspaces.", True),
  ("Impact analysis automatically fixes the reports that a change would break.", False)],
 "Lineage visualises dependencies, and impact analysis lists the affected downstream items, including those in other workspaces, so you can notify their owners. Nothing gets fixed automatically. Planning and fixing the change is still your job."),

# ---------------- P1 (6 + 1 in case)
match("P1",
 "Match each workload to the most appropriate Fabric data store.",
 [("A Spark team lands JSON, Parquet and images for a medallion architecture", "Lakehouse"),
  ("SQL developers maintain a dimensional model with stored procedures that update rows", "Warehouse"),
  ("Telemetry at 50,000 events per second needs sub-second time-window queries", "Eventhouse"),
  ("A new order-entry application needs a transactional relational database", "SQL database in Fabric")],
 ["Lakehouse", "Warehouse", "Eventhouse", "SQL database in Fabric"],
 "Pick the store by data type, workload and skill set. Lakehouse is for mixed data and Spark, warehouse for T-SQL with DML, eventhouse for streaming events, and SQL database for operational OLTP workloads. Data in all four ends up in OneLake as Delta."),

single("P1",
 "A finance team maintains Excel files in a SharePoint document library. Data engineers need them to appear in a lakehouse's Files area, kept in sync and not copied. What should you create?",
 ["A SharePoint shortcut in the lakehouse's Files area", "A pipeline that copies the files every hour", "A mirrored database of the document library", "A SharePoint shortcut in the Tables folder"], "A",
 "OneDrive and SharePoint are supported shortcut targets. Excel files belong under Files, because Tables-folder shortcuts are for Delta tables. Copying isn't syncing, and mirroring is for databases."),

single("P1",
 "A software vendor's proprietary database isn't a built-in mirroring source. The vendor can write change files continuously. How can Fabric still keep a near-real-time replica of the database in OneLake?",
 ["Open mirroring, with changes written to its landing zone", "An external shortcut to the vendor's database", "A Dataflow Gen2 scheduled every minute", "A KQL database with an update policy"], "A",
 "Open mirroring lets any application write change data in the documented format to a landing zone. Fabric then applies it to Delta tables in OneLake. Shortcuts point at storage, and minute-by-minute dataflows are batch ETL."),

single("P1",
 "A pipeline loads only new and changed rows from a large source table each night. The source has a reliable LastModified column. Which pattern should you implement?",
 ["A watermark: copy rows newer than the last LastModified, then save it", "Copy the full table every night into staging", "Truncate the target and reload all rows each night", "Copy the rows whose LastModified falls in the last 24 hours"], "A",
 "The watermark pattern (Lookup old watermark, Copy with a filter, update the watermark) moves only the changes. Full reloads waste time and capacity as the table grows."),

single("P1",
 "Business-critical dataflows depend on one on-premises data gateway server. If that server goes down, refreshes fail. How do you add resilience?",
 ["Add a second gateway member to the same cluster", "Install a personal gateway as a backup", "Move the dataflows to a VNet data gateway", "Schedule every refresh twice, an hour apart"], "A",
 "A gateway cluster with several members gives high availability. Requests go to an available member if one fails. Personal gateways are single-user and don't support dataflows."),

single("P1",
 "A notebook in Workspace A must read the Delta table `orders` from a lakehouse named LH_Sales in Workspace B, without a shortcut. Which path format should you use?",
 ["abfss://WorkspaceB@onelake.dfs.fabric.microsoft.com/LH_Sales.Lakehouse/Tables/orders", "https://app.fabric.microsoft.com/groups/WorkspaceB/lakehouses/LH_Sales/Tables/orders", "powerbi://api.powerbi.com/v1.0/myorg/WorkspaceB/LH_Sales/Tables/orders", "Tables/LH_Sales/orders"], "A",
 "OneLake uses ADLS Gen2-compatible paths of the form abfss://<workspace>@onelake.dfs.fabric.microsoft.com/<item>.<type>/... A relative Tables/orders path resolves against the notebook's default lakehouse. The powerbi:// address is the XMLA endpoint."),

# ---------------- P2 (7 + 1 in case)
single("P2",
 "Which key format is common practice for a gold date dimension?",
 ["An integer yyyymmdd key, such as 20260314, plus a Date column", "A GUID per date, generated at load", "The full date as text, such as 14-Mar-2026, as the key", "An IDENTITY integer assigned in the order rows are loaded"], "A",
 "A yyyymmdd integer key is compact and readable, and keeps facts easy to partition and debug. You still keep a real Date column for time intelligence. GUIDs and random keys add cardinality without meaning."),

single("P2",
 "In a PySpark Type 2 load, you need an efficient way to detect whether any of 12 tracked attributes changed between staging and the current dimension row. What is a common technique?",
 ["Compare a hash of the 12 tracked columns, such as sha2 over concat_ws", "Compare the row counts per business key in source and target", "Compare the surrogate keys of the source and target rows", "Rewrite every current row on every load"], "A",
 "Hashing the tracked columns gives one comparable value per row. A different hash means a change and triggers the expire-and-insert step. Row counts and surrogate keys can't detect attribute changes. Rewriting everything destroys the change history."),

single("P2",
 "A staging table contains exact duplicate rows: every column is identical. You want a clean copy in the warehouse. Which statement is simplest?",
 ["CREATE TABLE stg.Orders_Clean AS SELECT DISTINCT * FROM stg.Orders;", "DELETE FROM stg.Orders WHERE OrderID IN (SELECT OrderID FROM stg.Orders);", "CREATE TABLE stg.Orders_Clean AS SELECT * FROM stg.Orders GROUP BY OrderID;", "CREATE TABLE stg.Orders_Clean AS SELECT TOP (1) * FROM stg.Orders;"], "A",
 "When rows are completely identical, SELECT DISTINCT removes the copies. ROW_NUMBER is for picking one row out of near-duplicates. The DELETE removes every row. TOP (1) keeps a single row. GROUP BY OrderID with SELECT * is invalid."),

single("P2",
 "You must reconcile customer lists from the CRM and the billing system, and show customers who appear in only one system as well as those in both. Which join should you use?",
 ["FULL OUTER JOIN on CustomerID", "INNER JOIN on CustomerID", "LEFT JOIN from CRM to billing", "CROSS JOIN"], "A",
 "A full outer join keeps matched rows and the unmatched rows from both sides, which is what a reconciliation needs. An inner join drops the mismatches. A left join drops customers who are only in billing."),

single("P2",
 "Test transactions are flagged by a CustomerName that starts with \"TEST_\". Which PySpark line removes them?",
 ["df = df.filter(~F.col(\"CustomerName\").startswith(\"TEST_\"))", "df = df.filter(F.col(\"CustomerName\") == \"TEST_\")", "df = df.dropna(subset=[\"CustomerName\"])", "df = df.withColumn(\"CustomerName\", F.lit(\"TEST_\"))"], "A",
 "startswith matches the prefix, and ~ negates it, so test rows are dropped. Equality matches only the exact string \"TEST_\". dropna removes nulls. withColumn overwrites every name."),

single("P2",
 "A notebook must produce one row per Region, with a column for each Month containing that month's total Amount. Which expression is correct?",
 ["df.groupBy(\"Region\").pivot(\"Month\").sum(\"Amount\")", "df.groupBy(\"Month\").agg(F.sum(\"Region\"))", "df.select(\"Region\", \"Month\").distinct()", "df.orderBy(\"Region\", \"Month\")"], "A",
 "groupBy plus pivot plus an aggregate turns month values into columns with totals in them. You can pass the list of months to pivot to avoid an extra pass over the data. The other options don't pivot."),

yesno("P2",
 "For each statement about denormalising dimensions in the gold layer, select Yes if it is true.",
 [("Flattening Product, Subcategory and Category into one DimProduct removes relationship hops in the semantic model.", True),
  ("Denormalising dimensions usually increases storage a little but improves usability and query simplicity.", True),
  ("Measures from the fact table should be copied into dimension tables to speed up reports.", False)],
 "Flattening snowflaked dimensions is standard. The small repetition compresses well in columnar storage, and the model gets simpler. Measures belong in facts, so copying them into dimensions breaks the grain and causes double counting."),

# ---------------- P3 (6)
single("P3",
 "A report needs revenue by month, and each order's date must be rolled up to the first day of its month. Which expression should you use?",
 ["DATEFROMPARTS(YEAR(OrderDate), MONTH(OrderDate), 1)", "DATEADD(day, 1 - MONTH(OrderDate), OrderDate)", "EOMONTH(OrderDate, -1)", "DATEFROMPARTS(YEAR(OrderDate), 1, DAY(OrderDate))"], "A",
 "DATEFROMPARTS builds the first day of the order's month, a clean key to group by. EOMONTH(..., -1) is the last day of the previous month. DATEFROMPARTS(YEAR, 1, DAY) builds a January date. The DATEADD expression subtracts the month number in days, which doesn't land on the first of the month."),

single("P3",
 "Which T-SQL splits customers into four equal-sized groups by lifetime revenue?",
 ["NTILE(4) OVER (ORDER BY LifetimeRevenue DESC)", "RANK() OVER (ORDER BY LifetimeRevenue DESC) / 4", "PERCENT_RANK() OVER (ORDER BY CustomerKey)", "COUNT(*) / 4"], "A",
 "NTILE(4) spreads the ordered rows into four groups that are as equal as possible. Dividing a rank by 4 doesn't make equal groups. Ordering PERCENT_RANK by key ignores revenue."),

single("P3",
 "In KQL, you need to add the device's model from a small `DeviceInfo` table to each `Telemetry` row, keeping telemetry rows even when no match exists. Which operator is designed for this kind of dimension lookup?",
 ["Telemetry | lookup kind=leftouter DeviceInfo on DeviceId", "Telemetry | union DeviceInfo", "Telemetry | join kind=inner DeviceInfo on DeviceId", "Telemetry | summarize by DeviceId"], "A",
 "lookup is optimised for enriching a large fact table from a small dimension table, and kind=leftouter keeps unmatched rows. An inner join drops them. union stacks tables."),

single("P3",
 "A KQL table has a Payload column holding JSON text such as {\"temperature\": 21.5}. Which expression extracts the temperature as a number?",
 ["| extend Temp = toreal(parse_json(Payload).temperature)", "| extend Temp = Payload.temperature", "| extend Temp = toint(Payload)", "| where Payload has \"temperature\" | project Temp = Payload"], "A",
 "parse_json turns the text into a dynamic value, the property is read with dot notation, and toreal converts it to a number. A plain string column can't be navigated with dot notation, and toint can't convert JSON text. The has filter only finds rows containing the word."),

single("P3",
 "In the DAX query view, you want a single-row result showing total sales and total cost. Which query is valid?",
 ["EVALUATE ROW(\"Sales\", [Total Sales], \"Cost\", [Total Cost])", "EVALUATE [Total Sales], [Total Cost] ORDER BY 1", "SELECT [Total Sales] AS Sales, [Total Cost] AS Cost", "EVALUATE {([Total Sales], [Total Cost])} + {}"], "A",
 "ROW builds a one-row table from name and expression pairs, and EVALUATE needs a table. EVALUATE can't take a comma-separated list of scalars, the table-constructor expression isn't valid, and SELECT isn't DAX."),

single("P3",
 "Analysts need a quick distinct count of visitors across 20 billion rows in a warehouse. A small error margin is acceptable, but speed matters. Which function should they use?",
 ["APPROX_COUNT_DISTINCT(VisitorID)", "COUNT(VisitorID)", "COUNT(DISTINCT VisitorID) OVER ()", "SUM(VisitorID)"], "A",
 "APPROX_COUNT_DISTINCT uses a probabilistic algorithm that's much faster and uses far less memory at large scale, with a small error. COUNT counts rows, not distinct values. SUM adds up the IDs, which means nothing."),

# ---------------- S1 (5 + 1 in case)
single("S1",
 "Source data is in an on-premises SQL Server with no plan to move it into OneLake. The model needs heavy Power Query shaping and the full range of DAX features, and a daily refresh is acceptable. Which storage mode fits best?",
 ["Import, refreshed through the on-premises gateway", "Direct Lake through the on-premises gateway", "DirectQuery through the on-premises gateway", "Dual storage mode for every table"], "A",
 "Direct Lake needs the data in OneLake as Delta and can't use a gateway. DirectQuery restricts Power Query and some DAX, and it puts load on the source. Dual only matters in composite models. Import with a daily refresh through the gateway fits the requirement."),

single("S1",
 "Which measure counts the customers whose [Sales] is over 1,000 in the current filter context?",
 ["COUNTROWS(FILTER(VALUES(Customer[CustomerKey]), [Sales] > 1000))", "COUNTROWS(FILTER(Sales, Sales[Amount] > 1000))", "CALCULATE(COUNT(Customer[CustomerKey]), Sales[Amount] > 1000)", "DISTINCTCOUNT(Customer[CustomerKey]) > 1000"], "A",
 "FILTER over the distinct customers evaluates [Sales] per customer, using context transition, and keeps those over 1,000. Filtering the Sales table checks individual transactions, not customer totals. Comparing DISTINCTCOUNT with 1,000 returns TRUE or FALSE, not a count."),

single("S1",
 "Which argument restarts the ranking for each category in the measure below?",
 ["PARTITIONBY('Product'[Category])", "ORDERBY([Revenue], DESC)", "DENSE", "ALLSELECTED"], "A",
 "PARTITIONBY splits the relation into groups, here categories, and the ranking restarts in each one. ORDERBY decides the ranking order. DENSE controls how ties are handled. ALLSELECTED defines which rows are considered.",
 code="""Rank in Category =
RANK ( DENSE,
       ALLSELECTED ( 'Product'[Category], 'Product'[Name] ),
       ORDERBY ( [Revenue], DESC ),
       DEFAULT,
       ______ )"""),

single("S1",
 "After you add a calculation group to a model, report authors can no longer drag a numeric column into a visual and have it summed automatically. Why?",
 ["Adding a calculation group turns on Discourage implicit measures", "Calculation groups hide numeric columns from the field list", "The model has switched to DirectQuery for those columns", "Object-level security was applied to numeric columns"], "A",
 "Calculation groups only apply to explicit measures, so the model sets Discourage implicit measures. Authors have to create proper measures, which is good practice anyway. The columns aren't deleted, hidden or secured, and the storage mode doesn't change."),

single("S1",
 "EmployeeDetails has exactly one row per employee and shares EmployeeKey with DimEmployee, and the two are always used together. What is the recommended model design?",
 ["Merge them into a single DimEmployee table, in the gold layer or in Power Query", "Keep a one-to-one bidirectional relationship", "Create a many-to-many relationship", "Hide EmployeeDetails and use LOOKUPVALUE in every measure"], "A",
 "Two tables in a one-to-one relationship describe the same entity, so merging them makes the model simpler and faster. One-to-one relationships filter in both directions and add complexity for no benefit."),

# ---------------- S2 (6)
single("S2",
 "In the DAX query view, you tested an improved version of a measure with DEFINE MEASURE and it's faster. How do you apply it to the model without retyping it?",
 ["Select Update model with changes above the DEFINE block", "Run the query again with EVALUATE SAVE", "Republish the .pbix, which saves query view changes", "Export the query as a .dax file and import it"], "A",
 "The DAX query view can write DEFINE MEASURE changes back to the model with Update model, so you can go straight from testing to applying. The other options don't update the measure."),

multi("S2",
 "Which two actions reduce the memory footprint of an Import model?",
 ["Remove columns that no report or measure uses", "Reduce the precision or cardinality of columns, for example by rounding timestamps to the minute or splitting datetime into date and time", "Add a calculated column for every measure", "Turn on Auto date/time", "Convert integer keys to text"], "AB",
 "VertiPaq size depends on column count and cardinality, so removing unused columns and cutting cardinality give the biggest wins. Calculated columns, auto date tables and text keys all make the model bigger."),

single("S2",
 "One Direct Lake semantic model must combine Delta tables from a lakehouse and from a warehouse in different workspaces. Which Direct Lake variant supports this?",
 ["Direct Lake on OneLake", "Direct Lake on the SQL analytics endpoint", "Neither variant; Direct Lake allows one source only", "Both variants equally"], "A",
 "Direct Lake on OneLake can read Delta tables from several Fabric items. Direct Lake on the SQL analytics endpoint is tied to one lakehouse or warehouse endpoint.", fixed=True),

yesno("S2",
 "For each statement about refreshing Direct Lake semantic models, select Yes if it is true.",
 [("A Direct Lake table needs an incremental refresh policy to avoid reloading all its data.", False),
  ("With automatic updates turned on, the model can reframe when the underlying Delta tables change.", True),
  ("Framing (refresh) normally completes in seconds, because it processes metadata only.", True)],
 "Framing replaces data refresh in Direct Lake, so incremental refresh policies are for Import tables. Automatic updates keep the model in step with the Delta tables. You can turn them off and trigger framing from your ETL instead."),

single("S2",
 "A bronze landing table is written every few seconds by streaming jobs and is never read by Direct Lake or reports. What should you do about V-Order on this table?",
 ["Leave V-Order off, since it adds write cost with no read benefit", "Turn on V-Order and run OPTIMIZE every minute", "Turn on V-Order only for the most recent partition", "Turn on V-Order, and Z-Order by every filter column"], "A",
 "V-Order trades write performance for read performance. That's right for read-heavy gold tables and wrong for write-heavy staging tables that aren't read analytically. Adding Z-Order or minute-by-minute OPTIMIZE adds even more write cost for no benefit."),

single("S2",
 "A report page has eight slicers, and every change makes all the visuals requery straight away, so pages feel sluggish. Which setting cuts the number of queries?",
 ["Query reduction, such as an Apply button on slicers", "Turning off cross-highlighting on visuals", "Large semantic model storage format", "Syncing the slicers across pages"], "A",
 "Query reduction lets users make several slicer and filter changes, then apply them once, so far fewer queries are sent. Turning off cross-highlighting changes interactions between visuals, not slicer behaviour. Syncing slicers adds work. Storage format doesn't change how many queries interaction causes."),

# ---------------- Case study (M1, P1, P2, S1)
case("Wide World Importers",
 "Wide World Importers sells novelty goods through 40 promotions a year, and a product can be in several promotions at once. Customer data, including phone numbers, is stored in a lakehouse, LH_Core. Support agents query LH_Core with both T-SQL and Spark notebooks.\n\nA supplier publishes its product catalogue as Parquet files in a Google Cloud Storage bucket. A Direct Lake on OneLake semantic model is planned for sales analysis.",
 ["R1. Support agents must not see the PhoneNumber column, whether they use T-SQL or Spark. Everything else in Customers must stay readable.",
  "R2. The supplier catalogue must be available in LH_Core without being copied.",
  "R3. The gold layer must correctly represent products that belong to several promotions.",
  "R4. Sales must be analysable by promotion without double counting at the total."],
 [
  single("M1", "What should you configure for R1? The support agents are workspace Viewers.",
   ["A OneLake security role that excludes the PhoneNumber column", "Dynamic data masking on PhoneNumber via SQL", "Object-level security on PhoneNumber in the model", "A Highly Confidential label on LH_Core"], "A",
   "OneLake security roles can hide columns and are enforced across engines, so both T-SQL and Spark are covered. Masking is a SQL feature and doesn't cover Spark file access. OLS only applies inside a semantic model. Labels don't restrict access."),
  single("P1", "Which approach to the supplier catalogue satisfies R2?",
   ["An external shortcut to the GCS bucket", "A pipeline that copies the files daily", "Mirroring the GCS bucket into OneLake", "A Dataflow Gen2 that loads into LH_Core"], "A",
   "Google Cloud Storage is a supported external shortcut target, so the data is read in place. Copying breaks the no-copy rule. Mirroring is for databases."),
  single("P2", "Which gold-layer structure satisfies R3?",
   ["A ProductPromotion bridge table, one row per product per promotion", "A comma-separated PromotionList column on DimProduct", "One DimProduct row per promotion, repeating the product", "A PromotionKey on each fact row, with no other link"], "A",
   "A bridge table is the standard way to model a multi-valued attribute. A delimited list can't be filtered or related. Repeating product rows breaks the one-row-per-product rule on DimProduct and the uniqueness Direct Lake needs on the one side of a relationship."),
  single("S1", "Which modelling behaviour satisfies R4?",
   ["Filter through the bridge, so each promotion is right and the total counts each sale once", "Make the grand total the sum of the per-promotion rows", "Remove the bridge and make every relationship filter both ways", "Duplicate each fact row once for every promotion"], "A",
   "With a many-to-many path through a bridge, the engine calculates each promotion's sales correctly. A sale in two promotions shows under both, but the grand total counts it once. That non-additive behaviour is correct. Duplicating fact rows, or adding up the promotion rows, double counts."),
 ]),
]
