import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6 import QtWidgets
from PyQt6.QtCore import *
from PyQt6 import QtCore
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtWidgets import QApplication
from PyQt6 import uic
from os import path
from PyQt6.uic import loadUiType
import dbconnection

class teacherui(QMainWindow):
    def __init__(self):
        super(teacherui, self).__init__()
        uic.loadUi("UI/teacherwindow.ui",self)
        # self.Handel_Buttons()
        self.GET_DATA()

        #Definerer UI filens widgets

        #Hvad widgets skal gøre

        #Viser appen
        self.show()

    # def Handel_Buttons(self):
    #     self.pushButton.clicked.connect(self.GET_DATA)

    def GET_DATA(self):
        dbconnect = dbconnection.get_connection()
        mycursor = dbconnect.cursor()
        query = "SELECT * FROM users"

        # result = mycursor.execute(query)

        # self.tableWidget.setRowCount(0)

        for row in mycursor.execute(query):
            print(row)
            # self.tableWidget.insertRow(row_number)
            # for column_number, data in enumerate(row_data):
            #     self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))


#Initialiserer appen
app = QApplication(sys.argv)
UIWindow = teacherui()
UIWindow.show()
app.exec()
