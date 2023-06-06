import pandas as pd

# 'edad', 'peso', 'altura', 'presion', 'glucosa'

try:
    # Cargar el Archivo al DataFrame
    df = pd.read_csv("/Users/jairaceves/Documents/Curso Python/pandas/datos.csv")

    # Consulta 1
    c1 = df.query('edad > 30')
    print(c1)

    # Consulta 2
    c2 = df.query('presion > 120 and presion < 150')
    print(c2)

    # Consulta 3
    c3 = df.query('peso < 100')
    print(c3)
except Exception as e:
    print(e)
