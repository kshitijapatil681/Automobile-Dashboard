# Data provenance and handling

## Public file

[`processed/automobile_sales.csv`](processed/automobile_sales.csv) is a UTF-8 CSV derived from the `Automobile` worksheet in `Automobile _Project_Dashboard_Datasets.xlsx`.

- Source range: `Automobile!A1:P458`, including the header row.
- Source: 457 records, 16 columns, one visible worksheet.
- Public export: 457 records, 15 columns. The original `ClientName` column is removed in full, without a lookup table or replacement identifiers.
- Source row order, remaining field names, and remaining values are preserved. Dates use `YYYY-MM-DD`; numbers use decimal points without grouping separators. No index column is added.
- No records are filtered, deduplicated, imputed, or corrected. Negative delivery charges remain in place.
- The export was compared cell by cell with the retained source columns. All 457 rows matched after the documented date/number serialization.

Removing client names reduces direct disclosure but does not establish that all records are anonymous or synthetic. No claim that this is a public benchmark dataset has been verified.

## Original sources

The unchanged workbook is retained in the local original-source bundle, outside Git. It is excluded from the public repository because it contains client names. The ZIP and original PDFs are also retained locally; their roles are described in the [source audit](../docs/source_audit.md).

The public CSV is sufficient to reproduce the published aggregate checks. The original workbook is necessary to verify the excluded client field and the source checksum. No source URL, currency, invoice identifier, or explicit statement about whether the records are real or synthetic was supplied.

## Reading and updating

Use the [data dictionary](../docs/data_dictionary.md) for field types and interpretation. Do not use `InvoiceDate` plus `Make` as a unique identifier: 194 rows repeat an already observed combination, even though there are no exact duplicate source rows.

For a replacement export, remove `ClientName` before saving, preserve all other values and row order, and record the new source checksum and coverage. Run `python scripts/validate_data.py` from the repository root and review any changed control totals. The current script deliberately checks the supplied snapshot; a changed dataset requires a documented baseline update.
