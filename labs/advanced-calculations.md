# Advanced calculations: original exercise plan

Use `python examples/generate_sales.py` to create 120 synthetic sales. Build these
exercises independently before consulting Andy Kriebel's attributed solution collection.
These formulas and tasks are newly written for this repository, not copied blog excerpts.

## 1. Understand the grain

Create `[Revenue] = [Quantity] * [Unit Price]`. Put Region on Rows and SUM(Revenue)
on Columns. Add a label with the total. Check that the regional totals sum to the
full CSV total; use COUNTD(Sale ID) to confirm 120 distinct transactions.

## 2. FIXED level of detail

Create `[Region Revenue] = { FIXED [Region] : SUM([Revenue]) }`. Put Sale ID and
Region in a text table and inspect the repeated regional value. Do not sum a
repeated regional total across transactions; use MIN or ATTR when displaying it.
Apply a Date filter, record what changes, then make it a context filter and repeat.
Explain the different results using Tableau's current order-of-operations guide.

## 3. Running total

Put continuous day of Date on Columns and SUM(Revenue) on Rows. Add
`RUNNING_SUM(SUM([Revenue]))` and set Compute Using to Date. Add Region to Color,
then verify that each regional partition ends at its own regional total.

## 4. Percent of regional total

Create `SUM([Revenue]) / WINDOW_SUM(SUM([Revenue]))`. Display months within each
region, set addressing to Month and partitioning to Region, and format as a
percentage. Each complete regional partition should sum to 100%.

## 5. Metric selector

Create a string parameter `Metric` with values Revenue and Quantity. Create:

```tableau
CASE [Metric]
WHEN "Revenue" THEN [Revenue]
WHEN "Quantity" THEN [Quantity]
END
```

Chart SUM of this field by month. Show the parameter, change it, and verify totals.
Then build a selector sheet and configure a Change Parameter action. Check selection
and clearing behavior, and label the selected metric clearly.

## Evidence to capture

Save your original workbook with synthetic data as a TWBX, include a source/license
notice, and capture screenshots free of private server information. Record addressing,
partitioning, and filter/context settings beside each result. Do not claim authorship
of the imported Andy Kriebel workbook.

Reference: [Tableau order of operations](https://help.tableau.com/current/pro/desktop/en-us/order_of_operations.htm).
