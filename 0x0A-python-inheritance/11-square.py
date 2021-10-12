#!/usr/bin/python3
"""Class inherent"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """class Square"""
    def __init__(self, size):
        """size validator"""
        self.__size = size
        self.integer_validator("size", size)

    def area(self):
        """ area of rectangle"""
        return self.__size * self.__size

    def __str__(self):
        """Prints str"""
        return ("[Square] {}/{}".format(self.__size, self.__size))
