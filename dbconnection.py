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

connection = get_connection()
mycursor = connection.cursor()
mycursor.execute("SELECT * FROM users")
sqladmin = mycursor.fetchall()
print(sqladmin)
close_connection(connection)


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