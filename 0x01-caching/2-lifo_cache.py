#!/usr/bin/env python3
""" LIFO Caching """

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFO Caching """
    def __init__(self):
        """ Constructor """
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """ Add an item in the cache """
        if key is None or item is None:
            return

        if key in self.cache_data.keys():
            self.cache_data[key] = item

            self.stack.remove(key)
            self.stack.append(key)
            return

        if len(self.stack) >= self.MAX_ITEMS:
            latest_key = self.stack.pop()
            del self.cache_data[latest_key]

            print(f"DISCARD: {latest_key}")

        self.stack.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key """
        return self.cache_data.get(key)
