#!/usr/bin/env python3
"""Module documentation"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ main method"""
    tasks_list: list = []
    for _ in range(n):
        tasks_list.append(task_wait_random(max_delay))
    result = await asyncio.gather(*tasks_list)
    return sorted(result)
