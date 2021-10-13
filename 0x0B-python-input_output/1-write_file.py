#!/usr/bin/python3
"""function"""


def write_file(filename="", text=""):
    """writes a file"""
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
