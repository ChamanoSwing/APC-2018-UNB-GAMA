SALARY = None
NUMERO_DO_FUNCIONARIO = None
valor = None
NUMBER = None

def read_integer():
  try:
    # read for Python 2.x
    return int(raw_input())
  except NameError:
    # read for Python 3.x
    return int(input())

def read_numeric():
  try:
    # read for Python 2.x
    return float(raw_input())
  except NameError:
    # read for Python 3.x
    return float(input())


NUMERO_DO_FUNCIONARIO = read_integer()
NUMBER = read_integer()
valor = read_numeric()
SALARY = NUMBER * valor
SALARY = "{:0.2f}".format(SALARY)
print(str("NUMBER = ") + str(NUMERO_DO_FUNCIONARIO))
print(str("SALARY = U$ ") + str(SALARY))
