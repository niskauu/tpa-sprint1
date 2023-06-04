from PyQt6.QtWidgets import QLabel , QLineEdit , QSpinBox , QDateEdit , QPushButton , QDialog , QHBoxLayout , QVBoxLayout , QMessageBox
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt

class gerente(QDialog):

    def __init__(self):
        super().__init__()
        self.setModal(True)
        self.inicializarui()
        self.rut_predefinido = None
        self.contrasena_predefinida = None

    def inicializarui(self):

        self.setGeometry(100, 100, 350, 200)
        self.setWindowTitle("Confirmacion gerente")

        logo_label = QLabel()
        logo_pixmap = QPixmap("./hotel/logo.png")
        logo_pixmap = logo_pixmap.scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio)
        logo_label.setPixmap(logo_pixmap)
        logo_label.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)

        nombre_label = QLabel("Hotel CTCh")
        nombre_label.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
        nombre_label.setFixedHeight(30)

        rut_label = QLabel("Rut")
        rut_label.setFixedWidth(120)
        self.rut_input = QLineEdit()

        contrasena_label = QLabel("Contraseña")
        contrasena_label.setFixedWidth(120)
        self.contraseña_input = QLineEdit()

        descuento_label = QLabel("Descuento")
        descuento_label.setFixedWidth(120)
        self.descuento_input = QSpinBox()
        self.descuento_input.setRange(0,100)

        fecha_label = QLabel("Fecha")
        fecha_label.setFixedWidth(120)
        self.fecha_input = QDateEdit()

        cancelar_button = QPushButton("Cancelar")
        cancelar_button.clicked.connect(self.cerrarventana)

        confirmar_button = QPushButton("Confirmar Descuento")
        confirmar_button.clicked.connect(self.registro_gerente)

        Hlayout = QHBoxLayout()
        Hlayout.addWidget(logo_label)
        Hlayout.addWidget(nombre_label)
        Hlayout.addStretch()

        Hlayout1 = QHBoxLayout()
        Hlayout1.addWidget(rut_label)
        Hlayout1.addWidget(self.rut_input)

        Hlayout2 = QHBoxLayout()
        Hlayout2.addWidget(contrasena_label)
        Hlayout2.addWidget(self.contraseña_input)

        Hlayout3 = QHBoxLayout()
        Hlayout3.addWidget(descuento_label)
        Hlayout3.addWidget(self.descuento_input)

        Hlayout4 = QHBoxLayout()
        Hlayout4.addWidget(fecha_label)
        Hlayout4.addWidget(self.fecha_input)

        Hlayout5 = QHBoxLayout()
        Hlayout5.addWidget(cancelar_button)
        Hlayout5.addWidget(confirmar_button)

        Vlayout = QVBoxLayout()
        Vlayout.addLayout(Hlayout)
        Vlayout.addLayout(Hlayout1)
        Vlayout.addLayout(Hlayout2)
        Vlayout.addLayout(Hlayout3)
        Vlayout.addLayout(Hlayout4)
        Vlayout.addLayout(Hlayout5)

        self.setLayout(Vlayout)

    def registro_gerente(self):

        ruta_datos_gerente = "./hotel/datos_gerente.txt"
        archivo = open(ruta_datos_gerente,"a")

        rut_ingresado = self.rut_input.text()
        contrasena_ingresada = self.contraseña_input.text()
        descuento = self.descuento_input.text()
        fecha = self.fecha_input.text()

        self.rut_predefinido == rut_ingresado
        self.contrasena_predefinida == contrasena_ingresada

        if rut_ingresado and contrasena_ingresada: 
            
            self.rut_predefinido = rut_ingresado
            self.contrasena_predefinida = contrasena_ingresada

            archivo.write(f"Rut: {rut_ingresado}\n")
            archivo.write(f"Contraseña: {contrasena_ingresada}\n")
            archivo.write(f"Descuento: {descuento}\n")
            archivo.write(f"Fecha: {fecha}\n")
            archivo.close()

            QMessageBox.information(self, "Datos guardados", "Los datos se han guardado correctamente", QMessageBox.StandardButton.Ok, QMessageBox.StandardButton.Ok)
            self.close()
        else:
            archivo.close()
            QMessageBox.warning(self, "Error", "Debe ingresar un Rut y una Contraseña", QMessageBox.StandardButton.Ok, QMessageBox.StandardButton.Ok)

    def cerrarventana(self):
        self.close()



