#!/usr/bin/env python3
'''working with async comprehension'''

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    '''coroutin loop runs 10 times and yields a random number'''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
