# Caching

This project is an introduction to **caching systems** and the most common
**cache replacement policies**. Each caching class stores its data in a
dictionary and inherits from the provided `BaseCaching` parent class.

## Background Context

A caching system is a component that stores data so that future requests for
that data can be served faster. Because a cache has a **limited size**, it must
decide which item to discard when it becomes full. The rule used to make that
decision is called a **cache replacement (or eviction) policy**.

## Learning Objectives

At the end of this project, you should be able to explain, without the help of
Google:

- What a caching system is
- What the purpose of a caching system is
- What limits a caching system has
- **FIFO** — First In, First Out: discards the oldest inserted item
- **LIFO** — Last In, First Out: discards the most recently inserted item
- **LRU** — Least Recently Used: discards the least recently accessed item
- **MRU** — Most Recently Used: discards the most recently accessed item
- **LFU** — Least Frequently Used: discards the least frequently accessed item

## Requirements

- Interpreted on **Ubuntu 20.04 LTS** using **python3 (3.9)**
- All files end with a new line
- The first line of every file is exactly `#!/usr/bin/env python3`
- Code follows the **pycodestyle** style (version 2.5)
- All files are executable
- All modules, classes and functions are documented with real sentences

## Parent class — `BaseCaching`

Every caching class inherits from `BaseCaching`, which defines:

- `MAX_ITEMS = 4` — the maximum number of items a cache can hold
- `self.cache_data` — the dictionary where items are stored
- `print_cache()` — prints the current state of the cache
- `put(key, item)` / `get(key)` — abstract methods to implement in each child

## Tasks

| Task | File | Class | Policy |
|------|------|-------|--------|
| 0. Basic dictionary | `0-basic_cache.py` | `BasicCache` | No limit |
| 1. FIFO caching | `1-fifo_cache.py` | `FIFOCache` | FIFO |
| 2. LIFO Caching | `2-lifo_cache.py` | `LIFOCache` | LIFO |
| 3. LRU Caching | `3-lru_cache.py` | `LRUCache` | LRU |
| 4. MRU Caching | `4-mru_cache.py` | `MRUCache` | MRU |
| 100. LFU Caching | `100-lfu_cache.py` | `LFUCache` | LFU |

> Only task 0 (`BasicCache`) is implemented so far.

### Task 0 — `BasicCache`

A caching system **without any limit**:

- `put(self, key, item)` — assigns `item` to `key` in `self.cache_data`.
  Does nothing if `key` or `item` is `None`.
- `get(self, key)` — returns the value linked to `key`, or `None` if `key`
  is `None` or does not exist.

## Usage

```bash
$ ./0-main.py
Current cache:
Current cache:
A: Hello
B: World
C: Holberton
Hello
World
Holberton
None
Current cache:
A: Hello
B: World
C: Holberton
Current cache:
A: Street
B: World
C: Holberton
D: School
E: Battery
Street
```

## Files

| File | Description |
|------|-------------|
| `base_caching.py` | Parent class `BaseCaching` (provided) |
| `0-basic_cache.py` | Task 0 — `BasicCache` class |
| `0-main.py` | Test script for task 0 |

## Author

- **apsamade** — [GitHub](https://github.com/apsamade)
