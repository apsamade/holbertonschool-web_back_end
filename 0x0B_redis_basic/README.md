# 0x0B. Redis basic

A learning project on using Redis for basic operations and as a simple
cache from Python with the `redis-py` client.

## Learning objectives

- Use Redis for basic operations (get/set, incr, lists).
- Use Redis as a simple cache.

## File

- `exercise.py` — the `Cache` class plus decorators and helpers:
  - `Cache.store` — store data under a random UUID key.
  - `Cache.get` / `get_str` / `get_int` — retrieve and convert values.
  - `count_calls` — decorator counting method calls with `INCR`.
  - `call_history` — decorator recording inputs and outputs in lists.
  - `replay` — display the call history of a method.

## Requirements

Requires a running Redis server (`service redis-server start`) and the
`redis` Python package (`pip3 install redis`).
