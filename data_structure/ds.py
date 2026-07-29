
print("1. DS: string")
name = 'Rajesh'
print(name)

print("Multi-line string")
str = """I am Rajesh
         Learning python multi string """
print(str)

str1 = '''I am 
         Rajesh'''
print(str1)

str = "ABCDEF"
print(str[3])
print(str[-3])

print("2. DS: Arrays")
print("Python does not have a built-in array type like some other languages, similar functionality can be achieved using: Lists")

import array as arr
a = arr.array('i', [1, 2, 3])

# accessing first array
print(a[0])

# adding element to array
a.append(5)
print(a)

a = arr.array('i', [1, 2, 3])
print(*a)

a.insert(1, 4)  # Insert 4 at index 1
print(*a)

b = arr.array('d', [2.5, 3.2, 3.3])
print(b[1])
print(b[2])

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = arr.array('i', a)
print(*b)


print("3: DS: List")
print("1. Using Square Brackets: Square brackets [] are used to create a list directly.")
print("Using list() Constructor: A list can also be created by passing an iterable (such as tuple, string or another list) to the list() constructor")
a = [1, 2, 3]
print(a)

b = list("GFG")
print(b)
a = list((1, 2, 3, 'apple', 4.5))  
print(a)

a = [10, 20, 30]
print(a[0])
print(a[-1])

a = ['apple', 'banana', 'cherry']
for item in a:
    print(item)

print("Nested Lists")
a = [[1, 2], [3, 4]]
print(a[0])
print(a[1][0])

print("4. DS: Dictionary")
data = { "name": "Jake", "age": 22 }
print(data)

d = {"a": 1, "b": 2}
for key, value in d.items():
    print(key, value)
d = {"a": 1, "b": 2}
for value in d.values():
    print(value)

print("5: DS: SET")
s = {10, 50, 20}
print(s)
print(type(s))

print("set() method is used to convert other data types, such as lists or tuples, into sets.")
s = set(["a", "b", "c"])
print(s)

s = {"Geeks", "for", 10, 52.7, True}
print(s)

s = set(["a", "b", "c"])
print("Normal Set:", s)
fs = frozenset(["e", "f", "g"])
print("Frozen Set:", fs)


print("6: DS: Tuples")
'''
Tuples are similar to lists, but unlike lists, they cannot be changed after their creation.
Can hold elements of different data types.
These are ordered, heterogeneous and immutable.
'''

tup = ()
print(tup)

# Using String
tup = ('Geeks', 'For')
print(tup)

# Using List
li = [1, 2, 4, 5, 6]
print(tuple(li))

# Using Built-in Function
tup = tuple('Geeks')
print(tup)

tup = (5, 'Welcome', 7.5, True, [1, 2, 3], {'key': 'value'})
print(tup)

tup = (0, 1, 2, 3, 4)
del tup
print(tup)

tup = (1, 2, 3, 4, 5)
a, *b, c = tup
print(a) 
print(b) 
print(c)