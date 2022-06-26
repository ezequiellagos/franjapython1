# Modulo random

import random
# import random as rd

def main():
    # rd.randint()
    numero_aleatorio = random.randint(1, 100)
    print(numero_aleatorio)

    lista_numeros = [1, 2, 'hola', 4, True, 6, 7]
    numero_aleatorio = random.choice( lista_numeros )
    print( numero_aleatorio )

if __name__ == '__main__':
    main()

    