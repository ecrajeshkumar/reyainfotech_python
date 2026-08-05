class CountDown:
    def __init__(self, start):
        self.num = start
    def __iter__(self):
        return self
    def __next__(self):
        if self.num <= 0:
            raise StopIteration
        self.num -= 1
        return self.num

cd = CountDown(5)
for n in cd:
    print(n)

'''
OP: 
4
3
2
1
0
'''
'''
Explanation:

1. for calls iter() internally
    When you start a for loop, Python automatically calls iter(cd).
    This looks for the __iter__() method in your class.
    In your CountDown class, __iter__() returns self, meaning the object itself is the iterator.
2. for repeatedly calls next()
    Python then calls next(cd) in each loop iteration.
    This triggers your __next__() method.
    Each time, it returns the next value (self.num - 1) until the condition fails.
3. Loop ends with StopIteration
    When __next__() raises StopIteration, the loop stops automatically.
    That’s why you don’t need to manually handle loop termination.

cd = CountDown(5)

# for loop starts
it = iter(cd)          # calls cd.__iter__(), returns cd itself
n = next(it)           # calls cd.__next__(), returns 4
print(n)               # prints 4

n = next(it)           # returns 3
print(n)               # prints 3

n = next(it)           # returns 2
print(n)               # prints 2

n = next(it)           # returns 1
print(n)               # prints 1

n = next(it)           # returns 0
print(n)               # prints 0

next(it)               # raises StopIteration → loop ends

'''