import sys
from PyQt6.QtWidgets import QWidget, QMainWindow, QApplication, QLabel, QLineEdit, QPushButton, QTabWidget, QTableWidget, QListWidgetItem, QMessageBox
from PyQt6 import uic
import dbconnection
import datetime

current_userid = 1

class studentwindowUI(QMainWindow):
    def __init__(self):
        super(studentwindowUI, self).__init__()
        uic.loadUi("UI/studentwindow.ui", self)
        self.calendarWidget2.selectionChanged.connect(self.calendarDateChanged)
        self.calendarDateChanged()

    def calendarDateChanged(self):
        print("The calender date was changed")
        dateSelected = self.calendarWidget2.selectedDate().toPyDate()
        print("Date Selected:", dateSelected)
        self.showScheduleOnGivenDate(dateSelected)
        self.show()

    def showScheduleOnGivenDate(self, date):
        self.ScheduleList.clear()
        db = dbconnection.get_connection()
        cursor = db.cursor()
        query = ("SELECT classes.location, classes.classstart, classes.classend, courses.course, classes.id FROM defaultdb.classes join defaultdb.courses where classes.courseid = courses.courseID AND classes.classdate = %s")
        cursor.execute(query, (date,))
        results = cursor.fetchall()
        print(results)
        for result in results:
            print(str(result[1]))
            item = QListWidgetItem("ClassID: " + str(result[4]) + " - " + result[3] + ", " + result[0] + ":" + "\n" +"   fra " + result[1] + " til " + result[2])
            self.ScheduleList.addItem(item)

    def displayInfo(self):
        self.show()
