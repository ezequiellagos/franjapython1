# Ejercicio 1
# Escribir un programa que pregunte el nombre por consola
# y un número entero e imprimir por pantalla el nombre 
# tantas veces como el numero que introdujo

# Solución
#nombre = input("Ingrese su nombre: ")
#numero = int(input("Ingrese un numero: "))
#print(nombre * numero)

# Ejercicio 2
# Escribir un programa que muestre por pantalla el resultado
# de la siguiente operación matemática

# Solución 2
# print( ((3+2)/(2*5))**2 )

# Ejercicio 3
# Escribir un programa que lea un entero positivo n 
# introducido por el usuario y después muestre por pantalla 
# la suma de todos los enteros desde 1 hasta n.
# La suma de los n primeros positivos puede ser calculada
# de la siguiente forma


# Solución 3
n = int(input("Ingrese un numero positivo: "))
if n >= 1:
    suma = (n * (n + 1)) / 2
    suma = str(suma)
    n = str(n)
    print("La suma de los primeros numeros enteros desde 1 hasta " + n + " es " + suma)
else:
    print("El numero no es mayor o igual a 1")