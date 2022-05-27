from Models.Classes import Classes
from XML.classesReader import ClassesReader
from XML.classesWriter import ClassesWriter
from Controller import dbconnection

def main():
    db = dbconnection.get_connection()
    cursor = db.cursor()
    query = (
        "SELECT classes.id, classes.location, classes.start, classes.end, classes.courseID, courses.course FROM s206007.classes JOIN s206007.courses WHERE classes.courseid = courses.courseID")
    cursor.execute(query,)
    results = cursor.fetchall()
    print(results)
    objectlist = []
    for result in results:
        objectlist.append(Classes(result[0], result[1], result[2], result[3], result[4], result[5]))
    return objectlist


    objectlist[0].printout()
    LW = ClassesWriter(objectlist[0])
    LW.save()
        #object.erase()


    inter = ClassesReader().get_Classes()
    print(inter)
    # print("Printing the new contents of the pharmacy")
    # pharmacy.printout()


if __name__ == '__main__':
    main()
