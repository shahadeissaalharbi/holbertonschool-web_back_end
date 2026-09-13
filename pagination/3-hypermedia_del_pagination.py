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

    def get_hyper_index(self, index: int = None,
                         page_size: int = 10) -> Dict:
        """
        Return a dictionary containing pagination data that is
        resilient to deletions in the dataset.

        Args:
            index (int): the starting index of the current page.
            page_size (int): the number of items to return.

        Returns:
            dict: contains index, next_index, page_size and data.
        """
        data_dict = self.indexed_dataset()
        assert index is not None and 0 <= index < len(data_dict)

        data = []
        current_index = index
        keys = sorted(data_dict.keys())
        count = 0

        for key in keys:
            if key < index:
                continue
            if count >= page_size:
                break
            data.append(data_dict[key])
            current_index = key
            count += 1

        next_index = current_index + 1

        return {
            'index': index,
            'data': data,
            'page_size': len(data),
            'next_index': next_index
        }
