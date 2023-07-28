class TableFormatter:
  def headings(self, headers):
    """
    Emit the table headings.
    """
    raise NotImplementedError()

  def row(self, rowdata):
    """
    Emit a single row of table data.
    """
    raise NotImplementedError()


class TextTableFormatter(TableFormatter):
  """
  Emit a table in plain-text format.
  """
  def headings(self, headers):
    for h in headers:
      print(f'{h:>10s}', end=' ')
    print()
    print(('-'*10 + ' ')*len(headers))

  def row(self, rowdata):
    for d in rowdata:
      print(f'{d:>10s}', end=' ')
    print()


class CSVTableFormatter(TableFormatter):
  """
  Emit a table in CSV format.
  """
  def headings(self, headers):
    print(','.join(headers))

  def row(self, rowdata):
    print(','.join(rowdata))


class HTMLTableFormatter(TableFormatter):
  """
  Emit a table in HTML format.
  """
  def headings(self, headers):
    cols = "".join([f"<tr>{h}</th>" for h in headers])
    print(f"<tr>{cols}</tr>")

  def row(self, rowdata):
    rows = "".join([f"<tr>{r}</th>" for r in rowdata])
    print(f"<tr>{rows}</tr>")


def create_formatter(fmt):
  if fmt == 'txt':
    formatter = TextTableFormatter()
  elif fmt == 'csv':
    formatter = CSVTableFormatter()
  elif fmt == 'html':
    formatter = HTMLTableFormatter()
  else:
    raise RuntimeError(f"Unknown format {fmt}")
  return formatter

def print_table(portfolio, attrs, formatter):
  formatter.headings(attrs)
  for p in portfolio:
    rowdata = [ str(getattr(p, attr)) for attr in attrs ]
    formatter.row(rowdata)
