#!/usr/bin/env python3

import math
"""
Module that define a function that returns a tuple
"""


def to_kv(k: str, v: int | float) -> tuple:
    """_summary_

    Args:
        k (intorfloat): _description_

    Returns:
        tuple: _description_
    """
    return (k, math.square(v))
