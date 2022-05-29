class Changes:
    changes_list = []
    courseid = 0

    def __init__(self, id: int, location: str, date: str, start: str, end: str, courseid: int):
        self.__id = int(id)
        self.__location = location
        self.__date = date
        self.__start = start
        self.__end = end
        self.__courseid = int(courseid)
        self.changes_list.append(self)

    def get_id(self):
        return self.__id

    def set_id(self, new_id):
        self.__id = int(new_id)

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

    def get_courseid(self):
        return self.__courseid

    def set_courseid(self, new_courseid):
        self.__courseid = int(new_courseid)
