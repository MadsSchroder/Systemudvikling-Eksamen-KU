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

def get_users(users):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        select_query = """select * from defaultdb.users where id =%s"""
        cursor.execute(select_query, (users,))
        records = cursor.fetchall()
        print("Udskriver brugeren med")
        for row in records:
            print("id:", row[0], )
            print("navn:", row[1])
            print("kode:", row[2])
            print("lavet:", row[3])
        close_connection(connection)
    except (Exception, mysql.connector.Error) as error:
        print("Error while getting data", error)

get_users(1)