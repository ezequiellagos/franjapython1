# Ejercicio 3: Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar $3.500 y si es mayor de 18 años, $8.000.

def main():
    edad = int(input("Ingrese su edad: "))
    if edad < 4:
        precio = 0
    elif edad <= 18:
        precio = 3500
    else:
        precio = 8000
    
    print("El precio de la entrada es: " + str(precio))
    

if __name__ == '__main__':
    main()