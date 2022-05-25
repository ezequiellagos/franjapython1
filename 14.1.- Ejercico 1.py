# Ejercicio 1
# Escribir una función a la que se le pase una
#  cadena/variable <nombre> y muestre por pantalla el saludo 
# ¡hola <nombre>!.

def saludo(nombre):
    frase_saludo = "Hola " + nombre + "!"
    return frase_saludo

def main():
    name = saludo( input("Ingrese su nombre: ") )
    print(name)

if __name__ == '__main__':
    main()