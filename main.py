import sqlite3, sys
import commands

def main():

  try:

    db = sqlite3.connect("arbet.db")
    cursor = db.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS tasks (
      id INTEGER PRIMARY KEY,
      name TEXT NOT NULL,
      date DATE NOT NULL,
      duration REAL NOT NULL
    );""")

    if len(sys.argv) > 1:
      commands.dispatch(cursor, sys.argv)
    else:
      print("Error: No command provided.")
      exit(1)

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

