# Methodology and metric definitions

## Evidence boundary

The workbook supplies data. The 17-page PDF supplies an educational objective, field descriptions, and exercises. The 8-page PDF supplies retail dashboard screenshots that do not match the automobile data. No `.pbix`, `.pbit`, Tableau workbook, DAX source, Power Query source, or completed automobile findings report was present in the ZIP.

The repository separates original inputs from new work. A browser dashboard, data checks, and documentation were created during portfolio organization at the requester's direction. No unobserved Power BI modeling, DAX, business impact, or recommendations are attributed to the original project author.

## Preparation performed for this repository

1. Inventory the archive and inspect both PDFs, including rendered pages.
2. Read all 457 records and 16 source columns. Inspect sheet visibility, formulas, comments, hyperlinks, external links, and workbook package features.
3. Preserve the original archive unchanged outside the public repository.
4. Remove `ClientName` from the public CSV and serialize dates as ISO dates. Preserve every remaining value and the original row order.
5. Compare the export with all retained workbook cells and calculate the documented checks independently from the source.
6. Provide a standard-library validator that reproduces the public CSV checks.
7. Build a standalone HTML dashboard from the CSV, with year/country/make filters, grouped charts, summary cards, selected-data export, and a printable snapshot.
8. Add a task-view page that follows the supplied BI-view themes while keeping unsupported measures visibly marked as pending definitions.
9. Test the embedded data and filtered totals against the source workbook. Check empty selections, reset, chart measure switching, exported records, client-name exclusion, task-view KPIs, and mobile layout. Render and visually review the PDF.

No formula cells, hidden worksheets, comments, hyperlinks, workbook external links, or macro/connection/embedded-object package entries were found. This is an inspection result, not a comprehensive security certification.

## Metrics actually reported

| Metric | Definition | Interpretation |
| --- | --- | --- |
| Record count | Number of data rows | Records, not verified unique vehicles or invoices. |
| Recorded sale-price total | Sum of `SalePrice` | Numeric control total in unspecified source units. |
| Average recorded sale price | Sum of `SalePrice` divided by selected record count | Arithmetic mean; unavailable for an empty selection. |
| Grouped value or record count | Sum of `SalePrice` or count of selected rows grouped by year/make/country/type | The chart selector controls aggregation; summary cards retain their stated definitions. |
| Vehicle-type share | Selected type value or count divided by the corresponding selection total | Uses the selected chart metric. |
| Annual recorded sale-price total | Sum of `SalePrice` grouped by `ReportingYear` | Descriptive total; no exchange-rate conversion or discount adjustment. |
| Make/country/type counts | Count of distinct supplied labels | Data coverage only. |
| Missing cells | Count of empty data cells | Original workbook and public export checked separately. |
| Exact duplicate rows | Row count minus distinct full-row count | Original and public export checked separately. |
| Reporting-date mismatch | Invoice year/month differs from reporting year/month | A consistency check, not proof of complete period coverage. |
| Negative delivery charges | Records where `DeliveryCharge < 0` | Review items retained as supplied. |
| Sale price below cost | Records where `SalePrice < CostPrice` | Not a calculation of net loss or margin. |
| Average sales / month | Selection total divided by distinct `ReportingMonth` values present | Descriptive monthly average; no missing-period imputation. |
| Latest-year sales | Selection total for the latest year represented after filtering | A YTD-style card for the supplied period, not current-year live YTD. |
| Trailing 12 months | Sum of the latest 12 chronological `InvoiceDate` months represented | Uses the source's latest 12 months; no future refresh. |
| High-value sales | Sum of rows where `SalePrice >= 100000` | Threshold is a documented portfolio convention, not a supplied business rule. |
| Estimated total cost | `CostPrice + DeliveryCharge + SpareParts + LaborCost` | Assignment expression shown as a proxy; not an approved accounting measure. |

## Assignment requirements that remain unverified

The brief requests time-intelligence measures, rankings, customer metrics, transformations, and multiple chart types. It also references budgets, targets, regions, product categories, a client lookup table, and pipeline stages that are not supplied in the automobile workbook.

Its example total-cost expression is `CostPrice + DeliveryCharge + SpareParts + LaborCost`. That expression is an assignment prompt, not evidence of an implemented measure or an agreed accounting definition. Profit, net revenue, tax, and margin are not reported here because the necessary business definitions are missing.

The brief's exercises to replace `Coupe` with `Convertible`, filter to Jaguar, or remove duplicates by invoice date and make were not applied to the published dataset. They would change the original data and could discard valid records. A business-approved cleaning rule would be needed before treating these exercises as production transformations.

The new dashboard applies the three filters together before aggregation. Its largest-sales table is sorted by `SalePrice` descending, then invoice date, and shows up to eight rows. Export selection includes all selected rows. Displayed figures are rounded, with more precise values available on hover. The Task views tab implements the supported assignment themes from the uploaded BI reference and explicitly leaves sales variance, formal margin, targets, and customer-level views pending a business definition or non-public fields.

The new browser dashboard has been tested. An original Power BI model would still be needed to verify any original DAX measures, relationships, or refresh behavior. The new PDF is a static snapshot of the default, unfiltered selection.
