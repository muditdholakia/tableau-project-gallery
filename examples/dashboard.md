# Dashboard build recipe

Set Date to a date, Quantity and Unit Price to numbers. Create:

```tableau
// Revenue
[Quantity] * [Unit Price]
```

```tableau
// Average Sale
SUM([Revenue]) / COUNTD([Sale ID])
```

Create KPI sheets for SUM(Revenue), SUM(Quantity), and Average Sale.
Create a line chart of continuous MONTH(Date) against SUM(Revenue), and a bar
chart of Region against SUM(Revenue). Assemble a 1200 × 800 dashboard with KPIs
above the two charts. Add Region as a filter applying to all sheets. Include
currency labels, descriptive titles, alt text, and a note that data is synthetic.
Validate 120 distinct sales and compare totals with the source before publishing.
