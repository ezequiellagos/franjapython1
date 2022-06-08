# Listas

lista_numeros = [1,2,3,4,5]
lista_nombres = ["Ezequiel 'profesor' ", 'Lagos']
lista_tuplas = [(1,2,3), (1,2,3,4,5,6)]
lista_lista = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print( type(lista_numeros) )

for items in lista_lista:
    print(items[0])

# Ejemplo
nombre = "Juan"
nombre_2 =  "Juan 2"
lista_juanes = [nombre, nombre_2]
for juan in lista_juanes:
    print(juan)