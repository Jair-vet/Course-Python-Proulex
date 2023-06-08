import turtle
import random

# Crear la ventana
ventana = turtle.Screen()
ventana.title("Tortuga Figuras")
ventana.bgcolor("white")


# Metodos de movimiento
def cuadro():
    turtle.color(random.choice(["red", "blue", "green", "yellow", "black", "pink", "orange", "skyBlue"]))
    for x in range(4):
        turtle.forward(100)
        turtle.right(90)

def triangulo():
    turtle.color(random.choice(["red", "blue", "green", "yellow", "black", "pink", "orange", "skyBlue"]))
    for x in range(3):
        turtle.forward(100)
        turtle.right(120)

def circulo():
    turtle.color(random.choice(["red", "blue", "green", "yellow", "black", "pink", "orange", "skyBlue"]))
    for x in range(1):
        turtle.circle(50)


# Configuracion de los listen
ventana.listen()
ventana.onkeypress(cuadro, "s")
ventana.onkeypress(triangulo, "t")
ventana.onkeypress(circulo, "c")

# Mantener abierta la ventana
ventana.mainloop()