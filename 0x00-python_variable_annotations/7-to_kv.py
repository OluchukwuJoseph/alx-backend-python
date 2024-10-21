#!/usr/bin/env python3
""" This module contains the to_kv function """
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ Returns a tuple contains k and a square of v """
    new_tuple: Tuple[str, float] = (k, v * v)
    return new_tuple
