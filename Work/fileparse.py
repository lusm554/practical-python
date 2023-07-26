# fileparse.py
#
# Exercise 3.3
import csv

def parse_csv(filename: str, select: list = None, types: list = None, has_headers: bool = True, delimiter: str = ',') -> list[dict]:
  """
  Parse a CSV files into a list of records.
  """
  with open(filename, 'rt') as f:
    rows = csv.reader(f, delimiter=delimiter)
    header = next(rows) if has_headers else []
    if select:
      indices = [header.index(colname) for colname in select]
      header = select
    records = []
    for row in rows:
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
  return records

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
