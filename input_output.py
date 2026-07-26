
'''
name = input("Enter your name: ")
print("Hello, " ,name, "! Welcome")
#print(f"Hello, {name} ! Welcome")

s = "Anjelina"
age = 25
city = "New York"
print(s, age, city)

print("take multiple inputs at once ")
x,y = input("Enter two number: ").split()
print(x,y)

i = int(input("How old are you?: "))
f = float(input("Evaluate 7/2: "))
print(i, f)

# This reads a line of input, splits it by spaces, and converts each piece into an integer.
# Example: if you type 1 2 3 4 5, then arr = [1, 2, 3, 4, 5].
arr = [int(x) for x in input().split()]
summation = 0
for x in arr:
    summation += x
print(summation)

from sys import stdin, stdout 
def main():
    arr = [int(x) for x in stdin.readline().split()]
    summation = sum(arr)
    stdout.write(str(summation))

if __name__ == "__main__":
    main()

print("Taking User Input in Separate Variables")
import sys
def get_ints(): 
    return map(int, sys.stdin.readline().strip().split())
a, b, c, d = get_ints()
print(a, b, c, d)


print("Taking User Inputs as a List of Integers")
import sys
def get_list(): 
    return list(map(int, sys.stdin.readline().strip().split()))
Arr = get_list()
print(Arr)

'''
import sys
def get_string(): 
    return sys.stdin.readline().strip()
string = get_string()


