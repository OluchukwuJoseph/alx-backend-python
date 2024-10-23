#!/usr/bin/env python3
""" This module contains the wait_n function """
import asyncio
from random import uniform


wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> list:
    delays = []
    tasks = [wait_random(max_delay) for _ in range(n)]
    print(tasks)
    for fut in asyncio.as_completed(tasks):
        result = await fut
        delays.append(result)
    return delays
