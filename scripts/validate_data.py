"""Reproduce checks for the supplied automobile snapshot (standard library only).

Added during repository preparation; not part of the original project submission.
Run from any directory: python path/to/scripts/validate_data.py
"""

import csv
import json
from collections import Counter, defaultdict
from datetime import date
from decimal import Decimal
from pathlib import Path


FIELDS = [
    'InvoiceDate', 'Make', 'CountryName', 'SalePrice', 'CostPrice',
    'TotalDiscount', 'DeliveryCharge', 'SpareParts', 'LaborCost',
    'Model', 'Color', 'ReportingYear', 'ReportingMonth',
    'Registration_Date', 'VehicleType',
]
AMOUNTS = ['SalePrice', 'CostPrice', 'TotalDiscount', 'DeliveryCharge', 'SpareParts', 'LaborCost']
EXPECTED_TOTALS = {
    'SalePrice': Decimal('31697940'), 'CostPrice': Decimal('20409895'),
    'TotalDiscount': Decimal('225295.02'), 'DeliveryCharge': Decimal('239970'),
    'SpareParts': Decimal('495060'), 'LaborCost': Decimal('310498'),
}


def main():
    path = Path(__file__).resolve().parents[1] / 'data/processed/automobile_sales.csv'
    with path.open(encoding='utf-8', newline='') as stream:
        reader = csv.DictReader(stream)
        if reader.fieldnames != FIELDS:
            raise ValueError('Unexpected public schema; check excluded fields and column order.')
        rows = list(reader)
    if not rows or any(None in r or None in r.values() for r in rows):
        raise ValueError('Empty dataset or malformed CSV record.')

    totals = {key: Decimal('0') for key in AMOUNTS}
    annual_count = Counter()
    annual_sales = defaultdict(lambda: Decimal('0'))
    dates = []
    mismatch = negative_delivery = below_cost = 0
    for row in rows:
        invoice = date.fromisoformat(row['InvoiceDate'])
        date.fromisoformat(row['Registration_Date'])
        dates.append(invoice)
        year, month = int(row['ReportingYear']), int(row['ReportingMonth'])
        mismatch += (invoice.year, invoice.month) != (year, month)
        values = {key: Decimal(row[key]) for key in AMOUNTS}
        if not all(value.is_finite() for value in values.values()):
            raise ValueError('Non-finite numeric value.')
        for key, value in values.items():
            totals[key] += value
        annual_count[year] += 1
        annual_sales[year] += values['SalePrice']
        negative_delivery += values['DeliveryCharge'] < 0
        below_cost += values['SalePrice'] < values['CostPrice']

    metrics = {
        'records': len(rows), 'columns': len(FIELDS),
        'blank_cells': sum(v == '' for row in rows for v in row.values()),
        'exact_duplicate_public_rows': len(rows) - len({tuple(r[k] for k in FIELDS) for r in rows}),
        'invoice_date_min': min(dates).isoformat(), 'invoice_date_max': max(dates).isoformat(),
        'makes': len({r['Make'] for r in rows}), 'countries': len({r['CountryName'] for r in rows}),
        'vehicle_types': len({r['VehicleType'] for r in rows}),
        'reporting_date_mismatches': mismatch,
        'negative_delivery_charges': negative_delivery, 'sale_price_below_cost_price': below_cost,
        'repeated_invoice_date_make_pairs': len(rows) - len({(r['InvoiceDate'], r['Make']) for r in rows}),
    }
    expected = {
        'records': 457, 'columns': 15, 'blank_cells': 0, 'exact_duplicate_public_rows': 0,
        'invoice_date_min': '2012-01-01', 'invoice_date_max': '2015-12-02',
        'makes': 7, 'countries': 6, 'vehicle_types': 3, 'reporting_date_mismatches': 0,
        'negative_delivery_charges': 44, 'sale_price_below_cost_price': 87,
        'repeated_invoice_date_make_pairs': 194,
    }
    errors = [f'{key}: expected {value}, got {metrics[key]}' for key, value in expected.items() if metrics[key] != value]
    errors += [f'{key} total differs from source control' for key, value in EXPECTED_TOTALS.items() if totals[key] != value]
    if dict(annual_count) != {2012: 39, 2013: 115, 2014: 77, 2015: 226}:
        errors.append('Annual record counts differ from source controls.')
    if dict(annual_sales) != {2012: Decimal('3185500'), 2013: Decimal('7158710'), 2014: Decimal('6386440'), 2015: Decimal('14967290')}:
        errors.append('Annual sale-price totals differ from source controls.')
    print(json.dumps({
        'checks': metrics, 'amount_control_totals': {k: str(v) for k, v in totals.items()},
        'annual': [{ 'year': y, 'records': annual_count[y], 'sale_price_total': str(annual_sales[y]) } for y in sorted(annual_count)],
        'status': 'SOURCE SNAPSHOT MATCHES' if not errors else 'REVIEW REQUIRED', 'errors': errors,
    }, indent=2))
    if errors:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
