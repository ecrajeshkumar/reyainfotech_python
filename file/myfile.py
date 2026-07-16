# Python uses the open() function to open files. It takes two arguments: the file name and the mode (read, write, etc.).

# Read entire file
file = open("example.txt", "r")
content = file.read()
print(content)
file.close()

# Read line by line
file = open("example.txt", "r")
for line in file:
    print(line.strip())
file.close()

# Write (overwrites file if exists)
file = open("example2.txt", "w")
file.write("Hello Rakesh!\n")
file.write("This is a new line.")
file.close()

# Append (adds to existing file)
file = open("example2.txt", "a")
file.write("\nAdding more text.")
file.close()

# Using with automatically closes the file:
with open("example2.txt", "r") as file:
    content = file.read()
    print(content)

with open("example2.txt", "a") as file:
    file.write("Safe file handling with 'with'.")



