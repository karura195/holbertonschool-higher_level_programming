#!/usr/bin/python3
"""function"""


def read_file(filename=""):
    """reads a file"""
    with open(filename, encoding='utf-8') as file:
        for line in file:
            print(line, end="")
