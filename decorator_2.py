# decorator function to convert to lowercase
def lowercase_decorator(function):
    print("1_Inside lowercase_decorator")
    def wrapper_1():
        print("6_Inside wrapper of lowercase_decorator")
        ret = function() # calling the original hello function
        print("ret value inside wrapper_1 => ", ret) # ret value inside wrapper_1 =>  Hello World
        string_lowercase = ret.lower()
        print("string_lowercase value inside wrapper_1 => ", string_lowercase) # string_lowercase value inside wrapper_1 =>  hello world
        print("8_Returning wrapper of lowercase_decorator")
        return string_lowercase
    print("2_Returning lowercase_decorator")
    return wrapper_1
# decorator function to split words
def splitter_decorator(function_2):
    print("3_Inside splitter_decorator")
    def wrapper_2():
        print("5_Inside wrapper of splitter_decorator")
        func = function_2() #calling the function which is returned by lowercase_decorator means calling wrapper_1 function
        # func = "hello worldss" # This is for testing purpose. If you want to test the splitter_decorator only then you can uncomment this line and comment the above line.
        print("func value inside wrapper_2 => ", func)  # func value inside wrapper_2 =>  hello world. it is the return value of wrapper_1 function
        string_split = func.split()
        print("string_split value inside wrapper_2 => ", string_split) # string_split value inside wrapper_2 =>  ['hello', 'world']
        print("9_Returning wrapper of splitter_decorator")
        return string_split # returning the list of words. where it is the return value of wrapper_2 function
    print("4_Returning splitter_decorator")
    return wrapper_2
 
@splitter_decorator # this is executed next
@lowercase_decorator # this is executed first
def hello():
    print("7_Inside hello function")
    return 'Hello World'
ret = hello()   # output => [ 'hello' , 'world' ]
print("ret value => ", ret) # ret value =>  ['hello', 'world']

'''
When Python sees the decorators then It applies them from bottom to top at definition time. And Wrappers are executed top to bottom at call time.
Each wrapper adds its own logic before/after calling the next function in the chain.

When Python applies the decorator, it executes the body of lowercase_decorator immediately with the original hello function as its argument.
1. hello is passed into lowercase_decorator
2. wrapper_1 is defined but not executed yet. 
3. Return happens from lowercase_decorator and hello is replaced with wrapper_1 in the current scope.
So now, hello points to wrapper_1, but inside wrapper_1 the variable function still refers to the original hello function.
At definition time, hello is replaced with wrapper_1.
But inside wrapper_1, the variable function is a closure reference to the original hello.
So when you see ret = function(), it’s not calling wrapper_1 again — it’s calling the original hello() body.

At call time, the stack unwinds: wrapper_2 → wrapper_1 → original hello.

definition time:
hello is first passed into lowercase_decorator and hello is replaced with wrapper_1.
Then the wrapper_1 function is passed into splitter_decorator and hello is replaced with wrapper_2.
now the function hello actually refers to wrapper_2.

Function Call Phase:
    When we call hello(), it actually calls wrapper_2() function (from splitter_decorator). inside wrapper_2, it calls the function it wraps → which is wrapper_1.
    now wrapper_1() runs (from lowercase_decorator). Calls the function it wraps → which is the original hello. and enter the hello function and return the string 'Hello World' to wrapper_1.
    and so on ...


'''