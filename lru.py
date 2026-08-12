from functools import lru_cache

@lru_cache(maxsize=3)
def add(a, b):
    return a + b

print(add(1, 2))  # Calculates and caches result
print(add(1, 2))  # Retrieves result from cache
print(add(2, 3))  # Calculates and caches (5)
print(add(3, 4))  # Calculates and caches (7)
print(add(4, 5))  # Calculates and caches (9)