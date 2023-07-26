# report.py
#
# Exercise 2.4
import csv
from pprint import pprint

def read_portfolio(filename):
  portfolio = []
  with open(filename, 'rt') as f:
    rows = csv.reader(f)
    header = next(rows)
    for row in rows:
      record = dict(zip(header, row)) 
      record['shares'] = int(record['shares']) 
      record['price'] = float(record['price']) 
      portfolio.append(record)
  return portfolio


def read_prices(filename):
  prices = {}
  with open(filename, 'rt') as f:
    rows = csv.reader(f)
    for row in rows:
      try:
        name, price = row
        prices[name] = float(price)
      except ValueError:
        pass
        #print('Couldn\'t parse', row)
  return prices


def make_report(portfolio, prices):
  report = []
  for p in portfolio:
    name, shares = p['name'], p['shares']
    price = prices[name]
    change = round(price - p['price'], 2)
    row = (name, shares, price, change)
    report.append(row)
  return report

prices = read_prices('Data/prices.csv')
portfolio = read_portfolio('Data/portfolio.csv')
report = make_report(portfolio, prices)

headers = ('Name', 'Shares', 'Price', 'Change')
separator = ('-' * 10,) * 4
print('%10s %10s %10s %10s' % headers)
print('%s %s %s %s' % separator)

for name, shares, price, change in report:
  print('%10s %10d %10s %10.2f' % (name, shares, ("$%.2f" % price), change))

