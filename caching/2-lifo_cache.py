#!/usr/bin/env python3
""" LIFOCache module

This module defines a LIFOCache class, a caching system that follows the
LIFO (Last In, First Out) eviction policy when the cache is full.
"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache is a caching system that inherits from BaseCaching.

    When the cache exceeds BaseCaching.MAX_ITEMS items, the last item that
    was put in the cache is discarded (Last In, First Out).
    """

    def __init__(self):
        """ Initialize the cache by calling the parent constructor. """
        super().__init__()

    def put(self, key, item):
        """ Assign to the dictionary self.cache_data the item value for the
        key key.

        If key or item is None, this method does nothing. If adding a new
        item makes the cache exceed BaseCaching.MAX_ITEMS, the most recently
        inserted item is discarded and its key is printed after 'DISCARD: '.
        """
        if key is None or item is None:
            return
        if key in self.cache_data:
            del self.cache_data[key]
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            last_key = next(reversed(self.cache_data))
            del self.cache_data[last_key]
            print("DISCARD: {}".format(last_key))
        self.cache_data[key] = item

    def get(self, key):
        """ Return the value in self.cache_data linked to key.

        If key is None or if the key doesn't exist in self.cache_data,
        return None.
        """
        return self.cache_data.get(key)
