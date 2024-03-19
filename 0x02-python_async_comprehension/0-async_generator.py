#!/usr/bin/env python3
"""Definition of async_generator coroutine
"""
import asyncio
import random


async def async_generator() -> float:
    """Coroutine that yields a random number between 0 and 10
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
