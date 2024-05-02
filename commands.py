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

help
    Displays this help message.
"""


def dispatch(cursor, args):
    match args[1]:
        case "task":

            if len(args) >= 3:
                task(cursor, args[2])
            else:
                print("Error: The task must be given a name.")

        case "latest":
            latest(cursor)

        case "today":
            today(cursor)

        case "help":
            help()


def help():
    print(help_msg)


def task(cursor, name):

    duration = misc.elapsed_time()
    print("Total tast time: ", misc.timestamp(duration))
    database.add_record(name, duration, cursor)


def latest(cursor):
    cursor.execute("SELECT * FROM tasks ORDER BY id DESC LIMIT 1")

    latest = cursor.fetchone()
    print(
        f"Latest Task: {latest[1]}, {latest[2]}, {misc.timestamp(latest[3])}")


def today(cursor):
    cursor.execute("""
        SELECT * FROM tasks
        WHERE DATE(date) = DATE('now')
    """)

    entries = cursor.fetchall()
    for entry in entries:
        print(
            f"{entry[0]}: {entry[1]}, {entry[2]}, {misc.timestamp(entry[3])}")
