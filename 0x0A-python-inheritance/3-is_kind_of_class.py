#!/usr/bin/python3
"""
Contains function that checks whether object is an instance of
a class or is a member of a class that extends a given class
"""


def is_kind_of_class(obj, a_class):
    """
    Checks whether object is an instance of
    a class or is a member of a class that extends a given class
    """
    return isinstance(obj, a_class)
