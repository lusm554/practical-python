# report.py
#
# Exercise 2.4
from pprint import pprint
import fileparse
import stock
import tableformat
from portfolio import Portfolio


def read_portfolio(filename):
  portfolio = [ stock.Stock(**p) for p in fileparse.parse_csv(filename, types=[str, int, float]) ]
  return Portfolio(portfolio)

def read_prices(filename):
  prices = dict(fileparse.parse_csv(filename, types=[str, float], has_headers=False))
  return prices

def make_report(portfolio, prices):
  report = []
  for p in portfolio:
    name, shares = p.name, p.shares 
    price = prices[name]
    change = round(price - p.price, 2)
    row = (name, shares, price, change)
    report.append(row)
  return report

def print_report(report, formatter):
  formatter.headings(('Name', 'Shares', 'Price', 'Change'))
  for name, shares, price, change in report:
    rowdata = [ name, str(shares), f'{price:0.2f}', f'{change:0.2f}' ]
    formatter.row(rowdata)

def portfolio_report(portfoliofile, pricesfile, fmt='txt'):
  portfolio = read_portfolio(portfoliofile)
  prices = read_prices(pricesfile)
  report = make_report(portfolio, prices)
  formatter = tableformat.create_formatter(fmt)
  print_report(report, formatter)

def main(argv):
  #portfolio_report('Data/portfolio.csv', 'Data/prices.csv')
  scriptname, portf, prices, fmt = argv
  portfolio_report(portf, prices, fmt)

if __name__ == '__main__':
  import sys
  main(sys.argv)
