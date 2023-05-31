# Metodo: Accion que puede realizar un objeto
# Para definir un objeto se usa la palabra reservada "def"

# Declaración de los metodos
def saludo():
    print("Este metodo permite saludar")
    
def estudiante():
    nombre = input("Escribe tu nombre: ")
    print(f"Estudiante: {nombre}")

# Metodos con argumentos
def curso(c,h):
    print(f"El curso es de {c}")
    print(f"La cantidad de horas son: {h}")


# Invocar los metodos
saludo()
estudiante()
curso("Workshop Python", 120)