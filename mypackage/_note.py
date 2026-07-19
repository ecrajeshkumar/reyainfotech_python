''' Meaning of _ (single underscores), __ (double underscores) and __xyz__ (double underscore at both end i.e. dunder) 
In Python, the use of underscores has specific meanings:

1. Single Underscore (_): A single underscore is often used as a variable name to indicate that the variable is temporary or insignificant. 
It can also be used in loops to ignore the loop variable. For example:
in python used when you don’t care about the value:

A.
_ = 5  # Indicates that the variable is temporary or insignificant

B.
for _ in range(5): # Here _ is just a placeholder; we don’t use the loop variable.
    print("Hello")

C.
In the Python interactive shell, _ stores the result of the last expression:
>>> 5 + 3
8
>>> _
8

D.
Convention for “private” names  
A single leading underscore in a variable or method name means “internal use only”:
class MyClass:
    def __init__(self):
        self._hidden = 42   # meant as private

2. Double Underscore (__): A double underscore at the beginning of a variable or method name is used to indicate that it is intended for internal use within a class. 
This is known as name mangling, where the interpreter changes the name of the variable to include
    
A.
Name mangling (stronger privacy). Attributes with double leading underscores are “mangled” to avoid accidental access:
class MyClass:
    def __init__(self):
        self.__secret = 99

obj = MyClass()
# print(obj.__secret) → AttributeError
print(obj._MyClass__secret)  # 99 (mangled name)
This prevents subclasses or external code from accidentally overriding or accessing them.

3. Double Underscore at Both Ends (__xyz__): Names with double underscores at both ends are reserved for special use in the language.
These are often referred to as “dunder” methods or attributes. They are used to implement special behavior in classes, such as operator overloading or 
defining how objects are represented. Examples include:
A. 
class MyClass:
    def __init__(self):   # constructor
        pass
    def __str__(self):    # string representation
        return "MyClass object"

'''

class Demo:
    def __init__(self):
        self.value = 10          # normal attribute
        self._hidden = 20        # single underscore (weakly private)
        self.__secret = 30       # double underscore (name mangling)

obj = Demo()

# Accessing attributes
print("Normal:", obj.value)        # Works directly
print("Single underscore:", obj._hidden)   # Works directly, but by convention "internal use"
# print(obj.__secret)              # ❌ AttributeError
print("Double underscore (mangled):", obj._Demo__secret)  # Access via mangled name

