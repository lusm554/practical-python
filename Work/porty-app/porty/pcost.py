# pcost.py
#
# Exercise 1.2
import sys
import csv 
from . import report

def portfolio_cost(filepath):
  portfolio = report.read_portfolio(filepath)
  return portfolio.total_cost

if len(sys.argv) == 2:
  filename = sys.argv[1]
else:
  filename = 'Data/portfolio.csv'

def main(argv):
  scriptname, portf = argv
  cost = portfolio_cost(portf)
  print(f"Total cost: {cost}")

if __name__ == '__main__':
  main(sys.argv)
