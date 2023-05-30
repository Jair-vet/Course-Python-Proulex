# libreria permite trabajar con archivos
import os

# Metodos
def calcular(cliente, factura, producto, precio, cantidad, iva):
    cliente = f"Cliente: {cliente}"
    factura = f"Factura: {factura}"
    producto = f"Producto: {producto}"
    calculo = (precio * cantidad) + ((precio * cantidad) * iva)
    total = f"Total a Pagar: ${calculo} MX"

    imprimir(cliente, factura, producto, total)
def imprimir(c, f, p, t):
    ticket = open("/Users/jairaceves/Documents/Curso Python/ticket.txt", "w")

    ticket.write(c + os.linesep)
    ticket.write(f + os.linesep)
    ticket.write(p + os.linesep)
    ticket.write(t + os.linesep)

    ticket.close()

    print("¡¡Ticket Generado con Exito!!")
def datos():
    try:
        cliente = str(input("Nombre del Cliente: "))
        factura = str(input("Numero de la Factura: "))
        producto = str(input("Producto: "))
        precio = float(input("Digite el Precio: "))
        cantidad = int(input("Digite la Cantidad: "))
        iva = float(0.16)

        # Metodo puede llamar a otro
        calcular(cliente, factura, producto, precio, cantidad, iva)
    except Exception:
        print("Ingresaste un valor incorrecto")

# Invocar el metodo de arranque
datos()