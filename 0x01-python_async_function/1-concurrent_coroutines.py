#!/usr/bin/env python3
""" This module contains the wait_n function """
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ Spawn wait_random n times with the specified max_delay """
    delays: List[float] = []
    tasks: List = [wait_random(max_delay) for _ in range(n)]
    for fut in asyncio.as_completed(tasks):
        result: float = await fut
        delays.append(result)
    return delays
