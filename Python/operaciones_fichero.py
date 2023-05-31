
import os

try:
    # Variables
    n1 = float(input("Escribe el primer número: "))
    n2 = float(input("Escribe el segundo número: "))

    # Calculos 
    suma = n1 + n2
    resta = n1 - n2
    multiplicacion = n1 * n2
    division = n1 / n2

    # Crear un fichero
    fichero = open("/Users/jairaceves/Documents/Curso Python/resultados.txt", "w")

    # Escribir sobre el fichero
    fichero.write("Python" + os.linesep)
    fichero.write("==================================" + os.linesep)
    fichero.write("Variables, operaciones y fichero" + os.linesep)
    fichero.write("==================================" + os.linesep)
    fichero.write(f"El resultado de la suma es: { n1 + n2 } " + os.linesep)
    fichero.write(f"El resultado de la resta es: { n1 - n2 } " + os.linesep)
    fichero.write(f"El resultado de la multiplicación es: { n1 * n2 } " + os.linesep)
    fichero.write(f"El resultado de la división es: { n1 / n2 } " + os.linesep)

    # Cerrar el Fichero
    fichero.close()

    # Avisar al usuario sobre la creación
    print("Se creó el fichero Resultado con exito")

except Exception as error:
    print(error)