#!/usr/bin/env python3
""" FIFOCache module

This module defines a FIFOCache class, a caching system that follows the
FIFO (First In, First Out) eviction policy when the cache is full.
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache is a caching system that inherits from BaseCaching.

    When the cache exceeds BaseCaching.MAX_ITEMS items, the first item that
    was put in the cache is discarded (First In, First Out).
    """

    def __init__(self):
        """ Initialize the cache by calling the parent constructor. """
        super().__init__()

    def put(self, key, item):
        """ Assign to the dictionary self.cache_data the item value for the
        key key.

        If key or item is None, this method does nothing. If adding the item
        makes the cache exceed BaseCaching.MAX_ITEMS, the oldest inserted
        item is discarded and its key is printed after 'DISCARD: '.
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key = next(iter(self.cache_data))
            del self.cache_data[first_key]
            print("DISCARD: {}".format(first_key))

    def get(self, key):
        """ Return the value in self.cache_data linked to key.

        If key is None or if the key doesn't exist in self.cache_data,
        return None.
        """
        return self.cache_data.get(key)
