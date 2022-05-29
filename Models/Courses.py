class Courses:
    courses_list = []

    def __init__(self, courseID: int, year: int, university: str, uniID: int, program: str, programID: int, coursename: str):
        self.__courseID = int(courseID)
        self.__year = int(year)
        self.__university = university
        self.__uniID = int(uniID)
        self.__program = program
        self.__programID = int(programID)
        self.__coursename = coursename
        self.courses_list.append(self)

    def get_courseID(self):
        return self.__courseID

    def set_courseID(self, new_courseID):
        self.__courseID= new_courseID

    def get_year(self):
        return self.__year

    def set_year(self, new_year):
        self.__year = new_year

    def get_university(self):
        return self.__university

    def set_university(self, new_university):
        self.__university = new_university

    def get_uniID(self):
        return self.__uniID

    def set_uniID(self, new_uniID):
        self.__uniID = new_uniID

    def get_program(self):
        return self.__program

    def set_program(self, new_program):
        self.__program = new_program

    def get_programID(self):
        return self.__programID

    def set_programID(self, new_programID):
        self.__programID = new_programID

    def get_coursename(self):
        return self.__coursename

    def set_coursename(self, new_coursename):
        self.__coursename = new_coursename

    # Hvordan vores objekter bliver repræsenteret som string.
    def __str__(self):
        return f"Courses: {self.__courseID}, {self.__coursename}  \nat {self.__university}, program: {self.__program}\nin {self.__year}"



