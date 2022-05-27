import os
from xml.etree.ElementTree import ElementTree, tostring
import xml.etree.cElementTree as ET
from xml.dom import minidom
from Models.Classes import Classes


class ClassesWriter:
    def __init__(self, l: Classes) -> None:

        self.__root__ = ET.Element("lecture_class")
        self.__root__.set("ClassID", l.get_id())
        self.__root__.set("location", l.get_location())
        self.__root__.set("start_time", l.get_start())
        self.__root__.set("end", l.get_end())
        self.__root__.set("courseID", l.get_courseID())
        self.__root__.set("__coursename", l.get_coursename())

    def save(self) -> None:
        tree = ET.ElementTree(self.__root__)
        tree.write("../XLM/lecturedata.xml")


def prettify(elem):
    """retunerer en pretty-printed XML string"""
    elem.getroot()
    rough_string = tostring(elem, 'utf-8')
    reparesed = minidom.parseString(rough_string)
    return reparesed.topprettyxml(indent="  ")
