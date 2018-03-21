A = None
B = None
PROD = None

def read_integer():
  try:
    # read for Python 2.x
    return int(raw_input())
  except NameError:
    # read for Python 3.x
    return int(input())


A = read_integer()
B = read_integer()
PROD = A * B
print(str("PROD = ") + str(PROD))
