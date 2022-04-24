import sys
from PyQt6.QtWidgets import QWidget, QMainWindow, QApplication, QLabel, QLineEdit, QPushButton, QTabWidget, QTableWidget, QListWidgetItem, QMessageBox
from PyQt6 import uic
import dbconnection
from datetime import datetime

current_userid = 1

class adminwindowUI(QMainWindow):
    def __init__(self):
        super(adminwindowUI, self).__init__()
        uic.loadUi("UI/adminwindow.ui", self)
        self.calendarWidget.selectionChanged.connect(self.calendarDateChanged)
        self.calendarDateChanged()
        self.showScheduleRequests()
        self.hent_anmodninger.clicked.connect(self.showScheduleRequests)
        self.make_class.clicked.connect(self.create_new_class)
        self.GodkendAnmodning.clicked.connect(self.accept_change)
        self.AfvisAnmodning.clicked.connect(self.decline_change)

    def calendarDateChanged(self):
        print("The calender date was changed")
        dateSelected = self.calendarWidget.selectedDate().toPyDate()
        print("Date Selected:", dateSelected)
        self.showScheduleOnGivenDate(dateSelected)

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
            item = QListWidgetItem("ClassID: " + str(result[4]) + " - " + result[3] + ", " + result[0] + ":" + "\n" +"   fra " + result[1] + ", til " + result[2])
            self.ScheduleList.addItem(item)

    def showScheduleRequests(self):
        self.ScheduleList2.clear()
        db = dbconnection.get_connection()
        cursor = db.cursor()
        query = ("SELECT changes.id, changes.classesid, changes.location, changes.date, changes.start, changes.end, courses.course FROM defaultdb.changes join defaultdb.courses where changes.courseid = courses.courseID")
        cursor.execute(query)
        results = cursor.fetchall()
        print(results)
        for result in results:
            item = QListWidgetItem("ClassID: " + str(result[1]) + " - " + result[6] + ", " + result[2] + ": d. " + datetime.strftime(result[3], "%Y-%m-%d") +  " fra " + result[4] + " til " + result[5])
            self.ScheduleList2.addItem(item)

    def create_new_class(self):
        id = self.Line_courseid.text()
        location = self.Line_location.text()
        date = self.Line_date.text()
        start = self.Line_start.text()
        end = self.Line_end.text()
        print(id, location, date, start, end)
        dbconnection.CREATE_NEW_CLASSES(location, date, start, end, id)

    def accept_change(self):
        id = self.Line_classid.text()
        dbconnection.APPROVED_CLASS_CHANGE(id)

    def decline_change(self):
        id = self.Line_classid.text()
        dbconnection.DECLINE_CLASS_CHANGE(id)

    def displayInfo(self):
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    AdminUI = adminwindowUI()
    AdminUI.show()
    sys.exit(app.exec())
