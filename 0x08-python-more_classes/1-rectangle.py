#!/usr/bin/python3
"""Class Rectangle"""


class Rectangle:
    """Set rectangle"""

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def width(self):
        """Property width"""
        return self.__width

    @width.setter
    def width(self, width):
        """Sets width"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

    @property
    def height(self):
        """Property height"""
        return self.__height

    @height.setter
    def height(self, height):
        """Sets height"""
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height
