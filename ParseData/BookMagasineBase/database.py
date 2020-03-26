import sqlite3

conn = sqlite3.connect("mydata.db")

_SQL_CREATE = "CREATE TABLE books (name TEXT, price TEXT, description TEXT, info TEXT)"
_SQL_DATA = "SELECT * FROM books"
cursor = conn.cursor()

cursor.execute(_SQL_DATA)
res = cursor.fetchall()
for r in res:
    print("NAME", r[0])
    print("PRICE", r[1])

conn.close()
