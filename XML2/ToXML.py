from lxml import etree, objectify
from io import BytesIO
from Models.Classes import Classes
from XML2.Elements import Elements


class CoursesToXml:
    def __init__(self, classes: Classes):
        self.classes = classes

    def write_file(self):

        root = etree.Element("Klasser")
        print(self.classes)
        for classes in self.classes.get_classid():
            classes_element = Elements.create_classes(classes)
            root.append(classes_element)
            # create studerende as sub element to the course element

          #  classes =  objectify.SubElement(course_element,"classes")

            # Add all the student items to the student element

           # for classes in course.get_students():
           #     # create the student xml element from the student object
           #     student_element = Elements.create_student(student)
           #     # append the studetn xml element to the students list element.
           #     studerende.append(student_element)

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
