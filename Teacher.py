import sys
from PyQt6.QtWidgets import QWidget, QMainWindow, QApplication, QLabel, QLineEdit, QPushButton, QTabWidget, QTableWidget, QListWidgetItem, QMessageBox
from PyQt6 import uic
import dbconnection


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
        query = ("SELECT location, start, end FROM testers WHERE classdate = %s")
        cursor.execute(query, (date,))
        results = cursor.fetchall()
        for result in results:
            #item = QListWidgetItem((result[0]),(result[1]))
            self.ScheduleList.addItems(result)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    TeacherUI = teacherwindowUI()
    TeacherUI.show()
    sys.exit(app.exec())
