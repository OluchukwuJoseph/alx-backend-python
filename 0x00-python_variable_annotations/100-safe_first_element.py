#!/usr/bin/env python3
""" This module contains the safe_first_element function """
from typing import Any, Union, Sequence


# The types of the elements of the input are not know
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ Return the first element of an iterable """
    if lst:
        return lst[0]
    else:
        return None
