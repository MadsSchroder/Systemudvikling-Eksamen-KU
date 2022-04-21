import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel, QLineEdit, QPushButton
from PyQt6 import uic
import dbconnection

class LoginUI(QMainWindow):
    def __init__(self):
        super(LoginUI, self).__init__()

        #Loader den specifikke UI fil
        uic.loadUi("UI/Login.ui",self)

        #Definerer UI filens widgets
        self.Unilogin = self.findChild(QLineEdit, "Unilogin")
        self.Password = self.findChild(QLineEdit, "Password")
        self.LoginButton = self.findChild(QPushButton, "LoginButton")
        self.GlemtLoginButton = self.findChild(QPushButton, "GlemtLoginButton")

        #Hvad widgets skal gøre
        self.LoginButton.clicked.connect(self.loginfunction)

        #Viser appen
        self.show()

    def loginfunction(self):
        unilogin=self.Unilogin.text()
        password=self.Password.text()
        verification=dbconnection.check_password(unilogin, password)
        print(verification)



#Initialiserer appen
app = QApplication(sys.argv)
UIWindow = LoginUI()
app.exec()