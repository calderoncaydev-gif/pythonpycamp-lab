import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QLabel, QPushButton,
    QLineEdit, QWidget, QVBoxLayout
)

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Formulario PyQt6")
        self.setGeometry(300, 200, 400, 250)

        self.input_nombre = QLineEdit()
        self.input_nombre.setPlaceholderText("Escribe tu nombre")

        self.label = QLabel("")

        boton = QPushButton("Enviar")
        boton.clicked.connect(self.mostrar_nombre)

        layout = QVBoxLayout()
        layout.addWidget(self.input_nombre)
        layout.addWidget(boton)
        layout.addWidget(self.label)

        contenedor = QWidget()
        contenedor.setLayout(layout)
        self.setCentralWidget(contenedor)

    def mostrar_nombre(self):
        nombre = self.input_nombre.text()
        self.label.setText(f"Hola {nombre} 👋")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())
