# Funciones
def imprimir_mensaje():
    print("Mensaje de bienvenida")
    print("Aprendiendo Python")

# imprimir_mensaje()
# imprimir_mensaje()
# imprimir_mensaje()

# Parámetros
def saludo(nombre, apellido):
    print("Hola " + nombre + " " + apellido)

# entrada_texto = input("Ingrese su nombre: ")
# entrada_apellido = input("Ingrese su apellido: ")
# saludo(entrada_texto, entrada_apellido)

def suma(a, b):
    resultado = a + b
    return resultado

def resta(a, b):
    resultado = a - b
    return resultado

def division(a, b):
    resultado = a / b
    return resultado

def multiplicacion(a, b):
    resultado = a * b
    return resultado

print("""1 Para Suma
2 Para Resta
3 Para División
4 Para Multiplicación""")
opcion = int(input("Seleccione una opción: "))
numero_1 = int(input("Ingrese numero 1: "))
numero_2 = int(input("Ingrese numero 2: "))

if opcion == 1:
    res = suma(numero_1, numero_2)
    print("La suma es: " + str(res))
elif opcion == 2:
    res = resta(numero_1, numero_2)
    print("La resta es: " + str(res))
elif opcion == 3:
    res = division(numero_1, numero_2)
    print("La división es: " + str(res))
elif opcion == 4:
    res = multiplicacion(numero_1, numero_2)
    print("La multiplicación es: " + str(res))
else:
    print("Opción no válida")