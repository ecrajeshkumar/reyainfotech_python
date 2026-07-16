from mypackage import math_utils

print(math_utils.factorial(5))   # Output: 120
print(math_utils.is_prime(7))    # Output: True

# import specific functions:
from mypackage.string_utils import reverse_string, count_vowels

print(reverse_string("Hello, World!"))  # Output: !dlroW ,olleH
print(count_vowels("Hello, World!"))   # Output: 3

