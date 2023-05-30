# pip3 install pytube
# pip3 install pillow
# pip3 install image

# Fuente: https://pytube.io/en/latest/

# Importar librerias
from tkinter import *
from pytube import YouTube
from PIL import ImageTk, Image

# Metodos
def descargar():
    pass

def cerrar():
    pass

# Interfaz
# geometry (ancho, alto, posición H, posición V)
interfaz = Tk()
interfaz.title("Descargar videos")
interfaz.geometry("650x400+200+150")
interfaz.resizable(False,False)
interfaz.config(bg="#000000")

# Variable de control
# Es un objeto que permite comunicar la interfaz con el lenguaje
video = StringVar()

# Imagen

imagen = Image.open(r"/Users/jairaceves/Documents/Curso Python/Modelo Canvas.png")
imagen = imagen.resize((250,180))
objeto_imagen = ImageTk.PhotoImage(imagen)
marco_imagen = Label(interfaz, image=objeto_imagen, bg="#000000", compound="center").place(x=200,y=150)

# Titulo
titulo = Label(interfaz, text="Descargador Pytube", bg="#000000", fg="#E10000", compound="center", font=("Arial",22,"bold"))

titulo.place(x=180, y=10)

# Enlace etiqueta
enlace_etiqueta = Label(interfaz, text="Enlace:", bg="#000000", fg="#E10000", compound="center", font=("Arial",14,"bold"))

enlace_etiqueta.place(x=10, y=80)

# Enlace caja
enlace_caja = Entry(interfaz, text="Escribe aquí...", bg="#FFFFFF", fg="#0014E1", font=("Arial",14,"bold"), width=50, textvariable=video)

enlace_caja.place(x=90, y=80)

# Botones
aceptar = Button(interfaz, text="Descargar", width=20, height=1, font=("Arial",12,"bold"), command=descargar).place(x=100, y=350)

cancelar = Button(interfaz, text="Cancelar", width=20, height=1, font=("Arial",12,"bold"), command=cerrar).place(x=350, y=350)

# Ejecutar la interfaz
# El mainloop siempre tiene que ir hasta el final
interfaz.mainloop()