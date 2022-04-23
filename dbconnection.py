import mysql.connector
from mysql.connector import Error
from datetime import date


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
        return (False, "No user found", 0, 0)
    query = ("SELECT password, usertypeid, id FROM users where username = %s")
    mycursor.execute(query, (username,))
    this_password = ""
    this_usertypeid = 0
    this_userid = 0
    for (password) in mycursor:
        this_password = password[0]
        this_usertypeid = password[1]
        this_userid = password[2]
    mycursor.close()
    connection.close()
    if pw == this_password:
        return (True, "Success", this_usertypeid, this_userid)
    else:
        return (False, "Wrong password", 0, 0)

def get_classes(userid):
    connection = get_connection()
    mycursor = connection.cursor()
    query = ("SELECT courseID FROM attendscourse where userid = %s")
    mycursor.execute(query, (userid,))
    this_courseid = 0
    for (course) in mycursor:
        this_courseid = course[0]
    query2 = ("SELECT * FROM classes where courseid = %s")
    class_list=[]
    mycursor.execute(query2, (this_courseid,))
    for (classes) in mycursor:
        class_list.append(classes)
    mycursor.close()
    connection.close()
    return class_list

def get_classes_on_date(userid):
    connection = get_connection()
    mycursor = connection.cursor()
    class_list=[]
    query = ("SELECT courseID FROM attendscourse where userid = %s")
    mycursor.execute(query, (userid,))
    for (classes) in mycursor:
        class_list.append(classes)
    mycursor.close()
    connection.close()
    return class_list


test=check_password("Student", "test")
print(test)

