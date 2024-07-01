import time

def main():
  try:
      # This will work in Python 3.6 but not in Python 3.8,
      # where time.clock() has been removed.
      start_time = time.clock()
      print("time.clock() value:", start_time)
  except AttributeError:
      print("time.clock() is not available in your Python version. Only available in Python 3.6.")