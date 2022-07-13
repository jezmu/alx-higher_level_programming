#!/usr/bin/python3
"""Contains Square class"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Square class definition"""

    def __init__(self, size):
        """Instantiates a square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Returns Square's string representation"""
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
