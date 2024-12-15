#!/usr/bin/env python3

import asyncio


# Import the async_generator function from 0-async_generator.py
async_generator = __import__('0-async_generator').async_generator


async def print_yielded_values():
    result = []
    async for i in async_generator():
        result.append(i)
    print(result)

# Run the coroutine
asyncio.run(print_yielded_values())
