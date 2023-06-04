from PyQt6.QtWidgets import QLabel , QLineEdit , QPushButton , QHBoxLayout , QVBoxLayout , QDialog , QMessageBox
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt

class debito(QDialog):

    def __init__(self):

        super().__init__()
        self.setModal(True)
        self.inicializarui()

    def inicializarui(self):

        self.setGeometry(100, 100, 350, 200)
        self.setWindowTitle("Tarjeta de debito")
        self.contenido()

    def contenido(self):

        logo_label = QLabel()
        logo_pixmap = QPixmap("./hotel/logo.png")
        logo_pixmap = logo_pixmap.scaled(30, 30, Qt.AspectRatioMode.KeepAspectRatio)
        logo_label.setPixmap(logo_pixmap)
        logo_label.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)

        nombreHotel_label = QLabel("Hotel CTCh")
        nombreHotel_label.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
        nombreHotel_label.setFixedHeight(30)

        monto_label = QLabel("Monto")
        monto_input =QLineEdit()

        numeros_label = QLabel("Numero de trajeta")
        self.numtarjeta_input = QLineEdit()

        rut_label = QLabel("Rut")
        rut_input = QLineEdit()

        volver_button = QPushButton("Volver")
        volver_button.clicked.connect(self.cerrarventana)

        pagar_button = QPushButton("Realizar Pago")
        pagar_button.clicked.connect(self.pago)

        Hlayout = QHBoxLayout()
        Hlayout.addWidget(logo_label)
        Hlayout.addWidget(nombreHotel_label)
        Hlayout.addStretch()

        Hlayout1 = QHBoxLayout()
        Hlayout1.addWidget(monto_label)
        Hlayout1.addWidget(monto_input)

        Hlayout2 = QHBoxLayout()
        Hlayout2.addWidget(rut_label)
        Hlayout2.addWidget(rut_input)

        Hlayout3 = QHBoxLayout()
        Hlayout3.addWidget(volver_button)
        Hlayout3.addWidget(pagar_button)

        Vlayout = QVBoxLayout()
        Vlayout.addLayout(Hlayout)
        Vlayout.addLayout(Hlayout1)
        Vlayout.addWidget(numeros_label)
        Vlayout.addWidget(self.numtarjeta_input)
        Vlayout.addLayout(Hlayout2)
        Vlayout.addLayout(Hlayout3)

        self.setLayout(Vlayout)

    def cerrarventana(self):
        self.close()

    def pago(self):
        QMessageBox.information(self, "Pago exitoso", "El pago se realizo correctamente", QMessageBox.StandardButton.Ok, QMessageBox.StandardButton.Ok)
        self.close()



