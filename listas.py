# Listas
# Es un arreglo
# Coleccion de datos de una dimesión
# Las listas pueden ser modificadas en tiempo de ejecución
# Item: elemento de la lista
# Index: la posicion dentro de la lista

# Declarar una lista
frutas = ["manzana", "platano", "pera", "naranja"]

# Cantidad de items de una lista
print(len(frutas))

# Canbiar el valor de un item
frutas[3] = "Sandia"
print(frutas)

# Agregar un item al final de la lista
frutas.append("naranja")
print(frutas)

# Agregar un nuevo item en cierta posición
frutas.insert(0, "durazno")
print(frutas)


# Nueva lista
tropicales = ["piña", "mango", "coco"]

#* unir 2 listas
frutas.extend(tropicales)
print(frutas)

# Eliminar un item con base a su nombre
frutas.remove("platano")
print(frutas)

# Eliminar un item con base a su posición
frutas.pop(1)
print(frutas)

# Limpiar la lista
frutas.clear()
print(frutas)