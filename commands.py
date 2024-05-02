import database
import misc

help_msg = """
You must provide a command.

task [name]
    Record the duration of a task.

latest
    Get the latest recorded task.

today
    Get all tasks recorded today.

date [y-d-m]
    Get all tasks recorded on a certain date.

help
    Displays this help message.
"""


def dispatch(cursor, args):
    match args[1]:
        case "task":

            # Check if a task name was provided.
            if len(args) >= 3:
                task(cursor, args[2])
            else:
                print("Error: The task must be given a name.")

        case "latest":
            latest(cursor)

        case "today":
            today(cursor)

        case "date":
            date(cursor, args[2])

        case "help":
            help()


def help():
    print(help_msg)


# Record a new task.
def task(cursor, name):

    duration = misc.elapsed_time()
    print("Total tast time: ", misc.timestamp(duration))
    database.add_record(name, duration, cursor)


# Get the latest recorded task.
def latest(cursor):
    cursor.execute("SELECT * FROM tasks ORDER BY id DESC LIMIT 1")

    latest = cursor.fetchone()
    if (latest is None):
        print("No task found.")
    else:
        timestamp = misc.timestamp(latest[3])
        print(f"ID {latest[0]}: {latest[1]}, {latest[2]}, {timestamp}")


# Get all tasks recorded today.
def today(cursor):
    cursor.execute("""
        SELECT * FROM tasks
        WHERE DATE(date) = DATE('now')
    """)

    entries = cursor.fetchall()
    for entry in entries:
        timestamp = misc.timestamp(entry[3])
        print(f"ID {entry[0]}: {entry[1]}, {entry[2]}, {timestamp}")

    if (len(entries) == 0):
        print("No tasks found.")


def date(cursor, date):
    cursor.execute(f"SELECT * FROM tasks WHERE DATE(date) = '{date}'")
    entries = cursor.fetchall()

    for entry in entries:
        timestamp = misc.timestamp(entry[3])
        print(f"ID {entry[0]}: {entry[1]}, {entry[2]}, {timestamp}")

    if (len(entries) == 0):
        print("No tasks found.")
