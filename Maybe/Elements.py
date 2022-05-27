from lxml import objectify
from Models.Users import Users
from Models.Classes import Classes


class Elements:
    @staticmethod
    def create_student(student_obj: Users):
        # define the name of the xml element
        student = objectify.Element("student")
        # add the attributes
        # note the decoupling of the XML tag names from the object attributes
        # (compared to the first example)
        student.id = student_obj.get_id()
        return student

    @staticmethod
    def create_course(course_obj: Classes):
        course = objectify.Element("kursus")
        course.kursusID = course_obj.get_courseID()
        course.kursusnavn = course_obj.get_coursename()
        # note that we haven't appended the student list - it will be handled elsewhere
        return course
