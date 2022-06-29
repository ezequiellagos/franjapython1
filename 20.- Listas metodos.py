# Listas metodos

def main():
    numeros = [1,3,5,7,8,9,0]
    # print( type(numeros) )
    # print( numeros[4] )

    objetos = ['hola', 2, 4.5, True]
    print(objetos)
    
    # Agregar elementos
    objetos.append(False)
    print( objetos )

    objetos.append(45)
    objetos.append("Hola mundo")
    print( objetos )

    # Eliminar elementos
    objetos.pop(0)
    print( objetos )

    objetos.pop()
    print( objetos )

    # Recorrer lista
    for objeto in objetos:
        print(objeto)

    # Ordenar lista
    print( objetos[::-1] )

    # Sumar listas
    numeros_1 = [1, 2, 3]
    numeros_2 = [4, 5, 6]
    lista_final = numeros_1 + numeros_2
    print( lista_final )

    # Multiplicar listas
    print( numeros_1 * 3 )


if __name__ == '__main__':
    main()