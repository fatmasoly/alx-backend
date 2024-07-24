#!/usr/bin/env python3
""" LRU Caching """

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ LRU Caching """
    def __init__(self):
        """ Constructor """
        super().__init__()
        self.lru_list = []

    def put(self, key, item):
        """ Add an item in the cache """
        if key is None or item is None:
            return

        if key in self.lru_list:
            self.cache_data[key] = item

            self.lru_list.remove(key)
            self.lru_list.append(key)

            return

        if len(self.lru_list) >= self.MAX_ITEMS:
            least_key = self.lru_list.pop(0)
            del self.cache_data[least_key]

            print(f"DISCARD: {least_key}")

        self.cache_data[key] = item
        self.lru_list.append(key)

    def get(self, key):
        """ Get an item by key """
        if key is None or key is not self.cache_data.get(key):
            return

        return self.cache_data.get(key)
