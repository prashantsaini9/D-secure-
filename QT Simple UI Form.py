import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QPushButton, QVBoxLayout, QMessageBox
)

class SimpleFormApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simple Form")
        self.setGeometry(100, 100, 300, 200)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Name
        self.name_label = QLabel("Name:")
        self.name_input = QLineEdit()
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_input)

        # Email
        self.email_label = QLabel("Email:")
        self.email_input = QLineEdit()
        layout.addWidget(self.email_label)
        layout.addWidget(self.email_input)

        # Age
        self.age_label = QLabel("Age:")
        self.age_input = QLineEdit()
        layout.addWidget(self.age_label)
        layout.addWidget(self.age_input)

        # Submit Button
        self.submit_btn = QPushButton("Submit")
        self.submit_btn.clicked.connect(self.show_data)
        layout.addWidget(self.submit_btn)

        self.setLayout(layout)

    def show_data(self):
        name = self.name_input.text()
        email = self.email_input.text()
        age = self.age_input.text()

        QMessageBox.information(self, "Form Data",
                                f"Name: {name}\nEmail: {email}\nAge: {age}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SimpleFormApp()
    window.show()
    sys.exit(app.exec_())

