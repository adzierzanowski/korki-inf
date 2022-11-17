import re
import os
import sqlite3

class DB:
  def __init__(self, dbname=None):
    if dbname and os.path.exists(dbname):
      os.remove(dbname)
    self.dbname = dbname
    self.con = None

  def __enter__(self):
    self.con = sqlite3.connect(self.dbname or ':memory:')
    return self

  def __exit__(self, *args):
    self.con.close()
    if self.dbname:
      print(f"Connection to '{self.dbname}' closed.")
    else:
      print(f"Connection to in-memory database closed.")

  def create_table_from_file(self, table_name, path, sep='\t'):
    with open(path, 'r') as f:
      cur = self.con.cursor()
      data = [line.strip().split(sep) for line in f.readlines()]

      header = data[0]
      header = []
      for name, val in zip(data[0], data[1]):
        try:
          int(val)
          header.append(f'{name} integer')
        except ValueError:
          header.append(name)

      rows = data[1:]

      q = f'CREATE TABLE {table_name}({", ".join(header)})'
      print(q)

      cur.execute(q)
      for row in rows:
        r = [f"'{val}'" for val in row]
        cur.execute(f'INSERT INTO {table_name} VALUES({", ".join(r)})')
      self.con.commit()

  def query(self, q):
    cur = self.con.cursor()

    # Convert SQLITE syntax to MS ACCESS syntax
    # LIMIT -> SELECT TOP
    select_top = re.findall(r'select top (\d+)', q, re.IGNORECASE)
    if select_top:
      q = re.sub(r'select top \d+', 'SELECT', q, flags=re.IGNORECASE)
      q += f' LIMIT {select_top[0]}'

    # LIKE 'X*' -> LIKE 'X%'
    q = ' '.join(
      [s.replace('*', '%') if 'LIKE' in s.upper() else s
       for s
       in re.split(r'''(LIKE ['"].*['"])''', q, flags=re.I)])

    # DateDiff -> Unixepoch
    q = re.sub(
      r'DateDiff\(.*?, ?(.*?), ?(.*?)\)',
      r'Abs(Unixepoch(\1) - Unixepoch(\2))',
      q,
      flags=re.IGNORECASE)

    # & -> ||
    q = q.replace('&', '||')

    #print('Result of\n\t', q.strip())
    res = cur.execute(q)
    self.con.commit()
    rows = res.fetchall()

    if rows:
      print('='*40)
      if res.description:
        print(''.join(f'| {r[0]:20}' for r in res.description) + '|')
        print(('|' + '-'*21) * len(res.description) + '|')

    for row in rows:
      print(''.join(f'| {val:<20}' if val is not None else f'{"NULL":20}'
                    for val in row) + '|')

    if res.description and rows:
      print(('|' + '-'*21) * len(res.description) + '|')
      print(''.join(f'| {r[0]:20}' for r in res.description) + '|')

    print(f'{len(rows)} row(s) affected')
    if rows:
      print('='*40)
