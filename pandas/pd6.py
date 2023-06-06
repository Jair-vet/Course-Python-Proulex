import pandas as pd

# 'edad', 'peso', 'altura', 'presion', 'glucosa'

try:
    # Cargar el Archivo al DataFrame
    df = pd.read_csv("/Users/jairaceves/Documents/Curso Python/pandas/votos.csv")

    # Consulta 1
    c1 = df.query('candidato == "Hillary Clinton"')
    if c1.shape[0] == 0:
        print("La consulta 1 no contiene datos")
    else: 
        print(f"La consulta 1 Contiene {c1['estado'].count()} registros")
        # Exportar los registros
        c1.to_csv("/Users/jairaceves/Documents/Curso Python/pandas/consulta1.csv")
    

    # Consulta 2
    # Donde la cantidad de votos sea mayor a 20000
    c2 = df.query('candidato == "Hillary Clinton" and votos > 20000')
    if c2.shape[0] == 0:
        print("La consulta 2 no contiene datos")
    else: 
        print(f"La consulta 2 Contiene {c2['estado'].count()} registros")
        # Exportar los registros
        c2.to_csv("/Users/jairaceves/Documents/Curso Python/pandas/consulta2.csv")
    

    # Consulta 3
    c3 = df.query('partido == "Democrat" and estado == "Alabama" or estado == "Wisconsin"')
    if c3.shape[0] == 0:
        print("La consulta 3 no contiene datos")
    else: 
        print(f"La consulta 3 Contiene {c3['estado'].count()} registros")
        # Exportar los registros
        c3.to_csv("/Users/jairaceves/Documents/Curso Python/pandas/consulta3.csv")
    

    # Consulta 3
    c4 = df.query('partido == "Republican" and votos > 1500')
    if c4.shape[0] == 0:
        print("La consulta 4 no contiene datos")
    else: 
        print(f"La consulta 4 Contiene {c4['estado'].count()} registros")
        # Exportar los registros
        c4.to_csv("/Users/jairaceves/Documents/Curso Python/pandas/consulta4.csv")


except Exception as e:
    print(e)
