class Classes:
    classes_list = []

    def __init__(self, id, location, start, end, coursename):
        self.__id = id
        self.__location = location
        self.__start = start
        self.__end = end
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

    def get_coursename(self):
        return self.__coursename

    def set_coursename(self, new_coursename):
        self.__coursename = new_coursename

    # Streng formattering
    def __str__(self):
        return f" "
