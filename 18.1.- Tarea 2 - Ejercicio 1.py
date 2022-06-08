# Ejercicio 1: 
# Escribir un programa en el que se pregunte al usuario
#  por una frase y una letra, y muestre por pantalla el número de veces
#  que aparece la letra en la frase. 

def main():
    frase = input("Escriba una frase: ").lower()
    letra_a_buscar = input("Escriba una letra: ").lower()

    contador = 0
    for letra in frase:
        if letra == letra_a_buscar:
            contador = contador + 1
    
    print("La letra " + letra_a_buscar + " aparece " + str(contador))

if __name__ == '__main__':
    main()