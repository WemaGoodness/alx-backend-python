#!/usr/bin/env python3
"""
Module for converting a key-value pair to a tuple.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Convert a string and an int/float to a tuple where the second element is the square of the int/float.
    :param k: The string key.
    :param v: The int or float value to be squared.
    :return: A tuple with the string and the squared value as a float.
    """
    return (k, float(v ** 2))
