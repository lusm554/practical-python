# fileparse.py
#
# Exercise 3.3
import csv

def parse_csv(filename: str) -> list[dict]:
  """
  Parse a CSV files into a list of records.
  """
  with open(filename, 'rt') as f:
    rows = csv.reader(f)
    header = next(rows)
    records = []
    for row in rows:
      if not row: continue # skip empty rows
      record = dict(zip(header, row))
      records.append(record)
  return records
