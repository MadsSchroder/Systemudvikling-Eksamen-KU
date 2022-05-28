from Models.Classes import Classes
from XML.classesReader import ClassesReader
from XML.classesWriter import ClassesWriter
from Controller import dbconnection

def main():
    #Definerer main
    db = dbconnection.get_connection()
    cursor = db.cursor()
    query = ("SELECT classes.id, classes.location, classes.start, classes.end, classes.courseID, courses.course FROM s206007.classes JOIN s206007.courses WHERE classes.courseid = courses.courseID")

    cursor.execute(query)
    results = cursor.fetchall()
    objectlist = []
    for result in results:
        objectlist.append(Classes(str(result[0]), str(result[1]), str(result[2]), str(result[3]), str(result[4]), str(result[5])))



    objectlist[0].get_location()
    Classes_Writer =  ClassesWriter(objectlist[3])
    Classes_Writer.save()

    print(ClassesReader().get_Classes())




if __name__ == '__main__':
    main()
