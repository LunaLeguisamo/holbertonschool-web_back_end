#!/usr/bin/env python3

"""
Module that define a function that returns a multiplier
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Return a list of tuples that contain an
    element of the the lst and its length
    """
    return [(i, len(i)) for i in lst]
