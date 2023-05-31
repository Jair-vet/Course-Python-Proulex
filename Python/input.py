# Recibir el valor desde la terminal
# nombre = input("¿Como te llamas? ")

# Maneras de imprimir en la terminal
# print("Tu nombre es:",nombre)
# print(f"Tu nombre es: {nombre}")
# print("Tu nombre es: {}".format(nombre))

"""
minusculas = nombre.lower()
mayusculas = nombre.upper()
propio = nombre.title()
caracteres = len(nombre)

print(f"Minusculas: {minusculas}")
print(f"Mayusculas: {mayusculas}")
print(f"Nombre propio: {propio}")
print(f"Cantidad caracteres: {caracteres}")
"""

paterno = input("Paterno: ")
materno = input("Materno: ")
nombre = input("Nombre: ")
nombre2 = input("Segundo Nombre: ")

completo = nombre + " " +nombre2 + " " +  paterno + " " + materno 

print("Nombre completo: ", completo.title())