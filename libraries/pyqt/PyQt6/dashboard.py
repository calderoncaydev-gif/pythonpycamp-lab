from PyQt6.QtWidgets import (
     QApplication,QWidget, QVBoxLayout, QLabel, QFrame
)
from PyQt6.QtCore import Qt
import sys
class Dashboard(QWidget):
    def __init__(self):
        super().__init__()

        title = QLabel("Dashboard")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("font-size: 20px;")

        card = QFrame()
        card.setFrameShape(QFrame.Shape.StyledPanel)

        card_layout = QVBoxLayout()
        card_layout.addWidget(QLabel("Contenido principal"))
        card.setLayout(card_layout)

        layout = QVBoxLayout(self)
        layout.addWidget(title)
        layout.addWidget(card)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Dashboard()
    ventana.show()
    sys.exit(app.exec())
