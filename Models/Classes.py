class Classes:
    classes_list = []

    def __init__(self, id: int, location: str, start: str, end: str, courseID: int, coursename: str):
        self.__id = id
        self.__location = location
        self.__start = start
        self.__end = end
        self.__courseID = courseID
        self.__coursename = coursename
        self.classes_list.append(self)

    def get_id(self):
        return self.__id

    def set_id(self, new_id):
        self.__id = new_id

    def get_location(self):
        return self.__location

    def set_location(self, new_location):
        self.__location = new_location

    def get_start(self):
        return self.__start

    def set_start(self, new_start):
        self.__start = new_start

    def get_end(self):
        return self.__end

    def set_end(self, new_end):
        self.__end = new_end

    def get_courseID(self):
        return self.__courseID

    def set_courseID(self, new_courseID):
        self.__courseID= new_courseID

    def get_coursename(self):
        return self.__coursename

    def set_coursename(self, new_coursename):
        self.__coursename = new_coursename

    # Hvordan vores objekter bliver repræsenteret som string.
    def __str__(self):
        return f"Course: {self.__id}\nat {self.__location} on {self.__start}\nfrom {self.__end} until" \
               f" {self.__coursename}"


