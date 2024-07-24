#!/usr/bin/env python3
""" BasicCache module"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache defines:"""

    def __init__(self):
        """ Constructor """
        super().__init__()

    def put(self, key, item):
        """ Put method """
        if item is None or key is None:
            return

        self.cache_data[key] = item

    def get(self, key):
        """ Get method """
        if key is None or not self.cache_data.get(key):
            return None

        return self.cache_data.get(key)
