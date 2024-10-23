#!/usr/bin/env python3
""" This module contains the wait_n function """
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> list:
    """ Spawn wait_random n times with the specified max_delay """
    delays = []
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    for fut in asyncio.as_completed(tasks):
        result = await fut
        delays.append(result)
    return delays
