#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    new = a_dictionary
    for i in new:
        if key in new is True:
            del new[key]
            return new
        else:
            return new
