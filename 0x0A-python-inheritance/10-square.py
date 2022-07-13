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
