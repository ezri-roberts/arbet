import sqlite3, time, sys, signal

def task_time():

  cmd = ""
  start = time.time()
  last = start
  toal = 0

  while(cmd.lower() != 'q'):

    cmd = input("Timing task. Enter 'q' to stop: ")
    total = round((time.time() - start), 2)

  return total

def add_record(name, time, cursor):
  sql = f"INSERT INTO tasks (name, date, time) VALUES ('{name}', DATE('now'), '{time}')"
  cursor.execute(sql)

def main():

  try:
    db = sqlite3.connect("arbet.db")
    cursor = db.cursor()

    time = task_time()
    add_record("Task1", time, cursor)

    cursor.close()

  except sqlite3.Error as error:
    print("Error: ", error)

  finally:

    if(db):
      db.commit()
      db.close()
      print("Connection closed.")

if __name__ == "__main__":
  main()
