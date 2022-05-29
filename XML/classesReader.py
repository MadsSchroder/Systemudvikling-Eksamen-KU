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
        classid = root.attrib['ClassID']
        location = root.attrib['location']
        date = root.attrib['date']
        start = root.attrib['start_time']
        end = root.attrib['end_time']
        classcourseID = root.attrib['classcourseID']
        coursename = root.attrib['coursename']

        print("New lecture in", coursename)

        self.__Classes__ = Classes(classid, location, date, start, end, classcourseID, coursename)


    def get_Classes(self) -> Classes:
        return self.__Classes__
