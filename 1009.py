TOTAL = None
TOTAL_DE_VENDAS = None
SALARIO_FIXO = None
PRIMEIRO_NOME_DO_VENDEDOR = None

def read_string():
  try:
    # read for Python 2.x
    return raw_input()
  except NameError:
    # read for Python 3.x
    return input()

def read_numeric():
  try:
    # read for Python 2.x
    return float(raw_input())
  except NameError:
    # read for Python 3.x
    return float(input())


PRIMEIRO_NOME_DO_VENDEDOR = read_string()
SALARIO_FIXO = read_numeric()
TOTAL_DE_VENDAS = read_numeric()
TOTAL = SALARIO_FIXO + TOTAL_DE_VENDAS * 0.15
TOTAL = "{:0.2f}".format(TOTAL)
TOTAL_DE_VENDAS = "{:0.2f}".format(TOTAL_DE_VENDAS)
print(str("TOTAL = R$ ") + str(TOTAL))
