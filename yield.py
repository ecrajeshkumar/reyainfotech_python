### yield turns a normal function into a generator function.
### Instead of returning once, it pauses and resumes execution each time you call next() or iterate over it.
### This makes it ideal for streaming large or infinite sequences.
### Efficiency: No need to store huge lists in memory.
### Flexibility: Can pause/resume execution.
### Streaming: Perfect for reading large files line by line, or generating infinite sequences.

import pdb

def fibonacci(n):   # Generates the first n Fibonacci numbers
    a, b = 0, 1
    # pdb.set_trace()   # Debugger will pause here
    for _ in range(n):  #   The underscore _ is used because we don’t care about the loop index, just the repetition count. This loop will run exactly n times.
        yield a         # Instead of return, we use yield. This pauses the function and sends the current value of a to the caller. Next time the generator is resumed, execution continues right after this line.
        a, b = b, a + b 

# Usage
for num in fibonacci(10):
    print(num)
# Output: 0 1 1 2 3 5 8 13 21 34

def is_prime(num):  # Helper function to check if a number is prime
    if num <= 1 :
        return False
    for i in range(2, int(num**0.5) + 1) :
        if num % i == 0 :
            return False
    return True

def prime_generator(n):  # Generates all prime numbers up to n
    for num in range(2, n +1) :
        if is_prime(num) :
            yield num 

# Uses
for p in prime_generator(50):
    print(p, end = " ")
# Output: 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47


def infinite_counter():  # Generates an infinite sequence of numbers starting from 0
    count = 0
    while True:  # Infinite loop
        yield count  # Yield the current count
        count += 1   # Increment the count for the next iteration

gen = infinite_counter()  # Create a generator for an infinite sequence of numbers
for _ in range(5) :
    print(next(gen))
# Output : 0, 1, 2, 3, 4
