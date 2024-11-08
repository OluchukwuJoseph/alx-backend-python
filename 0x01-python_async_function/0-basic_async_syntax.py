#!/usr/bin/env python3
""" This module contains the wait_random function """
import asyncio
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    """
    Waits for a random delay between 0 and max_delay seconds and
    eventually returns it.
    """
    delay = uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
