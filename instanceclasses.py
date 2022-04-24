class instantiateclasses:
    def __init__(self, id, location, classdate, classstart, classend, courseid):
        self.__id = id
        self.__location = location
        self.__classdate = classdate
        self.__classstart = classstart
        self.__classend = classend
        self.__courseid = courseid

    def set_id(self, new_id):
        self.__id = new_id

    def get_id(self):
        return self.__id

    def set_location(self, new_location):
        self.__location = new_location

    def get_location(self):
        return self.__location

    def set_classdate(self, new_classdate):
        self.__classdate = new_classdate

    def get_classdate(self):
        return self.__classdate

    def set_classstart(self, new_classstart):
        self.__classstart= new_classstart

    def get_classstart(self):
        return self.__classstart

    def set_classend(self, new_classend):
        self.__classend = new_classend

    def get_classend(self):
        return self.__get_classend

    def set_courseid(self, new_courseid):
        self.__courseid = new_courseid

    def get_courseid(self):
        return self.__courseid

    def __str__(self):
        return f"Course: {self.courseid}\nat {self.location} on {self.classdate}\nfrom {self.classstart} until" \
               f" {self.classend}"
