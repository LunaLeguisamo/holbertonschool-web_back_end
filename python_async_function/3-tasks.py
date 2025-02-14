#!/usr/bin/env python3
"""
This file contains a function that return a asyncio
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Create an asyncio task
    """
    devolver = asyncio.create_task(wait_random(max_delay))
    return devolver
