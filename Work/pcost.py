# pcost.py
#
# Exercise 1.2
import csv
import sys

def portfolio_cost(filepath):
  total_cost = 0
  with open(filepath, 'rt') as f:
    rows = csv.reader(f)
    headers = next(rows)
    for rowno, row in enumerate(rows):
      record = dict(zip(headers, row))
      try:
        nshares = int(record['shares'])
        price = float(record['price'])
        total_cost += nshares * price
      except ValueError:
        print(f"Row {rowno}: Couldn't parse", repr(row))
  return total_cost

if len(sys.argv) == 2:
  filename = sys.argv[1]
else:
  filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print(f"{cost=}")
