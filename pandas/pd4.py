import pandas as pd

# Data Frame: es una estructura de dos dimensiones
# Podriamos decir que es una tabla (Filas, Columnas)
# 'edad', 'peso', 'altura', 'presion', 'glucosa'
try:
    # Cargar el Archivo al DataFrame
    df = pd.read_csv("/Users/jairaceves/Documents/Curso Python/pandas/datos.csv")

    # Suma
    print("========================= SUMA =========================")
    print(f" La suma de las edades es: {df['edad'].sum()}")
    print(f" La suma de los pesos es: {df['peso'].sum()}")
    print(f" La suma de las alturas es: {df['altura'].sum()}")
    print(f" La suma de las glucosas es: {df['presion'].sum()}")
    print(f" La suma de las presiones es: {df['glucosa'].sum()}")
    # Minimo
    print("========================= MINIMO =========================")
    print(f" El minimo de las edad es: {df['edad'].min()}")
    print(f" El minimo de las peso es: {df['peso'].min()}")
    print(f" El minimo de las altura es: {df['altura'].min()}")
    print(f" El minimo de las presion es: {df['presion'].min()}")
    print(f" El minimo de las glucosa es: {df['glucosa'].min()}")
    # Maximo
    print("========================= MAXIMO =========================")
    print(f" El máximo de las edad es: {df['edad'].max()}")
    print(f" El máximo de las peso es: {df['peso'].max()}")
    print(f" El máximo de las altura es: {df['altura'].max()}")
    print(f" El máximo de las presion es: {df['presion'].max()}")
    print(f" El máximo de las glucosa es: {df['glucosa'].max()}")
    # Media
    print("========================= MEDIA =========================")
    print(f" La media de las edad es: {df['edad'].mean()}")
    print(f" La media de las peso es: {df['peso'].mean()}")
    print(f" La media de las altura es: {df['altura'].mean()}")
    print(f" La media de las presion es: {df['presion'].mean()}")
    print(f" La media de las glucosa es: {df['glucosa'].mean()}")
    # STD
    print("========================= STD =========================")
    print(f" La desviación estandar de las edad es: {df['edad'].std()}")
    print(f" La desviación estandar de las peso es: {df['peso'].std()}")
    print(f" La desviación estandar de las altura es: {df['altura'].std()}")
    print(f" La desviación estandar de las presion es: {df['presion'].std()}")
    print(f" La desviación estandar de las glucosa es: {df['glucosa'].std()}")


except Exception as e:
    print(e)
