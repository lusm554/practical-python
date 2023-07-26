# fileparse.py
#
# Exercise 3.3
import csv

def parse_csv(filename: str, select: bool=False) -> list[dict]:
  """
  Parse a CSV files into a list of records.
  """
  with open(filename, 'rt') as f:
    rows = csv.reader(f)
    header = next(rows)
    if select:
      indices = [header.index(colname) for colname in select]
    else:
      indices = []
    records = []
    for row in rows:
      if not row: continue # skip empty rows
      if indices:
        row = [row[index] for index in indices]
      record = dict(zip(header, row))
      records.append(record)
  return records
