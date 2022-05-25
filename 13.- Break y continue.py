# Break y continue

def main():
    # Imprimir los números impares
    # for contador in range(1, 101):
    #     if contador % 2 == 0:
    #         continue
    #     print(contador)
    
    # for numero in range(1, 10000):
    #     print(numero)
    #     if numero == 5731:
    #         break

    texto = input("Ingrese un texto: ")
    for letra in texto:
        if letra == 'o':
            break
        print(letra)


if __name__ == '__main__':
    main()