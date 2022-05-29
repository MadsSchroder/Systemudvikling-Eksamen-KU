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
        courseID = root.attrib['courseID']
        year = root.attrib['year']
        university = root.attrib['university']
        uniID = root.attrib['uniID']
        program = root.attrib['program']
        programID = root.attrib['programID']






        print("New lecture in", coursename)

        self.__Classes__ = Classes(classid, location, date, start, end, classcourseID, coursename, courseID, year, university, uniID, program, programID)


    def get_Classes(self) -> Classes:
        return self.__Classes__
