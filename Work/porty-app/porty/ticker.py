# ticker.py

from .follow import follow
from . import report
import csv
from . import tableformat

def select_columns(rows, indices):
  for row in rows:
    yield [row[index] for index in indices]

def convert_types(rows, types):
  for row in rows:
    yield [cast(val) for cast, val in zip(types, row)]

def make_dicts(rows, headers):
  for row in rows:
    yield dict(zip(headers, row))

def filter_symbols(rows, names):
  return (row for row in rows if row['name'] in names)

def parse_stock_data(lines):
  rows = csv.reader(lines)
  rows = select_columns(rows, [0, 1, 4])
  rows = convert_types(rows, [str, float, float])
  rows = make_dicts(rows, ['name', 'price', 'change'])
  return rows

def ticker(portfile, logfile, fmt):
  portfolio = report.read_portfolio(portfile)
  lines = follow('Data/stocklog.csv')
  rows = parse_stock_data(lines)
  rows = filter_symbols(rows, portfolio)
  formatter = tableformat.create_formatter(fmt)
  formatter.headings(['Name', 'Prices', 'Change'])
  for row in rows:
    formatter.row([ row['name'], f"{row['price']:0.2f}", f"{row['change']:0.2f}"] )
  
def main(argv):
  if len(argv) < 4:
    raise SystemExit('Usage: %s portfoliofile logfile fmt' % argv[0])
  ticker(*argv[1:])

if __name__ == '__main__':
  import sys
  main(sys.argv)
