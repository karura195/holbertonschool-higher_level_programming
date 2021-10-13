#!/usr/bin/python3
"""function"""


def append_write(filename="", text=""):
    """appends a file"""
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
