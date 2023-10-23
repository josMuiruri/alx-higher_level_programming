#!/usr/bin/python3
"""
This module is composed by a function that adds two numbers
"""


def add_integer(a, b=98):
    """ Function that adds two integer and/or float numbers
    Args:
        a: first number
        b: second number
    Returns:
        The addition of the two given numbers
    Raises:
        TypeError: If a or b aren't integer and/or float numbers
    """

    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")
    
    # Cast a and b to integers if they are floats
    a = int(a) if isinstance(a, float) else a
    b = int(b) if isinstance(b, float) else b
    
    # Return the addition of a and b as an integer
    return (a + b)
