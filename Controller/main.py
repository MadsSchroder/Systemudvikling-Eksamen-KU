import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QLineEdit, QPushButton
from PyQt6 import uic
from Controller import dbconnection
from Controller.TeacherGUI import teacherwindowUI
from Controller.AdminGUI import adminwindowUI
from Controller.StudentGUI import studentwindowUI


class Login(QMainWindow):
    def __init__(self):
        super(Login, self).__init__()
        #Loader den specifikke Views fil
        uic.loadUi("../Views/Login.ui",self)

        #Definerer Views filens widgets
        self.Unilogin = self.findChild(QLineEdit, "Unilogin")
        self.Password = self.findChild(QLineEdit, "Password")
        self.LoginButton = self.findChild(QPushButton, "LoginButton")
        self.GlemtLoginButton = self.findChild(QPushButton, "GlemtLoginButton")

        #Hvad widgets skal gøre
        self.LoginButton.clicked.connect(self.loginfunction)
        self.Password.returnPressed.connect(self.loginfunction)

        #Viser appen
        self.show()

    def loginfunction(self):
        unilogin = self.Unilogin.text()
        password = self.Password.text()
        verification = dbconnection.check_password(unilogin, password)

        if verification[0] == True and verification[2] == 1:
            print(verification)
            self.close()
            self.StudentGUI = studentwindowUI(verification[3])
            self.StudentGUI.show()

        if verification[0] == True and verification[2] == 2:
            print(verification)
            self.close()
            self.TeacherGUI = teacherwindowUI(verification[3])
            self.TeacherGUI.show()

        if verification[0] == True and verification[2] == 3:
            print(verification)
            self.close()
            self.AdminGUI = adminwindowUI(verification[3])
            self.AdminGUI.show()
        else:
            print("error", verification)


#Initialiserer appen
app = QApplication(sys.argv)
UIWindow = Login()
UIWindow.show()
app.exec()
