# decorator function to convert to lowercase
def lowercase_decorator(function):
    print("1_Inside lowercase_decorator")
    def wrapper():
        print("6_Inside wrapper of lowercase_decorator")
        ret = function()
        string_lowercase = ret.lower()
        print("8_Returning wrapper of lowercase_decorator")
        return string_lowercase
    print("2_Returning lowercase_decorator")
    return wrapper
# decorator function to split words
def splitter_decorator(function):
    print("3_Inside splitter_decorator")
    def wrapper():
        print("5_Inside wrapper of splitter_decorator")
        func = function()
        string_split = func.split()
        print("9_Returning wrapper of splitter_decorator")
        return string_split
    print("4_Returning splitter_decorator")
    return wrapper

@splitter_decorator # this is executed next
@lowercase_decorator # this is executed first
def hello():
    print("7_Inside hello function")
    return 'Hello World'
hello()   # output => [ 'hello' , 'world' ]
