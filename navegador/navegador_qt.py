# pip3 install PyQtWebKit
# pip3 install PyQtWebEngine

# Impotar las librerias
import sys
from PyQt5.QtGui import *
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWebEngineWidgets import QWebEngineView

# Clases
class Navegador(object):
    def interfaz(self, ventana):
        # Ventana
        ventana.resize(1000,700)
        ventana.setWindowTitle("Navegador Python")
        ventana.setStyleSheet("background-color: #0E4DA8; color: #fff")

        # Titulo
        self.titulo = QtWidgets.QLabel(ventana)
        self.titulo.setText("Navegador Python")
        self.titulo.setGeometry(120, 10, 750, 50)
        self.titulo.setFont(QFont("Calibri Light", 18))
        self.titulo.setAlignment(QtCore.Qt.AlignCenter)
        self.titulo.setStyleSheet(
            """
            QLabel {
                background-color:#9C6BB0;
                color:#fff;
                border-radius: 13px;
                border:3px solid #6D0EAB
            }
            """)


        # Marco
        self.marco = QWebEngineView(ventana)
        self.marco.setGeometry(10,70,980,550)


        # Etiqueta URL
        self.lbUrl = QtWidgets.QLabel(ventana)
        self.lbUrl.setText("Ingreasa El Url...")
        self.lbUrl.setGeometry(120, 200, 750, 50)
        self.lbUrl.setFont(QFont("Calibri Light", 20))
        self.lbUrl.setAlignment(QtCore.Qt.AlignCenter)
        self.lbUrl.setStyleSheet(
            """
            QLabel {
                background-color:#fff;
                font-weight: bold;
                color:#6D0EAB;
                border-radius: 13px;
                border:none
            }
            """)


        # ! Caja de texto URL
        self.txtUrl = QtWidgets.QLineEdit(ventana)
        self.txtUrl.setText("")
        self.txtUrl.setGeometry(200, 250, 600, 50)
        self.txtUrl.setFont(QFont("Calibri Light", 18))
        self.txtUrl.setAlignment(QtCore.Qt.AlignCenter)
        self.txtUrl.setStyleSheet(
            """
            QLineEdit {
                background-color:#BFCCD2;
                color:#000;
                border-radius: 8px;
            }
            QLineEdit:focus {
                outline: 0;
            }
            
            """)


        # ! Boton Aceptar
        self.btnAceptar = QtWidgets.QPushButton(ventana)
        self.btnAceptar.setText("Aceptar")
        self.btnAceptar.setGeometry(280, 350, 100, 40)
        self.btnAceptar.setFont(QFont("Calibri Light", 18))
        self.btnAceptar.setStyleSheet(
            """
            QPushButton {
                background-color:#147522;
                color: #fff;
                font-weight: bold;
                border-radius: 10px;
            }
            """)


        # ! Boton Cancelar
        self.btnCancelar = QtWidgets.QPushButton(ventana)
        self.btnCancelar.setText("Cancelar")
        self.btnCancelar.setGeometry(600, 350, 100, 40)
        self.btnCancelar.setFont(QFont("Calibri Light", 18))
        self.btnCancelar.setStyleSheet(
            """
            QPushButton {
                background-color: #f34079;
                color: #fff;
                font-weight: bold;
                border-radius: 10px;
            }
            """)


class LlamarNavegador(QDialog):
    def __init__(self):
        super().__init__()
        self.navegador = Navegador()
        self.navegador.interfaz(self)

# Estructura de ejecución
if __name__ == "__main__":
    app = QApplication(sys.argv)
    llamar = LlamarNavegador()
    llamar.show()
    app.exec()