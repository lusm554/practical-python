import os
import time

def follow(filepath):
  with open(filepath) as f:
    f.seek(0, os.SEEK_END)
    while True:
      line = f.readline()
      if line == '':
        time.sleep(.1)
        continue
      yield line

if __name__ == '__main__':
  import report

  portfolio = report.read_portfolio('Data/portfolio.csv')
  for line in follow('Data/stocklog.csv'):
    fields = line.split(',')
    name, price, change = fields[0].strip('"'), float(fields[1]), float(fields[4])
    if name in portfolio:
      print(f'{name:>10s} {price:>10.2f} {change:>10.2f}')

