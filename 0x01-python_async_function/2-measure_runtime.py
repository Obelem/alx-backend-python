#!/usr/bin/env python3
'''Measure the runtime'''
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """function to measure the run

    Args:
        n (int): number of times to spawn wait_random
        max_delay (int): max delay

    Returns:
        float: the run time
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.time() - start_time

    return total_time / n
