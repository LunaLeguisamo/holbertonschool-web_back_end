#!/usr/bin/env python3
"""
This file import a function of other file and other elements
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    return the list of all the delays (float values).
    """
    tasks = []
    for i in range(n):
        tasks.append(wait_random(max_delay))
    list = await asyncio.gather(*tasks)
    return sorted(list)
