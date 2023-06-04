import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox, QCheckBox, QHBoxLayout, QVBoxLayout
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from ventanaprincipal import ventanaprincipal
from registrarse import ventanaderegistro

class Login(QWidget):
    
    def __init__(self):
        super().__init__()
        self.inicializarui()

    def inicializarui(self):
        self.setGeometry(100, 100, 350, 200)
        self.setWindowTitle("Registro recepcionista")
        self.informacion()
        self.show()

    def informacion(self):
        
        logo_label = QLabel()
        logo_pixmap = QPixmap("./hotel/logo.png")
        logo_pixmap = logo_pixmap.scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio)
        logo_label.setPixmap(logo_pixmap)
        logo_label.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)

        nombreHotel_label = QLabel("Hotel CTCh")
        nombreHotel_label.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
        nombreHotel_label.setFixedHeight(30)

        user_label = QLabel("Ingrese su Rut:")
        user_label.setFixedWidth(120)
        self.user_input = QLineEdit()

        password_label = QLabel("Ingrese su Contraseña:")
        password_label.setFixedWidth(120)
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        check_ver_contraseña = QCheckBox("Ver contraseña")
        check_ver_contraseña.toggled.connect(self.mostrarcontrasena)

        ingresar_button = QPushButton("Ingresar")
        ingresar_button.clicked.connect(self.iniciarventanaingreso)

        registro_button = QPushButton("Registrase")
        registro_button.clicked.connect(self.iniciarventanaderegistro)

        layout = QHBoxLayout()
        layout.addWidget(logo_label)
        layout.addWidget(nombreHotel_label)
        layout.addStretch()

        Hlayout1 = QHBoxLayout()
        Hlayout1.addWidget(user_label)
        Hlayout1.addWidget(self.user_input)

        Hlayout2 = QHBoxLayout()
        Hlayout2.addWidget(password_label)
        Hlayout2.addWidget(self.password_input)

        Hlayout3 = QHBoxLayout()
        Hlayout3.addWidget(check_ver_contraseña)

        Vlayout = QVBoxLayout()
        Vlayout.addLayout(layout)
        Vlayout.addLayout(Hlayout1)
        Vlayout.addLayout(Hlayout2)
        Vlayout.addLayout(Hlayout3)
        Vlayout.addWidget(ingresar_button)
        Vlayout.addWidget(registro_button)

        self.setLayout(Vlayout)

    def mostrarcontrasena(self, clicked):
        if clicked:
            self.password_input.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

    def iniciarventanaderegistro(self):
        self.nuevousuario = ventanaderegistro()
        self.nuevousuario.show()

    def iniciarventanaingreso(self):
        usuariosingresados = []
        rutadeusuario = "./hotel/datos_recepcionistas.txt"

        try: 
            with open(rutadeusuario,"r") as f:            
                for linea in f:
                    usuariosingresados.append(linea.strip("\n"))   
            informaciondeingreso = f"{self.user_input.text()},{self.password_input.text()}"  

            if informaciondeingreso in usuariosingresados:
                QMessageBox.information(self,"inicio de sesion","se ha iniciado sesion correctamente",QMessageBox.StandardButton.Ok,QMessageBox.StandardButton.Ok)
                self.is_logged = True
                self.close()
                self.abrirventanaprincipal()
            else:
                QMessageBox.warning(self,"error","la informacion no es correcta",QMessageBox.StandardButton.Close,QMessageBox.StandardButton.Close)

        except FileNotFoundError as e:
            QMessageBox.warning(self,"error","Datos no encontrados,Por favor registrese",QMessageBox.StandardButton.Close,QMessageBox.StandardButton.Close)

    def abrirventanaprincipal(self):
        self.ventanaprincipal = ventanaprincipal()
        self.ventanaprincipal.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Login()
    sys.exit(app.exec())
