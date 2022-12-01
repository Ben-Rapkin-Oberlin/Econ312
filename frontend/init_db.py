import sqlite3
import csv

connection = sqlite3.connect('database.db')

#with open('schema.sql') as f:
 #   connection.executescript(f.read())

cur = connection.cursor()



file = open('monks1.csv')
contents = csv.reader(file)
insert_records = "INSERT INTO monks1 (label, head_shape,body_shape,is_smiling,holding,jacket_color,has_tie) VALUES(?, ?,?,?,?,?,?)"
cur.executemany(insert_records, contents)

connection.commit()
connection.close()
