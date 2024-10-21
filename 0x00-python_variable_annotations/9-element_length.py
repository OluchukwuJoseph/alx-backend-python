#!/usr/bin/env python3
""" This module contains the element_length function """
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Return a list of tuple """
    return [(i, len(i)) for i in lst]
