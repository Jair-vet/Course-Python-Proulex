# Importar las librerias
from turtle import bye
import turtle
import time

# Ventana
pong = turtle.Screen()
pong.title("Juego Pong")
pong.bgcolor("#000000")
pong.setup(width=800,height=600)
pong.tracer(0)

# Puntaje
puntaje_a = 0
puntaje_b = 0

# GOTO(eje horizontal, eje vertical)

# Raqueta A
raqueta_a = turtle.Turtle()
raqueta_a.shape("square")
raqueta_a.color("#5AFF00")
raqueta_a.shapesize(stretch_wid=5, stretch_len=1)
raqueta_a.penup() # Lápiz alzado
raqueta_a.goto(-350,0)

# Raqueta B
raqueta_b = turtle.Turtle()
raqueta_b.shape("square")
raqueta_b.color("#00FFDE")
raqueta_b.shapesize(stretch_wid=5, stretch_len=1)
raqueta_b.penup() # Lápiz alzado
raqueta_b.goto(350,0)

# Pelota
pelota = turtle.Turtle()
pelota.shape("circle")
pelota.color("#FF0000")
pelota.penup()
pelota.goto(0,0)
pelota.dx = 0.5 # velocidad horizontal
pelota.dy = 0.5 # velocidad vertical
estatico = True

# Marcador
marcador = turtle.Turtle()
marcador.color("#FFFFFF")
marcador.penup()
marcador.goto(0,250)
marcador.hideturtle()
marcador.write("Jugador A: 0   Jugador B: 0",
               align="center",font=("Fixedsys",24,"bold"))

# Inicio
inicio = turtle.Turtle()
inicio.color("#FFFFFF")
inicio.penup()
inicio.goto(-10,125)
inicio.hideturtle()
inicio.write("Presiona enter para iniciar",
               align="center",font=("Fixedsys",24,"bold"))


# Cancha

# Izquierda
izquierda = turtle.Turtle()
izquierda.shape("square")
izquierda.color("#FFFFFF")
izquierda.penup()
izquierda.goto(-390,0)
izquierda.shapesize(stretch_wid=30,stretch_len=0.5)

# Derecha
derecha = turtle.Turtle()
derecha.shape("square")
derecha.color("#FFFFFF")
derecha.penup()
derecha.goto(390,0)
derecha.shapesize(stretch_wid=30,stretch_len=0.5)

# Superior
superior = turtle.Turtle()
superior.shape("square")
superior.color("#FFFFFF")
superior.penup()
superior.goto(0,300)
superior.shapesize(stretch_wid=1,stretch_len=39.5)

# Inferior
inferior = turtle.Turtle()
inferior.shape("square")
inferior.color("#FFFFFF")
inferior.penup()
inferior.goto(0,-290)
inferior.shapesize(stretch_wid=1,stretch_len=39.5)

# Medio
medio = turtle.Turtle()
medio.shape("square")
medio.color("#FFFFFF")
medio.penup()
medio.goto(0,0)
medio.shapesize(stretch_wid=30,stretch_len=0.1)

# Metodos
def actualizar_puntaje(puntaje_a,puntaje_b):
    marcador.clear()
    marcador.write(f"Jugador A: {puntaje_a}   Jugador B: {puntaje_b}",
               align="center",font=("Fixedsys",24,"bold"))

def raqueta_a_arriba():
    y = raqueta_a.ycor()
    if y <= 220:
        y+=20
        raqueta_a.sety(y)

def raqueta_a_abajo():
    y = raqueta_a.ycor()
    if y >= -220:
        y-=20
        raqueta_a.sety(y)

def raqueta_b_arriba():
    y = raqueta_b.ycor()
    if y <= 220:
        y+=20
        raqueta_b.sety(y)

def raqueta_b_abajo():
    y = raqueta_b.ycor()
    if y >= -220:
        y-=20
        raqueta_b.sety(y)

def iniciar_juego():
    global estatico
    estatico = False
    inicio.clear()

def pausar_juego():
    global estatico
    estatico = True
    inicio.write("Juego pausado", align="center",
                 font=("Fixedsys",24,"bold"))

def reiniciar_pantalla():
    pelota.goto(0,0)
    # pelota
    pelota.dx *= -1
    inicio.write("Presiona enter para iniciar", align="center",
                 font=("Fixedsys",24,"bold"))
    raqueta_a.goto(-350,0)
    raqueta_b.goto(350,0)

def movimiento_autonomo():
    letrero = turtle.Turtle()
    letrero.penup()
    letrero.color("#FCFF00")
    letrero.goto(0,200)
    letrero.write("Movimiento Autonomo Activado", align="center",
                 font=("Fixedsys",24,"bold"))
# Listen
pong.listen()
pong.onkeypress(raqueta_a_arriba,"w")
pong.onkeypress(raqueta_a_abajo,"s")
pong.onkeypress(raqueta_b_arriba,"Up")
pong.onkeypress(raqueta_b_abajo,"Down")
pong.onkeypress(iniciar_juego,"Return")
pong.onkeypress(pausar_juego,"p")
pong.onkeypress(movimiento_autonomo,"a")
pong.onkeypress(bye,"x")

# Actualización de la ventana
while True:
    try:
        # Actualización de los componentes
        pong.update()

        # Mover la pelota
        # setx | sety = establacer la nueva coordena
        # xcor | ycor = recuperar la coordenada actual
        # dx   | dy   = otorgar movimiento
        if estatico == False:
            # Mover en el eje x (horizontal) a cierta velocidad
            pelota.setx(pelota.xcor() + pelota.dx)
            # Mover en el eje y (vertical) a cierta velocidad
            pelota.sety(pelota.ycor() + pelota.dy)

          # Pared superior
        # Si la pelota toca la pared de arriba
        # entonces, tienen que ir hacia el lado contrario
        if pelota.ycor() >= 280:
            # Efecto del rebote
            pelota.sety(280)
            pelota.dy *= -1

        # Pared inferior
        if pelota.ycor() <= -280:
            # Efecto del rebote
            pelota.sety(-280)
            pelota.dy *= -1

        # Pared derecha
        # Si la pelota toca el limite del lado derecho
        # quiere decir que A metió gol a B
        # se debe actualizar el puntaje y reiniciar la pantalla
        if pelota.xcor() >= 380:
            puntaje_a += 1
            actualizar_puntaje(puntaje_a,puntaje_b)
            estatico = True
            time.sleep(2)
            reiniciar_pantalla()


        # Pared izquierda
        if pelota.xcor() <= -380:
            puntaje_b += 1
            actualizar_puntaje(puntaje_a,puntaje_b)
            estatico = True
            time.sleep(2)
            reiniciar_pantalla()

        # Raqueta de la derecha (B)
        # Si la pelota toca el limite del lado izquierdo
        # quiere decir que B metió gol a A
        # se debe actualizar el puntaje y reiniciar la pantalla
        if (pelota.xcor() > 340 and pelota.xcor() < 350
            ) and (pelota.ycor() < raqueta_b.ycor() + 50 and
                   pelota.ycor() > raqueta_b.ycor() - 50):
            pelota.setx(340)
            pelota.dx *= -1

        # Raqueda de la izquierda (A)
        if (pelota.xcor() < -340 and pelota.xcor() > -350
            ) and (pelota.ycor() < raqueta_a.ycor() + 50 and
                   pelota.ycor() > raqueta_a.ycor() - 50):
            pelota.setx(-340)
            pelota.dx *= -1



    except:
        break