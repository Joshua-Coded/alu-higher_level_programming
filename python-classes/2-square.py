#!/usr/bin/python3
""" Define a A sqaure class """


class Square:
    """ """
    
    def __init__(self, size=0) -> None:
        """ check for validations """
        
        if (type(size) is not int):
            raise TypeError("Size must be an integer")
        elif size < 0:
            raise ValueError("Size must be  >= 0")
        
        self.__size = size
