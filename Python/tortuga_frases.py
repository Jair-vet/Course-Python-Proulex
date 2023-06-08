import turtle
import random

def generar_frase():
    frases = ["DevOps", "React.Js", "Angular", "Typescript", "Json", "XJSX", "Vue.JS", "JavaScript",
              "Next.Js", "Tailwindcss", "Html", "NodeJs", "Nest.Js", "MongoDB", "Python"]
    return random.choice(frases)

def frase_aleatoria():
    turtle.clear()
    turtle.penup()
    x = random.randint(-200,200)
    y = random.randint(-200,200)
    turtle.goto(x,y)
    turtle.pendown()
    turtle.color(random.choice(["red", "blue", "green", "yellow", "black", "pink", "orange", "skyBlue"]))
    turtle.write(generar_frase(), align="center", font=("Consolas", 18,"bold"))


# Crear la ventana
ventana = turtle.Screen()
ventana.title("Tortuga Figuras")
ventana.bgcolor("white")

# Configuracion de los listen
ventana.listen()
ventana.onkeypress(frase_aleatoria, "Return")

# Mantener abierta la ventana
ventana.mainloop()