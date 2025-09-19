import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QLineEdit, QRadioButton, QPushButton, QLabel, QMessageBox
)
from PyQt5.QtGui import QDoubleValidator


class Calculadora(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Formulario con PyQt")
        self.setGeometry(200, 200, 300, 200)

        layout = QVBoxLayout()

        #Cajas de texto
        self.txt1 = QLineEdit()
        self.txt1.setPlaceholderText("Ingrese primer numero")
        self.txt1.setValidator(QDoubleValidator())  # Acepta decimales

        self.txt2 = QLineEdit()
        self.txt2.setPlaceholderText("Ingrese segundo numero")
        self.txt2.setValidator(QDoubleValidator())  # Acepta decimales

        layout.addWidget(self.txt1)
        layout.addWidget(self.txt2)

        #RadioButtons
        self.suma = QRadioButton("+")
        self.resta = QRadioButton("-")
        self.multi = QRadioButton("*")
        self.div = QRadioButton("/")

        # Colocarlos en una fila
        hbox_ops = QHBoxLayout()
        hbox_ops.addWidget(self.suma)
        hbox_ops.addWidget(self.resta)
        hbox_ops.addWidget(self.multi)
        hbox_ops.addWidget(self.div)
        layout.addLayout(hbox_ops)

        #Botones
        self.btn_ejecutar = QPushButton("Ejecutar")
        self.btn_salir = QPushButton("Salir")

        hbox_btns = QHBoxLayout()
        hbox_btns.addWidget(self.btn_ejecutar)
        hbox_btns.addWidget(self.btn_salir)
        layout.addLayout(hbox_btns)

        #Resultado
        self.lbl_resultado = QLabel("Resultado: ")
        layout.addWidget(self.lbl_resultado)

        self.setLayout(layout)

        #Eventos
        self.btn_ejecutar.clicked.connect(self.calcular)
        self.btn_salir.clicked.connect(self.close)

    def calcular(self):
        try:
            num1 = float(self.txt1.text())
            num2 = float(self.txt2.text())

            if self.suma.isChecked():
                resultado = num1 + num2
            elif self.resta.isChecked():
                resultado = num1 - num2
            elif self.multi.isChecked():
                resultado = num1 * num2
            elif self.div.isChecked():
                if num2 == 0:
                    QMessageBox.warning(self, "Error", "No se puede dividir entre cero")
                    return
                resultado = num1 / num2
            else:
                QMessageBox.warning(self, "Error", "Seleccione una operación")
                return

            self.lbl_resultado.setText(f"Resultado: {resultado}")
        except ValueError:
            QMessageBox.warning(self, "Error", "Ingrese números válidos")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Calculadora()
    ventana.show()
    sys.exit(app.exec_())