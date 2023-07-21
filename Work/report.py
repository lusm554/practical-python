# report.py
#
# Exercise 2.4
import csv

def read_portfolio(filename):
  portfolio = []
  with open(filename, 'rt') as f:
    rows = csv.reader(f)
    header = next(rows)
    for row in rows:
      curr_share = (row[0], int(row[1]), float(row[2]))
      portfolio.append(curr_share)
  return portfolio
