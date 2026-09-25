"""Build the offline dashboard from the published CSV, without dependencies."""

import csv
import json
from pathlib import Path


def main():
    root = Path(__file__).resolve().parents[1]
    with (root / 'data/processed/automobile_sales.csv').open(encoding='utf-8', newline='') as f:
        reader = csv.DictReader(f)
        if 'ClientName' in reader.fieldnames:
            raise ValueError('Remove the client-name field before building a public dashboard.')
        rows = list(reader)
    if not rows:
        raise ValueError('The dashboard needs source records.')
    template = (root / 'dashboards/src/dashboard.html').read_text(encoding='utf-8')
    if template.count('__SOURCE_DATA__') != 1:
        raise ValueError('Expected exactly one data insertion point.')
    payload = json.dumps(rows, ensure_ascii=True, separators=(',', ':')).replace('<', '\\u003c')
    output = root / 'dashboards/index.html'
    with output.open('w', encoding='utf-8', newline='\n') as stream:
        stream.write(template.replace('__SOURCE_DATA__', payload))
    print(f'Built standalone dashboard with {len(rows)} records.')


if __name__ == '__main__':
    main()
