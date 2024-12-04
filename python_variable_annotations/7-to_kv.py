#!/usr/bin/env python3

"""
Module that define a function that returns a tuple
"""
from typing import Tuple, Union

def to_kv(k: str, v:Union[int, float]) -> Tuple[str, float]:
    """_summary_

    Args:
        k (intorfloat): _description_

    Returns:
        tuple: _description_
    """
    return (k, float(v ** 2))
