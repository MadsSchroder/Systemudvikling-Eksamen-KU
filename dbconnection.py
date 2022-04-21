import mysql.connector
from mysql.connector import Error

def get_connection():
    connection = mysql.connector.connect(
        host='uniskemadb-do-user-11280721-0.b.db.ondigitalocean.com',
        port=25060,
        database='defaultdb',
        user='doadmin',
        password='AVNS_qt-pIDU320VjzTt')
    return connection

def close_connection(connection):
    if connection:
        connection.close()

def check_username(username):
    connection = get_connection()
    mycursor = connection.cursor()
    query = ("SELECT * FROM users where username = %s")
    mycursor.execute(query, (username,))
    myresult=mycursor.fetchall()
    if myresult:
        return True
    else:
        return False


def check_password(username, pw):
    connection = get_connection()
    mycursor = connection.cursor()
    if not check_username(username):
        return (False, "No user found", 0)
    query = ("SELECT password, usertypeid FROM users where username = %s")
    mycursor.execute(query, (username,))
    this_password = ""
    this_usertypeid = 0
    for (password) in mycursor:
        this_password = password[0]
        this_usertypeid = password[1]
    #print(this_password)
    mycursor.close()
    connection.close()
    if pw == this_password:
        return (True, "Success", this_usertypeid)
    else:
        return (False, "Wrong password", 0)


#test=check_password("Admin", "test")
#print(test)


# def get_users(users):
#     try:
#         connection = get_connection()
#         cursor = connection.cursor()
#         connection = get_connection()
#         mycursor = connection.cursor()
#         mycursor.execute("SELECT * FROM users")
#         sqladmin = mycursor.fetchall()
#         print(sqladmin)
#         close_connection(connection)
#     except (Exception, mysql.connector.Error) as error:
#         print("Error while getting data", error)
#
# get_users(1)