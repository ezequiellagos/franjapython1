# Ejercicio 1
# Escribir un programa que contenga una función que reciba una lista de palabras y devuelva la más larga. Imprimir por pantalla la palabra resultante.

def palabra_mas_larga(lista):
  palabra_mas_larga = ''
  for palabra in lista:
    if len(palabra) > len(palabra_mas_larga):
      palabra_mas_larga = palabra
  return palabra_mas_larga

def main():
  lista_palabras = ['hola', 'mundo', 'manzana', 'sol']
  print( palabra_mas_larga(lista_palabras) )

if __name__ == '__main__':
  main()