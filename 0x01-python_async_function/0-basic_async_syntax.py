#!/usr/bin/env python3
"""Module documentation"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """main method"""
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
