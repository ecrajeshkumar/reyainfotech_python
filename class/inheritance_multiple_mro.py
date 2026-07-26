'''
Method Resolution Order (MRO) defines the order in which Python searches for a method in a class and its 
parent classes. 

When obj.fun() is called, Python follows the MRO shown by D.__mro__.
It checks D, then B, then C, then A.
Since B defines fun(), that method is executed and the search stops.
'''

class A:
    def __init__(self):
        print("Constructor A")
    def fun(self):
        print("In class A")

class B(A):
    def __init__(self):
        print("Constructor B")
    def fun(self):
        print("In class B")

class C(A):
    def __init__(self):
        print("Constructor C")
    def fun(self):
        print("In class C")

class D(B, C):
    def __init__(self):
        print("Constructor D")
        super().fun()

obj = D()
obj.fun()

print(D.__mro__)

