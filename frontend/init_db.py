import sqlite3
import csv
from pathlib import Path, PureWindowsPath

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
  connection.executescript(f.read())

cur = connection.cursor()

format=""
vals="VALUES("
fordatabase=""

filename = PureWindowsPath('NVDA_SOXX_BTC.csv')
correct_path = Path(filename)
with open(correct_path) as f:
  reader = csv.reader(f)
  row1 = next(reader)
  for col in row1:
    format=format+col+", "
    fordatabase=fordatabase+col+" DECIMAL(5,5),\n"
    vals=vals+"?,"
format='('+format[:-2]+') '
vals=vals[:-1]+')'
#print(fordatabase[:-2])
#print(format+vals)

#filename = PureWindowsPath('NVDA_SOXX_BTC.csv')
#correct_path = Path(filename)
file=open(correct_path)
contents = csv.reader(file)


insert_records = "INSERT INTO fin"+ format+vals
cur.executemany(insert_records, contents)

connection.commit()
connection.close()
