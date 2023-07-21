# pcost.py
#
# Exercise 1.2
import csv

def portfolio_cost(filepath):
  total_cost = 0
  with open(filepath, 'rt') as f:
    rows = csv.reader(f)
    headers = next(rows)
    for row in rows:
      try:
        total_cost += int(row[1]) * float(row[2])
      except ValueError:
        print("Couldn't parse", repr(row))
  return total_cost

cost = portfolio_cost('Data/portfolio.csv')
print(f"{cost=}")
