import sqlite3

conn = sqlite3.connect("mydata.db")

_SQL_CREATE = "CREATE TABLE books (name TEXT, price TEXT, description TEXT, info TEXT)"
_SQL_DATA = "SELECT * FROM books"
cursor = conn.cursor()

res = cursor.fetchall()
for r in res:
    print(r)
cursor.execute(_SQL_DATA)

conn.close()
