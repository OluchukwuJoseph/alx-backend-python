#!/usr/bin/env python3
""" This module contains the make_multiplier function """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Returns a function multiplies a float by multiplier """
    def my_multiplier(n: float) -> float:
        """ Multiplies n by multiplier """
        return multiplier * n
    return my_multiplier
