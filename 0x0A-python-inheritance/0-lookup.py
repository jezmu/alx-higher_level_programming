#!/usr/bin/python3
"""
This module deals with lookup of object attributes
"""


def lookup(obj):
    """
    Looks up an object's attributes
    >>> lookup('') # doctest: +NORMALIZE_WHITESPACE
    ['__add__', '__class__', '__contains__',
    '__delattr__', '__dir__', '__doc__',
    '__eq__', '__format__', '__ge__',
    '__getattribute__', '__getitem__',
    '__getnewargs__', '__gt__', '__hash__',
    '__init__', '__init_subclass__', '__iter__',
    '__le__', '__len__', '__lt__', '__mod__',
    '__mul__', '__ne__', '__new__', '__reduce__',
    '__reduce_ex__', '__repr__', '__rmod__',
    '__rmul__', '__setattr__', '__sizeof__',
    '__str__', '__subclasshook__', 'capitalize',
    'casefold', 'center', 'count', 'encode',
    'endswith', 'expandtabs', 'find', 'format',
    'format_map', 'index', 'isalnum', 'isalpha',
    'isascii', 'isdecimal', 'isdigit', 'isidentifier',
    'islower', 'isnumeric', 'isprintable', 'isspace',
    'istitle', 'isupper', 'join', 'ljust', 'lower',
    'lstrip', 'maketrans', 'partition', 'replace',
    'rfind', 'rindex', 'rjust', 'rpartition',
    'rsplit', 'rstrip', 'split', 'splitlines',
    'startswith', 'strip', 'swapcase', 'title',
    'translate', 'upper', 'zfill']
    >>> lookup(None) # doctest: +NORMALIZE_WHITESPACE
    ['__bool__', '__class__', '__delattr__', '__dir__', '__doc__',
    '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__',
    '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__',
    '__ne__', '__new__', '__reduce__', '__reduce_ex__',
    '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
    Args:
        obj: the object to look up
    Returns:
        a list containing the object's attributes
    """
    return dir(obj)
