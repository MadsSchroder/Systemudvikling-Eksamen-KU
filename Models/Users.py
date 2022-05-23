class Users:
    users_list = []

    def __init__(self, id, password, usertypeid):
        self.__id = id
        self.__password = password
        self.__usertypeid = usertypeid
        self.users_list.append(self)

    def get_id(self):
        return self.__id

    def set_id(self, new_id):
        self.__id = new_id

    def get_password(self):
        return self.__password

    def set_password(self, new_password):
        self.__password = new_password

    def get_usertypeid(self):
        return self.__usertypeid

    def set_usertypeid(self, new_usertypeid):
        self.__usertypeid = new_usertypeid

    # Streng formattering
    def __str__(self):
        return f" "
