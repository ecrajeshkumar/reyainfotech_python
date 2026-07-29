
unique_squares = {x**2 for x in [1, 2, 2, 3, 3, 4]}
print(unique_squares)   # {1, 4, 9, 16}

text = "Hello Rajesh"
vowels = {ch for ch in text if ch.lower() in "aeiou"}
print(vowels)   # {'a', 'e', 'o'}

