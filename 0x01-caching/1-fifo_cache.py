#!/usr/bin/env python3
""" FIFO Caching """

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFO Caching """

    def __init__(self):
        """ Constructor """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """ Add an item in the cache """

        if key is None or item is None:
            return

        if key in self.queue:
            self.cache_data[key] = item

            self.queue.remove(key)
            self.queue.append(key)
            return

        if len(self.queue) >= self.MAX_ITEMS:
            oldest_key = self.queue.pop(0)
            del self.cache_data[oldest_key]

            print(f"DISCARD: {oldest_key}")

        self.queue.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key """
        if key is None or not self.cache_data.get(key):
            return

        return self.cache_data.get(key)
