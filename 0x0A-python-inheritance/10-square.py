#!/usr/bin/python3
"""Class inherent"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """class Square"""
    def __init__(self, size):
        """validate size"""
        self.__size = size
        self.integer_validator("size", size)

    def area(self):
        """ area of rectangle"""
        return self.__size * self.__size
