#!/usr/bin/env python3
"""First-In First-Out caching system.
"""
from collections import OrderedDict

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache inherits from BaseCaching and
    is a caching system using FIFO algorithm.
    """
    def __init__(self):
        """Initializes FIFOCache.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Adds an item in the cache
	using FIFO algorithm.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
	    # If cache is full, discard the first item (FIFO)
            first_key, _ = self.cache_data.popitem(False)
            print("DISCARD:", first_key)

    def get(self, key):
        """Get an item by key.
        """
        return self.cache_data.get(key, None)
