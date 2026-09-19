# decorator function to convert to lowercase
def lowercase_decorator(function):
    print("1_Inside lowercase_decorator")
    def wrapper_1():
        print("9_Inside wrapper of lowercase_decorator")
        ret = function() # calling the original hello function
        print("ret value inside wrapper_1 => ", ret) # ret value inside wrapper_1 =>  Hello World
        string_lowercase = ret.lower()
        print("string_lowercase value inside wrapper_1 => ", string_lowercase) # string_lowercase value inside wrapper_1 =>  hello world
        print("11_Returning wrapper of lowercase_decorator")
        return string_lowercase
    print("2_Returning lowercase_decorator")
    return wrapper_1

# decorator function to split words
def splitter_decorator(function_2):
    print("3_Inside splitter_decorator")
    def wrapper_2():
        print("8_Inside wrapper of splitter_decorator")
        func = function_2() #calling the function which is returned by lowercase_decorator means calling wrapper_1 function
        # func = "hello worldss" # This is for testing purpose. If you want to test the splitter_decorator only then you can uncomment this line and comment the above line.
        print("func value inside wrapper_2 => ", func)  # func value inside wrapper_2 =>  hello world. it is the return value of wrapper_1 function
        string_split = func.split()
        print("string_split value inside wrapper_2 => ", string_split) # string_split value inside wrapper_2 =>  ['hello', 'world']
        print("12_Returning wrapper of splitter_decorator")
        return string_split # returning the list of words. where it is the return value of wrapper_2 function
    print("4_Returning splitter_decorator")
    return wrapper_2
 
def test_decorator(function_3):
    print("5_Inside test_decorator")
    def wrapper_3():
        print("7_Inside wrapper of test_decorator")
        func = function_3() #calling the function which is returned by splitter_decorator means calling wrapper_2 function
        print("func value inside wrapper_3 => ", func)  # func value inside wrapper_3 =>  ['hello', 'world']. it is the return value of wrapper_2 function
        print("13_Returning wrapper of test_decorator")
        return func # returning the list of words. where it is the return value of wrapper_3 function
    print("6_Returning test_decorator")
    return wrapper_3

@test_decorator # this is executed next
@splitter_decorator # this is executed next
@lowercase_decorator # this is executed first
def hello():
    print("10_Inside hello function")
    return 'Hello World'
ret = hello()   # output => [ 'hello' , 'world' ]
print("ret value => ", ret) # ret value =>  ['hello', 'world']

