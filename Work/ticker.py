# ticker.py

from follow import follow
import csv

def select_columns(rows, indices):
  for row in rows:
    yield [row[index] for index in indices]

def convert_types(rows, types):
  for row in rows:
    yield [cast(val) for cast, val in zip(types, row)]

def make_dicts(rows, headers):
  for row in rows:
    yield dict(zip(headers, row))

def parse_stock_data(lines):
  rows = csv.reader(lines)
  rows = select_columns(rows, [0, 1, 4])
  rows = convert_types(rows, [str, float, float])
  rows = make_dicts(rows, ['name', 'price', 'change'])
  return rows

if __name__ == '__main__':
  lines = follow('Data/stocklog.csv')
  rows = parse_stock_data(lines)
  for row in rows:
    print(row)
