#Ciclo For
# Crear una repeticion finita de instrucciones

# 1) Recorer una lista e imprimir sus valores

# Declarar una lista
productos = ["Laptop, Impresora, CPU, Bocinas, Audifonos"]

# Iterador: es un objeto que sirve para recorrer/repetir una interacción con un ciclo

for p in productos:
    print(p) 

# 2) Recorer una lista para encontrar un valor
valores = [50,100,150,200,250,300,350,400,450,500]

buscar = 300

for v in valores:
    print(v)
    if buscar == v:
        print(f"Encontré lo que buscaba {buscar}")
        # El break sirve para forzar el cierre del for
        break

# 3) Repetir un proceso N cantidad de veces
n = int(input("¿Cuantas veces me repito? "))
saludo = "Hola mundo con Python"

for s in range(n):
    print(saludo)