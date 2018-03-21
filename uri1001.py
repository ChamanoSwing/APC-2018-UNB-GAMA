B = None
X = None
A = None

def read_integer():
  try:
    # read for Python 2.x
    return int(raw_input())
  except NameError:
    # read for Python 3.x
    return int(input())


B

A = read_integer()
B = read_integer()
X = A + B
print(str("X = ") + str(X))
