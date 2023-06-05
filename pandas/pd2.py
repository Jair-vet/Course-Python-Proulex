import pandas as pd

s = pd.Series([80,70,100,60,60,60,100,100,100,75])

'''
# Cantidad de elementos
print(f"La serie contiene {s.count()} elementos")

# Sumar los Elementos
print(f"La Suma de los elementos es: {s.sum()} ")

# Suma acumulada de los elementos
print(f"La suma Acumulada de los elementos es: {s.cumsum()}")

# Frecuencia de la serie
print(s.value_counts())

# Maximo, Minimo, Media
print(f"El valor Minimo de la serie es: {s.min()}")
print(f"El valor Maximo de la serie es: {s.max()}")
print(f"El valor Medio de la serie es: {s.mean()}")

# Desviacion Estandar
print(f"La desviación estándar es: {s.std()}")
'''

print(s.describe())