import os
from xml.etree.ElementTree import ElementTree, tostring
import xml.etree.cElementTree as ET
from xml.dom import minidom
from Models.Classes import Classes

class ClassesWriter:
    def __init__(self, c: Classes) -> None:

        self.__root__ = ET.Element("Classes")
        self.__root__.set("ClassID", c.get_id())
        self.__root__.set("location", c.get_location())
        self.__root__.set("start_time", c.get_start())
        self.__root__.set("end", c.get_end())
        self.__root__.set("courseID", c.get_courseID())
        self.__root__.set("coursename", c.get_coursename())

    def save(self) -> None:
        tree = ET.ElementTree(self.__root__)
        tree.write("data/classesData.xml", encoding="utf-8")


def prettify(elem):
    """retunerer en pretty-printed XML string"""
    elem.getroot()
    rough_string = tostring(elem, 'utf-8')
    reparesed = minidom.parseString(rough_string)
    return reparesed.topprettyxml(indent="  ")
