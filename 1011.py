VOLUME = None
Pi = None
Raio = None

def read_numeric():
  try:
   # read for Python 2.x
    return float(raw_input())
  except NameError:
    # read for Python 3.x
    return float(input())

Pi = 3.14159
Raio = read_numeric()
VOLUME = Pi * 4/3.0 * (Raio * Raio * Raio)
VOLUME = "{:0.3f}".format(VOLUME)
print(str("VOLUME = ") + str(VOLUME))
