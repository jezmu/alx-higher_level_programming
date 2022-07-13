#!/usr/bin/python3
"""
Contains function for checking whether an object is a subclass
of a class
"""


def inherits_from(obj, a_class):
    """
    Checks whether an object is a subclass
    of a class
    Returns:
        True if obj is a subclass of a_class
        False if obj is not a subclass of a_class
    """
    return issubclass(obj, a_class)
