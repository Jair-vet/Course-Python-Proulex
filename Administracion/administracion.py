# Librerias Graficas
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *
from PyQt5.QtPrintSupport import *
from PyQt5.QtCore import *
from PyQt5 import QtCore
import sys

# Importar clase del archivo crear_qr
from crear_qr import *

# Crear la clase principal
class Administracion(QMainWindow):
    # Metodo constructor de la clase
    def __init__(self):
        super().__init__()
        # invocar todos los metodos
        self.interfaz()

    # ! Interfaz
    def interfaz(self):
        # Ventana
        self.setFixedSize(500,550)
        self.setWindowTitle("Generador de credenciales")
        self.setStyleSheet("background-color:#0E68AB; color:#000")

         # ! Titulo
        self.IbTitulo = QLabel(self)
        self.IbTitulo.setText("Generar credencial QR")
        self.IbTitulo.setGeometry(120, 10, 250, 50)
        self.IbTitulo.setFont(QFont("Calibri Light", 18))
        self.IbTitulo.setAlignment(QtCore.Qt.AlignCenter)
        self.IbTitulo.setStyleSheet(
            """
            QLabel {
                background-color:#000;
                color:#fff;
                border-radius: 13px;
                border:3px solid #6D0EAB
            }
            """)


        # ! Paterno
        self.IbPaterno = QLabel(self)
        self.IbPaterno.setText("Paterno:")
        self.IbPaterno.setGeometry(10, 80, 150, 40)
        self.IbPaterno.setFont(QFont("Calibri Light", 18))
        self.IbPaterno.setAlignment(QtCore.Qt.AlignCenter)
        self.IbPaterno.setStyleSheet(
            """
            QLabel {
                background-color:#000;
                color:#fff;
                border-radius: 13px;
                border:3px solid #6D0EAB
            }
            """)
        # QLineEdit
        self.txtPaterno = QLineEdit(self)
        self.txtPaterno.setGeometry(180, 80, 300, 40)
        self.txtPaterno.setFont(QFont("Consolas", 18))
        self.txtPaterno.setStyleSheet(
            """
                QLineEdit {
                    background-color:#DCDCDC;
                    color:#000;
                    border-radius: 13px;
                    border:3px solid #25E745
                }
            """)
        

        # ! Materno
        self.IbMaterno = QLabel(self)
        self.IbMaterno.setText("Materno:")
        self.IbMaterno.setGeometry(10, 130, 150, 40)
        self.IbMaterno.setFont(QFont("Calibri Light", 18))
        self.IbMaterno.setAlignment(QtCore.Qt.AlignCenter)
        self.IbMaterno.setStyleSheet(
            """
            QLabel {
                background-color:#000;
                color:#fff;
                border-radius: 13px;
                border:3px solid #6D0EAB
            }
            """)
        # QLineEdit
        self.txtMaterno = QLineEdit(self)
        self.txtMaterno.setGeometry(180, 130, 300, 40)
        self.txtMaterno.setFont(QFont("Consolas", 18))
        self.txtMaterno.setStyleSheet(
            """
                QLineEdit {
                    background-color:#DCDCDC;
                    color:#000;
                    border-radius: 13px;
                    border:3px solid #25E745
                }
            """)
        

        # ! Nombre
        self.IbNombre = QLabel(self)
        self.IbNombre.setText("Nombre:")
        self.IbNombre.setGeometry(10, 180, 150, 40)
        self.IbNombre.setFont(QFont("Calibri Light", 18))
        self.IbNombre.setAlignment(QtCore.Qt.AlignCenter)
        self.IbNombre.setStyleSheet(
            """
            QLabel {
                background-color:#000;
                color:#fff;
                border-radius: 13px;
                border:3px solid #6D0EAB
            }
            """)
        # QLineEdit
        self.txtNombre = QLineEdit(self)
        self.txtNombre.setGeometry(180, 180, 300, 40)
        self.txtNombre.setFont(QFont("Consolas", 18))
        self.txtNombre.setStyleSheet(
            """
                QLineEdit {
                    background-color:#DCDCDC;
                    color:#000;
                    border-radius: 13px;
                    border:3px solid #25E745
                }
            """)
        

        # ! Edad
        self.IbEdad = QLabel(self)
        self.IbEdad.setText("Edad:")
        self.IbEdad.setGeometry(10, 230, 150, 40)
        self.IbEdad.setFont(QFont("Calibri Light", 18))
        self.IbEdad.setAlignment(QtCore.Qt.AlignCenter)
        self.IbEdad.setStyleSheet(
            """
            QLabel {
                background-color:#000;
                color:#fff;
                border-radius: 13px;
                border:3px solid #6D0EAB
            }
            """)
        # QLineEdit
        self.txtEdad = QLineEdit(self)
        self.txtEdad.setGeometry(180, 230, 300, 40)
        self.txtEdad.setFont(QFont("Consolas", 18))
        self.txtEdad.setStyleSheet(
            """
                QLineEdit {
                    background-color:#DCDCDC;
                    color:#000;
                    border-radius: 13px;
                    border:3px solid #25E745
                }
            """)
        

        # ! Rol
        self.IbRol = QLabel(self)
        self.IbRol.setText("Rol:")
        self.IbRol.setGeometry(10, 280, 150, 40)
        self.IbRol.setFont(QFont("Calibri Light", 18))
        self.IbRol.setAlignment(QtCore.Qt.AlignCenter)
        self.IbRol.setStyleSheet(
            """
            QLabel {
                background-color:#000;
                color:#fff;
                border-radius: 13px;
                border:3px solid #6D0EAB
            }
            """)
        # QComboBox
        self.cbrol = QComboBox(self)
        self.cbrol.addItem("Administrativo")
        self.cbrol.addItem("Estudiante")
        self.cbrol.addItem("Externo")
        self.cbrol.addItem("Operativo")
        self.cbrol.addItem("Profesor")
        self.cbrol.setGeometry(180, 280, 300, 40)
        self.cbrol.setFont(QFont("Consolas", 18))
        self.cbrol.setStyleSheet(
            """
            QComboBox {
                background-color:#DCDCDC;
                color:#000;
                border-radius: 13px;
                border:3px solid #25E745
            }
            """)
        

        # ! Correo
        self.IbCorreo = QLabel(self)
        self.IbCorreo.setText("Correo:")
        self.IbCorreo.setGeometry(10, 330, 150, 40)
        self.IbCorreo.setFont(QFont("Calibri Light", 18))
        self.IbCorreo.setAlignment(QtCore.Qt.AlignCenter)
        self.IbCorreo.setStyleSheet(
            """
            QLabel {
                background-color:#000;
                color:#fff;
                border-radius: 13px;
                border:3px solid #6D0EAB
            }
            """)
        # QLineEdit
        self.txtCorreo = QLineEdit(self)
        self.txtCorreo.setGeometry(180, 330, 300, 40)
        self.txtCorreo.setFont(QFont("Consolas", 18))
        self.txtCorreo.setStyleSheet(
            """
                QLineEdit {
                    background-color:#DCDCDC;
                    color:#000;
                    border-radius: 13px;
                    border:3px solid #25E745
                }
            """)
        

        # ! CURP
        self.IbCurp = QLabel(self)
        self.IbCurp.setText("Curp:")
        self.IbCurp.setGeometry(10, 380, 150, 40)
        self.IbCurp.setFont(QFont("Calibri Light", 18))
        self.IbCurp.setAlignment(QtCore.Qt.AlignCenter)
        self.IbCurp.setStyleSheet(
            """
            QLabel {
                background-color:#000;
                color:#fff;
                border-radius: 13px;
                border:3px solid #6D0EAB
            }
            """)
        # QLineEdit
        self.txtCurp = QLineEdit(self)
        self.txtCurp.setGeometry(180, 380, 300, 40)
        self.txtCurp.setFont(QFont("Consolas", 18))
        self.txtCurp.setStyleSheet(
            """
                QLineEdit {
                    background-color:#DCDCDC;
                    color:#000;
                    border-radius: 13px;
                    border:3px solid #25E745
                }
            """)
        

        # Botones
        # ! Registrar
        self.btnRegistrar = QPushButton(self)
        self.btnRegistrar.setText("Registrar")
        self.btnRegistrar.setGeometry(100, 450, 130, 40)
        self.btnRegistrar.setFont(QFont("Calibri Light", 18))
        self.btnRegistrar.setStyleSheet(
            """
            QPushButton {
                background-color:#fff;
                color:#000;
                border-radius: 10px;
                border:3px solid #00FF91
            }
            QPushButton:hover {
                background-color:#12864A; 
                color:#fff;
                border-radius: 10px;
                border:3px solid #0BEBF3
            }
            
            """)
        
        # ! Limpiar
        self.btnLimpiar = QPushButton(self)
        self.btnLimpiar.setText("Limpiar")
        self.btnLimpiar.setGeometry(300, 450, 130, 40)
        self.btnLimpiar.setFont(QFont("Calibri Light", 18))
        self.btnLimpiar.setStyleSheet(
            """
            QPushButton {
                background-color:#fff;
                color:#000;
                border-radius: 10px;
                border:3px solid #00FF91
            }
            QPushButton:hover {
                background-color:#12864A; 
                color:#fff;
                border-radius: 10px;
                border:3px solid #0BEBF3
            }
            
            """)
       


# Estructura que ejecuta la App
if __name__ == "__main__":
    # Instancia para iniciar la app
    app = QApplication(sys.argv)
    # Instancia de la clase Ventana
    administracion = Administracion()
    # Mostrar la ventana
    administracion.show()
    # Ejecutar la app
    app.exec()