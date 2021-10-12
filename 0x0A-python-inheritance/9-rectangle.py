#!/usr/bin/python3
"""Class inherent"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """class Rectangle"""
    def __init__(self, width, height):
        """rectangle checker"""
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """area of rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """string to print"""
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
