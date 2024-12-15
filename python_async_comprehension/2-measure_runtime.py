#!/usr/bin/env python3

"""
Module that write a measure_runtime coroutine that
will execute async_comprehension four times in parallel
using asyncio.gather.
"""
import time
import asyncio
from typing import List
async_comprehension = __import__('1-async_comprehension').async_comprehesion

async def measure_runtime() -> float:
    """
    measure_runtime should measure the total
    runtime and return it.
    """

    start_t = time.time()
    execute = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*execute)
    end_t = time.time()
    all_t = end_t - start_t
    return all_t
