#!/usr/bin/python3
"""Defines a matrix multiplication function using Numpy"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """Matrix multiplication using Numpy

    :param m_a: The first matrix
    :type m_a: list of list of ints/floats
    :param m_b: The second matrix
    :type m_b: list of list of int/floats
    :returns: The results of the matrix multiplication
    :rtype: list of list of int/floats
    """
    
    return(numpy.matmul(m_a, m_b))
