import turtle

# Crear la ventana
ventana = turtle.Screen()
ventana.title("Tortuga Listen")
ventana.bgcolor("white")

# Crear una tortuga
tortuga = turtle.Turtle()
tortuga.shape("turtle")
tortuga.color("blue")

# Metodos de movimiento
def mover_adelante():
    tortuga.forward(30)

def mover_atras():
    tortuga.back(30)

def girar_izquierda():
    tortuga.left(90)

def girar_derecha():
    tortuga.right(90)

# Configuracion de los listen
ventana.listen()
ventana.onkeypress(mover_adelante, "Up")
ventana.onkeypress(mover_atras, "Down")
ventana.onkeypress(girar_izquierda, "Right")
ventana.onkeypress(girar_derecha, "Left")

# Mantener abierta la ventana
turtle.done()