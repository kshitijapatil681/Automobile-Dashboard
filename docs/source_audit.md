# Source audit

Audit date: 26 September 2026.

## Repository baseline

The repository initially contained only `README.md` and `LICENSE`, at commit `dec7cfde0f67e86122ed2c270019069641e38d09` on `main`. The MIT license is preserved unchanged. Changes are proposed on a separate branch through a pull request.

## Supplied archive

`Automobile Dashboard.zip` contained three files under `Automobile Dashboard/`:

| Original file | Size (bytes) | Inspected content | Public handling |
| --- | ---: | --- | --- |
| `Automobile _Project_Dashboard_Datasets.xlsx` | 49,000 | One sheet, 457 automobile records, 16 columns | Publish only a CSV with `ClientName` removed. Preserve original locally. |
| `Automobile Dashboard Analysis.pdf` | 890,467 | 8 pages of retail sales dashboards | Exclude: unrelated to the automobile workbook and includes customer names. Preserve original locally. |
| `Project-3(Automobile Dashboard Analysis).pdf` | 556,294 | 17-page CoachX-branded assignment brief | Document as reference material; preserve original locally. Do not present it as completed project work. |

The local original-source bundle preserves all three files unchanged. Local filesystem paths and client values are not included in this repository.

### Original SHA-256 checksums

```text
a47009e8123bf170c6f2f54f857f24e6759ef32c612787e860a24237fbe6b7e7  Automobile _Project_Dashboard_Datasets.xlsx
2568c38c72436a131af7d08b5ac4dbce9c481dc366567f2bdcd172d8b48c0139  Automobile Dashboard Analysis.pdf
5ef2e6d60e2d97f9764b072e77d2a69bcef89c1462086be4e03a2c534862cabc  Project-3(Automobile Dashboard Analysis).pdf
```

## Why the dashboard is excluded

All eight pages refer to retail fields such as `Sales`, `Profit`, `Category`, `Ship Mode`, or `Order ID`, with furniture, office supplies, and technology categories. The automobile workbook instead contains makes, models, countries, `SalePrice`, and vehicle costs. The retail export includes 2016-2019 labels, whereas automobile invoices span 2012-2015. There is no supplied mapping or matching retail source dataset.

Several retail pages include customer names, and page 2 shows a disabled map visual. Neither that export nor its numbers or screenshots are used as evidence of automobile findings.

## Evidence map for the assignment brief

| Pages | Role |
| --- | --- |
| 1 | Educational cover and branding |
| 2-7 | Objective and source-field descriptions |
| 8-10 | DAX exercises |
| 11-12 | Data-transformation exercises |
| 13-14 | Visualization exercises |
| 15-16 | Requested documentation and submission format |
| 17 | Closing page |

These pages contain prompts, not submitted answers. The portfolio therefore does not claim those exercises have been implemented.

## New deliverables

At the requester's direction, an automobile dashboard was created from the inspected workbook after the mismatch was identified. The HTML dashboard, source template, screenshot, and PDF export are new work, as are the validation and build scripts. They do not reuse retail figures or claim to be the original Power BI model.

## Remaining source clarifications

- An original automobile Power BI model would be needed only to verify or extend the original Power BI work; the new browser dashboard operates independently.
- Currency and discount treatment, plus the interpretation of negative delivery charges.
- Dataset provenance and any applicable dataset redistribution terms.

The current data findings remain reproducible without those items, within the limits described in [methodology](methodology.md).
