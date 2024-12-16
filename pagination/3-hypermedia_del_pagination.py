#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        This method returns a paginated page of the dataset, resilient to
        deletions.
        It takes the starting index (index) and the page size (page_size),
        and return a dictionary with:
        - 'index': the starting index of the page.
        - 'next_index': the index of the next item to query, or None if
        the page is the last one.
        - 'page_size': the number of items in the current page.
        - 'data': the list of items on the current page.

        Parameters:
        - index (int): The index to start the pagination from. Default is 0.
        - page_size (int): The number of items to show on each page.
        Default is 10.

        Returns:
        - A dictionary containing pagination information.
        """

        new_dataset = []
        data = self.indexed_dataset()
        current_index = index
        assert index >= 0
        assert index < len(data)

        while len(new_dataset) < page_size:
            if current_index in data:
                new_dataset.append(data[current_index])
            current_index += 1

        next_index = current_index if current_index < len(data) else None

        return {
            'index': index,
            'next_index': next_index,
            'page_size': page_size,
            'data': new_dataset
        }
