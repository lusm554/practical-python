# pcost.py
#
# Exercise 1.2
import sys
import csv 
import report

def portfolio_cost(filepath):
  prices = report.read_portfolio(filepath)
  total_cost = sum([ p['shares'] * p['price'] for p in prices ])
  return total_cost

if len(sys.argv) == 2:
  filename = sys.argv[1]
else:
  filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print(f"{cost=}")
