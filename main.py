import sqlite3, time, sys, signal, math

def timestamp(seconds):
    hours = math.floor(seconds // 3600)
    minutes = math.floor((seconds % 3600) // 60)
    seconds = math.floor(seconds % 60)
    return f"{hours}:{minutes}:{seconds}"

def task_time():

  cmd = ""
  start = time.time()
  last = start
  toal = 0

  while(cmd.lower() != 'q'):

    cmd = input("Timing task. Enter 'q' to stop: ")
    total = round((time.time() - start), 2)

  return total

def add_record(name, duration, cursor):
  sql = f"INSERT INTO tasks (name, date, duration) VALUES ('{name}', DATE('now'), '{duration}')"
  cursor.execute(sql)

def main():

  task_name = ""

  if len(sys.argv) > 1:
    task_name = sys.argv[1]
  else:
    print("Error: You need to enter a name for the task.")
    exit(1)

  try:

    db = sqlite3.connect("arbet.db")
    cursor = db.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS tasks (
      id INTEGER PRIMARY KEY,
      name TEXT NOT NULL,
      date DATE NOT NULL,
      duration REAL NOT NULL
    );""")

    duration = task_time()
    print("Total tast time: ", timestamp(duration))
    add_record(task_name, duration, cursor)

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
