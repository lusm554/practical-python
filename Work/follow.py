import os
import time

f = open("Data/stocklog.csv")
f.seek(0, os.SEEK_END)

while True:
  line = f.readline()
  if line == '':
    time.sleep(.1)
    continue
  fields = line.split(',')
  name, price, change = fields[0].strip(), float(fields[1]), float(fields[4])
  if change < 0:
    print(f'{name:>10s} {price:>10.2f} {change:>10.2f}')
