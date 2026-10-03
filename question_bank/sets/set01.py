from model import single, multi, yesno, match, order, case

TITLE = "Foundations — the shape of Fabric"
SUBTITLE = "Core vocabulary across the whole outline: items, roles, routes in, the gold layer, and the three query languages."
LEVEL = "Level 1 · Foundation"
CASE_NAME = "Contoso Retail"

ITEMS = [
# ---------------- M1 Security and governance (5 + 1 in case)
single("M1",
 "A group of store managers must open reports and read data in a workspace. They must not be able to create, edit or delete any item. Which workspace role should you assign, following least privilege?",
 ["Admin", "Member", "Viewer", "Contributor"], "C",
 "Viewer is the only workspace role that can't create or change items. Contributor, Member and Admin can all create and edit content. Member and Admin can also manage access, which goes further still."),

single("M1",
 "You share a lakehouse with an analyst from another team. The analyst must query its tables with T-SQL through the SQL analytics endpoint, but must not read the underlying files with Spark. Which permissions do you grant?",
 ["Read only", "Read and ReadData (Read all SQL endpoint data)", "Read and ReadAll (Read all Apache Spark / OneLake data)", "Write"], "B",
 "ReadData lets a user query the item through the SQL analytics endpoint. ReadAll gives OneLake access to the files, so Spark and other engines can read them, which the stem rules out. Read alone shows the item's metadata but lets the user query nothing. Write grants everything."),

yesno("M1",
 "For each statement about Microsoft Purview sensitivity labels in Fabric, select Yes if it is true.",
 [("A sensitivity label applied to a semantic model stays on data exported from it to Excel.", True),
  ("Applying the Highly Confidential label stops workspace Viewers from opening the item.", False),
  ("Labels can be applied to lakehouses and warehouses as well as to Power BI reports.", True)],
 "Labels classify content and protect exported files. They carry through to Excel, PowerPoint and PDF exports. They don't grant or remove access inside Fabric: that's done by workspace roles, item permissions and OneLake security. Labels apply across Fabric items, including lakehouses, warehouses, semantic models, reports and dataflows."),

single("M1",
 "A data engineer wants to signal that a lakehouse is ready for others to reuse. No special approval process exists. Which action is available to anyone with write permission on the item?",
 ["Certify the lakehouse", "Promote the lakehouse", "Mark the lakehouse as Master data", "Apply a domain to the lakehouse"], "B",
 "Promoted is the endorsement level any user with write permission can apply. Certified and Master data are limited to users the Fabric administrator authorises. Domains are assigned to workspaces, not items, and are not an endorsement."),

single("M1",
 "A semantic model has a Sales table with a column `Sales[RepEmail]`. Each sales rep must see only their own rows when viewing the report. Which DAX filter expression do you put on the Sales table in the role?",
 ["Sales[RepEmail] = USERNAME()", "Sales[RepEmail] = USERPRINCIPALNAME()", "Sales[RepEmail] = SELECTEDVALUE(Sales[RepEmail])", "Sales[RepEmail] = CUSTOMDATA()"], "B",
 "USERPRINCIPALNAME() returns the signed-in user's UPN (normally their email) in the Power BI service, so the filter matches each rep's own rows. USERNAME() can return DOMAIN\\user in Desktop, which is why UPN is preferred. SELECTEDVALUE reads the filter context, not the user's identity. CUSTOMDATA comes from the connection string, which is an embedding scenario."),

# ---------------- M2 Lifecycle (6)
multi("M2",
 "Which two source-control providers can a Fabric workspace connect to through Fabric Git integration?",
 ["Azure DevOps (Azure Repos)", "A SharePoint document library", "GitHub", "An Azure Blob Storage container", "OneDrive for Business"], "AC",
 "Fabric Git integration connects a workspace to a branch in an Azure DevOps or GitHub repository. SharePoint, OneDrive and Blob Storage store files, but they aren't Git providers and give you no commit history or pull requests."),

single("M2",
 "You create a new deployment pipeline and accept the defaults. How many stages does it have?",
 ["Two: Development and Production", "Three: Development, Test and Production", "Four: Development, Test, UAT and Production", "Five: Development, Test, UAT, Pre-production and Production"], "B",
 "The default is three stages, named Development, Test and Production. You can customise a pipeline to have anywhere from 2 to 10 stages and rename them."),

single("M2",
 "Which statement correctly describes a Power BI template file (.pbit)?",
 ["It contains the report, the model definition and a full copy of the data.", "It contains the report pages, the model definition and queries, but no data.", "It contains only a data-source connection, so Power BI Desktop opens pre-connected.", "It contains only the report theme colours."], "B",
 "A .pbit holds everything except the data: report layout, model, measures and queries, plus any parameters to fill in when it's opened. A file that holds only a connection is a .pbids. A file that also holds the data is a .pbix."),

order("M2",
 "You need to deploy a metadata-only change to a semantic model in a Fabric workspace using Tabular Editor. Put the required actions in order.",
 ["Make sure the capacity's XMLA endpoint setting is Read Write",
  "Copy the workspace connection address (powerbi://api.powerbi.com/v1.0/myorg/<workspace>)",
  "Connect Tabular Editor to the workspace address and open the model",
  "Make the change and save it to the connected model"],
 "XMLA write needs the Read Write setting on the capacity. Then you connect an external tool using the workspace connection address and save the change straight to the model. Republishing the .pbix isn't needed, and it would overwrite the reports too.",
 extra=["Republish the .pbix file from Power BI Desktop", "Create a deployment pipeline"]),

single("M2",
 "You plan to rename a column in a warehouse table. Before you make the change, you must find out which semantic models and reports depend on the warehouse. What should you use?",
 ["Impact analysis on the warehouse, from lineage view or the item's details", "The Fabric Capacity Metrics app", "The deployment pipeline compare view", "The warehouse's query activity (query insights) views"], "A",
 "Impact analysis lists the downstream items and reports that depend on an item, and lets you notify their contacts. That's the standard answer for “before a breaking change”. Capacity Metrics shows compute use. Pipeline compare shows differences between stages. Query insights shows which queries ran."),

single("M2",
 "Fifteen report authors keep importing the same warehouse tables into their own models, and their revenue figures don't agree. What should you do?",
 ["Publish one endorsed shared semantic model and give the authors Build permission on it.", "Give every author the workspace Admin role, so they can review and fix each other's models.", "Send every author a .pbids file for the warehouse, so they all connect to the same tables.", "Turn on Git integration for the authors' workspace, so model changes are reviewed."], "A",
 "A shared semantic model gives everyone one governed set of measures and relationships. Build permission lets authors create their own reports on top of it, and endorsement helps them find it and trust it. A .pbids file only shares a connection, so each author would still build their own model."),

# ---------------- P1 Get data (6 + 1 in case)
single("P1",
 "A data engineering team writes PySpark. They will land CSV files, nested JSON and product images before they clean anything. Which Fabric item should they use for the raw (bronze) layer?",
 ["Warehouse", "Lakehouse", "Eventhouse", "Fabric SQL database"], "B",
 "A lakehouse has a Files area for unstructured and semi-structured data as well as Delta tables, and Spark is its main interface. A warehouse holds structured tables only. An eventhouse is built for event and time-series data. A SQL database is an operational (OLTP) store."),

single("P1",
 "Your organisation has five years of Parquet files in an Azure Data Lake Storage Gen2 account. Analysts must query them from a Fabric lakehouse, and the files must not be copied. What should you create?",
 ["A pipeline with a Copy activity that loads the files", "A Dataflow Gen2 that reads the files into a table", "An external shortcut to the ADLS Gen2 location", "A mirrored database over the storage account"], "C",
 "A shortcut is a pointer, so the data stays where it is and nothing is copied. ADLS Gen2 is a supported external shortcut target. A pipeline and a dataflow both copy the data. Mirroring replicates operational databases, not files in storage."),

single("P1",
 "An Azure Cosmos DB account powers an e-commerce application. Analysts need data that's at most a few minutes old in OneLake. No ETL may be built, and no analytical load may be put on the source. What should you implement?",
 ["Mirroring of the Cosmos DB account into Fabric", "A scheduled pipeline every five minutes", "A DirectQuery semantic model over Cosmos DB", "A Dataflow Gen2 with scheduled refresh"], "A",
 "Mirroring keeps a near-real-time replica of supported operational databases, Cosmos DB among them, in OneLake as Delta. There's no pipeline to build or maintain. A five-minute pipeline is ETL. DirectQuery puts query load straight onto the application's database."),

single("P1",
 "Business analysts know Power Query well. They must build and maintain a transformation themselves, and its output must be written to a lakehouse table. Which item should they use?",
 ["A notebook that writes to the lakehouse with PySpark", "A Dataflow Gen2 with a lakehouse destination", "A Spark job definition with a lakehouse reference", "A KQL queryset with an update policy"], "B",
 "Dataflow Gen2 is low-code Power Query with explicit destinations, including lakehouses, warehouses and KQL databases, so analysts can own it. Notebooks and Spark job definitions need code. A KQL queryset only queries data. It doesn't load it."),

match("P1",
 "Match each discovery need to the Fabric surface that meets it.",
 [("Find a certified warehouse that another team owns and request access to it", "OneLake catalog"),
  ("Browse event streams and Azure Event Hubs sources available to the organisation", "Real-Time hub"),
  ("See which reports are built on a specific lakehouse", "Lineage view")],
 ["OneLake catalog", "Real-Time hub", "Lineage view", "Capacity Metrics app"],
 "The OneLake catalog is where you discover and govern stored data items across the tenant. The Real-Time hub is where you discover streaming data and events. Lineage view shows upstream and downstream dependencies. The Capacity Metrics app reports on compute, not data."),

single("P1",
 "A pipeline must copy tables from a SQL Server instance on the company's internal network into a lakehouse. What must be in place for the Copy activity to reach the source?",
 ["An on-premises data gateway, and a connection that uses it", "A OneLake shortcut", "A personal-mode gateway on a developer's laptop", "Nothing; Fabric reaches internal networks directly"], "A",
 "Sources on a private network are reached through the on-premises data gateway, using a connection set up on that gateway. A personal-mode gateway supports only Power BI semantic model refresh for one user, so it isn't for production pipelines. A shortcut doesn't target a SQL Server database."),

# ---------------- P2 Transform (7 + 1 in case)
single("P2",
 "In a Fabric Warehouse, logic must insert the day's new rows into `gold.FactSales` and then update a load-audit table, as one unit a pipeline can call. Which object should you create?",
 ["A view", "An inline table-valued function", "A stored procedure", "A SQL analytics endpoint query"], "C",
 "A stored procedure can run DML (INSERT, UPDATE, DELETE) across several tables, and a pipeline can call it with the Stored procedure activity. Views and table-valued functions return data but can't change it. A lakehouse SQL analytics endpoint is read-only."),

single("P2",
 "A silver DataFrame `df` has nulls in `Region` and `Discount`. Nulls in Region must become \"Unknown\" and nulls in Discount must become 0, and no rows may be lost. Which PySpark line is correct?",
 ["df = df.dropna()", "df = df.fillna({\"Region\": \"Unknown\", \"Discount\": 0})", "df = df.na.drop(subset=[\"Region\", \"Discount\"])", "df = df.filter(\"Region IS NOT NULL\")"], "B",
 "fillna with a dictionary replaces nulls column by column and keeps every row. The other three options remove the rows that have nulls, which the requirement forbids."),

single("P2",
 "A staging table stores order dates as text in the format `2026-08-14`. The gold warehouse table needs a real date column. Which expression should the load use?",
 ["CAST(OrderDateText AS date)", "CAST(OrderDateText AS varchar(10))", "FORMAT(OrderDateText, 'yyyy-MM-dd')", "Keep it as text and convert it in a DAX measure"], "A",
 "Convert the type in the gold transformation so it's stored once in the correct type for every consumer. CAST to date handles ISO-format text. Casting to varchar leaves it as text. FORMAT returns text. Leaving the conversion to DAX pushes it downstream, where every query pays for it."),

single("P2",
 "The source has three tables: Product, Subcategory and Category, joined in a chain. You are building the gold star schema. What should you do?",
 ["Load the three tables separately and relate them in the semantic model.", "Denormalise the three into a single DimProduct table with Subcategory and Category columns.", "Put the category name on the fact table.", "Create a bridge table between Product and Category."], "B",
 "Flattening a snowflaked dimension into one table is standard star-schema practice. It removes relationship hops in the semantic model and makes the model simpler to use. Putting attributes on the fact breaks its grain. A bridge table is for many-to-many relationships, which this isn't."),

single("P2",
 "You need a physical summary table in a Fabric Warehouse with one row per product category per month, created and populated in one statement. Complete the statement.",
 ["SELECT INTO with ORDER BY", "CREATE TABLE ... AS SELECT ... GROUP BY", "CREATE VIEW ... AS SELECT ... GROUP BY", "INSERT ... VALUES"], "B",
 "CREATE TABLE AS SELECT (CTAS) creates and fills a table in one statement, and the GROUP BY produces one row per category per month. A view isn't a physical table. INSERT ... VALUES inserts literal rows, so it can't aggregate.",
 code="""____ gold.CategoryMonthSales
AS
SELECT p.Category, d.MonthStart, SUM(f.Amount) AS Amount
FROM   gold.FactSales f
JOIN   gold.DimProduct p ON p.ProductKey = f.ProductKey
JOIN   gold.DimDate d    ON d.DateKey    = f.DateKey
____ p.Category, d.MonthStart;"""),

single("P2",
 "Every product must appear in the result, including products that have never been sold, with their sales total where one exists. Which join should you use from DimProduct to FactSales?",
 ["INNER JOIN", "LEFT OUTER JOIN from DimProduct to FactSales", "RIGHT OUTER JOIN from DimProduct to FactSales", "CROSS JOIN"], "B",
 "A LEFT OUTER JOIN keeps every row from the left table (DimProduct), with NULL sales for products that have no matching fact rows. An INNER JOIN drops the unsold products. A CROSS JOIN pairs every product with every fact row."),

single("P2",
 "In a Dataflow Gen2, a customer query has repeated rows for the same CustomerID. Each CustomerID must appear once. What should you do in the Power Query editor?",
 ["Select CustomerID and choose Remove duplicates", "Select all columns and choose Remove blank rows", "Group by every column and count the rows", "Select CustomerID and choose Keep duplicates"], "A",
 "Remove duplicates on the key column keeps the first row for each CustomerID. Remove blank rows deals with empty rows, not repeated ones. Grouping by every column would only merge rows that are identical in every column."),

# ---------------- P3 Query (6)
single("P3",
 "A business analyst who doesn't write SQL must join two warehouse tables, filter them, group the result, and save it as a view. What should they use?",
 ["The warehouse's Visual Query Editor", "A KQL queryset connected to the warehouse", "A notebook attached to the warehouse", "The DAX query view in Power BI Desktop"], "A",
 "The Visual Query Editor is a no-code, Power Query-style canvas in the warehouse or SQL analytics endpoint. It generates SQL and can save the result as a view. Notebooks and querysets need code. The DAX query view works against semantic models, not the warehouse."),

single("P3",
 "Which KQL query returns the number of events per hour for the last day?",
 ["Events | where Timestamp > ago(1d) | summarize count() by bin(Timestamp, 1h)",
  "Events | where Timestamp > ago(1d) | project count() by Timestamp",
  "SELECT COUNT(*) FROM Events GROUP BY HOUR(Timestamp)",
  "Events | take 24 | extend Hour = hourofday(Timestamp)"], "A",
 "where filters the rows, summarize ... by groups and aggregates, and bin() puts timestamps into fixed buckets. project selects columns but can't aggregate. The SELECT option is SQL, not KQL. take 24 just returns 24 arbitrary rows."),

single("P3",
 "Which T-SQL query returns the ten products with the highest total revenue?",
 ["SELECT TOP (10) ProductKey, SUM(Revenue) AS Rev FROM gold.FactSales GROUP BY ProductKey ORDER BY Rev DESC;",
  "SELECT ProductKey, SUM(Revenue) FROM gold.FactSales GROUP BY ProductKey LIMIT 10;",
  "SELECT TOP (10) ProductKey, Revenue FROM gold.FactSales ORDER BY Revenue DESC;",
  "SELECT ProductKey, MAX(Revenue) FROM gold.FactSales GROUP BY ProductKey;"], "A",
 "The correct query aggregates per product, sorts by the total, and keeps ten. LIMIT isn't T-SQL. TOP (10) without GROUP BY returns the ten largest individual rows, which could include the same product twice, rather than the top products by total. MAX returns the largest single row per product, with no top-10 limit."),

single("P3",
 "In the DAX query view, you want the five product categories with the highest [Total Sales]. Which query is valid?",
 ["EVALUATE TOPN(5, SUMMARIZECOLUMNS('Product'[Category], \"Sales\", [Total Sales]), [Sales], DESC)",
  "SELECT TOP 5 Category, [Total Sales] FROM 'Product' ORDER BY [Total Sales] DESC",
  "TOPN(5, SUMMARIZECOLUMNS('Product'[Category], \"Sales\", [Total Sales]), [Sales], DESC)",
  "EVALUATE CALCULATE([Total Sales], TOPN(5, VALUES('Product'[Category]), [Total Sales]))"], "A",
 "A DAX query starts with EVALUATE and must return a table. Here TOPN wraps a SUMMARIZECOLUMNS grouping. The SELECT option is SQL. The TOPN without EVALUATE is an expression, not a query. EVALUATE CALCULATE(...) returns a scalar, which EVALUATE can't output."),

single("P3",
 "In KQL, you need to keep every existing column and add a new column `TempF` computed from `TempC`. Which operator should you use?",
 ["project", "extend", "summarize", "distinct"], "B",
 "extend adds computed columns and keeps all the existing ones. project returns only the columns you list. summarize aggregates the rows. distinct removes duplicate rows."),

single("P3",
 "Which surface is designed for writing and saving KQL queries against an Eventhouse?",
 ["A KQL queryset", "The Visual Query Editor", "A Dataflow Gen2", "The SQL analytics endpoint of a lakehouse"], "A",
 "A KQL queryset is the Fabric item for writing, running and saving KQL queries against KQL databases. The Visual Query Editor and the SQL analytics endpoint generate or use T-SQL. A Dataflow Gen2 loads and transforms data."),

# ---------------- S1 Design (6)
single("S1",
 "Your gold tables are Delta tables in a Fabric lakehouse. Reports need Import-class query speed, and you don't want to schedule data refreshes that copy the data. Which storage mode should you choose?",
 ["Import", "DirectQuery", "Direct Lake", "Dual"], "C",
 "Direct Lake reads Delta-Parquet column data from OneLake straight into the VertiPaq engine when a query needs it. Its refresh (framing) only updates metadata, so no data is copied. Import copies the data on each refresh. DirectQuery sends every query to the source. Dual only means something inside a composite model."),

single("S1",
 "FactSales has OrderDateKey and ShipDateKey, and both relate to DimDate. Only the OrderDate relationship is active. A measure must total sales by ship date. Which DAX function activates the ship-date relationship inside the measure?",
 ["CROSSFILTER", "USERELATIONSHIP", "TREATAS", "RELATED"], "B",
 "USERELATIONSHIP, used as a CALCULATE modifier, turns on an inactive relationship for that calculation only. That's the standard pattern for a role-playing date dimension. CROSSFILTER changes the filter direction. TREATAS applies a filter through a virtual relationship. RELATED fetches a column from the one side of a relationship."),

single("S1",
 "Accounts can have several customers, and customers can hold several accounts. You need to analyse balances (on the Account side) by customer attributes. What is the recommended model design?",
 ["Merge DimCustomer and DimAccount into one table with a row per customer-account pair", "A CustomerAccount bridge table, with the bridge-to-DimAccount relationship filtering both ways", "A direct many-to-many relationship between FactBalance and DimCustomer on CustomerName", "Duplicate each balance row once per account holder, so every customer gets the full balance"], "B",
 "A many-to-many relationship between dimensions is modelled with a bridge (factless) table. The filter from DimCustomer has to flow through the bridge to DimAccount and on to the fact, which is why one relationship is set to filter in both directions. Duplicating fact rows inflates totals. Merging the tables destroys the grain."),

match("S1",
 "Match each requirement to the modelling feature that meets it.",
 [("Thirty measures each need PY and YoY variants without writing 60 new measures", "Calculation group"),
  ("Users choose, from a slicer, whether a chart shows Revenue, Margin or Units", "Field parameter"),
  ("A YoY % calculation item must show as a percentage, while the others show as currency", "Dynamic format string"),
  ("An analyst wants to test the effect of a 0–20% price increase with a slider", "What-if parameter")],
 ["Calculation group", "Field parameter", "Dynamic format string", "What-if parameter"],
 "Calculation groups apply reusable logic (via SELECTEDMEASURE) to any measure. Field parameters let users swap which field a visual uses. Dynamic format strings change formatting based on a DAX expression. A what-if parameter creates a disconnected table of values for scenario analysis."),

single("S1",
 "Sales has columns Qty and UnitPrice, and no Amount column. Which measure correctly returns total revenue?",
 ["Revenue = SUM(Sales[Qty]) * SUM(Sales[UnitPrice])", "Revenue = SUMX(Sales, Sales[Qty] * Sales[UnitPrice])", "Revenue = AVERAGEX(Sales, Sales[Qty] * Sales[UnitPrice])", "Revenue = SUM(Sales[Qty] * Sales[UnitPrice])"], "B",
 "SUMX is an iterator: it works out Qty × UnitPrice for each row and then adds up the results. Multiplying two totals gives a wrong answer whenever there's more than one row. SUM only takes a single column reference, so SUM(Qty * UnitPrice) is invalid. AVERAGEX averages instead of summing."),

single("S1",
 "A visual shows Sales by City inside a Region hierarchy. A measure must return the text \"City\" on city rows and \"Region\" on region subtotal rows. Which function tells you which level is being evaluated?",
 ["ISINSCOPE", "ISBLANK", "ISERROR", "CONTAINSSTRING"], "A",
 "ISINSCOPE('Geo'[City]) is TRUE when the current row is grouped by City, so it tells hierarchy levels and subtotals apart. That's one of the information functions the skills outline names. The other options test values, not grouping levels."),

# ---------------- S2 Optimize (5 + 1 in case)
single("S2",
 "A report page is slow. You need to find which visual takes the longest and copy the DAX query it sends, without leaving Power BI Desktop. What should you use?",
 ["Performance Analyzer", "Lineage view", "The Capacity Metrics app", "Impact analysis"], "A",
 "Performance Analyzer records each visual's duration, split into DAX query, visual display and other. Copy query then gives you the DAX to tune in the DAX query view. The other tools work at the item or capacity level, not the visual level."),

single("S2",
 "What does a refresh of a Direct Lake semantic model do?",
 ["It copies all rows from the Delta tables into model memory, replacing the old copy.", "It frames the model: it points the model at the latest Delta table versions without copying data.", "It re-runs the Power Query transformations defined for each table.", "It rebuilds every calculated column and table from the source data."], "B",
 "Direct Lake refresh is called framing, and it only touches metadata. Data is loaded into memory later, when queries need it, through a step called transcoding. That's why a Direct Lake refresh takes seconds and uses very little capacity."),

multi("S2",
 "You configure incremental refresh on an Import fact table. Which two items are required?",
 ["Date/time parameters named exactly RangeStart and RangeEnd", "A filter on the fact query that uses RangeStart and RangeEnd", "A Direct Lake storage mode on the table", "A calculated column that flags the current year", "A deployment pipeline"], "AB",
 "Incremental refresh needs the two reserved parameters and a filter that uses them, and the filter should fold back to the source. Direct Lake tables don't use incremental refresh. A calculated column would break folding."),

single("S2",
 "An Import model will grow to about 25 GB after refresh in the service. What must be enabled for the model to grow past the default limit?",
 ["Large semantic model storage format", "Automatic page refresh on the report", "Query caching on the capacity", "Direct Lake fallback to DirectQuery"], "A",
 "Without large semantic model storage format, a model in the service is capped at a small size limit. With it turned on, the model can grow up to the capacity's limit. The Desktop upload limit (10 GB) still applies to the .pbix you publish, and the model then grows through refresh. The other settings don't affect size."),

single("S2",
 "A Spark job appends small files to a gold Delta table every 15 minutes. After a month, Direct Lake queries are slower even though the row count has barely grown. What should you do first?",
 ["Run OPTIMIZE on the table to compact the small files", "Switch the model to Import mode", "Add variables to every DAX measure", "Run VACUUM with a retention of 0 hours"], "A",
 "Lots of small files mean more column segments for Direct Lake to transcode. Compacting them with OPTIMIZE (then relying on auto compaction) fixes the problem at the table. VACUUM removes unreferenced files but doesn't improve how active files are laid out. A zero-hour retention also breaks time travel and can affect readers part-way through a query."),

# ---------------- Case study (M1, P1, P2, S2)
case("Contoso Retail",
 "Contoso Retail runs 180 stores. Sales data lands every night from an on-premises SQL Server into a Fabric lakehouse named LH_Sales, built by a PySpark team. A gold semantic model in Direct Lake mode serves 300 report users. A supplier shares weekly price files in an Amazon S3 bucket.\n\nToday, all 300 report users are workspace Contributors. The store-performance team has noticed that the nightly load sometimes inserts the same order twice.",
 ["R1. Report users must not be able to change any item in the workspace.",
  "R2. Supplier price files must be queryable in Fabric without being copied.",
  "R3. Duplicate orders must be removed before they reach the gold table.",
  "R4. Direct Lake queries must stay fast as the nightly appends build up."],
 [
  single("M1", "Which change satisfies R1 with the least administrative effort?",
   ["Keep the users as Contributors and apply a Highly Confidential label", "Change the users' workspace role to Viewer, or give them access through an app", "Make the users workspace Members and turn on item sharing", "Create one workspace per store and make each manager Admin"], "B",
   "Contributors can create and edit items. Viewer, or consuming content through an app, gives read-only access. A label grants and removes nothing. Member gives even more rights. One workspace per store means a lot more to administer."),
  single("P1", "Which approach satisfies R2?",
   ["A pipeline that copies the S3 files into LH_Sales every week", "An external shortcut in LH_Sales that points to the S3 bucket", "Mirroring the S3 bucket", "A Dataflow Gen2 that loads the files into a warehouse"], "B",
   "Amazon S3 is a supported external shortcut target. A shortcut gives access in place, with no copy. Copy activities and dataflows copy the data. Mirroring is for operational databases, not object storage."),
  single("P2", "The PySpark team must satisfy R3 while building the silver order table. Which line removes rows that repeat the same OrderID?",
   ["df.dropDuplicates([\"OrderID\"])", "df.distinct().count()", "df.dropna(subset=[\"OrderID\"])", "df.orderBy(\"OrderID\")"], "A",
   "dropDuplicates with a subset removes rows that repeat the key, even when other columns differ. distinct() only removes rows that are identical in every column, and adding count() returns a number instead of a DataFrame. dropna removes rows with nulls. orderBy only sorts."),
  single("S2", "Which practice best satisfies R4?",
   ["Turn on auto compaction, and run OPTIMIZE on tables that are already fragmented", "Schedule the semantic model to refresh every 15 minutes during the day", "Convert the gold tables to CSV so they're simpler to scan", "Turn off V-Order on the gold tables so the nightly writes are faster"], "A",
   "Direct Lake performance depends on how the Delta files are laid out. Auto compaction keeps file counts healthy after each write, and OPTIMIZE fixes existing fragmentation. Refreshing more often only re-frames metadata. CSV can't be read by Direct Lake. V-Order speeds up reads, so turning it off makes reports slower."),
 ]),
]
