import sqlite3
import psycopg2

# conn = sqlite3.connect('./bd/data.db')
conn = psycopg2.connect(
                host='localhost',
                database='projeto-db',
                user='postgres',
                password='1234'
            )

sql = ''
with open('bd/create_table.sql') as file:
    sql = file.read()

cs = conn.cursor()
cs.execute(sql)


with open('bd/dump.sql') as file:
    sql = file.read()

cs.execute(sql)

conn.commit()

conn.close()