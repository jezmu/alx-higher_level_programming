#!/usr/bin/python3
"""Defines Rectangle class"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class definition"""

    def __init__(self, width, height):
        """Instantiates Rectangle"""

        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """Calculates rectangle area"""
        return self.__width * self.__height

    def __str__(self):
        """Returns Rectangle's string representation"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
