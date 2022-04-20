import mysql.connector

mydb = mysql.connector.connect(
    host='uniskemadb-do-user-11280721-0.b.db.ondigitalocean.com',
    port=25060,
    database='defaultdb',
    user='doadmin',
    password='AVNS_qt-pIDU320VjzTt')


mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM users")
sqladmin = mycursor.fetchall()

def doQuery()
print(sqladmin)