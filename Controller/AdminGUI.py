from PyQt6.QtWidgets import QMainWindow, QListWidgetItem
from PyQt6 import uic
from Controller import dbconnection
from datetime import datetime
from Models.Classes import Classes


class adminwindowUI(QMainWindow):
    def __init__(self, userid):
        super(adminwindowUI, self).__init__()
        uic.loadUi("../Views/adminwindow.ui", self)
        self.__userid = userid
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
        class_list = self.getClasses(dateSelected)
        self.showScheduleOnGivenDate(class_list)
        self.show()

    def showScheduleOnGivenDate(self, classList):
        self.ScheduleList.clear()
        for result in classList:
            item = QListWidgetItem("ClassID: " + str(result.get_id()) + " - " + result.get_coursename() + ", " + result.get_location() + ":" + "\n" +"   fra " + result.get_start() + " til " + result.get_end())
            self.ScheduleList.addItem(item)

    def getClasses(self, date):
        db = dbconnection.get_connection()
        cursor = db.cursor()
        query = (
            "SELECT classes.location, classes.start, classes.end, courses.course, classes.id, classes.courseID FROM s206007.classes join s206007.courses where classes.courseid = courses.courseID AND classes.date = %s")
        cursor.execute(query, (date,), )
        results = cursor.fetchall()
        print(results)
        class_list = []
        for result in results:
            class_list.append(Classes(result[4], result[0], result[1], result[2], result[5], result[3]))
        return class_list

    def showScheduleRequests(self):
        self.ScheduleList2.clear()
        db = dbconnection.get_connection()
        cursor = db.cursor()
        query = ("SELECT changes.id, changes.classesid, changes.location, changes.date, changes.start, changes.end, courses.course FROM s206007.changes join s206007.courses where changes.courseid = courses.courseID")
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
        connection = dbconnection.get_connection()
        cursor = connection.cursor()
        maininput = (location, date, start, end, id)
        query = """INSERT INTO classes(location, date, start, end, courseid) VALUES (%s, %s, %s, %s, %s)"""
        cursor.execute(query, maininput)
        connection.commit()
        cursor.close()
        connection.close()

    def accept_change(self):
        id = self.Line_classid.text()
        dbconnection.APPROVED_CLASS_CHANGE(id)

    def decline_change(self):
        id = self.Line_classid.text()
        dbconnection.DECLINE_CLASS_CHANGE(id)

    def displayInfo(self):
        self.show()

#if __name__ == "__main__":
#    app = QApplication(sys.argv)
#    AdminUI = adminwindowUI()
#    AdminUI.show()
#    sys.exit(app.exec())
