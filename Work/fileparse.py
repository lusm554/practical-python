# fileparse.py
#
# Exercise 3.3
import csv

def parse_csv(
  sourceobj: [str, list],
  select: list = None,
  types: list = None,
  has_headers: bool = True,
  delimiter: str = ',',
  silence_errors: bool = False
) -> list[dict]:
  """
  Parse a CSV files into a list of records.
  """
  if select is not None and has_headers == False:
    raise RuntimeError('select argument requires column headers')
  if isinstance(sourceobj, str):
    with open(sourceobj, 'rt') as f:
      lines = [row for row in f]
  else:
    lines = sourceobj
  rows = csv.reader(lines, delimiter=delimiter)
  header = next(rows) if has_headers else []
  if select:
    indices = [header.index(colname) for colname in select]
    header = select
  records = []
  for rowno, row in enumerate(rows):
    try:
      if not row: continue # skip empty rows
      if select:
        row = [row[index] for index in indices]
      if types:
        row = [cast(val) for val, cast in zip(row, types)]
      if has_headers:
        record = dict(zip(header, row))
      else:
        record = tuple(row)
      records.append(record)
    except ValueError as error:
      if not silence_errors:
        print(f"Row {rowno}: Couldn't convert {row}")
        print(f"Row {rowno}: Reason {error}")
  return records

if __name__ == '__main__':
  # TEST CASE
  from pprint import pprint
  p = parse_csv('Data/portfolio.csv')
  pprint(p)

  p = parse_csv('Data/portfolio.csv', select=['name', 'price'])
  pprint(p)

  # it's good idea for handle this exception, but course leads the other way 
  #p = parse_csv('Data/portfolio.csv', select=['name', 'price'], types=[str, int, float])
  #pprint(p)

  p = parse_csv('Data/portfolio.csv', types=[str, int, float])
  pprint(p)

  p = parse_csv('Data/prices.csv', types=[str,float], has_headers=False)
  pprint(p)

  p = parse_csv('Data/portfolio.dat', types=[str, int, float], delimiter=' ')
  pprint(p)
