# Generador contraseña

import random

def generar_contrasena():
    mayusculas = ['A', 'B', 'C', 'D', 'E', 'F']
    minusculas = ['a', 'b', 'c', 'd', 'e', 'f']
    numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    simbolos = ['#', '$', '%', '&', '/']

    caracteres = mayusculas + minusculas + numeros + simbolos
    contrasena = []

    for i in range(15):
        caracter_aleatorio = random.choice( caracteres )
        contrasena.append( caracter_aleatorio )

    # Convertir lista a string
    # "" o '' simbolizan un string vacio
    # .join accedemos al metodo join
    contrasena = ''.join(contrasena)

    return contrasena

def main():
    contrasena = generar_contrasena()
    print("Su contraseña es: " + contrasena)

if __name__ == '__main__':
    main()