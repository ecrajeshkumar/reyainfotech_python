'''
1. Public Members:
    Public members are variables or methods that can be accessed from anywhere inside the class, outside the class or from other modules. 
    By default, all members in Python are public. They are defined without any underscore prefix (e.g., self.name).

    self.name: Declared without underscores, so it is public.
    display_name(): Public method that prints the value of the public attribute.
    emp.name: Directly accessed from outside the class, showing public members are fully accessible.
'''
class Employee:
    def __init__(self, name):
        self.name = name   # public attribute

    def display_name(self):   # public method
        print(self.name)

emp = Employee("Manoj")
emp.display_name()   # Accessible
print(emp.name)      # Accessible

'''
2. Protected members
    Protected members are variables or methods that are intended to be accessed only within the class and its subclasses. 
    They are not strictly private but should be treated as internal. In Python, protected members are defined with a single underscore prefix (e.g., self._name).

    self._age: Defined with a single underscore, marking it as protected.
    SubEmployee: Inherits from Employee and can access _age directly.
    Protected members should not be accessed outside the class hierarchy, but Python does not enforce this rule strictly.
'''
class Employee:
    def __init__(self, name, age):
        self.name = name       # public
        self._age = age        # protected
    def display_age(self):
        print("Age:", self._age)

class SubEmployee(Employee):
    def show_age(self):
        print("Age:", self._age)   # Accessible in subclass

emp = SubEmployee("Rajesh", 45)
print(emp.name)        # Public accessible
emp.show_age()         # Protected accessed through subclass
emp.display_age()

'''

3. Private members
    Private members are variables or methods that cannot be accessed directly from outside the class. They are used to restrict access and protect internal data. 
    In Python, private members are defined with a double underscore prefix (e.g., self.__salary).
    Python uses name mangling, where the interpreter internally renames the variable (for eg, __salary becomes _ClassName__salary). 
    This discourages direct access from outside the class, although it does not create strict privacy like other languages.

'''

class Employee2:
    def __init__(self, name, age, salary):
        self.name = name          # public
        self._age = age           # protected
        self.__salary = salary    # private

    def show_salary(self):
        print("Salary:", self.__salary)

emp = Employee2("Rakesh", 20, 60000)
print(emp.name)          # Public accessible
print(emp._age)          # protected member
# print(emp.__salary)    # Error: Not accessible directly private member
emp.show_salary()        # Accessing private correctly

