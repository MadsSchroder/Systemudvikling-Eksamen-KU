import sys
from PyQt6.QtWidgets import QWidget, QMainWindow, QApplication, QLabel, QLineEdit, QPushButton, QTabWidget, QTableWidget, QListWidgetItem, QMessageBox
from PyQt6 import uic
import dbconnection
import datetime

current_userid = 1

class teacherwindowUI(QMainWindow):
    def __init__(self):
        super(teacherwindowUI, self).__init__()
        uic.loadUi("UI/teacherwindow.ui", self)
        self.calendarWidget2.selectionChanged.connect(self.calendarDateChanged)
        self.calendarDateChanged()
        self.sendAnmodning.clicked.connect(self.send_request)

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


    def send_request(self):
        id = self.Line_classid.text()
        location = self.Line_location.text()
        date = self.Line_date.text()
        start = self.Line_start.text()
        end = self.Line_end.text()
        print(id, location, date, start, end)
        dbconnection.REQUEST_CHANGE_CLASS(id, location, date, start, end)

    def displayInfo(self):
        self.show()

#if __name__ == "__main__":
#    app = QApplication(sys.argv)
#    TeacherUI = teacherwindowUI()
#    TeacherUI.show()
#    sys.exit(app.exec())
