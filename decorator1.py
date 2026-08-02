
# A simple decorator
def my_decorator(func):
    def rajesh():
        print("Before the function runs...")
        func()
        print("After the function runs...")
    return rajesh

@my_decorator
def say_hello():
    print("Hello, Rajesh!")

say_hello()



# Common decorator in python

class MathUtils:
    @staticmethod
    def sum(a, b):
        return a + b;

print(MathUtils.sum(10,20))

class Person:
    def __init__(self, name) :
        self.name = name
    @classmethod
    def from_string(cls, data) :
        return cls(data.split("-")[0])

p = Person.from_string("Rajesh-35")
print(p.name)


class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def area(self):
        return 3.14 * (self._radius ** 2)

c = Circle(5)
print(c.area)   # Output: 78.5









