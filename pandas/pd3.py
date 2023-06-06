import pandas as pd

# Data Frame: es una estructura de dos dimensiones
# Podriamos decir que es una tabla (Filas, Columnas)


try:
    # Cargar el Archivo al DataFrame
    df = pd.read_csv("/Users/jairaceves/Documents/Curso Python/pandas/datos.csv")
    # Avisar que fue posdible leer el archivo
    print("Archivo leido con exito")
    # Cantidad de filas del archivo
    print(f"El Archivo contiene {df['id'].count()} registros")
    # Conocer el nombre de las columnas
    print(df.columns)
    # Datos estadisticos sobe el campo edad
    print(f"La edad Minima es {df['edad'].min()}")
    print(f"La edad Maxima es {df['edad'].max()}")
    print(f"La edad Media es {df['edad'].mean()}")
    print(f"La desviación estandar de la edad es {df['edad'].std()}")
    # print(f"Datos de la Edad {df['edad'].describe()}")

except Exception as e:
    print(e)
