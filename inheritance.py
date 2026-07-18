class Demo:
    def __init__(self):
        self.value = 10          # normal attribute
        self._hidden = 20        # single underscore (weakly private)
        self.__secret = 30       # double underscore (name mangling)

class Derived(Demo):
    def __init__(self):
        super().__init__()       # call parent constructor
        self.value = 100         # overrides parent normal attribute
        self._hidden = 200       # overrides parent single underscore
        self.__secret = 300      # creates a NEW mangled attribute

# Usage
obj = Derived()

print("Normal:", obj.value)          # 100 (overridden)
print("Single underscore:", obj._hidden)   # 200 (overridden)

# Double underscore attributes
# Parent's __secret is still there, mangled as _Demo__secret
print("Parent secret:", obj._Demo__secret)   # 30
# Child's __secret is separate, mangled as _Derived__secret
print("Child secret:", obj._Derived__secret) # 300
