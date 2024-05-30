import os
print("Directorio actual:", os.getcwd())

def Suma(s1,s2):
  return s1+s2
def Resta(r1,r2):
  return r1-r2
def Multi(m1,m2):
  return m1*m2
def Divis(d1,d2):
  try:
    resultado = d1/d2
    return resultado
  except ZeroDivisionError:
    return -1

print("Hola")