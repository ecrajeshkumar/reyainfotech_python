
square = lambda x: x * x
print(square(5))   # Output: 25

numbers = [1, 2, 3, 4]
squares = list(map(lambda x: x**2, numbers))
print(squares)   # Output: [1, 4, 9, 16]

numbers = [10, 15, 20, 25, 30]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)   # Output: [10, 20, 30]

pairs = [(1, 'one'), (3, 'three'), (2, 'two')]
sorted_pairs = sorted(pairs, key=lambda x: x[1])
print(sorted_pairs)   # Output: [(3, 'three'), (2, 'two'), (1, 'one')]

