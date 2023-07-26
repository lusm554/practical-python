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
      try:
        total_cost += int(row[1]) * float(row[2])
      except ValueError:
        print(f"Row {rowno}: Couldn't parse", repr(row))
  return total_cost

if len(sys.argv) == 2:
  filename = sys.argv[1]
else:
  filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print(f"{cost=}")
