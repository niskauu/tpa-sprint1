import sys
from PyQt6.QtWidgets import QWidget , QLabel , QLineEdit , QHBoxLayout ,QVBoxLayout , QPushButton ,QDateEdit , QSpinBox , QMessageBox , QDialog
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt 
from costos import costos
from principal_pasajeros import *

class ventanaprincipal(QDialog):   

    def __init__(self):
        super().__init__()
        self.inicializarui()

    def inicializarui(self):
        self.setGeometry(100,100,350,250)   
        self.setWindowTitle("Sistema de cobros de estadia")
        self.contenido()
        self.show()     

    def contenido(self):

        logo_label = QLabel()
        logo_pixmap = QPixmap("./hotel/logo.png")
        logo_pixmap = logo_pixmap.scaled(30, 30, Qt.AspectRatioMode.KeepAspectRatio)
        logo_label.setPixmap(logo_pixmap)
        logo_label.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)

        nombreHotel_label = QLabel("Hotel CTCh")
        nombreHotel_label.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
        nombreHotel_label.setFixedHeight(30) 

        texto1_label = QLabel("Validar datos de reserva")

        nombre_label = QLabel("Nombre")
        nombre_label.setFixedWidth(120)
        self.nombre_input = QLineEdit()

        fechaN_label = QLabel("Fecha de Nacimiento")
        fechaN_label.setFixedWidth(120)
        self.fechaN_input = QDateEdit()

        habitacion_label = QLabel("Habitaciones")
        habitacion_label.setFixedWidth(120)
        self.habitacion_input = QSpinBox()

        estadia_label = QLabel("Tiempo de estadia")
        estadia_label.setFixedWidth(120)
        self.estadia_input = QLineEdit()

        fecha_label = QLabel("fecha")
        fecha_label.setFixedWidth(120)
        self.fecha_input = QDateEdit()

        pasajeros_button = QPushButton("Pasajeros")
        pasajeros_button.clicked.connect(self.iniciarVentanaPasajero)

        costo_button = QPushButton("Calcular costo de estadia")
        costo_button.clicked.connect(self.iniciarventanacostos)

        texto2_label = QLabel("registrar tarjeta de credito")

        titular_label = QLabel("Titular de la tarjeta")
        self.nombretarjeta_input = QLineEdit()

        numeros_label = QLabel("Numero de trajeta")
        self.numtarjeta_input = QLineEdit()

        expiracion_label = QLabel("Fecha de expiracion")
        self.expiracion_input = QDateEdit()

        cvc_label = QLabel("CVC")
        self.cvc_input = QLineEdit()

        guardar_button = QPushButton("Guardar datos")
        guardar_button.clicked.connect(self.guardar_datos)

        Hlayout = QHBoxLayout()
        Hlayout.addWidget(logo_label)
        Hlayout.addWidget(nombreHotel_label)
        Hlayout.addStretch()

        Hlayout1 = QHBoxLayout()
        Hlayout1.addWidget(nombre_label)
        Hlayout1.addWidget(self.nombre_input)

        Hlayout2 = QHBoxLayout()
        Hlayout2.addWidget(fechaN_label)
        Hlayout2.addWidget(self.fechaN_input)

        Hlayout3 = QHBoxLayout()
        Hlayout3.addWidget(habitacion_label)
        Hlayout3.addWidget(self.habitacion_input)

        Hlayout4 = QHBoxLayout()
        Hlayout4.addWidget(estadia_label)
        Hlayout4.addWidget(self.estadia_input)

        Hlayout5 = QHBoxLayout()
        Hlayout5.addWidget(fecha_label)
        Hlayout5.addWidget(self.fecha_input)

        Hlayout6 = QHBoxLayout()
        Hlayout6.addWidget(pasajeros_button)
        Hlayout6.addWidget(costo_button)

        Hlayout7 = QHBoxLayout()
        Hlayout7.addWidget(expiracion_label)
        Hlayout7.addWidget(cvc_label)

        Hlayout8 = QHBoxLayout()
        Hlayout8.addWidget(self.expiracion_input)
        Hlayout8.addWidget(self.cvc_input)

        Vlayout = QVBoxLayout()
        Vlayout.addLayout(Hlayout)
        Vlayout.addWidget(texto1_label)
        Vlayout.addLayout(Hlayout1)
        Vlayout.addLayout(Hlayout2)
        Vlayout.addLayout(Hlayout3)
        Vlayout.addLayout(Hlayout4)
        Vlayout.addLayout(Hlayout5)
        Vlayout.addLayout(Hlayout6)
        Vlayout.addWidget(texto2_label)
        Vlayout.addWidget(titular_label)
        Vlayout.addWidget(self.nombretarjeta_input)
        Vlayout.addWidget(numeros_label)
        Vlayout.addWidget(self.numtarjeta_input)
        Vlayout.addLayout(Hlayout7)
        Vlayout.addLayout(Hlayout8)
        Vlayout.addWidget(guardar_button)

        self.setLayout(Vlayout)

    def guardar_datos(self):
        rutadatos = "./hotel/guardado.txt"
        archivo = open(rutadatos,"a")

        nombre = self.nombre_input.text()
        fecha_nacimiento = self.fechaN_input.text()
        habitaciones = self.habitacion_input.text()
        tiempo_estadia = self.estadia_input.text()
        fecha = self.fecha_input.text()
        titular_tarjeta = self.nombretarjeta_input.text()
        numero_tarjeta = self.numtarjeta_input.text()
        fecha_expiracion = self.expiracion_input.text()
        cvc = self.cvc_input.text()

        archivo.write(f"Nombre: {nombre}\n")
        archivo.write(f"Fecha de Nacimiento: {fecha_nacimiento}\n")
        archivo.write(f"Habitaciones: {habitaciones}\n")
        archivo.write(f"Tiempo de Estadia: {tiempo_estadia}\n")
        archivo.write(f"Fecha: {fecha}\n")
        archivo.write(f"Titular de la Tarjeta: {titular_tarjeta}\n")
        archivo.write(f"Numero de Tarjeta: {numero_tarjeta}\n")
        archivo.write(f"Fecha de Expiracion: {fecha_expiracion}\n")
        archivo.write(f"CVC: {cvc}\n")

        QMessageBox.information(self, "Datos guardados", "Los datos se han guardado correctamente", QMessageBox.StandardButton.Ok, QMessageBox.StandardButton.Ok)
        archivo.close()

    def iniciarventanacostos(self):
        self.ventanacostos = costos()
        self.ventanacostos.show()        

    def iniciarVentanaPasajero(self):
        self.principal_pasajeros = PrincipalPasajeros()
        self.principal_pasajeros.show()
                                  
