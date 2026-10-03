from model import single, multi, yesno, match, order, case

TITLE = "Advanced — performance and the hard edges"
SUBTITLE = "Guardrails, fallback, file layout, DAX tuning and the security details that catch strong candidates."
LEVEL = "Level 4 · Advanced"
CASE_NAME = "Proseware Telecom"

ITEMS = [
# ---------------- M1 (5 + 1 in case)
multi("M1",
 "A user has the workspace Viewer role. Which three mechanisms can limit the rows they see?",
 ["A OneLake security role with a row filter on the lakehouse", "A security policy (RLS) defined at the warehouse's SQL analytics endpoint", "An RLS role in the semantic model", "A sensitivity label on the warehouse", "Certified endorsement on the semantic model"], "ABC",
 "Rows can be filtered at three layers: OneLake security, SQL endpoint RLS and semantic model RLS. Which one applies depends on how the user reaches the data. Labels and endorsement never filter data."),

yesno("M1",
 "A semantic model has RLS roles. For each user, select Yes if RLS filters their results when they use Analyze in Excel.",
 [("A user with Build permission on the model and no workspace role", True),
  ("A user with the workspace Member role", False),
  ("A user who consumes the model through a workspace app and is a member of a role", True)],
 "RLS applies to anyone without edit rights on the model, whatever client they use, Excel included. Members, Contributors and Admins can edit the model, so RLS doesn't restrict them."),

single("M1",
 "An external partner company's analysts must view one report in your tenant. What is required?",
 ["Invite them as Entra B2B guests, with external sharing allowed, then share", "Create Fabric-local accounts for them in the admin portal", "Email them the .pbix file and a .pbids file", "Publish the report to the web with a public link"], "A",
 "Fabric shares with external users through Entra B2B guest accounts, controlled by the tenant's external sharing settings. There are no Fabric-local accounts. Publish to web makes the report public to anyone, and emailing .pbix files removes all governance."),

single("M1",
 "Notebooks and pipelines must reach an ADLS Gen2 account whose firewall blocks public access. You want to avoid a gateway. Which Fabric capability lets specific workspaces through the storage firewall?",
 ["Trusted workspace access, with a workspace identity and resource instance rule", "A personal gateway on a VM inside the storage virtual network", "A firewall rule that allows all Azure service IPs", "A sensitivity label on the account that permits Fabric access"], "A",
 "Trusted workspace access lets a workspace's identity through the storage firewall with a resource instance rule. It works for shortcuts, pipelines and other access paths, and needs an F SKU capacity. Opening the storage to the public breaks the security requirement."),

single("M1",
 "Complete the warehouse RLS predicate function so each sales rep sees only their own rows.",
 ["USER_NAME()", "GETDATE()", "SESSION_USER_TABLE()", "CURRENT_TIMESTAMP"], "A",
 "In a Fabric Warehouse, USER_NAME() returns the calling user's name, which is their UPN for Entra ID users. The predicate compares it with the row's SalesRep value, and the second comparison lets the named manager see every row. The same function fills both blanks. The other options either aren't identity functions or don't exist.",
 code="""CREATE FUNCTION sec.fn_rep_filter (@SalesRep AS varchar(128))
RETURNS TABLE WITH SCHEMABINDING
AS RETURN
  SELECT 1 AS result
  WHERE @SalesRep = ______
     OR ______ = 'sales.manager@contoso.com';"""),

# ---------------- M2 (5 + 1 in case)
multi("M2",
 "Which two statements about using Git integration and deployment pipelines together are true?",
 ["A common pattern connects the Dev workspace to Git and promotes Dev to Test to Prod with a deployment pipeline", "You can also build a Git-only process by connecting each stage's workspace to its own branch and merging between branches", "Deployment pipelines keep the commit history of every item", "Git integration copies table data between workspaces", "Deployment pipelines only work if the workspaces are connected to Git"], "AB",
 "Both processes are supported. You can combine Git with pipelines, or use Git alone with a branch per stage. Pipelines don't store commit history. Git doesn't move data. Pipelines don't need Git."),

single("M2",
 "You add one new measure to a semantic model in Test and deploy it to Production with a deployment pipeline. What happens to the data in the Production model?",
 ["Only metadata is deployed; Production keeps its data and needs no refresh", "Production data is cleared and must be fully reloaded", "The Test model's data is copied into Production", "The Production model switches to DirectQuery until refreshed"], "A",
 "Pipelines deploy metadata, and the target keeps its data wherever the change allows. A new measure needs no refresh. Structural changes, such as new columns or tables, still need a refresh in the target to fill them."),

single("M2",
 "In Power BI Desktop you need to move 40 measures into new display folders and rename them in one bulk scripted edit, with a preview of the code before you apply it. Which feature should you use?",
 ["TMDL view", "Performance Analyzer", "Model view drag and drop, one measure at a time", "Power Query editor"], "A",
 "TMDL view shows model objects as TMDL script. You can edit many objects at once and apply the changes. Performance Analyzer is a profiling tool, and Power Query shapes data, not model metadata."),

single("M2",
 "Your certified shared model isn't visible to users who don't yet have access, so they keep building their own. What helps them find it and request access?",
 ["Make the endorsed model discoverable so users can request access", "Give every user Build permission on the model", "Email a .pbix copy of the model to every user", "Change the endorsement from Certified to Promoted"], "A",
 "When discoverability is enabled in the tenant settings and on the item, endorsed items appear to users who don't have access yet, and they can request it. That supports reuse instead of duplication."),

single("M2",
 "In which format is a semantic model's definition stored in a Git repository by Fabric Git integration and in .pbip projects, so it can be diffed folder by folder?",
 ["TMDL text files", "A binary .abf backup", "A .pbix file", "PBIR JSON files"], "A",
 "Semantic models are serialised as TMDL: readable text files with one file per table or object. That makes diffs and merges practical. The older single-file model.bim (TMSL JSON) is also possible, but TMDL is the default and is easier to merge.", fixed=True),

# ---------------- P1 (7)
match("P1",
 "Match each requirement to the best way to get the data into or exposed in Fabric.",
 [("A Cosmos DB database must be replicated to OneLake continuously, with no ETL", "Mirroring"),
  ("Existing Delta tables in ADLS Gen2 must be queryable in place", "Shortcut"),
  ("Copy 500 tables from Oracle nightly, then run a validation notebook", "Data pipeline"),
  ("Analysts maintain a low-code clean-up of a SharePoint list into a warehouse", "Dataflow Gen2"),
  ("IoT events must be filtered and routed in real time into an Eventhouse", "Eventstream")],
 ["Mirroring", "Shortcut", "Data pipeline", "Dataflow Gen2", "Eventstream", "Notebook"],
 "Mirroring is for continuous database replication, shortcuts for access in place, pipelines for orchestration and bulk copy, Dataflow Gen2 for low-code transforms owned by analysts, and Eventstream for real-time routing. A notebook could do several of these with code, but it isn't the best fit for any of them."),

single("P1",
 "Analysts in an Eventhouse need to join streaming events with a product dimension that lives as a Delta table in a lakehouse, without copying the dimension. What should you do?",
 ["Create a shortcut in the KQL database and query it with external_table()", "Export the dimension to CSV and ingest it hourly", "Turn on OneLake availability on the lakehouse table", "Deploy the dimension to the Eventhouse with a pipeline"], "A",
 "KQL databases support OneLake shortcuts, which appear as external tables. external_table('DimProduct') can then be joined with streaming tables, with no copy. Hourly CSV exports duplicate the data and go out of date. OneLake availability is an Eventhouse setting that works in the other direction, and deployment pipelines don't move data."),

single("P1",
 "You configure mirroring for an Azure SQL Database, and setup fails at the prerequisites check. Which configuration on the source is a documented prerequisite?",
 ["The system-assigned managed identity on the logical server", "A personal gateway installed on the database server", "Public network access turned off on the server", "Change data capture turned off on every table"], "A",
 "Mirroring Azure SQL Database needs the logical server's system-assigned managed identity. Fabric uses it to publish change data to OneLake. Mirroring doesn't depend on CDC being turned off, and a personal gateway plays no part."),

single("P1",
 "Data scientists use notebooks, and SQL analysts need read-only T-SQL access to the same curated tables. Nobody needs T-SQL writes. Which single item serves both groups?",
 ["A lakehouse: notebooks for engineers, its SQL endpoint for analysts", "A warehouse, plus a lakehouse copy for the notebooks", "An Eventhouse with OneLake availability turned on", "Two warehouses, one per team, kept in sync"], "A",
 "A lakehouse gives Spark read-write access and an automatic read-only SQL analytics endpoint. That's a perfect fit when T-SQL writes aren't needed. Copying tables into a second store adds cost and drift."),

single("P1",
 "A pipeline runs a notebook and must pass it the load date. How should the notebook receive the value?",
 ["Mark a parameter cell and set a matching base parameter in the activity", "Read the value from a Spark environment variable set by the pipeline", "Write it to a control table the notebook reads", "Set it with a parameter deployment rule on the notebook"], "A",
 "Notebook activities pass base parameters into the cell marked as the parameter cell, overriding its default values. Hard-coding defeats parameterisation, and deployment rules apply at deployment time, not at run time."),

single("P1",
 "Five hundred tables must be copied as they are from a database to a lakehouse, with no transformation, as fast as possible. Which tool fits better than a Dataflow Gen2?",
 ["A Copy activity in a metadata-driven ForEach", "A Dataflow Gen2 with 500 queries", "The Visual Query Editor, saved as views", "A KQL update policy per table"], "A",
 "Bulk movement without transformation is what the Copy activity is built for, and it scales with parallel ForEach iterations. Dataflows suit Power Query transformations owned by analysts."),

single("P1",
 "A curated table must be visible in three lakehouses across three workspaces, and changes must appear everywhere immediately, with only one physical copy. What should you do?",
 ["One physical table, with internal shortcuts in the other two", "Copy the table to the other two lakehouses nightly", "Mirror the table into the other two workspaces", "A zero-copy clone in each of the other two"], "A",
 "Internal shortcuts give one physical copy and many logical views, with immediate consistency. Nightly copies create drift. Mirroring replicates external databases."),

# ---------------- P2 (8)
single("P2",
 "In this warehouse MERGE, which clause inserts staging rows that have no match in the dimension?",
 ["WHEN NOT MATCHED BY TARGET THEN INSERT", "WHEN MATCHED THEN DELETE", "WHEN NOT MATCHED BY SOURCE THEN DELETE", "OUTPUT $action"], "A",
 "NOT MATCHED BY TARGET means the source row has no counterpart in the target, so it's a new member to insert. NOT MATCHED BY SOURCE handles target rows missing from the source. OUTPUT returns the action taken; it doesn't insert anything.",
 code="""MERGE dim.Product AS t
USING stg.Product AS s ON t.ProductCode = s.ProductCode
WHEN MATCHED AND t.ListPrice <> s.ListPrice
     THEN UPDATE SET t.ListPrice = s.ListPrice
______
     (ProductCode, ProductName, ListPrice)
     VALUES (s.ProductCode, s.ProductName, s.ListPrice);"""),

single("P2",
 "In a Delta MERGE from a notebook, matched rows should be updated only when their attribute hash has changed. Which builder call does this?",
 [".whenMatchedUpdate(condition=\"t.RowHash <> s.RowHash\", set={...})", ".whenMatchedUpdateAll(condition=\"t.RowHash = s.RowHash\")", ".whenNotMatchedInsert(condition=\"t.RowHash <> s.RowHash\")", ".whenMatchedDelete(condition=\"t.RowHash = s.RowHash\")"], "A",
 "The condition argument limits updates to rows that really changed, which avoids rewriting unchanged rows. That saves time and keeps the transaction log lean. UpdateAll with an equality condition rewrites only the rows that didn't change. A not-matched clause can't compare with the target, which has no matching row. Deleting matched rows destroys data."),

single("P2",
 "A fact row arrives for ProductCode P-991 before the product is loaded into DimProduct. The product details will arrive tomorrow. What is the recommended handling?",
 ["Insert an inferred member for P-991 now, and update it when details arrive", "Hold the fact row in staging until the product arrives", "Load the fact now with a NULL product key, then fix it", "Delete the fact row and reload it from source later"], "A",
 "An inferred (late-arriving) member gives the fact a valid surrogate key straight away, so totals stay complete. Tomorrow's load then fills in the real attributes. NULL keys and deletes lose sales or break relationships."),

single("P2",
 "In a lakehouse notebook, which Spark SQL statement creates and fills a gold Delta table from a query in one step?",
 ["CREATE TABLE gold_sales_by_day USING DELTA AS SELECT ...", "CREATE VIEW gold_sales_by_day USING DELTA AS SELECT ...", "INSERT INTO gold_sales_by_day SELECT ...", "SELECT ... INTO gold_sales_by_day FROM silver_sales"], "A",
 "CREATE TABLE ... USING DELTA AS SELECT (CTAS) creates the Delta table and loads it in one statement. A view stores no data. INSERT needs an existing table. SELECT INTO is T-SQL syntax, not Spark SQL."),

single("P2",
 "A gold table that a Direct Lake model reads has a column of binary type that holds a hashed identifier. What should you do?",
 ["Convert it to a supported type, such as hex text, or drop it", "Keep it; Direct Lake reads binary columns as text", "Turn on V-Order for the table and re-frame", "Turn on DirectQuery fallback for the model"], "A",
 "Binary and GUID types aren't supported in Direct Lake semantic models. Convert the column to a supported type upstream, or leave it out if reports don't need it. V-Order and fallback settings don't change data type support."),

single("P2",
 "Rows in FactOrders with a NULL CustomerKey disappear when FactOrders is inner-joined to DimCustomer. Why?",
 ["NULL never equals anything in a join, not even another NULL", "Inner joins sort NULL keys last and truncate them", "DimCustomer has no Unknown member row with a NULL key", "The hash join discards rows with NULL hashes"], "A",
 "In SQL, NULL = NULL is unknown, not true, so NULL keys never match. That's why gold facts should use an Unknown member key such as -1 instead of NULL."),

single("P2",
 "A Dataflow Gen2 query folds until you add one step, after which everything runs in the mashup engine. Which step commonly breaks folding against a SQL source?",
 ["Adding an index column", "Filtering rows on a date column", "Removing columns", "Renaming columns"], "A",
 "Steps that need row-by-row ordering, such as adding an index column, often can't be translated to SQL. Filters, column removal and renames normally fold. Put steps that break folding as late as you can."),

single("P2",
 "Reports mostly query sales by day, product and store, but the fact is at receipt-line grain with 5 billion rows. Which gold-layer change best supports fast Direct Lake reporting while keeping the detail?",
 ["Add a day/product/store aggregate table and keep the line fact for drill-down", "Replace the line-level fact with the daily aggregate", "Add day, product and store totals as columns on the line fact", "Partition the line fact by ReceiptID"], "A",
 "An aggregate table at the reporting grain greatly reduces the rows Direct Lake has to read and keeps the model within guardrails. Keeping the detail table preserves drill-down. Deleting the detail loses information."),

# ---------------- P3 (5 + 1 in case)
yesno("P3",
 "A running total uses SUM(Amount) OVER (ORDER BY OrderDate ...). Several rows share the same OrderDate. For each statement, select Yes if it is true.",
 [("With RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW, all rows with the same date get the same running total.", True),
  ("With ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW, each row's total grows row by row, even within the same date.", True),
  ("ROWS and RANGE always give identical results.", False)],
 "RANGE treats rows with equal ORDER BY values as peers and includes them all. ROWS counts physical rows. When the ordering column has duplicates, the frame type changes the result. That's a classic code-reading trap."),

single("P3",
 "Which T-SQL filter selects the last complete calendar month, whatever today's date is?",
 ["WHERE OrderDate > EOMONTH(GETDATE(), -2) AND OrderDate <= EOMONTH(GETDATE(), -1)", "WHERE OrderDate > DATEADD(day, -30, CAST(GETDATE() AS date))", "WHERE MONTH(OrderDate) = MONTH(GETDATE()) - 1 AND YEAR(OrderDate) = YEAR(GETDATE())", "WHERE OrderDate BETWEEN EOMONTH(GETDATE(), -1) AND EOMONTH(GETDATE())"], "A",
 "EOMONTH(GETDATE(), -1) is the last day of last month, and EOMONTH(GETDATE(), -2) is the last day of the month before. The range between them is exactly last month (for a date column). A rolling 30 days isn't a calendar month. MONTH() - 1 gives 0 in January, and the year check is then wrong too. The BETWEEN range covers this month plus last month's final day."),

single("P3",
 "In KQL, how do you calculate each session's duration?",
 ["Events | summarize Duration = max(Timestamp) - min(Timestamp) by SessionId", "Events | extend Duration = now() - Timestamp | distinct SessionId", "Events | summarize Duration = count() by SessionId", "Events | project SessionId, Duration = Timestamp - prev(Timestamp)"], "A",
 "Subtracting the first event time from the last in each session gives a timespan per session. now() - Timestamp gives each event's age. count() gives the number of events, not a duration. prev() needs a serialised, sorted row set and gives gaps between events, not a session total."),

single("P3",
 "Which DAX query returns the product keys in the Product table that have no rows in Sales?",
 ["EVALUATE EXCEPT(VALUES('Product'[ProductKey]), VALUES(Sales[ProductKey]))", "EVALUATE INTERSECT(VALUES('Product'[ProductKey]), VALUES(Sales[ProductKey]))", "EVALUATE UNION(VALUES('Product'[ProductKey]), VALUES(Sales[ProductKey]))", "EVALUATE VALUES(Sales[ProductKey])"], "A",
 "EXCEPT returns the rows of the first table that aren't in the second, which here means products with no sales. INTERSECT returns products that do have sales. UNION combines the two lists."),

single("P3",
 "Which T-SQL returns the median order amount per category on every row?",
 ["PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY Amount) OVER (PARTITION BY Category)", "AVG(Amount) OVER (PARTITION BY Category ORDER BY Amount)", "NTILE(2) OVER (PARTITION BY Category ORDER BY Amount)", "(MAX(Amount) + MIN(Amount)) / 2 OVER (PARTITION BY Category)"], "A",
 "PERCENTILE_CONT(0.5) gives the median, interpolated, and the OVER clause computes it per category. AVG is the mean, not the median, and adding ORDER BY turns it into a running average. NTILE makes groups. The midpoint of the range isn't the median."),

# ---------------- S1 (5 + 1 in case)
single("S1",
 "Which measure returns each product's sales as a share of its own category's total, respecting all other filters?",
 ["DIVIDE([Sales], CALCULATE([Sales], REMOVEFILTERS('Product'), VALUES('Product'[Category])))", "DIVIDE([Sales], CALCULATE([Sales], ALL('Product')))", "DIVIDE([Sales], CALCULATE([Sales], ALL(Sales)))", "DIVIDE([Sales], CALCULATE([Sales], ALLSELECTED('Product'[Name])))"], "A",
 "REMOVEFILTERS('Product') clears product-level filters, and VALUES('Product'[Category]) puts back the current category, which gives the category total. ALL('Product') gives the total across all categories. ALL(Sales) removes every filter on the fact. ALLSELECTED on Name gives the total of the visible products, across categories.", code=None),

single("S1",
 "A Time Intelligence calculation group must not change the [Margin %] measure, which is a ratio that doesn't make sense as YTD. How should the YTD item handle this?",
 ["Return SELECTEDMEASURE() unchanged when SELECTEDMEASURENAME() is \"Margin %\"", "Give the Margin % measure a lower precedence than the group", "Move the ratio measures into a second semantic model", "Replace the calculation group with a field parameter"], "A",
 "Calculation items can branch on SELECTEDMEASURENAME() (or ISSELECTEDMEASURE) to skip particular measures. The ratio then stays as it is while additive measures get YTD. Precedence applies to calculation groups, not measures. A second model or a field parameter is excessive and doesn't solve it."),

single("S1",
 "In a Direct Lake on OneLake composite model, an Import table of targets relates to a Direct Lake Date table. What kind of relationship is this?",
 ["A limited relationship, because the tables are in different source groups", "A regular relationship, the same as two Import tables", "An invalid relationship that can't be created", "A one-to-one relationship by definition"], "A",
 "Relationships between tables in different source groups are limited relationships. They have different semantics: for example, no blank row is added for unmatched values, and queries are evaluated differently. Design and test measures with that in mind."),

single("S1",
 "Sales holds Qty, and Product holds UnitCost. There is a many-to-one relationship from Sales to Product. Which measure returns the total cost correctly?",
 ["SUMX(Sales, Sales[Qty] * RELATED('Product'[UnitCost]))", "SUM(Sales[Qty]) * SUM('Product'[UnitCost])", "SUMX('Product', 'Product'[UnitCost]) * COUNTROWS(Sales)", "RELATED('Product'[UnitCost]) * SUM(Sales[Qty])"], "A",
 "SUMX iterates the sales rows, and RELATED fetches each row's product cost through the relationship. Multiplying two totals is wrong. RELATED can't be used outside a row context."),

single("S1",
 "DimEmployee contains EmployeeKey and ManagerKey (a parent-child hierarchy). Users need an Organisation hierarchy with Level 1, Level 2 and Level 3 managers in the model. What is the standard approach?",
 ["Flatten it into level columns with PATH and PATHITEM, then build a hierarchy", "A self-referencing relationship from ManagerKey to EmployeeKey", "A calculation group with one item per level", "A field parameter over EmployeeKey and ManagerKey"], "A",
 "Power BI hierarchies need fixed level columns. PATH and PATHITEM (or doing the same in the gold layer) flatten a parent-child structure into Level columns. Self-referencing relationships aren't supported for this."),

# ---------------- S2 (6)
single("S2",
 "A Direct Lake on OneLake model runs on an F32 capacity. Its fact table has 900 million rows, and refreshes fail. What is the cause, and what is the fix?",
 ["It's over the F32 guardrail of 300 million rows; reduce rows in gold or use F64 or larger", "It needs an incremental refresh policy to frame in chunks", "V-Order is on; turn it off so framing has less metadata to read", "The model's memory is full; turn on large semantic model storage format"], "A",
 "F2 to F32 share a 300-million-row-per-table guardrail. On Direct Lake on OneLake, going over it makes framing fail, because there's no DirectQuery fallback. Either reduce the rows in gold or use a larger SKU. Incremental refresh doesn't apply to Direct Lake."),

single("S2",
 "How can you tell whether a particular visual on a Direct Lake on SQL report is falling back to DirectQuery?",
 ["In Performance Analyzer, a Direct query duration shows on that visual", "In the Capacity Metrics app, the visual shows as DirectQuery", "In lineage view, the model shows a DirectQuery icon", "In the refresh history, each visual's fallback is listed"], "A",
 "Performance Analyzer breaks a visual down into DAX query, Direct query, visual display and other. A Direct query entry for a Direct Lake visual shows that it fell back to SQL. Lineage, refresh history and the Capacity Metrics app don't show fallback for individual visuals."),

single("S2",
 "A query uses SUMMARIZE(Sales, 'Product'[Category], \"Total\", SUM(Sales[Amount])) and is slow, with confusing results under some filters. What is the recommended rewrite?",
 ["Group with SUMMARIZE, add Total with ADDCOLUMNS and CALCULATE", "Add the Total with SUMX inside the SUMMARIZE", "Store Total as a calculated column on Sales", "Wrap the SUMMARIZE in IFERROR and CALCULATETABLE"], "A",
 "Adding calculated extension columns inside SUMMARIZE is discouraged because the semantics are complex and slow, whichever aggregate you use. Group with SUMMARIZE or SUMMARIZECOLUMNS, and add expressions with ADDCOLUMNS and CALCULATE. IFERROR and calculated columns don't address the cause."),

yesno("S2",
 "For each statement about Direct Lake memory behaviour, select Yes if it is true.",
 [("Direct Lake loads only the columns that queries need into memory.", True),
  ("If memory runs short, Direct Lake can evict less-used columns and reload them later.", True),
  ("Direct Lake loads the whole model into memory at framing time.", False)],
 "Direct Lake loads columns on demand and evicts (pages out) cold columns under memory pressure. That's why it can work with more data than fits in memory at once. Framing loads no data."),

single("S2",
 "A team wants to run OPTIMIZE (with V-Order) and VACUUM on lakehouse tables without writing any code. What can they use?",
 ["The table's Maintenance option in the lakehouse explorer", "A deployment pipeline's post-deploy step", "The Visual Query Editor on the SQL endpoint", "The semantic model's refresh settings"], "A",
 "The lakehouse explorer has table maintenance options that run OPTIMIZE, with optional V-Order, and VACUUM with a retention you choose. For automation, schedule a notebook that runs the same commands. The other tools don't maintain tables."),

single("S2",
 "A composite model has a DirectQuery fact and an Import aggregation table at Date × Category grain. A visual showing Sales by Date and Product Color still sends queries to the source. Why?",
 ["The aggregation doesn't cover Color, so the query goes to the detail fact", "Aggregations only apply to measures written with SUMX", "The Date table is in Dual mode instead of Import", "The aggregation table is too large to stay in memory, so it's skipped"], "A",
 "An aggregation is only used when every column in the query is covered at its grain, directly or through relationships. Color is below the Category grain, so the detail fact is queried. Either add Color to the aggregation or accept the DirectQuery cost for that visual."),

# ---------------- Case study (M1, M2, P3, S1)
case("Proseware Telecom",
 "Proseware Telecom stores call detail records (CDRs) in an Eventhouse and billing data in a warehouse. A certified semantic model serves finance. Monthly finance reports are often exported to Excel and emailed to auditors at external firms.\n\nFamily plans are shared by up to five subscribers, and each holds an ownership percentage. The model is developed as TMDL in Azure DevOps and released through automated pipelines.",
 ["R1. Exported finance files must stay unreadable to anyone outside Proseware, even if they're forwarded.",
  "R2. Model releases must be scripted, quality-checked and approved before Production.",
  "R3. Network operations needs dropped calls per cell tower per hour over the last 24 hours, with zero shown for hours that had no drops.",
  "R4. Plan revenue must be split between subscribers by ownership percentage, without double counting."],
 [
  single("M1", "Which control over exported files satisfies R1?",
   ["A sensitivity label that encrypts content for internal users only", "Certification of the finance semantic model", "RLS roles that exclude every external user's UPN", "Assigning the workspace to a protected Finance domain"], "A",
   "Labels with encryption protect exported files wherever they go. Only authorised users can open them. Certification, RLS and domains have no effect once a file has left Fabric."),
  order("M2", "Put the steps of the release process for R2 in order.",
   ["Commit the TMDL changes and open a pull request",
    "Run automated checks in the build pipeline, such as Best Practice Analyzer rules",
    "Deploy to the Test workspace through the XMLA endpoint with a scripted tool",
    "Get approval, then deploy the same build to Production"],
   "Changes are reviewed in a pull request, checked automatically, deployed to Test by script, and promoted to Production only after approval. Editing Production by hand or publishing a .pbix skips the controls R2 requires.",
   extra=["Edit the Production model directly in the service", "Publish a .pbix from a developer's laptop"]),
  single("P3", "Which KQL query satisfies R3, including the zeros?",
   ["CDR | where Timestamp > ago(24h) and CallResult == \"Dropped\" | make-series Drops = count() default = 0 on Timestamp from ago(24h) to now() step 1h by TowerId",
    "CDR | where Timestamp > ago(24h) and CallResult == \"Dropped\" | summarize Drops = count() by TowerId, bin(Timestamp, 1h)",
    "CDR | where Timestamp > ago(24h) | summarize Drops = countif(CallResult == \"Dropped\") by bin(Timestamp, 1h)",
    "CDR | where CallResult == \"Dropped\" | make-series Drops = count() on Timestamp step 1h | take 24"], "A",
   "make-series builds a continuous series over the range, with default = 0 filling empty hours. summarize ... by bin() leaves gaps where there were no events, and the countif version doesn't group by tower either. make-series without a from/to range and by TowerId doesn't give 24 hours per tower."),
  single("S1", "Which revenue-allocation design satisfies R4?",
   ["A PlanSubscriber bridge with OwnershipPct, used as a weight in a SUMX", "Divide each plan's revenue by five, the most subscribers allowed", "Copy the full plan revenue to every subscriber", "A bidirectional PlanSubscriber bridge with no weight column"], "A",
   "A weighted bridge allocates each plan's revenue by ownership share, so subscriber totals add up to plan totals. A fixed split by five is wrong for most plans, and copying the full amount double counts."),
 ]),
]
