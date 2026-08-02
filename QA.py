How would you explain the difference between tuples and lists in Python?
Ans: Lists are mutable and allow modifications, while tuples are immutable and fixed once created. Lists are used for dynamic collections, whereas tuples are used for constant data or when immutability is required.
    my_list = [1, 2, 3]. my_tuple = (1, 2, 3)
    
Explain what is meant by PEP?
Ans: PEPs are official proposals that shape Python’s evolution. They ensure the language develops in a structured, transparent, and community driven way.

What are some of Python’s key benefits?
Ans: Its syntax is simple and close to English. Used in web development, data science, AI/ML, automation, scripting, scientific computing, and more.
     Pandas, NumPy, Matplotlib, TensorFlow, PyTorch, Django, Flask — covering everything from data analysis to web apps and AI.
     Cross‑Platform Compatibility. Works well with other languages like C, C++, and Java, and integrates with databases and web services.

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
     Scikit‑learn → For machine learning basics.
     PySpark/Dask → For distributed data processing.

Which approach would you use to get rid of white spaces from Python strings?
Ans: Removing white spaces from strings can be done in several efficient ways depending on where you want to remove them.
     .strip() removes leading/trailing spaces, .replace() removes all spaces, and regex or split/join can handle complex whitespace scenarios.
     1. Use mystr.strip() → removes spaces from both ends.
        mystr.lstrip() (left side only), mystr.rstrip() (right side only).
     2. Remove all spaces
        mystr.replace(" ", "") → removes every space in the string.

Can you explain which processes are used to do run-time checking of code?
Ans: Python performs run‑time checking through dynamic type checking, exception handling, assertions, and introspection.

How does the script mode differ from the interactive mode?
Ans: Interactive mode lets you run Python commands one at a time for quick testing, while script mode runs an entire .py file as a program. Interactive mode is great for experimentation, script mode is essential for building real applications.

Are you aware of some Python-supported modes for processing files?
Ans: Python supports several file processing modes, which determine how a file is opened and what operations you can perform on it. These modes are passed as a string argument to the built‑in open() function. "r", "rb", "w", "wb", "a", "ab", "r+" (Read and write. File must exist.)
    "w+" → Write and read. Creates new file or overwrites existing. "a+" → Append and read. Creates file if it doesn’t exist.
   
Explain what a unit test is in Python.
Ans: Python has a built‑in unittest module, and popular alternatives like pytest. 

Explain what docstring is in Python.
Ans: A docstring in Python is a string literal placed inside a module, class, or function to document its purpose. It can be accessed at run time via .__doc__ or help(), making it a standard way to embed documentation directly in code.”

What do you understand by negative index?
Ans: Negative indexing in Python allows you to access elements from the end of a sequence. -1 refers to the last element, -2 to the second‑last, and so on.

How would you explain the meaning of pass in Python?
Ans: pass is a no‑operation statement used as a placeholder to maintain valid syntax when no action is required. It’s commonly used in empty functions, classes, or control structures during development.

Can you explain what a generator is?
Ans: A generator in Python is a function that uses yield to produce values lazily, one at a time. 

Describe what the lambda function does.
Ans: A lambda function in Python is an anonymous, single‑expression function used for short, inline operations.





























