#!/usr/bin/env python3

"""
Module that define a function that returns a multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """_summary_

    Args:
        multiplier (float): _description_

    Returns:
        float: _description_
    """
    def a_multiplier(a: float) -> float:
        return multiplier * a

    return a_multiplier
