# report.py
#
# Exercise 2.4
from pprint import pprint
import fileparse
import stock
import tableformat


def read_portfolio(filename):
  portfolio = [ stock.Stock(*p.values()) for p in fileparse.parse_csv(filename, types=[str, int, float]) ]
  return portfolio

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
  """
  separator = ('-' * 10,) * 4
  print('%10s %10s %10s %10s' % headers)
  print('%s %s %s %s' % separator)
  """
  for name, shares, price, change in report:
    #print('%10s %10d %10s %10.2f' % (name, shares, ("$%.2f" % price), change))
    rowdata = [ name, str(shares), f'{price:0.2f}', f'{change:0.2f}' ]
    formatter.row(rowdata)

def portfolio_report(portfoliofile, pricesfile):
  portfolio = read_portfolio(portfoliofile)
  prices = read_prices(pricesfile)
  report = make_report(portfolio, prices)
  formatter = tableformat.TableFormatter()
  print_report(report, formatter)

def main(argv):
  #portfolio_report('Data/portfolio.csv', 'Data/prices.csv')
  scriptname, portf, prices = argv
  portfolio_report(portf, prices)

if __name__ == '__main__':
  import sys
  main(sys.argv)
