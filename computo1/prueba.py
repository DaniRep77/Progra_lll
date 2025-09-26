import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit,
    QRadioButton, QPushButton, QHBoxLayout, QMessageBox
)
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt


class Calculadora(QWidget):
    def __init__(self):  # ✅ Corregido: __init__ con doble guión bajo
        super().__init__()
        self.setWindowTitle("Calculadora Básica")
        self.setGeometry(200, 200, 400, 400)

        self.operacion = "+"  # Operación por defecto

        # Layout principal
        layout = QVBoxLayout()

        # Título
        titulo = QLabel("Formulario de Operaciones")
        titulo.setFont(QFont("Arial", 14, QFont.Weight.Bold))
        titulo.setStyleSheet("margin: 15px;")
        titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(titulo)

        # Número 1
        layout.addWidget(QLabel("Número 1:"))
        self.texto_num1 = QLineEdit()
        layout.addWidget(self.texto_num1)

        # Número 2
        layout.addWidget(QLabel("Número 2:"))
        self.texto_num2 = QLineEdit()
        layout.addWidget(self.texto_num2)

        # Operaciones
        layout.addWidget(QLabel("Operación:"))

        self.radio_suma = QRadioButton("Suma (+)")
        self.radio_suma.setChecked(True)
        self.radio_resta = QRadioButton("Resta (-)")
        self.radio_multiplicacion = QRadioButton("Multiplicación (*)")
        self.radio_division = QRadioButton("División (/)")

        self.radio_suma.toggled.connect(self.on_radio_selected)
        self.radio_resta.toggled.connect(self.on_radio_selected)
        self.radio_multiplicacion.toggled.connect(self.on_radio_selected)
        self.radio_division.toggled.connect(self.on_radio_selected)

        layout.addWidget(self.radio_suma)
        layout.addWidget(self.radio_resta)
        layout.addWidget(self.radio_multiplicacion)
        layout.addWidget(self.radio_division)

        # Botones
        botones_layout = QHBoxLayout()
        boton_ejecutar = QPushButton("Ejecutar")
        boton_salir = QPushButton("Salir")

        boton_ejecutar.clicked.connect(self.on_ejecutar)
        boton_salir.clicked.connect(self.close)

        botones_layout.addWidget(boton_ejecutar)
        botones_layout.addWidget(boton_salir)
        layout.addLayout(botones_layout)

        # Resultado
        self.resultado = QLabel("Resultado: ")
        self.resultado.setStyleSheet("margin: 10px; font-weight: bold;")
        layout.addWidget(self.resultado)

        self.setLayout(layout)

    def on_radio_selected(self):
        if self.radio_suma.isChecked():
            self.operacion = "+"
        elif self.radio_resta.isChecked():
            self.operacion = "-"
        elif self.radio_multiplicacion.isChecked():
            self.operacion = "*"
        elif self.radio_division.isChecked():
            self.operacion = "/"

    def on_ejecutar(self):
        try:
            num1 = float(self.texto_num1.text())
            num2 = float(self.texto_num2.text())

            if self.operacion == "+":
                resultado = num1 + num2
            elif self.operacion == "-":
                resultado = num1 - num2
            elif self.operacion == "*":
                resultado = num1 * num2
            elif self.operacion == "/":
                if num2 == 0:
                    QMessageBox.warning(self, "Error", "División por cero")
                    return
                resultado = num1 / num2

            self.resultado.setText(f"Resultado: {resultado}")

        except ValueError:
            QMessageBox.warning(self, "Error", "Ingrese números válidos")


if __name__ == "__main__":  # ✅ Corregido: __name__ con doble guión bajo
    app = QApplication(sys.argv)
    ventana = Calculadora()
    ventana.show()
    sys.exit(app.exec())