#!/usr/bin/env python3
'''0-async_generator.py'''
import random
from asyncio import sleep
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator:
    """intro to async_generator

    Returns:
        AsyncGenerator: _description_

    Yields:
        Iterator[AsyncGenerator]: _description_
    """
    for i in range(10):
        await sleep(1)
        yield random.uniform(0, 10)
