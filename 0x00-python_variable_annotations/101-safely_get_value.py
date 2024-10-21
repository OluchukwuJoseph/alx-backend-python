#!/usr/bin/env python3
""" This module contains the safely_get_value function """
from typing import TypeVar, Mapping, Any, Union


T = TypeVar('T')

def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    """
    Returns the first element of a given sequence,
    or None if the sequence is empty.
    
    Parameters:
    -----------
    lst : Sequence[Any]
        A sequence (e.g., list, tuple, string) containing elements of any type.
    key: Any
    default: Union[T, None]
    
    Returns:
    --------
    Union[Any, None]
        The first element of the sequence if it exists, otherwise None.
    """
    if key in dct:
        return dct[key]
    else:
        return default
