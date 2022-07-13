#!/usr/bin/python3
"""
Adds integer_validator to BaseGeometry
"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """area instance method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates a given value
        Raises:
            TypeError: if value is not an integer
            ValueError: if value is less than or equal to zero
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
