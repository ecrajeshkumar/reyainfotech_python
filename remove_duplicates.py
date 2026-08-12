# Can you remove duplicates from a sorted array?

# method 1: 
arr = [1, 1, 2, 2, 3, 4, 4]
unique_arr = []
for i in arr:
    if i not in unique_arr:
        unique_arr.append(i)
print(unique_arr)  # Output: [1, 2, 3, 4]

# method 2: Using a set
unique_arr = list(set(arr))
print(unique_arr)  # Output: [1, 2, 3, 4]

# method 3: Using a set
arr = [1, 1, 2, 2, 3, 4, 4]
unique = sorted(set(arr))
print(unique)   # [1, 2, 3, 4]


arr = [1, 19, 1, 5, 3, 10, 2, 9, 2, 3, 4, 8, 4]

# Method 4: Using set (quick and simple), not preserve order
unique = list(set(arr))
print("Unique elements:", unique)  # OP: Unique elements: [1, 2, 3, 4, 5, 8, 9, 10, 19]   # order not guaranteed but unique elements are present and assending order can be achieved by sorting the list after converting to set.


# Method 5: Using set, preserve order as given in the list
unique = []
for i in arr:
    if i not in unique:
        unique.append(i)
print("Unique elements (order preserved):", unique)  # OP: Unique elements (order preserved): [1, 19, 5, 3, 10, 2, 9, 4, 8]



