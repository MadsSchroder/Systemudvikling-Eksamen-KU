class Users:
    users_list = []

    def __init__(self, id: int, username: str, password: str, fname: str, lname: str, email: str, CPR: int, address: str, usertypeid: int):
        self.__id = int(id)
        self.__username = username
        self.__password = password
        self.__fname = fname
        self.__lname = lname
        self.__email = email
        self.__cpr = int(CPR)
        self.__address = address
        self.__usertypeid = int(usertypeid)
        self.users_list.append(self)


    def get_id(self):
        return self.__id

    def get_username(self):
        return self.__username

    def set_username(self, new_username):
        self.__username = new_username

    def get_password(self):
        return self.__password

    def set_password(self, new_password):
        self.__password = new_password

    def get_fname(self):
        return self.__fname

    def set_fname(self, new_fname):
        self.__fname = new_fname

    def get_lname(self):
        return self.__lname

    def set_lname(self, new_lname):
        self.__lname = new_lname

    def get_email(self):
        return self.__email

    def set_email(self, new_email):
        self.__email = new_email

    def get_cpr(self):
        return self.__cpr

    def set_cpr(self, new_cpr):
        self.__cpr = int(new_cpr)

    def get_address(self):
        return self.__address

    def set_address(self, new_address):
        self.__address = new_address

    def get_usertypeid(self):
        return self.__usertypeid

    def set_usertypeid(self, new_usertypeid):
        self.__usertypeid = int(new_usertypeid)

    # Hvordan vores objekter bliver repræsenteret som string.
    def __str__(self):
        return f"Bruger: {self.__fname}, {self.__lname}\n email:{self.__email}, addresse: {self.__address}"
