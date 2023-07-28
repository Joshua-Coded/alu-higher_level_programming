#!/usr/bin/python3
""" Sqaure class to represent a sqaure """


class Square:
    """ 
    Define a square and its basic properties
    """

    def __init__(self, size=0) -> None:
        """check for order by
        ensuring that int is entered
        """

        if (type(size) is not int):
            raise TypeError("Size must be an integer")
        elif size < 0:
            raise ValueError("Size must be >= 0")

        self.__size = size
            
