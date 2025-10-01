from qtpy.QtWidgets import (
    QApplication, QWidget, QPushButton, QGridLayout, QLabel, QVBoxLayout
)
from qtpy.QtCore import Qt
from qtpy.QtGui import QFont


class TicTacToe(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tic Tac Toe - QtPy")
        self.setFixedSize(400, 450)
        self.setStyleSheet(self.get_stylesheet())

        self.current_player = "X"
        self.board = [None] * 9

        self.status_label = QLabel("Player X's Turn")
        self.status_label.setAlignment(Qt.AlignCenter)
        self.status_label.setFont(QFont("Arial", 16, QFont.Bold))
        self.status_label.setObjectName("statusLabel")

        self.grid_layout = QGridLayout()
        self.grid_layout.setSpacing(5)

        self.buttons = []
        for i in range(9):
            btn = QPushButton("")
            btn.setFixedSize(100, 100)
            btn.setFont(QFont("Arial", 24, QFont.Bold))
            btn.clicked.connect(lambda _, idx=i: self.make_move(idx))
            btn.setObjectName("cellButton")
            self.buttons.append(btn)
            self.grid_layout.addWidget(btn, i // 3, i % 3)

        layout = QVBoxLayout(self)
        layout.addWidget(self.status_label)
        layout.addLayout(self.grid_layout)

    def make_move(self, idx):
        if self.board[idx] or self.check_winner():
            return

        self.board[idx] = self.current_player
        self.buttons[idx].setText(self.current_player)

        winner = self.check_winner()
        if winner:
            self.status_label.setText(f"🎉 Player {winner} wins!")
            self.highlight_winner(winner)
            return
        elif None not in self.board:
            self.status_label.setText("🤝 It's a draw!")
            return

        self.current_player = "O" if self.current_player == "X" else "X"
        self.status_label.setText(f"Player {self.current_player}'s Turn")

    def check_winner(self):
        wins = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Cols
            (0, 4, 8), (2, 4, 6)              # Diagonals
        ]
        for a, b, c in wins:
            if self.board[a] and self.board[a] == self.board[b] == self.board[c]:
                self.winning_line = (a, b, c)
                return self.board[a]
        return None

    def highlight_winner(self, winner):
        for idx in self.winning_line:
            self.buttons[idx].setStyleSheet("background-color: #2a9d8f; color: white;")

    def get_stylesheet(self):
        return """
        QWidget {
            background-color: #1e1e2f;
        }

        QLabel#statusLabel {
            color: #f0f0f0;
            margin: 15px;
        }

        QPushButton#cellButton {
            background-color: #2a2a40;
            color: #f0f0f0;
            border: 2px solid #444;
            border-radius: 5px;
        }

        QPushButton#cellButton:hover {
            background-color: #3c3c5c;
        }

        QPushButton#cellButton:pressed {
            background-color: #457b9d;
        }
        """


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = TicTacToe()
    window.show()
    sys.exit(app.exec_())
