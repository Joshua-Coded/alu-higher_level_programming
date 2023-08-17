#!/usr/bin/python3
"""Defines a matrix division function."""


def matrix_divided(matrix, div):
    """Divides all element of a matrix

    :param matrix: The matrix(list of list) whose element are to be \n
    divided by div
    :type matrix: list
    :param div: The value that divides each element in the matrix
    :type div: int
    :returns: A new matrix (list of list), derived form the division
    :rtype: list(list of lists)
    :raise: TypeError if div is not an int
    :raise: TypeError if matrix is not a list of lists
    :raise: TypeError if each row of the matrix is not of the same size
    """

    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all((isinstance(ele, int) or isinstance(ele, float))
                    for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return ([list(map(lambda x: round(x / div, 2), row)) for row in matrix])
