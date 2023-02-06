#!/usr/bin/env python3
'''more async'''
from asyncio import create_task, Task
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: float = 10) -> Task:
    """concurrency without async

    Args:
        max_delay (float, optional): _description_. Defaults to 10.

    Returns:
        Task: _description_
    """
    return create_task(wait_random(max_delay))
