### An iterator is an object that allows you to traverse through a sequence (like a list, tuple, or string) one element at a time.
### It implements two special methods:
    ### __iter__() → returns the iterator object itself.
    ### __next__() → returns the next value, and raises StopIteration when no items are left.

numbers = [1, 2, 3]
iterator = iter(numbers)

print(next(iterator))  # 1
print(next(iterator))  # 2
print(next(iterator))  # 3
# next(iterator) → raises StopIteration


print("We can build your own iterator by defining __iter__ and __next__.")
class CountDown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.start <= 0:
            raise StopIteration
        current = self.start
        self.start -= 1
        return current

# Usage
for num in CountDown(5): # Calls __init__ with start=5. Then __iter__ returns the iterator object (self), and __next__ is called repeatedly until StopIteration is raised.
    print(num)
'''
    for num in CountDown(5):
    1. Object Creation
        CountDown(5)
        It Calls __init__ with start=5. Stores self.start = 5.
    2. Entering the for loop
        for num in CountDown(5):
            Python internally calls iter() on the object.
            This triggers __iter__().
            Your __iter__ returns self, meaning the object itself is the iterator.
            Calls __iter__() → returns the iterator object (self).
            
            First Iteration
                Python calls next() on the iterator.
                This triggers __next__().
                self.start = 5, so it’s > 0.
                current = 5, then self.start becomes 4.
                Returns 5.
                Loop assigns num = 5 and prints it.
            Second Iteration
                Python calls next() again. 
                and continue ...
'''
# Output: 5 4 3 2 1

print( "Iterators vs Generators")
'''Iterators → You write __iter__ and __next__ manually.
Generators → You use yield to simplify iterator creation.
'''
def countdown_gen(start):
    while start > 0:
        yield start
        start -= 1

for num in countdown_gen(5):
    print(num)
# Output: 5 4 3 2 1
