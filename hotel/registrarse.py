from PyQt6.QtWidgets import QDialog , QLabel , QPushButton , QLineEdit , QMessageBox , QHBoxLayout , QVBoxLayout
from PyQt6.QtGui import QFont
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
import re

class ventanaderegistro(QDialog):
     
    def __init__(self):
        super().__init__()
        self.setModal(True)    
        self.datosusuario()

    def datosusuario(self):

        self.setGeometry(100,100,350,200)
        self.setWindowTitle("ventana de registro")

        logo_label = QLabel()
        logo_pixmap = QPixmap("./hotel/logo.png")
        logo_pixmap = logo_pixmap.scaled(30, 30, Qt.AspectRatioMode.KeepAspectRatio)
        logo_label.setPixmap(logo_pixmap)
        logo_label.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)

        nombre_label = QLabel("Hotel CTCh")
        nombre_label.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
        nombre_label.setFixedHeight(30)

        user_label = QLabel(self)
        user_label.setText("Ingrese su Rut")
        user_label.setFont(QFont("Arial",10))
        user_label.move(20,44)

        self.user_input = QLineEdit(self)
        self.user_input.resize(250,24)
        self.user_input.move(90,40)

        password1_label = QLabel(self)
        password1_label.setText("Ingrese una Contraseña")
        password1_label.setFont(QFont("Arial",10))
        password1_label.move(20,74)

        self.password1_label_input = QLineEdit(self)
        self.password1_label_input.resize(250,24)
        self.password1_label_input.move(90,70)
        self.password1_label_input.setEchoMode(QLineEdit.EchoMode.Password)

        password2_label = QLabel(self)
        password2_label.setText("Confirme su Contraseña")
        password2_label.setFont(QFont("Arial",10))
        password2_label.move(20,104)

        self.password2_label_input = QLineEdit(self)
        self.password2_label_input.resize(250,24)
        self.password2_label_input.move(90,100)
        self.password2_label_input.setEchoMode(QLineEdit.EchoMode.Password)

        aceptar_button = QPushButton(self)
        aceptar_button.setText("aceptar")
        aceptar_button.resize(150,32)
        aceptar_button.move(20,170)
        aceptar_button.clicked.connect(self.crearusuario)

        cancelar_button = QPushButton(self)
        cancelar_button.setText("cancelar")
        cancelar_button.resize(150,32)
        cancelar_button.move(170,170)
        cancelar_button.clicked.connect(self.cancelarcreacion)

        Hlayout = QHBoxLayout()
        Hlayout.addWidget(logo_label)
        Hlayout.addWidget(nombre_label)
        Hlayout.addStretch()

        Hlayout1 = QHBoxLayout()
        Hlayout1.addWidget(user_label)
        Hlayout1.addWidget(self.user_input)

        Hlayout2 = QHBoxLayout()
        Hlayout2.addWidget(password1_label)
        Hlayout2.addWidget(self.password1_label_input)

        Hlayout3 = QHBoxLayout()
        Hlayout3.addWidget(password2_label)
        Hlayout3.addWidget(self.password2_label_input)

        Hlayout4= QHBoxLayout()
        Hlayout4.addWidget(aceptar_button)
        Hlayout4.addWidget(cancelar_button)

        Vlayout = QVBoxLayout()
        Vlayout.addLayout(Hlayout)
        Vlayout.addLayout(Hlayout1)
        Vlayout.addLayout(Hlayout2)
        Vlayout.addLayout(Hlayout3)
        Vlayout.addLayout(Hlayout4)

        self.setLayout(Vlayout)

    def crearusuario(self):

        rutadeusuario = "./hotel/datos_recepcionistas.txt"
        rut = self.user_input.text()
        rut = rut.replace(".", "").replace("-", "")
        contraseña1 = self.password1_label_input.text()
        contraseña2 = self.password2_label_input.text()

        formato_rut = r'^\d{1,2}(\.\d{3}){2}-?[\dkK]$|^(\d{7,8})-?[\dkK]$|^(\d{9,10})$'
        if not re.match(formato_rut, rut):
            QMessageBox.warning(self, "Error", "Ingrese un rut válido", QMessageBox.StandardButton.Close, QMessageBox.StandardButton.Close)
            return
        elif contraseña1 == "" or contraseña2 == "":
            QMessageBox.warning(self, "Error", "Campos obligatorios, por favor ingrese los datos solicitados", QMessageBox.StandardButton.Close, QMessageBox.StandardButton.Close)
        elif contraseña1 != contraseña2:
            QMessageBox.warning(self, "Error", "Las contraseñas deben ser idénticas, por favor inténtelo de nuevo", QMessageBox.StandardButton.Close, QMessageBox.StandardButton.Close)
        else:
            try:
                with open(rutadeusuario, "a+") as f:
                    f.write(f"{rut},{contraseña1}\n")
                QMessageBox.information(self, "Creación exitosa", "El usuario se creó correctamente", QMessageBox.StandardButton.Ok, QMessageBox.StandardButton.Ok)
                self.close()

            except FileNotFoundError as e:
                QMessageBox.warning(self, "Error", "El archivo de texto no se encontró", QMessageBox.StandardButton.Close, QMessageBox.StandardButton.Close)

    def cancelarcreacion(self):
        self.close()               
