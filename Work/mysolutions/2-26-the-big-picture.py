import csv
from pprint import pprint

def simp_version():
  f = open('../Data/dowstocks.csv')
  rows = csv.reader(f)
  header = next(rows)
  types = [str, float, str, str, float, float, float, float, int]
  converted = [ { name: cast2(val) for name, val, cast2 in zip(header, row, types) } for row in rows ]
  print('simple version:') 
  pprint(converted[:1])
simp_version()

# Bonus: How would you modify this example to additionally parse the date entry into a tuple such as (6, 11, 2007)?
def harder_version():
  f = open('../Data/dowstocks.csv')
  rows = csv.reader(f)
  header = next(rows)
  date_type = lambda d: tuple(d.split('/')) # if int types needed: tuple(map(int, d.split('/')))
  types = [str, float, date_type, str, float, float, float, float, int]
  converted = [ { name: cast2(val) for name, val, cast2 in zip(header, row, types) } for row in rows ]
  print('harder version:')
  pprint(converted[:1])
harder_version()
