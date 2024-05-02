import sqlite3

def add_record(name, duration, cursor):
  sql = f"INSERT INTO tasks (name, date, duration) VALUES ('{name}', DATE('now'), '{duration}')"
  cursor.execute(sql)
