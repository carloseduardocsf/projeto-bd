import sqlite3

conn = sqlite3.connect('./bd/data.db')

sql = ''
with open('bd/create_table.sql') as file:
    sql = file.read()

cs = conn.cursor()
cs.executescript(sql)

with open('bd/dump.sql') as file:
    sql = file.read()

cs.executescript(sql)

conn.commit()

conn.close()