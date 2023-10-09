from PySide6.QtWidgets import QApplication
import sys
from pg_backend_v2 import PasswordGeneratorApp

app = QApplication(sys.argv)

main = PasswordGeneratorApp()
main.show()

app.exec()