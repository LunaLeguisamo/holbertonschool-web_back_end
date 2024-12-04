#!/usr/bin/env python3
from typing import Union, List
"""
Module that define a function that return a sum
of integers and floats in a list
"""

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """_summary_

    Args:
        mxd_lst (list[int, float]): _description_

    Returns:
        float: _description_
    """
    return sum(mxd_lst)
