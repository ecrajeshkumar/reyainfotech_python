
# [expression for item in iterable if condition]

# expression → what you want to store in the list
# item → variable representing each element
# iterable → sequence (list, range, string, etc.)
# condition → optional filter

squares = [x**2 for x in range(1, 6)]
print(squares)   # [1, 4, 9, 16, 25]

even_squares = [x**2 for x in range(1, 6) if x % 2 == 0]
print(even_squares)   # [4, 16]

words = ["Rajesh", "Python", "AI"]
lowercase = [w.lower() for w in words]
print(lowercase)   # ['rajesh', 'python', 'ai']

matrix = [[1, 2], [3, 4], [5, 6]]
flat = [num for row in matrix for num in row]
print(flat)   # [1, 2, 3, 4, 5, 6]

def factorial(n):
    return 1 if n == 0 or n == 1 else n * factorial(n - 1)

factorials = [factorial(x) for x in range(1, 6)]
print(factorials)   # Output: [1, 2, 6, 24, 120]


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

primes = [x for x in range(1, 51) if is_prime(x)]
print(primes)   # Output: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

