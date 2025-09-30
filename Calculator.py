from qtpy.QtWidgets import (
    QApplication, QWidget, QGridLayout, QPushButton, QLineEdit, QVBoxLayout
)
from qtpy.QtCore import Qt
import sys

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("iPhone Calculator")
        self.setMinimumSize(320, 480)
        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(10, 10, 10, 10)
        self.layout.setSpacing(10)

        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setObjectName("Display")
        self.display.setFixedHeight(70)

        self.layout.addWidget(self.display)

        self.grid = QGridLayout()
        self.grid.setSpacing(10)  # spacing between buttons
        self.layout.addLayout(self.grid)
        self.setLayout(self.layout)

        # Calculator button layout
        buttons = [
            ('AC', '(', ')', '/'),
            ('7', '8', '9', '*'),
            ('4', '5', '6', '-'),
            ('1', '2', '3', '+'),
            ('0', '.', '=', '')
        ]

        for row_idx, row in enumerate(buttons):
            for col_idx, text in enumerate(row):
                if not text:
                    continue
                button = QPushButton(text)
                button.clicked.connect(self.on_button_clicked)
                button.setObjectName(self.get_button_class(text))

                # Special handling for wide "0" button
                if text == '0':
                    self.grid.addWidget(button, row_idx, col_idx, 1, 2)  # span 2 columns
                elif text == '=' and buttons[row_idx][col_idx - 1] == '0':
                    self.grid.addWidget(button, row_idx, col_idx + 1)
                else:
                    self.grid.addWidget(button, row_idx, col_idx)

        self.setStyleSheet(self.get_stylesheet())

    def get_button_class(self, text):
        if text in {'+', '-', '*', '/', '='}:
            return 'OperatorButton'
        elif text in {'AC', '(', ')'}:
            return 'FunctionButton'
        elif text == '0':
            return 'ZeroButton'
        else:
            return 'NumberButton'

    def on_button_clicked(self):
        sender = self.sender()
        text = sender.text()

        if text == 'AC':
            self.display.setText('')
        elif text == '=':
            try:
                result = str(eval(self.display.text()))
                self.display.setText(result)
            except:
                self.display.setText("Error")
        else:
            self.display.setText(self.display.text() + text)

    def get_stylesheet(self):
        return """
        QWidget {
            background-color: #000000;
            font-family: 'Helvetica Neue', sans-serif;
        }

        QLineEdit#Display {
            background-color: #000000;
            color: white;
            border: none;
            font-size: 36px;
            padding: 10px;
        }

        QPushButton {
            border: none;
            font-size: 24px;
            padding: 20px;
            min-height: 60px;
            min-width: 60px;
            border-radius: 30px;
            box-shadow: inset 0 0 5px #111;
        }

        QPushButton:hover {
            filter: brightness(1.2);
        }

        QPushButton#NumberButton {
            background-color: #333333;
            color: white;
        }

        QPushButton#OperatorButton {
            background-color: #FF9500;
            color: white;
        }

        QPushButton#FunctionButton {
            background-color: #A5A5A5;
            color: black;
        }

        QPushButton#ZeroButton {
            background-color: #333333;
            color: white;
            font-size: 24px;
            border-radius: 30px;
        }
        """

# Run app
if __name__ == "__main__":
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec())
