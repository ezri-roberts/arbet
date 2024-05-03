import misc

help_msg = """
You must provide a command.

task [name] [category]
    Record the duration of a task.
    Category is optional.

latest
    Get the latest recorded task.

category [name]
    Get all tasks from a certain category.

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
            task(cursor, args)
        case "latest":
            latest(cursor)
        case "today":
            today(cursor)
        case "date":
            date(cursor, args[2])
        case "category":
            category(cursor, args)
        case "help":
            help()


def help():
    print(help_msg)


# Record a new task.
def task(cursor, args):

    # Check if a task name was provided.
    if len(args) < 3:
        print("Error: The task must be given a name.")
        return

    duration = misc.elapsed_time()
    print("Total tast time: ", misc.timestamp(duration))

    cursor.execute(f"""
        INSERT INTO tasks (name, date, duration)
        VALUES ('{args[2]}', DATE('now'), '{duration}')
    """)

    task_id = cursor.lastrowid

    if (len(args) >= 4):
        cursor.execute(f"""CREATE TABLE IF NOT EXISTS category_{args[3]} (
            task_id INTEGER,
            FOREIGN KEY (task_id) REFERENCES tasks(id)
        );""")
        cursor.execute(f"""
            INSERT INTO category_{args[3]} (task_id)
            VALUES ({task_id})
        """)


def category(cursor, args):
    cursor.execute(f"SELECT * FROM category_{category}")

    entries = cursor.fetchall()
    for entry in entries:
        timestamp = misc.timestamp(entry[3])
        print(f"ID {entry[0]}: {entry[1]}, {entry[2]}, {timestamp}")

    if (len(entries) == 0):
        print("No tasks found.")


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
