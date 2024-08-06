#!/usr/bin/env python3
"""
This module contains a function to measure the runtime of wait_n.
"""
import asyncio
import time
from typing import List
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay) and returns
    total_time / n.
    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): The maximum delay in seconds.
    Returns:
        float: The average time per coroutine.
    """
    start_time = time.perf_counter()
    await wait_n(n, max_delay)
    end_time = time.perf_counter()
    total_time = end_time - start_time
    return total_time / n
