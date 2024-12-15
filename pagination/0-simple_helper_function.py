#!/usr/bin/env python3

"""
Module that define a function that return a
tuple of size two containing a start index and
an end index corresponding to the range of indexes
to return in a list for those particular pagination
parameters.
"""

from typing import Tuple



def index_range(page: int, page_size:int) -> Tuple[int, int]:
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    tuple = (start_index, end_index)
    
    return tuple