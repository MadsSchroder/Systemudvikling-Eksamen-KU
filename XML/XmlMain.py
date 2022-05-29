from Models.Classes import Classes
from XML.classesReader import ClassesReader
from XML.classesWriter import ClassesWriter
from Controller import dbconnection

def main():
    #Definerer main
    db = dbconnection.get_connection()
    cursor = db.cursor()
    #query = ("SELECT classes.id, classes.location, classes.start, classes.end, classes.courseID, courses.course FROM s206007.classes JOIN s206007.courses WHERE classes.courseid = courses.courseID")
    query = (
        "SELECT classes.id, classes.location, classes.date, classes.start, classes.end, classes.courseid, courses.course, courses.courseid, courses.year, university.university, university.id, program.program, program.id FROM s206007.classes JOIN s206007.courses, s206007.program, s206007.university WHERE classes.courseid = courses.courseID AND courses.program = program.id AND courses.university = university.id")

    cursor.execute(query)
    results = cursor.fetchall()
    objectlist = []
    for result in results:
        #objectlist.append(Classes(str(result[0]), str(result[1]), str(result[2]), str(result[3]), str(result[4]), str(result[5])))
        objectlist.append(Classes(str(result[0]), str(result[1]), str(result[2]), str(result[3]), str(result[4]), str(result[5]), str(result[6]), str(result[7]), str(result[8]), str(result[9]), str(result[10]), str(result[11]), str(result[12])))
    objectlist[0].get_location()
    Classes_Writer =  ClassesWriter(objectlist[1])
    Classes_Writer.save()

    print(ClassesReader().get_Classes())




if __name__ == '__main__':
    main()
