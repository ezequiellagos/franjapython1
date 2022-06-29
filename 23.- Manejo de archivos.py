# Manejo de archivos

# with: manejador contextual.Si el programa se cierra inesperadamente, evita que se corrompa el archivo

def leer():
    numeros = []
    with open('./archivos/numeros.txt', 'r') as file:
        for linea in file:
            numeros.append( int(linea) )
    
    print( numeros )

def escribir():
    pass

def main():
    leer()

if __name__ == '__main__':
    main()