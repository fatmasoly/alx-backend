#!/usr/bin/env python3
""" MRU Caching """

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRU Caching """
    def __init__(self):
        """Constructor"""
        super().__init__()
        self.items = None

    def put(self, key, item):
        """Add an item in the cache"""
        if key is None or item is None:
            return None

        if (len(self.cache_data.keys()) >= self.MAX_ITEMS and
                key not in self.cache_data.keys()):
            del self.cache_data[self.items]
            print(f"DISCARD: {self.items}")

        self.cache_data[key] = item
        self.items = key

    def get(self, key):
        """Retrieve an item from the cache"""
        value = self.cache_data.get(key)

        if value:
            self.items = key

        return value
