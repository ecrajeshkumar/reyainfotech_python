'''
comprehensions are a concise way to create new sequences (like lists, sets, or dictionaries) by looping and optionally applying conditions.
The two most commonly used are list comprehensions and dictionary comprehensions.
'''

'''
1. List Comprehension
Purpose: Creates a new list by applying an expression to each item in an iterable.
Syntax: [expression for item in iterable if condition]
'''
numbers = [1,2,3,4,5,6]
squares = [x*x for x in numbers]
print(squares)
squares_evennumber = [x*x for x in numbers if (x%2 == 0)]
print(squares_evennumber)

'''
2. Dictionary Comprehension
Purpose: Creates a new dictionary by mapping keys to values using an expression.
Syntax: {key_expression: value_expression for item in iterable if condition}
'''

numbers = [1, 2, 3, 4, 5, 6]
num_dict = {x: x**2 for x in numbers}
print(num_dict)   # Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

num_dict_even = {x: x**2 for x in numbers if x%2 == 0}
print(num_dict_even)




