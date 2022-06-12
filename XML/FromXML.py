from logging import root
import os
from xml.etree import ElementTree
from Models.Classes import Classes
#This code is inspired from the course cookbook

class ClassesReader:
    __file_name__ = '../XML/data/classes.xml'

    def __init__(self):
        #full_file = os.path.abspath(os.path.join('data', self.__file_name__))
        full_file = '../XML/data/classes.xml'

        print(str(full_file))
        dom = ElementTree.parse(full_file)

        root = dom.getroot()
        classid = root.attrib['classid']
        location = root.attrib['location']
        date = root.attrib['date']
        start = root.attrib['start']
        end = root.attrib['end']
        classcourseID = root.attrib['classcourseID']
        coursename = root.attrib['coursename']

        self.__Classes__ = Classes(int(classid), location, date, start, end, classcourseID, coursename)

    def get_Classes(self) -> Classes:
        return self.__Classes__
