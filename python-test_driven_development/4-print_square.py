#!/usr/bin/python3
"""Defines a function that prints a square with the # character"""


def print_square(size):
    """Prints a square with the # character.
    :param: size
    :type size: int
    :raises: TypeError if size is not an integer
    :raises: ValueError if size is less than zero
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for k in range(size):
        [print("#", end="") for k in range(size)]
        print("")
