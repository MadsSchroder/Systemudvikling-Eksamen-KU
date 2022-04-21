import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel, QLineEdit, QPushButton, QDialog
from PyQt6 import uic

class LoginUI(QMainWindow):
    def __init__(self):
        super(LoginUI, self).__init__()

        #Loader den specifikke UI fil
        uic.loadUi("UI/Main.ui",self)


        #Viser appen
        self.show()

    def loginfunction(self):
        unilogin=self.Unilogin.text()
        password=self.Password.text()
        print("Du er logget ind med email:", unilogin, "og password:", password)


#Initialiserer appen
app = QApplication(sys.argv)
UIWindow = LoginUI()
app.exec()