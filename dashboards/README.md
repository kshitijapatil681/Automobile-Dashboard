# Automobile dashboard

## Open and explore

Download [`index.html`](index.html) and open it in a browser. GitHub displays HTML source rather than executing it; choose **Download raw file** before opening it locally. The file embeds the public dataset and requires no installation, web server, network access, or external libraries.

- Select a reporting year, country, and make. The filters are applied together.
- Switch the charts between recorded sale value and record count. Summary cards retain their own labels and definitions.
- Hover over bars and headline amounts for more precise values.
- Use **Export selection** to download all selected records, including all 15 public columns. It is disabled when the selection is empty.
- Use **Reset filters** to restore the full dataset and default chart measure.
- Use **Print / PDF** for a static snapshot of the current selection.

The largest-sales table shows at most eight selected rows. It is not the full export. On narrow screens the table can scroll horizontally.

## Files

| File | Purpose |
| --- | --- |
| [`index.html`](index.html) | Ready-to-open interactive dashboard |
| [`src/dashboard.html`](src/dashboard.html) | Editable HTML/CSS/JavaScript template with a data placeholder |
| [`screenshots/automobile-overview.png`](screenshots/automobile-overview.png) | Default, unfiltered dashboard preview |
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

Recorded sale value is the sum of `SalePrice`. Average sale price is that sum divided by selected row count. Currency and discount treatment are unspecified. Record count is not a verified count of unique vehicles or invoices.

Browser checks reconciled default totals, individual and combined filters, and all embedded source cells against the original workbook. Empty states, reset, count-mode charts, selected-record export, client-name exclusion, mobile width, and browser errors were checked. The PDF was rendered and visually inspected. Data-quality observations remain visible rather than being silently corrected. See [methodology](../docs/methodology.md) for definitions.
