import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel, QLineEdit, QPushButton
from PyQt6 import uic
import dbconnection
from TeacherGUI import teacherwindowUI
from AdminGUI import adminwindowUI
from StudentGUI import studentwindowUI


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
            print(verification)
            self.close()
            self.StudentGUI = studentwindowUI()
            self.StudentGUI.show()

        if verification[0] == True and verification[2] == 2:
            print(verification)
            self.close()
            self.TeacherGUI = teacherwindowUI()
            self.TeacherGUI.show()

        if verification[0] == True and verification[2] == 3:
            print(verification)
            self.close()
            self.AdminGUI = adminwindowUI()
            self.AdminGUI.show()
        else:
            print("error", verification)


#Initialiserer appen
app = QApplication(sys.argv)
UIWindow = Login()
UIWindow.show()
app.exec()
