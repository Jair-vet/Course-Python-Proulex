# Librerias
from turtle import bye
import turtle
import time

# Ventana
pong = turtle.Screen()
pong.title("Juego Pong")
pong.bgcolor("#000")
pong.setup(width=800, height=600)
pong.tracer(0)

# Marcador 
puntaje_a = 0
puntaje_b = 0

# raqueta A
raqueta_a = turtle.Turtle()
raqueta_a.shape("square")
raqueta_a.color("#469EDF")
raqueta_a.shapesize(stretch_wid=5, stretch_len=1)
raqueta_a.penup()
raqueta_a.goto(-350,0)

# raqueta B
raqueta_b = turtle.Turtle()
raqueta_b.shape("square")
raqueta_b.color("#6462EC")
raqueta_b.shapesize(stretch_wid=5, stretch_len=1)
raqueta_b.penup()
raqueta_b.goto(350,0)

# Pelota
pelota = turtle.Turtle()
pelota.shape("circle")
pelota.color("#46DF70")
pelota.penup()
pelota.goto(0,0)
pelota.dx = 0.5
pelota.dy = 0.5
static = True

# Marcador
marcador = turtle.Turtle()
marcador.color("#fff")
marcador.penup()
marcador.hideturtle()
marcador.goto(0, 250)
marcador.write("Player A: 0    Player B: 0",align="center", font=("Fixedsys", 24, "bold"))

# Inicio
inicio = turtle.Turtle()
inicio.speed(0)
inicio.color("#fff")
inicio.penup()
inicio.hideturtle()
inicio.goto(0, 120)
inicio.write("PRESS ENTER TO START",align="center", font=("Fixedsys", 24, "bold"))


# Cancha
# Izquierda
izquierda = turtle.Turtle()
izquierda.shape("square")
izquierda.color("#FFF")
izquierda.penup()
izquierda.goto(-397,0)
izquierda.shapesize(stretch_wid=30, stretch_len=0.7)
# Derecha
derecha = turtle.Turtle()
derecha.shape("square")
derecha.color("#FFF")
derecha.penup()
derecha.goto(390,0)
derecha.shapesize(stretch_wid=30, stretch_len=0.7)
# Superior
superior = turtle.Turtle()
superior.shape("square")
superior.color("#FFF")
superior.penup()
superior.goto(0,295)
superior.right(90)
superior.shapesize(stretch_wid=100, stretch_len=0.7)
# Inferior
inferior = turtle.Turtle()
inferior.shape("square")
inferior.color("#FFF")
inferior.penup()
inferior.goto(0,-290)
inferior.right(90)
inferior.shapesize(stretch_wid=100, stretch_len=0.7)
# Medio
medio = turtle.Turtle()
medio.shape("square")
medio.color("#FFF")
medio.penup()
medio.goto(0,0)
medio.shapesize(stretch_wid=30, stretch_len=0.1)

# Metodos
def actualizar_puntaje():
    marcador.clear()
    marcador.write("Player A: {} Player B: {}".format(puntaje_a, puntaje_b),align="center", font=("Fixedsys", 24, "bold")) #Courier   

def raqueta_a_arriba():
    y = raqueta_a.ycor()
    if y <= 230:
        y += 20
        raqueta_a.sety(y)

def raqueta_a_abajo():
    y = raqueta_a.ycor()
    if y >= -230:
        y -= 20
        raqueta_a.sety(y)

def raqueta_b_arriba():
    y = raqueta_b.ycor()
    if y <= 230:
        y += 20
        raqueta_b.sety(y)

def raqueta_b_abajo():
    y = raqueta_b.ycor()
    if y >= -230:
        y -= 20
        raqueta_b.sety(y)

def iniciar_juego():
    pass

def reiniciar_pantalla():
    pass


# Listen
pong.listen()
pong.onkeypress(raqueta_a_arriba, "w")
pong.onkeypress(raqueta_a_abajo, "s")
pong.onkeypress(raqueta_b_arriba, "Up")
pong.onkeypress(raqueta_b_abajo, "Down")
pong.onkeypress(iniciar_juego, "Return")
pong.onkeypress(bye, "x")

# Actualizacion de la Ventana
while True:
    try:
        pong.update()
    except:
        break
