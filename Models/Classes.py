class Classes:
    classes_list = []

    def __init__(self, classid: int, location: str, date: str, start: str, end: str, classcourseID: int, coursename: str):
        self.__classid = int(classid)
        self.__location = location
        self.__date = date
        self.__start = start
        self.__end = end
        self.__classcourseID = int(classcourseID)
        self.__coursename = coursename
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


    # Hvordan vores objekter bliver repræsenteret som string.
    def __str__(self):
        return f"Course: {self.__classid}\nat {self.__location} on {self.__start}\nfrom {self.__end} until" \
               f" {self.__coursename}"


