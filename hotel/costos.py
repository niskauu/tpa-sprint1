import sys
from PyQt6.QtWidgets import QApplication , QLabel , QCheckBox , QSpinBox , QPushButton , QHBoxLayout , QVBoxLayout , QLineEdit , QDialog
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from descuento_gerencial import gerente
from forma_pago import formas_pago


class costos(QDialog):

    def __init__(self):
        super().__init__()
        self.setModal(True)
        self.inicializarui()
        
    def inicializarui(self):
        self.setGeometry(100, 100, 350, 200)
        self.setWindowTitle("Calcular Costos")
        self.contenido()
        self.show()

    def contenido(self):

        logo_label = QLabel()
        logo_pixmap = QPixmap("./hotel/logo.png")
        logo_pixmap = logo_pixmap.scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio)
        logo_label.setPixmap(logo_pixmap)
        logo_label.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)

        nombre_label = QLabel("Hotel CTCh")
        nombre_label.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
        nombre_label.setFixedHeight(30)

        cliente_label = QLabel("Cliente frecuente")
        cliente_label.setFixedWidth(120)

        self.Check_cliente = QCheckBox()
        self.Check_cliente.clicked.connect(self.actualizar_porcentaje_descuento)

        descuento_label = QLabel("Descuento Aplicado")
        descuento_label.setFixedWidth(120)

        self.porcentaje_descuento = QSpinBox()
        self.porcentaje_descuento.setRange(0, 100)

        descuento_button = QPushButton("Descuento gerencial")
        descuento_button.clicked.connect(self.descuento_gerencial)

        texto_label = QLabel("Calcular Costos de estadia")

        ok_button = QPushButton("Ok")

        cuadro_label = QLabel("total:$$$$$")
        cuadro_label.resize(100,100)

        volver_button = QPushButton("Volver")
        volver_button.clicked.connect(self.volver)
        pago_button = QPushButton("Realizar pago")
        pago_button.clicked.connect(self.abrirformasdepago)

        Hlayout = QHBoxLayout()
        Hlayout.addWidget(logo_label)
        Hlayout.addWidget(nombre_label)
        Hlayout.addStretch()

        Hlayout1 = QHBoxLayout()
        Hlayout1.addWidget(cliente_label)
        Hlayout1.addWidget(self.Check_cliente)

        Hlayout2 = QHBoxLayout()
        Hlayout2.addWidget(descuento_label)
        Hlayout2.addWidget(self.porcentaje_descuento)

        Hlayout3 = QHBoxLayout()
        Hlayout3.addWidget(texto_label)
        Hlayout3.addWidget(ok_button)

        Hlayout4 = QHBoxLayout()
        Hlayout4.addWidget(volver_button)
        Hlayout4.addWidget(pago_button)

        Vlayout = QVBoxLayout()
        Vlayout.addLayout(Hlayout)
        Vlayout.addLayout(Hlayout1)
        Vlayout.addLayout(Hlayout2)
        Vlayout.addWidget(descuento_button)
        Vlayout.addLayout(Hlayout3)
        Vlayout.addWidget(cuadro_label)
        Vlayout.addLayout(Hlayout4)

        self.setLayout(Vlayout)

    def actualizar_porcentaje_descuento(self):

        if self.Check_cliente.isChecked():
            self.porcentaje_descuento.setValue(30)
        else:
            self.porcentaje_descuento.setValue(0)

    def descuento_gerencial(self):
        self.ventana_gerente = gerente()
        self.ventana_gerente.show()

    def abrirformasdepago(self):
        self.ventana_pago = formas_pago()
        self.ventana_pago.show()

    def volver(self):
        self.close()
