#!/usr/bin/env python3
'''more async'''
import random
from asyncio import create_task, Task
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: float = 10) -> Task:
    task = create_task(wait_random(max_delay))
    return task
