#!/usr/bin/env python3
""" BasicCache module

This module defines a BasicCache class, a caching system without any limit
on the number of items it can store.
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache is a caching system that inherits from BaseCaching.

    It stores items in a dictionary without any limit on the number of
    items it can hold.
    """

    def put(self, key, item):
        """ Assign to the dictionary self.cache_data the item value for the
        key key.

        If key or item is None, this method does nothing.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """ Return the value in self.cache_data linked to key.

        If key is None or if the key doesn't exist in self.cache_data,
        return None.
        """
        return self.cache_data.get(key)
