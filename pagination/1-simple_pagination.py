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

from typing import Tuple, List
import csv


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


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Returns a specific page of the dataset.

        This method takes two arguments: `page` (the page number to fetch)
        and `page_size` (the number of items per page). It validates that both
        arguments are positive integers, calculates the range of items for the
        requested page, and returns the corresponding subset of the dataset.
        If the page or size is invalid or the indices go beyond
        the dataset size, an empty list is returned.

        Args:
            page (int): The page number (default is 1).
            page_size (int): The number of items per page (default is 10).

        Returns:
            List[List]: A sublist of the dataset containing the items for the
            requested page.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        range = index_range(page, page_size)

        list = self.dataset()
        all_items = len(list)

        if all_items < range[0]:
            return []
        else:
            return list[range[0]:range[1]]
