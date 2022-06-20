# Ejercicio 2
# Escriba un programa que pida dos palabras y diga si riman o no. Si coinciden las últimas tres letras tiene que decir que riman. Si coinciden sólo las últimas dos tiene que decir que riman un poco. Y si no coinciden, decir que no riman. Validar que las palabras tengan al menos tres letras. Nota: Utilizar slices

# Cortas: ra ma
# Riman: manzana capitana
# Riman poco: completa camita
# No riman: sopaipilla churro

def main():
  palabra_uno = input("Ingrese la primera palabra: ").lower()
  palabra_dos = input("Ingrese la segunda palabra: ").lower()

  if len(palabra_uno) < 3 or len(palabra_dos) < 3:
    print("Las palabras deben tener al menos 3 letras")
  elif palabra_uno[-3:] == palabra_dos[-3:]:
    print("Las palabras riman")
  elif palabra_uno[-2:] == palabra_dos[-2:]:
    print("Las palabras riman un poco")
  else:
    print("Las palabras no riman")

if __name__ == '__main__':
  main()