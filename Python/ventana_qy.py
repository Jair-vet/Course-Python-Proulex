# pip3 install pyqt5
# pip3 install pyqt5-tools


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

# Crear la clase principal
class Ventana(QWidget):
    # Metodo constructor de la clase
    # Primer metodo que se ejecuta al instanciar la clase
    def __init__(self):
        super().__init__()
        # invocar todos los metodos
        self.interfaz()

    def interfaz(self):
        # ! Ventana
        self.resize(400,200)
        self.setMaximumSize(400,200)
        self.setWindowTitle("Ventana QT")
        self.setFont(QFont("Arial", 18))
        self.setStyleSheet("background-color:#000; color:#fff")

        
# Estructura que ejecuta la App
if __name__ == "__main__":
    # Instancia para iniciar la app
    app = QApplication(sys.argv)
    # Instancia de la clase Ventana
    ventana = Ventana()
    # Mostrar la ventana
    ventana.show()
    # Ejecutar la app
    app.exec()
