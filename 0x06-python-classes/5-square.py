#!/usr/bin/python3
"""Class Square"""


class Square:

    """Define Constructor"""
    def __init__(self, size=0):
        try:
            if type(size) is not int:
                raise TypeError
            if size < 0:
                raise ValueError
            self.__size = size
        except ValueError:
            print("size must be >= 0", end="")
            raise
        except TypeError:
            print("size must be an integer", end="")
            raise

    """Square area"""
    def area(self):
        return (self.__size * self.__size)

    """Getter Size"""
    @property
    def size(self):
        return self.__size

    """Setter Size"""
    @size.setter
    def size(self, value):
        try:
            if type(value) is not int:
                raise TypeError
            self.__size = value
        except TypeError:
            print("size must be an integer", end="")
            raise

    """"Print square"""
    def my_print(self):
        if self.size == 0:
            print()
        else:
            for i in range(self.size):
                print('#' * self.size)
