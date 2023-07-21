# pcost.py
#
# Exercise 1.2

def portfolio_cost(filepath):
  total_cost = 0
  with open(filepath, 'rt') as f:
    headers = next(f).strip().split(',')
    #print(headers)
    for line in f:
      row = line.strip().split(',')
      #print(row)
      total_cost += int(row[1]) * float(row[2])
  return total_cost

cost = portfolio_cost('Data/portfolio.csv')
print(f"{cost=}")
