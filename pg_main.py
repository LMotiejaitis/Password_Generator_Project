from PySide6.QtWidgets import QApplication
import sys
from pg_backend import PasswordGeneratorApp

app = QApplication(sys.argv)

main = PasswordGeneratorApp()
main.show()

app.exec()