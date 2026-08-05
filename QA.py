How would you explain the difference between tuples and lists in Python?
Ans: Lists are mutable and allow modifications, while tuples are immutable and fixed once created. Lists are used for dynamic collections, whereas tuples are used for constant data or when immutability is required.
    my_list = [1, 2, 3]. my_tuple = (1, 2, 3)
    
Explain what is meant by PEP?
Ans: PEP stands for Python Enhancement Proposal. It’s essentially a design document that describes new features, improvements, or processes for the Python language.

What are some of Python’s key benefits?
Ans: Its syntax is simple and close to English. Used in web development, data science, AI/ML, automation, scripting, scientific computing, and more.
     Pandas, NumPy, Matplotlib, TensorFlow, PyTorch, Django, Flask — covering everything from data analysis to web apps and AI.
     Cross Platform Compatibility. Works well with other languages like C, C++, and Java, and integrates with databases and web services.

Could you explain the meaning of a Python namespace?
Ans: A namespace in Python is a mapping between names and objects.

Could you define what is meant by decorators?
Ans: A decorator is a special function that allows us to modify or enhance the behavior of another function or class without changing its actual code.
     @staticmethod : 
     Used when a method doesn’t need access to the instance (self) or class (cls).
     It behaves like a normal function but lives inside the class for logical grouping.
     @classmethod :
     Used when a method needs access to the class itself (via cls) rather than an instance.
     Often used for alternative constructors.
     @property :
     Used to define getter methods that can be accessed like attributes.
    
Explain two main comprehensions. What do they do?
Ans: comprehensions are a concise way to create new sequences (like lists, sets, or dictionaries) by looping and optionally applying conditions. The two most commonly used are list comprehensions and dictionary comprehensions.
    numbers = [1, 2, 3, 4, 5]
    squares = [x**2 for x in numbers]

Could you explain two main built-in types of data in Python?
Ans: List: An ordered, mutable collection of items. Allows duplicates, Supports indexing and slicing, Can be modified (add, remove, update elements).
     Tuple: An ordered, immutable collection of items. Allows duplicates, Supports indexing and slicing, Cannot be modified once created.
     
Explain how .py and .pyc files are different.
Ans: .py file are plain text files containing source code. After compilation .py convert in .pyc (bytecode) and save in __pycache__ directory.

Could you explain what slicing means in Python?
Ans: It’s a way to access a range of elements without writing loops.
     givenList[start:stop:step]
     
Could you explain what keywords are in Python?
Ans: if, else, for, while, def, class, return, import, try, except, True, False, None.

Which best practices should a data engineer or data scientist follow in order to use Python efficiently?
Ans: it’s about writing code that scales, is maintainable, and integrates well with data workflows.
     NumPy → For numerical computations.
     Pandas → For structured data manipulation.
     Matplotlib/Seaborn → For visualization
     Scikit learn → For machine learning basics.
     PySpark/Dask → For distributed data processing.

Which approach would you use to get rid of white spaces from Python strings?
Ans: Removing white spaces from strings can be done in several efficient ways depending on where you want to remove them.
     .strip() removes leading/trailing spaces, .replace() removes all spaces, and regex or split/join can handle complex whitespace scenarios.
     1. Use mystr.strip() → removes spaces from both ends.
        mystr.lstrip() (left side only), mystr.rstrip() (right side only).
     2. Remove all spaces
        mystr.replace(" ", "") → removes every space in the string.

Can you explain which processes are used to do run-time checking of code?
Ans: Python performs run time checking through dynamic type checking, exception handling, assertions, and introspection.

How does the script mode differ from the interactive mode?
Ans: Interactive mode lets you run Python commands one at a time for quick testing, while script mode runs an entire .py file as a program. Interactive mode is great for experimentation, script mode is essential for building real applications.

Are you aware of some Python-supported modes for processing files?
Ans: Python supports several file processing modes, which determine how a file is opened and what operations you can perform on it. These modes are passed as a string argument to the built in open() function. "r", "rb", "w", "wb", "a", "ab", "r+" (Read and write. File must exist.)
    "w+" → Write and read. Creates new file or overwrites existing. "a+" → Append and read. Creates file if it doesn’t exist.
   
Explain what a unit test is in Python.
Ans: Python has a built in unittest module, and popular alternatives like pytest. 

Explain what docstring is in Python.
Ans: A docstring in Python is a string literal placed inside a module, class, or function to document its purpose. It can be accessed at run time via .__doc__ or help(), making it a standard way to embed documentation directly in code.”

What do you understand by negative index?
Ans: Negative indexing in Python allows you to access elements from the end of a sequence. -1 refers to the last element, -2 to the second‑last, and so on.

How would you explain the meaning of pass in Python?
Ans: pass is a no operation statement used as a placeholder to maintain valid syntax when no action is required. It’s commonly used in empty functions, classes, or control structures during development.

Can you explain what a generator is?
Ans: A generator in Python is a function that uses yield to produce values lazily, one at a time. 

Describe what the lambda function does.
Ans: A lambda function in Python is an anonymous, single expression function used for short, inline operations.

What is multithreading in Python?
Ans: Multithreading is a technique that allows multiple threads (smaller units of a process) to run concurrently within the same program. 

Explain what len() does in Python?
Ans: In Python, the len() function is used to return the number of items in an object. 
     numbers = [10, 20, 30, 40]  # On a list
     print(len(numbers))   # 4

    text = "Python"
    print(len(text))   # 6

    data = {"name": "Rajesh", "role": "Tech Lead"}   # dictionary
    print(len(data))   # 2 (two key-value pairs)

Explain what an operator is?
Ans: An operator is a special symbol or keyword that performs an operation on values (operands). +, -, *, <, and, or

Explain what a membership operator is?
Ans: A membership operator is used to test whether a value exists within a sequence (like a list, tuple, string, set, or dictionary). It returns a Boolean (True or False) depending on whether the membership condition is satisfied.
    in → Returns True if the value is present in the sequence.
    not in → Returns True if the value is not present in the sequence.

What is a ternary operator in Python?
Ans: A ternary operator is a shorthand way of writing conditional expressions. 
     x = 10
    result = "Even" if x % 2 == 0 else "Odd"
    print(result)   # Even

    score = 85
    grade = "A" if score >= 90 else "B" if score >= 75 else "C"
    print(grade)   # B

What is meant by help() in Python?
Ans: The help() function is a built in utility that provides interactive documentation about objects, modules, classes, functions, or keywords.

What is meant by dir() in Python?
Ans: The dir() function is a built in utility that returns a list of names (attributes and methods) associated with an object.
     print(dir())  # Shows all names defined in the current scope.
     
     print(dir(str)) # Lists all methods available for strings, like 'upper', 'lower', 'split', etc.

     print(dir(math))  # Displays all functions and constants in the math module.

Define what Python literals are.
Ans:  literals are constant values written directly into the source code, such as numbers, strings, booleans, None, or collections. They represent fixed data that doesn’t need computation.

Explain what the zip() function does in Python.
Ans: zip() combines multiple iterables into tuples, aligning elements by index. It stops at the shortest iterable and is commonly used for pairing related data.

    names = ["Rajesh", "Punam", "Prince"]
    ages = [35, 32, 5]
    combined = list(zip(names, ages))
    print(combined)
    # [('Rajesh', 35), ('Punam', 32), ('Prince', 5)]

    # Unzipping (reverse operation)
    pairs = [('Rajesh', 35), ('Punam', 32)]
    names, ages = zip(*pairs)
    print(names)  # ('Rajesh', 'Punam')
    print(ages)   # (35, 32)

What are the main Python parameter passing mechanisms?
Ans: Python uses pass by object reference (call by sharing). The function receives a reference to the object, not the variable itself. Immutable objects behave like pass by value, while mutable objects behave like pass by reference.

    Immutable objects (like int, float, str, tuple) cannot be changed inside the function — any modification creates a new object.
    Mutable objects (like list, dict, set) can be modified inside the function, and those changes will affect the original object outside the function.
    # Immutable (no change outside)
    def modify(x):
    x = x + 10
    print("Inside:", x) # Inside: 15

    a = 5
    modify(a)
    print("Outside:", a)  # outside: 5

    # Mutable (changes persist)
    def modify_list(lst):
    lst.append(100)
    print("Inside:", lst) # Inside: [1, 2, 3, 100]

    nums = [1, 2, 3]
    modify_list(nums)
    print("Outside:", nums)   # Outside: [1, 2, 3, 100]

What is meant by remove() in Python?
Ans: the remove() method is used to delete the first occurrence of a specified value from a list.
     numbers = [10, 20, 30, 20, 40]
     numbers.remove(20)
     print(numbers)
     # [10, 30, 20, 40]   (only the first 20 is removed)

What is meant by a del statement in Python?
Ans: the del statement is used to delete objects, variables, or specific elements from collections. 
     x = 10
     del x
     print(x)   # NameError: name 'x' is not defined

Can you explain the swapcase() function? What does it do in Python?
Ans:swapcase() is a string method that returns a new string with all uppercase letters converted to lowercase and all lowercase letters converted to  uppercase, leaving non‑alphabetic characters unchanged.”

What is join() in Python?
Ans: the join() method is a string method used to combine elements of an iterable (like a list, tuple, or set) into a single string, with the string  you call it on acting as the separator.
     words = ["Python", "is", "awesome"]
     sentence = " ".join(words)
     print(sentence)
     # Python is awesome

What is a break statement used for in Python?
Ans: x = 1
     while x <= 10:
        if x == 7:
            break
        print(x)
        x += 1

What is an iterator in Python?
Ans: An iterator in Python is an object that implements the iterator protocol (__iter__() and __next__()), allowing sequential access to elements. 

Explain what the enumerate() function does?
Ans: enumerate() is a built in function that returns an iterator of index–element pairs from an iterable. It’s commonly used in loops when both the item and its position are needed.

    names = ["Rajesh", "Punam", "Prince"]
    for index, name in enumerate(names, start=0):
        print(index, name)
    
    0 Rajesh
    1 Punam
    2 Prince
    
What method do you use for task prioritization?
Ans: Focuses on the 20% of tasks that deliver 80% of the value.
    Categorizes tasks into:
        Urgent & Important → Do immediately
        Important but Not Urgent → Schedule
        Urgent but Not Important → Delegate
        Neither → Eliminate

What strategy or approach do you use if you’re unclear about what a project requires?
Ans: If project requirements are unclear, I prioritize stakeholder conversations, break down objectives into smaller goals, and use prototypes or user stories to validate assumptions. I rely on iterative feedback loops to refine scope and ensure alignment.
     
What approach do you use to begin working on a new project?
Ans: When starting a new project, I begin by clarifying objectives, validating requirements, defining scope, and setting up the right team and resources. I often use prototypes and iterative planning to reduce ambiguity and ensure alignment with stakeholders.

Have you built any applications with Python?
Ans: Web Applications → Using frameworks Flask
     Automation Scripts → Automating repetitive tasks (file handling, report generation, scraping).
     APIs → REST APIs with Flask or FastAPI.
     Graph -> Bar chat using matplotlib
     
     from flask import Flask
     app = Flask(__name__)
    @app.route("/")
    def home():
        return "Hello Rajesh!"
    if __name__ == "__main__":
        app.run(debug=True)

What approaches would you use for module importation in Python?
Ans: Python supports multiple import strategies: standard imports, aliases, selective imports, and dynamic imports. Best practice is to use explicit imports or aliases for clarity, while avoiding import * to prevent namespace conflicts.
    # Import with Alias
    import numpy as np
    print(np.array([1, 2, 3]))

Have you ever made a mistake with Python? Name a few errors you should try to avoid.
Ans: 1. Indentation Errors
     2. Using is Instead of ==
     3. Not Handling Exceptions => Always wrap risky operations in try/except.
     4. Overusing import *
     
How do you stay organized when carrying out a project in Python?
Ans: 1. Project Structure
project/
├── data/
├── src/
│   ├── __init__.py
│   ├── module1.py
│   └── module2.py
├── tests/
├── requirements.txt
└── main.py
     2. Modularization
      Break code into modules and functions instead of one long script.
      Each module should handle a single responsibility (e.g., data loading, preprocessing, visualization).
     3. Version Control
     4. Documentation
        Write docstrings for functions and classes.
     5. Virtual Environments
     6. Testing
     7. Logging & Error Handling

What are yields in Python and what do they do?
Ans: yield is a keyword used inside a function to make it a generator. Instead of returning all results at once (like return does), yield produces values one at a time, pausing the function’s state between calls.

Explain how shallow copy and deep copy are different.
Ans: Shallow Copy : Creates a new object, but does not recursively copy nested objects.

     import copy
     list1 = [[1, 2], [3, 4]]
     shallow = copy.copy(list1)
     shallow[0][0] = 99
     print(list1)   # [[99, 2], [3, 4]]
     
     Deep Copy : Creates a new object and recursively copies all nested objects.
     
     import copy
     list1 = [[1, 2], [3, 4]]
     deep = copy.deepcopy(list1)
     deep[0][0] = 99
     print(list1)   # [[1, 2], [3, 4]]

Which processes are involved in memory management in Python?
Ans: All Python objects and data structures live in a private heap managed by the interpreter.
     Developers don’t directly access this heap; instead, Python’s memory manager handles allocation and deallocation.
     each object keeps a reference counter showing how many variables point to it.
     Reference counting + garbage collection ensure memory is freed when objects are no longer needed.

Name a few examples of arguments in Python?
Ans: Python supports positional, keyword, default, variable-length (*args, **kwargs), and required arguments.
     1. Positional Arguments : Values are matched to parameters in the order they’re given.
        def greet(name, age):
            print(f"Hello {name}, you are {age} years old.")
        greet("Rajesh", 35)   # Positional arguments
     2. Keyword Arguments : specify the parameter name explicitly.
        greet(age=35, name="Rajesh")   # Keyword arguments
     3. Default Arguments : Parameters can have default values if not provided. 
        def greet(name, age=30):
            print(f"Hello {name}, you are {age} years old.")
        greet("Rajesh")   # Uses default age = 30
     4. Variable-Length Arguments : *args → Collects extra positional arguments into a tuple.
        def add_numbers(*args):
            return sum(args)
        print(add_numbers(1, 2, 3, 4))   # 10
        
       **kwargs → Collects extra keyword arguments into a dictionary.
       def show_details(**kwargs):
            for key, value in kwargs.items():
                print(f"{key}: {value}")
        show_details(name="Rajesh", role="Tech Lead")
     
Would you say Python is an uninterpreted language or an interpreted language?
Ans: Its code is executed by the interpreter at runtime, which makes development faster and more interactive, though sometimes less performant compared to compiled languages.

What are the main differences between class variables and instance variables?
Ans: Class variables are shared across all instances of a class, while instance variables are unique to each object. 
     Class Variables :
       Defined inside a class but outside any methods.
       Shared across all instances of the class.
       Changing a class variable affects all objects unless it’s overridden in an instance.
     
     Instance Variables :
        Defined inside methods (usually __init__) using self.
        Unique to each object (instance).
        Changing one instance’s variable does not affect others.
        
       class Car:
        wheels = 4   # class variable
        
        def __init__(self, color):
            self.color = color   # instance variable
            
How is file deletion accomplished in Python?
Ans: file deletion is accomplished using the os module, which provides functions to interact with the operating system.

     os.remove() / os.unlink() → delete files.
     os.rmdir() → delete empty directories.
     shutil.rmtree() → delete directories with contents       
     
Can you explain what type conversion means in Python?
Ans: type conversion means changing a value from one data type to another. It’s useful when you need to perform operations that require compatible types. 
     1. Implicit Type Conversion      
     x = 10      # int
     y = 2.5     # float
     result = x + y
     2. Explicit Type Conversion
     num_str = "100"
     num_int = int(num_str)  
     
Can you explain how range and xrange are different?
Ans: range : Returns a list containing all numbers in the specified range. nums = range(1, 5)
     xrange : Returns an iterator (xrange object) that generates numbers on demand. nums = xrange(1, 5)

Explain map?
Ans: map() applies a function to each element of an iterable and returns an iterator. 
     map() returns an iterator, not a list (in Python 3).
     You often wrap it with list() or tuple() to see results.
     
     numbers = [1, 2, 3, 4]
     squared = map(lambda x: x**2, numbers)
     print(list(squared))   # [1, 4, 9, 16]

Can you outline the difference between unpickling and pickling?
Ans: Pickling is the process of serializing Python objects into a byte stream, while unpickling is the reverse process of deserializing that byte stream back into 
     Python objects. 
     Serialize object → byte stream = Pickling ; dump(), dumps()
     Deserialize byte stream → object = Unpickling ;  load(), loads()

What approach would you use to add a multi-line comment?
Ans: In Python, multi-line comments can be added using triple quotes (''' or """). 
     This is often used for docstrings, but can also serve as multi-line comments.
     
     Example:
     '''
     This is a multi-line comment.
     It can span multiple lines.
     '''
     Alternatively, you can use multiple single-line comments with # at the beginning of each line. 

Explain what packages in Python are.
Ans: A package is a way of organizing related modules into a single directory hierarchy.     
my_package/
├── __init__.py
├── module1.py
├── module2.py
└── subpackage/
    ├── __init__.py
    └── module3.py

Could you give examples of some different Python libraries?
Ans: NumPy → For numerical computations.
     Pandas → For structured data manipulation.
     Matplotlib/Seaborn → For visualization
     Scikit learn → For machine learning basics.
     PySpark/Dask → For distributed data processing.

What do you think are the main benefits of Flask?
Ans: Flask is a lightweight web framework that allows developers to build web applications quickly and easily. 
     It’s flexible, easy to learn, and has a large ecosystem of extensions for added functionality. Flask is ideal for small to medium-sized applications and APIs, 
     making it a popular choice for developers who want simplicity and control over their projects.

What are your methods for tracking your code versions?
Ans: I use Git for version control.

Which process do you use to locate bugs in code in Python?
Ans: 1. Print Statements (Quick Debugging)
     2. Using the pdb (Python Debugger)
     3. Logging. Instead of print(), use the logging module for structured debugging.
     4. Unit Testing
     5. Static Analysis Tools

Which approach do you use to make NumPy calculations?
Ans: NumPy calculations are typically accomplished using vectorized operations rather than traditional loops.

Which approach do you use for making visualizations with Num/SciPy?
Ans: NumPy/SciPy handle numerical computations, while visualization is typically done using Matplotlib or Seaborn. 
     The workflow is: compute with NumPy/SciPy → visualize with Matplotlib/Seaborn.   


       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       