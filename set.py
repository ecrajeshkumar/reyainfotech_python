# a set is a collection type that stores unique values only — duplicates are automatically removed. 
# It’s also unordered, meaning the items don’t have a fixed position like in a list.
# Sets are great when you need to eliminate duplicates or perform mathematical operations like union and intersection.

# Creating a set
fruits = {"apple", "banana", "orange", "apple"}

print(fruits) # "apple" appears only once, even though we added it twice.
# A set is also unordered, meaning Python doesn’t guarantee the order of elements when printing.
# When you print, Python shows the set in an arbitrary order (not the order you typed).
# output is {'banana', 'orange', 'apple'} instead of exactly {"apple", "banana", "orange"}.
#  If you want to preserve order and allow duplicates, use a list instead:

fruits = ["apple", "banana", "orange", "apple"]
print(fruits)

# Sets are best when you need unique values and don’t care about order. Lists are best when you need order preserved and duplicates allowed.


# Define two sets
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Union (combine unique elements)
print(A | B)   # {1, 2, 3, 4, 5, 6}

# Intersection (common elements)
print(A & B)   # {3, 4}

# Difference (elements in A but not in B)
print(A - B)   # {1, 2}

# Symmetric Difference (elements in either A or B but not both)
print(A ^ B)   # {1, 2, 5, 6}


