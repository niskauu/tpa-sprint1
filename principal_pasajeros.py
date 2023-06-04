import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QHBoxLayout, QPushButton, QWidget, QGridLayout, QTableWidget, QTableWidgetItem, QHeaderView
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from agregar_pasajero import*
from Pulsera import *
from ver_pulsera import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi Ventana")
        self.setFixedSize(350,200)

        widget = QWidget()
        layout = QGridLayout()
        grid_logo = QGridLayout()

        layout.addLayout(grid_logo,0,0)

        # Agregar la imagen en la esquina superior izquierda
        imagen_label = QLabel(self)
        pixmap = QPixmap("hotel.jpg")  
        pixmap = pixmap.scaled(30, 30)  
        imagen_label.setPixmap(pixmap)
        
        grid_logo.addWidget(imagen_label, 0,0)

        # Agregar el QLabel para el nombre del hotel
        hotel_label = QLabel("Hotel CTh", self)
        grid_logo.addWidget(hotel_label, 0, 1, 1, 7)
        widget.setLayout(layout)
        self.setCentralWidget(widget)


        self.table = QTableWidget(0, 2)  

        self.table.setHorizontalHeaderLabels(["Pasajero", "Pulsera"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.table.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        
        
        # Agregar botones pasajeros
        agregar_pasajero_button = QPushButton("Agregar pasajero")
        eliminar_pasajero = QPushButton("Eliminar pasajero")
        layout.addWidget(agregar_pasajero_button,1,0)
        layout.addWidget(eliminar_pasajero,2,0)
        agregar_pasajero_button.clicked.connect(self.mostrar_agregar_pasajero)
        eliminar_pasajero.clicked.connect(self.eliminar_pasajero)

        # Agregar botones de cancelar y aceptar
        cancelar_button = QPushButton("Cancelar")
        actualizar_button = QPushButton("Actualizar")

        cancelar_button.clicked.connect(self.close)
        
        layout.addWidget(cancelar_button, 4, 0, 1, 1)
        layout.addWidget(actualizar_button, 4, 1, 1, 1) 

        layout.addWidget(self.table, 1, 1, 3, 2)
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def mostrar_ventana_ver_pulsera(self):
        self.ventana_ver_pulsera = VentanaPulsera()
        self.ventana_ver_pulsera.show()
        # button = self.sender()
        # row = button.property("tableRow")
        # col = button.property("tableColumn")
        # print(f"Button clicked in cell ({row}, {col})")

    def mostrar_agregar_pasajero(self):
        self.ventana_agregar_pasajero = AgregarPasajero()
        self.ventana_agregar_pasajero.mi_signal.connect(self.agregar_pasajero)
        self.ventana_agregar_pasajero.show()
    
    def eliminar_pasajero(self):
        selected_row = self.table.currentRow()
        self.table.removeRow(selected_row)
    
    def agregar_pasajero(self):
        row_count = self.table.rowCount()
        self.table.insertRow(row_count)
        item = QTableWidgetItem(self.ventana_agregar_pasajero.nombre)
        item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)
        self.table.setItem(row_count, 0, item)

        button = QPushButton("Ver Pulsera")
        button.clicked.connect(self.mostrar_ventana_ver_pulsera)
        button.setProperty("tableRow", row_count)
        button.setProperty("tableColumn", 1)
        layout_widget = QWidget()
        button_layout = QHBoxLayout(layout_widget)
        button_layout.addWidget(button)
        button_layout.setAlignment(button, Qt.AlignmentFlag.AlignCenter)
        button_layout.setContentsMargins(0, 0, 0, 0)
        layout_widget.setLayout(button_layout)
        self.table.setCellWidget(row_count, 1, layout_widget)

   
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
