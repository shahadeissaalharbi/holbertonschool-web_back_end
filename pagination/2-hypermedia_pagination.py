#!/usr/bin/env python3
"""
Module for hypermedia pagination of a dataset.
"""
import csv
import math
from typing import List, Tuple, Dict, Any


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Return a tuple of start and end indexes for pagination.

    Args:
        page (int): the current page number (1-indexed).
        page_size (int): the number of items per page.

    Returns:
        tuple: (start_index, end_index)
    """
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
        """
        Return the requested page of the dataset.

        Args:
            page (int): the page number to retrieve (1-indexed).
            page_size (int): the number of items per page.

        Returns:
            List[List]: the rows corresponding to the requested page,
            or an empty list if the range is out of bounds.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start_index, end_index = index_range(page, page_size)
        data = self.dataset()

        if start_index >= len(data):
            return []

        return data[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """
        Return a dictionary containing pagination metadata along with
        the requested page of the dataset.

        Args:
            page (int): the page number to retrieve (1-indexed).
            page_size (int): the number of items per page.

        Returns:
            dict: contains page_size, page, data, next_page,
            prev_page and total_pages.
        """
        data = self.get_page(page, page_size)
        total_items = len(self.dataset())
        total_pages = math.ceil(total_items / page_size)

        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }
