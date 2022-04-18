import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel, QLineEdit, QPushButton
from PyQt6 import uic

class LoginUI(QMainWindow):
    def __init__(self):
        super(LoginUI, self).__init__()
        uic.loadUi("Login.ui",self)
        self.show()

app = QApplication(sys.argv)
UIWindow = LoginUI()
app.exec()