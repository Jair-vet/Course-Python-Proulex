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

        # ! Botones
        btn1 = QPushButton(self)
        btn1.setText("Boton 1")
        btn1.setGeometry(130, 50, 150, 40)
        btn1.setFont(QFont("Arial", 18))
        btn1.setStyleSheet(
            """
            QPushButton {
                background-color:#fff;
                color:#000;
                border-radius: 10px;
                border:3px solid #0BEBF3
            }
            QPushButton:hover {
                background-color:#227BC1; 
                color:#22C1B7;
                border-radius: 10px;
                border:3px solid #0BEBF3
            }
            QPushButton:pressed {
                background-color:#7B22C1; 
                color:#C88BF9;
                border-radius: 10px;
                border:3px solid #0BEBF3
            }
            """)
        
        btn2 = QPushButton(self)
        btn2.setText("Boton 2")
        btn2.setGeometry(130, 100, 150, 40)
        btn2.setFont(QFont("Arial", 18))
        btn2.setStyleSheet(
            """
            QPushButton {
                background-color:#fff;
                color:#000;
                border-radius: 10px;
                border:3px solid #0BEBF3
            }
            QPushButton:hover {
                background-color:#227BC1; 
                color:#22C1B7;
                border-radius: 10px;
                border:3px solid #0BEBF3
            }
            QPushButton:pressed {
                background-color:#7B22C1; 
                color:#C88BF9;
                border-radius: 10px;
                border:3px solid #0BEBF3
            }
            """)

        # Vincular los boones al metodo
        btn1.clicked.connect(self.boton_click)
        btn2.clicked.connect(self.boton_click)

    # ! Ventana Emergente
    def boton_click(self):
        texto_boton = self.sender().text()
        QMessageBox.information(self, "Titulo", f"Diste clic:{texto_boton}")

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
