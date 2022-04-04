import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QDialog, QApplication, QMainWindow
from PyQt6.uic import loadUi

class Login(QtWidgets):
    def __init__(self):
        super(Login,self).__init__()
        loadUi("Login_widget.ui",self)
        self.LoginButton.click.connect(self.loginfunction)

    def loginfunction(self):
        Unilogin=self.Unilogin.text()
        Password=self.Password.text()
        print("Godkendt login, Bruger: ", Unilogin, "og adgangskode: ", Password)


app=QApplication(sys.argv)
mainwindow=Login()
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(420)
widget.setFixedHeight(520)
widget.show()
app.exec()