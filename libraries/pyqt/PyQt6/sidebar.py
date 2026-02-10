from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton
)
import sys
class Sidebar(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)

        for text in ["Inicio", "Usuarios", "Configuración"]:
            btn = QPushButton(text)
            btn.setFixedHeight(40)
            layout.addWidget(btn)

        layout.addStretch()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Sidebar()
    ventana.show()
    sys.exit(app.exec())