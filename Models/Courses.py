from datetime import date
from stdnum.dk import cpr
from Models.Classes import Classes


class Courses:
    """
    class to represent a list of Courses
    """

    def __init__(self):
        self.classes = []

    def append_course(self, classes: Classes):
        self.classes.append(classes)

    def get_courses(self): return self.classes
