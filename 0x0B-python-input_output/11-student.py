#!/usr/bin/python3
"""class"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is not None:
            dic = {}
            for i in attrs:
                if i in self.__dict__:
                    dic[i] = self.__dict__[i]
            return dic
        return self.__dict_

    def reload_from_json(self, json):
        for a in json:
            self.__dict__[a] = json[a]
