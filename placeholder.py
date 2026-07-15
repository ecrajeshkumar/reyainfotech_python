# placeholders in strings


name = "Alice"
sentence = "%s is 15 years old"
print(sentence % name)


name = "Alice"
age = 30
sentence = "%s is %d years old"
print(sentence % (name, age))

message = f"Hello, my name is {name} and I am {age} years old."
print(message)

name = "Alice"
print(f"Hello, my name is {name}!")

x = 10
y = 20
print(f"The sum of {x} and {y} is {x + y}.")
