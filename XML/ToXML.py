from lxml import etree, objectify
from io import BytesIO
from Models.Classes import Classes
from Models.Courses import Courses
from XML.Elements import Elements


class CoursesToXml:
    def __init__(self, classes: Classes):
        self.classes = classes

    def write_file(self):

        root = etree.Element("Klasser")
        for classes in self.classes:
            classes_element = Elements.create_class(classes)
            root.append(classes_element)
            # create studerende as sub element to the course element

            #classesincourse =  objectify.SubElement(course_element,"classes")

            # Add all the student items to the student element

            #for classes in self.courses.get_classesincourse():
                #create the student xml element from the student object
                #class_element = Elements.create_class(classes)
                #append the studetn xml element to the students list element.
                #classesincourse.append(class_element)

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
            with open("../XML/data/classes.xml", "wb") as xml_writer:
                tree.write(xml_writer, pretty_print=True, encoding='utf-8', xml_declaration=True)
        except IOError:
            pass
