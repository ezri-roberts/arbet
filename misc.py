import time, sys, math

def elapsed_time():

  cmd = ""
  start = time.time()
  last = start
  toal = 0

  while(cmd.lower() != 'q'):

    cmd = input("Timing task. Enter 'q' to stop: ")
    total = round((time.time() - start), 2)

  return total

def timestamp(seconds):
    hours = math.floor(seconds // 3600)
    minutes = math.floor((seconds % 3600) // 60)
    seconds = math.floor(seconds % 60)
    return f"{hours}:{minutes}:{seconds}"
