import random
import string
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit

class PasswordGeneratorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Password Generator")
        self.setGeometry(100, 100, 400, 300)

        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)

        layout = QVBoxLayout()
        main_widget.setLayout(layout)

        length_layout = QHBoxLayout()
        layout.addLayout(length_layout)

        length_label = QLabel("Length:")
        length_layout.addWidget(length_label)
        self.length_input = QLineEdit()
        length_layout.addWidget(self.length_input)

        amount_layout = QHBoxLayout()
        layout.addLayout(amount_layout)

        amount_label = QLabel("Amount:")
        amount_layout.addWidget(amount_label)
        self.amount_input = QLineEdit()
        amount_layout.addWidget(self.amount_input)

        self.generate_button = QPushButton("Generate")
        self.generate_button.clicked.connect(self.generate_passwords)
        layout.addWidget(self.generate_button)

        self.passwords_output = QTextEdit()
        layout.addWidget(self.passwords_output)

        button_layout = QHBoxLayout()
        layout.addLayout(button_layout)

        self.clear_button = QPushButton("Clear")
        self.clear_button.clicked.connect(self.clear_output)
        button_layout.addWidget(self.clear_button)

        self.exit_button = QPushButton("Exit")
        self.exit_button.clicked.connect(self.close)
        button_layout.addWidget(self.exit_button)

    def generate_passwords(self):
        try:
            lnth = int(self.length_input.text())
            num = int(self.amount_input.text())
        except ValueError:
            self.passwords_output.setPlainText("Please enter valid numbers for Length and Amount.")
            return

        if not (0 < lnth <= 50 and 0 < num <= 50):
            self.passwords_output.setPlainText("Length and Amount must be between 1 and 50.")
            return

        passwords = self.generate_passwords_helper(num, lnth)
        self.printing_passwords(passwords)

    def generate_passwords_helper(self, num, lnth):
        passwords = []
        characters = string.ascii_letters + string.digits + string.punctuation
        for i in range(num):
            password = ''.join(random.choice(characters) for _ in range(lnth))
            passwords.append(password)
        return passwords

    def printing_passwords(self, passwords):
        if len(passwords) == 1:
            output_text = 'Here is your password:'
        else:
            output_text = 'Here are your passwords:'
        for i, password in enumerate(passwords):
            output_text += f'\n{i + 1}. {password}'
        self.passwords_output.setPlainText(output_text)

    def clear_output(self):
        self.passwords_output.clear()

def main():
    app = QApplication(sys.argv)
    window = PasswordGeneratorApp()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
