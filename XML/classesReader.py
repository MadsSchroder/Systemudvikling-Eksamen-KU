from logging import root
import os
from xml.etree import ElementTree
from Models.Classes import Classes

class ClassesReader:
    __file_name__ = 'classesData.xml'

    def __init__(self):
        full_file = os.path.abspath(os.path.join('data', self.__file_name__))
        print(str(full_file))
        dom = ElementTree.parse(full_file)

        root = dom.getroot()
        id = root.attrib['id']
        location = root.attrib['location']
        start = root.attrib['start']
        end = root.attrib['end']
        courseID = root.attrib['courseID']
        coursename = root.attrib['coursename']

        print("New lecture in", coursename)

        self.__Classes__ = Classes(id, location, start, end, courseID, coursename)

    def get_Classes(self) -> Classes:
        return self.__Classes__
