#!/usr/bin/env python3
"""Module documentation"""
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ main method"""
    tasks_list: list = []
    for _ in range(n):
        tasks_list.append(asyncio.create_task(wait_random(max_delay)))
    result = await asyncio.gather(*tasks_list)
    return sorted(result)
