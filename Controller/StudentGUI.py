from PyQt6.QtWidgets import QMainWindow, QListWidgetItem
from PyQt6 import uic
from Controller import dbconnection
from Models.Classes import Classes



class studentwindowUI(QMainWindow):
    def __init__(self, userid):
        super(studentwindowUI, self).__init__()
        uic.loadUi("../Views/studentwindow.ui", self)
        self.__userid = userid
        self.calendarWidget2.selectionChanged.connect(self.calendarDateChanged)
        self.calendarDateChanged()


    def calendarDateChanged(self):
        print("The calender date was changed")
        dateSelected = self.calendarWidget2.selectedDate().toPyDate()
        print("Date Selected:", dateSelected)
        class_list = self.getClasses(dateSelected)
        self.showScheduleOnGivenDate(class_list)
        self.show()

    def showScheduleOnGivenDate(self, classList):
        self.ScheduleList.clear()
        for result in classList:
            item = QListWidgetItem("ClassID: " + str(result.get_classid()) + " - " + result.get_coursename() + ", " + result.get_location() + ":" + "\n" +"   fra " + result.get_start() + " til " + result.get_end())
            self.ScheduleList.addItem(item)

    def getClasses(self, date):
        db = dbconnection.get_connection()
        cursor = db.cursor()
        query = ("SELECT classes.id, classes.location, classes.date, classes.start, classes.end, classes.courseid, courses.course, courses.courseid, courses.year, university.university, university.id, program.program, program.id FROM s206007.classes JOIN s206007.courses, s206007.program, s206007.university, s206007.attendscourse WHERE classes.courseid = courses.courseID AND courses.program = program.id AND courses.university = university.id AND attendscourse.courseID = classes.courseid AND classes.date = %s AND attendscourse.userid = %s")
            #"SELECT classes.location, classes.start, classes.end, courses.course, classes.id, classes.courseID FROM s206007.classes JOIN s206007.courses, s206007.attendscourse WHERE classes.courseid = courses.courseID AND attendscourse.courseID = classes.courseid AND classes.date = %s AND attendscourse.userid = %s")
        cursor.execute(query, (date, self.__userid), )
        results = cursor.fetchall()
        print(results)
        class_list = []
        for result in results:
            class_list.append(Classes(result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7], result[8], result[9], result[10], result[11], result[12]))
        return class_list
