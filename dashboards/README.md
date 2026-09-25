# Automobile dashboard

## Open and explore

Download [`index.html`](index.html) and open it in a browser. GitHub displays HTML source rather than executing it; choose **Download raw file** before opening it locally. The file embeds the public dataset and requires no installation, web server, network access, or external libraries.

- Select a reporting year, country, and make. The filters are applied together.
- Switch the charts between recorded sale value and record count. Summary cards retain their own labels and definitions.
- Hover over bars and headline amounts for more precise values.
- Use **Export selection** to download all selected records, including all 15 public columns. It is disabled when the selection is empty.
- Use **Reset filters** to restore the full dataset and default chart measure.
- Use **Print / PDF** for a static snapshot of the current selection.
- Switch to **Task views** for the pending assignment analysis: monthly trend and moving average, annual growth, top-model ranking, vehicle/country mix, price distribution, and sale value versus the documented total-cost proxy.

The largest-sales table shows at most eight selected rows. It is not the full export. On narrow screens the table can scroll horizontally. The task view deliberately labels metrics that need a business definition, such as profit margin and sales variance, instead of presenting them as verified KPIs.

## Files

| File | Purpose |
| --- | --- |
| [`index.html`](index.html) | Ready-to-open interactive dashboard |
| [`src/dashboard.html`](src/dashboard.html) | Editable HTML/CSS/JavaScript template with a data placeholder |
| [`screenshots/automobile-overview.png`](screenshots/automobile-overview.png) | Default, unfiltered dashboard preview |
| [`screenshots/automobile-task-views.png`](screenshots/automobile-task-views.png) | Assignment task-view preview |
| [`exports/automobile-dashboard.pdf`](exports/automobile-dashboard.pdf) | Two-page static snapshot of the default selection |

To rebuild after reviewing a change to the CSV or template:

```sh
python scripts/validate_data.py
python scripts/build_dashboard.py
```

Then open the rebuilt HTML and refresh the screenshot/PDF. The PDF uses A4 landscape with backgrounds enabled. Its first page contains summary cards and charts; the second contains source-data observations and the largest recorded sales. The PDF and screenshot do not automatically update when the CSV changes.

## Original versus new work

This dashboard was newly created during portfolio preparation, at the requester's direction, using the supplied automobile workbook. It uses HTML, CSS, and JavaScript. It is not a `.pbix` file and does not claim to implement the brief's DAX or Power Query exercises.

The original attachment named `Automobile Dashboard Analysis.pdf` is an eight-page retail export with unrelated fields and customer names. It is preserved locally and excluded from this repository. The second original PDF is an assignment brief, not a completed report.

## Definitions and validation

Recorded sale value is the sum of `SalePrice`. Average sale price is that sum divided by selected row count. Task-view average sales per month divides the selection total by the number of reporting months represented; latest-year sales use the latest year in the filtered selection; trailing sales use the latest 12 chronological source months. High-value sales use a transparent `SalePrice >= 100000` threshold. The total-cost comparison uses the assignment's expression `CostPrice + DeliveryCharge + SpareParts + LaborCost` and is labelled a proxy. Currency and discount treatment are unspecified. Record count is not a verified count of unique vehicles or invoices.

Browser checks reconciled default totals, individual and combined filters, and all embedded source cells against the original workbook. Empty states, reset, count-mode charts, selected-record export, client-name exclusion, mobile width, and browser errors were checked. The PDF was rendered and visually inspected. Data-quality observations remain visible rather than being silently corrected. See [methodology](../docs/methodology.md) for definitions.

## Colour palette

Solid chart colours are sampled from the supplied Power BI PDF: blue `#118DFF`, dark blue `#12239E`, and orange `#E66C37`. White report panels and neutral text replace the previous teal styling. Vehicle-type colours remain consistent when filters change. The PDF is a colour reference only; none of its unrelated retail data is used.

## Hosting

The dashboard can run as a public interactive website on Vercel. See [deployment instructions](../docs/deployment.md), including the repository-owner requirement and the distinction between a hosted dashboard and automatically refreshed data.
