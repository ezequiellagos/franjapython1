# Palíndromo

# Escribir un programa que identifique
# si una palabra es palíndromo o no
# Luz azul
# Ana
# Anita lava la tina
# Yo hago Yoga hoy

def palindromo(palabra):
    palabra = palabra.replace(' ', '')
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False

# Función principal main/run
def main():
    palabra = input("Ingrese una frase: ")
    es_palindromo = palindromo(palabra)

    if es_palindromo:
        print("Es palíndromo")
    else:
        print("No es palíndromo")
    

# Punto de entrada
# Buena práctica
if __name__ == "__main__":
    main()