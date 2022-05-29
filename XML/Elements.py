from lxml import objectify
from Models.Classes import Classes
from Models.Courses import Courses

class Elements:
    @staticmethod
    def create_class(classes_obj: Classes):
        # define the name of the xml element
        Classes = objectify.Element("Classes")
        # add the attributes
        # note the decoupling of the XML tag names from the object attributes
        # (compared to the first example)
        Classes.classid = classes_obj.get_classid()
        Classes.location = classes_obj.get_location()
        Classes.date = classes_obj.get_date()
        Classes.start = classes_obj.get_start()
        Classes.end = classes_obj.get_end()
        Classes.classcourseID = classes_obj.get_classcourseID()
        Classes.coursename = classes_obj.get_coursename()
        return Classes

    @staticmethod
    def create_course(courses_obj: Courses):
        courses = objectify.Element("kursus")
        courses.courseID = courses_obj.get_courseID()
        courses.year = courses_obj.get_year()
        courses.university = courses_obj.get_university()
        courses.uniID = courses_obj.get_uniID()
        courses.program = courses_obj.get_program()
        courses.programID = courses_obj.get_programID()
        courses.coursename = courses_obj.get_coursename()
        courses.classesincourse = courses_obj.get_classesincourse()
        # note that we haven't appended the student list - it will be handled elsewhere
        return courses
