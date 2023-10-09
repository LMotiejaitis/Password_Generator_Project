import random
import string
import sys
import os
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QTextEdit
from PySide6.QtUiTools import QUiLoader

ui_file = os.path.join("C:\\Qt\\6.5.2\\mingw_64\\bin", "password_generetor.ui")

class PasswordGeneratorApp(QMainWindow):
    def __init__(self):
        super().__init__()

        loader = QUiLoader()
        self.ui = loader.load(ui_file, None)
        self.setCentralWidget(self.ui)

        self.setWindowTitle("Password Generator")

        self.ui.generate_button.clicked.connect(self.generate_passwords)
        self.ui.clear_button.clicked.connect(self.clear_output)
        self.ui.exit_button.clicked.connect(self.close)

        self.ui.amount_input_slider.valueChanged.connect(self.update_amount_input)
        self.ui.amount_input.editingFinished.connect(self.update_amount_slider)
        self.ui.length_input_slider.valueChanged.connect(self.update_length_input)
        self.ui.length_input.editingFinished.connect(self.update_length_slider)

    def update_amount_input(self):
        self.ui.amount_input.setText(str(self.ui.amount_input_slider.value()))

    def update_length_input(self):
        self.ui.length_input.setText(str(self.ui.length_input_slider.value()))

    def update_amount_slider(self):
        try:
            value = int(self.ui.amount_input.text())
            if 0 < value <= 25:
                self.ui.amount_input_slider.setValue(value)
            else:
                self.ui.amount_input.setText("Invalid")
        except ValueError:
            self.ui.amount_input.setText("Invalid")

    def update_length_slider(self):
        try:
            value = int(self.ui.length_input.text())
            if 0 < value <= 25:
                self.ui.length_input_slider.setValue(value)
            else:
                self.ui.length_input.setText("Invalid")
        except ValueError:
            self.ui.length_input.setText("Invalid")

    def generate_passwords(self):
        try:
            lnth = int(self.ui.length_input.text())
            num = int(self.ui.amount_input.text())
        except ValueError:
            self.ui.passwords_output.setPlainText("Please enter valid numbers for Length and Amount.")
            return

        if not (6 < lnth <= 25 and 1 < num <= 25):
            self.ui.passwords_output.setPlainText("Length cannot exceed 50 while Amount can't be more than 25.")
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
        self.ui.passwords_output.setPlainText(output_text)

    def clear_output(self):
        self.ui.passwords_output.clear()

def main():
    app = QApplication(sys.argv)
    window = PasswordGeneratorApp()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
