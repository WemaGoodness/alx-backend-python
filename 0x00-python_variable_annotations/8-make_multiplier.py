#!/usr/bin/env python3
"""
Module for creating a multiplier function.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create a multiplier function.

    :param multiplier: The multiplier value.
    :return: A function that multiplies its input by the multiplier.
    """
    def multiplier_function(value: float) -> float:
        return value * multiplier
    return multiplier_function
