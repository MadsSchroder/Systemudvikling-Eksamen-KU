from lxml import etree, objectify
from io import BytesIO
from Models.Classes import Classes
from XML.Elements import Elements
#This code is inspired from the course cookbook


class CoursesToXml:
    def __init__(self, classes: Classes):
        self.classes = classes

    def write_file(self):

        root = etree.Element("Klasser")
        for classes in self.classes:
            classes_element = Elements.create_class(classes)
            root.append(classes_element)

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
