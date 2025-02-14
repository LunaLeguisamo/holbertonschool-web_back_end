#!/usr/bin/env python3
"""
This file contains a function
"""
from typing import List
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Wait for n random times between 0 and max_delay
    """
    tasks = []
    for i in range(n):
        tasks.append(task_wait_random(max_delay))
    list = await asyncio.gather(*tasks)
    return sorted(list)
