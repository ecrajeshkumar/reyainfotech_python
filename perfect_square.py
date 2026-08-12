# Given a positive integer num, write a function that returns True if num is a perfect square else False.

import math

def is_perfect_square(num) :
    if num < 0 :
        return False
    root = int(math.sqrt(num))
    return root * root == num

print(is_perfect_square(16))  # True