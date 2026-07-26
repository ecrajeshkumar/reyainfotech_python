
print("Keyword Arguments: pass values using parameter names, so argument order does not matter.")

def student(fname, lname):
    print(fname, lname)

student(fname="Rajesh", lname="kumar")
student(lname="kumar", fname="Rajesh")
student("Rajesh", "Kumar")
student("Kumar", "Rajesh")

print("=========================================")
print("Arbitrary Arguments: allow functions to accept multiple values. This is done using two special symbols:")
print("*args collects extra positional arguments as a tuple.")
print("**kwargs collects extra keyword arguments as a dictionary.")    
def myFun(*args, **kwargs):
    print("Non-Keyword Arguments(*args):")
    for arg in args:
        print(arg)
    
    print("keyword Arguments (**kwargs):")
    for key, value in kwargs.items():
        print(f"{key} == {value}")

myFun("Rajesh", "kumar", first="Geeks", mid="for", last="geeks")


print("=========================================")
def f1():
    print("inside f1")
    s = 'I love GeeksforGeeks'
    def f2():
        print("inside f2")
        print(s)
    f2()

f1()
##f2()


print("=========================================")
def list_mutable(x):
    x[2] = 100

b = [10,20,30,40,50]
list_mutable(b)
print(b)

def immutable_var(x):
    x = 20

x = 10
immutable_var(x)
print(x)
