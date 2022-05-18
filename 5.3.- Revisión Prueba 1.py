# Ejercicio 1
# Una panadería vende barras de pan a 3.49€ cada una. 
# El pan que no es el día tiene un descuento del 60 % . 
# Escribe un programa que comience leyendo el número de 
# barras vendidas que no son del día. Después tu programa 
# debe mostrar el precio habitual de una barra de pan, 
# el descuento que se le hace por no ser fresca y el coste final total.

barras = int(input("Ingrese la cantidad de barras vendidas que no son frescas: "))
precio = 3.49
descuento = 0.6
descuento_porcentual = 0.6 * 100
coste = barras * precio * (1 - descuento)
print("Precio de barra de pan: " + str(precio))
print("Descuento a barras de pan no frescas: " + str(descuento_porcentual) + "%")
print("Coste final: " + str(round(coste, 2)))

# Ejercicio 2
# Escribir un programa que le pregunte al usuario una cantidad a 
#invertir, el interés porcentual anual y el número de años, 
# y muestre por pantalla el capital obtenido en la inversión 
# redondeado a dos decimales.

cantidad = float(input("Ingrese cantidad de dinero a invertir: "))
interes = float(input("Ingrese el interés porcentual anual: "))
anio = int(input("Años a invertir: "))

formula = cantidad * ((interes/100) + 1) ** anio
formula = round(formula, 2)

print("Capital final es: " + str(formula))


# Ejercicio 3
# Escribir un programa que haga transformaciones de pesos a dólares. 
# Debe preguntarle al usuario si desea transformar de 
# pesos mexicanos a dólares, de pesos chilenos a dólares, 
# o desde pesos argentinos a dólares. Mostrar por pantalla la 
# cantidad de monedas a convertir, la moneda que se convirtió 
# y el monto en dólares.
# Peso Chileno a dólar: 855
# Peso Mexicano a dólar: 20
# Peso Argentino a dólar: 115

print("""Seleccione la moneda desde la cual convertir a dolares:
1 Peso Chileno
2 Peso Mexicano
3 Peso Argentino""")
opcion = int(input("Ingrese la opcion: "))
dinero = int(input("Ingrese la cantidad a convertir: "))

if opcion == 1:
    tipo_cambio = "Pesos Chileno"
    cambio = 855
    dolares = dinero / cambio
    dolares = round(dolares, 2)
elif opcion == 2:
    tipo_cambio = "Pesos Mexicano"
    cambio = 20
    dolares = dinero / cambio
    dolares = round(dolares, 2)
elif opcion == 3:
    tipo_cambio = "Pesos Argentino"
    cambio = 115
    dolares = dinero / cambio
    dolares = round(dolares, 2)
else:
    print("Opción no válida")

print("Convirtió "+ str(dinero) + " " + tipo_cambio + " a dólares y el total es: " + str(dolares))
