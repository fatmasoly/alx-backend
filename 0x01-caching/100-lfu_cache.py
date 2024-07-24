#!/usr/bin/env python3
""" lfu Caching """

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ lfu Caching """
    def __init__(self):
        """ Constructor """
        super().__init__()
        self.lfu_list = []

    def put(self, key, item):
        """ Add an item in the cache """
        if key is None or item is None:
            return

        if key in self.lfu_list:
            self.cache_data[key] = item

            self.lfu_list.remove(key)
            self.lfu_list.append(key)

            return

        if len(self.lfu_list) >= self.MAX_ITEMS:
            least_key = self.lfu_list.pop(0)
            del self.cache_data[least_key]

            print(f"DISCARD: {least_key}")

        self.cache_data[key] = item
        self.lfu_list.append(key)

    def get(self, key):
        """ Get an item by key """
        value = self.cache_data.get(key)

        if value:
            self.lfu_list.remove(key)
            self.lfu_list.append(key)

        return value
