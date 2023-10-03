import random
import string
from PySide6.QtWidgets import QMainWindow
from pg_ui_v2 import Ui_PasswordGenerator

class PasswordGeneratorApp(QMainWindow, Ui_PasswordGenerator):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.setWindowTitle("Password Generator")

        self.generate_button.clicked.connect(self.generate_passwords)
        self.clear_button.clicked.connect(self.clear_output)
        self.exit_button.clicked.connect(self.close)
        self.amount_input_slider.valueChanged.connect(self.update_amount_input)
        self.amount_input.editingFinished.connect(self.update_amount_slider)
        self.length_input_slider.valueChanged.connect(self.update_length_input)
        self.length_input.editingFinished.connect(self.update_length_slider)
        self.numbers_checkbox.stateChanged.connect(self.generate_passwords)
        self.symbols_checkbox.stateChanged.connect(self.generate_passwords)
        self.lowercase_checkbox.stateChanged.connect(self.generate_passwords)
        self.uppercase_checkbox.stateChanged.connect(self.generate_passwords)

    def update_amount_input(self):
        self.amount_input.setText(str(self.amount_input_slider.value()))

    def update_length_input(self):
        self.length_input.setText(str(self.length_input_slider.value()))

    def update_amount_slider(self):
        try:
            value = int(self.amount_input.text())
            if 0 < value <= 25:
                self.amount_input_slider.setValue(value)
            else:
                self.amount_input.setText("Invalid")
        except ValueError:
            self.amount_input.setText("Invalid")

    def update_length_slider(self):
        try:
            value = int(self.length_input.text())
            if 0 < value <= 25:
                self.length_input_slider.setValue(value)
            else:
                self.length_input.setText("Invalid")
        except ValueError:
            self.length_input.setText("Invalid")

    def generate_passwords(self):
        try:
            lnth = int(self.length_input.text())
            num = int(self.amount_input.text())
        except ValueError:
            self.passwords_output.setPlainText("Please enter valid numbers for Length and Amount.")
            return

        if not (5 < lnth <= 25 and 1 < num <= 25):
            self.passwords_output.setPlainText("Error has occurred. Please keep in mind that the amount can be set between 1 and 25 while the length between 6 and 25.")
            return

        include_numbers = self.numbers_checkbox.isChecked()
        include_symbols = self.symbols_checkbox.isChecked()
        include_lowercase = self.lowercase_checkbox.isChecked()
        include_uppercase = self.uppercase_checkbox.isChecked()

        characters = ''
        if include_lowercase:
            characters += string.ascii_lowercase
        if include_uppercase:
            characters += string.ascii_uppercase
        if include_numbers:
            characters += string.digits
        if include_symbols:
            characters += string.punctuation

        if not characters:
            self.passwords_output.setPlainText("Please select at least one option (Numbers, Symbols, Lowercase letters or Uppercase letters).")
            return

        passwords = self.generate_passwords_helper(num, lnth, characters)
        self.printing_passwords(passwords)

    def generate_passwords_helper(self, num, lnth, characters):
        passwords = []

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

""" def main():
    app = QApplication(sys.argv)
    window = PasswordGeneratorApp()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main() """
