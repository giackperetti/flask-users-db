import sqlite3

connection = sqlite3.connect('test.db')

with open('test.sql') as f:
    connection.executescript(f.read())

db_cursor = connection.cursor()

db_cursor.execute("INSERT INTO users (name) VALUES (?)", ('Admin',))

connection.commit()
connection.close()
