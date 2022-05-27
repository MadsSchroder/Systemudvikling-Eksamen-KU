from lxml import etree, objectify
from io import BytesIO
from Models.Courses import Courses
from Models.Users import Users
from Elements import Elements
from Controller.dbconnection import get_connection

class CoursesToXml:
    def __init__(self, courses: Courses):
        self.courses = courses

    def write_file(self):

        root = etree.Element("kurser")
        for classes in self.courses.get_courses():
            class_element = Elements.create_course(classes)
            root.append(class_element)
            # create studerende as sub element to the course element

            studerende =  objectify.SubElement(class_element,"studerende")

            # Add all the student items to the student element
            connection = get_connection()
            mycursor = connection.cursor()
            query = ("SELECT userid FROM s206007.attendscourse where courseID = %s")
            mycursor.execute(query, (self.courses.get_courses,))
            for (student) in mycursor:
                # create the student xml element from the student object
                student = Elements.create_student(student)
                # append the studetn xml element to the students list element.
                studerende.append(student)

        # Do some cleanup
        # remove lxml annotation
        objectify.deannotate(root)
        etree.cleanup_namespaces(root)

        # create the xml string
        parser = etree.XMLParser(remove_blank_text=True)
        file_obj = BytesIO(etree.tostring(root))
        tree = etree.parse(file_obj, parser)

        # Write the xml string to a file
        try:
            with open("courses.xml", "wb") as xml_writer:
                tree.write(xml_writer, pretty_print=True, encoding='utf-8', xml_declaration=True)
        except IOError:
            pass
