#!/usr/bin/env python3
""" This module contains the sum_list function """
from typing import List


def sum_list(input_list: List[float]) -> float:
    """ Return the sum of input_list """
    total: float = 0
    for item in input_list:
        total += item

    return total
