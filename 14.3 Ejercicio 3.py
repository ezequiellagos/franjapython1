# Ejercicio 3
# Escribir un programa que muestre por pantalla la tabla
# de multiplicar del 1 al 12. El usuario ingresa el número de la tabla

def main():
    numero_tabla = int( input("Ingrese el número de la tabla: ") )
    for contador in range(1, 13):
        frase = str(numero_tabla) + ' X ' + str(contador) + ' es: ' + str(contador*numero_tabla)
        print(frase)

if __name__ == '__main__':
    main()