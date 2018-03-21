Distancia = None

def read_integer():
  try:
    # read for Python 2.x
    return int(raw_input())
  except NameError:
    # read for Python 3.x
    return int(input())


Distancia = read_integer()
Distancia = Distancia * 2
print(str(Distancia) + str(" minutos"))
