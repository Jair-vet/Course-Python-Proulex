# pip3 install pyqt5
# pip3 install pyqt5-tools
# pip3 install pandas


import sys
import pandas
import random
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon

# Crear la clase principal
class Tabla(QWidget):
    # Metodo constructor de la clase
    # Primer metodo que se ejecuta al instanciar la clase
    def __init__(self):
        super().__init__()
        # invocar todos los metodos
        self.interfaz()

    def interfaz(self):
        # ! Interfaz
        self.setFixedSize(600,600)
        self.setWindowTitle("Tabla QT")
        # self.setWindowIcon(QIcon("/Users/jairaceves/Documents/Curso Python/logo.png"))
        self.setWindowIcon(QIcon(QPixmap('logo.png')))
        self.setStyleSheet("background-color:#DCDCDC; color:#000")

        # ! Titulo
        self.titulo = QLabel(self)
        self.titulo.setText("Python Tabla QT")
        self.titulo.setGeometry(165, 20, 300, 50)
        self.titulo.setFont(QFont("Calibri Light", 18))
        self.titulo.setAlignment(QtCore.Qt.AlignCenter)
        self.titulo.setStyleSheet(
            """
            QLabel {
                background-color:#000;
                color:#fff;
                border-radius: 13px;
                border:3px solid #00FF91
            }
            """)
        
        # ! Tabla
        self.tabla = QTableWidget(self)
        self.tabla.setGeometry(10, 110, 580, 400)
        self.tabla.setFont(QFont("Calibri Light", 11))
        self.tabla.setStyleSheet(
            """
            QTableWidget {
                background-color: #7A797A;
                color: #000;
                border-radius: 9px;
                border: 3px solid #00FF91;

            }
            QTableWidget:hover {
                border: 3px solid #890D9F;
            }
            """)
        
        # Establecer numero de columnas
        self.tabla.setColumnCount(6)
        # Establecer numero de filas
        self.tabla.setRowCount(0)
        # Deshabilitar la edición
        self.tabla.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # Seleccionar todas las filas
        self.tabla.setSelectionBehavior(QAbstractItemView.SelectRows)
        # Selecionar una sola fila a la vez
        self.tabla.setSelectionMode(QAbstractItemView.SingleSelection)
        # Filas de color alternadas
        self.tabla.setAlternatingRowColors(True)
        # Alto de las filas
        self.tabla.verticalHeader().setDefaultSectionSize(20)
        # Agregar nombres a las columnas
        nombre_columnas = ("id", "Edad", "Peso", "Altura", "Presion", "Glucosa")
        self.tabla.setHorizontalHeaderLabels(nombre_columnas)

        # Aceptar
        self.btnAceptar = QPushButton(self)
        self.btnAceptar.setText("Aceptar")
        self.btnAceptar.setGeometry(100, 520, 120, 40)
        self.btnAceptar.setFont(QFont("Calibri Light", 14))
        self.btnAceptar.clicked.connect(self.cargar_datos)
        self.btnAceptar.setStyleSheet(
            """
            QPushButton {
                background-color:#fff;
                color:#000;
                border-radius: 10px;
                border:3px solid #0BEBF3
            }
            QPushButton:hover {
                background-color:#12864A; 
                color:#fff;
                border-radius: 10px;
                border:3px solid #0BEBF3
            }
            QPushButton:pressed {
                background-color:#166AA9; 
                color:#fff;
                border-radius: 10px;
                border:3px solid #0BEBF3
            }
            """)

        # Limpiar
        self.btnLimpiar = QPushButton(self)
        self.btnLimpiar.setText("Limpiar")
        self.btnLimpiar.setGeometry(240, 520, 120, 40)
        self.btnLimpiar.setFont(QFont("Calibri Light", 14))
        self.btnLimpiar.clicked.connect(self.limpiar_tabla)
        self.btnLimpiar.setStyleSheet(
            """
            QPushButton {
                background-color:#fff;
                color:#000;
                border-radius: 10px;
                border:3px solid #0BEBF3
            }
            QPushButton:hover {
                background-color:#12864A; 
                color:#fff;
                border-radius: 10px;
                border:3px solid #0BEBF3
            }
            QPushButton:pressed {
                background-color:#166AA9; 
                color:#fff;
                border-radius: 10px;
                border:3px solid #0BEBF3
            }
            """)

        # Exportar
        self.btnExportar = QPushButton(self)
        self.btnExportar.setText("Exportar")
        self.btnExportar.setGeometry(380, 520, 120, 40)
        self.btnExportar.setFont(QFont("Calibri Light", 14))
        self.btnExportar.clicked.connect(self.exportar_datos)
        self.btnExportar.setStyleSheet(
            """
            QPushButton {
                background-color:#fff;
                color:#000;
                border-radius: 10px;
                border:3px solid #0BEBF3
            }
            QPushButton:hover {
                background-color:#12864A; 
                color:#fff;
                border-radius: 10px;
                border:3px solid #0BEBF3
            }
            QPushButton:pressed {
                background-color:#166AA9; 
                color:#fff;
                border-radius: 10px;
                border:3px solid #0BEBF3
            }
            """)

        # Menu desplegable
        self.menu = QMenu()
        for indice, columna in enumerate(nombre_columnas, start=0):
            accion = QAction(columna, self.menu)
            accion.setCheckable(True) # permite que le pongamos palomita
            accion.setChecked(True) # permite que se mantengan las palomitas
            accion.setData(indice)
            self.menu.addAction(accion)

        # Vincular el metodo al menu/boton
        self.menu.triggered.connect(self.mostrar_ocultar)

        # Boton Menu
        self.btnMenu = QPushButton(self)
        self.btnMenu.setText("Menu")
        self.btnMenu.setMenu(self.menu)
        self.btnMenu.setGeometry(10, 70, 200, 30)
        self.btnMenu.setFont(QFont("Calibri Light", 12))
        self.btnMenu.setStyleSheet(
            """
            QPushButton {
                background-color:#fff;
                color:#000;
                border-radius: 10px;
                border:3px solid #0BEBF3
            }
            QPushButton:hover {
                background-color:#12864A; 
                color:#fff;
                border-radius: 10px;
                border:3px solid #0BEBF3
            }
            QPushButton:pressed {
                background-color:#166AA9; 
                color:#fff;
                border-radius: 10px;
                border:3px solid #0BEBF3
            }
            """)


    def cargar_datos(self):
        try:
            # Limpiar tabla
            self.tabla.clearContents()
            # Variable para contruir las filas
            fila = 0
            # Cantidad de filas a generar
            cantidad = 1000
            # Ciclo para cargar los datos
            for i in range(cantidad):
                # Agregar una nueva fila
                self.tabla.setRowCount(fila + 1)
                # Añadir datos a cada celda de la fila
                
                # ID
                self.tabla.setItem(fila, 0, QTableWidgetItem(str(i + 1)))
                # Edad
                self.tabla.setItem(fila, 1, QTableWidgetItem(str(random.randint(18, 65))))
                # Peso
                self.tabla.setItem(fila, 2, QTableWidgetItem(str(random.randint(60, 100))))
                # Altura
                self.tabla.setItem(fila, 3, QTableWidgetItem(str(round(random.uniform(0,1) + 1, 2))))
                # Presión
                self.tabla.setItem(fila, 4, QTableWidgetItem(str(random.randint(80, 150))))
                # Glucosa
                self.tabla.setItem(fila, 5, QTableWidgetItem(str(random.randint(140,199))))

                # Icremento del Iterador
                fila += 1
            
            # Aviso
            # QMessageBox.information(self, "Aviso se cargaron los datos con exito")


        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))

    def limpiar_tabla(self):
        pregunta = QMessageBox.question(self,"Limpiar", "¿Desea Limpiar la Tabla?")
        if pregunta == QMessageBox.Yes:
            self.tabla.clearContents()
        else:
            QMessageBox.information(self,"Aviso", "No se limpiarán los Datos")

    def exportar_datos(self):
        try: 
            # Crear una lista para los encabezados
            encabezados = []
            # Recorer las columnas
            for c in range(self.tabla.model().columnCount()):
                # Agregar el valor string de las columnas al arreglo
                encabezados.append(self.tabla.horizontalHeaderItem(c).text())
            
            # Enviar los encabezados a un DataFrame
            df = pandas.DataFrame(columns=encabezados)

            # Recorrer las Filas
            for fila in range(self.tabla.model().rowCount()):
                # Recorrer las celdas de cada fila
                for celda in range(self.tabla.model().columnCount()):
                    # Agregar al df las celdas de cada fila
                    # at = acceder a una coordenada en especifico
                    df.at[fila, encabezados[celda]] = self.tabla.item(fila,celda).text()

            # Exportar
            df.to_html(r"/Users/jairaceves/Documents/Curso Python/exportacion.html")
            df.to_csv(r"/Users/jairaceves/Documents/Curso Python/exportacion.csv")

            QMessageBox.information(self,"Exportar","Exportacion Exitosa")

        except Exception as e:
            QMessageBox.warning(self, "Error", str(e))

    def mostrar_ocultar(self, accion):
        columna = accion.data()

        if accion.isChecked():
            self.tabla.setColumnHidden(columna, False)
        else:
            self.tabla.setColumnHidden(columna, True)
        
# Estructura que ejecuta la App
if __name__ == "__main__":
    # Instancia para iniciar la app
    app = QApplication(sys.argv)
    # Instancia de la clase Ventana
    tabla = Tabla()
    # Mostrar la tabla
    tabla.show()
    # Ejecutar la app
    app.exec()
