import sys
from PyQt6.QtWidgets import QWidget, QMainWindow, QApplication, QLabel, QLineEdit, QPushButton, QTabWidget, QTableWidget, QListWidgetItem, QMessageBox
from PyQt6 import uic
import dbconnection
import datetime

current_userid = 0

class teacherwindowUI(QMainWindow):
    def __init__(self):
        super(teacherwindowUI, self).__init__()
        uic.loadUi("UI/teacherwindow.ui", self)
        self.calendarWidget2.selectionChanged.connect(self.calendarDateChanged)
        self.calendarDateChanged()

    def calendarDateChanged(self):
        print("The calender date was changed")
        dateSelected = self.calendarWidget2.selectedDate().toPyDate()
        print("Date Selected:", dateSelected)
        self.showScheduleOnGivenDate(dateSelected)

    def showScheduleOnGivenDate(self, date):
        self.ScheduleList.clear()
        db = dbconnection.get_connection()
        cursor = db.cursor()
        query = ("SELECT classes.location, classes.classstart, classes.classend, courses.course FROM defaultdb.classes join defaultdb.courses where classes.courseid = courses.courseID AND classes.classdate = %s")
        cursor.execute(query, (date,))
        results = cursor.fetchall()
        print("hej")
        print(results)
        for result in results:
            print(str(result[1]))
            item = QListWidgetItem(result[3] + " " + result[0] + " " + result[1] + " " + result[2])
            self.ScheduleList.addItem(item)

    def showWindow(self, verification):
        print(verification)
        uic.loadUi("UI/teacherwindow.ui", self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    TeacherUI = teacherwindowUI()
    TeacherUI.show()
    sys.exit(app.exec())
