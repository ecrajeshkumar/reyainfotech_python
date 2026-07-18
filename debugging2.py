
# Debugger tools: Use pdb (Python Debugger) or IDE debuggers (VS Code, PyCharm).
# This lets you step through code line by line.

import pdb

def divide_numbers(a, b):
    result = a / b
    return result

def main():
    x = 10
    y = 0   # This will cause ZeroDivisionError
    pdb.set_trace()   # Debugger will pause here
    print("Before division")
    result = divide_numbers(x, y)
    print("Result:", result)

if __name__ == "__main__":
    main()

# When you run this script, execution stops at pdb.set_trace().

# You’ll enter the interactive debugger prompt (Pdb).

# Common commands you can use:

## n → Next line

## c → Continue execution

## l → List code around current line

## p variable → Print value of a variable

## q → Quit debugger

### > main()
### (Pdb) p x
### 10
### (Pdb) p y
### 0
### (Pdb) n
### Before division
### (Pdb) c
### ZeroDivisionError: division by zero
