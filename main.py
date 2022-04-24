import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel, QLineEdit, QPushButton
from PyQt6 import uic
import dbconnection
import Teacher

class Login(QMainWindow):
    def __init__(self):
        super(Login, self).__init__()

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
        unilogin = self.Unilogin.text()
        password = self.Password.text()
        verification = dbconnection.check_password(unilogin, password)
        if verification[0] == True and verification[2] == 1:
            uic.loadUi("UI/studentwindow.ui", self)
            print(verification)
        if verification[0] == True and verification[2] == 2:
            print(verification)
            uic.loadUi("UI/teacherwindow.ui", self)
            #self.Teacher.teacherwindowUI.displayInfo()
            #Teacher.calendarDateChanged()

        if verification[0] == True and verification[2] == 3:
            uic.loadUi("UI/adminwindow.ui", self)
            print(verification)
        else:
            print("error", verification)


#Initialiserer appen
app = QApplication(sys.argv)
UIWindow = Login()
UIWindow.show()
app.exec()
