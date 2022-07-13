#!/usr/bin/python3
"""
Contains class that extends list
"""


class MyList(list):
    """
    Custom list class
    """

    def print_sorted(self):
        """prints list in ascending order"""
        print(sorted(self))
