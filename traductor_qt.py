# pip3 install deep-translator
# pip3 install gtts
# pip3 install playsound

# Importaciones
import sys
import os
from playsound import *
from deep_translator import GoogleTranslator
from gtts import gTTS
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore

# Clase Principal
class Ventana(QWidget):
     # Primer metodo que se ejecuta al instanciar la clase
     # Metodo constructor de la clase
    # Primer metodo que se ejecuta al instanciar la clase
    def __init__(self):
        super().__init__()
        # invocar todos los metodos
        self.interfaz()

    def interfaz(self):
        # ! Interfaz
        self.setFixedSize(1200,700)
        self.setWindowTitle("Traductor QT")
        self.setStyleSheet("background-color:#0E68AB; color:#000")

        # ! Titulo
        self.IbTitulo = QLabel(self)
        self.IbTitulo.setText("Traductor QT Python")
        self.IbTitulo.setGeometry(400, 30, 400, 50)
        self.IbTitulo.setFont(QFont("Calibri Light", 18))
        self.IbTitulo.setAlignment(QtCore.Qt.AlignCenter)
        self.IbTitulo.setStyleSheet(
            """
            QLabel {
                background-color:#000;
                color:#fff;
                border-radius: 13px;
                border:3px solid #00FF91
            }
            """)

        # ! Entrada
        self.cbEntrada = QComboBox(self)
        self.cbEntrada.addItem("es")
        self.cbEntrada.addItem("en")
        self.cbEntrada.addItem("fr")
        self.cbEntrada.addItem("ja")
        self.cbEntrada.addItem("de")
        self.cbEntrada.setGeometry(20, 70, 100, 30)
        self.cbEntrada.setFont(QFont("Calibri Light", 18))
        self.cbEntrada.setStyleSheet(
            """
            QComboBox {
                background-color: #fff;
                color: #000;
                border-radius: 9px;
                border: 3px solid #00FF91;

            }
            """)
        
        # ! Salida
        self.cbSalida = QComboBox(self)
        self.cbSalida.addItem("es")
        self.cbSalida.addItem("en")
        self.cbSalida.addItem("fr")
        self.cbSalida.addItem("ja")
        self.cbSalida.addItem("de")
        self.cbSalida.setGeometry(1080, 70, 100, 30)
        self.cbSalida.setFont(QFont("Calibri Light", 18))
        self.cbSalida.setStyleSheet(
            """
            QComboBox {
                background-color: #fff;
                color: #000;
                border-radius: 9px;
                border: 3px solid #00FF91;

            }
            """)
        

        # ! Cajas de Texto 1
        self.txtEntrada = QTextEdit("Escribe aquí...", self)
        self.txtEntrada.setGeometry(20, 180, 480, 400)
        self.txtEntrada.setFont(QFont("Calibri Light", 18))
        self.txtEntrada.setStyleSheet(
            """
            QTextEdit {
                background-color: #fff;
                color: #000;
                border-radius: 9px;
                border: 3px solid #00FF91;

            }
            """)
        
        # ! Caja de Texto 2
        self.txtSalida = QTextEdit(self)
        self.txtSalida.setGeometry(710, 180, 480, 400)
        self.txtSalida.setFont(QFont("Calibri Light", 18))
        self.txtSalida.setStyleSheet(
            """
            QTextEdit {
                background-color: #fff;
                color: #000;
                border-radius: 9px;
                border: 3px solid #00FF91;

            }
            """)
        

        # ! Botones
        # Traducir
        self.btnTraducir = QPushButton(self)
        self.btnTraducir.setText("Traducir")
        self.btnTraducir.setGeometry(530, 250, 130, 40)
        self.btnTraducir.setFont(QFont("Calibri Light", 14))
        # self.btnTraducir.clicked.connect()
        self.btnTraducir.setStyleSheet(
            """
            QPushButton {
                background-color:#fff;
                color:#000;
                border-radius: 10px;
                border:3px solid #00FF91
            }
            
            """)
       
        # Traducir
        self.btnLimpiar = QPushButton(self)
        self.btnLimpiar.setText("Limpiar")
        self.btnLimpiar.setGeometry(530, 300, 130, 40)
        self.btnLimpiar.setFont(QFont("Calibri Light", 14))
        # self.btnLimpiarir.clicked.connect()
        self.btnLimpiar.setStyleSheet(
            """
            QPushButton {
                background-color:#fff;
                color:#000;
                border-radius: 10px;
                border:3px solid #00FF91
            }
            
            """)
        
        # Guardar
        self.btnGuardar = QPushButton(self)
        self.btnGuardar.setText("Guardar")
        self.btnGuardar.setGeometry(530, 350, 130, 40)
        self.btnGuardar.setFont(QFont("Calibri Light", 14))
        # self.btnGuardar.clicked.connect()
        self.btnGuardar.setStyleSheet(
            """
            QPushButton {
                background-color:#fff;
                color:#000;
                border-radius: 10px;
                border:3px solid #00FF91
            }
            
            """)
        
        # Escuchar
        self.btnEscuchar = QPushButton(self)
        self.btnEscuchar.setText("Escuchar")
        self.btnEscuchar.setGeometry(530, 400, 130, 40)
        self.btnEscuchar.setFont(QFont("Calibri Light", 14))
        # self.btnEscuchar.clicked.connect()
        self.btnEscuchar.setStyleSheet(
            """
            QPushButton {
                background-color:#fff;
                color:#000;
                border-radius: 10px;
                border:3px solid #00FF91
            }
            
            """)



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
