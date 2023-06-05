# pip3 install pandas 

import pandas

# Serie: es una estructura de una dimensión
# Una serie se alimenta de una lista

lista = [1,2,3,4,5,6,7,8,9,10,11,12]

s = pandas.Series(lista)

# Imprimir la serie
print(s)

print(f"El tamaño de la serie es: {s.size}")