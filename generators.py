
# What Are Generator Expressions?
### They look like list comprehensions but use parentheses () instead of square brackets [].
### Instead of building the entire list in memory, they generate items one by one — much more memory-efficient for large datasets.

gen = (x**2 for x in range(1, 6))
print(gen)          # Output: <generator object ...>
print(next(gen))    # 1
print(next(gen))    # 4

### next(gen) pulls the next value.
### Generators don’t store all values at once — they produce them on demand.

gen = (x**2 for x in range(1, 6))
for val in gen:
    print(val)
# Output: 1, 4, 9, 16, 25

gen = (x**2 for x in range(1, 6))
for val in gen:
    print(val)
# Output: 1, 4, 9, 16, 25

total = sum(x**2 for x in range(1, 101))
print(total)   # Sum of squares from 1 to 100

