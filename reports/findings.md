# Verified dataset findings

These are checks calculated during repository preparation from the supplied automobile workbook. They are not extracted from the unrelated retail dashboard and are not presented as a completed business-impact study.

## Coverage and control totals

The source range `Automobile!A1:P458` contains 457 data records, 7 makes, 6 countries, and 3 vehicle types. Invoice dates range from 2012-01-01 to 2015-12-02. All reporting year/month values agree with the invoice date.

| Reporting year | Records | Sum of `SalePrice` |
| --- | ---: | ---: |
| 2012 | 39 | 3,185,500 |
| 2013 | 115 | 7,158,710 |
| 2014 | 77 | 6,386,440 |
| 2015 | 226 | 14,967,290 |
| **Total** | **457** | **31,697,940** |

2015 has the highest recorded annual sale-price total and the most records in the supplied file. Coverage differs by year, and no complete-market or complete-period guarantee is supplied. The figures do not establish market growth, business performance, or causal drivers. Currency is not specified, so these totals should not be interpreted as revenue in a verified common currency.

## Data quality observations

| Check | Result | Treatment |
| --- | ---: | --- |
| Empty source cells | 0 | No imputation performed. |
| Exact duplicate source rows | 0 | No records removed. |
| Reporting-date mismatches | 0 | Reporting fields retained. |
| Negative `DeliveryCharge` entries | 44 | Preserve and seek business explanation. |
| `SalePrice < CostPrice` | 87 | Preserve; no automatic correction or net-loss label. |
| Repeated `(InvoiceDate, Make)` combinations after the first occurrence | 194 | Do not use this pair as a unique key. |

Negative delivery values range down to -75. They could represent adjustments, credits, or errors; the source does not establish which. Similarly, sale price below cost does not by itself establish net profitability, because the accounting treatment of other amounts is unverified.

## What can be concluded

The workbook supports descriptive comparisons of recorded values by year, make, model, country, color, and vehicle type. It also identifies concrete data-definition questions to resolve before a financial dashboard is finalized.

The supplied files do not support claims about achieved sales improvements, forecast accuracy, inventory savings, customer strategy outcomes, or completed original automobile dashboard interactions. The new browser dashboard implements filtering and descriptive charts from the verified dataset. Customer-level analysis is additionally excluded from the public export because `ClientName` has been removed.

Reproduce the published counts and control totals with `python scripts/validate_data.py`. See [methodology](../docs/methodology.md) for definitions and [dashboard notes](../dashboards/README.md) for usage and the distinction between new and original work.
