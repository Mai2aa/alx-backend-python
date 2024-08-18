#!/usr/bin/env python3
''' Basic async syntax'''
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    '''waits for a random integer'''
    r = random.uniform(0, max_delay)
    await asyncio.sleep(r)
    return r
