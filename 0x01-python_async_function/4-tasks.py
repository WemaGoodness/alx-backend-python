#!/usr/bin/env python3
"""
This module provides an async routine to execute multiple tasks concurrently.
"""
from typing import List
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn task_wait_random n times with the specified max_delay and return
    the list of delays.
    Args:
        n (int): Number of tasks to spawn.
        max_delay (int): Maximum delay in seconds.
    Returns:
        List[float]: List of delays in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
