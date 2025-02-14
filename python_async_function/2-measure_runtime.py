#!/usr/bin/env python3
"""
This file contains a function
"""
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Function that return the total execution time for wait_n(n, max_delay),
    and returns total_time / n
    """
    inicial = time.time()
    asyncio.run(wait_n(n, max_delay))
    final = time.time()
    total = (final - inicial) / n
    return total
