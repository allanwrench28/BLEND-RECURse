import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
)


class RefinedUI(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("GHST Refined UI")
        self.setGeometry(100, 100, 800, 600)

        # Main layout
        self.central_widget = QWidget()
        self.layout = QVBoxLayout()

        # Title Label
        self.title_label = QLabel("Welcome to GHST Refined UI", self)
        self.title_label.setStyleSheet(
            "font-size: 24px; font-weight: bold; text-align: center;"
        )
        self.layout.addWidget(self.title_label)

        # Start Button
        self.start_button = QPushButton("Start", self)
        self.start_button.clicked.connect(self.start_action)
        self.layout.addWidget(self.start_button)

        # Settings Button
        self.settings_button = QPushButton("Settings", self)
        self.settings_button.clicked.connect(self.settings_action)
        self.layout.addWidget(self.settings_button)

        # Exit Button
        self.exit_button = QPushButton("Exit", self)
        self.exit_button.clicked.connect(self.close)
        self.layout.addWidget(self.exit_button)

        # Feedback Label
        self.feedback_label = QLabel("", self)
        self.feedback_label.setStyleSheet("color: green; font-size: 16px;")
        self.layout.addWidget(self.feedback_label)

        self.central_widget.setLayout(self.layout)
        self.setCentralWidget(self.central_widget)

    def start_action(self):
        self.feedback_label.setText(
            "Start button clicked! Performing action..."
        )

    def settings_action(self):
        self.feedback_label.setText(
            "Settings button clicked! Opening settings..."
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RefinedUI()
    window.show()
    sys.exit(app.exec_())
