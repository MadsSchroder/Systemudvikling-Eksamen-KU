import mysql.connector
from mysql.connector import Error
from datetime import date
import Models.Classes
from Models.Users import Users

def get_connection():
    connection = mysql.connector.connect(
        host='mysql-db.caprover.diplomportal.dk',
        user='s206007',
        password='wFaRtFVTr9H9VqakBsN91',
        database='s206007')
    return connection

def close_connection(connection):
    if connection:
        connection.close()

def check_username(username):
    connection = get_connection()
    mycursor = connection.cursor()
    query = ("SELECT * FROM s206007.users where username = %s")
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
    query = ("SELECT id, password, usertypeid FROM s206007.users where username = %s")
    mycursor.execute(query, (username,))
    results = mycursor.fetchall()
    print(results)
    users_list = []
    for result in results:
        users_list.append(Users(result[0], result[1], result[2]))
    if pw == result[1]:
        return (True, "Success", result[2], result[0])
    else:
        return (False, "Wrong password", 0, 0)

def get_classes(userid):
    connection = get_connection()
    mycursor = connection.cursor()
    query = ("SELECT courseID FROM s206007.attendscourse where userid = %s")
    mycursor.execute(query, (userid,))
    this_courseids = []
    for (course) in mycursor:
        this_courseids.append(course)
    query2 = ("SELECT * FROM s206007.classes where courseid = %s")
    class_list=[]
    for (courses) in this_courseids:
        mycursor.execute(query2, (courses[0],))
        for (classes) in mycursor:
            class_list.append(classes)
    mycursor.close()
    connection.close()
    return class_list

def get_classes_on_date(userid):
    connection = get_connection()
    mycursor = connection.cursor()
    class_list=[]
    query = ("SELECT courseID FROM s206007.attendscourse where userid = %s")
    mycursor.execute(query, (userid,))
    for (classes) in mycursor:
        class_list.append(classes)
    mycursor.close()
    connection.close()
    return class_list

def CREATE_NEW_CLASSES(location, date, start, end, id):
    connection = get_connection()
    cursor = connection.cursor()
    maininput = (location, date, start, end, id)
    query = """INSERT INTO s206007.classes(location, date, start, end, courseid) VALUES (%s, %s, %s, %s, %s)"""
    cursor.execute(query, maininput)
    connection.commit()
    cursor.close()
    connection.close()

def UPDATE_LOCATION_CLASSES(location, id):
    connection = get_connection()
    cursor = connection.cursor()
    maininput = (location, id)
    query = """UPDATE s206007.classes SET location = (%s) WHERE id = (%s)"""
    cursor.execute(query, maininput,)
    connection.commit()
    cursor.close()
    connection.close()

def UPDATE_DATE_CLASSES(date, id):
    connection = get_connection()
    cursor = connection.cursor()
    maininput = (date, id)
    query = """UPDATE classes SET date = (%s) WHERE id = (%s)"""
    cursor.execute(query, maininput,)
    connection.commit()
    cursor.close()
    connection.close()

def UPDATE_TIMESTART_CLASSES(start, id):
    connection = get_connection()
    cursor = connection.cursor()
    maininput = (start, id)
    query = """UPDATE classes SET start = (%s) WHERE id = (%s)"""
    cursor.execute(query, maininput,)
    connection.commit()
    cursor.close()
    connection.close()

def UPDATE_TIMEEND_CLASSES(end, id):
    connection = get_connection()
    cursor = connection.cursor()
    maininput = (end, id)
    query = """UPDATE classes SET end = (%s) WHERE id = (%s)"""
    cursor.execute(query, maininput,)
    connection.commit()
    cursor.close()
    connection.close()

def CREATE_CHANGE_FROM_CLASS(id):
    connection = get_connection()
    cursor = connection.cursor()
    query = """SELECT * FROM changes WHERE classesid = %s"""
    cursor.execute(query, (id, ))
    existing = cursor.fetchall()
    if existing != []:
        return
    query1 = """SELECT * FROM classes WHERE id = %s"""
    cursor.execute(query1, (id,))
    this_data = ()
    for (data) in cursor:
        this_data = data
    query2 = """INSERT INTO changes(classesid, location, date, start, end, courseid) VALUES (%s, %s, %s, %s, %s, %s)"""
    cursor.execute(query2, this_data)
    connection.commit()
    cursor.close()
    connection.close()

def UPDATE_LOCATION_CHANGES(location, id):
    connection = get_connection()
    cursor = connection.cursor()
    maininput = (location, id)
    query = """UPDATE changes SET location = (%s) WHERE classesid = (%s)"""
    cursor.execute(query, maininput,)
    connection.commit()
    cursor.close()
    connection.close()

def UPDATE_DATE_CHANGES(date, id):
    connection = get_connection()
    cursor = connection.cursor()
    maininput = (date, id)
    query = """UPDATE changes SET date = (%s) WHERE classesid = (%s)"""
    cursor.execute(query, maininput,)
    connection.commit()
    cursor.close()
    connection.close()

def UPDATE_TIMESTART_CHANGES(start, id):
    connection = get_connection()
    cursor = connection.cursor()
    maininput = (start, id)
    query = """UPDATE changes SET start = (%s) WHERE classesid = (%s)"""
    cursor.execute(query, maininput,)
    connection.commit()
    cursor.close()
    connection.close()

def UPDATE_TIMEEND_CHANGES(end, id):
    connection = get_connection()
    cursor = connection.cursor()
    maininput = (end, id)
    query = """UPDATE changes SET end = (%s) WHERE classesid = (%s)"""
    cursor.execute(query, maininput,)
    connection.commit()
    cursor.close()
    connection.close()

def REQUEST_CHANGE_CLASS(id, location, date, start, end):
    CREATE_CHANGE_FROM_CLASS(id)
    if location != "":
        UPDATE_LOCATION_CHANGES(location, id)
    if date != "":
        UPDATE_DATE_CHANGES(date, id)
    if start != "":
        UPDATE_TIMESTART_CHANGES(start, id)
    if end != "":
        UPDATE_TIMEEND_CHANGES(end, id)

def CHANGE_CLASS(id, location, date, start, end):
    if location != "":
        UPDATE_LOCATION_CLASSES(location, id)
    if date != "":
        UPDATE_DATE_CLASSES(date, id)
    if start != "":
        UPDATE_TIMESTART_CLASSES(start, id)
    if end != "":
        UPDATE_TIMEEND_CLASSES(end, id)

def APPROVED_CLASS_CHANGE(id):
    connection = get_connection()
    cursor = connection.cursor()
    query = """SELECT classesid, location, date, start, end FROM changes WHERE classesid = %s"""
    cursor.execute(query, (id,))
    this_data = ()
    for (data) in cursor:
        this_data = data
    cursor.close()
    connection.close()
    CHANGE_CLASS(this_data[0], this_data[1], this_data[2], this_data[3], this_data[4])
    DECLINE_CLASS_CHANGE(id)

def DECLINE_CLASS_CHANGE(id):
    connection = get_connection()
    cursor = connection.cursor()
    query = "DELETE FROM changes WHERE classesid = %s"
    cursor.execute(query, (id,))
    connection.commit()
    cursor.close()
    connection.close()
