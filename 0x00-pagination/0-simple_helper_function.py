#!/usr/bin/env python3
"""Pagination helper function.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end indices for the pagination range.

    Args:
        page (int): The page number (1-indexed).
        page_size (int): The size of each page.

    Returns:
        tuple: A tuple containing the start index and the end index (exclusive).
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_inedx)
