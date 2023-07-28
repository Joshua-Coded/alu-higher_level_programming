#!/usr/bin/python3
""" task 3 """


class Square:
    """ task 3 """

    def __init__(self, size="0") -> None:
        """check for order by ensuring that int is entered """

        if(type(size) is not int):
            raise TypeError("Size must be an integer")
        elif size < 0:
            raise ValueError("Size must be >= 0")

        self.__size = size
            
