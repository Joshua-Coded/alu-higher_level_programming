#!/usr/bin/python3
""" Square class to represent a sqaure"""


class Square:
    """ Define a square and its basic properties
    >>> sqaure_1 = Square()
    >>> sqaure_2 = Sqaure(87)
    """

    def __init__(self, size: int) -> None:
        """ __init__ the size with a params of int """
        self.__size = size
