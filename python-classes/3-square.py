#!/usr/bin/python3
""" Define the sqaure class."""


class Sqaure:
    """ properties """
    
    def __init__(self, size=0) -> None:
        """ initialize """
        
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        
        self.__size = size
        
    def area(self) -> int:
        """ return the area of the object"""
        return self.__size ** 2