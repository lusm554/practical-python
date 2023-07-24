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
      #curr_share = (row[0], int(row[1]), float(row[2]))
      curr_share = {
        'name': row[0],
        'shares': int(row[1]),
        'price': float(row[2]),
      }
      portfolio.append(curr_share)
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
        print('Couldn\'t parse', row)
  return prices

prices = read_prices('Data/prices.csv')
pprint(prices)
portfolio = read_portfolio('Data/portfolio.csv')
pprint(portfolio)

total_cost = 0.0
current_cost = 0.0
for p in portfolio:
  total_cost += p['price'] * p['shares']
  current_cost += p['shares'] * prices[p['name']]
print(f"{total_cost=}")
print(f"{current_cost=}")
print("Gain", current_cost - total_cost)
