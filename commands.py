import database, misc

def dispatch(cursor, args):
    match args[1]:
        case "task":

            if len(args) >= 3:
                task(cursor, args[2])
            else:
                print("Error: The task must be given a name.")
                exit(1)

def task(cursor, name):

    duration = misc.elapsed_time()
    print("Total tast time: ", misc.timestamp(duration))
    database.add_record(name, duration, cursor)
