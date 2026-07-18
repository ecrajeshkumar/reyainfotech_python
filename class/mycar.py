# Class: A blueprint for creating objects. It defines attributes (data) and methods (functions).

# Object: An instance of a class. Think of it as a “real-world entity” created from the blueprint.

class Car:
    # Attributes (data)
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    # Method (function inside class)
    def drive(self):
        print(f"{self.brand} {self.model} is driving...")

# Create objects
car1 = Car("Toyota", "Corolla")
car2 = Car("Tesla", "Model 3")

car1.drive()   # Output: Toyota Corolla is driving...
car2.drive()   # Output: Tesla Model 3 is driving...


class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Marks: {self.marks}")

    def is_pass(self):
        return self.marks >= 40

# Create object
s1 = Student("Rajesh", 35, 85)
s1.display_info()          # Output: Name: Rajesh, Age: 35, Marks: 85
print(s1.is_pass())        # Output: True
