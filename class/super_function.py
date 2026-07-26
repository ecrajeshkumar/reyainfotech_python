'''
Super Function in Python is used to call a method from a parent (base) class, especially in multiple inheritance.
uper() function is used to call methods from a parent (superclass) inside a child (subclass).

'''


class Class1:
    def m(self):
        print("In Class1")

class Class2(Class1):
    def m(self):
        print("In Class2")
        super().m()

class Class3(Class1):
    def m(self):
        print("In Class3")
        super().m()

class Class4(Class2, Class3):
    def m(self):
        print("In Class4")
        super().m()
     
obj = Class4()
obj.m()