import sys
from PyQt6 import uic
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QWidget, QMainWindow, QApplication, QTableWidget, QTableWidgetItem
import dbconnection

class teacherui(QMainWindow):
    def __init__(self):
        super(teacherui, self).__init__()
        uic.loadUi("UI/teacherwindow.ui",self)
        self.tableWidget1.setColumnWidth(0, 100)
        self.tableWidget1.setColumnWidth(1, 100)
        self.tableWidget1.setColumnWidth(2, 100)
        self.tableWidget1.setHorizontalHeaderLabels(["Location", "Starttidspunkt", "Sluttidspunks"])
        self.loaddata()

        self.show()

    def loaddata(self):
        #people=[{"name":"John","age":45,"address":"New York"}, {"name":"Mark", "age":40,"address":"LA"}, {"name":"George","age":30,"address":"London"}]
        connection = dbconnection.get_connection()
        cursor = connection.cursor()
        query = "SELECT location, start, end FROM testers WHERE classdate = '2022-04-30'"
        cursor.execute(query)
        cur = cursor.fetchall()
        self.tableWidget1.setRowCount(50)
        tablerow=0
        for row in cur:
            print(row)
            self.tableWidget1.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.tableWidget1.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.tableWidget1.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(row[2]))
            tablerow+=1

#Initialiserer appen
app = QApplication(sys.argv)
UIWindow = teacherui()
UIWindow.show()
app.exec()
