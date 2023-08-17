#!/usr/bin/python3
"""Defines a name-printing function."""


def say_my_name(first_name, last_name=""):
    """Print the inputed name

    :param: first_name
    :type first_name: string
    :raise: TypeError if first_name not string
    :param: last_name
    :type last_name: string
    :raises: TypeError if last_name not string
    :returns: none
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
