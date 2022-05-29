class Classes:
    classes_list = []

    def __init__(self, classid: int, location: str, date: str, start: str, end: str, classcourseID: int, coursename: str, courseID: int, year: int, university: str, uniID: int, program: str, programID: int):
        self.__classid = int(classid)
        self.__location = location
        self.__date = date
        self.__start = start
        self.__end = end
        self.__classcourseID = int(classcourseID)
        self.__coursename = coursename
        self.__courseID = int(courseID)
        self.__year = int(year)
        self.__university = university
        self.__uniID = int(uniID)
        self.__program = program
        self.__programID = int(programID)
        self.classes_list.append(self)

    def get_classid(self):
        return self.__classid

    def set_classid(self, new_classid):
        self.__classid = new_classid

    def get_location(self):
        return self.__location

    def set_location(self, new_location):
        self.__location = new_location

    def get_date(self):
        return self.__date

    def set_date(self, new_date):
        self.__date = new_date

    def get_start(self):
        return self.__start

    def set_start(self, new_start):
        self.__start = new_start

    def get_end(self):
        return self.__end

    def set_end(self, new_end):
        self.__end = new_end

    def get_classcourseID(self):
        return self.__classcourseID

    def set_classcourseID(self, new_classcourseID):
        self.__classcourseID= new_classcourseID

    def get_coursename(self):
        return self.__coursename

    def set_coursename(self, new_coursename):
        self.__coursename = new_coursename

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

    # Hvordan vores objekter bliver repræsenteret som string.
    def __str__(self):
        return f"Course: {self.__classid}\nat {self.__location} on {self.__start}\nfrom {self.__end} until" \
               f" {self.__coursename}"


