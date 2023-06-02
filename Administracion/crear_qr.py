import qrcode

class Qr():
    def __init__(self):
        super().__init__()

    def crear_qr(self, rol, curp):
        # Generar el  objeto qr
        qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)

        # Llenar de datos el qr
        codigo = rol + "-" + curp
        qr.add_data(codigo)
        qr.make()

        # Agregar la imgaen al codigo qr
        qr_img = qr.make_image(fill_color="#25E745", back_color="#2574E7").convert("RGB")

        # Guardar la imagen en la carpeta
        if rol == "Administrativo":
            qr_img.save(f"/Users/jairaceves/Documents/Curso Python/Administracion/Administrativos/{codigo}.png")
        elif rol == "Estudiante":
            qr_img.save(f"/Users/jairaceves/Documents/Curso Python/Administracion/Estudiantes/{codigo}.png")
        elif rol == "Externo":
            qr_img.save(f"/Users/jairaceves/Documents/Curso Python/Administracion/Externos/{codigo}.png")
        elif rol == "Operativo":
            qr_img.save(f"/Users/jairaceves/Documents/Curso Python/Administracion/Operativos/{codigo}.png")
        elif rol == "Profesor":
            qr_img.save(f"/Users/jairaceves/Documents/Curso Python/Administracion/Profesores/{codigo}.png")
        else:
            qr_img.save(f"/Users/jairaceves/Documents/Curso Python/Administracion/{codigo}.png")

        # Imprimir el codigo
        print(codigo)