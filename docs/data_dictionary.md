# Data dictionary

The supplied assignment brief describes the fields on pages 2-7. Types and coverage below were checked against the workbook's `Automobile` worksheet. Each row appears to represent a vehicle sale record; no invoice ID or vehicle identifier is supplied, so unique transactions or vehicles cannot be established independently.

| Field | CSV type | Meaning and limits |
| --- | --- | --- |
| `InvoiceDate` | Date | Sale invoice date; 2012-01-01 through 2015-12-02. |
| `Make` | Text | Manufacturer/brand; 7 distinct values. |
| `CountryName` | Text | Country of sale according to the brief; 6 distinct values. It does not identify a currency. |
| `SalePrice` | Decimal | Recorded sale price. Currency and treatment of discounts/tax are unspecified. |
| `CostPrice` | Decimal | Recorded vehicle cost price; not necessarily the full cost of sale. |
| `TotalDiscount` | Decimal | Recorded discount amount. Whether already included in `SalePrice` is unspecified. |
| `DeliveryCharge` | Decimal | Recorded delivery charge. Includes 44 negative entries; accounting treatment is unverified. |
| `SpareParts` | Decimal | Recorded cost of spare parts associated with the sale. |
| `LaborCost` | Decimal | Recorded labor cost. The brief's illustrative value differs from the first workbook record; the workbook is used for all calculations. |
| `Model` | Text | Vehicle model label. |
| `Color` | Text | Recorded vehicle color. |
| `ReportingYear` | Integer | Reporting year, 2012-2015; matches the invoice year in every supplied record. |
| `ReportingMonth` | Integer | Reporting month, 1-12; matches the invoice month in every supplied record. |
| `Registration_Date` | Date | Vehicle registration date; distinct from the invoice/reporting date. |
| `VehicleType` | Text | `Coupe`, `Saloon`, or `Convertible`, preserved as supplied. |

## Excluded source field

`ClientName` is text in source column J. Its values are not published. The public CSV cannot reproduce distinct-customer counts, customer rankings, or customer joins. No customer IDs or name mappings are supplied.

## Missing definitions

The workbook has no currency, tax, quantity, budget, target, sales pipeline, region, or product-category field. Do not equate country with region, make with category, or row count with verified unique vehicles without documenting and justifying that separate modeling decision.
