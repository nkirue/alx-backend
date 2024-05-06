#!/usr/bin/env python3
"""Return start and end indexes for pagination
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Retrieves the index range from a given page and page size.
    """
    startindex = (page - 1) * page_size
    endindex = startindex + page_size
    return (startindex, endindex)
