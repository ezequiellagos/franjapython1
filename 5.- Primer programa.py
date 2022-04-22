# Transformar pesos chilenos a dólares

# El programa debe pedir una cantidad de pesos y mostrar el resultado en dólares

pesos = input("Ingrese la cantidad de pesos chilenos: ")
pesos = float(pesos)
valor_dolar = 806
dolares = pesos / valor_dolar
dolares = round(dolares, 2)
dolares = str(dolares)
print("Usted tiene $" + dolares + " dolares")

# Tarea: programa que transforme dólares a pesos chilenos