#!/usr/bin/env python3
""" This module contains the function sum_mixed_list """
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ Return the sum of mxd_lst """
    total: float = 0
    for item in mxd_lst:
        total += item
    return total
