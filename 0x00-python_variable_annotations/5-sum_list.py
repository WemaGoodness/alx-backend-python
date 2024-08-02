#!/usr/bin/env python3
"""
Module for summing a list of float numbers.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Sum a list of float numbers and return the result as a float.
    :param input_list: A list of float numbers.
    :return: The sum of the float numbers as a float.
    """
    return sum(input_list)
