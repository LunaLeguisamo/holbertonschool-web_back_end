#!/usr/bin/env python3

"""
The index_range function calculates the start and end indices for
a page in a dataset, given a page number (page) and a page size (page_size).
This is commonly used to implement pagination in APIs or systems that handle
large datasets by breaking the results into smaller, manageable pages to
improve efficiency and user experience.

Parameters:
- page (int): The requested page number (must be a positive integer).
- page_size (int): The number of items per page (must be a positive integer).

Returns:
- Tuple[int, int]: A pair of indices (start_index, end_index) that represent
the range of items to be returned for the requested page.
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculates the start and end indices for a page of data, given
    a page number (page) and a page size (page_size).

    Parameters:
    - page (int): The page number to fetch.
    - page_size (int): The number of items per page.

    Returns:
    - Tuple[int, int]: A tuple containing the start and end index
    for the requested page.
    """

    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    tuple = (start_index, end_index)

    return tuple
