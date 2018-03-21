MaiorAB = None
C = None
Maior = None
B = None
A = None
Lista = None
Linha1 = None

def read_line():
  try:
    # read for Python 2.x
    return raw_input()
  except NameError:
    # read for Python 3.x
    return input()


Linha1 = read_line()
Lista = Linha1.split(" ")
A = Lista[0]
B = Lista[1]
C = Lista[2]
A = int(A)
B = int(B)
C = int(C)
MaiorAB = ((A + B) + (abs((A - B)))) / 2
Maior = ((MaiorAB + C) + (abs((MaiorAB - C)))) / 2
print(str(Maior) + str(" eh o maior"))
