#!/usr/bin/env python3
"""intro to mixed type annotations in lists"""
from typing import List, Union


def sum_mixed_list(mixd_list: List[int, float]) -> float:
    """takes a list mxd_lst of integers and floats
    and returns their sum as a float.

    Keyword arguments:
    List -- list with complex types of int and float
    Return: sum of list elements as float
    """
    return sum(mixd_list)
