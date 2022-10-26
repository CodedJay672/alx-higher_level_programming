#!/usr/bin/python3
"""student module"""


class Student(object):
    """sudent class"""

    def __init__(self, first_name, last_name, age):
        """constructor"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves the dict representation of student"""
        return self.__dict__
