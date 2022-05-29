from PyQt6.QtWidgets import QMainWindow, QListWidgetItem
from PyQt6 import uic
from Controller import dbconnection
from datetime import datetime
from Models.Classes import Classes
from XML.ToXML import CoursesToXml
from XML.FromXML import ClassesReader
from lxml import etree, objectify


from Models.Courses import Courses

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
        self.xml_knap.clicked.connect(self.writeXML)
        self.xml_knap_2.clicked.connect(self.readXML)
        self.Uni_knap.clicked.connect(self.findUNI)

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
            item = QListWidgetItem("ClassID: " + str(result.get_classid()) + " - " + result.get_coursename() + ", " + result.get_location() + ":" + "\n" +"   fra " + result.get_start() + " til " + result.get_end())
            self.ScheduleList.addItem(item)

    def getClasses(self, date):
        db = dbconnection.get_connection()
        cursor = db.cursor()
        query = ("SELECT classes.id, classes.location, classes.date, classes.start, classes.end, classes.courseid, courses.course, courses.courseid, courses.year, university.university, university.id, program.program, program.id FROM s206007.classes JOIN s206007.courses, s206007.program, s206007.university WHERE classes.courseid = courses.courseID AND courses.program = program.id AND courses.university = university.id AND classes.date = %s")
        cursor.execute(query, (date,), )
        results = cursor.fetchall()
        print(results)
        class_list = []
        for result in results:
            class_list.append(Classes(result[0], result[1], result[2], result[3], result[4], result[5], result[6]))
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

    def writeXML(self):
        id = self.line_kursusid.text()
        input = (id,)

        # Create some nested objects: a courseList with som dummy courses-each with its own list of students
        print("Taking objects from DB")
        db = dbconnection.get_connection()
        cursor = db.cursor()
        query = (
            "SELECT classes.id, classes.location, classes.date, classes.start, classes.end, classes.courseid, courses.course FROM s206007.classes JOIN s206007.courses WHERE classes.courseid = courses.courseID AND classes.courseid = %s")
        cursor.execute(query, input)
        classresults = cursor.fetchall()
        class_list = []
        for result in classresults:
            class_list.append(Classes(result[0], result[1], result[2], result[3], result[4], result[5], result[6]))
        print("Write the following: ", class_list, " to XML/data/classes.xml")
        CoursesToXml(class_list).write_file()

    def readXML(self):
        inter = ClassesReader().get_Classes()
        print(inter)  # print(

        #dtd = etree.DTD(open('courses.dtd'))
        #print("check generated courses.xml", dtd.validate(etree.parse('courses.xml')))
        #print("check invalid courses_invalid.xml", dtd.validate(etree.parse('courses_invalid.xml')))

    def findUNI(self):
        self.Uni_list.clear()
        Uninr = self.Universitet.text()

        input = (Uninr,)
        db = dbconnection.get_connection()
        cursor = db.cursor()
        query = (
            #"SELECT * FROM s206007.courses JOIN s206007.university, s206007.programs WHERE university.courseid = courses.courseID AND course classes.courseid = %s")
            "SELECT program.program, courses.courseid, courses.course, university.university FROM s206007.courses JOIN s206007.university, s206007.program WHERE university.id = courses.university AND program.id = courses.program AND university.id= %s")
        cursor.execute(query, input)
        results = cursor.fetchall()
        print(results)
        for result in results:
            item = QListWidgetItem("Studieretning: " + str(result[0]) + ", Kursusid: " + str(result[1]) + ", fag:  " + str(result[2]))
            self.Uni_list.addItem(item)
            self.Uni_label.setText(result[3])

    def displayInfo(self):
        self.show()
