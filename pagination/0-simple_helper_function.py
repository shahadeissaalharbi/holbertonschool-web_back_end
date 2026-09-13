#!/usr/bin/env python3
"""
Module that provides a helper function for pagination.
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Return a tuple of start and end indexes for pagination.

    Given page number and page size, this function calculates
    the start and end index in a dataset that correspond to
    the range of items to display on that page.

    Args:
        page (int): the current page number (1-indexed).
        page_size (int): the number of items per page.

    Returns:
        tuple: (start_index, end_index)
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
