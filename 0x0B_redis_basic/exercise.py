#!/usr/bin/env python3
"""Cache module storing data in Redis under random keys."""
import uuid
from functools import wraps
from typing import Union, Callable, Optional

import redis


def count_calls(method: Callable) -> Callable:
    """Decorator counting how many times a Cache method is called."""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Increment the call count then call the wrapped method."""
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """Decorator storing the inputs and outputs of a Cache method."""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Record inputs and outputs around the wrapped method call."""
        self._redis.rpush("{}:inputs".format(method.__qualname__), str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush("{}:outputs".format(method.__qualname__), output)
        return output
    return wrapper


def replay(method: Callable) -> None:
    """Display the call history (inputs and outputs) of a Cache method."""
    cache = method.__self__
    name = method.__qualname__
    count = cache._redis.get(name)
    count = int(count) if count else 0
    print("{} was called {} times:".format(name, count))
    inputs = cache._redis.lrange("{}:inputs".format(name), 0, -1)
    outputs = cache._redis.lrange("{}:outputs".format(name), 0, -1)
    for inp, out in zip(inputs, outputs):
        print("{}(*{}) -> {}".format(
            name, inp.decode("utf-8"), out.decode("utf-8")))


class Cache:
    """Cache class wrapping a Redis client for simple storage."""

    def __init__(self) -> None:
        """Initialize the Redis client and flush the database."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store the data under a random key and return the key."""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """Retrieve a key's value, optionally converting it with fn."""
        data = self._redis.get(key)
        if data is None:
            return None
        if fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """Retrieve a value from Redis decoded as a UTF-8 string."""
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> int:
        """Retrieve a value from Redis converted to an integer."""
        return self.get(key, fn=int)
