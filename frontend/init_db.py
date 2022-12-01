import sqlite3
import csv

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
   connection.executescript(f.read())

cur = connection.cursor()

format=""
vals="VALUES("
fordatabase=""
with open('AllData\\mergedData\\semi-final\\NVDA_SOXX.csv') as f:
  reader = csv.reader(f)
  row1 = next(reader)
  for col in row1:
    format=format+col+", "
    fordatabase=fordatabase+col+" TEXT NOT NULL,\n"
    vals=vals+"?,"
format='('+format[:-2]+') '
vals=vals[:-1]+')'
#print(fordatabase[:-2])
#print(format+vals)

file = open('AllData\\mergedData\\semi-final\\NVDA_SOXX.csv')

contents = csv.reader(file)


insert_records = "INSERT INTO fin"+ format+vals
cur.executemany(insert_records, contents)

connection.commit()
connection.close()
