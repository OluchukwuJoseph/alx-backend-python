#!/usr/bin/env python3
""" This module contains the measure_runtime coroutine """
import time
import asyncio


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measure the total runtime of 4 async_comprehension
    executed parallel using asyncio.gather.
    """
    start: float = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end: float = time.perf_counter() - start
    return end
