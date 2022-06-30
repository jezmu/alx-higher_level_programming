#!/usr/bin/python3

"""
Contains function that adds two numbers together
"""


def add_integer(a, b=98):
    """
    Adds two numbers together
    Args:
        a: first number
        b: second number
    Returns: an integer, the sum of a and b
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    return int(a + b)
