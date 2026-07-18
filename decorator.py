'''
A decorator is a callable (usually a function) that takes another function as input, adds extra behavior, and returns a new function.
The @decorator_name syntax is shorthand for:

function = decorator_name(function)

'''
### Example 1: Basic Decorator

def my_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@my_decorator
def say_hello():
    print("Hello Rajesh!")

say_hello()


'''
OP:
    Before function call
    Hello Rajesh!
    After function call

say_hello is passed into my_decorator.
The wrapper adds behavior before and after the original function.
The @my_decorator syntax applies the decoration automatically.
'''

### Example 2: Decorator with Arguments

def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello {name}!")

greet("Rajesh")


### Real-world Use (Timing)
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end-start:.4f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(2)
    print("Finished!")

slow_function()


### Multiple decorators can be stacked:
@decorator1
@decorator2
def func():
    pass

### Equivalent to func = decorator1(decorator2(func)).

