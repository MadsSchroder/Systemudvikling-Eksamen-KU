import mysql.connector

mydb = mysql.connector.connect(
    host="uniskemadb-do-user-11280721-0.b.db.ondigitalocean.com",
    user="doadmin",
    password="AVNS_qt-pIDU320VjzTt",
    database="defaultdb")

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM lectures")
sqllec = mycursor.fetchall()