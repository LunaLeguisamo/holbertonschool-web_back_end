#!/usr/bin/env python3
"""
This file contains a function asynchronous
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Function asynchronous
    """
    num = random.uniform(0, max_delay)
    await asyncio.sleep(num)
    return num
