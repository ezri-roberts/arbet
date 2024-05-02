import sqlite3
import sys
import commands


def main():

    try:

        # Connect to database.
        db = sqlite3.connect("arbet.db")
        cursor = db.cursor()

        # Create tasks table if it does not exist.
        cursor.execute("""CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            date DATE NOT NULL,
            duration REAL NOT NULL
        );""")

        # Dispatch command if one was provided.
        if len(sys.argv) > 1:
            commands.dispatch(cursor, sys.argv)
        else:
            commands.help()

        cursor.close()

    except sqlite3.Error as error:
        print("Error: ", error)

    finally:

        if (db):
            db.commit()
            db.close()


if __name__ == "__main__":
    main()
