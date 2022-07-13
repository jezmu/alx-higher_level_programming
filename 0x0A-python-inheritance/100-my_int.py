#!/usr/bin/python3
"""Contains custom integer class"""


class MyInt(int):
    """Custom integer class"""

    def __init__(self, num):
        """Instantiates MyInt"""
        self.num = num

    def __eq__(self, obj):
        """Checks for equality"""
        return not super().__eq__(obj)

    def __ne__(self, obj):
        """Checks for inequality"""
        return super().__eq__(obj)
