
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

# Child class inherits from Animal
class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks!")

dog = Dog("Bruno")
dog.speak()   # Output: Bruno barks!
