from tkinter import *
from tkinter.messagebox import askokcancel, showerror, showinfo

# Interfaz
sistema = Tk()
sistema.title("Calculos Aritmeticos Tkinter")
sistema.geometry("800x450+350+150")
sistema.resizable(False,False) # Para indicar que no se estire
sistema.configure(background="#2074A4")

# Variables de control
numero1 = StringVar()
numero2 = StringVar()
lbsuma_impreso = StringVar()
lbresta_impreso = StringVar()
lbmulti_impreso = StringVar()
lbdivision_impreso = StringVar()

# Metodos
def limpiar_pregunta():
    resultado = askokcancel(title="Limpiar",
                            message="¿Está seguro de limpiar los valores?")
    if resultado == True:
        limpiar()
    else:
        showinfo(title="Aviso", message="No se borraran los resultados")

def limpiar():
    lbsuma_impreso.set("El Resultado de la suma es: ")
    lbresta_impreso.set("El Resultado de la resta es: ")
    lbmulti_impreso.set("El Resultado de la multi es: ")
    lbdivision_impreso.set("El Resultado de la division es: ")
    numero1.set("")
    numero2.set("")

def operaciones():
    try:
        n1 = float(numero1.get())
        n2 = float(numero2.get())

        suma = n1 + n2
        lbsuma_impreso.set(f"El Resultado de la suma es: {round(suma, 2)}")

        resta = n1 - n2
        lbresta_impreso.set(f"El Resultado de la resta es: {round(resta, 2)}")

        multi = n1 * n2
        lbmulti_impreso.set(f"El Resultado de la multi es: {round(multi, 2)}")

        if n1!=0 and n2!=0:
            division = n1 / n2
            lbdivision_impreso.set(f"El Resultado de la division es: {round(division, 2)}")
        else:
            lbdivision_impreso.set(" No es posible realizar la operación")

        
        showinfo(title="Mensaje", message="Operaciones realizadas")

    except Exception:
        showerror(title="Advertencia", message="Los valores ingresados no son numericos")
        limpiar()


# Componentes 
# x = eje Horizonta | y = ejer Vertical
# bg = color de fondo | fg = color de la letra del componente
# 1
titulo = Label(sistema, text="Sistema de calculos aritmeticos",
               font=("Arial", 22), fg="#4C2677",background="#CAC9CB").place(x=200, y=5)
# 2
etiqueta1 = Label(sistema, text="Ingresa un numero:   ",
               font=("Arial", 16), fg="#000",background="#CAC9CB").place(x=1, y=100)
# 3
etiqueta2 = Label(sistema, text="Ingresa otro numero: ",
               font=("Arial", 16), fg="#000",background="#CAC9CB").place(x=1, y=150)
# 4
texto1 = Entry(sistema, fg="#000",background="#fff", font=("Arial", 16),
               textvariable=numero1).place(x=230, y=100)
# 5
texto2 = Entry(sistema, fg="#000",background="#fff", font=("Arial", 16),
               textvariable=numero2).place(x=230, y=150)
# Resultados 
# 6
lbsuma = Label(sistema, font=("Arial", 16), fg="#4C2677",background="#CAC9CB",
               textvariable=lbsuma_impreso).place(x=1, y=200)
lbsuma_impreso.set("El Resultado de la suma es: ")
# 7
lbresta = Label(sistema, font=("Arial", 16), fg="#4C2677",background="#CAC9CB",
               textvariable=lbresta_impreso).place(x=1, y=250)
lbresta_impreso.set("El Resultado de la resta es: ")
# 8
lbmulti = Label(sistema, font=("Arial", 16), fg="#4C2677",background="#CAC9CB",
               textvariable=lbmulti_impreso).place(x=1, y=300)
lbmulti_impreso.set("El Resultado de la multi es: ")
# 9 
lbdivision = Label(sistema, font=("Arial", 16), fg="#4C2677",background="#CAC9CB",
               textvariable=lbdivision_impreso).place(x=1, y=350)
lbdivision_impreso.set("El Resultado de la division es: ")
# 10
btnaceptar = Button(sistema, text="Aceptar", font=("Arial", 18), fg="#1AB33A",
                    command=(operaciones)).place(x=500, y=125)
# 11
btcancelar = Button(sistema, text="Cancelar", font=("Arial", 18), fg="#C12222",
                    command=(limpiar_pregunta)).place(x=600, y=125)


# ejecutar la interfaz
sistema.mainloop()