from model import single, multi, yesno, match, order, case

TITLE = "Final mock exam"
SUBTITLE = "Sit this one last, under exam conditions, in one 100-minute session. It mixes every format and every sub-area at full difficulty."
LEVEL = "Level 5 · Final mock"
CASE_NAME = "Coho Winery"

ITEMS = [
# ---------------- M1 (6)
multi("M1",
 "A data scientist needs Spark read access to the tables of one lakehouse only, and nothing else in the workspace. Which two approaches meet the requirement with least privilege?",
 ["Share the lakehouse with the data scientist and grant ReadAll, with no workspace role", "Give the workspace Viewer role plus a OneLake security role that grants read on the lakehouse's tables", "Give the workspace Contributor role", "Give the workspace Member role", "Share the lakehouse with Write permission"], "AB",
 "Item sharing with ReadAll limits access to that lakehouse and allows Spark reads. A Viewer with a OneLake security role gets the same through roles. Contributor, Member and Write all grant write access well beyond reading."),

single("M1",
 "You created a OneLake security role that grants a group read on the Sales table only. Users in the group who were given ReadAll on the lakehouse can still read every table. What is the most likely reason?",
 ["DefaultReader still grants them everything, and roles add up", "OneLake roles only take effect after 24 hours", "The new role needs a Deny rule on the other tables", "The other tables are shortcuts, which ignore roles"], "A",
 "OneLake security roles add up. DefaultReader gives ReadAll users access to everything, so a narrower role makes no difference until DefaultReader is changed or those users are taken out of it. Roles grant access; there are no Deny rules to add. They apply straight away, and shortcuts don't bypass them."),

single("M1",
 "The central governance team wants Fabric items to appear in Microsoft Purview Unified Catalog alongside Azure SQL and ADLS sources, with lineage and classification. What should they do?",
 ["Register and scan the Fabric tenant in Purview", "Certify every item they want catalogued", "Connect every workspace to a Git repository", "Create a Fabric domain for each Azure source"], "A",
 "Scanning the Fabric tenant from Purview brings Fabric metadata into the enterprise catalogue and Data Map, next to other sources. Certification and Git don't publish metadata to Purview. Domains organise workspaces within Fabric."),

match("M1",
 "Match each requirement to the layer where the row filter should be defined.",
 [("Both Spark notebooks and SQL queries on a lakehouse must enforce a region filter", "OneLake security role"),
  ("Only T-SQL users and a Direct Lake on SQL analytics endpoint model must honour the filter defined in the warehouse", "SQL analytics endpoint security policy"),
  ("Consumers of an Import model through an app see only their own region", "Semantic model RLS role")],
 ["OneLake security role", "SQL analytics endpoint security policy", "Semantic model RLS role", "Sensitivity label"],
 "Define the filter at the layer every access path goes through. OneLake security covers all engines, SQL policies cover SQL access (including Direct Lake on SQL with SSO), and model RLS covers model consumers. Labels never filter rows."),

single("M1",
 "Support staff may query dbo.Customer in a warehouse but must be blocked from the Email column only. All other columns must stay queryable. Which statement does this most directly?",
 ["DENY SELECT ON dbo.Customer (Email) TO Support;", "DENY SELECT ON dbo.Customer TO Support;", "REVOKE CONNECT FROM Support;", "ALTER TABLE dbo.Customer DROP COLUMN Email;"], "A",
 "A column-level DENY blocks that column, and any query that references it, while the rest of the table stays available. Denying the whole table or revoking CONNECT goes too far. Dropping the column destroys the data."),

single("M1",
 "Report authors must build new reports on a semantic model in the Finance workspace. They must not see or open any other item in that workspace. What should you grant?",
 ["Build permission on the model, with no workspace role", "The Viewer role on the Finance workspace", "The Contributor role on the Finance workspace", "Write permission on the model, with no workspace role"], "A",
 "Build on the item is enough to create reports, including in their own workspaces, and exposes nothing else. Any workspace role shows every item. Write would let them change the model."),

# ---------------- M2 (5 + 1 in case)
single("M2",
 "Several items in a Git-connected workspace have changed. A developer wants to commit only the semantic model and keep a half-finished notebook out of the commit. What can they do?",
 ["Select only the semantic model in the pane and commit", "Commit everything; commits always include all items", "Move the notebook to another workspace first", "Disconnect Git, commit the model, then reconnect"], "A",
 "The source control pane lets you choose which changed items to commit, so unfinished work stays uncommitted. You don't need to delete or disconnect anything."),

single("M2",
 "Notebooks deployed from Dev to Test must automatically attach to the Test lakehouse, not the Dev lakehouse. What should you configure in the deployment pipeline?",
 ["A default lakehouse rule for the notebooks in Test", "A data source rule on the notebooks' reports", "A parameter rule on the Test dataflows", "A Git branch per stage with its own lakehouse"], "A",
 "Notebook deployment rules can change the default lakehouse per stage, so the same notebook runs against each stage's lakehouse. Data source and parameter rules apply to other item types."),

yesno("M2",
 "For each statement about the XMLA endpoint, select Yes if it is true.",
 [("With the Read setting, client tools such as DAX Studio and Excel can query the model.", True),
  ("With the Read Write setting, SQL Server Management Studio can refresh individual partitions.", True),
  ("The XMLA endpoint is available for workspaces on shared (Pro) capacity.", False)],
 "Read allows queries and metadata browsing. Read Write adds management operations, such as processing partitions and deploying. The XMLA endpoint needs Fabric, Premium or Premium Per User capacity."),

single("M2",
 "Impact analysis on a lakehouse lists 22 downstream reports. You have time to contact only the owners of the most-used ones before a change. Which information in impact analysis helps you prioritise?",
 ["The view counts of the affected items", "The items' sensitivity labels", "The number of measures in each model", "The colours used in each report"], "A",
 "Impact analysis shows usage, such as views, alongside the affected workspaces and items, so you can focus on the reports that matter most. Labels and model contents don't tell you about usage."),

single("M2",
 "A workspace connected to Git contains some item types that Fabric Git integration doesn't support. What happens to those items?",
 ["They stay in the workspace but are left out of Git", "They're deleted from the workspace on the next Update", "The Git connection fails for the whole workspace", "They're stored as binary files in the repository"], "A",
 "Git integration syncs only supported item types. Other items stay in the workspace untouched and don't appear in the repository. Check the current list of supported items before relying on Git for a given item type."),

# ---------------- P1 (6 + 1 in case)
single("P1",
 "Sensor data in an Eventhouse must be fast to query for the last 30 days and kept for two years in total. Which settings should you configure on the KQL database or table?",
 ["A 30-day caching policy and a 730-day retention policy", "A 730-day caching policy and a 30-day retention policy", "V-Order on the KQL table, with a 730-day retention", "A 30-day retention policy, with OneLake availability on"], "A",
 "The caching policy decides how much recent data is kept in the hot cache for the fastest queries. The retention policy decides how long data is kept at all. Swapping the two values deletes data after 30 days. V-Order applies to Delta writes from Spark, not to KQL tables, and OneLake availability doesn't extend retention."),

single("P1",
 "A team wants to copy changed rows from a cloud database into a lakehouse every hour, incrementally, with a simple guided setup and no pipeline to design. Which Fabric item is designed for this?",
 ["A Copy job", "A Spark job definition", "A KQL queryset", "A deployment pipeline"], "A",
 "Copy job is a simplified item for data movement that supports full and incremental copies on a schedule, without building a pipeline. Spark job definitions run code. The other two don't move data."),

multi("P1",
 "Which three Fabric items can be the target of an internal OneLake shortcut?",
 ["A lakehouse", "A KQL database", "A warehouse", "A Power BI report", "A deployment pipeline"], "ABC",
 "Internal shortcuts point at data in Fabric items, such as lakehouses, warehouses, KQL databases and mirrored databases. Reports and pipelines don't hold tabular data that a shortcut can reference."),

single("P1",
 "A pipeline must pull JSON from a REST API that returns 100 records per page with a next-page link. You want a no-code solution. What should you use?",
 ["A Copy activity with REST pagination rules", "A Dataflow Gen2 with a single Web call", "An external shortcut to the API URL", "Mirroring of the API's database"], "A",
 "The Copy activity's REST source supports pagination rules that follow next-page links until there are none left. Shortcuts and mirroring don't connect to REST APIs. A single web call returns only the first page."),

single("P1",
 "SQL developers must INSERT and UPDATE the curated tables with T-SQL, and data scientists must read the same tables from Spark notebooks. Where should the curated tables live?",
 ["In a warehouse; Spark reads its Delta tables through OneLake, for example through a shortcut or the OneLake path", "In a lakehouse, with the SQL developers writing through the SQL analytics endpoint", "In an Eventhouse", "In two copies, one per team"], "A",
 "T-SQL writes need a warehouse. Warehouse tables are Delta in OneLake, so Spark can read them without a copy. A lakehouse SQL endpoint can't write data."),

single("P1",
 "An Eventstream carries freezer temperature readings. Operations wants an email within seconds whenever a reading goes above -15 °C. What should you add?",
 ["An Activator destination with a threshold rule", "A pipeline that checks readings every hour", "A Power BI report subscription by email", "A KQL queryset with the threshold query saved"], "A",
 "Activator watches streaming data and fires actions, such as email or Teams messages, when conditions are met, in real time. Hourly pipelines, saved querysets and report subscriptions can't react within seconds."),

# ---------------- P2 (8)
single("P2",
 "A warehouse dimension needs integer surrogate keys for new members, continuing from the current maximum. Which pattern is reliable?",
 ["MAX(existing key) + ROW_NUMBER() over the new rows", "NEWID() for each new row", "Use the business key as the surrogate key", "CAST(RAND() * 1000000 AS int) for each new row"], "A",
 "Adding ROW_NUMBER to the current maximum gives compact, sequential integer keys for the new rows. NEWID gives GUIDs, which are wide, unsupported in Direct Lake and compress poorly. RAND can collide. Business keys tie the model to the source system."),

single("P2",
 "In PySpark, a developer generates surrogate keys with monotonically_increasing_id(). Which statement about the values is true?",
 ["They're unique and increasing, but not consecutive", "They're consecutive integers starting from 1", "They're GUIDs encoded as long integers", "They're guaranteed identical across reruns"], "A",
 "monotonically_increasing_id encodes the partition ID in the upper bits, so the values are unique and increasing, but with large gaps between partitions. If you need consecutive keys, use row_number over a window, plus an offset from the existing maximum."),

single("P2",
 "A staging column Quantity is text, and a few rows contain values like 'N/A'. The load must convert valid values to int and turn invalid ones into NULL, without failing. Which expression should you use?",
 ["TRY_CAST(Quantity AS int)", "CAST(Quantity AS int)", "CONVERT(int, Quantity)", "ISNUMERIC(Quantity)"], "A",
 "TRY_CAST returns NULL when the conversion fails, instead of raising an error. CAST and CONVERT fail the whole statement on 'N/A'. ISNUMERIC returns a flag, not a converted value."),

single("P2",
 "A notebook reads thousands of daily CSV files with inferSchema=true. It's slow, and column types sometimes change between runs. What should you do?",
 ["Pass an explicit StructType schema to the reader", "Increase the number of executors", "Set samplingRatio so inference reads fewer rows", "Read each file in a separate notebook run"], "A",
 "An explicit schema avoids the extra pass inferSchema needs and pins the column types, so they don't drift from run to run. More executors don't fix inconsistent types."),

single("P2",
 "An analyst in Dataflow Gen2 wants a new column that pulls the first name out of values like \"Smith, Jane\" by typing a couple of example outputs, rather than writing M code. Which feature should they use?",
 ["Column from examples", "Conditional column", "Merge queries with fuzzy matching", "Fill down"], "A",
 "Column from examples works out the transformation from sample outputs you type, then writes the M expression for you. A conditional column needs rules you define yourself, and the other features join or fill values."),

yesno("P2",
 "For each statement about star schemas in the gold layer, select Yes if it is true.",
 [("Fact tables hold foreign keys to dimensions plus numeric measures at a declared grain.", True),
  ("Dimension tables hold descriptive attributes used to filter and group.", True),
  ("For Power BI, a deeply snowflaked dimension is generally preferable to a flattened one.", False)],
 "Facts hold keys and measures, and dimensions hold descriptive context. Power BI guidance favours flattened (star) dimensions over snowflakes, for simpler models and fewer relationship hops."),

single("P2",
 "A monthly summary over a 6-billion-row fact is read by hundreds of report queries a day. As a view, it recalculates the aggregation every time and is slow. What is the better gold-layer design?",
 ["Persist the summary as a table, rebuilt after each load", "Keep the view and add WITH (NOLOCK) hints", "Turn the view into a stored procedure", "Move the aggregation into each report's measures"], "A",
 "A view recalculates on every query. When the same expensive aggregate is read often, storing it once per load is cheaper and faster. Direct Lake can also read a table but not a view. A stored procedure can't be queried like a table, and locking hints don't make the aggregation cheaper."),

single("P2",
 "A daily sales fact has no rows on days a store was closed. A report must show every day, with 0 for closed days. What should the gold-layer query do?",
 ["Cross join DimDate with stores, LEFT JOIN the fact, COALESCE to 0", "INNER JOIN DimDate to the fact, with COALESCE to 0", "LEFT JOIN the fact to DimDate, with COALESCE to 0", "Leave the gaps for the report to handle"], "A",
 "Building the full date-by-store grid first, then left joining the facts, makes sure every day appears, and COALESCE turns the missing sales into zeros. An inner join keeps the gaps. Left joining the fact to DimDate keeps only the days that have sales, and DimDate alone has no store dimension."),

# ---------------- P3 (5 + 1 in case)
single("P3",
 "For each customer order, you need the number of days until that customer's next order. Which expression should you use?",
 ["DATEDIFF(day, OrderDate, LEAD(OrderDate) OVER (PARTITION BY CustomerKey ORDER BY OrderDate))", "DATEDIFF(day, OrderDate, LAG(OrderDate) OVER (ORDER BY OrderDate))", "DATEDIFF(day, MIN(OrderDate), MAX(OrderDate))", "ROW_NUMBER() OVER (PARTITION BY CustomerKey ORDER BY OrderDate)"], "A",
 "LEAD gets the next order date within the customer's partition, and DATEDIFF measures the gap. LAG looks backwards, and without a partition it mixes customers. MIN and MAX give one span per group, not one per order."),

single("P3",
 "Logs are split across the KQL tables Logs2025 and Logs2026. You need to query both as one, and know which table each row came from. Which query does this?",
 ["union withsource=SourceTable Logs2025, Logs2026 | where Level == \"Error\"", "Logs2025 | join kind=fullouter Logs2026 on Timestamp", "Logs2025 | union Logs2026 | where Level == \"Error\"", "Logs2025 | lookup Logs2026 on Level | extend Source = \"both\""], "A",
 "union stacks tables, and withsource adds a column naming each row's source table. A plain union works but doesn't say where each row came from. Joins and lookups combine columns, not rows."),

single("P3",
 "Which DAX query returns the single best-selling product in each region?",
 ["EVALUATE GENERATE(VALUES('Geo'[Region]), TOPN(1, VALUES('Product'[Name]), [Total Sales], DESC))", "EVALUATE TOPN(1, 'Product', [Total Sales])", "EVALUATE SUMMARIZECOLUMNS('Geo'[Region], \"Top\", MAX('Product'[Name]))", "EVALUATE VALUES('Product'[Name])"], "A",
 "GENERATE evaluates TOPN once per region, in that region's context, which gives the top product in each. TOPN on its own returns one product overall. MAX of the name returns the alphabetically last name, not the best seller."),

single("P3",
 "A table has 1,000 rows. MiddleName is NULL in 400 of them. What do COUNT(*) and COUNT(MiddleName) return?",
 ["1,000 and 600", "600 and 600", "1,000 and 1,000", "400 and 600"], "A",
 "COUNT(*) counts rows. COUNT(column) counts the non-NULL values in that column. That difference often explains reconciliation gaps.", fixed=True),

single("P3",
 "A user built a query in the Visual Query Editor and wants to hand-edit the generated T-SQL to add a window function. What should they do?",
 ["View the generated SQL and open it as a new SQL query", "Add a window step from the editor's toolbar", "Save it as a view, then edit the view in the editor", "Open it in the DAX query view to edit"], "A",
 "The Visual Query Editor shows the T-SQL it generates. Users can open that as a SQL query and extend it by hand, which is useful when the visual steps can't express a window function. The visual editor has no window step, and the DAX query view works on semantic models, not the warehouse."),

# ---------------- S1 (6)
single("S1",
 "A Direct Lake model needs an AgeBand attribute derived from BirthDate. The solution must work for both Direct Lake variants and must not depend on preview features. Where should AgeBand be created?",
 ["As a column in the gold Delta table", "As a DAX calculated column", "As a calculated table of age bands", "As a report-level measure"], "A",
 "Calculated columns and tables aren't supported in Direct Lake on SQL, and their support in Direct Lake on OneLake has been limited or in preview. Creating the attribute in the gold layer works everywhere and for every consumer."),

single("S1",
 "A card must show 0 instead of blank when a region has no sales in the selected period. Which measure is the most concise?",
 ["COALESCE([Total Sales], 0)", "IF(ISERROR([Total Sales]), 0)", "[Total Sales] * 0", "BLANK()"], "A",
 "COALESCE returns the first non-blank argument, so blank becomes 0. ISERROR checks for errors, not blanks. Multiplying by 0 returns 0 even when there are sales."),

single("S1",
 "A measure must return the revenue of the first month in the selected period, as a baseline for an index chart. Which window function should you use?",
 ["CALCULATE([Revenue], INDEX(1, ALLSELECTED('Date'[YearMonth]), ORDERBY('Date'[YearMonth], ASC)))", "CALCULATE([Revenue], OFFSET(1, ALLSELECTED('Date'[YearMonth])))", "CALCULATE([Revenue], WINDOW(0, REL, 0, REL, ALLSELECTED('Date'[YearMonth])))", "RANK(DENSE, ALLSELECTED('Date'[YearMonth]))"], "A",
 "INDEX(1, ...) returns the first row of the ordered relation, which is the first selected month, whatever the current row is. OFFSET(1) is the next row. WINDOW(0, REL, 0, REL) is the current row. RANK returns a number, not a revenue."),

single("S1",
 "In a Direct Lake model, a relationship joins FactSales[ProductKey] (bigint) to DimProduct[ProductKey] (string). Visuals that use the relationship fail. What should you do?",
 ["Make both columns the same type in gold, ideally integer", "Make the relationship filter in both directions", "Change the column's data type in the model view", "Set DirectLakeBehavior to Automatic for fallback"], "A",
 "Direct Lake needs related columns to have matching data types. Fix the type upstream, preferably as integers for compression. Filter direction and fallback settings don't fix a type mismatch."),

single("S1",
 "An analyst wants a slider from 0% to 20% in steps of 1%, which a measure then uses to project price increases. What does creating a numeric range (what-if) parameter generate?",
 ["A GENERATESERIES table plus a SELECTEDVALUE measure", "A calculation group with 21 items", "A field parameter table that uses NAMEOF", "A table related to the fact by percentage"], "A",
 "A what-if parameter creates a disconnected table from GENERATESERIES and a measure such as SELECTEDVALUE(Parameter[Value], default). Your measures then use it. It doesn't relate to the facts."),

multi("S1",
 "Which two of these are DAX window functions?",
 ["OFFSET", "WINDOW", "EARLIER", "RELATED", "LOOKUPVALUE"], "AB",
 "The window function family is INDEX, OFFSET, WINDOW, RANK and ROWNUMBER, and they share the relation, ORDERBY and PARTITIONBY parameters. EARLIER refers to an outer row context, RELATED follows a relationship, and LOOKUPVALUE finds a value by matching columns."),

# ---------------- S2 (5 + 1 in case)
single("S2",
 "You need to confirm whether V-Order is turned on for an existing gold Delta table in a lakehouse. What should you check?",
 ["The table property delta.parquet.vorder.enabled", "The semantic model's DirectLakeBehavior", "The workspace's Spark pool settings", "The table's row count in DESCRIBE DETAIL"], "A",
 "V-Order is controlled at session, table or write level, and the table property records the setting for the table. The other settings aren't related to V-Order."),

single("S2",
 "A measure defines VAR TotalAll = [Sales] and then returns CALCULATE(TotalAll, ALL('Product')), expecting the all-products total. It returns the same value as [Sales]. Why?",
 ["A VAR is evaluated where it's defined, so CALCULATE can't change it", "ALL only works on the fact table, not on dimensions", "CALCULATE needs a measure reference, not a column", "ALL needs REMOVEFILTERS alongside it to work"], "A",
 "A VAR is a constant that's already been evaluated in the outer context, so CALCULATE's filters can't affect it. Write CALCULATE([Sales], ALL('Product')), either directly or inside the variable's definition. This trap catches performance tuners and correctness reviewers alike."),

single("S2",
 "In a composite model, slicers on DimCustomer (which relates to an Import aggregation and to a DirectQuery fact) send a DirectQuery query every time the page loads. Which change helps most?",
 ["Set DimCustomer to Dual storage mode", "Set DimCustomer to DirectQuery", "Remove the relationship to the aggregation", "Turn off query reduction"], "A",
 "Dual lets the engine answer slicer and aggregation queries from memory, while still joining to the DirectQuery fact when it needs to. DirectQuery storage would send every slicer query to the source."),

yesno("S2",
 "For each statement about Direct Lake guardrails, select Yes if it is true.",
 [("Capacities from F2 to F32 share the same per-table row guardrail.", True),
  ("Most guardrails are checked per query, while the maximum model size in memory is checked at the model level.", True),
  ("A Direct Lake model can use an on-premises data gateway to reach its data.", False)],
 "Guardrails step up from F64. Most limits apply per query, but model memory is a model-level limit. Direct Lake reads OneLake directly and can't use any gateway."),

single("S2",
 "A slicer on CustomerName lists 5 million distinct values, and the page loads slowly. What is the best design change?",
 ["Filter on a lower-cardinality attribute, or use the filter pane", "Sort the slicer by name and turn on Select all", "Turn the slicer into a table visual of all customers", "Make the Customer relationship bidirectional"], "A",
 "A slicer has to fetch its distinct values, and millions of them are expensive to query and render. Filtering by lower-cardinality attributes, or using search and the filter pane, keeps pages responsive."),

# ---------------- Case study (M2, P1, P3, S2)
case("Coho Winery",
 "Coho Winery operates vineyards in France, Spain and Italy. EU regulation requires all its analytics data to stay in the EU. One central semantic model is used by 30 thin reports owned by regional teams, each in its own workspace.\n\nSales by varietal (Merlot, Tempranillo, Sangiovese and others) are stored in a warehouse. A Direct Lake on OneLake model reads the gold lakehouse. Its fact table has grown past the capacity's row guardrail, and someone has set DirectLakeBehavior to Automatic, expecting that to keep reports working.",
 ["R1. All Fabric data must remain in the EU.",
  "R2. The central model must be changed and released independently of the 30 reports, and the reports must always use the governed model.",
  "R3. A SQL report must show monthly sales with one column per varietal.",
  "R4. Reports must work again after the fact table outgrew the guardrail."],
 [
  single("P1", "Which configuration satisfies R1?",
   ["Assign the workspaces to a capacity in an EU region", "Apply an EU-only sensitivity label", "Assign the workspaces to an EU domain", "Set the tenant's home region in each workspace"], "A",
   "Data residency in Fabric follows the region of the capacity a workspace is assigned to. Labels and domains are governance metadata and don't control where data is stored."),
  single("M2", "Which model-and-report architecture satisfies R2?",
   ["One model in its own workspace; thin reports connect to it live", "Embed a copy of the model in each of the 30 reports", "Merge all 30 reports into the model's .pbix", "Give each region its own copy of the model"], "A",
   "The thin-report pattern keeps one governed model with its own lifecycle, and reports connect to it live. Copies of the model drift apart, and a single .pbix ties every report's release to the model's."),
  single("P3", "Which T-SQL approach to the varietal columns satisfies R3?",
   ["SUM(CASE WHEN Varietal = 'Merlot' THEN Amount END) AS Merlot, … GROUP BY Month", "SELECT Month, STRING_AGG(Varietal, ',') … GROUP BY Month", "SELECT Month, Varietal, SUM(Amount) … GROUP BY Month, Varietal", "A recursive CTE that walks the varietals"], "A",
   "Conditional aggregation turns rows into columns with plain SUM(CASE ...) expressions, which work in any SQL engine. GROUP BY Month, Varietal keeps varietals as rows, and STRING_AGG makes one text list. No static SQL can add columns by itself, so a new varietal means extending the column list, or pivoting in the semantic model instead."),
  single("S2", "Which statement about R4 is correct?",
   ["OneLake has no fallback; reduce the table's rows or use a larger capacity", "Automatic already falls back to DirectQuery; nothing else is needed", "Set DirectLakeBehavior to DirectLakeOnly to raise the limit", "Run VACUUM, then OPTIMIZE, to cut the row count"], "A",
   "Only Direct Lake on the SQL analytics endpoint can fall back to DirectQuery. Direct Lake on OneLake has no fallback, so a guardrail breach still fails whatever DirectLakeBehavior says, and no setting raises the guardrail. VACUUM and OPTIMIZE don't reduce the rows in active files."),
 ]),
]
