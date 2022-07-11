#!/usr/bin/python3
"""
Contains class that restricts creation of instance attributes
"""


class LockedClass:
    """
    Restricts dynamic creation of instance attributes
    Only first_name is allowed
    >>> x = LockedClass()
    >>> x.first_name = 'foo'
    >>> x.last_name = 'bar'
    Traceback (most recent call last):
    ...
    AttributeError: 'LockedClass' object has no attribute 'last_name'
    """
    
    __slots__ = "first_name"
