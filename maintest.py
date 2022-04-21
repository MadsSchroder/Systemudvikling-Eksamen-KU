import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel, QLineEdit, QPushButton, QTabWidget, QTableWidget
from PyQt6 import uic

class LoginUI(QMainWindow):
    def __init__(self):
        super(LoginUI, self).__init__()

        #Loader den specifikke UI fil
        uic.loadUi("UI/mainwindow.ui",self)

        #Definerer UI filens widgets
        self.Unilogin = self.findChild(QLineEdit, "Unilogin")
        self.Password = self.findChild(QLineEdit, "Password")
        self.LoginButton = self.findChild(QPushButton, "LoginButton")
        self.GlemtLoginButton = self.findChild(QPushButton, "GlemtLoginButton")


        #Viser appen
        self.show()



#Initialiserer appen
app = QApplication(sys.argv)
UIWindow = LoginUI()
app.exec()