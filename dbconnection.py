import mysql.connector
from mysql.connector import Error
from datetime import date
from instanceclasses import instantiateclasses

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

# def get_classes_on_datess():
#     connection = get_connection()
#     mycursor = connection.cursor()
#     query = ("SELECT * FROM classes")
#     mycursor.execute(query)
#     class_list = []
#     result = mycursor.fetchall()
#     for row in result:
#         class_list.append(row)
#     mycursor.close()
#     connection.close()
#     return class_list

def testere():
    connection = get_connection()
    mycursor = connection.cursor()
    new = testlist = []
    query = ("SELECT * FROM classes")
    mycursor.execute(query)
    classfetch = mycursor.fetchall()
    for (classeslist) in range(len(classfetch)):
        testlist.append(
            instantiateclasses(classfetch[classeslist][0], classfetch[classeslist][1], classfetch[classeslist][2],
                    classfetch[classeslist][3], classfetch[classeslist][4], classfetch[classeslist][5]))

    return new

def CREATE_NEW_CLASSES(location, date, start, end, id):
    connection = get_connection()
    cursor = connection.cursor()
    maininput = (location, date, start, end, id)
    query = """INSERT INTO classes(location, classdate, classstart, classend, courseid) VALUES (%s, %s, %s, %s, %s)"""
    cursor.execute(query, maininput)
    connection.commit()
    cursor.close()
    connection.close()

def UPDATE_LOCATION(location, id):
    connection = get_connection()
    cursor = connection.cursor()
    maininput = (location, id)
    query = """UPDATE classes SET location = (%s) WHERE id = (%s)"""
    cursor.execute(query, maininput,)
    connection.commit()
    cursor.close()
    connection.close()

def UPDATE_DATE(date, id):
    connection = get_connection()
    cursor = connection.cursor()
    maininput = (date, id)
    query = """UPDATE classes SET classdate = (%s) WHERE id = (%s)"""
    cursor.execute(query, maininput,)
    connection.commit()
    cursor.close()
    connection.close()

def UPDATE_TIME(start, end, id):
    connection = get_connection()
    cursor = connection.cursor()
    maininput = (start, end, id)
    query = """UPDATE classes SET classstart = (%s), classend = (%s) WHERE id = (%s)"""
    cursor.execute(query, maininput,)
    connection.commit()
    cursor.close()
    connection.close()


#CREATE_NEW_CLASSES('Programmering - fra python','2022-04-30','08:00:00','17:00:00', 1)
#UPDATE_LOCATION('Python', 11)
#UPDATE_DATE('2022-04-01', 11)
#UPDATE_TIME('08:00:00', '13:00:00', 11)
#get_classes_on_datess()
#print(get_classes_on_datess)
