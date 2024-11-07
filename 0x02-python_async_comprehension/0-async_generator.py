#!/usr/bin/env python3
""" This script contains the async_generator coroutine """
from typing import Generator, AsyncGenerator
import asyncio
import random


async def async_generator():
    """ Yield a random number between 0 and 10 """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
