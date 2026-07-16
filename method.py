# In Python, functions are defined using the def keyword:

def add(a, b):
    return a + b

result = add(5, 3)   # result = 8
print(result)  # Output: 8

print("Factorial of n")
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1) 

print("Factorial of 5:", factorial(5))  # Output: 120

print("Prime Number Check")
def is_prime(n):
    # print(int(n ** 0.5) + 1)
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

print("Is 7 a prime number?", is_prime(7))  # Output: True
print("Is 4 a prime number?", is_prime(4))  # Output: False

print("Fibonacci Sequence")
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        sequence = fibonacci(n - 1)
        sequence.append(sequence[-1] + sequence[-2])
        print(f"{sequence[-1]} {sequence[-2]}")
        return sequence

print("Fibonacci sequence of 10:", fibonacci(10))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]  
