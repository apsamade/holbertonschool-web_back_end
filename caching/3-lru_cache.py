#!/usr/bin/env python3
""" LRUCache module

This module defines a LRUCache class, a caching system that follows the
LRU (Least Recently Used) eviction policy when the cache is full.
"""
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache is a caching system that inherits from BaseCaching.

    When the cache exceeds BaseCaching.MAX_ITEMS items, the least recently
    used item (accessed via get or put) is discarded.
    """

    def __init__(self):
        """ Initialize the cache by calling the parent constructor. """
        super().__init__()

    def put(self, key, item):
        """ Assign to the dictionary self.cache_data the item value for the
        key key.

        If key or item is None, this method does nothing. Updating an
        existing key marks it as recently used. If adding a new item makes
        the cache exceed BaseCaching.MAX_ITEMS, the least recently used item
        is discarded and its key is printed after 'DISCARD: '.
        """
        if key is None or item is None:
            return
        if key in self.cache_data:
            del self.cache_data[key]
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            lru_key = next(iter(self.cache_data))
            del self.cache_data[lru_key]
            print("DISCARD: {}".format(lru_key))
        self.cache_data[key] = item

    def get(self, key):
        """ Return the value in self.cache_data linked to key.

        Accessing a key marks it as the most recently used. If key is None
        or if the key doesn't exist in self.cache_data, return None.
        """
        if key is None or key not in self.cache_data:
            return None
        value = self.cache_data.pop(key)
        self.cache_data[key] = value
        return value
