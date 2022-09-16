#Programa en Python que calcula el area y radio de un circulo

import math #libreria matematica,se llama para el uso de Pi,raices,etc.

r = float(input("Ingresa  el radio : "))

area = math.pi*r**2
longitud = 2*math.pi*r

print(f"El area es : {area : .1f}") #El .1f referencia cuantos decimales deseas mostrar
print(f"La longitud es : {longitud:.1f}") #Puede ser .nf
