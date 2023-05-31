# Importar Libreria
import os


# Validar el proceso
try:
    # Codigo que deseas ejecutar
    
    # Crear un fichero
    fichero = open("/Users/jairaceves/Documents/Curso Python/fichero.txt", "w")

    # Escribir sobre el fichero
    fichero.write("Esta es la línea 1" + os.linesep)
    fichero.write("Esta es la línea 2" + os.linesep)
    fichero.write("Esta es la línea 3" + os.linesep)

    # Cerrar el Fichero
    fichero.close()

    # Avisar al usuario sobre la creación
    print("Se creó el fichero con exito")
except Exception as error:
    # En caso de que marque error, aqui llegará
    print(error)