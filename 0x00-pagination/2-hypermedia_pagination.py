#!/usr/bin/env python3
"""Simple pagination"""

import csv
import math
from typing import List, Dict


def index_range(page, page_size):
    """Return a tuple of size two containing a start index and an end index"""
    if page <= 0 or page_size <= 0:
        return (0, 0)

    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return (start_index, end_index)


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
        """Get a page with the given page and page_size  """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start, end = index_range(page, page_size)
        return self.dataset()[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Get a dictionary with the following key-value pairs:"""
        start_idx, end_idx = index_range(page, page_size)
        dataset_len = len(self.dataset())

        return {
            'page_size': page_size,
            'page': page,
            'data': self.get_page(page, page_size),
            'next_page': page + 1 if end_idx < dataset_len else None,
            'prev_page': page - 1 if start_idx > 0 else None,
            'total_pages': math.ceil(dataset_len / page_size)
        }
