from PyQt6.QtWidgets import QLabel , QPushButton , QHBoxLayout , QVBoxLayout ,QDialog , QLineEdit
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from efectivo import efectivo
from credito import credito
from debito import debito
from transferencia import Transferencia

class formas_pago(QDialog):

    def __init__(self):
        super().__init__()
        self.setModal(True)
        self.inicializarui()

    def inicializarui(self):
        self.setGeometry(100, 100, 350, 200)
        self.setWindowTitle("Pago de servicios")
        self.contenido()

    def contenido(self):

        logo_label = QLabel()
        logo_pixmap = QPixmap("./hotel/logo.png")
        logo_pixmap = logo_pixmap.scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio)
        logo_label.setPixmap(logo_pixmap)
        logo_label.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)

        nombreHotel_label = QLabel("Hotel CTCh")
        nombreHotel_label.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
        nombreHotel_label.setFixedHeight(30)

        monto_label = QLabel("Monto total: $")
        self.monto_input = QLineEdit()

        efectivo_button = QPushButton("Efectivo")
        efectivo_button.clicked.connect(self.pagarenefectivo)

        credito_button = QPushButton("Tarjeta de credito")
        credito_button.clicked.connect(self.pagarcontarjetacredito)

        debito_button = QPushButton("Tarjeta de debito")
        debito_button.clicked.connect(self.pagarcontarjetadebido)

        transferencia_button = QPushButton("Transferencia")
        transferencia_button.clicked.connect(self.pagartransferencia)

        volver_button = QPushButton("Volver")
        volver_button.clicked.connect(self.cerrarventana)

        layout = QHBoxLayout()
        layout.addWidget(logo_label)
        layout.addWidget(nombreHotel_label)
        layout.addStretch()

        Hlayout = QHBoxLayout()
        Hlayout.addWidget(monto_label)
        Hlayout.addWidget(self.monto_input)

        Hlayout1 =QHBoxLayout()
        Hlayout1.addWidget(efectivo_button)
        Hlayout1.addWidget(credito_button)
        Hlayout1.addWidget(debito_button)
        Hlayout1.addWidget(transferencia_button)

        Vlayout = QVBoxLayout()
        Vlayout.addLayout(layout)
        Vlayout.addLayout(Hlayout)
        Vlayout.addLayout(Hlayout1)
        Vlayout.addWidget(volver_button)

        self.setLayout(Vlayout)

    def pagarenefectivo(self):
        self.pagar = efectivo()
        self.pagar.show()

    def pagarcontarjetacredito(self):
        self.pagoTC = credito()
        self.pagoTC.show()

    def pagarcontarjetadebido(self):
        self.pagoTD = debito()
        self.pagoTD.show()

    def pagartransferencia(self):
        self.pagotransferencia = Transferencia()
        self.pagotransferencia.show()

    def cerrarventana(self):
        self.close()



