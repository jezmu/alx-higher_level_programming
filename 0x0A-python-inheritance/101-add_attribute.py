#!/usr/bin/python3
"""Contains function that adds attribute to object if possible"""


def add_attribute(obj, attribute, value):
    """Adds attribute to object if possible
    Params:
        obj: object to add attribute to
        attribute: attribute to add to obj
        value: value of attribute to add
    """

    if "__dict__" in dir(obj):
        setattr(obj, attribute, value)
    else:
        raise TypeError("can't add new attribute")
