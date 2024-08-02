#!/usr/bin/env python3
from typing import Sequence, List


def zoom_array(lst: Sequence[int], factor: int = 2) -> List[int]:
    """
    Returns a list where each element from the input sequence is repeated `factor` times.
    Parameters:
    lst (Sequence[int]): The input sequence of integers to be zoomed.
    factor (int): The number of times each element should be repeated.
    Returns:
    List[int]: A list with each element from the input sequence repeated `factor` times.
    """
    zoomed_in: List[int] = [item for item in lst for _ in range(factor)]
    return zoomed_in


array = [12, 72, 91]
zoom_2x = zoom_array(array)
zoom_3x = zoom_array(array, 3)
